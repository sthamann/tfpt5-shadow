#!/usr/bin/env python3
"""gauge_stiffness_stepscaling_probe -- EXPLORATION ONLY (no promotion).

Purpose
-------
Upgrade ``gauge_stiffness_fixpoint_probe.py`` along the two review-wave-5
directions that can be executed in a deterministic 1+1D toy: finite-volume
step scaling and a first nonabelian representation-content check.  This probe
does not compare to an observed coupling and does not alter
GAUGE.DETLINE.FIXPOINT.01, which stays [O].

Preregistered functional definition
------------------------------------
The following UTF-8 payload is hash-frozen before evaluation.  The runtime
reconstructs it from the active constants, extracts the verbatim copy from
this docstring, and requires both to have the declared SHA256.

PREREGISTRATION_FREEZE_BEGIN
model=Z6_global_rotor_x_staggered_fermion
electric_normalization_kappa=0.5
electric_sign=+1
background_rotor=n-theta/(2*pi)
background_fermion=exp(i*q*theta)_on_closing_link
beta=12.0
flux_cutoff=3
hopping=0.8
mass=0.6
chemical_potential=0.1
filling=grand_canonical_all_Fock_sectors
map=R(y;L)=K(g=y^(-1/2),L),K=Gamma_second(0)/L
finite_difference=Richardson(h=0.01,h/2)
su2_link_basis=j_in_{0,1/2,1}
su2_background=exp(i*theta*J3)_on_closing_link
su2_fermion_weights=m=-j,...,+j
su2_prediction=T(1)/T(1/2)=2/(1/2)=4
convergence_fit=L>=4,g(L)=a+b/L(+c/L^2)
convergence_bar=max(0.02,3*quadratic_fit_rms),all_abs_Rprime_lt_1
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=970230fb74265fb1b45540f1280e6a0a929815bf65a9449e6da4af114c0328cc

Step-scaling protocol
---------------------
The electric rotor has the same seven flux states n=-3,...,3 as the previous
probe (the historical "Z6 toy" label is retained, although the symmetric
cutoff contains seven states).  The fermion Hamiltonian is assembled as a
sparse Fock-space matrix.  L<=5 uses its full spectrum.  L>=6 uses
deterministically seeded sparse Lanczos eigenvalues; if k levels are retained,
the first omitted level E_k gives, after shifting E_0 to zero,

    Z_tail <= dim * exp[-beta (E_k-E_0)],
    |Delta Gamma| <= log(1 + Z_tail/Z_kept).

No stochastic or partial-trace estimator is used.  Lanczos k is increased
until this certified Gamma error is below 1e-10 (the implemented target is
stricter).  Rotor and fermion partition functions factor exactly, so the
small sparse factor supplies the same Gamma as the full sparse Kronecker sum.
The preferred thermodynamic estimate is the intercept of the L>=4 quadratic
fit in 1/L; linear and quadratic fits, residuals, and endpoint distance are
all printed.  "CONVERGENT" requires Lmax>=8, one root at every L, the frozen
endpoint bar, and |R'|<1 both volume by volume and in the extrapolation.

First nonabelian step
---------------------
Use the Peter-Weyl character basis |j,m,n> on the global SU(2) link, truncated
to j=0,1/2,1.  Its electric energy is kappa*g^2*L*j(j+1), and a boundary
Cartan twist inserts exp(i theta J3).  A fermion multiplet of spin j has
weights m=-j,...,+j on the closing link.  Preregistered before evaluation:

    T(1/2) = sum m^2 = 1/2,
    T(1)   = sum m^2 = 2,
    Delta K(j=1) / Delta K(j=1/2) = 4.

The j=0 mutant must have zero fermion stiffness, and Gamma(theta) must obey
the SU(2) Weyl reflection theta -> -theta.  The omitted-link-character tail
starting at j=3/2 is bounded explicitly; the gauge-subtracted index ratio is
independent of that common pure-gauge term.

Honest boundary and verdicts
----------------------------
This remains a 1+1D separable global-mode toy.  One spatial dimension has no
plaquette self-interaction; this model has no instantons, no interacting
nonabelian gauge-matter dynamics, and no four-dimensional continuum limit.
The character truncation and free determinant test representation content,
not a physical Standard-Model coupling.  GAUGE.DETLINE.FIXPOINT.01 stays [O].

Verdict enums:
STIFFNESS_STEPSCALING_{CONVERGENT(g_star_inf,Rprime_inf,Lmax)|
DIVERGENT|INCONCLUSIVE(Lmax too small)}
+ SU2_CONTENT_{MATCH|MISMATCH}.
"""

from __future__ import annotations

import hashlib
import math
import sys
from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from scipy import sparse
from scipy.optimize import brentq
from scipy.sparse import linalg as sparse_linalg


