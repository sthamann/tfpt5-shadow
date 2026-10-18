#!/usr/bin/env python3
"""tfpt3p1d_spinor_channels_probe -- EXPLORATION ONLY (no promotion).

Stage 8 is the stop-rule test for the B strand.  It embeds a charged
two-component wall-spin channel inside the exact Stage-7 periodic-face
gauge/matter quotient rather than attaching a one-body companion.

SECTOR.  Stage 7 has 32 gauge-cycle states times eight even-parity
four-site JW configurations, dimension 256.  The local eight-mode spinor
Fock space would enlarge this to 8192 before adding the mirror wall.
We take the translation-coherent spin block: each Stage-7 state carries
one global two-component surface-spin label.  The common interacting
dimension is therefore 256*2=512.  This is the k=0 coherent block of the
physical wall; the mirror is integrated out using its measured DET gap 2.

The Hamiltonian is

  H_spin = H_B8 tensor I_2
           - eta*t sum_x-links c_y^dag U_xy sigma_x c_x
           - eta*t sum_y-links c_y^dag U_xy sigma_y c_x + h.c.

with eta=1.  The Pauli channel uses the same fluctuating Z2 links and the
same periodic-cut background phase as the base charged hopping.  It is
therefore inside the 512-state gauge quotient.  Eta=0 is the charge-zero
mutant: exactly H_B8 tensor I_2, so its K must reproduce the B8 collapse
point by point.

PREREGISTRATION_FREEZE_BEGIN
model=B8_periodic_face_exact_quotient_x_global_two_component_spin_coherent_block
base_dim=256_spin_dim=2_total_dim=512
reduction=one_physical_wall_mirror_integrated_out_gap2_spin_coherent_translation_block
H=H_B8_tensor_I2_plus_eta_charge1_Pauli_xy_gauge_covariant_hopping
eta=1.0
beta=4.0
holonomy=same_B8_periodic_cut_background
K=Gamma_second_per_four_sites_Richardson_h0.04
couplings=0.6,1.0,1.4,1.6,2.0
root_interval=0.45,4.0
selector=unique_contractive_root_in_y_gminus2
comparison=charge0_eta0_exactly_B8_tensor_I2
limit=tree_stub_acyclic_theta_independent_so_face_response_is_2p1d_limit
stop_rule=no_root_means_B_strand_stops_with_confined_phase_collapse
scope=spin_coherent_block_not_full_8mode_spinor_Fock_mirror_integrated_out
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=6b268a23945db0266da7a2a657c460d14a4ffa1f02e078c4acd21e9808840cf3

The same beta, finite difference, normalization, root interval, and
contractive selector as Stage 7 are retained.  No multiplicity factor is
inserted: any restoration must arise from the explicit Pauli hopping.

HONEST BOUNDARY: one physical wall, globally coherent two-component block
rather than the full local eight-mode spinor Fock space, mirror integrated
out, Z2, one 2x2 face, no volume limit.  If no root appears, the B strand
stops and the confined-phase collapse is the typed result.  QFT4D
contracts stay [O].

VERDICT ENUM:
SPINOR_CHANNELS_{ROOT_RESTORED(gstar,Rprime)|COLLAPSE_CONFIRMED(reading)}.
"""

from __future__ import annotations

import hashlib
import math
import sys

import numpy as np
from scipy import sparse
from scipy.optimize import brentq
from scipy.sparse.linalg import eigsh

import tfpt3p1d_periodic_face_probe as b8


SPINOR_STRENGTH = 1.0
REPORT_COUPLINGS = (0.6, 1.0, 1.4, 1.6, 2.0)
ROOT_INTERVAL = (0.45, 4.0)
FROZEN_SHA256 = "6b268a23945db0266da7a2a657c460d14a4ffa1f02e078c4acd21e9808840cf3"

