#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Independent exact audit of the claimed "Milnor-Frobenius-Gray code".

Scope and typing
----------------
This is an exploration-only probe.  It rebuilds every finite object used
below with rational, integer, or F2 arithmetic and writes only to stdout.

Classical inputs:
  * the Jacobian/Milnor algebra of x^2+y^3+z^5;
  * the weighted-homogeneous spectrum
      alpha = (i+1)/p + (j+1)/q + (k+1)/r - 1;
  * the E8 Coxeter polynomial Phi_30.

Corpus cross-checks rebuilt here:
  * v1_e8_glue.py: E8 rank/Coxeter context;
  * note_e8_gaussian_code.tex and v833_gaussian_ramification_ladder.py:
    the Gaussian Construction-A E8, its order-four J, and
    E8/2E8 ~= F2[eps]/(eps^2)^4;
  * v804_prime_carrier_gray.py: the affine Gray cycle 00,01,11,10;
  * v819_prime_packet_rm14.py: the 15 = 7_NS + 8_R affine-hyperplane
    split.  The last comparison is reported only as [C].

Important correction:
There is no ring map Q -> F2, so the phrase "M tensor F2" for a Q-algebra
is not literally defined.  Claim 7(i) is tested in its honest form using
the distinguished integral monomial model
    M_Z = Z[y,z]/(y^2,z^4),
then M_Z tensor_Z F2.  The resulting D^4 identifications are exact but
basis-dependent, not a canonical map from singularity theory to E8.

Verdict enum:
  MILNOR_GRAY_VERIFIED(list)
  MILNOR_GRAY_PARTIAL(failures)
  MILNOR_GRAY_REFUTED(failures)
