#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mmst_wzw_coverage_probe -- SEAM.MMST.WZW_COVERAGE.01:
literature adjudication of the Osborne-Stottmeister WZW-current
theorem's COVERAGE of the TFPT seam target, plus a NEW empirical
convergence-RATE gate on the v367/v444 p+ip collar edge.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  v336 consumes Osborne-Stottmeister,
"Conformal Field Theory from Lattice Fermions" (Comm. Math. Phys.
398 (2023) 219, arXiv:2107.13834; below OS23) as the citable
continuum-scaling-limit leg of SEAM.EQUIV.01, quoting the WZW window
rank <= c <= D.  The corpus never adjudicated PRECISELY which part
of the seam target (SO(16)_1 -> (E8)_1 at c = 8) the proved theorems
cover, and v444 gated only Cauchy SHRINKAGE of the collar edge
correlator, never a convergence RATE against the polynomial form of
OS23's explicit error estimates.  This round does both: (a) a typed
coverage adjudication transcribed into exact-integer gates, and
(b) a preregistered rate measurement on the same collar.

LEG (a) ADJUDICATION (from the OS23 full text; anchors are OS23
section / theorem / equation numbers):

COVERED (by OS23's proved statements):
  A1. Free-fermion scaling limits via operator-algebraic
      renormalization, complex AND self-dual (Majorana) CAR algebras
      (Sects. 2-3; wavelet RG Sect. 3.1, momentum-cutoff RG
      Sect. 3.2; ground-state scaling limit Lemma 3.11).
  A2. Virasoro / Koo-Saleur convergence: KS approximants converge
      STRONGLY to the continuum Virasoro generators on the dense
      core of finite-energy vectors, central charge c = 1/2, 1
      (Thm A = Thm 4.11; smeared version Thm 4.16); Virasoro n-point
      correlators converge (Thm C = Thm 6.3).
  A3. WZW currents that are NORMAL-ORDERED FERMION BILINEARS
      (Sect. 5): the u(1) current -- Thm 5.1, smeared lattice
      currents converge STRONGLY on the dense domain F_alg(D_std) of
      finite-particle vectors; nonabelian u(D)_1 currents
      J^mu = t^mu_ij :psi_i^dag psi_j: (Eq. 225) by the
      Cauchy-Schwarz reduction (Eq. 229); the closing remark of
      Sect. 5 extends the same reasoning to ANY simply-laced g_k
      current of bilinear form (225), "possibly by using the
      Majorana algebras".  Hence so(16)_1 on D = 16 Majoranas (the
      adjoint = 120 antisymmetric bilinears) and u(8)_1 on 8 Dirac
      fermions (64 bilinears) ARE inside the proved class; the WZW
      window rank <= c <= D (Sect. 1.1) holds: 8 <= 8 <= 16.
      Honest nuance: Thm 5.1 is DISPLAYED only for u(1); the
      nonabelian case is proved-by-reduction (229) plus remark.
  A4. Correlation functions + explicit POLYNOMIAL error estimates:
      dynamical fermion correlators under current/KS-generated
      Bogoliubov flows (Thm B = Thm 6.1, uniform in t on compacts),
      mixed correlators with WZW-current insertions (Remark after
      Thm 6.3); error form Error^2 <~ C * 2^(-2*delta*N),
      delta in [0, 2] (Eqs. 205, 207) -- i.e. Error ~ eps_N^delta,
      polynomial in the lattice spacing, up to second order.

