#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gaussian_shell_global_probe -- E8.GAUSSIAN.SHELL.GLOBAL.01 (phase 1
of the 2026-08-08 evening plan): the GLOBAL GAUSSIAN SHELL THEOREM --
the finite census (v833/v844/v857: equidistribution measured to level
16, the -1/15 value theorem measured to 16500) is upgraded to ALL
shells by three verified structural inputs: (i) the deployed
G31 -> Sp(4,2) class action is by symplectic TRANSVECTIONS and is
transitive on the 15 nonzero classes of V = L/(1+i)L, and it is the
SAME class action used in the shell modules; (ii) multiplication by
(1+i) doubles the norm (J antisymmetry), so Theta_0(2m) = Theta_L(m)
and Theta_0(odd) = 0; (iii) Theta_L(n) = 240 sigma_3(n) (classical E8
theta = 240 E4-coefficients; CITED + verified on the computed range).
Consequence, for ALL n: Theta_v(n) = (Theta_L(n) - Theta_0(n))/15 for
every v != 0 and Thetahat_u(n) = (16 Theta_0(n) - Theta_L(n))/15 =
16 (16 1_{2|n} sigma_3(n/2) - sigma_3(n)); for ODD n: Thetahat_u(n) =
-16 sigma_3(n) and Thetahat_u/Theta_L = -1/15 EXACTLY -- a theorem for
all odd n, replacing the n <= 16500 census.

FROZEN CLAIMS (2026-08-08 evening, frozen + SHA-hashed before first run):

 S1  STRUCTURAL INPUT (i) -- THE ACTION (exact integer arithmetic):
     S1.1 rebuild: 240 doubled std-model E8 roots (norm 8); the J
     matrix satisfies J^T = -J, J^2 = -I, (I-J)(I+J) = 2I and
     det(I+J) = 16 = |L/(1+i)L| EXACTLY.
     S1.2 THE LATTICE IS THE ROOT SPAN: the HNF of the 240 roots has
     |det| = 256; the mod-4 membership residues of L number 256, so
     [L : 4Z^8] = 256 and det(L) = 4^8/256 = 256; every root passes
     the membership test => root span = L EXACTLY; and 4 e_k in
     (1+i)L for all 8 unit directions => classes are mod-4 data (the
     DP ground).
     S1.3 THE CLASSES, TWO LABELINGS (the coordination check, part 1):
     the shell-module labeling (mod-4 residue reps, DP path) and the
     G31-module labeling (greedy on the roots, v858 path) give the
     SAME partition of the 240 roots: 15 nonzero classes x 16, zero
     class EMPTY.
     S1.4 THE SYMPLECTIC FORM: b(x,y) = ((x.y)/4 + (x.Jy)/4) mod 2 is
     well-defined on V x V (class-constant over all 240 roots vs all
     16 reps), F2-bilinear (all 16^3 additivity triples), alternating
     (b(x,x) = 0, forced by |x|^2 in 8Z), symmetric, and NONDEGENERATE
     (rank 4 over F2).
     S1.5 THE 60 GENERATORS ARE SYMPLECTIC TRANSVECTIONS (the
     coordination check, part 2): each v858 reflection R_v satisfies
     (4M)^T (4M) = 16 I (isometry) and (4M) J = J (4M) (complex-
     linear), permutes the 240 roots (hence preserves L = root span),
     and its induced class map IS the symplectic transvection
     T_{vbar}: x -> x + b(x, vbar) vbar for vbar = class(v) -- and the
     two action paths (root-permutation transport vs matrix-on-reps
     transport) COINCIDE on every generator.
     S1.6 TRANSITIVITY: the closure of the 60 induced transvections
     has order 720 = |Sp(4,2)|, every generator preserves b, the
     action on the 15 nonzero classes is TRANSITIVE (one orbit of
     size 15), and the 60 root lines cover all 15 classes at 4 lines
     per class (v858 S2.3 reproduced).
 S2  STRUCTURAL INPUT (ii) -- NORM DOUBLING (exact):
     S2.1 (I+J)^T (I+J) = 2I EXACTLY (x.Jx = 0 from antisymmetry), so
     |(1+i)x|^2 = 2|x|^2 for EVERY x; the deployed membership test is
     the inverse bijection ((1-J)/2)(1+i) = I from (I-J)(I+J) = 2I;
     level-2 witness: the 240 vectors (1+i)r (r a root) are distinct,
     norm 16, ALL in the zero class.
     S2.2 RAMIFICATION on the DP range: Theta_0(n) = 0 for EVERY odd
     n <= 24 (one-line proof: x = (1+i)y => |x|^2 = 2|y|^2 with
     |y|^2 in 8Z => level even) and Theta_0(2m) = 240 sigma_3(m) =
     Theta_L(m) for every 2m <= 24 (the doubling bijection), with
     Theta_0(2) = 240 matching the witness.
 S3  STRUCTURAL INPUT (iii) -- THE THETA IDENTITY (exact int DP over
     the 256 mod-4 residues, levels |x|^2 = 8n, n <= NCAP = 24):
     S3.1 DP gates: residue fibers all 256; level-1 class census
     equals the root census (0; 16 x15).
     S3.2 Theta_L(n) = sum_v Theta_v(n) = 240 sigma_3(n) for EVERY
     n <= 24 against an independent sigma_3 sieve (the classical E8
     theta formula, CITED as Eisenstein E4 and verified here on the
     computed range).
 S4  THE DERIVED GLOBAL FORMULAS + THE WARD:
     S4.1 Theta_v(n) = (Theta_L(n) - Theta_0(n))/15 EXACTLY for every
     v != 0 and every n <= 24 (equidistribution is now a COROLLARY:
     the shell counting function is invariant under the induced
     Sp-action -- each generator is a norm-preserving lattice
     bijection transporting class v to gbar(v) -- and the action is
     transitive on the 15 nonzero classes; 15-divisibility exact).
     S4.2 Thetahat_u(n) = (16 Theta_0(n) - Theta_L(n))/15 =
     16 (16 1_{2|n} sigma_3(n/2) - sigma_3(n)) EXACTLY for every
     u != 0 and every n <= 24.
     S4.3 THE GLOBAL WARD to 16500 (v817/v857 packet machinery rebuilt
     read-only, int64 with the deployed exactness certificates):
     heads (Th0..Th3)(1) = (52,64,60,64); glue identity
     Th0+Th1+Th2+Th3 = 240 sigma_3(n) for ALL n <= 16500; Th1 = Th3;
     the packet numerator (Th0-Th1+Th2-Th3)(n) EQUALS the derived
     closed form 16 (16 1_{2|n} sigma_3(n/2) - sigma_3(n)) for EVERY
     n <= 16500 (odd AND even -- the deployed census range matches
     the theorem everywhere), and equals the DP Thetahat_u(n) on
     n <= 24; hence for ODD n: Thetahat_u(n) = -16 sigma_3(n) and
     Thetahat_u/Theta_L = -1/15 EXACTLY -- now a THEOREM for ALL odd
     n, the n <= 16500 census replaced by proof.
 C   CONTROLS (each must fire; exact):
     C1 A WRONG ACTION BREAKS EQUIDISTRIBUTION: the non-transitive
        subgroup H = <T_1> (one transvection) has 11 orbits on the 15
        nonzero classes (7 fixed + 4 swaps); an explicit H-invariant
        NON-uniform census (move 16 roots between two H-fixed
        classes: values 32 and 0) is constructed -- its Walsh values
        on u != 0 are the multiset {-48: 4, -16: 7, +16: 4}, NOT
        uniform, and the -1/15 law breaks; a full-group generator
        moves that census (measured) -- transitivity is the
        load-bearing input, H-invariance alone does not force
        uniformity.
     C2 THE EVEN-SHELL FORMULA DIFFERS CORRECTLY: Thetahat_u(2m) =
        16 (16 sigma_3(m) - sigma_3(2m)) (verified in BOTH
        machineries via S4.2/S4.3); at n = 2: Thetahat = 112,
        Theta_L = 2160, ratio 112/2160 = 7/135 != -1/15 (typed:
        the -1/15 law is the ODD-shell statement only).

