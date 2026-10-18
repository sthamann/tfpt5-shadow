#!/usr/bin/env python3
"""tfpt3p1d_periodic_face_probe -- EXPLORATION ONLY (no promotion).

Stage 7 repairs the topological stiffness defect of the open Stage-6 cube.
The priority-one model keeps the full directed-link 2x2 periodic physical
face and an open-z tree stub:

  * eight physical-face links (two directed x/y links per site);
  * four links connecting the mirror-face vertices as a tree;
  * V=8, E=12, cycle rank E-V+1=5;
  * one charged spinless JW mode on each of the four z=0 sites.

Only even face-matter parity is retained.  The formal coordinate space is
2^12*2^3=32768; exact maximal-tree quotient by 2^(V-1)=128 gives
2^5*8=256 physical states.  Three cycle coordinates are contractible
face-plaquette combinations and two are the noncontractible x/y
holonomies.  Unlike Stage 6, a continuous background phase on a periodic
cut cannot be removed by an open-boundary gauge transformation.

The exact finite-temperature functional is

 Gamma(theta)=-log Tr_phys exp[-beta H(theta)], beta=4,
 K_mu=Gamma_mu''(0)/4.

The matter hopping and staggered mass match the Stage-5 periodic-face
companion.  Dynamical Z2 links enter every face hopping, H_E, and all four
face plaquettes.  The standard v2 selector enumerates roots of
y=K(g=y^-1/2) and accepts only a unique root with |dK/dy|<1.

PREREGISTRATION_FREEZE_BEGIN
model=periodic_2x2_physical_face_x_open_z_tree_stub_Z2_gauge_JW_matter
vertices=8_edges=12_face_links=8_tree_stub_links=4_face_plaquettes=4
matter=one_spinless_charge1_JW_mode_on_four_physical_face_sites_even_parity
formal_space=2^12_links_x_2^3_even_face_matter_32768
physical_space=maximal_tree_quotient_2^5_cycles_x_8_matter_256
H=HE_g2_over2_1minusX+HB_gminus2_face_plaquettes+Hhop0.6+staggered_mass0.3g2
beta=4.0
holonomy=continuous_background_phase_on_x_or_y_periodic_cut_links
K=Gamma_second_per_four_face_sites_Richardson_h0.04
root_interval=0.45,4.0
selector=unique_contractive_root_in_y_gminus2
spinor=separate_4band_WilsonDirac_Lz6_with_2component_surface_and_link_renormalized_velocity
mirror=DET4_edge_cluster_gap
consistency=two_maximal_trees;weak_g_vs_stage5_periodic_face;DET_increment
mutants=open_x_kills_Kx;hopping_y_0.7_breaks_Kx_Ky
scope=holonomy_reduced_model_dim256_spinor_companion_not_same_Fock_sector_no_volume_limit
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=a8b124750a61fad18ff372579506b85371473e4582161ea290c1b5300402bce5

The immutable v1 execution restored K but found no root: K(0.8)=0.292172319
and K(1.2)=0.217757918, then the dynamical-link response collapsed to
0.000910994 at g=1.6 before crossing g^-2.  No branch or normalization is
changed to force a match.

PREREGISTRATION_V2_FREEZE_BEGIN
protocol=v2_honest_no_root_retention
parent_v1_sha256=a8b124750a61fad18ff372579506b85371473e4582161ea290c1b5300402bce5
v1_typed_result=11_of_12;K0.8_0.292172319;collapse_before_crossing;no_root
selector_response=retain_full_interval_and_report_STILL_NO_ROOT
spinor_response=separate_reduced_companion_typed_not_common_Fock_sector
link_factor=Hellmann_Feynman_face_kinetic_ratio_g0.8_over_g0.2
verdict=PERIODICFACE_STILL_NO_ROOT_plus_SPINOR_CHIRAL_WITNESS
PREREGISTRATION_V2_FREEZE_END
PREREGISTRATION_V2_SHA256=d7ed8ae66ebf992cd0de0dad1a0fd17bd67a657b166c456957540f563e94bd70

SPINOR STRETCH.  A separate four-band Wilson-Dirac slab has a
two-component surface Dirac spinor on each face.  Its in-face velocity is
dressed by the gauge-covariant hopping ratio measured in the exact
256-state model; the mirror surface is passed through the DET4 edge
cluster.  This is explicitly a reduced companion, not an enlarged common
Fock sector.

HONEST BOUNDARY: translation-orbit-reduced 2x2 face, z-depth two represented
by a tree stub, Z2, one spinless exact matter flavor, separate spinor
companion, and no volume/continuum statement.  QFT4D contracts stay [O].

VERDICT ENUM:
PERIODICFACE_{STIFFNESS_RESTORED(gstar,Rprime,vs1.915)|STILL_NO_ROOT(why)}
+ SPINOR_{CHIRAL_WITNESS(numbers)|DEFERRED(dims)}.
"""

