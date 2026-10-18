#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""flavor_feedback_probe -- FLAVOR.FEEDBACK.NORMALFORM.01 (phase 1 of the
2026-08-08 evening plan): the winding line R_s = R + s 1 e1^T has an exact
FEEDBACK NORMAL FORM -- one integral basis P puts the whole line into a
gain-plus-companion block matrix whose characteristic polynomial is the
feedback form chi_{R_s}(t) = (t - s - 4)(t^2 - 5t + 2) - 12t, with every
coefficient a compiler atom and the 12-gain the loop product 3 x 4 =
N_fam x |mu4| = dim g_SM.

FROZEN CLAIMS (2026-08-08 evening, frozen + SHA-hashed before first run):

 S1  THE BASIS IDENTITY (exact, symbolic in s):
     R = [[1,3,0],[1,5,2],[2,5,3]] (residue ward: det R = 8 = h(D5),
     tr R = 9, chi_R = t^3 - 9t^2 + 10t - 8, third column R e3 =
     (0,2,3)); the basis P = [b0, b1, b2] with b0 = 2*1 = (2,2,2),
     b1 = e3 = (0,0,1), b2 = R e3 = (0,2,3), i.e.
     P = [[2,0,0],[2,0,2],[2,1,3]], det P = -4.  The three EXACT
     module identities, symbolic in s:
       R_s b0 = (s+4) b0 + 4 b2
       R_s b1 = b2
       R_s b2 = 3 b0 - 2 b1 + 5 b2       (s-free: e1^T b1 = e1^T b2 = 0)
     hence P^{-1} R_s P = M(s) = [[s+4,0,3],[0,0,-2],[4,1,5]] EXACTLY --
     integral for every integer s although P is not unimodular (the
     normal form lives on the sublattice P Z^3), and the conjugated
     deformation P^{-1} (1 e1^T) P = E11 exactly (the deformation is a
     PURE GAIN on the (1,1) entry in normal-form coordinates).
 S2  THE FEEDBACK FORM (exact, symbolic in s):
     chi_{M(s)}(t) = chi_{R_s}(t) = (t - s - 4)(t^2 - 5t + 2) - 12t
     identically; in compiler atoms
       (t - s - |mu4|)(t^2 - g_car t + |Z2|) - N_fam |mu4| t
     with 12 = N_fam x |mu4| = dim g_SM = |R(A3)|; the block reading:
     the trailing 2x2 block [[0,-2],[1,5]] of M(s) is the COMPANION
     matrix of q_wind = t^2 - g_car t + |Z2| (v857 part B quadratic),
     the gain channel is the (1,1) entry s + |mu4|, and the loop
     product of the coupling entries M[0,2] x M[2,0] = 3 x 4 = 12 is
     the feedback tap; equivalently the remainder identity
     chi_R - (t - 4) q_wind = -12 t (pure t-tap at gain offset
     c = 4 = |mu4|).
 S3  s = 6 (the locked point): chi_L(t) = (t - 10)(t^2 - 5t + 2) - 12t
     = t^3 - 15t^2 + 40t - 20 = charpoly(L), L = R + 6 1 e1^T, with the
     COEFFICIENT IDENTITIES read off the feedback form at gain 10:
       15 = 10 + 5          ((s+4) + g_car at s = 6)
       40 = 50 + 2 - 12     (g_car (s+4) + |Z2| - dim g_SM)
       20 = 10 x 2          ((s+4) |Z2|).
 S4  THE HONEST SUBTLETY (typed, no identification): det P = -4;
     SNF(P) = diag(1,2,2); the quotient Z^3 / P Z^3 = Z2 x Z2 has
     CARDINALITY 4 = |mu4| but EXPONENT 2 -- the SAME cardinality as
     mu4, NOT the same group (mu4 = Z4 is cyclic of exponent 4).  The
     normal form lives on an index-4 sublattice with quotient Z2^2;
     NO premature identification with mu4 is made -- typed verbatim.
 C   CONTROLS (each must fire; exact):
     C1 direction 1 e2^T: conjugated deformation P^{-1}(1 e2^T)P =
        [[1,0,1],[0,0,0],[0,0,0]] != E11 (s leaks into the (1,3)
        coupling entry -- the pure-gain form breaks); the gain
        normalization of its quadratic q2 = t^2 - t + 2 forces offset
        c = 8 != 4 = |mu4| and the remainder chi_R - (t-8) q2 = +8 is a
        CONSTANT GRAFT, not a t-tap: no (s+4)/12-gain form exists.
     C2 direction 1 e3^T: conjugated deformation P^{-1}(1 e3^T)P =
        [[1,1/2,3/2],[0,0,0],[0,0,0]]: NOT integral and != E11; offset
        c = 10, remainder chi_R - (t-10) q3 = 22t - 28 MIXED (q3 =
        t^2 + t - 2): the feedback form breaks twice over.
     C3 THE SIBLING ROW MATRIX e1 1^T: conjugated deformation
        P^{-1}(e1 1^T)P = outer((1/2,1/2,-1/2), (6,1,5)) -- rank one
        smeared over ALL rows, != E11; offset c = 4 COINCIDES with
        |mu4| (typed honestly) but the remainder chi_R - (t-4) q_row =
        -11t - 4 (q_row = t^2 - 5t + 1) has a nonzero constant: the
        pure t-tap fails, the row transport breaks the form.

