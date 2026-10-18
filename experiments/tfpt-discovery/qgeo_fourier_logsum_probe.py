#!/usr/bin/env python3
"""Discovery probe: the QGEO Fourier log-sum inequality -- the surviving
analytic step of the grid-supremum split (parent probe verdict
GRIDSUP-SPLIT-CLOSED-LOG-LAW) -- CLOSED at theorem level.

THE TARGET (parent probe G9, quoted): "sum_{|k| <= M} |ghat_{q,eps}(k)|
<= c0(q,eps) + (J(eps)/pi) ln M, J(eps) = 2|f_q'(eps)| ... by two
integrations by parts ... elementary, explicit constants".

THE THEOREM (certified here; every constant explicit, no fits).  For
every sector q in {0..5}, every eps in {1/24, 1/12, 1/6} and every
M >= 24 with eps M an integer, the leading-part point matrix
F_q^(M)(eps) (entries (1/2M) f_q'((i-j)/M) on circ >= eps, the parent
probe's (a4) object) satisfies

  ||F_q^(M)(eps)||_1  =  sum_{k=0}^{M-1} |mu_k|
      <=  BOUND(q,eps,M)
       =  I1(eps) + F1(eps)/M                       [near-zero frequency]
        + (J(eps)/4) (2 + ln(M+3))                  [jump/spike term]
        + (pi^2/16) [I3(eps) + 3 F3(eps)/M + 2 F2(eps)]   [smooth term]
      <=  c0(q,eps) + (J(eps)/4) ln(M+3)
      <=  c0'(q,eps) + (J(eps)/pi) ln M             [named form, a
                                                     fortiori: 1/4 < 1/pi]
with the explicit constants
  J(eps)  = 2 |f_q'(eps)|                (the total mask-cut jump),
  I1(eps) = (5/3) cot(pi eps)                          [exact csc^2],
  I3(eps) = (C3/pi) (cot(pi eps) + cot^3(pi eps)/3)    [exact csc^4],
  F1 = C1/sin^2(pi eps),  F2 = C2/sin^3(pi eps),  F3 = C3/sin^4(pi eps),
  C1 = 5 pi/3,  C2 = 34 pi^2/9,  C3 = 314 pi^3/27,
  c0(q,eps) = I1 + F1/24 + (pi^2/16)(I3 + F3/8 + 2 F2) + J/2.

THE PROOF (the two integrations by parts, made exactly checkable on the
lattice -- each step is a machine-verified identity or a census-verified
inequality):
 P1 TWISTED-CIRCULANT DIAGONALISATION.  f_q'(t-1) = -e^{-i pi qt/3}
    f_q'(t) (sympy identity), so F_q^(M) = sum_d a_d S_nu^d is a
    polynomial in the unitary twisted shift S_nu (corner entry nubar =
    -e^{-i pi qt/3}; q = 3: nu = 1, plain circulant).  Hence F is
    NORMAL, and ||F||_1 = sum_k |mu_k| EXACTLY with
    mu_k = sum_d a_d z_k^d, z_k = e^{i(theta + 2 pi k)/M},
    theta = arg(nubar).  No compression loss, no continuum limit.
 P2 FIRST SUMMATION BY PARTS (the jump term).  The exact cyclic
    identity (1 - z_k) mu_k = sum_d (Delta_nu a)_d z_k^d holds with the
    twisted difference (Delta_nu a)_0 = a_0 - nubar a_{M-1}.  Because
    eps M is an integer, Delta_nu a contains EXACTLY TWO jump spikes of
    exact magnitude (1/2M)|f_q'(eps)| (mask entry/exit; |f_q'(1-eps)| =
    |f_q'(eps)|) plus a smooth part r.  This is the discrete first
    integration by parts: the spikes carry the 1/k decay.
 P3 SECOND SUMMATION BY PARTS (the absolutely-continuous term).  On the
    smooth part, |sum_d r_d z_k^d| <= TV2/|1 - z_k| with the second-
    variation mass TV2 = sum |Delta_nu r| bounded by the integral
    second-difference kernel + the F3 envelope + monotone Riemann:
    TV2 <= I3(eps)/M^2 + 3 F3(eps)/M^3 + 2 F2(eps)/M^2 (two junction
    terms).  This is the discrete second integration by parts: the
    smooth remainder carries 1/k^2 and stays BOUNDED in M.
 P4 HARMONIC COMPARISON (the log).  |1 - z_k| = 2 sin(pi m_k/M) with
    the frequency-distance multiset {m_k} contained in {beta + j} u
    {j - beta}; sin(pi x) >= 2x on [0, 1/2] gives, after excluding the
    single near-zero frequency k*,
      sum_{k != k*} 1/|1-z_k|   <= (M/2)(2 + ln(M+3)),
      sum_{k != k*} 1/|1-z_k|^2 <= pi^2 M^2/16
    (sum_{j>=1} (j-1/2)^{-2} = pi^2/2 exact; sum_{j<=n} (j-1/2)^{-1}
    <= 2 + ln(2n-1), verified for every used n).
 P5 NEAR-ZERO FREQUENCY.  |mu_{k*}| <= sum_d |a_d| <= I1(eps) + F1/M
    (monotone Riemann on the F1 envelope).
 P6 ASSEMBLY.  sum|mu| <= P5 + [spike mass J/(2M)] x P4a + TV2 x P4b
    = BOUND(q,eps,M).

THE REPAIRED (L1) CLAUSE (transfer; RHO(eps) from the parent's closed
remainder part (a3)):
  || D_N^(M)(eps) ||_1  <=  [ B0(q,eps) + (J(eps)/2) ln(M+3) ] / N
  for all M | N, N/M even, M >= 24,  B0 = 2 c0(q,eps) + RHO(eps),
  RHO(eps) = (5/2) I2(eps - 1/48) + (5/48) F2(eps - 1/48).
This implies the parent-named form [B0' + (J/pi) ln(M/24)]/N a
fortiori.  The Araki/Powers-Stormer summability survives: sum_l
[B0 + (J/2) ln(M_l+3)]/N_l is finite (exact closed form
sum_l (a + b l) 2^-l = 2a + 2b, printed).

FROZEN GRIDS AND BARS (preregistered before the run):
  18 pairs = 6 sectors x eps in (1/24, 1/12, 1/6); census ladder
  M = 24 * 2^j, j = 0..8 (M <= 6144, FFT eigenvalue route); structure
  checks at M in (24, 96, 384) vs dense SVD; transfer family M in
  (24..768), N/M in (2, 8, 32), N <= 3072 (parent G6 family).
  S1 all sympy residues identically zero; harmonic/sine inequalities
     0 violations on every used n / dense grid.
  S2 F3-envelope census (~2e5 points, circ >= 1/100): 0 violations;
     control 0.5 C3 must produce violations.
  S3 structure: wrap identity <= 1e-12; eig-vs-SVD <= 1e-8; Abel
     identities <= 1e-10; two spikes, each = (1/2M)|f'(eps)| within
     1e-10 relative.
  S4 THE CENSUS (18 x 9 rungs): 0 violations in ALL of (a) sum|a| <=
     I1 + F1/M, (b) TV2 <= TV2 bound, (c)/(d) denominator sums <=
     certified, (e) per-k chain inequality, (f) ||F||_1 <= BOUND with
     printed margins, (g) BOUND <= named (J/pi) form.
  S5 slopes b = [TN(6144) - TN(3072)]/ln 2: b <= J/4 and b <= J/pi for
     all 18; tracking (J/pi)/b in [2, 5]; sharpness b/(J/pi^2) in
     [0.80, 1.10] (the measured slope IS J/pi^2, not J/pi: report).
  S6 transfer census: 0 violations of N ||D||_1 <= B0 + (J/2) ln(M+3)
     on the full family; Araki sums printed (exact closed form).
  S7 controls: tapered C^1 mask slope <= 0.05 (J/pi^2) for all 18 (the
     J = 0 case: the bound collapses to the constant c0); halved-J
     sharp-slope control J/(2 pi^2) < b must fire on ALL 18.

VERDICT ENUMS (frozen): FOURIER-LOGSUM-CLOSED (all bars green: the
inequality is certified with explicit constants, zero census
violations, transfer verified -- remainder (a4) of the majorant lemma
is closed in the corrected (1 + ln M) form); FOURIER-LOGSUM-PARTIAL
(a named constant/case fails); FOURIER-LOGSUM-WRONG (the inequality is
violated -- counterexample reported).

FIREWALL: experiments-only; writes NO files; verification/ read-only
(hashed); no marker moves, no contract edits; NO RH relevance claims;
deterministic; runtime minutes.
"""

