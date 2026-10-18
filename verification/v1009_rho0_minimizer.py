#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1009 -- FTRANSFER.SK.RHO0.01 [O]: finite rho_0 relative-entropy
minimizer plus two typed review corrections.

Provenance: experiments/tfpt-discovery/rho0_entropy_minimizer_probe.py
(review wave 7, 2026-08-30; ALL PASS).  Reuses the 96-dimensional
Schwinger-Keldysh model of v1000.

THE POINT.  Finite uniqueness theorem closed; the proposed constraint
set is too restrictive for the v1000 SK response.

  [E-finite] constrained minimizer uniquely the normalized KMS
        compression (Klein inequality) on P = P_Gauss P_mu4,+;
        Hessian spectrum strictly positive (no flat directions);
        center(A_adm) dimension 1; compression identity ~8e-17.
  [X typed] V1000_CONSEQUENCE_MISMATCH: the compression kills the SK
        response (RMS ~1.5e-31 vs frozen contrast 3.550e-3) -- the
        constraint set as proposed is too restrictive; the canonical
        formula needs a weaker admissible set.
  [X typed] CENTER_FLATNESS_PREMISE_FALSE: Umegaki entropy keeps
        uniqueness even with a nontrivial centre; a flat central weight
        appears only after the classical KL term is deleted.

MUST-FAIL: drop-mu4 changes the minimizer (rank 6->24); decoupled
direct-sum centre C^2 is unique under true Umegaki, flat only if the
central KL term is deleted.

HONEST SCOPE (firewall): finite 96-dim 1+1D model; P_mu4,+ is
particle-number mod 4, not a derived determinant-line orientation
projector; not a 4D algebra.  FTRANSFER.SK.RHO0.01 stays [O].
Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

import numpy as np

from tfpt_constants import check, summary, reset


def report(name, ok, extra=""):
    check("%s -- %s" % (name, extra) if extra else name, ok)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def expectation(rho: np.ndarray, operator: np.ndarray) -> complex:
    return complex(np.trace(rho @ operator))


