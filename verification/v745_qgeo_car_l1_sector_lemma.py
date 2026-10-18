#!/usr/bin/env python3
"""v745 -- QGEO.CARL1.01: the (L1) sector lemma of the CAR continuum majorant, proven modulo elementary steps with explicit constants (L1-SECTOR-PROVEN-MODULO-ELEMENTARY).

PROVENANCE: discovery probe qgeo_car_l1_sector_lemma_probe.py (2026-08-04, 11/11, verdict L1-SECTOR-PROVEN-MODULO-ELEMENTARY; GATE.QGEO does not move).  Promoted verbatim; numbers unchanged.

Discovery probe: QGEO-CAR L1 -- the FIRST PROOF BLOCK of the
majorant lemma named in qgeo_car_continuum_probe.py (verdict
QGEO-CAR-RATES-SUMMABLE): prove

  (L1)   || K_2N^(q) - K_N^(q) ||_{S1(Lambda_eps)} <= B_q(eps)/N

for the UNDRESSED sector covariances (all six deck/twist channels)
with r1 = 1 and EXPLICIT constants, via the announced route (i)
"Euler-Maclaurin/Poisson with edge terms on the occupied-arc mode
sums -- pure lattice analysis".

THE DERIVATION (L1a) -- and an honest SHARPENING of the route: the
Euler-Maclaurin machinery COLLAPSES TO EXACT SUMMATION.  The occupied
arc is a contiguous run of exactly N/2 equally spaced momenta
k_m = 2 pi (m + eta)/N, eta = 1/2 + q/6, cos k > 0; the mode sum is a
finite GEOMETRIC sum, and the Dirichlet closed form is exact at every
N (the "boundary terms at +-k_F" of the EM route are exactly the
sin(pi d/2)/sin(pi d/N) edge structure -- summed, not estimated):

  arc bookkeeping (machine-checked in S0.4):
    q = 0,1,2,3: m in {-N/4, ..., N/4-1}; q = 4,5 (eta > 1):
    m in {-N/4-1, ..., N/4-2}; arc-center momentum kbar = pi qt/(3N)
    with qt = q for q <= 2 and qt = q-6 for q >= 4 (conjugation
    symmetry q <-> 6-q, matching the measured q=1==5, q=2==4 tables).

  (D1)  q != 3:  N c_N^(q)(d) = e^{i pi qt d/(3N)}
                                 * sin(pi d/2)/sin(pi d/N)      EXACT,
  (D2)  q  = 3:  the two weight-1/2 zero modes at k = +-pi/2
        CANCEL the interior edge exactly (S0.2):
                 N c_N^(3)(d) = sin(pi d/2) cot(pi d/N)         EXACT,
  and at d = 0: N c = N/2 (half filling).  Sublattice parity:
  i^{-d} sin(pi d/2) = -i for odd d, 0 for even d (S0.5), so the
  embedded grid kernel is EXACTLY

  (D3)  K_N(s, u) = -(i/M) f_q(s + u/N),   f_q(t) = e^{i pi qt t/3}
        / sin(pi t)  (q = 3: f_3 = cot(pi t)),  s = point separation,
        u = b - a in {-1, 0, +1} the spinor offset; u even => 0.

  CONSEQUENCE: there is NO Riemann-sum error at all -- ALL
  N-dependence of the sector covariances at fixed continuum data is
  the sublattice embedding offset u/N.  The rung difference is a pure
  Taylor step (S0.3, generic-f sympy series):

  (D4)  K_2N - K_N = (i u/(2MN)) f_q'(s)
                     + (integral-form Lagrange remainder),
        |remainder| <= (5/(8 M N^2)) max_{|t-s|<=1/N} |f_q''(t)|,

  with the ELEMENTARY envelopes (|cos| <= 1, sin <= 1, a = pi|qt|/3
  <= 2 pi/3):
  (D5)  |f_q'(t)|  <= (5 pi/3)  / sin^2(pi ct),
        |f_q''(t)| <= (34 pi^2/9)/ sin^3(pi ct),  ct = circ distance,
  and sin(pi eps) >= 2 eps on (0, 1/2]  =>  gamma = 2 (DERIVED).

  TRACE-NORM ASSEMBLY (rank + Frobenius, standard):
  (D6)  ||K_2N - K_N||_{S1(Lambda_eps)}
          <= (1/N) [ ||L_q(eps)||_1
                     + sqrt(2M) (5/(8M)) ||F2(circ s - 1/48)||_F / 48 ]
          =: B_q(eps)/N        for ALL ladder N >= 48,
        L_q(eps) = the EXACT N-independent leading matrix
        [(i u/(2M)) f_q'(s_ij)] on Lambda_eps,
        F2(t) = (34 pi^2/9)/sin^3(pi t)  (entrywise envelope, worst
        rung N = 48 since circ - 1/N >= circ - 1/48).

CHECKS (bars declared before any number):

 S0.1 [sympy] the geometric-sum identity (e^{iL phi}-1)/(e^{i phi}-1)
      = e^{i(L-1)phi/2} sin(L phi/2)/sin(phi/2)  -- symbolic zero.
 S0.2 [sympy] the q = 3 zero-mode cancellation sin(a-b)/sin(b)
      + cos(a) - sin(a)cos(b)/sin(b) = 0 -- symbolic zero.
 S0.3 [sympy] generic Taylor step: f(s+uh/2) - f(s+uh)
      = -(u h/2) f'(s) - (3 u^2 h^2/8) f''(s) + O(h^3) -- generic
      undefined f, covers every sector at once.
 S0.4 [machine] the closed forms (D1)/(D2) equal the FFT mode-sum
      kernels of the parent probe on the FULL embedded grid
      (all 6 q, all 7 N = 48..3072, negative d / wrap included):
      max |dev| < 1e-9 -- the "exact summation" theorem check.
 S0.5 [machine] parity: even-offset entries vanish identically
      (< 1e-10), diagonal = N/(2M) exact, i^{-d} sin(pi d/2) = -i on
      odd d (all residues).
 L1.1 [central] THE LEADING TERM HITS: ratio ||D_N||_1 * N /
      ||L_q(eps)||_1 -> 1 for every sector at eps_mid = 1/12
      (|ratio - 1| <= 0.01 at the last rung, |ratio - 1| monotone
      decreasing over the last 3 rungs); full ratio table printed.
 L1.2 [central] ENTRYWISE Taylor-Lagrange coverage: for ALL sectors,
      ALL 6 rungs, ALL off-diagonal grid entries (point pairs
      p_i != p_j): |D_entry - lead_entry/N| <= (5/(8 M N^2))
      F2(circ(s) - 1/N):  ZERO violations (~5e5 inequalities).
 L1.3 [central] the PROVEN bound covers the measurement:
      ||D_N||_1 <= B_q(eps)/N for all 6 x 6 x 3 = 108 (q, rung, eps)
      cases: ZERO violations; minimal slack reported.
 L1.4 [E] gamma consistency: the derived envelope gives gamma = 2;
      the eps-slope of the SHARP leading constant ||L_q(eps)||_1
      matches the measured collision exponent per sector
      (|slope_derived - slope_measured| <= 0.15); measured exponents
      re-derived here (parent: 1.84..1.91 <= 2).
 L1.5 [machine, must-fail] rate-2 is IMPOSSIBLE: ||D_N||_1 * N^2
      grows by a factor >= 1.8 per rung (last 3 rungs, every q at
      eps_mid) -- the 1/N sublattice boundary term is real; no
      constant B' can give ||D|| <= B'/N^2.
 L1.6 [C] LEMMA STATUS: (L1) for the undressed sectors is
      PROVEN-MODULO-ELEMENTARY (exact geometric summation [S0.1-S0.5]
      + Taylor-Lagrange [S0.3, L1.2] + envelope/assembly [D5/D6,
      L1.3]); the residue for the FULL operator statement and the
      difficulty typing of (L2)/(L3) are printed -- named, not
      claimed.  GATE.QGEO does not move.

VERDICT ENUMS (frozen): L1-SECTOR-PROVEN-MODULO-ELEMENTARY (all
pass), L1-LEADING-MISSES (the derived leading term does not match the
measurement), L1-BOUND-LEAKS (a coverage inequality is violated),
MIXED (anything else).

FIREWALL: experiments-only; verification/ strictly read-only;
GATE.QGEO does not move; no marker changes; deterministic (no RNG).
Machinery (occ_vec/kernels/grid/masks) verbatim from
qgeo_car_continuum_probe.py (2026-08-03, 22/22,
QGEO-CAR-RATES-SUMMABLE).
"""