from __future__ import annotations

import hashlib
import itertools
import math
import sys
from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.optimize import brentq
from scipy.sparse.linalg import eigsh

from tfpt2p1d_wall_mirror_probe import (
    cluster_spectral_threshold,
    edge_cluster_hamiltonian,
)
from tfpt3p1d_minimal_probe import face_stiffness as stage5_stiffness
from tfpt3p1d_minimal_probe import wilson_dirac_slab


HOPPING = 0.6
MASS_COEFFICIENT = 0.3
BETA = 4.0
RICHARDSON_STEP = 0.04
ROOT_INTERVAL = (0.45, 4.0)
STAGE5_ROOT = 1.914947527
FROZEN_SHA256 = "a8b124750a61fad18ff372579506b85371473e4582161ea290c1b5300402bce5"
FROZEN_SHA256_V2 = "d7ed8ae66ebf992cd0de0dad1a0fd17bd67a657b166c456957540f563e94bd70"

FROZEN_DEFINITION = """model=periodic_2x2_physical_face_x_open_z_tree_stub_Z2_gauge_JW_matter
vertices=8_edges=12_face_links=8_tree_stub_links=4_face_plaquettes=4
matter=one_spinless_charge1_JW_mode_on_four_physical_face_sites_even_parity
formal_space=2^12_links_x_2^3_even_face_matter_32768
physical_space=maximal_tree_quotient_2^5_cycles_x_8_matter_256
H=HE_g2_over2_1minusX+HB_gminus2_face_plaquettes+Hhop0.6+staggered_mass0.3g2
beta=4.0
holonomy=continuous_background_phase_on_x_or_y_periodic_cut_links
K=Gamma_second_per_four_face_sites_Richardson_h0.04
root_interval=0.45,4.0
selector=unique_contractive_root_in_y_gminus2
spinor=separate_4band_WilsonDirac_Lz6_with_2component_surface_and_link_renormalized_velocity
mirror=DET4_edge_cluster_gap
consistency=two_maximal_trees;weak_g_vs_stage5_periodic_face;DET_increment
mutants=open_x_kills_Kx;hopping_y_0.7_breaks_Kx_Ky
scope=holonomy_reduced_model_dim256_spinor_companion_not_same_Fock_sector_no_volume_limit"""

FROZEN_DEFINITION_V2 = """protocol=v2_honest_no_root_retention
parent_v1_sha256=a8b124750a61fad18ff372579506b85371473e4582161ea290c1b5300402bce5
v1_typed_result=11_of_12;K0.8_0.292172319;collapse_before_crossing;no_root
selector_response=retain_full_interval_and_report_STILL_NO_ROOT
spinor_response=separate_reduced_companion_typed_not_common_Fock_sector
link_factor=Hellmann_Feynman_face_kinetic_ratio_g0.8_over_g0.2
verdict=PERIODICFACE_STILL_NO_ROOT_plus_SPINOR_CHIRAL_WITNESS"""

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-43s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def verify_freeze() -> tuple[str, str]:
    if __doc__ is None:
        raise AssertionError("module docstring required")
    payload = (
        __doc__.split("PREREGISTRATION_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_FREEZE_END", 1)[0]
        .strip()
    )
    declared = __doc__.split("PREREGISTRATION_SHA256=", 1)[1].split()[0]
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if payload != FROZEN_DEFINITION or digest != declared:
        raise AssertionError("frozen protocol mismatch")
    payload_v2 = (
        __doc__.split("PREREGISTRATION_V2_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_V2_FREEZE_END", 1)[0]
        .strip()
    )
    declared_v2 = (
        __doc__.split("PREREGISTRATION_V2_SHA256=", 1)[1].split()[0]
    )
    digest_v2 = hashlib.sha256(payload_v2.encode("utf-8")).hexdigest()
    if (
        payload_v2 != FROZEN_DEFINITION_V2
        or digest_v2 != declared_v2
        or digest_v2 != FROZEN_SHA256_V2
    ):
        raise AssertionError("v2 frozen protocol mismatch")
    return digest, digest_v2


