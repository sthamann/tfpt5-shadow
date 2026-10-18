#!/usr/bin/env python3
"""weak_collision_hp_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION.  The deployed v977/v984 strong collision erases a perfect
which-path record in one step, so its reduced channel is singular and cannot
be the exponential of a finite GKSL generator.  Does the typed successor -- a
fresh-ancilla weak-collision/Hudson-Parthasarathy family -- supply the missing
finite-dimensional continuous-time leg?

THE FAMILY.  Let Q = log(B), where

    B = (1/18) [[13, 1, 4], [1, 13, 4], [4, 4, 10]]
      = P1 + (2/3) P2 + (1/3) P3.

For each positive off-diagonal rate Q_ij use

    L_ij = sqrt(Q_ij) |i><j|,

and a fresh environment vacuum |0>.  One collision is the exact unitary

    V_dt = exp(sqrt(dt) A),
    A = sum_alpha (L_alpha (x) |alpha><0|
                   - L_alpha^dagger (x) |0><alpha|).

The environment used here is the minimal seven-level vacuum-plus-one-label
space: one vacuum and one orthogonal excitation label for each of the six
directed jump channels.  Six fresh qubits (one per jump channel, with sigma+
and sigma-) also suffice; the seven-level star is the smaller exact
single-collision realization and has the same HP/GKSL limit.  The O(dt)
counterterm in the exponent is chosen to be zero; unitarity generates the
required -1/2 sum L_alpha^dagger L_alpha drift automatically.

EXECUTABLE CLAIMS.
  1. (Phi_dt-I)/dt converges entrywise to exactly the analytic GKSL
     superoperator.  The dt={1e-3,...,1e-6} extraction is checked directly
     and by first-order Richardson extrapolation.
  2. The diagonal restriction of the GKSL generator is symbolically exactly
     Q=log(B).
  3. Phi_dt^(1/dt) converges to exp(L) with measured O(dt) error.  The
     limiting t=1 diagonal semigroup is symbolically exactly exp(Q)=B;
     finite collision products are reported as convergent approximations,
     not mislabeled as exact.
  4. The dissipator is GNS/Hilbert-Schmidt symmetric for the uniform state.
     Adding a nonzero Hamiltonian whose commutator does not commute with the
     dissipator leaves the exact anti-GNS Hamiltonian plus GNS-symmetric
     dissipator split.
  5. On an L=3 open band, fresh local collisions followed by one brickwork
     nearest-neighbour Hamiltonian gate layer grow observable support by at
     most one cell in one micro-step.
  6. MUST-FAIL: the strong deployed collision from
     quantum_band_os_probe.py has rank 9 on the 81-dimensional L=2 operator
     space.  It is singular, hence has no finite logarithmic generator.

HONEST BOUNDARY.  Finite dimensions and kernel level only.  This constructs
the finite continuous-time leg of DYN.UNITARY.DILATION.01, but proves no
uniform thermodynamic limit, field-level HP dilation, or field-level
Lieb-Robinson theorem.  The contract therefore stays [O]; no marker moves.

VERDICT ENUM: WEAK_COLLISION_HP_FAMILY_COMPLETE (or typed failure).
"""

from itertools import product

import numpy as np
import sympy as sp
from scipy.linalg import expm


LOCAL_DIM = 3
JUMP_CHANNELS = LOCAL_DIM * (LOCAL_DIM - 1)
ENV_DIM = 1 + JUMP_CHANNELS
GENERATOR_DTS = np.array([1.0e-3, 1.0e-4, 1.0e-5, 1.0e-6])
CONVERGENCE_DTS = np.array([1 / 20, 1 / 40, 1 / 80, 1 / 160, 1 / 320])
ABS_TOL = 2.0e-11
RICHARDSON_TOL = 2.0e-9
RATE_TOL = 1.0e-13
SPLIT_TOL = 2.0e-13
LOCALITY_TOL = 2.0e-12
RANK_TOL = 1.0e-10
LOCALITY_DT = 0.037

ok_all = True


def rep(name, ok, extra=""):
    """Print one executable check and accumulate the probe status."""
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


