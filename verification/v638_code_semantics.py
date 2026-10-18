#!/usr/bin/env python3
"""v638 -- E8.CODESEM.01: the code-semantics stage-2 round -- exploit-or-kill
for the UNIQUE equivariant Hamming placement C* found by
code_semantics_kill_probe.py (stage 1, 13/13: the naive v626 placement is
DEAD for pisig, exactly 2/30 placements carry both compiler symmetries,
exchanged by the anchor transposition (67)).

Background (predecessor, verified 13/13):
  * the 30 S8-placements of the extended Hamming [8,4,4] code contain
    EXACTLY 2 that are invariant under BOTH compiler symmetries mod 2
      piJ   = J_all mod 2 = the mu4 in-pair swap (01)(23)(45)(67),
      pisig = the family pair 3-cycle (positions 0->2->4->0, 1->3->5->1,
              6,7 fixed),
    and the two are exchanged by the anchor-pair transposition (67):
    ONE placement up to the residual anchor orientation.  Call it C*.
  * C* reproduces the v629 root censuses verbatim
    (J {4:60}, sigma {3:76,1:12}, g = J o sigma {12:19,4:3}).

Stage-2 slices (sharpen the dictionary or kill it):
  S1  WHAT ARE THE INFORMATION BITS -- position orbits, information
      sets vs the pair structure, weight-4 orbit decomposition under
      Z6 = <piJ, pisig>, and exact bridges to compiler objects
      (lifted-mark shadow, clock-orbit fibration).
  S2  SYNDROME SEMANTICS -- the geometric single-coordinate error
      class x -> x +- e_i on the 240 Construction-A roots of C*:
      where does it land (exact norm census, distance to the lattice),
      and does the syndrome space factor as
        0 < <q> < F2^4   (q = the universal in-pair syndrome)
      with the quotient F2^3 carrying FOUR pair directions on which
      sigma acts as a 3-cycle + fixed point (anchor = sum of the
      three families)?
  S3  DECODE = PROJECTION -- does hard-decision Construction-A
      syndrome decoding commute mod 2 with the exact nearest-lattice-
      point projection?  (a) all 3840 integer single-coordinate
      errors, (b) 100 random sub-half-integer perturbations,
      (c) 100 random boundary perturbations (honest regime), all in
      exact Fraction arithmetic, seeds fixed.
  S4  KILL CONTROL -- repeat the S1(b) measurement for the NAIVE
      (non-equivariant) v626 placement and census all 30 placements:
      if non-equivariant placements carry the same clean structure,
      the equivariance is irrelevant and the semantics dies.

Verdict enums (frozen): DICTIONARY-SHARP (all pass),
DICTIONARY-PARTIAL, SEMANTICS-KILLED.

FIREWALL: no marker changes; the dictionary is a theorem-level structure
of the equivariant placement (RM(1,3) on AG(3,2)), not a physics
derivation; typed observations only.

PROVENANCE: discovery probes code_semantics_kill_probe.py (stage 1,
2026-08-02, 13/13, verdict CODE-SEMANTICS-RELABELLED) and
code_semantics_stage2_probe.py (2026-08-02, 27/27, verdict
DICTIONARY-SHARP).

Exact arithmetic throughout (int / Fraction); Python-only, counted per
GATE.WOLFRAM.02.
"""

import itertools
import random
import time
from collections import Counter
from fractions import Fraction as Fr
from math import floor

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------- the codes
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))

PI_J = (1, 0, 3, 2, 5, 4, 7, 6)          # in-pair swap
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)        # new[k] = old[PI_SIG[k]]
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7)]


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def compose(p, q):
    """r with apply(w, r) == apply(apply(w, q), p)."""
    return tuple(q[p[k]] for k in range(8))


# Z6 = <piJ, pisig> as a closed set of permutations
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


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


# reconstruct the both-invariant placements exactly as the predecessor
all_placements = set()
for p in itertools.permutations(range(8)):
    all_placements.add(code_image(C_NAIVE, p))
all_placements = sorted(all_placements,
                        key=lambda c: sorted(c))
