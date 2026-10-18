#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""one_object_reduction_probe -- THE d = 4 FORCING CENSUS: are P1 and P2
two functors of ONE four-point boundary object?

CLAIM CHAIN UNDER TEST (frozen; see FROZEN_SPEC, SHA-256 printed BEFORE
any lattice data is computed): for a boundary divisor with d marked
points the cycle side gives A_{d-1} (N_fam = d-1 = rank H_1 of the
d-punctured P^1) and the function/carrier side gives D_{d+1}
(g_car = d+1).  The corpus already reads 3 and 5 this way at d = 4:

  * X_f deg 4 boundary: X_f^o ~= P^1 \\ mu_4, H_1 = Z^3, "hence A_3 and
    N_fam = 3" (tfpt_1_architecture_e8.tex ~L894, ~L4234);
  * g_car = rank D_5 = 5, q(D5) = g_car/|mu4|, q(A3) = N_fam/|mu4| with
    n+1 = 4 = |mu4| on the A-side (tfpt_1 ~L4201-4205);
  * |mu4| = (g_car + N_fam)/2 = 4 (tfpt_1 ~L4235, v53_compiler_core).

THE NEW FORCING ARGUMENT to verify exactly: disc(A_{d-1}) ~= Z_d, while
disc(D_{d+1}) is Z_4 for d+1 odd (d even) and Z_2 x Z_2 for d+1 even
(d odd).  The TFPT glue pattern (v1_e8_glue + v92_glue_uniqueness:
cyclic isotropic glue group, evenness q = 0 mod 2Z, unimodularity
|H|^2 = |disc A| * |disc D|) admits a DIAGONAL glue of
A_{d-1} (+) D_{d+1} iff Z_d ~= Z_4 with anti-isometric quadratic forms,
i.e. iff d = 4 -- yielding E8 = the D5 (+) A3 glue.  Any other d
admitting an even unimodular diagonal glue KILLS the forcing claim.

CENSUS: for d = 2..12 compute both discriminant groups and their
quadratic/linking forms EXACTLY from the Cartan matrices (Fraction
arithmetic, no floats), enumerate ALL subgroups of the direct-sum
discriminant form, and classify:
  * even unimodular glues      (Lagrangian, q = 0 mod 2Z)
  * ... of which DIAGONAL      (trivial intersection with both factors)
  * odd unimodular glues       (Lagrangian, q = 0 mod Z, b = 0 mod Z,
                                NOT even)          [control: evenness]
  * nontrivial even glues of ANY index              [control: unimod]

VERDICT ENUMS (frozen):
  ONE-OBJECT-FORCED  = glue census forces d = 4 AND the c_3 = 1/(2 pi d)
                       link is corpus-DERIVED from the boundary object.
                       Predeclared UNREACHABLE for this corpus snapshot:
                       P1 is a primitive postulate (tfpt_1 ~L169) whose
                       Gauss-Bonnet hardening 1/(|Z2| * 4 pi) reads the
                       "4 pi" as total sphere curvature, NOT as d
                       (tfpt_1 ~L670-689).
  ONE-OBJECT-PARTIAL = the glue census forces d = 4 exactly (controls
                       fire), corollary g_car = d+1 = 5 is verified
                       arithmetic, but the c_3 link stays INTERPRETIVE:
                       c_3 = 1/(2 e_1(a) pi) with e_1(a) = 4 = |mu4| IS
                       corpus-legitimate (tfpt_1 ~L189-194, v23
                       anchor-first refinement), so 1/(2 pi d)|_{d=4}
                       = 1/(8 pi) is a corpus-legitimate REWRITING --
                       but "the glue-forced d derives P1" would be a NEW
                       derivation, which this probe must NOT smuggle.
  ONE-OBJECT-DEAD    = some d != 4 admits an even unimodular diagonal
                       glue (the forcing claim dies), or d = 4 fails.
  TEST-VOID          = a corpus-reproduction gate fails (G2/G3) or a
                       must-fire control does not fire (G4/G5).

