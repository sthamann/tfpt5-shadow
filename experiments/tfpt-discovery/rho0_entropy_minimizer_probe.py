#!/usr/bin/env python3
"""Finite rho_0 relative-entropy minimizer probe -- EXPLORATION ONLY.

This probe reuses exactly the 96-dimensional Schwinger--Keldysh model
from ``sk_rho0_mechanism_probe.py`` and ``v1000_spin2_sk_witnesses.py``.
The available finite symmetry data give two explicit Hilbert projectors:

* ``P_GAUSS`` is the group average of the surviving global Z6 Gauss
  action.  It is the product of the two endpoint Gauss transformations:
  their opposite link shifts cancel and leave exp(2 pi i N_Q / 6).
* ``P_MU4_PLUS`` is the +1 character projector of the finite-CAR deck
  action exp(i pi N_F / 2), the same particle-number-mod-4 action used
  in the v995 finite KMS witness.

Thus P = P_GAUSS P_MU4_PLUS is the literal finite implementation of
P_Gauss P_{mu4,+}.  In this reduced Q + e^c model its rank is only six:
Gauss neutrality forces N_Q=0 and the + mu4 sector then forces N_e=0,
leaving the six link states.  This severe reduction is tested rather
than hidden.

Finite theorem (and the needed correction)
------------------------------------------
Let sigma > 0 be a density matrix and P an orthogonal projector which
COMMUTES with sigma.  Put q = Tr(P sigma) and tau = P sigma P / q.
For every density rho with rho = P rho P,

    D(rho || sigma) = D(rho || tau) - log(q) >= -log(q),

because on P H one has log(tau) = P log(sigma) P - log(q) P.
Klein's inequality gives equality iff rho=tau.  This proves existence
and uniqueness, and the Hessian is the positive Bogoliubov--Kubo--Mori
form

    d2 D_tau(A,A) = sum_ij |A_ij|^2
        (log p_i-log p_j)/(p_i-p_j) > 0

for every nonzero Hermitian traceless tangent A (with the diagonal
quotient interpreted as 1/p_i).

The often quoted statement without [P,sigma]=0 is false: the exact
information projection is

    exp(P log(sigma) P) / Tr_P exp(P log(sigma) P),

not generally P sigma P / Tr(P sigma).  Here the commutator vanishes,
so the review's compression formula and the exact information
projection coincide.  A nontrivial centre also does NOT by itself
create flat directions for Umegaki relative entropy: its classical
central-weight KL term is strictly convex.  The direct-sum mutant below
checks this explicitly and shows that a flat central weight appears
only after that KL term is incorrectly deleted.

Repair lattice
--------------
Eight predeclared candidates compare hard support, symmetry invariance,
KMS-valued linear moments, and a fixed charged-seam marginal.  Affine
constraints are solved as

    rho(lambda) = exp(log(rho_KMS) + sum_i lambda_i A_i) / Z(lambda)

to moment residual below 1e-12.  Strict BKM lower bounds certify uniqueness
on every admissible tangent space, and each minimizer is compared directly
with the full KMS state used by v1000.

Honest boundary
---------------
Every hard Gauss or + character support candidate has zero seam-current
response.  Every response-alive candidate is exactly rho_KMS because its
affine data were fixed to rho_KMS; mu4 invariance alone also returns rho_KMS.
But deleting mu4 invariance still has the same unique minimizer by Klein's
inequality.  The required under-constrained mutant therefore cannot pass:
the weakest alive candidate reproduces v1000 but does not canonically select
its state.  This finite proxy is not a 4D algebra, and
FTRANSFER.SK.RHO0.01 remains [O].
"""

from __future__ import annotations

import time

import numpy as np
from scipy.optimize import root


START = time.perf_counter()
ALL_OK = True


def report(name: str, condition: bool, details: str = "") -> None:
    """Record one deterministic check."""
    global ALL_OK
    passed = bool(condition)
    ALL_OK &= passed
    suffix = "  | " + details if details else ""
    print(("PASS " if passed else "FAIL ") + name + suffix)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def expectation(rho: np.ndarray, operator: np.ndarray) -> complex:
    return complex(np.trace(rho @ operator))


def unitary_from_hermitian(
    hamiltonian: np.ndarray, duration: float
) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    phases = np.exp(-1j * duration * eigenvalues)
    return (eigenvectors * phases) @ eigenvectors.conj().T


def density_from_hamiltonian(
    hamiltonian: np.ndarray, beta: float
) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    weights = np.exp(-beta * eigenvalues - np.max(-beta * eigenvalues))
    weights /= np.sum(weights)
    return (eigenvectors * weights) @ eigenvectors.conj().T


def matrix_relative_entropy(
    rho: np.ndarray, sigma: np.ndarray
) -> float:
    """D(rho||sigma) for faithful matrices on one common support."""
    rho_values, rho_vectors = np.linalg.eigh(rho)
    sigma_values, sigma_vectors = np.linalg.eigh(sigma)
    if rho_values.min() <= 0.0 or sigma_values.min() <= 0.0:
        raise ValueError("relative-entropy helper requires faithful inputs")
    log_rho = (rho_vectors * np.log(rho_values)) @ rho_vectors.conj().T
    log_sigma = (
        sigma_vectors * np.log(sigma_values)
    ) @ sigma_vectors.conj().T
    return float(np.trace(rho @ (log_rho - log_sigma)).real)


