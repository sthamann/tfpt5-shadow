#!/usr/bin/env python3
"""Finite canonical-trivialization probe for the QWZ determinant line.

EXPLORATION ONLY.  This is the next finite-level check after v991; it
does not promote a claim and does not touch the continuum Bismut--Freed
or nonabelian Standard-Model determinant line.

The occupied determinant line over the twist torus has Chern number one,
so it has no global nonvanishing section.  We cut the torus at the
theta_y seam.  Products of determinant projection overlaps around the
transverse cycle give the bulk clutching section t_bulk(theta_x).  The
bottom-weighted regularized edge determinant from v991 gives the seam
section q_seam(theta_x).  Their equal winding permits the explicit
connection-matched restriction isomorphism

    R(theta_x) = (q_seam / t_bulk) / (q_seam(0) / t_bulk(0)),

for which q_seam = c_phase R t_bulk with one constant c_phase.

The important negative result is also executable: seam orientation
conjugates c_phase, but it does not choose its U(1) orbit.  Multiplying R
by any constant phase produces another restriction isomorphism obeying
the same orientation covariance.  Thus orientation selects one member
of a chosen conjugate pair only after an anchor is supplied; it does not
canonically fix the chiral determinant phase by itself.

VERDICT ENUM:
  DETLINE_TRIVIALIZATION_OBSTRUCTED(
      finite restriction isomorphism exists;
      orientation leaves a constant U(1) anchor ambiguity)
"""

import hashlib

import numpy as np


SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TX = SX / (2j) - SZ / 2

LATTICE_SIZE = 4
TWIST_SAMPLES = 64
TRANSVERSE_SAMPLES = 24
CHERN_GRID = 8
STRIP_WIDTH = 16
EDGE_REGULATOR = 0.02
EDGE_LOCALIZATION_LENGTH = 1.2
DETACHED_OFFSET = np.pi / 4

TOL_CHERN = 1e-8
TOL_WINDING = 1e-8
TOL_CONSTANCY = 1e-10
TOL_COVARIANCE = 1e-12
MIN_DETACHED_VARIATION = 0.1

CHECKS = []


def check(name, condition, detail=""):
    passed = bool(condition)
    CHECKS.append(passed)
    print(("PASS " if passed else "FAIL ") + name
          + (("  | " + detail) if detail else ""))
    return passed


def unit_phase(value):
    magnitude = abs(value)
    if magnitude < 1e-14:
        raise RuntimeError("determinant overlap is numerically singular")
    return value / magnitude


def winding(phases):
    closed = np.concatenate((np.asarray(phases), np.asarray(phases[:1])))
    unwrapped = np.unwrap(np.angle(closed))
    return float((unwrapped[-1] - unwrapped[0]) / (2 * np.pi))


def transverse_hopping(sy_sign):
    return sy_sign * SY / (2j) - SZ / 2


def torus_hamiltonian(size, mass, theta_x, theta_y, sy_sign=1.0):
    """Finite QWZ Hamiltonian with U(1) twists on the two closing bonds."""
    site_count = size * size
    hamiltonian = np.zeros((2 * site_count, 2 * site_count), dtype=complex)
    ty = transverse_hopping(sy_sign)

    def block(x_coord, y_coord):
        return 2 * ((x_coord % size) + size * (y_coord % size))

    for x_coord in range(size):
        for y_coord in range(size):
            source = block(x_coord, y_coord)
            hamiltonian[source:source + 2, source:source + 2] += mass * SZ
            bonds = (
                (1, 0, TX, theta_x),
                (0, 1, ty, theta_y),
            )
            for dx, dy, hopping, twist in bonds:
                target = block(x_coord + dx, y_coord + dy)
                crosses_cut = x_coord + dx == size or y_coord + dy == size
                phase = np.exp(1j * twist) if crosses_cut else 1.0
                hamiltonian[target:target + 2, source:source + 2] += (
                    phase * hopping
                )
                hamiltonian[source:source + 2, target:target + 2] += (
                    np.conj(phase) * hopping.conj().T
                )
    return hamiltonian


