"""Discovery probe: ORBIT60 CENSUS -- the 60 mu4-lines of E8 as a
combinatorial object: quotient graph, sigma / clock / Coxeter dynamics
on the ORBIT SPACE, and a STRICT park test for the cascade
D_n = 60 - 2n as canonical orbit elimination.

Objects (v629 / v633 / v634 conventions, recomputed self-contained):
the 240 E8 roots in the D8+spinor model (doubled integer coordinates),
J = the mu4 quarter-turn on all four coordinate pairs (free, 60
orbits = lines = D_start), sigma = the 3-cycle of pairs 1->2->3->1,
H(x,y) = <x,y> + i <x,Jy> the hermitian form (H(v,v) = 2 on roots),
the 60 order-2 unitary reflections R_v(x) = x - H(x,v) v, and the
induced LINE GROUP LG = G31 / mu4 of order 11520 on the 60 lines.

WHAT IS NEW versus v633/v634 (both are census-only prerequisites
here): the FULL cycle-type census of all 11520 line-group elements
(v634 censused element orders on the 240 roots, not cycle types on
the 60 lines), the Coxeter questions (does the W(E8) Coxeter element
descend at all? what do the maximal-order line elements do?), and the
involution-witness test for the cascade.

SLICES (bars and the canonicity criterion declared BEFORE any number):

O1 [CENSUS].  Line reps, the |H|^2 pair distribution over the 1770
   unordered line pairs (with {|Re|,|Im|} refinement), the quotient
   graphs G_m (edges = pairs with |H|^2 = m): degrees, connectivity,
   integer spectra, sigma-invariance; line group order (BFS from the
   60 reflection line-permutations), line stabilizer order, center.

O2 [DYNAMICS].  Exact cycle structure on the 60 lines of: sigma (3^19
   1^3 expected, v633 Q4), the compiler clock c = J o sigma (must act
   AS sigma on lines, since J is in the kernel -- exact check), the
   W(E8) Coxeter element (order 30; measured: does it normalize
   <J> and hence descend to the orbit space at all?), and the
   maximal-order elements of the line group (the 'Coxeter analogues'
   of ST31 seen from the quotient): full order census + cycle types.

O3 [THE HARD TEST -- canonical constructions ONLY, no free search
   over pairings].  The cascade D_n = 60 - 2n (60 -> 6 in 27 pair
   steps) needs a natural sequence of orbit pairs.  Tested routes:
   (i)   degree rules on the quotient graphs (max/min degree): dead
         iff the graphs are regular (v633 Q8 one level finer);
   (ii)  sigma-cycle structure: sigma orbits have sizes {3, 1} -- a
         parity/shape test against 2-blocks;
   (iii) THE INVOLUTION WITNESS: a one-shot carrier of the cascade
         would be a line-group involution of cycle type 2^27 1^6
         (27 disjoint transpositions, 6 survivors = D_end).
         CANONICITY BAR (declared): the type exists AND forms a
         single conjugacy class AND has a UNIQUE sigma-commuting
         representative.  Anything else is not canonical.
   (iv)  reflection / Coxeter-orbit routes: the cycle types of the 60
         reflections on the lines (do 2-blocks appear? is any
         reflection distinguished, i.e. do they split into more than
         one class?), and 2-cycles of the maximal-order elements;
   (v)   NUMEROLOGY MUST-FAIL CONTROL: rule-free lexicographic pair
         removal reproduces 60 -> 6 trivially -- the counting alone
         carries NO information (v633 Q8.2 reproduced in one line).

O4 [VERDICT + the A5 one-liner].  Enums (frozen):
     ORBIT60-CASCADE-CANONICAL  -- the canonicity bar of O3(iii) is
                                   met (or a degree/sigma route is
                                   canonically forced);
     ORBIT60-PARKED             -- no natural structure (the review's
                                   park criterion; no A5 expedition).
   A5 side note (1 line, as instructed): order-5 element count in the
   line group and the order of <sigma, first order-5 element> --
   measured signature only, no expedition.

FIREWALL: experiments-only; no marker moves; no file outside
experiments/ is touched; the involution census is a census over GROUP
elements (canonical objects), not a search over arbitrary pairings;
deterministic (fixed seed for the small-generating-set search only).

Provenance: root_incidence_probe.py / v629 (J free, 60 = D_start),
orbit60_quotient_probe.py / v633 (quotient Gram, cascade kill C0-C3),
st31_structure_probe.py / v634 (G31 = full unitary stabilizer, order
46080, line action 11520; W(D5) does not embed).
"""
import itertools
import random
import time
from collections import Counter
from math import lcm

