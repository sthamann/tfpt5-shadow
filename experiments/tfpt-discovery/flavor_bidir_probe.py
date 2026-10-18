#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""flavor_bidir_probe -- FLAVOR.BIDIR.01: the flavor residue matrix R as a
BIDIRECTIONAL anchor decoder, with the sibling-branch ablation as kill test.

MATRIX SOURCE (verified against the paper before freezing): R appears
verbatim in tfpt_2_standard_model.tex at lines 197 (tikz), 220 (L = R + 6W
display) and 2927 (spectral-selector equation):
    R = [[1,3,0],[1,5,2],[2,5,3]]   (rows = sectors u, d, e; cols = gen 1,2,3)
The sibling branch is documented at tfpt_2 lines 2920-2941: the down sector
is the single binary choice {1,2,5} vs the distinct-distance sibling
{1,3,4}; line 2941 quotes for the sibling (ordering (1,4,3)): tr R' = 8,
det R' = 6, minors (-3,1,3), ||R'||_F^2 = 74, det L' = -12.

FROZEN CLAIMS (2026-08-07, frozen before first run; anchor a = (1,1,2),
p_n = p_n(a) = 2 + 2^n, so p_0 = 3, p_1 = 4, p_2 = 6, p_3 = 10, p_4 = 18):

 S1  SPECTRAL LAYER (exact):  tr R = 9 = p_0^2;  det R = 8 = p_3 - 2;
     the three principal 2x2 minors are {2,3,5}, identified as
     {e_3(a), p_0(a), e_2(a)} = {1*1*2, 3, 1+2+2};
     chi_R(t) = t^3 - 9 t^2 + 10 t - 8
              = t^3 - p_0^2 t^2 + p_3 t - (p_3 - 2).
     Corpus fingerprints re-anchored: ||R||_F^2 = 78, SNF = diag(1,1,8),
     R^{-1} 1 = (1,1,-1)/4  (tfpt_2 lines 2935-2939).

 S2  BIDIRECTIONAL READOUT (exact):
       R  a = ( 4, 10, 13) = (p_1, p_3, N(3+2i))
       R^T a = ( 6, 18,  8) = (p_2, p_4, p_3 - 2)
     with N(3+2i) = (3+2i)(3-2i) = 13 verified exactly in Z[i]; corpus
     appearances of 13 = Delta_Q = N(3+2i): tfpt_safeguards.tex l.131,
     v222_cm_norm_duality (Gaussian CM norm), v230 (center budget),
     v415 (operator eigenvalue 3+2i).

 S3  SIBLING ABLATION (the kill test): with rows u = (1,3,0) and
     e = (2,5,3) frozen, replace the down row by each of the 12
     candidates: all 6 orderings of the accepted set {1,2,5} and all 6
     orderings of the sibling set {1,3,4}.  The FULL identity set is
       T = { tr = 9, det = 8, minors = {2,3,5},
             chi = t^3 - 9t^2 + 10t - 8,
             R a = (4,10,13), R^T a = (6,18,8) }.
     FROZEN EXPECTATION: the accepted ordering (1,5,2) is the UNIQUE
     candidate satisfying all of T; in particular the anchor contraction
     row.a: (1,5,2).a = 10 = p_3, (1,4,3).a = 11 != 10, (1,3,4).a = 12.
     KILL: if ANY other candidate (in particular any sibling ordering)
     satisfies the full set T, the checksum is NOT selective.
     Paper cross-check: the ordering (1,4,3) must reproduce tfpt_2
     l.2941 exactly (tr 8, det 6, minors {-3,1,3}, ||.||^2 74,
     det L' = -12 with L' = R' + 6*1 e_1^T).

 C   CONTROLS (must fire): C1 the sibling (1,4,3) reproduces the paper's
     failure numbers verbatim; C2 a scrambled accepted ordering (5,1,2)
     breaks the identity set (it must NOT pass).

VERDICT (frozen): FLAVOR-BIDIR-CHECKSUM (S1+S2 exact AND (1,5,2) unique
in S3) / FLAVOR-BIDIR-NONSELECTIVE (another candidate passes the full
set T) / FLAVOR-BIDIR-MISMATCH (an S1/S2 identity fails).

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but its
own stdout; no verification/, paper, ledger, changelog or website surface.
Exact sympy/integer arithmetic; no floats, no RNG, no fit.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/flavor_bidir_probe.py
"""

import itertools

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def section(title):
    print("\n== %s ==" % title)


def principal_minors2(M):
    """the three principal 2x2 minors (delete row/col k, k = 0,1,2)."""
    out = []
    for k in range(3):
        idx = [i for i in range(3) if i != k]
        out.append(M[idx, idx].det())
    return tuple(out)


t = sp.symbols("t")
A = sp.Matrix([1, 1, 2])                       # the anchor
p = {k: 2 + 2 ** k for k in range(5)}          # power sums of (1,1,2)
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])

print("FLAVOR.BIDIR.01 -- R = [[1,3,0],[1,5,2],[2,5,3]] "
      "(tfpt_2 l.197/220/2927), anchor a = (1,1,2)")

# ----------------------------------------------------------------------
section("S1: spectral layer")
# ----------------------------------------------------------------------
check("S1.1 tr R = %d == 9 = p_0^2" % R.trace(),
      R.trace() == 9 == p[0] ** 2)
check("S1.2 det R = %d == 8 = p_3 - 2" % R.det(), R.det() == 8 == p[3] - 2)

minors = principal_minors2(R)
e2 = 1 * 1 + 1 * 2 + 1 * 2
e3 = 1 * 1 * 2
check("S1.3 principal 2-minors (M11,M22,M33) = %s, set == {2,3,5} == "
      "{e_3(a), p_0(a), e_2(a)} = {%d, %d, %d}"
      % (str(minors), e3, p[0], e2),
      set(minors) == {2, 3, 5} == {e3, p[0], e2})

chi = R.charpoly(t).as_expr()
chi_target = t ** 3 - p[0] ** 2 * t ** 2 + p[3] * t - (p[3] - 2)
check("S1.4 chi_R(t) = %s == t^3 - p_0^2 t^2 + p_3 t - (p_3 - 2)"
      % sp.sstr(chi), sp.expand(chi - chi_target) == 0
      and chi == sp.expand(t ** 3 - 9 * t ** 2 + 10 * t - 8))
check("S1.5 coefficient readback: sum minors = %d = p_3 = A_L, "
      "prod minors = %d = 30 = h(E8)"
      % (sum(minors), sp.prod(minors)),
      sum(minors) == 10 and sp.prod(minors) == 30)

frob = sum(x ** 2 for x in R)
snf = smith_normal_form(R, domain=ZZ)
rinv1 = R.inv() * sp.Matrix([1, 1, 1])
check("S1.6 corpus fingerprints: ||R||_F^2 = %d == 78 = dim E6; "
      "SNF = %s == diag(1,1,8); R^-1 1 = %s == (1,1,-1)/4"
      % (frob, snf.diagonal(), rinv1.T),
      frob == 78 and list(snf.diagonal()) == [1, 1, 8]
      and rinv1 == sp.Matrix([sp.Rational(1, 4), sp.Rational(1, 4),
                              sp.Rational(-1, 4)]))

# ----------------------------------------------------------------------
section("S2: the bidirectional anchor readout")
# ----------------------------------------------------------------------
Ra = R * A
RTa = R.T * A
check("S2.1 R a = %s == (4, 10, 13) = (p_1, p_3, N(3+2i))"
      % str(tuple(Ra)),
      tuple(Ra) == (4, 10, 13) == (p[1], p[3], 13))
check("S2.2 R^T a = %s == (6, 18, 8) = (p_2, p_4, p_3 - 2)"
      % str(tuple(RTa)),
      tuple(RTa) == (6, 18, 8) == (p[2], p[4], p[3] - 2))

z = 3 + 2 * sp.I
norm13 = sp.expand(z * sp.conjugate(z))
check("S2.3 N(3+2i) = (3+2i)(3-2i) = %s == 13 exactly in Z[i] "
      "(corpus: Delta_Q, tfpt_safeguards l.131, v222/v230/v415)"
      % norm13, norm13 == 13)
check("S2.4 BIDIRECTIONALITY: the SAME anchor decodes both sides -- "
      "rows read (p_1, p_3, 13), columns read (p_2, p_4, p_3-2); "
      "union covers p_1..p_4 plus {8 = h(D5), 13 = Delta_Q}",
      set(tuple(Ra) + tuple(RTa)) == {4, 10, 13, 6, 18, 8})

# ----------------------------------------------------------------------
section("S3: the sibling ablation (kill test)")
# ----------------------------------------------------------------------
ROW_U, ROW_E = (1, 3, 0), (2, 5, 3)
TARGET = dict(tr=9, det=8, minors={2, 3, 5},
              chi=sp.expand(t ** 3 - 9 * t ** 2 + 10 * t - 8),
              Ra=(4, 10, 13), RTa=(6, 18, 8))

candidates = (sorted(set(itertools.permutations((1, 2, 5))))
              + sorted(set(itertools.permutations((1, 3, 4)))))
passing = []
print("    down-row candidate | row.a | tr det minors        | full set T?")
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
             res["tr"], res["det"], str(mins), "YES" if ok else "no"))

check("S3.1 the accepted ordering (1,5,2) satisfies the FULL identity "
      "set T", (1, 5, 2) in passing)
check("S3.2 anchor contraction: (1,5,2).a = 10 = p_3; (1,4,3).a = 11; "
      "(1,3,4).a = 12 -- both siblings miss p_3",
      1 + 5 + 4 == 10 and 1 + 4 + 6 == 11 and 1 + 3 + 8 == 12)
check("S3.3 SELECTIVITY (the kill decision): passing set = %s == "
      "{(1,5,2)} -- no sibling ordering and no re-ordering of {1,2,5} "
      "satisfies T" % str(passing), passing == [(1, 5, 2)])

# ----------------------------------------------------------------------
section("C: controls (must fire)")
# ----------------------------------------------------------------------
Rp = sp.Matrix([ROW_U, [1, 4, 3], ROW_E])
Lp = Rp + 6 * sp.Matrix([1, 1, 1]) * sp.Matrix([[1, 0, 0]])
mins_p = principal_minors2(Rp)
frob_p = sum(x ** 2 for x in Rp)
check("C1 sibling (1,4,3) reproduces tfpt_2 l.2941 VERBATIM: tr = %d "
      "== 8, det = %d == 6, minors %s == {-3,1,3}, ||.||^2 = %d == 74, "
      "det L' = %d == -12"
      % (Rp.trace(), Rp.det(), str(mins_p), frob_p, Lp.det()),
      Rp.trace() == 8 and Rp.det() == 6 and set(mins_p) == {-3, 1, 3}
      and frob_p == 74 and Lp.det() == -12)

Rs = sp.Matrix([ROW_U, [5, 1, 2], ROW_E])
ok_s = (Rs.trace() == 9 and Rs.det() == 8
        and set(principal_minors2(Rs)) == {2, 3, 5}
        and tuple(Rs * A) == (4, 10, 13))
check("C2 scrambled accepted ordering (5,1,2) does NOT pass "
      "(tr = %d, det = %d, minors = %s, R a = %s)"
      % (Rs.trace(), Rs.det(), str(principal_minors2(Rs)),
         str(tuple(Rs * A))), not ok_s)

# ----------------------------------------------------------------------
npass = sum(1 for _, ok in CHECKS if ok)
nfail = len(CHECKS) - npass
print("\n%d/%d checks passed, %d failed" % (npass, len(CHECKS), nfail))
if nfail == 0 and passing == [(1, 5, 2)]:
    verdict = "FLAVOR-BIDIR-CHECKSUM (selective)"
elif len(passing) > 1:
    verdict = "FLAVOR-BIDIR-NONSELECTIVE"
else:
    verdict = "FLAVOR-BIDIR-MISMATCH"
print("VERDICT: %s" % verdict)
print("\nCOMPRESSION NOTE (report-only): compresses the spectral-selector "
      "block tfpt_2 l.2920-2941 (tr/det/minors/chi + sibling failure) and "
      "the bilinear table l.2949-2961 (a^T R 1 = 40 etc.) into ONE "
      "statement: R is the unique branch whose row AND column contractions "
      "against the anchor return the power-sum ladder (p_1,p_3 | p_2,p_4) "
      "plus the two Gaussian/D5 constants 13 = N(3+2i) and 8 = h(D5).")
raise SystemExit(0 if nfail == 0 else 1)
