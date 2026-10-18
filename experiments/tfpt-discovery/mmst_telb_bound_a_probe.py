#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mmst_telb_bound_a_probe -- TELB.BOUND.A.01
r"""mmst_telb_bound_a_probe -- TELB.BOUND.A.01

FROZEN SPEC v1 (2026-09-04). EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing; verification/, ledger, papers, website, and
scorecard are untouched. The probe writes only its companion result JSON.

GOAL. Attack bound (A) for the MMST TEL-B lattice remainder,
    sup_N ||R^sm_N||_HS <= 1.85, equivalently sup_N ||R^sm_N||_HS^2 <= 3.4225.
The Hamiltonian, covariance, edge profiles, sawtooth, alpha=1/4 convention,
and four-fold-cover identity are copied from mmst_telb_cover_split_probe.py.

MODEL. MASS=1, NY=8, 16 modes,
    TY = SY/(2j) - SZ/2,
    h(p)_onsite = sin(p) SX + (MASS-cos(p)) SZ,
    P(p) = fermi_covariance(p), with zero modes at p=0 occupied by 1/2.
Let Q=P_bottom-P_top and dP=P(0+)-P(0-)=-Q. With
    saw(p)=1/2-(p mod 2pi)/(2pi), saw(0)=0,
set F(p)=P^sm(p)=P(p)-saw(p)dP.

CORPUS FOURIER CONVENTION AND ALL-M BOUND.
    C_infty(m)=(1/(2pi)) integral_0^{2pi} exp(-i m p) F(p) dp.
For a continuous periodic matrix function, integration by parts gives
    C_infty(m) = -Delta F'/(2pi m^2) + O(m^-3).
Thus the corpus prefactor is ||Delta F'||/(2pi), not
||Delta F'||/(2pi)^2. The latter formula is written in terms of the
derivative with respect to t=p/(2pi): ||Delta(dF/dt)||/(2pi)^2, and is
identical after Delta(dF/dt)=2pi Delta F'. If Delta F'=0, a third
integration by parts gives
    C_infty(m) = -i Delta F''/(2pi m^3) + O(m^-4)
up to the immaterial phase convention, hence K3_th=||Delta F''||/(2pi).
For t=p/(2pi), bounded variation of F_tt gives the all-mode inequality
    ||C_infty(m)|| <= TV_t(F_tt)/(2pi |m|)^3 = K3_TV/|m|^3.
Equivalently TV_t(F_tt)=(2pi)^2 TV_p(F_pp), so
    K3_TV=TV_t/(2pi)^3=TV_p/(2pi).
The jump contributes ||Delta F_pp||=2, hence its leading contribution is
2/(2pi)=1/pi. The remaining variation is the integral of ||F_ppp||_HS.

FOUR-FOLD COVER. For M=4N and d=x-y,
    A_N(d)=(1-i)C_M(d+N)+2C_M(d+2N)+(1+i)C_M(d+3N),
    ||R^sm_N||_HS^2=sum_{d=-(N-1)}^{N-1}(N-|d|)||A_N(d)||_HS^2.
The cut distance is m=N-|d|. The neighbourhood m<=m0 is evaluated
directly in float64. For m>m0, if ||C_infty(k)||<=K3/|k|^3, Poisson
aliasing gives the discrete-cover bound
    ||C_M(k)|| <= K3 sum_{ell in Z}|k+ell M|^-3.
The tail is the resulting finite weighted scalar sum, retaining all three
cover branches and their coefficients. The infinite alias sum is evaluated
with Hurwitz zeta, not truncated.

NUMERICAL CERTIFICATE AND HONEST SCOPE. The derivative and second-derivative
jumps are measured by one-sided polynomial extrapolation with step refinement.
TV_p(F_pp) is evaluated by fourth-order centered differences on three grids,
including the jump norm, Richardson-extrapolated, and enlarged by 1 percent.
This single float64 TV constant replaces the former sampled Fourier envelope:
the BV integration-by-parts inequality then applies to every nonzero integer
m. Fourier coefficients through m=8192 remain only a diagnostic comparison.
The cut neighbourhood and TV constant are numerical; the all-m tail inequality,
Poisson alias sum, and cover weighted sum are analytic once that constant is
accepted. This is not interval arithmetic. The reported verdict is therefore
explicitly BOUND_A_CERTIFIED_NUMERICALLY, never a load-bearing proof.

EDGE-CROSSING LEMMA. In the ordered (top,bottom) zero-mode basis,
    V* h'(0) V = diag(-1,+1),  V* h''(0) V = 0,
and (1-VV*)h'(0)V=0. Thus h_edge(p)=sin(p)diag(-1,+1) to the
reported order: the crossing vectors do not rotate at first order. The
occupied edge projector changes only by the fixed rank-two step dP. Subtracting
saw*dP removes that step, while saw'=-1/(2pi) is the same on both sides.
The smooth bulk projector has one derivative at zero, so F'(0+)=F'(0-).

BERNOULLI-2 FALLBACK. It is required only if the 1.85 margin is thin or a
bound gate fails. Here Delta F'=0 numerically and the m^-3 law already closes
the target with large margin, so subtracting a B2 term would be both
unnecessary and based on a vanishing coefficient. The probe records that it
was not used.

GATES.
G01 dP=-Q within 1e-6 and continuity residual tends linearly to zero.
G02 the 2x2 crossing lemma holds numerically and its reduced derivative jump
    is below 1e-6.
G03 derivative-jump refinement gives ||Delta F'||<1e-6 and the first nonzero
    jump is Delta F'', rank 4.
G04 the three-grid TV refinement is stable and K3_TV>=K3_emp.
G05 M-dependence of the Fourier coefficients is below 1e-6 relative on the
    frozen low-mode comparison window 16<=m<=256. The separate M=65536
    diagnostic extends through m=8192; near-Nyquist relative comparisons
    across unequal grids are not used as an alias diagnostic.
G06 measured ||R^sm_N||^2 is bounded by U_N for N=64..4096.
G07 every U_N and the stable large-N U_infty are below 3.4225.
G08 bulk gap after removing the two edge bands is at least 0.99.
G09 verdict enum is frozen.

VERDICTS:
    BOUND_A_CERTIFIED_NUMERICALLY
    BOUND_A_NEEDS_BERNOULLI2
    BOUND_A_FAILS
    INCONCLUSIVE
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
from scipy.special import zeta

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

MASS = 1.0
NY = 8
TRANSVERSE_DIMENSION = 2 * NY
ALPHA = 0.25
ZERO_CUT = 1.0e-11
TARGET_NORM = 1.85
TARGET_NORM2 = TARGET_NORM**2
CUT_M0 = 16
SIZES = (64, 128, 256, 512, 1024, 2048, 4096)
FOURIER_GRIDS = (16384, 32768, 65536)
FOURIER_TEST_MAX = 8192
TV_GRIDS = (2048, 4096, 8192)
TV_SAFETY_FACTOR = 1.01

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2

VERDICT_ENUM = (
    "BOUND_A_CERTIFIED_NUMERICALLY",
    "BOUND_A_NEEDS_BERNOULLI2",
    "BOUND_A_FAILS",
    "INCONCLUSIVE",
)
CHECKS: list[tuple[str, bool, str]] = []


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
Q_OPERATOR = BOTTOM_PROJECTION - TOP_PROJECTION
DP_OPERATOR = -Q_OPERATOR


def saw_scalar(momentum: float) -> float:
    reduced = float(np.mod(momentum, 2 * pi))
    if abs(reduced) < 1.0e-12 or abs(reduced - 2 * pi) < 1.0e-12:
        return 0.0
    return 0.5 - reduced / (2 * pi)


def smooth_projector(momentum: float) -> np.ndarray:
    return fermi_covariance(momentum) - saw_scalar(momentum) * DP_OPERATOR


def gate(name: str, passed: bool, detail: str) -> None:
    CHECKS.append((name, bool(passed), detail))
    print("  [%s] %s  %s" % ("PASS" if passed else "FAIL", name, detail))


def one_sided_jumps(step: float) -> tuple[np.ndarray, np.ndarray]:
    """Degree-four one-sided extrapolation of F'(0±), F''(0±)."""
    coordinates = np.arange(1, 6, dtype=float) * step
    vandermonde = np.vander(coordinates, 5, increasing=True)
    plus_values = np.stack(
        [smooth_projector(float(x)).reshape(-1) for x in coordinates]
    )
    minus_values = np.stack(
        [smooth_projector(float(-x)).reshape(-1) for x in coordinates]
    )
    plus_coefficients = np.linalg.solve(vandermonde, plus_values)
    minus_coefficients = np.linalg.solve(vandermonde, minus_values)
    # minus polynomial is F(-x), hence F'(0-)=-coefficient[1].
    derivative_jump = (plus_coefficients[1] + minus_coefficients[1]).reshape(
        TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION
    )
    second_derivative_jump = (
        2 * plus_coefficients[2] - 2 * minus_coefficients[2]
    ).reshape(TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION)
    return derivative_jump, second_derivative_jump


