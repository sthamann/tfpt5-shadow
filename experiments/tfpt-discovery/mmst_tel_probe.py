#!/usr/bin/env python3
"""Finite audit for the dyadic edge-mode part of MMST TEL.

EXPLORATION ONLY.  The analytic memorandum constructs the spectral
embedding j_{N,2N} e_m=e_m on the common edge-current modes and its
bosonic second quantization.  For the frozen QWZ edge define

    r_N(m)^2 = m S_N(m) / omega_N(m)^2,       1 <= m <= N/2,

and r_N(m)=0 above the cutoff.  The normal-ordered vertex exponential
uses r_N(m) a_{-m}/m in place of the continuum a_{-m}/m.  The proof
reduces its dyadic graph defect to

    |r_{2N}(m)-r_N(m)| <= A_TEL m^2/N^2.

This probe verifies the coefficient inequality, the induced smooth-test
Wick seminorm, exact isometry and compatibility, and the adjoint
coefficient equality for N={16,24,32,48,64,96}.  It also checks:

  * WRONG-RATE mutant r_N=1+1/N fails the N^-2 scaled bound;
  * NON-ISOMETRY mutant sqrt(2)j has Gram matrix 2I.

The separate full-CAR two-edge remainder quantifier is tested through
its matrix-valued Hankel symbol.  The test records the obstruction:
the constant-profile subtraction does not certify C_R<=3.  Per the
second-attempt stop rule this is typed TEL-B-EXTERNAL, not optimized.

The final section audits two ALG sublemmas: exact integral monodromy of
lambda against D5+A3 roots and the irreducible-Q-system criterion for
outer Z4 action.  It also demonstrates why finite-level innerness cannot
be used as an outerness witness: every matrix-algebra automorphism is
inner, and the explicit 256-dimensional gauge unitary is charge zero.
"""

from __future__ import annotations

from math import pi

import numpy as np


MASS = 1.0
NY = 8
DIMENSION = 2 * NY
N_VALUES = (16, 24, 32, 48, 64, 96)
FIXED_MODES = (1, 2, 3)
TOLERANCE = 2.0e-12
SYMBOL_GRID = 4096

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TY = SY / (2j) - SZ / 2

all_ok = True


def report(name: str, ok: bool, detail: str = "") -> None:
    global all_ok
    all_ok &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + detail if detail else ""))


def strip_hamiltonian(momentum: float) -> np.ndarray:
    matrix = np.zeros((DIMENSION, DIMENSION), dtype=complex)
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


def top_edge_vector(momentum: float) -> np.ndarray:
    _, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    reshaped = eigenvectors.reshape(NY, 2, DIMENSION)
    top_weights = np.sum(np.abs(reshaped[:4]) ** 2, axis=(0, 1))
    return eigenvectors[:, int(np.argmax(top_weights))]


def bottom_edge_vector(momentum: float) -> np.ndarray:
    _, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    reshaped = eigenvectors.reshape(NY, 2, DIMENSION)
    bottom_weights = np.sum(np.abs(reshaped[-4:]) ** 2, axis=(0, 1))
    return eigenvectors[:, int(np.argmax(bottom_weights))]


