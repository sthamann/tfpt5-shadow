#!/usr/bin/env python3
r"""spin10_det16_projector_probe -- EXPLORATION ONLY.

This probe tests the number-violating determinant vertex on the complete
2^16-dimensional Fock space of one positive-chirality Spin(10) spinor.  The
45 one-body generators are the verified Clifford/Weyl construction used by
``spin10_mirror_projector_probe.py``:

    T_ab = (i/2 gamma_a gamma_b)|_16,  0 <= a < b < 10.

Let Omega^dagger = chi_1^dagger ... chi_16^dagger, with
|F> = Omega^dagger|0>, and Omega its adjoint.  In the occupation-basis
convention used here the exact partial-isometry algebra is

    Omega^dagger Omega = P_16,       Omega Omega^dagger = P_0,
    P_16 Omega^dagger = Omega^dagger = Omega^dagger P_0,
    P_0 Omega = Omega = Omega P_16,
    (Omega)^2 = (Omega^dagger)^2 = 0.

Consequently A_phi = P_0 + P_16 + exp(-i phi) Omega
+ exp(i phi) Omega^dagger obeys A_phi^2 = 2 A_phi, and
P_phi = A_phi/2 is the rank-one projector onto

    |Omega_phi> = (|0> + exp(i phi)|F>)/sqrt(2).

Thus h_mir = 1-P_phi has exact spectrum {0^1, 1^(2^16-1)}.  For disjoint
clusters every h_x is even: P_0/P_16 preserve number and Omega contains 16
fermion operators.  Even operators with disjoint fermionic support commute,
so [h_x,h_y]=0 and sum_x h_x has the unique product ground state
tensor_x |Omega_phi_x> and exact, volume-independent gap 1.  The same
statement is checked explicitly for two and three four-mode determinant
clusters (dimensions 2^8 and 2^12); the four-operator vertex is also even.

Gauge invariance is checked infinitesimally.  Each chiral-16 generator is
traceless, so det(exp(i theta T_a)) = exp(i theta tr(T_a)) = 1.  Its second
quantization annihilates both |0> and |F>, hence commutes with P_phi.  This
finite-cluster identity does not supply dynamical gauge fields, a domain-wall
geometry, or a 4D thermodynamic/volume theorem.

CONTRACT: CHIRAL4D.MIRROR.DET16.01 remains [O].

VERDICT ENUM:
  DET16_PROJECTOR_EXACT(gap=1,hopping_stability=PASS_t<=0.2_toy)
  DET16_PROJECTOR_FAILS(where)
"""

from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass

import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as spla


TOL = 2.0e-10
EIG_TOL = 2.0e-8
SPIN10_MODES = 16
TOY_CLUSTER_MODES = 4
PHI = np.pi / 7.0
HOPPING_VALUES = (0.0, 0.05, 0.1, 0.2)
CHECKS: list[bool] = []


@dataclass(frozen=True)
class LowSpectrum:
    ground_energy: float
    degeneracy: int
    gap: float
    eigenvalues: np.ndarray


def check(name: str, condition: bool, detail: str) -> bool:
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-43s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def max_abs_sparse(matrix: sp.spmatrix) -> float:
    matrix = matrix.tocsr()
    matrix.eliminate_zeros()
    return float(np.max(np.abs(matrix.data))) if matrix.nnz else 0.0


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def kron_all(operators: list[np.ndarray]) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    for operator in operators:
        result = np.kron(result, operator)
    return result


def gamma_matrices_10d() -> list[np.ndarray]:
    """Hermitian Euclidean gamma matrices, verbatim from the killed route."""
    gammas = []
    for site in range(5):
        suffix = [Z] * (4 - site)
        gammas.append(kron_all([I2] * site + [X] + suffix))
        gammas.append(kron_all([I2] * site + [Y] + suffix))
    return gammas


