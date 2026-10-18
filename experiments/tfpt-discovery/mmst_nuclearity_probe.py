#!/usr/bin/env python3
"""Uniform CAR nuclearity audit for the frozen QWZ collar.

EXPLORATION ONLY.  This probe computes the singular values requested for
the Buchholz--Wichmann map, but it deliberately separates two statements:

  (A) uniform CAR nuclearity of the full finite collar (proved here);
  (B) the first line of (5.26), with its *prescribed* edge-generated
      projector P_gen (not implied by nuclearity alone).

For a quasifree Dirac/CAR system, D'Antoni--Hollands, Proposition IV.1,
gives

    ||Theta_beta||_p
      <= det(1 + (S* S)^(p/2))^(1/p)
       = prod_k (1 + s_k(S)^p)^(1/p),
    S = 2 chi_O exp(-beta h) P_+.

Thus, for p=1 and t_k the singular values of
T = exp(-beta h) P_+ chi_O,

    nu(beta,O) <= prod_k (1 + 2 t_k).

The collar contains eight complex copies (sixteen Majoranas), so the
right side is raised to the eighth power.  This is the fermionic
product, in contrast with the inverse determinant occurring for bosons.
The original phase-space criterion is Buchholz--Wichmann; the relation
to split/compactness conditions is developed by
Buchholz--D'Antoni--Longo.

The positive one-particle scaling Hamiltonian is

    h_N = (N/(2*pi)) H_N | Ran(P_+).

An explicit all-N trace bound follows directly from the frozen strip.
In the sigma_x basis,

    H(p)^2 = sin(p)^2 + diag(C(p) C(p)^*, C(p)^* C(p)),
    C(p) = (1-cos(p)) I - S_y,       ||S_y|| = 1.

For |p| <= pi/2 all eight positive energies obey E_j(p) >= |sin p|;
for |p| >= pi/2, s_min(C) >= -cos p and hence E_j(p) >= 1.
Using NS momenta p=2*pi*(n+1/2)/N and sin x >= 2x/pi gives

    ||T_N||_1 <= Tr(P_+ exp(-beta h_N)) <= C_beta,
    C_beta =
      16 exp(-beta/pi)/(1-exp(-2 beta/pi))
      + 64 exp(-8 beta/pi),                         (N >= 16)

for every localization projection chi_O.  Consequently

    log nu_N(beta,O) <= 16 C_beta

uniformly in N.  This proof is independent of the numerical plateau.

The quarter-circle spectra are also compared with the two-channel
continuum Hardy operator.  This comparison is numerical evidence, not a
trace-norm theorem: the memorandum's proved UGF estimate concerns the
bosonized current covariance, and its local Sobolev quadratic-form
convergence does not by itself imply trace-norm convergence of the full
fermionic heat-localization operator.

References:
  D. Buchholz and E. H. Wichmann, CMP 106 (1986), 321--344.
  D. Buchholz, C. D'Antoni and R. Longo, CMP 129 (1990), 115--138.
  C. D'Antoni and S. Hollands, CMP 261 (2006), 133--159,
  arXiv:math-ph/0106028, especially Proposition IV.1.
"""

from __future__ import annotations

from math import pi

import numpy as np


MASS = 1.0
NY = 8
INTERNAL_DIMENSION = 2 * NY
COMPLEX_COPIES = 8
N_VALUES = (16, 24, 32, 48, 64, 96)
BETA_VALUES = (0.5, 1.0, 2.0)
QUARTER_CIRCLE_FRACTION = 0.25
CONTINUUM_MODE_CUTOFF = 256
TOLERANCE = 2.0e-11
PLATEAU_RELATIVE_TOLERANCE = 0.04

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
    """Frozen M=1, Ny=8 QWZ strip at one longitudinal momentum."""
    matrix = np.zeros(
        (INTERNAL_DIMENSION, INTERNAL_DIMENSION), dtype=complex
    )
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


