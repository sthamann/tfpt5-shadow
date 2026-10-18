#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mmst_telb_trace_decomposition_probe -- TELB.TRACE.DECOMP.01

FROZEN SPEC v1 (2026-09-04).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  Writes one result JSON.

MANDATE: implement the EXACT trace decomposition of ||R_N||^2_HS for
the MMST TEL-B remainder into three trace sums computable WITHOUT
building the (16N)x(16N) matrix; validate against the direct matrix for
N <= 256; push N to 4096 to decide numerically whether the dyadic
increment law N*| ||R_2N|| - ||R_N|| | -> const (p=1) holds or a
residual log N survives; check the predicted leading log-N cancellation
between the three terms.

All numerics are float64, reported honestly as floats.  This is a
numerical decision on asymptotics, NOT a certificate.
SEAM.MMST.TYPEIII.CHARGED.01 stays [O].

PROVENANCE (copied verbatim, not imported): remainder_in_mode_basis and
helpers are copied verbatim from
experiments/tfpt-discovery/mmst_telb_kernel_structure_probe.py (which
itself copied from mmst_telb_tail_probe.py).  The source modules execute
cache/print bodies at import time, so import is not side-effect free.

Construction:
    D_0      = block_diag_k P_k   (P_k = fermi_covariance(p_k), p_k=2pi k/N)
    D_alpha  = block_diag_l P~_l   (P~_l = fermi_covariance(q_l), q_l=2pi(l+alpha)/N)
    W_kl     = (1/N) sum_x e^{2 pi i x (k-l-alpha)/N}
             = (1/N)(1 - e^{-2 pi i alpha})/(1 - e^{2 pi i (k-l-alpha)/N})
    |W_kl|^2 = sin^2(pi alpha)/(N^2 sin^2(pi (k-l-alpha)/N))
    H        = hardy_difference(S_N)  (N x N real symmetric)
    Q        = BOTTOM_PROJECTION - TOP_PROJECTION  (16 x 16, Tr Q^2 = 2)
    R_N      = D_0 - W D_alpha W^dagger - H (x) Q

EXACT IDENTITY (proof, 5 lines):
Let A := D_0 - W D_alpha W^dagger (Hermitian), B := H (x) Q (Hermitian),
so R = A - B and ||R||^2 = ||A||^2 + ||B||^2 - 2 Re Tr(A B).
(1) ||A||^2 = Tr[(W^dagger D_0 W - D_alpha)^2] (unitary invariance)
    = sum_k Tr(P_k^2) + sum_l Tr(P~_l^2) - 2 sum_{k,l} |W_kl|^2 Tr(P_k P~_l)
    = sum_{k,l} |W_kl|^2 ||P_k - P~_l||^2  (uses sum_l|W_kl|^2=sum_k|W_kl|^2=1).
(2) ||B||^2 = ||H||^2_HS Tr(Q^2) = 2 ||H||^2_HS.
(3) Tr(A B) = sum_k H_kk Tr(P_k Q) - sum_m (W^dagger H W)_mm Tr(P~_m Q),
    (W^dagger H W)_mm = sum_{k,l} conj(W_km) H_kl W_lm (H real symmetric).
Hence  ||R_N||^2 = T1 + T2 + T3  with
    T1 = sum_{k,l} |W_kl|^2 ||P_k - P~_l||^2_HS
    T2 = 2 ||H||^2_HS
    T3 = -2 [ sum_k H_kk Tr(P_k Q) - sum_m (W^dagger H W)_mm Tr(P~_m Q) ].
All traces real (H real symmetric, P_k, P~_l, Q Hermitian); assert
|Im| < 1e-10.  Identity exact regardless of whether P_k is a projector
(it is NOT at p_k = 0, where the template gives eigenvalue 1/2); we use
||P_k - P~_l||^2 directly, no projector assumption.

ALGORITHM (no (16N)x(16N) matrix):
* Tr(P_k P~_l) for ALL (k,l) as ONE real matmul: flatten each 16x16 into
  a 1024-vector [Re flat, Im flat]; G = V0 V~^T gives Tr(P_k P~_l) (real,
  Hermitian).  ||P_k - P~_l||^2 = Tr P_k^2 + Tr P~_l^2 - 2 Tr(P_k P~_l).
* T1 = sum_{k,l} |W_kl|^2 ||P_k - P~_l||^2  (elementwise, O(N^2)).
* T2 = 2 * sum_{i,j} H_ij^2.
* T3 second sum: Y = H @ W (real NxN times complex NxN -> complex NxN),
  (W^dagger H W)_mm = sum_k conj(W_km) Y_km.  Complexity O(N^3) only in
  the H @ W matmul; N = 4096 fits in memory (W, Y complex 4096^2 ~ 268 MB
  each); free intermediates.

SIZES: N in {16,32,64,96,128,192,256,384,512,768,1024,1536,2048,3072,
4096}.  If 4096 exceeds ~10 min or memory, stop at 3072.
Source pins: ||R_16||=2.09252848, ||R_96||=2.105079358.
Corpus dyadic products N*|d||R||| = 0.119783953, 0.121295482,
0.122435159, 0.122864637 for (16,32),(32,64),(64,128),(96,192).

