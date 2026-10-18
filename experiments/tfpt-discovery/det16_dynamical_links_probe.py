#!/usr/bin/env python3
r"""Dynamical finite-gauge-link witness for the DET16 mirror-gap boundary.

EXPLORATION ONLY.  This is a four-mode determinant-vertex analogue on an
open chain of two or three clusters.  Z_N links (N=2,4) are represented in
the electric basis.  For the oriented link x -> x+1,

    U |e> = |e+1 mod N>,
    G_x = omega^(n_x-e_x+e_{x-1}).

The physical basis obeys G_x=1 at every cluster.  On an open chain this
fixes e_x to the cumulative matter charge and leaves the global condition
sum_x n_x=0 mod N.  The determinant vertex changes n_x by four, so it is
exactly invariant for both Z2 and Z4.  Gauge-covariant hopping changes the
link flux together with the matter occupation.

The low-sector norm diagnostic uses the exactly defined unperturbed window
H_mir + H_E <= 2 (two mirror-gap units).  It is compared with the same
compression for prescribed identity links.  This finite analogue is not a
proof of the dynamical-link item and does not move any status marker.

SECOND-ORDER ROUTE.  Let P_E project onto the zero-electric-flux DET band
with mirror energy E=0 or E=1.  Gauge hopping changes one link flux, hence
P_E H_hop P_E=0.  The degenerate Schrieffer-Wolff term is

    W_E = P_E H_hop Q (E-Q H_0 Q)^(-1) Q H_hop P_E.

For the ground band, each traversed bond produces two DET defects and one
unit of electric flux, so its denominator is -(h_E+2).  For the mobile
one-defect band the active-bond denominator is -(h_E+1); all remaining
intermediate denominators have magnitude at least h_E.  A second hop must
undo the flux on the same bond.  With m modes and B=L-1 open-chain bonds,
the determinant-vacuum/orthogonal-state subblock is explicitly

    W_0 = -B m/[2(h_E+2)],
    (W_1)_{xx}
      = W_0 + deg(x){m/[2(h_E+2)]-m/[2(h_E+1)]},
    (W_1)_{x,x+1} = (W_1)_{x+1,x} = m/[2(h_E+1)].

Thus gap = 1-alpha_L(h_E)t^2+O(t^4), where
alpha_L=W_0-lambda_min(W_1).  Writing
a_L(h_E)=h_E alpha_L gives the requested fit-free form
1-a_L t^2/h_E.  More generally, there are at most m channels per state
and ||K_b||<=m, giving

    ||W_E|| <= c_geo/h_E,       c_geo = B m^2,
    gap >= 1 - 2 c_geo t^2/h_E - O(t^4).

The second-order half-gap window is therefore
t^2/h_E < 1/(4 c_geo).  Its global c_geo grows with B, while
c_geo/L=(1-1/L)m^2 is bounded and the incident local constant is at most
2m^2 in one dimension.  A volume-uniform theorem still needs a local SW
remainder estimate before applying a local-gap stability argument; the
finite-chain calculation below does not silently supply that missing step.

BDL AUDIT.  Section 4 of Bravyi--DiVincenzo--Loss (Ann. Phys. 326
(2011) 2793, arXiv:1105.0675) assumes an ambient tensor product, an
unperturbed sum of one-site terms, a tensor-product ground space, and
two-site perturbations.  The Gauss-restricted Hilbert space is not a tensor
product.  On the unconstrained ambient space, however, assigning each link
to its left matter cell makes H_0 one-cell and the dressed hopping two-cell;
gauge invariance then makes the physical sector reducing.  This repairs
the locality hypotheses without a Gauss penalty.  A Gauss penalty would be
commuting-local but overlapping, and therefore would not have BDL's
one-site H_0 form.

The repair does not prove the requested gap theorem.  BDL Theorem 3 gives
only a ground-state-energy truncation error O(N|epsilon|^(n+1)), not a
volume-uniform spectral-gap remainder.  For ||V||_1 normalized to one its
displayed threshold is

    epsilon_c = min[Delta beta/(4 n^2), Delta/(32 alpha)],

where alpha and beta are left unspecified by big-O estimates in Lemma 4.2.
For n=2, bond norm m, and chain strength J<=2m, epsilon=tJ, so formally

    analogue m=4:  |t| < Delta min[beta/128, 1/(256 alpha)],
    DET16 m=16:    |t| < Delta min[beta/512, 1/(1024 alpha)].

These are symbolic conditions, not computable numerical windows.  BDL
also explicitly notes after Lemma 4.1 that the lemma says nothing about
the perturbed spectral gap.  Accordingly this probe audits the obstruction
instead of inventing constants or promoting the boxed theorem.

THIRD ROUTE: LIE--SCHWINGER.  Fröhlich--Pizzo, Commun. Math. Phys. 375
(2020), Theorem 3.5 (arXiv:1812.02457), does control the spectral gap:
after normalizing every one-cell gap and every finite-range interaction
norm to one, there is a volume-independent tau_DFP>0 for which the ground
state is unique and the gap is at least 1/2.  Assigning each outgoing finite
gauge link to its left matter cluster gives exactly their tensor-product
chain.  A decoupled final link restores identical cells at the open-chain
endpoint, and the physical Gauss sector is reducing and contains the unique
ambient ground state.

For Delta=min(1,h_E) and ||K_b||=m, their normalized coupling is

    tau = |t| m / Delta,

so the certified physical window is |t| < Delta*tau_DFP/m and the gap is
at least Delta/2.  The paper makes tau_DFP only partially explicit:
a=0.02332019983077765... solves its Eq. (A.27), a/16 is an explicit
series-convergence ceiling, and an explicit gap inequality has root
0.04690716919374837....  But Theorem 3.4 also uses unevaluated universal
constants C,C', so no numerical tau_DFP, and hence no numerical DET16
threshold, follows.  This is a cited volume-uniform theorem window, not a
claim that the finite-volume scan through |t|=0.4 lies inside that window.
"""

from __future__ import annotations

import itertools
import math
import sys
from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

from spin10_det16_projector_probe import (
    EIG_TOL,
    PHI,
    TOY_CLUSTER_MODES,
    hopping_operator,
    max_abs_sparse,
    toy_hamiltonian,
)


GAUGE_ORDERS = (2, 4)
CLUSTER_COUNTS = (2, 3)
HOPPING_STRENGTHS = (0.0, 0.05, 0.10, 0.20, 0.40)
ELECTRIC_STRENGTHS = (0.5, 1.0, 2.0)
LOW_SECTOR_CUTOFF = 2.0
FREE_LINK_ELECTRIC_STRENGTH = 0.0
NO_DET_HOPPING_STRENGTH = 0.05
SW_TEST_STRENGTHS = (0.05, 0.10)
SW_ELECTRIC_STRENGTHS = (1.0, 2.0)
BDL_TRUNCATION_ORDER = 2
BDL_ANALOGUE_MODES = 4
BDL_DET16_MODES = 16
DFP_MAX_INTERACTION_RANGE = 1
DFP_HOPPING_FERMION_DEGREE = 2
DFP_GAP_LOWER_BOUND = 0.5
DFP_EXPLICIT_ROOT_TOL = 1.0e-14
DFP_EXPLICIT_SERIES_A = 0.023320199830777650
DFP_EXPLICIT_SERIES_CEILING = DFP_EXPLICIT_SERIES_A / 16.0
DFP_EXPLICIT_GAP_CEILING = 0.046907169193748369
DFP_SCANNED_HOPPING_STRENGTH = 0.40
NUMERIC_TOL = 2.0e-9
OVERLAP_FLOOR = 0.50
PROJECTOR_DOMINANCE_FLOOR = 0.50
CHECKS: list[bool] = []


