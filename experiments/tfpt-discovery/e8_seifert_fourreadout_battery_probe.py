#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""e8_seifert_fourreadout_battery_probe -- internal E8 consistency battery

FROZEN SPEC v1 (2026-09-02).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.
Deterministic (no randomness).  Pure mathematics of E8; no TFPT
physics input.

=======================================================================
MANDATE
=======================================================================
From ONE integer object -- the Euler/Seifert matrix S of an oriented
E8 Dynkin quiver -- derive four classical readouts and gate them:
  (i)   Cartan matrix A = S+S^T and Coxeter element C = -S^{-1} S^T
        with charpoly Phi_30, order 30, Y = C+C^{-1} of degree 4;
  (ii)  240 roots via Construction A of the extended Hamming code H8
        and their inner-product / line-graph statistics;
  (iii) shell counts N(n) = 240 sigma_3(n) and the harmonic degree-8
        weighted theta = Ramanujan tau;
  (iv)  eight Dirichlet-character channels mod 30 with
        D_chi(s) = L(s,chi) L(s-3,chi).
No physics claim.  No c3, g_car, phi0.

=======================================================================
CONSTRUCTIONS
=======================================================================
S1  Bourbaki E8 edges (1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4).
    S = I with S[a-1,b-1] = -1 for each oriented edge a->b.
    A = S+S^T (diag 2, det 1).  C = -S^{-1} S^T.
    charpoly(C) = x^8+x^7-x^5-x^4-x^3+x+1 = Phi_30(x).
    C^30 = I.  Eigenvalue arguments 12,84,132,156 deg (and conjugates).
    Y = C+C^{-1} satisfies Y^4+Y^3-4Y^2-4Y+I = 0;
    minpoly(2cos(2pi/30)) = x^4+x^3-4x^2-4x+1.
    Orientation gate: reverse-all and bipartite-alternate orientations
    give conjugate Coxeter elements (same charpoly).  For a tree, all
    orientations give conjugate C because Phi_30 is irreducible of
    degree 8, so one similarity class over Q; S-S^T carries no
    conjugacy-invariant information.

S2  H8 generator rows
      [1,1,1,1,0,0,0,0], [0,0,1,1,1,1,0,0],
      [0,0,0,0,1,1,1,1], [0,1,0,1,0,1,0,1].
    Weight enumerator 1+14 y^4+y^8.  The 14 weight-4 words are the
    14 affine 2-flats of F_2^3 (coordinate i <-> binary of i; 7
    directions x 2).  Roots: (+-2 e_i)/sqrt(2) (16) and
    (+-1 on a weight-4 support)/sqrt(2) (14 x 16 = 224); all norm 2.
    Inner products vs a fixed root: {2:1, 1:56, 0:126, -1:56, -2:1}.
    120 antipodal lines, classes {|ip|=2:1, 1:56, 0:63}.
    Adjacency |ip|=1: degree 56, spectrum {56:1, 8:35, -4:84}
    (srg(120,56,28,24)).  A simple system from a generic linear
    functional has Gram equal to A up to permutation (det, charpoly,
    Dynkin diagram).

S3  E8 as D8^+ = {v in Z^8 : sum even} union
    {v in (Z+1/2)^8 : sum even}.  N(n) = #{|x|^2 = 2n} = 240 sigma_3(n)
    for n=1..8.  Hecke: N(mn)=N(m)N(n)/240 for coprime pairs.
    Log-derivative: Dirichlet coefficients of -D'/D with
    D = sum sigma_3(n) n^{-s} equal Lambda(n)(1+n^3) for n<=30.
    Harmonic zonal P(x) = |x|^8 C_8^{(3)}(x_1/|x|); ratios
    A_P(n)/A_P(1) = tau(n) for n=1..8 (rel 1e-6).
    7-design: shell sums of harmonic zonals of degree 2,4,6 vanish
    for n=1..4 (|sum| < 1e-8 relative to sum |P|).
    Second harmonic P2 = Re((x_1+i x_2)^8) yields the same tau ratios.

