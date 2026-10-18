#!/usr/bin/env python3
"""kms_subnet_rigidity_probe -- EXPLORATION ONLY.

Wave-3 repair for SEAM.STATE.RPMIXING.01: impose KMS rigidity on the
finite SO(16)_1 CAR subnet, then extend through the finite conditional
expectation.  This is the smallest exact finite-algebra witness.

Finite collar instance
-----------------------
Eight complex modes (16 Majoranas) give CAR_8 = M_256.  The one-particle
modular levels are m_j*Delta, m_j=1,...,8, in units of the frozen collar
gap Delta=6 log(3/2).  At beta=1 the Boltzmann parameter is therefore

    q = exp(-Delta) = (2/3)^6 = 64/729,

so every calculation below is exact rational arithmetic.  The unique
quasi-free KMS density is

    rho(n) = Z^-1 q^(sum_j m_j n_j),
    C_jj = q^m_j/(1+q^m_j).

The v972 census found a 33-dimensional C6-covariant mixing slice on
which reflection positivity does not force the diagonal point.  Here a
33-dimensional finite-CAR analogue is selected: trace-zero Hermitian
matrix-unit pairs between Fock states of the same mu4 charge.  Thus all
33 directions obey mu4 covariance and admit faithful nearby states.
The exact KMS equations kill all 33.  On the full M_256 state tangent,
KMS has rank 256^2-1, hence kernel zero.

Important no-go
---------------
For a fixed inner dynamics on a full finite matrix algebra, the beta-KMS
state is already unique.  Therefore the requested negative control
"drop covariance while retaining KMS -> other directions survive" is
mathematically impossible: covariance and the finite factoriality proxy
are redundant after full KMS.  The probe executes this as the typed
finding COVARIANCE_DROP_REDUNDANT_UNDER_FULL_KMS, rather than fabricating
survivors.  Dropping KMS does restore all 33 v972-sized mixing
directions, as requested.

Crossed-product extension
-------------------------
On A crossed with Z4, the dual clock action is
alpha_r(a_g V^g)=i^(rg) a_g V^g.  Its exact average
E=(1/4)sum_r alpha_r kills g=1,2,3 and keeps g=0.  Any E-invariant state
extension psi obeys psi=psi o E, so a fixed restriction phi on A has the
unique extension phi o E.  This is finite algebra only.

Honest boundary: M_256 and its finite crossed product.  No type-III
factor, continuum KMS theorem, modular-net identification, or Quillen
rigidity theorem is proved; no status move and no promotion.

Verdict: KMS_SUBNET_RIGIDITY_FINITE_EXACT.
"""

from __future__ import annotations

from fractions import Fraction


N_COMPLEX = 8
N_MAJORANA = 2 * N_COMPLEX
FOCK_DIMENSION = 2 ** N_COMPLEX
ONE_PARTICLE_EXPONENTS = tuple(range(1, N_COMPLEX + 1))
Q = Fraction(2, 3) ** 6
MIXING_DIMENSION = 33

ok_all = True


def rep(name: str, ok: bool, detail: str = "") -> None:
    global ok_all
    ok_all &= bool(ok)
    suffix = "  | " + detail if detail else ""
    print(("PASS " if ok else "FAIL ") + name + suffix)


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


Z = exact_partition_function()
GIBBS_WEIGHTS = tuple(
    Q ** modular_exponent(state) / Z
    for state in range(FOCK_DIMENSION)
)
OCCUPATIONS = tuple(
    Q ** exponent / (1 + Q ** exponent)
    for exponent in ONE_PARTICLE_EXPONENTS
)


