#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mmst_telb_kernel_structure_probe -- TELB.KERNEL.STRUCTURE.01

FROZEN SPEC v1 (2026-09-03).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.

=======================================================================
MANDATE
=======================================================================
Diagnostic toward a rigorous proof of the TEL-B dyadic increment

    |‖R_{2N}‖_HS − ‖R_N‖_HS|  ≤  A_R / N     (A_R < 43)

for the MMST seam remainder R_N.  The corpus (v1016 / mmst_telb_tail
probe) measured N·|Δ‖R‖| ≈ 0.120–0.123 and blocked the certified-tail
route (N² D_N grows 530 → 19032; remainder UV-supported).  This probe
extracts the explicit 16×16 mode-blocks of R_N and tests whether they
have the structure that would make a finite-section (Böttcher–
Silbermann / Widom type) O(1/N) argument possible.

All numerics are float64, reported honestly as floats.  The goal is
STRUCTURE, not a certificate.  SEAM.MMST.TYPEIII.CHARGED.01 stays [O].

=======================================================================
CONSTRUCTION (copied, not imported)
=======================================================================
remainder_in_mode_basis and its helpers are copied verbatim from
experiments/tfpt-discovery/mmst_telb_tail_probe.py (the source has
module-level prints / cache fills; import is not side-effect free).
R_N is the (N·16)×(N·16) matrix in the untwisted longitudinal Fourier
basis, indexed by (mode k, transverse a), k ∈ {−N/2, …, N/2 − 1},
a ∈ {0, …, 15}.  The 16×16 block B_{k,l}(N) is the (k,l) block.

=======================================================================
SIZES / CORPUS PINS
=======================================================================
N in {16, 32, 64, 96, 128, 192, 256}.
Corpus dyadic pairs: (16,32), (32,64), (64,128), (96,192).
Source pins (mmst_telb_tail_probe F1 / paper remark 5.23–5.24):
  ‖R_16‖_HS = 2.09252848,  ‖R_96‖_HS = 2.105079358
  N·|Δ‖R‖| products = 0.119783953, 0.121295482, 0.122435159, 0.122864637
Band: products ∈ [0.119, 0.123].

=======================================================================
HYPOTHESES (numeric measures)
=======================================================================
Blocks live in C^{16×16}; ‖·‖ is Hilbert–Schmidt.  ‖B‖_ref(N) is the
max block HS at that N.  Class measure = max over classes of
max_{members} ‖B − class_mean‖_HS / ‖B‖_ref.

(H-Toeplitz)  B_{k,l} depends only on k−l.
(H-Hankel)    B_{k,l} depends only on k+l (edge/Hankel from the
              top/bottom projections).  Mode labels are an arithmetic
              progression, so array-index k−l / k+l coincide with
              mode-label differences / sums.
(H-N-stability) B_{k,l}(N) is independent of N for fixed integer (k,l):
              compare B_{k,l}(N) with B_{k,l}(2N) for all |k|,|l| < N/2.
              If this fails, report interior HS-ratio
              median ‖B(2N)‖/‖B(N)‖ (≈1/2 means 1/N scaling) and the
              doubled-index shift B_{k,l}(N) vs B_{2k,2l}(2N)
              (same physical momentum p = 2πk/N).

A structure "holds" when its max relative measure < STAB_CUT = 0.05.

=======================================================================
DECAY / IR-UV / CONVERGENCE
=======================================================================
Decay: OLS log–log slope of mean_d ‖B_{k,l}‖_HS versus |k−l| and
versus |k+l|, largest N, lags with mean HS > 1e-12; also the mass
slope of Σ ‖B‖_HS² versus |k−l| (the HS-summable object).
Classification of the mean-HS |k−l| slope (verdict input):
  HS-summable          slope ≤ −1.7   (~ 1/|lag|²)
  borderline           −1.7 < slope ≤ −0.7   (~ 1/|lag|)
  slower               slope > −0.7
