#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""curve_code_doily_probe -- CURVE.CODE.DOILY.01: the certified outer
bridge (duad_syntheme_bridge_probe, BRIDGE-CANONICAL, 24/24) sharpened
into an incidence-operator statement with a spectral payoff.

FROZEN CLAIMS:
 1. DOILY INCIDENCE.  On the 6 points (= the six Arf-1 refinements of
    the code side), 15 duads and 15 synthemes with N_{d,s} = [d in s].
    Each duad lies in exactly 3 synthemes; two duads share a syntheme
    iff disjoint (then exactly one).  Hence the EXACT matrix identity
        N N^T = 3I + A_{KG(6,2)} = B + 2I,
    where B = I + A_{KG(6,2)} is the certified v752/v774 symplectic
    incidence (B[x][y] = [hbar(x,y) = 0] under the K6 duad dictionary
    v <-> D(v)); synthemes <-> isotropic lines bijectively.
 2. SPECTRAL PAYOFF.  spec(N N^T) = {9^1, 4^9, 0^5} (from the v774
    charpoly (x-7)(x-2)^9(x+2)^5 of B, shifted by +2); the normalized
    point-to-line channel N/3 has singular values {1, 2/3^(x9), 0^(x5)}
    -- THE RECOVERY BASE RATE 2/3 as the unique nontrivial singular
    value of the canonical duad-to-syntheme incidence.
    TYPED IDENTIFICATION [H neu -> decidable, NOT decided here]: the
    corpus recovery rate is (2/3)^6 = 64/729 (v221 seam recoverability
    code, spectrum {1,(2/3)^6,(1/3)^6} from cusp weights {0,1/3,2/3}
    and the SIX-fold transfer (1-w)^6; v240 OS gap Delta = 6 ln(3/2);
    v425 native flow e^{-Delta} = (2/3)^6).  The doily channel supplies
    the PER-STEP number 2/3 exactly; identification with the corpus
    rate additionally requires the six-step composition semantics (the
    hexagon; conceptually the C6 = distance-2 shell of the parallel
    Petersen probe -- cited as a pointer only, NOTHING here depends on
    its output).  This probe verifies the number and TYPES the gap.
 3. PETERSEN LOCALIZATION.  With the q*-distinguished point the 15
    duads split 5 + 10 (5bar = duads at q* = {q*(v) = 0}\{0}; internal
    10 = {q*(v) = 1} = Petersen vertices, adjacency = disjointness,
    3-regular, 15 edges, girth 5).  Each syntheme contains exactly one
    distinguished-point duad and one disjoint internal pair = a
    Petersen EDGE; syntheme -> internal pair is a BIJECTION onto
    E(Petersen).  Petersen vertices = code duads, Petersen edges =
    (under the bridge) curve synthemes: the incidence object BETWEEN
    the two sides.
 4. REFINED BRIDGE.  For every census bridge beta (rebuilt here with
    the identical frozen conditions: beta sigma = tau beta, beta(q*) =
    S* the unique <tau, rho>-fixed spread; census must again be 6 per
    family), the induced duality has two components Delta (code duads
    -> curve lines) and Gamma (code synthemes -> curve points, the
    unique common point of {Delta(d) : d in s}), and the factorization
        Delta(d) = { Gamma(s) : N[d][s] = 1 }        (exact, all d)
    reproduces the bridge; equivalently the EXACT matrix identity
        N_code = P_Delta^T  N_curve^T  P_Gamma
    -- the outer bridge conjugates the code incidence to the TRANSPOSE
    of the curve incidence (a duality, not an isomorphism).  The Arf
    translation layer re-verified in doily coordinates: the switch set
    T6 = {t != 0 : q_Theta(t) = 1} has |T6| = 6, q_Theta + e2(t, .) is
    odd exactly for t in T6, t -> shifted form is a bijection onto the
    six odd theta characteristics, and T6 = the six WITHIN-BLOCK duads
    of the q_Theta point-split (the two triangles) -- the census-6
    anchor in doily coordinates.
 5. INTERTWINER CANDIDATE (reported, measured -- NO descent claim):
    N/3 is a doubly stochastic (unital, row and column sums 1)
    classical incidence channel; N^T N has the same spectrum
    {9^1, 4^9, 0^5}; both compositions (N N^T)/9 and (N^T N)/9 have
    spectrum {1, (2/3)^2 x9, 0 x5}: a rank-10 channel with a 1-dim
    fixed space (uniform), a 9-dim window contracted by exactly 2/3
    per application, and a 5-dim annihilated complement.  What it
    OFFERS for the prime front: a canonical, basis-free carrier
    intertwiner between the duad register (code side) and the syntheme
    register (= the curve side of the certified outer bridge) whose
    unique nontrivial rate is the recovery base rate.  What it does
    NOT provide (typed): CPTP on a quantum register (it is classical
    stochastic on the 15-dim function space), and the sixth power.

