#!/usr/bin/env python3
"""Discovery probe: the interacting gamma slice at toy level -- on the
RP-surviving interaction (the alignment bit, v534), the mirror stays
excluded, the generation stays multiplicity-free, and the mark transport
stays PD.  (WOIT gamma milestone, first interacting slice.)

v608 executed the FREE gamma slice (kill tests 3/7 cannot fire at the
free level).  The gamma milestone proper lives on the interacting algebra
A_hol; its only concrete interacting model in the corpus is the
16-Majorana Fidkowski-Kitaev seam toy (v529), where reflection positivity
survives for EXACTLY ONE member x sign of the equivariant mark family:
delta = pi/2 with positive coupling -- the alignment bit (v534).  This
probe runs the gamma battery ON that surviving interaction:

  (I1) TWO PARENTS [float, 1e-9]: the chiral parent (vacuum 2-point
       I + iC, the exact v519 chiral NS kernel) and the MIRROR parent
       (2-point I - iC, the conjugated kernel; the quartet interaction
       is conjugation-invariant, so the mirror system is -H_F + g H_int),
       both with gap 1.

  (I2) SURVIVOR ANCHOR [float, v534 regression]: the chiral interacting
       OS Grams at the forced twist eta = +i are PD (37,0,0) on all four
       admissible cuts {3,7,11,15} for g in {1/32, 1/4, 1, 8}.

  (I3) THE INTERACTING MIRROR FLIP [float, the central datum]: at the
       SAME eta = +i the mirror state's Grams split sector-exactly on
       every cut and every g: even (29,0,0) PD, odd (0,8,0) STRICTLY
       NEGATIVE DEFINITE with max odd eigenvalue <= -1e-3 (bounded away
       from zero over the whole grid) -- every mirror fermion vector has
       strictly negative OS norm AT THE INTERACTING LEVEL: in the
       doubled (vector-like) system any OS-positive subspace meets the
       mirror odd sector in {0} -- kill test (3) cannot fire on the
       surviving interaction class (upgrade of v608 G3 from g = 0 to
       the full coupling grid).

  (I4) CONVENTION CONTROL [float]: eta = -i swaps the roles exactly
       (chiral flips, mirror PD) -- the datum is the RELATIVE chirality;
       the doubled-system argument is convention-free.

  (I5) MARK TRANSPORT INTERACTING [exact + float]: the quarter turn
       alpha_4 maps the mark-A quartet algebra (16 monomials on sites
       {2,3,4,5} of the positive half of cut 3) exactly into the mark-B
       sites {6,7,8,9} (16/16, exact combinatorics), and both the
       mark-algebra OS Gram G_A and the transport form
       T_4[a,b] = <theta(e_a) alpha_4(e_b)> are Hermitian PD (16,0,0)
       at every g -- the incidence-compatible mark transport EXISTS on
       the interacting survivor: kill test (7) does not fire at the
       interacting toy level.

  (I6) MULTIPLICITY-FREE [float]: the generalized odd-block transfer
       spectrum (T_4 vs G_A on the 8 fermionic mark monomials) consists
       of 8 SIMPLE positive eigenvalues at every g in {0, 1/32, 1/4, 1,
       8} (min pairwise gap > 1e-5); honest finding: at strong coupling
       g = 8 the eigenvalues pair up to gaps ~2e-5 WITHOUT closing --
       a strong-coupling near-doubling tendency, strictly simple on the
       declared grid.  The g = 0 baseline is locked (top eigenvalue
       1.641438, bottom 0.018673); observation (no check): the top
       value coincides numerically with the v524 compressed-clock top
       (1.6414) -- the quarter-turn transfer datum recurs across N.

  (I7) DEAD-MEMBER CONTROL [float]: on the RP-dead member (m = 2,
       s = +, g = 1/2) the straddled cut 1 is indefinite (21,16,0)
       while the avoiding cut 9 stays PD -- off the survivor the gamma
       battery has no RP home: the dynamical selection of the bit and
       the chirality data CO-LOCATE on the same member.

  (I8) FIREWALL [C]: one toy, one interaction class, deg <= 2 cut bases
       + the full 16-dim mark algebra, finite coupling grid -- NO
       continuum claim, NO statement about A_hol beyond this model
       class; kill tests (3)/(6)/(7) stay formally live on A_hol; kill
       test (6) (internal SU(2)) is UNTOUCHED by this slice;
       WOIT.OS.TWISTOR.01 does not move.

Verdict enums (frozen): GAMMA-TOY-LANDED (all pass), GAMMA-TOY-FAILS,
MIXED.

Machinery: v529/v534 verbatim (Cl(16) monomial calculus, JW Fock track,
flat-band parent, quartets, cut Grams).  Python-only, counted per
GATE.WOLFRAM.02.
"""

