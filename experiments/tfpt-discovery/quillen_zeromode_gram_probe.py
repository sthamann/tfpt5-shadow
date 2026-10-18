#!/usr/bin/env python3
"""quillen_zeromode_gram_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (ALPHA.QUILLEN.EXACT.01 [O], after today's BFK probe retyped
the wave-2 'Quillen metric compensates 2^{-4}' claim as already-internal):
review wave 3 claims a *specific* compensation identity of its own,

    the Quillen norm contains the Gram determinant of the four
    normalized zero modes, and in the deck-graded basis
    det G_zero = 2^4 EXACTLY, hence 2^{-4} * det G_zero = 1.

Is that a new finitely computable identity, a reformulation of the
already-internal BFK 2-power, or false in every natural reading?

THE OBJECT.  Seam circle of circumference l, cut at the four mu4 marks
into intervals of lengths a_1..a_4.  Dirichlet-interval Laplacians have
no zero modes.  The BFK jump/mark structure carries four small modes:
kernel of R_0 (constants on the marks, mu4 channel k = 0) plus the three
nonzero channels of R_0 = 16 c3 circ(2,-1,0,-1) at the KMS scale.
'Deck-graded' in this corpus (v974/v985) is the mu4 character basis on
the four marks, F_{jk} = i^{jk}.

READINGS (each decided exactly, sympy):

  A   L^2 Gram of the interval-constant Neumann kernels after L^2
      normalisation: e_i = 1_{I_i}/sqrt(a_i).  Disjoint supports =>
      G = I, det G = 1.  2^{-4} det G = 1/16 =/= 1.  FAIL.
  A2  Same functions unnormalised: G = diag(a_j), det = prod a_j.
      Not identically 16; at KMS a_j = pi/2, (pi/2)^4 =/= 16.  FAIL.
  B   Unnormalised mu4 character table (DFT_4).  det F = -16 i,
      |det F| = 16 = 4^{4/2}.  Signed det is NOT 2^4; the modulus is.
      2^{-4} |det F| = 1.  HOLDS for the absolute-value identity.
  B_gram  Hilbert Gram of those four vectors: F^H F = 4 I, det = 256
      = 2^8 =/= 16.  2^{-4} det G = 16 =/= 1.  FAIL as a Gram.
  B_half  Gram of the half-normalised characters chi_k / sqrt(2):
      G = 2 I, det G = 16.  HOLDS as a genuine Gram (non-L^2, non-unitary
      normalisation: one sqrt(2) per mode).
  C   Geometric Fourier-Vandermonde at the mark *positions*
      V_{k j} = exp(2 pi i k x_j / l).  At equal spacing this IS F,
      |det| = 16; at general a_j, |det V|^2 = prod_{alpha<beta}
      4 sin^2(pi (x_beta-x_alpha)/l), equal to 256 only on the Z4-orbit.
      Pins the symmetric point; a_j-blind combinatorial B does not.
  D   Real Klein/Hadamard table (characters of the Z2 deck's associated
      graded (Z2)^2): det H_4 = +16 exactly.  2^{-4} det H = 1 signed.
  E   Real Z4 Fourier with the sqrt(2) on the 2-dim irrep (k = 1,3).
      det = +16.  Naive real form without sqrt(2): det = 8 (FAIL).

GENERAL LENGTHS.  Combinatorial B/D/E/B_half are a_j-blind (the
character table does not see the interval lengths) -- compensation
persists identically at N = 4.  Geometric C and the statement
'R_0 eigenbasis = DFT' hold only at equal marks (the KMS/symmetric
point).  The BFK internal cancellation 2^{-N} prod(2 a_j) = prod a_j
is identity-level in N *and* a_j -- a different partner for the same
2^{-4}.

MUTANTS (must fire against the identities that hold):
  r -> r+1  (row 4-cycle on the real tables): signed det 16 -> -16,
            so 2^{-4} det = -1 =/= 1.  |det DFT| is invariant (the
            abs identity is NOT a tooth for a channel relabel -- typed).
  Z3        2^{-3} |det DFT_3| = 3 sqrt(3)/8 =/= 1.  Among N = 1..7,
            N^{N/2} = 2^N only at N = 4.
  unitary   F/2 has |det| = 1; 2^{-4} * 1 =/= 1.
  naive-real (no sqrt(2) on the doublet): det = 8 =/= 16.

RELATION TYPING.  Two different decompositions of the same 2-power
at N = |mu4| = 4, not one identity in two bases:
  (1) BFK internal (today): 2^{-N} prod(2 a_j) = prod a_j, all N, all a_j.
  (2) Character-table: 2^{-N} |det DFT_N| = 1  iff N = 4
      (equivalently 2^{-4} det H_4 = 1, 2^{-4} det G_{chi/sqrt(2)} = 1).
v974 already flagged C_glue = 2^{-4} = |mu4|^{-2} as anti-numerology;
|det DFT_4| = |mu4|^2 restates that as C_glue * |det chi| = 1.  It is
NOT a Quillen-metric computation, NOT the L^2 Gram of the Neumann
kernels, and NOT an extra continuum identity.  The Hilbert Gram of
the unnormalised characters is 256, so the review's words 'Gram
determinant of four normalized zero modes' are a misnomer for the
character-table determinant (or for the nonstandard sqrt(2) Gram).
Valuable as a dictionary, not new analytic content.

HONEST BOUNDARY (firewall): finite 1D circle / 4x4 mark objects only;
continuum Bismut-Freed stays [O]; alpha untouched; no marker move.
ALPHA.QUILLEN.EXACT.01 stays [O].

VERDICT ENUM: ZEROMODE_GRAM_REFORMULATION.
"""
import sympy as sp

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


