#!/usr/bin/env python3
r"""spin2_hamiltonian_lattice_probe -- EXPLORATION ONLY.

Model and scope
---------------
This probe takes the simplest honest Hamiltonian-first route to the quadratic
graviton: linearized ADM gravity on a unit-spacing, periodic N^3 spatial
lattice, N=6,...,12.  At every nonzero lattice momentum

    q_i(k) = 2 sin(k_i/2),       k_i = 2 pi n_i/N in [-pi,pi),

the six components of a symmetric spatial tensor are split by the exact
lattice transverse tensor theta_ij=delta_ij-q_i q_j/q^2 into

    Sym^2(R^3) = TT(2) + transverse-vector(2)
                      + transverse-scalar(1) + longitudinal-scalar(1).

The physical Hamiltonian is the Dirac-reduced linearized ADM Hamiltonian

    H_q = 1/2 [pi_TT:pi_TT + q^2 h_TT:h_TT].

It is not a claimed derivation from the TFPT spectral action.  It is the
standard free graviton Hamiltonian after imposing the linearized Hamiltonian
and momentum constraints and quotienting their gauge orbits.  Full h_ij and
pi_ij are retained below so the reduction is checked rather than hidden:

    C_H(h) = q_i q_j h_ij - q^2 tr(h) = 0,
    C_M,i(pi) = q_j pi_ij = 0,
    delta h_ij = q_i xi_j + q_j xi_i,
    delta pi_ij = alpha (q_i q_j - q^2 delta_ij).

Thus C_H removes the transverse scalar, spatial gauge removes the vector plus
longitudinal scalar, C_M removes the momentum vector plus longitudinal scalar,
and Hamiltonian gauge removes the remaining momentum transverse scalar.  The
quotient has two canonical polarizations.

The half-link symbol q_i=2 sin(k_i/2), rather than the central-difference
symbol sin(k_i), is deliberate: it is the modulus (with a harmless translated
phase) of the nearest-neighbour forward difference and has no spurious zeros
at Brillouin-zone boundaries.  The sole exceptional momentum is k=0, where a
direction-dependent helicity projector is undefined; that homogeneous torus
mode is tabulated but is not counted as a propagating local graviton.

Executable claims
-----------------
* The exact reduced phase-space Hessian has spectrum
  {0 x 8, q^2 x 2, 1 x 2}, hence H is positive semidefinite on the
  constrained/gauge-quotiented system.  Every nonzero mode for N=6,...,12 is
  also diagonalized numerically.
* The exact lattice TT projector has rank two at every nonzero grid momentum,
  including Brillouin-zone boundary modes.
* omega(k)=|q(k)| is gapless.  Along an axis,
  omega=2 sin(k/2)=k-k^3/24+O(k^5), so c=1.
* The four non-TT tensor directions are exhausted exactly by the
  vector/scalar constraint-and-gauge sectors.
* A positive mass term gaps omega, while a wrong-sign pi_TT kinetic term gives
  two negative phase-space directions per nonzero momentum.

Bridge (typed; no status move)
------------------------------
The verdict SPIN2_HAMILTONIAN_QUADRATIC_EXECUTED executes only the QUADRATIC
Hamiltonian half of GRAV.SPIN2.EMERGENCE.01 on the lattice-fundamental route:
positive H and two gapless TT helicities are true by construction and checked
here.  Still [O] are (i) deriving this Hessian from the corpus spectral action,
with the frozen M_eff/Lambda=2.5537329354 only a scale input, (ii) the nonlinear
constraint algebra/diffeomorphism Ward identities, and (iii) universal matter
coupling.  No paper, ledger, verification, scorecard, or website status follows
from this exploration-only probe.
"""

import itertools
import sys

import numpy as np
import sympy as sp


LATTICE_SIZES = tuple(range(6, 13))
TOL = 2.0e-10
RANK_TOL = 1.0e-9
MASS_MUTANT = 0.4
FROZEN_M_EFF_OVER_LAMBDA = 2.5537329354
CHECKS = []


def check(name, condition, detail):
    """Record one deterministic executable assertion."""
    passed = bool(condition)
    CHECKS.append(passed)
    print("  [%s] %-38s %s" % (
        "PASS" if passed else "FAIL", name, detail))
    return passed


def symmetric_basis_numpy():
    """Frobenius-orthonormal basis of real symmetric 3x3 tensors."""
    basis = []
    for left in range(3):
        for right in range(left, 3):
            tensor = np.zeros((3, 3))
            if left == right:
                tensor[left, right] = 1.0
            else:
                tensor[left, right] = 1.0 / np.sqrt(2.0)
                tensor[right, left] = 1.0 / np.sqrt(2.0)
            basis.append(tensor)
    return basis


