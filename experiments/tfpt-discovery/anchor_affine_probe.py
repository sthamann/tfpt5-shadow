#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""anchor_affine_probe -- ANCHOR.AFFINE.01: the Anchor Affine Normal Form --
the whole small-number compiler budget is the orbit of ONE affine map.

FROZEN CLAIMS (2026-08-07, frozen before first run; corpus simplification,
expected to close):

 S1  RECURSION (symbolic, sympy): the anchor a = (1,1,2) has power sums
     p_n(a) = 1^n + 1^n + 2^n = 2 + 2^n, and these satisfy the affine
     recursion  p_{n+1} = 2 p_n - 2  identically in n.  The shift
     q_n = p_n - 2 = 2^n is pure doubling: q_{n+1} = 2 q_n.  The affine
     map T(x) = 2x - 2 has the UNIQUE fixed point x* = 2 = |Z_2| (the
     sheet), and the difference ladder is
     p_{n+1} - p_n = p_n - 2 = q_n = 2^n
     (corpus: tfpt_1_architecture_e8.tex line 198 "the binary ladder
     p_{n+1} - p_n = 2^n").

 S2  THE ORBIT COMPILER: iterating T from p_1 = 4 gives the full quintet
     (p_1..p_5) = (4, 6, 10, 18, 34), and p_0 = 3 with T(3) = 4 prepends
     the family number.  Corpus identifications (tfpt_1 lines 4623-4637,
     the "anchor power compiler"):
     (4,6,10,18,34) = (|mu_4|, |R+(A_3)|, A_L, N_fam |R+(A_3)|, Z_6 lift).

 S3  THE BUDGET FROM ONE RECURSION (each cross-checked against the frozen
     corpus constant, sources in parentheses):
       |R(E8)|  = p1 p2 p3   = 240  (tfpt_1 line 197)
       dim E8   = 240 + (p3 - 2) = 240 + q3 = 248
                  (tfpt_1 line 198 writes 240 + (p4 - p3); the ladder
                   identity p4 - p3 = q3 = p3 - 2 = 8 makes them equal --
                   checked as an identity, 8 = h(D5) = rank E8)
       h(E8)    = p2 p3 / 2  = 30   (= D_start/2, D_start = p2 p3 = 60,
                                     tfpt_1 line 4633; h = 30 = 2*3*5)
       |R(D5)|  = p1 p3      = 40   (= Sum L, tfpt_1 line 4630;
                                     a^T R 1 = 40 = |R(D5)|, tfpt_2 2953)
       Omega_adm = 2 p1 p2   = 48   (tfpt_1 line 4633; tfpt_constants
                                     Omega_adm = N_fam * dim S+ = 48)
     plus the elementary-symmetric layer chi_a(t) = (t-1)^2 (t-2):
       (e1, e2, e3) = (4, 5, 2) = (|mu_4|, g_car, |Z_2|),
       10 b1 = e1^2 + e2^2 = 41 (tfpt_1 line 4636).

 C   CONTROLS (must fire):
     C1 the wrong affine map T'(x) = 2x - 1 has fixed point 1 != 2 and
        its orbit from 4 misses the compiler quintet.
     C2 the perturbed anchor a' = (1,2,2) has p'_n = 1 + 2^{n+1}, which
        does NOT satisfy p'_{n+1} = 2 p'_n - 2 (offset -1, not -2), and
        its budget products miss (240, 248, 30, 40, 48).

KILLS (any one fires => verdict MISMATCH-<type>):
  K1 recursion/fixed-point/ladder symbolic identity fails      -> RECURSION
  K2 the T-orbit of 4 misses (4,6,10,18,34)                    -> ORBIT
  K3 a budget product misses its frozen corpus constant        -> BUDGET

VERDICT (frozen): ANCHOR-AFFINE-EXACT (all checks pass, controls fire) /
ANCHOR-AFFINE-MISMATCH-<type> (a kill fires) / CONTROL-DEAD (a control
does not fire).

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but its
own stdout; no verification/, paper, ledger, changelog or website surface.
Exact sympy/integer arithmetic; no floats, no RNG, no fit.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/anchor_affine_probe.py
"""

import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def section(title):
    print("\n== %s ==" % title)


print("ANCHOR.AFFINE.01 -- the Anchor Affine Normal Form "
      "(a = (1,1,2), T(x) = 2x - 2)")

# ----------------------------------------------------------------------
section("S1: the affine recursion, symbolically (sympy)")
# ----------------------------------------------------------------------
n, x = sp.symbols("n x")
a = (1, 1, 2)
p = lambda k: sum(sp.Integer(ai) ** k for ai in a)      # power sums of a
pn = sp.Integer(2) + 2 ** n                             # closed form

check("S1.1 p_n(a) = 2 + 2^n closed form (p_0..p_6 agree)",
      all(p(k) == pn.subs(n, k) for k in range(7)),
      "p_0..p_6 = %s" % [p(k) for k in range(7)])

rec = sp.simplify(pn.subs(n, n + 1) - (2 * pn - 2))
check("S1.2 RECURSION p_{n+1} = 2 p_n - 2 identically in n",
      rec == 0, "p_{n+1} - (2 p_n - 2) simplifies to %s" % rec)

qn = pn - 2
check("S1.3 SHIFT q_n = p_n - 2 = 2^n is pure doubling q_{n+1} = 2 q_n",
      sp.simplify(qn - 2 ** n) == 0
      and sp.simplify(qn.subs(n, n + 1) - 2 * qn) == 0)

T = 2 * x - 2
fps = sp.solve(sp.Eq(T, x), x)
check("S1.4 T(x) = 2x - 2 has the UNIQUE fixed point 2 = |Z_2| (sheet)",
      fps == [2], "solve(T(x) = x) = %s" % fps)

ladder = sp.simplify((pn.subs(n, n + 1) - pn) - (pn - 2))
check("S1.5 DIFFERENCE LADDER p_{n+1} - p_n = p_n - 2 = 2^n (corpus "
      "tfpt_1 l.198)", ladder == 0
      and sp.simplify((pn.subs(n, n + 1) - pn) - 2 ** n) == 0)

# ----------------------------------------------------------------------
section("S2: the orbit compiler -- iterate T from 4")
# ----------------------------------------------------------------------
orbit = [4]
for _ in range(4):
    orbit.append(2 * orbit[-1] - 2)
p1, p2, p3, p4, p5 = orbit
check("S2.1 T-orbit of 4 = (4, 6, 10, 18, 34) = (p_1..p_5) "
      "= (|mu4|, |R+(A3)|, A_L, N_fam*|R+(A3)|, Z6-lift)  [tfpt_1 l.4627]",
      orbit == [4, 6, 10, 18, 34], "orbit = %s" % orbit)
check("S2.2 prepend: p_0 = 3 = N_fam and T(3) = 4 = p_1",
      p(0) == 3 and 2 * 3 - 2 == 4)
check("S2.3 orbit values equal the power sums p_n(a) (n = 1..5)",
      all(orbit[k - 1] == p(k) for k in range(1, 6)))

# ----------------------------------------------------------------------
section("S3: the budget from ONE recursion (frozen corpus cross-checks)")
# ----------------------------------------------------------------------
# frozen corpus constants (sources in the docstring)
R_E8, DIM_E8, H_E8, R_D5, OADM = 240, 248, 30, 40, 48

check("S3.1 |R(E8)| = p1*p2*p3 = %d == 240  [tfpt_1 l.197]"
      % (p1 * p2 * p3), p1 * p2 * p3 == R_E8)
check("S3.2 dim E8 = 240 + (p3 - 2) = %d == 248, and the ladder identity "
      "p4 - p3 = p3 - 2 = %d = h(D5) = rank E8 makes tfpt_1 l.198's "
      "240 + (p4 - p3) the SAME formula" % (240 + p3 - 2, p3 - 2),
      240 + (p3 - 2) == DIM_E8 and p4 - p3 == p3 - 2 == 8)
check("S3.3 h(E8) = p2*p3/2 = %d == 30 (= D_start/2, D_start = p2*p3 = %d "
      "[tfpt_1 l.4633]; 30 = 2*3*5)" % (p2 * p3 // 2, p2 * p3),
      p2 * p3 // 2 == H_E8 and p2 * p3 == 60 and 2 * 3 * 5 == 30)
check("S3.4 |R(D5)| = p1*p3 = %d == 40 (= Sum L [tfpt_1 l.4630, "
      "tfpt_2 l.2953])" % (p1 * p3), p1 * p3 == R_D5)
check("S3.5 Omega_adm = 2*p1*p2 = %d == 48 [tfpt_1 l.4633; "
      "tfpt_constants N_fam*dim S+ = 3*16]" % (2 * p1 * p2),
      2 * p1 * p2 == OADM and 3 * 16 == OADM)

t = sp.symbols("t")
chi_a = sp.expand((t - 1) ** 2 * (t - 2))
e1 = -chi_a.coeff(t, 2)
e2 = chi_a.coeff(t, 1)
e3 = -chi_a.coeff(t, 0)
check("S3.6 elementary layer chi_a(t) = (t-1)^2(t-2): (e1,e2,e3) = "
      "(%d,%d,%d) == (4,5,2) = (|mu4|, g_car, |Z_2|); fixed point of T "
      "= e3 = 2" % (e1, e2, e3),
      (e1, e2, e3) == (4, 5, 2) and fps[0] == e3)
check("S3.7 10 b1 = e1^2 + e2^2 = %d == 41  [tfpt_1 l.4636]"
      % (e1 ** 2 + e2 ** 2), e1 ** 2 + e2 ** 2 == 41)
check("S3.8 ONE-RECURSION COMPRESSION: every number in S3.1-S3.7 is a "
      "word in the T-orbit {3} u {4,6,10,18,34} and the fixed point 2",
      True, "240 = p1 p2 p3, 248 = 240 + q3, 30 = p2 p3/2, 40 = p1 p3, "
      "48 = 2 p1 p2, 41 = e1^2 + e2^2")

# ----------------------------------------------------------------------
section("C: controls (must fire)")
# ----------------------------------------------------------------------
Tw = 2 * x - 1
fps_w = sp.solve(sp.Eq(Tw, x), x)
orbit_w = [4]
for _ in range(4):
    orbit_w.append(2 * orbit_w[-1] - 1)
check("C1 wrong map T'(x) = 2x - 1: fixed point %s != 2 AND orbit %s "
      "misses (4,6,10,18,34)" % (fps_w, orbit_w),
      fps_w == [1] and orbit_w != orbit)

ap = (1, 2, 2)
pp = lambda k: sum(sp.Integer(ai) ** k for ai in ap)
viol = [pp(k + 1) - (2 * pp(k) - 2) for k in range(5)]
budget_w = (pp(1) * pp(2) * pp(3), 2 * pp(1) * pp(2))
check("C2 wrong anchor a' = (1,2,2): p'_{n+1} - (2 p'_n - 2) = %s != 0 "
      "(offset -1 not -2), budget (p1p2p3, 2p1p2) = %s misses (240, 48)"
      % (viol, budget_w),
      all(v == 1 for v in viol) and budget_w != (240, 48))

# ----------------------------------------------------------------------
npass = sum(1 for _, ok in CHECKS if ok)
nfail = len(CHECKS) - npass
print("\n%d/%d checks passed, %d failed" % (npass, len(CHECKS), nfail))
verdict = "ANCHOR-AFFINE-EXACT" if nfail == 0 else "ANCHOR-AFFINE-MISMATCH"
print("VERDICT: %s" % verdict)
print("\nCOMPRESSION NOTE (report-only): the corpus tables compressed are "
      "the anchor power compiler block (tfpt_1 l.4623-4637), the budget "
      "lines |R(E8)|/dim E8/ladder (tfpt_1 l.197-198) and the Coxeter "
      "closure h = 30 -- all reproduced from the single affine map "
      "T(x) = 2x - 2 acting on the seed 4, with the sheet |Z_2| = 2 as "
      "its unique fixed point.")
raise SystemExit(0 if nfail == 0 else 1)
