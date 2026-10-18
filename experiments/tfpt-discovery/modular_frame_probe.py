#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""modular_frame_probe -- SEAM.STATE.MODULAR.FRAME.01
(EXPLORATION ONLY, experiments/; 2026-08-12 -- decide the frame
question from the physics side: is theta_S (or which frame on the
delta-circle) the ACTUAL modular conjugation J_Omega of the
deployed seam state (Tomita-Takesaki), possibly combined with
sheet grading and collar orientation?)

THE QUESTION.  The wiring question is closed as a compiler-freedom
theorem (CCXIII/CCXV/CCXXI: the compiler fixes the orbit C_rot and
the frame FAMILY; no enumerated internal demand picks a frame; the
frozen selection map: a frame at relative angle delta cuts C_rot in
the ray lambda(-sin delta, cos delta), delta = 0 <-> pure-(+-J),
delta = +-pi/2 <-> pure-(+-I)).  The Calderon probe (CCXXXIII)
measured a PREFERENCE (deg-2 defect argmin at the pure-I-selecting
integer-frame class; the polar natural reflection 99.99967 pct
proportional to A_int, off the frame circle) but no strict
selection.  The lead's directive: the right next source is the
ACTUAL modular conjugation of the seam state -- if the real modular
frame selects, strict Hermiticity selects a wiring; if not,
representative-dependent statements leave the main text.  CCXV D2
tested modular data as COMPATIBLE/SILENT on the orbit; this probe
goes deeper and computes J_Omega itself.

FEASIBILITY / REDUNDANCY CHECK (against the corpus, 2026-08-12):
CCXXIX computed the modular FLOW dictionary (K_mod = -beta K_rot
exact at t = 0; Ad(rho^{i/4}) = deck step) and deck-sector response
-- never J_Omega; CCXV censused DEMANDS on the frame orbit -- never
the conjugation; CCXXXIII measured the state's polar reflection --
an SVD datum, not the Tomita object; round 59 censused twisted
involutions as RP witnesses -- not as modular conjugations.
NOTHING in the corpus constructs J_Omega on the GNS space and
projects its one-particle action onto the frame family.  New.

THE FROZEN CONSTRUCTION (documented exactly).  States (both
deployed corpus objects, beta = 1): DEP = the deployed seam-cell
KMS state, h_dep = -(A16_dep + t A_int), t = 1/8 (v898 / CCXXXIII
convention; the collar's zero-momentum fiber); PAR = the CCXV/CCXXI
quasi-free parent at the frozen probe-7 point (kappa, m, t) =
(1/2, 1/2, 1/20) with the deployed pure-I wiring V_dep.  Fock lift
H(h) = -(i/4) sum h_ij g_i g_j on 2^8 = 256 (CCXXIX conventions,
rebuilt; covariance ward against sibling kms_A).  GNS/STANDARD
FORM (exact on the finite type-I factor): GNS space = HS(C^256)
with <x, y> = Tr(x^dag y), Omega = rho^{1/2}, pi(a) x = a x,
Delta x = rho x rho^{-1}, J x = x^dag; Tomita relation
J Delta^{1/2} a Omega = a^dag Omega is ALGEBRAIC here -- the wards
run the SPECTRAL construction of Delta^{1/2} against the algebraic
route and verify every Tomita axiom on a generating set (16 gammas,
120 quadratics, 8 seeded random algebra elements; RNG declared in
ward batteries and controls only).  ONE-PARTICLE ACTION (the probe
object): J gamma(v) Omega = gamma(M v-bar) Omega with M measured by
GNS Gram inversion AND matched to the closed form M =
exp(+-i (beta/2) h) (sign disclosed by the machine, then frozen);
j1 = M o Theta_0, Theta_0 = entrywise conjugation in the deployed
Majorana basis = the v898 real structure.  FRAME FAMILY (CCXV,
rebuilt): theta_cell(gamma, y) = per carrier pair cos(2 gamma) X +
sin(2 gamma) Z, per boundary pair cos(2y) X + sin(2y) Z; theta_S =
theta_cell(0, 0) (all-X pair swap; delta = 0, selects pure-(+-J));
integer frame theta' (carrier -X, boundary X; delta = +-pi/2,
selects pure-(+-I)).  DECLARED DECOMPOSITION FACTORS (the mission
list): frame member theta(gamma, y); SHEET GRADING Gamma_s = Z per
pair (the deployed even/odd Majorana sublattice sign, v109/round-58
sheet lineage -- an INPUT CONVENTION, typed as deployment, tested
for covariance); collar orientation = the layer mirror (collar
tier); deck powers/parity as rotation-type grading impostors.
COLLAR TIER (one-particle exact, CCXXXIII budget convention): the
2N-layer collar h_N = I (x) h_cell-part with bond (t/2) A_int;
M_N = exp(i (beta/2) h_N) by eigendecomposition; the dense-Fock
wards at the cell LICENSE the one-particle formulas (the
derivation is representation-level; typed).  Bogoliubov
implementers for the Fock census: frames via pair-Householder
products gamma(u_p) x parity, rotations via exp(i H(a)); every
implementer warded against its one-particle target before use.

SMOKE-RUN DISCLOSURE (2026-08-12; THREE declared smoke rounds
before freezing; fail-first preserved; ALL frozen numbers below
were read off the smoke runs):
 SMOKE-1 (19/25; two mechanical bugs of MINE plus one hand-sign
       corrected by the machine, all disclosed): (i) the closed-
       form sign: the machine selected M = exp(+i (beta/2) h)
       (dev 1.9e-15) against the hand-derived minus (dev 1.1) --
       frozen as PLUS, consistent with the repo Fock-lift sign
       H = -(i/4) h.g.g; the structure content (M positive,
       conj(M) = M^{-1}, polar = I) is sign-independent and was
       already green; (ii) the Householder angle bug (MINE):
       2 u u^T - I with u = (cos a, sin a) is cos 2a Z + sin 2a X,
       so the frame implementer needed a = pi/4 - angle (X and Z
       swapped) -- exposed by the implementer ward (1.41) and by
       the census zero appearing in the gamma = 0 row; fixed; the
       zero's delta* = 0 reading was never affected (it moved
       rows, not delta); (iii) the covariance check compared mixed
       signs -- same fix as (i).
 SMOKE-2 (24/25): ONE remaining bug of MINE: the zero-candidate
       ward applied the candidate conjugation to a Omega instead
       of Delta^{1/2} a Omega (correct target V a^dag rho^{1/2}
       V^dag); fixed; no bar or claim moved.
 SMOKE-3 (25/25; the numbers frozen below): Tomita max rel
       residual 5.7e-15 (DEP) / 2.9e-15 (PAR); closure out-of-span
       3.3e-15, Gram-solve == closed form 1.9e-15 (wrong sign
       1.1e+00); eigmin(M) = 0.4464 > 0, polar dev 1.1e-15,
       conj(M) M - I = 2.0e-15; dressing cross corr = 1.000000
       (dev 0.0); equidistance dev 8.9e-16; reversal closed form
       c_int = 144 == 16 x 9 I2-interior edge-slots EXACT
       (residual 2.7e-15; the hand-guess 96 was WRONG, machine
       corrected), argmin delta = -pi/2, floor/max =
       sqrt(144/384) = 0.61; pure frame candidates ALL at 1.4142
       = sqrt(2) (floor frozen 0.1); composite census: unique zero
       0.0e+00 at (pi/4, 0), off-zero floor 0.1633 (frozen bar
       0.02), grid-neighbour value 0.163; beta-rigid True;
       transported-grading zero 6.7e-16, untransported candidate
       1.2674; rotation gradings min dist 5.657 = sqrt(32);
       natural-cone Gram eigmin +0.74 (1p) / +0.60 (deg-2) --
       strictly PD, identical to 3 digits across ALL THREE
       wirings; beta family ||log M||/beta dev 4.4e-16, polar = I
       at beta in {1/2, 1, 2, 2pi}; collar N in {2, 4, 8}: polar
       <= 3.3e-15, mirror mass 0.0, equidistance dev 0.0,
       KMS-shadow corr 0.99999668 (N = 8; CCXXXIII tie 0.9999967);
       (1-corr) cell ratio t vs t/2 = 3.9 -- the hand-guessed t^4
       scaling is REFUTED, the deficit scales ~ t^2 (disclosed,
       reported-only); C1 fires 0.4286 / 0.7459, C2 fires 0.4338
       with ratio 2.0000000000, C3 fires 0.2715, C4 fires 5.657.
 HAND-PREDICTIONS SCORED (written before smoke, non-binding): H1
       polar(M) = I CONFIRMED; H2 equidistance sqrt(32) CONFIRMED;
       H3 reversal shape a + b(1 + cos 2 delta) with argmin
       +-pi/2 CONFIRMED, but c_int = 144 not 96 (machine
       corrected); H4 all pure frame candidates fail Tomita
       CONFIRMED (all exactly sqrt(2)); H5 natural-cone Gram
       wiring-blind CONFIRMED (strictly PD); H6 dressing
       beta-linear CONFIRMED; H7 composite zero pinned at
       delta* = 0 for every channel-uniform reflection grading
       CONFIRMED; the closed-form SIGN and the shadow-deficit
       scaling were hand-WRONG and machine-corrected (disclosed).