PREDICTIONS (alpha=1/4, sin^2(pi alpha)=1/2):
    T1 ~ +(2/pi^2) ln N,  T2 ~ +(2/pi^2) ln N,  T3 ~ -(4/pi^2) ln N
so the +log N parts cancel exactly at leading order and
    ||R_N||^2 = a + b/N + O(N^-2),  A_R := |b|/(4 sqrt(a)) ~ 0.12.
Dyadic increments of the terms:
    dT1 -> (2/pi^2) ln 2 = 0.140456
    dT2 -> (2/pi^2) ln 2 = 0.140456
    dT3 -> -(4/pi^2) ln 2 = -0.280912
Predicted a ~ (2.105...)^2 ~ 4.431...; sqrt(a) ~ 2.105.

GATES:
G01  sum_l |W_kl|^2 = 1 to 1e-10 (N=64); Tr Q^2 = 2 to 1e-12; closed
     form for |W_kl|^2 matches template overlap to 1e-12.
G02  Identity validation: for N in {16,32,64,128,256} build R_N with the
     template remainder_in_mode_basis and compare ||R_N||^2 with
     T1+T2+T3: relative error < 1e-9 each.  Also reproduce the two source
     pins to 1e-6 and the four corpus dyadic products to 1e-6.
G03  Term table finite for all N; print T1, T2, T3, s, ||R|| for every N.
G04  Log cancellation: for each dyadic pair (N,2N) with N >= 256 compute
     dT_i := T_i(2N) - T_i(N); predicted limits as above.  Gate: at the
     largest available pair each |dT_i - prediction| < 0.02 (15%); report
     the actual sequence so a slow approach is visible.  Report fitted
     log-slopes of T1, T2, T3 vs ln N over N >= 512.
G05  Increment law: table of N*| ||R_2N|| - ||R_N|| | for all dyadic pairs
     including (256,512),(512,1024),(1024,2048),(2048,4096) and
     (384,768),(768,1536),(1536,3072).  Also N*(s(2N)-s(N)) (-> -b/2 if
     p=1).  Two competing fits on N >= 256:
       F_A: s = a + b/N + c/N^2
       F_B: s = a' + d ln N + b'/N
     Report RSS of each, fitted a,b,c,d, the Richardson estimate of a
     from the three largest N assuming 1/N (3-point, 1/N and 1/N^2), and
     A_R := |b|/(4 sqrt(a)).  Gate G05 := F_A RSS < F_B RSS AND |d|<0.005
     AND the last three N*|d||R||| values lie within 3% of each other.
G06  Bound headroom: A_R < 43 and lim estimate sqrt(a) < 3 (report
     sqrt(a) to 6 digits and sqrt(a) - 2.105079358).
G07  verdict enum frozen:
       TELB_INCREMENT_1_OVER_N  (G04 and G05 pass)
       TELB_RESIDUAL_LOG         (G05's log fit wins OR last increments
                                  drift monotonically by > 3%)
       INCONCLUSIVE              otherwise.

HONEST NOTE (always printed): float64 trace sums, no interval
certificate; identity exact, asymptotics numerical;
SEAM.MMST.TYPEIII.CHARGED.01 stays [O].
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

# Threads: allow multithreading for the N=4096 H @ W matmul.  The template
# pins threads to 1; we relax this so the single O(N^3) matmul at N=4096
# finishes in minutes.  Documented in the result JSON.
THREADS = os.environ.get("TELB_TRACE_THREADS", "8")
os.environ.setdefault("OMP_NUM_THREADS", THREADS)
os.environ.setdefault("MKL_NUM_THREADS", THREADS)
os.environ.setdefault("OPENBLAS_NUM_THREADS", THREADS)
os.environ.setdefault("NUMEXPR_NUM_THREADS", THREADS)

from math import pi, log  # noqa: E402

import numpy as np  # noqa: E402
from scipy.special import digamma, polygamma  # noqa: E402

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------------------
# Provenance: remainder construction copied verbatim from
# experiments/tfpt-discovery/mmst_telb_kernel_structure_probe.py
# (which copied from mmst_telb_tail_probe.py).  Import is not side-effect
# free; we copy verbatim.
# ---------------------------------------------------------------------------

MASS = 1.0
NY = 8
TRANSVERSE_DIMENSION = 2 * NY
ALPHA = 0.25
ZERO_CUT = 1.0e-11

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2


def strip_hamiltonian(momentum: float) -> np.ndarray:
    matrix = np.zeros(
        (TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION), dtype=complex
    )
    onsite = np.sin(momentum) * SX + (MASS - np.cos(momentum)) * SZ
    for y_index in range(NY):
        site = slice(2 * y_index, 2 * y_index + 2)
        matrix[site, site] = onsite
    for y_index in range(NY - 1):
        lower = slice(2 * y_index, 2 * y_index + 2)
        upper = slice(2 * y_index + 2, 2 * y_index + 4)
        matrix[upper, lower] = TY
        matrix[lower, upper] = TY.conj().T
    return matrix