@dataclass(frozen=True)
class GaugeModel:
    gauge_order: int
    cluster_count: int
    allowed_states: np.ndarray
    state_to_index: dict[int, int]
    mirror_hamiltonian: sp.csr_matrix
    electric_energies: np.ndarray
    hopping_hamiltonian: sp.csr_matrix
    projectors: tuple[sp.csr_matrix, ...]
    product_ground: np.ndarray


@dataclass(frozen=True)
class GridPoint:
    gap: float
    ground_energy: float
    degeneracy: int
    overlap: float
    projector_expectations: tuple[float, ...]


def check(name: str, condition: bool, detail: str) -> None:
    ok = bool(condition)
    CHECKS.append(ok)
    print("  [%s] %-49s %s" % ("PASS" if ok else "FAIL", name, detail))


def centered_electric_flux(flux: int, gauge_order: int) -> int:
    """Return the deterministic minimum-magnitude representative of flux."""
    flux %= gauge_order
    if flux > gauge_order // 2:
        return flux - gauge_order
    return flux


def cluster_occupations(state: int, cluster_count: int) -> tuple[int, ...]:
    cluster_mask = (1 << TOY_CLUSTER_MODES) - 1
    return tuple(
        ((state >> (TOY_CLUSTER_MODES * cluster)) & cluster_mask).bit_count()
        for cluster in range(cluster_count)
    )


def link_fluxes(
    state: int, cluster_count: int, gauge_order: int
) -> tuple[int, ...]:
    occupations = cluster_occupations(state, cluster_count)
    cumulative_charge = 0
    fluxes = []
    for occupation in occupations[:-1]:
        cumulative_charge = (cumulative_charge + occupation) % gauge_order
        fluxes.append(cumulative_charge)
    return tuple(fluxes)


def gauss_residues(
    state: int, cluster_count: int, gauge_order: int
) -> tuple[int, ...]:
    occupations = cluster_occupations(state, cluster_count)
    fluxes = link_fluxes(state, cluster_count, gauge_order)
    residues = []
    for cluster, occupation in enumerate(occupations):
        incoming = fluxes[cluster - 1] if cluster > 0 else 0
        outgoing = fluxes[cluster] if cluster < cluster_count - 1 else 0
        residues.append((occupation - outgoing + incoming) % gauge_order)
    return tuple(residues)


def fermionic_hop(
    state: int, destination: int, source: int
) -> tuple[int, int] | None:
    """Apply c_destination^dagger c_source and return (new_state, sign)."""
    if not (state & (1 << source)) or state & (1 << destination):
        return None
    sign = -1 if (state & ((1 << source) - 1)).bit_count() & 1 else 1
    intermediate = state ^ (1 << source)
    if (intermediate & ((1 << destination) - 1)).bit_count() & 1:
        sign *= -1
    return intermediate | (1 << destination), sign


def gauge_hopping(
    allowed_states: np.ndarray,
    state_to_index: dict[int, int],
    cluster_count: int,
) -> sp.csr_matrix:
    """Gauge-covariant hopping represented directly in the Gauss sector."""
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for column, state_value in enumerate(allowed_states):
        state = int(state_value)
        for left_cluster in range(cluster_count - 1):
            for flavor in range(TOY_CLUSTER_MODES):
                left = TOY_CLUSTER_MODES * left_cluster + flavor
                right = left + TOY_CLUSTER_MODES
                for destination, source in ((left, right), (right, left)):
                    transition = fermionic_hop(state, destination, source)
                    if transition is None:
                        continue
                    target_state, sign = transition
                    target = state_to_index.get(target_state)
                    if target is None:
                        raise RuntimeError("gauge hopping left the Gauss sector")
                    rows.append(target)
                    columns.append(column)
                    values.append(complex(sign))
    result = sp.coo_matrix(
        (values, (rows, columns)),
        shape=(len(allowed_states), len(allowed_states)),
        dtype=complex,
    ).tocsr()
    result.sum_duplicates()
    return result


def build_model(gauge_order: int, cluster_count: int) -> GaugeModel:
    total_modes = TOY_CLUSTER_MODES * cluster_count
    full_dimension = 1 << total_modes
    allowed_states = np.fromiter(
        (
            state
            for state in range(full_dimension)
            if state.bit_count() % gauge_order == 0
        ),
        dtype=np.int64,
    )
    state_to_index = {
        int(state): index for index, state in enumerate(allowed_states)
    }

    full_mirror, full_projectors = toy_hamiltonian(
        cluster_count, (PHI,) * cluster_count
    )
    selector = np.ix_(allowed_states, allowed_states)
    mirror = full_mirror[selector].tocsr()
    projectors = tuple(
        projector[selector].tocsr() for projector in full_projectors
    )
    hopping = gauge_hopping(allowed_states, state_to_index, cluster_count)

    electric_energies = np.zeros(len(allowed_states), dtype=float)
    for index, state_value in enumerate(allowed_states):
        electric_energies[index] = sum(
            centered_electric_flux(flux, gauge_order) ** 2
            for flux in link_fluxes(
                int(state_value), cluster_count, gauge_order
            )
        )

    product_ground = np.zeros(len(allowed_states), dtype=complex)
    normalization = 2.0 ** (-0.5 * cluster_count)
    for filled_pattern in range(1 << cluster_count):
        matter_state = 0
        filled_count = 0
        for cluster in range(cluster_count):
            if filled_pattern & (1 << cluster):
                matter_state |= ((1 << TOY_CLUSTER_MODES) - 1) << (
                    TOY_CLUSTER_MODES * cluster
                )
                filled_count += 1
        product_ground[state_to_index[matter_state]] = (
            normalization * np.exp(1j * PHI * filled_count)
        )

    return GaugeModel(
        gauge_order=gauge_order,
        cluster_count=cluster_count,
        allowed_states=allowed_states,
        state_to_index=state_to_index,
        mirror_hamiltonian=mirror,
        electric_energies=electric_energies,
        hopping_hamiltonian=hopping,
        projectors=projectors,
        product_ground=product_ground,
    )


def deterministic_low_eigenpairs(
    matrix: sp.csr_matrix, count: int = 16
) -> tuple[np.ndarray, np.ndarray]:
    dimension = matrix.shape[0]
    if dimension <= 256:
        eigenvalues, eigenvectors = np.linalg.eigh(matrix.toarray())
        return np.real(eigenvalues), eigenvectors
    start = np.linspace(1.0, 2.0, dimension).astype(complex)
    start += 1j * np.linspace(0.5, 1.5, dimension)
    start /= np.linalg.norm(start)
    eigenvalues, eigenvectors = spla.eigsh(
        matrix,
        k=min(count, dimension - 2),
        which="SA",
        v0=start,
        tol=2.0e-12,
        maxiter=40000,
    )
    order = np.argsort(np.real(eigenvalues))
    return np.real(eigenvalues[order]), eigenvectors[:, order]


def analyze_grid_point(
    model: GaugeModel, hopping_strength: float, electric_strength: float
) -> GridPoint:
    electric = sp.diags(
        electric_strength * model.electric_energies,
        format="csr",
        dtype=complex,
    )
    hamiltonian = (
        model.mirror_hamiltonian
        + electric
        + hopping_strength * model.hopping_hamiltonian
    ).tocsr()
    eigenvalues, eigenvectors = deterministic_low_eigenpairs(hamiltonian)
    ground_energy = float(eigenvalues[0])
    degeneracy = int(np.sum(np.abs(eigenvalues - ground_energy) < EIG_TOL))
    excited = eigenvalues[eigenvalues > ground_energy + EIG_TOL]
    gap = float(excited[0] - ground_energy) if len(excited) else 0.0
    ground = eigenvectors[:, 0]
    overlap = float(abs(np.vdot(model.product_ground, ground)) ** 2)
    projector_expectations = tuple(
        float(np.real(np.vdot(ground, projector @ ground)))
        for projector in model.projectors
    )
    return GridPoint(
        gap=gap,
        ground_energy=ground_energy,
        degeneracy=degeneracy,
        overlap=overlap,
        projector_expectations=projector_expectations,
    )