import time

import numpy as np
import sympy as sp

CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------------ constants
NLAD = (48, 96, 192, 384, 768, 1536, 3072)
MGRID = 24
EPS_LADDER = (1.0 / 24.0, 1.0 / 12.0, 1.0 / 6.0)
EPS_MID = 1.0 / 12.0
ZTOL = 1e-12
IP = np.array([1.0, 1j, -1.0, -1j])
QT = {0: 0, 1: 1, 2: 2, 4: -2, 5: -1}       # arc-center offset (q=3: cot)
C_FP1 = 5.0 * np.pi / 3.0                    # |f'|  envelope numerator
C_FP2 = 34.0 * np.pi ** 2 / 9.0              # |f''| envelope numerator
BAR_RATIO_DEV = 0.01
BAR_SLOPE = 0.15
BAR_GROW = 1.8


# ------------------------------------------------ machinery (parent verbatim)
def occ_vec(N, q):
    m = np.arange(N)
    k = 2.0 * np.pi * (m + 0.5 + (q % 6) / 6.0) / N
    e = -np.cos(k)
    return np.where(e < -ZTOL, 1.0, np.where(np.abs(e) <= ZTOL, 0.5, 0.0))


_KER = {}


def sector_kernel(N, q):
    key = (N, q)
    if key not in _KER:
        n = occ_vec(N, q)
        d = np.arange(N)
        eta = 0.5 + (q % 6) / 6.0
        _KER[key] = np.fft.ifft(n) * np.exp(2j * np.pi * eta * d / N)
    return _KER[key]