from fractions import Fraction as Fr
from itertools import combinations

import numpy as np
import sympy as sp

N, DIM = 16, 256
TOL_HERM = 1e-8
TOL_ZERO = 1e-9
TOL_ND = 1e-3       # mirror odd sector: bounded away from zero
TOL_GAP = 1e-5      # multiplicity-free: min pairwise eigenvalue gap
GRID = (1.0 / 32, 0.25, 1.0, 8.0)

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ---------------------------------------------------------------- Cl(16)
def mono_mul(m1, m2):
    out = list(m1)
    sign = 1
    for g in m2:
        out.append(g)
        i = len(out) - 1
        while i > 0 and out[i - 1] > out[i]:
            out[i - 1], out[i] = out[i], out[i - 1]
            sign = -sign
            i -= 1
        if i > 0 and out[i - 1] == out[i]:
            del out[i - 1:i + 1]
    return sign, tuple(out)


def cmul(x, y):
    out = {}
    for m1, c1 in x.items():
        for m2, c2 in y.items():
            s, m = mono_mul(m1, m2)
            c = out.get(m, Fr(0)) + s * c1 * c2
            if c:
                out[m] = c
            elif m in out:
                del out[m]
    return out


def gam(*idx):
    return {tuple(idx): Fr(1)}


ONE = {(): Fr(1)}


def refl_map(k, n=N):
    def r(a):
        return (k - a) % n

    def s(a):
        return -1 if (k - a) % (2 * n) >= n else 1
    return r, s


