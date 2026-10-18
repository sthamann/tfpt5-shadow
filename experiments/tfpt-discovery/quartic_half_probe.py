#!/usr/bin/env python3
"""quartic_half_probe.py -- E8.QUARTIC.HALF.01 (discovery probe): the
quartic invariant restriction -- is G31 the holomorphic mu4 shadow of
the E8 Coxeter compiler?

HYPOTHESIS (external review, theorem candidate): restricting the
W(E8)-invariant root power sums f_d(x) = sum_roots <alpha, x>^d
(d in Deg W(E8) = {2,8,12,14,18,20,24,30}) to the holomorphic
eigenspace V^{1,0} = ker(J - i) (dim 4) kills exactly the half
{2,14,18,30} (degrees = 2 mod 4) and keeps {8,12,20,24} = Deg(G31)
alive -- 'G31 is the holomorphic mu4 shadow of the E8 compiler'.

RADICAL HONESTY -- the review's own Fallstrick, resolved in layers:

  (L1) the mu4-orbit mechanism: for x in V^{1,0} and any root alpha,
       <J alpha, x> = -i <alpha, x> EXACTLY (verified for all 240
       roots as a weight identity), so summing over each J-orbit
       {a, Ja, -a, -Ja} gives the factor 1 + (-i)^d + (-1)^d + i^d
       = 0 for ALL d != 0 mod 4.  The claimed vanishing {2,14,18,30}
       is therefore TRIVIAL and not degree-list-specific: 6, 10, 22,
       26 vanish identically too (checked).  This is a symbolic
       PROOF of the vanishing half, but it carries no G31 content.
  (L2) the isotropy layer: V^{1,0} of ANY orthogonal complex
       structure is q-isotropic (q = <x,x>), and W(E8) has NO basic
       invariant in degrees 4, 6, 10 (f_4 ~ q^2, f_6 ~ q^3, f_10 in
       q-multiples -- f_4, f_6 proportionality verified SYMBOLICALLY
       as 8-variable polynomial identities here).  So F_4| = F_6| =
       F_10| = 0 persists even on non-compiler complex structures.
  (L3) the SUBSTANCE: F_8|, F_12|, F_20|, F_24| are nonzero (exact
       points; a nonzero value at one exact point is a rigorous
       nonvanishing proof), G31-invariant (all 60 reflections + the
       clock generators sigma, J, exact Gaussian arithmetic), and
       ALGEBRAICALLY INDEPENDENT (exact Jacobian != 0).  With
       degrees (8,12,20,24) = the Molien-unique degree quadruple of
       G31 (v634) and 8*12*20*24 = 46080 = |G31|, Chevalley's
       theorem [maths-lit fact, cited not proved] makes them a
       system of BASIC INVARIANTS: the restriction of the W(E8)
       invariant ring to V^{1,0} generates the FULL G31 invariant
       ring.  That -- not the vanishing pattern -- is the theorem
       candidate's load-bearing content.
  (L4) the Jacobian mirror factorization: sum(d_i - 1) = 60 = number
       of G31 mirror lines; the exact Jacobian vanishes at random
       exact points ON each of the 60 mirrors and is nonzero at
       generic points.  The full polynomial identity
       Jac = c * prod(60 linear forms) is the standard basic-
       invariant Jacobian theorem [cited]; the symbolic degree-60
       expansion is NOT performed here (named residual).

Slices:
  II1  the exact number checks (documented, trivial): Exp(E8) =
       (Z/30)^x, chi_-4 split -> Deg(G31), sums 60/60, Deg W(E8)
       mod-4 halves.
  II2  the restriction test with the honesty layers L1/L2 + exact
       nonvanishing {8,12,16,20,24,28} and SYMBOLIC F_4| = 0
       (35/35 coefficients).
  II3  G31 anchoring: invariance under all 60 reflections + sigma +
       J, exact Jacobian != 0, mirror vanishing 60/60 (L3/L4).
  II4  must-fail controls: (0) HONEST NEGATIVE: the naive pair-
       orientation flip S7 J S7 = J o S67 (even sign flip in W(D8))
       PRESERVES the roots -- signed-permutation complex structures
       cannot break compatibility; (a) J' = R J R^T with R the exact
       rational (3,4,5) rotation crossing the mu4 pairs: NOT root-
       preserving, the informative vanishing {14,18,22,26,30} BREAKS
       while the trivial layers {2,4,6,10} persist (documented);
       (b) J'' = S57 J S57 (root-preserving): the pattern survives
       -- the theorem is about root-compatible complex structures,
       not one matrix; (c) a random non-isotropic 4-space: even
       F_2 != 0.

Exact Gaussian-integer / Gaussian-rational arithmetic throughout
(int pairs / Fraction pairs); no floats anywhere.  Verdict enums
(frozen): QUARTIC-HALF-ALIVE, QUARTIC-HALF-PARTIAL,
QUARTIC-HALF-KILLED.

FIREWALL: experiments/ probe; writes nothing; no verification/,
paper, ledger or website surface touched; typed exploration only.

Predecessors (read-only): v634_st31_structure.py (G31, degrees
8/12/20/24 Molien-unique, 60 reflections, sigma = c^4, J = c^9),
v647/v654 (regular clocks, d/4-theorem).
"""