def kron_all(factors):
    """Kronecker product of a nonempty factor sequence."""
    result = np.array([[1.0]], dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def matrix_unit(row, column, dimension=LOCAL_DIM):
    """Return |row><column|."""
    operator = np.zeros((dimension, dimension), dtype=complex)
    operator[row, column] = 1.0
    return operator


def q_and_projectors_exact():
    """Return exact B, Q=log(B), and its spectral projectors."""
    uniform = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    sign = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    trace_free = sp.Matrix([1, 1, -2]) / sp.sqrt(6)
    projectors = (
        uniform * uniform.T,
        sign * sign.T,
        trace_free * trace_free.T,
    )
    p1, p2, p3 = projectors
    matrix_b = p1 + sp.Rational(2, 3) * p2 + sp.Rational(1, 3) * p3
    generator_q = sp.log(sp.Rational(2, 3)) * p2 + sp.log(
        sp.Rational(1, 3)
    ) * p3
    return matrix_b, generator_q, projectors


def build_jump_operators(generator_q):
    """Build the six L_ij=sqrt(Q_ij)|i><j| jump operators."""
    generator_float = np.array(generator_q.evalf(30), dtype=float)
    jumps = []
    labels = []
    for target in range(LOCAL_DIM):
        for source in range(LOCAL_DIM):
            if target == source:
                continue
            rate = float(generator_float[target, source])
            if rate <= RATE_TOL:
                raise ValueError(
                    "Q has nonpositive directed rate Q[%d,%d]=%.16e"
                    % (target, source, rate)
                )
            jumps.append(np.sqrt(rate) * matrix_unit(target, source))
            labels.append((target, source, rate))
    return tuple(jumps), tuple(labels)


def gksl_superoperator(jump_operators):
    """Column-vectorized sum L rho L* - 1/2{L*L,rho}."""
    identity = np.eye(LOCAL_DIM, dtype=complex)
    generator = np.zeros((LOCAL_DIM**2, LOCAL_DIM**2), dtype=complex)
    for jump in jump_operators:
        loss = jump.conj().T @ jump
        generator += np.kron(jump.conj(), jump)
        generator -= 0.5 * np.kron(identity, loss)
        generator -= 0.5 * np.kron(loss.T, identity)
    return generator


def collision_antihermitian(jump_operators):
    """Build A=sum L_alpha x |alpha><0|-L_alpha* x |0><alpha|."""
    interaction = np.zeros(
        (LOCAL_DIM * ENV_DIM, LOCAL_DIM * ENV_DIM), dtype=complex
    )
    for channel, jump in enumerate(jump_operators, start=1):
        creation = matrix_unit(channel, 0, ENV_DIM)
        annihilation = creation.conj().T
        interaction += np.kron(jump, creation)
        interaction -= np.kron(jump.conj().T, annihilation)
    return interaction


def collision_kraus(dt, interaction):
    """Extract K_e=<e|exp(sqrt(dt)A)|0> from the exact collision unitary."""
    unitary = expm(np.sqrt(dt) * interaction)
    vacuum_columns = np.arange(LOCAL_DIM) * ENV_DIM
    kraus = []
    for environment_outcome in range(ENV_DIM):
        output_rows = (
            np.arange(LOCAL_DIM) * ENV_DIM + environment_outcome
        )
        kraus.append(unitary[np.ix_(output_rows, vacuum_columns)])
    return tuple(kraus), unitary


def channel_superoperator(kraus_operators):
    """Column-vectorized CPTP channel superoperator."""
    channel = np.zeros((LOCAL_DIM**2, LOCAL_DIM**2), dtype=complex)
    for operator in kraus_operators:
        channel += np.kron(operator.conj(), operator)
    return channel


def channel_defects(kraus_operators):
    """Return trace-preservation and unitality max-entry defects."""
    trace_sum = np.zeros((LOCAL_DIM, LOCAL_DIM), dtype=complex)
    unit_sum = np.zeros((LOCAL_DIM, LOCAL_DIM), dtype=complex)
    for operator in kraus_operators:
        trace_sum += operator.conj().T @ operator
        unit_sum += operator @ operator.conj().T
    identity = np.eye(LOCAL_DIM)
    return (
        float(np.max(np.abs(trace_sum - identity))),
        float(np.max(np.abs(unit_sum - identity))),
    )


def diagonal_compression(superoperator, dimension=LOCAL_DIM):
    """Map diagonal input coefficients to diagonal output coefficients."""
    compression = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        vector = matrix_unit(source, source, dimension).reshape(-1, order="F")
        output = (superoperator @ vector).reshape(
            (dimension, dimension), order="F"
        )
        compression[:, source] = np.diag(output)
    return compression


def exact_diagonal_generator(generator_q):
    """Construct the symbolic diagonal restriction from the directed rates."""
    diagonal_generator = sp.zeros(LOCAL_DIM)
    for target in range(LOCAL_DIM):
        for source in range(LOCAL_DIM):
            if target == source:
                continue
            rate = generator_q[target, source]
            diagonal_generator[target, source] += rate
            diagonal_generator[source, source] -= rate
    return diagonal_generator


def commutator_superoperator(hamiltonian):
    """Column-vectorized -i[H,.]."""
    identity = np.eye(hamiltonian.shape[0], dtype=complex)
    return -1.0j * (
        np.kron(identity, hamiltonian)
        - np.kron(hamiltonian.T, identity)
    )


def relative_adjoint_defect(superoperator, sign=1.0):
    """Relative ||S-sign*S*||_F, with a safe absolute fallback."""
    difference = superoperator - sign * superoperator.conj().T
    return float(
        np.linalg.norm(difference, ord="fro")
        / max(np.linalg.norm(superoperator, ord="fro"), np.finfo(float).eps)
    )


def embed_local(operator, site, length):
    """Embed one qutrit operator into an open qutrit chain."""
    factors = [np.eye(LOCAL_DIM, dtype=complex) for _ in range(length)]
    factors[site] = operator
    return kron_all(factors)


def swap_operator(dimension):
    """Two-site SWAP matrix."""
    swap = np.zeros((dimension**2, dimension**2), dtype=complex)
    for left in range(dimension):
        for right in range(dimension):
            source = dimension * left + right
            target = dimension * right + left
            swap[target, source] = 1.0
    return swap


def local_heisenberg(operator, kraus_operators):
    """Apply the one-cell adjoint collision channel."""
    return sum(
        kraus.conj().T @ operator @ kraus for kraus in kraus_operators
    )


def outside_commutator_defect(operator, outside_sites, length):
    """Largest commutator with matrix units on forbidden outside sites."""
    worst = 0.0
    for site in outside_sites:
        for row in range(LOCAL_DIM):
            for column in range(LOCAL_DIM):
                probe = embed_local(matrix_unit(row, column), site, length)
                defect = np.linalg.norm(
                    operator @ probe - probe @ operator, ord="fro"
                )
                worst = max(worst, float(defect))
    return worst


def strong_lift():
    """Numerical v977 U_B with |U_B|^2=B."""
    sine_13_squared = 2.0 / 9.0
    sine_12_squared = 1.0 / 14.0
    sine_23_squared = 2.0 / 7.0
    cosine_13_squared = 1.0 - sine_13_squared
    cosine_12_squared = 1.0 - sine_12_squared
    cosine_23_squared = 1.0 - sine_23_squared
    sine_12, cosine_12 = np.sqrt(sine_12_squared), np.sqrt(
        cosine_12_squared
    )
    sine_23, cosine_23 = np.sqrt(sine_23_squared), np.sqrt(
        cosine_23_squared
    )
    sine_13, cosine_13 = np.sqrt(sine_13_squared), np.sqrt(
        cosine_13_squared
    )
    phase = (-4.0 + 7.0j) / np.sqrt(65.0)
    return np.array(
        [
            [
                cosine_12 * cosine_13,
                sine_12 * cosine_13,
                sine_13 / phase,
            ],
            [
                -sine_12 * cosine_23
                - cosine_12 * sine_23 * sine_13 * phase,
                cosine_12 * cosine_23
                - sine_12 * sine_23 * sine_13 * phase,
                sine_23 * cosine_13,
            ],
            [
                sine_12 * sine_23
                - cosine_12 * cosine_23 * sine_13 * phase,
                -cosine_12 * sine_23
                - sine_12 * cosine_23 * sine_13 * phase,
                cosine_23 * cosine_13,
            ],
        ],
        dtype=complex,
    )


def strong_collision_superoperator_l2():
    """L=2 strong which-path collision from quantum_band_os_probe.py."""
    unitary = strong_lift()
    local_kraus = []
    for outcome in range(LOCAL_DIM):
        operator = np.zeros((LOCAL_DIM, LOCAL_DIM), dtype=complex)
        operator[outcome, :] = unitary[outcome, :]
        local_kraus.append(operator)
    strong_superoperator = np.zeros((81, 81), dtype=complex)
    for left, right in product(local_kraus, repeat=2):
        operator = np.kron(left, right)
        strong_superoperator += np.kron(operator.conj(), operator)
    return strong_superoperator, unitary


def fitted_power(arguments, values):
    """Return the log-log least-squares convergence power."""
    return float(np.polyfit(np.log(arguments), np.log(values), 1)[0])


def main():
    """Run the weak-collision construction and all executable checks."""
    matrix_b_exact, generator_q_exact, projectors = q_and_projectors_exact()
    matrix_b = np.array(matrix_b_exact, dtype=float)
    generator_q = np.array(generator_q_exact.evalf(30), dtype=float)
    jumps, jump_labels = build_jump_operators(generator_q_exact)
    analytic_generator = gksl_superoperator(jumps)
    interaction = collision_antihermitian(jumps)

    print("=== (1) weak-collision family and generator extraction ===")
    antihermitian_defect = float(
        np.max(np.abs(interaction + interaction.conj().T))
    )
    rates = np.array([label[2] for label in jump_labels])
    rep(
        "six directed Q_ij rates are strictly positive and A is "
        "anti-Hermitian",
        len(jumps) == JUMP_CHANNELS
        and np.min(rates) > 0.0
        and antihermitian_defect < ABS_TOL,
        "rate range [%.12e, %.12e]; A+A* %.3e"
        % (np.min(rates), np.max(rates), antihermitian_defect),
    )

    generator_estimates = []
    direct_errors = []
    expansion_scaled_errors = []
    finite_unital_defects = []
    collision_records = {}
    for dt in GENERATOR_DTS:
        kraus, unitary = collision_kraus(dt, interaction)
        channel = channel_superoperator(kraus)
        collision_records[float(dt)] = (kraus, channel)
        estimate = (channel - np.eye(LOCAL_DIM**2)) / dt
        error = float(np.max(np.abs(estimate - analytic_generator)))
        remainder = float(
            np.max(
                np.abs(
                    channel
                    - np.eye(LOCAL_DIM**2)
                    - dt * analytic_generator
                )
            )
        )
        tp_defect, unital_defect = channel_defects(kraus)
        unitary_defect = float(
            np.max(
                np.abs(
                    unitary.conj().T @ unitary
                    - np.eye(LOCAL_DIM * ENV_DIM)
                )
            )
        )
        generator_estimates.append(estimate)
        direct_errors.append(error)
        expansion_scaled_errors.append(remainder / dt**1.5)
        finite_unital_defects.append(unital_defect)
        print(
            "   dt=%.0e: max|G_dt-L|=%.12e; "
            "max|Phi-I-dt L|/dt^(3/2)=%.12e; "
            "unitary/TP/unital=(%.3e, %.3e, %.3e)"
            % (
                dt,
                error,
                expansion_scaled_errors[-1],
                unitary_defect,
                tp_defect,
                unital_defect,
            )
        )
        rep(
            "dt=%.0e exact collision is unitary and CPTP" % dt,
            unitary_defect < ABS_TOL
            and tp_defect < ABS_TOL,
        )

    finite_unital_power = fitted_power(
        GENERATOR_DTS, finite_unital_defects
    )
    generator_unital_defect = float(
        np.max(
            np.abs(
                analytic_generator
                @ np.eye(LOCAL_DIM).reshape(-1, order="F")
            )
        )
    )
    rep(
        "finite star collisions have only O(dt^2) unital drift, while "
        "the limiting GKSL generator is exactly unital",
        1.9 < finite_unital_power < 2.1
        and generator_unital_defect < ABS_TOL,
        "finite-dt power %.6f; L(I) max defect %.3e"
        % (finite_unital_power, generator_unital_defect),
    )

    richardson_errors = []
    for coarse_index in range(len(GENERATOR_DTS) - 1):
        ratio = (
            GENERATOR_DTS[coarse_index]
            / GENERATOR_DTS[coarse_index + 1]
        )
        extrapolated = (
            ratio * generator_estimates[coarse_index + 1]
            - generator_estimates[coarse_index]
        ) / (ratio - 1.0)
        error = float(np.max(np.abs(extrapolated - analytic_generator)))
        richardson_errors.append(error)
        print(
            "   Richardson %.0e/%.0e -> dt=0: max entry error %.12e"
            % (
                GENERATOR_DTS[coarse_index],
                GENERATOR_DTS[coarse_index + 1],
                error,
            )
        )
    rep(
        "Phi_dt = id + dt L_GKSL + O(dt^(3/2)); direct extraction "
        "converges and Richardson reaches numerical precision",
        np.all(np.diff(direct_errors) < 0.0)
        and expansion_scaled_errors[-1] < expansion_scaled_errors[0]
        and richardson_errors[-1] < RICHARDSON_TOL,
        "direct %.3e -> %.3e; final Richardson %.3e"
        % (direct_errors[0], direct_errors[-1], richardson_errors[-1]),
    )

    print("=== (2) exact classical diagonal restriction ===")
    diagonal_exact = exact_diagonal_generator(generator_q_exact)
    symbolic_diagonal_defect = sp.simplify(
        diagonal_exact - generator_q_exact
    )
    numeric_diagonal_defect = float(
        np.max(
            np.abs(
                diagonal_compression(analytic_generator) - generator_q
            )
        )
    )
    rep(
        "diag(L_GKSL)=Q=log(B) symbolically exactly",
        symbolic_diagonal_defect == sp.zeros(LOCAL_DIM)
        and numeric_diagonal_defect < ABS_TOL,
        "symbolic zero=%s; numerical max defect %.3e"
        % (
            symbolic_diagonal_defect == sp.zeros(LOCAL_DIM),
            numeric_diagonal_defect,
        ),
    )

    print("=== (3) finite products and exact t=1 kernel anchor ===")
    semigroup_t1 = expm(analytic_generator)
    semigroup_diagonal = diagonal_compression(semigroup_t1)
    semigroup_b_defect = float(
        np.max(np.abs(semigroup_diagonal - matrix_b))
    )
    p1, p2, p3 = projectors
    exact_exp_q = (
        p1
        + sp.exp(sp.log(sp.Rational(2, 3))) * p2
        + sp.exp(sp.log(sp.Rational(1, 3))) * p3
    )
    exact_t1_defect = sp.simplify(exact_exp_q - matrix_b_exact)
    rep(
        "limiting t=1 diagonal dynamics exp(Q)=B exactly",
        exact_t1_defect == sp.zeros(LOCAL_DIM)
        and semigroup_b_defect < ABS_TOL,
        "symbolic zero=%s; numerical max defect %.3e"
        % (
            exact_t1_defect == sp.zeros(LOCAL_DIM),
            semigroup_b_defect,
        ),
    )

    product_errors = []
    product_b_errors = []
    for dt in CONVERGENCE_DTS:
        steps = int(round(1.0 / dt))
        kraus, _ = collision_kraus(dt, interaction)
        channel = channel_superoperator(kraus)
        product_channel = np.linalg.matrix_power(channel, steps)
        product_error = float(
            np.max(np.abs(product_channel - semigroup_t1))
        )
        product_b_error = float(
            np.max(
                np.abs(diagonal_compression(product_channel) - matrix_b)
            )
        )
        product_errors.append(product_error)
        product_b_errors.append(product_b_error)
        print(
            "   dt=%8.6f n=%3d: max|Phi_dt^n-exp(L)|=%.12e; "
            "diagonal-to-B=%.12e"
            % (dt, steps, product_error, product_b_error)
        )
    convergence_power = fitted_power(CONVERGENCE_DTS, product_errors)
    rep(
        "n-fold weak collisions converge to exp(t L) with O(dt) error",
        np.all(np.diff(product_errors) < 0.0)
        and 0.90 < convergence_power < 1.10,
        "measured power %.6f; finest full/diagonal errors %.3e / %.3e"
        % (
            convergence_power,
            product_errors[-1],
            product_b_errors[-1],
        ),
    )

    print("=== (4) GNS detailed balance and exact Hamiltonian split ===")
    dissipator_gns_defect = relative_adjoint_defect(analytic_generator)
    hamiltonian = np.array(
        [[0.03, 0.07, 0.0], [0.07, -0.02, 0.05j], [0.0, -0.05j, -0.01]],
        dtype=complex,
    )
    hamiltonian *= 0.2
    commutator = commutator_superoperator(hamiltonian)
    total_generator = analytic_generator + commutator
    symmetric_part = 0.5 * (
        total_generator + total_generator.conj().T
    )
    anti_part = 0.5 * (
        total_generator - total_generator.conj().T
    )
    symmetric_split_defect = float(
        np.max(np.abs(symmetric_part - analytic_generator))
    )
    anti_split_defect = float(np.max(np.abs(anti_part - commutator)))
    commutator_anti_defect = relative_adjoint_defect(commutator, sign=-1.0)
    noncommutation_norm = float(
        np.linalg.norm(
            analytic_generator @ commutator
            - commutator @ analytic_generator,
            ord="fro",
        )
    )
    rep(
        "classical-embedding dissipator is GNS-detailed-balanced for "
        "the uniform state",
        dissipator_gns_defect < SPLIT_TOL,
        "relative GNS symmetry defect %.3e" % dissipator_gns_defect,
    )
    rep(
        "nonzero H_eff gives the exact L=-i[H,.]+L_sym split even when "
        "the two parts do not commute",
        np.linalg.norm(hamiltonian, ord="fro") > 0.0
        and commutator_anti_defect < SPLIT_TOL
        and symmetric_split_defect < SPLIT_TOL
        and anti_split_defect < SPLIT_TOL
        and noncommutation_norm > 1.0e-6,
        "anti-GNS %.3e; sym split %.3e; anti split %.3e; "
        "||[L_sym,L_H]||_F %.3e"
        % (
            commutator_anti_defect,
            symmetric_split_defect,
            anti_split_defect,
            noncommutation_norm,
        ),
    )

    print("=== (5) L=3 brickwork locality ===")
    locality_kraus, _ = collision_kraus(LOCALITY_DT, interaction)
    pair_hamiltonian = 0.11 * swap_operator(LOCAL_DIM)
    pair_unitary = expm(-1.0j * LOCALITY_DT * pair_hamiltonian)
    layer_unitary = np.kron(pair_unitary, np.eye(LOCAL_DIM))
    worst_outside_defect = 0.0
    nontrivial_growth = 0.0
    for origin in range(3):
        allowed = (
            {0, 1} if origin in (0, 1) else {2}
        )
        outside = set(range(3)) - allowed
        for row in range(LOCAL_DIM):
            for column in range(LOCAL_DIM):
                local_input = matrix_unit(row, column)
                after_collision = local_heisenberg(
                    local_input, locality_kraus
                )
                chain_operator = embed_local(after_collision, origin, 3)
                after_layer = (
                    layer_unitary.conj().T
                    @ chain_operator
                    @ layer_unitary
                )
                worst_outside_defect = max(
                    worst_outside_defect,
                    outside_commutator_defect(
                        after_layer, outside, 3
                    ),
                )
                if origin == 0:
                    neighbour_probe = embed_local(
                        matrix_unit(0, 1), 1, 3
                    )
                    nontrivial_growth = max(
                        nontrivial_growth,
                        float(
                            np.linalg.norm(
                                after_layer @ neighbour_probe
                                - neighbour_probe @ after_layer,
                                ord="fro",
                            )
                        ),
                    )
    rep(
        "L=3 fresh local collisions plus one nearest-neighbour "
        "Hamiltonian brickwork layer grow support by at most one cell",
        worst_outside_defect < LOCALITY_TOL
        and nontrivial_growth > 1.0e-6,
        "outside-support commutator %.3e; neighbour-growth witness %.3e"
        % (worst_outside_defect, nontrivial_growth),
    )

    print("=== (6) MUST-FAIL strong-collision contrast ===")
    strong_superoperator, unitary_b = strong_collision_superoperator_l2()
    singular_values = np.linalg.svd(
        strong_superoperator, compute_uv=False
    )
    strong_rank = int(np.sum(singular_values > RANK_TOL))
    strong_minimum = float(singular_values[-1])
    lift_defect = float(
        np.max(np.abs(np.abs(unitary_b) ** 2 - matrix_b))
    )
    rep(
        "MUST-FAIL FIRES: deployed strong L=2 collision is singular "
        "(rank 9/81), so no finite channel logarithm/GKSL generator exists",
        lift_defect < ABS_TOL
        and strong_rank == 9
        and strong_minimum < RANK_TOL,
        "|U_B|^2-B %.3e; rank %d/81; sigma_min %.3e "
        "(contrast: quantum_band_os_probe.py)"
        % (lift_defect, strong_rank, strong_minimum),
    )

    print()
    verdict = (
        "WEAK_COLLISION_HP_FAMILY_COMPLETE"
        if ok_all
        else "WEAK_COLLISION_HP_FAMILY_TYPED_FAILURE"
    )
    print(
        "VERDICT: %s -- the fresh-ancilla sqrt(dt) collision family has "
        "the standard GKSL limit with exact classical restriction Q=log B, "
        "recovers B at t=1 in the limiting semigroup, restores the exact "
        "GNS-symmetric-plus-Hamiltonian split, and preserves one-layer "
        "brickwork locality at finite L=3.  The deployed strong collision "
        "remains singular.  Finite-dimensional kernel result only; the "
        "field/thermodynamic-limit contract stays [O]." % verdict
    )
    print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
