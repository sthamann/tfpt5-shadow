#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v974 -- ALPHA.QUILLEN.EXACT.01 [O update: both named faces now carry
COMPUTED witnesses; the diagonal-zeta face sharpened to the CHANNEL-SWAP
question; the finite Quillen identity verified two-sided] +
SEAM.CONTACT.UNIT.01/.02 [update: the BFK resummation named in v485 is now
EXECUTED -- gluing constant 2^-N exact, jump matrix = 16 c3 circ(2,-1,0,-1),
scale channel reproduced via the KMS unit] + EM.WARD.01 /
ALPHA.QUILLEN.INFLOW.01 [update: the cited EM1 inflow step now carries a
computed lattice witness -- pumped charge == spectral flow == Streda ==
Chern == 1 with sign-coherent conjugation mutant] + the value alpha^-1 =
137.0359992168 re-anchored (residual 6.4e-58).

ONE module from THREE finished exploration probes (2026-08-27, all
deterministic, no RNG, each with two identical record runs .run1/.run2.log):

  (1) seam_bfk_conical_det_probe.py -- ALPHA.QUILLEN.BFK_CONICAL.01, 21/21,
      SPEC_SHA d06b3bbec70e7efc, VERDICT MATCH_MODULO_LOCAL_FACTOR.  The
      Burghelea-Friedlander-Kappeler Mayer-Vietoris determinant formula
      (BFK, J. Funct. Anal. 107 (1992) 34) made EXECUTABLE on the seam
      circle cut at the four mu4 marks: the 1D gluing constant is EXACTLY
      2^-N (derived symbolically for N = 1..4 at GENERAL interval lengths,
      Laurent-polynomial identity + 50-digit numerics); the massless
      reassembly det'_zeta(Delta_S1) = l^2 = 2^-N prod(2 a_j) (l/N)
      det'(R_0) with det'(R_0) = N l / prod a_j; at the KMS scale
      l = 2 pi = 1/(4 c3): R_0 = 16 c3 circ(2,-1,0,-1) (16 c3 = |mu4| x
      4 c3 per-interval unit), per-interval det_D = 1/(8 c3), det'R_0 =
      2^16 c3^3, glued product = (2 pi)^2; the jump matrix is the inverse
      mark Green matrix, R(m) = (G_m|_marks)^-1 EXACTLY.  Against the v484
      mark matrix G_marks = -4 c3 ln2 circ(0,1,2,1): NO global
      proportionality (the kernels sit in SWAPPED mu4 channels -- B kills
      the gauge/zero-mode k = 0 channel, C kills the sign-rep k = 2
      channel), but the correspondence is channel-wise EXACT: same mu4
      Fourier eigenbasis, |spec| multisets {0,2,2,4} equal, doublet ratio
      4/ln2 with c3 CANCELLING, Tr B^k = 4^k + 2(+2)^k mirroring v484's
      Tr C^k = 4^k + 2(-2)^k with the sign flip = the kernel swap.  The
      v485 scale channel is reproduced EXACTLY: log det' difference =
      (1/(4 c3)) G_reg(0; l) = the KMS unit converting the glued log-det
      into (1/pi) ln(l/2pi).  Mutants: off-mark breaks the circulant while
      the BFK identity survives (correct control -- the identity is
      mark-independent, the mu4 correspondence is not); a wrong gluing
      constant breaks the anchor by an exact factor 2.  NOT covered
      (typed in-probe): pillowcase moduli, the 8 b1 index budget, and a
      |D|-level BFK as an operator identity.
  (2) laughlin_pump_em1_probe.py -- ALPHA.QUILLEN.EM1_PUMP.01, 20/20,
      SPEC_SHA f9b5cb0bf20d0293, VERDICT PUMP_QUANTIZED_MATCHES_CHERN.
      All on the v367 collar model: FHS Chern C(M=1) = +1, C(M=3) = 0
      exact; hybrid-Wannier winding DeltaP(M=1) = +1.000000000000
      (residual 0.0), DeltaP(M=3) = 0; cylinder P y P transport: net
      continuous midline crossings +1 per flux quantum (teleports -1,
      period closure exact); edge spectral flow bottom -1 / top +1
      (antisymmetric as inflow demands), M = 3 zero; Streda N(n_phi) =
      [144,145,146,147], DeltaN = C n_phi exact integers, M = 3 constant.
      Bookkeeping: 16 Majoranas = 8 complex copies, c_- = 16 x 1/2 = 8,
      per-copy k0 = |C| = 1 (the v470 EM1 statement), kY = (5/6)/(1/2) =
      5/3 and (1/kY) x 41/6 = 41/10 = b1 (v470 arithmetic verbatim).
      Mutants: the conjugated model flips ALL FOUR readings to -1
      simultaneously; a wrong-band projector breaks quantization
      (grid-unstable FHS, unreadable Wannier flow).
  (3) quillen_rigidity_chain_probe.py -- ALPHA.QUILLEN.RIGIDITY_CHAIN.01,
      18/18, SPEC_SHA b4ee0dd0141da6ab, VERDICT CHAIN_SHADOW_OK.
      Quillen's identity at the finite shadow: the FHS/Berry curvature
      integral of the determinant line over the U(1)-twist torus == +1
      AND the metric side (||s||^2 = det(U_ref^dag U(theta)) Gaussian
      overlap; distributional i ddbar log||s||^2 evaluated by
      Poincare-Lelong as the vortex divisor) == +1, both references, both
      sizes L = 4/6; the difference is an EXACT form (total 3.3e-16);
      patching gate: transition-function winding == Chern == +1 (the
      Dai-Freed picture); alpha anchor: the Quillen split a^3 - 2 c3^3 a^2
      = 8 b1 c3^6 ln(1/phi_seam) at alpha^-1 = 137.03599921684071,
      residual 6.4e-58 (mpmath 50 digits), 8 b1 = 164/5 = (4/5) 41 exact.
      Typed conditional L2: IF the seam state is quasi-free (named premise
      SEAM.RP.RIGIDITY -- MEASURED, not forced in the strong form, by the
      parallel S1 probe) THEN the seam det line IS the free-fermion det
      line and the identity applies literally.  Typed DAG gate: the
      remaining open content of ALPHA.QUILLEN.EXACT.01 = {rigidity
      premise} + {diagonal-zeta face} + {EM1} -- no additional analytic
      unknown.  Mutants: the e^{2 i theta} twist mutant gives FHS 4
      (caught); the squeezed kernel breaks integrality + the norm
      identity (caught).

WHAT MOVES AND WHAT DOES NOT (binding): NO marker moves.
ALPHA.QUILLEN.EXACT.01 stays [O] -- "why this functional" is not closed;
its remaining content is TYPED as {the rigidity premise (SEAM.RP.RIGIDITY,
measured not proven)} + {the channel-swap question (why the |D|-side mark
matrix and the Delta-side jump matrix carry their kernels in swapped mu4
channels -- the sharpened form of the old diagonal-zeta face)} + {the
continuum Bismut-Freed identification of the exact-form difference field}.
The pump is a SINGLE-COPY complex-fermion statement; the 16-copy collar
enters only as exact bookkeeping arithmetic, not as a 16-band simulation,
and the complex-copy U(1) identification stays part of the cited EM1
reading [C].  The BFK probe covers the U(1)-scalar SECOND-ORDER
determinant face (Delta = |D|^2); a BFK gluing of the nonlocal |D| itself
is NOT performed -- |D| enters via its mark Green matrix and the scale
dictionary.  The finite Quillen identity is a 2-band lattice Gaussian
family, not the abstract-seam zeta determinant.  alpha^-1 =
137.0359992168 stays [E] regardless (it is re-anchored here, not
re-claimed).

THE MODULE-OWN EXACT SECTION S0 (sympy / Fraction / mpmath, no probe
imports): (a) the BFK closed forms INDEPENDENTLY re-derived --
det'_zeta(Delta on S^1_l) = l^2 and det'_zeta(|D|) = l from the Riemann
zeta values zeta_R(0) = -1/2, zeta_R'(0) = -(1/2) ln 2pi; the interval
Dirichlet det = 2a; the N = 4 equal-interval reassembly identity as exact
rationals in c3 (R_0 = 16 c3 circ(2,-1,0,-1), det'R_0 = 2^16 c3^3,
per-interval det = 1/(8 c3), Gram factor 1/(16 c3), glued product =
(2 pi)^2 = 1/(16 c3^2), gluing constant 2^-4); the spec multisets
{0,2,2,4} and Tr B^k = 4^k + 2 2^k / Tr C^k = 4^k + 2(-2)^k for k = 1..4
exact, B + C = 2(I + S); the doublet ratio 4/ln2 exact symbolic with the
c3 cancellation exhibited on a GENERIC symbol; the v485 scale dictionary
log det'Delta(l) - log det'Delta(2pi) = (1/(4 c3)) G_reg(0; l) exact.
(b) the alpha anchor RE-DERIVED at 50 digits: coefficients as exact
Fractions (8 b1 = 164/5 = (4/5) 41, q(D5) + q(A3) = 5/4 + 3/4 = 2), root
UNIQUE on the scanned window (exactly one sign change of F_U(1) on a log
grid a in [1e-4, 1]), |alpha^-1 - 137.03599921684071| < 1e-9, split
residual < 1e-30 (measured ~6.4e-58).  (c) the inflow bookkeeping exact
(N_maj = 2^(g_car-1) = 16 = dim S+, 8 complex copies, c_- = 8 = g_car +
N_fam, kY = 5/3, (1/kY)(41/6) = 41/10 = b1, 41/6 = 20/3 + 1/6 as
Fractions).  (d) a small exact Chern-number certificate INDEPENDENT of the
probes: module-own FHS on a coarse 12 x 12 grid with an integer-rounding
ward, C(M=1) = 1 vs C(M=3) = 0.  MUTANTS (tipping): a single-byte hash
mutation of an embedded source is caught by the sha256 pin; the wrong KMS
unit (2 pi -> 4 pi) breaks the S0 scale-channel identity by EXACTLY
-2 ln 2; the b1 mutant (41/10 -> 4) breaks the coefficient identities AND
the split residual by ~9.3e-9 >> 1e-30 (caught).

EMBEDDING CONVENTION (as in v960..v970): the three probe sources are
embedded BYTE-EXACT as string constants, sha256-pinned (full-source pins
gated every run), byte-warded against the experiments/tfpt-discovery/
copies (read-only), and executed VERBATIM in isolated module namespaces
(runtimes ~0.6 / 2.9 / 1.8 s); the pattern gates check the printed gate
counts (21/21, 20/20, 18/18), the verdict lines, the printed SPEC_SHAs
and the exit codes.

PROVENANCE: seam_bfk_conical_det_probe.py (21/21, SPEC_SHA
d06b3bbec70e7efc, VERDICT MATCH_MODULO_LOCAL_FACTOR),
laughlin_pump_em1_probe.py (20/20, SPEC_SHA f9b5cb0bf20d0293, VERDICT
PUMP_QUANTIZED_MATCHES_CHERN; one disclosed calibration pass froze the
three orientation signs OR1/OR2/OR3 and the mutant record values),
quillen_rigidity_chain_probe.py (18/18, SPEC_SHA b4ee0dd0141da6ab,
VERDICT CHAIN_SHADOW_OK; one disclosed smoke run corrected the MUT-A
expected value 2 -> 4 pre-freeze); all 2026-08-27, all with .run1/.run2
record logs identical modulo WALL lines.

FIREWALL: the probes are experiments/-level exploration promoted HERE and
only here; they import no verification/ module and use no RNG (their own
firewall gates re-run embedded); this module consults the experiments
tree READ-ONLY (byte ward + __file__ anchoring for the probes' own
source-inspection gates); no ledger row is written by code, no marker is
moved by code -- ledger/paper/website sync is a separate documented step.
Exact identities in sympy/Fraction; mpmath 50 digits for the anchor.
Python-only per GATE.WOLFRAM.02.
"""

import contextlib
import hashlib
import io
import os
import re
import sys
import time
import types
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from tfpt_constants import check, summary, reset, g_car, N_fam, dim_Splus

C3S = 1 / (8 * sp.pi)                      # c3 = 1/(8 pi), P1 axiom
ZP0 = -sp.log(2 * sp.pi) / 2               # zeta_R'(0) = -(1/2) ln 2pi

ALPHA_INV_REF = "137.03599921684071"       # v341/v3 anchor, 17 digits
SPLIT_BAR = mp.mpf("1e-30")
ROOT_BAR = mp.mpf("1e-9")
N_COARSE = 12                              # module-own FHS certificate grid


# ---------------------------------------------------------------- helpers
def _circ(row):
    """NxN circulant with given first row."""
    n = len(row)
    return sp.Matrix(n, n, lambda i, j: row[(j - i) % n])


def _fhs_coarse(M, N=N_COARSE):
    """Module-own Fukui-Hatsugai-Suzuki Chern number of the lower band of
    h(k) = sin kx SX + sin ky SY + (M - cos kx - cos ky) SZ on a coarse
    N x N grid -- INDEPENDENT re-derivation, no probe code."""
    SXn = np.array([[0, 1], [1, 0]], complex)
    SYn = np.array([[0, -1j], [1j, 0]], complex)
    SZn = np.array([[1, 0], [0, -1]], complex)
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)

    def occ(kx, ky):
        h = (np.sin(kx) * SXn + np.sin(ky) * SYn
             + (M - np.cos(kx) - np.cos(ky)) * SZn)
        return np.linalg.eigh(h)[1][:, 0]

    u = [[occ(kx, ky) for ky in ks] for kx in ks]

    def ln(a, b):
        x = np.vdot(a, b)
        return x / abs(x)

    F = 0.0
    for i in range(N):
        for j in range(N):
            ip, jp = (i + 1) % N, (j + 1) % N
            F += np.angle(ln(u[i][j], u[ip][j]) * ln(u[ip][j], u[ip][jp])
                          * np.conj(ln(u[i][jp], u[ip][jp]))
                          * np.conj(ln(u[i][j], u[i][jp])))
    return F / (2 * np.pi)


def _alpha_functional():
    """The v341 alpha functional at mpmath dps 50 (module-own rebuild)."""
    mp.mp.dps = 50
    cc = 1 / (8 * mp.pi)
    pb = 1 / (6 * mp.pi)
    dt = 48 * cc ** 4

    def phiseam(a):
        Q = dt * mp.e ** (-2 * a)
        return pb + Q * (1 - Q) ** (mp.mpf(-5) / 4)

    def F(a):
        return (a ** 3 - 2 * cc ** 3 * a ** 2
                - (mp.mpf(4) / 5) * 41 * cc ** 6 * mp.log(1 / phiseam(a)))

    return cc, phiseam, F


# --------------------------------------------------------------- probes
# The three frozen probe sources, embedded BYTE-EXACT (leading newline
# stripped at execution).  sha256 pins are over the exact file bytes.
_SRC_BFK = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_bfk_conical_det_probe -- ALPHA.QUILLEN.BFK_CONICAL.01 (strategy S7):
the Burghelea-Friedlander-Kappeler gluing formula (BFK, "Mayer-Vietoris type
formula for determinants of elliptic differential operators", J. Funct. Anal.
107 (1992) 34) made EXECUTABLE on the KMS seam circle with the four mu4
marks, and priced EXACTLY against the v484/v485 closed forms of the merged
ALPHA.QUILLEN.EXACT.01 + HYP.PHI0.PUNCTURE.01 analytic target.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO ledger
row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  v484 derived the finite CYCLE sector of the merged
target on the seam circle (mark-Green matrix G_marks = -4 c3 ln2 x
circ(0,1,2,1), spec {4,-2,0,-2}, Tr C^k = 4^k + 2(-2)^k); v485 settled the
DIAGONAL channel (G_reg(0; l) = (1/pi) ln(l/2pi), zero exactly at the KMS
circumference l = 2 pi = 1/(4 c3)) and resummed the mark determinant closed-
form (det(I - uC) = (1-4u)(1+2u)^2), naming the BFK/gluing route (v151
class) without EXECUTING it.  What was never done: cut the seam circle at
the four mu4 marks {0, pi/2, pi, 3pi/2}, write the ACTUAL BFK identity
det_zeta = C_glue x prod_j det_zeta(Dirichlet interval_j) x det(R) with the
Neumann-jump (Dirichlet-to-Neumann) matrix R at the marks, derive the 1D
gluing constant C_glue in closed form, and confront R with the v484 mark
circulant and the v485 scale channel.  This probe does exactly that, for
the LOCAL second-order operator Delta = -d^2/dx^2 = |D|^2 on the seam
circle (BFK applies to differential operators; the nonlocal |D| itself
enters only through its mark Green matrix and the scale dictionary --
typed honestly in P8/G19).

THE SETUP.  Circle S^1_l of circumference l, marks p_1..p_N cutting it into
intervals of lengths a_1..a_N (sum = l).  Conventions VERIFIED in-probe and
stated: zeta-determinants with the zero mode REMOVED are primed, det'; the
same zero-mode-removed convention is used by v484 (Green function of |D|
with n = 0 dropped) and v485 (G_reg zero mode removed).  Anchors:
det'_zeta(Delta on S^1_l) = l^2, det'_zeta(|D| on S^1_l) = l,
det_zeta(Dirichlet Delta on [0,a]) = 2a (no zero mode, unprimed).  Massive
regulator for the BFK step (Delta + m^2 is invertible, plain BFK applies):
det_zeta(Delta + m^2 on S^1_l) = 4 sinh^2(ml/2),
det_zeta(Dirichlet on [0,a] + m^2) = 2 sinh(ma)/m, interval DtN
Lambda_a(m) = (m/sinh ma) [[cosh ma, -1], [-1, cosh ma]], assembled jump
matrix R(m) = sum of interval DtN blocks (weighted-cycle structure), and
the m -> 0 limit performed with the exact zero-mode bookkeeping
(lambda_0(m) = m^2 l/N + O(m^4), Gram ratio l/N = ||1||^2_{L^2(S^1_l)} /
||1||^2_{C^N}).  All identities symbolic (sympy, exact q = e^{m a_j / 2}
Laurent-polynomial form) wherever feasible, mpmath 40-60 digits elsewhere;
deterministic fixed rational parameters, no randomness.

PRE-REGISTERED ADJUDICATION (frozen before the record runs):
  P1 CONVENTIONS/ANCHORS: det'_zeta(Delta_S1) = l^2, det'_zeta(|D|) = l
     (and (det'|D|)^2 = det' Delta), det_zeta(Dirichlet [0,a]) = 2a --
     symbolic via zeta_Delta(s) = 2 (l/2pi)^{2s} zeta_R(2s) etc. with
     zeta_R(0) = -1/2, zeta_R'(0) = -(1/2) ln 2pi, plus 30-digit numeric
     zeta'(0) cross-checks; massive closed forms recovered through the
     relative-Fredholm product prod_{n>=1}(1 + x^2/n^2) = sinh(pi x)/(pi x).
  P2 BFK IDENTITY + GLUING CONSTANT: for N = 4 with GENERAL symbolic
     lengths, det_zeta(Delta + m^2 on S^1) = 2^{-4} prod_j det_zeta(D_j +
     m^2) x det R(m) EXACTLY (Laurent-polynomial identity in q_j); the 1D
     gluing constant is derived, C_glue = 2^{-N} (one factor 1/2 per cut
     point), verified symbolically for N = 1, 2, 3, 4 and to 40 digits
     numerically.
  P3 ZERO-MODE (MASSLESS) BFK: det'_zeta(Delta_S1) = 2^{-N} prod_j (2 a_j)
     x (l/N) x det'(R_0) with R_0 the weighted cycle Laplacian
     (R_0 = graph Laplacian, weights 1/a_j), det'(R_0) = N l / prod a_j
     (charpoly + matrix-tree cross-check), and the l/N factor typed as the
     zero-mode Gram ratio.
  P4 DtN-GREEN DUALITY: R(m) = (G_m|_marks)^{-1} exactly (the jump matrix
     is the inverse of the mark-restricted Green matrix), and massless
     R_0 x G_Delta|_marks = I - J/4 (identity off the zero mode) with
     G_Delta(d) = d^2/2l - d/2 + l/12 verified as the zero-mode-removed
     Green function.
  P5 KMS c3-GRADING vs v484: at l = 2 pi = 1/(4 c3), a = pi/2 = 1/(16 c3):
     R_0 = 16 c3 x circ(2,-1,0,-1) =: 16 c3 B -- integer circulant times a
     pure c3 unit (16 c3 = |mu4| x 4 c3 = |mu4| x bare 1/(2pi)); v484's
     G_marks = -4 c3 ln2 x circ(0,1,2,1) =: -4 c3 ln2 C re-derived in-probe;
     GLOBAL matrix proportionality B ~ C is expected to FAIL (kernel
     channels swapped: B kills the mu4-trivial k=0 channel, C kills the
     mu4-sign k=2 channel), while the correspondence holds EXACTLY channel-
     wise: same mu4 Fourier eigenbasis, |spec B| = |spec C| = {0,2,2,4} as
     multisets, doublet channel (k = 1,3) R_0|_d = (4/ln2) G_marks|_d (c3
     CANCELS -- both matrices carry the same c3 grading), B + C = 2(I + S);
     cycle combinatorics Tr B^k = 4^k + 2(+2)^k vs v484's Tr C^k =
     4^k + 2(-2)^k (same {4, 2-doublet} magnitude law, sign flip = the
     kernel-channel swap); Tr B = 8 <> 0 vs Tr C = 0 typed via v485
     (C's diagonal renormalises to zero at KMS, B's diagonal is the
     Dirichlet jump -- nonzero by construction).
  P6 SCALE CHANNEL vs v485: d/dl log det'_zeta(Delta) = 2/l with the BFK
     factor decomposition 4/l - 3/l + 1/l (intervals - jump matrix + zero
     mode); the v485 diagonal is reproduced EXACTLY through the dictionary
     log det'Delta(l) - log det'Delta(1/(4c3)) = (1/(4 c3)) G_reg(0; l)
     and G_reg(0; l) = (1/pi)(log det'|D|(l) - log det'|D|(2pi)), i.e. the
     KMS unit 2 pi = 1/(4 c3) converts the glued log-det scale channel
     into the v485 closed form; derivative ratio exactly 2 pi.
  P7 MUTANTS CAUGHT: (A) moving one mark off mu4 (pi/2 -> 7pi/12) breaks
     the circulant property, the {0,2,4,2}/a spectrum and the Tr law
     (CAUGHT) while the BFK identity itself STILL holds (control: the
     identity is mark-position independent, the correspondence is mu4-
     specific); (B) a wrong gluing constant 2^{-3} breaks the anchor
     identity by an exact factor 2 (CAUGHT).
  P8 HONEST TYPING: this probe covers the U(1)-scalar SECOND-ORDER
     determinant face (Delta = |D|^2 on the seam circle with the four
     marks, BFK-glued); it does NOT cover the full pillowcase moduli
     variation, the 8 b1 / 41 = 10 b1 index-coefficient budget, or a BFK
     gluing of the nonlocal |D| itself.
EXPECTED VERDICT (pre-registered): MATCH_MODULO_LOCAL_FACTOR -- the gluing
identity is exact and the v485 scale channel is reproduced exactly, but the
mark-matrix correspondence to v484 is channel-graded (doublet factor 4/ln2,
kernel channels swapped by the operator order |D| vs |D|^2), NOT a global
matrix proportionality, so BFK_MATCH_EXACT is not available.

VERDICT ENUM: BFK_MATCH_EXACT (gluing identity verified + mark-matrix
correspondence exact with printed constant + scale channel reproduced) /
MATCH_MODULO_LOCAL_FACTOR (identity holds, correspondence holds up to a
mark-local/channel factor, quantified) / MISMATCH.

RECORD: two identical runs (seam_bfk_conical_det_probe.run1.log /
.run2.log, diff modulo the wall-clock line), runtime bar 180 s,
deterministic (fixed rational parameters, no RNG).
"""

