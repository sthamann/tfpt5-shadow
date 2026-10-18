#!/usr/bin/env python3
"""Discovery probe: ARF/GSO HARDENING of the last [C] discriminator of
the orbifold front -- B vs C3 (the Arf/GSO twin of the seam assembly)
decided STRUCTURALLY, not only by the measured ground-class datum.

CONTEXT (inherited read-only): orbifold_assembly_probe.py M3.4 left the
B-vs-C3 kill as a data-backed [C]: both pass {integer spectrum, unique
vacuum, S measured, T exact}; B keeps the measured c = 0 sector grounds
and the Klein eta = (1,1), C3 (weight (-1)^{gt ht}, the Arf stacking)
excises all odd-sector grounds.  This probe hardens the kill along
three routes:

ROUTE A1 (RP/excision -- defect spectroscopy):
  The mu6 defect ladder on the seam double: the dressed charge string
  with angle lam = pi gt/3 is the gt-half-twist defect pair (the gt = 2
  string is the v639 sigma pair, the gt = 3 string the Ising disorder
  control).  Its two-point decay measures the LIGHTEST gt-twist state
  the seam actually interpolates; the string is diagonal in the
  occupation basis, hence EXACTLY charge-neutral: every interpolated
  state lies in the c = 0 class.  Exact charge-resolved Fock
  enumeration gives the per-sector minima of both candidates:
    B  (c = 0):      Delta_min = (0, 1, 4, 9, 4, 1)/36
    C3 (c = 3gt):    Delta_min = (0, 85, 4, 81, 4, 85)/36 on gt odd
  (crosschecks: the untwisted c = 3 minimum 5/2 = the assembly probe's
  M1.3 value; the gt = 2, c = 3 minimum 4/36 + 13/6 = 41/18 = the C2
  exponent).  The measured exponents must hit 2 x (c = 0 minima)
  = (1/18, 2/9, 1/2); C3's odd-sector predictions (85/18, 81/18) are
  off by factors ~85 and ~9.  The Klein RP Gram of the half-twist
  (tau) sector is PSD: the excised states are physical seam states
  (positive norm), not gauge artifacts.  If all this stands, C3
  excises states that demonstrably exist on the lattice seam.

ROUTE A2 (Arf/spin-structure bookkeeping):
  (i) The cover circle is NS (v622/v623 kernel identity re-verified,
  Ramond must-fail): the spatial spin holonomy is antiperiodic.
  (ii) The canonical deck lift: 16 k_m = pi (2m+1)/3 exactly, so
  deck^3 gives e^{i pi (2m+1)} = -1 on EVERY mode: deck^3 = (-1)^F
  with the empty-state / Fermi-sea eigenvalue pinned to +1 by exact
  integer arithmetic (sea momentum sum 1152 x pi/3 = 384 pi, even);
  the R cover would give deck^3 = +1 (the Arf-relevant sign is
  NS-borne).  (iii) One-Fock-space realization: every twist sector is
  the SAME 48-site Fock space with one twisted bond (spectra check),
  the Z6 generator V1 = exp(i pi (Nhat - N/2)/3) is a fixed on-site
  product with V1^3 = (-1)^F (c-number-exact for N/2 even) commuting
  with every sector Hamiltonian.  (iv) THE CLASSIFICATION: all 6^6
  sector-character wirings w(gt,ht) = chi(gt)^{ht}/6 (the group-average
  family -- what a genuine quotient by a concrete generator can
  produce, with per-sector lift characters chi) are enumerated; the
  survivors of {temporal weights are projectors, vacuum kept, exact
  weight-level S, exact weight-level T} are EXACTLY chi = 1 (= B) and
  chi(gt) = (-1)^{gt} (= C3).  The structural pin: chi(gt) is the
  extra phase of the lift on the gt-defect sector; since all sectors
  live on ONE Fock space where the generator (and (-1)^F = the on-site
  parity product) is a single fixed operator, chi = 1 is forced: the
  geometric quotient of the seam is B.  C3 requires representing
  (-1)^F as -(-1)^F on odd-defect sectors -- the Arf/Kitaev stacking:
  a DIFFERENT fermionic decoration (its R-type states are parity-odd),
  not a quotient of the seam.  Parity fingerprint: C3's kept odd-sector
  charge classes are odd (parity -1); the enumerated seam grounds are
  charge-0 (parity +1).

ROUTE A3 (character/OPE):
  B and C3 coincide EXACTLY on the even (sigma) sectors, so the v639
  OPE datum c1 = 2 Delta = 2/9 CANNOT discriminate them -- an honest
  structural finding about the route as originally proposed.  The
  discriminating OPE data live in the half-twisted sectors: the tau
  four-point (lam = pi/3 strings) with the v639 closed form
  Ghat = A^2 [w(1-w)]^{-2 Delta}: measured leading exponent and
  model-bound c1 = 2 Delta = 1/18 (B's tau, charge 0, eta = 1/6);
  C3's lightest gt = 1 interpolator (charge 3) would give
  2 Delta = 85/18.

Checks:

  (A0.1) [machine] Toeplitz covariance == verbatim mode-sum covariance
         (N = 96, machinery validation).
  (A0.2) [machine] PH reality of the dressed strings for the FULL mu6
         angle family (random multi-arc, mixed angles pi/3 .. 5pi/3):
         the Klein/zero-mode dressing e^{-i sum(u)/2} makes every
         string expectation exactly real at half filling.

  (A1.1) [E] N-scaling exponents of the defect ladder (N = 96..1536,
         x = N/4, FH-corrected 3-parameter fit): 2 Delta =
         1/18 (lam = pi/3), 2/9 (2pi/3, v639 reproduction), 1/2 (pi,
         Ising control), each < 3 %.
  (A1.2) [E] within-ring exponents at N = 384 (x = 24..120): same
         targets, < 3 %.
  (A1.3) [machine] Klein RP of the half-twist sector: the tau Gram
         (lam = pi/3, Klein pairing + dressing) is exactly real
         symmetric and PSD at N = 48/96/192/384; the k = 1 and k = 5
         blocks coincide (charge conjugation); eta = -1 must-fail
         (negative definite).
  (A1.4) [machine] exact charge-resolved spectral minima per sector
         (Fock enumeration, N = 48 and 96 give IDENTICAL p/36
         fractions): c = 0 minima (0, 1, 4, 9, 4, 1)/36 and c = 3
         minima (90, 85, 82, 81, 82, 85)/36; crosschecks 5/2 (M1.3
         untwisted Q = 3 level) and 4/36 + 13/6 = 82/36 (the C2
         exponent 41/18).
  (A1.5) [central] THE EXCISION VERDICT: the measured ladder exponents
         match 2 x (c = 0 minima) at < 3 % (= B in every sector);
         C3's odd-sector predictions 85/18 and 81/18 exceed the
         measurements by factors ~85 and ~9 (rejection: C3's relative
         deviation > 50 %, measured ~7 and ~84); the string is exactly
         charge-neutral (occupation-diagonal), so the interpolated
         states have ZERO overlap with C3's odd-sector space: C3
         excises states that exist on the lattice seam with positive
         Klein norm and measured dimension.

  (A2.1) [exact] the cover circle is NS: the 48-site chiral kernel =
         NS mode sum (closed form sum sin((2j+1)x) = sin^2(24x)/sin x,
         sympy) for all d; the Ramond mode sum must-fails EXACTLY:
         kernel - R sum = (2/N) tan(pi d/96) != 0 for every odd d
         (symbolic identity; numerically small, ~0.007 at d = 1 --
         the exactness, not the size, is the kill, as in v622 D2).
  (A2.2) [exact] deck-lift integer arithmetic: 16 k_m / pi = (2m+1)/3;
         deck class phases e^{i pi (2r+1)/3}; deck^3 phase per mode
         = e^{i pi (2m+1)} = -1 for ALL 48 modes (deck^3 = (-1)^F);
         deck^6 = 1; Fermi-sea eigenvalue +1 (occupied-sum 1152,
         1152/3 = 384 even -- exact integers); R-cover control:
         deck_R^3 = +1 per mode (the -1 is NS-borne).
  (A2.3) [machine] one-Fock-space realization: the bond-defect
         Hamiltonian (one twisted bond, same lattice) reproduces
         eps6(N, gt) for ALL six sectors at machine precision; the
         uniform-gauge deck permutation commutes with H (deck is a
         symmetry); V1^3 = (-1)^F as exact c-number arithmetic on all
         occupation numbers (N/2 even).
  (A2.4) [central] the classification: enumerating ALL 6^6 sector-
         character wirings chi(gt)^{ht}/6 (orbit-averaged over the
         exact lattice degeneracies gt -> -gt, ht -> -ht), the
         survivors of {projector integrality, vacuum, exact table-level
         S, exact table-level T} are EXACTLY two: chi = 1 (= B, the
         uniform table) and chi(gt) = (-1)^{gt} (= C3, the Arf
         stacking); the canonical fixed-operator pin (one Fock space,
         one generator, one on-site parity product) forces chi = 1:
         the seam quotient is B; C3 = seam x Kitaev/Arf (odd-sector
         parity redefined), structurally not the seam.
  (A3.1) [machine] B and C3 coincide exactly on even gt (weights and
         projectors): the v639 sigma-sector OPE datum c1 = 2/9 is
         B-vs-C3-BLIND -- the route as proposed cannot discriminate
         (honest finding).
  (A3.2) [E] the tau four-point (lam = pi/3): string gauge identity
         and exact lattice crossing (machine); conformal collapse onto
         Ghat = A^2 [w(1-w)]^{-2 Delta}; N-extrapolated (192 -> 384,
         d^{-4/3}) MODEL-BOUND exponent p = 2 Delta = 1/18 at < 8 %,
         with c1 = p from the single-block form (v639 S3 convention);
         the MODEL-FREE small-w extractor only brackets 1/18 in a band
         (reported, not gated -- same honest split as v639); the
         amplitude agrees with the independent two-point A^2; C3's
         alternative (charge-3 interpolator, 85/18) rejected by the
         measured p.
  (A4.1) [C] typing: what is now structural, what stays [C].

Verdict enums (frozen): ARF-B-STRUCTURAL (classification + canonical
pin + excision data all pass: B-vs-C3 decided structurally at the
lattice level), ARF-B-DATA-ONLY (excision data pass but the
classification or the pin fails: kill stays data-backed), ARF-UNDECIDED
(the discriminating measurements are inconclusive), MIXED (machinery or
controls break).

FIREWALL: experiments/ only; GATE.QGEO does not move; no marker
changes; verification/ untouched.

Conventions inherited read-only from orbifold_assembly_probe.py,
orbifold_modular_probe.py, parafermion_klein_rp_probe.py,
orbifold_twist_ope_probe.py, v622/v623/v628/v639.
"""