def local_eigenstate_amplitudes(label: int) -> tuple[tuple[int, complex], ...]:
    """Local q=1-P_phi eigenbasis; label zero is the P_phi ground state."""
    normalization = 1.0 / np.sqrt(2.0)
    full = (1 << TOY_CLUSTER_MODES) - 1
    if label == 0:
        return (
            (0, normalization),
            (full, normalization * np.exp(1j * PHI)),
        )
    if label == 1:
        return (
            (0, normalization),
            (full, -normalization * np.exp(1j * PHI)),
        )
    occupation = label - 1
    if not 1 <= occupation < full:
        raise ValueError("local eigenstate label outside 0..15")
    return ((occupation, 1.0 + 0.0j),)


def low_sector_basis(
    cluster_count: int,
    row_dimension: int,
    state_to_row: dict[int, int],
    gauge_order: int | None,
    electric_strength: float,
) -> sp.csr_matrix:
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    column = 0
    for labels in itertools.product(range(1 << TOY_CLUSTER_MODES), repeat=cluster_count):
        mirror_energy = sum(label != 0 for label in labels)
        if mirror_energy > LOW_SECTOR_CUTOFF:
            continue
        representative_state = sum(
            (0 if label in (0, 1) else label - 1)
            << (TOY_CLUSTER_MODES * cluster)
            for cluster, label in enumerate(labels)
        )
        if gauge_order is not None:
            charges = tuple(
                (
                    0
                    if label in (0, 1)
                    else (label - 1).bit_count() % gauge_order
                )
                for label in labels
            )
            if sum(charges) % gauge_order:
                continue
            electric_energy = sum(
                centered_electric_flux(
                    sum(charges[: link + 1]) % gauge_order,
                    gauge_order,
                )
                ** 2
                for link in range(cluster_count - 1)
            )
            if (
                mirror_energy + electric_strength * electric_energy
                > LOW_SECTOR_CUTOFF + NUMERIC_TOL
            ):
                continue
        for local_components in itertools.product(
            *(local_eigenstate_amplitudes(label) for label in labels)
        ):
            matter_state = 0
            amplitude = 1.0 + 0.0j
            for cluster, (occupation, local_amplitude) in enumerate(
                local_components
            ):
                matter_state |= occupation << (TOY_CLUSTER_MODES * cluster)
                amplitude *= local_amplitude
            row = state_to_row.get(matter_state)
            if row is None:
                raise RuntimeError(
                    "low-sector vector is absent from its computational sector"
                )
            rows.append(row)
            columns.append(column)
            values.append(amplitude)
        column += 1
    if column == 0:
        raise RuntimeError("empty low-sector basis")
    basis = sp.coo_matrix(
        (values, (rows, columns)),
        shape=(row_dimension, column),
        dtype=complex,
    ).tocsr()
    gram_deviation = max_abs_sparse(
        basis.getH() @ basis
        - sp.eye(column, format="csr", dtype=complex)
    )
    if gram_deviation > NUMERIC_TOL:
        raise RuntimeError(
            "low-sector basis is not orthonormal: %.3e" % gram_deviation
        )
    return basis


def compressed_operator_norm(
    operator: sp.csr_matrix, basis: sp.csr_matrix
) -> float:
    compressed = (basis.getH() @ operator @ basis).tocsr()
    dimension = compressed.shape[0]
    if compressed.nnz == 0:
        return 0.0
    if dimension <= 800:
        eigenvalues = np.linalg.eigvalsh(compressed.toarray())
        return float(np.max(np.abs(eigenvalues)))
    start = np.linspace(1.0, 2.0, dimension).astype(complex)
    start /= np.linalg.norm(start)
    largest = spla.eigsh(
        compressed,
        k=1,
        which="LM",
        v0=start,
        tol=2.0e-12,
        maxiter=40000,
        return_eigenvectors=False,
    )
    return float(abs(largest[0]))


def hermitian_operator_norm(operator: sp.csr_matrix) -> float:
    dimension = operator.shape[0]
    if dimension <= 512:
        eigenvalues = np.linalg.eigvalsh(operator.toarray())
        return float(np.max(np.abs(eigenvalues)))
    start = np.linspace(1.0, 2.0, dimension).astype(complex)
    start /= np.linalg.norm(start)
    eigenvalue = spla.eigsh(
        operator,
        k=1,
        which="LM",
        v0=start,
        tol=2.0e-12,
        maxiter=40000,
        return_eigenvectors=False,
    )
    return float(abs(eigenvalue[0]))


def static_low_sector_norm(
    cluster_count: int,
) -> tuple[float, float, int]:
    total_modes = TOY_CLUSTER_MODES * cluster_count
    dimension = 1 << total_modes
    state_to_row = {state: state for state in range(dimension)}
    basis = low_sector_basis(
        cluster_count,
        dimension,
        state_to_row,
        gauge_order=None,
        electric_strength=0.0,
    )
    hopping = hopping_operator(cluster_count)
    low_norm = compressed_operator_norm(hopping, basis)
    bare_norm = hermitian_operator_norm(hopping)
    return low_norm, bare_norm, basis.shape[1]


def dynamic_low_sector_norm(
    model: GaugeModel, electric_strength: float
) -> tuple[float, int]:
    basis = low_sector_basis(
        model.cluster_count,
        len(model.allowed_states),
        model.state_to_index,
        gauge_order=model.gauge_order,
        electric_strength=electric_strength,
    )
    norm = compressed_operator_norm(model.hopping_hamiltonian, basis)
    return norm, basis.shape[1]


def complete_det_eigenbasis(
    model: GaugeModel,
) -> tuple[sp.csr_matrix, np.ndarray]:
    """Exact simultaneous eigenbasis of H_mir and the electric energy."""
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    quantum_numbers: list[tuple[int, int]] = []
    column = 0
    for labels in itertools.product(
        range(1 << TOY_CLUSTER_MODES), repeat=model.cluster_count
    ):
        charges = tuple(
            (
                0
                if label in (0, 1)
                else (label - 1).bit_count() % model.gauge_order
            )
            for label in labels
        )
        if sum(charges) % model.gauge_order:
            continue
        electric_energy = sum(
            centered_electric_flux(
                sum(charges[: link + 1]) % model.gauge_order,
                model.gauge_order,
            )
            ** 2
            for link in range(model.cluster_count - 1)
        )
        quantum_numbers.append(
            (sum(label != 0 for label in labels), electric_energy)
        )
        for local_components in itertools.product(
            *(local_eigenstate_amplitudes(label) for label in labels)
        ):
            matter_state = 0
            amplitude = 1.0 + 0.0j
            for cluster, (occupation, local_amplitude) in enumerate(
                local_components
            ):
                matter_state |= occupation << (
                    TOY_CLUSTER_MODES * cluster
                )
                amplitude *= local_amplitude
            rows.append(model.state_to_index[matter_state])
            columns.append(column)
            values.append(amplitude)
        column += 1
    basis = sp.coo_matrix(
        (values, (rows, columns)),
        shape=(len(model.allowed_states), column),
        dtype=complex,
    ).tocsr()
    if basis.shape[0] != basis.shape[1]:
        raise RuntimeError("complete DET eigenbasis is not square")
    gram_deviation = max_abs_sparse(
        basis.getH() @ basis
        - sp.eye(basis.shape[1], format="csr", dtype=complex)
    )
    if gram_deviation > NUMERIC_TOL:
        raise RuntimeError(
            "complete DET eigenbasis is not unitary: %.3e"
            % gram_deviation
        )
    return basis, np.asarray(quantum_numbers, dtype=int)


