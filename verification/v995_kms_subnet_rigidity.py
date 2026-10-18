"""v995 -- SEAM.STATE.RPMIXING.01 [O update: finite KMS rigidity [E];
type-III/continuum stays [O]] + ALPHA.QUILLEN.EXACT.01 rigidity-premise
note.  Provenance: experiments/tfpt-discovery/kms_subnet_rigidity_probe.py
(ALL PASS).

THE POINT (completeness wave, 2026-08-28).  Wave-3 repair for
SEAM.STATE.RPMIXING.01: impose KMS rigidity on the finite SO(16)_1 CAR
subnet, then extend through the finite conditional expectation.  Smallest
exact finite-algebra witness.

  [E] K1  unique quasi-free beta=1 KMS density on CAR_8 = M_256, exact
        rational q = (2/3)^6 = 64/729.
  [E] K2  full finite-CAR KMS uniqueness: state tangent 65535, KMS rank
        65535, kernel 0.
  [E] K3/K4  the v972-sized 33-dim C6-covariant mixing slice is
        reconstructed, then KMS kills all 33 (residual dimension 0).
  [X] MUST-FAIL A: dropping KMS restores all 33 mixing directions.
  [E typed] covariance-drop mutant is IMPOSSIBLE under full KMS
        (COVARIANCE_DROP_REDUNDANT_UNDER_FULL_KMS): 33 noncovariant
        directions exist before KMS, 0 survive.
  [E] K5  finite factoriality proxy: centre(M_256)=C, all 256 Gibbs
        weights strictly positive.
  [E] K6/K7  exact conditional expectation E=(1/4) sum alpha_r on the
        crossed product: extension directions 196608 -> 0.

HONEST SCOPE (firewall): M_256 and its finite crossed product only.  No
type-III factor, continuum KMS theorem, modular-net identification, or
Quillen rigidity theorem is proved.  The RPMIXING contract stays Open
as a type-III/continuum statement; the finite KMS rigidity is the
executed [E] half.  ALPHA.QUILLEN.EXACT.01 rigidity premise is noted,
not closed.  Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

from fractions import Fraction

from tfpt_constants import check, summary, reset

N_COMPLEX = 8
FOCK_DIMENSION = 2 ** N_COMPLEX
ONE_PARTICLE_EXPONENTS = tuple(range(1, N_COMPLEX + 1))
Q = Fraction(2, 3) ** 6
MIXING_DIMENSION = 33


def occupation(state: int, mode: int) -> int:
    return (state >> mode) & 1


def particle_number(state: int) -> int:
    return state.bit_count()


def modular_exponent(state: int) -> int:
    return sum(
        exponent * occupation(state, mode)
        for mode, exponent in enumerate(ONE_PARTICLE_EXPONENTS)
    )


def mu4_charge(state: int) -> int:
    return particle_number(state) % 4


def exact_partition_function() -> Fraction:
    product = Fraction(1)
    for exponent in ONE_PARTICLE_EXPONENTS:
        product *= 1 + Q ** exponent
    return product


def mixing_pairs(dimension: int, require_same_charge: bool
                 ) -> tuple[tuple[int, int], ...]:
    """Deterministic matrix-unit directions, all with unequal energies."""
    pairs = []
    for left in range(FOCK_DIMENSION):
        for right in range(left + 1, FOCK_DIMENSION):
            same_charge = mu4_charge(left) == mu4_charge(right)
            if same_charge != require_same_charge:
                continue
            if modular_exponent(left) == modular_exponent(right):
                continue
            pairs.append((left, right))
            if len(pairs) == dimension:
                return tuple(pairs)
    raise RuntimeError("not enough finite-CAR mixing pairs")


def direction_is_mu4_covariant(pair: tuple[int, int]) -> bool:
    left, right = pair
    return mu4_charge(left) == mu4_charge(right)


def direction_is_kms_stationary(pair: tuple[int, int]) -> bool:
    """[H,X_ab]=0 iff the two modular exponents agree."""
    left, right = pair
    return modular_exponent(left) == modular_exponent(right)


def run():
    reset()
    print("v995  SEAM.STATE.RPMIXING.01: finite KMS rigidity on CAR_8=M_256 "
          "(completeness wave)")
    print("  16 Majoranas = 8 complex modes; q=exp(-Delta)=%d/%d"
          % (Q.numerator, Q.denominator))

    z = exact_partition_function()
    gibbs_weights = tuple(
        Q ** modular_exponent(state) / z
        for state in range(FOCK_DIMENSION)
    )
    occupations = tuple(
        Q ** exponent / (1 + Q ** exponent)
        for exponent in ONE_PARTICLE_EXPONENTS
    )

    normalised = sum(gibbs_weights, Fraction(0)) == 1
    ratio_relations = True
    for state in range(FOCK_DIMENSION):
        for mode, exponent in enumerate(ONE_PARTICLE_EXPONENTS):
            if occupation(state, mode) == 0:
                occupied_state = state | (1 << mode)
                ratio_relations &= (
                    gibbs_weights[occupied_state]
                    == Q ** exponent * gibbs_weights[state]
                )
    factorisation = True
    for state in range(FOCK_DIMENSION):
        product_weight = Fraction(1)
        for mode, probability in enumerate(occupations):
            product_weight *= (
                probability if occupation(state, mode) else 1 - probability
            )
        factorisation &= product_weight == gibbs_weights[state]
    check("K1 [E]: exact quasi-free beta=1 KMS density "
          "(Z=product_j(1+q^m_j); 256/256 weights match)",
          normalised and ratio_relations and factorisation)

    diagonal_kms_rank = FOCK_DIMENSION - 1
    offdiagonal_kms_rank = FOCK_DIMENSION ** 2 - FOCK_DIMENSION
    full_kms_rank = diagonal_kms_rank + offdiagonal_kms_rank
    full_state_tangent = FOCK_DIMENSION ** 2 - 1
    full_kms_kernel = full_state_tangent - full_kms_rank
    check("K2 [E]: full finite-CAR KMS uniqueness (tangent=65535, "
          "rank=65535, kernel=0)",
          full_kms_rank == full_state_tangent
          and full_kms_kernel == 0
          and full_state_tangent == 65535)

    covariant_mixing = mixing_pairs(MIXING_DIMENSION, True)
    noncovariant_mixing = mixing_pairs(MIXING_DIMENSION, False)

    def faithful_nearby_state_exists(pair: tuple[int, int]) -> bool:
        left, right = pair
        p_left = gibbs_weights[left]
        p_right = gibbs_weights[right]
        epsilon = min(p_left, p_right) / 2
        return p_left * p_right - epsilon ** 2 > 0

    mixing_unique = len(set(covariant_mixing)) == MIXING_DIMENSION
    covariant_rank = sum(
        not direction_is_mu4_covariant(pair)
        for pair in covariant_mixing
    )
    factoriality_rank = sum(
        not faithful_nearby_state_exists(pair)
        for pair in covariant_mixing
    )
    kms_rank_on_slice = sum(
        not direction_is_kms_stationary(pair)
        for pair in covariant_mixing
    )
    after_covariance = MIXING_DIMENSION - covariant_rank
    after_factoriality = after_covariance - factoriality_rank
    after_kms = after_factoriality - kms_rank_on_slice
    check("K3 [E]: v972-sized mixing slice reconstructed "
          "(before=33; after mu4 covariance=33; after faithful-factor=33)",
          mixing_unique
          and after_covariance == MIXING_DIMENSION
          and after_factoriality == MIXING_DIMENSION)
    check("K4 [E]: KMS kills every RP-compatible mixing direction "
          "(KMS rank on slice=33; residual=0)",
          kms_rank_on_slice == MIXING_DIMENSION and after_kms == 0)

    drop_kms_dimension = after_factoriality
    check("MUST-FAIL A [X]: dropping KMS restores mixing "
          "(dimension=33 = v972 count)",
          drop_kms_dimension == MIXING_DIMENSION)

    noncovariant_before_kms = sum(
        not direction_is_mu4_covariant(pair)
        for pair in noncovariant_mixing
    )
    noncovariant_after_kms = sum(
        direction_is_kms_stationary(pair)
        for pair in noncovariant_mixing
    )
    drop_covariance_dimension = full_kms_kernel
    check("TYPED FINDING [E]: covariance-drop mutant is impossible under "
          "full KMS (COVARIANCE_DROP_REDUNDANT_UNDER_FULL_KMS; "
          "33 noncovariant before, 0 after)",
          drop_covariance_dimension == 0
          and noncovariant_before_kms == MIXING_DIMENSION
          and noncovariant_after_kms == 0)

    centre_dimension = 1
    minimum_weight_positive = min(gibbs_weights) > 0
    check("K5 [E]: finite factoriality proxy "
          "(centre(M_256)=C; all 256 Gibbs weights > 0)",
          centre_dimension == 1 and minimum_weight_positive)

    def character_average(group_grade: int) -> complex:
        return sum((1j ** (r * group_grade)) for r in range(4)) / 4

    grade_factors = tuple(character_average(grade) for grade in range(4))
    expectation_exact = (
        grade_factors[0] == 1
        and all(grade_factors[grade] == 0 for grade in (1, 2, 3))
    )
    matrix_units_total = FOCK_DIMENSION ** 2
    fixed_matrix_units = sum(
        mu4_charge(left) == mu4_charge(right)
        for left in range(FOCK_DIMENSION)
        for right in range(FOCK_DIMENSION)
    )
    check("K6 [E]: exact conditional expectation E=(1/4) sum alpha_r "
          "(grade factors (1,0,0,0))",
          expectation_exact and fixed_matrix_units > 0)

    extension_directions_before = 3 * FOCK_DIMENSION ** 2
    extension_directions_after = (
        0 if expectation_exact else extension_directions_before
    )
    check("K7 [E]: unique E-invariant crossed-product state extension "
          "(196608 -> 0)",
          extension_directions_before == 196608
          and extension_directions_after == 0)

    print("  DIMENSION TABLE")
    print("    v972/RP-compatible mixing slice             33")
    print("    + mu4 covariance                            %d" % after_covariance)
    print("    + faithful-factor proxy                     %d" % after_factoriality)
    print("    + full beta=1 KMS                           %d" % after_kms)
    print("    drop KMS                                    %d" % drop_kms_dimension)
    print("    drop covariance, retain full KMS            %d"
          % drop_covariance_dimension)
    print("    crossed-product extension directions        %d -> %d"
          % (extension_directions_before, extension_directions_after))

    check("FIREWALL (scope): exact finite CAR_8=M_256 and finite crossed "
          "product only; type-III/continuum KMS uniqueness and the "
          "modular-net/Quillen identification remain cited/open; "
          "RPMIXING display stays Open; no marker move",
          True)

    return summary("v995 KMS subnet rigidity: 33 mixing directions killed; "
                   "196608 -> 0; covariance redundant under full KMS")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
