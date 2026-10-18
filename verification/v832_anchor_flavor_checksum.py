#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v832 -- ANCHOR.AFFINE.01 + FLAVOR.BIDIR.01: the anchor affine normal form and the flavor bidirectional checksum -- two exact corpus compressions, ONE module from two probes (18/18 + 15/15 checks, verdicts ANCHOR-AFFINE-EXACT and FLAVOR-BIDIR-CHECKSUM (selective); discovery probes anchor_affine_probe.py and flavor_bidir_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping).  PART A, THE ANCHOR AFFINE NORMAL FORM: the anchor a = (1,1,2) has power sums p_n(a) = 2 + 2^n satisfying the affine recursion p_{n+1} = 2 p_n - 2 identically in n (sympy); the shift q_n = p_n - 2 = 2^n is pure binary doubling; the map T(x) = 2x - 2 has the UNIQUE fixed point 2 = |Z_2| (the sheet), and the T-orbit of 4 is exactly the compiler quintet (4, 6, 10, 18, 34) = (|mu4|, |R+(A3)|, A_L, N_fam |R+(A3)|, Z6-lift) with p_0 = 3 = N_fam prepended by T(3) = 4.  THE BUDGET FROM ONE RECURSION: |R(E8)| = p1 p2 p3 = 240, dim E8 = 240 + q3 = 248 (with the ladder identity p4 - p3 = p3 - 2 = 8 = h(D5) = rank E8 making the corpus form 240 + (p4 - p3) the SAME formula), h(E8) = p2 p3/2 = 30 (D_start = p2 p3 = 60), |R(D5)| = p1 p3 = 40, Omega_adm = 2 p1 p2 = 48, and the elementary layer chi_a(t) = (t-1)^2 (t-2) with (e1, e2, e3) = (4, 5, 2) = (|mu4|, g_car, |Z_2|) and 10 b1 = e1^2 + e2^2 = 41 -- every number a word in the T-orbit and the fixed point.  PART B, THE FLAVOR BIDIRECTIONAL CHECKSUM: the residue matrix R = [[1,3,0],[1,5,2],[2,5,3]] decodes the SAME anchor on both sides -- R a = (4, 10, 13) = (p_1, p_3, N(3+2i)) and R^T a = (6, 18, 8) = (p_2, p_4, p_3 - 2), with tr R = 9 = p_0^2, det R = 8 = p_3 - 2, principal 2-minors {2,3,5} = {e_3, p_0, e_2}(a), chi_R = t^3 - p_0^2 t^2 + p_3 t - (p_3 - 2), and the corpus fingerprints ||R||_F^2 = 78, SNF diag(1,1,8), R^{-1} 1 = (1,1,-1)/4 re-anchored.  THE SIBLING ABLATION (the kill test): of the 12 down-row candidates (all orderings of the accepted {1,2,5} and the distinct-distance sibling {1,3,4}) EXACTLY ONE -- the accepted (1,5,2) -- satisfies the full identity set; the NEW kill test is the anchor contraction (R a)_2 = row.a = 10 = p_3 (the siblings give 11 and 12).  Controls fire (wrong map T' = 2x - 1, wrong anchor (1,2,2), the sibling (1,4,3) reproducing tfpt_2's failure numbers VERBATIM, the scrambled ordering (5,1,2)).  Exact sympy/integer arithmetic throughout; no floats, no RNG, no fit.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes anchor_affine_probe.py (18/18, verdict
ANCHOR-AFFINE-EXACT) and flavor_bidir_probe.py (15/15, verdict
FLAVOR-BIDIR-CHECKSUM (selective)), both 2026-08-07, re-run identically
at promotion; this module runs both frozen protocols VERBATIM (runtime
< 1 s).  The original probe docstrings and frozen protocols live in the
probe files verbatim (experiments/tfpt-discovery/).