import itertools
import random
import time
from fractions import Fraction as Fr
from math import factorial, gcd

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


# ------------------------------------------------- Gaussian arithmetic
GZERO = (0, 0)
GONE = (1, 0)
MINUS_I = (0, -1)


def gadd(u, v):
    return (u[0] + v[0], u[1] + v[1])


def gsub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def gmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])


def gconj(u):
    return (u[0], -u[1])


def gpow_list(t, n):
    out = [GONE]
    for _ in range(n):
        out.append(gmul(out[-1], t))
    return out


# ================================================================== S0
section("S0: roots, J, lines, holomorphic weights (doubled coordinates)")

_roots = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        _roots.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        _roots.append(v)
RD = sorted(_roots)
RSET = set(RD)
check("S0.1 240 doubled-integer E8 roots reconstructed", len(RD) == 240)


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


SIGMA_IDX = (4, 5, 0, 1, 2, 3, 6, 7)

line_of = {}
LINES = []
for r in RD:
    if r in line_of:
        continue
    orb = [r]
    y = J_vec(r)
    while y != r:
        orb.append(y)
        y = J_vec(y)
    for x in orb:
        line_of[x] = len(LINES)
    LINES.append(orb)
check("S0.2 J preserves the roots, acts freely, 60 lines of size 4",
      all(J_vec(r) in RSET for r in RD) and len(LINES) == 60
      and all(len(o) == 4 for o in LINES))


def weights_J(r):
    """<alpha, b_k> for b_k = e_2k - i e_2k+1 (basis of ker(J - i))."""
    return ((r[0], -r[1]), (r[2], -r[3]), (r[4], -r[5]), (r[6], -r[7]))


WEIGHTS = [weights_J(r) for r in RD]
W_OF = {r: w for r, w in zip(RD, WEIGHTS)}


def t_val(z, Wr):
    acc = GZERO
    for k in range(4):
        acc = gadd(acc, gmul(z[k], Wr[k]))
    return acc


def F_vals(z, ds, weights=None):
    """exact F_d(z) for all d in ds simultaneously."""
    weights = WEIGHTS if weights is None else weights
    dmax = max(ds)
    tot = {d: GZERO for d in ds}
    for Wr in weights:
        pw = gpow_list(t_val(z, Wr), dmax)
        for d in ds:
            tot[d] = gadd(tot[d], pw[d])
    return tot


def grand(rng, m=3):
    return (rng.randint(-m, m), rng.randint(-m, m))


def grand_vec(rng, m=3):
    return tuple(grand(rng, m) for _ in range(4))


# ================================================================== II1
section("II1: the exact number checks (trivial, documented)")

EXP_E8 = {1, 7, 11, 13, 17, 19, 23, 29}
tot30 = {m for m in range(1, 30) if gcd(m, 30) == 1}
check("II1.1 Exp(E8) = {1,7,11,13,17,19,23,29} = (Z/30)^x (h = 30; the "
      "exponent list is the standard E8 datum, the totative identity is "
      "computed)", tot30 == EXP_E8)

chi_minus = {m for m in EXP_E8 if m % 4 == 3}
DEGS_G31 = (8, 12, 20, 24)
check("II1.2 chi_-4 split: {m in Exp(E8): m = 3 mod 4} = %s; shifted by "
      "+1 = %s = Deg(G31) (Molien-unique per v634 S9.3)"
      % (sorted(chi_minus), sorted(m + 1 for m in chi_minus)),
      chi_minus == {7, 11, 19, 23}
      and tuple(sorted(m + 1 for m in chi_minus)) == DEGS_G31)

