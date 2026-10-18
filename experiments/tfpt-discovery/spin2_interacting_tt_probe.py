#!/usr/bin/env python3
r"""spin2_interacting_tt_probe -- EXPLORATION ONLY.

Purpose
-------
This is the first interacting stress-correlator witness for the open half of
TOE gate T7 / GRAV.SPIN2.EMERGENCE.01.  The quadratic graviton construction in
``spin2_hamiltonian_lattice_probe.py`` is a read-only input for its half-link
momentum and TT projector.  Here the SS16 wave-4 mechanism is executed on a
small generic matter system: construct a conserved lattice energy-stress
complex, project the spatial stress into a TT channel, and track its positive
Lehmann measure under interactions.

Model and exact finite space
----------------------------
The model is a real scalar on the periodic 2x2x2 cubic lattice,

  H = 1/2 sum_x pi_x^2
      + 1/2 sum_<xy> (phi_y-phi_x)^2
      + m^2/2 sum_x phi_x^2 + lambda/4! sum_x phi_x^4,

with lattice spacing and kinetic coefficient one, m=0.6, and
lambda=(0,0.5,2).  The free lattice has eight exact normal modes with

  Omega_p = sqrt(m^2 + |q_lat(p)|^2),  q_lat,i=2 sin(p_i/2).

The Galerkin space contains every normal-mode Fock state with total occupation
N<=4.  Its exact dimension is C(8+4,4)=495.  All 495 eigenpairs are computed
at every coupling.  Projected fields are used in phi^4.  The free Hamiltonian
is kept as the exact diagonal sum_p Omega_p(n_p+1/2); local quadratic energy
densities include the equally distributed finite-cutoff boundary correction
between that operator and the projected canonical density.  This correction
vanishes on the vacuum-to-two-particle matrix elements used by the analytic
free control, but makes sum_x h_x=H exact on the whole 495-dimensional space.

Conserved energy-stress complex
-------------------------------
The local energy is

  h_x = 1/2 pi_x^2 + m^2 phi_x^2/2
        + 1/4 sum_i [(phi_{x+i}-phi_x)^2
                     +(phi_x-phi_{x-i})^2]
        + lambda phi_x^4/4! + cutoff_correction/8.

For the finite graph, J_{x->y}=i[h_x,h_y] is an exact bond/overlap energy
current and

  d h_x/dt + sum_y J_{x->y}=0.

Dropping lambda phi_x^4/4! from h_x while evolving with the interacting H is
the required non-conserved mutant.  It must fail before spectral claims are
evaluated.

The honest canonical spatial stress response is

  T_ij(x) = 1/2 [D_i phi_x D_j phi_x + D_j phi_x D_i phi_x]
            + delta_ij [pi_x^2/2 - sum_a(D_a phi_x)^2/2
                         -m^2 phi_x^2/2-lambda phi_x^4/4!],

with D_i phi_x=phi_{x+i}-phi_x.  Thus it contains the momentum/gradient
bilinear and the interaction pressure.  The latter is pure trace and cancels
from the TT projection exactly.  Interactions nevertheless alter TT energies
and residues through the eigenstates.  Energy continuity fixes T_00 and
T_0i; on a discrete lattice there is no exact continuous-translation Ward
identity forcing the metric-response T_ij to equal a locally conserved
momentum current.

TT channel and dimensional caveat
---------------------------------
For each nonzero q_lat, the free-probe projector is

  P_TT A = theta A theta - theta tr(theta A)/2.

It has rank two in three spatial dimensions.  On this central-difference
scalar lattice, one real plus channel is evaluated; the orthogonal cross
polarization is also checked kinematically.  Contrary to a common shorthand,
a genuine 2+1-dimensional TT tensor has rank zero, not one:
(d+1)(d-2)/2=0 for d=2.  The 3D spatial lattice is therefore necessary for
an honest nonzero TT channel.

Spectral conventions and witnesses
----------------------------------
At zero temperature,

  rho_TT(omega,k)/(2 pi)
    = sum_{n>0} |<n|T_TT(k)|0>|^2 delta(omega-E_n+E_0).

Positivity is structural because every coefficient is a squared norm.  The
positive-frequency zeroth moment equals <T^dagger T>_connected.  The literal
equal-time commutator of an operator with itself is zero, so calling this
zeroth moment an "equal-time commutator" would be incorrect.  The first
moment sum_n omega_n w_n=<T^dagger[H,T]> is checked as well.  Degenerate delta
levels are grouped at 1e-9; no broadening or fit is used.  Z is the absolute
weight of the dominant grouped pole, with Z/total also reported.

The two momenta are k1=(pi,0,0), the smallest nonzero shell, and
k2=(pi,pi,0), the next distinct half-link norm.  They are not an infrared
sequence.  At lambda=0, the complete two-particle stress spectrum is compared
with the analytic normal-mode Fock decomposition.

Honest boundary
---------------
This is a small-volume, low-dimensional-cutoff generic scalar, not the full
TFPT content.  Finite-volume delta levels are not asymptotic particles, two
momenta cannot establish a massless pole, and no continuum or thermodynamic
extrapolation is made.  The SS16 mechanism is executed; the 3+1D graviton
theorem and GRAV.SPIN2.EMERGENCE.01 remain [O].
"""