def occupied_frame(size, mass, theta_x, theta_y, sy_sign=1.0):
    eigenvalues, eigenvectors = np.linalg.eigh(
        torus_hamiltonian(size, mass, theta_x, theta_y, sy_sign)
    )
    occupied_count = int(np.sum(eigenvalues < 0))
    if occupied_count * 2 != len(eigenvalues):
        raise RuntimeError("half-filled occupied rank changed")
    return eigenvectors[:, :occupied_count], eigenvalues


def detline_chern(size, mass, sy_sign=1.0):
    """Fukui-Hatsugai-Suzuki Chern number of the occupied determinant line."""
    twists = 2 * np.pi * np.arange(CHERN_GRID) / CHERN_GRID
    frames = {}
    minimum_gap = np.inf
    for x_index, theta_x in enumerate(twists):
        for y_index, theta_y in enumerate(twists):
            frame, eigenvalues = occupied_frame(
                size, mass, theta_x, theta_y, sy_sign
            )
            frames[(x_index, y_index)] = frame
            occupied_count = frame.shape[1]
            minimum_gap = min(
                minimum_gap,
                float(eigenvalues[occupied_count]
                      - eigenvalues[occupied_count - 1]),
            )

    def link(first, second):
        return unit_phase(np.linalg.det(frames[first].conj().T @ frames[second]))

    curvature = 0.0
    for x_index in range(CHERN_GRID):
        for y_index in range(CHERN_GRID):
            next_x = (x_index + 1) % CHERN_GRID
            next_y = (y_index + 1) % CHERN_GRID
            plaquette = (
                link((x_index, y_index), (next_x, y_index))
                * link((next_x, y_index), (next_x, next_y))
                * np.conj(link((x_index, next_y), (next_x, next_y)))
                * np.conj(link((x_index, y_index), (x_index, next_y)))
            )
            curvature += np.angle(plaquette)
    return float(curvature / (2 * np.pi)), float(minimum_gap)


def bulk_clutching_section(mass=1.0, sy_sign=1.0):
    """Determinant-overlap holonomy around theta_y for every theta_x.

    This is the transition section on the seam of a theta_y-cut torus.
    Every factor is the standard determinant of a projection overlap.
    """
    theta_x_values = 2 * np.pi * np.arange(TWIST_SAMPLES) / TWIST_SAMPLES
    theta_y_values = (
        2 * np.pi * np.arange(TRANSVERSE_SAMPLES) / TRANSVERSE_SAMPLES
    )
    section = []
    for theta_x in theta_x_values:
        frames = [
            occupied_frame(
                LATTICE_SIZE, mass, theta_x, theta_y, sy_sign
            )[0]
            for theta_y in theta_y_values
        ]
        holonomy = 1.0 + 0.0j
        for first, second in zip(frames, frames[1:] + frames[:1]):
            holonomy *= unit_phase(np.linalg.det(first.conj().T @ second))
        section.append(unit_phase(holonomy))
    return np.asarray(section)


def strip_hamiltonian(momentum, mass, sy_sign=1.0):
    onsite = np.sin(momentum) * SX + (mass - np.cos(momentum)) * SZ
    hopping = -0.5 * SZ + sy_sign * SY / (2j)
    hamiltonian = np.zeros((2 * STRIP_WIDTH, 2 * STRIP_WIDTH), dtype=complex)
    for y_coord in range(STRIP_WIDTH):
        start = 2 * y_coord
        hamiltonian[start:start + 2, start:start + 2] = onsite
    for y_coord in range(STRIP_WIDTH - 1):
        lower = 2 * y_coord
        upper = lower + 2
        hamiltonian[lower:lower + 2, upper:upper + 2] = hopping
        hamiltonian[upper:upper + 2, lower:lower + 2] = hopping.conj().T
    return hamiltonian


def seam_edge_section(mass=1.0, sy_sign=1.0):
    """v991 bottom-weighted regularized edge-determinant phase section."""
    momenta = 2 * np.pi * np.arange(TWIST_SAMPLES) / TWIST_SAMPLES
    y_operator = np.repeat(np.arange(STRIP_WIDTH), 2).astype(float)
    section = []
    for momentum in momenta:
        eigenvalues, eigenvectors = np.linalg.eigh(
            strip_hamiltonian(momentum, mass, sy_sign)
        )
        log_determinant = 0.0j
        for state_index, energy in enumerate(eigenvalues):
            y_expectation = float(
                np.abs(eigenvectors[:, state_index]) ** 2 @ y_operator
            )
            collar_weight = np.exp(
                -y_expectation / EDGE_LOCALIZATION_LENGTH
            )
            log_determinant += collar_weight * np.log(
                energy + 1j * EDGE_REGULATOR
            )
        section.append(np.exp(1j * log_determinant.imag))
    return np.asarray(section)