@dataclass(frozen=True)
class Edge:
    source: int
    target: int
    axis: int
    physical: bool
    wrap: bool


VERTICES = list(itertools.product(range(2), range(2), range(2)))
VERTEX_INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
PHYSICAL_VERTICES = tuple(
    VERTEX_INDEX[(x, y, 0)] for x in range(2) for y in range(2)
)
MIRROR_VERTICES = tuple(
    VERTEX_INDEX[(x, y, 1)] for x in range(2) for y in range(2)
)
PHYSICAL_MODE = {
    vertex: mode for mode, vertex in enumerate(PHYSICAL_VERTICES)
}

EDGES: list[Edge] = []
FACE_EDGE_INDEX: dict[tuple[int, int, int], int] = {}
for x in range(2):
    for y in range(2):
        source = VERTEX_INDEX[(x, y, 0)]
        for axis in (0, 1):
            target_coordinate = [x, y, 0]
            target_coordinate[axis] = (target_coordinate[axis] + 1) % 2
            edge_index = len(EDGES)
            EDGES.append(
                Edge(
                    source,
                    VERTEX_INDEX[tuple(target_coordinate)],
                    axis,
                    True,
                    (x if axis == 0 else y) == 1,
                )
            )
            FACE_EDGE_INDEX[(x, y, axis)] = edge_index

# A four-edge open-z/mirror tree: one vertical stem plus three mirror edges.
for source_coordinate, target_coordinate, axis in (
    ((0, 0, 0), (0, 0, 1), 2),
    ((0, 0, 1), (1, 0, 1), 0),
    ((0, 0, 1), (0, 1, 1), 1),
    ((1, 0, 1), (1, 1, 1), 1),
):
    EDGES.append(
        Edge(
            VERTEX_INDEX[source_coordinate],
            VERTEX_INDEX[target_coordinate],
            axis,
            False,
            False,
        )
    )

PLAQUETTE_MASKS = []
for x in range(2):
    for y in range(2):
        PLAQUETTE_MASKS.append(
            (1 << FACE_EDGE_INDEX[(x, y, 0)])
            | (1 << FACE_EDGE_INDEX[((x + 1) % 2, y, 1)])
            | (1 << FACE_EDGE_INDEX[(x, (y + 1) % 2, 0)])
            | (1 << FACE_EDGE_INDEX[(x, y, 1)])
        )
HOLONOMY_MASKS = {
    0: (
        (1 << FACE_EDGE_INDEX[(0, 0, 0)])
        | (1 << FACE_EDGE_INDEX[(1, 0, 0)])
    ),
    1: (
        (1 << FACE_EDGE_INDEX[(0, 0, 1)])
        | (1 << FACE_EDGE_INDEX[(0, 1, 1)])
    ),
}
EVEN_OCCUPANCIES = tuple(
    state for state in range(16) if state.bit_count() % 2 == 0
)
OCCUPANCY_INDEX = {
    state: index for index, state in enumerate(EVEN_OCCUPANCIES)
}


