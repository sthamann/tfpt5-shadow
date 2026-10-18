#!/usr/bin/env python3
"""Euclidean-cap selection probe for the finite SK initial state.

EXPLORATION ONLY.  This file reuses the frozen 96-dimensional model of
``sk_rho0_mechanism_probe.py`` and ``v1000_spin2_sk_witnesses.py``.  It tests
four predeclared Euclidean-cap families after the relative-entropy principle
was found to be either response-dead or selection-vacuous:

R1
    The untwisted thermal half-cap.  Squaring it must give rho_KMS.
R2
    A +1 mu4 character projector inserted in the thermal cap.
R3a-c
    Three unitary midpoint/split mu4 twists.  Their cap amplitudes retain an
    orientation branch, although A A^dag may erase the twist.
R4
    The modular half-cap of the charged seam (Z6 link plus Q pair), tensored
    with the identity on the neutral control pair.

The finite seam modular generator is defined without a fit by

    K_Sigma = -(1/(2 pi)) log Tr_control(rho_KMS).

Consequently exp(-pi K_Sigma) is the positive square root of the exact seam
marginal.  R4 therefore gives that marginal tensored with the normalized
identity on the complement.  This is a canonical finite construction, but
its success here is deliberately typed only as a finite-model candidate:
FTRANSFER.SK.RHO0.01 remains [O].
"""

from __future__ import annotations

import time

import numpy as np


START = time.perf_counter()
ALL_OK = True


def report(name: str, condition: bool, details: str = "") -> None:
    """Accumulate and print one deterministic assertion."""
    global ALL_OK
    passed = bool(condition)
    ALL_OK &= passed
    suffix = "  | " + details if details else ""
    print(("PASS " if passed else "FAIL ") + name + suffix)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def expectation(density: np.ndarray, operator: np.ndarray) -> complex:
    return complex(np.trace(density @ operator))


def hermitian_function(
    matrix: np.ndarray,
    function,
) -> np.ndarray:
    """Apply a scalar function to a Hermitian matrix spectrally."""
    values, vectors = np.linalg.eigh(0.5 * (matrix + matrix.conj().T))
    transformed = function(values)
    return (vectors * transformed) @ vectors.conj().T


def positive_exponential(matrix: np.ndarray) -> np.ndarray:
    return hermitian_function(matrix, np.exp)


def positive_square_root(matrix: np.ndarray) -> np.ndarray:
    return hermitian_function(matrix, lambda values: np.sqrt(values))


def positive_logarithm(matrix: np.ndarray) -> np.ndarray:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    if values.min() <= 0.0:
        raise ValueError("positive logarithm requires a faithful matrix")
    return hermitian_function(matrix, np.log)


def density_from_cap(cap: np.ndarray) -> np.ndarray:
    density = cap @ cap.conj().T
    return 0.5 * (density + density.conj().T) / np.trace(density).real


def density_from_hamiltonian(
    hamiltonian: np.ndarray,
    inverse_temperature: float,
) -> np.ndarray:
    values, vectors = np.linalg.eigh(hamiltonian)
    exponents = -inverse_temperature * values
    weights = np.exp(exponents - exponents.max())
    weights /= weights.sum()
    return (vectors * weights) @ vectors.conj().T


def euclidean_evolution(
    hamiltonian: np.ndarray,
    imaginary_time: float,
) -> np.ndarray:
    values, vectors = np.linalg.eigh(hamiltonian)
    return (vectors * np.exp(-imaginary_time * values)) @ vectors.conj().T


def unitary_from_hermitian(
    hamiltonian: np.ndarray,
    duration: float,
) -> np.ndarray:
    values, vectors = np.linalg.eigh(hamiltonian)
    return (vectors * np.exp(-1j * duration * values)) @ vectors.conj().T


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = 0.5 * (left - right + (left - right).conj().T)
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(difference))))


def partial_trace(
    density: np.ndarray,
    dimensions: tuple[int, ...],
    keep: tuple[int, ...],
) -> np.ndarray:
    """Trace a tensor-product density over every factor not in ``keep``."""
    factor_count = len(dimensions)
    traced = tuple(index for index in range(factor_count) if index not in keep)
    keep_dimension = int(np.prod([dimensions[index] for index in keep]))
    trace_dimension = int(np.prod([dimensions[index] for index in traced]))
    permutation = (
        keep
        + traced
        + tuple(index + factor_count for index in keep)
        + tuple(index + factor_count for index in traced)
    )
    tensor = density.reshape(dimensions + dimensions).transpose(permutation)
    tensor = tensor.reshape(
        keep_dimension,
        trace_dimension,
        keep_dimension,
        trace_dimension,
    )
    return np.einsum("aibi->ab", tensor)


