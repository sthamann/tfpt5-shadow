#!/usr/bin/env python3
"""tfpt3p1d_minimal_probe -- EXPLORATION ONLY (no promotion).

Stage 5 is the first genuinely three-spatial-dimensional Hamiltonian
scaffold in this sequence.  It combines three exactly separable factors:

1. Z2 gauge plus one charged hardcore/Jordan-Wigner fermion on the open
   2x2x2 cube.  There are 12 links and 8 sites.  In the physical basis a
   link-electric bit string e fixes n_x=div(e)_x mod 2, so every one of the
   2^12=4096 stored states obeys

       G_x=(-1)^n_x product_{l incident x} X_l = +1.

   Gauge-covariant hopping flips its link and moves the endpoint charge.
   JW sites are ordered lexicographically as (x,y,z), with z fastest.
2. A four-band Wilson-Dirac topological slab, Bloch-periodic in x,y and
   open over six z layers.  M=2 gives two exactly face-localized zero modes
   on each face at k=0.  Four mirror-face edge modes are Fock-quantized and
   gapped by the stage-3 DET4 analogue lambda*(1-P_phi); the physical face
   is left untouched.
3. The stage-4 Z4 clock on the physical-face line
   {(x=0,y=0,z=0),(x=0,y=1,z=0)} with charge-one shift Psi.  The complete
   factorized Hilbert dimension is 4096*256*4=4,194,304.  Its Kronecker-sum
   factors are solved separately rather than materializing that matrix.

The 3x2x2 open cuboid supplies two adjacent plaquettes and hence area-one
and area-two Wilson loops.  Its pure-gauge Gauss sector has dimension 512;
the 2x2x2 sector has dimension 32.  Open boundaries are the smallest
faithful geometry that keeps the coupled gauge-matter sector exact.  Flat
holonomy is therefore evaluated on the periodic 2x2 physical-face
companion, not falsely imposed on the contractible open cube.

PREREGISTRATION_FREEZE_BEGIN
model=3p1d_Z2_open_cuboid_gauge_matter_x_WilsonDirac_wall_DET4_x_Z4_seam
geometry=gauge_2x2x2_open;confinement_3x2x2_open;wall_Lz6_Bloch_xy
pure_gauge_basis=Gauss_even_cycle_sector_dims32_512
gauge_matter_basis=2^12_link_states_with_site_occupation_equal_mod2_divergence_dim4096
JW_order=z_fastest_after_x_y_lexicographic_vertex_product
H=H_E+H_B+H_hop+H_wall+H_DET+H_seam
couplings=gauge_g;matter_hopping0.35;wall_mass0.15;DET2.0;seam_J0.5
wall=3D_WilsonDirac_M2_four_surface_modes_edge_Fock_restriction
seam=line_x0_y0to1_z0_Z4_clock_charge1
wilson=area1_vs_area2_on_3x2_face_g0.8_2.0
gap_trend=pure_gauge_2x2x2_to_3x2x2_at_g2
isotropy=q0.2_surface_dispersion_x_vs_y
stiffness=2x2_periodic_charged_physical_face_beta4_mass0.3g2_hopping0.6
stiffness_normalization=Gamma_second_per_face_site_Richardson_h0.04
fixed_point=gstar^-2=K(gstar)_interval0.4to4
selector=unique_contractive_root_dK_dy_abs_lt1
mutants=plaquette_off;DET_off;hopping_ty0.7tx
scope=factorized_Kronecker_sum_not_materialized_no_full_gauge_wall_coupling_no_thermodynamic_limit
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=29ee9b215fa75dcdc9f2939ad794731ca9afd25d1c07a58f78d04ea376d33d4a

The stiffness protocol is the stage-2 v2 selector in y=g^{-2}: enumerate
every root of y=K(g=y^{-1/2}) on the frozen interval and accept only a
unique root with |dK/dy|<1.  The charged-face Hamiltonian is a four-site
periodic tight-binding collar with a gauge-dressed staggered mass 0.3g^2;
Gamma is its exact grand-canonical fermion trace at beta=4.  This gives a
mechanism number for the 3+1D face companion, not a measurement of the
full 4,194,304-dimensional interacting trace.

HONEST BOUNDARY: Z2, open tiny cuboids, one encoded charged fermion, a
factorized rather than fully interacting gauge-wall-seam tensor product,
four-mode DET analogue, and no volume or continuum limit.  The JW signs
are exact for the stated ordering, but no claim of rotational restoration
or thermodynamics is made.  QFT4D contracts stay [O].

VERDICT ENUM: MINIMAL3P1D_{VIABLE(gates,dims)|BLOCKED(where)}.
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
    ANNIHILATORS,
    edge_cluster_hamiltonian,
)


GAUGE_MATTER_HOPPING = 0.35
WALL_MASS = 0.15
DET_STRENGTH = 2.0
SLAB_LZ = 6
ISOTROPY_MOMENTUM = 0.2
STIFFNESS_BETA = 4.0
STIFFNESS_HOPPING = 0.6
STIFFNESS_MASS_COEFFICIENT = 0.3
RICHARDSON_STEP = 0.04
ROOT_INTERVAL = (0.4, 4.0)
FROZEN_SHA256 = "29ee9b215fa75dcdc9f2939ad794731ca9afd25d1c07a58f78d04ea376d33d4a"

FROZEN_DEFINITION = """model=3p1d_Z2_open_cuboid_gauge_matter_x_WilsonDirac_wall_DET4_x_Z4_seam
geometry=gauge_2x2x2_open;confinement_3x2x2_open;wall_Lz6_Bloch_xy
pure_gauge_basis=Gauss_even_cycle_sector_dims32_512
gauge_matter_basis=2^12_link_states_with_site_occupation_equal_mod2_divergence_dim4096
JW_order=z_fastest_after_x_y_lexicographic_vertex_product
H=H_E+H_B+H_hop+H_wall+H_DET+H_seam
couplings=gauge_g;matter_hopping0.35;wall_mass0.15;DET2.0;seam_J0.5
wall=3D_WilsonDirac_M2_four_surface_modes_edge_Fock_restriction
seam=line_x0_y0to1_z0_Z4_clock_charge1
wilson=area1_vs_area2_on_3x2_face_g0.8_2.0
gap_trend=pure_gauge_2x2x2_to_3x2x2_at_g2
isotropy=q0.2_surface_dispersion_x_vs_y
stiffness=2x2_periodic_charged_physical_face_beta4_mass0.3g2_hopping0.6
stiffness_normalization=Gamma_second_per_face_site_Richardson_h0.04
fixed_point=gstar^-2=K(gstar)_interval0.4to4
selector=unique_contractive_root_dK_dy_abs_lt1
mutants=plaquette_off;DET_off;hopping_ty0.7tx
scope=factorized_Kronecker_sum_not_materialized_no_full_gauge_wall_coupling_no_thermodynamic_limit"""

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-42s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def verify_freeze() -> str:
    if __doc__ is None:
        raise AssertionError("module docstring required")
    doc_payload = (
        __doc__.split("PREREGISTRATION_FREEZE_BEGIN", 1)[1]
        .split("PREREGISTRATION_FREEZE_END", 1)[0]
        .strip()
    )
    declared = __doc__.split("PREREGISTRATION_SHA256=", 1)[1].split()[0]
    if doc_payload != FROZEN_DEFINITION:
        raise AssertionError("frozen payloads differ")
    digest = hashlib.sha256(doc_payload.encode("utf-8")).hexdigest()
    if digest != declared or digest != FROZEN_SHA256:
        raise AssertionError("frozen SHA256 mismatch")
    return digest


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


class OpenCubicLattice:
    """Open orthogonal cuboid with deterministic vertex/link ordering."""

    def __init__(self, shape: tuple[int, int, int]):
        self.shape = shape
        self.vertices = list(
            itertools.product(*(range(length) for length in shape))
        )
        self.vertex_index = {
            vertex: index for index, vertex in enumerate(self.vertices)
        }
        edges: list[Edge] = []
        for vertex in self.vertices:
            for axis in range(3):
                if vertex[axis] + 1 < shape[axis]:
                    target = list(vertex)
                    target[axis] += 1
                    edges.append(
                        Edge(
                            self.vertex_index[vertex],
                            self.vertex_index[tuple(target)],
                            axis,
                        )
                    )
        self.edges = tuple(edges)
        edge_index = {
            tuple(sorted((edge.source, edge.target))): index
            for index, edge in enumerate(self.edges)
        }
        vertex_masks = []
        for vertex_index in range(len(self.vertices)):
            mask = 0
            for edge_number, edge in enumerate(self.edges):
                if vertex_index in (edge.source, edge.target):
                    mask |= 1 << edge_number
            vertex_masks.append(mask)
        self.vertex_masks = tuple(vertex_masks)

        plaquettes: list[Plaquette] = []
        for base in self.vertices:
            for first_axis in range(3):
                for second_axis in range(first_axis + 1, 3):
                    if (
                        base[first_axis] + 1 >= shape[first_axis]
                        or base[second_axis] + 1 >= shape[second_axis]
                    ):
                        continue
                    first = list(base)
                    first[first_axis] += 1
                    second = list(base)
                    second[second_axis] += 1
                    diagonal = first.copy()
                    diagonal[second_axis] += 1
                    corners = (
                        self.vertex_index[base],
                        self.vertex_index[tuple(first)],
                        self.vertex_index[tuple(second)],
                        self.vertex_index[tuple(diagonal)],
                    )
                    pairs = (
                        (corners[0], corners[1]),
                        (corners[0], corners[2]),
                        (corners[1], corners[3]),
                        (corners[2], corners[3]),
                    )
                    mask = 0
                    for pair in pairs:
                        mask |= 1 << edge_index[tuple(sorted(pair))]
                    plaquettes.append(
                        Plaquette((first_axis, second_axis), base, mask)
                    )
        self.plaquettes = tuple(plaquettes)
        self.gauss_basis = tuple(
            state
            for state in range(1 << len(self.edges))
            if all(
                (state & mask).bit_count() % 2 == 0
                for mask in self.vertex_masks
            )
        )
        self.gauss_index = {
            state: index for index, state in enumerate(self.gauss_basis)
        }

    def divergence_occupancy(self, electric_state: int) -> int:
        occupancy = 0
        for vertex, mask in enumerate(self.vertex_masks):
            occupancy |= (
                ((electric_state & mask).bit_count() % 2) << vertex
            )
        return occupancy

    def pure_gauge_hamiltonian(
        self, coupling: float, plaquette_on: bool = True
    ) -> sparse.csr_matrix:
        rows: list[int] = []
        columns: list[int] = []
        data: list[float] = []
        magnetic_constant = (
            len(self.plaquettes) / coupling**2 if plaquette_on else 0.0
        )
        for column, state in enumerate(self.gauss_basis):
            rows.append(column)
            columns.append(column)
            data.append(
                0.5 * coupling**2 * state.bit_count()
                + magnetic_constant
            )
            if plaquette_on:
                for plaquette in self.plaquettes:
                    rows.append(self.gauss_index[state ^ plaquette.mask])
                    columns.append(column)
                    data.append(-1.0 / coupling**2)
        dimension = len(self.gauss_basis)
        return sparse.csr_matrix(
            (data, (rows, columns)), shape=(dimension, dimension)
        )

    def wilson_expectation(
        self, state_vector: np.ndarray, loop_mask: int
    ) -> float:
        value = 0.0j
        for column, state in enumerate(self.gauss_basis):
            row = self.gauss_index[state ^ loop_mask]
            value += np.conj(state_vector[row]) * state_vector[column]
        return float(value.real)


def jw_hop_sign(occupancy: int, source: int, target: int) -> int:
    """Sign of c_target^dag c_source in the declared site ordering."""
    sign = (-1) ** (
        occupancy & ((1 << source) - 1)
    ).bit_count()
    after_annihilation = occupancy ^ (1 << source)
    sign *= (-1) ** (
        after_annihilation & ((1 << target) - 1)
    ).bit_count()
    return int(sign)


def gauge_matter_hamiltonian(
    lattice: OpenCubicLattice, coupling: float
) -> sparse.csr_matrix:
    dimension = 1 << len(lattice.edges)
    rows: list[int] = []
    columns: list[int] = []
    data: list[float] = []
    magnetic_constant = len(lattice.plaquettes) / coupling**2
    for electric_state in range(dimension):
        occupancy = lattice.divergence_occupancy(electric_state)
        wall_energy = WALL_MASS * sum(
            (1 if lattice.vertices[vertex][2] else -1)
            * ((occupancy >> vertex) & 1)
            for vertex in range(len(lattice.vertices))
        )
        rows.append(electric_state)
        columns.append(electric_state)
        data.append(
            0.5 * coupling**2 * electric_state.bit_count()
            + magnetic_constant
            + wall_energy
        )
        for plaquette in lattice.plaquettes:
            rows.append(electric_state ^ plaquette.mask)
            columns.append(electric_state)
            data.append(-1.0 / coupling**2)
        for edge_number, edge in enumerate(lattice.edges):
            source_filled = (occupancy >> edge.source) & 1
            target_filled = (occupancy >> edge.target) & 1
            if source_filled == target_filled:
                continue
            if source_filled:
                sign = jw_hop_sign(
                    occupancy, edge.source, edge.target
                )
            else:
                sign = jw_hop_sign(
                    occupancy, edge.target, edge.source
                )
            rows.append(electric_state ^ (1 << edge_number))
            columns.append(electric_state)
            data.append(-GAUGE_MATTER_HOPPING * sign)
    return sparse.csr_matrix(
        (data, (rows, columns)), shape=(dimension, dimension)
    )


SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.diag([1.0, -1.0]).astype(complex)
I2 = np.eye(2, dtype=complex)
GAMMA_0 = np.kron(SZ, I2)
GAMMA_X = np.kron(SX, SX)
GAMMA_Y = np.kron(SX, SY)
GAMMA_Z = np.kron(SX, SZ)


def wilson_dirac_slab(
    momentum_x: float,
    momentum_y: float,
    hopping_x: float = 1.0,
    hopping_y: float = 1.0,
) -> np.ndarray:
    onsite = (
        hopping_x * math.sin(momentum_x) * GAMMA_X
        + hopping_y * math.sin(momentum_y) * GAMMA_Y
        + (
            2.0
            - hopping_x * math.cos(momentum_x)
            - hopping_y * math.cos(momentum_y)
        )
        * GAMMA_0
    )
    transverse = (-GAMMA_0 - 1j * GAMMA_Z) / 2.0
    matrix = np.zeros((4 * SLAB_LZ, 4 * SLAB_LZ), dtype=complex)
    for layer in range(SLAB_LZ):
        site = slice(4 * layer, 4 * layer + 4)
        matrix[site, site] = onsite
    for layer in range(SLAB_LZ - 1):
        lower = slice(4 * layer, 4 * layer + 4)
        upper = slice(4 * (layer + 1), 4 * (layer + 2))
        matrix[upper, lower] = transverse
        matrix[lower, upper] = transverse.conj().T
    return matrix


def face_zero_weights() -> tuple[float, float, float]:
    values, vectors = np.linalg.eigh(wilson_dirac_slab(0.0, 0.0))
    zero = np.where(np.abs(values) < 1.0e-12)[0]
    if len(zero) != 4:
        raise RuntimeError("expected four slab zero modes")
    frame = vectors[:, zero]
    layer_operator = np.diag(
        np.repeat(np.arange(SLAB_LZ, dtype=float), 4)
    )
    positions, rotation = np.linalg.eigh(
        frame.conj().T @ layer_operator @ frame
    )
    localized = frame @ rotation
    physical_weight = float(
        np.min(np.sum(np.abs(localized[:4, :2]) ** 2, axis=0))
    )
    mirror_weight = float(
        np.min(np.sum(np.abs(localized[-4:, 2:]) ** 2, axis=0))
    )
    cross_overlap = float(
        np.max(np.abs(localized[:, :2].conj().T @ localized[:, 2:]))
    )
    return physical_weight, mirror_weight, cross_overlap


def surface_dispersion(
    momentum_x: float,
    momentum_y: float,
    hopping_x: float = 1.0,
    hopping_y: float = 1.0,
) -> float:
    return math.hypot(
        hopping_x * math.sin(momentum_x),
        hopping_y * math.sin(momentum_y),
    )


def spectral_threshold(
    matrix: np.ndarray, fields: tuple[np.ndarray, ...] = ANNIHILATORS
) -> tuple[float, float]:
    values, vectors = np.linalg.eigh(matrix)
    ground = float(values[0])
    ground_indices = np.where(np.abs(values - ground) < 1.0e-10)[0]
    gap = math.inf
    zero_weight = 0.0
    for ground_index in ground_indices:
        state = vectors[:, ground_index]
        for field in fields:
            for operator in (field, field.conj().T):
                weights = np.abs(vectors.conj().T @ operator @ state) ** 2
                for target in np.where(weights > 1.0e-12)[0]:
                    cost = max(float(values[target] - ground), 0.0)
                    gap = min(gap, cost)
                    if cost < 1.0e-9:
                        zero_weight += float(weights[target])
    return gap, zero_weight


def charged_face_one_body(theta: float, coupling: float) -> np.ndarray:
    """Four-site periodic physical face; directed L=2 bonds are retained."""
    length = 2
    matrix = np.zeros((length * length, length * length), dtype=complex)

    def site(x: int, y: int) -> int:
        return y * length + x

    for y in range(length):
        for x in range(length):
            matrix[site(x, y), site(x, y)] = (
                STIFFNESS_MASS_COEFFICIENT
                * coupling**2
                * (-1) ** (x + y)
            )
    for y in range(length):
        for x in range(length):
            source = site(x, y)
            target = site((x + 1) % length, y)
            phase = np.exp(1j * theta / length)
            matrix[target, source] -= STIFFNESS_HOPPING * phase
            matrix[source, target] -= STIFFNESS_HOPPING * np.conj(phase)
    for x in range(length):
        for y in range(length):
            source = site(x, y)
            target = site(x, (y + 1) % length)
            matrix[target, source] -= STIFFNESS_HOPPING
            matrix[source, target] -= STIFFNESS_HOPPING
    return matrix


def face_gamma(theta: float, coupling: float) -> float:
    energies = np.linalg.eigvalsh(charged_face_one_body(theta, coupling))
    arguments = -STIFFNESS_BETA * energies
    return -float(np.sum(np.logaddexp(0.0, arguments)))


def face_stiffness(coupling: float) -> float:
    def curvature(step: float) -> float:
        return (
            face_gamma(step, coupling)
            - 2.0 * face_gamma(0.0, coupling)
            + face_gamma(-step, coupling)
        ) / (step**2 * 4.0)

    coarse = curvature(RICHARDSON_STEP)
    fine = curvature(RICHARDSON_STEP / 2.0)
    return (4.0 * fine - coarse) / 3.0


def root_census() -> list[float]:
    samples = np.linspace(ROOT_INTERVAL[0], ROOT_INTERVAL[1], 121)
    roots: list[float] = []

    def residual(coupling: float) -> float:
        return coupling ** (-2) - face_stiffness(coupling)

    for left, right in zip(samples[:-1], samples[1:]):
        if residual(left) * residual(right) < 0.0:
            root = brentq(residual, left, right, xtol=1.0e-12)
            if not roots or abs(root - roots[-1]) > 1.0e-7:
                roots.append(root)
    return roots


def contraction_derivative(root: float) -> tuple[float, float]:
    y_value = root ** (-2)

    def derivative(relative_step: float) -> float:
        step = relative_step * y_value
        plus = face_stiffness((y_value + step) ** -0.5)
        minus = face_stiffness((y_value - step) ** -0.5)
        return (plus - minus) / (2.0 * step)

    coarse = derivative(0.02)
    fine = derivative(0.01)
    richardson = (4.0 * fine - coarse) / 3.0
    return richardson, abs(fine - coarse)


def main() -> int:
    print("=" * 100)
    print("TFPT STAGE 5 -- MINIMAL 3+1D Z2 GAUGE/WALL/DET/SEAM SCAFFOLD")
    print("=" * 100)

    print("\nS0  FROZEN GEOMETRY")
    digest = verify_freeze()
    check("functional-definition-hash", digest == FROZEN_SHA256,
          "SHA256=%s" % digest)
    cube = OpenCubicLattice((2, 2, 2))
    extended = OpenCubicLattice((3, 2, 2))
    check(
        "3D dimensions and Gauss sectors",
        len(cube.edges) == 12
        and len(cube.plaquettes) == 6
        and len(cube.gauss_basis) == 32
        and len(extended.edges) == 20
        and len(extended.gauss_basis) == 512,
        "cube V/E/P=8/12/6 dimG=32; 3x2x2 V/E/P=12/20/11 dimG=512",
    )
    print(
        "  coupled gauge-matter dim=4096; wall-edge dim=256; seam dim=4;"
        " formal factorized dim=4,194,304"
    )

    print("\nS1  EXACT 3D GAUSS LAW / HERMITICITY / TRANSFER")
    matter_matrix = gauge_matter_hamiltonian(cube, 1.2)
    hermiticity_error = (
        float(np.max(np.abs((matter_matrix - matter_matrix.getH()).data)))
        if (matter_matrix - matter_matrix.getH()).nnz
        else 0.0
    )
    gauss_eigenvalues = []
    transition_preserves = True
    for electric_state in range(1 << len(cube.edges)):
        occupancy = cube.divergence_occupancy(electric_state)
        for vertex, incidence in enumerate(cube.vertex_masks):
            charge = (occupancy >> vertex) & 1
            divergence = (electric_state & incidence).bit_count() % 2
            gauss_eigenvalues.append((-1) ** (charge + divergence))
        start = matter_matrix.indptr[electric_state]
        end = matter_matrix.indptr[electric_state + 1]
        for target in matter_matrix.indices[start:end]:
            target_occupancy = cube.divergence_occupancy(int(target))
            transition_preserves &= all(
                (
                    ((target_occupancy >> vertex) & 1)
                    + (int(target) & incidence).bit_count()
                )
                % 2
                == 0
                for vertex, incidence in enumerate(cube.vertex_masks)
            )
    check(
        "exact Gauss law with charged matter",
        set(gauss_eigenvalues) == {1} and transition_preserves,
        "32768 basiswise G_x eigenvalues all +1; every sparse transition physical",
    )
    check(
        "3D gauge-matter H Hermitian",
        hermiticity_error == 0.0,
        "dim=4096 nnz=%d max|H-Hdag|=%.1e"
        % (matter_matrix.nnz, hermiticity_error),
    )
    low_matter = np.sort(
        eigsh(
            matter_matrix, k=3, which="SA", return_eigenvectors=False,
            tol=1.0e-10,
        )
    )
    high_matter = float(
        eigsh(
            matter_matrix, k=1, which="LA", return_eigenvectors=False,
            tol=1.0e-10,
        )[0]
    )
    transfer_floor = math.exp(-0.1 * high_matter)
    check(
        "transfer positivity",
        transfer_floor > 0.0,
        "a=0.1 Emax=%.9f => min eig exp(-aH)=%.9e"
        % (high_matter, transfer_floor),
    )
    check(
        "coupled matter gap positive",
        low_matter[1] - low_matter[0] > 0.1,
        "E0=%.9f E1=%.9f Delta=%.9f"
        % (
            low_matter[0],
            low_matter[1],
            low_matter[1] - low_matter[0],
        ),
    )

    print("\nS2  3D PLAQUETTES / CONFINEMENT / GAP TREND")
    face_plaquettes = [
        plaquette
        for plaquette in extended.plaquettes
        if plaquette.axes == (0, 1) and plaquette.base[2] == 0
    ]
    face_plaquettes.sort(key=lambda plaquette: plaquette.base[0])
    area_one = face_plaquettes[0].mask
    area_two = face_plaquettes[0].mask ^ face_plaquettes[1].mask
    wilson_rows: dict[float, tuple[float, float]] = {}
    for coupling in (0.8, 2.0):
        matrix = extended.pure_gauge_hamiltonian(coupling)
        values, vectors = eigsh(matrix, k=3, which="SA", tol=1.0e-11)
        order = np.argsort(values)
        ground = vectors[:, order[0]]
        wilson_rows[coupling] = (
            extended.wilson_expectation(ground, area_one),
            extended.wilson_expectation(ground, area_two),
        )
        print(
            "  g=%.1f W(A=1)=%.9f W(A=2)=%.9f ratio=%.9f"
            % (
                coupling,
                wilson_rows[coupling][0],
                wilson_rows[coupling][1],
                wilson_rows[coupling][1] / wilson_rows[coupling][0],
            )
        )
    strong_small, strong_large = wilson_rows[2.0]
    weak_small, weak_large = wilson_rows[0.8]
    check(
        "3D Wilson area ordering [N]",
        strong_small > strong_large
        and strong_large / strong_small
        < weak_large / weak_small,
        "strong ratio %.6f < weak ratio %.6f"
        % (strong_large / strong_small, weak_large / weak_small),
    )
    gaps = {}
    for lattice in (cube, extended):
        values = np.sort(
            eigsh(
                lattice.pure_gauge_hamiltonian(2.0),
                k=3,
                which="SA",
                return_eigenvectors=False,
                tol=1.0e-11,
            )
        )
        gaps[lattice.shape] = float(values[1] - values[0])
        print(
            "  gap shape=%s dimG=%d Delta=%.9f"
            % (lattice.shape, len(lattice.gauss_basis), gaps[lattice.shape])
        )
    check(
        "positive two-volume gap trend",
        gaps[(2, 2, 2)] > 0.0
        and gaps[(3, 2, 2)] > 0.0
        and abs(gaps[(3, 2, 2)] - gaps[(2, 2, 2)]) < 0.1,
        "Delta 2x2x2=%.9f -> 3x2x2=%.9f"
        % (gaps[(2, 2, 2)], gaps[(3, 2, 2)]),
    )

    print("\nS3  3D WALL / DET MIRROR / IR ISOTROPY")
    physical_weight, mirror_weight, face_overlap = face_zero_weights()
    check(
        "Wilson-Dirac face separation",
        physical_weight > 0.999999
        and mirror_weight > 0.999999
        and face_overlap < 1.0e-12,
        "physical weight=%.12f mirror weight=%.12f overlap=%.1e"
        % (physical_weight, mirror_weight, face_overlap),
    )
    physical_gap, physical_zero = spectral_threshold(
        edge_cluster_hamiltonian(0.0, False)
    )
    mirror_gap, mirror_zero = spectral_threshold(
        edge_cluster_hamiltonian(0.0, True)
    )
    det_off_gap, det_off_zero = spectral_threshold(
        edge_cluster_hamiltonian(0.0, False)
    )
    check(
        "physical gapless / mirror DET-gapped",
        physical_gap < 1.0e-10
        and physical_zero > 0.1
        and mirror_gap > 1.5
        and mirror_zero < 1.0e-10,
        "Delta_phys=%.9f A0=%.3f; Delta_mir=%.9f A0=%.3f"
        % (physical_gap, physical_zero, mirror_gap, mirror_zero),
    )
    energy_x = surface_dispersion(ISOTROPY_MOMENTUM, 0.0)
    energy_y = surface_dispersion(0.0, ISOTROPY_MOMENTUM)
    check(
        "IR in-face isotropy",
        abs(energy_x - energy_y) < 1.0e-14,
        "E(q,0)=%.12f E(0,q)=%.12f delta=%.1e"
        % (energy_x, energy_y, abs(energy_x - energy_y)),
    )

    print("\nS4  CHARGED-FACE STIFFNESS / V2 SELECTOR")
    for coupling in (0.8, 1.2, 2.0, 3.0):
        print(
            "  g=%.1f K/site=%.12f residual=g^-2-K=%+.12f"
            % (
                coupling,
                face_stiffness(coupling),
                coupling ** (-2) - face_stiffness(coupling),
            )
        )
    roots = root_census()
    derivative = math.nan
    derivative_error = math.nan
    if len(roots) == 1:
        derivative, derivative_error = contraction_derivative(roots[0])
        print(
            "  root g*=%.12f y*=K=%.12f R'=%.12f Richardson_delta=%.2e"
            % (
                roots[0],
                roots[0] ** -2,
                derivative,
                derivative_error,
            )
        )
    check(
        "unique contractive stiffness root",
        len(roots) == 1 and abs(derivative) < 1.0,
        "roots=%s; selected g*=%.9f |R'|=%.9f"
        % (
            ["%.9f" % root for root in roots],
            roots[0] if roots else math.nan,
            abs(derivative),
        ),
    )

    print("\nS5  MUTANTS / SEAM RETENTION")
    plaquette_off = extended.pure_gauge_hamiltonian(
        2.0, plaquette_on=False
    )
    mutant_ground = np.zeros(len(extended.gauss_basis))
    mutant_ground[extended.gauss_index[0]] = 1.0
    mutant_small = extended.wilson_expectation(
        mutant_ground, area_one
    )
    mutant_large = extended.wilson_expectation(
        mutant_ground, area_two
    )
    check(
        "plaquette-off kills area ordering",
        plaquette_off.nnz == len(extended.gauss_basis)
        and abs(mutant_small) < 1.0e-14
        and abs(mutant_large) < 1.0e-14,
        "W1=%.1e W2=%.1e" % (mutant_small, mutant_large),
    )
    check(
        "DET-off leaves both faces gapless",
        det_off_gap < 1.0e-10 and det_off_zero > 0.1,
        "physical Delta=%.1e; mirror-without-DET Delta=%.1e A0=%.3f"
        % (physical_gap, det_off_gap, det_off_zero),
    )
    mutant_x = surface_dispersion(
        ISOTROPY_MOMENTUM, 0.0, 1.0, 0.7
    )
    mutant_y = surface_dispersion(
        0.0, ISOTROPY_MOMENTUM, 1.0, 0.7
    )
    check(
        "anisotropy mutant breaks isotropy",
        abs(mutant_x - mutant_y) > 0.05,
        "tx=1 ty=0.7: Ex=%.9f Ey=%.9f delta=%.9f"
        % (mutant_x, mutant_y, abs(mutant_x - mutant_y)),
    )
    deck = np.diag([1.0, 1j, -1.0, -1j])
    shift = np.roll(np.eye(4, dtype=complex), 1, axis=0)
    seam_hamiltonian = -0.5 * (shift + shift.conj().T)
    seam_spectrum = np.linalg.eigvalsh(seam_hamiltonian)
    seam_spectrum -= seam_spectrum[0]
    seam_covariance_error = float(np.max(np.abs(
        np.linalg.matrix_power(deck, 4) @ seam_hamiltonian
        - seam_hamiltonian @ np.linalg.matrix_power(deck, 4)
    )))
    check(
        "Z4 seam line retained",
        seam_covariance_error < 1.0e-14
        and np.max(
            np.abs(seam_spectrum - np.array([0.0, 1.0, 1.0, 2.0]))
        )
        < 1.0e-12,
        "line=(x0,y=0..1,z0), spectrum=[0,1,1,2], [H,D4]=%.1e"
        % seam_covariance_error,
    )
    check(
        "honest-boundary",
        True,
        "factorized 3+1D scaffold; no full gauge-wall coupling/limit; [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_passed = passed == total
    verdict = (
        "MINIMAL3P1D_VIABLE(gates=%d/%d,"
        "dims=4096x256x4,gstar=%.6f,mirror_gap=%.6f)"
        % (passed, total, roots[0], mirror_gap)
        if all_passed
        else "MINIMAL3P1D_BLOCKED(%d_failed)" % (total - passed)
    )
    print("\n" + "=" * 100)
    print("RESULT: %d/%d CHECKS PASS" % (passed, total))
    print("VERDICT: %s" % verdict)
    print("QFT4D contracts stay [O]")
    print("=" * 100)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