NOT COVERED (named; what the TFPT seam target still needs):
  N1. NET_EXTENSION_MU4_GSO -- the simple-current (mu4 / GSO)
      extension SO(16)_1 -> (E8)_1 as a NET statement.  The 128
      weight-1 spinor currents (128 = 2^7 = dim S+ of so(16);
      248 = 120 + 128) are NOT fermion bilinears, hence outside the
      Sect.-5 class; OS23's own scope line restricts results to
      "free-fermion CFTs, products thereof and certain CFTs
      embeddable into those", and defers general rational-CFT
      extensions to anyonic-chain methods (Sect. 1.1).
  N2. ODD_SECTOR_TWIST_FIELDS -- convergence for odd / twist
      (spin-field) observables is explicitly deferred to "a separate
      publication" (Sect. 1.1, Ising remark); the SO(16)_1 spinor
      sector whose currents build (E8)_1 is exactly this type.
  N3. ONE_SIDED_CHIRAL_EDGE_NET -- OS23 lives on a 1+1-d lattice
      with BOTH chiralities entangled at finite scale (the finitely
      renormalized states are not pure "due to the entanglement of
      the chiral halves", Sect. 1.2); the TFPT seam needs the
      genuinely one-sided chiral edge net of a 2+1-d p+ip bulk
      (bulk-edge correspondence) -- not an OS23 statement.
  N4. OS_HOLOMORPHY_SELECTOR -- nothing in OS23 selects the
      holomorphic det K = 1 net (E8)_1 over det K = 4 SO(16)_1 at
      c = 8; the OS-reconstruction / holomorphy discriminator legs
      (v336 legs 2 and 4) are external to the paper.

So OS23 covers the BILINEAR HALF of the seam target (the SO(16)_1
current algebra and its convergence with polynomial rate) and does
NOT cover the extension half (mu4/GSO net statement, twist sector,
one-sided edge, holomorphy selector).  COVERAGE_FULL is therefore
not on the table; the probe adjudicates PARTIAL vs ABSENT, and the
rate leg adjudicates RATE_CONSISTENT vs RATE_INCONSISTENT.

LEG (b) THE RATE MEASUREMENT (new empirical content).  On the
v367/v444 p+ip collar (rebuilt in-probe; M = 1 topological, gapped;
strip periodic in x, open in y; the momentum-space build is the
EXACT x-Fourier transform of v444's real-space model and is
cross-checked against it), define the edge-row Nambu correlator
C_Nx(r) at y = 0 and the dimensionless ratio
    rho(Nx) = C_Nx(Nx/4) / C_Nx(Nx/8).
The chiral-CFT prediction (eta = 1 correlator on a ring, chord law
1/chord(r), chord(r) = (Nx/pi) sin(pi r/Nx)) gives the continuum
target
    T = chord(Nx/8)/chord(Nx/4) = sin(pi/8)/sin(pi/4) = 0.5411961...
independent of Nx.  Under the refinement ladder
Nx = 16, 24, 32, 48, 64, 96, 128, 192, 256 the error
e(Nx) = |rho(Nx) - T| must vanish POLYNOMIALLY, exponent p from the
log-log fit plus dyadic Richardson cross-checks.

PRE-REGISTERED BAND (frozen before the record runs; a disclosed
calibration pass informed the bars, prints frozen below):
RATE_BAND = [0.5, 4.0].  Rationale: OS23's Eqs. (205)/(207) are
UPPER bounds Error ~ eps_N^delta with delta in [0, 2] at the
operator level, so consistency requires only p >= a first-order-ish
lower edge (0.5 = half the guaranteed first order, honest margin);
the upper edge 4.0 is a calibration-informed allowance for
OBSERVABLE-level superconvergence -- the dimensionless ratio cancels
the leading amplitude correction and the calibration measured
p ~ 3.5, which does NOT contradict an upper bound.  A wrong-target
mutant must land OUTSIDE the band (rate ~ 0).

PRE-REGISTERED ADJUDICATION:
  P1 coverage arithmetic (exact integers): 16 Majoranas = 8 Dirac,
     c = 16/2 = 8 = rank so(16), window 8 <= 8 <= 16; bilinear
     counts dim so(16) = C(16,2) = 120, dim u(8) = 8^2 = 64.
  P2 the extension is OUTSIDE the bilinear class (exact): dim E8 =
     248 = 120 + 128, 128 = 2^7 = dim S+ (not a bilinear count);
     root split 240 = 112 + 128 by explicit enumeration; spinor
     conformal weight h(S+) = 1 and h(vector) = 1/2 by exact
     Sugawara arithmetic (inverse Cartan of D8, h_dual = 14, k = 1).
  P3 det/index bookkeeping (exact): det Cartan D8 = 4 -> det Cartan
     E8 = 1; lattice index [E8 : D8] = 2 with index^2 = 4/1; global
     index of SO(16)_1 = sum d_i^2 over its 4 simple-current
     primaries = 4 -> 1 (holomorphic); typed COVERED/NOT-COVERED
     table internally consistent (bilinear predicate separates).
  P4 collar rebuild: gap(M=1) = 2, Chern |C| = 1 (M=1) vs 0 (M=3);
     momentum-space == real-space correlator to < 1e-12.
  P5 edge criticality: eta(Nx=64) in [0.85, 1.15] (log-log fit,
     r in [2, 16]); bulk-row slope < -0.3 (exponential).
  P6 THE RATE GATE: ladder valid (strictly increasing, span >= 8x,
     all rungs divisible by 8); e(Nx) strictly decreasing along the
     ladder; fitted exponent p in RATE_BAND = [0.5, 4.0]; dyadic
     Richardson exponents (16,32,64), (32,64,128), (64,128,256) all
     > 0, the finest inside the band, max |p_Rich - p| <= 1.0.
  P7 negative control: M = 3 (trivial, no edge) must NOT converge
     to T: min over its ladder of |rho - T|/T >= 0.5 and
     rho_triv(128) < 0.01 (it decays toward 0, not T).
  P8 mutant A (wrong CFT target T^2, the eta=2 value): the rate
     extractor must FAIL the band (p < 0.5) with terminal error
     > 0.1 => CAUGHT.
  P9 mutant B (scrambled refinement ladder, frozen permutation):
     the ladder validator must flag it => CAUGHT.
EXPECTED VERDICT (pre-registered): COVERAGE_PARTIAL_RATE_CONSISTENT.
VERDICT ENUM: COVERAGE_PARTIAL_RATE_CONSISTENT /
COVERAGE_PARTIAL_RATE_INCONSISTENT / COVERAGE_FULL (only if Thm 5.1
provably covered the (E8)_1 net statement -- it does not) /
COVERAGE_ABSENT.

CALIBRATION RECORD (one disclosed calibration pass, prints frozen
verbatim; no bar, ladder rung, Ny, target or tolerance moved after
freeze):
CAL_RHO {Nx: rho}: 16: 0.47779817, 24: 0.52679022, 32: 0.53836478,
  48: 0.54167324, 64: 0.54161384, 96: 0.54132400, 128: 0.54123909,
  192: 0.54120460, 256: 0.54119878.  (Note the sign change of
  rho - T between Nx = 32 and 48: two competing correction terms;
  |e| stays strictly decreasing.)
CAL_P = 3.477 (log-log fit over the full ladder).
CAL_RICH = 4.220 / 3.116 / 3.217 (dyadic triplets, coarse to fine).
CAL_ETA(64) = 0.991; CAL_BULK_SLOPE = -0.874.
CAL_TRIV {Nx: rho}: 16: 8.902e-02, 32: 1.713e-02, 64: 9.494e-04,
  128: 3.730e-06 (decaying toward 0, min |rho-T|/T = 0.836).
CAL_MUT_A: rate -0.067, terminal error 0.248 (CAUGHT).
Ny-independence: rho(64) identical to 10 decimals for
Ny = 16/20/24/28 (frozen NY = 20); the kx = 0 strip carries two
EXACT zero modes, both excluded by the occupancy rule w < -1e-9
(the v444 convention, deterministic).

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 preregistration;
S1 coverage transcription G10-G14 (exact sympy/Fraction integer
arithmetic only); S2 collar + rate G20-G26; S3 mutants G30-G31;
S4 G40 determinism vs frozen calibration, G41 verdict, G99 runtime.
DETERMINISM: no randomness anywhere; fixed ladder, fixed Ny, fixed
occupancy rule; run2 must be identical modulo wall-clock tokens
(lines carrying 'WALL').

HONEST LIMITATIONS: (i) the rate is measured on ONE dimensionless
observable of ONE collar model -- it grounds the polynomial-rate
FORM of OS23's estimates on the TFPT collar, it does not verify the
theorem's constants or its operator topology; (ii) the observable
superconverges (p ~ 3.5 > delta_max = 2), so the band's upper edge
is calibration-informed, not paper-derived; (iii) the coverage
gates are exact TRANSCRIPTIONS of a human literature adjudication
-- executable bookkeeping, not new mathematics; (iv) nothing here
closes or narrows SEAM.EQUIV.01: the four NOT-COVERED items stand.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import math
import time
from fractions import Fraction

import numpy as np
import sympy as sp

# ---------------------------------------------------------------- frozen
CONTRACT = "SEAM.MMST.WZW_COVERAGE.01"
RUNTIME_BAR = 180.0

D_MAJORANA = 16
N_DIRAC = 8
LADDER = (16, 24, 32, 48, 64, 96, 128, 192, 256)
SCRAMBLED_LADDER = (32, 16, 64, 24, 48, 96, 128, 192, 256)   # frozen mutant
NY = 20
M_TOPO = 1.0
M_TRIV = 3.0
TRIV_LADDER = (16, 32, 64, 128)
OCC_EPS = -1e-9                 # v444 occupancy convention
RATE_BAND = (0.5, 4.0)          # preregistered (see docstring)
PAPER_DELTA_RANGE = (0, 2)      # OS23 Eqs. (205)/(207): Error ~ eps_N^delta
RICH_DEV_BAR = 1.0
ETA_BAND = (0.85, 1.15)
BULK_SLOPE_BAR = -0.3
TRIV_REL_BAR = 0.5
TRIV_TERMINAL_BAR = 0.01
MUT_ERR_FLOOR = 0.1
XCHECK_BAR = 1e-12
CAL_TOL = 5e-7                  # vs frozen 8-decimal calibration prints

CAL_RHO = {16: "0.47779817", 24: "0.52679022", 32: "0.53836478",
           48: "0.54167324", 64: "0.54161384", 96: "0.54132400",
           128: "0.54123909", 192: "0.54120460", 256: "0.54119878"}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list = []

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)


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


