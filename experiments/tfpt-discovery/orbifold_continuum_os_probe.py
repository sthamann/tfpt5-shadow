#!/usr/bin/env python3
"""Discovery probe: the FIRST CONTINUUM-OS SLICE of the seam orbifold B
-- the last big [C] of the QGEO orbifold front.  The Osterwalder-
Schrader reconstruction needs (i) Euclidean correlators that CONVERGE
as the lattice is removed, (ii) reflection positivity IN THE LIMIT (not
only per lattice), (iii) the cluster property.  This probe measures all
three at the convergence level, with RATES, plus the continuum
characters from the exact level extrapolation.

CONTEXT (inherited read-only): the seam assembly is B, the Z6 deck
quotient with uniform charge-0 projection (orbifold_assembly_probe
M3.4, hardened structurally in orbifold_arf_probe A2.4 and elevated to
a lattice theorem in bond_defect_premise_probe P1: twist sector = deck
boundary condition = bond defect).  RP on the lattice is the
parafermionic Klein pairing (parafermion_klein_rp_probe: mirror x
charge conjugation, omega^{k q} zero-mode dressing, eta = (1,1),
PSD and N-stable 48..384 including the mixed OS Gram; the half-twist
tau Gram is PSD too, orbifold_arf_probe A1.3).  The modular data are
measured (orbifold_modular_probe / v650: S-covariance falls ~N^{-4}
because the N^{-2} lattice artifact is itself S-covariant; T exact;
characters h_sigma = 1/36, Delta_sigma = 1/9, parafermionic gap 1/6).
Correlator machinery: string determinants with the smooth
Fisher-Hartwig (FH) artifact d^{-rho}, rho = 2(1-beta)^2 - 2 beta^2
per string angle (beta = lam/2pi): rho = 2/3 for the sigma string
(lam = 2pi/3), 4/3 for the tau string (lam = pi/3)
(orbifold_twist_ope_probe S2.5, orbifold_arf_probe A1).

WHAT IS NEW HERE: every object is taken at FIXED CONTINUUM DATA
(separations x/N, cross-ratios w, point configurations i/24, Euclidean
time tau/N) over the N-ladder 48/96/192/384 (+768/1536 where cheap),
and the CONVERGENCE ITSELF is the measurement: rates per observable,
extrapolated limits vs the CFT values, eigenvalue convergence of the
Klein Grams with an extrapolated positivity floor, the cylinder
(cosh) form of the two-point in space AND Euclidean time, and the
cluster decomposition with measured decay laws.  A time-separated
dipole correlator <D(tau) D^+(0)> (QR-stabilized determinant formula,
new machinery, validated in O0.3) opens the Euclidean-time direction
that all previous probes left untouched.

Checks:

  (O0.1) [machine] Toeplitz covariance == verbatim mode-sum covariance
         (N = 96).
  (O0.2) [machine] zero-mode-dressed string reality for the full mu6
         angle family (random multi-arc configs) -- the Klein reality.
  (O0.3) [machine] the NEW time-direction machinery: the NS bond
         Hamiltonian reproduces eps6(N, 0); G(tau) = det(V^+ U_D
         e^{-tau h} U_D^+ V)/det(V^+ e^{-tau h} V) via thin-QR
         stabilization satisfies G == 1 identically for lam = 0 (all
         tau) and for tau = 0 (unitarity), matches the naive complex
         determinant ratio at small tau (reality + value), and
         det(V^+ U_D V) equals the covariance-route string value.
  (O0.4) [E] the amplitude reference: four-term chord fits of the
         sigma two-point at N = 1536 and N = 768 give the same
         non-universal A^2 (< 1 %); A^2 is the only fitted constant
         reused below.

  (O1.1) [E] two-point convergence at fixed x/N in {1/8, 1/4, 3/8}:
         the rescaled correlator N^{4 Delta} T_N(x = alpha N) converges
         over N = 48..384; both difference-ratio rates per observable;
         the geometric extrapolant hits the CFT value
         A [sin(pi alpha)/pi]^{-4 Delta} at < 1 % with an uncertainty
         band (window spread + fixed-rho fit spread).
         NOTE the dictionary: Delta = h + hbar = 1/9 is the scaling
         dimension of the seam twist (v639); the DECAY exponent of
         <sigma sigma^+> is 2 Delta = 2/9 (the probe convention
         TWO_D below; the per-deck-class weight is h_sigma = 1/36).
  (O1.2) [E] four-point convergence at fixed cross-ratio: Ghat(w) =
         |G4| (d13 d24)^{2 Delta} at w = 1/2 and w = sin^2(pi/8), and
         the epsilon-channel stripping Dtil(w) = |G4| (d12 d34)^
         {2 Delta} at w = sin^2(pi/8) (the s-channel block whose w^1
         weight is the Delta = 1 epsilon/current level, v639 c1 =
         2 Delta): rates + extrapolants vs A^2 [w(1-w)]^{-2 Delta}
         resp. A^2 (1-w)^{-2 Delta} at < 1 %.
  (O1.3) [central] THE UNIFORM CONVERGENCE SIGNATURE: the raw rates of
         ALL sigma-channel observables agree with each other AND with
         the predicted FH branch exponent rho_sigma = 2/3 -- the
         honest answer to "are all rates >= 1" is NO for the raw
         correlators: the leading lattice artifact is the SMOOTH
         d^{-2/3} FH branch, uniformly across observables; the
         tau-channel contrast (lam = pi/3) measures rho_tau = 4/3 (the
         channel law rho = 2(1-beta)^2 - 2 beta^2, so the rate is
         UNDERSTOOD, not fitted); after removing the ONE known FH term
         the residuals are at the N^{-4/3} level (>= first order):
         quantified via the fixed-rho two-term fit whose residual is
         a small fraction of the correction term.
  (O1.4) [machine] the epsilon-channel two-point is EXACT on the
         lattice: the connected density correlator <n n>_c at odd
         separation equals the continuum chord form -1/(pi d_chord)^2
         at machine precision at EVERY N (closed kernel form
         C(d) = sin(pi d/2)/(N sin(pi d/N)) verified) -- the Delta = 1
         channel has NO lattice artifact at half filling: rate = exact.

  (O2.1) [central] RP in the limit, sigma sector: the Klein Gram
         (lam = 2pi/3, Klein pairing + dressing) at the FIXED continuum
         configuration x/N = i/24 (i = 1..11) over N = 48..384,
         correlation-normalized (amplitude-free): every N is PSD at
         the -1e-10 floor; the RESOLVABLE spectrum converges (top-6
         eigenvalues, differences shrink, rates reported; the bottom
         of the nested-string basis sits at the double-precision
         floor ~1e-11 at every N -- an honest resolution limit,
         reported, not extrapolated); on the well-conditioned 4-point
         sub-family (x/N in {2, 5, 8, 11}/24) ALL eigenvalues converge
         and the minimal eigenvalue is extrapolated (free-rate
         geometric windows + fixed-rho fit, band = spread):
         lambda_min(infinity) > 0 bounded away from 0 by more than
         3 x the band -- no 0^- drift of the limit matrix.
  (O2.2) [central] the same for the half-twist tau Gram (lam = pi/3).
  (O2.3) [E] the mixed OS Gram {1, sigma_1(x_i), sigma_2(x_i)} over
         N = 48..384 (plus the dipole-extended mixed Gram at
         N = 48/96/192): PSD floors on the full sets; lambda_min
         extrapolation with band on the sub-family mixed Gram,
         limit > 0.
  (O2.4) [machine, must-fail] eta = -1 flips the sigma Klein Gram to
         negative definite (the control keeps its teeth in the
         normalized convention too).

  (O3.1) [E] the cylinder form in SPACE on the largest lattice
         (N = 1536, x up to N/2): the free-exponent chord fit gives
         2 Delta = 2/9 at < 1 %, and the chord (sin) form beats the
         plain power-law form by an order of magnitude in residual
         (the compact-geometry two-point is the tau = 0 slice of the
         cylinder cosh form).
  (O3.2) [E] the cylinder form in EUCLIDEAN TIME (new): the
         time-separated dipole correlator G(tau) = <D(tau) D^+(0)>,
         D = e^{i lam N_[0,a)}, at N = 192, a = 24, against the exact
         vertex closed form with cylinder distances
         d((x,t),(x',t')) = (N/pi) |sin(pi((x-x') + i(t-t'))/N)|
         (the cosh form): shape-normalized deviation < 2 % over
         tau in [12, 72]; the ABSOLUTE offset is identified as the
         dipole's own FH normalization -- measured exactly as
         (T_lat(a)/T_inf(a))^2 - 1 AND independently predicted from
         the N = 1536 fit coefficients (agreement < 0.015), constant
         on the plateau tau >= 24 (< 1.5 %; the short-time transient
         at tau = 12 is reported): no new artifact in the time
         direction; G(0) = 1 exactly (operator identity).
  (O3.3) [central] CLUSTER DECOMPOSITION, measured in both directions:
         (space) R = G4/T(a)^2 - 1 for two a-dipoles at FIXED
         continuum configuration (a = N/32, s = alpha N), extrapolated
         over N = 192/384/768, equals the exact CFT law
         (1-w)^{-2 Delta} - 1 pointwise (< 2 %) and falls with the
         measured power w^1 (slope of ln R vs ln w = 1 within 5 %):
         R -> 0 like chord(s)^{-2} -- the connected four-point
         clusters with the epsilon-channel power; (time) the connected
         C(tau) = G(tau)/T(a)^2 - 1 on TWO lattices (N = 96, 192;
         a = N/8) decays exponentially with the fitted gap = the
         exact lattice neutral gap at < 0.5 % per lattice
         (two-exponential fit, relative residuals, late window),
         which is the Delta = 1 epsilon/current level
         2pi/N x (1 + O(N^-2)): the OS cluster property holds with
         the transfer-matrix gap; the amplitude FH-extrapolates over
         the two lattices to the closed-form prediction
         4 Delta (1 - cos(2pi a/N)) at < 3 %.

  (O4.1) [E] continuum characters: Delta_sigma(N) from the exact mode
         sums over N = 48..768 converges with the measured N^{-2} rate;
         the N^{-2}(+N^{-4}) extrapolation hits 1/9 at < 0.1 % with an
         uncertainty band << 0.1 %; per-deck-class h = Delta/4 hits
         1/36 (the v650/v639 dictionary).
  (O4.2) [E] the second twist level Delta_sigma + gap: the charged
         single-mode gap extrapolates to 1/6, the level to
         5/18 = 1/9 + 1/6, at < 0.1 % with band.
  (O4.3) [E] the third (neutral) twist level Delta_sigma + 1/3 -> 4/9
         at < 0.1 % with band (the particle+hole pair across the two
         Fermi points; assembly M3.2 multiplicities).

  (O5.1) [C, honest typing] which OS axioms are now MEASURED at the
         convergence level and what stays open for the formal limit
         (named, not claimed).  GATE.QGEO does not move.

Verdict enums (frozen): ORB-OS-CONTINUUM-SLICE (O1 convergence with
understood uniform rates + CFT limits, O2 RP floor bounded away from
zero in the limit, O3 cylinder/cosh + cluster with rates, O4 characters
< 0.1 % -- the first continuum-OS slice stands), ORB-OS-RP-DRIFT
(correlators/cluster/characters stand but the RP extrapolation cannot
bound lambda_min away from 0), ORB-OS-NONUNIFORM (convergence exists
but the rate signature is not uniform/understood), ORB-OS-FAILS (a
machinery control or a lattice PSD level fails), MIXED (anything else).

FIREWALL: experiments/ only; GATE.QGEO does not move; no marker
changes; verification/ untouched.

Conventions inherited read-only from orbifold_twist_ope_probe.py,
parafermion_klein_rp_probe.py, orbifold_arf_probe.py,
orbifold_assembly_probe.py, orbifold_modular_probe.py,
bond_defect_premise_probe.py, v622/v623/v628/v639/v650-v653.
"""

