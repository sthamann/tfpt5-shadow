#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1018 -- E8.DIRECTED.READOUT.01 (2026-09-02):
SEVEN EXACT E8 READOUT CELLS (C7 OPEN).

Promotion of round r609.  The module RE-DERIVES the seven sealed
cells from scratch (no probe imports, no subprocess, no note-file
parser).  Every gated identity is exact over Z/Q via sympy or
plain integer arithmetic.  Display [E] (Identity).

THE SEVEN CELLS (probe C1--C6,C8; Hamming and the 120-line graph
are listed separately in the promotion brief):

  1. Seifert/Euler form.  Bourbaki E8 edges
     (1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4).  S_ii=1, S_ij=-1
     on a bipartite orientation.  S+S^T = A_{E8},
     charpoly(-S^{-1} S^T) = Phi_30, rank(S-S^T)=8, the charpoly
     is independent of bipartite vs unique-sink orientations.
     Accompanying sealed C5: exponents = totatives of 30,
     degrees {2,8,12,14,18,20,24,30}, sum(2m_i+1)=248,
     sum m_i=120, sum(m_i+1)=128.
  2. Hamming H_8 = RM(1,3)=extended Hamming [8,4,4]: weight
     enumerator 1+14 y^4+y^8, Construction A even unimodular,
     240 = 16 + 14*16 minimal vectors, S(3,4,8) Steiner system.
  3. Strongly regular root-line graph srg(120,56,28,24) with
     eigenvalues 56/8/-4 and multiplicities 1/35/84.
  4. Hecke rule: N(n)=240 sigma_3(n) for n<=10 (theta of E8 = E_4);
     coprime Hecke on (2,3),(2,5),(3,4),(4,5).
  5. Delta signature: A_P(n)/A_P(1)=tau(n) for n<=8 on three axes,
     degree-2/4/6 vanishing, E_4^3 - E_6^2 = 1728 Delta.
  6. (Z/30)^x cong C_2 x C_4 (orders {1,2,2,2,4,4,4,4}, not C_2^3);
     D_chi(s)=L(s,chi) L(s-3,chi) coefficientwise for n<=200.
  7. E6 oplus A2 gluing census: index 3, Smith (1^6,3,3),
     roots 72+6+162, glue classes 78/81/81.

NOT PROMOTED -- C7 (Gauss-code transform).  The eighth cell stays
OPEN: see note_e8_gaussian_code.tex remark rem:c7-audit.  The note
does not yet fix a transformation matrix of the Gaussian E8 code, so
monomial equivalence to H_2 tensor F_4 is an audit question, not a
sealed identity.  This module does not invent that matrix and does
not gate C7.

HONEST SCOPE: finite exact identities of the E8 lattice / Coxeter /
Hamming / Hecke / Delta / Dirichlet-character package.  Classical
ingredients (Phi_30, E_4=theta_{E8}, Ramanujan tau, Steiner S(3,4,8))
are re-derived here as machine-checked statements, not cited-only.
No physics claim.  NOT evidence for or against the Riemann Hypothesis.
NO RH CLAIM.  Python-only / Wolfram deferred (engine DEFERRED_NO_ENGINE).