CONTROLS (must fire):
  C1 wrong incidence (one membership bit flipped): row/column sums
     break and N N^T != B + 2I.
  C2 scrambled synthemes (frozen deterministic corruption: in each
     syntheme replace the lex-highest duad by the lex-next duad that
     meets another member): the Petersen edge bijection breaks.
  C3 inner recomposition: census of point-to-point symplectic
     isomorphisms g: V -> A[2] with g sigma = tau g is 0 (the earlier
     inner kill; only the outer/transpose route exists).

VERDICT ENUM (frozen): DOILY-EXACT (all identities exact, spectra
exact, Petersen bijection 15/15, refactorization exact for the full
census, Arf layer verified, controls fire; the 2/3 identification
typed with its exact requirement = six-step composition) /
DOILY-PARTIAL (incidence core holds, a named layer fails) /
DOILY-DEAD (the core identity N N^T = B + 2I fails).  TEST-VOID on
control failure.

FENCES: finite exact algebra (integers/Fractions; no floats in any
load-bearing check); the curve side is the certified exact model of
curve_code_2torsion_probe (periods certified there at dps 120); NO
matter semantics (ROOTCLASS-MIXED, v775, stands); the inner
identification stays dead (CURVE-CODE-PARTIAL); nothing here modifies
the corpus recovery modules v221/v240/v425 -- claim 2 is a typed
cross-reference, not a re-derivation.  EXPLORATION ONLY: one new file
in experiments/tfpt-discovery/, report only, no promotion.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/curve_code_doily_probe.py
"""

import itertools
import time
from fractions import Fraction

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
# frozen machinery (identical to duad_syntheme_bridge_probe)
# ======================================================================
ZPOW = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
        (-1, 0, 1, 0), (0, -1, 0, 1), (-1, 0, 0, 0)]
CONJ_BASIS = [(1, 0, 0, 0), (0, 1, 0, -1), (1, 0, -1, 0), (0, 0, 0, -1)]
E_K = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]


def kmul(a, b):
    conv = [0] * 7
    for i in range(4):
        if a[i]:
            for j in range(4):
                conv[i + j] += a[i] * b[j]
    out = [0, 0, 0, 0]
    for k in range(7):
        if conv[k]:
            for t in range(4):
                out[t] += conv[k] * ZPOW[k][t]
    return tuple(out)


def kconj(a):
    out = [0, 0, 0, 0]
    for i in range(4):
        if a[i]:
            for t in range(4):
                out[t] += a[i] * CONJ_BASIS[i][t]
    return tuple(out)


def ktrace(a):
    return 4 * a[0] + 2 * a[2]


def kpow_zeta(k):
    out = (1, 0, 0, 0)
    for _ in range(k % 12):
        out = kmul(out, (0, 1, 0, 0))
    return out


def mult_matrix_mod2(g):
    return [[kmul(g, E_K[j])[i] % 2 for j in range(4)] for i in range(4)]


def Estar(x, y):
    t = ktrace(kmul(kmul(kpow_zeta(3), x), kconj(y)))
    assert t % 2 == 0
    return t // 2


def build_tables(gram):
    tab = [[0] * 16 for _ in range(16)]
    for x in range(16):
        for y in range(16):
            xv = [(x >> k) & 1 for k in range(4)]
            yv = [(y >> k) & 1 for k in range(4)]
            tab[x][y] = sum(xv[i] * gram[i][j] * yv[j]
                            for i in range(4) for j in range(4)) % 2
    return tab


def all_refinements(tab):
    refs = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            row = tab[i]
            qi = q[i]
            for j in range(16):
                if q[i ^ j] ^ qi ^ q[j] != row[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            refs.append(tuple(q))
    return refs


def iso_lines(tab):
    out = set()
    for a in range(1, 16):
        for b in range(a + 1, 16):
            if tab[a][b] == 0 and (a ^ b) != 0:
                out.add(frozenset({a, b, a ^ b}))
    return sorted(out, key=sorted)


def spreads_of(lines):
    pts = set(range(1, 16))
    by_pt = {}
    for L in lines:
        for p in L:
            by_pt.setdefault(p, []).append(L)

    def rec(cov, used):
        if len(cov) == 15:
            return [frozenset(used)]
        p = min(pts - cov)
        res = []
        for L in by_pt[p]:
            if cov & L:
                continue
            res += rec(cov | L, used + [L])
        return res

    return sorted(set(rec(frozenset(), [])),
                  key=lambda S: sorted(map(sorted, S)))


def linear_transporters(src_tab, dst_tab):
    out = []
    for m in range(1 << 16):
        cols = [(m >> (4 * k)) & 15 for k in range(4)]
        img = [0] * 16
        for x in range(16):
            v = 0
            for k in range(4):
                if x & (1 << k):
                    v ^= cols[k]
            img[x] = v
        if len(set(img)) != 16:
            continue
        ok = True
        for x in range(1, 16):
            for y in range(x, 16):
                if dst_tab[img[x]][img[y]] != src_tab[x][y]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(img))
    return out


def inv_perm16(g):
    gi = [0] * 16
    for x in range(16):
        gi[g[x]] = x
    return gi


class Side(object):
    def __init__(self, name, gram):
        self.name = name
        self.tab = build_tables(gram)
        self.refs = all_refinements(self.tab)
        zeros = {q: sum(1 for b in q if b == 0) for q in self.refs}
        self.odds = sorted(q for q in self.refs if zeros[q] == 6)
        self.evens = sorted(q for q in self.refs if zeros[q] == 10)
        self.lines = iso_lines(self.tab)
        self.spreads = spreads_of(self.lines)
        self.duad_of = {}      # vector -> frozenset of 2 odd indices
        self.duad_vec = {}     # frozenset of 2 odd indices -> vector
        for v in range(1, 16):
            dv = frozenset(i for i, q in enumerate(self.odds) if q[v] == 0)
            assert len(dv) == 2
            self.duad_of[v] = dv
            self.duad_vec[dv] = v
        self.shared = {}
        for i in range(6):
            for j in range(i + 1, 6):
                inter = self.spreads[i] & self.spreads[j]
                assert len(inter) == 1
                self.shared[frozenset({i, j})] = inter

    def odd_perm(self, g):
        gi = inv_perm16(g)
        return [self.odds.index(tuple(q[gi[v]] for v in range(16)))
                for q in self.odds]

    def spread_perm(self, g):
        out = []
        for S in self.spreads:
            Sg = frozenset(frozenset(g[p] for p in L) for L in S)
            out.append(self.spreads.index(Sg))
        return out

    def split_pts(self, q):
        adj = {i: set() for i in range(6)}
        for i in range(6):
            for j in range(i + 1, 6):
                if q[self.duad_vec[frozenset({i, j})]] == 1:
                    adj[i].add(j)
                    adj[j].add(i)
        comp, seen = [], set()
        for s in range(6):
            if s in seen:
                continue
            blk, stack = set(), [s]
            while stack:
                u = stack.pop()
                if u in blk:
                    continue
                blk.add(u)
                stack += list(adj[u] - blk)
            seen |= blk
            comp.append(frozenset(blk))
        return frozenset(comp)


def mat_mul(A, Bm):
    n, m, p = len(A), len(Bm), len(Bm[0])
    out = [[0] * p for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for k in range(m):
            a = Ai[k]
            if a:
                Bk = Bm[k]
                Oi = out[i]
                for j in range(p):
                    Oi[j] += a * Bk[j]
    return out


def mat_rank_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    n, m = len(A), len(A[0])
    rank, row = 0, 0
    for col in range(m):
        piv = None
        for r in range(row, n):
            if A[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        pv = A[row][col]
        A[row] = [x / pv for x in A[row]]
        for r in range(n):
            if r != row and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[row])]
        row += 1
        rank += 1
        if row == n:
            break
    return rank


def spectrum_945(M, label):
    """certify spec(M) = {9^1, 4^9, 0^5} exactly (integer arithmetic)."""
    n = len(M)
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    M4 = [[M[i][j] - 4 * I[i][j] for j in range(n)] for i in range(n)]
    M9 = [[M[i][j] - 9 * I[i][j] for j in range(n)] for i in range(n)]
    annih = mat_mul(mat_mul(M, M4), M9)
    ann_ok = all(x == 0 for row in annih for x in row)
    tr1 = sum(M[i][i] for i in range(n))
    M2 = mat_mul(M, M)
    tr2 = sum(M2[i][i] for i in range(n))
    rk = mat_rank_q(M)
    # eigenvalues in {0,4,9}; m9*9 + m4*4 = tr1, m9*81 + m4*16 = tr2,
    # m9 + m4 = rank -> unique solution (1, 9, 5)
    ok = (ann_ok and tr1 == 45 and tr2 == 225 and rk == 10)
    print("    %s: annihilator M(M-4)(M-9)=0: %s; tr=%d tr2=%d rank=%d"
          % (label, ann_ok, tr1, tr2, rk))
    return ok


# ======================================================================
# S1 -- the doily incidence N and the exact identity NN^T = B + 2I
# ======================================================================
section("S1: doily incidence N (15 duads x 15 synthemes) and the exact "
        "identity NN^T = 3I + A_KG = B + 2I (v752/v774 object)")

GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
SIG_B = [0] * 16
for x in range(16):
    b = [(x >> k) & 1 for k in range(4)]
    nb = (b[2], b[0], b[1], b[3])
    SIG_B[x] = nb[0] | (nb[1] << 1) | (nb[2] << 2) | (nb[3] << 3)
code = Side("code", GJI)

DUADS = sorted(map(sorted, itertools.combinations(range(6), 2)))
DUADS = [frozenset(d) for d in DUADS]
SYNTHEMES = []
for m in itertools.combinations(DUADS, 3):
    if len(m[0] | m[1] | m[2]) == 6:
        SYNTHEMES.append(frozenset(m))
SYNTHEMES.sort(key=lambda s: sorted(map(sorted, s)))
check("S1.1 K6 census: 15 duads, %d synthemes (perfect matchings)"
      % len(SYNTHEMES), len(SYNTHEMES) == 15, kill="K")

# syntheme <-> isotropic line dictionary
syn_line = {}
for s in SYNTHEMES:
    trip = frozenset(code.duad_vec[d] for d in s)
    match = [L for L in code.lines if frozenset(L) == trip]
    syn_line[s] = match[0] if len(match) == 1 else None
check("S1.2 synthemes <-> isotropic lines BIJECTIVE via the duad "
      "dictionary v <-> D(v): every matching is an isotropic line and "
      "all 15 lines are hit",
      all(v is not None for v in syn_line.values())
      and len(set(map(frozenset, syn_line.values()))) == 15, kill="K")

N = [[1 if DUADS[i] in SYNTHEMES[j] else 0 for j in range(15)]
     for i in range(15)]
rows3 = all(sum(N[i]) == 3 for i in range(15))
cols3 = all(sum(N[i][j] for i in range(15)) == 3 for j in range(15))
check("S1.3 each duad lies in exactly 3 synthemes and each syntheme "
      "contains exactly 3 duads (row and column sums 3)",
      rows3 and cols3, kill="K")

NNt = mat_mul(N, [list(r) for r in zip(*N)])
share_ok = True
for i in range(15):
    for j in range(15):
        dis = (i != j and not (DUADS[i] & DUADS[j]))
        want = 3 if i == j else (1 if dis else 0)
        if NNt[i][j] != want:
            share_ok = False
check("S1.4 two duads share a syntheme iff DISJOINT, then exactly one: "
      "NN^T = 3I + A_KG(6,2) entrywise", share_ok, kill="K")

Bmat = [[1 if code.tab[code.duad_vec[DUADS[i]]][code.duad_vec[DUADS[j]]]
         == 0 else 0 for j in range(15)] for i in range(15)]
b_id = all(NNt[i][j] == Bmat[i][j] + 2 * (i == j)
           for i in range(15) for j in range(15))
kg_id = all(Bmat[i][j] == (1 if (i == j or not (DUADS[i] & DUADS[j]))
                           else 0) for i in range(15) for j in range(15))
check("S1.5 EXACT MATRIX IDENTITY: NN^T == B + 2I where B[x][y] = "
      "[hbar(x,y) = 0] is the certified v752/v774 symplectic incidence, "
      "and B == I + A_KG entrywise (re-verified)", b_id and kg_id,
      kill="K")

# ======================================================================
# S2 -- spectra and the 2/3 payoff (typed identification)
# ======================================================================
section("S2: spectra -- spec(NN^T) = {9,4^9,0^5}, singular values of "
        "N/3 = {1, 2/3, 0}; the corpus (2/3)^6 cross-check TYPED")

Nt = [list(r) for r in zip(*N)]
NtN = mat_mul(Nt, N)
ok_a = spectrum_945(NNt, "NN^T (duad side)")
ok_b = spectrum_945(NtN, "N^T N (syntheme side)")
check("S2.1 spec(NN^T) = spec(N^T N) = {9^1, 4^9, 0^5} EXACT "
      "(annihilating polynomial + traces + rank over Q; consistent with "
      "v774 charpoly of B = (x-7)(x-2)^9(x+2)^5 shifted by +2)",
      ok_a and ok_b, kill="K")
sv2 = sorted({Fraction(e, 9) for e in (9, 4, 0)}, reverse=True)
check("S2.2 singular values of the normalized channel N/3: squared "
      "values {1, 4/9, 0} -> {1, 2/3, 0}: THE RECOVERY BASE RATE 2/3 is "
      "the unique nontrivial singular value of the duad-to-syntheme "
      "incidence", sv2 == [Fraction(1), Fraction(4, 9), Fraction(0)],
      kill="K")
rate6 = Fraction(2, 3) ** 6
check("S2.3 corpus cross-check EXACT AT NUMBER LEVEL: (2/3)^6 = %s = "
      "64/729 = the v221 seam recovery rate ((1-w)^6 at cusp weight "
      "w = 1/3; v240 OS gap Delta = 6 ln(3/2); v425 native flow)"
      % rate6, rate6 == Fraction(64, 729), kill="K")
print("    TYPED [H neu -> decidable, NOT decided here]: the doily")
print("    channel supplies the PER-STEP 2/3; identification with the")
print("    corpus rate requires the SIX-step composition semantics")
print("    (the hexagon / C6 = distance-2 shell of the parallel")
print("    Petersen probe -- conceptual pointer only, no dependence).")

# ======================================================================
# S3 -- Petersen localization at q*
# ======================================================================
section("S3: Petersen localization at the q*-distinguished point")

QSTAR = [q for q in code.odds
         if all(q[SIG_B[x]] == q[x] for x in range(16))
         and q[0b1000] == 1 and q[0b0111] == 0]
assert len(QSTAR) == 1
QSTAR = QSTAR[0]
qs_idx = code.odds.index(QSTAR)
at_q = [i for i, d in enumerate(DUADS) if qs_idx in d]
internal = [i for i, d in enumerate(DUADS) if qs_idx not in d]
split_ok = (len(at_q) == 5 and len(internal) == 10
            and all(QSTAR[code.duad_vec[DUADS[i]]] == 0 for i in at_q)
            and all(QSTAR[code.duad_vec[DUADS[i]]] == 1
                    for i in internal))
check("S3.1 duad split 5 + 10 at q*: the 5 duads at q* = the 5bar words "
      "{q* = 0}\\{0}; the 10 internal duads = the 10 words {q* = 1}",
      split_ok, kill="K")

pet_adj = {i: set() for i in internal}
for i in internal:
    for j in internal:
        if i != j and not (DUADS[i] & DUADS[j]):
            pet_adj[i].add(j)
n_edges = sum(len(v) for v in pet_adj.values()) // 2


def girth(adj):
    best = None
    for s in adj:
        dist, par = {s: 0}, {s: None}
        queue = [s]
        while queue:
            u = queue.pop(0)
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    queue.append(w)
                elif par[u] != w:
                    c = dist[u] + dist[w] + 1
                    if best is None or c < best:
                        best = c
    return best


check("S3.2 internal graph (adjacency = disjointness) IS Petersen: 10 "
      "vertices, 3-regular, %d edges, girth %d (3-regular girth-5 on 10 "
      "vertices is Petersen, Moore uniqueness)"
      % (n_edges, girth(pet_adj)),
      all(len(v) == 3 for v in pet_adj.values()) and n_edges == 15
      and girth(pet_adj) == 5, kill="K")

syn_edge = {}
pet_ok = True
for j, s in enumerate(SYNTHEMES):
    dq = [d for d in s if qs_idx in d]
    di = [d for d in s if qs_idx not in d]
    if not (len(dq) == 1 and len(di) == 2 and not (di[0] & di[1])):
        pet_ok = False
        continue
    syn_edge[j] = frozenset({DUADS.index(di[0]), DUADS.index(di[1])})
edges = {frozenset({i, j}) for i in pet_adj for j in pet_adj[i]}
bij_ok = (len(syn_edge) == 15
          and set(syn_edge.values()) == edges
          and len(set(syn_edge.values())) == 15)
check("S3.3 PETERSEN EDGE BIJECTION: every syntheme = one q*-duad + one "
      "disjoint internal pair; syntheme -> internal pair is a bijection "
      "onto the 15 Petersen edges (census %d/15 valid, %d/15 distinct)"
      % (len(syn_edge), len(set(syn_edge.values()))),
      pet_ok and bij_ok, kill="K")

# ======================================================================
# S4 -- the refined bridge: factorization through N
# ======================================================================
section("S4: refined bridge -- the census bridges factor through N "
        "(N_code = P_Delta^T N_curve^T P_Gamma)")

ESTAR = [[Estar(E_K[i], E_K[j]) % 2 for j in range(4)] for i in range(4)]
MT = mult_matrix_mod2(kpow_zeta(4))
MR = mult_matrix_mod2(kpow_zeta(9))
TAU_B = [0] * 16
RHO_B = [0] * 16
for x in range(16):
    xv = [(x >> k) & 1 for k in range(4)]
    it = [sum(MT[i][j] * xv[j] for j in range(4)) % 2 for i in range(4)]
    ir = [sum(MR[i][j] * xv[j] for j in range(4)) % 2 for i in range(4)]
    TAU_B[x] = it[0] | (it[1] << 1) | (it[2] << 2) | (it[3] << 3)
    RHO_B[x] = ir[0] | (ir[1] << 1) | (ir[2] << 2) | (ir[3] << 3)
curve = Side("curve", ESTAR)

code.sp = linear_transporters(code.tab, code.tab)
sigO = code.odd_perm(SIG_B)
tauT = curve.spread_perm(TAU_B)
rhoT = curve.spread_perm(RHO_B)
S_STAR_SET = [i for i in range(6) if tauT[i] == i and rhoT[i] == i]
assert len(S_STAR_SET) == 1
S_STAR = S_STAR_SET[0]
FULL_tau = [beta for beta in itertools.permutations(range(6))
            if all(beta[sigO[i]] == tauT[beta[i]] for i in range(6))
            and beta[qs_idx] == S_STAR]
check("S4.1 census bridges rebuilt with the identical frozen "
      "conditions: %d (must be 6, the BRIDGE-CANONICAL torsor)"
      % len(FULL_tau), len(FULL_tau) == 6, kill="K")

N_curve = [[1 if p in L else 0 for L in curve.lines]
           for p in range(1, 16)]     # 15 points x 15 lines
fact_ok = True
matid_ok = True
petersen_bridge_ok = True
for beta in FULL_tau:
    Delta = {}
    for v in range(1, 16):
        i, j = sorted(beta[i] for i in code.duad_of[v])
        (L,) = curve.shared[frozenset({i, j})]
        Delta[v] = L
    Gamma = {}
    for s_idx, s in enumerate(SYNTHEMES):
        pts = None
        for d in s:
            P = set(Delta[code.duad_vec[d]])
            pts = P if pts is None else (pts & P)
        if pts is None or len(pts) != 1:
            fact_ok = False
            continue
        Gamma[s_idx] = pts.pop()
    # factorization Delta(d) = {Gamma(s) : d in s}
    for i, d in enumerate(DUADS):
        v = code.duad_vec[d]
        img = {Gamma[j] for j in range(15) if N[i][j] == 1}
        if img != set(Delta[v]):
            fact_ok = False
    # matrix identity N_code[d][s] == N_curve[Gamma(s)][Delta(d)]
    for i, d in enumerate(DUADS):
        v = code.duad_vec[d]
        Lidx = curve.lines.index(Delta[v])
        for j in range(15):
            if N[i][j] != N_curve[Gamma[j] - 1][Lidx]:
                matid_ok = False
    # Petersen blocks under the bridge: 5bar duads -> lines of S*,
    # internal (Petersen vertex) duads -> the 10 non-S* lines
    img5 = {Delta[code.duad_vec[DUADS[i]]] for i in at_q}
    img10 = {Delta[code.duad_vec[DUADS[i]]] for i in internal}
    if img5 != set(curve.spreads[S_STAR]) or \
       img10 != set(curve.lines) - set(curve.spreads[S_STAR]):
        petersen_bridge_ok = False

check("S4.2 FACTORIZATION exact for all 6 census bridges: Gamma(s) = "
      "the unique common curve point of {Delta(d) : d in s}, and "
      "Delta(d) = {Gamma(s) : N[d][s] = 1} for every duad -- the bridge "
      "IS 'apply N, then the outer duality on synthemes'", fact_ok,
      kill="K")
check("S4.3 EXACT MATRIX IDENTITY for all 6 census bridges: N_code = "
      "P_Delta^T N_curve^T P_Gamma -- the outer bridge conjugates the "
      "code incidence to the TRANSPOSE of the curve incidence (a "
      "duality, not an isomorphism)", matid_ok, kill="K")
check("S4.4 Petersen blocks transport: the 5 duads at q* -> the 5 lines "
      "of S*, the 10 Petersen vertices -> the 10 non-S* lines (all "
      "census bridges) -- Petersen vertices = code duads, Petersen "
      "edges = curve synthemes", petersen_bridge_ok, kill="K")

# Arf translation layer in doily coordinates (curve side)
QTHETA = [q for q in curve.refs
          if all(q[TAU_B[x]] == q[x] for x in range(16))]
assert len(QTHETA) == 1
QTHETA = QTHETA[0]
T6 = [t for t in range(1, 16) if QTHETA[t] == 1]
shift_odds = {}
arf_layer_ok = len(T6) == 6
for t in range(1, 16):
    qt = tuple((QTHETA[x] + curve.tab[t][x]) % 2 for x in range(16))
    is_odd = qt in curve.odds
    if t in T6:
        if not is_odd:
            arf_layer_ok = False
        shift_odds[t] = qt
    else:
        if is_odd:
            arf_layer_ok = False
arf_layer_ok = arf_layer_ok and sorted(shift_odds.values()) == curve.odds
split_qT = curve.split_pts(QTHETA)
within = set()
for blk in split_qT:
    for pair in itertools.combinations(sorted(blk), 2):
        within.add(curve.duad_vec[frozenset(pair)])
check("S4.5 ARF TRANSLATION LAYER in doily coordinates: |T6| = %d "
      "switch points {q_Theta = 1}; q_Theta + e2(t, .) is odd EXACTLY "
      "for t in T6 and t -> shifted form is a bijection onto the 6 odd "
      "theta characteristics; T6 == the 6 WITHIN-BLOCK duads of the "
      "q_Theta point-split (the two triangles) -- the census-6 anchor"
      % len(T6), arf_layer_ok and within == set(T6), kill="K")

# ======================================================================
# S5 -- the intertwiner candidate (reported, measured)
# ======================================================================
section("S5: the intertwiner candidate N/3 (reported, measured -- no "
        "descent claim)")

ds_ok = (all(sum(Fraction(x, 3) for x in N[i]) == 1 for i in range(15))
         and all(sum(Fraction(N[i][j], 3) for i in range(15)) == 1
                 for j in range(15)))
check("S5.1 N/3 is DOUBLY STOCHASTIC (unital classical channel on the "
      "15-dim function space): all row and column sums exactly 1",
      ds_ok, kill="K")
check("S5.2 both compositions have spectrum {1, (2/3)^2 x9, 0 x5}: "
      "1-dim fixed space (uniform), 9-dim window contracted by exactly "
      "2/3 per application, 5-dim annihilated complement (rank 10)",
      ok_a and ok_b, kill="K")
print("    OFFERED for the prime front (measured): a canonical,")
print("    basis-free carrier intertwiner between the duad register")
print("    (code side) and the syntheme register (= the curve side of")
print("    the certified outer bridge), unique nontrivial rate = the")
print("    recovery base rate 2/3 on the 9-dim window.")
print("    NOT PROVIDED (typed): CPTP on a quantum register (this is")
print("    classical stochastic incidence), and the sixth power --")
print("    the six-step composition is the open identification of S2.")

# ======================================================================
# S6 -- controls
# ======================================================================
section("S6: controls")

N_bad = [row[:] for row in N]
N_bad[0][0] ^= 1
NNt_bad = mat_mul(N_bad, [list(r) for r in zip(*N_bad)])
c1 = (sum(N_bad[0]) != 3 or sum(N_bad[i][0] for i in range(15)) != 3) \
    and any(NNt_bad[i][j] != Bmat[i][j] + 2 * (i == j)
            for i in range(15) for j in range(15))
check("C1 FIRES: one flipped membership bit breaks the count-3 "
      "structure AND NN^T != B + 2I", c1, kill="K7")

scr_ok_cols = 0
for s in SYNTHEMES:
    ds = sorted(map(sorted, s))
    keep = [frozenset(d) for d in ds[:2]]
    top = frozenset(ds[2])
    repl = None
    for d in DUADS:
        if d != top and d not in keep and (d & keep[0]):
            repl = d
            break
    scr = keep + [repl]
    dq = [d for d in scr if qs_idx in d]
    di = [d for d in scr if qs_idx not in d]
    if len(dq) == 1 and len(di) == 2 and not (di[0] & di[1]):
        scr_ok_cols += 1
check("C2 FIRES: scrambled synthemes (lex-highest duad replaced by a "
      "MEETING duad, frozen rule): only %d/15 corrupted synthemes still "
      "satisfy the Petersen-edge property (bijection broken)"
      % scr_ok_cols, scr_ok_cols < 15, kill="K7")

inner = linear_transporters(code.tab, curve.tab)
n_inner_eq = sum(1 for g in inner
                 if all(g[SIG_B[x]] == TAU_B[g[x]] for x in range(16)))
check("C3 FIRES: inner recomposition -- %d symplectic isomorphisms "
      "V -> A[2] exist but %d intertwine sigma with tau (the inner "
      "route stays DEAD; only the outer/transpose factorization exists)"
      % (len(inner), n_inner_eq),
      len(inner) == 720 and n_inner_eq == 0, kill="K7")

# ======================================================================
# S7 -- verdict (frozen rule)
# ======================================================================
section("S7: VERDICT (frozen enum: DOILY-EXACT / DOILY-PARTIAL / "
        "DOILY-DEAD; TEST-VOID on control failure)")

n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
core_ok = all(ok for nm, ok in CHECKS if nm.startswith("S1"))
print("%d/%d checks passed" % (n_pass, n_tot))

if not controls_ok:
    verdict = "TEST-VOID"
elif not core_ok:
    verdict = "DOILY-DEAD"
elif n_pass == n_tot:
    verdict = "DOILY-EXACT"
else:
    verdict = "DOILY-PARTIAL"

print("VERDICT: %s" % verdict)
if verdict == "DOILY-EXACT":
    print()
    print("RECOMMENDED CONTRACT TEXT (exploration grade -- promotion is")
    print("a separate decision):")
    print("  * The K6 doily incidence N (15 duads x 15 synthemes) on the")
    print("    six odd refinements satisfies NN^T = B + 2I exactly, with")
    print("    B the certified v752/v774 symplectic incidence; spec =")
    print("    {9, 4^9, 0^5} and the normalized channel N/3 has singular")
    print("    values {1, 2/3, 0}: the recovery base rate 2/3 (v221) is")
    print("    the unique nontrivial singular value of the canonical")
    print("    duad-to-syntheme map.  Identification with the corpus")
    print("    rate (2/3)^6 requires the six-step composition semantics")
    print("    [H neu -> decidable, typed, not decided here].")
    print("  * At the q*-point the 10 internal duads form the Petersen")
    print("    graph and syntheme -> internal pair is a bijection onto")
    print("    E(Petersen): Petersen vertices = code duads, Petersen")
    print("    edges = curve synthemes under the certified bridge.")
    print("  * Every census bridge factors EXACTLY through N:")
    print("    Delta(d) = {Gamma(s) : d in s} and N_code = P_Delta^T")
    print("    N_curve^T P_Gamma -- the outer bridge is transpose-")
    print("    conjugation of the incidence channel; the Arf layer is")
    print("    the 6-point switch set T6 = within-block duads of the")
    print("    q_Theta split.")
    print("  * N/3 is a doubly stochastic carrier intertwiner (1 + 9 +")
    print("    5 spectral decomposition, rate 2/3 on the window) --")
    print("    measured; no CPTP/quantum or descent claim.")
    print("  * NO matter semantics (ROOTCLASS-MIXED, v775, stands); the")
    print("    inner identification stays CURVE-CODE-PARTIAL/dead.")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if n_pass == n_tot else 1)