import hashlib
import os
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
EPS_LADDER = (1.0 / 24.0, 1.0 / 12.0, 1.0 / 6.0)
MLAD = tuple(24 * 2 ** j for j in range(9))          # 24 .. 6144
MSTRUCT = (24, 96, 384)
RATIOS_NM = (2, 8, 32)
QT = {0: 0, 1: 1, 2: 2, 4: -2, 5: -1}                # q = 3: cot sector
C1 = 5.0 * np.pi / 3.0
C2 = 34.0 * np.pi ** 2 / 9.0
C3 = 314.0 * np.pi ** 3 / 27.0
IP = np.array([1.0, 1j, -1.0, -1j])
LN2 = float(np.log(2.0))

BAR_TRACK_LO, BAR_TRACK_HI = 2.0, 5.0        # (J/pi)/b tracking band
BAR_SHARP_LO, BAR_SHARP_HI = 0.80, 1.10      # b/(J/pi^2) band
BAR_TAPER = 0.05                             # taper slope vs J/pi^2

FROZEN_SOURCES = (
    "verification/v745_qgeo_car_l1_sector_lemma.py",
    "experiments/tfpt-discovery/qgeo_grid_supremum_probe.py",
    "experiments/tfpt-discovery/qgeo_car_continuum_probe.py",
)


# ------------------------------------------------------------------ helpers
def circ(d):
    f = np.mod(np.asarray(d, dtype=float), 1.0)
    return np.minimum(f, 1.0 - f)


def fprime(q, t):
    t = np.asarray(t, dtype=float)
    st = np.sin(np.pi * t)
    if q == 3:
        return (-np.pi / st ** 2).astype(complex)
    a = np.pi * QT[q] / 3.0
    return np.exp(1j * a * t) * (1j * a / st
                                 - np.pi * np.cos(np.pi * t) / st ** 2)


def fthird(q, t):
    """f_q'''(t) closed form (verified symbolically in S1.2)."""
    t = np.asarray(t, dtype=float)
    s, c = np.sin(np.pi * t), np.cos(np.pi * t)
    if q == 3:
        return (-2.0 * np.pi ** 3 * (3.0 - 2.0 * s ** 2) / s ** 4
                ).astype(complex)
    a = np.pi * QT[q] / 3.0
    g0 = 1.0 / s
    g1 = -np.pi * c / s ** 2
    g2 = np.pi ** 2 / s + 2.0 * np.pi ** 2 * c ** 2 / s ** 3
    g3 = -np.pi ** 3 * c * (6.0 - s ** 2) / s ** 4
    return np.exp(1j * a * t) * ((1j * a) ** 3 * g0 + 3.0 * (1j * a) ** 2
                                 * g1 + 3.0 * (1j * a) * g2 + g3)


def F1(t):
    return C1 / np.sin(np.pi * np.asarray(t, dtype=float)) ** 2


