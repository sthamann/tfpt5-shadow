#!/usr/bin/env python3
"""tfpt3p1d_coupled_wall_probe -- EXPLORATION ONLY (no promotion).

Stage 6 removes the stage-5 Kronecker sum on the largest exact sector that
is cheap enough for repeated Lanczos solves.  The spatial graph is one open
2x2x2 cube: V=8, E=12, P=6.  One charged spinless JW mode lives at every
site; z=0 is the physical face and z=1 the mirror face.  The formal
coordinate-link/even-matter space has 2^12*2^7=524288 states.  Quotienting
the 2^(V-1)=128 local Z2 gauge orbit by a maximal tree leaves

                    2^(E-V+1)*2^(V-1) = 32*128 = 4096

physical states.  This is exact gauge fixing, not link freezing.

In the coordinate-link basis,

 H_E=(g^2/2) sum_l(1-X_l),
 H_B=(1/g^2) sum_p(1-U_p),
 H_hop=-t sum_<xy>(exp(i A_xy)c_y^dag U_xy c_x+h.c.),
 H_m=m sum_x(2z_x-1)n_x.

The vertex JW order is lexicographic (x,y,z), z fastest.  Gauge fixing
sets the seven tree links to +1.  Acting with X_l is followed by the unique
vertex gauge transformation that restores the tree gauge; its fermionic
sign (-1)^(sum eta_x n_x) is retained.  Two distinct maximal trees must
therefore give identical spectra.

The mirror interaction is a genuinely gauge-covariant DET4 analogue.
For the four mirror sites, |0> and |F> are joined by the two-link matching
S on the mirror face:

 P_phi=(|0>+exp(i phi) S|F>)(h.c.)/2,  H_DET=lambda(1-P_phi).

The boundary of S is all four mirror vertices, so the occupancy change and
link string cancel in every local Gauss generator.  The physical face has
an oriented quarter-flux hopping pattern; the mirror face has the conjugate
orientation before DET, providing the finite-cell wall/mirror pair.

PREREGISTRATION_FREEZE_BEGIN
model=single_open_cube_Z2_links_x_8_JW_sites_x_gauge_covariant_mirror_DET4
geometry=2x2x2_open_V8_E12_P6_physical_z0_mirror_z1
formal_space=2^12_links_x_2^7_even_matter_524288
physical_space=maximal_tree_quotient_2^5_cycles_x_2^7_matter_4096
JW_order=lexicographic_xyz_z_fastest
H=HE_g2_over2_1minusX+HB_gminus2_1minusUp+Hhop_t0.35+Hmass0.15+HDET2
wall=oriented_physical_face_flux_plus_pi_over2_mirror_conjugate
DET=gauge_covariant_rank1_vacuum_full_mirror_projector_phi_pi_over7
tree_check=default_Kruskal_vs_reverse_Kruskal_lowest8_spectra
couplings=0.8,2.0
confinement=one_plaquette_vs_two_perpendicular_plaquette_surface
backreaction=gauge_covariant_face_bond_response_over_flat_link_control
stiffness=physical_face_plaquette_holonomy_ground_energy_curvature_per_site
stiffness_difference=Richardson_h0.04
root_interval=0.45,3.5
selector=unique_contractive_root_in_y_gminus2
mutants=cyclic_non_tree_gauge_set_rank_defect;hopping_zero_Kronecker_continuity
scope=open_cube_flux_curvature_not_flat_torus_holonomy_no_volume_scaling
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=142b7d8014b6e314bc773df8b3d6278211720c0396d2f56407a724fbc60f199d

The immutable v1 execution found four negatives: its DET implementation
incorrectly flipped the matching links instead of multiplying by U_S,
making tree spectra differ by 1.96e-3; face-number thresholds did not
separate the edges; theta=0 was a flux-energy maximum; and no fixed point
existed.  The following v2 correction was declared before rerunning:

PREREGISTRATION_V2_FREEZE_BEGIN
protocol=v2_coordinate_string_minimum_holonomy_and_blocked_selector
parent_v1_sha256=142b7d8014b6e314bc773df8b3d6278211720c0396d2f56407a724fbc60f199d
v1_typed_result=8_of_12;tree_mismatch_1.96e-3;face_thresholds_equal;K_theta0_negative;no_root
DET_correction=U_string_multiplies_coordinate_state_and_does_not_flip_links
wall_flux=single_oriented_edge_plus_pi_over2_and_mirror_conjugate
wall_gate=finite_cell_total_gap_reported_not_claimed_gapless
mirror_gate=DET_on_minus_DET_off_total_gap_positive
stiffness_center=minimum_over_17_holonomy_samples
selector_outcome=no_root_is_typed_blocker_not_fitted_away
decoupling=weak_g_bond_response_approaches_exact_flat_link_control
verdict=COUPLED3P1D_BLOCKED_if_no_contractive_root
PREREGISTRATION_V2_FREEZE_END
PREREGISTRATION_V2_SHA256=b442d086156a326793c4e998540f466646e60e770eb777f2e5e6867c81edf5f9

Because the open cube is simply connected, it has no noncontractible flat
holonomy.  The reported fully coupled K is therefore the curvature under a
gauge-invariant physical-face plaquette holonomy, normalized per face site.
It is the honest minimal-cell replacement for the stage-5 periodic-face
number, and its root is compared numerically with 1.914947527, but the two
functionals are not claimed to be identical step-scaling schemes.

The wrong-gauge mutant fixes seven edges containing a cycle.  Its incidence
rank is six rather than V-1=7, leaving a local gauge transformation unfixed;
fermion states on that orbit acquire different phases, so the would-be
representative is not gauge invariant.  The decoupling control t=0 is an
exact Kronecker sum of gauge and diagonal matter/DET sectors; its spectrum
is compared with the explicit pairwise-sum construction.

HONEST BOUNDARY: one open cube, Z2, two reported couplings, no volume
scaling, no full four-component Wilson spinor, and plaquette-flux curvature
rather than a torus flat holonomy.  Chirality is a finite oriented-current
witness, not a continuum Weyl theorem.  QFT4D contracts stay [O].

VERDICT ENUM: COUPLED3P1D_{ALIVE(numbers)|BLOCKED(dims/method)}.
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


SHAPE = (2, 2, 2)
HOPPING = 0.35
MASS = 0.15
DET_STRENGTH = 2.0
DET_PHASE = math.pi / 7.0
TWIST_STEP = 0.04
ROOT_INTERVAL = (0.45, 3.5)
STAGE5_ROOT = 1.914947527
FROZEN_SHA256 = "142b7d8014b6e314bc773df8b3d6278211720c0396d2f56407a724fbc60f199d"
FROZEN_SHA256_V2 = "b442d086156a326793c4e998540f466646e60e770eb777f2e5e6867c81edf5f9"

FROZEN_DEFINITION = """model=single_open_cube_Z2_links_x_8_JW_sites_x_gauge_covariant_mirror_DET4
geometry=2x2x2_open_V8_E12_P6_physical_z0_mirror_z1
formal_space=2^12_links_x_2^7_even_matter_524288
physical_space=maximal_tree_quotient_2^5_cycles_x_2^7_matter_4096
JW_order=lexicographic_xyz_z_fastest
H=HE_g2_over2_1minusX+HB_gminus2_1minusUp+Hhop_t0.35+Hmass0.15+HDET2
wall=oriented_physical_face_flux_plus_pi_over2_mirror_conjugate
DET=gauge_covariant_rank1_vacuum_full_mirror_projector_phi_pi_over7
tree_check=default_Kruskal_vs_reverse_Kruskal_lowest8_spectra
couplings=0.8,2.0
confinement=one_plaquette_vs_two_perpendicular_plaquette_surface
backreaction=gauge_covariant_face_bond_response_over_flat_link_control
stiffness=physical_face_plaquette_holonomy_ground_energy_curvature_per_site
stiffness_difference=Richardson_h0.04
root_interval=0.45,3.5
selector=unique_contractive_root_in_y_gminus2
mutants=cyclic_non_tree_gauge_set_rank_defect;hopping_zero_Kronecker_continuity
scope=open_cube_flux_curvature_not_flat_torus_holonomy_no_volume_scaling"""

FROZEN_DEFINITION_V2 = """protocol=v2_coordinate_string_minimum_holonomy_and_blocked_selector
parent_v1_sha256=142b7d8014b6e314bc773df8b3d6278211720c0396d2f56407a724fbc60f199d
v1_typed_result=8_of_12;tree_mismatch_1.96e-3;face_thresholds_equal;K_theta0_negative;no_root
DET_correction=U_string_multiplies_coordinate_state_and_does_not_flip_links
wall_flux=single_oriented_edge_plus_pi_over2_and_mirror_conjugate
wall_gate=finite_cell_total_gap_reported_not_claimed_gapless
mirror_gate=DET_on_minus_DET_off_total_gap_positive
stiffness_center=minimum_over_17_holonomy_samples
selector_outcome=no_root_is_typed_blocker_not_fitted_away
decoupling=weak_g_bond_response_approaches_exact_flat_link_control
verdict=COUPLED3P1D_BLOCKED_if_no_contractive_root"""

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-44s %s" % ("PASS" if result else "FAIL", name, detail))
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
    if payload != FROZEN_DEFINITION:
        raise AssertionError("frozen payload mismatch")
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if digest != declared or digest != FROZEN_SHA256:
        raise AssertionError("frozen hash mismatch")
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
        raise AssertionError("v2 frozen hash mismatch")
    return digest, digest_v2


@dataclass(frozen=True)
class Edge:
    source: int
    target: int
    axis: int


@dataclass(frozen=True)
class Plaquette:
    axes: tuple[int, int]
    base: tuple[int, int, int]
    mask: int


VERTICES = list(itertools.product(*(range(length) for length in SHAPE)))
VERTEX_INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
EDGES: list[Edge] = []
for vertex in VERTICES:
    for axis in range(3):
        if vertex[axis] + 1 < SHAPE[axis]:
            target = list(vertex)
            target[axis] += 1
            EDGES.append(
                Edge(
                    VERTEX_INDEX[vertex],
                    VERTEX_INDEX[tuple(target)],
                    axis,
                )
            )
EDGE_INDEX = {
    tuple(sorted((edge.source, edge.target))): index
    for index, edge in enumerate(EDGES)
}
PLAQUETTES: list[Plaquette] = []
for base in VERTICES:
    for first_axis in range(3):
        for second_axis in range(first_axis + 1, 3):
            if (
                base[first_axis] + 1 >= SHAPE[first_axis]
                or base[second_axis] + 1 >= SHAPE[second_axis]
            ):
                continue
            first = list(base)
            first[first_axis] += 1
            second = list(base)
            second[second_axis] += 1
            diagonal = first.copy()
            diagonal[second_axis] += 1
            corners = (
                VERTEX_INDEX[base],
                VERTEX_INDEX[tuple(first)],
                VERTEX_INDEX[tuple(second)],
                VERTEX_INDEX[tuple(diagonal)],
            )
            mask = 0
            for pair in (
                (corners[0], corners[1]),
                (corners[0], corners[2]),
                (corners[1], corners[3]),
                (corners[2], corners[3]),
            ):
                mask |= 1 << EDGE_INDEX[tuple(sorted(pair))]
            PLAQUETTES.append(
                Plaquette((first_axis, second_axis), base, mask)
            )

EVEN_OCCUPANCIES = tuple(
    occupancy
    for occupancy in range(1 << len(VERTICES))
    if occupancy.bit_count() % 2 == 0
)
OCCUPANCY_INDEX = {
    occupancy: index for index, occupancy in enumerate(EVEN_OCCUPANCIES)
}
PHYSICAL_FACE = tuple(
    index for index, vertex in enumerate(VERTICES) if vertex[2] == 0
)
MIRROR_FACE = tuple(
    index for index, vertex in enumerate(VERTICES) if vertex[2] == 1
)
PHYSICAL_MASK = sum(1 << vertex for vertex in PHYSICAL_FACE)
MIRROR_MASK = sum(1 << vertex for vertex in MIRROR_FACE)


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
    if len(selected) != len(VERTICES) - 1:
        raise RuntimeError("failed to construct spanning tree")
    return tuple(sorted(selected))


TREE_A = spanning_tree(False)
TREE_B = spanning_tree(True)


class TreeGauge:
    def __init__(self, tree_edges: tuple[int, ...]):
        self.tree_edges = tree_edges
        self.chord_edges = tuple(
            edge for edge in range(len(EDGES)) if edge not in tree_edges
        )
        adjacency: list[list[tuple[int, int]]] = [
            [] for _ in range(len(VERTICES))
        ]
        for edge_index in tree_edges:
            edge = EDGES[edge_index]
            adjacency[edge.source].append((edge.target, edge_index))
            adjacency[edge.target].append((edge.source, edge_index))
        self.adjacency = adjacency

    def representative_bits(self, chord_bits: int) -> int:
        full_bits = 0
        for position, edge_index in enumerate(self.chord_edges):
            full_bits |= ((chord_bits >> position) & 1) << edge_index
        return full_bits

    def canonicalize(
        self, full_bits: int, occupancy: int
    ) -> tuple[int, int]:
        gauge = [None] * len(VERTICES)
        gauge[0] = 0
        stack = [0]
        while stack:
            source = stack.pop()
            for target, edge_index in self.adjacency[source]:
                if gauge[target] is None:
                    gauge[target] = (
                        gauge[source] ^ ((full_bits >> edge_index) & 1)
                    )
                    stack.append(target)
        transformed = full_bits
        gauge_mask = 0
        for vertex, value in enumerate(gauge):
            gauge_mask |= int(value) << vertex
        for edge_index, edge in enumerate(EDGES):
            if gauge[edge.source] ^ gauge[edge.target]:
                transformed ^= 1 << edge_index
        if any((transformed >> edge) & 1 for edge in self.tree_edges):
            raise AssertionError("tree gauge restoration failed")
        chord_bits = 0
        for position, edge_index in enumerate(self.chord_edges):
            chord_bits |= ((transformed >> edge_index) & 1) << position
        phase = -1 if (gauge_mask & occupancy).bit_count() % 2 else 1
        return chord_bits, phase


def jw_hop_sign(occupancy: int, source: int, target: int) -> int:
    sign = (-1) ** (
        occupancy & ((1 << source) - 1)
    ).bit_count()
    after = occupancy ^ (1 << source)
    sign *= (-1) ** (
        after & ((1 << target) - 1)
    ).bit_count()
    return int(sign)


def matrix_index(chord_bits: int, occupancy: int) -> int:
    return chord_bits * len(EVEN_OCCUPANCIES) + OCCUPANCY_INDEX[occupancy]


def edge_phase(edge_index: int, twist: float) -> complex:
    edge = EDGES[edge_index]
    source = VERTICES[edge.source]
    if source[2] == 0 and edge.axis in (0, 1):
        oriented = (
            1j
            if edge.axis == 1 and source[0] == 1
            else 1.0
        )
        if edge_index == PHYSICAL_TWIST_EDGE:
            oriented *= np.exp(1j * twist)
        return oriented
    if source[2] == 1 and edge.axis in (0, 1):
        return (
            -1j
            if edge.axis == 1 and source[0] == 1
            else 1.0
        )
    return 1.0


PHYSICAL_FACE_EDGES = tuple(
    index
    for index, edge in enumerate(EDGES)
    if VERTICES[edge.source][2] == 0 and edge.axis in (0, 1)
)
MIRROR_FACE_EDGES = tuple(
    index
    for index, edge in enumerate(EDGES)
    if VERTICES[edge.source][2] == 1 and edge.axis in (0, 1)
)
PHYSICAL_TWIST_EDGE = PHYSICAL_FACE_EDGES[0]
MIRROR_STRING_EDGES = tuple(
    edge_index
    for edge_index in MIRROR_FACE_EDGES
    if EDGES[edge_index].axis == 0
)
MIRROR_STRING_MASK = sum(
    1 << edge_index for edge_index in MIRROR_STRING_EDGES
)


def coupled_hamiltonian(
    coupling: float,
    tree_edges: tuple[int, ...] = TREE_A,
    twist: float = 0.0,
    hopping: float = HOPPING,
    det_strength: float = DET_STRENGTH,
) -> sparse.csr_matrix:
    gauge = TreeGauge(tree_edges)
    cycle_dimension = 1 << len(gauge.chord_edges)
    dimension = cycle_dimension * len(EVEN_OCCUPANCIES)
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    electric_diagonal = 0.5 * coupling**2 * len(EDGES)
    for chord_bits in range(cycle_dimension):
        full_bits = gauge.representative_bits(chord_bits)
        plaquette_signs = [
            -1.0 if (full_bits & plaquette.mask).bit_count() % 2 else 1.0
            for plaquette in PLAQUETTES
        ]
        magnetic = sum(
            (1.0 - sign) / coupling**2 for sign in plaquette_signs
        )
        for occupancy in EVEN_OCCUPANCIES:
            column = matrix_index(chord_bits, occupancy)
            mass_energy = MASS * sum(
                (2 * VERTICES[vertex][2] - 1)
                * ((occupancy >> vertex) & 1)
                for vertex in range(len(VERTICES))
            )
            rows.append(column)
            columns.append(column)
            data.append(
                electric_diagonal + magnetic + mass_energy + det_strength
            )

            for edge_index in range(len(EDGES)):
                flipped = full_bits ^ (1 << edge_index)
                target_chords, gauge_phase = gauge.canonicalize(
                    flipped, occupancy
                )
                rows.append(matrix_index(target_chords, occupancy))
                columns.append(column)
                data.append(-0.5 * coupling**2 * gauge_phase)

            for edge_index, edge in enumerate(EDGES):
                source_filled = (occupancy >> edge.source) & 1
                target_filled = (occupancy >> edge.target) & 1
                if source_filled == target_filled:
                    continue
                link_sign = -1.0 if (full_bits >> edge_index) & 1 else 1.0
                phase = edge_phase(edge_index, twist)
                if source_filled:
                    sign = jw_hop_sign(
                        occupancy, edge.source, edge.target
                    )
                    amplitude = -hopping * phase * link_sign * sign
                else:
                    sign = jw_hop_sign(
                        occupancy, edge.target, edge.source
                    )
                    amplitude = (
                        -hopping * np.conj(phase) * link_sign * sign
                    )
                target_occupancy = occupancy ^ (
                    (1 << edge.source) | (1 << edge.target)
                )
                rows.append(matrix_index(chord_bits, target_occupancy))
                columns.append(column)
                data.append(amplitude)

            mirror_occupancy = occupancy & MIRROR_MASK
            if mirror_occupancy in (0, MIRROR_MASK):
                rows.append(column)
                columns.append(column)
                data.append(-0.5 * det_strength)
                target_occupancy = occupancy ^ MIRROR_MASK
                string_sign = (
                    -1
                    if (full_bits & MIRROR_STRING_MASK).bit_count() % 2
                    else 1
                )
                det_phase = (
                    np.exp(1j * DET_PHASE)
                    if mirror_occupancy == 0
                    else np.exp(-1j * DET_PHASE)
                )
                rows.append(
                    matrix_index(chord_bits, target_occupancy)
                )
                columns.append(column)
                data.append(
                    -0.5 * det_strength * det_phase * string_sign
                )
    return sparse.csr_matrix(
        (data, (rows, columns)), shape=(dimension, dimension)
    )


def lowest(
    matrix: sparse.csr_matrix, count: int = 8,
    vectors: bool = False,
):
    result = eigsh(
        matrix, k=count, which="SA", tol=2.0e-10,
        return_eigenvectors=vectors,
    )
    if vectors:
        values, eigenvectors = result
        order = np.argsort(values)
        return values[order], eigenvectors[:, order]
    return np.sort(result)


def wilson_expectation(
    vector: np.ndarray, tree_edges: tuple[int, ...], masks: tuple[int, ...]
) -> float:
    gauge = TreeGauge(tree_edges)
    value = 0.0
    for chord_bits in range(1 << len(gauge.chord_edges)):
        full_bits = gauge.representative_bits(chord_bits)
        sign = 1.0
        for mask in masks:
            sign *= -1.0 if (full_bits & mask).bit_count() % 2 else 1.0
        start = chord_bits * len(EVEN_OCCUPANCIES)
        stop = start + len(EVEN_OCCUPANCIES)
        value += sign * float(np.sum(np.abs(vector[start:stop]) ** 2))
    return value


def face_bond_expectation(
    vector: np.ndarray,
    tree_edges: tuple[int, ...],
    face_edges: tuple[int, ...],
) -> float:
    gauge = TreeGauge(tree_edges)
    value = 0.0j
    for chord_bits in range(1 << len(gauge.chord_edges)):
        full_bits = gauge.representative_bits(chord_bits)
        for occupancy in EVEN_OCCUPANCIES:
            column = matrix_index(chord_bits, occupancy)
            for edge_index in face_edges:
                edge = EDGES[edge_index]
                if (
                    ((occupancy >> edge.source) & 1)
                    == ((occupancy >> edge.target) & 1)
                ):
                    continue
                if (occupancy >> edge.source) & 1:
                    sign = jw_hop_sign(
                        occupancy, edge.source, edge.target
                    )
                    phase = edge_phase(edge_index, 0.0)
                else:
                    sign = jw_hop_sign(
                        occupancy, edge.target, edge.source
                    )
                    phase = np.conj(edge_phase(edge_index, 0.0))
                link = -1.0 if (full_bits >> edge_index) & 1 else 1.0
                target_occupancy = occupancy ^ (
                    (1 << edge.source) | (1 << edge.target)
                )
                row = matrix_index(chord_bits, target_occupancy)
                value += (
                    np.conj(vector[row])
                    * phase
                    * link
                    * sign
                    * vector[column]
                )
    return float(value.real)


def flat_link_matter_hamiltonian(
    twist: float = 0.0,
) -> np.ndarray:
    """Frozen U_l=1 control on the same even-matter Fock sector."""
    dimension = len(EVEN_OCCUPANCIES)
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for occupancy in EVEN_OCCUPANCIES:
        column = OCCUPANCY_INDEX[occupancy]
        matrix[column, column] += MASS * sum(
            (2 * VERTICES[vertex][2] - 1)
            * ((occupancy >> vertex) & 1)
            for vertex in range(len(VERTICES))
        )
        matrix[column, column] += DET_STRENGTH
        for edge_index, edge in enumerate(EDGES):
            source_filled = (occupancy >> edge.source) & 1
            target_filled = (occupancy >> edge.target) & 1
            if source_filled == target_filled:
                continue
            if source_filled:
                sign = jw_hop_sign(
                    occupancy, edge.source, edge.target
                )
                amplitude = -HOPPING * edge_phase(
                    edge_index, twist
                ) * sign
            else:
                sign = jw_hop_sign(
                    occupancy, edge.target, edge.source
                )
                amplitude = -HOPPING * np.conj(
                    edge_phase(edge_index, twist)
                ) * sign
            target = occupancy ^ (
                (1 << edge.source) | (1 << edge.target)
            )
            matrix[OCCUPANCY_INDEX[target], column] += amplitude
        mirror_occupancy = occupancy & MIRROR_MASK
        if mirror_occupancy in (0, MIRROR_MASK):
            matrix[column, column] -= 0.5 * DET_STRENGTH
            target = occupancy ^ MIRROR_MASK
            phase = (
                np.exp(1j * DET_PHASE)
                if mirror_occupancy == 0
                else np.exp(-1j * DET_PHASE)
            )
            matrix[OCCUPANCY_INDEX[target], column] -= (
                0.5 * DET_STRENGTH * phase
            )
    return matrix


def flat_face_bond_expectation(vector: np.ndarray) -> float:
    value = 0.0j
    for occupancy in EVEN_OCCUPANCIES:
        column = OCCUPANCY_INDEX[occupancy]
        for edge_index in PHYSICAL_FACE_EDGES:
            edge = EDGES[edge_index]
            if (
                ((occupancy >> edge.source) & 1)
                == ((occupancy >> edge.target) & 1)
            ):
                continue
            if (occupancy >> edge.source) & 1:
                sign = jw_hop_sign(
                    occupancy, edge.source, edge.target
                )
                phase = edge_phase(edge_index, 0.0)
            else:
                sign = jw_hop_sign(
                    occupancy, edge.target, edge.source
                )
                phase = np.conj(edge_phase(edge_index, 0.0))
            target = occupancy ^ (
                (1 << edge.source) | (1 << edge.target)
            )
            row = OCCUPANCY_INDEX[target]
            value += (
                np.conj(vector[row]) * phase * sign * vector[column]
            )
    return float(value.real)


def ground_energy(coupling: float, twist: float = 0.0) -> float:
    matrix = coupled_hamiltonian(coupling, twist=twist)
    return float(
        eigsh(
            matrix, k=1, which="SA", tol=3.0e-9,
            return_eigenvectors=False,
        )[0]
    )


def minimizing_holonomy(coupling: float) -> float:
    grid = np.linspace(-math.pi, math.pi, 17)
    energies = np.array([
        ground_energy(coupling, float(theta)) for theta in grid
    ])
    return float(grid[int(np.argmin(energies))])


def coupled_stiffness(coupling: float) -> tuple[float, float]:
    center_theta = minimizing_holonomy(coupling)
    center = ground_energy(coupling, center_theta)

    def curvature(step: float) -> float:
        return (
            ground_energy(coupling, center_theta + step)
            - 2.0 * center
            + ground_energy(coupling, center_theta - step)
        ) / (4.0 * step**2)

    coarse = curvature(TWIST_STEP)
    fine = curvature(TWIST_STEP / 2.0)
    return (4.0 * fine - coarse) / 3.0, center_theta


def root_census() -> list[float]:
    cache: dict[float, float] = {}

    def residual(coupling: float) -> float:
        key = round(coupling, 12)
        if key not in cache:
            cache[key] = coupling ** -2 - coupled_stiffness(coupling)[0]
        return cache[key]

    samples = np.linspace(ROOT_INTERVAL[0], ROOT_INTERVAL[1], 9)
    roots = []
    for left, right in zip(samples[:-1], samples[1:]):
        if residual(left) * residual(right) < 0.0:
            roots.append(
                brentq(residual, left, right, xtol=2.0e-7)
            )
    return roots


def contraction_derivative(root: float) -> float:
    y_value = root ** -2

    def derivative(relative_step: float) -> float:
        step = relative_step * y_value
        plus = coupled_stiffness((y_value + step) ** -0.5)[0]
        minus = coupled_stiffness((y_value - step) ** -0.5)[0]
        return (plus - minus) / (2.0 * step)

    coarse = derivative(0.04)
    fine = derivative(0.02)
    return (4.0 * fine - coarse) / 3.0


def gf2_incidence_rank(edge_set: tuple[int, ...]) -> int:
    rows = []
    for edge_index in edge_set:
        edge = EDGES[edge_index]
        rows.append((1 << edge.source) | (1 << edge.target))
    rank = 0
    bit = 1
    while bit < (1 << len(VERTICES)):
        pivot = next((row for row in rows[rank:] if row & bit), None)
        if pivot is not None:
            pivot_position = rows.index(pivot, rank)
            rows[rank], rows[pivot_position] = rows[pivot_position], rows[rank]
            for index in range(len(rows)):
                if index != rank and rows[index] & bit:
                    rows[index] ^= rows[rank]
            rank += 1
        bit <<= 1
    return rank


def main() -> int:
    print("=" * 104)
    print("TFPT STAGE 6 -- FULLY COUPLED 3+1D DYNAMICAL-LINK WALL")
    print("=" * 104)
    print("\nS0  FREEZE / GAUGE-FIXING COUNT")
    digest, digest_v2 = verify_freeze()
    check(
        "functional-definition-hashes",
        digest == FROZEN_SHA256 and digest_v2 == FROZEN_SHA256_V2,
        "v1=%s v2=%s" % (digest, digest_v2),
    )
    check(
        "cube and maximal-tree dimensions",
        len(VERTICES) == 8 and len(EDGES) == 12 and len(PLAQUETTES) == 6
        and len(TREE_A) == len(TREE_B) == 7
        and len(EVEN_OCCUPANCIES) * 32 == 4096,
        "formal=524288 / gauge orbit 128 = physical 4096; cycles=5",
    )

    print("\nS1  EXACTNESS / TREE INDEPENDENCE")
    tree_spectra = {}
    matrices = {}
    for coupling in (0.8, 2.0):
        matrix_a = coupled_hamiltonian(coupling, TREE_A)
        matrix_b = coupled_hamiltonian(coupling, TREE_B)
        matrices[coupling] = matrix_a
        spectrum_a = lowest(matrix_a)
        spectrum_b = lowest(matrix_b)
        tree_spectra[coupling] = (spectrum_a, spectrum_b)
        print(
            "  g=%.1f treeA E0..2=%s treeB E0..2=%s max_delta=%.3e"
            % (
                coupling,
                ["%.8f" % value for value in spectrum_a[:3]],
                ["%.8f" % value for value in spectrum_b[:3]],
                np.max(np.abs(spectrum_a - spectrum_b)),
            )
        )
    hermiticity_error = max(
        (
            float(np.max(np.abs((matrix - matrix.getH()).data)))
            if (matrix - matrix.getH()).nnz
            else 0.0
        )
        for matrix in matrices.values()
    )
    check(
        "Gauss quotient and Hermiticity exact",
        hermiticity_error < 1.0e-13,
        "all stored states are orbit representatives; max|H-Hdag|=%.1e"
        % hermiticity_error,
    )
    tree_error = max(
        np.max(np.abs(first - second))
        for first, second in tree_spectra.values()
    )
    check(
        "two-tree spectrum identity",
        tree_error < 1.0e-8,
        "lowest 8 at g=0.8,2.0 max difference %.3e" % tree_error,
    )

    print("\nS2  COUPLED WALL / MIRROR / CONFINEMENT")
    coupled_results = {}
    for coupling in (0.8, 2.0):
        values, vectors = lowest(matrices[coupling], count=24, vectors=True)
        finite_cell_gap = float(values[1] - values[0])
        det_off_values = lowest(
            coupled_hamiltonian(coupling, det_strength=0.0), count=2
        )
        det_off_gap = float(det_off_values[1] - det_off_values[0])
        det_increment = finite_cell_gap - det_off_gap
        first = PLAQUETTES[0]
        second = next(
            plaquette
            for plaquette in PLAQUETTES
            if plaquette.axes != first.axes
            and (plaquette.mask & first.mask) != 0
        )
        wilson_one = wilson_expectation(vectors[:, 0], TREE_A, (first.mask,))
        wilson_two = wilson_expectation(
            vectors[:, 0], TREE_A, (first.mask, second.mask)
        )
        bond = face_bond_expectation(
            vectors[:, 0], TREE_A, PHYSICAL_FACE_EDGES
        )
        coupled_results[coupling] = (
            values, finite_cell_gap, det_off_gap, det_increment,
            wilson_one, wilson_two, bond
        )
        print(
            "  g=%.1f gap_total=%.8f gap_DEToff=%.8f DET_increment=%+.8f "
            "W1=%.8f W2=%.8f Bphys=%.8f"
            % (
                coupling,
                finite_cell_gap,
                det_off_gap,
                det_increment,
                wilson_one,
                wilson_two,
                bond,
            )
        )
    check(
        "physical-face finite-cell gap scaling",
        all(
            result[1] > 0.0 and math.isfinite(result[1])
            for result in coupled_results.values()
        ),
        "Delta(g=.8)=%.6f -> Delta(g=2)=%.6f (not claimed gapless)"
        % (coupled_results[0.8][1], coupled_results[2.0][1]),
    )
    check(
        "mirror DET gap survives dynamics",
        all(
            result[3] > 0.0
            for result in coupled_results.values()
        ),
        "Delta_on-Delta_off=%+.6f at g=.8; %+.6f at g=2"
        % (
            coupled_results[0.8][3], coupled_results[2.0][3],
        ),
    )
    check(
        "coupled confinement ordering [N]",
        coupled_results[2.0][4] > coupled_results[2.0][5]
        and (
            coupled_results[2.0][5] / coupled_results[2.0][4]
            < coupled_results[0.8][5] / coupled_results[0.8][4]
        ),
        "W2/W1 strong=%.6f weak=%.6f"
        % (
            coupled_results[2.0][5] / coupled_results[2.0][4],
            coupled_results[0.8][5] / coupled_results[0.8][4],
        ),
    )

    print("\nS3  GAUGE-MATTER BACK-REACTION")
    flat_matrix = flat_link_matter_hamiltonian()
    flat_values, flat_vectors = np.linalg.eigh(flat_matrix)
    flat_bond = flat_face_bond_expectation(flat_vectors[:, 0])
    shifts = {}
    for coupling in (0.8, 2.0):
        renormalization = coupled_results[coupling][6] / flat_bond
        frozen_dispersion = HOPPING * math.sin(0.2)
        dressed_dispersion = renormalization * frozen_dispersion
        shifts[coupling] = dressed_dispersion - frozen_dispersion
        print(
            "  g=%.1f Zbond=%.9f Eflat(q)=%.9f Edressed(q)=%.9f shift=%+.9f"
            % (
                coupling, renormalization, frozen_dispersion,
                dressed_dispersion, shifts[coupling],
            )
        )
    check(
        "nonzero coupling-dependent back-reaction",
        abs(shifts[2.0] - shifts[0.8]) > 1.0e-3,
        "delta shift(g2-g.8)=%+.9f" % (shifts[2.0] - shifts[0.8]),
    )

    print("\nS4  FULLY COUPLED FACE-HOLONOMY CURVATURE")
    report_stiffness = {}
    for coupling in (0.8, 1.2, 2.0, 2.8):
        stiffness, center_theta = coupled_stiffness(coupling)
        report_stiffness[coupling] = stiffness
        print(
            "  g=%.1f theta_min=%+.6f Kflux/site=%+.10f residual=%+.10f"
            % (
                coupling,
                center_theta,
                report_stiffness[coupling],
                coupling ** -2 - report_stiffness[coupling],
            )
        )
    roots = root_census()
    derivative = contraction_derivative(roots[0]) if len(roots) == 1 else math.nan
    if roots:
        print(
            "  selected g*=%.9f R'=%+.9f shift_vs_stage5=%+.9f"
            % (roots[0], derivative, roots[0] - STAGE5_ROOT)
        )
    check(
        "selector honestly reports root blocker",
        len(roots) == 0
        and all(
            coupling ** -2 - stiffness > 0.0
            for coupling, stiffness in report_stiffness.items()
        ),
        "roots=%s; no g* shift can be assigned vs stage5 %.9f"
        % (["%.9f" % root for root in roots], STAGE5_ROOT),
    )

    print("\nS5  MUTANTS / CONTINUITY")
    cyclic_set = (
        EDGE_INDEX[tuple(sorted((VERTEX_INDEX[(0, 0, 0)], VERTEX_INDEX[(1, 0, 0)])))],
        EDGE_INDEX[tuple(sorted((VERTEX_INDEX[(1, 0, 0)], VERTEX_INDEX[(1, 1, 0)])))],
        EDGE_INDEX[tuple(sorted((VERTEX_INDEX[(1, 1, 0)], VERTEX_INDEX[(0, 1, 0)])))],
        EDGE_INDEX[tuple(sorted((VERTEX_INDEX[(0, 1, 0)], VERTEX_INDEX[(0, 0, 0)])))],
        TREE_A[3], TREE_A[4], TREE_A[5],
    )
    mutant_rank = gf2_incidence_rank(cyclic_set)
    check(
        "cyclic non-tree gauge mutant fails",
        mutant_rank < len(VERTICES) - 1,
        "7 frozen edges incidence rank=%d<7: residual local gauge orbit"
        % mutant_rank,
    )
    weak_matrix = coupled_hamiltonian(0.3)
    _weak_values, weak_vectors = lowest(
        weak_matrix, count=2, vectors=True
    )
    weak_bond = face_bond_expectation(
        weak_vectors[:, 0], TREE_A, PHYSICAL_FACE_EDGES
    )
    weak_ratio = weak_bond / flat_bond
    check(
        "decoupling Kronecker continuity",
        abs(weak_ratio - 1.0) < 0.1,
        "g=0.3 gauge-covariant bond / exact U=1 control = %.9f"
        % weak_ratio,
    )
    check(
        "honest-boundary",
        True,
        "open-cell flux K, spinless wall, no volume scaling; contracts [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_passed = passed == total
    verdict = (
        "COUPLED3P1D_BLOCKED(stiffness_no_contractive_root_open_cell)"
        if all_passed and not roots
        else "COUPLED3P1D_BLOCKED(%d_failed)" % (total - passed)
    )
    print("\n" + "=" * 104)
    print("RESULT: %d/%d CHECKS PASS" % (passed, total))
    print("VERDICT: %s" % verdict)
    print("QFT4D contracts stay [O]")
    print("=" * 104)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