def localization_singular_values(
    size: int,
    beta: float,
    interval_fraction: float = QUARTER_CIRCLE_FRACTION,
    gapless_mutant: bool = False,
) -> np.ndarray:
    """Singular values of exp(-beta h_N) P_+ chi_O for one complex copy."""
    interval_size = max(1, int(round(interval_fraction * size)))
    interval_sites = np.arange(interval_size)
    mode_indices = np.arange(-size // 2, size // 2)
    momenta = 2 * pi * (mode_indices + 0.5) / size

    # Rows are positive-energy eigenmodes; columns are local site-spin
    # vectors.  This is the momentum representation of T_N.
    localized_map = np.zeros(
        (NY * size, INTERNAL_DIMENSION * interval_size), dtype=complex
    )
    for momentum_index, momentum in enumerate(momenta):
        eigenvalues, eigenvectors = np.linalg.eigh(
            strip_hamiltonian(float(momentum))
        )
        positive_indices = np.where(eigenvalues > 0)[0]
        if len(positive_indices) != NY:
            raise AssertionError("NS grid must have eight positive modes")

        if gapless_mutant:
            damping = np.ones(NY)
        else:
            scaled_energies = (
                size / (2 * pi) * eigenvalues[positive_indices]
            )
            damping = np.exp(-beta * scaled_energies)

        phases = (
            np.exp(-1j * momentum * interval_sites) / np.sqrt(size)
        )
        block = (
            damping[:, None, None]
            * eigenvectors[:, positive_indices].conj().T[:, :, None]
            * phases[None, None, :]
        )
        row = slice(NY * momentum_index, NY * (momentum_index + 1))
        localized_map[row, :] = block.reshape(
            NY, INTERNAL_DIMENSION * interval_size
        )

    return np.linalg.svd(localized_map, compute_uv=False)


def continuum_hardy_singular_values(
    beta: float,
    interval_fraction: float = QUARTER_CIRCLE_FRACTION,
) -> np.ndarray:
    """Two-channel continuum Hardy singular values at a stable cutoff."""
    positive_modes = np.arange(CONTINUUM_MODE_CUTOFF) + 0.5
    damping = np.exp(-beta * positive_modes)
    differences = np.subtract.outer(positive_modes, positive_modes)

    compression = np.empty(
        (CONTINUUM_MODE_CUTOFF, CONTINUUM_MODE_CUTOFF), dtype=complex
    )
    diagonal = differences == 0
    compression[diagonal] = interval_fraction
    compression[~diagonal] = (
        np.exp(
            2j * pi * interval_fraction * differences[~diagonal]
        )
        - 1
    ) / (2j * pi * differences[~diagonal])

    gram_matrix = (
        damping[:, None] * compression * damping[None, :]
    )
    eigenvalues = np.linalg.eigvalsh(gram_matrix)
    one_channel = np.sqrt(np.maximum(eigenvalues, 0))[::-1]
    return np.repeat(one_channel, 2)


def proved_trace_constant(beta: float) -> float:
    """Explicit all-N trace constant C_beta from the docstring proof."""
    central_momenta = (
        16
        * np.exp(-beta / pi)
        / (1 - np.exp(-2 * beta / pi))
    )
    # For beta >= 1/2, N exp(-beta N/(2 pi)) decreases on N >= 16.
    outer_momenta = 64 * np.exp(-8 * beta / pi)
    return float(central_momenta + outer_momenta)


def log_nuclearity_bound(singular_values: np.ndarray) -> float:
    """Eight-copy D'Antoni--Hollands product bound."""
    return float(
        COMPLEX_COPIES * np.sum(np.log1p(2 * singular_values))
    )


print("=" * 88)
print("MMST CAR NUCLEARITY PROBE -- full frozen collar, exploration only")
print("=" * 88)

# Check the pointwise spectral inequalities used in the analytic bound.
minimum_central_margin = float("inf")
minimum_outer_margin = float("inf")
for size in N_VALUES:
    for mode_index in range(-size // 2, size // 2):
        momentum = 2 * pi * (mode_index + 0.5) / size
        positive = np.linalg.eigvalsh(strip_hamiltonian(momentum))[NY:]
        if abs(momentum) <= pi / 2:
            minimum_central_margin = min(
                minimum_central_margin,
                float(np.min(positive) - abs(np.sin(momentum))),
            )
        else:
            minimum_outer_margin = min(
                minimum_outer_margin,
                float(np.min(positive) - 1),
            )

report(
    "N1 frozen-strip pointwise spectral lower bounds",
    minimum_central_margin >= -TOLERANCE
    and minimum_outer_margin >= -TOLERANCE,
    "central E-|sin p| margin=%.3e; outer E-1 margin=%.3e"
    % (minimum_central_margin, minimum_outer_margin),
)

print()
print(
    " beta   N    ||T_N||_1       max s_k       log nu_8       "
    "first six singular values"
)
print("-" * 88)

spectra: dict[tuple[float, int], np.ndarray] = {}
trace_norms: dict[float, list[float]] = {
    beta: [] for beta in BETA_VALUES
}
log_indices: dict[float, list[float]] = {
    beta: [] for beta in BETA_VALUES
}

for beta in BETA_VALUES:
    trace_constant = proved_trace_constant(beta)
    for size in N_VALUES:
        singular_values = localization_singular_values(size, beta)
        spectra[(beta, size)] = singular_values
        trace_norm = float(np.sum(singular_values))
        log_index = log_nuclearity_bound(singular_values)
        trace_norms[beta].append(trace_norm)
        log_indices[beta].append(log_index)
        print(
            " %4.1f  %3d   %.12f   %.12f   %.12f   %s"
            % (
                beta,
                size,
                trace_norm,
                singular_values[0],
                log_index,
                "["
                + ", ".join(
                    "%.6e" % value for value in singular_values[:6]
                )
                + "]",
            )
        )

        report(
            "N2 beta=%.1f N=%d analytic trace domination" % (beta, size),
            trace_norm <= trace_constant + TOLERANCE,
            "measured %.12f <= C_beta %.12f"
            % (trace_norm, trace_constant),
        )
        report(
            "N3 beta=%.1f N=%d fermionic product domination"
            % (beta, size),
            log_index <= 16 * trace_constant + TOLERANCE,
            "measured log nu %.12f <= 16 C_beta %.12f"
            % (log_index, 16 * trace_constant),
        )

print()
print("Continuum plateau comparison (two chiral boundary channels)")
for beta in BETA_VALUES:
    continuum = continuum_hardy_singular_values(beta)
    continuum_trace = float(np.sum(continuum))
    continuum_log_index = log_nuclearity_bound(continuum)
    finite_trace = trace_norms[beta][-1]
    finite_log_index = log_indices[beta][-1]
    trace_relative_error = abs(finite_trace - continuum_trace) / continuum_trace
    log_relative_error = (
        abs(finite_log_index - continuum_log_index)
        / continuum_log_index
    )
    monotone_to_plateau = all(
        later <= earlier + TOLERANCE
        for earlier, later in zip(
            trace_norms[beta], trace_norms[beta][1:]
        )
    )
    report(
        "N4 beta=%.1f N=96 continuum plateau" % beta,
        monotone_to_plateau
        and trace_relative_error < PLATEAU_RELATIVE_TOLERANCE
        and log_relative_error < PLATEAU_RELATIVE_TOLERANCE,
        "trace %.12f -> %.12f (rel %.3e); "
        "log nu %.12f -> %.12f (rel %.3e)"
        % (
            finite_trace,
            continuum_trace,
            trace_relative_error,
            finite_log_index,
            continuum_log_index,
            log_relative_error,
        ),
    )

print()
print("Explicit uniform constants")
for beta in BETA_VALUES:
    trace_constant = proved_trace_constant(beta)
    print(
        " beta=%.1f: C_beta=%.12f; log F_beta=16 C_beta=%.12f; "
        "measured max log nu=%.12f"
        % (
            beta,
            trace_constant,
            16 * trace_constant,
            max(log_indices[beta]),
        )
    )

# Mutant A: remove all energy damping while retaining the positive-energy
# polarization.  Since s_k <= 1 and ||P_+ chi_O||_2^2 = 2N for a quarter
# circle, ||P_+ chi_O||_1 >= 2N and uniformity is impossible.
gapless_trace_norms = [
    float(
        np.sum(
            localization_singular_values(
                size, BETA_VALUES[0], gapless_mutant=True
            )
        )
    )
    for size in N_VALUES
]
report(
    "MUST-FAIL A gapless mutant loses N-uniformity",
    all(
        value >= 2 * size - TOLERANCE
        for size, value in zip(N_VALUES, gapless_trace_norms)
    )
    and gapless_trace_norms[-1] > 5 * gapless_trace_norms[0],
    "||T||_1 %.12f -> %.12f; linear lower bound 2N"
    % (gapless_trace_norms[0], gapless_trace_norms[-1]),
)

# Mutant B: O is not fixed; enlarge the interval at fixed cutoff.  The
# nuclearity cost must degrade with volume, although the compact circle
# prevents literal divergence once O reaches the whole circle.
growing_fractions = (0.25, 0.5, 0.75, 1.0)
growing_log_indices = [
    log_nuclearity_bound(
        localization_singular_values(
            N_VALUES[-1], 1.0, interval_fraction=fraction
        )
    )
    for fraction in growing_fractions
]
report(
    "MUST-FAIL B growing-interval mutant degrades by volume",
    all(
        later > earlier
        for earlier, later in zip(
            growing_log_indices, growing_log_indices[1:]
        )
    )
    and growing_log_indices[-1] > 2 * growing_log_indices[0],
    "log nu_8 %.12f -> %.12f as |O|/|S1| goes 1/4 -> 1"
    % (growing_log_indices[0], growing_log_indices[-1]),
)

print()
print("LEMMA STATUS: UNIFORM_CAR_NUCLEARITY_PROVED")
print(
    "ALG-EXH LINE 1: NOT CLOSED -- collective compactness does not "
    "identify the prescribed P_gen subspace"
)
print(
    "TRACE-NORM LIMIT: NUMERICALLY SUPPORTED -- not implied by the "
    "existing UGF Sobolev-form theorem"
)
print("PROBE " + ("ALL PASS" if all_ok else "HAS FAILURES"))
if __name__ == "__main__":
    raise SystemExit(0 if all_ok else 1)