def F2(t):
    return C2 / np.sin(np.pi * np.asarray(t, dtype=float)) ** 3


def F3(t):
    return C3 / np.sin(np.pi * np.asarray(t, dtype=float)) ** 4


def nu_bar(q):
    if q == 3:
        return 1.0 + 0.0j
    return -np.exp(-1j * np.pi * QT[q] / 3.0)


def a_seq(q, eps, M, taper=False):
    """First column of F_q^(M)(eps): a_d = (1/2M) f'(d/M) masked."""
    d = np.arange(M)
    cs = circ(d / float(M))
    a = np.zeros(M, dtype=complex)
    if taper:
        w = np.clip((cs - eps) / (eps / 2.0), 0.0, 1.0)
        w = w * w * (3.0 - 2.0 * w)
        sel = (d > 0) & (w > 0)
        a[sel] = w[sel] * fprime(q, d[sel] / float(M)) / (2.0 * M)
    else:
        sel = (d > 0) & (cs >= eps - 1e-12)
        a[sel] = fprime(q, d[sel] / float(M)) / (2.0 * M)
    return a


def eig_moduli(q, eps, M, taper=False):
    """|mu_k| via the twisted-DFT route (exact; FFT, O(M log M))."""
    a = a_seq(q, eps, M, taper=taper)
    th = np.angle(nu_bar(q))
    d = np.arange(M)
    b = a * np.exp(1j * th * d / M)
    mu = M * np.fft.ifft(b)          # sum_d b_d e^{+2 pi i k d/M}
    return np.abs(mu)


def f_matrix(q, M, eps):
    i = np.arange(M)
    S = (i[:, None] - i[None, :]) / float(M)
    Cm = circ(S)
    off = i[:, None] != i[None, :]
    F = np.zeros((M, M), dtype=complex)
    sel = off & (Cm >= eps - 1e-12)
    F[sel] = fprime(q, S[sel]) / (2.0 * M)
    return F


def closed_Nc(N, q, D):
    D = np.asarray(D)
    Ds = np.where(D == 0, 1, D)
    if q == 3:
        val = (np.sin(np.pi * Ds / 2.0) * np.cos(np.pi * Ds / N)
               / np.sin(np.pi * Ds / N)).astype(complex)
    else:
        val = (np.exp(1j * np.pi * QT[q] * Ds / (3.0 * N))
               * np.sin(np.pi * Ds / 2.0) / np.sin(np.pi * Ds / N))
    return np.where(D == 0, N / 2.0 + 0j, val)


def embed_closed_M(N, q, M):
    step = N // M
    base = step * np.arange(M)
    g = np.empty(2 * M, dtype=int)
    g[0::2] = base
    g[1::2] = base + 1
    D = g[None, :] - g[:, None]
    return (1.0 / M) * IP[(-D) % 4] * closed_Nc(N, q, D)


def tnorm(A):
    return float(np.linalg.svd(A, compute_uv=False).sum())


def exact_I1(eps):
    return (5.0 / 3.0) / np.tan(np.pi * eps)


def exact_I3(eps):
    ct = 1.0 / np.tan(np.pi * eps)
    return (C3 / np.pi) * (ct + ct ** 3 / 3.0)


def Jconst(q, eps):
    return 2.0 * float(np.abs(fprime(q, eps)))


def bound_pieces(q, eps, M):
    """(MU0cert, spike log term, smooth term) of the certified BOUND."""
    mu0 = exact_I1(eps) + float(F1(eps)) / M
    spike = (Jconst(q, eps) / 4.0) * (2.0 + np.log(M + 3.0))
    smooth = (np.pi ** 2 / 16.0) * (exact_I3(eps)
                                    + 3.0 * float(F3(eps)) / M
                                    + 2.0 * float(F2(eps)))
    return mu0, spike, smooth


def c0_const(q, eps):
    """M-free constant of the theorem line (M >= 24 worst case)."""
    return (exact_I1(eps) + float(F1(eps)) / 24.0
            + (np.pi ** 2 / 16.0) * (exact_I3(eps)
                                     + float(F3(eps)) / 8.0
                                     + 2.0 * float(F2(eps)))
            + Jconst(q, eps) / 2.0)


# ================================================================== S0
print("=" * 72)
print("S0: freeze")
print("=" * 72)
repo = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
nh = 0
for rel in FROZEN_SOURCES:
    p = os.path.join(repo, rel)
    h = hashlib.sha256(open(p, "rb").read()).hexdigest()
    nh += 1
    print("  SHA256 %s = %s" % (rel, h))
check("S0.1 [freeze] the three frozen sources hashed (read-only; "
      "nothing else is read)", nh == 3)


# ================================================================== S1
print("=" * 72)
print("S1: the symbolic elementary lemmas (sympy, exact)")
print("=" * 72)

t_s, a_s = sp.symbols("t a", real=True)
s_ = sp.sin(sp.pi * t_s)
c_ = sp.cos(sp.pi * t_s)

# S1.1 the twist identity f'(t-1) = -e^{-ia} f'(t)  (a = pi qt/3)
fp_sym = sp.diff(sp.exp(sp.I * a_s * t_s) / s_, t_s)
res_tw = sp.simplify(fp_sym.subs(t_s, t_s - 1)
                     + sp.exp(-sp.I * a_s) * fp_sym)
res_tw = sp.simplify(sp.expand_trig(res_tw).rewrite(sp.exp))
cotp = sp.diff(sp.cot(sp.pi * t_s), t_s)
res_tw3 = sp.simplify(cotp.subs(t_s, t_s - 1) - cotp)
check("S1.1 [sympy] twist: f'(t-1) = -e^{-ia} f'(t) (residue %s); "
      "cot'(t-1) = cot'(t) (residue %s) -- F_q^(M) is an exact "
      "nu-twisted circulant, nubar = -e^{-i pi qt/3} (q=3: nu=1)"
      % (res_tw, res_tw3), res_tw == 0 and res_tw3 == 0)