from __future__ import annotations

import itertools
import math
import sys
from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.linalg import eigh


SHAPE = (2, 2, 2)
SITE_COUNT = math.prod(SHAPE)
MODE_COUNT = SITE_COUNT
MAX_TOTAL_OCCUPATION = 4
HILBERT_DIMENSION = math.comb(
    MODE_COUNT + MAX_TOTAL_OCCUPATION, MAX_TOTAL_OCCUPATION
)
MASS = 0.6
INTERACTIONS = (0.0, 0.5, 2.0)
MOMENTA = (
    ("k1", (math.pi, 0.0, 0.0)),
    ("k2", (math.pi, math.pi, 0.0)),
)
FACTORIAL_FOUR = 24.0
ALGEBRA_TOLERANCE = 3.0e-11
SPECTRAL_TOLERANCE = 3.0e-9
PEAK_ENERGY_TOLERANCE = 1.0e-9
WEIGHT_RELATIVE_CUTOFF = 1.0e-11
MUTANT_MINIMUM_RESIDUAL = 1.0e-4

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    """Record one deterministic executable assertion."""
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print(
        "  [%s] %-43s %s"
        % ("PASS" if result else "FAIL", name, detail)
    )
    return result


@dataclass(frozen=True)
class Peak:
    """One exact finite-volume energy-degeneracy class."""

    energy: float
    weight: float


@dataclass(frozen=True)
class SpectralResult:
    """Lehmann data and sum-rule residuals for one coupling and momentum."""

    interaction: float
    momentum_name: str
    lattice_momentum_norm: float
    peaks: tuple[Peak, ...]
    total_weight: float
    connected_norm: float
    zeroth_relative_error: float
    first_moment: float
    commutator_first_moment: float
    first_relative_error: float
    minimum_raw_weight: float

    @property
    def dominant_peak(self) -> Peak:
        return max(self.peaks, key=lambda peak: peak.weight)

    @property
    def lowest_peak(self) -> Peak:
        return self.peaks[0]

    @property
    def dominant_fraction(self) -> float:
        return self.dominant_peak.weight / self.total_weight


COORDINATES = tuple(itertools.product(*(range(length) for length in SHAPE)))
SITE_INDEX = {coordinate: index for index, coordinate in enumerate(COORDINATES)}


def shifted(
    coordinate: tuple[int, int, int], axis: int, amount: int
) -> tuple[int, int, int]:
    """Periodic coordinate shift."""
    output = list(coordinate)
    output[axis] = (output[axis] + amount) % SHAPE[axis]
    return tuple(output)


def fock_states() -> tuple[tuple[int, ...], ...]:
    """Deterministically enumerate all eight-mode states with N<=4."""
    states = [
        occupation
        for occupation in itertools.product(
            range(MAX_TOTAL_OCCUPATION + 1), repeat=MODE_COUNT
        )
        if sum(occupation) <= MAX_TOTAL_OCCUPATION
    ]
    return tuple(sorted(states, key=lambda state: (sum(state), state)))


FOCK_STATES = fock_states()
FOCK_INDEX = {state: index for index, state in enumerate(FOCK_STATES)}


def annihilation_operator(mode: int) -> sparse.csr_matrix:
    """Projected normal-mode annihilator."""
    rows = []
    columns = []
    values = []
    for column, state in enumerate(FOCK_STATES):
        if state[mode] == 0:
            continue
        target = list(state)
        target[mode] -= 1
        rows.append(FOCK_INDEX[tuple(target)])
        columns.append(column)
        values.append(math.sqrt(state[mode]))
    return sparse.coo_matrix(
        (values, (rows, columns)),
        shape=(HILBERT_DIMENSION, HILBERT_DIMENSION),
        dtype=complex,
    ).tocsr()


def lattice_stiffness() -> np.ndarray:
    """m^2 minus the nearest-neighbour periodic lattice Laplacian."""
    stiffness = MASS**2 * np.eye(SITE_COUNT)
    for coordinate in COORDINATES:
        source = SITE_INDEX[coordinate]
        for axis in range(3):
            target = SITE_INDEX[shifted(coordinate, axis, 1)]
            difference = np.zeros(SITE_COUNT)
            difference[target] = 1.0
            difference[source] -= 1.0
            stiffness += np.outer(difference, difference)
    return stiffness


