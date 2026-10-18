#!/usr/bin/env python3
"""v634 -- E8.ST31.01: the ST31 structure round -- does the fresh ST31 find
carry structural weight?

Builds on orbit60_quotient_probe.py (read-only): the 240 E8 roots under the
free mu4-action J_all give 60 Z[i]-lines; the 60 order-2 unitary reflections
R_v(x) = x - H(x,v) v generate a group G acting on the 240 roots.

TEST 1 -- the subgroup kill test
  T1.1  |G| = 46080 (BFS + independent sympy Schreier-Sims); induced line
        action 11520 = 46080/4; G is the FULL group of unitary maps
        preserving the root set (exact backtracking count of hermitian-
        Gram-matching images of a Z[i]-unimodular root basis).
  T1.2  P = W(D5) x W(A3) built concretely on the SAME 240 roots
        (D5 in coords 1-5, A3 = D3 in coords 6-8); |P| = 1920 * 24 = 46080.
  T1.3  abstract isomorphism G =?= P killed by cheap invariants: center,
        abelianization, derived series, element-order spectrum.
  T1.4  semidirect kill: capped normal closures per conjugacy class; the
        join Nsmall of all small closures has order 64; any normal subgroup
        of order 24 or 1920 would lie inside Nsmall -> Lagrange kill.
        Structure of N64 and G/N64 = Sp4(2) (order 720) via the conjugation
        action on N/Z = F2^4 with its commutator symplectic form
        -> G = (Z4 o 2^{1+4}) . Sp4(2), computed not cited.
  T1.5  stronger: W(D5) = Z2^4 : S5 has NO faithful complex rep of dim <= 4
        (S5-orbits on the nonzero dual of the sign module have sizes 5, 10;
        a faithful dim-<=4 rep needs an S5-invariant spanning character set
        of size <= 4) -> W(D5) embeds in NO rank-4 group, hence not in G31.
        S4 = W(A3) DOES embed (pair permutations, contains sigma).
  T1.6  compiler anchoring: J, sigma, c = J o sigma in G; exact identities
        sigma = c^4, J = c^9 (<c> = <J,sigma> = Z12, the mu4 center is a
        POWER of the clock); root stabilizer order 192 = <15 reflections>
        (Steinberg), restricted degrees (4,6,8) -> G(4,2,3) fingerprint;
        line stabilizer 768 = Z4 x rootstab; sigma / c NOT in P; |G cap P|
        for standard and random W(E8)-conjugate positions.

TEST 2 -- degree fingerprints
  Eigenvalue census of all 46080 matrices: exactly 60 reflections, all of
  order 2 (zeta = i quasi-reflections preserving the roots: 0).  Molien
  series -> invariant degrees; uniqueness of (8,12,20,24) among ALL divisor
  quadruples with product 46080; sum(d-1) = 60, prod d = |G|.  Springer
  fingerprint: regular elements of orders 8/12/20/24 with centralizer
  orders 192/288/20/24.  HONEST: the v629 clock c = J o sigma is NOT
  zeta12-regular (census 19 x 12 + 3 x 4, |C(c)| = 72 -- v629 R2 KILL
  reproduced); the free 20 = 240/12 comb belongs to the REGULAR
  12-element of G31, a different conjugacy class.

TEST 3 -- controls
  ST29 (order 7680, 40 reflections, degrees 4,8,12,20) and ST32 (order
  155520, 80 reflections, degrees 12,18,24,30) killed by >= 3 measured
  numbers each.  Molien machinery positive controls: W(D5) 5-dim ->
  degrees (2,4,5,6,8); S4 4-dim permutation rep -> (1,2,3,4).

FIREWALL: no marker changes; the numerology kill (|G31| = |W(D5)|*|W(A3)|
carries NO subgroup structure) is a typed negative; the clock-is-not-
regular finding reproduces the v629 R2 KILL one level deeper; typed
observations only.

PROVENANCE: discovery probe st31_structure_probe.py (2026-08-02, 56/56,
verdicts KILL (subgroup) + CONFIRMED (embedding, degrees) + PASS
(controls)).

Python-only (exact integer combinatorics + sympy Schreier-Sims),
counted per GATE.WOLFRAM.02.
"""
import itertools
import random
import time
from collections import Counter
from math import gcd, lcm

import numpy as np

T0 = time.time()
CHECKS = []
N240 = 240


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ================================================================ S0: roots
section("S0: roots, J, sigma (doubled integer coordinates)")

_roots = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        _roots.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        _roots.append(v)
RD = np.array(sorted(_roots), dtype=np.int64)          # 240 x 8, doubled
ridx = {tuple(int(a) for a in RD[i]): i for i in range(N240)}
check("S0.1 240 doubled-integer E8 roots reconstructed", RD.shape == (240, 8))


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
IDP = np.arange(N240, dtype=np.int16)


def comp(p, q):
    """(p o q)[i] = p[q[i]]  (apply q first, then p)."""
    return p[q]


def pinv(p):
    return np.argsort(p).astype(np.int16)


def perm_order(p):
    n = 1
    seen = np.zeros(N240, dtype=bool)
    for s in range(N240):
        if seen[s]:
            continue
        ln = 0
        j = s
        while not seen[j]:
            seen[j] = True
            j = int(p[j])
            ln += 1
        n = lcm(n, ln)
    return n


check("S0.2 J free of order 4, sigma of order 3, [J,sigma] = 0",
      perm_order(Jperm) == 4 and perm_order(sigperm) == 3
      and np.array_equal(comp(Jperm, sigperm), comp(sigperm, Jperm))
      and not np.any(Jperm == IDP))

line_of = np.full(N240, -1, dtype=np.int32)
line_reps = []
for i in range(N240):
    if line_of[i] >= 0:
        continue
    orb = [i, int(Jperm[i]), int(Jperm[Jperm[i]]), int(Jperm[Jperm[Jperm[i]]])]
    for j in orb:
        line_of[j] = len(line_reps)
    line_reps.append(i)
