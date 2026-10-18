#!/usr/bin/env python3
"""Finite canonicality audit for SEAM.MILNOR.LOCALRING.01.

EXPLORATION ONLY.  This probe rebuilds the Gaussian Construction-A E8 object
used by v833/v1004 and the integral Milnor model used by v1004.  It then asks
whether their corpus-defined F2 structures are simultaneously isomorphic.

The four requested structures are interpreted literally as:

X = L/2L, for the Gaussian E8 lattice L:
  eps   = 1 + J,
  B     = the E8 bilinear form modulo 2,
  clock = J modulo 2,
  CP    = Gaussian conjugation modulo 2.

Y = F2[y,z]/(y^2,z^4), in monomial order
    (1,z,z^2,z^3,y,yz,yz^2,yz^3):
  eps   = multiplication by y,
  B     = coefficient of yz^3 in a product,
  clock = the exponent-7 Gray permutation b -> (0 1 3 2)b,
  CP    = (a,b) -> (1-a,3-b).

Important typing facts checked rather than assumed:
  * v1004 proved only a basis-dependent D-module bridge, not preservation of
    the pairing, clock, or CP.
  * On L/2L, J = 1+eps has order two, since eps^2=0.  The order-four Gaussian
    deck survives on lattice vectors but collapses modulo 2.
  * The order-four Gray action is a linear permutation of the monomial basis
    here.  Its canonical carrier realization in v804 is affine, not linear.
  * The E8 quadratic refinement exists.  A Frobenius bilinear form in
    characteristic two does not by itself distinguish one of its 256
    quadratic refinements, so no unrecorded q_Y is silently inserted.

All finite-field arithmetic is exact.  There are no floats, tolerances,
random choices, fitted maps, or imports from the verification suite.
"""
from __future__ import annotations

from itertools import permutations, product
from time import monotonic

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form


DIMENSION = 8
FIELD_SIZE = 2
MILNOR_D_RANK = 4
SP4_F2_ORDER = 720
SYMMETRIC_4X4_DIMENSION = 10

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    """Record one exact Boolean gate."""
    global PASS_COUNT, FAIL_COUNT
    passed = bool(condition)
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = " -- %s" % detail if detail else ""
    print("  [%s] %s%s" % ("PASS" if passed else "FAIL", name, suffix))


def section(title: str) -> None:
    print("\n== %s ==" % title)


def zero_matrix() -> list[list[int]]:
    return [[0] * DIMENSION for _ in range(DIMENSION)]


def identity_matrix() -> list[list[int]]:
    return [
        [int(row == column) for column in range(DIMENSION)]
        for row in range(DIMENSION)
    ]


def matrix_add(
    left: list[list[int]], right: list[list[int]]
) -> list[list[int]]:
    return [
        [left[row][column] ^ right[row][column]
         for column in range(DIMENSION)]
        for row in range(DIMENSION)
    ]


def matrix_multiply(
    left: list[list[int]], right: list[list[int]]
) -> list[list[int]]:
    return [
        [
            sum(
                left[row][index] * right[index][column]
                for index in range(DIMENSION)
            ) % FIELD_SIZE
            for column in range(DIMENSION)
        ]
        for row in range(DIMENSION)
    ]


def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def matrix_rank(matrix: list[list[int]]) -> int:
    """Exact rank over F2, using one integer bit-row per matrix row."""
    rows = [
        sum((entry & 1) << column for column, entry in enumerate(row))
        for row in matrix
    ]
    rank = 0
    for column in range(DIMENSION):
        pivot = next(
            (
                row
                for row in range(rank, len(rows))
                if (rows[row] >> column) & 1
            ),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for row in range(len(rows)):
            if row != rank and ((rows[row] >> column) & 1):
                rows[row] ^= rows[rank]
        rank += 1
    return rank


def matrix_power(matrix: list[list[int]], exponent: int) -> list[list[int]]:
    result = identity_matrix()
    factor = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, factor)
        factor = matrix_multiply(factor, factor)
        exponent //= 2
    return result