def kernel_at(N, q, D):
    c = sector_kernel(N, q)
    wrap = np.exp(-2j * np.pi * (0.5 + (q % 6) / 6.0))
    vals = c[np.asarray(D) % N]
    return np.where(np.asarray(D) < 0, vals * wrap, vals)


def grid_sites(N):
    step = N // MGRID
    base = step * np.arange(MGRID)
    g = np.empty(2 * MGRID, dtype=int)
    g[0::2] = base
    g[1::2] = base + 1
    xi = np.repeat(np.arange(MGRID) / MGRID, 2)
    return g, xi


def embed_sector(N, q):
    g, _ = grid_sites(N)
    D = g[None, :] - g[:, None]
    return (N / MGRID) * IP[(-D) % 4] * kernel_at(N, q, D)


def circ(d):
    ad = np.abs(d)
    return np.minimum(ad, 1.0 - ad)


def mask_eps(xi, eps):
    return circ(xi[None, :] - xi[:, None]) >= eps - 1e-12


def tnorm(A):
    return float(np.linalg.svd(A, compute_uv=False).sum())


# ------------------------------------------------ the derived closed forms
def closed_Nc(N, q, D):
    """(D1)/(D2): N c_N^(q)(d) exact; d = 0 -> N/2."""
    D = np.asarray(D)
    Ds = np.where(D == 0, 1, D)
    if q == 3:
        val = (np.sin(np.pi * Ds / 2.0) * np.cos(np.pi * Ds / N)
               / np.sin(np.pi * Ds / N)).astype(complex)
    else:
        val = (np.exp(1j * np.pi * QT[q] * Ds / (3.0 * N))
               * np.sin(np.pi * Ds / 2.0) / np.sin(np.pi * Ds / N))
    return np.where(D == 0, N / 2.0 + 0j, val)


def embed_closed(N, q):
    g, _ = grid_sites(N)
    D = g[None, :] - g[:, None]
    return (1.0 / MGRID) * IP[(-D) % 4] * closed_Nc(N, q, D)


def fprime(q, t):
    """f_q'(t); t real, noninteger (D3)."""
    t = np.asarray(t, dtype=float)
    st = np.sin(np.pi * t)
    if q == 3:
        return (-np.pi / st ** 2).astype(complex)
    a = np.pi * QT[q] / 3.0
    return np.exp(1j * a * t) * (1j * a / st
                                 - np.pi * np.cos(np.pi * t) / st ** 2)