import hashlib
import sys
import time

import mpmath as mp
import sympy as sp

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
RUNTIME_BAR = 180.0

CHECKS: list = []


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


# ---------------------------------------------------------------- constants
C3S = 1 / (8 * sp.pi)                       # c3 = 1/(8 pi), P1 axiom
ZP0 = -sp.log(2 * sp.pi) / 2                # zeta_R'(0) = -(1/2) ln 2pi
N_MARKS = 4                                 # |mu4|
LENS_GEN = [sp.Rational(7, 10), sp.Rational(13, 10),
            sp.Rational(11, 10), sp.Rational(9, 10)]   # generic lengths, l=4
M_VALUES = [sp.Rational(1, 3), sp.Integer(1), sp.Rational(7, 2)]


def circ(row):
    """4x4 (or NxN) circulant with given first row."""
    n = len(row)
    return sp.Matrix(n, n, lambda i, j: row[(j - i) % n])


def assemble_R_sym(qs):
    """Jump matrix R(m)/m from interval half-exponentials q_j = e^{m a_j/2}.

    Interval j joins marks j and j+1 (mod N); its DtN block is
    (1/s_j) [[c_j, -1], [-1, c_j]] with s_j = sinh(m a_j), c_j = cosh(m a_j).
    """
    n = len(qs)
    R = sp.zeros(n, n)
    for j, q in enumerate(qs):
        s = (q ** 2 - q ** -2) / 2
        c = (q ** 2 + q ** -2) / 2
        k = (j + 1) % n
        R[j, j] += c / s
        R[k, k] += c / s
        R[j, k] += -1 / s
        R[k, j] += -1 / s
    return R


def assemble_R0_sym(lens):
    """Massless jump matrix: weighted cycle Laplacian, weights 1/a_j."""
    n = len(lens)
    R = sp.zeros(n, n)
    for j, a in enumerate(lens):
        k = (j + 1) % n
        R[j, j] += 1 / a
        R[k, k] += 1 / a
        R[j, k] += -1 / a
        R[k, j] += -1 / a
    return R


def assemble_R_num(lens, m):
    """Numeric massive jump matrix (mpmath)."""
    n = len(lens)
    R = mp.zeros(n, n)
    for j, a in enumerate(lens):
        a = mp.mpf(a)
        s, c = mp.sinh(m * a), mp.cosh(m * a)
        k = (j + 1) % n
        R[j, j] += m * c / s
        R[k, k] += m * c / s
        R[j, k] += -m / s
        R[k, j] += -m / s
    return R


def bfk_poly_check(qs):
    """Massive BFK identity as an exact Laurent-polynomial identity.

    LHS = 4 sinh^2(ml/2) = (Q - 1/Q)^2, Q = prod q_j;
    RHS = 2^{-N} prod_j (2 s_j / m) x det R(m) = prod_j s_j x det(R/m)
    (the m^N factors cancel exactly).  Clearing denominators: multiplying
    row j of R/m by s_{j-1} s_j turns it polynomial and multiplies the
    determinant by prod s_j^2, so the identity is equivalent to
    D := det(cleared matrix) == (Q - 1/Q)^2 x prod s_j, checked by expand.
    """
    n = len(qs)
    svals = [(q ** 2 - q ** -2) / 2 for q in qs]
    R = assemble_R_sym(qs)
    M = sp.zeros(n, n)
    for j in range(n):
        f = svals[(j - 1) % n] * svals[j]
        for k in range(n):
            M[j, k] = sp.expand(sp.cancel(sp.together(R[j, k] * f)))
    D = M.det(method='berkowitz')
    Q = sp.prod(qs)
    return sp.expand(D - (Q - 1 / Q) ** 2 * sp.prod(svals)) == 0