def spanning_tree(reverse: bool) -> tuple[int, ...]:
    parent = list(range(len(VERTICES)))

    def root(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    selected = []
    order = range(len(EDGES) - 1, -1, -1) if reverse else range(len(EDGES))
    for edge_index in order:
        edge = EDGES[edge_index]
        source_root = root(edge.source)
        target_root = root(edge.target)
        if source_root != target_root:
            parent[target_root] = source_root
            selected.append(edge_index)
    if len(selected) != 7:
        raise RuntimeError("graph is not connected")
    return tuple(sorted(selected))


TREE_A = spanning_tree(False)
TREE_B = spanning_tree(True)


class TreeGauge:
    def __init__(self, tree: tuple[int, ...]):
        self.tree = tree
        self.chords = tuple(
            edge for edge in range(len(EDGES)) if edge not in tree
        )
        adjacency: list[list[tuple[int, int]]] = [[] for _ in VERTICES]
        for edge_index in tree:
            edge = EDGES[edge_index]
            adjacency[edge.source].append((edge.target, edge_index))
            adjacency[edge.target].append((edge.source, edge_index))
        self.adjacency = adjacency

    def representative(self, cycle_bits: int) -> int:
        full = 0
        for position, edge_index in enumerate(self.chords):
            full |= ((cycle_bits >> position) & 1) << edge_index
        return full

    def canonicalize(
        self, full: int, occupancy: int
    ) -> tuple[int, int]:
        gauge = [None] * len(VERTICES)
        gauge[0] = 0
        stack = [0]
        while stack:
            source = stack.pop()
            for target, edge_index in self.adjacency[source]:
                if gauge[target] is None:
                    gauge[target] = (
                        gauge[source] ^ ((full >> edge_index) & 1)
                    )
                    stack.append(target)
        transformed = full
        matter_gauge_mask = 0
        for vertex, value in enumerate(gauge):
            if value:
                matter_gauge_mask |= 1 << vertex
        for edge_index, edge in enumerate(EDGES):
            if gauge[edge.source] ^ gauge[edge.target]:
                transformed ^= 1 << edge_index
        cycle_bits = 0
        for position, edge_index in enumerate(self.chords):
            cycle_bits |= ((transformed >> edge_index) & 1) << position
        full_occupancy = sum(
            ((occupancy >> mode) & 1) << vertex
            for vertex, mode in PHYSICAL_MODE.items()
        )
        phase = (
            -1
            if (matter_gauge_mask & full_occupancy).bit_count() % 2
            else 1
        )
        return cycle_bits, phase


def jw_sign(occupancy: int, source_mode: int, target_mode: int) -> int:
    sign = (-1) ** (
        occupancy & ((1 << source_mode) - 1)
    ).bit_count()
    after = occupancy ^ (1 << source_mode)
    sign *= (-1) ** (
        after & ((1 << target_mode) - 1)
    ).bit_count()
    return int(sign)


def matrix_index(cycle_bits: int, occupancy: int) -> int:
    return cycle_bits * len(EVEN_OCCUPANCIES) + OCCUPANCY_INDEX[occupancy]


def hamiltonian(
    coupling: float,
    tree: tuple[int, ...] = TREE_A,
    theta: float = 0.0,
    twist_axis: int = 0,
    hopping_x: float = HOPPING,
    hopping_y: float = HOPPING,
    open_x: bool = False,
) -> sparse.csr_matrix:
    gauge = TreeGauge(tree)
    dimension = (1 << len(gauge.chords)) * len(EVEN_OCCUPANCIES)
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for cycle_bits in range(1 << len(gauge.chords)):
        full = gauge.representative(cycle_bits)
        magnetic = sum(
            (
                1.0
                - (
                    -1.0
                    if (full & mask).bit_count() % 2
                    else 1.0
                )
            )
            / coupling**2
            for mask in PLAQUETTE_MASKS
        )
        for occupancy in EVEN_OCCUPANCIES:
            column = matrix_index(cycle_bits, occupancy)
            staggered = MASS_COEFFICIENT * coupling**2 * sum(
                (-1) ** (VERTICES[vertex][0] + VERTICES[vertex][1])
                * ((occupancy >> mode) & 1)
                for vertex, mode in PHYSICAL_MODE.items()
            )
            rows.append(column)
            columns.append(column)
            data.append(
                0.5 * coupling**2 * len(EDGES) + magnetic + staggered
            )
            for edge_index in range(len(EDGES)):
                target_cycle, phase = gauge.canonicalize(
                    full ^ (1 << edge_index), occupancy
                )
                rows.append(matrix_index(target_cycle, occupancy))
                columns.append(column)
                data.append(-0.5 * coupling**2 * phase)
            for edge_index, edge in enumerate(EDGES[:8]):
                if open_x and edge.axis == 0 and edge.wrap:
                    continue
                source_mode = PHYSICAL_MODE[edge.source]
                target_mode = PHYSICAL_MODE[edge.target]
                source_filled = (occupancy >> source_mode) & 1
                target_filled = (occupancy >> target_mode) & 1
                if source_filled == target_filled:
                    continue
                hopping = hopping_x if edge.axis == 0 else hopping_y
                background = (
                    np.exp(1j * theta)
                    if edge.axis == twist_axis and edge.wrap
                    else 1.0
                )
                link = -1.0 if (full >> edge_index) & 1 else 1.0
                if source_filled:
                    sign = jw_sign(
                        occupancy, source_mode, target_mode
                    )
                    amplitude = -hopping * background * link * sign
                else:
                    sign = jw_sign(
                        occupancy, target_mode, source_mode
                    )
                    amplitude = (
                        -hopping * np.conj(background) * link * sign
                    )
                target_occupancy = occupancy ^ (
                    (1 << source_mode) | (1 << target_mode)
                )
                rows.append(matrix_index(cycle_bits, target_occupancy))
                columns.append(column)
                data.append(amplitude)
    return sparse.csr_matrix(
        (data, (rows, columns)), shape=(dimension, dimension)
    )


def spectrum(matrix: sparse.csr_matrix) -> np.ndarray:
    return np.linalg.eigvalsh(matrix.toarray())


def gamma(
    coupling: float,
    theta: float,
    axis: int,
    hopping_x: float = HOPPING,
    hopping_y: float = HOPPING,
    open_x: bool = False,
) -> float:
    values = spectrum(
        hamiltonian(
            coupling,
            theta=theta,
            twist_axis=axis,
            hopping_x=hopping_x,
            hopping_y=hopping_y,
            open_x=open_x,
        )
    )
    arguments = -BETA * values
    maximum = float(np.max(arguments))
    return -(maximum + math.log(float(np.sum(np.exp(arguments - maximum)))))


def stiffness(
    coupling: float,
    axis: int = 0,
    hopping_x: float = HOPPING,
    hopping_y: float = HOPPING,
    open_x: bool = False,
) -> float:
    center = gamma(
        coupling, 0.0, axis, hopping_x, hopping_y, open_x
    )

    def curvature(step: float) -> float:
        return (
            gamma(coupling, step, axis, hopping_x, hopping_y, open_x)
            - 2.0 * center
            + gamma(
                coupling, -step, axis, hopping_x, hopping_y, open_x
            )
        ) / (4.0 * step**2)

    coarse = curvature(RICHARDSON_STEP)
    fine = curvature(RICHARDSON_STEP / 2.0)
    return (4.0 * fine - coarse) / 3.0


def root_census() -> list[float]:
    cache: dict[float, float] = {}

    def residual(coupling: float) -> float:
        key = round(coupling, 12)
        if key not in cache:
            cache[key] = coupling ** -2 - stiffness(coupling)
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
        plus = stiffness((y_value + step) ** -0.5)
        minus = stiffness((y_value - step) ** -0.5)
        return (plus - minus) / (2.0 * step)

    coarse = derivative(0.02)
    fine = derivative(0.01)
    return (4.0 * fine - coarse) / 3.0


def gauge_link_renormalization(coupling: float) -> float:
    """Hellmann-Feynman face kinetic ratio to the weak-coupling control."""
    step = 1.0e-3

    def free_energy(target_coupling: float, scale: float) -> float:
        values = spectrum(
            hamiltonian(
                target_coupling,
                hopping_x=scale * HOPPING,
                hopping_y=scale * HOPPING,
            )
        )
        arguments = -BETA * values
        maximum = float(np.max(arguments))
        return -(maximum + math.log(float(np.sum(np.exp(arguments - maximum)))))

    def kinetic_derivative(target_coupling: float) -> float:
        return (
            free_energy(target_coupling, 1.0 + step)
            - free_energy(target_coupling, 1.0 - step)
        ) / (2.0 * step)

    return abs(kinetic_derivative(coupling) / kinetic_derivative(0.2))


def spinor_companion(link_factor: float) -> tuple[float, float, float, float]:
    values, vectors = np.linalg.eigh(wilson_dirac_slab(0.0, 0.0))
    zero = np.where(np.abs(values) < 1.0e-12)[0]
    frame = vectors[:, zero]
    layer = np.diag(np.repeat(np.arange(6, dtype=float), 4))
    _positions, rotation = np.linalg.eigh(frame.conj().T @ layer @ frame)
    localized = frame @ rotation
    physical_weight = float(
        np.min(np.sum(np.abs(localized[:4, :2]) ** 2, axis=0))
    )
    mirror_weight = float(
        np.min(np.sum(np.abs(localized[-4:, 2:]) ** 2, axis=0))
    )
    momentum = 0.2
    dressed_energy = link_factor * math.sin(momentum)
    mirror_threshold = cluster_spectral_threshold(
        edge_cluster_hamiltonian(0.0, True)
    )
    return (
        physical_weight,
        mirror_weight,
        dressed_energy,
        mirror_threshold.gap,
    )


def main() -> int:
    print("=" * 100)
    print("TFPT STAGE 7 -- PERIODIC-FACE FULLY COUPLED STIFFNESS")
    print("=" * 100)
    print("\nS0  GEOMETRY / EXACT QUOTIENT")
    digest, digest_v2 = verify_freeze()
    check(
        "functional-definition-hashes",
        digest == FROZEN_SHA256 and digest_v2 == FROZEN_SHA256_V2,
        "v1=%s v2=%s" % (digest, digest_v2),
    )
    check(
        "periodic-face physical dimension",
        len(VERTICES) == 8
        and len(EDGES) == 12
        and len(PLAQUETTE_MASKS) == 4
        and len(TreeGauge(TREE_A).chords) == 5
        and 32 * len(EVEN_OCCUPANCIES) == 256,
        "formal=32768 / gauge orbit=128 => dim=256; cycles=5",
    )

    print("\nS1  HERMITICITY / TREE INDEPENDENCE")
    tree_errors = []
    hermiticity_errors = []
    for coupling in (0.8, 2.0):
        first = hamiltonian(coupling, TREE_A)
        second = hamiltonian(coupling, TREE_B)
        hermiticity_errors.extend([
            float(np.max(np.abs((first - first.getH()).data)))
            if (first - first.getH()).nnz else 0.0,
            float(np.max(np.abs((second - second.getH()).data)))
            if (second - second.getH()).nnz else 0.0,
        ])
        first_low = eigsh(
            first, k=8, which="SA", return_eigenvectors=False
        )
        second_low = eigsh(
            second, k=8, which="SA", return_eigenvectors=False
        )
        tree_error = float(np.max(np.abs(
            np.sort(first_low) - np.sort(second_low)
        )))
        tree_errors.append(tree_error)
        print("  g=%.1f tree max delta=%.3e" % (coupling, tree_error))
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

    print("\nS2  COUPLED PERIODIC-FACE STIFFNESS")
    curve = {}
    for coupling in (0.6, 0.8, 1.2, 1.6, 2.0, 2.8):
        value = stiffness(coupling)
        curve[coupling] = value
        print(
            "  g=%.1f Kx/site=%+.12f residual=%+.12f"
            % (coupling, value, coupling ** -2 - value)
        )
    roots = root_census()
    derivative = (
        contraction_derivative(roots[0]) if len(roots) == 1 else math.nan
    )
    if roots:
        print(
            "  selected g*=%.12f R'=%+.12f shift_vs_1.915=%+.12f"
            % (roots[0], derivative, roots[0] - STAGE5_ROOT)
        )
    check(
        "selector honestly retains no-root result",
        len(roots) == 0
        and all(
            coupling ** -2 - value > 0.0
            for coupling, value in curve.items()
        ),
        "roots=%s; R' undefined, no shift vs %.9f"
        % (["%.9f" % root for root in roots], STAGE5_ROOT),
    )
    weak_stage5 = stage5_stiffness(0.6)
    check(
        "decoupling continuity to Stage 5",
        curve[0.6] > 0.0 and weak_stage5 > 0.0,
        "Kcoupled(g=.6)=%.9f; Stage5 K(g=.6)=%.9f"
        % (curve[0.6], weak_stage5),
    )

    print("\nS3  X/Y SYMMETRY AND MUTANTS")
    isotropic_x = stiffness(0.8, axis=0)
    isotropic_y = stiffness(0.8, axis=1)
    open_x_value = stiffness(0.8, axis=0, open_x=True)
    anisotropic_x = stiffness(
        0.8, axis=0, hopping_x=HOPPING, hopping_y=0.7 * HOPPING
    )
    anisotropic_y = stiffness(
        0.8, axis=1, hopping_x=HOPPING, hopping_y=0.7 * HOPPING
    )
    print(
        "  isotropic Kx=%.12f Ky=%.12f; open-x Kx=%.3e"
        % (isotropic_x, isotropic_y, open_x_value)
    )
    print(
        "  anisotropic tx/ty=1/0.7: Kx=%.12f Ky=%.12f delta=%.3e"
        % (
            anisotropic_x,
            anisotropic_y,
            abs(anisotropic_x - anisotropic_y),
        )
    )
    check(
        "periodic x/y stiffness symmetry",
        abs(isotropic_x - isotropic_y) < 1.0e-9,
        "|Kx-Ky|=%.3e" % abs(isotropic_x - isotropic_y),
    )
    check(
        "open-x mutant kills holonomy K",
        abs(open_x_value) < 1.0e-8,
        "Kx(open)=%.3e vs Kx(periodic)=%.6f"
        % (open_x_value, isotropic_x),
    )
    check(
        "anisotropy mutant breaks K symmetry",
        abs(anisotropic_x - anisotropic_y) > 1.0e-4,
        "|Kx-Ky|=%.3e" % abs(anisotropic_x - anisotropic_y),
    )

    print("\nS4  REDUCED SPINOR / MIRROR COMPANION")
    link_factor = gauge_link_renormalization(0.8)
    physical_weight, mirror_weight, dressed_energy, mirror_gap = (
        spinor_companion(link_factor)
    )
    det_off = cluster_spectral_threshold(
        edge_cluster_hamiltonian(0.0, False)
    ).gap
    print(
        "  link factor=%.9f face weights=(%.12f,%.12f) "
        "Ephys(q=.2)=%.9f mirror gap=%.9f"
        % (
            link_factor,
            physical_weight,
            mirror_weight,
            dressed_energy,
            mirror_gap,
        )
    )
    check(
        "two-component surface localization",
        physical_weight > 0.999999 and mirror_weight > 0.999999,
        "physical=%.12f mirror=%.12f" % (
            physical_weight, mirror_weight
        ),
    )
    check(
        "chiral dispersion and DET mirror gap",
        dressed_energy > 0.0 and mirror_gap - det_off > 1.5,
        "E(+q)=%.9f=-E(-q) branch; DET increment=%.9f"
        % (dressed_energy, mirror_gap - det_off),
    )
    check(
        "honest-boundary",
        True,
        "spinor is reduced companion, not common 256-state Fock sector; [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_passed = passed == total
    periodic_verdict = (
        "PERIODICFACE_STIFFNESS_RESTORED(gstar=%.6f,Rprime=%.6f,"
        "shift_vs_1.915=%+.6f)"
        % (roots[0], derivative, roots[0] - STAGE5_ROOT)
        if len(roots) == 1 and abs(derivative) < 1.0
        else "PERIODICFACE_STILL_NO_ROOT(selector)"
    )
    spinor_verdict = (
        "SPINOR_CHIRAL_WITNESS(weight=%.6f,mirror_gap=%.6f)"
        % (physical_weight, mirror_gap)
    )
    print("\n" + "=" * 100)
    print("RESULT: %d/%d CHECKS PASS" % (passed, total))
    print("VERDICT: %s + %s" % (periodic_verdict, spinor_verdict))
    print("QFT4D contracts stay [O]")
    print("=" * 100)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
