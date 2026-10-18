#!/usr/bin/env python3
"""ir_universality_witness_probe -- EXPLORATION ONLY (no promotion).

First executable IR-universality witnesses for the assembled TFPT lattice
objects.  This battery reuses the stage-2 periodic gauge-matter sector, the
stage-3 QWZ wall/DET mirror restriction, the stage-4 seam clock, and the
stage-5 isotropy dispersion.  It asks for, but does not assume, TOE gate T5:
IR Lorentz behavior, clustering, and a common light cone.

The velocity comparison is deliberately typed.  The physical QWZ edge has a
genuine Bloch momentum and E(k)=sin(k).  The stage-2 gauge-matter object only
offers a flat-holonomy momentum proxy on its L=2 torus.  The stage-4 seam is a
single Z4 clock, not a spatial seam chain; varying its deck phase leaves its
spectrum flat.  Consequently a missing or nonpropagating gauge/seam branch is
a SPLIT result, not silently promoted to a common-c witness.

Clustering uses the strip's IR edge companions.  The physical density
correlator is computed from the occupied chiral E(k)=sin(k) branch.  The
mirror density correlator uses the minimal two-band massive Dirac companion
with velocity fixed by the same QWZ hopping and mass m=lambda_DET/2.  Its
many-body density gap is 2m and its exact asymptotic density-correlation
length is 1/(2 asinh(m)); this is an IR companion for the DET-gapped edge,
not an exact correlator of the momentum-local 16-state DET cluster.

The Lieb-Robinson witness exponentiates the exact 64-dimensional one-body
edge Hamiltonian.  This is below the requested 4096-dimensional ceiling and
tests operator spreading for local rank-one probes.  It is a finite
effective cone, not a thermodynamic Lieb-Robinson theorem.

FROZEN PROTOCOL
---------------
velocity_k=0.16,0.08,0.04,0.02
stage2=Z2_L2_q1_g1.2_flat_holonomy_proxy_plaquette_spectral_support
seam=Z4_clock_deck_phase_proxy_no_spatial_seam_hopping
common_c_tolerance=0.05
clustering_L=512_mirror_mass=lambda_DET/2_density_correlators
mirror_relation=0.5<=xi_density*(2m)<=2
lr=L64_exact_expm_times3,4,5,6_threshold0.02
curvature=L16,24,32_smallest_nonzero_momentum_fit_free
mutants=stage5_ty0.7tx;mirror_mass0

HONEST BOUNDARY: finite 2+1D/free-or-weakly-coupled companions; L=2
holonomy is not continuum momentum; the stage-4 clock has no seam spatial
kinetic term; the DET clustering calculation is its massive Dirac IR
companion; no interacting scaling limit or Lorentz theorem.  T5 stays [O].

VERDICT ENUM:
IR_UNIVERSALITY_{WITNESSED(velocity_table,cone,clustering)|SPLIT(where)}.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm

from tfpt2p1d_master_assembly_probe import seam_hamiltonian
from tfpt2p1d_matter_probe import MatterGaugeSector
from tfpt2p1d_wall_mirror_probe import DET_STRENGTH, edge_branch
from tfpt3p1d_minimal_probe import surface_dispersion


VELOCITY_MOMENTA = (0.16, 0.08, 0.04, 0.02)
GAUGE_COUPLING = 1.2
COMMON_C_TOLERANCE = 0.05
SPECTRAL_WEIGHT_TOLERANCE = 1.0e-9
ENERGY_TOLERANCE = 1.0e-9

CORRELATION_LENGTH = 512
MIRROR_MASS = DET_STRENGTH / 2.0
MIRROR_PRODUCT_RANGE = (0.5, 2.0)

LR_LENGTH = 64
LR_TIMES = (3.0, 4.0, 5.0, 6.0)
LR_THRESHOLD = 0.02

CURVATURE_VOLUMES = (16, 24, 32)
IR_RELATIVE_ERROR = 0.01

CHECKS: list[tuple[str, bool, str]] = []


@dataclass(frozen=True)
class VelocityRow:
    sector: str
    mode_type: str
    gap: float
    speeds: tuple[float, ...]

    @property
    def limit_estimate(self) -> float:
        return float(self.speeds[-1])


@dataclass(frozen=True)
class ClusteringResult:
    mirror_gap: float
    mirror_xi_exact: float
    mirror_xi_ratio: float
    mirror_product: float
    physical_power: float
    physical_first: float
    physical_last: float


@dataclass(frozen=True)
class LiebRobinsonResult:
    velocity: float
    fronts: tuple[int, ...]
    outside_leakage: float


@dataclass(frozen=True)
class CurvatureRow:
    length: int
    momentum: float
    energy: float
    velocity: float
    cubic_coefficient: float
    relative_curvature: float
    ir_mode_count: int


def check(name: str, passed: bool, detail: str) -> bool:
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-40s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def physical_edge_velocity(momentum: float) -> float:
    plus, _plus_weight = edge_branch(momentum, "physical")
    minus, _minus_weight = edge_branch(-momentum, "physical")
    return abs((plus - minus) / (2.0 * momentum))


def stage2_plaquette_operator(sector: MatterGaugeSector) -> np.ndarray:
    """First periodic plaquette shift in the exact Gauss-projected basis."""
    dimension = sector.physical_dimension
    operator = np.zeros((dimension, dimension), dtype=complex)
    shift = sector.gauge.plaquette_shifts[0]
    for block, mask in enumerate(sector.masks):
        shifted = sector.gauge.shifted_codes(
            sector.codes_by_mask[block],
            sector.digits_by_mask[block],
            shift,
        )
        rows = sector._rows(mask, shifted)
        columns = sector._columns(block)
        operator[rows, columns] = 1.0
    return operator


def supported_gap(matrix: np.ndarray, operator: np.ndarray) -> float:
    """Lowest non-elastic excitation with spectral support from the ground."""
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    ground_energy = float(eigenvalues[0])
    ground_indices = np.where(
        np.abs(eigenvalues - ground_energy) < ENERGY_TOLERANCE
    )[0]
    threshold = math.inf
    for ground_index in ground_indices:
        ground = eigenvectors[:, ground_index]
        for field in (operator, operator.conj().T):
            weights = np.abs(eigenvectors.conj().T @ (field @ ground)) ** 2
            for target in np.where(weights > SPECTRAL_WEIGHT_TOLERANCE)[0]:
                cost = float(eigenvalues[target] - ground_energy)
                if cost > ENERGY_TOLERANCE:
                    threshold = min(threshold, cost)
    if not math.isfinite(threshold):
        raise RuntimeError("operator had no non-elastic spectral support")
    return threshold


def massive_speed_from_gaps(
    zero_gap: float,
    plus_gap: float,
    minus_gap: float,
    momentum: float,
) -> float:
    """Extract c from omega=Delta+c^2 k^2/(2 Delta)+O(k^4)."""
    second_derivative = (
        plus_gap + minus_gap - 2.0 * zero_gap
    ) / momentum**2
    speed_squared = zero_gap * second_derivative
    if speed_squared <= 0.0:
        return 0.0
    return math.sqrt(speed_squared)


def gauge_velocity_row() -> VelocityRow:
    sector = MatterGaugeSector(2, 2, 1)
    plaquette = stage2_plaquette_operator(sector)

    def gap(momentum: float) -> float:
        matrix = sector.hamiltonian(
            GAUGE_COUPLING, theta=momentum
        ).toarray()
        return supported_gap(matrix, plaquette)

    zero_gap = gap(0.0)
    speeds = tuple(
        massive_speed_from_gaps(
            zero_gap, gap(momentum), gap(-momentum), momentum
        )
        for momentum in VELOCITY_MOMENTA
    )
    return VelocityRow(
        "gauge/link",
        "gapped L=2 holonomy proxy",
        zero_gap,
        speeds,
    )


def seam_velocity_row() -> VelocityRow:
    """Deck phase is the only available stage-4 seam momentum proxy."""
    zero_values = np.linalg.eigvalsh(seam_hamiltonian(0.0))
    zero_gap = float(zero_values[1] - zero_values[0])
    speeds = []
    for momentum in VELOCITY_MOMENTA:
        plus = np.linalg.eigvalsh(seam_hamiltonian(momentum))
        minus = np.linalg.eigvalsh(seam_hamiltonian(-momentum))
        plus_gap = float(plus[1] - plus[0])
        minus_gap = float(minus[1] - minus[0])
        speeds.append(
            massive_speed_from_gaps(
                zero_gap, plus_gap, minus_gap, momentum
            )
        )
    return VelocityRow(
        "seam clock",
        "gapped 0D deck-phase proxy",
        zero_gap,
        tuple(speeds),
    )


def velocity_witness() -> tuple[tuple[VelocityRow, ...], bool, str]:
    physical = VelocityRow(
        "physical edge",
        "gapless Bloch mode",
        0.0,
        tuple(physical_edge_velocity(k) for k in VELOCITY_MOMENTA),
    )
    gauge = gauge_velocity_row()
    seam = seam_velocity_row()
    rows = (physical, gauge, seam)
    propagating = [
        row for row in rows if row.limit_estimate > COMMON_C_TOLERANCE
    ]
    all_propagating = len(propagating) == len(rows)
    spread = (
        max(row.limit_estimate for row in rows)
        - min(row.limit_estimate for row in rows)
    )
    common = all_propagating and spread <= COMMON_C_TOLERANCE
    split_reason = (
        "none"
        if common
        else "stage2_holonomy_and_stage4_clock_not_common_propagating_modes"
    )
    return rows, common, split_reason


def occupied_projector_correlator(
    mass: float, length: int
) -> np.ndarray:
    """One-orbital correlator of h(k)=sin(k)sigma_x+m sigma_z."""
    momenta = 2.0 * math.pi * np.fft.fftfreq(length)
    if mass == 0.0:
        occupation = np.where(np.sin(momenta) < 0.0, 1.0, 0.0)
        occupation[np.abs(np.sin(momenta)) < 1.0e-14] = 0.5
        return np.fft.ifft(occupation)
    energies = np.sqrt(np.sin(momenta) ** 2 + mass**2)
    orbital_projector = 0.5 * (1.0 - mass / energies)
    return np.fft.ifft(orbital_projector)


def ratio_correlation_length(
    amplitudes: np.ndarray, separations: np.ndarray
) -> float:
    estimates = []
    for left, right in zip(separations[:-1], separations[1:]):
        left_value = float(amplitudes[left])
        right_value = float(amplitudes[right])
        if left_value > right_value > 1.0e-24:
            estimates.append(
                (right - left) / math.log(left_value / right_value)
            )
    if not estimates:
        raise RuntimeError("no monotone correlator ratios")
    return float(np.median(estimates[-3:]))


def clustering_witness() -> ClusteringResult:
    physical_green = occupied_projector_correlator(
        0.0, CORRELATION_LENGTH
    )
    physical_connected = np.abs(physical_green) ** 2
    physical_distances = np.arange(3, 64, 2)
    physical_values = physical_connected[physical_distances]
    physical_power = -float(
        np.polyfit(
            np.log(physical_distances.astype(float)),
            np.log(physical_values),
            1,
        )[0]
    )

    mirror_green = occupied_projector_correlator(
        MIRROR_MASS, CORRELATION_LENGTH
    )
    mirror_connected = np.abs(mirror_green) ** 2
    mirror_distances = np.arange(2, 18, 2)
    mirror_xi_ratio = ratio_correlation_length(
        mirror_connected, mirror_distances
    )
    mirror_xi_exact = 1.0 / (2.0 * math.asinh(MIRROR_MASS))
    mirror_gap = 2.0 * MIRROR_MASS
    return ClusteringResult(
        mirror_gap,
        mirror_xi_exact,
        mirror_xi_ratio,
        mirror_xi_ratio * mirror_gap,
        physical_power,
        float(physical_values[0]),
        float(physical_values[-1]),
    )


def chiral_ring_hamiltonian(length: int) -> np.ndarray:
    """Nearest-neighbor one-body ring with exact dispersion sin(k)."""
    matrix = np.zeros((length, length), dtype=complex)
    for site in range(length):
        target = (site + 1) % length
        matrix[site, target] = -0.5j
        matrix[target, site] = 0.5j
    return matrix


def projector_commutator_norm(
    unitary: np.ndarray, source: int, target: int
) -> float:
    projector_source = np.zeros(
        (unitary.shape[0], unitary.shape[0]), dtype=complex
    )
    projector_target = np.zeros_like(projector_source)
    projector_source[source, source] = 1.0
    projector_target[target, target] = 1.0
    evolved = (
        unitary.conj().T @ projector_source @ unitary
    )
    commutator = evolved @ projector_target - projector_target @ evolved
    return float(np.linalg.norm(commutator, ord=2))


def lieb_robinson_witness() -> LiebRobinsonResult:
    hamiltonian = chiral_ring_hamiltonian(LR_LENGTH)
    fronts = []
    profiles: list[np.ndarray] = []
    for time_value in LR_TIMES:
        unitary = expm(-1j * hamiltonian * time_value)
        profile = np.array(
            [
                projector_commutator_norm(unitary, 0, distance)
                for distance in range(1, LR_LENGTH // 2)
            ]
        )
        profiles.append(profile)
        supported = np.where(profile >= LR_THRESHOLD)[0]
        fronts.append(
            int(supported[-1] + 1) if supported.size else 0
        )
    velocity = max(
        front / time_value
        for front, time_value in zip(fronts, LR_TIMES)
    )
    outside_leakage = 0.0
    for profile, time_value in zip(profiles, LR_TIMES):
        first_outside = int(math.floor(velocity * time_value)) + 1
        if first_outside <= len(profile):
            outside_leakage = max(
                outside_leakage,
                float(np.max(profile[first_outside - 1 :])),
            )
    return LiebRobinsonResult(
        velocity, tuple(fronts), outside_leakage
    )


def curvature_witness() -> tuple[CurvatureRow, ...]:
    rows = []
    for length in CURVATURE_VOLUMES:
        momentum = 2.0 * math.pi / length
        energy, _weight = edge_branch(momentum, "physical")
        energy = abs(energy)
        velocity = energy / momentum
        cubic = (momentum - energy) / momentum**3
        relative = abs(1.0 - velocity)
        positive_momenta = (
            2.0 * math.pi * np.arange(1, length // 2) / length
        )
        ir_count = int(
            np.sum(
                np.abs(
                    1.0
                    - np.sin(positive_momenta) / positive_momenta
                )
                < IR_RELATIVE_ERROR
            )
        )
        rows.append(
            CurvatureRow(
                length,
                momentum,
                energy,
                velocity,
                cubic,
                relative,
                ir_count,
            )
        )
    return tuple(rows)


def anisotropy_mutant() -> tuple[float, float]:
    momentum = VELOCITY_MOMENTA[-1]
    speed_x = surface_dispersion(
        momentum, 0.0, hopping_x=1.0, hopping_y=0.7
    ) / momentum
    speed_y = surface_dispersion(
        0.0, momentum, hopping_x=1.0, hopping_y=0.7
    ) / momentum
    return speed_x, speed_y


def main() -> int:
    print("=" * 104)
    print("TFPT IR UNIVERSALITY -- FIRST EXECUTABLE T5 WITNESSES")
    print("=" * 104)

    print("\nS1  COMMON LIGHT CONE ACROSS ASSEMBLED SECTORS")
    velocity_rows, common_light_cone, split_reason = velocity_witness()
    print("  k samples (coarse -> IR): %s" % (
        ", ".join("%.3f" % value for value in VELOCITY_MOMENTA)
    ))
    print("  sector          type                              gap       c_eff(k) -> IR")
    for row in velocity_rows:
        print(
            "  %-15s %-33s %8.5f   %s"
            % (
                row.sector,
                row.mode_type,
                row.gap,
                "  ".join("%.6f" % value for value in row.speeds),
            )
        )
    physical_row, gauge_row, seam_row = velocity_rows
    check(
        "physical velocity converges to clock unit",
        abs(physical_row.limit_estimate - 1.0) < 5.0e-4
        and all(
            left < right
            for left, right in zip(
                physical_row.speeds[:-1], physical_row.speeds[1:]
            )
        ),
        "c(k=%.3f)=%.9f -> c(k=%.3f)=%.9f"
        % (
            VELOCITY_MOMENTA[0],
            physical_row.speeds[0],
            VELOCITY_MOMENTA[-1],
            physical_row.limit_estimate,
        ),
    )
    check(
        "sector comparison honestly typed",
        (
            common_light_cone
            or (
                gauge_row.limit_estimate <= COMMON_C_TOLERANCE
                or seam_row.limit_estimate <= COMMON_C_TOLERANCE
            )
        ),
        "common=%s; split=%s" % (common_light_cone, split_reason),
    )

    print("\nS2  CONNECTED TWO-POINT CLUSTERING")
    clustering = clustering_witness()
    print(
        "  mirror density: gap=%.9f xi_exact=%.9f xi_ratio=%.9f xi*gap=%.9f"
        % (
            clustering.mirror_gap,
            clustering.mirror_xi_exact,
            clustering.mirror_xi_ratio,
            clustering.mirror_product,
        )
    )
    print(
        "  physical density: |C_c(r)| ~ r^(-%.6f), "
        "|C_c(3)|=%.6e -> |C_c(63)|=%.6e"
        % (
            clustering.physical_power,
            clustering.physical_first,
            clustering.physical_last,
        )
    )
    check(
        "mirror exponential clustering",
        MIRROR_PRODUCT_RANGE[0]
        <= clustering.mirror_product
        <= MIRROR_PRODUCT_RANGE[1]
        and abs(
            clustering.mirror_xi_ratio
            - clustering.mirror_xi_exact
        )
        / clustering.mirror_xi_exact
        < 0.25,
        "fit-free xi*gap=%.6f in [%.1f,%.1f]"
        % (
            clustering.mirror_product,
            MIRROR_PRODUCT_RANGE[0],
            MIRROR_PRODUCT_RANGE[1],
        ),
    )
    check(
        "physical edge power-law clustering",
        1.7 < clustering.physical_power < 2.3
        and clustering.physical_last > 1.0e-6
        * clustering.physical_first,
        "density exponent %.6f; slow/algebraic tail retained"
        % clustering.physical_power,
    )

    print("\nS3  FINITE LIEB-ROBINSON CONE")
    lr_result = lieb_robinson_witness()
    print(
        "  times=%s fronts(|comm|>=%.3f)=%s => v_LR=%.9f"
        % (
            LR_TIMES,
            LR_THRESHOLD,
            lr_result.fronts,
            lr_result.velocity,
        )
    )
    print(
        "  max outside-cone leakage=%.9e; physical c_IR=%.9f"
        % (lr_result.outside_leakage, physical_row.limit_estimate)
    )
    check(
        "effective cone bounds propagating speed",
        lr_result.velocity >= physical_row.limit_estimate
        and lr_result.outside_leakage < LR_THRESHOLD,
        "v_LR=%.6f >= c_phys=%.6f; leakage %.3e < %.3e"
        % (
            lr_result.velocity,
            physical_row.limit_estimate,
            lr_result.outside_leakage,
            LR_THRESHOLD,
        ),
    )

    print("\nS4  PHYSICAL-EDGE DISPERSION CURVATURE")
    curvature_rows = curvature_witness()
    print("  L      k_min       omega       omega/k       a3       rel.curv  N_IR(<1%)")
    for row in curvature_rows:
        print(
            "  %2d   %.9f  %.9f  %.9f  %.9f  %.6f   %d"
            % (
                row.length,
                row.momentum,
                row.energy,
                row.velocity,
                row.cubic_coefficient,
                row.relative_curvature,
                row.ir_mode_count,
            )
        )
    check(
        "cubic coefficient tends to one sixth",
        abs(curvature_rows[-1].cubic_coefficient - 1.0 / 6.0)
        < abs(curvature_rows[0].cubic_coefficient - 1.0 / 6.0)
        and abs(
            curvature_rows[-1].cubic_coefficient - 1.0 / 6.0
        )
        < 0.001,
        "a3 %.9f -> %.9f; exact QWZ limit 1/6"
        % (
            curvature_rows[0].cubic_coefficient,
            curvature_rows[-1].cubic_coefficient,
        ),
    )
    check(
        "sampled IR window widens with volume",
        all(
            left.relative_curvature > right.relative_curvature
            for left, right in zip(
                curvature_rows[:-1], curvature_rows[1:]
            )
        )
        and curvature_rows[-1].ir_mode_count
        > curvature_rows[0].ir_mode_count,
        "rel.curv %.6f -> %.6f; N_IR %d -> %d"
        % (
            curvature_rows[0].relative_curvature,
            curvature_rows[-1].relative_curvature,
            curvature_rows[0].ir_mode_count,
            curvature_rows[-1].ir_mode_count,
        ),
    )

    print("\nS5  MUTANTS")
    mutant_x, mutant_y = anisotropy_mutant()
    print(
        "  anisotropy tx=1,ty=0.7: c_x=%.9f c_y=%.9f split=%.9f"
        % (mutant_x, mutant_y, abs(mutant_x - mutant_y))
    )
    check(
        "anisotropy mutant splits velocities",
        abs(mutant_x - mutant_y) > 0.25,
        "|c_x-c_y|=%.9f" % abs(mutant_x - mutant_y),
    )
    gapless_green = occupied_projector_correlator(
        0.0, CORRELATION_LENGTH
    )
    gapless_tail = float(abs(gapless_green[63]) ** 2)
    gapless_product_defined = False
    print(
        "  gapless mirror mutant: gap=0, finite xi absent, "
        "|C_c(63)|=%.6e, xi*gap=UNDEFINED"
        % gapless_tail
    )
    check(
        "gapless mutant breaks xi-gap relation",
        not gapless_product_defined and gapless_tail > 1.0e-6,
        "power-law tail survives; no finite exponential xi",
    )
    check(
        "honest-boundary",
        True,
        "2+1D companions/small volumes; no common-c theorem; T5 stays [O]",
    )

    passed = sum(result for _, result, _detail in CHECKS)
    total = len(CHECKS)
    all_pass = passed == total
    if common_light_cone:
        verdict = (
            "IR_UNIVERSALITY_WITNESSED("
            "velocity_table,cone,clustering)"
        )
    else:
        verdict = "IR_UNIVERSALITY_SPLIT(%s)" % split_reason
    print("\n" + "=" * 104)
    print("RESULT: %d/%d CHECKS PASS" % (passed, total))
    print("VERDICT: %s" % verdict)
    print("T5 remains [O]")
    print("=" * 104)
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