check("S0.3 EXACTLY 60 J-orbits (lines) of size 4", len(line_reps) == 60)

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
row0 = sorted(Counter(int(x) for x in absH2[0]).items())
row_reg = all(sorted(Counter(int(x) for x in absH2[a]).items()) == row0
              for a in range(60))
check("S0.4 line Gram |H|^2 row profile %s (row-regular: %s)"
      % (row0, row_reg), row_reg)
ORTH_PER_LINE = int(np.sum(absH2[0] == 0)) - (1 if absH2[0, 0] == 0 else 0)
print("      lines hermitian-orthogonal to a given line: %d" % ORTH_PER_LINE)

# ================================================== S1: reflections and G
section("S1: the 60 reflections and the group G on the 240 roots")

refl_perms = []
for a in range(60):
    vi = line_reps[a]
    re4, im4 = herm4_rowvec(vi)
    assert np.all(re4 % 4 == 0) and np.all(im4 % 4 == 0)
    re, im = re4 // 4, im4 // 4
    Y = RD - re[:, None] * RD[vi][None, :] - im[:, None] * JRD[vi][None, :]
    refl_perms.append(np.array([ridx[tuple(int(t) for t in Y[i])]
                                for i in range(N240)], dtype=np.int16))
ok_inv = all(np.array_equal(comp(p, p), IDP) for p in refl_perms)
n_distinct = len({p.tobytes() for p in refl_perms})
check("S1.1 60 distinct order-2 reflection permutations preserve the roots",
      ok_inv and n_distinct == 60, "distinct: %d" % n_distinct)

ok4 = 0
for a in range(60):
    vi = line_reps[a]
    re4, im4 = herm4_rowvec(vi)
    cr4, ci4 = (re4 + im4), (im4 - re4)
    num_r = RD * 8 - cr4[:, None] * RD[vi][None, :] - ci4[:, None] * JRD[vi][None, :]
    if np.all(num_r % 8 == 0):
        Y = num_r // 8
        if all(tuple(int(t) for t in Y[i]) in ridx for i in range(N240)):
            ok4 += 1
check("S1.2 order-4 (zeta=i) reflections preserving the root set: %d "
      "(0 expected: the stabilizer has only order-2 reflections)" % ok4,
      ok4 == 0)


def bfs_group(gens, cap=50000):
    seen = {IDP.tobytes(): IDP}
    frontier = [IDP]
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
Gset, complete = bfs_group(refl_perms)
check("S1.3 |<60 reflections>| = %d on the 240 roots (BFS, %.1f s) -- "
      "prediction 46080 = 8*12*20*24" % (len(Gset), time.time() - t),
      complete and len(Gset) == 46080)

gens_small = None
rng_g = random.Random(11)
for size in (5, 6, 7):
    for _ in range(120):
        cand_g = [refl_perms[i] for i in rng_g.sample(range(60), size)]
        sub, _ = bfs_group(cand_g)
        if len(sub) == 46080:
            gens_small = cand_g
            break
    if gens_small is not None:
        break
if gens_small is None:
    gens_small = refl_perms
check("S1.4 small generating set: %d reflections suffice to generate G "
      "(G31 is NOT well-generated: rank 4 but needs 5 generators)"
      % len(gens_small), 5 <= len(gens_small) <= 7)

try:
    from sympy.combinatorics import Permutation, PermutationGroup
    t = time.time()
    sympy_G = PermutationGroup([Permutation(p.tolist()) for p in gens_small])
    so = sympy_G.order()
    check("S1.5 independent sympy Schreier-Sims order: %d (%.1f s)"
          % (so, time.time() - t), so == 46080)
except Exception as e:  # pragma: no cover
    check("S1.5 sympy cross-check ran", False, repr(e))

line_perm_bytes = set()
for p in Gset.values():
    line_perm_bytes.add(line_of[p[line_reps]].astype(np.int16).tobytes())
check("S1.6 induced action on the 60 lines has order %d = 46080/4 "
      "(kernel = mu4 scalars)" % len(line_perm_bytes),
      len(line_perm_bytes) == 11520)
check("S1.7 J (the mu4 scalar) is GENERATED by the 60 reflections: J in G",
      Jperm.tobytes() in Gset)

# ============================== S2: G = FULL unitary stabilizer (exact)
section("S2: exact count of ALL unitary maps preserving the root set")


def gmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def gdet4(M):
    tot = (0, 0)
    for perm in itertools.permutations(range(4)):
        sgn = 1
        for a in range(4):
            for b in range(a + 1, 4):
                if perm[a] > perm[b]:
                    sgn = -sgn
        term = (sgn, 0)
        for r in range(4):
            term = gmul(term, M[r][perm[r]])
        tot = (tot[0] + term[0], tot[1] + term[1])
    return tot


random.seed(0)
basis = None
for _ in range(50000):
    cand = random.sample(range(60), 4)
    M4 = [[(int(HG[a, b, 0]), int(HG[a, b, 1])) for b in cand] for a in cand]
    if gdet4(M4) == (1, 0):
        basis = [line_reps[a] for a in cand]
        break
check("S2.1 hermitian-unimodular Z[i]-basis among the line reps: %s"
      % (basis,), basis is not None)

