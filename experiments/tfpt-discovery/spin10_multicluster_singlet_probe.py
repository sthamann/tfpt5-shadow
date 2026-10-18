#!/usr/bin/env python3
r"""spin10_multicluster_singlet_probe -- EXPLORATION ONLY.

Exact Spin(10) singlet census for Lambda^N(k x 16), k=1,2,3, without
constructing a 2^(16k)-dimensional Fock space.  The doubled orthonormal
coordinates of the positive-chirality spinor weights are reused from
spin10_mirror_projector_probe.py:

    {(+/-1,...,+/-1) with an even number of minus signs}.

For a character ch = sum_mu c_mu y^mu, Weyl alternation gives the trivial
representation multiplicity

    mult(1, ch) = sum_{w in W} det(w) c_{rho-w(rho)}.

The coefficient polynomial c_mu(q) of

    product_{spinor weights s} (1 + q y^s)^k

is evaluated only at the 1920 required alternant targets.  A memoized exact
recursion over the 16 distinct weights keeps integer q-polynomials and never
enumerates Fock basis states.  Coordinates are doubled, so all exponents and
rho=(8,6,4,2,0) are integral.

The vector-10 and Spin(9)-restriction calculations are exact destructive
mutants.  This remains a discovery probe: CHIRAL4D.NOMIRROR.01 stays [O].

VERDICT ENUM:
  MULTICLUSTER_SINGLET_FOUND(k,N,multiplicity)
  MULTICLUSTER_SINGLET_OBSTRUCTED(k_max tested)
"""

from __future__ import annotations

import gc
import itertools
import math
import sys
from collections import defaultdict
from functools import lru_cache
from typing import Callable, Iterable


RankWeight = tuple[int, ...]
CoefficientPolynomial = tuple[int, ...]
CHECKS: list[bool] = []

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


def check(name: str, condition: bool, detail: str) -> bool:
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def spin10_chiral_weights_doubled() -> list[RankWeight]:
    """Verified positive-chirality 16 weights from the one-cluster probe."""
    return [
        signs
        for signs in itertools.product((-1, 1), repeat=SPIN10_RANK)
        if sum(value < 0 for value in signs) % 2 == 0
    ]


def spin10_vector_weights_doubled() -> list[RankWeight]:
    """The vector 10 weights +/-e_i in doubled spinor coordinates."""
    weights = []
    for coordinate in range(SPIN10_RANK):
        for sign in (-2, 2):
            weight = [0] * SPIN10_RANK
            weight[coordinate] = sign
            weights.append(tuple(weight))
    return weights


def spin9_spinor_weights_doubled() -> list[RankWeight]:
    """Restriction 16|Spin(9), the B4 spinor with all four sign choices."""
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


def weyl_alternant_targets(
    rho_doubled: RankWeight,
    allow_all_sign_changes: bool,
) -> dict[RankWeight, int]:
    """Return target rho-w(rho) -> det(w) for D_r or B_r."""
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
) -> tuple[list[int], int, int]:
    """Project prod_s(1+q y^s)^copies onto the trivial character exactly."""
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
    def coefficient_polynomial(
        weight_count: int, target: RankWeight
    ) -> CoefficientPolynomial:
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


def direct_exterior_character(
    weights: list[RankWeight], particle_number: int
) -> dict[RankWeight, int]:
    """Small independent character DP used only for validation."""
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


def nonzero_entries(census: Iterable[int]) -> list[tuple[int, int]]:
    return [
        (particle_number, multiplicity)
        for particle_number, multiplicity in enumerate(census)
        if multiplicity
    ]


def expected_full_census(mode_count: int, entries: dict[int, int]) -> list[int]:
    return [entries.get(particle_number, 0) for particle_number in range(mode_count + 1)]


def print_full_table(copies: int, census: list[int]) -> None:
    mode_count = 16 * copies
    print("\nFULL TABLE: k=%d, Lambda^N(%d x 16), %d modes" % (copies, copies, mode_count))
    print("  N                 dim Lambda^N       singlet multiplicity")
    for particle_number, multiplicity in enumerate(census):
        print(
            " %2d %30d %26d"
            % (particle_number, math.comb(mode_count, particle_number), multiplicity)
        )


