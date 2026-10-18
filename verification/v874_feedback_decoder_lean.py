#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v874 -- FLAVOR.FEEDBACK.NORMALFORM.01 + E8.WINDING.DECODER.01 + the FlavorFeedback Lean mirror: TWO EXACT COMPILER THEOREMS from the 2026-08-08 evening campaign, one kernel-checked.  THEOREM 1, THE FEEDBACK NORMAL FORM (14/14, FEEDBACK-NORMALFORM-EXACT): one integral basis P = [2*1 | e3 | R e3] (det P = -4, SNF diag(1,2,2)) conjugates the WHOLE winding line R_s = R + s 1 e1^T to the gain-plus-companion form P^{-1} R_s P = [[s+4,0,3],[0,0,-2],[4,1,5]] EXACTLY (symbolic in s) -- a gain channel s + |mu4|, the companion block of the v857 winding quadratic q_wind = t^2 - g_car t + |Z2|, and the coupling pair (3,4) with loop product N_fam x |mu4| = 12 = dim g_SM; hence chi_{R_s}(t) = (t - s - |mu4|) q_wind(t) - 12t identically, and at the locked point s = 6 the (15, 40, 20) coefficients are the three gain-10 readouts 10+5, 50+2-12, 10x2.  The deformation direction 1 e1^T is the ONLY direction (vs 1 e2^T, 1 e3^T, e1 1^T -- all three controls fire) whose conjugated deformation is the pure gain E11 and whose remainder is a pure t-tap.  THE HONEST TYPING (load-bearing): the quotient Z^3/PZ^3 = Z2 x Z2 has CARDINALITY 4 = |mu4| but EXPONENT 2 -- the same cardinality as mu4 = Z4, NOT the same group; no mu4 identification is claimed.  THEOREM 2, THE WINDING DECODER (11/11, WINDING-DECODER-EXACT): q_wind maps the G31 clock alphabet {2,3,5,6} = {|Z2|, N_fam, g_car, |R+(A3)|} (v858) to (-4,-4,2,8) = (-|mu4|, -|mu4|, |Z2|, h(D5)), with q(2) = q(3) FORCED by the palindrome axis g_car/2 and 2+3=5; the decoder polynomial D(y) = (y+4)^2 (y-2)(y-8) = y^4 - 2y^3 - 48y^2 - 32y + 256 carries budget coefficients (|Z2|, Omega_adm = 48, 2^g_car = 32, 2^rank(E8) = 256); and |mu4| q(|Z2|)/|R(E8)| = -16/240 = -1/15 is EXACTLY the nonzero-character Walsh eigenvalue of the Gaussian census (v857/v875) -- the winding quadratic DECODES the message eigenvalue.  Sibling directions collapse the bridge; alternative alphabets change the decoder; the honest line typed: the -32 coefficient alone is not selective, the selective object is the full vector; TYPE: exact AUDIT theorem, NOT a physical functor (an explicit intertwiner would be needed to make it causal).  THE LEAN MIRROR: TfptCarrier/FlavorFeedback.lean kernel-checks theorem 1 (11 theorems: the three action identities, the inverse-free conjugation P F_s = R_s P over Z for symbolic s, charpoly_Rs in Z[X], the s = 6 instance, det P = -4 and the SNF determinantal divisors d1 = 1, d1 d2 = 2 forcing diag(1,2,2) -- with the Z2^2-vs-mu4 honest typing in the module doc).  ONE module from two probes (re-executed verbatim, embedded BYTE-EXACT, ~5 s) plus 4 Lean mirror checks.  Exact integer/sympy arithmetic in every probe decision; NO physics claim beyond the audit statements.  Python-only per GATE.WOLFRAM.02 (sympy symbolic; the Wolfram mirror carries the s = 6 lock via v857).

PROVENANCE: both probes frozen + SHA-hashed before first run (FROZEN_SPEC
SHA-256 printed and gated below); executed 2026-08-08 evening, re-executed
verbatim at this promotion in isolated namespaces with the byte-equality
provenance ward vs experiments/tfpt-discovery/.  Lean: lake build green
(3418 jobs), no sorry, no native_decide, axioms propext/Classical.choice/
Quot.sound on all 18 new theorems (FlavorFeedback 11 + GaussianShells 7,
the latter gated in v875), lean_manifest at 90 files.  NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