S4  (Z/30)^x = {1,7,11,13,17,19,23,29} ≅ C2 x C4; element orders
    {1,2,2,2,4,4,4,4}.  Characters = products of (Z/3)^x (order 2)
    and (Z/5)^x (order 4, generator 2).  Ordered by
    (log2 of mod-3 part) x (dlog2 of mod-5 part), the character
    table IS H_2 ⊗ F_4.  Convolution: chi(n) sigma_3(n) =
    sum_{d|n} chi(d) chi(n/d) (n/d)^3 for n<=60 (all 8 chi).

S5  Exponents {1,7,11,13,17,19,23,29} = units mod 30, sum 120.
    2m+1 -> {3,15,23,27,35,39,47,59} sum 248.
    Affine marks {1,2,3,4,5,6,4,2,3} sum 30, sum of squares 120.
    Brieskorn (15a+10b+6c) mod 30 for a=1, b in {1,2}, c in {1..4}
    = units mod 30.  1/2+1/3+1/5-1 = 1/30.
    Tr(C^k) = c_30(k) (Ramanujan sum) for k=1..30.

=======================================================================
GATES / VERDICT
=======================================================================
Gates are the S1--S5 checks named below.  Verdict enum frozen:
  FOUR_READOUTS_FROM_ONE_OBJECT  if every gate passes;
  BATTERY_INCOMPLETE(list)       otherwise.