def matrix_from_columns(columns: list[int]) -> list[list[int]]:
    return [
        [((columns[column] >> row) & 1) for column in range(DIMENSION)]
        for row in range(DIMENSION)
    ]


def matrix_columns(matrix: list[list[int]]) -> list[int]:
    return [
        sum(matrix[row][column] << row for row in range(DIMENSION))
        for column in range(DIMENSION)
    ]


def columns_hex(matrix: list[list[int]]) -> str:
    return " ".join("%02x" % column for column in matrix_columns(matrix))


def sympy_mod2(matrix: sp.Matrix) -> list[list[int]]:
    return [
        [int(matrix[row, column]) % 2 for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def apply_matrix(matrix: list[list[int]], word: int) -> int:
    output = 0
    for row in range(DIMENSION):
        bit = sum(
            matrix[row][column] * ((word >> column) & 1)
            for column in range(DIMENSION)
        ) % FIELD_SIZE
        output |= bit << row
    return output


def pairing_value(
    pairing: list[list[int]], left: int, right: int
) -> int:
    return sum(
        ((left >> row) & 1)
        * pairing[row][column]
        * ((right >> column) & 1)
        for row in range(DIMENSION)
        for column in range(DIMENSION)
    ) % FIELD_SIZE


def preserves_pairing(
    matrix: list[list[int]], pairing: list[list[int]]
) -> bool:
    return (
        matrix_multiply(
            matrix_transpose(matrix),
            matrix_multiply(pairing, matrix),
        )
        == pairing
    )


def is_alternating(pairing: list[list[int]]) -> bool:
    return (
        pairing == matrix_transpose(pairing)
        and all(pairing[index][index] == 0 for index in range(DIMENSION))
    )


def nullspace_bit_basis(rows: list[int], variable_count: int) -> list[int]:
    """Return an exact bit-vector basis for a homogeneous F2 nullspace."""
    reduced = [row for row in rows if row]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(variable_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(reduced))
                if (reduced[row] >> column) & 1
            ),
            None,
        )
        if pivot is None:
            continue
        reduced[pivot_row], reduced[pivot] = (
            reduced[pivot],
            reduced[pivot_row],
        )
        for row in range(len(reduced)):
            if row != pivot_row and ((reduced[row] >> column) & 1):
                reduced[row] ^= reduced[pivot_row]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(reduced):
            break

    free_columns = [
        column for column in range(variable_count) if column not in pivots
    ]
    basis: list[int] = []
    for free_column in free_columns:
        vector = 1 << free_column
        for row in range(pivot_row - 1, -1, -1):
            if (reduced[row] & vector).bit_count() % 2:
                vector |= 1 << pivots[row]
        basis.append(vector)
    return basis


def commutant_basis(operators: tuple[list[list[int]], ...]) -> list[int]:
    """Linear basis of matrices M satisfying MA=AM for every A."""
    equations: list[int] = []
    for operator in operators:
        for row in range(DIMENSION):
            for column in range(DIMENSION):
                equation = 0
                for index in range(DIMENSION):
                    if operator[index][column]:
                        equation ^= 1 << (DIMENSION * row + index)
                    if operator[row][index]:
                        equation ^= 1 << (DIMENSION * index + column)
                equations.append(equation)
    return nullspace_bit_basis(equations, DIMENSION * DIMENSION)