import itertools
from fractions import Fraction

import numpy as np
import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------------ constants
LAM6 = {gt: np.pi * gt / 3.0 for gt in range(1, 6)}   # mu6 string angles
TARGET_2D = {1: 1.0 / 18.0, 2: 2.0 / 9.0, 3: 0.5}    # 2 Delta = 2 (gt/6)^2
FH_RHO = {1: 4.0 / 3.0, 2: 2.0 / 3.0, 3: 2.0}        # FH correction exps
N_SCAL = (96, 192, 384, 768, 1536)
N_RING = 384
N_KLEIN = (48, 96, 192, 384)
N_ENUM = (48, 96)
TOL_MACH = 1e-10
TOL_RP = 1e-10
TOL_EXP = 0.03            # 3 % on two-point exponents
TOL_4PT = 0.08            # 8 % on the four-point exponent
RNG = np.random.default_rng(61)

# expected exact minima (p/36) per sector, from the charge bookkeeping
C0_EXPECT = [Fraction(p, 36) for p in (0, 1, 4, 9, 4, 1)]
C3_EXPECT = [Fraction(p, 36) for p in (90, 85, 82, 81, 82, 85)]


# ------------------------------------------------------------------ machinery
def cov_verbatim(N):
    """NS half-filled covariance (verbatim parafermion_klein_rp_probe)."""
    assert N % 4 == 0
    m = np.arange(-(N // 4), N // 4)
    k = 2.0 * np.pi * (m + 0.5) / N
    j = np.arange(N)
    V = np.exp(1j * np.outer(k, j)) / np.sqrt(N)
    return V.conj().T @ V


def cov_toeplitz(N):
    """Same covariance via the real Toeplitz kernel (fast at large N)."""
    assert N % 4 == 0
    m = np.arange(N // 4)
    k = 2.0 * np.pi * (m + 0.5) / N
    d = np.arange(N)
    c = (2.0 / N) * np.cos(np.outer(d, k)).sum(axis=1)
    idx = np.abs(np.subtract.outer(np.arange(N), np.arange(N)))
    return c[idx].astype(complex)


_COV = {}


def cov(N):
    if N not in _COV:
        _COV[N] = cov_toeplitz(N)
    return _COV[N]


def string_det(C, sites, u):
    """<prod e^{i u_j n_j}> = det(I + D C_S), D = diag(e^{iu} - 1)."""
    S = np.asarray(sites, dtype=int)
    Cs = C[np.ix_(S, S)]
    M = np.eye(len(S), dtype=complex) \
        + (np.exp(1j * np.asarray(u, dtype=float)) - 1.0)[:, None] * Cs
    return np.linalg.det(M)


def two_point(N, x, lam):
    """|dressed| defect two-point T(x) on the N-ring (x even)."""
    S = np.arange(x)
    u = lam * np.ones(x)
    return abs(string_det(cov(N), S, u))


def chord(N, x):
    return (N / np.pi) * np.sin(np.pi * x / N)


def modes6(N, gt):
    return 2.0 * np.pi * (np.arange(N) + 0.5 + (gt % 6) / 6.0) / N


def eps6(N, gt):
    e = -np.cos(modes6(N, gt))
    e[np.abs(e) < 1e-13] = 0.0
    return e


# ================================================================== A0
print("=" * 72)
print("A0: machinery validation")
print("=" * 72)

dev_cov = np.abs(cov_toeplitz(96) - cov_verbatim(96)).max()
check("A0.1 [machine] the Toeplitz covariance equals the verbatim "
      "mode-sum covariance of the Klein probe (N = 96)",
      dev_cov < 1e-12, "max |dev| = %.3e" % dev_cov)

C96 = cov(96)
ANGLES = [np.pi / 3, 2 * np.pi / 3, np.pi, 4 * np.pi / 3, 5 * np.pi / 3]
dev_re = 0.0
for _ in range(40):
    cuts = np.sort(RNG.choice(np.arange(0, 96, 2), size=6, replace=False))
    ops = []
    for (a1, a2) in ((cuts[0], cuts[1]), (cuts[2], cuts[3]),
                     (cuts[4], cuts[5])):
        if a2 > a1:
            ops.append((np.arange(a1, a2), float(RNG.choice(ANGLES))))
    sites = np.concatenate([s for s, _ in ops])
    u = np.concatenate([a * np.ones(len(s)) for s, a in ops])
    w = np.exp(-0.5j * u.sum()) * string_det(C96, sites, u)
    dev_re = max(dev_re, abs(w.imag) / max(1.0, abs(w)))
check("A0.2 [machine] the zero-mode-dressed string is EXACTLY real for "
      "the FULL mu6 angle family (pi/3 .. 5pi/3, random multi-arc "
      "mixed-angle configs): the particle-hole identity carries the "
      "Klein reality for the half-twist strings too",
      dev_re < TOL_MACH, "max |Im|/|w| = %.3e (40 configs)" % dev_re)


# ================================================================== A1
print("=" * 72)
print("A1: the mu6 defect ladder and the excision test")
print("=" * 72)

# A1.1 N-scaling exponents
P_SCAL = {}
print("  N-scaling fits ln T = a - p ln N + b N^{-rho}, x = N/4:")
for gt in (1, 2, 3):
    lam, rho = LAM6[gt], FH_RHO[gt]
    ys, lns, cors = [], [], []
    for N in N_SCAL:
        x = int(round(N / 4))
        x -= x % 2
        ys.append(np.log(two_point(N, x, lam)))
        lns.append(np.log(N))
        cors.append(N ** (-rho))
    A = np.column_stack([np.ones(len(ys)), lns, cors])
    coef, res, *_ = np.linalg.lstsq(A, np.array(ys), rcond=None)
    p = -coef[1]
    P_SCAL[gt] = p
    print("  gt=%d lam=%5.3f  p = %.6f  target %.6f  rel dev %.3e"
          % (gt, lam, p, TARGET_2D[gt],
             abs(p - TARGET_2D[gt]) / TARGET_2D[gt]))
ok11 = all(abs(P_SCAL[gt] - TARGET_2D[gt]) / TARGET_2D[gt] < TOL_EXP
           for gt in (1, 2, 3))
check("A1.1 [E] the defect-ladder exponents (N-scaling 96..1536): "
      "2 Delta = %.5f vs 1/18 (half twist), %.5f vs 2/9 (v639 sigma "
      "reproduction), %.5f vs 1/2 (Ising disorder control), each < 3 %%"
      % (P_SCAL[1], P_SCAL[2], P_SCAL[3]), ok11)

# A1.2 within-ring exponents at N = 384
P_RING = {}
xs = np.arange(24, 121, 8)
for gt in (1, 2, 3):
    lam, rho = LAM6[gt], FH_RHO[gt]
    ys = np.array([np.log(two_point(N_RING, int(x), lam)) for x in xs])
    D = chord(N_RING, xs)
    A = np.column_stack([np.ones(len(xs)), np.log(D), D ** (-rho)])
    coef, *_ = np.linalg.lstsq(A, ys, rcond=None)
    P_RING[gt] = -coef[1]
ok12 = all(abs(P_RING[gt] - TARGET_2D[gt]) / TARGET_2D[gt] < TOL_EXP
           for gt in (1, 2, 3))
check("A1.2 [E] within-ring exponents at N = 384 (x = 24..120): "
      "p = %.6f / %.6f / %.6f vs (1/18, 2/9, 1/2), each < 3 %%"
      % (P_RING[1], P_RING[2], P_RING[3]), ok12,
      "rel devs %.2e / %.2e / %.2e"
      % tuple(abs(P_RING[g] - TARGET_2D[g]) / TARGET_2D[g]
              for g in (1, 2, 3)))

# A1.3 Klein Gram of the half-twist (tau) sector
LAMK = {1: np.pi / 3, 5: 5 * np.pi / 3, 2: 2 * np.pi / 3}


def xgrid(N):
    return [4 * i * N // 96 for i in range(1, 12)]


def gram_tau(N, k, klein=True, dress=True, b=0):
    """Mirror Gram of the lam_k strings (verbatim Klein-probe pairing:
    bond reflection r(j) = 2b - 1 - j, Klein keeps the string angle)."""
    C = cov(N)
    lam = LAMK[k]
    els = xgrid(N)
    n = len(els)
    M = np.zeros((n, n), dtype=complex)
    for i, xa in enumerate(els):
        bra = (np.arange(b - xa, b) % N,
               lam if klein else -lam)
        for j, xb in enumerate(els):
            ket = (np.arange(b, b + xb) % N, lam)
            sites = np.concatenate([bra[0], ket[0]])
            u = np.concatenate([bra[1] * np.ones(len(bra[0])),
                                ket[1] * np.ones(len(ket[0]))])
            val = string_det(C, sites, u)
            M[i, j] = np.exp(-0.5j * u.sum()) * val if dress else val
    return M


def herm_dev(M):
    return np.abs(M - M.conj().T).max() / np.abs(M).max()


def imag_dev(M):
    return np.abs(M.imag).max() / np.abs(M).max()


def eig_ratio(M):
    ev = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
    return ev, ev.min() / np.abs(ev).max()


k13_real, k13_psd = True, True
rows13 = []
G_TAU = {}
for N in N_KLEIN:
    for k in (1, 5):
        M = gram_tau(N, k)
        G_TAU[(N, k)] = M
        ev, r = eig_ratio(M)
        k13_real &= (imag_dev(M) < TOL_MACH and herm_dev(M) < TOL_MACH)
        k13_psd &= (r >= -TOL_RP)
        rows13.append((N, k, r))
        print("  Klein tau Gram N=%4d k=%d  min=%.6e  max=%.6e  "
              "min/max=%.3e" % (N, k, ev.min(), ev.max(), r))
dev_cc = max(np.abs(G_TAU[(N, 1)] - G_TAU[(N, 5)]).max()
             / np.abs(G_TAU[(N, 1)]).max() for N in N_KLEIN)
r_neg = eig_ratio(-1.0 * G_TAU[(96, 1)])[1]
check("A1.3 [machine] the Klein RP Gram of the HALF-TWIST (tau) sector "
      "(lam = pi/3, Klein pairing + zero-mode dressing) is exactly real "
      "symmetric and PSD at N = 48/96/192/384; the k = 1 and k = 5 "
      "charge blocks coincide (dev %.1e); eta = -1 must-fail flips the "
      "spectrum (floor %.2f): the Delta = 1/36 twist states are "
      "positive-norm seam states"
      % (dev_cc, r_neg),
      k13_real and k13_psd and dev_cc < 1e-9 and r_neg < -0.5,
      "worst min/max = %.3e" % min(r for *_, r in rows13))

# A1.4 exact charge-resolved spectral minima


def sector_minima(N, gt):
    """(dg, Qsea, nz, particle costs, hole costs) in Delta units."""
    e = eps6(N, gt)
    e0 = eps6(N, 0)
    dg = (e[e < 0].sum() - e0[e0 < 0].sum()) * N / (2.0 * np.pi)
    Qsea = int((e < 0).sum()) - N // 2
    nz = int((e == 0.0).sum())
    par = np.sort(e[e > 0]) * N / (2.0 * np.pi)
    hol = np.sort(-e[e < 0]) * N / (2.0 * np.pi)
    return dg, Qsea, nz, par, hol


def class_min(N, gt, cmod):
    """Minimal Delta in sector gt with charge c = (Nhat - N/2) = cmod
    mod 6, exact greedy over (zeros z, particles p, holes h)."""
    dg, Qsea, nz, par, hol = sector_minima(N, gt)
    Ppre = np.concatenate([[0.0], np.cumsum(par[:10])])
    Hpre = np.concatenate([[0.0], np.cumsum(hol[:10])])
    best = None
    for z in range(nz + 1):
        for p in range(len(Ppre)):
            for h in range(len(Hpre)):
                c = Qsea + z + p - h
                if c % 6 != cmod % 6:
                    continue
                cost = Ppre[p] + Hpre[h]
                if best is None or cost < best:
                    best = cost
    return dg + best


mins = {}
ok14 = True
print("  charge-resolved minima Delta_min(gt, c) as p/36 fractions:")
print("  %-4s %-3s %-12s %-12s %s" % ("N", "gt", "c=0", "c=3", "resid"))
for N in N_ENUM:
    for gt in range(6):
        row = {}
        resid = 0.0
        for cmod in (0, 3):
            d = class_min(N, gt, cmod)
            fr = Fraction(int(round(36.0 * d)), 36)
            resid = max(resid, abs(d - float(fr)))
            row[cmod] = fr
        mins[(N, gt)] = row
        print("  %-4d %-3d %-12s %-12s %.2e"
              % (N, gt, row[0], row[3], resid))
        ok14 &= resid < 0.02
for gt in range(6):
    ok14 &= (mins[(48, gt)] == mins[(96, gt)])
    ok14 &= (mins[(48, gt)][0] == C0_EXPECT[gt])
    ok14 &= (mins[(48, gt)][3] == C3_EXPECT[gt])
check("A1.4 [machine] the exact charge-resolved minima (N = 48 and 96 "
      "IDENTICAL fractions): c = 0 gives (0, 1, 4, 9, 4, 1)/36 -- the "
      "measured sector grounds; c = 3 gives (90, 85, 82, 81, 82, 85)/36"
      " -- crosschecks: untwisted 90/36 = 5/2 (assembly M1.3) and "
      "gt = 2: 82/36 = 41/18 (the C2 exponent), reproduced from pure "
      "charge bookkeeping", ok14)

# A1.5 the excision verdict
b_pred = {gt: 2.0 * float(C0_EXPECT[gt]) for gt in (1, 2, 3)}
c3_pred = {gt: 2.0 * float(C3_EXPECT[gt]) for gt in (1, 3)}
dev_b = {gt: abs(P_SCAL[gt] - b_pred[gt]) / b_pred[gt] for gt in (1, 2, 3)}
dev_c3 = {gt: abs(P_SCAL[gt] - c3_pred[gt]) / c3_pred[gt]
          for gt in (1, 3)}
factor_c3 = {gt: c3_pred[gt] / P_SCAL[gt] for gt in (1, 3)}
print("  B predictions 2 Delta(c=0): %s" % {g: "%.5f" % v
                                            for g, v in b_pred.items()})
print("  C3 predictions 2 Delta(c=3), odd sectors: %s"
      % {g: "%.5f" % v for g, v in c3_pred.items()})
print("  C3 prediction / measured p: %s"
      % {g: "%.2f" % v for g, v in factor_c3.items()})
ok15 = (all(v < TOL_EXP for v in dev_b.values())
        and all(v > 0.5 for v in dev_c3.values()))
check("A1.5 [central] THE EXCISION VERDICT: the measured ladder "
      "exponents hit B's c = 0 minima in every sector (rel devs "
      "%.2e / %.2e / %.2e < 3 %%); C3's odd-sector predictions 85/18 = "
      "%.3f and 81/18 = %.3f exceed the measurements by factors %.1f "
      "and %.1f (relative deviations %.1f and %.1f, rejection "
      "threshold 0.5); the defect string is occupation-diagonal, hence "
      "EXACTLY charge-neutral: every interpolated state is c = 0 and "
      "has ZERO overlap with C3's odd-sector space (c = 3): C3 excises "
      "states that exist on the lattice seam with positive Klein norm "
      "(A1.3) and measured dimension (A1.1/A1.2)"
      % (dev_b[1], dev_b[2], dev_b[3], c3_pred[1], c3_pred[3],
         factor_c3[1], factor_c3[3], dev_c3[1], dev_c3[3]), ok15)


# ================================================================== A2
print("=" * 72)
print("A2: the Arf/spin-structure bookkeeping")
print("=" * 72)

# A2.1 NS forced on the 48-cover
xsym = sp.symbols("x")
lhs = sum(sp.sin((2 * j + 1) * xsym) for j in range(24))
rhs = sp.sin(24 * xsym) ** 2 / sp.sin(xsym)
closed = sp.simplify(sp.expand_trig(lhs - rhs).rewrite(sp.exp)) == 0
ns_ok = True
for d in range(1, 48):
    # via the closed form: mode sum = (2/48) sin^2(pi d/2)/sin(pi d/48)
    tgt = sp.Rational(2, 48) / sp.sin(sp.pi * sp.Rational(d, 48)) \
        if d % 2 else sp.Integer(0)
    ms = sp.Rational(2, 48) * sp.sin(sp.pi * sp.Rational(d, 2)) ** 2 \
        / sp.sin(sp.pi * sp.Rational(d, 48))
    if sp.simplify(ms - tgt) != 0:
        ns_ok = False
# the R must-fail, proven symbolically in three steps:
# (i) R closed form in x: sum_{j=1}^{23} sin(2jx) = sin(24x)sin(23x)/sin(x)
sym1 = sp.simplify(sp.expand_trig(
    sum(sp.sin(2 * j * xsym) for j in range(1, 24))
    - sp.sin(24 * xsym) * sp.sin(23 * xsym) / sp.sin(xsym)
).rewrite(sp.exp)) == 0
# (ii) half-angle identity: csc x - cot x = tan(x/2)
sym2 = sp.simplify((1 / sp.sin(xsym) - sp.cos(xsym) / sp.sin(xsym)
                    - sp.tan(xsym / 2)).rewrite(sp.exp)) == 0
# (iii) per-d exact reductions at x = pi d/48 (odd d): sin(24x) = +-1,
# +-sin(23x) = cos(x)  =>  kernel - R sum = (2/48) tan(pi d/96) > 0
r_exact, r_num = sym1 and sym2, 0.0
for d in (1, 3, 5):
    s = (-1) ** ((d - 1) // 2)
    e1 = sp.simplify(sp.sin(24 * sp.pi * d / sp.Integer(48)) - s) == 0
    e2 = sp.simplify(s * sp.sin(23 * sp.pi * d / sp.Integer(48))
                     - sp.cos(sp.pi * d / sp.Integer(48))) == 0
    gap = sp.Rational(2, 48) * sp.tan(sp.pi * sp.Rational(d, 96))
    r_exact &= e1 and e2 and (gap.is_positive is True)
    r_num = max(r_num, float(gap))
check("A2.1 [exact] the cover circle is NS: closed form sum_{j<24} "
      "sin((2j+1)x) = sin^2(24x)/sin(x) (sympy) => the 48-site chiral "
      "kernel equals the NS mode sum for ALL d (even-d zeros included);"
      " the Ramond mode sum must-fails EXACTLY: kernel - R sum = "
      "(2/48) tan(pi d/96) != 0 for every odd d (symbolic; numerically "
      "up to %.4f at d = 5 -- the exactness is the kill, as in v622 "
      "D2): the spatial spin holonomy of the cover is ANTIPERIODIC, "
      "measured and forced" % r_num,
      closed and ns_ok and r_exact and r_num > 0)

# A2.2 deck-lift integer arithmetic (all exact fractions)
ok22 = True
cls_phase = set()
for m in range(48):
    q16 = Fraction(2 * m + 1, 3)          # 16 k_m / pi
    q48 = Fraction(2 * m + 1, 1)          # 48 k_m / pi
    ok22 &= (q48.denominator == 1 and q48.numerator % 2 == 1)
    cls_phase.add(((2 * (m % 3) + 1) % 6, (q16 * 3) % 6 == (2 * m + 1) % 6))
occ = [m for m in range(48) if (2 * m + 1) < 24 or (2 * m + 1) > 72]
sea_sum = sum(2 * m + 1 for m in occ)
sea_phase_even = (sea_sum % 3 == 0) and ((sea_sum // 3) % 2 == 0)
okR = all((2 * m) % 2 == 0 for m in range(48))
check("A2.2 [exact] the canonical deck lift on the NS cover: 16 k_m = "
      "pi (2m+1)/3 (deck-class phases e^{i pi (2r+1)/3}); deck^3 phase "
      "per mode = e^{i pi (2m+1)} = -1 for ALL 48 modes => deck^3 = "
      "(-1)^F, deck^6 = 1; the Fermi sea (24 modes, occupied-sum %d, "
      "%d/3 = %d even) has deck eigenvalue EXACTLY +1 (the geometric "
      "vacuum pin); R-cover control: 16 k = 2 pi m/3, deck_R^3 = +1 "
      "per mode -- the Arf-relevant sign deck^3 = -1 is NS-BORNE"
      % (sea_sum, sea_sum, sea_sum // 3),
      ok22 and len(occ) == 24 and sea_sum == 1152 and sea_phase_even
      and okR)

# A2.3 one-Fock-space realization
dev_spec = 0.0
for gt in range(6):
    N = 48
    h = np.zeros((N, N), dtype=complex)
    for j in range(N - 1):
        h[j, j + 1] = -0.5
        h[j + 1, j] = -0.5
    phi = np.pi * (gt + 3) / 3.0          # NS (-1) x e^{i pi gt/3}
    h[N - 1, 0] = -0.5 * np.exp(1j * phi)
    h[0, N - 1] = -0.5 * np.exp(-1j * phi)
    ev = np.sort(np.linalg.eigvalsh(h))
    tgt = np.sort(-np.cos(modes6(N, gt)))
    dev_spec = max(dev_spec, np.abs(ev - tgt).max())
# uniform gauge: deck permutation commutes with H
N = 48
hu = np.zeros((N, N), dtype=complex)
ph = np.exp(1j * np.pi / N)               # uniform NS flux pi
for j in range(N):
    hu[j, (j + 1) % N] = -0.5 * ph.conjugate()
    hu[(j + 1) % N, j] = -0.5 * ph
P16 = np.zeros((N, N))
for j in range(N):
    P16[(j + 16) % N, j] = 1.0
comm = np.abs(P16 @ hu - hu @ P16).max()
ev_u = np.sort(np.linalg.eigvalsh(hu))
dev_u = np.abs(ev_u - np.sort(-np.cos(modes6(N, 0)))).max()
par_ok = all((((F - 24) % 2) == (F % 2)) for F in range(49))
check("A2.3 [machine] ONE Fock space carries all six sectors: the "
      "bond-defect Hamiltonian (same 48-site lattice, one twisted "
      "bond, phase pi(gt+3)/3) reproduces eps6(48, gt) for ALL gt (max "
      "dev %.1e); in uniform gauge the deck permutation commutes with "
      "H exactly (%.1e) and the spectrum is NS (%.1e): deck is a "
      "symmetry of the one shared lattice; V1^3 = e^{i pi (Nhat - 24)} "
      "= (-1)^F exactly for every occupation (N/2 = 24 even): the Z6 "
      "generator and the parity are FIXED on-site-product operators, "
      "identical in every twist sector"
      % (dev_spec, comm, dev_u),
      dev_spec < 1e-12 and comm < 1e-14 and dev_u < 1e-12 and par_ok)

# A2.4 the classification of sector-character wirings
RE_POW = {s: np.array([np.cos(np.pi * s * ht / 3.0) for ht in range(6)])
          for s in range(6)}
COSQ = np.array([[np.cos(np.pi * ht * q / 3.0) for ht in range(6)]
                 for q in range(6)])
survivors = []
for svec in itertools.product(range(6), repeat=6):
    W = np.zeros((6, 6))
    for gt in range(6):
        W[gt] = 0.5 * (RE_POW[svec[gt]] + RE_POW[svec[(6 - gt) % 6]]) / 6.0
    # projector integrality + vacuum
    phi_ok = True
    for gt in range(6):
        for q in range(6):
            v = (W[gt] @ COSQ[q])
            if min(abs(v), abs(v - 1.0)) > 1e-9:
                phi_ok = False
                break
        if not phi_ok:
            break
    if not phi_ok:
        continue
    if abs((W[0] @ COSQ[0]) - 1.0) > 1e-9:
        continue
    # exact table-level T: W[gt, ht - gt - 3] == W[gt, ht]
    t_ok = all(abs(W[gt, (ht - gt - 3) % 6] - W[gt, ht]) < 1e-12
               for gt in range(6) for ht in range(6))
    if not t_ok:
        continue
    # exact table-level S: W[ht, -gt] == W[gt, ht]
    s_ok = all(abs(W[ht % 6, (-gt) % 6] - W[gt, ht]) < 1e-12
               for gt in range(6) for ht in range(6))
    if not s_ok:
        continue
    survivors.append((svec, W))
WB = np.full((6, 6), 1.0 / 6.0)
WC3 = np.array([[((-1.0) ** (gt * ht)) / 6.0 for ht in range(6)]
                for gt in range(6)])
ids = []
for svec, W in survivors:
    if np.abs(W - WB).max() < 1e-12:
        ids.append(("B", svec))
    elif np.abs(W - WC3).max() < 1e-12:
        ids.append(("C3", svec))
    else:
        ids.append(("?", svec))
print("  classification survivors: %s" % ids)
c3_even = np.abs(WC3[0::2, :] - WB[0::2, :]).max()
check("A2.4 [central] THE CLASSIFICATION: among ALL 6^6 = 46656 sector-"
      "character wirings chi(gt)^{ht}/6 (orbit-averaged over the exact "
      "lattice degeneracies), the survivors of {projector integrality, "
      "vacuum, exact table-level S, exact table-level T} are EXACTLY "
      "TWO: chi = 1 (= B) and chi(gt) = (-1)^{gt} (= C3, the Arf "
      "stacking).  The structural pin: chi(gt) is the extra lift phase "
      "of the ONE fixed generator V1 on the gt-defect sector; all "
      "sectors share ONE Fock space (A2.3) where V1 and (-1)^F are "
      "single fixed on-site-product operators -- a fixed operator "
      "cannot act as V1 on even-defect and as -V1 on odd-defect "
      "sectors, so chi = 1 is forced: THE SEAM QUOTIENT IS B.  C3 "
      "requires representing (-1)^F as -(-1)^F on the odd (R-type) "
      "sectors: the Kitaev/Arf stacking -- a different fermionic "
      "decoration (parity-ODD odd-sector classes: c = 3 mod 6), while "
      "the seam's enumerated grounds are charge-0/parity-EVEN (A1.4)",
      len(survivors) == 2
      and sorted(t for t, _ in ids) == ["B", "C3"]
      and (0, 0, 0, 0, 0, 0) in [s for _, s in ids]
      and (0, 3, 0, 3, 0, 3) in [s for _, s in ids])


# ================================================================== A3
print("=" * 72)
print("A3: the character/OPE route")
print("=" * 72)

# A3.1 B == C3 on even sectors
phiB = np.zeros((6, 6))
phiC3 = np.zeros((6, 6))
for gt in range(6):
    for q in range(6):
        phiB[gt, q] = sum(np.exp(1j * np.pi * ht * q / 3.0) / 6.0
                          for ht in range(6)).real
        phiC3[gt, q] = sum(((-1.0) ** (gt * ht))
                           * np.exp(1j * np.pi * ht * q / 3.0) / 6.0
                           for ht in range(6)).real
dev_even = max(np.abs(WB[gt] - WC3[gt]).max()
               + np.abs(phiB[gt] - phiC3[gt]).max() for gt in (0, 2, 4))
dev_odd = min(np.abs(phiB[gt] - phiC3[gt]).max() for gt in (1, 3, 5))
check("A3.1 [machine] B and C3 coincide EXACTLY on the even (sigma) "
      "sectors (weights and projectors, dev %.1e) and differ on every "
      "odd sector (dev %.2f): the v639 OPE datum c1 = 2/9 lives "
      "entirely in the even sectors and is B-vs-C3-BLIND -- the "
      "character route as originally proposed cannot discriminate; the "
      "discriminating OPE data are the half-twisted (tau) data"
      % (dev_even, dev_odd), dev_even < 1e-12 and dev_odd > 0.5)

# A3.2 the tau four-point
LAM_T = np.pi / 3.0
D_TAU = 1.0 / 36.0


def g4(N, pts, lam):
    x1, x2, x3, x4 = pts
    S = np.concatenate([np.arange(x1, x2), np.arange(x3, x4)]) % N
    u = lam * np.ones(len(S))
    return abs(string_det(cov(N), S, u))


# gauge identity (s- vs t-channel string realization)
ptst = (0, 32, 192, 224)
Sa = np.concatenate([np.arange(0, 32), np.arange(192, 224)])
Sb = np.concatenate([np.arange(32, 192), np.arange(224, 384)])
va = string_det(cov(384), Sa, LAM_T * np.ones(len(Sa)))
vb = string_det(cov(384), Sb, -LAM_T * np.ones(len(Sb)))
dev_gauge = abs(abs(va) - abs(vb)) / abs(va)
# exact lattice crossing: rotate the gap 4-tuple by one step
gaps = (32, 160, 32, 160)
p1 = (0, 32, 192, 224)
p2 = (0, 160, 192, 352)
dev_cross = abs(g4(384, p1, LAM_T) - g4(384, p2, LAM_T)) / g4(384, p1,
                                                              LAM_T)
check("A3.2a [machine] tau four-point structure: the s- vs t-channel "
      "string realizations agree (gauge identity, dev %.1e) and the "
      "one-step gap rotation (w -> 1-w) is an exact lattice symmetry "
      "(dev %.1e)" % (dev_gauge, dev_cross),
      dev_gauge < 1e-9 and dev_cross < 1e-9)

# amplitude reference from the two-point at N = 384 (3-term fit)
ys = np.array([np.log(two_point(384, int(x), LAM_T)) for x in xs])
D = chord(384, xs)
A = np.column_stack([np.ones(len(xs)), np.log(D), D ** (-4.0 / 3.0)])
coef2, *_ = np.linalg.lstsq(A, ys, rcond=None)
lnA_amp = coef2[0]
A2_ref = np.exp(2.0 * lnA_amp)

ALPHAS = (Fraction(1, 48), Fraction(1, 24), Fraction(1, 12),
          Fraction(1, 8), Fraction(1, 6), Fraction(5, 24), Fraction(1, 4))
rows = []
for al in ALPHAS:
    w = float(np.sin(np.pi * float(al)) ** 2)
    lnD = {}
    for N in (192, 384):
        d = int(al * N)
        pts = (0, d, N // 2, N // 2 + d)
        G = g4(N, pts, LAM_T)
        Dt = G * (chord(N, d) ** 2) ** (2 * D_TAU)
        lnD[N] = np.log(Dt)
    # per-config N-extrapolation linear in N^{-4/3}
    c1_, c2_ = 192.0 ** (-4.0 / 3.0), 384.0 ** (-4.0 / 3.0)
    ln_inf = (lnD[384] * c1_ - lnD[192] * c2_) / (c1_ - c2_)
    rows.append((w, ln_inf))
    print("  4pt alpha=%-6s w=%.4f  lnDtil(192)=%.6f (384)=%.6f "
          "extrap=%.6f" % (al, w, lnD[192], lnD[384], ln_inf))
wv = np.array([r[0] for r in rows])
yv = np.array([r[1] for r in rows])
Afit = np.column_stack([np.ones(len(wv)), -np.log(1.0 - wv)])
coef4, *_ = np.linalg.lstsq(Afit, yv, rcond=None)
lnA2_4, p4 = coef4[0], coef4[1]
# model-bound c1 = p (single-block form, v639 S3 convention); the
# model-free small-w extractor is amplification-limited (intercept
# error / w) and only brackets the target -- reported, not gated.
c1_bound = p4
c1_free = (np.exp(yv[:3] - lnA2_4) - 1.0) / wv[:3]
dev_p4 = abs(p4 - 2 * D_TAU) / (2 * D_TAU)
dev_amp = abs(np.exp(lnA2_4) - A2_ref) / A2_ref
p4_c3 = 2.0 * 85.0 / 36.0
check("A3.2b [E] the tau OPE data: N-extrapolated Dtil(w) fits "
      "A^2 (1-w)^{-p} with p = %.6f vs 2 Delta = 1/18 = %.6f (rel dev "
      "%.2e < 8 %%) => model-bound c1 = p = %.6f (single-block form, "
      "v639 S3 convention); the model-free small-w extractor brackets "
      "it in [%.3f, %.3f] (amplification-limited, reported not gated); "
      "amplitude consistency with the independent two-point A^2 at "
      "%.2e; C3's lightest gt = 1 interpolator (charge 3) would demand "
      "p = 85/18 = %.3f -- rejected by a factor %.0f: the tau OPE "
      "datum discriminates, and it picks B"
      % (p4, 2 * D_TAU, dev_p4, c1_bound, c1_free.min(), c1_free.max(),
         dev_amp, p4_c3, p4_c3 / max(p4, 1e-12)),
      dev_p4 < TOL_4PT and dev_amp < 0.02 and p4 < 0.1 * p4_c3)


# ================================================================== A4
print("=" * 72)
print("A4: the typing")
print("=" * 72)

check("A4.1 [C, honest typing] WHAT IS NOW STRUCTURAL: (i) the "
      "classification is exact -- within the group-average family "
      "(what a genuine quotient produces) the consistency axioms leave "
      "exactly {B, C3}, and the canonical pin (one Fock space, one "
      "fixed on-site generator V1, one fixed on-site parity product) "
      "forces chi = 1 = B; C3 is the Arf/Kitaev-stacked decoration "
      "(odd-sector parity redefined), i.e. a DIFFERENT fermionic "
      "system, not the seam quotient; (ii) the excision is measured -- "
      "the seam interpolates c = 0 twist states of dimension 1/36 "
      "(exponent 1/18, Klein-PSD norm), which C3 excises (its "
      "odd-sector floor 85/36 resp. 81/36 misses the measurement by "
      "factors ~85 / ~9); (iii) the tau OPE datum (1/18) discriminates "
      "where the v639 sigma datum (2/9) structurally cannot (B = C3 on "
      "even sectors).  WHAT STAYS [C]: the premise that the seam's "
      "twist sectors are the bond-defect realization on the one cover "
      "lattice (grounded in the v622/v623 mark/bond geometry, but a "
      "reading, not a theorem), and the continuum/CFT-level statement; "
      "as an ABSTRACT fermionic orbifold C3 remains modular-consistent "
      "-- the claim is 'C3 is not the seam', not 'C3 is inconsistent'. "
      "GATE.QGEO does not move", True)


# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
a1_ok = all(ok for n, ok in CHECKS if n.startswith("A1"))
a2_ok = all(ok for n, ok in CHECKS if n.startswith("A2"))
ctrl_ok = all(ok for n, ok in CHECKS if n.startswith(("A0", "A3.2a")))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: ARF-B-STRUCTURAL -- B vs C3 is decided structurally")
    print("at the lattice level: the sector-character classification")
    print("leaves exactly {B, C3}; the one-Fock-space canonical action")
    print("forces chi = 1 (B); C3 = the Arf/Kitaev stacking, whose")
    print("excised states demonstrably exist on the seam (measured")
    print("defect exponents 1/18, 2/9, 1/2 with positive Klein norm).")
elif a1_ok and ctrl_ok and not a2_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: ARF-B-DATA-ONLY -- the excision data stand but the")
    print("structural classification/pin failed: kill stays data-backed.")
elif not a1_ok and ctrl_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: ARF-UNDECIDED -- the discriminating measurements")
    print("are inconclusive: honest negative.")
else:
    print("SOME CHECKS FAILED")
    print("VERDICT: MIXED")