def positive_weyl_generators() -> tuple[list[np.ndarray], list[tuple[int, int]]]:
    """Return the 45 verified Hermitian so(10) generators in the chiral 16."""
    gammas = gamma_matrices_10d()
    clifford_deviation = max(
        np.max(
            np.abs(
                gammas[a] @ gammas[b]
                + gammas[b] @ gammas[a]
                - (
                    2.0 * np.eye(32, dtype=complex)
                    if a == b
                    else np.zeros((32, 32), dtype=complex)
                )
            )
        )
        for a in range(10)
        for b in range(10)
    )
    gamma_product = np.eye(32, dtype=complex)
    for gamma in gammas:
        gamma_product = gamma_product @ gamma
    chirality = ((-1j) ** 5) * gamma_product
    positive = np.flatnonzero(np.real(np.diag(chirality)) > 0.5)
    if len(positive) != SPIN10_MODES or clifford_deviation > TOL:
        raise RuntimeError("failed to reconstruct the positive Weyl module")
    pairs = list(itertools.combinations(range(10), 2))
    generators = [
        (0.5j * gammas[a] @ gammas[b])[np.ix_(positive, positive)]
        for a, b in pairs
    ]
    return generators, pairs


def parity_table(mode_count: int) -> np.ndarray:
    dimension = 1 << mode_count
    return np.fromiter(
        ((state.bit_count() & 1) for state in range(dimension)),
        dtype=np.int8,
        count=dimension,
    )


def second_quantize(one_body: np.ndarray) -> sp.csr_matrix:
    """Return dGamma(one_body) in the full occupation basis."""
    mode_count = one_body.shape[0]
    if one_body.shape != (mode_count, mode_count):
        raise ValueError("one-body operator must be square")
    dimension = 1 << mode_count
    all_states = np.arange(dimension, dtype=np.int64)
    parity = parity_table(mode_count)
    row_parts: list[np.ndarray] = []
    column_parts: list[np.ndarray] = []
    data_parts: list[np.ndarray] = []
    for target_mode, source_mode in zip(*np.nonzero(np.abs(one_body) > TOL)):
        occupied_source = (all_states & (1 << source_mode)) != 0
        if target_mode == source_mode:
            columns = all_states[occupied_source]
            rows = columns
            signs = np.ones(len(columns), dtype=np.int8)
        else:
            allowed = occupied_source & ((all_states & (1 << target_mode)) == 0)
            columns = all_states[allowed]
            rows = columns ^ (1 << target_mode) ^ (1 << source_mode)
            low, high = sorted((target_mode, source_mode))
            between_mask = ((1 << high) - 1) ^ ((1 << (low + 1)) - 1)
            signs = 1 - 2 * parity[columns & between_mask]
        row_parts.append(rows)
        column_parts.append(columns)
        data_parts.append(one_body[target_mode, source_mode] * signs)
    if not data_parts:
        return sp.csr_matrix((dimension, dimension), dtype=complex)
    result = sp.coo_matrix(
        (
            np.concatenate(data_parts),
            (np.concatenate(row_parts), np.concatenate(column_parts)),
        ),
        shape=(dimension, dimension),
        dtype=complex,
    ).tocsr()
    result.eliminate_zeros()
    return result


def mode_operator(mode_count: int, mode: int, dagger: bool) -> sp.csr_matrix:
    """Sparse Jordan-Wigner creation or annihilation operator."""
    dimension = 1 << mode_count
    states = np.arange(dimension, dtype=np.int64)
    occupied = (states & (1 << mode)) != 0
    allowed = ~occupied if dagger else occupied
    columns = states[allowed]
    rows = columns ^ (1 << mode)
    lower_mask = (1 << mode) - 1
    signs = 1 - 2 * parity_table(mode_count)[columns & lower_mask]
    return sp.coo_matrix(
        (signs.astype(complex), (rows, columns)),
        shape=(dimension, dimension),
    ).tocsr()