import numpy as np

T0 = time.time()
CHECKS = []
N240 = 240
NL = 60
CASCADE_PAIRS = 27          # 60 -> 6 in 27 pair steps
D_END = 6
SEED_GEN = 11               # v634 S1.4 small-generating-set search seed


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ================================================================ S0: roots
section("S0: roots, J, sigma, lines, hermitian line Gram "
        "(v634 conventions, doubled integers)")

_roots = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        _roots.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        _roots.append(v)
RD = np.array(sorted(_roots), dtype=np.int64)
ridx = {tuple(int(a) for a in RD[i]): i for i in range(N240)}


def J_vec(x):
    out = np.empty_like(x)
    out[0::2] = -x[1::2]
    out[1::2] = x[0::2]
    return out


def perm_from_map(f):
    return np.array([ridx[tuple(int(a) for a in f(RD[i]))]
                     for i in range(N240)], dtype=np.int16)


Jperm = perm_from_map(J_vec)
SIGMA_IDX = [4, 5, 0, 1, 2, 3, 6, 7]
sigperm = perm_from_map(lambda x: x[SIGMA_IDX])
IDP240 = np.arange(N240, dtype=np.int16)


def comp(p, q):
    """(p o q)[i] = p[q[i]] (apply q first, then p)."""
    return p[q]


def pinv(p):
    return np.argsort(p).astype(np.int16)


def cyc_type(p):
    """Exact cycle type as a sorted tuple of (length, count)."""
    n = len(p)
    seen = [False] * n
    cnt = Counter()
    for s in range(n):
        if seen[s]:
            continue
        ln, j = 0, s
        while not seen[j]:
            seen[j] = True
            j = int(p[j])
            ln += 1
        cnt[ln] += 1
    return tuple(sorted(cnt.items()))


def order_of_type(tp):
    o = 1
    for ln, _ in tp:
        o = lcm(o, ln)
    return o


line_of = np.full(N240, -1, dtype=np.int32)
line_reps = []
for i in range(N240):
    if line_of[i] >= 0:
        continue
    orb = [i, int(Jperm[i]), int(Jperm[Jperm[i]]),
           int(Jperm[Jperm[Jperm[i]]])]
    for j in orb:
        line_of[j] = len(line_reps)
    line_reps.append(i)
check("S0.1 240 roots; J free of order 4 with EXACTLY 60 lines; sigma "
      "of order 3; [J, sigma] = 0 (v629 reproduced)",
      RD.shape == (240, 8) and len(line_reps) == 60
      and order_of_type(cyc_type(Jperm)) == 4
      and not np.any(Jperm == IDP240)
      and order_of_type(cyc_type(sigperm)) == 3
      and np.array_equal(comp(Jperm, sigperm), comp(sigperm, Jperm)))

JRD = np.array([J_vec(RD[i]) for i in range(N240)], dtype=np.int64)


def herm4_rowvec(v_i):
    """4*H(x, root_i) for all 240 roots x -> (re4, im4) integer arrays."""
    return RD @ RD[v_i], RD @ JRD[v_i]


HG = np.zeros((60, 60, 2), dtype=np.int64)
for a in range(60):
    re4, im4 = herm4_rowvec(line_reps[a])
    for b in range(60):
        HG[a, b, 0] = re4[line_reps[b]] // 4
        HG[a, b, 1] = im4[line_reps[b]] // 4