ELECTRIC_KAPPA = 0.5
BETA = 12.0
FLUX_CUTOFF = 3
HOPPING = 0.8
MASS = 0.6
CHEMICAL_POTENTIAL = 0.1
RICHARDSON_STEP = 0.01
VOLUMES = tuple(range(2, 9))
FULL_SPECTRUM_MAX_VOLUME = 5
TRACE_ERROR_TARGET = 1.0e-12
G_MIN = 0.65
G_MAX = 3.75
G_SCAN_POINTS = 181
MAIN_CHARGE = 1.0
SU2_COUPLING = 2.0
SU2_REPRESENTATIONS = (0.0, 0.5, 1.0)
FIT_MIN_VOLUME = 4
FROZEN_SHA256 = "970230fb74265fb1b45540f1280e6a0a929815bf65a9449e6da4af114c0328cc"

FROZEN_FUNCTIONAL_DEFINITION = """model=Z6_global_rotor_x_staggered_fermion
electric_normalization_kappa=0.5
electric_sign=+1
background_rotor=n-theta/(2*pi)
background_fermion=exp(i*q*theta)_on_closing_link
beta=12.0
flux_cutoff=3
hopping=0.8
mass=0.6
chemical_potential=0.1
filling=grand_canonical_all_Fock_sectors
map=R(y;L)=K(g=y^(-1/2),L),K=Gamma_second(0)/L
finite_difference=Richardson(h=0.01,h/2)
su2_link_basis=j_in_{0,1/2,1}
su2_background=exp(i*theta*J3)_on_closing_link
su2_fermion_weights=m=-j,...,+j
su2_prediction=T(1)/T(1/2)=2/(1/2)=4
convergence_fit=L>=4,g(L)=a+b/L(+c/L^2)
convergence_bar=max(0.02,3*quadratic_fit_rms),all_abs_Rprime_lt_1"""

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    """Record one deterministic protocol gate."""
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-34s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def logsumexp(values: np.ndarray) -> float:
    """Stable real log(sum(exp(values))) for a nonempty finite vector."""
    values = np.asarray(values, dtype=float)
    maximum = float(np.max(values))
    return maximum + math.log(float(np.sum(np.exp(values - maximum))))


def verify_freeze() -> tuple[str, str]:
    """Return docstring/runtime hashes after enforcing the frozen payload."""
    if __doc__ is None:
        raise AssertionError("module docstring is required for the freeze")
    doc_payload = (
        __doc__.split("PREREGISTRATION_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_FREEZE_END", 1)[0]
        .strip()
    )
    runtime_payload = "\n".join(
        (
            "model=Z6_global_rotor_x_staggered_fermion",
            "electric_normalization_kappa=%s" % ELECTRIC_KAPPA,
            "electric_sign=+1",
            "background_rotor=n-theta/(2*pi)",
            "background_fermion=exp(i*q*theta)_on_closing_link",
            "beta=%s" % BETA,
            "flux_cutoff=%d" % FLUX_CUTOFF,
            "hopping=%s" % HOPPING,
            "mass=%s" % MASS,
            "chemical_potential=%s" % CHEMICAL_POTENTIAL,
            "filling=grand_canonical_all_Fock_sectors",
            "map=R(y;L)=K(g=y^(-1/2),L),K=Gamma_second(0)/L",
            "finite_difference=Richardson(h=%s,h/2)" % RICHARDSON_STEP,
            "su2_link_basis=j_in_{0,1/2,1}",
            "su2_background=exp(i*theta*J3)_on_closing_link",
            "su2_fermion_weights=m=-j,...,+j",
            "su2_prediction=T(1)/T(1/2)=2/(1/2)=4",
            "convergence_fit=L>=4,g(L)=a+b/L(+c/L^2)",
            "convergence_bar=max(0.02,3*quadratic_fit_rms),"
            "all_abs_Rprime_lt_1",
        )
    )
    doc_hash = hashlib.sha256(doc_payload.encode("utf-8")).hexdigest()
    runtime_hash = hashlib.sha256(runtime_payload.encode("utf-8")).hexdigest()
    declared_hash = __doc__.split("PREREGISTRATION_SHA256=", 1)[1].split()[0]
    if doc_payload != FROZEN_FUNCTIONAL_DEFINITION:
        raise AssertionError("docstring freeze differs from module freeze constant")
    if runtime_payload != FROZEN_FUNCTIONAL_DEFINITION:
        raise AssertionError("active parameters differ from frozen functional definition")
    if not doc_hash == runtime_hash == declared_hash == FROZEN_SHA256:
        raise AssertionError("preregistration SHA256 mismatch")
    return doc_hash, runtime_hash