Also report the HS² fraction on the diagonal k=l and the Toeplitz
measure with the lag-0 class excluded (a p-dependent multiplier is
diagonal in mode and makes lag-0 fail Toeplitz by itself).
IR fraction: ‖R_N‖_HS² carried by |k|,|l| ≤ N/4 (UV-supported iff
this is small).  UV-CUT: IR fraction < 0.25.  A Z-section with
decaying kernel would send this fraction → 1; a p-kernel keeps it
O(1) in N.

Convergence: ‖R_N‖_HS² = a − b/N^p, p on a grid in [0.1, 2.5], (a,b)
by linear least squares.  Implied dyadic constant
  pref = b(1 − 2^{−p}) / (2√a)
so that N·|Δ‖R‖| ∼ pref · N^{1−p}  (→ pref if p ≈ 1, should ≈ 0.12).
Also OLS ‖R_N‖_HS² = c0 + c1 N.  Converges iff p > 0.5 and a > max s
and |c1| is not a stable positive drift (c1 * N_max < 0.05 * max s).

=======================================================================
VERDICT (frozen enum; derived ONLY from the measures)
=======================================================================
SECTION_OF_FIXED_HS_OPERATOR
    H-N-stability holds AND decay HS-summable AND converges
    AND interior HS-ratio not in the 1/N band [0.40, 0.60].
    → (a) finite section of a fixed HS operator, Böttcher–Silbermann
      style, in principle provable.
FIXED_OPERATOR_BORDERLINE
    H-N-stability holds AND decay borderline AND converges
    AND ratio not in the 1/N band.
    → (b) fixed operator, borderline decay; needs sharper analysis.
NOT_A_SECTION
    H-N-stability fails OR interior HS-ratio in the 1/N band
    OR the power fit does not converge (p ≤ 0.5 or a unstable).
    → (c) N-dependent operator, not a Z-section; dyadic bound needs
      a different mechanism.
INCONCLUSIVE  otherwise.

=======================================================================
GATES
=======================================================================
G01  ‖R_16‖_HS and ‖R_96‖_HS within 1e-6 of the source pins.
G02  corpus N·|Δ‖R‖| within 1e-6 of the source-printed products
     AND every corpus product inside [0.119, 0.123].
G03  H-Toeplitz / H-Hankel / H-N-stability measures finite.
G04  both decay slopes finite; IR fraction in [0, 1].
G05  convergence fit a, b, p finite; implied pref finite.
G06  verdict is one of the four frozen enum tokens.

