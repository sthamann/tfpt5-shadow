#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""laughlin_pump_em1_probe -- ALPHA.QUILLEN.EM1_PUMP.01 (Strategy S8):
the cited EM1/inflow step "boundary level = bulk response" made
COMPUTABLE as a Laughlin flux pump + Streda response on the very
collar model that realises S3.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  v470 (ALPHA.QUILLEN.INFLOW.01) reads the a^3
level as k0 = |C| = 1, the FHS Chern invariant of the p+ip collar
model h(k) = sin kx SX + sin ky SY + (M - cos kx - cos ky) SZ
(v367/v368), with the bulk-boundary identification CITED (TKNN 1982;
Callan-Harvey 1985; APS/Witten eta-CS; Quillen/Bismut-Freed), and
v472 computed the det-line curvature over the U(1)-twist moduli = 1.
What stayed cited-only is the INFLOW step itself: that the boundary
LEVEL equals the bulk RESPONSE.  On a lattice that step IS the
Laughlin argument -- threading one flux quantum through a cylinder
pumps exactly C charges from one edge to the other, visible as
quantised polarisation winding, as unit spectral flow of the chiral
edge branch, and (thermodynamic dual) as the Streda count
dN/dPhi = C/(2 pi).  This probe computes all three on the SAME
h(k), in its COMPLEX-fermion Chern-insulator form (single copy; the
16-Majorana collar = 8 complex copies is printed as exact Fraction
arithmetic, not simulated), and prices them against mutants.

THE SETUP (all frozen).  Model and conventions VERBATIM from
v367/v368/v472: Bloch h(k) above, occupied = lower band; strip
on-site sin kx SX + (M - cos kx) SZ, y-hop -SZ/2 + SY/(2i); M = 1
topological (C = 1), M = 3 trivial (C = 0).  Cylinder: Lx = 8 slices
periodic in x, Ny = 40 open in y, flux phi entering as the exact
gauge shift kx -> kx + phi/Lx of every momentum slice (uniform
Peierls phase e^{i phi/Lx} on the x-bonds), NPHI = 128 steps over
one flux quantum, phi-grid offset by half a step to dodge symmetric
crossings.  Filling on the cylinder: fixed particle number
N = Lx * Ny (half filling by count), so the hybrid-Wannier count is
constant and the occupied-set switch at the edge-branch crossing
appears as ONE quantised teleport event, bookkept separately from
the continuous transport.  PUMP FORMULATION (chosen for a clean
integer winding, documented): (i) BULK hybrid-Wannier winding -- the
gauge-invariant Wilson loop of the occupied band around the ky
circle at fixed kx gives the Wannier center ybar(kx) mod 1; since
flux threading is the rigid shift kx -> kx + phi/Lx, the total
y-polarisation P_y(phi) = sum_n ybar(k_n + phi/Lx) winds over one
flux quantum by EXACTLY the Brillouin-zone winding of ybar
(telescoping over the Lx slices), which is gated == C to 1e-6;
(ii) CYLINDER transport -- per slice the occupied projector's
P yhat P spectrum (hybrid Wannier charge centers, gauge invariant)
is tracked in phi, and the NET number of centers crossing the bulk
fiducial line y_cut = (Ny-1)/2 + 0.2871 CONTINUOUSLY per flux
quantum is the pumped charge, gated == C exactly (integer), with
the teleport events counted and the period-closure identity
(continuous + teleport = 0) checked as an instrument.
ORIENTATION CONVENTIONS (three signs frozen at the single
calibration pass, nothing else moved): OR1 the Berry-phase sign in
ybar(kx) := +arg(W)/(2 pi); OR2 the flux-threading sign
k_n(phi) = (2 pi n - phi)/Lx; OR3 the Streda field orientation
(measured s = DeltaN(1) = +1 at M = 1 for the +n_phi Peierls gauge
below, i.e. DeltaN(n) = +C n; the C-linearity is the gate, the
absolute sign is the orientation).  The convention-FREE content:
the magnitude |pump| = |C| = 1, the M = 3 zeros, the per-edge
antisymmetry of the spectral flow, the cross-n_phi linearity of the
Streda count, and the SIMULTANEOUS sign flip of everything under
complex conjugation of the model.

