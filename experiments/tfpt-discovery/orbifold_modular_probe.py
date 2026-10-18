#!/usr/bin/env python3
"""Discovery probe: MODULAR DATA of the Z3 orbifold of the seam on the
lattice -- the nine twisted-sector partition functions Z[g,h] of the
seam double (free complex fermion) on the N x L cylinder, their modular
S-covariance (MEASURED, with a convergence rate in N), the twisted
character exponents against h_sigma = 1/36, and the deck^3 = -1
spin-structure bookkeeping (v623) as exact Z6 phase arithmetic.

CONVENTIONS (declared up front; everything below hangs on these):

  * SEAM DOUBLE: one complex free fermion = the doubled Majorana seam
    (v622 doubled bookkeeping; a single Majorana cannot be
    omega-twisted -- orbifold_twist_ope_probe.py T0).  Lattice: N-site
    hopping chain, dispersion eps(k) = -cos k, half filling, Fermi
    velocity v = 1.  NS BASIS: the untwisted spatial sector is
    ANTIPERIODIC, momenta k = 2 pi (m + 1/2)/N.
  * TWIST SECTORS: the spatial Z3 twist g is the phase boundary
    condition psi(x+N) = -omega^g psi(x) (NS times omega^g), i.e.
    momenta k = 2 pi (m + 1/2 + g/3)/N.  The temporal insertion h is
    the CHARGE-SYMMETRIC Z3 phase U_h = exp(i lam_h (Nhat - N/2)),
    lam_h = 2 pi h/3 (the zero-mode dressing of
    parafermion_klein_rp_probe.py; N even makes U_{h+3} consistent).
    Euclidean time is CONTINUOUS (Hamiltonian transfer matrix,
    H = sum_k eps_k (n_k - 1/2)), time length L, tau = i L/N (v = 1).
    Exact free-fermion product:
      Z[g,h] = prod_k 2 cosh((L eps_k - i lam_h)/2),
    plain trace = ANTIPERIODIC time; the (-1)^F insertion is
    lam -> lam + pi.  Z[g,h] is exactly REAL AND POSITIVE (k -> -k
    reflection + particle-hole at half filling; machine-checked).
  * EXACT LATTICE DEGENERACIES (checked): Z[g,h] = Z[-g,h] = Z[g,-h]
    (charge conjugation of the double): only the four sectors
    (g,h) in {0,1}^2 are independent -- exactly the continuum
    conjugate-sector degeneracy of the Z3 orbifold.
  * CONTINUUM TARGET: Z_cft[g,h](tau) = |theta[g/3, h/3](0|tau) /
    eta(tau)|^2 (theta with characteristics; theta[0,0] = theta_3 =
    the known NS-NS Dirac answer), S: Z[g,h](-1/tau) = Z[h,-g](tau).
    Lattice Casimir coefficient in pi/N units:
    C_g = 8 (h_nu - c/24)|_{c=1/2} = 4 x the v628 per-class datum:
    C = (-1/6, 1/18, 1/18) for g = (0, 1, 2), i.e. C_g/4 =
    (-1/24, 1/72, 1/72) -- the seam double carries FOUR real chiral
    deck families (complex doubling x two chiralities), each with the
    v628 coefficient (6 nu^2 - 6 nu + 1)/12 = 2(h_nu - c/24).
  * MODULAR MAPS ON THE LATTICE: S is realized by exchanging the
    N <-> L roles (rotated lattice) with (g,h) -> (h,-g); it is NOT an
    exact lattice symmetry (space is a discrete cos-band, time is
    continuous) -- the S-deviation vs N IS the measurement (M2).
    T is realized EXACTLY: the discrete Dehn twist = translation by N
    sites, which acts on the g-sector as (-omega^g)^{Nhat}, i.e.
    (g,h) -> (g, g+h) PLUS a fermion-parity flip -- the Z6
    spin-structure shift, an exact operator identity (M2.4); the
    continuum T-PHASES per character are NOT resolvable in the
    real-positive trace convention and stay OPEN (M5), so only S is
    MEASURED.

Checks:

  (C0) CONTINUUM REFERENCE INTEGRITY [machine]: the product form of
       Z_cft equals the theta_3-series/eta form at (0,0) (the known NS
       partition function) and |theta[g/3,h/3]/eta|^2 for all nine
       sectors, and the reference itself is exactly S-covariant
       (theta-transform, numerically < 1e-9).

  (M1) THE NINE Z[g,h] [E-float]: exact reality/positivity, half
       filling in every twist sector, the exact lattice degeneracies
       Z[g,h] = Z[-g,h] = Z[g,-h], Z3 periodicity of the insertion
       (N even); the 9 x 3 table (tau = i/2, i, 2i; N = 48) matches
       Z_cft at < 1 % on ln Z after removing the exact bulk N L/pi;
       the L -> infinity Casimir slope fit reproduces
       C_g/4 = (-1/24, 1/72, 1/72) per g-sector at < 1 % (v628).

  (M2) MODULAR S-COVARIANCE, MEASURED [central]: Z[g,h] at tau vs the
       rotated lattice Z[h,-g] (N <-> L), relative deviation as a
       function of N (N = 24/48/96): tau = i (the self-dual point,
       one dynamical relation Z[1,0] vs Z[0,1]) and tau = i/2 <-> 2i
       (all nine, four independent).  PASS = every dynamical deviation
       decreases monotonically in N with a stable rate; the rate is
       REPORTED.  MEASURED RESULT: the S-deviation falls ~ N^{-4},
       FASTER than the naive N^{-2} dispersion artifact -- the
       single-lattice deviation from the continuum reference falls
       ~ N^{-2} (measured alongside), so the leading N^{-2} lattice
       artifact is itself S-COVARIANT and cancels in the S-relation;
       only the N^{-4} tail survives.  Both rates are measured.
       T [E]: the exact Dehn identity Z_T[g,h] = Z^F[g, g+h] at
       machine precision (the Z6 shift; phases beyond it: open).

  (M3) q-EXPANSION / CHARACTER EXPONENTS [E-float, N = 48]: the
       leading exponent of Z[1,0]/Z[0,0] gives the twisted ground
       state Delta_sigma = 1/9 = 4 h_sigma, i.e. h_sigma = 1/36 per
       deck class (v639 dictionary) at < 1 %; the next gap in the
       twisted sector is the parafermionic moding 1/6 (= 1/2 - 1/3,
       the {1/6, 5/6} twisted pair) with multiplicity 2 at < 1 %/2 %;
       the omega^{k q} charge bookkeeping in TIME: the level-1/6
       weight in Z[1,1]/Z[1,0] is 2 cos(2 pi/3) - 2 = -3 (< 2 %).

  (M4) SPIN-STRUCTURE BOOKKEEPING [E, machine]: on the 48-site cover
       (deck = translation by 16, v623) the deck insertion phases are
       the Z6 values e^{i pi (2r+1)/3} per deck class (r = m mod 3),
       deck^3 = (-1)^F and deck^6 = 1 as EXACT partition-function
       identities; the cover trace FACTORIZES exactly into the three
       base-sector (N = 16) traces with per-class insertion
       (-1)^h omega^{g~ h} -- the Z3 twist lifts to a Z6 structure on
       the double, exactly as deck^3 = -1 demands; parity projections
       Z^{+-} = (Z +- Z^F)/2 are nonnegative state counters in the
       h = 0 column, every sector ground state is parity-EVEN
       (charge-0), the odd towers open at gap (1/2, 1/6, 1/6) for
       g = (0, 1, 2) (< 1 %), and the POSITIVE bookkeeping of the
       full Z6 insertion family is the Z6 CHARGE PROJECTION
       P_c[g] = (1/6) sum_j e^{-i pi j c/3} Tr[e^{i pi j (Nhat-N/2)/3}
       e^{-LH}] (projector on (Nhat - N/2) mod 6): all six P_c >= 0
       per g-sector, summing to Z[g,0], ground charge class c = 0.
       HONEST NOTE: for h != 0 the naive ratio Z^F[g,h]/Z[g,h]
       EXCEEDS 1 (measured up to 1.93) -- Z^{+-}[g, h!=0] are
       omega-weighted parity traces, not counters; the Z6 projection
       is the counter.

  (M5) TYPING [C]: what stands on the lattice (S measured with rate,
       characters consistent, Z6/spin bookkeeping exact) and what is
       missing (exact continuum eta/theta identification of chiral
       PHASES, complete T-phases per character, the non-abelian sector
       assembly / orbifold projection sum, continuum OS) -- named, not
       claimed.

Verdict enums (frozen): ORB-MODULAR-COHERENT (all pass: S measured
with a clean rate, characters and Casimir consistent, Z6 bookkeeping
exact), ORB-MODULAR-S-OPEN (M1/M3/M4 pass but the S-deviation has no
clean monotone rate), ORB-MODULAR-FAILS (reference or M1 control level
fails), MIXED (anything else).

FIREWALL: experiments/ only; GATE.QGEO does not move; no marker
changes; verification/ untouched.

Conventions inherited read-only from orbifold_twist_ope_probe.py,
parafermion_klein_rp_probe.py, v622/v623/v628/v639.
"""