def fit_slope(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx if sxx else float("nan")


# ---------------------------------------------- S1: exact Lie arithmetic
def cartan(n, edges):
    A = sp.zeros(n, n)
    for i in range(n):
        A[i, i] = 2
    for a, b in edges:
        A[a - 1, b - 1] = -1
        A[b - 1, a - 1] = -1
    return A


D8_EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (6, 8)]
E8_EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)]


def d8_root_split():
    """Explicit enumeration of the 240 E8 roots as D8 + spinor cosets."""
    d8 = 0
    for i, j in itertools.combinations(range(8), 2):
        d8 += 4                                    # +-e_i +- e_j
    spinor = 0
    half = Fraction(1, 2)
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:               # even # of minus signs
            v = [half * s for s in signs]
            if sum(x * x for x in v) == 2:
                spinor += 1
    return d8, spinor


def sugawara_weights():
    """Exact conformal weights of the D8 level-1 vector / spinor primaries:
    h = (lam, lam + 2 rho) / (2 (k + h_dual)); (omega_i, omega_j) = (A^-1)_ij
    for simply-laced normalisation (alpha, alpha) = 2."""
    A = cartan(8, D8_EDGES)
    Ainv = A.inv()
    h_dual = 14                                    # h_dual(D8) = 2*8 - 2
    k = 1

    def h_of(node):
        lam_lam = Ainv[node - 1, node - 1]
        lam_rho = sum(Ainv[node - 1, j] for j in range(8))
        return sp.Rational((lam_lam + 2 * lam_rho), 2 * (k + h_dual))

    return h_of(1), h_of(8)                        # vector omega_1, spinor omega_8


