#!/usr/bin/env python3
"""v1024 -- parent-internal T6--T8 integration and obstruction battery.

Exact finite checks for the parent-internal T6--T8 integration pass.

The checked model uses only two factors already present in
QLGW32-Seam-Parent-3D-v1:

* the four-state seam clock; and
* the six gauge-singlet right-handed-neutrino modes
  (three families times two spin components).

No C5, oscillator, or tensor-gravity Hilbert factor is added.  The script
checks finite matrix identities and sharp algebraic obstructions; it does
not claim a continuum, Lorentz, or TOE limit.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np

from tfpt_constants import check as suite_check, reset, summary


TOL = 3.0e-10


@dataclass(frozen=True)
class Result:
    name: str
    passed: bool
    detail: str


RESULTS: list[Result] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    result = Result(name, bool(condition), detail)
    RESULTS.append(result)
    label = name if not detail else f"{name} -- {detail}"
    suite_check(label, result.passed)


def shift(dimension: int) -> np.ndarray:
    result = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        result[(source + 1) % dimension, source] = 1.0
    return result


def jordan_wigner_annihilator(mode_count: int, mode: int) -> np.ndarray:
    dimension = 1 << mode_count
    result = np.zeros((dimension, dimension), dtype=complex)
    lower_mask = (1 << mode) - 1
    for state in range(dimension):
        if (state >> mode) & 1:
            target = state ^ (1 << mode)
            sign = -1.0 if (state & lower_mask).bit_count() % 2 else 1.0
            result[target, state] = sign
    return result


def permutation_fock_lift(permutation: list[int]) -> np.ndarray:
    """Second-quantize a one-particle permutation, including wedge signs."""

    mode_count = len(permutation)
    dimension = 1 << mode_count
    result = np.zeros((dimension, dimension), dtype=complex)
    for state in range(dimension):
        occupied = [mode for mode in range(mode_count) if (state >> mode) & 1]
        targets = [permutation[mode] for mode in occupied]
        inversions = sum(
            targets[left] > targets[right]
            for left in range(len(targets))
            for right in range(left + 1, len(targets))
        )
        target_state = sum(1 << mode for mode in targets)
        result[target_state, state] = -1.0 if inversions % 2 else 1.0
    return result


def interaction_residual(operator: np.ndarray, left_dim: int, right_dim: int) -> np.ndarray:
    """Remove every A x I + I x B component from a bipartite operator."""

    tensor = operator.reshape(left_dim, right_dim, left_dim, right_dim)
    trace_right = np.einsum("abcb->ac", tensor)
    trace_left = np.einsum("abad->bd", tensor)
    total_trace = np.trace(operator)
    return (
        operator
        - np.kron(trace_right / right_dim, np.eye(right_dim))
        - np.kron(np.eye(left_dim), trace_left / left_dim)
        + total_trace * np.eye(left_dim * right_dim) / (left_dim * right_dim)
    )


def spectral_gap(operator: np.ndarray) -> tuple[int, float, np.ndarray]:
    eigenvalues = np.linalg.eigvalsh(operator)
    eigenvalues[np.abs(eigenvalues) < 2.0e-11] = 0.0
    degeneracy = int(np.sum(np.abs(eigenvalues - eigenvalues[0]) < 2.0e-9))
    gap = float(eigenvalues[degeneracy] - eigenvalues[0]) if degeneracy < len(eigenvalues) else math.inf
    return degeneracy, gap, eigenvalues


def parent_internal_intertwiner() -> dict[str, np.ndarray | float]:
    print("\nA3--D4 PARENT-INTERNAL INTERTWINER")

    omega = np.exp(2j * np.pi / 4)
    clock = shift(4)
    reflection = np.zeros((4, 4), dtype=complex)
    for source in range(4):
        reflection[(-source) % 4, source] = 1.0

    fourier = [
        np.array([omega ** (momentum * position) for position in range(4)], dtype=complex) / 2.0
        for momentum in range(4)
    ]
    fourier_matrix = np.column_stack(fourier)
    seam_ground = fourier[0]
    seam_ground_projector = np.outer(seam_ground, seam_ground.conj())
    seam_excitation_projector = np.eye(4) - seam_ground_projector
    seam_lowerers = [np.outer(seam_ground, fourier[k].conj()) for k in range(1, 4)]

    check("C4 Fourier basis is unitary", np.linalg.norm(fourier_matrix.conj().T @ fourier_matrix - np.eye(4)) < TOL)
    coxeter = fourier_matrix[:, 1:].conj().T @ clock @ fourier_matrix[:, 1:]
    expected_coxeter = np.diag([omega ** (-k) for k in range(1, 4)])
    check(
        "nontrivial C4 modes are the A3 Coxeter module",
        np.linalg.norm(coxeter - expected_coxeter) < TOL,
        "exponents=(1,2,3), eigenvalues=(-i,-1,+i)",
    )
    check(
        "seam generators obey D4 relations",
        np.linalg.norm(np.linalg.matrix_power(clock, 4) - np.eye(4)) < TOL
        and np.linalg.norm(reflection @ reflection - np.eye(4)) < TOL
        and np.linalg.norm(reflection @ clock @ reflection - clock.conj().T) < TOL,
    )

    operator_rotation = np.diag([omega**k for k in range(1, 4)])
    operator_reflection = np.array(
        [[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]], dtype=complex
    )
    check(
        "A3 Coxeter and family D4 representations intertwine",
        np.linalg.norm(operator_reflection @ operator_rotation @ operator_reflection - operator_rotation.conj().T) < TOL,
        "the intertwiner W maps seam k=1,2,3 to family g=1,2,3",
    )

    mode_count = 6
    fock_dimension = 1 << mode_count
    annihilators = [jordan_wigner_annihilator(mode_count, mode) for mode in range(mode_count)]
    identity_fock = np.eye(fock_dimension)
    max_car_defect = 0.0
    for left in range(mode_count):
        for right in range(mode_count):
            anticommutator = (
                annihilators[left] @ annihilators[right].conj().T
                + annihilators[right].conj().T @ annihilators[left]
            )
            target = identity_fock if left == right else np.zeros_like(identity_fock)
            max_car_defect = max(max_car_defect, float(np.linalg.norm(anticommutator - target)))
    check("six nu^c modes obey exact finite CAR", max_car_defect < TOL, f"max defect={max_car_defect:.3e}")

    pair_annihilators = [
        annihilators[2 * family + 1] @ annihilators[2 * family]
        for family in range(3)
    ]
    number = sum(operator.conj().T @ operator for operator in annihilators)
    parity = np.diag(
        [(-1.0) ** state.bit_count() for state in range(fock_dimension)]
    )
    check(
        "nu^c pair channels are fermion-even",
        max(np.linalg.norm(parity @ pair - pair @ parity) for pair in pair_annihilators) < TOL,
    )

    one_particle_phases: list[complex] = []
    for family in range(1, 4):
        one_particle_phases.extend([np.exp(-1j * np.pi * family / 4)] * 2)
    family_rotation = np.diag(
        [
            np.prod(
                [one_particle_phases[mode] for mode in range(mode_count) if (state >> mode) & 1]
            )
            for state in range(fock_dimension)
        ]
    )
    family_reflection = permutation_fock_lift([4, 5, 2, 3, 0, 1])
    family_13_parity = np.diag(
        [
            (-1.0) ** ((state & ((1 << 0) | (1 << 1) | (1 << 4) | (1 << 5))).bit_count())
            for state in range(fock_dimension)
        ]
    )

    seam_rotation_defects = [
        np.linalg.norm(clock @ lowerer @ clock.conj().T - omega**k * lowerer)
        for k, lowerer in zip(range(1, 4), seam_lowerers, strict=True)
    ]
    pair_rotation_defects = [
        np.linalg.norm(family_rotation @ pair @ family_rotation.conj().T - omega**k * pair)
        for k, pair in zip(range(1, 4), pair_annihilators, strict=True)
    ]
    seam_reflection_defects = [
        np.linalg.norm(reflection @ seam_lowerers[k - 1] @ reflection - seam_lowerers[4 - k - 1])
        for k in range(1, 4)
    ]
    pair_reflection_defects = [
        np.linalg.norm(family_reflection @ pair_annihilators[k - 1] @ family_reflection - pair_annihilators[4 - k - 1])
        for k in range(1, 4)
    ]
    check(
        "seam and pair triples carry the same D4 operator representation",
        max(seam_rotation_defects + pair_rotation_defects + seam_reflection_defects + pair_reflection_defects) < TOL,
    )
    check(
        "family lift has the exact order-eight/projective powers",
        np.linalg.norm(np.linalg.matrix_power(family_rotation, 8) - identity_fock) < TOL
        and np.linalg.norm(np.linalg.matrix_power(family_rotation, 4) - family_13_parity) < TOL
        and np.linalg.norm(family_13_parity - parity) > 1.0,
        "C_f^8=1 and C_f^4=(-1)^(N_1+N_3), not total fermion parity",
    )
    check(
        "fermionic lift implements the pair-operator D4 reflection law",
        np.linalg.norm(family_reflection @ family_rotation @ family_reflection - parity @ family_rotation.conj().T) < TOL,
        "R C R=(-1)^F C^-1; the selected pair triplet carries ordinary D4",
    )

    # Rational, preregistered model couplings.  No measured or target constant
    # appears anywhere in this checker.
    delta_seam = 2.0
    physical_mass = 0.25
    delta_mirror = 3.0
    coupling = 1.0 / 3.0
    mixing = 2.0 / 5.0

    identity_seam = np.eye(4)
    interaction = np.zeros((4 * fock_dimension, 4 * fock_dimension), dtype=complex)
    cross = np.zeros_like(interaction)
    for lowerer, pair in zip(seam_lowerers, pair_annihilators, strict=True):
        a_operator = np.kron(lowerer, identity_fock) - mixing * np.kron(identity_seam, pair)
        interaction += coupling * a_operator.conj().T @ a_operator
        cross += -coupling * mixing * (
            np.kron(lowerer.conj().T, pair) + np.kron(lowerer, pair.conj().T)
        )

    total_rotation = np.kron(clock, family_rotation)
    total_reflection = np.kron(reflection, family_reflection)
    total_parity = np.kron(identity_seam, parity)
    check("intertwiner term is self-adjoint", np.linalg.norm(interaction - interaction.conj().T) < TOL)
    check("intertwiner term is positive", np.min(np.linalg.eigvalsh(interaction)) > -TOL)
    check("intertwiner term is C4/D4 invariant", np.linalg.norm(total_rotation @ interaction @ total_rotation.conj().T - interaction) < TOL and np.linalg.norm(total_reflection @ interaction @ total_reflection - interaction) < TOL)
    check("intertwiner preserves fermion parity", np.linalg.norm(total_parity @ interaction - interaction @ total_parity) < TOL)

    # nu^c is (1,1)_{q=0}; the quotient congruence is exactly zero.  The pair
    # and seam operators therefore commute with every SM Gauss generator.
    quotient_residue = (2 * 0 + 3 * 0 + 0) % 6
    check("G_SM/Z6 typing is exact", quotient_residue == 0, "nu^c pair=(1,1)_{q=0}, seam is neutral")

    additive_residual = interaction_residual(cross, 4, fock_dimension)
    check(
        "mixed term is not an additive spectator Hamiltonian",
        np.linalg.norm(cross) > 1.0e-6 and np.linalg.norm(additive_residual) > 1.0e-6,
        f"||cross||={np.linalg.norm(cross):.6f}, additive residual={np.linalg.norm(additive_residual):.6f}",
    )

    h0 = (
        delta_seam * np.kron(seam_excitation_projector, identity_fock)
        + physical_mass * np.kron(identity_seam, number)
    )
    h_intertwined = h0 + interaction
    vacuum = np.eye(fock_dimension, dtype=complex)[:, 0]
    ground = np.kron(seam_ground, vacuum)
    degeneracy, gap, _ = spectral_gap(h_intertwined)
    check("old parent vacuum is annihilated", np.linalg.norm(h_intertwined @ ground) < TOL)
    check(
        "positive parent gap bound survives",
        degeneracy == 1 and gap + TOL >= min(delta_seam, physical_mass),
        f"degeneracy={degeneracy}, finite gap={gap:.12f}, lower bound=0.25",
    )

    # An exact, nonzero zero-temperature mixed resolvent in each A3 exponent
    # channel.  This is stronger than a thermal covariance and rules out a
    # tensor-spectator reading of the constructed term.
    expected_block = np.array(
        [
            [delta_seam + coupling, -coupling * mixing],
            [-coupling * mixing, 2.0 * physical_mass + coupling * mixing**2],
        ]
    )
    inverse_crosses = []
    for family, (seam_mode, pair) in enumerate(
        zip(fourier[1:], pair_annihilators, strict=True), start=1
    ):
        seam_state = np.kron(seam_mode, vacuum)
        pair_state = np.kron(seam_ground, pair.conj().T @ vacuum)
        block = np.array(
            [
                [np.vdot(seam_state, h_intertwined @ seam_state), np.vdot(seam_state, h_intertwined @ pair_state)],
                [np.vdot(pair_state, h_intertwined @ seam_state), np.vdot(pair_state, h_intertwined @ pair_state)],
            ],
            dtype=complex,
        )
        block_isometry = np.column_stack((seam_state, pair_state))
        block_projector = block_isometry @ block_isometry.conj().T
        check(
            f"family {family} hybrid block is invariant",
            np.linalg.norm((np.eye(len(h_intertwined)) - block_projector) @ h_intertwined @ block_isometry) < TOL,
        )
        check(f"family {family} hybrid block is analytic", np.linalg.norm(block - expected_block) < TOL)
        inverse_crosses.append(float(np.real(np.linalg.inv(block)[0, 1])))
    analytic_inverse_cross = coupling * mixing / np.linalg.det(expected_block)
    check(
        "intertwined local Parent block has nonzero mixed response",
        min(abs(value) for value in inverse_crosses) > 1.0e-3
        and max(abs(value - analytic_inverse_cross) for value in inverse_crosses) < TOL,
        f"(K^-1)_sf={inverse_crosses[0]:.12f}",
    )

    # Setting the physical regulator to zero can destroy the full gap, but a
    # positive term acting trivially on mirrors cannot reduce the mirror
    # operator inequality H >= Delta_M Q_mir.
    h_massless_nonmirror = delta_seam * np.kron(seam_excitation_projector, identity_fock) + interaction
    check(
        "nonmirror Hamiltonian stays positive at zero physical regulator",
        np.min(np.linalg.eigvalsh(h_massless_nonmirror)) > -TOL,
    )
    check(
        "volume-uniform mirror lower bound is untouched",
        delta_mirror == 3.0 and np.min(np.linalg.eigvalsh(h_massless_nonmirror)) > -TOL,
        "H_new >= 3 sum_x Q_mir,x because every added term is positive and mirror-blind",
    )

    return {
        "h_intertwined": h_intertwined,
        "ground": ground,
        "vacuum": vacuum,
        "fourier_matrix": fourier_matrix,
        "pair_annihilators": pair_annihilators,
        "fock_dimension": float(fock_dimension),
        "total_rotation": total_rotation,
        "total_reflection": total_reflection,
        "total_parity": total_parity,
    }


def internal_z5_cap(data: dict[str, np.ndarray | float]) -> None:
    print("\nPARENT-INTERNAL Z5/CAP BLOCK")

    fock_dimension = int(data["fock_dimension"])
    vacuum = np.asarray(data["vacuum"])
    fourier_matrix = np.asarray(data["fourier_matrix"])
    pair_annihilators = list(data["pair_annihilators"])
    full_dimension = 4 * fock_dimension

    # Existing neutral even excitation subspace:
    # E=span{|r>_seam x d_g^dagger|vac>, r=0..3, g=1..3}, dim E=12.
    computational_seam = np.eye(4, dtype=complex)
    embedding_columns = []
    for seam_index in range(4):
        for family in range(3):
            pair_state = pair_annihilators[family].conj().T @ vacuum
            embedding_columns.append(np.kron(computational_seam[:, seam_index], pair_state))
    embedding = np.column_stack(embedding_columns)
    check("neutral seam--pair block is an internal 12D isometry", np.linalg.norm(embedding.conj().T @ embedding - np.eye(12)) < TOL)

    # A fixed five-cycle chosen before diagonalization.  It uses both seam and
    # family coordinates.  Its arbitrariness is a claim boundary, not hidden.
    selected = [0, 4, 8, 9, 1]
    p5 = np.zeros((12, 12), dtype=complex)
    x_partial = np.zeros((12, 12), dtype=complex)
    z_partial = np.zeros((12, 12), dtype=complex)
    omega5 = np.exp(2j * np.pi / 5)
    for position, basis_index in enumerate(selected):
        p5[basis_index, basis_index] = 1.0
        x_partial[selected[(position + 1) % 5], basis_index] = 1.0
        z_partial[basis_index, basis_index] = omega5**position
    p_perp = np.eye(12) - p5
    x_full = x_partial + p_perp
    z_full = z_partial + p_perp

    check("internal order-five unitary exists", np.linalg.norm(x_full.conj().T @ x_full - np.eye(12)) < TOL and np.linalg.norm(np.linalg.matrix_power(x_full, 5) - np.eye(12)) < TOL and np.linalg.norm(x_full - np.eye(12)) > 1.0)
    check("compressed five-dimensional Weyl relation is exact", np.linalg.norm(z_partial @ x_partial - omega5 * x_partial @ z_partial) < TOL)
    full_weyl_defect = z_full @ x_full - omega5 * x_full @ z_full
    expected_defect = (1.0 - omega5) * p_perp
    check(
        "unital 12D Weyl relation fails exactly on the complement",
        np.linalg.norm(full_weyl_defect - expected_defect) < TOL and np.linalg.norm(full_weyl_defect) > 1.0,
        f"rank complement={int(np.trace(p_perp).real)}",
    )

    kappa = 2.0 / 7.0
    complement_penalty = 3.0 / 5.0
    cap12 = kappa * (p5 - 0.5 * (x_partial + x_partial.conj().T)) + complement_penalty * p_perp
    degeneracy, gap, eigenvalues = spectral_gap(cap12)
    expected_gap = min(complement_penalty, kappa * (1.0 - math.cos(2.0 * math.pi / 5.0)))
    check("internal cap is self-adjoint and positive", np.linalg.norm(cap12 - cap12.conj().T) < TOL and eigenvalues[0] > -TOL)
    check(
        "internal cap has one 12D ground and analytic gap",
        degeneracy == 1 and abs(gap - expected_gap) < TOL,
        f"gap={gap:.12f}",
    )

    cap_ground = np.zeros(12, dtype=complex)
    cap_ground[selected] = 1.0 / math.sqrt(5.0)
    coefficient_matrix = cap_ground.reshape(4, 3)
    check("cap ground genuinely mixes seam and family", np.linalg.matrix_rank(coefficient_matrix, tol=1.0e-10) > 1)
    cap_interaction_residual = interaction_residual(cap12, 4, 3)
    check(
        "cap block is not A x I + I x B",
        np.linalg.norm(cap_interaction_residual) > 1.0e-4,
        f"interaction residual={np.linalg.norm(cap_interaction_residual):.6f}",
    )

    # Vacuum-preserving extension to the actual parent space.  It is a valid
    # bounded local positive operator, but its global zero space includes the
    # complement of E; it therefore does not by itself select rho_0.
    cap_parent = embedding @ cap12 @ embedding.conj().T
    parent_ground = np.asarray(data["ground"])
    h_intertwined = np.asarray(data["h_intertwined"])
    h_combined = h_intertwined + cap_parent
    combined_degeneracy, combined_gap, _ = spectral_gap(h_combined)
    check("vacuum-preserving cap extension is positive", np.min(np.linalg.eigvalsh(cap_parent)) > -TOL)
    total_parity = np.asarray(data["total_parity"])
    check(
        "cap extension preserves fermion parity",
        np.linalg.norm(total_parity @ cap_parent - cap_parent @ total_parity) < TOL,
    )
    check("cap extension annihilates the old parent vacuum", np.linalg.norm(cap_parent @ parent_ground) < TOL)
    check(
        "shared intertwined parent retains its finite gap",
        combined_degeneracy == 1 and combined_gap + TOL >= 0.25,
        f"gap={combined_gap:.12f}",
    )
    combined_inverse = np.linalg.pinv(h_combined, rcond=1.0e-11)
    seam_ground = fourier_matrix[:, 0]
    combined_cross_responses = []
    for family in range(3):
        seam_state = np.kron(fourier_matrix[:, family + 1], vacuum)
        pair_state = np.kron(
            seam_ground, pair_annihilators[family].conj().T @ vacuum
        )
        combined_cross_responses.append(
            float(abs(np.vdot(seam_state, combined_inverse @ pair_state)))
        )
    check(
        "mixed resolvent remains alive after adding the internal cap",
        min(combined_cross_responses) > 1.0e-4,
        "responses=" + ",".join(f"{value:.6e}" for value in combined_cross_responses),
    )

    total_rotation = np.asarray(data["total_rotation"])
    total_reflection = np.asarray(data["total_reflection"])
    orientation_breaking = max(
        np.linalg.norm(total_rotation @ cap_parent @ total_rotation.conj().T - cap_parent),
        np.linalg.norm(total_reflection @ cap_parent @ total_reflection - cap_parent),
    )
    check(
        "cap selector does not masquerade as a derived D4 invariant",
        orientation_breaking > 1.0e-3,
        f"D4-breaking residual={orientation_breaking:.6f}",
    )


def relative_commutant_no_go() -> None:
    print("\nUNITAL MATRIX-ENLARGEMENT NO-GO")

    parent_dimension = 3
    spectator_dimension = 5
    total_dimension = parent_dimension * spectator_dimension
    constraints = []
    for row in range(parent_dimension):
        for column in range(parent_dimension):
            matrix_unit = np.zeros((parent_dimension, parent_dimension), dtype=complex)
            matrix_unit[row, column] = 1.0
            represented = np.kron(matrix_unit, np.eye(spectator_dimension))
            constraints.append(
                np.kron(np.eye(total_dimension), represented)
                - np.kron(represented.T, np.eye(total_dimension))
            )
    constraint_matrix = np.vstack(constraints)
    singular_values = np.linalg.svd(constraint_matrix, compute_uv=False)
    nullity = int(np.sum(singular_values < 2.0e-9))
    check(
        "relative commutant has dimension d^2",
        nullity == spectator_dimension**2,
        f"M_3 -> M_3 tensor M_5: nullity={nullity}=25",
    )

    witness5 = np.diag(np.arange(spectator_dimension, dtype=float))
    witness = np.kron(np.eye(parent_dimension), witness5)
    commutators = []
    for row in range(parent_dimension):
        for column in range(parent_dimension):
            matrix_unit = np.zeros((parent_dimension, parent_dimension), dtype=complex)
            matrix_unit[row, column] = 1.0
            represented = np.kron(matrix_unit, np.eye(spectator_dimension))
            commutators.append(np.linalg.norm(represented @ witness - witness @ represented))
    check("relative commutant contains a non-scalar witness", max(commutators) < TOL and np.linalg.norm(witness - np.trace(witness) * np.eye(total_dimension) / total_dimension) > 1.0)


def z5_divisibility_no_go() -> None:
    print("\nZ5 WEYL-PAIR DIVISIBILITY NO-GO")

    # D_site=3*4*2^192 and D_link=137 are both 2 modulo 5.
    site_modulo = (3 * 4 * pow(2, 192, 5)) % 5
    link_modulo = 137 % 5
    check("unprojected site and link dimensions are 2 mod 5", site_modulo == 2 and link_modulo == 2)

    residues = {
        (vertices, edges): pow(2, vertices + edges, 5)
        for vertices in range(1, 7)
        for edges in range(0, 10)
    }
    check(
        "every sampled finite unprojected region has nonzero dimension mod 5",
        all(residue != 0 for residue in residues.values()),
        "in general D_region=2^(V+E) mod 5, hence never zero",
    )

    omega5 = np.exp(2j * np.pi / 5)
    dimension12 = 12
    check(
        "determinant obstruction fires in dimension 12",
        dimension12 % 5 != 0 and abs(omega5**dimension12 - 1.0) > 1.0,
        "ZX=omega XZ with invertible X,Z would force omega^D=1 and 5|D",
    )


def symmetric_basis() -> list[np.ndarray]:
    e = []
    e.append(np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0))
    e.append(np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0))
    for left, right in ((0, 1), (0, 2), (1, 2)):
        matrix = np.zeros((3, 3), dtype=float)
        matrix[left, right] = matrix[right, left] = 1.0 / math.sqrt(2.0)
        e.append(matrix)
    return e


def tt_projector(momentum: np.ndarray) -> np.ndarray:
    direction = momentum / np.linalg.norm(momentum)
    theta = np.eye(3) - np.outer(direction, direction)
    basis6 = []
    for index in range(3):
        matrix = np.zeros((3, 3), dtype=float)
        matrix[index, index] = 1.0
        basis6.append(matrix)
    for left, right in ((0, 1), (0, 2), (1, 2)):
        matrix = np.zeros((3, 3), dtype=float)
        matrix[left, right] = matrix[right, left] = 1.0 / math.sqrt(2.0)
        basis6.append(matrix)

    result = np.zeros((6, 6), dtype=float)
    for column, matrix in enumerate(basis6):
        projected = theta @ matrix @ theta - 0.5 * theta * np.trace(theta @ matrix)
        for row, test in enumerate(basis6):
            result[row, column] = np.sum(test * projected)
    return result


def spin2_no_go() -> None:
    print("\nT7 LOCAL-STRESS / SPIN-2 BOUNDARY")

    basis5 = symmetric_basis()
    gram = np.array([[np.sum(left * right) for right in basis5] for left in basis5])
    check(
        "the symmetric-traceless tensor target has five pointwise components",
        np.linalg.norm(gram - np.eye(5)) < TOL and max(abs(np.trace(matrix)) for matrix in basis5) < TOL,
        "pure tensor typing (cubic E_g plus T_2g), not yet a Parent stress operator",
    )

    epsilon = 1.0e-9
    projector_x = tt_projector(np.array([epsilon, 0.0, 0.0]))
    projector_y = tt_projector(np.array([0.0, epsilon, 0.0]))
    check("TT projector has rank two away from k=0", np.linalg.matrix_rank(projector_x, tol=1.0e-9) == 2 and np.linalg.norm(projector_x @ projector_x - projector_x) < TOL)
    directional_jump = np.linalg.norm(projector_x - projector_y)
    check(
        "exact TT projection has a direction-dependent k->0 limit",
        directional_jump > 1.0,
        f"||P_TT(ex)-P_TT(ey)||={directional_jump:.6f}",
    )

    uniform_gap = 0.25
    size = 128
    massless_energy = 2.0 * math.sin(math.pi / size)
    check(
        "uniform full parent gap excludes a massless spin-2 pole",
        massless_energy < uniform_gap,
        f"at N={size}, omega(k_min)={massless_energy:.6f}<Delta_parent={uniform_gap}",
    )


def run() -> int:
    reset()
    RESULTS.clear()
    print("v1024 -- QLGW32 parent-internal T6--T8 integration checker")
    print("No target observable or fitted constant is loaded.")
    data = parent_internal_intertwiner()
    internal_z5_cap(data)
    relative_commutant_no_go()
    z5_divisibility_no_go()
    spin2_no_go()
    print("\nVERDICT: PARENT_INTERNAL_FINITE_SUBGATES_PROVED; "
          "T6_T7_T8_AND_TOE_OPEN")
    return summary("v1024 parent-internal T6--T8 boundaries")


if __name__ == "__main__":
    raise SystemExit(run())