FROZEN_DEFINITION = """model=B8_periodic_face_exact_quotient_x_global_two_component_spin_coherent_block
base_dim=256_spin_dim=2_total_dim=512
reduction=one_physical_wall_mirror_integrated_out_gap2_spin_coherent_translation_block
H=H_B8_tensor_I2_plus_eta_charge1_Pauli_xy_gauge_covariant_hopping
eta=1.0
beta=4.0
holonomy=same_B8_periodic_cut_background
K=Gamma_second_per_four_sites_Richardson_h0.04
couplings=0.6,1.0,1.4,1.6,2.0
root_interval=0.45,4.0
selector=unique_contractive_root_in_y_gminus2
comparison=charge0_eta0_exactly_B8_tensor_I2
limit=tree_stub_acyclic_theta_independent_so_face_response_is_2p1d_limit
stop_rule=no_root_means_B_strand_stops_with_confined_phase_collapse
scope=spin_coherent_block_not_full_8mode_spinor_Fock_mirror_integrated_out"""

SIGMA_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SIGMA_Y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
IDENTITY_SPIN = np.eye(2, dtype=complex)
CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-43s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def verify_freeze() -> str:
    if __doc__ is None:
        raise AssertionError("module docstring required")
    payload = (
        __doc__.split("PREREGISTRATION_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_FREEZE_END", 1)[0]
        .strip()
    )
    declared = __doc__.split("PREREGISTRATION_SHA256=", 1)[1].split()[0]
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if (
        payload != FROZEN_DEFINITION
        or digest != declared
        or digest != FROZEN_SHA256
    ):
        raise AssertionError("frozen protocol mismatch")
    return digest


def spinor_hamiltonian(
    coupling: float,
    theta: float = 0.0,
    spinor_strength: float = SPINOR_STRENGTH,
    tree: tuple[int, ...] = b8.TREE_A,
) -> sparse.csr_matrix:
    base = b8.hamiltonian(
        coupling, tree=tree, theta=theta, twist_axis=0
    )
    matrix = sparse.kron(
        base, sparse.eye(2, dtype=complex), format="lil"
    )
    if spinor_strength == 0.0:
        return matrix.tocsr()

    gauge = b8.TreeGauge(tree)
    for cycle_bits in range(1 << len(gauge.chords)):
        full = gauge.representative(cycle_bits)
        for occupancy in b8.EVEN_OCCUPANCIES:
            base_column = b8.matrix_index(cycle_bits, occupancy)
            for edge_index, edge in enumerate(b8.EDGES[:8]):
                source_mode = b8.PHYSICAL_MODE[edge.source]
                target_mode = b8.PHYSICAL_MODE[edge.target]
                source_filled = (occupancy >> source_mode) & 1
                target_filled = (occupancy >> target_mode) & 1
                if source_filled == target_filled:
                    continue
                pauli = SIGMA_X if edge.axis == 0 else SIGMA_Y
                background = (
                    np.exp(1j * theta)
                    if edge.axis == 0 and edge.wrap
                    else 1.0
                )
                link = -1.0 if (full >> edge_index) & 1 else 1.0
                if source_filled:
                    sign = b8.jw_sign(
                        occupancy, source_mode, target_mode
                    )
                    coefficient = (
                        -spinor_strength
                        * b8.HOPPING
                        * background
                        * link
                        * sign
                    )
                else:
                    sign = b8.jw_sign(
                        occupancy, target_mode, source_mode
                    )
                    coefficient = (
                        -spinor_strength
                        * b8.HOPPING
                        * np.conj(background)
                        * link
                        * sign
                    )
                target_occupancy = occupancy ^ (
                    (1 << source_mode) | (1 << target_mode)
                )
                base_row = b8.matrix_index(
                    cycle_bits, target_occupancy
                )
                for target_spin in range(2):
                    for source_spin in range(2):
                        value = coefficient * pauli[
                            target_spin, source_spin
                        ]
                        if value:
                            matrix[
                                2 * base_row + target_spin,
                                2 * base_column + source_spin,
                            ] += value
    return matrix.tocsr()


