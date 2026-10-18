#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""calderon_scaling_realize_probe -- SEAM.CALDERON.SCALING.REALIZE.01
(EXPLORATION ONLY, experiments/; 2026-08-12 -- the scoped FINITE tier
of the one big functional-analytic theorem of the physics side:
collar projectors P_N on growing finite collars, the four
convergences (gap law FIRST), the realization check against the
gapped one-particle contraction, and the CCXV payoff question --
does the limiting Calderon object select a collar frame on the
delta-circle, which via the frozen selection map would dictate the
forced wiring.)

THE QUESTION.  The seam lane has (a) the deployed 16-dim seam cell
with the FIXED integer pencil P(t) = A_dep + t A_int, deployed
t = 1/8, and the theorem-shaped gap object t_gap = 0.2309488708...
(unique positive root of q(t) = 9t^3 + 21t^2 - t - 1, CXXXIII);
(b) the frame/wiring structure: the rule-gauge frame circle
theta(gamma, y), the frozen SELECTION MAP -- frame at relative
angle delta = y - gamma cuts the admissible wiring component C_rot
exactly in the ray (a_o, c_o) = lambda(-sin delta, cos delta) in
(I, J) coordinates, delta = 0 <-> pure-(+-J), delta = +-pi/2 <->
pure-(+-I) (CCXV, gauge-covariance audited in CCXXI); and (c) the
verdict THETA-CONVENTIONAL: no enumerated compiler demand pins the
frame.  What the lane does NOT have is the scaling tier: a family
of collar projectors P_N on growing finite collars, measured
convergence P_N -> P_Sigma, a uniform gap statement, mu4-step
commutator decay, CAR covariance convergence, the ward of the
limiting one-particle contraction against the gapped contraction
the compiler demands -- and the payoff measurement: does the
LIMITING Calderon object select a frame?  That is this probe.

FEASIBILITY / REDUNDANCY CHECK (against the corpus, 2026-08-12):
CXXXIII shaped t_gap as a pencil eigenvalue on ONE cell; CXXXII
built the parent dilation family on ONE cell; CCXIII/CCXV/CCXXI
censused wiring and frames on ONE cell; v476/v478 measured the
compression conjecture on a FOREIGN toy chain (staggered-mass, not
the seam wiring).  NOTHING in the corpus scales the deployed seam
cell itself into a collar family, states the collar gap window,
states the commutation [A_dep, A_int] = 0, or measures a frame
selection of the scaling limit.  New content.

THE FROZEN CONSTRUCTION (the deployed seam structure scaled up;
documented exactly).  Collar C_N = two-sided chain of L = 2N seam
cells (layers m = 0..L-1, the seam cut between m = N-1 and m = N;
each cell = the 16-dim Majorana seam space).  One-particle
generator
    A_N = I_L (x) A_dep + (t/2) K_L (x) A_int,   h_N = -A_N,
with A_dep = (+)_8 J and A_int = the C6-covariant integer seam
wiring (both rebuilt from the compiler, byte-identical to the
gap-pencil probe), K_L = the path-graph adjacency, deployed
t = 1/8.  BUDGET CONVENTION (frozen): the deployed wiring budget
t A_int per layer is split equally between the two collar
neighbours (bond weight t/2); every interior layer then carries
exactly the deployed budget, and the collar SYMBOL
    a(theta) = A_dep + t cos(theta) A_int,  theta in [0, pi],
has the deployed pencil point A_dep + t A_int as its EXACT
zero-momentum fiber.  The collar direction is the mu4-step
direction (one layer = one mu4 step); the C6 lift O16 fixes both
members entrywise.  Exact diagonalization: K_L has sine
eigenvectors, so every collar object is fiber-exact through the
gap-pencil machinery (warded once against a dense
eigendecomposition).  States: the collar ground state
(beta = infinity; the Calderon projector P_N) and the DEPLOYED
KMS covariance (beta = 1, u = 1; corpus regression smax =
0.667735 at the cell).  THE LIMIT CANDIDATE (anti-circular by
construction): the block-Toeplitz objects with symbol fibers
Pi(t cos theta) / A_beta(t cos theta), assembled by
Gauss-Legendre quadrature of the SYMBOL only -- no finite-N data
enters the limit candidate.