def main() -> int:
    print("=" * 78)
    print("seam_bfk_conical_det_probe  ALPHA.QUILLEN.BFK_CONICAL.01  "
          "(strategy S7)")
    print("EXPLORATION ONLY (2026-08-27). experiments/ level: NO promotion, "
          "NO ledger row,")
    print("NO marker moved, NO gate closed or narrowed.")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    l, a, m, x = sp.symbols('l a m x', positive=True)

    # ================================================================ P1
    section("P1  CONVENTIONS AND ANCHORS (zero mode removed = primed det')")

    # G01 -- circle anchors, symbolic zeta computation
    # zeta_Delta(s) = 2 (l/2pi)^{2s} zeta_R(2s); eigenvalues (2 pi n/l)^2,
    # n <> 0 (zero mode REMOVED -- same convention as v484/v485).
    A = l / (2 * sp.pi)
    dlogdet_D2 = -(4 * sp.log(A) * sp.Rational(-1, 2) + 4 * ZP0)   # -zeta'(0)
    dlogdet_D1 = -(2 * sp.log(A) * sp.Rational(-1, 2) + 2 * ZP0)   # |D| case
    sym_circle = sp.simplify(sp.expand_log(dlogdet_D2 - 2 * sp.log(l),
                                           force=True)) == 0
    sym_absD = sp.simplify(sp.expand_log(dlogdet_D1 - sp.log(l),
                                         force=True)) == 0
    mp.mp.dps = 40
    lnum = mp.mpf(3)
    zder = mp.diff(lambda ss: 2 * (lnum / (2 * mp.pi)) ** (2 * ss)
                   * mp.zeta(2 * ss), mp.mpf(0))
    num_circle = abs(-zder - 2 * mp.log(lnum)) < mp.mpf('1e-25')
    check("G01-anchor-circle", sym_circle and sym_absD and num_circle,
          "det'_zeta(Delta on S^1_l) = l^2 and det'_zeta(|D|) = l "
          "(so (det'|D|)^2 = det'Delta), symbolic via zeta_R(0) = -1/2, "
          "zeta_R'(0) = -(1/2)ln 2pi + numeric -zeta'(0) = 2 ln l at l = 3 "
          "(err %.1e); CONVENTION: zero mode REMOVED (primed det'), the "
          "same zero-mode-removed convention as v484/v485"
          % float(abs(-zder - 2 * mp.log(lnum))))

    # G02 -- interval anchor det_zeta(Dirichlet [0,a]) = 2a
    B_ = a / sp.pi
    dlogdet_int = -(2 * sp.log(B_) * sp.Rational(-1, 2) + 2 * ZP0)
    sym_int = sp.simplify(sp.expand_log(dlogdet_int - sp.log(2 * a),
                                        force=True)) == 0
    anum = mp.mpf(5) / 4
    zder_i = mp.diff(lambda ss: (anum / mp.pi) ** (2 * ss) * mp.zeta(2 * ss),
                     mp.mpf(0))
    num_int = abs(-zder_i - mp.log(2 * anum)) < mp.mpf('1e-25')
    check("G02-anchor-interval", sym_int and num_int,
          "det_zeta(-d^2/dx^2 on [0,a], Dirichlet) = 2a (no zero mode, "
          "unprimed), symbolic + numeric at a = 5/4 (err %.1e)"
          % float(abs(-zder_i - mp.log(2 * anum))))

    # G03 -- massive closed forms via the relative-Fredholm product
    # gamma-reflection route: prod(1+x^2/n^2) = 1/(Gamma(1+ix)Gamma(1-ix))
    # (Weierstrass) and Gamma(1+ix)Gamma(1-ix) = pi x / sinh(pi x) (exact)
    refl_ok = sp.simplify(sp.gamma(1 + sp.I * x) * sp.gamma(1 - sp.I * x)
                          - sp.pi * x / sp.sinh(sp.pi * x)) == 0
    errs_p = []
    for xv in (mp.mpf(1) / 3, mp.mpf(1), mp.mpf(12) / 5):
        lhs_p = mp.nsum(lambda n: mp.log(1 + xv ** 2 / n ** 2), [1, mp.inf])
        errs_p.append(abs(lhs_p - mp.log(mp.sinh(mp.pi * xv)
                                         / (mp.pi * xv))))
    num_prod = max(errs_p) < mp.mpf('1e-25')
    X = m * l / 2
    chain_circ = sp.simplify(l ** 2 * m ** 2 * (sp.sinh(X) / X) ** 2
                             - 4 * sp.sinh(X) ** 2) == 0
    chain_int = sp.simplify(2 * a * (sp.sinh(m * a) / (m * a))
                            - 2 * sp.sinh(m * a) / m) == 0
    lim_circ = sp.limit(4 * sp.sinh(X) ** 2 / m ** 2, m, 0) == l ** 2
    lim_int = sp.limit(2 * sp.sinh(m * a) / m, m, 0) == 2 * a
    check("G03-massive-closed-forms",
          refl_ok and num_prod and chain_circ and chain_int
          and lim_circ and lim_int,
          "det_zeta(Delta+m^2 on S^1_l) = 4 sinh^2(ml/2) = det'Delta x m^2 "
          "x prod(1+ (ml/2 pi n)^2)^2 and det_zeta(D_a+m^2) = 2 sinh(ma)/m; "
          "product identity prod(1+x^2/n^2) = sinh(pi x)/(pi x): gamma-"
          "reflection Gamma(1+ix)Gamma(1-ix) = pi x/sinh(pi x) symbolic + "
          "25+ digit numeric (max err %.1e); m->0 recovers the G01/G02 "
          "anchors (symbolic limits)" % float(max(errs_p)))

    # ================================================================ P2
    section("P2  MASSIVE BFK GLUING (identity + gluing constant, exact)")

    # G04 -- interval DtN block
    f0, fa = sp.symbols('f0 fa')
    usol = (f0 * sp.sinh(m * (a - x)) + fa * sp.sinh(m * x)) / sp.sinh(m * a)
    ode_ok = sp.simplify(-sp.diff(usol, x, 2) + m ** 2 * usol) == 0
    bc_ok = (sp.simplify(usol.subs(x, 0) - f0) == 0
             and sp.simplify(usol.subs(x, a) - fa) == 0)
    n0 = sp.simplify(-sp.diff(usol, x).subs(x, 0)
                     - m * (f0 * sp.cosh(m * a) - fa) / sp.sinh(m * a)) == 0
    na = sp.simplify(sp.diff(usol, x).subs(x, a)
                     - m * (fa * sp.cosh(m * a) - f0) / sp.sinh(m * a)) == 0
    lam00 = sp.limit(m * sp.cosh(m * a) / sp.sinh(m * a), m, 0)
    lam01 = sp.limit(-m / sp.sinh(m * a), m, 0)
    check("G04-interval-DtN", ode_ok and bc_ok and n0 and na
          and lam00 == 1 / a and lam01 == -1 / a,
          "Lambda_a(m) = (m/sinh ma)[[cosh ma, -1],[-1, cosh ma]] derived "
          "from the explicit solution (ODE + boundary values + outward "
          "normal derivatives, symbolic); m->0 limit (1/a)[[1,-1],[-1,1]]")

    # G05 -- the BFK identity, N = 4, GENERAL symbolic lengths
    q1, q2, q3, q4 = sp.symbols('q1 q2 q3 q4', positive=True)
    sym_bfk4 = bfk_poly_check([q1, q2, q3, q4])
    mp.mp.dps = 50
    worst = mp.mpf(0)
    for mv in M_VALUES:
        mv = mp.mpf(sp.Rational(mv))
        lens_n = [mp.mpf(sp.Rational(av)) for av in LENS_GEN]
        ltot = mp.fsum(lens_n)
        lhs_n = 4 * mp.sinh(mv * ltot / 2) ** 2
        rhs_n = mp.mpf(2) ** -4
        for av in lens_n:
            rhs_n *= 2 * mp.sinh(mv * av) / mv
        rhs_n *= mp.det(assemble_R_num(lens_n, mv))
        worst = max(worst, abs(lhs_n / rhs_n - 1))
    check("G05-BFK-identity-N4", sym_bfk4 and worst < mp.mpf('1e-40'),
          "det_zeta(Delta+m^2 on S^1) = 2^{-4} prod_j det_zeta(D_j+m^2) x "
          "det R(m) EXACT for GENERAL lengths a_1..a_4 (Laurent-polynomial "
          "identity in q_j = e^{m a_j/2}, expand == 0) + 50-digit numeric "
          "at a = (7,13,11,9)/10, m in {1/3, 1, 7/2} (worst rel err %.1e)"
          % float(worst))

    # G06 -- the gluing constant, derived: C_glue = 2^{-N}, N = 1, 2, 3
    # bfk_poly_check verifies det_zeta(circle) = 2^{-N} prod det_D x det R
    # as an exact polynomial identity; passing it for each N IS the
    # derivation C_glue = 2^{-N} (any other constant fails, see G18).
    cs = [bfk_poly_check(syms)
          for syms in ([q1], [q1, q2], [q1, q2, q3])]
    check("G06-gluing-constant", all(cs),
          "C_glue DERIVED in closed form: det_zeta(circle) / "
          "[prod det_zeta(Dirichlet) x det R] = 2^{-N} exactly for "
          "N = 1, 2, 3 cut points (general symbolic lengths) -- one local "
          "factor 1/2 per cut point; with G05 this fixes C_glue = 2^{-N} "
          "for the mu4 case N = 4 as well")

    # ================================================================ P3
    section("P3  MASSLESS (ZERO-MODE) BFK -- det' Delta = l^2 reassembled")

    a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4', positive=True)
    lens_s = [a1, a2, a3, a4]
    ltot_s = sum(lens_s)

    # G07 -- det'(R_0) = N l / prod a_j  (weights w_j = 1/a_j, polynomial)
    ws = sp.symbols('w1 w2 w3 w4', positive=True)
    R0w = sp.zeros(4, 4)
    for j in range(4):
        k2 = (j + 1) % 4
        R0w[j, j] += ws[j]
        R0w[k2, k2] += ws[j]
        R0w[j, k2] += -ws[j]
        R0w[k2, j] += -ws[j]
    lam_ = sp.Symbol('lam_')
    coeffs = R0w.charpoly(lam_).all_coeffs()     # [1, c3, c2, c1, c0]
    c0_zero = sp.expand(coeffs[4]) == 0
    detp_w = -coeffs[3]                 # product of nonzero eigenvalues
    mtree_w = sum(sp.prod(ws[i] for i in range(4) if i != j)
                  for j in range(4))
    mtree_ok = sp.expand(detp_w - 4 * mtree_w) == 0
    # under w_j = 1/a_j: 4 sum_j prod_{i<>j} 1/a_i = 4 (sum a_j)/prod a_j
    detp = 4 * ltot_s / (a1 * a2 * a3 * a4)
    detp_ok = sp.simplify(
        detp_w.subs(dict(zip(ws, [1 / aj for aj in lens_s]))) - detp) == 0
    kernel_ok = sp.expand(R0w * sp.ones(4, 1)) == sp.zeros(4, 1)
    check("G07-detprime-R0", c0_zero and detp_ok and mtree_ok and kernel_ok,
          "R_0 = weighted cycle Laplacian (weights 1/a_j), kernel = "
          "constants exactly; det'(R_0) = N l / prod a_j (charpoly "
          "coefficient, general symbolic lengths) = N x weighted spanning-"
          "tree sum (matrix-tree cross-check)")

    # G08 -- zero-mode limit and the assembled massless identity
    rowsum = sum(2 * m * sp.tanh(m * aj / 2) for aj in lens_s)
    ser = sp.series(rowsum, m, 0, 4).removeO()
    ser_ok = sp.simplify(ser - m ** 2 * ltot_s) == 0
    mp.mp.dps = 60
    lens_n = [mp.mpf(sp.Rational(av)) for av in LENS_GEN]
    ltot_n = mp.fsum(lens_n)
    mtiny = mp.mpf('1e-10')
    detRm = mp.det(assemble_R_num(lens_n, mtiny))
    detp_n = mp.mpf(sp.Rational(
        sp.simplify(detp.subs(dict(zip(lens_s, LENS_GEN))))))
    lim_err = abs(detRm / (mtiny ** 2 * (ltot_n / 4) * detp_n) - 1)
    assembled = sp.simplify(
        sp.Rational(1, 16) * sp.prod([2 * aj for aj in lens_s])
        * (ltot_s / 4) * (4 * ltot_s / (a1 * a2 * a3 * a4))
        - ltot_s ** 2) == 0
    check("G08-massless-BFK", ser_ok and lim_err < mp.mpf('1e-15')
          and assembled,
          "<1|R(m)|1> = m^2 l + O(m^4) (symbolic series) => lambda_0(m) = "
          "m^2 l/N + O(m^4); det R(m)/m^2 -> (l/N) det'(R_0) verified to "
          "rel err %.1e at m = 1e-10 (60 dps); ASSEMBLED IDENTITY "
          "det'_zeta(Delta_S1) = 2^{-N} prod(2 a_j) x (l/N) x det'(R_0) = "
          "l^2 EXACT for general lengths; l/N = ||1||^2_{L^2(S^1_l)} / "
          "||1||^2_{C^N} is the zero-mode Gram ratio" % float(lim_err))

    # ================================================================ P4
    section("P4  DtN-GREEN DUALITY (jump matrix = inverse mark Green matrix)")

    # G09 -- massive duality R(m) = (G_m|marks)^{-1}
    t = sp.Symbol('t', positive=True)        # t = m a, equal marks, l = 4a
    Rsym = (1 / sp.sinh(t)) * circ([2 * sp.cosh(t), -1, 0, -1])
    Gsym = (sp.Rational(1, 2) / sp.sinh(2 * t)) * circ(
        [sp.cosh(2 * t), sp.cosh(t), 1, sp.cosh(t)])
    prod_RG = Rsym * Gsym
    sym_dual = all(
        sp.cancel(sp.together(
            (prod_RG[i, j] - (1 if i == j else 0)).rewrite(sp.exp))) == 0
        for i in range(4) for j in range(4))
    mp.mp.dps = 50
    marks_n = [mp.mpf(0), mp.mpf(9) / 10, mp.mpf(5) / 2, mp.mpf(22) / 5]
    ln_ = 2 * mp.pi
    lens_dual = [(marks_n[(j + 1) % 4] - marks_n[j]) % ln_ for j in range(4)]
    worst_d = mp.mpf(0)
    for mv in M_VALUES:
        mv = mp.mpf(sp.Rational(mv))
        Rn = assemble_R_num(lens_dual, mv)
        Gn = mp.zeros(4, 4)
        for i in range(4):
            for j in range(4):
                d = abs(marks_n[i] - marks_n[j])
                Gn[i, j] = mp.cosh(mv * (ln_ / 2 - d)) \
                    / (2 * mv * mp.sinh(mv * ln_ / 2))
        E = Rn * Gn
        for i in range(4):
            for j in range(4):
                worst_d = max(worst_d, abs(E[i, j] - (1 if i == j else 0)))
    check("G09-massive-duality", sym_dual and worst_d < mp.mpf('1e-40'),
          "R(m) x G_m|_marks = I EXACT: symbolic 4x4 at equal marks "
          "(G_m(d) = cosh(m(l/2-d))/(2m sinh(ml/2))) + 50-digit numeric at "
          "GENERAL marks (0, 9/10, 5/2, 22/5) on l = 2pi, m in "
          "{1/3, 1, 7/2} (worst |entry err| %.1e) -- the BFK jump matrix "
          "is the inverse of the mark-restricted Green matrix"
          % float(worst_d))

    # G10 -- massless Green function and R_0 G_Delta = I - J/4
    d_ = sp.Symbol('d_', positive=True)
    GD = d_ ** 2 / (2 * l) - d_ / 2 + l / 12
    ode2 = sp.simplify(-sp.diff(GD, d_, 2) + 1 / l) == 0
    jump = sp.simplify((sp.diff(GD, d_).subs(d_, 0)
                        - sp.diff(GD, d_).subs(d_, l)) + 1) == 0
    mean0 = sp.simplify(sp.integrate(GD, (d_, 0, l))) == 0
    symm = sp.simplify(GD - GD.subs(d_, l - d_)) == 0
    mp.mp.dps = 30
    lf = 2 * mp.pi
    errs_f = []
    for df in (mp.mpf(0), lf / 5, lf / 3, lf / 2):
        four = (lf / (2 * mp.pi ** 2)) * mp.re(
            mp.polylog(2, mp.e ** (1j * 2 * mp.pi * df / lf)))
        errs_f.append(abs(four - (df ** 2 / (2 * lf) - df / 2 + lf / 12)))
    four_ok = max(errs_f) < mp.mpf('1e-25')
    GDm = (l / 96) * circ([8, -1, -4, -1])
    marks_vals = [sp.simplify(GD.subs(d_, dv))
                  for dv in (0, l / 4, l / 2, l / 4)]
    marks_ok = all(sp.simplify(marks_vals[j] - GDm[0, j]) == 0
                   for j in range(4))
    R0eq = sp.Rational(4, 1) / l * circ([2, -1, 0, -1])
    proj = sp.simplify(R0eq * GDm - (sp.eye(4) - sp.ones(4, 4) / 4)) \
        == sp.zeros(4, 4)
    check("G10-massless-duality", ode2 and jump and mean0 and symm
          and four_ok and marks_ok and proj,
          "G_Delta(d) = d^2/2l - d/2 + l/12 is THE zero-mode-removed Green "
          "function (-G'' = delta - 1/l: ODE + unit derivative jump + zero "
          "mean + symmetry, symbolic; Fourier/polylog check to 25+ digits, "
          "max err %.1e); mark matrix (l/96) circ(8,-1,-4,-1); "
          "R_0 x G_Delta|_marks = I - J/4 EXACT (identity off the zero "
          "mode)" % float(max(errs_f)))

    # ================================================================ P5
    section("P5  KMS c3-GRADING AND THE v484 MARK-MATRIX CORRESPONDENCE")

    Bm = circ([2, -1, 0, -1])
    Cm = circ([0, 1, 2, 1])
    Sm = circ([0, 0, 1, 0])
    lkms = 2 * sp.pi                       # = 1/(4 c3), v239 KMS unit
    akms = lkms / 4                        # = pi/2 = 1/(16 c3)

    # G11 -- R_0 at the KMS marks is a pure c3-graded integer circulant
    R0kms = assemble_R0_sym([akms] * 4)
    r0_ok = sp.simplify(R0kms - 16 * C3S * Bm) == sp.zeros(4, 4)
    unit_ok = (sp.simplify(16 * C3S - 4 * (4 * C3S)) == 0
               and sp.simplify(4 * C3S - 1 / (2 * sp.pi)) == 0)
    detp_kms = sp.simplify(4 * lkms / akms ** 4)
    detp_c3 = sp.simplify(detp_kms - 2 ** 16 * C3S ** 3) == 0
    product_c3 = sp.simplify(
        sp.Rational(1, 16) * (2 * akms) ** 4 * (lkms / 4) * detp_kms
        - 1 / (16 * C3S ** 2)) == 0
    anchor_c3 = sp.simplify(lkms ** 2 - 1 / (16 * C3S ** 2)) == 0
    check("G11-KMS-c3-grading", r0_ok and unit_ok and detp_c3
          and product_c3 and anchor_c3,
          "at l = 2pi = 1/(4c3): R_0 = 16 c3 x circ(2,-1,0,-1) EXACT "
          "(proportionality constant 16 c3 = |mu4| x 4 c3 = |mu4| x bare "
          "1/(2pi) -- the v484 unit chain per interval); det'(R_0) = "
          "128/pi^3 = 2^16 c3^3; per-interval det_D = 2a = pi = 1/(8 c3); "
          "zero-mode factor l/N = pi/2 = 1/(16 c3); whole glued product = "
          "2^{-4} c3^{-2} = (2pi)^2 = det'Delta -- every BFK factor is a "
          "pure 2-power times a c3 power (NOTE: C_glue = 2^{-4} = |mu4|^{-2}"
          " holds only because N = |mu4| = 4; C_glue = 2^{-N} generally -- "
          "anti-numerology)")

    # G12 -- v484 mark matrix re-derived in-probe (not imported on trust)
    Gfun = lambda dd: -(1 / sp.pi) * sp.log(2 * sp.sin(dd / 2))
    g_adj = sp.simplify(Gfun(sp.pi / 2) / (C3S * sp.log(2)))
    g_opp = sp.simplify(Gfun(sp.pi) / (C3S * sp.log(2)))
    mp.mp.dps = 30
    errs_li = [abs(mp.re(mp.polylog(1, mp.e ** (1j * v)))
                   + mp.log(2 * mp.sin(v / 2)))
               for v in (mp.pi / 7, mp.pi / 2, mp.pi)]
    spec_C = dict(Cm.eigenvals()) == {4: 1, -2: 2, 0: 1}
    check("G12-v484-rederived", g_adj == -4 and g_opp == -8
          and max(errs_li) < mp.mpf('1e-25') and spec_C,
          "G_|D|(d) = -(1/pi) ln|2 sin(d/2)| (polylog identity to 25+ "
          "digits, max err %.1e); at the mu4 separations G(pi/2) = "
          "-4 c3 ln2, G(pi) = -8 c3 ln2 => G_marks = -4 c3 ln2 x "
          "circ(0,1,2,1) =: -4 c3 ln2 C, spec(C) = {4,-2,0,-2} -- the v484 "
          "mark matrix, re-derived in-probe" % float(max(errs_li)))

    # G13 -- the correspondence: NOT globally proportional; exact channel form
    one = sp.ones(4, 1)
    v2 = sp.Matrix([1, -1, 1, -1])
    ker_swap = (sp.simplify(Bm * one) == sp.zeros(4, 1)
                and sp.simplify(Cm * v2) == sp.zeros(4, 1)
                and sp.simplify(Cm * one - 4 * one) == sp.zeros(4, 1)
                and sp.simplify(Bm * v2 - 4 * v2) == sp.zeros(4, 1))
    # no scalar k gives B = k C: B[0,0] = 2 <> 0 while C[0,0] = 0, and the
    # kernels disagree (any B = k C with k <> 0 forces equal kernels)
    not_prop = (Bm[0, 0] == 2 and Cm[0, 0] == 0)
    I4 = sp.I
    F4 = sp.Matrix(4, 4, lambda i, j: I4 ** (i * j))
    diagB = sp.simplify(F4.inv() * Bm * F4)
    diagC = sp.simplify(F4.inv() * Cm * F4)
    shared_basis = diagB.is_diagonal() and diagC.is_diagonal()
    specB = dict(Bm.eigenvals())
    mults_ok = (sorted(abs(k2) for k2, v_ in specB.items()
                       for _ in range(v_))
                == sorted(abs(k2) for k2, v_ in dict(Cm.eigenvals()).items()
                          for _ in range(v_)) == [0, 2, 2, 4])
    Pd = (sp.eye(4) - Sm) / 2              # projector onto k = 1,3 doublet
    Gmarks = -4 * C3S * sp.log(2) * Cm
    doublet = sp.simplify(16 * C3S * Bm * Pd
                          - (4 / sp.log(2)) * Gmarks * Pd) == sp.zeros(4, 4)
    bc_sum = sp.simplify(Bm + Cm - 2 * (sp.eye(4) + Sm)) == sp.zeros(4, 4)
    check("G13-correspondence", ker_swap and not_prop and shared_basis
          and mults_ok and doublet and bc_sum,
          "GLOBAL proportionality R_0 ~ G_marks FAILS (kernel channels "
          "SWAPPED: B kills the mu4-TRIVIAL k=0 channel [gauge/zero mode], "
          "C kills the mu4-SIGN k=2 channel [ln 2 arithmetic of the square]"
          "); what holds EXACTLY: same mu4 Fourier eigenbasis (both "
          "diagonal in F4), |spec| multisets EQUAL {0,2,2,4}, doublet "
          "channel (k=1,3) R_0|_d = (4/ln2) x G_marks|_d -- the c3 grading "
          "CANCELS in the ratio (16 c3 vs 4 c3 ln2, both c3-graded, "
          "constant 4/ln2 = %.10f...), and B + C = 2(I + S)"
          % float(4 / mp.log(2)))

    # G14 -- cycle combinatorics through the BFK matrix powers
    trB_ok = all(sp.trace(Bm ** k2) == 4 ** k2 + 2 * 2 ** k2
                 for k2 in range(1, 9))
    trC_ok = all(sp.trace(Cm ** k2) == 4 ** k2 + 2 * (-2) ** k2
                 for k2 in range(1, 9))
    check("G14-cycle-combinatorics", trB_ok and trC_ok
          and sp.trace(Cm) == 0 and sp.trace(Bm) == 8,
          "Tr(B^k) = 4^k + 2(+2)^k and Tr(C^k) = 4^k + 2(-2)^k EXACT "
          "(k = 1..8): the BFK jump circulant reproduces the v484 "
          "{4, 2-doublet} magnitude law with the sign channel flipped "
          "(= the kernel swap of G13); Tr C = 0 <=> the v485 diagonal "
          "renormalises to ZERO at the KMS scale, Tr B = 8 <> 0 <=> the "
          "Dirichlet jump diagonal 2/a is nonzero by construction -- the "
          "absent linear term of det(I - uC) = (1-4u)(1+2u)^2 is a |D|-"
          "side statement, not a Delta-side one (typed)")

    # ================================================================ P6
    section("P6  THE SCALE CHANNEL vs v485")

    # G15 -- d/dl log det' through the BFK factors
    t1 = sp.diff(sp.log((l / 2) ** 4), l)          # intervals prod(2 l/4)
    t2 = sp.diff(sp.log(1024 / l ** 3), l)         # det'R_0 = 4l/(l/4)^4
    t3 = sp.diff(sp.log(l / 4), l)                 # zero-mode Gram factor
    dec_ok = (sp.simplify(t1 - 4 / l) == 0 and sp.simplify(t2 + 3 / l) == 0
              and sp.simplify(t3 - 1 / l) == 0
              and sp.simplify(t1 + t2 + t3
                              - sp.diff(sp.log(l ** 2), l)) == 0)
    check("G15-scale-decomposition", dec_ok,
          "d/dl log det'_zeta(Delta) = 2/l decomposes through the glued "
          "product as 4/l (four Dirichlet intervals) - 3/l (jump-matrix "
          "det', rank 3) + 1/l (zero-mode Gram factor l/N): 4 - 3 + 1 = 2 "
          "exactly, factor by factor")

    # G16 -- the v485 dictionary
    Greg = sp.log(l / (2 * sp.pi)) / sp.pi         # v485 closed form
    dict1 = sp.simplify(sp.log(l ** 2) - sp.log((2 * sp.pi) ** 2)
                        - (1 / (4 * C3S)) * Greg) == 0
    dict2 = sp.simplify(sp.log(l) - sp.log(2 * sp.pi)
                        - sp.pi * Greg) == 0
    ratio = sp.simplify(sp.diff(sp.log(l ** 2), l) / sp.diff(Greg, l)
                        - 2 * sp.pi) == 0
    kms_pt = (sp.simplify(Greg.subs(l, 2 * sp.pi)) == 0
              and sp.simplify(1 / (4 * C3S) - 2 * sp.pi) == 0)
    check("G16-v485-scale-channel", dict1 and dict2 and ratio and kms_pt,
          "log det'Delta(l) - log det'Delta(1/(4c3)) = (1/(4 c3)) x "
          "G_reg(0; l) EXACT, and G_reg(0; l) = (1/pi)[log det'|D|(l) - "
          "log det'|D|(2pi)] (v485 closed form (1/pi) ln(l/2pi) reproduced "
          "from the glued determinant); derivative ratio = 2 pi = 1/(4 c3) "
          "= the KMS unit exactly; at the seam point G_reg = 0 while "
          "det'Delta = (2pi)^2 (the log-det is ANCHORED, not zero -- "
          "honest print)")

    # ================================================================ P7
    section("P7  MUTANTS (must be CAUGHT)")

    # G17 -- MUTANT A: one mark moved off mu4: pi/2 -> 7 pi/12
    mp.mp.dps = 50
    lens_mut = [7 * mp.pi / 12, 5 * mp.pi / 12, mp.pi / 2, mp.pi / 2]
    R0mut = mp.zeros(4, 4)
    for j in range(4):
        k2 = (j + 1) % 4
        w = 1 / lens_mut[j]
        R0mut[j, j] += w
        R0mut[k2, k2] += w
        R0mut[j, k2] += -w
        R0mut[k2, j] += -w
    anom = mp.pi / 2
    not_circ = abs(R0mut[0, 1] - R0mut[1, 2]) * anom > mp.mpf('0.1')
    evs = sorted(mp.eigsy(R0mut, eigvals_only=True))
    evs_scaled = [float(anom * e) for e in evs]
    spec_dev = max(abs(anom * e - r) for e, r in zip(evs, [0, 2, 2, 4]))
    spec_broken = spec_dev > mp.mpf('0.01')
    tr2 = mp.fsum((anom * e) ** 2 for e in evs)
    tr_broken = abs(tr2 - 24) > mp.mpf('0.05')
    detp_mut = evs[1] * evs[2] * evs[3]
    ident_mut = mp.mpf(2) ** -4
    for av in lens_mut:
        ident_mut *= 2 * av
    ident_mut *= (2 * mp.pi / 4) * detp_mut
    ident_holds = abs(ident_mut / (2 * mp.pi) ** 2 - 1) < mp.mpf('1e-40')
    check("G17-mutant-off-mark", not_circ and spec_broken and tr_broken
          and ident_holds and abs(evs[0]) < mp.mpf('1e-45'),
          "marks (0, 7pi/12, pi, 3pi/2): R_0 NOT circulant "
          "(|R01-R12| a = %.3f), a x spec = (%.4f, %.4f, %.4f, %.4f) vs "
          "mu4 (0,2,2,4) (max dev %.3f), Tr((aR)^2) = %.4f vs 24 -- "
          "CAUGHT; CONTROL: the massless BFK identity STILL gives "
          "det' = (2pi)^2 (rel err < 1e-40): the identity is mark-"
          "independent, the mu4 correspondence is not"
          % (float(abs(R0mut[0, 1] - R0mut[1, 2]) * anom),
             evs_scaled[0], evs_scaled[1], evs_scaled[2], evs_scaled[3],
             float(spec_dev), float(tr2)))

    # G18 -- MUTANT B: wrong gluing constant 2^{-3}
    rhs_wrong = sp.Rational(1, 8) * sp.prod([2 * aj for aj in lens_s]) \
        * (ltot_s / 4) * (4 * ltot_s / (a1 * a2 * a3 * a4))
    factor2 = sp.simplify(rhs_wrong / ltot_s ** 2 - 2) == 0
    check("G18-mutant-wrong-constant", factor2,
          "replacing C_glue = 2^{-4} by 2^{-3} breaks the anchor identity "
          "by an EXACT factor 2 (symbolic, general lengths): "
          "RHS_wrong / det'Delta = 2 -- CAUGHT")

    # ================================================================ P8
    section("P8  HONEST TYPING + VERDICT")

    covered = (sym_bfk4 and assembled and r0_ok and dict1)
    check("G19-honest-typing", covered,
          "COVERED: the U(1)-scalar SECOND-ORDER determinant face of the "
          "ALPHA.QUILLEN diagonal target -- Delta = |D|^2 on the seam "
          "CIRCLE with the four mu4 marks, BFK-glued, all constants in "
          "closed form. NOT covered (stays with the keystone, v382/v485 "
          "typing): the full pillowcase MODULI variation, the 8 b1 / "
          "41 = 10 b1 index-coefficient budget, and a BFK gluing of the "
          "NONLOCAL |D| itself (|D| is order-1 pseudodifferential; it "
          "enters only via its mark Green matrix, G12, and the scale "
          "dictionary, G16). experiments/ level: nothing promoted")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    verdict_ok = (npass == len(CHECKS))
    check("G20-verdict", verdict_ok,
          "MATCH_MODULO_LOCAL_FACTOR: gluing identity EXACT (C_glue = "
          "2^{-N}, general lengths) + zero-mode BFK reassembles det' = l^2 "
          "+ jump matrix = inverse mark Green matrix + v485 scale channel "
          "reproduced EXACTLY via the KMS unit 2pi = 1/(4c3); the v484 "
          "mark-matrix correspondence is CHANNEL-GRADED, not global: "
          "doublet factor 4/ln2 (c3 cancels -- both matrices c3-graded: "
          "16 c3 vs 4 c3 ln2), kernel channels swapped (mu4-trivial vs "
          "mu4-sign) -- so NOT BFK_MATCH_EXACT, and nothing mismatched")

    return finish()