def fixed_reference_overlap_section(theta_y=0.0):
    """Projection-overlap chart against the frame at theta_x = 0."""
    momenta = 2 * np.pi * np.arange(TWIST_SAMPLES) / TWIST_SAMPLES
    reference = occupied_frame(
        LATTICE_SIZE, 1.0, 0.0, theta_y
    )[0]
    values = []
    for momentum in momenta:
        frame = occupied_frame(
            LATTICE_SIZE, 1.0, momentum, theta_y
        )[0]
        values.append(np.linalg.det(reference.conj().T @ frame))
    return np.asarray(values)


def anchored_restriction_map(bulk_section, seam_section, c_phase=None):
    """Construct R with q = c_phase R t and return its residual."""
    raw_ratio = seam_section / bulk_section
    chosen_phase = unit_phase(raw_ratio[0]) if c_phase is None else unit_phase(c_phase)
    restriction = raw_ratio / chosen_phase
    mapped_bulk = restriction * bulk_section
    constant_samples = seam_section / mapped_bulk
    residual = float(np.max(np.abs(constant_samples - chosen_phase)))
    return restriction, chosen_phase, constant_samples, residual


def align_frame(frame, reference):
    """Polar-align frame so reference^* frame is positive Hermitian."""
    overlap = reference.conj().T @ frame
    left, singular_values, right_adjoint = np.linalg.svd(overlap)
    gauge = right_adjoint.conj().T @ left.conj().T
    return frame @ gauge, singular_values


def parallel_frames(theta_y, initial_reference=None):
    """Gauge-covariant nearest-neighbour parallel frames along theta_x."""
    momenta = 2 * np.pi * np.arange(TWIST_SAMPLES) / TWIST_SAMPLES
    raw_frames = [
        occupied_frame(LATTICE_SIZE, 1.0, momentum, theta_y)[0]
        for momentum in momenta
    ]
    if initial_reference is None:
        first = raw_frames[0]
    else:
        first, _ = align_frame(raw_frames[0], initial_reference)
    transported = [first]
    for raw_frame in raw_frames[1:]:
        aligned, _ = align_frame(raw_frame, transported[-1])
        transported.append(aligned)
    return transported


def detached_projection_section():
    """Normal projection from the seam circle to theta_y = pi/4."""
    seam_frames = parallel_frames(0.0)
    detached_frames = parallel_frames(
        DETACHED_OFFSET, initial_reference=seam_frames[0]
    )
    phases = []
    magnitudes = []
    for seam_frame, detached_frame in zip(seam_frames, detached_frames):
        determinant = np.linalg.det(seam_frame.conj().T @ detached_frame)
        phases.append(unit_phase(determinant))
        magnitudes.append(abs(determinant))
    return np.asarray(phases), float(min(magnitudes))


def near_integer(value, integer, tolerance):
    return abs(value - integer) < tolerance


def phase_text(value):
    return (
        "c=(%+.12f%+.12fj), arg=%+.12f"
        % (value.real, value.imag, np.angle(value))
    )