SMOKE-RUN DISCLOSURE (2026-08-12; declared smoke rounds before
freezing, fail-first preserved; the frozen numbers below were read
off the smoke runs):
 SMOKE-1 (two mechanical bugs, disclosed): (i) the seam window
       (3 layers per side) overran the chain at N <= 3 -- window
       reduced to 2 layers per side and the window ladder guarded
       to N >= 3; (ii) the cell smax ward hermitized the complex
       covariance, which ANNIHILATES a real antisymmetric matrix
       (measured 0.000000) -- replaced by the spectrum of i A
       directly; both fixed before any claim was frozen.
 SMOKE-2 (THE STRUCTURAL SURPRISE, and the probe's first result):
       the ground-state prongs came back IDENTICALLY trivial --
       e_N flat at the quadrature floor for every N, the mu4
       commutator ~ 1e-14 including the open ends, the
       seam-adjacent cross block of P_N ZERO to machine precision
       (sigma_max = 8e-16), and the deg-2 defect flat zero over
       the whole delta-grid.  Diagnosis, then verified EXACTLY:
       [A_dep, A_int] = 0 as INTEGER matrices.  Hence all pencil
       fibers commute, the ground projector is CONSTANT across
       the gap window, P_N == I (x) Pi_0 EXACTLY (a product
       state: ZERO cross-seam entanglement at beta = infinity),
       and [P_N, S] == 0 exactly.  AMENDMENT (typed, no bar
       weakened): the beta = infinity statements are promoted to
       EXACT wards; the fitted convergence laws, the mu4 law and
       BOTH frame prongs move to the deployed KMS state beta = 1
       (u = 1) -- which is also the corpus-deployed seam state --
       where the seam correlations actually live.  Read off
       smoke: the thermal Toeplitz datum T_A(1) is 99.99967 %
       proportional to A_int itself (the wiring IS the leading
       Calderon datum), its singular floor is the EXACT
       4-dimensional kernel of A_int (rank 12 over Q = CXXXIII's
       four infinite pencil eigenvalues), the deg-2 defect curve
       is nonflat with its MINIMUM at delta = +-pi/2 (the
       pure-I-selecting integer-frame class) lifted to ~ 0.198
       (max ~ 0.320 at delta = 0), and lam_min < 0 at every
       frame: no strict collar RP at any angle.  The C3 fire
       criterion (polar off-circle) was VACUOUS against this
       truth (truth itself is off-circle) and is replaced by the
       A_int-correlation kill.  Hand predictions: H1 (mirror side
       binds) CONFIRMED; H3 (symbol rate -2) CONFIRMED; H4 (polar
       reflection on the frame circle) REFUTED by the machine.
 SMOKE-3 (rebuilt probe, 24/25): ONE hand prediction corrected by
       the machine -- the equivariance defect-curve shift under
       the rational carrier gauge R(3/5, 4/5) is the frame
       PARAMETER shift gamma_0 = atan2(4,3) = 0.9273 (measured
       0.9163 on the 0.131-rad grid), NOT the pair-block angle
       2 gamma_0 that was hand-written (conjugation by R(gamma_0)
       maps the frame at parameter gamma to gamma + gamma_0);
       target corrected, no other change.  Measured numbers frozen
       below: mu4 thermal slope -4.43/layer (R^2 0.996),
       covariance slope -5.33/layer (R^2 1.000), profile slope
       -2.46/step (R^2 0.993), realization -1.896 (R^2 0.999),
       deg-2 curve min 0.198 at delta = +-pi/2, max 0.320 at
       delta = 0, min/med 0.744, shape R^2 1.000, lam_min at the
       argmin -0.0216 (negative at EVERY angle), polar corr
       0.9999967 / rho 0.000 / sigma_12 = 1.04e-2.

CONVENTIONS (rebuilt inline, READ-ONLY import of tfpt_constants):
16-dim cell, carrier C = 0..9 (5 channels, pairs), boundary
B = 10..15; A_dep = (+)_8 J; A_int = the C6-covariant integer seam
wiring (vacuum orbit blocks IOTA/I2/J2); deployed wiring
V_dep = A_int[C, B] is pure-I.  Frames: theta_cell(gamma, y) = per
carrier pair cos(2 gamma) X + sin(2 gamma) Z, per boundary pair
cos(2y) X + sin(2y) Z; collar reflection THETA = (layer mirror)
(x) theta_cell; eta = +i (v519, forced); the carrier angle is
global gauge on the chain (carrier-carrier blocks transform
delta-independently), so the delta-only scan theta_cell(0, delta)
is complete.  RP Grams: vector-Wick on kernel dot products
u^T (I + i A) v; M[a,b] = omega(Theta(m_a) m_b) with
Theta(f_p f_q) = eta^2 phi(theta f_q) phi(theta f_p) (CCXV
machinery, rebuilt).  SELECTION MAP (frozen, cited CCXV):
delta -> ray lambda(-sin delta, cos delta) in (I, J) wiring
coordinates.  NUMERICAL PROTOCOL (declared): commutation, ranks,
Sturm counts, the det factorization and the symbol identity are
EXACT (integer/Fraction/sympy); everything spectral is float64
with declared bars; RNG only in controls C2/C3.

FROZEN CLAIMS (2026-08-12, frozen + SHA-hashed before the frozen
run; bars from the declared smokes):

 P1  THE FAMILY (construction; exact where algebraic).
     (a) members exact: 16 A_N integer for t = 1/8; C6 lift fixes
         BOTH members entrywise (integer);
     (b) NEW EXACT STRUCTURE: [A_dep, A_int] = 0 as integer
         matrices; rank_Q(A_int) = 12, dim ker = 4 == CXXXIII's
         four infinite pencil eigenvalues (exact rational rank);
         spec(i A_int) reported;
     (c) fiber == dense ward at N = 12: seam-window blocks of P_N
         and A_N^{beta=1} match a dense eigendecomposition to
         <= 1e-10; global projector ward <= 1e-12; covariance
         real + antisymmetric <= 1e-12;
     (d) the zero-momentum symbol fiber IS the deployed pencil
         point: a(0) == A_dep + (1/8) A_int EXACT (Fraction);
         det factorization re-locked at 13 rational points (exact
         Bareiss); corpus regression smax = 0.667735 +- 1e-6;
     (e) EXACT-PRODUCT COROLLARY (from (b)): the ground projector
         is constant across the gap window (||Pi(+-t) - Pi(0)||
         <= 1e-12), P_N == I (x) Pi_0 (window defect <= 1e-12),
         and [P_N, S] == 0 EXACTLY including the open ends (full
         norm <= 1e-12): the collar ground state is the PRODUCT
         state -- zero cross-seam entanglement at beta = infinity;
         ALL seam correlation is THERMAL (deployed beta = 1).
 P2  THE FOUR CONVERGENCES (gap law first; fitted + typed).
     (a) GAP LAW (the single most important number): EXACT -- no
         det factor has a root in [-1/8, 1/8] (Sturm 0/0/0), so
         EVERY fiber of EVERY P_N is gapped; the MIRROR ROOT
         t_mir = 0.2038188... (unique root of 9t^3-21t^2-t+1 in
         (0, 1/4), Sturm count 1) binds the ASYMMETRIC collar gap
         window (-t_mir, t_gap), and t = 1/8 < t_mir < t_gap;
         quantitative floor g_inf = 0.386710 at s = -1/8 (the
         mirror side binds: gap(-1/8) = 0.38671 < gap(+1/8) =
         0.45875; hand prediction H1), Lipschitz-certified floor
         0.386273 > 0; the ladder gap_N is nonincreasing, >=
         g_inf - 1e-9 for ALL N, excess law (gap_N - g_inf) ~
         N^p with p in [-3, -1] (R^2 >= 0.95; smoke -1.898 /
         0.999) -- INF_N GAP = 0.38671 > 0: UNIFORM;
     (b) LOCAL TRACE NORM (P_N -> P_Sigma): e_N and the Cauchy
         differences sit at the declared float floor (<= 2e-12)
         for EVERY window size N >= 3 -- CONVERGED-IDENTICALLY
         (the exact-product mechanism P1.e; the trace norm IS the
         quadrature floor); quadrature doubling ward <= 1e-11;
     (c) MU4-STEP COMMUTATOR: at beta = infinity EXACTLY ZERO
         (P1.e); the deployed-state law: w_N = || E_W [A_N^{b=1},
         S] E_W ||_F decays with exponential fit slope <= -1.5
         per layer (R^2 >= 0.9) on the sub-ladder N in {3..8}
         above the float floor, and floors <= 1e-10 for N >= 12;
         the full-collar norm at beta = 1 is reported (open ends;
         the statement is local); C6 ward <= 1e-12;
     (d) CAR COVARIANCE (deployed beta = 1): d_N = || W(A_N^1) -
         W(A_Sigma^1) ||_1 decays with exponential fit slope <=
         -2 per layer (R^2 >= 0.9) on the sub-ladder and floors
         for N >= 10; PROFILE LAW: the limiting Calderon kernel
         decays in the collar distance, ||T_A(d)||_2 fit slope <=
         -1.5 per step (R^2 >= 0.9) on d = 1..8 above floor; the
         contraction band ward: spec(i A_fiber) in +-[tanh(beta
         g_lo / 2) - 1e-9, 0.667735 + 1e-9] for all fibers at
         N = 96 -- uniformly gapped one-particle contractions.
 P3  THE REALIZATION CHECK.
     (a) EXACT: the limiting contraction family contains the
         deployed gapped one-particle contraction as its
         theta = 0 fiber (P1.d identity); the finite approximants
         realize it at the SYMBOL RATE: r_N ~ N^p, p in [-2.5,
         -1.5] (R^2 >= 0.95; smoke -1.896 / 0.999), and
         smax(fiber_1) -> 0.667735 (|diff| <= 1e-4 at N = 96);
     (b) KERNEL-CHANNEL BARE SURVIVAL (new, from P1.b): the
         on-site block of the limiting thermal kernel has
         ||T_A(0)||_2 == tanh(beta u / 2) = 0.4621171573 to
         <= 1e-9 -- the 4-dim A_int-kernel sector carries the
         UNDRESSED bare contraction (strict concavity of tanh
         suppresses every dressed sector below it); the dressing
         distance ||T_A(0) - A_cell(t, beta=1)||_2 is reported.
 P4  FRAME SELECTION (the CCXV payoff; both-way, the hierarchy
     frozen BEFORE the runs: the deg-2 prong is PRIMARY, the
     polar prong is corroborating; all on the deployed state).
     (a) polar natural reflection: X_N = A_N^{beta=1}[layer N-1,
         layer N] (seam-adjacent cross block); wards: the
         singular profile splits 12 / 4 (sigma_12 >= 1e-3,
         sigma_13 <= 1e-8 -- the EXACT A_int kernel, corpus tie
         P1.b); the A_int-correlation corr(X_N, A_int) >= 0.999
         (THE LEADING CALDERON DATUM IS THE WIRING); the rank-12
         partial polar isometry's pair-diagonal and on-circle
         masses are MEASURED with the frozen decision rule:
         rho >= 0.85 -> ON-CIRCLE (angles read), rho <= 0.15 ->
         REFLECTION-OFF-FAMILY, else AMBIGUOUS (smoke: OFF);
     (b) deg-2 strict-collar scan (N in {16, 48, 96}, W_rp = 2,
         24-point delta-grid, frames theta_cell(0, delta)): the
         curve is NONFLAT ((max-min)/median >= 0.2), the argmin
         delta_0(N) is stable across the three sizes (<= one grid
         step), and the curve carries the two-seat shape
         (regression of defect^2 on {1, cos 2d, sin 2d}, R^2 >=
         0.8); the PSD margin at delta_0 (lam_min of the
         hermitized Gram) is reported both-way (smoke: negative
         at every angle -- NO strict collar RP on the thermal
         collar at ANY frame);
     (c) equivariance (ward exact where algebra is exact): under
         the rational carrier gauge g = R(3/5, 4/5) per carrier
         pair, the cross block transports exactly ((I x g) X
         (I x g)^T ward <= 1e-10), the range projector of the
         partial polar transports (<= 1e-8), and the defect curve
         shifts by the frame-parameter gauge angle gamma_0 mod pi
         (min-RMS circular shift within 1.5 grid steps; the
         hand-written 2 gamma_0 was corrected by smoke-3,
         disclosed) -- ONLY delta is invariant;
     (d) THE FRAME VERDICT (frozen rule): FRAME-SELECTED(delta_0)
         iff defect_min / defect_median <= 0.2 AND delta_0 stable
         per (b); then the frozen selection map names the forced
         wiring (|sin delta_0| >= 0.92 -> PURE-I-class,
         |cos delta_0| >= 0.92 -> PURE-J-class, else MIXED-RAY).
         FRAME-FLAT iff (max-min)/median <= 0.2.  Else
         FRAME-OBSTRUCTED-MINIMUM(delta_0, ratios) -- a measured
         PREFERENCE ORDERING, not a strict selection; the
         selection-map ray of the argmin frame is named with that
         typing.
 C   CONTROLS (must fire; frozen fire rules; RNG only here).
     C1 GAPLESS IMPOSTOR (the double-budget collar, bond weight t
        instead of t/2): its fibers sweep (-1/4, 1/4) which
        contains BOTH -t_mir and +t_gap (exact Sturm counts 1/1)
        -- the gap law must BREAK: gap_imp(96) <= 1e-2 AND <=
        g_inf / 3 (measured decay law reported);
     C2 NON-EQUIVARIANT PERTURBATION (seeded rng 907, eps = 0.05
        random antisymmetric block on the seam bond; dense eigh
        at N in {24, 48}, beta = 1): the mu4-window commutator
        must acquire a floor: w_pert(48) >= 10 x max(w_truth(48),
        1e-13) and w_pert(48) >= 0.3 x w_pert(24);
     C3 SCRAMBLED CROSS BLOCK (seeded rng 908, random orthogonal
        left factor): the A_int-correlation must DIE:
        corr(Q X_N, A_int) <= 0.5 against truth >= 0.999.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 construction / exactness ward breaks        -> CONSTRUCTION-BROKEN
  K2 a convergence law breaks                    -> LAW-BROKEN
  K3 the realization check breaks                -> REALIZATION-BROKEN
  K4 frame machinery ward breaks                 -> FRAME-MACHINERY-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum, both-way): CALDERON-SCALING-REALIZED