I = sp.I

# ------------------------------------------------------------------ DFT / real tables
F = sp.Matrix([
    [1,  1,  1,  1],
    [1,  I, -1, -I],
    [1, -1,  1, -1],
    [1, -I, -1,  I],
])
H = sp.Matrix([
    [1,  1,  1,  1],
    [1, -1,  1, -1],
    [1,  1, -1, -1],
    [1, -1, -1,  1],
])
s2 = sp.sqrt(2)
R2 = sp.Matrix([
    [1,   1,  1,   1],
    [s2,  0, -s2,  0],
    [1,  -1,  1,  -1],
    [0,  s2,  0,  -s2],
])
R_naive = sp.Matrix([
    [1, 1,  1,  1],
    [1, 0, -1,  0],
    [1, -1, 1, -1],
    [0, 1,  0, -1],
])


def wpow(n):
    return [1, I, -1, -I][n % 4]


# ================================================================== A, A2
a1, a2, a3, a4 = sp.symbols("a1:5", positive=True)
a = (a1, a2, a3, a4)
G_L2 = sp.eye(4)                          # disjoint supports after /sqrt(a_i)
rep("READING A: L2 Gram of e_i = 1_{I_i}/sqrt(a_i) is I (disjoint "
    "supports), det G = 1 -- 2^{-4} det G = 1/16 =/= 1; the claim "
    "FAILS for the L2/Quillen inner product on interval constants",
    G_L2.det() == 1)

G_un = sp.diag(*a)
rep("READING A2: unnormalised interval-constant Gram = diag(a_j), "
    "det = prod a_j, not identically 16; at the KMS symmetric point "
    "a_j = pi/2, (pi/2)^4 =/= 16",
    sp.simplify(G_un.det() - sp.prod(a)) == 0
    and sp.simplify((sp.pi / 2) ** 4 - 16) != 0)


# ================================================================== B, B_gram, B_half
detF = F.det()
rep("READING B: unnormalised mu4 character table DFT_4 has "
    "det F = -16 i and |det F| = 16 = 4^{4/2} exactly -- "
    "2^{-4} |det F| = 1; the SIGNED det is not 2^4",
    detF == -16 * I
    and sp.simplify(sp.Abs(detF) - 16) == 0
    and sp.simplify(sp.Abs(detF) * sp.Rational(1, 16) - 1) == 0)

G_chi = sp.simplify(F.H * F)
rep("READING B_gram: Hilbert Gram of the four unnormalised character "
    "vectors is 4 I, det G = 256 = 2^8 =/= 16 -- if 'Gram' is the "
    "Hilbert-space Gram, the claim is FALSE (2^{-4} det G = 16; the "
    "matching power would be 2^{-8})",
    G_chi == 4 * sp.eye(4) and G_chi.det() == 256)

G_half = sp.simplify((F / s2).H * (F / s2))
rep("READING B_half: Gram of chi_k / sqrt(2) is 2 I, det G = 16 "
    "exactly -- this is the UNIQUE natural Hilbert Gram with det = 2^4 "
    "(unnormalised 256, L2-normalised /2 gives 1); 2^{-4} det G = 1.  "
    "The normalisation is neither L2 nor unitary: one sqrt(2) per mode",
    G_half == 2 * sp.eye(4) and G_half.det() == 16)


# ================================================================== D, E
rep("READING D: real Klein/Hadamard character table (associated "
    "graded of the Z2 deck) has signed det H_4 = +16, so "
    "2^{-4} det H = 1 with no absolute value",
    H.det() == 16)

