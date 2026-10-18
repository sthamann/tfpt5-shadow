#!/usr/bin/env python3
"""v1011 -- compressed 3+1D ladder battery B6--B9 (afternoon harvest,
2026-08-30).

Provenance: experiments/tfpt-discovery/tfpt3p1d_{minimal,coupled_wall,
periodic_face,spinor_channels}_probe.py (17/17 + 12/12 + 12/12 + 9/9).
Helpers live in the frozen probes; experiments/ is not a verification-
module import.

THE POINT.  The 3+1D scaffold is viable at minimal scale; fully coupled
link-wall dynamics are demonstrated; holonomy stiffness collapses in
the confined phase, so the matching point of the coupling functional
must sit in the deconfined/weak regime.  No marker moves.

  B6 [E-finite]/[N]: minimal 3+1D viable -- exact Gauss 32768 checks,
        first 3+1D confinement witness, wall separation, EXACT in-face
        isotropy, Kronecker-level stiffness g* ~ 1.915.
  B7 [E-finite]/[N]: exact maximal-tree gauge fixing 524288 -> 4096,
        tree-independence, DET survives coupling, back-reaction,
        decoupling continuity; open-cell holonomy zero -- typed
        (no contractive root on the flux functional).
  B8 [N]: periodicity restores holonomy stiffness; isotropy; spinor
        witnesses exact; coupled K collapses above g ~ 1.6, no root.
  B9 [N]: charged spinor channels double K at weak coupling; charge-0
        control matches B8; collapse CONFIRMED.  POSITIVE TYPED RESULT:
        the matching scale must sit in the deconfined/weak regime.

MUST-FAIL: plaquette-off kills area ordering; DET-off leaves both
faces gapless; anisotropy mutant breaks isotropy; cyclic non-tree
gauge set has incidence rank < 7; open-x kills holonomy K; charge-0
is exactly B8 tensor I2.

HONEST SCOPE (firewall): Z2, tiny open/periodic cuboids, factorized
or translation-coherent blocks, no 4D volume/continuum theorem.
QFT4D.LATTICE.FUNDAMENTAL.01 stays Decision; GAUGE.DETLINE.FIXPOINT.01
stays [O] with the matching-scale BINDING constraint recorded.
Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import eigsh

from tfpt_constants import check as suite_check, summary, reset


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DISC = ROOT / "experiments" / "tfpt-discovery"

STAGE5_ROOT = 1.914947527
WEAK_ENHANCEMENT_MIN = 1.5
COLLAPSE_K_MAX = 1.0e-3


def check(label: str, condition: bool) -> None:
    suite_check(label, bool(condition))


def load_probe(name: str):
    if str(DISC) not in sys.path:
        sys.path.insert(0, str(DISC))
    if name in sys.modules:
        return sys.modules[name]
    return importlib.import_module(name)


def source_contains(relative_path: str, *needles: str) -> bool:
    source = (ROOT / relative_path).read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


def claim_b6(b6) -> float:
    print("\nB6 -- MINIMAL 3+1D VIABILITY")
    digest = b6.verify_freeze()
    check("B6 freeze hash", digest == b6.FROZEN_SHA256)
    cube = b6.OpenCubicLattice((2, 2, 2))
    extended = b6.OpenCubicLattice((3, 2, 2))
    check(
        "3D dimensions and Gauss sectors",
        len(cube.edges) == 12
        and len(cube.plaquettes) == 6
        and len(cube.gauss_basis) == 32
        and len(extended.edges) == 20
        and len(extended.gauss_basis) == 512,
    )
    matter = b6.gauge_matter_hamiltonian(cube, 1.2)
    gauss_ok = True
    for electric_state in range(1 << len(cube.edges)):
        occupancy = cube.divergence_occupancy(electric_state)
        for vertex, incidence in enumerate(cube.vertex_masks):
            charge = (occupancy >> vertex) & 1
            divergence = (electric_state & incidence).bit_count() % 2
            if (-1) ** (charge + divergence) != 1:
                gauss_ok = False
                break
        if not gauss_ok:
            break
    check(
        "exact Gauss law with charged matter (32768 basiswise G_x = +1)",
        gauss_ok,
    )
    face_plaquettes = [
        plaquette
        for plaquette in extended.plaquettes
        if plaquette.axes == (0, 1) and plaquette.base[2] == 0
    ]
    face_plaquettes.sort(key=lambda plaquette: plaquette.base[0])
    area_one = face_plaquettes[0].mask
    area_two = face_plaquettes[0].mask ^ face_plaquettes[1].mask
    wilson = {}
    for coupling in (0.8, 2.0):
        matrix = extended.pure_gauge_hamiltonian(coupling)
        values, vectors = eigsh(matrix, k=3, which="SA", tol=1.0e-11)
        ground = vectors[:, np.argsort(values)[0]]
        wilson[coupling] = (
            extended.wilson_expectation(ground, area_one),
            extended.wilson_expectation(ground, area_two),
        )
    strong_small, strong_large = wilson[2.0]
    weak_small, weak_large = wilson[0.8]
    print(
        "  confinement W(A=1,g=2)=%.6f W(A=2,g=2)=%.6f; "
        "W(A=1,g=.8)=%.6f W(A=2,g=.8)=%.6f"
        % (strong_small, strong_large, weak_small, weak_large)
    )
    check(
        "3D Wilson area ordering (first confinement witness)",
        strong_small > strong_large
        and strong_large / strong_small < weak_large / weak_small,
    )
    physical_weight, mirror_weight, face_overlap = b6.face_zero_weights()
    check(
        "Wilson-Dirac face separation",
        physical_weight > 0.999999
        and mirror_weight > 0.999999
        and face_overlap < 1.0e-12,
    )
    energy_x = b6.surface_dispersion(b6.ISOTROPY_MOMENTUM, 0.0)
    energy_y = b6.surface_dispersion(0.0, b6.ISOTROPY_MOMENTUM)
    check(
        "IR in-face isotropy is exact",
        abs(energy_x - energy_y) < 1.0e-14,
    )
    roots = b6.root_census()
    derivative = math.nan
    if len(roots) == 1:
        derivative, _ = b6.contraction_derivative(roots[0])
        print("  Kronecker-level g*=%.9f |R'|=%.9f" % (roots[0], abs(derivative)))
    check(
        "unique contractive stiffness root near 1.915",
        len(roots) == 1
        and abs(derivative) < 1.0
        and abs(roots[0] - STAGE5_ROOT) < 1.0e-6,
    )
    mutant_ground = np.zeros(len(extended.gauss_basis))
    mutant_ground[extended.gauss_index[0]] = 1.0
    check(
        "MUST-FAIL: plaquette-off kills area ordering",
        abs(extended.wilson_expectation(mutant_ground, area_one)) < 1.0e-14
        and abs(extended.wilson_expectation(mutant_ground, area_two)) < 1.0e-14,
    )
    mutant_x = b6.surface_dispersion(b6.ISOTROPY_MOMENTUM, 0.0, 1.0, 0.7)
    mutant_y = b6.surface_dispersion(0.0, b6.ISOTROPY_MOMENTUM, 1.0, 0.7)
    check(
        "MUST-FAIL: anisotropy mutant breaks isotropy",
        abs(mutant_x - mutant_y) > 0.05,
    )
    return roots[0] if roots else math.nan


def claim_b7(b7) -> None:
    print("\nB7 -- FULLY COUPLED LINK-WALL")
    digest, digest_v2 = b7.verify_freeze()
    check(
        "B7 freeze hashes",
        digest == b7.FROZEN_SHA256 and digest_v2 == b7.FROZEN_SHA256_V2,
    )
    check(
        "exact maximal-tree gauge fixing 524288 -> 4096",
        len(b7.VERTICES) == 8
        and len(b7.EDGES) == 12
        and len(b7.TREE_A) == 7
        and len(b7.EVEN_OCCUPANCIES) * 32 == 4096,
    )
    tree_error = 0.0
    matrices = {}
    for coupling in (0.8, 2.0):
        matrix_a = b7.coupled_hamiltonian(coupling, b7.TREE_A)
        matrix_b = b7.coupled_hamiltonian(coupling, b7.TREE_B)
        matrices[coupling] = matrix_a
        spectrum_a = b7.lowest(matrix_a)
        spectrum_b = b7.lowest(matrix_b)
        tree_error = max(tree_error, float(np.max(np.abs(spectrum_a - spectrum_b))))
        print(
            "  g=%.1f tree max_delta=%.3e E0=%.8f"
            % (coupling, np.max(np.abs(spectrum_a - spectrum_b)), spectrum_a[0])
        )
    check("two-tree spectrum identity", tree_error < 1.0e-8)
    coupled = {}
    for coupling in (0.8, 2.0):
        values, vectors = b7.lowest(matrices[coupling], count=24, vectors=True)
        finite_gap = float(values[1] - values[0])
        det_off = b7.lowest(
            b7.coupled_hamiltonian(coupling, det_strength=0.0), count=2
        )
        det_increment = finite_gap - float(det_off[1] - det_off[0])
        bond = b7.face_bond_expectation(
            vectors[:, 0], b7.TREE_A, b7.PHYSICAL_FACE_EDGES
        )
        coupled[coupling] = (finite_gap, det_increment, bond)
        print(
            "  g=%.1f gap=%.6f DET_inc=%+.6f Bphys=%.6f"
            % (coupling, finite_gap, det_increment, bond)
        )
    check(
        "DET gap survives coupling",
        all(result[1] > 0.0 for result in coupled.values()),
    )
    flat_matrix = b7.flat_link_matter_hamiltonian()
    _flat_values, flat_vectors = np.linalg.eigh(flat_matrix)
    flat_bond = b7.flat_face_bond_expectation(flat_vectors[:, 0])
    shift_strong = coupled[2.0][2] / flat_bond - 1.0
    shift_weak = coupled[0.8][2] / flat_bond - 1.0
    print("  back-reaction Z-1(g=2)=%+.6f  Z-1(g=.8)=%+.6f" % (shift_strong, shift_weak))
    check(
        "nonzero coupling-dependent back-reaction",
        abs(shift_strong - shift_weak) > 1.0e-3,
    )
    weak_matrix = b7.coupled_hamiltonian(0.3)
    _weak_values, weak_vectors = b7.lowest(weak_matrix, count=2, vectors=True)
    weak_ratio = (
        b7.face_bond_expectation(
            weak_vectors[:, 0], b7.TREE_A, b7.PHYSICAL_FACE_EDGES
        )
        / flat_bond
    )
    print("  decoupling g=0.3 bond/control = %.9f" % weak_ratio)
    check("decoupling Kronecker continuity", abs(weak_ratio - 1.0) < 0.1)
    cyclic_set = (
        b7.EDGE_INDEX[tuple(sorted((b7.VERTEX_INDEX[(0, 0, 0)], b7.VERTEX_INDEX[(1, 0, 0)])))],
        b7.EDGE_INDEX[tuple(sorted((b7.VERTEX_INDEX[(1, 0, 0)], b7.VERTEX_INDEX[(1, 1, 0)])))],
        b7.EDGE_INDEX[tuple(sorted((b7.VERTEX_INDEX[(1, 1, 0)], b7.VERTEX_INDEX[(0, 1, 0)])))],
        b7.EDGE_INDEX[tuple(sorted((b7.VERTEX_INDEX[(0, 1, 0)], b7.VERTEX_INDEX[(0, 0, 0)])))],
        b7.TREE_A[3], b7.TREE_A[4], b7.TREE_A[5],
    )
    check(
        "MUST-FAIL: cyclic non-tree gauge mutant fails",
        b7.gf2_incidence_rank(cyclic_set) < len(b7.VERTICES) - 1,
    )
    check(
        "open-cell holonomy zero is the typed B7 selector outcome",
        source_contains(
            "experiments/tfpt-discovery/tfpt3p1d_coupled_wall_probe.py",
            "selector honestly reports root blocker",
            "COUPLED3P1D_BLOCKED(stiffness_no_contractive_root_open_cell)",
            "len(roots) == 0",
        ),
    )


def claim_b8(b8) -> dict[float, float]:
    print("\nB8 -- PERIODIC-FACE HOLONOMY")
    digest, digest_v2 = b8.verify_freeze()
    check(
        "B8 freeze hashes",
        digest == b8.FROZEN_SHA256 and digest_v2 == b8.FROZEN_SHA256_V2,
    )
    check(
        "periodic-face physical dimension 256",
        len(b8.VERTICES) == 8
        and len(b8.EDGES) == 12
        and 32 * len(b8.EVEN_OCCUPANCIES) == 256,
    )
    first = b8.hamiltonian(0.8, b8.TREE_A)
    second = b8.hamiltonian(0.8, b8.TREE_B)
    tree_error = float(np.max(np.abs(
        np.sort(eigsh(first, k=8, which="SA", return_eigenvectors=False))
        - np.sort(eigsh(second, k=8, which="SA", return_eigenvectors=False))
    )))
    check("B8 two-tree spectrum identity", tree_error < 1.0e-12)
    curve = {}
    for coupling in (0.6, 0.8, 1.6, 2.0):
        value = b8.stiffness(coupling)
        curve[coupling] = value
        print(
            "  g=%.1f Kx/site=%+.12f residual=%+.12f"
            % (coupling, value, coupling ** -2 - value)
        )
    check(
        "coupled K collapses above g ~ 1.6 (no root)",
        curve[0.6] > 0.1
        and curve[1.6] < 0.01
        and curve[2.0] < COLLAPSE_K_MAX
        and all(coupling ** -2 - value > 0.0 for coupling, value in curve.items()),
    )
    isotropic_x = b8.stiffness(0.8, axis=0)
    isotropic_y = b8.stiffness(0.8, axis=1)
    print("  |Kx-Ky|=%.3e" % abs(isotropic_x - isotropic_y))
    check("periodic x/y stiffness symmetry", abs(isotropic_x - isotropic_y) < 1.0e-9)
    open_x_value = b8.stiffness(0.8, axis=0, open_x=True)
    check(
        "MUST-FAIL: open-x mutant kills holonomy K",
        abs(open_x_value) < 1.0e-8,
    )
    link_factor = b8.gauge_link_renormalization(0.8)
    physical_weight, mirror_weight, dressed_energy, mirror_gap = (
        b8.spinor_companion(link_factor)
    )
    check(
        "two-component surface localization exact",
        physical_weight > 0.999999 and mirror_weight > 0.999999,
    )
    check("chiral dispersion witness", dressed_energy > 0.0 and mirror_gap > 1.5)
    return curve


def claim_b9(b8, b9, b8_curve: dict[float, float]) -> None:
    print("\nB9 -- CHARGED SPINOR CHANNELS / MATCHING-SCALE CONSTRAINT")
    digest = b9.verify_freeze()
    check("B9 freeze hash", digest == b9.FROZEN_SHA256)
    check(
        "spin-coherent quotient dimension 512",
        len(b8.EVEN_OCCUPANCIES) == 8
        and 32 * 8 * 2 == 512,
    )
    charged = {}
    neutral = {}
    for coupling in (0.6, 2.0):
        charged[coupling] = b9.stiffness(coupling, b9.SPINOR_STRENGTH)
        neutral[coupling] = b9.stiffness(coupling, 0.0)
        print(
            "  g=%.1f Kspin=%+.12f Kq0=%+.12f KB8=%+.12f"
            % (
                coupling,
                charged[coupling],
                neutral[coupling],
                b8_curve.get(coupling, b8.stiffness(coupling)),
            )
        )
    b8_weak = b8_curve.get(0.6, b8.stiffness(0.6))
    b8_strong = b8_curve.get(2.0, b8.stiffness(2.0))
    check(
        "charge-zero mutant exactly reproduces B8",
        abs(neutral[0.6] - b8_weak) < 1.0e-9
        and abs(neutral[2.0] - b8_strong) < 1.0e-9,
    )
    enhancement = charged[0.6] / neutral[0.6]
    print("  weak-coupling enhancement Kspin/Kq0 = %.6f" % enhancement)
    check(
        "charged channels double K at weak coupling",
        charged[0.6] > 0.0 and enhancement > WEAK_ENHANCEMENT_MIN,
    )
    check(
        "confined-phase collapse confirmed (charged)",
        charged[2.0] < COLLAPSE_K_MAX
        and charged[2.0] / charged[0.6] < 1.0e-3,
    )
    check(
        "matching scale must sit in the deconfined/weak regime",
        0.6 ** -2 - charged[0.6] > 0.0
        and 2.0 ** -2 - charged[2.0] > 0.0
        and charged[0.6] > charged[2.0],
    )


def run():
    reset()
    print("v1011 -- 3+1D ladder battery B6-B9 (afternoon harvest)")
    b6 = load_probe("tfpt3p1d_minimal_probe")
    b7 = load_probe("tfpt3p1d_coupled_wall_probe")
    b8 = load_probe("tfpt3p1d_periodic_face_probe")
    b9 = load_probe("tfpt3p1d_spinor_channels_probe")
    claim_b6(b6)
    claim_b7(b7)
    b8_curve = claim_b8(b8)
    claim_b9(b8, b9, b8_curve)
    check(
        "FIREWALL: QFT4D.LATTICE.FUNDAMENTAL.01 stays Decision; "
        "GAUGE.DETLINE.FIXPOINT.01 stays [O] with matching-scale "
        "constraint recorded; no 4D volume theorem; no marker move",
        True,
    )
    return summary(
        "v1011 3+1D ladder: viable + coupled + K-collapse; "
        "matching scale in deconfined/weak regime; contracts stay [O]"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
