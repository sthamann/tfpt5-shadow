#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""majorana_rp_class_probe -- SEAM.INT.MAJORANA_RP_CLASS.01
(Strategy S2): price the v529 straddle law against the known Majorana
reflection-positivity class (Jaffe-Pedrocchi / Wei-Li-Xiang).

EXPLORATION ONLY (2026-08-27). experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS PROBE EXISTS.  v529 (SEAM.INT.FKTOY.01) MEASURED, on the
16-Majorana Fidkowski-Kitaev (FK) seam toy H_g = H_free + g H_int
(H_int = the NS-shift-covariant FK quartic), that OS reflection
positivity (RP) fails EXACTLY on quartet-straddled cuts and stays PD
on quartet-avoiding ones (the straddle law, 24/24), with the bond-cut
inertia ladder (37,0,0) -> (33,4,0) -> (33,4,0) -> (31,6,0) ->
(29,8,0) at g = 0, 1/4, 1/2, 1, 2.  That was a measurement with no
structural price tag.  This probe prices it against the KNOWN
sufficient condition for Majorana RP: Jaffe-Pedrocchi, "Reflection
Positivity for Majoranas" (arXiv:1406.1384, Ann. Henri Poincare 16
(2015) 189), and the Majorana/Kramers positivity conditions of
Wei-Li-Xiang et al. (arXiv:1601.01994, PRL 116, 250601 (2016)).
EXTERNAL INPUT AT IDEA LEVEL ONLY: nothing is imported on trust; the
condition is implemented from scratch and its soundness is verified
in-probe on anchors (P2) before it is used as an instrument.

THE INSTRUMENT (the JP crossing form, made operational).  For a bond
cut with the v519 NS reflection theta (antilinear, eta in {+i,-i},
signed permutation r/s) splitting the 16 Majoranas into halves L | R,
a Hamiltonian H = H_L + theta(H_L)theta^{-1} + H_X is JP-reflection-
positive if H_X = - sum_k lambda_k A_k theta(A_k) with lambda_k >= 0
and A_k in the left algebra.  Expanding A_k in left monomials M_i,
this is EXACTLY: H_X = - sum_{ij} G_ij M_i theta(M_j) with G a PSD
Gram matrix.  Because (M_i, M_j) -> M_i theta(M_j) is a sign-
decorated BIJECTION onto the crossing monomials (left support =
supp M_i, right support = r(supp M_j)), the coefficient matrix B
with H_X = sum_{ij} B_ij M_i theta(M_j) is UNIQUELY determined by
H_X, and JP-certifiability is DECIDABLE: B Hermitian and -B PSD,
plus exact theta-symmetry of the side parts.  Parity blocks
decouple.  For a quartic H_int the odd block is
[[B11_free, g B13], [g B31, 0]] (the deg-3 diagonal is empty because
H has no degree-6 terms), so PSD forces B13 = 0 EXACTLY (all 1+3 /
3+1 crossing monomials excluded), and the even 2+2 block must be
-PSD on its own (exact rational entries, pairing signs +-1).  The
eta convention affects only the odd block and is frozen by
calibration on the g = 0 anchor; the even block is convention-
independent (eta^2 = -1 for both).