def determinant_operators(
    total_modes: int, modes: tuple[int, ...]
) -> tuple[sp.csr_matrix, sp.csr_matrix, sp.csr_matrix, sp.csr_matrix]:
    """Return local P_empty, P_full, Omega, Omega^dagger on global Fock space."""
    if tuple(sorted(modes)) != modes or len(set(modes)) != len(modes):
        raise ValueError("determinant modes must be distinct and ordered")
    dimension = 1 << total_modes
    cluster_mask = sum(1 << mode for mode in modes)
    all_states = np.arange(dimension, dtype=np.int64)
    empty_states = all_states[(all_states & cluster_mask) == 0]
    full_states = empty_states | cluster_mask

    creation_amplitudes = np.ones(len(empty_states), dtype=complex)
    for index, empty_state in enumerate(empty_states):
        state = int(empty_state)
        amplitude = 1
        for mode in reversed(modes):
            amplitude *= -1 if (state & ((1 << mode) - 1)).bit_count() & 1 else 1
            state |= 1 << mode
        if state != int(full_states[index]):
            raise RuntimeError("determinant creation state mismatch")
        creation_amplitudes[index] = amplitude

    ones = np.ones(len(empty_states), dtype=complex)
    p_empty = sp.coo_matrix(
        (ones, (empty_states, empty_states)), shape=(dimension, dimension)
    ).tocsr()
    p_full = sp.coo_matrix(
        (ones, (full_states, full_states)), shape=(dimension, dimension)
    ).tocsr()
    omega_dagger = sp.coo_matrix(
        (creation_amplitudes, (full_states, empty_states)),
        shape=(dimension, dimension),
    ).tocsr()
    omega = omega_dagger.getH().tocsr()
    return p_empty, p_full, omega, omega_dagger


def determinant_projector(
    total_modes: int,
    modes: tuple[int, ...],
    phi: float,
    normalization: float = 0.5,
) -> sp.csr_matrix:
    p_empty, p_full, omega, omega_dagger = determinant_operators(total_modes, modes)
    return (
        normalization
        * (
            p_empty
            + p_full
            + np.exp(-1j * phi) * omega
            + np.exp(1j * phi) * omega_dagger
        )
    ).tocsr()


