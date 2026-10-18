#!/usr/bin/env python3
"""quantum_band_os_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION.  Can the finite coupled collision band

    W_theta = U_int(theta) (x)_x V_x

be assigned the finite GKSL generator requested by the quantum
detailed-balance route, and can that generator split exactly into a
GNS-symmetric dissipator plus a Hamiltonian commutator?

NAMED-DEAD RESULT.  The premise fails before the interaction is tested.
With a fresh qutrit ancilla, the v977/v984 collision has Kraus operators

    K_a = |a><a| U_B,       Phi_0(rho) = sum_a K_a rho K_a^dag.

It has superoperator rank 3 on M_3: six coherence directions are erased
in one step.  On L cells the product channel has rank 3^L on the
9^L-dimensional operator space.  Post-composition by the unitary
U_int(theta) does not change that rank.  Hence Phi_theta is singular for
every theta, whereas exp(L) is invertible for every finite-dimensional
bounded generator L.  The requested channel logarithm/GKSL generator
therefore does not exist.

There is a second independent obstruction.  At theta = 0 the actual
quantum collision channel is D o Ad_{U_B}, not the classical
measure-and-prepare lift of B.  Although its diagonal restriction is the
symmetric positive B^(xL), it is not Hilbert-Schmidt/GNS symmetric with
respect to the maximally mixed state.  Even the always-defined
Poissonized fallback L_P = Phi - I has an anti-GNS part which is not a
Hamiltonian commutator.  Its least-squares Hamiltonian projection leaves
a nonzero residual already at theta = 0, so the required anchor
H_eff(0) = 0 and the exact reversible+dissipative split both fail.

The probe reports:
  * exact classical diagonal anchor B^(xL), CPTP/unitality, and ranks for
    L = 2, 3;
  * the nonzero theta = 0 GNS defect and the singular-log obstruction;
  * the closest Hamiltonian projection of the anti-GNS part at L = 2,
    its reconstruction residual, Hermiticity, symmetric-part spectrum,
    and small-theta scaling;
  * covariance defects for the natural qutrit mu4-character action
    Q = diag(1, i, -1);
  * a non-unitary contractive interaction mutant, which additionally
    breaks trace preservation and retains a nonzero splitting defect.

HONEST BOUNDARY.  Finite L = 2, 3 only.  This kills the proposed
``log(one-step reduced channel)`` route for the stated collision band;
it does not rule out a different weak-collision family V(dt) -> I, an
explicit Poisson clock with a redesigned detailed-balanced collision,
or an operator-algebraic thermodynamic-limit OS construction.  Those
remain [O].  No marker moves.

VERDICT ENUM: QUANTUM_OS_SPLITTING_BLOCKED_SINGULAR_COLLISION.
"""

from itertools import product

import numpy as np
import sympy as sp


ABS_TOL = 1.0e-10
RANK_TOL = 1.0e-9
DEFECT_TOL = 1.0e-8
THETAS = (0.0, 0.01, 0.02, 0.04, 0.08)
MUTANT_ETA = 0.2
LOCAL_DIM = 3
BF = np.array(
    [[13.0, 1.0, 4.0], [1.0, 13.0, 4.0], [4.0, 4.0, 10.0]]
) / 18.0

ok_all = True


def rep(name, ok, extra=""):
    """Print one executable check and accumulate the probe status."""
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