# S1.2 third-derivative closed forms + envelope C3
g3_sym = sp.diff(1 / s_, t_s, 3)
g3_form = -sp.pi ** 3 * c_ * (6 - s_ ** 2) / s_ ** 4
res_g3 = sp.simplify(sp.expand_trig(sp.simplify(g3_sym - g3_form)))
cot3_sym = sp.diff(sp.cot(sp.pi * t_s), t_s, 3)
cot3_form = -2 * sp.pi ** 3 * (3 - 2 * s_ ** 2) / s_ ** 4
res_c3 = sp.simplify(sp.expand_trig(sp.simplify(cot3_sym - cot3_form)))
a_max = 2 * sp.pi / 3
coefC3 = sp.simplify(a_max ** 3 + 3 * a_max ** 2 * sp.pi
                     + 6 * a_max * sp.pi ** 2 + 6 * sp.pi ** 3
                     - sp.Rational(314, 27) * sp.pi ** 3)
check("S1.2 [sympy] csc''' = -pi^3 c (6 - s^2)/s^4 (res %s), so "
      "|csc'''| <= 6 pi^3/s^4; cot''' = -2 pi^3 (3 - 2 s^2)/s^4 "
      "(res %s), so |cot'''| <= 6 pi^3/s^4; triangle a^3 + 3 a^2 pi + "
      "6 a pi^2 + 6 pi^3 = 314 pi^3/27 at a = 2 pi/3 (res %s): "
      "|f_q'''| <= C3/s^4 with C3 = 314 pi^3/27 = %.1f"
      % (res_g3, res_c3, coefC3, C3),
      res_g3 == 0 and res_c3 == 0 and coefC3 == 0)

# S1.3 exact integrals I1, I3
eps_s = sp.symbols("epsilon", positive=True)
I1_sym = sp.integrate(sp.csc(sp.pi * t_s) ** 2, (t_s, eps_s, sp.S(1) / 2))
res_I1 = sp.simplify(sp.Rational(5, 3) * sp.pi * I1_sym
                     - sp.Rational(5, 3) * sp.cot(sp.pi * eps_s))
I3_sym = sp.integrate(sp.csc(sp.pi * t_s) ** 4, (t_s, eps_s, sp.S(1) / 2))
res_I3 = sp.simplify(I3_sym - (sp.cot(sp.pi * eps_s)
                               + sp.cot(sp.pi * eps_s) ** 3 / 3) / sp.pi)
check("S1.3 [sympy] I1(eps) = int C1 csc^2 = (5/3) cot(pi eps) "
      "(res %s); int csc^4 = (cot + cot^3/3)/pi (res %s) => I3(eps) = "
      "(C3/pi)(cot + cot^3/3) exact" % (res_I1, res_I3),
      res_I1 == 0 and res_I3 == 0)

# S1.4 the two summation lemmas
zsum = sp.Sum(1 / (sp.Symbol("j", positive=True, integer=True)
                   - sp.S(1) / 2) ** 2,
              (sp.Symbol("j", positive=True, integer=True), 1, sp.oo)
              ).doit()
res_z = sp.simplify(zsum - sp.pi ** 2 / 2)
jmax = max(MLAD) // 2 + 2
jj = np.arange(1, jmax + 1, dtype=float)
part = np.cumsum(1.0 / (jj - 0.5))
harm_ok = bool(np.all(part <= 2.0 + np.log(2.0 * jj - 1.0) + 1e-12))
xg = np.linspace(1e-9, 0.5, 400001)
sin_ok = bool(np.all(np.sin(np.pi * xg) >= 2.0 * xg - 1e-12))
check("S1.4 [sympy+census] sum_{j>=1} (j-1/2)^-2 = pi^2/2 (res %s); "
      "sum_{j<=n} (j-1/2)^-1 <= 2 + ln(2n-1) for ALL n <= %d "
      "(0 violations); sin(pi x) >= 2x on [0, 1/2] (dense, 0 "
      "violations)" % (res_z, jmax), res_z == 0 and harm_ok and sin_ok)

# S1.5 second-difference kernel: numeric spot-check of the exact identity
ok15 = True
for q in (0, 1, 3, 5):
    for (x0, h) in ((0.21, 1.0 / 96.0), (0.37, 1.0 / 384.0)):
        lhs = fprime(q, x0) - 2.0 * fprime(q, x0 - h) \
            + fprime(q, x0 - 2.0 * h)
        ss = np.linspace(0, h, 401)
        tt = np.linspace(0, h, 401)
        SS, TT = np.meshgrid(ss, tt)
        vals = fthird(q, x0 - SS - TT)
        rhs = np.trapezoid(np.trapezoid(vals, tt, axis=0), ss)
        ok15 &= abs(lhs - rhs) <= 1e-8 * max(abs(lhs), 1.0)
check("S1.5 [machine] second-difference kernel f'(x) - 2f'(x-h) + "
      "f'(x-2h) = int int f'''(x-s-t) ds dt (quadrature residue <= "
      "1e-8 rel on spot grid) => |second difference| <= h^2 "
      "sup|f'''|", ok15)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== S2
print("=" * 72)
print("S2: third-derivative envelope census |f'''| <= F3(circ)")
print("=" * 72)
rng = np.random.default_rng(76101)
tg = np.concatenate([np.linspace(0.01, 0.99, 120001),
                     0.01 + 0.98 * rng.random(80000)])
