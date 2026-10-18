#!/usr/bin/env python3
"""Third TEL-b attempt: certified-finite plus dyadic-tail diagnostic.

EXPLORATION ONLY.  This probe places the full-CAR remainder R_N in the
untwisted longitudinal Fourier basis and tests the proposed estimate

    ||R_{2N} - J_{N,2N} R_N J_{N,2N}^*||_HS <= D/N^2.

The embedding J preserves the integer longitudinal mode label and every
one of the 16 transverse/orbital components.  No large embedding matrix
is formed: the cross term is read from the matching principal submatrix.

If the N^-2 envelope fails, the geometric tail theorem cannot be used,
regardless of finite-value certification.  In that case the probe emits
TAIL-TELESCOPING-FAILS and treats the requested certified enclosure as
blocked before certification, rather than presenting high-precision
floating point values as rigorous intervals.
"""

from __future__ import annotations

from math import pi

import numpy as np
from scipy.special import digamma, polygamma


MASS = 1.0
NY = 8
TRANSVERSE_DIMENSION = 2 * NY
ALPHA = 0.25
ZERO_CUT = 1.0e-11
FINITE_SIZES = (16, 24, 32, 48, 64, 96)
DYADIC_PAIRS = ((16, 32), (32, 64), (64, 128), (96, 192))
TOLERANCE = 2.0e-10

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


print("=" * 78)
print("MMST TEL-B CERTIFIED-TAIL ATTEMPT -- exploration only")
print("=" * 78)

cache: dict[int, np.ndarray] = {}
for size in sorted(set(FINITE_SIZES) | {value for pair in DYADIC_PAIRS for value in pair}):
    cache[size] = remainder_in_mode_basis(size)

print()
print("FINITE VALUES (double precision diagnostic; not interval certificates)")
finite_norms: dict[int, float] = {}
for size in FINITE_SIZES:
    finite_norms[size] = hs_norm(cache[size])
    print("  N=%3d  ||R_N||_HS=%.12f" % (size, finite_norms[size]))
report(
    "F1 mode-basis construction reproduces the established finite values",
    abs(finite_norms[16] - 2.09252848) < 2.0e-8
    and abs(finite_norms[96] - 2.105079358) < 2.0e-9,
    "endpoints=(%.12f, %.12f)" % (finite_norms[16], finite_norms[96]),
)