def fermi_covariance(momentum: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    occupation = np.zeros_like(eigenvalues)
    occupation[eigenvalues < -ZERO_CUT] = 1.0
    occupation[np.abs(eigenvalues) <= ZERO_CUT] = 0.5
    return (eigenvectors * occupation) @ eigenvectors.conj().T


def edge_profiles() -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0))
    zero_indices = np.where(np.abs(eigenvalues) <= ZERO_CUT)[0]
    top_scores = [
        float(np.sum(np.abs(eigenvectors[:4, index]) ** 2))
        for index in zero_indices
    ]
    bottom_scores = [
        float(np.sum(np.abs(eigenvectors[-4:, index]) ** 2))
        for index in zero_indices
    ]
    top = eigenvectors[:, zero_indices[int(np.argmax(top_scores))]]
    bottom = eigenvectors[:, zero_indices[int(np.argmax(bottom_scores))]]
    return top, bottom


TOP_PROFILE, BOTTOM_PROFILE = edge_profiles()
TOP_PROJECTION = np.outer(TOP_PROFILE, TOP_PROFILE.conj())
BOTTOM_PROJECTION = np.outer(BOTTOM_PROFILE, BOTTOM_PROFILE.conj())
Q_PROJECTION = BOTTOM_PROJECTION - TOP_PROJECTION


def hardy_difference(mode_indices: np.ndarray) -> np.ndarray:
    shifted = mode_indices.astype(float) - ALPHA
    size = len(mode_indices)
    occupied_twisted = np.empty((size, size), dtype=float)
    factor = np.sin(pi * ALPHA) ** 2 / pi**2
    for row in range(size):
        for column in range(size):
            if row == column:
                overlap_sum = polygamma(1, shifted[row])
            else:
                overlap_sum = (
                    digamma(shifted[column]) - digamma(shifted[row])
                ) / (shifted[column] - shifted[row])
            occupied_twisted[row, column] = factor * overlap_sum
    occupied_untwisted = np.diag((mode_indices <= 0).astype(float))
    difference = occupied_untwisted - occupied_twisted
    return 0.5 * (difference + difference.T)