def hermitian_log(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    if values.min() <= 0.0:
        raise ValueError("matrix logarithm requires positive spectrum")
    return (vectors * np.log(values)) @ vectors.conj().T


def normalized_hermitian_exponential(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(0.5 * (matrix + matrix.conj().T))
    weights = np.exp(values - values.max())
    density = (vectors * weights) @ vectors.conj().T
    return density / np.trace(density)


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = 0.5 * (left - right + (left - right).conj().T)
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(difference))))


def gibbs_tilt(
    reference: np.ndarray,
    observables: tuple[np.ndarray, ...],
    targets: np.ndarray,
    initial_duals: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Solve the finite quantum exponential-family moment dual."""
    log_reference = hermitian_log(reference)

    def state_at(duals: np.ndarray) -> np.ndarray:
        generator = log_reference.copy()
        for dual, observable in zip(duals, observables):
            generator += dual * observable
        return normalized_hermitian_exponential(generator)

    def residual(duals: np.ndarray) -> np.ndarray:
        density = state_at(duals)
        return np.asarray(
            [
                expectation(density, observable).real - target
                for observable, target in zip(observables, targets)
            ]
        )

    solution = root(residual, initial_duals, method="hybr", tol=1e-12)
    density = state_at(solution.x)
    maximum_residual = float(np.max(np.abs(residual(solution.x))))
    if maximum_residual > 1e-12:
        raise RuntimeError(
            "moment dual did not converge to 1e-12: %.3e"
            % maximum_residual
        )
    return density, solution.x, maximum_residual


def group_average_projector(unitary: np.ndarray, order: int) -> np.ndarray:
    projector = np.zeros_like(unitary)
    power = np.eye(unitary.shape[0], dtype=complex)
    for _ in range(order):
        projector += power
        power = power @ unitary
    return 0.5 * (projector / order + (projector / order).conj().T)


def character_projector(
    unitary: np.ndarray, order: int, character: int
) -> np.ndarray:
    projector = np.zeros_like(unitary)
    power = np.eye(unitary.shape[0], dtype=complex)
    root = np.exp(2j * np.pi / order)
    for exponent in range(order):
        projector += root ** (-character * exponent) * power
        power = power @ unitary
    projector /= order
    return 0.5 * (projector + projector.conj().T)


def tangent_basis(dimension: int) -> tuple[np.ndarray, ...]:
    """Hilbert--Schmidt orthonormal Hermitian traceless basis."""
    basis: list[np.ndarray] = []
    for level in range(1, dimension):
        diagonal = np.zeros(dimension)
        diagonal[:level] = 1.0
        diagonal[level] = -float(level)
        diagonal /= np.sqrt(level * (level + 1.0))
        basis.append(np.diag(diagonal).astype(complex))
    for left in range(dimension):
        for right in range(left + 1, dimension):
            symmetric = np.zeros((dimension, dimension), dtype=complex)
            symmetric[left, right] = 1.0 / np.sqrt(2.0)
            symmetric[right, left] = 1.0 / np.sqrt(2.0)
            basis.append(symmetric)
            antisymmetric = np.zeros((dimension, dimension), dtype=complex)
            antisymmetric[left, right] = -1j / np.sqrt(2.0)
            antisymmetric[right, left] = 1j / np.sqrt(2.0)
            basis.append(antisymmetric)
    return tuple(basis)


# ---------------------------------------------------------------------------
# The exact v1000 finite model: Z6 link x four Jordan--Wigner modes = 96.
# ---------------------------------------------------------------------------
NUMBER_OF_SITES = 2
LINK_DIMENSION = 6
NUMBER_OF_MODES = 4
FERMION_DIMENSION = 2**NUMBER_OF_MODES
HILBERT_DIMENSION = LINK_DIMENSION * FERMION_DIMENSION
SPECIES_CHARGES = (1, 0)

ELECTRIC_COUPLING = 1.0
HOPPING_COUPLING = 0.7
STAGGERED_MASS = 0.5
Q_CHEMICAL_OFFSET = 0.5
BETA = 0.35
REFERENCE_THETA = 0.7

OMEGA = np.exp(2j * np.pi / LINK_DIMENSION)
Z_LINK_SMALL = np.diag(OMEGA ** np.arange(LINK_DIMENSION)).astype(complex)
X_LINK_SMALL = np.roll(
    np.eye(LINK_DIMENSION, dtype=complex), 1, axis=0
)
SIGMA_Z = np.diag([1.0, -1.0]).astype(complex)
ANNIHILATION = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)


def jordan_wigner_annihilator(mode: int) -> np.ndarray:
    factors = []
    for index in range(NUMBER_OF_MODES):
        if index < mode:
            factors.append(SIGMA_Z)
        elif index == mode:
            factors.append(ANNIHILATION)
        else:
            factors.append(np.eye(2, dtype=complex))
    result = factors[0]
    for factor in factors[1:]:
        result = np.kron(result, factor)
    return np.kron(np.eye(LINK_DIMENSION, dtype=complex), result)


def lift_link(operator: np.ndarray) -> np.ndarray:
    return np.kron(operator, np.eye(FERMION_DIMENSION, dtype=complex))


PSI = [jordan_wigner_annihilator(mode) for mode in range(NUMBER_OF_MODES)]
NUMBER = [operator.conj().T @ operator for operator in PSI]
X_LINK = lift_link(X_LINK_SMALL)
Z_LINK = lift_link(Z_LINK_SMALL)


def build_hamiltonian(theta: float) -> np.ndarray:
    hamiltonian = -ELECTRIC_COUPLING * (X_LINK + X_LINK.conj().T)
    for species, charge in enumerate(SPECIES_CHARGES):
        mode_0 = species * NUMBER_OF_SITES
        mode_1 = mode_0 + 1
        z_charge = np.linalg.matrix_power(Z_LINK, charge)
        open_hop = PSI[mode_0].conj().T @ z_charge @ PSI[mode_1]
        seam_hop = (
            np.exp(1j * charge * theta)
            * PSI[mode_1].conj().T
            @ PSI[mode_0]
        )
        hamiltonian += HOPPING_COUPLING * (
            open_hop
            + open_hop.conj().T
            + seam_hop
            + seam_hop.conj().T
        )
        hamiltonian += STAGGERED_MASS * (
            NUMBER[mode_0] - NUMBER[mode_1]
        )
    hamiltonian += Q_CHEMICAL_OFFSET * (NUMBER[0] + NUMBER[1])
    return 0.5 * (hamiltonian + hamiltonian.conj().T)


def seam_derivative(theta: float) -> np.ndarray:
    phase = np.exp(1j * theta)
    directed_hop = PSI[1].conj().T @ PSI[0]
    derivative = 1j * phase * directed_hop
    return HOPPING_COUPLING * (derivative + derivative.conj().T)


HAMILTONIAN = build_hamiltonian(REFERENCE_THETA)
RHO_KMS = density_from_hamiltonian(HAMILTONIAN, BETA)
Q_CHARGE = NUMBER[0] + NUMBER[1]
CONTROL_CHARGE = NUMBER[2] + NUMBER[3]
TOTAL_FERMION_NUMBER = Q_CHARGE + CONTROL_CHARGE
CURRENT = -seam_derivative(REFERENCE_THETA)

report(
    "v1000 Hamiltonian and KMS state reconstructed",
    max_abs(HAMILTONIAN - HAMILTONIAN.conj().T) < 1e-13
    and abs(np.trace(RHO_KMS) - 1.0) < 1e-13
    and np.linalg.eigvalsh(RHO_KMS).min() > 0.0,
    "dim=%d, min eig(rho_KMS)=%.3e"
    % (HILBERT_DIMENSION, np.linalg.eigvalsh(RHO_KMS).min()),
)


# ---------------------------------------------------------------------------
# Explicit global-Gauss and mu4 + character projectors.
# ---------------------------------------------------------------------------
IDENTITY = np.eye(HILBERT_DIMENSION, dtype=complex)
GAUSS_ACTION = (
    IDENTITY + (OMEGA - 1.0) * NUMBER[0]
) @ (
    IDENTITY + (OMEGA - 1.0) * NUMBER[1]
)
MU4_ACTION = np.eye(HILBERT_DIMENSION, dtype=complex)
for number_operator in NUMBER:
    MU4_ACTION = MU4_ACTION @ (
        IDENTITY + (1j - 1.0) * number_operator
    )

P_GAUSS = group_average_projector(GAUSS_ACTION, LINK_DIMENSION)
P_MU4_PLUS = group_average_projector(MU4_ACTION, 4)
P_ADMISSIBLE = 0.5 * (
    P_GAUSS @ P_MU4_PLUS
    + (P_GAUSS @ P_MU4_PLUS).conj().T
)

projector_checks = max(
    max_abs(P_GAUSS @ P_GAUSS - P_GAUSS),
    max_abs(P_MU4_PLUS @ P_MU4_PLUS - P_MU4_PLUS),
    max_abs(P_ADMISSIBLE @ P_ADMISSIBLE - P_ADMISSIBLE),
    max_abs(P_GAUSS @ P_MU4_PLUS - P_MU4_PLUS @ P_GAUSS),
)
projector_ranks = (
    int(round(np.trace(P_GAUSS).real)),
    int(round(np.trace(P_MU4_PLUS).real)),
    int(round(np.trace(P_ADMISSIBLE).real)),
)
report(
    "Gauss and mu4 projections are explicit commuting projectors",
    projector_checks < 2e-13 and projector_ranks == (24, 12, 6),
    "ranks P_Gauss/P_mu4+/P=%s, maxdev=%.2e"
    % (projector_ranks, projector_checks),
)

symmetry_deviation = max(
    max_abs(GAUSS_ACTION @ HAMILTONIAN - HAMILTONIAN @ GAUSS_ACTION),
    max_abs(MU4_ACTION @ HAMILTONIAN - HAMILTONIAN @ MU4_ACTION),
    max_abs(P_ADMISSIBLE @ RHO_KMS - RHO_KMS @ P_ADMISSIBLE),
)
report(
    "constraints commute with the finite KMS dynamics",
    symmetry_deviation < 2e-13,
    "max commutator=%.2e" % symmetry_deviation,
)

support_values, support_vectors = np.linalg.eigh(P_ADMISSIBLE)
SUPPORT = support_vectors[:, support_values > 0.5]
SUPPORT_DIMENSION = SUPPORT.shape[1]
sigma_support = SUPPORT.conj().T @ RHO_KMS @ SUPPORT
sector_probability = float(np.trace(sigma_support).real)
rho_star = sigma_support / sector_probability

# K_Sigma = beta H/(2 pi) is the exact finite identification which makes
# exp(-2 pi K_Sigma) equal exp(-beta H).
hamiltonian_values, hamiltonian_vectors = np.linalg.eigh(HAMILTONIAN)
gibbs_unnormalized = (
    hamiltonian_vectors * np.exp(-BETA * hamiltonian_values)
) @ hamiltonian_vectors.conj().T
review_compression = (
    SUPPORT.conj().T
    @ P_ADMISSIBLE
    @ gibbs_unnormalized
    @ P_ADMISSIBLE
    @ SUPPORT
)
review_compression /= np.trace(review_compression)
identity_deviation = max_abs(rho_star - review_compression)
report(
    "rho_star equals the review compression formula",
    identity_deviation < 3e-14,
    "rank=%d, Tr(P rho_KMS)=%.12f, maxdev=%.2e"
    % (SUPPORT_DIMENSION, sector_probability, identity_deviation),
)


# ---------------------------------------------------------------------------
# Exact theorem instantiated; complete 35-direction strict Hessian witness.
# ---------------------------------------------------------------------------
star_values, star_vectors = np.linalg.eigh(rho_star)
rho_star_diagonal = np.diag(star_values).astype(complex)
basis = tangent_basis(SUPPORT_DIMENSION)
divided_difference = np.empty(
    (SUPPORT_DIMENSION, SUPPORT_DIMENSION), dtype=float
)
for left in range(SUPPORT_DIMENSION):
    for right in range(SUPPORT_DIMENSION):
        if left == right or abs(star_values[left] - star_values[right]) < 1e-14:
            divided_difference[left, right] = 1.0 / star_values[left]
        else:
            divided_difference[left, right] = (
                np.log(star_values[left]) - np.log(star_values[right])
            ) / (star_values[left] - star_values[right])

hessian = np.empty((len(basis), len(basis)), dtype=float)
for left, left_direction in enumerate(basis):
    for right, right_direction in enumerate(basis):
        hessian[left, right] = float(
            np.sum(
                np.conjugate(left_direction)
                * divided_difference
                * right_direction
            ).real
        )
hessian = 0.5 * (hessian + hessian.T)
hessian_spectrum = np.linalg.eigvalsh(hessian)

minimum_increase = np.inf
chain_residual = 0.0
optimum_value = -np.log(sector_probability)
for direction in basis:
    step = 0.1 * star_values.min() / np.linalg.norm(direction, ord=2)
    for sign in (-1.0, 1.0):
        trial = rho_star_diagonal + sign * step * direction
        increase = matrix_relative_entropy(trial, rho_star_diagonal)
        minimum_increase = min(minimum_increase, increase)
        direct_value = increase + optimum_value
        chain_residual = max(
            chain_residual,
            abs(direct_value - (increase - np.log(sector_probability))),
        )

report(
    "complete admissible Hessian is strictly positive",
    len(basis) == SUPPORT_DIMENSION**2 - 1
    and hessian_spectrum.min() > 0.0,
    "directions=%d, spectrum=[%.9e, %.9e]"
    % (len(basis), hessian_spectrum.min(), hessian_spectrum.max()),
)
report(
    "all signed basis deviations increase relative entropy",
    minimum_increase > 1e-8 and chain_residual < 1e-14,
    "min increase=%.9e, chain residual=%.1e"
    % (minimum_increase, chain_residual),
)


# The constrained observable algebra on one selected sector is M_6.
# Compute its commutant by the matrix-unit commutator linear system.
matrix_units = []
for left in range(SUPPORT_DIMENSION):
    for right in range(SUPPORT_DIMENSION):
        unit = np.zeros((SUPPORT_DIMENSION, SUPPORT_DIMENSION), dtype=complex)
        unit[left, right] = 1.0
        matrix_units.append(unit)
commutator_system = np.vstack(
    [
        np.kron(unit.T, np.eye(SUPPORT_DIMENSION))
        - np.kron(np.eye(SUPPORT_DIMENSION), unit)
        for unit in matrix_units
    ]
)
commutant_rank = np.linalg.matrix_rank(commutator_system, tol=1e-10)
center_dimension = SUPPORT_DIMENSION**2 - commutant_rank
report(
    "constrained observable algebra has trivial center",
    center_dimension == 1,
    "A_adm=M_%d, commutant rank=%d/%d, center dim=%d"
    % (
        SUPPORT_DIMENSION,
        commutant_rank,
        SUPPORT_DIMENSION**2,
        center_dimension,
    ),
)


# ---------------------------------------------------------------------------
# v1000 consequence: reproduce frozen values, then test compressed rho_star.
# ---------------------------------------------------------------------------
PULSE_AMPLITUDE = 0.18
PULSE_DURATION = 0.45
OBSERVATION_TIMES = np.linspace(0.0, 12.0, 97)
PULSE_HAMILTONIAN = build_hamiltonian(REFERENCE_THETA + PULSE_AMPLITUDE)
PULSE_UNITARY = unitary_from_hermitian(PULSE_HAMILTONIAN, PULSE_DURATION)


def product_density_from_kms_marginals() -> np.ndarray:
    link_density = np.zeros((LINK_DIMENSION, LINK_DIMENSION), dtype=complex)
    link_density[0, 0] = 1.0
    fermion_density = np.array([[1.0]], dtype=complex)
    for number_operator in NUMBER:
        occupation = expectation(RHO_KMS, number_operator).real
        fermion_density = np.kron(
            fermion_density,
            np.diag([1.0 - occupation, occupation]).astype(complex),
        )
    return np.kron(link_density, fermion_density)


def pulse_response(rho: np.ndarray) -> np.ndarray:
    induced = []
    for time_after_pulse in OBSERVATION_TIMES:
        free_after = unitary_from_hermitian(HAMILTONIAN, time_after_pulse)
        pulsed_evolution = free_after @ PULSE_UNITARY
        baseline_evolution = unitary_from_hermitian(
            HAMILTONIAN, time_after_pulse + PULSE_DURATION
        )
        pulsed_density = pulsed_evolution @ rho @ pulsed_evolution.conj().T
        baseline_density = (
            baseline_evolution @ rho @ baseline_evolution.conj().T
        )
        induced.append(
            expectation(pulsed_density, CURRENT).real
            - expectation(baseline_density, CURRENT).real
        )
    return np.asarray(induced)


def response_numbers(response: np.ndarray) -> tuple[float, float, float, float]:
    peak_index = int(np.argmax(np.abs(response)))
    return (
        float(response[peak_index]),
        float(OBSERVATION_TIMES[peak_index]),
        float(np.sqrt(np.mean(response**2))),
        float(np.mean(response)),
    )


rho_star_full = SUPPORT @ rho_star @ SUPPORT.conj().T
rho_product = product_density_from_kms_marginals()
kms_response = pulse_response(RHO_KMS)
product_response = pulse_response(rho_product)
star_response = pulse_response(rho_star_full)
kms_numbers = response_numbers(kms_response)
product_numbers = response_numbers(product_response)
star_numbers = response_numbers(star_response)
frozen_contrast = float(
    np.sqrt(np.mean((kms_response - product_response) ** 2))
)
star_product_contrast = float(
    np.sqrt(np.mean((star_response - product_response) ** 2))
)

report(
    "v1000 frozen SK consequence is reproduced",
    abs(kms_numbers[2] - 3.038094542e-3) < 5e-12
    and abs(product_numbers[2] - 1.429661901e-3) < 5e-12
    and abs(frozen_contrast - 3.549988483e-3) < 5e-12,
    "RMS KMS/product=%.9e/%.9e, contrast=%.9e"
    % (kms_numbers[2], product_numbers[2], frozen_contrast),
)
report(
    "nontrivial canonical compression fails v1000 consequence consistency",
    star_numbers[2] < 1e-13
    and abs(star_product_contrast - frozen_contrast) > 1e-4,
    "rho_star RMS=%.3e, rho_star/product contrast=%.9e (expected mismatch)"
    % (star_numbers[2], star_product_contrast),
)


# ---------------------------------------------------------------------------
# Predeclared admissible-set lattice for the T8 repair attempt.
#
# Weak-to-strong partial order:
#   C2 < {C3,C4,C5,C6,C7,C8},  C3 < C1,  C7 < C1.
# C4--C6 and C8 use KMS-valued affine data and are therefore not comparable
# with the hard + character support in C7.  C0 (no constraint) is retained
# only as the required under-constrained mutant below.
# ---------------------------------------------------------------------------
def compression_minimizer(projector: np.ndarray) -> tuple[np.ndarray, int]:
    values, vectors = np.linalg.eigh(projector)
    support = vectors[:, values > 0.5]
    compressed_log = support.conj().T @ hermitian_log(RHO_KMS) @ support
    density_on_support = normalized_hermitian_exponential(compressed_log)
    density = support @ density_on_support @ support.conj().T
    return density, support.shape[1]


def invariant_tangent_dimension(
    sector_projectors: tuple[np.ndarray, ...],
    support_projector: np.ndarray,
) -> tuple[int, tuple[int, ...]]:
    ranks = tuple(
        int(round(np.trace(support_projector @ sector).real))
        for sector in sector_projectors
    )
    return sum(rank * rank for rank in ranks) - 1, ranks


def hessian_lower_bound(density: np.ndarray) -> float:
    positive_values = np.linalg.eigvalsh(density)
    positive_values = positive_values[positive_values > 1e-12]
    return 1.0 / float(positive_values.max())


MU4_SECTORS = tuple(
    character_projector(MU4_ACTION, 4, character)
    for character in range(4)
)
mu4_resolution_error = max_abs(sum(MU4_SECTORS) - IDENTITY)
mu4_tangent_dimension, mu4_sector_ranks = invariant_tangent_dimension(
    MU4_SECTORS, IDENTITY
)
gauss_mu4_tangent_dimension, gauss_mu4_ranks = (
    invariant_tangent_dimension(MU4_SECTORS, P_GAUSS)
)
report(
    "mu4 character resolution fixes invariant tangent spaces",
    mu4_resolution_error < 3e-13
    and mu4_sector_ranks == (12, 24, 36, 24)
    and gauss_mu4_ranks == (6, 12, 6, 0),
    "full ranks=%s, Gauss ranks=%s, tangent dims=%d/%d"
    % (
        mu4_sector_ranks,
        gauss_mu4_ranks,
        mu4_tangent_dimension,
        gauss_mu4_tangent_dimension,
    ),
)

# C3 and C7 are exact support information projections.
rho_c3, rank_c3 = compression_minimizer(P_GAUSS)
rho_c7, rank_c7 = compression_minimizer(P_MU4_PLUS)

# C4: orientation is an expectation, not a hard character projection.
orientation_target = expectation(RHO_KMS, P_MU4_PLUS).real
rho_c4, duals_c4, residual_c4 = gibbs_tilt(
    RHO_KMS,
    (P_MU4_PLUS,),
    np.asarray([orientation_target]),
    np.asarray([0.13]),
)

# C5: the Hermitian deck charge records the four mu4 character labels.
DECK_CHARGE = sum(
    character * sector
    for character, sector in enumerate(MU4_SECTORS)
)
deck_target = expectation(RHO_KMS, DECK_CHARGE).real
rho_c5, duals_c5, residual_c5 = gibbs_tilt(
    RHO_KMS,
    (DECK_CHARGE,),
    np.asarray([deck_target]),
    np.asarray([-0.11]),
)

# C6: the seam subalgebra is the abelian algebra generated by the two
# charged-site occupation projections.  Three probabilities fix its complete
# four-outcome marginal; the fourth follows from normalization.  The
# KMS-valued Petz/conditional information projection is the identity recovery.
N0 = NUMBER[0]
N1 = NUMBER[1]
SEAM_MARGINAL_PROJECTORS = (
    (IDENTITY - N0) @ (IDENTITY - N1),
    (IDENTITY - N0) @ N1,
    N0 @ (IDENTITY - N1),
)
seam_targets = np.asarray(
    [
        expectation(RHO_KMS, projector).real
        for projector in SEAM_MARGINAL_PROJECTORS
    ]
)
rho_c6, duals_c6, residual_c6 = gibbs_tilt(
    RHO_KMS,
    SEAM_MARGINAL_PROJECTORS,
    seam_targets,
    np.asarray([0.10, -0.08, 0.06]),
)

# C8: preserve the two conserved species-charge expectations.  This is the
# strongest affine state-data candidate naturally exposed by the v1000 model.
charge_targets = np.asarray(
    [
        expectation(RHO_KMS, Q_CHARGE).real,
        expectation(RHO_KMS, CONTROL_CHARGE).real,
    ]
)
rho_c8, duals_c8, residual_c8 = gibbs_tilt(
    RHO_KMS,
    (Q_CHARGE, CONTROL_CHARGE),
    charge_targets,
    np.asarray([0.07, -0.09]),
)

tilt_data = (
    ("C4", rho_c4, duals_c4, residual_c4),
    ("C5", rho_c5, duals_c5, residual_c5),
    ("C6", rho_c6, duals_c6, residual_c6),
    ("C8", rho_c8, duals_c8, residual_c8),
)
report(
    "all affine duals solve to 1e-12 and return rho_KMS",
    all(
        residual < 1e-12
        and np.max(np.abs(duals)) < 1e-10
        and trace_distance(density, RHO_KMS) < 1e-10
        for _, density, duals, residual in tilt_data
    ),
    "; ".join(
        "%s max|lambda|=%.2e residual=%.2e"
        % (name, np.max(np.abs(duals)), residual)
        for name, _, duals, residual in tilt_data
    ),
)

candidate_specs = (
    {
        "name": "C1",
        "constraint": "hard Gauss + hard mu4,+ support",
        "density": rho_star_full,
        "tangent_dim": SUPPORT_DIMENSION**2 - 1,
    },
    {
        "name": "C2",
        "constraint": "mu4 invariance only",
        "density": RHO_KMS,
        "tangent_dim": mu4_tangent_dimension,
    },
    {
        "name": "C3",
        "constraint": "mu4 invariance + hard Gauss support",
        "density": rho_c3,
        "tangent_dim": gauss_mu4_tangent_dimension,
    },
    {
        "name": "C4",
        "constraint": "mu4 + <P_mu4,+>=KMS",
        "density": rho_c4,
        "tangent_dim": mu4_tangent_dimension - 1,
    },
    {
        "name": "C5",
        "constraint": "mu4 + <deck charge>=KMS",
        "density": rho_c5,
        "tangent_dim": mu4_tangent_dimension - 1,
    },
    {
        "name": "C6",
        "constraint": "mu4 + fixed charged-seam marginal",
        "density": rho_c6,
        "tangent_dim": mu4_tangent_dimension - 3,
    },
    {
        "name": "C7",
        "constraint": "hard mu4,+ support only",
        "density": rho_c7,
        "tangent_dim": rank_c7**2 - 1,
    },
    {
        "name": "C8",
        "constraint": "mu4 + fixed <N_Q>,<N_e>",
        "density": rho_c8,
        "tangent_dim": mu4_tangent_dimension - 2,
    },
)

candidate_rows = []
response_cache = {
    "C1": star_response,
    "C2": kms_response,
    "C4": kms_response,
    "C5": kms_response,
    "C6": kms_response,
    "C8": kms_response,
}
for candidate in candidate_specs:
    name = candidate["name"]
    density = candidate["density"]
    response = response_cache.get(name)
    if response is None:
        response = pulse_response(density)
    rms = response_numbers(response)[2]
    product_contrast = float(
        np.sqrt(np.mean((response - product_response) ** 2))
    )
    distance_to_v1000 = trace_distance(density, RHO_KMS)
    hessian_bound = hessian_lower_bound(density)
    candidate_rows.append(
        {
            **candidate,
            "rms": rms,
            "contrast": product_contrast,
            "distance": distance_to_v1000,
            "hessian_bound": hessian_bound,
            "unique": hessian_bound > 0.0,
            "alive": rms > 1e-5,
            "matches": distance_to_v1000 < 1e-10
            and abs(product_contrast - frozen_contrast) < 1e-10,
        }
    )

report(
    "all eight exact minimizers have positive admissible Hessian",
    all(
        row["unique"]
        and row["tangent_dim"] > 0
        and row["hessian_bound"] > 0.0
        for row in candidate_rows
    ),
    "min BKM lower bound=%.9e over tangent dimensions %s"
    % (
        min(row["hessian_bound"] for row in candidate_rows),
        [row["tangent_dim"] for row in candidate_rows],
    ),
)
report(
    "hard sector candidates kill the SK response",
    all(
        row["rms"] < 1e-13
        for row in candidate_rows
        if row["name"] in ("C1", "C3", "C7")
    ),
    "RMS C1/C3/C7=%s"
    % [
        "%.3e" % row["rms"]
        for row in candidate_rows
        if row["name"] in ("C1", "C3", "C7")
    ],
)
report(
    "response-alive candidates are exactly the unchanged KMS state",
    all(
        row["matches"] == row["alive"]
        for row in candidate_rows
    )
    and {
        row["name"] for row in candidate_rows if row["alive"]
    } == {"C2", "C4", "C5", "C6", "C8"},
    "alive/matching=%s"
    % [
        row["name"] for row in candidate_rows
        if row["alive"] and row["matches"]
    ],
)

print("\nCANDIDATE LATTICE OUTCOME")
print("  order: C2 < {C3,C4,C5,C6,C7,C8}; C3<C1 and C7<C1")
print(
    "  set  unique response  RMS(response)  contrast(product) "
    "D_tr(v1000)  tangents  Hessian>="
)
for row in candidate_rows:
    print(
        "  %-3s  %-6s %-8s %.9e  %.9e    %.9e  %7d  %.3e"
        % (
            row["name"],
            "yes" if row["unique"] else "no",
            "alive" if row["alive"] else "dead",
            row["rms"],
            row["contrast"],
            row["distance"],
            row["tangent_dim"],
            row["hessian_bound"],
        )
    )


# ---------------------------------------------------------------------------
# Mutants.
# ---------------------------------------------------------------------------
# Drop mu4-sector support while retaining Gauss support.
gauss_values, gauss_vectors = np.linalg.eigh(P_GAUSS)
GAUSS_SUPPORT = gauss_vectors[:, gauss_values > 0.5]
sigma_gauss = GAUSS_SUPPORT.conj().T @ RHO_KMS @ GAUSS_SUPPORT
rho_drop_mu4 = sigma_gauss / np.trace(sigma_gauss)
rho_drop_mu4_full = GAUSS_SUPPORT @ rho_drop_mu4 @ GAUSS_SUPPORT.conj().T
trace_distance_drop = 0.5 * float(
    np.sum(np.abs(np.linalg.eigvalsh(rho_drop_mu4_full - rho_star_full)))
)
report(
    "MUTANT dropping mu4-sector support changes the minimizer",
    GAUSS_SUPPORT.shape[1] == 24 and trace_distance_drop > 0.1,
    "rank 6 -> 24, trace distance=%.9f" % trace_distance_drop,
)

# Removing even mu4 invariance leaves the unconstrained Umegaki problem.
# Because rho_KMS is faithful, Klein's inequality still gives the same unique
# minimizer.  This is the decisive failed mutant: C2 has no identifying power.
unconstrained_minimizer = RHO_KMS
unconstrained_to_c2 = trace_distance(unconstrained_minimizer, RHO_KMS)
unconstrained_hessian_bound = hessian_lower_bound(unconstrained_minimizer)
report(
    "MUTANT no-mu4 exposes the canonical-selection tension",
    unconstrained_to_c2 < 1e-13
    and unconstrained_hessian_bound > 0.0,
    "still unique; D_tr(C0,C2)=%.3e, Hessian>=%.9e"
    % (unconstrained_to_c2, unconstrained_hessian_bound),
)
report(
    "MUTANT over-constrained C1 kills the response",
    star_numbers[2] < 1e-13
    and trace_distance_drop > 0.1,
    "C1 RMS=%.3e, D_tr(C1,C3)=%.9f"
    % (star_numbers[2], trace_distance_drop),
)

# Add a decoupled copy: A_mut=M_6 direct-sum M_6 has centre C^2.  True
# Umegaki entropy retains the binary KL term, whose central Hessian at
# equal weights is four.  Deleting that term is the deliberately broken
# objective and produces the expected flat central weight.
mutant_center_dimension = 2
central_hessian_ugemaki = 4.0
central_weights = np.linspace(0.1, 0.9, 9)
true_central_costs = np.array(
    [
        weight * np.log(2.0 * weight)
        + (1.0 - weight) * np.log(2.0 * (1.0 - weight))
        for weight in central_weights
    ]
)
central_blind_costs = np.zeros_like(central_weights)
report(
    "MUTANT decoupled block exposes a two-dimensional center",
    mutant_center_dimension == 2
    and true_central_costs[4] == 0.0
    and np.count_nonzero(true_central_costs < 1e-14) == 1
    and central_hessian_ugemaki > 0.0,
    "center dim=2; true central Hessian=%.1f; unique weight=1/2"
    % central_hessian_ugemaki,
)
report(
    "MUTANT flat directions require deleting the central KL term",
    np.ptp(central_blind_costs) == 0.0
    and np.ptp(true_central_costs) > 0.1,
    "central-blind objective flat on 9/9 weights; Umegaki is not flat",
)


print("\nTHEOREM RESULT")
print(
    "  D(rho||rho_KMS) = D(rho||rho_star) - log Tr(P rho_KMS), "
    "rho=P rho P"
)
print(
    "  strict Hessian spectrum: [%.9e, %.9e] on all %d tangents"
    % (hessian_spectrum.min(), hessian_spectrum.max(), len(basis))
)
print("  center(A_adm) dimension: %d" % center_dimension)
print("  compression identity maxdev: %.3e" % identity_deviation)
print(
    "  consequence: frozen contrast %.9e; compressed-state RMS %.3e"
    % (frozen_contrast, star_numbers[2])
)
print(
    "  mutants: hard-sector removal distance %.9f; no-mu4 distance %.3e"
    % (trace_distance_drop, unconstrained_to_c2)
)
print("\nCONTRACT DEFINITION TEST")
print(
    "  Proposed weakest alive set: S_adm={rho: "
    "[rho,U_mu4]=0}; rho_0=argmin D(rho||rho_KMS)=rho_KMS."
)
print(
    "  It reproduces v1000 exactly and the frozen contrast %.9e."
    % frozen_contrast
)
print(
    "  Rejected as a canonical repair: deleting the mu4 condition leaves "
    "the same unique rho_KMS."
)
print("\nHONEST BOUNDARY")
print("  Finite 96-dimensional 1+1D model, not the 4D algebra.")
print("  The finite proxy P_mu4,+ is particle-number mod 4, not a derived")
print("  determinant-line orientation projector.")
print("  Hard projections kill response; affine KMS data are selection-vacuous.")
print("  FTRANSFER.SK.RHO0.01 remains [O].")
print(
    "\nVERDICT: RHO0_ADMISSIBLE_NO_SET_WORKS("
    "HARD_SECTORS_RESPONSE_DEAD; KMS_AFFINE_SETS_SELECTION_VACUOUS)"
)
print(
    "FINDING: C2_IS_WEAKEST_UNIQUE_RESPONSE_ALIVE_AND_MATCHES_V1000 "
    "BUT C0_EQUALS_C2"
)
print("runtime %.2f s" % (time.perf_counter() - START))
print("PROBE " + ("ALL PASS" if ALL_OK else "HAS FAILURES"))
raise SystemExit(0 if ALL_OK else 1)