print()
print("DYADIC EMBEDDING DEFECTS")
print("  N->2N      low-mode defect       dilation n->2n defect")
dyadic_defects: list[tuple[int, float, float]] = []
dilation_defects: list[tuple[int, float, float]] = []
for coarse_size, fine_size in DYADIC_PAIRS:
    coarse = cache[coarse_size]
    fine = cache[fine_size]
    coarse_modes = np.arange(-coarse_size // 2, coarse_size // 2)
    fine_modes = np.arange(-fine_size // 2, fine_size // 2)
    fine_mode_positions = {
        int(mode): position for position, mode in enumerate(fine_modes)
    }
    selected = []
    for mode in coarse_modes:
        position = fine_mode_positions[int(mode)]
        selected.extend(
            range(
                position * TRANSVERSE_DIMENSION,
                (position + 1) * TRANSVERSE_DIMENSION,
            )
        )
    matching_fine_corner = fine[np.ix_(selected, selected)]
    defect_squared = (
        hs_norm(fine) ** 2
        + hs_norm(coarse) ** 2
        - 2 * float(np.vdot(matching_fine_corner, coarse).real)
    )
    defect = float(np.sqrt(max(defect_squared, 0.0)))
    scaled = coarse_size**2 * defect
    dyadic_defects.append((coarse_size, defect, scaled))

    dilation_selected = []
    for mode in coarse_modes:
        doubled_mode = 2 * int(mode)
        position = fine_mode_positions[doubled_mode]
        dilation_selected.extend(
            range(
                position * TRANSVERSE_DIMENSION,
                (position + 1) * TRANSVERSE_DIMENSION,
            )
        )
    dilation_corner = fine[np.ix_(dilation_selected, dilation_selected)]
    dilation_defect_squared = (
        hs_norm(fine) ** 2
        + hs_norm(coarse) ** 2
        - 2 * float(np.vdot(dilation_corner, coarse).real)
    )
    dilation_defect = float(np.sqrt(max(dilation_defect_squared, 0.0)))
    dilation_scaled = coarse_size**2 * dilation_defect
    dilation_defects.append((coarse_size, dilation_defect, dilation_scaled))
    print(
        "  %3d->%3d       %.12f          %.12f"
        % (coarse_size, fine_size, defect, dilation_defect)
    )

scaled_values = np.asarray([entry[2] for entry in dyadic_defects])
defect_values = np.asarray([entry[1] for entry in dyadic_defects])
tail_rate_holds = bool(
    np.max(scaled_values) < 100.0
    and defect_values[-1] < defect_values[0] / 10
)
report(
    "F2 proposed TEL-a-type N^-2 remainder envelope",
    not tail_rate_holds,
    "correctly rejected; scaled range [%.6f, %.6f]"
    % (float(np.min(scaled_values)), float(np.max(scaled_values))),
)

dilation_values = np.asarray([entry[1] for entry in dilation_defects])
dilation_scaled_values = np.asarray([entry[2] for entry in dilation_defects])
dilation_rate_holds = bool(
    np.max(dilation_scaled_values) < 100.0
    and dilation_values[-1] < dilation_values[0] / 10
)
report(
    "F2b physical-momentum dilation n->2n has an N^-2 envelope",
    not dilation_rate_holds,
    "correctly rejected; defects %.6f -> %.6f"
    % (float(dilation_values[0]), float(dilation_values[-1])),
)

norm_increments = []
for coarse_size, fine_size in DYADIC_PAIRS:
    norm_increments.append(
        abs(hs_norm(cache[fine_size]) - hs_norm(cache[coarse_size]))
    )
report(
    "F3 norm increments are bounded by embedding defects",
    all(
        increment <= defect + TOLERANCE
        for increment, (_, defect, _) in zip(norm_increments, dyadic_defects)
    ),
    "max norm increment %.6e; min embedding defect %.6e"
    % (max(norm_increments), min(defect_values)),
)
print(
    "  scalar norm increments:",
    ["%.12f" % value for value in norm_increments],
)
print(
    "  N*scalar increments:",
    [
        "%.9f" % (pair[0] * increment)
        for pair, increment in zip(DYADIC_PAIRS, norm_increments)
    ],
)

# A synthetic N^-1 defect violates the geometric 4^{-k} tail assumed by
# an N^-2 certificate.
mutant_scaled = np.asarray([size for size, _, _ in dyadic_defects], dtype=float)
report(
    "MUST-FAIL rate mutant D_N=1/N breaks an N^-2 tail certificate",
    mutant_scaled[-1] > mutant_scaled[0],
    "N^2 D_N grows %.1f -> %.1f"
    % (mutant_scaled[0], mutant_scaled[-1]),
)

print()
if tail_rate_holds:
    first_size, first_defect, _ = dyadic_defects[-1]
    geometric_tail = first_defect / (1 - 0.25)
    print(
        "TAIL CERTIFICATE CANDIDATE: ||R_%d|| + %.12f"
        % (first_size, geometric_tail)
    )
    verdict = "TAIL-TELESCOPING-PASSES"
else:
    print("CERTIFICATION BLOCKED: the prerequisite N^-2 tail estimate is false.")
    print("No mpmath value is mislabeled as a rigorous interval certificate.")
    verdict = "TAIL-TELESCOPING-FAILS"

print("VERDICT: " + verdict)
print("PROBE " + ("ALL PASS" if all_ok else "HAS FAILURES"))
if __name__ == "__main__":
    raise SystemExit(0 if all_ok else 1)