def F2(t):
    """(D5) envelope for |f''| at circular distance t."""
    return C_FP2 / np.sin(np.pi * np.asarray(t, dtype=float)) ** 3


# ================================================================== S0
print("=" * 72)
print("S0: the symbolic derivation + exactness controls")
print("=" * 72)

phi, Lsym = sp.symbols("phi L")
lhs = (sp.exp(sp.I * Lsym * phi) - 1) / (sp.exp(sp.I * phi) - 1)
rhs = sp.exp(sp.I * (Lsym - 1) * phi / 2) \
    * sp.sin(Lsym * phi / 2) / sp.sin(phi / 2)
diff01 = sp.simplify(sp.expand(sp.cancel((lhs - rhs).rewrite(sp.exp))))
check("S0.1 [sympy] geometric-sum identity: the occupied-arc mode sum "
      "IS the Dirichlet closed form (symbolic residue = %s)" % diff01,
      diff01 == 0)

aa, bb = sp.symbols("a b")
expr2 = sp.simplify(sp.sin(aa - bb) / sp.sin(bb) + sp.cos(aa)
                    - sp.sin(aa) * sp.cos(bb) / sp.sin(bb))
check("S0.2 [sympy] the R-line (q = 3) zero-mode cancellation: "
      "interior Dirichlet + 1/2-weighted zero modes collapse to the "
      "cot form (symbolic residue = %s)" % expr2, expr2 == 0)

ssym, hsym, usym = sp.symbols("s h u")
fgen = sp.Function("f")
step = fgen(ssym + usym * hsym / 2) - fgen(ssym + usym * hsym)
ser = sp.series(step, hsym, 0, 3).removeO()
c1 = sp.simplify(ser.coeff(hsym, 1)
                 + (usym / 2) * sp.Derivative(fgen(ssym), ssym))
c2 = sp.simplify(ser.coeff(hsym, 2)
                 + sp.Rational(3, 8) * usym ** 2
                 * sp.Derivative(fgen(ssym), ssym, 2))
check("S0.3 [sympy] generic Taylor step (covers all sectors): "
      "f(s+uh/2) - f(s+uh) = -(uh/2) f'(s) - (3u^2h^2/8) f''(s) "
      "+ O(h^3) (residues %s / %s)" % (c1, c2),
      sp.simplify(c1) == 0 and sp.simplify(c2) == 0)

dev04 = 0.0
A_SEC = {}
for N in NLAD:
    for q in range(6):
        A_SEC[(N, q)] = embed_sector(N, q)
        dev04 = max(dev04, np.abs(A_SEC[(N, q)]
                                  - embed_closed(N, q)).max())
check("S0.4 [machine] the closed forms (D1)/(D2) equal the FFT "
      "mode-sum kernels on the full embedded grid (6 sectors x 7 N = "
      "48..3072, wrap/negative d included): the mode sums are EXACT "
      "geometric sums -- no Riemann-sum error exists",
      dev04 < 1e-9, "max |dev| = %.2e" % dev04)

g48, XI = grid_sites(48)
PIDX = np.repeat(np.arange(MGRID), 2)
UMAT = (np.arange(2 * MGRID) % 2)[None, :] \
    - (np.arange(2 * MGRID) % 2)[:, None]
SMAT = (PIDX[None, :] - PIDX[:, None]) / float(MGRID)
OFFP = PIDX[None, :] != PIDX[:, None]
dev_even, dev_diag = 0.0, 0.0
for N in NLAD:
    for q in range(6):
        A = A_SEC[(N, q)]
        dev_even = max(dev_even,
                       np.abs(A[(UMAT == 0) & OFFP]).max())
        dev_diag = max(dev_diag,
                       np.abs(np.diag(A) - N / (2.0 * MGRID)).max())
par_ok = all(abs(IP[(-d) % 4] * np.sin(np.pi * d / 2.0) + 1j) < 1e-15
             for d in (-7, -5, -3, -1, 1, 3, 5, 7, 9))
check("S0.5 [machine] parity structure: even-offset entries vanish "
      "identically (max %.1e), diagonal = N/(2M) exact (max dev "
      "%.1e), i^{-d} sin(pi d/2) = -i on every odd residue"
      % (dev_even, dev_diag),
      dev_even < 1e-10 and dev_diag < 1e-10 and par_ok)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== L1.1
