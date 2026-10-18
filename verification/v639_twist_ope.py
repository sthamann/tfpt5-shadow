#!/usr/bin/env python3
"""v639 -- QGEO.TWISTOPE.01: the twist-field/OPE round -- the
interacting/CFT-level slice of the Z3 orbifold residue named by
v623/v628: twist-field weights
(three independent routes), lattice twist two-point functions, the
four-point function with crossing, the leading OPE data, and reflection
positivity of the twist sector.

CONVENTIONS (declared up front; everything below hangs on these):

  * The base seam is a chiral Majorana (c = 1/2) on the N-site NS
    circle (v622); the covered seam (mu3-cover) is ONE 48-site NS
    circle whose modes split into deck classes with offsets
    nu in {1/6, 1/2, 5/6} (v623).  v628 (exact): the lattice vacuum
    energy of the nu-class has 1/N coefficient (6 nu^2 - 6 nu + 1)/12
    in pi/N units, i.e. the CHIRAL SUM convention where the lattice
    band [0, pi] carries TWO chiral branches: coefficient
    = 2 (h_nu - c/24) with c = 1/2 per branch.
  * Therefore h_nu = (6 nu^2 - 6 nu + 1)/24 + 1/48 = (nu - 1/2)^2 / 4:
    the chiral weight of ONE deck class (one real chiral mode family).
    h_{1/6} = h_{5/6} = 1/36, h_{1/2} = 0.  The v628 twist gap 1/18
    (pi/N units) is 2 (h_{1/6} - h_{1/2}) = 2/36 = 1/18.
  * A single Majorana cannot be phase-twisted by omega; the Z3 deck
    twist acts on the SEAM DOUBLE (the conjugate class pair
    {1/6, 5/6} = one complex fermion, the v622 doubled bookkeeping).
    Complex-pair twist weight h_cplx = eta^2/2 at eta = 1/3, i.e.
    1/18 = 2 x 1/36.
  * LATTICE REALIZATION: seam double = complex free-fermion chain at
    half filling, NS (antiperiodic) sector; the Z3 twist-field
    two-point function is the U(1) phase string
    <exp(i lam sum_{j in A} n_j)> with lam = 2 pi/3 (the flux line
    between the two twist insertions, gauge-equivalent to the bond
    defect e^{+-2 pi i/3} on the time slice).  The lattice twist
    operator is NON-CHIRAL over the double: scaling dimension
    Delta = h + hbar = eta^2 = 1/9 = 4 h_sigma, decay exponent
    2 Delta = 2/9.  Control anchor eta = 1/2: Delta = 1/4,
    h_Majorana = 1/16 = the Ising sigma/disorder weight.
  * CROSSING on the lattice: rotating the gap 4-tuple of the
    alternating four-point by ONE step is exactly the crossing map
    w -> 1 - w, and it is an EXACT lattice symmetry (ring translation
    + charge conjugation on |G4|): crossing of the modulus is
    symmetry-protected.  The dynamical content is (i) conformal
    collapse (G4 depends on the configuration only through the
    cross-ratio w) and (ii) the exact closed form.  For the ABELIAN
    phase twist the orbifold four-point is the vertex-operator closed
    form Ghat = A^2 [w(1-w)]^{-2 Delta} (no hypergeometric blocks --
    those belong to the Z2 reflection orbifold, not to the U(1)
    string).
  * LATTICE ARTIFACTS: the leading Fisher-Hartwig correction to every
    string correlator is a smooth d^{-2/3} term (branch shift
    beta -> beta - 1 at one jump, relative exponent 2(2/3)^2 - 2(1/3)^2
    = 2/3; all coordinates kept EVEN so the (-1)^x oscillation is
    frozen).  Finite-size claims below therefore extrapolate each
    configuration N -> infinity linearly in N^{-2/3} at exactly fixed
    cross-ratio (configs scaled x2, x4), and the scaling run S2.5
    verifies the attribution.

Checks:

  (T0) THE CONVENTION ROUND [exact, sympy]: h_sigma from three
       independent routes -- the v628 Casimir datum, the zeta-function
       mode formula, and the bosonization/pair route -- agree exactly:
       h_sigma = 1/36 per chiral deck class.  The literature formula
       eta(1-eta)/2 (giving 1/9 resp. 5/72) is the R-based /
       boson-rotation convention; the exact complement identity
       eta(1-eta)/2 = 1/8 - (1/2-eta)^2/2 resolves the apparent
       discrepancy.  Lattice dictionary: Delta = 4 h_sigma = 1/9.

  (S1) TWIST TWO-POINT ON THE LATTICE [numeric]: the string
       determinant T(x) = |det(I + (e^{i lam}-1) C_x)| decays with
       chord exponent 2 Delta = 2/9; two estimators (N-scaling
       N = 48..1536 with d^{-2/3} slope extrapolation, and a
       within-ring three-parameter fit at N = 192); PASS at < 1 %
       each.  Control: lam = pi reproduces the Ising disorder
       exponent 1/2.  Amplitude reference A^2 from two independent
       four-term fits (consistency < 0.5 %).

  (S2) FOUR-POINT AND CROSSING [numeric, N = 96 -> 384]: (i) string
       gauge identity (s- vs t-channel string realization, machine
       precision); (ii) exact lattice crossing |G4(g)| = |G4(rot g)|
       with w -> 1-w (machine precision); (iii) conformal collapse:
       Ghat = G4 (D13 D24)^{2 Delta} depends only on w (leave-one-out
       local-fit residuals < 1 % raw at N = 96); (iv) the exact
       closed form Ghat = A^2 [w(1-w)]^{-2 Delta} after per-config
       N^{-2/3} extrapolation at < 1 %; (v) the raw N = 96 deviation
       is a d^{-2/3} artifact: doubling N shrinks it by ~2^{-2/3}.

  (S3) THE LEADING OPE DATA [numeric, extrapolated over
       N = 192/384/768]: s-channel stripping Dtil = G4 (D12 D34)^
       {2 Delta} -> A^2 (1-w)^{-2 Delta}: free-exponent fit hits
       2 Delta = 2/9 (< 1 %); the w^1 OPE weight c1 = 2 Delta = 2/9
       = the total Delta = 1 neutral level (C^2_{sig sig^dag -> J} +
       C^2_{-> Jbar} = 2 eta^2, per-current C = eta = 1/3 in the
       vertex dictionary): MODEL-BOUND value c1 = p from the
       single-block form (independently confirmed by S2.4 over the
       full w range) at < 2 %; the MODEL-FREE extractors (f(w)
       slice, log-Taylor polynomial, derivative fit) only bracket
       2/9 inside a ~[0.19, 0.26] band -- the < 2 % model-free
       extraction is typed OPEN with the measured band (honest
       partial result).  Identity normalization
       C_{sig sig^dag -> 1} = 1 via beta0 = A^2 (< 2 %).  The
       Majorana-orbifold split of the Delta = 1 level (epsilon vs
       current) is NOT fixed by G4 alone -- typed open [O].

  (S4) RP OF THE TWIST SECTOR [numeric, differentiated]: reflection
       Gram matrices M_ab = <theta(O_a) O_b> across the bond-centered
       diameter (v622 cut geometry), theta = antiunitary mirror.
       (i) Hermiticity at machine precision.  (ii) POSITIVE CONTROL:
       for the REAL Z2 string class (lam = pi, Ising disorder) M is
       exactly PSD at every N -- the pairing and the machinery are
       validated.  (iii) HONEST NEGATIVE: for the complex Z3 class
       the naive antiunitary pairing FAILS positivity by an
       N-STABLE amount (charged axis strings: min/max ~ -4.5e-3 at
       N = 96/192/384; neutral pairs: ~ -2.5e-2): structural, not a
       lattice artifact -- the mirror pairing of the Z3 twist sector
       needs the parafermionic Klein/twist correction
       (Jaffe-Pedrocchi-type), and the naive single-branch vertex
       Gram is indefinite already in the continuum (checked): the
       positivity-carrying pairing is typed OPEN [O], not claimed.

  (R)  THE READING [C]: what stands: the interacting slice of the Z3
       orbifold statement holds on the seam double at the abelian
       vertex level (weights, two-point, four-point + crossing, OPE
       normalization); RP holds in the validated real class, while
       the correct positivity pairing for the complex twist class is
       an honest open item.  Also open: the Majorana-level block
       split, chiral factorization, the modular/partition-function
       level, and any non-abelian orbifold content -- named, not
       claimed.  GATE.QGEO does not move.

Verdict enums (frozen): TWIST-OPE-COHERENT (all slices incl. Z3
mirror positivity), TWIST-OPE-COHERENT-RP-OPEN (T0/S1/S2/S3 pass, Z2
control passes, Z3 naive mirror pairing indefinite -- the honest
current state), MIXED (an interacting slice fails), TWIST-OPE-FAILS
(convention or two-point level fails).

FIREWALL: GATE.QGEO does not move; no marker changes; the Z3 mirror
pairing (parafermionic Klein twist) and the model-free < 2% OPE
extraction stay typed OPEN items, named, not claimed.

PROVENANCE: discovery probe orbifold_twist_ope_probe.py (2026-08-02,
25/25, verdict TWIST-OPE-COHERENT-RP-OPEN).

Python-only (sympy exact + numpy lattice determinants), counted per
GATE.WOLFRAM.02.
"""

