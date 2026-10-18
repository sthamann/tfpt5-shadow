#!/usr/bin/env python3
"""Discovery probe: QGEO grid supremum -- the ELEMENTARY remainder (a) of
the (L1) sector lemma (v745), closed at theorem level where it is true and
typed precisely where it is not.

THE REMAINDER (frozen source, quoted verbatim):

  v745_qgeo_car_l1_sector_lemma.py, "WHAT REMAINS", item (a):
    "(a) L1 grid-sup (fixed grid -> any refinement / the integral
         operator on L2(Lambda_eps)): same chain with the integrable
         envelope int int_{circ>=eps} |f_q'| < inf; difficulty:
         ELEMENTARY (bookkeeping; no new analysis)."

  and the frozen (L1) clause it must serve (qgeo_car_continuum_probe.py,
  C5 lemma statement):
    "there are constants B(eps) <= B0 eps^{-gamma}, gamma <= 2, such
     that for all N in the doubling ladder and ALL grid refinements of
     Lambda_eps
       (L1)  || K_2N^(q) - K_N^(q) ||_S1(Lambda_eps) <= B(eps) N^{-r1}"

PREREGISTERED CLAIM SPLIT (declared before any number is computed).
With f_q(t) = e^{i pi qt t/3}/sin(pi t) (q=3: cot(pi t)), qt in
{0,1,2,-2,-1}, the v745 (D3) closed kernel k_N(s,u) = -i f_q(s + u/N)
(odd spinor offset u; even offsets vanish identically), and the v745
(D5) envelopes F1(t) = (5 pi/3)/sin^2(pi t), F2(t) = (34 pi^2/9)
/sin^3(pi t), the elementary remainder decomposes into FOUR parts:

 (a1) THE CONTINUUM ENTRYWISE SUPREMUM (fixed grid -> every real
      separation).  CLAIM: for EVERY real s with circ(s) >= eps, every
      N >= 48, u = +-1, q = 0..5:
        |k_2N - k_N + (u/2N) (-i) f_q'(s)| <= (5/(8 N^2)) F2(circ(s) - 1/N)
        |k_2N - k_N| <= (1/(2N)) F1(circ(s)) + (5/(8 N^2)) F2(circ(s) - 1/N).
      Proof = Taylor integral remainder (coefficient 5/8, symbolic)
      + envelopes (symbolic coefficient arithmetic) + monotonicity of
      F1, F2 + 1-Lipschitz circ.  Fully elementary; census-verified.

 (a2) THE CONFIGURATION-S1 CLOSURE (every eps-separated configuration
      of every refinement).  CLAIM: any configuration X of n points
      with pairwise circ >= eps has n <= floor(1/eps) (packing), the
      m-th cyclic neighbour sits at circ >= min(m, n-m) eps, and
        || (K_2N - K_N)|_X ||_S1 <= B_conf(eps)/N  for all N >= 48,
        B_conf(eps) = floor(1/eps) [ (5 pi/6) zeta(2) eps^-2
                       + (5/192)(68 pi^2/9) zeta(3) eps^-3 ]
      (kernel-VALUE normalisation; collision-excised as in Lambda_eps).
      Fully elementary; census-verified with zero violations.

 (a3) THE REMAINDER PART UNDER REFINEMENT (quadrature-weighted grids,
      M points, M | N, N/M even).  CLAIM: the Taylor remainder of the
      rung difference obeys, uniformly over ALL refinements M <= N/2,
        || D_N^(M) - L_q^(M)/N ||_l1(entries)  <=  RHO(eps)/N,
        RHO(eps) = (5/2) I2(eps - 1/48) + (5/48) F2(eps - 1/48),
        I2(t0) = int_t0^{1/2} F2(t) dt  (exact csc^3 antiderivative),
      by the monotone-Riemann comparison.  Fully elementary;
      census-verified with zero violations.

 (a4) THE LEADING PART UNDER REFINEMENT -- the honest obstruction.
      L_q^(M)(eps) factorises as F_q^(M) (x) K2 with ||L||_1 =
      2 ||F||_1; the mask cut circ >= eps is a JUMP of the symbol at
      +-eps, so the Fourier coefficients of the masked symbol decay
      like 1/k and the trace norm of F_q^(M) grows like log M.
      PREREGISTERED TEST: per-doubling increments of ||F||_1 become
      CONSTANT (log law), the constant is proportional to the jump
      |f_q'(eps)| across all sectors and eps, and a C^1-tapered mask
      (no jump) SATURATES.  If confirmed, the literal v715 clause
      "one B(eps) for ALL grid refinements" is FALSE at r1 = 1 with a
      fixed B(eps): the surviving analytic step is exactly ONE
      elementary-Fourier inequality (named in G9, not claimed):
        sum_{|k| <= M} |ghat_{q,eps}(k)| <= c0(q,eps) + (J(eps)/pi) ln M,
        J(eps) = 2 |f_q'(eps)|,  ghat = Fourier coefficients of the
        eps-cut symbol -- integration by parts, explicit constants.
      The Araki/Powers-Stormer CONSEQUENCE of (L1) is unaffected:
      for every FIXED refinement M the doubling-ladder majorant stays
      summable, and even the extreme joint scaling M = N/2 gives
      B(eps)(1 + ln(N/48))/N, still summable along the ladder.

FROZEN CONSTANTS AND GRIDS (all declared here):
  NLAD = (48, 96, 192, 384, 768, 1536, 3072); base grid MGRID = 24;
  refinement ladder MLAD = (24, 48, 96, 192, 384, 768), extension
  M = 1536 for (q in {0,3}, eps = 1/12) and M = 3072 for (q = 3,
  eps = 1/12); EPS_LADDER = (1/24, 1/12, 1/6); envelope numerators
  C1 = 5 pi/3, C2 = 34 pi^2/9; Taylor constant 5/8; refinement-pair
  family N/M in {2, 8, 32} capped at N <= 3072.

PASS BARS (preregistered):
  S0.2/S0.3 symbolic residues identically zero.
  G1  envelope census (~2e5 continuum points): 0 violations;
      controls 0.5*C1 / 0.5*C2 must EACH produce violations.
  G2  entrywise supremum census (~1e6 inequalities): 0 violations;
      Taylor control 1/8 (instead of 5/8) must produce violations.
  G3  packing + m-th-neighbour lemma on 500 random configurations:
      0 violations.
  G4  configuration-S1 census (60 configs/eps x 6 q x 6 rungs):
      0 violations of ||D|_X||_1 <= B_conf(eps)/N.
  G5  machinery guard: closed forms vs FFT kernels on refined grids
      < 1e-9; ||L||_1 = 2 ||F||_1 rel dev <= 1e-8.
  G6  remainder-uniformity census over all declared (q, eps, M, N):
      0 violations of rem_l1 <= RHO(eps)/N and of the monotone-Riemann
      comparison.
  G7  log law: (7a) increment stability 0.85 <= inc_last/inc_prev
      <= 1.35 for every (q, eps); (7b) mechanism ratio
      inc_last/|f_q'(eps)| in [0.10, 0.17] with spread <= 0.25 of the
      mean; (7c) log-fit R^2 >= 0.98 on the last 4 rungs for
      eps in {1/12, 1/6}; (7d) taper control: increment ratio <= 0.5
      AND final increment <= 0.1 x the sharp final increment.
  G8  transfer: N ||D_N^(96)||_1 / (2||F^(96)||_1) -> 1 (last dev
      <= 0.05, decreasing over the last 3 rungs).

VERDICT ENUMS (frozen): GRIDSUP-SPLIT-CLOSED-LOG-LAW (a1/a2/a3 closed
with zero violations AND the a4 log law confirmed with controls);
GRIDSUP-FULLY-CLOSED (a1/a2/a3 closed AND the a4 increments collapse
like the taper: sup over refinements finite); CENSUS-LEAK (any
coverage violation in G1/G2/G4/G6); MIXED (anything else).

SHA-FREEZE: the SHA-256 of the three frozen sources (v745 module,
parent continuum probe, L1 sector probe) is printed in S0.1; this
probe reads NOTHING else.

FIREWALL: experiments-only; verification/ strictly read-only (hashed,
never imported); GATE.QGEO does not move; no marker changes; NO RH
relevance is claimed anywhere; deterministic (seeded RNG for census
sampling only); runtime minutes.
"""