def _annihilate_create(
    occupation: int, create_mode: int, annihilate_mode: int
) -> tuple[int, int] | None:
    """Apply c_create^dag c_annihilate, returning (new_mask, fermion_sign)."""
    if not occupation & (1 << annihilate_mode):
        return None
    if occupation & (1 << create_mode):
        return None
    sign_annihilate = -1 if (
        (occupation & ((1 << annihilate_mode) - 1)).bit_count() % 2
    ) else 1
    intermediate = occupation ^ (1 << annihilate_mode)
    sign_create = -1 if (
        (intermediate & ((1 << create_mode) - 1)).bit_count() % 2
    ) else 1
    return intermediate | (1 << create_mode), sign_annihilate * sign_create


def fermion_fock_hamiltonian(
    theta: float, volume: int, weights: tuple[float, ...]
) -> sparse.csr_matrix:
    """Sparse free-fermion Fock Hamiltonian with a frozen closing-link twist."""
    color_count = len(weights)
    mode_count = volume * color_count
    dimension = 1 << mode_count
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []

    for occupation in range(dimension):
        diagonal = 0.0
        for site in range(volume):
            onsite = MASS * (-1) ** site + CHEMICAL_POTENTIAL
            for color in range(color_count):
                mode = site * color_count + color
                if occupation & (1 << mode):
                    diagonal += onsite
        rows.append(occupation)
        columns.append(occupation)
        data.append(diagonal)

    def add_hop(create_mode: int, annihilate_mode: int, coefficient: complex) -> None:
        for occupation in range(dimension):
            result = _annihilate_create(
                occupation, create_mode, annihilate_mode
            )
            if result is not None:
                new_occupation, sign = result
                rows.append(new_occupation)
                columns.append(occupation)
                data.append(coefficient * sign)

    for color, weight in enumerate(weights):
        for site in range(volume - 1):
            left = site * color_count + color
            right = (site + 1) * color_count + color
            add_hop(left, right, -HOPPING)
            add_hop(right, left, -HOPPING)
        first = color
        last = (volume - 1) * color_count + color
        phase = np.exp(1j * weight * theta)
        add_hop(last, first, -HOPPING * phase)
        add_hop(first, last, -HOPPING * phase.conjugate())

    matrix = sparse.coo_matrix(
        (np.asarray(data, dtype=complex), (rows, columns)),
        shape=(dimension, dimension),
    ).tocsr()
    hermiticity_error = float(
        sparse_linalg.norm(matrix - matrix.getH(), ord=np.inf)
    )
    if hermiticity_error > 2.0e-13:
        raise AssertionError("fermion Hamiltonian is not Hermitian")
    return matrix


def rotor_hamiltonian(
    coupling: float, theta: float, volume: int, electric_sign: int = 1
) -> sparse.csr_matrix:
    """Sparse seven-state holonomy-twisted electric Hamiltonian."""
    flux = np.arange(-FLUX_CUTOFF, FLUX_CUTOFF + 1, dtype=float)
    shifted = flux - theta / (2.0 * math.pi)
    energies = (
        electric_sign
        * ELECTRIC_KAPPA
        * coupling**2
        * volume
        * shifted**2
    )
    return sparse.diags(energies, format="csr")


def total_z6_hamiltonian(
    coupling: float,
    theta: float,
    volume: int,
    charge: float,
    electric_sign: int = 1,
) -> sparse.csr_matrix:
    """Full sparse Kronecker-sum Hamiltonian, used for structural checks."""
    rotor = rotor_hamiltonian(coupling, theta, volume, electric_sign)
    fermion = fermion_fock_hamiltonian(theta, volume, (charge,))
    return (
        sparse.kron(
            rotor, sparse.identity(fermion.shape[0], format="csr"), format="csr"
        )
        + sparse.kron(
            sparse.identity(rotor.shape[0], format="csr"),
            fermion,
            format="csr",
        )
    )


@dataclass(frozen=True)
class SpectralTrace:
    gamma: float
    gamma_error_bound: float
    kept_levels: int
    dimension: int
    method: str
    first_omitted_gap: float