GATES (frozen before running):
  G1  d-table: {d in 2..12 admitting an even unimodular DIAGONAL glue}
      must be decided exactly; forcing holds iff it equals {4}.
  G2  at d = 4 the census must reproduce v92 EXACTLY: precisely TWO
      even Lagrangian glues, both diagonal cyclic Z4 -- the graphs of
      the two anti-isometries k -> k and k -> 3k.
  G3  explicit lattice certificate at d = 4 (v1 reproduction): gluing
      A3 (+) D5 by one such glue gives an even lattice with Gram det 1
      and EXACTLY 240 norm-2 vectors, all integral over the glued
      basis -- i.e. E8.
  G4  CONTROL (must fire): dropping evenness (isotropy mod Z only)
      opens at least one d != 4 (an odd unimodular glue exists there).
  G5  CONTROL (must fire): dropping unimodularity (any nontrivial even
      isotropic glue subgroup) opens at least one d != 4.
  G6  square obstruction layer: |H|^2 = 4d needs 4d to be a perfect
      square, i.e. d itself a square: only d in {4, 9} survive the
      coarse layer in 2..12; the census must show HOW d = 9 dies
      (no isotropic-even Lagrangian in Z9 (+) Z2 x Z2).
  G7  corollaries stated as verified arithmetic at the forced d:
      g_car = d+1 = 5, N_fam = d-1 = 3, rank = 2d = 8,
      glue index = sqrt(4d) = 4 = d = |mu4|; c_3 typing per the
      PARTIAL/FORCED rule above (honesty gate: interpretation label).

FIREWALL: experiments/tfpt-discovery probe; EXPLORATION ONLY; writes
nothing; touches no verification/, paper, ledger, changelog or website
surface; no marker moves; no physics claims.  ROOTCLASS-MIXED fence
(v775_gaussian_class_d5_purity): no code->matter semantics is used or
implied anywhere -- this census is pure lattice/discriminant-form
arithmetic.  A d != 4 hit is a valid, well-powered KILL and will be
reported honestly.

Sources (read-only): verification/v1_e8_glue.py (glue conditions +
lattice certificate pattern), v92_glue_uniqueness.py (Lagrangian
classification of Z4 x Z4, q = (5x^2+3y^2)/8 mod 1 in conformal-weight
normalization = half of our q mod 2Z), v53_compiler_core.py (atoms),
tfpt_1_architecture_e8.tex ~L160-194 (P1/P2, anchor-first refinement),
~L670-689 (Gauss-Bonnet hardening), ~L4190-4245 (glue norms as
compiler atoms), ~L894/4234 (H_1 = Z^3 reading).

Run:
    experiments/tfpt-discovery/.venv/bin/python \\
        experiments/tfpt-discovery/one_object_reduction_probe.py
"""

import hashlib
import itertools
import time
from fractions import Fraction as Fr

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ======================================================================
# S0: FROZEN SPEC -- hashed BEFORE any lattice data is computed
# ======================================================================
FROZEN_SPEC = """\
ONE-OBJECT REDUCTION FROZEN SPEC (one_object_reduction_probe)
frozen 2026-08-05, BEFORE computing any lattice data in this run.

CLAIM: the TFPT glue pattern (cyclic isotropic glue group, evenness
q = 0 mod 2Z, unimodularity |H|^2 = |disc|) admits an even unimodular
DIAGONAL glue of A_{d-1} (+) D_{d+1} iff d = 4; the boundary object
with d marks then forces g_car = d+1 = 5 and N_fam = d-1 = 3 as the
two functor readouts of ONE four-point object.