check("II1.3 sums 60/60: sum{7,11,19,23} = %d = number of G31 mirror "
      "lines (= 60 J-lines computed in S0.2); complement sum "
      "{1,13,17,29} = %d" % (sum(chi_minus), sum(EXP_E8 - chi_minus)),
      sum(chi_minus) == 60 == sum(EXP_E8 - chi_minus)
      and len(LINES) == 60)

DEG_WE8 = tuple(sorted(m + 1 for m in EXP_E8))
half0 = tuple(d for d in DEG_WE8 if d % 4 == 0)
half2 = tuple(d for d in DEG_WE8 if d % 4 == 2)
check("II1.4 Deg W(E8) = %s; the 0-mod-4 half %s = Deg(G31); the "
      "complement %s is all 2 mod 4; product of the G31 half = %d = "
      "|G31| (v634)" % (DEG_WE8, half0, half2,
                        half0[0] * half0[1] * half0[2] * half0[3]),
      DEG_WE8 == (2, 8, 12, 14, 18, 20, 24, 30)
      and half0 == DEGS_G31 and half2 == (2, 14, 18, 30)
      and 8 * 12 * 20 * 24 == 46080)

# ================================================================== II2
section("II2: the restriction test (with honesty layers L1/L2)")

# --- L1: the mu4-orbit weight identity (symbolic proof of vanishing) ---
ok_orbit = all(W_OF[J_vec(r)] == tuple(gmul(MINUS_I, w) for w in W_OF[r])
               for r in RD)
check("II2.1 [L1, PROOF] W(J alpha) = -i W(alpha) for ALL 240 roots -> "
      "each J-orbit contributes t^d (1 + (-i)^d + (-1)^d + i^d) to "
      "F_d| -- IDENTICALLY ZERO for every d != 0 mod 4: the vanishing "
      "half {2,14,18,30} is proven symbolically, and it is TRIVIAL "
      "(mu4), not degree-list-specific", ok_orbit)

rng = random.Random(20260803)
VAN = (2, 6, 10, 14, 18, 22, 26, 30)
pts = [grand_vec(rng) for _ in range(5)]
van_ok = all(all(F_vals(z, VAN)[d] == GZERO for d in VAN) for z in pts)
check("II2.2 [L1 cross-check] F_d| = 0 at 5 exact random points for ALL "
      "d in %s -- including 6, 10, 22, 26 (NOT in the review's list): "
      "the mod-4 mechanism, exactly" % (VAN,), van_ok)

# --- L2: f_4 ~ q^2 and f_6 ~ q^3 as 8-variable polynomial identities ---
def real_powersum_coeffs(d):
    """coefficients of f_d(x) = sum_a <a,x>^d as an 8-var polynomial."""
    out = {}
    powtabs = [[[c ** e for e in range(d + 1)] for c in r] for r in RD]
    fac = factorial(d)
    for m in itertools.product(range(d + 1), repeat=7):
        s7 = sum(m)
        if s7 > d:
            continue
        mm = m + (d - s7,)
        mult = fac
        for e in mm:
            mult //= factorial(e)
        tot = 0
        for pt in powtabs:
            p = 1
            for i in range(8):
                p *= pt[i][mm[i]]
            tot += p
        if tot:
            out[mm] = mult * tot
    return out


def q_power_coeffs(k):
    """coefficients of q(x)^k = (sum x_i^2)^k."""
    out = {}
    fac = factorial(k)
    for m in itertools.product(range(k + 1), repeat=7):
        s7 = sum(m)
        if s7 > k:
            continue
        mm = m + (k - s7,)
        mult = fac
        for e in mm:
            mult //= factorial(e)
        out[tuple(2 * e for e in mm)] = mult
    return out


t_l2 = time.time()
f4 = real_powersum_coeffs(4)
q2 = q_power_coeffs(2)
lam4 = Fr(f4[(4, 0, 0, 0, 0, 0, 0, 0)], q2[(4, 0, 0, 0, 0, 0, 0, 0)])
ok_f4 = (set(f4) == set(q2)
         and all(Fr(f4[m], q2[m]) == lam4 for m in q2))