def spin10_single_cluster() -> tuple[list[np.ndarray], sp.csr_matrix]:
    print("\nEXACT SINGLE-CLUSTER CHECKS (16 modes, Fock dimension 65536)")
    dimension = 1 << SPIN10_MODES
    full_state = dimension - 1
    modes = tuple(range(SPIN10_MODES))
    p_empty, p_full, omega, omega_dagger = determinant_operators(
        SPIN10_MODES, modes
    )
    projector = determinant_projector(SPIN10_MODES, modes, PHI)
    identity = sp.eye(dimension, format="csr", dtype=complex)
    hamiltonian = identity - projector

    algebra_deviation = max(
        max_abs_sparse(omega_dagger @ omega - p_full),
        max_abs_sparse(omega @ omega_dagger - p_empty),
        max_abs_sparse(p_full @ omega_dagger - omega_dagger),
        max_abs_sparse(omega_dagger @ p_empty - omega_dagger),
        max_abs_sparse(p_empty @ omega - omega),
        max_abs_sparse(omega @ p_full - omega),
        max_abs_sparse(omega @ omega),
        max_abs_sparse(omega_dagger @ omega_dagger),
    )
    check(
        "determinant partial-isometry algebra",
        algebra_deviation == 0.0,
        "Omega^dag Omega=P16, Omega Omega^dag=P0; max exact defect %.1e"
        % algebra_deviation,
    )

    hermitian_deviation = max_abs_sparse(projector - projector.getH())
    idempotency_deviation = max_abs_sparse(projector @ projector - projector)
    trace = complex(projector.diagonal().sum())
    support = projector[np.ix_([0, full_state], [0, full_state])].toarray()
    rank = int(np.linalg.matrix_rank(support, tol=TOL))
    check(
        "P_phi rank-one Hermitian projector",
        hermitian_deviation < TOL
        and idempotency_deviation < TOL
        and abs(trace - 1.0) < TOL
        and rank == 1,
        "rank=%d, trace=%.16g, Herm dev %.1e, idem dev %.1e"
        % (rank, trace.real, hermitian_deviation, idempotency_deviation),
    )

    omega_phi = np.zeros(dimension, dtype=complex)
    omega_phi[0] = 1.0 / np.sqrt(2.0)
    omega_phi[full_state] = np.exp(1j * PHI) / np.sqrt(2.0)
    orthogonal = np.zeros(dimension, dtype=complex)
    orthogonal[0] = 1.0 / np.sqrt(2.0)
    orthogonal[full_state] = -np.exp(1j * PHI) / np.sqrt(2.0)
    ground_residual = float(np.linalg.norm(hamiltonian @ omega_phi))
    excited_residual = float(np.linalg.norm(hamiltonian @ orthogonal - orthogonal))
    h_projector_deviation = max_abs_sparse(hamiltonian @ hamiltonian - hamiltonian)
    excited_multiplicity = dimension - rank
    check(
        "h_mir exact ground space and gap",
        ground_residual < TOL
        and excited_residual < TOL
        and h_projector_deviation < TOL
        and rank == 1,
        "spectrum {0^1,1^%d}; gap=1 exactly; residuals %.1e/%.1e"
        % (excited_multiplicity, ground_residual, excited_residual),
    )

    parity = sp.diags(
        1 - 2 * parity_table(SPIN10_MODES), format="csr", dtype=complex
    )
    parity_commutator = max_abs_sparse(projector @ parity - parity @ projector)
    check(
        "fermion parity preserved",
        parity_commutator == 0.0 and SPIN10_MODES % 2 == 0,
        "Delta N=16 is even; max [P_phi,(-1)^F] %.1e" % parity_commutator,
    )

    generators, pairs = positive_weyl_generators()
    one_body_trace_deviation = max(abs(np.trace(generator)) for generator in generators)
    theta = 0.2718281828459045
    determinant_deviation = max(
        abs(np.linalg.det(la.expm(1j * theta * generator)) - 1.0)
        for generator in generators
    )

    odd_modes = tuple(range(SPIN10_MODES - 1))
    odd_projector = determinant_projector(SPIN10_MODES, odd_modes, PHI)
    odd_parity_commutator = max_abs_sparse(
        odd_projector @ parity - parity @ odd_projector
    )

    gauge_commutator_deviation = 0.0
    vacuum_singlet_deviation = 0.0
    filled_singlet_deviation = 0.0
    odd_gauge_commutator = 0.0
    generator_hermitian_deviation = 0.0
    for generator in generators:
        fock_generator = second_quantize(generator)
        generator_hermitian_deviation = max(
            generator_hermitian_deviation,
            max_abs_sparse(fock_generator - fock_generator.getH()),
        )
        gauge_commutator_deviation = max(
            gauge_commutator_deviation,
            max_abs_sparse(projector @ fock_generator - fock_generator @ projector),
        )
        odd_gauge_commutator = max(
            odd_gauge_commutator,
            max_abs_sparse(
                odd_projector @ fock_generator - fock_generator @ odd_projector
            ),
        )
        vacuum_singlet_deviation = max(
            vacuum_singlet_deviation,
            float(np.linalg.norm(fock_generator.getcol(0).data)),
        )
        filled_singlet_deviation = max(
            filled_singlet_deviation,
            float(np.linalg.norm(fock_generator.getcol(full_state).data)),
        )

    check(
        "chiral-16 determinant-one identity",
        one_body_trace_deviation < TOL and determinant_deviation < TOL,
        "45 generators %s; max |tr T| %.1e, max |det exp(i theta T)-1| %.1e"
        % (pairs[0:1] + pairs[-1:], one_body_trace_deviation, determinant_deviation),
    )
    check(
        "Spin(10) gauge invariance of P_phi",
        generator_hermitian_deviation < TOL and gauge_commutator_deviation < TOL,
        "45 sparse dGamma(T_a); max commutator %.1e, Herm dev %.1e"
        % (gauge_commutator_deviation, generator_hermitian_deviation),
    )
    check(
        "|0> and |F> are Spin(10) singlets",
        vacuum_singlet_deviation < TOL and filled_singlet_deviation < TOL,
        "max_a norms %.1e and %.1e" % (
            vacuum_singlet_deviation,
            filled_singlet_deviation,
        ),
    )
    check(
        "odd 15-vertex destructive mutant",
        odd_parity_commutator > 0.5 and odd_gauge_commutator > 1.0e-3,
        "required failures observed: parity comm %.3g, gauge comm %.3g"
        % (odd_parity_commutator, odd_gauge_commutator),
    )
    return generators, projector