FROZEN CLAIMS (2026-08-12, frozen + SHA-hashed after the declared
smoke rounds, before the frozen run; bars from the smokes):

 P1  THE STANDARD FORM AND THE TOMITA WARDS (both states).
     (a) faithfulness: eigmin(rho) > 0 (reported); ||Omega|| = 1;
         J Omega = Omega exact; Delta Omega = Omega <= 1e-10;
     (b) Tomita relation J Delta^{1/2} a Omega = a^dag Omega on
         the generating set (16 + 120 + 8 seeded), spectral route,
         relative residual <= 1e-8 (algebraic route is an exact
         identity on the finite factor, stated); J^2 = 1 and
         J Delta J = Delta^{-1} on 8 seeded vectors <= 1e-8;
     (c) modular flow tie (CCXXIX regression): Delta^{it}'s
         one-particle action == the REAL ROTATION exp(-t beta h)
         <= 1e-9 at t in {0.37, 1.0} -- the flow is the seam
         rotation; j1 COMMUTES with it (<= 1e-10), it does NOT
         reverse it: J is on the KMS side, frames are reversers.
 P2  THE ONE-PARTICLE ACTION (exact structure).
     (a) closure: J gamma(v) Omega stays in the one-particle GNS
         subspace (dense out-of-span residual <= 1e-10); the
         Gram-solved matrix == M = exp(+i (beta/2) h) <= 1e-10
         (sign frozen from smoke-1); Ad(rho^{1/2}) ward <= 1e-8;
     (b) STRUCTURE THEOREM (finite, exact): j1 = M o Theta_0 with
         M Hermitian POSITIVE (eigmin > 0), conj(M) = M^{-1}
         (<= 1e-10), j1^2 = 1 (<= 1e-10); polar/orthogonal factor
         of M == IDENTITY (<= 1e-10): the modular conjugation of
         EVERY deployed quasi-free seam state is the gauge-fixed
         real structure Theta_0 times a positive KMS dressing;
         Theta_0 is rule-gauge INVARIANT (exact for real g;
         measured for g_r = R(3/5, 4/5) <= 1e-12);
     (c) THE DRESSING CARRIES THE WIRING (the CCXXXIII polar
         reconciliation): log M = +i (beta/2) h EXACTLY, so the
         carrier-boundary cross block of the dressing is
         proportional to the wiring A_int cross block with
         corr == 1 (<= 1e-12); the KMS covariance cross block has
         corr(A_int) = 0.9999967 +- 1e-4 (collar N = 8
         seam-adjacent block; CCXXXIII regression) -- the polar
         off-family finding is the odd-function SHADOW of the
         dressing (the (1-corr) ratio at t vs t/2 reported;
         measured ~ t^2, ratio 3.9; the hand-guessed t^4 was
         wrong, disclosed);
     (d) BETA-DEPENDENCE: at beta in {1/2, 1, 2, 2pi}
         (one-particle route): polar(M(beta)) = I <= 1e-9 and
         ||log M(beta)||_F / beta constant <= 1e-9 relative --
         the frame-relevant part of J_Omega is BETA-RIGID (it is
         Theta_0 at every temperature), the dressing is
         beta-linear;
     (e) COLLAR TIER (N in {2, 4, 8}, one-particle exact,
         CCXXXIII budget): polar(M_N) = I <= 1e-9; the layer-
         mirror overlap tr(mirror . polar)/(16 L) == 0 (<= 1e-12):
         NO collar-orientation factor appears in J_Omega itself
         (the mirror lives in declared identifications only);
         equidistance ||I - mirror (x) theta(delta)||_F =
         sqrt(32 L) constant over the delta-grid (<= 1e-9).
 P3  THE FRAME COMPARISON (the payoff; exact + measured).
     (a) EXACT SEPARATION: every frame theta(delta) has per-pair
         2x2 blocks of det = -1 (exact identity, warded on the
         grid <= 1e-12); polar(j1) = I has per-pair det = +1;
         polar uniqueness => NO factorization j1 = frame x
         positive exists: J_Omega is OFF the frame circle AS AN
         ELEMENT; moreover ||I - theta(delta)||_F = sqrt(32)
         CONSTANT over the grid (<= 1e-9): J_Omega is EQUIDISTANT
         from the entire delta-circle -- maximal frame-silence of
         the raw conjugation;
     (b) THE DECOMPOSITION THEOREM (J = frame x grading x
         dressing; exact): the orthogonal-factor equation
         theta . Gamma = I has, among the declared factors, the
         UNIQUE solution theta = Gamma (polar uniqueness);
         a solution with theta in the frame family exists IFF the
         grading is reflection-type; for EVERY channel-uniform
         reflection grading Gamma(phi) (same in-pair angle phi on
         all 8 pairs) the solving frame is theta_cell(phi, phi):
         RELATIVE ANGLE delta* = 0 INDEPENDENT of the convention
         angle phi (measured over the phi-grid, drift <= 1e-9);
         for the DEPLOYED sheet grading Gamma_s = Z per pair the
         solving frame is theta_cell(pi/4, pi/4) = the diagonal-
         gauge transport of theta_S (exact); rotation-type
         gradings (deck powers A16^k, parity -I) admit NO frame
         solution (min distance >= 1);
     (c) THE FOCK CENSUS (the direct Tomita measurement of (b)):
         J-candidates J_V(x) = V x^dag V^dag with warded
         Bogoliubov implementers (implementer ward <= 1e-9):
         PURE frame candidates theta_S, theta_S x P, theta'
         (integer), theta(pi/4): Tomita residual >= 0.1 on the
         gamma set (ALL FAIL: theta_S is NOT the modular
         conjugation of the seam state -- measured); COMPOSITE
         frame x Gamma_s candidates over the (gamma in {0, pi/4},
         24-point delta)-grid: residual has the UNIQUE ZERO
         (<= 1e-9) at (gamma, delta) = (pi/4, 0) and >= 0.02
         everywhere else on the grid; at the zero the candidate
         is warded to equal J on quadratics + randoms too
         (<= 1e-9): RELATIVE TO THE DEPLOYED SHEET GRADING the
         modular conjugation pins the frame class delta* = 0 =
         the theta_S class, whose frozen selection-map ray is
         PURE-(+-J); beta-rigidity: the off-zero floor persists
         at beta in {1/2, 2} (>= 0.01) and the zero stays exact;
     (d) COVARIANCE (the CCXXI law; gate): under the rational
         carrier gauge g_r: M(g h g^T) = g M g^T <= 1e-10; the
         composite-census zero TRANSPORTS 1:1: with the
         transported grading g_r Gamma_s g_r^T the zero sits at
         the transported frame (residual <= 1e-9) and the
         UNTRANSPORTED zero candidate now FAILS (>= 0.02): the
         pinning is exactly as conventional as the sheet-grading
         deployment -- jointly covariant, NO absolute selection
         (the compiler-freedom theorem is honored, not moved);
     (e) THE PREFERENCE ANATOMY (CCXXXIII reconciliation #2): the
         flow-reversal defect D(delta)^2 = || theta h_dep theta +
         h_dep ||_F^2 has the EXACT closed form t^2 (c_int + 120
         (1 + cos 2 delta)) with c_int = 16 x (number of I2-type
         interior edge-slots) an integer (residual <= 1e-10),
         argmin at delta = +-pi/2 (the integer class -- the
         CCXXXIII deg-2 argmin class), gamma-invariant floor
         c_int > 0 (three gamma values, <= 1e-10): the measured
         CCXXXIII preference ordering is the anatomy of a
         theta-RELATIVE reversal demand, NOT a selection by
         J_Omega (which commutes with the flow, P1.c);
     (f) STRICT-HERMITICITY IS WIRING-BLIND AT THE MODULAR
         REFLECTION: the natural-cone Gram G[a,b] =
         Tr(m_a rho^{1/2} m_b^dag rho^{1/2}) on the 1p (16) and
         deg-2 (120) monomial sets is Hermitian (<= 1e-10) and
         PSD (eigmin >= -1e-10 x scale) IDENTICALLY for the
         pure-I, pure-J and (4/5, 3/5)-ray wirings: the true
         modular reflection provides NO wiring discrimination;
         the selective strict-RP mechanism lives entirely in the
         frame-theta forms (CCXV/CCXXXIII), which J_Omega does
         not rank absolutely (P3.a) -- only sheet-relatively
         (P3.c).
 C   CONTROLS (must fire; frozen fire rules; RNG declared).
     C1 NON-KMS/NON-QUASI-FREE STATE (seeded psi, eps = 0.1 mix):
        the one-particle closure BREAKS: out-of-span residual
        >= 0.005 (quasi-freeness is load-bearing); the mismatched
        Tomita relation (old (J, Delta), new Omega') breaks:
        residual >= 0.05;
     C2 WRONG-BETA STATE: the mismatched Tomita relation at
        beta' = 2 against the beta = 1 objects breaks (residual
        >= 0.05) and the one-particle reading SHIFTS exactly:
        ||log M(2)|| / ||log M(1)|| = 2 +- 1e-8;
     C3 SCRAMBLED DRESSING (seeded orthogonal Q): corr(Q .
        crossblock, A_int) <= 0.5 against truth 1 (kills the
        wiring correlation -- the CCXXXIII C3 analogue);
     C4 GRADING IMPOSTORS: deck powers A16^k (k = 1, 2, 3) and
        parity as gradings admit no frame solution: min distance
        over the torus grid >= 1 (rotation-type cannot cancel a
        reflection) -- the P3.b dichotomy is non-vacuous.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild / Fock ward   -> PIPELINE-BROKEN
  K1 a standard-form / Tomita ward breaks (P1)     -> MODULAR-MACHINERY-BROKEN
  K2 a one-particle structure ward breaks (P2)     -> MODULAR-MACHINERY-BROKEN
  K3 a comparison / census computation breaks (P3) -> COMPARISON-BROKEN
  K7 a control does not fire (C)                   -> CONTROL-DEAD

VERDICT (frozen enum, both-way):
  MODULAR-FRAME-SELECTS-ABSOLUTE(delta*) iff a PURE frame
    candidate passes Tomita (residual <= 1e-9) -- would contradict
    CCXV and is not expected;
  MODULAR-FRAME-SELECTS-RELATIVE(delta* = 0 -> theta_S class ->
    pure-(+-J) ray) iff P3.c holds as frozen (unique composite
    zero at (pi/4, 0) with the deployed sheet grading, off-zero
    floor, beta-rigid) AND P3.d covariance holds (the pinning
    transports 1:1 -- no absolute content) AND P3.a holds (the
    raw J_Omega is off-family; the CCXXXIII polar finding is the
    dressing);
  MODULAR-FRAME-COVARIANT-SILENT iff no composite zero exists
    with any declared grading;
  MODULAR-MACHINERY-BROKEN / COMPARISON-BROKEN / PIPELINE-BROKEN /
  CONTROL-DEAD as above.
Exit 0 iff all checks pass and no kill fired; else 1.

THE FROZEN EDITORIAL CONSEQUENCE (frozen with the spec; printed by
the verdict block if SELECTS-RELATIVE): frame-fixed wiring
sentences in ABSOLUTE form (e.g. "strict collar RP selects
pure-J") are representative-dependent gauge commentary and leave
the main text; the stateable physics form is SHEET-RELATIVE:
"relative to the deployed sheet grading, the seam state's own
modular conjugation pins the theta_S frame class (delta* = 0,
beta-rigid), whose frozen selection-map ray is pure-(+-J); the
deployed pure-I wiring is the g_int gauge transport of that ray;
absolutely, J_Omega = Theta_0 x positive KMS dressing pins no
frame and the compiler-freedom theorem stands."

ANTI-CIRCULARITY (declared): J_Omega is built from the STATE
alone (rho via the standard form; never from a frame); the frame
family enters only as TESTED candidates; the sheet grading is a
declared deployment convention (v109/round-58 lineage) whose
conventionality is itself measured (P3.d transport); the
selection map is the frozen CCXV formula, cited for NAMING only;
no bar was moved after the frozen run started.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  HONEST SCOPE: everything here is a
FINITE-MODEL computation on the deployed 16-Majorana seam cell
(256-dim Fock standard form) and its one-particle collar family;
on a finite type-I factor the modular conjugation is the standard-
form adjoint and the half-sided/Bisognano-Wichmann GEOMETRIC
conjugation of a true collar inclusion needs the continuum limit
-- typed OPEN, untouched; the sheet grading is deployment lineage,
not compiler output; the compiler-freedom theorem (CCXIII/CCXV/
CCXXI) is UNMOVED -- the relative selection is a PHYSICS statement
on top of it.  NO marker moves.  NO RH claim.

SPEC v1 (2026-08-12): frozen after the declared smoke rounds
(disclosed above); no bar moved after the frozen run started.

Sources (read-only, machinery rebuilt inline): p1_modular_index_
response_probe (Fock layer, gibbs, kms_A), calderon_scaling_
realize_probe (compiler rebuild, collar family, theta_cell,
delta-grid), theta_frame_selector_probe (frame orbit, theta_S,
integer frame, selection map), wiring_gauge_rp_audit_probe
(covariance law), seam_state_derivation_probe (round 58 sheet
lineage), v898 (Theta_0), tfpt_constants.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/modular_frame_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

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
SEED = 20260812

T_DEP = 0.125
BETA_DEP = 1.0
ZTOL = 1e-10
WTOL = 1e-8
EQ_TOL = 1e-9
PURE_FLOOR = 0.1            # pure frame candidates must exceed
COMP_FLOOR = 0.02           # composite off-zero floor
COMP_FLOOR_B = 0.01         # off-zero floor at other betas
C1_SPAN = 0.005
C1_TOMITA = 0.05
C2_TOMITA = 0.05
DELTA_GRID = -np.pi / 2 + np.arange(24) * np.pi / 24
GAMMA0 = math.atan2(4.0, 3.0)


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


# ---------------------------------------------------------- bit model
# (byte-parallel to calderon_scaling_realize_probe S0)
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
    n_i2_int = 0
    for edges, rev, rep in orbs:
        i, j = rep
        B = J2i if rev else (IOTA6i if i == 0 else I2i)
        if (not rev) and i != 0:
            n_i2_int += len(edges)
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
    return ok0, A_dep, A_int, O16, n_i2_int


# ---------------------------------------------------------- Fock layer
def jw_ops(n):
    sm = np.array([[0, 1], [0, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2c = np.eye(2, dtype=complex)
    ops = []
    for j in range(n):
        m = np.array([[1.0]], dtype=complex)
        for l in range(n):
            m = np.kron(m, sz if l < j else (sm if l == j else I2c))
        ops.append(m)
    return ops


def majoranas(n_modes):
    cs = jw_ops(n_modes)
    gs = []
    for p in range(n_modes):
        gs.append(cs[p] + cs[p].conj().T)
        gs.append(1j * (cs[p] - cs[p].conj().T))
    return gs, cs


def quad_op(h, gs):
    """Fock lift H(h) = -(i/4) sum h_ij g_i g_j (CCXXIX frozen sign)."""
    n = h.shape[0]
    dim = gs[0].shape[0]
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(n):
        for j in range(n):
            if h[i, j] != 0.0:
                H += (-0.25j) * h[i, j] * (gs[i] @ gs[j])
    return (H + H.conj().T) / 2


def kms_A(h, beta):
    n = h.shape[0]
    w, Q = np.linalg.eigh(1j * h)
    f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
    C = (Q * f) @ Q.conj().T
    return np.real(-1j * (2 * C - np.eye(n))), C


def gibbs(H, beta):
    w, V = np.linalg.eigh(H)
    lw = -beta * w
    lw -= lw.max()
    p = np.exp(lw)
    p /= p.sum()
    return (V * p) @ V.conj().T, w, V, p


def one_particle_M(h, beta, sign=-1.0):
    """closed-form dressing M = exp(sign * i (beta/2) h) via eigh."""
    mu, Q = np.linalg.eigh(1j * h)
    return (Q * np.exp(sign * beta / 2.0 * mu)) @ Q.conj().T


# --------------------------------------------------- frames / gradings
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


def refl_uniform(phi):
    """channel-uniform reflection grading Gamma(phi) (all 8 pairs)."""
    th = np.zeros((16, 16))
    u = math.cos(2 * phi) * X2 + math.sin(2 * phi) * Z2
    for p in range(8):
        th[2 * p:2 * p + 2, 2 * p:2 * p + 2] = u
    return th


GAMMA_S = refl_uniform(np.pi / 4)          # Z per pair (sheet grading)


def polar_dev(M):
    """(eigmin, ||polar factor - I||_max) of a Hermitian matrix."""
    lam, Q = np.linalg.eigh((M + M.conj().T) / 2)
    U = (Q * np.sign(lam)) @ Q.conj().T
    return float(np.min(lam)), float(np.max(np.abs(U - np.eye(len(M)))))


# ------------------------------------------------- Fock implementers
def householder_refl_impl(units, gs, P_par):
    """implementer of the per-pair Householder reflection product
    (2 u_p u_p^T - I on pair p) via prod gamma(u_p) x parity fix."""
    dim = gs[0].shape[0]
    V = np.eye(dim, dtype=complex)
    for u in units:
        g_u = sum(u[a] * gs[a] for a in range(16) if u[a] != 0.0)
        V = V @ g_u
    n = len(units)
    # prod of n odd factors implements (-1)^(n-1) x blockwise map;
    # compose with parity when n is even to fix the global sign.
    if n % 2 == 0:
        V = V @ P_par
    return V


def rot_impl(a, gs):
    """unitary with Ad(V) gamma(v) = gamma(e^a v), a real antisym."""
    HF = quad_op(a, gs)
    w, Q = np.linalg.eigh(HF)
    return (Q * np.exp(1j * w)) @ Q.conj().T


def impl_ward(V, O, gs):
    """max_a || V g_a V^dag - gamma(O e_a) ||_max."""
    dev = 0.0
    Vd = V.conj().T
    for a in range(16):
        tgt = sum(O[b, a] * gs[b] for b in range(16)
                  if abs(O[b, a]) > 1e-15)
        dev = max(dev, float(np.max(np.abs(V @ gs[a] @ Vd - tgt))))
    return dev


def tomita_residual(V, gset_rho, rho_h):
    """rms over the gamma set of || V g_a rho^(1/2) V^dag -
    g_a rho^(1/2) || (all norms 1: ||g_a rho^(1/2)|| = 1)."""
    Vd = V.conj().T
    r2 = 0.0
    for GR in gset_rho:
        d = V @ GR @ Vd - GR
        r2 += float(np.real(np.vdot(d, d)))
    return math.sqrt(r2 / len(gset_rho))


def main():
    print("SEAM.STATE.MODULAR.FRAME.01 -- the actual modular "
          "conjugation J_Omega of the deployed seam state, its "
          "one-particle action, and the frame-circle decision")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")
    rng = np.random.default_rng(SEED)

    # ==================================================================
    section("S0 -- firewall + compiler rebuild + Fock layer")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s" % (BANNED_IDS,),
          not bad, kill="K0")

    ok0, A_dep, A_int, O16, n_i2_int = build_compiler()
    check("S0.1 compiler rebuilt: unique q*, |Aut| = 6, pi cycle "
          "type (1,2,3), A_dep/A_int covariant + antisymmetric "
          "(N_fam = %d, g_car = %d consumed read-only)"
          % (N_fam, g_car), ok0, kill="K0")

    Adep_f = A_dep.astype(np.float64)
    Aint_f = A_int.astype(np.float64)
    comm_ok = not (A_dep @ A_int - A_int @ A_dep).any()
    rank_q = sp.Matrix(A_int.tolist()).rank()
    h_dep = -(Adep_f + T_DEP * Aint_f)
    A1p_dep, _C = kms_A(h_dep, BETA_DEP)
    smax_cell = float(np.max(np.abs(np.linalg.eigvalsh(1j * A1p_dep))))
    check("S0.2 corpus regressions: [A_dep, A_int] = 0 integer (%s); "
          "rank_Q(A_int) = %d == 12; cell KMS smax = %.6f "
          "(0.667735 +- 1e-6)" % (comm_ok, rank_q, smax_cell),
          comm_ok and rank_q == 12
          and abs(smax_cell - 0.667735) <= 1e-6, kill="K0")

    gs, cs = majoranas(8)
    dim = 256
    car_dev = 0.0
    for a in range(16):
        for b in range(a, 16):
            tgt = 2.0 * (a == b) * np.eye(dim)
            car_dev = max(car_dev, float(np.max(np.abs(
                gs[a] @ gs[b] + gs[b] @ gs[a] - tgt))))
    # the CCXV parent at (kappa, m, t) = (1/2, 1/2, 1/20), wiring V_dep
    Vdep_CB = Aint_f[np.ix_(range(10), range(10, 16))]
    cross = np.zeros((16, 16))
    cross[np.ix_(range(10), range(10, 16))] = Vdep_CB
    cross[np.ix_(range(10, 16), range(10))] = -Vdep_CB.T
    h_par = -(0.5 * Adep_f + 0.05 * cross)
    cov_dev = 0.0
    packs = {}
    for name, h in (("DEP", h_dep), ("PAR", h_par)):
        HF = quad_op(h, gs)
        rho, wE, VE, pE = gibbs(HF, BETA_DEP)
        A1p, _ = kms_A(h, BETA_DEP)
        Mtp = np.zeros((16, 16), dtype=complex)
        for a in range(16):
            Ra = rho @ gs[a]
            for b in range(16):
                Mtp[a, b] = np.sum(Ra.T * gs[b])
        cov_dev = max(cov_dev, float(np.max(np.abs(
            Mtp - np.eye(16) - 1j * A1p))))
        ph = np.sqrt(pE)
        rho_h = (VE * ph) @ VE.conj().T
        packs[name] = dict(h=h, HF=HF, rho=rho, w=wE, V=VE, p=pE,
                           rho_h=rho_h, A1p=A1p)
    check("S0.3 Fock layer: CAR dev %.1e <= 1e-10; the frozen lift "
          "H(h) = -(i/4) h.g.g reproduces the sibling KMS covariance "
          "for BOTH deployed states (dev %.1e <= 1e-8)"
          % (car_dev, cov_dev),
          car_dev <= ZTOL and cov_dev <= WTOL, kill="K0")

    Nvec = np.zeros(dim)
    for p in range(8):
        Nvec += np.real(np.diag(cs[p].conj().T @ cs[p]))
    Nint = np.rint(Nvec).astype(int)
    P_par = np.diag(np.array([(-1.0) ** n for n in Nint],
                             dtype=complex))

    # ==================================================================
    section("P1 -- the standard form and the Tomita wards")
    # ==================================================================
    for name in ("DEP", "PAR"):
        pk = packs[name]
        rho, rho_h = pk["rho"], pk["rho_h"]
        VE, pE = pk["V"], pk["p"]
        pmin = float(np.min(pE))
        nrm = float(np.linalg.norm(rho_h))
        # spectral Delta^{1/2} on x: V (X' * sqrt(p_m/p_n)) V^dag
        ratio = np.sqrt(np.outer(pE, 1.0 / pE))

        def delta_half(x):
            Xp = VE.conj().T @ x @ VE
            return VE @ (Xp * ratio) @ VE.conj().T

        gen = [gs[a] for a in range(16)]
        gen += [gs[p] @ gs[q] for p in range(16) for q in range(p + 1, 16)]
        gen += [(rng.normal(size=(dim, dim))
                 + 1j * rng.normal(size=(dim, dim))) for _ in range(8)]
        res_max = 0.0
        for aop in gen:
            lhs = delta_half(aop @ rho_h).conj().T
            tgt = aop.conj().T @ rho_h
            res_max = max(res_max, float(np.linalg.norm(lhs - tgt))
                          / max(float(np.linalg.norm(tgt)), 1e-30))
        # J^2 = 1 trivial; J Delta J = Delta^{-1} on seeded vectors
        jdj_dev = 0.0
        for _ in range(8):
            x = (rng.normal(size=(dim, dim))
                 + 1j * rng.normal(size=(dim, dim)))
            lhs = (rho @ x.conj().T @ np.linalg.solve(
                rho, np.eye(dim))).conj().T
            rhs = np.linalg.solve(rho, x) @ rho
            jdj_dev = max(jdj_dev, float(np.linalg.norm(lhs - rhs))
                          / max(float(np.linalg.norm(rhs)), 1e-30))
        dOm = float(np.linalg.norm(rho @ rho_h @ np.linalg.solve(
            rho, np.eye(dim)) - rho_h))
        check("P1.1[%s] standard form: eigmin(rho) = %.1e > 0, "
              "||Omega|| = %.12f, Delta Omega = Omega (%.1e); "
              "TOMITA J Delta^{1/2} a Omega = a^dag Omega on 144 "
              "generators (spectral route, max rel res %.1e <= 1e-8); "
              "J Delta J = Delta^{-1} (%.1e <= 1e-8)"
              % (name, pmin, nrm, dOm, res_max, jdj_dev),
              pmin > 0 and abs(nrm - 1) <= 1e-10 and dOm <= WTOL
              and res_max <= WTOL and jdj_dev <= WTOL, kill="K1")

    # modular flow tie (CCXXIX): Delta^{it} one-particle rotation
    pk = packs["DEP"]
    mu, Qh = np.linalg.eigh(1j * pk["h"])
    flow_dev = 0.0
    for tt in (0.37, 1.0):
        # (M^2)^{it} = Q e^{i t beta mu} Q^dag is REAL orthogonal
        D_it = (Qh * np.exp(1j * tt * BETA_DEP * mu)) @ Qh.conj().T
        Ereal = np.real(D_it)
        flow_dev = max(flow_dev, float(np.max(np.abs(D_it - Ereal))))
    # Delta gamma(v) Omega = gamma(M^2 v) Omega, M = e^{+i(beta/2)h}
    Mdep = one_particle_M(pk["h"], BETA_DEP, sign=+1.0)
    M2 = Mdep @ Mdep
    dflow = 0.0
    rho, rho_h = pk["rho"], pk["rho_h"]
    rinv = np.linalg.solve(rho, np.eye(dim))
    for a in range(4):
        lhs = rho @ gs[a] @ rinv @ rho_h
        tgt = sum(M2[b, a] * gs[b] for b in range(16)) @ rho_h
        dflow = max(dflow, float(np.linalg.norm(lhs - tgt)))
    # j1 commutes with the flow: [M, h] = 0
    comm_flow = float(np.max(np.abs(Mdep @ pk["h"] - pk["h"] @ Mdep)))
    check("P1.2 modular flow tie (CCXXIX regression): Delta^{it}'s "
          "one-particle map is the REAL seam rotation (imag part "
          "%.1e <= 1e-9 at t in {0.37, 1}); Delta gamma(v) Omega = "
          "gamma(M^2 v) Omega (%.1e <= 1e-8); j1 COMMUTES with the "
          "flow ([M, h] = %.1e <= 1e-10): J is on the KMS side, "
          "frames are flow-REVERSERS"
          % (flow_dev, dflow, comm_flow),
          flow_dev <= EQ_TOL and dflow <= WTOL and comm_flow <= ZTOL,
          kill="K1")

    # ==================================================================
    section("P2 -- the one-particle action of J_Omega (exact)")
    # ==================================================================
    Mmeas = {}
    for name in ("DEP", "PAR"):
        pk = packs[name]
        rho_h, A1p, h = pk["rho_h"], pk["A1p"], pk["h"]
        G16 = np.eye(16) + 1j * A1p
        # Y[b, a] = <g_b Omega, J g_a Omega> = Tr(rho_h g_b rho_h g_a)
        Y = np.zeros((16, 16), dtype=complex)
        RgR = [rho_h @ gs[b] @ rho_h for b in range(16)]
        for b in range(16):
            for a in range(16):
                Y[b, a] = np.sum(RgR[b].T * gs[a])
        Cmat = np.linalg.solve(G16, Y)
        Mminus = one_particle_M(h, BETA_DEP, sign=-1.0)
        Mplus = one_particle_M(h, BETA_DEP, sign=+1.0)
        dev_m = float(np.max(np.abs(Cmat - Mminus)))
        dev_p = float(np.max(np.abs(Cmat - Mplus)))
        sgn = "-" if dev_m <= dev_p else "+"
        Msel = Mminus if dev_m <= dev_p else Mplus
        dev_sel = min(dev_m, dev_p)
        # dense out-of-span + closure residual
        span_res = 0.0
        adr_dev = 0.0
        rinv_h = (pk["V"] * (1.0 / np.sqrt(pk["p"]))) @ pk["V"].conj().T
        for a in range(16):
            lhs = rho_h @ gs[a]
            fit = sum(Msel[b, a] * gs[b] for b in range(16)) @ rho_h
            span_res = max(span_res, float(np.linalg.norm(lhs - fit)))
            adr = rho_h @ gs[a] @ rinv_h
            tgt = sum(Msel[b, a] * gs[b] for b in range(16))
            adr_dev = max(adr_dev, float(np.max(np.abs(adr - tgt))))
        Mmeas[name] = Msel
        check("P2.1[%s] one-particle closure: J gamma Omega stays in "
              "the 1p subspace (out-of-span %.1e <= 1e-10); measured "
              "Gram solve == closed form M = exp(%si (beta/2) h) "
              "(dev %.1e <= 1e-10; other sign dev %.1e); "
              "Ad(rho^{1/2}) ward %.1e <= 1e-8"
              % (name, span_res, sgn, dev_sel, max(dev_m, dev_p),
                 adr_dev),
              span_res <= ZTOL and dev_sel <= ZTOL and sgn == "+"
              and adr_dev <= WTOL, kill="K2")

    M = Mmeas["DEP"]
    eigmin_M, pol_dev = polar_dev(M)
    conj_dev = float(np.max(np.abs(M.conj() @ M - np.eye(16))))
    # j1^2 = M conj(M) = 1
    theta0_dev = 0.0
    g_r = np.eye(16)
    R35 = np.array([[3.0 / 5, -4.0 / 5], [4.0 / 5, 3.0 / 5]])
    for p in range(5):
        g_r[2 * p:2 * p + 2, 2 * p:2 * p + 2] = R35
    # Theta_0 gauge invariance: g conj(g^-1 v) = conj(v) for real g
    v_test = rng.normal(size=16) + 1j * rng.normal(size=16)
    theta0_dev = float(np.max(np.abs(
        g_r @ np.conj(g_r.T @ v_test) - np.conj(v_test))))
    check("P2.2 STRUCTURE THEOREM: j1 = M o Theta_0 with M POSITIVE "
          "(eigmin %.4f > 0), polar factor == I (%.1e <= 1e-10), "
          "conj(M) = M^{-1} (j1^2 = 1: %.1e <= 1e-10); Theta_0 is "
          "rule-gauge INVARIANT (g_r ward %.1e <= 1e-12)"
          % (eigmin_M, pol_dev, conj_dev, theta0_dev),
          eigmin_M > 0 and pol_dev <= ZTOL and conj_dev <= ZTOL
          and theta0_dev <= 1e-12, kill="K2")

    # the dressing carries the wiring
    logM = 1j * (BETA_DEP / 2.0) * packs["DEP"]["h"]
    lamM, QM = np.linalg.eigh(M)
    logM_num = (QM * np.log(lamM)) @ QM.conj().T
    lm_check = float(np.max(np.abs(logM_num - logM)))
    cr = np.ix_(range(10), range(10, 16))
    xb = np.imag(logM[cr]).ravel()
    yb = Aint_f[cr].ravel()
    corr_dress = float(np.dot(xb, yb)
                       / max(np.linalg.norm(xb) * np.linalg.norm(yb),
                             1e-30))
    check("P2.3 THE DRESSING CARRIES THE WIRING: log M (measured "
          "from the eigendecomposition) == +i (beta/2) h EXACT "
          "(%.1e <= 1e-10); cross block of the dressing prop. A_int "
          "with |corr| = %.12f (dev %.1e <= 1e-12)"
          % (lm_check, abs(corr_dress), abs(abs(corr_dress) - 1.0)),
          lm_check <= ZTOL and abs(abs(corr_dress) - 1.0) <= 1e-12,
          kill="K2")

    # beta family
    ok_beta = True
    lnorms = []
    for beta in (0.5, 1.0, 2.0, 2 * math.pi):
        Mb = one_particle_M(packs["DEP"]["h"], beta, sign=+1.0)
        emin, pdev = polar_dev(Mb)
        mub, Qb = np.linalg.eigh(1j * packs["DEP"]["h"])
        ln = float(np.linalg.norm((beta / 2.0) * mub))
        lnorms.append(ln / beta)
        ok_beta &= (emin > 0 and pdev <= EQ_TOL)
    beta_lin = float(np.max(np.abs(np.array(lnorms) - lnorms[0])))
    check("P2.4 BETA-DEPENDENCE: polar(M(beta)) = I at beta in "
          "{1/2, 1, 2, 2pi} (all <= 1e-9: %s); ||log M||/beta "
          "constant (dev %.1e <= 1e-9): the frame-relevant part of "
          "J_Omega is BETA-RIGID (Theta_0 at every temperature), "
          "the dressing beta-linear" % (ok_beta, beta_lin),
          ok_beta and beta_lin <= EQ_TOL, kill="K2")

    # collar tier (one-particle exact; CCXXXIII budget)
    ok_col = True
    col_report = []
    corr_shadow = {}
    for N in (2, 4, 8):
        L = 2 * N
        hN = np.zeros((16 * L, 16 * L))
        for m in range(L):
            hN[16 * m:16 * m + 16, 16 * m:16 * m + 16] = -Adep_f
        for m in range(L - 1):
            hN[16 * m:16 * m + 16, 16 * (m + 1):16 * (m + 1) + 16] \
                = -(T_DEP / 2) * Aint_f
            hN[16 * (m + 1):16 * (m + 1) + 16, 16 * m:16 * m + 16] \
                = (T_DEP / 2) * Aint_f.T
        MN = one_particle_M(hN, BETA_DEP, sign=+1.0)
        emin, pdev = polar_dev(MN)
        mir = np.zeros((16 * L, 16 * L))
        for m in range(L):
            mm = L - 1 - m
            mir[16 * mm:16 * mm + 16, 16 * m:16 * m + 16] = np.eye(16)
        mir_mass = abs(float(np.sum(mir * np.eye(16 * L)))) / (16 * L)
        # equidistance of I from mirror (x) theta(delta)
        dists = []
        for dl in DELTA_GRID[::4]:
            TH = np.kron(mir, theta_cell(0.0, dl))
            # mirror on layers x cell frame: build directly
            TH = np.zeros((16 * L, 16 * L))
            thc = theta_cell(0.0, dl)
            for m in range(L):
                mm = L - 1 - m
                TH[16 * mm:16 * mm + 16, 16 * m:16 * m + 16] = thc
            dists.append(float(np.linalg.norm(np.eye(16 * L) - TH)))
        d_flat = float(np.max(np.abs(np.array(dists)
                                     - math.sqrt(32 * L))))
        # KMS shadow at the seam-adjacent cross block
        AN, _ = kms_A(hN, BETA_DEP)
        Xb = AN[16 * (N - 1):16 * N, 16 * N:16 * N + 16]
        cshad = float(np.sum(Xb * Aint_f)
                      / max(np.linalg.norm(Xb)
                            * np.linalg.norm(Aint_f), 1e-30))
        corr_shadow[N] = cshad
        ok_col &= (emin > 0 and pdev <= EQ_TOL and mir_mass <= 1e-12
                   and d_flat <= EQ_TOL)
        col_report.append("N=%d: polar %.1e, mirror %.1e, "
                          "equid %.1e, shadow corr %.8f"
                          % (N, pdev, mir_mass, d_flat, cshad))
    # shadow scaling at t vs t/2 (cell level, reported)
    def cell_shadow(t):
        hh = -(Adep_f + t * Aint_f)
        AA, _ = kms_A(hh, BETA_DEP)
        Xc = AA[cr]
        return float(np.sum(Xc * Aint_f[cr])
                     / max(np.linalg.norm(Xc)
                           * np.linalg.norm(Aint_f[cr]), 1e-30))
    s_t = 1.0 - abs(cell_shadow(T_DEP))
    s_t2 = 1.0 - abs(cell_shadow(T_DEP / 2))
    ratio_shadow = s_t / max(s_t2, 1e-30)
    print("      collar ladder: " + " | ".join(col_report))
    print("      dressing corr == 1 exact vs KMS shadow corr "
          "(CCXXXIII tie 0.9999967); (1-corr) cell: t %.3e / t/2 "
          "%.3e, ratio %.1f (reported, ~t^2)"
          % (s_t, s_t2, ratio_shadow))
    check("P2.5 COLLAR TIER: polar(M_N) = I, layer-mirror overlap "
          "= 0, equidistance sqrt(32 L) flat (N in {2,4,8}); the "
          "KMS shadow corr at N = 8 = %.7f (CCXXXIII tie 0.9999967 "
          "+- 1e-4): NO collar-orientation factor appears in "
          "J_Omega itself" % (corr_shadow[8],),
          ok_col and abs(abs(corr_shadow[8]) - 0.9999967) <= 1e-4,
          kill="K2")

    # ==================================================================
    section("P3 -- the frame comparison (the payoff)")
    # ==================================================================
    # (a) exact separation + equidistance on the cell
    det_dev = 0.0
    eq_dev = 0.0
    for dl in DELTA_GRID:
        th = theta_cell(0.0, dl)
        for p in range(8):
            det_dev = max(det_dev, abs(np.linalg.det(
                th[2 * p:2 * p + 2, 2 * p:2 * p + 2]) + 1.0))
        eq_dev = max(eq_dev, abs(float(np.linalg.norm(np.eye(16) - th))
                                 - math.sqrt(32.0)))
    check("P3.1 EXACT SEPARATION: every frame has per-pair det = -1 "
          "(max dev %.1e <= 1e-12); polar(j1) = I has det = +1 per "
          "pair; polar uniqueness => NO j1 = frame x positive "
          "factorization; equidistance ||I - theta(delta)|| = "
          "sqrt(32) constant (dev %.1e <= 1e-9): J_Omega is "
          "EQUIDISTANT from the whole delta-circle"
          % (det_dev, eq_dev),
          det_dev <= 1e-12 and eq_dev <= EQ_TOL, kill="K3")

    # (b) decomposition theorem
    drift = 0.0
    for phi in np.linspace(0, np.pi, 13):
        Gam = refl_uniform(phi)
        # solving frame theta = Gamma; its (gamma, y) angles are
        # (phi, phi): relative angle delta* = 0 by construction;
        # verify by direct residual minimization over the torus grid
        best = (1e9, None, None)
        for gl in np.linspace(0, np.pi, 12, endpoint=False):
            for dl in DELTA_GRID:
                th = theta_cell(gl, gl + dl)
                r = float(np.linalg.norm(th @ Gam - np.eye(16)))
                if r < best[0]:
                    best = (r, gl, dl)
        drift = max(drift, abs(best[2]), best[0])
    Gs_frame = theta_cell(np.pi / 4, np.pi / 4)
    gs_exact = float(np.max(np.abs(Gs_frame @ GAMMA_S - np.eye(16))))
    # rotation gradings: no solution
    rot_min = 1e9
    for k in (1, 2, 3):
        Gk = np.linalg.matrix_power(Adep_f, k)
        for gl in np.linspace(0, np.pi, 12, endpoint=False):
            for dl in DELTA_GRID[::2]:
                th = theta_cell(gl, gl + dl)
                rot_min = min(rot_min, float(np.linalg.norm(
                    th @ Gk - np.eye(16))))
    for gl in np.linspace(0, np.pi, 12, endpoint=False):
        for dl in DELTA_GRID[::2]:
            th = theta_cell(gl, gl + dl)
            rot_min = min(rot_min, float(np.linalg.norm(
                th @ (-np.eye(16)) - np.eye(16))))
    check("P3.2 DECOMPOSITION THEOREM: for EVERY channel-uniform "
          "reflection grading Gamma(phi) the solving frame is "
          "theta_cell(phi, phi): delta* = 0 INDEPENDENT of the "
          "convention angle (max |delta*| + residual %.1e <= 1e-9 "
          "over 13 phi); deployed sheet grading Gamma_s = Z-per-"
          "pair: solving frame theta_cell(pi/4, pi/4) EXACT (%.1e) "
          "= the diagonal-gauge transport of theta_S; rotation "
          "gradings (deck powers, parity): NO solution (min dist "
          "%.3f >= 1)" % (drift, gs_exact, rot_min),
          drift <= EQ_TOL and gs_exact <= 1e-12 and rot_min >= 1.0,
          kill="K3")

    # (c) the Fock census
    rho_h = packs["DEP"]["rho_h"]
    gset_rho = [gs[a] @ rho_h for a in range(16)]

    def frame_impl(gamma, y):
        """implementer of theta_cell(gamma, y) (warded)."""
        units = []
        for p in range(8):
            ang = gamma if p < 5 else y
            # Householder 2 u u^T - I with u = (cos a, sin a) is
            # cos 2a Z + sin 2a X; the frame cos 2 ang X +
            # sin 2 ang Z needs a = pi/4 - ang (smoke-1 fix (ii))
            a_h = math.pi / 4 - ang
            u = np.zeros(16)
            u[2 * p] = math.cos(a_h)
            u[2 * p + 1] = math.sin(a_h)
            units.append(u)
        return householder_refl_impl(units, gs, P_par)

    def grading_impl_sheet():
        """implementer of Gamma_s = Z per pair (u_p = e_{2p})."""
        units = []
        for p in range(8):
            u = np.zeros(16)
            u[2 * p] = 1.0
            units.append(u)
        return householder_refl_impl(units, gs, P_par)

    V_Gs = grading_impl_sheet()
    wd = impl_ward(V_Gs, GAMMA_S, gs)
    V_thS = frame_impl(0.0, 0.0)
    wd = max(wd, impl_ward(V_thS, theta_cell(0.0, 0.0), gs))
    V_int = frame_impl(np.pi / 2, 0.0)
    wd = max(wd, impl_ward(V_int, theta_cell(np.pi / 2, 0.0), gs))
    V_q = frame_impl(0.0, np.pi / 4)
    wd = max(wd, impl_ward(V_q, theta_cell(0.0, np.pi / 4), gs))
    check("P3.3a implementer wards: Bogoliubov implementers "
          "reproduce their one-particle targets (max dev %.1e <= "
          "1e-9)" % wd, wd <= EQ_TOL, kill="K3")

    pure_res = {}
    pure_res["theta_S"] = tomita_residual(V_thS, gset_rho, rho_h)
    pure_res["theta_S x P"] = tomita_residual(V_thS @ P_par,
                                              gset_rho, rho_h)
    pure_res["theta_int"] = tomita_residual(V_int, gset_rho, rho_h)
    pure_res["theta(pi/4)"] = tomita_residual(V_q, gset_rho, rho_h)
    print("      PURE frame candidates (Tomita residual, floor %.2f):"
          % PURE_FLOOR)
    for k, v in pure_res.items():
        print("        %-12s : %.4f" % (k, v))
    ok_pure = all(v >= PURE_FLOOR for v in pure_res.values())
    check("P3.3b PURE frame candidates ALL FAIL Tomita (min %.4f >= "
          "%.2f): theta_S is NOT the modular conjugation of the "
          "seam state (measured)"
          % (min(pure_res.values()), PURE_FLOOR),
          ok_pure, kill="K3")

    # composite census over (gamma in {0, pi/4}, delta grid)
    comp = {}
    for gl in (0.0, np.pi / 4):
        row = []
        for dl in DELTA_GRID:
            Vf = frame_impl(gl, gl + dl)
            r = tomita_residual(Vf @ V_Gs, gset_rho, rho_h)
            row.append(r)
        comp[gl] = row
    i0 = int(np.argmin(np.abs(DELTA_GRID - 0.0)))
    r_zero = comp[np.pi / 4][i0]
    others = [r for gl in comp for j, r in enumerate(comp[gl])
              if not (gl == np.pi / 4 and j == i0)]
    r_floor = min(others)
    print("      COMPOSITE frame x Gamma_s census "
          "(gamma = 0 / pi/4 rows over the 24-point delta grid):")
    for gl in (0.0, np.pi / 4):
        print("        gamma=%.3f: " % gl
              + " ".join("%.3f" % r for r in comp[gl]))
    # ward the zero on quadratics + randoms too
    Vzero = frame_impl(np.pi / 4, np.pi / 4) @ V_Gs
    zward = 0.0
    for aop in ([gs[p] @ gs[q] for p in range(4) for q in
                 range(p + 1, 5)]
                + [rng.normal(size=(dim, dim))
                   + 1j * rng.normal(size=(dim, dim))
                   for _ in range(3)]):
        # J_cand Delta^{1/2} a Omega = V a^dag rho^{1/2} V^dag
        lhs = Vzero @ aop.conj().T @ rho_h @ Vzero.conj().T
        tgt = aop.conj().T @ rho_h
        zward = max(zward, float(np.linalg.norm(lhs - tgt))
                    / max(float(np.linalg.norm(tgt)), 1e-30))
    # beta rigidity of the census
    ok_brig = True
    for beta in (0.5, 2.0):
        HFb = packs["DEP"]["HF"]
        rho_b, wb, Vb, pb = gibbs(HFb, beta)
        rho_hb = (Vb * np.sqrt(pb)) @ Vb.conj().T
        gset_b = [gs[a] @ rho_hb for a in range(16)]
        rz = tomita_residual(Vzero, gset_b, rho_hb)
        roffs = [tomita_residual(frame_impl(np.pi / 4,
                                            np.pi / 4 + dl) @ V_Gs,
                                 gset_b, rho_hb)
                 for dl in (DELTA_GRID[6], DELTA_GRID[18])]
        ok_brig &= (rz <= EQ_TOL and min(roffs) >= COMP_FLOOR_B)
    check("P3.3c COMPOSITE census: UNIQUE ZERO at (gamma, delta) = "
          "(pi/4, 0): residual %.1e <= 1e-9, warded on quadratics + "
          "randoms (%.1e <= 1e-9); off-zero floor %.4f >= %.2f; "
          "beta-rigid at beta in {1/2, 2} (%s): RELATIVE TO THE "
          "DEPLOYED SHEET GRADING J_Omega pins delta* = 0 = the "
          "theta_S class -> frozen selection map -> PURE-(+-J) ray"
          % (r_zero, zward, r_floor, COMP_FLOOR, ok_brig),
          r_zero <= EQ_TOL and zward <= EQ_TOL
          and r_floor >= COMP_FLOOR and ok_brig, kill="K3")

    # (d) covariance (CCXXI law)
    h_g = g_r @ packs["DEP"]["h"] @ g_r.T
    M_g = one_particle_M(h_g, BETA_DEP, sign=+1.0)
    cov_law = float(np.max(np.abs(M_g - g_r @ M @ g_r.T)))
    # transported grading and its solving frame
    Gam_t = g_r @ GAMMA_S @ g_r.T
    th_t = Gam_t.copy()          # solving frame = Gamma_t itself
    # implementer for th_t: per-pair reflection angles
    units_t = []
    ok_units = True
    for p in range(8):
        B = th_t[2 * p:2 * p + 2, 2 * p:2 * p + 2]
        ang = 0.5 * math.atan2(B[0, 1] + B[1, 0],
                               B[0, 0] - B[1, 1])
        # B = cos2a X + sin2a Z? recover a from B = 2uu^T - I
        lam, W = np.linalg.eigh(B)
        u2 = W[:, int(np.argmax(lam))]
        u = np.zeros(16)
        u[2 * p:2 * p + 2] = u2
        units_t.append(u)
        ok_units &= abs(np.max(lam) - 1.0) <= 1e-10
    V_tht = householder_refl_impl(units_t, gs, P_par)
    units_g = []
    for p in range(8):
        B = Gam_t[2 * p:2 * p + 2, 2 * p:2 * p + 2]
        lam, W = np.linalg.eigh(B)
        u2 = W[:, int(np.argmax(lam))]
        u = np.zeros(16)
        u[2 * p:2 * p + 2] = u2
        units_g.append(u)
    V_Gt = householder_refl_impl(units_g, gs, P_par)
    wd_t = max(impl_ward(V_tht, th_t, gs), impl_ward(V_Gt, Gam_t, gs))
    r_trans = tomita_residual(V_tht @ V_Gt, gset_rho, rho_h)
    r_untrans = tomita_residual(
        frame_impl(np.pi / 4, np.pi / 4) @ V_Gt, gset_rho, rho_h)
    check("P3.4 COVARIANCE (CCXXI law): M(g h g^T) = g M g^T "
          "(%.1e <= 1e-10); with the TRANSPORTED grading the census "
          "zero sits at the TRANSPORTED frame (implementer wards "
          "%.1e; residual %.1e <= 1e-9) and the untransported "
          "candidate FAILS (%.4f >= %.2f): the pinning transports "
          "1:1 -- jointly covariant, NO absolute selection, the "
          "compiler-freedom theorem honored"
          % (cov_law, wd_t, r_trans, r_untrans, COMP_FLOOR),
          cov_law <= ZTOL and ok_units and wd_t <= EQ_TOL
          and r_trans <= EQ_TOL and r_untrans >= COMP_FLOOR,
          kill="K3")

    # (e) the preference anatomy (flow-reversal defect)
    hd = packs["DEP"]["h"]
    c_int_pred = 16 * n_i2_int
    dev_form = 0.0
    dmins = []
    for dl in DELTA_GRID:
        th = theta_cell(0.0, dl)
        D2 = float(np.linalg.norm(th @ hd @ th + hd) ** 2)
        pred = T_DEP ** 2 * (c_int_pred + 120.0
                             * (1.0 + math.cos(2 * dl)))
        dev_form = max(dev_form, abs(D2 - pred))
        dmins.append(D2)
    i_min = int(np.argmin(dmins))
    gam_inv = 0.0
    for gl in (0.0, 0.3, np.pi / 5):
        for dl in (DELTA_GRID[0], DELTA_GRID[7]):
            th = theta_cell(gl, gl + dl)
            D2 = float(np.linalg.norm(th @ hd @ th + hd) ** 2)
            pred = T_DEP ** 2 * (c_int_pred + 120.0
                                 * (1.0 + math.cos(2 * dl)))
            gam_inv = max(gam_inv, abs(D2 - pred))
    check("P3.5 PREFERENCE ANATOMY: D(delta)^2 = t^2 (c_int + 120 "
          "(1 + cos 2 delta)) EXACT with c_int = %d = 16 x %d "
          "I2-interior edge-slots (residual %.1e <= 1e-10; gamma-"
          "invariance %.1e <= 1e-10); argmin at delta = -pi/2 "
          "(index %d == 0, the INTEGER class -- the CCXXXIII deg-2 "
          "argmin class); floor c_int > 0: the CCXXXIII preference "
          "is theta-RELATIVE flow-reversal anatomy, NOT a J_Omega "
          "selection (J commutes with the flow, P1.2)"
          % (c_int_pred, n_i2_int, dev_form, gam_inv, i_min),
          dev_form <= ZTOL and gam_inv <= ZTOL and i_min == 0
          and c_int_pred > 0, kill="K3")

    # (f) natural-cone Gram wiring-blindness
    def wiring_variant(u2):
        Av = A_int.astype(np.float64).copy()
        Av[np.ix_(range(10), range(10, 16))] = 0.0
        Av[np.ix_(range(10, 16), range(10))] = 0.0
        for i in range(5):
            for s in range(3):
                r0, c0 = 2 * i, 10 + 2 * s
                Av[r0:r0 + 2, c0:c0 + 2] = u2
                Av[c0:c0 + 2, r0:r0 + 2] = -u2.T
        return Av

    ward_I = float(np.max(np.abs(wiring_variant(-I2) - Aint_f)))
    monos_1p = [gs[a] for a in range(16)]
    monos_d2 = [gs[p] @ gs[q] for p in range(16)
                for q in range(p + 1, 16)]
    blind = []
    for wname, u2 in (("pure-I", -I2), ("pure-J", -J2),
                      ("ray(4/5,3/5)", -(0.8 * I2 + 0.6 * J2))):
        hV = -(Adep_f + T_DEP * wiring_variant(u2))
        HFv = quad_op(hV, gs)
        rho_v, wv, Vv, pv = gibbs(HFv, BETA_DEP)
        Rv = (Vv * np.sqrt(pv)) @ Vv.conj().T
        rep = []
        for monos in (monos_1p, monos_d2):
            n_m = len(monos)
            Mst = np.array([m.ravel() for m in monos])
            Xst = np.array([(Rv @ m.conj().T @ Rv).T.ravel()
                            for m in monos])
            G = Mst @ Xst.T
            herm = float(np.linalg.norm(G - G.conj().T)) \
                / max(float(np.linalg.norm(G)), 1e-30)
            emin = float(np.min(np.linalg.eigvalsh(
                (G + G.conj().T) / 2)))
            scale = float(np.max(np.abs(G)))
            rep.append((herm, emin, scale))
        blind.append((wname, rep))
    ok_blind = all(h1 <= ZTOL and e1 >= -ZTOL * max(s1, 1.0)
                   for _n, rp in blind for (h1, e1, s1) in rp)
    print("      natural-cone Grams (herm dev / eigmin), all "
          "wirings:")
    for wname, rp in blind:
        print("        %-14s 1p: %.1e / %+.1e   deg2: %.1e / %+.1e"
              % (wname, rp[0][0], rp[0][1], rp[1][0], rp[1][1]))
    check("P3.6 STRICT HERMITICITY IS WIRING-BLIND AT THE MODULAR "
          "REFLECTION: the natural-cone Gram is Hermitian and PSD "
          "IDENTICALLY at pure-I, pure-J and the (4/5,3/5) ray "
          "(deployed-wiring rebuild ward %.1e == 0): no wiring "
          "discrimination from J_Omega" % ward_I,
          ok_blind and ward_I == 0.0, kill="K3")

    # ==================================================================
    section("C -- controls (must fire; RNG declared)")
    # ==================================================================
    # C1 non-quasi-free state
    psi = rng.normal(size=dim) + 1j * rng.normal(size=dim)
    psi /= np.linalg.norm(psi)
    rho_p = 0.9 * packs["DEP"]["rho"] + 0.1 * np.outer(psi,
                                                       psi.conj())
    wp, Vp = np.linalg.eigh((rho_p + rho_p.conj().T) / 2)
    rho_ph = (Vp * np.sqrt(np.clip(wp, 1e-300, None))) @ Vp.conj().T
    A1pp = np.zeros((16, 16))
    for a in range(16):
        for b in range(16):
            A1pp[a, b] = np.imag(np.sum((rho_p @ gs[a]).T * gs[b]))
    G16p = np.eye(16) + 1j * A1pp
    Yp = np.zeros((16, 16), dtype=complex)
    for b in range(16):
        RbR = rho_ph @ gs[b] @ rho_ph
        for a in range(16):
            Yp[b, a] = np.sum(RbR.T * gs[a])
    Cp = np.linalg.solve(G16p, Yp)
    span_p = 0.0
    for a in range(16):
        lhs = rho_ph @ gs[a]
        fit = sum(Cp[b, a] * gs[b] for b in range(16)) @ rho_ph
        span_p = max(span_p, float(np.linalg.norm(lhs - fit)))
    pk = packs["DEP"]
    ratio_dep = np.sqrt(np.outer(pk["p"], 1.0 / pk["p"]))
    mis = 0.0
    for a in range(3):
        x = gs[a] @ rho_ph
        lhs = (pk["V"] @ ((pk["V"].conj().T @ x @ pk["V"])
                          * ratio_dep) @ pk["V"].conj().T).conj().T
        mis = max(mis, float(np.linalg.norm(lhs - gs[a] @ rho_ph)))
    check("C1 FIRES: non-quasi-free state (seeded psi, eps = 0.1): "
          "one-particle closure BREAKS (out-of-span %.4f >= %.3f) "
          "and the mismatched Tomita relation breaks (%.4f >= %.2f)"
          % (span_p, C1_SPAN, mis, C1_TOMITA),
          span_p >= C1_SPAN and mis >= C1_TOMITA, kill="K7")

    # C2 wrong beta
    rho_2, w2, V2, p2 = gibbs(packs["DEP"]["HF"], 2.0)
    rho_2h = (V2 * np.sqrt(p2)) @ V2.conj().T
    mis2 = 0.0
    for a in range(3):
        x = gs[a] @ rho_2h
        lhs = (pk["V"] @ ((pk["V"].conj().T @ x @ pk["V"])
                          * ratio_dep) @ pk["V"].conj().T).conj().T
        mis2 = max(mis2, float(np.linalg.norm(lhs - gs[a] @ rho_2h)))
    muX, _QX = np.linalg.eigh(1j * packs["DEP"]["h"])
    l1 = float(np.linalg.norm(0.5 * muX))
    l2 = float(np.linalg.norm(1.0 * muX))
    ratio_beta = l2 / l1
    check("C2 FIRES: wrong-beta state (beta' = 2 vs beta = 1 "
          "objects): mismatched Tomita residual %.4f >= %.2f; the "
          "reading shifts EXACTLY: ||log M(2)||/||log M(1)|| = "
          "%.10f == 2 +- 1e-8"
          % (mis2, C2_TOMITA, ratio_beta),
          mis2 >= C2_TOMITA and abs(ratio_beta - 2.0) <= 1e-8,
          kill="K7")

    # C3 scrambled dressing
    Qs, _ = np.linalg.qr(rng.normal(size=(10, 10)))
    Xd = np.imag(logM[cr])
    Xs = Qs @ Xd
    corr_s = float(np.sum(Xs * Aint_f[cr])
                   / max(np.linalg.norm(Xs)
                         * np.linalg.norm(Aint_f[cr]), 1e-30))
    check("C3 FIRES: seeded scrambled dressing kills the wiring "
          "correlation: |corr| = %.4f <= 0.5 (truth 1.0)"
          % abs(corr_s), abs(corr_s) <= 0.5, kill="K7")

    # C4 grading impostors (== P3.2 rotation branch, restated as fire)
    check("C4 FIRES: rotation-type gradings (deck powers, parity) "
          "admit NO frame solution (min distance %.3f >= 1): the "
          "reflection/rotation dichotomy is non-vacuous" % rot_min,
          rot_min >= 1.0, kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    pure_pass = any(v <= EQ_TOL for v in pure_res.values())
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "K1" in KILLS or "K2" in KILLS:
        VERDICT = "MODULAR-MACHINERY-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "COMPARISON-BROKEN"
    elif pure_pass:
        VERDICT = "MODULAR-FRAME-SELECTS-ABSOLUTE(unexpected)"
    else:
        VERDICT = ("MODULAR-FRAME-SELECTS-RELATIVE(delta* = 0 rel. "
                   "deployed sheet grading -> theta_S class -> "
                   "pure-(+-J) ray) x OFF-FAMILY-AS-ELEMENT(J = "
                   "Theta_0 x positive KMS dressing; equidistant "
                   "sqrt(32) from the whole circle) x JOINTLY-"
                   "COVARIANT(no absolute selection; compiler-"
                   "freedom theorem unmoved)")
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    if VERDICT.startswith("MODULAR-FRAME-SELECTS-RELATIVE"):
        print("""
FROZEN EDITORIAL CONSEQUENCE: frame-fixed wiring sentences in
ABSOLUTE form (e.g. "strict collar RP selects pure-J") are
representative-dependent gauge commentary and leave the main text;
the stateable physics form is SHEET-RELATIVE: "relative to the
deployed sheet grading, the seam state's own modular conjugation
pins the theta_S frame class (delta* = 0, beta-rigid), whose
frozen selection-map ray is pure-(+-J); the deployed pure-I wiring
is the g_int gauge transport of that ray; absolutely, J_Omega =
Theta_0 x positive KMS dressing pins no frame and the
compiler-freedom theorem stands." """)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE MODULAR CONJUGATION: computed exactly on the finite GNS
    space (standard form on HS(C^256)) for the deployed seam-cell
    KMS state AND the CCXV quasi-free parent; all Tomita wards
    pass; one-particle action j1 = M o Theta_0 with the POSITIVE
    KMS dressing M = exp(+i (beta/2) h) -- measured by Gram
    inversion, matched to the closed form.
  * THE COMPARISON: as an element, J_Omega is OFF the frame circle
    (polar factor = identity = the gauge-invariant real structure
    Theta_0; equidistant sqrt(32) from every frame); the CCXXXIII
    polar off-family finding is the dressing's odd-function shadow
    (dressing-wiring corr == 1 exact vs KMS corr 0.9999967); the
    CCXXXIII preference argmin is the exact flow-reversal anatomy
    t^2 (c_int + 120 (1 + cos 2 delta)) -- theta-relative, not a
    J_Omega selection.  RELATIVE to the deployed sheet grading the
    Fock census pins delta* = 0 (the theta_S class) uniquely and
    beta-rigidly; the frozen selection map names the pure-(+-J)
    ray; the pinning transports 1:1 with the grading convention
    (CCXXI covariance): jointly covariant, no absolute selection.
  * WHAT REMAINS ANALYTIC (typed): the half-sided/Bisognano-
    Wichmann geometric conjugation of a true collar inclusion
    (continuum limit), OS reconstruction, net existence -- all
    open, untouched; the sheet grading is deployment lineage
    (v109/round-58), not compiler output.  NO marker moves.
    NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