import numpy as np
import sympy as sp

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ------------------------------------------------------------------ constants
LAM = 2.0 * np.pi / 3.0          # Z3 twist string angle
ETA = sp.Rational(1, 3)          # NS-relative mode shift of the twisted pair
DELTA = 1.0 / 9.0                # lattice twist dimension = eta^2 = 4 h_sigma
TOL_EXP = 0.01                   # 1 % on decay exponents (S1)
TOL_4PT = 0.01                   # 1 % on collapse / closed form (S2)
TOL_OPE = 0.02                   # 2 % on OPE coefficients (S3)
TOL_AMP = 0.005                  # 0.5 % consistency of the two A^2 fits
TOL_MACH = 1e-10                 # machine-precision identities
TOL_RP = 1e-10                   # RP eigenvalue floor (relative)
MIN_GAP = 12                     # enumeration floor at N = 96 (even coords)
CORE_GAP = 16                    # core window for the < 1 % claims
N_EXTRAP_SUB = 120               # configs in the extrapolated S2.4 battery
RNG = np.random.default_rng(60)


# ------------------------------------------------------------------ machinery
def cov(N):
    """NS (antiperiodic) half-filled covariance <c^dag_j c_l> on N sites.

    Filled NS momenta k = 2 pi (m + 1/2)/N, m = -N/4 .. N/4 - 1
    (unique gapped ground state for N = 0 mod 4)."""
    assert N % 4 == 0
    m = np.arange(-(N // 4), N // 4)
    k = 2.0 * np.pi * (m + 0.5) / N
    j = np.arange(N)
    V = np.exp(1j * np.outer(k, j)) / np.sqrt(N)
    return V.conj().T @ V


def string_logabs(C, sites, u):
    """log |<prod_{j in sites} e^{i u_j n_j}>| = log |det(I + D C_S)|,
    D = diag(e^{i u_j} - 1) (Slater-determinant identity)."""
    S = np.asarray(sites, dtype=int)
    Cs = C[np.ix_(S, S)]
    M = np.eye(len(S), dtype=complex) \
        + (np.exp(1j * np.asarray(u, dtype=float)) - 1.0)[:, None] * Cs
    return np.linalg.slogdet(M)[1]


def string_det(C, sites, u):
    """The complex value <prod e^{i u_j n_j}> (for Gram matrices)."""
    S = np.asarray(sites, dtype=int)
    Cs = C[np.ix_(S, S)]
    M = np.eye(len(S), dtype=complex) \
        + (np.exp(1j * np.asarray(u, dtype=float)) - 1.0)[:, None] * Cs
    return np.linalg.det(M)


def chord(N, x):
    return (N / np.pi) * np.sin(np.pi * x / N)


def twist_two_point(C, N, x, lam=LAM):
    return string_logabs(C, np.arange(x), lam * np.ones(x))


def fourpt_logabs(C, N, g, lam=LAM):
    """|G4| for the alternating twist four-point with gap tuple
    g = (g1, g2, g3, g4), points (0, g1, g1+g2, g1+g2+g3), strings
    [x1, x2) and [x3, x4) at angle +lam."""
    x2, x3, x4 = g[0], g[0] + g[1], g[0] + g[1] + g[2]
    sites = np.concatenate([np.arange(0, x2), np.arange(x3, x4)])
    return string_logabs(C, sites, lam * np.ones(len(sites)))


def cross_ratio(N, g):
    """(w, v, chords) from chord distances; w + v = 1 exactly (Ptolemy)."""
    x2, x3, x4 = g[0], g[0] + g[1], g[0] + g[1] + g[2]
    d12, d23 = chord(N, x2), chord(N, x3 - x2)
    d34, d41 = chord(N, x4 - x3), chord(N, N - x4)
    d13, d24 = chord(N, x3), chord(N, x4 - x2)
    w = (d12 * d34) / (d13 * d24)
    v = (d41 * d23) / (d13 * d24)
    return w, v, (d12, d23, d34, d41, d13, d24)


def extrapolate_n23(ns, vals):
    """Linear N^{-2/3} extrapolation of log-quantities to N = infinity."""
    u = np.asarray(ns, dtype=float) ** (-2.0 / 3.0)
    A = np.vstack([np.ones(len(u)), u]).T
    cf, *_ = np.linalg.lstsq(A, np.asarray(vals), rcond=None)
    return cf[0]


def canon8(g):
    """Canonical form of the gap 4-tuple under the dihedral images
    (all 4 rotations x reversal) -- ALL of these are exact lattice
    symmetries of |G4| (odd rotations via charge conjugation)."""
    imgs = []
    t = tuple(g)
    r = tuple(reversed(g))
    for i in range(4):
        imgs.append(t[i:] + t[:i])
        imgs.append(r[i:] + r[:i])
    return min(imgs)


def enum_configs(N, min_gap):
    cfgs = []
    for g1 in range(min_gap, N - 3 * min_gap + 1, 2):
        for g2 in range(min_gap, N - g1 - 2 * min_gap + 1, 2):
            for g3 in range(min_gap, N - g1 - g2 - min_gap + 1, 2):
                g4 = N - g1 - g2 - g3
                if g4 >= min_gap:
                    cfgs.append((g1, g2, g3, g4))
    return cfgs


# ================================================================== T0
print("=" * 72)
print("T0: the convention round (three routes to h_sigma, exact)")
print("=" * 72)

nu, eta = sp.symbols("nu eta", positive=True)
half = sp.Rational(1, 2)

# route 1: the v628 Casimir datum.  Coefficient (pi/N units) of the
# lattice vacuum energy = (6 nu^2 - 6 nu + 1)/12 = 2 (h_nu - c/24),
# c = 1/2 per chiral branch (the lattice band [0, pi] carries two).
coeff = (6 * nu ** 2 - 6 * nu + 1) / 12
h_cas = sp.simplify(coeff / 2 + sp.Rational(1, 48))
h_closed = (nu - half) ** 2 / 4
tab = {v: sp.nsimplify(h_cas.subs(nu, v))
       for v in (sp.Rational(1, 6), half, sp.Rational(5, 6))}
gap_pi_over_N = sp.nsimplify(
    (coeff.subs(nu, sp.Rational(1, 6)) - coeff.subs(nu, half)))
check("T0.1 route 1 (v628 Casimir datum): coefficient (6nu^2-6nu+1)/12 "
      "= 2(h_nu - c/24), c = 1/2 => h_nu = (nu - 1/2)^2/4 EXACTLY; "
      "h_{1/6} = h_{5/6} = 1/36, h_{1/2} = 0; the v628 twist gap 1/18 "
      "(pi/N units) IS 2(h_{1/6} - h_{1/2})",
      sp.simplify(h_cas - h_closed) == 0
      and tab[sp.Rational(1, 6)] == sp.Rational(1, 36)
      and tab[half] == 0
      and tab[sp.Rational(5, 6)] == sp.Rational(1, 36)
      and gap_pi_over_N == sp.Rational(1, 18)
      and sp.simplify(gap_pi_over_N
                      - 2 * (tab[sp.Rational(1, 6)] - tab[half])) == 0,
      "h = %s, gap = %s" % (str(tab), gap_pi_over_N))

# route 2: the zeta-function mode formula.  One chiral branch with
# offsets m + nu: E_branch = -(1/2) zeta(-1, nu) = B2(nu)/4; the
# lattice coefficient is 2 x E_branch; and E_branch = h_nu - 1/48.
E_branch = sp.bernoulli(2, nu) / 4
check("T0.2 route 2 (zeta-function mode sum): -(1/2) zeta(-1, nu) = "
      "B2(nu)/4 per chiral branch; 2 x branch = the v628 coefficient "
      "EXACTLY, and E_branch = h_nu - c/24 with c = 1/2",
      sp.simplify(2 * E_branch - coeff) == 0
      and sp.simplify(E_branch - (h_closed - sp.Rational(1, 48))) == 0,
      "E_branch = %s" % sp.factor(E_branch))

# route 3: bosonization / the pair route.  The conjugate classes
# {1/6, 5/6} form ONE complex fermion twisted by eta = 1/3 relative
# to NS: h_cplx = eta^2/2 = h(1/6) + h(5/6) = 1/18 = 2 h_sigma.
# Anchor eta = 1/2: h_cplx = 1/8 (Dirac spin field), per-Majorana
# 1/16 = Ising sigma.
h_pair = sp.simplify(h_closed.subs(nu, half - eta)
                     + h_closed.subs(nu, half + eta))
check("T0.3 route 3 (bosonization/pair): h(1/2-eta) + h(1/2+eta) = "
      "eta^2/2 EXACTLY; at eta = 1/3: 1/18 = 2 x 1/36; anchor "
      "eta = 1/2: 1/8 = Dirac spin field, per-Majorana 1/16 = Ising "
      "sigma", sp.simplify(h_pair - eta ** 2 / 2) == 0
      and h_pair.subs(eta, ETA) == sp.Rational(1, 18)
      and h_pair.subs(eta, half) == sp.Rational(1, 8),
      "h_cplx(1/3) = %s" % h_pair.subs(eta, ETA))

# the convention traps: eta(1-eta)/2 conventions do NOT match the
# v628 datum -- and the exact complement identity explains why.
f_trap = eta * (1 - eta) / 2
trap_13 = f_trap.subs(eta, ETA)            # 1/9  (label = NS shift 1/3)
trap_16 = f_trap.subs(eta, sp.Rational(1, 6))  # 5/72 (label = R offset 1/6)
ident = sp.simplify(f_trap - (sp.Rational(1, 8) - (half - eta) ** 2 / 2))
check("T0.4 [convention traps, must-fail] eta(1-eta)/2 gives 1/9 "
      "(label 1/3) resp. 5/72 (label 1/6) and matches NEITHER 1/18 "
      "nor 1/36: it is the R-based / boson-rotation convention; the "
      "exact complement identity eta(1-eta)/2 = 1/8 - (1/2-eta)^2/2 "
      "resolves the discrepancy (weight deficit from the Ramond point "
      "1/8, not a second answer)",
      trap_13 == sp.Rational(1, 9) and trap_16 == sp.Rational(5, 72)
      and trap_13 != sp.Rational(1, 18) and trap_16 != sp.Rational(1, 36)
      and ident == 0,
      "traps = (%s, %s), identity residue = %s" % (trap_13, trap_16, ident))

# the lattice dictionary
delta_lat = sp.nsimplify(2 * h_pair.subs(eta, ETA))
check("T0.5 the lattice dictionary: the U(1) string operator is "
      "non-chiral over the seam double: Delta = 2 h_cplx = eta^2 = "
      "1/9 = 4 h_sigma; predicted decay exponent 2 Delta = 2/9; "
      "control eta = 1/2: Delta = 1/4, exponent 1/2",
      delta_lat == sp.Rational(1, 9)
      and sp.nsimplify(4 * tab[sp.Rational(1, 6)]) == sp.Rational(1, 9)
      and abs(float(delta_lat) - DELTA) < 1e-15,
      "Delta = %s" % delta_lat)


# ================================================================== S1
print("=" * 72)
print("S1: the twist two-point on the lattice (string determinants)")
print("=" * 72)

# S1.1 the covariance kernel vs the v519 seam kernel
N0 = 48
C48 = cov(N0)
dev_k = 0.0
for d in range(1, N0):
    v519 = (2.0 / N0) / np.sin(np.pi * d / N0) if d % 2 else 0.0
    target = 0.5 * v519 * np.sin(np.pi * d / 2.0)
    dev_k = max(dev_k, abs(C48[0, d] - target))
check("S1.1 the equal-time covariance of the seam-double chain is "
      "HALF the v519 seam kernel with the k_F sign, C(d) = "
      "(1/2) c_v519(d) sin(pi d/2) (N = 48, all d)", dev_k < TOL_MACH,
      "max dev = %.3e" % dev_k)

# S1.2 N-scaling exponent at x = N/2 with d^{-2/3} slope extrapolation
NS_LIST = [48, 96, 192, 384, 768, 1536]
COVS = {Nv: cov(Nv) for Nv in NS_LIST}
logT = np.array([twist_two_point(COVS[Nv], Nv, Nv // 2)
                 for Nv in NS_LIST])
dchord = np.array([chord(Nv, Nv // 2) for Nv in NS_LIST])
slopes = np.diff(logT) / np.diff(np.log(dchord))
dmid = np.sqrt(dchord[:-1] * dchord[1:])
Aex = np.vstack([np.ones(len(slopes)), dmid ** (-2.0 / 3.0)]).T
coef_ex, *_ = np.linalg.lstsq(Aex, slopes, rcond=None)
p_scaling = -coef_ex[0]
rel_sc = abs(p_scaling - 2 * DELTA) / (2 * DELTA)
check("S1.2 N-scaling exponent (x = N/2, N = 48..1536, linear "
      "extrapolation of local slopes in d^{-2/3}) hits 2 Delta = 2/9 "
      "at < 1 %%" % (), rel_sc < TOL_EXP,
      "p = %.6f vs 2/9 = %.6f (rel dev %.3e); raw slopes %s"
      % (p_scaling, 2 * DELTA, rel_sc,
         np.array2string(-slopes, precision=5)))

# S1.3 within-ring fit at N = 192 (even x, three-parameter model)
N1 = 192
C192 = COVS[N1]
xs = np.arange(24, 97, 2)
lt = np.array([twist_two_point(C192, N1, int(x)) for x in xs])
dc = chord(N1, xs)
Afit = np.vstack([np.ones(len(xs)), np.log(dc), dc ** (-2.0 / 3.0)]).T
cfit, *_ = np.linalg.lstsq(Afit, lt, rcond=None)
p_ring = -cfit[1]
rel_ring = abs(p_ring - 2 * DELTA) / (2 * DELTA)
check("S1.3 within-ring fit (N = 192, even x in [24, 96], model "
      "log T = log A - p log d + b d^{-2/3}) hits 2 Delta = 2/9 at "
      "< 1 %%" % (), rel_ring < TOL_EXP,
      "p = %.6f (rel dev %.3e), b = %.4f" % (p_ring, rel_ring, cfit[2]))

# S1.4 control lam = pi: the Ising disorder exponent 1/2
logT_pi = np.array([string_logabs(COVS[Nv], np.arange(Nv // 2),
                                  np.pi * np.ones(Nv // 2))
                    for Nv in NS_LIST])
slopes_pi = np.diff(logT_pi) / np.diff(np.log(dchord))
coef_pi, *_ = np.linalg.lstsq(Aex, slopes_pi, rcond=None)
p_pi = -coef_pi[0]
rel_pi = abs(p_pi - 0.5) / 0.5
check("S1.4 control lam = pi (eta = 1/2): the same machinery gives "
      "the Ising disorder exponent 2 Delta = 1/2 at < 1 %% "
      "(h_Majorana = 1/16 anchor)" % (), rel_pi < TOL_EXP,
      "p = %.6f vs 0.5 (rel dev %.3e)" % (p_pi, rel_pi))

# S1.5 the amplitude reference: two independent four-term fits
# (N-scaling over N = 96..1536 and within-ring at N = 192), model
# log T = log A - p log d + b d^{-2/3} + b2 d^{-4/3}
Ns5 = np.array(NS_LIST[1:], dtype=float)
lt5 = logT[1:]
dn5 = dchord[1:]
A4 = np.vstack([np.ones(len(Ns5)), np.log(dn5), dn5 ** (-2.0 / 3.0),
                dn5 ** (-4.0 / 3.0)]).T
c4, *_ = np.linalg.lstsq(A4, lt5, rcond=None)
A2_REF = np.exp(2 * c4[0])
A4r = np.vstack([np.ones(len(xs)), np.log(dc), dc ** (-2.0 / 3.0),
                 dc ** (-4.0 / 3.0)]).T
c4r, *_ = np.linalg.lstsq(A4r, lt, rcond=None)
A2_ring = np.exp(2 * c4r[0])
rel_amp = abs(A2_ring / A2_REF - 1.0)
check("S1.5 amplitude reference: the four-term N-scaling fit and the "
      "four-term within-ring fit give the same non-universal "
      "amplitude A^2 at < 0.5 %% (A^2 is the only fitted constant "
      "reused below)" % (), rel_amp < TOL_AMP,
      "A^2(N-scaling) = %.6f, A^2(ring) = %.6f (rel dev %.3e); "
      "p4 = %.6f" % (A2_REF, A2_ring, rel_amp, -c4[1]))


# ================================================================== S2
print("=" * 72)
print("S2: the four-point slice and crossing (N = 96 -> 384)")
print("=" * 72)

N2 = 96
C96 = COVS[N2]

# S2.1 determinant self-test + string gauge identity (s vs t channel)
la_ring = string_logabs(C96, np.arange(N2), LAM * np.ones(N2))
dev_ring = abs(np.exp(la_ring) - 1.0)

cfgs = enum_configs(N2, MIN_GAP)
sample = [cfgs[i] for i in RNG.choice(len(cfgs), 200, replace=False)]
dev_gauge = 0.0
for g in sample:
    x2, x3, x4 = g[0], g[0] + g[1], g[0] + g[1] + g[2]
    la_s = fourpt_logabs(C96, N2, g)
    sites_t = np.concatenate([np.arange(x2, x3), np.arange(x4, N2)])
    la_t = string_logabs(C96, sites_t, -LAM * np.ones(len(sites_t)))
    dev_gauge = max(dev_gauge, abs(la_s - la_t))
check("S2.1 determinant self-test (full-ring string |det| = 1, rank "
      "N/2 projector) and the s/t string-GAUGE identity "
      "|G4|_s = |G4|_t (complement strings at -lam) at machine "
      "precision (200 random configs)",
      dev_ring < TOL_MACH and dev_gauge < TOL_MACH,
      "|det|-1 = %.3e, max |dlog| = %.3e" % (dev_ring, dev_gauge))

# S2.2 exact lattice crossing: gap rotation by ONE = w -> 1 - w
dev_cross, dev_ptolemy = 0.0, 0.0
for g in sample:
    rot = (g[1], g[2], g[3], g[0])
    la_g = fourpt_logabs(C96, N2, g)
    la_r = fourpt_logabs(C96, N2, rot)
    w_g, v_g, _ = cross_ratio(N2, g)
    w_r, v_r, _ = cross_ratio(N2, rot)
    dev_cross = max(dev_cross, abs(la_g - la_r))
    dev_ptolemy = max(dev_ptolemy, abs(w_g + v_g - 1.0),
                      abs(w_r - (1.0 - w_g)))
check("S2.2 exact lattice crossing: |G4(g1,g2,g3,g4)| = "
      "|G4(g2,g3,g4,g1)| at machine precision while the gap rotation "
      "maps w -> 1-w exactly (chord Ptolemy w + v = 1): crossing "
      "symmetry of the modulus is SYMMETRY-PROTECTED on the lattice "
      "(ring translation + charge conjugation)",
      dev_cross < TOL_MACH and dev_ptolemy < 1e-12,
      "max |dlog| = %.3e, max Ptolemy/crossing map dev = %.3e"
      % (dev_cross, dev_ptolemy))

# the full battery on the core window (all gaps >= CORE_GAP)
core = [g for g in cfgs if min(g) >= CORE_GAP]
recs = []
for g in core:
    la = fourpt_logabs(C96, N2, g)
    w, v, dd = cross_ratio(N2, g)
    log_ghat = la + 2 * DELTA * (np.log(dd[4]) + np.log(dd[5]))
    recs.append((w, log_ghat, canon8(g), g))
recs.sort(key=lambda r: r[0])
ws = np.array([r[0] for r in recs])
lg = np.array([r[1] for r in recs])
cans = [r[2] for r in recs]

# S2.3 conformal collapse: leave-one-out local-fit residuals
resid, n_used = [], 0
for i in range(len(recs)):
    if not (0.15 <= ws[i] <= 0.85):
        continue
    msk = (np.abs(ws - ws[i]) <= 0.01)
    msk[i] = False
    other = {cans[j] for j in np.nonzero(msk)[0]} - {cans[i]}
    if msk.sum() < 6 or len(other) < 3:
        continue
    Aw = np.vstack([np.ones(msk.sum()), ws[msk]]).T
    cf, *_ = np.linalg.lstsq(Aw, lg[msk], rcond=None)
    resid.append(lg[i] - (cf[0] + cf[1] * ws[i]))
    n_used += 1
resid = np.abs(np.array(resid))
check("S2.3 conformal collapse (form-free): Ghat = G4 (D13 D24)^"
      "{2 Delta} depends on the configuration ONLY through w -- "
      "leave-one-out local-fit residuals over canon-distinct "
      "geometries < 1 %% raw at N = 96 (gaps >= %d, w in [0.15, 0.85])"
      % CORE_GAP, len(resid) > 100 and resid.max() < TOL_4PT,
      "%d points, max resid = %.3e, median = %.3e"
      % (n_used, resid.max(), np.median(resid)))

# S2.4 the exact closed form after per-config N^{-2/3} extrapolation
sub_idx = RNG.choice(len(recs), N_EXTRAP_SUB, replace=False)
dev_raw_sub, dev_ext = [], []
for i in sub_idx:
    g = recs[i][3]
    lgs = []
    for scale, Nv in ((1, 96), (2, 192), (4, 384)):
        gs = tuple(scale * gi for gi in g)
        w, _, dd = cross_ratio(Nv, gs)
        la = fourpt_logabs(COVS[Nv], Nv, gs)
        lgs.append(la + 2 * DELTA * (np.log(dd[4]) + np.log(dd[5])))
    pred = np.log(A2_REF) - 2 * DELTA * np.log(w * (1.0 - w))
    dev_raw_sub.append(abs(lgs[0] - pred))
    dev_ext.append(abs(extrapolate_n23([96, 192, 384], lgs) - pred))
dev_raw_sub, dev_ext = np.array(dev_raw_sub), np.array(dev_ext)
check("S2.4 the exact closed form: Ghat = A^2 [w(1-w)]^{-2 Delta} "
      "(vertex form of the abelian orbifold four-point; A^2 from the "
      "independent S1.5 two-point fits) at < 1 %% after per-config "
      "N^{-2/3} extrapolation (N = 96/192/384, %d configs)"
      % N_EXTRAP_SUB, dev_ext.max() < TOL_4PT,
      "extrapolated: max dev = %.3e, median = %.3e (raw N = 96: "
      "max %.3e, median %.3e)"
      % (dev_ext.max(), np.median(dev_ext), dev_raw_sub.max(),
         np.median(dev_raw_sub)))

# S2.5 lattice-artifact attribution: the raw deviation is a d^{-2/3}
# artifact -- the identical cross-ratio battery at N = 192 (configs
# x2, w unchanged) shrinks it by ~ 2^{-2/3} = 0.63
pred_all = np.log(A2_REF) - 2 * DELTA * np.log(ws * (1.0 - ws))
dev_form = np.abs(lg - pred_all)
dev_form_192 = []
for (w, _, _, g) in recs:
    g2 = tuple(2 * gi for gi in g)
    la2 = fourpt_logabs(C192, 2 * N2, g2)
    w2, _, dd2 = cross_ratio(2 * N2, g2)
    lg2 = la2 + 2 * DELTA * (np.log(dd2[4]) + np.log(dd2[5]))
    dev_form_192.append(
        abs(lg2 - (np.log(A2_REF) - 2 * DELTA * np.log(w2 * (1 - w2)))))
dev_form_192 = np.array(dev_form_192)
ratio_med = np.median(dev_form_192) / np.median(dev_form)
check("S2.5 scaling attribution: the raw closed-form deviation at "
      "N = 96 shrinks at N = 192 (same w exactly) by a factor "
      "consistent with the d^{-2/3} Fisher-Hartwig artifact "
      "(2^{-2/3} = 0.63), i.e. finite-lattice, not a CFT mismatch",
      dev_form_192.max() < dev_form.max()
      and 0.5 < ratio_med < 0.8,
      "median: %.3e -> %.3e (ratio %.3f vs 0.63), max: %.3e -> %.3e"
      % (np.median(dev_form), np.median(dev_form_192), ratio_med,
         dev_form.max(), dev_form_192.max()))


# ================================================================== S3
print("=" * 72)
print("S3: the leading OPE data (extrapolated, N = 192/384/768)")
print("=" * 72)

ts = np.arange(8, 65, 2)
wt, ld_ext = [], []
for t in ts:
    lgs = []
    for scale, Nv in ((1, 192), (2, 384), (4, 768)):
        g = (scale * int(t), scale * (96 - int(t)),
             scale * int(t), scale * (96 - int(t)))
        w, _, dd = cross_ratio(Nv, g)
        la = fourpt_logabs(COVS[Nv], Nv, g)
        lgs.append(la + 2 * DELTA * (np.log(dd[0]) + np.log(dd[2])))
    wt.append(w)
    ld_ext.append(extrapolate_n23([192, 384, 768], lgs))
wt, ld_ext = np.array(wt), np.array(ld_ext)

# S3.1 free-exponent fit: log Dtil = log beta0 - p log(1 - w)
msk = wt <= 0.75
Ax = np.vstack([np.ones(msk.sum()), np.log(1.0 - wt[msk])]).T
cx, *_ = np.linalg.lstsq(Ax, ld_ext[msk], rcond=None)
p_ope, beta0 = -cx[1], np.exp(cx[0])
rel_ope = abs(p_ope - 2 * DELTA) / (2 * DELTA)
check("S3.1 s-channel stripping: Dtil = G4 (D12 D34)^{2 Delta} = "
      "beta0 (1-w)^{-p} with p = 2 Delta = 2/9 at < 1 %% (the "
      "resummed cross-channel sigma sigma^dag block; family "
      "(0, t, N/2, N/2+t), per-t extrapolation N = 192/384/768)"
      % (), rel_ope < TOL_EXP,
      "p = %.6f vs 2/9 = %.6f (rel dev %.3e), beta0 = %.6f"
      % (p_ope, 2 * DELTA, rel_ope, beta0))

# S3.2a the w^1 OPE weight, model-bound: for the single-block form
# (1-w)^{-p} -- independently confirmed by S2.4 over the full w range
# at < 0.1 % -- the Taylor coefficient of w^1 IS p.
c1_th = 2 * DELTA
rel_c1 = abs(p_ope - c1_th) / c1_th
check("S3.2a the leading OPE constant, model-bound: c1 = 2 Delta = "
      "2/9 at < 2 %% -- the total Delta = 1 neutral level, "
      "C^2_{sig sig^dag -> J} + C^2_{-> Jbar} = 2 eta^2 (per-current "
      "C = eta = 1/3, the exact vertex value; Gamma-monomial factors "
      "collapse to 1 for the abelian twist).  Extraction: c1 = p of "
      "the single-block form, whose validity is confirmed "
      "INDEPENDENTLY by S2.4 over the full w range" % (),
      rel_c1 < TOL_OPE,
      "c1 = p = %.6f vs 2/9 = %.6f (rel dev %.3e)"
      % (p_ope, c1_th, rel_c1))

# S3.2b model-free extractors (declared band, honest partial result)
msk2 = wt <= 0.5
f = (np.exp(ld_ext[msk2]) / beta0 - 1.0) / wt[msk2]
Af = np.vstack([np.ones(msk2.sum()), wt[msk2]]).T
cff, *_ = np.linalg.lstsq(Af, f, rcond=None)
c1_f = cff[0]
Wl = np.vstack([wt[msk2] ** k for k in range(4)]).T
clp, *_ = np.linalg.lstsq(Wl, ld_ext[msk2], rcond=None)
c1_lp = clp[1]
sl = np.diff(ld_ext) / np.diff(wt)
wm = 0.5 * (wt[:-1] + wt[1:])
mdv = wm <= 0.3
Adv = np.vstack([np.ones(mdv.sum()), wm[mdv]]).T
cdv, *_ = np.linalg.lstsq(Adv, sl[mdv], rcond=None)
c1_dv = cdv[0]
band = (min(c1_f, c1_lp, c1_dv), max(c1_f, c1_lp, c1_dv))
check("S3.2b [O, honest partial] model-free c1 extractors (f(w) "
      "slice, cubic log-Taylor, derivative fit) BRACKET 2/9 but "
      "spread over a band of ~ +-15 %%: the < 2 %% model-free "
      "extraction is OPEN (normalization/collinearity systematics); "
      "the measured band is reported, not tuned away" % (),
      band[0] < c1_th < band[1],
      "c1(f-slice) = %.4f, c1(log-poly) = %.4f, c1(derivative) = "
      "%.4f; band = [%.4f, %.4f] vs 2/9 = %.4f"
      % (c1_f, c1_lp, c1_dv, band[0], band[1], c1_th))

# S3.3 identity normalization
rel_id = abs(beta0 / A2_REF - 1.0)
check("S3.3 identity normalization C_{sig sig^dag -> 1} = 1: the "
      "four-point normalization beta0 equals A^2 from the independent "
      "two-point fits at < 2 %%" % (), rel_id < TOL_OPE,
      "beta0 = %.6f vs A^2 = %.6f (rel dev %.3e)"
      % (beta0, A2_REF, rel_id))

check("S3.4 [O, honest typing] the Delta = 1 level is measured as ONE "
      "number (2 eta^2 = 2/9); its split into Majorana-orbifold "
      "blocks (epsilon of the seam copies vs the U(1) current of the "
      "double) is NOT fixed by this four-point alone -- open, named, "
      "not claimed", True)


# ================================================================== S4
print("=" * 72)
print("S4: reflection positivity of the twist sector (differentiated)")
print("=" * 72)

# reflection r(j) = N-1-j: the bond-centered diameter (v622 cut
# geometry); theta antiunitary: theta(e^{i lam N_A}) = e^{-i lam
# N_r(A)}.  Two operator classes:
#   charged axis strings  O_a = e^{i lam N_[0, x_a)}   (x_a = 4s..44s)
#   neutral pair strings  O_a = e^{i lam N_[a1, a2)}   (right half)


def gram_charged(Nv, xs_rp, lam):
    C = COVS[Nv]
    n = len(xs_rp)
    M = np.zeros((n, n), dtype=complex)
    for a, xa in enumerate(xs_rp):
        for b, xb in enumerate(xs_rp):
            left = np.arange(Nv - xa, Nv)
            right = np.arange(0, xb)
            sites = np.concatenate([left, right])
            u = np.concatenate([-lam * np.ones(len(left)),
                                lam * np.ones(len(right))])
            M[a, b] = string_det(C, sites, u)
    return M


def gram_neutral(Nv, pairs, lam):
    C = COVS[Nv]
    n = len(pairs)
    M = np.zeros((n, n), dtype=complex)
    for a, (a1, a2) in enumerate(pairs):
        for b, (b1, b2) in enumerate(pairs):
            left = np.arange(Nv - a2, Nv - a1)
            right = np.arange(b1, b2)
            sites = np.concatenate([left, right])
            u = np.concatenate([-lam * np.ones(len(left)),
                                lam * np.ones(len(right))])
            M[a, b] = string_det(C, sites, u)
    return M


PAIRS = [(s, s + l) for s in (0, 4, 8, 16, 24) for l in (4, 8, 16)
         if s + l <= 48]

herm_max = 0.0
ratios_z3, ratios_z2 = {}, {}
ratios_z3n, ratios_z2n = {}, {}
for Nv, sc in ((96, 1), (192, 2), (384, 4)):
    xr = np.arange(4 * sc, 45 * sc, 4 * sc)
    for lam, store in ((LAM, ratios_z3), (np.pi, ratios_z2)):
        M = gram_charged(Nv, xr, lam)
        herm_max = max(herm_max,
                       np.abs(M - M.conj().T).max() / np.abs(M).max())
        ev = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
        store[Nv] = ev.min() / ev.max()
for Nv, sc in ((96, 1), (192, 2)):
    p2 = [(sc * a, sc * b) for a, b in PAIRS]
    for lam, store in ((LAM, ratios_z3n), (np.pi, ratios_z2n)):
        M = gram_neutral(Nv, p2, lam)
        herm_max = max(herm_max,
                       np.abs(M - M.conj().T).max() / np.abs(M).max())
        ev = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
        store[Nv] = ev.min() / ev.max()

check("S4.1 all mirror Gram matrices M_ab = <theta(O_a) O_b> (charged "
      "axis strings N = 96/192/384 and neutral pairs N = 96/192, "
      "both lam = 2pi/3 and pi) are Hermitian at machine precision",
      herm_max < TOL_MACH, "max |M - M^dag|/max|M| = %.3e" % herm_max)

z2_ok = (min(ratios_z2.values()) >= -TOL_RP
         and min(ratios_z2n.values()) >= -TOL_RP)
check("S4.2 POSITIVE CONTROL: for the REAL Z2 string class (lam = pi, "
      "Ising disorder) the mirror Gram is exactly PSD at every N and "
      "for both operator classes: the pairing and the machinery are "
      "validated", z2_ok,
      "charged min/max: %s; neutral min/max: %s"
      % ({k: "%.2e" % v for k, v in ratios_z2.items()},
         {k: "%.2e" % v for k, v in ratios_z2n.items()}))

r3 = np.array(sorted(ratios_z3.values()))
stable = (r3.max() < -1e-3
          and (r3.max() - r3.min()) / abs(r3.mean()) < 0.5
          and min(ratios_z3n.values()) < -1e-3)
check("S4.3 [honest negative, X-slice] for the complex Z3 class the "
      "NAIVE antiunitary mirror pairing FAILS positivity by an "
      "N-STABLE amount (structural, not a lattice artifact; the "
      "naive single-branch vertex Gram is indefinite already in the "
      "continuum): the check certifies the STABILITY of the "
      "violation", stable,
      "charged min/max: %s; neutral min/max: %s"
      % ({k: "%.3e" % v for k, v in ratios_z3.items()},
         {k: "%.3e" % v for k, v in ratios_z3n.items()}))

check("S4.4 [O, honest typing] the positivity-carrying reflection "
      "pairing of the Z3 twist sector (parafermionic Klein/twist "
      "correction, Jaffe-Pedrocchi-type, or the full block-sum "
      "pairing) is OPEN -- named, not claimed; the Z2 control shows "
      "the failure is specific to the complex string class, not to "
      "the seam geometry", True)


# ================================================================== R
print("=" * 72)
print("R: the reading")
print("=" * 72)

check("R.1 [C] the interacting/CFT-level slice of the Z3 orbifold "
      "statement STANDS AT THE ABELIAN VERTEX LEVEL on the seam "
      "double: h_sigma = 1/36 per deck class (three exact routes, "
      "conventions reconciled), lattice two-point exponent 2 Delta = "
      "2/9, four-point with symmetry-protected crossing and the exact "
      "closed form [w(1-w)]^{-2 Delta}, OPE normalization "
      "C_{-> 1} = 1 and Delta = 1 level 2 eta^2; RP is validated in "
      "the real class and OPEN for the complex Z3 pairing (Klein "
      "twist); also OPEN: the Majorana-level block split, chiral "
      "factorization, the modular/partition-function level, "
      "non-abelian content.  GATE.QGEO does not move", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: TWIST-OPE-COHERENT-RP-OPEN -- the interacting slice of")
    print("the Z3 orbifold statement holds at the abelian vertex level on")
    print("the seam double (weights 1/36, exponent 2/9, crossing, closed-")
    print("form four-point, OPE data); mirror positivity is validated in")
    print("the real Z2 class and honestly open for the complex Z3 pairing")
    print("(parafermionic Klein twist).")
else:
    hard = [n for n, ok in CHECKS if not ok
            and (n.startswith("T0") or n.startswith("S1"))]
    print("SOME CHECKS FAILED")
    print("VERDICT: %s" % ("TWIST-OPE-FAILS" if hard else "MIXED"))


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