f6 = real_powersum_coeffs(6)
q3 = q_power_coeffs(3)
lam6 = Fr(f6[(6, 0, 0, 0, 0, 0, 0, 0)], q3[(6, 0, 0, 0, 0, 0, 0, 0)])
ok_f6 = (set(f6) == set(q3)
         and all(Fr(f6[m], q3[m]) == lam6 for m in q3))
check("II2.3 [L2, PROOF] f_4 = %s q^2 and f_6 = %s q^3 as SYMBOLIC "
      "8-variable identities (%.1f s): W(E8) has no basic invariant in "
      "degrees 4, 6 -> their restriction vanishes on ANY q-isotropic "
      "subspace, mu4 or not" % (lam4, lam6, time.time() - t_l2),
      ok_f4 and ok_f6)

# isotropy: q(b_k) = <b_k, b_k> with b_k = e_2k - i e_2k+1
# = 1^2 + (-i)^2 = 0; verified exactly in Gaussian arithmetic:
q_bk = gadd(gmul(GONE, GONE), gmul((0, -1), (0, -1)))
check("II2.4 [L2] V^{1,0} is q-isotropic: q(b_k) = 1 + (-i)^2 = %s = 0 "
      "exactly -> F_4| = F_6| = F_10| = 0 by L2 alone (also forced by "
      "the G31 Molien series: no invariant below degree 8)" % (q_bk,),
      q_bk == GZERO)

# --- symbolic F_4| = 0: all 35 coefficients of the restricted quartic --
t_f4 = time.time()
pw4 = [[gpow_list(w, 4) for w in Wr] for Wr in WEIGHTS]
n_nonzero4 = 0
for m in itertools.product(range(5), repeat=3):
    if sum(m) > 4:
        continue
    mm = m + (4 - sum(m),)
    tot = GZERO
    for pt in pw4:
        p = GONE
        for k in range(4):
            p = gmul(p, pt[k][mm[k]])
        tot = gadd(tot, p)
    if tot != GZERO:
        n_nonzero4 += 1
check("II2.5 SYMBOLIC: F_4|_{V^{1,0}} has ALL 35 monomial coefficients "
      "= 0 exactly (%.1f s): the first G31-consistency point -- mod-4 "
      "alone would allow F_4 != 0, the invariant theory forbids it "
      "(nonzero coefficients: %d)" % (time.time() - t_f4, n_nonzero4),
      n_nonzero4 == 0)

# --- exact nonvanishing on the 0-mod-4 side -----------------------------
NONVAN = (8, 12, 16, 20, 24, 28)
z_nv = grand_vec(rng)
fv = F_vals(z_nv, NONVAN)
nz = {d: fv[d] != GZERO for d in NONVAN}
print("      F_d| at exact point %s: nonzero pattern %s" % (z_nv, nz))
check("II2.6 F_d| != 0 at an exact point for ALL d in %s (a nonzero "
      "exact value proves nonvanishing rigorously); 16 and 28 are "
      "NON-degrees of G31 -- honest: nonvanishing alone is generic "
      "mod-4 behaviour above degree 4, the G31 content is II3"
      % (NONVAN,), all(nz.values()))

# ================================================================== II3
section("II3: G31 anchoring -- invariance, independence, mirrors")

# complex coordinates of roots and lines
def c4(r):
    return ((r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7]))


ROOTC = [c4(r) for r in RD]
ROOTC_SET = set(ROOTC)
LINE_V = [c4(o[0]) for o in LINES]


def herm(z, V):
    acc = GZERO
    for k in range(4):
        acc = gadd(acc, gmul(z[k], gconj(V[k])))
    return acc