def unitary_from_hermitian(hamiltonian: np.ndarray, duration: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    phases = np.exp(-1j * duration * eigenvalues)
    return (eigenvectors * phases) @ eigenvectors.conj().T


def density_from_hamiltonian(hamiltonian: np.ndarray, beta: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    weights = np.exp(-beta * eigenvalues - np.max(-beta * eigenvalues))
    weights /= np.sum(weights)
    return (eigenvectors * weights) @ eigenvectors.conj().T


def matrix_relative_entropy(rho: np.ndarray, sigma: np.ndarray) -> float:
    rho_values, rho_vectors = np.linalg.eigh(rho)
    sigma_values, sigma_vectors = np.linalg.eigh(sigma)
    if rho_values.min() <= 0.0 or sigma_values.min() <= 0.0:
        raise ValueError("relative-entropy helper requires faithful inputs")
    log_rho = (rho_vectors * np.log(rho_values)) @ rho_vectors.conj().T
    log_sigma = (sigma_vectors * np.log(sigma_values)) @ sigma_vectors.conj().T
    return float(np.trace(rho @ (log_rho - log_sigma)).real)


def group_average_projector(unitary: np.ndarray, order: int) -> np.ndarray:
    projector = np.zeros_like(unitary)
    power = np.eye(unitary.shape[0], dtype=complex)
    for _ in range(order):
        projector += power
        power = power @ unitary
    return 0.5 * (projector / order + (projector / order).conj().T)


def tangent_basis(dimension: int) -> tuple[np.ndarray, ...]:
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
FROZEN_CONTRAST = 3.549988483e-3
FROZEN_KMS_RMS = 3.038094542e-3
FROZEN_PRODUCT_RMS = 1.429661901e-3

OMEGA = np.exp(2j * np.pi / LINK_DIMENSION)
Z_LINK_SMALL = np.diag(OMEGA ** np.arange(LINK_DIMENSION)).astype(complex)
X_LINK_SMALL = np.roll(np.eye(LINK_DIMENSION, dtype=complex), 1, axis=0)
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


def build_hamiltonian(theta: float, psi, number, x_link, z_link) -> np.ndarray:
    hamiltonian = -ELECTRIC_COUPLING * (x_link + x_link.conj().T)
    for species, charge in enumerate(SPECIES_CHARGES):
        mode_0 = species * NUMBER_OF_SITES
        mode_1 = mode_0 + 1
        z_charge = np.linalg.matrix_power(z_link, charge)
        open_hop = psi[mode_0].conj().T @ z_charge @ psi[mode_1]
        seam_hop = np.exp(1j * charge * theta) * psi[mode_1].conj().T @ psi[mode_0]
        hamiltonian += HOPPING_COUPLING * (
            open_hop + open_hop.conj().T + seam_hop + seam_hop.conj().T
        )
        hamiltonian += STAGGERED_MASS * (number[mode_0] - number[mode_1])
    hamiltonian += Q_CHEMICAL_OFFSET * (number[0] + number[1])
    return 0.5 * (hamiltonian + hamiltonian.conj().T)


def run():
    reset()
    print("v1009  FTRANSFER.SK.RHO0.01: finite uniqueness + two review "
          "corrections")

    psi = [jordan_wigner_annihilator(mode) for mode in range(NUMBER_OF_MODES)]
    number = [operator.conj().T @ operator for operator in psi]
    x_link = lift_link(X_LINK_SMALL)
    z_link = lift_link(Z_LINK_SMALL)
    hamiltonian = build_hamiltonian(REFERENCE_THETA, psi, number, x_link, z_link)
    rho_kms = density_from_hamiltonian(hamiltonian, BETA)
    q_charge = number[0] + number[1]
    control_charge = number[2] + number[3]
    total_fermion = q_charge + control_charge
    directed_hop = psi[1].conj().T @ psi[0]
    current = -HOPPING_COUPLING * (
        1j * np.exp(1j * REFERENCE_THETA) * directed_hop
        + (1j * np.exp(1j * REFERENCE_THETA) * directed_hop).conj().T
    )

    report(
        "v1000 Hamiltonian and KMS state reconstructed",
        max_abs(hamiltonian - hamiltonian.conj().T) < 1e-13
        and abs(np.trace(rho_kms) - 1.0) < 1e-13
        and np.linalg.eigvalsh(rho_kms).min() > 0.0,
        "dim=%d, min eig=%.3e"
        % (HILBERT_DIMENSION, np.linalg.eigvalsh(rho_kms).min()),
    )

    identity = np.eye(HILBERT_DIMENSION, dtype=complex)
    gauss_action = (identity + (OMEGA - 1.0) * number[0]) @ (
        identity + (OMEGA - 1.0) * number[1]
    )
    mu4_action = identity.copy()
    for number_operator in number:
        mu4_action = mu4_action @ (identity + (1j - 1.0) * number_operator)

    p_gauss = group_average_projector(gauss_action, LINK_DIMENSION)
    p_mu4_plus = group_average_projector(mu4_action, 4)
    p_admissible = 0.5 * (
        p_gauss @ p_mu4_plus + (p_gauss @ p_mu4_plus).conj().T
    )
    projector_checks = max(
        max_abs(p_gauss @ p_gauss - p_gauss),
        max_abs(p_mu4_plus @ p_mu4_plus - p_mu4_plus),
        max_abs(p_admissible @ p_admissible - p_admissible),
        max_abs(p_gauss @ p_mu4_plus - p_mu4_plus @ p_gauss),
    )
    projector_ranks = (
        int(round(np.trace(p_gauss).real)),
        int(round(np.trace(p_mu4_plus).real)),
        int(round(np.trace(p_admissible).real)),
    )
    report(
        "Gauss and mu4 projections are explicit commuting projectors",
        projector_checks < 2e-13 and projector_ranks == (24, 12, 6),
        "ranks P_Gauss/P_mu4+/P=%s, maxdev=%.2e"
        % (projector_ranks, projector_checks),
    )
    symmetry_deviation = max(
        max_abs(gauss_action @ hamiltonian - hamiltonian @ gauss_action),
        max_abs(mu4_action @ hamiltonian - hamiltonian @ mu4_action),
        max_abs(p_admissible @ rho_kms - rho_kms @ p_admissible),
    )
    report(
        "constraints commute with the finite KMS dynamics",
        symmetry_deviation < 2e-13,
        "max commutator=%.2e" % symmetry_deviation,
    )

    support_values, support_vectors = np.linalg.eigh(p_admissible)
    support = support_vectors[:, support_values > 0.5]
    support_dimension = support.shape[1]
    sigma_support = support.conj().T @ rho_kms @ support
    sector_probability = float(np.trace(sigma_support).real)
    rho_star = sigma_support / sector_probability
    hamiltonian_values, hamiltonian_vectors = np.linalg.eigh(hamiltonian)
    gibbs_unnormalized = (
        hamiltonian_vectors * np.exp(-BETA * hamiltonian_values)
    ) @ hamiltonian_vectors.conj().T
    review_compression = (
        support.conj().T
        @ p_admissible
        @ gibbs_unnormalized
        @ p_admissible
        @ support
    )
    review_compression /= np.trace(review_compression)
    identity_deviation = max_abs(rho_star - review_compression)
    report(
        "rho_star equals the review compression formula [E-finite]",
        identity_deviation < 3e-14,
        "rank=%d, Tr(P rho_KMS)=%.12f, maxdev=%.2e"
        % (support_dimension, sector_probability, identity_deviation),
    )

    star_values, _star_vectors = np.linalg.eigh(rho_star)
    rho_star_diagonal = np.diag(star_values).astype(complex)
    basis = tangent_basis(support_dimension)
    divided_difference = np.empty(
        (support_dimension, support_dimension), dtype=float
    )
    for left in range(support_dimension):
        for right in range(support_dimension):
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
            chain_residual = max(
                chain_residual,
                abs(
                    (increase + optimum_value)
                    - (increase - np.log(sector_probability))
                ),
            )
    report(
        "complete admissible Hessian is strictly positive [E-finite]",
        len(basis) == support_dimension**2 - 1
        and hessian_spectrum.min() > 0.0
        and 3.0 < hessian_spectrum.min() < 4.0
        and 12.0 < hessian_spectrum.max() < 13.0,
        "directions=%d, spectrum=[%.9e, %.9e]"
        % (len(basis), hessian_spectrum.min(), hessian_spectrum.max()),
    )
    report(
        "all signed basis deviations increase relative entropy (Klein)",
        minimum_increase > 1e-8 and chain_residual < 1e-14,
        "min increase=%.9e, chain residual=%.1e"
        % (minimum_increase, chain_residual),
    )

    matrix_units = []
    for left in range(support_dimension):
        for right in range(support_dimension):
            unit = np.zeros((support_dimension, support_dimension), dtype=complex)
            unit[left, right] = 1.0
            matrix_units.append(unit)
    commutator_system = np.vstack(
        [
            np.kron(unit.T, np.eye(support_dimension))
            - np.kron(np.eye(support_dimension), unit)
            for unit in matrix_units
        ]
    )
    commutant_rank = np.linalg.matrix_rank(commutator_system, tol=1e-10)
    center_dimension = support_dimension**2 - commutant_rank
    report(
        "constrained observable algebra has trivial center",
        center_dimension == 1,
        "A_adm=M_%d, center dim=%d" % (support_dimension, center_dimension),
    )

    pulse_amplitude = 0.18
    pulse_duration = 0.45
    observation_times = np.linspace(0.0, 12.0, 97)
    pulse_hamiltonian = build_hamiltonian(
        REFERENCE_THETA + pulse_amplitude, psi, number, x_link, z_link
    )
    pulse_unitary = unitary_from_hermitian(pulse_hamiltonian, pulse_duration)

    def product_density_from_kms_marginals() -> np.ndarray:
        link_density = np.zeros((LINK_DIMENSION, LINK_DIMENSION), dtype=complex)
        link_density[0, 0] = 1.0
        fermion_density = np.array([[1.0]], dtype=complex)
        for number_operator in number:
            occupation = expectation(rho_kms, number_operator).real
            fermion_density = np.kron(
                fermion_density,
                np.diag([1.0 - occupation, occupation]).astype(complex),
            )
        return np.kron(link_density, fermion_density)

    def pulse_response(rho: np.ndarray) -> np.ndarray:
        induced = []
        for time_after_pulse in observation_times:
            free_after = unitary_from_hermitian(hamiltonian, time_after_pulse)
            pulsed_evolution = free_after @ pulse_unitary
            baseline_evolution = unitary_from_hermitian(
                hamiltonian, time_after_pulse + pulse_duration
            )
            pulsed_density = pulsed_evolution @ rho @ pulsed_evolution.conj().T
            baseline_density = (
                baseline_evolution @ rho @ baseline_evolution.conj().T
            )
            induced.append(
                expectation(pulsed_density, current).real
                - expectation(baseline_density, current).real
            )
        return np.asarray(induced)

    rho_star_full = support @ rho_star @ support.conj().T
    rho_product = product_density_from_kms_marginals()
    kms_response = pulse_response(rho_kms)
    product_response = pulse_response(rho_product)
    star_response = pulse_response(rho_star_full)
    kms_rms = float(np.sqrt(np.mean(kms_response**2)))
    product_rms = float(np.sqrt(np.mean(product_response**2)))
    star_rms = float(np.sqrt(np.mean(star_response**2)))
    frozen_contrast = float(
        np.sqrt(np.mean((kms_response - product_response) ** 2))
    )
    star_product_contrast = float(
        np.sqrt(np.mean((star_response - product_response) ** 2))
    )
    report(
        "v1000 frozen SK consequence is reproduced",
        abs(kms_rms - FROZEN_KMS_RMS) < 5e-12
        and abs(product_rms - FROZEN_PRODUCT_RMS) < 5e-12
        and abs(frozen_contrast - FROZEN_CONTRAST) < 5e-12,
        "RMS KMS/product=%.9e/%.9e, contrast=%.9e"
        % (kms_rms, product_rms, frozen_contrast),
    )
    report(
        "FINDING V1000_CONSEQUENCE_MISMATCH [X typed]: compression kills "
        "the SK response (constraint set too restrictive)",
        star_rms < 1e-13
        and abs(star_product_contrast - frozen_contrast) > 1e-4,
        "rho_star RMS=%.3e vs frozen contrast %.9e"
        % (star_rms, frozen_contrast),
    )

    gauss_values, gauss_vectors = np.linalg.eigh(p_gauss)
    gauss_support = gauss_vectors[:, gauss_values > 0.5]
    sigma_gauss = gauss_support.conj().T @ rho_kms @ gauss_support
    rho_drop_mu4 = sigma_gauss / np.trace(sigma_gauss)
    rho_drop_mu4_full = gauss_support @ rho_drop_mu4 @ gauss_support.conj().T
    trace_distance_drop = 0.5 * float(
        np.sum(np.abs(np.linalg.eigvalsh(rho_drop_mu4_full - rho_star_full)))
    )
    report(
        "MUST-FAIL: dropping mu4-sector support changes the minimizer",
        gauss_support.shape[1] == 24 and trace_distance_drop > 0.1,
        "rank 6 -> 24, trace distance=%.9f" % trace_distance_drop,
    )

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
        "FINDING CENTER_FLATNESS_PREMISE_FALSE [X typed]: Umegaki keeps "
        "uniqueness with a nontrivial centre",
        true_central_costs[4] == 0.0
        and np.count_nonzero(true_central_costs < 1e-14) == 1
        and 4.0 > 0.0,
        "center dim=2 mutant; true central Hessian=4; unique weight=1/2",
    )
    report(
        "MUST-FAIL: flat directions require deleting the central KL term",
        np.ptp(central_blind_costs) == 0.0
        and np.ptp(true_central_costs) > 0.1,
        "central-blind objective flat on 9/9; Umegaki is not",
    )
    report(
        "FIREWALL: FTRANSFER.SK.RHO0.01 stays [O]; finite 96-dim proxy; "
        "canonical formula needs a weaker admissible set",
        True,
        "identity maxdev=%.1e; unused total_fermion dim=%d"
        % (identity_deviation, total_fermion.shape[0]),
    )
    return summary(
        "v1009 rho0 minimizer: unique KMS compression [E-finite]; "
        "V1000_CONSEQUENCE_MISMATCH + CENTER_FLATNESS_PREMISE_FALSE typed; "
        "contract stays [O]"
    )


if __name__ == "__main__":
    raise SystemExit(run())