def symmetric_basis_sympy():
    """Exact counterpart of symmetric_basis_numpy."""
    basis = []
    for left in range(3):
        for right in range(left, 3):
            tensor = sp.zeros(3)
            if left == right:
                tensor[left, right] = 1
            else:
                tensor[left, right] = 1 / sp.sqrt(2)
                tensor[right, left] = 1 / sp.sqrt(2)
            basis.append(tensor)
    return basis


NUMERIC_BASIS = symmetric_basis_numpy()
SYMBOLIC_BASIS = symmetric_basis_sympy()


def tensor_coordinates(tensor):
    """Coordinates in the orthonormal symmetric-tensor basis."""
    return np.array([np.sum(element * tensor) for element in NUMERIC_BASIS])


def projector_matrices(momentum):
    """Return the orthogonal TT/vector/two-scalar lattice projectors."""
    momentum = np.asarray(momentum, dtype=float)
    momentum_squared = float(momentum @ momentum)
    if momentum_squared == 0.0:
        raise ValueError("the TT projector is undefined at zero momentum")
    longitudinal = np.outer(momentum, momentum) / momentum_squared
    transverse = np.eye(3) - longitudinal

    def project(kind, tensor):
        if kind == "TT":
            transverse_trace = np.trace(transverse @ tensor)
            return (transverse @ tensor @ transverse
                    - 0.5 * transverse * transverse_trace)
        if kind == "V":
            return (transverse @ tensor @ longitudinal
                    + longitudinal @ tensor @ transverse)
        if kind == "ST":
            return 0.5 * transverse * np.trace(transverse @ tensor)
        if kind == "L":
            return longitudinal * np.trace(longitudinal @ tensor)
        raise ValueError(kind)

    matrices = {}
    for kind in ("TT", "V", "ST", "L"):
        matrices[kind] = np.array([
            [np.sum(left * project(kind, right))
             for right in NUMERIC_BASIS]
            for left in NUMERIC_BASIS
        ])
    return matrices


def symbolic_projector_matrices():
    """Exact projectors for a representative nonzero momentum q along z."""
    longitudinal = sp.diag(0, 0, 1)
    transverse = sp.eye(3) - longitudinal

    def inner(left, right):
        return sp.simplify(sum(
            left[i, j] * right[i, j]
            for i in range(3) for j in range(3)
        ))

    def project(kind, tensor):
        if kind == "TT":
            transverse_trace = sp.trace(transverse * tensor)
            return sp.simplify(
                transverse * tensor * transverse
                - transverse * transverse_trace / 2)
        if kind == "V":
            return sp.simplify(
                transverse * tensor * longitudinal
                + longitudinal * tensor * transverse)
        if kind == "ST":
            return sp.simplify(
                transverse * sp.trace(transverse * tensor) / 2)
        if kind == "L":
            return sp.simplify(
                longitudinal * sp.trace(longitudinal * tensor))
        raise ValueError(kind)

    return {
        kind: sp.Matrix([
            [inner(left, project(kind, right))
             for right in SYMBOLIC_BASIS]
            for left in SYMBOLIC_BASIS
        ])
        for kind in ("TT", "V", "ST", "L")
    }


def wrapped_wave_numbers(size):
    """Dimensionless periodic momenta in numpy's [-pi,pi) convention."""
    return 2.0 * np.pi * np.fft.fftfreq(size)


def constraint_and_gauge_data(momentum):
    """Ranks/inclusions for the four linearized ADM first-class directions."""
    momentum = np.asarray(momentum, dtype=float)
    norm = float(np.linalg.norm(momentum))
    unit = momentum / norm
    transverse = np.eye(3) - np.outer(unit, unit)

    # C_H/q^2 = (qhat qhat - I):h.  Normalization does not affect its rank.
    hamiltonian_constraint = tensor_coordinates(
        np.outer(unit, unit) - np.eye(3))[None, :]

    # Three spatial-diffeomorphism gauge columns delta h=qhat_(i xi_j).
    spatial_gauge = np.column_stack([
        tensor_coordinates(
            np.outer(unit, direction) + np.outer(direction, unit))
        for direction in np.eye(3)
    ])

    # C_M,i = qhat_j pi_ij.
    momentum_constraints = np.array([
        [float((basis @ unit)[component]) for basis in NUMERIC_BASIS]
        for component in range(3)
    ])

    # Hamiltonian-constraint gauge direction in momentum space.
    hamiltonian_gauge = tensor_coordinates(-transverse)[:, None]

    return {
        "rank_ch": np.linalg.matrix_rank(
            hamiltonian_constraint, tol=RANK_TOL),
        "rank_gh": np.linalg.matrix_rank(spatial_gauge, tol=RANK_TOL),
        "rank_cm": np.linalg.matrix_rank(
            momentum_constraints, tol=RANK_TOL),
        "rank_gp": np.linalg.matrix_rank(
            hamiltonian_gauge, tol=RANK_TOL),
        "h_gauge_in_constraint": float(np.max(np.abs(
            hamiltonian_constraint @ spatial_gauge))),
        "p_gauge_in_constraint": float(np.max(np.abs(
            momentum_constraints @ hamiltonian_gauge))),
    }


