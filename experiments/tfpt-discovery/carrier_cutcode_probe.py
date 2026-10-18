#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""carrier_cutcode_probe -- CARRIER.CUTCODE.01 (K5 round, cut-code
strand): the Arf split 16 = 1 + 5bar + 10 IS the cut classification of
K5, and the Clebsch graph grades over the Arf shells as 40 = 5 + 20 + 15
with the within-10 edge graph the Petersen graph.

THEOREM CANDIDATE (preregistered, frozen BEFORE running).  Let
C_even(5) = iota(V) be the 16 even-weight words on the five carrier
slots (the certified parity lift of V = L/(1+i)L, v774 /
arf_spinor_compiler_probe, ARF-SPINOR-EXACT), q* the canonical Arf
refinement (q* = q_wt = wt(iota)/2 mod 2, selector-unique).  Define the
CUT MAP into the K5 edge space

    delta: F2^5 -> F2^10,   delta(x)_{ij} = x_i + x_j   (edges of K5).

STEPS (all exact F2/integer censuses; kill bars frozen):
 S0  q* rebuilt from the certified machinery: brute force over all
     2^16 functions gives exactly 16 quadratic refinements of hbar
     (Gram J - I); the frozen selector (sigma-invariant, q(A) = 1,
     q(F_Sigma) = 0) is unique; q* == q_wt.
 S1  CUT MAP: delta injective on C_even(5) (kernel on F2^5 = the
     repetition code {00000, 11111}); ISOMETRIC for the bilinear form:
     delta(x).delta(y) = x.y mod 2 for ALL 256 pairs of C_even words;
     quadratic identity q*(v) = wt(iota v)/2 = wt(delta iota v)/2
     mod 2 on all 16 words (with wt(delta x) = w(5 - w), w = wt(x)).
 S2  CUT CENSUS: cut weights (0 -> 0; ten wt-2 words -> 6; five wt-4
     words -> 4); the five wt-4 words ARE the elementary (1|4) cuts
     (bijection onto the 5 vertices; delta = star indicator) and the
     ten wt-2 words ARE the (2|3) cuts (bijection onto the 10 duads);
     the Arf split 16 = 1 + 5bar + 10 = the cut classification
     (0|5) + (1|4) + (2|3)  [E neu -- certify].
 S3  CLEBSCH -> PETERSEN SHELLS: the flip-weight-4 relation on the 16
     words is the Clebsch graph SRG(16,5,0,2) (corpus identification:
     tfpt_1_architecture_e8.tex Theorem 2, R_4(C^+) = Clebsch, 40
     edges = |R(D5)|); the 40 edges split EXACTLY over the Arf shells
     as 40 = 5 (0<->5bar) + 20 (5bar<->10) + 15 (within-10), with
     0<->10 and within-5bar EMPTY; the within-10 edge graph IS the
     Petersen graph = Kneser(5,2) (explicit support bijection, SRG
     (10,3,0,1), girth 5, FULL isomorphism census expected 120).
     Number readings typed as AUDIT FINGERPRINTS [C]: 5 = g_car (P2),
     20 = det L (v52/v71/v91), 15 = dim A3 (v91); the partition
     itself [E neu].
 S4  GAUSSIAN GRADING (v752 machinery verbatim, read-only): the 240
     roots (15 classes x 16) and the 60 mu4-lines (J free of order 4,
     v700/v629) grade over the Arf shells of their Gaussian classes:
     240 roots = 80 (5bar shell) + 160 (10 shell), 60 lines = 20 + 40;
     240 = 160 + 80 equals the scheme orthogonality diag(16,160,80)
     of tfpt_1 Theorem 2 (fingerprint).  TYPED: this is an Arf/cut
     grading of root classes, explicitly NOT a matter split -- the
     code->matter reading is ROOTCLASS-MIXED (v775), dead at root
     level; nothing here reopens it.