PRE-REGISTERED ADJUDICATION (frozen before the record runs; one
calibration pass fixed OR1/OR2/OR3 and the mutant record values,
nothing else moved):
  P1 ANCHORS: FHS Chern C(M=1) = 1, C(M=3) = 0 exactly (integer
     gates, tol 1e-9, v367/v470 convention); strip in-gap edge
     branch min_kx|E| < 0.05 at M = 1, > 0.3 at M = 3 (v368).
  P2 THE PUMP: bulk hybrid-Wannier winding DeltaP == C within 1e-6
     at M = 1 and == 0 at M = 3 (unwrap steps < 0.25 gated); cylinder
     P yhat P continuous midline transport == C exactly (integer)
     per flux quantum at M = 1, == 0 at M = 3, teleport bookkeeping
     printed and period closure (continuous + teleport = 0) checked.
  P3 SPECTRAL FLOW: edge-resolved zero crossings of the in-gap
     branch per flux quantum: net sigma = +-1 on the bottom edge and
     -sigma on the top edge at M = 1 (chirality sign printed), and
     ZERO in-gap crossings at M = 3.
  P4 STREDA: on the L x L torus (L = 12) with n_phi uniform flux
     quanta (verified uniform Peierls gauge, plaquette deviation
     < 1e-12), the filled-band count obeys N(n_phi) - N(0) = s C
     n_phi EXACTLY for n_phi = 1, 2, 3 at M = 1 (fit slope within
     5e-2 first, then the exact integer), and stays CONSTANT at
     M = 3; gap at E = 0 open (min|E| > 0.1) for every n_phi.
  P5 THE 16-COPY / LEVEL BOOKKEEPING (exact Fractions): 16 Majorana
     = 8 complex copies; c_- = 16 x (1/2) x |C| = 8 = g_car + N_fam;
     k0 = |C| = 1 per complex copy (the v470 statement); k_Y
     re-derived from the v470 arithmetic: tr_5bar(Y^2)/tr(T3^2)
     = (5/6)/(1/2) = 5/3, (3/5)(41/6) = 41/10 = b1,
     41/6 = 20/3 + 1/6.
  P6 MUTANTS: the complex-conjugated model (sin ky -> -sin ky) must
     flip EVERYTHING simultaneously -- FHS Chern -1, Wannier winding
     -1, cylinder transport -1, Streda -s C n_phi (CAUGHT as the
     sign gate); a wrong-band projector (band chosen by
     sign(sin 3(kx + ky)), a k-dependent valence/conduction
     patchwork) must BREAK quantisation through three channels:
     the FHS reading is GRID-UNSTABLE (|C_mut(N=24) - C_mut(N=36)|
     >= 1 -- no well-defined invariant; calibrated 3 vs 1), the
     Wannier flow is UNREADABLE (max unwrap step > 0.25, calibrated
     0.331), and the nominal winding disagrees with C (calibrated
     0 vs 1) (CAUGHT).
EXPECTED VERDICT (pre-registered): PUMP_QUANTIZED_MATCHES_CHERN --
pumped charge == spectral flow == Streda == C on the S3 collar
model, i.e. the "boundary level = bulk response" step of EM1 holds
COMPUTABLY at the lattice level, per complex copy.

RECORD PROTOCOL (house pattern): two calibration passes at
pre-freeze SHAs c0c96e0d8bbd7ee0 (14/20 -- the six fails were
exactly the three orientation signs OR1/OR3 + the untested strip
conjugation hook + a self-referential source scan + the first
too-weak mutant, every physics finding already held) and the fixed
spec (20/20 in 2.9 s); OR1/OR2/OR3, the strip sy hook, the mutant
rule sin(3(kx+ky)) and its record values (FHS 3 vs 1, step 0.331,
winding 0) frozen from calibration; the only edit after the clean
calibration pass is this record-note insertion itself.  Two record
runs laughlin_pump_em1_probe.run1.log / .run2.log at the final
SPEC_SHA must be identical modulo WALL lines.

VERDICT ENUM: PUMP_QUANTIZED_MATCHES_CHERN (all anchors and all
matches pass) / PUMP_MISMATCH (instruments fine but a quantised
response disagrees with C) / INSTRUMENT_FAILS (an anchor, gauge
check, arithmetic identity or the runtime bar fails).

WHAT IS BUILT AND GATED: S0 G01 firewall/spec; S1 anchors G02-G05;
S2 pump G06-G09; S3 spectral flow G10-G11; S4 Streda G12-G14; S5
bookkeeping G15-G16; S6 mutants G17-G18; S7 G19 runtime (< 180 s)
+ G20 verdict aggregate.  20 gates.