import numpy as np

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------------ constants
OMEGA = np.exp(2j * np.pi / 3.0)
N_MAIN = 48                       # the covered-seam scale (v623)
N_BASE = 16                       # the base seam (v622)
NS_M2 = (24, 48, 96)              # S-covariance N series
TAUS = ((0.5, 24), (1.0, 48), (2.0, 96))   # (beta, L) at N = 48
C_TARGET = {0: -1.0 / 6.0, 1: 1.0 / 18.0, 2: 1.0 / 18.0}
V628 = {0: -1.0 / 24.0, 1: 1.0 / 72.0, 2: 1.0 / 72.0}
H_SIGMA = 1.0 / 36.0              # v639 per-deck-class twist weight
DELTA_SIGMA = 4.0 * H_SIGMA       # lattice twist dimension 1/9
GAP2 = 1.0 / 6.0                  # parafermionic next gap (1/2 - 1/3)
TOL_MACH = 1e-9                   # machine-precision identities (on lnZ)
TOL_FIT = 0.01                    # 1 % on exponents / Casimir / table
TOL_MULT = 0.02                   # 2 % on multiplicities / weights
MAX_IMAG = [0.0]                  # running reality-deviation tracker


# ------------------------------------------------------------------ machinery
def modes(N, g):
    """g-twisted NS momenta k = 2 pi (m + 1/2 + g/3)/N."""
    m = np.arange(N)
    return 2.0 * np.pi * (m + 0.5 + (g % 3) / 3.0) / N


def eps_of(N, g):
    return -np.cos(modes(N, g))


