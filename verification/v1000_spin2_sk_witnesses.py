"""v1000 -- GRAV.SPIN2.EMERGENCE.01 + FTRANSFER.SK.RHO0.01
[O updates: quadratic Hamiltonian half executed; SK mechanism executed].
Provenance: experiments/tfpt-discovery/spin2_hamiltonian_lattice_probe.py
+ sk_rho0_mechanism_probe.py (review wave 4, 2026-08-29).

THE POINT.  Two independent executed halves of two open contracts.

  GRAV.SPIN2.EMERGENCE.01 (quadratic Hamiltonian, lattice-fundamental):
  [E] positivity exact; 2 TT helicities at all 5852 nonzero momenta
      (N=6..12); omega = |q| with q_i = 2 sin(k_i/2); axis expansion
      omega = k - k^3/24 exact.  Spectrum {0 x8, q^2 x2, 1 x2}.
  Still [O]: spectral-action Hessian identification, nonlinear Ward,
      universal coupling.  Display stays [O].

  FTRANSFER.SK.RHO0.01 (finite SK / rho_0 mechanism):
  [N] KMS/FDT on the exact Bohr grid ~1e-17.
  [N] rho_0-dependence contrast ~3.5e-3 vs static ~1e-16.
  [C] saddle 5-fold degenerate; 3pi/5 unique in the chosen mu4 lift.
  Display stays [O]; no cosmological solve.

MUST-FAIL: mass term gaps TT; wrong-sign kinetic term gives 2 negative
directions; SK product-state contrast is O(1) relative to the KMS pulse.

HONEST SCOPE (firewall): quadratic free graviton on a periodic N^3
lattice; finite 96-dim 1+1D W[J] sector.  Neither contract closes.
Python-only / Wolfram mirror deferred.
"""
import itertools

import numpy as np
import sympy as sp
from scipy.linalg import expm

from tfpt_constants import check, summary, reset


def report(name, ok, extra=""):
    check(name if not extra else "%s -- %s" % (name, extra), ok)


LATTICE_SIZES = tuple(range(6, 13))
TOL = 2.0e-10
RANK_TOL = 1.0e-9
MASS_MUTANT = 0.4
FROZEN_M_EFF_OVER_LAMBDA = 2.5537329354
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