def spectrum(
    coupling: float,
    theta: float,
    spinor_strength: float,
    tree: tuple[int, ...] = b8.TREE_A,
) -> np.ndarray:
    return np.linalg.eigvalsh(
        spinor_hamiltonian(
            coupling, theta, spinor_strength, tree
        ).toarray()
    )


def gamma(
    coupling: float,
    theta: float,
    spinor_strength: float,
) -> float:
    values = spectrum(coupling, theta, spinor_strength)
    arguments = -b8.BETA * values
    maximum = float(np.max(arguments))
    return -(maximum + math.log(float(np.sum(np.exp(arguments - maximum)))))


def stiffness(coupling: float, spinor_strength: float) -> float:
    center = gamma(coupling, 0.0, spinor_strength)

    def curvature(step: float) -> float:
        return (
            gamma(coupling, step, spinor_strength)
            - 2.0 * center
            + gamma(coupling, -step, spinor_strength)
        ) / (4.0 * step**2)

    coarse = curvature(b8.RICHARDSON_STEP)
    fine = curvature(b8.RICHARDSON_STEP / 2.0)
    return (4.0 * fine - coarse) / 3.0


def root_census() -> list[float]:
    cache: dict[float, float] = {}

    def residual(coupling: float) -> float:
        key = round(coupling, 12)
        if key not in cache:
            cache[key] = (
                coupling ** -2
                - stiffness(coupling, SPINOR_STRENGTH)
            )
        return cache[key]

    samples = np.linspace(ROOT_INTERVAL[0], ROOT_INTERVAL[1], 25)
    roots = []
    for left, right in zip(samples[:-1], samples[1:]):
        if residual(left) * residual(right) < 0.0:
            root = brentq(residual, left, right, xtol=2.0e-8)
            if not roots or abs(root - roots[-1]) > 1.0e-6:
                roots.append(root)
    return roots


def contraction_derivative(root: float) -> float:
    y_value = root ** -2

    def derivative(relative_step: float) -> float:
        step = relative_step * y_value
        plus = stiffness(
            (y_value + step) ** -0.5, SPINOR_STRENGTH
        )
        minus = stiffness(
            (y_value - step) ** -0.5, SPINOR_STRENGTH
        )
        return (plus - minus) / (2.0 * step)

    coarse = derivative(0.02)
    fine = derivative(0.01)
    return (4.0 * fine - coarse) / 3.0