def ln2cosh(z):
    """Stable elementwise log(2 cosh z) for complex z."""
    zs = np.where(z.real >= 0, z, -z)
    return zs + np.log(1.0 + np.exp(-2.0 * zs))


def lnZ_lam(N, L, g, lam):
    """Complex ln Z for insertion exp(i lam (Nhat - N/2)):
    sum_k log 2cosh((L eps_k - i lam)/2)."""
    z = 0.5 * (L * eps_of(N, g) - 1j * lam)
    return ln2cosh(z).sum()


def lnZ(N, L, g, h, parity=False):
    """Real ln Z[g,h] (optionally with (-1)^F); returns (lnZ, sign) and
    tracks the reality deviation |e^{i Im} -+ 1|."""
    lam = 2.0 * np.pi * (h % 3) / 3.0 + (np.pi if parity else 0.0)
    val = lnZ_lam(N, L, g, lam)
    ph = np.exp(1j * val.imag)
    dev_p, dev_m = abs(ph - 1.0), abs(ph + 1.0)
    MAX_IMAG[0] = max(MAX_IMAG[0], min(dev_p, dev_m))
    return val.real, (1.0 if dev_p <= dev_m else -1.0)


def lnZr(N, L, g, h):
    """Plain real ln Z[g,h] (must be positive; sign asserted)."""
    v, s = lnZ(N, L, g, h)
    assert s > 0
    return v


def lnZraw(N, L, g, theta):
    """Complex ln of Tr[prod_k e^{i theta_k n_k} e^{-L H}] with RAW
    per-mode phases theta_k (no zero-mode dressing):
    prod_k (e^{L eps_k/2} + e^{i theta_k} e^{-L eps_k/2})."""
    a = 0.5 * L * eps_of(N, g)
    th = np.broadcast_to(np.asarray(theta, dtype=float), (N,))
    out = np.empty(N, dtype=complex)
    pos = a >= 0
    out[pos] = a[pos] + np.log(1.0 + np.exp(1j * th[pos] - 2.0 * a[pos]))
    out[~pos] = (-a[~pos] + 1j * th[~pos]
                 + np.log(1.0 + np.exp(-1j * th[~pos] + 2.0 * a[~pos])))
    return out.sum()


def E0_exact(N, g):
    """Exact twisted-sector ground-state energy (mode sum)."""
    eps = eps_of(N, g)
    assert (eps < 0).sum() == N // 2      # half filling in every sector
    return eps[eps < 0].sum()


def lnZcft(g, h, beta, M=2000):
    """Continuum ln Z_cft[g,h](tau = i beta): q^{C_g/2} times the four
    real chiral deck families, q = e^{-2 pi beta}."""
    lnq = -2.0 * np.pi * beta
    lam = 2.0 * np.pi * (h % 3) / 3.0
    a0 = (0.5 + (g % 3) / 3.0) % 1.0
    m = np.arange(M)
    tot = 0.5 * C_TARGET[g % 3] * lnq
    for a in (m + a0, m + 1.0 - a0):
        qa = np.exp(lnq * a)
        tot += np.sum(np.log(1.0 + 2.0 * np.cos(lam) * qa + qa * qa))
    return tot


def theta_ab(a, b, beta, M=80):
    """theta[a,b](0 | i beta) = sum_n e^{-pi beta (n+a)^2 + 2 pi i (n+a) b}."""
    n = np.arange(-M, M + 1)
    return np.sum(np.exp(-np.pi * beta * (n + a) ** 2
                         + 2j * np.pi * (n + a) * b))


def ln_eta(beta, M=4000):
    n = np.arange(1, M)
    return -np.pi * beta / 12.0 + np.sum(np.log1p(-np.exp(-2.0 * np.pi
                                                          * beta * n)))


# ================================================================== C0
print("=" * 72)
print("C0: continuum reference integrity (theta/eta bookkeeping)")
print("=" * 72)

# C0.1 the reference is exactly S-covariant: Z[g,h](i/beta) = Z[h,-g](i beta)
dev_s = 0.0
for beta in (0.5, 1.0, 2.0):
    for g in range(3):
        for h in range(3):
            dev_s = max(dev_s, abs(lnZcft(g, h, 1.0 / beta)
                                   - lnZcft(h, (-g) % 3, beta)))
check("C0.1 the continuum reference Z_cft[g,h] = |theta[g/3,h/3]/eta|^2 "
      "is EXACTLY S-covariant, Z[g,h](-1/tau) = Z[h,-g](tau) (all nine "
      "sectors, beta = 1/2, 1, 2)", dev_s < TOL_MACH,
      "max |dev lnZ| = %.3e" % dev_s)

# C0.2 (0,0) = the known NS-NS Dirac partition function |theta_3/eta|^2
dev_ns = max(abs(lnZcft(0, 0, beta)
                 - 2.0 * (np.log(theta_ab(0.0, 0.0, beta).real)
                          - ln_eta(beta)))
             for beta in (0.5, 1.0, 2.0))
check("C0.2 Z_cft[0,0] equals the KNOWN NS partition function "
      "|theta_3/eta|^2 (theta_3 as its own lattice-independent series)",
      dev_ns < TOL_MACH, "max dev = %.3e" % dev_ns)