def toy_projectors(
    cluster_count: int, phases: tuple[float, ...]
) -> list[sp.csr_matrix]:
    if len(phases) != cluster_count:
        raise ValueError("one phase is required per toy cluster")
    total_modes = TOY_CLUSTER_MODES * cluster_count
    projectors = []
    for cluster, phase in enumerate(phases):
        start = TOY_CLUSTER_MODES * cluster
        modes = tuple(range(start, start + TOY_CLUSTER_MODES))
        projectors.append(determinant_projector(total_modes, modes, phase))
    return projectors


def toy_hamiltonian(
    cluster_count: int, phases: tuple[float, ...]
) -> tuple[sp.csr_matrix, list[sp.csr_matrix]]:
    total_modes = TOY_CLUSTER_MODES * cluster_count
    dimension = 1 << total_modes
    projectors = toy_projectors(cluster_count, phases)
    identity = sp.eye(dimension, format="csr", dtype=complex)
    hamiltonian = sp.csr_matrix((dimension, dimension), dtype=complex)
    for projector in projectors:
        hamiltonian = hamiltonian + identity - projector
    return hamiltonian.tocsr(), projectors


def low_spectrum(matrix: sp.csr_matrix, count: int = 12) -> LowSpectrum:
    dimension = matrix.shape[0]
    if dimension <= 512:
        eigenvalues = np.linalg.eigvalsh(matrix.toarray())
    else:
        deterministic_start = np.linspace(1.0, 2.0, dimension).astype(complex)
        deterministic_start /= np.linalg.norm(deterministic_start)
        eigenvalues = spla.eigsh(
            matrix,
            k=min(count, dimension - 2),
            which="SA",
            v0=deterministic_start,
            tol=1.0e-12,
            maxiter=20000,
            return_eigenvectors=False,
        )
        eigenvalues = np.sort(np.real(eigenvalues))
    ground = float(eigenvalues[0])
    degeneracy = int(np.sum(np.abs(eigenvalues - ground) < EIG_TOL))
    excited = eigenvalues[eigenvalues > ground + EIG_TOL]
    if len(excited) == 0:
        raise RuntimeError("low-spectrum window did not resolve an excitation")
    gap = float(excited[0] - ground)
    return LowSpectrum(ground, degeneracy, gap, eigenvalues)


def hopping_operator(cluster_count: int) -> sp.csr_matrix:
    """Open-chain flavor-diagonal hopping with unit coefficient."""
    total_modes = TOY_CLUSTER_MODES * cluster_count
    one_body = np.zeros((total_modes, total_modes), dtype=complex)
    for cluster in range(cluster_count - 1):
        for flavor in range(TOY_CLUSTER_MODES):
            left = TOY_CLUSTER_MODES * cluster + flavor
            right = TOY_CLUSTER_MODES * (cluster + 1) + flavor
            one_body[left, right] = 1.0
            one_body[right, left] = 1.0
    return second_quantize(one_body)


def so4_vector_generators() -> list[np.ndarray]:
    generators = []
    for left, right in itertools.combinations(range(TOY_CLUSTER_MODES), 2):
        generator = np.zeros(
            (TOY_CLUSTER_MODES, TOY_CLUSTER_MODES), dtype=complex
        )
        generator[left, right] = -1j
        generator[right, left] = 1j
        generators.append(generator)
    return generators