def build_lift():
    """Return the exact v977 unitary lift U_B as a NumPy array."""
    matrix_b = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]]) / 18
    sine_13_squared = sp.Rational(2, 9)
    cosine_13_squared = 1 - sine_13_squared
    sine_12_squared = sp.Rational(1, 14)
    sine_23_squared = sp.Rational(2, 7)
    cosine_12_squared = 1 - sine_12_squared
    cosine_23_squared = 1 - sine_23_squared
    sine_12, cosine_12 = sp.sqrt(sine_12_squared), sp.sqrt(cosine_12_squared)
    sine_23, cosine_23 = sp.sqrt(sine_23_squared), sp.sqrt(cosine_23_squared)
    sine_13, cosine_13 = sp.sqrt(sine_13_squared), sp.sqrt(cosine_13_squared)
    cross = 2 * sine_12 * cosine_12 * sine_23 * cosine_23 * sine_13
    cosine_delta = sp.simplify(
        (
            matrix_b[1, 0]
            - sine_12_squared * cosine_23_squared
            - cosine_12_squared * sine_23_squared * sine_13_squared
        )
        / cross
    )
    sine_delta = sp.sqrt(sp.simplify(1 - cosine_delta**2))
    phase_delta = cosine_delta + sp.I * sine_delta
    unitary = sp.Matrix(
        [
            [
                cosine_12 * cosine_13,
                sine_12 * cosine_13,
                sine_13 / phase_delta,
            ],
            [
                -sine_12 * cosine_23
                - cosine_12 * sine_23 * sine_13 * phase_delta,
                cosine_12 * cosine_23
                - sine_12 * sine_23 * sine_13 * phase_delta,
                sine_23 * cosine_13,
            ],
            [
                sine_12 * sine_23
                - cosine_12 * cosine_23 * sine_13 * phase_delta,
                -cosine_12 * sine_23
                - sine_12 * cosine_23 * sine_13 * phase_delta,
                cosine_23 * cosine_13,
            ],
        ]
    )
    return np.array(
        [
            [complex(sp.N(unitary[row, column], 20)) for column in range(3)]
            for row in range(3)
        ]
    )


def local_collision_kraus(unitary):
    """K_a = |a><a| U_B for a fresh |0> collision ancilla."""
    operators = []
    for outcome in range(LOCAL_DIM):
        operator = np.zeros((LOCAL_DIM, LOCAL_DIM), dtype=complex)
        operator[outcome, :] = unitary[outcome, :]
        operators.append(operator)
    return tuple(operators)


def kron_all(factors):
    """Kronecker product of a nonempty factor sequence."""
    result = np.array([[1.0]], dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def chain_collision_kraus(local_operators, length):
    """Tensor-product collision Kraus family on the system chain."""
    return tuple(
        kron_all([local_operators[index] for index in indices])
        for indices in product(range(LOCAL_DIM), repeat=length)
    )


def swap_ring_hamiltonian(length):
    """H_int = sum_x SWAP_{x,x+1} on the periodic qutrit chain."""
    dimension = LOCAL_DIM**length
    hamiltonian = np.zeros((dimension, dimension), dtype=float)
    for site in range(length):
        neighbour = (site + 1) % length
        for source in range(dimension):
            digits = []
            remainder = source
            for _ in range(length):
                digits.append(remainder % LOCAL_DIM)
                remainder //= LOCAL_DIM
            digits = digits[::-1]
            target_digits = digits[:]
            target_digits[site], target_digits[neighbour] = (
                target_digits[neighbour],
                target_digits[site],
            )
            target = 0
            for digit in target_digits:
                target = LOCAL_DIM * target + digit
            hamiltonian[target, source] += 1.0
    return hamiltonian


def interaction_unitary(length, theta):
    """U_int(theta) from the Hermitian SWAP-ring Hamiltonian."""
    hamiltonian = swap_ring_hamiltonian(length)
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    return (
        eigenvectors
        @ np.diag(np.exp(-1.0j * theta * eigenvalues))
        @ eigenvectors.conj().T
    )


def channel_superoperator(kraus_operators, left_layer):
    """Column-vectorized superoperator for J_a = left_layer K_a."""
    dimension = left_layer.shape[0]
    superoperator = np.zeros((dimension**2, dimension**2), dtype=complex)
    for operator in kraus_operators:
        dressed = left_layer @ operator
        superoperator += np.kron(dressed.conj(), dressed)
    return superoperator


def channel_normalization_defects(kraus_operators, left_layer):
    """Return trace-preservation and unitality max-norm defects."""
    dimension = left_layer.shape[0]
    trace_sum = np.zeros((dimension, dimension), dtype=complex)
    unital_sum = np.zeros((dimension, dimension), dtype=complex)
    for operator in kraus_operators:
        dressed = left_layer @ operator
        trace_sum += dressed.conj().T @ dressed
        unital_sum += dressed @ dressed.conj().T
    identity = np.eye(dimension)
    return (
        float(np.max(np.abs(trace_sum - identity))),
        float(np.max(np.abs(unital_sum - identity))),
    )


def diagonal_compression(superoperator, dimension):
    """Restriction from diagonal inputs to diagonal outputs."""
    compression = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        matrix_unit = np.zeros((dimension, dimension), dtype=complex)
        matrix_unit[source, source] = 1.0
        output = (
            superoperator @ matrix_unit.reshape(-1, order="F")
        ).reshape((dimension, dimension), order="F")
        compression[:, source] = np.diag(output)
    return compression


def matrix_rank_and_edges(matrix):
    """Numerical rank plus largest and first-null singular values."""
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.sum(singular_values > RANK_TOL))
    smallest_kept = float(singular_values[rank - 1]) if rank else 0.0
    largest_null = (
        float(singular_values[rank]) if rank < len(singular_values) else 0.0
    )
    return rank, smallest_kept, largest_null