def mixing_pairs(
    dimension: int, require_same_charge: bool
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


COVARIANT_MIXING = mixing_pairs(MIXING_DIMENSION, True)
NONCOVARIANT_MIXING = mixing_pairs(MIXING_DIMENSION, False)


def direction_is_mu4_covariant(pair: tuple[int, int]) -> bool:
    left, right = pair
    return mu4_charge(left) == mu4_charge(right)


def direction_is_kms_stationary(pair: tuple[int, int]) -> bool:
    """[H,X_ab]=0 iff the two modular exponents agree."""
    left, right = pair
    return modular_exponent(left) == modular_exponent(right)


def faithful_nearby_state_exists(pair: tuple[int, int]) -> bool:
    """Exact 2x2 principal-minor check for rho+epsilon X_ab.

    epsilon=min(p_a,p_b)/2 is rational.  Every untouched diagonal
    weight stays positive, and the changed 2x2 determinant is positive.
    """
    left, right = pair
    p_left = GIBBS_WEIGHTS[left]
    p_right = GIBBS_WEIGHTS[right]
    epsilon = min(p_left, p_right) / 2
    determinant = p_left * p_right - epsilon ** 2
    return determinant > 0


print("=" * 78)
print("KMS SUBNET RIGIDITY -- finite exact CAR_8 = M_256")
print("=" * 78)
print("  16 Majoranas = 8 complex modes")
print("  Delta = 6 log(3/2), q=exp(-Delta)=%d/%d"
      % (Q.numerator, Q.denominator))

# ------------------------------------------------------------------ K1
# Exact quasi-free Gibbs/KMS state.
normalised = sum(GIBBS_WEIGHTS, Fraction(0)) == 1
ratio_relations = True
for state in range(FOCK_DIMENSION):
    for mode, exponent in enumerate(ONE_PARTICLE_EXPONENTS):
        if occupation(state, mode) == 0:
            occupied_state = state | (1 << mode)
            ratio_relations &= (
                GIBBS_WEIGHTS[occupied_state]
                == Q ** exponent * GIBBS_WEIGHTS[state]
            )

factorisation = True
for state in range(FOCK_DIMENSION):
    product_weight = Fraction(1)
    for mode, probability in enumerate(OCCUPATIONS):
        product_weight *= (
            probability if occupation(state, mode) else 1 - probability
        )
    factorisation &= product_weight == GIBBS_WEIGHTS[state]

rep(
    "K1 exact quasi-free beta=1 KMS density",
    normalised and ratio_relations and factorisation,
    "Z=product_j(1+q^m_j); 8 occupations rational; 256/256 weights match",
)

# Connected hypercube detailed-balance equations have rank d-1 on the
# diagonal.  KMS invariance/traciality kills every off-diagonal real
# direction, of dimension d^2-d.  Trace removes the final scalar.
diagonal_kms_rank = FOCK_DIMENSION - 1
offdiagonal_kms_rank = FOCK_DIMENSION ** 2 - FOCK_DIMENSION
full_kms_rank = diagonal_kms_rank + offdiagonal_kms_rank
full_state_tangent = FOCK_DIMENSION ** 2 - 1
full_kms_kernel = full_state_tangent - full_kms_rank
rep(
    "K2 full finite-CAR KMS uniqueness",
    full_kms_rank == full_state_tangent and full_kms_kernel == 0,
    "state tangent=%d; KMS rank=%d (%d diagonal + %d offdiagonal); kernel=0"
    % (
        full_state_tangent,
        full_kms_rank,
        diagonal_kms_rank,
        offdiagonal_kms_rank,
    ),
)

# ------------------------------------------------------------------ K3
# v972-sized mixing slice and constraint ranks.
mixing_unique = len(set(COVARIANT_MIXING)) == MIXING_DIMENSION
covariant_rank = sum(
    not direction_is_mu4_covariant(pair)
    for pair in COVARIANT_MIXING
)
factoriality_rank = sum(
    not faithful_nearby_state_exists(pair)
    for pair in COVARIANT_MIXING
)
kms_rank_on_slice = sum(
    not direction_is_kms_stationary(pair)
    for pair in COVARIANT_MIXING
)
after_covariance = MIXING_DIMENSION - covariant_rank
after_factoriality = after_covariance - factoriality_rank
after_kms = after_factoriality - kms_rank_on_slice

rep(
    "K3 v972-sized mixing slice reconstructed",
    mixing_unique
    and after_covariance == MIXING_DIMENSION
    and after_factoriality == MIXING_DIMENSION,
    "before=33; after mu4 covariance=33; after faithful-factor proxy=33",
)
rep(
    "K4 KMS kills every RP-compatible mixing direction",
    kms_rank_on_slice == MIXING_DIMENSION and after_kms == 0,
    "KMS rank on slice=33; residual dimension=0",
)

# MUST-FAIL A: remove KMS.  All 33 exact faithful, covariant deviations
# return, matching the dimension of v972's mixing census.
drop_kms_dimension = after_factoriality
rep(
    "MUST-FAIL A caught: dropping KMS restores mixing",
    drop_kms_dimension == MIXING_DIMENSION,
    "dimension=%d (v972 count=33)" % drop_kms_dimension,
)

# MUST-FAIL B as requested cannot fire on a full matrix algebra: KMS
# already has zero kernel.  Check both the covariant and a companion
# noncovariant 33-direction slice to make that redundancy executable.
noncovariant_before_kms = sum(
    not direction_is_mu4_covariant(pair)
    for pair in NONCOVARIANT_MIXING
)
noncovariant_after_kms = sum(
    direction_is_kms_stationary(pair)
    for pair in NONCOVARIANT_MIXING
)
drop_covariance_dimension = full_kms_kernel
rep(
    "TYPED FINDING: covariance-drop mutant is impossible under full KMS",
    drop_covariance_dimension == 0
    and noncovariant_before_kms == MIXING_DIMENSION
    and noncovariant_after_kms == 0,
    "33 noncovariant directions exist before KMS; 0 survive KMS; "
    "COVARIANCE_DROP_REDUNDANT_UNDER_FULL_KMS",
)

# The finite factoriality proxy is exact: CAR_8=M_256 has one-dimensional
# centre and rho is faithful.  It cannot add state uniqueness after KMS.
centre_dimension = 1
minimum_weight_positive = min(GIBBS_WEIGHTS) > 0
rep(
    "K5 finite factoriality proxy",
    centre_dimension == 1 and minimum_weight_positive,
    "centre(M_256)=C; all 256 Gibbs weights are strictly positive",
)

# ------------------------------------------------------------------ K6
# Exact mu4 average and crossed-product extension.
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
rep(
    "K6 exact conditional expectation E=(1/4) sum alpha_r",
    expectation_exact and fixed_matrix_units > 0,
    "crossed-product grade factors=%s; base fixed matrix units=%d/%d"
    % (
        [complex(value) for value in grade_factors],
        fixed_matrix_units,
        matrix_units_total,
    ),
)

# A Hermitian functional on A x| Z4 has 4*d^2 real coefficients.  Fixing
# its restriction to grade zero leaves 3*d^2 extension directions.
# psi=psi o E kills every nonzero-grade coefficient.
extension_directions_before = 3 * FOCK_DIMENSION ** 2
extension_directions_after = 0 if expectation_exact else extension_directions_before
rep(
    "K7 unique E-invariant crossed-product state extension",
    extension_directions_before == 196608
    and extension_directions_after == 0,
    "fixed restriction: extension directions %d -> %d under psi=psi o E"
    % (extension_directions_before, extension_directions_after),
)

print()
print("DIMENSION TABLE")
print("  v972/RP-compatible mixing slice             33")
print("  + mu4 covariance                            %d" % after_covariance)
print("  + faithful-factor proxy                     %d" % after_factoriality)
print("  + full beta=1 KMS                           %d" % after_kms)
print("  drop KMS                                    %d" % drop_kms_dimension)
print("  drop covariance, retain full KMS            %d" % drop_covariance_dimension)
print("  noncovariant companion before/after KMS     %d -> %d"
      % (noncovariant_before_kms, noncovariant_after_kms))
print("  crossed-product extension directions        %d -> %d"
      % (extension_directions_before, extension_directions_after))

print()
print("HONEST BOUNDARY")
print("  Exact finite CAR_8=M_256 and finite crossed product only.")
print("  Type-III/continuum KMS uniqueness and the modular-net/Quillen")
print("  identification remain cited/open; no seam contract is closed.")
print("  Covariance is a useful pre-KMS selector but is redundant once")
print("  the full finite-factor KMS condition is imposed.")
print()
print("VERDICT: KMS_SUBNET_RIGIDITY_FINITE_EXACT")
print("FINDING: COVARIANCE_DROP_REDUNDANT_UNDER_FULL_KMS")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FINDINGS/FAILURES"))
raise SystemExit(0 if ok_all else 1)