# -------------------------------------------- S2: the p+ip collar (v367/v444)
def strip_H(kx, M, Ny):
    """v444 _strip_H verbatim: Ly sites open in y, kx periodic; 2Ny x 2Ny BdG."""
    ons = np.sin(kx) * SX + (M - np.cos(kx)) * SZ
    hop = -0.5 * SZ + (1 / (2j)) * SY
    H = np.zeros((2 * Ny, 2 * Ny), complex)
    for y in range(Ny):
        H[2 * y:2 * y + 2, 2 * y:2 * y + 2] = ons
    for y in range(Ny - 1):
        H[2 * y:2 * y + 2, 2 * y + 2:2 * y + 4] = hop
        H[2 * y + 2:2 * y + 4, 2 * y:2 * y + 2] = hop.conj().T
    return H


def row_corr_k(Nx, Ny, M, y0, dxs):
    """Edge/bulk row correlator via exact x-Fourier transform of the v444
    real-space model: G(dx) = (1/Nx) sum_kx e^{i kx dx} P(kx)|_{(y0,y0) block},
    C(dx) = Frobenius norm of the 2x2 block (the v444 convention)."""
    blocks = []
    for m in range(Nx):
        kx = 2 * np.pi * m / Nx
        w, v = np.linalg.eigh(strip_H(kx, M, Ny))
        occ = v[:, w < OCC_EPS]
        P = occ @ occ.conj().T
        blocks.append(P[2 * y0:2 * y0 + 2, 2 * y0:2 * y0 + 2])
    blocks = np.array(blocks)
    out = {}
    for dx in dxs:
        ph = np.exp(1j * 2 * np.pi * np.arange(Nx) * dx / Nx)
        out[dx] = float(np.linalg.norm((blocks * ph[:, None, None]).sum(0) / Nx))
    return out


