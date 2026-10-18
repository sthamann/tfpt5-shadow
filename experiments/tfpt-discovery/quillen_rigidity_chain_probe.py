#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""quillen_rigidity_chain_probe -- ALPHA.QUILLEN.RIGIDITY_CHAIN.01
(Strategy S9): the conditional chain that collapses
ALPHA.QUILLEN.EXACT.01 onto the seam-state rigidity lemma, made
executable and verified at its finite shadow.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  ALPHA.QUILLEN.EXACT.01 (ledger row; v341 /
v382 / v484 / v485) is the one remaining EM obligation: the from-
first-principles proof that F_U(1) = a^3 - 2 c3^3 a^2 - 8 b1 c3^6
ln(1/phi_seam) is the EXACT zeta-regularised Quillen functional of
the seam U(1).  v472 (ALPHA.QUILLEN.DETLINE.01) computed the finite
Quillen shadow -- the determinant-line Chern over the U(1)-twist
moduli of the collar model = 1, size-independent -- but only ONE
side of Quillen's identity: the FHS/Berry curvature of the occupied-
band line bundle.  Quillen's theorem has TWO sides: the curvature of
the DETERMINANT-LINE METRIC ||s||^2 (the norm of the overlap
section, i.e. i ddbar log||det||^2 of the Gaussian overlap kernel)
reproduces the Berry/index form up to a LOCAL ANOMALY term (Quillen
1985; Bismut-Freed CMP 106 (1986)).  IF the seam state is quasi-free
-- the rigidity target of the parallel S1 probe
seam_rp_rigidity_probe.py (premise SEAM.RP.RIGIDITY; terrain v903,
where OS positivity <=> a_J = 0 forces the quasi-free-diagonal point
on the deployed family) -- THEN the seam determinant line IS a
free-fermion determinant line and the identity applies literally.
THIS probe makes the chain executable at the finite shadow:
  L1 verifies BOTH sides of the identity on the v472 collar family
     over the twist torus and measures the difference field;
  L2 types the conditional on the named premise (printed, NOT a
     numeric gate -- the premise is NOT assumed proven);
  L3 re-verifies the value-level anchor exactly (the Quillen split
     at the alpha root, mpmath 50 digits + exact Fractions);
  L4 prints the resulting DAG: with L1 verified and L2 conditional,
     the remaining open content of ALPHA.QUILLEN.EXACT.01 is exactly
     {the rigidity premise} + {the diagonal-zeta face} + {EM1} --
     no ADDITIONAL analytic unknown; parallel probes cross-named:
     seam_bfk_conical_det_probe (the diagonal-zeta / conical-
     determinant face), laughlin_pump_em1_probe (EM1).

THE SETUP (v472 VERBATIM).  Collar Hamiltonian h(k) = sin kx SX +
sin ky SY + (M - cos kx - cos ky) SZ (v367/v470), in real space on
an L x L torus with U(1)-twisted boundary conditions; the twist
torus (theta_x, theta_y) is the moduli space of flat U(1)
connections.  The many-body ground state at half filling is the
Slater determinant of the occupied one-particle frame U(theta)
(2L^2 x L^2 columns); the family is QUASI-FREE (Gaussian) by
construction -- exactly the hypothesis of the L2 conditional,
realised here so the L1 identity can be tested where the premise
HOLDS.  Main cell M = 1 (C = 1 phase), L = 4, twist grid 48 x 48
(offset half-cell so reference twists and section zeros avoid grid
nodes); confirmation cell L = 6, grid 24 x 24; controls M = 3
(C = 0) and M = -1 (C = -1) at L = 4, grid 24.

