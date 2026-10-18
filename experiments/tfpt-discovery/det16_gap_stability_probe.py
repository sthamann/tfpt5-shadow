#!/usr/bin/env python3
r"""Numeric twin for the DET16 product-projector stability memorandum.

EXPLORATION ONLY.  The exact four-mode analogue is used to check:

* the proposed counting line ``gap >= 1 - 2 c |t|`` on open chains with
  ``c = modes_per_cluster * maximum_coordination``;
* the absence (or presence) of a finite-volume gap closing on a declared scan;
* Spin(4) covariance of flavor-diagonal hopping;
* visible failure of a flavor-selective, non-covariant mutant;
* visible failure of the 1/3 projector-normalization mutant.

The linear counting line is a numeric comparison, not a proof for ordinary
hopping.  Its elementary relative-form proof would require block diagonality
with respect to the product ground projector.  This probe explicitly checks
that ordinary hopping violates that extra hypothesis.  Volume-independent
stability instead comes from the LTQO/local-gap theorem cited in the companion
proof memorandum; that theorem supplies an existence threshold, not the
counting value below.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp

from spin10_det16_projector_probe import (
    EIG_TOL,
    PHI,
    TOY_CLUSTER_MODES,
    determinant_projector,
    hopping_operator,
    low_spectrum,
    max_abs_sparse,
    repeated_one_body,
    second_quantize,
    so4_vector_generators,
    toy_hamiltonian,
)


TEST_STRENGTHS = (0.05, 0.10, 0.20, 0.30)
SCAN_MAX = 4.0
SCAN_STEP_SMALL = 0.05
SCAN_STEP_FOUR_CLUSTERS = 0.10
CHECKS: list[bool] = []


@dataclass(frozen=True)
class ScanResult:
    cluster_count: int
    minimum_gap: float
    minimizing_strength: float
    closing_strength: float | None


def check(name: str, condition: bool, detail: str) -> None:
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-48s %s" % ("PASS" if ok else "FAIL", name, detail))


def maximum_coordination(cluster_count: int) -> int:
    if cluster_count < 2:
        raise ValueError("the stability twin requires at least two clusters")
    return 1 if cluster_count == 2 else 2


def counting_constant(cluster_count: int) -> int:
    return TOY_CLUSTER_MODES * maximum_coordination(cluster_count)


def product_ground_projector(cluster_count: int) -> sp.csr_matrix:
    _hamiltonian, projectors = toy_hamiltonian(
        cluster_count, (PHI,) * cluster_count
    )
    result = sp.eye(projectors[0].shape[0], format="csr", dtype=complex)
    for projector in projectors:
        result = result @ projector
    return result.tocsr()


def flavor_selective_hopping(cluster_count: int) -> sp.csr_matrix:
    total_modes = TOY_CLUSTER_MODES * cluster_count
    one_body = np.zeros((total_modes, total_modes), dtype=complex)
    selected_flavor = 0
    for cluster in range(cluster_count - 1):
        left = TOY_CLUSTER_MODES * cluster + selected_flavor
        right = TOY_CLUSTER_MODES * (cluster + 1) + selected_flavor
        one_body[left, right] = 1.0
        one_body[right, left] = 1.0
    return second_quantize(one_body)


def test_counting_line() -> dict[int, dict[float, float]]:
    print("\nCOUNTING-LINE NUMERIC COMPARISON")
    measured: dict[int, dict[float, float]] = {}
    for cluster_count in (2, 3, 4):
        base, _projectors = toy_hamiltonian(
            cluster_count, (PHI,) * cluster_count
        )
        hopping = hopping_operator(cluster_count)
        c_value = counting_constant(cluster_count)
        measured[cluster_count] = {}
        for strength in TEST_STRENGTHS:
            spectrum = low_spectrum((base + strength * hopping).tocsr())
            lower_line = 1.0 - 2.0 * c_value * abs(strength)
            measured[cluster_count][strength] = spectrum.gap
            check(
                "bound n=%d, t=%.2f" % (cluster_count, strength),
                spectrum.degeneracy == 1
                and spectrum.gap + EIG_TOL >= lower_line,
                "c=%d, line=% .6f, exact gap=%.9f"
                % (c_value, lower_line, spectrum.gap),
            )
    return measured


def scan_gap(cluster_count: int) -> ScanResult:
    base, _projectors = toy_hamiltonian(
        cluster_count, (PHI,) * cluster_count
    )
    hopping = hopping_operator(cluster_count)
    step = (
        SCAN_STEP_FOUR_CLUSTERS
        if cluster_count == 4
        else SCAN_STEP_SMALL
    )
    strengths = np.arange(0.0, SCAN_MAX + 0.5 * step, step)
    minimum_gap = float("inf")
    minimizing_strength = 0.0
    closing_strength: float | None = None
    for strength in strengths:
        spectrum = low_spectrum((base + strength * hopping).tocsr())
        if spectrum.gap < minimum_gap:
            minimum_gap = spectrum.gap
            minimizing_strength = float(strength)
        if spectrum.gap <= EIG_TOL and closing_strength is None:
            closing_strength = float(strength)
    return ScanResult(
        cluster_count=cluster_count,
        minimum_gap=minimum_gap,
        minimizing_strength=minimizing_strength,
        closing_strength=closing_strength,
    )


def test_closing_scan() -> list[ScanResult]:
    print("\nFINITE-VOLUME GAP-CLOSING SCAN")
    results = [scan_gap(cluster_count) for cluster_count in (2, 3, 4)]
    for result in results:
        no_closing = result.closing_strength is None
        closing_text = (
            "none through %.2f" % SCAN_MAX
            if no_closing
            else "%.6f" % result.closing_strength
        )
        check(
            "scan n=%d" % result.cluster_count,
            no_closing and result.minimum_gap > EIG_TOL,
            "closing=%s; min gap %.9f at t=%.3f"
            % (
                closing_text,
                result.minimum_gap,
                result.minimizing_strength,
            ),
        )
    return results


def test_covariance_and_mutants() -> None:
    print("\nHYPOTHESIS AND MUTANT CHECKS")
    cluster_count = 2
    base, _projectors = toy_hamiltonian(
        cluster_count, (PHI,) * cluster_count
    )
    hopping = hopping_operator(cluster_count)
    ground_projector = product_ground_projector(cluster_count)
    complement = sp.eye(
        base.shape[0], format="csr", dtype=complex
    ) - ground_projector
    off_diagonal_norm = float(
        np.linalg.norm((complement @ hopping @ ground_projector).toarray(), 2)
    )
    check(
        "ordinary hopping is not block diagonal",
        off_diagonal_norm > 1.0e-6,
        "||(1-P) K P||=%.9f; elementary relative-form premise fails"
        % off_diagonal_norm,
    )

    covariant_deviation = 0.0
    mutant_deviation = 0.0
    mutant = flavor_selective_hopping(cluster_count)
    for generator in so4_vector_generators():
        total_generator = second_quantize(
            repeated_one_body(generator, cluster_count)
        )
        covariant_deviation = max(
            covariant_deviation,
            max_abs_sparse(total_generator @ hopping - hopping @ total_generator),
        )
        mutant_deviation = max(
            mutant_deviation,
            max_abs_sparse(total_generator @ mutant - mutant @ total_generator),
        )
    check(
        "flavor-diagonal hopping is Spin(4)-covariant",
        covariant_deviation < 1.0e-10,
        "max commutator %.3e" % covariant_deviation,
    )
    check(
        "flavor-selective hopping mutant violates covariance",
        mutant_deviation > 1.0e-3,
        "max commutator %.3e" % mutant_deviation,
    )

    bad_projector = determinant_projector(
        TOY_CLUSTER_MODES,
        tuple(range(TOY_CLUSTER_MODES)),
        PHI,
        normalization=1.0 / 3.0,
    )
    bad_idempotency = max_abs_sparse(
        bad_projector @ bad_projector - bad_projector
    )
    bad_trace = float(np.real(bad_projector.diagonal().sum()))
    check(
        "1/3-normalization mutant is not a projector",
        bad_idempotency > 0.1 and abs(bad_trace - 2.0 / 3.0) < 1.0e-10,
        "trace=%.9f, idempotency defect=%.9f"
        % (bad_trace, bad_idempotency),
    )


def print_summary(
    measured: dict[int, dict[float, float]],
    scan_results: list[ScanResult],
) -> None:
    toy_worst_c = TOY_CLUSTER_MODES * 2
    toy_counting_threshold = 1.0 / (2.0 * toy_worst_c)
    det16_spatial_coordination = 6
    det16_counting_constant = 16 * det16_spatial_coordination
    det16_counting_threshold = 1.0 / (2.0 * det16_counting_constant)

    print("\nSUMMARY")
    print(
        "  toy counting threshold: t0_count = 1/(2*%d) = %.9f"
        % (toy_worst_c, toy_counting_threshold)
    )
    print(
        "  DET16 cubic spatial slice: c_count = 16*6 = %d, "
        "t0_count = 1/%d = %.9f"
        % (
            det16_counting_constant,
            2 * det16_counting_constant,
            det16_counting_threshold,
        )
    )
    print(
        "  exact t=0.20 gaps: n=2 %.9f, n=3 %.9f, n=4 %.9f"
        % (
            measured[2][0.20],
            measured[3][0.20],
            measured[4][0.20],
        )
    )
    if all(result.closing_strength is None for result in scan_results):
        ratio_upper_bound = toy_counting_threshold / SCAN_MAX
        print(
            "  no finite-volume closing for n=2..4 on [0, %.2f]; "
            "therefore t_c^scan > %.2f and t0_count/t_c^scan < %.9f"
            % (SCAN_MAX, SCAN_MAX, ratio_upper_bound)
        )
    print(
        "  interpretation: the counting line passed numerically but is not "
        "a theorem for hopping because ||(1-P)KP|| is nonzero"
    )


def main() -> int:
    print("=" * 92)
    print("det16_gap_stability_probe -- four-mode numeric twin")
    print("EXPLORATION ONLY; no status-marker move")
    print("=" * 92)
    measured = test_counting_line()
    scan_results = test_closing_scan()
    test_covariance_and_mutants()
    print_summary(measured, scan_results)
    print("\nCHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    verdict = (
        "DET16_GAP_STABILITY_TWIN_PASS"
        if all(CHECKS)
        else "DET16_GAP_STABILITY_TWIN_FAIL"
    )
    print("VERDICT: %s" % verdict)
    print("=" * 92)
    return 0 if all(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