viol2, viol2c, n2 = 0, 0, 0
for q in range(6):
    fv = np.abs(fthird(q, tg))
    env = C3 / np.sin(np.pi * tg) ** 4
    viol2 += int(np.sum(fv > env * (1.0 + 1e-12)))
    viol2c += int(np.sum(fv > 0.5 * env * (1.0 + 1e-12)))
    n2 += tg.size
check("S2 [census] |f_q'''(t)| <= F3(circ(t)) on %d continuum points "
      "(all 6 sectors, circ >= 1/100): %d violations" % (n2, viol2),
      viol2 == 0)
check("S2c [control] halved envelope 0.5 C3 must fail: %d violations "
      "(fires)" % viol2c, viol2c > 0)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== S3
print("=" * 72)
print("S3: the structure identities (P1/P2/P3), machine precision")
print("=" * 72)
dev_wrap = dev_eig = dev_ab1 = dev_ab2 = dev_spk = 0.0
ok_nspk = True
for q in range(6):
    for eps in EPS_LADDER:
        for M in MSTRUCT:
            F = f_matrix(q, M, eps)
            a = a_seq(q, eps, M)
            nub = nu_bar(q)
            # P1: wrap identity + normality (eigs vs SVD)
            dev_wrap = max(dev_wrap, float(np.max(np.abs(
                F[0, 1:] - nub * a[:0:-1]))))
            th = np.angle(nub)
            d = np.arange(M)
            mu = M * np.fft.ifft(a * np.exp(1j * th * d / M))
            sv = np.linalg.svd(F, compute_uv=False)
            dev_eig = max(dev_eig, float(np.max(np.abs(
                np.sort(np.abs(mu))[::-1] - sv))))
            # P2: first twisted Abel identity
            z = np.exp(1j * (th + 2.0 * np.pi * np.arange(M)) / M)
            Da = a - np.roll(a, 1)
            Da[0] = a[0] - nub * a[M - 1]
            rhs = M * np.fft.ifft(Da * np.exp(1j * th * d / M))
            dev_ab1 = max(dev_ab1, float(np.max(np.abs(
                (1.0 - z) * mu - rhs))))
            # spikes: exactly two, exact magnitude (1/2M)|f'(eps)|
            supp = np.where(np.abs(a) > 0)[0]
            d_ent = int(supp.min())
            d_ex = int((supp.max() + 1) % M)
            ok_nspk &= bool(np.all(np.diff(supp) == 1))
            ref = float(np.abs(fprime(q, eps))) / (2.0 * M)
            dev_spk = max(dev_spk,
                          abs(abs(Da[d_ent]) - ref) / ref,
                          abs(abs(Da[d_ex]) - ref) / ref)
            # P3: second twisted Abel identity on the smooth part
            r = Da.copy()
            r[d_ent] = 0.0
            r[d_ex] = 0.0
            Dr = r - np.roll(r, 1)
            Dr[0] = r[0] - nub * r[M - 1]
            rser = M * np.fft.ifft(r * np.exp(1j * th * d / M))
            rhs2 = M * np.fft.ifft(Dr * np.exp(1j * th * d / M))
            dev_ab2 = max(dev_ab2, float(np.max(np.abs(
                (1.0 - z) * rser - rhs2))))
check("S3.1 [machine] P1 twisted-circulant: wrap identity max dev "
      "%.1e <= 1e-12; sorted |mu_k| vs SVD singular values max dev "
      "%.1e <= 1e-8 on all 18 pairs x M in %s -- ||F||_1 = sum|mu_k| "
      "EXACTLY" % (dev_wrap, dev_eig, MSTRUCT),
      dev_wrap <= 1e-12 and dev_eig <= 1e-8)
check("S3.2 [machine] P2/P3 the two summation-by-parts identities are "
      "exact: Abel-1 dev %.1e, Abel-2 dev %.1e (<= 1e-10)"
      % (dev_ab1, dev_ab2), dev_ab1 <= 1e-10 and dev_ab2 <= 1e-10)
check("S3.3 [machine] the mask cut sits ON the lattice: exactly two "
      "jump spikes (contiguous support), each of exact magnitude "
      "(1/2M)|f_q'(eps)| (rel dev %.1e <= 1e-10; uses |f'(1-eps)| = "
      "|f'(eps)|)" % dev_spk, ok_nspk and dev_spk <= 1e-10)
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== S4
print("=" * 72)
print("S4: THE CENSUS -- certified chain vs measured, 18 x %d rungs"
      % len(MLAD))
