#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""flavor_graph_filtration_probe -- FLAVOR.GRAPH.FILTRATION.01 (K5 round).

HYPOTHESIS [H neu] (frozen before running): the three corpus flavor
matrices Q, K, L = K + Q are three levels of ONE incidence compiler on
the F|W = 3|2 slot geometry (Cut -> Incidence -> Code completion):

  Q row budgets (4,5,6)   = (|E(K5) \\ E(K_{3,2})|, |V(K5)|, |E(K_{3,2})|)
  K row budgets (6,9,10)  = (|E(K_{3,2})|, |E(L(K_{3,2}))|, |E(K5)|),
                            L(K_{3,2}) = triangular prism
  L row budgets (10,14,16) = (|E(K5)|, #wt-4 words of H8, |H8|),
                            H8 = extended Hamming [8,4,4]

DEPLOYED MATRICES (corpus, verification/ -- the objects under test):
  Q = [[3,1,0],[3,2,0],[3,2,1]]   (v11_unique_KQ.py, v37_plucker_anchor.py)
  K = [[4,2,0],[4,3,2],[5,3,2]]   (v11_unique_KQ.py, v12_mass_generation_polynomials.py)
  L = K + Q = [[7,3,0],[7,5,2],[8,5,3]]
      (v37_plucker_anchor.py "L = K + Q"; v4_flavor_matrix.py L = R + 6W;
       tfpt_2_standard_model.tex l.1276; ledger FLAV.PENCIL.01)
The corpus budgets are exact compiler data: v11 proves Q and K are the
UNIQUE nonneg-integer 3x3 matrices with those row sums, column sums,
characteristic polynomial and monotone rows.  Row sums re-derived here.

THE DECISIVE BAR (user's own, frozen): row sums alone do NOT count.
The test is whether the MATRIX ENTRIES can be reconstructed from the
corresponding incidence operators via a FINITE, PREDECLARED list of
structurally motivated candidate maps.  NO fitting: the candidate list
below is frozen before any comparison is executed, and a discriminating
control (exhaustive false-positive census over ALL nonneg-integer
matrices with the same row sums) verifies the candidate set is not
vacuously flexible.

FROZEN CANDIDATE LIST (motivations documented; nothing added after
first run):

  Slot geometry: V = F u W, F = {f0,f1,f2}, W = {w0,w1} (indices
  0,1,2 | 3,4).  Objects per level ("types" = rows, in ascending-budget
  order = the deployed row order):
    Q level: T1 = non-cut edges of K5 (4: E(K3) u E(K2)),
             T2 = vertices of K5 (5), T3 = cut edges = E(K_{3,2}) (6).
    K level: T1 = cut edges (6), T2 = prism edges = length-2 paths of
             K_{3,2}, represented by their 3-vertex support (9),
             T3 = E(K5) (10).
    L level: T1 = E(K5) (10), T2 = wt-4 words of H8 (14),
             T3 = all words of H8 (16).

  (A) FLAG/SHELL CLASSIFIER CENSUS chi_S(x) = |x ^ S| in {0,1,2}
      for S one of the 11 S3xS2-orbit representatives of nonempty
      subsets of V (sizes (a,b), a <= 3 f's, b <= 2 w's).  Motivation:
      the only structural way to get non-S3-symmetric 3x3 matrices from
      the slot geometry is a symmetry-breaking flag S; chi_S is the
      incidence count with that flag ("distance shell" around S).
      Candidate matrix M[i][j] = #{type-i objects x : chi_S(x) = j}.
      A classifier is dropped for a level if any object has |x^S| > 2
      (more than 3 shells -- no 3x3 census exists).
      For the L level, word rows need a word classifier (frozen list):
        w-wt : weight/4 in {0,1,2}  (the code's own weight filtration)
        w-p01: |supp ^ {0,1}|       (first J-pair of the corpus pairing
                                     (0,1)(2,3)(4,5)(6,7), v752)
        w-c0 : |supp ^ {0}|         (single marked coordinate)
      An L-level (A) candidate = (chi_S for the edge row) x (word
      classifier for the two word rows) -- H neu itself mixes the two
      domains at the code level, so mixed candidates are forced.
  (B) OPERATOR QUOTIENTS / RESTRICTIONS (the task-predeclared list):
      - F-block restrictions of the 5x5 vertex operators A(K5),
        A(K_{3,2}), A(K3 u K2), cut-incidence Gram N N^T, Laplacian
        L(K5); motivation: families = the F part of the carrier.
      - Equitable-partition quotients of the prism (= C6(2,3), the
        hexagon circulant): fiber partition {(fi,w0),(fi,w1)} (the S3
        axis) and antipodal partition {v, v+3} (the C6/hexagon axis),
        both for the adjacency and the distance-2 matrix, both as
        per-vertex neighbor counts (equitable quotient) and as total
        inter-class edge counts.
      - Distance-shell sums of K_{3,2} from the F side (3x3: shells
        d = 0,1,2 from each fi, counted on V).

  COMPARISON RULE (frozen): entry-exact integer equality of the full
  3x3 matrix.  Row order is FIXED by the budget identification
  (ascending budgets).  Column order: the generation axis is not
  predeclared by [H neu], so all 6 column permutations are allowed,
  applied uniformly to the whole matrix.  No transpose (rows = types is
  part of the hypothesis), no scaling, no entry shifts.  Per-row
  matches are recorded separately (fingerprint typing), but only
  full-matrix matches count toward reconstruction.

CONTROLS (must fire, frozen):
  C1 scrambled budgets: every non-identity permutation of each graph
     count triple differs from the deployed row-sum triple.
  C2 wrong split 4|1: cut K_{4,1} has 4 edges (not 6), its line graph
     is K4 with 6 edges (not 9), non-cut = 6 (not 4) -- the Q and K
     identifications break.  Wrong code: the non-extended Hamming [7,4]
     has 7 wt-4 words (not 14) -- the L identification breaks.
  C3 discriminating control: EXHAUSTIVE enumeration of all nonneg-
     integer 3x3 matrices with the deployed row sums per level; the
     fraction matching ANY frozen candidate (same 6-perm allowance)
     must be < 5% -- otherwise the census is vacuous (TEST-VOID).

VERDICTS (frozen): FILTRATION-ENTRIES-EXACT (all three levels entry-
reconstruct) / FILTRATION-PARTIAL (some but not all; named exactly) /
FILTRATION-FINGERPRINT-ONLY (budgets are exact graph counts but no
frozen candidate reproduces any full matrix) / TEST-VOID (a control
does not fire).

FENCES: matrix-structure archaeology only -- no mass/physics claims.
FIREWALL: experiments/tfpt-discovery probe; deterministic (no RNG);
pure Python integers; writes nothing; touches no verification/, paper,
ledger or website surface.
"""

import itertools
from collections import Counter

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ---------------------------------------------------------------- helpers
def mat_rows(M):
    return [sum(r) for r in M]


def mat_cols(M):
    return [sum(M[i][j] for i in range(3)) for j in range(3)]


def charpoly3(M):
    """(tr, sum of principal 2x2 minors, det) of an integer 3x3."""
    tr = M[0][0] + M[1][1] + M[2][2]
    m2 = (M[1][1] * M[2][2] - M[1][2] * M[2][1]
          + M[0][0] * M[2][2] - M[0][2] * M[2][0]
          + M[0][0] * M[1][1] - M[0][1] * M[1][0])
    det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
           - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
           + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return (tr, m2, det)


def col_perm_images(M):
    """All 6 column permutations of M, as 9-tuples."""
    out = set()
    for p in itertools.permutations(range(3)):
        out.add(tuple(M[i][p[j]] for i in range(3) for j in range(3)))
    return out


def as9(M):
    return tuple(M[i][j] for i in range(3) for j in range(3))


# ================================================================== P0
section("P0: the deployed corpus matrices (v11/v37/v4) -- re-derived")

Q = [[3, 1, 0], [3, 2, 0], [3, 2, 1]]
K = [[4, 2, 0], [4, 3, 2], [5, 3, 2]]
L = [[K[i][j] + Q[i][j] for j in range(3)] for i in range(3)]

check("P0.1 L = K + Q = [[7,3,0],[7,5,2],[8,5,3]] (v37/v4 identical: "
      "L = R + 6W with R = v4 residue matrix)",
      L == [[7, 3, 0], [7, 5, 2], [8, 5, 3]])

check("P0.2 row budgets: Q (4,5,6), K (6,9,10), L (10,14,16); column "
      "budgets Q (9,5,1), K (13,8,4), L (22,13,5)",
      mat_rows(Q) == [4, 5, 6] and mat_rows(K) == [6, 9, 10]
      and mat_rows(L) == [10, 14, 16]
      and mat_cols(Q) == [9, 5, 1] and mat_cols(K) == [13, 8, 4]
      and mat_cols(L) == [22, 13, 5])

check("P0.3 budget additivity of the filtration: (4,5,6) + (6,9,10) = "
      "(10,14,16) level-wise (Cut + Incidence = Code)",
      [4 + 6, 5 + 9, 6 + 10] == [10, 14, 16])


def enumerate_unique(rowsums, colsums, chi):
    """v11 enumeration, pure integers: all nonneg-int 3x3 with given
    row/col sums, char poly (tr, minor2, det) = chi, monotone rows."""
    sols = []
    r0, r1, r2 = rowsums
    c0, c1, c2 = colsums
    for a in range(r0 + 1):
        for b in range(r0 - a + 1):
            c = r0 - a - b
            for d in range(r1 + 1):
                for e in range(r1 - d + 1):
                    f = r1 - d - e
                    g, h, i = c0 - a - d, c1 - b - e, c2 - c - f
                    if g < 0 or h < 0 or i < 0 or g + h + i != r2:
                        continue
                    if not (a >= b >= c and d >= e >= f and g >= h >= i):
                        continue
                    M = [[a, b, c], [d, e, f], [g, h, i]]
                    if charpoly3(M) == chi:
                        sols.append(M)
    return sols


# chi_Q = (t-1)(t^2-5t+3) = t^3 - 6t^2 + 8t - 3 -> (tr, m2, det) = (6, 8, 3)
# chi_K = (t-1)(t^2-8t+4) = t^3 - 9t^2 + 12t - 4 -> (9, 12, 4)
Qsol = enumerate_unique((4, 5, 6), (9, 5, 1), (6, 8, 3))
Ksol = enumerate_unique((6, 9, 10), (13, 8, 4), (9, 12, 4))
check("P0.4 v11 uniqueness re-derived (pure int): Q and K are the "
      "unique matrices with their budgets + charpoly + monotone rows",
      Qsol == [Q] and Ksol == [K])

# ================================================================== P1
section("P1: budget identifications -- the graph counts (frozen, exact)")

F = (0, 1, 2)
W = (3, 4)
V5 = F + W

E_K5 = [frozenset(e) for e in itertools.combinations(V5, 2)]
E_CUT = [frozenset((f, w)) for f in F for w in W]           # K_{3,2}
E_NONCUT = [e for e in E_K5 if e not in E_CUT]              # K3 u K2
VERTS = [frozenset((v,)) for v in V5]

check("P1.1 Q budgets: |noncut| = 4 = |E(K3)|+|E(K2)| = 3+1, |V| = 5, "
      "|E(K_{3,2})| = 6, |E(K5)| = 10 = 4+6",
      len(E_NONCUT) == 4 and len(VERTS) == 5 and len(E_CUT) == 6
      and len(E_K5) == 10)

# prism = line graph of K_{3,2}: vertices = cut edges, adjacency = share
# an endpoint; prism edges represented by the 3-vertex support of the
# length-2 path they encode.
PRISM_V = list(E_CUT)
PRISM_ADJ = {(a, b) for a in range(6) for b in range(6)
             if a != b and PRISM_V[a] & PRISM_V[b]}
PRISM_E_IDX = [(a, b) for a in range(6) for b in range(a + 1, 6)
               if (a, b) in PRISM_ADJ]
PRISM_E = [PRISM_V[a] | PRISM_V[b] for a, b in PRISM_E_IDX]

deg = Counter()
for a, b in PRISM_E_IDX:
    deg[a] += 1
    deg[b] += 1
check("P1.2 L(K_{3,2}) has 6 vertices, 9 edges, 3-regular; edge "
      "supports are 9 distinct 3-sets (6 sharing a w, 3 sharing an f)",
      len(PRISM_V) == 6 and len(PRISM_E) == 9
      and all(deg[a] == 3 for a in range(6))
      and len(set(map(frozenset, PRISM_E))) == 9
      and sum(1 for s in PRISM_E if len(s & set(W)) == 1) == 6
      and sum(1 for s in PRISM_E if len(s & set(W)) == 2) == 3)


def graphs_isomorphic(adj1, adj2, n):
    for p in itertools.permutations(range(n)):
        if all(((p[a], p[b]) in adj2) == ((a, b) in adj1)
               for a in range(n) for b in range(n) if a != b):
            return True
    return False


# triangular prism K3 x K2 and hexagon circulant C6(2,3)
PRISM_REF = {(a, b) for a in range(6) for b in range(6) if a != b
             and ((a % 3 == b % 3) or (a // 3 == b // 3
                                       and (a - b) % 3 in (1, 2)))}
C6_23 = {(a, b) for a in range(6) for b in range(6)
         if (a - b) % 6 in (2, 3, 4)}
check("P1.3 L(K_{3,2}) isomorphic to the triangular prism K3 x K2 AND "
      "to the hexagon circulant C6(2,3) (brute force over S6)",
      graphs_isomorphic(PRISM_ADJ, PRISM_REF, 6)
      and graphs_isomorphic(PRISM_ADJ, C6_23, 6))

check("P1.4 K budgets: (|E(K_{3,2})|, |E(prism)|, |E(K5)|) = (6,9,10)",
      (len(E_CUT), len(PRISM_E), len(E_K5)) == (6, 9, 10))

# H8 = extended Hamming [8,4,4] (generator = v752 G_NAIVE)
G8 = [(1, 0, 0, 0, 0, 1, 1, 1),
      (0, 1, 0, 0, 1, 0, 1, 1),
      (0, 0, 1, 0, 1, 1, 0, 1),
      (0, 0, 0, 1, 1, 1, 1, 0)]
H8 = sorted(set(tuple(sum(m[k] * G8[k][j] for k in range(4)) % 2
                      for j in range(8))
                for m in itertools.product((0, 1), repeat=4)))
WT = Counter(sum(w) for w in H8)
H8_set = set(H8)
selfdual = all(sum(a * b for a, b in zip(u, v)) % 2 == 0
               for u in H8 for v in H8)
check("P1.5 H8: 16 words, weight enumerator 1 + 14 x^4 + x^8 "
      "(doubly even, self-orthogonal = self-dual at dim 4)",
      len(H8) == 16 and WT == Counter({0: 1, 4: 14, 8: 1}) and selfdual)

W4 = [w for w in H8 if sum(w) == 4]
check("P1.6 L budgets: (|E(K5)|, #wt-4 words, |H8|) = (10,14,16)",
      (len(E_K5), len(W4), len(H8)) == (10, 14, 16))

# ================================================================== P2
section("P2: THE ENTRY RECONSTRUCTION -- frozen candidate census")

# ---- (A) flag classifiers: 11 S3xS2 orbit representatives ------------
FLAGS = []
for a in range(4):
    for b in range(3):
        if a + b == 0:
            continue
        FLAGS.append(("S(%df,%dw)" % (a, b),
                      frozenset(list(F[:a]) + list(W[:b]))))

TYPES = {
    "Q": [("noncut", E_NONCUT), ("vertex", VERTS), ("cut", E_CUT)],
    "K": [("cut", E_CUT), ("prismE", PRISM_E), ("K5E", E_K5)],
}
L_EDGE_ROW = ("K5E", E_K5)

WORD_CLASSIFIERS = [
    ("w-wt", lambda w: sum(w) // 4),
    ("w-p01", lambda w: w[0] + w[1]),
    ("w-c0", lambda w: w[0]),
]


def census_row(objs, chi):
    """(n0, n1, n2) of classifier values; None if any value > 2."""
    row = [0, 0, 0]
    for x in objs:
        v = chi(x)
        if v > 2:
            return None
        row[v] += 1
    return row


def flag_candidates(level):
    """All valid (A) candidates for a level, as (name, matrix)."""
    out = []
    if level in ("Q", "K"):
        for fname, S in FLAGS:
            rows = [census_row(objs, lambda x: len(x & S))
                    for _, objs in TYPES[level]]
            if all(r is not None for r in rows):
                out.append(("chi_" + fname, rows))
    else:  # L: edge row via chi_S, word rows via word classifier
        for fname, S in FLAGS:
            erow = census_row(L_EDGE_ROW[1], lambda x: len(x & S))
            if erow is None:
                continue
            for wname, wchi in WORD_CLASSIFIERS:
                r2 = census_row(W4, wchi)
                r3 = census_row(H8, wchi)
                if r2 is None or r3 is None:
                    continue
                out.append(("chi_%s x %s" % (fname, wname),
                            [erow, r2, r3]))
    return out


# ---- (B) operator quotients / restrictions ---------------------------
def adj_matrix(edges, n=5):
    A = [[0] * n for _ in range(n)]
    for e in edges:
        a, b = sorted(e)
        A[a][b] = A[b][a] = 1
    return A


A5 = adj_matrix(E_K5)
Acut = adj_matrix(E_CUT)
Anc = adj_matrix(E_NONCUT)
NNt = [[sum((v in e) * (u in e) for e in E_CUT) for u in V5] for v in V5]
L5 = [[(4 if i == j else 0) - A5[i][j] for j in range(5)] for i in range(5)]


def f_block(M):
    return [[M[i][j] for j in range(3)] for i in range(3)]


def quotient(adj_pairs, parts, mode):
    """3x3 quotient of a 6-vertex graph under a 3-part partition.
    mode 'eq': per-vertex neighbor counts (requires equitability);
    mode 'sum': total adjacency count between parts."""
    Mq = [[0] * 3 for _ in range(3)]
    for pi, P in enumerate(parts):
        for pj, Qp in enumerate(parts):
            counts = [sum(1 for b in Qp if (a, b) in adj_pairs) for a in P]
            if mode == "eq":
                if len(set(counts)) != 1:
                    return None
                Mq[pi][pj] = counts[0]
            else:
                Mq[pi][pj] = sum(counts)
    return Mq


# prism partitions: fibers (share the same f) and C6-antipodal pairs
fiber_parts = [[a for a in range(6) if sorted(PRISM_V[a] & set(F))[0] == f]
               for f in F]
DIST2 = {(a, b) for a in range(6) for b in range(6)
         if a != b and (a, b) not in PRISM_ADJ}
# The complement of the prism is a 6-cycle (each vertex has exactly two
# distance-2 vertices), so the hexagon-axis 3-pair partitions are the
# perfect matchings of that 6-cycle -- there are exactly 2.  (The C6
# rotation pairing {i, i+3} of C6(2,3) is a matching EDGE of the prism
# and coincides with the fiber partition, already listed.)
comp_edges = [(a, b) for a in range(6) for b in range(a + 1, 6)
              if (a, b) in DIST2]
hex_matchings = []
for combo in itertools.combinations(comp_edges, 3):
    verts = [v for e in combo for v in e]
    if len(set(verts)) == 6:
        hex_matchings.append([list(e) for e in combo])

OPERATOR_CANDIDATES = [
    ("A(K5)|F", f_block(A5)),
    ("A(K32)|F", f_block(Acut)),
    ("A(K3uK2)|F", f_block(Anc)),
    ("NN^T|F (cut Gram)", f_block(NNt)),
    ("Lap(K5)|F", f_block(L5)),
]
PART_LIST = [("fiber", fiber_parts)] + [
    ("hexmatch%d" % k, m) for k, m in enumerate(hex_matchings)]
for pname, parts in PART_LIST:
    for gname, g in (("A(prism)", PRISM_ADJ), ("D2(prism)", DIST2)):
        for mode in ("eq", "sum"):
            Mq = quotient(g, parts, mode)
            if Mq is not None:
                OPERATOR_CANDIDATES.append(
                    ("%s/%s[%s]" % (gname, pname, mode), Mq))
# distance shells of K_{3,2} from the F side: row f = (#V at dist 0,1,2)
dshell = []
for f in F:
    row = [0, 0, 0]
    for v in V5:
        d = 0 if v == f else (1 if frozenset((f, v)) in E_CUT else 2)
        row[d] += 1
    dshell.append(row)
OPERATOR_CANDIDATES.append(("distshell(K32,F)", dshell))

check("P2.0 candidate machinery: fiber partition 3x2 valid, prism "
      "complement is a 6-cycle with exactly 2 perfect matchings "
      "(hexagon-axis partitions), %d operator candidates, flag census "
      "sizes Q/K/L = %d/%d/%d (frozen)"
      % (len(OPERATOR_CANDIDATES), len(flag_candidates("Q")),
         len(flag_candidates("K")), len(flag_candidates("L"))),
      all(len(p) == 2 for p in fiber_parts)
      and len(comp_edges) == 6 and len(hex_matchings) == 2)


def full_pool(level):
    """(name, matrix) list: flag census + operator candidates."""
    return flag_candidates(level) + OPERATOR_CANDIDATES


DEPLOYED = {"Q": Q, "K": K, "L": L}
RESULTS = {}
for level in ("Q", "K", "L"):
    pool = full_pool(level)
    target = DEPLOYED[level]
    t9 = as9(target)
    full_matches = []
    # per-row matches (fingerprint typing; any col perm per row)
    row_match = [set(), set(), set()]
    for name, M in pool:
        if t9 in col_perm_images(M):
            full_matches.append(name)
        for i in range(3):
            for p in itertools.permutations(range(3)):
                if [M[i][p[j]] for j in range(3)] == target[i]:
                    row_match[i].add(name)
                    break
    RESULTS[level] = (pool, full_matches, row_match)
    print("  level %s: %d candidates, full-matrix matches: %s"
          % (level, len(pool), full_matches if full_matches else "NONE"))
    for i in range(3):
        nm = sorted(row_match[i])
        print("    row %d %s reconstructed by %d candidate(s)%s"
              % (i + 1, target[i], len(nm),
                 ": " + ", ".join(nm[:4]) + ("..." if len(nm) > 4 else "")
                 if nm else ""))

check("P2.1 census executed on all three levels (frozen pools, "
      "entry-exact comparison, 6 column perms)",
      all(len(RESULTS[lv][0]) > 10 for lv in RESULTS))

recon = {lv: bool(RESULTS[lv][1]) for lv in ("Q", "K", "L")}
print("  entry reconstruction: Q=%s K=%s L=%s"
      % (recon["Q"], recon["K"], recon["L"]))

# ================================================================== P3
section("P3: CONTROLS (must fire)")

count_triples = {"Q": (len(E_NONCUT), len(VERTS), len(E_CUT)),
                 "K": (len(E_CUT), len(PRISM_E), len(E_K5)),
                 "L": (len(E_K5), len(W4), len(H8))}
scramble_ok = True
for lv in ("Q", "K", "L"):
    t = count_triples[lv]
    rs = tuple(mat_rows(DEPLOYED[lv]))
    if t != rs:
        scramble_ok = False
    for p in itertools.permutations(range(3)):
        if p == (0, 1, 2):
            continue
        if tuple(t[p[j]] for j in range(3)) == rs:
            scramble_ok = False
check("P3.1 C1 scrambled budgets: each count triple equals the "
      "deployed row-sum triple in EXACTLY the identity order (all 5 "
      "non-identity permutations differ, all levels)", scramble_ok)

# wrong split 4|1
F4, W1 = (0, 1, 2, 3), (4,)
cut41 = [frozenset((f, w)) for f in F4 for w in W1]
noncut41 = [e for e in E_K5 if e not in cut41]
lg41 = {(a, b) for a in range(4) for b in range(4)
        if a != b and cut41[a] & cut41[b]}
lg41_edges = sum(1 for a in range(4) for b in range(a + 1, 4)
                 if (a, b) in lg41)
check("P3.2 C2 wrong split 4|1: cut has %d edges (not 6), L(K_{4,1}) "
      "= K4 has %d edges (not 9), noncut %d (not 4) -- Q and K "
      "identifications break" % (len(cut41), lg41_edges, len(noncut41)),
      len(cut41) == 4 and lg41_edges == 6 and len(noncut41) == 6
      and (len(noncut41), 5, len(cut41)) != (4, 5, 6)
      and (len(cut41), lg41_edges, 10) != (6, 9, 10))

# wrong code: Hamming [7,4]
G7 = [(1, 0, 0, 0, 0, 1, 1), (0, 1, 0, 0, 1, 0, 1),
      (0, 0, 1, 0, 1, 1, 0), (0, 0, 0, 1, 1, 1, 1)]
H7 = set(tuple(sum(m[k] * G7[k][j] for k in range(4)) % 2
               for j in range(7))
         for m in itertools.product((0, 1), repeat=4))
WT7 = Counter(sum(w) for w in H7)
check("P3.3 C2b wrong code: Hamming [7,4] has weight census %s -- "
      "%d wt-4 words (not 14), the L identification breaks"
      % (dict(sorted(WT7.items())), WT7[4]),
      len(H7) == 16 and WT7[4] != 14)


def compositions(n):
    return [(a, b, n - a - b) for a in range(n + 1)
            for b in range(n - a + 1)]


fp_rates = {}
for lv in ("Q", "K", "L"):
    pool = RESULTS[lv][0]
    cand_images = set()
    for _, M in pool:
        cand_images |= col_perm_images(M)
    rs = mat_rows(DEPLOYED[lv])
    total = hits = 0
    for r0 in compositions(rs[0]):
        for r1 in compositions(rs[1]):
            for r2 in compositions(rs[2]):
                total += 1
                if r0 + r1 + r2 in cand_images:
                    hits += 1
    fp_rates[lv] = (hits, total)
    print("  level %s: %d / %d row-sum-matched matrices hit a candidate "
          "(%.3f%%)" % (lv, hits, total, 100.0 * hits / total))
disc_ok = all(h / t < 0.05 for h, t in fp_rates.values())
check("P3.4 C3 discriminating control: exhaustive false-positive rate "
      "< 5%% on every level (candidate set is not vacuously flexible)",
      disc_ok)

# ============================================================== VERDICT
section("ZUSAMMENFASSUNG / VERDIKT")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
core = all(ok for n, ok in CHECKS if not n.startswith("P3"))
controls = all(ok for n, ok in CHECKS if n.startswith("P3"))

n_recon = sum(recon.values())
if not controls:
    verdict = "TEST-VOID"
elif not core:
    verdict = "FILTRATION-PARTIAL (core check failed -- see FAILs)"
elif n_recon == 3:
    verdict = "FILTRATION-ENTRIES-EXACT"
elif n_recon > 0:
    verdict = ("FILTRATION-PARTIAL (%s reconstruct, %s do not)"
               % ("/".join(lv for lv in "QKL" if recon[lv]),
                  "/".join(lv for lv in "QKL" if not recon[lv])))
else:
    verdict = "FILTRATION-FINGERPRINT-ONLY"

print("entry reconstruction per level: Q=%s K=%s L=%s" %
      (recon["Q"], recon["K"], recon["L"]))
print("VERDICT: %s" % verdict)
if verdict == "FILTRATION-FINGERPRINT-ONLY":
    print("  The row budgets of Q, K, L are EXACT counts of the "
          "K_{3,2}/prism/K5/H8 incidence chain (P1, order-exact per "
          "P3.1), but NO frozen structural candidate reproduces any "
          "full deployed matrix entry-wise.  The identification is an "
          "AUDIT FINGERPRINT at the budget level, not an entry-level "
          "incidence construction.")
print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else "CHECKS FAILED")
raise SystemExit(0 if n_pass == len(CHECKS) else 1)
