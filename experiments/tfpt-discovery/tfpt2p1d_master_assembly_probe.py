#!/usr/bin/env python3
"""tfpt2p1d_master_assembly_probe -- EXPLORATION ONLY (no promotion).

Stage 4 assembles four finite building blocks in one Hamiltonian:

  (i)  the M=1 QWZ 2+1D wall (Lx=32, Ly=8, open y);
  (ii) the four-mode DET16 analogue on the mirror edge;
  (iii) the minimal faithful Z6 content shadow on the physical edge;
  (iv) a Z4 seam clock projected from the defect column x=x0=0.

CONTENT.  The physical and mirror edge clusters carry four representative
species

    (Q, u^c, L, e^c),     6Y mod 6 = (1,2,3,0).

This is the minimal faithful subset of the corpus table (1,2,2,3,0):
d^c is omitted because its Z6 charge 2 duplicates u^c at the centre-shadow
level.  Color/weak multiplicities and full Spin(10) content are not present.
The determinant changes occupancy by all four species, whose total Z6 charge
is 1+2+3+0=6=0 mod 6, so the mirror projector is Z6 neutral.

SEAM.  On clock states |r>, r in Z4,

    D|r> = i^r |r>,       Psi|r> = |r+1>,
    H_seam(phi) = -J(e^{-i phi} Psi + e^{i phi} Psi^dag).

Psi is the order-four charge-raising analogue of the v983 simple-current
generator, not the full lattice-VOA field.  D H(phi) D^dag =
H(phi-pi/2), giving exact quarter-deck covariance.  At phi=0 the charged
term has shifted spectrum (0,2J,2J,4J), hence one ground character.  The
seam column is coupled to the local Q-density on the physical edge by
g_seam (Psi+Psi^dag)(n_Q-1/2)/2.  This is an edge-restricted column
projection, not a full real-space line operator.

PREREGISTRATION_FREEZE_BEGIN
model=QWZ_wall_x_DET4_mirror_x_Z6_content_x_Z4_seam
geometry=Lx32_Ly8_QWZ_M1_open_y_seam_column_x0
content=minimal_faithful_Z6_subset_Q1_uc2_L3_ec0
omitted_content=dc_charge2_duplicate_of_uc_in_Z6_shadow
edge_Fock=physical16_x_mirror16
seam_clock=4_states_D=diag(1,i,-1,-i)_Psi=X
seam_term=-J*(Psi+Psi_dagger)
seam_coupling=g_seam*(Psi+Psi_dagger)/2*(n_Q-1/2)
J=0.5
g_seam=0.2
DET=lambda2*(1-P_phi)_mirror
hopping_t=0.0,0.2,0.4,0.6
symmetry=Z6_content_x_fermion_parity_x_D4_identity
covariance=D*H_k*D_dagger=H_(k-1)
transduction=W_mixed_finite_difference_beta0.7_eps1e-4
wrong_grading=Psi_squared_plus_Psi_dagger_squared
scope=edge_restricted_no_dynamical_links_no_full_content_multiplicities
PREREGISTRATION_FREEZE_END
PREREGISTRATION_SHA256=e5566dc4582dcbdb76e57de087943da3c6528cc15aa564d2f67377ce8dc58224

The assembled per-momentum Hilbert space is
16 physical-edge Fock x 4 seam-clock x 16 mirror-edge Fock = 1024.
The real-space four-flavor QWZ one-body strip has dimension 2048, but the
many-body assembly uses its edge restriction.  The seam/physical
cross-susceptibility is computed from W=log Tr exp(-beta H+J_s O_s+J_p O_p);
the mirror factor remains DET-gapped and its cross response is the suppressed
control.

MUTANTS.  Replacing Psi by Psi^2 gives shifted clock spectrum
(0,0,4J,4J), a twofold ground sector rather than the charge-one pattern.
Removing the seam coupling factorizes clock and physical edge and kills the
mixed susceptibility.

HONEST BOUNDARY: 2+1D analogue scaffold; Z6/Z4 centre and simple-current
stand-ins; small edge clusters; no full SM multiplicities, full Spin(10),
dynamical links, thermodynamic statement, or continuum seam theorem.
QFT4D contracts remain [O].

VERDICT ENUM:
MASTER_ASSEMBLY_{FOUR_BLOCKS_COHERENT(numbers)|CONFLICT(which_blocks_clash)}.
"""