def main():
    print("=" * 96)
    print("spin2_hamiltonian_lattice_probe -- Hamiltonian-first free graviton")
    print("EXPLORATION ONLY; quadratic lattice witness, no contract status move")
    print("=" * 96)

    symbolic_projectors = symbolic_projector_matrices()
    symbolic_identity = sp.eye(6)
    symbolic_zero = sp.zeros(6)
    expected_ranks = {"TT": 2, "V": 2, "ST": 1, "L": 1}
    symbolic_algebra_ok = (
        all(projector * projector == projector
            for projector in symbolic_projectors.values())
        and all(
            symbolic_projectors[left] * symbolic_projectors[right]
            == symbolic_zero
            for left, right in itertools.permutations(
                symbolic_projectors, 2)
        )
        and sum(symbolic_projectors.values(), sp.zeros(6))
        == symbolic_identity
        and {
            name: int(projector.rank())
            for name, projector in symbolic_projectors.items()
        } == expected_ranks
    )
    check(
        "exact tensor-projector algebra",
        symbolic_algebra_ok,
        "P_a P_b=delta_ab P_a, sum P_a=I_6; ranks %s"
        % expected_ranks,
    )

    q_squared = sp.symbols("q_lat_sq", positive=True)
    physical_projector = symbolic_projectors["TT"]
    phase_hessian = sp.diag(
        q_squared * physical_projector, physical_projector)
    symbolic_spectrum = phase_hessian.eigenvals()
    expected_spectrum = {
        sp.Integer(0): 8,
        sp.Integer(1): 2,
        q_squared: 2,
    }
    check(
        "exact reduced-Hamiltonian spectrum",
        symbolic_spectrum == expected_spectrum,
        "spec(K_q)={0 x8, q_lat^2 x2, 1 x2}; H=1/2 X^T K_q X",
    )

    polarization_rows = []
    worst_projector_deviation = 0.0
    worst_negative_eigenvalue = 0.0
    smallest_positive_h_eigenvalue = np.inf
    largest_constraint_inclusion_error = 0.0
    all_numeric_ranks_ok = True
    all_numeric_spectra_ok = True
    all_constraint_counts_ok = True
    wrong_sign_minimum = np.inf
    wrong_sign_negative_counts = set()
    minimum_massive_frequency = np.inf

    for size in LATTICE_SIZES:
        wave_numbers = wrapped_wave_numbers(size)
        total_modes = size ** 3
        rank_two_modes = 0
        rank_exceptions = 0
        boundary_modes = 0

        for momentum_tuple in itertools.product(wave_numbers, repeat=3):
            continuum_momentum = np.array(momentum_tuple)
            if np.all(continuum_momentum == 0.0):
                continue

            if np.any(np.isclose(
                    np.abs(continuum_momentum), np.pi, atol=1.0e-14)):
                boundary_modes += 1

            lattice_momentum = 2.0 * np.sin(continuum_momentum / 2.0)
            lattice_norm_squared = float(
                lattice_momentum @ lattice_momentum)
            projectors = projector_matrices(lattice_momentum)
            ranks = {
                name: int(np.linalg.matrix_rank(
                    projector, tol=RANK_TOL))
                for name, projector in projectors.items()
            }
            if ranks["TT"] == 2:
                rank_two_modes += 1
            else:
                rank_exceptions += 1
            all_numeric_ranks_ok &= ranks == expected_ranks

            projector_sum = sum(projectors.values())
            worst_projector_deviation = max(
                worst_projector_deviation,
                float(np.max(np.abs(projector_sum - np.eye(6)))),
            )
            for left_name, left_projector in projectors.items():
                worst_projector_deviation = max(
                    worst_projector_deviation,
                    float(np.max(np.abs(
                        left_projector @ left_projector - left_projector))),
                )
                for right_name, right_projector in projectors.items():
                    if left_name != right_name:
                        worst_projector_deviation = max(
                            worst_projector_deviation,
                            float(np.max(np.abs(
                                left_projector @ right_projector))),
                        )

            tt_projector = projectors["TT"]
            numeric_hessian = np.block([
                [lattice_norm_squared * tt_projector, np.zeros((6, 6))],
                [np.zeros((6, 6)), tt_projector],
            ])
            hessian_eigenvalues = np.linalg.eigvalsh(numeric_hessian)
            positive_eigenvalues = hessian_eigenvalues[
                hessian_eigenvalues > RANK_TOL]
            all_numeric_spectra_ok &= (
                len(positive_eigenvalues) == 4
                and np.count_nonzero(
                    np.abs(hessian_eigenvalues) <= RANK_TOL) == 8
                and hessian_eigenvalues[0] >= -TOL
            )
            worst_negative_eigenvalue = min(
                worst_negative_eigenvalue, float(hessian_eigenvalues[0]))
            smallest_positive_h_eigenvalue = min(
                smallest_positive_h_eigenvalue,
                float(np.min(positive_eigenvalues)),
            )

            constraint_data = constraint_and_gauge_data(lattice_momentum)
            configuration_physical_dimension = (
                6 - constraint_data["rank_ch"]
                - constraint_data["rank_gh"])
            momentum_physical_dimension = (
                6 - constraint_data["rank_cm"]
                - constraint_data["rank_gp"])
            all_constraint_counts_ok &= (
                constraint_data["rank_ch"] == 1
                and constraint_data["rank_gh"] == 3
                and constraint_data["rank_cm"] == 3
                and constraint_data["rank_gp"] == 1
                and configuration_physical_dimension == 2
                and momentum_physical_dimension == 2
            )
            largest_constraint_inclusion_error = max(
                largest_constraint_inclusion_error,
                constraint_data["h_gauge_in_constraint"],
                constraint_data["p_gauge_in_constraint"],
            )

            massive_frequency = np.sqrt(
                lattice_norm_squared + MASS_MUTANT ** 2)
            minimum_massive_frequency = min(
                minimum_massive_frequency, massive_frequency)

            wrong_sign_hessian = np.block([
                [lattice_norm_squared * tt_projector, np.zeros((6, 6))],
                [np.zeros((6, 6)), -tt_projector],
            ])
            wrong_sign_eigenvalues = np.linalg.eigvalsh(
                wrong_sign_hessian)
            wrong_sign_minimum = min(
                wrong_sign_minimum, float(wrong_sign_eigenvalues[0]))
            wrong_sign_negative_counts.add(int(np.count_nonzero(
                wrong_sign_eigenvalues < -RANK_TOL)))

        polarization_rows.append({
            "size": size,
            "total": total_modes,
            "nonzero": total_modes - 1,
            "rank_two": rank_two_modes,
            "exceptions": rank_exceptions,
            "boundary": boundary_modes,
        })

    check(
        "all-grid projector ranks",
        all_numeric_ranks_ok
        and all(row["exceptions"] == 0 for row in polarization_rows),
        "N=6..12: TT/V/ST/L ranks 2/2/1/1 at every k != 0",
    )
    check(
        "all-grid projector algebra",
        worst_projector_deviation < TOL,
        "worst idempotence/orthogonality/completeness deviation %.3e"
        % worst_projector_deviation,
    )
    check(
        "all-mode Hamiltonian positivity",
        all_numeric_spectra_ok and worst_negative_eigenvalue >= -TOL,
        "all nonzero modes: 8 null + 4 positive phase directions; "
        "lambda_min=%.3e, smallest positive=%.12f"
        % (worst_negative_eigenvalue, smallest_positive_h_eigenvalue),
    )
    check(
        "constraint/gauge quotient count",
        all_constraint_counts_ok
        and largest_constraint_inclusion_error < TOL,
        "h:6-1(C_H)-3(gauge)=2; pi:6-3(C_M)-1(gauge)=2; "
        "max inclusion error %.3e" % largest_constraint_inclusion_error,
    )

    fit_momenta = np.array([
        2.0 * np.pi / size for size in LATTICE_SIZES])
    fit_frequencies = 2.0 * np.sin(fit_momenta / 2.0)
    fit_design = np.column_stack([
        fit_momenta,
        fit_momenta ** 3,
        fit_momenta ** 5,
        fit_momenta ** 7,
    ])
    fit_coefficients, _, _, _ = np.linalg.lstsq(
        fit_design, fit_frequencies, rcond=None)
    fitted_speed = float(fit_coefficients[0])
    fitted_cubic = float(fit_coefficients[1])
    exact_k = sp.symbols("k", positive=True)
    exact_dispersion_series = sp.series(
        2 * sp.sin(exact_k / 2), exact_k, 0, 6)
    exact_cubic = -1.0 / 24.0
    check(
        "gapless lattice dispersion",
        abs(fitted_speed - 1.0) < 2.0e-7
        and abs(fitted_cubic - exact_cubic) < 2.0e-6,
        "axis fit N=6..12: c=%.10f, a3=%.10f; exact a3=-1/24"
        % (fitted_speed, fitted_cubic),
    )
    check(
        "exact small-k expansion",
        exact_dispersion_series.removeO()
        == exact_k - exact_k ** 3 / 24 + exact_k ** 5 / 1920,
        "omega=2 sin(k/2)=k-k^3/24+k^5/1920+O(k^7)",
    )

    check(
        "mass-term mutant gaps TT",
        MASS_MUTANT > 0.0
        and minimum_massive_frequency > MASS_MUTANT,
        "omega_m=sqrt(q_lat^2+m^2), continuum gap m=%.3f; "
        "smallest sampled omega_m=%.12f" % (
            MASS_MUTANT, minimum_massive_frequency),
    )
    check(
        "wrong-sign kinetic mutant",
        wrong_sign_negative_counts == {2}
        and abs(wrong_sign_minimum + 1.0) < TOL,
        "two negative TT momentum directions per k != 0; "
        "global lambda_min=%.12f" % wrong_sign_minimum,
    )

    all_checks_pass = all(CHECKS)
    verdict = (
        "SPIN2_HAMILTONIAN_QUADRATIC_EXECUTED"
        if all_checks_pass
        else "SPIN2_HAMILTONIAN_QUADRATIC_FAILS"
    )

    print("\nPOLARIZATION COUNT TABLE")
    print("  N   total   k!=0   rank(P_TT)=2   exceptions   BZ-boundary tested")
    for row in polarization_rows:
        print(" %2d   %5d   %5d       %5d          %3d             %3d" % (
            row["size"], row["total"], row["nonzero"], row["rank_two"],
            row["exceptions"], row["boundary"]))
    print("  k=0: one homogeneous torus mode per grid; helicity projector "
          "undefined and excluded.")
    print("  BZ boundary: no extra exception with q_i=2 sin(k_i/2).")

    print("\nQUADRATIC HAMILTONIAN RESULT")
    print("  H_q          = 1/2 (||pi_TT||^2 + |q_lat|^2 ||h_TT||^2)")
    print("  exact spec   = {0 x8, |q_lat|^2 x2, 1 x2}")
    print("  dispersion   = omega=|q_lat|; fitted c=%.10f, a3=%.10f"
          % (fitted_speed, fitted_cubic))
    print("  exact axis   = omega=k-k^3/24+O(k^5)")
    print("  massive mut. = gap %.3f (smallest sampled omega %.12f)"
          % (MASS_MUTANT, minimum_massive_frequency))
    print("  sign mutant  = 2 negative directions/mode, lambda_min=%.12f"
          % wrong_sign_minimum)

    print("\nBRIDGE")
    print("  Executed: quadratic Hamiltonian witness with positive H and exactly")
    print("            two gapless TT helicities on the lattice-fundamental route.")
    print("  Frozen input only: M_eff/Lambda=%.10f (not used to derive H)."
          % FROZEN_M_EFF_OVER_LAMBDA)
    print("  Still [O]: spectral-action Hessian identification; nonlinear")
    print("             constraint algebra/diffeomorphism Ward identities;")
    print("             universal matter coupling.")
    print("\nVERDICT: %s" % verdict)
    print("CHECKS: %d/%d PASS" % (sum(CHECKS), len(CHECKS)))
    print("\nFIVE-SENTENCE CONCLUSION")
    print("1. The exact half-link lattice TT projector has rank two at every "
          "nonzero momentum for N=6 through 12.")
    print("2. The constrained and gauge-quotiented quadratic Hamiltonian is "
          "positive semidefinite with two canonical physical modes.")
    print("3. Their dispersion is gapless with c=1 and leading correction "
          "-k^3/24 along a lattice axis.")
    print("4. A mass term opens a gap while a wrong-sign kinetic term creates "
          "two negative-energy directions, so both controls fire.")
    print("5. The corpus-to-Hessian derivation, nonlinear Ward/constraint "
          "algebra, and universal matter coupling remain [O].")
    print("=" * 96)
    return 0 if (
        all_checks_pass
        and verdict == "SPIN2_HAMILTONIAN_QUADRATIC_EXECUTED"
    ) else 1


if __name__ == "__main__":
    sys.exit(main())