t = time.time()
val_index = []
for i in range(N240):
    re4, im4 = herm4_rowvec(i)
    d = {}
    for j in range(N240):
        d.setdefault((int(re4[j]) // 4, int(im4[j]) // 4), set()).add(j)
    val_index.append(d)


def hval(i, j):
    return (int(RD[i] @ RD[j]) // 4, int(RD[i] @ JRD[j]) // 4)


b1, b2, b3, b4 = basis
g12, g13, g14 = hval(b1, b2), hval(b1, b3), hval(b1, b4)
g23, g24, g34 = hval(b2, b3), hval(b2, b4), hval(b3, b4)
count = 0
for r1 in range(N240):
    for r2 in val_index[r1].get(g12, ()):
        c3 = val_index[r1].get(g13, set()) & val_index[r2].get(g23, set())
        for r3 in c3:
            c4 = (val_index[r1].get(g14, set())
                  & val_index[r2].get(g24, set())
                  & val_index[r3].get(g34, set()))
            count += len(c4)
check("S2.2 EXACT count of unitary root-set automorphisms = %d (%.1f s): "
      "every Gram-matching image of a unimodular basis extends to a "
      "unitary automorphism of the Z[i]-E8 lattice, and those preserve "
      "{v : H(v,v) = 2} = the 240 roots" % (count, time.time() - t),
      count == 46080)
check("S2.3 => G (generated by the 60 reflections) IS the full unitary "
      "stabilizer of the mu4-quotient structure", count == len(Gset))

Rc = (RD[:, 0::2] + 1j * RD[:, 1::2]) / 2.0          # 240 x 4 complex
Bmat = Rc[list(basis)].T
Binv = np.linalg.inv(Bmat)
Eall = np.stack(list(Gset.values()))                 # 46080 x 240
elem_bytes = [p.tobytes() for p in Gset.values()]
byte2row = {b: i for i, b in enumerate(elem_bytes)}
Bimg = Rc[Eall[:, list(basis)]].transpose(0, 2, 1)   # 46080 x 4 x 4
Mall = Bimg @ Binv[None, :, :]
dev = float(np.max(np.abs(2 * Mall - np.round(2 * Mall.real)
                          - 1j * np.round(2 * Mall.imag))))
spot = np.random.default_rng(1).integers(0, len(Eall), 12)
ok_map = all(np.allclose(Rc @ Mall[i].T, Rc[Eall[i]]) for i in spot)
check("S2.4 4x4 matrices for all 46080 elements are half-Gaussian-integral "
      "(max dev %.1e) and reproduce the root permutations (12 spot checks)"
      % dev, dev < 1e-9 and ok_map)

# ============================== S3: P = W(D5) x W(A3) on the SAME roots
section("S3: the compiler glue group P = W(D5) x W(A3) inside W(E8)")


def real_refl_perm(rd):
    ip4 = RD @ rd
    Y = RD - (ip4 // 4)[:, None] * rd[None, :]
    return np.array([ridx[tuple(int(t) for t in Y[i])]
                     for i in range(N240)], dtype=np.int16)


def rt(*pairs):
    v = np.zeros(8, dtype=np.int64)
    for i, s in pairs:
        v[i] = 2 * s
    return v


d5_gens = [real_refl_perm(rt((0, 1), (1, -1))),
           real_refl_perm(rt((1, 1), (2, -1))),
           real_refl_perm(rt((2, 1), (3, -1))),
           real_refl_perm(rt((3, 1), (4, -1))),
           real_refl_perm(rt((3, 1), (4, 1)))]
a3_gens = [real_refl_perm(rt((5, 1), (6, -1))),
           real_refl_perm(rt((6, 1), (7, -1))),
           real_refl_perm(rt((6, 1), (7, 1)))]
D5set, _ = bfs_group(d5_gens)
A3set, _ = bfs_group(a3_gens)
t = time.time()
Pset, _ = bfs_group(d5_gens + a3_gens)
commute = all(np.array_equal(comp(a, b), comp(b, a))
              for a in d5_gens for b in a3_gens)
check("S3.1 |W(D5)| = %d, |W(A3)| = %d, factors commute, intersection %d"
      % (len(D5set), len(A3set), len(set(D5set) & set(A3set))),
      len(D5set) == 1920 and len(A3set) == 24 and commute
      and len(set(D5set) & set(A3set)) == 1)
check("S3.2 |P| = |W(D5) x W(A3)| = %d = 46080 = |G31| (%.1f s) -- "
      "the numerological twin, realized on the SAME 240 roots"
      % (len(Pset), time.time() - t), len(Pset) == 46080)

# ======================= S4: abstract invariants -> isomorphism kill
section("S4: TEST 1a -- cheap invariants: G31 vs W(D5) x W(A3)")


def center_elems(elem_stack, gens):
    mask = np.ones(len(elem_stack), dtype=bool)
    for g in gens:
        mask &= np.all(elem_stack[:, g] == g[elem_stack], axis=1)
    return elem_stack[mask]


ZG = center_elems(Eall, list(gens_small))
Epn = np.stack(list(Pset.values()))
ZP = center_elems(Epn, d5_gens + a3_gens)
J2 = comp(Jperm, Jperm)
J3 = comp(Jperm, J2)
zg_ok = (len(ZG) == 4 and {z.tobytes() for z in ZG} ==
         {IDP.tobytes(), Jperm.tobytes(), J2.tobytes(), J3.tobytes()})
check("S4.1 |Z(G31)| = %d (= the mu4 scalars {1, J, -1, J^3}); |Z(P)| = %d"
      % (len(ZG), len(ZP)), zg_ok and len(ZP) == 1)
check("S4.2 KILL: G31 is NOT isomorphic to W(D5) x W(A3) "
      "(centers of order 4 vs 1)", len(ZG) != len(ZP))

t = time.time()
ordG_arr = np.array([perm_order(Eall[i]) for i in range(len(Eall))])
ordP_arr = np.array([perm_order(Epn[i]) for i in range(len(Epn))])
ordG = Counter(ordG_arr.tolist())
ordP = Counter(ordP_arr.tolist())
print("      order spectrum G31 (%.1f s): %s"
      % (time.time() - t, dict(sorted(ordG.items()))))
print("      order spectrum P        : %s" % dict(sorted(ordP.items())))
diff_orders = sorted(set(ordG) ^ set(ordP))
check("S4.3 element-order spectra differ (orders present in exactly one "
      "group: %s)" % diff_orders, ordG != ordP)


def derived_subgroup(genset, ambient_gens):
    """exact derived subgroup: normal closure of commutators of genset."""
    def commut(x, y):
        return comp(comp(x, y), comp(pinv(x), pinv(y)))

    gens_h = []
    seen_seed = set()
    for x in genset:
        for y in genset:
            c = commut(x, y)
            b = c.tobytes()
            if b != IDP.tobytes() and b not in seen_seed:
                seen_seed.add(b)
                gens_h.append(c)
            if len(gens_h) >= 10:
                break
        if len(gens_h) >= 10:
            break
    if not gens_h:
        return {IDP.tobytes(): IDP}, [IDP]
    while True:
        H, _ = bfs_group(gens_h)
        missing = None
        for x in genset:
            for y in genset:
                c = commut(x, y)
                if c.tobytes() not in H:
                    missing = c
                    break
            if missing is not None:
                break
        if missing is None:
            for g in ambient_gens:
                gi = pinv(g)
                for h in gens_h:
                    c = comp(g, comp(h, gi))
                    if c.tobytes() not in H:
                        missing = c
                        break
                if missing is not None:
                    break
        if missing is None:
            return H, gens_h
        gens_h.append(missing)


t = time.time()
Gp, Gp_gens = derived_subgroup(list(gens_small), list(gens_small))
Gpp, _ = derived_subgroup(Gp_gens, Gp_gens)
Pp, Pp_gens = derived_subgroup(d5_gens + a3_gens, d5_gens + a3_gens)
Ppp, Ppp_gens = derived_subgroup(Pp_gens, Pp_gens)
Pppp, _ = derived_subgroup(Ppp_gens, Ppp_gens)
print("      derived series computed in %.1f s" % (time.time() - t))
check("S4.4 derived series: G31: 46080 > %d >= %d ; "
      "P: 46080 > %d > %d > %d"
      % (len(Gp), len(Gpp), len(Pp), len(Ppp), len(Pppp)),
      len(Gp) == 23040 and len(Pp) == 11520)
check("S4.5 KILL confirmed twice more: abelianizations |G/G'| = %d vs "
      "|P/P'| = %d; derived-series profiles differ"
      % (46080 // len(Gp), 46080 // len(Pp)),
      46080 // len(Gp) != 46080 // len(Pp))

# ============ S5: conjugacy classes, normal lattice, semidirect kill
section("S5: TEST 1a -- normal subgroups: no order-24 / order-1920 factor")

t = time.time()
conj_gens = [(g, pinv(g)) for g in gens_small]
class_id = np.full(len(Eall), -1, dtype=np.int32)
class_reps = []
for i in range(len(Eall)):
    if class_id[i] >= 0:
        continue
    cid = len(class_reps)
    class_reps.append(i)
    stack = [Eall[i]]
    class_id[i] = cid
    while stack:
        x = stack.pop()
        for g, gi in conj_gens:
            y = g[x[gi]]
            r = byte2row[y.tobytes()]
            if class_id[r] < 0:
                class_id[r] = cid
                stack.append(y)
n_classes = len(class_reps)
class_sizes = Counter(class_id.tolist())
refl_classes = sorted({int(class_id[byte2row[p.tobytes()]])
                       for p in refl_perms})
check("S5.1 conjugacy classes of G31: %d (%.1f s); the 60 reflections form "
      "%d class(es)" % (n_classes, time.time() - t, len(refl_classes)),
      sum(class_sizes.values()) == 46080)

CAP = 1921
small_class_elems = []
closure_info = []
id_row = byte2row[IDP.tobytes()]
for cid in range(n_classes):
    rows = np.where(class_id == cid)[0]
    if len(rows) == 1 and rows[0] == id_row:
        continue
    gens_c = [Eall[rows[0]]]
    while True:
        H, full = bfs_group(gens_c, cap=CAP)
        if not full:
            closure_info.append((len(rows), ">%d" % (CAP - 1)))
            break
        missing = next((r for r in rows if Eall[r].tobytes() not in H), None)
        if missing is None:
            closure_info.append((len(rows), len(H)))
            small_class_elems.extend(Eall[r] for r in rows)
            break
        gens_c.append(Eall[missing])
small_orders = sorted({c for _, c in closure_info if isinstance(c, int)})
print("      (class size, normal-closure order) for all %d nontrivial "
      "classes: %s" % (len(closure_info), sorted(closure_info,
                                                 key=lambda x: str(x))))
if small_class_elems:
    Nsmall, _ = bfs_group(small_class_elems, cap=10000)
else:
    Nsmall = {IDP.tobytes(): IDP}
n64 = len(Nsmall)
check("S5.2 join of ALL small (<= 1920) class closures: |Nsmall| = %d; "
      "small closure orders seen: %s" % (n64, small_orders), True)
check("S5.3 KILL: any normal subgroup H with |H| in {24, 1920} satisfies "
      "H <= Nsmall (each of its elements has normal closure <= |H|), but "
      "|Nsmall| = %d, and 24 does not divide %d, 1920 > %d -> G31 is NOT "
      "a direct OR semidirect product W(D5) x| W(A3) in either order"
      % (n64, n64, n64),
      n64 == 64 and n64 % 24 != 0 and n64 < 1920)

Nstack = np.stack(list(Nsmall.values()))
ordN = Counter(perm_order(x) for x in Nstack)
ZN = center_elems(Nstack, list(Nsmall.values()))
Np, _ = derived_subgroup([Nstack[i] for i in range(len(Nstack))],
                         [Nstack[i] for i in range(len(Nstack))])
zbytes = {z.tobytes() for z in ZG}
zin = zbytes <= set(Nsmall.keys())
sq_central = all(comp(x, x).tobytes() in zbytes for x in Nstack)
check("S5.4 N64 structure: order census %s, |Z(N64)| = %d, |N64'| = %d, "
      "Z(G) <= N64: %s, all squares central: %s -> the central product "
      "Z4 o 2^(1+4)" % (dict(sorted(ordN.items())), len(ZN), len(Np),
                        zin, sq_central),
      len(ZN) == 4 and len(Np) == 2 and zin and sq_central)

# G/N64 -> Sp4(2) via conjugation on N/Z = F2^4
vgens = []


def build_span(vg):
    span = {}
    for bits in itertools.product((0, 1), repeat=len(vg)):
        w = IDP
        for bit, gv in zip(bits, vg):
            if bit:
                w = comp(w, gv)
        vec = tuple(bits) + (0,) * (4 - len(vg))
        for z in ZG:
            span[comp(w, z).tobytes()] = vec
    return span


span = build_span(vgens)
for x in Nstack:
    if x.tobytes() in span:
        continue
    vgens.append(x)
    span = build_span(vgens)
    if len(vgens) == 4:
        break
coset_vec = span
check("S5.5 N64 / Z(G) = F2^4: 4 generators label all 64 elements",
      len(vgens) == 4 and len(coset_vec) == 64)

zc = next(z for z in ZG if perm_order(z) == 2)       # central involution -1


def commutator(x, y):
    return comp(comp(x, y), comp(pinv(x), pinv(y)))


PB = np.zeros((4, 4), dtype=np.int64)
pair_ok = True
for i in range(4):
    for j in range(4):
        c = commutator(vgens[i], vgens[j])
        if c.tobytes() == IDP.tobytes():
            PB[i, j] = 0
        elif c.tobytes() == zc.tobytes():
            PB[i, j] = 1
        else:
            pair_ok = False
check("S5.6 commutator pairing on F2^4 lands in N' = {1, -1}; Gram of the "
      "symplectic form:\n      %s" % PB.tolist(),
      pair_ok and np.array_equal(PB, PB.T)
      and int(round(abs(np.linalg.det(PB.astype(float))))) % 2 == 1)


def qmat(g):
    gi = pinv(g)
    cols = [coset_vec[comp(g, comp(nk, gi)).tobytes()] for nk in vgens]
    return tuple(tuple(cols[k][r] for k in range(4)) for r in range(4))


def mat2mul(A, B):
    return tuple(tuple(sum(A[r][k] * B[k][c] for k in range(4)) % 2
                       for c in range(4)) for r in range(4))


I4 = tuple(tuple(1 if r == c else 0 for c in range(4)) for r in range(4))
qgens = [qmat(g) for g in gens_small]
g1, g2 = gens_small[0], gens_small[1]
hom_ok = qmat(comp(g1, g2)) == mat2mul(qmat(g1), qmat(g2))
img = {I4}
frontier = [I4]
while frontier:
    nxt = []
    for A in frontier:
        for B in qgens:
            C = mat2mul(A, B)
            if C not in img:
                img.add(C)
                nxt.append(C)
    frontier = nxt
sympl = all(np.array_equal(
    np.array(mat2mul(mat2mul(tuple(zip(*A)), tuple(map(tuple, PB.tolist()))),
                     A)), PB % 2) for A in img)
ker_order = 46080 // len(img)
n_in_ker = all(qmat(Nstack[i]) == I4 for i in range(0, 64, 7))
check("S5.7 conjugation action on N/Z: image order %d = |Sp4(2)| = 720, "
      "symplectic-form preserving: %s, hom spot check: %s, kernel order "
      "%d = |N64| (and N64 <= kernel) -> G31/N64 = Sp4(2) [= S6], i.e. "
      "G31 = (Z4 o 2^(1+4)).Sp4(2) -- COMPUTED, not guessed"
      % (len(img), sympl, hom_ok, ker_order),
      len(img) == 720 and sympl and hom_ok and ker_order == 64 and n_in_ker)

# ==================== S6: W(D5) cannot live in rank 4 at all
section("S6: TEST 1a -- W(D5) has no faithful complex rep of dim <= 4")

# A = even sign group = Z2^4; characters of A = F2^5 / <(1,...,1)>;
# S5 permutes coordinates. Any faithful rep of dim <= 4 restricted to A
# gives an S5-invariant set of <= 4 characters whose joint kernel is
# trivial, i.e. a spanning set of the 4-dim dual -- must have >= 4 and
# be a union of S5-orbits.
allv = list(itertools.product((0, 1), repeat=5))
ONE = (1, 1, 1, 1, 1)


def cls(v):
    w = tuple((a + 1) % 2 for a in v)
    return min(v, w)


classes = sorted({cls(v) for v in allv if cls(v) != cls((0,) * 5)})
orbits = []
seen_c = set()
for c0 in classes:
    if c0 in seen_c:
        continue
    orb = {c0}
    frontier = [c0]
    while frontier:
        x = frontier.pop()
        for i in range(4):
            y = list(x)
            y[i], y[i + 1] = y[i + 1], y[i]
            y = cls(tuple(y))
            if y not in orb:
                orb.add(y)
                frontier.append(y)
    seen_c |= orb
    orbits.append(len(orb))
check("S6.1 S5-orbit sizes on the 15 nontrivial characters of Z2^4: %s "
      "(weights {1,4} and {2,3})" % sorted(orbits),
      sorted(orbits) == [5, 10] and len(classes) == 15)
check("S6.2 KILL (stronger): a faithful rep of W(D5) with dim <= 4 needs "
      "an S5-invariant spanning character set of size <= 4; the smallest "
      "nonempty invariant set has size 5 -> W(D5) has NO faithful complex "
      "rep of dim <= 4 -> W(D5) embeds in NO subgroup of GL(4,C), in "
      "particular NOT in G31 (min faithful dim = 5 = its reflection rep)",
      min(orbits) == 5)

# ==================== S7: compiler data inside G31 (TEST 1b)
section("S7: TEST 1b -- the compiler elements J, sigma, clock c in G31")

c_perm = comp(Jperm, sigperm)
c2 = comp(c_perm, c_perm)
c4 = comp(c2, c2)
c8 = comp(c4, c4)
c9 = comp(c8, c_perm)
check("S7.1 memberships: J in G31: %s, sigma in G31: %s, c = J o sigma in "
      "G31: %s, ord(c) = %d"
      % (Jperm.tobytes() in Gset, sigperm.tobytes() in Gset,
         c_perm.tobytes() in Gset, perm_order(c_perm)),
      Jperm.tobytes() in Gset and sigperm.tobytes() in Gset
      and c_perm.tobytes() in Gset and perm_order(c_perm) == 12)
check("S7.2 EXACT clock identities: sigma = c^4 and J = c^9, so "
      "<c> = <J, sigma> = Z12 and the mu4 CENTER is a power of the clock",
      np.array_equal(c4, sigperm) and np.array_equal(c9, Jperm))

pair_perm_bytes = set()
for p4 in itertools.permutations(range(4)):
    idxmap = np.empty(8, dtype=np.int64)
    for k2 in range(4):
        idxmap[2 * k2] = 2 * p4[k2]
        idxmap[2 * k2 + 1] = 2 * p4[k2] + 1
    pair_perm_bytes.add(perm_from_map(lambda x: x[idxmap]).tobytes())
s4_in_g = all(b in Gset for b in pair_perm_bytes)
check("S7.3 W(A3) = S4 EMBEDS: the 24 coordinate-pair permutations all lie "
      "in G31 and contain sigma", s4_in_g and len(pair_perm_bytes) == 24
      and sigperm.tobytes() in pair_perm_bytes)

check("S7.4 sigma and c do NOT lie in the glue product P (standard "
      "position): sigma in P: %s, c in P: %s"
      % (sigperm.tobytes() in Pset, c_perm.tobytes() in Pset),
      sigperm.tobytes() not in Pset and c_perm.tobytes() not in Pset)

GB, PBset = set(Gset.keys()), set(Pset.keys())
inters = [len(GB & PBset)]
rng = random.Random(7)
for _ in range(3):
    w = IDP
    for _ in range(25):
        w = comp(w, real_refl_perm(RD[rng.randrange(240)]))
    wi = pinv(w)
    conjP = {w[Epn[i][wi]].tobytes() for i in range(len(Epn))}
    inters.append(len(GB & conjP))
check("S7.5 |G31 cap P| inside W(E8): standard position %d; three random "
      "W(E8)-conjugate positions of P: %s (position-dependent, never a "
      "common order-46080 subgroup -- consistent with non-isomorphy)"
      % (inters[0], inters[1:]), all(x < 46080 for x in inters))

# ==================== S8: stabilizers (the 768 question)
section("S8: TEST 1b -- root and line stabilizers in G31")

r0 = line_reps[0]
orbit_roots = len(set(Eall[:, r0].tolist()))
orbit_lines = len(set(line_of[Eall[:, r0]].tolist()))
stab_rows = np.where(Eall[:, r0] == r0)[0]
lstab_rows = np.where(line_of[Eall[:, r0]] == 0)[0]
check("S8.1 G31 transitive on the 240 roots (orbit %d) and 60 lines "
      "(orbit %d); |Stab(root)| = %d = 46080/240, |Stab(line)| = %d "
      "= 46080/60" % (orbit_roots, orbit_lines, len(stab_rows),
                      len(lstab_rows)),
      orbit_roots == 240 and orbit_lines == 60
      and len(stab_rows) == 192 and len(lstab_rows) == 768)

fix_refl = [p for p in refl_perms if p[r0] == r0]
Hfix, _ = bfs_group(fix_refl)
check("S8.2 reflections fixing the root: %d (= lines hermitian-orthogonal "
      "to it: %d); they generate the FULL root stabilizer: |<refl_fix>| = "
      "%d = 192 (Steinberg)" % (len(fix_refl), ORTH_PER_LINE, len(Hfix)),
      len(fix_refl) == 15 and len(Hfix) == 192
      and set(Hfix.keys()) == {Eall[i].tobytes() for i in stab_rows})

zprod = {comp(z, Eall[i]).tobytes() for z in ZG for i in stab_rows}
check("S8.3 line stabilizer = Z4 x Stab(root): 4 * 192 = %d elements, set "
      "equality with the 768 line-stabilizing elements: %s"
      % (len(zprod), zprod == {Eall[i].tobytes() for i in lstab_rows}),
      len(zprod) == 768
      and zprod == {Eall[i].tobytes() for i in lstab_rows})

# restricted Molien of Stab(root) on the 3-dim orthogonal complement
w0 = Rc[r0]
A1 = w0.conj().reshape(1, 4)
_, _, vh = np.linalg.svd(A1)
Q3 = vh[1:].conj().T                                  # 4 x 3
Mstab = Mall[stab_rows]
M3 = np.einsum('ij,njk,kl->nil', Q3.conj().T, Mstab, Q3)


def eig_census(mats, orders):
    cen = Counter()
    bad = 0
    ev = np.linalg.eigvals(mats)
    for i in range(len(mats)):
        n = int(orders[i])
        ks = []
        for lam in ev[i]:
            k = int(round((np.angle(lam) * n) / (2 * np.pi))) % n
            if abs(lam - np.exp(2j * np.pi * k / n)) > 1e-5:
                bad += 1
            g_ = gcd(k, n)
            ks.append((k // g_, n // g_))
        cen[tuple(sorted(ks))] += 1
    return cen, bad


def molien(census, order, N=28):
    tot = np.zeros(N + 1, dtype=complex)
    for key, cnt in census.items():
        c = np.zeros(N + 1, dtype=complex)
        c[0] = 1.0
        for (k, n) in key:
            lam = np.exp(2j * np.pi * k / n)
            powv = lam ** np.arange(N + 1)
            d = np.empty(N + 1, dtype=complex)
            for m in range(N + 1):
                d[m] = np.dot(c[:m + 1], powv[:m + 1][::-1])
            c = d
        tot += cnt * c
    tot /= order
    assert np.max(np.abs(tot.imag)) < 1e-6
    coef = np.round(tot.real).astype(int)
    assert np.max(np.abs(tot.real - coef)) < 1e-6
    return coef


def degrees_series(degs, N=28):
    c = np.zeros(N + 1, dtype=int)
    c[0] = 1
    for d in degs:
        for m in range(d, N + 1):
            c[m] += c[m - d]
    return c


cen3, bad3 = eig_census(M3, ordG_arr[stab_rows])
mol3 = molien(cen3, 192, N=14)
check("S8.4 Stab(root): restricted Molien on the complement matches "
      "degrees (4,6,8): %s -- with order 192 and 15 reflections this is "
      "the G(4,2,3) fingerprint [768-group = Z4 x G(4,2,3)]"
      % np.array_equal(mol3, degrees_series([4, 6, 8], N=14)),
      bad3 == 0 and np.array_equal(mol3, degrees_series([4, 6, 8], N=14)))

s4_found = False
S4_SPEC = Counter({1: 1, 2: 9, 3: 8, 4: 6})
for trip in itertools.combinations(range(15), 3):
    Ht, full = bfs_group([fix_refl[i] for i in trip], cap=30)
    if full and len(Ht) == 24:
        spec = Counter(perm_order(x) for x in Ht.values())
        if spec == S4_SPEC:
            s4_found = True
            break
check("S8.5 Stab(root) contains W(A3) = S4 (generated by 3 of its 15 "
      "reflections); W(D5) cannot (order 1920 > 768, and S6.2)", s4_found)

# ==================== S9: TEST 2 -- degree fingerprints
section("S9: TEST 2 -- reflection census, Molien series, degrees")

t = time.time()
cenG, badG = eig_census(Mall, ordG_arr)
refl_keys = [k for k in cenG
             if sorted(k).count((0, 1)) == 3 and k != ((0, 1),) * 4]
n_refl = sum(cenG[k] for k in refl_keys)
refl_orders = sorted({n for k in refl_keys for (kk, n) in k if n > 1})
check("S9.1 eigenvalue census over all 46080 matrices (%.1f s, %d distinct "
      "spectra, %d angle failures): EXACTLY %d reflections, nontrivial "
      "eigenvalue orders %s (all order 2 <=> Sum(d_i - 1) = 60)"
      % (time.time() - t, len(cenG), badG, n_refl, refl_orders),
      badG == 0 and n_refl == 60 and refl_orders == [2])

molG = molien(cenG, 46080, N=28)
target = degrees_series([8, 12, 20, 24], N=28)
check("S9.2 Molien series of G31 = prod 1/(1-t^d) for degrees (8,12,20,24) "
      "up to t^28: %s\n      coefficients: %s"
      % (np.array_equal(molG, target), molG.tolist()),
      np.array_equal(molG, target))

divs = [d for d in range(1, 46081) if 46080 % d == 0]
matches = []
for i1, d1 in enumerate(divs):
    if d1 ** 4 > 46080:
        break
    for i2 in range(i1, len(divs)):
        d2 = divs[i2]
        if 46080 % (d1 * d2) or d1 * d2 * d2 * d2 > 46080:
            continue
        for i3 in range(i2, len(divs)):
            d3 = divs[i3]
            r = 46080 // (d1 * d2)
            if r % d3 or d3 * d3 > r:
                continue
            d4 = r // d3
            if np.array_equal(molG, degrees_series([d1, d2, d3, d4], N=28)):
                matches.append((d1, d2, d3, d4))
check("S9.3 UNIQUENESS: among ALL divisor quadruples with product 46080, "
      "the Molien series matches only %s" % matches,
      matches == [(8, 12, 20, 24)])
check("S9.4 exact consistency: 8*12*20*24 = %d = |G31|; 7+11+19+23 = %d "
      "= number of reflections = number of hyperplanes"
      % (8 * 12 * 20 * 24, 7 + 11 + 19 + 23),
      8 * 12 * 20 * 24 == 46080 and 7 + 11 + 19 + 23 == 60 == n_refl)

# ==================== S10: Springer fingerprint + the v629 clock
section("S10: TEST 2 -- regular elements: orders (8,12,20,24), "
        "centralizers (192,288,20,24)")

LINESC = np.conj(Rc[line_reps])                       # 60 x 4
rng_reg = np.random.default_rng(123)


def is_regular(row, d):
    """some vector in a primitive-d eigenspace avoids all 60 hyperplanes
    (handles DEGENERATE eigenvalues via random eigenspace combinations)."""
    M = Mall[row]
    lam_all = np.linalg.eigvals(M)
    for k in range(1, d):
        if gcd(k, d) != 1:
            continue
        z = np.exp(2j * np.pi * k / d)
        if np.min(np.abs(lam_all - z)) > 1e-6:
            continue
        A = M - z * np.eye(4)
        _, sv, vh = np.linalg.svd(A)
        dim = int(np.sum(sv < 1e-8))
        if dim == 0:
            continue
        Bas = vh[4 - dim:].conj().T
        for _ in range(50):
            e = Bas @ (rng_reg.normal(size=dim)
                       + 1j * rng_reg.normal(size=dim))
            if np.min(np.abs(LINESC @ e)) > 1e-6 * np.linalg.norm(e):
                return True
    return False


def orbit_census(p):
    cen = Counter()
    seen_o = np.zeros(N240, dtype=bool)
    for s in range(N240):
        if seen_o[s]:
            continue
        ln, j = 0, s
        while not seen_o[j]:
            seen_o[j] = True
            j = int(p[j])
            ln += 1
        cen[ln] += 1
    return cen


def centralizer_order(row):
    x = Eall[row]
    return int(np.sum(np.all(Eall[:, x] == x[Eall], axis=1)))


DEGS = [8, 12, 20, 24]
# product of the degrees divisible by d (Springer prediction)
exp_cent = {d: int(np.prod([e for e in DEGS if e % d == 0])) for d in DEGS}
# regular elements form whole conjugacy classes -> test one rep per class
reg_witness = {}
for d in DEGS:
    rows = np.where(ordG_arr == d)[0]
    creps = [r for r in class_reps if ordG_arr[r] == d]
    found = None
    n_reg_cls = 0
    for row in creps:
        if is_regular(row, d):
            n_reg_cls += 1
            if found is None:
                found = row
    cen = centralizer_order(found) if found is not None else -1
    rcen = orbit_census(Eall[found]) if found is not None else {}
    reg_witness[d] = (found, cen, dict(rcen))
    ok = found is not None and cen == exp_cent[d]
    check("S10.%d regular element of order %d exists (%d of %d classes of "
          "that order are regular; %d elements of order %d in G31), "
          "centralizer order %d = product of degrees divisible by %d "
          "(%d); root-orbit census of the witness: %s"
          % (DEGS.index(d) + 1, d, n_reg_cls, len(creps), len(rows), d,
             cen, d, exp_cent[d], dict(rcen)), ok)

crow = byte2row[c_perm.tobytes()]
ccyc = orbit_census(c_perm)
c_reg = is_regular(crow, 12)
c_cent = centralizer_order(crow)
check("S10.5 HONEST: the v629 clock c = J o sigma is NOT zeta12-regular "
      "(regular: %s), does NOT act freely: orbit census %s = 19 x 12 + "
      "3 x 4 (v629 R2 KILL reproduced), |C_G31(c)| = %d (not 288) -> the "
      "compiler clock is NOT the Springer-regular 12-element of G31"
      % (c_reg, dict(ccyc), c_cent),
      (not c_reg) and ccyc == Counter({12: 19, 4: 3}) and c_cent == 72)

w12 = reg_witness[12][0]
free12 = reg_witness[12][2] == {12: 20}
check("S10.7 the REGULAR order-12 element w acts freely on the 240 roots "
      "with census %s -> '20 = 240/12 free 12-slots' is realized by the "
      "regular 12-clock of G31, NOT by the compiler clock c"
      % reg_witness[12][2], w12 is not None and free12)

max_ord = max(ordG)
check("S10.6 anchor typing for 24: order-24 elements exist (%d of them; "
      "max element order in G31 is %d); 24 = largest degree = largest "
      "REGULAR clock order (S10.4); the equality with |W(A3)| = 24 has NO "
      "subgroup backing (S5/S6) and stays numerology"
      % (ordG.get(24, 0), max_ord), 24 in ordG)

# ==================== S11: TEST 3 -- controls
section("S11: TEST 3 -- wrong-group controls and machinery controls")

st29 = dict(order=4 * 8 * 12 * 20, nrefl=3 + 7 + 11 + 19,
            degs=(4, 8, 12, 20))
st32 = dict(order=12 * 18 * 24 * 30, nrefl=11 + 17 + 23 + 29,
            degs=(12, 18, 24, 30))
k29 = (len(Gset) != st29["order"], n_refl != st29["nrefl"],
       not np.array_equal(molG, degrees_series(st29["degs"], N=28)))
k32 = (len(Gset) != st32["order"], n_refl != st32["nrefl"],
       not np.array_equal(molG, degrees_series(st32["degs"], N=28)))
check("S11.1 ST29 KILLED by order (46080 != %d), reflection count "
      "(60 != %d), Molien mismatch: %s" % (st29["order"], st29["nrefl"],
                                           all(k29)), all(k29))
check("S11.2 ST32 KILLED by order (46080 != %d), reflection count "
      "(60 != %d), Molien mismatch: %s" % (st32["order"], st32["nrefl"],
                                           all(k32)), all(k32))

# positive control 1: W(D5), 5-dim reflection rep -> degrees (2,4,5,6,8)
mats5, ord5 = [], []
for pi5 in itertools.permutations(range(5)):
    P5 = np.zeros((5, 5))
    for i5, j5 in enumerate(pi5):
        P5[j5, i5] = 1.0
    for signs in itertools.product((1.0, -1.0), repeat=5):
        if np.prod(signs) != 1.0:
            continue
        M5 = np.diag(signs) @ P5
        n5, X5 = 1, M5
        while not np.allclose(X5, np.eye(5)):
            X5 = X5 @ M5
            n5 += 1
        mats5.append(M5)
        ord5.append(n5)
cen5, bad5 = eig_census(np.array(mats5, dtype=complex), ord5)
mol5 = molien(cen5, len(mats5), N=16)
check("S11.3 machinery control: Molien of W(D5) (%d signed perms, 5-dim) "
      "= degrees (2,4,5,6,8): %s"
      % (len(mats5), np.array_equal(mol5, degrees_series([2, 4, 5, 6, 8],
                                                         N=16))),
      bad5 == 0 and len(mats5) == 1920
      and np.array_equal(mol5, degrees_series([2, 4, 5, 6, 8], N=16)))

# positive control 2: S4 in its 4-dim permutation rep -> degrees (1,2,3,4)
mats4, ord4 = [], []
for pi4 in itertools.permutations(range(4)):
    P4 = np.zeros((4, 4))
    for i4, j4 in enumerate(pi4):
        P4[j4, i4] = 1.0
    n4, X4 = 1, P4
    while not np.allclose(X4, np.eye(4)):
        X4 = X4 @ P4
        n4 += 1
    mats4.append(P4)
    ord4.append(n4)
cen4, bad4 = eig_census(np.array(mats4, dtype=complex), ord4)
mol4 = molien(cen4, 24, N=10)
check("S11.4 machinery control: Molien of S4 (4-dim perm rep) = degrees "
      "(1,2,3,4): %s"
      % np.array_equal(mol4, degrees_series([1, 2, 3, 4], N=10)),
      bad4 == 0 and np.array_equal(mol4, degrees_series([1, 2, 3, 4],
                                                        N=10)))

# ==================== summary
section("SUMMARY")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
print()
print("VERDICT TEST 1a (subgroup kill): KILL -- G31 is NOT W(D5) x W(A3),")
print("  not as isomorphism (centers 4 vs 1, abelianizations, spectra),")
print("  not as semidirect product (no normal subgroup of order 24 or")
print("  1920: any such lies in N64), and W(D5) does not even EMBED in")
print("  G31 (min faithful dim 5 > 4). W(A3) = S4 does embed.")
print("  Computed structure: G31 = (Z4 o 2^(1+4)) . Sp4(2).")
print("VERDICT TEST 1b (canonical embedding of compiler data): CONFIRMED")
print("  -- J, sigma, c in G31 with sigma = c^4, J = c^9; G31 = full")
print("  unitary stabilizer; root stab = G(4,2,3), line stab = Z4 x")
print("  G(4,2,3); sigma, c NOT in the glue product P.")
print("VERDICT TEST 2 (degree fingerprints): CONFIRMED -- degrees")
print("  (8,12,20,24) unique via Molien; 60 order-2 reflections; Springer")
print("  regular orders 8/12/20/24 with centralizers 192/288/20/24.")
print("  HONEST: the v629 clock c is NOT the regular 12-element (census")
print("  19x12 + 3x4, |C(c)| = 72); the free 20 = 240/12 comb belongs to")
print("  the regular 12-clock of G31 (a different conjugacy class).")
print("VERDICT TEST 3 (controls): PASS -- ST29/ST32 killed by 3 numbers")
print("  each; Molien machinery reproduces W(D5) and S4 exactly.")
print()
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else "SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
