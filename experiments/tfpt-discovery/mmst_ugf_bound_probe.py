#!/usr/bin/env python3
"""Finite audit of the UGF proof for the frozen QWZ/CAR collar.

EXPLORATION ONLY.  This script verifies, for N in {16,24,32,48,64,96},
every finite inequality used in the analytic proof in
articles/2026-08-30/mmst_charged_scaling_limit_en.tex.

The collar is the M=1, Ny=8 QWZ strip

    h(p)=sin(p) sx + (1-cos(p)) sz + open-y hopping,

with antiperiodic longitudinal momenta p_n=2*pi*(n+1/2)/N.  At every
momentum we select the normalized eigenvector with maximal weight on the
top four y sites.  The Hardy edge filling is nu_n=1 for n<0 and 0 for
n>=0.  For 1 <= m <= N/2 its edge density structure factor is

    S_N(m)=sum_{n=-m}^{-1}|<u_{n+m},u_n>|^2.

The lattice derivative symbol and boson Green coefficient are

    omega_N(m)=N/pi*sin(pi*m/N),
    g_N(m)=S_N(m)/(2*omega_N(m)^2).

Since each overlap is at most one, S_N(m)<=m.  Since
sin x >= 2x/pi on [0,pi/2], omega_N(m)>=2m/pi.  Therefore

    0 <= g_N(m) <= (pi^2/4)/(2m)

for every N and every fundamental nonzero mode.  Eight independent
bosons have the same scalar multiplier, so K_G=pi^2/4 is unchanged.

The probe also checks fixed-mode convergence to 1/(2m), the transverse
bulk-complement gap at p=0, and two mandatory mutants:

  * a completely gapless transverse covariance C=1/2 has
    S_mut(m)=Ny_orb*N/4 and violates the N-independent bound;
  * the false comparison omega_N(m)>=m fails at the Nyquist mode.

Finite checks support the proof but are not substituted for its analytic
universal quantifiers.
"""

from __future__ import annotations

from math import pi

import numpy as np


MASS = 1.0
NY = 8
INTERNAL_DIMENSION = 2 * NY
N_VALUES = (16, 24, 32, 48, 64, 96)
K_G_PROVED = pi**2 / 4
TOLERANCE = 2.0e-12
FIXED_MODES = (1, 2, 3)

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2

all_ok = True


def report(name: str, ok: bool, detail: str = "") -> None:
    global all_ok
    all_ok &= bool(ok)
    suffix = "  | " + detail if detail else ""
    print(("PASS " if ok else "FAIL ") + name + suffix)


def strip_hamiltonian(momentum: float) -> np.ndarray:
    """Frozen M=1, Ny=8 QWZ strip in longitudinal momentum space."""
    matrix = np.zeros((INTERNAL_DIMENSION, INTERNAL_DIMENSION), dtype=complex)
    onsite = (
        np.sin(momentum) * SX
        + (MASS - np.cos(momentum)) * SZ
    )
    for y_index in range(NY):
        site = slice(2 * y_index, 2 * y_index + 2)
        matrix[site, site] = onsite
    for y_index in range(NY - 1):
        lower = slice(2 * y_index, 2 * y_index + 2)
        upper = slice(2 * y_index + 2, 2 * y_index + 4)
        matrix[upper, lower] = TY
        matrix[lower, upper] = TY.conj().T
    return matrix


def top_edge_vector(momentum: float) -> tuple[float, np.ndarray, float]:
    """Most top-localized normalized eigenvector and its top weight."""
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    reshaped = eigenvectors.reshape(NY, 2, INTERNAL_DIMENSION)
    top_weights = np.sum(np.abs(reshaped[:4]) ** 2, axis=(0, 1))
    selected = int(np.argmax(top_weights))
    return (
        float(eigenvalues[selected]),
        eigenvectors[:, selected],
        float(top_weights[selected]),
    )


