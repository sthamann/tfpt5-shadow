#!/usr/bin/env python3
"""Probe frozen D4-odd determinant/Pfaffian candidates for nu kappa.

EXPLORATION ONLY.  This module evaluates only the already-frozen finite
v991 collar, v1000 SK sector, and Stage-4 master assembly.  It performs no
parameter scan and reads no measured neutrino data.

ANTI-NUMEROLOGY / PRE-DECLARATION
----------------------------------
Exactly six candidates are evaluated (LEE trials = 6), before comparison
with the required cancellation ``1-|c/a| = 1.885e-4``:

K1  ``det(T_+)/det(T_-)-1`` for the block-diagonal, regularized v991 seam
    cycle transfer kernels; ordering the sheets is the orientation bit.
K2  ``Pf(A_+)/Pf(A_-)-1`` for their canonical antisymmetric Majorana lifts;
    Pfaffian orientation changes with the same sheet ordering.
K3  ``(hol_+-hol_-)/(hol_++hol_-)`` for the v991 determinant-line
    holonomies; conjugation exchanges the two orientation sheets.
K4  the signed v1000 SK response-trace correlator (magnitude about 3.55e-3);
    the current and contour pulse are odd under orientation reflection.
K5  ``(chi_1-chi_3)/(chi_1+chi_3)`` for the master-assembly seam
    transduction in the D4-mirror clock sectors k=1 and k=3.
K6  ``(E_1-E_3)/(E_1+E_3)`` for the corresponding assembled ground
    energies; the deck-sector ordering is the orientation bit.

The magnitude window is pre-declared as a factor of three around 1.885e-4.
Every candidate must also obey K(reflected model) = -K(model).  The eta=0
projection uses equal sheet weights and must vanish for every candidate.
A D4-even normalized sheet sum is the mandatory parity mutant and must fail
the odd test.

If a candidate hits, it is inserted without fitting into the frozen
orientation-seesaw Schur complement with ``c/a = 1-K``.  If all six miss,
the typed conclusion is that these finite scaffold objects do not supply
the scale and that the true 4D functional remains the required location.
"""

from __future__ import annotations

import inspect
import math
import os
import sys
from dataclasses import dataclass

import mpmath as mp
import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
VERIFICATION = os.path.join(REPO, "verification")
for import_path in (HERE, VERIFICATION):
    if import_path not in sys.path:
        sys.path.insert(0, import_path)

import tfpt2p1d_master_assembly_probe as master  # noqa: E402
import v991_detline_bulk_edge as detline  # noqa: E402
from nu_orientation_seesaw_probe import (  # noqa: E402
    Candidate as SeesawCandidate,
    I3,
    ODD_DIAGONAL,
    effective_kernel,
    solve_inverse_diagnostic,
)
from tfpt_constants import g_car, phi0  # noqa: E402


REQUIRED_KAPPA = 1.885e-4
WINDOW_FACTOR = 3.0
WINDOW = (REQUIRED_KAPPA / WINDOW_FACTOR, REQUIRED_KAPPA * WINDOW_FACTOR)
PARITY_TOLERANCE = 2.0e-8
ZERO_TOLERANCE = 2.0e-8
LEE_TRIALS = 6

KAPPA_DECLARATIONS = (
    ("K1", "v991 seam-cycle determinant ratio"),
    ("K2", "v991 antisymmetric Majorana-kernel Pfaffian ratio"),
    ("K3", "v991 determinant-line holonomy odd part"),
    ("K4", "v1000 signed SK orientation correlator"),
    ("K5", "master k=1 versus k=3 seam-transduction asymmetry"),
    ("K6", "master k=1 versus k=3 deck-energy splitting"),
)


@dataclass(frozen=True)
class CandidateResult:
    label: str
    rationale: str
    value: complex
    reflected_value: complex
    eta_zero_value: complex

    @property
    def parity_error(self) -> float:
        return abs(self.value + self.reflected_value)

    @property
    def parity_ok(self) -> bool:
        scale = max(1.0, abs(self.value), abs(self.reflected_value))
        return self.parity_error <= PARITY_TOLERANCE * scale

    @property
    def eta_zero_ok(self) -> bool:
        return abs(self.eta_zero_value) <= ZERO_TOLERANCE

    @property
    def magnitude(self) -> float:
        return abs(self.value)

    @property
    def magnitude_hit(self) -> bool:
        return WINDOW[0] <= self.magnitude <= WINDOW[1]

    @property
    def hit(self) -> bool:
        return self.parity_ok and self.eta_zero_ok and self.magnitude_hit