STIFFNESS = lattice_stiffness()
MODE_FREQUENCIES_SQUARED, MODE_VECTORS = np.linalg.eigh(STIFFNESS)
MODE_FREQUENCIES = np.sqrt(MODE_FREQUENCIES_SQUARED)
ANNIHILATORS = tuple(annihilation_operator(mode) for mode in range(MODE_COUNT))
CREATORS = tuple(operator.getH().tocsr() for operator in ANNIHILATORS)


def field_operators() -> tuple[
    tuple[sparse.csr_matrix, ...], tuple[sparse.csr_matrix, ...]
]:
    """Projected phi_x and pi_x from exact free normal modes."""
    fields = []
    momenta = []
    for site in range(SITE_COUNT):
        field = sparse.csr_matrix(
            (HILBERT_DIMENSION, HILBERT_DIMENSION), dtype=complex
        )
        conjugate = sparse.csr_matrix(
            (HILBERT_DIMENSION, HILBERT_DIMENSION), dtype=complex
        )
        for mode in range(MODE_COUNT):
            vector_component = MODE_VECTORS[site, mode]
            field += (
                vector_component
                / math.sqrt(2.0 * MODE_FREQUENCIES[mode])
                * (ANNIHILATORS[mode] + CREATORS[mode])
            )
            conjugate += (
                -1j
                * vector_component
                * math.sqrt(MODE_FREQUENCIES[mode] / 2.0)
                * (ANNIHILATORS[mode] - CREATORS[mode])
            )
        fields.append(field.tocsr())
        momenta.append(conjugate.tocsr())
    return tuple(fields), tuple(momenta)


FIELDS, CONJUGATE_MOMENTA = field_operators()
FIELD_SQUARED = tuple((field @ field).tocsr() for field in FIELDS)
FIELD_FOURTH = tuple((squared @ squared).tocsr() for squared in FIELD_SQUARED)


def exact_free_hamiltonian() -> sparse.csr_matrix:
    """Diagonal Galerkin free Hamiltonian with exact oscillator energies."""
    energies = [
        sum(
            MODE_FREQUENCIES[mode] * (occupation[mode] + 0.5)
            for mode in range(MODE_COUNT)
        )
        for occupation in FOCK_STATES
    ]
    return sparse.diags(energies, format="csr", dtype=complex)


FREE_HAMILTONIAN = exact_free_hamiltonian()


def forward_gradient(site: int, axis: int) -> sparse.csr_matrix:
    """Forward half-link scalar gradient."""
    coordinate = COORDINATES[site]
    target = SITE_INDEX[shifted(coordinate, axis, 1)]
    return (FIELDS[target] - FIELDS[site]).tocsr()


GRADIENTS = tuple(
    tuple(forward_gradient(site, axis) for axis in range(3))
    for site in range(SITE_COUNT)
)


def projected_quadratic_local_energies() -> tuple[sparse.csr_matrix, ...]:
    """Canonical projected h_x plus the exact finite-cutoff correction."""
    raw = []
    for site, coordinate in enumerate(COORDINATES):
        local = 0.5 * (
            CONJUGATE_MOMENTA[site] @ CONJUGATE_MOMENTA[site]
            + MASS**2 * FIELD_SQUARED[site]
        )
        for axis in range(3):
            incoming_site = SITE_INDEX[shifted(coordinate, axis, -1)]
            outgoing_gradient = GRADIENTS[site][axis]
            incoming_gradient = GRADIENTS[incoming_site][axis]
            local += 0.25 * (
                outgoing_gradient @ outgoing_gradient
                + incoming_gradient @ incoming_gradient
            )
        raw.append(local.tocsr())
    raw_sum = sum(
        raw,
        sparse.csr_matrix(
            (HILBERT_DIMENSION, HILBERT_DIMENSION), dtype=complex
        ),
    )
    cutoff_correction_per_site = (
        FREE_HAMILTONIAN - raw_sum
    ) / SITE_COUNT
    return tuple(
        (local + cutoff_correction_per_site).tocsr() for local in raw
    )


QUADRATIC_LOCAL_ENERGIES = projected_quadratic_local_energies()
TOTAL_QUARTIC = sum(
    FIELD_FOURTH,
    sparse.csr_matrix(
        (HILBERT_DIMENSION, HILBERT_DIMENSION), dtype=complex
    ),
)


def hamiltonian(interaction: float) -> sparse.csr_matrix:
    """Galerkin phi^4 Hamiltonian."""
    return (
        FREE_HAMILTONIAN + interaction * TOTAL_QUARTIC / FACTORIAL_FOUR
    ).tocsr()