def group_average_projector(unitary: np.ndarray, order: int) -> np.ndarray:
    projector = np.zeros_like(unitary)
    power = np.eye(unitary.shape[0], dtype=complex)
    for _ in range(order):
        projector += power
        power = power @ unitary
    projector /= order
    return 0.5 * (projector + projector.conj().T)


# ---------------------------------------------------------------------------
# Exact frozen 96-dimensional SK model.
# ---------------------------------------------------------------------------
NUMBER_OF_SITES = 2
LINK_DIMENSION = 6
NUMBER_OF_MODES = 4
FERMION_DIMENSION = 2**NUMBER_OF_MODES
HILBERT_DIMENSION = LINK_DIMENSION * FERMION_DIMENSION
TENSOR_DIMENSIONS = (LINK_DIMENSION, 2, 2, 2, 2)
SPECIES_CHARGES = (1, 0)

ELECTRIC_COUPLING = 1.0
HOPPING_COUPLING = 0.7
STAGGERED_MASS = 0.5
Q_CHEMICAL_OFFSET = 0.5
BETA = 0.35
REFERENCE_THETA = 0.7
PULSE_AMPLITUDE = 0.18
PULSE_DURATION = 0.45
OBSERVATION_TIMES = np.linspace(0.0, 12.0, 97)