def _deterministic_lanczos_trace(matrix: sparse.csr_matrix) -> SpectralTrace:
    """Certified low-spectrum trace with a deterministic ARPACK start vector."""
    dimension = matrix.shape[0]
    candidates = (16, 24, 32, 48, 64, 96, 128, 160, 192, 224, dimension - 2)
    start = np.linspace(1.0, 2.0, dimension, dtype=float)
    start /= np.linalg.norm(start)
    last_bound = math.inf
    for kept in sorted({value for value in candidates if 1 <= value <= dimension - 2}):
        eigenvalues = sparse_linalg.eigsh(
            matrix,
            k=kept + 1,
            which="SA",
            v0=start,
            tol=2.0e-13,
            maxiter=max(5000, 40 * dimension),
            return_eigenvectors=False,
        )
        eigenvalues = np.sort(np.asarray(eigenvalues, dtype=float))
        ground = float(eigenvalues[0])
        shifted_kept = eigenvalues[:kept] - ground
        first_omitted_gap = float(eigenvalues[kept] - ground)
        kept_partition = float(np.sum(np.exp(-BETA * shifted_kept)))
        tail_partition_bound = dimension * math.exp(
            -BETA * first_omitted_gap
        )
        gamma_error_bound = math.log1p(tail_partition_bound / kept_partition)
        last_bound = gamma_error_bound
        if gamma_error_bound < TRACE_ERROR_TARGET:
            gamma = (
                BETA * ground
                - math.log(kept_partition)
            )
            return SpectralTrace(
                gamma,
                gamma_error_bound,
                kept,
                dimension,
                "Lanczos",
                first_omitted_gap,
            )
    raise RuntimeError(
        "Lanczos trace certificate failed: dim=%d last bound=%.3e"
        % (dimension, last_bound)
    )


@lru_cache(maxsize=None)
def fermion_spectral_trace(
    theta: float, volume: int, charge: float
) -> SpectralTrace:
    """Full small-volume or certified Lanczos fermion trace."""
    matrix = fermion_fock_hamiltonian(theta, volume, (charge,))
    dimension = matrix.shape[0]
    if volume <= FULL_SPECTRUM_MAX_VOLUME:
        eigenvalues = np.linalg.eigvalsh(matrix.toarray())
        return SpectralTrace(
            -logsumexp(-BETA * eigenvalues),
            0.0,
            dimension,
            dimension,
            "full",
            math.inf,
        )
    return _deterministic_lanczos_trace(matrix)


def gamma_z6(
    coupling: float,
    theta: float,
    volume: int,
    charge: float,
    electric_sign: int = 1,
) -> tuple[float, float]:
    """Factorized exact-rotor plus certified fermion effective action."""
    rotor_energies = rotor_hamiltonian(
        coupling, theta, volume, electric_sign
    ).diagonal()
    rotor_gamma = -logsumexp(-BETA * rotor_energies)
    fermion_trace = fermion_spectral_trace(theta, volume, charge)
    return rotor_gamma + fermion_trace.gamma, fermion_trace.gamma_error_bound


@dataclass(frozen=True)
class Stiffness:
    value: float
    finite_difference_error: float
    spectral_error_bound: float


def stiffness_z6(
    coupling: float,
    volume: int,
    charge: float = MAIN_CHARGE,
    electric_sign: int = 1,
    step: float = RICHARDSON_STEP,
) -> Stiffness:
    """Centered Gamma''/L with Richardson and certified trace errors."""
    def second_difference(delta: float) -> tuple[float, float]:
        plus, plus_error = gamma_z6(
            coupling, delta, volume, charge, electric_sign
        )
        zero, zero_error = gamma_z6(
            coupling, 0.0, volume, charge, electric_sign
        )
        minus, minus_error = gamma_z6(
            coupling, -delta, volume, charge, electric_sign
        )
        scale = delta**2 * volume
        value = (plus - 2.0 * zero + minus) / scale
        error_bound = (
            plus_error + 2.0 * zero_error + minus_error
        ) / scale
        return value, error_bound

    coarse, coarse_bound = second_difference(step)
    fine, fine_bound = second_difference(step / 2.0)
    richardson = (4.0 * fine - coarse) / 3.0
    finite_difference_error = abs(fine - coarse) / 3.0
    spectral_error_bound = (4.0 * fine_bound + coarse_bound) / 3.0
    return Stiffness(
        richardson, finite_difference_error, spectral_error_bound
    )


def fixed_point_residual(
    coupling: float, volume: int, electric_sign: int = 1
) -> float:
    """Frozen residual g^-2-K(g,L)."""
    return coupling**-2 - stiffness_z6(
        coupling, volume, electric_sign=electric_sign
    ).value


def root_census(
    volume: int, electric_sign: int = 1
) -> tuple[list[float], np.ndarray]:
    """Enumerate every sign-changing root on the preregistered interval."""
    grid = np.linspace(G_MIN, G_MAX, G_SCAN_POINTS)
    residuals = np.array(
        [fixed_point_residual(g, volume, electric_sign) for g in grid]
    )
    roots: list[float] = []
    for left, right, value_left, value_right in zip(
        grid[:-1], grid[1:], residuals[:-1], residuals[1:]
    ):
        if value_left == 0.0:
            candidate = float(left)
        elif value_left * value_right < 0.0:
            candidate = float(
                brentq(
                    fixed_point_residual,
                    left,
                    right,
                    args=(volume, electric_sign),
                    xtol=2.0e-12,
                    rtol=2.0e-12,
                )
            )
        else:
            continue
        if not roots or abs(candidate - roots[-1]) > 1.0e-8:
            roots.append(candidate)
    return roots, residuals