HONEST NOTE (always printed): float64 diagnostics of structure; no
interval certificate; SEAM.MMST.TYPEIII.CHARGED.01 stays [O].
"""

from __future__ import annotations

import hashlib
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

from math import pi  # noqa: E402

import numpy as np  # noqa: E402
from scipy.special import digamma, polygamma  # noqa: E402

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------------------
# Provenance: remainder construction copied verbatim from
# experiments/tfpt-discovery/mmst_telb_tail_probe.py (lines 28–168).
# Import is not used: that module executes the full cache/print body
# at import time.
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
    fourier_zero = np.exp(-1j * np.outer(positions, momenta_zero)) / np.sqrt(
        size
    )
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
        (
            size * TRANSVERSE_DIMENSION,
            size * TRANSVERSE_DIMENSION,
        ),
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


# ---------------------------------------------------------------------------
# Probe-specific frozen constants
# ---------------------------------------------------------------------------

SIZES = (16, 32, 64, 96, 128, 192, 256)
DYADIC_PAIRS = ((16, 32), (32, 64), (64, 128), (96, 192))
SOURCE_HS = {16: 2.09252848, 96: 2.105079358}
SOURCE_PRODUCTS = (0.119783953, 0.121295482, 0.122435159, 0.122864637)
PRODUCT_BAND = (0.119, 0.123)
STAB_CUT = 0.05
HS_SUMMABLE_CUT = -1.7
BORDERLINE_CUT = -0.7
IR_UV_CUT = 0.25
RATIO_ONE_OVER_N = (0.40, 0.60)
P_CONVERGE_CUT = 0.5
REPRO_TOL = 1.0e-6
BLOCK_FLOOR = 1.0e-12
VERDICT_ENUM = (
    "SECTION_OF_FIXED_HS_OPERATOR",
    "FIXED_OPERATOR_BORDERLINE",
    "NOT_A_SECTION",
    "INCONCLUSIVE",
)

CHECKS: list[tuple[str, bool]] = []
T_DIM = TRANSVERSE_DIMENSION


def gate(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(
        "  [%s] %s%s"
        % ("PASS" if ok else "FAIL", name, ("  " + detail) if detail else "")
    )


def modes_of(size: int) -> np.ndarray:
    return np.arange(-size // 2, size // 2)


def as_blocks(remainder: np.ndarray, size: int) -> np.ndarray:
    """(N, N, 16, 16) view: blocks[i, j] = B_{mode_i, mode_j}."""
    return remainder.reshape(size, T_DIM, size, T_DIM).transpose(0, 2, 1, 3)


def block_hs_array(blocks: np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum(np.abs(blocks) ** 2, axis=(2, 3)).real)


def class_max_rel(
    blocks: np.ndarray,
    lag: np.ndarray,
    ref_hs: float,
    exclude: tuple = (),
) -> float:
    """Max over lag-classes of max_member ‖B − mean‖_HS / ref_hs."""
    worst = 0.0
    unique = np.unique(lag)
    excluded = set(exclude)
    for value in unique:
        if int(value) in excluded:
            continue
        mask = lag == value
        count = int(np.count_nonzero(mask))
        if count < 2:
            continue
        sl = blocks[mask]
        mean = sl.mean(axis=0)
        dev = sl - mean
        max_dev = float(np.sqrt(np.max(np.sum(np.abs(dev) ** 2, axis=(1, 2)).real)))
        worst = max(worst, max_dev / ref_hs)
    return worst


def loglog_slope(xs: np.ndarray, ys: np.ndarray) -> float:
    mask = (xs > 0.0) & (ys > BLOCK_FLOOR)
    if int(np.count_nonzero(mask)) < 3:
        return float("nan")
    lx = np.log(xs[mask])
    ly = np.log(ys[mask])
    design = np.column_stack([lx, np.ones_like(lx)])
    coef, _, _, _ = np.linalg.lstsq(design, ly, rcond=None)
    return float(coef[0])


def lag_profiles(
    blocks: np.ndarray, signed_lag: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """lags ≥ 1, mean HS, and total HS² mass per |lag|."""
    abs_lag = np.abs(signed_lag)
    max_lag = int(abs_lag.max())
    hs = block_hs_array(blocks)
    lags = []
    means = []
    masses = []
    for d in range(1, max_lag + 1):
        mask = abs_lag == d
        if not np.any(mask):
            continue
        lags.append(float(d))
        means.append(float(np.mean(hs[mask])))
        masses.append(float(np.sum(hs[mask] ** 2)))
    return np.asarray(lags), np.asarray(means), np.asarray(masses)


def n_stability_report(
    blocks_n: np.ndarray,
    blocks_2n: np.ndarray,
    size: int,
) -> dict:
    modes_n = modes_of(size)
    modes_2n = modes_of(2 * size)
    pos_n = {int(m): i for i, m in enumerate(modes_n)}
    pos_2n = {int(m): i for i, m in enumerate(modes_2n)}
    cutoff = size / 2.0
    interior = [int(m) for m in modes_n if abs(int(m)) < cutoff]
    max_rel = 0.0
    max_rel_shift = 0.0
    ratios = []
    num = 0.0
    den = 0.0
    for k in interior:
        ik = pos_n[k]
        ik2 = pos_2n[k]
        ik_d = pos_2n[2 * k]
        for l in interior:
            il = pos_n[l]
            il2 = pos_2n[l]
            il_d = pos_2n[2 * l]
            b_n = blocks_n[ik, il]
            b_2 = blocks_2n[ik2, il2]
            b_d = blocks_2n[ik_d, il_d]
            hs_n = float(np.sqrt(np.vdot(b_n, b_n).real))
            hs_2 = float(np.sqrt(np.vdot(b_2, b_2).real))
            hs_d = float(np.sqrt(np.vdot(b_d, b_d).real))
            diff = b_n - b_2
            diff_s = b_n - b_d
            hs_diff = float(np.sqrt(np.vdot(diff, diff).real))
            hs_diff_s = float(np.sqrt(np.vdot(diff_s, diff_s).real))
            scale = max(hs_n, hs_2, BLOCK_FLOOR)
            scale_s = max(hs_n, hs_d, BLOCK_FLOOR)
            max_rel = max(max_rel, hs_diff / scale)
            max_rel_shift = max(max_rel_shift, hs_diff_s / scale_s)
            num += hs_diff ** 2
            den += hs_n ** 2
            if hs_n > BLOCK_FLOOR:
                ratios.append(hs_2 / hs_n)
    median_ratio = float(np.median(ratios)) if ratios else float("nan")
    rms_rel = float(np.sqrt(num / den)) if den > 0.0 else float("nan")
    return {
        "max_rel": max_rel,
        "rms_rel": rms_rel,
        "median_ratio": median_ratio,
        "max_rel_shift": max_rel_shift,
        "n_pairs": len(interior) ** 2,
    }


def fit_power(sizes: np.ndarray, values: np.ndarray) -> tuple[float, float, float, float]:
    """‖R_N‖² = a − b/N^p by p-grid + OLS.  Returns a, b, p, rss."""
    best_rss = float("inf")
    best = (float("nan"), float("nan"), float("nan"), float("inf"))
    coarse = np.linspace(0.10, 2.50, 241)
    for p in coarse:
        x = sizes ** (-p)
        design = np.column_stack([np.ones_like(x), -x])
        coef, residuals, _, _ = np.linalg.lstsq(design, values, rcond=None)
        a, b = float(coef[0]), float(coef[1])
        pred = a - b * x
        rss = float(np.sum((values - pred) ** 2))
        if rss < best_rss:
            best_rss = rss
            best = (a, b, float(p), rss)
    a0, b0, p0, _ = best
    fine = np.linspace(max(0.10, p0 - 0.05), min(2.50, p0 + 0.05), 101)
    for p in fine:
        x = sizes ** (-p)
        design = np.column_stack([np.ones_like(x), -x])
        coef, _, _, _ = np.linalg.lstsq(design, values, rcond=None)
        a, b = float(coef[0]), float(coef[1])
        pred = a - b * x
        rss = float(np.sum((values - pred) ** 2))
        if rss < best_rss:
            best_rss = rss
            best = (a, b, float(p), rss)
    return best


def decay_class(slope: float) -> str:
    if not np.isfinite(slope):
        return "undefined"
    if slope <= HS_SUMMABLE_CUT:
        return "HS-summable"
    if slope <= BORDERLINE_CUT:
        return "borderline"
    return "slower"


def classify_verdict(
    nstab_holds: bool,
    median_ratio: float,
    slope_diff: float,
    converges: bool,
) -> str:
    ratio_one_over_n = (
        np.isfinite(median_ratio)
        and RATIO_ONE_OVER_N[0] <= median_ratio <= RATIO_ONE_OVER_N[1]
    )
    klass = decay_class(slope_diff)
    if (not nstab_holds) or ratio_one_over_n or (not converges):
        return "NOT_A_SECTION"
    if klass == "HS-summable" and nstab_holds and converges:
        return "SECTION_OF_FIXED_HS_OPERATOR"
    if klass == "borderline" and nstab_holds and converges:
        return "FIXED_OPERATOR_BORDERLINE"
    return "INCONCLUSIVE"


def assessment_paragraph(
    verdict: str,
    toe: float,
    han: float,
    nstab: float,
    ratio: float,
    shift: float,
    slope_d: float,
    slope_s: float,
    ir_frac: float,
    a: float,
    b: float,
    p: float,
    pref: float,
) -> str:
    head = (
        "H-Toeplitz max-rel %.4e (%s); H-Hankel max-rel %.4e (%s); "
        "H-N-stability max-rel %.4e (%s); interior HS-ratio median %.4f; "
        "doubled-index (p-matched) max-rel %.4e; |k-l| slope %.3f (%s); "
        "|k+l| slope %.3f (%s); IR(|k|,|l|<=N/4) fraction %.4f of ||R||_HS^2; "
        "fit a=%.6f b=%.6f p=%.3f, implied N*|Δ| pref %.4f."
        % (
            toe,
            "holds" if toe < STAB_CUT else "fails",
            han,
            "holds" if han < STAB_CUT else "fails",
            nstab,
            "holds" if nstab < STAB_CUT else "fails",
            ratio,
            shift,
            slope_d,
            decay_class(slope_d),
            slope_s,
            decay_class(slope_s),
            ir_frac,
            a,
            b,
            p,
            pref,
        )
    )
    if verdict == "SECTION_OF_FIXED_HS_OPERATOR":
        body = (
            " Interior blocks at fixed integer (k,l) are N-stable and "
            "off-diagonal HS decay is at least 1/|lag|^2, so R_N is "
            "consistent with the N-section of a fixed HS operator on "
            "l2(Z)⊗C^16. A Böttcher–Silbermann / Widom finite-section "
            "argument for the O(1/N) dyadic HS-norm increment is the "
            "indicated proof route."
        )
    elif verdict == "FIXED_OPERATOR_BORDERLINE":
        body = (
            " Interior blocks are N-stable (section of a fixed operator) "
            "but the lag decay is only ~1/|lag| (HS-summable borderline). "
            "A finite-section argument remains possible but needs a "
            "sharper (log-corrected or cancellation) analysis; the naive "
            "HS-sum test does not close."
        )
    elif verdict == "NOT_A_SECTION":
        body = (
            " Fixed-(k,l) blocks change with N (interior HS-ratio "
            "in the 1/N band; doubled-index p-matching also fails), "
            "so R_N is not the N-section of one N-independent operator "
            "on l2(Z). Lag decay is slower than 1/|k-l| and the IR "
            "fraction |k|,|l|≤N/4 stays O(1) in N rather than →1, "
            "which is the signature of a physical-momentum kernel "
            "B_{k,l}(N) ∼ N^{-1} K(k/N, l/N), not a decaying kernel "
            "on Z. The dyadic bound |‖R_2N‖−‖R_N‖|≤A_R/N needs a "
            "different mechanism (symbol calculus in p=2πk/N, "
            "compactness of a p-kernel, or a coercivity estimate), "
            "not Böttcher–Silbermann finite sections of a fixed HS "
            "operator."
        )
    else:
        body = (
            " The three structural tests do not line up on a single "
            "finite-section story. More N or a different basis is "
            "required before choosing a proof route."
        )
    return (
        head
        + body
        + " This is a float64 structure diagnostic, not a certificate."
    )


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print("mmst_telb_kernel_structure_probe -- TELB.KERNEL.STRUCTURE.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)

    cache: dict[int, np.ndarray] = {}
    norms: dict[int, float] = {}
    print()
    print("REPRODUCTION  ‖R_N‖_HS  (float64; not an interval certificate)")
    for size in SIZES:
        cache[size] = remainder_in_mode_basis(size)
        norms[size] = hs_norm(cache[size])
        pin = SOURCE_HS.get(size)
        extra = ""
        if pin is not None:
            extra = "  source_pin=%.9f  |Δ|=%.3e" % (
                pin,
                abs(norms[size] - pin),
            )
        print("  N=%3d  ||R_N||_HS=%.12f%s" % (size, norms[size], extra))

    g01 = abs(norms[16] - SOURCE_HS[16]) < REPRO_TOL and abs(
        norms[96] - SOURCE_HS[96]
    ) < REPRO_TOL
    gate(
        "G01 source HS pins N=16 and N=96 within 1e-6",
        g01,
        "N16=%.12f N96=%.12f" % (norms[16], norms[96]),
    )

    print()
    print("DYADIC  N·|‖R_2N‖_HS − ‖R_N‖_HS|")
    products = []
    for (n, n2), pin in zip(DYADIC_PAIRS, SOURCE_PRODUCTS):
        increment = abs(norms[n2] - norms[n])
        product = n * increment
        products.append(product)
        print(
            "  %3d→%3d  |Δ|=%.12f  N|Δ|=%.12f  source=%.9f  |Δpin|=%.3e"
            % (n, n2, increment, product, pin, abs(product - pin))
        )
    extra_inc = abs(norms[256] - norms[128])
    extra_prod = 128.0 * extra_inc
    print(
        "  128→256  |Δ|=%.12f  N|Δ|=%.12f  (not a corpus pair)"
        % (extra_inc, extra_prod)
    )
    pin_ok = all(
        abs(prod - pin) < REPRO_TOL
        for prod, pin in zip(products, SOURCE_PRODUCTS)
    )
    band_ok = all(PRODUCT_BAND[0] <= prod <= PRODUCT_BAND[1] for prod in products)
    gate(
        "G02 corpus N*|Δ| within 1e-6 of source and inside [0.119, 0.123]",
        pin_ok and band_ok,
        "products=%s" % (", ".join("%.9f" % p for p in products)),
    )

    # Structure at the largest N, plus N-stability across dyadic pairs.
    print()
    print("STRUCTURE  16×16 blocks B_{k,l}(N)")
    big = 256
    blocks_big = as_blocks(cache[big], big)
    hs_big = block_hs_array(blocks_big)
    ref_big = float(np.max(hs_big))
    n_idx, l_idx = np.indices((big, big))
    lag_diff = n_idx - l_idx
    lag_sum = n_idx + l_idx
    toe = class_max_rel(blocks_big, lag_diff, ref_big)
    han = class_max_rel(blocks_big, lag_sum, ref_big)
    toe_off = class_max_rel(blocks_big, lag_diff, ref_big, exclude=(0,))
    han_off = class_max_rel(blocks_big, lag_sum, ref_big, exclude=(0,))
    diag_idx = np.arange(big)
    diag_hs = hs_big[diag_idx, diag_idx]
    total_hs2 = float(np.sum(hs_big ** 2))
    diag_frac = float(np.sum(diag_hs ** 2) / total_hs2) if total_hs2 > 0.0 else float("nan")
    diag_blocks = blocks_big[diag_idx, diag_idx]
    diag_mean = diag_blocks.mean(axis=0)
    diag_dev = float(
        np.sqrt(np.max(np.sum(np.abs(diag_blocks - diag_mean) ** 2, axis=(1, 2)).real))
    )
    print("  N=%d  max_block_HS=%.12f  ||R||=%.12f" % (big, ref_big, norms[big]))
    print("  (H-Toeplitz) max_rel vs ||B||_ref = %.12e  (off-diag %.12e)" % (toe, toe_off))
    print("  (H-Hankel)   max_rel vs ||B||_ref = %.12e  (off-diag %.12e)" % (han, han_off))
    print(
        "  diagonal HS^2 fraction=%.8f  diagonal class spread/ref=%.6e"
        % (diag_frac, diag_dev / ref_big)
    )

    print()
    print("  (H-N-stability)  B_{k,l}(N) vs B_{k,l}(2N) for |k|,|l| < N/2")
    stab_pairs = []
    for n, n2 in ((16, 32), (32, 64), (64, 128), (96, 192), (128, 256)):
        rep = n_stability_report(as_blocks(cache[n], n), as_blocks(cache[n2], n2), n)
        stab_pairs.append((n, n2, rep))
        print(
            "  %3d→%3d  max_rel=%.6e  rms_rel=%.6e  "
            "median_HS_ratio=%.6f  doubled-index max_rel=%.6e  pairs=%d"
            % (
                n,
                n2,
                rep["max_rel"],
                rep["rms_rel"],
                rep["median_ratio"],
                rep["max_rel_shift"],
                rep["n_pairs"],
            )
        )
    nstab = max(rep["max_rel"] for _, _, rep in stab_pairs)
    nstab_rms = max(rep["rms_rel"] for _, _, rep in stab_pairs)
    median_ratio = float(
        np.median([rep["median_ratio"] for _, _, rep in stab_pairs])
    )
    shift = max(rep["max_rel_shift"] for _, _, rep in stab_pairs)
    nstab_holds = nstab < STAB_CUT
    print(
        "  N-stability MAX max_rel=%.6e  MAX rms_rel=%.6e  "
        "median ratio=%.6f  MAX doubled-index=%.6e  holds=%s"
        % (nstab, nstab_rms, median_ratio, shift, nstab_holds)
    )
    if median_ratio >= RATIO_ONE_OVER_N[0] and median_ratio <= RATIO_ONE_OVER_N[1]:
        scale_note = "interior blocks scale ~1/N"
    elif abs(median_ratio - 1.0) < 0.10:
        scale_note = "interior blocks ~ N-independent in HS scale"
    else:
        scale_note = "interior HS-ratio %.3f (neither 1 nor 1/2)" % median_ratio
    print("  scale diagnostic: %s" % scale_note)

    g03 = all(
        np.isfinite(x)
        for x in (toe, han, toe_off, han_off, diag_frac, nstab, nstab_rms, median_ratio, shift)
    )
    gate(
        "G03 hypothesis measures finite",
        g03,
        "toe=%.4e han=%.4e nstab=%.4e" % (toe, han, nstab),
    )

    print()
    print("DECAY  mean ‖B_{k,l}‖_HS and HS² mass vs |k−l| / |k+l|  (N=%d)" % big)
    lags_d, means_d, mass_d = lag_profiles(blocks_big, lag_diff)
    lags_s, means_s, mass_s = lag_profiles(blocks_big, lag_sum)
    slope_d = loglog_slope(lags_d, means_d)
    slope_s = loglog_slope(lags_s, means_s)
    slope_mass_d = loglog_slope(lags_d, mass_d)
    slope_mass_s = loglog_slope(lags_s, mass_s)
    print(
        "  lag=  0  mean_HS(k=l)=%.6e  (diagonal)"
        % float(np.mean(diag_hs))
    )
    for d in (1, 2, 4, 8, 16, 32, 64):
        md = float(means_d[lags_d == d][0]) if np.any(lags_d == d) else float("nan")
        ms = float(means_s[lags_s == d][0]) if np.any(lags_s == d) else float("nan")
        print("  lag=%3d  mean_HS(|k-l|)=%.6e  mean_HS(|k+l|)=%.6e" % (d, md, ms))
    abs_diff = np.abs(lag_diff)
    for window in (0, 1, 8, big // 16, big // 4):
        frac_w = float(np.sum(hs_big[abs_diff <= window] ** 2) / total_hs2)
        print("  HS^2 fraction |k-l|<=%d = %.8f" % (window, frac_w))
    print(
        "  log-log mean-HS slope |k-l|=%.4f (%s)  |k+l|=%.4f (%s)"
        % (slope_d, decay_class(slope_d), slope_s, decay_class(slope_s))
    )
    print(
        "  log-log HS^2-mass slope |k-l|=%.4f  |k+l|=%.4f"
        % (slope_mass_d, slope_mass_s)
    )

    print()
    print("IR / UV  fraction of ‖R_N‖_HS² on |k|,|l| ≤ N/4")
    ir_fracs = {}
    for size in SIZES:
        blocks = as_blocks(cache[size], size)
        hs = block_hs_array(blocks)
        modes = modes_of(size)
        ir = np.abs(modes) <= (size / 4.0)
        total = float(np.sum(hs ** 2))
        ir_mass = float(np.sum(hs[np.ix_(ir, ir)] ** 2))
        ir_fracs[size] = ir_mass / total if total > 0.0 else float("nan")
        print(
            "  N=%3d  IR_frac=%.8f  UV_complement=%.8f"
            % (size, ir_fracs[size], 1.0 - ir_fracs[size])
        )
    ir_big = ir_fracs[big]
    g04 = (
        np.isfinite(slope_d)
        and np.isfinite(slope_s)
        and np.isfinite(slope_mass_d)
        and np.isfinite(slope_mass_s)
        and 0.0 <= ir_big <= 1.0
        and 0.0 <= diag_frac <= 1.0
    )
    gate(
        "G04 decay slopes finite; IR fraction in [0,1]",
        g04,
        "slopes=(%.4f, %.4f) mass=(%.4f, %.4f) IR=%.6f diag=%.6f"
        % (slope_d, slope_s, slope_mass_d, slope_mass_s, ir_big, diag_frac),
    )

    print()
    print("CONVERGENCE  ‖R_N‖_HS² = a − b/N^p")
    size_arr = np.asarray(SIZES, dtype=float)
    svals = np.asarray([norms[n] ** 2 for n in SIZES], dtype=float)
    a, b, p, rss = fit_power(size_arr, svals)
    pred = a - b * size_arr ** (-p)
    resid = float(np.max(np.abs(svals - pred)))
    # p=1 comparison
    x1 = 1.0 / size_arr
    design1 = np.column_stack([np.ones_like(x1), -x1])
    coef1, _, _, _ = np.linalg.lstsq(design1, svals, rcond=None)
    a1, b1 = float(coef1[0]), float(coef1[1])
    # linear drift
    design_lin = np.column_stack([np.ones_like(size_arr), size_arr])
    coef_lin, _, _, _ = np.linalg.lstsq(design_lin, svals, rcond=None)
    c0, c1 = float(coef_lin[0]), float(coef_lin[1])
    sqrt_a = float(np.sqrt(abs(a))) if a != 0.0 else float("nan")
    pref = (
        b * (1.0 - 2.0 ** (-p)) / (2.0 * sqrt_a)
        if np.isfinite(sqrt_a) and sqrt_a > 0.0
        else float("nan")
    )
    pref_p1 = b1 / (4.0 * math_sqrt_pos(a1))
    drift_mass = abs(c1) * float(SIZES[-1])
    converges = (
        np.isfinite(a)
        and np.isfinite(b)
        and np.isfinite(p)
        and p > P_CONVERGE_CUT
        and a > float(np.max(svals))
        and drift_mass < 0.05 * float(np.max(svals))
    )
    print("  s(N)=‖R_N‖_HS²: " + ", ".join("%.10f" % v for v in svals))
    print("  fit a=%.10f  b=%.10f  p=%.4f  max|resid|=%.3e  rss=%.3e" % (a, b, p, resid, rss))
    print("  p=1 comparison a=%.10f  b=%.10f  implied N*|Δ|→ b/(4√a)=%.6f" % (a1, b1, pref_p1))
    print(
        "  implied pref b(1-2^{-p})/(2√a)=%.6f  so N*|Δ| ~ pref · N^{%.3f}"
        % (pref, 1.0 - p)
    )
    print(
        "  linear s=c0+c1 N: c0=%.10f  c1=%.6e  |c1|N_max=%.6e  converges=%s"
        % (c0, c1, drift_mass, converges)
    )
    g05 = all(np.isfinite(x) for x in (a, b, p, pref, pref_p1))
    gate(
        "G05 convergence fit finite",
        g05,
        "a=%.6f b=%.6f p=%.3f pref=%.4f" % (a, b, p, pref),
    )

    nstab_holds = nstab < STAB_CUT
    verdict = classify_verdict(nstab_holds, median_ratio, slope_d, converges)
    g06 = verdict in VERDICT_ENUM
    gate("G06 verdict enum frozen", g06, verdict)

    print()
    print("PROOF-ROUTE ASSESSMENT")
    print(
        assessment_paragraph(
            verdict,
            toe,
            han,
            nstab,
            median_ratio,
            shift,
            slope_d,
            slope_s,
            ir_big,
            a,
            b,
            p,
            pref,
        )
    )

    n_pass = sum(1 for _, ok in CHECKS if ok)
    rt = time.time() - t0
    file_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print()
    print(
        "HONEST NOTE: float64 diagnostics of structure; no interval "
        "certificate; SEAM.MMST.TYPEIII.CHARGED.01 stays [O]."
    )
    print("GATES %d/%d" % (n_pass, len(CHECKS)))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha)
    print("runtime %.3f s" % rt)
    return 0 if n_pass == len(CHECKS) else 1


def math_sqrt_pos(value: float) -> float:
    if not np.isfinite(value) or value <= 0.0:
        return float("nan")
    return float(np.sqrt(value))


if __name__ == "__main__":
    sys.exit(main())