MUST-FAIL CONTROLS (frozen):
 C1  a mutated cut map (entry (0,1) replaced by x_0 alone) breaks the
     quadratic-identity census.
 C2  odd-weight words break the isometry: over all 1024 pairs of
     F2^5, delta(x).delta(y) != x.y exactly on the 16 x 16 = 256
     odd x odd pairs (the correction term is (sum x)(sum y)).
 C3  the wrong edge relation (flip weight 2 = the Clebsch complement
     SRG(16,10,6,6)) does NOT produce the (5, 20, 15) shell split.
 C4  scrambled Clebsch vertices (deterministic transposition of a
     wt-2 word with a wt-4 word) break the 5 + 20 + 15 partition.

KILLS (any one fires => core dead):
 K1  refinement count != 16, selector not unique, or q* != q_wt.
 K2  delta not injective on C_even(5), kernel != repetition code,
     isometry fails in any of the 256 cells, or the quadratic
     identity fails on any word.
 K3  cut census != {0: 1, 6: 10, 4: 5}, or either cut bijection
     ((1|4) <-> 5bar, (2|3) <-> 10) fails.
 K4  Clebsch parameters != SRG(16,5,0,2) or 40 edges, or the shell
     split != (5, 0, 0, 20, 15), or the within-10 graph is not
     Petersen (isomorphism census != 120).
 K5  (grading only, -> PARTIAL not DEAD) root split != 80 + 160,
     line count != 60, lines not class-pure, or line split != 20+40.

VERDICTS (frozen): CUTCODE-EXACT (S0-S4 all green, all controls
fire) / CUTCODE-PARTIAL (S0-S3 green, S4 grading fails) /
CUTCODE-DEAD (any of K1-K4 fires) / TEST-VOID (a must-fail control
does not fire).

HONESTY FENCE: finite exact combinatorics reproducing and extending
corpus objects (v774 Arf geometry, tfpt_1 Theorem 2 Clebsch, v700
lines).  No physics claim; the 5/20/15/80/160 readings are audit
fingerprints, not derivations; ROOTCLASS-MIXED (v775) stands.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt.  Exakte Ganzzahl/F2-Arithmetik durchgehend; keine Floats,
kein RNG, kein Fit, kein freier Parameter, kein sympy.

