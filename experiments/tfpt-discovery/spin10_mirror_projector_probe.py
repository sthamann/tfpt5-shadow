#!/usr/bin/env python3
r"""spin10_mirror_projector_probe -- EXPLORATION ONLY.

Deterministic one-cluster census for the fermionic Fock space of one
positive-chirality Spin(10) Weyl spinor (16 complex modes, dimension 2^16).
The exterior powers Lambda^N(16) are decomposed exactly by spinor-weight
enumeration and Freudenthal recursion.  Sparse second quantization is checked
directly on the full 65536-state Fock basis without retaining 45 large matrices.

Normalization warning.  For T_ab = i gamma_a gamma_b / 2 and the Casimir
sum over a<b, C2(16)=45/4, Tr_16(T_a T_b)=4 delta_ab, and C2(adj)=16.
The root-normalized convention C2(adj)=8 rescales every generator by 1/sqrt(2)
and therefore has C2(16)=45/8.  The often-quoted pair
"C2(16)=45/4 where C2(adj)=8" mixes these two conventions.  This probe prints
both consistently normalized values and uses the adjoint-8 convention for
the projector spectrum.

The exact projector is represented by its finite spectral Lagrange polynomial
P_1(C2) = product_{c != 0} (C2-c)/(-c).  No 65536-by-65536 dense matrix is
formed.  The two-cluster calculation is explicitly a low-Casimir truncation,
not a statement about the 2^32-dimensional tensor product or a volume theorem.

VERDICT ENUM:
  SPIN10_SINGLET_CENSUS(numbers)+SMG_CLUSTER_UNIQUE
  SPIN10_SINGLET_CENSUS(numbers)+SMG_CLUSTER_DEGENERATE(typed)
  SPIN10_ALGEBRA_OR_DECOMPOSITION_FAIL

CHIRAL4D.NOMIRROR.01 stays [O].
"""

from __future__ import annotations

import itertools
import math
import sys
from collections import defaultdict
from fractions import Fraction

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


TOL = 2.0e-9
CHECKS: list[bool] = []
N_MODES = 16
FOCK_DIM = 1 << N_MODES
RHO2 = (8, 6, 4, 2, 0)  # twice the D5 Weyl vector


def check(name: str, condition: bool, detail: str) -> bool:
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


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
    """Hermitian Euclidean gamma matrices with {gamma_a,gamma_b}=2 delta_ab."""
    gammas = []
    for site in range(5):
        suffix = [Z] * (4 - site)
        gammas.append(kron_all([I2] * site + [X] + suffix))
        gammas.append(kron_all([I2] * site + [Y] + suffix))
    return gammas


def positive_weyl_generators() -> tuple[list[np.ndarray], list[tuple[int, int]]]:
    gammas = gamma_matrices_10d()
    clifford_deviation = max(
        np.max(np.abs(gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
                      - (2.0 * np.eye(32) if a == b else np.zeros((32, 32)))))
        for a in range(10) for b in range(10)
    )
    gamma_product = np.eye(32, dtype=complex)
    for gamma in gammas:
        gamma_product = gamma_product @ gamma
    chirality = ((-1j) ** 5) * gamma_product
    chirality_values = np.real(np.diag(chirality))
    positive = np.flatnonzero(chirality_values > 0.5)
    if len(positive) != 16 or clifford_deviation > TOL:
        raise RuntimeError("failed to construct the 10D Weyl Clifford module")

    pairs = list(itertools.combinations(range(10), 2))
    generators = [
        (0.5j * gammas[a] @ gammas[b])[np.ix_(positive, positive)]
        for a, b in pairs
    ]
    return generators, pairs


def signed_generator(
    generators: list[np.ndarray],
    pair_to_index: dict[tuple[int, int], int],
    a: int,
    b: int,
) -> np.ndarray:
    if a == b:
        return np.zeros_like(generators[0])
    if a < b:
        return generators[pair_to_index[(a, b)]]
    return -generators[pair_to_index[(b, a)]]