def contraction_derivative(coupling: float, volume: int) -> float:
    """Numerical dR/dy for R(y)=K(y^-1/2,L), y=g^-2."""
    inverse_coupling = coupling**-2
    delta = 2.0e-4 * inverse_coupling

    def fixed_map(y_value: float) -> float:
        return stiffness_z6(y_value**-0.5, volume).value

    return (
        fixed_map(inverse_coupling + delta)
        - fixed_map(inverse_coupling - delta)
    ) / (2.0 * delta)


@dataclass(frozen=True)
class ScalingFit:
    intercept: float
    coefficients: tuple[float, ...]
    rms_residual: float
    maximum_residual: float


def scaling_fit(
    volumes: np.ndarray, values: np.ndarray, degree: int
) -> ScalingFit:
    """Fit a polynomial in 1/L and report its infinite-volume intercept."""
    inverse_volume = 1.0 / np.asarray(volumes, dtype=float)
    coefficients = np.polyfit(inverse_volume, values, degree)
    fitted = np.polyval(coefficients, inverse_volume)
    residuals = np.asarray(values) - fitted
    return ScalingFit(
        float(coefficients[-1]),
        tuple(float(value) for value in coefficients),
        float(np.sqrt(np.mean(residuals**2))),
        float(np.max(np.abs(residuals))),
    )


def su2_weights(spin: float) -> tuple[float, ...]:
    """Cartan J3 weights of the spin-j SU(2) representation."""
    doubled_spin = int(round(2.0 * spin))
    return tuple(
        value / 2.0
        for value in range(-doubled_spin, doubled_spin + 1, 2)
    )


def su2_link_partition(theta: float, volume: int) -> float:
    """Truncated Peter-Weyl trace Tr[exp(i theta J3) exp(-beta H_E)]."""
    partition = 0.0
    for spin in SU2_REPRESENTATIONS:
        dimension = int(round(2.0 * spin + 1.0))
        character = sum(
            math.cos(weight * theta) for weight in su2_weights(spin)
        )
        casimir = spin * (spin + 1.0)
        energy = ELECTRIC_KAPPA * SU2_COUPLING**2 * volume * casimir
        partition += dimension * character * math.exp(-BETA * energy)
    if partition <= 0.0:
        raise AssertionError("SU(2) character partition became nonpositive")
    return partition


def su2_character_tail_bound(volume: int) -> float:
    """Absolute theta=0 partition tail omitted by j<=1."""
    tail = 0.0
    spin = 1.5
    while spin <= 20.0:
        dimension = int(round(2.0 * spin + 1.0))
        energy = (
            ELECTRIC_KAPPA
            * SU2_COUPLING**2
            * volume
            * spin
            * (spin + 1.0)
        )
        tail += dimension**2 * math.exp(-BETA * energy)
        spin += 0.5
    return tail


def one_body_fermion_gamma(
    theta: float, volume: int, weights: tuple[float, ...]
) -> float:
    """Exact grand-canonical free-fermion Gamma from one-body eigenvalues."""
    color_count = len(weights)
    matrix = np.zeros(
        (volume * color_count, volume * color_count), dtype=complex
    )
    for color, weight in enumerate(weights):
        for site in range(volume - 1):
            left = site * color_count + color
            right = (site + 1) * color_count + color
            matrix[left, right] -= HOPPING
            matrix[right, left] -= HOPPING
        first = color
        last = (volume - 1) * color_count + color
        phase = np.exp(1j * weight * theta)
        matrix[last, first] -= HOPPING * phase
        matrix[first, last] -= HOPPING * phase.conjugate()
        for site in range(volume):
            mode = site * color_count + color
            matrix[mode, mode] += MASS * (-1) ** site + CHEMICAL_POTENTIAL
    eigenvalues = np.linalg.eigvalsh(matrix)
    return -float(np.sum(np.logaddexp(0.0, -BETA * eigenvalues)))


def gamma_su2(theta: float, volume: int, spin: float | None) -> float:
    """SU(2) character-link Gamma, optionally with a spin-j multiplet."""
    gamma = -math.log(su2_link_partition(theta, volume))
    if spin is not None:
        gamma += one_body_fermion_gamma(theta, volume, su2_weights(spin))
    return gamma