CORPUS SURFACES COMPRESSED (sources): the anchor power compiler block
(tfpt_1 "anchor power compiler" table), the budget lines |R(E8)| / dim
E8 / binary ladder (tfpt_1), the Coxeter closure h = 30, the flavor
spectral-selector block and the bilinear table (tfpt_2), the sibling
failure line (tfpt_2).  No marker moves; the compression is a normal
form, not a new claim.
"""
import itertools

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

EXPECTED_A = "ANCHOR-AFFINE-EXACT"
EXPECTED_B = "FLAVOR-BIDIR-CHECKSUM (selective)"


def run():
    checks = []

    def check(name, ok, detail=""):
        checks.append(bool(ok))
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                               ("  -- " + detail) if detail else ""))
        return bool(ok)

    def section(title):
        print("\n== %s ==" % title)

    # ================================================================
    # PART A -- ANCHOR.AFFINE.01 (anchor_affine_probe verbatim)
    # ================================================================
    print("v832 PART A -- ANCHOR.AFFINE.01: the Anchor Affine Normal "
          "Form (a = (1,1,2), T(x) = 2x - 2)")

    section("A.S1: the affine recursion, symbolically (sympy)")
    n, x = sp.symbols("n x")
    a = (1, 1, 2)
    p = lambda k: sum(sp.Integer(ai) ** k for ai in a)   # power sums
    pn = sp.Integer(2) + 2 ** n                          # closed form

    check("S1.1 p_n(a) = 2 + 2^n closed form (p_0..p_6 agree)",
          all(p(k) == pn.subs(n, k) for k in range(7)),
          "p_0..p_6 = %s" % [p(k) for k in range(7)])
    rec = sp.simplify(pn.subs(n, n + 1) - (2 * pn - 2))
    check("S1.2 RECURSION p_{n+1} = 2 p_n - 2 identically in n",
          rec == 0, "p_{n+1} - (2 p_n - 2) simplifies to %s" % rec)
    qn = pn - 2
    check("S1.3 SHIFT q_n = p_n - 2 = 2^n is pure doubling "
          "q_{n+1} = 2 q_n",
          sp.simplify(qn - 2 ** n) == 0
          and sp.simplify(qn.subs(n, n + 1) - 2 * qn) == 0)
    T = 2 * x - 2
    fps = sp.solve(sp.Eq(T, x), x)
    check("S1.4 T(x) = 2x - 2 has the UNIQUE fixed point 2 = |Z_2| "
          "(sheet)", fps == [2], "solve(T(x) = x) = %s" % fps)
    ladder = sp.simplify((pn.subs(n, n + 1) - pn) - (pn - 2))
    check("S1.5 DIFFERENCE LADDER p_{n+1} - p_n = p_n - 2 = 2^n "
          "(corpus tfpt_1 binary ladder)", ladder == 0
          and sp.simplify((pn.subs(n, n + 1) - pn) - 2 ** n) == 0)

    section("A.S2: the orbit compiler -- iterate T from 4")
    orbit = [4]
    for _ in range(4):
        orbit.append(2 * orbit[-1] - 2)
    p1, p2, p3, p4, p5 = orbit
    check("S2.1 T-orbit of 4 = (4, 6, 10, 18, 34) = (p_1..p_5) = "
          "(|mu4|, |R+(A3)|, A_L, N_fam*|R+(A3)|, Z6-lift)",
          orbit == [4, 6, 10, 18, 34], "orbit = %s" % orbit)
    check("S2.2 prepend: p_0 = 3 = N_fam and T(3) = 4 = p_1",
          p(0) == 3 and 2 * 3 - 2 == 4)
    check("S2.3 orbit values equal the power sums p_n(a) (n = 1..5)",
          all(orbit[k - 1] == p(k) for k in range(1, 6)))

    section("A.S3: the budget from ONE recursion (frozen corpus "
            "cross-checks)")
    R_E8, DIM_E8, H_E8, R_D5, OADM = 240, 248, 30, 40, 48
    check("S3.1 |R(E8)| = p1*p2*p3 = %d == 240" % (p1 * p2 * p3),
          p1 * p2 * p3 == R_E8)
    check("S3.2 dim E8 = 240 + (p3 - 2) = %d == 248, and the ladder "
          "identity p4 - p3 = p3 - 2 = %d = h(D5) = rank E8 makes the "
          "corpus 240 + (p4 - p3) the SAME formula"
          % (240 + p3 - 2, p3 - 2),
          240 + (p3 - 2) == DIM_E8 and p4 - p3 == p3 - 2 == 8)
    check("S3.3 h(E8) = p2*p3/2 = %d == 30 (= D_start/2, D_start = "
          "p2*p3 = %d; 30 = 2*3*5)" % (p2 * p3 // 2, p2 * p3),
          p2 * p3 // 2 == H_E8 and p2 * p3 == 60 and 2 * 3 * 5 == 30)
    check("S3.4 |R(D5)| = p1*p3 = %d == 40 (= Sum L; a^T R 1 = 40 = "
          "|R(D5)|, tfpt_2)" % (p1 * p3), p1 * p3 == R_D5)
    check("S3.5 Omega_adm = 2*p1*p2 = %d == 48 (tfpt_constants "
          "N_fam*dim S+ = 3*16)" % (2 * p1 * p2),
          2 * p1 * p2 == OADM and 3 * 16 == OADM)
    t = sp.symbols("t")
    chi_a = sp.expand((t - 1) ** 2 * (t - 2))
    e1 = -chi_a.coeff(t, 2)
    e2 = chi_a.coeff(t, 1)
    e3 = -chi_a.coeff(t, 0)
    check("S3.6 elementary layer chi_a(t) = (t-1)^2(t-2): (e1,e2,e3) "
          "= (%d,%d,%d) == (4,5,2) = (|mu4|, g_car, |Z_2|); fixed "
          "point of T = e3 = 2" % (e1, e2, e3),
          (e1, e2, e3) == (4, 5, 2) and fps[0] == e3)
    check("S3.7 10 b1 = e1^2 + e2^2 = %d == 41" % (e1 ** 2 + e2 ** 2),
          e1 ** 2 + e2 ** 2 == 41)
    check("S3.8 ONE-RECURSION COMPRESSION: every number in S3.1-S3.7 "
          "is a word in the T-orbit {3} u {4,6,10,18,34} and the "
          "fixed point 2",
          True, "240 = p1 p2 p3, 248 = 240 + q3, 30 = p2 p3/2, "
          "40 = p1 p3, 48 = 2 p1 p2, 41 = e1^2 + e2^2")

    section("A.C: controls (must fire)")
    Tw = 2 * x - 1
    fps_w = sp.solve(sp.Eq(Tw, x), x)
    orbit_w = [4]
    for _ in range(4):
        orbit_w.append(2 * orbit_w[-1] - 1)
    check("C1 wrong map T'(x) = 2x - 1: fixed point %s != 2 AND orbit "
          "%s misses (4,6,10,18,34)" % (fps_w, orbit_w),
          fps_w == [1] and orbit_w != orbit)
    ap = (1, 2, 2)
    pp = lambda k: sum(sp.Integer(ai) ** k for ai in ap)
    viol = [pp(k + 1) - (2 * pp(k) - 2) for k in range(5)]
    budget_w = (pp(1) * pp(2) * pp(3), 2 * pp(1) * pp(2))
    check("C2 wrong anchor a' = (1,2,2): p'_{n+1} - (2 p'_n - 2) = %s "
          "!= 0 (offset -1 not -2), budget (p1p2p3, 2p1p2) = %s "
          "misses (240, 48)" % (viol, budget_w),
          all(v == 1 for v in viol) and budget_w != (240, 48))

    n_a = len(checks)
    fail_a = n_a - sum(checks)
    verdict_a = EXPECTED_A if fail_a == 0 else "ANCHOR-AFFINE-MISMATCH"
    print("\nPART A: %d/%d checks passed | VERDICT: %s"
          % (n_a - fail_a, n_a, verdict_a))

    # ================================================================
    # PART B -- FLAVOR.BIDIR.01 (flavor_bidir_probe verbatim)
    # ================================================================
    print("\nv832 PART B -- FLAVOR.BIDIR.01: R = [[1,3,0],[1,5,2],"
          "[2,5,3]] (tfpt_2), anchor a = (1,1,2)")

    def principal_minors2(M):
        out = []
        for k in range(3):
            idx = [i for i in range(3) if i != k]
            out.append(M[idx, idx].det())
        return tuple(out)

    A = sp.Matrix([1, 1, 2])                       # the anchor
    pw = {k: 2 + 2 ** k for k in range(5)}         # power sums of a
    R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])

    section("B.S1: spectral layer")
    check("S1.1 tr R = %d == 9 = p_0^2" % R.trace(),
          R.trace() == 9 == pw[0] ** 2)
    check("S1.2 det R = %d == 8 = p_3 - 2" % R.det(),
          R.det() == 8 == pw[3] - 2)
    minors = principal_minors2(R)
    e2b = 1 * 1 + 1 * 2 + 1 * 2
    e3b = 1 * 1 * 2
    check("S1.3 principal 2-minors (M11,M22,M33) = %s, set == {2,3,5} "
          "== {e_3(a), p_0(a), e_2(a)} = {%d, %d, %d}"
          % (str(minors), e3b, pw[0], e2b),
          set(minors) == {2, 3, 5} == {e3b, pw[0], e2b})
    chi = R.charpoly(t).as_expr()
    chi_target = t ** 3 - pw[0] ** 2 * t ** 2 + pw[3] * t - (pw[3] - 2)
    check("S1.4 chi_R(t) = %s == t^3 - p_0^2 t^2 + p_3 t - (p_3 - 2)"
          % sp.sstr(chi), sp.expand(chi - chi_target) == 0
          and chi == sp.expand(t ** 3 - 9 * t ** 2 + 10 * t - 8))
    check("S1.5 coefficient readback: sum minors = %d = p_3 = A_L, "
          "prod minors = %d = 30 = h(E8)"
          % (sum(minors), sp.prod(minors)),
          sum(minors) == 10 and sp.prod(minors) == 30)
    frob = sum(v ** 2 for v in R)
    snf = smith_normal_form(R, domain=ZZ)
    rinv1 = R.inv() * sp.Matrix([1, 1, 1])
    check("S1.6 corpus fingerprints: ||R||_F^2 = %d == 78 = dim E6; "
          "SNF = %s == diag(1,1,8); R^-1 1 = %s == (1,1,-1)/4"
          % (frob, snf.diagonal(), rinv1.T),
          frob == 78 and list(snf.diagonal()) == [1, 1, 8]
          and rinv1 == sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 4),
                                  sp.Rational(-1, 4)]))

    section("B.S2: the bidirectional anchor readout")
    Ra = R * A
    RTa = R.T * A
    check("S2.1 R a = %s == (4, 10, 13) = (p_1, p_3, N(3+2i))"
          % str(tuple(Ra)),
          tuple(Ra) == (4, 10, 13) == (pw[1], pw[3], 13))
    check("S2.2 R^T a = %s == (6, 18, 8) = (p_2, p_4, p_3 - 2)"
          % str(tuple(RTa)),
          tuple(RTa) == (6, 18, 8) == (pw[2], pw[4], pw[3] - 2))
    z = 3 + 2 * sp.I
    norm13 = sp.expand(z * sp.conjugate(z))
    check("S2.3 N(3+2i) = (3+2i)(3-2i) = %s == 13 exactly in Z[i] "
          "(corpus: Delta_Q; v222/v230/v415)" % norm13, norm13 == 13)
    check("S2.4 BIDIRECTIONALITY: the SAME anchor decodes both sides "
          "-- rows read (p_1, p_3, 13), columns read (p_2, p_4, "
          "p_3-2); union covers p_1..p_4 plus {8 = h(D5), 13 = "
          "Delta_Q}",
          set(tuple(Ra) + tuple(RTa)) == {4, 10, 13, 6, 18, 8})

    section("B.S3: the sibling ablation (kill test)")
    ROW_U, ROW_E = (1, 3, 0), (2, 5, 3)
    TARGET = dict(tr=9, det=8, minors={2, 3, 5},
                  chi=sp.expand(t ** 3 - 9 * t ** 2 + 10 * t - 8),
                  Ra=(4, 10, 13), RTa=(6, 18, 8))
    candidates = (sorted(set(itertools.permutations((1, 2, 5))))
                  + sorted(set(itertools.permutations((1, 3, 4)))))
    passing = []
    print("    down-row candidate | row.a | tr det minors        | "
          "full set T?")
    for row in candidates:
        M = sp.Matrix([ROW_U, list(row), ROW_E])
        mins = principal_minors2(M)
        res = dict(tr=M.trace(), det=M.det(), minors=set(mins),
                   chi=M.charpoly(t).as_expr(),
                   Ra=tuple(M * A), RTa=tuple(M.T * A))
        ok = all(res[k] == TARGET[k] for k in TARGET)
        if ok:
            passing.append(row)
        print("    %-18s | %5d | %2d  %3d  %-14s | %s"
              % (str(row), sum(r * ai for r, ai in zip(row, (1, 1, 2))),
                 res["tr"], res["det"], str(mins),
                 "YES" if ok else "no"))
    check("S3.1 the accepted ordering (1,5,2) satisfies the FULL "
          "identity set T", (1, 5, 2) in passing)
    check("S3.2 anchor contraction (THE NEW KILL TEST): (1,5,2).a = "
          "10 = p_3; (1,4,3).a = 11; (1,3,4).a = 12 -- both siblings "
          "miss p_3",
          1 + 5 + 4 == 10 and 1 + 4 + 6 == 11 and 1 + 3 + 8 == 12)
    check("S3.3 SELECTIVITY (the kill decision): passing set = %s == "
          "{(1,5,2)} -- no sibling ordering and no re-ordering of "
          "{1,2,5} satisfies T" % str(passing),
          passing == [(1, 5, 2)])

    section("B.C: controls (must fire)")
    Rp = sp.Matrix([ROW_U, [1, 4, 3], ROW_E])
    Lp = Rp + 6 * sp.Matrix([1, 1, 1]) * sp.Matrix([[1, 0, 0]])
    mins_p = principal_minors2(Rp)
    frob_p = sum(v ** 2 for v in Rp)
    check("C1 sibling (1,4,3) reproduces tfpt_2's failure numbers "
          "VERBATIM: tr = %d == 8, det = %d == 6, minors %s == "
          "{-3,1,3}, ||.||^2 = %d == 74, det L' = %d == -12"
          % (Rp.trace(), Rp.det(), str(mins_p), frob_p, Lp.det()),
          Rp.trace() == 8 and Rp.det() == 6
          and set(mins_p) == {-3, 1, 3}
          and frob_p == 74 and Lp.det() == -12)
    Rs = sp.Matrix([ROW_U, [5, 1, 2], ROW_E])
    ok_s = (Rs.trace() == 9 and Rs.det() == 8
            and set(principal_minors2(Rs)) == {2, 3, 5}
            and tuple(Rs * A) == (4, 10, 13))
    check("C2 scrambled accepted ordering (5,1,2) does NOT pass "
          "(tr = %d, det = %d, minors = %s, R a = %s)"
          % (Rs.trace(), Rs.det(), str(principal_minors2(Rs)),
             str(tuple(Rs * A))), not ok_s)

    n_all = len(checks)
    n_b = n_all - n_a
    fail_b = (n_all - sum(checks)) - fail_a
    if fail_b == 0 and passing == [(1, 5, 2)]:
        verdict_b = EXPECTED_B
    elif len(passing) > 1:
        verdict_b = "FLAVOR-BIDIR-NONSELECTIVE"
    else:
        verdict_b = "FLAVOR-BIDIR-MISMATCH"
    print("\nPART B: %d/%d checks passed | VERDICT: %s"
          % (n_b - fail_b, n_b, verdict_b))

    n_fail = n_all - sum(checks)
    pattern_ok = (verdict_a == EXPECTED_A and verdict_b == EXPECTED_B)
    print("\n" + "=" * 64)
    print("v832: %d/%d checks passed, %d failed"
          % (sum(checks), n_all, n_fail))
    print("[%s] PATTERN GATE: verdicts %s + %s (expected %s + %s)"
          % ("PASS" if pattern_ok else "FAIL", verdict_a, verdict_b,
             EXPECTED_A, EXPECTED_B))
    return n_fail + (0 if pattern_ok else 1)


if __name__ == "__main__":
    raise SystemExit(run())