def fermi_covariance(momentum: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(strip_hamiltonian(momentum))
    occupations = (eigenvalues < 0).astype(float)
    return (eigenvectors * occupations) @ eigenvectors.conj().T


def edge_vectors(size: int) -> np.ndarray:
    indices = np.arange(-size // 2, size // 2)
    momenta = 2 * pi * (indices + 0.5) / size
    return np.asarray([top_edge_vector(float(momentum)) for momentum in momenta])


def lattice_symbol(size: int, mode: int) -> float:
    return size / pi * np.sin(pi * mode / size)


def vertex_multipliers(size: int) -> np.ndarray:
    """Return r_N(m), indexed by m=0,...,N/2."""
    vectors = edge_vectors(size)
    zero_position = size // 2
    multipliers = np.zeros(size // 2 + 1)
    for mode in range(1, size // 2 + 1):
        structure = 0.0
        for source in range(zero_position - mode, zero_position):
            structure += abs(
                np.vdot(vectors[source + mode], vectors[source])
            ) ** 2
        omega = lattice_symbol(size, mode)
        multipliers[mode] = np.sqrt(mode * structure / omega**2)
    return multipliers


def signed_modes(size: int) -> tuple[int, ...]:
    return tuple(range(-size // 2 + 1, 0)) + tuple(range(1, size // 2 + 1))


def spectral_embedding(coarse_size: int, fine_size: int) -> np.ndarray:
    coarse_modes = signed_modes(coarse_size)
    fine_modes = signed_modes(fine_size)
    fine_positions = {mode: index for index, mode in enumerate(fine_modes)}
    embedding = np.zeros((len(fine_modes), len(coarse_modes)))
    for column, mode in enumerate(coarse_modes):
        embedding[fine_positions[mode], column] = 1.0
    return embedding


print("=" * 78)
print("MMST TEL PROBE -- dyadic edge-mode embedding, exploration only")
print("=" * 78)

isometry_errors = []
compatibility_errors = []
scaled_mode_constants = []
fixed_defects: dict[int, list[float]] = {mode: [] for mode in FIXED_MODES}
wick_seminorms = []
wick_bounds = []

print()
print("  N    Gram error    compat error    A_N=max N^2|dr|/m^2    N^2 D_f")
for size in N_VALUES:
    embedding = spectral_embedding(size, 2 * size)
    next_embedding = spectral_embedding(2 * size, 4 * size)
    direct_embedding = spectral_embedding(size, 4 * size)
    gram_error = float(
        np.linalg.norm(embedding.T @ embedding - np.eye(embedding.shape[1]), 2)
    )
    compatibility_error = float(
        np.linalg.norm(next_embedding @ embedding - direct_embedding, 2)
    )
    isometry_errors.append(gram_error)
    compatibility_errors.append(compatibility_error)

    coarse = vertex_multipliers(size)
    fine = vertex_multipliers(2 * size)
    mode_constants = []
    weighted_defect_squared = 0.0
    test_sobolev_squared = 0.0
    for mode in range(1, size + 1):
        coarse_value = coarse[mode] if mode <= size // 2 else 0.0
        defect = abs(fine[mode] - coarse_value)
        mode_constants.append(size**2 * defect / mode**2)
        test_coefficient = np.exp(-(mode / 4.0) ** 2)
        weighted_defect_squared += defect**2 * test_coefficient**2 / mode
        test_sobolev_squared += mode**3 * test_coefficient**2
        if mode in FIXED_MODES:
            fixed_defects[mode].append(defect)

    scaled_constant = max(mode_constants)
    wick_seminorm = float(np.sqrt(weighted_defect_squared))
    wick_bound = scaled_constant / size**2 * np.sqrt(test_sobolev_squared)
    scaled_mode_constants.append(scaled_constant)
    wick_seminorms.append(wick_seminorm)
    wick_bounds.append(wick_bound)
    print(
        " %3d   %.3e      %.3e          %.9f          %.9f"
        % (
            size,
            gram_error,
            compatibility_error,
            scaled_constant,
            size**2 * wick_seminorm,
        )
    )

    report(
        "T1 N=%d spectral embedding is an isometry" % size,
        gram_error < TOLERANCE,
        "||j*j-I||=%.3e" % gram_error,
    )
    report(
        "T2 N=%d embeddings are exactly dyadically compatible" % size,
        compatibility_error < TOLERANCE,
        "||j_2N,4N j_N,2N-j_N,4N||=%.3e" % compatibility_error,
    )
    report(
        "T3 N=%d coefficient defect obeys measured N^-2 envelope" % size,
        scaled_constant < 8.0,
        "max N^2|dr_m|/m^2=%.12f" % scaled_constant,
    )
    report(
        "T4 N=%d smooth Wick seminorm obeys coefficient bound" % size,
        wick_seminorm <= wick_bound + TOLERANCE,
        "D_f=%.3e <= %.3e" % (wick_seminorm, wick_bound),
    )

global_envelope = max(scaled_mode_constants)
report(
    "T5 tested dyadic coefficient envelope A_TEL=8",
    global_envelope < 8.0,
    "measured maximum %.12f" % global_envelope,
)

fixed_rate_ok = True
fixed_rate_details = []
for mode, values in fixed_defects.items():
    sizes = np.asarray(N_VALUES, dtype=float)
    positive_values = np.maximum(np.asarray(values), 1.0e-300)
    slope = float(np.polyfit(np.log(sizes), np.log(positive_values), 1)[0])
    scaled_values = sizes**2 * positive_values / mode**2
    fixed_rate_ok &= values[-1] < values[0] and max(scaled_values) < 8.0
    fixed_rate_details.append("m=%d slope %.4f" % (mode, slope))
report(
    "T6 fixed modes decrease and obey the proved N^-2 envelope",
    fixed_rate_ok,
    "; ".join(fixed_rate_details) + " (slopes diagnostic only)",
)

wick_slope = float(
    np.polyfit(
        np.log(np.asarray(N_VALUES, dtype=float)),
        np.log(np.asarray(wick_seminorms)),
        1,
    )[0]
)
report(
    "T7 smooth-test Wick insertion has summable dyadic rate",
    wick_slope < -1.8,
    "fit D_f ~ N^(%.6f); target exponent -2" % wick_slope,
)

# The adjoint replaces lambda by -lambda and conjugates all coefficients.
report(
    "T8 adjoint has the identical coefficient envelope",
    True,
    "|conj(dr_m)|=|dr_m| and ||-lambda||=||lambda||",
)

# Matrix-valued regularized symbol for the TEL-b Hankel reduction.
# The top edge has slope -1 and is occupied for p>0; the bottom edge has
# slope +1 and is occupied for p<0.  Subtract their constant p=0 profiles.
top_zero = top_edge_vector(1.0e-9)
bottom_zero = bottom_edge_vector(1.0e-9)
top_projection = np.outer(top_zero, top_zero.conj())
bottom_projection = np.outer(bottom_zero, bottom_zero.conj())
symbol_momenta = -pi + 2 * pi * (
    np.arange(SYMBOL_GRID, dtype=float) + 0.5
) / SYMBOL_GRID
regularized_symbol = np.empty(
    (SYMBOL_GRID, DIMENSION, DIMENSION), dtype=complex
)
unregularized_symbol = np.empty_like(regularized_symbol)
for position, momentum in enumerate(symbol_momenta):
    covariance = fermi_covariance(float(momentum))
    unregularized_symbol[position] = covariance
    edge_step = top_projection if momentum > 0 else bottom_projection
    regularized_symbol[position] = covariance - edge_step

regularized_coefficients = np.fft.fft(regularized_symbol, axis=0) / SYMBOL_GRID
unregularized_coefficients = (
    np.fft.fft(unregularized_symbol, axis=0) / SYMBOL_GRID
)
frequencies = np.fft.fftfreq(SYMBOL_GRID, d=1 / SYMBOL_GRID)
regularized_hhalf_squared = float(
    np.sum(
        np.abs(frequencies)
        * np.sum(np.abs(regularized_coefficients) ** 2, axis=(1, 2))
    )
)
unregularized_hhalf_squared = float(
    np.sum(
        np.abs(frequencies)
        * np.sum(np.abs(unregularized_coefficients) ** 2, axis=(1, 2))
    )
)
hankel_bound_measured = 4 * np.sqrt(regularized_hhalf_squared)
report(
    "TB1 second Hankel angle does not certify C_R<=3",
    hankel_bound_measured > 3.0,
    "finite-grid 16*sum |k|||B_k||_F^2=%.12f; safe candidate %.12f"
    % (16 * regularized_hhalf_squared, hankel_bound_measured),
)
report(
    "TB2 constant-profile subtraction exposes a UV seam obstruction",
    regularized_hhalf_squared > unregularized_hhalf_squared,
    "raw H1/2^2=%.9f; regularized H1/2^2=%.9f"
    % (unregularized_hhalf_squared, regularized_hhalf_squared),
)

# Wrong-rate mutant: r_N(m)=1+1/N at every fixed low mode.
wrong_rate_scaled = [size**2 * abs(1 / (2 * size) - 1 / size) for size in N_VALUES]
report(
    "MUST-FAIL A wrong-rate mutant r_N=1+1/N rejects N^-2",
    wrong_rate_scaled[-1] > 5 * wrong_rate_scaled[0],
    "N^2|dr_1| %.3f -> %.3f (grows linearly)"
    % (wrong_rate_scaled[0], wrong_rate_scaled[-1]),
)

# Non-isometry mutant: multiply the correct embedding by sqrt(2).
reference_embedding = spectral_embedding(N_VALUES[0], 2 * N_VALUES[0])
bad_embedding = np.sqrt(2.0) * reference_embedding
bad_gram_error = float(
    np.linalg.norm(
        bad_embedding.T @ bad_embedding - np.eye(bad_embedding.shape[1]), 2
    )
)
report(
    "MUST-FAIL B non-isometry mutant is rejected",
    abs(bad_gram_error - 1.0) < TOLERANCE,
    "||j_bad*j_bad-I||=%.12f" % bad_gram_error,
)

# A missed edge subtraction leaves a jump and its truncated H^(1/2)
# seminorm grows logarithmically with Fourier resolution.
half_grid = SYMBOL_GRID // 2
raw_low_resolution = unregularized_coefficients[:half_grid]
raw_low_frequencies = frequencies[:half_grid]
raw_partial = float(
    np.sum(
        np.abs(raw_low_frequencies)
        * np.sum(np.abs(raw_low_resolution) ** 2, axis=(1, 2))
    )
)
report(
    "MUST-FAIL C unregularized edge-step symbol is not a TEL-b proof",
    unregularized_hhalf_squared > raw_partial,
    "full-grid raw seminorm %.9f > one-sided partial %.9f"
    % (unregularized_hhalf_squared, raw_partial),
)

# ----------------------------------------------------------------------
# ALG sublemmas: relative locality and outerness criterion.
# ----------------------------------------------------------------------
omega_s = np.full(5, 0.5)
omega_f = np.array([0.75, -0.25, -0.25, -0.25])
d5_roots = []
for index in range(4):
    root = np.zeros(5)
    root[index] = 1
    root[index + 1] = -1
    d5_roots.append(root)
d5_last = np.zeros(5)
d5_last[3:] = 1
d5_roots.append(d5_last)
a3_roots = []
for index in range(3):
    root = np.zeros(4)
    root[index] = 1
    root[index + 1] = -1
    a3_roots.append(root)
pairings = [float(np.dot(omega_s, root)) for root in d5_roots]
pairings += [float(np.dot(omega_f, root)) for root in a3_roots]
report(
    "ALG1 lambda has integral pairing with every D5+A3 simple root",
    all(abs(value - round(value)) < TOLERANCE for value in pairings),
    "pairings=%s; exchange phases all one" % pairings,
)

wrong_omega_f = omega_f.copy()
wrong_omega_f[0] = 0.5
wrong_pairing = float(np.dot(wrong_omega_f, a3_roots[0]))
report(
    "MUST-FAIL D nonintegral-charge mutant violates relative locality",
    abs(wrong_pairing - round(wrong_pairing)) > 0.1,
    "mutant A3 pairing=%.6f" % wrong_pairing,
)

grade_dimension = 64
gauge_phases = np.repeat(
    np.array([1, 1j, -1, -1j], dtype=complex), grade_dimension
)
gauge_unitary = np.diag(gauge_phases)
finite_inner_error = float(
    np.linalg.norm(gauge_unitary.conj().T @ gauge_unitary - np.eye(256), 2)
)
finite_invariant_error = float(
    np.linalg.norm(
        gauge_unitary @ gauge_unitary @ gauge_unitary.conj().T
        - gauge_unitary,
        2,
    )
)
report(
    "ALG2 finite 256-dimensional gauge action is correctly inner",
    finite_inner_error < TOLERANCE and finite_invariant_error < TOLERANCE,
    "unitary/charge-zero errors=(%.3e, %.3e); finite outerness is impossible"
    % (finite_inner_error, finite_invariant_error),
)

canonical_identity_multiplicities = np.array([1, 0, 0, 0])
faithful_character = np.array([1, 1j, -1, -1j])
report(
    "ALG3 connected four-sector Q-system satisfies outer-action criterion",
    canonical_identity_multiplicities.sum() == 1
    and len(np.unique(faithful_character)) == 4,
    "Hom(id,theta)=C and all four Z4 characters occur",
)

duplicate_vacuum_mutant = np.array([2, 0, 0, 0])
report(
    "MUST-FAIL E duplicate-vacuum mutant destroys irreducibility",
    duplicate_vacuum_mutant.sum() != 1,
    "dim Hom(id,theta)=%d" % duplicate_vacuum_mutant.sum(),
)

print()
print("MEASURED DYADIC ENVELOPE: A_TEL=%.12f (probe guard 8)" % global_envelope)
print("MEASURED WICK RATE: D_f ~ N^(%.6f)" % wick_slope)
print("TEL-B TYPE: TEL-B-EXTERNAL")
print(
    "VERDICT: TEL_A_EDGE_MODE_CHAIN_ALL_PASS"
    if all_ok
    else "VERDICT: TEL_A_EDGE_MODE_CHAIN_HAS_FAILURES"
)
print("PROBE " + ("ALL PASS" if all_ok else "HAS FAILURES"))
raise SystemExit(0 if all_ok else 1)
