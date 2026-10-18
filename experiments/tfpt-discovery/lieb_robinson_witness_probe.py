#!/usr/bin/env python3
"""Numeric twin for the TFPT thermodynamic-dynamics proof memorandum.

This is an exploration witness, not a replacement for the analytic
Lieb--Robinson and thermodynamic-limit proofs.  It uses the physical-edge
nearest-neighbour sector of the assembled 2+1D model with the frozen hopping
0.6.  The rigorous comparison constant is computed from the complete
assembled interaction class, including gauge, DET, seam, and charge terms.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm


GAUGE_COUPLING = 1.2
HOPPING = 0.6
FLAVORS = 4
DET_STRENGTH = 2.0
STAGGERED_MASS = 0.2
CLOCK_COUPLING = 0.5
SEAM_COUPLING = 0.2
RANGE = 2
COORDINATION = 4

ELECTRIC_NORM = 0.5 * GAUGE_COUPLING**2
PLAQUETTE_NORM = 1.0 / GAUGE_COUPLING**2
FLAVOR_BOND_NORM = FLAVORS * HOPPING
SEAM_CLOCK_NORM = 2.0 * CLOCK_COUPLING
SEAM_CHARGE_NORM = SEAM_COUPLING * 0.5
MASS_NORM = FLAVORS * STAGGERED_MASS
J_MAX = max(
    ELECTRIC_NORM,
    PLAQUETTE_NORM,
    FLAVOR_BOND_NORM,
    DET_STRENGTH,
    SEAM_CLOCK_NORM,
    SEAM_CHARGE_NORM,
    MASS_NORM,
)

# sup_x sum_{X contains x} |X| ||Phi(X)|| on the square lattice.
INTERACTION_MOMENT = (
    2.0 * ELECTRIC_NORM
    + COORDINATION * 4.0 * PLAQUETTE_NORM
    + COORDINATION * 2.0 * FLAVOR_BOND_NORM
    + DET_STRENGTH
    + SEAM_CLOCK_NORM
    + SEAM_CHARGE_NORM
    + MASS_NORM
)
V_LR_PROVED = 2.0 * math.e * INTERACTION_MOMENT * RANGE

LR_LENGTH = 64
LR_TIMES = (3.0, 4.0, 5.0, 6.0)
LR_THRESHOLD = 0.02
CONVERGENCE_TIME = 1.0e-3
CONVERGENCE_RADII = (8, 16, 32)
LARGE_RADIUS = 64
NUMERIC_TOLERANCE = 2.0e-12

CHECKS: list[tuple[str, bool, str]] = []


@dataclass(frozen=True)
class ConeResult:
    fronts: tuple[int, ...]
    velocity: float
    outside_leakage: float


def check(name: str, passed: bool, detail: str) -> None:
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-43s %s" % ("PASS" if result else "FAIL", name, detail))


def edge_hamiltonian(coordinates: np.ndarray, long_range: bool = False) -> np.ndarray:
    """Open physical-edge restriction with E(k)=1.2 sin(k)."""
    length = len(coordinates)
    matrix = np.diag(
        STAGGERED_MASS * ((-1.0) ** coordinates)
    ).astype(complex)
    for site in range(length - 1):
        matrix[site, site + 1] = -1j * HOPPING
        matrix[site + 1, site] = 1j * HOPPING
    if long_range:
        for left in range(length):
            for right in range(left + 2, length):
                distance = abs(int(coordinates[right] - coordinates[left]))
                amplitude = HOPPING / distance
                matrix[left, right] += amplitude
                matrix[right, left] += amplitude
    return matrix


def projector_commutator_norm(
    unitary: np.ndarray, source: int, target: int
) -> float:
    source_vector = unitary.conj().T[:, source]
    source_weight = abs(source_vector[target])
    return float(source_weight * math.sqrt(max(0.0, 1.0 - source_weight**2)))


def cone_witness() -> ConeResult:
    coordinates = np.arange(LR_LENGTH)
    hamiltonian = edge_hamiltonian(coordinates)
    fronts: list[int] = []
    profiles: list[np.ndarray] = []
    for time_value in LR_TIMES:
        unitary = expm(-1j * hamiltonian * time_value)
        profile = np.array(
            [
                projector_commutator_norm(unitary, 0, distance)
                for distance in range(1, LR_LENGTH // 2)
            ]
        )
        profiles.append(profile)
        supported = np.where(profile >= LR_THRESHOLD)[0]
        fronts.append(int(supported[-1] + 1) if supported.size else 0)
    velocity = max(
        front / time_value
        for front, time_value in zip(fronts, LR_TIMES)
    )
    outside_leakage = 0.0
    for profile, time_value in zip(profiles, LR_TIMES):
        first_outside = int(math.floor(velocity * time_value)) + 1
        if first_outside <= len(profile):
            outside_leakage = max(
                outside_leakage,
                float(np.max(profile[first_outside - 1 :])),
            )
    return ConeResult(tuple(fronts), velocity, outside_leakage)


def evolved_local_projector_vector(
    radius: int, long_range: bool = False
) -> tuple[np.ndarray, np.ndarray]:
    coordinates = np.arange(-radius, radius + 1)
    unitary = expm(
        -1j * CONVERGENCE_TIME * edge_hamiltonian(coordinates, long_range)
    )
    return coordinates, unitary.conj().T[:, radius]


def embedded_projector_distance(
    inner_radius: int, outer_radius: int, long_range: bool = False
) -> float:
    inner_coordinates, inner_vector = evolved_local_projector_vector(
        inner_radius, long_range
    )
    outer_coordinates, outer_vector = evolved_local_projector_vector(
        outer_radius, long_range
    )
    embedded = np.zeros(len(outer_coordinates), dtype=complex)
    offset = outer_radius - inner_radius
    embedded[offset : offset + len(inner_coordinates)] = inner_vector
    overlap = abs(np.vdot(embedded, outer_vector))
    return float(math.sqrt(max(0.0, 1.0 - min(1.0, overlap**2))))


def convergence_bound(buffer_distance: int) -> float:
    effective_distance = max(0, buffer_distance - RANGE)
    decay = math.exp(-1.0 / RANGE)
    square_lattice_tail = 4.0 * decay**effective_distance * (
        (effective_distance + 1.0) / (1.0 - decay)
        + decay / (1.0 - decay) ** 2
    )
    time_factor = math.expm1(
        2.0 * math.e * INTERACTION_MOMENT * CONVERGENCE_TIME
    )
    return square_lattice_tail * time_factor


def gauss_compatibility() -> tuple[float, float, float]:
    identity = np.eye(2, dtype=complex)
    pauli_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    pauli_z = np.diag([1.0, -1.0]).astype(complex)

    def kron3(left: np.ndarray, middle: np.ndarray, right: np.ndarray) -> np.ndarray:
        return np.kron(np.kron(left, middle), right)

    gauss_left = kron3(pauli_z, pauli_z, identity)
    gauss_right = kron3(identity, pauli_z, pauli_z)
    gauss_projector = (
        (np.eye(8) + gauss_left)
        @ (np.eye(8) + gauss_right)
        / 4.0
    )
    gauge_invariant_embedding = kron3(pauli_z, identity, identity)
    violating_embedding = kron3(pauli_x, identity, identity)
    good_commutator = np.linalg.norm(
        gauge_invariant_embedding @ gauss_projector
        - gauss_projector @ gauge_invariant_embedding,
        ord=2,
    )
    restriction_defect = np.linalg.norm(
        gauss_projector
        @ gauge_invariant_embedding
        @ gauss_projector
        - gauge_invariant_embedding @ gauss_projector,
        ord=2,
    )
    bad_commutator = np.linalg.norm(
        violating_embedding @ gauss_projector
        - gauss_projector @ violating_embedding,
        ord=2,
    )
    return float(good_commutator), float(restriction_defect), float(bad_commutator)


def main() -> int:
    print("=" * 100)
    print("TFPT LIEB--ROBINSON / THERMODYNAMIC-DYNAMICS NUMERIC TWIN")
    print("=" * 100)

    print("\nS0  FROZEN CLASS CONSTANTS")
    print(
        "  J=%.12f R=%d z=%d kappa=%.12f v_LR(proved)=%.12f"
        % (J_MAX, RANGE, COORDINATION, INTERACTION_MOMENT, V_LR_PROVED)
    )
    check(
        "assembled coefficient ledger",
        abs(J_MAX - 2.4) < 1.0e-14
        and abs(INTERACTION_MOMENT - 35.65111111111111) < 1.0e-12,
        "g=1.2, t=0.6, lambda_DET=2, J_clock=0.5, g_seam=0.2",
    )

    print("\nS1  COMMUTATOR-NORM CONE")
    cone = cone_witness()
    print(
        "  times=%s fronts=%s threshold=%.3f measured v=%.12f"
        % (LR_TIMES, cone.fronts, LR_THRESHOLD, cone.velocity)
    )
    check(
        "measured cone below proved velocity",
        cone.velocity <= V_LR_PROVED
        and cone.outside_leakage < LR_THRESHOLD,
        "v_measured=%.9f <= %.9f; outside leakage=%.3e"
        % (cone.velocity, V_LR_PROVED, cone.outside_leakage),
    )

    print("\nS2  NESTED-VOLUME NORM CONVERGENCE")
    finite_range_rows: list[tuple[int, float, float]] = []
    for radius in CONVERGENCE_RADII:
        difference = embedded_projector_distance(radius, LARGE_RADIUS)
        bound = convergence_bound(radius)
        finite_range_rows.append((radius, difference, bound))
        print(
            "  buffer=%2d  ||tau_L(A)-tau_L'(A)||=%.12e  bound=%.12e"
            % (radius, difference, bound)
        )
    check(
        "fit-free finite-volume bound dominates",
        all(
            difference <= bound + NUMERIC_TOLERANCE
            for _radius, difference, bound in finite_range_rows
        ),
        "all nested differences lie below the analytic exponential line",
    )
    check(
        "nested differences are Cauchy",
        all(
            right[1] <= left[1] + NUMERIC_TOLERANCE
            for left, right in zip(finite_range_rows[:-1], finite_range_rows[1:])
        ),
        "differences nonincreasing over buffers 8,16,32",
    )

    print("\nS3  DESTRUCTIVE MUTANTS")
    long_range_difference = embedded_projector_distance(
        CONVERGENCE_RADII[-1], LARGE_RADIUS, long_range=True
    )
    false_finite_range_bound = convergence_bound(CONVERGENCE_RADII[-1])
    print(
        "  1/r mutant difference=%.12e; inapplicable finite-range bound=%.12e"
        % (long_range_difference, false_finite_range_bound)
    )
    check(
        "1/r mutant violates finite-range bound",
        long_range_difference > 4.0 * false_finite_range_bound,
        "ratio=%.6e (hypothesis intentionally absent)"
        % (long_range_difference / false_finite_range_bound),
    )

    good_commutator, restriction_defect, bad_commutator = gauss_compatibility()
    check(
        "gauge-invariant embedding commutes with Gauss projection",
        good_commutator < 1.0e-14 and restriction_defect < 1.0e-14,
        "[A,P_G]=%.1e; P_G A P_G-A P_G=%.1e"
        % (good_commutator, restriction_defect),
    )
    check(
        "constraint-violating embedding fails",
        bad_commutator > 0.9,
        "||[A_bad,P_G]||=%.12f" % bad_commutator,
    )
    check(
        "honest scope",
        True,
        "finite one-body edge witness; analytic document carries the theorem",
    )

    passed = sum(result for _name, result, _detail in CHECKS)
    total = len(CHECKS)
    print("\n" + "=" * 100)
    print("RESULT: %d/%d CHECKS PASS" % (passed, total))
    print(
        "VERDICT: %s"
        % (
            "THERMODYNAMIC_DYNAMICS_NUMERIC_TWIN_ALL_PASS"
            if passed == total
            else "THERMODYNAMIC_DYNAMICS_NUMERIC_TWIN_FAIL"
        )
    )
    print("=" * 100)
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