def relative_gns_defect(superoperator):
    """Maximally-mixed GNS symmetry equals Hilbert-Schmidt symmetry."""
    return float(
        np.linalg.norm(superoperator - superoperator.conj().T, ord="fro")
        / np.linalg.norm(superoperator, ord="fro")
    )


def hermitian_traceless_basis(dimension):
    """Orthonormal generalized Gell-Mann basis."""
    basis = []
    for row in range(dimension):
        for column in range(row + 1, dimension):
            symmetric = np.zeros((dimension, dimension), dtype=complex)
            symmetric[row, column] = symmetric[column, row] = 1.0 / np.sqrt(2.0)
            basis.append(symmetric)
            antisymmetric = np.zeros((dimension, dimension), dtype=complex)
            antisymmetric[row, column] = -1.0j / np.sqrt(2.0)
            antisymmetric[column, row] = 1.0j / np.sqrt(2.0)
            basis.append(antisymmetric)
    for order in range(1, dimension):
        diagonal = np.zeros((dimension, dimension), dtype=complex)
        scale = np.sqrt(order * (order + 1.0))
        diagonal[np.arange(order), np.arange(order)] = 1.0 / scale
        diagonal[order, order] = -order / scale
        basis.append(diagonal)
    return tuple(basis)


def commutator_superoperator(hamiltonian):
    """Superoperator of -i[H, .] in column-vectorization convention."""
    dimension = hamiltonian.shape[0]
    identity = np.eye(dimension)
    return -1.0j * (
        np.kron(identity, hamiltonian)
        - np.kron(hamiltonian.T, identity)
    )


def project_anti_part_to_hamiltonian(anti_part, dimension):
    """Least-squares projection of an anti-GNS map onto commutators."""
    basis = hermitian_traceless_basis(dimension)
    design = np.column_stack(
        [commutator_superoperator(element).reshape(-1) for element in basis]
    )
    target = anti_part.reshape(-1)
    real_design = np.vstack((design.real, design.imag))
    real_target = np.concatenate((target.real, target.imag))
    coefficients, _, _, _ = np.linalg.lstsq(
        real_design, real_target, rcond=None
    )
    hamiltonian = sum(
        coefficient * element for coefficient, element in zip(coefficients, basis)
    )
    fitted = commutator_superoperator(hamiltonian)
    residual = float(
        np.linalg.norm(anti_part - fitted, ord="fro")
        / max(np.linalg.norm(anti_part, ord="fro"), np.finfo(float).eps)
    )
    return hamiltonian, fitted, residual