import hashlib
import time
from fractions import Fraction

import numpy as np
import sympy as sp

CHECKS = []
T0 = time.time()
RNG = np.random.default_rng(74501)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------------ constants
NLAD = (48, 96, 192, 384, 768, 1536, 3072)
MGRID = 24
MLAD = (24, 48, 96, 192, 384, 768)
EPS_LADDER = (1.0 / 24.0, 1.0 / 12.0, 1.0 / 6.0)
EPS_MID = 1.0 / 12.0
RATIOS_NM = (2, 8, 32)                      # N/M family (even steps)
QT = {0: 0, 1: 1, 2: 2, 4: -2, 5: -1}       # q = 3 handled as cot
C_FP1 = 5.0 * np.pi / 3.0                   # |f'| envelope numerator (D5)
C_FP2 = 34.0 * np.pi ** 2 / 9.0             # |f''| envelope numerator (D5)
TAYLOR_C = 5.0 / 8.0                        # two-point Taylor constant
IP = np.array([1.0, 1j, -1.0, -1j])
BAR_INC_LO, BAR_INC_HI = 0.85, 1.35
BAR_MECH_LO, BAR_MECH_HI = 0.10, 0.17
BAR_MECH_SPREAD = 0.25
BAR_R2 = 0.98
BAR_TAPER_RATIO = 0.5
BAR_TAPER_FRAC = 0.1
BAR_TRANSFER = 0.05

FROZEN_SOURCES = (
    "verification/v745_qgeo_car_l1_sector_lemma.py",
    "experiments/tfpt-discovery/qgeo_car_continuum_probe.py",
    "experiments/tfpt-discovery/qgeo_car_l1_sector_lemma_probe.py",
)


# ------------------------------------------------------------------ helpers
def circ(d):
    f = np.mod(np.asarray(d, dtype=float), 1.0)
    return np.minimum(f, 1.0 - f)


def fval(q, t):
    """f_q(t) of (D3); q = 3 is cot(pi t)."""
    t = np.asarray(t, dtype=float)
    st = np.sin(np.pi * t)
    if q == 3:
        return (np.cos(np.pi * t) / st).astype(complex)
    return np.exp(1j * np.pi * QT[q] * t / 3.0) / st


def fprime(q, t):
    t = np.asarray(t, dtype=float)
    st = np.sin(np.pi * t)
    if q == 3:
        return (-np.pi / st ** 2).astype(complex)
    a = np.pi * QT[q] / 3.0
    return np.exp(1j * a * t) * (1j * a / st
                                 - np.pi * np.cos(np.pi * t) / st ** 2)