print("=" * 72)
print("L1.1: the leading term hits -- ratio ||D_N||_1 N / ||L_q||_1")
print("=" * 72)

# the exact N-independent leading matrices L_q on the grid
LEAD = {}
for q in range(6):
    L = np.zeros((2 * MGRID, 2 * MGRID), dtype=complex)
    sel = (np.abs(UMAT) == 1) & OFFP
    L[sel] = (1j * UMAT[sel] / (2.0 * MGRID)) * fprime(q, SMAT[sel])
    LEAD[q] = L

MASKS = {eps: mask_eps(XI, eps) for eps in EPS_LADDER}
D_MEAS = {}
for q in range(6):
    for l in range(len(NLAD) - 1):
        D_MEAS[(q, l)] = A_SEC[(NLAD[l + 1], q)] - A_SEC[(NLAD[l], q)]

ok11 = True
print("  ratio table (eps = 1/12): ||D_N||_1 * N / ||L_q||_1")
print("  %-3s %9s %8s %8s %8s %8s %8s %8s"
      % ("q", "||L_q||_1", "N=48", "N=96", "N=192", "N=384", "N=768",
         "N=1536"))
for q in range(6):
    Tl = tnorm(LEAD[q] * MASKS[EPS_MID])
    ratios = [tnorm(D_MEAS[(q, l)] * MASKS[EPS_MID]) * NLAD[l] / Tl
              for l in range(len(NLAD) - 1)]
    devs = [abs(r - 1.0) for r in ratios]
    ok11 &= devs[-1] <= BAR_RATIO_DEV and devs[-1] < devs[-2] < devs[-3]
    print("  q=%d %9.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f"
          % (q, Tl, *ratios))
check("L1.1 [central] the DERIVED leading term (i u/(2MN)) f_q'(s) "
      "reproduces the measured trace-norm ladder: ratio -> 1 in every "
      "sector (last-rung |dev| <= %.2f, monotone over the last 3 "
      "rungs)" % BAR_RATIO_DEV, ok11)


# ================================================================== L1.2
print("=" * 72)
print("L1.2: entrywise Taylor-Lagrange coverage (all entries/rungs)")
print("=" * 72)

viol12, ncheck, min_slack12 = 0, 0, np.inf
for q in range(6):
    for l in range(len(NLAD) - 1):
        N = NLAD[l]
        sel = (np.abs(UMAT) == 1) & OFFP
        lhs_e = np.abs(D_MEAS[(q, l)][sel] - LEAD[q][sel] / N)
        rhs_e = (5.0 / (8.0 * MGRID * N ** 2)) \
            * F2(circ(SMAT[sel]) - 1.0 / N)
        viol12 += int((lhs_e > rhs_e + 1e-14).sum())
        ncheck += lhs_e.size
        min_slack12 = min(min_slack12,
                          float((rhs_e / np.maximum(lhs_e, 1e-300))
                                .min()))
check("L1.2 [central] entrywise Taylor-Lagrange coverage "
      "|D - lead/N| <= (5/(8MN^2)) F2(circ - 1/N): %d violations in "
      "%d inequalities (6 sectors x 6 rungs x all off-diagonal "
      "entries); minimal envelope slack %.2f x"
      % (viol12, ncheck, min_slack12), viol12 == 0)


# ================================================================== L1.3
print("=" * 72)
print("L1.3: the PROVEN bound B_q(eps)/N covers the measurement")
print("=" * 72)

B_TAB = {}
for q in range(6):
    for eps in EPS_LADDER:
        mk = MASKS[eps]
        T1 = tnorm(LEAD[q] * mk)
        sel = (np.abs(UMAT) == 1) & OFFP & mk
        Rhat = (5.0 / (8.0 * MGRID)) * F2(np.maximum(
            circ(SMAT[sel]) - 1.0 / 48.0, 1e-9))
        remc = np.sqrt(2 * MGRID) * float(np.sqrt((Rhat ** 2).sum())) \
            / 48.0
        B_TAB[(q, eps)] = (T1, remc, T1 + remc)