PROVENANCE: experiments/tfpt-discovery/e8_directed_readout_probe.py
(r609, 49/49, VERDICT E8_READOUT_SEALED(7/8), SPEC_SHA
3edfb82499d80cecff6afb8da3b4533888b1dd042e7a8943e8caea1bdee581a3).
The probe stays experiments-side.
"""
from __future__ import annotations

import itertools
import math
from collections import defaultdict

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

from tfpt_constants import check as suite_check, summary, reset


R609_SPEC = "3edfb82499d80cecff6afb8da3b4533888b1dd042e7a8943e8caea1bdee581a3"
PHI30 = [1, 1, 0, -1, -1, -1, 0, 1, 1]
TAU = (1, -24, 252, -1472, 4830, -6048, -16744, 84480)
TOTATIVES = (1, 7, 11, 13, 17, 19, 23, 29)
EXPONENTS = TOTATIVES
DEGREES = tuple(m + 1 for m in EXPONENTS)
EDGES_E8 = ((1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4))
C7_NOTE = (
    "C7 Gauss-code transform NOT promoted: stays OPEN "
    "(note_e8_gaussian_code.tex rem:c7-audit)"
)


def check(label: str, condition: bool, detail: str = "") -> bool:
    ok = bool(condition)
    suite_check(label if not detail else "%s -- %s" % (label, detail), ok)
    return ok


def divisors(n: int) -> list[int]:
    n = abs(int(n))
    if n == 0:
        return []
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    out.sort()
    return out


def sigma_k(n: int, k: int) -> int:
    return sum(d ** k for d in divisors(n))


def ramanujan_c(n: int, k: int) -> int:
    g = math.gcd(n, k)
    return sum(int(sp.mobius(n // d)) * d for d in divisors(g))


def poly_mul(a: list[int], b: list[int], nmax: int) -> list[int]:
    c = [0] * (nmax + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        jmax = min(len(b) - 1, nmax - i)
        for j in range(jmax + 1):
            bj = b[j]
            if bj:
                c[i + j] += ai * bj
    return c


def _f2_points() -> list[tuple[int, int, int]]:
    return [(i & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]


def hamming_code() -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    pts = _f2_points()
    gens = [tuple(1 for _ in range(8))]
    for j in range(3):
        gens.append(tuple(p[j] for p in pts))
    gens_t = tuple(gens)
    words = []
    for bits in itertools.product((0, 1), repeat=4):
        w = [0] * 8
        for b, g in zip(bits, gens):
            if b:
                for i in range(8):
                    w[i] ^= g[i]
        words.append(tuple(w))
    return tuple(sorted(words)), gens_t


CODE, CODE_GENS = hamming_code()


def affine_hyperplanes() -> set[frozenset[int]]:
    pts = _f2_points()
    blocks = set()
    for a in itertools.product((0, 1), repeat=3):
        if a == (0, 0, 0):
            continue
        for bit in (0, 1):
            supp = frozenset(
                i for i, p in enumerate(pts)
                if (a[0] * p[0] + a[1] * p[1] + a[2] * p[2]) % 2 == bit
            )
            blocks.add(supp)
    return blocks


def cartan_e8() -> sp.Matrix:
    a = sp.eye(8) * 2
    for i, j in EDGES_E8:
        a[i - 1, j - 1] = -1
        a[j - 1, i - 1] = -1
    return a


def euler_S(arrows: list[tuple[int, int]]) -> sp.Matrix:
    s = sp.eye(8)
    for i, j in arrows:
        s[i - 1, j - 1] = -1
    return s


def bipartite_arrows() -> list[tuple[int, int]]:
    a_set = {1, 4, 6, 8}
    arrows = []
    for i, j in EDGES_E8:
        if i in a_set:
            arrows.append((i, j))
        else:
            arrows.append((j, i))
    return arrows


def sink_arrows(sink: int) -> list[tuple[int, int]]:
    adj: dict[int, list[int]] = {i: [] for i in range(1, 9)}
    for i, j in EDGES_E8:
        adj[i].append(j)
        adj[j].append(i)
    parent = {sink: 0}
    queue = [sink]
    for u in queue:
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                queue.append(v)
    arrows = []
    for v, u in parent.items():
        if u != 0:
            arrows.append((v, u))
    return arrows


def coxeter_from_arrows(arrows: list[tuple[int, int]]) -> sp.Matrix:
    s = euler_S(arrows)
    return -s.inv() * s.T


def charpoly_coeffs(m: sp.Matrix) -> list[int]:
    x = sp.symbols("x")
    p = m.charpoly(x)
    return [int(c) for c in p.all_coeffs()]


def gegenbauer_coeffs(n: int, lam: sp.Rational) -> list[sp.Rational]:
    t = sp.symbols("t")
    expr = sp.expand(sp.gegenbauer(n, lam, t))
    poly = sp.Poly(expr, t)
    return [sp.Rational(poly.coeff_monomial(t ** k)) for k in range(n + 1)]


def zonal_ql(n: int, u2: sp.Expr) -> tuple[sp.Expr, sp.Symbol, sp.Symbol]:
    q, ell = sp.symbols("q ell")
    ak = gegenbauer_coeffs(n, sp.Rational(3))
    expr = sp.Integer(0)
    for k, a in enumerate(ak):
        if a == 0 or ((n - k) & 1):
            continue
        expr += a * ell ** k * q ** ((n - k) // 2) / (u2 ** (sp.Rational(k, 2)))
    return sp.expand(expr), q, ell


def laplacian_ql(f: sp.Expr, q: sp.Symbol, ell: sp.Symbol, d: int, u2: sp.Expr) -> sp.Expr:
    fq = sp.diff(f, q)
    return sp.expand(
        2 * d * fq
        + 4 * q * sp.diff(f, q, 2)
        + 4 * ell * sp.diff(f, q, ell)
        + u2 * sp.diff(f, ell, 2)
    )


def half_table(bound: int, par: tuple[int, ...], max_ss: int) -> dict[int, list[tuple[int, ...]]]:
    ranges = [
        [x for x in range(-bound, bound + 1) if (x & 1) == (par[i] & 1)]
        for i in range(4)
    ]
    tab: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for v in itertools.product(*ranges):
        ss = v[0] * v[0] + v[1] * v[1] + v[2] * v[2] + v[3] * v[3]
        if ss <= max_ss:
            tab[ss].append(v)
    return tab


def enumerate_construction_a(max_n: int, collect_n: int = 0):
    max_ss = 4 * max_n
    bound = int(math.isqrt(max_ss))
    counts = {n: 0 for n in range(1, max_n + 1)}
    collected: dict[int, list[tuple[int, ...]]] = {
        n: [] for n in range(1, collect_n + 1)
    }
    for cw in CODE:
        left = half_table(bound, cw[:4], max_ss)
        right = half_table(bound, cw[4:], max_ss)
        for sl, lvecs in left.items():
            sr_max = max_ss - sl
            for sr, rvecs in right.items():
                if sr > sr_max:
                    continue
                ss = sl + sr
                if ss == 0 or ss % 4 != 0:
                    continue
                n = ss // 4
                if n > max_n:
                    continue
                nvec = len(lvecs) * len(rvecs)
                counts[n] += nvec
                if 1 <= n <= collect_n:
                    for a in lvecs:
                        for b in rvecs:
                            collected[n].append(a + b)
    return counts, collected


def eval_zonal_shell(arr: np.ndarray, ak: list[sp.Rational], n_deg: int, mode: str) -> sp.Rational:
    x = np.asarray(arr, dtype=object)
    ss = np.sum(x * x, axis=1)
    if mode == "e1":
        ell_num, ell_den = x[:, 0], 1
    elif mode == "diag":
        ell_num, ell_den = x[:, 0] + x[:, 1], "sqrt2"
    elif mode == "generic":
        ell_num, ell_den = 3 * x[:, 0] + 4 * x[:, 1], 5
    else:
        raise ValueError(mode)
    acc = 0
    for k, a in enumerate(ak):
        if a == 0 or ((n_deg - k) & 1):
            continue
        term = (ell_num ** k) * (ss ** ((n_deg - k) // 2))
        sterm = int(np.sum(term))
        if ell_den == "sqrt2":
            sterm = sp.Integer(sterm) / (2 ** (k // 2))
        elif ell_den != 1:
            sterm = sp.Integer(sterm) / (sp.Integer(ell_den) ** k)
        else:
            sterm = sp.Integer(sterm)
        acc += a * sterm
    return sp.nsimplify(acc)


def zspan_hnf_rows(vectors: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    if not vectors:
        return []
    dim = len(vectors[0])
    m = sp.Matrix(dim, len(vectors), lambda i, j: int(vectors[j][i]))
    h = hermite_normal_form(m)
    basis = []
    for j in range(h.cols):
        col = tuple(int(h[i, j]) for i in range(h.rows))
        if any(col):
            basis.append(col)
    return basis


def gram_int(basis: list[tuple[int, ...]]) -> sp.Matrix:
    b = sp.Matrix([list(v) for v in basis])
    return b * b.T


def smith_diag(mat: sp.Matrix) -> list[int]:
    s = smith_normal_form(mat)
    return [int(s[i, i]) for i in range(min(s.rows, s.cols))]


def gmul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def i_pow(m: int) -> tuple[int, int]:
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[m % 4]


def unit_ab(n: int) -> tuple[int, int] | None:
    n = n % 30
    for a in (0, 1):
        for b in range(4):
            if (pow(11, a, 30) * pow(7, b, 30)) % 30 == n:
                return a, b
    return None


def chi_kl(k: int, l: int, n: int) -> tuple[int, int]:
    if math.gcd(n, 30) != 1:
        return (0, 0)
    ab = unit_ab(n)
    if ab is None:
        return (0, 0)
    a, b = ab
    sign = 1 if ((k * a) & 1) == 0 else -1
    re, im = i_pow(l * b)
    return (sign * re, sign * im)


def cell1_seifert() -> sp.Matrix:
    print("\nCELL 1  Seifert/Euler form + principal multiplets")
    a = cartan_e8()
    arrows0 = bipartite_arrows()
    s = euler_S(arrows0)
    check("C1.S+ST=Cartan", s + s.T == a, "bipartite orientation")
    c = coxeter_from_arrows(arrows0)
    coeffs = charpoly_coeffs(c)
    x = sp.symbols("x")
    phi = [int(cf) for cf in sp.Poly(sp.cyclotomic_poly(30, x), x).all_coeffs()]
    check("C1.charpoly=Phi_30", coeffs == PHI30 and coeffs == phi, "coeffs=%s" % coeffs)
    ident = sp.eye(8)
    ok_period = c ** 30 == ident
    smaller = [d for d in divisors(30) if 0 < d < 30 and c ** d == ident]
    check("C1.C^30=I_min", ok_period and smaller == [], "smaller=%s" % (smaller,))
    traces = [int((c ** k).trace()) for k in range(0, 31)]
    rsums = [ramanujan_c(30, k) for k in range(0, 31)]
    check("C1.Tr(C^k)=c_30(k)", traces == rsums, "k=0..30")
    y = c + c.inv()
    quartic = y ** 4 + y ** 3 - 4 * y ** 2 - 4 * y + ident
    check("C1.Y-quartic", quartic == 0 * ident, "Y^4+Y^3-4Y^2-4Y+I=0")
    rk = int((s - s.T).rank())
    check("C1.skew-rank", rk == 8, "rank(S-S^T)=%d" % rk)
    p0 = coeffs
    p8 = charpoly_coeffs(coxeter_from_arrows(sink_arrows(8)))
    p4 = charpoly_coeffs(coxeter_from_arrows(sink_arrows(4)))
    check("C1.charpoly orientation-invariant", p0 == p8 == p4,
          "bipartite vs sink-8 vs sink-4")
    m = list(EXPONENTS)
    check("C5.sum(2m_i+1)=248", sum(2 * mi + 1 for mi in m) == 248)
    check("C5.sum m_i=120", sum(m) == 120)
    check("C5.sum(m_i+1)=128", sum(mi + 1 for mi in m) == 128)
    check("C5.degrees=m_i+1", DEGREES == (2, 8, 12, 14, 18, 20, 24, 30),
          "degrees=%s" % (DEGREES,))
    return c


def cell2_hamming_and_srg():
    print("\nCELL 2--3  Hamming H_8 + srg(120,56,28,24)")
    wdist = {}
    for w in CODE:
        wt = sum(w)
        wdist[wt] = wdist.get(wt, 0) + 1
    check("C2.weight-enumerator",
          len(CODE) == 16 and wdist == {0: 1, 4: 14, 8: 1},
          "1+14 y^4+y^8  dist=%s" % (wdist,))
    dual = []
    for v in itertools.product((0, 1), repeat=8):
        if all(sum(a * b for a, b in zip(v, c)) % 2 == 0 for c in CODE):
            dual.append(v)
    check("C2.self-dual", sorted(dual) == list(CODE), "C=C-perp")
    check("C2.doubly-even", all(sum(c) % 4 == 0 for c in CODE), "weights in 0 mod 4")
    gens = [list(g) for g in CODE_GENS]
    for i in range(8):
        v = [0] * 8
        v[i] = 2
        gens.append(v)
    basis_L = zspan_hnf_rows([tuple(g) for g in gens])
    check("C2.L-rank", len(basis_L) == 8, "HNF rank %d" % len(basis_L))
    gram = gram_int(basis_L)
    even = all(int(gram[i, j]) % 2 == 0 for i in range(8) for j in range(8))
    even_diag = all(int(gram[i, i]) % 4 == 0 for i in range(8))
    det_g = int(gram.det())
    det_scaled = sp.Rational(det_g, 256)
    check("C2.Gram even unimodular",
          even and even_diag and det_scaled == 1,
          "det(Gram_L)=%d  det(Gram/2)=%s" % (det_g, det_scaled))
    roots = []
    for cw in CODE:
        ranges = []
        for i in range(8):
            if cw[i] == 0:
                ranges.append([-2, 0, 2])
            else:
                ranges.append([-1, 1])
        for v in itertools.product(*ranges):
            if sum(x * x for x in v) == 4:
                roots.append(v)
    roots = tuple(sorted(roots))
    n_coord = sum(1 for r in roots if max(abs(x) for x in r) == 2)
    n_w4 = len(roots) - n_coord
    check("C2.min-vectors 240=16+14*16",
          len(roots) == 240 and n_coord == 16 and n_w4 == 14 * 16,
          "240=%d+%d" % (n_coord, n_w4))
    w4 = [c for c in CODE if sum(c) == 4]
    supports = [frozenset(i for i, b in enumerate(c) if b) for c in w4]
    planes = affine_hyperplanes()
    check("C2.affine-hyperplanes",
          set(supports) == planes and len(planes) == 14,
          "14 = 7 directions x 2")
    steiner_ok = True
    for triple in itertools.combinations(range(8), 3):
        hit = sum(1 for s in supports if set(triple) <= s)
        if hit != 1:
            steiner_ok = False
            break
    check("C2.Steiner S(3,4,8)", steiner_ok,
          "every 3-subset in exactly one weight-4 word")
    r0 = roots[0]
    dist = {2: 0, 1: 0, 0: 0, -1: 0, -2: 0}
    for r in roots:
        ip = sum(a * b for a, b in zip(r0, r)) // 2
        dist[ip] = dist.get(ip, 0) + 1
    want = {2: 1, 1: 56, 0: 126, -1: 56, -2: 1}
    check("C2.inner-product dist", dist == want,
          "(2,1,0,-1,-2)=(%d,%d,%d,%d,%d)"
          % (dist[2], dist[1], dist[0], dist[-1], dist[-2]))
    lines = []
    seen = set()
    for r in roots:
        key = r if r > tuple(-x for x in r) else tuple(-x for x in r)
        if key not in seen:
            seen.add(key)
            lines.append(key)
    nlines = len(lines)
    a_adj = np.zeros((nlines, nlines), dtype=np.int64)
    for i in range(nlines):
        for j in range(i + 1, nlines):
            ip = sum(a * b for a, b in zip(lines[i], lines[j])) // 2
            if abs(ip) == 1:
                a_adj[i, j] = 1
                a_adj[j, i] = 1
    a2 = a_adj @ a_adj
    deg = np.diag(a2)
    lam_vals = a2[a_adj == 1]
    mu_mask = (a_adj == 0) & (~np.eye(nlines, dtype=bool))
    mu_vals = a2[mu_mask]
    lam = int(lam_vals[0]) if lam_vals.size else -1
    mu = int(mu_vals[0]) if mu_vals.size else -1
    srg = (
        nlines == 120
        and set(int(d) for d in deg) == {56}
        and lam_vals.size > 0 and mu_vals.size > 0
        and int(lam_vals.min()) == int(lam_vals.max()) == 28
        and int(mu_vals.min()) == int(mu_vals.max()) == 24
    )
    disc = (lam - mu) ** 2 + 4 * (56 - mu)
    theta = (lam - mu + int(math.isqrt(disc))) // 2
    tau_e = (lam - mu - int(math.isqrt(disc))) // 2
    n_m, k_m = 120, 56
    rootd = int(math.isqrt(disc))
    f_mult = ((n_m - 1) + ((n_m - 1) * (mu - lam) - 2 * k_m) // rootd) // 2
    g_mult = ((n_m - 1) - ((n_m - 1) * (mu - lam) - 2 * k_m) // rootd) // 2
    mults = sorted((1, f_mult, g_mult))
    check("C2.120-line spectrum",
          srg and mults == [1, 35, 84] and (theta, tau_e) == (8, -4),
          "srg(120,56,%d,%d) eig (56, %d, %d) mult (1, %d, %d)"
          % (lam, mu, theta, tau_e, f_mult, g_mult))
    return roots, basis_L


def cell4_hecke(counts: dict[int, int]) -> None:
    print("\nCELL 4  Hecke N(n)=240 sigma_3(n)")
    n_ok = True
    got = []
    for n in range(1, 11):
        want = 240 * sigma_k(n, 3)
        got.append(counts[n])
        if counts[n] != want:
            n_ok = False
            check("C3.N(%d)" % n, False,
                  "got %d want 240*sigma_3(%d)=%d" % (counts[n], n, want))
    if n_ok:
        check("C3.N(n)=240 sigma_3(n)", True, "n=1..10  N=%s" % (got,))
    pairs = ((2, 3), (2, 5), (3, 4), (4, 5))
    hecke_ok = True
    details = []
    for m, n in pairs:
        lhs = counts[m * n]
        rhs = counts[m] * counts[n] // 240
        details.append("%d*%d: %d vs %d" % (m, n, lhs, rhs))
        if lhs != rhs:
            hecke_ok = False
    check("C3.Hecke coprime", hecke_ok, "; ".join(details))


def cell5_delta(collected: dict[int, list[tuple[int, ...]]]) -> None:
    print("\nCELL 5  Ramanujan Delta as first anisotropy")
    for tag, u2 in (
        ("u=e1", 1),
        ("u=(1,1,0..)/sqrt2", 1),
        ("u=(3,4,0..)/5", 1),
    ):
        f, q, ell = zonal_ql(8, sp.Integer(u2))
        lap = laplacian_ql(f, q, ell, 8, sp.Integer(u2))
        check("C4.Delta P=0 (%s)" % tag, lap == 0, "symbolic Laplacian in (q,ell)")
    ak8 = gegenbauer_coeffs(8, sp.Rational(3))
    directions = ("e1", "diag", "generic")
    ap_table: dict[str, list[sp.Rational]] = {}
    for name in directions:
        vals = []
        for n in range(1, 9):
            arr = np.array(collected[n], dtype=object)
            vals.append(eval_zonal_shell(arr, ak8, 8, name))
        ap_table[name] = vals
    working = None
    tau_hits = []
    for name, vals in ap_table.items():
        if vals[0] == 0:
            check("C4.A_P(n)/A_P(1)=tau(n)  u=%s" % name, False, "A_P(1)=0")
            continue
        if working is None:
            working = name
        ratios = [sp.simplify(vals[n] / vals[0]) for n in range(8)]
        ok = ratios == [sp.Integer(t) for t in TAU]
        if ok:
            tau_hits.append(name)
        check("C4.A_P(n)/A_P(1)=tau(n)  u=%s" % name, ok,
              "A_P(1)=%s ratios=%s" % (vals[0], [int(r) for r in ratios]))
    nonzero = [name for name, vals in ap_table.items() if vals[0] != 0]
    check("C4.which-u", len(nonzero) > 0,
          "A_P(1)!=0 on %s; tau match on %s"
          % (",".join(nonzero) if nonzero else "(none)",
             ",".join(tau_hits) if tau_hits else "(none)"))
    vanish_ok = True
    vanish_detail = []
    for deg in (2, 4, 6):
        ak = gegenbauer_coeffs(deg, sp.Rational(3))
        f, q, ell = zonal_ql(deg, sp.Integer(1))
        if laplacian_ql(f, q, ell, 8, sp.Integer(1)) != 0:
            vanish_ok = False
            vanish_detail.append("deg%d not harmonic" % deg)
            continue
        for n in range(1, 5):
            arr = np.array(collected[n], dtype=object)
            s = eval_zonal_shell(arr, ak, deg, "e1")
            vanish_detail.append("F_%d(n=%d)=%s" % (deg, n, s))
            if s != 0:
                vanish_ok = False
    check("C4.deg 2,4,6 vanish n=1..4", vanish_ok,
          "7-design; " + ", ".join(vanish_detail[:6]))
    nmax = 8
    e4 = [0] * (nmax + 1)
    e6 = [0] * (nmax + 1)
    e4[0] = 1
    e6[0] = 1
    for n in range(1, nmax + 1):
        e4[n] = 240 * sigma_k(n, 3)
        e6[n] = -504 * sigma_k(n, 5)
    e4_3 = poly_mul(poly_mul(e4, e4, nmax), e4, nmax)
    e6_2 = poly_mul(e6, e6, nmax)
    diff = [e4_3[i] - e6_2[i] for i in range(nmax + 1)]
    delta = [0] * (nmax + 1)
    delta[1] = 1
    for n in range(1, nmax + 1):
        fac = [0] * (nmax + 1)
        for k in range(0, 25):
            exp = n * k
            if exp > nmax:
                break
            fac[exp] += math.comb(24, k) * ((-1) ** k)
        delta = poly_mul(delta, fac, nmax)
    check("C4.E4^3-E6^2=1728 Delta",
          diff == [1728 * c for c in delta],
          "q-series to order 8; Delta=%s" % (delta[1:],))
    if working is not None:
        c0 = ap_table[working][0]
        theta_p = [0] + ap_table[working]
        want_th = [c0 * sp.Integer(delta[n]) for n in range(nmax + 1)]
        ok_th = all(theta_p[n] == want_th[n] for n in range(1, nmax + 1))
        check("C4.Theta_{E8,P}=c Delta", ok_th, "c=A_P(1)=%s" % c0)


def cell6_characters() -> None:
    print("\nCELL 6  (Z/30)^x characters")
    units = list(TOTATIVES)
    orders = []
    for g in units:
        x, k = g, 1
        while x != 1:
            x = (x * g) % 30
            k += 1
            if k > 30:
                break
        orders.append(k)
    multiset = tuple(sorted(orders))
    check("C6.order multiset",
          multiset == (1, 2, 2, 2, 4, 4, 4, 4),
          "orders=%s" % (multiset,))
    check("C6.iso C2xC4",
          orders.count(1) == 1 and orders.count(2) == 3 and orders.count(4) == 4,
          "(Z/30)^x cong C2 x C4")
    check("C6.not iso (F2^3,+)",
          multiset != tuple([1] + [2] * 7),
          "(F2^3,+) all seven nontrivial order 2")
    elts = []
    for a in range(2):
        for b in range(4):
            elts.append((pow(11, a, 30) * pow(7, b, 30)) % 30)
    h2f4 = [[None] * 8 for _ in range(8)]
    for k in range(2):
        for l in range(4):
            for a in range(2):
                for b in range(4):
                    sign = 1 if ((k * a) & 1) == 0 else -1
                    re, im = i_pow(l * b)
                    h2f4[k * 4 + l][a * 4 + b] = (sign * re, sign * im)
    chi_prod = [[None] * 8 for _ in range(8)]
    for k in range(2):
        for l in range(4):
            for j, g in enumerate(elts):
                chi_prod[k * 4 + l][j] = chi_kl(k, l, g)
    check("C6.H2⊗F4 in product order", chi_prod == h2f4,
          "cols (a,b), rows (k,l)")
    col_of = [elts.index(u) for u in units]
    chi_sorted = [[chi_kl(k, l, u) for u in units] for k in range(2) for l in range(4)]
    h2_perm = [[h2f4[r][col_of[c]] for c in range(8)] for r in range(8)]
    check("C6.Fourier monomially ~ H2⊗F4", chi_sorted == h2_perm,
          "column perm %s" % (col_of,))
    vals = {chi_kl(k, l, u) for k in range(2) for l in range(4) for u in units}
    check("C6.character values in {±1,±i}",
          vals <= {(1, 0), (-1, 0), (0, 1), (0, -1)},
          "values=%s" % (sorted(vals),))
    nmax = 200
    dchi_ok = True
    nfail = None
    for k in range(2):
        for l in range(4):
            for n in range(1, nmax + 1):
                chn = chi_kl(k, l, n)
                lhs = (chn[0] * sigma_k(n, 3), chn[1] * sigma_k(n, 3))
                rhs = (0, 0)
                for d in divisors(n):
                    prod = gmul(chi_kl(k, l, d), chi_kl(k, l, n // d))
                    sc = (n // d) ** 3
                    rhs = (rhs[0] + prod[0] * sc, rhs[1] + prod[1] * sc)
                if lhs != rhs:
                    dchi_ok = False
                    nfail = (k, l, n, lhs, rhs)
                    break
            if not dchi_ok:
                break
        if not dchi_ok:
            break
    check("C6.D_chi = L(s,chi)L(s-3,chi)", dchi_ok,
          "n<=200, 8 Dirichlet chars mod 30"
          + ("" if dchi_ok else " FAIL %s" % (nfail,)))


def cell7_e6_a2(roots: tuple, basis_L: list[tuple[int, ...]]) -> None:
    print("\nCELL 7  E6 ⊕ A2 ⊂ E8 glue")
    alpha = None
    beta = None
    for r in roots:
        if r == (2, 0, 0, 0, 0, 0, 0, 0) or r == (-2, 0, 0, 0, 0, 0, 0, 0):
            alpha = r
            break
    if alpha is None:
        alpha = roots[0]
    for r in roots:
        ip = sum(a * b for a, b in zip(alpha, r))
        if ip == -2:
            beta = r
            break
    check("C8.A2 pair", alpha is not None and beta is not None,
          "alpha=%s beta=%s" % (alpha, beta))
    a2_roots = []
    for s in (1, -1):
        a2_roots.append(tuple(s * x for x in alpha))
        a2_roots.append(tuple(s * x for x in beta))
        a2_roots.append(tuple(s * (alpha[i] + beta[i]) for i in range(8)))
    a2_roots = tuple(sorted(set(a2_roots)))
    e6_roots = []
    for r in roots:
        if (sum(a * b for a, b in zip(r, alpha)) == 0
                and sum(a * b for a, b in zip(r, beta)) == 0):
            e6_roots.append(r)
    in_a2 = set(a2_roots)
    e6_set = set(e6_roots)
    glue_roots = [r for r in roots if r not in in_a2 and r not in e6_set]
    split = (len(e6_roots), len(a2_roots), len(glue_roots))
    check("C8.root split 72+6+162", split == (72, 6, 162),
          "got %s" % (split,))
    e6_basis = zspan_hnf_rows(e6_roots)
    a2_basis = zspan_hnf_rows(list(a2_roots))
    check("C8.ranks E6,A2",
          len(e6_basis) == 6 and len(a2_basis) == 2,
          "rk E6=%d rk A2=%d" % (len(e6_basis), len(a2_basis)))
    m_basis = zspan_hnf_rows(e6_basis + a2_basis)
    check("C8.M=E6⊕A2 rank 8", len(m_basis) == 8, "rk M=%d" % len(m_basis))
    gram_m = gram_int(m_basis)
    gram_l = gram_int(basis_L)
    det_m = int(gram_m.det())
    det_l = int(gram_l.det())
    ratio = sp.Rational(det_m, det_l)
    index = int(sp.sqrt(ratio)) if ratio > 0 and sp.sqrt(ratio).is_integer else -1
    check("C8.index 3 (det 9 scaled)",
          index == 3 and ratio == 9,
          "det Gram_M=%d det Gram_L=%d  [L:M]=%s" % (det_m, det_l, index))
    even_m = all(int(gram_m[i, j]) % 2 == 0 for i in range(8) for j in range(8))
    gram_scaled = sp.Matrix(8, 8, lambda i, j: int(gram_m[i, j]) // 2)
    inv = smith_diag(gram_scaled) if even_m else []
    inv_abs = [abs(d) for d in inv if d not in (0,)]
    check("C8.Smith (1^6,3,3)",
          even_m and sorted(inv_abs) == [1, 1, 1, 1, 1, 1, 3, 3],
          "Smith(Gram_M/2)=%s" % (inv,))
    b = sp.Matrix([list(v) for v in m_basis])
    binv = b.inv()
    class_count: dict[tuple, int] = defaultdict(int)
    for r in roots:
        xi = (sp.Matrix(list(r)).T * binv).tolist()[0]
        frac = []
        for t in xi:
            t = sp.nsimplify(t)
            frac.append(t - sp.floor(t))
        class_count[tuple(frac)] += 1
    sizes = sorted(class_count.values(), reverse=True)
    check("C8.glue classes 78/81/81",
          len(class_count) == 3 and sizes == [81, 81, 78],
          "#classes=%d  sizes=%s" % (len(class_count), sizes))


def run():
    reset()
    print("=" * 74)
    print("v1018 -- E8.DIRECTED.READOUT.01  (seven exact cells; C7 OPEN)")
    print("SPEC_SHA %s" % R609_SPEC)
    print(C7_NOTE)
    print("=" * 74, flush=True)

    cell1_seifert()
    roots, basis_L = cell2_hamming_and_srg()
    cell6_characters()

    print("\nenumeration  Construction-A shells n=1..20 (collect n<=8)")
    counts, collected = enumerate_construction_a(max_n=20, collect_n=8)
    print("  N(n) n=1..10: %s" % [counts[n] for n in range(1, 11)], flush=True)
    cell4_hecke(counts)
    cell5_delta(collected)
    cell7_e6_a2(roots, basis_L)

    print("\nC7 STATUS: OPEN -- not gated.  %s" % C7_NOTE)
    print("  r609 SPEC_SHA  %s" % R609_SPEC)
    return summary("v1018 E8 directed readout (7/8 cells; C7 open)")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
