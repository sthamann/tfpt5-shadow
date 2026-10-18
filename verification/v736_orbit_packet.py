#!/usr/bin/env python3
"""v736 -- E8.ORBITPACKET.01: the Gaussian ORBIT PACKET lemma --
Burnside 7, the canonical 5 x 48 packet split, the (0,1,1,2) anchor
weights, the q = 16 normal form, and the P1/P2 reconstruction (typed
as reconstruction, NOT derivation).


BUILDS ON (proven, read-only): v689_gaussian_code_bridge.py /
gaussian_code_bridge_probe.py (26/26, GAUSSIAN-CODE-BRIDGE-EXACT):
L = A(C*) is a rank-4 Z[i]-lattice, L/(1+i)L = F2^4, the 240 roots
fall 15 classes x 16 (zero class EMPTY), classes are mu4-stable and
unions of 4 G31 lines, sigma = c^4 acts on the quotient with 3 fixed
classes + 4 three-cycles.  Also read-only: v634_st31_structure.py
(G31 = full unitary stabilizer, order 46080, J = c^9 central),
v638_code_semantics.py (C* = RM(1,3), anchor pair {6,7}).

THE LEMMA (external review, 5 claims, each checked separately):

 (1) BURNSIDE: N_orbit = (|Fix id| + |Fix s| + |Fix s^2|)/3
     = (15 + 3 + 3)/3 = 7 family orbits on V \\ {0} -- the scalaron
     count 7 as an ORBIT COUNT (and it agrees with the previous
     reading 7 = 4 + 3: four moved orbits + three fixed classes).
 (2) PACKETS: the sigma-fixed block (3 fixed classes x 16 = 48
     roots) plus four moved blocks (one per three-orbit, 3 classes
     x 16 = 48 each)  =>  240 = 5 x 48 CANONICALLY (the partition
     is forced by (L, J, sigma); the only residual freedom is the
     ORDERING of the 4 moved blocks); each block is a union of
     exactly 12 Gaussian lines; g_car = 5 = 1 + 4 moved orbits.
 (3) ANCHOR: the coset-leader weights of the sigma-fixed syndromes
     of C* are (0, 1, 1, 2); the nontrivial part is exactly
     a = (1, 1, 2); elementary symmetric functions e1 = 4, e2 = 5,
     e3 = 2.  (The two weight-1 fixed cosets are led by e_6, e_7 --
     the v638 anchor pair {6,7}.)
 (4) q-NORMAL FORM: |R(E8)| = q(q-1) = 16 * 15 = 240 and
     dim E8 = q(q-1) + 2 log2 q = 240 + 8 = 248 with q = 16.
     Trivial arithmetic, documented with the review framing:
     q = 16 is the order of a CANONICAL quotient (L/(1+i)L), not a
     fitted parameter.
 (5) P1/P2 RECONSTRUCTION: c3 = 1/(2 pi dim V) = 1/(8 pi) with
     dim V = 4 = rank_F2 L/(1+i)L, and g_car = 1 + #moved orbits
     = 5.  TYPE: EXACT-INTERNAL-RECONSTRUCTION -- NOT a derivation.

CIRCULARITY FENCE (prominent, review honesty, applies to claim (5)
and to the whole lemma's status): the code C*, the lattice L, the
complex structure J and the clock sigma are all built FROM E8
(v626/v634/v638/v689).  Reading c3 = 1/(8 pi) and g_car = 5 back out
of the quotient dimensions is an exact internal consistency identity
of the E8 compiler -- it is NOT an independent derivation of the
axioms P1/P2.  A non-circular derivation would have to construct the
code/quotient directly from the boundary datum (seam/horizon data)
WITHOUT E8 input.  Until that exists, the correct type is
RECONSTRUCTION, not DERIVATION.

MUST-FAIL CONTROLS:
  (a) non-equivariant placement (naive v626 code): sigma does not
      preserve L_naive, so the sigma-action on the quotient and on
      the syndrome cosets is UNDEFINED -- the 5-packet structure and
      the anchor weights cannot even be stated (fires); plus an
      honest search whether ANY orientation-preserving pair 3-cycle
      (a relabeled clock commuting with J) preserves the naive code.
  (b) wrong sigma-candidate: classify ALL order-3 elements of the
      FULL unitary stabilizer G31 (46080 elements, BFS from the 60
      reflections) by their quotient orbit census -- is the
      3-fixed + 4-moved structure sigma-specific or automatic for
      every order-3 symmetry?  (Honest documentation either way.)
  (c) abstract free order-3 matrix in GL(4, F2) (companion of
      x^2+x+1, twice): 0 fixed labels, 5 free three-orbits ->
      Burnside (15+0+0)/3 = 5 != 7 and a 0 + 5 packet reading
      (1 + #moved = 6 != 5): order 3 ALONE does not imply the
      packet law (fires).

Exact integer / Fraction arithmetic throughout; numpy only for the
G31 permutation enumeration in control (b) (integer permutation
indices, no floats).  Verdict enums (frozen):
ORBIT-PACKET-EXACT, ORBIT-PACKET-PARTIAL, ORBIT-PACKET-KILLED.

FIREWALL: experiments/ probe; writes nothing; no verification/,
paper, ledger or website surface touched; typed exploration only.

Lean counterpart: experiments/lean4-carrier-rigidity/TfptCarrier/
OrbitPacket.lean (kernel decide, no sorry / native_decide).

PROVENANCE: discovery probe orbit_packet_probe.py (2026-08-04, 26/26,
verdict ORBIT-PACKET-EXACT: Burnside 7 = (15+3+3)/3; canonical 5 x 48
partition -- fixed block + 4 moved blocks of 12 Gaussian lines each,
label-free canonical; anchor (1,1,2) from the fixed-syndrome leader
weights (0,1,1,2) with the leader pair e6/e7 = the v638 anchor pair;
q normal form 240 = 16*15, 248 = 240 + 8; P1/P2 typed as
EXACT-INTERNAL-RECONSTRUCTION behind the circularity fence
(reconstruction, NOT derivation); sigma-CLASS specificity: the 160
free order-3 elements of G31 give Burnside 5, not 7).  Companion Lean
module TfptCarrier/OrbitPacket.lean (34 theorems, kernel-checked).
Promoted verbatim; numbers unchanged.
"""

