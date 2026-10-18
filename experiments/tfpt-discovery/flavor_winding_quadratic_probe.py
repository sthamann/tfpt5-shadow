#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""flavor_winding_quadratic_probe -- FLAVOR.WINDING.QUADRATIC.01 (the
I.5 mini-theorem of the 2026-08-08 morning analysis): the winding
deformation of the flavor residue matrix is controlled by ONE quadratic
q_wind(t) = t^2 - g_car t + |Z2|, exactly.

FROZEN CLAIMS (2026-08-08, frozen + SHA-hashed before first run):

 S1  THE RESIDUE MATRIX re-verified against the deployed invariants
     (v4_flavor_matrix.py + tfpt_2 winding boxes, read-only):
     R = [[1,3,0],[1,5,2],[2,5,3]]; det R = 8 = h(D5); tr R = 9;
     chi_R = t^3 - 9t^2 + 10t - 8; principal 2x2 minors (5,3,2)
     (deletion order), sorted {2,3,5}; SNF (1,1,8); ||R||_F^2 = 78;
     anchor column R e1 = a = (1,1,2); column sums (4,13,5);
     R^T a = (6,18,8); the cofactor seam normal n = (5,-9,6) = the
     common first adjugate row of R AND L, with n.1 = 2 = |Z2| and
     n^T R = (8,0,0) (tfpt_2 Winding Line box).
 S2  THE MINI-THEOREM (sympy, exact, symbols s and t): for
     R_s = R + s 1 e1^T:
       chi_{R_s}(t) = det(tI - R_s)
                    = t^3 - (9+s) t^2 + (10+5s) t - (8+2s)
     identically; equivalently  chi_{R_s} - chi_R = -s q_wind(t)  with
       q_wind(t) = t^2 - 5t + 2 = t^2 - g_car t + |Z2|
     (coefficient triple (1, -g_car, |Z2|), magnitudes (1,5,2)).
     SIGN CONVENTION typed: in the det(R_s - tI) convention (odd
     dimension) the deformation term is +s q_wind(t) -- the morning
     note's "+" form -- BOTH computed exactly.  The structural origin:
     the matrix determinant lemma gives q_wind(t) = e1^T adj(tI-R) 1
     (verified symbolically), so d(det R_s)/ds = q_wind(0) = 2 = |Z2|
     (the per-winding determinant increment of the deployed Winding
     Line box).  q_wind is irreducible over Q (disc = 17, nonsquare);
     the pencil has two s-INVARIANT base points: rem(chi_{R_s},
     q_wind, t) is s-free and equals rem(chi_R, q_wind, t).
     MEASURED COINCIDENCE (report): q_wind(6) = 8 = det R.
 S3  THE TRIPLE LOCK (three independent fixings, each solved exactly):
     tr R_s = 15 = dim A3      => s = 6;
     det R_s = 8 + 2s = 20 = 2 A_Lambda = |R(A4)|  => s = 6;
     Coxeter lift (R_s^T a)_1 = 6 + 4s = 30 = h(E8) => s = 6
     (the 4 is 1^T a = |mu4|); intersection = {6} = {|R+(A3)|}.
     At s = 6: chi_L = t^3 - 15t^2 + 40t - 20 with (15,40,20) =
     (dim A3, |R(D5)|, |R(A4)|); PrinMin2(R_s) = (5, 3(s+1), 2(s+1))
     symbolically, hence PrinMin2(L) = (5,21,14) = (g_car, 3x7, 2x7)
     (carrier minor 5 is s-INVARIANT); R_s^{-1} 1 = (1,1,-1)/(4+s);
     L = R + 6W rows = word lengths (7,3,0),(7,5,2),(8,5,3) (v4).
 S4  THE ROOT LOCUS (measure, don't narrate; exact Sturm/resultant):
     Delta(s) = disc_t(chi_{R_s}) computed exactly as a polynomial in
     s; FROZEN VALUES: Delta(0) = -7996 = -2^2 x 1999 (complex pair at
     s = 0, deployed) and Delta(6) = 39200 = 2^5 5^2 7^2 = 2 x 140^2
     > 0 (three real eigenvalues, deployed); s = 6 is NOT on the
     discriminant locus (Delta(6) != 0); the reality threshold s* lies
     in (2,3) (deployed ~2.83): exactly one real root of Delta in
     (2,3), and the real-eigenvalue count of chi_{R_s} jumps 1 -> 3
     between s = 2 and s = 3 (Sturm counts); at s = 6 the spectrum is
     3 real POSITIVE roots.  MEASURED AND TYPED (no frozen
     prediction): the full real-root census of Delta (count, factor
     decomposition over Q, rational isolations, minimal polynomial of
     s*), whether any collision point exists at s > 6, and the integer
     window s = -2..12 of Delta values with square / 2 x square
     typing (is 6 distinguished in the window? -- reported either
     way).
 C   CONTROLS (each must fire; exact):
     C1 direction 1 e2^T: the deformation quadratic is
        e2^T adj(tI-R) 1 = t^2 - t + 2 != q_wind (middle coefficient
        1 != g_car); the triple lock BREAKS: trace-fix {6}, det-fix
        {6} (constant term coincides -- typed honestly), Coxeter-fix
        EMPTY ((R_s^T a)_1 = 6 s-free) => intersection EMPTY.
     C2 direction 1 e3^T: quadratic t^2 + t - 2 = (t+2)(t-1) !=
        q_wind AND reducible (typed); det-fix {-6}, trace-fix {6},
        Coxeter-fix EMPTY => intersection EMPTY.
     C3 THE SIBLING ROW TRANSPORT e1 1^T (row instead of column):
        quadratic 1^T adj(tI-R) e1 = t^2 - 5t + 1: keeps the g_car
        coefficient, LOSES the |Z2| constant; fixings {6}, {12}, {24}
        pairwise disjoint (the measured doubling chain) =>
        intersection EMPTY.
     C4 THE SIBLING MINOR BRANCH (v4's control transported): the
        sibling triple {1,3,4} is unreachable on the whole winding
        line: 5 in PrinMin2(R_s) for EVERY s (the invariant carrier
        minor), 5 not in {1,3,4}; ratio 3:2 of the moving minors is
        s-invariant.

KILLS (any one fires => typed failure):
  K1 deployed residue invariants break        -> RESIDUE-MISMATCH
  K2 the quadratic law (S2) breaks            -> QUADRATIC-MISMATCH
  K3 the triple lock (S3) breaks              -> LOCK-BROKEN
  K4 the frozen locus values/counts break     -> LOCUS-BROKEN
  K5 a control does not fire                  -> CONTROL-DEAD

VERDICT (frozen enum): WINDING-QUADRATIC-EXACT / RESIDUE-MISMATCH /
QUADRATIC-MISMATCH / LOCK-BROKEN / LOCUS-BROKEN / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact sympy/integer arithmetic in every decision;
floats only in report-line prints of algebraic numbers; no RNG, no
fits.  NO physics claim.  Runtime cap: minutes.

Sources (read-only): verification/v4_flavor_matrix.py (R, sibling
branch), v10_projection_involution.py (6W forcing), v134_dual_anchor.py
(dual anchor), tfpt_2_standard_model.tex (winding-deformation keybox +
Winding Line box: chi_{R_s}, triple lock, disc values, s* ~ 2.83).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/flavor_winding_quadratic_probe.py
"""
import hashlib
import math
import time

import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []

G_CAR = 5
Z2 = 2
N_FAM = 3
MU4 = 4
H_E8 = 30
DIM_A3 = 15
R_D5 = 40
R_A4 = 20
A_LAMBDA = 10
RP_A3 = 6


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
print("FLAVOR.WINDING.QUADRATIC.01 -- chi_{R_s} = chi_R - s q_wind,")
print("q_wind = t^2 - g_car t + |Z2|; triple lock s = 6; root locus")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

t, s = sp.symbols("t s")
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
ONES = sp.Matrix([1, 1, 1])
E1 = sp.Matrix([[1, 0, 0]])
A = sp.Matrix([1, 1, 2])
L = R + 6 * sp.Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])

# ======================================================================
section("S1: the residue matrix against the deployed invariants (v4)")
# ======================================================================
chiR = sp.expand(R.charpoly(t).as_expr())
minors = [sp.det(R.minor_submatrix(k, k)) for k in range(3)]
from sympy.matrices.normalforms import smith_normal_form
snf = sorted(abs(int(x)) for x in smith_normal_form(R, domain=sp.ZZ)
             .diagonal())
check("S1.1 det R = %d == 8 = h(D5); tr R = %d == 9; chi_R = %s"
      % (R.det(), R.trace(), chiR),
      R.det() == 8 and R.trace() == 9
      and chiR == t ** 3 - 9 * t ** 2 + 10 * t - 8, kill="K1")
check("S1.2 PrinMin2(R) = %s == (5,3,2); sorted {2,3,5}; SNF %s == "
      "(1,1,8); ||R||_F^2 = %d == 78"
      % (tuple(minors), tuple(snf), sum(x ** 2 for x in R)),
      tuple(minors) == (5, 3, 2) and snf == [1, 1, 8]
      and sum(x ** 2 for x in R) == 78, kill="K1")
n_vec = R.adjugate().row(0)
check("S1.3 anchor R e1 = %s == (1,1,2); column sums %s == (4,13,5); "
      "R^T a = %s == (6,18,8)"
      % (tuple(R.col(0)), tuple(ONES.T * R), tuple(R.T * A)),
      tuple(R.col(0)) == (1, 1, 2)
      and tuple(ONES.T * R) == (4, 13, 5)
      and tuple(R.T * A) == (6, 18, 8), kill="K1")
check("S1.4 cofactor seam normal: adj(R) row 1 = %s == (5,-9,6) == "
      "adj(L) row 1; n.1 = %s == 2 = |Z2|; n^T R = %s == (8,0,0)"
      % (tuple(n_vec), (n_vec * ONES)[0], tuple(n_vec * R)),
      tuple(n_vec) == (5, -9, 6)
      and tuple(L.adjugate().row(0)) == (5, -9, 6)
      and (n_vec * ONES)[0] == 2 and tuple(n_vec * R) == (8, 0, 0),
      kill="K1")

# ======================================================================
section("S2: the mini-theorem -- one quadratic controls the deformation")
# ======================================================================
Rs = R + s * ONES * E1
chiS = sp.expand(Rs.charpoly(t).as_expr())
target = sp.expand(t ** 3 - (9 + s) * t ** 2 + (10 + 5 * s) * t
                   - (8 + 2 * s))
q_wind = t ** 2 - G_CAR * t + Z2
check("S2.1 chi_{R_s}(t) = det(tI - R_s) = t^3 - (9+s)t^2 + (10+5s)t "
      "- (8+2s) EXACT (sympy expand)",
      sp.expand(chiS - target) == 0, kill="K2")
check("S2.2 chi_{R_s} - chi_R = -s q_wind with q_wind = t^2 - 5t + 2 = "
      "t^2 - g_car t + |Z2| (triple (1,-5,2))",
      sp.expand(chiS - chiR + s * q_wind) == 0, kill="K2")
det_conv = sp.expand(sp.det(Rs - t * sp.eye(3)))
check("S2.3 SIGN CONVENTION typed: det(R_s - tI) = (-t^3 + 9t^2 - 10t "
      "+ 8) + s (t^2 - 5t + 2) -- the '+' reading, computed",
      sp.expand(det_conv - (-chiR + s * q_wind)) == 0, kill="K2")
adjP = (t * sp.eye(3) - R).adjugate()
lemma = sp.expand((E1 * adjP * ONES)[0])
check("S2.4 matrix determinant lemma: e1^T adj(tI-R) 1 = %s == q_wind; "
      "d(det R_s)/ds = q_wind(0) = %d == |Z2| (per-winding det "
      "increment)" % (lemma, lemma.subs(t, 0)),
      sp.expand(lemma - q_wind) == 0 and lemma.subs(t, 0) == Z2,
      kill="K2")
rem_s = sp.rem(chiS, q_wind, t)
check("S2.5 q_wind irreducible over Q (disc = %s, nonsquare); the two "
      "base points are s-INVARIANT: rem(chi_{R_s}, q_wind, t) = %s is "
      "s-free and = rem(chi_R, q_wind, t)"
      % (sp.discriminant(q_wind, t), sp.expand(rem_s)),
      sp.discriminant(q_wind, t) == 17
      and not sp.expand(rem_s).has(s)
      and sp.expand(rem_s - sp.rem(chiR, q_wind, t)) == 0, kill="K2")
print("      MEASURED COINCIDENCE (report): q_wind(6) = %s (= det R = 8)"
      % q_wind.subs(t, 6))

# ======================================================================
section("S3: the triple lock s = 6 (three independent exact fixings)")
# ======================================================================
fix_tr = sp.solve(sp.Eq(Rs.trace(), DIM_A3), s)
fix_det = sp.solve(sp.Eq(Rs.det(), R_A4), s)
cox = sp.expand((Rs.T * A)[0])
fix_cox = sp.solve(sp.Eq(cox, H_E8), s)
check("S3.1 tr R_s = 15 => s = %s; det R_s = 8+2s = 20 => s = %s; "
      "(R_s^T a)_1 = %s = 30 => s = %s; intersection {6} = {|R+(A3)|}"
      % (fix_tr, fix_det, cox, fix_cox),
      fix_tr == [6] and fix_det == [6] and fix_cox == [6]
      and sp.expand(cox - (6 + 4 * s)) == 0
      and int((ONES.T * A)[0]) == MU4, kill="K3")
chiL = sp.expand(L.charpoly(t).as_expr())
minorsS = [sp.factor(sp.det(Rs.minor_submatrix(k, k))) for k in range(3)]
check("S3.2 at s = 6: chi_L = %s == t^3 - 15t^2 + 40t - 20 with "
      "(15,40,20) = (dim A3, |R(D5)|, |R(A4)|)" % chiL,
      chiL == t ** 3 - DIM_A3 * t ** 2 + R_D5 * t - R_A4
      and sp.expand(chiS.subs(s, 6) - chiL) == 0, kill="K3")
check("S3.3 PrinMin2(R_s) = %s == (5, 3(s+1), 2(s+1)); at s = 6: "
      "(5,21,14) = (g_car, 3x7, 2x7); carrier minor 5 s-INVARIANT"
      % (tuple(minorsS),),
      sp.expand(minorsS[0] - 5) == 0
      and sp.expand(minorsS[1] - 3 * (s + 1)) == 0
      and sp.expand(minorsS[2] - 2 * (s + 1)) == 0
      and [m.subs(s, 6) for m in minorsS] == [5, 21, 14], kill="K3")
rsinv1 = sp.simplify(Rs.inv() * ONES)
check("S3.4 R_s^{-1} 1 = (1,1,-1)/(4+s) (keybox); L rows = word "
      "lengths (7,3,0),(7,5,2),(8,5,3) (v4)",
      sp.simplify(rsinv1 - sp.Matrix([1, 1, -1]) / (4 + s))
      == sp.zeros(3, 1)
      and [tuple(L.row(i)) for i in range(3)]
      == [(7, 3, 0), (7, 5, 2), (8, 5, 3)], kill="K3")

# ======================================================================
section("S4: the root locus (exact Sturm / resultant measurements)")
# ======================================================================
Delta = sp.expand(sp.discriminant(chiS, t))
D0 = int(Delta.subs(s, 0))
D6 = int(Delta.subs(s, 6))
check("S4.1 Delta(s) = disc_t chi_{R_s} = %s; Delta(0) = %d == -7996 = "
      "-2^2 x 1999; Delta(6) = %d == 39200 = 2^5 5^2 7^2 = 2 x 140^2; "
      "s = 6 NOT on the locus" % (Delta, D0, D6),
      D0 == -7996 and D6 == 39200 and D6 == 2 * 140 ** 2 and D6 != 0,
      kill="K4")
Dpoly = sp.Poly(Delta, s)
n_real = Dpoly.count_roots()
n_23 = Dpoly.count_roots(2, 3)
n_after6 = Dpoly.count_roots(6, 10 ** 9)
rr = sp.real_roots(Dpoly)
facs = sp.factor_list(Delta, s)
check("S4.2 FROZEN: exactly one real root of Delta in (2,3) (the "
      "reality threshold s*, deployed ~2.83): count = %d; Sturm real-"
      "eigenvalue counts of chi jump 1 -> 3 between s = 2 and s = 3: "
      "(%d, %d)"
      % (n_23, sp.Poly(chiS.subs(s, 2), t).count_roots(),
         sp.Poly(chiS.subs(s, 3), t).count_roots()),
      n_23 == 1
      and sp.Poly(chiS.subs(s, 2), t).count_roots() == 1
      and sp.Poly(chiS.subs(s, 3), t).count_roots() == 3, kill="K4")
check("S4.3 at s = 6: chi_L has 3 real POSITIVE roots (count all = %d, "
      "count in (0, inf) = %d)"
      % (sp.Poly(chiL, t).count_roots(),
         sp.Poly(chiL, t).count_roots(0, 10 ** 9)),
      sp.Poly(chiL, t).count_roots() == 3
      and sp.Poly(chiL, t).count_roots(0, 10 ** 9) == 3, kill="K4")
print("      MEASURED (typed): Delta real-root census: %d real roots; "
      "collision points at s > 6: %d" % (n_real, n_after6))
print("      factor_list(Delta) = %s" % (facs,))
for r_ in rr:
    print("      real root s* ~ %s  (minpoly %s)"
          % (sp.N(r_, 8), sp.minimal_polynomial(r_, s)))
print("      integer window s = -2..12 (value, square?, 2 x square?):")
for si in range(-2, 13):
    v = int(Delta.subs(s, si))
    sq = v >= 0 and math.isqrt(v) ** 2 == v
    tsq = v >= 0 and v % 2 == 0 and math.isqrt(v // 2) ** 2 == v // 2
    print("        s=%3d  Delta=%10d  square=%s  2xsquare=%s"
          % (si, v, sq, tsq))
window_flags = [si for si in range(-2, 13)
                if (lambda v: v >= 0 and v % 2 == 0
                    and math.isqrt(v // 2) ** 2 == v // 2)
                (int(Delta.subs(s, si)))]
print("      2 x square hits in window: %s (measured, typed)"
      % window_flags)

# ======================================================================
section("C: controls (each must fire)")
# ======================================================================
E2 = sp.Matrix([[0, 1, 0]])
E3 = sp.Matrix([[0, 0, 1]])


def lockset(D):
    """solution sets of the three fixings for deformation matrix D."""
    Ms = R + s * D
    f1 = set(sp.solve(sp.Eq(Ms.trace(), DIM_A3), s))
    f2 = set(sp.solve(sp.Eq(Ms.det(), R_A4), s))
    f3 = set(sp.solve(sp.Eq(sp.expand((Ms.T * A)[0]), H_E8), s))
    return f1, f2, f3


q2 = sp.expand((E2 * adjP * ONES)[0])
l2 = lockset(ONES * E2)
check("C1 FIRES: direction 1 e2^T: quadratic %s != q_wind (triple "
      "(1,-1,2)); locks (tr, det, Cox) = (%s, %s, %s): intersection "
      "EMPTY (det coincides -- typed; Coxeter kills)"
      % (q2, sorted(l2[0]), sorted(l2[1]), sorted(l2[2])),
      sp.expand(q2 - q_wind) != 0
      and q2 == t ** 2 - t + 2
      and l2[0] == {6} and l2[1] == {6} and l2[2] == set()
      and (l2[0] & l2[1] & l2[2]) == set(), kill="K5")

q3 = sp.expand((E3 * adjP * ONES)[0])
l3 = lockset(ONES * E3)
check("C2 FIRES: direction 1 e3^T: quadratic %s = %s != q_wind, "
      "REDUCIBLE (typed); locks (%s, %s, %s): intersection EMPTY"
      % (q3, sp.factor(q3), sorted(l3[0]), sorted(l3[1]), sorted(l3[2])),
      sp.expand(q3 - q_wind) != 0 and q3 == t ** 2 + t - 2
      and sp.factor(q3) == (t + 2) * (t - 1)
      and l3[0] == {6} and l3[1] == {-6} and l3[2] == set()
      and (l3[0] & l3[1] & l3[2]) == set(), kill="K5")

q_row = sp.expand((ONES.T * adjP * E1.T)[0])
lrow = lockset(E1.T * ONES.T)
check("C3 FIRES: sibling ROW transport e1 1^T: quadratic %s: keeps "
      "-g_car t, LOSES |Z2| (constant 1); locks (%s, %s, %s) pairwise "
      "disjoint (measured doubling chain 6/12/24): intersection EMPTY"
      % (q_row, sorted(lrow[0]), sorted(lrow[1]), sorted(lrow[2])),
      q_row == t ** 2 - 5 * t + 1
      and lrow[0] == {6} and lrow[1] == {12} and lrow[2] == {24}
      and (lrow[0] & lrow[1] & lrow[2]) == set(), kill="K5")

sib = sp.solve([sp.Eq(minorsS[1], 3), sp.Eq(minorsS[2], 4)], s)
sib_hit = any(set(int(m.subs(s, sv)) for m in minorsS) == {1, 3, 4}
              for sv in range(-100, 101))
check("C4 FIRES: sibling minor branch {1,3,4} unreachable on the whole "
      "winding line: 5 in PrinMin2(R_s) for EVERY s (invariant carrier "
      "minor), moving minors locked at ratio 3:2 (integer scan "
      "s = -100..100 finds no hit: %s)" % sib_hit,
      minorsS[0] == 5 and not sib_hit
      and sp.simplify(minorsS[1] / minorsS[2] - sp.Rational(3, 2)) == 0,
      kill="K5")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if KILLS:
    VERDICT = {"K1": "RESIDUE-MISMATCH", "K2": "QUADRATIC-MISMATCH",
               "K3": "LOCK-BROKEN", "K4": "LOCUS-BROKEN",
               "K5": "CONTROL-DEAD"}[KILLS[0]]
else:
    VERDICT = "WINDING-QUADRATIC-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION NOTES (report only -- no promotion, no edits):")
print("  * THE I.5 MINI-THEOREM: the whole winding line chi_{R_s} =")
print("    chi_R - s (t^2 - g_car t + |Z2|) is one rank-one determinant")
print("    lemma; the tfpt_2 keybox coefficients (9+s, 10+5s, 8+2s), the")
print("    det increment 2 = |Z2| and the minor law (5, 3(s+1), 2(s+1))")
print("    are all readouts of the single quadratic e1^T adj(tI-R) 1.")
print("  * THE LOCK: trace/det/Coxeter each solve to s = 6 alone; every")
print("    sibling direction (1e2^T, 1e3^T, e1 1^T) breaks the lock AND")
print("    changes the quadratic -- (1, -5, 2) is direction-specific.")
print("  * THE LOCUS: s = 6 is NOT a collision point (Delta(6) = 39200 =")
print("    2 x 140^2 > 0); the reality threshold is the Delta-root in")
print("    (2,3) (~2.83, deployed); the integer-window 2xsquare census is")
print("    typed above (measured, not narrated).")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