def crossing_reduction(derivative_jump: np.ndarray) -> dict:
    """Numerically verify the exact first-order two-edge-mode reduction."""
    edge_basis = np.column_stack([TOP_PROFILE, BOTTOM_PROFILE])
    edge_projection = edge_basis @ edge_basis.conj().T
    h_prime_zero = np.kron(np.eye(NY), SX)
    h_second_zero = np.kron(np.eye(NY), SZ)
    effective_velocity = edge_basis.conj().T @ h_prime_zero @ edge_basis
    effective_curvature = edge_basis.conj().T @ h_second_zero @ edge_basis
    bulk_coupling = float(
        np.linalg.norm(
            (np.eye(TRANSVERSE_DIMENSION) - edge_projection)
            @ h_prime_zero
            @ edge_basis
        )
    )
    test_step = 1.0e-4
    effective_plus = (
        edge_basis.conj().T @ strip_hamiltonian(test_step) @ edge_basis
    )
    effective_minus = (
        edge_basis.conj().T @ strip_hamiltonian(-test_step) @ edge_basis
    )
    finite_velocity = (effective_plus - effective_minus) / (2 * test_step)
    target_velocity = np.diag([-1.0, 1.0])
    velocity_residual = float(np.linalg.norm(finite_velocity - target_velocity))
    odd_residual = float(np.linalg.norm(effective_plus + effective_minus))
    reduced_derivative_jump = float(
        np.linalg.norm(edge_basis.conj().T @ derivative_jump @ edge_basis)
    )
    return {
        "basis_order": ["top", "bottom"],
        "effective_velocity_real": effective_velocity.real.tolist(),
        "effective_curvature_real": effective_curvature.real.tolist(),
        "bulk_coupling_norm": bulk_coupling,
        "finite_difference_velocity_residual": velocity_residual,
        "odd_block_residual": odd_residual,
        "reduced_derivative_jump_norm": reduced_derivative_jump,
    }