STRUCTURAL PREDICTIONS (items (i), (iii), (v), (vi) derived by hand
from the JP bijection before any run; items (ii) and (iv) CORRECTED
by run 1 -- see TRANSPARENCY -- and now locked regression-style):
 (i)   a quartic monomial contributes a 1+3 / 3+1 (odd) split on
       some bond cut UNLESS its support is antipodal-invariant
       (S + 8 = S); there are exactly 28 antipodal quartic
       monomials, so any JP-certifiable-on-all-cuts quartic is
       supported on them;
 (ii)  [corrected] the antipodal mirror-diagonal census over the 8
       bond axes is {diagonal on exactly 2 axes: 16 monomials,
       diagonal on 0 axes: 12}; ALL 192 off-diagonal cases have
       BOTH even-block partner monomials (supp u r(supp))
       NON-antipodal, and the closure fixed point of the antipodal
       sector under "keep only monomials whose off-diagonal
       partners are alive" is EMPTY -- so the JP class on ALL cuts
       simultaneously is {0} for the WHOLE 1820-dim quartic space
       (covariant or not): expected verdict CLASS_EMPTY_ON_BASIS;
 (iii) the mu4-covariant quartic space has dimension 464
       (1820 monomials = 448 clock orbits of length 4 + 12 of
       length 2 + 4 fixed; every alpha_4 step carries monomial
       coefficient +1: reorder sign (-1)^{k(4-k)} times wrap sign
       (-1)^k is +1 for every wrap count k);
 (iv)  [corrected -- the run-1 DISCOVERY] the m = 4 clock orbit
       (= v529's delta = pi/2 model, == h_marks(4) exactly) is
       JP-certified on FOUR axes {3, 7, 11, 15}: axes 3/11 are
       quartet-avoiding (v529 C3.2), but axes 7/15 are quartet-
       STRADDLED -- each straddling quartet sits CENTERED on the
       cut bond, splitting 2+2 mirror-diagonally with the JP-good
       sign.  JP therefore PREDICTS measured RP survival on
       center-straddled cuts, beyond the v529 census; gate G10
       measures it ((37,0,0) expected at g in {1/2, 1, 2}).  The
       v529 straddle law refines to an ODD-SPLIT law: RP fails
       where a quartet is straddled OFF-center (odd 1+3 split),
       survives where it is centered (even mirror split);
       certifiable-axes histogram over the 464 basis directions:
       {0: 432, 2: 28, 4: 4}, the four 4-axis directions being the
       four consecutive-quartet clock orbits;
 (v)   the FK quartic's crossing part on the bond cut k = 15 has 6
       terms: 4 odd (1+3 / 3+1) and 2 even 2+2, BOTH mirror-
       diagonal with the JP-GOOD sign (-B_ii = +1) -- the straddle-
       law failure is typed ENTIRELY in the odd sector (a
       sharpening of v529's "interference" mechanism);
 (vi)  the single antipodal monomial S0 = g0 g1 g8 g9 is mirror-
       diagonal on axes {1, 9} with JP sign sigma = +1: +S0 is
       certified there and -S0 is not (DIAGSIGN).

PRE-REGISTERED ADJUDICATION (measurement anchors, tolerances and
verdict logic frozen before run 1 and NEVER changed; structural
census numbers in P3/P4 corrected once after run 1, see
TRANSPARENCY):
 P1 anchor reproduction (G02-G05): JW/Clifford exact; free ground
    state reproduces the chiral NS 2-point kernel to < 1e-9; g = 0
    bond Gram inertia (37,0,0) (odd (8,0,0), even (29,0,0)), min
    eigenvalue in (1e-6, 3e-6) [v529: 1.78e-6]; ladder inertias
    match v529 EXACTLY ((37,0,0),(33,4,0),(33,4,0),(31,6,0),
    (29,8,0)), worst min eigenvalue at g = 2 in (-0.1, -0.01)
    [v529: -4.5e-2]; straddle census 24/24 (8 straddled indefinite,
    16 avoiding strictly PD).
 P2 instrument soundness (G06-G08): EXACTLY ONE eta in {+i,-i}
    certifies the (sign-fixed) free Hamiltonian on ALL 8 bond axes
    (B Hermitian dev < 1e-9, min eig(-B) >= -1e-10, side dev
    < 1e-12); measured RP at g = 0 is PD (37,0,0) on all 8 axes;
    the hand-built mutant (sign-flipped free crossing on k = 15) is
    NOT certified (min eig < -1e-3) -- must-fail CAUGHT.
 P3 classification (G09-G12): FK on k = 15 decomposes 5 + 5 + 6
    (left/right/crossing), sides theta-symmetric exactly, crossing
    typed {4 x ODD13, 2 x even-diagonal with -B_ii = +1}; the m = 4
    model is certified on {3, 7, 11, 15} with the center-straddled
    cells 7/15 MEASURED PD (prediction (iv)); confusion matrix over
    35 cells (24-cell straddle census + 5 bond-ladder cells + 6
    center-straddle discovery cells): JP-certifiable <=> measured
    RP PD -- counts 23 / 12 / FP 0 / FN 0; every census-straddled
    cell fails typed ODD13, every avoiding cell is certified.
 P4 class scan (G13-G16): covariant dimension = 464 (census 448 L4
    + 12 L2 + 4 L1, 0 inconsistent, all step coefficients +1);
    never-odd-splitting monomials = exactly the 28 antipodal;
    corrected emptiness lemma verified on all 28 x 8 cases
    (diagonal-axes histogram {2: 16, 0: 12}, all 192 off-diagonal
    partners non-antipodal, closure fixed point EMPTY); brute scan:
    0 of the 464 basis directions and 0 of 64 seeded random
    covariant combinations JP-certifiable on all 8 axes,
    certifiable-axes histogram {0: 432, 2: 28, 4: 4}.
 P5 witness / emptiness branch (G17): no witness expected -- the
    emptiness chain (G14 support exclusion + G15 closure + G16
    brute + random) must agree; IF a witness appears: verify
    genuinely interacting (degree-4 terms, nonzero commutator with
    a bilinear), ground overlap with the free vacuum < 1 - 1e-6,
    and measured RP PD on all 8 axes at g = 1 (min eigenvalues
    printed).
 P6 controls (G18-G19): scrambled clock (seeded signed permutation)
    flagged non-covariant -- CAUGHT; single-monomial control S0 on
    axis 9: predicted sigma = +1; +S0 JP-certified and measured RP
    PD (nneg = 0) at g in {1/2, 1}; -S0 loses the certificate
    (DIAGSIGN) AND loses measured RP (nneg > 0 for some g in
    {1/2, 1, 2}) -- CAUGHT.
 G20 runtime < 180 s; fixed seed 20260827; two identical record
    runs (.run1.log / .run2.log, wall-time line excepted).

=== TRANSPARENCY (run-1 deviation; anchors, tolerances and verdict
logic unchanged) ===
Run 1 (2026-08-27, SPEC_SHA 3d961d76eade9d7b, 17/20, wall 1.8 s)
passed EVERY measurement anchor, instrument and control gate and
already returned CLASS_EMPTY_ON_BASIS (0/464 + 0/64 certifiable),
but caught two errors in the HAND-DERIVED structural predictions:
(a) the m = 4 clock orbit is JP-certified on FOUR axes {3,7,11,15},
not the predicted {3,11} -- on axes 7/15 the straddling quartets are
CENTERED on the cut bond (2+2 mirror-diagonal, good sign), so run 1
DISCOVERED the center-straddle prediction now measured and gated in
G10 (6 new confusion cells, 29 -> 35); (b) the first emptiness lemma
("every antipodal monomial mirror-diagonal on exactly 2 axes") is
wrong -- the correct census is {2: 16, 0: 12} with all 192
off-diagonal partners non-antipodal and an EMPTY closure fixed
point, which RESTORES and strengthens the support-level exclusion
(now covering the whole quartic space).  G10/G11/G15/G16/G17 were
corrected accordingly; no measurement bar, tolerance, seed, verdict
enum or verdict logic moved.  Expected verdict unchanged.

VERDICT ENUM: CLASS_NONEMPTY (a mu4-covariant interacting quartic
JP-certified on all cuts, with direct RP verification) /
CLASS_EMPTY_ON_BASIS (no basis direction and no sampled combination
certifiable; honest: a finite census + a support-level exclusion for
THIS sufficient form, not a theorem about measured RP) /
INSTRUMENT_FAILS (the JP checker is unsound on the anchors).

[C] FENCES (declared): one toy (N = 16, 256-dim Fock), quartic
interactions only, deg <= 2 OS Gram bases (37 = 1 + 8 + 28), the
v529 [C] flat-band parent H_free, float tolerances (Hermiticity
1e-8, eigenvalue zero 1e-9), the JP pairing convention frozen on
the g = 0 anchor.  JP is SUFFICIENT only: non-certifiable does NOT
imply measured RP failure -- on the deployed 35-cell family the two
coincide exactly (the P3 confusion matrix), which is the round's
measured finding, not an assumption.  All v529 machinery (Cl(16)
dicts, kernel, reflections, Gram) is copied verbatim from
verification/v529_seam_interacting_toy_fk.py as read-only basis.

Run:  experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/majorana_rp_class_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

N = 16
DIM = 256
AXES = (1, 3, 5, 7, 9, 11, 13, 15)
G_LADDER = (0.0, 0.25, 0.5, 1.0, 2.0)
SEED = 20260827
TOL_HERM = 1e-8
TOL_ZERO = 1e-9
TOL_DEG = 1e-8
RUNTIME_BAR = 180.0

GATES = []


def check(gid, name, ok, detail):
    ok = bool(ok)
    GATES.append((gid, ok))
    print("  [%s] %s %-38s %s"
          % ("PASS" if ok else "FAIL", gid, name, detail), flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(title):
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ---------------------------------------------------------------------------
# exact Cl(16) monomial machinery (v529/v519 verbatim)
# ---------------------------------------------------------------------------
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


def cadd(x, y):
    out = dict(x)
    for m, c in y.items():
        cc = out.get(m, Fr(0)) + c
        if cc:
            out[m] = cc
        elif m in out:
            del out[m]
    return out


def cscale(x, s):
    return {m: c * s for m, c in x.items()} if s else {}


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


def dict_eq(x, y):
    return not cadd(x, cscale(y, Fr(-1)))


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
    assert len(set(lst)) == len(lst)
    return c * sgn, tuple(lst)


def sperm_dict(H, pm):
    out = {}
    for m, c in H.items():
        c2, m2 = alpha_mono(m, pm)
        cc = out.get(m2, Fr(0)) + c * c2
        if cc:
            out[m2] = cc
        elif m2 in out:
            del out[m2]
    return out


def refl_map(k, n=N):
    def r(a):
        return (k - a) % n

    def s(a):
        return -1 if (k - a) % (2 * n) >= n else 1
    return r, s


def refl_pm(k, n=N):
    r, s = refl_map(k, n)
    return (tuple(r(a) for a in range(n)), tuple(s(a) for a in range(n)))


def half_of(k, n=N):
    if k % 2 == 0:
        f1 = (k // 2) % n
        P = [(f1 + j) % n for j in range(1, n // 2)]
    else:
        b = (k + 1) // 2
        P = [(b + j) % n for j in range(n // 2)]
    rP = {(k - a) % n for a in P}
    assert not (rP & set(P))
    return P


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
    assert len(set(lst)) == len(lst)
    return coeff * sign, tuple(lst)


TW = tower_maps(N, 1, N)
CLOCK_PM = TW[4]                      # the mu4 quarter-shift (v529 clock)
DECK_PM = TW[8]


# ---------------------------------------------------------------------------
# Jordan-Wigner Fock representation (v529 verbatim, float track)
# ---------------------------------------------------------------------------
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
_MONO_MAT = {(): np.eye(DIM, dtype=complex)}


def mono_mat(m):
    if m not in _MONO_MAT:
        M = GAM[m[0]]
        for a in m[1:]:
            M = M @ GAM[a]
        _MONO_MAT[m] = M
    return _MONO_MAT[m]


def dict_to_mat(H):
    M = np.zeros((DIM, DIM), dtype=complex)
    for m, c in H.items():
        M += float(c) * mono_mat(m)
    return M


def dict_to_mat_c(H):
    M = np.zeros((DIM, DIM), dtype=complex)
    for m, c in H.items():
        M += complex(c) * mono_mat(m)
    return M


def herm_dev_mat(M):
    return float(np.max(np.abs(M - M.conj().T)))


def ground_state(Hm):
    w, Q = np.linalg.eigh(Hm)
    deg = int(np.sum(w < w[0] + TOL_DEG))
    if deg == 1:
        return ('pure', Q[:, 0]), float(w[1] - w[0]), 1, w
    rho = Q[:, :deg] @ Q[:, :deg].conj().T / deg
    return ('mix', rho), float(w[deg] - w[0]), deg, w


def expec(state, A):
    kind, x = state
    if kind == 'pure':
        return complex(np.vdot(x, A @ x))
    return complex(np.sum(x * A.T))


def basis_of(k):
    P = half_of(k)
    return [()] + [(a,) for a in P] + list(combinations(P, 2))


def gram_state(state, k, eta, basis):
    r, s = refl_map(k)
    nb = len(basis)
    th = [theta_mono_num(m, r, s, eta) for m in basis]
    G = np.zeros((nb, nb), dtype=complex)
    kind, x = state
    if kind == 'pure':
        vb = [mono_mat(m) @ x for m in basis]
        for a, (ca, ta) in enumerate(th):
            wa = mono_mat(ta).conj().T @ x
            for b in range(nb):
                G[a, b] = ca * np.vdot(wa, vb[b])
    else:
        Mb = [mono_mat(m) for m in basis]
        for a, (ca, ta) in enumerate(th):
            Pa = x @ mono_mat(ta)
            for b in range(nb):
                G[a, b] = ca * np.sum(Pa * Mb[b].T)
    return G


def inertia_num(evs, tol=TOL_ZERO):
    npos = int(np.sum(evs > tol))
    nneg = int(np.sum(evs < -tol))
    return (npos, nneg, len(evs) - npos - nneg)


def gram_report(state, k, basis):
    odd_idx = [i for i, m in enumerate(basis) if len(m) % 2 == 1]
    ev_idx = [i for i, m in enumerate(basis) if len(m) % 2 == 0]
    out = []
    for eta, tag in ((1j, '+i'), (-1j, '-i')):
        G = gram_state(state, k, eta, basis)
        dev = herm_dev_mat(G)
        if dev > TOL_HERM:
            continue
        Gh = (G + G.conj().T) / 2
        evs = np.linalg.eigvalsh(Gh)
        io = inertia_num(np.linalg.eigvalsh(Gh[np.ix_(odd_idx, odd_idx)]))
        ie = inertia_num(np.linalg.eigvalsh(Gh[np.ix_(ev_idx, ev_idx)]))
        out.append((tag, dev, inertia_num(evs), io, ie, np.sort(evs)))
    out.sort(key=lambda t: t[2][1])
    return out


# ---------------------------------------------------------------------------
# Hamiltonians (v529 verbatim)
# ---------------------------------------------------------------------------
def c_of(d):
    if d % 2 == 0:
        return 0.0
    return (2.0 / N) / math.sin(math.pi * d / N)


CNUM = np.zeros((N, N))
for _a in range(N):
    for _b in range(N):
        if _a != _b:
            CNUM[_a, _b] = c_of(_a - _b)


def build_hfree():
    M = np.zeros((DIM, DIM), dtype=complex)
    for a in range(N):
        for b in range(a + 1, N):
            if CNUM[a, b]:
                M += 0.5j * CNUM[a, b] * (GAM[a] @ GAM[b])
    return M


def fk_quartic_ns():
    H = {}
    Qp = {(0, 1, 2, 3): Fr(1)}
    for _ in range(N):
        H = cadd(H, Qp)
        Qp = sperm_dict(Qp, TW[1])
    return H


def quartet(b):
    q = ONE
    for j in (b - 2, b - 1, b, b + 1):
        q = cmul(q, gam(j % N))
    return q


def h_marks(m):
    H = {}
    for b in (0, m, 8, 8 + m):
        H = cadd(H, quartet(b % N))
    return H


def cut_bonds(k):
    x = ((k - 1) // 2) % N
    return ((x, (x + 1) % N), ((x + 8) % N, (x + 9) % N))


def straddles(m, k):
    for b in (0, m, 8, 8 + m):
        sites = {(b - 2) % N, (b - 1) % N, b % N, (b + 1) % N}
        for (x, y) in cut_bonds(k):
            if x in sites and y in sites:
                return True
    return False


HQ = fk_quartic_ns()


# ---------------------------------------------------------------------------
# THE INSTRUMENT: the JP crossing form as a decidable certificate
# ---------------------------------------------------------------------------
def pair_coeff_even(mi, mj, k):
    """exact integer p with M_i . theta_eta(M_j) = p * (sorted union),
    for EVEN M_j (eta^len = (-1)^{len/2}, eta-independent)."""
    r, s = refl_map(k)
    imgs = [r(a) for a in reversed(mj)]
    coeff = (-1) ** (len(mj) // 2)
    for a in mj:
        coeff *= s(a)
    lst = list(imgs)
    sign = 1
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                sign = -sign
    s2, mm = mono_mul(tuple(mi), tuple(lst))
    return coeff * sign * s2, mm


def jp_quartic(h, k):
    """exact JP-certifiability of a real-rational quartic on bond axis
    k: returns (certifiable, failure types, detail dict)."""
    Lset = set(half_of(k))
    r, _s = refl_map(k)
    hl = {m: c for m, c in h.items() if set(m) <= Lset}
    hr = {m: c for m, c in h.items() if not (set(m) & Lset)}
    hx = {m: c for m, c in h.items() if m not in hl and m not in hr}
    types = set()
    if not dict_eq(sperm_dict(hl, refl_pm(k)), hr):
        types.add("SIDEASYM")
    entries = {}
    for m, c in hx.items():
        lm = tuple(a for a in m if a in Lset)
        rm = tuple(a for a in m if a not in Lset)
        if len(lm) % 2 == 1:
            types.add("ODD13")
            continue
        mj = tuple(sorted(r(y) for y in rm))
        pc, mm = pair_coeff_even(lm, mj, k)
        assert mm == m and pc in (1, -1)
        entries[(lm, mj)] = Fr(c) / pc
    for (i, j), c in entries.items():
        if i == j:
            if -c < 0:
                types.add("DIAGSIGN")
        else:
            if entries.get((j, i), Fr(0)) != c:
                types.add("NONHERM")
            if (-entries.get((i, i), Fr(0)) <= 0
                    or -entries.get((j, j), Fr(0)) <= 0):
                types.add("OFFDIAG_NODIAG")
    evmin = None
    if not types and entries:
        idx = sorted({i for i, _ in entries} | {j for _, j in entries})
        pos = {t: n for n, t in enumerate(idx)}
        Bm = np.zeros((len(idx), len(idx)))
        for (i, j), c in entries.items():
            Bm[pos[i], pos[j]] = float(c)
        evmin = float(np.linalg.eigvalsh(-(Bm + Bm.T) / 2)[0])
        if evmin < -1e-12:
            types.add("EVEN_NOTPSD")
    return (not types), types, {
        "nx": len(hx), "nl": len(hl), "nr": len(hr), "entries": entries,
        "evmin": evmin}


def jp_free_block(k, eta, hdict):
    """deg-1 odd-block matrix B of the quadratic crossing part of
    hdict (complex float coefficients on sorted pairs) on axis k."""
    L = half_of(k)
    r, s = refl_map(k)
    B = np.zeros((8, 8), dtype=complex)
    for ia, a in enumerate(L):
        for ib, b in enumerate(L):
            rb = r(b)
            key = (a, rb) if a < rb else (rb, a)
            cf = hdict.get(key, 0j)
            if cf == 0:
                continue
            sgn, _ = mono_mul((a,), (rb,))
            pc = eta * s(b) * sgn
            B[ia, ib] = cf / pc
    dev = herm_dev_mat(B)
    evmin = float(np.linalg.eigvalsh(-(B + B.conj().T) / 2)[0])
    return B, dev, evmin


def theta_dict_num(d, k, eta):
    r, s = refl_map(k)
    out = {}
    for m, c in d.items():
        tc, tm = theta_mono_num(m, r, s, eta)
        out[tm] = out.get(tm, 0j) + np.conj(c) * tc
    return out


def free_side_dev(k, eta, hdict):
    Lset = set(half_of(k))
    dl = {m: c for m, c in hdict.items() if set(m) <= Lset}
    dr = {m: c for m, c in hdict.items() if not (set(m) & Lset)}
    th = theta_dict_num(dl, k, eta)
    keys = set(th) | set(dr)
    if not keys:
        return 0.0
    return max(abs(th.get(m, 0j) - dr.get(m, 0j)) for m in keys)


# ---------------------------------------------------------------------------
# clock-orbit census of the quartic monomial space
# ---------------------------------------------------------------------------
def clock_orbit_census():
    orbits, seen = [], set()
    incons = 0
    all_plus = True
    for m in combinations(range(N), 4):
        if m in seen:
            continue
        orb = {m: 1}
        cur, coeff = m, 1
        while True:
            c2, nxt = alpha_mono(cur, CLOCK_PM)
            if c2 != 1:
                all_plus = False
            coeff *= c2
            cur = nxt
            if cur == m:
                consistent = (coeff == 1)
                break
            orb[cur] = coeff
        seen |= set(orb)
        if consistent:
            orbits.append({mm: Fr(cf) for mm, cf in orb.items()})
        else:
            incons += 1
    return orbits, incons, all_plus


# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("majorana_rp_class_probe -- SEAM.INT.MAJORANA_RP_CLASS.01")
    print("EXPLORATION ONLY (2026-08-27). experiments/ level: NO promotion,"
          " NO ledger row,")
    print("NO marker moved, NO gate closed or narrowed.")
    print("SPEC_SHA = %s" % SPEC_SHA[:16])
    print("=" * 78)

    # =================================================================
    section("S0  firewall / scope")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    allowed = {"ast", "hashlib", "math", "os", "sys", "time",
               "fractions", "itertools", "numpy"}
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for mo in mods:
                root = mo.split(".")[0]
                if root not in allowed:
                    bad.append("import %s" % mo)
                if "verification" in mo:
                    bad.append("verification import %s" % mo)
        if isinstance(node, ast.Attribute) and node.attr == "system":
            bad.append("os.system @%d" % node.lineno)
    check("G01", "firewall/scope",
          not bad,
          "imports whitelisted %s; no verification/ import, no shell "
          "calls, no file writes; standalone sandbox probe%s"
          % (sorted(allowed), ("; VIOLATIONS: " + "; ".join(bad))
             if bad else ""))

    # =================================================================
    section("S1  P1 -- rebuild the v529 toy, reproduce the anchors")
    dev_ac = 0.0
    for a in range(N):
        for b in range(a, N):
            tgt = 2.0 * np.eye(DIM) if a == b else np.zeros((DIM, DIM))
            dev_ac = max(dev_ac, float(np.max(np.abs(
                GAM[a] @ GAM[b] + GAM[b] @ GAM[a] - tgt))))
    Gm = mono_mat(tuple(range(N)))
    dev_par = float(np.max(np.abs(Gm @ Gm - np.eye(DIM))))
    check("G02", "JW Clifford exact",
          dev_ac < 1e-12 and dev_par < 1e-12,
          "136 anticommutators dev %.1e, parity Gamma^2 dev %.1e"
          % (dev_ac, dev_par))

    Hf = build_hfree()
    pick = None
    for sgn in (1.0, -1.0):
        st, gap, deg, w = ground_state(sgn * Hf)
        M2 = np.zeros((N, N), dtype=complex)
        for a in range(N):
            for b in range(N):
                M2[a, b] = expec(st, GAM[a] @ GAM[b])
        dev2 = float(np.max(np.abs(M2 - (np.eye(N) + 1j * CNUM))))
        if dev2 < 1e-9:
            pick = (sgn, gap, deg, dev2)
    HF_SGN = pick[0] if pick else 1.0
    HF_MAT = HF_SGN * Hf
    HFREE = {}
    for a in range(N):
        for b in range(a + 1, N):
            if CNUM[a, b]:
                HFREE[(a, b)] = HF_SGN * 0.5j * CNUM[a, b]
    st0, gap0, deg0, _w0 = ground_state(HF_MAT)
    BASIS = {k: basis_of(k) for k in AXES}
    p0 = gram_report(st0, 15, BASIS[15])[0]
    min0 = float(p0[5][0])
    ok03 = (pick is not None and pick[2] == 1
            and p0[2] == (37, 0, 0) and p0[3] == (8, 0, 0)
            and p0[4] == (29, 0, 0) and 1e-6 < min0 < 3e-6)
    check("G03", "free anchor (kernel + g=0 Gram)",
          ok03,
          "H_free sign %+d, unique ground (gap %.4f), 2-point dev %.1e "
          "(< 1e-9); k=15 Gram eta %s: full %s odd %s even %s, min "
          "%.4e in (1e-6, 3e-6) [v529: 1.7801e-6]"
          % (int(HF_SGN), pick[1] if pick else -1,
             pick[3] if pick else -1, p0[0], p0[2], p0[3], p0[4], min0))

    HQ_MAT = dict_to_mat(HQ)
    LOCK = {0.0: (37, 0, 0), 0.25: (33, 4, 0), 0.5: (33, 4, 0),
            1.0: (31, 6, 0), 2.0: (29, 8, 0)}
    LAD = {}
    print("        bond-cut ladder (k = 15, ground states):")
    for g in G_LADDER:
        st, gap, deg, _ = ground_state(HF_MAT + g * HQ_MAT)
        p = gram_report(st, 15, BASIS[15])[0]
        LAD[g] = (p[2], float(p[5][0]))
        print("          g=%-5s gap %.4f deg %d  eta %s  inertia %s  "
              "min %.4e" % (g, gap, deg, p[0], p[2], float(p[5][0])),
              flush=True)
    worst = min(LAD[g][1] for g in (0.25, 0.5, 1.0, 2.0))
    ok04 = (all(LAD[g][0] == LOCK[g] for g in G_LADDER)
            and -0.1 < worst < -0.01)
    check("G04", "v529 inertia ladder reproduced",
          ok04,
          "inertias %s == v529 lock %s; worst min eig %.4e in "
          "(-0.1, -0.01) [v529: -4.5e-2]"
          % ([LAD[g][0] for g in G_LADDER],
             [LOCK[g] for g in G_LADDER], worst))

    HMARK = {m: h_marks(m) for m in (2, 4, 6)}
    CEN = {}
    print("        straddle census (mark-anchored, ground states):")
    for m in (2, 4, 6):
        for g in (0.25, 0.5, 1.0, 2.0):
            st, _, _, _ = ground_state(
                HF_MAT + g * dict_to_mat(HMARK[m]))
            for k in ((m - 1) % N, (m + 7) % N):
                p = gram_report(st, k, BASIS[k])[0]
                CEN[(m, g, k)] = (p[2], float(p[5][0]), straddles(m, k))
        for k in ((m - 1) % N, (m + 7) % N):
            seq = " ".join(str(CEN[(m, g, k)][0])
                           for g in (0.25, 0.5, 1.0, 2.0))
            print("          m=%d axis %2d [%s]: %s"
                  % (m, k, "straddled" if straddles(m, k)
                     else "avoiding ", seq), flush=True)
    law_ok = all((it[1] > 0) if strad else (it[1] == 0 and it[2] == 0)
                 for (it, _mn, strad) in CEN.values())
    nstrad = sum(1 for v in CEN.values() if v[2])
    check("G05", "straddle law 24/24",
          law_ok and len(CEN) == 24 and nstrad == 8,
          "%d cells: %d straddled all indefinite, %d avoiding all "
          "strictly PD -- v529 B3.1 law reproduced"
          % (len(CEN), nstrad, len(CEN) - nstrad))

    # =================================================================
    section("S2  P2 -- instrument soundness on the anchors")
    cert_etas = []
    freeinfo = {}
    for eta, tag in ((1j, "+i"), (-1j, "-i")):
        rows = {}
        for k in AXES:
            _B, dev, evmin = jp_free_block(k, eta, HFREE)
            sdev = free_side_dev(k, eta, HFREE)
            rows[k] = (dev, evmin, sdev)
        freeinfo[tag] = rows
        if all(d < 1e-9 and e >= -1e-10 and sd < 1e-12
               for (d, e, sd) in rows.values()):
            cert_etas.append(tag)
    ETA_TAG = cert_etas[0] if cert_etas else None
    ETA_JP = {"+i": 1j, "-i": -1j}.get(ETA_TAG, None)
    if ETA_TAG:
        mins = [freeinfo[ETA_TAG][k][1] for k in AXES]
        detail = ("frozen eta_JP = %s; per-axis min eig(-B11) in "
                  "[%.4e, %.4e], herm dev <= %.1e, side dev <= %.1e"
                  % (ETA_TAG, min(mins), max(mins),
                     max(freeinfo[ETA_TAG][k][0] for k in AXES),
                     max(freeinfo[ETA_TAG][k][2] for k in AXES)))
    else:
        detail = ("NO eta certifies the free anchor: %s"
                  % {t: {k: (round(v[0], 12), round(v[1], 6))
                         for k, v in rows_.items()}
                     for t, rows_ in freeinfo.items()})
    ok06 = check("G06", "free H JP-certified on all 8 axes",
                 len(cert_etas) == 1, detail
                 + " [exactly one eta must certify: %s]" % cert_etas)

    g0all = {k: gram_report(st0, k, BASIS[k])[0] for k in AXES}
    ok07 = check("G07", "measured RP at g=0 PD on all axes",
                 all(g0all[k][2] == (37, 0, 0) for k in AXES),
                 "inertia (37,0,0) on all 8 bond axes; mins %s"
                 % ["%.2e" % float(g0all[k][5][0]) for k in AXES])

    Lset15 = set(half_of(15))
    HMUT = {m: (-c if (set(m) & Lset15) and not (set(m) <= Lset15)
                else c) for m, c in HFREE.items()}
    _Bm, devm, evminm = jp_free_block(15, ETA_JP if ETA_JP else 1j, HMUT)
    stm, _, _, _ = ground_state(dict_to_mat_c(HMUT))
    pm = gram_report(stm, 15, BASIS[15])
    pmt = pm[0] if pm else None
    ok08 = check("G08", "must-fail mutant CAUGHT",
                 evminm < -1e-3,
                 "sign-flipped free crossing on k=15: min eig(-B11) = "
                 "%.4e < -1e-3 -- NOT certified (herm dev %.1e); "
                 "measured ground Gram there: %s (datum, not gated)"
                 % (evminm, devm, pmt[2] if pmt else "non-Hermitian"))
    instrument_ok = ok06 and ok07 and ok08

    # =================================================================
    section("S3  P3 -- JP classification vs the measured straddle law")
    cert15, types15, det15 = jp_quartic(HQ, 15)
    dvals = {i: c for (i, j), c in det15["entries"].items() if i == j}
    offd = [(i, j) for (i, j) in det15["entries"] if i != j]
    ok09 = check("G09", "FK decomposition on k=15 typed",
                 (det15["nx"] == 6 and det15["nl"] == 5
                  and det15["nr"] == 5 and types15 == {"ODD13"}
                  and len(dvals) == 2 and not offd
                  and all(c == Fr(-1) for c in dvals.values())),
                 "split 5+5+6, sides theta-symmetric; crossing typed "
                 "%s; the 2 even 2+2 terms are mirror-DIAGONAL with "
                 "the JP-GOOD sign (-B_ii = %s, predicted +1): the "
                 "straddle failure lives ENTIRELY in the odd 1+3 "
                 "sector" % (sorted(types15),
                             [str(-c) for c in dvals.values()]))

    # the run-1 DISCOVERY, measured: m = 4 is JP-certified on the two
    # quartet-avoiding axes 3/11 (empty crossing) AND on the two
    # CENTER-straddled axes 7/15 (2+2 mirror-diagonal, good sign)
    jp4 = {k: jp_quartic(HMARK[4], k) for k in (3, 7, 11, 15)}
    meas4 = [(g, k, CEN[(4, g, k)][0], CEN[(4, g, k)][1])
             for g in (0.5, 1.0) for k in (3, 11)]
    NEW = {}
    for g in (0.5, 1.0, 2.0):
        st, _, _, _ = ground_state(HF_MAT + g * dict_to_mat(HMARK[4]))
        for k in (7, 15):
            p = gram_report(st, k, BASIS[k])[0]
            NEW[(g, k)] = (p[2], float(p[5][0]))
    struct_ok = (all(jp4[k][0] for k in (3, 7, 11, 15))
                 and all(jp4[k][2]["nx"] == 0 for k in (3, 11))
                 and all(jp4[k][2]["nx"] == 2
                         and all(i == j and c == Fr(-1) for (i, j), c
                                 in jp4[k][2]["entries"].items())
                         for k in (7, 15))
                 and all(straddles(4, k) for k in (7, 15)))
    ok10 = check("G10", "center-straddle prediction MEASURED",
                 (struct_ok
                  and all(it == (37, 0, 0) for (_g, _k, it, _mn)
                          in meas4)
                  and all(v[0] == (37, 0, 0) for v in NEW.values())),
                 "m=4 JP-certified on {3,7,11,15}: axes 3/11 crossing "
                 "EMPTY (avoiding, v529 C3.2, measured PD %s); axes "
                 "7/15 quartet-STRADDLED but CENTERED (2 crossing "
                 "quartets each, 2+2 mirror-diagonal, -B_ii = +1) -- "
                 "JP predicts RP survival OFF the v529 census and "
                 "measurement CONFIRMS: %s -- the straddle law "
                 "refines to an ODD-SPLIT law"
                 % (["g=%s k=%d min %.2e" % (g, k, mn)
                     for (g, k, _it, mn) in meas4],
                    ["g=%s k=%d %s min %.2e" % (g, k, v[0], v[1])
                     for (g, k), v in sorted(NEW.items())]))

    cells = []
    for (m, g, k), (it, _mn, strad) in CEN.items():
        cert = (not strad) and instrument_ok \
            and jp_quartic(HMARK[m], k)[0]
        cells.append((cert, it[1] == 0))
    for g in G_LADDER:
        cert = instrument_ok and (g == 0.0 or cert15)
        cells.append((cert, LAD[g][0][1] == 0))
    for (g, k), (it, _mn) in NEW.items():
        cert = instrument_ok and jp_quartic(HMARK[4], k)[0]
        cells.append((cert, it[1] == 0))
    tp = sum(1 for c, pd in cells if c and pd)
    tn = sum(1 for c, pd in cells if not c and not pd)
    fp = sum(1 for c, pd in cells if c and not pd)
    fn = sum(1 for c, pd in cells if not c and pd)
    ok11 = check("G11", "confusion matrix 35 cells",
                 (len(cells) == 35 and tp == 23 and tn == 12
                  and fp == 0 and fn == 0),
                 "JP-certifiable vs measured-RP over 24 census + 5 "
                 "ladder + 6 center-straddle cells: cert&PD %d, "
                 "uncert&fail %d, FP %d, FN %d -- on this family the "
                 "JP boundary tracks measured RP EXACTLY"
                 % (tp, tn, fp, fn))

    typed_ok = True
    typelist = []
    for m in (2, 4, 6):
        for k in ((m - 1) % N, (m + 7) % N):
            cert, tps, _ = jp_quartic(HMARK[m], k)
            if straddles(m, k):
                typed_ok &= ("ODD13" in tps)
                typelist.append("m=%d k=%d %s" % (m, k, sorted(tps)))
            else:
                typed_ok &= cert
    typed_ok &= ("ODD13" in types15)
    ok12 = check("G12", "census-straddled cells typed ODD13",
                 typed_ok,
                 "every CENSUS-straddled cut fails via the odd 1+3 "
                 "sector (zero deg-3 diagonal kills PSD exactly): %s; "
                 "FK k=15 idem; every avoiding cut certified [the "
                 "G10 center-straddled cuts are the complementary "
                 "even case]" % typelist)

    # =================================================================
    section("S4  P4 -- the mu4-covariant quartic class scan")
    DIRS, incons, all_plus = clock_orbit_census()
    lens = {}
    for d in DIRS:
        lens[len(d)] = lens.get(len(d), 0) + 1
    ok13 = check("G13", "covariant space dim = 464",
                 (len(DIRS) == 464 and incons == 0 and all_plus
                  and lens == {4: 448, 2: 12, 1: 4}),
                 "1820 quartic monomials -> %d consistent clock "
                 "orbits (lengths %s, %d inconsistent); every alpha_4 "
                 "step coefficient +1 (reorder x wrap = "
                 "(-1)^{k(4-k)+k} = +1)" % (len(DIRS), lens, incons))

    antipodal = set()
    for m in combinations(range(N), 4):
        if all((a + 8) % N in m for a in m):
            antipodal.add(m)
    never_odd = set()
    for m in combinations(range(N), 4):
        odd_any = False
        for k in AXES:
            Lk = set(half_of(k))
            nl = len(set(m) & Lk)
            if nl % 2 == 1:
                odd_any = True
                break
        if not odd_any:
            never_odd.add(m)
    ok14 = check("G14", "odd-split census: 28 antipodal",
                 never_odd == antipodal and len(antipodal) == 28,
                 "monomials never 1+3/3+1-splitting on any bond axis: "
                 "%d, == the %d antipodal-invariant (S+8 = S) "
                 "monomials exactly; the other %d all odd-split "
                 "somewhere" % (len(never_odd), len(antipodal),
                                1820 - len(never_odd)))

    diaghist = {}
    all2p2 = True
    partner_ok = True
    offcases = 0
    for m in sorted(antipodal):
        nd = 0
        for k in AXES:
            Lk = set(half_of(k))
            r, _s = refl_map(k)
            lm = tuple(a for a in m if a in Lk)
            rm = tuple(a for a in m if a not in Lk)
            if len(lm) != 2:
                all2p2 = False
                continue
            mj = tuple(sorted(r(y) for y in rm))
            if set(mj) == set(lm):
                nd += 1
            else:
                offcases += 1
                Sii = tuple(sorted(set(lm) | {r(a) for a in lm}))
                Sjj = tuple(sorted(set(mj) | {r(a) for a in mj}))
                if Sii in antipodal or Sjj in antipodal:
                    partner_ok = False
        diaghist[nd] = diaghist.get(nd, 0) + 1
    alive = set(antipodal)
    changed = True
    while changed:
        changed = False
        for m in sorted(alive):
            gone = False
            for k in AXES:
                Lk = set(half_of(k))
                r, _s = refl_map(k)
                lm = tuple(a for a in m if a in Lk)
                mj = tuple(sorted(r(y) for y in m if y not in Lk))
                if set(mj) == set(lm):
                    continue
                Sii = tuple(sorted(set(lm) | {r(a) for a in lm}))
                Sjj = tuple(sorted(set(mj) | {r(a) for a in mj}))
                if Sii not in alive or Sjj not in alive:
                    gone = True
                    break
            if gone:
                alive.discard(m)
                changed = True
    ok15 = check("G15", "emptiness lemma census 28 x 8 (corrected)",
                 (all2p2 and diaghist == {2: 16, 0: 12}
                  and partner_ok and offcases == 192
                  and len(alive) == 0),
                 "every antipodal monomial splits 2+2 on every axis; "
                 "mirror-diagonal-axes histogram %s (predicted "
                 "{2: 16, 0: 12}); all %d off-diagonal partner "
                 "monomials (supp u r(supp)) NON-antipodal (%s); "
                 "closure fixed point of the antipodal sector: %d "
                 "monomials survive -- with G14 this pins the "
                 "certifiable-on-all-cuts class of the WHOLE quartic "
                 "space to {0}"
                 % (dict(sorted(diaghist.items())), offcases,
                    partner_ok, len(alive)))

    hm4_keys = frozenset(HMARK[4].keys())
    hm4_axes = None
    hm4_match = False
    n_all8 = 0
    hist = {}
    witness = None
    for d in DIRS:
        ca = tuple(k for k in AXES if jp_quartic(d, k)[0])
        hist[len(ca)] = hist.get(len(ca), 0) + 1
        if len(ca) == 8:
            n_all8 += 1
            if witness is None:
                witness = dict(d)
        if frozenset(d.keys()) == hm4_keys:
            hm4_axes = ca
            hm4_match = dict_eq(d, HMARK[4])
    rng = np.random.default_rng(SEED)
    n_rand_all8 = 0
    rand_cov_ok = True
    for _ in range(64):
        idxs = rng.choice(len(DIRS), 8, replace=False)
        cofs = rng.integers(1, 4, 8) * rng.choice([-1, 1], 8)
        h = {}
        for ii, cf in zip(idxs, cofs):
            h = cadd(h, cscale(DIRS[int(ii)], Fr(int(cf))))
        rand_cov_ok &= dict_eq(sperm_dict(h, CLOCK_PM), h)
        ca = [k for k in AXES if jp_quartic(h, k)[0]]
        if len(ca) == 8:
            n_rand_all8 += 1
            if witness is None:
                witness = dict(h)
    ok16 = check("G16", "brute class scan: 0 certifiable",
                 (n_all8 == 0 and n_rand_all8 == 0 and rand_cov_ok
                  and hist == {0: 432, 2: 28, 4: 4}
                  and hm4_axes == (3, 7, 11, 15) and hm4_match),
                 "464 basis directions: certifiable-axes histogram %s "
                 "(predicted {0: 432, 2: 28, 4: 4}) -> %d certifiable "
                 "on all 8; 64 seeded random covariant combinations "
                 "(all alpha_4-invariant exactly): %d on all 8; the "
                 "m=4 clock orbit (== h_marks(4) exactly) certified "
                 "on exactly axes %s (predicted (3, 7, 11, 15))"
                 % (dict(sorted(hist.items())), n_all8, n_rand_all8,
                    list(hm4_axes) if hm4_axes else None))

    # =================================================================
    section("S5  P5 -- verdict branch (witness / emptiness chain)")
    if not instrument_ok:
        VERDICT = "INSTRUMENT_FAILS"
    elif witness is not None:
        VERDICT = "CLASS_NONEMPTY"
    else:
        VERDICT = "CLASS_EMPTY_ON_BASIS"

    if witness is None:
        chain_ok = ok14 and ok15 and n_all8 == 0 and n_rand_all8 == 0
        ok17 = check("G17", "emptiness chain consistent",
                     chain_ok,
                     "structural route (G14 support exclusion + G15 "
                     "empty closure fixed point) and brute route "
                     "(G16: 0/464 basis + 0/64 random) AGREE: within "
                     "the JP sufficient form, NO nonzero quartic -- "
                     "covariant or not -- is RP-certifiable on all 8 "
                     "bond cuts")
    else:
        wmat = dict_to_mat(witness)
        deg4 = all(len(m) == 4 for m in witness)
        b01 = mono_mat((0, 1))
        commdev = float(np.max(np.abs(wmat @ b01 - b01 @ wmat)))
        stw, _, degw, _ = ground_state(HF_MAT + 1.0 * wmat)
        ov = (abs(complex(np.vdot(st0[1], stw[1])))
              if stw[0] == 'pure' else float('nan'))
        mins = []
        okrp = True
        for k in AXES:
            pw = gram_report(stw, k, BASIS[k])
            okrp &= bool(pw) and pw[0][2][1] == 0
            mins.append(float(pw[0][5][0]) if pw else float('nan'))
        info("WITNESS coefficients: %s"
             % {m: str(c) for m, c in sorted(witness.items())})
        ok17 = check("G17", "witness verified",
                     deg4 and commdev > 1e-8 and ov < 1 - 1e-6
                     and okrp,
                     "degree-4 %s, [h, g0 g1] dev %.2e > 1e-8 "
                     "(interacting), |<Om_0|Om_w>| = %.8f < 1-1e-6, "
                     "measured RP mins on all axes at g=1: %s"
                     % (deg4, commdev, ov,
                        ["%.2e" % x for x in mins]))

    # =================================================================
    section("S6  P6 -- controls")
    perm = tuple(int(x) for x in rng.permutation(N))
    sgns = tuple(int(x) for x in rng.choice([-1, 1], N))
    pm_scr = (perm, sgns)
    hq_cov = dict_eq(sperm_dict(HQ, CLOCK_PM), HQ)
    hq_scr = dict_eq(sperm_dict(HQ, pm_scr), HQ)
    d_scr = {(0, 1, 2, 3): Fr(1)}
    cur = (0, 1, 2, 3)
    cf = 1
    for _ in range(3):
        c2, cur = alpha_mono(cur, pm_scr)
        cf *= c2
        d_scr = cadd(d_scr, {cur: Fr(cf)})
    scr_cov = dict_eq(sperm_dict(d_scr, CLOCK_PM), d_scr)
    ok18 = check("G18", "scrambled clock CAUGHT",
                 hq_cov and (not hq_scr) and (not scr_cov),
                 "H_q alpha_4-covariant exactly (%s); H_q NOT "
                 "invariant under the seeded scrambled signed "
                 "permutation (%s); the scrambled-orbit direction is "
                 "flagged NON-covariant (%s) -- the covariance "
                 "instrument has teeth" % (hq_cov, hq_scr, scr_cov))

    S0 = (0, 1, 8, 9)
    sigma = None
    for sg in (1, -1):
        if jp_quartic({S0: Fr(sg)}, 9)[0]:
            sigma = sg
    diag_axes_S0 = tuple(k for k in AXES
                         if jp_quartic({S0: Fr(sigma or 1)}, k)[0])
    res19 = {}
    for sg, gs in ((sigma or 1, (0.5, 1.0)),
                   (-(sigma or 1), (0.5, 1.0, 2.0))):
        hmat = dict_to_mat({S0: Fr(sg)})
        for g in gs:
            st, _, deg, _ = ground_state(HF_MAT + g * hmat)
            p = gram_report(st, 9, BASIS[9])[0]
            res19[(sg, g)] = (p[2], float(p[5][0]), deg)
    pos_ok = all(res19[(sigma or 1, g)][0][1] == 0 for g in (0.5, 1.0))
    neg_cert, neg_types, _ = jp_quartic({S0: Fr(-(sigma or 1))}, 9)
    neg_fail = any(res19[(-(sigma or 1), g)][0][1] > 0
                   for g in (0.5, 1.0, 2.0))
    ok19 = check("G19", "S0 sign control (JP has teeth)",
                 (sigma == 1 and diag_axes_S0 == (1, 9) and pos_ok
                  and (not neg_cert) and "DIAGSIGN" in neg_types
                  and neg_fail),
                 "S0 = g0 g1 g8 g9: JP sign sigma = %s (predicted +1), "
                 "mirror-diagonal certified on axes %s (predicted "
                 "(1, 9)); +S0 measured RP on axis 9: %s; -S0 NOT "
                 "certified (%s) and measured RP: %s -- the wrong "
                 "sign both loses the certificate AND breaks measured "
                 "RP" % (sigma, list(diag_axes_S0),
                         {g: (res19[(sigma or 1, g)][0],
                              "%.2e" % res19[(sigma or 1, g)][1])
                          for g in (0.5, 1.0)},
                         sorted(neg_types),
                         {g: (res19[(-(sigma or 1), g)][0],
                              "%.2e" % res19[(-(sigma or 1), g)][1])
                          for g in (0.5, 1.0, 2.0)}))

    # =================================================================
    wall = time.time() - T0_WALL
    check("G20", "runtime + determinism",
          wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f); seed %d fixed; eigh/np "
          "deterministic; two record runs diffed" % (wall, RUNTIME_BAR,
                                                     SEED))

    # =================================================================
    section("FINAL REPORT")
    npass = sum(1 for _g, ok in GATES if ok)
    info("anchors: ladder %s; straddle census 24/24 (8 straddled / 16 "
         "avoiding); g=0 min %.4e"
         % ([LAD[g][0] for g in G_LADDER], min0))
    info("instrument: eta_JP = %s; free-anchor min eig(-B11) range "
         "[%.4e, %.4e] over 8 axes; mutant min %.4e CAUGHT"
         % (ETA_TAG,
            min(freeinfo[ETA_TAG][k][1] for k in AXES) if ETA_TAG else
            float('nan'),
            max(freeinfo[ETA_TAG][k][1] for k in AXES) if ETA_TAG else
            float('nan'), evminm))
    info("classification: confusion (cert&PD, uncert&fail, FP, FN) = "
         "(%d, %d, %d, %d) over 35 cells; census-straddled failures "
         "all typed ODD13; FK even 2+2 entries JP-GOOD (-B_ii = +1); "
         "center-straddled m=4 cells on axes 7/15 JP-certified AND "
         "measured PD: %s" % (tp, tn, fp, fn,
                              {("g=%s k=%d" % (g, k)): v[0]
                               for (g, k), v in sorted(NEW.items())}))
    info("class scan: covariant dim %d (448 L4 + 12 L2 + 4 L1); 28 "
         "antipodal monomials; diagonal-axes hist %s; certifiable on "
         "all 8 cuts: %d basis + %d random; closure fixed point %d"
         % (len(DIRS), dict(sorted(diaghist.items())), n_all8,
            n_rand_all8, len(alive)))
    info("controls: sigma(S0) = %s on axes %s; -S0 lost certificate "
         "AND measured RP %s" % (sigma, list(diag_axes_S0),
                                 {g: res19[(-(sigma or 1), g)][0]
                                  for g in (0.5, 1.0, 2.0)}))
    info("honest limitations: one N = 16 toy, quartic class only, "
         "deg <= 2 OS bases, [C] flat-band parent; JP is a SUFFICIENT "
         "condition -- CLASS_EMPTY_ON_BASIS is a statement about the "
         "JP-certifiable class (finite census + support-level "
         "exclusion), NOT a no-go for measured RP; the confusion "
         "matrix shows measured RP and JP coincide on the deployed "
         "35-cell family, which is a finding, not an assumption.")
    print("=" * 78)
    if npass == len(GATES):
        print("ALL GATES PASSED %d/%d" % (npass, len(GATES)))
    else:
        print("GATES PASSED %d/%d -- FAILURES PRESENT"
              % (npass, len(GATES)))
    if VERDICT == "CLASS_EMPTY_ON_BASIS":
        vtxt = ("no mu4-covariant quartic direction (464-dim basis; 64 "
                "seeded combos; the support-level exclusion pins the "
                "whole 1820-dim quartic space) is JP-reflection-"
                "positive on all 8 bond cuts -- the v529 straddle law "
                "is the generic face of the Majorana-RP class "
                "boundary, refined to an odd-split law; honest: "
                "finite census for a sufficient condition, not a "
                "theorem about measured RP")
    elif VERDICT == "CLASS_NONEMPTY":
        vtxt = "witness found and verified (see G17)"
    else:
        vtxt = "JP checker unsound on anchors (see G06-G08)"
    print("VERDICT: %s -- %s" % (VERDICT, vtxt))
    print("EXPLORATION ONLY: no promotion, no ledger row, no marker "
          "moved, no gate closed or narrowed.")
    print("SPEC_SHA = %s" % SPEC_SHA[:16])
    print("=" * 78)
    return 0 if npass == len(GATES) else 1


if __name__ == "__main__":
    sys.exit(main())