def algebra_diagnostics(
    generators: list[np.ndarray], pairs: list[tuple[int, int]]
) -> tuple[float, float, float, float, float]:
    pair_to_index = {pair: index for index, pair in enumerate(pairs)}
    closure_deviation = 0.0
    for left, (a, b) in zip(generators, pairs):
        for right, (c, d) in zip(generators, pairs):
            expected = 1j * (
                (signed_generator(generators, pair_to_index, a, d) if b == c else 0)
                - (signed_generator(generators, pair_to_index, b, d) if a == c else 0)
                - (signed_generator(generators, pair_to_index, a, c) if b == d else 0)
                + (signed_generator(generators, pair_to_index, b, c) if a == d else 0)
            )
            closure_deviation = max(
                closure_deviation, float(np.max(np.abs(left @ right - right @ left - expected)))
            )

    gram = np.array(
        [[np.trace(left @ right) for right in generators] for left in generators]
    )
    trace_deviation = float(np.max(np.abs(gram - 4.0 * np.eye(45))))
    spinor_casimir = sum(generator @ generator for generator in generators)
    spinor_c2 = float(np.real(np.trace(spinor_casimir)) / 16.0)
    spinor_c2_deviation = float(
        np.max(np.abs(spinor_casimir - (45.0 / 4.0) * np.eye(16)))
    )

    # The adjoint matrices are obtained from the same commutator constants.
    adjoint = []
    for source in generators:
        matrix = np.zeros((45, 45), dtype=complex)
        for column, target in enumerate(generators):
            commutator = source @ target - target @ source
            matrix[:, column] = [
                -np.trace(basis @ commutator) / 4.0 for basis in generators
            ]
        adjoint.append(matrix)
    adjoint_casimir = sum(matrix @ matrix for matrix in adjoint)
    adjoint_c2 = float(np.real(np.trace(adjoint_casimir)) / 45.0)
    adjoint_deviation = float(
        np.max(np.abs(adjoint_casimir - 16.0 * np.eye(45)))
    )
    return (
        closure_deviation,
        trace_deviation,
        spinor_c2,
        spinor_c2_deviation,
        max(adjoint_deviation, abs(adjoint_c2 - 16.0)),
    )


def parity_table() -> np.ndarray:
    return np.fromiter(
        ((state.bit_count() & 1) for state in range(FOCK_DIM)),
        dtype=np.int8,
        count=FOCK_DIM,
    )


def second_quantize_full(
    one_body: np.ndarray, parity: np.ndarray
) -> sp.csr_matrix:
    """Return dGamma(one_body) on the full 2^16 occupation basis."""
    all_states = np.arange(FOCK_DIM, dtype=np.int64)
    row_parts = []
    column_parts = []
    data_parts = []
    for i, j in zip(*np.nonzero(np.abs(one_body) > TOL)):
        occupied_j = (all_states & (1 << j)) != 0
        if i == j:
            columns = all_states[occupied_j]
            rows = columns
            signs = np.ones(len(columns), dtype=np.int8)
        else:
            allowed = occupied_j & ((all_states & (1 << i)) == 0)
            columns = all_states[allowed]
            rows = columns ^ (1 << i) ^ (1 << j)
            low, high = sorted((i, j))
            between_mask = ((1 << high) - 1) ^ ((1 << (low + 1)) - 1)
            signs = 1 - 2 * parity[columns & between_mask]
        row_parts.append(rows)
        column_parts.append(columns)
        data_parts.append(one_body[i, j] * signs)
    result = sp.coo_matrix(
        (np.concatenate(data_parts), (np.concatenate(row_parts), np.concatenate(column_parts))),
        shape=(FOCK_DIM, FOCK_DIM),
    ).tocsr()
    result.eliminate_zeros()
    return result