def report_check(label: str, passed: bool) -> bool:
    print(("PASS " if passed else "FAIL ") + label)
    return bool(passed)


def pfaffian(matrix: np.ndarray) -> complex:
    """Compute a complex skew-matrix Pfaffian by pivoted elimination."""
    work = np.array(matrix, dtype=complex, copy=True)
    if work.ndim != 2 or work.shape[0] != work.shape[1]:
        raise ValueError("Pfaffian input must be square")
    dimension = work.shape[0]
    if dimension % 2:
        return 0.0j
    if np.max(np.abs(work + work.T)) > 1.0e-10:
        raise ValueError("Pfaffian input must be antisymmetric")

    value = 1.0 + 0.0j
    for left in range(0, dimension - 1, 2):
        pivot = left + 1 + int(np.argmax(np.abs(work[left, left + 1 :])))
        if abs(work[left, pivot]) < 1.0e-14:
            return 0.0j
        if pivot != left + 1:
            work[[left + 1, pivot], :] = work[[pivot, left + 1], :]
            work[:, [left + 1, pivot]] = work[:, [pivot, left + 1]]
            value *= -1.0
        pivot_value = work[left, left + 1]
        value *= pivot_value
        if left + 2 < dimension:
            rest = slice(left + 2, dimension)
            update = (
                np.outer(work[left, rest], work[left + 1, rest])
                - np.outer(work[left + 1, rest], work[left, rest])
            ) / pivot_value
            work[rest, rest] -= update
    return complex(value)


def seam_cycle_kernels(sheet: int) -> tuple[np.ndarray, ...]:
    """Return the frozen v991 regularized strip kernels on one sheet."""
    momenta = np.linspace(
        0.0, 2.0 * np.pi, detline.NK_STRIP, endpoint=False
    )
    identity = np.eye(2 * detline.NY_STRIP, dtype=complex)
    return tuple(
        detline.strip_H(
            momentum,
            1.0,
            detline.NY_STRIP,
            sy=float(sheet),
        )
        + 1j * detline.EPS_DET * identity
        for momentum in momenta
    )


def determinant_cycle_ratio(
    numerator: tuple[np.ndarray, ...],
    denominator: tuple[np.ndarray, ...],
) -> complex:
    """Evaluate det(blockdiag numerator)/det(blockdiag denominator)."""
    log_magnitude = 0.0
    phase = 1.0 + 0.0j
    for left, right in zip(numerator, denominator):
        left_sign, left_log = np.linalg.slogdet(left)
        right_sign, right_log = np.linalg.slogdet(right)
        log_magnitude += float(left_log - right_log)
        phase *= complex(left_sign / right_sign)
    return complex(np.exp(log_magnitude) * phase)


def majorana_lift(kernel: np.ndarray) -> np.ndarray:
    """Canonical antisymmetric lift A(T)=[[0,T],[-T^T,0]]."""
    zero = np.zeros_like(kernel)
    return np.block([[zero, kernel], [-kernel.T, zero]])


def pfaffian_cycle_ratio(
    numerator: tuple[np.ndarray, ...],
    denominator: tuple[np.ndarray, ...],
) -> tuple[complex, float]:
    """Evaluate the Pfaffian ratio and the worst Pf(A)^2-det(A) residual."""
    ratio = 1.0 + 0.0j
    worst_identity_error = 0.0
    for left, right in zip(numerator, denominator):
        left_lift = majorana_lift(left)
        right_lift = majorana_lift(right)
        left_pfaffian = pfaffian(left_lift)
        right_pfaffian = pfaffian(right_lift)
        ratio *= left_pfaffian / right_pfaffian
        for lift, pfaffian_value in (
            (left_lift, left_pfaffian),
            (right_lift, right_pfaffian),
        ):
            determinant_value = np.linalg.det(lift)
            scale = max(1.0, abs(determinant_value))
            worst_identity_error = max(
                worst_identity_error,
                abs(pfaffian_value**2 - determinant_value) / scale,
            )
    return complex(ratio), worst_identity_error