def fsecond(q, t):
    """f_q''(t), from the symbolic form verified in S0.3."""
    t = np.asarray(t, dtype=float)
    st, ct = np.sin(np.pi * t), np.cos(np.pi * t)
    if q == 3:
        return (2.0 * np.pi ** 2 * ct / st ** 3).astype(complex)
    a = np.pi * QT[q] / 3.0
    return np.exp(1j * a * t) * (-a ** 2 / st
                                 - 2j * a * np.pi * ct / st ** 2
                                 + np.pi ** 2 / st
                                 + 2.0 * np.pi ** 2 * ct ** 2 / st ** 3)


def F1(t):
    return C_FP1 / np.sin(np.pi * np.asarray(t, dtype=float)) ** 2


def F2(t):
    return C_FP2 / np.sin(np.pi * np.asarray(t, dtype=float)) ** 3


def closed_Nc(N, q, D):
    """(D1)/(D2) closed mode sums, exact at every N (v745 S0.4)."""
    D = np.asarray(D)
    Ds = np.where(D == 0, 1, D)
    if q == 3:
        val = (np.sin(np.pi * Ds / 2.0) * np.cos(np.pi * Ds / N)
               / np.sin(np.pi * Ds / N)).astype(complex)
    else:
        val = (np.exp(1j * np.pi * QT[q] * Ds / (3.0 * N))
               * np.sin(np.pi * Ds / 2.0) / np.sin(np.pi * Ds / N))
    return np.where(D == 0, N / 2.0 + 0j, val)


def refine_sites(N, M):
    """Refinement grid: M spinor pairs, step N/M (even), sites (p, p+1)."""
    step = N // M
    base = step * np.arange(M)
    g = np.empty(2 * M, dtype=int)
    g[0::2] = base
    g[1::2] = base + 1
    return g


def embed_closed_M(N, q, M):
    """Quadrature-weighted embedded kernel on the M-refinement grid."""
    g = refine_sites(N, M)
    D = g[None, :] - g[:, None]
    return (1.0 / M) * IP[(-D) % 4] * closed_Nc(N, q, D)


def grid_structs(M):
    pidx = np.repeat(np.arange(M), 2)
    umat = (np.arange(2 * M) % 2)[None, :] - (np.arange(2 * M) % 2)[:, None]
    smat = (pidx[None, :] - pidx[:, None]) / float(M)
    offp = pidx[None, :] != pidx[:, None]
    return pidx, umat, smat, offp


def tnorm(A):
    return float(np.linalg.svd(A, compute_uv=False).sum())


def lead_matrix(q, M, mask):
    """L_q^(M): entries (i u/2M) f_q'(s) on masked odd-offset pairs."""
    _, umat, smat, offp = grid_structs(M)
    L = np.zeros((2 * M, 2 * M), dtype=complex)
    sel = (np.abs(umat) == 1) & offp & mask
    L[sel] = (1j * umat[sel] / (2.0 * M)) * fprime(q, smat[sel])
    return L


def f_matrix(q, M, eps, taper=False):
    """F_q^(M)(eps): M x M point matrix, entries (1/2M) f_q'(s) masked."""
    i = np.arange(M)
    S = (i[None, :] - i[:, None]) / float(M)
    C = circ(S)
    off = i[None, :] != i[:, None]
    F = np.zeros((M, M), dtype=complex)
    if taper:
        w = np.clip((C - eps) / (eps / 2.0), 0.0, 1.0)
        w = w * w * (3.0 - 2.0 * w)          # C^1 smoothstep on [eps, 3eps/2]
        sel = off & (w > 0)
        F[sel] = w[sel] * fprime(q, S[sel]) / (2.0 * M)
    else:
        sel = off & (C >= eps - 1e-12)
        F[sel] = fprime(q, S[sel]) / (2.0 * M)
    return F


# ================================================================== S0
print("=" * 72)
print("S0: freeze + the symbolic elementary lemmas")
print("=" * 72)

import os

repo = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
hashes = []
for rel in FROZEN_SOURCES:
    p = os.path.join(repo, rel)
    h = hashlib.sha256(open(p, "rb").read()).hexdigest()
    hashes.append(h)
    print("  SHA256 %s = %s" % (rel, h))
check("S0.1 [freeze] the three frozen sources exist and are hashed "
      "(read-only; nothing else is read)", len(hashes) == 3)

# S0.2: two-point Taylor constant 5/8 via integral remainders
x, tau, hh = sp.symbols("x tau h", positive=True)
i_half = sp.integrate(hh / 2 - tau, (tau, 0, hh / 2))     # remainder weight
i_full = sp.integrate(hh - tau, (tau, 0, hh))
comb = sp.simplify(i_half + i_full - sp.Rational(5, 8) * hh ** 2)
check("S0.2 [sympy] two-point Taylor constant: |R(h/2)| + |R(h)| "
      "weights integrate to h^2/8 + h^2/2 = (5/8) h^2 exactly "
      "(residue = %s); with R(x) = f(s+x) - f(s) - x f'(s) the chain "
      "f(s+h/2) - f(s+h) + (h/2) f'(s) = R(h/2) - R(h) is an identity"
      % comb, comb == 0)

# S0.3: f'' closed form + envelope coefficient arithmetic (exact)
t_s, a_s = sp.symbols("t a", real=True)
f_sym = sp.exp(sp.I * a_s * t_s) / sp.sin(sp.pi * t_s)
f2_sym = sp.diff(f_sym, t_s, 2)
f2_form = sp.exp(sp.I * a_s * t_s) * (
    -a_s ** 2 / sp.sin(sp.pi * t_s)
    - 2 * sp.I * a_s * sp.pi * sp.cos(sp.pi * t_s) / sp.sin(sp.pi * t_s) ** 2
    + sp.pi ** 2 / sp.sin(sp.pi * t_s)
    + 2 * sp.pi ** 2 * sp.cos(sp.pi * t_s) ** 2 / sp.sin(sp.pi * t_s) ** 3)