def full_fock_sparse_diagnostics(
    generators: list[np.ndarray],
) -> tuple[int, int, float, float]:
    parity = parity_table()
    minimum_nnz = FOCK_DIM
    maximum_nnz = 0
    hermitian_deviation = 0.0
    filled_deviation = 0.0
    filled = FOCK_DIM - 1
    for generator in generators:
        fock_generator = second_quantize_full(generator, parity)
        minimum_nnz = min(minimum_nnz, fock_generator.nnz)
        maximum_nnz = max(maximum_nnz, fock_generator.nnz)
        difference = fock_generator - fock_generator.getH()
        if difference.nnz:
            hermitian_deviation = max(
                hermitian_deviation, float(np.max(np.abs(difference.data)))
            )
        filled_deviation = max(
            filled_deviation,
            float(np.linalg.norm(fock_generator.getcol(filled).toarray())),
        )
    return minimum_nnz, maximum_nnz, hermitian_deviation, filled_deviation


def spinor_weights_doubled() -> list[tuple[int, ...]]:
    """Weights of one chiral 16; coordinates are doubled orthonormal weights."""
    return [
        signs
        for signs in itertools.product((-1, 1), repeat=5)
        if sum(value < 0 for value in signs) % 2 == 0
    ]


def exterior_characters() -> list[dict[tuple[int, ...], int]]:
    sectors: list[dict[tuple[int, ...], int]] = [
        defaultdict(int) for _ in range(N_MODES + 1)
    ]
    sectors[0][(0, 0, 0, 0, 0)] = 1
    occupied = 0
    for weight in spinor_weights_doubled():
        occupied += 1
        for particle_number in range(occupied, 0, -1):
            for old_weight, multiplicity in list(sectors[particle_number - 1].items()):
                new_weight = tuple(a + b for a, b in zip(old_weight, weight))
                sectors[particle_number][new_weight] += multiplicity
    return [dict(sector) for sector in sectors]


def is_dominant(weight: tuple[int, ...]) -> bool:
    return (
        weight[0] >= weight[1] >= weight[2] >= weight[3]
        and weight[3] >= abs(weight[4])
    )


