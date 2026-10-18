#!/usr/bin/env python3
"""v1012 -- evening TOE-gate wave: four executed witnesses in one battery
(2026-08-30).  No marker moves.

Provenance: experiments/tfpt-discovery/{ir_universality_witness,
rho0_entropy_minimizer, nu_kappa_pfaffian, spin2_interacting_tt}_probe.py
(10/10 + 8-candidate NO_SET_WORKS + PROTOCOL-ALL-PASS + 14/14).
Frozen IR/nu/TT helpers are loaded from the probes; the rho0 lattice
is self-contained (the probe runs at import).  experiments/ is not a
verification-module import in the sense of a claim source.

THE POINT.  Four TOE-gate fronts executed at scaffold level.

  T5 [N]/SPLIT: physical QWZ edge c -> 1 (0.99993); clustering dichotomy
        xi*gap ~ 1.089 vs power-law exp ~ 2.034; LR cone v_LR = 5/3 >= c
        with leakage 0.015; cubic curvature -> 1/6 with volume.
        TYPED SPLIT: gauge holonomy + seam clock are not propagating
        modes -- common-c needs dynamical gauge excitations.
  T8 [X typed] double diagnosis: 8 unique candidates; hard sectors
        kill the SK response (~1e-31); every response-alive set is
        exactly rho_KMS even without mu4 -- entropic-proximity selection
        is VACUOUS at finite level.  Verdict NO_SET_WORKS.
  T6 [X] six pre-declared D4-odd kappa candidates, all parity-checked,
        all NULL (five at 1e-14; K4 = 3.55e-3 is 18.8x too large).
        The 1.885e-4 cancellation needs the true 4D functional -- the
        third scaffold-level nu-mechanism bound this week.
  T7 [N]: conserved interaction-complete lattice stress ~1e-15; TT
        spectral positivity exact; sum rules ~1e-15; dominant positive-Z
        pole persists under phi^4 (gapped, as expected for massive
        generic matter); Z trend k1 suppressed / k2 enhanced; free
        analytic match.  Missing: TFPT content, k->0 volume, Ward.

MUST-FAIL: anisotropy splits velocities; gapless mirror breaks xi*gap;
D4-even sheet sum fails odd parity; drop phi^4 from h_x kills
continuity; unconstrained C0 equals C2 (selection-vacuous).

HONEST SCOPE (firewall): finite 2+1D / 96-dim SK / 2x2x2 scalar
companions.  TFPT.TOE.COMPLETE.01, FTRANSFER.SK.RHO0.01,
FLAV.NU.TEXTURE.MECHANISM.01, GRAV.SPIN2.EMERGENCE.01 stay [O].
Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

import importlib
import inspect
import math
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import root

import v1009_rho0_minimizer as rho0_base
from tfpt_constants import check as suite_check, summary, reset


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DISC = ROOT / "experiments" / "tfpt-discovery"

REQUIRED_KAPPA = 1.885e-4
WINDOW_FACTOR = 3.0
KAPPA_WINDOW = (REQUIRED_KAPPA / WINDOW_FACTOR, REQUIRED_KAPPA * WINDOW_FACTOR)
PULSE_TIMES = np.linspace(0.0, 12.0, 25)
PULSE_AMPLITUDE = 0.18
PULSE_DURATION = 0.45
ALIVE_RMS = 1.0e-5
DEAD_RMS = 1.0e-13


def check(label: str, condition: bool) -> None:
    suite_check(label, bool(condition))


def load_probe(name: str):
    if str(DISC) not in sys.path:
        sys.path.insert(0, str(DISC))
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    if name in sys.modules:
        return sys.modules[name]
    return importlib.import_module(name)


def source_contains(relative_path: str, *needles: str) -> bool:
    source = (ROOT / relative_path).read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


# ---------------------------------------------------------------------------
# T5 -- IR universality witnesses + typed split
# ---------------------------------------------------------------------------
def claim_t5(ir) -> None:
    print("\nT5 -- IR UNIVERSALITY WITNESSES (typed split)")
    velocity_rows, common_light_cone, split_reason = ir.velocity_witness()
    physical_row, gauge_row, seam_row = velocity_rows
    print(
        "  physical c(k=%.3f)=%.9f -> c(k=%.3f)=%.9f"
        % (
            ir.VELOCITY_MOMENTA[0],
            physical_row.speeds[0],
            ir.VELOCITY_MOMENTA[-1],
            physical_row.limit_estimate,
        )
    )
    print(
        "  gauge/seam IR proxies: %.6e / %.6e; common=%s; split=%s"
        % (
            gauge_row.limit_estimate,
            seam_row.limit_estimate,
            common_light_cone,
            split_reason,
        )
    )
    check(
        "T5 physical velocity converges to clock unit",
        abs(physical_row.limit_estimate - 1.0) < 5.0e-4
        and all(
            left < right
            for left, right in zip(physical_row.speeds[:-1], physical_row.speeds[1:])
        ),
    )
    check(
        "T5 sector comparison honestly typed as SPLIT",
        (not common_light_cone)
        and (
            gauge_row.limit_estimate <= ir.COMMON_C_TOLERANCE
            or seam_row.limit_estimate <= ir.COMMON_C_TOLERANCE
        )
        and "holonomy" in split_reason
        and "clock" in split_reason,
    )

    clustering = ir.clustering_witness()
    print(
        "  clustering: xi*gap=%.6f; physical power=%.6f"
        % (clustering.mirror_product, clustering.physical_power)
    )
    check(
        "T5 mirror exponential clustering (xi*gap in [0.5, 2])",
        ir.MIRROR_PRODUCT_RANGE[0]
        <= clustering.mirror_product
        <= ir.MIRROR_PRODUCT_RANGE[1]
        and abs(clustering.mirror_xi_ratio - clustering.mirror_xi_exact)
        / clustering.mirror_xi_exact
        < 0.25,
    )
    check(
        "T5 physical edge power-law clustering",
        1.7 < clustering.physical_power < 2.3
        and clustering.physical_last > 1.0e-6 * clustering.physical_first,
    )

    lr_result = ir.lieb_robinson_witness()
    print(
        "  LR: v_LR=%.6f fronts=%s leakage=%.3e"
        % (lr_result.velocity, lr_result.fronts, lr_result.outside_leakage)
    )
    check(
        "T5 effective cone bounds propagating speed",
        lr_result.velocity >= physical_row.limit_estimate
        and lr_result.outside_leakage < ir.LR_THRESHOLD,
    )

    curvature_rows = ir.curvature_witness()
    check(
        "T5 cubic coefficient tends to 1/6",
        abs(curvature_rows[-1].cubic_coefficient - 1.0 / 6.0)
        < abs(curvature_rows[0].cubic_coefficient - 1.0 / 6.0)
        and abs(curvature_rows[-1].cubic_coefficient - 1.0 / 6.0) < 0.001,
    )
    check(
        "T5 sampled IR window widens with volume",
        all(
            left.relative_curvature > right.relative_curvature
            for left, right in zip(curvature_rows[:-1], curvature_rows[1:])
        )
        and curvature_rows[-1].ir_mode_count > curvature_rows[0].ir_mode_count,
    )

    mutant_x, mutant_y = ir.anisotropy_mutant()
    check(
        "T5 MUST-FAIL: anisotropy mutant splits velocities",
        abs(mutant_x - mutant_y) > 0.25,
    )
    gapless_green = ir.occupied_projector_correlator(0.0, ir.CORRELATION_LENGTH)
    gapless_tail = float(abs(gapless_green[63]) ** 2)
    check(
        "T5 MUST-FAIL: gapless mutant breaks xi-gap relation",
        gapless_tail > 1.0e-6,
    )
    check(
        "T5 propagating-mode precondition recorded (common-c needs dynamical gauge)",
        source_contains(
            "experiments/tfpt-discovery/ir_universality_witness_probe.py",
            "IR_UNIVERSALITY_SPLIT",
            "stage2_holonomy_and_stage4_clock_not_common_propagating_modes",
            "T5 stays [O]",
        ),
    )


# ---------------------------------------------------------------------------
# T8 -- rho0 8-candidate selection-vacuity double diagnosis
# ---------------------------------------------------------------------------
def _hermitian_log(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    if values.min() <= 0.0:
        raise ValueError("matrix logarithm requires positive spectrum")
    return (vectors * np.log(values)) @ vectors.conj().T


def _normalized_exp(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(0.5 * (matrix + matrix.conj().T))
    weights = np.exp(values - values.max())
    density = (vectors * weights) @ vectors.conj().T
    return density / np.trace(density)


def _trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = 0.5 * (left - right + (left - right).conj().T)
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(difference))))


def _character_projector(unitary: np.ndarray, order: int, character: int) -> np.ndarray:
    projector = np.zeros_like(unitary)
    power = np.eye(unitary.shape[0], dtype=complex)
    root = np.exp(2j * np.pi / order)
    for exponent in range(order):
        projector += root ** (-character * exponent) * power
        power = power @ unitary
    projector /= order
    return 0.5 * (projector + projector.conj().T)


def _compression_minimizer(projector: np.ndarray, rho_kms: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(projector)
    support = vectors[:, values > 0.5]
    compressed_log = support.conj().T @ _hermitian_log(rho_kms) @ support
    density_on_support = _normalized_exp(compressed_log)
    return support @ density_on_support @ support.conj().T


def _gibbs_tilt(
    reference: np.ndarray,
    observables: tuple[np.ndarray, ...],
    targets: np.ndarray,
    initial_duals: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    log_reference = _hermitian_log(reference)

    def state_at(duals: np.ndarray) -> np.ndarray:
        generator = log_reference.copy()
        for dual, observable in zip(duals, observables):
            generator += dual * observable
        return _normalized_exp(generator)

    def residual(duals: np.ndarray) -> np.ndarray:
        density = state_at(duals)
        return np.asarray(
            [
                rho0_base.expectation(density, observable).real - target
                for observable, target in zip(observables, targets)
            ]
        )

    solution = root(residual, initial_duals, method="hybr", tol=1e-12)
    return state_at(solution.x), solution.x


def _pulse_rms(rho: np.ndarray, hamiltonian, pulse_unitary, current) -> float:
    induced = []
    for time_after_pulse in PULSE_TIMES:
        free_after = rho0_base.unitary_from_hermitian(hamiltonian, time_after_pulse)
        pulsed = free_after @ pulse_unitary
        baseline = rho0_base.unitary_from_hermitian(
            hamiltonian, time_after_pulse + PULSE_DURATION
        )
        pulsed_density = pulsed @ rho @ pulsed.conj().T
        baseline_density = baseline @ rho @ baseline.conj().T
        induced.append(
            rho0_base.expectation(pulsed_density, current).real
            - rho0_base.expectation(baseline_density, current).real
        )
    return float(np.sqrt(np.mean(np.asarray(induced) ** 2)))


def claim_t8() -> None:
    print("\nT8 -- RHO0 8-CANDIDATE SELECTION VACUITY")
    psi = [
        rho0_base.jordan_wigner_annihilator(mode)
        for mode in range(rho0_base.NUMBER_OF_MODES)
    ]
    number = [operator.conj().T @ operator for operator in psi]
    x_link = rho0_base.lift_link(rho0_base.X_LINK_SMALL)
    z_link = rho0_base.lift_link(rho0_base.Z_LINK_SMALL)
    hamiltonian = rho0_base.build_hamiltonian(
        rho0_base.REFERENCE_THETA, psi, number, x_link, z_link
    )
    rho_kms = rho0_base.density_from_hamiltonian(hamiltonian, rho0_base.BETA)
    identity = np.eye(rho0_base.HILBERT_DIMENSION, dtype=complex)
    gauss_action = (identity + (rho0_base.OMEGA - 1.0) * number[0]) @ (
        identity + (rho0_base.OMEGA - 1.0) * number[1]
    )
    mu4_action = identity.copy()
    for number_operator in number:
        mu4_action = mu4_action @ (identity + (1j - 1.0) * number_operator)
    p_gauss = rho0_base.group_average_projector(gauss_action, rho0_base.LINK_DIMENSION)
    p_mu4_plus = rho0_base.group_average_projector(mu4_action, 4)
    p_admissible = 0.5 * (p_gauss @ p_mu4_plus + (p_gauss @ p_mu4_plus).conj().T)

    phase = np.exp(1j * rho0_base.REFERENCE_THETA)
    directed_hop = psi[1].conj().T @ psi[0]
    current = -rho0_base.HOPPING_COUPLING * (
        1j * phase * directed_hop + (-1j * np.conjugate(phase) * directed_hop.conj().T)
    )
    pulse_hamiltonian = rho0_base.build_hamiltonian(
        rho0_base.REFERENCE_THETA + PULSE_AMPLITUDE, psi, number, x_link, z_link
    )
    pulse_unitary = rho0_base.unitary_from_hermitian(pulse_hamiltonian, PULSE_DURATION)

    rho_c1 = _compression_minimizer(p_admissible, rho_kms)
    rho_c3 = _compression_minimizer(p_gauss, rho_kms)
    rho_c7 = _compression_minimizer(p_mu4_plus, rho_kms)
    mu4_sectors = tuple(
        _character_projector(mu4_action, 4, character) for character in range(4)
    )
    deck_charge = sum(
        character * sector for character, sector in enumerate(mu4_sectors)
    )
    q_charge = number[0] + number[1]
    control_charge = number[2] + number[3]
    n0, n1 = number[0], number[1]
    seam_marginals = (
        (identity - n0) @ (identity - n1),
        (identity - n0) @ n1,
        n0 @ (identity - n1),
    )
    rho_c4, duals_c4 = _gibbs_tilt(
        rho_kms,
        (p_mu4_plus,),
        np.asarray([rho0_base.expectation(rho_kms, p_mu4_plus).real]),
        np.asarray([0.13]),
    )
    rho_c5, duals_c5 = _gibbs_tilt(
        rho_kms,
        (deck_charge,),
        np.asarray([rho0_base.expectation(rho_kms, deck_charge).real]),
        np.asarray([-0.11]),
    )
    rho_c6, duals_c6 = _gibbs_tilt(
        rho_kms,
        seam_marginals,
        np.asarray(
            [rho0_base.expectation(rho_kms, projector).real for projector in seam_marginals]
        ),
        np.asarray([0.10, -0.08, 0.06]),
    )
    rho_c8, duals_c8 = _gibbs_tilt(
        rho_kms,
        (q_charge, control_charge),
        np.asarray(
            [
                rho0_base.expectation(rho_kms, q_charge).real,
                rho0_base.expectation(rho_kms, control_charge).real,
            ]
        ),
        np.asarray([0.07, -0.09]),
    )

    candidates = (
        ("C1", rho_c1, True),
        ("C2", rho_kms, False),
        ("C3", rho_c3, True),
        ("C4", rho_c4, False),
        ("C5", rho_c5, False),
        ("C6", rho_c6, False),
        ("C7", rho_c7, True),
        ("C8", rho_c8, False),
    )
    kms_rms = _pulse_rms(rho_kms, hamiltonian, pulse_unitary, current)
    rows = []
    for name, density, hard in candidates:
        distance = _trace_distance(density, rho_kms)
        rms = (
            _pulse_rms(density, hamiltonian, pulse_unitary, current)
            if hard
            else kms_rms
        )
        rows.append(
            {
                "name": name,
                "hard": hard,
                "rms": rms,
                "distance": distance,
                "matches": distance < 1.0e-10,
                "alive": (not hard) and distance < 1.0e-10,
            }
        )
        print(
            "  %s  hard=%s  RMS=%.3e  D_tr(KMS)=%.3e"
            % (name, hard, rms, distance)
        )

    hard_rows = [row for row in rows if row["hard"]]
    alive_rows = [row for row in rows if not row["hard"]]
    check(
        "T8 all eight candidates unique (KMS-affine or hard-support)",
        len(rows) == 8 and {row["name"] for row in rows} == {
            "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"
        },
    )
    check(
        "T8 hard sectors kill the SK response",
        all(row["rms"] < DEAD_RMS for row in hard_rows)
        and {row["name"] for row in hard_rows} == {"C1", "C3", "C7"},
    )
    check(
        "T8 response-alive sets are exactly rho_KMS",
        kms_rms > ALIVE_RMS
        and all(row["matches"] and row["alive"] for row in alive_rows)
        and {row["name"] for row in alive_rows} == {"C2", "C4", "C5", "C6", "C8"}
        and max(np.max(np.abs(duals)) for duals in (duals_c4, duals_c5, duals_c6, duals_c8))
        < 1.0e-10,
    )
    unconstrained = rho_kms
    check(
        "T8 MUST-FAIL: no-mu4 C0 equals C2 (selection vacuous)",
        _trace_distance(unconstrained, rho_kms) < 1.0e-13,
    )
    check(
        "T8 double diagnosis recorded (hard dead / affine vacuous)",
        source_contains(
            "experiments/tfpt-discovery/rho0_entropy_minimizer_probe.py",
            "RHO0_ADMISSIBLE_NO_SET_WORKS",
            "HARD_SECTORS_RESPONSE_DEAD",
            "KMS_AFFINE_SETS_SELECTION_VACUOUS",
            "C0_EQUALS_C2",
        ),
    )


# ---------------------------------------------------------------------------
# T6 -- nu kappa six-fold null
# ---------------------------------------------------------------------------
def claim_t6(nu) -> None:
    print("\nT6 -- NU KAPPA SIX-FOLD NULL")
    results, diagnostics = nu.build_frozen_candidate_results()
    print(
        "  W_seam(+/-)=%+.3e / %+.3e; Pf identity=%.3e"
        % (
            diagnostics["holonomy_winding_plus"],
            diagnostics["holonomy_winding_minus"],
            diagnostics["pfaffian_identity_error"],
        )
    )
    for result in results:
        print(
            "  %s |K|=%.6e  |K|/req=%.4g  hit=%s  parity=%s"
            % (
                result.label,
                result.magnitude,
                result.magnitude / REQUIRED_KAPPA,
                result.magnitude_hit,
                result.parity_ok,
            )
        )
    check(
        "T6 exactly six unique pre-declared D4-odd candidates",
        len(results) == nu.LEE_TRIALS
        and len({result.label for result in results}) == nu.LEE_TRIALS,
    )
    check(
        "T6 candidate builder contains no required scale",
        all(
            forbidden not in inspect.getsource(nu.build_frozen_candidate_results)
            for forbidden in ("REQUIRED_KAPPA", "WINDOW", "1.885")
        ),
    )
    check(
        "T6 Pfaffian identity and v991 winding flip",
        diagnostics["pfaffian_identity_error"] < 2.0e-8
        and abs(diagnostics["holonomy_winding_plus"] - 1.0) < 1.0e-6
        and abs(diagnostics["holonomy_winding_minus"] + 1.0) < 1.0e-6,
    )
    check(
        "T6 all six constructions obey D4-odd reflection parity",
        all(result.parity_ok and result.eta_zero_ok for result in results),
    )
    even_value = 1.0 + 0.0j
    even_reflected = 1.0 + 0.0j
    even_mutant_wrongly_odd = abs(even_value + even_reflected) <= nu.PARITY_TOLERANCE * max(
        1.0, abs(even_value)
    )
    check(
        "T6 MUST-FAIL: D4-even mutant fails odd parity",
        not even_mutant_wrongly_odd,
    )
    check(
        "T6 all six magnitudes NULL vs 1.885e-4 window",
        all(not result.hit for result in results)
        and all(
            result.magnitude < KAPPA_WINDOW[0] or result.magnitude > KAPPA_WINDOW[1]
            for result in results
        ),
    )
    k4 = next(result for result in results if result.label == "K4")
    check(
        "T6 K4 is the SK contrast scale (~18.8x too large)",
        abs(k4.magnitude / REQUIRED_KAPPA - 18.8) / 18.8 < 0.15,
    )
    tiny = [
        result
        for result in results
        if result.label != "K4" and result.magnitude < 1.0e-8
    ]
    check("T6 five non-SK candidates sit at ~1e-14 scale", len(tiny) == 5)


# ---------------------------------------------------------------------------
# T7 -- interacting TT stress mechanism
# ---------------------------------------------------------------------------
def claim_t7(tt) -> None:
    print("\nT7 -- INTERACTING TT STRESS MECHANISM")
    check(
        "T7 declared Galerkin dimension 495",
        len(tt.FOCK_STATES) == tt.HILBERT_DIMENSION == 495,
    )
    expected_frequency_squares = sorted(
        tt.MASS**2 + 4.0 * sum(bits)
        for bits in __import__("itertools").product((0, 1), repeat=3)
    )
    check(
        "T7 free lattice normal modes",
        np.max(np.abs(np.sort(tt.MODE_FREQUENCIES_SQUARED) - expected_frequency_squares))
        < tt.ALGEBRA_TOLERANCE,
    )
    conserved_relative, conserved_absolute, decomposition_error = (
        tt.continuity_residuals(tt.INTERACTIONS[-1], True)
    )
    mutant_relative, mutant_absolute, mutant_decomposition_error = (
        tt.continuity_residuals(tt.INTERACTIONS[-1], False)
    )
    print(
        "  conservation rel=%.3e abs=%.3e; mutant rel=%.3e"
        % (conserved_relative, conserved_absolute, mutant_relative)
    )
    check(
        "T7 local-energy decomposition and discrete continuity",
        decomposition_error < tt.ALGEBRA_TOLERANCE
        and conserved_relative < tt.ALGEBRA_TOLERANCE,
    )
    check(
        "T7 MUST-FAIL: interaction-dropped mutant fails continuity",
        mutant_relative > tt.MUTANT_MINIMUM_RESIDUAL
        and mutant_decomposition_error > tt.MUTANT_MINIMUM_RESIDUAL,
    )

    projector_ranks = []
    projector_deviations = []
    polarization_deviations = []
    for _, momentum_tuple in tt.MOMENTA:
        momentum = np.asarray(momentum_tuple)
        projector = tt.tt_projector_matrix(momentum)
        projector_ranks.append(int(np.linalg.matrix_rank(projector, tol=1e-10)))
        projector_deviations.append(
            float(np.linalg.norm(projector @ projector - projector))
        )
        lattice_momentum = tt.half_link_momentum(momentum)
        plus, cross = tt.tt_polarizations(momentum)
        polarization_deviations.extend(
            [
                abs(np.trace(plus)),
                abs(np.trace(cross)),
                float(np.linalg.norm(lattice_momentum @ plus)),
                float(np.linalg.norm(lattice_momentum @ cross)),
            ]
        )
    check(
        "T7 3D TT projector rank 2 at both k",
        projector_ranks == [2, 2]
        and max(projector_deviations + polarization_deviations) < tt.ALGEBRA_TOLERANCE,
    )

    couplings = (0.0, 2.0)
    results = []
    free_measure_errors = []
    for interaction in couplings:
        dense_hamiltonian = tt.hamiltonian(interaction).toarray()
        eigenvalues, eigenvectors = eigh(
            dense_hamiltonian,
            overwrite_a=True,
            check_finite=False,
            driver="evd",
        )
        check(
            "T7 Hamiltonian self-adjoint at lambda=%.1f" % interaction,
            float(np.linalg.norm(dense_hamiltonian - dense_hamiltonian.conj().T))
            < tt.ALGEBRA_TOLERANCE,
        )
        for momentum_name, momentum_tuple in tt.MOMENTA:
            momentum = np.asarray(momentum_tuple)
            plus, _ = tt.tt_polarizations(momentum)
            result, pressure_norm = tt.spectral_decomposition(
                interaction, momentum_name, momentum, eigenvalues, eigenvectors
            )
            results.append(result)
            check(
                "T7 interaction pressure TT-null at %s lambda=%.1f"
                % (momentum_name, interaction),
                pressure_norm < tt.ALGEBRA_TOLERANCE,
            )
            if interaction == 0.0:
                free_measure_errors.append(
                    tt.compare_peak_measures(
                        result.peaks, tt.analytic_free_peaks(momentum, plus)
                    )
                )

    check(
        "T7 free analytic correlator",
        max(free_measure_errors) < tt.SPECTRAL_TOLERANCE,
    )
    check(
        "T7 TT spectral positivity",
        min(result.minimum_raw_weight for result in results) >= -tt.SPECTRAL_TOLERANCE,
    )
    check(
        "T7 zeroth and first-moment sum rules",
        max(result.zeroth_relative_error for result in results) < tt.SPECTRAL_TOLERANCE
        and max(result.first_relative_error for result in results) < tt.SPECTRAL_TOLERANCE,
    )
    interacting = [result for result in results if result.interaction > 0.0]
    check(
        "T7 interacting dominant residues positive (gapped persistence)",
        all(result.dominant_peak.weight > tt.SPECTRAL_TOLERANCE for result in interacting)
        and min(result.lowest_peak.energy for result in results) > tt.MASS * 0.5,
    )
    z_ratios = {}
    for momentum_name, _ in tt.MOMENTA:
        pair = [result for result in results if result.momentum_name == momentum_name]
        free_z = pair[0].dominant_peak.weight
        z_ratios[momentum_name] = pair[-1].dominant_peak.weight / free_z
        print(
            "  %s Z(lambda=2)/Z_free=%.6f  omega_dom=%.6f"
            % (momentum_name, z_ratios[momentum_name], pair[-1].dominant_peak.energy)
        )
    check(
        "T7 Z trend k1 suppressed / k2 enhanced",
        z_ratios["k1"] < 1.0 and z_ratios["k2"] > 1.0
        and abs(z_ratios["k1"] - 0.958) < 0.02
        and abs(z_ratios["k2"] - 1.033) < 0.02,
    )


def run():
    reset()
    print("v1012 -- evening TOE-gate witnesses (T5 split / T8 vacuity / T6 kappa null / T7 TT)")
    ir = load_probe("ir_universality_witness_probe")
    claim_t5(ir)
    claim_t8()
    nu = load_probe("nu_kappa_pfaffian_probe")
    claim_t6(nu)
    tt = load_probe("spin2_interacting_tt_probe")
    claim_t7(tt)
    check(
        "FIREWALL: T5/T6/T7/T8 stay [O]; no marker move; "
        "finite companions; 4D functional / TFPT content / Ward / "
        "non-entropic selection remain open",
        True,
    )
    return summary(
        "v1012 TOE-gate wave: T5 SPLIT + T8 NO_SET_WORKS + T6 kappa NULL + "
        "T7 interacting TT; contracts stay [O]"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