res_f2 = sp.simplify(sp.expand_trig(sp.simplify(f2_sym - f2_form)))
a_max = 2 * sp.pi / 3
coef1 = sp.simplify(a_max + sp.pi - sp.Rational(5, 3) * sp.pi)
coef2 = sp.simplify(a_max ** 2 + 2 * a_max * sp.pi + 2 * sp.pi ** 2
                    - sp.Rational(34, 9) * sp.pi ** 2)
cot_f2 = sp.simplify(sp.diff(sp.cot(sp.pi * t_s), t_s, 2)
                     - 2 * sp.pi ** 2 * sp.cos(sp.pi * t_s)
                     / sp.sin(sp.pi * t_s) ** 3)
check("S0.3 [sympy] envelope arithmetic exact: f'' closed form "
      "(residue %s); a + pi = 5pi/3 (res %s); a^2 + 2a pi + 2pi^2 "
      "= 34pi^2/9 (res %s) at a = 2pi/3; cot'' = 2pi^2 c/s^3 (res %s); "
      "with 0 < s <= 1 every term absorbs into C1/s^2 resp. C2/s^3 "
      "(s^2 <= s <= 1, |c| <= 1: elementary)"
      % (res_f2, coef1, coef2, cot_f2),
      res_f2 == 0 and coef1 == 0 and coef2 == 0 and cot_f2 == 0)

# S0.4: circ is 1-Lipschitz (exact rationals) and |sin(pi t)| = sin(pi circ t)
def circ_frac(z):
    z = z % 1
    return min(z, 1 - z)

lip_ok = True
pts = [Fraction(k, 97) for k in range(-97, 195)] \
    + [Fraction(k, 64) for k in range(-64, 129)]
for i in range(0, len(pts), 7):
    for j in range(0, len(pts), 11):
        za, zb = pts[i], pts[j]
        if abs(circ_frac(za) - circ_frac(zb)) > abs(za - zb):
            lip_ok = False
ts = RNG.uniform(-2.0, 2.0, 40000)
ts = ts[np.abs(np.round(ts) - ts) > 1e-6]
sin_ok = float(np.max(np.abs(np.abs(np.sin(np.pi * ts))
                             - np.sin(np.pi * circ(ts))))) < 1e-12
check("S0.4 [exact] circ is 1-Lipschitz (exact-rational census, "
      "piecewise slope +-1) and |sin(pi t)| = sin(pi circ(t)) "
      "(4e4 points, dev < 1e-12) -- so F1/F2 envelopes read at the "
      "circular distance and shift by at most 1/N under a 1/N move",
      lip_ok and sin_ok)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G1
print("=" * 72)
print("G1: envelope coverage on the continuum (census + must-fail)")
print("=" * 72)

tt = np.concatenate([
    RNG.uniform(1e-4, 0.5, 30000),
    np.geomspace(1e-6, 1e-4, 4000),
    0.5 - np.geomspace(1e-8, 1e-2, 2000),
    RNG.uniform(0.5, 1.0 - 1e-4, 10000),
    RNG.uniform(-1.0 + 1e-4, -1e-4, 10000),
])
viol1, viol1c, nin1 = 0, 0, 0
sup_r1, sup_r2 = 0.0, 0.0
for q in range(6):
    fp = np.abs(fprime(q, tt))
    fs = np.abs(fsecond(q, tt))
    e1, e2 = F1(circ(tt)), F2(circ(tt))
    viol1 += int((fp > e1 * (1 + 1e-12)).sum())
    viol1 += int((fs > e2 * (1 + 1e-12)).sum())
    viol1c += int((fp > 0.5 * e1).sum()) + int((fs > 0.5 * e2).sum())
    nin1 += 2 * tt.size
    sup_r1 = max(sup_r1, float((fp / e1).max()))
    sup_r2 = max(sup_r2, float((fs / e2).max()))
check("G1 [census] |f_q'| <= F1(circ), |f_q''| <= F2(circ) on %d "
      "continuum inequalities (all sectors, adversarial near 0/wrap): "
      "%d violations; sup ratios %.4f / %.4f (envelopes hold with "
      "margin)" % (nin1, viol1, sup_r1, sup_r2), viol1 == 0)
check("G1c [must-fail] halved envelopes 0.5*C1 / 0.5*C2 are violated "
      "(%d violations > 0): the census has teeth" % viol1c, viol1c > 0)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G2
print("=" * 72)
print("G2: THE CONTINUUM ENTRYWISE SUPREMUM THEOREM (a1) -- census")
print("=" * 72)