"""

from fractions import Fraction
from itertools import permutations, product
from math import gcd

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form


CHECKS = []
CLAIM_FAILURES = {claim: [] for claim in range(1, 9)}


def check(claim, name, condition, detail=""):
    """Record one exact Boolean gate."""
    passed = bool(condition)
    CHECKS.append((claim, name, passed))
    if not passed:
        CLAIM_FAILURES[claim].append(name)
    suffix = " -- %s" % detail if detail else ""
    print("  [%s] C%d %s%s" %
          ("PASS" if passed else "FAIL", claim, name, suffix))
    return passed


def section(title):
    print("\n== %s ==" % title)


def f2_apply(columns, word):
    """Apply an F2-linear map stored by integer-bit columns."""
    out = 0
    for column_index, column in enumerate(columns):
        if (word >> column_index) & 1:
            out ^= column
    return out


def truncated_product(left, right, bounds):
    """Multiply monomial exponent tuples in a truncated tensor algebra."""
    exponent = tuple(a + b for a, b in zip(left, right))
    return None if any(e >= bound for e, bound in zip(exponent, bounds)) \
        else exponent


print("MILNOR-FROBENIUS-GRAY independent audit")
print("Arithmetic domains: QQ / ZZ / F2 only; no floats, no RNG")


# ============================================================================
section("Claim 1: Milnor algebra by Groebner normal form")
# ============================================================================
x, y, z = sp.symbols("x y z")
groebner = sp.groebner(
    [sp.diff(x**2 + y**3 + z**5, variable)
     for variable in (x, y, z)],
    x, y, z, domain=sp.QQ,
)
groebner_expressions = tuple(poly.as_expr() for poly in groebner.polys)
basis_exponents = tuple((a, b) for a in range(2) for b in range(4))
basis_polynomials = tuple(y**a * z**b for a, b in basis_exponents)
normal_forms = tuple(groebner.reduce(monomial)[1]
                     for monomial in basis_polynomials)

check(1, "Jacobian Groebner basis is (x,y^2,z^4)",
      groebner_expressions == (x, y**2, z**4),
      "computed %s" % (groebner_expressions,))
check(1, "eight standard monomials survive",
      len(basis_polynomials) == 8
      and normal_forms == basis_polynomials,
      "basis=%s" % (basis_exponents,))
check(1, "defining relations reduce to zero",
      all(groebner.reduce(relation)[1] == 0
          for relation in (x, y**2, z**4, 2*x, 3*y**2, 5*z**4)))


# ============================================================================
section("Claim 2: explicit multiplication matrices and rank clock")
# ============================================================================
basis_index = {exponent: index
               for index, exponent in enumerate(basis_exponents)}


def multiplication_matrix(multiplier):
    matrix = sp.zeros(8, 8)
    for column, exponent in enumerate(basis_exponents):
        target = truncated_product(multiplier, exponent, (2, 4))
        if target is not None:
            matrix[basis_index[target], column] = 1
    return matrix


multiplication_matrices = {
    exponent: multiplication_matrix(exponent)
    for exponent in basis_exponents
}
rank_table = [
    [multiplication_matrices[(a, b)].rank() for b in range(4)]
    for a in range(2)
]
formula_table = [[(2 - a) * (4 - b) for b in range(4)]
                 for a in range(2)]
matrix_entries_exact = all(
    entry in (0, 1)
    for matrix in multiplication_matrices.values()
    for entry in matrix
)

check(2, "all eight 8x8 multiplication matrices built over ZZ",
      len(multiplication_matrices) == 8 and matrix_entries_exact)
check(2, "rank formula rank(m_{y^a z^b})=(2-a)(4-b)",
      rank_table == formula_table,
      "ranks=%s" % rank_table)
check(2, "rank table sums to h(E8)=30",
      sum(sum(row) for row in rank_table) == 30,
      "sum=%d" % sum(sum(row) for row in rank_table))


# ============================================================================
section("Claim 3: general Brieskorn rank formula and spherical uniqueness")
# ============================================================================
n, index = sp.symbols("n index", integer=True, positive=True)
one_factor_sum = sp.summation(n - index, (index, 0, n - 1))
check(3, "one-factor rank sum is n(n+1)/2",
      sp.simplify(one_factor_sum - n * (n + 1) / 2) == 0,
      "sum=%s" % one_factor_sum)

p_symbol, q_symbol, r_symbol = sp.symbols(
    "p q r", integer=True, positive=True)
mu_symbol = (p_symbol - 1) * (q_symbol - 1) * (r_symbol - 1)
rank_sum_symbol = (
    p_symbol * (p_symbol - 1)
    * q_symbol * (q_symbol - 1)
    * r_symbol * (r_symbol - 1) / 8
)
reviewer_formula = p_symbol * q_symbol * r_symbol * mu_symbol / 8
check(3, "reviewer formula S=p*q*r*mu/8 is algebraically correct",
      sp.simplify(rank_sum_symbol - reviewer_formula) == 0,
      "S=%s" % sp.factor(rank_sum_symbol))
check(3, "self-clock S=p*q*r iff mu=8",
      sp.simplify(
          rank_sum_symbol - p_symbol*q_symbol*r_symbol
          - p_symbol*q_symbol*r_symbol*(mu_symbol - 8)/8
      ) == 0)

finite_tensor_checks = []
for p_value in range(2, 7):
    for q_value in range(2, 7):
        for r_value in range(2, 7):
            explicit_sum = sum(
                (p_value - 1 - i_value)
                * (q_value - 1 - j_value)
                * (r_value - 1 - k_value)
                for i_value in range(p_value - 1)
                for j_value in range(q_value - 1)
                for k_value in range(r_value - 1)
            )
            mu_value = ((p_value - 1)
                        * (q_value - 1)
                        * (r_value - 1))
            finite_tensor_checks.append(
                8 * explicit_sum
                == p_value*q_value*r_value*mu_value)
check(3, "explicit tensor-rank census agrees for 2<=p,q,r<=6",
      all(finite_tensor_checks),
      "tested=%d" % len(finite_tensor_checks))

# With p<=q<=r and 1/p+1/q+1/r>1: p=2.  If q>=4 the sum is
# at most 1; q=2 is the dihedral family, and q=3 forces r<6.
exceptional_spherical = [
    triple for triple in product(range(2, 6), repeat=3)
    if triple[0] <= triple[1] <= triple[2]
    and triple[1] >= 3
    and sum(Fraction(1, value) for value in triple) > 1
]
strict_spherical = [
    triple for triple in product(range(2, 6), repeat=3)
    if triple[0] < triple[1] < triple[2]
    and sum(Fraction(1, value) for value in triple) > 1
]
strict_self_clock = [
    triple for triple in strict_spherical
    if (triple[0] - 1)*(triple[1] - 1)*(triple[2] - 1) == 8
]
check(3, "exceptional spherical triples are exactly 233,234,235",
      exceptional_spherical == [(2, 3, 3), (2, 3, 4), (2, 3, 5)],
      "triples=%s; (2,2,r) is the excluded dihedral family"
      % exceptional_spherical)
check(3, "strict spherical triples are 234 and 235",
      strict_spherical == [(2, 3, 4), (2, 3, 5)],
      "triples=%s" % strict_spherical)
check(3, "235 is uniquely strict-spherical and self-clocking",
      strict_self_clock == [(2, 3, 5)],
      "solutions=%s" % strict_self_clock)


# ============================================================================
section("Claim 4: spectrum, E8 exponents, and Coxeter polynomial")
# ============================================================================
spectral_numbers = [
    [Fraction(1, 2) + Fraction(a + 1, 3) + Fraction(b + 1, 5) - 1
     for b in range(4)]
    for a in range(2)
]
spectral_m_table = [
    [30 * spectral_numbers[a][b] for b in range(4)]
    for a in range(2)
]
expected_m_table = [[1, 7, 13, 19], [11, 17, 23, 29]]
unit_set_30 = {value for value in range(30) if gcd(value, 30) == 1}
flat_m = sorted(int(value) for row in spectral_m_table for value in row)

check(4, "weighted-homogeneous spectral formula gives stated table",
      spectral_m_table == expected_m_table,
      "30*alpha=%s" % spectral_m_table)
check(4, "scaled spectrum is the unit set modulo 30",
      set(flat_m) == unit_set_30,
      "spectrum=%s" % flat_m)

# Rebuild the E8 Cartan matrix from the exact simple roots used by the
# corpus v1 module, then independently form a Coxeter element.
identity8 = sp.eye(8)
coordinate_rows = []
coordinate_rows.append([
    Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2),
    Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2),
    Fraction(-1, 2), Fraction(1, 2),
])
coordinate_rows.extend([
    [1, 1, 0, 0, 0, 0, 0, 0],
    [-1, 1, 0, 0, 0, 0, 0, 0],
    [0, -1, 1, 0, 0, 0, 0, 0],
    [0, 0, -1, 1, 0, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 0, -1, 1, 0, 0],
    [0, 0, 0, 0, 0, -1, 1, 0],
])
simple_roots = sp.Matrix(coordinate_rows)
cartan_e8 = simple_roots * simple_roots.T
simple_reflections = []
for reflection_index in range(8):
    reflection = sp.eye(8)
    for column in range(8):
        reflection[reflection_index, column] -= \
            cartan_e8[reflection_index, column]
    simple_reflections.append(reflection)
coxeter = sp.eye(8)
for reflection in simple_reflections:
    coxeter = coxeter * reflection
t = sp.symbols("t")
coxeter_polynomial = sp.expand(coxeter.charpoly(t).as_expr())
phi30 = sp.expand(sp.cyclotomic_poly(30, t))

check(4, "exact E8 Cartan reconstruction is even unimodular",
      cartan_e8.det() == 1
      and all(cartan_e8[i, i] == 2 for i in range(8)))
check(4, "Coxeter characteristic polynomial is Phi_30",
      coxeter_polynomial == phi30,
      "chi=%s" % coxeter_polynomial)
check(4, "Coxeter element has exact order 30",
      coxeter**30 == identity8
      and all(coxeter**divisor != identity8
              for divisor in (1, 2, 3, 5, 6, 10, 15)))


# ============================================================================
section("Claim 5: Galois action and Gray cycle")
# ============================================================================
label_by_m = {
    1 + 10*a + 6*b: (a, b)
    for a in range(2) for b in range(4)
}


def mod30_label(multiplier, a, b):
    return label_by_m[(multiplier * (1 + 10*a + 6*b)) % 30]


gray_column_map = {0: 1, 1: 3, 3: 2, 2: 0}
check(5, "multiplication by 11 swaps the two rows",
      all(mod30_label(11, a, b) == (1 - a, b)
          for a in range(2) for b in range(4)))
check(5, "multiplication by 7 follows column Gray cycle 0,1,3,2",
      all(mod30_label(7, a, b) == (a, gray_column_map[b])
          for a in range(2) for b in range(4)))
check(5, "multiplication by -1 is (a,b)->(1-a,3-b)",
      all(mod30_label(-1, a, b) == (1 - a, 3 - b)
          for a in range(2) for b in range(4)))

powers7 = [(7**power) % 30 for power in range(4)]
generated_units = {
    (11**row_swap * 7**column_turn) % 30
    for row_swap in range(2) for column_turn in range(4)
}
gray_words = ((0, 0), (0, 1), (1, 1), (1, 0))
gray_steps = [
    sum(left ^ right
        for left, right in zip(gray_words[k], gray_words[(k + 1) % 4]))
    for k in range(4)
]
check(5, "(Z/30)^x=<11>x<7> is C2 x C4",
      (11**2) % 30 == 1
      and powers7 == [1, 7, 19, 13]
      and generated_units == unit_set_30
      and 11 not in set(powers7),
      "generated=%s" % sorted(generated_units))
check(5, "column labels are the binary Gray cycle",
      gray_steps == [1, 1, 1, 1],
      "words=%s, steps=%s" % (gray_words, gray_steps))


# ============================================================================
section("Claim 6: Frobenius/socle pairing from multiplication matrices")
# ============================================================================
socle = (1, 3)
socle_row = basis_index[socle]
frobenius_gram = sp.Matrix([
    [multiplication_matrices[left][socle_row, basis_index[right]]
     for right in basis_exponents]
    for left in basis_exponents
])
expected_frobenius = sp.Matrix([
    [int(left[0] + right[0] == 1 and left[1] + right[1] == 3)
     for right in basis_exponents]
    for left in basis_exponents
])
check(6, "socle coefficient pairing is the complement permutation",
      frobenius_gram == expected_frobenius
      and frobenius_gram.det() in (-1, 1))
check(6, "socle complement equals the -1/CP label involution",
      all(label_by_m[30 - (1 + 10*a + 6*b)] == (1 - a, 3 - b)
          for a in range(2) for b in range(4)))
check(6, "paired spectral labels sum to 30",
      all((1 + 10*a + 6*b)
          + (1 + 10*(1 - a) + 6*(3 - b)) == 30
          for a in range(2) for b in range(4)))

frobenius_associative = True
for left in basis_exponents:
    for middle in basis_exponents:
        for right in basis_exponents:
            left_middle = truncated_product(left, middle, (2, 4))
            middle_right = truncated_product(middle, right, (2, 4))
            lhs = int(left_middle is not None
                      and truncated_product(left_middle, right, (2, 4))
                      == socle)
            rhs = int(middle_right is not None
                      and truncated_product(left, middle_right, (2, 4))
                      == socle)
            frobenius_associative &= lhs == rhs
check(6, "pairing is Frobenius-associative on all basis triples",
      frobenius_associative)


# ============================================================================
section("Claim 7: dual-number bus and Gaussian E8 cross-check")
# ============================================================================
# Honest mod-2 object: M_Z tensor F2, not the nonexistent Q-algebra tensor F2.
def milnor_epsilon(word):
    """Multiplication by eps=y on F2[y,z]/(y^2,z^4)."""
    return ((word & 0b1111) << 4)


milnor_d_generators = tuple(1 << b for b in range(4))  # 1,z,z^2,z^3
milnor_d_span = set()
for coefficients in product(range(4), repeat=4):
    word = 0
    for generator, coefficient in zip(milnor_d_generators, coefficients):
        if coefficient & 1:
            word ^= generator
        if coefficient & 2:
            word ^= milnor_epsilon(generator)
    milnor_d_span.add(word)
check(7, "retyped M_Z mod 2 is D[z]/(z^4)=D^4",
      len(milnor_d_span) == 256
      and all(milnor_epsilon(milnor_epsilon(word)) == 0
              for word in range(256)),
      "D-basis=(1,z,z^2,z^3); literal M_Q tensor F2 is undefined")

# Z[i]/(2) -> D, a+bi |-> (a+b)+b eps because i=1+eps.
zi_elements = tuple(product((0, 1), repeat=2))


def zi_add(left, right):
    return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)


def zi_multiply(left, right):
    return ((left[0]*right[0] - left[1]*right[1]) % 2,
            (left[0]*right[1] + left[1]*right[0]) % 2)


def dual_add(left, right):
    return ((left[0] + right[0]) % 2, (left[1] + right[1]) % 2)


def dual_multiply(left, right):
    return ((left[0]*right[0]) % 2,
            (left[0]*right[1] + left[1]*right[0]) % 2)


def zi_to_dual(value):
    return ((value[0] + value[1]) % 2, value[1])


ring_iso_ok = (
    len({zi_to_dual(value) for value in zi_elements}) == 4
    and zi_to_dual((1, 1)) == (0, 1)
    and all(
        zi_to_dual(zi_add(left, right))
        == dual_add(zi_to_dual(left), zi_to_dual(right))
        and zi_to_dual(zi_multiply(left, right))
        == dual_multiply(zi_to_dual(left), zi_to_dual(right))
        for left in zi_elements for right in zi_elements
    )
)
check(7, "Z[i]/(2) is D with eps=image(1+i)",
      ring_iso_ok
      and zi_multiply((1, 1), (1, 1)) == (0, 0))

# Rebuild the exact Gaussian Construction-A placement used in
# note_e8_gaussian_code/v833, then compute eps=1+J on L/2L.
g_naive = (
    (1, 0, 0, 0, 0, 1, 1, 1),
    (0, 1, 0, 0, 1, 0, 1, 1),
    (0, 0, 1, 0, 1, 1, 0, 1),
    (0, 0, 0, 1, 1, 1, 1, 0),
)
c_naive = frozenset(
    tuple(sum(message[k]*g_naive[k][j] for k in range(4)) % 2
          for j in range(8))
    for message in product((0, 1), repeat=4)
)
pi_j = (1, 0, 3, 2, 5, 4, 7, 6)
pi_sigma = (2, 3, 4, 5, 0, 1, 6, 7)


def code_image(code, permutation):
    return frozenset(
        tuple(codeword[permutation[k]] for k in range(8))
        for codeword in code
    )


placements = {
    code_image(c_naive, permutation)
    for permutation in permutations(range(8))
}
invariant_placements = [
    code for code in placements
    if code_image(code, pi_j) == code
    and code_image(code, pi_sigma) == code
]
w0246 = (1, 0, 1, 0, 1, 0, 1, 0)
c_star = next(code for code in invariant_placements if w0246 in code)
check(7, "corpus Gaussian placement census reproduces 30 and 2",
      len(placements) == 30 and len(invariant_placements) == 2)

lattice_generators = sp.Matrix(
    [list(codeword) for codeword in sorted(c_star)]
    + [[2*int(row == column) for column in range(8)]
       for row in range(8)]
).T
lattice_basis = hermite_normal_form(lattice_generators)
j_matrix = sp.zeros(8, 8)
for pair_index in range(4):
    j_matrix[2*pair_index, 2*pair_index + 1] = -1
    j_matrix[2*pair_index + 1, 2*pair_index] = 1
epsilon_matrix = lattice_basis.inv() * (sp.eye(8) + j_matrix) \
    * lattice_basis
j_lattice_matrix = lattice_basis.inv() * j_matrix * lattice_basis
check(7, "J preserves L and satisfies J^2=-1",
      all(entry.is_Integer for entry in j_lattice_matrix)
      and j_lattice_matrix**2 == -sp.eye(8))

epsilon_columns = []
for column in range(8):
    bit_column = 0
    for row in range(8):
        if int(epsilon_matrix[row, column]) % 2:
            bit_column ^= 1 << row
    epsilon_columns.append(bit_column)


def e8_epsilon(word):
    return f2_apply(epsilon_columns, word)


epsilon_image = {e8_epsilon(word) for word in range(256)}
epsilon_kernel = {
    word for word in range(256) if e8_epsilon(word) == 0
}
check(7, "on E8/2E8, eps^2=0 and ker(eps)=im(eps)=F2^4",
      all(e8_epsilon(e8_epsilon(word)) == 0 for word in range(256))
      and len(epsilon_image) == 16
      and epsilon_image == epsilon_kernel)


def d_scalar_multiple(coefficient, generator, epsilon_action):
    value = 0
    if coefficient & 1:
        value ^= generator
    if coefficient & 2:
        value ^= epsilon_action(generator)
    return value


e8_d_generators = []
e8_d_span = {0}
for candidate in range(1, 256):
    candidate_span = {
        previous ^ d_scalar_multiple(coefficient, candidate, e8_epsilon)
        for previous in e8_d_span for coefficient in range(4)
    }
    if len(candidate_span) == 4*len(e8_d_span):
        e8_d_generators.append(candidate)
        e8_d_span = candidate_span
    if len(e8_d_generators) == 4:
        break
check(7, "E8/2E8 is free D-rank 4 with explicit generators",
      len(e8_d_generators) == 4 and len(e8_d_span) == 256,
      "generators=%s" %
      [format(generator, "08b") for generator in e8_d_generators])


def milnor_to_e8(word):
    target = 0
    for b, generator in enumerate(e8_d_generators):
        if (word >> b) & 1:
            target ^= generator
        if (word >> (4 + b)) & 1:
            target ^= e8_epsilon(generator)
    return target


bridge_images = {milnor_to_e8(word) for word in range(256)}
check(7, "chosen D-bases give an explicit Milnor-to-E8 intertwiner",
      len(bridge_images) == 256
      and all(milnor_to_e8(milnor_epsilon(word))
              == e8_epsilon(milnor_to_e8(word))
              for word in range(256)),
      "exact and basis-dependent, not canonical")


# ============================================================================
section("Claim 8: PG(3,2)=AG(3,2)+PG(2,2), interpretation only")
# ============================================================================
pg32_points = [
    vector for vector in product((0, 1), repeat=4) if any(vector)
]
hyperplane_at_infinity = [
    vector for vector in pg32_points if vector[0] == 0
]
affine_chart = [
    vector for vector in pg32_points if vector[0] == 1
]
check(8, "PG(3,2) has 15 points",
      len(pg32_points) == (2**4 - 1)//(2 - 1))
check(8, "hyperplane plus affine chart has sizes 7+8",
      len(hyperplane_at_infinity) == 7
      and len(affine_chart) == 8
      and set(hyperplane_at_infinity).isdisjoint(affine_chart)
      and set(hyperplane_at_infinity) | set(affine_chart)
      == set(pg32_points))
print("  [C] Corpus comparison only: 7 points at infinity + 8 affine "
      "points has the same hyperplane/coset shape as 7_NS + 8_R "
      "(v819); no Milnor-to-NS/R identification is asserted.")


# ============================================================================
section("Mutants: required failures")
# ============================================================================
mutant_failures = []

p237 = (2, 3, 7)
mu237 = (p237[0] - 1)*(p237[1] - 1)*(p237[2] - 1)
sum237 = p237[0]*p237[1]*p237[2]*mu237 // 8
mutant_237_fires = sum237 != p237[0]*p237[1]*p237[2]
mutant_failures.append(mutant_237_fires)
print("  [%s] MUTANT (2,3,7): mu=%d, S=%d != pqr=%d" %
      ("PASS" if mutant_237_fires else "FAIL",
       mu237, sum237, p237[0]*p237[1]*p237[2]))

# A8: x^2+y^2+z^9 has mu=8 and therefore passes the rank self-clock,
# but its Coxeter exponents are 1,...,8 at h=9, not (Z/30)^x.
a8_mu = (2 - 1)*(2 - 1)*(9 - 1)
a8_rank_sum = 2*2*9*a8_mu // 8
a8_exponents = set(range(1, 9))
mutant_a8_fires = (
    a8_mu == 8 and a8_rank_sum == 36
    and a8_exponents != unit_set_30
)
mutant_failures.append(mutant_a8_fires)
print("  [%s] MUTANT A8: self-clock survives (%d=36), "
      "but exponents %s != units mod 30" %
      ("PASS" if mutant_a8_fires else "FAIL",
       a8_rank_sum, sorted(a8_exponents)))

# Wrong "socle" z^3 omits y and produces a degenerate rank-four form.
wrong_socle_row = basis_index[(0, 3)]
wrong_pairing = sp.Matrix([
    [multiplication_matrices[left][wrong_socle_row, basis_index[right]]
     for right in basis_exponents]
    for left in basis_exponents
])
wrong_pairing_fires = wrong_pairing.rank() == 4 \
    and wrong_pairing.rank() < 8
mutant_failures.append(wrong_pairing_fires)
print("  [%s] MUTANT wrong socle z^3: pairing rank=%d < 8" %
      ("PASS" if wrong_pairing_fires else "FAIL", wrong_pairing.rank()))


# ============================================================================
section("Typing and verdict")
# ============================================================================
claim_types = {
    1: "VERIFIED -- classical singularity theory",
    2: "VERIFIED -- exact rank identity; new-in-corpus packaging",
    3: "VERIFIED -- reviewer formula correct; uniqueness includes hypotheses",
    4: "VERIFIED -- classical E8 singularity spectrum/Coxeter exponents",
    5: "VERIFIED -- exact Galois/Gray identity; new-in-corpus packaging",
    6: "VERIFIED -- exact socle=-1/CP identity; new-in-corpus packaging",
    7: "RETYPED+VERIFIED -- integral mod-2 model; exact basis-dependent D^4 bridge",
    8: "VERIFIED COUNTS / [C] CONSISTENT-INTERPRETATION only",
}
for claim in range(1, 9):
    failures = CLAIM_FAILURES[claim]
    status = claim_types[claim] if not failures \
        else "FAILED -- %s" % ", ".join(failures)
    print("  C%d: %s" % (claim, status))

failed_claims = {
    claim: failures for claim, failures in CLAIM_FAILURES.items() if failures
}
controls_ok = all(mutant_failures)
passed_count = sum(passed for _, _, passed in CHECKS)
print("\nCHECKS: %d/%d PASS; mutants %d/%d fired" %
      (passed_count, len(CHECKS), sum(mutant_failures),
       len(mutant_failures)))

if failed_claims:
    verdict = "MILNOR_GRAY_PARTIAL(%s)" % sorted(failed_claims)
elif not controls_ok:
    verdict = "MILNOR_GRAY_REFUTED(['mutant-control-dead'])"
else:
    verdict = (
        "MILNOR_GRAY_VERIFIED([1,2,3,4,5,6,'7-retyped','8-C'])"
    )
print("VERDICT: %s" % verdict)

raise SystemExit(0 if not failed_claims and controls_ok else 1)