# C0.3 all nine sectors are |theta[g/3, h/3]/eta|^2
dev_th = 0.0
for beta in (0.5, 1.0):
    for g in range(3):
        for h in range(3):
            t = theta_ab(g / 3.0, h / 3.0, beta)
            dev_th = max(dev_th, abs(lnZcft(g, h, beta)
                                     - 2.0 * (np.log(abs(t))
                                              - ln_eta(beta))))
check("C0.3 all nine reference sectors are theta quotients: "
      "Z_cft[g,h] = |theta[g/3, h/3](0|tau)/eta(tau)|^2 exactly",
      dev_th < TOL_MACH, "max dev = %.3e" % dev_th)


# ================================================================== M1
print("=" * 72)
print("M1: the nine Z[g,h] on the lattice (N = 48; tau = i/2, i, 2i)")
print("=" * 72)

# M1.1 exact structure: reality, degeneracies, Z3 periodicity
dev_deg = 0.0
for (beta, L) in TAUS:
    for g in range(3):
        for h in range(3):
            z = lnZr(N_MAIN, L, g, h)
            dev_deg = max(dev_deg,
                          abs(z - lnZr(N_MAIN, L, (-g) % 3, h)),
                          abs(z - lnZr(N_MAIN, L, g, (-h) % 3)))
# Z3 periodicity of the RAW (unreduced) insertion lam -> lam + 2 pi (N even)
per = lnZ_lam(N_MAIN, 48, 1, 2.0 * np.pi / 3.0)
per3 = lnZ_lam(N_MAIN, 48, 1, 2.0 * np.pi / 3.0 + 2.0 * np.pi)
dev_per = (abs(per.real - per3.real)
           + abs(np.exp(1j * (per.imag - per3.imag)) - 1.0))
check("M1.1 exact lattice structure: Z[g,h] is REAL POSITIVE (max "
      "reality dev %.1e), every twist sector is half filled, the "
      "charge-conjugation degeneracies Z[g,h] = Z[-g,h] = Z[g,-h] hold "
      "at machine precision, and the insertion is Z3-periodic "
      "(U_{h+3} = U_h, N even)" % MAX_IMAG[0],
      MAX_IMAG[0] < TOL_MACH and dev_deg < TOL_MACH and dev_per < TOL_MACH,
      "max degeneracy dev = %.3e, periodicity dev = %.3e"
      % (dev_deg, dev_per))

# M1.2 the 9 x 3 table vs the continuum reference
print("  lnZhat = lnZ - N L/pi vs continuum (N = 48):")
print("  %-6s %-6s %14s %14s %11s" % ("tau", "(g,h)", "lattice",
                                      "continuum", "|dev|"))
dev_tab = 0.0
for (beta, L) in TAUS:
    for g in range(3):
        for h in range(3):
            zl = lnZr(N_MAIN, L, g, h) - N_MAIN * L / np.pi
            zc = lnZcft(g, h, beta)
            d = abs(zl - zc)
            dev_tab = max(dev_tab, d)
            if (g, h) in ((0, 0), (0, 1), (1, 0), (1, 1)):
                print("  %-6s (%d,%d) %14.8f %14.8f %11.3e"
                      % ("i" if beta == 1 else ("i/2" if beta == 0.5
                                                else "2i"), g, h, zl, zc, d))
check("M1.2 the full 9 x 3 lattice table (tau = i/2, i, 2i at N = 48) "
      "matches the continuum |theta[g/3,h/3]/eta|^2 at < 1 %% on ln Z "
      "after removing the exact bulk N L/pi (four independent sectors "
      "shown; the other five are exact degenerates)" % (),
      dev_tab < TOL_FIT, "max |dev lnZ| = %.3e" % dev_tab)

# M1.3 Casimir limit L -> infinity: slope fit vs v628 per-class data
#      (L = 768/960: the twisted-sector e^{-delta L} tail is < 1e-9)
print("  Casimir coefficients (pi/N units), N = 48:")
cas_ok, fit_vs_exact = True, 0.0
for g in range(3):
    lz1, lz2 = lnZr(N_MAIN, 768, g, 0), lnZr(N_MAIN, 960, g, 0)
    E0_fit = -(lz2 - lz1) / 192.0
    E0_ex = E0_exact(N_MAIN, g)
    fit_vs_exact = max(fit_vs_exact, abs(E0_fit - E0_ex))
    C_fit = (E0_fit + N_MAIN / np.pi) * N_MAIN / np.pi
    rel = abs(C_fit / 4.0 - V628[g]) / abs(V628[g])
    cas_ok &= rel < TOL_FIT
    print("    g=%d  E0_fit=%.9f  E0_exact=%.9f  C=%.6f  C/4=%.6f "
          "vs v628 %.6f  (rel dev %.2e)"
          % (g, E0_fit, E0_ex, C_fit, C_fit / 4.0, V628[g], rel))
check("M1.3 the L -> infinity Casimir slope of ln Z[g,0] reproduces the "
      "v628 coefficients per deck class: C_g/4 = (-1/24, 1/72, 1/72) "
      "for g = (0,1,2) at < 1 %% (dictionary C_g = 4 x v628: complex "
      "doubling x two chiralities; slope fit vs exact mode sum "
      "agrees to %.1e)" % fit_vs_exact,
      cas_ok and fit_vs_exact < 1e-6)


# ================================================================== M2
print("=" * 72)
print("M2: modular S-covariance, MEASURED (N = 24/48/96)")
print("=" * 72)