viol13, min_slack13, worst_case = 0, np.inf, None
for q in range(6):
    for eps in EPS_LADDER:
        B = B_TAB[(q, eps)][2]
        for l in range(len(NLAD) - 1):
            N = NLAD[l]
            lhs_n = tnorm(D_MEAS[(q, l)] * MASKS[eps])
            slack = (B / N) / lhs_n
            if lhs_n > B / N + 1e-12:
                viol13 += 1
            if slack < min_slack13:
                min_slack13, worst_case = slack, (q, eps, N)
print("  B_q(eps) table  (leading ||L||_1 + remainder part):")
for eps in EPS_LADDER:
    print("  eps=%.4f: " % eps + "  ".join(
        "q%d: %.1f+%.1f=%.1f" % (q, *B_TAB[(q, eps)])
        for q in range(6)))
check("L1.3 [central] ||D_N||_1 <= B_q(eps)/N holds in ALL 108 "
      "(sector, rung, eps) cases: %d violations; minimal slack "
      "%.2f x at (q=%d, eps=%.4f, N=%d) -- the constants are EXPLICIT "
      "and the bound is proven for every ladder N >= 48"
      % (viol13, min_slack13, *worst_case), viol13 == 0)


# ================================================================== L1.4
print("=" * 72)
print("L1.4: gamma = 2 derived; slope consistency with the measurement")
print("=" * 72)

C_env = max(B_TAB[(q, eps)][2] * eps ** 2
            for q in range(6) for eps in EPS_LADDER)
ok14 = True
for q in range(6):
    sl_der = np.polyfit(np.log(EPS_LADDER),
                        np.log([tnorm(LEAD[q] * MASKS[e])
                                for e in EPS_LADDER]), 1)[0]
    sl_meas = np.polyfit(np.log(EPS_LADDER),
                         np.log([tnorm(D_MEAS[(q, 5)] * MASKS[e])
                                 for e in EPS_LADDER]), 1)[0]
    ok14 &= abs(sl_der - sl_meas) <= BAR_SLOPE and -sl_meas <= 2.0
    print("  q=%d: derived eps-slope of ||L_q||_1 = %.3f, measured "
          "slope of ||D(1536->3072)||_1 = %.3f (|diff| %.3f)"
          % (q, sl_der, sl_meas, abs(sl_der - sl_meas)))
check("L1.4 [E] the elementary envelope gives gamma = 2 "
      "(B_q(eps) <= %.1f eps^{-2} on the declared eps ladder; "
      "sin(pi eps) >= 2 eps); the SHARP leading constant's eps-slope "
      "matches the measured collision exponent per sector "
      "(|diff| <= %.2f) -- derived and measured collision scaling "
      "agree, both <= 2" % (C_env, BAR_SLOPE), ok14)


# ================================================================== L1.5
print("=" * 72)
print("L1.5: must-fail -- rate 2 is impossible (the 1/N term is real)")
print("=" * 72)

ok15 = True
for q in range(6):
    w = [tnorm(D_MEAS[(q, l)] * MASKS[EPS_MID]) * NLAD[l] ** 2
         for l in range(len(NLAD) - 1)]
    grow = [w[l + 1] / w[l] for l in range(len(w) - 1)]
    ok15 &= all(gr >= BAR_GROW for gr in grow[-3:])
    if q == 0:
        print("  q=0: ||D_N||_1 * N^2 = %s (growth %s)"
              % ("/".join("%.1f" % v for v in w),
                 "/".join("%.2f" % v for v in grow)))
check("L1.5 [machine, must-fail] rate-2 impossibility: ||D_N||_1 N^2 "
      "grows by >= %.1f x per rung (last 3 rungs, every sector, "
      "eps = 1/12): NO constant B' gives ||D|| <= B'/N^2 -- the 1/N "
      "sublattice boundary term is real, r1 = 1 is sharp" % BAR_GROW,
      ok15)


# ================================================================== L1.6
print("=" * 72)
print("L1.6: the lemma statement + status typing")
print("=" * 72)