print("=" * 72)
viol4 = {key: 0 for key in "abcdefg"}
n4 = 0
TN = {}
min_margin = np.inf
max_ratio_meas = 0.0
for q in range(6):
    for eps in EPS_LADDER:
        tns = []
        for M in MLAD:
            a = a_seq(q, eps, M)
            nub = nu_bar(q)
            th = np.angle(nub)
            d = np.arange(M)
            mu = np.abs(M * np.fft.ifft(a * np.exp(1j * th * d / M)))
            tn = float(mu.sum())
            tns.append(tn)
            n4 += 1
            # (a) near-zero-frequency bound
            mu0c = exact_I1(eps) + float(F1(eps)) / M
            if float(np.abs(a).sum()) > mu0c * (1 + 1e-12):
                viol4["a"] += 1
            # (b) TV2 exact vs analytic bound
            Da = a - np.roll(a, 1)
            Da[0] = a[0] - nub * a[M - 1]
            supp = np.where(np.abs(a) > 0)[0]
            d_ent = int(supp.min())
            d_ex = int((supp.max() + 1) % M)
            r = Da.copy()
            r[d_ent] = 0.0
            r[d_ex] = 0.0
            Dr = r - np.roll(r, 1)
            Dr[0] = r[0] - nub * r[M - 1]
            tv2 = float(np.abs(Dr).sum())
            tv2b = (exact_I3(eps) / M ** 2 + 3.0 * float(F3(eps)) / M ** 3
                    + 2.0 * float(F2(eps)) / M ** 2)
            if tv2 > tv2b * (1 + 1e-12):
                viol4["b"] += 1
            # (c)/(d) denominator sums vs certified
            z = np.exp(1j * (th + 2.0 * np.pi * np.arange(M)) / M)
            az = np.abs(1.0 - z)
            kstar = int(np.argmin(az))
            msk = np.arange(M) != kstar
            s1x = float(np.sum(1.0 / az[msk]))
            s2x = float(np.sum(1.0 / az[msk] ** 2))
            s1c = (M / 2.0) * (2.0 + np.log(M + 3.0))
            s2c = np.pi ** 2 * M ** 2 / 16.0
            if s1x > s1c * (1 + 1e-12):
                viol4["c"] += 1
            if s2x > s2c * (1 + 1e-12):
                viol4["d"] += 1
            # (e) per-k chain inequality (proven; roundoff tolerance)
            spike_mass = float(np.abs(Da[d_ent]) + np.abs(Da[d_ex]))
            lhs_k = mu[msk]
            rhs_k = spike_mass / az[msk] + tv2 / az[msk] ** 2
            if np.any(lhs_k > rhs_k * (1 + 1e-9) + 1e-12):
                viol4["e"] += 1
            # (f) THE BOUND
            mu0c_, spikec, smoothc = bound_pieces(q, eps, M)
            bound = mu0c_ + spikec + smoothc
            if tn > bound * (1 + 1e-12):
                viol4["f"] += 1
            min_margin = min(min_margin, bound / tn)
            max_ratio_meas = max(max_ratio_meas, tn / bound)
            # (g) the named (J/pi) form dominates the certified bound
            named = (c0_const(q, eps)
                     + (Jconst(q, eps) / np.pi) * np.log(M))
            if bound > named * (1 + 1e-12):
                viol4["g"] += 1
        TN[(q, eps)] = tns
print("  measured ||F||_1 vs certified BOUND (q = 0 and q = 3 rows):")
for q in (0, 3):
    for eps in EPS_LADDER:
        tns = TN[(q, eps)]
        b_lo = sum(bound_pieces(q, eps, MLAD[0]))
        b_hi = sum(bound_pieces(q, eps, MLAD[-1]))
        print("  q=%d eps=%.4f: TN 24->6144: %.1f -> %.1f | BOUND "
              "%.0f -> %.0f | margin factor %.0fx"
              % (q, eps, tns[0], tns[-1], b_lo, b_hi, b_hi / tns[-1]))
check("S4 [census] the certified chain holds on ALL %d (q, eps, M) "
      "cases with ZERO violations in every clause: (a) mu0 %d, "
      "(b) TV2 %d, (c) S1-sum %d, (d) S2-sum %d, (e) per-k chain %d, "
      "(f) ||F||_1 <= BOUND %d (worst measured/bound = %.3f), "
      "(g) BOUND <= named (J/pi) form %d -- the log-sum inequality is "
      "CERTIFIED with explicit constants"
      % (n4, viol4["a"], viol4["b"], viol4["c"], viol4["d"],
         viol4["e"], viol4["f"], max_ratio_meas, viol4["g"]),
      all(v == 0 for v in viol4.values()))
print("  NOTE (honest): the bound is VALID but LOOSE in the constant "
      "part (margin %.0fx at worst-case eps; dominated by the "
      "pi^2/16 smooth term).  The LOG COEFFICIENT is the load-"
      "bearing content." % (1.0 / (1.0 / min_margin)))
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== S5
print("=" * 72)
print("S5: slope identification -- certified vs measured log slopes")
print("=" * 72)
ok5a = ok5b = ok5c = True
track_lo, track_hi = np.inf, 0.0
sharp_lo, sharp_hi = np.inf, 0.0
print("  b = [TN(6144) - TN(3072)]/ln2 per (q,eps); J = 2|f'(eps)|:")
for q in range(6):
    for eps in EPS_LADDER:
        tns = TN[(q, eps)]
        b = (tns[-1] - tns[-2]) / LN2
        J = Jconst(q, eps)
        ok5a &= (b <= J / 4.0)
        ok5b &= (b <= J / np.pi)
        tr = (J / np.pi) / b
        track_lo, track_hi = min(track_lo, tr), max(track_hi, tr)
        sh = b / (J / np.pi ** 2)
        sharp_lo, sharp_hi = min(sharp_lo, sh), max(sharp_hi, sh)
        ok5c &= (BAR_SHARP_LO <= sh <= BAR_SHARP_HI)
        if q in (0, 3):
            print("  q=%d eps=%.4f: b = %8.3f | J/4 = %8.3f | J/pi = "
                  "%8.3f | b/(J/pi^2) = %.3f"
                  % (q, eps, b, J / 4.0, J / np.pi, sh))
check("S5a [census] the certified coefficient J/4 upper-bounds the "
      "measured log slope b for ALL 18 (q, eps)", ok5a)
check("S5b [census] the named coefficient J/pi upper-bounds b for ALL "
      "18 and TRACKS it within the frozen band: (J/pi)/b in "
      "[%.2f, %.2f] subset [%.1f, %.1f]"
      % (track_lo, track_hi, BAR_TRACK_LO, BAR_TRACK_HI),
      ok5b and BAR_TRACK_LO <= track_lo and track_hi <= BAR_TRACK_HI)
check("S5c [census] SHARPNESS: b/(J/pi^2) in [%.3f, %.3f] subset "
      "[%.2f, %.2f] for all 18 -- the measured slope is J/pi^2, NOT "
      "J/pi" % (sharp_lo, sharp_hi, BAR_SHARP_LO, BAR_SHARP_HI), ok5c)