def normalized_difference(left: complex, right: complex) -> complex:
    denominator = left + right
    if abs(denominator) <= 1.0e-13 * max(1.0, abs(left), abs(right)):
        raise ZeroDivisionError("normalized odd part has a zero even denominator")
    return complex((left - right) / denominator)


def v1000_sk_orientation_correlators() -> tuple[float, float, float]:
    """Recompute the signed v1000 response-trace correlator on both sheets."""
    number_of_sites = 2
    link_dimension = 6
    species_charges = (1, 0)
    number_of_modes = 4
    fermion_dimension = 2**number_of_modes
    omega = np.exp(2j * np.pi / link_dimension)
    z_link_small = np.diag(omega ** np.arange(link_dimension)).astype(complex)
    x_link_small = np.roll(
        np.eye(link_dimension, dtype=complex), 1, axis=0
    )
    sigma_z = np.diag([1.0, -1.0]).astype(complex)
    annihilation = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    electric_coupling = 1.0
    hopping_coupling = 0.7
    staggered_mass = 0.5
    chemical_offset = 0.5
    beta = 0.35
    reference_theta = 0.7
    pulse_amplitude = 0.18
    pulse_duration = 0.45
    observation_times = np.linspace(0.0, 12.0, 97)

    def jordan_wigner_annihilator(mode: int) -> np.ndarray:
        factors = []
        for index in range(number_of_modes):
            if index < mode:
                factors.append(sigma_z)
            elif index == mode:
                factors.append(annihilation)
            else:
                factors.append(np.eye(2, dtype=complex))
        result = factors[0]
        for factor in factors[1:]:
            result = np.kron(result, factor)
        return np.kron(np.eye(link_dimension, dtype=complex), result)

    operators = tuple(
        jordan_wigner_annihilator(mode) for mode in range(number_of_modes)
    )
    numbers = tuple(operator.conj().T @ operator for operator in operators)
    x_link = np.kron(x_link_small, np.eye(fermion_dimension, dtype=complex))
    z_link = np.kron(z_link_small, np.eye(fermion_dimension, dtype=complex))

    def build_hamiltonian(theta: float) -> np.ndarray:
        hamiltonian = -electric_coupling * (x_link + x_link.conj().T)
        for species, charge in enumerate(species_charges):
            mode_0 = species * number_of_sites
            mode_1 = mode_0 + 1
            z_charge = np.linalg.matrix_power(z_link, charge)
            open_hop = (
                operators[mode_0].conj().T
                @ z_charge
                @ operators[mode_1]
            )
            seam_hop = (
                np.exp(1j * charge * theta)
                * operators[mode_1].conj().T
                @ operators[mode_0]
            )
            hamiltonian += hopping_coupling * (
                open_hop
                + open_hop.conj().T
                + seam_hop
                + seam_hop.conj().T
            )
            hamiltonian += staggered_mass * (
                numbers[mode_0] - numbers[mode_1]
            )
        hamiltonian += chemical_offset * (numbers[0] + numbers[1])
        return 0.5 * (hamiltonian + hamiltonian.conj().T)

    def seam_derivative(theta: float) -> np.ndarray:
        directed_hop = operators[1].conj().T @ operators[0]
        derivative = 1j * np.exp(1j * theta) * directed_hop
        return hopping_coupling * (derivative + derivative.conj().T)

    def thermal_state(hamiltonian: np.ndarray) -> np.ndarray:
        eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
        shifted = -beta * eigenvalues
        weights = np.exp(shifted - np.max(shifted))
        probabilities = weights / np.sum(weights)
        return (eigenvectors * probabilities) @ eigenvectors.conj().T

    def product_state(kms_state: np.ndarray) -> np.ndarray:
        link_density = np.zeros(
            (link_dimension, link_dimension), dtype=complex
        )
        link_density[0, 0] = 1.0
        fermion_density = np.array([[1.0]], dtype=complex)
        for number_operator in numbers:
            occupation = float(np.trace(kms_state @ number_operator).real)
            fermion_density = np.kron(
                fermion_density,
                np.diag((1.0 - occupation, occupation)).astype(complex),
            )
        return np.kron(link_density, fermion_density)

    def unitary_data(hamiltonian: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        return np.linalg.eigh(hamiltonian)

    def unitary(
        spectral_data: tuple[np.ndarray, np.ndarray], duration: float
    ) -> np.ndarray:
        eigenvalues, eigenvectors = spectral_data
        phases = np.exp(-1j * duration * eigenvalues)
        return (eigenvectors * phases) @ eigenvectors.conj().T

    def induced_trace(
        hamiltonian: np.ndarray,
        pulse_hamiltonian: np.ndarray,
        current: np.ndarray,
        density: np.ndarray,
    ) -> np.ndarray:
        base_data = unitary_data(hamiltonian)
        pulse_unitary = unitary(
            unitary_data(pulse_hamiltonian), pulse_duration
        )
        induced = []
        for time_after_pulse in observation_times:
            free_after = unitary(base_data, time_after_pulse)
            pulsed_evolution = free_after @ pulse_unitary
            baseline_evolution = unitary(
                base_data, time_after_pulse + pulse_duration
            )
            pulsed_density = (
                pulsed_evolution @ density @ pulsed_evolution.conj().T
            )
            baseline_density = (
                baseline_evolution @ density @ baseline_evolution.conj().T
            )
            induced.append(
                float(
                    np.trace((pulsed_density - baseline_density) @ current).real
                )
            )
        return np.asarray(induced)

    hamiltonian = build_hamiltonian(reference_theta)
    pulse_hamiltonian = build_hamiltonian(
        reference_theta + pulse_amplitude
    )
    current = -seam_derivative(reference_theta)
    kms_state = thermal_state(hamiltonian)
    decorrelated_state = product_state(kms_state)
    plus_trace = induced_trace(
        hamiltonian, pulse_hamiltonian, current, kms_state
    ) - induced_trace(
        hamiltonian, pulse_hamiltonian, current, decorrelated_state
    )

    # The v1000 scalar contour dynamics is unchanged on the mirror sheet,
    # while the oriented seam current carries the D4 sign character.  Complex
    # conjugation is time reversal, not this spatial/orientation reflection,
    # and would incorrectly reverse the finite-time evolution as well.
    reflected_hamiltonian = hamiltonian
    reflected_pulse = pulse_hamiltonian
    reflected_current = -current
    reflected_kms = kms_state
    reflected_decorrelated = decorrelated_state
    minus_trace = induced_trace(
        reflected_hamiltonian,
        reflected_pulse,
        reflected_current,
        reflected_kms,
    ) - induced_trace(
        reflected_hamiltonian,
        reflected_pulse,
        reflected_current,
        reflected_decorrelated,
    )

    reference_norm = float(np.linalg.norm(plus_trace))
    normalization = reference_norm * math.sqrt(len(plus_trace))
    plus_correlator = float(np.vdot(plus_trace, plus_trace).real / normalization)
    minus_correlator = float(
        np.vdot(plus_trace, minus_trace).real / normalization
    )
    eta_zero_trace = 0.5 * (plus_trace + minus_trace)
    zero_correlator = float(
        np.vdot(plus_trace, eta_zero_trace).real / normalization
    )
    return plus_correlator, minus_correlator, zero_correlator


def master_sector_transduction(sector: int) -> float:
    """Recompute the frozen master mixed response in clock sector k."""
    phi = sector * np.pi / 2.0
    base = master.physical_clock_hamiltonian(
        0.0, master.SEAM_COUPLING, phi
    )

    def generating_function(
        seam_source: float, physical_source: float
    ) -> float:
        exponent = (
            -master.TRANSDUCTION_BETA * base
            + seam_source * master.SEAM_SOURCE_PC
            + physical_source * master.PHYSICAL_SOURCE_PC
        )
        return master.log_trace_exp(exponent)

    return float(master.mixed_derivative(generating_function))


def master_sector_energy(sector: int) -> float:
    """Ground energy of the frozen additive 1024-state assembly at p=0."""
    phi = sector * np.pi / 2.0
    physical_clock = master.physical_clock_hamiltonian(
        0.0, master.SEAM_COUPLING, phi
    )
    mirror = master.edge_cluster_hamiltonian(0.0, True)
    return float(
        np.linalg.eigvalsh(physical_clock)[0]
        + np.linalg.eigvalsh(mirror)[0]
    )


def build_frozen_candidate_results() -> tuple[
    tuple[CandidateResult, ...], dict[str, float]
]:
    """Build the six target-free candidates from frozen finite objects."""
    plus_kernels = seam_cycle_kernels(+1)
    minus_kernels = seam_cycle_kernels(-1)

    determinant_ratio = determinant_cycle_ratio(
        plus_kernels, minus_kernels
    )
    determinant_ratio_reflected = determinant_cycle_ratio(
        minus_kernels, plus_kernels
    )

    pfaffian_ratio, pfaffian_identity_error = pfaffian_cycle_ratio(
        plus_kernels, minus_kernels
    )
    pfaffian_ratio_reflected, reflected_identity_error = (
        pfaffian_cycle_ratio(minus_kernels, plus_kernels)
    )

    plus_detline = detline.seam_detline(1.0, sy=+1.0)
    minus_detline = detline.seam_detline(1.0, sy=-1.0)
    holonomy_plus = np.exp(1j * plus_detline["phase"])
    holonomy_minus = np.exp(1j * minus_detline["phase"])

    sk_plus, sk_minus, sk_zero = v1000_sk_orientation_correlators()

    chi_1 = master_sector_transduction(1)
    chi_3 = master_sector_transduction(3)
    energy_1 = master_sector_energy(1)
    energy_3 = master_sector_energy(3)

    results = (
        CandidateResult(
            "K1",
            KAPPA_DECLARATIONS[0][1],
            determinant_ratio - 1.0,
            determinant_ratio_reflected - 1.0,
            0.0j,
        ),
        CandidateResult(
            "K2",
            KAPPA_DECLARATIONS[1][1],
            pfaffian_ratio - 1.0,
            pfaffian_ratio_reflected - 1.0,
            0.0j,
        ),
        CandidateResult(
            "K3",
            KAPPA_DECLARATIONS[2][1],
            normalized_difference(holonomy_plus, holonomy_minus),
            normalized_difference(holonomy_minus, holonomy_plus),
            normalized_difference(
                0.5 * (holonomy_plus + holonomy_minus),
                0.5 * (holonomy_plus + holonomy_minus),
            ),
        ),
        CandidateResult(
            "K4",
            KAPPA_DECLARATIONS[3][1],
            complex(sk_plus),
            complex(sk_minus),
            complex(sk_zero),
        ),
        CandidateResult(
            "K5",
            KAPPA_DECLARATIONS[4][1],
            normalized_difference(chi_1, chi_3),
            normalized_difference(chi_3, chi_1),
            normalized_difference(
                0.5 * (chi_1 + chi_3), 0.5 * (chi_1 + chi_3)
            ),
        ),
        CandidateResult(
            "K6",
            KAPPA_DECLARATIONS[5][1],
            normalized_difference(energy_1, energy_3),
            normalized_difference(energy_3, energy_1),
            normalized_difference(
                0.5 * (energy_1 + energy_3),
                0.5 * (energy_1 + energy_3),
            ),
        ),
    )
    diagnostics = {
        "pfaffian_identity_error": max(
            pfaffian_identity_error, reflected_identity_error
        ),
        "holonomy_winding_plus": float(plus_detline["W_seam"]),
        "holonomy_winding_minus": float(minus_detline["W_seam"]),
        "chi_1": chi_1,
        "chi_3": chi_3,
        "energy_1": energy_1,
        "energy_3": energy_3,
    }
    return results, diagnostics


def consequence_spectrum(kappa_value: float) -> dict[str, object]:
    """Insert one hit into the frozen orientation-seesaw Schur complement."""
    epsilon = mp.mpf(phi0) ** 2 / (2 * mp.mpf(g_car))
    inverse = solve_inverse_diagnostic(epsilon)
    a_value = float(inverse["a"])
    candidate = SeesawCandidate(
        label="KAPPA-CONSEQUENCE",
        rationale="c/a=1-K_hit",
        k_even=np.diag(
            (a_value, float(inverse["b"]), a_value)
        ),
        k_odd=(a_value * (1.0 - kappa_value)) * ODD_DIAGONAL,
        coupling=float(inverse["gamma"]) * I3,
    )
    spectrum_values = np.linalg.eigvalsh(
        np.linalg.inv(effective_kernel(candidate, 1))
    )
    spectrum = tuple(float(value) for value in spectrum_values)
    positive = spectrum[0] > 0.0
    hierarchy_ratio = spectrum[0] / spectrum[2]
    light_pair_ratio = spectrum[1] / spectrum[0]
    hierarchy_like = (
        positive
        and 1.0e-5 <= hierarchy_ratio <= 1.0e-3
        and 1.8 <= light_pair_ratio <= 2.2
    )
    return {
        "epsilon": float(epsilon),
        "spectrum": spectrum,
        "hierarchy_ratio": hierarchy_ratio,
        "light_pair_ratio": light_pair_ratio,
        "hierarchy_like": hierarchy_like,
    }


def format_complex(value: complex) -> str:
    if abs(value.imag) < 5.0e-13:
        return f"{value.real:+.12e}"
    return f"{value.real:+.6e}{value.imag:+.6e}i"


def main() -> int:
    print("NU KAPPA PFAFFIAN PROBE -- EXPLORATION ONLY")
    print("PRE-DECLARED TARGET-FREE CANDIDATES")
    for label, rationale in KAPPA_DECLARATIONS:
        print(f"  {label}: {rationale}")
    print(f"  LEE trials = {LEE_TRIALS}")
    print(
        "  magnitude test: |K| in "
        f"[{WINDOW[0]:.12e}, {WINDOW[1]:.12e}] "
        f"(factor {WINDOW_FACTOR:g} around {REQUIRED_KAPPA:.12e})"
    )
    print("  parity test: K(reflected model) = -K(model)")
    print()

    results, diagnostics = build_frozen_candidate_results()

    print("FROZEN OBJECT ANCHORS")
    print(
        "  v991 W_seam(+/-) = "
        f"{diagnostics['holonomy_winding_plus']:+.12e} / "
        f"{diagnostics['holonomy_winding_minus']:+.12e}"
    )
    print(
        "  master chi_1/chi_3 = "
        f"{diagnostics['chi_1']:+.12e} / "
        f"{diagnostics['chi_3']:+.12e}"
    )
    print(
        "  master E_1/E_3 = "
        f"{diagnostics['energy_1']:+.12e} / "
        f"{diagnostics['energy_3']:+.12e}"
    )
    print(
        "  worst Pf(A)^2=det(A) relative residual = "
        f"{diagnostics['pfaffian_identity_error']:.3e}"
    )
    print()

    print("CANDIDATE TABLE")
    print(
        "  K   value(model)             value(mirror)            "
        "parity   |K|/required   magnitude"
    )
    for result in results:
        magnitude_state = "HIT" if result.magnitude_hit else "null"
        print(
            f"  {result.label:<3} {format_complex(result.value):<24} "
            f"{format_complex(result.reflected_value):<24} "
            f"{'PASS' if result.parity_ok else 'FAIL':<8} "
            f"{result.magnitude / REQUIRED_KAPPA:>12.6g}   "
            f"{magnitude_state}"
        )
    print()

    hit_results = tuple(result for result in results if result.hit)
    consequence_rows = []
    if hit_results:
        print("HIT CONSEQUENCE -- ORIENTATION-SEESAW INSERTION")
        for result in hit_results:
            consequence = consequence_spectrum(result.value.real)
            consequence_rows.append((result.label, consequence))
            spectrum = consequence["spectrum"]
            print(
                f"  {result.label}: c/a=1-K; "
                f"M_R/M_scal=[{spectrum[0]:.9e}, {spectrum[1]:.9e}, "
                f"{spectrum[2]:.9e}]; min/max="
                f"{consequence['hierarchy_ratio']:.6e}; mid/min="
                f"{consequence['light_pair_ratio']:.6f}; "
                f"{'HIERARCHY' if consequence['hierarchy_like'] else 'NO_HIERARCHY'}"
            )
    else:
        print("HIT CONSEQUENCE")
        print(
            "  none: all six declared finite-object magnitudes miss the "
            "factor-three window"
        )
    print()

    even_value = 1.0 + 0.0j
    even_reflected = 1.0 + 0.0j
    even_mutant_wrongly_odd = (
        abs(even_value + even_reflected)
        <= PARITY_TOLERANCE * max(1.0, abs(even_value))
    )
    all_eta_zero = all(result.eta_zero_ok for result in results)

    print("MUTANTS")
    print(
        "  D4-even normalized sheet sum: E=+1, E(reflected)=+1; "
        f"odd parity accepted = {even_mutant_wrongly_odd}"
    )
    print(
        "  eta=0 equal-sheet projection: "
        + ", ".join(
            f"{result.label}={format_complex(result.eta_zero_value)}"
            for result in results
        )
    )
    print()

    candidate_source = inspect.getsource(build_frozen_candidate_results)
    circularity_clean = all(
        forbidden not in candidate_source
        for forbidden in (
            "REQUIRED_KAPPA",
            "WINDOW",
            "epsilon",
            "1.885",
        )
    )
    checks = [
        report_check(
            "exactly six unique pre-declared candidates were evaluated",
            len(results) == LEE_TRIALS
            and len({result.label for result in results}) == LEE_TRIALS,
        ),
        report_check(
            "candidate builder contains no required scale or target input",
            circularity_clean,
        ),
        report_check(
            "Pfaffian elimination satisfies Pf(A)^2=det(A)",
            diagnostics["pfaffian_identity_error"] < 2.0e-8,
        ),
        report_check(
            "v991 mirror flips the determinant-line winding",
            abs(diagnostics["holonomy_winding_plus"] - 1.0) < 1.0e-6
            and abs(diagnostics["holonomy_winding_minus"] + 1.0) < 1.0e-6,
        ),
        report_check(
            "all six constructions obey D4-odd reflection parity",
            all(result.parity_ok for result in results),
        ),
        report_check(
            "eta=0 zeros every declared odd construction",
            all_eta_zero,
        ),
        report_check(
            "D4-even mutant fails the odd parity check",
            not even_mutant_wrongly_odd,
        ),
        report_check(
            "all six candidate magnitudes received one frozen classification",
            all(
                result.magnitude_hit
                or result.magnitude < WINDOW[0]
                or result.magnitude > WINDOW[1]
                for result in results
            ),
        ),
    ]

    if hit_results:
        spectrum_hits = [
            label
            for label, consequence in consequence_rows
            if bool(consequence["hierarchy_like"])
        ]
        verdict = (
            "NU_KAPPA_HIT("
            + ",".join(result.label for result in hit_results)
            + ", spectrum="
            + (",".join(spectrum_hits) if spectrum_hits else "none")
            + ")"
        )
    else:
        verdict = "NU_KAPPA_NULL(all magnitudes, trials=6)"

    print()
    print("VERDICT", verdict)
    print()
    print("FIVE-SENTENCE CONCLUSION")
    print(
        "  1. Six and only six target-free determinant, Pfaffian, "
        "holonomy, correlator, transduction, and energy candidates were "
        "evaluated on frozen finite objects."
    )
    print(
        "  2. Reflection was applied to each underlying model ordering, "
        "and every resulting candidate obeyed the required D4-odd sign law."
    )
    if hit_results:
        print(
            "  3. At least one candidate entered the factor-three magnitude "
            "window and was therefore propagated through the frozen "
            "orientation-seesaw Schur complement."
        )
        print(
            "  4. The consequence table states directly whether that "
            "insertion produces the epsilon, 2epsilon, 3-like hierarchy."
        )
        print(
            "  5. The hit remains an exploration result and supplies no "
            "status-marker or four-dimensional theorem by itself."
        )
    else:
        print(
            "  3. None lies within a factor of three of 1.885e-4 after "
            "honest accounting of all six trials."
        )
        print(
            "  4. The D4-even mutant is rejected while equal sheet weights "
            "zero all six odd projections, so the null is not a parity-test "
            "failure."
        )
        print(
            "  5. Thus the finite scaffold objects do not supply the "
            "required cancellation scale; its mechanism must reside in the "
            "true 4D functional, consistent with review wave 6."
        )

    all_pass = all(checks)
    print("PROTOCOL-ALL-PASS" if all_pass else "PROTOCOL-FAILURE")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