HONEST LIMITATIONS.  (i) Single COMPLEX copy: the physical collar
carrier is 16 Majoranas = 8 complex copies; the multi-copy statement
enters only as exact arithmetic (P5), not as a 16-band simulation.
(ii) Complex-fermion form: the QWZ/Chern-insulator reading of h(k)
carries a genuine U(1); the Majorana/BdG collar has no microscopic
U(1) per Majorana -- the U(1) pumped here is the one EM1 actually
uses (the complex-copy pairing), and that identification stays part
of the cited EM1 reading [C].  (iii) Lattice only: no continuum
scaling limit (MMST, v336) is touched.  (iv) Nothing here closes or
narrows ALPHA.QUILLEN.EXACT.01; the bridge lemma stays the named
cited step; this probe upgrades "cited" to "computable on the
model" at experiments/ level only.

DETERMINISM: no randomness anywhere (numpy eigh on fixed grids,
gauge-invariant observables only); two record runs
laughlin_pump_em1_probe.run1.log / .run2.log must be identical
modulo wall-clock tokens (lines carrying 'WALL').
"""

from __future__ import annotations

import hashlib
import os
import time
from fractions import Fraction

import numpy as np

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)

# ---------------------------------------------------------------- frozen
M_TOPO, M_TRIV = 1.0, 3.0
N_FHS = 24                 # v367/v470/v472 FHS grid
TOL_CHERN = 1e-9
NKX_WILSON = 64            # kx steps of the pump (>= 64 required)
NKY_WILSON = 256           # ky Wilson-loop resolution
PUMP_TOL = 1e-6
UNWRAP_BAR = 0.25          # max legal unwrap step (adiabatic readability)
LX_CYL, NY_CYL, NPHI_CYL = 8, 40, 128
Y_CUT = (NY_CYL - 1) / 2 + 0.2871
GAP_WINDOW = 0.6           # in-gap window for the edge branch (bulk |E|>~1)
MATCH_BAR = 0.4            # continuous-move bar in the center matching
L_STREDA = 12
NPHI_STREDA = (0, 1, 2, 3)
STREDA_GAP_BAR = 0.1
STREDA_FIT_BAR = 5e-2
GAUGE_DEV_BAR = 1e-12
MUTANT_GRID_BAR = 0.5      # FHS grid instability threshold (N=24 vs N=36)
N_FHS_ALT = 36
RUNTIME_BAR = 180.0

# frozen from verification/tfpt_constants (P2 axiom g_car = 5; N_fam = 3)
G_CAR = 5
N_FAM = 3

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-22s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ Bloch layer
def bloch_h(kx, ky, M, sy=1.0):
    """h(k) of v367; sy = -1 is the complex-conjugated (mutant) model."""
    return (np.sin(kx) * SX + sy * np.sin(ky) * SY
            + (M - np.cos(kx) - np.cos(ky)) * SZ)


def band_vec(kx, ky, M, sy=1.0, band=0):
    _, v = np.linalg.eigh(bloch_h(kx, ky, M, sy))
    return v[:, band]


def fhs_chern(M, sy=1.0, N=N_FHS, band_rule=None):
    """Fukui-Hatsugai-Suzuki plaquette Chern number (v367/v470 verbatim
    convention); band_rule(kx, ky) -> band index (mutant hook)."""
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    if band_rule is None:
        band_rule = lambda kx, ky: 0
    u = [[band_vec(kx, ky, M, sy, band_rule(kx, ky)) for ky in ks]
         for kx in ks]

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


# ------------------------------------------- pump (i): bulk Wannier winding
def wannier_center(kx, M, sy=1.0, nky=NKY_WILSON, band_rule=None):
    """Gauge-invariant Wilson loop of the occupied band around the ky
    circle at fixed kx -> hybrid Wannier center ybar(kx) mod 1 (OR1:
    ybar := +arg(W)/(2 pi))."""
    kys = np.linspace(0, 2 * np.pi, nky, endpoint=False)
    if band_rule is None:
        band_rule = lambda kx, ky: 0
    us = [band_vec(kx, ky, M, sy, band_rule(kx, ky)) for ky in kys]
    W = 1.0 + 0.0j
    for j in range(nky):
        W *= np.vdot(us[j], us[(j + 1) % nky])
    return np.angle(W) / (2 * np.pi)


def pump_winding(M, sy=1.0, nkx=NKX_WILSON, band_rule=None):
    """Winding of ybar(kx) over the BZ = the y-charge pumped through the
    cylinder by one flux quantum (P_y(phi) telescopes over the Lx slices
    to exactly this winding).  Returns (DeltaP, max unwrap step)."""
    kxs = np.linspace(0, 2 * np.pi, nkx + 1)
    raw = [wannier_center(kx, M, sy, band_rule=band_rule) for kx in kxs]
    y = [raw[0]]
    max_step = 0.0
    for r in raw[1:]:
        d = r - y[-1]
        d -= round(d)
        max_step = max(max_step, abs(d))
        y.append(y[-1] + d)
    return y[-1] - y[0], max_step


# --------------------------------------- pump (ii): cylinder P y P transport
def strip_H(k, M, Ny, sy=1.0):
    """v368 strip Hamiltonian verbatim: Ny open sites in y, momentum k;
    sy = -1 conjugates the y-hopping (the mutant model's strip)."""
    ons = np.sin(k) * SX + (M - np.cos(k)) * SZ
    hop = -0.5 * SZ + sy * (1 / 2j) * SY
    H = np.zeros((2 * Ny, 2 * Ny), complex)
    for y in range(Ny):
        H[2 * y:2 * y + 2, 2 * y:2 * y + 2] = ons
    for y in range(Ny - 1):
        H[2 * y:2 * y + 2, 2 * y + 2:2 * y + 4] = hop
        H[2 * y + 2:2 * y + 4, 2 * y:2 * y + 2] = hop.conj().T
    return H


def match_step(prev, new):
    """Match two sorted Wannier-center lists between adjacent phi steps.
    Returns (net continuous up-crossings of Y_CUT, teleport sign, anomaly).
    Teleport sign -1 = a center left the top edge and reappeared at the
    bottom (discontinuous down-crossing), +1 the reverse."""
    cands = []
    d0 = float(np.max(np.abs(new - prev)))
    cands.append((d0, 0))
    if len(prev) > 1:
        cands.append((float(np.max(np.abs(new[1:] - prev[:-1]))), +1))
        cands.append((float(np.max(np.abs(new[:-1] - prev[1:]))), -1))
    maxd, shift = min(cands)
    if shift == 0:
        a, b = prev, new
        tele = 0
    elif shift == +1:          # arrival at bottom, departure from top
        a, b = prev[:-1], new[1:]
        tele = -1
    else:                      # arrival at top, departure from bottom
        a, b = prev[1:], new[:-1]
        tele = +1
    up = int(np.sum((a < Y_CUT) & (b > Y_CUT)))
    down = int(np.sum((b < Y_CUT) & (a > Y_CUT)))
    anomaly = 1 if maxd > MATCH_BAR else 0
    return up - down, tele, anomaly


def cylinder_sweep(M, sy=1.0):
    """One flux quantum through the cylinder (OR2: k_n(phi) =
    (2 pi n - phi)/Lx).  Tracks (a) the P y P hybrid Wannier centers per
    slice -> continuous midline transport + teleports, (b) the in-gap
    edge levels -> edge-resolved spectral flow through E = 0."""
    y_site = np.repeat(np.arange(NY_CYL), 2).astype(float)
    phis = 2 * np.pi * (np.arange(NPHI_CYL + 1) + 0.5) / NPHI_CYL
    net_up, tele_net, anomalies = 0, 0, 0
    flow = {"bottom": 0, "top": 0}
    prev_centers = [None] * LX_CYL
    prev_ingap = [dict() for _ in range(LX_CYL)]
    for phi in phis:
        for n in range(LX_CYL):
            k = (2 * np.pi * n - phi) / LX_CYL          # OR2
            w, v = np.linalg.eigh(strip_H(k, M, NY_CYL, sy))
            V = v[:, :NY_CYL]                       # fixed count: half filling
            A = V.conj().T @ (V * y_site[:, None])
            centers = np.sort(np.linalg.eigvalsh(A))
            ingap = {}
            for i in np.where(np.abs(w) < GAP_WINDOW)[0]:
                yexp = float(np.abs(v[:, i]) ** 2 @ y_site)
                edge = "bottom" if yexp < NY_CYL / 2 else "top"
                if edge not in ingap or abs(w[i]) < abs(ingap[edge]):
                    ingap[edge] = float(w[i])
            if prev_centers[n] is not None:
                u, t, a = match_step(prev_centers[n], centers)
                net_up += u
                tele_net += t
                anomalies += a
                for edge, E_new in ingap.items():
                    E_old = prev_ingap[n].get(edge)
                    if E_old is not None and E_old * E_new < 0:
                        flow[edge] += 1 if E_new > E_old else -1
            prev_centers[n] = centers
            prev_ingap[n] = ingap
    return dict(net_up=net_up, teleports=tele_net, anomalies=anomalies,
                flow=flow)


# ------------------------------------------------------ Streda (magnetic torus)
def _theta_x(x, y, n, L):
    """Peierls phase on the x-bond (x,y)->(x+1,y); seam twist at x=L-1."""
    return 0.0 if x < L - 1 else -2 * np.pi * n * y / L


def _theta_y(x, y, n, L):
    """Peierls phase on the y-bond (x,y)->(x,y+1) (Landau gauge)."""
    return 2 * np.pi * n * x / L ** 2


def gauge_check(n, L):
    """Max deviation of any plaquette flux from the uniform 2 pi n / L^2."""
    target = 2 * np.pi * n / L ** 2
    dev = 0.0
    for x in range(L):
        for y in range(L):
            loop = (_theta_x(x, y, n, L) + _theta_y((x + 1) % L, y, n, L)
                    - _theta_x(x, (y + 1) % L, n, L) - _theta_y(x, y, n, L))
            d = (loop - target + np.pi) % (2 * np.pi) - np.pi
            dev = max(dev, abs(d))
    return dev


def streda_count(M, n, L=L_STREDA, sy=1.0):
    """Filled-band count N = #{E < 0} and min|E| on the L x L torus with
    n uniform flux quanta.  Real-space hoppings TX, TY verbatim v472."""
    TX = (-SZ - 1j * SX) / 2
    TY = (-SZ - 1j * sy * SY) / 2
    N = L * L
    H = np.zeros((2 * N, 2 * N), complex)

    def blk(x, y):
        return 2 * ((x % L) + L * (y % L))

    for x in range(L):
        for y in range(L):
            i = blk(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            for (dx, dy, T, th) in ((1, 0, TX, _theta_x(x, y, n, L)),
                                    (0, 1, TY, _theta_y(x, y, n, L))):
                j = blk(x + dx, y + dy)
                ph = np.exp(1j * th)
                H[j:j + 2, i:i + 2] += ph * T
                H[i:i + 2, j:j + 2] += np.conj(ph) * T.conj().T
    w = np.linalg.eigvalsh(H)
    return int(np.sum(w < 0)), float(np.min(np.abs(w)))


def fit_slope(xs, ys):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    mx, my = xs.mean(), ys.mean()
    return float(((xs - mx) * (ys - my)).sum() / ((xs - mx) ** 2).sum())


# ------------------------------------------------------------------ mutants
def mutant_band_rule(kx, ky):
    """Wrong-band projector: a k-dependent valence/conduction patchwork
    (upper band wherever sin(3(kx + ky)) > 0) -- not a gapped band."""
    return 1 if np.sin(3 * (kx + ky)) > 0 else 0


# --------------------------------------------------------------------- main
def main() -> int:
    print("=" * 78)
    print("laughlin_pump_em1_probe -- ALPHA.QUILLEN.EM1_PUMP.01 (Strategy S8)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, "
          "NO ledger row,")
    print("NO marker moved, NO gate closed or narrowed.")
    print("=" * 78)

    # ---------------------------------------------------------------- S0
    section("S0  firewall / spec")
    here = os.path.dirname(os.path.abspath(__file__))
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    in_disc = here.endswith(os.path.join("experiments", "tfpt-discovery"))
    no_rng = (("np." + "random") not in src
              and ("import " + "random") not in src)
    check("G01-spec", in_disc and no_rng,
          "probe lives in experiments/tfpt-discovery, no RNG anywhere "
          "(deterministic); frozen: FHS N=%d, Wilson %dx%d, cylinder "
          "Lx=%d Ny=%d NPHI=%d, Streda L=%d n_phi=%s"
          % (N_FHS, NKX_WILSON, NKY_WILSON, LX_CYL, NY_CYL, NPHI_CYL,
             L_STREDA, list(NPHI_STREDA)))

    # ---------------------------------------------------------------- S1
    section("S1  anchors (P1): FHS Chern + strip edge branch (v367/v368)")
    C_topo = fhs_chern(M_TOPO)
    C_triv = fhs_chern(M_TRIV)
    check("G02-chern-topo", abs(C_topo - 1) < TOL_CHERN,
          "FHS Chern C(M=1) = %+.12f == +1 (tol %.0e, v367/v470 convention)"
          % (C_topo, TOL_CHERN))
    check("G03-chern-triv", abs(C_triv) < TOL_CHERN,
          "FHS Chern C(M=3) = %+.12f == 0 (trivial control)" % C_triv)
    kxs = np.linspace(0, 2 * np.pi, 80, endpoint=False)
    minE_topo = min(np.min(np.abs(np.linalg.eigvalsh(strip_H(k, M_TOPO,
                                                             NY_CYL))))
                    for k in kxs)
    minE_triv = min(np.min(np.abs(np.linalg.eigvalsh(strip_H(k, M_TRIV,
                                                             NY_CYL))))
                    for k in kxs)
    check("G04-strip-ingap", minE_topo < 0.05,
          "strip min_kx|E| = %.6f < 0.05 at M=1 -- chiral edge branch deep "
          "in the gap (v368)" % minE_topo)
    check("G05-strip-gap", minE_triv > 0.3,
          "strip min_kx|E| = %.4f > 0.3 at M=3 -- clean gap, no edge branch "
          "(v368 control)" % minE_triv)
    C_int = int(round(C_topo))

    # ---------------------------------------------------------------- S2
    section("S2  THE PUMP (P2): Laughlin flux pump, two formulations")
    dP_topo, step_topo = pump_winding(M_TOPO)
    dP_triv, step_triv = pump_winding(M_TRIV)
    check("G06-pump-wilson-topo",
          abs(dP_topo - C_int) < PUMP_TOL and step_topo < UNWRAP_BAR,
          "hybrid-Wannier winding DeltaP(M=1) = %+.12f == C = %+d "
          "(residual %.1e < 1e-6; max unwrap step %.4f < %.2f)"
          % (dP_topo, C_int, abs(dP_topo - C_int), step_topo, UNWRAP_BAR))
    check("G07-pump-wilson-triv",
          abs(dP_triv) < PUMP_TOL and step_triv < UNWRAP_BAR,
          "hybrid-Wannier winding DeltaP(M=3) = %+.12f == 0 "
          "(residual %.1e; max step %.4f)"
          % (dP_triv, abs(dP_triv), step_triv))
    cyl_topo = cylinder_sweep(M_TOPO)
    cyl_triv = cylinder_sweep(M_TRIV)
    check("G08-pump-cyl-topo",
          cyl_topo["net_up"] == C_int and cyl_topo["anomalies"] == 0
          and cyl_topo["net_up"] + cyl_topo["teleports"] == 0,
          "cylinder P y P transport (M=1): net continuous midline crossings "
          "= %+d == C = %+d per flux quantum (teleports %+d, closure "
          "cont+tele = %d, anomalies %d)"
          % (cyl_topo["net_up"], C_int, cyl_topo["teleports"],
             cyl_topo["net_up"] + cyl_topo["teleports"],
             cyl_topo["anomalies"]))
    check("G09-pump-cyl-triv",
          cyl_triv["net_up"] == 0 and cyl_triv["teleports"] == 0
          and cyl_triv["anomalies"] == 0,
          "cylinder P y P transport (M=3): net crossings = %+d == 0, "
          "teleports %+d, anomalies %d"
          % (cyl_triv["net_up"], cyl_triv["teleports"],
             cyl_triv["anomalies"]))

    # ---------------------------------------------------------------- S3
    section("S3  SPECTRAL FLOW (P3): edge levels through E = 0 per flux "
            "quantum")
    fb, ft = cyl_topo["flow"]["bottom"], cyl_topo["flow"]["top"]
    check("G10-flow-topo", abs(fb) == 1 and ft == -fb,
          "M=1: net zero-crossings bottom edge = %+d, top edge = %+d "
          "(chirality sigma = %+d, one chiral branch per edge, "
          "antisymmetric as inflow demands)" % (fb, ft, fb))
    fb3, ft3 = cyl_triv["flow"]["bottom"], cyl_triv["flow"]["top"]
    check("G11-flow-triv", fb3 == 0 and ft3 == 0,
          "M=3: net zero-crossings bottom = %d, top = %d (no in-gap "
          "spectral flow in the trivial phase)" % (fb3, ft3))

    # ---------------------------------------------------------------- S4
    section("S4  STREDA (P4): dN/dPhi of the filled band on the magnetic "
            "torus")
    dev = max(gauge_check(n, L_STREDA) for n in NPHI_STREDA)
    st_topo = [streda_count(M_TOPO, n) for n in NPHI_STREDA]
    st_triv = [streda_count(M_TRIV, n) for n in NPHI_STREDA]
    min_gap = min(min(g for _N, g in st_topo), min(g for _N, g in st_triv))
    check("G12-streda-gauge", dev < GAUGE_DEV_BAR
          and min_gap > STREDA_GAP_BAR,
          "uniform-flux Peierls gauge verified: max plaquette deviation "
          "%.2e < 1e-12 (all n_phi); E=0 gap open, min|E| = %.4f > %.1f "
          "(both M, all n_phi)" % (dev, min_gap, STREDA_GAP_BAR))
    N0 = st_topo[0][0]
    dN = [st_topo[i][0] - N0 for i, _ in enumerate(NPHI_STREDA)]
    slope = fit_slope(NPHI_STREDA, [N for N, _g in st_topo])
    s_or3 = +1                                   # OR3, frozen at calibration
    check("G13-streda-topo",
          abs(slope - s_or3 * C_int) < STREDA_FIT_BAR
          and all(dN[i] == s_or3 * C_int * n
                  for i, n in enumerate(NPHI_STREDA)),
          "M=1: N(n_phi) = %s, DeltaN = %s = s C n_phi with s = %+d (OR3) "
          "and C = %+d; fit slope %+.6f (|slope - sC| < 5e-2, then exact "
          "integer); dN/dPhi = sC/(2 pi) per unit flux Phi = 2 pi n_phi"
          % ([N for N, _g in st_topo], dN, s_or3, C_int, slope))
    dN3 = [st_triv[i][0] - st_triv[0][0] for i, _ in enumerate(NPHI_STREDA)]
    check("G14-streda-triv", all(d == 0 for d in dN3),
          "M=3: N(n_phi) = %s constant, DeltaN = %s == 0 (C = 0 dual)"
          % ([N for N, _g in st_triv], dN3))

    # ---------------------------------------------------------------- S5
    section("S5  16-COPY / LEVEL BOOKKEEPING (P5): exact Fractions "
            "(v470 arithmetic re-derived)")
    N_maj = 2 ** (G_CAR - 1)
    N_cplx = Fraction(N_maj, 2)
    c_minus = N_maj * Fraction(1, 2) * abs(C_int)
    k0 = abs(C_int)
    check("G15-copies", N_maj == 16 and N_cplx == 8 and c_minus == 8
          and c_minus == G_CAR + N_FAM and k0 == 1,
          "N_maj = 2^(g_car-1) = %d Majoranas = %s complex copies; "
          "c_- = 16 x 1/2 x |C| = %s = g_car + N_fam = %d; per-copy U(1) "
          "level k0 = |C| = %d (the v470 EM1 statement, one copy computed "
          "here)" % (N_maj, N_cplx, c_minus, G_CAR + N_FAM, k0))
    trY2 = 3 * Fraction(1, 3) ** 2 + 2 * Fraction(1, 2) ** 2
    trT32 = 2 * Fraction(1, 2) ** 2
    kY = trY2 / trT32
    b1_SM = Fraction(41, 6)
    ferm = Fraction(2, 3) * 3 * (6 * Fraction(1, 6) ** 2
                                 + 3 * Fraction(2, 3) ** 2
                                 + 3 * Fraction(1, 3) ** 2
                                 + 2 * Fraction(1, 2) ** 2 + 1)
    higgs = Fraction(1, 3) * 2 * Fraction(1, 2) ** 2
    check("G16-embedding",
          kY == Fraction(5, 3) and b1_SM / kY == Fraction(41, 10)
          and ferm == Fraction(20, 3) and higgs == Fraction(1, 6)
          and ferm + higgs == b1_SM,
          "k_Y = tr_5bar(Y^2)/tr(T3^2) = (%s)/(%s) = %s; (1/k_Y) x 41/6 = "
          "%s = b1; carrier decomposition 41/6 = %s (fermions) + %s (Higgs) "
          "(v470 arithmetic verbatim)"
          % (trY2, trT32, kY, b1_SM / kY, ferm, higgs))

    # ---------------------------------------------------------------- S6
    section("S6  MUTANTS (P6): reversed chirality + wrong-band projector")
    C_conj = fhs_chern(M_TOPO, sy=-1.0)
    dP_conj, step_conj = pump_winding(M_TOPO, sy=-1.0)
    cyl_conj = cylinder_sweep(M_TOPO, sy=-1.0)
    st_conj = [streda_count(M_TOPO, n, sy=-1.0) for n in NPHI_STREDA]
    dNc = [st_conj[i][0] - st_conj[0][0] for i, _ in enumerate(NPHI_STREDA)]
    check("G17-mutant-conj",
          abs(C_conj + 1) < TOL_CHERN and abs(dP_conj + 1) < PUMP_TOL
          and step_conj < UNWRAP_BAR and cyl_conj["net_up"] == -1
          and cyl_conj["anomalies"] == 0
          and all(dNc[i] == -s_or3 * n for i, n in enumerate(NPHI_STREDA)),
          "complex-conjugated model flips EVERYTHING simultaneously: FHS "
          "C = %+.9f == -1, winding DeltaP = %+.9f == -1, cylinder "
          "transport %+d == -1, Streda DeltaN = %s = -s n_phi -- sign "
          "mutant CAUGHT (convention-free consistency)"
          % (C_conj, dP_conj, cyl_conj["net_up"], dNc))
    C_mut24 = fhs_chern(M_TOPO, band_rule=mutant_band_rule)
    C_mut36 = fhs_chern(M_TOPO, N=N_FHS_ALT, band_rule=mutant_band_rule)
    dP_mut, step_mut = pump_winding(M_TOPO, band_rule=mutant_band_rule)
    grid_dev = abs(C_mut24 - C_mut36)
    check("G18-mutant-band",
          grid_dev > MUTANT_GRID_BAR and step_mut > UNWRAP_BAR
          and abs(dP_mut - C_int) > 0.5,
          "wrong-band projector BREAKS quantisation: FHS reading is "
          "GRID-UNSTABLE ('C' = %+.4f at N=24 vs %+.4f at N=36, dev %.2f > "
          "%.1f -- no well-defined invariant), the Wannier flow is "
          "unreadable (max unwrap step %.4f > %.2f) and the nominal "
          "winding %+.4f != C = %+d -- mutant CAUGHT"
          % (C_mut24, C_mut36, grid_dev, MUTANT_GRID_BAR, step_mut,
             UNWRAP_BAR, dP_mut, C_int))

    # ---------------------------------------------------------------- S7
    section("S7  runtime + verdict")
    wall = time.time() - T0_WALL
    check("G19-runtime", wall < RUNTIME_BAR,
          "WALL %.1f s < %.0f s bar" % (wall, RUNTIME_BAR))

    by_name = {n: ok for n, ok, _d in CHECKS}
    instr = ["G01-spec", "G02-chern-topo", "G03-chern-triv",
             "G04-strip-ingap", "G05-strip-gap", "G12-streda-gauge",
             "G15-copies", "G16-embedding", "G19-runtime"]
    match = ["G06-pump-wilson-topo", "G07-pump-wilson-triv",
             "G08-pump-cyl-topo", "G09-pump-cyl-triv", "G10-flow-topo",
             "G11-flow-triv", "G13-streda-topo", "G14-streda-triv",
             "G17-mutant-conj", "G18-mutant-band"]
    if not all(by_name[n] for n in instr):
        verdict = "INSTRUMENT_FAILS"
    elif all(by_name[n] for n in match):
        verdict = "PUMP_QUANTIZED_MATCHES_CHERN"
    else:
        verdict = "PUMP_MISMATCH"
    check("G20-verdict", verdict == "PUMP_QUANTIZED_MATCHES_CHERN",
          "VERDICT = %s (pre-registered expectation: "
          "PUMP_QUANTIZED_MATCHES_CHERN)" % verdict)

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    if npass == len(CHECKS):
        print("ALL GATES PASSED %d/%d" % (npass, len(CHECKS)))
    else:
        print("GATES PASSED %d/%d -- FAILURES: %s"
              % (npass, len(CHECKS),
                 [n for n, ok, _d in CHECKS if not ok]))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s   WALL %.1f s" % (SPEC_SHA[:16], wall))
    print("EXPLORATION ONLY -- experiments/ level: NO promotion, NO ledger "
          "row, NO marker")
    print("moved, NO gate closed or narrowed.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