def run_spin10_census() -> dict[int, list[int]]:
    spinor_weights = spin10_chiral_weights_doubled()
    check(
        "verified chiral-16 weight table",
        len(spinor_weights) == 16
        and len(set(spinor_weights)) == 16
        and all(sum(value < 0 for value in weight) % 2 == 0 for weight in spinor_weights)
        and all(sum(weight[index] for weight in spinor_weights) == 0 for index in range(5)),
        "16 unique even-minus doubled weights; coordinate sums vanish",
    )

    lambda_two_character = direct_exterior_character(spinor_weights, 2)
    lambda_two_highest = d5_highest_weight(lambda_two_character)
    check(
        "known Lambda^2(16)=120 validation",
        sum(lambda_two_character.values()) == math.comb(16, 2)
        and lambda_two_highest == (2, 2, 2, 0, 0),
        "dimension 120; highest doubled weight %s = D5 label (0,0,1,0,0)"
        % (lambda_two_highest,),
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
        check(
            "exact D5 alternant census k=%d" % copies,
            census == expected,
            "%d Weyl targets; %d memo states; nonzero %s"
            % (target_count, cache_entries, nonzero_entries(census)),
        )
        check(
            "particle-hole symmetry k=%d" % copies,
            census == list(reversed(census)),
            "m_N=m_%d-N; total projector rank %d"
            % (16 * copies, sum(census)),
        )

    check(
        "mandatory one-cluster reproduction",
        nonzero_entries(censuses[1]) == [(0, 1), (16, 1)]
        and censuses[1][2] == 0,
        "N=0:1, N=1..15:0, N=16:1; Lambda^2 singlet multiplicity 0",
    )
    check(
        "half-filling decision cases",
        censuses[1][8] == 0 and censuses[2][16] == 27 and censuses[3][24] == 1463,
        "k=1:0; k=2:27 (not unique); k=3:1463 (not unique)",
    )
    return censuses


def run_mutants(reference_censuses: dict[int, list[int]]) -> None:
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
        check(
            "vector-10 mutant k=%d" % copies,
            nonzero_entries(census) == expected,
            "%d D5 targets; nonzero %s" % (target_count, nonzero_entries(census)),
        )
    check(
        "vector mutant changes half filling",
        vector_censuses[1][5] == 0
        and vector_censuses[2][10] == 12
        and vector_censuses[2][10] != reference_censuses[2][16],
        "Lambda^5(10)=0; Lambda^10(10+10)=12 versus spinor k=2 value 27",
    )

    spin9_census, target_count, _cache_entries = exact_singlet_census(
        spin9_spinor_weights_doubled(),
        1,
        SPIN9_RHO_DOUBLED,
        allow_all_sign_changes=True,
    )
    check(
        "Spin(9)-restriction mutant",
        nonzero_entries(spin9_census) == [(0, 1), (8, 1), (16, 1)]
        and spin9_census != reference_censuses[1],
        "%d B4 targets; nonzero %s; a new unique N=8 singlet appears"
        % (target_count, nonzero_entries(spin9_census)),
    )


def main() -> int:
    print("=" * 94)
    print("spin10_multicluster_singlet_probe -- exact Weyl-alternant census")
    print("EXPLORATION ONLY; CHIRAL4D.NOMIRROR.01 stays [O]")
    print("=" * 94)

    censuses = run_spin10_census()
    run_mutants(censuses)

    for copies in COPY_COUNTS:
        print_full_table(copies, censuses[copies])

    print("\nDECISION SUMMARY")
    for copies in COPY_COUNTS:
        half_filling = 8 * copies
        print(
            "  k=%d: N_half=%d, multiplicity=%d, total singlet-projector rank=%d"
            % (
                copies,
                half_filling,
                censuses[copies][half_filling],
                sum(censuses[copies]),
            )
        )

    smallest_half_filled = next(
        (
            (copies, 8 * copies, censuses[copies][8 * copies])
            for copies in COPY_COUNTS
            if censuses[copies][8 * copies]
        ),
        None,
    )
    if smallest_half_filled is None:
        verdict = "MULTICLUSTER_SINGLET_OBSTRUCTED(k_max tested=3)"
    else:
        verdict = "MULTICLUSTER_SINGLET_FOUND(%d,%d,%d)" % smallest_half_filled

    print("\nVERDICT: %s" % verdict)
    print(
        "INTERPRETATION: k counts identical positive-chirality 16 copies, not a "
        "16 plus conjugate-16 vector-like pair.  The physical k=3 mirror content "
        "has 1463 half-filled singlets.  Fermion-number-preserving Casimir "
        "projection therefore does not meet the proposed uniqueness test at k=2 "
        "or k=3; SMG interactions that violate fermion number lie outside this census."
    )
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("=" * 94)
    return 0 if all(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