def mu4_covariance_defect(superoperator, length):
    """Covariance defect for Q = diag(1, i, -1) and all mu4 powers."""
    local_character = np.diag([1.0, 1.0j, -1.0]).astype(complex)
    worst = 0.0
    for group_element in range(4):
        representation = kron_all(
            [np.linalg.matrix_power(local_character, group_element)] * length
        )
        adjoint_action = np.kron(representation.conj(), representation)
        defect = np.linalg.norm(
            superoperator @ adjoint_action - adjoint_action @ superoperator,
            ord="fro",
        ) / np.linalg.norm(superoperator, ord="fro")
        worst = max(worst, float(defect))
    return worst


def fitted_power(arguments, values):
    """Log-log power fit for strictly positive samples."""
    return float(np.polyfit(np.log(arguments), np.log(values), 1)[0])


unitary_b = build_lift()
local_kraus = local_collision_kraus(unitary_b)

print("=== (1) actual reduced collision and classical diagonal anchor ===")
unitary_defect = float(
    np.max(np.abs(unitary_b.conj().T @ unitary_b - np.eye(LOCAL_DIM)))
)
unistochastic_defect = float(np.max(np.abs(np.abs(unitary_b) ** 2 - BF)))
rep(
    "v977 lift is unitary and |U_B|^2 = B",
    unitary_defect < ABS_TOL and unistochastic_defect < ABS_TOL,
    "unitary defect %.3e; |U|^2-B %.3e"
    % (unitary_defect, unistochastic_defect),
)

records = {}
for length in (2, 3):
    dimension = LOCAL_DIM**length
    kraus = chain_collision_kraus(local_kraus, length)
    for theta in (0.0, 0.08):
        left = interaction_unitary(length, theta)
        superoperator = channel_superoperator(kraus, left)
        tp_defect, unital_defect = channel_normalization_defects(kraus, left)
        rank, smallest_kept, largest_null = matrix_rank_and_edges(superoperator)
        records[(length, theta)] = superoperator
        expected_rank = dimension
        rep(
            "L=%d theta=%.2f channel is CPTP/unital and has rank %d on M_%d "
            "(nullity %d)" % (
                length,
                theta,
                expected_rank,
                dimension,
                dimension**2 - expected_rank,
            ),
            tp_defect < ABS_TOL
            and unital_defect < ABS_TOL
            and rank == expected_rank
            and largest_null < RANK_TOL,
            "TP %.3e; unital %.3e; sigma_kept %.3e; sigma_null %.3e"
            % (tp_defect, unital_defect, smallest_kept, largest_null),
        )

    classical = diagonal_compression(records[(length, 0.0)], dimension)
    expected_classical = kron_all([BF] * length)
    classical_defect = float(np.max(np.abs(classical - expected_classical)))
    classical_eigenvalues = np.linalg.eigvalsh(expected_classical)
    rep(
        "L=%d diagonal restriction is the proven-positive B^(xL)" % length,
        classical_defect < ABS_TOL and classical_eigenvalues[0] > 0.0,
        "max defect %.3e; spectrum [%.6f, %.6f]"
        % (
            classical_defect,
            float(classical_eigenvalues[0]),
            float(classical_eigenvalues[-1]),
        ),
    )

print("=== (2) finite channel logarithm and detailed-balance anchor ===")
for length in (2, 3):
    dimension = LOCAL_DIM**length
    for theta in (0.0, 0.08):
        superoperator = records[(length, theta)]
        rank, _, _ = matrix_rank_and_edges(superoperator)
        rep(
            "L=%d theta=%.2f finite channel logarithm is obstructed: "
            "rank %d < %d, while exp(generator) is always invertible"
            % (length, theta, rank, dimension**2),
            rank < dimension**2,
        )
    theta_zero_defect = relative_gns_defect(records[(length, 0.0)])
    rep(
        "L=%d theta=0 requested GNS anchor FAILS as a premise: "
        "Phi_0 != Phi_0^GNS-adj" % length,
        theta_zero_defect > DEFECT_TOL,
        "relative defect %.6e" % theta_zero_defect,
    )