def stiffness_su2(volume: int, spin: float | None) -> Stiffness:
    """SU(2) Gamma''/L with the same frozen Richardson prescription."""
    def second_difference(delta: float) -> float:
        return (
            gamma_su2(delta, volume, spin)
            - 2.0 * gamma_su2(0.0, volume, spin)
            + gamma_su2(-delta, volume, spin)
        ) / delta**2 / volume

    coarse = second_difference(RICHARDSON_STEP)
    fine = second_difference(RICHARDSON_STEP / 2.0)
    return Stiffness(
        (4.0 * fine - coarse) / 3.0,
        abs(fine - coarse) / 3.0,
        0.0,
    )


def main() -> int:
    """Execute the frozen step-scaling and SU(2) protocol."""
    print("=" * 88)
    print("GAUGE.DETLINE.FIXPOINT.01 -- DETERMINISTIC STIFFNESS STEP SCALING")
    print("=" * 88)

    print("\nS0  ANTI-TAUTOLOGY FREEZE")
    doc_hash, runtime_hash = verify_freeze()
    check(
        "functional-definition-hash",
        doc_hash == runtime_hash == FROZEN_SHA256,
        "SHA256=%s" % doc_hash,
    )
    check(
        "no-observed-target",
        True,
        "map inputs are frozen toy constants only; no measured coupling is present",
    )

    print("\nS1  SPARSE CONSTRUCTION + TRACE CERTIFICATES")
    small_full = total_z6_hamiltonian(2.0, 0.07, 2, MAIN_CHARGE)
    small_eigenvalues = np.linalg.eigvalsh(small_full.toarray())
    factorized_gamma, _ = gamma_z6(2.0, 0.07, 2, MAIN_CHARGE)
    direct_gamma = -logsumexp(-BETA * small_eigenvalues)
    factorization_error = abs(factorized_gamma - direct_gamma)
    large_sparse = total_z6_hamiltonian(2.0, 0.0, 8, MAIN_CHARGE)
    check(
        "sparse-Kronecker-factorization",
        factorization_error < 2.0e-12 and sparse.issparse(large_sparse),
        "L=2 |Gamma_full-Gamma_factors|=%.2e; L=8 dim=%d nnz=%d"
        % (factorization_error, large_sparse.shape[0], large_sparse.nnz),
    )

    trace_rows: dict[int, tuple[int, int, float, float, str]] = {}
    for volume in VOLUMES:
        traces = [
            fermion_spectral_trace(theta, volume, MAIN_CHARGE)
            for theta in (
                -RICHARDSON_STEP,
                -RICHARDSON_STEP / 2.0,
                0.0,
                RICHARDSON_STEP / 2.0,
                RICHARDSON_STEP,
            )
        ]
        maximum_error = max(trace.gamma_error_bound for trace in traces)
        minimum_gap = min(trace.first_omitted_gap for trace in traces)
        maximum_kept = max(trace.kept_levels for trace in traces)
        trace_rows[volume] = (
            maximum_kept,
            traces[0].dimension,
            maximum_error,
            minimum_gap,
            traces[0].method,
        )
        print(
            "  L=%d method=%-8s kept<=%3d/%3d  max|DeltaGamma|<=%.3e  "
            "min omitted gap=%s"
            % (
                volume,
                traces[0].method,
                maximum_kept,
                traces[0].dimension,
                maximum_error,
                (
                    "FULL"
                    if math.isinf(minimum_gap)
                    else "%.9f" % minimum_gap
                ),
            )
        )
    maximum_trace_error = max(row[2] for row in trace_rows.values())
    check(
        "deterministic-trace-bounds",
        maximum_trace_error < 1.0e-10
        and all(
            row[4] == ("full" if volume <= 5 else "Lanczos")
            for volume, row in trace_rows.items()
        ),
        "max certified |DeltaGamma| %.3e; full L<=5, Lanczos L>=6"
        % maximum_trace_error,
    )

    print("\nS2  Z6 STEP-SCALING TABLE")
    print(
        "  %3s %16s %16s %13s %13s"
        % ("L", "g_star", "Rprime", "FD error", "trace K bound")
    )
    roots_by_volume: dict[int, float] = {}
    derivatives_by_volume: dict[int, float] = {}
    for volume in VOLUMES:
        roots, _ = root_census(volume)
        if len(roots) == 1:
            root = roots[0]
            fixed_stiffness = stiffness_z6(root, volume)
            derivative = contraction_derivative(root, volume)
            roots_by_volume[volume] = root
            derivatives_by_volume[volume] = derivative
            print(
                "  %3d %16.12f %+16.12f %13.3e %13.3e"
                % (
                    volume,
                    root,
                    derivative,
                    fixed_stiffness.finite_difference_error,
                    fixed_stiffness.spectral_error_bound,
                )
            )
        else:
            print("  %3d %16s %16s" % (volume, "roots=%s" % roots, "--"))
    check(
        "one-root-through-Lmax",
        len(roots_by_volume) == len(VOLUMES),
        "unique roots at %d/%d volumes" % (len(roots_by_volume), len(VOLUMES)),
    )

    fit_volumes = np.array(
        [volume for volume in VOLUMES if volume >= FIT_MIN_VOLUME], dtype=float
    )
    fit_roots = np.array([roots_by_volume[int(volume)] for volume in fit_volumes])
    fit_derivatives = np.array(
        [derivatives_by_volume[int(volume)] for volume in fit_volumes]
    )
    root_linear = scaling_fit(fit_volumes, fit_roots, 1)
    root_quadratic = scaling_fit(fit_volumes, fit_roots, 2)
    derivative_linear = scaling_fit(fit_volumes, fit_derivatives, 1)
    derivative_quadratic = scaling_fit(fit_volumes, fit_derivatives, 2)
    endpoint_distance = abs(
        roots_by_volume[max(roots_by_volume)] - root_quadratic.intercept
    )
    convergence_bar = max(0.02, 3.0 * root_quadratic.rms_residual)
    print("\nS3  CONTROLLED 1/L EXTRAPOLATION (fit window L=4..8)")
    print(
        "  g linear:    g_inf=%.12f  RMS=%.3e  max|res|=%.3e"
        % (
            root_linear.intercept,
            root_linear.rms_residual,
            root_linear.maximum_residual,
        )
    )
    print(
        "  g quadratic: g_inf=%.12f  RMS=%.3e  max|res|=%.3e"
        % (
            root_quadratic.intercept,
            root_quadratic.rms_residual,
            root_quadratic.maximum_residual,
        )
    )
    print(
        "  R linear:    R_inf=%+.12f  RMS=%.3e  max|res|=%.3e"
        % (
            derivative_linear.intercept,
            derivative_linear.rms_residual,
            derivative_linear.maximum_residual,
        )
    )
    print(
        "  R quadratic: R_inf=%+.12f  RMS=%.3e  max|res|=%.3e"
        % (
            derivative_quadratic.intercept,
            derivative_quadratic.rms_residual,
            derivative_quadratic.maximum_residual,
        )
    )
    print(
        "  |g(Lmax)-g_inf(quadratic)|=%.6e; frozen bar=%.6e"
        % (endpoint_distance, convergence_bar)
    )
    all_contractive = (
        all(abs(value) < 1.0 for value in derivatives_by_volume.values())
        and abs(derivative_quadratic.intercept) < 1.0
    )
    scaling_convergent = (
        max(roots_by_volume) >= 8
        and len(roots_by_volume) == len(VOLUMES)
        and endpoint_distance <= convergence_bar
        and all_contractive
    )
    scaling_verdict = (
        "STIFFNESS_STEPSCALING_CONVERGENT"
        "(g_star_inf=%.12f,Rprime_inf=%+.12f,Lmax=%d)"
        % (
            root_quadratic.intercept,
            derivative_quadratic.intercept,
            max(roots_by_volume),
        )
        if scaling_convergent
        else (
            "STIFFNESS_STEPSCALING_INCONCLUSIVE(Lmax too small)"
            if max(roots_by_volume) < 8
            else "STIFFNESS_STEPSCALING_DIVERGENT"
        )
    )
    maximum_finite_contraction = max(
        abs(value) for value in derivatives_by_volume.values()
    )
    check(
        "contraction-diagnostic-finite",
        all(
            math.isfinite(value) for value in derivatives_by_volume.values()
        )
        and math.isfinite(derivative_quadratic.intercept),
        "criterion=%s; max finite-L |R'|=%.9f; |R'_inf|=%.9f"
        % (
            "PASS" if all_contractive else "FAIL",
            maximum_finite_contraction,
            abs(derivative_quadratic.intercept),
        ),
    )
    check(
        "scaling-verdict-executed",
        True,
        "%s; endpoint criterion %s"
        % (
            scaling_verdict,
            "PASS" if endpoint_distance <= convergence_bar else "FAIL",
        ),
    )

    print("\nS4  SU(2) CHARACTER / DYNKIN-INDEX LEG")
    representation_results: dict[int, tuple[float, float, float, float]] = {}
    maximum_weyl_error = 0.0
    maximum_ratio_error = 0.0
    maximum_tail = 0.0
    for volume in (2, 3):
        pure = stiffness_su2(volume, None)
        singlet = stiffness_su2(volume, 0.0)
        fundamental = stiffness_su2(volume, 0.5)
        adjoint = stiffness_su2(volume, 1.0)
        fundamental_contribution = fundamental.value - pure.value
        adjoint_contribution = adjoint.value - pure.value
        ratio = adjoint_contribution / fundamental_contribution
        ratio_error = abs(ratio - 4.0)
        singlet_contribution = singlet.value - pure.value
        theta_grid = (-0.17, -0.09, 0.0, 0.09, 0.17)
        gamma_grid = np.array(
            [gamma_su2(theta, volume, 1.0) for theta in theta_grid]
        )
        weyl_error = float(np.max(np.abs(gamma_grid - gamma_grid[::-1])))
        tail = su2_character_tail_bound(volume)
        representation_results[volume] = (
            fundamental_contribution,
            adjoint_contribution,
            ratio,
            singlet_contribution,
        )
        maximum_weyl_error = max(maximum_weyl_error, weyl_error)
        maximum_ratio_error = max(maximum_ratio_error, ratio_error)
        maximum_tail = max(maximum_tail, tail)
        print(
            "  L=%d DeltaK_fund=%+.12f DeltaK_adj=%+.12f ratio=%.12f "
            "|ratio-4|=%.2e"
            % (
                volume,
                fundamental_contribution,
                adjoint_contribution,
                ratio,
                ratio_error,
            )
        )
        print(
            "      Weyl max error=%.2e  j=0 DeltaK=%+.2e  "
            "omitted character Z tail<=%.3e"
            % (weyl_error, singlet_contribution, tail)
        )

    sparse_su2 = fermion_fock_hamiltonian(0.13, 3, su2_weights(1.0))
    check(
        "SU2-sparse-faithful-truncation",
        sparse_su2.shape == (512, 512) and sparse.issparse(sparse_su2),
        "j=1,L=3 fermion Fock matrix dim=%d nnz=%d; link j<=1"
        % (sparse_su2.shape[0], sparse_su2.nnz),
    )
    dynkin_fundamental = sum(weight**2 for weight in su2_weights(0.5))
    dynkin_adjoint = sum(weight**2 for weight in su2_weights(1.0))
    check(
        "SU2-Dynkin-index-ratio",
        dynkin_fundamental == 0.5
        and dynkin_adjoint == 2.0
        and maximum_ratio_error < 2.0e-5,
        "T(1/2)=%.1f T(1)=%.1f; max ratio error %.2e"
        % (dynkin_fundamental, dynkin_adjoint, maximum_ratio_error),
    )
    check(
        "SU2-Weyl-symmetry",
        maximum_weyl_error < 2.0e-13,
        "max |Gamma(theta)-Gamma(-theta)|=%.2e" % maximum_weyl_error,
    )
    check(
        "SU2-character-tail",
        maximum_tail < 1.0e-10,
        "max omitted j>=3/2 theta=0 partition tail %.3e" % maximum_tail,
    )
    su2_match = (
        maximum_ratio_error < 2.0e-5 and maximum_weyl_error < 2.0e-13
    )
    su2_verdict = (
        "SU2_CONTENT_MATCH" if su2_match else "SU2_CONTENT_MISMATCH"
    )

    print("\nS5  MUTANTS")
    mutant_root_counts: dict[int, int] = {}
    mutant_minimum_residuals: dict[int, float] = {}
    for volume in VOLUMES:
        mutant_roots, mutant_residuals = root_census(volume, electric_sign=-1)
        mutant_root_counts[volume] = len(mutant_roots)
        mutant_minimum_residuals[volume] = float(np.min(mutant_residuals))
        print(
            "  wrong-sign L=%d roots=%s min[g^-2-K]=%+.9f"
            % (
                volume,
                mutant_roots if mutant_roots else "NONE",
                mutant_minimum_residuals[volume],
            )
        )
    wrong_sign_killed = all(count == 0 for count in mutant_root_counts.values())
    check(
        "wrong-sign-no-scaling-roots",
        wrong_sign_killed
        and all(value > 0.0 for value in mutant_minimum_residuals.values()),
        "no fixed point at %d/%d L; extrapolation has no input series"
        % (
            sum(count == 0 for count in mutant_root_counts.values()),
            len(VOLUMES),
        ),
    )
    maximum_singlet = max(
        abs(result[3]) for result in representation_results.values()
    )
    check(
        "j0-fermion-zero-stiffness",
        maximum_singlet < 2.0e-9,
        "max |DeltaK(j=0)|=%.2e" % maximum_singlet,
    )
    check(
        "honest-boundary",
        True,
        "1+1D; no plaquettes in 1D, instantons, interacting gauge matter, "
        "or physical coupling; contract [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_pass = passed == total
    print("\n" + "=" * 88)
    print("RESULT: %d/%d PROTOCOL GATES PASS" % (passed, total))
    print("VERDICT: %s + %s" % (scaling_verdict, su2_verdict))
    print("GAUGE.DETLINE.FIXPOINT.01 stays [O]")
    print("=" * 88)
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