def second_derivative_total_variation(
    grid_size: int, second_jump_norm: float
) -> dict[str, float]:
    """Polygonal float64 estimate of TV_p(F_pp), including its cut jump.

    Away from the cut saw*dP is affine, hence F_pp=P_pp. The five-point
    centered stencil is fourth order. Centers within two grid cells of the
    cut are omitted; their missing smooth variation is recovered by the
    first-order Richardson extrapolation performed across grids in main().
    """
    spacing = 2 * pi / grid_size
    projector_samples = np.empty(
        (grid_size - 1, TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION),
        dtype=complex,
    )
    for index in range(1, grid_size):
        projector_samples[index - 1] = fermi_covariance(index * spacing)
    second_derivatives = (
        -projector_samples[4:]
        + 16 * projector_samples[3:-1]
        - 30 * projector_samples[2:-2]
        + 16 * projector_samples[1:-3]
        - projector_samples[:-4]
    ) / (12 * spacing**2)
    increments = np.diff(second_derivatives, axis=0)
    smooth_variation = float(
        np.sum(np.linalg.norm(increments.reshape(len(increments), -1), axis=1))
    )
    tv_p = smooth_variation + second_jump_norm
    tv_t = (2 * pi) ** 2 * tv_p
    return {
        "grid_size": grid_size,
        "smooth_variation_p": smooth_variation,
        "jump_variation_p": second_jump_norm,
        "TV_p": tv_p,
        "TV_t": tv_t,
        "K3_grid": tv_t / (2 * pi) ** 3,
    }