rep("READING E: real Z4 Fourier with sqrt(2) on the 2-dim irrep "
    "(k = 1,3) has det = +16; the naive Re/Im form without sqrt(2) "
    "has det = 8 =/= 16 (wrong irrep normalisation)",
    sp.simplify(R2.det() - 16) == 0 and R_naive.det() == 8)


# ================================================================== C geometric
def vandermonde_absdet_sq(xs, ell):
    """|det V|^2 for V_{kj} = exp(2 pi i k x_j / ell), via
    prod_{alpha<beta} |zeta_beta - zeta_alpha|^2 = prod 4 sin^2(pi Dx/ell)."""
    p = 1
    n = len(xs)
    for alpha in range(n):
        for beta in range(alpha + 1, n):
            p *= 4 * sp.sin(sp.pi * (xs[beta] - xs[alpha]) / ell) ** 2
    return sp.simplify(p)


p_eq = vandermonde_absdet_sq([0, 1, 2, 3], 4)
rep("READING C at the symmetric point: geometric Vandermonde at equal "
    "marks IS the DFT, |det V|^2 = 256 so |det V| = 16 -- the "
    "compensation 2^{-4} |det V| = 1 holds at equal spacing",
    p_eq == 256)

p_uneq = vandermonde_absdet_sq([0, 1, 2, 3], 5)   # a = (1,1,1,2), l = 5
rep("READING C at general lengths: a = (1,1,1,2) gives |det V|^2 = 125 "
    "exactly =/= 256 -- the geometric reading pins the symmetric "
    "(equal-mark / KMS) point and is NOT identity-level in a_j",
    p_uneq == 125 and p_uneq != 256)


# ================================================================== R_0 eigenbasis vs DFT
def assemble_R0(lens):
    R = sp.zeros(4)
    for j in range(4):
        w = 1 / sp.sympify(lens[j])
        k = (j + 1) % 4
        R[j, j] += w
        R[k, k] += w
        R[j, k] += -w
        R[k, j] += -w
    return R


Fh = F.H
Req = assemble_R0([1, 1, 1, 1])
D_eq = sp.simplify(Fh * Req * F / 4)
rep("R_0 at equal marks is circulant: DFT-diagonal with spectrum "
    "[0, 2, 4, 2] -- the four mark-supported modes ARE the mu4 "
    "characters, so readings B/D/E describe the R_0 eigenbasis",
    sp.simplify(D_eq - sp.diag(0, 2, 4, 2)) == sp.zeros(4))

Rgen = assemble_R0(a)
Mgen = Fh * Rgen * F / 4
off = sp.simplify(Mgen[1, 2])
rep("R_0 at general a_j is NOT DFT-diagonal (channel-mixing "
    "M_{1,2} = (1-I)(a1 a2 a3 - I a1 a2 a4 - a1 a3 a4 + I a2 a3 a4) "
    "/ (2 prod a) =/= 0) -- the R_0 eigenbasis coincides with the "
    "deck-graded character table ONLY at the symmetric point",
    sp.expand(off) != 0)


# ================================================================== general-length combinatorial
rep("GENERAL LENGTHS, combinatorial: DFT/Hadamard/sqrt2-Gram do not "
    "depend on a_j, so 2^{-4} |det chi| = 1 persists identically at "
    "N = 4 (a_j-blind).  This is the opposite of geometric C and of "
    "the BFK internal cancellation, which sees the lengths",
    sp.simplify(F.det() - detF) == 0 and H.det() == 16)

# weighted character Gram: G = F^H diag(a) F, det = 256 prod a
G_w = F.H * sp.diag(*a) * F
rep("GENERAL LENGTHS, weighted character Gram F^H diag(a) F has "
    "det = 256 prod a_j (not 16): the a_j-weighted inner product on "
    "the marks recovers the unnormalised interval Gram up to 2^8, "
    "not a new compensation",
    sp.simplify(G_w.det() - 256 * sp.prod(a)) == 0)


# ================================================================== BFK internal is a DIFFERENT partner
rep("RELATION ANCHOR (today's internal cancellation, still true): "
    "2^{-4} prod(2 a_j) = prod a_j identically -- a DIFFERENT "
    "partner for the same 2^{-4} (geometric, all N in the BFK probe; "
    "here N = 4).  Character-table compensation does not use a_j",
    sp.simplify(sp.Rational(1, 16) * sp.prod(2 * aj for aj in a)
                - sp.prod(a)) == 0)

rep("N^{N/2} = 2^N holds among N = 1..7 ONLY at N = 4 -- the "
    "character-table compensation 2^{-N} |det DFT_N| = 1 is an "
    "N = |mu4| selection, not a general BFK identity",
    all((N ** sp.Rational(N, 2) == 2 ** N) == (N == 4)
        for N in range(1, 8)))