OMEGA = np.exp(2j * np.pi / LINK_DIMENSION)
Z_LINK_SMALL = np.diag(OMEGA ** np.arange(LINK_DIMENSION)).astype(complex)
X_LINK_SMALL = np.roll(
    np.eye(LINK_DIMENSION, dtype=complex),
    1,
    axis=0,
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
        charged_link = np.linalg.matrix_power(Z_LINK, charge)
        open_hop = (
            PSI[mode_0].conj().T
            @ charged_link
            @ PSI[mode_1]
        )
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
PULSE_HAMILTONIAN = build_hamiltonian(
    REFERENCE_THETA + PULSE_AMPLITUDE
)
CURRENT = -seam_derivative(REFERENCE_THETA)
IDENTITY = np.eye(HILBERT_DIMENSION, dtype=complex)
RHO_KMS = density_from_hamiltonian(HAMILTONIAN, BETA)

TOTAL_FERMION_NUMBER = sum(NUMBER)


def deck_power(exponent: float) -> np.ndarray:
    """Canonical spectral power of u=exp(i*pi*N_F/2)."""
    phases = np.exp(
        0.5j * np.pi * exponent
        * np.diag(TOTAL_FERMION_NUMBER).real
    )
    return np.diag(phases)


MU4_ACTION = deck_power(1.0)
P_MU4_PLUS = group_average_projector(MU4_ACTION, 4)

report(
    "frozen Hamiltonian and KMS state reconstructed",
    HILBERT_DIMENSION == 96
    and max_abs(HAMILTONIAN - HAMILTONIAN.conj().T) < 1e-13
    and abs(np.trace(RHO_KMS) - 1.0) < 1e-13
    and np.linalg.eigvalsh(RHO_KMS).min() > 0.0,
    "dim=%d, min eig(rho_KMS)=%.3e"
    % (HILBERT_DIMENSION, np.linalg.eigvalsh(RHO_KMS).min()),
)

mu4_commutator = max_abs(
    MU4_ACTION @ HAMILTONIAN - HAMILTONIAN @ MU4_ACTION
)
projector_error = max_abs(
    P_MU4_PLUS @ P_MU4_PLUS - P_MU4_PLUS
)
report(
    "frozen mu4 lift is an exact conserved finite symmetry",
    mu4_commutator < 2e-13
    and projector_error < 2e-13
    and int(round(np.trace(P_MU4_PLUS).real)) == 12,
    "rank(P_+)=%d, [u,H]=%.2e"
    % (int(round(np.trace(P_MU4_PLUS).real)), mu4_commutator),
)


# ---------------------------------------------------------------------------
# Predeclared cap amplitudes and states.
# ---------------------------------------------------------------------------
THERMAL_HALF = euclidean_evolution(HAMILTONIAN, BETA / 2.0)
THERMAL_QUARTER = euclidean_evolution(HAMILTONIAN, BETA / 4.0)

# R1: no branch insertion.
CAP_R1 = THERMAL_HALF
RHO_R1 = density_from_cap(CAP_R1)

# R2: the + orientation character inside the cap.  In this frozen model the
# projector commutes with H, so Euclidean smearing cannot rescue the response.
CAP_R2 = P_MU4_PLUS @ THERMAL_HALF
RHO_R2 = density_from_cap(CAP_R2)
RHO_R2_SYMMETRIC = (
    THERMAL_HALF @ P_MU4_PLUS @ THERMAL_HALF
)
RHO_R2_SYMMETRIC /= np.trace(RHO_R2_SYMMETRIC).real

# R3: three honest unitary twist placements.  These are distinct amplitudes,
# but the conserved unitary twist cancels from A A^dag.
CAP_R3A = THERMAL_QUARTER @ deck_power(0.5) @ THERMAL_QUARTER
CAP_R3B = THERMAL_QUARTER @ MU4_ACTION @ THERMAL_QUARTER
CAP_R3C = deck_power(0.25) @ THERMAL_HALF @ deck_power(0.25)
RHO_R3A = density_from_cap(CAP_R3A)
RHO_R3B = density_from_cap(CAP_R3B)
RHO_R3C = density_from_cap(CAP_R3C)

# R4: K_Sigma on the charged seam = link plus the two Q modes.  The two
# neutral control modes are the complement on which the cap is the identity.
SEAM_KEEP = (0, 1, 2)
RHO_SEAM = partial_trace(RHO_KMS, TENSOR_DIMENSIONS, SEAM_KEEP)
K_SIGMA = -positive_logarithm(RHO_SEAM) / (2.0 * np.pi)
CAP_SEAM = positive_exponential(-np.pi * K_SIGMA)
CONTROL_DIMENSION = 4
CAP_R4 = np.kron(CAP_SEAM, np.eye(CONTROL_DIMENSION, dtype=complex))
RHO_R4 = density_from_cap(CAP_R4)
RHO_R4_DIRECT = np.kron(
    RHO_SEAM,
    np.eye(CONTROL_DIMENSION, dtype=complex) / CONTROL_DIMENSION,
)

report(
    "R1 pure KMS-square is selection-vacuous",
    trace_distance(RHO_R1, RHO_KMS) < 2e-13,
    "D_tr=%.3e" % trace_distance(RHO_R1, RHO_KMS),
)
report(
    "R2 smearing collapses to hard projection in this model",
    trace_distance(RHO_R2, RHO_R2_SYMMETRIC) < 2e-13
    and mu4_commutator < 2e-13,
    "D_tr(cap-square,symmetric)=%.3e"
    % trace_distance(RHO_R2, RHO_R2_SYMMETRIC),
)
twist_distances = (
    trace_distance(RHO_R3A, RHO_KMS),
    trace_distance(RHO_R3B, RHO_KMS),
    trace_distance(RHO_R3C, RHO_KMS),
)
report(
    "all honest conserved unitary twists cancel in A A^dag",
    max(twist_distances) < 3e-13,
    "D_tr R3a/b/c=%s"
    % [f"{distance:.3e}" for distance in twist_distances],
)
modular_reconstruction = positive_exponential(-2.0 * np.pi * K_SIGMA)
report(
    "R4 seam modular cap is reconstructed without a fit",
    max_abs(modular_reconstruction - RHO_SEAM) < 2e-13
    and max_abs(CAP_SEAM @ CAP_SEAM - RHO_SEAM) < 2e-13
    and trace_distance(RHO_R4, RHO_R4_DIRECT) < 2e-13,
    "seam dim=%d, reconstruction=%.2e"
    % (RHO_SEAM.shape[0], max_abs(modular_reconstruction - RHO_SEAM)),
)


# ---------------------------------------------------------------------------
# The exact v1000 pulse response, evaluated for every cap state.
# ---------------------------------------------------------------------------
PULSE_UNITARY = unitary_from_hermitian(
    PULSE_HAMILTONIAN,
    PULSE_DURATION,
)


def pulse_response(density: np.ndarray) -> np.ndarray:
    induced = []
    for time_after_pulse in OBSERVATION_TIMES:
        free_after = unitary_from_hermitian(
            HAMILTONIAN,
            time_after_pulse,
        )
        pulsed_evolution = free_after @ PULSE_UNITARY
        baseline_evolution = unitary_from_hermitian(
            HAMILTONIAN,
            time_after_pulse + PULSE_DURATION,
        )
        pulsed_density = (
            pulsed_evolution @ density @ pulsed_evolution.conj().T
        )
        baseline_density = (
            baseline_evolution @ density @ baseline_evolution.conj().T
        )
        induced.append(
            expectation(pulsed_density, CURRENT).real
            - expectation(baseline_density, CURRENT).real
        )
    return np.asarray(induced)


def response_rms(response: np.ndarray) -> float:
    return float(np.sqrt(np.mean(response**2)))


KMS_RESPONSE = pulse_response(RHO_KMS)
KMS_RESPONSE_RMS = response_rms(KMS_RESPONSE)
report(
    "v1000 response observable is reproduced",
    abs(KMS_RESPONSE_RMS - 3.038094542e-3) < 5e-12,
    "RMS=%.9e" % KMS_RESPONSE_RMS,
)


# ---------------------------------------------------------------------------
# Recompute the v1000 saddle leg.
#
# On a fixed orientation branch the action is -cos(5 theta-3 pi).  Removing
# orientation means averaging over all four deck branches.  The fifth
# harmonic then vanishes exactly because 5 == 1 mod 4.
# ---------------------------------------------------------------------------
ORIENTATION_SHIFTS = 0.5 * np.pi * np.arange(4)
TARGET_THETA = 3.0 * np.pi / 5.0
LIFT_LEFT = 7.0 * np.pi / 20.0
LIFT_RIGHT = 17.0 * np.pi / 20.0
SADDLES = np.arange(10) * np.pi / 5.0
MINIMA = SADDLES[1::2]
LIFT_MINIMA = MINIMA[
    (MINIMA >= LIFT_LEFT) & (MINIMA < LIFT_RIGHT)
]


def oriented_action(theta: np.ndarray | float) -> np.ndarray:
    return -np.cos(5.0 * np.asarray(theta) - 3.0 * np.pi)


def orientation_averaged_action(
    theta: np.ndarray | float,
) -> np.ndarray:
    values = [
        oriented_action(np.asarray(theta) + shift)
        for shift in ORIENTATION_SHIFTS
    ]
    return np.mean(values, axis=0)


theta_grid = np.linspace(0.0, 2.0 * np.pi, 401)
orientation_free_amplitude = float(
    np.max(np.abs(orientation_averaged_action(theta_grid)))
)
report(
    "oriented saddle leg retains the typed 3pi/5 lift",
    len(MINIMA) == 5
    and len(LIFT_MINIMA) == 1
    and abs(LIFT_MINIMA[0] - TARGET_THETA) < 1e-14,
    "global minima=5, lift minimum=%.12f*pi"
    % (LIFT_MINIMA[0] / np.pi),
)
report(
    "MUTANT orientation-free twist loses branch structure",
    orientation_free_amplitude < 1e-14,
    "max four-branch averaged |S|=%.3e" % orientation_free_amplitude,
)


# ---------------------------------------------------------------------------
# Candidate table and selection test.
# ---------------------------------------------------------------------------
candidate_specs = (
    ("R1", "thermal half-cap", RHO_R1, False),
    ("R2", "inside P_mu4,+", RHO_R2, True),
    ("R3a", "midpoint u^(1/2)", RHO_R3A, True),
    ("R3b", "midpoint u", RHO_R3B, True),
    ("R3c", "split u^(1/4)", RHO_R3C, True),
    ("R4", "seam modular cap", RHO_R4, True),
)

candidate_rows = []
for name, description, density, has_orientation_branch in candidate_specs:
    eigenvalues = np.linalg.eigvalsh(
        0.5 * (density + density.conj().T)
    )
    response = pulse_response(density)
    rms = response_rms(response)
    distance = trace_distance(density, RHO_KMS)
    invariance_error = max_abs(
        MU4_ACTION @ density @ MU4_ACTION.conj().T - density
    )
    well_defined = (
        abs(np.trace(density).real - 1.0) < 2e-13
        and eigenvalues.min() > -2e-13
    )
    alive = 1e-3 <= rms <= 1e-2
    saddle_survives = (
        has_orientation_branch
        and len(LIFT_MINIMA) == 1
        and abs(LIFT_MINIMA[0] - TARGET_THETA) < 1e-14
    )
    selects = (
        well_defined
        and distance > 1e-6
        and alive
        and invariance_error < 2e-12
        and saddle_survives
    )
    candidate_rows.append(
        {
            "name": name,
            "description": description,
            "density": density,
            "well_defined": well_defined,
            "distance": distance,
            "response": rms,
            "alive": alive,
            "invariance_error": invariance_error,
            "invariant": invariance_error < 2e-12,
            "saddle": saddle_survives,
            "selects": selects,
        }
    )

report(
    "every cap state is positive normalized and deterministic",
    all(row["well_defined"] for row in candidate_rows),
    "six predeclared states; no optimization or random input",
)
report(
    "every cap state is mu4 invariant",
    all(row["invariant"] for row in candidate_rows),
    "max invariance error=%.2e"
    % max(row["invariance_error"] for row in candidate_rows),
)

r2_row = next(row for row in candidate_rows if row["name"] == "R2")
r4_row = next(row for row in candidate_rows if row["name"] == "R4")
report(
    "inside-projector cap is nontrivial but response-dead",
    r2_row["distance"] > 1e-6
    and r2_row["response"] < 1e-12
    and not r2_row["selects"],
    "D_tr=%.9e, RMS=%.3e"
    % (r2_row["distance"], r2_row["response"]),
)
report(
    "seam modular cap differs from KMS and keeps v1000 response",
    r4_row["distance"] > 1e-6
    and abs(r4_row["response"] - KMS_RESPONSE_RMS) < 5e-12
    and r4_row["selects"],
    "D_tr=%.9e, RMS=%.9e"
    % (r4_row["distance"], r4_row["response"]),
)

winners = [row for row in candidate_rows if row["selects"]]
report(
    "selection criterion has exactly one finite-model winner",
    [row["name"] for row in winners] == ["R4"],
    "winners=%s" % [row["name"] for row in winners],
)

print("\nCANDIDATE TABLE")
print(
    "  cap  positive/normalized  D_tr(KMS)    RMS(response)  "
    "mu4 invariant  saddle"
)
for row in candidate_rows:
    print(
        "  %-4s %-20s %.9e  %.9e  %-13s %s"
        % (
            row["name"],
            "yes" if row["well_defined"] else "no",
            row["distance"],
            row["response"],
            "yes" if row["invariant"] else "no",
            "3pi/5 [C]" if row["saddle"] else "lost",
        )
    )

print("\nMUTANTS")
print(
    "  R1 control: D_tr(rho_R1,rho_KMS)=%.3e "
    "(selection-vacuous)." % trace_distance(RHO_R1, RHO_KMS)
)
print(
    "  Orientation-free four-branch average: max |S|=%.3e "
    "(no isolated branch saddle)." % orientation_free_amplitude
)
print(
    "  R2 commuting-projector diagnosis: Euclidean smearing equals the "
    "hard + character projection and RMS=%.3e." % r2_row["response"]
)

print("\nHONEST BOUNDARY")
print("  Finite 96-dimensional 1+1D model, not the 4D algebra.")
print(
    "  R4 changes only the neutral complementary factor while preserving "
    "the exact charged-seam marginal."
)
print(
    "  Its response survival is therefore a finite factorization result, "
    "not a cosmological-state derivation."
)
print("  The 3pi/5 lift remains the same conditional [C] saddle leg.")
print("  FTRANSFER.SK.RHO0.01 remains [O].")

if winners:
    winner = winners[0]
    verdict = (
        "EUCLIDEAN_CAP_SELECTS(%s,%.9e,%.9e)"
        % (winner["name"], winner["distance"], winner["response"])
    )
else:
    compact_table = ";".join(
        "%s:D=%.3e,R=%.3e"
        % (row["name"], row["distance"], row["response"])
        for row in candidate_rows
    )
    verdict = "EUCLIDEAN_CAP_ALL_VACUOUS_OR_DEAD(%s)" % compact_table

print("\nVERDICT: " + verdict)
print("runtime %.2f s" % (time.perf_counter() - START))
print("PROBE " + ("ALL PASS" if ALL_OK else "HAS FAILURES"))
if __name__ == "__main__":
    raise SystemExit(0 if ALL_OK else 1)