def sampled_fourier(grid_size: int) -> np.ndarray:
    samples = np.empty(
        (grid_size, TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION), dtype=complex
    )
    for index in range(grid_size):
        samples[index] = smooth_projector(2 * pi * index / grid_size)
    return np.fft.fft(samples, axis=0) / grid_size


def hs_norms(coefficients: np.ndarray) -> np.ndarray:
    return np.linalg.norm(coefficients.reshape(len(coefficients), -1), axis=1)


def periodic_representative(index: int, period: int) -> int:
    reduced = index % period
    return reduced if reduced <= period // 2 else reduced - period


def alias_sum_inverse_cube(index: int, period: int) -> float:
    """sum_{ell in Z}|index+ell*period|^-3, exactly via Hurwitz zeta."""
    representative = abs(periodic_representative(index, period))
    if representative == 0:
        raise ValueError("zero Fourier mode has no inverse-cube tail bound")
    ratio = representative / period
    return float((zeta(3, ratio) + zeta(3, 1.0 - ratio)) / period**3)


def cover_split(size: int, k3_bound: float) -> dict[str, float]:
    cover_size = 4 * size
    coefficients = sampled_fourier(cover_size)
    cover_weights = ((1.0 - 1.0j), 2.0, (1.0 + 1.0j))
    measured = 0.0
    neighbourhood = 0.0
    measured_tail = 0.0
    tail_bound = 0.0
    for displacement in range(-(size - 1), size):
        multiplicity = size - abs(displacement)
        cut_distance = multiplicity
        block = np.zeros(
            (TRANSVERSE_DIMENSION, TRANSVERSE_DIMENSION), dtype=complex
        )
        scalar_block_bound = 0.0
        for branch, weight in enumerate(cover_weights, start=1):
            fourier_index = displacement + branch * size
            block += weight * coefficients[fourier_index % cover_size]
            if cut_distance > CUT_M0:
                scalar_block_bound += (
                    abs(weight)
                    * k3_bound
                    * alias_sum_inverse_cube(fourier_index, cover_size)
                )
        contribution = multiplicity * float(np.vdot(block, block).real)
        measured += contribution
        if cut_distance <= CUT_M0:
            neighbourhood += contribution
        else:
            measured_tail += contribution
            tail_bound += multiplicity * scalar_block_bound**2
    return {
        "N": size,
        "neighbourhood": neighbourhood,
        "measured_tail": measured_tail,
        "tail_bound": tail_bound,
        "U_N": neighbourhood + tail_bound,
        "measured_rsm2": measured,
        "measured_rsm_norm": float(np.sqrt(measured)),
    }


def spectral_gaps() -> tuple[float, dict[str, float]]:
    momenta = np.linspace(-pi, pi, 8193)
    bulk_gap = float("inf")
    edge_outside: dict[str, float] = {}
    spectra = []
    for momentum in momenta:
        absolute = np.sort(np.abs(np.linalg.eigvalsh(strip_hamiltonian(momentum))))
        spectra.append((float(momentum), float(absolute[0])))
        bulk_gap = min(bulk_gap, float(absolute[2]))
    for delta in (pi / 16, pi / 8, pi / 4, pi / 2):
        edge_outside["pi/%d" % round(pi / delta)] = min(
            gap for momentum, gap in spectra if abs(momentum) >= delta
        )
    return bulk_gap, edge_outside