KILLS (any one fires => typed failure):
  K1 rebuild / lattice / J identities break     -> LATTICE-BROKEN
  K2 action / coordination / transitivity break -> ACTION-MISMATCH
  K3 doubling / ramification breaks             -> DOUBLING-BROKEN
  K4 DP gates / theta identity break            -> THETA-MISMATCH
  K5 a derived global formula / ward breaks     -> FORMULA-BROKEN
  K6 a control does not fire                    -> CONTROL-DEAD

VERDICT (frozen enum): SHELL-GLOBAL-THEOREM / LATTICE-BROKEN /
ACTION-MISMATCH / DOUBLING-BROKEN / THETA-MISMATCH / FORMULA-BROKEN /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact integer/Fraction arithmetic in every
decision (numpy int64 packet layer uses the deployed divisibility
certificates); no floats, no RNG, no fits.  NO physics claim, NO RH
claim.  Runtime cap: minutes.

Sources (read-only, machinery rebuilt inline): verification/
v833_gaussian_ramification_ladder.py + v844_message_doily_rank.py
(census, class machinery), v857_simplex_fourier_winding.py (Walsh law,
theta DP, packet thetas, equidistribution to 16, value theorem to
16500), v858_g31_clock_alphabet.py (60 reflections, lines per class),
v634_st31_structure.py (G31 = (Z4 o 2^{1+4}).Sp4(2)), v817 (packet
machinery), Eisenstein E4 / classical E8 theta (Theta_L = 240 sigma_3,
citation).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gaussian_shell_global_probe.py
"""
import hashlib
import itertools
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
CHECKS = []
KILLS = []

NCAP = 24          # DP shell levels (|x|^2 = 8n), exact python ints
N_THETA = 16500    # packet reach (v817/v857 value)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("=" * 74)
print("E8.GAUSSIAN.SHELL.GLOBAL.01 -- transitivity + doubling + theta")
print("identity => Theta_v(n) = (Theta_L - Theta_0)/15 for ALL shells;")
print("Thetahat_u(odd)/Theta_L = -1/15 as a THEOREM (census replaced)")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ======================================================================
section("S1: structural input (i) -- the G31 -> Sp(4,2) class action")
# ======================================================================
STD = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        STD.append(tuple(2 * a for a in v))
for yb in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in yb)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        STD.append(v)
STD = sorted(STD)

J = np.zeros((8, 8), dtype=np.int64)
for k in range(4):
    J[2 * k, 2 * k + 1] = -1
    J[2 * k + 1, 2 * k] = 1
I8 = np.eye(8, dtype=np.int64)
check("S1.1 240 roots (norm 8); J^T = -J; J^2 = -I; (I-J)(I+J) = 2I; "
      "det(I+J) = %d == 16 = |L/(1+i)L|"
      % round(np.linalg.det((I8 + J).astype(float))),
      len(STD) == 240 and len(set(STD)) == 240
      and all(sum(x * x for x in r) == 8 for r in STD)
      and np.array_equal(J.T, -J)
      and np.array_equal(J @ J, -I8)
      and np.array_equal((I8 - J) @ (I8 + J), 2 * I8)
      and round(np.linalg.det((I8 + J).astype(float))) == 16, kill="K1")


def in_L_std(v):
    if all(x % 2 == 0 for x in v):
        return sum(x // 2 for x in v) % 2 == 0
    if all(x % 2 == 1 for x in v):
        return sum(v) % 4 == 0
    return False


def in_pi2L_std(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L_std([x // 2 for x in w])


def ext_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        qt = old_r // r
        old_r, r = r, old_r - qt * r
        old_s, s = s, old_s - qt * s
        old_t, t = t, old_t - qt * t
    return old_r, old_s, old_t


def hnf_det(rows):
    """|det| of the lattice generated by integer rows (greedy upper-
    triangular HNF fold; exact)."""
    H = [[0] * 8 for _ in range(8)]
    for r in rows:
        v = list(r)
        for i in range(8):
            if v is None or v[i] == 0:
                continue
            if H[i][i] == 0:
                if v[i] < 0:
                    v = [-x for x in v]
                H[i] = v
                v = None
            else:
                g, x0, y0 = ext_gcd(H[i][i], v[i])
                new = [x0 * H[i][j] + y0 * v[j] for j in range(8)]
                v = [(H[i][i] // g) * v[j] - (v[i] // g) * H[i][j]
                     for j in range(8)]
                H[i] = new
    det = 1
    for i in range(8):
        det *= H[i][i]
    return abs(det)


det_root_span = hnf_det(STD)
residues = []
for par in ((0, 2), (1, 3)):
    for rho in itertools.product(par, repeat=8):
        if sum(rho) % 4 == 0:
            residues.append(rho)
four_ek = all(in_pi2L_std(tuple(4 if j == k else 0 for j in range(8)))
              for k in range(8))
check("S1.2 lattice = root span: HNF |det| = %d == 256; membership "
      "residues mod 4: %d == 256 => det(L) = 4^8/256 = 256; every "
      "root in L: %s; 4 e_k in (1+i)L for all k: %s (classes are "
      "mod-4 data)"
      % (det_root_span, len(residues),
         all(in_L_std(r) for r in STD), four_ek),
      det_root_span == 256 and len(residues) == 256
      and all(in_L_std(r) for r in STD) and four_ek, kill="K1")

# ---- two labelings: shell path (mod-4 residue reps) vs G31 path (roots)
res_reps = []
res_label = {}
for rho in sorted(residues):
    for li, rep in enumerate(res_reps):
        if in_pi2L_std(tuple(a - b for a, b in zip(rho, rep))):
            res_label[rho] = li
            break
    else:
        res_label[rho] = len(res_reps)
        res_reps.append(rho)


def label_shell(x):
    return res_label[tuple(a % 4 for a in x)]


root_reps = []
root_label = {}
for r in STD:
    for li, rep in enumerate(root_reps):
        if in_pi2L_std(tuple(a - b for a, b in zip(r, rep))):
            root_label[r] = li
            break
    else:
        root_label[r] = len(root_reps)
        root_reps.append(r)

part_shell = {}
part_g31 = {}
for r in STD:
    part_shell.setdefault(label_shell(r), set()).add(r)
    part_g31.setdefault(root_label[r], set()).add(r)
same_partition = ({frozenset(s) for s in part_shell.values()}
                  == {frozenset(s) for s in part_g31.values()})
zero_shell = res_label[(0,) * 8]
census_g31 = sorted(Counter(root_label.values()).values())
check("S1.3 coordination part 1: shell-module labeling (16 residue "
      "classes, zero class = residue 0) and G31-module labeling (%d "
      "root classes) give the SAME partition: %s; census 15 x 16, "
      "zero class EMPTY (no root labels as residue-zero: %s)"
      % (len(root_reps), same_partition,
         all(label_shell(r) != zero_shell for r in STD)),
      len(res_reps) == 16 and len(root_reps) == 15 and same_partition
      and census_g31 == [16] * 15
      and all(label_shell(r) != zero_shell for r in STD), kill="K2")

# canonical 16-class indexing: 0 = zero class, 1..15 = root classes
ZERO = (0,) * 8
REPS16 = [ZERO] + list(root_reps)


def lab16(x):
    hits = [k for k in range(16)
            if in_pi2L_std(tuple(a - b for a, b in zip(x, REPS16[k])))]
    assert len(hits) == 1
    return hits[0]


def b_raw(x, yv):
    d = sum(a * c for a, c in zip(x, yv))
    jy = []
    for k in range(4):
        jy.append(-yv[2 * k + 1])
        jy.append(yv[2 * k])
    dj = sum(a * c for a, c in zip(x, jy))
    assert d % 4 == 0 and dj % 4 == 0
    return (d // 4 + dj // 4) % 2


B = [[b_raw(REPS16[a], REPS16[c]) for c in range(16)] for a in range(16)]
ADD = [[None] * 16 for _ in range(16)]
for a in range(16):
    for c in range(16):
        ADD[a][c] = lab16(tuple(x + z
                                for x, z in zip(REPS16[a], REPS16[c])))
well_def = all(b_raw(r, REPS16[c]) == B[lab16(r)][c]
               for r in STD for c in range(16))
bilinear = all(B[ADD[a][c]][d] == (B[a][d] + B[c][d]) % 2
               for a in range(16) for c in range(16) for d in range(16))
alt = all(B[a][a] == 0 for a in range(16))
sym = all(B[a][c] == B[c][a] for a in range(16) for c in range(16))
rows_bits = [sum(B[a][c] << c for c in range(16)) for a in range(16)]
rank = 0
pivots = []
for rb in rows_bits:
    cur = rb
    for p in pivots:
        cur = min(cur, cur ^ p)
    if cur:
        pivots.append(cur)
        rank += 1
check("S1.4 symplectic form b = ((x.y)/4 + (x.Jy)/4) mod 2: well-"
      "defined on classes (240 x 16): %s; F2-bilinear (16^3): %s; "
      "alternating: %s; symmetric: %s; rank over F2 = %d == 4 "
      "(nondegenerate)" % (well_def, bilinear, alt, sym, rank),
      well_def and bilinear and alt and sym and rank == 4, kill="K2")

# ---- the 60 reflections (v858 machinery) and their induced class maps
ridx = {r: i for i, r in enumerate(STD)}
Jvec = {}
for r in STD + [ZERO]:
    out = []
    for k in range(4):
        out.append(-r[2 * k + 1])
        out.append(r[2 * k])
    Jvec[r] = tuple(out)

line_of = {}
line_reps = []
for r in STD:
    if r in line_of:
        continue
    orb = [r]
    cur = r
    for _ in range(3):
        cur = Jvec[cur]
        orb.append(cur)
    for x in orb:
        line_of[x] = len(line_reps)
    line_reps.append(r)


def refl_apply(vroot, x):
    """complex reflection in the Gaussian line of vroot, exact ints."""
    w = Jvec[vroot]
    d = sum(a * c for a, c in zip(x, vroot))
    dj = sum(a * c for a, c in zip(x, w))
    assert d % 4 == 0 and dj % 4 == 0
    re, im = d // 4, dj // 4
    return tuple(x[i] - re * vroot[i] - im * w[i] for i in range(8))


ok_matrix = True
ok_perm = True
ok_transvec = True
ok_coincide = True
induced_maps = []
for a in range(60):
    vroot = line_reps[a]
    varr = np.array(vroot, dtype=np.int64)
    warr = J @ varr
    M4 = 4 * I8 - np.outer(varr, varr) - np.outer(warr, warr)
    if not np.array_equal(M4.T @ M4, 16 * I8):
        ok_matrix = False
    if not np.array_equal(M4 @ J, J @ M4):
        ok_matrix = False
    imgs = [refl_apply(vroot, r) for r in STD]
    if sorted(imgs) != STD:
        ok_perm = False
    vbar = lab16(vroot)
    gbar = tuple(lab16(refl_apply(vroot, REPS16[k])) for k in range(16))
    pred = tuple(ADD[k][vbar] if B[k][vbar] == 1 else k
                 for k in range(16))
    if gbar != pred:
        ok_transvec = False
    # coincidence of the two action paths on every root
    for r, im_r in zip(STD, imgs):
        if lab16(im_r) != gbar[lab16(r)]:
            ok_coincide = False
            break
    induced_maps.append(gbar)
check("S1.5 coordination part 2 (60 generators): (4M)^T(4M) = 16I and "
      "(4M)J = J(4M): %s; each permutes the 240 roots (preserves L = "
      "root span): %s; induced class map == symplectic transvection "
      "T_vbar: %s; root-permutation path == matrix-on-reps path on "
      "every generator: %s"
      % (ok_matrix, ok_perm, ok_transvec, ok_coincide),
      ok_matrix and ok_perm and ok_transvec and ok_coincide, kill="K2")

IDMAP = tuple(range(16))
pool = {IDMAP}
frontier = [IDMAP]
while frontier:
    nxt = []
    for p in frontier:
        for g in induced_maps:
            qm = tuple(g[p[k]] for k in range(16))
            if qm not in pool:
                pool.add(qm)
                nxt.append(qm)
    frontier = nxt
orbit = {1}
frontier = [1]
while frontier:
    x = frontier.pop()
    for g in induced_maps:
        if g[x] not in orbit:
            orbit.add(g[x])
            frontier.append(g[x])
gens_symp = all(B[g[a]][g[c]] == B[a][c]
                for g in induced_maps
                for a in range(16) for c in range(16))
lines_per_class = Counter(lab16(line_reps[a]) for a in range(60))
check("S1.6 TRANSITIVITY: closure order %d == 720 = |Sp(4,2)|; all 60 "
      "induced generators preserve b: %s; orbit of a nonzero class "
      "has size %d == 15 (ONE orbit); 60 lines cover all 15 classes "
      "at %s per class"
      % (len(pool), gens_symp, len(orbit),
         sorted(set(lines_per_class.values()))),
      len(pool) == 720 and gens_symp and len(orbit) == 15
      and sorted(lines_per_class.values()) == [4] * 15, kill="K2")

# ======================================================================
section("S2: structural input (ii) -- norm doubling by (1+i)")
# ======================================================================
doubling_matrix = np.array_equal((I8 + J).T @ (I8 + J), 2 * I8)
pi_roots = [tuple(r[i] + Jvec[r][i] for i in range(8)) for r in STD]
witness = (len(set(pi_roots)) == 240
           and all(sum(x * x for x in p) == 16 for p in pi_roots)
           and all(lab16(p) == 0 for p in pi_roots))
check("S2.1 (I+J)^T(I+J) = 2I EXACT => |(1+i)x|^2 = 2|x|^2 for every "
      "x; inverse bijection ((1-J)/2)(1+i) = I (S1.1 identity); level-"
      "2 witness: 240 distinct vectors (1+i)r, norm 16, ALL class 0: "
      "%s" % witness,
      doubling_matrix and witness, kill="K3")

# ======================================================================
section("S3: structural input (iii) -- theta identity via mod-4 DP")
# ======================================================================
EMAX = 8 * NCAP
DIGIT = {}
for d in range(4):
    poly = {}
    for zz in range(-16, 17):
        e = (d + 4 * zz) ** 2
        if e <= EMAX:
            poly[e] = poly.get(e, 0) + 1
    DIGIT[d] = poly


def poly_mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = ea + eb
            if e <= EMAX:
                out[e] = out.get(e, 0) + ca * cb
    return out


THETA = [[0] * (NCAP + 1) for _ in range(16)]
fibers = [0] * 16
for rho in residues:
    k = lab16(rho)
    fibers[k] += 1
    poly = {0: 1}
    for i in range(8):
        poly = poly_mul(poly, DIGIT[rho[i]])
    for n in range(NCAP + 1):
        THETA[k][n] += poly.get(8 * n, 0)

sigma3 = [0] * (NCAP + 1)
for d in range(1, NCAP + 1):
    for m in range(d, NCAP + 1, d):
        sigma3[m] += d ** 3
lvl1 = [THETA[k][1] for k in range(16)]
check("S3.1 DP gates: residue fibers %s == {16 x16}; level-1 class "
      "census = (0; 16 x15): %s"
      % (sorted(set(fibers)), lvl1[0] == 0
         and sorted(lvl1[1:]) == [16] * 15),
      sorted(set(fibers)) == [16] and lvl1[0] == 0
      and sorted(lvl1[1:]) == [16] * 15, kill="K4")
theta_L = [sum(THETA[k][n] for k in range(16)) for n in range(NCAP + 1)]
check("S3.2 Theta_L(n) = 240 sigma_3(n) for EVERY n <= %d against the "
      "independent sieve (classical E8 theta = E4, CITED + verified "
      "on the computed range)" % NCAP,
      all(theta_L[n] == 240 * sigma3[n] for n in range(1, NCAP + 1)),
      kill="K4")

odd_zero = all(THETA[0][n] == 0 for n in range(1, NCAP + 1, 2))
even_dbl = all(THETA[0][2 * m] == 240 * sigma3[m]
               for m in range(1, NCAP // 2 + 1))
check("S2.2/S3 RAMIFICATION on the DP range: Theta_0(odd n) = 0 for "
      "all odd n <= %d (proof: |x|^2 = 2|y|^2, |y|^2 in 8Z => level "
      "even); Theta_0(2m) = 240 sigma_3(m) = Theta_L(m) for 2m <= %d; "
      "Theta_0(2) = %d == 240 (witness)"
      % (NCAP, NCAP, THETA[0][2]),
      odd_zero and even_dbl and THETA[0][2] == 240, kill="K3")

# ======================================================================
section("S4: the derived global formulas + the ward")
# ======================================================================
equi_formula = True
for n in range(1, NCAP + 1):
    num = theta_L[n] - THETA[0][n]
    if num % 15 != 0:
        equi_formula = False
        break
    val = num // 15
    if any(THETA[k][n] != val for k in range(1, 16)):
        equi_formula = False
        break
check("S4.1 Theta_v(n) = (Theta_L(n) - Theta_0(n))/15 EXACTLY for "
      "every v != 0 and every n <= %d (15-divisibility exact; "
      "equidistribution = COROLLARY of S1 transitivity + isometry "
      "transport)" % NCAP, equi_formula, kill="K5")

# coordinatize V for the Walsh transform
basis = []
for k in range(1, 16):
    closure = {0}
    fr = [0]
    while fr:
        x = fr.pop()
        for g in basis:
            z = ADD[x][g]
            if z not in closure:
                closure.add(z)
                fr.append(z)
    if k not in closure:
        basis.append(k)
COORD = {}
for bits in itertools.product((0, 1), repeat=4):
    c = 0
    for i, bt in enumerate(bits):
        if bt:
            c = ADD[c][basis[i]]
    COORD[c] = bits
U0 = (0, 0, 0, 0)
THAT = {}
for u in itertools.product((0, 1), repeat=4):
    THAT[u] = [sum((-1) ** (sum(a * b for a, b in zip(u, COORD[k])) % 2)
                   * THETA[k][n] for k in range(16))
               for n in range(NCAP + 1)]


def closed_form(n, sig):
    even_part = 16 * sig[n // 2] if n % 2 == 0 else 0
    return 16 * (even_part - sig[n])


hat_ok = all(15 * THAT[u][n] == 16 * THETA[0][n] - theta_L[n]
             and THAT[u][n] == closed_form(n, sigma3)
             for u in THAT if u != U0 for n in range(1, NCAP + 1))
check("S4.2 Thetahat_u(n) = (16 Theta_0 - Theta_L)/15 = "
      "16 (16 1_{2|n} sigma_3(n/2) - sigma_3(n)) EXACTLY for every "
      "u != 0 and n <= %d" % NCAP,
      len(COORD) == 16 and len(basis) == 4 and hat_ok, kill="K5")


def sparse_theta_terms(kind, cap):
    out = []
    if kind in ("th3", "th4"):
        out.append((0, 1))
        n = 1
        while n * n <= cap:
            out.append((n * n, 2 if kind == "th3" else 2 * ((-1) ** n)))
            n += 1
    else:
        o = 1
        while o * o <= cap:
            out.append((o * o, 2))
            o += 2
    return out


def sparse_mul(dense, terms):
    out = np.zeros_like(dense)
    for e, c in terms:
        if e == 0:
            out += c * dense
        else:
            out[e:] += c * dense[:-e]
    return out


def build_thetas():
    """exact class thetas Th_j, sigma3 to N_THETA (v817/v857
    build_thetas, rebuilt verbatim)."""
    sig3 = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(1, N_THETA + 1):
        sig3[d::d] += d ** 3
    scap = 2 * N_THETA
    t3 = sparse_theta_terms("th3", scap)
    t4 = sparse_theta_terms("th4", scap)
    one = np.zeros(scap + 1, dtype=np.int64)
    one[0] = 1
    p3 = one.copy()
    p4 = one.copy()
    for _ in range(8):
        p3 = sparse_mul(p3, t3)
        p4 = sparse_mul(p4, t4)
    m53 = one.copy()
    for _ in range(5):
        m53 = sparse_mul(m53, t3)
    for _ in range(3):
        m53 = sparse_mul(m53, t4)
    m35 = one.copy()
    for _ in range(5):
        m35 = sparse_mul(m35, t4)
    for _ in range(3):
        m35 = sparse_mul(m35, t3)
    num0 = p3 + m53 + m35 + p4
    num2 = p3 - m53 - m35 + p4
    ok_div = bool(np.all(num0 % 4 == 0) and np.all(num2 % 4 == 0))
    Th0 = (num0 // 4)[::2][:N_THETA + 1].copy()
    Th2 = (num2 // 4)[::2][:N_THETA + 1].copy()
    tcap = 8 * N_THETA
    t2 = sparse_theta_terms("th2", tcap)
    acc = np.zeros(tcap + 1, dtype=np.int64)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    ok_div &= bool(np.all(acc[::8][:N_THETA + 1] % 4 == 0))
    Th1 = (acc[::8][:N_THETA + 1] // 4).copy()
    return dict(sig3=sig3, Th=(Th0, Th1, Th2, Th1), ok_div=ok_div)


TH = build_thetas()
Th0, Th1, Th2, Th3 = TH["Th"]
sig3p = TH["sig3"]
heads = (int(Th0[1]), int(Th1[1]), int(Th2[1]), int(Th3[1]))
glue = bool(np.all((Th0 + Th1 + Th2 + Th3)[1:] == 240 * sig3p[1:]))
num2c = Th0 - Th1 + Th2 - Th3
F = -16 * sig3p.copy()
F[2::2] += 256 * sig3p[1:N_THETA // 2 + 1]
ward_all = bool(np.all(num2c[1:] == F[1:]))
odd_idx = np.arange(1, N_THETA + 1, 2)
odd_thm = bool(np.all(15 * num2c[odd_idx] == -240 * sig3p[odd_idx]))
dp_bridge = all(int(num2c[n]) == THAT[u][n]
                for u in THAT if u != U0 for n in range(1, NCAP + 1))
sieve_agree = all(int(sig3p[n]) == sigma3[n] for n in range(1, NCAP + 1))
check("S4.3 GLOBAL WARD to %d: heads %s == (52,64,60,64); divisibility "
      "certificates: %s; glue Th0+..+Th3 = 240 sigma_3 ALL n: %s; "
      "packet numerator == closed form 16(16 1_{2|n} sigma_3(n/2) - "
      "sigma_3(n)) for EVERY n (odd AND even): %s; == DP Thetahat_u on "
      "n <= %d: %s; odd theorem 15 num = -240 sigma_3: %s => "
      "Thetahat_u/Theta_L = %s at every odd n"
      % (N_THETA, heads, TH["ok_div"], glue, ward_all, NCAP, dp_bridge,
         odd_thm, Fr(-16, 240)),
      heads == (52, 64, 60, 64) and TH["ok_div"] and glue and ward_all
      and dp_bridge and odd_thm and sieve_agree
      and Fr(-16, 240) == Fr(-1, 15), kill="K5")

print("\n  THE STRUCTURAL ARGUMENT (the promotable proof sketch, "
      "step by step):")
print("    LEMMA 1 (invariance + transitivity): every g in G31 is a")
print("      norm-preserving bijection of L ((4M)^T(4M) = 16I; roots ->")
print("      roots; L = root span, S1.2/S1.5) that transports class v")
print("      to gbar(v) (complex-linearity (4M)J = J(4M) makes gbar")
print("      well-defined on V = L/(1+i)L); hence Theta_{gbar(v)}(n) =")
print("      Theta_v(n) for ALL n.  The induced group is Sp(4,2) (order")
print("      720, generated by the 60 transvections T_vbar, S1.5/S1.6),")
print("      TRANSITIVE on the 15 nonzero classes => Theta_v(n) is ONE")
print("      value over v != 0 at every shell n.")
print("    LEMMA 2 (doubling): (I+J)^T(I+J) = 2I => |(1+i)x|^2 =")
print("      2|x|^2, and (1-J)/2 inverts (1+i) on L => Theta_0(2m) =")
print("      Theta_L(m), Theta_0(odd) = 0 (|y|^2 in 8Z forces even")
print("      level).")
print("    LEMMA 3 (theta identity): Theta_L(n) = 240 sigma_3(n)")
print("      (classical: Theta_{E8} = E4; verified here to n = 24 and")
print("      via the packet glue identity to n = 16500).")
print("    CONCLUSION: 15 Theta_v(n) = Theta_L(n) - Theta_0(n) for")
print("      v != 0; Thetahat_u(n) = (16 Theta_0(n) - Theta_L(n))/15 =")
print("      16(16 1_{2|n} sigma_3(n/2) - sigma_3(n)); at odd n:")
print("      Thetahat_u(n) = -16 sigma_3(n), Thetahat_u/Theta_L = -1/15")
print("      EXACTLY -- for ALL odd n, no census cap.")
print("    LEAN NOTES (report): needs (a) the Sp-transitivity as a")
print("      FINITE fact (decidable orbit computation on F_2^4 from the")
print("      60 transvections -- all data in this probe), (b) the")
print("      doubling as the two matrix identities above, (c) the theta")
print("      identity as citation (Eisenstein E4) or finite")
print("      verification; the conclusion is linear algebra over Q.")

# ======================================================================
section("C: controls (each must fire)")
# ======================================================================
T1 = induced_maps[0]
fixed = [k for k in range(1, 16) if T1[k] == k]
moved = [k for k in range(1, 16) if T1[k] != k]
n_orbits = len(fixed) + len(moved) // 2
a_cl, b_cl = fixed[0], fixed[1]
r_prime = [0] + [16] * 15
r_prime[a_cl] = 32
r_prime[b_cl] = 0
h_invariant = all(r_prime[T1[k]] == r_prime[k] for k in range(16))
WP = {}
for u in itertools.product((0, 1), repeat=4):
    WP[u] = sum((-1) ** (sum(x * z for x, z in zip(u, COORD[k])) % 2)
                * r_prime[k] for k in range(16))
mult = Counter(WP[u] for u in WP if u != U0)
full_group_moves = any(any(r_prime[g[k]] != r_prime[k]
                           for k in range(16)) for g in induced_maps)
check("C1 FIRES: non-transitive H = <T_1>: %d orbits on the 15 nonzero "
      "classes (%d fixed + %d swaps) != 1; explicit H-invariant NON-"
      "uniform census (32/0 on two H-fixed classes): invariant %s; "
      "Walsh multiset on u != 0 = %s == {-48: 4, -16: 7, 16: 4} NOT "
      "uniform => the -1/15 law breaks; a full-group generator moves "
      "it: %s (transitivity is load-bearing)"
      % (n_orbits, len(fixed), len(moved) // 2, h_invariant,
         dict(sorted(mult.items())), full_group_moves),
      n_orbits == 11 and len(fixed) == 7 and h_invariant
      and dict(mult) == {-48: 4, -16: 7, 16: 4}
      and len(set(mult)) > 1 and full_group_moves, kill="K6")

even_vals_ok = all(int(num2c[2 * m]) == 16 * (16 * int(sig3p[m])
                                              - int(sig3p[2 * m]))
                   for m in range(1, N_THETA // 2 + 1))
ratio2 = Fr(int(num2c[2]), int(240 * sig3p[2]))
check("C2 FIRES: even-shell formula Thetahat_u(2m) = 16(16 sigma_3(m) "
      "- sigma_3(2m)) for ALL 2m <= %d: %s; at n = 2: Thetahat = %d "
      "== 112, Theta_L = %d == 2160, ratio %s == 7/135 != -1/15 "
      "(the -1/15 law is the ODD-shell statement only)"
      % (N_THETA, even_vals_ok, int(num2c[2]), int(240 * sig3p[2]),
         ratio2),
      even_vals_ok and int(num2c[2]) == 112
      and int(240 * sig3p[2]) == 2160 and ratio2 == Fr(7, 135)
      and ratio2 != Fr(-1, 15), kill="K6")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if KILLS:
    VERDICT = {"K1": "LATTICE-BROKEN", "K2": "ACTION-MISMATCH",
               "K3": "DOUBLING-BROKEN", "K4": "THETA-MISMATCH",
               "K5": "FORMULA-BROKEN", "K6": "CONTROL-DEAD"}[KILLS[0]]
else:
    VERDICT = "SHELL-GLOBAL-THEOREM"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nPROMOTION-READY STATEMENT (report only -- no promotion, no edits):")
print("  THEOREM (global Gaussian shell law): on V = L/(1+i)L of the")
print("  Gaussian E8, for EVERY shell n >= 1: Theta_v(n) = (Theta_L(n)")
print("  - Theta_0(n))/15 for all v != 0, Thetahat_u(n) = 16(16 1_{2|n}")
print("  sigma_3(n/2) - sigma_3(n)) for all u != 0, and at every ODD n:")
print("  Thetahat_u(n) = -16 sigma_3(n), Thetahat_u(n)/Theta_L(n) =")
print("  -1/15 EXACTLY.  Inputs: (i) the G31 class action = the 60")
print("  symplectic transvections generating Sp(4,2), transitive on the")
print("  15 nonzero classes -- and IDENTICAL to the shell-module class")
print("  action (coordination verified on generators); (ii) norm")
print("  doubling by (1+i); (iii) Theta_L = 240 sigma_3 (classical).")
print("  This REPLACES the n <= 16500 census (v857 value theorem) by a")
print("  proof; the census range is retained as the exact ward (matched")
print("  everywhere, odd AND even).  Controls: a non-transitive")
print("  subgroup admits a non-uniform invariant census (the law")
print("  breaks); the even-shell formula differs correctly (7/135 at")
print("  n = 2).")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