def lowering_height(
    highest: tuple[int, ...], weight: tuple[int, ...]
) -> int | None:
    difference = [highest[index] - weight[index] for index in range(5)]
    if any(value % 2 for value in difference):
        return None
    d1, d2, d3, d4, d5 = (value // 2 for value in difference)
    n1 = d1
    n2 = d1 + d2
    n3 = d1 + d2 + d3
    numerator4 = d4 - d5 + n3
    numerator5 = d4 + d5 + n3
    if numerator4 % 2 or numerator5 % 2:
        return None
    coefficients = (n1, n2, n3, numerator4 // 2, numerator5 // 2)
    if min(coefficients) < 0:
        return None
    return sum(coefficients)


def positive_roots_doubled() -> list[tuple[int, ...]]:
    roots = []
    for i in range(5):
        for j in range(i + 1, 5):
            difference = [0] * 5
            difference[i], difference[j] = 2, -2
            roots.append(tuple(difference))
            total = [0] * 5
            total[i], total[j] = 2, 2
            roots.append(tuple(total))
    return roots


POSITIVE_ROOTS = positive_roots_doubled()


def irreducible_character(
    highest: tuple[int, ...],
    available_weights: set[tuple[int, ...]],
) -> dict[tuple[int, ...], int]:
    candidates = []
    for weight in available_weights:
        height = lowering_height(highest, weight)
        if height is not None:
            candidates.append((height, weight))
    candidates.sort(key=lambda item: (item[0], item[1]), reverse=False)
    multiplicities: dict[tuple[int, ...], int] = {highest: 1}
    highest_shifted_norm = sum(
        (highest[index] + RHO2[index]) ** 2 for index in range(5)
    )
    maximum_height = max((height for height, _weight in candidates), default=0)
    for height, weight in candidates:
        if height == 0:
            continue
        numerator = 0
        for root in POSITIVE_ROOTS:
            for step in range(1, maximum_height + 1):
                parent = tuple(
                    weight[index] + step * root[index] for index in range(5)
                )
                parent_multiplicity = multiplicities.get(parent, 0)
                if parent_multiplicity:
                    numerator += (
                        2
                        * sum(
                            (weight[index] + step * root[index]) * root[index]
                            for index in range(5)
                        )
                        * parent_multiplicity
                    )
        denominator = highest_shifted_norm - sum(
            (weight[index] + RHO2[index]) ** 2 for index in range(5)
        )
        if denominator <= 0:
            continue
        value = Fraction(numerator, denominator)
        if value.denominator != 1 or value < 0:
            raise RuntimeError(
                "nonintegral Freudenthal multiplicity %s at %s below %s"
                % (value, weight, highest)
            )
        if value:
            multiplicities[weight] = int(value)
    return multiplicities


def dynkin_labels(weight: tuple[int, ...]) -> tuple[int, ...]:
    x1, x2, x3, x4, x5 = weight
    numerators = (x1 - x2, x2 - x3, x3 - x4, x4 - x5, x4 + x5)
    if any(value % 2 for value in numerators):
        raise RuntimeError("nonintegral D5 Dynkin labels")
    return tuple(value // 2 for value in numerators)


def c2_raw(highest: tuple[int, ...]) -> Fraction:
    # lambda.(lambda+2rho), with lambda=highest/2.
    twice_two_rho = (16, 12, 8, 4, 0)
    return Fraction(
        sum(
            highest[index] * (highest[index] + twice_two_rho[index])
            for index in range(5)
        ),
        4,
    )


def decompose_sector(
    character: dict[tuple[int, ...], int]
) -> list[tuple[tuple[int, ...], int, int, Fraction]]:
    remaining = dict(character)
    decomposition = []
    while remaining:
        dominant_weights = [weight for weight in remaining if is_dominant(weight)]
        if not dominant_weights:
            raise RuntimeError("character has no dominant highest weight")
        highest = max(
            dominant_weights,
            key=lambda weight: (
                sum(weight[index] * RHO2[index] for index in range(5)),
                weight,
            ),
        )
        copies = remaining[highest]
        irrep_character = irreducible_character(highest, set(remaining))
        dimension = sum(irrep_character.values())
        for weight, weight_multiplicity in irrep_character.items():
            updated = remaining.get(weight, 0) - copies * weight_multiplicity
            if updated < 0:
                raise RuntimeError(
                    "character subtraction went negative at %s: %d"
                    % (weight, updated)
                )
            if updated:
                remaining[weight] = updated
            else:
                remaining.pop(weight, None)
        decomposition.append((dynkin_labels(highest), copies, dimension, c2_raw(highest)))
    return decomposition


def exact_decomposition():
    characters = exterior_characters()
    decompositions = []
    for particle_number, character in enumerate(characters):
        expected_dimension = math.comb(N_MODES, particle_number)
        if sum(character.values()) != expected_dimension:
            raise RuntimeError("exterior-character dimension mismatch")
        decomposition = decompose_sector(character)
        reconstructed = sum(copies * dimension for _, copies, dimension, _ in decomposition)
        if reconstructed != expected_dimension:
            raise RuntimeError("irrep dimension mismatch in sector %d" % particle_number)
        decompositions.append(decomposition)
    return characters, decompositions


def casimir_levels(
    decomposition: list[tuple[tuple[int, ...], int, int, Fraction]]
) -> dict[Fraction, int]:
    levels: dict[Fraction, int] = defaultdict(int)
    for _labels, copies, dimension, raw_c2 in decomposition:
        levels[raw_c2 / 2] += copies * dimension
    return dict(sorted(levels.items()))


def lagrange_projector_polynomial(nonzero_levels: list[Fraction]) -> list[Fraction]:
    coefficients = [Fraction(1)]
    for level in nonzero_levels:
        updated = [Fraction(0)] * (len(coefficients) + 1)
        for power, coefficient in enumerate(coefficients):
            updated[power] += coefficient
            updated[power + 1] -= coefficient / level
        coefficients = updated
    return coefficients


def evaluate_polynomial(coefficients: list[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def truncated_two_cluster(
    all_levels: dict[Fraction, int],
    singlet_count: int,
    delta: float = 1.0,
) -> tuple[int, int, int, dict[float, tuple[int, float]]]:
    lowest_nonzero = min(level for level in all_levels if level)
    lowest_dimension = all_levels[lowest_nonzero]
    truncated_dimension = singlet_count + lowest_dimension
    if truncated_dimension > 100:
        raise RuntimeError("low-Casimir truncation exceeds the declared dimension cap")
    projector = np.diag(
        np.array([1.0] * singlet_count + [0.0] * lowest_dimension)
    )
    identity = np.eye(truncated_dimension)
    results = {}
    for epsilon in (-0.1, 0.1):
        hamiltonian = (
            delta * (np.kron(identity - projector, identity)
                     + np.kron(identity, identity - projector))
            + epsilon * (np.kron(identity, identity) - np.kron(projector, projector))
        )
        eigenvalues = np.linalg.eigvalsh(hamiltonian)
        ground = eigenvalues[0]
        ground_degeneracy = int(np.sum(np.abs(eigenvalues - ground) < TOL))
        excited = eigenvalues[eigenvalues > ground + TOL]
        gap = float(excited[0] - ground)
        results[epsilon] = (ground_degeneracy, gap)
    return truncated_dimension, singlet_count ** 2, lowest_dimension, results


def sector_basis(particle_number: int) -> np.ndarray:
    return np.fromiter(
        (
            sum(1 << mode for mode in occupied)
            for occupied in itertools.combinations(range(N_MODES), particle_number)
        ),
        dtype=np.int64,
        count=math.comb(N_MODES, particle_number),
    )


def second_quantize_sector(
    one_body: np.ndarray,
    basis: np.ndarray,
    state_to_index: np.ndarray,
    parity: np.ndarray,
) -> sp.csr_matrix:
    row_parts = []
    column_parts = []
    data_parts = []
    for i, j in zip(*np.nonzero(np.abs(one_body) > TOL)):
        occupied_j = (basis & (1 << j)) != 0
        if i == j:
            columns = np.flatnonzero(occupied_j)
            rows = columns
            signs = np.ones(len(columns), dtype=np.int8)
        else:
            allowed = occupied_j & ((basis & (1 << i)) == 0)
            columns = np.flatnonzero(allowed)
            target_states = basis[columns] ^ (1 << i) ^ (1 << j)
            rows = state_to_index[target_states]
            low, high = sorted((i, j))
            between_mask = ((1 << high) - 1) ^ ((1 << (low + 1)) - 1)
            signs = 1 - 2 * parity[basis[columns] & between_mask]
        row_parts.append(rows)
        column_parts.append(columns)
        data_parts.append(one_body[i, j] * signs)
    dimension = len(basis)
    result = sp.coo_matrix(
        (np.concatenate(data_parts), (np.concatenate(row_parts), np.concatenate(column_parts))),
        shape=(dimension, dimension),
    ).tocsr()
    result.eliminate_zeros()
    return result


def spin9_half_filling_mutant(
    generators: list[np.ndarray], pairs: list[tuple[int, int]]
) -> tuple[np.ndarray, int]:
    """Drop all generators involving axis 9: Spin(10) -> Spin(9)."""
    basis = sector_basis(8)
    state_to_index = np.full(FOCK_DIM, -1, dtype=np.int64)
    state_to_index[basis] = np.arange(len(basis))
    parity = parity_table()
    retained = [
        generator for generator, (a, b) in zip(generators, pairs) if a < 9 and b < 9
    ]
    sector_generators = [
        second_quantize_sector(generator, basis, state_to_index, parity)
        for generator in retained
    ]

    def apply_casimir(vector):
        result = np.zeros_like(vector, dtype=complex)
        for generator in sector_generators:
            result += generator @ (generator @ vector)
        return result

    operator = spla.LinearOperator(
        (len(basis), len(basis)), matvec=apply_casimir, dtype=complex
    )
    deterministic_start = np.linspace(1.0, 2.0, len(basis), dtype=complex)
    deterministic_start /= np.linalg.norm(deterministic_start)
    eigenvalues = np.sort(
        np.real(
            spla.eigsh(
                operator,
                k=4,
                which="SM",
                tol=1.0e-10,
                v0=deterministic_start,
                return_eigenvectors=False,
            )
        )
    )
    nullity_seen = int(np.sum(np.abs(eigenvalues) < 1.0e-7))
    return eigenvalues, nullity_seen


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def main() -> int:
    print("=" * 88)
    print("spin10_mirror_projector_probe -- exact Fock(16) singlet census")
    print("EXPLORATION ONLY; CHIRAL4D.NOMIRROR.01 stays [O]")
    print("=" * 88)

    generators, pairs = positive_weyl_generators()
    closure_dev, trace_dev, spinor_c2, spinor_dev, adjoint_dev = algebra_diagnostics(
        generators, pairs
    )
    check(
        "Spin(10) Weyl algebra closes",
        closure_dev < TOL,
        "45 Hermitian generators; max commutator deviation %.2e" % closure_dev,
    )
    check(
        "raw-pair Casimir + trace identity",
        trace_dev < TOL and spinor_dev < TOL and abs(spinor_c2 - 45 / 4) < TOL,
        "C2(16)=%.6g=45/4; Tr(TaTb)=4 delta (dev %.1e); "
        "C2*16=I2*45=180" % (spinor_c2, trace_dev),
    )
    check(
        "normalization consistency",
        adjoint_dev < TOL,
        "same raw generators: C2(adj)=16; after T/sqrt(2): "
        "C2(adj)=8 and C2(16)=45/8 (45/4 with adj=8 is mixed)",
    )

    minimum_nnz, maximum_nnz, hermitian_dev, filled_dev = (
        full_fock_sparse_diagnostics(generators)
    )
    check(
        "full sparse second quantization",
        hermitian_dev < TOL and filled_dev < TOL,
        "45 dGamma(Ta), shape 65536^2, nnz range %d..%d, "
        "Hermitian dev %.1e" % (minimum_nnz, maximum_nnz, hermitian_dev),
    )
    check(
        "totally filled state is singlet",
        filled_dev < TOL,
        "max ||dGamma(Ta)|filled>||=%.1e; equivalently sum of 16 weights=0"
        % filled_dev,
    )

    _characters, decompositions = exact_decomposition()
    sector_levels = [casimir_levels(decomposition) for decomposition in decompositions]
    singlet_census = [
        (particle_number, levels.get(Fraction(0), 0))
        for particle_number, levels in enumerate(sector_levels)
        if levels.get(Fraction(0), 0)
    ]
    exact_dimensions = all(
        sum(levels.values()) == math.comb(N_MODES, particle_number)
        for particle_number, levels in enumerate(sector_levels)
    )
    check(
        "all exterior sectors decomposed",
        exact_dimensions,
        "17 exact character decompositions; every multiplicity sums to C(16,N)",
    )
    check(
        "exact Spin(10) singlet census",
        singlet_census == [(0, 1), (16, 1)],
        "nonzero entries %s; total singlets %d"
        % (singlet_census, sum(count for _, count in singlet_census)),
    )
    half_filling_singlets = sector_levels[8].get(Fraction(0), 0)
    check(
        "half-filling acceptance test",
        half_filling_singlets == 0,
        "Lambda^8(16) singlet multiplicity = %d (there is no physical N=8 singlet)"
        % half_filling_singlets,
    )

    all_levels: dict[Fraction, int] = defaultdict(int)
    for levels in sector_levels:
        for value, multiplicity in levels.items():
            all_levels[value] += multiplicity
    nonzero_levels = sorted(level for level in all_levels if level)
    projector_coefficients = lagrange_projector_polynomial(nonzero_levels)
    projector_values = {
        level: evaluate_polynomial(projector_coefficients, level) for level in all_levels
    }
    projector_ok = (
        projector_values[Fraction(0)] == 1
        and all(projector_values[level] == 0 for level in nonzero_levels)
        and all_levels[Fraction(0)] == 2
    )
    check(
        "exact spectral singlet projector",
        projector_ok,
        "degree %d over %d distinct nonzero C2 values; rank(P1)=2"
        % (len(projector_coefficients) - 1, len(nonzero_levels)),
    )

    truncated_dimension, expected_ground_degeneracy, lowest_dimension, coupling = (
        truncated_two_cluster(all_levels, all_levels[Fraction(0)])
    )
    coupling_ok = all(
        degeneracy == expected_ground_degeneracy and gap > 0
        for degeneracy, gap in coupling.values()
    )
    check(
        "two-cluster low-C2 truncation",
        truncated_dimension <= 100 and coupling_ok,
        "per cluster dim %d = 2 singlets + %d lowest-nonsinglets; "
        "eps=-0.1/+0.1 -> %s"
        % (truncated_dimension, lowest_dimension, coupling),
    )
    check(
        "claimed unique product rejected",
        expected_ground_degeneracy == 4,
        "P1 projects both N=0 and N=16: two-cluster ground degeneracy = 2^2 = 4; "
        "an extra filling/interaction selector is required",
    )

    mutant_eigenvalues, mutant_nullity = spin9_half_filling_mutant(generators, pairs)
    check(
        "Spin(9) generator-drop mutant",
        mutant_nullity >= 1 and mutant_eigenvalues[1] > 1.0e-6,
        "drop 9 generators involving axis 10: N=8 lowest C2 %s; "
        "a unique observed half-filled singlet appears"
        % np.array2string(mutant_eigenvalues, precision=7),
    )

    print("\nFULL SINGLET CENSUS")
    print("  N   dim Lambda^N(16)   singlet multiplicity")
    for particle_number, levels in enumerate(sector_levels):
        print(
            " %2d %18d %22d"
            % (
                particle_number,
                math.comb(N_MODES, particle_number),
                levels.get(Fraction(0), 0),
            )
        )

    print("\nCASIMIR SPECTRUM BY PARTICLE-NUMBER SECTOR")
    print("  convention: C2(adj)=8, hence C2(16)=45/8")
    for particle_number, levels in enumerate(sector_levels):
        entries = ", ".join(
            "%s:%d" % (fraction_text(value), multiplicity)
            for value, multiplicity in levels.items()
        )
        print("  N=%2d  %s" % (particle_number, entries))

    print("\nIRREP DECOMPOSITION (Dynkin labels^copies[dimension; C2_adj8])")
    for particle_number, decomposition in enumerate(decompositions):
        entries = []
        for labels, copies, dimension, raw_value in decomposition:
            entries.append(
                "%s^%d[%d;%s]"
                % (labels, copies, dimension, fraction_text(raw_value / 2))
            )
        print("  N=%2d  %s" % (particle_number, " + ".join(entries)))

    census_numbers = ",".join(
        "N%d:%d" % (particle_number, multiplicity)
        for particle_number, multiplicity in singlet_census
    )
    if not all(CHECKS):
        verdict = "SPIN10_ALGEBRA_OR_DECOMPOSITION_FAIL"
    elif half_filling_singlets == 1 and all_levels[Fraction(0)] == 1:
        verdict = "SPIN10_SINGLET_CENSUS(%s)+SMG_CLUSTER_UNIQUE" % census_numbers
    else:
        verdict = (
            "SPIN10_SINGLET_CENSUS(%s)+"
            "SMG_CLUSTER_DEGENERATE(NO_N8_SINGLET;GLOBAL_RANK2)"
        ) % census_numbers

    print("\nVERDICT: %s" % verdict)
    print(
        "BOUNDARY: exact one-cluster representation census and exact spectral "
        "projector; two clusters only after a declared low-Casimir truncation "
        "(per-cluster dim %d); no 2^32 construction, no volume/Knabe theorem, "
        "no gauge fields. CHIRAL4D.NOMIRROR.01 stays [O]." % truncated_dimension
    )
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("=" * 88)
    return 0 if all(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
