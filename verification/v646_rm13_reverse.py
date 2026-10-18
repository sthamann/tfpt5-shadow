#!/usr/bin/env python3
"""v646 -- E8.RM13REV.01: the RM(1,3) reverse reading -- are compiler
numbers CODE operations?  An honestly TWO-PART answer: the sigma-fixed
syndromes carry the anchor decomposition (1,1,2)/norm 6 exactly (with
the anchor = family sum an equivariance-specific SELECTION, the raw
weights generic for any [8,4,4] placement), while the bytecode
p-sequence p_n = 2 + 2^n has NO code reading (0/11 natural families;
18/27/81 without any hit -- the bingo is buried).

Predecessors (read-only; both promoted as v638_code_semantics.py):
  * code_semantics_kill_probe.py: the UNIQUE equivariant Hamming
    placement C* (invariant under piJ and pisig, one up to anchor
    orientation).
  * code_semantics_stage2_probe.py: C* = RM(1,3) on AG(3,2);
    information bits = one per mu4 pair; syndrome flag 0 < <q> < F2^4
    with quotient = pair pointer (sigma: P0 -> P1 -> P2 cycled, anchor
    P3 = P0+P1+P2 fixed); decode = projection on the single-error
    class; all of it placement-dependent (kill control fired).

REVERSE question: are known compiler computations derivable as CODE
operations instead of merely parallel?

R1  the anchor norm (1,1,2).(1,1,2) = 6
    (a) exact orbit censuses of the 14 weight-4 words under the placed
        symmetry chain Z2 < Z3 < Z6 < P48 < P192 < AGL(3,2); exact
        pattern test against (1,1,2)-combinatorics
        ({1,1,2}, {1,1,4}, {2,2,4}, {2,2,8}, {2,4,8}).
    (b) pair-sector coset-leader weights: for a mu4 pair {2k, 2k+1} the
        nonzero sector syndromes {s(e_2k), s(e_2k+1), q} carry leader
        weights (1,1,2) with norm-square sum 6; sigma fixes EXACTLY the
        anchor sector (P3 = P0+P1+P2 = family sum).  R3 measures how
        much of this is generic [8,4,4] vs equivariance-specific.
R2  bytecode connection p_n = 2 + 2^n (v624s; p1 p2 p3 = 240,
    p4 - p3 = 8, 240 + 8 = 248): tabulate the small code invariants
    (coset-leader census, coset weight distributions, ball volumes,
    Construction-A root counts, sigma/Z6 censuses) and match EXACTLY
    against 2,3,4,6,10,18 / 240,8,248,60,12,27,81; scan natural
    families f(n) for the sequence (4,6,10,18).  Pure number
    coincidences are typed BINGO explicitly.
R3  KILL control (non-equivariant v626 placement + 30-census): what
    survives is a placement-independent code fact (typed as such),
    what dies is equivariance-specific.

Exact integer arithmetic throughout.

FIREWALL: no marker moves; number coincidences stay typed BINGO; the
honest negative (no code reading of the p-sequence) closes a route,
not a gap.  Python-only, counted per GATE.WOLFRAM.02.

PROVENANCE: discovery probe rm13_reverse_probe.py (2026-08-02, 20/20;
R1b exact / R1a + R2 honest negatives / R3 kill control selective).
"""

import itertools
import time
from collections import Counter
from math import comb

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78)


# ------------------------------------------------- codes and placements
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))

PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7)]
ZERO8 = (0,) * 8


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def compose(p, q):
    return tuple(q[p[k]] for k in range(8))


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


Z6 = {tuple(range(8))}
frontier = [tuple(range(8))]
while frontier:
    p = frontier.pop()
    for g in (PI_J, PI_SIG):
        r = compose(g, p)
        if r not in Z6:
            Z6.add(r)
            frontier.append(r)
Z6 = sorted(Z6)
assert len(Z6) == 6

all_placements = set()
for p in itertools.permutations(range(8)):
    all_placements.add(code_image(C_NAIVE, p))