def repeated_one_body(generator: np.ndarray, cluster_count: int) -> np.ndarray:
    return la.block_diag(*([generator] * cluster_count))


def toy_multicluster_and_stability() -> dict[int, dict[float, LowSpectrum]]:
    print("\nMULTI-CLUSTER FOUR-MODE ANALOGUE")
    spectra: dict[int, dict[float, LowSpectrum]] = {}
    for cluster_count in (2, 3):
        phases = (PHI,) * cluster_count
        hamiltonian, projectors = toy_hamiltonian(cluster_count, phases)
        commutator_deviation = max(
            (
                max_abs_sparse(
                    projectors[left] @ projectors[right]
                    - projectors[right] @ projectors[left]
                )
                for left in range(cluster_count)
                for right in range(left + 1, cluster_count)
            ),
            default=0.0,
        )
        spectrum = low_spectrum(hamiltonian)
        check(
            "%d-cluster commuting-projector gap" % cluster_count,
            commutator_deviation < TOL
            and spectrum.degeneracy == 1
            and abs(spectrum.ground_energy) < EIG_TOL
            and abs(spectrum.gap - 1.0) < EIG_TOL,
            "dim=%d, max [P_x,P_y] %.1e, ground deg=%d, gap=%.12g"
            % (
                hamiltonian.shape[0],
                commutator_deviation,
                spectrum.degeneracy,
                spectrum.gap,
            ),
        )

    print("\nSTABILITY LEG: H(t)=sum_x(1-P_x)+t K on open four-mode chains")
    for cluster_count in (2, 3):
        base_hamiltonian, _projectors = toy_hamiltonian(
            cluster_count, (PHI,) * cluster_count
        )
        hopping = hopping_operator(cluster_count)
        spectra[cluster_count] = {}
        for hopping_strength in HOPPING_VALUES:
            spectrum = low_spectrum(
                (base_hamiltonian + hopping_strength * hopping).tocsr()
            )
            spectra[cluster_count][hopping_strength] = spectrum
            check(
                "stability k=%d, t=%.2f" % (cluster_count, hopping_strength),
                spectrum.degeneracy == 1 and spectrum.gap > EIG_TOL,
                "E0=% .10f, ground deg=%d, gap=%.10f"
                % (
                    spectrum.ground_energy,
                    spectrum.degeneracy,
                    spectrum.gap,
                ),
            )

    base_two, _ = toy_hamiltonian(2, (PHI, PHI))
    hopping_two = hopping_operator(2)
    covariance_deviation = 0.0
    for generator in so4_vector_generators():
        total_generator = second_quantize(repeated_one_body(generator, 2))
        covariance_deviation = max(
            covariance_deviation,
            max_abs_sparse(
                total_generator @ base_two - base_two @ total_generator
            ),
            max_abs_sparse(
                total_generator @ hopping_two - hopping_two @ total_generator
            ),
        )
    check(
        "SO(4)-covariance of toy stability leg",
        covariance_deviation < TOL,
        "max commutator of H0 or flavor-diagonal K with 6 total generators %.1e"
        % covariance_deviation,
    )

    misaligned_hamiltonian, _ = toy_hamiltonian(2, (PHI, PHI + np.pi / 5.0))
    misaligned_spectrum = low_spectrum(misaligned_hamiltonian)
    check(
        "independent per-cluster phases control",
        misaligned_spectrum.degeneracy == 1
        and abs(misaligned_spectrum.gap - 1.0) < EIG_TOL,
        "phi_2-phi_1=pi/5 remains unique with exact gap %.12g"
        % misaligned_spectrum.gap,
    )

    bad_projector = determinant_projector(
        TOY_CLUSTER_MODES,
        tuple(range(TOY_CLUSTER_MODES)),
        PHI,
        normalization=1.0 / 3.0,
    )
    bad_idempotency = max_abs_sparse(bad_projector @ bad_projector - bad_projector)
    bad_trace = complex(bad_projector.diagonal().sum())
    check(
        "non-projector normalization mutant",
        bad_idempotency > 0.1 and abs(bad_trace - 2.0 / 3.0) < TOL,
        "1/3 normalization: trace=%.12g, idempotency defect=%.12g"
        % (bad_trace.real, bad_idempotency),
    )
    return spectra