assert len(all_placements) == 30
both_inv = [c for c in all_placements
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
assert len(both_inv) == 2
# deterministic pick: the placement containing the even transversal
# support {0,2,4,6} (this is 'placement 1' of the predecessor output)
W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
CSTAR = [c for c in both_inv if W0246 in c][0]
COTHER = [c for c in both_inv if c is not CSTAR][0]

CSTAR_SUPPORTS_EXPECTED = [
    (0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6), (0, 2, 5, 7),
    (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 4, 6),
    (1, 3, 5, 7), (2, 3, 4, 5), (2, 3, 6, 7), (4, 5, 6, 7)]


def supports_w4(code):
    return sorted(tuple(i for i in range(8) if w[i])
                  for w in code if sum(w) == 4)


# ---------------------------------------------------------- linear algebra
def code_basis(code):
    """Gaussian elimination -> 4 basis words."""
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


BASIS = code_basis(CSTAR)
assert len(BASIS) == 4


def synd(v):
    """syndrome in F2^4 wrt the self-dual C* (codeword <=> 0)."""
    return tuple(sum(a * b for a, b in zip(bb, v)) % 2 for bb in BASIS)


SYND = {v: synd(v) for v in itertools.product((0, 1), repeat=8)}
LEADERS = {}
for v, s in SYND.items():
    w = sum(v)
    cur = LEADERS.get(s)
    if cur is None or w < cur[0]:
        LEADERS[s] = (w, [v])
    elif w == cur[0]:
        cur[1].append(v)

# ======================================================================= S1
print("=" * 78)
print("S1: what are the information bits")
print("=" * 78)

check("S1.0 C* reconstructed deterministically: 16 words, weight-4 "
      "supports match the predecessor's placement 1 verbatim",
      supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED
      and len(CSTAR) == 16)

# --- S1(a): position orbits ------------------------------------------------
def subset_image(S, p):
    return frozenset(k for k in range(8) if p[k] in S)


def orbits_subsets(subsets, perms):
    seen = set()
    orbs = []
    for s in sorted(subsets, key=sorted):
        if s in seen:
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
        seen.update(orb)
        orbs.append(orb)
    return orbs


singles = [frozenset([i]) for i in range(8)]
orb_pos_J = [sorted(sorted(s)[0] for s in o)
             for o in orbits_subsets(singles, [PI_J])]
orb_pos_S = [sorted(sorted(s)[0] for s in o)
             for o in orbits_subsets(singles, [PI_SIG])]
orb_pos_Z6 = [sorted(sorted(s)[0] for s in o)
              for o in orbits_subsets(singles, Z6)]
check("S1.1 position orbits: piJ -> the 4 mu4 pairs %s; pisig -> "
      "%s (two 3-cycles + fixed pair {6,7}); Z6 -> sizes %s = 6+2 "
      "(three cycled pairs + the fixed ANCHOR pair {6,7})"
      % (sorted(orb_pos_J), sorted(orb_pos_S),
         sorted(len(o) for o in orbits_subsets(singles, Z6))),
      sorted(sorted(o) for o in orb_pos_J) ==
      [[0, 1], [2, 3], [4, 5], [6, 7]]
      and sorted(len(o) for o in orbits_subsets(singles, Z6)) == [2, 6])

# invariant 4-subsets and information sets
four_subsets = [frozenset(s) for s in itertools.combinations(range(8), 4)]
w4_supports = {frozenset(s) for s in supports_w4(CSTAR)}
info_sets = [s for s in four_subsets if s not in w4_supports]
z6_inv_4 = [s for s in four_subsets
            if all(subset_image(s, p) == s for p in Z6)]
pair_unions = [frozenset(PAIRS[a] + PAIRS[b])
               for a in range(4) for b in range(a + 1, 4)]
pu_in_code = [pu for pu in pair_unions if pu in w4_supports]
piJ_inv_info = [s for s in info_sets if subset_image(s, PI_J) == s]
check("S1.2 information sets: %d of 70 four-subsets (complement of a "
      "weight-4 support is a support since 1^8 in C*); Z6-invariant "
      "4-subsets: %d (position orbits 6+2 admit NO invariant 4-set) "
      "=> NO equivariant block-systematic 4+4 split exists"
      % (len(info_sets), len(z6_inv_4)),
      len(info_sets) == 56 and len(z6_inv_4) == 0)
check("S1.3 ALL %d/6 pair-unions are C* codeword supports => even "
      "piJ-invariant information sets: %d => no information set "
      "respects the mu4-pair block structure; in particular the "
      "standard split {0,1,2,3} info / {4,5,6,7} parity is IMPOSSIBLE "
      "(both are codeword supports)"
      % (len(pu_in_code), len(piJ_inv_info)),
      len(pu_in_code) == 6 and len(piJ_inv_info) == 0
      and frozenset({0, 1, 2, 3}) in w4_supports
      and frozenset({4, 5, 6, 7}) in w4_supports)

info_orbs = orbits_subsets(info_sets, Z6)
info_census = Counter(len(o) for o in info_orbs)
min_orb = min(info_orbs, key=len)
check("S1.4 information-set Z6 orbit census: %s (56 = 2 + 9 x 6); the "
      "UNIQUE minimal orbit (size 2) is %s = the transversal info sets "
      "'one bit per mu4 pair, anchor orientation flipped': the "
      "canonical systematic form takes ONE information bit from each "
      "pair (3 family bits + 1 anchor bit), parity = the complementary "
      "transversal"
      % (dict(sorted(info_census.items())),
         sorted(sorted(s) for s in min_orb)),
      dict(info_census) == {2: 1, 6: 9}
      and sorted(sorted(s) for s in min_orb) ==
      [[0, 2, 4, 7], [1, 3, 5, 6]])


# transversal digit helpers: word one-per-pair <-> digits (a,b,c,d)
def transversal_digits(supp):
    dig = []
    for k, (i, j) in enumerate(PAIRS):
        a = int(j in supp)
        if (i in supp) == (j in supp):
            return None
        dig.append(a)
    return tuple(dig)


transversal_words = {w: transversal_digits({i for i in range(8) if w[i]})
                     for w in CSTAR if sum(w) == 4}
transversal_words = {w: d for w, d in transversal_words.items()
                     if d is not None}
check("S1.5 the 8 non-pair-union weight-4 words are exactly the pair "
      "TRANSVERSALS with EVEN digit parity (codeword supports = even "
      "sheet, information sets = odd sheet): digits %s"
      % sorted(transversal_words.values()),
      len(transversal_words) == 8
      and all(sum(d) % 2 == 0 for d in transversal_words.values()))

# --- S1(b): weight-4 orbit decomposition under Z6 --------------------------
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


w4_star = [w for w in CSTAR if sum(w) == 4]
orbs_star = orbits_words(w4_star, Z6)
sizes_star = sorted(len(o) for o in orbs_star)
orb_names = []
for o in orbs_star:
    sup = sorted(tuple(i for i in range(8) if w[i]) for w in o)
    orb_names.append((len(o), sup))
print("    C* weight-4 Z6 orbits:")
for n, sup in sorted(orb_names):
    print("      size %d: %s" % (n, sup))
check("S1.6 the 14 weight-4 words decompose under Z6 as 14 = 2 + 3 + 3 "
      "+ 6: size-2 = the transversal doublet {0000,1111} (even/odd-"
      "diagonal sheet pair), size-3 = the family-family pair-unions, "
      "size-3 = the family-anchor pair-unions, size-6 = the mixed "
      "transversals", sizes_star == [2, 3, 3, 6])

orb2 = [o for o in orbs_star if len(o) == 2][0]
orb3s = [o for o in orbs_star if len(o) == 3]
fam_fam = {frozenset(PAIRS[a] + PAIRS[b])
           for a in range(3) for b in range(a + 1, 3)}
fam_anc = {frozenset(PAIRS[a] + PAIRS[3]) for a in range(3)}
orb3_sets = [{frozenset(i for i in range(8) if w[i]) for w in o}
             for o in orb3s]
check("S1.7 the two size-3 orbits are EXACTLY {family+family} and "
      "{family+anchor} pair-unions (the anchor pair {6,7} grades the "
      "decomposition)",
      (fam_fam in orb3_sets) and (fam_anc in orb3_sets))

# --- S1(c): exact bridges to compiler objects ------------------------------
# roots of the Construction-A model of C*
ROOTS = sorted(x for x in itertools.product(range(-2, 3), repeat=8)
               if sum(v * v for v in x) == 4
               and tuple(v % 2 for v in x) in CSTAR)
assert len(ROOTS) == 240
RSET = set(ROOTS)


def J_all(v):
    out = []
    for i in range(0, 8, 2):
        a, b = v[i], v[i + 1]
        out += [-b, a]
    return tuple(out)


def sigma_r(v):
    return (v[4], v[5], v[0], v[1], v[2], v[3], v[6], v[7])


sig_fixed = [x for x in ROOTS if sigma_r(x) == x]
shadow = Counter(tuple(v % 2 for v in x) for x in sig_fixed)
t_even = next(w for w, d in transversal_words.items() if d == (0, 0, 0, 0))
t_odd = next(w for w, d in transversal_words.items() if d == (1, 1, 1, 1))
zero_fibre = [x for x in sig_fixed
              if tuple(v % 2 for v in x) == (0,) * 8]
check("S1.8 the 12 sigma-fixed roots (the lifted-mark count) reduce "
      "mod 2 to EXACTLY three classes with 4 roots each: {0, t_even, "
      "t_odd} where {t_even, t_odd} IS the size-2 Z6 orbit of S1.6, "
      "and the 0-fibre is {+-2e6, +-2e7} = the ANCHOR pair "
      "(12 = 3 x 4 exactly)",
      len(sig_fixed) == 12
      and shadow == Counter({(0,) * 8: 4, t_even: 4, t_odd: 4})
      and sorted(zero_fibre) == sorted(
          [tuple(2 * (i == j) - 4 * (i == j) * (s == 1) for i in range(8))
           for j in (6, 7) for s in (0, 1)])
      and {t_even, t_odd} == orb2)


def orbit_of(x, f):
    orb = [x]
    y = f(x)
    while y != x:
        orb.append(y)
        y = f(y)
    return orb


# the 60 clock orbits and their mod-2 shadow
seen = set()
J_orbits = []
for x in ROOTS:
    if x in seen:
        continue
    orb = orbit_of(x, J_all)
    seen.update(orb)
    J_orbits.append(frozenset(orb))
assert len(J_orbits) == 60

classes_visited = [frozenset(tuple(v % 2 for v in x) for x in o)
                   for o in J_orbits]
fibre = Counter()
for cl in classes_visited:
    fibre[cl] += 1
piJ_class_orbits = {frozenset({c, apply_perm(c, PI_J)}) for c in CSTAR
                    if sum(c) in (0, 4)}
check("S1.9 clock-orbit fibration: each clock orbit projects onto one "
      "piJ-class-orbit of codewords; the 11 bases (1 zero + 6 pair-"
      "unions + 4 transversal doublets) carry %s clock orbits "
      "(60 = 7 x 4 + 4 x 8); D_start = 60 counts 4 clock orbits per "
      "piJ-fixed class and 8 per transversal doublet"
      % sorted(fibre.values()),
      set(fibre.keys()) == piJ_class_orbits
      and sorted(fibre.values()) == [4] * 7 + [8] * 4)

# sigma action on the 60 clock orbits
orb_index = {}
for k, o in enumerate(J_orbits):
    for x in o:
        orb_index[x] = k
sig_on_orbits = {}
for k, o in enumerate(J_orbits):
    sig_on_orbits[k] = orb_index[sigma_r(next(iter(o)))]
seen = set()
cens60 = Counter()
fixed_orbit_classes = []
for k in range(60):
    if k in seen:
        continue
    cyc = [k]
    j = sig_on_orbits[k]
    while j != k:
        cyc.append(j)
        j = sig_on_orbits[j]
    seen.update(cyc)
    cens60[len(cyc)] += 1
    if len(cyc) == 1:
        fixed_orbit_classes.append(classes_visited[k])
check("S1.10 sigma on the 60 clock orbits: census %s = 3 fixed + 19 "
      "free 3-cycles (reproducing the v629 g-census 19 x 12 + 3 x 4 "
      "as the quotient tower 240 -> 60 -> 3+19); the 3 fixed clock "
      "orbits project exactly onto {0} and the size-2 codeword orbit"
      % dict(sorted(cens60.items())),
      dict(cens60) == {1: 3, 3: 19}
      and sorted(map(sorted, fixed_orbit_classes)) ==
      sorted(map(sorted, [frozenset({(0,) * 8}),
                          frozenset({t_even, t_odd}),
                          frozenset({t_even, t_odd})])))

# the WHY: C* = RM(1,3) and the symmetries are affine maps of AG(3,2)
def bits(j):
    return ((j >> 2) & 1, (j >> 1) & 1, j & 1)


RM13 = set()
for a, c2, c1, c0 in itertools.product((0, 1), repeat=4):
    RM13.add(tuple((a + c2 * bits(j)[0] + c1 * bits(j)[1]
                    + c0 * bits(j)[2]) % 2 for j in range(8)))


def posmap(p):
    return tuple(p.index(i) for i in range(8))


def is_affine(m):
    """m affine on AG(3,2) <=> T(u) = bits(m[u]) xor bits(m[0]) linear."""
    b = bits(m[0])

    def T(u):
        return tuple(x ^ y for x, y in zip(bits(m[u]), b))

    for u in range(8):
        for v in range(8):
            uv = ((bits(u)[0] ^ bits(v)[0]) << 2 |
                  (bits(u)[1] ^ bits(v)[1]) << 1 |
                  (bits(u)[2] ^ bits(v)[2]))
            if T(uv) != tuple(x ^ y for x, y in zip(T(u), T(v))):
                return False
    return True


mJ = posmap(PI_J)
mS = posmap(PI_SIG)
planes_ok = all(
    all((u ^ v ^ w) in {a for a in s}
        for u, v, w in itertools.combinations(s, 3))
    for s in ({i for i in sup} for sup in supports_w4(CSTAR)))
check("S1.11 [the WHY, observation] under the binary position labels "
      "j = (b2,b1,b0), C* IS the Reed-Muller code RM(1,3): %s; piJ = "
      "translation by 001: %s; pisig is an AFFINE map of AG(3,2): %s; "
      "the 14 weight-4 supports are the 14 planes of AG(3,2): %s "
      "-- the equivariant placement exists because Aut = AGL(3,2) "
      "contains the Z6, and 30 = |S8|/|AGL(3,2)|"
      % (frozenset(RM13) == CSTAR,
         mJ == tuple(j ^ 1 for j in range(8)),
         is_affine(mS), planes_ok),
      frozenset(RM13) == CSTAR and mJ == tuple(j ^ 1 for j in range(8))
      and is_affine(mS) and planes_ok)

movers67 = code_image(CSTAR, (0, 1, 2, 3, 4, 5, 7, 6)) == COTHER
check("S1.12 [observation] the residual ambiguity of the equivariant "
      "placement is EXACTLY the anchor-pair orientation: the (67) "
      "swap maps C* to the second placement: %s" % movers67, movers67)

# ======================================================================= S2
print("=" * 78)
print("S2: syndrome semantics")
print("=" * 78)

# --- S2(a): the geometric error class --------------------------------------
norm_census = Counter()
for x in ROOTS:
    for i in range(8):
        for e in (1, -1):
            norm_census[4 + 2 * e * x[i] + 1] += 1
check("S2.1 single-coordinate errors x -> x +- e_i on the 240 roots: "
      "exact norm census over all 3840 perturbations %s -- every "
      "perturbed vector has ODD norm, hence lies OFF the (doubly-even) "
      "lattice and OFF every shell"
      % dict(sorted(norm_census.items())),
      dict(norm_census) == {1: 16, 3: 896, 5: 2016, 7: 896, 9: 16}
      and all(n % 2 == 1 for n in norm_census))


def nearest_lattice(y):
    """exact nearest points of the Construction-A lattice of C*.

    Complete by construction: min over the 16 cosets c + 2Z^8, each
    minimized coordinatewise (parity-constrained nearest integers).
    Returns (min squared distance, set of nearest lattice points)."""
    best = None
    packs = []
    for c in CSTAR:
        tot = 0
        opts = []
        for yi, ci in zip(y, c):
            f = floor(yi)
            cands = [k for k in range(f - 2, f + 3) if k % 2 == ci]
            d2 = [(yi - k) ** 2 for k in cands]
            m = min(d2)
            tot += m
            opts.append([k for k, d in zip(cands, d2) if d == m])
        if best is None or tot < best:
            best = tot
            packs = [opts]
        elif tot == best:
            packs.append(opts)
    pts = set()
    for opts in packs:
        pts.update(itertools.product(*opts))
    return best, pts


geo_ok = True
tie_pair_ok = True
class_ok = True
for x in ROOTS:
    c = tuple(v % 2 for v in x)
    for i in range(8):
        for e in (1, -1):
            y = list(x)
            y[i] += e
            y = tuple(y)
            d2, pts = nearest_lattice(y)
            if d2 != 1:
                geo_ok = False
            exp = {x, tuple(v + (2 * e if k == i else 0)
                            for k, v in enumerate(x))}
            if pts != exp:
                tie_pair_ok = False
            if {tuple(v % 2 for v in p) for p in pts} != {c}:
                class_ok = False
check("S2.2 every perturbed vector lies at squared distance EXACTLY 1 "
      "from the lattice (the packing radius) with EXACTLY the tie pair "
      "{x, x +- 2e_i} as nearest points (3840/3840): %s, %s"
      % (geo_ok, tie_pair_ok), geo_ok and tie_pair_ok)
check("S2.3 the geometric 2-fold tie COLLAPSES mod 2: both nearest "
      "points reduce to the original codeword c in every one of the "
      "3840 cases -- mod-2 projection is unambiguous on the whole "
      "single-coordinate error class", class_ok)

# --- S2(b): the syndrome factorization -------------------------------------
s_coord = [SYND[tuple(1 if k == i else 0 for k in range(8))]
           for i in range(8)]
q_list = [tuple((a + b) % 2 for a, b in zip(s_coord[2 * k],
                                            s_coord[2 * k + 1]))
          for k in range(4)]
q = q_list[0]
check("S2.4 the 8 coordinate syndromes are distinct and nonzero "
      "(the code corrects the exact COORDINATE), and the in-pair "
      "syndrome q = s(e_2k)+s(e_2k+1) is UNIVERSAL: all four pairs "
      "give the same q = %s != 0 (this needs all pair-unions in the "
      "code -- exactly the S1.3 fact)"
      % (q,),
      len(set(s_coord)) == 8 and all(s != (0,) * 4 for s in s_coord)
      and len(set(q_list)) == 1 and q != (0,) * 4)

piv = next(i for i, b in enumerate(q) if b)


def qred(s):
    """linear projection F2^4 -> F2^4/<q> (canonical rep)."""
    if s[piv]:
        return tuple((a + b) % 2 for a, b in zip(s, q))
    return s


P = [qred(s_coord[2 * k]) for k in range(4)]
span = {(0,) * 4}
for v in P:
    span |= {tuple((a + b) % 2 for a, b in zip(v, u)) for u in span}
check("S2.5 the four PAIR DIRECTIONS P_k = [s(e_2k)] mod <q>: distinct "
      "and nonzero %s, P0+P1+P2+P3 = 0 (the all-ones word is a "
      "codeword), and P0,P1,P2 span the full quotient F2^3: the "
      "syndrome space factors as the flag 0 < <q> < F2^4 with "
      "quotient = the PAIR POINTER (in-pair bit q localizes the "
      "element WITHIN the pair)"
      % (len(set(P)) == 4,),
      len(set(P)) == 4 and all(p != (0,) * 4 for p in P)
      and qred(tuple(sum(x) % 2 for x in zip(*P))) == (0,) * 4
      and len(span) == 8
      and all(qred(s_coord[i]) == P[i // 2] for i in range(8)))

# induced actions on the syndrome space: well-defined + the sharp test
def induced_action(perm):
    m = {}
    for v in itertools.product((0, 1), repeat=8):
        s = SYND[v]
        t = SYND[apply_perm(v, perm)]
        if s in m and m[s] != t:
            return None
        m[s] = t
    return m


A_sig = induced_action(PI_SIG)
A_J = induced_action(PI_J)
sig_on_P = [P.index(qred(A_sig[s_coord[2 * k]])) for k in range(4)]
check("S2.6 THE SHARP TEST: sigma is well-defined on syndromes "
      "(placement equivariance), fixes <q>, and acts on the four pair "
      "directions as the 3-CYCLE + FIXED POINT %s (P0->P1->P2->P0, "
      "ANCHOR P3 fixed) with P3 = P0+P1+P2: the 4 pairs = 3 families "
      "cycled + 1 fixed anchor -- the (1,1,2)-type anchor structure "
      "on the syndrome quotient, exactly"
      % (sig_on_P,),
      A_sig is not None and A_sig[q] == q
      and sig_on_P == [1, 2, 0, 3]
      and qred(tuple((a + b + c) % 2 for a, b, c
                     in zip(P[0], P[1], P[2]))) == P[3])
check("S2.7 piJ is well-defined on syndromes, fixes q, and acts "
      "TRIVIALLY on the quotient F2^3 (swapping only the in-pair bit): "
      "the pair pointer is exactly the piJ-invariant content of the "
      "syndrome -- the syndrome localizes the mu4 PAIR canonically, "
      "the coordinate only after choosing a pair orientation",
      A_J is not None and A_J[q] == q
      and all(qred(A_J[s]) == qred(s) for s in set(SYND.values())))

# ======================================================================= S3
print("=" * 78)
print("S3: decode = projection (exact, Fraction arithmetic)")
print("=" * 78)


def nearest_int(y):
    f = floor(y)
    r = y - f
    assert r != Fr(1, 2), "half-integer rounding tie -- excluded by design"
    return f if r < Fr(1, 2) else f + 1


def decode_A(y):
    """hard-decision Construction-A syndrome decoder.

    Round to Z^8, syndrome-decode mod 2 (all minimum-weight coset
    leaders), realize each flip toward y, keep the exact-nearest
    candidates.  Returns (set of decoded lattice points, leader wt)."""
    z = tuple(nearest_int(v) for v in y)
    s = SYND[tuple(v % 2 for v in z)]
    if s == (0,) * 4:
        return {z}, 0
    wt, leaders = LEADERS[s]
    cands = set()
    for e in leaders:
        opts = []
        for j in range(8):
            if e[j]:
                two = [z[j] - 1, z[j] + 1]
                d2 = [(y[j] - t) ** 2 for t in two]
                m = min(d2)
                opts.append([t for t, d in zip(two, d2) if d == m])
            else:
                opts.append([z[j]])
        cands.update(itertools.product(*opts))
    scored = sorted((sum((a - b) ** 2 for a, b in zip(y, w)), w)
                    for w in cands)
    m = scored[0][0]
    return {w for d, w in scored if d == m}, wt


def mods(pts):
    return {tuple(v % 2 for v in p) for p in pts}


# --- S3.1: the full integer error class ------------------------------------
ok31 = True
for x in ROOTS:
    for i in range(8):
        for e in (1, -1):
            y = tuple(Fr(v + (e if k == i else 0))
                      for k, v in enumerate(x))
            dec, wt = decode_A(y)
            d2, near = nearest_lattice(y)
            if not (wt == 1 and dec == near and len(mods(dec)) == 1
                    and mods(dec) == mods(near)):
                ok31 = False
check("S3.1 all 3840 integer single-coordinate errors: the syndrome "
      "decoder (unique weight-1 leader) returns EXACTLY the geometric "
      "nearest-point tie pair {x, x+-2e_i}, and both agree mod 2 -- "
      "decode = projection holds VERBATIM (3840/3840) on the "
      "geometric error class", ok31)

# --- S3.2: 100 random sub-half perturbations (provably safe regime) --------
rng = random.Random(20260802)
ok32 = 0
for _ in range(100):
    x = ROOTS[rng.randrange(240)]
    d = tuple(Fr(rng.randint(-7, 7), 16) for _ in range(8))
    y = tuple(Fr(v) + dv for v, dv in zip(x, d))
    dec, wt = decode_A(y)
    d2, near = nearest_lattice(y)
    if dec == near == {x}:
        ok32 += 1
check("S3.2 100 random perturbations with |delta_i| <= 7/16 < 1/2 "
      "(seed 20260802): decoder and exact projection BOTH return "
      "exactly x in %d/100 cases (provable: |delta|_inf < 1/2 keeps "
      "x the unique nearest point and rounding exact)" % ok32,
      ok32 == 100)

# --- S3.3: 100 boundary perturbations (honest regime) ----------------------
rng = random.Random(20260629)
ks = [k for k in range(-9, 10) if abs(k) != 8]
stats = Counter()
mismatch_detail = []
for t in range(100):
    x = ROOTS[rng.randrange(240)]
    d = tuple(Fr(rng.choice(ks), 16) for _ in range(8))
    y = tuple(Fr(v) + dv for v, dv in zip(x, d))
    z = tuple(nearest_int(v) for v in y)
    nerr = sum(1 for zi, xi in zip(z, x) if zi != xi)
    dec, wt = decode_A(y)
    d2, near = nearest_lattice(y)
    dm, nm = mods(dec), mods(near)
    if dm == nm and len(nm) == 1:
        cat = "commute"
    elif dm == nm:
        cat = "commute-multiclass-tie"
    else:
        cat = "MISMATCH"
        mismatch_detail.append((t, nerr, wt, sorted(dm), sorted(nm)))
    stats[(min(nerr, 3), cat)] += 1

by_err = {}
for (nerr, cat), n in stats.items():
    by_err.setdefault(nerr, Counter())[cat] += n
print("    boundary regime |delta_i| <= 9/16 (seed 20260629), by number")
print("    of rounding errors (3 = '>=3'):")
tot_commute = 0
tot = 0
low_err_clean = True
mismatch_low = 0
for nerr in sorted(by_err):
    row = by_err[nerr]
    n_all = sum(row.values())
    n_com = row.get("commute", 0) + row.get("commute-multiclass-tie", 0)
    tot += n_all
    tot_commute += n_com
    if nerr <= 1 and n_com != n_all:
        low_err_clean = False
        mismatch_low += n_all - n_com
    print("      %d rounding errors: %2d samples, %2d commute, %2d "
          "mismatch" % (nerr, n_all, n_com, n_all - n_com))
for t, nerr, wt, dm, nm in mismatch_detail:
    print("      mismatch sample %2d: %d rounding errors, leader "
          "weight %d, decode class %s vs nearest class %s"
          % (t, nerr, wt, dm, nm))
check("S3.3 boundary regime, honest: %d/100 commute mod 2 overall; "
      "CONDITIONAL on <= 1 rounding error the commutation is %s "
      "(every mismatch has >= 2 rounding errors: %s) -- exactly the "
      "d = 4 correction radius: decode = projection ON the "
      "single-error class, and it degrades beyond it as any [8,4,4] "
      "decoder must"
      % (tot_commute, "100%" if low_err_clean else "BROKEN",
         all(m[1] >= 2 for m in mismatch_detail)),
      low_err_clean and all(m[1] >= 2 for m in mismatch_detail))

# ======================================================================= S4
print("=" * 78)
print("S4: kill control -- the naive placement and the 30-census")
print("=" * 78)

w4_all = [w for w in itertools.product((0, 1), repeat=8) if sum(w) == 4]
orbs70 = orbits_words(w4_all, Z6)
check("S4.1 Z6 orbit structure of ALL 70 weight-4 words: census %s "
      "(2 transversal doublets, 2 pair-union triples, 10 sextets)"
      % dict(sorted(Counter(len(o) for o in orbs70).items())),
      dict(Counter(len(o) for o in orbs70)) == {2: 2, 3: 2, 6: 10})


def placement_stats(code):
    w4 = {w for w in code if sum(w) == 4}
    invJ = code_image(code, PI_J) == code
    invS = code_image(code, PI_SIG) == code
    npu = sum(1 for pu in pair_unions
              if tuple(1 if i in pu else 0 for i in range(8)) in code)
    b = code_basis(code)

    def sy(v):
        return tuple(sum(a * c for a, c in zip(bb, v)) % 2 for bb in b)

    qs = {sy(tuple(1 if i in PAIRS[k] else 0 for i in range(8)))
          for k in range(4)}
    quniv = (len(qs) == 1 and (0,) * 4 not in qs)
    frag = sum(1 for o in orbs70 if 0 < len(o & w4) < len(o))
    own = [p for p in (PI_J, PI_SIG) if code_image(code, p) == code]
    sizes = sorted(len(o) for o in orbits_words(w4, own + [tuple(range(8))]))
    return invJ, invS, npu, quniv, frag, sizes


stats30 = [placement_stats(c) for c in all_placements]
naive_stats = placement_stats(C_NAIVE)
star_stats = placement_stats(CSTAR)
print("    naive v626 placement: invJ=%s invS=%s pair-unions=%d/6 "
      "q-universal=%s fragmented-orbits=%d own-group w4 sizes %s"
      % naive_stats)
print("    C* placement:         invJ=%s invS=%s pair-unions=%d/6 "
      "q-universal=%s fragmented-orbits=%d Z6 w4 sizes %s"
      % star_stats)
frag_profile = Counter()
for o in orbs70:
    w4n = {w for w in C_NAIVE if sum(w) == 4}
    k = len(o & w4n)
    if k:
        frag_profile[(len(o), k)] += 1
check("S4.2 S1(b) repeated on the NAIVE placement: the 14 words "
      "fragment across Z6 orbits with intersection profile "
      "{(orbit size, words inside): count} = %s -- only the "
      "transversal doublet survives intact; %d of the meeting orbits "
      "are PROPERLY fragmented (C*: 0 fragmented, 4 full orbits): "
      "the orbit structure measurably degrades without equivariance"
      % (dict(sorted(frag_profile.items())), naive_stats[4]),
      naive_stats[4] > 0 and star_stats[4] == 0
      and naive_stats[5] == [1, 1, 2, 2, 2, 2, 2, 2]
      and star_stats[5] == [2, 3, 3, 6])
check("S4.3 the naive placement has only %d/6 pair-unions, so the "
      "in-pair syndrome is NOT universal (%s): the S2 flag "
      "0 < <q> < F2^4 (pair localization + anchor 3-cycle) DOES NOT "
      "EXIST for the naive placement -- the stage-2 dictionary is "
      "strictly a property of the equivariant placement"
      % (naive_stats[2], naive_stats[3]),
      naive_stats[2] == 2 and naive_stats[3] is False)

n_quniv = sum(1 for s in stats30 if s[3])
n_frag0 = sum(1 for s in stats30 if s[4] == 0)
n_both = sum(1 for s in stats30 if s[0] and s[1])
check("S4.4 the 30-census: %d/30 placements carry the universal "
      "in-pair syndrome (= contain all 6 pair-unions), %d/30 have "
      "zero fragmented Z6 orbits, %d/30 are both-invariant -- and "
      "these three sets COINCIDE (the two C* relabellings): "
      "equivariance <=> pair-syndrome flag <=> clean orbit structure; "
      "the kill control FIRES, the equivariance is load-bearing"
      % (n_quniv, n_frag0, n_both),
      n_quniv == 2 and n_frag0 == 2 and n_both == 2
      and all((s[3] and s[4] == 0) == (s[0] and s[1]) for s in stats30))

# ================================================================== summary
print("=" * 78)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
s1 = all(ok for n, ok in CHECKS if n.startswith("S1"))
s2 = all(ok for n, ok in CHECKS if n.startswith("S2"))
s3 = all(ok for n, ok in CHECKS if n.startswith("S3"))
s4 = all(ok for n, ok in CHECKS if n.startswith("S4"))
print("slice verdicts: S1 %s | S2 %s | S3 %s | S4 %s"
      % tuple("PASS" if s else "FAIL" for s in (s1, s2, s3, s4)))
if s1 and s2 and s3 and s4:
    print("VERDICT: DICTIONARY-SHARP -- the equivariant placement carries")
    print("an exact dictionary: positions = AG(3,2) points, pairs = the")
    print("mu4 digits (3 families cycled + 1 anchor fixed), information")
    print("bits = one per pair (transversal, anchor-flipped), syndrome =")
    print("(in-pair bit) + (pair pointer with anchor = sum of families),")
    print("decode = projection verbatim on the single-error class, and")
    print("all of it dies for every non-equivariant placement.")
elif s4:
    print("VERDICT: DICTIONARY-PARTIAL -- equivariance load-bearing but")
    print("part of the stage-2 dictionary failed; see FAIL lines.")
else:
    print("VERDICT: SEMANTICS-KILLED -- the kill control did not fire;")
    print("equivariance is irrelevant to the observed structure.")
print("elapsed: %.1f s" % (time.time() - T0))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