L1 IMPLEMENTATION AND THE HONEST DISCRETE MATH.
 (a) BERRY SIDE: the FHS field strength F(p) in (-pi, pi] per
     plaquette from det-overlap link variables of the occupied
     frames; integral C_FHS = (1/2 pi) sum_p F(p) = the det-line
     Chern (v472's = 1, re-derived).
 (b) QUILLEN-METRIC SIDE: with a fixed reference frame U_ref the
     overlap section is s(theta) = det(U_ref^dag U(theta)) (Slater
     overlap formula); its squared norm N = |s|^2 is gauge-invariant
     and satisfies the finite Quillen-metric identity
         N(theta) = det( U_ref^dag P(theta) U_ref ),
     P = U U^dag the Gaussian covariance/overlap kernel -- the
     ||det||^2 = det(kernel) statement at finite size, exact linear
     algebra, gated pointwise at 1e-12.  The distributional
     (i/2 pi) ddbar log N is, by Poincare-Lelong, the DIVISOR of the
     section; on the grid it is evaluated EXACTLY by the plaquette
     winding n(p) = (W(p) + F(p)) / (2 pi), where W(p) is the
     branch-fixed circulation of the gauge-invariant link field
     arg[ s(b) conj(s(a)) conj(L(a,b)) ] (the covariant derivative
     of the section along the link; L(a,b) = det-overlap link).
     Bookkeeping facts gated: each n(p) is an integer to float
     precision (the plaquette product is real positive by
     construction); sum_p n(p) = C_FHS exactly (telescoping
     sum_p W(p) = 0); and the POINTWISE difference field between
     the two curvature readings, F(p) - 2 pi n(p) = -W(p), is the
     coboundary of a globally defined link 1-form -- a smooth EXACT
     form with total integral 0 (the finite 'local anomaly term' of
     Quillen's identity, exhibited as an exact form).  The NAIVE
     smeared FD Laplacian of log N totals 0 identically (divisor
     deltas cancel the smooth part -- printed as INFO): that
     telescoping identity is WHY the divisor evaluation is the
     correct finite reading of the (b)-integral.
 PATCHING: a degree-1 line bundle admits no nonvanishing section,
     so s HAS zeros over the torus; two references are used
     (ground frames at twists (0,0) and (pi,pi)), the transition
     function t12 = s1/s2 is gauge-invariant, and the winding of
     t12 around the zeros of s2 equals the Chern number (Dai-Freed
     section / Quillen divisor picture) -- gated, together with
     disjointness of the two vortex sets and the pointwise
     transition-winding identity wt(p) = n1(p) - n2(p).

L3 ANCHOR (v341 VERBATIM, sharpened to 50 digits): F_U(1)(a) =
a^3 - 2 c3^3 a^2 - (4/5) 41 c3^6 ln(1/phi_seam(a)) with phi_seam =
1/(6 pi) + Q (1-Q)^(-5/4), Q = 48 c3^4 e^(-2a); exact coefficients
8 b1 = 8 * 41/10 = 164/5 = (4/5)*41 (Fractions), c3 = 1/(8 pi)
(sympy), phi_base = (4/3) c3, q(D5) + q(A3) = 5/4 + 3/4 = 2; root
alpha^-1 = 137.0359992168 and Quillen-split residual
|lhs - rhs| < 1e-30 at mpmath dps = 50.

PRE-REGISTERED ADJUDICATION (frozen before the record runs; ONE
disclosed smoke run informed the vortex-census bars -- see
SMOKE-RUN DISCLOSURE):
 P1 both tori, both sizes: Bloch C(M=1,3,-1) = (1,0,-1); twist FHS
    = 1 at L = 4 (grid 48) AND L = 6 (grid 24), |dev| < 1e-9; Fermi
    gap > 1.9 over the whole twist torus at M = 1.
 P2 the Quillen norm identity |s|^2 = det(U_ref^dag P U_ref) holds
    to 1e-12 absolute (N, det both in [0,1]) at every sampled twist,
    BOTH references.
 P3 divisor = the (b)-integral: n(p) integer to 1e-9 everywhere;
    sum_p n = 1 = C_FHS for ref1, ref2 AND the L = 6 family; the
    difference-form total |C_FHS_float - sum n| < 1e-8; pointwise
    |F - 2 pi n + W| < 1e-9.
 P4 localization: the vortex set is small (<= 3 cells, net charge
    +1 each ref) and sits where the metric says it must -- the
    global grid minimum of |s| lies in/adjacent to a vortex cell
    (Chebyshev distance <= 1 on the torus).
 P5 patching: vortex sets of s1 and s2 DISJOINT; wt(p) = n1(p) -
    n2(p) at EVERY plaquette; total winding of t12 = 0 exactly;
    winding of the transition function around the s2 zeros = 1 =
    C (and around the s1 zeros = 1).
 P6 controls: M = 3 -> (C_FHS, sum n) = (0, 0); M = -1 -> (-1, -1):
    the divisor tracks the phase, not the mesh.
 P7 anchor: exact coefficient identities (Fractions/sympy) and the
    50-digit root: |alpha^-1 - 137.0359992168407| < 1e-9, split
    residual < 1e-30.
 P8 mutants CAUGHT: (MUT-A) wrong twist normalisation e^{2 i theta}
    in BOTH cycles -> the moduli map is the degree-4 (2,2)-cover ->
    FHS = 4 != 1; (MUT-B) a squeezed non-unitary kernel insertion
    (I + eps S), eps = 0.05, S = diag(cos(0.7(k+1))) -> the divisor
    integrality breaks (max integer deviation > 1e-6) AND the
    Quillen norm identity breaks (residual > 1e-4): a non-Gaussian-
    consistent overlap kernel cannot fake the (b)-side.
EXPECTED VERDICT: CHAIN_SHADOW_OK.

SMOKE-RUN DISCLOSURE (2026-08-27, ONE declared smoke run before the
freeze, 16/18 in 1.7 s; the two smoke fails were BOTH the MUT-A
expected value, corrected here and disclosed -- recording the
surprises is part of the method):
 (i)   MUT-A ARITHMETIC SLIP, corrected pre-freeze: the plan
       expected FHS = 2 for the e^{2 i theta} mutant, but doubling
       the twist in BOTH cycles is the (2,2)-cover of the moduli
       torus, degree 4, so the pullback Chern is 4 x 1 = 4 -- the
       smoke measured +4.000000000 exactly and the frozen gate now
       demands 4 (still CAUGHT: != 1); G60 failed only downstream
       of this;
 (ii)  the vortex census is NOT minimal for ref1: THREE cells with
       charges (-1 near (pi,pi), +1 near (pi,0), +1 near (0,pi)),
       net +1 -- extra +/- structure is legitimate for a section;
       ref2 has ONE cell (+1 near (0,0), its antipode's twin); the
       two vortex sets are cleanly disjoint, so the patching
       battery runs at full strength;
 (iii) the integer deviations came out at 2e-16 and the difference-
       form total at 3e-16, far inside the frozen bars (1e-9 /
       1e-8); min|s| on the grid 4.3e-3 / 5.9e-3;
 (iv)  MUT-B fires at 2.9e-6 integrality (bar 1e-6, a thin but
       deterministic 2.9x margin -- disclosed) and 1.05e-1 norm
       identity (bar 1e-4, four decades of margin).
No bar, grid, reference twist, mutant recipe or verdict enum moved
after the freeze except the disclosed MUT-A expected-value
correction (2 -> 4); the record runs are the run1/run2 logs.

WHAT THE CHAIN BUYS (L4, printed as a typed statement): with L1
verified at the finite shadow and L2 typed on the named premise,
the open content of ALPHA.QUILLEN.EXACT.01 decomposes with NO
additional analytic unknown: {SEAM.RP.RIGIDITY premise (S1 probe)}
+ {the diagonal-zeta face, v484/v485's remaining [O] = the
SEAM.EQUIV.01 typing (S-parallel probe seam_bfk_conical_det_probe)}
+ {EM1 (laughlin_pump_em1_probe)}.

HONEST LIMITATIONS: this is the FINITE shadow -- a 2-band lattice
Gaussian family, not the abstract-seam zeta determinant; L2 is a
TYPED implication whose premise is NOT proven here (the parallel S1
probe MEASURES rigidity, it does not prove it); the difference
field is exhibited as an exact lattice coboundary, its continuum
identification with the Bismut-Freed local anomaly stays [O]; the
choice of reference frames is a patching convenience, gauge-
invariance of every gated object is by construction (moduli of
dets, det-ratio transitions); ALPHA.QUILLEN.EXACT.01 stays [O],
alpha^-1 = 137.0359992168 stays [E] regardless; nothing moves on
the ledger.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; L1
battery G10-G19 (Bloch integers, twist FHS both sizes, Quillen norm
identity, divisor integrality + pointwise exact form, (b)-integrals
+ difference-form total, localization, patching, controls); L2 G20
typed conditional; L3 G30-G31 exact anchor; L4 G40 DAG; mutants
G50-G51; G60 verdict + G99 runtime.  18 gates.

DETERMINISM: no RNG anywhere; pure numpy eigh / dets + sympy +
mpmath; two record runs must be byte-identical except lines
carrying 'WALL'.  Runtime bar 180 s.

VERDICT ENUM: CHAIN_SHADOW_OK / SHADOW_FAILS / PATCHING_OBSTRUCTED.
"""

from __future__ import annotations

import ast
import hashlib
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

# ---------------------------------------------------------------- frozen
L_MAIN, GRID_MAIN = 4, 48
L_CONF, GRID_CONF = 6, 24
GRID_CTRL = 24
GRID_MUTA = 16
GRID_BLOCH = 24
REF1_TH = (0.0, 0.0)
REF2_TH = (np.pi, np.pi)
TOL_CHERN = 1e-9              # FHS integer bar
TOL_NORMID = 1e-12            # Quillen norm identity, absolute
TOL_INT = 1e-9                # divisor integer deviation
TOL_EXFORM = 1e-8             # difference-form total (spec bar)
TOL_PTWISE = 1e-9             # pointwise F - 2 pi n + W
GAP_BAR = 1.9
VORTEX_MAX_CELLS = 3
LOC_CHEB = 1                  # localization Chebyshev distance (cells)
MUTB_EPS = 0.05
MUTB_INT_BAR = 1e-6           # MUT-B integrality catch bar
MUTB_NORM_BAR = 1e-4          # MUT-B norm-identity catch bar
ROOT_BAR = 1e-9
SPLIT_BAR = mp.mpf("1e-30")
RUNTIME_BAR = 180.0

RIGIDITY_PREMISE = "SEAM.RP.RIGIDITY"
PARALLEL_PROBES = ("seam_rp_rigidity_probe",
                   "seam_bfk_conical_det_probe",
                   "laughlin_pump_em1_probe")

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
TX = (-SZ - 1j * SX) / 2       # v472 verbatim real-space hoppings
TY = (-SZ - 1j * SY) / 2

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import) else [node.module or ""])
            for m in mods:
                root = m.split(".")[0]
                if root in ("verification", "tfpt_constants", "random",
                            "subprocess"):
                    bad.append("forbidden import %s @%d" % (m, node.lineno))
        if isinstance(node, ast.Attribute) and node.attr in ("random",
                                                             "seed"):
            bad.append("RNG attribute @%d" % node.lineno)
    return (not bad), ("; ".join(bad) if bad else
                       "no verification/ or tfpt_constants import, no RNG, "
                       "no subprocess; standalone experiments/-level probe; "
                       "writes nothing but stdout")


# ---------------------------------------------------- model (v472 verbatim)
def hamiltonian(L: int, M: float, thx: float, thy: float,
                twist_pow: int = 1) -> np.ndarray:
    n = L * L
    H = np.zeros((2 * n, 2 * n), complex)

    def blk(x, y):
        return 2 * ((x % L) + L * (y % L))

    for x in range(L):
        for y in range(L):
            i = blk(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            for (dx, dy, T, th) in ((1, 0, TX, thx), (0, 1, TY, thy)):
                j = blk(x + dx, y + dy)
                phase = (np.exp(1j * twist_pow * th)
                         if (x + dx == L or y + dy == L) else 1.0)
                H[j:j + 2, i:i + 2] += phase * T
                H[i:i + 2, j:j + 2] += np.conj(phase) * T.conj().T
    return H


def occupied_frame(L: int, M: float, thx: float, thy: float,
                   twist_pow: int = 1):
    w, v = np.linalg.eigh(hamiltonian(L, M, thx, thy, twist_pow))
    n_occ = int(np.sum(w < 0))
    return v[:, :n_occ], n_occ, float(w[n_occ] - w[n_occ - 1])


def bloch_chern(M: float, N: int = GRID_BLOCH) -> float:
    def occ(kx, ky):
        d = np.array([np.sin(kx), np.sin(ky), M - np.cos(kx) - np.cos(ky)])
        _, v = np.linalg.eigh(d[0] * SX + d[1] * SY + d[2] * SZ)
        return v[:, 0]

    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    u = [[occ(kx, ky) for ky in ks] for kx in ks]

    def ln(a, b):
        x = np.vdot(a, b)
        return x / abs(x)

    F = 0.0
    for i in range(N):
        for j in range(N):
            ip, jp = (i + 1) % N, (j + 1) % N
            F += np.angle(ln(u[i][j], u[ip][j]) * ln(u[ip][j], u[ip][jp])
                          * np.conj(ln(u[i][jp], u[ip][jp]))
                          * np.conj(ln(u[i][j], u[i][jp])))
    return F / (2 * np.pi)


# --------------------------------------------- twist-torus grid machinery
def build_grid(L: int, M: float, G: int, twist_pow: int = 1):
    """Frames on the offset twist grid th_i = 2 pi (i + 1/2) / G.
    Returns (frames[G,G] object array, min_gap); asserts constant n_occ."""
    ths = 2 * np.pi * (np.arange(G) + 0.5) / G
    frames = np.empty((G, G), object)
    min_gap, n_ref = np.inf, None
    for i, tx in enumerate(ths):
        for j, ty in enumerate(ths):
            fr, n_occ, gap = occupied_frame(L, M, tx, ty, twist_pow)
            frames[i, j] = fr
            min_gap = min(min_gap, gap)
            n_ref = n_occ if n_ref is None else n_ref
            assert n_occ == n_ref, "occupation jumped on the twist torus"
    return frames, float(min_gap)


def link_fields(frames: np.ndarray, G: int):
    """Raw det-overlap links Lx[i,j] = det(U(i,j)^dag U(i+1,j)), Ly ditto."""
    lx = np.empty((G, G), complex)
    ly = np.empty((G, G), complex)
    for i in range(G):
        for j in range(G):
            lx[i, j] = np.linalg.det(
                frames[i, j].conj().T @ frames[(i + 1) % G, j])
            ly[i, j] = np.linalg.det(
                frames[i, j].conj().T @ frames[i, (j + 1) % G])
    return lx, ly


def fhs_field(lx: np.ndarray, ly: np.ndarray) -> np.ndarray:
    """FHS plaquette field F(p) in (-pi, pi]."""
    return np.angle(lx * np.roll(ly, -1, axis=0)
                    * np.conj(np.roll(lx, -1, axis=1)) * np.conj(ly))


def section_field(frames: np.ndarray, ref: np.ndarray, G: int) -> np.ndarray:
    """Overlap section s(theta) = det(U_ref^dag U(theta))."""
    s = np.empty((G, G), complex)
    for i in range(G):
        for j in range(G):
            s[i, j] = np.linalg.det(ref.conj().T @ frames[i, j])
    return s


def divisor_field(s: np.ndarray, lx: np.ndarray, ly: np.ndarray,
                  fpl: np.ndarray):
    """Poincare-Lelong divisor: n(p) = (W(p) + F(p)) / 2 pi with W the
    branch-fixed circulation of the covariant link field of s.
    Returns (n int array, max integer deviation, W, max pointwise
    |F - 2 pi n + W|)."""
    ax = np.angle(np.roll(s, -1, axis=0) * np.conj(s) * np.conj(lx))
    ay = np.angle(np.roll(s, -1, axis=1) * np.conj(s) * np.conj(ly))
    W = ax + np.roll(ay, -1, axis=0) - np.roll(ax, -1, axis=1) - ay
    n_raw = (W + fpl) / (2 * np.pi)
    n = np.rint(n_raw)
    dev = float(np.max(np.abs(n_raw - n)))
    ptwise = float(np.max(np.abs(fpl - 2 * np.pi * n + W)))
    return n.astype(int), dev, W, ptwise


def winding_field(t: np.ndarray):
    """Plaquette winding of a scalar complex field (branch-fixed)."""
    bx = np.angle(np.roll(t, -1, axis=0) * np.conj(t))
    by = np.angle(np.roll(t, -1, axis=1) * np.conj(t))
    Wt = bx + np.roll(by, -1, axis=0) - np.roll(bx, -1, axis=1) - by
    wt_raw = Wt / (2 * np.pi)
    wt = np.rint(wt_raw)
    return wt.astype(int), float(np.max(np.abs(wt_raw - wt)))


def norm_identity_err(frames: np.ndarray, ref: np.ndarray, s: np.ndarray,
                      G: int, stride: int = 3) -> float:
    """max |  |s|^2 - det(U_ref^dag P U_ref) |  on a subsampled grid."""
    err = 0.0
    for i in range(0, G, stride):
        for j in range(0, G, stride):
            fr = frames[i, j]
            K = ref.conj().T @ (fr @ fr.conj().T) @ ref
            err = max(err, abs(float(np.linalg.det(K).real)
                               - float(abs(s[i, j]) ** 2)))
    return err


def cheb_dist_torus(a, b, G: int) -> int:
    d = 0
    for x, y in zip(a, b):
        dd = abs(x - y) % G
        d = max(d, min(dd, G - dd))
    return int(d)


def vortex_cells(n: np.ndarray):
    return [(int(i), int(j)) for i, j in zip(*np.nonzero(n))]


def naive_laplacian_total(s: np.ndarray) -> float:
    """Telescoping instrument: total FD Laplacian of log N (exact 0)."""
    logN = np.log(np.abs(s) ** 2)
    lap = (np.roll(logN, -1, 0) + np.roll(logN, 1, 0)
           + np.roll(logN, -1, 1) + np.roll(logN, 1, 1) - 4 * logN)
    return float(np.sum(lap)) / (4 * np.pi)


# ------------------------------------------------------------------ main
def main() -> int:
    print("=" * 78)
    print("quillen_rigidity_chain_probe -- ALPHA.QUILLEN.RIGIDITY_CHAIN.01 "
          "(Strategy S9)")
    print("EXPLORATION ONLY (2026-08-27): no promotion, no ledger row, no "
          "marker moved,")
    print("no gate closed or narrowed.   SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    fw_ok, fw_msg = firewall_audit()
    check("G01-firewall", fw_ok, fw_msg)
    check("G02-predefinition", True,
          "frozen BEFORE record runs: L=%d grid %d main / L=%d grid %d "
          "conf / ctrl grid %d; refs (0,0) + (pi,pi); bars Chern %.0e, "
          "norm-id %.0e, integer %.0e, exact-form %.0e, gap %.1f, vortex "
          "<= %d cells, loc Chebyshev <= %d; MUT-B eps %.2f (catch bars "
          "%.0e / %.0e); root bar %.0e, split bar 1e-30; runtime %.0f s; "
          "verdict enum CHAIN_SHADOW_OK / SHADOW_FAILS / "
          "PATCHING_OBSTRUCTED"
          % (L_MAIN, GRID_MAIN, L_CONF, GRID_CONF, GRID_CTRL, TOL_CHERN,
             TOL_NORMID, TOL_INT, TOL_EXFORM, GAP_BAR, VORTEX_MAX_CELLS,
             LOC_CHEB, MUTB_EPS, MUTB_INT_BAR, MUTB_NORM_BAR, ROOT_BAR,
             RUNTIME_BAR))

    # ---------------------------------------------------------------- L1
    section("L1  QUILLEN'S IDENTITY AT THE FINITE SHADOW "
            "(both curvature readings on the twist torus)")

    c_bz = {M: bloch_chern(M) for M in (1.0, 3.0, -1.0)}
    check("G10-bloch-integers",
          abs(c_bz[1.0] - 1) < TOL_CHERN and abs(c_bz[3.0]) < TOL_CHERN
          and abs(c_bz[-1.0] + 1) < TOL_CHERN,
          "Bloch-BZ FHS Chern C(M=1) = %+.9f, C(M=3) = %+.9f, C(M=-1) = "
          "%+.9f (v470/v367 integers re-derived)"
          % (c_bz[1.0], c_bz[3.0], c_bz[-1.0]))

    frames4, gap4 = build_grid(L_MAIN, 1.0, GRID_MAIN)
    lx4, ly4 = link_fields(frames4, GRID_MAIN)
    fpl4 = fhs_field(lx4, ly4)
    c4 = float(np.sum(fpl4)) / (2 * np.pi)

    frames6, gap6 = build_grid(L_CONF, 1.0, GRID_CONF)
    lx6, ly6 = link_fields(frames6, GRID_CONF)
    fpl6 = fhs_field(lx6, ly6)
    c6 = float(np.sum(fpl6)) / (2 * np.pi)

    check("G11-twist-fhs-both-sizes",
          abs(c4 - 1) < TOL_CHERN and abs(c6 - 1) < TOL_CHERN
          and gap4 > GAP_BAR and gap6 > GAP_BAR,
          "side (a), the Berry integral: C_detline(L=4, grid 48) = "
          "%+.12f, C_detline(L=6, grid 24) = %+.12f (FHS integer 1, "
          "size-independent); Fermi gap open over the WHOLE torus "
          "(min %.3f / %.3f > %.1f) -- section family globally defined"
          % (c4, c6, gap4, gap6, GAP_BAR))

    ref1 = occupied_frame(L_MAIN, 1.0, *REF1_TH)[0]
    ref2 = occupied_frame(L_MAIN, 1.0, *REF2_TH)[0]
    s1 = section_field(frames4, ref1, GRID_MAIN)
    s2 = section_field(frames4, ref2, GRID_MAIN)
    ref6 = occupied_frame(L_CONF, 1.0, *REF1_TH)[0]
    s6 = section_field(frames6, ref6, GRID_CONF)

    err_n1 = norm_identity_err(frames4, ref1, s1, GRID_MAIN)
    err_n2 = norm_identity_err(frames4, ref2, s2, GRID_MAIN)
    check("G12-quillen-norm-identity",
          err_n1 < TOL_NORMID and err_n2 < TOL_NORMID,
          "||s||^2 = |det(U_ref^dag U)|^2 == det(U_ref^dag P U_ref) "
          "(Gaussian covariance kernel) pointwise: max |diff| = %.2e / "
          "%.2e (refs 1/2) < %.0e -- the metric IS the determinant of "
          "the quasi-free overlap kernel (finite ||det||^2 = det)"
          % (err_n1, err_n2, TOL_NORMID))

    n1, dev1, W1, pt1 = divisor_field(s1, lx4, ly4, fpl4)
    n2, dev2, W2, pt2 = divisor_field(s2, lx4, ly4, fpl4)
    n6, dev6, W6, pt6 = divisor_field(s6, lx6, ly6, fpl6)
    check("G13-divisor-integrality-exact-form",
          max(dev1, dev2, dev6) < TOL_INT
          and max(pt1, pt2, pt6) < TOL_PTWISE,
          "Poincare-Lelong bookkeeping: n(p) integer to %.1e (max dev, "
          "all refs/sizes); pointwise F(p) - 2 pi n(p) + W(p) = 0 to "
          "%.1e -- the difference field between the two curvature "
          "readings IS the coboundary of the gauge-invariant link "
          "1-form (the finite 'local anomaly term', an exact form)"
          % (max(dev1, dev2, dev6), max(pt1, pt2, pt6)))

    sum1, sum2, sum6 = int(np.sum(n1)), int(np.sum(n2)), int(np.sum(n6))
    exform1 = abs(c4 - sum1)
    exform2 = abs(c4 - sum2)
    exform6 = abs(c6 - sum6)
    lap_tot = naive_laplacian_total(s1)
    info("naive smeared FD-Laplacian total of log N (ref1): %.3e -- "
         "identically 0 by telescoping (divisor deltas cancel the smooth "
         "part), the reason the divisor is the correct finite (b)-integral"
         % lap_tot)
    check("G14-b-integral-equals-chern",
          sum1 == 1 and sum2 == 1 and sum6 == 1
          and max(exform1, exform2, exform6) < TOL_EXFORM,
          "side (b), the Quillen-metric integral (distributional "
          "(i/2 pi) ddbar log||s||^2 = divisor mass): sum n = %+d / %+d "
          "/ %+d (ref1 / ref2 / L=6) == 1 == C_FHS; difference-form "
          "total |C_float - sum n| = %.2e / %.2e / %.2e < %.0e"
          % (sum1, sum2, sum6, exform1, exform2, exform6, TOL_EXFORM))

    v1 = vortex_cells(n1)
    v2 = vortex_cells(n2)
    amin1 = np.unravel_index(int(np.argmin(np.abs(s1))), s1.shape)
    amin2 = np.unravel_index(int(np.argmin(np.abs(s2))), s2.shape)
    loc1 = min((cheb_dist_torus(amin1, c, GRID_MAIN) for c in v1),
               default=99)
    loc2 = min((cheb_dist_torus(amin2, c, GRID_MAIN) for c in v2),
               default=99)
    th_of = lambda c: tuple(round(2 * np.pi * (x + 0.5) / GRID_MAIN, 3)
                            for x in c)
    check("G15-vortex-localization",
          0 < len(v1) <= VORTEX_MAX_CELLS and 0 < len(v2) <= VORTEX_MAX_CELLS
          and loc1 <= LOC_CHEB and loc2 <= LOC_CHEB,
          "the degree-1 bundle FORCES section zeros and the metric finds "
          "them: vortex cells ref1 %s (charges %s, twist ~%s), ref2 %s "
          "(charges %s, twist ~%s); |s| grid-argmin sits at Chebyshev "
          "distance %d / %d (<= %d) from a vortex cell; min|s| = %.2e / "
          "%.2e"
          % (v1, [int(n1[c]) for c in v1], th_of(v1[0]) if v1 else "-",
             v2, [int(n2[c]) for c in v2], th_of(v2[0]) if v2 else "-",
             loc1, loc2, LOC_CHEB,
             float(np.min(np.abs(s1))), float(np.min(np.abs(s2)))))

    t12 = s1 * np.conj(s2)      # arg t12 = arg(s1/s2), gauge-invariant
    wt, devt = winding_field(t12)
    disjoint = not (set(v1) & set(v2))
    ptwise_trans = bool(np.all(wt == n1 - n2))
    wind_total = int(np.sum(wt))
    c_via_s2 = -int(sum(wt[c] for c in v2))
    c_via_s1 = int(sum(wt[c] for c in v1))
    check("G16-patching-transition-winding",
          disjoint and ptwise_trans and wind_total == 0
          and devt < TOL_INT and c_via_s2 == 1 and c_via_s1 == 1,
          "two-patch Dai-Freed picture: vortex sets DISJOINT; transition "
          "t12 = s1/s2 gauge-invariant with wt(p) == n1(p) - n2(p) at "
          "EVERY plaquette (max int dev %.1e); total winding %d == 0; "
          "winding of the transition function around the s2 zeros = %+d "
          "== C == 1 (and around the s1 zeros = %+d) -- the Chern number "
          "IS the transition winding"
          % (devt, wind_total, c_via_s2, c_via_s1))

    ctrl = {}
    for M in (3.0, -1.0):
        fr, _g = build_grid(L_MAIN, M, GRID_CTRL)
        lx, ly = link_fields(fr, GRID_CTRL)
        fpl = fhs_field(lx, ly)
        refc = occupied_frame(L_MAIN, M, *REF1_TH)[0]
        sc = section_field(fr, refc, GRID_CTRL)
        nc, devc, _wc, _pc = divisor_field(sc, lx, ly, fpl)
        ctrl[M] = (float(np.sum(fpl)) / (2 * np.pi), int(np.sum(nc)), devc)
    check("G17-controls-track-the-phase",
          abs(ctrl[3.0][0]) < TOL_CHERN and ctrl[3.0][1] == 0
          and abs(ctrl[-1.0][0] + 1) < TOL_CHERN and ctrl[-1.0][1] == -1
          and max(ctrl[3.0][2], ctrl[-1.0][2]) < TOL_INT,
          "trivial collar M = 3: (C_FHS, divisor) = (%+.9f, %+d); "
          "orientation flip M = -1: (%+.9f, %+d) -- BOTH curvature "
          "readings track the phase, not the mesh"
          % (ctrl[3.0][0], ctrl[3.0][1], ctrl[-1.0][0], ctrl[-1.0][1]))

    # ---------------------------------------------------------------- L2
    section("L2  THE CONDITIONAL (typed, premise NAMED -- not a numeric "
            "gate)")
    check("G20-typed-conditional", True,
          "TYPED IMPLICATION [C], premise NOT assumed: IF the seam state "
          "is QUASI-FREE (premise %s -- the rigidity target of the "
          "parallel S1 probe %s.py; v903 terrain: OS positivity <=> "
          "a_J = 0 on the deployed family) THEN the seam determinant "
          "line is a free-fermion determinant line and L1's identity "
          "applies LITERALLY (||det||^2 = det of the Gaussian kernel, "
          "divisor = index form + exact anomaly term) -- the premise "
          "stays [O], typed here, closed nowhere"
          % (RIGIDITY_PREMISE, PARALLEL_PROBES[0]))

    # ---------------------------------------------------------------- L3
    section("L3  THE VALUE-LEVEL ANCHOR (exact, closed regardless)")
    b1 = Fraction(41, 10)
    coeff_ok = (8 * b1 == Fraction(164, 5) == Fraction(4, 5) * 41
                and 10 * b1 == 41)
    c3s = 1 / (8 * sp.pi)
    sym_ok = (sp.simplify(sp.Rational(1, 6) / sp.pi
                          - sp.Rational(4, 3) * c3s) == 0
              and sp.Rational(5, 4) + sp.Rational(3, 4) == 2)
    check("G30-exact-coefficients", coeff_ok and sym_ok,
          "exact Fractions/sympy: 8 b1 = 8*(41/10) = 164/5 = (4/5)*41 "
          "(the U(1) index, v48); c3 = 1/(8 pi) (Gauss-Bonnet, v216); "
          "phi_base = 1/(6 pi) = (4/3) c3; q(D5) + q(A3) = 5/4 + 3/4 = 2 "
          "(E8 root norm, v1/v154)")

    mp.mp.dps = 50
    cc = 1 / (8 * mp.pi)
    pb = 1 / (6 * mp.pi)
    dt = 48 * cc ** 4

    def phiseam(a):
        Q = dt * mp.e ** (-2 * a)
        return pb + Q * (1 - Q) ** (mp.mpf(-5) / 4)

    def F_alpha(a):
        return (a ** 3 - 2 * cc ** 3 * a ** 2
                - (mp.mpf(4) / 5) * 41 * cc ** 6 * mp.log(1 / phiseam(a)))

    a_root = mp.findroot(F_alpha, mp.mpf("0.0073"))
    ainv = 1 / a_root
    lhs = a_root ** 3 - 2 * cc ** 3 * a_root ** 2
    rhs = (8 * mp.mpf(41) / 10) * cc ** 6 * mp.log(1 / phiseam(a_root))
    resid = abs(lhs - rhs)
    check("G31-quillen-split-at-the-root",
          abs(ainv - mp.mpf("137.0359992168407")) < ROOT_BAR
          and resid < SPLIT_BAR,
          "a^3 - 2 c3^3 a^2 = 8 b1 c3^6 ln(1/phi_seam) at alpha^-1 = "
          "%s (bar %.0e vs 137.0359992168407); split residual "
          "|lhs - rhs| = %s < 1e-30 (mpmath dps 50) -- the anchor that "
          "stays closed [E] regardless of the chain"
          % (mp.nstr(ainv, 17), ROOT_BAR, mp.nstr(resid, 3)))

    # ---------------------------------------------------------------- L4
    section("L4  WHAT THE CHAIN BUYS (typed DAG statement)")
    check("G40-dag-no-new-analytic-unknown", True,
          "TYPED [C]: with L1 verified at the finite shadow and L2 "
          "conditional on %s, the remaining open content of "
          "ALPHA.QUILLEN.EXACT.01 is EXACTLY {the rigidity premise "
          "(probe %s)} + {the diagonal-zeta face = the v484/v485 "
          "residual, = the SEAM.EQUIV.01 typing (probe %s)} + {EM1 "
          "(probe %s)} -- NO additional analytic unknown; the target "
          "stays [O], nothing closes or narrows here"
          % (RIGIDITY_PREMISE, PARALLEL_PROBES[0], PARALLEL_PROBES[1],
             PARALLEL_PROBES[2]))

    # ------------------------------------------------------------ mutants
    section("S5  MUTANTS (both must be CAUGHT)")
    fr_a, _ = build_grid(L_MAIN, 1.0, GRID_MUTA, twist_pow=2)
    lx_a, ly_a = link_fields(fr_a, GRID_MUTA)
    c_muta = float(np.sum(fhs_field(lx_a, ly_a))) / (2 * np.pi)
    check("G50-mutant-twist-normalisation",
          abs(c_muta - 4) < 1e-6 and abs(c_muta - 1) > 0.5,
          "CAUGHT: wrong twist normalisation e^{2 i theta} in both cycles "
          "pulls back along the degree-4 (2,2)-cover of the moduli torus "
          "-> FHS = %+.9f = 4 != 1 (the twist-torus integer is NOT "
          "convention-proof; the correct normalisation is load-bearing; "
          "expected value 2 -> 4 corrected at smoke, disclosed)" % c_muta)

    S_sq = np.diag(np.cos(0.7 * (np.arange(2 * L_MAIN * L_MAIN) + 1)))
    ins = np.eye(2 * L_MAIN * L_MAIN) + MUTB_EPS * S_sq
    G = GRID_MAIN
    lx_m = np.empty((G, G), complex)
    ly_m = np.empty((G, G), complex)
    for i in range(G):
        for j in range(G):
            lx_m[i, j] = np.linalg.det(
                frames4[i, j].conj().T @ ins @ frames4[(i + 1) % G, j])
            ly_m[i, j] = np.linalg.det(
                frames4[i, j].conj().T @ ins @ frames4[i, (j + 1) % G])
    _nm, dev_m, _wm, _pm = divisor_field(s1, lx_m, ly_m, fpl4)
    s_sq = np.empty((G, G), complex)
    for i in range(0, G, 3):
        for j in range(0, G, 3):
            s_sq[i, j] = np.linalg.det(ref1.conj().T @ ins @ frames4[i, j])
    err_sq = 0.0
    for i in range(0, G, 3):
        for j in range(0, G, 3):
            fr = frames4[i, j]
            K = ref1.conj().T @ (fr @ fr.conj().T) @ ref1
            err_sq = max(err_sq, abs(float(np.linalg.det(K).real)
                                     - float(abs(s_sq[i, j]) ** 2)))
    check("G51-mutant-squeezed-kernel",
          dev_m > MUTB_INT_BAR and err_sq > MUTB_NORM_BAR,
          "CAUGHT twice: squeezed non-unitary kernel insertion "
          "(I + %.2f S) breaks (i) the divisor integrality (max integer "
          "deviation %.2e > %.0e -- the (b)-side bookkeeping REFUSES a "
          "non-Gaussian-consistent transport kernel) and (ii) the "
          "Quillen norm identity (residual %.2e > %.0e -- ||det||^2 = "
          "det holds ONLY for the quasi-free kernel)"
          % (MUTB_EPS, dev_m, MUTB_INT_BAR, err_sq, MUTB_NORM_BAR))

    # ------------------------------------------------------------ verdict
    section("S6  VERDICT")
    npass_pre = sum(1 for _n, ok, _d in CHECKS if ok)
    all_pre = npass_pre == len(CHECKS)
    patching_ok = disjoint and ptwise_trans
    if all_pre:
        verdict = "CHAIN_SHADOW_OK"
    elif not patching_ok:
        verdict = "PATCHING_OBSTRUCTED"
    else:
        verdict = "SHADOW_FAILS"
    check("G60-verdict", all_pre,
          "%s: L1 both curvature readings = 1 on the twist torus with "
          "the difference an exact form (Quillen's identity at the "
          "finite shadow, incl. patching + controls + norm identity); "
          "L2 typed on %s; L3 anchor exact at 50 digits; L4 DAG: no new "
          "analytic unknown; both mutants CAUGHT"
          % (verdict, RIGIDITY_PREMISE))

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    if npass == len(CHECKS):
        print("ALL GATES PASSED %d/%d" % (npass, len(CHECKS)))
    else:
        print("GATES: %d/%d PASS -- FAILURES:" % (npass, len(CHECKS)))
        for nm, ok, _d in CHECKS:
            if not ok:
                print("  FAIL " + nm)
    print("VERDICT: %s" % verdict)
    print("KEY NUMBERS: FHS integer = 1 (C_detline L=4 %.12f, L=6 %.12f); "
          "Berry integral %.12f; Quillen-metric (divisor) integral %+d / "
          "%+d / %+d; difference-form integral %.2e (bar 1e-8); "
          "alpha-root inverse %s, split residual %s"
          % (c4, c6, c4, sum1, sum2, sum6,
             max(exform1, exform2, exform6), mp.nstr(ainv, 14),
             mp.nstr(resid, 3)))
    print("EXPLORATION ONLY: no promotion, no ledger row, no marker "
          "moved, no gate closed or narrowed.")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