def refl_apply(V, z):
    """R_V(z) = z - (herm(z,V)/4) V; caller guarantees divisibility."""
    h = herm(z, V)
    assert h[0] % 4 == 0 and h[1] % 4 == 0
    s = (h[0] // 4, h[1] // 4)
    return tuple(gsub(z[k], gmul(s, V[k])) for k in range(4))


ok_perm = True
ok_invol = True
for V in LINE_V:
    img = [refl_apply(V, zc) for zc in ROOTC]
    if set(img) != ROOTC_SET:
        ok_perm = False
    if any(refl_apply(V, w) != zc for zc, w in zip(ROOTC, img)):
        ok_invol = False
check("II3.1 all 60 hermitian reflections R_V permute the 240 root "
      "coordinate vectors and are involutions (exact)",
      ok_perm and ok_invol)

DS = (8, 12, 20, 24)
z0 = tuple((4 * a, 4 * b) for (a, b) in grand_vec(rng))
F0 = F_vals(z0, DS)
ok_refl = all(F_vals(refl_apply(V, z0), DS) == F0 for V in LINE_V)


def sig_z(z):
    return (z[2], z[0], z[1], z[3])


def J_z(z):
    return tuple(gmul((0, 1), zk) for zk in z)


ok_gen = True
for _ in range(3):
    zz = grand_vec(rng)
    Fz = F_vals(zz, DS)
    if F_vals(sig_z(zz), DS) != Fz or F_vals(J_z(zz), DS) != Fz:
        ok_gen = False
check("II3.2 G31-INVARIANCE: F_8|, F_12|, F_20|, F_24| invariant under "
      "ALL 60 reflections (exact, one 4Z[i]-point) and under the clock "
      "generators sigma, J (3 exact points each) -- the reflections "
      "generate G31 (v634 S1.3), so the restrictions are G31-invariants",
      ok_refl and ok_gen)


def jac_det(z, weights=None):
    """exact 4x4 Jacobian determinant of (F_8, F_12, F_20, F_24) at z."""
    weights = WEIGHTS if weights is None else weights
    D = [[GZERO] * 4 for _ in range(4)]
    for Wr in weights:
        pw = gpow_list(t_val(z, Wr), 23)
        for i, d in enumerate(DS):
            td = pw[d - 1]
            for j in range(4):
                D[i][j] = gadd(D[i][j], gmul(Wr[j], td))
    for i, d in enumerate(DS):
        D[i] = [gmul((d, 0), x) for x in D[i]]
    tot = GZERO
    for perm in itertools.permutations(range(4)):
        sgn = 1
        for a in range(4):
            for b in range(a + 1, 4):
                if perm[a] > perm[b]:
                    sgn = -sgn
        term = (sgn, 0)
        for r4 in range(4):
            term = gmul(term, D[r4][perm[r4]])
        tot = gadd(tot, term)
    return tot


t_j = time.time()
# small Gaussian-integer points frequently LIE on one of the 60 mirror
# hyperplanes (where the Jacobian must vanish, see II3.5) -- honest
# rejection sampling: test points must avoid all 60 mirrors
jac_pts = []
n_rejected = 0
while len(jac_pts) < 3:
    z = grand_vec(rng)
    if any(herm(z, V) == GZERO for V in LINE_V):
        n_rejected += 1
        continue
    jac_pts.append(z)
jacs = [jac_det(z) for z in jac_pts]
check("II3.3 ALGEBRAIC INDEPENDENCE: exact Jacobian det of (F_8, F_12, "
      "F_20, F_24) nonzero at 3 exact random points OFF all mirrors "
      "(%d small integer points rejected ON mirrors -- where Jac = 0 "
      "is FORCED, see II3.5; %.1f s) -> with degrees (8,12,20,24) "
      "Molien-unique and product 46080 = |G31|, Chevalley [cited] "
      "makes them a system of BASIC INVARIANTS of G31: the holomorphic "
      "restriction of the W(E8) ring generates the FULL G31 invariant "
      "ring" % (n_rejected, time.time() - t_j),
      all(j != GZERO for j in jacs))

check("II3.4 degree bookkeeping: sum(d_i - 1) = %d = number of mirror "
      "lines = deg Jac -- the Jacobian has exactly the degree of the "
      "product of the 60 mirror forms"
      % sum(d - 1 for d in DS), sum(d - 1 for d in DS) == 60)

# mirror vanishing: 2 exact in-hyperplane points per line
t_m = time.time()
ok_mirror = True
n_generic_fail = 0
for li, V in enumerate(LINE_V):
    l0 = next(k for k in range(4) if V[k] != GZERO)
    others = [k for k in range(4) if k != l0]
    us = []
    for k in others:
        u = [GZERO] * 4
        u[k] = gconj(V[l0])
        u[l0] = tuple(-x for x in gconj(V[k]))
        us.append(tuple(u))
    got = 0
    tries = 0
    while got < 2 and tries < 30:
        tries += 1
        cs = [grand(rng, 4) for _ in range(3)]
        z = tuple(gadd(gadd(gmul(cs[0], us[0][k]), gmul(cs[1], us[1][k])),
                       gmul(cs[2], us[2][k])) for k in range(4))
        if all(x == GZERO for x in z) or herm(z, V) != GZERO:
            continue
        if any(herm(z, LINE_V[m]) == GZERO
               for m in range(60) if m != li):
            continue
        got += 1
        if jac_det(z) != GZERO:
            ok_mirror = False
    if got < 2:
        n_generic_fail += 1
check("II3.5 MIRROR FACTORIZATION EVIDENCE: Jac = 0 at 2 exact generic "
      "points ON each of the 60 mirror hyperplanes (off all other "
      "mirrors; %.1f s; lines without 2 generic points: %d) and != 0 "
      "off the mirrors (II3.3); full identity Jac = c prod(60 forms) = "
      "standard basic-invariant theorem [cited], symbolic degree-60 "
      "expansion NOT performed (named residual)"
      % (time.time() - t_m, n_generic_fail),
      ok_mirror and n_generic_fail == 0)

# ================================================================== II4
section("II4: must-fail controls")

# (a) an honest negative first: the review's natural candidate -- flip
# the orientation of one mu4 pair (J' = S7 J S7) -- does NOT fire:
# S7 J S7 = J o S67, and the EVEN sign flip S67 lies in W(D8) < W(E8),
# so this J' preserves the roots.  The same argument covers EVERY
# signed-permutation complex structure: compiler compatibility is
# robust across the whole integral orthogonal class.
def J_s7(x):
    y = list(x)
    y[7] = -y[7]
    z = list(J_vec(tuple(y)))
    z[7] = -z[7]
    return tuple(z)


n_s7 = sum(1 for r in RD if J_s7(r) in RSET)
check("II4.0 HONEST NEGATIVE: the pair-orientation flip J' = S7 J S7 "
      "PRESERVES the root set (%d/240: it equals J o S67 with S67 in "
      "W(D8)) -- signed-permutation complex structures cannot break "
      "compiler compatibility; a genuine must-fail control must leave "
      "the integral orthogonal group" % n_s7, n_s7 == 240)


# the firing control: J' = R J R^T with R the exact rational (3,4,5)
# rotation in the (1,2)-coordinate plane -- R crosses the mu4 pairs
# (0,1) and (2,3), is orthogonal but NOT integral.
def R_apply(x, transpose=False):
    c, s = Fr(3, 5), Fr(4, 5)
    y = [Fr(v) for v in x]
    a, b = y[1], y[2]
    if transpose:
        y[1], y[2] = c * a + s * b, -s * a + c * b
    else:
        y[1], y[2] = c * a - s * b, s * a + c * b
    return tuple(y)


def Jp_vec(x):
    return R_apply(J_vec(R_apply(x, transpose=True)))


EBASIS = [tuple(1 if i == j else 0 for i in range(8)) for j in range(8)]
okJp2 = all(Jp_vec(Jp_vec(e)) == tuple(-Fr(v) for v in e) for e in EBASIS)
okJpO = all(sum(a * b for a, b in zip(Jp_vec(u), Jp_vec(v)))
            == sum(Fr(a) * Fr(b) for a, b in zip(u, v))
            for u in EBASIS for v in EBASIS)
n_kept = 0
for r in RD:
    y = Jp_vec(r)
    if all(v.denominator == 1 for v in y) \
            and tuple(int(v) for v in y) in RSET:
        n_kept += 1
check("II4.1 CONTROL SETUP: J' = R J R^T (exact rational rotation "
      "crossing the mu4 pairs) is an orthogonal complex structure "
      "(J'^2 = -1: %s, orthogonal: %s) that does NOT preserve the "
      "root set (%d/240 root images stay roots)"
      % (okJp2, okJpO, n_kept), okJp2 and okJpO and n_kept < 240)


def weights_Jp(r):
    """<alpha, b'_k> with b'_k = R b_k a basis of ker(J' - i):
    <alpha, R b_k> = <R^T alpha, b_k> (exact Fractions)."""
    rr = R_apply(r, transpose=True)
    return ((rr[0], -rr[1]), (rr[2], -rr[3]),
            (rr[4], -rr[5]), (rr[6], -rr[7]))


WP = [weights_Jp(r) for r in RD]
trivial_persist = True
informative_break = {}
for _ in range(3):
    zz = grand_vec(rng)
    fvp = F_vals(zz, (2, 4, 6, 10, 14, 18, 22, 26, 30), weights=WP)
    if any(fvp[d] != GZERO for d in (2, 4, 6, 10)):
        trivial_persist = False
    for d in (14, 18, 22, 26, 30):
        informative_break[d] = informative_break.get(d, False) or (
            fvp[d] != GZERO)
check("II4.2 CONTROL FIRES (J' = R J R^T): the TRIVIAL layers persist "
      "(F'_2 = F'_4 = F'_6 = F'_10 = 0: isotropy + q-powers, honest) "
      "but the informative mu4 half BREAKS: F'_d != 0 for d in "
      "{14,18,22,26,30}: %s -- the vanishing pattern {14,18,30} is a "
      "property of the COMPILER-compatible (root-preserving) complex "
      "structure, not of orthogonal complex structures per se"
      % ({d: informative_break[d] for d in sorted(informative_break)},),
      trivial_persist and all(informative_break.values()))

# (b) J'' = S57 J S57: root-compatible twin (even sign flip in W(E8))
def Jpp_vec(x):
    y = list(x)
    y[5] = -y[5]
    y[7] = -y[7]
    z = J_vec(tuple(y))
    z = list(z)
    z[5] = -z[5]
    z[7] = -z[7]
    return tuple(z)


n_kept2 = sum(1 for r in RD if Jpp_vec(r) in RSET)


def weights_Jpp(r):
    return ((r[0], -r[1]), (r[2], -r[3]), (r[4], r[5]), (r[6], r[7]))


WPP = [weights_Jpp(r) for r in RD]
ok_twin = True
for _ in range(3):
    zz = grand_vec(rng)
    fvt = F_vals(zz, VAN, weights=WPP)
    if any(fvt[d] != GZERO for d in VAN):
        ok_twin = False
check("II4.3 POSITIVE CONTROL (J'' = S57 J S57, EVEN sign flip, "
      "preserves the roots: %d/240): the full vanishing pattern "
      "SURVIVES on ker(J''- i) -- the theorem candidate is about the "
      "W(E8)-conjugacy class of J (compiler compatibility), not one "
      "matrix" % n_kept2, n_kept2 == 240 and ok_twin)

# (c) random non-isotropic 4-space: even F_2 breaks
rngc = random.Random(4711)
Brand = [[grand(rngc, 2) for _ in range(8)] for _ in range(4)]


def weights_rand(r):
    out = []
    for k in range(4):
        acc = GZERO
        for j in range(8):
            acc = gadd(acc, gmul(Brand[k][j], (r[j], 0)))
        out.append(acc)
    return tuple(out)


WR = [weights_rand(r) for r in RD]
zz = grand_vec(rng)
f2r = F_vals(zz, (2,), weights=WR)[2]
check("II4.4 CONTROL FIRES (random 4-space): F_2 = %s != 0 on a random "
      "non-isotropic subspace -- even the first (isotropy) layer needs "
      "an orthogonal complex structure" % (f2r,), f2r != GZERO)

# ================================================================ summary
section("SUMMARY")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
core = all(ok for n, ok in CHECKS
           if n.split()[0][:3] in ("II1", "II2", "II3", "S0."))
controls = all(ok for n, ok in CHECKS if n.startswith("II4"))
if core and controls:
    print("VERDICT: QUARTIC-HALF-ALIVE -- with the honest split:")
    print("  * vanishing half {2,14,18,30}: TRUE but TRIVIAL (mu4 orbit")
    print("    factor, proven symbolically; holds for 6,10,22,26 too;")
    print("    degree 2/4/6/10 even hold on non-compiler J' via isotropy);")
    print("  * the load-bearing content: F_8|, F_12|, F_20|, F_24| are")
    print("    G31-invariant, algebraically independent (exact Jacobian),")
    print("    degrees Molien-unique, product = |G31| -> a system of")
    print("    BASIC INVARIANTS: the holomorphic restriction of the W(E8)")
    print("    invariant ring generates the FULL G31 invariant ring;")
    print("  * Jacobian carries the 60 mirror lines (point-verified 60/60,")
    print("    full factorization = cited theorem, named residual).")
elif controls:
    print("VERDICT: QUARTIC-HALF-PARTIAL -- controls fire but a core")
    print("check failed; see FAIL lines.")
else:
    print("VERDICT: QUARTIC-HALF-KILLED -- a must-fail control did not")
    print("fire; the pattern is generic, not compiler-specific.")
print("elapsed: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == len(CHECKS) else "SOME CHECKS FAILED")

if __name__ == "__main__":
    raise SystemExit(0 if n_pass == len(CHECKS) else 1)