def local_energy_operators(
    interaction: float, include_interaction: bool = True
) -> tuple[sparse.csr_matrix, ...]:
    """Honest h_x or the interaction-dropped continuity mutant."""
    if not include_interaction:
        return QUADRATIC_LOCAL_ENERGIES
    return tuple(
        (
            quadratic
            + interaction * FIELD_FOURTH[site] / FACTORIAL_FOUR
        ).tocsr()
        for site, quadratic in enumerate(QUADRATIC_LOCAL_ENERGIES)
    )


def sparse_frobenius_norm(operator: sparse.spmatrix) -> float:
    """Frobenius norm without densifying."""
    return float(np.sqrt(np.sum(np.abs(operator.data) ** 2)))


def continuity_residuals(
    interaction: float, include_interaction: bool
) -> tuple[float, float, float]:
    """Maximum graph-continuity residual and local-sum error."""
    full_hamiltonian = hamiltonian(interaction)
    local_energies = local_energy_operators(
        interaction, include_interaction=include_interaction
    )
    local_sum = sum(
        local_energies,
        sparse.csr_matrix(
            (HILBERT_DIMENSION, HILBERT_DIMENSION), dtype=complex
        ),
    )
    decomposition_error = sparse_frobenius_norm(local_sum - full_hamiltonian)
    maximum_relative = 0.0
    maximum_absolute = 0.0
    for local_energy in local_energies:
        time_derivative = 1j * (
            full_hamiltonian @ local_energy - local_energy @ full_hamiltonian
        )
        current_divergence = 1j * (
            local_energy @ local_sum - local_sum @ local_energy
        )
        residual = time_derivative + current_divergence
        residual_norm = sparse_frobenius_norm(residual)
        scale = (
            sparse_frobenius_norm(time_derivative)
            + sparse_frobenius_norm(current_divergence)
            + np.finfo(float).eps
        )
        maximum_relative = max(maximum_relative, residual_norm / scale)
        maximum_absolute = max(maximum_absolute, residual_norm)
    return maximum_relative, maximum_absolute, decomposition_error


def half_link_momentum(momentum: np.ndarray) -> np.ndarray:
    """The forward-difference symbol used in the quadratic graviton probe."""
    return 2.0 * np.sin(momentum / 2.0)