print("=== (3) Poissonized fallback: closest Hamiltonian split at L=2 ===")
length = 2
dimension = LOCAL_DIM**length
kraus_l2 = chain_collision_kraus(local_kraus, length)
identity_superoperator = np.eye(dimension**2)
hamiltonians = {}
symmetric_parts = {}
split_residuals = {}
for theta in THETAS:
    superoperator = channel_superoperator(
        kraus_l2, interaction_unitary(length, theta)
    )
    poisson_generator = superoperator - identity_superoperator
    symmetric_part = 0.5 * (
        poisson_generator + poisson_generator.conj().T
    )
    anti_part = 0.5 * (
        poisson_generator - poisson_generator.conj().T
    )
    hamiltonian, fitted_anti, residual = project_anti_part_to_hamiltonian(
        anti_part, dimension
    )
    reconstruction_defect = float(
        np.linalg.norm(
            poisson_generator - symmetric_part - fitted_anti, ord="fro"
        )
        / np.linalg.norm(poisson_generator, ord="fro")
    )
    hermitian_defect = float(
        np.max(np.abs(hamiltonian - hamiltonian.conj().T))
    )
    spectrum = np.linalg.eigvalsh(symmetric_part)
    hamiltonians[theta] = hamiltonian
    symmetric_parts[theta] = symmetric_part
    split_residuals[theta] = residual
    print(
        "   theta=%.2f: ||H_fit||_F=%.6e, anti->comm residual=%.6e, "
        "full reconstruction defect=%.6e, spec(L_sym)=[%.6e, %.6e]"
        % (
            theta,
            np.linalg.norm(hamiltonian, ord="fro"),
            residual,
            reconstruction_defect,
            float(spectrum[0]),
            float(spectrum[-1]),
        )
    )
    rep(
        "theta=%.2f closest H_eff is Hermitian and L_sym has real "
        "nonpositive spectrum" % theta,
        hermitian_defect < ABS_TOL and spectrum[-1] < ABS_TOL,
        "Hermitian defect %.3e; lambda_max %.3e"
        % (hermitian_defect, float(spectrum[-1])),
    )
    rep(
        "theta=%.2f exact reversible+dissipative split is BLOCKED: "
        "anti-GNS part is not a Hamiltonian commutator" % theta,
        residual > DEFECT_TOL and reconstruction_defect > DEFECT_TOL,
        "projection residual %.6e; reconstruction %.6e"
        % (residual, reconstruction_defect),
    )

h_zero_norm = float(np.linalg.norm(hamiltonians[0.0], ord="fro"))
rep(
    "theta=0 H_eff=0 anchor is false for the actual collision channel",
    h_zero_norm > DEFECT_TOL,
    "closest projected ||H_eff(0)||_F = %.6e" % h_zero_norm,
)