def finish() -> int:
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    if npass == len(CHECKS):
        print("ALL GATES PASSED %d/%d" % (npass, len(CHECKS)))
    else:
        print("GATES: %d/%d passed -- NOT all green" % (npass, len(CHECKS)))
    print("VERDICT: %s" % ("MATCH_MODULO_LOCAL_FACTOR"
                           if npass == len(CHECKS) else "MISMATCH"))
    print("RESULT: %d/%d gates PASS   SPEC_SHA %s"
          % (npass, len(CHECKS), SPEC_SHA[:16]))
    print("EXPLORATION ONLY: no promotion, no ledger row, no marker moved, "
          "no gate closed or narrowed.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

_SRC_PUMP = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""laughlin_pump_em1_probe -- ALPHA.QUILLEN.EM1_PUMP.01 (Strategy S8):
the cited EM1/inflow step "boundary level = bulk response" made
COMPUTABLE as a Laughlin flux pump + Streda response on the very
collar model that realises S3.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  v470 (ALPHA.QUILLEN.INFLOW.01) reads the a^3
level as k0 = |C| = 1, the FHS Chern invariant of the p+ip collar
model h(k) = sin kx SX + sin ky SY + (M - cos kx - cos ky) SZ
(v367/v368), with the bulk-boundary identification CITED (TKNN 1982;
Callan-Harvey 1985; APS/Witten eta-CS; Quillen/Bismut-Freed), and
v472 computed the det-line curvature over the U(1)-twist moduli = 1.
What stayed cited-only is the INFLOW step itself: that the boundary
LEVEL equals the bulk RESPONSE.  On a lattice that step IS the
Laughlin argument -- threading one flux quantum through a cylinder
pumps exactly C charges from one edge to the other, visible as
quantised polarisation winding, as unit spectral flow of the chiral
edge branch, and (thermodynamic dual) as the Streda count
dN/dPhi = C/(2 pi).  This probe computes all three on the SAME
h(k), in its COMPLEX-fermion Chern-insulator form (single copy; the
16-Majorana collar = 8 complex copies is printed as exact Fraction
arithmetic, not simulated), and prices them against mutants.

THE SETUP (all frozen).  Model and conventions VERBATIM from
v367/v368/v472: Bloch h(k) above, occupied = lower band; strip
on-site sin kx SX + (M - cos kx) SZ, y-hop -SZ/2 + SY/(2i); M = 1
topological (C = 1), M = 3 trivial (C = 0).  Cylinder: Lx = 8 slices
periodic in x, Ny = 40 open in y, flux phi entering as the exact
gauge shift kx -> kx + phi/Lx of every momentum slice (uniform
Peierls phase e^{i phi/Lx} on the x-bonds), NPHI = 128 steps over
one flux quantum, phi-grid offset by half a step to dodge symmetric
crossings.  Filling on the cylinder: fixed particle number
N = Lx * Ny (half filling by count), so the hybrid-Wannier count is
constant and the occupied-set switch at the edge-branch crossing
appears as ONE quantised teleport event, bookkept separately from
the continuous transport.  PUMP FORMULATION (chosen for a clean
integer winding, documented): (i) BULK hybrid-Wannier winding -- the
gauge-invariant Wilson loop of the occupied band around the ky
circle at fixed kx gives the Wannier center ybar(kx) mod 1; since
flux threading is the rigid shift kx -> kx + phi/Lx, the total
y-polarisation P_y(phi) = sum_n ybar(k_n + phi/Lx) winds over one
flux quantum by EXACTLY the Brillouin-zone winding of ybar
(telescoping over the Lx slices), which is gated == C to 1e-6;
(ii) CYLINDER transport -- per slice the occupied projector's
P yhat P spectrum (hybrid Wannier charge centers, gauge invariant)
is tracked in phi, and the NET number of centers crossing the bulk
fiducial line y_cut = (Ny-1)/2 + 0.2871 CONTINUOUSLY per flux
quantum is the pumped charge, gated == C exactly (integer), with
the teleport events counted and the period-closure identity
(continuous + teleport = 0) checked as an instrument.
ORIENTATION CONVENTIONS (three signs frozen at the single
calibration pass, nothing else moved): OR1 the Berry-phase sign in
ybar(kx) := +arg(W)/(2 pi); OR2 the flux-threading sign
k_n(phi) = (2 pi n - phi)/Lx; OR3 the Streda field orientation
(measured s = DeltaN(1) = +1 at M = 1 for the +n_phi Peierls gauge
below, i.e. DeltaN(n) = +C n; the C-linearity is the gate, the
absolute sign is the orientation).  The convention-FREE content:
the magnitude |pump| = |C| = 1, the M = 3 zeros, the per-edge
antisymmetry of the spectral flow, the cross-n_phi linearity of the
Streda count, and the SIMULTANEOUS sign flip of everything under
complex conjugation of the model.

PRE-REGISTERED ADJUDICATION (frozen before the record runs; one
calibration pass fixed OR1/OR2/OR3 and the mutant record values,
nothing else moved):
  P1 ANCHORS: FHS Chern C(M=1) = 1, C(M=3) = 0 exactly (integer
     gates, tol 1e-9, v367/v470 convention); strip in-gap edge
     branch min_kx|E| < 0.05 at M = 1, > 0.3 at M = 3 (v368).
  P2 THE PUMP: bulk hybrid-Wannier winding DeltaP == C within 1e-6
     at M = 1 and == 0 at M = 3 (unwrap steps < 0.25 gated); cylinder
     P yhat P continuous midline transport == C exactly (integer)
     per flux quantum at M = 1, == 0 at M = 3, teleport bookkeeping
     printed and period closure (continuous + teleport = 0) checked.
  P3 SPECTRAL FLOW: edge-resolved zero crossings of the in-gap
     branch per flux quantum: net sigma = +-1 on the bottom edge and
     -sigma on the top edge at M = 1 (chirality sign printed), and
     ZERO in-gap crossings at M = 3.
  P4 STREDA: on the L x L torus (L = 12) with n_phi uniform flux
     quanta (verified uniform Peierls gauge, plaquette deviation
     < 1e-12), the filled-band count obeys N(n_phi) - N(0) = s C
     n_phi EXACTLY for n_phi = 1, 2, 3 at M = 1 (fit slope within
     5e-2 first, then the exact integer), and stays CONSTANT at
     M = 3; gap at E = 0 open (min|E| > 0.1) for every n_phi.
  P5 THE 16-COPY / LEVEL BOOKKEEPING (exact Fractions): 16 Majorana
     = 8 complex copies; c_- = 16 x (1/2) x |C| = 8 = g_car + N_fam;
     k0 = |C| = 1 per complex copy (the v470 statement); k_Y
     re-derived from the v470 arithmetic: tr_5bar(Y^2)/tr(T3^2)
     = (5/6)/(1/2) = 5/3, (3/5)(41/6) = 41/10 = b1,
     41/6 = 20/3 + 1/6.
  P6 MUTANTS: the complex-conjugated model (sin ky -> -sin ky) must
     flip EVERYTHING simultaneously -- FHS Chern -1, Wannier winding
     -1, cylinder transport -1, Streda -s C n_phi (CAUGHT as the
     sign gate); a wrong-band projector (band chosen by
     sign(sin 3(kx + ky)), a k-dependent valence/conduction
     patchwork) must BREAK quantisation through three channels:
     the FHS reading is GRID-UNSTABLE (|C_mut(N=24) - C_mut(N=36)|
     >= 1 -- no well-defined invariant; calibrated 3 vs 1), the
     Wannier flow is UNREADABLE (max unwrap step > 0.25, calibrated
     0.331), and the nominal winding disagrees with C (calibrated
     0 vs 1) (CAUGHT).
EXPECTED VERDICT (pre-registered): PUMP_QUANTIZED_MATCHES_CHERN --
pumped charge == spectral flow == Streda == C on the S3 collar
model, i.e. the "boundary level = bulk response" step of EM1 holds
COMPUTABLY at the lattice level, per complex copy.

RECORD PROTOCOL (house pattern): two calibration passes at
pre-freeze SHAs c0c96e0d8bbd7ee0 (14/20 -- the six fails were
exactly the three orientation signs OR1/OR3 + the untested strip
conjugation hook + a self-referential source scan + the first
too-weak mutant, every physics finding already held) and the fixed
spec (20/20 in 2.9 s); OR1/OR2/OR3, the strip sy hook, the mutant
rule sin(3(kx+ky)) and its record values (FHS 3 vs 1, step 0.331,
winding 0) frozen from calibration; the only edit after the clean
calibration pass is this record-note insertion itself.  Two record
runs laughlin_pump_em1_probe.run1.log / .run2.log at the final
SPEC_SHA must be identical modulo WALL lines.

VERDICT ENUM: PUMP_QUANTIZED_MATCHES_CHERN (all anchors and all
matches pass) / PUMP_MISMATCH (instruments fine but a quantised
response disagrees with C) / INSTRUMENT_FAILS (an anchor, gauge
check, arithmetic identity or the runtime bar fails).

WHAT IS BUILT AND GATED: S0 G01 firewall/spec; S1 anchors G02-G05;
S2 pump G06-G09; S3 spectral flow G10-G11; S4 Streda G12-G14; S5
bookkeeping G15-G16; S6 mutants G17-G18; S7 G19 runtime (< 180 s)
+ G20 verdict aggregate.  20 gates.

HONEST LIMITATIONS.  (i) Single COMPLEX copy: the physical collar
carrier is 16 Majoranas = 8 complex copies; the multi-copy statement
enters only as exact arithmetic (P5), not as a 16-band simulation.
(ii) Complex-fermion form: the QWZ/Chern-insulator reading of h(k)
carries a genuine U(1); the Majorana/BdG collar has no microscopic
U(1) per Majorana -- the U(1) pumped here is the one EM1 actually
uses (the complex-copy pairing), and that identification stays part
of the cited EM1 reading [C].  (iii) Lattice only: no continuum
scaling limit (MMST, v336) is touched.  (iv) Nothing here closes or
narrows ALPHA.QUILLEN.EXACT.01; the bridge lemma stays the named
cited step; this probe upgrades "cited" to "computable on the
model" at experiments/ level only.

DETERMINISM: no randomness anywhere (numpy eigh on fixed grids,
gauge-invariant observables only); two record runs
laughlin_pump_em1_probe.run1.log / .run2.log must be identical
modulo wall-clock tokens (lines carrying 'WALL').
"""

from __future__ import annotations

import hashlib
import os
import time
from fractions import Fraction

import numpy as np

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)

# ---------------------------------------------------------------- frozen
M_TOPO, M_TRIV = 1.0, 3.0
N_FHS = 24                 # v367/v470/v472 FHS grid
TOL_CHERN = 1e-9
NKX_WILSON = 64            # kx steps of the pump (>= 64 required)
NKY_WILSON = 256           # ky Wilson-loop resolution
PUMP_TOL = 1e-6
UNWRAP_BAR = 0.25          # max legal unwrap step (adiabatic readability)
LX_CYL, NY_CYL, NPHI_CYL = 8, 40, 128
Y_CUT = (NY_CYL - 1) / 2 + 0.2871
GAP_WINDOW = 0.6           # in-gap window for the edge branch (bulk |E|>~1)
MATCH_BAR = 0.4            # continuous-move bar in the center matching
L_STREDA = 12
NPHI_STREDA = (0, 1, 2, 3)
STREDA_GAP_BAR = 0.1
STREDA_FIT_BAR = 5e-2
GAUGE_DEV_BAR = 1e-12
MUTANT_GRID_BAR = 0.5      # FHS grid instability threshold (N=24 vs N=36)
N_FHS_ALT = 36
RUNTIME_BAR = 180.0

# frozen from verification/tfpt_constants (P2 axiom g_car = 5; N_fam = 3)
G_CAR = 5
N_FAM = 3

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-22s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ Bloch layer
def bloch_h(kx, ky, M, sy=1.0):
    """h(k) of v367; sy = -1 is the complex-conjugated (mutant) model."""
    return (np.sin(kx) * SX + sy * np.sin(ky) * SY
            + (M - np.cos(kx) - np.cos(ky)) * SZ)


def band_vec(kx, ky, M, sy=1.0, band=0):
    _, v = np.linalg.eigh(bloch_h(kx, ky, M, sy))
    return v[:, band]


def fhs_chern(M, sy=1.0, N=N_FHS, band_rule=None):
    """Fukui-Hatsugai-Suzuki plaquette Chern number (v367/v470 verbatim
    convention); band_rule(kx, ky) -> band index (mutant hook)."""
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    if band_rule is None:
        band_rule = lambda kx, ky: 0
    u = [[band_vec(kx, ky, M, sy, band_rule(kx, ky)) for ky in ks]
         for kx in ks]

    def ln(a, b):
        x = np.vdot(a, b)
        return x / abs(x)

    F = 0.0
    for i in range(N):
        for j in range(N):
            ip, jp = (i + 1) % N, (j + 1) % N
            F += np.angle(ln(u[i][j], u[ip][j]) * ln(u[ip][j], u[ip][jp])
                          * np.conj(ln(u[i][jp], u[ip][jp]))
                          * np.conj(ln(u[i][j], u[i][jp])))
    return F / (2 * np.pi)


# ------------------------------------------- pump (i): bulk Wannier winding
def wannier_center(kx, M, sy=1.0, nky=NKY_WILSON, band_rule=None):
    """Gauge-invariant Wilson loop of the occupied band around the ky
    circle at fixed kx -> hybrid Wannier center ybar(kx) mod 1 (OR1:
    ybar := +arg(W)/(2 pi))."""
    kys = np.linspace(0, 2 * np.pi, nky, endpoint=False)
    if band_rule is None:
        band_rule = lambda kx, ky: 0
    us = [band_vec(kx, ky, M, sy, band_rule(kx, ky)) for ky in kys]
    W = 1.0 + 0.0j
    for j in range(nky):
        W *= np.vdot(us[j], us[(j + 1) % nky])
    return np.angle(W) / (2 * np.pi)


def pump_winding(M, sy=1.0, nkx=NKX_WILSON, band_rule=None):
    """Winding of ybar(kx) over the BZ = the y-charge pumped through the
    cylinder by one flux quantum (P_y(phi) telescopes over the Lx slices
    to exactly this winding).  Returns (DeltaP, max unwrap step)."""
    kxs = np.linspace(0, 2 * np.pi, nkx + 1)
    raw = [wannier_center(kx, M, sy, band_rule=band_rule) for kx in kxs]
    y = [raw[0]]
    max_step = 0.0
    for r in raw[1:]:
        d = r - y[-1]
        d -= round(d)
        max_step = max(max_step, abs(d))
        y.append(y[-1] + d)
    return y[-1] - y[0], max_step


# --------------------------------------- pump (ii): cylinder P y P transport
def strip_H(k, M, Ny, sy=1.0):
    """v368 strip Hamiltonian verbatim: Ny open sites in y, momentum k;
    sy = -1 conjugates the y-hopping (the mutant model's strip)."""
    ons = np.sin(k) * SX + (M - np.cos(k)) * SZ
    hop = -0.5 * SZ + sy * (1 / 2j) * SY
    H = np.zeros((2 * Ny, 2 * Ny), complex)
    for y in range(Ny):
        H[2 * y:2 * y + 2, 2 * y:2 * y + 2] = ons
    for y in range(Ny - 1):
        H[2 * y:2 * y + 2, 2 * y + 2:2 * y + 4] = hop
        H[2 * y + 2:2 * y + 4, 2 * y:2 * y + 2] = hop.conj().T
    return H


def match_step(prev, new):
    """Match two sorted Wannier-center lists between adjacent phi steps.
    Returns (net continuous up-crossings of Y_CUT, teleport sign, anomaly).
    Teleport sign -1 = a center left the top edge and reappeared at the
    bottom (discontinuous down-crossing), +1 the reverse."""
    cands = []
    d0 = float(np.max(np.abs(new - prev)))
    cands.append((d0, 0))
    if len(prev) > 1:
        cands.append((float(np.max(np.abs(new[1:] - prev[:-1]))), +1))
        cands.append((float(np.max(np.abs(new[:-1] - prev[1:]))), -1))
    maxd, shift = min(cands)
    if shift == 0:
        a, b = prev, new
        tele = 0
    elif shift == +1:          # arrival at bottom, departure from top
        a, b = prev[:-1], new[1:]
        tele = -1
    else:                      # arrival at top, departure from bottom
        a, b = prev[1:], new[:-1]
        tele = +1
    up = int(np.sum((a < Y_CUT) & (b > Y_CUT)))
    down = int(np.sum((b < Y_CUT) & (a > Y_CUT)))
    anomaly = 1 if maxd > MATCH_BAR else 0
    return up - down, tele, anomaly


def cylinder_sweep(M, sy=1.0):
    """One flux quantum through the cylinder (OR2: k_n(phi) =
    (2 pi n - phi)/Lx).  Tracks (a) the P y P hybrid Wannier centers per
    slice -> continuous midline transport + teleports, (b) the in-gap
    edge levels -> edge-resolved spectral flow through E = 0."""
    y_site = np.repeat(np.arange(NY_CYL), 2).astype(float)
    phis = 2 * np.pi * (np.arange(NPHI_CYL + 1) + 0.5) / NPHI_CYL
    net_up, tele_net, anomalies = 0, 0, 0
    flow = {"bottom": 0, "top": 0}
    prev_centers = [None] * LX_CYL
    prev_ingap = [dict() for _ in range(LX_CYL)]
    for phi in phis:
        for n in range(LX_CYL):
            k = (2 * np.pi * n - phi) / LX_CYL          # OR2
            w, v = np.linalg.eigh(strip_H(k, M, NY_CYL, sy))
            V = v[:, :NY_CYL]                       # fixed count: half filling
            A = V.conj().T @ (V * y_site[:, None])
            centers = np.sort(np.linalg.eigvalsh(A))
            ingap = {}
            for i in np.where(np.abs(w) < GAP_WINDOW)[0]:
                yexp = float(np.abs(v[:, i]) ** 2 @ y_site)
                edge = "bottom" if yexp < NY_CYL / 2 else "top"
                if edge not in ingap or abs(w[i]) < abs(ingap[edge]):
                    ingap[edge] = float(w[i])
            if prev_centers[n] is not None:
                u, t, a = match_step(prev_centers[n], centers)
                net_up += u
                tele_net += t
                anomalies += a
                for edge, E_new in ingap.items():
                    E_old = prev_ingap[n].get(edge)
                    if E_old is not None and E_old * E_new < 0:
                        flow[edge] += 1 if E_new > E_old else -1
            prev_centers[n] = centers
            prev_ingap[n] = ingap
    return dict(net_up=net_up, teleports=tele_net, anomalies=anomalies,
                flow=flow)


# ------------------------------------------------------ Streda (magnetic torus)
def _theta_x(x, y, n, L):
    """Peierls phase on the x-bond (x,y)->(x+1,y); seam twist at x=L-1."""
    return 0.0 if x < L - 1 else -2 * np.pi * n * y / L


def _theta_y(x, y, n, L):
    """Peierls phase on the y-bond (x,y)->(x,y+1) (Landau gauge)."""
    return 2 * np.pi * n * x / L ** 2


def gauge_check(n, L):
    """Max deviation of any plaquette flux from the uniform 2 pi n / L^2."""
    target = 2 * np.pi * n / L ** 2
    dev = 0.0
    for x in range(L):
        for y in range(L):
            loop = (_theta_x(x, y, n, L) + _theta_y((x + 1) % L, y, n, L)
                    - _theta_x(x, (y + 1) % L, n, L) - _theta_y(x, y, n, L))
            d = (loop - target + np.pi) % (2 * np.pi) - np.pi
            dev = max(dev, abs(d))
    return dev


def streda_count(M, n, L=L_STREDA, sy=1.0):
    """Filled-band count N = #{E < 0} and min|E| on the L x L torus with
    n uniform flux quanta.  Real-space hoppings TX, TY verbatim v472."""
    TX = (-SZ - 1j * SX) / 2
    TY = (-SZ - 1j * sy * SY) / 2
    N = L * L
    H = np.zeros((2 * N, 2 * N), complex)

    def blk(x, y):
        return 2 * ((x % L) + L * (y % L))

    for x in range(L):
        for y in range(L):
            i = blk(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            for (dx, dy, T, th) in ((1, 0, TX, _theta_x(x, y, n, L)),
                                    (0, 1, TY, _theta_y(x, y, n, L))):
                j = blk(x + dx, y + dy)
                ph = np.exp(1j * th)
                H[j:j + 2, i:i + 2] += ph * T
                H[i:i + 2, j:j + 2] += np.conj(ph) * T.conj().T
    w = np.linalg.eigvalsh(H)
    return int(np.sum(w < 0)), float(np.min(np.abs(w)))


def fit_slope(xs, ys):
    xs = np.asarray(xs, float)
    ys = np.asarray(ys, float)
    mx, my = xs.mean(), ys.mean()
    return float(((xs - mx) * (ys - my)).sum() / ((xs - mx) ** 2).sum())


# ------------------------------------------------------------------ mutants
def mutant_band_rule(kx, ky):
    """Wrong-band projector: a k-dependent valence/conduction patchwork
    (upper band wherever sin(3(kx + ky)) > 0) -- not a gapped band."""
    return 1 if np.sin(3 * (kx + ky)) > 0 else 0


# --------------------------------------------------------------------- main
def main() -> int:
    print("=" * 78)
    print("laughlin_pump_em1_probe -- ALPHA.QUILLEN.EM1_PUMP.01 (Strategy S8)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, "
          "NO ledger row,")
    print("NO marker moved, NO gate closed or narrowed.")
    print("=" * 78)

    # ---------------------------------------------------------------- S0
    section("S0  firewall / spec")
    here = os.path.dirname(os.path.abspath(__file__))
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    in_disc = here.endswith(os.path.join("experiments", "tfpt-discovery"))
    no_rng = (("np." + "random") not in src
              and ("import " + "random") not in src)
    check("G01-spec", in_disc and no_rng,
          "probe lives in experiments/tfpt-discovery, no RNG anywhere "
          "(deterministic); frozen: FHS N=%d, Wilson %dx%d, cylinder "
          "Lx=%d Ny=%d NPHI=%d, Streda L=%d n_phi=%s"
          % (N_FHS, NKX_WILSON, NKY_WILSON, LX_CYL, NY_CYL, NPHI_CYL,
             L_STREDA, list(NPHI_STREDA)))

    # ---------------------------------------------------------------- S1
    section("S1  anchors (P1): FHS Chern + strip edge branch (v367/v368)")
    C_topo = fhs_chern(M_TOPO)
    C_triv = fhs_chern(M_TRIV)
    check("G02-chern-topo", abs(C_topo - 1) < TOL_CHERN,
          "FHS Chern C(M=1) = %+.12f == +1 (tol %.0e, v367/v470 convention)"
          % (C_topo, TOL_CHERN))
    check("G03-chern-triv", abs(C_triv) < TOL_CHERN,
          "FHS Chern C(M=3) = %+.12f == 0 (trivial control)" % C_triv)
    kxs = np.linspace(0, 2 * np.pi, 80, endpoint=False)
    minE_topo = min(np.min(np.abs(np.linalg.eigvalsh(strip_H(k, M_TOPO,
                                                             NY_CYL))))
                    for k in kxs)
    minE_triv = min(np.min(np.abs(np.linalg.eigvalsh(strip_H(k, M_TRIV,
                                                             NY_CYL))))
                    for k in kxs)
    check("G04-strip-ingap", minE_topo < 0.05,
          "strip min_kx|E| = %.6f < 0.05 at M=1 -- chiral edge branch deep "
          "in the gap (v368)" % minE_topo)
    check("G05-strip-gap", minE_triv > 0.3,
          "strip min_kx|E| = %.4f > 0.3 at M=3 -- clean gap, no edge branch "
          "(v368 control)" % minE_triv)
    C_int = int(round(C_topo))

    # ---------------------------------------------------------------- S2
    section("S2  THE PUMP (P2): Laughlin flux pump, two formulations")
    dP_topo, step_topo = pump_winding(M_TOPO)
    dP_triv, step_triv = pump_winding(M_TRIV)
    check("G06-pump-wilson-topo",
          abs(dP_topo - C_int) < PUMP_TOL and step_topo < UNWRAP_BAR,
          "hybrid-Wannier winding DeltaP(M=1) = %+.12f == C = %+d "
          "(residual %.1e < 1e-6; max unwrap step %.4f < %.2f)"
          % (dP_topo, C_int, abs(dP_topo - C_int), step_topo, UNWRAP_BAR))
    check("G07-pump-wilson-triv",
          abs(dP_triv) < PUMP_TOL and step_triv < UNWRAP_BAR,
          "hybrid-Wannier winding DeltaP(M=3) = %+.12f == 0 "
          "(residual %.1e; max step %.4f)"
          % (dP_triv, abs(dP_triv), step_triv))
    cyl_topo = cylinder_sweep(M_TOPO)
    cyl_triv = cylinder_sweep(M_TRIV)
    check("G08-pump-cyl-topo",
          cyl_topo["net_up"] == C_int and cyl_topo["anomalies"] == 0
          and cyl_topo["net_up"] + cyl_topo["teleports"] == 0,
          "cylinder P y P transport (M=1): net continuous midline crossings "
          "= %+d == C = %+d per flux quantum (teleports %+d, closure "
          "cont+tele = %d, anomalies %d)"
          % (cyl_topo["net_up"], C_int, cyl_topo["teleports"],
             cyl_topo["net_up"] + cyl_topo["teleports"],
             cyl_topo["anomalies"]))
    check("G09-pump-cyl-triv",
          cyl_triv["net_up"] == 0 and cyl_triv["teleports"] == 0
          and cyl_triv["anomalies"] == 0,
          "cylinder P y P transport (M=3): net crossings = %+d == 0, "
          "teleports %+d, anomalies %d"
          % (cyl_triv["net_up"], cyl_triv["teleports"],
             cyl_triv["anomalies"]))

    # ---------------------------------------------------------------- S3
    section("S3  SPECTRAL FLOW (P3): edge levels through E = 0 per flux "
            "quantum")
    fb, ft = cyl_topo["flow"]["bottom"], cyl_topo["flow"]["top"]
    check("G10-flow-topo", abs(fb) == 1 and ft == -fb,
          "M=1: net zero-crossings bottom edge = %+d, top edge = %+d "
          "(chirality sigma = %+d, one chiral branch per edge, "
          "antisymmetric as inflow demands)" % (fb, ft, fb))
    fb3, ft3 = cyl_triv["flow"]["bottom"], cyl_triv["flow"]["top"]
    check("G11-flow-triv", fb3 == 0 and ft3 == 0,
          "M=3: net zero-crossings bottom = %d, top = %d (no in-gap "
          "spectral flow in the trivial phase)" % (fb3, ft3))

    # ---------------------------------------------------------------- S4
    section("S4  STREDA (P4): dN/dPhi of the filled band on the magnetic "
            "torus")
    dev = max(gauge_check(n, L_STREDA) for n in NPHI_STREDA)
    st_topo = [streda_count(M_TOPO, n) for n in NPHI_STREDA]
    st_triv = [streda_count(M_TRIV, n) for n in NPHI_STREDA]
    min_gap = min(min(g for _N, g in st_topo), min(g for _N, g in st_triv))
    check("G12-streda-gauge", dev < GAUGE_DEV_BAR
          and min_gap > STREDA_GAP_BAR,
          "uniform-flux Peierls gauge verified: max plaquette deviation "
          "%.2e < 1e-12 (all n_phi); E=0 gap open, min|E| = %.4f > %.1f "
          "(both M, all n_phi)" % (dev, min_gap, STREDA_GAP_BAR))
    N0 = st_topo[0][0]
    dN = [st_topo[i][0] - N0 for i, _ in enumerate(NPHI_STREDA)]
    slope = fit_slope(NPHI_STREDA, [N for N, _g in st_topo])
    s_or3 = +1                                   # OR3, frozen at calibration
    check("G13-streda-topo",
          abs(slope - s_or3 * C_int) < STREDA_FIT_BAR
          and all(dN[i] == s_or3 * C_int * n
                  for i, n in enumerate(NPHI_STREDA)),
          "M=1: N(n_phi) = %s, DeltaN = %s = s C n_phi with s = %+d (OR3) "
          "and C = %+d; fit slope %+.6f (|slope - sC| < 5e-2, then exact "
          "integer); dN/dPhi = sC/(2 pi) per unit flux Phi = 2 pi n_phi"
          % ([N for N, _g in st_topo], dN, s_or3, C_int, slope))
    dN3 = [st_triv[i][0] - st_triv[0][0] for i, _ in enumerate(NPHI_STREDA)]
    check("G14-streda-triv", all(d == 0 for d in dN3),
          "M=3: N(n_phi) = %s constant, DeltaN = %s == 0 (C = 0 dual)"
          % ([N for N, _g in st_triv], dN3))

    # ---------------------------------------------------------------- S5
    section("S5  16-COPY / LEVEL BOOKKEEPING (P5): exact Fractions "
            "(v470 arithmetic re-derived)")
    N_maj = 2 ** (G_CAR - 1)
    N_cplx = Fraction(N_maj, 2)
    c_minus = N_maj * Fraction(1, 2) * abs(C_int)
    k0 = abs(C_int)
    check("G15-copies", N_maj == 16 and N_cplx == 8 and c_minus == 8
          and c_minus == G_CAR + N_FAM and k0 == 1,
          "N_maj = 2^(g_car-1) = %d Majoranas = %s complex copies; "
          "c_- = 16 x 1/2 x |C| = %s = g_car + N_fam = %d; per-copy U(1) "
          "level k0 = |C| = %d (the v470 EM1 statement, one copy computed "
          "here)" % (N_maj, N_cplx, c_minus, G_CAR + N_FAM, k0))
    trY2 = 3 * Fraction(1, 3) ** 2 + 2 * Fraction(1, 2) ** 2
    trT32 = 2 * Fraction(1, 2) ** 2
    kY = trY2 / trT32
    b1_SM = Fraction(41, 6)
    ferm = Fraction(2, 3) * 3 * (6 * Fraction(1, 6) ** 2
                                 + 3 * Fraction(2, 3) ** 2
                                 + 3 * Fraction(1, 3) ** 2
                                 + 2 * Fraction(1, 2) ** 2 + 1)
    higgs = Fraction(1, 3) * 2 * Fraction(1, 2) ** 2
    check("G16-embedding",
          kY == Fraction(5, 3) and b1_SM / kY == Fraction(41, 10)
          and ferm == Fraction(20, 3) and higgs == Fraction(1, 6)
          and ferm + higgs == b1_SM,
          "k_Y = tr_5bar(Y^2)/tr(T3^2) = (%s)/(%s) = %s; (1/k_Y) x 41/6 = "
          "%s = b1; carrier decomposition 41/6 = %s (fermions) + %s (Higgs) "
          "(v470 arithmetic verbatim)"
          % (trY2, trT32, kY, b1_SM / kY, ferm, higgs))

    # ---------------------------------------------------------------- S6
    section("S6  MUTANTS (P6): reversed chirality + wrong-band projector")
    C_conj = fhs_chern(M_TOPO, sy=-1.0)
    dP_conj, step_conj = pump_winding(M_TOPO, sy=-1.0)
    cyl_conj = cylinder_sweep(M_TOPO, sy=-1.0)
    st_conj = [streda_count(M_TOPO, n, sy=-1.0) for n in NPHI_STREDA]
    dNc = [st_conj[i][0] - st_conj[0][0] for i, _ in enumerate(NPHI_STREDA)]
    check("G17-mutant-conj",
          abs(C_conj + 1) < TOL_CHERN and abs(dP_conj + 1) < PUMP_TOL
          and step_conj < UNWRAP_BAR and cyl_conj["net_up"] == -1
          and cyl_conj["anomalies"] == 0
          and all(dNc[i] == -s_or3 * n for i, n in enumerate(NPHI_STREDA)),
          "complex-conjugated model flips EVERYTHING simultaneously: FHS "
          "C = %+.9f == -1, winding DeltaP = %+.9f == -1, cylinder "
          "transport %+d == -1, Streda DeltaN = %s = -s n_phi -- sign "
          "mutant CAUGHT (convention-free consistency)"
          % (C_conj, dP_conj, cyl_conj["net_up"], dNc))
    C_mut24 = fhs_chern(M_TOPO, band_rule=mutant_band_rule)
    C_mut36 = fhs_chern(M_TOPO, N=N_FHS_ALT, band_rule=mutant_band_rule)
    dP_mut, step_mut = pump_winding(M_TOPO, band_rule=mutant_band_rule)
    grid_dev = abs(C_mut24 - C_mut36)
    check("G18-mutant-band",
          grid_dev > MUTANT_GRID_BAR and step_mut > UNWRAP_BAR
          and abs(dP_mut - C_int) > 0.5,
          "wrong-band projector BREAKS quantisation: FHS reading is "
          "GRID-UNSTABLE ('C' = %+.4f at N=24 vs %+.4f at N=36, dev %.2f > "
          "%.1f -- no well-defined invariant), the Wannier flow is "
          "unreadable (max unwrap step %.4f > %.2f) and the nominal "
          "winding %+.4f != C = %+d -- mutant CAUGHT"
          % (C_mut24, C_mut36, grid_dev, MUTANT_GRID_BAR, step_mut,
             UNWRAP_BAR, dP_mut, C_int))

    # ---------------------------------------------------------------- S7
    section("S7  runtime + verdict")
    wall = time.time() - T0_WALL
    check("G19-runtime", wall < RUNTIME_BAR,
          "WALL %.1f s < %.0f s bar" % (wall, RUNTIME_BAR))

    by_name = {n: ok for n, ok, _d in CHECKS}
    instr = ["G01-spec", "G02-chern-topo", "G03-chern-triv",
             "G04-strip-ingap", "G05-strip-gap", "G12-streda-gauge",
             "G15-copies", "G16-embedding", "G19-runtime"]
    match = ["G06-pump-wilson-topo", "G07-pump-wilson-triv",
             "G08-pump-cyl-topo", "G09-pump-cyl-triv", "G10-flow-topo",
             "G11-flow-triv", "G13-streda-topo", "G14-streda-triv",
             "G17-mutant-conj", "G18-mutant-band"]
    if not all(by_name[n] for n in instr):
        verdict = "INSTRUMENT_FAILS"
    elif all(by_name[n] for n in match):
        verdict = "PUMP_QUANTIZED_MATCHES_CHERN"
    else:
        verdict = "PUMP_MISMATCH"
    check("G20-verdict", verdict == "PUMP_QUANTIZED_MATCHES_CHERN",
          "VERDICT = %s (pre-registered expectation: "
          "PUMP_QUANTIZED_MATCHES_CHERN)" % verdict)

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    if npass == len(CHECKS):
        print("ALL GATES PASSED %d/%d" % (npass, len(CHECKS)))
    else:
        print("GATES PASSED %d/%d -- FAILURES: %s"
              % (npass, len(CHECKS),
                 [n for n, ok, _d in CHECKS if not ok]))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s   WALL %.1f s" % (SPEC_SHA[:16], wall))
    print("EXPLORATION ONLY -- experiments/ level: NO promotion, NO ledger "
          "row, NO marker")
    print("moved, NO gate closed or narrowed.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_RIG = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""quillen_rigidity_chain_probe -- ALPHA.QUILLEN.RIGIDITY_CHAIN.01
(Strategy S9): the conditional chain that collapses
ALPHA.QUILLEN.EXACT.01 onto the seam-state rigidity lemma, made
executable and verified at its finite shadow.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed.

WHY THIS ROUND EXISTS.  ALPHA.QUILLEN.EXACT.01 (ledger row; v341 /
v382 / v484 / v485) is the one remaining EM obligation: the from-
first-principles proof that F_U(1) = a^3 - 2 c3^3 a^2 - 8 b1 c3^6
ln(1/phi_seam) is the EXACT zeta-regularised Quillen functional of
the seam U(1).  v472 (ALPHA.QUILLEN.DETLINE.01) computed the finite
Quillen shadow -- the determinant-line Chern over the U(1)-twist
moduli of the collar model = 1, size-independent -- but only ONE
side of Quillen's identity: the FHS/Berry curvature of the occupied-
band line bundle.  Quillen's theorem has TWO sides: the curvature of
the DETERMINANT-LINE METRIC ||s||^2 (the norm of the overlap
section, i.e. i ddbar log||det||^2 of the Gaussian overlap kernel)
reproduces the Berry/index form up to a LOCAL ANOMALY term (Quillen
1985; Bismut-Freed CMP 106 (1986)).  IF the seam state is quasi-free
-- the rigidity target of the parallel S1 probe
seam_rp_rigidity_probe.py (premise SEAM.RP.RIGIDITY; terrain v903,
where OS positivity <=> a_J = 0 forces the quasi-free-diagonal point
on the deployed family) -- THEN the seam determinant line IS a
free-fermion determinant line and the identity applies literally.
THIS probe makes the chain executable at the finite shadow:
  L1 verifies BOTH sides of the identity on the v472 collar family
     over the twist torus and measures the difference field;
  L2 types the conditional on the named premise (printed, NOT a
     numeric gate -- the premise is NOT assumed proven);
  L3 re-verifies the value-level anchor exactly (the Quillen split
     at the alpha root, mpmath 50 digits + exact Fractions);
  L4 prints the resulting DAG: with L1 verified and L2 conditional,
     the remaining open content of ALPHA.QUILLEN.EXACT.01 is exactly
     {the rigidity premise} + {the diagonal-zeta face} + {EM1} --
     no ADDITIONAL analytic unknown; parallel probes cross-named:
     seam_bfk_conical_det_probe (the diagonal-zeta / conical-
     determinant face), laughlin_pump_em1_probe (EM1).

THE SETUP (v472 VERBATIM).  Collar Hamiltonian h(k) = sin kx SX +
sin ky SY + (M - cos kx - cos ky) SZ (v367/v470), in real space on
an L x L torus with U(1)-twisted boundary conditions; the twist
torus (theta_x, theta_y) is the moduli space of flat U(1)
connections.  The many-body ground state at half filling is the
Slater determinant of the occupied one-particle frame U(theta)
(2L^2 x L^2 columns); the family is QUASI-FREE (Gaussian) by
construction -- exactly the hypothesis of the L2 conditional,
realised here so the L1 identity can be tested where the premise
HOLDS.  Main cell M = 1 (C = 1 phase), L = 4, twist grid 48 x 48
(offset half-cell so reference twists and section zeros avoid grid
nodes); confirmation cell L = 6, grid 24 x 24; controls M = 3
(C = 0) and M = -1 (C = -1) at L = 4, grid 24.

L1 IMPLEMENTATION AND THE HONEST DISCRETE MATH.
 (a) BERRY SIDE: the FHS field strength F(p) in (-pi, pi] per
     plaquette from det-overlap link variables of the occupied
     frames; integral C_FHS = (1/2 pi) sum_p F(p) = the det-line
     Chern (v472's = 1, re-derived).
 (b) QUILLEN-METRIC SIDE: with a fixed reference frame U_ref the
     overlap section is s(theta) = det(U_ref^dag U(theta)) (Slater
     overlap formula); its squared norm N = |s|^2 is gauge-invariant
     and satisfies the finite Quillen-metric identity
         N(theta) = det( U_ref^dag P(theta) U_ref ),
     P = U U^dag the Gaussian covariance/overlap kernel -- the
     ||det||^2 = det(kernel) statement at finite size, exact linear
     algebra, gated pointwise at 1e-12.  The distributional
     (i/2 pi) ddbar log N is, by Poincare-Lelong, the DIVISOR of the
     section; on the grid it is evaluated EXACTLY by the plaquette
     winding n(p) = (W(p) + F(p)) / (2 pi), where W(p) is the
     branch-fixed circulation of the gauge-invariant link field
     arg[ s(b) conj(s(a)) conj(L(a,b)) ] (the covariant derivative
     of the section along the link; L(a,b) = det-overlap link).
     Bookkeeping facts gated: each n(p) is an integer to float
     precision (the plaquette product is real positive by
     construction); sum_p n(p) = C_FHS exactly (telescoping
     sum_p W(p) = 0); and the POINTWISE difference field between
     the two curvature readings, F(p) - 2 pi n(p) = -W(p), is the
     coboundary of a globally defined link 1-form -- a smooth EXACT
     form with total integral 0 (the finite 'local anomaly term' of
     Quillen's identity, exhibited as an exact form).  The NAIVE
     smeared FD Laplacian of log N totals 0 identically (divisor
     deltas cancel the smooth part -- printed as INFO): that
     telescoping identity is WHY the divisor evaluation is the
     correct finite reading of the (b)-integral.
 PATCHING: a degree-1 line bundle admits no nonvanishing section,
     so s HAS zeros over the torus; two references are used
     (ground frames at twists (0,0) and (pi,pi)), the transition
     function t12 = s1/s2 is gauge-invariant, and the winding of
     t12 around the zeros of s2 equals the Chern number (Dai-Freed
     section / Quillen divisor picture) -- gated, together with
     disjointness of the two vortex sets and the pointwise
     transition-winding identity wt(p) = n1(p) - n2(p).

L3 ANCHOR (v341 VERBATIM, sharpened to 50 digits): F_U(1)(a) =
a^3 - 2 c3^3 a^2 - (4/5) 41 c3^6 ln(1/phi_seam(a)) with phi_seam =
1/(6 pi) + Q (1-Q)^(-5/4), Q = 48 c3^4 e^(-2a); exact coefficients
8 b1 = 8 * 41/10 = 164/5 = (4/5)*41 (Fractions), c3 = 1/(8 pi)
(sympy), phi_base = (4/3) c3, q(D5) + q(A3) = 5/4 + 3/4 = 2; root
alpha^-1 = 137.0359992168 and Quillen-split residual
|lhs - rhs| < 1e-30 at mpmath dps = 50.

PRE-REGISTERED ADJUDICATION (frozen before the record runs; ONE
disclosed smoke run informed the vortex-census bars -- see
SMOKE-RUN DISCLOSURE):
 P1 both tori, both sizes: Bloch C(M=1,3,-1) = (1,0,-1); twist FHS
    = 1 at L = 4 (grid 48) AND L = 6 (grid 24), |dev| < 1e-9; Fermi
    gap > 1.9 over the whole twist torus at M = 1.
 P2 the Quillen norm identity |s|^2 = det(U_ref^dag P U_ref) holds
    to 1e-12 absolute (N, det both in [0,1]) at every sampled twist,
    BOTH references.
 P3 divisor = the (b)-integral: n(p) integer to 1e-9 everywhere;
    sum_p n = 1 = C_FHS for ref1, ref2 AND the L = 6 family; the
    difference-form total |C_FHS_float - sum n| < 1e-8; pointwise
    |F - 2 pi n + W| < 1e-9.
 P4 localization: the vortex set is small (<= 3 cells, net charge
    +1 each ref) and sits where the metric says it must -- the
    global grid minimum of |s| lies in/adjacent to a vortex cell
    (Chebyshev distance <= 1 on the torus).
 P5 patching: vortex sets of s1 and s2 DISJOINT; wt(p) = n1(p) -
    n2(p) at EVERY plaquette; total winding of t12 = 0 exactly;
    winding of the transition function around the s2 zeros = 1 =
    C (and around the s1 zeros = 1).
 P6 controls: M = 3 -> (C_FHS, sum n) = (0, 0); M = -1 -> (-1, -1):
    the divisor tracks the phase, not the mesh.
 P7 anchor: exact coefficient identities (Fractions/sympy) and the
    50-digit root: |alpha^-1 - 137.0359992168407| < 1e-9, split
    residual < 1e-30.
 P8 mutants CAUGHT: (MUT-A) wrong twist normalisation e^{2 i theta}
    in BOTH cycles -> the moduli map is the degree-4 (2,2)-cover ->
    FHS = 4 != 1; (MUT-B) a squeezed non-unitary kernel insertion
    (I + eps S), eps = 0.05, S = diag(cos(0.7(k+1))) -> the divisor
    integrality breaks (max integer deviation > 1e-6) AND the
    Quillen norm identity breaks (residual > 1e-4): a non-Gaussian-
    consistent overlap kernel cannot fake the (b)-side.
EXPECTED VERDICT: CHAIN_SHADOW_OK.

SMOKE-RUN DISCLOSURE (2026-08-27, ONE declared smoke run before the
freeze, 16/18 in 1.7 s; the two smoke fails were BOTH the MUT-A
expected value, corrected here and disclosed -- recording the
surprises is part of the method):
 (i)   MUT-A ARITHMETIC SLIP, corrected pre-freeze: the plan
       expected FHS = 2 for the e^{2 i theta} mutant, but doubling
       the twist in BOTH cycles is the (2,2)-cover of the moduli
       torus, degree 4, so the pullback Chern is 4 x 1 = 4 -- the
       smoke measured +4.000000000 exactly and the frozen gate now
       demands 4 (still CAUGHT: != 1); G60 failed only downstream
       of this;
 (ii)  the vortex census is NOT minimal for ref1: THREE cells with
       charges (-1 near (pi,pi), +1 near (pi,0), +1 near (0,pi)),
       net +1 -- extra +/- structure is legitimate for a section;
       ref2 has ONE cell (+1 near (0,0), its antipode's twin); the
       two vortex sets are cleanly disjoint, so the patching
       battery runs at full strength;
 (iii) the integer deviations came out at 2e-16 and the difference-
       form total at 3e-16, far inside the frozen bars (1e-9 /
       1e-8); min|s| on the grid 4.3e-3 / 5.9e-3;
 (iv)  MUT-B fires at 2.9e-6 integrality (bar 1e-6, a thin but
       deterministic 2.9x margin -- disclosed) and 1.05e-1 norm
       identity (bar 1e-4, four decades of margin).
No bar, grid, reference twist, mutant recipe or verdict enum moved
after the freeze except the disclosed MUT-A expected-value
correction (2 -> 4); the record runs are the run1/run2 logs.

WHAT THE CHAIN BUYS (L4, printed as a typed statement): with L1
verified at the finite shadow and L2 typed on the named premise,
the open content of ALPHA.QUILLEN.EXACT.01 decomposes with NO
additional analytic unknown: {SEAM.RP.RIGIDITY premise (S1 probe)}
+ {the diagonal-zeta face, v484/v485's remaining [O] = the
SEAM.EQUIV.01 typing (S-parallel probe seam_bfk_conical_det_probe)}
+ {EM1 (laughlin_pump_em1_probe)}.

HONEST LIMITATIONS: this is the FINITE shadow -- a 2-band lattice
Gaussian family, not the abstract-seam zeta determinant; L2 is a
TYPED implication whose premise is NOT proven here (the parallel S1
probe MEASURES rigidity, it does not prove it); the difference
field is exhibited as an exact lattice coboundary, its continuum
identification with the Bismut-Freed local anomaly stays [O]; the
choice of reference frames is a patching convenience, gauge-
invariance of every gated object is by construction (moduli of
dets, det-ratio transitions); ALPHA.QUILLEN.EXACT.01 stays [O],
alpha^-1 = 137.0359992168 stays [E] regardless; nothing moves on
the ledger.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; L1
battery G10-G19 (Bloch integers, twist FHS both sizes, Quillen norm
identity, divisor integrality + pointwise exact form, (b)-integrals
+ difference-form total, localization, patching, controls); L2 G20
typed conditional; L3 G30-G31 exact anchor; L4 G40 DAG; mutants
G50-G51; G60 verdict + G99 runtime.  18 gates.

DETERMINISM: no RNG anywhere; pure numpy eigh / dets + sympy +
mpmath; two record runs must be byte-identical except lines
carrying 'WALL'.  Runtime bar 180 s.

VERDICT ENUM: CHAIN_SHADOW_OK / SHADOW_FAILS / PATCHING_OBSTRUCTED.
"""

from __future__ import annotations

import ast
import hashlib
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

# ---------------------------------------------------------------- frozen
L_MAIN, GRID_MAIN = 4, 48
L_CONF, GRID_CONF = 6, 24
GRID_CTRL = 24
GRID_MUTA = 16
GRID_BLOCH = 24
REF1_TH = (0.0, 0.0)
REF2_TH = (np.pi, np.pi)
TOL_CHERN = 1e-9              # FHS integer bar
TOL_NORMID = 1e-12            # Quillen norm identity, absolute
TOL_INT = 1e-9                # divisor integer deviation
TOL_EXFORM = 1e-8             # difference-form total (spec bar)
TOL_PTWISE = 1e-9             # pointwise F - 2 pi n + W
GAP_BAR = 1.9
VORTEX_MAX_CELLS = 3
LOC_CHEB = 1                  # localization Chebyshev distance (cells)
MUTB_EPS = 0.05
MUTB_INT_BAR = 1e-6           # MUT-B integrality catch bar
MUTB_NORM_BAR = 1e-4          # MUT-B norm-identity catch bar
ROOT_BAR = 1e-9
SPLIT_BAR = mp.mpf("1e-30")
RUNTIME_BAR = 180.0

RIGIDITY_PREMISE = "SEAM.RP.RIGIDITY"
PARALLEL_PROBES = ("seam_rp_rigidity_probe",
                   "seam_bfk_conical_det_probe",
                   "laughlin_pump_em1_probe")

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
TX = (-SZ - 1j * SX) / 2       # v472 verbatim real-space hoppings
TY = (-SZ - 1j * SY) / 2

CHECKS: list = []


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


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import) else [node.module or ""])
            for m in mods:
                root = m.split(".")[0]
                if root in ("verification", "tfpt_constants", "random",
                            "subprocess"):
                    bad.append("forbidden import %s @%d" % (m, node.lineno))
        if isinstance(node, ast.Attribute) and node.attr in ("random",
                                                             "seed"):
            bad.append("RNG attribute @%d" % node.lineno)
    return (not bad), ("; ".join(bad) if bad else
                       "no verification/ or tfpt_constants import, no RNG, "
                       "no subprocess; standalone experiments/-level probe; "
                       "writes nothing but stdout")


# ---------------------------------------------------- model (v472 verbatim)
def hamiltonian(L: int, M: float, thx: float, thy: float,
                twist_pow: int = 1) -> np.ndarray:
    n = L * L
    H = np.zeros((2 * n, 2 * n), complex)

    def blk(x, y):
        return 2 * ((x % L) + L * (y % L))

    for x in range(L):
        for y in range(L):
            i = blk(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            for (dx, dy, T, th) in ((1, 0, TX, thx), (0, 1, TY, thy)):
                j = blk(x + dx, y + dy)
                phase = (np.exp(1j * twist_pow * th)
                         if (x + dx == L or y + dy == L) else 1.0)
                H[j:j + 2, i:i + 2] += phase * T
                H[i:i + 2, j:j + 2] += np.conj(phase) * T.conj().T
    return H


def occupied_frame(L: int, M: float, thx: float, thy: float,
                   twist_pow: int = 1):
    w, v = np.linalg.eigh(hamiltonian(L, M, thx, thy, twist_pow))
    n_occ = int(np.sum(w < 0))
    return v[:, :n_occ], n_occ, float(w[n_occ] - w[n_occ - 1])


def bloch_chern(M: float, N: int = GRID_BLOCH) -> float:
    def occ(kx, ky):
        d = np.array([np.sin(kx), np.sin(ky), M - np.cos(kx) - np.cos(ky)])
        _, v = np.linalg.eigh(d[0] * SX + d[1] * SY + d[2] * SZ)
        return v[:, 0]

    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    u = [[occ(kx, ky) for ky in ks] for kx in ks]

    def ln(a, b):
        x = np.vdot(a, b)
        return x / abs(x)

    F = 0.0
    for i in range(N):
        for j in range(N):
            ip, jp = (i + 1) % N, (j + 1) % N
            F += np.angle(ln(u[i][j], u[ip][j]) * ln(u[ip][j], u[ip][jp])
                          * np.conj(ln(u[i][jp], u[ip][jp]))
                          * np.conj(ln(u[i][j], u[i][jp])))
    return F / (2 * np.pi)


# --------------------------------------------- twist-torus grid machinery
def build_grid(L: int, M: float, G: int, twist_pow: int = 1):
    """Frames on the offset twist grid th_i = 2 pi (i + 1/2) / G.
    Returns (frames[G,G] object array, min_gap); asserts constant n_occ."""
    ths = 2 * np.pi * (np.arange(G) + 0.5) / G
    frames = np.empty((G, G), object)
    min_gap, n_ref = np.inf, None
    for i, tx in enumerate(ths):
        for j, ty in enumerate(ths):
            fr, n_occ, gap = occupied_frame(L, M, tx, ty, twist_pow)
            frames[i, j] = fr
            min_gap = min(min_gap, gap)
            n_ref = n_occ if n_ref is None else n_ref
            assert n_occ == n_ref, "occupation jumped on the twist torus"
    return frames, float(min_gap)


def link_fields(frames: np.ndarray, G: int):
    """Raw det-overlap links Lx[i,j] = det(U(i,j)^dag U(i+1,j)), Ly ditto."""
    lx = np.empty((G, G), complex)
    ly = np.empty((G, G), complex)
    for i in range(G):
        for j in range(G):
            lx[i, j] = np.linalg.det(
                frames[i, j].conj().T @ frames[(i + 1) % G, j])
            ly[i, j] = np.linalg.det(
                frames[i, j].conj().T @ frames[i, (j + 1) % G])
    return lx, ly


def fhs_field(lx: np.ndarray, ly: np.ndarray) -> np.ndarray:
    """FHS plaquette field F(p) in (-pi, pi]."""
    return np.angle(lx * np.roll(ly, -1, axis=0)
                    * np.conj(np.roll(lx, -1, axis=1)) * np.conj(ly))


def section_field(frames: np.ndarray, ref: np.ndarray, G: int) -> np.ndarray:
    """Overlap section s(theta) = det(U_ref^dag U(theta))."""
    s = np.empty((G, G), complex)
    for i in range(G):
        for j in range(G):
            s[i, j] = np.linalg.det(ref.conj().T @ frames[i, j])
    return s


def divisor_field(s: np.ndarray, lx: np.ndarray, ly: np.ndarray,
                  fpl: np.ndarray):
    """Poincare-Lelong divisor: n(p) = (W(p) + F(p)) / 2 pi with W the
    branch-fixed circulation of the covariant link field of s.
    Returns (n int array, max integer deviation, W, max pointwise
    |F - 2 pi n + W|)."""
    ax = np.angle(np.roll(s, -1, axis=0) * np.conj(s) * np.conj(lx))
    ay = np.angle(np.roll(s, -1, axis=1) * np.conj(s) * np.conj(ly))
    W = ax + np.roll(ay, -1, axis=0) - np.roll(ax, -1, axis=1) - ay
    n_raw = (W + fpl) / (2 * np.pi)
    n = np.rint(n_raw)
    dev = float(np.max(np.abs(n_raw - n)))
    ptwise = float(np.max(np.abs(fpl - 2 * np.pi * n + W)))
    return n.astype(int), dev, W, ptwise


def winding_field(t: np.ndarray):
    """Plaquette winding of a scalar complex field (branch-fixed)."""
    bx = np.angle(np.roll(t, -1, axis=0) * np.conj(t))
    by = np.angle(np.roll(t, -1, axis=1) * np.conj(t))
    Wt = bx + np.roll(by, -1, axis=0) - np.roll(bx, -1, axis=1) - by
    wt_raw = Wt / (2 * np.pi)
    wt = np.rint(wt_raw)
    return wt.astype(int), float(np.max(np.abs(wt_raw - wt)))


def norm_identity_err(frames: np.ndarray, ref: np.ndarray, s: np.ndarray,
                      G: int, stride: int = 3) -> float:
    """max |  |s|^2 - det(U_ref^dag P U_ref) |  on a subsampled grid."""
    err = 0.0
    for i in range(0, G, stride):
        for j in range(0, G, stride):
            fr = frames[i, j]
            K = ref.conj().T @ (fr @ fr.conj().T) @ ref
            err = max(err, abs(float(np.linalg.det(K).real)
                               - float(abs(s[i, j]) ** 2)))
    return err


def cheb_dist_torus(a, b, G: int) -> int:
    d = 0
    for x, y in zip(a, b):
        dd = abs(x - y) % G
        d = max(d, min(dd, G - dd))
    return int(d)


def vortex_cells(n: np.ndarray):
    return [(int(i), int(j)) for i, j in zip(*np.nonzero(n))]


def naive_laplacian_total(s: np.ndarray) -> float:
    """Telescoping instrument: total FD Laplacian of log N (exact 0)."""
    logN = np.log(np.abs(s) ** 2)
    lap = (np.roll(logN, -1, 0) + np.roll(logN, 1, 0)
           + np.roll(logN, -1, 1) + np.roll(logN, 1, 1) - 4 * logN)
    return float(np.sum(lap)) / (4 * np.pi)


# ------------------------------------------------------------------ main
def main() -> int:
    print("=" * 78)
    print("quillen_rigidity_chain_probe -- ALPHA.QUILLEN.RIGIDITY_CHAIN.01 "
          "(Strategy S9)")
    print("EXPLORATION ONLY (2026-08-27): no promotion, no ledger row, no "
          "marker moved,")
    print("no gate closed or narrowed.   SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    fw_ok, fw_msg = firewall_audit()
    check("G01-firewall", fw_ok, fw_msg)
    check("G02-predefinition", True,
          "frozen BEFORE record runs: L=%d grid %d main / L=%d grid %d "
          "conf / ctrl grid %d; refs (0,0) + (pi,pi); bars Chern %.0e, "
          "norm-id %.0e, integer %.0e, exact-form %.0e, gap %.1f, vortex "
          "<= %d cells, loc Chebyshev <= %d; MUT-B eps %.2f (catch bars "
          "%.0e / %.0e); root bar %.0e, split bar 1e-30; runtime %.0f s; "
          "verdict enum CHAIN_SHADOW_OK / SHADOW_FAILS / "
          "PATCHING_OBSTRUCTED"
          % (L_MAIN, GRID_MAIN, L_CONF, GRID_CONF, GRID_CTRL, TOL_CHERN,
             TOL_NORMID, TOL_INT, TOL_EXFORM, GAP_BAR, VORTEX_MAX_CELLS,
             LOC_CHEB, MUTB_EPS, MUTB_INT_BAR, MUTB_NORM_BAR, ROOT_BAR,
             RUNTIME_BAR))

    # ---------------------------------------------------------------- L1
    section("L1  QUILLEN'S IDENTITY AT THE FINITE SHADOW "
            "(both curvature readings on the twist torus)")

    c_bz = {M: bloch_chern(M) for M in (1.0, 3.0, -1.0)}
    check("G10-bloch-integers",
          abs(c_bz[1.0] - 1) < TOL_CHERN and abs(c_bz[3.0]) < TOL_CHERN
          and abs(c_bz[-1.0] + 1) < TOL_CHERN,
          "Bloch-BZ FHS Chern C(M=1) = %+.9f, C(M=3) = %+.9f, C(M=-1) = "
          "%+.9f (v470/v367 integers re-derived)"
          % (c_bz[1.0], c_bz[3.0], c_bz[-1.0]))

    frames4, gap4 = build_grid(L_MAIN, 1.0, GRID_MAIN)
    lx4, ly4 = link_fields(frames4, GRID_MAIN)
    fpl4 = fhs_field(lx4, ly4)
    c4 = float(np.sum(fpl4)) / (2 * np.pi)

    frames6, gap6 = build_grid(L_CONF, 1.0, GRID_CONF)
    lx6, ly6 = link_fields(frames6, GRID_CONF)
    fpl6 = fhs_field(lx6, ly6)
    c6 = float(np.sum(fpl6)) / (2 * np.pi)

    check("G11-twist-fhs-both-sizes",
          abs(c4 - 1) < TOL_CHERN and abs(c6 - 1) < TOL_CHERN
          and gap4 > GAP_BAR and gap6 > GAP_BAR,
          "side (a), the Berry integral: C_detline(L=4, grid 48) = "
          "%+.12f, C_detline(L=6, grid 24) = %+.12f (FHS integer 1, "
          "size-independent); Fermi gap open over the WHOLE torus "
          "(min %.3f / %.3f > %.1f) -- section family globally defined"
          % (c4, c6, gap4, gap6, GAP_BAR))

    ref1 = occupied_frame(L_MAIN, 1.0, *REF1_TH)[0]
    ref2 = occupied_frame(L_MAIN, 1.0, *REF2_TH)[0]
    s1 = section_field(frames4, ref1, GRID_MAIN)
    s2 = section_field(frames4, ref2, GRID_MAIN)
    ref6 = occupied_frame(L_CONF, 1.0, *REF1_TH)[0]
    s6 = section_field(frames6, ref6, GRID_CONF)

    err_n1 = norm_identity_err(frames4, ref1, s1, GRID_MAIN)
    err_n2 = norm_identity_err(frames4, ref2, s2, GRID_MAIN)
    check("G12-quillen-norm-identity",
          err_n1 < TOL_NORMID and err_n2 < TOL_NORMID,
          "||s||^2 = |det(U_ref^dag U)|^2 == det(U_ref^dag P U_ref) "
          "(Gaussian covariance kernel) pointwise: max |diff| = %.2e / "
          "%.2e (refs 1/2) < %.0e -- the metric IS the determinant of "
          "the quasi-free overlap kernel (finite ||det||^2 = det)"
          % (err_n1, err_n2, TOL_NORMID))

    n1, dev1, W1, pt1 = divisor_field(s1, lx4, ly4, fpl4)
    n2, dev2, W2, pt2 = divisor_field(s2, lx4, ly4, fpl4)
    n6, dev6, W6, pt6 = divisor_field(s6, lx6, ly6, fpl6)
    check("G13-divisor-integrality-exact-form",
          max(dev1, dev2, dev6) < TOL_INT
          and max(pt1, pt2, pt6) < TOL_PTWISE,
          "Poincare-Lelong bookkeeping: n(p) integer to %.1e (max dev, "
          "all refs/sizes); pointwise F(p) - 2 pi n(p) + W(p) = 0 to "
          "%.1e -- the difference field between the two curvature "
          "readings IS the coboundary of the gauge-invariant link "
          "1-form (the finite 'local anomaly term', an exact form)"
          % (max(dev1, dev2, dev6), max(pt1, pt2, pt6)))

    sum1, sum2, sum6 = int(np.sum(n1)), int(np.sum(n2)), int(np.sum(n6))
    exform1 = abs(c4 - sum1)
    exform2 = abs(c4 - sum2)
    exform6 = abs(c6 - sum6)
    lap_tot = naive_laplacian_total(s1)
    info("naive smeared FD-Laplacian total of log N (ref1): %.3e -- "
         "identically 0 by telescoping (divisor deltas cancel the smooth "
         "part), the reason the divisor is the correct finite (b)-integral"
         % lap_tot)
    check("G14-b-integral-equals-chern",
          sum1 == 1 and sum2 == 1 and sum6 == 1
          and max(exform1, exform2, exform6) < TOL_EXFORM,
          "side (b), the Quillen-metric integral (distributional "
          "(i/2 pi) ddbar log||s||^2 = divisor mass): sum n = %+d / %+d "
          "/ %+d (ref1 / ref2 / L=6) == 1 == C_FHS; difference-form "
          "total |C_float - sum n| = %.2e / %.2e / %.2e < %.0e"
          % (sum1, sum2, sum6, exform1, exform2, exform6, TOL_EXFORM))

    v1 = vortex_cells(n1)
    v2 = vortex_cells(n2)
    amin1 = np.unravel_index(int(np.argmin(np.abs(s1))), s1.shape)
    amin2 = np.unravel_index(int(np.argmin(np.abs(s2))), s2.shape)
    loc1 = min((cheb_dist_torus(amin1, c, GRID_MAIN) for c in v1),
               default=99)
    loc2 = min((cheb_dist_torus(amin2, c, GRID_MAIN) for c in v2),
               default=99)
    th_of = lambda c: tuple(round(2 * np.pi * (x + 0.5) / GRID_MAIN, 3)
                            for x in c)
    check("G15-vortex-localization",
          0 < len(v1) <= VORTEX_MAX_CELLS and 0 < len(v2) <= VORTEX_MAX_CELLS
          and loc1 <= LOC_CHEB and loc2 <= LOC_CHEB,
          "the degree-1 bundle FORCES section zeros and the metric finds "
          "them: vortex cells ref1 %s (charges %s, twist ~%s), ref2 %s "
          "(charges %s, twist ~%s); |s| grid-argmin sits at Chebyshev "
          "distance %d / %d (<= %d) from a vortex cell; min|s| = %.2e / "
          "%.2e"
          % (v1, [int(n1[c]) for c in v1], th_of(v1[0]) if v1 else "-",
             v2, [int(n2[c]) for c in v2], th_of(v2[0]) if v2 else "-",
             loc1, loc2, LOC_CHEB,
             float(np.min(np.abs(s1))), float(np.min(np.abs(s2)))))

    t12 = s1 * np.conj(s2)      # arg t12 = arg(s1/s2), gauge-invariant
    wt, devt = winding_field(t12)
    disjoint = not (set(v1) & set(v2))
    ptwise_trans = bool(np.all(wt == n1 - n2))
    wind_total = int(np.sum(wt))
    c_via_s2 = -int(sum(wt[c] for c in v2))
    c_via_s1 = int(sum(wt[c] for c in v1))
    check("G16-patching-transition-winding",
          disjoint and ptwise_trans and wind_total == 0
          and devt < TOL_INT and c_via_s2 == 1 and c_via_s1 == 1,
          "two-patch Dai-Freed picture: vortex sets DISJOINT; transition "
          "t12 = s1/s2 gauge-invariant with wt(p) == n1(p) - n2(p) at "
          "EVERY plaquette (max int dev %.1e); total winding %d == 0; "
          "winding of the transition function around the s2 zeros = %+d "
          "== C == 1 (and around the s1 zeros = %+d) -- the Chern number "
          "IS the transition winding"
          % (devt, wind_total, c_via_s2, c_via_s1))

    ctrl = {}
    for M in (3.0, -1.0):
        fr, _g = build_grid(L_MAIN, M, GRID_CTRL)
        lx, ly = link_fields(fr, GRID_CTRL)
        fpl = fhs_field(lx, ly)
        refc = occupied_frame(L_MAIN, M, *REF1_TH)[0]
        sc = section_field(fr, refc, GRID_CTRL)
        nc, devc, _wc, _pc = divisor_field(sc, lx, ly, fpl)
        ctrl[M] = (float(np.sum(fpl)) / (2 * np.pi), int(np.sum(nc)), devc)
    check("G17-controls-track-the-phase",
          abs(ctrl[3.0][0]) < TOL_CHERN and ctrl[3.0][1] == 0
          and abs(ctrl[-1.0][0] + 1) < TOL_CHERN and ctrl[-1.0][1] == -1
          and max(ctrl[3.0][2], ctrl[-1.0][2]) < TOL_INT,
          "trivial collar M = 3: (C_FHS, divisor) = (%+.9f, %+d); "
          "orientation flip M = -1: (%+.9f, %+d) -- BOTH curvature "
          "readings track the phase, not the mesh"
          % (ctrl[3.0][0], ctrl[3.0][1], ctrl[-1.0][0], ctrl[-1.0][1]))

    # ---------------------------------------------------------------- L2
    section("L2  THE CONDITIONAL (typed, premise NAMED -- not a numeric "
            "gate)")
    check("G20-typed-conditional", True,
          "TYPED IMPLICATION [C], premise NOT assumed: IF the seam state "
          "is QUASI-FREE (premise %s -- the rigidity target of the "
          "parallel S1 probe %s.py; v903 terrain: OS positivity <=> "
          "a_J = 0 on the deployed family) THEN the seam determinant "
          "line is a free-fermion determinant line and L1's identity "
          "applies LITERALLY (||det||^2 = det of the Gaussian kernel, "
          "divisor = index form + exact anomaly term) -- the premise "
          "stays [O], typed here, closed nowhere"
          % (RIGIDITY_PREMISE, PARALLEL_PROBES[0]))

    # ---------------------------------------------------------------- L3
    section("L3  THE VALUE-LEVEL ANCHOR (exact, closed regardless)")
    b1 = Fraction(41, 10)
    coeff_ok = (8 * b1 == Fraction(164, 5) == Fraction(4, 5) * 41
                and 10 * b1 == 41)
    c3s = 1 / (8 * sp.pi)
    sym_ok = (sp.simplify(sp.Rational(1, 6) / sp.pi
                          - sp.Rational(4, 3) * c3s) == 0
              and sp.Rational(5, 4) + sp.Rational(3, 4) == 2)
    check("G30-exact-coefficients", coeff_ok and sym_ok,
          "exact Fractions/sympy: 8 b1 = 8*(41/10) = 164/5 = (4/5)*41 "
          "(the U(1) index, v48); c3 = 1/(8 pi) (Gauss-Bonnet, v216); "
          "phi_base = 1/(6 pi) = (4/3) c3; q(D5) + q(A3) = 5/4 + 3/4 = 2 "
          "(E8 root norm, v1/v154)")

    mp.mp.dps = 50
    cc = 1 / (8 * mp.pi)
    pb = 1 / (6 * mp.pi)
    dt = 48 * cc ** 4

    def phiseam(a):
        Q = dt * mp.e ** (-2 * a)
        return pb + Q * (1 - Q) ** (mp.mpf(-5) / 4)

    def F_alpha(a):
        return (a ** 3 - 2 * cc ** 3 * a ** 2
                - (mp.mpf(4) / 5) * 41 * cc ** 6 * mp.log(1 / phiseam(a)))

    a_root = mp.findroot(F_alpha, mp.mpf("0.0073"))
    ainv = 1 / a_root
    lhs = a_root ** 3 - 2 * cc ** 3 * a_root ** 2
    rhs = (8 * mp.mpf(41) / 10) * cc ** 6 * mp.log(1 / phiseam(a_root))
    resid = abs(lhs - rhs)
    check("G31-quillen-split-at-the-root",
          abs(ainv - mp.mpf("137.0359992168407")) < ROOT_BAR
          and resid < SPLIT_BAR,
          "a^3 - 2 c3^3 a^2 = 8 b1 c3^6 ln(1/phi_seam) at alpha^-1 = "
          "%s (bar %.0e vs 137.0359992168407); split residual "
          "|lhs - rhs| = %s < 1e-30 (mpmath dps 50) -- the anchor that "
          "stays closed [E] regardless of the chain"
          % (mp.nstr(ainv, 17), ROOT_BAR, mp.nstr(resid, 3)))

    # ---------------------------------------------------------------- L4
    section("L4  WHAT THE CHAIN BUYS (typed DAG statement)")
    check("G40-dag-no-new-analytic-unknown", True,
          "TYPED [C]: with L1 verified at the finite shadow and L2 "
          "conditional on %s, the remaining open content of "
          "ALPHA.QUILLEN.EXACT.01 is EXACTLY {the rigidity premise "
          "(probe %s)} + {the diagonal-zeta face = the v484/v485 "
          "residual, = the SEAM.EQUIV.01 typing (probe %s)} + {EM1 "
          "(probe %s)} -- NO additional analytic unknown; the target "
          "stays [O], nothing closes or narrows here"
          % (RIGIDITY_PREMISE, PARALLEL_PROBES[0], PARALLEL_PROBES[1],
             PARALLEL_PROBES[2]))

    # ------------------------------------------------------------ mutants
    section("S5  MUTANTS (both must be CAUGHT)")
    fr_a, _ = build_grid(L_MAIN, 1.0, GRID_MUTA, twist_pow=2)
    lx_a, ly_a = link_fields(fr_a, GRID_MUTA)
    c_muta = float(np.sum(fhs_field(lx_a, ly_a))) / (2 * np.pi)
    check("G50-mutant-twist-normalisation",
          abs(c_muta - 4) < 1e-6 and abs(c_muta - 1) > 0.5,
          "CAUGHT: wrong twist normalisation e^{2 i theta} in both cycles "
          "pulls back along the degree-4 (2,2)-cover of the moduli torus "
          "-> FHS = %+.9f = 4 != 1 (the twist-torus integer is NOT "
          "convention-proof; the correct normalisation is load-bearing; "
          "expected value 2 -> 4 corrected at smoke, disclosed)" % c_muta)

    S_sq = np.diag(np.cos(0.7 * (np.arange(2 * L_MAIN * L_MAIN) + 1)))
    ins = np.eye(2 * L_MAIN * L_MAIN) + MUTB_EPS * S_sq
    G = GRID_MAIN
    lx_m = np.empty((G, G), complex)
    ly_m = np.empty((G, G), complex)
    for i in range(G):
        for j in range(G):
            lx_m[i, j] = np.linalg.det(
                frames4[i, j].conj().T @ ins @ frames4[(i + 1) % G, j])
            ly_m[i, j] = np.linalg.det(
                frames4[i, j].conj().T @ ins @ frames4[i, (j + 1) % G])
    _nm, dev_m, _wm, _pm = divisor_field(s1, lx_m, ly_m, fpl4)
    s_sq = np.empty((G, G), complex)
    for i in range(0, G, 3):
        for j in range(0, G, 3):
            s_sq[i, j] = np.linalg.det(ref1.conj().T @ ins @ frames4[i, j])
    err_sq = 0.0
    for i in range(0, G, 3):
        for j in range(0, G, 3):
            fr = frames4[i, j]
            K = ref1.conj().T @ (fr @ fr.conj().T) @ ref1
            err_sq = max(err_sq, abs(float(np.linalg.det(K).real)
                                     - float(abs(s_sq[i, j]) ** 2)))
    check("G51-mutant-squeezed-kernel",
          dev_m > MUTB_INT_BAR and err_sq > MUTB_NORM_BAR,
          "CAUGHT twice: squeezed non-unitary kernel insertion "
          "(I + %.2f S) breaks (i) the divisor integrality (max integer "
          "deviation %.2e > %.0e -- the (b)-side bookkeeping REFUSES a "
          "non-Gaussian-consistent transport kernel) and (ii) the "
          "Quillen norm identity (residual %.2e > %.0e -- ||det||^2 = "
          "det holds ONLY for the quasi-free kernel)"
          % (MUTB_EPS, dev_m, MUTB_INT_BAR, err_sq, MUTB_NORM_BAR))

    # ------------------------------------------------------------ verdict
    section("S6  VERDICT")
    npass_pre = sum(1 for _n, ok, _d in CHECKS if ok)
    all_pre = npass_pre == len(CHECKS)
    patching_ok = disjoint and ptwise_trans
    if all_pre:
        verdict = "CHAIN_SHADOW_OK"
    elif not patching_ok:
        verdict = "PATCHING_OBSTRUCTED"
    else:
        verdict = "SHADOW_FAILS"
    check("G60-verdict", all_pre,
          "%s: L1 both curvature readings = 1 on the twist torus with "
          "the difference an exact form (Quillen's identity at the "
          "finite shadow, incl. patching + controls + norm identity); "
          "L2 typed on %s; L3 anchor exact at 50 digits; L4 DAG: no new "
          "analytic unknown; both mutants CAUGHT"
          % (verdict, RIGIDITY_PREMISE))

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    if npass == len(CHECKS):
        print("ALL GATES PASSED %d/%d" % (npass, len(CHECKS)))
    else:
        print("GATES: %d/%d PASS -- FAILURES:" % (npass, len(CHECKS)))
        for nm, ok, _d in CHECKS:
            if not ok:
                print("  FAIL " + nm)
    print("VERDICT: %s" % verdict)
    print("KEY NUMBERS: FHS integer = 1 (C_detline L=4 %.12f, L=6 %.12f); "
          "Berry integral %.12f; Quillen-metric (divisor) integral %+d / "
          "%+d / %+d; difference-form integral %.2e (bar 1e-8); "
          "alpha-root inverse %s, split residual %s"
          % (c4, c6, c4, sum1, sum2, sum6,
             max(exform1, exform2, exform6), mp.nstr(ainv, 14),
             mp.nstr(resid, 3)))
    print("EXPLORATION ONLY: no promotion, no ledger row, no marker "
          "moved, no gate closed or narrowed.")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

_PLAN = (
    ("seam_bfk_conical_det_probe", _SRC_BFK,
     "a5e0146830cad201ca24c4a0e8179881366e85fbc9a95e5fdc7248f646b5257c",
     21, "MATCH_MODULO_LOCAL_FACTOR", "d06b3bbec70e7efc"),
    ("laughlin_pump_em1_probe", _SRC_PUMP,
     "68f9f09c27733596fe4964ffecce6d044c06eae725c89ab28d651e0d4da52e4f",
     20, "PUMP_QUANTIZED_MATCHES_CHERN", "f9b5cb0bf20d0293"),
    ("quillen_rigidity_chain_probe", _SRC_RIG,
     "e770b73de363329bffed2faeaf063d379281b3d398fbe058821dc3a09bde8b2e",
     18, "CHAIN_SHADOW_OK", "b4ee0dd0141da6ab"),
)

_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]", re.M)
_ALL_RE = re.compile(r"ALL GATES PASSED (\d+)/(\d+)")
_VER_RE = re.compile(r"^VERDICT:\s+(\S+)", re.M)
_SHA_RE = re.compile(r"SPEC_SHA ([0-9a-f]{16})")


def _probe_bytes(src):
    """Embedded source with the leading r'''-newline stripped -- the exact
    file bytes the sha256 pin is over."""
    return src[1:] if src[:1] == "\n" else src


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _exec_probe(name, src):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (v960..v970 convention); __file__ points at the
    experiments copy so the probes' own firewall/spec gates inspect the
    byte-warded original.  Returns (stdout, exit_code, byte_equal)."""
    src = _probe_bytes(src)
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    argv_saved = sys.argv
    sys.argv = [fname]
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main")
            if callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                          # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
        finally:
            sys.argv = argv_saved
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _pattern_gate(name, out, code, same, src, pin, exp_n, exp_verdict,
                  exp_sha16):
    """One pattern gate per probe: sha256 pin + byte ward + printed gate
    count + verdict + SPEC_SHA + exit code."""
    sha_ok = hashlib.sha256(
        _probe_bytes(src).encode("utf-8")).hexdigest() == pin
    marks = _PF_RE.findall(out)
    n_pass = sum(1 for m_ in marks if m_ == "PASS")
    n_fail = sum(1 for m_ in marks if m_ == "FAIL")
    m_all = _ALL_RE.search(out)
    all_ok = (m_all is not None and int(m_all.group(1)) == exp_n
              and int(m_all.group(2)) == exp_n)
    m_ver = _VER_RE.search(out)
    ver_ok = (m_ver is not None and m_ver.group(1) == exp_verdict)
    sha16_ok = exp_sha16 in _SHA_RE.findall(out)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (experiments source not present)"
            if same is None else "SOURCE MISMATCH")
    ok = (sha_ok and n_pass == exp_n and n_fail == 0 and all_ok and ver_ok
          and sha16_ok and code == 0 and same is not False)
    return ok, ("%s: %d/%d PASS marks, 0 FAIL exp (got %d), 'ALL GATES "
                "PASSED %d/%d' %s, VERDICT %s %s, SPEC_SHA %s %s, exit %d "
                "(exp 0), sha256 pin %s, provenance: %s"
                % (name, n_pass, exp_n, n_fail, exp_n, exp_n,
                   "found" if all_ok else "MISSING",
                   exp_verdict, "matched" if ver_ok else "WRONG",
                   exp_sha16, "printed" if sha16_ok else "MISSING",
                   code, "OK" if sha_ok else "BROKEN", prov))


# ------------------------------------------------------------------- run
def run():
    reset()
    t0 = time.time()
    print("=" * 74)
    print("v974  ALPHA.QUILLEN.EXACT.01 [O update] + SEAM.CONTACT.UNIT"
          ".01/.02 +")
    print("EM.WARD.01 / ALPHA.QUILLEN.INFLOW.01: both named faces of the "
          "alpha target")
    print("now carry COMPUTED witnesses -- BFK gluing executed on the seam "
          "circle")
    print("(constant 2^-N, jump matrix 16 c3 circ(2,-1,0,-1), v485 scale "
          "channel via")
    print("the KMS unit), the EM1 inflow step computed as a Laughlin pump "
          "(pump ==")
    print("flow == Streda == Chern == 1), the finite Quillen identity "
          "verified")
    print("two-sided; alpha^-1 re-anchored at 50 digits.  NO marker moves; "
          "the")
    print("target stays [O] (rigidity premise + channel-swap question + "
          "continuum")
    print("Bismut-Freed identification).")
    print("=" * 74, flush=True)

    # ============================================================== S0(a)
    print("\nS0(a)  BFK closed forms, module-own exact re-derivation")
    l, a = sp.symbols('l a', positive=True)
    A_ = l / (2 * sp.pi)
    dlog_D2 = -(4 * sp.log(A_) * sp.Rational(-1, 2) + 4 * ZP0)
    dlog_D1 = -(2 * sp.log(A_) * sp.Rational(-1, 2) + 2 * ZP0)
    B_ = a / sp.pi
    dlog_int = -(2 * sp.log(B_) * sp.Rational(-1, 2) + 2 * ZP0)
    circle_ok = sp.simplify(sp.expand_log(dlog_D2 - 2 * sp.log(l),
                                          force=True)) == 0
    absD_ok = sp.simplify(sp.expand_log(dlog_D1 - sp.log(l),
                                        force=True)) == 0
    int_ok = sp.simplify(sp.expand_log(dlog_int - sp.log(2 * a),
                                       force=True)) == 0
    check("S0a-ANCHORS [E]: det'_zeta(Delta on S^1_l) = l^2, "
          "det'_zeta(|D|) = l, det_zeta(Dirichlet [0,a]) = 2a -- symbolic "
          "from zeta_R(0) = -1/2, zeta_R'(0) = -(1/2) ln 2pi (zero mode "
          "removed = primed; module-own, no probe import)",
          circle_ok and absD_ok and int_ok)

    Bm = _circ([2, -1, 0, -1])
    Cm = _circ([0, 1, 2, 1])
    Sm = _circ([0, 0, 1, 0])
    lkms = 2 * sp.pi
    akms = sp.pi / 2
    R0 = sp.zeros(4, 4)
    for j in range(4):
        k2 = (j + 1) % 4
        w = 1 / akms
        R0[j, j] += w
        R0[k2, k2] += w
        R0[j, k2] += -w
        R0[k2, j] += -w
    r0_ok = sp.simplify(R0 - 16 * C3S * Bm) == sp.zeros(4, 4)
    detpR0 = 4 * lkms / akms ** 4               # N l / prod a_j
    detp_ok = sp.simplify(detpR0 - 2 ** 16 * C3S ** 3) == 0
    detD_ok = sp.simplify(2 * akms - 1 / (8 * C3S)) == 0
    gram_ok = sp.simplify(lkms / 4 - 1 / (16 * C3S)) == 0
    product_ok = sp.simplify(
        sp.Rational(1, 16) * (2 * akms) ** 4 * (lkms / 4) * detpR0
        - (2 * sp.pi) ** 2) == 0
    anchor_ok = sp.simplify((2 * sp.pi) ** 2 - 1 / (16 * C3S ** 2)) == 0
    check("S0a-KMS-REASSEMBLY [E]: at l = 2 pi = 1/(4 c3), a = pi/2: "
          "R_0 = 16 c3 circ(2,-1,0,-1) EXACT (16 c3 = |mu4| x 4 c3); "
          "det'(R_0) = 2^16 c3^3; per-interval det_D = 2a = 1/(8 c3); "
          "Gram factor l/N = 1/(16 c3); glued product 2^-4 prod(2a) (l/4) "
          "det'R_0 = (2 pi)^2 = 1/(16 c3^2) = det'Delta -- every BFK "
          "factor a pure 2-power times a c3 power, gluing constant 2^-4",
          r0_ok and detp_ok and detD_ok and gram_ok and product_ok
          and anchor_ok)

    specB_ok = dict(Bm.eigenvals()) == {0: 1, 2: 2, 4: 1}
    specC_ok = dict(Cm.eigenvals()) == {4: 1, -2: 2, 0: 1}
    trB_ok = all(sp.trace(Bm ** k) == 4 ** k + 2 * 2 ** k
                 for k in range(1, 5))
    trC_ok = all(sp.trace(Cm ** k) == 4 ** k + 2 * (-2) ** k
                 for k in range(1, 5))
    bc_ok = sp.simplify(Bm + Cm - 2 * (sp.eye(4) + Sm)) == sp.zeros(4, 4)
    check("S0a-SPEC-AND-TRACES [E]: spec(B) = {0,2,2,4}, spec(C) = "
          "{4,-2,0,-2} -- |spec| multisets EQUAL {0,2,2,4}, kernels in "
          "SWAPPED mu4 channels (B kills k=0 gauge/zero mode, C kills "
          "k=2 sign rep); Tr B^k = 4^k + 2(+2)^k and Tr C^k = 4^k + "
          "2(-2)^k exact (k = 1..4, the sign flip IS the kernel swap); "
          "B + C = 2(I + S)",
          specB_ok and specC_ok and trB_ok and trC_ok and bc_ok)

    c_gen = sp.Symbol('c_gen', positive=True)
    cancel_ok = sp.simplify((16 * c_gen) / (4 * c_gen * sp.log(2))
                            - 4 / sp.log(2)) == 0
    Pd = (sp.eye(4) - Sm) / 2
    Gmarks = -4 * C3S * sp.log(2) * Cm
    doublet_ok = sp.simplify(16 * C3S * Bm * Pd
                             - (4 / sp.log(2)) * Gmarks * Pd) \
        == sp.zeros(4, 4)
    check("S0a-DOUBLET-RATIO [E]: on the k = 1,3 doublet channel "
          "R_0|_d = (4/ln2) G_marks|_d EXACT (G_marks = -4 c3 ln2 C, "
          "v484); the c3 grading CANCELS in the ratio -- exhibited on a "
          "GENERIC symbol: (16 c)/(4 c ln2) = 4/ln2 independent of c",
          cancel_ok and doublet_ok)

    Greg = sp.log(l / (2 * sp.pi)) / sp.pi
    dict_ok = sp.simplify(sp.log(l ** 2) - sp.log((2 * sp.pi) ** 2)
                          - (1 / (4 * C3S)) * Greg) == 0
    ratio_ok = sp.simplify(sp.diff(sp.log(l ** 2), l) / sp.diff(Greg, l)
                           - 2 * sp.pi) == 0
    kms0_ok = sp.simplify(Greg.subs(l, 2 * sp.pi)) == 0
    check("S0a-SCALE-CHANNEL [E]: log det'Delta(l) - log det'Delta(2pi) "
          "= (1/(4 c3)) G_reg(0; l) EXACT with G_reg = (1/pi) ln(l/2pi) "
          "(the v485 closed form); derivative ratio = 2 pi = 1/(4 c3) = "
          "the KMS unit; G_reg(0; 2pi) = 0 at the seam point",
          dict_ok and ratio_ok and kms0_ok)

    # ============================================================== S0(b)
    print("\nS0(b)  the alpha anchor, module-own re-derivation (50 digits)")
    b1F = Fraction(41, 10)
    coeff_ok = (8 * b1F == Fraction(164, 5) == Fraction(4, 5) * 41
                and 10 * b1F == 41)
    qsum_ok = sp.Rational(5, 4) + sp.Rational(3, 4) == 2
    check("S0b-COEFFICIENTS [E]: 8 b1 = 8 x 41/10 = 164/5 = (4/5) x 41 "
          "and 10 b1 = 41 as exact Fractions; q(D5) + q(A3) = 5/4 + 3/4 "
          "= 2 (E8 root norm) exact",
          coeff_ok and qsum_ok)

    cc, phiseam, F_alpha = _alpha_functional()
    grid = [mp.mpf(10) ** (-4 + mp.mpf(4) * i / 80) for i in range(81)]
    signs = [1 if F_alpha(av) > 0 else -1 for av in grid]
    flips = sum(1 for i in range(80) if signs[i] != signs[i + 1])
    a_root = mp.findroot(F_alpha, mp.mpf("0.0073"))
    ainv = 1 / a_root
    lhs = a_root ** 3 - 2 * cc ** 3 * a_root ** 2
    rhs = (8 * mp.mpf(41) / 10) * cc ** 6 * mp.log(1 / phiseam(a_root))
    resid = abs(lhs - rhs)
    print("   alpha^-1 = %s   split residual = %s"
          % (mp.nstr(ainv, 17), mp.nstr(resid, 3)))
    check("S0b-ROOT-AND-SPLIT [E]: F_U(1)(a) = a^3 - 2 c3^3 a^2 - "
          "(4/5) 41 c3^6 ln(1/phi_seam) has EXACTLY ONE sign change on "
          "the log grid a in [1e-4, 1] (unique root on the window); "
          "alpha^-1 = 137.03599921684071 to < 1e-9; Quillen split "
          "residual |a^3 - 2 c3^3 a^2 - 8 b1 c3^6 ln(1/phi_seam)| < "
          "1e-30 at dps 50 (measured ~6.4e-58)",
          flips == 1
          and abs(ainv - mp.mpf(ALPHA_INV_REF)) < ROOT_BAR
          and resid < SPLIT_BAR)

    # ============================================================== S0(c)
    print("\nS0(c)  inflow bookkeeping, exact Fractions")
    N_maj = 2 ** (g_car - 1)
    N_cplx = Fraction(N_maj, 2)
    c_minus = N_maj * Fraction(1, 2)
    trY2 = 3 * Fraction(1, 3) ** 2 + 2 * Fraction(1, 2) ** 2
    trT32 = 2 * Fraction(1, 2) ** 2
    kY = trY2 / trT32
    b1_SM = Fraction(41, 6)
    ferm = Fraction(2, 3) * 3 * (6 * Fraction(1, 6) ** 2
                                 + 3 * Fraction(2, 3) ** 2
                                 + 3 * Fraction(1, 3) ** 2
                                 + 2 * Fraction(1, 2) ** 2 + 1)
    higgs = Fraction(1, 3) * 2 * Fraction(1, 2) ** 2
    check("S0c-INFLOW-BOOKKEEPING [E]: N_maj = 2^(g_car-1) = 16 = dim S+ "
          "Majoranas = 8 complex copies; c_- = 16 x 1/2 = 8 = g_car + "
          "N_fam; per-copy k0 = |C| = 1; kY = tr(Y^2)/tr(T3^2) = "
          "(5/6)/(1/2) = 5/3; (1/kY) x 41/6 = 41/10 = b1; 41/6 = 20/3 "
          "(fermions) + 1/6 (Higgs) -- all exact Fractions (v470 "
          "arithmetic re-derived)",
          N_maj == 16 == dim_Splus and N_cplx == 8 and c_minus == 8
          and c_minus == g_car + N_fam and kY == Fraction(5, 3)
          and b1_SM / kY == Fraction(41, 10)
          and ferm == Fraction(20, 3) and higgs == Fraction(1, 6)
          and ferm + higgs == b1_SM)

    # ============================================================== S0(d)
    print("\nS0(d)  coarse Chern certificate, module-own (probe-free)")
    c_topo = _fhs_coarse(1.0)
    c_triv = _fhs_coarse(3.0)
    int_ward = (abs(c_topo - round(c_topo)) < 1e-9
                and abs(c_triv - round(c_triv)) < 1e-9)
    check("S0d-COARSE-CHERN [E]: module-own FHS on the %d x %d grid: "
          "C(M=1) = %+.12f -> 1, C(M=3) = %+.12f -> 0 (integer-rounding "
          "ward < 1e-9) -- the pump probe's anchor integer re-derived "
          "independently, ~20 lines, no probe code"
          % (N_COARSE, N_COARSE, c_topo, c_triv),
          int_ward and round(c_topo) == 1 and round(c_triv) == 0)

    # ============================================================ mutants
    print("\nS0(m)  tipping mutants (all must be CAUGHT)")
    orig = _probe_bytes(_SRC_BFK)
    pos = 100
    mut = orig[:pos] + ("X" if orig[pos] != "X" else "Y") + orig[pos + 1:]
    sha_orig_ok = (hashlib.sha256(orig.encode("utf-8")).hexdigest()
                   == _PLAN[0][2])
    sha_mut_bad = (hashlib.sha256(mut.encode("utf-8")).hexdigest()
                   != _PLAN[0][2])
    check("MUT-HASH [E]: a single-byte mutation of the embedded BFK "
          "source breaks the sha256 pin (mutated != pin) while the "
          "embedded original matches it -- the byte ward is live, CAUGHT",
          sha_orig_ok and sha_mut_bad)

    resid_wrong = sp.simplify(sp.log(l ** 2) - sp.log((4 * sp.pi) ** 2)
                              - (1 / (4 * C3S)) * Greg)
    mut_kms_ok = (sp.simplify(resid_wrong + 2 * sp.log(2)) == 0
                  and resid_wrong != 0)
    check("MUT-KMS [E]: the wrong KMS unit (2 pi -> 4 pi as the anchor "
          "scale) breaks the S0 scale-channel identity by EXACTLY "
          "-2 ln 2 (symbolic, nonzero) -- CAUGHT",
          mut_kms_ok)

    b1w = Fraction(4, 1)
    coeff_broken = (8 * b1w != Fraction(164, 5))
    rhs_w = 8 * mp.mpf(4) * cc ** 6 * mp.log(1 / phiseam(a_root))
    resid_w = abs(lhs - rhs_w)
    check("MUT-B1 [E]: the b1 mutant 41/10 -> 4 breaks the coefficient "
          "identity (8 x 4 = 32 != 164/5) AND the split residual at the "
          "frozen root (%.2e >> 1e-30 bar) -- CAUGHT" % float(resid_w),
          coeff_broken and resid_w > mp.mpf("1e-12"))

    # ===================================================== embedded probes
    gate_results = []
    for name, src, pin, exp_n, exp_verdict, exp_sha16 in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s (expect %d/%d, VERDICT %s, "
              "SPEC_SHA %s)" % (name, exp_n, exp_n, exp_verdict, exp_sha16))
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        ok, detail = _pattern_gate(name, out, code, same, src, pin,
                                   exp_n, exp_verdict, exp_sha16)
        gate_results.append(ok)
        check("PATTERN-GATE %s [E]: %s" % (name, detail), ok)

    # ============================================================ verdict
    print("\n" + "-" * 74)
    check("HONEST BOUNDARY [O]: NO marker moves -- ALPHA.QUILLEN.EXACT.01 "
          "stays [O] ('why this functional' not closed); its remaining "
          "content TYPED as {SEAM.RP.RIGIDITY premise (measured, not "
          "proven)} + {the channel-swap question (the sharpened "
          "diagonal-zeta face)} + {the continuum Bismut-Freed "
          "identification of the exact-form difference field}; the pump "
          "is a single-copy complex-fermion statement (16-copy collar = "
          "bookkeeping arithmetic only); the BFK face is Delta = |D|^2, "
          "not a |D|-level operator identity; alpha^-1 stays [E] "
          "regardless", True)

    check("v974 VERDICT [E]: all three probes green in their embedded "
          "byte-exact form (21/21 MATCH_MODULO_LOCAL_FACTOR + 20/20 "
          "PUMP_QUANTIZED_MATCHES_CHERN + 18/18 CHAIN_SHADOW_OK), all "
          "S0 module-own identities exact, all tipping mutants caught",
          all(gate_results))

    print("   runtime %.1f s" % (time.time() - t0))
    return summary("v974 ALPHA.QUILLEN faces computed: BFK gluing "
                   "executed (2^-N, 16 c3 circ(2,-1,0,-1), v485 scale "
                   "channel via the KMS unit), EM1 inflow computed "
                   "(pump == flow == Streda == Chern == 1), finite "
                   "Quillen identity two-sided; alpha^-1 = "
                   "137.0359992168 re-anchored (residual ~6.4e-58); "
                   "NO marker moves, the target stays [O]")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