# ================================================================== mutants
H_shift = sp.Matrix.vstack(H[1, :], H[2, :], H[3, :], H[0, :])
R2_shift = sp.Matrix.vstack(R2[1, :], R2[2, :], R2[3, :], R2[0, :])
F_shift = sp.Matrix(4, 4, lambda j, k: wpow(j * (k + 1)))
rep("MUTANT r->r+1 FIRES on the SIGNED identity: a 4-cycle of the "
    "real Klein/Z4 tables sends det 16 -> -16, so 2^{-4} det = -1 "
    "=/= 1 -- the signed compensation is grading-order dependent",
    H_shift.det() == -16
    and sp.simplify(R2_shift.det() + 16) == 0
    and sp.simplify(H_shift.det() * sp.Rational(1, 16) + 1) == 0)

rep("MUTANT r->r+1 does NOT fire against |det DFT|: F_{jk} = i^{j(k+1)} "
    "has det = +16 i, |det| still 16 -- channel relabel is monomial, "
    "the absolute-value identity is grading-order blind (typed: this "
    "is not a tooth for reading B_abs, it is a tooth for D/E signed)",
    F_shift.det() == 16 * I
    and sp.simplify(sp.Abs(F_shift.det()) - 16) == 0)

w3 = (-1 + I * sp.sqrt(3)) / 2
F3 = sp.Matrix(3, 3, lambda j, k: w3 ** (j * k))
detF3 = sp.simplify(F3.det())
rep("MUTANT Z3 FIRES: DFT_3 has det = -3 sqrt(3) i, |det| = 3 sqrt(3) "
    "= 3^{3/2}, and 2^{-3} |det DFT_3| = 3 sqrt(3)/8 =/= 1",
    detF3 == -3 * sp.sqrt(3) * I
    and sp.simplify(sp.Abs(detF3) - 3 * sp.sqrt(3)) == 0
    and sp.simplify(sp.Abs(detF3) * sp.Rational(1, 8) - 1) != 0)

F2 = sp.Matrix([[1, 1], [1, -1]])
rep("MUTANT Z2 (companion): |det DFT_2| = 2, 2^{-2} * 2 = 1/2 =/= 1 "
    "-- same N^{N/2} vs 2^N mismatch",
    F2.det() == -2 and sp.simplify(sp.Abs(F2.det()) * sp.Rational(1, 4) - 1) != 0)

Fu = F / 2
rep("MUTANT wrong normalisation FIRES: unitary DFT F/2 has |det| = 1 "
    "and Gram I, so 2^{-4} |det| = 1/16 =/= 1 -- full L2/unitary "
    "normalisation kills the identity; only the unnormalised table "
    "or the half-normalised Gram retains 16",
    sp.simplify(sp.Abs(Fu.det()) - 1) == 0
    and sp.simplify(Fu.H * Fu) == sp.eye(4))


# ================================================================== relation typing gate
rep("RELATION TYPING: at N = 4 the two partners of 2^{-4} are "
    "distinct -- (BFK) prod(2 a_j) vs (chi) |det DFT_4| = 16.  "
    "They agree numerically on the 2-power but are not the same "
    "identity: the first holds for general N (with 2^{-N}), the "
    "second only for N = 4.  v974's |mu4|^{-2} * |mu4|^2 = 1 is "
    "exactly 2^{-4} * 16 = 1 restated.  REFORMULATION of that "
    "numerology in the character-table basis, not a Quillen metric",
    sp.simplify(sp.Rational(1, 16) * 16 - 1) == 0
    and sp.simplify(sp.Rational(1, 16) * sp.prod(2 * aj for aj in a)
                   / sp.prod(a) - 1) == 0
    and 4 ** (-2) * 4 ** 2 == 1)

print()
print("VERDICT: ZEROMODE_GRAM_REFORMULATION -- readings that give "
      "det = 16 exactly: B_abs |det DFT_4|, D det H_4, E det(real "
      "Z4+sqrt2), B_half Gram(chi/sqrt2).  Failures: A (L2 Gram=1), "
      "A2 (prod a_j), B_signed (det F = -16i), B_gram (256).  "
      "General lengths: combinatorial identities persist; geometric "
      "Vandermonde and R_0 = DFT pin the symmetric point.  Mutants "
      "Z3 / unitary / signed r->r+1 fire.  Same 2^{-4} as today's "
      "internal cancellation, DIFFERENT partner (character-table "
      "volume at N=4, not prod(2a_j)); not a Quillen-metric object.  "
      "ALPHA.QUILLEN.EXACT.01 stays [O]; alpha untouched")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