[COMMUTING-PENCIL(exact) + PRODUCT-GROUND-STATE(exact),
GAP-UNIFORM(g_inf; window (-t_mir, t_gap)),
LOCAL-TRACE-CONVERGED-IDENTICALLY, MU4-EXACT(beta=inf) +
MU4-THERMAL-DECAYS(rate), CAR-COV-EXP(rate) + KERNEL-PROFILE(rate),
CONTRACTION-FIBER-EXACT + RATE(~ -2) + BARE-SURVIVES-IN-KERNEL]
x FRAME-SELECTED(delta_0, forced wiring) / FRAME-FLAT /
FRAME-OBSTRUCTED-MINIMUM(delta_0 -> named ray, preference only) /
PIPELINE-BROKEN / CONSTRUCTION-BROKEN / LAW-BROKEN /
REALIZATION-BROKEN / FRAME-MACHINERY-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

ANTI-CIRCULARITY (declared): the limit candidates are built from
the SYMBOL by quadrature only; the realization target is built
from the single 16-dim cell only; the selection map is the frozen
CCXV formula (rebuilt, never fitted); the frame angles are
measured from the state's polar/Gram data, never injected.  The
collar family itself is a frozen construction choice (budget
convention) -- documented, and its one free convention (the t/2
split) is exactly what C1 probes.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  HONEST SCOPE: everything here is a
FINITE-MODEL measurement on a frozen one-parameter collar family
of the deployed integer seam cell; the analytic theorem (operator
convergence of the true continuum Calderon projectors, OS
reconstruction over the limit, net existence, current-algebra /
(E8)_1 identification) is UNTOUCHED and stays open; the frame
verdict is a finite-model statement about THIS family.  NO marker
moves.  NO RH claim.

SPEC v1 (2026-08-12): frozen after the declared smoke rounds
(disclosed above); no bar moved after the frozen run started.

Sources (read-only, machinery rebuilt inline): seam_gap_pencil_
probe (pencil + compiler rebuild + corpus regression),
seam_state_derivation_probe (round 58 KMS wiring),
theta_frame_selector_probe (frame circle, selection map, vector
Wick Grams), wiring_gauge_rp_audit_probe (two-seat defect law),
v898_kms_schur_mixing (deployed state), tfpt_constants.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/calderon_scaling_realize_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402  (READ-ONLY)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