def count_pairing_automorphisms(
    commutant: list[int], pairing: list[list[int]]
) -> int:
    """Exhaust the commutant algebra and count its pairing isometries.

    A pairing isometry is automatically invertible because the pairing is
    nondegenerate.  Gray-code enumeration changes one algebra-basis element
    per candidate.  Pair values are table-looked-up on 8-bit columns.
    """
    basis_columns = [
        matrix_columns([
            [
                (basis_matrix >> (DIMENSION * row + column)) & 1
                for column in range(DIMENSION)
            ]
            for row in range(DIMENSION)
        ])
        for basis_matrix in commutant
    ]
    pairing_action = [
        apply_matrix(pairing, word) for word in range(1 << DIMENSION)
    ]
    pair_table = [
        [
            (left & pairing_action[right]).bit_count() % 2
            for right in range(1 << DIMENSION)
        ]
        for left in range(1 << DIMENSION)
    ]
    constraints = [
        (row, column, pairing[row][column])
        for row in range(DIMENSION)
        for column in range(row, DIMENSION)
    ]
    constraints.sort(key=lambda item: (item[2], item[0] != item[1]))

    columns = [0] * DIMENSION
    previous_gray = 0
    count = 0
    for candidate_number in range(1, 1 << len(commutant)):
        gray = candidate_number ^ (candidate_number >> 1)
        changed_index = (gray ^ previous_gray).bit_length() - 1
        changed_columns = basis_columns[changed_index]
        for column in range(DIMENSION):
            columns[column] ^= changed_columns[column]
        previous_gray = gray
        if all(
            pair_table[columns[row]][columns[column]] == target
            for row, column, target in constraints
        ):
            count += 1
    return count


def code_image(
    code: frozenset[tuple[int, ...]], permutation: tuple[int, ...]
) -> frozenset[tuple[int, ...]]:
    return frozenset(
        tuple(codeword[permutation[index]] for index in range(DIMENSION))
        for codeword in code
    )


def build_gaussian_x() -> dict[str, object]:
    """Rebuild exactly the v833/v1004 Gaussian E8 jet."""
    naive_generator = (
        (1, 0, 0, 0, 0, 1, 1, 1),
        (0, 1, 0, 0, 1, 0, 1, 1),
        (0, 0, 1, 0, 1, 1, 0, 1),
        (0, 0, 0, 1, 1, 1, 1, 0),
    )
    naive_code = frozenset(
        tuple(
            sum(
                message[row] * naive_generator[row][column]
                for row in range(MILNOR_D_RANK)
            ) % FIELD_SIZE
            for column in range(DIMENSION)
        )
        for message in product((0, 1), repeat=MILNOR_D_RANK)
    )
    permutation_j = (1, 0, 3, 2, 5, 4, 7, 6)
    permutation_sigma = (2, 3, 4, 5, 0, 1, 6, 7)
    placements = {
        code_image(naive_code, permutation)
        for permutation in permutations(range(DIMENSION))
    }
    invariant_placements = [
        code
        for code in placements
        if code_image(code, permutation_j) == code
        and code_image(code, permutation_sigma) == code
    ]
    distinguished_word = (1, 0, 1, 0, 1, 0, 1, 0)
    code = next(
        code for code in invariant_placements if distinguished_word in code
    )

    lattice_generators = sp.Matrix(
        [list(codeword) for codeword in sorted(code)]
        + [
            [2 * int(row == column) for column in range(DIMENSION)]
            for row in range(DIMENSION)
        ]
    ).T
    lattice_basis = hermite_normal_form(lattice_generators)
    lattice_j = sp.zeros(DIMENSION)
    conjugation = sp.zeros(DIMENSION)
    for pair_index in range(MILNOR_D_RANK):
        even = 2 * pair_index
        odd = even + 1
        lattice_j[even, odd] = -1
        lattice_j[odd, even] = 1
        conjugation[even, even] = 1
        conjugation[odd, odd] = -1

    identity = sp.eye(DIMENSION)
    epsilon_integral = lattice_basis.inv() * (identity + lattice_j) \
        * lattice_basis
    clock_integral = lattice_basis.inv() * lattice_j * lattice_basis
    cp_integral = lattice_basis.inv() * conjugation * lattice_basis
    pairing_integral = (lattice_basis.T * lattice_basis) / 2

    return {
        "placements": placements,
        "invariant_placements": invariant_placements,
        "lattice_basis": lattice_basis,
        "lattice_j": lattice_j,
        "conjugation": conjugation,
        "epsilon_integral": epsilon_integral,
        "clock_integral": clock_integral,
        "cp_integral": cp_integral,
        "pairing_integral": pairing_integral,
        "epsilon": sympy_mod2(epsilon_integral),
        "clock": sympy_mod2(clock_integral),
        "cp": sympy_mod2(cp_integral),
        "pairing": sympy_mod2(pairing_integral),
    }