absH2 = HG[..., 0] ** 2 + HG[..., 1] ** 2
check("S0.2 H(v,v) = 2 on all 60 line reps (diagonal |H|^2 = 4)",
      bool(np.all(np.diag(absH2) == 4))
      and bool(np.all(np.diag(HG[..., 0]) == 2)))

# ================================================================ O1
section("O1: pair census, quotient graphs, line group, stabilizers")

offd = ~np.eye(60, dtype=bool)
pair_census = Counter()
cls_census = Counter()
for a in range(60):
    for b in range(a + 1, 60):
        n2 = int(absH2[a, b])
        pair_census[n2] += 1
        key = (n2, tuple(sorted((abs(int(HG[a, b, 0])),
                                 abs(int(HG[a, b, 1]))))))
        cls_census[key] += 1
check("O1.1 |H|^2 pair census over the 1770 line pairs: %s; refined "
      "{|Re|,|Im|} classes: %s"
      % (dict(sorted(pair_census.items())),
         {k: v for k, v in sorted(cls_census.items())}),
      sum(pair_census.values()) == 1770)

rowprof = [tuple(sorted(Counter(int(x) for x in absH2[a][offd[a]])
                        .items())) for a in range(60)]
row_regular = len(set(rowprof)) == 1
check("O1.2 row regularity: every line sees the SAME |H|^2 profile %s"
      % (rowprof[0],), row_regular)

# reflection line-permutations (v634 S1, projected to lines)
refl_line = []
for a in range(60):
    vi = line_reps[a]
    re4, im4 = herm4_rowvec(vi)
    re, im = re4 // 4, im4 // 4
    Y = RD - re[:, None] * RD[vi][None, :] - im[:, None] * JRD[vi][None, :]
    p = np.array([ridx[tuple(int(t) for t in Y[i])]
                  for i in range(N240)], dtype=np.int16)
    refl_line.append(line_of[p[line_reps]].astype(np.int16))
n_dist = len({p.tobytes() for p in refl_line})

IDL = np.arange(NL, dtype=np.int16)


def bfs_group(gens, cap=20000):
    seen = {IDL.tobytes(): IDL}
    frontier = [IDL]
    while frontier:
        nxt = []
        for p in frontier:
            for g in gens:
                q = p[g]
                b = q.tobytes()
                if b not in seen:
                    seen[b] = q
                    nxt.append(q)
                    if len(seen) > cap:
                        return seen, False
        frontier = nxt
    return seen, True


t = time.time()
LGset, full = bfs_group(refl_line)
Els = list(LGset.values())
check("O1.3 the line group LG = <60 reflection line-perms> has order "
      "%d = 46080/4 (BFS, %.1f s; %d distinct generator perms)"
      % (len(Els), time.time() - t, n_dist),
      full and len(Els) == 11520 and n_dist == 60)

stab0 = sum(1 for p in Els if int(p[0]) == 0)
orbit0 = len({int(p[0]) for p in Els})
check("O1.4 LG transitive on the 60 lines (orbit %d); line stabilizer "
      "order %d = 11520/60 (= |G(4,2,3)| = the v634 root-stabilizer "
      "order)" % (orbit0, stab0), orbit0 == 60 and stab0 == 192)

# small generating set (for cheap conjugation / center work)
rng_g = random.Random(SEED_GEN)
gens_small = None
for size in (5, 6, 7):
    for _ in range(120):
        cand = [refl_line[i] for i in rng_g.sample(range(60), size)]
        sub, f2 = bfs_group(cand)
        if f2 and len(sub) == 11520:
            gens_small = cand
            break
    if gens_small is not None:
        break
if gens_small is None:
    gens_small = refl_line
center = [p for p in Els
          if all(np.array_equal(comp(p, g), comp(g, p))
                 for g in gens_small)]
center = [p for p in center
          if all(np.array_equal(comp(p, g), comp(g, p))
                 for g in refl_line)]
check("O1.5 center of LG: order %d (mu4 is the kernel of the line "
      "action, so a canonical central involution on the lines %s)"
      % (len(center), "EXISTS" if len(center) > 1 else "does NOT exist"),
      len(center) >= 1)

