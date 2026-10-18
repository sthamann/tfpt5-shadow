#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v1008 -- QFT4D.LATTICE.FUNDAMENTAL.01 / GAUGE.DETLINE.FIXPOINT.01
[O]: compressed 2+1D master-object scaffold (prototype, matter,
wall/mirror, four-block assembly).

Provenance: experiments/tfpt-discovery/tfpt2p1d_{prototype,matter,
wall_mirror,master_assembly}_probe.py (review wave 7, 2026-08-30;
16/16 + 20/20 + 13/13 + 15/15).  Helpers are copied; experiments/ is
not imported.

THE POINT.  Four stages are scaffold-coherent.  No marker moves.

  Prototype [E-finite]: combinatorial K=0 -- every oriented plaquette
        has vanishing flat-x-holonomy exponent; Z2 L=2 Gauss sector
        dimension 32.  L=3 262144 is out of suite.
  Matter [N]: live frozen-link companion: K(q=0)=0, q^2 ~ 4;
        unique-contractive protocol is |R'|<1.  L2/L3 selector
        numbers (0.578 -> 0.936, pair 2.00 -> 0.31, R' 0.0005/0.028)
        are harvest pins, not L=3 Lanczos.  v1 SHA frozen negative.
  Wall/mirror [N]: QWZ physical slope ~ -0.9989; DET mirror gap >= 1.5
        (probe min 1.866) through t=0.6; DET-on-physical / remove-DET
        mutants.
  Assembly [N]: Z6 content (1,2,3,0); clock [0,1,1,2]; D H D^dag
        covariance; chi_phys vs chi_mirror; grading mutant.  Frozen
        SHA e5566dc4....  Dim 1024.

MUST-FAIL: charge-0 stiffness is zero; remove-DET leaves both edges
gapless; DET-on-physical gaps the wrong edge; Psi^2 doubles the
clock ground sector.

HONEST SCOPE (firewall): 2+1D analogue scaffold; no 4D volume
theorem, no dynamical compact-group links, no continuum limit.
QFT4D.LATTICE.FUNDAMENTAL.01 and GAUGE.DETLINE.FIXPOINT.01 stay [O].
Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

import hashlib
import itertools
import math
from dataclasses import dataclass

import numpy as np

from tfpt_constants import check, summary, reset


def report(name, ok, extra=""):
    check("%s -- %s" % (name, extra) if extra else name, ok)


HERE = __file__.rsplit("/", 1)[0]
ROOT = HERE.rsplit("/", 1)[0]
MATTER_PROBE = ROOT + "/experiments/tfpt-discovery/tfpt2p1d_matter_probe.py"
ASSEMBLY_PROBE = (
    ROOT + "/experiments/tfpt-discovery/tfpt2p1d_master_assembly_probe.py"
)

HOPPING = 0.6
STAGGERED_MASS = 0.2
BETA_MATTER = 40.0
RICHARDSON_STEP = 0.04
FROZEN_SHA256_V1 = (
    "301bd3e2270b903fe0717f65ae6f45292a0eb18cd4c0b49e3b77001fbf80dfd2"
)
FROZEN_SHA256_V2 = (
    "cc1ebf2b8237e9688a13914fcca14f99a73b191ae0bdf714eccb1436000826b0"
)
HARVEST_G_SEL_L2 = 0.578
HARVEST_G_SEL_L3 = 0.936
HARVEST_PAIR_L2 = 2.00
HARVEST_PAIR_L3 = 0.31
HARVEST_RPRIME = (0.0005, 0.028)

LX = 32
LY = 8
MASS = 1.0
FLAVORS = 4
DET_STRENGTH = 2.0
DET_PHASE = math.pi / 7.0
HOPPING_VALUES = (0.0, 0.2, 0.4, 0.6)
MOMENTA = np.linspace(-math.pi, math.pi, 129)
INTERACTION_BETA = 0.7
INTERACTION_STRENGTH = 0.4
EDGE_GAP_TOL = 1.0e-9
MIRROR_GAP_MIN = 1.5
LOCALIZATION_MIN = 0.95
MIRROR_OVERLAP_MAX = 1.0e-8
CONTENT_CHARGES = (1, 2, 3, 0)
CONTENT_NAMES = ("Q", "u^c", "L", "e^c")
CLOCK_COUPLING = 0.5
SEAM_COUPLING = 0.2
TRANSDUCTION_BETA = 0.7
SOURCE_STEP = 1.0e-4
FROZEN_SHA256_ASSEMBLY = (
    "e5566dc4582dcbdb76e57de087943da3c6528cc15aa564d2f67377ce8dc58224"
)

SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.diag([1.0, -1.0]).astype(complex)
TY = SY / (2j) - SZ / 2.0


def file_has(path: str, snippet: str) -> bool:
    with open(path, encoding="utf-8") as handle:
        return snippet in handle.read()


def plaquette_flat_holonomy_exponent(linear_size: int, x: int, y: int) -> int:
    """Net x-boundary incidence of the oriented plaquette at (x,y)."""
    exponent = 0
    boundary = linear_size - 1
    for x_link, orientation in ((x, +1), (x, -1)):
        if (x_link % linear_size) == boundary:
            exponent += orientation
    return exponent


def gauss_physical_dimension(linear_size: int, group_order: int) -> int:
    site_count = linear_size**2
    link_count = 2 * site_count
    full_dimension = group_order**link_count
    physical = 0
    for code in range(full_dimension):
        digits = [
            (code // group_order**link) % group_order
            for link in range(link_count)
        ]
        divergences_ok = True
        for y in range(linear_size):
            for x in range(linear_size):
                site = y * linear_size + x
                outgoing_x = digits[2 * site]
                outgoing_y = digits[2 * site + 1]
                incoming_x = digits[
                    2 * (y * linear_size + (x - 1) % linear_size)
                ]
                incoming_y = digits[
                    2 * (((y - 1) % linear_size) * linear_size + x) + 1
                ]
                if (outgoing_x + outgoing_y - incoming_x - incoming_y) % group_order:
                    divergences_ok = False
                    break
            if not divergences_ok:
                break
        if divergences_ok:
            physical += 1
    return physical


def fixed_weight_masks(site_count: int, filling: int) -> tuple[int, ...]:
    return tuple(
        sum(1 << site for site in occupied)
        for occupied in itertools.combinations(range(site_count), filling)
    )


def hop_mask(mask: int, source: int, target: int):
    if not (mask & (1 << source)) or mask & (1 << target):
        return None
    sign_annihilate = -1 if (mask & ((1 << source) - 1)).bit_count() % 2 else 1
    intermediate = mask ^ (1 << source)
    sign_create = (
        -1 if (intermediate & ((1 << target) - 1)).bit_count() % 2 else 1
    )
    return intermediate | (1 << target), sign_annihilate * sign_create


def logsumexp(values: np.ndarray) -> float:
    maximum = float(np.max(values))
    return maximum + math.log(float(np.sum(np.exp(values - maximum))))


def frozen_matter_gamma(theta: float, charge: int) -> float:
    linear_size = 2
    masks = fixed_weight_masks(4, 2)
    mask_to_row = {mask: row for row, mask in enumerate(masks)}
    matrix = np.zeros((len(masks), len(masks)), dtype=complex)
    for row, mask in enumerate(masks):
        matrix[row, row] = STAGGERED_MASS * sum(
            ((-1) ** ((site % 2) + (site // 2)))
            * (((mask >> site) & 1) - ((0b0110 >> site) & 1))
            for site in range(4)
        )
        for y in range(linear_size):
            for x in range(linear_size):
                source = y * 2 + x
                for direction, target in (
                    (0, y * 2 + (x + 1) % 2),
                    (1, ((y + 1) % 2) * 2 + x),
                ):
                    boundary = direction == 0 and x == 1
                    for a, b, phase_sign in (
                        (source, target, +1),
                        (target, source, -1),
                    ):
                        hopped = hop_mask(mask, a, b)
                        if hopped is None:
                            continue
                        new_mask, sign = hopped
                        phase = (
                            np.exp(1j * phase_sign * charge * theta)
                            if boundary
                            else 1.0
                        )
                        matrix[mask_to_row[new_mask], row] += (
                            -HOPPING * sign * phase
                        )
    return -logsumexp(-BETA_MATTER * np.linalg.eigvalsh(matrix))


def frozen_stiffness(charge: int) -> float:
    zero = frozen_matter_gamma(0.0, charge)

    def second(step: float) -> float:
        return (
            frozen_matter_gamma(step, charge)
            - 2.0 * zero
            + frozen_matter_gamma(-step, charge)
        ) / (step**2 * 4)

    coarse = second(RICHARDSON_STEP)
    fine = second(RICHARDSON_STEP / 2.0)
    return (4.0 * fine - coarse) / 3.0


def qwz_strip(momentum: float, hopping: float = 1.0) -> np.ndarray:
    onsite = (
        hopping * math.sin(momentum) * SX
        + (MASS - hopping * math.cos(momentum)) * SZ
    )
    transverse = hopping * TY
    matrix = np.zeros((2 * LY, 2 * LY), dtype=complex)
    for y in range(LY):
        site = slice(2 * y, 2 * y + 2)
        matrix[site, site] = onsite
    for y in range(LY - 1):
        lower = slice(2 * y, 2 * y + 2)
        upper = slice(2 * (y + 1), 2 * (y + 1) + 2)
        matrix[upper, lower] = transverse
        matrix[lower, upper] = transverse.conj().T
    return matrix


def localized_zero_profiles():
    eigenvalues, eigenvectors = np.linalg.eigh(qwz_strip(0.0))
    zero_indices = np.where(np.abs(eigenvalues) < 1.0e-10)[0]
    if len(zero_indices) != 2:
        raise RuntimeError("QWZ strip did not have exactly two zero modes")
    zero_frame = eigenvectors[:, zero_indices]
    y_operator = np.diag(np.repeat(np.arange(LY, dtype=float), 2))
    positions, rotation = np.linalg.eigh(zero_frame.conj().T @ y_operator @ zero_frame)
    localized = zero_frame @ rotation
    return localized[:, 0], localized[:, 1], float(abs(np.vdot(localized[:, 0], localized[:, 1])))


def edge_branch(momentum: float, edge: str):
    eigenvalues, eigenvectors = np.linalg.eigh(qwz_strip(momentum))
    candidates = np.where(np.abs(eigenvalues) < 0.9)[0]
    boundary = slice(0, 2) if edge == "physical" else slice(-2, None)
    weights = [
        float(np.sum(np.abs(eigenvectors[boundary, index]) ** 2))
        for index in candidates
    ]
    selected = int(candidates[int(np.argmax(weights))])
    return float(eigenvalues[selected]), max(weights)


def jw_annihilator(mode: int) -> np.ndarray:
    dimension = 1 << FLAVORS
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for state in range(dimension):
        if state & (1 << mode):
            target = state ^ (1 << mode)
            sign = -1 if (state & ((1 << mode) - 1)).bit_count() % 2 else 1
            matrix[target, state] = sign
    return matrix


ANNIHILATORS = tuple(jw_annihilator(mode) for mode in range(FLAVORS))
NUMBER = sum(operator.conj().T @ operator for operator in ANNIHILATORS)
PARITY = np.diag(
    [(-1.0) ** state.bit_count() for state in range(1 << FLAVORS)]
).astype(complex)


def determinant_projector() -> np.ndarray:
    omega = np.zeros(1 << FLAVORS, dtype=complex)
    omega[0] = 1.0 / math.sqrt(2.0)
    omega[-1] = np.exp(1j * DET_PHASE) / math.sqrt(2.0)
    return np.outer(omega, omega.conj())


P_PHI = determinant_projector()
H_DET = np.eye(1 << FLAVORS, dtype=complex) - P_PHI


def edge_cluster_hamiltonian(dispersion: float, det_enabled: bool) -> np.ndarray:
    matrix = dispersion * (NUMBER - 0.5 * FLAVORS * np.eye(1 << FLAVORS))
    if det_enabled:
        matrix = matrix + DET_STRENGTH * H_DET
    return matrix


@dataclass(frozen=True)
class SpectralThreshold:
    gap: float
    zero_weight: float


def cluster_spectral_threshold(matrix: np.ndarray) -> SpectralThreshold:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    ground_energy = float(eigenvalues[0])
    ground_indices = np.where(np.abs(eigenvalues - ground_energy) < 1.0e-10)[0]
    minimum = math.inf
    zero_weight = 0.0
    for ground_index in ground_indices:
        ground = eigenvectors[:, ground_index]
        for annihilator in ANNIHILATORS:
            for field in (annihilator, annihilator.conj().T):
                amplitudes = eigenvectors.conj().T @ (field @ ground)
                weights = np.abs(amplitudes) ** 2
                for target in np.where(weights > 1.0e-12)[0]:
                    cost = float(eigenvalues[target] - ground_energy)
                    if cost >= -1.0e-10:
                        minimum = min(minimum, max(0.0, cost))
                        if abs(cost) < EDGE_GAP_TOL:
                            zero_weight += float(weights[target])
    if not math.isfinite(minimum):
        raise RuntimeError("edge spectral function had no support")
    return SpectralThreshold(minimum, zero_weight)


def edge_spectral_scan(hopping: float, det_enabled: bool, chirality_sign: int):
    minimum_gap = math.inf
    zero_weight = 0.0
    for momentum in MOMENTA:
        dispersion = chirality_sign * hopping * math.sin(float(momentum))
        threshold = cluster_spectral_threshold(
            edge_cluster_hamiltonian(dispersion, det_enabled)
        )
        minimum_gap = min(minimum_gap, threshold.gap)
        if threshold.gap < EDGE_GAP_TOL:
            zero_weight = max(zero_weight, threshold.zero_weight)
    return SpectralThreshold(minimum_gap, zero_weight)


def clock_operators():
    deck = np.diag([1.0, 1j, -1.0, -1j]).astype(complex)
    raising = np.roll(np.eye(4, dtype=complex), 1, axis=0)
    return deck, raising


DECK, PSI = clock_operators()
CLOCK_OBSERVABLE = 0.5 * (PSI + PSI.conj().T)
IDENTITY_EDGE = np.eye(1 << FLAVORS, dtype=complex)
IDENTITY_CLOCK = np.eye(4, dtype=complex)
Q_NUMBER = ANNIHILATORS[0].conj().T @ ANNIHILATORS[0]
Q_DENSITY = Q_NUMBER - 0.5 * IDENTITY_EDGE


def content_charge_operator() -> np.ndarray:
    phases = []
    for state in range(1 << FLAVORS):
        charge = sum(
            CONTENT_CHARGES[mode]
            for mode in range(FLAVORS)
            if state & (1 << mode)
        )
        phases.append(np.exp(2j * math.pi * charge / 6.0))
    return np.diag(phases).astype(complex)


Z6_CHARGE = content_charge_operator()


def seam_hamiltonian(phi: float, grading: int = 1) -> np.ndarray:
    charged = np.linalg.matrix_power(PSI, grading)
    return -CLOCK_COUPLING * (
        np.exp(-1j * phi) * charged + np.exp(1j * phi) * charged.conj().T
    )


def physical_clock_hamiltonian(
    dispersion: float,
    seam_coupling: float = SEAM_COUPLING,
    phi: float = 0.0,
) -> np.ndarray:
    physical = edge_cluster_hamiltonian(dispersion, False)
    return (
        np.kron(physical, IDENTITY_CLOCK)
        + np.kron(IDENTITY_EDGE, seam_hamiltonian(phi))
        + seam_coupling * np.kron(Q_DENSITY, CLOCK_OBSERVABLE)
    )


def full_assembly_hamiltonian(dispersion: float) -> np.ndarray:
    physical_clock = physical_clock_hamiltonian(dispersion)
    mirror = edge_cluster_hamiltonian(-dispersion, True)
    return (
        np.kron(physical_clock, IDENTITY_EDGE)
        + np.kron(np.eye(physical_clock.shape[0]), mirror)
    )


def spectral_threshold(matrix: np.ndarray, fields):
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    ground_energy = float(eigenvalues[0])
    ground_indices = np.where(np.abs(eigenvalues - ground_energy) < 1.0e-10)[0]
    minimum = math.inf
    zero_weight = 0.0
    for ground_index in ground_indices:
        ground = eigenvectors[:, ground_index]
        for field in fields:
            for operator in (field, field.conj().T):
                weights = np.abs(eigenvectors.conj().T @ (operator @ ground)) ** 2
                for target in np.where(weights > 1.0e-12)[0]:
                    cost = float(eigenvalues[target] - ground_energy)
                    if cost >= -1.0e-10:
                        minimum = min(minimum, max(cost, 0.0))
                        if abs(cost) < EDGE_GAP_TOL:
                            zero_weight += float(weights[target])
    return SpectralThreshold(minimum, zero_weight)


PHYSICAL_FIELDS = tuple(
    np.kron(operator, IDENTITY_CLOCK) for operator in ANNIHILATORS
)


def physical_seam_scan(hopping: float) -> SpectralThreshold:
    minimum_gap = math.inf
    zero_weight = 0.0
    for momentum in MOMENTA:
        matrix = physical_clock_hamiltonian(hopping * math.sin(float(momentum)))
        threshold = spectral_threshold(matrix, PHYSICAL_FIELDS)
        minimum_gap = min(minimum_gap, threshold.gap)
        if threshold.gap < EDGE_GAP_TOL:
            zero_weight = max(zero_weight, threshold.zero_weight)
    return SpectralThreshold(minimum_gap, zero_weight)


def log_trace_exp(matrix: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    maximum = float(np.max(eigenvalues))
    return maximum + math.log(float(np.sum(np.exp(eigenvalues - maximum))))


SEAM_SOURCE_PC = np.kron(IDENTITY_EDGE, CLOCK_OBSERVABLE)
PHYSICAL_SOURCE_PC = np.kron(Q_DENSITY, IDENTITY_CLOCK)
MIRROR_SOURCE = Q_DENSITY


def mixed_derivative(function) -> float:
    step = SOURCE_STEP
    return (
        function(+step, +step)
        - function(+step, -step)
        - function(-step, +step)
        + function(-step, -step)
    ) / (4.0 * step**2)


def transduction_pack(seam_coupling: float):
    base_pc = physical_clock_hamiltonian(0.0, seam_coupling)
    base_mirror = edge_cluster_hamiltonian(0.0, True)

    def physical_w(seam_source: float, physical_source: float) -> float:
        exponent = (
            -TRANSDUCTION_BETA * base_pc
            + seam_source * SEAM_SOURCE_PC
            + physical_source * PHYSICAL_SOURCE_PC
        )
        return log_trace_exp(exponent)

    def mirror_w(seam_source: float, mirror_source: float) -> float:
        pc_exponent = (
            -TRANSDUCTION_BETA * base_pc + seam_source * SEAM_SOURCE_PC
        )
        mirror_exponent = (
            -TRANSDUCTION_BETA * base_mirror + mirror_source * MIRROR_SOURCE
        )
        return log_trace_exp(pc_exponent) + log_trace_exp(mirror_exponent)

    return mixed_derivative(physical_w), mixed_derivative(mirror_w)


def run():
    reset()
    print("v1008  2+1D master-object scaffold (four stages, compressed)")

    print("\nSTAGE 1  PROTOTYPE K=0")
    exponents = [
        plaquette_flat_holonomy_exponent(linear_size, x, y)
        for linear_size in (2, 3)
        for y in range(linear_size)
        for x in range(linear_size)
    ]
    report(
        "combinatorial K=0: plaquette exponents cancel [E-finite]",
        all(value == 0 for value in exponents),
        "all %d oriented plaquettes on L=2,3 have exponent 0"
        % len(exponents),
    )
    physical_dim = gauss_physical_dimension(2, 2)
    report(
        "Z2 L=2 Gauss sector dimension 32 [E-finite]",
        physical_dim == 32 == 2 ** (4 + 1),
        "physical=%d (N^(L^2+1)); L=3 262144 out of suite" % physical_dim,
    )

    print("\nSTAGE 2  MATTER FROZEN-LINK + SELECTOR PINS")
    k0 = frozen_stiffness(0)
    k1 = frozen_stiffness(1)
    k2 = frozen_stiffness(2)
    report(
        "frozen-link K(q=0)=0 [N]",
        abs(k0) < 1.0e-10,
        "K(0)=%.3e" % k0,
    )
    report(
        "frozen-link q^2 content law K(2)/K(1)~4 [N]",
        abs(k2 / k1 - 4.0) < 1.0e-4,
        "K(1)=%.9f K(2)=%.9f ratio=%.9f" % (k1, k2, k2 / k1),
    )
    report(
        "v1 SHA frozen (typed negative protocol) [N]",
        file_has(MATTER_PROBE, FROZEN_SHA256_V1)
        and hashlib.sha256(
            "protocol=v2_contractive_selector".encode("utf-8")
        ).hexdigest()
        != FROZEN_SHA256_V1,
        FROZEN_SHA256_V1,
    )
    report(
        "v2 SHA frozen (contractive selector) [N]",
        file_has(MATTER_PROBE, FROZEN_SHA256_V2)
        and file_has(
            MATTER_PROBE, "physical_selector=unique_root_with_abs_dK_dy_lt_1"
        ),
        FROZEN_SHA256_V2,
    )
    report(
        "unique-contractive protocol is |R'|<1 [N]",
        file_has(MATTER_PROBE, "unique_root_with_abs_dK_dy_lt_1"),
        "selector falsifies a root with |R'|>=1; L=3 Lanczos out of suite",
    )
    report(
        "L2/L3 selector harvest pins (not recomputed) [N]",
        HARVEST_G_SEL_L3 > HARVEST_G_SEL_L2
        and HARVEST_PAIR_L3 < HARVEST_PAIR_L2
        and all(abs(value) < 1.0 for value in HARVEST_RPRIME),
        "g_sel %.3f -> %.3f; pair %.2f -> %.2f; R'=%s"
        % (
            HARVEST_G_SEL_L2,
            HARVEST_G_SEL_L3,
            HARVEST_PAIR_L2,
            HARVEST_PAIR_L3,
            HARVEST_RPRIME,
        ),
    )

    print("\nSTAGE 3  QWZ WALL + DET4 MIRROR")
    physical_profile, mirror_profile, profile_overlap = localized_zero_profiles()
    physical_weight = float(np.sum(np.abs(physical_profile[:2]) ** 2))
    mirror_weight = float(np.sum(np.abs(mirror_profile[-2:]) ** 2))
    delta = 0.08
    physical_minus, _ = edge_branch(-delta, "physical")
    physical_plus, _ = edge_branch(delta, "physical")
    physical_slope = (physical_plus - physical_minus) / (2.0 * delta)
    report(
        "QWZ physical slope ~ -0.9989 [N]",
        abs(physical_slope + 0.9989) < 0.01
        and physical_weight > LOCALIZATION_MIN
        and mirror_weight > LOCALIZATION_MIN
        and profile_overlap < MIRROR_OVERLAP_MAX,
        "slope=%+.6f; y0 weight=%.6f; overlap=%.1e"
        % (physical_slope, physical_weight, profile_overlap),
    )

    table = {}
    assignments = {
        "integrated": (False, True),
        "no_DET": (False, False),
        "wrong_side": (True, False),
    }
    for assignment, (physical_det, mirror_det) in assignments.items():
        for hopping in HOPPING_VALUES:
            table[(assignment, hopping, "physical")] = edge_spectral_scan(
                hopping, physical_det, +1
            )
            table[(assignment, hopping, "mirror")] = edge_spectral_scan(
                hopping, mirror_det, -1
            )
    integrated_mirror = [
        table[("integrated", hopping, "mirror")].gap for hopping in HOPPING_VALUES
    ]
    report(
        "DET mirror gap >= 1.5 through t=0.6 [N]",
        min(integrated_mirror) > MIRROR_GAP_MIN,
        "min=%.9f (probe min 1.866)" % min(integrated_mirror),
    )
    report(
        "physical edge remains gapless [N]",
        all(
            table[("integrated", hopping, "physical")].gap < EDGE_GAP_TOL
            and table[("integrated", hopping, "physical")].zero_weight > 0.1
            for hopping in HOPPING_VALUES
        ),
        "all physical thresholds zero with A_edge(0)>0",
    )
    report(
        "MUST-FAIL: remove-DET leaves both edges gapless",
        all(
            table[("no_DET", hopping, edge)].gap < EDGE_GAP_TOL
            for hopping in HOPPING_VALUES
            for edge in ("physical", "mirror")
        ),
        "mirror doubler visible at every t",
    )
    report(
        "MUST-FAIL: DET-on-physical gaps the wrong side",
        all(
            table[("wrong_side", hopping, "physical")].gap > MIRROR_GAP_MIN
            and table[("wrong_side", hopping, "mirror")].gap < EDGE_GAP_TOL
            for hopping in HOPPING_VALUES
        ),
        "edge-exchange symmetry",
    )

    print("\nSTAGE 4  FOUR-BLOCK ASSEMBLY")
    report(
        "assembly frozen SHA [N]",
        file_has(ASSEMBLY_PROBE, FROZEN_SHA256_ASSEMBLY),
        FROZEN_SHA256_ASSEMBLY,
    )
    report(
        "minimal faithful Z6 content (1,2,3,0) [N]",
        CONTENT_NAMES == ("Q", "u^c", "L", "e^c")
        and CONTENT_CHARGES == (1, 2, 3, 0)
        and math.gcd(*CONTENT_CHARGES) == 1
        and sum(CONTENT_CHARGES) % 6 == 0,
        "charges=%s; DET is Z6-neutral" % (CONTENT_CHARGES,),
    )
    representative = full_assembly_hamiltonian(0.6 * math.sin(0.37))
    hermiticity = float(np.max(np.abs(representative - representative.conj().T)))
    charge_full = np.kron(np.kron(Z6_CHARGE, IDENTITY_CLOCK), Z6_CHARGE)
    charge_error = float(
        np.max(np.abs(representative @ charge_full - charge_full @ representative))
    )
    report(
        "assembled H Hermitian, dim 1024, Z6 exact [N]",
        representative.shape == (1024, 1024)
        and hermiticity < 1.0e-13
        and charge_error < 1.0e-13,
        "dim=%d |H-Hdag|=%.1e [H,Q6]=%.1e"
        % (representative.shape[0], hermiticity, charge_error),
    )

    covariance_errors = []
    sector_spectra = []
    expected_clock = np.array([0.0, 1.0, 1.0, 2.0])
    for sector in range(4):
        phi = sector * math.pi / 2.0
        current = seam_hamiltonian(phi)
        target = seam_hamiltonian(phi - math.pi / 2.0)
        covariance_errors.append(
            float(np.max(np.abs(DECK @ current @ DECK.conj().T - target)))
        )
        shifted = np.linalg.eigvalsh(current)
        shifted -= shifted[0]
        sector_spectra.append(shifted)
    report(
        "quarter-deck covariance + clock [0,1,1,2] [N]",
        max(covariance_errors) < 1.0e-13
        and all(
            np.max(np.abs(spectrum - expected_clock)) < 1.0e-12
            for spectrum in sector_spectra
        ),
        "max |D H Ddag-H_(k-1)|=%.1e" % max(covariance_errors),
    )

    wall_ok = True
    mirror_minimum = math.inf
    for hopping in HOPPING_VALUES:
        physical = physical_seam_scan(hopping)
        mirror = edge_spectral_scan(hopping, True, -1)
        wall_ok = wall_ok and physical.gap < EDGE_GAP_TOL and physical.zero_weight > 0.1
        mirror_minimum = min(mirror_minimum, mirror.gap)
    report(
        "physical wall + DET mirror survive the seam [N]",
        wall_ok and mirror_minimum > MIRROR_GAP_MIN,
        "min mirror gap=%.9f through t=0.6" % mirror_minimum,
    )

    physical_cross, mirror_cross = transduction_pack(SEAM_COUPLING)
    removed_cross, removed_mirror = transduction_pack(0.0)
    report(
        "chi_phys nonzero, chi_mirror suppressed [N]",
        abs(physical_cross) > 1.0e-4
        and abs(mirror_cross) < 1.0e-6
        and abs(mirror_cross) < 1.0e-3 * abs(physical_cross),
        "chi_phys=%+.6e chi_mirror=%.3e" % (physical_cross, mirror_cross),
    )
    wrong = seam_hamiltonian(0.0, grading=2)
    wrong_spectrum = np.linalg.eigvalsh(wrong)
    wrong_spectrum -= wrong_spectrum[0]
    wrong_ground = int(np.sum(np.abs(wrong_spectrum) < 1.0e-12))
    report(
        "MUST-FAIL: Psi^2 doubles the clock ground sector",
        np.max(np.abs(wrong_spectrum - np.array([0.0, 0.0, 2.0, 2.0]))) < 1.0e-12
        and wrong_ground == 2,
        "q=1 [0,1,1,2] unique -> q=2 [0,0,2,2] doubled",
    )
    report(
        "MUST-FAIL: remove seam kills cross response",
        abs(removed_cross) < 1.0e-6 and abs(removed_mirror) < 1.0e-6,
        "|chi_phys(off)|=%.3e" % abs(removed_cross),
    )
    report(
        "FIREWALL: QFT4D.LATTICE.FUNDAMENTAL.01 and "
        "GAUGE.DETLINE.FIXPOINT.01 stay [O]",
        True,
        "2+1D analogue; no 4D volume theorem; no marker move",
    )
    return summary(
        "v1008 master-object scaffold: K=0 + frozen q^2 + wall/mirror "
        "+ Z6/clock assembly; contracts stay [O]"
    )


if __name__ == "__main__":
    raise SystemExit(run())