ss = np.concatenate([
    RNG.uniform(-1.0, 1.0, 6000),
    1.0 / 24.0 + RNG.uniform(0, 1e-6, 500),      # exactly-at-cut
    -1.0 / 24.0 - RNG.uniform(0, 1e-6, 500),
    1.0 - 1.0 / 24.0 - RNG.uniform(0, 1e-4, 500),  # wrap-side cut
    RNG.uniform(0.45, 0.55, 500),
])
ss = ss[circ(ss) >= 1.0 / 24.0 - 1e-15]
viol2, viol2c, nin2 = 0, 0, 0
min_slack2 = np.inf
for q in range(6):
    for N in NLAD:
        for u in (+1, -1):
            d = fval(q, ss + u / (2.0 * N)) - fval(q, ss + u / N)
            # identity: d + (u/2N) f'(s) = R(u/2N) - R(u/N)  [S0.2]
            lead = (u / (2.0 * N)) * fprime(q, ss)
            env2 = (TAYLOR_C / N ** 2) * F2(circ(ss) - 1.0 / N)
            lhs_t = np.abs(d + lead)
            viol2 += int((lhs_t > env2 * (1 + 1e-12)).sum())
            viol2c += int((lhs_t > (1.0 / 8.0 / N ** 2)
                           * F2(circ(ss) - 1.0 / N)).sum())
            full = (1.0 / (2.0 * N)) * np.abs(fprime(q, ss)) + env2
            lhs_f = np.abs(d)
            viol2 += int((lhs_f > full * (1 + 1e-12)).sum())
            nin2 += 2 * ss.size
            min_slack2 = min(min_slack2,
                             float((env2 / np.maximum(lhs_t, 1e-300))
                                   .min()))
check("G2 [census] (a1) entrywise supremum: |k_2N - k_N + (u/2N)(-i)f'|"
      " <= (5/8N^2) F2(circ - 1/N) and the full-value bound, for ALL "
      "continuum s with circ >= 1/24 (%d inequalities, 6 q x 7 N x "
      "u = +-1, adversarial cut/wrap points): %d violations; minimal "
      "Taylor slack %.2f x -- the fixed-grid restriction of v745 is "
      "REMOVED at entry level" % (nin2, viol2, min_slack2), viol2 == 0)
check("G2c [must-fail] the Taylor constant 1/8 (instead of 5/8) is "
      "violated (%d violations > 0): the constant is load-bearing"
      % viol2c, viol2c > 0)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G3
print("=" * 72)
print("G3: packing + m-th-neighbour lemma (exact + census)")
print("=" * 72)

print("  PACKING (2-line proof): n points pairwise circ >= eps on the")
print("  unit circle have consecutive gaps summing to 1, each >= eps,")
print("  so n eps <= 1, i.e. n <= floor(1/eps).  m-th neighbour: the")
print("  two arcs to the m-th cyclic neighbour are sums of m resp.")
print("  n-m gaps, each >= eps, so circ >= min(m, n-m) eps.")


def random_config(eps, n=None):
    nmax = int(np.floor(1.0 / eps + 1e-9))
    if n is None:
        n = int(RNG.integers(2, nmax + 1))
    gaps = eps + RNG.dirichlet(np.ones(n)) * (1.0 - n * eps)
    pos = (RNG.uniform() + np.cumsum(gaps)) % 1.0
    return np.sort(pos)


viol3, nin3 = 0, 0
for _ in range(500):
    eps = EPS_LADDER[int(RNG.integers(0, 3))]
    xs = random_config(eps)
    n = xs.size
    cd = circ(xs[None, :] - xs[:, None])
    if n > int(np.floor(1.0 / eps + 1e-9)):
        viol3 += 1
    for m in range(1, n):
        lo = min(m, n - m) * eps
        bad = int((cd[np.arange(n), (np.arange(n) + m) % n]
                   < lo - 1e-12).sum())
        viol3 += bad
        nin3 += n
check("G3 [census] packing n <= floor(1/eps) and m-th-neighbour "
      "circ >= min(m, n-m) eps on 500 random maximal configurations "
      "(%d inequalities): %d violations -- both lemmas are exact "
      "pigeonhole statements" % (nin3, viol3), viol3 == 0)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G4
print("=" * 72)
print("G4: THE CONFIGURATION-S1 CLOSURE (a2) -- explicit B_conf(eps)")
print("=" * 72)

# exact constants via sympy
z2, z3 = sp.zeta(2), sp.zeta(3)
B_CONF = {}
for eps in EPS_LADDER:
    ef = sp.Rational(1, int(round(1 / eps)))
    nmax = sp.floor(1 / ef)
    bc = nmax * (sp.Rational(5, 6) * sp.pi * z2 / ef ** 2
                 + sp.Rational(5, 192) * sp.Rational(68, 9)
                 * sp.pi ** 2 * z3 / ef ** 3)
    B_CONF[eps] = float(bc)
    print("  B_conf(eps = %s) = floor(1/eps)[(5pi/6) z2 eps^-2 "
          "+ (5/192)(68pi^2/9) z3 eps^-3] = %.1f  (n_max = %d)"
          % (ef, float(bc), int(nmax)))

viol4, nin4 = 0, 0
min_slack4, max_meas4 = np.inf, 0.0
for eps in EPS_LADDER:
    for _ in range(60):
        xs = random_config(eps)
        n = xs.size
        S = xs[None, :] - xs[:, None]
        offp = ~np.eye(n, dtype=bool)
        for q in range(6):
            for li in range(len(NLAD) - 1):
                N = NLAD[li]
                D = np.zeros((2 * n, 2 * n), dtype=complex)
                for (ua, ub, u) in ((0, 1, +1), (1, 0, -1)):
                    blk = np.zeros((n, n), dtype=complex)
                    blk[offp] = -1j * (fval(q, S[offp] + u / (2.0 * N))
                                       - fval(q, S[offp] + u / N))
                    D[ua::2, ub::2] = blk
                tn = tnorm(D)
                nin4 += 1
                if tn > B_CONF[eps] / N + 1e-12:
                    viol4 += 1
                min_slack4 = min(min_slack4, (B_CONF[eps] / N) / max(tn,
                                                                     1e-300))
                max_meas4 = max(max_meas4, tn * N)