print("""
  PI-BOOKKEEPING (honest): the parent probe reported per-doubling
  increments inc = b ln 2 = (0.119..0.143)|f'(eps)|, i.e. b =
  (0.086..0.103) J = (0.85..1.02) J/pi^2.  The measured b does NOT
  equal J/pi: the named bound is VALID (factor ~pi above measured)
  but NOT SHARP.  The sharp constant is J/pi^2: the small-angle csc
  sum contributes M/(pi k) per frequency and the TWO lattice spikes
  interfere with mean modulus (2/pi) x spike mass (average of
  |1 - e^{i psi}| = 4/pi over the equidistributed phase psi), giving
  J/pi^2 exactly.  The certified J/4 and named J/pi remain honest
  UPPER bounds; sharpening 1/4 -> 1/pi^2 would need the average-
  interference step, which is NOT elementary-uniform (not claimed).""")
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== S6
print("=" * 72)
print("S6: TRANSFER -- the repaired (L1) clause, re-verified")
print("=" * 72)
u_s = sp.symbols("u", positive=True)
I2_EXACT, RHO = {}, {}
for eps in EPS_LADDER:
    t0 = sp.Rational(1, int(round(1 / eps))) - sp.Rational(1, 48)
    intval = sp.integrate(sp.csc(u_s) ** 3, (u_s, sp.pi * t0, sp.pi / 2))
    I2_EXACT[eps] = float(sp.Rational(34, 9) * sp.pi ** 2 * intval / sp.pi)
    t0f = max(eps - 1.0 / 48.0, 1.0 / 48.0)
    RHO[eps] = 2.5 * I2_EXACT[eps] + (5.0 / 48.0) * float(F2(t0f))

print("  REPAIRED CLAUSE: ||D_N^(M)||_1 <= [B0(q,eps) + (J(eps)/2) "
      "ln(M+3)]/N,")
print("  B0 = 2 c0(q,eps) + RHO(eps):")
for eps in EPS_LADDER:
    print("    eps=%.4f: RHO = %.1f | B0(q=0) = %.0f | J/2 = %.2f"
          % (eps, RHO[eps], 2.0 * c0_const(0, eps) + RHO[eps],
             Jconst(0, eps) / 2.0))

MLAD_T = (24, 48, 96, 192, 384, 768)
pairs = [(M, M * r) for M in MLAD_T for r in RATIOS_NM if M * r <= 3072]
_EMB = {}


def emb(N, q, M):
    key = (N, q, M)
    if key not in _EMB:
        _EMB[key] = embed_closed_M(N, q, M)
    return _EMB[key]


viol6, n6 = 0, 0
worst6 = 0.0
for eps in EPS_LADDER:
    for (M, N) in pairs:
        xi = np.repeat(np.arange(M) / float(M), 2)
        mask = circ(xi[None, :] - xi[:, None]) >= eps - 1e-12
        for q in range(6):
            D = (emb(2 * N, q, M) - emb(N, q, M)) * mask
            lhs = tnorm(D) * N
            rhs = (2.0 * c0_const(q, eps) + RHO[eps]
                   + (Jconst(q, eps) / 2.0) * np.log(M + 3.0))
            n6 += 1
            if lhs > rhs * (1 + 1e-12):
                viol6 += 1
            worst6 = max(worst6, lhs / rhs)
check("S6.1 [census] the repaired clause N ||D_N^(M)||_1 <= B0 + "
      "(J/2) ln(M+3) holds on ALL %d (eps, M, N, q) cases of the "
      "parent family (M <= 768, N <= 3072, N/M in %s): %d violations; "
      "worst measured/bound = %.4f" % (n6, RATIOS_NM, viol6, worst6),
      viol6 == 0)

# Araki/Powers-Stormer summability with the explicit constants
l_s, aa, bb = sp.symbols("l A B", positive=True)
geo = sp.Sum((aa + bb * l_s) * sp.Rational(1, 2) ** l_s,
             (l_s, 0, sp.oo)).doit()
res_geo = sp.simplify(geo - (2 * aa + 2 * bb))
q0, eps0 = 0, 1.0 / 12.0
B0v = 2.0 * c0_const(q0, eps0) + RHO[eps0]
Jv = Jconst(q0, eps0)
fixed_M = 3072
s_fixed = (B0v + (Jv / 2.0) * np.log(fixed_M + 3.0)) * (2.0 / 48.0)
A_ex = B0v + (Jv / 2.0) * np.log(24.0 + 3.0 / 1.0)
s_extreme = (1.0 / 48.0) * (2.0 * (B0v + (Jv / 2.0) * np.log(48.0))
                            + 2.0 * (Jv / 2.0) * LN2)
check("S6.2 [sympy+machine] Araki/Powers-Stormer summability survives "
      "with the explicit constants: sum_l (A + B l) 2^-l = 2A + 2B "
      "exact (residue %s); fixed M = %d, (q=0, eps=1/12): sum_l "
      "[B0 + (J/2) ln(M+3)]/N_l = %.1f < inf; extreme joint scaling "
      "M = N/2: sum <= %.1f < inf (both printed from the closed form)"
      % (res_geo, fixed_M, s_fixed, s_extreme),
      res_geo == 0 and np.isfinite(s_fixed) and np.isfinite(s_extreme))
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== S7
print("=" * 72)
print("S7: controls (must fire)")
print("=" * 72)
# S7a: tapered C^1 mask = the J = 0 case; the bound collapses to c0
ok7a = True
dev_tap = 0.0
Ft = None
for q in range(6):
    for eps in EPS_LADDER:
        tn_hi = float(eig_moduli(q, eps, MLAD[-1], taper=True).sum())
        tn_lo = float(eig_moduli(q, eps, MLAD[-2], taper=True).sum())
        b_tap = (tn_hi - tn_lo) / LN2
        ok7a &= (b_tap <= BAR_TAPER * Jconst(q, eps) / np.pi ** 2)