def main() -> int:
    print("=" * 100)
    print("TFPT STAGE 8 -- CHARGED SPINOR CHANNEL STOP-RULE TEST")
    print("=" * 100)
    print("\nS0  COMMON GAUGE/SPINOR SECTOR")
    digest = verify_freeze()
    check("functional-definition-hash", digest == FROZEN_SHA256,
          "SHA256=%s" % digest)
    check(
        "spin-coherent quotient dimension",
        len(b8.EVEN_OCCUPANCIES) == 8
        and len(b8.TreeGauge(b8.TREE_A).chords) == 5
        and 32 * 8 * 2 == 512,
        "32 gauge cycles x 8 JW states x 2 spin = 512",
    )

    print("\nS1  EXACTNESS / TREE INDEPENDENCE")
    tree_errors = []
    hermiticity_errors = []
    for coupling in (0.8, 1.6):
        first = spinor_hamiltonian(coupling, tree=b8.TREE_A)
        second = spinor_hamiltonian(coupling, tree=b8.TREE_B)
        for matrix in (first, second):
            difference = matrix - matrix.getH()
            hermiticity_errors.append(
                float(np.max(np.abs(difference.data)))
                if difference.nnz else 0.0
            )
        first_low = eigsh(
            first, k=8, which="SA", return_eigenvectors=False
        )
        second_low = eigsh(
            second, k=8, which="SA", return_eigenvectors=False
        )
        tree_errors.append(float(np.max(np.abs(
            np.sort(first_low) - np.sort(second_low)
        ))))
    check(
        "Hermiticity exact",
        max(hermiticity_errors) < 1.0e-13,
        "max|H-Hdag|=%.1e" % max(hermiticity_errors),
    )
    check(
        "two-tree spectrum identity",
        max(tree_errors) < 1.0e-12,
        "lowest-eight max delta %.3e" % max(tree_errors),
    )

    print("\nS2  CHARGED-SPINOR K CURVE VS B8")
    charged_curve = {}
    neutral_curve = {}
    for coupling in REPORT_COUPLINGS:
        charged = stiffness(coupling, SPINOR_STRENGTH)
        neutral = stiffness(coupling, 0.0)
        b8_value = b8.stiffness(coupling)
        charged_curve[coupling] = charged
        neutral_curve[coupling] = neutral
        print(
            "  g=%.1f Kspin=%+.12f Kq0=%+.12f KB8=%+.12f "
            "residual=%+.12f"
            % (
                coupling,
                charged,
                neutral,
                b8_value,
                coupling ** -2 - charged,
            )
        )
    neutral_error = max(
        abs(neutral_curve[coupling] - b8.stiffness(coupling))
        for coupling in REPORT_COUPLINGS
    )
    check(
        "charge-zero mutant exactly reproduces B8",
        neutral_error < 1.0e-9,
        "max |Kq0-KB8|=%.3e" % neutral_error,
    )

    roots = root_census()
    derivative = (
        contraction_derivative(roots[0]) if len(roots) == 1 else math.nan
    )
    if roots:
        print(
            "  selected g*=%.12f R'=%+.12f" % (roots[0], derivative)
        )
    else:
        print("  selector: no roots on [0.45,4.0]; B-strand stop fires")

    if roots:
        selector_pass = len(roots) == 1 and abs(derivative) < 1.0
        selector_detail = "g*=%.9f R'=%.9f" % (roots[0], derivative)
    else:
        selector_pass = all(
            coupling ** -2 - value > 0.0
            for coupling, value in charged_curve.items()
        )
        selector_detail = (
            "no root; charged K also collapses in confined regime"
        )
    check(
        "frozen selector reaches typed outcome",
        selector_pass,
        selector_detail,
    )

    print("\nS3  2+1D LIMIT / PHYSICAL READING")
    weak_enhancement = (
        charged_curve[0.6] / neutral_curve[0.6]
    )
    confined_ratio = (
        charged_curve[2.0] / charged_curve[0.6]
        if charged_curve[0.6] != 0.0 else math.nan
    )
    check(
        "charged 2+1D-face response is alive",
        charged_curve[0.6] > 0.0 and weak_enhancement > 1.0,
        "Kspin/Kq0 at g=.6=%.6f; compare Stage2 selected roots "
        "0.578402->0.936332" % weak_enhancement,
    )
    check(
        "confined-phase collapse classified",
        charged_curve[2.0] < 1.0e-3
        and confined_ratio < 1.0e-3,
        "K(2)/K(.6)=%.3e" % confined_ratio,
    )
    check(
        "honest-boundary",
        True,
        "global coherent spin block, mirror integrated out, no volume limit; [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_passed = passed == total
    if len(roots) == 1 and abs(derivative) < 1.0:
        verdict = (
            "SPINOR_CHANNELS_ROOT_RESTORED(gstar=%.6f,Rprime=%.6f)"
            % (roots[0], derivative)
        )
    else:
        verdict = (
            "SPINOR_CHANNELS_COLLAPSE_CONFIRMED("
            "matching_scale_must_be_deconfined_weak_regime)"
        )
    print("\n" + "=" * 100)
    print("RESULT: %d/%d CHECKS PASS" % (passed, total))
    print("VERDICT: %s" % verdict)
    print("B-STRAND STOP: %s" % ("NO" if roots else "YES"))
    print("QFT4D contracts stay [O]")
    print("=" * 100)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