def remainder_in_mode_basis(size: int) -> np.ndarray:
    mode_indices = np.arange(-size // 2, size // 2)
    positions = np.arange(size)
    momenta_zero = 2 * pi * mode_indices / size
    momenta_alpha = 2 * pi * (mode_indices + ALPHA) / size
    fourier_zero = np.exp(-1j * np.outer(positions, momenta_zero)) / np.sqrt(size)
    fourier_alpha = np.exp(
        -1j * np.outer(positions, momenta_alpha)
    ) / np.sqrt(size)
    overlap = fourier_zero.conj().T @ fourier_alpha

    covariance_zero_blocks = np.asarray(
        [fermi_covariance(float(momentum)) for momentum in momenta_zero]
    )
    covariance_alpha_blocks = np.asarray(
        [fermi_covariance(float(momentum)) for momentum in momenta_alpha]
    )
    covariance_zero = np.zeros(
        (size * TRANSVERSE_DIMENSION, size * TRANSVERSE_DIMENSION),
        dtype=complex,
    )
    for position, block in enumerate(covariance_zero_blocks):
        start = position * TRANSVERSE_DIMENSION
        covariance_zero[
            start : start + TRANSVERSE_DIMENSION,
            start : start + TRANSVERSE_DIMENSION,
        ] = block

    covariance_alpha = np.einsum(
        "im,mab,jm->iajb",
        overlap,
        covariance_alpha_blocks,
        overlap.conj(),
        optimize=True,
    ).reshape(
        size * TRANSVERSE_DIMENSION,
        size * TRANSVERSE_DIMENSION,
    )

    hardy = hardy_difference(mode_indices)
    edge_remainder = np.kron(
        hardy,
        BOTTOM_PROJECTION - TOP_PROJECTION,
    )
    return covariance_zero - covariance_alpha - edge_remainder


def hs_norm(matrix: np.ndarray) -> float:
    return float(np.sqrt(np.vdot(matrix, matrix).real))


# ---- end verbatim copy ----
# ---------------------------------------------------------------------------
# Probe-specific frozen constants
# ---------------------------------------------------------------------------

T_DIM = TRANSVERSE_DIMENSION  # 16

SIZES = (16, 32, 64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048, 3072, 4096)
# Dyadic pairs used for the increment table (must all be present in SIZES).
DYADIC_PAIRS = (
    (16, 32), (32, 64), (64, 128), (96, 192),
    (128, 256), (256, 512), (384, 768), (512, 1024),
    (768, 1536), (1024, 2048), (1536, 3072), (2048, 4096),
)
VALIDATION_SIZES = (16, 32, 64, 128, 256)
SOURCE_HS = {16: 2.09252848, 96: 2.105079358}
SOURCE_PRODUCTS = (0.119783953, 0.121295482, 0.122435159, 0.122864637)
SOURCE_DYADIC = ((16, 32), (32, 64), (64, 128), (96, 192))

# Predicted leading log-N coefficients (natural log), alpha = 1/4.
LOG_COEF_T1 = 2.0 / (pi * pi)
LOG_COEF_T2 = 2.0 / (pi * pi)
LOG_COEF_T3 = -4.0 / (pi * pi)
LN2 = log(2.0)
PRED_DT1 = LOG_COEF_T1 * LN2   # 0.140456...
PRED_DT2 = LOG_COEF_T2 * LN2   # 0.140456...
PRED_DT3 = LOG_COEF_T3 * LN2   # -0.280912...

# Tolerances / cuts
TOL_ROW_UNIT = 1.0e-10
TOL_TRQ = 1.0e-12
TOL_W_CLOSED = 1.0e-12
TOL_IDENTITY = 1.0e-9
TOL_REPRO = 1.0e-6
TOL_IMAG = 1.0e-10
G04_TOL = 0.02          # 15% of ~0.14
G05_LOG_SLOPE_CUT = 0.005
G05_INC_DRIFT_CUT = 0.03
A_R_BOUND = 43.0
SQRT_A_BOUND = 3.0

VERDICT_ENUM = (
    "TELB_INCREMENT_1_OVER_N",
    "TELB_RESIDUAL_LOG",
    "INCONCLUSIVE",
)

CHECKS: list[tuple[str, bool]] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(
        "  [%s] %s%s"
        % ("PASS" if ok else "FAIL", name, ("  " + detail) if detail else "")
    )


def modes_of(size: int) -> np.ndarray:
    return np.arange(-size // 2, size // 2)


# ----
# Overlap matrix W (N x N complex) via the closed form, matching the
# template's overlap = fourier_zero.conj().T @ fourier_alpha.
# ----
def overlap_matrix(size: int) -> np.ndarray:
    """W_kl = (1/N)(1 - e^{-2 pi i alpha})/(1 - e^{2 pi i (k-l-alpha)/N})."""
    k = modes_of(size).astype(complex)
    l = modes_of(size).astype(complex)
    diff = k[:, None] - l[None, :] - ALPHA  # (k - l - alpha)
    denom = 1.0 - np.exp(2j * pi * diff / size)
    numer = 1.0 - np.exp(-2j * pi * ALPHA)
    return (numer / size) / denom


def w_abs2_closed(size: int) -> np.ndarray:
    """|W_kl|^2 = sin^2(pi alpha)/(N^2 sin^2(pi (k-l-alpha)/N))."""
    k = modes_of(size).astype(float)
    l = modes_of(size).astype(float)
    diff = k[:, None] - l[None, :] - ALPHA
    s = np.sin(pi * diff / size)
    return (np.sin(pi * ALPHA) ** 2) / (size * size * s * s)


# ----
# Trace decomposition.  All in float64 / complex128, no (16N)x(16N) matrix.
# ----
def trace_decomposition(size: int) -> dict:
    """Compute T1, T2, T3, s = T1+T2+T3 for R_N.  Returns dict of floats."""
    mode_indices = modes_of(size)
    momenta_zero = 2 * pi * mode_indices / size
    momenta_alpha = 2 * pi * (mode_indices + ALPHA) / size

    # P_k (N x 16 x 16) and P~_l (N x 16 x 16).
    p_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_zero])
    pa_blocks = np.asarray([fermi_covariance(float(m)) for m in momenta_alpha])

    # Tr(P_k^2), Tr(P~_l^2): real (Hermitian).
    tr_p2 = np.asarray([float(np.trace(p_blocks[i] @ p_blocks[i]).real)
                        for i in range(size)])
    tr_pa2 = np.asarray([float(np.trace(pa_blocks[i] @ pa_blocks[i]).real)
                        for i in range(size)])

    # Tr(P_k P~_l) for ALL (k,l) as ONE real matmul.
    # Flatten each 16x16 into [Re flat (256), Im flat (256)] -> 512-vector.
    # For Hermitian A, B: Tr(A B) = sum_{i,j} A_ij B_ji = sum_{i,j} A_ij conj(B_ij)
    # = Re(flat(A)) . Re(flat(B)) + Im(flat(A)) . Im(flat(B)).
    v0_re = p_blocks.reshape(size, T_DIM * T_DIM).real
    v0_im = p_blocks.reshape(size, T_DIM * T_DIM).imag
    va_re = pa_blocks.reshape(size, T_DIM * T_DIM).real
    va_im = pa_blocks.reshape(size, T_DIM * T_DIM).imag
    # G[k,l] = Tr(P_k P~_l) (real)
    g = v0_re @ va_re.T + v0_im @ va_im.T
    # ||P_k - P~_l||^2 = Tr P_k^2 + Tr P~_l^2 - 2 Tr(P_k P~_l)
    dist2 = tr_p2[:, None] + tr_pa2[None, :] - 2.0 * g  # (N, N)

    # |W_kl|^2
    wabs2 = w_abs2_closed(size)

    # T1 = sum_{k,l} |W_kl|^2 ||P_k - P~_l||^2
    t1 = float(np.sum(wabs2 * dist2))

    # T2 = 2 ||H||^2_HS
    hardy = hardy_difference(mode_indices)
    h_hs2 = float(np.sum(hardy * hardy))
    t2 = 2.0 * h_hs2

    # T3 = -2 [ sum_k H_kk Tr(P_k Q) - sum_m (W^dagger H W)_mm Tr(P~_m Q) ]
    tr_pq = np.asarray([float(np.trace(p_blocks[i] @ Q_PROJECTION).real)
                        for i in range(size)])
    tr_pa_q = np.asarray([float(np.trace(pa_blocks[i] @ Q_PROJECTION).real)
                         for i in range(size)])

    w = overlap_matrix(size)
    # Y = H @ W  (real NxN @ complex NxN -> complex NxN), O(N^3)
    y = hardy @ w
    # (W^dagger H W)_mm = sum_k conj(W_km) Y_km  -> sum over k axis 0
    whw_diag = np.sum(w.conj() * y, axis=0)  # (N,)

    # Imaginary parts must be ~0 (all traces real, H real symmetric).
    im_whw = float(np.max(np.abs(whw_diag.imag))) if size > 0 else 0.0
    im_tr_pq = float(np.max(np.abs(
        np.asarray([np.trace(p_blocks[i] @ Q_PROJECTION).imag
                    for i in range(size)])
    ))) if size > 0 else 0.0
    im_tr_pa_q = float(np.max(np.abs(
        np.asarray([np.trace(pa_blocks[i] @ Q_PROJECTION).imag
                    for i in range(size)])
    ))) if size > 0 else 0.0

    sum1 = float(np.sum(np.diag(hardy) * tr_pq))
    sum2 = float(np.sum(whw_diag.real * tr_pa_q))
    t3 = -2.0 * (sum1 - sum2)

    s = t1 + t2 + t3
    norm = float(np.sqrt(s)) if s > 0.0 else 0.0

    return {
        "N": size,
        "T1": t1, "T2": t2, "T3": t3, "s": s, "norm": norm,
        "im_whw": im_whw, "im_tr_pq": im_tr_pq, "im_tr_pa_q": im_tr_pa_q,
        "h_hs2": h_hs2, "tr_q2": float(np.trace(Q_PROJECTION @ Q_PROJECTION).real),
    }