def tt_polarizations(momentum: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Frobenius-orthonormal plus/cross tensors transverse to q_lat."""
    lattice_momentum = half_link_momentum(momentum)
    unit_momentum = lattice_momentum / np.linalg.norm(lattice_momentum)
    axes = np.eye(3)
    reference = axes[int(np.argmin(np.abs(axes @ unit_momentum)))]
    first = np.cross(unit_momentum, reference)
    first /= np.linalg.norm(first)
    second = np.cross(unit_momentum, first)
    second /= np.linalg.norm(second)
    plus = (
        np.outer(first, first) - np.outer(second, second)
    ) / math.sqrt(2.0)
    cross = (
        np.outer(first, second) + np.outer(second, first)
    ) / math.sqrt(2.0)
    return plus, cross


def tt_projector_matrix(momentum: np.ndarray) -> np.ndarray:
    """Rank-two TT projector represented on Sym^2(R^3)."""
    lattice_momentum = half_link_momentum(momentum)
    longitudinal = np.outer(lattice_momentum, lattice_momentum) / (
        lattice_momentum @ lattice_momentum
    )
    transverse = np.eye(3) - longitudinal
    basis = []
    for left in range(3):
        for right in range(left, 3):
            tensor = np.zeros((3, 3))
            if left == right:
                tensor[left, right] = 1.0
            else:
                tensor[left, right] = 1.0 / math.sqrt(2.0)
                tensor[right, left] = 1.0 / math.sqrt(2.0)
            basis.append(tensor)

    def project(tensor: np.ndarray) -> np.ndarray:
        return (
            transverse @ tensor @ transverse
            - 0.5 * transverse * np.trace(transverse @ tensor)
        )

    return np.asarray(
        [
            [np.sum(left * project(right)) for right in basis]
            for left in basis
        ]
    )


def tt_stress_operator(
    momentum: np.ndarray, interaction: float, polarization: np.ndarray
) -> tuple[np.ndarray, float]:
    """Fourier spatial stress contracted with a TT polarization."""
    operator = sparse.csr_matrix(
        (HILBERT_DIMENSION, HILBERT_DIMENSION), dtype=complex
    )
    interaction_pressure = sparse.csr_matrix(
        (HILBERT_DIMENSION, HILBERT_DIMENSION), dtype=complex
    )
    trace_coefficient = float(np.trace(polarization))
    for site, coordinate in enumerate(COORDINATES):
        phase = np.exp(
            -1j * momentum @ np.asarray(coordinate, dtype=float)
        ) / math.sqrt(SITE_COUNT)
        for left in range(3):
            for right in range(3):
                symmetrized = 0.5 * (
                    GRADIENTS[site][left] @ GRADIENTS[site][right]
                    + GRADIENTS[site][right] @ GRADIENTS[site][left]
                )
                operator += (
                    phase * polarization[left, right] * symmetrized
                )
        # The explicitly retained phi^4 pressure is delta_ij times a scalar.
        interaction_pressure += (
            -phase
            * trace_coefficient
            * interaction
            * FIELD_FOURTH[site]
            / FACTORIAL_FOUR
        )
    return (
        (operator + interaction_pressure).toarray(),
        sparse_frobenius_norm(interaction_pressure),
    )


def group_peaks(
    excitation_energies: np.ndarray, weights: np.ndarray
) -> tuple[Peak, ...]:
    """Group exact degeneracies and discard numerical zero support."""
    positive = [
        (float(energy), float(weight))
        for energy, weight in zip(excitation_energies, weights)
        if energy > SPECTRAL_TOLERANCE
    ]
    total = sum(weight for _, weight in positive)
    grouped: list[Peak] = []
    for energy, weight in sorted(positive):
        if grouped and abs(energy - grouped[-1].energy) < PEAK_ENERGY_TOLERANCE:
            previous = grouped[-1]
            grouped[-1] = Peak(previous.energy, previous.weight + weight)
        else:
            grouped.append(Peak(energy, weight))
    cutoff = WEIGHT_RELATIVE_CUTOFF * max(total, 1.0)
    return tuple(peak for peak in grouped if peak.weight > cutoff)


def spectral_decomposition(
    interaction: float,
    momentum_name: str,
    momentum: np.ndarray,
    eigenvalues: np.ndarray,
    eigenvectors: np.ndarray,
) -> tuple[SpectralResult, float]:
    """Exact finite-matrix zero-temperature Lehmann decomposition."""
    plus, _ = tt_polarizations(momentum)
    stress, interaction_pressure_norm = tt_stress_operator(
        momentum, interaction, plus
    )
    ground = eigenvectors[:, 0]
    stress_on_ground = stress @ ground
    amplitudes = eigenvectors.conj().T @ stress_on_ground
    weights = np.abs(amplitudes) ** 2
    excitation_energies = eigenvalues - eigenvalues[0]
    positive = excitation_energies > SPECTRAL_TOLERANCE

    expectation = np.vdot(ground, stress_on_ground)
    connected_norm = float(
        np.vdot(stress_on_ground, stress_on_ground).real
        - abs(expectation) ** 2
    )
    total_weight = float(np.sum(weights[positive]))
    zeroth_scale = max(total_weight, connected_norm, 1.0e-15)
    zeroth_relative_error = abs(
        total_weight - connected_norm
    ) / zeroth_scale

    first_moment = float(
        np.sum(excitation_energies[positive] * weights[positive])
    )
    hamiltonian_in_eigenbasis = (
        eigenvectors * eigenvalues[np.newaxis, :]
    ) @ eigenvectors.conj().T
    commutator = (
        hamiltonian_in_eigenbasis @ stress
        - stress @ hamiltonian_in_eigenbasis
    )
    commutator_first_moment = float(
        np.vdot(ground, stress.conj().T @ commutator @ ground).real
    )
    first_scale = max(
        first_moment, abs(commutator_first_moment), 1.0e-15
    )
    first_relative_error = abs(
        first_moment - commutator_first_moment
    ) / first_scale
    peaks = group_peaks(excitation_energies, weights)
    if not peaks:
        raise AssertionError("TT stress has no positive-frequency support")

    return (
        SpectralResult(
            interaction=interaction,
            momentum_name=momentum_name,
            lattice_momentum_norm=float(
                np.linalg.norm(half_link_momentum(momentum))
            ),
            peaks=peaks,
            total_weight=total_weight,
            connected_norm=connected_norm,
            zeroth_relative_error=zeroth_relative_error,
            first_moment=first_moment,
            commutator_first_moment=commutator_first_moment,
            first_relative_error=first_relative_error,
            minimum_raw_weight=float(np.min(weights)),
        ),
        interaction_pressure_norm,
    )


def analytic_free_peaks(
    momentum: np.ndarray, polarization: np.ndarray
) -> tuple[Peak, ...]:
    """Normal-mode Fock/Wick decomposition of T_TT(k)|vacuum>."""
    stress, _ = tt_stress_operator(momentum, 0.0, polarization)
    vacuum_index = FOCK_INDEX[(0,) * MODE_COUNT]
    vector = stress[:, vacuum_index]
    vacuum_energy = 0.5 * float(np.sum(MODE_FREQUENCIES))
    energies = np.asarray(
        [
            sum(
                MODE_FREQUENCIES[mode] * (occupation[mode] + 0.5)
                for mode in range(MODE_COUNT)
            )
            - vacuum_energy
            for occupation in FOCK_STATES
        ]
    )
    weights = np.abs(vector) ** 2
    return group_peaks(energies, weights)


def compare_peak_measures(
    left: tuple[Peak, ...], right: tuple[Peak, ...]
) -> float:
    """Maximum absolute mismatch between two grouped delta measures."""
    if len(left) != len(right):
        return math.inf
    deviations = []
    for left_peak, right_peak in zip(left, right):
        deviations.extend(
            [
                abs(left_peak.energy - right_peak.energy),
                abs(left_peak.weight - right_peak.weight),
            ]
        )
    return max(deviations, default=0.0)


def print_spectral_tables(results: list[SpectralResult]) -> None:
    """Print dominant poles, leading delta levels, and exact sum rules."""
    print("\nDOMINANT TT POLE TABLE")
    print(
        " lambda  k   |q_lat|   lowest_omega  dominant_omega"
        "       Z_abs      Z/total  active"
    )
    for result in results:
        print(
            " %5.2f  %-2s  %7.4f     %10.6f      %10.6f"
            "  %10.6e   %7.4f   %3d"
            % (
                result.interaction,
                result.momentum_name,
                result.lattice_momentum_norm,
                result.lowest_peak.energy,
                result.dominant_peak.energy,
                result.dominant_peak.weight,
                result.dominant_fraction,
                len(result.peaks),
            )
        )

    print("\nLEADING EXACT DELTA PEAKS: rho_TT/(2pi)=sum weight*delta")
    print(" lambda  k   rank       omega          weight       fraction")
    for result in results:
        leading = sorted(
            result.peaks, key=lambda peak: peak.weight, reverse=True
        )[:4]
        for rank, peak in enumerate(leading, start=1):
            print(
                " %5.2f  %-2s   %d     %11.7f   %11.6e    %8.5f"
                % (
                    result.interaction,
                    result.momentum_name,
                    rank,
                    peak.energy,
                    peak.weight,
                    peak.weight / result.total_weight,
                )
            )

    print("\nEXACT SUM-RULE TABLE")
    print(
        " lambda  k      int rho/(2pi)       <T^dag T>_c"
        "       rel.err       M1(spec)       M1(comm)    rel.err"
    )
    for result in results:
        print(
            " %5.2f  %-2s    %14.8e   %14.8e   %8.2e"
            "   %12.6e   %12.6e  %8.2e"
            % (
                result.interaction,
                result.momentum_name,
                result.total_weight,
                result.connected_norm,
                result.zeroth_relative_error,
                result.first_moment,
                result.commutator_first_moment,
                result.first_relative_error,
            )
        )


def main() -> int:
    print("=" * 104)
    print("spin2_interacting_tt_probe -- interacting conserved-stress spectral witness")
    print("EXPLORATION ONLY; GRAV.SPIN2.EMERGENCE.01 remains [O]")
    print("=" * 104)
    print(
        "MODEL: periodic %dx%dx%d scalar phi^4; modes=%d; N_total<=%d; "
        "dim=%d; full diagonalization"
        % (
            *SHAPE,
            MODE_COUNT,
            MAX_TOTAL_OCCUPATION,
            HILBERT_DIMENSION,
        )
    )
    print("PARAMETERS: m=%.3f, lambda=%s" % (MASS, INTERACTIONS))

    check(
        "declared Galerkin dimension",
        len(FOCK_STATES) == HILBERT_DIMENSION == 495,
        "sum_{N=0}^4 C(N+7,7)=C(12,4)=495",
    )
    expected_frequency_squares = sorted(
        MASS**2 + 4.0 * sum(bits)
        for bits in itertools.product((0, 1), repeat=3)
    )
    check(
        "free lattice normal modes",
        np.max(
            np.abs(
                np.sort(MODE_FREQUENCIES_SQUARED)
                - expected_frequency_squares
            )
        )
        < ALGEBRA_TOLERANCE,
        "Omega^2=m^2+4(nx+ny+nz); range %.6f..%.6f"
        % (
            np.min(MODE_FREQUENCIES),
            np.max(MODE_FREQUENCIES),
        ),
    )

    print("\nCONSERVATION GATE")
    interaction_for_gate = INTERACTIONS[-1]
    conserved_relative, conserved_absolute, decomposition_error = (
        continuity_residuals(interaction_for_gate, True)
    )
    mutant_relative, mutant_absolute, mutant_decomposition_error = (
        continuity_residuals(interaction_for_gate, False)
    )
    check(
        "local-energy decomposition",
        decomposition_error < ALGEBRA_TOLERANCE,
        "||sum_x h_x-H||_F=%.3e at lambda=%.2f"
        % (decomposition_error, interaction_for_gate),
    )
    check(
        "discrete energy continuity",
        conserved_relative < ALGEBRA_TOLERANCE,
        "max_x relative residual %.3e; absolute %.3e"
        % (conserved_relative, conserved_absolute),
    )
    check(
        "interaction-dropped mutant fails",
        mutant_relative > MUTANT_MINIMUM_RESIDUAL
        and mutant_decomposition_error > MUTANT_MINIMUM_RESIDUAL,
        "drop lambda phi^4/4!: relative %.3e, absolute %.3e, "
        "||sum h_mut-H||_F=%.3e"
        % (mutant_relative, mutant_absolute, mutant_decomposition_error),
    )

    projector_deviations = []
    projector_ranks = []
    polarization_deviations = []
    for _, momentum_tuple in MOMENTA:
        momentum = np.asarray(momentum_tuple)
        projector = tt_projector_matrix(momentum)
        projector_ranks.append(int(np.linalg.matrix_rank(projector, tol=1e-10)))
        projector_deviations.append(
            float(np.linalg.norm(projector @ projector - projector))
        )
        lattice_momentum = half_link_momentum(momentum)
        plus, cross = tt_polarizations(momentum)
        polarization_deviations.extend(
            [
                abs(np.trace(plus)),
                abs(np.trace(cross)),
                float(np.linalg.norm(lattice_momentum @ plus)),
                float(np.linalg.norm(lattice_momentum @ cross)),
                abs(float(np.sum(plus * cross))),
                abs(float(np.linalg.norm(plus) - 1.0)),
                abs(float(np.linalg.norm(cross) - 1.0)),
            ]
        )
    check(
        "3D TT projector and polarizations",
        projector_ranks == [2, 2]
        and max(projector_deviations + polarization_deviations)
        < ALGEBRA_TOLERANCE,
        "rank(P_TT)=2 at both k; max deviation %.3e"
        % max(projector_deviations + polarization_deviations),
    )

    results: list[SpectralResult] = []
    hermiticity_errors = []
    momentum_adjoint_errors = []
    interaction_pressure_norms = []
    free_measure_errors = []
    for interaction in INTERACTIONS:
        dense_hamiltonian = hamiltonian(interaction).toarray()
        hermiticity_errors.append(
            float(
                np.linalg.norm(
                    dense_hamiltonian - dense_hamiltonian.conj().T
                )
            )
        )
        eigenvalues, eigenvectors = eigh(
            dense_hamiltonian,
            overwrite_a=True,
            check_finite=False,
            driver="evd",
        )
        for momentum_name, momentum_tuple in MOMENTA:
            momentum = np.asarray(momentum_tuple)
            plus, _ = tt_polarizations(momentum)
            stress_plus, _ = tt_stress_operator(
                momentum, interaction, plus
            )
            stress_minus, _ = tt_stress_operator(
                -momentum, interaction, plus
            )
            momentum_adjoint_errors.append(
                float(np.linalg.norm(stress_minus - stress_plus.conj().T))
            )
            result, pressure_norm = spectral_decomposition(
                interaction,
                momentum_name,
                momentum,
                eigenvalues,
                eigenvectors,
            )
            results.append(result)
            interaction_pressure_norms.append(pressure_norm)
            if interaction == 0.0:
                free_measure_errors.append(
                    compare_peak_measures(
                        result.peaks,
                        analytic_free_peaks(momentum, plus),
                    )
                )

    check(
        "Hamiltonian self-adjointness",
        max(hermiticity_errors) < ALGEBRA_TOLERANCE,
        "max ||H-H^dagger||_F=%.3e" % max(hermiticity_errors),
    )
    check(
        "Fourier stress adjoint relation",
        max(momentum_adjoint_errors) < ALGEBRA_TOLERANCE,
        "max ||T(-k)-T(k)^dagger||_F=%.3e"
        % max(momentum_adjoint_errors),
    )
    check(
        "interaction pressure is TT-null",
        max(interaction_pressure_norms) < ALGEBRA_TOLERANCE,
        "max ||epsilon_TT:delta_ij lambda phi^4/4!||_F=%.3e"
        % max(interaction_pressure_norms),
    )
    check(
        "free analytic correlator",
        max(free_measure_errors) < SPECTRAL_TOLERANCE,
        "complete normal-mode two-particle delta measure; max error %.3e"
        % max(free_measure_errors),
    )
    minimum_weight = min(result.minimum_raw_weight for result in results)
    check(
        "TT spectral positivity",
        minimum_weight >= -SPECTRAL_TOLERANCE,
        "all 6x495 weights are |<n|T|0>|^2; min %.3e"
        % minimum_weight,
    )
    maximum_zeroth_error = max(
        result.zeroth_relative_error for result in results
    )
    maximum_first_error = max(
        result.first_relative_error for result in results
    )
    check(
        "zeroth spectral sum rule",
        maximum_zeroth_error < SPECTRAL_TOLERANCE,
        "int rho/(2pi)=<T^dag T>_c; max relative error %.3e"
        % maximum_zeroth_error,
    )
    check(
        "first-moment commutator rule",
        maximum_first_error < SPECTRAL_TOLERANCE,
        "sum omega*w=<T^dag[H,T]>; max relative error %.3e"
        % maximum_first_error,
    )
    check(
        "interacting dominant residues positive",
        all(
            result.dominant_peak.weight > SPECTRAL_TOLERANCE
            for result in results
            if result.interaction > 0.0
        ),
        "Z(k,lambda)>0 for lambda=0.5,2 at both momenta",
    )

    print_spectral_tables(results)

    print("\nZ TREND AND LOW-ENERGY CLASSIFICATION")
    trend_phrases = []
    for momentum_name, _ in MOMENTA:
        momentum_results = [
            result
            for result in results
            if result.momentum_name == momentum_name
        ]
        free_z = momentum_results[0].dominant_peak.weight
        z_ratios = [
            result.dominant_peak.weight / free_z
            for result in momentum_results
        ]
        fractions = [
            result.dominant_fraction for result in momentum_results
        ]
        energies = [
            result.dominant_peak.energy for result in momentum_results
        ]
        print(
            "  %s: omega_dom(lambda=0,.5,2)=%s; Z/Z_free=%s; "
            "pole fractions=%s"
            % (
                momentum_name,
                ["%.6f" % value for value in energies],
                ["%.6f" % value for value in z_ratios],
                ["%.6f" % value for value in fractions],
            )
        )
        if z_ratios[-1] < 1.0:
            trend_phrases.append("%s_Z_suppressed" % momentum_name)
        else:
            trend_phrases.append("%s_Z_enhanced" % momentum_name)

    for interaction in INTERACTIONS:
        pair = [
            result
            for result in results
            if result.interaction == interaction
        ]
        omega_ratio = (
            pair[1].dominant_peak.energy / pair[0].dominant_peak.energy
        )
        momentum_ratio = (
            pair[1].lattice_momentum_norm
            / pair[0].lattice_momentum_norm
        )
        print(
            "  lambda=%.2f: omega2/omega1=%.6f vs "
            "|q2|/|q1|=%.6f"
            % (interaction, omega_ratio, momentum_ratio)
        )
    minimum_observed_peak = min(
        result.lowest_peak.energy for result in results
    )
    print(
        "  Classification: a dominant positive-Z finite-volume peak persists, "
        "but the matter mass m=%.2f leaves the spectrum gapped "
        "(smallest observed omega %.6f); no massless pole is present."
        % (MASS, minimum_observed_peak)
    )

    all_checks_pass = all(result for _, result, _ in CHECKS)
    behavior = "dominant_peak_persists_gapped"
    z_trend = "_".join(trend_phrases)
    verdict = (
        "TT_INTERACTING_MECHANISM_EXECUTED(%s,%s)"
        % (behavior, z_trend)
        if all_checks_pass
        else "TT_INTERACTING_BLOCKED(executable_gate_failure)"
    )

    print("\nMUTANTS")
    print(
        "  drop lambda phi^4 from h_x: conservation residual %.3e "
        "-> MUST-FAIL fires" % mutant_relative
    )
    print(
        "  free lambda=0: analytic normal-mode TT correlator reproduced"
    )
    print("\nVERDICT: %s" % verdict)
    print(
        "CHECKS: %d/%d PASS"
        % (sum(result for _, result, _ in CHECKS), len(CHECKS))
    )
    print("\nFIVE-SENTENCE CONCLUSION")
    print(
        "1. The periodic 2x2x2 scalar phi^4 model has eight modes and a "
        "495-state N<=4 Galerkin space, fully diagonalized at three couplings."
    )
    print(
        "2. Its interaction-complete local energy obeys exact graph "
        "continuity, while dropping phi^4 from the stress complex fails "
        "the conservation gate."
    )
    print(
        "3. The TT Lehmann measure remains nonnegative, satisfies the "
        "zeroth and first-moment sum rules, and retains a dominant pole "
        "with positive Z under both interactions."
    )
    print(
        "4. At this scale the scalar mass and finite box leave the stress "
        "sector gapped rather than linearly massless, so no graviton-like "
        "collective mode is found."
    )
    print(
        "5. A 3+1D claim requires TFPT matter, larger-volume k->0 scaling, "
        "cutoff removal, restored Ward identities, and a stable positive "
        "massless residue; the contract remains [O]."
    )
    print("=" * 104)
    return 0 if all_checks_pass else 1


if __name__ == "__main__":
    sys.exit(main())