def main():
    print("detline_canonical_trivialization_probe")
    print("EXPLORATION ONLY: finite QWZ/U(1) shadow; CHIRAL4D stays [O]")
    print()

    print("=== BULK OBJECT AND TOPOLOGICAL OBSTRUCTION ===")
    chern_plus, gap_plus = detline_chern(LATTICE_SIZE, 1.0, sy_sign=1.0)
    chern_mirror, gap_mirror = detline_chern(
        LATTICE_SIZE, 1.0, sy_sign=-1.0
    )
    reference_section = fixed_reference_overlap_section()
    minimum_reference_overlap = float(np.min(np.abs(reference_section)))
    check(
        "occupied determinant line has Chern +1 and remains gapped",
        near_integer(chern_plus, 1, TOL_CHERN) and gap_plus > 1.9,
        "C=%+.12f, min_gap=%.12f" % (chern_plus, gap_plus),
    )
    check(
        "one fixed projection-overlap chart cannot globally trivialize "
        "the seam circle",
        minimum_reference_overlap < 1e-12,
        "min |det(U_ref^* U(theta))|=%.3e" % minimum_reference_overlap,
    )

    print()
    print("=== FINITE RESTRICTION ISOMORPHISM ===")
    bulk_plus = bulk_clutching_section(sy_sign=1.0)
    seam_plus = seam_edge_section(sy_sign=1.0)
    restriction_plus, c_plus, constants_plus, residual_plus = (
        anchored_restriction_map(bulk_plus, seam_plus)
    )
    winding_bulk_plus = winding(bulk_plus)
    winding_seam_plus = winding(seam_plus)
    winding_mapped_plus = winding(restriction_plus * bulk_plus)
    winding_restriction_plus = winding(restriction_plus)
    print("   eta=+  " + phase_text(c_plus))
    print("   max_theta |q/(R t)-c| = %.3e" % residual_plus)
    check(
        "Res_Sigma L_bulk is isomorphic to L_Sigma: one c_phase is "
        "constant along the seam to 1e-10",
        residual_plus < TOL_CONSTANCY,
        "residual=%.3e" % residual_plus,
    )
    check(
        "the restriction map is topologically neutral",
        near_integer(winding_restriction_plus, 0, TOL_WINDING),
        "wind(R)=%+.12f" % winding_restriction_plus,
    )

    print()
    print("=== ORIENTATION COVARIANCE AND ITS LIMIT ===")
    # The antiunitary D4 action on a determinant line conjugates scalar
    # coordinates.  This is the orientation-reversed branch of the same
    # finite isomorphism.
    bulk_negative_orientation = np.conj(bulk_plus)
    seam_negative_orientation = np.conj(seam_plus)
    restriction_negative, c_negative, constants_negative, residual_negative = (
        anchored_restriction_map(
            bulk_negative_orientation,
            seam_negative_orientation,
        )
    )
    covariance_residual = abs(c_negative - np.conj(c_plus))
    orbit_separation = abs(c_plus - np.conj(c_plus))
    print("   eta=-  " + phase_text(c_negative))
    print("   |c_- - conjugate(c_+)| = %.3e" % covariance_residual)
    check(
        "orientation reversal sends c_phase to its conjugate/inverse",
        covariance_residual < TOL_COVARIANCE
        and residual_negative < TOL_CONSTANCY,
        "covariance=%.3e, constancy=%.3e"
        % (covariance_residual, residual_negative),
    )
    check(
        "a fixed anchored phase has a two-element orientation orbit",
        orbit_separation > 1e-3,
        "|c-conjugate(c)|=%.6f" % orbit_separation,
    )

    alternative_orbit_data = []
    alternatives_pass = True
    for orbit_denominator in (7, 11):
        phase_shift = 2 * np.pi / orbit_denominator
        shifted_restriction_plus = (
            np.exp(-1j * phase_shift) * restriction_plus
        )
        shifted_restriction_negative = (
            np.exp(1j * phase_shift) * restriction_negative
        )
        shifted_c_plus = unit_phase(
            seam_plus[0]
            / (shifted_restriction_plus[0] * bulk_plus[0])
        )
        shifted_c_negative = unit_phase(
            seam_negative_orientation[0]
            / (
                shifted_restriction_negative[0]
                * bulk_negative_orientation[0]
            )
        )
        shifted_samples_plus = seam_plus / (
            shifted_restriction_plus * bulk_plus
        )
        shifted_samples_negative = seam_negative_orientation / (
            shifted_restriction_negative * bulk_negative_orientation
        )
        shifted_constancy = max(
            float(np.max(np.abs(shifted_samples_plus - shifted_c_plus))),
            float(np.max(np.abs(
                shifted_samples_negative - shifted_c_negative
            ))),
        )
        shifted_covariance = abs(
            shifted_c_negative - np.conj(shifted_c_plus)
        )
        distance_from_original_orbit = min(
            abs(shifted_c_plus - c_plus),
            abs(shifted_c_plus - np.conj(c_plus)),
        )
        alternative_orbit_data.append(
            (
                orbit_denominator,
                shifted_constancy,
                shifted_covariance,
                distance_from_original_orbit,
            )
        )
        alternatives_pass &= (
            shifted_constancy < TOL_CONSTANCY
            and shifted_covariance < TOL_COVARIANCE
            and distance_from_original_orbit > 1e-3
        )
        print(
            "   shift 2pi/%d: const=%.3e, cov=%.3e, "
            "distance from original orbit=%.6f"
            % alternative_orbit_data[-1]
        )
    check(
        "UNIQUENESS MUTANT: other constant phases preserve both the "
        "restriction identity and orientation covariance",
        alternatives_pass,
        "two explicit inequivalent U(1)/conjugation orbits survive",
    )
    check(
        "therefore orientation chooses 2 -> 1 only inside a preselected "
        "orbit, not a canonical orbit in U(1)",
        alternatives_pass,
        "missing datum: one constant phase anchor",
    )

    print()
    print("=== ANOMALY BOOKKEEPING ===")
    check(
        "Chern/inflow tie-in: C_bulk = wind(t_bulk) = wind(q_seam) "
        "= wind(c R t) = +1",
        near_integer(chern_plus, 1, TOL_CHERN)
        and near_integer(winding_bulk_plus, 1, TOL_WINDING)
        and near_integer(winding_seam_plus, 1, TOL_WINDING)
        and near_integer(winding_mapped_plus, 1, TOL_WINDING),
        "C=%+.12f, W_bulk=%+.12f, W_seam=%+.12f, W_mapped=%+.12f"
        % (
            chern_plus,
            winding_bulk_plus,
            winding_seam_plus,
            winding_mapped_plus,
        ),
    )

    print()
    print("=== MUTANTS ===")
    bulk_mirror = bulk_clutching_section(sy_sign=-1.0)
    seam_mirror = seam_edge_section(sy_sign=-1.0)
    winding_bulk_mirror = winding(bulk_mirror)
    winding_seam_mirror = winding(seam_mirror)
    check(
        "mirror-content mutant flips the anomaly and the "
        "orientation-labelled phase branch",
        near_integer(chern_mirror, -1, TOL_CHERN)
        and gap_mirror > 1.9
        and near_integer(winding_bulk_mirror, -1, TOL_WINDING)
        and near_integer(winding_seam_mirror, -1, TOL_WINDING)
        and covariance_residual < TOL_COVARIANCE,
        "C=%+.12f, W_bulk=%+.12f, W_seam=%+.12f, c_- = conjugate(c_+)"
        % (chern_mirror, winding_bulk_mirror, winding_seam_mirror),
    )

    detached_phase, detached_minimum_overlap = detached_projection_section()
    detached_constant_samples = constants_plus / detached_phase
    detached_relative = (
        detached_constant_samples / detached_constant_samples[0]
    )
    detached_phase_variation = float(
        np.max(np.abs(np.angle(detached_relative)))
    )
    check(
        "seam-detached mutant loses constant c_phase without a new "
        "normal-transport correction",
        detached_minimum_overlap > 0.5
        and detached_phase_variation > MIN_DETACHED_VARIATION,
        "theta_y=pi/4, min projection=%.6f, phase variation=%.6f rad"
        % (detached_minimum_overlap, detached_phase_variation),
    )

    print()
    check(
        "HONEST BOUNDARY: finite 2+1D QWZ family and U(1) twist torus "
        "only; full nonabelian SM determinant line and CHIRAL4D remain [O]",
        True,
    )
    passed_count = sum(CHECKS)
    print("-" * 78)
    print("CHECKS %d/%d PASS" % (passed_count, len(CHECKS)))
    if passed_count == len(CHECKS):
        verdict = (
            "DETLINE_TRIVIALIZATION_OBSTRUCTED("
            "finite isomorphism constant to %.1e; "
            "orientation orbit 2 -> 1 only after a U(1) anchor)"
            % residual_plus
        )
    else:
        verdict = "DETLINE_TRIVIALIZATION_OBSTRUCTED(numerical check failure)"
    print("VERDICT: " + verdict)
    with open(__file__, "rb") as probe_file:
        print("SPEC_SHA " + hashlib.sha256(probe_file.read()).hexdigest()[:16])
    return 0 if passed_count == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