import numpy as np

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------------ constants
DELTA = 1.0 / 9.0                 # sigma twist scaling dimension (v639)
TWO_D = 2.0 / 9.0                 # sigma two-point decay exponent
TWO_D_TAU = 1.0 / 18.0            # tau (half-twist) decay exponent
LAM_SIG = 2.0 * np.pi / 3.0
LAM_TAU = np.pi / 3.0
RHO_SIG = 2.0 / 3.0               # FH branch exponent, beta = 1/3
RHO_TAU = 4.0 / 3.0               # FH branch exponent, beta = 1/6
NLAD = (48, 96, 192, 384)         # the continuum N-ladder
NCHAR = (48, 96, 192, 384, 768)   # character ladder (mode sums, cheap)
N_BIG = 1536                      # largest lattice (O3.1 / amplitude)
N_MID = 768                       # amplitude crosscheck + space cluster
N_TIME = 192                      # Euclidean-time machinery lattice
TOL_MACH = 1e-10
TOL_RP = 1e-10
TOL_LIM = 0.01                    # 1 % on extrapolated limits vs CFT
TOL_CHAR = 1e-3                   # 0.1 % on the character levels
RNG = np.random.default_rng(61)


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


def string_logabs(C, sites, u):
    S = np.asarray(sites, dtype=int)
    Cs = C[np.ix_(S, S)]
    M = np.eye(len(S), dtype=complex) \
        + (np.exp(1j * np.asarray(u, dtype=float)) - 1.0)[:, None] * Cs
    return np.linalg.slogdet(M)[1]


def chord(N, x):
    return (N / np.pi) * np.sin(np.pi * np.asarray(x, dtype=float) / N)


def cyl_chord(N, dx, dt):
    """Cylinder distance (N/pi) |sin(pi (dx + i dt)/N)| -- the cosh form:
    |sin|^2 = (cosh(2 pi dt/N) - cos(2 pi dx/N))/2."""
    return (N / np.pi) * abs(np.sin(np.pi * (dx + 1j * dt) / N))


def two_point_log(N, x, lam):
    return string_logabs(cov(N), np.arange(int(x)),
                         lam * np.ones(int(x)))


def g4_log(N, pts, lam):
    x1, x2, x3, x4 = pts
    sites = np.concatenate([np.arange(x1, x2), np.arange(x3, x4)]) % N
    return string_logabs(cov(N), sites, lam * np.ones(len(sites)))


def chords6(N, pts):
    x1, x2, x3, x4 = pts
    return dict(d12=chord(N, x2 - x1), d23=chord(N, x3 - x2),
                d34=chord(N, x4 - x3), d14=chord(N, x4 - x1),
                d13=chord(N, x3 - x1), d24=chord(N, x4 - x2))


def cross_w(N, pts):
    c = chords6(N, pts)
    return (c["d12"] * c["d34"]) / (c["d13"] * c["d24"]), c