def main() -> int:
    started = time.time()
    print("=" * 78)
    print("mmst_telb_bound_a_probe -- TELB.BOUND.A.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("=" * 78)

    epsilon_rows = []
    for epsilon in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
        residual = float(
            np.linalg.norm(smooth_projector(epsilon) - smooth_projector(-epsilon))
        )
        epsilon_rows.append({"epsilon": epsilon, "continuity_residual": residual})
    numerical_dp = fermi_covariance(1e-7) - fermi_covariance(-1e-7)
    dp_residual = float(np.linalg.norm(numerical_dp + Q_OPERATOR))
    continuity_ratio = epsilon_rows[-1]["continuity_residual"] / (
        2 * epsilon_rows[-1]["epsilon"]
    )
    g01 = dp_residual < 1e-6 and epsilon_rows[-1]["continuity_residual"] < 1e-6
    gate(
        "G01 jump removal and continuity",
        g01,
        "||dP_num+Q||=%.3e, ||F(e)-F(-e)||@1e-7=%.3e, slope=%.6f"
        % (dp_residual, epsilon_rows[-1]["continuity_residual"], continuity_ratio),
    )

    jump_rows = []
    final_derivative_jump = None
    final_second_jump = None
    for step in (1e-2, 5e-3, 2e-3, 1e-3, 5e-4):
        derivative_jump, second_jump = one_sided_jumps(step)
        jump_rows.append(
            {
                "step": step,
                "derivative_jump_norm": float(np.linalg.norm(derivative_jump)),
                "second_derivative_jump_norm": float(np.linalg.norm(second_jump)),
            }
        )
        final_derivative_jump = derivative_jump
        final_second_jump = second_jump
    assert final_derivative_jump is not None and final_second_jump is not None
    derivative_singular = np.linalg.svd(final_derivative_jump, compute_uv=False)
    second_singular = np.linalg.svd(final_second_jump, compute_uv=False)
    derivative_rank = int(np.sum(derivative_singular > 1e-6))
    second_rank = int(np.sum(second_singular > 1e-4))
    derivative_jump_norm = float(np.linalg.norm(final_derivative_jump))
    second_jump_norm = float(np.linalg.norm(final_second_jump))
    k2_th_corpus = derivative_jump_norm / (2 * pi)
    k2_th_normalized_literal = derivative_jump_norm / (2 * pi) ** 2
    k3_th = second_jump_norm / (2 * pi)

    crossing = crossing_reduction(final_derivative_jump)
    crossing_ok = (
        crossing["bulk_coupling_norm"] < 1e-12
        and crossing["finite_difference_velocity_residual"] < 1e-7
        and crossing["odd_block_residual"] < 1e-12
        and crossing["reduced_derivative_jump_norm"] < 1e-6
    )
    print()
    print("2x2 CROSSING LEMMA (basis: top,bottom)")
    print("  V*h'(0)V = %s" % crossing["effective_velocity_real"])
    print("  V*h''(0)V = %s" % crossing["effective_curvature_real"])
    gate(
        "G02 two-by-two crossing lemma",
        crossing_ok,
        "bulk coupling=%.3e, velocity residual=%.3e, odd residual=%.3e, "
        "reduced ||dF'||=%.3e"
        % (
            crossing["bulk_coupling_norm"],
            crossing["finite_difference_velocity_residual"],
            crossing["odd_block_residual"],
            crossing["reduced_derivative_jump_norm"],
        ),
    )
    jump_ok = derivative_jump_norm < 1e-6 and second_rank == 4
    gate(
        "G03 first nonzero derivative jump",
        jump_ok,
        "rank(dF')=%d ||dF'||=%.3e; rank(d2F)=%d ||d2F||=%.9f; "
        "leading K3=||d2F||/(2pi)=%.9f"
        % (
            derivative_rank,
            derivative_jump_norm,
            second_rank,
            second_jump_norm,
            k3_th,
        ),
    )

    fourier_coefficients = {}
    fourier_norms = {}
    for grid_size in FOURIER_GRIDS:
        coefficients = sampled_fourier(grid_size)
        fourier_coefficients[grid_size] = coefficients
        fourier_norms[grid_size] = hs_norms(coefficients)
    reference_norms = fourier_norms[FOURIER_GRIDS[-1]]
    tested_indices = np.arange(CUT_M0, FOURIER_TEST_MAX + 1)
    scaled_cube = tested_indices**3 * reference_norms[tested_indices]
    k3_emp = float(np.max(scaled_cube))
    k3_emp_index = int(tested_indices[int(np.argmax(scaled_cube))])
    tv_rows = [
        second_derivative_total_variation(grid_size, second_jump_norm)
        for grid_size in TV_GRIDS
    ]
    tv_p_richardson = 2 * tv_rows[-1]["TV_p"] - tv_rows[-2]["TV_p"]
    tv_p_bound = TV_SAFETY_FACTOR * tv_p_richardson
    tv_t_bound = (2 * pi) ** 2 * tv_p_bound
    k3_tv = tv_t_bound / (2 * pi) ** 3
    tv_last_relative_change = abs(
        tv_rows[-1]["TV_p"] - tv_rows[-2]["TV_p"]
    ) / tv_rows[-1]["TV_p"]
    tv_ok = tv_last_relative_change < 0.01 and k3_tv >= k3_emp
    print()
    print("TV(F_tt) REFINEMENT")
    for row in tv_rows:
        print(
            "  grid=%5d  TV_p=%.9f  TV_t=%.9f  K3=%.9f"
            % (row["grid_size"], row["TV_p"], row["TV_t"], row["K3_grid"])
        )
    gate(
        "G04 all-mode TV Fourier bound",
        tv_ok,
        "TV_p_bound=%.9f TV_t_bound=%.9f; K3_TV=%.9f >= "
        "K3_emp=%.9f@%d"
        % (
            tv_p_bound,
            tv_t_bound,
            k3_tv,
            k3_emp,
            k3_emp_index,
        ),
    )
    k3_bound = k3_tv

    alias_rows = []
    alias_relative_max = 0.0
    for grid_a, grid_b in zip(FOURIER_GRIDS, FOURIER_GRIDS[1:]):
        comparison_max = 256
        indices = np.arange(CUT_M0, comparison_max + 1)
        differences = np.linalg.norm(
            (
                fourier_coefficients[grid_a][indices]
                - fourier_coefficients[grid_b][indices]
            ).reshape(len(indices), -1),
            axis=1,
        )
        relative = differences / np.maximum(
            fourier_norms[grid_b][indices], 1e-30
        )
        maximum = float(np.max(relative))
        alias_relative_max = max(alias_relative_max, maximum)
        alias_rows.append(
            {"M_a": grid_a, "M_b": grid_b, "max_relative_difference": maximum}
        )
    alias_ok = alias_relative_max < 1e-6
    gate(
        "G05 Fourier-grid alias diagnostic",
        alias_ok,
        "max relative M-dependence=%.3e (m=%d..256)"
        % (alias_relative_max, CUT_M0),
    )

    table = []
    print()
    print("  N      neighbourhood       tail_bound              U_N       measured_Rsm2")
    for size in SIZES:
        row = cover_split(size, k3_bound)
        table.append(row)
        print(
            "%5d  %.12f  %.12e  %.12f  %.12f"
            % (
                size,
                row["neighbourhood"],
                row["tail_bound"],
                row["U_N"],
                row["measured_rsm2"],
            )
        )
    measured_bounded = all(
        row["measured_rsm2"] <= row["U_N"] + 1e-12 for row in table
    )
    gate(
        "G06 bound dominates measurements",
        measured_bounded,
        "minimum slack=%.3e"
        % min(row["U_N"] - row["measured_rsm2"] for row in table),
    )
    u_infinity = float(np.mean([row["U_N"] for row in table[-2:]]))
    u_max = max(row["U_N"] for row in table)
    bound_closed = u_max < TARGET_NORM2 and u_infinity < TARGET_NORM2
    gate(
        "G07 bound-A target",
        bound_closed,
        "max U_N=%.12f, U_inf=%.12f, target=%.4f, norm bound=%.9f"
        % (u_max, u_infinity, TARGET_NORM2, np.sqrt(max(u_max, u_infinity))),
    )

    bulk_gap, edge_outside = spectral_gaps()
    bulk_ok = bulk_gap >= 0.99
    gate(
        "G08 bulk spectral gap",
        bulk_ok,
        "non-edge gap=%.12f; edge |p|>=pi/2 gap=%.12f"
        % (bulk_gap, edge_outside["pi/2"]),
    )

    bernoulli2_used = False
    all_bound_inputs_ok = (
        g01
        and crossing_ok
        and jump_ok
        and tv_ok
        and alias_ok
        and measured_bounded
        and bound_closed
        and bulk_ok
    )
    if all_bound_inputs_ok:
        verdict = "BOUND_A_CERTIFIED_NUMERICALLY"
    elif g01 and not bound_closed:
        verdict = "BOUND_A_NEEDS_BERNOULLI2"
    elif not measured_bounded:
        verdict = "BOUND_A_FAILS"
    else:
        verdict = "INCONCLUSIVE"
    gate("G09 frozen verdict enum", verdict in VERDICT_ENUM, verdict)

    runtime = time.time() - started
    file_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "contract": "TELB.BOUND.A.01",
        "spec_sha": SPEC_SHA,
        "file_sha256": file_sha,
        "verdict": verdict,
        "gates": {
            name: {"passed": passed, "detail": detail}
            for name, passed, detail in CHECKS
        },
        "continuity_refinement": epsilon_rows,
        "derivative_refinement": jump_rows,
        "crossing_reduction_2x2": crossing,
        "derivative_jump_explanation": (
            "In the (top,bottom) edge basis h'(0)=diag(-1,+1) and has zero "
            "bulk coupling, so the crossing vectors do not rotate at first order. "
            "The occupied edge contribution is only the fixed dP step; saw*dP "
            "removes it, and saw' is identical on both sides."
        ),
        "jumps": {
            "derivative_rank_threshold_1e-6": derivative_rank,
            "derivative_jump_norm": derivative_jump_norm,
            "second_derivative_rank_threshold_1e-4": second_rank,
            "second_derivative_jump_norm": second_jump_norm,
        },
        "fourier": {
            "convention": "C(m)=(1/2pi) integral exp(-imp)F(p)dp",
            "K2_th_corpus": k2_th_corpus,
            "K2_th_normalized_coordinate_literal": k2_th_normalized_literal,
            "K3_th": k3_th,
            "K3_emp": k3_emp,
            "K3_emp_at_m": k3_emp_index,
            "K3_TV_all_m": k3_tv,
            "m0": CUT_M0,
            "empirical_diagnostic_through_m": FOURIER_TEST_MAX,
            "grid_alias_checks": alias_rows,
        },
        "total_variation": {
            "coordinate_note": (
                "t=p/(2pi); TV_t(F_tt)=(2pi)^2 TV_p(F_pp), "
                "K3_TV=TV_t/(2pi)^3=TV_p/(2pi)"
            ),
            "refinement": tv_rows,
            "TV_p_richardson": tv_p_richardson,
            "safety_factor": TV_SAFETY_FACTOR,
            "TV_p_bound": tv_p_bound,
            "TV_t_bound": tv_t_bound,
            "K3_TV_all_m": k3_tv,
        },
        "table": table,
        "U_infinity_numeric": u_infinity,
        "bulk_gap_non_edge_bands": bulk_gap,
        "edge_gap_outside_neighbourhoods": edge_outside,
        "bernoulli2": {
            "used": bernoulli2_used,
            "reason": "not needed: derivative jump vanishes and m^-3 tail closes target",
            "change_in_rsm2": 0.0,
        },
        "analytic_steps": [
            "BV integration by parts: ||C(m)||<=TV_t(F_tt)/(2pi|m|)^3 for all m!=0",
            "Poisson alias bound for the M-point Fourier coefficient",
            "four-fold-cover weighted HS identity",
            "Hurwitz-zeta evaluation of the infinite alias sum",
        ],
        "honest_note": (
            "float64, not interval arithmetic; finite cut is computed numerically; "
            "the all-m tail inequality is analytic conditional on the numerically "
            "Richardson-extrapolated TV constant; U_infinity is numerical stabilization"
        ),
        "weakest_step": (
            "the float64 finite-difference TV estimate and its 1-percent Richardson "
            "safety factor are not an interval-certified upper integral"
        ),
        "runtime_s": runtime,
    }
    output = Path(__file__).with_name("mmst_telb_bound_a_result.json")
    with output.open("w") as handle:
        json.dump(result, handle, indent=1)

    passed_count = sum(passed for _, passed, _ in CHECKS)
    print()
    print(
        "HONEST NOTE: float64, not interval arithmetic; all-m BV tail is analytic "
        "conditional on the numerically extrapolated TV constant."
    )
    print("BERNOULLI2 used: %s" % bernoulli2_used)
    print("GATES %d/%d" % (passed_count, len(CHECKS)))
    print("VERDICT: %s" % verdict)
    print("SPEC_SHA %s" % SPEC_SHA)
    print("FILE_SHA256 %s" % file_sha)
    print("runtime %.3f s" % runtime)
    print("wrote %s" % output)
    return 0 if passed_count == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