Sources (read-only): experiments/tfpt-discovery/
arf_spinor_compiler_probe.py == verification/v774 (q*, iota, hbar,
v752 lattice recipe copied verbatim), tfpt_1_architecture_e8.tex
Theorem 2 (Clebsch SRG(16,5,0,2), 40 = |R(D5)|, diag(16,160,80)),
verification/v700_orbit60_census.py (60 mu4-lines), v52/v71/v91
(det L = 20, dim A3 = 15), verification/v775 (ROOTCLASS-MIXED).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/carrier_cutcode_probe.py
"""

import itertools
import time
from collections import Counter
from fractions import Fraction as Fr

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ======================================================================
# abstract F2^4 layer (verbatim conventions of arf_spinor_compiler_probe)
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]  # J - I


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


def xor(v, w):
    return tuple((a + b) % 2 for a, b in zip(v, w))


ADD = [[WIDX[xor(v, w)] for w in W16] for v in W16]
HTAB = [[hb(v, w) for w in W16] for v in W16]
NZ15 = [w for w in W16 if any(w)]
A_BIT = (0, 0, 0, 1)
FSIG = (1, 1, 1, 0)


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


def iota(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


# ======================================================================
# S0 -- q* rebuilt from the certified machinery
# ======================================================================
def s0_qstar():
    section("S0: q* rebuilt (brute force 2^16 + frozen selector; == q_wt)")
    refs = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            hrow = HTAB[i]
            arow = ADD[i]
            qi = q[i]
            for j in range(16):
                if q[arow[j]] ^ qi ^ q[j] != hrow[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            refs.append(tuple(q))
    sig_perm = [WIDX[sig_bits(w)] for w in W16]
    siginv = [q for q in refs
              if all(q[sig_perm[i]] == q[i] for i in range(16))]
    cand = [q for q in siginv
            if q[WIDX[A_BIT]] == 1 and q[WIDX[FSIG]] == 0]
    qwt = tuple((sum(iota(w)) // 2) % 2 for w in W16)
    check("S0.1 exactly 16 quadratic refinements; frozen selector unique; "
          "q* == q_wt = wt(iota)/2 mod 2 (certified identification, v774)",
          len(refs) == 16 and len(cand) == 1 and cand[0] == qwt,
          "refs=%d, selector candidates=%d" % (len(refs), len(cand)),
          kill="K1")
    return qwt


# ======================================================================
# S1 -- the cut map
# ======================================================================
EDGES = [(i, j) for i in range(5) for j in range(i + 1, 5)]


def delta(x):
    return tuple((x[i] + x[j]) % 2 for (i, j) in EDGES)


def wt(x):
    return sum(x)


def s1_cut_map(qstar):
    section("S1: the cut map delta: C_even(5) -> F2^10 (cuts of K5)")
    ceven = sorted(iota(v) for v in W16)
    imgs = {delta(x) for x in ceven}
    f2_5 = list(itertools.product((0, 1), repeat=5))
    kernel = [x for x in f2_5 if delta(x) == (0,) * 10]
    check("S1.1 delta INJECTIVE on C_even(5) (16 distinct images); kernel "
          "on F2^5 = repetition code {00000, 11111}",
          len(imgs) == 16 and sorted(kernel) == [(0,) * 5, (1,) * 5],
          "images=%d, kernel=%s" % (len(imgs), kernel), kill="K2")

    ok_iso = all(sum(a * b for a, b in zip(delta(x), delta(y))) % 2
                 == sum(a * b for a, b in zip(x, y)) % 2
                 for x in ceven for y in ceven)
    check("S1.2 ISOMETRY: delta(x).delta(y) == x.y mod 2 for ALL 256 "
          "pairs of C_even words (exact census)", ok_iso, kill="K2")

    ok_wt = all(wt(delta(x)) == wt(x) * (5 - wt(x)) for x in ceven)
    ok_even = all(wt(delta(x)) % 2 == 0 for x in ceven)
    ok_q = all(qstar[WIDX[v]] == (wt(delta(iota(v))) // 2) % 2
               and qstar[WIDX[v]] == (wt(iota(v)) // 2) % 2
               for v in W16)
    check("S1.3 QUADRATIC IDENTITY: wt(delta x) = w(5-w) (even), and "
          "q*(v) = wt(iota v)/2 = wt(delta iota v)/2 mod 2 on all 16 "
          "words (census)", ok_wt and ok_even and ok_q, kill="K2")
    return ceven


# ======================================================================
# S2 -- the cut census: Arf split = cut classification
# ======================================================================
def s2_cut_census(qstar):
    section("S2: cut census -- 16 = 1 + 5bar + 10 IS (0|5) + (1|4) + (2|3)")
    cw = Counter(wt(delta(iota(v))) for v in W16)
    check("S2.1 CUT WEIGHTS: {0: 1, 6: 10, 4: 5} (zero word -> 0; ten "
          "wt-2 words -> 6; five wt-4 words -> 4): %s"
          % dict(sorted(cw.items())),
          dict(cw) == {0: 1, 6: 10, 4: 5}, kill="K3")

    five = [v for v in NZ15 if qstar[WIDX[v]] == 0]
    ten = [v for v in W16 if qstar[WIDX[v]] == 1]
    ok_shell_wt = (all(wt(iota(v)) == 4 for v in five)
                   and all(wt(iota(v)) == 2 for v in ten))

    # the five 5bar words ARE the elementary (1|4) cuts
    star_of = {}
    ok_star = True
    for v in five:
        x = iota(v)
        zeros = [i for i in range(5) if x[i] == 0]
        if len(zeros) != 1:
            ok_star = False
            continue
        i = zeros[0]
        star_of[v] = i
        if delta(x) != tuple(1 if i in e else 0 for e in EDGES):
            ok_star = False
    check("S2.2 the 5bar words ARE the elementary (1|4) cuts: each wt-4 "
          "word isolates a unique vertex, delta = star indicator; the "
          "map onto the 5 vertices is a BIJECTION",
          ok_star and ok_shell_wt and sorted(star_of.values()) == [0, 1,
                                                                   2, 3, 4],
          kill="K3")

    # the ten 10 words ARE the (2|3) cuts
    duad_of = {}
    ok_23 = True
    for v in ten:
        x = iota(v)
        supp = tuple(i for i in range(5) if x[i] == 1)
        if len(supp) != 2:
            ok_23 = False
            continue
        duad_of[v] = supp
        if delta(x) != tuple(1 if len(set(e) & set(supp)) == 1 else 0
                             for e in EDGES):
            ok_23 = False
    check("S2.3 the 10 words ARE the (2|3) cuts: delta(x)_e = 1 iff e "
          "crosses the duad; the map onto the 10 duads is a BIJECTION "
          "==> the Arf split 16 = 1 + 5bar + 10 IS the cut "
          "classification (0|5) + (1|4) + (2|3)  [E neu]",
          ok_23 and len(set(duad_of.values())) == 10, kill="K3")
    return five, ten, star_of, duad_of


# ======================================================================
# S3 -- Clebsch graph over the Arf shells; within-10 = Petersen
# ======================================================================
def clebsch_adj(x, y):
    return wt(xor4or5(x, y)) == 4


def xor4or5(x, y):
    return tuple((a + b) % 2 for a, b in zip(x, y))


def shell_split(words5, adj_fn):
    """edge counts (0-5, 0-10, 5-5, 5-10, 10-10) for a relation on the
    16 C_even words, shells frozen as iota-weight 0 / 4 / 2."""
    def shell(x):
        return {0: "0", 4: "5", 2: "10"}[wt(x)]
    cnt = Counter()
    for x, y in itertools.combinations(words5, 2):
        if adj_fn(x, y):
            cnt[tuple(sorted((shell(x), shell(y))))] += 1
    return (cnt[("0", "5")], cnt[("0", "10")], cnt[("5", "5")],
            cnt[("10", "5")], cnt[("10", "10")])


def count_isomorphisms(adj1, adj2, n):
    """exact backtracking census of graph isomorphisms adj1 -> adj2."""
    count = 0
    mapping = [-1] * n
    used = [False] * n

    def rec(k):
        nonlocal count
        if k == n:
            count += 1
            return
        for t in range(n):
            if used[t]:
                continue
            ok = True
            for j in range(k):
                if (j in adj1[k]) != (mapping[j] in adj2[t]):
                    ok = False
                    break
            if ok:
                mapping[k] = t
                used[t] = True
                rec(k + 1)
                used[t] = False
        mapping[k] = -1

    rec(0)
    return count


def s3_clebsch(ceven, ten, duad_of):
    section("S3: Clebsch SRG(16,5,0,2) -> Arf shells 40 = 5 + 20 + 15; "
            "within-10 = Petersen")
    n = 16
    adj = {x: {y for y in ceven if y != x and clebsch_adj(x, y)}
           for x in ceven}
    degs = {len(a) for a in adj.values()}
    n_edges = sum(len(a) for a in adj.values()) // 2
    lam_ok = all(len(adj[x] & adj[y]) == 0
                 for x in ceven for y in adj[x])
    mu_ok = all(len(adj[x] & adj[y]) == 2
                for x, y in itertools.combinations(ceven, 2)
                if y not in adj[x])
    check("S3.1 the flip-weight-4 relation on the 16 words is "
          "SRG(16,5,0,2) with 40 edges = |R(D5)| (corpus: tfpt_1 "
          "Theorem 2, R_4(C^+) = Clebsch graph)",
          degs == {5} and n_edges == 40 and lam_ok and mu_ok,
          "deg=%s, edges=%d" % (sorted(degs), n_edges), kill="K4")

    split = shell_split(ceven, clebsch_adj)
    check("S3.2 ARF-SHELL EDGE SPLIT: (0-5bar, 0-10, 5bar-5bar, "
          "5bar-10, 10-10) = %s == (5, 0, 0, 20, 15); 40 = 5 + 20 + 15 "
          "[E neu partition; fingerprints [C]: 5 = g_car (P2), 20 = "
          "det L (v52/v71/v91), 15 = dim A3 (v91)]" % (split,),
          split == (5, 0, 0, 20, 15) and sum(split) == 40, kill="K4")

    # within-10 graph == Petersen = Kneser(5,2)
    ten_w = sorted(iota(v) for v in ten)
    adj10 = [set() for _ in range(10)]
    for i, x in enumerate(ten_w):
        for j, y in enumerate(ten_w):
            if i != j and clebsch_adj(x, y):
                adj10[i].add(j)
    duads = sorted(itertools.combinations(range(5), 2))
    didx = {d: i for i, d in enumerate(duads)}
    kneser = [set() for _ in range(10)]
    for a, b in itertools.combinations(duads, 2):
        if not set(a) & set(b):
            kneser[didx[a]].add(didx[b])
            kneser[didx[b]].add(didx[a])
    # explicit support bijection is an isomorphism
    supp_map = [didx[tuple(i for i in range(5) if x[i] == 1)]
                for x in ten_w]
    ok_bij = (sorted(supp_map) == list(range(10))
              and all((j in adj10[i])
                      == (supp_map[j] in kneser[supp_map[i]])
                      for i in range(10) for j in range(10) if i != j))
    # Petersen parameters: SRG(10,3,0,1) + girth 5
    deg10 = {len(a) for a in adj10}
    lam10 = all(len(adj10[i] & adj10[j]) == 0
                for i in range(10) for j in adj10[i])
    mu10 = all(len(adj10[i] & adj10[j]) == 1
               for i, j in itertools.combinations(range(10), 2)
               if j not in adj10[i])
    tri = any(j in adj10[i] and k in adj10[j] and i in adj10[k]
              for i in range(10) for j in adj10[i] for k in adj10[j])
    quad = any(len(adj10[i] & adj10[j]) >= 2
               for i, j in itertools.combinations(range(10), 2))
    n_iso = count_isomorphisms(adj10, kneser, 10)
    check("S3.3 the WITHIN-10 edge graph IS the Petersen graph: support "
          "bijection onto Kneser(5,2) is an isomorphism; SRG(10,3,0,1), "
          "girth 5; FULL isomorphism census = %d == 120 = |S5|" % n_iso,
          ok_bij and deg10 == {3} and lam10 and mu10
          and not tri and not quad and n_iso == 120, kill="K4")
    return adj, ten_w


# ======================================================================
# S4 -- Gaussian grading (v752 machinery, copied VERBATIM; read-only)
# ======================================================================
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


def mat_det_inv(rows):
    n = len(rows)
    A = [[Fr(v) for v in r] for r in rows]
    I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        if piv is None:
            return Fr(0), None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            I[col], I[piv] = I[piv], I[col]
            det = -det
        det *= A[col][col]
        inv = 1 / A[col][col]
        A[col] = [a * inv for a in A[col]]
        I[col] = [a * inv for a in I[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                I[r] = [a - f * b for a, b in zip(I[r], I[col])]
    return det, I


def vec_mat(x, M):
    n = len(M)
    return tuple(sum(x[i] * M[i][j] for i in range(n)) for j in range(n))


def row_hnf(rows):
    M = [list(map(int, r)) for r in rows]
    m = len(M)
    for col in range(m):
        piv = next(r for r in range(col, m) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, m):
            while M[r][col] != 0:
                q = M[col][col] // M[r][col]
                M[col] = [a - q * b for a, b in zip(M[col], M[r])]
                M[col], M[r] = M[r], M[col]
        if M[col][col] < 0:
            M[col] = [-a for a in M[col]]
    return M


def hnf_reduce(c, H):
    c = list(c)
    for i in range(len(H)):
        q = c[i] // H[i][i]
        if q:
            c = [a - q * b for a, b in zip(c, H[i])]
    return tuple(c)


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def add_vec(x, y):
    return tuple(a + b for a, b in zip(x, y))


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


def f2_rref(words):
    rows = [list(w) for w in sorted(words, reverse=True) if any(w)]
    basis, pivots = [], []
    for r in rows:
        r = r[:]
        for b, pv in zip(basis, pivots):
            if r[pv]:
                r = [(a + c) % 2 for a, c in zip(r, b)]
        if any(r):
            basis.append(r)
            pivots.append(next(i for i, a in enumerate(r) if a))
    return basis, pivots


def make_lattice(in_lat, basis_rows):
    det, Binv = mat_det_inv(basis_rows)
    lat = {"in": in_lat, "B": basis_rows, "det": det, "Binv": Binv}

    def coords(x):
        c = vec_mat(x, Binv)
        assert all(v.denominator == 1 for v in c), "kein Gittervektor"
        return tuple(int(v) for v in c)

    A = [coords(add_vec(b, J_vec(b))) for b in basis_rows]
    H = row_hnf(A)
    lat["coords"] = coords
    lat["A"] = A
    lat["H"] = H
    lat["label"] = lambda x: hnf_reduce(coords(x), H)
    return lat


def constrA_lattice(code):
    cb, pivots = f2_rref(code)
    rows = [tuple(r) for r in cb]
    rows += [tuple(2 if i == j else 0 for i in range(8))
             for j in range(8) if j not in pivots]
    return make_lattice(lambda x: tuple(v % 2 for v in x) in code, rows)


def constrA_roots(code):
    return [x for x in itertools.product(range(-2, 3), repeat=8)
            if sum(v * v for v in x) == 4
            and tuple(v % 2 for v in x) in code]


def label_group(lat):
    reps = {hnf_reduce((0,) * 8, lat["H"]): (0,) * 8}
    frontier = [(0,) * 8]
    while frontier:
        v = frontier.pop()
        for b in lat["B"]:
            w = add_vec(v, b)
            l = lat["label"](w)
            if l not in reps:
                reps[l] = w
                frontier.append(w)
    return reps


def family_anchor_basis(lat, reps, zero_label, sig_label_fn):
    fixed_labels = [lb for lb in reps if sig_label_fn(lb) == lb]
    fam_basis = None
    for lb in reps:
        if lb == zero_label or sig_label_fn(lb) == lb:
            continue
        o1 = lb
        o2 = sig_label_fn(lb)
        o3 = sig_label_fn(o2)
        s = lat["label"](add_vec(add_vec(reps[o1], reps[o2]), reps[o3]))
        if s == zero_label:
            continue
        span3 = set()
        for bits in itertools.product((0, 1), repeat=3):
            w = (0,) * 8
            for bit, l2 in zip(bits, (o1, o2, o3)):
                if bit:
                    w = add_vec(w, reps[l2])
            span3.add(lat["label"](w))
        if len(span3) != 8:
            continue
        anchor = next(l2 for l2 in fixed_labels
                      if l2 != zero_label and l2 not in span3)
        fam_basis = (o1, o2, o3, anchor, s)
        break
    assert fam_basis is not None
    o1, o2, o3, anc, fsum = fam_basis
    bits_of = {}
    for bits in itertools.product((0, 1), repeat=4):
        v = (0,) * 8
        for bit, l2 in zip(bits, (o1, o2, o3, anc)):
            if bit:
                v = add_vec(v, reps[l2])
        bits_of[lat["label"](v)] = bits
    return fam_basis, bits_of


def s4_gaussian_grading(qstar):
    section("S4: Gaussian grading -- 240 roots = 80 + 160, 60 lines = "
            "20 + 40 over the Arf shells (v752 machinery, read-only)")
    all_placements = set()
    for p in itertools.permutations(range(8)):
        all_placements.add(code_image(C_NAIVE, p))
    both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
                if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
    CSTAR = [c for c in both_inv if W0246 in c][0]
    ROOTS = constrA_roots(CSTAR)
    LAT = constrA_lattice(CSTAR)
    REPS = label_group(LAT)
    ZERO = LAT["label"]((0,) * 8)
    census = Counter(LAT["label"](r) for r in ROOTS)

    def sig_label(lb):
        return LAT["label"](sig_vec(REPS[lb]))

    FAM, BITS = family_anchor_basis(LAT, REPS, ZERO, sig_label)
    check("S4.1 v752 machinery reproduced: 240 roots, 15 nonzero classes "
          "x 16, zero class empty (read-only rebuild)",
          len(ROOTS) == 240 and len(census) == 15
          and sorted(census.values()) == [16] * 15 and ZERO not in census,
          kill="K5")

    def shell_of_label(lb):
        return qstar[WIDX[BITS[lb]]]           # 0 = 5bar shell, 1 = 10

    root_split = Counter(shell_of_label(LAT["label"](r)) for r in ROOTS)
    check("S4.2 ROOT GRADING: 240 = %d (5bar shell, 5 classes x 16) + "
          "%d (10 shell, 10 classes x 16) == 80 + 160; matches the "
          "scheme orthogonality diag(16,160,80) of tfpt_1 Theorem 2 "
          "(fingerprint)" % (root_split[0], root_split[1]),
          root_split[0] == 80 and root_split[1] == 160, kill="K5")

    # mu4-lines: {r, Jr, -r, -Jr}; J free of order 4 (v700/v629)
    root_set = set(ROOTS)
    ok_J = all(J_vec(r) in root_set for r in ROOTS)
    lines = set()
    ok_free = True
    ok_pure = True
    for r in ROOTS:
        orbit = (r, J_vec(r), tuple(-a for a in r),
                 tuple(-a for a in J_vec(r)))
        if len(set(orbit)) != 4:
            ok_free = False
        if len({LAT["label"](x) for x in orbit}) != 1:
            ok_pure = False
        lines.add(frozenset(orbit))
    per_class = Counter()
    line_shell = Counter()
    for L in lines:
        lb = LAT["label"](next(iter(L)))
        per_class[lb] += 1
        line_shell[shell_of_label(lb)] += 1
    check("S4.3 LINE GRADING: J maps roots to roots, free of order 4; "
          "%d lines (== 60 = 240/4, v700), each line CLASS-PURE, 4 per "
          "class; 60 = %d (5bar shell) + %d (10 shell) == 20 + 40"
          % (len(lines), line_shell[0], line_shell[1]),
          ok_J and ok_free and ok_pure and len(lines) == 60
          and set(per_class.values()) == {4}
          and line_shell[0] == 20 and line_shell[1] == 40, kill="K5")

    print("    TYPED: Arf/cut grading of root classes -- explicitly NOT "
          "a matter split;")
    print("    the code->matter reading is ROOTCLASS-MIXED (v775), dead "
          "at root level.")


# ======================================================================
# C -- must-fail controls
# ======================================================================
def c_controls(qstar):
    section("C: must-fail controls")
    # C1: mutated cut map breaks the quadratic-identity census
    def delta_bad(x):
        out = list(delta(x))
        out[0] = x[0]               # edge (0,1) reads x_0 alone
        return tuple(out)

    n_fail_q = sum(1 for v in W16
                   if wt(delta_bad(iota(v))) % 2 == 1
                   or qstar[WIDX[v]] != (wt(delta_bad(iota(v))) // 2) % 2)
    check("C1 CONTROL FIRES: the mutated cut map (edge (0,1) -> x_0) "
          "breaks the quadratic-identity census on %d > 0 of the 16 "
          "words" % n_fail_q, n_fail_q > 0)

    # C2: odd words break the isometry exactly on odd x odd pairs
    f2_5 = list(itertools.product((0, 1), repeat=5))
    fails = [(x, y) for x in f2_5 for y in f2_5
             if sum(a * b for a, b in zip(delta(x), delta(y))) % 2
             != sum(a * b for a, b in zip(x, y)) % 2]
    ok_pattern = all(wt(x) % 2 == 1 and wt(y) % 2 == 1 for x, y in fails)
    check("C2 CONTROL FIRES: over all 1024 pairs of F2^5 the isometry "
          "fails on exactly %d == 256 = 16 x 16 pairs, all odd x odd "
          "(correction term (sum x)(sum y))" % len(fails),
          len(fails) == 256 and ok_pattern)

    # C3: the flip-weight-2 relation (Clebsch complement) has a
    # different shell split
    ceven = sorted(iota(v) for v in W16)

    def flip2(x, y):
        return wt(xor4or5(x, y)) == 2

    split2 = shell_split(ceven, flip2)
    check("C3 CONTROL FIRES: flip-weight-2 (Clebsch complement "
          "SRG(16,10,6,6)) gives shell split %s != (5, 0, 0, 20, 15)"
          % (split2,), split2 != (5, 0, 0, 20, 15))

    # C4: scrambled Clebsch vertices break the partition
    w2 = iota((1, 1, 0, 0))         # a wt-2 word
    w4 = iota((1, 1, 0, 1))         # a wt-4 word (iota adds parity bit)
    assert wt(w2) == 2 and wt(w4) == 4

    def swapped(x):
        if x == w2:
            return w4
        if x == w4:
            return w2
        return x

    def adj_scr(x, y):
        return clebsch_adj(swapped(x), swapped(y))

    split_scr = shell_split(ceven, adj_scr)
    check("C4 CONTROL FIRES: transposing one wt-2 with one wt-4 vertex "
          "scrambles the split to %s != (5, 0, 0, 20, 15)"
          % (split_scr,), split_scr != (5, 0, 0, 20, 15))


# ======================================================================
def main():
    print("=" * 78)
    print("CARRIER.CUTCODE.01 -- the Arf split as the cut classification "
          "of K5")
    print("=" * 78, flush=True)
    qstar = s0_qstar()
    ceven = s1_cut_map(qstar)
    five, ten, star_of, duad_of = s2_cut_census(qstar)
    s3_clebsch(ceven, ten, duad_of)
    s4_gaussian_grading(qstar)
    c_controls(qstar)

    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    core_kills = [k for k in KILLS if k in ("K1", "K2", "K3", "K4")]
    grading_kills = [k for k in KILLS if k == "K5"]
    print("%d/%d checks passed" % (n_pass, n_all))
    if not controls_ok:
        verdict = "TEST-VOID"
        print("VERDICT: TEST-VOID -- a must-fail control does not fire; "
              "the test measures nothing.")
    elif core_kills:
        verdict = "CUTCODE-DEAD"
        print("VERDICT: CUTCODE-DEAD -- core kills fired: %s"
              % sorted(set(core_kills)))
    elif grading_kills:
        verdict = "CUTCODE-PARTIAL"
        print("VERDICT: CUTCODE-PARTIAL -- cut map + census + Clebsch "
              "shells exact, but the Gaussian grading (S4) failed.")
    else:
        verdict = "CUTCODE-EXACT"
        print("VERDICT: CUTCODE-EXACT -- delta isometric + quadratic "
              "(q* = half cut weight), the Arf split 16 = 1 + 5bar + 10 "
              "IS the cut classification (0|5) + (1|4) + (2|3), the "
              "Clebsch 40 edges grade 5 + 20 + 15 over the Arf shells "
              "with within-10 = Petersen (isomorphism census 120), and "
              "the 240 roots / 60 mu4-lines grade 80 + 160 / 20 + 40 -- "
              "typed as Arf/cut grading, NOT a matter split "
              "(ROOTCLASS-MIXED, v775).")
    print("Verdict enum: %s" % verdict)
    print("Runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