Honest scope: pure mathematics of E8 (Construction A, Coxeter theory,
modular forms); no TFPT-specific physics input (c3, g_car, phi0)
enters; not a claim.
"""

import hashlib
import itertools
import math
import sys
from collections import Counter
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.special import eval_gegenbauer

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

CHECKS = []

UNITS30 = (1, 7, 11, 13, 17, 19, 23, 29)
EDGES_FWD = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
H8_GEN = (
    (1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 1, 1, 1, 1, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1),
    (0, 1, 0, 1, 0, 1, 0, 1),
)
TAU = (1, -24, 252, -1472, 4830, -6048, -16744, 84480)
MARKS = (1, 2, 3, 4, 5, 6, 4, 2, 3)
N_EXPECT = (240, 2160, 6720, 17520, 30240, 60480, 82560, 140400)


def gate(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))


def section(title):
    print("\n" + title)
    print("-" * len(title))


def seifert(edges):
    S = sp.eye(8)
    for a, b in edges:
        S[a - 1, b - 1] = -1
    return S


def fmt_mat(M):
    lines = []
    for i in range(8):
        lines.append("[" + " ".join("%2d" % int(M[i, j]) for j in range(8))
                     + "]")
    return "\n    ".join(lines)


def sigma3(n):
    s = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            s += d ** 3
            q = n // d
            if q != d:
                s += q ** 3
        d += 1
    return s


def divisors(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            q = n // d
            if q != d:
                out.append(q)
        d += 1
    return out


def von_mangoldt(n):
    if n < 2:
        return 0.0
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
        p += 1 if p == 2 else 2
    return math.log(n)


def ramanujan_c(n, k):
    d = math.gcd(k, n)
    nd = n // d
    return int(sp.mobius(nd) * sp.totient(n) // sp.totient(nd))


def mul_order(a, n=30):
    x = 1
    for k in range(1, n + 1):
        x = (x * a) % n
        if x == 1:
            return k
    return None


def disc_log3(n):
    return {1: 0, 2: 1}[n % 3]


def disc_log5(n):
    return {1: 0, 2: 1, 4: 2, 3: 3}[n % 5]


def chi_ab(a, b, n):
    if math.gcd(n, 30) != 1:
        return 0j
    return ((-1) ** (a * disc_log3(n))) * ((1j) ** (b * disc_log5(n)))


def crt_unit(alpha, beta):
    a3 = pow(2, alpha, 3)
    b5 = pow(2, beta, 5)
    for n in UNITS30:
        if n % 3 == a3 and n % 5 == b5:
            return n
    raise RuntimeError("no unit for (%s,%s)" % (alpha, beta))


def affine_2flats():
    vecs = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    subs = []
    seen = set()
    for i, u in enumerate(vecs):
        if u == (0, 0, 0):
            continue
        for w in vecs[i + 1:]:
            if w == (0, 0, 0):
                continue
            par = (u[0] * w[1] == u[1] * w[0]
                   and u[0] * w[2] == u[2] * w[0]
                   and u[1] * w[2] == u[2] * w[1])
            if par:
                continue
            span = set()
            for au in (0, 1):
                for aw in (0, 1):
                    span.add(tuple((au * u[k] + aw * w[k]) % 2
                                   for k in range(3)))
            if len(span) == 4:
                fs = frozenset(span)
                if fs not in seen:
                    seen.add(fs)
                    subs.append(fs)
    flats = []
    for V in subs:
        flats.append(V)
        t = next(v for v in vecs if v not in V)
        flats.append(frozenset(tuple((p[k] + t[k]) % 2 for k in range(3))
                               for p in V))
    return subs, flats


def idx_of(p):
    return p[0] + 2 * p[1] + 4 * p[2]


def bourbaki_perm(G):
    adj = (np.array(G, dtype=int) == -1)
    deg = adj.sum(axis=1)
    if sorted(int(d) for d in deg) != [1, 1, 1, 2, 2, 2, 2, 3]:
        return None
    branch = int(np.flatnonzero(deg == 3)[0])
    nbrs = [int(x) for x in np.flatnonzero(adj[branch])]

    def walk(start, prev):
        path = [start]
        cur, pr = start, prev
        while True:
            nxt = [int(x) for x in np.flatnonzero(adj[cur]) if x != pr]
            if len(nxt) != 1:
                return path
            pr, cur = cur, nxt[0]
            path.append(cur)

    arms = sorted((walk(nb, branch) for nb in nbrs), key=len)
    if [len(a) for a in arms] != [1, 2, 4]:
        return None
    p = [None] * 8
    p[3] = branch
    p[1] = arms[0][0]
    p[2] = arms[1][0]
    p[0] = arms[1][1]
    p[4], p[5], p[6], p[7] = arms[2]
    return p


def enumerate_d8plus(n_max, store_max):
    counts = {}
    stored = {}
    for n in range(1, n_max + 1):
        vecs = []
        target = 2 * n
        max_abs = int(math.sqrt(target) + 1e-12)
        for combo in itertools.combinations_with_replacement(
                range(0, max_abs + 1), 8):
            if sum(a * a for a in combo) != target:
                continue
            for perm in set(itertools.permutations(combo)):
                nz = [i for i, a in enumerate(perm) if a]
                for sgn in itertools.product((-1, 1), repeat=len(nz)):
                    v = [perm[i] for i in range(8)]
                    for i, s in zip(nz, sgn):
                        v[i] *= s
                    if sum(v) % 2 == 0:
                        vecs.append(tuple(float(x) for x in v))
        target_m = 8 * n
        max_odd = int(math.sqrt(target_m) + 1e-12)
        if max_odd % 2 == 0:
            max_odd -= 1
        odds = range(1, max_odd + 1, 2)
        for combo in itertools.combinations_with_replacement(odds, 8):
            if sum(a * a for a in combo) != target_m:
                continue
            for perm in set(itertools.permutations(combo)):
                for sgn in itertools.product((-1, 1), repeat=8):
                    m = [s * a for s, a in zip(sgn, perm)]
                    if sum(m) % 4 == 0:
                        vecs.append(tuple(x / 2.0 for x in m))
        counts[n] = len(vecs)
        if n <= store_max:
            stored[n] = np.asarray(vecs, dtype=np.float64)
    return counts, stored


def zonal_sum(shell, degree):
    r2 = np.sum(shell * shell, axis=1)
    r = np.sqrt(r2)
    t = shell[:, 0] / r
    p = (r ** degree) * eval_gegenbauer(degree, 3.0, t)
    return float(np.sum(p)), float(np.sum(np.abs(p)))


def rez8_sum(shell):
    z = shell[:, 0] + 1j * shell[:, 1]
    p = np.real(z ** 8)
    return float(np.sum(p)), float(np.sum(np.abs(p)))


def main():
    x = sp.symbols("x")
    phi30 = sp.Poly(sp.cyclotomic_poly(30, x), x)
    expected_phi = sp.Poly(
        x ** 8 + x ** 7 - x ** 5 - x ** 4 - x ** 3 + x + 1, x)
    minpoly_cos = sp.Poly(sp.minpoly(2 * sp.cos(2 * sp.pi / 30), x), x)
    expected_min = sp.Poly(x ** 4 + x ** 3 - 4 * x ** 2 - 4 * x + 1, x)

    # ------------------------------------------------------------------ S1
    section("S1  Seifert -> Cartan / Coxeter")
    S = seifert(EDGES_FWD)
    A = S + S.T
    diag2 = all(A[i, i] == 2 for i in range(8))
    detA = A.det()
    C = sp.simplify(-S.inv() * S.T)
    cp = sp.Poly(C.charpoly(x).as_expr(), x)
    c30 = sp.simplify(C ** 30)
    ev = np.linalg.eigvals(np.array(C, dtype=np.float64))
    angs = np.sort(np.mod(np.degrees(np.angle(ev)), 360.0))
    angs_r = tuple(int(round(a)) % 360 for a in angs)
    angs_r = tuple(0 if a == 360 else a for a in angs_r)
    expect_angs = tuple(sorted((12 * m) % 360 for m in UNITS30))
    acute = tuple(a for a in angs_r if 0 < a < 180)
    Y = sp.simplify(C + C.inv())
    Yrel = sp.simplify(Y ** 4 + Y ** 3 - 4 * Y ** 2 - 4 * Y + sp.eye(8))

    S_rev = seifert(tuple((b, a) for a, b in EDGES_FWD))
    C_rev = sp.simplify(-S_rev.inv() * S_rev.T)
    cp_rev = sp.Poly(C_rev.charpoly(x).as_expr(), x)
    # bipartite alternate: parts {1,4,6,8} -> {2,3,5,7}
    edges_alt = ((1, 3), (4, 3), (4, 2), (4, 5), (6, 5), (6, 7), (8, 7))
    S_alt = seifert(edges_alt)
    C_alt = sp.simplify(-S_alt.inv() * S_alt.T)
    cp_alt = sp.Poly(C_alt.charpoly(x).as_expr(), x)
    skew_fwd = sp.simplify(S - S.T)
    skew_alt = sp.simplify(S_alt - S_alt.T)
    rk_fwd = int(skew_fwd.rank())
    rk_alt = int(skew_alt.rank())
    C_inv = sp.simplify(C.inv())

    print("  charpoly(C) =", cp.as_expr())
    print("  Phi_30      =", phi30.as_expr())
    print("  eigenvalue arguments (deg):", angs_r)
    print("  acute arguments:", acute)
    print("  charpoly(C_fwd) == charpoly(C_rev) == Phi_30:",
          cp == cp_rev == phi30)
    print("  charpoly(C_alt) == Phi_30:", cp_alt == phi30)
    print("  C_rev == C^{-1}:", C_rev == C_inv)
    print("  for a tree all orientations give conjugate C")
    print("  (Phi_30 irreducible of deg 8 => one similarity class over Q;")
    print("   S-S^T carries no conjugacy-invariant information)")
    print("  S_fwd - S_fwd^T, rank %d =" % rk_fwd)
    print("    " + fmt_mat(skew_fwd))
    print("  S_alt - S_alt^T, rank %d =" % rk_alt)
    print("    " + fmt_mat(skew_alt))

    gate("S1-Cartan A=S+S^T diag 2 det 1",
         diag2 and detA == 1, "det=%s" % detA)
    gate("S1-Phi_30 charpoly(C)=cyclotomic_poly(30)",
         cp == phi30 == expected_phi)
    gate("S1-C^30=I", c30 == sp.eye(8))
    gate("S1-eigenvalue arguments 12,84,132,156 deg",
         angs_r == expect_angs and acute == (12, 84, 132, 156))
    gate("S1-Y^4+Y^3-4Y^2-4Y+I=0", Yrel == sp.zeros(8))
    gate("S1-minpoly(2cos(2pi/30))", minpoly_cos == expected_min)
    gate("S1-orientation conjugacy (rev, alt share Phi_30)",
         cp == cp_rev == cp_alt == phi30)

    # ------------------------------------------------------------------ S2
    section("S2  H8 Construction A -> roots / statistics")
    gen = np.array(H8_GEN, dtype=int)
    code = []
    for bits in itertools.product((0, 1), repeat=4):
        code.append(tuple(int(x) % 2 for x in np.dot(bits, gen)))
    code = sorted(set(code))
    wdist = Counter(sum(c) for c in code)
    wt4 = [c for c in code if sum(c) == 4]
    subs, flats = affine_2flats()
    flat_words = []
    for F in flats:
        w = [0] * 8
        for p in F:
            w[idx_of(p)] = 1
        flat_words.append(tuple(w))
    flat_set = set(flat_words)
    wt4_set = set(wt4)

    int_roots = []
    for i in range(8):
        v = [0] * 8
        v[i] = 2
        int_roots.append(tuple(v))
        v = [0] * 8
        v[i] = -2
        int_roots.append(tuple(v))
    for word in wt4:
        supp = [i for i in range(8) if word[i]]
        for sgn in itertools.product((-1, 1), repeat=4):
            v = [0] * 8
            for i, s in zip(supp, sgn):
                v[i] = s
            int_roots.append(tuple(v))
    norms = [sum(a * a for a in v) for v in int_roots]
    n_pm2 = 16
    n_wt4 = len(int_roots) - 16

    fixed = int_roots[0]
    ip_scaled = Counter(sum(a * b for a, b in zip(fixed, v)) // 2
                        for v in int_roots)

    def line_rep(v):
        nv = tuple(-x for x in v)
        return v if v > nv else nv

    lines = sorted(set(line_rep(v) for v in int_roots))
    ip_lines = Counter(abs(sum(a * b for a, b in zip(lines[0], w)) // 2)
                       for w in lines)

    nL = len(lines)
    Adj = np.zeros((nL, nL), dtype=np.float64)
    for i in range(nL):
        for j in range(i + 1, nL):
            ip = abs(sum(a * b for a, b in zip(lines[i], lines[j])))
            if ip == 2:
                Adj[i, j] = Adj[j, i] = 1.0
    deg = int(round(Adj.sum(axis=1).mean())) if nL else -1
    degs = Adj.sum(axis=1)
    spec = Counter(int(round(e)) for e in np.linalg.eigvalsh(Adj))
    A2 = Adj.dot(Adj)
    lam_ok = True
    mu_ok = True
    for i in range(nL):
        for j in range(i + 1, nL):
            c = A2[i, j]
            if Adj[i, j] == 1.0:
                lam_ok &= abs(c - 28.0) < 1e-8
            else:
                mu_ok &= abs(c - 24.0) < 1e-8

    wfun = np.array([1.0, math.e, math.pi, math.sqrt(2.0), math.sqrt(3.0),
                     math.sqrt(5.0), math.sqrt(7.0), math.sqrt(11.0)])
    dots = np.array([float(np.dot(v, wfun)) for v in int_roots])
    pos = [v for v, d in zip(int_roots, dots) if d > 0.0]
    pos_set = set(pos)
    simple = []
    for a in pos:
        dec = False
        for b in pos:
            if b is a:
                continue
            ip = sum(x * y for x, y in zip(a, b))
            if ip == 2:
                diff = tuple(x - y for x, y in zip(a, b))
                if diff in pos_set:
                    dec = True
                    break
        if not dec:
            simple.append(a)
    gram = None
    gram_match = False
    det_char = False
    if len(simple) == 8:
        gram = np.array([[sum(a * b for a, b in zip(simple[i], simple[j])) / 2.0
                          for j in range(8)] for i in range(8)])
        Gint = np.rint(gram).astype(int)
        p = bourbaki_perm(Gint)
        A_np = np.array(A, dtype=int)
        if p is not None:
            Gp = np.array([[Gint[p[i], p[j]] for j in range(8)]
                           for i in range(8)])
            gram_match = np.array_equal(Gp, A_np)
        det_char = (int(round(np.linalg.det(gram))) == 1
                    and np.allclose(sorted(np.linalg.eigvalsh(gram)),
                                    sorted(np.linalg.eigvalsh(A_np.astype(float))),
                                    atol=1e-8))

    print("  |H8|=%d  weight enumerator: 1 + %d y^4 + %d y^8"
          % (len(code), wdist[4], wdist[8]))
    print("  affine 2-flats: %d subspaces (directions), %d flats"
          % (len(subs), len(set(flats))))
    print("  roots: %d  (pm2e_i %d, wt4-signs %d)  norms %s"
          % (len(int_roots), n_pm2, n_wt4, sorted(set(norms))))
    print("  ip vs fixed root:", dict(sorted(ip_scaled.items())))
    print("  lines %d  |ip| classes:" % nL, dict(sorted(ip_lines.items())))
    print("  line-graph degree %d  spectrum %s" % (deg, dict(sorted(spec.items()))))
    print("  simple roots %d  Gram==Cartan (perm): %s  det+charpoly: %s"
          % (len(simple), gram_match, det_char))

    gate("S2-weight enumerator 1+14 y^4+y^8",
         len(code) == 16 and wdist == Counter({0: 1, 4: 14, 8: 1}))
    gate("S2-14 wt-4 words = 14 affine 2-flats (7 dirs x 2)",
         len(subs) == 7 and len(set(flats)) == 14 and flat_set == wt4_set)
    gate("S2-240 roots all integer-norm 4 (= Euclidean 2)",
         len(int_roots) == 240 and set(norms) == {4}
         and n_pm2 == 16 and n_wt4 == 224)
    gate("S2-inner products {2:1, 1:56, 0:126, -1:56, -2:1}",
         dict(ip_scaled) == {2: 1, 1: 56, 0: 126, -1: 56, -2: 1})
    gate("S2-120 lines {|ip|=2:1, 1:56, 0:63}",
         nL == 120 and dict(ip_lines) == {2: 1, 1: 56, 0: 63})
    gate("S2-srg(120,56,28,24) spectrum {56:1, 8:35, -4:84}",
         deg == 56 and dict(spec) == {56: 1, 8: 35, -4: 84}
         and lam_ok and mu_ok and np.allclose(degs, 56.0))
    gate("S2-simple-system Gram = Cartan (perm / det+charpoly)",
         gram_match or det_char)

    # ------------------------------------------------------------------ S3
    section("S3  theta: N(n), Hecke, log-derivative, 7-design, tau")
    counts, shells = enumerate_d8plus(n_max=12, store_max=8)
    n_ok = all(counts[n] == N_EXPECT[n - 1] == 240 * sigma3(n)
               for n in range(1, 9))
    print("  N(n) n=1..8:", [counts[n] for n in range(1, 9)])
    print("  240 sigma_3(n):", [240 * sigma3(n) for n in range(1, 9)])

    hecke_pairs = ((2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (3, 8), (5, 7))
    hecke_ok = True
    hecke_report = []
    for m, n in hecke_pairs:
        lhs = counts.get(m * n)
        if lhs is None:
            lhs = 240 * sigma3(m * n)
            src = "240*sigma3"
        else:
            src = "enum"
        rhs = counts[m] * counts[n] / 240.0
        ok = abs(lhs - rhs) < 1e-9
        hecke_ok &= ok
        hecke_report.append("(%d,%d)->%d %s %d vs %.1f" % (
            m, n, m * n, src, lhs, rhs))
    print("  Hecke:", "; ".join(hecke_report))

    logd_ok = True
    a = [0] + [sigma3(n) for n in range(1, 31)]
    ccoeff = [0.0] * 31
    for n in range(1, 31):
        rhs = a[n] * math.log(n) if n > 1 else 0.0
        for d in range(1, n):
            if n % d == 0:
                rhs -= ccoeff[d] * a[n // d]
        ccoeff[n] = rhs
        target = von_mangoldt(n) * (1.0 + n ** 3)
        if abs(ccoeff[n] - target) > 1e-8 * max(1.0, abs(target)):
            logd_ok = False
    print("  log-derivative n<=30 matches Lambda(n)(1+n^3):", logd_ok)

    tau_z = []
    ap1, _ = zonal_sum(shells[1], 8)
    z_ok = ap1 != 0.0
    for n in range(1, 9):
        ap, _ = zonal_sum(shells[n], 8)
        ratio = ap / ap1 if ap1 != 0.0 else float("nan")
        tau_z.append(ratio)
        rel = abs(ratio - TAU[n - 1]) / max(1.0, abs(TAU[n - 1]))
        z_ok &= rel < 1e-6
    print("  tau zonal  :", ", ".join("%.6f" % r for r in tau_z))

    design_ok = True
    for deg in (2, 4, 6):
        for n in range(1, 5):
            sm, ab = zonal_sum(shells[n], deg)
            rel = abs(sm) / max(ab, 1e-30)
            design_ok &= rel < 1e-8
            if rel >= 1e-8:
                print("  7-design FAIL deg %d n %d rel %.3e" % (deg, n, rel))
    print("  7-design deg 2,4,6 n=1..4 vanish:", design_ok)

    tau_2 = []
    bp1, _ = rez8_sum(shells[1])
    r_ok = bp1 != 0.0
    for n in range(1, 9):
        bp, _ = rez8_sum(shells[n])
        ratio = bp / bp1 if bp1 != 0.0 else float("nan")
        tau_2.append(ratio)
        rel = abs(ratio - TAU[n - 1]) / max(1.0, abs(TAU[n - 1]))
        r_ok &= rel < 1e-6
    print("  tau Re(z^8):", ", ".join("%.6f" % r for r in tau_2))
    print("  A_P(1) zonal=%.6g  Re(z^8)=%.6g" % (ap1, bp1))

    gate("S3-N(n)=240 sigma_3(n) n=1..8", n_ok)
    gate("S3-Hecke N(mn)=N(m)N(n)/240 coprime", hecke_ok)
    gate("S3-log-derivative -D'/D = Lambda(n)(1+n^3) n<=30", logd_ok)
    gate("S3-tau from zonal Gegenbauer C_8^{(3)}", z_ok,
         " ".join("%.6f" % r for r in tau_z))
    gate("S3-7-design zonal deg 2,4,6 vanish n=1..4", design_ok)
    gate("S3-tau from Re((x1+i x2)^8)", r_ok,
         " ".join("%.6f" % r for r in tau_2))

    # ------------------------------------------------------------------ S4
    section("S4  characters mod 30")
    orders = tuple(mul_order(u) for u in UNITS30)
    order_ctr = Counter(orders)
    print("  units:", UNITS30)
    print("  orders of 1,7,11,13,17,19,23,29:", orders)
    print("  order multiset:", dict(sorted(order_ctr.items())))

    H2 = np.array([[1.0, 1.0], [1.0, -1.0]], dtype=np.complex128)
    F4 = np.array([[(1j) ** (b * beta) for beta in range(4)]
                   for b in range(4)], dtype=np.complex128)
    kron = np.kron(H2, F4)
    table = np.zeros((8, 8), dtype=np.complex128)
    col_elts = []
    for alpha in range(2):
        for beta in range(4):
            col_elts.append(crt_unit(alpha, beta))
    row = 0
    for a in range(2):
        for b in range(4):
            for col, n in enumerate(col_elts):
                table[row, col] = chi_ab(a, b, n)
            row += 1
    kron_ok = np.allclose(table, kron, atol=1e-12)
    print("  columns (alpha,beta)->n:", col_elts)
    print("  F_G == H_2 ⊗ F_4 (literal, specified ordering):", kron_ok)

    conv_ok = True
    n_checked = 0
    for a in range(2):
        for b in range(4):
            for n in range(1, 61):
                lhs = chi_ab(a, b, n) * sigma3(n)
                rhs = 0j
                for d in divisors(n):
                    rhs += chi_ab(a, b, d) * chi_ab(a, b, n // d) * ((n // d) ** 3)
                if abs(lhs - rhs) > 1e-8:
                    conv_ok = False
                n_checked += 1
    print("  convolution identity chi(n) sigma_3(n) = sum chi(d) chi(n/d) (n/d)^3")
    print("  checked %d (8 chars x n<=60):" % n_checked, conv_ok)

    gate("S4-element orders {1,2,2,2,4,4,4,4}",
         orders[0] == 1 and order_ctr[2] == 3 and order_ctr[4] == 4
         and set(orders) <= {1, 2, 4})
    gate("S4-character table = H_2 ⊗ F_4", kron_ok)
    gate("S4-convolution D_chi = L(s,chi) L(s-3,chi) n<=60", conv_ok)

    # ------------------------------------------------------------------ S5
    section("S5  exponent arithmetic / Tr C^k = c_30(k)")
    exps = UNITS30
    sum_e = sum(exps)
    twom1 = tuple(2 * m + 1 for m in exps)
    sum_2m1 = sum(twom1)
    sum_marks = sum(MARKS)
    sumsq_marks = sum(m * m for m in MARKS)
    bries = sorted((15 * 1 + 10 * b + 6 * c) % 30
                   for b in (1, 2) for c in (1, 2, 3, 4))
    mckay = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 5) - 1
    traces = []
    ram = []
    Ck = sp.eye(8)
    tr_ok = True
    for k in range(1, 31):
        Ck = sp.simplify(Ck * C)
        tr = int(sp.simplify(Ck.trace()))
        ck = ramanujan_c(30, k)
        traces.append(tr)
        ram.append(ck)
        tr_ok &= tr == ck
    print("  exponents:", exps, "sum", sum_e)
    print("  2m+1:", twom1, "sum", sum_2m1)
    print("  affine marks:", MARKS, "sum", sum_marks, "sumsq", sumsq_marks)
    print("  Brieskorn (15+10b+6c) mod 30:", tuple(bries))
    print("  1/2+1/3+1/5-1 =", mckay)
    print("  Tr(C^k) k=1..30:", tuple(traces))
    print("  c_30(k)        :", tuple(ram))

    gate("S5-exponents = units mod 30, sum 120",
         exps == UNITS30 and sum_e == 120)
    gate("S5-2m+1 list sum 248",
         twom1 == (3, 15, 23, 27, 35, 39, 47, 59) and sum_2m1 == 248)
    gate("S5-affine marks sum 30, sum of squares 120",
         sum_marks == 30 and sumsq_marks == 120)
    gate("S5-Brieskorn (15a+10b+6c) mod 30 = units",
         tuple(bries) == tuple(sorted(UNITS30)))
    gate("S5-McKay 1/2+1/3+1/5-1=1/30", mckay == Fraction(1, 30))
    gate("S5-Tr(C^k)=c_30(k) k=1..30", tr_ok)

    # ------------------------------------------------------------------ S6
    section("S6  VERDICT")
    failed = [name for name, ok in CHECKS if not ok]
    if not failed:
        verdict = "FOUR_READOUTS_FROM_ONE_OBJECT"
    else:
        verdict = "BATTERY_INCOMPLETE(%s)" % ",".join(failed)
    gate("S6-verdict enum frozen",
         verdict == "FOUR_READOUTS_FROM_ONE_OBJECT"
         or verdict.startswith("BATTERY_INCOMPLETE("))

    n_pass = sum(1 for _, ok in CHECKS if ok)
    print("\nGATES %d/%d" % (n_pass, len(CHECKS)))
    print("SPEC_SHA %s" % SPEC_SHA)
    print("VERDICT: %s" % verdict)
    print("pure mathematics of E8 (Construction A, Coxeter theory, "
          "modular forms); no TFPT-specific physics input "
          "(c3, g_car, phi0) enters; not a claim")
    sys.exit(0 if n_pass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