def run_spin2():
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
    report(
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
    report(
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

    report(
        "all-grid projector ranks",
        all_numeric_ranks_ok
        and all(row["exceptions"] == 0 for row in polarization_rows),
        "N=6..12: TT/V/ST/L ranks 2/2/1/1 at every k != 0",
    )
    report(
        "all-grid projector algebra",
        worst_projector_deviation < TOL,
        "worst idempotence/orthogonality/completeness deviation %.3e"
        % worst_projector_deviation,
    )
    report(
        "all-mode Hamiltonian positivity",
        all_numeric_spectra_ok and worst_negative_eigenvalue >= -TOL,
        "all nonzero modes: 8 null + 4 positive phase directions; "
        "lambda_min=%.3e, smallest positive=%.12f"
        % (worst_negative_eigenvalue, smallest_positive_h_eigenvalue),
    )
    report(
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
    report(
        "gapless lattice dispersion",
        abs(fitted_speed - 1.0) < 2.0e-7
        and abs(fitted_cubic - exact_cubic) < 2.0e-6,
        "axis fit N=6..12: c=%.10f, a3=%.10f; exact a3=-1/24"
        % (fitted_speed, fitted_cubic),
    )
    report(
        "exact small-k expansion",
        exact_dispersion_series.removeO()
        == exact_k - exact_k ** 3 / 24 + exact_k ** 5 / 1920,
        "omega=2 sin(k/2)=k-k^3/24+k^5/1920+O(k^7)",
    )

    report(
        "mass-term mutant gaps TT",
        MASS_MUTANT > 0.0
        and minimum_massive_frequency > MASS_MUTANT,
        "omega_m=sqrt(q_lat^2+m^2), continuum gap m=%.3f; "
        "smallest sampled omega_m=%.12f" % (
            MASS_MUTANT, minimum_massive_frequency),
    )
    report(
        "wrong-sign kinetic mutant",
        wrong_sign_negative_counts == {2}
        and abs(wrong_sign_minimum + 1.0) < TOL,
        "two negative TT momentum directions per k != 0; "
        "global lambda_min=%.12f" % wrong_sign_minimum,
    )


    n_nonzero = sum(row["nonzero"] for row in polarization_rows)
    report(
        "N=6..12 nonzero-momentum census is 5852",
        n_nonzero == 5852
        and all(row["rank_two"] == row["nonzero"] for row in polarization_rows),
        "nonzero=%d; every mode has rank(P_TT)=2" % n_nonzero,
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

    
def run_sk():

    def report(name, condition, details=""):
        check(name if not details else "%s -- %s" % (name, details), condition)


    def max_abs(matrix):
        return float(np.max(np.abs(matrix)))


    def expectation(rho, operator):
        return complex(np.trace(rho @ operator))


    def unitary_from_hermitian(hamiltonian, duration):
        """Exact dense finite-dimensional unitary via Hermitian diagonalisation."""
        eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
        phases = np.exp(-1j * duration * eigenvalues)
        return (eigenvectors * phases) @ eigenvectors.conj().T


    # ---------------------------------------------------------------------------
    # Reused W[J]-sector Hamiltonian: Z6 link x four JW modes = 6 x 16 = 96.
    # ---------------------------------------------------------------------------
    NUMBER_OF_SITES = 2
    LINK_DIMENSION = 6
    SPECIES_CHARGES = (1, 0)  # Q and e^c, i.e. 6Y mod 6
    NUMBER_OF_MODES = 4
    FERMION_DIMENSION = 2**NUMBER_OF_MODES
    HILBERT_DIMENSION = LINK_DIMENSION * FERMION_DIMENSION

    OMEGA = np.exp(2j * np.pi / LINK_DIMENSION)
    Z_LINK_SMALL = np.diag(OMEGA ** np.arange(LINK_DIMENSION)).astype(complex)
    X_LINK_SMALL = np.roll(
        np.eye(LINK_DIMENSION, dtype=complex), 1, axis=0
    )
    SIGMA_Z = np.diag([1.0, -1.0]).astype(complex)
    ANNIHILATION = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)

    ELECTRIC_COUPLING = 1.0
    HOPPING_COUPLING = 0.7
    STAGGERED_MASS = 0.5
    Q_CHEMICAL_OFFSET = 0.5
    BETA = 0.35
    REFERENCE_THETA = 0.7


    def jordan_wigner_annihilator(mode):
        factors = []
        for index in range(NUMBER_OF_MODES):
            if index < mode:
                factors.append(SIGMA_Z)
            elif index == mode:
                factors.append(ANNIHILATION)
            else:
                factors.append(np.eye(2, dtype=complex))
        result = factors[0]
        for factor in factors[1:]:
            result = np.kron(result, factor)
        return np.kron(np.eye(LINK_DIMENSION, dtype=complex), result)


    def lift_link(operator):
        return np.kron(operator, np.eye(FERMION_DIMENSION, dtype=complex))


    PSI = [jordan_wigner_annihilator(mode) for mode in range(NUMBER_OF_MODES)]
    NUMBER = [operator.conj().T @ operator for operator in PSI]
    X_LINK = lift_link(X_LINK_SMALL)
    Z_LINK = lift_link(Z_LINK_SMALL)


    def build_hamiltonian(theta):
        """Hamiltonian copied from the earlier finite W[J] sector."""
        hamiltonian = -ELECTRIC_COUPLING * (X_LINK + X_LINK.conj().T)
        for species, charge in enumerate(SPECIES_CHARGES):
            mode_0 = species * NUMBER_OF_SITES
            mode_1 = mode_0 + 1
            z_charge = np.linalg.matrix_power(Z_LINK, charge)
            open_hop = PSI[mode_0].conj().T @ z_charge @ PSI[mode_1]
            seam_hop = (
                np.exp(1j * charge * theta)
                * PSI[mode_1].conj().T
                @ PSI[mode_0]
            )
            hamiltonian += HOPPING_COUPLING * (
                open_hop + open_hop.conj().T
                + seam_hop + seam_hop.conj().T
            )
            hamiltonian += STAGGERED_MASS * (
                NUMBER[mode_0] - NUMBER[mode_1]
            )
        hamiltonian += Q_CHEMICAL_OFFSET * (NUMBER[0] + NUMBER[1])
        return 0.5 * (hamiltonian + hamiltonian.conj().T)


    def seam_derivative(theta):
        """dH/dtheta for the charged Q seam; e^c is theta-blind."""
        phase = np.exp(1j * theta)
        directed_hop = PSI[1].conj().T @ PSI[0]
        derivative = 1j * phase * directed_hop
        return HOPPING_COUPLING * (derivative + derivative.conj().T)


    HAMILTONIAN = build_hamiltonian(REFERENCE_THETA)
    Q_CHARGE = NUMBER[0] + NUMBER[1]
    Q_STAGGERED = NUMBER[0] - NUMBER[1]
    LINK_COSINE = 0.5 * (Z_LINK + Z_LINK.conj().T)
    CONTROL_CHARGE = NUMBER[2] + NUMBER[3]
    CURRENT = -seam_derivative(REFERENCE_THETA)
    W_OBSERVABLES = (
        ("Q-charge", Q_CHARGE),
        ("link (Z+Zdag)/2", LINK_COSINE),
        ("e^c-charge CONTROL", CONTROL_CHARGE),
    )

    hermiticity_error = max_abs(HAMILTONIAN - HAMILTONIAN.conj().T)
    report(
        "finite candidate Hamiltonian is Hermitian",
        hermiticity_error < 1e-13,
        "dim=%d, maxdev=%.1e" % (HILBERT_DIMENSION, hermiticity_error),
    )


    def thermal_state(hamiltonian):
        eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
        shifted = -BETA * eigenvalues
        weights = np.exp(shifted - np.max(shifted))
        probabilities = weights / np.sum(weights)
        rho = (eigenvectors * probabilities) @ eigenvectors.conj().T
        return rho, eigenvalues, eigenvectors, probabilities


    RHO_KMS, ENERGIES, ENERGY_VECTORS, KMS_PROBABILITIES = thermal_state(HAMILTONIAN)


    def product_density_from_kms_marginals():
        """Decorrelated quench state with KMS one-mode number marginals.

        The link is the pure flux state |0><0|.  Each fermion mode has the
        same occupation probability as in rho_KMS, but every inter-mode and
        link-fermion correlation is removed.
        """
        link_density = np.zeros((LINK_DIMENSION, LINK_DIMENSION), dtype=complex)
        link_density[0, 0] = 1.0
        fermion_density = np.array([[1.0]], dtype=complex)
        occupations = []
        for number_operator in NUMBER:
            occupation = expectation(RHO_KMS, number_operator).real
            occupations.append(occupation)
            local_density = np.diag([1.0 - occupation, occupation]).astype(complex)
            fermion_density = np.kron(fermion_density, local_density)
        return np.kron(link_density, fermion_density), occupations


    RHO_PRODUCT, MATCHED_OCCUPATIONS = product_density_from_kms_marginals()
    for state_name, density in (("KMS", RHO_KMS), ("product", RHO_PRODUCT)):
        report(
            "%s rho_0 is normalized positive" % state_name,
            abs(np.trace(density) - 1.0) < 1e-13
            and np.linalg.eigvalsh(density).min() > -1e-13,
            "Tr=%.15f, lambda_min=%.2e"
            % (np.trace(density).real, np.linalg.eigvalsh(density).min()),
        )


    # ---------------------------------------------------------------------------
    # 1. Finite SK functional and equal-branch identities.
    # ---------------------------------------------------------------------------
    SOURCE_DURATION = 0.8


    def source_unitary(source):
        return unitary_from_hermitian(
            HAMILTONIAN - source * Q_STAGGERED, SOURCE_DURATION
        )


    def sk_functional(source_plus, source_minus, rho):
        u_plus = source_unitary(source_plus)
        u_minus = source_unitary(source_minus)
        return complex(np.trace(rho @ u_plus.conj().T @ u_minus))


    def sk_insertion(source_plus, source_minus, rho, operator):
        u_plus = source_unitary(source_plus)
        u_minus = source_unitary(source_minus)
        numerator = np.trace(rho @ u_plus.conj().T @ operator @ u_minus)
        return complex(numerator / sk_functional(source_plus, source_minus, rho))


    print("\n=== finite Schwinger--Keldysh functional ===")
    for state_name, density in (("KMS", RHO_KMS), ("product", RHO_PRODUCT)):
        diagonal_value = sk_functional(0.11, 0.11, density)
        zero_value = sk_functional(0.0, 0.0, density)
        forward_value = sk_functional(0.13, -0.07, density)
        reverse_value = sk_functional(-0.07, 0.13, density)
        report(
            "SK unitarity/closure for %s rho_0" % state_name,
            abs(diagonal_value - 1.0) < 2e-13
            and abs(zero_value - 1.0) < 2e-13
            and abs(reverse_value - forward_value.conjugate()) < 2e-13,
            "Z[J,J]=%.12f%+.1ei, Z[.13,-.07]=%.8f%+.8fi"
            % (
                diagonal_value.real,
                diagonal_value.imag,
                forward_value.real,
                forward_value.imag,
            ),
        )


    # ---------------------------------------------------------------------------
    # 1b. Exact finite KMS/FDT anchor on the unbroadened Bohr grid.
    # ---------------------------------------------------------------------------
    print("\n=== KMS/FDT anchor: exact finite Bohr-frequency grid ===")
    OBSERVABLE_ENERGY_BASIS = (
        ENERGY_VECTORS.conj().T @ Q_STAGGERED @ ENERGY_VECTORS
    )
    kms_absolute_error = 0.0
    kms_relative_error = 0.0
    fdt_absolute_error = 0.0
    fdt_relative_error = 0.0
    active_lines = 0
    nonzero_fdt_lines = 0
    representative = None

    for initial in range(HILBERT_DIMENSION):
        for final in range(HILBERT_DIMENSION):
            matrix_weight = abs(OBSERVABLE_ENERGY_BASIS[initial, final]) ** 2
            if matrix_weight < 1e-14:
                continue
            frequency = ENERGIES[final] - ENERGIES[initial]
            greater = KMS_PROBABILITIES[initial] * matrix_weight
            lesser = KMS_PROBABILITIES[final] * matrix_weight
            kms_rhs = np.exp(-BETA * frequency) * greater
            kms_error = abs(lesser - kms_rhs)
            kms_scale = max(abs(lesser), abs(kms_rhs), 1e-300)
            kms_absolute_error = max(kms_absolute_error, kms_error)
            kms_relative_error = max(kms_relative_error, kms_error / kms_scale)
            active_lines += 1

            if abs(frequency) > 1e-9 and abs(greater - lesser) > 1e-18:
                symmetric = 0.5 * (greater + lesser)
                dissipative = 0.5 * (greater - lesser)
                fdt_rhs = dissipative / np.tanh(0.5 * BETA * frequency)
                fdt_error = abs(symmetric - fdt_rhs)
                fdt_scale = max(abs(symmetric), abs(fdt_rhs), 1e-300)
                fdt_absolute_error = max(fdt_absolute_error, fdt_error)
                fdt_relative_error = max(fdt_relative_error, fdt_error / fdt_scale)
                nonzero_fdt_lines += 1
                if representative is None or greater > representative[1]:
                    representative = (frequency, greater, lesser, symmetric, fdt_rhs)

    report(
        "KMS detailed balance C<(w)=exp(-beta*w) C>(w)",
        kms_absolute_error < 2e-15 and kms_relative_error < 2e-12,
        "%d active lines, maxabs=%.2e, maxrel=%.2e"
        % (active_lines, kms_absolute_error, kms_relative_error),
    )
    report(
        "FDT S_sym(w)=coth(beta*w/2) rho(w)/2",
        fdt_absolute_error < 2e-15 and fdt_relative_error < 2e-12,
        "%d nonzero lines, maxabs=%.2e, maxrel=%.2e"
        % (
            nonzero_fdt_lines,
            fdt_absolute_error,
            fdt_relative_error,
        ),
    )
    if representative is not None:
        print(
            "ANCHOR representative: w=%+.9f  C>=%.9e  C<=%.9e  "
            "S_sym=%.9e  FDT_rhs=%.9e"
            % representative
        )


    # ---------------------------------------------------------------------------
    # 1b continued. Cross-anchor to the earlier finite W[J].
    # ---------------------------------------------------------------------------
    def log_trace_exp(hermitian):
        eigenvalues = np.linalg.eigvalsh(hermitian)
        maximum = float(eigenvalues.max())
        return maximum + float(np.log(np.sum(np.exp(eigenvalues - maximum))))


    def generating_function(source, operator):
        return log_trace_exp(-BETA * HAMILTONIAN + source * operator)


    print("\n=== equal-time SK <-> W[J] derivative cross-anchor ===")
    SOURCE_STEP = 1e-4
    cross_anchor_errors = []
    for observable_name, operator in W_OBSERVABLES:
        derivative = (
            generating_function(SOURCE_STEP, operator)
            - generating_function(-SOURCE_STEP, operator)
        ) / (2.0 * SOURCE_STEP)
        direct = expectation(RHO_KMS, operator).real
        sk_equal = sk_insertion(0.0, 0.0, RHO_KMS, operator).real
        error = max(abs(derivative - direct), abs(sk_equal - direct))
        cross_anchor_errors.append(error)
        print(
            "  %-22s W'=%.9f  thermal=%.9f  SK_equal=%.9f  maxdiff=%.2e"
            % (observable_name, derivative, direct, sk_equal, error)
        )
    report(
        "equal-time SK observables reproduce W[J] first derivatives",
        max(cross_anchor_errors) < 1e-6,
        "maxdiff=%.2e" % max(cross_anchor_errors),
    )

    # For the conserved Q charge, the W Hessian is the equal-time connected
    # variance (the Kubo/equal-time distinction vanishes because [H,N_Q]=0).
    w_zero = generating_function(0.0, Q_CHARGE)
    w_hessian = (
        generating_function(SOURCE_STEP, Q_CHARGE)
        - 2.0 * w_zero
        + generating_function(-SOURCE_STEP, Q_CHARGE)
    ) / SOURCE_STEP**2
    q_mean = expectation(RHO_KMS, Q_CHARGE)
    q_variance = expectation(RHO_KMS, Q_CHARGE @ Q_CHARGE) - q_mean * q_mean
    report(
        "W[J] Hessian matches equal-time connected Q fluctuation",
        abs(w_hessian - q_variance.real) < 2e-6,
        "W''=%.9f, variance=%.9f, diff=%.2e"
        % (w_hessian, q_variance.real, abs(w_hessian - q_variance.real)),
    )


    # ---------------------------------------------------------------------------
    # 1c. Nonequilibrium discriminator: exact rectangular seam-phase pulse.
    # ---------------------------------------------------------------------------
    print("\n=== rho_0 discriminator: CP-odd-like seam phase pulse ===")
    PULSE_AMPLITUDE = 0.18
    PULSE_DURATION = 0.45
    OBSERVATION_TIMES = np.linspace(0.0, 12.0, 97)
    PULSE_HAMILTONIAN = build_hamiltonian(REFERENCE_THETA + PULSE_AMPLITUDE)
    PULSE_UNITARY = unitary_from_hermitian(PULSE_HAMILTONIAN, PULSE_DURATION)


    def pulse_response(rho):
        """Induced current: pulsed history minus unpulsed history."""
        induced = []
        unpulsed_current = []
        q_values = []
        control_values = []
        for time_after_pulse in OBSERVATION_TIMES:
            free_after = unitary_from_hermitian(HAMILTONIAN, time_after_pulse)
            pulsed_evolution = free_after @ PULSE_UNITARY
            baseline_evolution = unitary_from_hermitian(
                HAMILTONIAN, time_after_pulse + PULSE_DURATION
            )
            pulsed_density = pulsed_evolution @ rho @ pulsed_evolution.conj().T
            baseline_density = (
                baseline_evolution @ rho @ baseline_evolution.conj().T
            )
            pulsed_current = expectation(pulsed_density, CURRENT).real
            baseline_current = expectation(baseline_density, CURRENT).real
            induced.append(pulsed_current - baseline_current)
            unpulsed_current.append(baseline_current)
            q_values.append(expectation(baseline_density, Q_CHARGE).real)
            control_values.append(expectation(baseline_density, CONTROL_CHARGE).real)
        return (
            np.asarray(induced),
            np.asarray(unpulsed_current),
            np.asarray(q_values),
            np.asarray(control_values),
        )


    kms_response = pulse_response(RHO_KMS)
    product_response = pulse_response(RHO_PRODUCT)
    kms_induced = kms_response[0]
    product_induced = product_response[0]


    def response_numbers(response):
        peak_index = int(np.argmax(np.abs(response)))
        peak = float(response[peak_index])
        rms = float(np.sqrt(np.mean(response**2)))
        signed_average = float(np.mean(response))
        return peak, float(OBSERVATION_TIMES[peak_index]), rms, signed_average


    kms_numbers = response_numbers(kms_induced)
    product_numbers = response_numbers(product_induced)
    trace_difference_rms = float(
        np.sqrt(np.mean((kms_induced - product_induced) ** 2))
    )
    print(
        "  KMS:     peak=%+.9e at t=%.3f  RMS=%.9e  mean=%+.9e"
        % kms_numbers
    )
    print(
        "  product: peak=%+.9e at t=%.3f  RMS=%.9e  mean=%+.9e"
        % product_numbers
    )
    print("  response-trace RMS contrast = %.9e" % trace_difference_rms)
    report(
        "induced asymmetry depends measurably on rho_0",
        abs(kms_numbers[2] - product_numbers[2]) > 1e-5
        and trace_difference_rms > 1e-4,
        "|RMS_KMS-RMS_product|=%.3e, trace contrast=%.3e"
        % (abs(kms_numbers[2] - product_numbers[2]), trace_difference_rms),
    )

    # The pulse and H conserve each species number.  The product state was
    # deliberately matched to the KMS one-mode occupancies, so these static
    # charge readouts agree not merely in long-time average but at every sampled
    # time.  The Hamiltonian spectrum/gaps are state-independent by construction.
    q_average_difference = abs(
        np.mean(kms_response[2]) - np.mean(product_response[2])
    )
    control_average_difference = abs(
        np.mean(kms_response[3]) - np.mean(product_response[3])
    )
    q_drift = max(
        np.ptp(kms_response[2]),
        np.ptp(product_response[2]),
    )
    control_drift = max(
        np.ptp(kms_response[3]),
        np.ptp(product_response[3]),
    )
    sorted_energies = np.sort(ENERGIES)
    positive_gaps = np.diff(sorted_energies)
    positive_gaps = positive_gaps[positive_gaps > 1e-10]
    spectral_gap = float(positive_gaps.min())
    print(
        "  equilibrium/static anchors: <N_Q>_KMS=%.9f, <N_Q>_product=%.9f; "
        "<N_e>_KMS=%.9f, <N_e>_product=%.9f; spectral gap=%.9f"
        % (
            expectation(RHO_KMS, Q_CHARGE).real,
            expectation(RHO_PRODUCT, Q_CHARGE).real,
            expectation(RHO_KMS, CONTROL_CHARGE).real,
            expectation(RHO_PRODUCT, CONTROL_CHARGE).real,
            spectral_gap,
        )
    )
    report(
        "matched conserved static readouts agree in long-time average",
        q_average_difference < 2e-13
        and control_average_difference < 2e-13
        and q_drift < 2e-13
        and control_drift < 2e-13,
        "d<N_Q>=%.2e, d<N_e>=%.2e, max drift=%.2e"
        % (
            q_average_difference,
            control_average_difference,
            max(q_drift, control_drift),
        ),
    )


    # ---------------------------------------------------------------------------
    # 2. Exact saddle enumeration and honest mu4-orientation typing.
    # ---------------------------------------------------------------------------
    print("\n=== exact initial-angle saddle classification ===")
    theta = sp.symbols("theta", real=True)
    kappa = sp.symbols("kappa", positive=True)
    s_initial = -kappa * sp.cos(5 * theta - 3 * sp.pi)
    first_derivative = sp.diff(s_initial, theta)
    second_derivative = sp.diff(first_derivative, theta)

    # theta=(3+n)pi/5 in [0,2pi): n=-3,...,6, equivalently theta=j*pi/5.
    saddles = []
    print("  theta/pi   n   S/kappa   S''/(25 kappa)   class")
    for j in range(10):
        theta_j = sp.Rational(j, 5) * sp.pi
        n = j - 3
        action_ratio = sp.simplify(s_initial.subs(theta, theta_j) / kappa)
        curvature_ratio = sp.simplify(
            second_derivative.subs(theta, theta_j) / (25 * kappa)
        )
        classification = "MIN" if curvature_ratio == 1 else "MAX"
        saddles.append((sp.Rational(j, 5), n, action_ratio, classification))
        print(
            "  %7s   %2d     %2s            %2s        %s"
            % (
                str(sp.Rational(j, 5)),
                n,
                str(action_ratio),
                str(curvature_ratio),
                classification,
            )
        )

    stationary_exact = all(
        sp.simplify(first_derivative.subs(theta, ratio * sp.pi)) == 0
        for ratio, _, _, _ in saddles
    )
    global_minima = [entry for entry in saddles if entry[3] == "MIN"]
    report(
        "stationary set theta=(3+n)pi/5 is complete on [0,2pi)",
        stationary_exact and len(saddles) == 10,
        "10 saddles: 5 minima and 5 maxima",
    )

    # A mu4 orientation quotient has angular width 2pi/4=pi/2.  The lift
    # centered at 3pi/5 is [3pi/5-pi/4, 3pi/5+pi/4)=[7pi/20,17pi/20).
    # S_init itself is not mu4-invariant, so choosing this lift is explicitly [C].
    domain_left = sp.Rational(7, 20)
    domain_right = sp.Rational(17, 20)
    domain_saddles = [
        entry for entry in saddles
        if domain_left <= entry[0] < domain_right
    ]
    domain_minima = [entry for entry in domain_saddles if entry[3] == "MIN"]
    mu4_shift_failure = sp.simplify(
        s_initial.subs(theta, theta + sp.pi / 2) - s_initial
    ) != 0
    target_ratio = sp.Rational(3, 5)
    report(
        "3pi/5 is unique minimum in chosen mu4 orientation lift [C]",
        len(domain_minima) == 1
        and domain_minima[0][0] == target_ratio
        and mu4_shift_failure,
        "domain=[7pi/20,17pi/20), saddles=%s; S_init not mu4-invariant"
        % [str(entry[0]) + "pi:" + entry[3] for entry in domain_saddles],
    )
    report(
        "global degeneracy is retained honestly",
        len(global_minima) == 5
        and [entry[0] for entry in global_minima]
        == [sp.Rational(j, 5) for j in (1, 3, 5, 7, 9)],
        "global minima=%s"
        % [str(entry[0]) + "pi" for entry in global_minima],
    )

    # Read-only corpus consistency anchor from v211_axion_spine_angle.py.
    number_of_families = sp.Integer(3)
    carrier_rank = sp.Integer(5)
    spine_angle = sp.pi * number_of_families / carrier_rank
    saddle_angle = target_ratio * sp.pi
    report(
        "saddle angle equals v211 spine quotient (consistency only)",
        sp.simplify(saddle_angle - spine_angle) == 0,
        "theta_i=3pi/5=pi*N_fam/g_car with N_fam=3, g_car=5",
    )


    # ---------------------------------------------------------------------------

def run():
    reset()
    print("v1000  GRAV.SPIN2.EMERGENCE.01 quadratic Hamiltonian + "
          "FTRANSFER.SK.RHO0.01 mechanism")
    run_spin2()
    run_sk()
    return summary(
        "v1000_spin2_sk_witnesses: 5852 momenta, 2 helicities, "
        "omega=k-k^3/24; KMS/FDT; rho_0 contrast; 3pi/5 [C] lift"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