CENSUS RANGE: d = 2..12 inclusive.  All arithmetic exact (Fraction).
DIAGONAL glue := Lagrangian H with H int (A(+)0) = 0 = H int (0(+)D).
EVEN glue     := q(h) = 0 mod 2Z for all h in H.
UNIMODULAR    := |H|^2 = |disc(A_{d-1})| * |disc(D_{d+1})| = 4d.
ODD-relaxed   := q(h) = 0 mod Z and b(h,h') = 0 mod Z, not even.

VERDICT RULE (frozen):
  TEST-VOID          if G2 or G3 fails, or G4 or G5 does not fire;
  ONE-OBJECT-DEAD    if {d with even unimodular diagonal glue} != {4};
  ONE-OBJECT-PARTIAL otherwise.  ONE-OBJECT-FORCED is predeclared
  unreachable: the c_3 = 1/(2 pi d) link is a corpus-legitimate
  REWRITING (c_3 = 1/(2 e_1(a) pi), e_1(a) = 4 = |mu4| = d; tfpt_1
  ~L189-194, v23) but NOT a corpus derivation of P1 from the boundary
  object; this probe must not smuggle a new derivation of P1.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
section("S0: FROZEN SPEC (SHA-256 %s)" % SPEC_SHA)
print(FROZEN_SPEC)


# ======================================================================
# exact linear algebra helpers (Fractions, no floats anywhere)
# ======================================================================
def cartan_A(n):
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = 2
    for i in range(n - 1):
        M[i][i + 1] = M[i + 1][i] = -1
    return M


def cartan_D(n):
    """v1_e8_glue convention: A_n chain, detach last node, re-attach at
    the fork (n >= 3; D_3 ~= A_3)."""
    M = cartan_A(n)
    M[n - 2][n - 1] = M[n - 1][n - 2] = 0
    M[n - 3][n - 1] = M[n - 1][n - 3] = -1
    return M


def frac_inv(G):
    """exact matrix inverse via Gauss-Jordan."""
    n = len(G)
    A = [[Fr(G[i][j]) for j in range(n)] + [Fr(int(i == k)) for k in range(n)]
         for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [A[r][j] - f * A[c][j] for j in range(2 * n)]
    return [row[n:] for row in A]


def det_int(G):
    """exact integer determinant (fraction-free would be nicer; Fraction
    Gaussian elimination is exact and fine at n <= 11)."""
    n = len(G)
    A = [[Fr(G[i][j]) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            A[c], A[p] = A[p], A[c]
            det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / A[c][c]
                A[r] = [A[r][j] - f * A[c][j] for j in range(n)]
    assert det.denominator == 1
    return int(det)


def mod1(x):
    return x - (x.numerator // x.denominator)


def mod2(x):
    m = x % 2
    return m


class DiscForm(object):
    """discriminant group L*/L of an even lattice with Gram G, with the
    quadratic form q: A -> Q/2Z and linking form b: A x A -> Q/Z,
    computed exactly from the Cartan/Gram matrix."""

    def __init__(self, G):
        self.G = G
        self.n = len(G)
        Ginv = frac_inv(G)
        gens = [tuple(Ginv[i][j] for i in range(self.n))
                for j in range(self.n)]  # dual basis vectors, root coords
        # BFS closure of the generators mod Z^n
        elems = {tuple(Fr(0) for _ in range(self.n))}
        frontier = list(elems)
        while frontier:
            nxt = []
            for e in frontier:
                for g in gens:
                    s = tuple(mod1(a + b) for a, b in zip(e, g))
                    if s not in elems:
                        elems.add(s)
                        nxt.append(s)
            frontier = nxt
        self.elems = sorted(elems)
        self.index = {e: i for i, e in enumerate(self.elems)}
        self.zero = self.index[tuple(Fr(0) for _ in range(self.n))]
        m = len(self.elems)
        self.add = [[0] * m for _ in range(m)]
        for i, u in enumerate(self.elems):
            for j, v in enumerate(self.elems):
                self.add[i][j] = self.index[
                    tuple(mod1(a + b) for a, b in zip(u, v))]

    def q(self, i):
        v = self.elems[i]
        s = Fr(0)
        for a in range(self.n):
            for b in range(self.n):
                s += v[a] * self.G[a][b] * v[b]
        return mod2(s)

    def b(self, i, j):
        u, v = self.elems[i], self.elems[j]
        s = Fr(0)
        for a in range(self.n):
            for b in range(self.n):
                s += u[a] * self.G[a][b] * v[b]
        return mod1(s)

    def order_of(self, i):
        k, cur = 1, i
        while cur != self.zero:
            cur = self.add[cur][i]
            k += 1
        return k

    def structure(self):
        from collections import Counter
        return dict(Counter(self.order_of(i) for i in range(len(self.elems))))


class SumForm(object):
    """orthogonal direct sum of two DiscForms; elements are index pairs."""

    def __init__(self, A, D):
        self.A, self.D = A, D
        self.elems = [(i, j) for i in range(len(A.elems))
                      for j in range(len(D.elems))]
        self.index = {e: k for k, e in enumerate(self.elems)}
        self.zero = self.index[(A.zero, D.zero)]

    def add(self, x, y):
        (a1, d1), (a2, d2) = self.elems[x], self.elems[y]
        return self.index[(self.A.add[a1][a2], self.D.add[d1][d2])]

    def q(self, x):
        a, d = self.elems[x]
        return mod2(self.A.q(a) + self.D.q(d))

    def b(self, x, y):
        (a1, d1), (a2, d2) = self.elems[x], self.elems[y]
        return mod1(self.A.b(a1, a2) + self.D.b(d1, d2))

    def closure(self, gens):
        H = {self.zero}
        frontier = list(H)
        while frontier:
            nxt = []
            for h in frontier:
                for g in gens:
                    s = self.add(h, g)
                    if s not in H:
                        H.add(s)
                        nxt.append(s)
            frontier = nxt
        return frozenset(H)

    def all_subgroups(self):
        subs = {frozenset({self.zero})}
        work = [frozenset({self.zero})]
        while work:
            H = work.pop()
            for e in range(len(self.elems)):
                if e in H:
                    continue
                H2 = self.closure(list(H) + [e])
                if H2 not in subs:
                    subs.add(H2)
                    work.append(H2)
        return subs


def classify(d):
    """full glue census for A_{d-1} (+) D_{d+1}."""
    A = DiscForm(cartan_A(d - 1))
    D = DiscForm(cartan_D(d + 1))
    S = SumForm(A, D)
    total = len(S.elems)
    lag_order_sq = total  # |H|^2 == |A|*|D| condition on the order
    res = {
        "d": d,
        "discA": A.structure(),
        "discD": D.structure(),
        "orderA": len(A.elems),
        "orderD": len(D.elems),
        "square": int(round(total ** 0.5)) ** 2 == total,
        "even_unimod": [],
        "even_unimod_diagonal": [],
        "odd_unimod": [],
        "even_nontrivial_any": [],
    }
    for H in S.all_subgroups():
        hl = sorted(H)
        even = all(S.q(h) == 0 for h in hl)
        modZ = (all(S.q(h).denominator == 1 for h in hl)
                and all(S.b(x, y) == 0 for x in hl for y in hl))
        lag = len(H) * len(H) == lag_order_sq
        intA = sum(1 for h in hl if S.elems[h][1] == D.zero)
        intD = sum(1 for h in hl if S.elems[h][0] == A.zero)
        diagonal = (intA == 1 and intD == 1)  # only 0 in each factor
        if even and len(H) > 1:
            res["even_nontrivial_any"].append(H)
        if lag and even:
            res["even_unimod"].append(H)
            if diagonal:
                res["even_unimod_diagonal"].append(H)
        if lag and modZ and not even:
            res["odd_unimod"].append(H)
    return A, D, S, res


# ======================================================================
# S1: THE d-CENSUS 2..12
# ======================================================================
section("S1: the d-census (exact discriminant-form glue theory, d = 2..12)")

TABLE = {}
FORMS = {}
for d in range(2, 13):
    A, D, S, res = classify(d)
    FORMS[d] = (A, D, S)
    TABLE[d] = res
    print("  d=%2d  disc(A_%d)=%s (Z_%d)  disc(D_%d)=%s  4d=%2d square=%s  "
          "evenUnimod=%d (diag %d)  oddUnimod=%d  evenAnyIndex(nontriv)=%d"
          % (d, d - 1, res["discA"], res["orderA"], d + 1, res["discD"],
             4 * d, res["square"], len(res["even_unimod"]),
             len(res["even_unimod_diagonal"]), len(res["odd_unimod"]),
             len(res["even_nontrivial_any"])), flush=True)

# structural sanity: disc(A_{d-1}) = Z_d; disc(D_{d+1}) = Z4 (d even) /
# Z2xZ2 (d odd)
ok_A = all(TABLE[d]["orderA"] == d and max(TABLE[d]["discA"]) == d
           for d in range(2, 13))
ok_D = all(TABLE[d]["orderD"] == 4 and
           (max(TABLE[d]["discD"]) == (4 if d % 2 == 0 else 2))
           for d in range(2, 13))
check("S1.1 disc(A_{d-1}) ~= Z_d for all d (order d, cyclic)", ok_A)
check("S1.2 disc(D_{d+1}) ~= Z4 for d even, Z2 x Z2 for d odd (order 4)",
      ok_D)

forced_set = sorted(d for d in TABLE
                    if len(TABLE[d]["even_unimod_diagonal"]) > 0)
any_glue_set = sorted(d for d in TABLE if len(TABLE[d]["even_unimod"]) > 0)
g1 = check("S1.3 [G1] {d : even unimodular DIAGONAL glue exists} = %s "
           "(forcing claim needs exactly {4})" % forced_set,
           forced_set == [4])
check("S1.4 [G1+] even stronger: {d : ANY even unimodular glue exists} "
      "= %s (all glues at the forced d are diagonal)" % any_glue_set,
      any_glue_set == [4])

# G6: the coarse square layer
square_set = sorted(d for d in TABLE if TABLE[d]["square"])
check("S1.5 [G6] coarse layer: |H|^2 = 4d is a perfect square only for "
      "d in %s (d must itself be a square)" % square_set,
      square_set == [4, 9])
d9 = TABLE[9]
# how d = 9 dies: no even Lagrangian; exact reason: the order-2 part of
# any |H| = 6 subgroup must sit in disc(D_10) (Z9 has no 2-torsion) and
# no element of disc(D_10) has q = 0 mod 2Z.
D10 = FORMS[9][1]
d10_qvals = sorted(str(D10.q(i)) for i in range(len(D10.elems)))
check("S1.6 [G6] d = 9 dies at isotropy: 0 even Lagrangians; "
      "disc(D_10) q-values %s contain no 0 besides the origin -> the "
      "forced order-2 part of |H| = 6 cannot be even-isotropic"
      % d10_qvals,
      len(d9["even_unimod"]) == 0
      and all(D10.q(i) != 0 for i in range(len(D10.elems))
              if i != D10.zero))

# ======================================================================
# S2: G2 -- d = 4 must reproduce v92 EXACTLY
# ======================================================================
section("S2: [G2] d = 4 reproduces v92 (two diagonal Lagrangians, "
        "graphs of k -> k and k -> 3k)")

A4, D4, S4 = FORMS[4]
res4 = TABLE[4]
# corpus q-values: q(A3) = 3/4, q(D5) = 5/4 on primitive generators
qA_prim = sorted({str(A4.q(i)) for i in range(len(A4.elems))
                  if A4.order_of(i) == 4})
qD_prim = sorted({str(D4.q(i)) for i in range(len(D4.elems))
                  if D4.order_of(i) == 4})
check("S2.1 q on primitive generators: q(A3) = {3/4} mod 2Z, "
      "q(D5) = {5/4} mod 2Z (v1: 3/4 + 5/4 = 2 = E8 root norm)",
      qA_prim == ["3/4"] and qD_prim == ["5/4"],
      "qA %s qD %s" % (qA_prim, qD_prim))

lags = res4["even_unimod"]
check("S2.2 EXACTLY two even Lagrangian glues at d = 4 (v92: <(1,1)> "
      "and <(1,3)>), both diagonal, both cyclic Z4",
      len(lags) == 2 and len(res4["even_unimod_diagonal"]) == 2
      and all(max(len({h for h in H}), 0) == 4 for H in lags))

# graph check: each Lagrangian is the graph of an anti-isometry
# Z4 -> Z4; the two anti-isometries are k -> k and k -> 3k on suitable
# generators (equivalently: their intersection is {0, (2,2)})
a_gen = next(i for i in range(len(A4.elems)) if A4.order_of(i) == 4)
d_gen = next(i for i in range(len(D4.elems)) if D4.order_of(i) == 4)
d_gen3 = D4.add[D4.add[d_gen][d_gen]][d_gen]
exp1 = S4.closure([S4.index[(a_gen, d_gen)]])
exp2 = S4.closure([S4.index[(a_gen, d_gen3)]])
check("S2.3 the two Lagrangians ARE the graphs <(a, s)> and <(a, 3s)> "
      "for a fixed primitive pair (a, s) (v92's <(1,1)>, <(1,3)>)",
      {exp1, exp2} == set(lags))
inter = set(lags[0]) & set(lags[1])
check("S2.4 their intersection is the order-2 halfway glue "
      "{0, (2,2)} (v92's unique isotropic Z2 = the SO(16)_1 rung)",
      len(inter) == 2 and all(S4.q(h) == 0 for h in inter))

# ======================================================================
# S3: G3 -- explicit lattice certificate at d = 4 (v1 reproduction)
# ======================================================================
section("S3: [G3] explicit glue A3 (+) D5 + <(w1, s)> = E8 "
        "(240 roots, even, det 1)")

# orthonormal ambient R^4 (+) R^5; A3 = sum-zero integer vectors of Z^4,
# D5 = even-sum integer vectors of Z^5.
A3_basis = [(1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1)]
D5_basis = [(1, -1, 0, 0, 0), (0, 1, -1, 0, 0), (0, 0, 1, -1, 0),
            (0, 0, 0, 1, -1), (0, 0, 0, 1, 1)]
wA = (Fr(3, 4), Fr(-1, 4), Fr(-1, 4), Fr(-1, 4))       # A3 weight, q = 3/4
wD = (Fr(1, 2),) * 5                                    # D5 spinor, q = 5/4
glue = tuple(list(wA) + list(wD))                       # norm 2 = E8 root


def dot(u, v):
    return sum(Fr(a) * Fr(b) for a, b in zip(u, v))


check("S3.1 glue vector g = (w_A3, spinor_D5) has norm q(A3) + q(D5) "
      "= 3/4 + 5/4 = 2 (an E8 root already)",
      dot(wA, wA) == Fr(3, 4) and dot(wD, wD) == Fr(5, 4)
      and dot(glue, glue) == 2)

full9 = [tuple(list(b) + [0] * 5) for b in A3_basis] + \
        [tuple([0] * 4 + list(b)) for b in D5_basis]

# glued basis: replace one root vector by g so that the 8-set has det 1
best = None
for drop in range(8):
    basis = [full9[i] for i in range(8) if i != drop] + [glue]
    Gm = [[dot(u, v) for v in basis] for u in basis]
    dt = det_int([[int(x) if x.denominator == 1 else x for x in row]
                  for row in Gm]) if all(
        x.denominator == 1 for row in Gm for x in row) else None
    if dt is None:
        # Gram has half-integers off-diagonal? (g vs roots gives
        # integers here, but keep the exact fallback)
        n = len(basis)
        Af = [[Fr(Gm[i][j]) for j in range(n)] for i in range(n)]
        dtf = Fr(1)
        for c in range(n):
            p = next((r for r in range(c, n) if Af[r][c] != 0), None)
            if p is None:
                dtf = Fr(0)
                break
            if p != c:
                Af[c], Af[p] = Af[p], Af[c]
                dtf = -dtf
            dtf *= Af[c][c]
            for r in range(c + 1, n):
                if Af[r][c] != 0:
                    f = Af[r][c] / Af[c][c]
                    Af[r] = [Af[r][j] - f * Af[c][j] for j in range(n)]
        dt = dtf
    if dt == 1:
        even_diag = all(Gm[i][i] % 2 == 0 for i in range(8))
        integer = all(x.denominator == 1 for row in Gm for x in row)
        if even_diag and integer:
            best = (drop, basis, Gm)
            break
check("S3.2 glued basis found (drop root #%s, add g): Gram is integer, "
      "even diagonal, det = 1 -> even UNIMODULAR rank 8"
      % (best[0] if best else "-"), best is not None)

# count norm-2 vectors coset by coset: L' = L + Z g, L'/L = Z4
def coset_norm_counts(k, side):
    """multiset {norm: count} of vectors in k*w + lattice, norm <= 2."""
    if side == "A":
        w, dim = wA, 4
    else:
        w, dim = wD, 5
    counts = {}
    for m in itertools.product(range(-3, 4), repeat=dim):
        if side == "A" and sum(m) != 0:
            continue
        if side == "D" and sum(m) % 2 != 0:
            continue
        v = tuple(Fr(k) * w[i] + m[i] for i in range(dim))
        nrm = dot(v, v)
        if nrm <= 2:
            counts[nrm] = counts.get(nrm, 0) + 1
    return counts


root_total = 0
per_coset = []
for k in range(4):
    cA = coset_norm_counts(k, "A")
    cD = coset_norm_counts(k, "D")
    n_k = sum(cA[na] * cD[nd] for na in cA for nd in cD if na + nd == 2)
    per_coset.append(n_k)
    root_total += n_k
check("S3.3 norm-2 count per glue coset k = 0..3: %s, total = %d "
      "(v1: A3+D5 roots 12+40 = 52 in k = 0; glued total must be 240)"
      % (per_coset, root_total),
      per_coset[0] == 52 and root_total == 240)

# integrality of all 240 roots over the glued basis
if best:
    _, basis, Gm = best
    Ginv8 = frac_inv([[Fr(x) for x in row] for row in Gm])
    roots_all = []
    for k in range(4):
        for mA in itertools.product(range(-3, 4), repeat=4):
            if sum(mA) != 0:
                continue
            vA = tuple(Fr(k) * wA[i] + mA[i] for i in range(4))
            nA = dot(vA, vA)
            if nA > 2:
                continue
            for mD in itertools.product(range(-3, 4), repeat=5):
                if sum(mD) % 2 != 0:
                    continue
                vD = tuple(Fr(k) * wD[i] + mD[i] for i in range(5))
                if nA + dot(vD, vD) == 2:
                    roots_all.append(tuple(list(vA) + list(vD)))
    integral = True
    for r in roots_all:
        proj = [dot(r, bv) for bv in basis]
        coef = [sum(Ginv8[i][j] * proj[j] for j in range(8))
                for i in range(8)]
        if not all(c.denominator == 1 for c in coef):
            integral = False
            break
    check("S3.4 all %d enumerated norm-2 vectors are INTEGRAL over the "
          "glued basis: the glue closes to THE even unimodular E8 "
          "lattice (v1 certificate reproduced)" % len(roots_all),
          integral and len(roots_all) == 240)

# ======================================================================
# S4: CONTROLS G4 / G5 -- the constraints must BIND
# ======================================================================
section("S4: controls -- relaxing evenness/unimodularity must open "
        "other d (must fire)")

odd_set = sorted(d for d in TABLE if d != 4 and len(TABLE[d]["odd_unimod"]))
g4 = check("S4.1 [G4, must fire] dropping EVENNESS opens d in %s "
           "(odd unimodular glues exist there; e.g. d = 9: "
           "A8 (+) D10 + <(3,0),(0,v)> is an ODD unimodular rank-18 "
           "glue)" % odd_set, len(odd_set) > 0)

sub_set = sorted(d for d in TABLE
                 if d != 4 and len(TABLE[d]["even_nontrivial_any"]))
g5 = check("S4.2 [G5, must fire] dropping UNIMODULARITY opens d in %s "
           "(nontrivial even isotropic glue subgroups of smaller index "
           "exist there)" % sub_set, len(sub_set) > 0)

check("S4.3 the intermediate at d = 4 itself: exactly one nontrivial "
      "even isotropic subgroup BELOW the Lagrangians (v92's halfway "
      "SO(16)_1 rung, |H| = 2)",
      sum(1 for H in TABLE[4]["even_nontrivial_any"] if len(H) == 2) == 1)

# ======================================================================
# S5: [G7] corollaries at the forced d -- typed honestly
# ======================================================================
section("S5: [G7] corollaries at the forced d = 4 (typed)")

d_star = forced_set[0] if len(forced_set) == 1 else None
if d_star is not None:
    check("S5.1 [verified arithmetic] g_car = d+1 = %d, N_fam = d-1 = %d, "
          "rank = 2d = %d, glue index = sqrt(4d) = %d = d = |mu4|"
          % (d_star + 1, d_star - 1, 2 * d_star,
             int(round((4 * d_star) ** 0.5))),
          d_star + 1 == 5 and d_star - 1 == 3 and 2 * d_star == 8
          and int(round((4 * d_star) ** 0.5)) == 4)
    check("S5.2 [corpus-anchored] N_fam = d-1 = rank H_1(P^1 minus d "
          "points) = 3 (tfpt_1 ~L894/4234: H_1 = Z^3 hence A_3); "
          "q(A3) = N_fam/|mu4|, q(D5) = g_car/|mu4| with n+1 = 4 = "
          "|mu4| = d (tfpt_1 ~L4201-4205)", d_star == 4)
    # the c3 honesty gate: arithmetic identity is [E]-grade, the LINK is
    # an interpretation -- frozen in the spec, restated here.
    c3_arith = Fr(1, 2 * d_star) # times 1/pi: 1/(2 pi d) = 1/(8 pi)
    check("S5.3 [verified arithmetic] 1/(2 pi d)|_{d=4} = 1/(8 pi): "
          "coefficient 1/(2d) = %s = 1/8" % c3_arith,
          c3_arith == Fr(1, 8))
    check("S5.4 [HONESTY GATE -- interpretation, NOT derivation] the "
          "1/(2 pi d) READING of P1 is corpus-legitimate only as a "
          "rewriting: c_3 = 1/(2 e_1(a) pi) with e_1(a) = 4 = |mu4| "
          "(tfpt_1 ~L189-194, v23 anchor-first refinement) and "
          "|mu4| = #marks = d; but the corpus derivation chain of P1 "
          "is Gauss-Bonnet 1/(|Z2| * oint K dA) = 1/(2 * 4 pi) where "
          "4 pi is TOTAL SPHERE CURVATURE, not d (tfpt_1 ~L670-689); "
          "P1 status: primitive postulate (tfpt_1 ~L169).  The glue "
          "census therefore does NOT derive P1; the c_3 link is typed "
          "INTERPRETATION", True)

# ======================================================================
# S6: VERDICT (frozen rule)
# ======================================================================
section("S6: VERDICT (frozen enum: ONE-OBJECT-FORCED / ONE-OBJECT-"
        "PARTIAL / ONE-OBJECT-DEAD / TEST-VOID)")

g2_ok = all(ok for name, ok in CHECKS if name.startswith("S2."))
g3_ok = all(ok for name, ok in CHECKS if name.startswith("S3."))
controls_fire = g4 and g5
if not (g2_ok and g3_ok and controls_fire):
    VERDICT = "TEST-VOID"
elif forced_set != [4]:
    VERDICT = "ONE-OBJECT-DEAD"
else:
    VERDICT = "ONE-OBJECT-PARTIAL"

print("VERDICT: %s" % VERDICT)
print("  glue-forced d set: %s (needed {4})" % forced_set)
print("  c_3 link: corpus-legitimate rewriting via e_1(a) = |mu4| = d "
      "(tfpt_1 ~L192), typed INTERPRETATION -- FORCED predeclared "
      "unreachable")
print("  controls: evenness relaxation opens %s, unimodularity "
      "relaxation opens %s" % (odd_set, sub_set))

n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else
      "SOME CHECKS FAILED")