KILLS (any one fires => typed failure):
  K1 residue ward breaks                       -> RESIDUE-MISMATCH
  K2 a basis identity of S1 breaks             -> BASIS-MISMATCH
  K3 the feedback form (S2) breaks             -> FORM-MISMATCH
  K4 an s = 6 coefficient identity breaks      -> COEFF-MISMATCH
  K5 det/SNF/quotient typing (S4) breaks       -> LATTICE-MISMATCH
  K6 a control does not fire                   -> CONTROL-DEAD

VERDICT (frozen enum): FEEDBACK-NORMALFORM-EXACT / RESIDUE-MISMATCH /
BASIS-MISMATCH / FORM-MISMATCH / COEFF-MISMATCH / LATTICE-MISMATCH /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact sympy/integer arithmetic in every decision;
no floats, no RNG, no fits.  NO physics claim.  Runtime cap: minutes.

Sources (read-only): verification/v4_flavor_matrix.py (R),
v832_anchor_flavor_checksum.py + v844_message_doily_rank.py (anchor /
flavor context), v857_simplex_fourier_winding.py part B (q_wind =
t^2 - g_car t + |Z2|, the winding quadratic and its sibling-direction
controls), tfpt_2_standard_model.tex (winding keyboxes).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/flavor_feedback_probe.py
"""
import hashlib
import time

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

T0 = time.time()
CHECKS = []
KILLS = []

G_CAR = 5
Z2 = 2
N_FAM = 3
MU4 = 4
DIM_GSM = 12
H_D5 = 8


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("=" * 74)
print("FLAVOR.FEEDBACK.NORMALFORM.01 -- P^{-1} R_s P = [[s+4,0,3],[0,0,-2],")
print("[4,1,5]]; chi_{R_s} = (t-s-|mu4|) q_wind - dim(g_SM) t; quotient Z2^2")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

t, s = sp.symbols("t s")
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
ONES = sp.Matrix([1, 1, 1])
E1 = sp.Matrix([[1, 0, 0]])
E2 = sp.Matrix([[0, 1, 0]])
E3 = sp.Matrix([[0, 0, 1]])
Rs = R + s * ONES * E1
L = R + 6 * ONES * E1
q_wind = t ** 2 - G_CAR * t + Z2

# ======================================================================
section("S1: the basis identity -- P = [2*1 | e3 | R e3]")
# ======================================================================
chiR = sp.expand(R.charpoly(t).as_expr())
check("S1.1 residue ward: det R = %d == 8 = h(D5); tr R = %d == 9; "
      "chi_R = %s; R e3 = %s == (0,2,3)"
      % (R.det(), R.trace(), chiR, tuple(R.col(2))),
      R.det() == H_D5 and R.trace() == 9
      and chiR == t ** 3 - 9 * t ** 2 + 10 * t - 8
      and tuple(R.col(2)) == (0, 2, 3), kill="K1")

b0 = 2 * ONES
b1 = sp.Matrix([0, 0, 1])
b2 = R * b1
P = sp.Matrix.hstack(b0, b1, b2)
check("S1.2 P = [b0|b1|b2] = %s == [[2,0,0],[2,0,2],[2,1,3]] "
      "(b0 = 2*1, b1 = e3, b2 = R e3); det P = %d == -4"
      % (P.tolist(), P.det()),
      P == sp.Matrix([[2, 0, 0], [2, 0, 2], [2, 1, 3]]) and P.det() == -4,
      kill="K2")

id0 = sp.simplify(Rs * b0 - ((s + 4) * b0 + 4 * b2))
id1 = sp.simplify(Rs * b1 - b2)
id2 = sp.simplify(Rs * b2 - (3 * b0 - 2 * b1 + 5 * b2))
check("S1.3 module identities EXACT (symbolic in s): R_s b0 = (s+4) b0 "
      "+ 4 b2; R_s b1 = b2; R_s b2 = 3 b0 - 2 b1 + 5 b2",
      id0 == sp.zeros(3, 1) and id1 == sp.zeros(3, 1)
      and id2 == sp.zeros(3, 1), kill="K2")

M = sp.Matrix([[s + 4, 0, 3], [0, 0, -2], [4, 1, 5]])
conj = sp.simplify(P.inv() * Rs * P)
D1 = sp.simplify(P.inv() * (ONES * E1) * P)
check("S1.4 P^{-1} R_s P = %s == [[s+4,0,3],[0,0,-2],[4,1,5]] EXACT; "
      "integral though det P = -4 (index-4 sublattice); conjugated "
      "deformation P^{-1}(1 e1^T)P = %s == E11 (PURE GAIN)"
      % (conj.tolist(), D1.tolist()),
      sp.simplify(conj - M) == sp.zeros(3, 3)
      and D1 == sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]]), kill="K2")

# ======================================================================
section("S2: the feedback form chi = (t-s-4) q_wind - 12 t")
# ======================================================================
chiM = sp.expand(M.charpoly(t).as_expr())
chiS = sp.expand(Rs.charpoly(t).as_expr())
feedback = sp.expand((t - s - 4) * (t ** 2 - 5 * t + 2) - 12 * t)
check("S2.1 chi_{M(s)}(t) = chi_{R_s}(t) = (t-s-4)(t^2-5t+2) - 12t "
      "EXACT (symbolic in s)",
      sp.expand(chiM - feedback) == 0 and sp.expand(chiS - feedback) == 0,
      kill="K3")

atoms = sp.expand((t - s - MU4) * (t ** 2 - G_CAR * t + Z2)
                  - N_FAM * MU4 * t)
comp = M[1:, 1:]
chi_comp = sp.expand(comp.charpoly(t).as_expr())
check("S2.2 compiler atoms: (t-s-|mu4|)(t^2 - g_car t + |Z2|) - "
      "N_fam |mu4| t identical; 12 = N_fam x |mu4| = %d = dim g_SM; "
      "block [[0,-2],[1,5]] is the COMPANION matrix of q_wind "
      "(chi = %s); loop product M[0,2] x M[2,0] = %d x %d = 12"
      % (N_FAM * MU4, chi_comp, M[0, 2], M[2, 0]),
      sp.expand(atoms - feedback) == 0 and N_FAM * MU4 == DIM_GSM
      and sp.expand(chi_comp - q_wind) == 0
      and M[0, 2] * M[2, 0] == DIM_GSM, kill="K3")

rem1 = sp.expand(chiR - (t - 4) * q_wind)
check("S2.3 remainder identity: chi_R - (t - 4) q_wind = %s == -12t "
      "(pure t-tap at gain offset c = 4 = |mu4|)" % rem1,
      rem1 == -12 * t, kill="K3")

# ======================================================================
section("S3: s = 6 -- the coefficient identities of chi_L")
# ======================================================================
chiL = sp.expand(L.charpoly(t).as_expr())
lock = sp.expand((t - 10) * (t ** 2 - 5 * t + 2) - 12 * t)
check("S3.1 chi_L = (t-10)(t^2-5t+2) - 12t = %s == t^3 - 15t^2 + 40t "
      "- 20 = charpoly(R + 6 1 e1^T)" % chiL,
      sp.expand(chiL - lock) == 0
      and chiL == t ** 3 - 15 * t ** 2 + 40 * t - 20, kill="K4")
check("S3.2 coefficient identities at gain 10: 15 = 10 + 5 (%s); "
      "40 = 50 + 2 - 12 (%s); 20 = 10 x 2 (%s)"
      % (10 + G_CAR == 15, G_CAR * 10 + Z2 - DIM_GSM == 40, 10 * Z2 == 20),
      10 + G_CAR == 15 and G_CAR * 10 + Z2 - DIM_GSM == 40
      and 10 * Z2 == 20, kill="K4")

# ======================================================================
section("S4: the honest subtlety -- SNF(P) and the quotient Z2 x Z2")
# ======================================================================
snf = smith_normal_form(P, domain=sp.ZZ)
inv_factors = sorted(abs(int(x)) for x in snf.diagonal())
check("S4.1 det P = -4; SNF(P) = diag%s == (1,2,2)"
      % (tuple(inv_factors),),
      P.det() == -4 and inv_factors == [1, 2, 2], kill="K5")
card = 1
for f in inv_factors:
    card *= f
check("S4.2 quotient Z^3/PZ^3: cardinality %d == 4 = |mu4| (SAME "
      "cardinality) but invariant factors (1,2,2) => group Z2 x Z2 "
      "with EXPONENT %d = 2, NOT Z4 = mu4 (exponent 4): NOT the same "
      "group -- typed, no identification made"
      % (card, max(inv_factors)),
      card == MU4 and max(inv_factors) == 2 and max(inv_factors) != 4,
      kill="K5")
print("      TYPED: the normal form lives on the index-4 sublattice "
      "P Z^3 with")
print("      quotient Z2^2 -- same CARDINALITY as mu4, different GROUP; "
      "any mu4")
print("      reading would need an extra order-4 witness (none claimed "
      "here).")

# ======================================================================
section("C: controls (each must fire)")
# ======================================================================


def gain_split(q_dir):
    """offset c killing the t^2 term of chi_R - (t-c) q_dir, and the
    remainder polynomial (exact)."""
    c = sp.symbols("c")
    rem = sp.expand(chiR - (t - c) * q_dir)
    c_val = sp.solve(sp.Eq(rem.coeff(t, 2), 0), c)[0]
    return c_val, sp.expand(rem.subs(c, c_val))


adjP = (t * sp.eye(3) - R).adjugate()
q2 = sp.expand((E2 * adjP * ONES)[0])
D2 = sp.simplify(P.inv() * (ONES * E2) * P)
c2, r2 = gain_split(q2)
check("C1 FIRES: direction 1 e2^T: P^{-1}(1 e2^T)P = %s == "
      "[[1,0,1],0,0] != E11 (s leaks into the (1,3) coupling); q2 = %s;"
      " offset c = %s != 4; remainder %s == +8 CONSTANT GRAFT, not a "
      "t-tap" % (D2.tolist(), q2, c2, r2),
      D2 == sp.Matrix([[1, 0, 1], [0, 0, 0], [0, 0, 0]])
      and q2 == t ** 2 - t + 2 and c2 == 8 and r2 == 8
      and sp.expand(chiR - (t - c2) * q2 - r2) == 0, kill="K6")

q3 = sp.expand((E3 * adjP * ONES)[0])
D3 = sp.simplify(P.inv() * (ONES * E3) * P)
c3_, r3 = gain_split(q3)
check("C2 FIRES: direction 1 e3^T: P^{-1}(1 e3^T)P = %s NOT integral "
      "and != E11; q3 = %s; offset c = %s; remainder %s == 22t - 28 "
      "MIXED" % (D3.tolist(), q3, c3_, r3),
      D3 == sp.Matrix([[1, sp.Rational(1, 2), sp.Rational(3, 2)],
                       [0, 0, 0], [0, 0, 0]])
      and q3 == t ** 2 + t - 2 and c3_ == 10 and r3 == 22 * t - 28,
      kill="K6")

q_row = sp.expand((ONES.T * adjP * E1.T)[0])
Drow = sp.simplify(P.inv() * (E1.T * ONES.T) * P)
crow, rrow = gain_split(q_row)
drow_expect = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2),
                         sp.Rational(-1, 2)]) * sp.Matrix([[6, 1, 5]])
check("C3 FIRES: sibling ROW matrix e1 1^T: P^{-1}(e1 1^T)P = "
      "outer((1/2,1/2,-1/2),(6,1,5)) smeared over ALL rows, != E11; "
      "q_row = %s; offset c = %s == 4 = |mu4| COINCIDES (typed "
      "honestly) but remainder %s == -11t - 4 has a nonzero constant: "
      "the pure t-tap fails" % (q_row, crow, rrow),
      sp.simplify(Drow - drow_expect) == sp.zeros(3, 3)
      and Drow != sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
      and q_row == t ** 2 - 5 * t + 1 and crow == 4
      and rrow == -11 * t - 4, kill="K6")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if KILLS:
    VERDICT = {"K1": "RESIDUE-MISMATCH", "K2": "BASIS-MISMATCH",
               "K3": "FORM-MISMATCH", "K4": "COEFF-MISMATCH",
               "K5": "LATTICE-MISMATCH", "K6": "CONTROL-DEAD"}[KILLS[0]]
else:
    VERDICT = "FEEDBACK-NORMALFORM-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nPROMOTION-READY STATEMENT (report only -- no promotion, no edits):")
print("  THEOREM (feedback normal form of the winding line): with P =")
print("  [2*1 | e3 | R e3] (det -4, SNF diag(1,2,2)) the whole winding")
print("  line conjugates EXACTLY to M(s) = [[s+4,0,3],[0,0,-2],[4,1,5]]:")
print("  a gain channel s + |mu4|, the companion block of q_wind =")
print("  t^2 - g_car t + |Z2|, and the coupling pair (3,4) with loop")
print("  product N_fam x |mu4| = 12 = dim g_SM; hence chi_{R_s} =")
print("  (t - s - |mu4|) q_wind - 12t, and at s = 6 the (15,40,20)")
print("  coefficients are the three gain-10 readouts 10+5, 50+2-12,")
print("  10x2.  The deformation direction 1 e1^T is the ONLY direction")
print("  (among 1 e2^T, 1 e3^T, e1 1^T) whose conjugated deformation is")
print("  the pure gain E11 and whose remainder is a pure t-tap.")
print("  HONEST TYPE: the quotient Z^3/PZ^3 = Z2 x Z2 has cardinality 4")
print("  = |mu4| but exponent 2 -- same cardinality, NOT the same group;")
print("  no mu4 identification is claimed.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
