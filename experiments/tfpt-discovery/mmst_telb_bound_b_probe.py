#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mmst_telb_bound_b_probe -- TELB.BOUND.B.01
r"""mmst_telb_bound_b_probe -- TELB.BOUND.B.01

FROZEN SPEC v2 (2026-09-04).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing; no verification module, ledger row, paper,
website surface, or scorecard row is touched.  The companion JSON is written
next to this probe.

PURPOSE.  Check every explicit constant in a short proof sketch for

    sup_{even N >= 16} ||S_N + H_N||_HS^2 <= 0.62.

CONVENTIONS (copied from mmst_telb_cover_split_probe.py).  The corpus uses
e^{-ipx}; alpha=1/4; k,l in {-N/2,...,N/2-1}; p_k=2*pi*k/N and
q_l=2*pi*(l+alpha)/N.  W=F_0^* F_alpha, hence

 W_kl=(1/N)(1-exp(-2*pi*i*alpha))
             /(1-exp(2*pi*i*(k-l-alpha)/N)).

saw(p)=1/2-(p mod 2*pi)/(2*pi), with saw(0)=0, and
S_N=diag(saw(p_k))-W diag(saw(q_l)) W^*.  H_N is the symmetric
digamma Hardy difference from the corpus.

EXACT SPLIT.  Put sigma_0(k)=sign(k)/2,
sigma_alpha(l)=sign(l+alpha)/2, K=diag(k), K_alpha=diag(l+alpha).
Then

 S_N = T_N + L_N,
 T_N = diag(sigma_0)-W diag(sigma_alpha) W^*,
 L_N = -(1/N)[K-W K_alpha W^*].

Let w_k=exp(-i*pi*alpha) sin(pi*alpha)/(pi(k-alpha)), e=e_0, and
 A_N=(1/2)|e><e|-|w_N><w_N|.
The explicit finite remainder is

 Res_N = L_N + [T_N+H_N-A_N] = S_N+H_N-A_N.

Thus E_N=0 exactly; the bracket is precisely the circle-versus-Toeplitz
step mismatch.  The position-space closed form used for fast evaluation is

 s_N(x,y)=[-(1+t^2)+3*i*t-i*t^3]/[4*N*(1-t^2)],
 t=tan(pi*(x-y)/(4*N)).

PROVED IDENTITIES USED BY THE SKETCH.
P1: saw splits exactly into sigma-ramp on both grids.
P2: entrywise, S_N+H_N -> A_infinity.  This follows from
    saw(p_k)->sign(k)/2, the infinite overlap
    (W_inf)_{km}=exp(-i*pi*alpha)sin(pi*alpha)/(pi(k-m-alpha)),
    and unitarity applied to the step projection.
P3: ||A_infinity||_HS^2
      = 5/4-|<e_0,w>|^2 = 5/4-8/pi^2.
P4: E_N=0 by the exact split above.

EXPLICIT ENTRY FORMULA.  The step identities give exactly

 T_N+H_N-A_N
 = W_N P_{[-N/2,-1]} W_N^*
   - P_N W_inf P_{(-infinity,-1]} W_inf^* P_N.

Consequently the branchwise difference, before absolute values, is

 Res_N(k,l) = -k*delta_kl/N
   + sum_{m in I_N} [(m+alpha)/N + 1_{m<=-1}]
       W_N(k,m) conjugate(W_N(l,m))
   - sum_{m<=-1} W_inf(k,m) conjugate(W_inf(l,m)).

The finite products equal
 exp(-i*pi*(k-l)/N) sin(alpha*pi)^2 /
 [N^2 sin(pi*(k-m-alpha)/N) sin(pi*(l-m-alpha)/N)].
For k != l the infinite sum is
 (sin(alpha*pi)^2/pi^2)
 [psi(1+l-alpha)-psi(1+k-alpha)]/(l-k).

Equivalently, with c=1-exp(-2*pi*i*alpha), a_m=saw(q_m),

 S_kl = delta_kl saw(p_k)
        - |c|^2/N^2 sum_m a_m /
          [(1-exp(2*pi*i*(k-m-alpha)/N))
           (1-exp(-2*pi*i*(l-m-alpha)/N))].

Adding the displayed digamma divided difference in hardy_difference and
subtracting A_N gives every Res_N(k,l) explicitly.

ANALYTIC ATTEMPT AND OBSTRUCTION.  The separate estimates
||S_N||_HS <= sqrt(N), ||H_N||_HS <= 2*sqrt(N), and
||A_N||_HS <= sqrt(C_A) prove only

 ||Res_N||_HS <= 3*sqrt(N)+sqrt(C_A).

Cauchy-Schwarz then gives
 N*|2 Re<A_N,Res_N>|
 <= 2*N*sqrt(C_A)*(3*sqrt(N)+sqrt(C_A)).
These are rigorous but non-uniform.  The degree -1 terms of the Cauchy
step sum and the digamma divided difference cancel only after subtraction.
Majorizing either term first leaves a non-L2 1/r singularity (logarithmic
divergence of its squared two-dimensional majorant).  A uniform proof
therefore requires a branchwise closed formula for their DIFFERENCE and a
bounded-variation/Euler--Maclaurin estimate.  That formula is not supplied.

NUMERICALLY CHECKED LEMMAS (NOT INTERVAL-CERTIFIED).
N1: ||Res_N||_HS^2 <= C_RES=0.155000 for every even N>=16.
N2: |2 Re <A_N,Res_N>| <= C_CROSS/N, C_CROSS=0.382000.
The probe checks EVERY even N from 16 through 512, then
N={1024,2048,4096}; it does not turn N1/N2 into all-N proofs.
With ||A_N||^2<=||A_inf||^2,

 ||S_N+H_N||^2 <= C_A+C_RES+C_CROSS/16
                  = 0.618305... < 0.62.

DIAGNOSTICS.  The physical-momentum character is checked through the
N-independent central-square HS-squared contributions
 ||Res[|k|,|l|<N/8]||^2 <= 0.013 and
 ||Res[|k|,|l|<N/4]||^2 <= 0.043.

GATES.
G01 closed S formula and exact ramp+step split (N<=256), residual <1e-10.
G02 corpus values at N=64,256,1024,4096 reproduced within 5e-6.
G03 A bound and exact constant C_A=5/4-8/pi^2.
G04 measured ||Res_N||^2 <= C_RES on the dense finite scan.
G05 measured N*|cross_N| <= C_CROSS on the dense finite scan.
G06 central-square HS-squared diagnostics <= their named constants.
G07 assembled constant <=0.62 and every computed norm <=0.62.
G08 corrected relaxed TEL-B threshold and measured margin.
G09 analytic-status declaration matches the available proof.
G10 verdict enum frozen.

VERDICTS.
BOUND_B_CLOSED_WITH_CONSTANTS: analytic all-N proofs of N1/N2 supplied.
BOUND_B_UNIFORM_ANALYTIC: a uniform analytic constant closes the relaxed
TEL-B triangle target, even if the sharper 0.62 target is not closed.
BOUND_B_SKETCH_INCOMPLETE: constants pass numerically and assemble, but at
least one all-N lemma remains numerical.
BOUND_B_FAILS: a claimed numerical constant or the assembly fails.

HONEST NOTE.  Float64, no interval arithmetic.  P1--P4 and the
N-dependent bounds above are analytic; N1--N2 are finite numerical checks,
not proofs over all even N.  Therefore this v2 probe cannot return
BOUND_B_CLOSED_WITH_CONSTANTS.
SEAM.MMST.TYPEIII.CHARGED.01 stays [O].

FROZEN SPEC v3 ADDENDUM (2026-09-04, second adjudication).

The v2 route R2 compares Res_N with the cell-average matrix K_N of the
scaling kernel r of equation (21).  Three facts about r were stated
incorrectly in the note and are corrected here; all three are gated.

K1 KERNEL STRUCTURE.  Write f(u)=-log|u|-pi*cot(pi*alpha)*1_{u<0} for the
   scaled digamma potential and Phi_star for the potential of (20).  Then

     F(u) := f(u)+Phi_star(u)  is 1-PERIODIC,

   because Phi_star carries the single jump -pi*cot(pi*alpha) that
   compensates the jump of f.  Exact edge and centre values:

     Phi_star(1/2^-)  = -2*log2 - pi/2  = -2.957090...
     Phi_star(-1/2^+) = -2*log2 + pi/2  = +0.184500...
     Phi_star(0)      = -log(2*pi)      = -1.837877...

   Consequently Phi_star is BOUNDED, and so are its derivatives:

     Phi_star'(u)  = 1/u - 2*pi/sin(2*pi*u) + pi*tan(pi*u) - pi*cot(pi*alpha),
     Phi_star''(u) = -1/u^2 + 4*pi^2*cos(2*pi*u)/sin(2*pi*u)^2
                     + pi^2/cos(pi*u)^2,

   with sup|Phi_star'| = 2+pi and pi^2/3 <= Phi_star'' <= pi^2-4.  The
   u^{-2} and (1/2-|u|)^{-2} terms CANCEL identically.  The note's claim
   that Phi_star'' has non-integrable singular parts, which is what its
   Euler--Maclaurin attempt foundered on, is therefore false.

   The only singularities of r on [-1/2,1/2]^2 are the two LOGARITHMIC
   lines u=0 and v=0, inherited from f.  There is no singular line at
   u=+-1/2 or v=+-1/2; the apparent corner blow-up of lambda(u-v) as
   |u-v| -> 1 is cancelled by the periodicity of F, and
   r(-1/2+a, 1/2-a) -> 1/pi as a -> 0.

K2 ONE-VARIABLE REDUCTION.  With u=k/N, v=l/N and A=sin^2(pi*alpha)/pi^2,

     eta(k)   := F_infinity(k) + log N + gamma - f(k/N)
               = -psi(k+1-alpha) + log|k| + pi*cot(pi*alpha)*1_{k<0},
     phi_N(k) := F_N(k) - F_infinity(k) - log N - gamma - Phi_star(k/N),

   and eta is N-INDEPENDENT.  Then, exactly, for k != l and k,l != 0,

     N*Res_N(k,l) = r(u,v)
                    + A*[ (1-lambda(u-v))*(eta(l)-eta(k))
                          - lambda(u-v)*(phi_N(l)-phi_N(k)) ] / (v-u).

   So the whole discrete-to-continuum discrepancy is carried by two
   ONE-DIMENSIONAL sequences.  Measured: max|eta| = 0.247472 at k=1 and
   sum eta^2 = 0.1915 (both N-free), and N*max_{k!=0}|phi_N(k)| increases
   monotonically to 1/2.  The resulting point-sample discrepancy
   Delta_N := Res_N^{reg} - N^{-1} r(k/N,l/N) obeys
   sqrt(N)*||Delta_N||_HS = 0.0923 ... 0.1039.

K3 CORRECTED RATE.  The v2 adjudication asserted a reference sequence
   sqrt(N)*||E_N|| = 0.2645 ... 0.2711 and blamed the probe's smaller
   values on under-resolved logarithmic strips.  That reference is wrong.
   An independent geometrically graded cell quadrature (levels of dyadic
   refinement toward each singular endpoint, Gauss-8 per level), run at
   two refinement depths, reproduces the probe's composite-Gauss values to
   ~1e-6.  The correct sequence is

     sqrt(N)*||E_N|| = 0.19425, 0.19781, 0.19961, 0.20051, 0.20096, 0.20119
     (N = 16,32,64,128,256,512),  limit ~ 0.2016.

   The constant required by the relaxed TEL-B target is
   c_E <= 4*(sqrt(RELAXED_RES2_THRESHOLD) - sqrt(C_STAR_LIMIT)) = 0.5435,
   NOT 0.30.  The measured constant therefore clears the requirement by a
   factor ~2.7.  This is a measurement, not a proof: the all-N inequality
   ||Res_N - K_N||_HS <= c_E * N^{-1/2} is still not established, so the
   verdict is unchanged.

ADDITIONAL GATES.
G15 corrected kernel structure (periodicity, edge values, derivative
    bounds, corner limit 1/pi).
G16 one-variable reduction identity and its two 1-D constants.
G17 corrected c_E requirement and the measured margin.

FROZEN SPEC v4 ADDENDUM (2026-09-04, elementary-lemma attempt).

G18 checks c_1=0.51 against N*sup|phi_N| at N=16,64,256,1024 and
    separately records whether the requested all-N analytic proof exists.
G19 records whether an explicit analytic cell-oscillation constant c_2
    has been obtained after subtracting the variable-coefficient logarithmic
    terms of r and treating the k=0 or l=0 rows not covered by (33).
G20 records whether those proved constants assemble to an analytic
    c_E <= 0.542702 while dominating the measured 0.201296.

The numerical part of G18 passes, but the analytic part does not.  Recentring
the full-period sum gives, for 0<=k<N,

 F_N(k)=C_N-pi*k*cot(pi*alpha)/N
        +(pi/N)*sum_{t=1}^k cot(pi*(alpha-t)/N),
 C_N=-(pi/N^2)*sum_{j=0}^{N-1}(j+alpha)cot(pi*(j+alpha)/N).

This is a useful one-variable Euler--Maclaurin starting point, but the
requested uniform 0.51 remainder and the assertion that its maximum is at
the seam were not proved in the time-box.

For G19, the per-cell mean-value inequality is valid on a smooth cell.
It is not yet a global c_2 estimate: the logarithmic coefficient in r
depends on the other coordinate, grad(r) is not square-integrable before
that term is explicitly subtracted, and reduction (33) excludes the zero
row and column.  K_N integrating the logarithm exactly does not by itself
identify those missing discrete entries.  Therefore G18--G20 fail
honestly and the verdict remains BOUND_B_SKETCH_INCOMPLETE.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from math import pi
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np
from scipy.special import digamma, polygamma, spence
from numpy.polynomial.legendre import leggauss

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

ALPHA = 0.25
SIZES = (16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
EVEN_SCAN_MAX = 512
CHECKED_SIZES = tuple(
    sorted(set(range(16, EVEN_SCAN_MAX + 1, 2)).union(SIZES))
)
DIRECT_SPLIT_SIZES = (16, 32, 64, 128, 256)
CORPUS_PINS = {
    64: 0.580006,
    256: 0.588607,
    1024: 0.590758,
    4096: 0.591296,
}

C_A = 5.0 / 4.0 - 8.0 / pi**2
C_RES = 0.155000
C_CROSS = 0.382000
C_FRAC_EIGHTH = 0.013000
C_FRAC_QUARTER = 0.043000
TARGET = 0.620000
RSM_NORM_BOUND = 1.7833
M_NORM_ALLOWANCE = 3.0 - RSM_NORM_BOUND
RELAXED_TOTAL2_TARGET = M_NORM_ALLOWANCE**2 / 2.0
RELAXED_RES2_THRESHOLD = (
    RELAXED_TOTAL2_TARGET - C_A - C_CROSS / min(SIZES)
)
PIN_TOL = 5.0e-6
IDENTITY_TOL = 1.0e-10
ANALYTIC_UNIFORM_RES_PROVED = False
ANALYTIC_UNIFORM_CROSS_PROVED = False
RELAXED_UNIFORM_ANALYTIC_PROVED = False
C_STAR_LIMIT = 0.1525
C_E_NUMERIC = 0.30
C_E_REQUIRED = 4.0 * (RELAXED_RES2_THRESHOLD**0.5 - C_STAR_LIMIT**0.5)
PHI_STAR_PRIME_SUP = 2.0 + pi
PHI_STAR_SECOND_SUP = pi**2 - 4.0
PHI_STAR_SECOND_INF = pi**2 / 3.0
ETA_SUP_CLAIM = 0.2475
PHI_N_SCALED_SUP = 0.51
DELTA_SCALED_SUP = 0.11
QUADRATURE_AGREEMENT_TOL = 5.0e-4
GRADED_SELF_CONVERGENCE_TOL = 1.0e-5
C2A_ANALYTIC_PROVED = False
C2B_ANALYTIC_PROVED = False
C_1_ANALYTIC = 0.51
C_2_ANALYTIC = None
C_E_ANALYTIC = None

VERDICT_ENUM = (
    "BOUND_B_CLOSED_WITH_CONSTANTS",
    "BOUND_B_UNIFORM_ANALYTIC",
    "BOUND_B_SKETCH_INCOMPLETE",
    "BOUND_B_FAILS",
)

CHECKS: list[tuple[str, bool, str]] = []


def gate(name: str, ok: bool, detail: str) -> None:
    """Record and print one frozen gate."""
    CHECKS.append((name, bool(ok), detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail))


def mode_indices(size: int) -> np.ndarray:
    return np.arange(-size // 2, size // 2, dtype=float)


def overlap_closed(size: int) -> np.ndarray:
    """Closed corpus-convention overlap W=F_0^*F_alpha."""
    indices = mode_indices(size)
    delta = indices[:, None] - indices[None, :] - ALPHA
    numerator = 1.0 - np.exp(-2j * pi * ALPHA)
    denominator = 1.0 - np.exp(2j * pi * delta / size)
    return numerator / (size * denominator)


def hardy_difference(size: int) -> np.ndarray:
    """Vectorized copy of the corpus digamma Hardy section."""
    indices = mode_indices(size)
    shifted = indices - ALPHA
    row = shifted[:, None]
    column = shifted[None, :]
    denominator = column - row
    numerator = digamma(column) - digamma(row)
    with np.errstate(divide="ignore", invalid="ignore"):
        overlap_sum = numerator / denominator
    np.fill_diagonal(overlap_sum, polygamma(1, shifted))
    factor = np.sin(pi * ALPHA) ** 2 / pi**2
    occupied_twisted = factor * overlap_sum
    occupied_untwisted = np.diag((indices <= 0).astype(float))
    difference = occupied_untwisted - occupied_twisted
    return 0.5 * (difference + difference.T)


def saw_position_closed(size: int) -> np.ndarray:
    """Exact position-space sawtooth response in the corpus convention."""
    positions = np.arange(size)
    difference = positions[:, None] - positions[None, :]
    tangent = np.tan(pi * difference / (4.0 * size))
    return (
        -(1.0 + tangent**2) + 3j * tangent - 1j * tangent**3
    ) / (4.0 * size * (1.0 - tangent**2))


def position_to_mode(matrix: np.ndarray) -> np.ndarray:
    """Compute F_0^* matrix F_0 by two unitary FFT legs."""
    transformed = np.fft.ifft(np.fft.fft(matrix, axis=1), axis=0)
    return np.fft.fftshift(transformed, axes=(0, 1))


def saw_response_fast(size: int) -> np.ndarray:
    return position_to_mode(saw_position_closed(size))


def saw_values(momentum: np.ndarray) -> np.ndarray:
    reduced = np.mod(momentum, 2.0 * pi)
    values = 0.5 - reduced / (2.0 * pi)
    return np.where(np.isclose(reduced, 0.0, atol=1.0e-13), 0.0, values)


def saw_response_direct(size: int) -> np.ndarray:
    """Definition-level S_N, used only by the identity gate."""
    indices = mode_indices(size)
    w_matrix = overlap_closed(size)
    p_zero = 2.0 * pi * indices / size
    p_alpha = 2.0 * pi * (indices + ALPHA) / size
    return (
        np.diag(saw_values(p_zero))
        - (w_matrix * saw_values(p_alpha)[None, :]) @ w_matrix.conj().T
    )


def step_and_ramp(size: int) -> tuple[np.ndarray, np.ndarray]:
    """Return the explicit step response T_N and ramp response L_N."""
    indices = mode_indices(size)
    w_matrix = overlap_closed(size)
    sigma_zero = 0.5 * np.sign(indices)
    sigma_alpha = 0.5 * np.sign(indices + ALPHA)
    step = (
        np.diag(sigma_zero)
        - (w_matrix * sigma_alpha[None, :]) @ w_matrix.conj().T
    )
    ramp = -(1.0 / size) * (
        np.diag(indices)
        - (w_matrix * (indices + ALPHA)[None, :]) @ w_matrix.conj().T
    )
    return step, ramp


def limit_section(size: int) -> np.ndarray:
    """Finite section A_N of the rank-two operator A_infinity."""
    indices = mode_indices(size)
    e_zero = (indices == 0).astype(complex)
    w_zero = (
        np.exp(-1j * pi * ALPHA)
        * np.sin(pi * ALPHA)
        / (pi * (indices - ALPHA))
    )
    return 0.5 * np.outer(e_zero, e_zero.conj()) - np.outer(
        w_zero, w_zero.conj()
    )


def branchwise_remainder(size: int) -> np.ndarray:
    """Evaluate the one-line finite-Cauchy minus infinite-digamma formula."""
    indices = mode_indices(size)
    w_matrix = overlap_closed(size)
    weights = (indices + ALPHA) / size + (indices <= -1).astype(float)
    finite_branch = (w_matrix * weights[None, :]) @ w_matrix.conj().T

    shifted = 1.0 + indices - ALPHA
    row = shifted[:, None]
    column = shifted[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        infinite_branch = (digamma(column) - digamma(row)) / (column - row)
    np.fill_diagonal(infinite_branch, polygamma(1, shifted))
    infinite_branch *= np.sin(pi * ALPHA) ** 2 / pi**2
    return -np.diag(indices) / size + finite_branch - infinite_branch


def potential_samples(size: int) -> tuple[np.ndarray, np.ndarray]:
    """Return the sampled potentials F_N(k) and F_infinity(k) on I_N."""
    indices = mode_indices(size)
    weights = np.mod((indices + ALPHA) / size, 1.0)
    arguments = pi * (indices[:, None] - indices[None, :] - ALPHA) / size
    finite_values = (pi / size) * np.sum(
        weights[None, :] / np.tan(arguments), axis=1
    )
    infinite_values = -digamma(indices + 1.0 - ALPHA) - np.euler_gamma
    return finite_values, infinite_values


def master_identity_remainder(size: int) -> np.ndarray:
    """Judge R2 identity: divided differences of F_infinity and F_N."""
    indices = mode_indices(size)
    weights = np.mod((indices + ALPHA) / size, 1.0)
    arguments = (
        pi * (indices[:, None] - indices[None, :] - ALPHA) / size
    )
    finite_values = (pi / size) * np.sum(
        weights[None, :] / np.tan(arguments), axis=1
    )
    finite_derivatives = -(pi**2 / size**2) * np.sum(
        weights[None, :] / np.sin(arguments) ** 2, axis=1
    )
    infinite_values = -digamma(indices + 1.0 - ALPHA) - np.euler_gamma
    infinite_derivatives = -polygamma(1, indices + 1.0 - ALPHA)
    denominator = indices[None, :] - indices[:, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        finite_dd = (
            finite_values[None, :] - finite_values[:, None]
        ) / denominator
        infinite_dd = (
            infinite_values[None, :] - infinite_values[:, None]
        ) / denominator
    np.fill_diagonal(finite_dd, finite_derivatives)
    np.fill_diagonal(infinite_dd, infinite_derivatives)
    delta = indices[:, None] - indices[None, :]
    angle = pi * delta / size
    lambda_matrix = np.ones((size, size), dtype=complex)
    off_diagonal = delta != 0
    lambda_matrix[off_diagonal] = (
        angle[off_diagonal]
        / np.sin(angle[off_diagonal])
        * np.exp(-1j * angle[off_diagonal])
    )
    return (
        np.sin(pi * ALPHA) ** 2
        / pi**2
        * (infinite_dd - lambda_matrix * finite_dd)
        - np.diag(indices) / size
    )


def clausen2(angle: np.ndarray) -> np.ndarray:
    """Cl_2(theta)=Im Li_2(exp(i theta)), vectorized through Spence."""
    return np.imag(spence(1.0 - np.exp(1j * angle)))


def sigma_cot_primitive(value: np.ndarray) -> np.ndarray:
    """Primitive of sigma*cot(pi*sigma), continuously extended at integers."""
    sine = np.abs(2.0 * np.sin(pi * value))
    logarithmic = np.zeros_like(value, dtype=float)
    regular = sine > 1.0e-14
    logarithmic[regular] = (
        value[regular] / pi * np.log(sine[regular])
    )
    return logarithmic + clausen2(2.0 * pi * value) / (2.0 * pi**2)


def phi_star(value: np.ndarray) -> np.ndarray:
    """The explicit scaling potential Phi_star from judge equation (20).

    The two coordinate singularities of the closed form at u=0 and
    u=+-1/2 are removable; the exact limits are -log(2*pi) and
    -2*log2 -+ pi/2.  Inserting them keeps Phi_star finite and bounded on
    the closed square, which is what the corrected structure lemma needs.
    """
    value = np.asarray(value, dtype=float)
    result = np.empty_like(value)
    at_zero = np.abs(value) < 1.0e-13
    at_upper = np.abs(value - 0.5) < 1.0e-13
    at_lower = np.abs(value + 0.5) < 1.0e-13
    regular = ~(at_zero | at_upper | at_lower)
    result[at_zero] = -np.log(2.0 * pi)
    result[at_upper] = -2.0 * np.log(2.0) - pi / 2.0
    result[at_lower] = -2.0 * np.log(2.0) + pi / 2.0
    inner = value[regular]
    ratio_term = np.log(np.abs(inner / np.tan(pi * inner)))
    integral = sigma_cot_primitive(inner + 0.5) - sigma_cot_primitive(
        inner - 0.5
    )
    result[regular] = (
        ratio_term - pi * integral - pi * inner / np.tan(pi * ALPHA)
    )
    return result


def phi_star_prime(value: np.ndarray) -> np.ndarray:
    """First derivative of Phi_star; bounded, with sup modulus 2+pi."""
    value = np.asarray(value, dtype=float)
    return (
        1.0 / value
        - 2.0 * pi / np.sin(2.0 * pi * value)
        + pi * np.tan(pi * value)
        - pi / np.tan(pi * ALPHA)
    )


def phi_star_second(value: np.ndarray) -> np.ndarray:
    """Second derivative of Phi_star.

    The u^{-2} and (1/2-|u|)^{-2} parts cancel identically, so this stays
    inside [pi^2/3, pi^2-4].
    """
    value = np.asarray(value, dtype=float)
    return (
        -1.0 / value**2
        + 4.0 * pi**2 * np.cos(2.0 * pi * value) / np.sin(2.0 * pi * value) ** 2
        + pi**2 / np.cos(pi * value) ** 2
    )


def scaled_infinite_potential(value: np.ndarray) -> np.ndarray:
    value = np.asarray(value, dtype=float)
    return (
        -np.log(np.abs(value))
        - pi / np.tan(pi * ALPHA) * (value < 0)
    )


def scaling_kernel(u_value: np.ndarray, v_value: np.ndarray) -> np.ndarray:
    """Kernel r(u,v), evaluated away from its measure-zero singular lines."""
    theta = u_value - v_value
    lambda_value = (
        pi * theta * np.exp(-1j * pi * theta) / np.sin(pi * theta)
    )
    numerator = (
        (1.0 - lambda_value)
        * (
            scaled_infinite_potential(v_value)
            - scaled_infinite_potential(u_value)
        )
        - lambda_value * (phi_star(v_value) - phi_star(u_value))
    )
    return (
        np.sin(pi * ALPHA) ** 2
        / pi**2
        * numerator
        / (v_value - u_value)
    )


def periodic_potential(value: np.ndarray) -> np.ndarray:
    """F = f + Phi_star, the 1-periodic combination of the two potentials."""
    return scaled_infinite_potential(value) + phi_star(value)


def kernel_from_potentials(
    u_values: np.ndarray,
    v_values: np.ndarray,
    f_u: np.ndarray,
    f_v: np.ndarray,
    p_u: np.ndarray,
    p_v: np.ndarray,
) -> np.ndarray:
    """Kernel r built from precomputed one-dimensional potential values."""
    theta = u_values[:, None] - v_values[None, :]
    lambda_value = (
        pi * theta * np.exp(-1j * pi * theta) / np.sin(pi * theta)
    )
    numerator = (1.0 - lambda_value) * (
        f_v[None, :] - f_u[:, None]
    ) - lambda_value * (p_v[None, :] - p_u[:, None])
    return (
        np.sin(pi * ALPHA) ** 2
        / pi**2
        * numerator
        / (v_values[None, :] - u_values[:, None])
    )


def graded_cell_rules(
    size: int, regular_order: int, singular_order: int, levels: int, strip: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Per-cell 1-D rules, dyadically graded toward each singular endpoint.

    Cells whose closer endpoint is within strip/size of one of the three
    singular abscissae 0, -1/2, +1/2 are refined by `levels` dyadic
    bisections toward that endpoint; every level carries a Gauss rule.
    """
    singular_points = (0.0, -0.5, 0.5)
    regular_nodes, regular_weights = leggauss(regular_order)
    singular_nodes, singular_weights = leggauss(singular_order)
    collected: list[tuple[np.ndarray, np.ndarray]] = []
    is_strip = np.zeros(size, dtype=bool)
    for position, cell in enumerate(range(-size // 2, size // 2)):
        left = cell / size
        right = (cell + 1) / size
        distance_left = min(abs(left - s) for s in singular_points)
        distance_right = min(abs(right - s) for s in singular_points)
        if min(distance_left, distance_right) >= strip / size:
            collected.append(
                (
                    0.5 * (left + right)
                    + 0.5 * (right - left) * regular_nodes,
                    0.5 * (right - left) * regular_weights,
                )
            )
            continue
        is_strip[position] = True
        toward_left = distance_left <= distance_right
        nodes: list[np.ndarray] = []
        weights: list[np.ndarray] = []
        low, high = left, right
        for _ in range(levels):
            middle = 0.5 * (low + high)
            segment = (middle, high) if toward_left else (low, middle)
            if toward_left:
                high = middle
            else:
                low = middle
            nodes.append(
                0.5 * (segment[0] + segment[1])
                + 0.5 * (segment[1] - segment[0]) * singular_nodes
            )
            weights.append(
                0.5 * (segment[1] - segment[0]) * singular_weights
            )
        nodes.append(
            0.5 * (low + high) + 0.5 * (high - low) * singular_nodes
        )
        weights.append(0.5 * (high - low) * singular_weights)
        collected.append(
            (np.concatenate(nodes), np.concatenate(weights))
        )
    width = max(len(item[0]) for item in collected)
    node_array = np.zeros((size, width))
    weight_array = np.zeros((size, width))
    for position, (nodes_1d, weights_1d) in enumerate(collected):
        node_array[position, : len(nodes_1d)] = nodes_1d
        node_array[position, len(nodes_1d):] = nodes_1d[-1]
        weight_array[position, : len(weights_1d)] = weights_1d
    return node_array, weight_array, is_strip


def graded_cell_average_kernel(
    size: int,
    regular_order: int = 8,
    singular_order: int = 8,
    levels: int = 10,
    strip: int = 4,
) -> np.ndarray:
    """Independent evaluation of K_N by graded per-cell quadrature.

    The row and column rules use different Gauss orders so that no
    quadrature node pair ever lands on the regular diagonal u=v.
    Evaluation is blocked into regular/strip row and column groups so the
    graded rules are only paid for where they are needed.
    """
    u_nodes, u_weights, u_strip = graded_cell_rules(
        size, regular_order, singular_order, levels, strip
    )
    v_nodes, v_weights, v_strip = graded_cell_rules(
        size, regular_order + 1, singular_order + 1, levels, strip
    )
    u_f = scaled_infinite_potential(u_nodes.ravel()).reshape(u_nodes.shape)
    u_p = phi_star(u_nodes.ravel()).reshape(u_nodes.shape)
    v_f = scaled_infinite_potential(v_nodes.ravel()).reshape(v_nodes.shape)
    v_p = phi_star(v_nodes.ravel()).reshape(v_nodes.shape)
    accumulator = np.zeros((size, size), dtype=complex)
    for row_mask in (~u_strip, u_strip):
        rows = np.flatnonzero(row_mask)
        if rows.size == 0:
            continue
        row_width = int(
            np.max(np.count_nonzero(u_weights[rows], axis=1))
        )
        for column_mask in (~v_strip, v_strip):
            columns = np.flatnonzero(column_mask)
            if columns.size == 0:
                continue
            column_width = int(
                np.max(np.count_nonzero(v_weights[columns], axis=1))
            )
            block = np.zeros((rows.size, columns.size), dtype=complex)
            for p_index in range(row_width):
                row_weight = u_weights[rows, p_index]
                if not np.any(row_weight):
                    continue
                for q_index in range(column_width):
                    column_weight = v_weights[columns, q_index]
                    if not np.any(column_weight):
                        continue
                    block += (
                        row_weight[:, None] * column_weight[None, :]
                    ) * kernel_from_potentials(
                        u_nodes[rows, p_index],
                        v_nodes[columns, q_index],
                        u_f[rows, p_index],
                        v_f[columns, q_index],
                        u_p[rows, p_index],
                        v_p[columns, q_index],
                    )
            accumulator[np.ix_(rows, columns)] = block
    return size * accumulator


def one_variable_reduction(size: int) -> dict[str, float]:
    """Check N*Res_N = r(u,v) + A*[(1-lambda)*d(eta) - lambda*d(phi)]/(v-u).

    Also returns the two one-dimensional constants of the reduction and
    the point-sample discrepancy Delta_N on the regular index block.
    """
    indices = mode_indices(size)
    scaled = indices / size
    finite_values, infinite_values = potential_samples(size)
    eta = infinite_values + np.log(size) + np.euler_gamma
    nonzero = indices != 0
    eta[nonzero] -= scaled_infinite_potential(scaled[nonzero])
    eta[~nonzero] = 0.0
    phi = (
        finite_values
        - infinite_values
        - np.log(size)
        - np.euler_gamma
        - phi_star(scaled)
    )

    remainder = master_identity_remainder(size)
    potential_f = np.where(
        nonzero, scaled_infinite_potential(np.where(nonzero, scaled, 1.0)), 0.0
    )
    potential_p = phi_star(scaled)
    with np.errstate(divide="ignore", invalid="ignore"):
        model = kernel_from_potentials(
            scaled, scaled, potential_f, potential_f, potential_p, potential_p
        )
    delta = indices[:, None] - indices[None, :]
    angle = pi * delta / size
    lambda_matrix = np.ones((size, size), dtype=complex)
    off_diagonal = delta != 0
    lambda_matrix[off_diagonal] = (
        angle[off_diagonal]
        / np.sin(angle[off_diagonal])
        * np.exp(-1j * angle[off_diagonal])
    )
    with np.errstate(divide="ignore", invalid="ignore"):
        correction = (
            np.sin(pi * ALPHA) ** 2
            / pi**2
            * (
                (1.0 - lambda_matrix) * (eta[None, :] - eta[:, None])
                - lambda_matrix * (phi[None, :] - phi[:, None])
            )
            / (scaled[None, :] - scaled[:, None])
        )
    regular = np.outer(nonzero, nonzero) & off_diagonal
    residual = float(
        np.max(
            np.abs(
                size * remainder[regular]
                - model[regular]
                - correction[regular]
            )
        )
    )
    discrepancy = float(
        np.linalg.norm(size * remainder[regular] - model[regular]) / size
    )
    return {
        "N": size,
        "identity_residual": residual,
        "eta_sup": float(np.max(np.abs(eta[nonzero]))),
        "eta_norm2": float(np.sum(eta[nonzero] ** 2)),
        "scaled_phi_sup": float(size * np.max(np.abs(phi[nonzero]))),
        "scaled_delta_norm": float(np.sqrt(size) * discrepancy),
    }


def singular_quadrature_extrapolation(
    offsets: tuple[float, float],
) -> tuple[float, list[float]]:
    """Extrapolate C_star using the known (log M)/M singular correction."""
    mesh_sizes = np.array((256, 512, 1024, 2048), dtype=float)
    values = []
    for mesh_size_float in mesh_sizes:
        mesh_size = int(mesh_size_float)
        u_values = -0.5 + (
            np.arange(mesh_size) + offsets[0]
        ) / mesh_size
        v_values = -0.5 + (
            np.arange(mesh_size) + offsets[1]
        ) / mesh_size
        kernel = scaling_kernel(u_values[:, None], v_values[None, :])
        values.append(float(np.mean(np.abs(kernel) ** 2)))
    design = np.column_stack(
        [
            np.ones_like(mesh_sizes),
            np.log(mesh_sizes) / mesh_sizes,
            1.0 / mesh_sizes,
        ]
    )
    coefficients, _, _, _ = np.linalg.lstsq(
        design, np.asarray(values), rcond=None
    )
    return float(coefficients[0]), values


def approximate_cell_average_kernel(
    size: int, order: int = 4, singular_order: int = 32
) -> np.ndarray:
    """Composite Gauss cell averages, refined on the four singular strips."""
    u_nodes, u_weights = leggauss(order)
    v_nodes, v_weights = leggauss(order + 1)
    accumulator = np.zeros((size, size), dtype=complex)
    for u_node, u_weight in zip(u_nodes, u_weights):
        u_values = -0.5 + (
            np.arange(size) + 0.5 + 0.5 * u_node
        ) / size
        for v_node, v_weight in zip(v_nodes, v_weights):
            v_values = -0.5 + (
                np.arange(size) + 0.5 + 0.5 * v_node
            ) / size
            accumulator += (
                u_weight
                * v_weight
                * scaling_kernel(u_values[:, None], v_values[None, :])
            )
    result = accumulator / (4.0 * size)

    singular_cells = np.array(
        sorted({0, size - 1, size // 2 - 1, size // 2}), dtype=int
    )
    u_nodes, u_weights = leggauss(singular_order)
    v_nodes, v_weights = leggauss(singular_order + 1)
    row_accumulator = np.zeros(
        (len(singular_cells), size), dtype=complex
    )
    column_accumulator = np.zeros(
        (size, len(singular_cells)), dtype=complex
    )
    for u_node, u_weight in zip(u_nodes, u_weights):
        u_all = -0.5 + (
            np.arange(size) + 0.5 + 0.5 * u_node
        ) / size
        u_strips = -0.5 + (
            singular_cells + 0.5 + 0.5 * u_node
        ) / size
        for v_node, v_weight in zip(v_nodes, v_weights):
            v_all = -0.5 + (
                np.arange(size) + 0.5 + 0.5 * v_node
            ) / size
            v_strips = -0.5 + (
                singular_cells + 0.5 + 0.5 * v_node
            ) / size
            weight = u_weight * v_weight
            row_accumulator += weight * scaling_kernel(
                u_strips[:, None], v_all[None, :]
            )
            column_accumulator += weight * scaling_kernel(
                u_all[:, None], v_strips[None, :]
            )
    result[singular_cells, :] = row_accumulator / (4.0 * size)
    result[:, singular_cells] = column_accumulator / (4.0 * size)
    return result


def central_hs_squared(
    remainder: np.ndarray, indices: np.ndarray, cutoff: float
) -> float:
    selected = np.abs(indices) < cutoff
    return float(
        np.vdot(remainder[np.ix_(selected, selected)],
                remainder[np.ix_(selected, selected)]).real
    )


def evaluate(size: int) -> dict[str, float]:
    indices = mode_indices(size)
    s_matrix = saw_response_fast(size)
    h_matrix = hardy_difference(size)
    a_matrix = limit_section(size)
    total_matrix = s_matrix + h_matrix
    remainder = total_matrix - a_matrix
    total2 = float(np.vdot(total_matrix, total_matrix).real)
    a2 = float(np.vdot(a_matrix, a_matrix).real)
    remainder2 = float(np.vdot(remainder, remainder).real)
    cross = float(2.0 * np.vdot(a_matrix, remainder).real)
    return {
        "N": size,
        "total2": total2,
        "a2": a2,
        "remainder2": remainder2,
        "cross": cross,
        "N_abs_cross": size * abs(cross),
        "central_hs2_eighth": central_hs_squared(
            remainder, indices, size / 8.0
        ),
        "central_hs2_quarter": central_hs_squared(
            remainder, indices, size / 4.0
        ),
        "identity_residual": abs(total2 - (a2 + remainder2 + cross)),
    }


def direct_identity_residual(size: int) -> dict[str, float]:
    direct = saw_response_direct(size)
    fast = saw_response_fast(size)
    step, ramp = step_and_ramp(size)
    remainder = direct + hardy_difference(size) - limit_section(size)
    return {
        "closed_formula": float(np.linalg.norm(direct - fast)),
        "step_plus_ramp": float(np.linalg.norm(direct - step - ramp)),
        "branchwise_difference": float(
            np.linalg.norm(remainder - branchwise_remainder(size))
        ),
        "unitarity": float(
            np.linalg.norm(
                overlap_closed(size).conj().T @ overlap_closed(size)
                - np.eye(size)
            )
        ),
    }


def main() -> int:
    started = time.time()
    print("=" * 86)
    print("mmst_telb_bound_b_probe -- TELB.BOUND.B.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 86)

    print("\nIDENTITIES")
    direct_checks = {
        size: direct_identity_residual(size) for size in DIRECT_SPLIT_SIZES
    }
    identity_max = max(
        max(values.values()) for values in direct_checks.values()
    )
    gate(
        "G01 exact formulas",
        identity_max < IDENTITY_TOL,
        "max residual %.3e / %.1e" % (identity_max, IDENTITY_TOL),
    )

    print("\nPER-N CONSTANT TABLE")
    print(
        "  %5s %12s %12s %12s %12s %10s %10s"
        % ("N", "||S+H||^2", "||A_N||^2", "||Res||^2",
           "N|cross|", "frac 1/8", "frac 1/4")
    )
    evaluated = {size: evaluate(size) for size in CHECKED_SIZES}
    rows = [evaluated[size] for size in SIZES]
    for row in rows:
        size = int(row["N"])
        print(
            "  %5d %12.9f %12.9f %12.9f %12.9f %10.6f %10.6f"
            % (
                size,
                row["total2"],
                row["a2"],
                row["remainder2"],
                row["N_abs_cross"],
                row["central_hs2_eighth"],
                row["central_hs2_quarter"],
            )
        )

    pin_errors = {
        str(size): abs(evaluated[size]["total2"] - value)
        for size, value in CORPUS_PINS.items()
    }
    max_pin_error = max(pin_errors.values())
    gate(
        "G02 corpus pins",
        max_pin_error < PIN_TOL,
        "max |difference| %.3e / %.1e" % (max_pin_error, PIN_TOL),
    )

    checked_rows = list(evaluated.values())
    max_a2 = max(row["a2"] for row in checked_rows)
    gate(
        "G03 rank-two constant",
        max_a2 <= C_A + 1.0e-13,
        "C_A %.9f, measured max %.9f, ratio %.6f"
        % (C_A, max_a2, C_A / max_a2),
    )

    max_remainder_row = max(checked_rows, key=lambda row: row["remainder2"])
    max_remainder2 = max_remainder_row["remainder2"]
    gate(
        "G04 remainder bound",
        max_remainder2 <= C_RES,
        "claimed %.6f, max %.9f at N=%d, ratio %.6f"
        % (
            C_RES,
            max_remainder2,
            max_remainder_row["N"],
            C_RES / max_remainder2,
        ),
    )

    max_cross_row = max(checked_rows, key=lambda row: row["N_abs_cross"])
    max_scaled_cross = max_cross_row["N_abs_cross"]
    gate(
        "G05 cross-term bound",
        max_scaled_cross <= C_CROSS,
        "claimed %.6f, max %.9f at N=%d, ratio %.6f"
        % (
            C_CROSS,
            max_scaled_cross,
            max_cross_row["N"],
            C_CROSS / max_scaled_cross,
        ),
    )

    max_central_eighth = max(
        row["central_hs2_eighth"] for row in checked_rows
    )
    max_central_quarter = max(
        row["central_hs2_quarter"] for row in checked_rows
    )
    central_hs_ok = (
        max_central_eighth <= C_FRAC_EIGHTH
        and max_central_quarter <= C_FRAC_QUARTER
    )
    gate(
        "G06 central HS-squared",
        central_hs_ok,
        "1/8 %.6f/%.6f; 1/4 %.6f/%.6f"
        % (
            max_central_eighth,
            C_FRAC_EIGHTH,
            max_central_quarter,
            C_FRAC_QUARTER,
        ),
    )

    assembled = C_A + C_RES + C_CROSS / min(SIZES)
    max_total2 = max(row["total2"] for row in checked_rows)
    assembly_ok = assembled <= TARGET and max_total2 <= TARGET
    gate(
        "G07 assembled bound",
        assembly_ok,
        "%.9f <= %.6f; measured max %.9f"
        % (assembled, TARGET, max_total2),
    )

    relaxed_numeric_ok = (
        max_remainder2 <= RELAXED_RES2_THRESHOLD
        and max_total2 <= RELAXED_TOTAL2_TARGET
    )
    gate(
        "G08 relaxed TEL-B threshold",
        relaxed_numeric_ok,
        "Res^2 %.9f <= %.9f; total^2 %.9f <= %.9f"
        % (
            max_remainder2,
            RELAXED_RES2_THRESHOLD,
            max_total2,
            RELAXED_TOTAL2_TARGET,
        ),
    )

    analytic_uniform_lemmas_supplied = (
        ANALYTIC_UNIFORM_RES_PROVED and ANALYTIC_UNIFORM_CROSS_PROVED
    )
    gate(
        "G09 analytic status",
        not RELAXED_UNIFORM_ANALYTIC_PROVED,
        "sharp Res=%s, sharp cross=%s, relaxed uniform=%s"
        % (
            ANALYTIC_UNIFORM_RES_PROVED,
            ANALYTIC_UNIFORM_CROSS_PROVED,
            RELAXED_UNIFORM_ANALYTIC_PROVED,
        ),
    )

    numeric_gates_ok = all(ok for _, ok, _ in CHECKS)
    if not numeric_gates_ok:
        verdict = "BOUND_B_FAILS"
    elif analytic_uniform_lemmas_supplied:
        verdict = "BOUND_B_CLOSED_WITH_CONSTANTS"
    elif RELAXED_UNIFORM_ANALYTIC_PROVED:
        verdict = "BOUND_B_UNIFORM_ANALYTIC"
    else:
        verdict = "BOUND_B_SKETCH_INCOMPLETE"
    gate("G10 verdict enum", verdict in VERDICT_ENUM, verdict)

    master_sizes = (16, 64, 256, 1024)
    master_residuals = {}
    for size in master_sizes:
        definition_remainder = (
            saw_response_fast(size)
            + hardy_difference(size)
            - limit_section(size)
        )
        master_residuals[size] = float(
            np.max(
                np.abs(
                    definition_remainder
                    - master_identity_remainder(size)
                )
            )
        )
    master_max = max(master_residuals.values())
    gate(
        "G11 master identity",
        master_max <= 1.0e-12,
        "max entry residual %.3e / 1e-12" % master_max,
    )

    c_star_method_1, c_star_raw_1 = singular_quadrature_extrapolation(
        (0.37, 0.73)
    )
    c_star_method_2, c_star_raw_2 = singular_quadrature_extrapolation(
        (0.211, 0.789)
    )
    c_star_agreement = abs(c_star_method_1 - c_star_method_2)
    c_star_numeric = max(c_star_method_1, c_star_method_2)
    gate(
        "G12 C_star quadratures",
        c_star_agreement <= 3.0e-4 and c_star_numeric <= C_STAR_LIMIT,
        "values %.9f/%.9f; agreement %.2e; limit %.4f"
        % (
            c_star_method_1,
            c_star_method_2,
            c_star_agreement,
            C_STAR_LIMIT,
        ),
    )

    e_sizes = (16, 32, 64, 128, 256, 512)
    scaled_e_sequence = []
    scaled_e_graded = []
    cell_norm2_sequence = []
    for size in e_sizes:
        definition_remainder = (
            saw_response_fast(size)
            + hardy_difference(size)
            - limit_section(size)
        )
        cell_kernel = approximate_cell_average_kernel(size)
        graded_kernel = graded_cell_average_kernel(size)
        scaled_e_sequence.append(
            float(np.sqrt(size) * np.linalg.norm(
                definition_remainder - cell_kernel
            ))
        )
        scaled_e_graded.append(
            float(np.sqrt(size) * np.linalg.norm(
                definition_remainder - graded_kernel
            ))
        )
        cell_norm2_sequence.append(
            float(np.vdot(graded_kernel, graded_kernel).real)
        )
    e_numeric_max = max(scaled_e_sequence)
    e_graded_max = max(scaled_e_graded)
    quadrature_agreement = max(
        abs(first - second)
        for first, second in zip(scaled_e_sequence, scaled_e_graded)
    )
    cell_norm_ok = all(value <= C_STAR_LIMIT for value in cell_norm2_sequence)
    deep_reference = graded_cell_average_kernel(64, levels=15)
    deep_remainder = (
        saw_response_fast(64) + hardy_difference(64) - limit_section(64)
    )
    graded_self_drift = abs(
        float(np.sqrt(64) * np.linalg.norm(deep_remainder - deep_reference))
        - scaled_e_graded[e_sizes.index(64)]
    )
    gate(
        "G13 cell-average remainder",
        (
            max(e_numeric_max, e_graded_max) <= C_E_NUMERIC
            and quadrature_agreement <= QUADRATURE_AGREEMENT_TOL
            and graded_self_drift <= GRADED_SELF_CONVERGENCE_TOL
            and cell_norm_ok
            and max(e_sizes) >= 512
        ),
        "max %.6f/%.6f vs %.2f; two-method %.2e; graded self-drift %.2e; "
        "||K_N||^2<=C_star %s"
        % (
            e_numeric_max,
            e_graded_max,
            C_E_NUMERIC,
            quadrature_agreement,
            graded_self_drift,
            cell_norm_ok,
        ),
    )

    relaxed_analytic_candidate = (
        np.sqrt(C_STAR_LIMIT) + C_E_NUMERIC / np.sqrt(16.0)
    ) ** 2
    candidate_dominates_samples = all(
        row["remainder2"]
        <= (
            np.sqrt(C_STAR_LIMIT)
            + C_E_NUMERIC / np.sqrt(row["N"])
        ) ** 2
        for row in checked_rows
    )
    gate(
        "G14 conditional assembly",
        (
            relaxed_analytic_candidate <= RELAXED_RES2_THRESHOLD
            and candidate_dominates_samples
        ),
        "%.9f <= %.9f; dominates measured=%s"
        % (
            relaxed_analytic_candidate,
            RELAXED_RES2_THRESHOLD,
            candidate_dominates_samples,
        ),
    )

    edge_offsets = np.array([1.0e-7, 1.0e-9, 1.0e-11])
    periodicity_residual = float(
        np.max(
            np.abs(
                periodic_potential(-0.5 + edge_offsets)
                - periodic_potential(0.5 - edge_offsets)
            )
            - 2.0 * pi * edge_offsets
        )
    )
    phi_star_jump = float(
        (phi_star(np.array([-0.5])) - phi_star(np.array([0.5])))[0]
    )
    interior = -0.5 + (np.arange(200000) + 0.5) / 200000.0
    prime_sup = float(np.max(np.abs(phi_star_prime(interior))))
    second_values = phi_star_second(interior)
    second_min = float(np.min(second_values))
    second_max = float(np.max(second_values))
    corner_offsets = np.array([1.0e-4, 1.0e-6, 1.0e-8])
    corner_values = np.array(
        [
            scaling_kernel(
                np.array([-0.5 + offset]), np.array([0.5 - offset])
            )[0]
            for offset in corner_offsets
        ]
    )
    corner_residual = float(np.max(np.abs(corner_values - 1.0 / pi)))
    structure_ok = (
        abs(periodicity_residual) <= 1.0e-6
        and abs(phi_star_jump - pi) <= 1.0e-12
        and abs(prime_sup - PHI_STAR_PRIME_SUP) <= 1.0e-4
        and second_min >= PHI_STAR_SECOND_INF - 1.0e-4
        and second_max <= PHI_STAR_SECOND_SUP + 1.0e-3
        and corner_residual <= 1.0e-3
    )
    gate(
        "G15 corrected kernel structure",
        structure_ok,
        "periodicity %.2e; jump-pi %.2e; sup|Phi*'| %.6f/%.6f; "
        "Phi*'' in [%.6f,%.6f]; corner-1/pi %.2e"
        % (
            periodicity_residual,
            abs(phi_star_jump - pi),
            prime_sup,
            PHI_STAR_PRIME_SUP,
            second_min,
            second_max,
            corner_residual,
        ),
    )

    reduction_rows = [
        one_variable_reduction(size) for size in (16, 64, 256, 1024)
    ]
    reduction_residual = max(row["identity_residual"] for row in reduction_rows)
    eta_sup = max(row["eta_sup"] for row in reduction_rows)
    eta_spread = max(row["eta_sup"] for row in reduction_rows) - min(
        row["eta_sup"] for row in reduction_rows
    )
    phi_scaled_sup = max(row["scaled_phi_sup"] for row in reduction_rows)
    delta_scaled_sup = max(row["scaled_delta_norm"] for row in reduction_rows)
    gate(
        "G16 one-variable reduction",
        (
            reduction_residual <= 1.0e-11
            and eta_spread <= 1.0e-12
            and abs(eta_sup - ETA_SUP_CLAIM) <= 5.0e-4
            and phi_scaled_sup <= PHI_N_SCALED_SUP
            and delta_scaled_sup <= DELTA_SCALED_SUP
        ),
        "residual %.2e; eta sup %.6f (N-spread %.1e); N*sup|phi| %.6f/%.2f; "
        "sqrtN||Delta|| %.6f/%.2f"
        % (
            reduction_residual,
            eta_sup,
            eta_spread,
            phi_scaled_sup,
            PHI_N_SCALED_SUP,
            delta_scaled_sup,
            DELTA_SCALED_SUP,
        ),
    )

    c_e_measured = max(e_numeric_max, e_graded_max)
    conditional_with_measured = (
        np.sqrt(C_STAR_LIMIT) + c_e_measured / np.sqrt(16.0)
    ) ** 2
    gate(
        "G17 corrected c_E requirement",
        (
            C_E_REQUIRED > C_E_NUMERIC
            and c_e_measured <= C_E_REQUIRED
            and conditional_with_measured <= RELAXED_RES2_THRESHOLD
        ),
        "required %.6f (not 0.30); measured %.6f; margin %.4f; "
        "assembled %.9f <= %.9f"
        % (
            C_E_REQUIRED,
            c_e_measured,
            C_E_REQUIRED / c_e_measured,
            conditional_with_measured,
            RELAXED_RES2_THRESHOLD,
        ),
    )

    phi_sample_bound_ok = phi_scaled_sup <= C_1_ANALYTIC
    gate(
        "G18 C2a analytic phi bound",
        C2A_ANALYTIC_PROVED and phi_sample_bound_ok,
        "c1 %.6f; sampled max %.9f at N=16,64,256,1024; "
        "samples=%s; all-N proof=%s"
        % (
            C_1_ANALYTIC,
            phi_scaled_sup,
            phi_sample_bound_ok,
            C2A_ANALYTIC_PROVED,
        ),
    )
    gate(
        "G19 C2b cell oscillation",
        C2B_ANALYTIC_PROVED and C_2_ANALYTIC is not None,
        "c2=%s; log subtraction and zero-row/column estimate proved=%s"
        % (C_2_ANALYTIC, C2B_ANALYTIC_PROVED),
    )
    assembled_c_e_ok = (
        C_E_ANALYTIC is not None
        and C_E_ANALYTIC >= c_e_measured
        and C_E_ANALYTIC <= C_E_REQUIRED
    )
    gate(
        "G20 analytic c_E assembly",
        bool(
            C2A_ANALYTIC_PROVED
            and C2B_ANALYTIC_PROVED
            and assembled_c_e_ok
        ),
        "analytic c_E=%s; measured %.9f; required %.9f"
        % (C_E_ANALYTIC, c_e_measured, C_E_REQUIRED),
    )

    runtime = time.time() - started
    file_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    passed = sum(ok for _, ok, _ in CHECKS)

    result = {
        "contract": "TELB.BOUND.B.01",
        "spec_sha": SPEC_SHA,
        "file_sha256": file_sha,
        "convention": "corpus e^{-ipx}; alpha=1/4; modes -N/2,...,N/2-1",
        "constants": {
            "C_A_exact_formula": "5/4 - 8/pi^2",
            "C_A": C_A,
            "C_RES": C_RES,
            "C_CROSS": C_CROSS,
            "C_FRAC_EIGHTH": C_FRAC_EIGHTH,
            "C_FRAC_QUARTER": C_FRAC_QUARTER,
            "TARGET": TARGET,
            "numerical_assembled": assembled,
            "analytic_uniform_assembled": None,
            "RSM_NORM_BOUND": RSM_NORM_BOUND,
            "M_NORM_ALLOWANCE": M_NORM_ALLOWANCE,
            "RELAXED_TOTAL2_TARGET": RELAXED_TOTAL2_TARGET,
            "RELAXED_RES2_THRESHOLD_with_C_CROSS": RELAXED_RES2_THRESHOLD,
            "C_STAR_LIMIT": C_STAR_LIMIT,
            "C_E_NUMERIC": C_E_NUMERIC,
            "C_1_ANALYTIC_CANDIDATE": C_1_ANALYTIC,
            "C_2_ANALYTIC": C_2_ANALYTIC,
            "C_E_ANALYTIC": C_E_ANALYTIC,
            "conditional_remainder_bound_N16": relaxed_analytic_candidate,
        },
        "measured_maxima": {
            "a2": max_a2,
            "remainder2": max_remainder2,
            "N_abs_cross": max_scaled_cross,
            "central_hs2_eighth": max_central_eighth,
            "central_hs2_quarter": max_central_quarter,
            "total2": max_total2,
        },
        "claimed_to_measured_ratios": {
            "remainder": C_RES / max_remainder2,
            "cross": C_CROSS / max_scaled_cross,
            "central_hs2_eighth": C_FRAC_EIGHTH / max_central_eighth,
            "central_hs2_quarter": C_FRAC_QUARTER / max_central_quarter,
        },
        "gates": {
            name: {"pass": ok, "detail": detail}
            for name, ok, detail in CHECKS
        },
        "rows": rows,
        "checked_sizes": list(CHECKED_SIZES),
        "dense_scan": {
            "all_even_from": 16,
            "all_even_through": EVEN_SCAN_MAX,
            "additional_sizes": [
                size for size in SIZES if size > EVEN_SCAN_MAX
            ],
            "remainder_max_N": int(max_remainder_row["N"]),
            "cross_max_N": int(max_cross_row["N"]),
        },
        "route_R2": {
            "master_identity_residuals": master_residuals,
            "C_star_method_1": c_star_method_1,
            "C_star_method_2": c_star_method_2,
            "C_star_agreement": c_star_agreement,
            "C_star_raw_method_1": c_star_raw_1,
            "C_star_raw_method_2": c_star_raw_2,
            "E_sizes": list(e_sizes),
            "sqrt_N_E_norm": scaled_e_sequence,
            "sqrt_N_E_norm_graded_quadrature": scaled_e_graded,
            "two_quadrature_agreement": quadrature_agreement,
            "graded_self_convergence_drift": graded_self_drift,
            "retracted_judge_E_reference": [
                0.2645, 0.2680, 0.2697, 0.2705, 0.2709, 0.2711
            ],
            "cell_kernel_norm2": cell_norm2_sequence,
            "quadrature_status": (
                "float64 singular-asymptotic extrapolation; not interval-certified"
            ),
            "analytic_c_E_status": (
                "not proved; but the stated obstruction is retracted: "
                "Phi_star'' is bounded (pi^2/3 <= Phi_star'' <= pi^2-4), so "
                "there are no logarithmic strips at u,v=+-1/2 to counterterm"
            ),
        },
        "corrected_structure": {
            "F_periodicity_residual": periodicity_residual,
            "phi_star_jump": phi_star_jump,
            "phi_star_edge_upper_exact": "-2*log2 - pi/2",
            "phi_star_edge_lower_exact": "-2*log2 + pi/2",
            "phi_star_centre_exact": "-log(2*pi)",
            "phi_star_prime_sup": prime_sup,
            "phi_star_prime_sup_exact": "2+pi",
            "phi_star_second_min": second_min,
            "phi_star_second_max": second_max,
            "phi_star_second_bounds_exact": "[pi^2/3, pi^2-4]",
            "corner_limit_residual": corner_residual,
            "corner_limit_exact": "1/pi",
            "singular_lines": "u=0 and v=0 only (logarithmic)",
            "retracted_claim": (
                "the note's singular lines u,v=+-1/2 and the non-integrable "
                "u^{-2}, (1/2-|u|)^{-2} parts of Phi_star'' do not exist"
            ),
        },
        "one_variable_reduction": {
            "rows": reduction_rows,
            "identity_residual_max": reduction_residual,
            "eta_sup": eta_sup,
            "eta_is_N_independent_spread": eta_spread,
            "scaled_phi_sup": phi_scaled_sup,
            "scaled_delta_norm_sup": delta_scaled_sup,
            "statement": (
                "N*Res_N(k,l) = r(u,v) + A*[(1-lambda)*d(eta) "
                "- lambda*d(phi_N)]/(v-u) for k!=l, k,l!=0"
            ),
        },
        "c_E_requirement": {
            "required": C_E_REQUIRED,
            "previously_assumed": C_E_NUMERIC,
            "measured": c_e_measured,
            "margin_ratio": C_E_REQUIRED / c_e_measured,
            "assembled_with_measured_c_E": conditional_with_measured,
        },
        "direct_identity_checks": direct_checks,
        "pin_errors": pin_errors,
        "proof_status": {
            "P1_saw_split": "proved",
            "P2_entrywise_limit": "proved",
            "P3_rank_two_norm": "proved",
            "P4_E_N_zero": "proved",
            "N1_uniform_remainder": "numerical_on_frozen_sizes",
            "N2_uniform_cross": "numerical_on_frozen_sizes",
            "analytic_fallback_remainder": (
                "proved: ||Res_N|| <= 3*sqrt(N)+sqrt(C_A), non-uniform"
            ),
            "analytic_fallback_cross": (
                "proved: N|cross| <= "
                "2*N*sqrt(C_A)*(3*sqrt(N)+sqrt(C_A)), non-uniform"
            ),
            "obstruction": (
                "the single missing inequality is ||Res_N - K_N||_HS <= "
                "c_E*N^{-1/2} for every even N>=16 with c_E <= 0.5435; the "
                "reduction leaves only (i) the one-dimensional bound "
                "|phi_N(k)| <= c_1/N (measured c_1 -> 1/2) and (ii) an "
                "explicit cell-oscillation bound for r, whose sole "
                "singularity is the logarithmic line u=0/v=0"
            ),
            "C2a_attempt": (
                "sampled c1=0.51 passes through N=1024, but the uniform "
                "Euler-Maclaurin remainder and seam-maximum claim are unproved"
            ),
            "C2b_attempt": (
                "the smooth-cell mean-value inequality holds, but no global "
                "c2 was obtained after variable-coefficient log subtraction; "
                "equation (33) also excludes the zero row and column"
            ),
            "single_relaxed_inequality_needed": (
                "sum_{k,l}|Res_N(k,l)|^2 <= %.16f for all even N>=16"
                % RELAXED_RES2_THRESHOLD
            ),
        },
        "verdict": verdict,
        "runtime_s": runtime,
        "honest_note": (
            "float64; P1-P4, the master identity, the one-variable reduction "
            "and the corrected kernel structure are analytic; N1-N2 checked "
            "on every even N through 512 plus 1024,2048,4096, so the "
            "all-even-N bound is not certified; the required c_E is 0.5435 "
            "and the measured c_E is 0.2012, but that is a measurement, not "
            "a proof; SEAM.MMST.TYPEIII.CHARGED.01 stays [O]."
        ),
    }
    output_path = Path(__file__).with_name("mmst_telb_bound_b_result.json")
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=1)

    all_gates_ok = all(ok for _, ok, _ in CHECKS)
    print("\nHONEST NOTE: %s" % result["honest_note"])
    print("GATES %d/%d" % (passed, len(CHECKS)))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha)
    print("runtime %.3f s" % runtime)
    print("wrote %s" % output_path)
    return 0 if all_gates_ok else 1


if __name__ == "__main__":
    sys.exit(main())