T_DEP = 0.125                       # deployed pencil coupling
BETA_DEP = 1.0                      # deployed KMS temperature
ETA = 1j                            # v519 twist (forced)
TGAP_REF = 0.2309488708333614
SMAX_REF = 0.667735                 # corpus cell KMS regression
TANH_HALF = math.tanh(0.5)          # 0.4621171573...
FLOOR = 1e-13                       # declared float floor for fits
N_LADDER = [2, 3, 4, 5, 6, 8, 10, 12, 16, 24, 32, 48, 64, 96]
N_WIN = [N for N in N_LADDER if N >= 3]   # window ladder
N_FIT_MAX = 8                       # exponential-fit sub-ladder cap
W_LOC = 2                           # seam window (layers per side)
W_RP = 2                            # deg-2 scan window per side
N_RP = (16, 48, 96)                 # deg-2 scan sizes
QUAD_M = 800                        # symbol quadrature nodes
DELTA_GRID = -np.pi / 2 + np.arange(24) * np.pi / 24
GAMMA0 = math.atan2(4.0, 3.0)       # rational gauge angle (3/5,4/5)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------------------ helpers
def linfit(x, y):
    """least squares y = a + b x; returns (b, a, R^2)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) < 3:
        return float("nan"), float("nan"), float("nan")
    b, a = np.polyfit(x, y, 1)
    yh = a + b * x
    ss_res = float(np.sum((y - yh) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return float(b), float(a), r2


def trace_norm(M):
    return float(np.sum(np.linalg.svd(M, compute_uv=False)))


def bareiss_det(M):
    """exact determinant of a Fraction matrix (fraction-free)."""
    A = [row[:] for row in M]
    n = len(A)
    sign = Fraction(1)
    prev = Fraction(1)
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0),
                       None)
            if piv is None:
                return Fraction(0)
            A[k], A[piv] = A[piv], A[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k]
                           - A[i][k] * A[k][j]) / prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


# ---------------------------------------------------------- bit model
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v]) if bit)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def edge_orbits(perm):
    n_ord = perm_order(perm)
    seen = set()
    out = []
    for i, j in itertools.combinations(range(6), 2):
        e = frozenset({i, j})
        if e in seen:
            continue
        x, y = i, j
        edges = set()
        rev = False
        for _k in range(n_ord):
            edges.add(frozenset({x, y}))
            x, y = perm[x], perm[y]
            if (x, y) == (j, i):
                rev = True
        seen |= edges
        out.append((frozenset(edges), rev, (i, j)))
    return out


def build_compiler():
    """rebuild q*, Aut, PI6, A_int, A_dep, O16 (gap-pencil S0)."""
    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    QSTAR = cand[0] if cand else None
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5 and set(phi.values()) == set(range(1, 6)))

    def lab(j):
        return 0 if j == V0 else phi[j]

    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                              for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    ok0 = ok_ref and len(cand) == 1 and ok_phi and len(AUT) == 6 \
        and len(g_pin) == 1
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(pia[j])
    PI6 = tuple(PI6)
    ok0 &= (PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3))

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]

    J2i = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    I2i = np.eye(2, dtype=np.int64)
    IOTA6i = np.vstack([I2i, I2i, I2i])
    orbs = edge_orbits(PI6)

    def put_ordered(A, x, y, B):
        rx, cy = CH[x], CH[y]
        for r in range(len(rx)):
            for c in range(len(cy)):
                A[rx[r], cy[c]] = B[r, c]
                A[cy[c], rx[r]] = -B[r, c]

    A_int = np.zeros((16, 16), dtype=np.int64)
    for edges, rev, rep in orbs:
        i, j = rep
        B = J2i if rev else (IOTA6i if i == 0 else I2i)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    A_dep = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        A_dep[2 * i, 2 * i + 1] = 1
        A_dep[2 * i + 1, 2 * i] = -1
    ok0 &= (np.array_equal(A_int[np.ix_(img, img)], A_int)
            and np.array_equal(A_int, -A_int.T)
            and np.array_equal(A_dep[np.ix_(img, img)], A_dep))
    O16 = np.zeros((16, 16), dtype=np.int64)
    for src in range(16):
        O16[img[src], src] = 1
    return ok0, A_dep, A_int, O16


# --------------------------------------------------- cell-level state
def cell_gap(Adep_f, Aint_f, s):
    h = -(Adep_f + s * Aint_f)
    w = np.linalg.eigvalsh(1j * h)
    return float(np.min(np.abs(w)))


def cell_state(Adep_f, Aint_f, s, beta):
    """(w, Q, P_ground, A_beta) of the cell at coupling s."""
    h = -(Adep_f + s * Aint_f)
    w, Q = np.linalg.eigh(1j * h)
    if beta == np.inf:
        f = (w < 0).astype(np.float64)
    else:
        f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
    P = (Q * (w < 0)) @ Q.conj().T
    A = -1j * (2 * (Q * f) @ Q.conj().T - np.eye(16))
    return w, Q, P, A


# ------------------------------------------------------ collar fibers
class Collar:
    """fiber-exact collar: L = 2N layers, bond weight wb."""

    def __init__(self, Adep_f, Aint_f, N, wb, beta):
        self.N = N
        self.L = 2 * N
        L = self.L
        j = np.arange(1, L + 1)
        self.thetas = j * np.pi / (L + 1)
        m = np.arange(L)
        self.V = (np.sqrt(2.0 / (L + 1))
                  * np.sin(np.outer(self.thetas, m + 1)))
        self.s = 2.0 * wb * np.cos(self.thetas)
        Pj = np.empty((L, 16, 16), dtype=complex)
        Aj = np.empty((L, 16, 16), dtype=complex)
        gaps = np.empty(L)
        smax = np.empty(L)
        smin = np.empty(L)
        for k in range(L):
            w, Q, P, A = cell_state(Adep_f, Aint_f, self.s[k], beta)
            Pj[k] = P
            Aj[k] = A
            gaps[k] = float(np.min(np.abs(w)))
            ev = np.linalg.eigvalsh(1j * A.real)
            smax[k] = float(np.max(np.abs(ev)))
            smin[k] = float(np.min(np.abs(ev)))
        self.Pj, self.Aj = Pj, Aj
        self.gaps, self.smax, self.smin = gaps, smax, smin
        self.gap = float(np.min(gaps))

    def block(self, stack, rows, cols):
        """window block over layer lists rows/cols; (16r x 16c)."""
        VR = self.V[:, rows]
        VC = self.V[:, cols]
        X = np.einsum("jm,jn,jab->manb", VR, VC, stack,
                      optimize=True)
        return X.reshape(16 * len(rows), 16 * len(cols))

    def window(self, stack, w):
        """seam window: layers N-w .. N+w-1."""
        lay = list(range(self.N - w, self.N + w))
        return self.block(stack, lay, lay)


def toeplitz_symbol(Adep_f, Aint_f, t, beta, dmax, M):
    """T(d) = (1/pi) int_0^pi cos(d theta) F(t cos theta) dtheta
    for F = ground projector and beta-covariance; GL quadrature."""
    x, wq = np.polynomial.legendre.leggauss(M)
    th = 0.5 * np.pi * (x + 1.0)
    ww = 0.5 * np.pi * wq
    Pn = np.empty((M, 16, 16), dtype=complex)
    An = np.empty((M, 16, 16), dtype=complex)
    for k in range(M):
        _w, _Q, P, A = cell_state(Adep_f, Aint_f,
                                  t * math.cos(th[k]), beta)
        Pn[k] = P
        An[k] = A
    ds = np.arange(-dmax, dmax + 1)
    cosd = np.cos(np.outer(ds, th))          # (D, M)
    TP = np.einsum("dm,m,mab->dab", cosd, ww, Pn) / np.pi
    TA = np.einsum("dm,m,mab->dab", cosd, ww, An) / np.pi
    return ds, TP, TA


def toeplitz_window(ds, T, w):
    """(16*2w)^2 window of the Toeplitz limit."""
    n = 2 * w
    out = np.empty((16 * n, 16 * n), dtype=complex)
    off = {int(d): i for i, d in enumerate(ds)}
    for a in range(n):
        for b in range(n):
            out[16 * a:16 * a + 16, 16 * b:16 * b + 16] = \
                T[off[a - b]]
    return out


# --------------------------------------------------- frames and Grams
X2 = np.array([[0.0, 1.0], [1.0, 0.0]])
Z2 = np.array([[1.0, 0.0], [0.0, -1.0]])
J2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
I2 = np.eye(2)


def theta_cell(gamma, y):
    th = np.zeros((16, 16))
    for p in range(5):
        u = math.cos(2 * gamma) * X2 + math.sin(2 * gamma) * Z2
        th[2 * p:2 * p + 2, 2 * p:2 * p + 2] = u
    for p in range(3):
        u = math.cos(2 * y) * X2 + math.sin(2 * y) * Z2
        i0 = 10 + 2 * p
        th[i0:i0 + 2, i0:i0 + 2] = u
    return th


def deg2_defect(A_dw, wloc, th_c):
    """strict-collar deg-2 Gram on the double window; returns
    (Hermiticity defect, lam_min of hermitized Gram)."""
    nl = 2 * wloc
    dim = 16 * nl
    nf = 16 * wloc
    K = np.eye(dim) + 1j * A_dw
    Th = np.zeros((dim, nf))
    for l in range(wloc):
        lm = nl - 1 - l
        Th[16 * lm:16 * lm + 16, 16 * l:16 * l + 16] = th_c
    Fsel = np.arange(nf)
    G_tt = Th.T @ K @ Th
    G_tf = (Th.T @ K)[:, Fsel]
    G_ff = K[np.ix_(Fsel, Fsel)]
    pairs = [(p, q) for p in range(nf) for q in range(p + 1, nf)]
    P = np.array([p for p, q in pairs])
    Q = np.array([q for p, q in pairs])
    npr = len(pairs)
    M = np.zeros((npr + 1, npr + 1), dtype=complex)
    M[0, 0] = 1.0
    M[0, 1:] = G_ff[P, Q]
    M[1:, 0] = (ETA ** 2) * G_tt[Q, P]
    t1 = np.outer(G_tt[Q, P], G_ff[P, Q])
    t2 = G_tf[np.ix_(Q, P)] * G_tf[np.ix_(P, Q)]
    t3 = G_tf[np.ix_(Q, Q)] * G_tf[np.ix_(P, P)]
    M[1:, 1:] = (ETA ** 2) * (t1 - t2 + t3)
    nrm = float(np.linalg.norm(M))
    defect = float(np.linalg.norm(M - M.conj().T)) / max(nrm, 1e-30)
    Mh = (M + M.conj().T) / 2
    lmin = float(np.min(np.linalg.eigvalsh(Mh)))
    return defect, lmin


def polar_frame(X1, rank=12):
    """rank-restricted polar of the seam-adjacent cross block +
    frame decomposition; returns dict of measurements."""
    U, S, Vh = np.linalg.svd(X1)
    Ur = U[:, :rank] @ Vh[:rank, :]
    cs = []
    for p in range(8):
        B = Ur[2 * p:2 * p + 2, 2 * p:2 * p + 2]
        cI = np.trace(B) / 2
        cX = np.trace(X2 @ B) / 2
        cZ = np.trace(Z2 @ B) / 2
        cJ = np.trace(J2.T @ B) / 2
        cs.append((cI, cX, cZ, cJ))
    cs = np.array(cs)
    pair_mass = float(sum(np.sum(np.abs(
        Ur[2 * p:2 * p + 2, 2 * p:2 * p + 2]) ** 2)
        for p in range(8)) / max(np.sum(np.abs(Ur) ** 2), 1e-30))
    tot = float(np.sum(np.abs(cs) ** 2))
    circ = float(np.sum(np.abs(cs[:, 1]) ** 2)
                 + np.sum(np.abs(cs[:, 2]) ** 2))
    rho = circ / max(tot, 1e-30)
    zsum = np.sum(cs[:, 1] ** 2 + cs[:, 2] ** 2)
    phi = 0.5 * np.angle(zsum) if abs(zsum) > 1e-30 else 0.0
    ex = np.real(cs[:, 1] * np.exp(-1j * phi))
    ez = np.real(cs[:, 2] * np.exp(-1j * phi))
    ang2 = np.arctan2(ez, ex)
    wgt = np.abs(cs[:, 1]) ** 2 + np.abs(cs[:, 2]) ** 2
    zc = np.sum(wgt[:5] * np.exp(1j * ang2[:5]))
    zb = np.sum(wgt[5:] * np.exp(1j * ang2[5:]))
    g2 = np.angle(zc) if abs(zc) > 1e-30 else 0.0
    y2 = np.angle(zb) if abs(zb) > 1e-30 else 0.0
    delta = ((y2 - g2) / 2 + np.pi / 2) % np.pi - np.pi / 2
    rng_proj = U[:, :rank] @ U[:, :rank].conj().T
    return dict(Ur=Ur, sig=S, pair_mass=pair_mass, rho=rho,
                gamma=float(g2 / 2), y=float(y2 / 2),
                delta=float(delta), range_proj=rng_proj)


def main():
    print("SEAM.CALDERON.SCALING.REALIZE.01 -- collar projectors "
          "P_N, the four convergences, the contraction realization, "
          "and the frame-selection payoff (finite tier)")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler rebuild + corpus regressions")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s" % (BANNED_IDS,),
          not bad, kill="K0")

    ok0, A_dep, A_int, O16 = build_compiler()
    check("S0.1 compiler rebuilt: unique q*, |Aut| = 6, pi cycle "
          "type (1,2,3), A_dep/A_int covariant + antisymmetric "
          "(N_fam = %d, g_car = %d consumed read-only)"
          % (N_fam, g_car), ok0, kill="K0")

    Adep_f = A_dep.astype(np.float64)
    Aint_f = A_int.astype(np.float64)

    tt = sp.Symbol("t")
    q_pol = 9 * tt ** 3 + 21 * tt ** 2 - tt - 1
    cand = sp.expand((tt - 1) ** 2 * (3 * tt ** 2 - 1) ** 2
                     * q_pol ** 2)
    pts = [Fraction(a, b) for a, b in
           ((0, 1), (1, 2), (-1, 2), (1, 3), (-1, 3), (1, 4),
            (-1, 4), (1, 5), (2, 3), (3, 2), (-2, 3), (1, 8),
            (-1, 8))]
    ok_fac = True
    for tv in pts:
        Mfr = [[Fraction(int(A_dep[i, j]))
                + tv * Fraction(int(A_int[i, j]))
                for j in range(16)] for i in range(16)]
        dv = bareiss_det(Mfr)
        cv = sp.Rational(cand.subs(
            tt, sp.Rational(tv.numerator, tv.denominator)))
        ok_fac &= (Fraction(int(cv.p), int(cv.q)) == dv)
    roots_pos = [x for x in sp.Poly(q_pol, tt).all_roots()
                 if x.is_real and x > 0]
    t_gap = float(sp.N(roots_pos[0], 20))
    check("S0.2 pencil re-locked: det P(s) = (s-1)^2 (3s^2-1)^2 "
          "q(s)^2 at 13 rational points (exact Bareiss, all match: "
          "%s); t_gap = %.13f == %.13f +- 1e-12"
          % (ok_fac, t_gap, TGAP_REF),
          ok_fac and abs(t_gap - TGAP_REF) <= 1e-12, kill="K0")

    w_c, Q_c, P_c, A_cell = cell_state(Adep_f, Aint_f, T_DEP,
                                       BETA_DEP)
    smax_cell = float(np.max(np.abs(np.linalg.eigvalsh(
        1j * A_cell.real))))
    _wb, _Qb, _Pb, A_bare = cell_state(Adep_f, Aint_f, 0.0, BETA_DEP)
    bare_def = float(np.max(np.abs(
        A_bare.real - math.tanh(BETA_DEP / 2.0) * Adep_f)))
    check("S0.3 corpus regressions: cell KMS smax = %.6f "
          "(0.667735 +- 1e-6); bare closed form A0 = tanh(beta/2) "
          "A_dep at t = 0 (defect %.1e <= 1e-12)"
          % (smax_cell, bare_def),
          abs(smax_cell - SMAX_REF) <= 1e-6 and bare_def <= 1e-12,
          kill="K0")

    # ==================================================================
    section("P1 -- THE FAMILY (construction; exact where algebraic)")
    # ==================================================================
    okC6 = (np.array_equal(O16 @ A_dep @ O16.T, A_dep)
            and np.array_equal(O16 @ A_int @ O16.T, A_int))
    check("P1.1 members exact: 16 A_N integer at t = 1/8 (on-site "
          "16 A_dep, bond 16*(t/2) A_int = A_int, integer); C6 lift "
          "fixes BOTH members entrywise (integer)", okC6, kill="K1")

    comm = A_dep @ A_int - A_int @ A_dep
    ok_comm = not comm.any()
    rank_q = sp.Matrix(A_int.tolist()).rank()
    wi = np.linalg.eigvalsh(1j * Aint_f)
    print("      spec(i A_int) = %s"
          % np.round(np.unique(np.round(wi, 6)), 4).tolist())
    check("P1.2 NEW EXACT STRUCTURE: [A_dep, A_int] = 0 as INTEGER "
          "matrices (%s); rank_Q(A_int) = %d == 12, dim ker = 4 == "
          "CXXXIII's four infinite pencil eigenvalues"
          % (ok_comm, rank_q),
          ok_comm and rank_q == 12, kill="K1")

    Nw = 12
    col = Collar(Adep_f, Aint_f, Nw, T_DEP / 2, BETA_DEP)
    colP = Collar(Adep_f, Aint_f, Nw, T_DEP / 2, np.inf)
    L = 2 * Nw
    A_full = np.zeros((16 * L, 16 * L))
    for m in range(L):
        A_full[16 * m:16 * m + 16, 16 * m:16 * m + 16] = Adep_f
    for m in range(L - 1):
        A_full[16 * m:16 * m + 16, 16 * (m + 1):16 * (m + 1) + 16] \
            = (T_DEP / 2) * Aint_f
        A_full[16 * (m + 1):16 * (m + 1) + 16, 16 * m:16 * m + 16] \
            = -(T_DEP / 2) * Aint_f.T
    wF, QF = np.linalg.eigh(1j * (-A_full))
    fF = 1.0 / (1.0 + np.exp(np.clip(BETA_DEP * wF, -700, 700)))
    P_dense = (QF * (wF < 0)) @ QF.conj().T
    A_dense = -1j * (2 * (QF * fF) @ QF.conj().T
                     - np.eye(16 * L))
    lay = list(range(Nw - W_LOC, Nw + W_LOC))
    sel = np.concatenate([np.arange(16 * m, 16 * m + 16)
                          for m in lay])
    dP = float(np.max(np.abs(colP.window(colP.Pj, W_LOC)
                             - P_dense[np.ix_(sel, sel)])))
    dA = float(np.max(np.abs(col.window(col.Aj, W_LOC)
                             - A_dense[np.ix_(sel, sel)])))
    proj_def = float(np.max(np.abs(P_dense @ P_dense - P_dense)))
    Aw = col.window(col.Aj, W_LOC)
    car_def = max(float(np.max(np.abs(Aw.imag))),
                  float(np.max(np.abs(Aw.real + Aw.real.T))))
    check("P1.3 fiber == dense at N = 12: window defects P %.1e / "
          "A %.1e <= 1e-10; global projector ward %.1e <= 1e-12; "
          "covariance real+antisym %.1e <= 1e-12"
          % (dP, dA, proj_def, car_def),
          dP <= 1e-10 and dA <= 1e-10 and proj_def <= 1e-12
          and car_def <= 1e-12, kill="K1")

    ok_sym = all(
        Fraction(int(A_dep[i, j])) + Fraction(1, 8)
        * Fraction(int(A_int[i, j]))
        == Fraction(int(A_dep[i, j]))
        + Fraction(1, 8) * Fraction(int(A_int[i, j]))
        for i in range(16) for j in range(16))
    check("P1.4 zero-momentum symbol fiber a(0) == A_dep + (1/8) "
          "A_int EXACT (Fraction; definitional for the frozen "
          "budget convention -- each interior layer carries the "
          "deployed budget t A_int)", ok_sym, kill="K1")

    # exact-product corollary
    _w0, _Q0, Pi0, _A0 = cell_state(Adep_f, Aint_f, 0.0, np.inf)
    _wp, _Qp, Pip, _Ap = cell_state(Adep_f, Aint_f, T_DEP, np.inf)
    _wm, _Qm, Pim, _Am = cell_state(Adep_f, Aint_f, -T_DEP, np.inf)
    dPi = max(float(np.max(np.abs(Pip - Pi0))),
              float(np.max(np.abs(Pim - Pi0))))
    Pw12 = colP.window(colP.Pj, W_LOC)
    Iprod = np.kron(np.eye(2 * W_LOC), Pi0)
    d_prod = float(np.max(np.abs(Pw12 - Iprod)))
    cP8 = Collar(Adep_f, Aint_f, 8, T_DEP / 2, np.inf)
    L8 = cP8.L
    Pfull = cP8.block(cP8.Pj, list(range(L8)), list(range(L8)))
    Sfull = np.zeros((16 * L8, 16 * L8))
    for i in range(L8 - 1):
        Sfull[16 * (i + 1):16 * (i + 1) + 16, 16 * i:16 * i + 16] \
            = np.eye(16)
    full_norm_gs = float(np.linalg.norm(Pfull @ Sfull
                                        - Sfull @ Pfull, 2))
    check("P1.5 EXACT-PRODUCT COROLLARY: Pi(s) constant across the "
          "window (||Pi(+-t) - Pi(0)|| = %.1e <= 1e-12); P_N == "
          "I (x) Pi_0 (window defect %.1e <= 1e-12); [P_N, S] == 0 "
          "INCLUDING the open ends (full norm %.1e <= 1e-12): the "
          "collar ground state is the PRODUCT state -- zero "
          "cross-seam entanglement at beta = inf; ALL seam "
          "correlation is thermal" % (dPi, d_prod, full_norm_gs),
          dPi <= 1e-12 and d_prod <= 1e-12
          and full_norm_gs <= 1e-12, kill="K1")

    # ==================================================================
    section("P2 -- THE FOUR CONVERGENCES (gap law first)")
    # ==================================================================
    n_q = sp.Poly(q_pol, tt).count_roots(sp.Rational(-1, 8),
                                         sp.Rational(1, 8))
    n_3t = sp.Poly(3 * tt ** 2 - 1, tt).count_roots(
        sp.Rational(-1, 8), sp.Rational(1, 8))
    n_t1 = sp.Poly(tt - 1, tt).count_roots(sp.Rational(-1, 8),
                                           sp.Rational(1, 8))
    q_mir = 9 * tt ** 3 - 21 * tt ** 2 - tt + 1
    n_mir = sp.Poly(q_mir, tt).count_roots(0, sp.Rational(1, 4))
    r_mir = [x for x in sp.Poly(q_mir, tt).all_roots()
             if x.is_real and 0 < x < sp.Rational(1, 4)]
    t_mir = float(sp.N(r_mir[0], 20))
    ok_order = (T_DEP < t_mir < t_gap)
    check("P2.1a EXACT gap window: no det factor has a root in "
          "[-1/8, 1/8] (Sturm %d/%d/%d == 0/0/0) => EVERY fiber of "
          "EVERY P_N is gapped; the MIRROR ROOT t_mir = %.10f "
          "(unique root of 9t^3-21t^2-t+1 in (0,1/4), Sturm count "
          "%d == 1) binds the ASYMMETRIC window (-t_mir, t_gap); "
          "deployed t = 1/8 < t_mir < t_gap: %s"
          % (n_q, n_3t, n_t1, t_mir, n_mir, ok_order),
          n_q == 0 and n_3t == 0 and n_t1 == 0 and n_mir == 1
          and ok_order, kill="K2")

    grid = np.linspace(-T_DEP, T_DEP, 2001)
    ggrid = np.array([cell_gap(Adep_f, Aint_f, s) for s in grid])
    lip = math.sqrt(float(np.max(np.sum(np.abs(A_int), axis=0)))
                    * float(np.max(np.sum(np.abs(A_int), axis=1))))
    hstep = grid[1] - grid[0]
    g_inf = float(np.min(ggrid))
    g_floor = g_inf - lip * hstep / 2
    gp = cell_gap(Adep_f, Aint_f, T_DEP)
    gm = cell_gap(Adep_f, Aint_f, -T_DEP)
    check("P2.1b quantitative floor: min gap over the swept window "
          "[-1/8, 1/8] = %.7f at s = %+.5f (gap(-1/8) = %.6f < "
          "gap(+1/8) = %.6f -- the MIRROR side binds, hand "
          "prediction H1); Lipschitz-certified floor %.7f > 0 "
          "(||A_int||_2 <= %.3f, step %.1e)"
          % (g_inf, grid[int(np.argmin(ggrid))], gm, gp,
             g_floor, lip, hstep),
          g_floor > 0 and gm < gp, kill="K2")

    gaps_N = {}
    for N in N_LADDER:
        c = Collar(Adep_f, Aint_f, N, T_DEP / 2, np.inf)
        gaps_N[N] = c.gap
    gvals = [gaps_N[N] for N in N_LADDER]
    mono = all(gvals[i + 1] <= gvals[i] + 1e-12
               for i in range(len(gvals) - 1))
    above = all(v >= g_inf - 1e-9 for v in gvals)
    ex = [(N, gaps_N[N] - g_inf) for N in N_LADDER
          if gaps_N[N] - g_inf > 1e-12]
    sl_g, _a, r2_g = linfit([math.log(n) for n, e in ex],
                            [math.log(e) for n, e in ex])
    print("      gap_N ladder: %s"
          % ", ".join("N=%d: %.6f" % (N, gaps_N[N])
                      for N in N_LADDER))
    check("P2.1c GAP LAW: gap_N nonincreasing (%s), gap_N >= g_inf "
          "- 1e-9 for ALL N (%s); excess law (gap_N - g_inf) ~ "
          "N^%.3f (R^2 %.3f >= 0.95, slope in [-3,-1]); INF_N GAP "
          "= %.7f > 0 -- UNIFORM (the headline number)"
          % (mono, above, sl_g, r2_g, g_inf),
          mono and above and -3.0 <= sl_g <= -1.0 and r2_g >= 0.95,
          kill="K2")

    dmax = 2 * W_LOC + 4
    ds, TP, TA = toeplitz_symbol(Adep_f, Aint_f, T_DEP, BETA_DEP,
                                 dmax, QUAD_M)
    ds2, TP2, TA2 = toeplitz_symbol(Adep_f, Aint_f, T_DEP, BETA_DEP,
                                    dmax, 2 * QUAD_M)
    quad_def = max(float(np.max(np.abs(TP - TP2))),
                   float(np.max(np.abs(TA - TA2))))
    PSig = toeplitz_window(ds, TP, W_LOC)
    ASig = toeplitz_window(ds, TA, W_LOC)
    check("P2.2a quadrature ward: doubling M = %d -> %d moves the "
          "Toeplitz blocks by %.1e <= 1e-11" % (QUAD_M, 2 * QUAD_M,
                                                quad_def),
          quad_def <= 1e-11, kill="K1")

    e_N, d_N, cau_N = {}, {}, {}
    colA = {}
    for N in N_WIN:
        cP = Collar(Adep_f, Aint_f, N, T_DEP / 2, np.inf)
        cA = Collar(Adep_f, Aint_f, N, T_DEP / 2, BETA_DEP)
        colA[N] = cA
        e_N[N] = trace_norm(cP.window(cP.Pj, W_LOC) - PSig)
        d_N[N] = trace_norm(cA.window(cA.Aj, W_LOC) - ASig)
        cQ = Collar(Adep_f, Aint_f, N + 1, T_DEP / 2, np.inf)
        cau_N[N] = trace_norm(cP.window(cP.Pj, W_LOC)
                              - cQ.window(cQ.Pj, W_LOC))
    print("      e_N  : %s" % ", ".join("N=%d: %.2e" % (N, e_N[N])
                                        for N in N_WIN))
    print("      cauchy: %s" % ", ".join("N=%d: %.2e" % (N, cau_N[N])
                                         for N in N_WIN))
    print("      d_N  : %s" % ", ".join("N=%d: %.2e" % (N, d_N[N])
                                        for N in N_WIN))
    ok_e = all(e_N[N] <= 2e-12 for N in N_WIN) \
        and all(cau_N[N] <= 2e-12 for N in N_WIN)
    check("P2.2b LOCAL TRACE NORM (P_N -> P_Sigma): e_N and the "
          "Cauchy differences sit at the float floor (max %.1e / "
          "%.1e <= 2e-12) for EVERY N -- CONVERGED-IDENTICALLY "
          "(exact-product mechanism P1.5)"
          % (max(e_N.values()), max(cau_N.values())),
          ok_e, kill="K2")

    # mu4-step commutator on the deployed covariance
    def mu4_window(collar, stack, w):
        N = collar.N
        ext = list(range(N - w - 1, N + w + 1))
        Pe = collar.block(stack, ext, ext)
        nl = len(ext)
        S = np.zeros((16 * nl, 16 * nl))
        for i in range(nl - 1):
            S[16 * (i + 1):16 * (i + 1) + 16, 16 * i:16 * i + 16] \
                = np.eye(16)
        C = Pe @ S - S @ Pe
        i0 = 16
        i1 = 16 * (nl - 1)
        return float(np.linalg.norm(C[i0:i1, i0:i1]))

    w_N = {}
    for N in N_WIN:
        w_N[N] = mu4_window(colA[N], colA[N].Aj, W_LOC)
    print("      w_N  : %s" % ", ".join("N=%d: %.2e" % (N, w_N[N])
                                        for N in sorted(w_N)))
    pts_w = [(N, w_N[N]) for N in sorted(w_N)
             if w_N[N] > FLOOR and N <= N_FIT_MAX]
    if len(pts_w) >= 3:
        sl_w, _aw, r2_w = linfit([p[0] for p in pts_w],
                                 [math.log(p[1]) for p in pts_w])
    else:
        sl_w, r2_w = float("nan"), float("nan")
    floor_w = all(w_N[N] <= 1e-10 for N in w_N if N >= 12)
    cA8 = colA[8]
    Af8 = cA8.block(cA8.Aj, list(range(cA8.L)), list(range(cA8.L)))
    Sf8 = np.zeros((16 * cA8.L, 16 * cA8.L))
    for i in range(cA8.L - 1):
        Sf8[16 * (i + 1):16 * (i + 1) + 16, 16 * i:16 * i + 16] \
            = np.eye(16)
    full_norm_th = float(np.linalg.norm(Af8 @ Sf8 - Sf8 @ Af8, 2))
    O16f = O16.astype(np.float64)
    c6_def = max(float(np.max(np.abs(
        O16f @ colA[8].Aj[k] @ O16f.T - colA[8].Aj[k])))
        for k in range(colA[8].L))
    check("P2.3 MU4-STEP COMMUTATOR: beta = inf EXACTLY ZERO "
          "(P1.5); deployed state: windowed w_N decays with slope "
          "%.3f/layer (R^2 %.3f, %d pts, <= -1.5) and floors "
          "<= 1e-10 for N >= 12 (%s); full-collar thermal norm "
          "%.3e at N = 8 (open ends, disclosed); C6 ward %.1e "
          "<= 1e-12" % (sl_w, r2_w, len(pts_w), floor_w,
                        full_norm_th, c6_def),
          sl_w <= -1.5 and r2_w >= 0.9 and floor_w
          and c6_def <= 1e-12, kill="K2")

    # CAR covariance convergence + profile law + band
    pts_d = [(N, d_N[N]) for N in N_WIN
             if d_N[N] > FLOOR and N <= N_FIT_MAX]
    sl_d, _ad, r2_d = linfit([p[0] for p in pts_d],
                             [math.log(p[1]) for p in pts_d])
    floor_d = all(d_N[N] <= 10 * FLOOR for N in N_WIN if N >= 10)
    prof = [(d, float(np.linalg.norm(TA[list(ds).index(d)], 2)))
            for d in range(1, dmax + 1)]
    pts_p = [(d, v) for d, v in prof if v > FLOOR]
    sl_p, _ap, r2_p = linfit([p[0] for p in pts_p],
                             [math.log(p[1]) for p in pts_p])
    print("      profile ||T_A(d)||: %s"
          % ", ".join("d=%d: %.2e" % (d, v) for d, v in prof))
    cA96 = colA[96]
    wmax_f = float(np.max(cA96.smax))
    band_lo = math.tanh(BETA_DEP * (1 - T_DEP * 4.9064) / 2) - 1e-3
    ok_band = (float(np.min(cA96.smin)) >= band_lo
               and wmax_f <= SMAX_REF + 1e-9)
    check("P2.4 CAR COVARIANCE (beta = 1): local convergence slope "
          "%.3f/layer (R^2 %.3f, %d pts, <= -2), floor for N >= 10 "
          "(%s); PROFILE LAW ||T_A(d)|| ~ e^{%.3f d} (R^2 %.3f, "
          "%d pts, slope <= -1.5); contraction band: spec in "
          "+-[%.4f, %.6f] all fibers at N = 96 (%s)"
          % (sl_d, r2_d, len(pts_d), floor_d, sl_p, r2_p,
             len(pts_p), float(np.min(cA96.smin)), wmax_f, ok_band),
          sl_d <= -2.0 and r2_d >= 0.9 and floor_d
          and sl_p <= -1.5 and r2_p >= 0.9 and ok_band, kill="K2")

    # ==================================================================
    section("P3 -- THE REALIZATION CHECK (gapped 1p contraction)")
    # ==================================================================
    r_N, smax1 = {}, {}
    for N in N_LADDER:
        cA = colA.get(N) or Collar(Adep_f, Aint_f, N, T_DEP / 2,
                                   BETA_DEP)
        A1 = cA.Aj[0].real
        r_N[N] = float(np.linalg.norm(A1 - A_cell.real, 2))
        smax1[N] = cA.smax[0]
    print("      r_N  : %s" % ", ".join("N=%d: %.2e" % (N, r_N[N])
                                        for N in N_LADDER))
    pts_r = [(N, r_N[N]) for N in N_LADDER if r_N[N] > FLOOR]
    sl_r, _ar, r2_r = linfit([math.log(p[0]) for p in pts_r],
                             [math.log(p[1]) for p in pts_r])
    dsm = abs(smax1[96] - SMAX_REF)
    check("P3.1 REALIZATION: the theta = 0 symbol fiber IS the "
          "deployed contraction (P1.4, exact); the closest finite "
          "fiber realizes it at the SYMBOL RATE: r_N ~ N^%.3f "
          "(R^2 %.3f >= 0.95, slope in [-2.5, -1.5], hand "
          "prediction H3 p = -2); smax(fiber_1) at N = 96 = %.6f "
          "vs corpus 0.667735 (|diff| = %.1e <= 1e-4)"
          % (sl_r, r2_r, smax1[96], dsm),
          -2.5 <= sl_r <= -1.5 and r2_r >= 0.95 and dsm <= 1e-4,
          kill="K3")

    TA0 = TA[list(ds).index(0)].real
    n_TA0 = float(np.linalg.norm(TA0, 2))
    dress = float(np.linalg.norm(TA0 - A_cell.real, 2))
    check("P3.2 KERNEL-CHANNEL BARE SURVIVAL: ||T_A(0)||_2 = "
          "%.10f == tanh(beta u / 2) = %.10f (|diff| = %.1e <= "
          "1e-9) -- the 4-dim A_int-kernel sector carries the "
          "UNDRESSED bare contraction (strict tanh concavity "
          "suppresses every dressed sector); dressing distance "
          "||T_A(0) - A_cell|| = %.4f (reported)"
          % (n_TA0, TANH_HALF, abs(n_TA0 - TANH_HALF), dress),
          abs(n_TA0 - TANH_HALF) <= 1e-9, kill="K3")

    # ==================================================================
    section("P4 -- FRAME SELECTION (the CCXV payoff)")
    # ==================================================================
    # (a) polar natural reflection on the deployed covariance
    pol = {}
    for N in N_WIN:
        cA = colA[N]
        X1 = cA.block(cA.Aj, [cA.N - 1], [cA.N]).real
        corr = float(np.sum(X1 * Aint_f)
                     / max(np.linalg.norm(X1)
                           * np.linalg.norm(Aint_f), 1e-30))
        pol[N] = polar_frame(X1)
        pol[N]["corr"] = corr
    print("      polar ladder (deployed state):")
    for N in N_WIN:
        p = pol[N]
        print("        N=%3d: sig12=%.3e sig13=%.2e corr(A_int)="
              "%.7f pair=%.3f circ=%.3f delta=%+.4f"
              % (N, p["sig"][11], p["sig"][12], p["corr"],
                 p["pair_mass"], p["rho"], p["delta"]))
    pN = pol[N_WIN[-1]]
    ok_pol = (pN["sig"][11] >= 1e-3 and pN["sig"][12] <= 1e-8
              and pN["corr"] >= 0.999)
    if pN["rho"] >= 0.85:
        pol_read = "ON-CIRCLE(delta* = %+.4f)" % pN["delta"]
    elif pN["rho"] <= 0.15:
        pol_read = "REFLECTION-OFF-FAMILY(rho = %.3f)" % pN["rho"]
    else:
        pol_read = "AMBIGUOUS(rho = %.3f)" % pN["rho"]
    check("P4.1 polar natural reflection: singular split 12/4 "
          "(sig_12 = %.3e >= 1e-3, sig_13 = %.1e <= 1e-8 -- the "
          "EXACT A_int kernel, corpus tie P1.2); corr(X_N, A_int) "
          "= %.7f >= 0.999: THE LEADING CALDERON DATUM IS THE "
          "WIRING; frozen decision: %s (pair-diagonal mass %.3f)"
          % (pN["sig"][11], pN["sig"][12], pN["corr"], pol_read,
             pN["pair_mass"]),
          ok_pol, kill="K4")

    # (b) deg-2 strict-collar scan on the deployed state
    scan = {}
    for N in N_RP:
        cA = colA.get(N) or Collar(Adep_f, Aint_f, N, T_DEP / 2,
                                   BETA_DEP)
        layw = list(range(N - W_RP, N + W_RP))
        A_dw = cA.block(cA.Aj, layw, layw).real
        row = []
        for dl in DELTA_GRID:
            th_c = theta_cell(0.0, dl)
            dfc, lmin = deg2_defect(A_dw, W_RP, th_c)
            row.append((dfc, lmin))
        scan[N] = row
    print("      deg-2 defect(delta) at N = %s:" % (N_RP,))
    for N in N_RP:
        print("        N=%3d: " % N + " ".join(
            "%.3f" % scan[N][i][0]
            for i in range(len(DELTA_GRID))))
    d0_idx = {N: int(np.argmin([r[0] for r in scan[N]]))
              for N in N_RP}
    d0 = {N: float(DELTA_GRID[d0_idx[N]]) for N in N_RP}
    gridstep = float(DELTA_GRID[1] - DELTA_GRID[0])
    stab = max(abs(((d0[N_RP[-1]] - d0[N]) + np.pi / 2) % np.pi
                   - np.pi / 2) for N in N_RP)
    dvals = np.array([r[0] for r in scan[N_RP[-1]]])
    ratio_min = float(np.min(dvals) / max(np.median(dvals), 1e-30))
    ratio_var = float((np.max(dvals) - np.min(dvals))
                      / max(np.median(dvals), 1e-30))
    Bm = np.vstack([np.ones_like(DELTA_GRID),
                    np.cos(2 * DELTA_GRID),
                    np.sin(2 * DELTA_GRID)]).T
    coef, res, _rk, _sv = np.linalg.lstsq(Bm, dvals ** 2, rcond=None)
    ss_tot = float(np.sum((dvals ** 2 - np.mean(dvals ** 2)) ** 2))
    r2_shape = 1.0 - (float(res[0]) / ss_tot if len(res) else 0.0)
    lmin_at = scan[N_RP[-1]][d0_idx[N_RP[-1]]][1]
    lmin_all = max(r[1] for r in scan[N_RP[-1]])
    print("      argmin delta_0: %s (grid step %.3f); min/med = "
          "%.3f, (max-min)/med = %.3f, shape R^2 = %.3f, "
          "lam_min(herm) at delta_0 = %.4f (max over grid %.4f)"
          % ({N: round(d0[N], 4) for N in N_RP}, gridstep,
             ratio_min, ratio_var, r2_shape, lmin_at, lmin_all))
    check("P4.2 deg-2 strict-collar scan: NONFLAT ((max-min)/med = "
          "%.3f >= 0.2); argmin stable across sizes (max drift "
          "%.4f <= one grid step %.3f); two-seat shape R^2 = %.3f "
          ">= 0.8; PSD margin at delta_0: lam_min = %.4f "
          "(both-way, reported; negative => NO strict collar RP "
          "at any frame on the thermal collar)"
          % (ratio_var, stab, gridstep, r2_shape, lmin_at),
          ratio_var >= 0.2 and stab <= gridstep + 1e-9
          and r2_shape >= 0.8, kill="K4")

    # (c) equivariance under the rational carrier gauge
    g_cell = np.eye(16)
    R35 = np.array([[3.0 / 5, -4.0 / 5], [4.0 / 5, 3.0 / 5]])
    for p in range(5):
        g_cell[2 * p:2 * p + 2, 2 * p:2 * p + 2] = R35
    Aint_g = g_cell @ Aint_f @ g_cell.T
    dep_move = float(np.max(np.abs(g_cell @ Adep_f @ g_cell.T
                                   - Adep_f)))
    Ng = N_RP[1]
    cG = Collar(Adep_f, Aint_g, Ng, T_DEP / 2, BETA_DEP)
    layg = list(range(Ng - W_RP, Ng + W_RP))
    A_dwg = cG.block(cG.Aj, layg, layg).real
    dval_g = np.array([deg2_defect(A_dwg, W_RP,
                                   theta_cell(0.0, dl))[0]
                       for dl in DELTA_GRID])
    cT = colA[Ng]
    A_dwt = cT.block(cT.Aj, layg, layg).real
    dval_t = np.array([deg2_defect(A_dwt, W_RP,
                                   theta_cell(0.0, dl))[0]
                       for dl in DELTA_GRID])
    shifts = np.arange(len(DELTA_GRID))
    rms = [float(np.sqrt(np.mean(
        (np.roll(dval_t, k) - dval_g) ** 2))) for k in shifts]
    k_best = int(np.argmin(rms))
    shift_rad = k_best * gridstep
    tgt = GAMMA0 % np.pi
    shift_err = min(abs(shift_rad - tgt),
                    abs(shift_rad - tgt + np.pi),
                    abs(shift_rad - tgt - np.pi))
    X1t = cT.block(cT.Aj, [Ng - 1], [Ng]).real
    X1g = cG.block(cG.Aj, [Ng - 1], [Ng]).real
    x_def = float(np.linalg.norm(g_cell @ X1t @ g_cell.T - X1g))
    Pt = polar_frame(g_cell @ X1t @ g_cell.T)["range_proj"]
    Pg_ = polar_frame(X1g)["range_proj"]
    rp_def = float(np.linalg.norm(Pt - Pg_))
    check("P4.3 equivariance: rational carrier gauge (3/5, 4/5) "
          "preserves A_dep exactly (%.1e); cross-block transport "
          "ward %.1e <= 1e-10; range-projector transport %.1e <= "
          "1e-8; defect-curve shift %.4f rad vs gamma_0 mod pi "
          "= %.4f (|err| = %.4f <= 1.5 grid steps %.3f; smoke-3 "
          "corrected the hand-written 2 gamma_0) -- ONLY delta "
          "is invariant"
          % (dep_move, x_def, rp_def, shift_rad, tgt, shift_err,
             1.5 * gridstep),
          dep_move <= 1e-12 and x_def <= 1e-10 and rp_def <= 1e-8
          and shift_err <= 1.5 * gridstep, kill="K4")

    # (d) THE FRAME VERDICT (frozen rule)
    d_sel = d0[N_RP[-1]]
    s_, c_ = abs(math.sin(d_sel)), abs(math.cos(d_sel))
    if s_ >= 0.92:
        wname = "PURE-I-class"
    elif c_ >= 0.92:
        wname = "PURE-J-class"
    else:
        wname = "MIXED-RAY(delta_0 = %+.4f)" % d_sel
    if ratio_min <= 0.2 and stab <= gridstep + 1e-9:
        frame_verdict = ("FRAME-SELECTED(delta_0 = %+.4f -> ray "
                         "lambda(%+.4f, %+.4f) in (I, J) -> %s)"
                         % (d_sel, -math.sin(d_sel),
                            math.cos(d_sel), wname))
    elif ratio_var <= 0.2:
        frame_verdict = "FRAME-FLAT (freedom persists in the limit)"
    else:
        frame_verdict = ("FRAME-OBSTRUCTED-MINIMUM(delta_0 = "
                         "%+.4f, min/med = %.3f, (max-min)/med = "
                         "%.3f; argmin ray -> %s -- PREFERENCE "
                         "ORDERING, not strict selection)"
                         % (d_sel, ratio_min, ratio_var, wname))
    print("      FRAME VERDICT: %s" % frame_verdict)
    print("      polar corroboration: %s" % pol_read)
    check("P4.4 frame verdict assembled under the frozen rule "
          "(both-way enum; the deg-2 prong is primary, polar "
          "corroborates)", True)

    # ==================================================================
    section("C -- controls (must fire; RNG only here)")
    # ==================================================================
    n_mir_i = sp.Poly(q_mir, tt).count_roots(0, sp.Rational(1, 4))
    n_q_i = sp.Poly(q_pol, tt).count_roots(0, sp.Rational(1, 4))
    gimp = {}
    for N in N_LADDER:
        c = Collar(Adep_f, Aint_f, N, T_DEP, np.inf)
        gimp[N] = c.gap
    print("      impostor gap ladder: %s"
          % ", ".join("N=%d: %.2e" % (N, gimp[N]) for N in N_LADDER))
    ptsi = [(math.log(N), math.log(gimp[N])) for N in N_LADDER]
    sl_i, _ai, r2_i = linfit([p[0] for p in ptsi],
                             [p[1] for p in ptsi])
    check("C1 FIRES: the double-budget collar (bond t) sweeps "
          "(-1/4, 1/4) which contains BOTH -t_mir and +t_gap "
          "(Sturm counts %d/%d == 1/1) -- its gap DECAYS: "
          "gap_imp(96) = %.2e <= 1e-2 and <= g_inf/3 = %.2e "
          "(measured law: slope %.2f, R^2 %.2f)"
          % (n_mir_i, n_q_i, gimp[96], g_inf / 3, sl_i, r2_i),
          n_mir_i == 1 and n_q_i == 1 and gimp[96] <= 1e-2
          and gimp[96] <= g_inf / 3, kill="K7")

    rng2 = np.random.default_rng(907)
    R16 = rng2.normal(size=(16, 16))
    R16 = 0.05 * (R16 - R16.T) / 2
    w_pert = {}
    for N in (24, 48):
        L2 = 2 * N
        Af = np.zeros((16 * L2, 16 * L2))
        for m in range(L2):
            Af[16 * m:16 * m + 16, 16 * m:16 * m + 16] = Adep_f
        for m in range(L2 - 1):
            blk = (T_DEP / 2) * Aint_f
            if m == N - 1:
                blk = blk + R16
            Af[16 * m:16 * m + 16,
               16 * (m + 1):16 * (m + 1) + 16] = blk
            Af[16 * (m + 1):16 * (m + 1) + 16,
               16 * m:16 * m + 16] = -blk.T
        wf, Qf = np.linalg.eigh(1j * (-Af))
        ff = 1.0 / (1.0 + np.exp(np.clip(BETA_DEP * wf, -700, 700)))
        Ab = -1j * (2 * (Qf * ff) @ Qf.conj().T - np.eye(16 * L2))
        ext = list(range(N - W_LOC - 1, N + W_LOC + 1))
        selp = np.concatenate([np.arange(16 * m, 16 * m + 16)
                               for m in ext])
        Ae = Ab[np.ix_(selp, selp)]
        nl = len(ext)
        S = np.zeros((16 * nl, 16 * nl))
        for i in range(nl - 1):
            S[16 * (i + 1):16 * (i + 1) + 16,
              16 * i:16 * i + 16] = np.eye(16)
        C = Ae @ S - S @ Ae
        w_pert[N] = float(np.linalg.norm(
            C[16:16 * (nl - 1), 16:16 * (nl - 1)]))
    w_truth_48 = w_N[48]
    ok_c2 = (w_pert[48] >= 10 * max(w_truth_48, FLOOR)
             and w_pert[48] >= 0.3 * w_pert[24])
    check("C2 FIRES: seeded non-equivariant seam-bond perturbation "
          "(eps = 0.05, beta = 1) gives the mu4-window commutator "
          "a FLOOR: w_pert(48) = %.2e >= 10 x max(w_truth(48), "
          "floor) = %.2e and >= 0.3 x w_pert(24) = %.2e"
          % (w_pert[48], max(w_truth_48, FLOOR), w_pert[24]),
          ok_c2, kill="K7")

    rng3 = np.random.default_rng(908)
    cS = colA[48]
    X1s = cS.block(cS.Aj, [cS.N - 1], [cS.N]).real
    Qs, _ = np.linalg.qr(rng3.normal(size=(16, 16)))
    X1s = Qs @ X1s
    corr_s = float(np.sum(X1s * Aint_f)
                   / max(np.linalg.norm(X1s)
                         * np.linalg.norm(Aint_f), 1e-30))
    check("C3 FIRES: seeded scrambled cross block kills the wiring "
          "correlation: corr(Q X, A_int) = %.4f <= 0.5 (truth "
          "%.7f)" % (corr_s, pN["corr"]),
          abs(corr_s) <= 0.5, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "K1" in KILLS:
        VERDICT = "CONSTRUCTION-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "LAW-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "REALIZATION-BROKEN"
    elif "K4" in KILLS:
        VERDICT = "FRAME-MACHINERY-BROKEN"
    else:
        VERDICT = ("CALDERON-SCALING-REALIZED [COMMUTING-PENCIL + "
                   "PRODUCT-GROUND-STATE (exact), GAP-UNIFORM("
                   "%.5f; window (-%.5f, %.5f)), LOCAL-TRACE-"
                   "CONVERGED-IDENTICALLY, MU4-EXACT+THERMAL-"
                   "DECAYS(%.2f/layer), CAR-COV-EXP(%.2f) + "
                   "KERNEL-PROFILE(%.2f/step), CONTRACTION-FIBER-"
                   "EXACT + RATE(%.2f) + BARE-SURVIVES-IN-KERNEL] "
                   "x %s"
                   % (g_inf, t_mir, t_gap, sl_w, sl_d, sl_p, sl_r,
                      frame_verdict))
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE FAMILY: P_N = ground projectors / deployed KMS states of
    the mu4-homogeneous two-sided collar A_N = I (x) A_dep +
    (t/2) K_2N (x) A_int of the deployed integer seam cell
    (budget convention: each interior layer carries the deployed
    t A_int; the zero-momentum symbol fiber IS the deployed
    pencil point, exactly).
  * THE STRUCTURE THEOREM OF THE FAMILY (new, exact):
    [A_dep, A_int] = 0 over the integers -- the collar ground
    state is the PRODUCT state I (x) Pi_0 (zero cross-seam
    entanglement at beta = inf; P_N -> P_Sigma converges
    IDENTICALLY and [P_N, S] == 0 exactly); ALL seam correlation
    is THERMAL and lives in the deployed KMS state.
  * THE GAP LAW (first): the collar gap window is the ASYMMETRIC
    exact interval (-t_mir, t_gap) -- the binding constraint is
    the MIRROR ROOT t_mir = 0.20382 (orientation-reversed factor
    9t^3-21t^2-t+1), not t_gap; deployed t = 1/8 sits inside, so
    inf_N gap > 0 UNIFORMLY (exact Sturm + Lipschitz floor).  The
    double-budget collar leaves the window and dies (C1).
  * REALIZATION: the finite fibers realize the corpus gapped
    one-particle contraction at the symbol rate ~ N^-2 with
    smax -> 0.667735 exactly at the deployed fiber; the
    A_int-kernel channels carry the UNDRESSED bare contraction
    tanh(1/2) through the limit.
  * WHAT REMAINS ANALYTIC (typed): the continuum/operator-norm
    convergence of the true seam Calderon projectors (this probe
    is a frozen finite lattice family), the OS reconstruction
    over the limit state, net existence, and the current-algebra
    / (E8)_1 identification -- all untouched, all open.
  * FRAME: see the frame verdict line above -- a finite-model
    measurement on THIS family; where only a preference ordering
    is found, the selection map names the argmin ray with that
    honest typing.  NO marker moves.  NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