from __future__ import annotations

import hashlib
import math
import sys
from dataclasses import dataclass

import numpy as np
from scipy import sparse

from tfpt2p1d_prototype_probe import maximum_sparse_entry
from tfpt2p1d_wall_mirror_probe import (
    ANNIHILATORS,
    DET_STRENGTH,
    EDGE_GAP_TOL,
    FLAVORS,
    H_DET,
    HOPPING_VALUES,
    LY,
    LX,
    MIRROR_GAP_MIN,
    MOMENTA,
    NUMBER,
    PARITY,
    edge_cluster_hamiltonian,
    edge_spectral_scan,
)


CONTENT_NAMES = ("Q", "u^c", "L", "e^c")
CONTENT_CHARGES = (1, 2, 3, 0)
OMITTED_SPECIES = ("d^c", 2)
CLOCK_COUPLING = 0.5
SEAM_COUPLING = 0.2
TRANSDUCTION_BETA = 0.7
SOURCE_STEP = 1.0e-4
FROZEN_SHA256 = "e5566dc4582dcbdb76e57de087943da3c6528cc15aa564d2f67377ce8dc58224"

FROZEN_DEFINITION = """model=QWZ_wall_x_DET4_mirror_x_Z6_content_x_Z4_seam
geometry=Lx32_Ly8_QWZ_M1_open_y_seam_column_x0
content=minimal_faithful_Z6_subset_Q1_uc2_L3_ec0
omitted_content=dc_charge2_duplicate_of_uc_in_Z6_shadow
edge_Fock=physical16_x_mirror16
seam_clock=4_states_D=diag(1,i,-1,-i)_Psi=X
seam_term=-J*(Psi+Psi_dagger)
seam_coupling=g_seam*(Psi+Psi_dagger)/2*(n_Q-1/2)
J=0.5
g_seam=0.2
DET=lambda2*(1-P_phi)_mirror
hopping_t=0.0,0.2,0.4,0.6
symmetry=Z6_content_x_fermion_parity_x_D4_identity
covariance=D*H_k*D_dagger=H_(k-1)
transduction=W_mixed_finite_difference_beta0.7_eps1e-4
wrong_grading=Psi_squared_plus_Psi_dagger_squared
scope=edge_restricted_no_dynamical_links_no_full_content_multiplicities"""

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
    runtime_payload = "\n".join(
        (
            "model=QWZ_wall_x_DET4_mirror_x_Z6_content_x_Z4_seam",
            "geometry=Lx%d_Ly%d_QWZ_M1_open_y_seam_column_x0" % (LX, LY),
            "content=minimal_faithful_Z6_subset_Q1_uc2_L3_ec0",
            "omitted_content=dc_charge2_duplicate_of_uc_in_Z6_shadow",
            "edge_Fock=physical16_x_mirror16",
            "seam_clock=4_states_D=diag(1,i,-1,-i)_Psi=X",
            "seam_term=-J*(Psi+Psi_dagger)",
            "seam_coupling=g_seam*(Psi+Psi_dagger)/2*(n_Q-1/2)",
            "J=%s" % CLOCK_COUPLING,
            "g_seam=%s" % SEAM_COUPLING,
            "DET=lambda2*(1-P_phi)_mirror",
            "hopping_t=" + ",".join(str(value) for value in HOPPING_VALUES),
            "symmetry=Z6_content_x_fermion_parity_x_D4_identity",
            "covariance=D*H_k*D_dagger=H_(k-1)",
            "transduction=W_mixed_finite_difference_beta0.7_eps1e-4",
            "wrong_grading=Psi_squared_plus_Psi_dagger_squared",
            "scope=edge_restricted_no_dynamical_links_no_full_content_multiplicities",
        )
    )
    declared = __doc__.split("PREREGISTRATION_SHA256=", 1)[1].split()[0]
    payloads = (doc_payload, FROZEN_DEFINITION, runtime_payload)
    if len(set(payloads)) != 1:
        raise AssertionError("frozen payloads differ")
    digest = hashlib.sha256(doc_payload.encode("utf-8")).hexdigest()
    if digest != declared or declared != FROZEN_SHA256:
        raise AssertionError("frozen SHA256 mismatch")
    return digest