def spectator_check() -> None:
    print("\nPHYSICAL-SPECTATOR CHECK")
    mirror_modes = 2 * TOY_CLUSTER_MODES
    spectator_modes = 2
    mirror_hamiltonian, mirror_projectors = toy_hamiltonian(2, (PHI, PHI))
    spectator_identity = sp.eye(
        1 << spectator_modes, format="csr", dtype=complex
    )
    total_hamiltonian = sp.kron(
        spectator_identity, mirror_hamiltonian, format="csr"
    )
    mirror_ground_projector = (mirror_projectors[0] @ mirror_projectors[1]).tocsr()
    total_ground_projector = sp.kron(
        spectator_identity, mirror_ground_projector, format="csr"
    )
    ground_rank = int(round(float(np.real(total_ground_projector.diagonal().sum()))))
    ground_residual = max_abs_sparse(
        total_hamiltonian @ total_ground_projector
    )
    spectator_commutator = 0.0
    total_modes = mirror_modes + spectator_modes
    for mode in range(mirror_modes, total_modes):
        creation = mode_operator(total_modes, mode, dagger=True)
        spectator_commutator = max(
            spectator_commutator,
            max_abs_sparse(
                total_hamiltonian @ creation - creation @ total_hamiltonian
            ),
        )
    spectrum = low_spectrum(total_hamiltonian, count=10)
    check(
        "spectator sector untouched and zero-cost",
        ground_rank == 1 << spectator_modes
        and spectrum.degeneracy == 1 << spectator_modes
        and ground_residual < TOL
        and spectator_commutator < TOL
        and abs(spectrum.gap - 1.0) < EIG_TOL,
        "%d spectator states at E=0, [H,c_spec^dag] %.1e; mirror gap %.12g"
        % (ground_rank, spectator_commutator, spectrum.gap),
    )


def print_gap_table(spectra: dict[int, dict[float, LowSpectrum]]) -> None:
    print("\nGAP TABLE")
    print("  clusters     t              E0       degeneracy             gap")
    for cluster_count in (2, 3):
        for hopping_strength in HOPPING_VALUES:
            spectrum = spectra[cluster_count][hopping_strength]
            print(
                "  %8d  %5.2f  %14.9f  %15d  %14.9f"
                % (
                    cluster_count,
                    hopping_strength,
                    spectrum.ground_energy,
                    spectrum.degeneracy,
                    spectrum.gap,
                )
            )


def main() -> int:
    print("=" * 96)
    print("spin10_det16_projector_probe -- determinant-vertex mirror projector")
    print("EXPLORATION ONLY; CHIRAL4D.MIRROR.DET16.01 stays [O]")
    print("=" * 96)

    spin10_single_cluster()
    spectra = toy_multicluster_and_stability()
    spectator_check()
    print_gap_table(spectra)

    hopping_stable = all(
        spectrum.degeneracy == 1 and spectrum.gap > EIG_TOL
        for cluster_spectra in spectra.values()
        for spectrum in cluster_spectra.values()
    )
    if all(CHECKS) and hopping_stable:
        verdict = (
            "DET16_PROJECTOR_EXACT("
            "gap=1,hopping_stability=PASS_t<=0.2_toy)"
        )
    else:
        failed_count = len(CHECKS) - sum(CHECKS)
        verdict = "DET16_PROJECTOR_FAILS(%d_checks)" % failed_count

    print("\nVERDICT: %s" % verdict)
    print(
        "BOUNDARY: exact finite-cluster core plus the first toy stability leg only; "
        "no dynamical gauge fields, no domain-wall geometry, and no 4D volume theorem. "
        "The contract remains [O]."
    )
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("=" * 96)
    return 0 if all(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