positive_thetas = np.array(THETAS[1:])
h_increments = np.array(
    [
        np.linalg.norm(hamiltonians[theta] - hamiltonians[0.0], ord="fro")
        for theta in THETAS[1:]
    ]
)
sym_increments = np.array(
    [
        np.linalg.norm(
            symmetric_parts[theta] - symmetric_parts[0.0], ord="fro"
        )
        for theta in THETAS[1:]
    ]
)
h_power = fitted_power(positive_thetas, h_increments)
sym_power = fitted_power(positive_thetas, sym_increments)
swap_hamiltonian = swap_ring_hamiltonian(length).astype(complex)
swap_hamiltonian -= (
    np.trace(swap_hamiltonian) / dimension
) * np.eye(dimension)
smallest_theta = THETAS[1]
smallest_h_increment = (
    hamiltonians[smallest_theta] - hamiltonians[0.0]
)
swap_coefficient = float(
    np.vdot(swap_hamiltonian, smallest_h_increment).real
    / (smallest_theta * np.vdot(swap_hamiltonian, swap_hamiltonian).real)
)
swap_leading_residual = float(
    np.linalg.norm(
        smallest_h_increment
        - smallest_theta * swap_coefficient * swap_hamiltonian,
        ord="fro",
    )
    / np.linalg.norm(smallest_h_increment, ord="fro")
)
print(
    "   small-theta increments: ||H_fit(theta)-H_fit(0)|| ~ theta^%.4f; "
    "||L_sym(theta)-L_sym(0)|| ~ theta^%.4f" % (h_power, sym_power)
)
print(
    "   leading closest-H form: H_fit(theta) = H_fit(0) "
    "+ theta * %.6e * (H_SWAP-ring - tr/d I) + orthogonal remainder "
    "(relative remainder %.6e at theta=%.2f)"
    % (swap_coefficient, swap_leading_residual, smallest_theta)
)
rep(
    "coupling-induced closest-H increment is linear",
    0.8 < h_power < 1.2,
    "power %.6f" % h_power,
)
rep(
    "requested quadratic L_sym correction is NOT present in the full "
    "quantum channel (typed obstruction, not silently promoted)",
    not (1.8 < sym_power < 2.2),
    "measured power %.6f" % sym_power,
)

print("=== (4) natural mu4-character covariance ===")
for length in (2, 3):
    for theta in (0.0, 0.08):
        covariance_defect = mu4_covariance_defect(
            records[(length, theta)], length
        )
        rep(
            "L=%d theta=%.2f natural qutrit mu4 covariance is absent"
            % (length, theta),
            covariance_defect > DEFECT_TOL,
            "relative commutator defect %.6e" % covariance_defect,
        )

print("=== (5) MUST-FAIL: non-unitary contractive interaction ===")
rates = np.linspace(0.5, 1.5, dimension)
contractive_layer = np.diag(np.exp(-MUTANT_ETA * rates)).astype(complex)
mutant_superoperator = channel_superoperator(kraus_l2, contractive_layer)
mutant_tp, mutant_unital = channel_normalization_defects(
    kraus_l2, contractive_layer
)
mutant_generator = mutant_superoperator - identity_superoperator
mutant_symmetric = 0.5 * (
    mutant_generator + mutant_generator.conj().T
)
mutant_anti = 0.5 * (
    mutant_generator - mutant_generator.conj().T
)
_, mutant_fitted, mutant_residual = project_anti_part_to_hamiltonian(
    mutant_anti, dimension
)
mutant_reconstruction = float(
    np.linalg.norm(
        mutant_generator - mutant_symmetric - mutant_fitted, ord="fro"
    )
    / np.linalg.norm(mutant_generator, ord="fro")
)
rep(
    "MUST-FAIL FIRES: contractive V_int is not a quantum channel and "
    "does not admit the clean split",
    mutant_tp > DEFECT_TOL
    and mutant_unital > DEFECT_TOL
    and mutant_residual > DEFECT_TOL
    and mutant_reconstruction > DEFECT_TOL,
    "TP %.6e; unital %.6e; anti->comm %.6e; reconstruction %.6e"
    % (
        mutant_tp,
        mutant_unital,
        mutant_residual,
        mutant_reconstruction,
    ),
)

print()
print(
    "VERDICT: QUANTUM_OS_SPLITTING_BLOCKED_SINGULAR_COLLISION -- "
    "the actual reduced collision channel has rank 3^L on an "
    "operator space of dimension 9^L, so no finite channel logarithm "
    "exists; at theta=0 it is already non-GNS-symmetric and its "
    "anti-GNS part is not a Hamiltonian commutator.  The classical "
    "positive B^(xL) diagonal shadow survives, but it does not lift to "
    "the requested exact quantum reversible+dissipative OS structure.  "
    "A weak-collision or redesigned detailed-balanced family is needed; "
    "thermodynamic-limit OS reconstruction stays [O]."
)
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