def real2d_row_corr(Nx, Ny, M, y0, dxs):
    """v444 _real2d verbatim (periodic x, open y) -- cross-check only."""
    onx = -0.5 * SZ + (1 / (2j)) * SX
    ony = -0.5 * SZ + (1 / (2j)) * SY
    ons = M * SZ
    N = Nx * Ny

    def idx(x, y):
        return (x % Nx) * Ny + y

    H = np.zeros((2 * N, 2 * N), complex)
    for x in range(Nx):
        for y in range(Ny):
            a = idx(x, y)
            H[2 * a:2 * a + 2, 2 * a:2 * a + 2] += ons
            b = idx(x + 1, y)
            H[2 * a:2 * a + 2, 2 * b:2 * b + 2] += onx
            H[2 * b:2 * b + 2, 2 * a:2 * a + 2] += onx.conj().T
            if y < Ny - 1:
                c = idx(x, y + 1)
                H[2 * a:2 * a + 2, 2 * c:2 * c + 2] += ony
                H[2 * c:2 * c + 2, 2 * a:2 * a + 2] += ony.conj().T
    w, v = np.linalg.eigh(H)
    occ = v[:, w < OCC_EPS]
    G = occ @ occ.conj().T
    a0 = idx(0, y0)
    return {dx: float(np.linalg.norm(G[2 * a0:2 * a0 + 2,
                                       2 * idx(dx, y0):2 * idx(dx, y0) + 2]))
            for dx in dxs}


def chern(M, N=24):
    """v367 Fukui-Hatsugai-Suzuki plaquette Chern number (verbatim)."""
    def d(kx, ky):
        return np.array([np.sin(kx), np.sin(ky), M - np.cos(kx) - np.cos(ky)])

    def occ_vec(kx, ky):
        dx, dy, dz = d(kx, ky)
        w, v = np.linalg.eigh(dx * SX + dy * SY + dz * SZ)
        return v[:, 0]

    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    u = [[occ_vec(kx, ky) for ky in ks] for kx in ks]
    F = 0.0
    for i in range(N):
        for j in range(N):
            ip, jp = (i + 1) % N, (j + 1) % N
            u00, u10, u01, u11 = u[i][j], u[ip][j], u[i][jp], u[ip][jp]
            Ux = np.vdot(u00, u10); Ux /= abs(Ux)
            Uy = np.vdot(u10, u11); Uy /= abs(Uy)
            Ux2 = np.vdot(u01, u11); Ux2 /= abs(Ux2)
            Uy2 = np.vdot(u00, u01); Uy2 /= abs(Uy2)
            F += np.angle(Ux * Uy * np.conj(Ux2) * np.conj(Uy2))
    return F / (2 * np.pi)


def gap(M, N=48):
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    return 2 * min(np.linalg.norm([np.sin(kx), np.sin(ky),
                                   M - np.cos(kx) - np.cos(ky)])
                   for kx in ks for ky in ks)


def ladder_valid(ladder):
    """Refinement-ladder validator: strictly increasing, span >= 8x,
    every rung divisible by 8 (so Nx/8, Nx/4 are integers)."""
    mono = all(b > a for a, b in zip(ladder, ladder[1:]))
    span = ladder[-1] >= 8 * ladder[0]
    div = all(n % 8 == 0 for n in ladder)
    return mono and span and div


def rate_fit(rho, ladder, target):
    xs = [math.log(n) for n in ladder]
    ys = [math.log(abs(rho[n] - target)) for n in ladder]
    return -fit_slope(xs, ys)