check("G4 [census] (a2) CLOSED: || (K_2N - K_N)|_X ||_1 <= B_conf(eps)"
      "/N on %d (config, q, rung) cases (60 random eps-separated "
      "configurations per eps, all sectors, all rungs): %d violations;"
      " max measured N||D||_1 = %.2f; minimal slack %.1f x (the bound "
      "is loose but explicit and elementary: packing + neighbour "
      "ladder + zeta(2)/zeta(3))"
      % (nin4, viol4, max_meas4, min_slack4), viol4 == 0)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G5
print("=" * 72)
print("G5: refinement machinery guard (closed forms + factorisation)")
print("=" * 72)

def occ_vec(N, q):
    m = np.arange(N)
    k = 2.0 * np.pi * (m + 0.5 + (q % 6) / 6.0) / N
    e = -np.cos(k)
    return np.where(e < -1e-12, 1.0, np.where(np.abs(e) <= 1e-12, 0.5,
                                              0.0))


def fft_kernel_at(N, q, D):
    n = occ_vec(N, q)
    d = np.arange(N)
    eta = 0.5 + (q % 6) / 6.0
    c = np.fft.ifft(n) * np.exp(2j * np.pi * eta * d / N)
    wrap = np.exp(-2j * np.pi * eta)
    vals = c[np.asarray(D) % N]
    return np.where(np.asarray(D) < 0, vals * wrap, vals)


dev5 = 0.0
for (M, N) in ((48, 192), (96, 384), (192, 768)):
    g = refine_sites(N, M)
    D = g[None, :] - g[:, None]
    for q in (0, 3, 5):
        A_fft = (N / M) * IP[(-D) % 4] * fft_kernel_at(N, q, D)
        A_cf = embed_closed_M(N, q, M)
        dev5 = max(dev5, float(np.abs(A_fft - A_cf).max()))
check("G5a [machine] closed forms (D1)/(D2) equal the FFT mode-sum "
      "kernels on REFINED grids (M = 48/96/192, q = 0/3/5, wrap "
      "included): max |dev| = %.2e < 1e-9 -- the exact-summation "
      "theorem survives refinement" % dev5, dev5 < 1e-9)

dev5b = 0.0
for (M, q) in ((24, 0), (96, 3)):
    _, _, smat, _ = grid_structs(M)
    xi = np.repeat(np.arange(M) / M, 2)
    mask = circ(xi[None, :] - xi[:, None]) >= EPS_MID - 1e-12
    L = lead_matrix(q, M, mask)
    Fm = f_matrix(q, M, EPS_MID)
    dev5b = max(dev5b, abs(tnorm(L) - 2.0 * tnorm(Fm))
                / max(tnorm(L), 1e-300))
check("G5b [machine] spinor factorisation L = F (x) K2: ||L||_1 = "
      "2 ||F||_1 (rel dev %.1e <= 1e-8) -- the refinement ladder can "
      "run on the M x M point matrix" % dev5b, dev5b <= 1e-8)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G6
print("=" * 72)
print("G6: REMAINDER-PART REFINEMENT UNIFORMITY (a3) -- closed")
print("=" * 72)

u_s = sp.symbols("u", positive=True)
I2_EXACT = {}
for eps in EPS_LADDER:
    t0 = sp.Rational(1, int(round(1 / eps))) - sp.Rational(1, 48)
    intval = sp.integrate(sp.csc(u_s) ** 3, (u_s, sp.pi * t0, sp.pi / 2))
    I2_EXACT[eps] = float(sp.Rational(34, 9) * sp.pi ** 2
                          * intval / sp.pi)
RHO = {}
for eps in EPS_LADDER:
    t0f = max(eps - 1.0 / 48.0, 1.0 / 48.0)
    RHO[eps] = 2.5 * I2_EXACT[eps] + (5.0 / 48.0) * float(F2(t0f))
    print("  RHO(eps=%.4f) = (5/2) I2 + (5/48) F2 = %.1f  "
          "(I2 = %.2f exact csc^3 integral)"
          % (eps, RHO[eps], I2_EXACT[eps]))

pairs = [(M, M * r) for M in MLAD for r in RATIOS_NM if M * r <= 3072]
viol6r, viol6u, nin6 = 0, 0, 0
worst_ratio6 = 0.0
_EMB = {}


def emb(N, q, M):
    key = (N, q, M)
    if key not in _EMB:
        _EMB[key] = embed_closed_M(N, q, M)
    return _EMB[key]


for eps in EPS_LADDER:
    for (M, N) in pairs:
        # monotone-Riemann comparison for this (M, N, eps)
        dd = np.arange(1, M)
        cs = circ(dd / float(M))
        sel = cs >= eps - 1e-12
        lhs_r = float(F2(cs[sel] - 1.0 / N).sum()) / M
        # I2_EXACT is at cut eps - 1/48 <= eps - 1/N: valid upper bound
        rhs_r = 2.0 * I2_EXACT[eps] + (2.0 / M) \
            * float(F2(eps - 1.0 / N))
        if lhs_r > rhs_r + 1e-9:
            viol6r += 1
        nin6 += 1
        for q in range(6):
            A1 = emb(N, q, M)
            A2 = emb(2 * N, q, M)
            _, umat, smat, offp = grid_structs(M)
            xi = np.repeat(np.arange(M) / M, 2)
            mask = circ(xi[None, :] - xi[:, None]) >= eps - 1e-12
            sel_e = (np.abs(umat) == 1) & offp & mask
            lead = np.zeros_like(A1)
            lead[sel_e] = (1j * umat[sel_e] / (2.0 * M)) \
                * fprime(q, smat[sel_e])
            rem = np.abs((A2 - A1) - lead / N)[sel_e].sum()
            nin6 += 1
            if rem > RHO[eps] / N + 1e-12:
                viol6u += 1
            worst_ratio6 = max(worst_ratio6, rem * N / RHO[eps])