# tau = i, the self-dual point: the single dynamical relation
dev_i = {N: abs(lnZr(N, N, 1, 0) - lnZr(N, N, 0, 2)) for N in NS_M2}
rates_i = [np.log(dev_i[24] / dev_i[48]) / np.log(2.0),
           np.log(dev_i[48] / dev_i[96]) / np.log(2.0)]
print("  tau = i (self-dual): |lnZ[1,0] - lnZ[0,-1]| per N:")
print("    " + "  ".join("N=%d: %.3e" % (N, dev_i[N]) for N in NS_M2)
      + "   rates: %.3f, %.3f" % tuple(rates_i))
check("M2.1 S at the self-dual point tau = i: the dynamical relation "
      "Z[1,0] = Z[0,-1] (space twist <-> time twist) converges "
      "monotonically in N with a stable rate (the other seven "
      "relations at tau = i are EXACT lattice degeneracies)",
      dev_i[24] > dev_i[48] > dev_i[96]
      and abs(rates_i[0] - rates_i[1]) < 0.5,
      "rates %.3f / %.3f" % tuple(rates_i))

# tau = i/2 <-> 2i: all nine (four independent)
INDEP = ((0, 0), (0, 1), (1, 0), (1, 1))
print("  tau = i/2 <-> 2i: |lnZ^{(N,N/2)}[g,h] - lnZ^{(N/2,N)}[h,-g]|:")
print("  %-6s %12s %12s %12s %9s %9s" % ("(g,h)", "N=24", "N=48",
                                         "N=96", "rate1", "rate2"))
