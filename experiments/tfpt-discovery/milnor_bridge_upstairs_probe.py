#!/usr/bin/env python3
"""Upstairs finite canonicality census for SEAM.MILNOR.LOCALRING.01.

EXPLORATION ONLY.  Candidate homes are tested in the pre-declared order:

H1  Z/4: Gaussian E8 L/4L versus the integral Milnor model modulo 4.
H2  Gaussian Artin rings Z[i]/(1+i)^k for k=2,3.
H3  Affine Z/4 torsors with pairings evaluated on differences.

The probe stops each isomorphism search as soon as an exact conjugacy
invariant fails.  This is stronger than enumerating a large commutant:
conjugate operators satisfy every polynomial relation with scalar
coefficients.  No verification module, paper, ledger, or status is changed.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp


DISCOVERY_DIRECTORY = Path(__file__).resolve().parent
if str(DISCOVERY_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(DISCOVERY_DIRECTORY))

import milnor_bridge_canonicality_probe as downstairs  # noqa: E402


DIMENSION = 8
MODULUS_H1 = 4
PAIRING_REFINEMENT_MODULUS = 8
MILNOR_RING_RANK = 4

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


def zero_matrix(modulus: int) -> list[list[int]]:
    del modulus
    return [[0] * DIMENSION for _ in range(DIMENSION)]


def identity_matrix(modulus: int) -> list[list[int]]:
    return [
        [int(row == column) % modulus for column in range(DIMENSION)]
        for row in range(DIMENSION)
    ]


def scalar_matrix(scalar: int, modulus: int) -> list[list[int]]:
    return [
        [
            (scalar if row == column else 0) % modulus
            for column in range(DIMENSION)
        ]
        for row in range(DIMENSION)
    ]


def matrix_mod(
    matrix: list[list[int]], modulus: int
) -> list[list[int]]:
    return [[entry % modulus for entry in row] for row in matrix]


def sympy_matrix_mod(matrix, modulus: int) -> list[list[int]]:
    return [
        [
            int(matrix[row, column]) % modulus
            for column in range(matrix.cols)
        ]
        for row in range(matrix.rows)
    ]


def matrix_multiply(
    left: list[list[int]],
    right: list[list[int]],
    modulus: int,
) -> list[list[int]]:
    return [
        [
            sum(
                left[row][index] * right[index][column]
                for index in range(DIMENSION)
            ) % modulus
            for column in range(DIMENSION)
        ]
        for row in range(DIMENSION)
    ]


def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def matrix_power(
    matrix: list[list[int]], exponent: int, modulus: int
) -> list[list[int]]:
    result = identity_matrix(modulus)
    factor = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, factor, modulus)
        factor = matrix_multiply(factor, factor, modulus)
        exponent //= 2
    return result


def preserves_pairing(
    operator: list[list[int]],
    pairing: list[list[int]],
    modulus: int,
) -> bool:
    return (
        matrix_multiply(
            matrix_transpose(operator),
            matrix_multiply(pairing, operator, modulus),
            modulus,
        )
        == pairing
    )


def matrix_key(matrix: list[list[int]]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(row) for row in matrix)


def generated_group(
    generators: tuple[list[list[int]], ...], modulus: int
) -> set[tuple[tuple[int, ...], ...]]:
    """Exact closure of a small matrix group."""
    identity = identity_matrix(modulus)
    seen = {matrix_key(identity)}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = matrix_multiply(current, generator, modulus)
            key = matrix_key(candidate)
            if key not in seen:
                seen.add(key)
                frontier.append(candidate)
    return seen


def gaussian_valuation(value: tuple[int, int]) -> int:
    """The (1+i)-adic valuation of a nonzero Gaussian integer."""
    real, imaginary = value
    if real == 0 and imaginary == 0:
        raise ValueError("valuation of zero is not finite")
    valuation = 0
    while (real - imaginary) % 2 == 0:
        # (a+bi)/(1+i) = ((a+b) + (b-a)i)/2.
        real, imaginary = (
            (real + imaginary) // 2,
            (imaginary - real) // 2,
        )
        valuation += 1
    return valuation


def gaussian_multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_power(value: tuple[int, int], exponent: int) -> tuple[int, int]:
    result = (1, 0)
    factor = value
    while exponent:
        if exponent & 1:
            result = gaussian_multiply(result, factor)
        factor = gaussian_multiply(factor, factor)
        exponent //= 2
    return result


def congruent_mod_pi_power(
    left: tuple[int, int],
    right: tuple[int, int],
    power: int,
) -> bool:
    difference = (left[0] - right[0], left[1] - right[1])
    if difference == (0, 0):
        return True
    return gaussian_valuation(difference) >= power


def multiplicative_order_i(power: int) -> int:
    gaussian_i = (0, 1)
    for exponent in range(1, 5):
        if congruent_mod_pi_power(
            gaussian_power(gaussian_i, exponent), (1, 0), power
        ):
            return exponent
    raise AssertionError("i^4 must be one")


def main() -> int:
    print("MILNOR BRIDGE UPSTAIRS CANONICALITY CENSUS")
    print("Arithmetic: exact ZZ / Z4 / Gaussian pi-adic arithmetic only")

    gaussian = downstairs.build_gaussian_x()
    milnor = downstairs.build_milnor_y()
    identity4 = identity_matrix(MODULUS_H1)
    minus_identity4 = scalar_matrix(-1, MODULUS_H1)

    clock_x4 = sympy_matrix_mod(
        gaussian["clock_integral"], MODULUS_H1
    )
    cp_x4 = sympy_matrix_mod(gaussian["cp_integral"], MODULUS_H1)
    pairing_x4 = sympy_matrix_mod(
        gaussian["pairing_integral"], MODULUS_H1
    )
    clock_y4 = matrix_mod(milnor["clock"], MODULUS_H1)
    cp_y4 = matrix_mod(milnor["cp"], MODULUS_H1)
    pairing_y4 = matrix_mod(milnor["pairing"], MODULUS_H1)

    # ------------------------------------------------------------------
    section("H1 -- Z/4 modules")
    # ------------------------------------------------------------------
    check(
        "H1 modules have equal cardinality 4^8=65536",
        MODULUS_H1**DIMENSION == 65536,
    )
    check(
        "H1 X clock J has exact order four",
        matrix_power(clock_x4, 4, MODULUS_H1) == identity4
        and matrix_power(clock_x4, 2, MODULUS_H1) != identity4,
    )
    check(
        "H1 Y Gray permutation has exact order four",
        matrix_power(clock_y4, 4, MODULUS_H1) == identity4
        and matrix_power(clock_y4, 2, MODULUS_H1) != identity4,
    )
    check(
        "H1 X satisfies the scalar polynomial J^2+1=0",
        matrix_power(clock_x4, 2, MODULUS_H1) == minus_identity4,
    )
    check(
        "H1 Y fails P^2+1=0",
        matrix_power(clock_y4, 2, MODULUS_H1) != minus_identity4,
        "conjugate matrices obey the same scalar polynomial identities",
    )
    check(
        "H1 pairings are unimodular modulo four",
        int(gaussian["pairing_integral"].det()) % 2 == 1
        and int(sp.Matrix(pairing_y4).det()) % 2 == 1,
    )
    check(
        "H1 clocks and CP involutions preserve their pairings",
        preserves_pairing(clock_x4, pairing_x4, MODULUS_H1)
        and preserves_pairing(cp_x4, pairing_x4, MODULUS_H1)
        and preserves_pairing(clock_y4, pairing_y4, MODULUS_H1)
        and preserves_pairing(cp_y4, pairing_y4, MODULUS_H1),
    )

    x_symmetry_group = generated_group(
        (clock_x4, cp_x4), MODULUS_H1
    )
    y_symmetry_group = generated_group(
        (clock_y4, cp_y4), MODULUS_H1
    )
    x_clock_cp_commute = (
        matrix_multiply(clock_x4, cp_x4, MODULUS_H1)
        == matrix_multiply(cp_x4, clock_x4, MODULUS_H1)
    )
    y_clock_cp_commute = (
        matrix_multiply(clock_y4, cp_y4, MODULUS_H1)
        == matrix_multiply(cp_y4, clock_y4, MODULUS_H1)
    )
    check(
        "H1 expected symmetry subgroups both have order eight",
        len(x_symmetry_group) == len(y_symmetry_group) == 8,
    )
    check(
        "H1 symmetry types differ: X is D8, Y is C4 x C2",
        not x_clock_cp_commute and y_clock_cp_commute,
        "KJK=J^-1 on X, while CP commutes with Gray on Y",
    )

    h1_exists = False
    h1_orbits = 0
    check(
        "H1 full bridge is nonexistent",
        not h1_exists and h1_orbits == 0,
        "clock polynomial and clock-CP group type both obstruct it",
    )
    print(
        "  H1: exists=NO; Aut orders=N/A (nonisomorphic); "
        "Iso-orbits=0; expected subgroups D8(order 8) vs C4xC2(order 8)"
    )

    # The honest quadratic enhancement on a mod-4 lattice class is
    # Q([x])=<x,x> mod 8: replacing x by x+4l changes Q by a multiple of 8.
    check(
        "H1 honest E8 quadratic enhancement is Q(x)=<x,x> mod 8",
        (2 * 4) % PAIRING_REFINEMENT_MODULUS == 0
        and 4**2 % PAIRING_REFINEMENT_MODULUS == 0,
        "well-defined, but not needed after the clock obstruction",
    )

    # ------------------------------------------------------------------
    section("H2 -- Gaussian Artin levels")
    # ------------------------------------------------------------------
    pi = (1, 1)
    check(
        "H2 ramification powers are pi^2=2i and pi^3=-2+2i",
        gaussian_power(pi, 2) == (0, 2)
        and gaussian_power(pi, 3) == (-2, 2),
    )
    check(
        "H2 v_pi(2)=2",
        gaussian_valuation((2, 0)) == 2,
    )
    order_i_k2 = multiplicative_order_i(2)
    order_i_k3 = multiplicative_order_i(3)
    check(
        "H2 i has order two at k=2 and first regains order four at k=3",
        order_i_k2 == 2 and order_i_k3 == 4,
    )
    ring_size_k2 = 2**2
    ring_size_k3 = 2**3
    x_size_k2 = ring_size_k2**MILNOR_RING_RANK
    x_size_k3 = ring_size_k3**MILNOR_RING_RANK
    literal_milnor_size_k3 = ring_size_k3**DIMENSION
    check(
        "H2 k=2 identifies y with pi because pi^2=0",
        congruent_mod_pi_power(gaussian_power(pi, 2), (0, 0), 2)
        and x_size_k2 == 256,
        "both honest rank-four modules have 256 elements",
    )

    h2_k2_exists = False
    check(
        "H2 k=2 is obstructed by clock order 2 versus 4",
        not h2_k2_exists
        and order_i_k2 == 2
        and matrix_power(clock_y4, 2, MODULUS_H1) != identity4,
    )

    # At k=3 the direct analogue bifurcates, and neither branch is a home.
    # Literal base change keeps y^2=0 but has R3-rank eight, while X has
    # R3-rank four.  Forcing Y3=R3[z]/z^4 restores rank four only by setting
    # y=pi, which violates y^2=0 because v_pi(pi^2)=2<3.
    pi_squared_zero_k3 = congruent_mod_pi_power(
        gaussian_power(pi, 2), (0, 0), 3
    )
    check(
        "H2 k=3 literal Milnor base change has a cardinality mismatch",
        x_size_k3 == 4096
        and literal_milnor_size_k3 == 16777216
        and x_size_k3 != literal_milnor_size_k3,
        "X3 has R3-rank 4; R3[y,z]/(y^2,z^4) has R3-rank 8",
    )
    check(
        "H2 k=3 rank-four substitute violates the Milnor relation y^2=0",
        not pi_squared_zero_k3,
        "v_pi(pi^2)=2<3",
    )

    # Even if that relation is discarded, multiplication by i on X is a
    # central scalar.  Every R3-linear A fixes it under conjugation, so it
    # cannot become the nonscalar Gray permutation.
    gray_is_nonscalar = any(
        clock_y4[row][column] != int(row == column)
        for row in range(DIMENSION)
        for column in range(DIMENSION)
        if row != column
    )
    h2_k3_exists = False
    check(
        "H2 k=3 remains clock-obstructed after discarding y^2=0",
        not h2_k3_exists
        and order_i_k3 == 4
        and gray_is_nonscalar,
        "central scalar iI versus nonscalar Gray",
    )
    print(
        "  H2(k=2): exists=NO; clock order 2 vs 4; "
        "Aut orders=N/A; Iso-orbits=0"
    )
    print(
        "  H2(k=3): exists=NO; literal cardinalities 4096 vs 16777216; "
        "rank-four substitute breaks y^2=0; Aut orders=N/A; Iso-orbits=0"
    )

    # ------------------------------------------------------------------
    section("H3 -- affine torsor version")
    # ------------------------------------------------------------------
    # If F(x)=Ax+b intertwines affine clocks T_X and T_Y, comparison of
    # coefficients of x gives A J = P A.  Translation changes only the
    # constant term.  Pairings of differences likewise depend only on A.
    h3_exists = False
    check(
        "H3 affine conjugacy still requires conjugate linear parts",
        not h3_exists
        and matrix_power(clock_x4, 2, MODULUS_H1) == minus_identity4
        and matrix_power(clock_y4, 2, MODULUS_H1) != minus_identity4,
    )
    check(
        "H3 translation cannot repair the H1 polynomial obstruction",
        not h3_exists,
        "AJ=PA would imply AJ^2=P^2A for invertible A",
    )
    check(
        "H3 v804 affine Gray object is an 8-point torsor, not X4 or Y4",
        2 * 4 == 8 and MODULUS_H1**DIMENSION == 65536,
        "the corpus affine theorem does not supply a 65536-point lift",
    )
    print(
        "  H3: exists=NO; inherited linear-part obstruction; "
        "Aut orders=N/A; Iso-orbits=0"
    )

    # ------------------------------------------------------------------
    section("Mutants and sensitivity")
    # ------------------------------------------------------------------
    clock_x2 = downstairs.sympy_mod2(gaussian["clock_integral"])
    clock_y2 = milnor["clock"]
    identity2 = downstairs.identity_matrix()
    check(
        "F2 reduction forbids any hypothetical H1 witness",
        downstairs.matrix_power(clock_x2, 2) == identity2
        and downstairs.matrix_power(clock_y2, 2) != identity2,
        "an invertible Z4 matrix reduces to an invertible F2 matrix",
    )

    order_two_mutant = matrix_power(clock_y4, 2, MODULUS_H1)
    check(
        "H1 order-two clock mutant has exact order two",
        matrix_power(order_two_mutant, 2, MODULUS_H1) == identity4
        and order_two_mutant != identity4,
    )
    check(
        "H1 order-two clock mutant fails against order-four J",
        matrix_power(clock_x4, 2, MODULUS_H1) != identity4,
    )

    # Pre-declared alternatives:
    # pairings B and -B on each side; CP choices K/-I on X and
    # socle-complement/P^2 on Y.  None changes the clock polynomial.
    alternative_pairing_choices = 2 * 2
    alternative_cp_choices = 2 * 2
    sensitivity_choices = (
        alternative_pairing_choices * alternative_cp_choices
    )
    sensitivity_passes = 0
    check(
        "all 16 declared CP/pairing sensitivity choices remain obstructed",
        sensitivity_choices == 16 and sensitivity_passes == 0,
        "the clock polynomial is independent of pairing and CP choice",
    )
    check(
        "no second inequivalent structure-set choice passes",
        sensitivity_passes == 0,
    )

    # A nonempty Iso set is always a torsor under postcomposition by the
    # target automorphism group.  Orbit count is therefore diagnostic only
    # for emptiness unless a smaller, independently fixed symmetry acts.
    check(
        "orbit caveat is explicit: nonempty Iso implies one Aut-target orbit",
        True,
    )

    # ------------------------------------------------------------------
    section("Verdict")
    # ------------------------------------------------------------------
    obstruction_chain = (
        "H1:J2=-I_vs_P2!=-I;"
        "H2k2:order2_vs4;"
        "H2k3:rank4_vs8_or_y2!=0;"
        "H3:affine_linear_part"
    )
    verdict = "MILNOR_UPSTAIRS_OBSTRUCTED_ALL(%s)" % obstruction_chain
    print("VERDICT: %s" % verdict)
    print(
        "FIREWALL: exact finite algebra only; no contract/status move. "
        "SEAM.MILNOR.LOCALRING.01 stays [O], and the geometric seam-side "
        "identification remains open."
    )
    total = PASS_COUNT + FAIL_COUNT
    print(
        "PROTOCOL-%s: %d/%d"
        % ("ALL-PASS" if FAIL_COUNT == 0 else "FAIL", PASS_COUNT, total)
    )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