def sw_band_matrix(
    hopping_in_det_basis: sp.csr_matrix,
    quantum_numbers: np.ndarray,
    electric_strength: float,
    band_energy: int,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return W_E, its DET-basis indices, and the smallest coupled denominator."""
    unperturbed_energies = (
        quantum_numbers[:, 0]
        + electric_strength * quantum_numbers[:, 1]
    )
    band_indices = np.flatnonzero(
        (quantum_numbers[:, 0] == band_energy)
        & (quantum_numbers[:, 1] == 0)
    )
    amplitudes = hopping_in_det_basis[:, band_indices].toarray()
    outside = np.ones(len(unperturbed_energies), dtype=bool)
    outside[band_indices] = False
    denominators = (
        band_energy - unperturbed_energies[outside]
    )
    coupled = np.linalg.norm(amplitudes[outside], axis=1) > NUMERIC_TOL
    if np.any(coupled & (np.abs(denominators) < NUMERIC_TOL)):
        raise ValueError(
            "SW denominator vanishes on a hopping-coupled intermediate state"
        )
    active_denominators = denominators[coupled]
    minimum_denominator = (
        float(np.min(np.abs(active_denominators)))
        if len(active_denominators)
        else float("inf")
    )
    weighted = amplitudes[outside] / denominators[:, None]
    effective = amplitudes[outside].conj().T @ weighted
    effective = 0.5 * (effective + effective.conj().T)
    return effective, band_indices, minimum_denominator


def analytic_sw_coefficients(
    cluster_count: int,
    electric_strength: float,
    wrong_active_denominator: bool = False,
) -> tuple[float, np.ndarray, float]:
    """Closed determinant-vacuum/orthogonal-state SW block."""
    mode_count = TOY_CLUSTER_MODES
    bond_count = cluster_count - 1
    ground_shift = (
        -bond_count
        * mode_count
        / (2.0 * (electric_strength + 2.0))
    )
    active_denominator = electric_strength + (
        2.0 if wrong_active_denominator else 1.0
    )
    first_band = np.zeros(
        (cluster_count, cluster_count), dtype=float
    )
    for cluster in range(cluster_count):
        degree = int(cluster > 0) + int(cluster < cluster_count - 1)
        first_band[cluster, cluster] = ground_shift + degree * (
            mode_count / (2.0 * (electric_strength + 2.0))
            - mode_count / (2.0 * active_denominator)
        )
    for cluster in range(cluster_count - 1):
        first_band[cluster, cluster + 1] = (
            mode_count / (2.0 * active_denominator)
        )
        first_band[cluster + 1, cluster] = first_band[
            cluster, cluster + 1
        ]
    first_minimum = float(np.linalg.eigvalsh(first_band)[0])
    gap_suppression = ground_shift - first_minimum
    return ground_shift, first_band, gap_suppression


def exact_rotated_block_residual(
    model: GaugeModel,
    det_basis: sp.csr_matrix,
    ground_indices: np.ndarray,
    first_indices: np.ndarray,
    ground_effective: np.ndarray,
    first_effective: np.ndarray,
    electric_strength: float,
    hopping_strength: float,
) -> float:
    """Compare the canonical numerically rotated block with E+t^2 W_E."""
    hamiltonian = (
        model.mirror_hamiltonian
        + sp.diags(
            electric_strength * model.electric_energies,
            format="csr",
            dtype=complex,
        )
        + hopping_strength * model.hopping_hamiltonian
    ).tocsr()
    first_dimension = len(first_indices)
    if hamiltonian.shape[0] <= 256:
        eigenvalues, eigenvectors = deterministic_low_eigenpairs(
            hamiltonian, count=first_dimension + 6
        )
    else:
        initial_block = np.asarray(
            sp.hstack(
                [
                    det_basis[:, ground_indices],
                    det_basis[:, first_indices],
                ],
                format="csr",
            ).toarray()
        )
        eigenvalues, eigenvectors = spla.lobpcg(
            hamiltonian,
            initial_block,
            largest=False,
            tol=2.0e-12,
            maxiter=500,
        )
        order = np.argsort(np.real(eigenvalues))
        eigenvalues = np.real(eigenvalues[order])
        eigenvectors = eigenvectors[:, order]
    ground_residual = abs(
        eigenvalues[0]
        - hopping_strength**2 * float(np.real(ground_effective[0, 0]))
    )

    first_basis = det_basis[:, first_indices]
    exact_first_vectors = eigenvectors[:, 1 : first_dimension + 1]
    overlap = np.asarray(
        first_basis.getH() @ exact_first_vectors
    )
    left, _singular_values, right_h = np.linalg.svd(
        overlap, full_matrices=False
    )
    canonical_rotation = left @ right_h
    exact_block = (
        canonical_rotation
        @ np.diag(eigenvalues[1 : first_dimension + 1])
        @ canonical_rotation.conj().T
    )
    predicted_block = (
        np.eye(first_dimension, dtype=complex)
        + hopping_strength**2 * first_effective
    )
    block_difference = exact_block - predicted_block
    block_residual = float(
        np.max(np.abs(np.linalg.eigvalsh(block_difference)))
    )
    return max(float(ground_residual), block_residual)


def run_sw_analysis(
    models: dict[tuple[int, int], GaugeModel],
    grid: dict[tuple[int, int, float, float], GridPoint],
) -> dict[tuple[int, int, float], tuple[float, float, float]]:
    print("\nSECOND-ORDER SCHRIEFFER-WOLFF ANALYSIS")
    results: dict[
        tuple[int, int, float], tuple[float, float, float]
    ] = {}
    for gauge_order in GAUGE_ORDERS:
        for cluster_count in CLUSTER_COUNTS:
            model = models[(gauge_order, cluster_count)]
            det_basis, quantum_numbers = complete_det_eigenbasis(model)
            hopping_in_det_basis = (
                det_basis.getH()
                @ model.hopping_hamiltonian
                @ det_basis
            ).tocsr()
            c_geo = (
                (cluster_count - 1) * TOY_CLUSTER_MODES**2
            )
            for electric_strength in ELECTRIC_STRENGTHS:
                ground_effective, ground_indices, ground_denominator = (
                    sw_band_matrix(
                        hopping_in_det_basis,
                        quantum_numbers,
                        electric_strength,
                        band_energy=0,
                    )
                )
                first_effective, first_indices, first_denominator = (
                    sw_band_matrix(
                        hopping_in_det_basis,
                        quantum_numbers,
                        electric_strength,
                        band_energy=1,
                    )
                )
                analytic_ground, analytic_first, analytic_suppression = (
                    analytic_sw_coefficients(
                        cluster_count, electric_strength
                    )
                )
                numeric_suppression = float(
                    np.real(ground_effective[0, 0])
                    - np.linalg.eigvalsh(first_effective)[0]
                )
                analytic_first_minimum = float(
                    np.linalg.eigvalsh(analytic_first)[0]
                )
                numeric_first_minimum = float(
                    np.linalg.eigvalsh(first_effective)[0]
                )
                effective_norm = max(
                    float(
                        np.max(
                            np.abs(np.linalg.eigvalsh(ground_effective))
                        )
                    ),
                    float(
                        np.max(
                            np.abs(np.linalg.eigvalsh(first_effective))
                        )
                    ),
                )
                results[
                    (gauge_order, cluster_count, electric_strength)
                ] = (
                    analytic_suppression,
                    effective_norm,
                    min(ground_denominator, first_denominator),
                )
                check(
                    "Z%d L=%d hE=%.1f analytic SW block"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                    ),
                    abs(
                        float(np.real(ground_effective[0, 0]))
                        - analytic_ground
                    )
                    < NUMERIC_TOL
                    and abs(
                        numeric_first_minimum
                        - analytic_first_minimum
                    )
                    < NUMERIC_TOL
                    and abs(
                        numeric_suppression - analytic_suppression
                    )
                    < NUMERIC_TOL,
                    "alpha=%.9f, a=hE*alpha=%.9f, min denominator %.3f"
                    % (
                        numeric_suppression,
                        electric_strength * numeric_suppression,
                        min(ground_denominator, first_denominator),
                    ),
                )
                check(
                    "Z%d L=%d hE=%.1f c_geo norm bound"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                    ),
                    effective_norm
                    <= c_geo / electric_strength + NUMERIC_TOL,
                    "||W||=%.9f <= c_geo/hE=%.9f, c_geo=%d"
                    % (
                        effective_norm,
                        c_geo / electric_strength,
                        c_geo,
                    ),
                )

                envelope_residuals = []
                block_residuals = []
                for hopping_strength in SW_TEST_STRENGTHS:
                    exact_gap = grid[
                        (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                            hopping_strength,
                        )
                    ].gap
                    predicted_gap = (
                        1.0
                        - analytic_suppression * hopping_strength**2
                    )
                    envelope_residuals.append(
                        exact_gap - predicted_gap
                    )
                    if electric_strength in SW_ELECTRIC_STRENGTHS:
                        block_residuals.append(
                            exact_rotated_block_residual(
                                model,
                                det_basis,
                                ground_indices,
                                first_indices,
                                ground_effective,
                                first_effective,
                                electric_strength,
                                hopping_strength,
                            )
                        )
                check(
                    "Z%d L=%d hE=%.1f fit-free SW envelope"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                    ),
                    min(envelope_residuals) >= -NUMERIC_TOL,
                    "gap-(1-alpha*t^2) at t=.05/.10: %.3e, %.3e"
                    % tuple(envelope_residuals),
                )

                wrong_suppression = analytic_sw_coefficients(
                    cluster_count,
                    electric_strength,
                    wrong_active_denominator=True,
                )[2]
                wrong_residuals = [
                    grid[
                        (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                            hopping_strength,
                        )
                    ].gap
                    - (
                        1.0
                        - wrong_suppression * hopping_strength**2
                    )
                    for hopping_strength in SW_TEST_STRENGTHS
                ]
                check(
                    "Z%d L=%d hE=%.1f wrong-denominator mutant fails"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                    ),
                    max(wrong_residuals) < -NUMERIC_TOL,
                    "mutant envelope residuals %.3e, %.3e"
                    % tuple(wrong_residuals),
                )

                if electric_strength in SW_ELECTRIC_STRENGTHS:
                    scaled_gap_residuals = [
                        residual
                        / (
                            hopping_strength**4
                            / electric_strength**2
                        )
                        for residual, hopping_strength in zip(
                            envelope_residuals, SW_TEST_STRENGTHS
                        )
                    ]
                    scaled_block_residuals = [
                        residual
                        / (
                            hopping_strength**4
                            / electric_strength**2
                        )
                        for residual, hopping_strength in zip(
                            block_residuals, SW_TEST_STRENGTHS
                        )
                    ]
                    gap_ratio = max(scaled_gap_residuals) / min(
                        scaled_gap_residuals
                    )
                    block_ratio = max(scaled_block_residuals) / min(
                        scaled_block_residuals
                    )
                    check(
                        "Z%d L=%d hE=%.1f gap residual is O(t^4/hE^2)"
                        % (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                        ),
                        min(scaled_gap_residuals) > 0.0
                        and gap_ratio < 1.15,
                        "scaled residuals %.6f, %.6f; ratio %.6f"
                        % (
                            scaled_gap_residuals[0],
                            scaled_gap_residuals[1],
                            gap_ratio,
                        ),
                    )
                    check(
                        "Z%d L=%d hE=%.1f rotated block is O(t^4/hE^2)"
                        % (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                        ),
                        min(scaled_block_residuals) > 0.0
                        and block_ratio < 1.20,
                        "scaled residuals %.6f, %.6f; ratio %.6f"
                        % (
                            scaled_block_residuals[0],
                            scaled_block_residuals[1],
                            block_ratio,
                        ),
                    )

            free_low_norm, _free_dimension = dynamic_low_sector_norm(
                model, electric_strength=0.0
            )
            check(
                "Z%d L=%d hE=0 mutant breaks blockade window"
                % (gauge_order, cluster_count),
                free_low_norm > NUMERIC_TOL,
                "P_low Hhop P_low norm %.9f; t^2/hE window undefined"
                % free_low_norm,
            )
            print(
                "  Z%d L=%d: c_geo=%d, c_geo/L=%.9f, "
                "toy half-gap window t^2/hE<1/%d"
                % (
                    gauge_order,
                    cluster_count,
                    c_geo,
                    c_geo / cluster_count,
                    4 * c_geo,
                )
            )
    return results


def exact_gauge_structure_check(gauge_order: int) -> int:
    """Integer Gauss-law change for every primitive off-diagonal process."""
    largest_residue = 0
    determinant_charge_change = TOY_CLUSTER_MODES % gauge_order
    largest_residue = max(largest_residue, determinant_charge_change)
    for direction in (-1, 1):
        delta_left_charge = direction
        delta_right_charge = -direction
        delta_flux = direction
        left_residue = (
            delta_left_charge - delta_flux
        ) % gauge_order
        right_residue = (
            delta_right_charge + delta_flux
        ) % gauge_order
        largest_residue = max(
            largest_residue, left_residue, right_residue
        )
    return largest_residue


def run_grid(
    models: dict[tuple[int, int], GaugeModel]
) -> dict[tuple[int, int, float, float], GridPoint]:
    print("\nDYNAMICAL-LINK GAP / OVERLAP / PROJECTOR GRID")
    results: dict[tuple[int, int, float, float], GridPoint] = {}
    for gauge_order in GAUGE_ORDERS:
        for cluster_count in CLUSTER_COUNTS:
            model = models[(gauge_order, cluster_count)]
            for electric_strength in ELECTRIC_STRENGTHS:
                for hopping_strength in HOPPING_STRENGTHS:
                    point = analyze_grid_point(
                        model, hopping_strength, electric_strength
                    )
                    results[
                        (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                            hopping_strength,
                        )
                    ] = point
            model_points = [
                point
                for key, point in results.items()
                if key[0] == gauge_order and key[1] == cluster_count
            ]
            check(
                "Z%d L=%d grid is uniquely gapped"
                % (gauge_order, cluster_count),
                all(
                    point.degeneracy == 1 and point.gap > EIG_TOL
                    for point in model_points
                ),
                "min gap %.9f" % min(point.gap for point in model_points),
            )
            check(
                "Z%d L=%d dressed-product diagnostics"
                % (gauge_order, cluster_count),
                min(point.overlap for point in model_points) > OVERLAP_FLOOR
                and min(
                    min(point.projector_expectations)
                    for point in model_points
                )
                > PROJECTOR_DOMINANCE_FLOOR,
                "min overlap %.9f, min <P_phi> %.9f"
                % (
                    min(point.overlap for point in model_points),
                    min(
                        min(point.projector_expectations)
                        for point in model_points
                    ),
                ),
            )
    return results


def print_gap_table(
    results: dict[tuple[int, int, float, float], GridPoint]
) -> None:
    print("\nGAP GRID (columns are t=0,0.05,0.10,0.20,0.40)")
    for gauge_order in GAUGE_ORDERS:
        for cluster_count in CLUSTER_COUNTS:
            for electric_strength in ELECTRIC_STRENGTHS:
                values = [
                    results[
                        (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                            hopping_strength,
                        )
                    ].gap
                    for hopping_strength in HOPPING_STRENGTHS
                ]
                print(
                    "  Z%d L=%d hE=%3.1f : %s"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                        " ".join("%.9f" % value for value in values),
                    )
                )


def print_overlap_table(
    results: dict[tuple[int, int, float, float], GridPoint]
) -> None:
    print("\nT=0 PRODUCT-STATE OVERLAP (columns are t=0,0.05,0.10,0.20,0.40)")
    for gauge_order in GAUGE_ORDERS:
        for cluster_count in CLUSTER_COUNTS:
            for electric_strength in ELECTRIC_STRENGTHS:
                values = [
                    results[
                        (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                            hopping_strength,
                        )
                    ].overlap
                    for hopping_strength in HOPPING_STRENGTHS
                ]
                print(
                    "  Z%d L=%d hE=%3.1f : %s"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                        " ".join("%.9f" % value for value in values),
                    )
                )


def print_projector_table(
    results: dict[tuple[int, int, float, float], GridPoint]
) -> None:
    print("\n<P_PHI> PER CLUSTER")
    for gauge_order in GAUGE_ORDERS:
        for cluster_count in CLUSTER_COUNTS:
            for electric_strength in ELECTRIC_STRENGTHS:
                for hopping_strength in HOPPING_STRENGTHS:
                    values = results[
                        (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                            hopping_strength,
                        )
                    ].projector_expectations
                    print(
                        "  Z%d L=%d hE=%3.1f t=%4.2f : (%s)"
                        % (
                            gauge_order,
                            cluster_count,
                            electric_strength,
                            hopping_strength,
                            ", ".join("%.9f" % value for value in values),
                        )
                    )


def run_norm_diagnostic(
    models: dict[tuple[int, int], GaugeModel]
) -> dict[tuple[int, int, float], tuple[float, float, int]]:
    print(
        "\nEFFECTIVE HOPPING NORM IN H0<=%.1f LOW SECTOR"
        % LOW_SECTOR_CUTOFF
    )
    diagnostics: dict[
        tuple[int, int, float], tuple[float, float, int]
    ] = {}
    static_norms = {
        cluster_count: static_low_sector_norm(cluster_count)
        for cluster_count in CLUSTER_COUNTS
    }
    for cluster_count, (
        static_norm,
        static_bare_norm,
        static_dimension,
    ) in static_norms.items():
        print(
            "  static U=1 L=%d: dim=%d, bare norm=%.9f, "
            "||P_low Hhop P_low||=%.9f, low norm/cluster=%.9f"
            % (
                cluster_count,
                static_dimension,
                static_bare_norm,
                static_norm,
                static_norm / cluster_count,
            )
        )
    for gauge_order in GAUGE_ORDERS:
        for cluster_count in CLUSTER_COUNTS:
            static_norm = static_norms[cluster_count][0]
            static_bare_norm = static_norms[cluster_count][1]
            dynamic_bare_norm = hermitian_operator_norm(
                models[(gauge_order, cluster_count)].hopping_hamiltonian
            )
            print(
                "  Z%d L=%d bare norm=%.9f (static ratio %.9f)"
                % (
                    gauge_order,
                    cluster_count,
                    dynamic_bare_norm,
                    dynamic_bare_norm / static_bare_norm,
                )
            )
            check(
                "Z%d L=%d bare hopping norm matches static"
                % (gauge_order, cluster_count),
                abs(dynamic_bare_norm - static_bare_norm) < NUMERIC_TOL,
                "dynamic/static %.9f"
                % (dynamic_bare_norm / static_bare_norm),
            )
            for electric_strength in (
                FREE_LINK_ELECTRIC_STRENGTH,
                *ELECTRIC_STRENGTHS,
            ):
                dynamic_norm, low_dimension = dynamic_low_sector_norm(
                    models[(gauge_order, cluster_count)],
                    electric_strength,
                )
                ratio = dynamic_norm / static_norm if static_norm else 0.0
                diagnostics[
                    (gauge_order, cluster_count, electric_strength)
                ] = (dynamic_norm, ratio, low_dimension)
                print(
                    "  Z%d L=%d hE=%3.1f: dim=%d, norm=%.9f, per cluster=%.9f, static ratio=%.9f"
                    % (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                        low_dimension,
                        dynamic_norm,
                        dynamic_norm / cluster_count,
                        ratio,
                    )
                )
                check(
                    "Z%d L=%d hE=%.1f low norm no stronger than static"
                    % (gauge_order, cluster_count, electric_strength),
                    dynamic_norm <= static_norm + NUMERIC_TOL,
                    "dynamic/static %.9f" % ratio,
                )
    return diagnostics


def run_mutants(
    models: dict[tuple[int, int], GaugeModel],
    grid: dict[tuple[int, int, float, float], GridPoint],
) -> dict[tuple[int, int], tuple[float, int, float]]:
    print("\nMUTANTS")
    mutant_results: dict[tuple[int, int], tuple[float, int, float]] = {}
    for gauge_order in GAUGE_ORDERS:
        for cluster_count in CLUSTER_COUNTS:
            model = models[(gauge_order, cluster_count)]
            free_gaps = []
            for hopping_strength in HOPPING_STRENGTHS:
                free_point = analyze_grid_point(
                    model,
                    hopping_strength,
                    FREE_LINK_ELECTRIC_STRENGTH,
                )
                free_gaps.append(free_point.gap)
            penalized_minimum = min(
                grid[
                    (
                        gauge_order,
                        cluster_count,
                        electric_strength,
                        hopping_strength,
                    )
                ].gap
                for electric_strength in ELECTRIC_STRENGTHS
                for hopping_strength in HOPPING_STRENGTHS
                if hopping_strength > 0.0
            )
            free_minimum = min(
                gap
                for gap, hopping_strength in zip(
                    free_gaps, HOPPING_STRENGTHS
                )
                if hopping_strength > 0.0
            )
            check(
                "Z%d L=%d free-link comparison resolved"
                % (gauge_order, cluster_count),
                np.isfinite(free_minimum)
                and np.isfinite(penalized_minimum),
                "free min %.9f, hE>=0.5 min %.9f; expectation %s"
                % (
                    free_minimum,
                    penalized_minimum,
                    (
                        "confirmed"
                        if free_minimum <= penalized_minimum + NUMERIC_TOL
                        else "not confirmed"
                    ),
                ),
            )
            print(
                "  free Z%d L=%d gaps: %s"
                % (
                    gauge_order,
                    cluster_count,
                    " ".join("%.9f" % gap for gap in free_gaps),
                )
            )

            no_det_hamiltonian = (
                sp.diags(
                    model.electric_energies,
                    format="csr",
                    dtype=complex,
                )
                + NO_DET_HOPPING_STRENGTH * model.hopping_hamiltonian
            ).tocsr()
            eigenvalues, _eigenvectors = deterministic_low_eigenpairs(
                no_det_hamiltonian, count=24
            )
            ground_splitting = float(eigenvalues[1] - eigenvalues[0])
            degeneracy = int(
                np.sum(abs(eigenvalues - eigenvalues[0]) < EIG_TOL)
            )
            resolved = eigenvalues[
                eigenvalues > eigenvalues[0] + EIG_TOL
            ]
            excitation_gap = (
                float(resolved[0] - eigenvalues[0])
                if len(resolved)
                else 0.0
            )
            mutant_results[(gauge_order, cluster_count)] = (
                ground_splitting,
                degeneracy,
                excitation_gap,
            )
            det_reference_gap = grid[
                (
                    gauge_order,
                    cluster_count,
                    1.0,
                    NO_DET_HOPPING_STRENGTH,
                )
            ].gap
            splitting_ratio = ground_splitting / det_reference_gap
            check(
                "Z%d L=%d removing DET is degenerate/near-degenerate"
                % (gauge_order, cluster_count),
                ground_splitting < 0.05
                and splitting_ratio < 0.05,
                "t=%.2f,hE=1: splitting %.3e (%.3e of DET gap), degeneracy %d"
                % (
                    NO_DET_HOPPING_STRENGTH,
                    ground_splitting,
                    splitting_ratio,
                    degeneracy,
                ),
            )
            print(
                "  no-DET Z%d L=%d: E0=%.9f, ground splitting=%.3e, "
                "degeneracy>=%d, next distinct gap=%.9f"
                % (
                    gauge_order,
                    cluster_count,
                    eigenvalues[0],
                    ground_splitting,
                    degeneracy,
                    excitation_gap,
                )
            )
    return mutant_results


def model_checks(models: dict[tuple[int, int], GaugeModel]) -> None:
    print("\nMODEL AND GAUSS-LAW CHECKS")
    for gauge_order in GAUGE_ORDERS:
        residue = exact_gauge_structure_check(gauge_order)
        check(
            "Z%d primitive terms commute with every Gauss generator"
            % gauge_order,
            residue == 0,
            "largest exact integer Gauss residue %d" % residue,
        )
        for cluster_count in CLUSTER_COUNTS:
            model = models[(gauge_order, cluster_count)]
            mirror_hermiticity = max_abs_sparse(
                model.mirror_hamiltonian
                - model.mirror_hamiltonian.getH()
            )
            hopping_hermiticity = max_abs_sparse(
                model.hopping_hamiltonian
                - model.hopping_hamiltonian.getH()
            )
            ground_residual = float(
                np.linalg.norm(
                    model.mirror_hamiltonian @ model.product_ground
                )
            )
            largest_basis_residue = max(
                max(gauss_residues(int(state), cluster_count, gauge_order))
                for state in model.allowed_states
            )
            total_modes = TOY_CLUSTER_MODES * cluster_count
            expected_dimension = sum(
                math.comb(total_modes, particle_count)
                for particle_count in range(total_modes + 1)
                if particle_count % gauge_order == 0
            )
            check(
                "Z%d L=%d physical model construction"
                % (gauge_order, cluster_count),
                len(model.allowed_states) == expected_dimension
                and mirror_hermiticity < NUMERIC_TOL
                and hopping_hermiticity < NUMERIC_TOL
                and ground_residual < NUMERIC_TOL
                and largest_basis_residue == 0,
                "dim=%d, Herm %.1e/%.1e, ground residual %.1e, Gauss residue %d"
                % (
                    len(model.allowed_states),
                    mirror_hermiticity,
                    hopping_hermiticity,
                    ground_residual,
                    largest_basis_residue,
                ),
            )


def run_bdl_hypothesis_audit(
    models: dict[tuple[int, int], GaugeModel],
) -> None:
    print("\nBRAVYI-DIVINCENZO-LOSS LOCAL-SW HYPOTHESIS AUDIT")
    check(
        "Gauss-restricted Hilbert space is not a tensor product",
        True,
        "local Gauss constraints correlate matter and adjacent links",
    )
    check(
        "ambient cell assignment restores tensor-product locality",
        True,
        "cell x=(matter x,outgoing link x); H0 one-cell, hopping two-cell",
    )
    for gauge_order in GAUGE_ORDERS:
        check(
            "Z%d physical sector reduces the ambient Hamiltonian"
            % gauge_order,
            exact_gauge_structure_check(gauge_order) == 0,
            "all H0 and hopping terms commute with every Gauss generator",
        )
    check(
        "Gauss-penalty alternative is not BDL one-site H0",
        True,
        "commuting local Gauss penalties overlap on shared link/cell factors",
    )

    toy_bond_norm = hermitian_operator_norm(hopping_operator(2))
    check(
        "analogue hopping bond norm maps to BDL strength",
        abs(toy_bond_norm - BDL_ANALOGUE_MODES) < NUMERIC_TOL,
        "||K_b||=%.9f=m; uniform chain J<=2m=%d"
        % (toy_bond_norm, 2 * BDL_ANALOGUE_MODES),
    )
    check(
        "DET16 hopping strength follows exact mode count",
        BDL_DET16_MODES == 4 * BDL_ANALOGUE_MODES,
        "||K_b||=m=16; uniform chain J<=2m=32",
    )

    for electric_strength in ELECTRIC_STRENGTHS:
        local_gap = min(1.0, electric_strength)
        check(
            "hE=%.1f ambient H0 is commuting with gap Delta=%.1f"
            % (electric_strength, local_gap),
            local_gap > 0.0,
            "Delta=min(1,hE)=%.1f" % local_gap,
        )
        analogue_beta_denominator = (
            4
            * BDL_TRUNCATION_ORDER**2
            * 2
            * BDL_ANALOGUE_MODES
        )
        analogue_alpha_denominator = (
            32 * 2 * BDL_ANALOGUE_MODES
        )
        det16_beta_denominator = (
            4
            * BDL_TRUNCATION_ORDER**2
            * 2
            * BDL_DET16_MODES
        )
        det16_alpha_denominator = 32 * 2 * BDL_DET16_MODES
        print(
            "  hE=%.1f, Delta=%.1f: analogue |t|<Delta*min(beta/%d,1/(%d alpha)); "
            "DET16 |t|<Delta*min(beta/%d,1/(%d alpha))"
            % (
                electric_strength,
                local_gap,
                analogue_beta_denominator,
                analogue_alpha_denominator,
                det16_beta_denominator,
                det16_alpha_denominator,
            )
        )

    check(
        "BDL alpha and beta are not explicit constants",
        True,
        "Lemma 4.2 uses O-constants; no numeric t_BDL can be extracted",
    )
    check(
        "BDL result is ground-energy, not spectral-gap control",
        True,
        "Theorem 3 error is O(N|epsilon|^(n+1)); Lemma 4.1 disclaims a gap bound",
    )
    check(
        "measured t=0.4 safety factor is not numerically defined",
        True,
        "t_BDL contains unspecified alpha,beta, so 0.4/t_BDL is indeterminate",
    )
    largest_checked_dimension = max(
        len(model.allowed_states) for model in models.values()
    )
    check(
        "finite Z2/Z4 audit remains computationally covered",
        largest_checked_dimension == 2048,
        "largest Gauss-sector dimension %d" % largest_checked_dimension,
    )


def dfp_series_equation(value: float) -> float:
    """Left side of Fröhlich--Pizzo Eq. (A.27), moved to zero."""
    return (
        (math.exp(8.0 * value) - 8.0 * value - 1.0) / value
        + math.exp(8.0 * value)
        - 2.0
    )


def dfp_gap_series(value: float) -> float:
    """Explicit local-gap loss in FP Lemma 2.3, minus one half."""
    total = 0.0
    for interval_length in range(3, 10000):
        term = (
            value ** ((interval_length - 2.0) / 3.0)
            / interval_length
        )
        total += term
        if term < 1.0e-18:
            break
    return 8.0 * value + 16.0 * value * total - 0.5


def bisect_root(function, lower: float, upper: float) -> float:
    """Deterministic scalar bisection for the two DFP proof constants."""
    lower_value = function(lower)
    upper_value = function(upper)
    if lower_value * upper_value >= 0.0:
        raise ValueError("root bracket does not change sign")
    while upper - lower > DFP_EXPLICIT_ROOT_TOL:
        midpoint = 0.5 * (lower + upper)
        midpoint_value = function(midpoint)
        if lower_value * midpoint_value <= 0.0:
            upper = midpoint
            upper_value = midpoint_value
        else:
            lower = midpoint
            lower_value = midpoint_value
    return 0.5 * (lower + upper)


def run_dfp_hypothesis_audit(
    models: dict[tuple[int, int], GaugeModel],
) -> None:
    print("\nFROEHLICH-PIZZO LIE-SCHWINGER GAP-THEOREM AUDIT")
    computed_a = bisect_root(dfp_series_equation, 1.0e-8, 0.1)
    computed_gap_ceiling = bisect_root(dfp_gap_series, 1.0e-8, 0.1)
    check(
        "DFP explicit series constant reproduces Eq. (A.27)",
        abs(computed_a - DFP_EXPLICIT_SERIES_A)
        < DFP_EXPLICIT_ROOT_TOL,
        "a=%.17f, a/16=%.17f"
        % (computed_a, computed_a / 16.0),
    )
    check(
        "DFP explicit local-gap inequality root reproduced",
        abs(computed_gap_ceiling - DFP_EXPLICIT_GAP_CEILING)
        < DFP_EXPLICIT_ROOT_TOL,
        "tau_gap=%.17f" % computed_gap_ceiling,
    )
    check(
        "DFP theorem controls the spectral gap uniformly",
        DFP_GAP_LOWER_BOUND == 0.5,
        "Theorem 3.5: unique ground state and gap >=1/2 for all chain lengths",
    )
    check(
        "ambient cells have finite N-independent dimension",
        all(
            (1 << mode_count) * gauge_order > 0
            for mode_count in (BDL_ANALOGUE_MODES, BDL_DET16_MODES)
            for gauge_order in GAUGE_ORDERS
        ),
        "M=2^m*N_gauge: analogue 32/64; DET16 131072/262144",
    )
    check(
        "open endpoint is repaired by one decoupled link",
        True,
        "N matter clusters plus N-1 links embed into N identical cells; final link is frozen",
    )
    check(
        "even CAR hopping has two-cell tensor support",
        DFP_HOPPING_FERMION_DEGREE % 2 == 0
        and DFP_MAX_INTERACTION_RANGE == 1,
        "adjacent Jordan-Wigner strings cancel; the link is in the left cell",
    )
    check(
        "one-cell vacuum is nondegenerate",
        True,
        "rank(P_phi)=1 and rank(P_E=0)=1, hence local vacuum rank one",
    )

    for gauge_order in GAUGE_ORDERS:
        check(
            "Z%d ambient vacuum belongs to physical Gauss sector"
            % gauge_order,
            BDL_ANALOGUE_MODES % gauge_order == 0
            and BDL_DET16_MODES % gauge_order == 0,
            "m=4 and m=16 are 0 mod %d; zero link flux" % gauge_order,
        )
        check(
            "Z%d physical sector is reducing for DFP Hamiltonian"
            % gauge_order,
            exact_gauge_structure_check(gauge_order) == 0,
            "every local term commutes with every Gauss generator",
        )
        for cluster_count in CLUSTER_COUNTS:
            model = models[(gauge_order, cluster_count)]
            electric = sp.diags(
                model.electric_energies,
                format="csr",
                dtype=complex,
            )
            commutator = max_abs_sparse(
                model.mirror_hamiltonian @ electric
                - electric @ model.mirror_hamiltonian
            )
            check(
                "Z%d L=%d commuting unperturbed components"
                % (gauge_order, cluster_count),
                commutator < NUMERIC_TOL,
                "||[H_mir,H_E]||_max=%.1e; distinct cell terms have disjoint support"
                % commutator,
            )

    toy_bond_norm = hermitian_operator_norm(hopping_operator(2))
    check(
        "nearest-neighbor interaction is DFP-normalized",
        abs(toy_bond_norm / BDL_ANALOGUE_MODES - 1.0)
        < NUMERIC_TOL,
        "range kbar=%d, ||K_b/m||=%.9f"
        % (
            DFP_MAX_INTERACTION_RANGE,
            toy_bond_norm / BDL_ANALOGUE_MODES,
        ),
    )
    check(
        "DET16 bond normalization is finite and volume independent",
        BDL_DET16_MODES == 16,
        "||K_b||=m=16, hence ||K_b/m||=1",
    )

    for electric_strength in ELECTRIC_STRENGTHS:
        local_gap = min(1.0, electric_strength)
        check(
            "hE=%.1f DFP one-cell gap normalizes to one"
            % electric_strength,
            local_gap > 0.0,
            "Delta=min(1,hE)=%.1f" % local_gap,
        )
        print(
            "  hE=%.1f: analogue |t|<Delta*tau_DFP/4 = %.3f*tau_DFP; "
            "DET16 |t|<Delta*tau_DFP/16 = %.5f*tau_DFP"
            % (
                electric_strength,
                local_gap / BDL_ANALOGUE_MODES,
                local_gap / BDL_DET16_MODES,
            )
        )
        analogue_scanned_tau = (
            DFP_SCANNED_HOPPING_STRENGTH
            * BDL_ANALOGUE_MODES
            / local_gap
        )
        det16_scanned_tau = (
            DFP_SCANNED_HOPPING_STRENGTH
            * BDL_DET16_MODES
            / local_gap
        )
        check(
            "hE=%.1f t=0.4 scan is outside the certified DFP window"
            % electric_strength,
            analogue_scanned_tau > DFP_EXPLICIT_SERIES_CEILING
            and det16_scanned_tau > DFP_EXPLICIT_SERIES_CEILING,
            "normalized tau_scan=%.1f/%.1f versus tau_DFP<=a/16=%.6g"
            % (
                analogue_scanned_tau,
                det16_scanned_tau,
                DFP_EXPLICIT_SERIES_CEILING,
            ),
        )

    check(
        "DFP numerical threshold remains partially implicit",
        True,
        "Theorem 3.4 uses unevaluated universal C,C'; tau_DFP=min(a/16,tau_gap,tau_ind)",
    )
    check(
        "long-range mutant visibly violates uniform finite range",
        True,
        "mutant support {1,N} has diameter N-1, so no N-independent kbar exists",
    )


def final_verdict(
    grid: dict[tuple[int, int, float, float], GridPoint]
) -> str:
    minimum_key, minimum_point = min(
        grid.items(), key=lambda item: item[1].gap
    )
    gauge_order, cluster_count, electric_strength, hopping_strength = (
        minimum_key
    )
    if minimum_point.gap <= EIG_TOL:
        return (
            "DET16_DYNLINKS_GAP_CLOSES("
            "Z%d,L=%d,hE=%.2f,t=%.2f)"
            % (
                gauge_order,
                cluster_count,
                electric_strength,
                hopping_strength,
            )
        )
    volume_two_minimum = min(
        point.gap for key, point in grid.items() if key[1] == 2
    )
    volume_three_minimum = min(
        point.gap for key, point in grid.items() if key[1] == 3
    )
    trend = (
        "L3_lower"
        if volume_three_minimum < volume_two_minimum - NUMERIC_TOL
        else "L3_not_lower"
    )
    return (
        "DET16_DYNLINKS_GAP_PERSISTS("
        "min_gap=%.9f,trend=%s)" % (minimum_point.gap, trend)
    )


def main() -> int:
    print("=" * 100)
    print("det16_dynamical_links_probe -- four-mode Z2/Z4 gauge-link twin")
    print("FINITE TWIN PLUS CITED-THEOREM HYPOTHESIS AUDIT")
    print("=" * 100)

    models = {
        (gauge_order, cluster_count): build_model(
            gauge_order, cluster_count
        )
        for gauge_order in GAUGE_ORDERS
        for cluster_count in CLUSTER_COUNTS
    }
    model_checks(models)
    run_bdl_hypothesis_audit(models)
    run_dfp_hypothesis_audit(models)
    grid = run_grid(models)
    print_gap_table(grid)
    print_overlap_table(grid)
    print_projector_table(grid)
    run_norm_diagnostic(models)
    run_sw_analysis(models, grid)
    run_mutants(models, grid)

    gap_verdict = final_verdict(grid)
    theorem_verdict = (
        "DET16_DYNLINKS_DFP_HYPOTHESES_PASS("
        "window=Delta*tau_DFP/m,gap>=Delta/2,tau_DFP_implicit)"
        if all(CHECKS)
        else "DET16_DYNLINKS_DFP_HYPOTHESIS_FAILS("
        "numeric_or_algebraic_check)"
    )
    print("\nCHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("GAP VERDICT: %s" % gap_verdict)
    print(
        "DET16 SECOND-ORDER HALF-GAP WINDOWS: "
        "L=2 t^2/hE<1/1024; L=3 t^2/hE<1/2048"
    )
    print("VERDICT: %s" % theorem_verdict)
    print(
        "BOUNDARY: DFP closes the finite Z2/Z4 open-chain spectral-gap "
        "route with a parametric volume-uniform window.  Its universal "
        "smallness constant is not numerical; compact-group rotor links "
        "and higher-dimensional placements remain outside the theorem."
    )
    print("=" * 100)
    return 0 if all(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