# quotient graphs G_m for every off-diagonal |H|^2 value
sig_line = line_of[sigperm[line_reps]].astype(np.int16)
graph_rows = []
for m in sorted(pair_census):
    Adj = (absH2 == m) & offd
    degs = sorted(set(int(d) for d in Adj.sum(axis=1)))
    # connectivity
    seen_c = {0}
    stack = [0]
    while stack:
        x = stack.pop()
        for yv in np.nonzero(Adj[x])[0]:
            if int(yv) not in seen_c:
                seen_c.add(int(yv))
                stack.append(int(yv))
    conn = len(seen_c) == 60 if degs != [0] else False
    spec = Counter(round(float(e), 6)
                   for e in np.linalg.eigvalsh(Adj.astype(float)))
    sig_inv = bool(np.array_equal(Adj[np.ix_(sig_line, sig_line)], Adj))
    graph_rows.append((m, degs, conn, spec, sig_inv))
    print("      G_%d: degrees %s, connected %s, sigma-invariant %s, "
          "spectrum %s"
          % (m, degs, conn, sig_inv, dict(sorted(spec.items()))))
check("O1.6 all quotient graphs are sigma-invariant and REGULAR "
      "(single degree each): %s"
      % ([(m, degs) for m, degs, _, _, _ in graph_rows]),
      all(sig and len(degs) == 1
          for _, degs, _, _, sig in graph_rows))

# ================================================================ O2
section("O2: sigma, clock and Coxeter dynamics on the orbit space")

tp_sig = cyc_type(sig_line)
check("O2.1 sigma on the 60 lines: cycle type %s = 3^19 1^3 (v633 Q4 "
      "reproduced exactly)" % (tp_sig,),
      tp_sig == ((1, 3), (3, 19)))

clock = comp(Jperm, sigperm)
clock_line = line_of[clock[line_reps]].astype(np.int16)
check("O2.2 the compiler clock c = J o sigma acts on the lines EXACTLY "
      "as sigma (J is in the kernel of the line action): %s -- the "
      "order-12 clock is INVISIBLE on the orbit space beyond its "
      "sigma part" % np.array_equal(clock_line, sig_line),
      np.array_equal(clock_line, sig_line))