import itertools
import random
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ---------------------------------------------------------------- codes
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))

PI_J = (1, 0, 3, 2, 5, 4, 7, 6)          # in-pair swap
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)        # new[k] = old[PI_SIG[k]]
PAIRS = ((0, 1), (2, 3), (4, 5), (6, 7))

CSTAR_SUPPORTS_EXPECTED = [
    (0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6), (0, 2, 5, 7),
    (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 4, 6),
    (1, 3, 5, 7), (2, 3, 4, 5), (2, 3, 6, 7), (4, 5, 6, 7)]


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


def supports_w4(code):
    return sorted(tuple(i for i in range(8) if w[i])
                  for w in code if sum(w) == 4)


# ------------------------------------------------------- linear algebra
def mat_det_inv(rows):
    """exact determinant + inverse of a square matrix (Fractions)."""
    n = len(rows)
    A = [[Fr(v) for v in r] for r in rows]
    I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        assert piv is not None, "singular matrix"
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
    """row vector times matrix (exact)."""
    n = len(M)
    return tuple(sum(x[i] * M[i][j] for i in range(n)) for j in range(n))


def row_hnf(rows):
    """row-style Hermite normal form of a full-rank square integer
    matrix (upper triangular, positive diagonal)."""
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


# --------------------------------------------------------- J and sigma
def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def add_vec(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub_vec(x, y):
    return tuple(a - b for a, b in zip(x, y))


# --------------------------------------------------- lattice machinery
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
        assert all(v.denominator == 1 for v in c), "not a lattice vector"
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


def equivalent(lat, x, y):
    """x ~ y mod (1+i)L  <=>  (1-J)(x-y)/2 in L (exact, label-free)."""
    u = sub_vec(x, y)
    w = sub_vec(u, J_vec(u))
    if any(v % 2 for v in w):
        return False
    return lat["in"](tuple(v // 2 for v in w))


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


# ====================================================================== O0
section("O0: preconditions (the proven v689 state, re-established)")

all_placements = set()
for p in itertools.permutations(range(8)):
    all_placements.add(code_image(C_NAIVE, p))
all_placements = sorted(all_placements, key=lambda c: sorted(c))
both_inv = [c for c in all_placements
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
CSTAR = [c for c in both_inv if W0246 in c][0]
ROOTS = constrA_roots(CSTAR)
LAT = constrA_lattice(CSTAR)
REPS = label_group(LAT)
zero_label = LAT["label"]((0,) * 8)
root_label = {r: LAT["label"](r) for r in ROOTS}
census = Counter(root_label.values())
check("O0.1 C* deterministic (v638 recipe), 240 Construction-A roots, "
      "16 quotient classes",
      supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED
      and len(ROOTS) == 240 and len(REPS) == 16)
check("O0.2 v689 census re-established: zero class empty, 15 classes "
      "x 16 roots",
      zero_label not in census and len(census) == 15
      and sorted(census.values()) == [16] * 15)


def sig_label(lb):
    return LAT["label"](sig_vec(REPS[lb]))


sig2_label = {lb: sig_label(sig_label(lb)) for lb in REPS}
fixed_nonzero = [lb for lb in REPS
                 if lb != zero_label and sig_label(lb) == lb]
moved_labels = [lb for lb in REPS
                if lb != zero_label and sig_label(lb) != lb]
orb_census = Counter()
seen = set()
sigma_orbits = []
for lb in REPS:
    if lb == zero_label or lb in seen:
        continue
    orb = frozenset({lb, sig_label(lb), sig2_label[lb]})
    seen |= orb
    orb_census[len(orb)] += 1
    if len(orb) == 3:
        sigma_orbits.append(orb)
check("O0.3 v689 sigma structure re-established: sigma^3 = id on labels, "
      "3 fixed classes + 4 three-cycles",
      all(sig_label(sig2_label[lb]) == lb for lb in REPS)
      and dict(orb_census) == {1: 3, 3: 4}
      and len(fixed_nonzero) == 3 and len(sigma_orbits) == 4)

# ====================================================================== O1
section("O1: claim (1) -- Burnside: N_orbit = (15 + 3 + 3)/3 = 7")

nonzero = [lb for lb in REPS if lb != zero_label]
fix_id = len(nonzero)
fix_s = sum(1 for lb in nonzero if sig_label(lb) == lb)
fix_s2 = sum(1 for lb in nonzero if sig2_label[lb] == lb)
total = fix_id + fix_s + fix_s2
check("O1.1 fixed-point counts on V \\ {0}: |Fix id| = %d, |Fix sigma| "
      "= %d, |Fix sigma^2| = %d; sum %d divisible by |<sigma>| = 3"
      % (fix_id, fix_s, fix_s2, total),
      fix_id == 15 and fix_s == 3 and fix_s2 == 3 and total % 3 == 0)

n_orbit_burnside = total // 3
n_orbit_direct = orb_census[1] + orb_census[3]
check("O1.2 BURNSIDE: N_orbit = %d/3 = %d = direct orbit count %d -- the "
      "scalaron count 7 as an orbit count"
      % (total, n_orbit_burnside, n_orbit_direct),
      n_orbit_burnside == 7 and n_orbit_direct == 7)

check("O1.3 the two readings agree: 7 = 3 fixed + 4 moved (old reading "
      "7 = 4 + 3, same decomposition)",
      orb_census[1] == 3 and orb_census[3] == 4
      and orb_census[1] + orb_census[3] == 7)

# ====================================================================== O2
section("O2: claim (2) -- the canonical packet split 240 = 5 x 48")

label_set_fix = set(fixed_nonzero)
fix_block = [r for r in ROOTS if root_label[r] in label_set_fix]
moved_blocks = [[r for r in ROOTS if root_label[r] in orb]
                for orb in sigma_orbits]
blocks = [fix_block] + moved_blocks
sizes = [len(b) for b in blocks]
all_roots_once = sorted(r for b in blocks for r in b)
check("O2.1 PACKET SIZES: fixed block + 4 moved blocks = %s roots; "
      "pairwise disjoint, union = all 240 roots; 240 = 5 x 48"
      % sizes,
      sizes == [48] * 5 and all_roots_once == sorted(ROOTS)
      and 5 * 48 == 240)

ok_sig_stable = all(
    all(root_label[sig_vec(r)] in ({root_label[r]} if k == 0 else
                                   sigma_orbits[k - 1])
        for r in b)
    for k, b in enumerate(blocks))
# sigma maps each block into itself (fixed block: label fixed;
# moved block: label stays in the same three-orbit)
check("O2.2 each packet is sigma-STABLE (sigma maps every block into "
      "itself: fixed labels stay fixed, moved labels stay in their "
      "three-orbit)", ok_sig_stable)

# 12 Gaussian lines per block
line_of = {}
lines = []
for r in ROOTS:
    if r in line_of:
        continue
    orb = [r]
    y = J_vec(r)
    while y != r:
        orb.append(y)
        y = J_vec(y)
    for x in orb:
        line_of[x] = len(lines)
    lines.append(orb)
lines_per_block = []
ok_lines_inside = True
for b in blocks:
    bset = set(b)
    ids = {line_of[r] for r in b}
    lines_per_block.append(len(ids))
    for i in ids:
        if not all(x in bset for x in lines[i]):
            ok_lines_inside = False
check("O2.3 each packet is a union of EXACTLY 12 of the 60 Gaussian "
      "lines (no line is cut): %s, 60 = 5 x 12"
      % lines_per_block,
      len(lines) == 60 and lines_per_block == [12] * 5
      and ok_lines_inside)

# canonicity: rebuild the partition from the LABEL-FREE equivalence
# relation (1-J)(x-y)/2 in L -- no HNF/basis convention enters
class_members = {}
for r in ROOTS:
    class_members.setdefault(root_label[r], []).append(r)
reps_list = [(lb, mem[0]) for lb, mem in class_members.items()]
ok_within = all(equivalent(LAT, m, mem[0])
                for lb, mem in class_members.items() for m in mem)
ok_between = all(not equivalent(LAT, reps_list[a][1], reps_list[b][1])
                 for a in range(15) for b in range(a + 1, 15))
check("O2.4 CANONICITY (label-free cross-check): the 15 classes agree "
      "with the intrinsic equivalence x ~ y <=> (1-J)(x-y)/2 in L "
      "(240 within-class + 105 between-class tests); the partition "
      "into 1 + 4 packets is forced by (L, J, sigma) -- the only "
      "residual freedom is the ordering of the 4 moved blocks",
      ok_within and ok_between)

g_car_packets = 1 + len(moved_blocks)
check("O2.5 g_car reading: packets = 1 fixed + %d moved = %d = g_car "
      "(P2 value), and 240 = g_car x 48"
      % (len(moved_blocks), g_car_packets),
      g_car_packets == 5 and 5 * 48 == 240)

# ====================================================================== O3
section("O3: claim (3) -- anchor weights (0,1,1,2) from the fixed "
        "syndromes of C*")

CSTAR_LIST = sorted(CSTAR)


def coset_rep(x):
    """canonical coset representative: the minimum of x + C*."""
    return min(tuple((a + b) % 2 for a, b in zip(x, c))
               for c in CSTAR_LIST)


cosets = {}
for x in itertools.product((0, 1), repeat=8):
    cosets.setdefault(coset_rep(x), []).append(x)
leader_weight = {rep: min(sum(m) for m in mem)
                 for rep, mem in cosets.items()}
wdist = Counter(leader_weight.values())
check("O3.1 coset geometry of C*: 16 cosets, leader-weight distribution "
      "%s (covering radius 2; matches HammingCode.lean {0:1, 1:8, 2:7})"
      % dict(sorted(wdist.items())),
      len(cosets) == 16 and dict(wdist) == {0: 1, 1: 8, 2: 7})

ok_sig_on_cosets = code_image(CSTAR, PI_SIG) == CSTAR
fixed_cosets = [rep for rep in cosets
                if coset_rep(apply_perm(rep, PI_SIG)) == rep]
fixed_weights = sorted(leader_weight[rep] for rep in fixed_cosets)
check("O3.2 sigma acts on the cosets (C* is pi_sigma-invariant) with "
      "EXACTLY 4 fixed cosets; their coset-leader weights are %s = "
      "(0, 1, 1, 2)" % (tuple(fixed_weights),),
      ok_sig_on_cosets and len(fixed_cosets) == 4
      and fixed_weights == [0, 1, 1, 2])

w1_leaders = [min((m for m in cosets[rep]), key=sum)
              for rep in fixed_cosets if leader_weight[rep] == 1]
w1_supports = sorted(tuple(i for i in range(8) if l[i]) for l in w1_leaders)
w2_rep = next(rep for rep in fixed_cosets if leader_weight[rep] == 2)
e67 = tuple(1 if i in (6, 7) else 0 for i in range(8))
check("O3.3 the two weight-1 fixed cosets are led by e_6 and e_7 "
      "(supports %s = the v638 anchor pair {6,7}); the weight-2 fixed "
      "coset contains e_6 + e_7" % (w1_supports,),
      w1_supports == [(6,), (7,)] and e67 in cosets[w2_rep])

a_vec = tuple(sorted(leader_weight[rep] for rep in fixed_cosets
                     if leader_weight[rep] > 0))
e1 = sum(a_vec)
e2 = (a_vec[0] * a_vec[1] + a_vec[0] * a_vec[2] + a_vec[1] * a_vec[2])
e3 = a_vec[0] * a_vec[1] * a_vec[2]
check("O3.4 nontrivial anchor weights a = %s = (1,1,2); elementary "
      "symmetric e1 = %d, e2 = %d, e3 = %d -- review reading: "
      "e1 = 4 = |mu4|, e2 = 5 = g_car, e3 = 2 = N(1+i) (exact "
      "arithmetic; the IDENTIFICATION with TFPT constants is the "
      "review's interpretation, not an independent derivation)"
      % (a_vec, e1, e2, e3),
      a_vec == (1, 1, 2) and e1 == 4 and e2 == 5 and e3 == 2)

# honest note: two DIFFERENT F2^4 spaces are in play
check("O3.5 HONEST SCOPE: the syndrome space F2^8/C* (claim 3) and the "
      "Gaussian quotient L/(1+i)L (claims 1-2) are DIFFERENT F2^4's; "
      "both carry sigma with a 2-dim fixed space (4 = %d fixed cosets, "
      "4 = %d fixed labels), but no canonical identification between "
      "them is claimed here"
      % (len(fixed_cosets), 1 + len(fixed_nonzero)),
      len(fixed_cosets) == 4 and 1 + len(fixed_nonzero) == 4)

# ====================================================================== O4
section("O4: claim (4) -- the q-normal form (q = 16, documented)")

q = len(REPS)
check("O4.1 q = |L/(1+i)L| = %d (CANONICAL quotient order, review "
      "framing -- not a fitted parameter): |R(E8)| = q(q-1) = %d = 240; "
      "2^4 = q exactly, so log2 q = 4; dim E8 = q(q-1) + 2 log2 q = %d "
      "= 248 (trivial arithmetic, documented)"
      % (q, q * (q - 1), q * (q - 1) + 2 * 4),
      q == 16 and q * (q - 1) == 240 and 2 ** 4 == q
      and q * (q - 1) + 2 * 4 == 248)

# ====================================================================== O5
section("O5: claim (5) -- P1/P2 reconstruction (TYPED, with fence)")

dimV = 4
ok_dim = 2 ** dimV == len(REPS)
c3_coeff = Fr(1, 2 * dimV)
check("O5.1 P1 reconstruction: dim_F2 V = %d (16 = 2^4 classes), "
      "c3 = 1/(2 pi dim V) = (%s)/pi = 1/(8 pi) -- exact Fraction "
      "identity 1/(2*4) = 1/8" % (dimV, c3_coeff),
      ok_dim and c3_coeff == Fr(1, 8))

check("O5.2 P2 reconstruction: g_car = 1 + #moved orbits = 1 + %d = %d "
      "= 5" % (len(sigma_orbits), 1 + len(sigma_orbits)),
      1 + len(sigma_orbits) == 5)

print("""
    TYPE: EXACT-INTERNAL-RECONSTRUCTION (NOT a derivation).
    +--------------------------------------------------------------+
    | CIRCULARITY FENCE: C*, L, J, sigma are built FROM E8          |
    | (v626/v634/v638/v689).  Reading c3 = 1/(8 pi) and g_car = 5   |
    | back out of the quotient dimensions is an exact internal      |
    | consistency identity of the E8 compiler -- NOT an independent |
    | derivation of P1/P2.  Non-circular status would require       |
    | constructing the code/quotient directly from the boundary     |
    | datum (seam/horizon data) WITHOUT E8 input.                   |
    +--------------------------------------------------------------+
""", flush=True)

# ====================================================================== O6
section("O6: must-fail controls")

# (a) the non-equivariant (naive v626) placement ------------------------
naive_piS = code_image(C_NAIVE, PI_SIG) == C_NAIVE
LATN = constrA_lattice(C_NAIVE)
bad_vec = next((c for c in sorted(C_NAIVE)
                if not LATN["in"](sig_vec(c))), None)
check("O6.1 CONTROL FIRES (non-equivariant placement): pi_sigma-"
      "invariant %s -> the canonical sigma does NOT preserve L_naive "
      "(witness codeword lift %s); the sigma-action on L_naive/(1+i) "
      "and on the naive cosets is UNDEFINED: the 5-packet split, the "
      "Burnside count 7 and the (0,1,1,2) anchor weights cannot even "
      "be STATED for the naive placement"
      % (naive_piS, bad_vec),
      not naive_piS and bad_vec is not None)

# honest relabeled-clock search: orientation-preserving pair 3-cycles
pair3 = []
for qperm in itertools.permutations(range(4)):
    # order-3 permutations of the 4 pairs
    o = 1
    x = list(range(4))
    y = [qperm[i] for i in x]
    while y != x:
        y = [qperm[i] for i in y]
        o += 1
    if o == 3:
        p8 = [0] * 8
        for j in range(4):
            p8[2 * j], p8[2 * j + 1] = 2 * qperm[j], 2 * qperm[j] + 1
        pair3.append(tuple(p8))
n_naive3 = sum(1 for p in pair3 if code_image(C_NAIVE, p) == C_NAIVE)
n_cstar3 = sum(1 for p in pair3 if code_image(CSTAR, p) == CSTAR)
check("O6.2 HONESTY (relabeled clocks): of the 8 orientation-preserving "
      "pair 3-cycles (all commute with J), %d preserve the naive code "
      "and %d preserve C* (C* carries the FULL pair-permutation S4 -- "
      "v634: S4 = W(A3) embeds; all 8 are monomial, hence in sigma's "
      "quotient class): the naive placement admits NO pair-clock at "
      "all -- not even a relabeled one"
      % (n_naive3, n_cstar3),
      n_naive3 == 0 and n_cstar3 == 8)

# (b) wrong sigma-candidate: ALL order-3 elements of G31 ----------------
print("    building G31 on the 240 standard-model roots (BFS from the "
      "60 reflections) ...", flush=True)
N240 = 240
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


def J_np(x):
    out = np.empty_like(x)
    out[0::2] = -x[1::2]
    out[1::2] = x[0::2]
    return out


def perm_from_map(f):
    return np.array([ridx[tuple(int(a) for a in f(RD[i]))]
                     for i in range(N240)], dtype=np.int16)


Jperm = perm_from_map(J_np)
sigperm = perm_from_map(lambda x: x[[4, 5, 0, 1, 2, 3, 6, 7]])
IDP = np.arange(N240, dtype=np.int16)

JRD = np.array([J_np(RD[i]) for i in range(N240)], dtype=np.int64)
line_reps_std = []
line_seen = np.zeros(N240, dtype=bool)
for i in range(N240):
    if line_seen[i]:
        continue
    j = i
    for _ in range(4):
        line_seen[j] = True
        j = int(Jperm[j])
    line_reps_std.append(i)

refl_perms = []
for vi in line_reps_std:
    re4 = RD @ RD[vi]
    im4 = RD @ JRD[vi]
    assert np.all(re4 % 4 == 0) and np.all(im4 % 4 == 0)
    re, im = re4 // 4, im4 // 4
    Y = RD - re[:, None] * RD[vi][None, :] - im[:, None] * JRD[vi][None, :]
    refl_perms.append(np.array([ridx[tuple(int(t) for t in Y[i])]
                                for i in range(N240)], dtype=np.int16))


def bfs_group(gens, cap=46081):
    seen_g = {IDP.tobytes(): IDP}
    frontier = [IDP]
    while frontier:
        nxt = []
        for p in frontier:
            for g in gens:
                qp = p[g]
                b = qp.tobytes()
                if b not in seen_g:
                    seen_g[b] = qp
                    nxt.append(qp)
                    if len(seen_g) > cap:
                        return seen_g, False
        frontier = nxt
    return seen_g, True


t_bfs = time.time()
gens = [Jperm, sigperm] + refl_perms[0:60:12]
Gset, complete = bfs_group(gens)
k_extra = 0
while complete and len(Gset) < 46080 and k_extra < 60:
    extra = next((rp for rp in refl_perms
                  if rp.tobytes() not in Gset), None)
    if extra is None:
        break
    gens = gens + [extra]
    Gset, complete = bfs_group(gens)
    k_extra += 1
check("O6.3a G31 rebuilt: |G31| = %d = 46080 (full unitary stabilizer, "
      "v634; BFS %.1f s, %d generators)"
      % (len(Gset), time.time() - t_bfs, len(gens)),
      complete and len(Gset) == 46080)

# labels in the standard model


def in_E8_std(x):
    par = {v % 2 for v in x}
    return len(par) == 1 and sum(x) % 4 == 0


B_STD = [(4, 0, 0, 0, 0, 0, 0, 0),
         (-2, 2, 0, 0, 0, 0, 0, 0),
         (0, -2, 2, 0, 0, 0, 0, 0),
         (0, 0, -2, 2, 0, 0, 0, 0),
         (0, 0, 0, -2, 2, 0, 0, 0),
         (0, 0, 0, 0, -2, 2, 0, 0),
         (0, 0, 0, 0, 0, -2, 2, 0),
         (1, 1, 1, 1, 1, 1, 1, 1)]
LATS = make_lattice(in_E8_std, list(B_STD))
zeroS = LATS["label"]((0,) * 8)
lab_ids = {}
lab = np.empty(N240, dtype=np.int16)
for i in range(N240):
    l = LATS["label"](tuple(int(a) for a in RD[i]))
    if l not in lab_ids:
        lab_ids[l] = len(lab_ids)
    lab[i] = lab_ids[l]
n_lab = len(lab_ids)
rep_idx = np.array([int(np.nonzero(lab == k)[0][0]) for k in range(n_lab)],
                   dtype=np.int64)
check("O6.3b standard-model labels: %d nonzero classes hit, zero class "
      "empty, 16 roots per class" % n_lab,
      n_lab == 15 and zeroS not in lab_ids
      and all(int(np.sum(lab == k)) == 16 for k in range(n_lab)))

# classify ALL order-3 elements of G31 by their quotient census
t_cls = time.time()
order3 = []
for p in Gset.values():
    p3 = p[p][p]
    if np.array_equal(p3, IDP) and not np.array_equal(p, IDP):
        order3.append(p)
nf_census = Counter()
ok_welldef = True
sig_nf = None
for p in order3:
    f_full = lab[p[rep_idx]]
    if not np.array_equal(lab[p], f_full[lab]):
        ok_welldef = False
        continue
    nf = int(np.sum(f_full == np.arange(n_lab)))
    nf_census[nf] += 1
    if np.array_equal(p, sigperm):
        sig_nf = nf
n3A = nf_census.get(3, 0)
n3B = nf_census.get(0, 0)
check("O6.3c ALL %d order-3 elements of G31 classified (%.1f s): every "
      "one acts WELL-DEFINED on L/(1+i)L (J is central), fixed-label "
      "census %s -- only two classes occur: %d elements with 3 fixed "
      "labels (census {1:3, 3:4}, sigma's class: sigma has %s) and %d "
      "elements with 0 fixed labels (FREE: census {3:5})"
      % (len(order3), time.time() - t_cls, dict(sorted(nf_census.items())),
         n3A, sig_nf, n3B),
      ok_welldef and sig_nf == 3
      and set(nf_census) <= {0, 3} and n3A > 0)

check("O6.4 CONTROL FIRES (wrong sigma-candidate, REALIZED): the free "
      "order-3 class exists inside G31 itself (%d elements): a free "
      "candidate gives 0 fixed + 5 moved orbits, i.e. Burnside "
      "(15+0+0)/3 = 5 != 7 and a packet count 1 + 5 = 6 != 5 = g_car "
      "-- the 3-fixed + 4-moved packet law is SIGMA-CLASS-SPECIFIC "
      "(it needs the 2-dim fixed space of sigma = c^4), NOT an "
      "order-3 tautology" % n3B,
      n3B > 0)

# (c) abstract free order-3 matrix in GL(4, F2) -------------------------
MF = ((0, 1, 0, 0),
      (1, 1, 0, 0),
      (0, 0, 0, 1),
      (0, 0, 1, 1))


def mf_apply(l):
    return tuple(sum(l[i] * MF[i][j] for i in range(4)) % 2
                 for j in range(4))


labels4 = [l for l in itertools.product((0, 1), repeat=4) if any(l)]
mf3_ok = all(mf_apply(mf_apply(mf_apply(l))) == l for l in labels4)
mf_fixed = [l for l in labels4 if mf_apply(l) == l]
seen_f = set()
orbs_f = Counter()
for l in labels4:
    if l in seen_f:
        continue
    orb = {l, mf_apply(l), mf_apply(mf_apply(l))}
    seen_f |= orb
    orbs_f[len(orb)] += 1
check("O6.5 CONTROL FIRES (abstract free class): the companion matrix "
      "of (x^2+x+1)^2 on F2^4 has order 3, %d fixed nonzero labels, "
      "orbit census %s = 5 free three-orbits: Burnside (15+0+0)/3 = 5 "
      "!= 7; order 3 ALONE does not imply the 1 + 4 packet law"
      % (len(mf_fixed), dict(orbs_f)),
      mf3_ok and not mf_fixed and dict(orbs_f) == {3: 5})

# ================================================================ summary
section("SUMMARY")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
core = all(ok for n, ok in CHECKS
           if n.split()[0][:2] in ("O0", "O1", "O2", "O3", "O4", "O5"))
controls = all(ok for n, ok in CHECKS if n.startswith("O6"))
if core and controls:
    print("VERDICT: ORBIT-PACKET-EXACT -- the Gaussian orbit packet")
    print("lemma holds: Burnside 7 = (15+3+3)/3 on L/(1+i)L, the")
    print("canonical split 240 = 5 x 48 (1 sigma-fixed packet + 4 moved")
    print("orbit packets, 12 Gaussian lines each, g_car = 1 + 4 = 5),")
    print("anchor weights (0,1,1,2) with a = (1,1,2) -> e = (4, 5, 2),")
    print("q-normal form 240 = 16*15 and 248 = 240 + 2*4; P1/P2 read")
    print("back EXACTLY as internal reconstruction (see fence).  The")
    print("packet law is sigma-CLASS-specific: G31 contains free")
    print("order-3 elements whose census (5 orbits, Burnside 5) does")
    print("NOT carry the 1 + 4 structure.")
elif controls:
    print("VERDICT: ORBIT-PACKET-PARTIAL -- controls fire but part of")
    print("the lemma failed; see FAIL lines.")
else:
    print("VERDICT: ORBIT-PACKET-KILLED -- a must-fail control did not")
    print("fire; the claimed structure is generic, not sigma-specific.")
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else "SOME CHECKS FAILED")

def run():
    """run_all entry point: the checks execute at import time (module level)."""
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(run())