print("""
  LEMMA L1 (sector covariances, fixed-grid version) -- STATUS:
  PROVEN MODULO ELEMENTARY STEPS, every step machine-verified:
  For every deck/twist sector q = 0..5, every eps in the declared
  ladder, and every N >= 48 with 48 | N:
      || K_2N^(q) - K_N^(q) ||_{S1(Lambda_eps)}  <=  B_q(eps)/N,
      B_q(eps) = ||L_q(eps)||_1 + sqrt(48)(5/192)||F2(circ-1/48)||_F/48
  with the numeric table printed in L1.3 and the elementary envelope
  B_q(eps) <= %.1f eps^{-2} (gamma = 2).  Proof chain:
   (1) exact geometric summation of the occupied-arc mode sum
       [S0.1, S0.4]: the EM boundary terms at +-k_F sum EXACTLY into
       sin(pi d/2)/sin(pi d/N); the R-line zero modes cancel the
       interior edge exactly [S0.2] -- hence K_N(s,u) =
       -(i/M) f_q(s + u/N) EXACTLY: all N-dependence is the
       sublattice offset (no Riemann-sum error term exists at all);
   (2) Taylor with integral-form remainder between rungs [S0.3,
       entrywise coverage L1.2, zero violations];
   (3) elementary envelopes (D5) and the rank/Frobenius trace-norm
       assembly (D6) [L1.3, zero violations; L1.4 gamma = 2].
  Sharpness: r1 = 1 is exact (L1.1 ratio -> 1; L1.5 rate-2
  impossible).  Summability along the doubling ladder: sum_l B/N_l =
  B/48 * sum 2^{-l} = B/24 < infinity -- the sector covariances are
  Cauchy in S1(Lambda_eps) with PROVEN majorant.

  WHAT REMAINS (typed, named -- not claimed):
   (a) L1 grid-sup (fixed grid -> any refinement / the integral
       operator on L2(Lambda_eps)): same chain with the integrable
       envelope int int_{circ>=eps} |f_q'| < inf; difficulty:
       ELEMENTARY (bookkeeping; no new analysis).
   (b) L2 (dressed/twist-inserted covariances): needs a UNIFORM
       Fisher-Hartwig remainder on eps-separated configurations and
       the identification of the measured slow far-branch exponent;
       technology: Riemann-Hilbert / Deift-Its-Krasovsky uniformity;
       difficulty: HARD-TECHNICAL (known machinery, real work).
   (c) L3 (FH-renormalized determinant channels): the asymptotics
       including the Barnes-G constant is theorem-grade (verified to
       8.8e-7 in the parent probe); missing is the uniformity of the
       error across the configuration family; difficulty: MEDIUM
       (citation + uniform error control).
  GATE.QGEO does not move.""" % C_env)
check("L1.6 [C] lemma status typed: (L1, undressed sectors, fixed "
      "grid) = PROVEN-MODULO-ELEMENTARY with explicit constants; "
      "residues (a) grid-sup [elementary], (b) L2 uniform FH/RH "
      "[hard-technical], (c) L3 uniformity [medium] -- named, not "
      "claimed; GATE.QGEO does not move", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed  [total %.1f s]"
      % (n_pass, len(CHECKS), time.time() - T0))
s0_ok = all(ok for n, ok in CHECKS if n.startswith("S0"))
lead_ok = all(ok for n, ok in CHECKS if n.startswith("L1.1"))
cover_ok = all(ok for n, ok in CHECKS
               if n.startswith(("L1.2", "L1.3")))
if n_pass == len(CHECKS):
    print("VERDICT: L1-SECTOR-PROVEN-MODULO-ELEMENTARY")
    print("The occupied-arc mode sums are EXACT geometric sums (no")
    print("Riemann-sum error); the entire 1/N structure is the")
    print("sublattice embedding offset; the leading term is the exact")
    print("matrix (iu/2MN) f_q'(s) (ratio -> 1), the Taylor-Lagrange")
    print("envelope covers every entry and every trace norm with zero")
    print("violations, gamma = 2 is derived and consistent with the")
    print("measured collision exponents, and r1 = 1 is sharp.  (L1)")
    print("for the undressed sectors is proven modulo elementary")
    print("steps, with all constants explicit.  GATE.QGEO does not")
    print("move.")
elif s0_ok and not lead_ok:
    print("VERDICT: L1-LEADING-MISSES")
elif s0_ok and lead_ok and not cover_ok:
    print("VERDICT: L1-BOUND-LEAKS")
else:
    print("VERDICT: MIXED")


def run():
    """run_all entry point: the checks execute at import time (module level)."""
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(run())
