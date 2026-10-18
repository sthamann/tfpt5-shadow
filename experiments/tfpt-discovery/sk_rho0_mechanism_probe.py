#!/usr/bin/env python3
"""Finite Schwinger--Keldysh/rho_0 mechanism probe -- EXPLORATION ONLY.

This reuses the 96-dimensional W[J] sector of
``tfpt4d_content_candidate_probe.py``: one quantum Z6 link, two sites,
and the Q (6Y=1) plus e^c (6Y=0) representative species.  It executes

    Z_SK[J_+,J_-;rho_0] = Tr(rho_0 U[J_+]^dagger U[J_-])

and operator insertions on both contour branches for two initial states:
the Euclidean-cap/KMS state exp(-beta H)/Z and a decorrelated product
state with the same one-mode occupancies.  The product state is a
contrast class, not another equilibrium state.

The equilibrium anchor is finite-spectral and unbroadened: KMS and FDT
are compared line by line on the exact Bohr-frequency grid.  W[J]
first derivatives are cross-checked against equal-branch SK insertions.
A rectangular seam-phase pulse then gives an exact unitary finite-time
asymmetry response whose dependence on rho_0 is measured.

The saddle S_init=-kappa*cos(5 theta-3 pi) has five global minima on
[0,2 pi).  A chosen mu4 orientation lift, represented by the width-pi/2
interval centered at 3pi/5, contains 3pi/5 as its unique minimum.  Since
S_init is not invariant under theta -> theta+pi/2, that lift is a [C]
orientation-selection step; the honest global verdict is DEGENERATE.

Boundary: finite 1+1D toy, one current/asymmetry class, no cosmological
solve and no eta_B/relic prediction.  FTRANSFER.SK.RHO0.01 stays [O].
This probe executes only its rho_0-dependence and typed saddle mechanism.
"""

import time

import numpy as np
import sympy as sp
from scipy.linalg import expm


START = time.perf_counter()
ALL_OK = True


def report(name, condition, details=""):
    """Record and print one deterministic check."""
    global ALL_OK
    passed = bool(condition)
    ALL_OK &= passed
    suffix = "  | " + details if details else ""
    print(("PASS " if passed else "FAIL ") + name + suffix)


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
# Honest boundary and verdict.
# ---------------------------------------------------------------------------
print("\n=== honest boundary ===")
print("  finite 96-dimensional 1+1D content shadow; one current class")
print("  no cosmological evolution; no eta_B or relic-number calculation")
print("  FTRANSFER.SK.RHO0.01 remains [O]; mechanism execution is not closure")
report(
    "honest typing boundary is enforced",
    HILBERT_DIMENSION <= 300 and len(global_minima) == 5,
)

elapsed = time.perf_counter() - START
print(
    "\nVERDICT: SK_RHO0_MECHANISM_EXECUTED + "
    "SADDLE_3PI5_DEGENERATE(typed)"
)
print(
    "  conditional [C] orientation lift: 3pi/5 is its unique minimum; "
    "globally five minima remain"
)
print("runtime %.2f s" % elapsed)
print("PROBE " + ("ALL PASS" if ALL_OK else "HAS FAILURES"))
raise SystemExit(0 if ALL_OK else 1)