dev_half, rates_half = {}, {}
for g in range(3):
    for h in range(3):
        ds = [abs(lnZr(N, N // 2, g, h) - lnZr(N // 2, N, h, (-g) % 3))
              for N in NS_M2]
        dev_half[(g, h)] = ds
        r = [np.log(ds[0] / ds[1]) / np.log(2.0),
             np.log(ds[1] / ds[2]) / np.log(2.0)]
        rates_half[(g, h)] = r
        tag = "  *" if (g, h) in INDEP else "   "
        print("  (%d,%d)%s %12.4e %12.4e %12.4e %9.3f %9.3f"
              % (g, h, tag, ds[0], ds[1], ds[2], r[0], r[1]))
mono = all(dev_half[k][0] > dev_half[k][1] > dev_half[k][2]
           for k in INDEP)
check("M2.2 S at tau = i/2 <-> 2i (rotated lattice, N <-> L): all nine "
      "(g,h) deviations DECREASE monotonically over N = 24/48/96 "
      "(four independent relations, marked *; the rest are exact "
      "degenerates of these)", mono,
      "worst N=96 deviation = %.3e"
      % max(dev_half[k][2] for k in INDEP))

all_rates = [r for k in INDEP for r in rates_half[k]] + rates_i
fine_rates = ([rates_half[k][1] for k in INDEP] + [rates_i[1]])
rate_mean = float(np.mean(fine_rates))
rate_spread = float(np.max(fine_rates) - np.min(fine_rates))
# the single-lattice deviation from the continuum reference (tau = i):
# measures the RAW lattice artifact that S could have seen
cft_dev = {}
for N in NS_M2:
    cft_dev[N] = max(abs((lnZr(N, N, g, h) - N * N / np.pi)
                         - lnZcft(g, h, 1.0))
                     for (g, h) in INDEP)
cft_rates = [np.log(cft_dev[24] / cft_dev[48]) / np.log(2.0),
             np.log(cft_dev[48] / cft_dev[96]) / np.log(2.0)]
print("  single-lattice vs continuum (tau = i, worst of the four "
      "independent sectors):")
print("    " + "  ".join("N=%d: %.3e" % (N, cft_dev[N]) for N in NS_M2)
      + "   rates: %.3f, %.3f" % tuple(cft_rates))
check("M2.3 the S-convergence RATE is clean and common across sectors "
      "AND is N^{-4}, not N^{-2}: fine-pair rate %.3f (spread %.3f "
      "over the five dynamical relations), while the SINGLE-LATTICE "
      "deviation from the continuum falls with rate ~ %.2f (= the "
      "naive N^{-2} dispersion artifact) -- the leading N^{-2} "
      "lattice artifact is itself S-covariant and CANCELS in the "
      "S-relation; the measured S-answer is N^{-4}"
      % (rate_mean, rate_spread, float(np.mean(cft_rates))),
      3.5 < rate_mean < 4.5 and rate_spread < 0.5
      and 1.5 < float(np.mean(cft_rates)) < 2.5,
      "S rates = %s; cft rates = %s"
      % (np.array2string(np.array(all_rates), precision=3),
         np.array2string(np.array(cft_rates), precision=3)))

# M2.4 T as the EXACT discrete Dehn twist (Z6 shift bookkeeping)
dev_T = 0.0
for g in range(3):
    for h in range(3):
        lam_h = 2.0 * np.pi * h / 3.0
        theta = lam_h + N_MAIN * modes(N_MAIN, g)     # U_h x shift by N
        lhs = lnZraw(N_MAIN, 48, g, theta) - 1j * lam_h * (N_MAIN / 2.0)
        lam_hg = 2.0 * np.pi * ((h + g) % 3) / 3.0 + np.pi
        rhs = lnZ_lam(N_MAIN, 48, g, lam_hg)
        dev_T = max(dev_T, abs(lhs.real - rhs.real)
                    + abs(np.exp(1j * (lhs.imag - rhs.imag)) - 1.0))
check("M2.4 [E] T on the lattice is the EXACT discrete Dehn twist "
      "(translation by N sites): per occupied mode e^{i k N} = "
      "-omega^g, hence Z_T[g,h] = Z^F[g, g+h] -- the sector map "
      "(g,h) -> (g, g+h) PLUS a fermion-parity flip (the Z6 "
      "spin-structure shift), machine-exact for all nine sectors; the "
      "continuum T-PHASES per character are not resolvable in the "
      "real-positive trace convention: only S is MEASURED (honest "
      "scope, see M5)", dev_T < TOL_MACH, "max dev = %.3e" % dev_T)


# ================================================================== M3
print("=" * 72)
print("M3: q-expansion -- twisted character exponents (N = 48)")
print("=" * 72)

# M3.1 the leading twisted exponent: Delta_sigma = 1/9 = 4 h_sigma
#      (L = 768/960: the e^{-delta L} tail of the fit is < 1e-9)
lr1 = lnZr(N_MAIN, 768, 1, 0) - lnZr(N_MAIN, 768, 0, 0)
lr2 = lnZr(N_MAIN, 960, 1, 0) - lnZr(N_MAIN, 960, 0, 0)
dE_fit = -(lr2 - lr1) / 192.0
dE_ex = E0_exact(N_MAIN, 1) - E0_exact(N_MAIN, 0)
Delta_lat = dE_fit * N_MAIN / (2.0 * np.pi)
rel_D = abs(Delta_lat - DELTA_SIGMA) / DELTA_SIGMA
h_lat = Delta_lat / 4.0
check("M3.1 the lowest twisted state: the leading exponent of "
      "Z[1,0]/Z[0,0] gives Delta_sigma = %.8f vs 1/9 = %.8f (rel dev "
      "%.2e < 1 %%), i.e. h_sigma = Delta/4 = %.8f vs 1/36 = %.8f -- "
      "the v639 twist dimension carried by the lowest twisted state"
      % (Delta_lat, DELTA_SIGMA, rel_D, h_lat, H_SIGMA),
      rel_D < TOL_FIT and abs(dE_fit - dE_ex) < 1e-7,
      "slope fit vs exact gap: %.2e" % abs(dE_fit - dE_ex))

# M3.2 the next gap: F(L) = ln(Z[1,0]/Z[0,0]) + L dE_exact
#      = d ln(1 + e^{-delta L}) with d = 2, delta = (2 pi/N)/6
Ls3 = (240, 288, 336)
Fs = [lnZr(N_MAIN, L, 1, 0) - lnZr(N_MAIN, L, 0, 0) + dE_ex * L
      for L in Ls3]
L1, L2 = Ls3[0], Ls3[-1]
F1, F2 = Fs[0], Fs[-1]
lo, hi = 1e-4, 1.0
for _ in range(200):                       # bisection: ratio monotone
    mid = 0.5 * (lo + hi)
    ratio = (np.log1p(np.exp(-mid * L1)) / np.log1p(np.exp(-mid * L2)))
    if ratio < F1 / F2:
        lo = mid
    else:
        hi = mid
delta_fit = 0.5 * (lo + hi)
d_fit = F1 / np.log1p(np.exp(-delta_fit * L1))
resid = abs(Fs[1] - d_fit * np.log1p(np.exp(-delta_fit * Ls3[1])))
gap_lat = delta_fit * N_MAIN / (2.0 * np.pi)
rel_gap = abs(gap_lat - GAP2) / GAP2
check("M3.2 the next twisted gap: F(L) = d ln(1 + e^{-delta L}) fit "
      "gives gap = %.7f vs 1/6 = %.7f (rel dev %.2e < 1 %%) with "
      "multiplicity d = %.5f vs 2 (< 2 %%) -- the parafermionic "
      "twisted-pair moding {1/6, 5/6} (one R-hole + one L-particle), "
      "mid-point residual %.1e"
      % (gap_lat, GAP2, rel_gap, d_fit, resid),
      rel_gap < TOL_FIT and abs(d_fit - 2.0) / 2.0 < TOL_MULT
      and resid < 1e-4)

# M3.3 omega^{k q} charge bookkeeping in TIME: the level-1/6 weight in
#      Z[1,1]/Z[1,0] is (omega + omega^-1) - 2 = -3
LG = 240
G = lnZr(N_MAIN, LG, 1, 1) - lnZr(N_MAIN, LG, 1, 0)
xG = np.exp(-delta_fit * LG)
c_fit = G / xG
rel_c = abs(c_fit - (-3.0)) / 3.0
check("M3.3 the omega^{k q} charge bookkeeping in time: the level-1/6 "
      "weight of Z[1,1]/Z[1,0] is c = %.5f vs 2 cos(2 pi/3) - 2 = -3 "
      "(rel dev %.2e < 2 %%): the h-insertion resolves the +-1 charges "
      "of the twisted pair with exactly the omega phases of the Klein "
      "pairing" % (c_fit, rel_c),
      rel_c < TOL_MULT)


# ================================================================== M4
print("=" * 72)
print("M4: spin-structure bookkeeping -- deck^3 = -1 as Z6 arithmetic")
print("=" * 72)

# M4.1 per-mode deck phases are Z6; deck^3 = (-1)^F, deck^6 = 1 exactly
kc = modes(N_MAIN, 0)                     # 48-site cover, NS
ph_deck = np.exp(1j * N_BASE * kc)        # deck = translation by 16
m_idx = np.arange(N_MAIN)
ph_expect = np.exp(1j * np.pi * (2 * (m_idx % 3) + 1) / 3.0)
dev_ph = np.abs(ph_deck - ph_expect).max()
dev_cube = np.abs(ph_deck ** 3 + 1.0).max()
dev_z1, dev_z2 = 0.0, 0.0
for L in (32, 72):
    z3 = lnZraw(N_MAIN, L, 0, 3.0 * N_BASE * kc)
    zF = lnZ_lam(N_MAIN, L, 0, np.pi)
    dev_z1 = max(dev_z1, abs(z3.real - zF.real)
                 + abs(np.exp(1j * (z3.imag - zF.imag)) - 1.0))
    z6 = lnZraw(N_MAIN, L, 0, 6.0 * N_BASE * kc)
    z0 = lnZ_lam(N_MAIN, L, 0, 0.0)
    dev_z2 = max(dev_z2, abs(z6.real - z0.real)
                 + abs(np.exp(1j * (z6.imag - z0.imag)) - 1.0))
check("M4.1 the fermionic deck lift on the 48-site cover: per-mode "
      "phases e^{i 16 k} take EXACTLY the Z6 values e^{i pi (2r+1)/3} "
      "on the three deck classes (max dev %.1e), each cubes to -1 "
      "(max dev %.1e), and as partition-function identities "
      "deck^3 = (-1)^F and deck^6 = 1 at machine precision -- "
      "deck^3 = -1 (v623) closes exactly in the trace"
      % (dev_ph, dev_cube),
      dev_ph < 1e-12 and dev_cube < 1e-12
      and dev_z1 < TOL_MACH and dev_z2 < TOL_MACH,
      "Z-identity devs: deck^3 vs (-1)^F %.2e, deck^6 vs 1 %.2e"
      % (dev_z1, dev_z2))

# M4.2 exact factorization: cover deck^h trace = product of the three
#      base twist sectors with per-class insertion (-1)^h omega^{g~ h}
GTIL = {0: 2, 1: 0, 2: 1}                 # class r -> base twist g~
dev_fac, dev_z6 = 0.0, 0.0
for h in range(6):
    for L in (32, 72):
        lhs = lnZraw(N_MAIN, L, 0, N_BASE * kc * h)
        rhs = 0.0 + 0.0j
        for r in range(3):
            nu = (2 * r + 1) / 6.0
            rhs += lnZraw(N_BASE, L, GTIL[r], 2.0 * np.pi * nu * h)
        dev_fac = max(dev_fac, abs(lhs.real - rhs.real)
                      + abs(np.exp(1j * (lhs.imag - rhs.imag)) - 1.0))
    for r in range(3):
        nu = (2 * r + 1) / 6.0
        dev_z6 = max(dev_z6, abs(np.exp(2j * np.pi * nu * h)
                                 - (-1.0) ** h
                                 * OMEGA ** (GTIL[r] * h)))
check("M4.2 EXACT factorization of the cover trace: "
      "Tr_48[deck^h e^{-LH}] = prod_{g~=0,1,2} Tr_16-base[g~-twist, "
      "insertion ((-1)^h omega^{g~ h})^{Nhat} e^{-LH}] for all h in "
      "Z6 -- on the seam double the Z3 deck insertion IS the Z3 phase "
      "times a fermion-parity flip PER STEP: the Z6 spin structure "
      "demanded by deck^3 = -1, exact", dev_fac < TOL_MACH
      and dev_z6 < 1e-12,
      "max factorization dev = %.3e, Z6 phase identity dev = %.3e"
      % (dev_fac, dev_z6))

# M4.3 parity / Z6-charge projections of the sectors
print("  parity data per g-sector (h = 0), N = 48:")
par_pos, par_even, gap_ok = True, True, True
z6_pos, z6_sum, z6_ground = True, 0.0, True
rmax_h = 0.0
GAP_ODD = {0: 0.5, 1: GAP2, 2: GAP2}
D_ODD = {0: 4.0, 1: 2.0, 2: 2.0}
for g in range(3):
    # h = 0 column: Z^{+-} are state counters, must be nonnegative
    z0, _ = lnZ(N_MAIN, 48, g, 0)
    zF0, sF0 = lnZ(N_MAIN, 48, g, 0, parity=True)
    R0 = sF0 * np.exp(zF0 - z0)
    par_pos &= (1.0 + R0 >= -1e-12) and (1.0 - R0 >= -1e-12)
    # h != 0: the naive ratio exceeds 1 (omega-weighted, NOT a counter)
    for h in (1, 2):
        z, _ = lnZ(N_MAIN, 48, g, h)
        zF, sF = lnZ(N_MAIN, 48, g, h, parity=True)
        rmax_h = max(rmax_h, sF * np.exp(zF - z))
    # the POSITIVE bookkeeping: Z6 charge projection on (Nhat-N/2) mod 6
    zj = np.array([lnZ_lam(N_MAIN, 48, g, np.pi * j / 3.0)
                   for j in range(6)])
    dev_im = max(abs(np.exp(1j * v.imag) - np.sign(np.cos(v.imag)))
                 for v in zj)
    zvals = np.array([np.sign(np.cos(v.imag)) * np.exp(v.real - z0)
                      for v in zj])
    P = np.array([np.mean([np.exp(-1j * np.pi * j * c / 3.0) * zvals[j]
                           for j in range(6)]).real for c in range(6)])
    z6_pos &= (P.min() >= -1e-12) and dev_im < TOL_MACH
    z6_sum = max(z6_sum, abs(P.sum() - 1.0))
    z6_ground &= (P[0] == P.max())
    if g < 2:
        print("    g=%d  Z6 charge classes P_c/Z[g,0], c=0..5: %s"
              % (g, np.array2string(P, precision=5)))
    # ground-state parity and the odd tower.  R = Z^F/Z -> +1 with the
    # measured odd gap: demand R > 0 growing towards 1 (at L = 336 the
    # residual odd weight is the fitted 2 e^{-delta L} ~ 1e-3 for g != 0)
    Rs, ys = [], []
    for L in (240, 336):
        z, _ = lnZ(N_MAIN, L, g, 0)
        zF, sF = lnZ(N_MAIN, L, g, 0, parity=True)
        R = sF * np.exp(zF - z)
        Rs.append(R)
        ys.append((1.0 - R) / (1.0 + R))
    par_even &= (Rs[0] > 0.9 and Rs[1] > 0.99 and Rs[1] > Rs[0])
    gap_fit = np.log(ys[0] / ys[1]) / 96.0 * N_MAIN / (2.0 * np.pi)
    d_odd = ys[0] * np.exp(gap_fit * 2.0 * np.pi / N_MAIN * 240.0)
    rel_g = abs(gap_fit - GAP_ODD[g]) / GAP_ODD[g]
    rel_d = abs(d_odd - D_ODD[g]) / D_ODD[g]
    gap_ok &= (rel_g < TOL_FIT and rel_d < TOL_MULT)
    print("    g=%d  ground parity EVEN, odd tower gap = %.7f vs %.7f "
          "(rel %.1e), multiplicity = %.4f vs %d"
          % (g, gap_fit, GAP_ODD[g], rel_g, d_odd, int(D_ODD[g])))
check("M4.3 parity / Z6-charge bookkeeping per sector: in the h = 0 "
      "column Z^{+-} = (Z +- Z^F)/2 are nonnegative state counters, "
      "every sector ground state is parity-EVEN (charge-0 twisted "
      "vacua), the parity-ODD towers open at gap (1/2, 1/6, 1/6) with "
      "multiplicities (4, 2, 2) for g = (0, 1, 2) at < 1 %%/2 %%; for "
      "h != 0 the naive Z^F/Z ratio EXCEEDS 1 (max %.3f measured: "
      "omega-weighted parity traces, not counters -- honest), and the "
      "POSITIVE bookkeeping of the full Z6 family is the Z6 charge "
      "projection: all six P_c >= 0, sum_c P_c = Z[g,0] (dev %.1e), "
      "ground class c = 0, in every g-sector -- the (-1)^F / Z6 "
      "transformation of the sectors, resolved" % (rmax_h, z6_sum),
      par_pos and par_even and gap_ok and z6_pos and z6_ground
      and z6_sum < TOL_MACH and rmax_h > 1.0)


# ================================================================== M5
print("=" * 72)
print("M5: the typing")
print("=" * 72)

check("M5.1 [C, honest typing] WHAT STANDS on the lattice: the nine "
      "Z[g,h] with exact conjugation degeneracies; the continuum "
      "match |theta[g/3,h/3]/eta|^2 at < 1 % (N = 48); the v628 "
      "Casimir table per g-sector; modular S-covariance MEASURED with "
      "a clean common N^{-4} rate (the N^{-2} lattice artifact is "
      "itself S-covariant and cancels); T realized exactly as the "
      "discrete Dehn twist = the Z6 shift (g,h) -> (g, g+h) x (-1)^F; "
      "the twisted characters (h_sigma = 1/36, parafermionic gap 1/6, "
      "omega charge weights); and the deck^3 = -1 spin structure as "
      "exact Z6 trace arithmetic including the cover factorization.  "
      "STILL OPEN: the chiral PHASES of the eta/theta identification "
      "(only |.|^2 is matched), the full continuum T-phases per "
      "character (the lattice convention is real-positive), the "
      "non-abelian sector assembly / orbifold projection sum with its "
      "discrete-torsion choice, and the continuum OS statement -- "
      "named, not claimed.  GATE.QGEO does not move", True)


# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
c_ok = all(ok for n, ok in CHECKS if n.startswith(("C0", "M1")))
s_ok = all(ok for n, ok in CHECKS if n.startswith("M2"))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: ORB-MODULAR-COHERENT -- the modular data of the Z3")
    print("orbifold of the seam stands on the lattice: nine sectors match")
    print("|theta[g/3,h/3]/eta|^2, S-covariance is MEASURED with a clean")
    print("N^{-4} rate (the N^{-2} artifact is itself S-covariant and")
    print("cancels), T is the exact Z6 Dehn shift, the twisted")
    print("characters carry h_sigma = 1/36 with the parafermionic 1/6 gap,")
    print("and deck^3 = -1 closes exactly as Z6 trace arithmetic.")
elif c_ok and not s_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: ORB-MODULAR-S-OPEN -- sectors and characters stand but")
    print("the S-relation does not converge with a clean rate: honest open.")
elif not c_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: ORB-MODULAR-FAILS -- the reference or sector level")
    print("fails: honest negative.")
else:
    print("SOME CHECKS FAILED")
    print("VERDICT: MIXED")