# ---------------------------------------------------------------------------
# Fits and helpers
# ---------------------------------------------------------------------------

def fit_FA(sizes, svals):
    """F_A: s = a + b/N + c/N^2."""
    x = 1.0 / sizes
    design = np.column_stack([np.ones_like(x), x, x * x])
    coef, _, _, _ = np.linalg.lstsq(design, svals, rcond=None)
    a, b, c = float(coef[0]), float(coef[1]), float(coef[2])
    pred = a + b * x + c * x * x
    rss = float(np.sum((svals - pred) ** 2))
    return {"a": a, "b": b, "c": c, "rss": rss}


def fit_FB(sizes, svals):
    """F_B: s = a' + d ln N + b'/N."""
    x = 1.0 / sizes
    lnN = np.log(sizes)
    design = np.column_stack([np.ones_like(x), lnN, x])
    coef, _, _, _ = np.linalg.lstsq(design, svals, rcond=None)
    a, d, b = float(coef[0]), float(coef[1]), float(coef[2])
    pred = a + d * lnN + b * x
    rss = float(np.sum((svals - pred) ** 2))
    return {"a": a, "d": d, "b": b, "rss": rss}


def log_slope_terms(sizes, tvals):
    """OLS slope of T_i vs ln N."""
    lnN = np.log(sizes)
    design = np.column_stack([lnN, np.ones_like(lnN)])
    coef, _, _, _ = np.linalg.lstsq(design, tvals, rcond=None)
    return float(coef[0])


def richardson_a(sizes_sorted, svals_sorted):
    """3-point Richardson a = lim s(N), s = a + b/N + c/N^2,
    using three largest N (descending: n1>n2>n3)."""
    n1, n2, n3 = sizes_sorted
    s1, s2, s3 = svals_sorted
    x1, x2, x3 = 1.0 / n1, 1.0 / n2, 1.0 / n3
    mat = np.array([[1.0, x1, x1 * x1],
                    [1.0, x2, x2 * x2],
                    [1.0, x3, x3 * x3]])
    coef = np.linalg.solve(mat, np.array([s1, s2, s3]))
    return float(coef[0])