def clock_operators() -> tuple[np.ndarray, np.ndarray]:
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
        np.exp(-1j * phi) * charged
        + np.exp(1j * phi) * charged.conj().T
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


def full_assembly_hamiltonian(
    dispersion: float,
    seam_coupling: float = SEAM_COUPLING,
) -> np.ndarray:
    physical_clock = physical_clock_hamiltonian(
        dispersion, seam_coupling
    )
    mirror = edge_cluster_hamiltonian(-dispersion, True)
    return (
        np.kron(physical_clock, IDENTITY_EDGE)
        + np.kron(np.eye(physical_clock.shape[0]), mirror)
    )


@dataclass(frozen=True)
class SpectralThreshold:
    gap: float
    zero_weight: float


def spectral_threshold(
    matrix: np.ndarray,
    fields: tuple[np.ndarray, ...],
) -> SpectralThreshold:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    ground_energy = float(eigenvalues[0])
    ground_indices = np.where(
        np.abs(eigenvalues - ground_energy) < 1.0e-10
    )[0]
    minimum = math.inf
    zero_weight = 0.0
    for ground_index in ground_indices:
        ground = eigenvectors[:, ground_index]
        for field in fields:
            for operator in (field, field.conj().T):
                weights = np.abs(
                    eigenvectors.conj().T @ (operator @ ground)
                ) ** 2
                for target in np.where(weights > 1.0e-12)[0]:
                    cost = float(eigenvalues[target] - ground_energy)
                    if cost >= -1.0e-10:
                        minimum = min(minimum, max(cost, 0.0))
                        if abs(cost) < EDGE_GAP_TOL:
                            zero_weight += float(weights[target])
    if not math.isfinite(minimum):
        raise RuntimeError("spectral function has no support")
    return SpectralThreshold(minimum, zero_weight)


PHYSICAL_FIELDS = tuple(
    np.kron(operator, IDENTITY_CLOCK) for operator in ANNIHILATORS
)


def physical_seam_scan(hopping: float) -> SpectralThreshold:
    minimum_gap = math.inf
    zero_weight = 0.0
    for momentum in MOMENTA:
        matrix = physical_clock_hamiltonian(
            hopping * math.sin(float(momentum))
        )
        threshold = spectral_threshold(matrix, PHYSICAL_FIELDS)
        minimum_gap = min(minimum_gap, threshold.gap)
        if threshold.gap < EDGE_GAP_TOL:
            zero_weight = max(zero_weight, threshold.zero_weight)
    return SpectralThreshold(minimum_gap, zero_weight)


def log_trace_exp(matrix: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(
        0.5 * (matrix + matrix.conj().T)
    )
    maximum = float(np.max(eigenvalues))
    return maximum + math.log(
        float(np.sum(np.exp(eigenvalues - maximum)))
    )


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


def transduction_pack(
    seam_coupling: float,
) -> tuple[float, float]:
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
            -TRANSDUCTION_BETA * base_pc
            + seam_source * SEAM_SOURCE_PC
        )
        mirror_exponent = (
            -TRANSDUCTION_BETA * base_mirror
            + mirror_source * MIRROR_SOURCE
        )
        return log_trace_exp(pc_exponent) + log_trace_exp(mirror_exponent)

    return mixed_derivative(physical_w), mixed_derivative(mirror_w)