EXPECT_SHA_FLAVOR = ("f5f40996794860cccb35cc18759efc40b49a0cc0"
                     "9b8b0e9d12e07e80fe05bf9d")
EXPECT_SHA_DECODER = ("6a54768d9eed60467c6d05452b786c500466537"
                      "93f019c297c6418382059ac3e")

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_FLAVOR = r'''
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
'''

_SRC_DECODER = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""g31_winding_decoder_probe -- G31.WINDING.DECODER.01 (phase 1 of the
2026-08-08 evening plan): the winding quadratic q(t) = t^2 - g_car t +
|Z2| READS the G31 clock alphabet {2,3,5,6} into compiler atoms
{-|mu4|, -|mu4|, |Z2|, h(D5)}, packages them into ONE decoder polynomial
D(y) = (y+4)^2 (y-2)(y-8) = y^4 - 2y^3 - 48y^2 - 32y + 256, and bridges
EXACTLY to the Walsh eigenvalue -1/15 of the Gaussian census
(|mu4| q(|Z2|) / |R(E8)| = 4 x (-4) / 240 = -1/15, v857's law).

FROZEN CLAIMS (2026-08-08 evening, frozen + SHA-hashed before first run):

 S1  THE ALPHABET AND THE QUADRATIC (exact):
     S1.1 the clock alphabet {2,3,5,6} = {|Z2|, N_fam, g_car, |R+(A3)|}
     = Deg(G31)/4 (v858 normal form); the arithmetic pin recomputed
     HERE: the integer-quadruple census with product 46080 and sum 64
     returns EXACTLY [(8,12,20,24)]; the 607-group kill-scan
     selectivity (G31 the SOLE full-battery passer) is CITED from
     v858, not recomputed.
     S1.2 q(t) = t^2 - 5t + 2 (v857 part B winding quadratic) on the
     alphabet: q(2) = -4, q(3) = -4, q(5) = 2, q(6) = 8 EXACTLY; in
     compiler atoms {-|mu4|, -|mu4|, |Z2|, h(D5)} with h(D5) = 8.
     S1.3 THE PALINDROME (the complement check-code): q(5 - t) = q(t)
     identically (axis g_car/2), hence q(|Z2|) = q(N_fam) = -|mu4|
     BECAUSE 2 + 3 = 5 = g_car; typed honestly (measured): the
     reflection images of 5 and 6 are 0 and -1, OUTSIDE the alphabet
     (only the {2,3} pair is complement-closed).
 S2  THE DECODER POLYNOMIAL (exact expansion):
     S2.1 D(y) = prod_{a in {2,3,5,6}} (y - q(a)) = (y+4)^2 (y-2)(y-8)
     = y^4 - 2y^3 - 48y^2 - 32y + 256.
     S2.2 coefficient identification (signed coefficients
     (-2, -48, -32, +256)): 2 = |Z2|; 48 = Omega_adm = N_fam dim S+
     (ARCH.QUAD.01); 32 = 2^{g_car} = dim(S+ (+) S-); 256 =
     2^{rank E8}; the double root -4 = -|mu4| is FORCED by the
     palindrome pair {2,3} (report).
 S3  THE FOURIER BRIDGE (exact; v857 census law reproduced, not cited):
     S3.1 census rebuild on the 240 standard-model roots (v844/v857
     S6.3 machinery, read-only): V = L/(1+i)L has 15 nonzero classes
     x 16 roots, zero class EMPTY.
     S3.2 Walsh transform of the census: rhat(0) = 240, rhat(u) = -16
     for ALL 15 nonzero u; lambda_msg = -16/240 = -1/15 EXACT.
     S3.3 THE BRIDGE IDENTITY: |mu4| q(|Z2|) / |R(E8)| = 4 x (-4)/240
     = -1/15 = lambda_msg, and the SAME via q(N_fam) (the palindrome
     route): the winding quadratic evaluated at the sheet atom IS the
     nonzero-character Walsh eigenvalue, -16 = |mu4| q(|Z2|) = rhat(u).
 C   CONTROLS (each must fire; exact):
     C1 sibling deformation directions (probe-1 / v857 controls)
        change q and COLLAPSE the bridge: q2 = t^2 - t + 2 gives
        |mu4| q2(|Z2|)/240 = 16/240 = +1/15 != -1/15; q3 = t^2 + t - 2
        gives +1/15; q_row = t^2 - 5t + 1 gives -20/240 = -1/12.
     C2 sibling palindromes break the check-code: the axis of q2 is
        1/2 and of q3 is -1/2 (!= 5/2 = g_car/2); q2(3) = 8 != 4 =
        q2(2): the 2 <-> 3 complement symmetry dies off-direction.
     C3 alternative alphabets give DIFFERENT decoder polynomials:
        {2,3,5,7}: (y+4)^2 (y-2)(y-16) = y^4 - 10y^3 - 96y^2 - 32y
        + 512 (constant 2^9, NOT 2^{rank E8}; q(7) = 16);
        {1,2,3,5}: (y+2)(y+4)^2 (y-2) = y^4 + 8y^3 + 12y^2 - 32y - 64;
        HONEST LINE (typed, no kill): the -32 y coefficient SURVIVES
        in both alternatives -- per-coefficient selectivity is weak,
        the selective object is the full vector (-2,-48,-32,+256);
        the 6-vs-7 tension typed: replacing 6 = |R+(A3)| by 7 loses
        the y^3, y^2 and constant identifications; a third alphabet
        {3,5,6,7} is computed and reported (measured, not frozen).
 T   THE TYPING (mandatory, verbatim in the output): exact AUDIT
     theorem, NOT a physical functor -- an explicit intertwiner would
     be needed to make it causal; report only.

KILLS (any one fires => typed failure):
  K1 alphabet / arithmetic pin breaks           -> ALPHABET-MISMATCH
  K2 q-values / palindrome break                -> QVALUE-MISMATCH
  K3 decoder expansion / coefficients break     -> DECODER-MISMATCH
  K4 census / Walsh / bridge breaks             -> BRIDGE-MISMATCH
  K5 a control does not fire                    -> CONTROL-DEAD

VERDICT (frozen enum): WINDING-DECODER-EXACT / ALPHABET-MISMATCH /
QVALUE-MISMATCH / DECODER-MISMATCH / BRIDGE-MISMATCH / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact sympy/integer/Fraction arithmetic in every
decision; no floats, no RNG, no fits.  NO physics claim, NO RH claim.
Runtime cap: minutes.

Sources (read-only, machinery rebuilt inline): verification/
v858_g31_clock_alphabet.py (alphabet normal form + kill scan),
v857_simplex_fourier_winding.py (q_wind, census Walsh law -1/15,
S6.3 std-model census), v844_message_doily_rank.py + v833_gaussian_
ramification_ladder.py (class machinery), v832_anchor_flavor_
checksum.py (anchor/flavor context), ARCH.QUAD.01 (Omega_adm = 48).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/g31_winding_decoder_probe.py
"""
import hashlib
import itertools
import time
from fractions import Fraction as Fr

import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []

G_CAR = 5
Z2 = 2
N_FAM = 3
MU4 = 4
RP_A3 = 6
H_D5 = 8
OMEGA_ADM = 48
R_E8 = 240
RANK_E8 = 8
DEG31 = (8, 12, 20, 24)
ALPHABET = (2, 3, 5, 6)


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
print("G31.WINDING.DECODER.01 -- q(t) = t^2 - 5t + 2 reads {2,3,5,6} into")
print("{-4,-4,2,8}; D(y) = (y+4)^2(y-2)(y-8); |mu4| q(|Z2|)/240 = -1/15")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

t, y = sp.symbols("t y")
q = t ** 2 - G_CAR * t + Z2

# ======================================================================
section("S1: the alphabet and the quadratic")
# ======================================================================
quads = []
divs = [d for d in range(2, 46081) if 46080 % d == 0]
for d1 in divs:
    if d1 > 16:
        continue
    for d2 in divs:
        if d2 < d1 or 46080 % (d1 * d2) != 0:
            continue
        rest = 46080 // (d1 * d2)
        for d3 in divs:
            if d3 < d2 or rest % d3 != 0:
                continue
            d4 = rest // d3
            if d4 >= d3 and d1 + d2 + d3 + d4 == 64:
                quads.append((d1, d2, d3, d4))
check("S1.1 alphabet {2,3,5,6} = {|Z2|, N_fam, g_car, |R+(A3)|} = "
      "Deg(G31)/4 = %s; arithmetic pin recomputed: quadruples with "
      "product 46080, sum 64: %s == [(8,12,20,24)] UNIQUE"
      % (tuple(d // 4 for d in DEG31), quads),
      tuple(d // 4 for d in DEG31) == ALPHABET
      and set(ALPHABET) == {Z2, N_FAM, G_CAR, RP_A3}
      and quads == [DEG31], kill="K1")
print("      CITED (v858, not recomputed): the 607-group rank-4 kill "
      "scan --")
print("      G31 is the SOLE full-battery passer; weak-triple and "
      "raw-sum-64")
print("      impostors typed there.")

qvals = tuple(int(q.subs(t, a)) for a in ALPHABET)
check("S1.2 q on the alphabet: (q(2), q(3), q(5), q(6)) = %s == "
      "(-4,-4,2,8) = (-|mu4|, -|mu4|, |Z2|, h(D5))" % (qvals,),
      qvals == (-MU4, -MU4, Z2, H_D5), kill="K2")

pal = sp.expand(q.subs(t, G_CAR - t) - q)
check("S1.3 palindrome q(5-t) = q(t) identically (axis g_car/2); "
      "q(|Z2|) = q(N_fam) = -|mu4| BECAUSE 2 + 3 = 5 = g_car; "
      "reflection images of 5, 6 are %d, %d -- OUTSIDE the alphabet "
      "(typed: only {2,3} is complement-closed)"
      % (G_CAR - 5, G_CAR - 6),
      pal == 0 and Z2 + N_FAM == G_CAR
      and int(q.subs(t, Z2)) == int(q.subs(t, N_FAM)) == -MU4
      and (G_CAR - 5) not in ALPHABET and (G_CAR - 6) not in ALPHABET,
      kill="K2")

# ======================================================================
section("S2: the decoder polynomial D(y)")
# ======================================================================
D = sp.expand(sp.prod([y - v for v in qvals]))
D_target = y ** 4 - 2 * y ** 3 - 48 * y ** 2 - 32 * y + 256
D_factored = sp.expand((y + 4) ** 2 * (y - 2) * (y - 8))
check("S2.1 D(y) = prod (y - q(a)) = %s == (y+4)^2 (y-2)(y-8) == "
      "y^4 - 2y^3 - 48y^2 - 32y + 256" % D,
      sp.expand(D - D_target) == 0
      and sp.expand(D - D_factored) == 0, kill="K3")

coeffs = tuple(int(D.coeff(y, k)) for k in (3, 2, 1, 0))
check("S2.2 coefficients %s: 2 = |Z2|; 48 = Omega_adm = N_fam dim S+ "
      "= 3 x 16; 32 = 2^g_car = dim(S+ (+) S-); 256 = 2^rank(E8); "
      "double root -4 = -|mu4| forced by the palindrome pair {2,3}"
      % (coeffs,),
      coeffs == (-Z2, -OMEGA_ADM, -2 ** G_CAR, 2 ** RANK_E8)
      and OMEGA_ADM == N_FAM * 16 and 2 ** G_CAR == 32
      and qvals[0] == qvals[1] == -MU4, kill="K3")

# ======================================================================
section("S3: the Fourier bridge -- census Walsh law reproduced")
# ======================================================================
STD = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        STD.append(tuple(2 * a for a in v))
for yb in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in yb)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        STD.append(v)
STD = sorted(STD)


def in_L_std(v):
    if all(x % 2 == 0 for x in v):
        return sum(x // 2 for x in v) % 2 == 0
    if all(x % 2 == 1 for x in v):
        return sum(v) % 4 == 0
    return False


def in_pi2L_std(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L_std([x // 2 for x in w])


reps = []
label = {}
for r in STD:
    for li, rep in enumerate(reps):
        if in_pi2L_std(tuple(a - b for a, b in zip(r, rep))):
            label[r] = li
            break
    else:
        label[r] = len(reps)
        reps.append(r)
ZERO = (0,) * 8
REPS16 = [ZERO] + list(reps)


def cls16(v):
    return [k for k in range(16)
            if in_pi2L_std(tuple(a - b for a, b in zip(v, REPS16[k])))]


census = [0] * 16
for r in STD:
    census[label[r] + 1] += 1
check("S3.1 std-model census: %d classes + zero; census (zero; "
      "nonzero) = (%d; %s) == (0; 16 x15)"
      % (len(reps), census[0], sorted(set(census[1:]))),
      len(reps) == 15 and census[0] == 0
      and sorted(census[1:]) == [16] * 15, kill="K4")

ADD = [[None] * 16 for _ in range(16)]
add_ok = True
for a in range(16):
    for b in range(16):
        sv = tuple(x + z for x, z in zip(REPS16[a], REPS16[b]))
        hits = cls16(sv)
        if len(hits) != 1:
            add_ok = False
        else:
            ADD[a][b] = hits[0]
basis = []
for k in range(1, 16):
    closure = {0}
    frontier = [0]
    while frontier:
        x = frontier.pop()
        for g in basis:
            z = ADD[x][g]
            if z not in closure:
                closure.add(z)
                frontier.append(z)
    if k not in closure:
        basis.append(k)
COORD = {}
for bits in itertools.product((0, 1), repeat=4):
    c = 0
    for i, b in enumerate(bits):
        if b:
            c = ADD[c][basis[i]]
    COORD[c] = bits
RHAT = {}
for u in itertools.product((0, 1), repeat=4):
    RHAT[u] = sum((-1) ** (sum(a * b for a, b in zip(u, COORD[k])) % 2)
                  * census[k] for k in range(16))
U0 = (0, 0, 0, 0)
nz = sorted(set(RHAT[u] for u in RHAT if u != U0))
check("S3.2 Walsh: rhat(0) = %d == 240; rhat(u != 0) values %s == "
      "{-16}; lambda_msg = -16/240 = %s == -1/15"
      % (RHAT[U0], nz, Fr(-16, 240)),
      add_ok and len(COORD) == 16 and len(basis) == 4
      and RHAT[U0] == 240 and nz == [-16]
      and Fr(-16, 240) == Fr(-1, 15), kill="K4")

bridge = Fr(MU4 * int(q.subs(t, Z2)), R_E8)
bridge_fam = Fr(MU4 * int(q.subs(t, N_FAM)), R_E8)
check("S3.3 THE BRIDGE: |mu4| q(|Z2|)/|R(E8)| = 4 x (-4)/240 = %s == "
      "-1/15 == lambda_msg; same via q(N_fam) (palindrome route): %s; "
      "-16 = |mu4| q(|Z2|) = rhat(u)"
      % (bridge, bridge_fam),
      bridge == Fr(-1, 15) == bridge_fam
      and MU4 * int(q.subs(t, Z2)) == -16 == nz[0], kill="K4")

# ======================================================================
section("C: controls (each must fire)")
# ======================================================================
q2 = t ** 2 - t + 2
q3 = t ** 2 + t - 2
q_row = t ** 2 - 5 * t + 1
b2 = Fr(MU4 * int(q2.subs(t, Z2)), R_E8)
b3 = Fr(MU4 * int(q3.subs(t, Z2)), R_E8)
brow = Fr(MU4 * int(q_row.subs(t, Z2)), R_E8)
check("C1 FIRES: sibling directions collapse the bridge: q2 -> %s, "
      "q3 -> %s, q_row -> %s; none equals -1/15"
      % (b2, b3, brow),
      b2 == Fr(1, 15) and b3 == Fr(1, 15) and brow == Fr(-1, 12)
      and all(v != Fr(-1, 15) for v in (b2, b3, brow)), kill="K5")

ax2 = sp.Rational(1, 2)
ax3 = sp.Rational(-1, 2)
check("C2 FIRES: sibling palindromes: axis of q2 = %s, axis of q3 = %s "
      "(!= 5/2); q2(3) = %d != %d = q2(2): the 2 <-> 3 complement "
      "check-code dies off-direction"
      % (ax2, ax3, q2.subs(t, 3), q2.subs(t, 2)),
      sp.expand(q2.subs(t, 2 * ax2 - t) - q2) == 0
      and sp.expand(q3.subs(t, 2 * ax3 - t) - q3) == 0
      and ax2 != sp.Rational(5, 2) and ax3 != sp.Rational(5, 2)
      and int(q2.subs(t, 3)) == 8 != 4 == int(q2.subs(t, 2)), kill="K5")


def decoder(alphabet):
    return sp.expand(sp.prod([y - q.subs(t, a) for a in alphabet]))


D7 = decoder((2, 3, 5, 7))
D7_target = y ** 4 - 10 * y ** 3 - 96 * y ** 2 - 32 * y + 512
D1235 = decoder((1, 2, 3, 5))
D1235_target = y ** 4 + 8 * y ** 3 + 12 * y ** 2 - 32 * y - 64
D3567 = decoder((3, 5, 6, 7))
check("C3 FIRES: alternative alphabets: {2,3,5,7} -> %s (constant 512 "
      "= 2^9 NOT 2^rank(E8); q(7) = %d); {1,2,3,5} -> %s; both != D"
      % (D7, q.subs(t, 7), D1235),
      sp.expand(D7 - D7_target) == 0 and int(q.subs(t, 7)) == 16
      and sp.expand(D1235 - D1235_target) == 0
      and sp.expand(D7 - D) != 0 and sp.expand(D1235 - D) != 0
      and int(D7.coeff(y, 0)) == 512 != 256, kill="K5")
print("      HONEST LINE (typed, no kill): the -32 y coefficient "
      "survives in")
print("      BOTH alternatives (%s, %s) -- per-coefficient selectivity "
      "is weak;"
      % (int(D7.coeff(y, 1)), int(D1235.coeff(y, 1))))
print("      the selective object is the full vector (-2,-48,-32,+256).")
print("      6-vs-7 TENSION typed: replacing 6 = |R+(A3)| by 7 loses "
      "the y^3,")
print("      y^2 and constant identifications (10, 96, 512 are not "
      "compiler")
print("      atoms of this normal form).")
print("      MEASURED (report, not frozen): {3,5,6,7} -> %s" % D3567)

# ======================================================================
section("T: the typing (mandatory)")
# ======================================================================
print("  TYPING (verbatim): exact AUDIT theorem, NOT a physical functor")
print("  -- an explicit intertwiner would be needed to make it causal;")
print("  report only.")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if KILLS:
    VERDICT = {"K1": "ALPHABET-MISMATCH", "K2": "QVALUE-MISMATCH",
               "K3": "DECODER-MISMATCH", "K4": "BRIDGE-MISMATCH",
               "K5": "CONTROL-DEAD"}[KILLS[0]]
else:
    VERDICT = "WINDING-DECODER-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nPROMOTION-READY STATEMENT (report only -- no promotion, no edits):")
print("  THEOREM (winding decoder of the clock alphabet): the v857")
print("  winding quadratic q(t) = t^2 - g_car t + |Z2| maps the G31")
print("  clock alphabet {|Z2|, N_fam, g_car, |R+(A3)|} to the atom")
print("  quadruple (-|mu4|, -|mu4|, |Z2|, h(D5)) -- with q(|Z2|) =")
print("  q(N_fam) forced by the palindrome axis g_car/2 and 2 + 3 = 5;")
print("  the decoder D(y) = (y+4)^2 (y-2)(y-8) expands with signed")
print("  coefficients (|Z2|, Omega_adm, 2^g_car, 2^rank(E8)); and")
print("  |mu4| q(|Z2|)/|R(E8)| = -1/15 is EXACTLY the nonzero-character")
print("  Walsh eigenvalue of the Gaussian census (reproduced here on")
print("  the std-model roots).  Every sibling deformation direction")
print("  collapses the bridge; alternative alphabets change the")
print("  decoder (honest line: the -32 coefficient alone is not")
print("  selective).  TYPE: exact AUDIT theorem, NOT a physical")
print("  functor -- an explicit intertwiner would be needed to make it")
print("  causal; report only.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")
_SHA_RE = re.compile(r"FROZEN_SPEC SHA-256[ :=]+([0-9a-f]{64})")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (top-level probes: the whole analysis runs at exec
    time and exits via SystemExit); capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict, exp_code,
          exp_sha, gates):
    n, fails, verdict = _census(out)
    m = _SHA_RE.search(out)
    sha_ok = m is not None and m.group(1) == exp_sha
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False and sha_ok)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s (exp %s) "
          "| exit %d (exp %d) | spec SHA %s | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, "ok" if sha_ok else "MISMATCH", prov,
             verdict[:120]), flush=True)
    return ok


# ====== PART C -- the Lean mirror (FlavorFeedback.lean; kernel-checked
# statements cited, sympy witnesses here -- v849/v856 precedent)

_C_CHECKS = []


def _ccheck(name, ok, detail=""):
    _C_CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


_LEAN_THEOREMS = (
    "Rs_eq", "action_b0", "action_b1", "action_b2", "conjugation",
    "charpoly_Rs", "charpoly_L", "det_P", "natAbs_det_P",
    "snf_gcd_entries", "snf_gcd_minors",
)


def part_c():
    import sympy as sp
    from math import gcd
    print("\n" + "-" * 74)
    print("v874 PART C -- the Lean mirror: TfptCarrier/FlavorFeedback."
          "lean (kernel-checked; sympy witnesses here)")
    print("-" * 74, flush=True)
    t, s = sp.symbols("t s")
    R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
    ONES = sp.Matrix([1, 1, 1])
    E1 = sp.Matrix([[1, 0, 0]])
    Rs = R + s * ONES * E1
    P = sp.Matrix([[2, 0, 0], [2, 0, 2], [2, 1, 3]])
    F = sp.Matrix([[s + 4, 0, 3], [0, 0, -2], [4, 1, 5]])

    # C1: the inverse-free conjugation (Lean `conjugation`), symbolic s
    _ccheck("C1 THE CONJUGATION (conjugation, kernel-checked): P F_s = "
            "R_s P over Z for SYMBOLIC s -- the inverse-free house form "
            "of P^{-1} R_s P = F_s (det P = -4 != 0); verified "
            "symbolically here",
            sp.expand(P * F - Rs * P) == sp.zeros(3, 3))

    # C2: the charpoly identity in Z[X] (Lean `charpoly_Rs`/`charpoly_L`)
    chi = sp.expand(Rs.charpoly(t).as_expr())
    form = sp.expand((t - (s + 4)) * (t ** 2 - 5 * t + 2) - 12 * t)
    chi6 = sp.expand(chi.subs(s, 6))
    _ccheck("C2 THE CHARPOLY IDENTITY (charpoly_Rs / charpoly_L, "
            "kernel-checked): chi_{R_s}(t) = (t - (s+4))(t^2 - 5t + 2) "
            "- 12t in Z[X] symbolically, and at s = 6: chi_L = t^3 - "
            "15t^2 + 40t - 20",
            sp.expand(chi - form) == 0
            and chi6 == t ** 3 - 15 * t ** 2 + 40 * t - 20)

    # C3: the SNF determinantal divisors (Lean `det_P`/`snf_gcd_*`)
    entries = [int(P[i, j]) for i in range(3) for j in range(3)]
    g1 = 0
    for e in entries:
        g1 = gcd(g1, abs(e))
    minors = []
    for i in range(3):
        for j in range(3):
            M2 = P.copy()
            M2.row_del(i)
            M2.col_del(j)
            minors.append(int(M2.det()))
    g2 = 0
    for m in minors:
        g2 = gcd(g2, abs(m))
    _ccheck("C3 THE LATTICE INDEX (det_P / snf_gcd_entries / "
            "snf_gcd_minors, kernel-checked): det P = %d == -4, "
            "gcd(entries) = %d == 1, gcd(2x2 minors) = %d == 2 -- the "
            "determinantal divisors d1 = 1, d1 d2 = 2, d1 d2 d3 = 4 "
            "force SNF diag(1,2,2): quotient Z2 x Z2, cardinality 4 = "
            "|mu4| but exponent 2 -- NOT mu4 (the honest typing, "
            "kernel-checked rather than blurred)"
            % (P.det(), g1, g2),
            P.det() == -4 and g1 == 1 and g2 == 2)

    # C4: the Lean file inventory (structural)
    lean_path = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "lean4-carrier-rigidity",
        "TfptCarrier", "FlavorFeedback.lean"))
    ok_file = os.path.isfile(lean_path)
    missing, has_sorry = list(_LEAN_THEOREMS), False
    if ok_file:
        txt = open(lean_path, encoding="utf-8").read()
        body = txt.split("-/", 1)[1] if "-/" in txt else txt
        missing = [nm for nm in _LEAN_THEOREMS
                   if ("theorem %s " % nm) not in body
                   and ("theorem %s\n" % nm) not in body]
        has_sorry = (re.search(r"^\s*sorry\b", body, re.M) is not None
                     or "native_decide" in body)
    _ccheck("C4 THE LEAN INVENTORY (structural): TfptCarrier/"
            "FlavorFeedback.lean present with all %d theorems %s, no "
            "sorry / native_decide in the proof body (build green 3418 "
            "jobs, axioms propext/Classical.choice/Quot.sound on every "
            "theorem -- verified at promotion)"
            % (len(_LEAN_THEOREMS), list(_LEAN_THEOREMS)),
            ok_file and not missing and not has_sorry,
            "missing: %s" % missing if missing else "")
    print("  (kernel-checked statements: experiments/"
          "lean4-carrier-rigidity/TfptCarrier/FlavorFeedback.lean -- "
          "16 declarations (11 theorems), lake build green 3418 jobs, "
          "no sorry, no native_decide, axioms propext/Classical.choice/"
          "Quot.sound only; import wired in TfptCarrier.lean; "
          "lean_manifest.sha256 at 90 files)")


_PLAN = (
    ("flavor_feedback_probe", _SRC_FLAVOR, 14, (),
     "FEEDBACK-NORMALFORM-EXACT", 0, EXPECT_SHA_FLAVOR),
    ("g31_winding_decoder_probe", _SRC_DECODER, 11, (),
     "WINDING-DECODER-EXACT", 0, EXPECT_SHA_DECODER),
)


def run():
    t0 = time.time()
    _C_CHECKS.clear()
    print("=" * 74)
    print("v874 -- FLAVOR.FEEDBACK.NORMALFORM.01 + E8.WINDING.DECODER.01")
    print("+ the FlavorFeedback Lean mirror (two exact compiler theorems:")
    print("the winding line's gain-plus-companion normal form with the "
          "Z2^2-not-mu4")
    print("typing, and the clock-alphabet decoder hitting the -1/15 Walsh "
          "eigenvalue;")
    print("NO physics claim beyond the audit statements)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code, exp_sha in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, exp_sha, gates)
    part_c()
    ok_c = all(_C_CHECKS) and len(_C_CHECKS) == 4
    gates.append(ok_c)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v874: %d/%d gates passed (2 probe pattern gates + %d/4 Lean "
          "mirror checks) | runtime %.1f s"
          % (sum(gates), len(gates), sum(_C_CHECKS), time.time() - t0))
    print("The feedback normal form and the winding decoder are exact "
          "integer theorems;")
    print("the lattice quotient typing (Z2^2, not mu4) is kernel-checked, "
          "not blurred;")
    print("the decoder is an AUDIT theorem, not a physical functor.")
    print("[%s] v874 VERDICT GATE: FEEDBACK-NORMALFORM-EXACT + "
          "WINDING-DECODER-EXACT + the Lean mirror"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