def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print("mmst_telb_trace_decomposition_probe -- TELB.TRACE.DECOMP.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("threads=%s  alpha=%.4f  sin^2(pi alpha)=%.6f"
          % (THREADS, ALPHA, np.sin(pi * ALPHA) ** 2))
    print("predictions: dT1=%.6f dT2=%.6f dT3=%.6f"
          % (PRED_DT1, PRED_DT2, PRED_DT3))
    print("=" * 78)

    # ---- G01: unitarity, Tr Q^2, closed form ----
    print()
    print("G01  structural identities (N=64)")
    n64 = 64
    w64 = overlap_matrix(n64)
    wabs2_64 = w_abs2_closed(n64)
    row_sum = np.sum(np.abs(w64) ** 2, axis=1)
    col_sum = np.sum(np.abs(w64) ** 2, axis=0)
    max_row_err = float(np.max(np.abs(row_sum - 1.0)))
    max_col_err = float(np.max(np.abs(col_sum - 1.0)))
    trq2 = float(np.trace(Q_PROJECTION @ Q_PROJECTION).real)
    mode_indices = modes_of(n64)
    positions = np.arange(n64)
    fz = np.exp(-1j * np.outer(positions, 2 * pi * mode_indices / n64)) / np.sqrt(n64)
    fa = np.exp(-1j * np.outer(positions, 2 * pi * (mode_indices + ALPHA) / n64)) / np.sqrt(n64)
    w_template = fz.conj().T @ fa
    w_closed_err = float(np.max(np.abs(w64 - w_template)))
    wabs2_template = np.abs(w_template) ** 2
    wabs2_err = float(np.max(np.abs(wabs2_64 - wabs2_template)))
    print("  max|sum_l|W_kl|^2 - 1| = %.3e" % max_row_err)
    print("  max|sum_k|W_kl|^2 - 1| = %.3e" % max_col_err)
    print("  Tr(Q^2) = %.12f   |Tr(Q^2)-2| = %.3e" % (trq2, abs(trq2 - 2.0)))
    print("  max|W_closed - W_template| = %.3e" % w_closed_err)
    print("  max||W|^2_closed - |W|^2_template| = %.3e" % wabs2_err)
    g01 = (max_row_err < TOL_ROW_UNIT and max_col_err < TOL_ROW_UNIT
           and abs(trq2 - 2.0) < TOL_TRQ
           and w_closed_err < TOL_W_CLOSED and wabs2_err < TOL_W_CLOSED)
    gate("G01 unitarity / Tr Q^2 / closed form", g01,
         "row=%.2e col=%.2e trq2=%.12f werr=%.2e w2err=%.2e"
         % (max_row_err, max_col_err, trq2, w_closed_err, wabs2_err))
    # ---- Compute decomposition for all sizes ----
    print()
    print("TRACE DECOMPOSITION  (N, T1, T2, T3, s, ||R||)")
    results = {}
    stopped_at = None
    for size in SIZES:
        tN = time.time()
        try:
            res = trace_decomposition(size)
        except MemoryError:
            print("  N=%5d  MEMORY ERROR -- stopping here" % size)
            stopped_at = size
            break
        except Exception as exc:
            print("  N=%5d  ERROR %r -- stopping here" % (size, exc))
            stopped_at = size
            break
        results[size] = res
        dt = time.time() - tN
        print("  N=%5d  T1=%.12f  T2=%.12f  T3=%.12f  s=%.12f  ||R||=%.12f  (%.2fs)"
              % (size, res["T1"], res["T2"], res["T3"], res["s"], res["norm"], dt))

    available = sorted(results.keys())
    print("  available sizes: %s" % available)

    # ---- G02: identity validation against direct matrix ----
    print()
    print("G02  identity validation (direct matrix vs T1+T2+T3)")
    id_ok = True
    for size in VALIDATION_SIZES:
        r_direct = remainder_in_mode_basis(size)
        s_direct = float(np.vdot(r_direct, r_direct).real)
        s_decomp = results[size]["s"]
        rel = abs(s_direct - s_decomp) / abs(s_direct) if s_direct != 0 else 0.0
        print("  N=%3d  s_direct=%.12f  s_decomp=%.12f  rel=%.3e"
              % (size, s_direct, s_decomp, rel))
        if rel >= TOL_IDENTITY:
            id_ok = False
    pin16_ok = abs(results[16]["norm"] - SOURCE_HS[16]) < TOL_REPRO
    pin96_ok = abs(results[96]["norm"] - SOURCE_HS[96]) < TOL_REPRO
    print("  ||R_16||=%.12f  pin=%.9f  |d|=%.3e  ok=%s"
          % (results[16]["norm"], SOURCE_HS[16],
             abs(results[16]["norm"] - SOURCE_HS[16]), pin16_ok))
    print("  ||R_96||=%.12f  pin=%.9f  |d|=%.3e  ok=%s"
          % (results[96]["norm"], SOURCE_HS[96],
             abs(results[96]["norm"] - SOURCE_HS[96]), pin96_ok))
    prod_ok = True
    prods = []
    for (n, n2), pin in zip(SOURCE_DYADIC, SOURCE_PRODUCTS):
        inc = abs(results[n2]["norm"] - results[n]["norm"])
        prod = n * inc
        prods.append(prod)
        okp = abs(prod - pin) < TOL_REPRO
        prod_ok = prod_ok and okp
        print("  %3d->%3d  N|d|=%.12f  pin=%.9f  |d|=%.3e  ok=%s"
              % (n, n2, prod, pin, abs(prod - pin), okp))
    g02 = id_ok and pin16_ok and pin96_ok and prod_ok
    gate("G02 identity + source pins + corpus products", g02,
         "id_ok=%s pin16=%s pin96=%s prod_ok=%s"
         % (id_ok, pin16_ok, pin96_ok, prod_ok))

    # ---- G03: term table finite ----
    g03 = all(np.isfinite(results[n]["T1"]) and np.isfinite(results[n]["T2"])
              and np.isfinite(results[n]["T3"]) and np.isfinite(results[n]["s"])
              for n in available)
    gate("G03 term table finite for all N", g03, "n_sizes=%d" % len(available))
    # ---- G04: log cancellation ----
    print()
    print("G04  log cancellation  dT_i = T_i(2N) - T_i(N)  (N >= 256)")
    dyadic_for_g04 = [(n, 2 * n) for n in available
                      if n >= 256 and (2 * n) in results]
    for (n, n2) in dyadic_for_g04:
        d1 = results[n2]["T1"] - results[n]["T1"]
        d2 = results[n2]["T2"] - results[n]["T2"]
        d3 = results[n2]["T3"] - results[n]["T3"]
        print("  %5d->%-5d  dT1=%+.9f (pred %+.6f, |d|=%.3e)  "
              "dT2=%+.9f (pred %+.6f, |d|=%.3e)  dT3=%+.9f (pred %+.6f, |d|=%.3e)"
              % (n, n2, d1, PRED_DT1, abs(d1 - PRED_DT1),
                 d2, PRED_DT2, abs(d2 - PRED_DT2),
                 d3, PRED_DT3, abs(d3 - PRED_DT3)))
    big_for_slope = [n for n in available if n >= 512]
    slope_t1 = slope_t2 = slope_t3 = float("nan")
    if len(big_for_slope) >= 3:
        sa = np.asarray(big_for_slope, dtype=float)
        slope_t1 = log_slope_terms(sa, np.asarray([results[n]["T1"] for n in big_for_slope]))
        slope_t2 = log_slope_terms(sa, np.asarray([results[n]["T2"] for n in big_for_slope]))
        slope_t3 = log_slope_terms(sa, np.asarray([results[n]["T3"] for n in big_for_slope]))
        print("  fitted log-slopes (N>=512): T1=%+.6f (pred %+.6f)  "
              "T2=%+.6f (pred %+.6f)  T3=%+.6f (pred %+.6f)"
              % (slope_t1, LOG_COEF_T1, slope_t2, LOG_COEF_T2,
                 slope_t3, LOG_COEF_T3))
    g04 = False
    if dyadic_for_g04:
        n_l, n2_l = dyadic_for_g04[-1]
        d1_l = results[n2_l]["T1"] - results[n_l]["T1"]
        d2_l = results[n2_l]["T2"] - results[n_l]["T2"]
        d3_l = results[n2_l]["T3"] - results[n_l]["T3"]
        g04 = (abs(d1_l - PRED_DT1) < G04_TOL and abs(d2_l - PRED_DT2) < G04_TOL
               and abs(d3_l - PRED_DT3) < G04_TOL)
    last_g04 = dyadic_for_g04[-1] if dyadic_for_g04 else (0, 0)
    gate("G04 log cancellation at largest pair", g04,
         "pairs=%d last=(%d,%d)" % (len(dyadic_for_g04), last_g04[0], last_g04[1]))
    # ---- G05: increment law ----
    print()
    print("G05  increment law  N*| ||R_2N|| - ||R_N|| |  and  N*(s(2N)-s(N))")
    inc_table = []
    for (n, n2) in DYADIC_PAIRS:
        if n in results and n2 in results:
            inc = abs(results[n2]["norm"] - results[n]["norm"])
            prod = n * inc
            ds = results[n2]["s"] - results[n]["s"]
            sprod = n * ds
            inc_table.append((n, n2, inc, prod, sprod))
            print("  %5d->%-5d  |d||R|||=%.12e  N|d|=%.12f  N*(s2N-sN)=%+.12f"
                  % (n, n2, inc, prod, sprod))
    fit_sizes = np.asarray([n for n in available if n >= 256], dtype=float)
    fit_s = np.asarray([results[n]["s"] for n in available if n >= 256], dtype=float)
    fa = fit_FA(fit_sizes, fit_s)
    fb = fit_FB(fit_sizes, fit_s)
    print("  F_A (a+b/N+c/N^2): a=%.12f b=%.12f c=%.12f rss=%.6e"
          % (fa["a"], fa["b"], fa["c"], fa["rss"]))
    print("  F_B (a'+d ln N+b'/N): a=%.12f d=%.6e b=%.12f rss=%.6e"
          % (fb["a"], fb["d"], fb["b"], fb["rss"]))
    big3 = sorted(available, reverse=True)[:3]
    if len(big3) == 3:
        a_rich = richardson_a(big3, [results[n]["s"] for n in big3])
    else:
        a_rich = float("nan")
    a_R = abs(fa["b"]) / (4.0 * np.sqrt(abs(fa["a"]))) if fa["a"] > 0 else float("nan")
    print("  Richardson a (3 largest N) = %.12f" % a_rich)
    print("  A_R = |b|/(4 sqrt(a)) = %.9f  (FA a=%.9f b=%.9f)" % (a_R, fa["a"], fa["b"]))
    last_prods = [p for (_, _, _, p, _) in inc_table][-3:]
    drift_ok = False
    if len(last_prods) == 3:
        m = np.mean(last_prods)
        drift_ok = all(abs(p - m) / m < G05_INC_DRIFT_CUT for p in last_prods)
        print("  last three N|d|: %s  mean=%.9f  within3%%=%s"
              % ([("%.9f" % p) for p in last_prods], m, drift_ok))
    g05 = (fa["rss"] < fb["rss"] and abs(fb["d"]) < G05_LOG_SLOPE_CUT and drift_ok)
    gate("G05 increment law 1/N (FA<FB, |d|<0.005, drift<3%)", g05,
         "FA_rss=%.3e FB_rss=%.3e |d|=%.3e drift=%s"
         % (fa["rss"], fb["rss"], abs(fb["d"]), drift_ok))
    # ---- G06: bound headroom ----
    sqrt_a = float(np.sqrt(abs(fa["a"]))) if fa["a"] > 0 else float("nan")
    sqrt_a_rich = float(np.sqrt(abs(a_rich))) if a_rich > 0 else float("nan")
    print()
    print("G06  bound headroom")
    print("  sqrt(a_FA) = %.9f   sqrt(a_FA) - 2.105079358 = %+.9f"
          % (sqrt_a, sqrt_a - 2.105079358))
    print("  sqrt(a_Richardson) = %.9f" % sqrt_a_rich)
    print("  A_R = %.9f   A_R < 43 = %s   sqrt(a) < 3 = %s"
          % (a_R, a_R < A_R_BOUND, sqrt_a < SQRT_A_BOUND))
    g06 = (a_R < A_R_BOUND and sqrt_a < SQRT_A_BOUND)
    gate("G06 bound headroom A_R<43 and sqrt(a)<3", g06,
         "A_R=%.6f sqrt_a=%.6f" % (a_R, sqrt_a))

    # ---- G07: verdict ----
    # monotonic drift of last increments by > 3%
    last_inc = [p for (_, _, _, p, _) in inc_table][-3:]
    mono_drift = False
    if len(last_inc) == 3:
        diffs = [last_inc[1] - last_inc[0], last_inc[2] - last_inc[1]]
        if (diffs[0] * diffs[1] > 0) and abs(last_inc[2] - last_inc[0]) / abs(last_inc[0]) > G05_INC_DRIFT_CUT:
            mono_drift = True
    if g04 and g05:
        verdict = "TELB_INCREMENT_1_OVER_N"
    elif (not g05 and (fb["rss"] < fa["rss"])) or mono_drift:
        verdict = "TELB_RESIDUAL_LOG"
    else:
        verdict = "INCONCLUSIVE"
    g07 = verdict in VERDICT_ENUM
    gate("G07 verdict enum frozen", g07, verdict)

    n_pass = sum(1 for _, ok in CHECKS if ok)
    rt = time.time() - t0
    file_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    # ---- write result JSON ----
    per_n_table = [
        {"N": n, "T1": results[n]["T1"], "T2": results[n]["T2"],
         "T3": results[n]["T3"], "s": results[n]["s"], "norm": results[n]["norm"]}
        for n in available
    ]
    dyadic_table = [
        {"N": n, "N2": n2, "inc": inc, "N_inc": prod, "N_ds": sprod}
        for (n, n2, inc, prod, sprod) in inc_table
    ]
    g04_seq = [
        {"N": n, "N2": n2,
         "dT1": results[n2]["T1"] - results[n]["T1"],
         "dT2": results[n2]["T2"] - results[n]["T2"],
         "dT3": results[n2]["T3"] - results[n]["T3"]}
        for (n, n2) in dyadic_for_g04
    ]
    result = {
        "contract": "TELB.TRACE.DECOMP.01",
        "spec_sha": SPEC_SHA,
        "file_sha256": file_sha,
        "gates": {name: ok for name, ok in CHECKS},
        "verdict": verdict,
        "per_N": per_n_table,
        "dyadic": dyadic_table,
        "g04_sequence": g04_seq,
        "fits": {
            "FA": fa, "FB": fb,
            "a_Richardson": a_rich, "A_R": a_R,
            "sqrt_a_FA": sqrt_a, "sqrt_a_Richardson": sqrt_a_rich,
            "log_slopes": {"T1": slope_t1, "T2": slope_t2, "T3": slope_t3},
        },
        "predictions": {
            "dT1": PRED_DT1, "dT2": PRED_DT2, "dT3": PRED_DT3,
            "log_coef_T1": LOG_COEF_T1, "log_coef_T2": LOG_COEF_T2,
            "log_coef_T3": LOG_COEF_T3,
        },
        "threads": int(THREADS),
        "stopped_at": stopped_at,
        "available_sizes": available,
        "runtime": rt,
        "honest_note": ("float64 trace sums, no interval certificate; "
                        "identity exact, asymptotics numerical; "
                        "SEAM.MMST.TYPEIII.CHARGED.01 stays [O]"),
    }
    out_path = Path(__file__).with_name(
        "mmst_telb_trace_decomposition_result.json")
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print()
    print("HONEST NOTE: float64 trace sums, no interval certificate; "
          "identity exact, asymptotics numerical; "
          "SEAM.MMST.TYPEIII.CHARGED.01 stays [O].")
    print("GATES %d/%d" % (n_pass, len(CHECKS)))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha)
    print("runtime %.3f s" % rt)
    print("wrote %s" % out_path)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