all_placements = sorted(all_placements, key=lambda c: sorted(c))
both_inv = [c for c in all_placements
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
CSTAR = [c for c in both_inv if W0246 in c][0]

check("S0.1 placement space reconstructed: %d placements, %d "
      "both-invariant, C* selected deterministically"
      % (len(all_placements), len(both_inv)),
      len(all_placements) == 30 and len(both_inv) == 2)


# ------------------------------------------------- syndrome machinery
def code_basis(code):
    rows = [list(w) for w in sorted(code, reverse=True) if any(w)]
    basis = []
    pivots = []
    for r in rows:
        r = r[:]
        for b, pv in zip(basis, pivots):
            if r[pv]:
                r = [(x + y) % 2 for x, y in zip(r, b)]
        if any(r):
            basis.append(r)
            pivots.append(next(i for i, x in enumerate(r) if x))
    return basis


def synd_data(code):
    basis = code_basis(code)
    synd = {}
    for v in itertools.product((0, 1), repeat=8):
        synd[v] = tuple(sum(a * b for a, b in zip(bb, v)) % 2
                        for bb in basis)
    leaders = {}
    for v, s in synd.items():
        w = sum(v)
        cur = leaders.get(s)
        if cur is None or w < cur[0]:
            leaders[s] = (w, [v])
        elif w == cur[0]:
            cur[1].append(v)
    leaders = {s: (w, sorted(vs)) for s, (w, vs) in leaders.items()}
    return basis, synd, leaders


def e(i):
    return tuple(1 if k == i else 0 for k in range(8))


def induced_action(perm, synd):
    m = {}
    for v in itertools.product((0, 1), repeat=8):
        s = synd[v]
        t = synd[apply_perm(v, perm)]
        if s in m and m[s] != t:
            return None
        m[s] = t
    return m


BASIS, SYND, LEADERS = synd_data(CSTAR)
S0 = tuple(0 for _ in range(4))


def orbits_words(words, perms):
    seen = set()
    orbs = []
    for w in sorted(words):
        if w in seen:
            continue
        orb = {w}
        fr = [w]
        while fr:
            u = fr.pop()
            for p in perms:
                v = apply_perm(u, p)
                if v not in orb:
                    orb.add(v)
                    fr.append(v)
        seen.update(orb)
        orbs.append(orb)
    return orbs


def roots_of(code):
    return [x for x in itertools.product(range(-2, 3), repeat=8)
            if sum(v * v for v in x) == 4
            and tuple(v % 2 for v in x) in code]


def J_all(v):
    out = []
    for i in range(0, 8, 2):
        a, b = v[i], v[i + 1]
        out += [-b, a]
    return tuple(out)


def sigma_r(v):
    return (v[4], v[5], v[0], v[1], v[2], v[3], v[6], v[7])


# =================================================================== R1a
section("R1a: weight-4 orbit censuses under the placed symmetry chain")

# affine group AGL(3,2) as position permutations j -> A j + t
def bits3(j):
    return ((j >> 2) & 1, (j >> 1) & 1, j & 1)


AGL = []
for cA in range(1, 8):
    for cB in range(1, 8):
        if cB in (0, cA):
            continue
        for cC in range(1, 8):
            if cC in (0, cA, cB, cA ^ cB):
                continue
            for t in range(8):
                def phi(j, cA=cA, cB=cB, cC=cC, t=t):
                    out = t
                    if j & 4:
                        out ^= cA
                    if j & 2:
                        out ^= cB
                    if j & 1:
                        out ^= cC
                    return out
                AGL.append(tuple(phi(k) for k in range(8)))
AGL = sorted(set(AGL))
agl_preserves = all(code_image(CSTAR, p) == CSTAR for p in AGL)
P192 = [p for p in AGL if all(p[j ^ 1] == p[j] ^ 1 for j in range(8))]
P48 = [p for p in P192 if {p[6], p[7]} == {6, 7}]
check("R1a.1 symmetry chain built: |AGL(3,2)| = %d (all preserve C*: %s), "
      "|pair-partition stabilizer P192| = %d, |P48 = P192 fixing anchor "
      "pair| = %d; piJ in P48: %s, pisig in P48: %s"
      % (len(AGL), agl_preserves, len(P192), len(P48),
         PI_J in P48, PI_SIG in P48),
      len(AGL) == 1344 and agl_preserves and len(P192) == 192
      and len(P48) == 48 and PI_J in P48 and PI_SIG in P48)

w4_star = [w for w in CSTAR if sum(w) == 4]
GROUPS = [("Z2 = <piJ>", [PI_J]),
          ("Z3 = <pisig>", [PI_SIG]),
          ("Z6 = <piJ,pisig>", Z6),
          ("P48", P48),
          ("P192", P192),
          ("AGL(3,2)", AGL)]
PATTERNS = {"(1,1,2) Eintraege": [1, 1, 2],
            "(1,1,4) Normen": [1, 1, 4],
            "2*(1,1,2)": [2, 2, 4],
            "2*(1,1,4)": [2, 2, 8],
            "(2,4,8) Beispielmuster": [2, 4, 8]}
census_by_group = {}
pattern_hits = []
for gname, perms in GROUPS:
    sizes = sorted(len(o) for o in orbits_words(w4_star, perms))
    census_by_group[gname] = sizes
    hits = [pn for pn, pat in PATTERNS.items() if sorted(pat) == sizes]
    pattern_hits.extend((gname, h) for h in hits)
    print("    %-18s orbit sizes %-22s sum %2d  contains-6: %s  "
          "(1,1,2)-pattern hit: %s"
          % (gname, sizes, sum(sizes), 6 in sizes,
             hits if hits else "-"))
check("R1a.2 exact censuses computed for all 6 groups (each sums to 14)",
      all(sum(s) == 14 for s in census_by_group.values()))
check("R1a.3 HONEST RESULT: number of exact (1,1,2)-pattern hits across "
      "the whole chain: %d -- the weight-4 orbit decomposition does NOT "
      "carry the anchor decomposition (1,1,2) or its norms; the size-6 "
      "orbit (mixed transversals) coincides NUMERICALLY with the anchor "
      "norm 6 but has no (1,1,2)-refinement (Z3 splits it 3+3, Z2 splits "
      "it 2+2+2, never 1+1+4) => observation/BINGO, not a derivation"
      % len(pattern_hits), len(pattern_hits) == 0)
sext = [o for o in orbits_words(w4_star, Z6) if len(o) == 6][0]
sub3 = sorted(len(o) for o in orbits_words(sorted(sext), [PI_SIG]))
sub2 = sorted(len(o) for o in orbits_words(sorted(sext), [PI_J]))
check("R1a.4 size-6 orbit refinements measured exactly: under Z3 %s, "
      "under Z2 %s (neither is (1,1,4))" % (sub3, sub2),
      sub3 == [3, 3] and sub2 == [2, 2, 2])

# =================================================================== R1b
section("R1b: pair-sector coset-leader weights and the anchor (1,1,2)")

q_list = [tuple((a + b) % 2 for a, b in zip(SYND[e(2 * k)],
                                            SYND[e(2 * k + 1)]))
          for k in range(4)]
q = q_list[0]
A_sig = induced_action(PI_SIG, SYND)
A_J = induced_action(PI_J, SYND)
check("R1b.1 baseline (stage-2): q universal (all 4 pairs give the same "
      "q = %s != 0), sigma and piJ well-defined on syndromes"
      % (q,), len(set(q_list)) == 1 and q != S0
      and A_sig is not None and A_J is not None)

wq, q_leaders = LEADERS[q]
inpair_words = sorted(tuple((1 if i in PAIRS[k] else 0) for i in range(8))
                      for k in range(4))
check("R1b.2 the q-coset has leader weight %d with EXACTLY the 4 mu4 "
      "in-pair words as leaders: %s" % (wq, q_leaders == inpair_words),
      wq == 2 and q_leaders == inpair_words)

fixed_synd = sorted(s for s in set(SYND.values()) if A_sig[s] == s)
expected_fixed = sorted({S0, q, SYND[e(6)], SYND[e(7)]})
fixed_wts = sorted(LEADERS[s][0] for s in fixed_synd)
nz_wts = sorted(LEADERS[s][0] for s in fixed_synd if s != S0)
norm = sum(w * w for w in nz_wts)
check("R1b.3 THE ANCHOR IDENTITY: sigma-fixed syndromes = {0, s(e6), "
      "s(e7), q} exactly (%s); leader weights %s; the nonzero ones are "
      "(1,1,2) with norm-square sum %d = 6 = (1,1,2).(1,1,2)"
      % (fixed_synd == expected_fixed, fixed_wts, norm),
      fixed_synd == expected_fixed and fixed_wts == [0, 1, 1, 2]
      and nz_wts == [1, 1, 2] and norm == 6)

# quotient bookkeeping (stage-2 machinery)
piv = next(i for i, b in enumerate(q) if b)


def qred(s):
    if s[piv]:
        return tuple((a + b) % 2 for a, b in zip(s, q))
    return s


P = [qred(SYND[e(2 * k)]) for k in range(4)]
famsum = qred(tuple((a + b + c) % 2 for a, b, c in zip(P[0], P[1], P[2])))
check("R1b.4 anchor = family sum in the quotient: qred(s(e6)) = "
      "qred(s(e7)) = P3 and P3 = P0+P1+P2: %s"
      % (qred(SYND[e(6)]) == P[3] == qred(SYND[e(7)]) == famsum,),
      qred(SYND[e(6)]) == P[3] and qred(SYND[e(7)]) == P[3]
      and famsum == P[3])

sector_rows = []
all_112 = True
for k in range(4):
    sec = [SYND[e(2 * k)], SYND[e(2 * k + 1)], q]
    wts = sorted(LEADERS[s][0] for s in sec)
    img = [A_sig[s] for s in sec[:2]]
    stable = set(img) <= set(sec)
    ptwise = all(A_sig[s] == s for s in sec)
    sector_rows.append((k, wts, stable, ptwise))
    all_112 &= (wts == [1, 1, 2])
    print("    pair %d (%s): sector syndromes leader weights %s, "
          "norm %d; sigma-stable setwise: %s, pointwise: %s"
          % (k, PAIRS[k], wts, sum(w * w for w in wts), stable, ptwise))
check("R1b.5 ALL four pair sectors carry leader weights (1,1,2), norm 6 "
      "-- the sigma action selects the ANCHOR copy: only pair 3 = {6,7} "
      "is sigma-stable (indeed pointwise fixed): %s"
      % ([(k, st, pt) for k, _, st, pt in sector_rows],),
      all_112
      and [st for _, _, st, _ in sector_rows] == [False] * 3 + [True]
      and [pt for _, _, _, pt in sector_rows] == [False] * 3 + [True])

# =================================================================== R2
section("R2: small code invariants vs compiler numbers (p_n = 2 + 2^n)")

INV = []  # (name, value, tag)  tag: CODE = placement-independent


def add(name, value, tag):
    INV.append((name, int(value), tag))


leader_census = Counter(w for w, _ in LEADERS.values())
add("Ueberdeckungsradius", max(leader_census), "CODE")
for wt, cnt in sorted(leader_census.items()):
    add("#Cosets mit Leader-Gewicht %d" % wt, cnt, "CODE")
n_leaders = Counter(len(vs) for _, vs in LEADERS.values())
for nl, cnt in sorted(n_leaders.items()):
    add("#Cosets mit %d Leadern" % nl, cnt, "CODE")

dist_types = Counter()
for s in set(SYND.values()):
    dist = tuple(sorted(Counter(
        sum(v) for v in SYND if SYND[v] == s).items()))
    dist_types[dist] += 1
print("    coset weight distributions {weight: count} x multiplicity:")
for dist, mult in sorted(dist_types.items()):
    print("      %s x %d" % (dict(dist), mult))
    for wgt, cnt in dist:
        add("Coset-Verteilung (Typ x%d): #Gewicht-%d-Woerter"
            % (mult, wgt), cnt, "CODE")
check("R2.1 coset tables exact: leader census {0:1, 1:8, 2:7}, "
      "distributions = zero coset {0:1,4:14,8:1}, 8 x weight-1 "
      "{1:1,3:7,5:7,7:1}, 7 x weight-2 {2:4,4:8,6:4}",
      dict(leader_census) == {0: 1, 1: 8, 2: 7}
      and dist_types == Counter({
          ((0, 1), (4, 14), (8, 1)): 1,
          ((1, 1), (3, 7), (5, 7), (7, 1)): 8,
          ((2, 4), (4, 8), (6, 4)): 7}))

for r in range(1, 5):
    add("|B_%d| Kugelvolumen" % r, sum(comb(8, i) for i in range(r + 1)),
        "CODE")
add("n (Laenge)", 8, "CODE")
add("k (Dimension)", 4, "CODE")
add("d (Minimalabstand)", 4, "CODE")
add("#Codewoerter", 16, "CODE")
add("#Syndrome", 16, "CODE")
add("A_4 (#Gewicht-4-Woerter)", 14, "CODE")

ROOTS = roots_of(CSTAR)
root_class = Counter(tuple(v % 2 for v in x) for x in ROOTS)
add("#Konstruktion-A-Wurzeln", len(ROOTS), "CODE")
add("#wurzeltragende Codewoerter", len(root_class), "CODE")
add("Wurzeln pro tragendem Codewort", set(root_class.values()).pop()
    if len(set(root_class.values())) == 1 else -1, "CODE")
add("Wurzeln + n (E8-Dimension)", len(ROOTS) + 8, "CODE")

RSET = set(ROOTS)
seen = set()
n_lines = 0
lines_ok = True
for x in ROOTS:
    if x in seen:
        continue
    orb = [x]
    y = J_all(x)
    while y != x:
        if y not in RSET:
            lines_ok = False
        orb.append(y)
        y = J_all(y)
    seen.update(orb)
    n_lines += 1
add("#Clock-Orbits (Wurzeln/4)", n_lines, "CODE")
sig_fixed_roots = [x for x in ROOTS if sigma_r(x) == x]
add("#sigma-fixierte Wurzeln", len(sig_fixed_roots), "CSTAR")
add("#sigma-fixierte Syndrome", len(fixed_synd), "CSTAR")
add("Anker-Norm (Leader-Gewichte^2, sigma-fixe Syndrome != 0)", norm,
    "CSTAR")
add("#Paar-Unionen im Code", sum(
    1 for k1 in range(4) for k2 in range(k1 + 1, 4)
    if tuple(1 if i in PAIRS[k1] + PAIRS[k2] else 0
             for i in range(8)) in CSTAR), "CSTAR")
sig_fixed_cw = [w for w in CSTAR if apply_perm(w, PI_SIG) == w]
add("#sigma-fixierte Codewoerter", len(sig_fixed_cw), "CSTAR")
add("#sigma-Orbits auf den 16 Codewoertern",
    len(orbits_words(CSTAR, [PI_SIG])), "CSTAR")
info_sets = [frozenset(s) for s in itertools.combinations(range(8), 4)
             if frozenset(s) not in
             {frozenset(i for i in range(8) if w[i]) for w in w4_star}]
add("#Informationsmengen", len(info_sets), "CODE")


def subset_image(S, p):
    return frozenset(k for k in range(8) if p[k] in S)


def orbits_subsets(subsets, perms):
    seen_l = set()
    orbs = []
    for s in sorted(subsets, key=sorted):
        if s in seen_l:
            continue
        orb = {s}
        fr = [s]
        while fr:
            u = fr.pop()
            for p in perms:
                v = subset_image(u, p)
                if v not in orb:
                    orb.add(v)
                    fr.append(v)
        seen_l.update(orb)
        orbs.append(orb)
    return orbs


add("#Z6-Orbits der Informationsmengen",
    len(orbits_subsets(info_sets, Z6)), "CSTAR")
w4_all = [w for w in itertools.product((0, 1), repeat=8) if sum(w) == 4]
add("#Z6-Orbits auf allen 70 Gewicht-4-Woertern",
    len(orbits_words(w4_all, Z6)), "CSTAR")
add("#Z6-Orbits auf F2^8",
    len(orbits_words(list(itertools.product((0, 1), repeat=8)), Z6)),
    "CSTAR")
add("#beide-invariante Placements", len(both_inv), "CSTAR")

print("    invariant battery (%d entries):" % len(INV))
for name, val, tag in INV:
    print("      %-58s %5d  [%s]" % (name, val, tag))

TARGETS = [2, 3, 4, 6, 10, 18, 240, 8, 248, 60, 12, 27, 81]
print("    exact matches against the compiler numbers:")
match_map = {}
for t in TARGETS:
    hits = [(name, tag) for name, val, tag in INV if val == t]
    match_map[t] = hits
    print("      %4d: %s" % (t, ["%s [%s]" % h for h in hits]
                             if hits else "KEIN TREFFER"))
check("R2.2 structural anchors land exactly: 240 = #roots = 16 x 15, "
      "8 = n = #weight-1 cosets, 248 = roots + n, 60 = roots/4 "
      "(clock orbits), 12 = #sigma-fixed roots [C*], 6 = anchor norm = "
      "#pair-unions [C*], 4 = k = d = #q-leaders",
      all(match_map[t] for t in (240, 8, 248, 60, 12, 6, 4)))
check("R2.3 HONEST RESULT: 27 and 81 have NO exact code-invariant "
      "reading in the battery (%s, %s); 10 hits only the Z6-orbit count "
      "of the 56 information sets [C*-specific, no p_n family]; 18 has "
      "%s" % (match_map[27], match_map[81],
              match_map[18] if match_map[18] else "KEIN TREFFER"),
      not match_map[27] and not match_map[81])

# ---- p_n sequence family scan --------------------------------------
P_SEQ = (4, 6, 10, 18)     # p_n = 2 + 2^n, n = 1..4
weights_all = {n: [w for w in itertools.product((0, 1), repeat=8)
                   if sum(w) == n] for n in (1, 2, 3, 4)}
cw_sorted = sorted(CSTAR, key=sum)
zero_dist = Counter(sum(v) for v in SYND if SYND[v] == S0)
w1_dist = Counter(sum(v) for v in SYND if SYND[v] == SYND[e(0)])
q_dist = Counter(sum(v) for v in SYND if SYND[v] == q)
FAMS = {
    "|B_n| (Kugelvolumen)":
        tuple(sum(comb(8, i) for i in range(n + 1)) for n in (1, 2, 3, 4)),
    "#Woerter Gewicht<=n im 0-Coset":
        tuple(sum(c for w, c in zero_dist.items() if w <= n)
              for n in (1, 2, 3, 4)),
    "#Woerter Gewicht<=n im Gewicht-1-Coset":
        tuple(sum(c for w, c in w1_dist.items() if w <= n)
              for n in (1, 2, 3, 4)),
    "#Woerter Gewicht<=n im q-Coset":
        tuple(sum(c for w, c in q_dist.items() if w <= n)
              for n in (1, 2, 3, 4)),
    "#Cosets mit Leader-Gewicht<=n":
        tuple(sum(c for w, c in leader_census.items() if w <= n)
              for n in (1, 2, 3, 4)),
    "#Syndrome der Gewicht-n-Woerter":
        tuple(len({SYND[w] for w in weights_all[n]}) for n in (1, 2, 3, 4)),
    "#Z6-Orbits auf Gewicht-n-Woertern":
        tuple(len(orbits_words(weights_all[n], Z6)) for n in (1, 2, 3, 4)),
    "#piJ-Orbits auf Gewicht-n-Woertern":
        tuple(len(orbits_words(weights_all[n], [PI_J]))
              for n in (1, 2, 3, 4)),
    "#sigma-Orbits auf Gewicht-n-Woertern":
        tuple(len(orbits_words(weights_all[n], [PI_SIG]))
              for n in (1, 2, 3, 4)),
    "#Codewoerter Gewicht<=2n":
        tuple(sum(1 for w in CSTAR if sum(w) <= 2 * n)
              for n in (1, 2, 3, 4)),
    "A_{2n} (Gewichtszaehler)":
        tuple(sum(1 for w in CSTAR if sum(w) == 2 * n)
              for n in (1, 2, 3, 4)),
}
print("    p-sequence scan, target (4, 6, 10, 18):")
fam_hits = []
for name, vec in sorted(FAMS.items()):
    hit = vec == P_SEQ
    if hit:
        fam_hits.append(name)
    print("      %-42s %-22s %s" % (name, vec, "TREFFER" if hit else ""))
check("R2.4 HONEST RESULT: %d of %d natural code families reproduce the "
      "p-sequence (4,6,10,18) -- the v624s bytecode p_n = 2 + 2^n has "
      "NO coset/ball/orbit reading in RM(1,3); individual matches "
      "(240, 8, 248) are real but do not assemble the sequence"
      % (len(fam_hits), len(FAMS)), len(fam_hits) == 0)

# =================================================================== R3
section("R3: kill control -- naive placement and the 30-census")

BASIS_N, SYND_N, LEADERS_N = synd_data(C_NAIVE)
q_list_n = [tuple((a + b) % 2 for a, b in zip(SYND_N[e(2 * k)],
                                              SYND_N[e(2 * k + 1)]))
            for k in range(4)]
A_sig_n = induced_action(PI_SIG, SYND_N)
check("R3.1 KILL fires for the sigma layer: naive placement has %d "
      "distinct in-pair syndromes (no universal q) and sigma is NOT "
      "well-defined on its syndromes (induced action: %s) => the "
      "anchor-sector SELECTION (R1b.3-5) has no analogue"
      % (len(set(q_list_n)), A_sig_n),
      len(set(q_list_n)) > 1 and A_sig_n is None)

naive_112 = []
for k in range(4):
    sec = [SYND_N[e(2 * k)], SYND_N[e(2 * k + 1)], q_list_n[k]]
    wts = sorted(LEADERS_N[s][0] for s in sec)
    naive_112.append(wts)
check("R3.2 KILL does NOT fire for the raw weights: naive pair sectors "
      "carry leader weights %s -- the (1,1,2)/norm-6 triple per pair is "
      "GENERIC for any [8,4,4] placement (weight-1 cosets + a d>=4 "
      "in-pair coset); only q-universality, sigma-fixedness and "
      "anchor = family sum are equivariance-specific"
      % naive_112, all(w == [1, 1, 2] for w in naive_112))

leader_census_n = Counter(w for w, _ in LEADERS_N.values())
dist_types_n = Counter()
for s in set(SYND_N.values()):
    dist = tuple(sorted(Counter(
        sum(v) for v in SYND_N if SYND_N[v] == s).items()))
    dist_types_n[dist] += 1
check("R3.3 KILL does NOT fire for R2: naive leader census %s and "
      "distribution multiset identical to C* (%s) -- ALL pure-code "
      "R2 matches (240, 8, 248, 60, ...) are placement-INDEPENDENT "
      "code facts, not equivariance results"
      % (dict(leader_census_n), dist_types_n == dist_types),
      leader_census_n == leader_census and dist_types_n == dist_types)

all30_leader = {tuple(sorted(Counter(
    w for w, _ in synd_data(c)[2].values()).items()))
    for c in all_placements}
check("R3.4 30-census: every one of the 30 placements has the same "
      "leader census (distinct censuses: %d)" % len(all30_leader),
      len(all30_leader) == 1)

w4_naive = [w for w in C_NAIVE if sum(w) == 4]
orbs70 = orbits_words(w4_all, Z6)
frag = sum(1 for o in orbs70 if 0 < len(o & set(w4_naive)) < len(o))
check("R3.5 KILL fires for the orbit layer: naive weight-4 set "
      "fragments %d Z6-orbits (C*: 0) => the C*-tagged orbit entries "
      "(6 = #pair-unions, 10 = info-set orbits) die without "
      "equivariance" % frag, frag > 0)

# sigma-fixed root COUNT across all 30 placements (exact, closed form:
# the 20 sigma-fixed norm-4 vectors are +-2e6, +-2e7 (class 0) and
# 16 vectors over the four transversal classes {0,2,4}u{6 or 7},
# {1,3,5}u{6 or 7}, 4 roots per class that lies in the code)
TRANS4 = [tuple(1 if i in s else 0 for i in range(8))
          for s in ({0, 2, 4, 6}, {0, 2, 4, 7},
                    {1, 3, 5, 6}, {1, 3, 5, 7})]


def n_sigma_fixed_roots(code):
    return 4 + 4 * sum(1 for tw in TRANS4 if tw in code)


dist30 = Counter(n_sigma_fixed_roots(c) for c in all_placements)
n_star = n_sigma_fixed_roots(CSTAR)
n_naive = n_sigma_fixed_roots(C_NAIVE)
sig_fixed_roots_n = [x for x in roots_of(C_NAIVE) if sigma_r(x) == x]
check("R3.6 HONEST CORRECTION: the sigma-fixed root COUNT does NOT "
      "separate C* -- closed-form count verified against enumeration "
      "for naive (%d = %d); distribution over the 30 placements: %s; "
      "C* = %d, naive = %d => the raw '12' is NOT "
      "equivariance-specific (only the mod-2 FIBRATION of stage-2 "
      "S1.8 -- 3 classes x 4, zero fibre = anchor pair, doublet = "
      "Z6-orbit -- is C*-structure); retype the R2 hit '12' "
      "accordingly"
      % (n_naive, len(sig_fixed_roots_n), dict(sorted(dist30.items())),
         n_star, n_naive),
      n_naive == len(sig_fixed_roots_n) and n_star == 12)

# ================================================================ summary
section("SUMMARY")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print()
print("R1a (Gewicht-4-Orbits tragen (1,1,2)): FAIL -- Ketten-Zensen")
for gname, sizes in census_by_group.items():
    print("      %-18s %s" % (gname, sizes))
print("  kein exaktes (1,1,2)-Muster; die 6 ist Zahlen-Koinzidenz.")
print("R1b (Anker-(1,1,2) als Coset-Leader-Gewichte): PASS -- exakt,")
print("  aber ehrlich zweigeteilt: (1,1,2)/Norm 6 pro Paar-Sektor ist")
print("  GENERISCH ([8,4,4]-Fakt, R3.2); aequivariant-spezifisch sind")
print("  q-Universalitaet, sigma-Fixierung des Anker-Sektors und")
print("  Anker = Familiensumme (R1b.3-5, stirbt fuer naive: R3.1).")
print("R2  (p_n = 2+2^n als Code-Operation): FAIL/BINGO -- 240, 8, 248,")
print("  60 sind exakte platzierungs-unabhaengige Code-Fakten; die")
print("  p-FOLGE (4,6,10,18) hat keine gefundene Code-Lesart; 27/81")
print("  ohne Treffer; 10 nur als Z6-Orbitzahl der Info-Mengen (BINGO).")
print("R3  (Kill-Kontrolle): feuert fuer sigma/Anker-Auswahl und die")
print("  Orbit-Zensen (6, 10), feuert NICHT fuer Sektor-Gewichte,")
print("  reine Code-Invarianten UND den sigma-Fixwurzel-ZAEHLER 12")
print("  (naive hat ebenfalls 12; nur die Faserstruktur ist C*-")
print("  spezifisch) => ehrlich entsprechend getypt.")
print()
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS)
      else "SOME CHECKS FAILED")


def run():
    """run_all entry point: the checks above already ran at import."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