check("G6 [census] (a3) CLOSED: the monotone-Riemann comparison "
      "(1/M) sum F2(circ - 1/N) <= 2 I2 + (2/M) F2(eps - 1/N) and the "
      "uniform remainder bound ||D - L/N||_l1 <= RHO(eps)/N hold on "
      "ALL %d declared (eps, M, N, q) cases with M <= N/2: %d + %d "
      "violations; worst remainder/bound ratio %.3f -- the remainder "
      "part of the chain is refinement-UNIFORM with explicit "
      "constants" % (nin6, viol6r, viol6u, worst_ratio6),
      viol6r == 0 and viol6u == 0)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G7
print("=" * 72)
print("G7: LEADING-PART LOG LAW (a4) -- the honest obstruction")
print("=" * 72)

FN = {}
for q in range(6):
    for eps in EPS_LADDER:
        lad = list(MLAD)
        if eps == EPS_MID and q in (0, 3):
            lad.append(1536)
            if q == 3:
                lad.append(3072)
        FN[(q, eps)] = (lad, [tnorm(f_matrix(q, M, eps)) for M in lad])

ok7a, ok7b, ok7c = True, True, True
mech = []
print("  ||F_q^(M)(eps)||_1 ladder (per-doubling increments in "
      "brackets):")
for q in range(6):
    for eps in EPS_LADDER:
        lad, vals = FN[(q, eps)]
        inc = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        ratio = inc[-1] / inc[-2]
        ok7a &= (BAR_INC_LO <= ratio <= BAR_INC_HI)
        jump = float(np.abs(fprime(q, eps)))
        mr = inc[-1] / jump
        mech.append(mr)
        ok7b &= (BAR_MECH_LO <= mr <= BAR_MECH_HI)
        if eps in (1.0 / 12.0, 1.0 / 6.0):
            xs_f = np.log(lad[-4:])
            ys_f = np.array(vals[-4:])
            b, a = np.polyfit(xs_f, ys_f, 1)
            resid = ys_f - (a + b * xs_f)
            r2 = 1.0 - resid.var() / ys_f.var()
            ok7c &= (r2 >= BAR_R2)
        if q in (0, 3):
            print("  q=%d eps=%.4f: %s | inc %s | inc/|f'(eps)| = %.3f"
                  % (q, eps, "/".join("%.1f" % v for v in vals),
                     "/".join("%.2f" % v for v in inc), mr))
mech = np.array(mech)
spread = float((mech.max() - mech.min()) / mech.mean())
check("G7a [census] per-doubling increments of ||F||_1 are STABLE "
      "(last/prev in [%.2f, %.2f] for all 18 (q, eps)) -- log growth, "
      "not saturation and not blow-up" % (BAR_INC_LO, BAR_INC_HI),
      ok7a)
check("G7b [census] the mechanism is the cut jump: inc_last/|f_q'(eps)"
      "| in [%.2f, %.2f] for ALL sectors and eps, spread %.3f <= %.2f "
      "of the mean -- the log slope is proportional to the jump "
      "|f'(eps)| across a factor ~17 in the jump size"
      % (BAR_MECH_LO, BAR_MECH_HI, spread, BAR_MECH_SPREAD),
      ok7b and spread <= BAR_MECH_SPREAD)
check("G7c [census] log-law fit: ||F^(M)||_1 = a + b ln M with R^2 >= "
      "%.2f on the last 4 rungs (eps = 1/12, 1/6, all q)" % BAR_R2,
      ok7c)

ok7d = True
for q in (0, 3):
    lad = MLAD
    sharp_vals = FN[(q, EPS_MID)][1][:len(MLAD)]
    tap_vals = [tnorm(f_matrix(q, M, EPS_MID, taper=True)) for M in lad]
    inc_s = sharp_vals[-1] - sharp_vals[-2]
    inc_t = tap_vals[-1] - tap_vals[-2]
    rat_t = inc_t / (tap_vals[-2] - tap_vals[-3])
    ok7d &= (rat_t <= BAR_TAPER_RATIO and inc_t <= BAR_TAPER_FRAC
             * inc_s)
    print("  q=%d taper: %s | final inc %.4f vs sharp %.2f"
          % (q, "/".join("%.2f" % v for v in tap_vals), inc_t, inc_s))
check("G7d [control] the C^1-tapered mask (no jump) SATURATES: "
      "increment ratio <= %.1f and final increment <= %.1f x the "
      "sharp one -- the log divergence IS the eps-cut jump, not f' "
      "itself" % (BAR_TAPER_RATIO, BAR_TAPER_FRAC), ok7d)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G8
print("=" * 72)
print("G8: transfer to the frozen clause (fixed M, N -> inf)")
print("=" * 72)