def richardson(rho, triplet):
    a, b, c = triplet
    return math.log2(abs(rho[a] - rho[b]) / abs(rho[b] - rho[c]))


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.parse_args()

    print("=" * 78)
    print("mmst_wzw_coverage_probe -- %s" % CONTRACT)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("EXPLORATION ONLY (2026-08-27). experiments/ level: NO promotion, "
          "NO ledger row,")
    print("NO marker moved, NO gate closed or narrowed.")
    print("=" * 78)

    # ---------------------------------------------------------- S0
    section("S0  firewall + preregistration")
    check("G01 FIREWALL", True,
          "exploration only; touches nothing outside experiments/tfpt-discovery/; "
          "verification/, website/, rh/, TeX, ledger untouched")
    enum_ok = RATE_BAND == (0.5, 4.0) and PAPER_DELTA_RANGE == (0, 2) \
        and LADDER == (16, 24, 32, 48, 64, 96, 128, 192, 256)
    check("G02 PREREG", enum_ok,
          "verdict enum + RATE_BAND %s + ladder frozen in docstring "
          "(SPEC_SHA %s); paper delta range %s (OS23 Eqs. 205/207)"
          % (list(RATE_BAND), SPEC_SHA[:16], list(PAPER_DELTA_RANGE)))

    # ---------------------------------------------------------- S1
    section("S1  coverage transcription (exact integer arithmetic)")

    c_seam = sp.Rational(D_MAJORANA, 2)                       # 16 * (1/2)
    rank_so16 = 8
    window = rank_so16 <= c_seam <= D_MAJORANA
    check("G10 FERMION/CENTRAL-CHARGE ARITHMETIC",
          D_MAJORANA == 2 * N_DIRAC and c_seam == 8 and window,
          "16 Majoranas = 8 Dirac, c = 16*(1/2) = %s = rank so(16) = %d; "
          "OS23 WZW window rank <= c <= D: 8 <= 8 <= 16 HOLDS (Sect. 1.1)"
          % (c_seam, rank_so16))

    dim_so16 = math.comb(D_MAJORANA, 2)
    dim_u8 = N_DIRAC ** 2
    check("G11 BILINEAR CLASS (COVERED)",
          dim_so16 == 120 and dim_u8 == 64,
          "dim so(16) = C(16,2) = %d antisymmetric Majorana bilinears; "
          "dim u(8) = 8^2 = %d Dirac bilinears -- both of OS23 form (225), "
          "inside the Thm 5.1 / Sect. 5 proved class" % (dim_so16, dim_u8))

    n_d8_roots, n_spinor = d8_root_split()
    dim_e8 = dim_so16 + 2 ** 7
    h_vec, h_spin = sugawara_weights()
    check("G12 E8 EXTENSION OUTSIDE CLASS",
          dim_e8 == 248 and n_d8_roots == 112 and n_spinor == 128
          and n_d8_roots + n_spinor == 240
          and h_spin == 1 and h_vec == sp.Rational(1, 2),
          "dim E8 = 120 + 128 = %d; root split 240 = %d + %d (explicit "
          "enumeration); Sugawara h(spinor S+) = %s (weight-1 CURRENT but NOT "
          "a bilinear -- 128 = 2^7 = dim S+), h(vector) = %s"
          % (dim_e8, n_d8_roots, n_spinor, h_spin, h_vec))

    detD8 = int(cartan(8, D8_EDGES).det())
    detE8 = int(cartan(8, E8_EDGES).det())
    lattice_index = sp.sqrt(sp.Rational(detD8, detE8))
    global_index_so16 = 4 * 1 ** 2          # 4 simple-current primaries, d_i = 1
    check("G13 DET/INDEX ARITHMETIC",
          detD8 == 4 and detE8 == 1 and lattice_index == 2
          and global_index_so16 == 4,
          "det Cartan D8 = %d -> det Cartan E8 = %d; lattice index [E8:D8] = "
          "%s (index^2 = 4/1); global index of SO(16)_1 = sum d_i^2 = %d over "
          "its 4 simple-current primaries -> 1 (holomorphic)"
          % (detD8, detE8, lattice_index, global_index_so16))

    covered = {
        "A1_FREE_FERMION_SCALING_LIMIT": dict(anchor="Sects. 2-3, Lemma 3.11",
                                              bilinear=None),
        "A2_VIRASORO_KS": dict(anchor="Thm A/4.11, 4.16, Thm C/6.3",
                               bilinear=True),
        "A3_WZW_BILINEAR_CURRENTS": dict(anchor="Sect. 5, Thm 5.1, Eqs. 225/229",
                                         bilinear=True),
        "A4_CORRELATORS_ERROR_ESTIMATES": dict(anchor="Thm B/6.1, Eqs. 205/207",
                                               bilinear=True),
    }
    not_covered = {
        "N1_NET_EXTENSION_MU4_GSO": dict(anchor="Sect. 1.1 scope + Sect. 5 class",
                                         bilinear=False),
        "N2_ODD_SECTOR_TWIST_FIELDS": dict(anchor="Sect. 1.1 Ising remark",
                                           bilinear=False),
        "N3_ONE_SIDED_CHIRAL_EDGE_NET": dict(anchor="Sect. 1.2 chiral halves",
                                             bilinear=False),
        "N4_OS_HOLOMORPHY_SELECTOR": dict(anchor="absent from OS23",
                                          bilinear=False),
    }
    sep = all(v["bilinear"] in (True, None) for v in covered.values()) \
        and all(v["bilinear"] is False for v in not_covered.values())
    check("G14 TYPED ADJUDICATION TABLE",
          len(covered) == 4 and len(not_covered) == 4 and sep
          and all(v["anchor"] for v in list(covered.values())
                  + list(not_covered.values())),
          "COVERED %d items / NOT COVERED %d named items, every item "
          "anchored; the executable bilinear predicate separates the lists "
          "(the seam's missing half is exactly the non-bilinear extension)"
          % (len(covered), len(not_covered)))

    # ---------------------------------------------------------- S2
    section("S2  the collar rate measurement (v367/v444 p+ip edge)")

    g_topo = gap(M_TOPO)
    C_topo = round(abs(chern(M_TOPO)))
    C_triv = round(abs(chern(M_TRIV)))
    check("G20 COLLAR REBUILD", g_topo > 1.0 and C_topo == 1 and C_triv == 0,
          "gap(M=1) = %.3f > 1; FHS Chern |C| = %d (M=1 topological) vs "
          "%d (M=3 trivial) -- the v367 collar, rebuilt in-probe"
          % (g_topo, C_topo, C_triv))

    dxs_x = list(range(1, 6))
    ck = row_corr_k(12, 8, M_TOPO, 0, dxs_x)
    cr = real2d_row_corr(12, 8, M_TOPO, 0, dxs_x)
    xdiff = max(abs(ck[d] - cr[d]) for d in dxs_x)
    check("G21 MOMENTUM = REAL-SPACE CROSS-CHECK", xdiff < XCHECK_BAR,
          "max |C_k - C_real| = %.3e < %.0e at Nx=12, Ny=8 (the momentum "
          "build IS the v444 real-space model)" % (xdiff, XCHECK_BAR))

    Nx_eta = 64
    c64 = row_corr_k(Nx_eta, NY, M_TOPO, 0, list(range(1, Nx_eta // 2)))
    rs = np.arange(2, Nx_eta // 4 + 1)
    eta = -fit_slope([math.log(r) for r in rs],
                     [math.log(c64[r]) for r in rs])
    cbulk = row_corr_k(Nx_eta, NY, M_TOPO, NY // 2, list(range(2, 13)))
    bslope = fit_slope(list(range(2, 13)),
                       [math.log(max(cbulk[r], 1e-15)) for r in range(2, 13)])
    check("G22 EDGE CRITICALITY",
          ETA_BAND[0] < eta < ETA_BAND[1] and bslope < BULK_SLOPE_BAR,
          "eta(Nx=64) = %.4f in %s (chiral free-fermion exponent); bulk-row "
          "slope %.3f < %.1f (exponential) -- edge critical, bulk gapped"
          % (eta, list(ETA_BAND), bslope, BULK_SLOPE_BAR))

    T_cft = float(sp.sin(sp.pi / 8) / sp.sin(sp.pi / 4))
    rho = {}
    for Nx in LADDER:
        c = row_corr_k(Nx, NY, M_TOPO, 0, [Nx // 8, Nx // 4])
        rho[Nx] = c[Nx // 4] / c[Nx // 8]
    errs = [abs(rho[n] - T_cft) for n in LADDER]
    for n in LADDER:
        info("rho(%3d) = %.8f   e = %+.3e" % (n, rho[n], rho[n] - T_cft))
    shrink = all(b < a for a, b in zip(errs, errs[1:]))
    check("G23 LADDER VALID + MONOTONE SHRINKAGE",
          ladder_valid(LADDER) and shrink,
          "ladder %s valid (monotone, span 16x, rungs %% 8 == 0); "
          "e(Nx) = |rho - T| strictly decreasing 16 -> 256 "
          "(%.2e -> %.2e); T = sin(pi/8)/sin(pi/4) = %.7f"
          % (list(LADDER), errs[0], errs[-1], T_cft))

    p_rate = rate_fit(rho, LADDER, T_cft)
    in_band = RATE_BAND[0] <= p_rate <= RATE_BAND[1]
    check("G24 THE RATE GATE", in_band,
          "fitted convergence exponent p = %.3f in preregistered band %s "
          "(OS23 polynomial form Error ~ eps_N^delta, delta in %s, is an "
          "UPPER bound; observable superconverges, disclosed)"
          % (p_rate, list(RATE_BAND), list(PAPER_DELTA_RANGE)))

    triplets = [(16, 32, 64), (32, 64, 128), (64, 128, 256)]
    p_rich = [richardson(rho, t) for t in triplets]
    rich_ok = all(p > 0 for p in p_rich) \
        and RATE_BAND[0] <= p_rich[-1] <= RATE_BAND[1] \
        and max(abs(p - p_rate) for p in p_rich) <= RICH_DEV_BAR
    check("G25 RICHARDSON CROSS-CHECK", rich_ok,
          "dyadic Richardson exponents %s (coarse->fine) all > 0, finest in "
          "band, max |p_R - p| = %.3f <= %.1f"
          % (["%.3f" % p for p in p_rich],
             max(abs(p - p_rate) for p in p_rich), RICH_DEV_BAR))

    rho_t = {}
    for Nx in TRIV_LADDER:
        c = row_corr_k(Nx, NY, M_TRIV, 0, [Nx // 8, Nx // 4])
        rho_t[Nx] = c[Nx // 4] / c[Nx // 8]
    rel_t = [abs(rho_t[n] - T_cft) / T_cft for n in TRIV_LADDER]
    check("G26 NEGATIVE CONTROL (M=3)",
          min(rel_t) >= TRIV_REL_BAR and rho_t[128] < TRIV_TERMINAL_BAR,
          "trivial phase does NOT converge to the chiral CFT value: "
          "min |rho - T|/T = %.3f >= %.1f over %s and rho(128) = %.2e "
          "< %.2f (decays toward 0, not T)"
          % (min(rel_t), TRIV_REL_BAR, list(TRIV_LADDER), rho_t[128],
             TRIV_TERMINAL_BAR))

    # ---------------------------------------------------------- S3
    section("S3  mutants (must be CAUGHT)")

    T_wrong = T_cft ** 2                     # the eta = 2 target
    p_wrong = rate_fit(rho, LADDER, T_wrong)
    err_wrong = abs(rho[LADDER[-1]] - T_wrong)
    caught_a = (p_wrong < RATE_BAND[0]) and err_wrong > MUT_ERR_FLOOR
    check("G30 MUTANT A: WRONG CFT TARGET", caught_a,
          "target T^2 = %.4f (eta=2 value): rate %.3f < %.1f (out of band) "
          "with terminal error %.3f > %.1f => CAUGHT"
          % (T_wrong, p_wrong, RATE_BAND[0], err_wrong, MUT_ERR_FLOOR))

    caught_b = not ladder_valid(SCRAMBLED_LADDER)
    check("G31 MUTANT B: SCRAMBLED LADDER", caught_b,
          "frozen permutation %s flagged INVALID by the ladder validator "
          "(monotonicity broken) => CAUGHT" % (list(SCRAMBLED_LADDER),))

    # ---------------------------------------------------------- S4
    section("S4  determinism, verdict, runtime")

    cal_dev = max(abs(rho[n] - float(CAL_RHO[n])) for n in LADDER)
    check("G40 DETERMINISM vs FROZEN CALIBRATION", cal_dev < CAL_TOL,
          "max |rho - CAL_RHO| = %.2e < %.0e over the full ladder (no "
          "randomness; run2 must match run1 modulo WALL lines)"
          % (cal_dev, CAL_TOL))

    coverage_ok = all(ok for name, ok, _d in CHECKS
                      if name.startswith(("G10", "G11", "G12", "G13", "G14")))
    rate_ok = all(ok for name, ok, _d in CHECKS
                  if name.startswith(("G22", "G23", "G24", "G25", "G26")))
    if coverage_ok and rate_ok:
        verdict = "COVERAGE_PARTIAL_RATE_CONSISTENT"
    elif coverage_ok:
        verdict = "COVERAGE_PARTIAL_RATE_INCONSISTENT"
    else:
        verdict = "COVERAGE_ABSENT"
    check("G41 VERDICT", verdict == "COVERAGE_PARTIAL_RATE_CONSISTENT",
          "VERDICT: %s (expected, pre-registered; COVERAGE_FULL impossible: "
          "the mu4/GSO net extension is outside Thm 5.1's bilinear class)"
          % verdict)

    wall = time.time() - T0_WALL
    check("G99 RUNTIME", wall < RUNTIME_BAR,
          "WALL %.1f s < %.0f s" % (wall, RUNTIME_BAR))

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    if npass == len(CHECKS):
        print("ALL GATES PASSED %d/%d" % (npass, len(CHECKS)))
    else:
        print("GATES PASSED %d/%d -- FAILURES PRESENT" % (npass, len(CHECKS)))
    print("VERDICT: %s   SPEC_SHA %s" % (verdict, SPEC_SHA[:16]))
    print("EXPLORATION ONLY: no promotion, no ledger row, no marker moved, "
          "no gate closed or narrowed.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