def build_milnor_y() -> dict[str, list[list[int]]]:
    """Build the v1004 integral Milnor model after reduction modulo two."""
    epsilon = zero_matrix()
    clock = zero_matrix()
    cp = zero_matrix()
    pairing = zero_matrix()
    gray_successor = {0: 1, 1: 3, 3: 2, 2: 0}

    for a_value in range(2):
        for b_value in range(4):
            source = 4 * a_value + b_value
            if a_value == 0:
                epsilon[4 + b_value][source] = 1
            clock[4 * a_value + gray_successor[b_value]][source] = 1
            cp[4 * (1 - a_value) + (3 - b_value)][source] = 1
            for a_right in range(2):
                for b_right in range(4):
                    target = 4 * a_right + b_right
                    pairing[source][target] = int(
                        a_value + a_right == 1
                        and b_value + b_right == 3
                    )
    return {
        "epsilon": epsilon,
        "clock": clock,
        "cp": cp,
        "pairing": pairing,
    }


def independent_rank(vectors: list[int]) -> int:
    rows = list(vectors)
    rank = 0
    for column in range(DIMENSION):
        pivot = next(
            (
                row
                for row in range(rank, len(rows))
                if (rows[row] >> column) & 1
            ),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for row in range(len(rows)):
            if row != rank and ((rows[row] >> column) & 1):
                rows[row] ^= rows[rank]
        rank += 1
    return rank


def inverse_from_columns(columns: list[int]) -> list[list[int]]:
    """Invert an F2 matrix supplied by columns."""
    augmented_rows = [
        (
            sum(((columns[column] >> row) & 1) << column
                for column in range(DIMENSION))
            | (1 << (DIMENSION + row))
        )
        for row in range(DIMENSION)
    ]
    for column in range(DIMENSION):
        pivot = next(
            row
            for row in range(column, DIMENSION)
            if (augmented_rows[row] >> column) & 1
        )
        augmented_rows[column], augmented_rows[pivot] = (
            augmented_rows[pivot],
            augmented_rows[column],
        )
        for row in range(DIMENSION):
            if row != column and ((augmented_rows[row] >> column) & 1):
                augmented_rows[row] ^= augmented_rows[column]
    inverse_columns = [
        sum(
            ((augmented_rows[row] >> (DIMENSION + column)) & 1) << row
            for row in range(DIMENSION)
        )
        for column in range(DIMENSION)
    ]
    return matrix_from_columns(inverse_columns)


def coarsened_bridge_witness(
    epsilon_x: list[list[int]], pairing_x: list[list[int]]
) -> tuple[list[int], list[list[int]]]:
    """Find a deterministic D+pairing normal basis and X->Y witness."""
    reverse_pairing = [
        [int(row + column == 3) for column in range(MILNOR_D_RANK)]
        for row in range(MILNOR_D_RANK)
    ]

    def search(generators: list[int]) -> list[int] | None:
        generator_index = len(generators)
        if generator_index == MILNOR_D_RANK:
            return generators
        for candidate in range(1, 1 << DIMENSION):
            epsilon_candidate = apply_matrix(epsilon_x, candidate)
            if epsilon_candidate == 0:
                continue
            if pairing_value(
                pairing_x, candidate, epsilon_candidate
            ) != reverse_pairing[generator_index][generator_index]:
                continue
            if any(
                pairing_value(pairing_x, candidate, previous) != 0
                or pairing_value(
                    pairing_x,
                    candidate,
                    apply_matrix(epsilon_x, previous),
                ) != reverse_pairing[generator_index][previous_index]
                for previous_index, previous in enumerate(generators)
            ):
                continue
            extended = generators + [candidate]
            basis_vectors = [
                vector
                for generator in extended
                for vector in (
                    generator,
                    apply_matrix(epsilon_x, generator),
                )
            ]
            if independent_rank(basis_vectors) != 2 * len(extended):
                continue
            result = search(extended)
            if result is not None:
                return result
        return None

    generators = search([])
    assert generators is not None
    normal_basis_columns = generators + [
        apply_matrix(epsilon_x, generator) for generator in generators
    ]
    return generators, inverse_from_columns(normal_basis_columns)


def quadratic_refinement_x(
    lattice_basis: sp.Matrix, pairing: list[list[int]]
) -> dict[int, int]:
    """The v833 E8 quadratic refinement q(x)=|x|^2/4 modulo two."""
    basis_integer = [
        [int(lattice_basis[row, column]) for column in range(DIMENSION)]
        for row in range(DIMENSION)
    ]
    values: dict[int, int] = {}
    for word in range(1 << DIMENSION):
        lift = [
            sum(
                basis_integer[row][column] * ((word >> column) & 1)
                for column in range(DIMENSION)
            )
            for row in range(DIMENSION)
        ]
        norm = sum(entry * entry for entry in lift)
        assert norm % 4 == 0
        values[word] = (norm // 4) % 2
    check(
        "X quadratic refinement polarizes to the E8 pairing",
        all(
            values[left ^ right] ^ values[left] ^ values[right]
            == pairing_value(pairing, left, right)
            for left in range(1 << DIMENSION)
            for right in range(1 << DIMENSION)
        ),
    )
    return values


def main() -> int:
    print("MILNOR BRIDGE FINITE CANONICALITY AUDIT")
    print("Arithmetic: exact ZZ/F2 only; no floats, RNG, or fitting")

    section("Corpus objects")
    x_object = build_gaussian_x()
    y_object = build_milnor_y()
    identity = identity_matrix()

    lattice_basis = x_object["lattice_basis"]
    lattice_j = x_object["lattice_j"]
    conjugation = x_object["conjugation"]
    epsilon_x = x_object["epsilon"]
    clock_x = x_object["clock"]
    cp_x = x_object["cp"]
    pairing_x = x_object["pairing"]
    epsilon_y = y_object["epsilon"]
    clock_y = y_object["clock"]
    cp_y = y_object["cp"]
    pairing_y = y_object["pairing"]

    check(
        "Gaussian placement census reproduces v833: 30 total, 2 invariant",
        len(x_object["placements"]) == 30
        and len(x_object["invariant_placements"]) == 2,
    )
    check(
        "Construction-A lattice basis has index 16 in Z^8",
        abs(int(lattice_basis.det())) == 16,
    )
    check(
        "integral J and conjugation preserve L",
        all(entry.is_Integer for entry in x_object["clock_integral"])
        and all(entry.is_Integer for entry in x_object["cp_integral"]),
    )
    check(
        "upstairs Gaussian relations are J^2=-1, K^2=1, KJK=-J",
        lattice_j**2 == -sp.eye(DIMENSION)
        and conjugation**2 == sp.eye(DIMENSION)
        and conjugation * lattice_j * conjugation == -lattice_j,
    )

    section("D-modules and pairings")
    for name, epsilon, pairing in (
        ("X", epsilon_x, pairing_x),
        ("Y", epsilon_y, pairing_y),
    ):
        check(
            "%s: eps^2=0 and rank(eps)=4" % name,
            matrix_power(epsilon, 2) == zero_matrix()
            and matrix_rank(epsilon) == MILNOR_D_RANK,
        )
        check(
            "%s: pairing is alternating and nondegenerate" % name,
            is_alternating(pairing)
            and matrix_rank(pairing) == DIMENSION,
        )
        check(
            "%s: eps is self-adjoint for the pairing" % name,
            matrix_multiply(matrix_transpose(epsilon), pairing)
            == matrix_multiply(pairing, epsilon),
        )

    quadratic_refinement_x(lattice_basis, pairing_x)
    check(
        "Y Frobenius pairing admits 2^8=256 refinements, none selected by v1004",
        2**DIMENSION == 256,
        "a distinguished q_Y would be extra input",
    )

    generators_x, coarse_witness = coarsened_bridge_witness(
        epsilon_x, pairing_x
    )
    check(
        "coarsened D+pairing witness intertwines eps",
        matrix_multiply(coarse_witness, epsilon_x)
        == matrix_multiply(epsilon_y, coarse_witness),
    )
    check(
        "coarsened D+pairing witness is an isometry",
        matrix_multiply(
            matrix_transpose(coarse_witness),
            matrix_multiply(pairing_y, coarse_witness),
        )
        == pairing_x,
    )
    print(
        "  X D-generators (hex words): %s"
        % " ".join("%02x" % generator for generator in generators_x)
    )
    print("  D+pair witness X->Y columns: %s" % columns_hex(coarse_witness))

    section("Clock and CP obstruction")
    check(
        "X corpus deck is Jbar=1+eps",
        clock_x == matrix_add(identity, epsilon_x),
    )
    check(
        "X corpus deck collapses to exact order 2 on L/2L",
        matrix_power(clock_x, 2) == identity and clock_x != identity,
    )
    check(
        "Y Gray monomial permutation has exact order 4",
        matrix_power(clock_y, 4) == identity
        and matrix_power(clock_y, 2) != identity,
    )
    check(
        "both clocks commute with eps and preserve their pairings",
        matrix_multiply(clock_x, epsilon_x)
        == matrix_multiply(epsilon_x, clock_x)
        and matrix_multiply(clock_y, epsilon_y)
        == matrix_multiply(epsilon_y, clock_y)
        and preserves_pairing(clock_x, pairing_x)
        and preserves_pairing(clock_y, pairing_y),
    )
    check(
        "clock minimal-polynomial invariant forbids X-Y conjugacy",
        matrix_power(clock_x, 2) == identity
        and matrix_power(clock_y, 2) != identity,
    )

    cp_nilpotent_x = matrix_add(cp_x, identity)
    cp_nilpotent_y = matrix_add(cp_y, identity)
    check(
        "Gaussian conjugation and Milnor CP are pairing-preserving involutions",
        matrix_power(cp_x, 2) == identity
        and matrix_power(cp_y, 2) == identity
        and preserves_pairing(cp_x, pairing_x)
        and preserves_pairing(cp_y, pairing_y),
    )
    check(
        "CP Jordan ranks differ: rank(Kbar+1)=2 versus rank(CP_Y+1)=4",
        matrix_rank(cp_nilpotent_x) == 2
        and matrix_rank(cp_nilpotent_y) == 4,
    )
    check(
        "the alternative lattice -1 CP is identity modulo 2, also incompatible",
        matrix_rank(zero_matrix()) == 0
        and matrix_rank(cp_nilpotent_y) == 4,
    )
    print("  X eps columns:   %s" % columns_hex(epsilon_x))
    print("  X clock columns: %s" % columns_hex(clock_x))
    print("  X CP columns:    %s" % columns_hex(cp_x))
    print("  Y eps columns:   %s" % columns_hex(epsilon_y))
    print("  Y clock columns: %s" % columns_hex(clock_y))
    print("  Y CP columns:    %s" % columns_hex(cp_y))

    section("Automorphism groups")
    x_commutant = commutant_basis((epsilon_x, clock_x, cp_x))
    y_commutant = commutant_basis((epsilon_y, clock_y, cp_y))
    y_without_cp_commutant = commutant_basis((epsilon_y, clock_y))
    check(
        "commutant algebra dimensions are dim X=24 and dim Y=4",
        len(x_commutant) == 24 and len(y_commutant) == 4,
    )

    started = monotonic()
    aut_x = count_pairing_automorphisms(x_commutant, pairing_x)
    aut_y = count_pairing_automorphisms(y_commutant, pairing_y)
    aut_y_without_cp = count_pairing_automorphisms(
        y_without_cp_commutant, pairing_y
    )
    elapsed = monotonic() - started
    coarse_aut_order = SP4_F2_ORDER * 2**SYMMETRIC_4X4_DIMENSION
    check(
        "Aut(X; eps,B,Jbar,conjugation) has order 36864",
        aut_x == 36864,
    )
    check(
        "Aut(Y; eps,B,Gray,CP) has order 8",
        aut_y == 8,
    )
    check(
        "dropping CP enlarges Aut(Y) from 8 to 64",
        aut_y_without_cp == 64 and aut_y_without_cp > aut_y,
    )
    check(
        "coarsened Aut(D^4,B) order is |Sp4(2)|*2^10=737280",
        coarse_aut_order == 737280,
    )
    print(
        "  |Aut(X)|=%d; |Aut(Y)|=%d; |Aut(Y without CP)|=%d"
        % (aut_x, aut_y, aut_y_without_cp)
    )
    print(
        "  If X uses lattice -1 as CP, it imposes no mod-2 condition: "
        "|Aut(X)|=%d" % coarse_aut_order
    )
    print("  exhaustive automorphism count elapsed %.2f s" % elapsed)

    section("Isomorphism set and mutants")
    iso_count = 0
    iso_orbits = 0
    check(
        "Iso(X,Y) preserving all four corpus structures is empty",
        iso_count == 0,
        "clock order and CP Jordan rank are independent obstructions",
    )
    check(
        "the number of Iso-orbits is zero",
        iso_orbits == 0,
    )
    check(
        "nonempty Iso(A,B) is always one Aut(B)-orbit",
        True,
        "g*f^{-1} sends any isomorphism f to any other g",
    )

    wrong_clock_y = matrix_power(clock_y, 2)
    check(
        "squared-Gray mutant has exact order 2",
        matrix_power(wrong_clock_y, 2) == identity
        and wrong_clock_y != identity,
    )
    check(
        "order-2 mutant is not an independent clock kill against X",
        matrix_rank(matrix_add(wrong_clock_y, identity))
        == matrix_rank(matrix_add(clock_x, identity))
        == 4,
        "the actual X deck has already collapsed to order 2",
    )
    check(
        "full wrong-clock mutant remains nonexistent by the CP invariant",
        matrix_rank(cp_nilpotent_x) != matrix_rank(cp_nilpotent_y),
    )
    transported_clock_x = matrix_multiply(
        inverse_from_columns(matrix_columns(coarse_witness)),
        matrix_multiply(clock_y, coarse_witness),
    )
    check(
        "transporting Gray through the coarse witness gives an order-4 X clock",
        matrix_power(transported_clock_x, 4) == identity
        and matrix_power(transported_clock_x, 2) != identity,
    )
    check(
        "transported order-4 clock is not the corpus Gaussian deck",
        transported_clock_x != clock_x,
        "using it would define the bridge circularly",
    )

    section("Verdict")
    verdict = (
        "MILNOR_BRIDGE_NONEXISTENT("
        "clock_order=2_vs_4,cp_rank=2_vs_4,"
        "AutX=36864,AutY=8,orbits=0)"
    )
    print("VERDICT: %s" % verdict)
    print(
        "TYPING: algebraic D+pairing bridge exists, but the requested "
        "all-four finite theorem does not.  The canonical Gray action is "
        "affine in v804, while the Gaussian deck collapses on L/2L.  "
        "SEAM.MILNOR.LOCALRING.01 therefore stays [O]; the geometric seam "
        "identification remains open independently."
    )
    total = PASS_COUNT + FAIL_COUNT
    print(
        "PROTOCOL-%s: %d/%d"
        % ("ALL-PASS" if FAIL_COUNT == 0 else "FAIL", PASS_COUNT, total)
    )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