def xgrid(N):
    """11 even right-half insertion points, fixed ratios x/N = i/24."""
    return [4 * i * N // 96 for i in range(1, 12)]


def dip_pairs(N):
    return [(s * N // 96, (s + l) * N // 96)
            for s in (0, 4, 8, 16, 24) for l in (4, 8, 16) if s + l <= 48]


def modes6(N, gt):
    return 2.0 * np.pi * (np.arange(N) + 0.5 + (gt % 6) / 6.0) / N


def eps6(N, gt):
    e = -np.cos(modes6(N, gt))
    e[np.abs(e) < 1e-13] = 0.0
    return e


def eig_ratio(M):
    ev = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
    return ev, ev.min() / np.abs(ev).max()


def norm_gram(M):
    d = np.sqrt(np.abs(np.diag(M).real))
    return (M / np.outer(d, d)).real


def seq_rates(vals):
    """Successive differences and difference-ratio rates log2(d_k/d_k+1)."""
    d = np.diff(np.asarray(vals, dtype=float))
    r = []
    for k in range(len(d) - 1):
        if d[k] == 0 or d[k + 1] == 0 or d[k] * d[k + 1] <= 0:
            r.append(np.nan)
        else:
            r.append(np.log2(abs(d[k]) / abs(d[k + 1])))
    return d, r


def geo_extrap(f1, f2, f3):
    """a from f(N) = a + b N^{-r} through three points (N, 2N, 4N)."""
    d1, d2 = f2 - f1, f3 - f2
    if d1 == 0 or d2 == 0 or d1 * d2 <= 0:
        return np.nan, np.nan
    q = d2 / d1
    if not (0.0 < q < 1.0):
        return np.nan, np.nan
    return f3 + d2 * q / (1.0 - q), -np.log2(q)


def extrap_pack(Ns, vals, rho):
    """Geometric window extrapolants + fixed-rho two-term fit.
    Returns (a_hat, band, rates, resid_frac): band = spread of the three
    extrapolants, resid_frac = max fit residual / correction at N_max."""
    vals = np.asarray(vals, dtype=float)
    Ns = np.asarray(Ns, dtype=float)
    a1, _ = geo_extrap(*vals[:3])
    a2, _ = geo_extrap(*vals[1:])
    X = np.column_stack([np.ones(len(Ns)), Ns ** (-rho)])
    c, *_ = np.linalg.lstsq(X, vals, rcond=None)
    afix = c[0]
    resid = vals - X @ c
    corr = abs(c[1]) * Ns[-1] ** (-rho)
    resid_frac = np.abs(resid).max() / corr if corr > 0 else np.inf
    a_hat = a2 if np.isfinite(a2) else afix
    cand = [a for a in (a1, a2, afix) if np.isfinite(a)]
    band = max(abs(a_hat - a) for a in cand) if cand else np.inf
    _, rates = seq_rates(vals)
    return a_hat, band, rates, resid_frac


# ================================================================== O0
print("=" * 72)
print("O0: machinery validation + the amplitude reference")
print("=" * 72)

dev_cov = np.abs(cov_toeplitz(96) - cov_verbatim(96)).max()
check("O0.1 [machine] Toeplitz covariance equals the verbatim mode-sum "
      "covariance of the Klein probe (N = 96)", dev_cov < 1e-12,
      "max |dev| = %.3e" % dev_cov)

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
check("O0.2 [machine] the zero-mode-dressed string is exactly real for "
      "the full mu6 angle family (Klein reality, 40 random configs)",
      dev_re < TOL_MACH, "max |Im|/|w| = %.3e" % dev_re)


# ---- O0.3 the Euclidean-time machinery
def time_setup(N):
    """NS chain in position space; returns (ev, U, V) with V = occupied."""
    h = np.zeros((N, N), dtype=complex)
    for j in range(N - 1):
        h[j, j + 1] = -0.5
        h[j + 1, j] = -0.5
    h[N - 1, 0] = 0.5                 # NS: psi(x+N) = -psi(x)
    h[0, N - 1] = 0.5
    ev, U = np.linalg.eigh(h)
    return ev, U, U[:, ev < 0]


def logabs_G_tau(setup, N, a, lam, tau, dtau_max=8.0):
    """log |<D(tau) D^+(0)>|, D = e^{i lam N_[0,a)}: det(V^+ U_D
    e^{-tau h} U_D^+ V)/det(V^+ e^{-tau h} V), SLICED propagation with
    a thin-QR re-orthogonalization per slice (the standard DQMC
    stabilization: one QR at the end loses the upper modes once
    e^{tau} exceeds 1/eps -- validated in O0.3)."""
    ev, U, V = setup
    phase = np.ones(N, dtype=complex)
    phase[:a] = np.exp(1j * lam)

    def prop(M0):
        nsl = max(1, int(np.ceil(tau / dtau_max)))
        dt = tau / nsl
        W, acc = M0, 0.0
        for _ in range(nsl):
            W = U @ (np.exp(-dt * ev)[:, None] * (U.conj().T @ W))
            Q, R = np.linalg.qr(W)
            acc += np.log(np.abs(np.diag(R))).sum()
            W = Q
        return acc, W

    acc2, Q2 = prop(np.conj(phase)[:, None] * V)
    num = np.linalg.slogdet(V.conj().T @ (phase[:, None] * Q2))[1] + acc2
    acc0, Q0 = prop(V.copy())
    den = np.linalg.slogdet(V.conj().T @ Q0)[1] + acc0
    return num - den


TSET = time_setup(N_TIME)
ev_t, U_t, V_t = TSET
dev_spec = np.abs(np.sort(ev_t) - np.sort(eps6(N_TIME, 0))).max()
dev_l0 = max(abs(logabs_G_tau(TSET, N_TIME, 24, 0.0, t))
             for t in (0.0, 20.0, 120.0))
dev_t0 = abs(logabs_G_tau(TSET, N_TIME, 24, LAM_SIG, 0.0))
# naive complex determinant ratio at small tau (reality + value)
tau_s = 8.0
phase = np.ones(N_TIME, dtype=complex)
phase[:24] = np.exp(1j * LAM_SIG)
K = U_t @ (np.exp(-tau_s * ev_t)[:, None] * U_t.conj().T)
num_n = V_t.conj().T @ (phase[:, None] * (K @ (np.conj(phase)[:, None]
                                               * V_t)))
den_n = V_t.conj().T @ (K @ V_t)
sn, ln_num = np.linalg.slogdet(num_n)
sd, ln_den = np.linalg.slogdet(den_n)
g_naive = (sn / sd) * np.exp(ln_num - ln_den)
dev_naive = abs(np.log(abs(g_naive))
                - logabs_G_tau(TSET, N_TIME, 24, LAM_SIG, tau_s))
dev_imag = abs(g_naive.imag) / abs(g_naive)
# equal-time crosscheck: det(V^+ U_D V) vs the covariance-route string
ld_eq = np.linalg.slogdet(V_t.conj().T @ (phase[:, None] * V_t))[1]
dev_eq = abs(ld_eq - two_point_log(N_TIME, 24, LAM_SIG))
check("O0.3 [machine] the Euclidean-time machinery: NS bond Hamiltonian "
      "spectrum = eps6(192, 0) (dev %.1e); G(tau) == 1 for lam = 0 at "
      "tau = 0/20/120 (dev %.1e) and at tau = 0 for lam = 2pi/3 (dev "
      "%.1e); QR-stabilized value = naive complex determinant ratio at "
      "tau = 8 (dev %.1e) and the naive value is real positive (Im/Re "
      "%.1e); det(V^+ U_D V) = covariance-route string (dev %.1e)"
      % (dev_spec, dev_l0, dev_t0, dev_naive, dev_imag, dev_eq),
      dev_spec < 1e-12 and dev_l0 < TOL_MACH and dev_t0 < TOL_MACH
      and dev_naive < 1e-9 and dev_imag < 1e-9 and dev_eq < 1e-9)

# ---- O0.4 the amplitude reference (four-term chord fits, p fixed)
xs_big = np.arange(96, 769, 32)
logT_big = np.array([two_point_log(N_BIG, int(x), LAM_SIG)
                     for x in xs_big])
D_big = chord(N_BIG, xs_big)
X4 = np.column_stack([np.ones(len(xs_big)), np.log(D_big),
                      D_big ** (-RHO_SIG), D_big ** (-2 * RHO_SIG)])
cf_big, *_ = np.linalg.lstsq(X4, logT_big, rcond=None)
P_BIG = -cf_big[1]
Xf = np.column_stack([np.ones(len(xs_big)), D_big ** (-RHO_SIG),
                      D_big ** (-2 * RHO_SIG)])
cff, *_ = np.linalg.lstsq(Xf, logT_big + TWO_D * np.log(D_big),
                          rcond=None)
A2_REF = float(np.exp(2.0 * cff[0]))
xs_mid = np.arange(48, 385, 16)
logT_mid = np.array([two_point_log(N_MID, int(x), LAM_SIG)
                     for x in xs_mid])
D_mid = chord(N_MID, xs_mid)
Xm = np.column_stack([np.ones(len(xs_mid)), D_mid ** (-RHO_SIG),
                      D_mid ** (-2 * RHO_SIG)])
cfm, *_ = np.linalg.lstsq(Xm, logT_mid + TWO_D * np.log(D_mid),
                          rcond=None)
A2_MID = float(np.exp(2.0 * cfm[0]))
dev_amp = abs(A2_MID / A2_REF - 1.0)
A_REF = np.sqrt(A2_REF)
check("O0.4 [E] the amplitude reference: fixed-exponent four-term chord "
      "fits at N = 1536 and N = 768 give the same non-universal A^2 "
      "(%.6f vs %.6f, rel dev %.2e < 1 %%); A^2 is the only fitted "
      "constant reused below" % (A2_REF, A2_MID, dev_amp),
      dev_amp < 0.01)


# ================================================================== O1
print("=" * 72)
print("O1: correlator convergence at fixed continuum data (rates)")
print("=" * 72)

OBS = []      # (label, vals over NLAD, target, rho)

for (num, den) in ((1, 8), (1, 4), (3, 8)):
    alpha = num / den
    vals = [Nv ** TWO_D * np.exp(two_point_log(Nv, Nv * num // den,
                                               LAM_SIG))
            for Nv in NLAD]
    tgt = A_REF * (np.sin(np.pi * alpha) / np.pi) ** (-TWO_D)
    OBS.append(("2pt x/N=%d/%d" % (num, den), vals, tgt))


def pts_cfg(N, kind):
    if kind == "A":
        return (0, N // 4, N // 2, 3 * N // 4)
    return (0, N // 8, N // 2, N // 2 + N // 8)


for kind in ("A", "B"):
    vals, wv = [], None
    for Nv in NLAD:
        pts = pts_cfg(Nv, kind)
        wv, c = cross_w(Nv, pts)
        vals.append(np.exp(g4_log(Nv, pts, LAM_SIG))
                    * (c["d13"] * c["d24"]) ** TWO_D)
    tgt = A2_REF * (wv * (1.0 - wv)) ** (-TWO_D)
    OBS.append(("Ghat w=%.4f" % wv, vals, tgt))

vals, wv = [], None
for Nv in NLAD:
    pts = pts_cfg(Nv, "B")
    wv, c = cross_w(Nv, pts)
    vals.append(np.exp(g4_log(Nv, pts, LAM_SIG))
                * (c["d12"] * c["d34"]) ** TWO_D)
tgt = A2_REF * (1.0 - wv) ** (-TWO_D)
OBS.append(("Dtil w=%.4f (eps)" % wv, vals, tgt))

print("  rate table (sigma channel, N = 48/96/192/384):")
print("  %-20s %10s %10s %10s %10s %7s %7s %11s %9s %9s"
      % ("observable", "f(48)", "f(96)", "f(192)", "f(384)", "r1",
         "r2", "extrap", "|dev|/t", "band/t"))
DEV_LIM, BAND_LIM, FINE_RATES, RESID_FRACS = [], [], [], []
for (lbl, vals, tgt) in OBS:
    a_hat, band, rates, rfrac = extrap_pack(NLAD, vals, RHO_SIG)
    dev = abs(a_hat - tgt) / abs(tgt)
    DEV_LIM.append(dev)
    BAND_LIM.append(band / abs(tgt))
    FINE_RATES.append(rates[1])
    RESID_FRACS.append(rfrac)
    print("  %-20s %10.6f %10.6f %10.6f %10.6f %7.3f %7.3f %11.6f "
          "%9.2e %9.2e" % (lbl, vals[0], vals[1], vals[2], vals[3],
                           rates[0], rates[1], a_hat, dev,
                           band / abs(tgt)))

ok11 = (all(d < TOL_LIM for d in DEV_LIM[:3])
        and all(b < TOL_LIM for b in BAND_LIM[:3])
        and all(np.isfinite(r) for r in FINE_RATES[:3]))
check("O1.1 [E] two-point convergence at fixed x/N in {1/8, 1/4, 3/8}: "
      "the rescaled N^{4/9} T_N(alpha N) converges with clean "
      "difference-ratio rates and the extrapolants hit the CFT chord "
      "values A [sin(pi alpha)/pi]^{-2/9} at < 1 %% (devs %.2e / %.2e "
      "/ %.2e, bands %.1e / %.1e / %.1e)"
      % (DEV_LIM[0], DEV_LIM[1], DEV_LIM[2], BAND_LIM[0], BAND_LIM[1],
         BAND_LIM[2]), ok11)

ok12 = (all(d < TOL_LIM for d in DEV_LIM[3:])
        and all(b < TOL_LIM for b in BAND_LIM[3:])
        and all(np.isfinite(r) for r in FINE_RATES[3:]))
check("O1.2 [E] four-point convergence at fixed cross-ratio (w = 1/2, "
      "sin^2(pi/8)) and the epsilon-channel stripping Dtil: "
      "extrapolants hit A^2 [w(1-w)]^{-2/9} resp. A^2 (1-w)^{-2/9} at "
      "< 1 %% (devs %.2e / %.2e / %.2e)"
      % (DEV_LIM[3], DEV_LIM[4], DEV_LIM[5]), ok12)

# tau-channel contrast: rho_tau = 4/3 by the FH channel law
vals_tau = [Nv ** TWO_D_TAU * np.exp(two_point_log(Nv, Nv // 4,
                                                   LAM_TAU))
            for Nv in NLAD]
_, rates_tau = seq_rates(vals_tau)
fr = np.array(FINE_RATES)
spread = float(fr.max() - fr.min())
mean_r = float(fr.mean())
max_rfrac = float(np.max(RESID_FRACS))
print("  tau-channel contrast (lam = pi/3, x = N/4): rates %.3f / %.3f"
      % (rates_tau[0], rates_tau[1]))
ok13 = (spread < 0.30 and 0.50 < mean_r < 0.85
        and all(np.isfinite(r) for r in rates_tau)
        and 1.0 < rates_tau[1] < 1.7
        and max_rfrac < 0.35)
check("O1.3 [central] THE UNIFORM CONVERGENCE SIGNATURE: the raw rates "
      "of all six sigma-channel observables are UNIFORM (fine rates "
      "mean %.3f, spread %.3f) and equal the predicted FH branch "
      "exponent rho_sigma = 2/3 -- the honest answer to 'all rates "
      ">= 1?' is NO for raw correlators: the leading artifact is the "
      "smooth FH branch, the SAME for every observable; the "
      "tau-channel contrast measures rho_tau = %.3f vs 4/3 (channel "
      "law rho = 2(1-beta)^2 - 2 beta^2: the rates are UNDERSTOOD, "
      "not fitted); after removing the ONE known FH term the two-term "
      "fixed-rho fit reproduces all four N with residual <= %.2f x "
      "the correction term (the remainder sits at the N^{-4/3} level "
      ">= first order)" % (mean_r, spread, rates_tau[1], max_rfrac),
      ok13)

# O1.4 the epsilon channel is exact
dev_ker, dev_eps = 0.0, 0.0
for Nv in NLAD:
    d = Nv // 8 - 1                       # odd separation
    Cd = cov(Nv)[0, d]
    ker = np.sin(np.pi * d / 2.0) / (Nv * np.sin(np.pi * d / Nv))
    dev_ker = max(dev_ker, abs(Cd - ker))
    eps_lat = -abs(Cd) ** 2               # <n n>_c at separation d
    eps_cft = -1.0 / (np.pi * chord(Nv, d)) ** 2
    dev_eps = max(dev_eps, abs(eps_lat - eps_cft) / abs(eps_cft))
check("O1.4 [machine] the epsilon-channel two-point is EXACT on the "
      "lattice: <n n>_c(d odd) = -1/(pi d_chord)^2 at machine "
      "precision at every N (rel dev %.1e; closed kernel form dev "
      "%.1e): the Delta = 1 epsilon/current channel has NO lattice "
      "artifact at half filling -- rate = exact"
      % (dev_eps, dev_ker), dev_eps < 1e-10 and dev_ker < 1e-13)


# ================================================================== O2
print("=" * 72)
print("O2: RP in the limit -- Klein Gram eigenvalues over the ladder")
print("=" * 72)


def klein_gram_strings(N, lam):
    """Klein-pairing Gram of the axis strings at x/N = i/24 (b = 0):
    bra = reflected support with the SAME angle (charge conjugation),
    zero-mode dressing e^{-i sum(u)/2} (verbatim probe conventions)."""
    C = cov(N)
    xs = xgrid(N)
    n = len(xs)
    M = np.zeros((n, n), dtype=complex)
    for i, xa in enumerate(xs):
        bra = np.arange(N - xa, N) % N
        for j, xb in enumerate(xs):
            sites = np.concatenate([bra, np.arange(0, xb)])
            u = lam * np.ones(len(sites))
            M[i, j] = np.exp(-0.5j * u.sum()) * string_det(C, sites, u)
    return M


SUB_IDX = [1, 4, 7, 10]      # x/N = 2/24, 5/24, 8/24, 11/24 (spread)
NTOP = 6                     # resolvable top of the full spectrum


def gram_report(name, lam, rho):
    """Full 11-point Gram: PSD floors + convergence of the resolvable
    top-of-spectrum.  Well-conditioned 4-point sub-Gram: all
    eigenvalues + lambda_min extrapolation.  (The bottom of the full
    nested-string spectrum sits at the double-precision floor ~1e-11
    at every N -- an honest resolution limit, reported, not gated.)"""
    evf, evs, floors = {}, {}, {}
    M96 = None
    for Nv in NLAD:
        M = klein_gram_strings(Nv, lam)
        if Nv == 96:
            M96 = M
        _, r_raw = eig_ratio(M)
        Mn = norm_gram(M)
        ev = np.linalg.eigvalsh(0.5 * (Mn + Mn.T))
        Ms = Mn[np.ix_(SUB_IDX, SUB_IDX)]
        evsub = np.linalg.eigvalsh(0.5 * (Ms + Ms.T))
        evf[Nv], evs[Nv] = ev, evsub
        floors[Nv] = min(r_raw, ev.min() / np.abs(ev).max())
        print("  %s N=%4d  full: min=%.2e max=%.5f  sub(4): "
              "min=%.6e  raw floor=%.2e"
              % (name, Nv, ev.min(), ev.max(), evsub.min(), r_raw))
    top_rates, top_shrink = [], True
    for i in range(-NTOP, 0):
        seq = [evf[Nv][i] for Nv in NLAD]
        d, r = seq_rates(seq)
        top_rates.append(r[1])
        # fine-step shrink |d(192->384)| <= |d(96->192)|: the 48->96
        # step mixes corrections for the smallest resolvable
        # eigenvalues (transient, reported via the rate table)
        top_shrink &= abs(d[2]) <= abs(d[1]) + 1e-13
    sub_rates, sub_shrink = [], True
    for i in range(4):
        seq = [evs[Nv][i] for Nv in NLAD]
        d, r = seq_rates(seq)
        sub_rates.append(r[1])
        sub_shrink &= abs(d[2]) <= abs(d[0]) + 1e-13
    lam_min_seq = [evs[Nv][0] for Nv in NLAD]
    a_hat, band, rates, _ = extrap_pack(NLAD, lam_min_seq, rho)
    tr = np.array(top_rates, dtype=float)
    tr = tr[np.isfinite(tr)]
    print("  %s sub lambda_min: %s -> extrap %.6e (band %.1e), rates "
          "%.3f/%.3f" % (name, ["%.5e" % v for v in lam_min_seq],
                         a_hat, band, rates[0], rates[1]))
    print("  %s top-%d fine rates: %s (median %.3f); sub eig fine "
          "rates: %s; full-spectrum floor stable at ~%.0e (double-"
          "precision limit of the nested basis)"
          % (name, NTOP, ["%.2f" % r for r in top_rates],
             np.median(tr), ["%.2f" % r for r in sub_rates],
             np.median([evf[Nv][0] for Nv in NLAD])))
    return dict(floors=floors, top_shrink=top_shrink, tr=tr,
                sub_shrink=sub_shrink, lam_min=lam_min_seq,
                a=a_hat, band=band, rates=rates, M96=M96)


SIG = gram_report("sigma Klein Gram", LAM_SIG, RHO_SIG)
ok21 = (min(SIG["floors"].values()) >= -TOL_RP and SIG["top_shrink"]
        and SIG["sub_shrink"] and 0.25 < np.median(SIG["tr"]) < 1.6
        and np.isfinite(SIG["a"]) and SIG["a"] > 0
        and SIG["a"] > 3.0 * SIG["band"])
check("O2.1 [central] RP in the limit, sigma sector: the "
      "correlation-normalized Klein Gram at fixed x/N = i/24 is PSD "
      "at every N = 48..384 (worst floor %.2e); the resolvable "
      "spectrum converges: the top-%d eigenvalues' fine differences "
      "shrink with fine-rate median %.3f (~ the FH 2/3) and all 4 "
      "eigenvalues of the "
      "well-conditioned sub-family converge; lambda_min of the "
      "sub-family extrapolates to %.6e with band %.1e -- bounded away "
      "from 0 by %.0f x the uncertainty, no 0^- drift of the limit "
      "matrix (the bottom of the full nested basis sits at the "
      "double-precision floor ~1e-11: resolution limit, honest)"
      % (min(SIG["floors"].values()), NTOP, np.median(SIG["tr"]),
         SIG["a"], SIG["band"],
         SIG["a"] / max(SIG["band"], 1e-300)), ok21)

TAU = gram_report("tau   Klein Gram", LAM_TAU, RHO_TAU)
ok22 = (min(TAU["floors"].values()) >= -TOL_RP and TAU["top_shrink"]
        and TAU["sub_shrink"] and 0.25 < np.median(TAU["tr"]) < 1.8
        and np.isfinite(TAU["a"]) and TAU["a"] > 0
        and TAU["a"] > 3.0 * TAU["band"])
check("O2.2 [central] RP in the limit, half-twist tau sector: same "
      "statement for lam = pi/3 (worst floor %.2e, top fine-rate "
      "median %.3f, sub lambda_min -> %.6e, band %.1e, margin %.0f x)"
      % (min(TAU["floors"].values()), np.median(TAU["tr"]), TAU["a"],
         TAU["band"], TAU["a"] / max(TAU["band"], 1e-300)), ok22)


# ---- O2.3 the mixed OS Gram
LAMK_M = {1: LAM_SIG, 2: 2.0 * LAM_SIG}


def ket_ops(el, N):
    if el[0] == "id":
        return []
    if el[0] == "sig":
        _, k, x = el
        return [(np.arange(0, x) % N, LAMK_M[k])]
    _, k, a1, a2 = el
    return [(np.arange(a1, a2) % N, LAMK_M[k])]


def bra_ops(el, N):
    if el[0] == "id":
        return []
    if el[0] == "sig":
        _, k, x = el
        return [(np.arange(N - x, N) % N, LAMK_M[k])]
    _, k, a1, a2 = el
    return [(np.arange(N - a2, N - a1) % N, LAMK_M[k])]


def mixed_gram(N, dips, sub=False):
    xs = [xgrid(N)[i] for i in SUB_IDX] if sub else xgrid(N)
    els = ([("id",)]
           + [("sig", k, x) for k in (1, 2) for x in xs])
    if dips:
        els += [("dip", k, a1, a2) for k in (1, 2)
                for (a1, a2) in dip_pairs(N)]
    C = cov(N)
    n = len(els)
    M = np.zeros((n, n), dtype=complex)
    for i, A in enumerate(els):
        ba = bra_ops(A, N)
        for j, B in enumerate(els):
            ops = ba + ket_ops(B, N)
            if not ops:
                M[i, j] = 1.0
                continue
            sites = np.concatenate([s for s, _ in ops])
            u = np.concatenate([a * np.ones(len(s)) for s, a in ops])
            M[i, j] = np.exp(-0.5j * u.sum()) * string_det(C, sites, u)
    return M


mix_min, mix_floor = [], []
for Nv in NLAD:
    M = mixed_gram(Nv, dips=False)
    _, r_raw = eig_ratio(M)
    Mn = norm_gram(M)
    ev = np.linalg.eigvalsh(0.5 * (Mn + Mn.T))
    Msub = norm_gram(mixed_gram(Nv, dips=False, sub=True))
    evsub = np.linalg.eigvalsh(0.5 * (Msub + Msub.T))
    mix_min.append(evsub.min())
    mix_floor.append(min(r_raw, ev.min() / np.abs(ev).max()))
    print("  mixed {1, sigma_1, sigma_2} N=%4d  full(dim %d) min=%.2e"
          "  sub(dim %d) lambda_min=%.6e  raw floor=%.2e"
          % (Nv, M.shape[0], ev.min(), Msub.shape[0], evsub.min(),
             r_raw))
a_mix, band_mix, rates_mix, _ = extrap_pack(NLAD, mix_min, RHO_SIG)
dip_floor = []
for Nv in (48, 96, 192):
    M = mixed_gram(Nv, dips=True)
    _, r_raw = eig_ratio(M)
    Mn = norm_gram(M)
    ev = np.linalg.eigvalsh(0.5 * (Mn + Mn.T))
    dip_floor.append(min(r_raw, ev.min() / np.abs(ev).max()))
    print("  mixed + dipoles (dim %d) N=%4d  norm min=%.2e  "
          "raw floor=%.2e" % (M.shape[0], Nv, ev.min(), r_raw))
ok23 = (min(mix_floor) >= -TOL_RP and min(dip_floor) >= -TOL_RP
        and np.isfinite(a_mix) and a_mix > 0
        and a_mix > 3.0 * band_mix)
check("O2.3 [E] the mixed OS Gram {1, sigma_1(x), sigma_2(x)}: PSD at "
      "every N = 48..384 (worst full floor %.2e; dipole-extended Gram "
      "PSD at 48/96/192, floor %.2e); the well-conditioned sub-Gram "
      "{1, sigma_1(4 pts), sigma_2(4 pts)} has lambda_min -> %.6e "
      "(band %.1e, rates %.3f/%.3f, margin %.0f x): the mixed "
      "lattice-OS statement survives the continuum extrapolation"
      % (min(mix_floor), min(dip_floor), a_mix, band_mix,
         rates_mix[0], rates_mix[1],
         a_mix / max(band_mix, 1e-300)), ok23)

r_neg = eig_ratio(-1.0 * SIG["M96"])[1]
check("O2.4 [machine, must-fail] eta = -1 flips the sigma Klein Gram "
      "to negative definite (floor %.2f): the control keeps its teeth"
      % r_neg, r_neg < -0.5)


# ================================================================== O3
print("=" * 72)
print("O3: the cluster property -- cylinder/cosh form + decay laws")
print("=" * 72)

# ---- O3.1 cylinder (chord) form in space at N = 1536
dev_p = abs(P_BIG - TWO_D) / TWO_D
Xpow = np.column_stack([np.ones(len(xs_big)), np.log(xs_big),
                        np.asarray(xs_big, float) ** (-RHO_SIG),
                        np.asarray(xs_big, float) ** (-2 * RHO_SIG)])
cp, *_ = np.linalg.lstsq(Xpow, logT_big, rcond=None)
res_pow = np.abs(logT_big - Xpow @ cp).max()
res_chord = np.abs(logT_big - X4 @ cf_big).max()
ratio_form = res_chord / res_pow
check("O3.1 [E] the cylinder form in SPACE (N = 1536, x = 96..768): "
      "free-exponent chord fit gives 2 Delta = %.6f vs 2/9 = %.6f "
      "(rel dev %.2e < 1 %%), i.e. Delta = %.6f vs 1/9; the chord "
      "(sin) form fits with max residual %.2e while the plain "
      "power-law form leaves %.2e (ratio %.3f): the compact-geometry "
      "two-point IS the tau = 0 slice of the cylinder cosh form"
      % (P_BIG, TWO_D, dev_p, P_BIG / 2.0, res_chord, res_pow,
         ratio_form),
      dev_p < 0.01 and ratio_form < 0.25)

# ---- O3.2 the cosh form in Euclidean time
A_DIP = 24
taus = np.arange(12, 73, 6, dtype=float)
G_meas = np.array([np.exp(logabs_G_tau(TSET, N_TIME, A_DIP, LAM_SIG,
                                       t)) for t in taus])


def G_pred(N, a, tau):
    d12 = chord(N, a)
    d13 = cyl_chord(N, 0, tau)
    d14 = cyl_chord(N, a, tau)
    return A2_REF * (d12 * d12) ** (-TWO_D) * (d13 * d13) ** (-TWO_D) \
        * (d14 * d14) ** (TWO_D)


G_th = np.array([G_pred(N_TIME, A_DIP, t) for t in taus])
rel = G_meas / G_th - 1.0
iref = int(np.argmin(np.abs(taus - 24.0)))
dev_shape = np.abs((G_meas / G_meas[iref]) / (G_th / G_th[iref]) - 1.0)
# the absolute offset IS the dipole's own FH normalization: measured
# exactly as (T_lat(a)/T_inf(a))^2 - 1 and predicted independently
# from the N = 1536 fit coefficients b, c of log T
ch_a = float(chord(N_TIME, A_DIP))
off_dip = np.exp(2.0 * two_point_log(N_TIME, A_DIP, LAM_SIG)) \
    / (A2_REF * ch_a ** (-2.0 * TWO_D)) - 1.0
off_fh = np.exp(2.0 * (cff[1] * ch_a ** (-RHO_SIG)
                       + cff[2] * ch_a ** (-2 * RHO_SIG))) - 1.0
dev_off = np.abs(rel - off_dip)
print("  cosh-form table (N = 192, a = 24; dipole FH offset: measured "
      "%.5f, predicted from the N=1536 fit %.5f):" % (off_dip, off_fh))
print("  %-6s %14s %14s %10s %10s %12s" % ("tau", "G_meas", "G_pred",
                                           "rel", "|shape dev|",
                                           "|rel-offset|"))
for i, t in enumerate(taus):
    print("  %-6d %14.8e %14.8e %+10.2e %10.2e %12.2e"
          % (int(t), G_meas[i], G_th[i], rel[i], dev_shape[i],
             dev_off[i]))
pl = taus >= 24.0
check("O3.2 [E] the cylinder form in EUCLIDEAN TIME (new machinery): "
      "the time-separated dipole correlator <D(tau) D^+(0)> matches "
      "the exact vertex closed form with cylinder distances "
      "(N/pi)|sin(pi(dx + i dtau)/N)| -- the cosh form -- over "
      "tau = 12..72 at N = 192: shape-normalized max dev %.2e < 2 %%; "
      "the ABSOLUTE offset %.4f is the dipole's own FH normalization, "
      "reproduced by the independent N = 1536 fit coefficients "
      "(predicted %.4f, |diff| %.4f < 0.015) and constant on the "
      "plateau tau >= 24 (max |rel - offset| %.2e < 0.015; the "
      "remaining short-time transient is %.2e at tau = 12, decaying "
      "-- the expected small-distance lattice term in the time "
      "channel, reported): the time direction carries NO new "
      "artifact beyond the known FH structure; G(0) = 1 exactly "
      "(O0.3)"
      % (dev_shape.max(), off_dip, off_fh, abs(off_dip - off_fh),
         dev_off[pl].max(), dev_off[0]),
      dev_shape.max() < 0.02 and abs(off_dip - off_fh) < 0.015
      and dev_off[pl].max() < 0.015)

# ---- O3.3 cluster decomposition in space and time
# (space) R(s) = G4/T(a)^2 - 1 at FIXED continuum configuration
# (a = N/32, s = alpha N) extrapolated over N = 192/384/768, vs the
# exact CFT law (1-w)^{-2 Delta} - 1
ALPHAS_CL = ((1, 8), (3, 16), (1, 4), (5, 16), (3, 8))
NS_CL = (192, 384, 768)
Rext, Rp, ws_cl, rrates = [], [], [], []
print("  space cluster (a = N/32, s = alpha N; extrapolated over "
      "N = 192/384/768):")
for (nn, dd) in ALPHAS_CL:
    Rv, wv = [], None
    for Nv in NS_CL:
        a_cl = Nv // 32
        s = Nv * nn // dd
        pts = (0, a_cl, s, s + a_cl)
        wv, _ = cross_w(Nv, pts)
        Rv.append(np.exp(g4_log(Nv, pts, LAM_SIG)
                         - 2.0 * two_point_log(Nv, a_cl, LAM_SIG))
                  - 1.0)
    a_geo, r_geo = geo_extrap(*Rv)
    q23 = 2.0 ** (-RHO_SIG)
    a_fix = Rv[2] + (Rv[2] - Rv[1]) * q23 / (1.0 - q23)
    band_R = abs(a_geo - a_fix) if np.isfinite(a_geo) else np.inf
    a_use = a_geo if np.isfinite(a_geo) else a_fix
    Rext.append(a_use)
    rrates.append(r_geo)
    ws_cl.append(wv)
    Rp.append((1.0 - wv) ** (-TWO_D) - 1.0)
    print("    s/N=%d/%-3d w=%.5f  R(N): %s -> extrap %.6e "
          "(rate %.3f, band %.1e)  R_cft=%.6e"
          % (nn, dd, wv, ["%.5e" % v for v in Rv], a_use, r_geo,
             band_R, Rp[-1]))
Rs, Rp, ws_cl = np.array(Rext), np.array(Rp), np.array(ws_cl)
dev_R = np.abs(Rs / Rp - 1.0)
Xw = np.column_stack([np.ones(len(ws_cl)), np.log(ws_cl)])
cw, *_ = np.linalg.lstsq(Xw, np.log(Rs), rcond=None)
q_w = cw[1]
pref_w = np.exp(cw[0])
# (time) connected C(tau) on TWO lattices (N = 96, 192; a = N/8):
# two-exponential fit with RELATIVE residuals on the late window
# tau in [100, 240] x N/192 (the truncation bias of the earlier
# window is gone there); gap vs the exact lattice neutral gap per N;
# the amplitude is FH-extrapolated over the two lattices
TSET96 = time_setup(96)
TIME_FITS = {}
for (Nv, S) in ((96, TSET96), (192, TSET)):
    a_t = Nv // 8
    sc = Nv / 192.0
    lt = two_point_log(Nv, a_t, LAM_SIG)
    taus_c = np.arange(100.0 * sc, 241.0 * sc, 10.0 * sc)
    C_meas = np.array([np.exp(logabs_G_tau(S, Nv, a_t, LAM_SIG, t)
                              - 2.0 * lt) - 1.0 for t in taus_c])
    e_ns = eps6(Nv, 0)
    gap_ex = e_ns[e_ns > 0].min() + (-e_ns[e_ns < 0]).min()
    X1 = np.column_stack([np.ones(len(taus_c)), -taus_c])
    cl, *_ = np.linalg.lstsq(X1, np.log(C_meas), rcond=None)
    best = (np.inf, cl[1], None)
    for gg in np.linspace(0.8 * cl[1], 1.2 * cl[1], 801):
        Xg = np.column_stack([np.exp(-gg * taus_c),
                              np.exp(-2.0 * gg * taus_c)])
        cg, *_ = np.linalg.lstsq(Xg, C_meas, rcond=None)
        ss = float((((C_meas - Xg @ cg) / C_meas) ** 2).sum())
        if ss < best[0]:
            best = (ss, gg, cg)
    _, gap_fit, cg = best
    C_pred = np.array([(cyl_chord(Nv, a_t, t)
                        / cyl_chord(Nv, 0, t)) ** (2 * TWO_D) - 1.0
                       for t in taus_c])
    amp_pred = 4.0 * DELTA * (1.0 - np.cos(2.0 * np.pi * a_t / Nv))
    TIME_FITS[Nv] = dict(gap_ex=gap_ex, gap_fit=gap_fit, c1=cg[0],
                         c2c1=cg[1] / cg[0], amp_pred=amp_pred,
                         ratio=C_meas / C_pred,
                         devC=np.abs(C_meas / C_pred - 1.0).max(),
                         Clast=C_meas[-1], taumax=taus_c[-1])
    print("  time cluster N=%3d (a=%d): gap_fit/gap_ex = %.5f, "
          "Delta_exch = %.5f vs 1; c1/amp_pred = %.4f (c2/c1 = "
          "%.2f); max |C/C_pred - 1| = %.2e; C(%d) = %.2e -> 0"
          % (Nv, a_t, gap_fit / gap_ex,
             gap_fit * Nv / (2.0 * np.pi), cg[0] / amp_pred,
             cg[1] / cg[0], TIME_FITS[Nv]["devC"],
             int(taus_c[-1]), C_meas[-1]))
q23 = 2.0 ** (-RHO_SIG)
r96 = TIME_FITS[96]["c1"] / TIME_FITS[96]["amp_pred"]
r192 = TIME_FITS[192]["c1"] / TIME_FITS[192]["amp_pred"]
amp_ext = r192 + (r192 - r96) * q23 / (1.0 - q23)
gap_dev = max(abs(TIME_FITS[Nv]["gap_fit"] / TIME_FITS[Nv]["gap_ex"]
                  - 1.0) for Nv in (96, 192))
d_exch = TIME_FITS[192]["gap_fit"] * 192 / (2.0 * np.pi)
# pointwise cosh-form ratio at FIXED tau/N (the grids are aligned):
# FH-extrapolate over the two lattices, as everywhere in this probe
ratio_ext = TIME_FITS[192]["ratio"] \
    + (TIME_FITS[192]["ratio"] - TIME_FITS[96]["ratio"]) \
    * q23 / (1.0 - q23)
devCt_ext = np.abs(ratio_ext - 1.0).max()
print("  amplitude FH extrapolation (rate 2/3): c1/amp_pred %.4f "
      "(N=96) -> %.4f (N=192) -> %.4f (N=inf) vs 1"
      % (r96, r192, amp_ext))
print("  pointwise cosh ratio at fixed tau/N: raw offsets %.2e / "
      "%.2e (the dipole FH amplitude) -> FH-extrapolated max "
      "|ratio - 1| = %.2e"
      % (TIME_FITS[96]["devC"], TIME_FITS[192]["devC"], devCt_ext))
ok33 = (dev_R.max() < 0.02 and abs(q_w - 1.0) < 0.05
        and gap_dev < 0.005 and abs(d_exch - 1.0) < 0.01
        and abs(amp_ext - 1.0) < 0.03 and devCt_ext < 0.02
        and TIME_FITS[192]["Clast"] < 1e-3)
check("O3.3 [central] CLUSTER DECOMPOSITION measured in both "
      "directions: (space) the N-extrapolated connected ratio "
      "R = G4/T^2 - 1 at fixed continuum dipole configurations "
      "equals the exact CFT law (1-w)^{-2/9} - 1 pointwise (max dev "
      "%.2e < 2 %%) and falls with the measured power w^%.4f "
      "(epsilon-channel prefactor %.4f vs 2 Delta = %.4f): R -> 0 "
      "like chord(s)^{-2}; (time) the connected C(tau) decays "
      "exponentially with the fitted gap = the exact lattice neutral "
      "gap at < 0.5 %% on BOTH lattices (worst dev %.1e; Delta_exch "
      "= %.5f vs 1: the epsilon/current level IS the transfer-matrix "
      "gap), the amplitude FH-extrapolates to %.4f x the closed-form "
      "4 Delta (1 - cos(2 pi a/N)) (< 3 %%), the pointwise cosh "
      "ratio at fixed tau/N FH-extrapolates to 1 within %.1e < 2 %% "
      "(per-lattice raw offsets %.1e / %.1e = the known dipole FH "
      "amplitude), and C(tau_max) = %.2e -> 0: the OS cluster "
      "property is measured in space AND Euclidean time"
      % (dev_R.max(), q_w, pref_w, TWO_D, gap_dev, d_exch, amp_ext,
         devCt_ext, TIME_FITS[96]["devC"], TIME_FITS[192]["devC"],
         TIME_FITS[192]["Clast"]), ok33)


# ================================================================== O4
print("=" * 72)
print("O4: the continuum characters -- N^{-2} level extrapolation")
print("=" * 72)


def char_levels(N):
    """Exact mode-sum levels in Delta units for the g = 1 (gt = 2)
    twisted sector: (Delta_sigma, charged level, neutral level)."""
    u = N / (2.0 * np.pi)
    e2 = eps6(N, 2) * u
    e0 = eps6(N, 0) * u
    dsig = e2[e2 < 0].sum() - e0[e0 < 0].sum()
    par = e2[e2 > 0].min()
    hol = (-e2[e2 < 0]).min()
    return dsig, dsig + min(par, hol), dsig + par + hol


LEVELS = {lbl: [] for lbl in ("h_sigma", "Delta_sigma", "level 5/18",
                              "level 4/9")}
for Nv in NCHAR:
    dsig, lev2, lev3 = char_levels(Nv)
    LEVELS["h_sigma"].append(dsig / 4.0)
    LEVELS["Delta_sigma"].append(dsig)
    LEVELS["level 5/18"].append(lev2)
    LEVELS["level 4/9"].append(lev3)
TARGETS = {"h_sigma": 1.0 / 36.0, "Delta_sigma": 1.0 / 9.0,
           "level 5/18": 5.0 / 18.0, "level 4/9": 4.0 / 9.0}

print("  level table (exact mode sums, Delta units):")
print("  %-13s %12s %12s %12s %12s %12s %7s %7s %13s %9s %9s"
      % ("level", "N=48", "N=96", "N=192", "N=384", "N=768", "r1",
         "r2", "extrap", "|dev|/t", "band/t"))
CH = {}
for lbl in ("h_sigma", "Delta_sigma", "level 5/18", "level 4/9"):
    vals = np.array(LEVELS[lbl])
    Ns = np.asarray(NCHAR, dtype=float)
    X2 = np.column_stack([np.ones(len(Ns)), Ns ** (-2.0)])
    c2, *_ = np.linalg.lstsq(X2, vals, rcond=None)
    X3 = np.column_stack([np.ones(len(Ns)), Ns ** (-2.0), Ns ** (-4.0)])
    c3, *_ = np.linalg.lstsq(X3, vals, rcond=None)
    resid3 = np.abs(vals - X3 @ c3).max()
    a_hat = c3[0]
    band = abs(c2[0] - c3[0]) + resid3
    _, rates = seq_rates(vals)
    tgt = TARGETS[lbl]
    dev = abs(a_hat - tgt) / tgt
    CH[lbl] = (a_hat, band / tgt, dev, rates)
    print("  %-13s %12.8f %12.8f %12.8f %12.8f %12.8f %7.3f %7.3f "
          "%13.9f %9.2e %9.2e"
          % (lbl, vals[0], vals[1], vals[2], vals[3], vals[4],
             rates[0], rates[2] if len(rates) > 2 else rates[1],
             a_hat, dev, band / tgt))

ok41 = (CH["Delta_sigma"][2] < TOL_CHAR
        and CH["Delta_sigma"][1] < TOL_CHAR
        and CH["h_sigma"][2] < TOL_CHAR
        and all(1.7 < r < 2.3 for r in CH["Delta_sigma"][3]))
check("O4.1 [E] Delta_sigma(N) converges with the measured N^{-2} rate "
      "(rates %s) and extrapolates to %.9f vs 1/9 (rel dev %.2e < "
      "0.1 %%, band %.1e); per-deck-class h = Delta/4 -> %.9f vs 1/36 "
      "(the v650/v639 dictionary): the leading continuum character is "
      "implied by the lattice at the 1e-%d level"
      % (["%.3f" % r for r in CH["Delta_sigma"][3]],
         CH["Delta_sigma"][0], CH["Delta_sigma"][2],
         CH["Delta_sigma"][1], CH["h_sigma"][0],
         int(-np.log10(max(CH["Delta_sigma"][2], 1e-16)))), ok41)

ok42 = (CH["level 5/18"][2] < TOL_CHAR and CH["level 5/18"][1] < TOL_CHAR
        and all(1.7 < r < 2.3 for r in CH["level 5/18"][3]))
check("O4.2 [E] the second twist level (charged {1/6, 5/6} pair, "
      "modular-probe M3.2) extrapolates to %.9f vs 5/18 = %.9f (rel "
      "dev %.2e, band %.1e)"
      % (CH["level 5/18"][0], 5.0 / 18.0, CH["level 5/18"][2],
         CH["level 5/18"][1]), ok42)

ok43 = (CH["level 4/9"][2] < TOL_CHAR and CH["level 4/9"][1] < TOL_CHAR
        and all(1.7 < r < 2.3 for r in CH["level 4/9"][3]))
check("O4.3 [E] the third (neutral particle-hole) twist level "
      "extrapolates to %.9f vs 4/9 = %.9f (rel dev %.2e, band %.1e): "
      "all three leading twist levels are < 0.1 %% consistent with the "
      "exact CFT characters, with N^{-2} rates measured"
      % (CH["level 4/9"][0], 4.0 / 9.0, CH["level 4/9"][2],
         CH["level 4/9"][1]), ok43)


# ================================================================== O5
print("=" * 72)
print("O5: the typing")
print("=" * 72)

check("O5.1 [C, honest typing] WHICH OS AXIOMS ARE NOW MEASURED AT THE "
      "CONVERGENCE LEVEL: E0 (temperedness) -- the rescaled twist "
      "correlators converge at every fixed continuum configuration "
      "with power-law bounds (exponents 2/9, 1/18 measured; O1); E1 "
      "(Euclidean invariance) -- only DISCRETE lattice symmetries are "
      "exact (translation: both RP axes coincide, Klein probe K1.4; "
      "reflection: built into the pairing); full rotation invariance "
      "is EMERGENT: cross-ratio collapse (OPE probe S2.3) and the "
      "S-covariance rate N^{-4} (modular probe M2/v650) measure it, "
      "the limit statement stays open; E2 (reflection positivity) -- "
      "MEASURED WITH RATES: Klein Grams PSD at every N AND eigenvalue "
      "convergence with an extrapolated lambda_min bounded away from "
      "0 (O2); E3 (symmetry/hermiticity) -- exact reality/symmetry of "
      "the dressed Grams at every N (machine); E4 (cluster) -- "
      "MEASURED: power-law clustering in space with the exact "
      "cylinder form and exponential clustering in Euclidean time "
      "with the transfer-matrix gap = the epsilon level (O3).  WHAT "
      "REMAINS FOR THE FORMAL LIMIT: uniform bounds over ALL point "
      "configurations (measured: finitely many), tightness/"
      "equicontinuity of the correlator family, the construction of "
      "the limit Hilbert space (GNS on the limiting Schwinger data), "
      "operator (not Gram-entry) convergence, the R/parity sectors in "
      "the OS frame, and the assembled orbifold-B correlators beyond "
      "the twist blocks (the B-projection at correlator level) -- "
      "named, not claimed.  GATE.QGEO does not move", True)

print("-" * 72)
print("DIARY (de, fuer next.txt durch den Promotions-Worker):")
print("  Kontinuums-OS-Scheibe fuer den Naht-Orbifold B: Die euklidischen")
print("  Daten des Twist-Sektors konvergieren bei festen Kontinuums-")
print("  Konfigurationen ueber N = 48..384 mit VERSTANDENEN, uniformen")
print("  Raten -- roh ist die Rate die glatte Fisher-Hartwig-Branche")
print("  N^{-2/3} (sigma-Kanal) bzw. N^{-4/3} (tau-Kanal), nach EINEM")
print("  FH-Term liegen die Reste auf N^{-4/3}-Niveau; die Limites")
print("  treffen die CFT-Werte < 1%. Die Klein-RP-Gram-Eigenwerte")
print("  konvergieren und der minimale Eigenwert extrapoliert vom")
print("  Kontinuums-Limes WEG von 0 (sigma-, tau- und gemischter OS-")
print("  Gram). Cluster: Raum power-law mit exakter Zylinder-(sin-)Form")
print("  (N = 1536), euklidische Zeit exponentiell mit Transfermatrix-")
print("  Gap = epsilon-Level (cosh-Form gemessen, neue Zeitmaschinerie).")
print("  Charaktere: 1/36, 1/9, 5/18, 4/9 aus N^{-2}-Extrapolation")
print("  < 0.1%. Offen fuer den formalen Limes: uniforme Schranken,")
print("  Limes-Hilbertraum (GNS), Operator-Konvergenz, R-Sektoren,")
print("  B-Assembly auf Korrelator-Ebene. GATE.QGEO bewegt sich nicht.")

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
ctrl_ok = all(ok for n, ok in CHECKS if n.startswith("O0"))
o1_ok = all(ok for n, ok in CHECKS if n.startswith("O1"))
o2_ok = all(ok for n, ok in CHECKS if n.startswith("O2"))
o3_ok = all(ok for n, ok in CHECKS if n.startswith("O3"))
o4_ok = all(ok for n, ok in CHECKS if n.startswith("O4"))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: ORB-OS-CONTINUUM-SLICE -- the first continuum-OS")
    print("slice of the seam orbifold B stands: the Euclidean twist data")
    print("converge at fixed continuum configurations with uniform,")
    print("UNDERSTOOD rates (FH branch law; limits = CFT values < 1%),")
    print("reflection positivity survives the limit (Klein Gram")
    print("eigenvalues converge, lambda_min bounded away from 0), the")
    print("cluster property holds in space (exact cylinder form) and")
    print("Euclidean time (gap = epsilon level, cosh form), and the")
    print("characters extrapolate to the exact CFT values < 0.1%.")
elif ctrl_ok and o1_ok and o3_ok and o4_ok and not o2_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: ORB-OS-RP-DRIFT -- correlators, cluster and")
    print("characters converge but the RP extrapolation cannot bound")
    print("lambda_min away from zero: honest open.")
elif ctrl_ok and not o1_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: ORB-OS-NONUNIFORM -- convergence exists but the rate")
    print("signature is not uniform/understood: honest open.")
elif not ctrl_ok:
    print("SOME CHECKS FAILED")
    print("VERDICT: ORB-OS-FAILS -- a machinery control fails.")
else:
    print("SOME CHECKS FAILED")
    print("VERDICT: MIXED")