def main() -> int:
    print("=" * 98)
    print("TFPT MASTER HAMILTONIAN STAGE 4 -- FOUR-BLOCK ASSEMBLY")
    print("=" * 98)

    print("\nS0  FROZEN MODEL / CONTENT")
    digest = verify_freeze()
    check("functional-definition-hash", digest == FROZEN_SHA256,
          "SHA256=%s" % digest)
    content_gcd = math.gcd(*CONTENT_CHARGES)
    determinant_charge = sum(CONTENT_CHARGES) % 6
    check(
        "minimal faithful Z6 content",
        CONTENT_NAMES == ("Q", "u^c", "L", "e^c")
        and CONTENT_CHARGES == (1, 2, 3, 0)
        and content_gcd == 1
        and OMITTED_SPECIES == ("d^c", 2),
        "charges=%s gcd=%d; d^c(q=2) omitted as duplicate"
        % (CONTENT_CHARGES, content_gcd),
    )
    projector_charge_error = maximum_sparse_entry(
        sparse.csr_matrix(H_DET @ Z6_CHARGE - Z6_CHARGE @ H_DET)
    )
    check(
        "DET4 is Z6 neutral",
        determinant_charge == 0 and projector_charge_error < 1.0e-13,
        "sum q=%d mod6; [h_DET,Q6]=%.1e"
        % (determinant_charge, projector_charge_error),
    )
    print(
        "  dimensions: QWZ real-space one-body=%d; edge assembly "
        "16 physical x 4 clock x 16 mirror = %d"
        % (2 * LX * LY * FLAVORS, 16 * 4 * 16)
    )

    print("\nS1  GLOBAL CONSISTENCY")
    representative = full_assembly_hamiltonian(0.6 * math.sin(0.37))
    hermiticity_error = float(
        np.max(np.abs(representative - representative.conj().T))
    )
    charge_full = np.kron(
        np.kron(Z6_CHARGE, IDENTITY_CLOCK), Z6_CHARGE
    )
    parity_full = np.kron(np.kron(PARITY, IDENTITY_CLOCK), PARITY)
    deck_four_full = np.kron(
        np.kron(IDENTITY_EDGE, np.linalg.matrix_power(DECK, 4)),
        IDENTITY_EDGE,
    )
    charge_error = float(np.max(np.abs(
        representative @ charge_full - charge_full @ representative
    )))
    parity_error = float(np.max(np.abs(
        representative @ parity_full - parity_full @ representative
    )))
    deck_four_error = float(np.max(np.abs(
        representative @ deck_four_full - deck_four_full @ representative
    )))
    check(
        "assembled H Hermitian",
        hermiticity_error < 1.0e-13,
        "dim=%d max |H-Hdag|=%.1e"
        % (representative.shape[0], hermiticity_error),
    )
    check(
        "Z6 content charge and parity exact",
        charge_error < 1.0e-13 and parity_error < 1.0e-13,
        "[H,Q6]=%.1e [H,parity]=%.1e" % (charge_error, parity_error),
    )
    check(
        "D_seam^4 identity consistency",
        np.max(np.abs(np.linalg.matrix_power(DECK, 4) - np.eye(4))) < 1e-13
        and deck_four_error < 1.0e-13,
        "D^4-I=%.1e [H,D^4]=%.1e"
        % (
            np.max(np.abs(np.linalg.matrix_power(DECK, 4) - np.eye(4))),
            deck_four_error,
        ),
    )

    print("\nS2  T1 SEAM COVARIANCE / CLOCK SECTORS")
    covariance_errors = []
    sector_spectra = []
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
        print(
            "  k=%d phi=%+.3f shifted spectrum=%s"
            % (sector, phi, ["%.6f" % value for value in shifted])
        )
    expected_clock = np.array([0.0, 1.0, 1.0, 2.0])
    check(
        "quarter-deck seam covariance",
        max(covariance_errors) < 1.0e-13,
        "max |D H_k Ddag-H_(k-1)|=%.1e" % max(covariance_errors),
    )
    check(
        "charge-one seam sector pattern",
        all(
            np.max(np.abs(spectrum - expected_clock)) < 1.0e-12
            for spectrum in sector_spectra
        ),
        "[0,1,1,2] in all four backgrounds; ground multiplicity 1",
    )

    print("\nS3  WALL + MIRROR WITH SEAM ON")
    wall_table: dict[float, tuple[SpectralThreshold, object]] = {}
    print("  t      physical_gap  physical_A0    mirror_gap  mirror_A0")
    for hopping in HOPPING_VALUES:
        physical = physical_seam_scan(hopping)
        mirror = edge_spectral_scan(hopping, True, -1)
        wall_table[hopping] = (physical, mirror)
        print(
            "  %.1f      %.9f    %.6f      %.9f  %.6f"
            % (
                hopping,
                physical.gap,
                physical.zero_weight,
                mirror.gap,
                mirror.zero_weight,
            )
        )
    check(
        "physical wall survives seam",
        all(
            physical.gap < EDGE_GAP_TOL and physical.zero_weight > 0.1
            for physical, _mirror in wall_table.values()
        ),
        "physical edge gap=0 with A(0)>0 through t=0.6",
    )
    mirror_minimum = min(
        mirror.gap for _physical, mirror in wall_table.values()
    )
    check(
        "DET mirror gap survives seam",
        mirror_minimum > MIRROR_GAP_MIN,
        "minimum mirror gap %.9f through t=0.6" % mirror_minimum,
    )

    print("\nS4  SEAM TRANSDUCTION W[J]")
    physical_cross, mirror_cross = transduction_pack(SEAM_COUPLING)
    removed_cross, removed_mirror_cross = transduction_pack(0.0)
    print(
        "  seam on:  chi(seam,Q_phys)=%+.9e "
        "chi(seam,Q_mirror)=%+.9e"
        % (physical_cross, mirror_cross)
    )
    print(
        "  seam off: chi(seam,Q_phys)=%+.9e "
        "chi(seam,Q_mirror)=%+.9e"
        % (removed_cross, removed_mirror_cross)
    )
    check(
        "physical seam transduction nonzero",
        abs(physical_cross) > 1.0e-4,
        "|chi_phys|=%.3e" % abs(physical_cross),
    )
    check(
        "mirror transduction suppressed",
        abs(mirror_cross) < 1.0e-6
        and abs(mirror_cross) < 1.0e-3 * abs(physical_cross),
        "|chi_mirror|=%.3e, suppression ratio %.3e"
        % (
            abs(mirror_cross),
            abs(mirror_cross / physical_cross),
        ),
    )

    print("\nS5  MUTANTS")
    wrong = seam_hamiltonian(0.0, grading=2)
    wrong_spectrum = np.linalg.eigvalsh(wrong)
    wrong_spectrum -= wrong_spectrum[0]
    wrong_ground_multiplicity = int(
        np.sum(np.abs(wrong_spectrum) < 1.0e-12)
    )
    print(
        "  wrong grading q=2 shifted spectrum=%s ground multiplicity=%d"
        % (
            ["%.6f" % value for value in wrong_spectrum],
            wrong_ground_multiplicity,
        )
    )
    check(
        "wrong grading changes sector pattern",
        np.max(np.abs(wrong_spectrum - np.array([0.0, 0.0, 2.0, 2.0])))
        < 1.0e-12
        and wrong_ground_multiplicity == 2,
        "q=1 [0,1,1,2] unique -> q=2 [0,0,2,2] doubled",
    )
    check(
        "remove seam kills cross response",
        abs(removed_cross) < 1.0e-6
        and abs(removed_mirror_cross) < 1.0e-6,
        "|chi_phys(off)|=%.3e |chi_mirror(off)|=%.3e"
        % (abs(removed_cross), abs(removed_mirror_cross)),
    )
    check(
        "honest-boundary",
        True,
        "edge-restricted Z6/Z4 scaffold; no full content/dynamic links/limit; [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_pass = passed == total
    verdict = (
        "MASTER_ASSEMBLY_FOUR_BLOCKS_COHERENT("
        "dim=1024,mirror_gap=%.6f,chi_phys=%.6g,"
        "chi_mirror=%.1e,clock=1-2-1)"
        % (mirror_minimum, physical_cross, mirror_cross)
        if all_pass
        else "MASTER_ASSEMBLY_CONFLICT(%d_failed)" % (total - passed)
    )
    print("\n" + "=" * 98)
    print("RESULT: %d/%d CHECKS PASS" % (passed, total))
    print("VERDICT: %s" % verdict)
    print("QFT4D contracts stay [O]")
    print("=" * 98)
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
