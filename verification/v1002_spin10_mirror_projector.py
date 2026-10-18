"""v1002 -- CHIRAL4D.MIRROR.DET16.01: DET16 rank-one projector on the
full 2^16 cluster, plus the number-preserving Casimir-route kill.

Provenance: experiments/tfpt-discovery/spin10_det16_projector_probe.py
+ spin10_mirror_projector_probe.py + spin10_multicluster_singlet_probe.py
(review wave 5, 2026-08-29).

THE POINT.  Exact finite-cluster gapping mechanism; the Casimir projector
is permanently excluded.

  [E-finite] DET16 rank-one projector on the full 2^16 cluster:
       Omega^dag Omega = P_16, Omega Omega^dag = P_0, defect 0;
       P_phi hermitian idempotent, rank 1;
       h_mir spectrum {0^1, 1^65535}, gap exactly 1;
       all 45 so(10) Fock commutators = 0 (det rho_16 = 1);
       parity commutator 0; |0> and |F> singlets.
  [N]  hopping stability on the 4-mode analogue chain: gap ~0.90
       (2 clusters) / ~0.86 (3 clusters) at t = 0.2; spectators untouched.
  [X]  KILLED number-preserving Casimir route: singlet census one 16
       = {N=0:1, N=16:1} (none at N=8); k=2 half-filling multiplicity 27;
       k=3: 1463 (census via exact Weyl alternation, |W(D5)| = 1920).
       Uniqueness fails at every cluster size.

MUST-FAIL: odd 15-vertex (parity + gauge fail); 1/3 normalization
(not a projector); vector-10 mutant; Spin(9) restriction (new unique
N=8 singlet).

HONEST SCOPE (firewall): finite-cluster identity; no dynamical gauge
fields, no domain-wall geometry, no 4D volume theorem.
CHIRAL4D.NOMIRROR.01 stays Open; MIRROR.DET16 is Candidate [C].
Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

import gc
import itertools
import math
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable

import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
import scipy.sparse.linalg as spla

from tfpt_constants import check, summary, reset


def report(name, ok, extra=""):
    check(name if not extra else "%s -- %s" % (name, extra), ok)


TOL = 2.0e-10
EIG_TOL = 2.0e-8
SPIN10_MODES = 16
TOY_CLUSTER_MODES = 4
PHI = np.pi / 7.0
HOPPING_VALUES = (0.0, 0.05, 0.1, 0.2)
SPIN10_RANK = 5
SPIN10_RHO_DOUBLED = (8, 6, 4, 2, 0)
SPIN9_RHO_DOUBLED = (7, 5, 3, 1)
COPY_COUNTS = (1, 2, 3)
EXPECTED_SPIN10_CENSUS = {
    1: {0: 1, 16: 1},
    2: {0: 1, 4: 1, 8: 1, 12: 1, 16: 27, 20: 1, 24: 1, 28: 1, 32: 1},
    3: {
        0: 1,
        4: 6,
        8: 21,
        12: 84,
        16: 747,
        20: 1374,
        24: 1463,
        28: 1374,
        32: 747,
        36: 84,
        40: 21,
        44: 6,
        48: 1,
    },
}
RankWeight = tuple[int, ...]
CoefficientPolynomial = tuple[int, ...]

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


@dataclass(frozen=True)
class LowSpectrum:
    ground_energy: float
    degeneracy: int
    gap: float
    eigenvalues: np.ndarray


def max_abs_sparse(matrix: sp.spmatrix) -> float:
    matrix = matrix.tocsr()
    matrix.eliminate_zeros()
    return float(np.max(np.abs(matrix.data))) if matrix.nnz else 0.0


def kron_all(operators: list[np.ndarray]) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    for operator in operators:
        result = np.kron(result, operator)
    return result


def gamma_matrices_10d() -> list[np.ndarray]:
    gammas = []
    for site in range(5):
        suffix = [Z] * (4 - site)
        gammas.append(kron_all([I2] * site + [X] + suffix))
        gammas.append(kron_all([I2] * site + [Y] + suffix))
    return gammas


def positive_weyl_generators():
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


def determinant_operators(total_modes: int, modes: tuple[int, ...]):
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


def spin10_single_cluster():
    print("\nEXACT SINGLE-CLUSTER CHECKS (16 modes, Fock dimension 65536)")
    dimension = 1 << SPIN10_MODES
    full_state = dimension - 1
    modes = tuple(range(SPIN10_MODES))
    p_empty, p_full, omega, omega_dagger = determinant_operators(SPIN10_MODES, modes)
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
    report(
        "DET16 [E]: determinant partial-isometry algebra",
        algebra_deviation == 0.0,
        "Omega^dag Omega=P16, Omega Omega^dag=P0; defect %.1e" % algebra_deviation,
    )

    hermitian_deviation = max_abs_sparse(projector - projector.getH())
    idempotency_deviation = max_abs_sparse(projector @ projector - projector)
    trace = complex(projector.diagonal().sum())
    support = projector[np.ix_([0, full_state], [0, full_state])].toarray()
    rank = int(np.linalg.matrix_rank(support, tol=TOL))
    report(
        "DET16 [E]: P_phi rank-one Hermitian projector",
        hermitian_deviation < TOL
        and idempotency_deviation < TOL
        and abs(trace - 1.0) < TOL
        and rank == 1,
        "rank=%d, trace=%.16g, Herm %.1e, idem %.1e"
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
    report(
        "DET16 [E]: h_mir exact ground space and gap",
        ground_residual < TOL
        and excited_residual < TOL
        and h_projector_deviation < TOL
        and rank == 1,
        "spectrum {0^1, 1^%d}; gap=1 exactly; residuals %.1e/%.1e"
        % (excited_multiplicity, ground_residual, excited_residual),
    )

    parity = sp.diags(
        1 - 2 * parity_table(SPIN10_MODES), format="csr", dtype=complex
    )
    parity_commutator = max_abs_sparse(projector @ parity - parity @ projector)
    report(
        "DET16 [E]: fermion parity preserved",
        parity_commutator == 0.0 and SPIN10_MODES % 2 == 0,
        "Delta N=16 even; max [P_phi,(-1)^F] %.1e" % parity_commutator,
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

    report(
        "DET16 [E]: chiral-16 determinant-one identity (det rho_16 = 1)",
        one_body_trace_deviation < TOL and determinant_deviation < TOL,
        "45 generators; max |tr T| %.1e, max |det exp(i theta T)-1| %.1e"
        % (one_body_trace_deviation, determinant_deviation),
    )
    report(
        "DET16 [E]: Spin(10) gauge invariance of P_phi (45 Fock commutators = 0)",
        generator_hermitian_deviation < TOL and gauge_commutator_deviation < TOL,
        "max commutator %.1e, Herm dev %.1e"
        % (gauge_commutator_deviation, generator_hermitian_deviation),
    )
    report(
        "DET16 [E]: |0> and |F> are Spin(10) singlets",
        vacuum_singlet_deviation < TOL and filled_singlet_deviation < TOL,
        "max_a norms %.1e and %.1e"
        % (vacuum_singlet_deviation, filled_singlet_deviation),
    )
    report(
        "DET16 mutant [X]: odd 15-vertex destructive mutant",
        odd_parity_commutator > 0.5 and odd_gauge_commutator > 1.0e-3,
        "parity comm %.3g, gauge comm %.3g"
        % (odd_parity_commutator, odd_gauge_commutator),
    )
    return generators, projector


def toy_projectors(cluster_count: int, phases: tuple[float, ...]):
    if len(phases) != cluster_count:
        raise ValueError("one phase is required per toy cluster")
    total_modes = TOY_CLUSTER_MODES * cluster_count
    projectors = []
    for cluster, phase in enumerate(phases):
        start = TOY_CLUSTER_MODES * cluster
        modes = tuple(range(start, start + TOY_CLUSTER_MODES))
        projectors.append(determinant_projector(total_modes, modes, phase))
    return projectors


def toy_hamiltonian(cluster_count: int, phases: tuple[float, ...]):
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
    total_modes = TOY_CLUSTER_MODES * cluster_count
    one_body = np.zeros((total_modes, total_modes), dtype=complex)
    for cluster in range(cluster_count - 1):
        for flavor in range(TOY_CLUSTER_MODES):
            left = TOY_CLUSTER_MODES * cluster + flavor
            right = TOY_CLUSTER_MODES * (cluster + 1) + flavor
            one_body[left, right] = 1.0
            one_body[right, left] = 1.0
    return second_quantize(one_body)


def so4_vector_generators():
    generators = []
    for left, right in itertools.combinations(range(TOY_CLUSTER_MODES), 2):
        generator = np.zeros((TOY_CLUSTER_MODES, TOY_CLUSTER_MODES), dtype=complex)
        generator[left, right] = -1j
        generator[right, left] = 1j
        generators.append(generator)
    return generators


def repeated_one_body(generator: np.ndarray, cluster_count: int) -> np.ndarray:
    return la.block_diag(*([generator] * cluster_count))


def toy_multicluster_and_stability():
    print("\nMULTI-CLUSTER FOUR-MODE ANALOGUE + HOPPING STABILITY")
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
        report(
            "HOPPING [N]: %d-cluster commuting-projector gap" % cluster_count,
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
            report(
                "HOPPING [N]: stability k=%d, t=%.2f" % (cluster_count, hopping_strength),
                spectrum.degeneracy == 1 and spectrum.gap > EIG_TOL,
                "E0=%.10f, ground deg=%d, gap=%.10f"
                % (spectrum.ground_energy, spectrum.degeneracy, spectrum.gap),
            )

    gap_two = spectra[2][0.2].gap
    gap_three = spectra[3][0.2].gap
    report(
        "HOPPING [N]: t=0.2 gaps 0.90 (2 clusters) / 0.86 (3 clusters)",
        abs(gap_two - 0.90) < 0.03 and abs(gap_three - 0.86) < 0.03,
        "measured gap_2=%.4f, gap_3=%.4f" % (gap_two, gap_three),
    )

    base_two, _ = toy_hamiltonian(2, (PHI, PHI))
    hopping_two = hopping_operator(2)
    covariance_deviation = 0.0
    for generator in so4_vector_generators():
        total_generator = second_quantize(repeated_one_body(generator, 2))
        covariance_deviation = max(
            covariance_deviation,
            max_abs_sparse(total_generator @ base_two - base_two @ total_generator),
            max_abs_sparse(total_generator @ hopping_two - hopping_two @ total_generator),
        )
    report(
        "HOPPING [N]: SO(4)-covariance of toy stability leg",
        covariance_deviation < TOL,
        "max commutator %.1e" % covariance_deviation,
    )

    misaligned_hamiltonian, _ = toy_hamiltonian(2, (PHI, PHI + np.pi / 5.0))
    misaligned_spectrum = low_spectrum(misaligned_hamiltonian)
    report(
        "HOPPING [N]: independent per-cluster phases control",
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
    report(
        "DET16 mutant [X]: non-projector 1/3 normalization",
        bad_idempotency > 0.1 and abs(bad_trace - 2.0 / 3.0) < TOL,
        "trace=%.12g, idempotency defect=%.12g" % (bad_trace.real, bad_idempotency),
    )
    return spectra


def spectator_check():
    print("\nPHYSICAL-SPECTATOR CHECK")
    mirror_modes = 2 * TOY_CLUSTER_MODES
    spectator_modes = 2
    mirror_hamiltonian, mirror_projectors = toy_hamiltonian(2, (PHI, PHI))
    spectator_identity = sp.eye(1 << spectator_modes, format="csr", dtype=complex)
    total_hamiltonian = sp.kron(spectator_identity, mirror_hamiltonian, format="csr")
    mirror_ground_projector = (mirror_projectors[0] @ mirror_projectors[1]).tocsr()
    total_ground_projector = sp.kron(
        spectator_identity, mirror_ground_projector, format="csr"
    )
    ground_rank = int(round(float(np.real(total_ground_projector.diagonal().sum()))))
    ground_residual = max_abs_sparse(total_hamiltonian @ total_ground_projector)
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
    report(
        "HOPPING [N]: spectator sector untouched and zero-cost",
        ground_rank == 1 << spectator_modes
        and spectrum.degeneracy == 1 << spectator_modes
        and ground_residual < TOL
        and spectator_commutator < TOL
        and abs(spectrum.gap - 1.0) < EIG_TOL,
        "%d spectator states at E=0, [H,c_spec^dag] %.1e; mirror gap %.12g"
        % (ground_rank, spectator_commutator, spectrum.gap),
    )


def spin10_chiral_weights_doubled():
    return [
        signs
        for signs in itertools.product((-1, 1), repeat=SPIN10_RANK)
        if sum(value < 0 for value in signs) % 2 == 0
    ]


def spin10_vector_weights_doubled():
    weights = []
    for coordinate in range(SPIN10_RANK):
        for sign in (-2, 2):
            weight = [0] * SPIN10_RANK
            weight[coordinate] = sign
            weights.append(tuple(weight))
    return weights


def spin9_spinor_weights_doubled():
    return list(itertools.product((-1, 1), repeat=4))


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def sign_product(signs: tuple[int, ...]) -> int:
    result = 1
    for sign in signs:
        result *= sign
    return result


def weyl_alternant_targets(rho_doubled: RankWeight, allow_all_sign_changes: bool):
    rank = len(rho_doubled)
    targets: defaultdict[RankWeight, int] = defaultdict(int)
    for permutation in itertools.permutations(range(rank)):
        permutation_determinant = permutation_sign(permutation)
        for signs in itertools.product((-1, 1), repeat=rank):
            if not allow_all_sign_changes and sum(sign < 0 for sign in signs) % 2:
                continue
            transformed_rho = tuple(
                signs[index] * rho_doubled[permutation[index]]
                for index in range(rank)
            )
            determinant = permutation_determinant * sign_product(signs)
            target = tuple(
                rho_doubled[index] - transformed_rho[index]
                for index in range(rank)
            )
            targets[target] += determinant
    return {target: coefficient for target, coefficient in targets.items() if coefficient}


def exact_singlet_census(
    weights: list[RankWeight],
    copies: int,
    rho_doubled: RankWeight,
    allow_all_sign_changes: bool,
):
    if copies < 1 or not weights:
        raise ValueError("copies and weight table must be nonempty")
    rank = len(rho_doubled)
    if any(len(weight) != rank for weight in weights):
        raise ValueError("weight rank does not match rho")
    targets = weyl_alternant_targets(rho_doubled, allow_all_sign_changes)
    minimum_reachable = [(0,) * rank]
    maximum_reachable = [(0,) * rank]
    for weight in weights:
        minimum_reachable.append(
            tuple(
                minimum_reachable[-1][index] + min(0, copies * weight[index])
                for index in range(rank)
            )
        )
        maximum_reachable.append(
            tuple(
                maximum_reachable[-1][index] + max(0, copies * weight[index])
                for index in range(rank)
            )
        )

    @lru_cache(maxsize=None)
    def coefficient_polynomial(weight_count: int, target: RankWeight):
        if any(
            target[index] < minimum_reachable[weight_count][index]
            or target[index] > maximum_reachable[weight_count][index]
            for index in range(rank)
        ):
            return ()
        if weight_count == 0:
            return (1,) if target == (0,) * rank else ()
        polynomial = [0] * (copies * weight_count + 1)
        last_weight = weights[weight_count - 1]
        for occupation in range(copies + 1):
            predecessor = tuple(
                target[index] - occupation * last_weight[index]
                for index in range(rank)
            )
            lower_polynomial = coefficient_polynomial(weight_count - 1, predecessor)
            binomial_weight = math.comb(copies, occupation)
            for degree, coefficient in enumerate(lower_polynomial):
                polynomial[degree + occupation] += binomial_weight * coefficient
        while polynomial and polynomial[-1] == 0:
            polynomial.pop()
        return tuple(polynomial)

    census = [0] * (copies * len(weights) + 1)
    for target, alternant_sign in targets.items():
        polynomial = coefficient_polynomial(len(weights), target)
        for particle_number, coefficient in enumerate(polynomial):
            census[particle_number] += alternant_sign * coefficient
    cache_entries = coefficient_polynomial.cache_info().currsize
    coefficient_polynomial.cache_clear()
    gc.collect()
    if any(multiplicity < 0 for multiplicity in census):
        raise RuntimeError("Weyl projection produced a negative multiplicity")
    return census, len(targets), cache_entries


def direct_exterior_character(weights: list[RankWeight], particle_number: int):
    rank = len(weights[0])
    sectors: list[dict[RankWeight, int]] = [
        defaultdict(int) for _ in range(particle_number + 1)
    ]
    sectors[0][(0,) * rank] = 1
    occupied = 0
    for weight in weights:
        occupied += 1
        for degree in range(min(occupied, particle_number), 0, -1):
            for old_weight, multiplicity in list(sectors[degree - 1].items()):
                new_weight = tuple(
                    old_weight[index] + weight[index] for index in range(rank)
                )
                sectors[degree][new_weight] += multiplicity
    return dict(sectors[particle_number])


def is_d5_dominant(weight: RankWeight) -> bool:
    return (
        weight[0] >= weight[1] >= weight[2] >= weight[3]
        and weight[3] >= abs(weight[4])
    )


def d5_highest_weight(character: dict[RankWeight, int]) -> RankWeight:
    dominant = [weight for weight in character if is_d5_dominant(weight)]
    return max(
        dominant,
        key=lambda weight: (
            sum(weight[index] * SPIN10_RHO_DOUBLED[index] for index in range(5)),
            weight,
        ),
    )


def nonzero_entries(census: Iterable[int]):
    return [
        (particle_number, multiplicity)
        for particle_number, multiplicity in enumerate(census)
        if multiplicity
    ]


def expected_full_census(mode_count: int, entries: dict[int, int]):
    return [entries.get(particle_number, 0) for particle_number in range(mode_count + 1)]


def run_casimir_kill():
    print("\nCASIMIR-ROUTE KILL: exact Weyl-alternant singlet census")
    weyl_order = math.factorial(5) * (2 ** 4)
    report(
        "CASIMIR [X]: |W(D5)| = 1920 (even sign changes)",
        weyl_order == 1920,
        "5! * 2^4 = %d" % weyl_order,
    )
    spinor_weights = spin10_chiral_weights_doubled()
    report(
        "CASIMIR [X]: verified chiral-16 weight table",
        len(spinor_weights) == 16
        and len(set(spinor_weights)) == 16
        and all(sum(value < 0 for value in weight) % 2 == 0 for weight in spinor_weights)
        and all(
            sum(weight[index] for weight in spinor_weights) == 0
            for index in range(5)
        ),
        "16 unique even-minus doubled weights; coordinate sums vanish",
    )
    lambda_two_character = direct_exterior_character(spinor_weights, 2)
    lambda_two_highest = d5_highest_weight(lambda_two_character)
    report(
        "CASIMIR [X]: known Lambda^2(16)=120 validation",
        sum(lambda_two_character.values()) == math.comb(16, 2)
        and lambda_two_highest == (2, 2, 2, 0, 0),
        "dimension 120; highest doubled weight %s" % (lambda_two_highest,),
    )

    censuses: dict[int, list[int]] = {}
    for copies in COPY_COUNTS:
        census, target_count, cache_entries = exact_singlet_census(
            spinor_weights,
            copies,
            SPIN10_RHO_DOUBLED,
            allow_all_sign_changes=False,
        )
        censuses[copies] = census
        expected = expected_full_census(16 * copies, EXPECTED_SPIN10_CENSUS[copies])
        report(
            "CASIMIR [X]: exact D5 alternant census k=%d" % copies,
            census == expected,
            "%d Weyl targets; %d memo states; nonzero %s"
            % (target_count, cache_entries, nonzero_entries(census)),
        )
        report(
            "CASIMIR [X]: particle-hole symmetry k=%d" % copies,
            census == list(reversed(census)),
            "m_N=m_%d-N; total projector rank %d" % (16 * copies, sum(census)),
        )

    report(
        "CASIMIR [X]: one 16 = {N=0:1, N=16:1} (none at N=8)",
        nonzero_entries(censuses[1]) == [(0, 1), (16, 1)] and censuses[1][8] == 0,
        "N=0:1, N=1..15:0, N=16:1",
    )
    report(
        "CASIMIR [X]: uniqueness fails at every cluster size",
        censuses[1][8] == 0 and censuses[2][16] == 27 and censuses[3][24] == 1463,
        "k=1 half-fill 0; k=2:27; k=3:1463",
    )

    vector_weights = spin10_vector_weights_doubled()
    vector_censuses = {}
    for copies in (1, 2):
        census, target_count, _cache_entries = exact_singlet_census(
            vector_weights,
            copies,
            SPIN10_RHO_DOUBLED,
            allow_all_sign_changes=False,
        )
        vector_censuses[copies] = census
        expected = (
            [(0, 1), (10, 1)]
            if copies == 1
            else [(0, 1)]
            + [(degree, 1) for degree in range(2, 10, 2)]
            + [(10, 12)]
            + [(degree, 1) for degree in range(12, 21, 2)]
        )
        report(
            "CASIMIR mutant [X]: vector-10 mutant k=%d" % copies,
            nonzero_entries(census) == expected,
            "%d D5 targets; nonzero %s" % (target_count, nonzero_entries(census)),
        )
    report(
        "CASIMIR mutant [X]: vector mutant changes half filling",
        vector_censuses[1][5] == 0
        and vector_censuses[2][10] == 12
        and vector_censuses[2][10] != censuses[2][16],
        "Lambda^5(10)=0; Lambda^10(10+10)=12 versus spinor k=2 value 27",
    )
    spin9_census, target_count, _cache_entries = exact_singlet_census(
        spin9_spinor_weights_doubled(),
        1,
        SPIN9_RHO_DOUBLED,
        allow_all_sign_changes=True,
    )
    report(
        "CASIMIR mutant [X]: Spin(9)-restriction mutant",
        nonzero_entries(spin9_census) == [(0, 1), (8, 1), (16, 1)]
        and spin9_census != censuses[1],
        "%d B4 targets; a new unique N=8 singlet appears" % target_count,
    )
    return censuses


def run():
    reset()
    print("=" * 78)
    print("v1002 -- CHIRAL4D.MIRROR.DET16.01 DET16 projector + Casimir kill")
    print("=" * 78)
    spin10_single_cluster()
    toy_multicluster_and_stability()
    spectator_check()
    run_casimir_kill()
    report(
        "FIREWALL (scope): finite-cluster identity only; no dynamical "
        "gauge fields, no domain-wall geometry, no 4D volume theorem; "
        "CHIRAL4D.NOMIRROR.01 stays Open; MIRROR.DET16 is Candidate [C]; "
        "no status-marker move",
        True,
    )
    return summary(
        "v1002 Spin(10) DET16 projector [E-finite] + hopping [N] + "
        "Casimir-route kill [X]"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