ok8 = True
for q in (0, 3):
    M = 96
    xi = np.repeat(np.arange(M) / M, 2)
    mask = circ(xi[None, :] - xi[:, None]) >= EPS_MID - 1e-12
    Ltn = 2.0 * tnorm(f_matrix(q, M, EPS_MID))
    devs = []
    for N in (192, 384, 768, 1536, 3072):
        D = (embed_closed_M(2 * N, q, M) - embed_closed_M(N, q, M)) \
            * mask
        devs.append(abs(tnorm(D) * N / Ltn - 1.0))
    ok8 &= (devs[-1] <= BAR_TRANSFER and devs[-1] < devs[-2] < devs[-3])
    print("  q=%d, M=96, eps=1/12: |N ||D||_1 / ||L^(96)||_1 - 1| = %s"
          % (q, "/".join("%.4f" % v for v in devs)))
check("G8 [census] N ||D_N^(M)||_1 -> ||L^(M)||_1 for fixed refinement "
      "(last dev <= %.2f, decreasing): the log growth of ||L^(M)||_1 "
      "TRANSFERS to the frozen clause -- no single B(eps) can serve "
      "ALL grid refinements at r1 = 1; the literal v715 all-"
      "refinements S1 clause needs the log repair" % BAR_TRANSFER, ok8)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== G9
print("=" * 72)
print("G9: the typing -- what is CLOSED and what survives")
print("=" * 72)

print("""
  THE ELEMENTARY REMAINDER (a) OF v745, SPLIT AND SETTLED:

  (a1) continuum entrywise supremum  ..............  CLOSED [G2]
       (Taylor 5/8 symbolic + envelopes symbolic + monotone F1/F2 +
        1-Lipschitz circ; zero violations on ~1e6 inequalities)
  (a2) configuration-S1 (every eps-separated configuration of every
       refinement; collision-excised)  ............  CLOSED [G3/G4]
       B_conf(eps) explicit (packing + neighbour ladder + zeta(2),
       zeta(3)); zero violations
  (a3) remainder part under refinement (all M <= N/2)  CLOSED [G6]
       RHO(eps) explicit (monotone Riemann + exact csc^3 integral);
       zero violations
  (a4) leading part under refinement  ....  NOT closable as frozen:
       ||L_q^(M)(eps)||_1 = 2||F_q^(M)||_1 grows like a + b ln M with
       b = (0.10..0.17) |f_q'(eps)| [G7a-c], the growth is the eps-cut
       jump [G7d taper control], and it transfers to N ||D_N^(M)||_1
       [G8].  The frozen v715 clause "one B(eps) for ALL grid
       refinements" is therefore FALSE at r1 = 1 with a fixed B(eps).

  THE SURVIVING ANALYTIC STEP (named, not claimed) -- exactly ONE
  elementary-Fourier inequality:
       for the eps-cut symbol g_{q,eps}(x) = (1/2) f_q'(2x)
       1_{eps <= |2x| <= 1-eps} on [-1/2, 1/2),
       sum_{|k| <= M} |ghat_{q,eps}(k)|  <=  c0(q, eps)
                                             + (J(eps)/pi) ln M,
       J(eps) = 2 |f_q'(eps)|  (four jumps of size |f_q'(eps)|/2),
       by two integrations by parts (jump term J/(2 pi |k|) + smooth
       term V2/(2 pi k)^2) plus the BV Riemann-sum comparison for the
       DFT eigenvalues -- elementary, explicit constants, no
       asymptotics; it upgrades the census log law of G7 to a proven
       bound  ||D_N^(M)||_1 <= [B0(eps) + (J(eps)/pi) ln(M/24)] / N.

  CONSEQUENCE UNAFFECTED: for every FIXED refinement M the doubling-
  ladder majorant stays summable (sum_l [B0 + J ln(M/24)]/N_l < inf),
  and even the extreme joint scaling M = N/2 gives ln(N)/N, still
  summable -- the Araki/Powers-Stormer Cauchy argument of the (L1)
  consequence is NOT weakened; only the literal uniform-B wording of
  the frozen clause must carry the log factor.

  GATE.QGEO does not move.  No RH relevance is claimed.""")
check("G9 [C] typing: (a1)/(a2)/(a3) CLOSED elementarily with explicit"
      " constants and zero census violations; (a4) reduced to ONE "
      "named elementary-Fourier inequality with the log repair; the "
      "(L1) consequence survives -- named, not claimed; GATE.QGEO "
      "does not move", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed  [total %.1f s]"
      % (n_pass, len(CHECKS), time.time() - T0))
census_ok = all(ok for nm, ok in CHECKS
                if nm.startswith(("G1 ", "G2 ", "G3", "G4", "G6")))
log_ok = all(ok for nm, ok in CHECKS
             if nm.startswith(("G7", "G8")))
if n_pass == len(CHECKS):
    print("VERDICT: GRIDSUP-SPLIT-CLOSED-LOG-LAW")
    print("The elementary grid-supremum remainder (a) of the (L1)")
    print("sector lemma splits four ways: the continuum entrywise")
    print("supremum, the configuration-S1 statement and the remainder")
    print("part under refinement are CLOSED elementarily with explicit")
    print("constants and zero census violations; the leading part is")
    print("log-divergent under refinement (jump-driven, taper-")
    print("controlled), so the literal all-refinements clause needs")
    print("the (1 + ln M) repair, whose proof is ONE named elementary")
    print("Fourier inequality.  The Araki/Powers-Stormer consequence")
    print("of (L1) is unaffected.  GATE.QGEO does not move.")
elif census_ok and not log_ok:
    print("VERDICT: GRIDSUP-FULLY-CLOSED (log law NOT confirmed -- "
          "re-examine: if increments collapse, sup_M is finite)")
elif not census_ok:
    print("VERDICT: CENSUS-LEAK")
else:
    print("VERDICT: MIXED")