# taper eigen-route guard: still an exact twisted circulant
q_g, eps_g, M_g = 1, 1.0 / 12.0, 96
i = np.arange(M_g)
S = (i[:, None] - i[None, :]) / float(M_g)
Cm = circ(S)
w = np.clip((Cm - eps_g) / (eps_g / 2.0), 0.0, 1.0)
w = w * w * (3.0 - 2.0 * w)
Fm = np.zeros((M_g, M_g), dtype=complex)
sel = (i[:, None] != i[None, :]) & (w > 0)
Fm[sel] = w[sel] * fprime(q_g, S[sel]) / (2.0 * M_g)
dev_tap = abs(float(eig_moduli(q_g, eps_g, M_g, taper=True).sum())
              - tnorm(Fm)) / tnorm(Fm)
check("S7a [control] the C^1-tapered mask (J = 0: no spikes, the "
      "certified bound collapses to the CONSTANT c0) shows NO log "
      "growth: measured taper slope <= %.2f x (J/pi^2) for ALL 18 "
      "(q, eps) at M = 3072 -> 6144 (eigen route re-verified vs SVD, "
      "rel dev %.1e)" % (BAR_TAPER, dev_tap),
      ok7a and dev_tap <= 1e-10)

# S7b: halved jump constant must produce census violations
fire_sharp, fire_named, fire_crude, fire_bound = 0, 0, 0, 0
for q in range(6):
    for eps in EPS_LADDER:
        tns = TN[(q, eps)]
        b = (tns[-1] - tns[-2]) / LN2
        J = Jconst(q, eps)
        if b > (J / 2.0) / np.pi ** 2:
            fire_sharp += 1
        if b > (J / 2.0) / np.pi:
            fire_named += 1
        if b > (J / 2.0) / 4.0:
            fire_crude += 1
        mu0c_, spikec, smoothc = bound_pieces(q, eps, MLAD[-1])
        half_bound = mu0c_ + spikec / 2.0 + smoothc
        if tns[-1] > half_bound:
            fire_bound += 1
check("S7b [control] halved jump constant J -> J/2 produces census "
      "violations at the sharp slope identification: b > (J/2)/pi^2 "
      "fires on %d/18 (must be 18)" % fire_sharp, fire_sharp == 18)
print("  HONEST NOTE: halving J inside the FULL bound is masked by "
      "the large constant part (violations: named-slope %d/18, "
      "crude-slope %d/18, full-bound %d/18) -- the constant c0 "
      "dominates at these M; the J-identification is falsifiable at "
      "the slope level, where it FIRES 18/18."
      % (fire_named, fire_crude, fire_bound))
print("  [t = %.1f s]" % (time.time() - T0))


# ================================================================== S8
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed  [total %.1f s]"
      % (n_pass, len(CHECKS), time.time() - T0))
bound_ok = all(ok for nm, ok in CHECKS if nm.startswith(
    ("S1", "S2 ", "S3", "S4")))
if n_pass == len(CHECKS):
    print("VERDICT: FOURIER-LOGSUM-CLOSED")
    print("""
The surviving analytic step of the grid-supremum split is CLOSED at
theorem level.  The two integrations by parts are realised as exact
twisted summation-by-parts identities on the lattice (machine-
verified); the jump term carries (J(eps)/4) ln(M+3) with the exact
two-spike mass J/(2M); the smooth term is bounded M-uniformly by
(pi^2/16)(I3 + 3F3/M + 2F2) via the F3 envelope; the near-zero
frequency by I1 + F1/M.  Zero census violations on 18 x 9 rungs up to
M = 6144; the named (J/pi) ln M form holds a fortiori; the repaired
(L1) clause ||D_N^(M)||_1 <= [B0 + (J/2) ln(M+3)]/N is verified with
zero violations on the full parent family and Araki/Powers-Stormer
summability survives with explicit constants.  Remainder (a) of the
v745 majorant lemma is now FULLY closed in the corrected (1 + ln M)
form: (a1)-(a3) by the parent probe, (a4) by this theorem.

RECOMMENDED CONTRACT/LEDGER TEXT (report only -- files untouched):
  "(a) grid-sup [elementary]: CLOSED.  (a1)-(a3) as before; (a4) the
   leading part obeys the certified grid Fourier log-sum theorem
   ||F_q^(M)(eps)||_1 <= c0(q,eps) + (J(eps)/4) ln(M+3), J = 2
   |f_q'(eps)|, c0 = I1 + F1/24 + (pi^2/16)(I3 + F3/8 + 2 F2) + J/2
   (all constants exact csc-integrals/envelopes; proof = twisted-
   circulant diagonalisation + two summation-by-parts + harmonic
   comparison, fully elementary).  The (L1) all-refinements clause is
   REPAIRED to ||D_N^(M)||_1 <= [B0(q,eps) + (J(eps)/2) ln(M+3)]/N,
   B0 = 2 c0 + RHO; Araki/Powers-Stormer summability unaffected.
   Sharpness: the measured slope is J/pi^2 (spike interference); the
   certified J/4 and the named J/pi are honest upper bounds.
   Discovery evidence: qgeo_fourier_logsum_probe.py (18 x 9 census to
   M = 6144, zero violations, controls fired)."

GATE.QGEO does not move.  No RH relevance is claimed.""")
elif not bound_ok:
    print("VERDICT: FOURIER-LOGSUM-WRONG (a chain clause is violated "
          "-- see the failing check above; counterexample in census)")
else:
    failing = [nm for nm, ok in CHECKS if not ok]
    print("VERDICT: FOURIER-LOGSUM-PARTIAL (failing: %s)"
          % "; ".join(failing))