def half_of(k, n=N):
    if k % 2 == 0:
        f1 = (k // 2) % n
        return [(f1 + j) % n for j in range(1, n // 2)]
    b = (k + 1) // 2
    return [(b + j) % n for j in range(n // 2)]


def theta_mono_num(mono, r, s, eta):
    imgs = [r(a) for a in reversed(mono)]
    coeff = complex(eta) ** len(mono)
    for a in mono:
        coeff *= s(a)
    lst = list(imgs)
    sign = 1
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                sign = -sign
    return coeff * sign, tuple(lst)


def tower_maps(n, shift, kmax):
    maps = [(tuple(range(n)), (1,) * n)]
    for _ in range(kmax):
        perm, sign = maps[-1]
        np_, ns_ = [], []
        for a in range(n):
            p, s0 = perm[a], sign[a]
            q = p + shift
            np_.append(q % n)
            ns_.append(s0 * (-1 if (q >= n or q < 0) else 1))
        maps.append((tuple(np_), tuple(ns_)))
    return maps


def alpha_mono(m, pm):
    perm, sign = pm
    c = 1
    imgs = []
    for a in m:
        c *= sign[a]
        imgs.append(perm[a])
    lst = list(imgs)
    sgn = 1
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                sgn = -sgn
    return c * sgn, tuple(lst)


TW = tower_maps(N, 1, N)


def c_of(d, n=N):
    if d % 2 == 0:
        return sp.Integer(0)
    return sp.Rational(2, n) / sp.sin(sp.pi * sp.Rational(d, n))


CNUM = np.zeros((N, N))
for _a in range(N):
    for _b in range(N):
        if _a != _b:
            CNUM[_a, _b] = float(sp.N(c_of(_a - _b), 20))


def build_gammas():
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    E = np.eye(2, dtype=complex)
    gams = []
    for l in range(8):
        for P in (X, Y):
            ops = [Z] * l + [P] + [E] * (7 - l)
            M = ops[0]
            for o in ops[1:]:
                M = np.kron(M, o)
            gams.append(M)
    return gams


GAM = build_gammas()
_MM = {(): np.eye(DIM, dtype=complex)}


def mono_mat(m):
    if m not in _MM:
        M = GAM[m[0]]
        for a in m[1:]:
            M = M @ GAM[a]
        _MM[m] = M
    return _MM[m]


def dict_to_mat(H):
    M = np.zeros((DIM, DIM), dtype=complex)
    for m, c in H.items():
        M += float(c) * mono_mat(m)
    return M


def build_hfree():
    M = np.zeros((DIM, DIM), dtype=complex)
    for a in range(N):
        for b in range(a + 1, N):
            if CNUM[a, b]:
                M += 0.5j * CNUM[a, b] * (GAM[a] @ GAM[b])
    return M


def quartet(b):
    q = ONE
    for j in (b - 2, b - 1, b, b + 1):
        q = cmul(q, gam(j % N))
    return q


def ground(Hm):
    w, Q = np.linalg.eigh(Hm)
    return Q[:, 0], float(w[1] - w[0])


def basis_of(k):
    P = half_of(k)
    return [()] + [(a,) for a in P] + list(combinations(P, 2))


def gram_forms(x, k, eta, basis, alpha_pm=None):
    """OS Gram (and optionally the alpha-transport form) on basis."""
    r, s = refl_map(k)
    th = [theta_mono_num(m, r, s, eta) for m in basis]
    nb = len(basis)
    G = np.zeros((nb, nb), dtype=complex)
    T = np.zeros((nb, nb), dtype=complex) if alpha_pm is not None else None
    for a, (ca, ta) in enumerate(th):
        wa = mono_mat(ta).conj().T @ x
        for b in range(nb):
            G[a, b] = ca * np.vdot(wa, mono_mat(basis[b]) @ x)
            if alpha_pm is not None:
                c2, m2 = alpha_mono(basis[b], alpha_pm)
                T[a, b] = ca * c2 * np.vdot(wa, mono_mat(m2) @ x)
    return G, T


def herm_dev(M):
    return float(np.max(np.abs(M - M.conj().T)))


def inertia(Gh, tol=TOL_ZERO):
    evs = np.linalg.eigvalsh(Gh)
    return (int(np.sum(evs > tol)), int(np.sum(evs < -tol)),
            int(np.sum(np.abs(evs) <= tol)))


CUTS = (3, 7, 11, 15)
MARKA_SITES = (2, 3, 4, 5)
MARKB_SITES = (6, 7, 8, 9)
MARKA = [()]
for _r in range(1, 5):
    MARKA += list(combinations(MARKA_SITES, _r))

# ================================================================== I1
print("=" * 72)
print("I1: the two parents (chiral and mirror kernels)")
print("=" * 72)

HF0 = build_hfree()
parents = {}
for sgn in (1.0, -1.0):
    x, gap = ground(sgn * HF0)
    M2 = np.zeros((N, N), dtype=complex)
    for a in range(N):
        for b in range(N):
            M2[a, b] = np.vdot(x, GAM[a] @ GAM[b] @ x)
    if np.max(np.abs(M2 - (np.eye(N) + 1j * CNUM))) < 1e-9:
        parents['chiral'] = (sgn, gap)
    if np.max(np.abs(M2 - (np.eye(N) - 1j * CNUM))) < 1e-9:
        parents['mirror'] = (sgn, gap)
check("I1.1 chiral parent (2-point I + iC, the v519 chiral NS kernel) and "
      "MIRROR parent (2-point I - iC) identified on opposite sign branches, "
      "both with gap 1",
      set(parents) == {'chiral', 'mirror'}
      and parents['chiral'][0] == -parents['mirror'][0]
      and abs(parents['chiral'][1] - 1) < 1e-9
      and abs(parents['mirror'][1] - 1) < 1e-9)

HF = parents['chiral'][0] * HF0
HINT = sum(dict_to_mat(quartet(b)) for b in (0, 4, 8, 12))   # m = 4 survivor
HINT2 = sum(dict_to_mat(quartet(b)) for b in (0, 2, 8, 10))  # m = 2 control

# ================================================================== I2 + I3
print("=" * 72)
print("I2/I3: survivor anchor + the interacting mirror flip")
print("=" * 72)

anchor_ok = True
flip_ok = True
nd_worst = -np.inf   # largest (closest-to-zero) mirror odd eigenvalue seen
dev_worst = 0.0
for g in GRID:
    xc, _ = ground(HF + g * HINT)
    xm, _ = ground(-HF + g * HINT)
    for k in CUTS:
        basis = basis_of(k)
        oidx = [i for i, m in enumerate(basis) if len(m) % 2 == 1]
        eidx = [i for i, m in enumerate(basis) if len(m) % 2 == 0]
        Gc, _ = gram_forms(xc, k, 1j, basis)
        Gm, _ = gram_forms(xm, k, 1j, basis)
        dev_worst = max(dev_worst, herm_dev(Gc), herm_dev(Gm))
        Gch = (Gc + Gc.conj().T) / 2
        Gmh = (Gm + Gm.conj().T) / 2
        anchor_ok &= inertia(Gch) == (37, 0, 0)
        ie = inertia(Gmh[np.ix_(eidx, eidx)])
        io = inertia(Gmh[np.ix_(oidx, oidx)])
        flip_ok &= (ie == (29, 0, 0) and io == (0, 8, 0))
        nd_worst = max(nd_worst,
                       float(np.linalg.eigvalsh(
                           Gmh[np.ix_(oidx, oidx)]).max()))
    print("  g = %-6s: chiral PD %s | mirror flip %s (worst odd max %.2e)"
          % (g, anchor_ok, flip_ok, nd_worst))
check("I2.1 survivor anchor (v534 regression): chiral Grams PD (37,0,0) at "
      "eta = +i on all four cuts for g in {1/32, 1/4, 1, 8} (Hermiticity "
      "dev < 1e-8)", anchor_ok and dev_worst < TOL_HERM,
      "max herm dev = %.1e" % dev_worst)
check("I3.1 THE INTERACTING MIRROR FLIP: at the SAME eta the mirror state "
      "splits sector-exactly on EVERY cut and EVERY g -- even (29,0,0) PD, "
      "odd (0,8,0) STRICTLY ND", flip_ok)
check("I3.2 the mirror odd sector is BOUNDED AWAY from zero over the whole "
      "grid (max odd eigenvalue <= -1e-3): every mirror fermion vector has "
      "strictly negative OS norm at the interacting level -- in the doubled "
      "vector-like system any OS-positive subspace meets the mirror odd "
      "sector in {0}: kill test (3) cannot fire on the surviving "
      "interaction class", nd_worst <= -TOL_ND,
      "worst mirror odd max eigenvalue = %.2e" % nd_worst)

# ================================================================== I4
print("=" * 72)
print("I4: convention control (eta = -i swaps the roles)")
print("=" * 72)

g = 0.25
xc, _ = ground(HF + g * HINT)
xm, _ = ground(-HF + g * HINT)
basis = basis_of(3)
oidx = [i for i, m in enumerate(basis) if len(m) % 2 == 1]
Gc, _ = gram_forms(xc, 3, -1j, basis)
Gm, _ = gram_forms(xm, 3, -1j, basis)
Gch = (Gc + Gc.conj().T) / 2
Gmh = (Gm + Gm.conj().T) / 2
check("I4.1 at eta = -i the roles swap exactly: chiral odd flips to (0,8,0) "
      "and the mirror Gram is PD (37,0,0) -- the datum is the RELATIVE "
      "chirality; the doubled-system exclusion is convention-free",
      inertia(Gch[np.ix_(oidx, oidx)]) == (0, 8, 0)
      and inertia(Gmh) == (37, 0, 0))

# ================================================================== I5 + I6
print("=" * 72)
print("I5/I6: interacting mark transport + multiplicity-free spectrum")
print("=" * 72)

shift_ok = all(set(alpha_mono(m, TW[4])[1]) <= set(MARKB_SITES)
               for m in MARKA)
check("I5.1 the quarter turn maps the mark-A quartet algebra exactly into "
      "the mark-B sites (alpha_4: {2,3,4,5} -> {6,7,8,9}, 16/16 monomials, "
      "exact combinatorics)", shift_ok)

oidxA = [i for i, m in enumerate(MARKA) if len(m) % 2 == 1]
transport_ok = True
simple_ok = True
min_gap_seen = np.inf
spec0 = None
for g in (0.0,) + GRID:
    x, _ = ground(HF + g * HINT)
    GA, T4 = gram_forms(x, 3, 1j, MARKA, alpha_pm=TW[4])
    dev = max(herm_dev(GA), herm_dev(T4))
    GAh = (GA + GA.conj().T) / 2
    T4h = (T4 + T4.conj().T) / 2
    transport_ok &= (dev < TOL_HERM and inertia(GAh) == (16, 0, 0)
                     and inertia(T4h) == (16, 0, 0))
    Go = GAh[np.ix_(oidxA, oidxA)]
    To = T4h[np.ix_(oidxA, oidxA)]
    L = np.linalg.cholesky(Go)
    Li = np.linalg.inv(L)
    lam = np.sort(np.linalg.eigvalsh(Li @ To @ Li.conj().T))
    gapmin = float(np.diff(lam).min())
    min_gap_seen = min(min_gap_seen, gapmin)
    simple_ok &= (lam.min() > 0 and gapmin > TOL_GAP)
    if g == 0.0:
        spec0 = lam
    print("  g = %-6s: transport PD %s | odd spectrum min %.4f max %.4f "
          "min gap %.2e" % (g, transport_ok, lam.min(), lam.max(), gapmin))
check("I5.2 the mark-algebra Gram G_A AND the transport form T_4 are "
      "Hermitian PD (16,0,0) at EVERY g in {0, 1/32, 1/4, 1, 8}: the "
      "incidence-compatible mark transport EXISTS on the interacting "
      "survivor -- kill test (7) does not fire at the interacting toy "
      "level", transport_ok)
check("I6.1 the generalized odd-block transfer spectrum has 8 SIMPLE "
      "positive eigenvalues at every g (min pairwise gap %.1e > 1e-5); "
      "honest finding: at g = 8 the eigenvalues pair up to ~2e-5 without "
      "closing -- a strong-coupling near-doubling tendency, strictly "
      "simple on the declared grid" % min_gap_seen,
      simple_ok, "min gap over grid = %.2e" % min_gap_seen)
check("I6.2 the g = 0 baseline is locked: top eigenvalue 1.641438, bottom "
      "0.018673 (observation, no check: the top coincides numerically with "
      "the v524 compressed-clock top 1.6414 -- the quarter-turn transfer "
      "datum recurs across N)",
      abs(spec0[-1] - 1.641438) < 1e-5 and abs(spec0[0] - 0.018673) < 1e-5,
      "spec0 = [%s]" % ", ".join("%.6f" % v for v in spec0))

# ================================================================== I7
print("=" * 72)
print("I7: dead-member control (the gamma battery has no RP home off the "
      "survivor)")
print("=" * 72)

x2, _ = ground(HF + 0.5 * HINT2)
res = {}
for k in (1, 9):
    basis = basis_of(k)
    best = None
    for eta in (1j, -1j):
        G, _ = gram_forms(x2, k, eta, basis)
        if herm_dev(G) < TOL_HERM:
            io = inertia((G + G.conj().T) / 2)
            if best is None or io[1] < best[1]:
                best = io
    res[k] = best
check("I7.1 dead-member control (m = 2, s = +, g = 1/2): the straddled cut "
      "1 is INDEFINITE (21,16,0) while the avoiding cut 9 stays PD "
      "(37,0,0) -- off the survivor the gamma battery has no RP home: the "
      "dynamical selection of the bit (v534) and the chirality data "
      "CO-LOCATE on the same member",
      res[1] == (21, 16, 0) and res[9] == (37, 0, 0),
      "cut 1: %s, cut 9: %s" % (res[1], res[9]))

# ================================================================== I8
print("=" * 72)
print("I8: firewall")
print("=" * 72)

check("I8.1 [C] FIREWALL: one toy, one interaction class (FK quartets on "
      "the flat-band parent), deg <= 2 cut bases + the full 16-dim mark "
      "algebra, finite coupling grid -- NO continuum claim, NO statement "
      "about A_hol beyond this model class; kill tests (3)/(6)/(7) stay "
      "formally live on A_hol; kill test (6) (internal SU(2)) is UNTOUCHED "
      "by this slice; WOIT.OS.TWISTOR.01 does not move", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: GAMMA-TOY-LANDED -- on the RP-surviving interaction (the")
    print("alignment bit) the mirror stays excluded sector-exactly, the")
    print("generation stays multiplicity-free, and the mark transport stays PD")
    print("over the whole coupling grid.")
else:
    print("SOME CHECKS FAILED")