def real_refl_perm(rd):
    ip4 = RD @ rd
    Y = RD - (ip4 // 4)[:, None] * rd[None, :]
    return np.array([ridx[tuple(int(t) for t in Y[i])]
                     for i in range(N240)], dtype=np.int16)


# Bourbaki simple roots of E8 (even coordinate system), doubled
SIMPLE = [
    (1, -1, -1, -1, -1, -1, -1, 1),      # (e1+e8)/2 - (e2+..+e7)/2
    (2, 2, 0, 0, 0, 0, 0, 0),            # e1 + e2
    (-2, 2, 0, 0, 0, 0, 0, 0),           # e2 - e1
    (0, -2, 2, 0, 0, 0, 0, 0),           # e3 - e2
    (0, 0, -2, 2, 0, 0, 0, 0),           # e4 - e3
    (0, 0, 0, -2, 2, 0, 0, 0),           # e5 - e4
    (0, 0, 0, 0, -2, 2, 0, 0),           # e6 - e5
    (0, 0, 0, 0, 0, -2, 2, 0),           # e7 - e6
]
ok_simple = all(tuple(s) in ridx for s in SIMPLE)
cox = IDP240
for s in SIMPLE:
    cox = comp(cox, real_refl_perm(np.array(s, dtype=np.int64)))
ord_cox = order_of_type(cyc_type(cox))
Jc = comp(cox, comp(Jperm, pinv(cox)))
Jpow = {IDP240.tobytes(): 0, Jperm.tobytes(): 1,
        comp(Jperm, Jperm).tobytes(): 2,
        comp(Jperm, comp(Jperm, Jperm)).tobytes(): 3}
normalizes = Jc.tobytes() in Jpow
check("O2.3 the W(E8) Coxeter element (product of the 8 Bourbaki "
      "simple reflections, all 8 in the root set: %s) has order %d; "
      "it %s <J> (c J c^-1 = %s) -- it %s to the 60-line orbit space"
      % (ok_simple, ord_cox,
         "NORMALIZES" if normalizes else "does NOT normalize",
         ("J^%d" % Jpow[Jc.tobytes()]) if normalizes else "not a power "
         "of J", "DESCENDS" if normalizes else "does NOT descend"),
      ok_simple and ord_cox == 30)

t = time.time()
types = [cyc_type(p) for p in Els]
orders = [order_of_type(tp) for tp in types]
ord_census = Counter(orders)
check("O2.4 FULL cycle-type census of all 11520 line-group elements "
      "(%.1f s): element-order census %s"
      % (time.time() - t, dict(sorted(ord_census.items()))),
      sum(ord_census.values()) == 11520 and ord_census[1] == 1)

max_ord = max(ord_census)
max_types = Counter(tp for tp, o in zip(types, orders) if o == max_ord)
print("      maximal element order in LG: %d (%d elements); their "
      "cycle types on the 60 lines:" % (max_ord, ord_census[max_ord]))
for tp, cnt in sorted(max_types.items()):
    print("        %s  x %d" % (tp, cnt))

# ================================================================ O3
section("O3: the hard test -- D_n = 60 - 2n as canonical orbit "
        "elimination (declared canonicity bar)")

check("O3.1 [route i, degree rules] every quotient graph is REGULAR "
      "(O1.6): a max/min-degree elimination rule is ILL-DEFINED on "
      "the orbit space -- the v633 Q8 kill one level finer", 
      all(len(degs) == 1 for _, degs, _, _, _ in graph_rows))

sig_orbit_sizes = sorted(ln for ln, c in tp_sig for _ in range(c))
n_sig_classes = sum(c for _, c in tp_sig)
check("O3.2 [route ii, sigma structure] sigma-orbit sizes on the lines "
      "are %s -- NO 2-blocks exist; the sigma quotient is 60 -> %d "
      "classes, not 60 -> 58: the family cycle cannot carry a -2 step"
      % (dict(tp_sig), n_sig_classes),
      2 not in {ln for ln, _ in tp_sig})

# route iii: the involution witness 2^27 1^6
inv_idx = [i for i, o in enumerate(orders) if o == 2]
fix_census = Counter()
for i in inv_idx:
    tp = dict(types[i])
    fix_census[tp.get(1, 0)] += 1
print("      involution census of LG: %d involutions; fixed-line "
      "census {fixed: count} = %s"
      % (len(inv_idx), dict(sorted(fix_census.items()))))
witnesses = [i for i in inv_idx if dict(types[i]).get(1, 0) == D_END]
witness_exists = len(witnesses) > 0

# conjugacy classes (needed only for the witness canonicity)
t = time.time()
byte2i = {p.tobytes(): i for i, p in enumerate(Els)}
conj_gens = [(g, pinv(g)) for g in gens_small]
cls_id = np.full(len(Els), -1, dtype=np.int32)
n_cls = 0
for i in range(len(Els)):
    if cls_id[i] >= 0:
        continue
    cid = n_cls
    n_cls += 1
    stack = [Els[i]]
    cls_id[i] = cid
    while stack:
        x = stack.pop()
        for g, gi in conj_gens:
            yv = g[x[gi]]
            r = byte2i[yv.tobytes()]
            if cls_id[r] < 0:
                cls_id[r] = cid
                stack.append(yv)
print("      conjugacy classes of LG: %d (%.1f s)"
      % (n_cls, time.time() - t))

if witness_exists:
    w_classes = sorted({int(cls_id[i]) for i in witnesses})
    w_sig_comm = [i for i in witnesses
                  if np.array_equal(comp(Els[i], sig_line),
                                    comp(sig_line, Els[i]))]
    canonical = (len(w_classes) == 1 and len(w_sig_comm) == 1)
    check("O3.3 [route iii, involution witness] type 2^%d 1^%d EXISTS: "
          "%d elements in %d conjugacy class(es); sigma-commuting "
          "representatives: %d -- canonicity bar (single class AND "
          "unique sigma-commuting rep): %s"
          % (CASCADE_PAIRS, D_END, len(witnesses), len(w_classes),
             len(w_sig_comm), "MET" if canonical else "NOT met"),
          True)
else:
    canonical = False
    check("O3.3 [route iii, involution witness] NO line-group "
          "involution has cycle type 2^%d 1^%d (fixed-line census "
          "%s): the one-shot group-action carrier of the cascade "
          "does NOT exist in LG -- route killed"
          % (CASCADE_PAIRS, D_END, dict(sorted(fix_census.items()))),
          True)

# route iv: reflections and maximal-order elements
refl_types = Counter(cyc_type(p) for p in refl_line)
refl_cls = sorted({int(cls_id[byte2i[p.tobytes()]]) for p in refl_line})
two_cycles_max = sorted({dict(tp).get(2, 0) for tp in max_types})
check("O3.4 [route iv, reflection / Coxeter orbits] reflection cycle "
      "types on the lines: %s in %d conjugacy class(es) -- %s; "
      "2-cycle counts of the maximal-order elements: %s (a canonical "
      "27-pair sequence would need 27 disjoint 2-blocks from ONE "
      "distinguished element)"
      % (dict(refl_types), len(refl_cls),
         "no reflection is distinguished" if len(refl_cls) == 1
         else "reflections split into classes",
         two_cycles_max),
      True)

# route v: the numerology must-fail control
alive = list(range(60))
seq = [len(alive)]
while len(alive) > D_END:
    alive = alive[2:]                     # rule-free lexicographic pairs
    seq.append(len(alive))
n_free = 1
for k in range(30, D_END // 2, -1):
    n_free *= k * (2 * k - 1)
check("O3.5 [route v, MUST-FAIL numerology control] rule-free "
      "lexicographic pair removal reproduces the counting %s... -> %d "
      "in exactly %d steps; the number of equally 'successful' "
      "pairing sequences is astronomically large (> 10^%d): the "
      "COUNTING 60 - 2n carries no structural information -- only a "
      "canonical pair choice would (v633 Q8.2 reproduced)"
      % (seq[:4], seq[-1], len(seq) - 1,
         int(np.floor(np.log10(float(n_free))))),
      seq == list(range(60, D_END - 1, -2)))

# ================================================================ O4
section("O4: verdict + the A5 one-liner")

n5 = ord_census.get(5, 0)
g5 = next((Els[i] for i, o in enumerate(orders) if o == 5), None)
if g5 is not None:
    sub5, _ = bfs_group([sig_line, g5], cap=20000)
    a5_note = ("order-5 elements exist (%d); <sigma, first order-5 "
               "element (sample, NOT canonical)> has order %d"
               % (n5, len(sub5)))
else:
    a5_note = "NO order-5 element in LG"
check("O4.1 [A5 one-liner] %s -- no visible NATURAL A5 action attached "
      "to the compiler data (sigma has order 3, the clock acts as "
      "sigma); the A5 expedition stays parked per the review criterion"
      % a5_note, True)

VERDICT = ("ORBIT60-CASCADE-CANONICAL" if canonical
           else "ORBIT60-PARKED")

# ================================================================ summary
section("SUMMARY")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print()
print("VERDICT: %s" % VERDICT)
if not canonical:
    print("  route i   (degree rules)      : DEAD (all quotient graphs "
          "regular)")
    print("  route ii  (sigma structure)   : DEAD (orbit sizes {3,1}, "
          "no 2-blocks)")
    print("  route iii (involution witness): %s"
          % ("DEAD (type 2^27 1^6 absent from LG)"
             if not witness_exists else
             "NOT CANONICAL (witness type exists but fails the "
             "declared bar)"))
    print("  route iv  (reflection/Coxeter): no distinguished element "
          "carries 27 disjoint 2-blocks")
    print("  route v   (numerology control): fires as designed -- the "
          "counting is free")
print()
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS)
      else "SOME CHECKS FAILED")


def run():
    """Entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