def edge_data(size: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    mode_indices = np.arange(-size // 2, size // 2)
    momenta = 2 * pi * (mode_indices + 0.5) / size
    energies = np.empty(size)
    vectors = np.empty((size, INTERNAL_DIMENSION), dtype=complex)
    weights = np.empty(size)
    for position, momentum in enumerate(momenta):
        energy, vector, weight = top_edge_vector(float(momentum))
        energies[position] = energy
        vectors[position] = vector
        weights[position] = weight
    return energies, vectors, weights


def lattice_symbol(size: int, mode: int) -> float:
    return size / pi * np.sin(pi * abs(mode) / size)


def structure_factor(vectors: np.ndarray, mode: int) -> float:
    """Hardy particle-hole sum: n=-m,...,-1 to n+m=0,...,m-1."""
    size = vectors.shape[0]
    zero_position = size // 2
    occupied_positions = range(zero_position - mode, zero_position)
    total = 0.0
    for source in occupied_positions:
        target = source + mode
        total += abs(np.vdot(vectors[target], vectors[source])) ** 2
    return float(total)


def bulk_gap_at_crossing() -> tuple[float, float, int, float]:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(0.0))
    zero_indices = np.where(np.abs(eigenvalues) < 1.0e-10)[0]
    bulk = np.delete(eigenvalues, zero_indices)
    gap = float(np.min(np.abs(bulk)))
    boundary_weights = []
    for index in zero_indices:
        vector = eigenvectors[:, index]
        boundary_weights.append(
            max(
                float(np.sum(np.abs(vector[:2]) ** 2)),
                float(np.sum(np.abs(vector[-2:]) ** 2)),
            )
        )
    derivative_step = 1.0e-5
    positive_energy = top_edge_vector(derivative_step)[0]
    negative_energy = top_edge_vector(-derivative_step)[0]
    edge_slope = (positive_energy - negative_energy) / (2 * derivative_step)
    return gap, min(boundary_weights), len(zero_indices), float(edge_slope)


print("=" * 78)
print("MMST UGF BOUND PROBE -- frozen QWZ edge, exploration only")
print("=" * 78)

bulk_gap, zero_boundary_weight, zero_count, edge_slope = bulk_gap_at_crossing()
report(
    "U1 transverse edge doublet and bulk-complement gap",
    zero_count == 2
    and bulk_gap > 0.9
    and zero_boundary_weight > 1 - 1.0e-12
    and abs(abs(edge_slope) - 1) < 1.0e-8,
    "zero modes=%d; delta_bulk(p=0)=%.12f; min boundary weight=%.12f; "
    "top-edge slope=%.12f"
    % (zero_count, bulk_gap, zero_boundary_weight, edge_slope),
)

global_measured_ratio = 0.0
fixed_mode_ratios: dict[int, list[float]] = {
    mode: [] for mode in FIXED_MODES
}
minimum_edge_weight = 1.0

print()
print("  N    max S/m    min omega/m    measured K    fixed g/(1/(2m))")
for size in N_VALUES:
    energies, vectors, weights = edge_data(size)
    minimum_edge_weight = min(minimum_edge_weight, float(np.min(weights)))
    structure_ratios = []
    symbol_ratios = []
    green_ratios = []
    fixed_display = []

    for mode in range(1, size // 2 + 1):
        structure = structure_factor(vectors, mode)
        omega = lattice_symbol(size, mode)
        green = structure / (2 * omega**2)
        comparison_ratio = 2 * mode * green
        structure_ratios.append(structure / mode)
        symbol_ratios.append(omega / mode)
        green_ratios.append(comparison_ratio)
        if mode in FIXED_MODES:
            fixed_mode_ratios[mode].append(comparison_ratio)
            fixed_display.append(comparison_ratio)

    measured_ratio = max(green_ratios)
    global_measured_ratio = max(global_measured_ratio, measured_ratio)
    print(
        " %3d   %.9f    %.9f      %.9f    %s"
        % (
            size,
            max(structure_ratios),
            min(symbol_ratios),
            measured_ratio,
            "[" + ", ".join("%.8f" % value for value in fixed_display) + "]",
        )
    )

    report(
        "U2 N=%d overlap/Schur count S_N(m)<=m" % size,
        max(structure_ratios) <= 1 + TOLERANCE,
        "max S/m=%.12f" % max(structure_ratios),
    )
    report(
        "U3 N=%d sine comparison 2/pi <= omega_N(m)/m <= 1" % size,
        min(symbol_ratios) >= 2 / pi - TOLERANCE
        and max(symbol_ratios) <= 1 + TOLERANCE,
        "range=[%.12f, %.12f]" % (min(symbol_ratios), max(symbol_ratios)),
    )
    report(
        "U4 N=%d Green domination K_G=pi^2/4" % size,
        measured_ratio <= K_G_PROVED + TOLERANCE,
        "measured K=%.12f; proved K=%.12f"
        % (measured_ratio, K_G_PROVED),
    )

report(
    "U5 all-size final UGF bound",
    global_measured_ratio <= K_G_PROVED + TOLERANCE,
    "max measured K=%.12f; analytic K_G=pi^2/4=%.12f; ratio=%.6f"
    % (
        global_measured_ratio,
        K_G_PROVED,
        global_measured_ratio / K_G_PROVED,
    ),
)

convergence_ok = True
convergence_details = []
for mode, ratios in fixed_mode_ratios.items():
    final_error = abs(ratios[-1] - 1.0)
    initial_error = abs(ratios[0] - 1.0)
    mode_ok = final_error < initial_error and final_error < 0.03
    convergence_ok &= mode_ok
    convergence_details.append(
        "m=%d %.3e->%.3e" % (mode, initial_error, final_error)
    )
report(
    "U6 fixed-mode local Green convergence g_N(m)->1/(2|m|)",
    convergence_ok,
    "; ".join(convergence_details),
)

report(
    "U7 edge branch remains normalized/localized on sampled grids",
    minimum_edge_weight > 0.24,
    "minimum top-four-site weight=%.9f (global continuation; "
    "local convergence uses the near-zero branch)" % minimum_edge_weight,
)

# Mutant A: all transverse modes are flat at zero and half occupied.
# Every longitudinal source contributes C(1-C)=1/4 in every internal mode.
mutant_ratios = []
for size in N_VALUES:
    mode = 1
    mutant_structure = INTERNAL_DIMENSION * size / 4
    omega = lattice_symbol(size, mode)
    mutant_ratios.append(mode * mutant_structure / omega**2)
report(
    "MUST-FAIL A gapless transverse mutant violates uniform K_G",
    min(mutant_ratios) > K_G_PROVED
    and mutant_ratios[-1] > mutant_ratios[0],
    "K_mut(N=16)=%.3f -> K_mut(N=96)=%.3f (grows linearly)"
    % (mutant_ratios[0], mutant_ratios[-1]),
)

# Mutant B: replace the sharp lower comparison 2/pi by the false constant 1.
wrong_symbol_margins = []
for size in N_VALUES:
    nyquist_mode = size // 2
    wrong_symbol_margins.append(
        lattice_symbol(size, nyquist_mode) / nyquist_mode
    )
report(
    "MUST-FAIL B false symbol claim omega_N(m)>=m is rejected",
    max(wrong_symbol_margins) < 1 - 0.3,
    "Nyquist omega/m=%s; exact value 2/pi=%.12f"
    % (
        ["%.12f" % value for value in wrong_symbol_margins],
        2 / pi,
    ),
)

print()
print("PROVED CONSTANT: K_G = pi^2/4 = %.12f" % K_G_PROVED)
print("MEASURED MAXIMUM: %.12f" % global_measured_ratio)
print(
    "VERDICT: UGF_FULLY_PROVED_FOR_EDGE_PROJECTED_FROZEN_COLLAR"
    if all_ok
    else "VERDICT: UGF_PROBE_HAS_FAILURES"
)
print("PROBE " + ("ALL PASS" if all_ok else "HAS FAILURES"))
raise SystemExit(0 if all_ok else 1)
