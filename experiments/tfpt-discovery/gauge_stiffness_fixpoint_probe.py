#!/usr/bin/env python3
"""gauge_stiffness_fixpoint_probe -- EXPLORATION ONLY (no promotion).

Purpose
-------
Execute the background-field stiffness fixed-point *mechanism* requested by
GAUGE.DETLINE.FIXPOINT.01, after the naive nonabelian alpha-grammar extension
was structurally killed.  This probe changes no verification, ledger, paper,
website, scorecard, README, or next-task surface.  The contract stays [O].

Toy model
---------
Use the Gauss-reduced global mode of a 1+1D compact U(1) gauge field on an
L-site ring.  The electric-flux basis is truncated to n=-N,...,N.  A flat
background holonomy theta is equivalently a twist of the rotor wavefunction,
so its momentum is shifted by theta/(2*pi).  One staggered Jordan-Wigner
fermion species is coupled to the same frozen closing link exactly as in the
T3b construction of ``tfpt4d_content_candidate_probe.py``:

    H(g,theta) = H_rot(g,theta) tensor I + I tensor H_f(theta),
    H_rot = s (g^2 L/2) (n-theta/(2*pi))^2,
    H_f = -t sum_{x=0}^{L-2} (c_x^dag c_{x+1}+h.c.)
          -t (exp(i q theta)c_{L-1}^dag c_0+h.c.)
          +m sum_x (-1)^x n_x + mu sum_x n_x.

Here s=+1 canonically and s=-1 is the wrong-sign electric mutant.  The
background-field reduction is deliberately separable: it is the smallest
model that contains both the electric g-dependence and the frozen-seam
representation character exp(i q theta).  The complete finite Hilbert space
has dimension (2N+1) 2^L <= 112, and Gamma=-log Tr exp(-beta H) is evaluated
from its exact spectrum, with no stochastic estimator.

Free-rotor check
----------------
For weights p_n proportional to exp[-beta s g^2 L n^2/2], direct
differentiation at theta=0 gives

    K_rot = Gamma_rot''(0)/L
          = beta s g^2/(4*pi^2)
            - beta^2 g^4 L Var_p(n)/(4*pi^2).

For the physical sign and a cold zero-flux rotor, Var_p(n)->0 and this reduces
to the classical zero-flux value beta g^2/(4*pi^2).  The probe checks the
finite-temperature finite-truncation formula, which is stronger than using
the limiting expression.  Numerical stiffness uses centered differences at
h and h/2 and fourth-order Richardson extrapolation.

Fixed point and scope
---------------------
The one-factor toy equation is y=K(1/sqrt(y)), y=g^{-2}.  We enumerate a
declared g interval, refine its only sign bracket, run undamped Picard
iteration, and check |dK/dy|<1 at the solution.  Charge q enters only through
q theta, so the fermionic curvature must scale as q^2; q=0 is exactly blind.

HONEST BOUNDARY: this is a 1+1D, one-factor, truncated-global-rotor toy with a
free staggered fermion determinant.  It has no nonabelian root system,
Casimir, instanton, interacting gauge-matter, or four-dimensional continuum
content.  It executes existence, uniqueness, contraction, positivity, and
representation-character sensitivity of the stiffness mechanism; it does
not compute alpha_s or any physical Standard-Model coupling.

Verdict enum
------------
STIFFNESS_FIXPOINT_MECHANISM_{EXECUTED(g_star,contraction)|FAILS(where)}.
GAUGE.DETLINE.FIXPOINT.01 stays [O].
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq


BETA = 1.2
FLUX_CUTOFF = 3
HOPPING = 0.8
MASS = 0.6
CHEMICAL_POTENTIAL = 0.1
RICHARDSON_STEP = 0.01
G_MIN = 1.25
G_MAX = 3.50
G_SCAN_POINTS = 121
MAIN_VOLUME = 2
MAIN_CHARGE = 1
CURVE_G_VALUES = (1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 3.00, 3.50)
VOLUMES = (2, 3, 4)

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str) -> bool:
    """Record one deterministic protocol gate."""
    result = bool(passed)
    CHECKS.append((name, result, detail))
    print("  [%s] %-31s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def logsumexp(values: np.ndarray) -> float:
    """Stable real log(sum(exp(values))) for a nonempty finite vector."""
    values = np.asarray(values, dtype=float)
    maximum = float(np.max(values))
    return maximum + math.log(float(np.sum(np.exp(values - maximum))))


def rotor_energies(
    coupling: float,
    theta: float,
    volume: int,
    electric_sign: int = 1,
) -> np.ndarray:
    """Exact spectrum of the holonomy-twisted truncated global rotor."""
    flux = np.arange(-FLUX_CUTOFF, FLUX_CUTOFF + 1, dtype=float)
    shifted_flux = flux - theta / (2.0 * math.pi)
    return electric_sign * 0.5 * coupling**2 * volume * shifted_flux**2


def fermion_one_body(
    theta: float,
    volume: int,
    charge: int,
) -> np.ndarray:
    """Frozen-seam staggered-fermion matrix, the content-probe T3b pattern."""
    matrix = np.zeros((volume, volume), dtype=complex)
    for site in range(volume - 1):
        matrix[site, site + 1] -= HOPPING
        matrix[site + 1, site] -= HOPPING

    seam_phase = np.exp(1j * charge * theta)
    matrix[volume - 1, 0] -= HOPPING * seam_phase
    matrix[0, volume - 1] -= HOPPING * seam_phase.conjugate()
    for site in range(volume):
        matrix[site, site] += MASS * (-1) ** site + CHEMICAL_POTENTIAL
    return matrix


def fermion_fock_energies(theta: float, volume: int, charge: int) -> np.ndarray:
    """All 2^L many-body energies of the number-conserving quadratic fermion."""
    one_body = fermion_one_body(theta, volume, charge)
    hermiticity_error = float(np.max(np.abs(one_body - one_body.conj().T)))
    if hermiticity_error > 1e-13:
        raise AssertionError("fermion one-body Hamiltonian is not Hermitian")
    levels = np.linalg.eigvalsh(one_body)
    energies = np.empty(2**volume, dtype=float)
    for occupation_mask in range(2**volume):
        energies[occupation_mask] = sum(
            levels[level]
            for level in range(volume)
            if occupation_mask & (1 << level)
        )
    return energies


def gamma_exact(
    coupling: float,
    theta: float,
    volume: int,
    charge: int | None,
    electric_sign: int = 1,
) -> float:
    """Return -log Tr exp(-beta H) from every eigenvalue of the finite model."""
    rotor = rotor_energies(coupling, theta, volume, electric_sign)
    if charge is None:
        full_spectrum = rotor
    else:
        fermion = fermion_fock_energies(theta, volume, charge)
        full_spectrum = (rotor[:, None] + fermion[None, :]).reshape(-1)
    return -logsumexp(-BETA * full_spectrum)


@dataclass(frozen=True)
class Stiffness:
    value: float
    coarse: float
    fine: float
    error_estimate: float


def stiffness(
    coupling: float,
    volume: int,
    charge: int | None,
    electric_sign: int = 1,
    step: float = RICHARDSON_STEP,
) -> Stiffness:
    """Centered Gamma''/L with h,h/2 fourth-order Richardson extrapolation."""
    gamma_zero = gamma_exact(coupling, 0.0, volume, charge, electric_sign)

    def second_difference(delta: float) -> float:
        return (
            gamma_exact(coupling, delta, volume, charge, electric_sign)
            - 2.0 * gamma_zero
            + gamma_exact(coupling, -delta, volume, charge, electric_sign)
        ) / delta**2 / volume

    coarse = second_difference(step)
    fine = second_difference(step / 2.0)
    richardson = (4.0 * fine - coarse) / 3.0
    error_estimate = abs(fine - coarse) / 3.0
    return Stiffness(richardson, coarse, fine, error_estimate)


def rotor_stiffness_analytic(
    coupling: float,
    volume: int,
    electric_sign: int = 1,
) -> float:
    """Finite-beta, finite-cutoff free-rotor stiffness derived above."""
    flux = np.arange(-FLUX_CUTOFF, FLUX_CUTOFF + 1, dtype=float)
    exponents = (
        -BETA * electric_sign * 0.5 * coupling**2 * volume * flux**2
    )
    exponents -= np.max(exponents)
    probabilities = np.exp(exponents)
    probabilities /= np.sum(probabilities)
    mean_flux = float(np.dot(probabilities, flux))
    variance = float(np.dot(probabilities, (flux - mean_flux) ** 2))
    return (
        BETA * electric_sign * coupling**2 / (4.0 * math.pi**2)
        - BETA**2 * coupling**4 * volume * variance / (4.0 * math.pi**2)
    )


def residual(
    coupling: float,
    volume: int,
    charge: int | None,
    electric_sign: int = 1,
) -> float:
    """Fixed-point residual g^-2-K(g)."""
    return coupling**-2 - stiffness(
        coupling, volume, charge, electric_sign
    ).value


def root_census(
    volume: int,
    charge: int | None,
    electric_sign: int = 1,
) -> tuple[list[float], np.ndarray, np.ndarray]:
    """Enumerate all sign brackets on the declared interval and refine them."""
    couplings = np.linspace(G_MIN, G_MAX, G_SCAN_POINTS)
    residuals = np.array(
        [residual(g, volume, charge, electric_sign) for g in couplings]
    )
    roots: list[float] = []
    for left, right, f_left, f_right in zip(
        couplings[:-1], couplings[1:], residuals[:-1], residuals[1:]
    ):
        if f_left == 0.0:
            candidate = float(left)
        elif f_left * f_right < 0.0:
            candidate = float(
                brentq(
                    residual,
                    left,
                    right,
                    args=(volume, charge, electric_sign),
                    xtol=1e-13,
                    rtol=1e-13,
                )
            )
        else:
            continue
        if not roots or abs(candidate - roots[-1]) > 1e-9:
            roots.append(candidate)
    return roots, couplings, residuals


def contraction_derivative(coupling: float, volume: int, charge: int) -> float:
    """Centered derivative d K(1/sqrt(y))/dy at y=g^-2."""
    inverse_coupling = coupling**-2
    delta = 2.0e-4 * inverse_coupling

    def fixed_map(y_value: float) -> float:
        return stiffness(y_value**-0.5, volume, charge).value

    return (
        fixed_map(inverse_coupling + delta)
        - fixed_map(inverse_coupling - delta)
    ) / (2.0 * delta)


def picard_iterate(
    initial_coupling: float,
    volume: int,
    charge: int,
    tolerance: float = 1e-9,
    maximum_iterations: int = 200,
) -> tuple[float, int, float]:
    """Undamped iteration y_{k+1}=K(1/sqrt(y_k))."""
    inverse_coupling = initial_coupling**-2
    for iteration in range(1, maximum_iterations + 1):
        next_inverse = stiffness(
            inverse_coupling**-0.5, volume, charge
        ).value
        if next_inverse <= 0.0:
            return math.nan, iteration, math.inf
        update = abs(next_inverse - inverse_coupling)
        inverse_coupling = next_inverse
        if update < tolerance:
            coupling = inverse_coupling**-0.5
            return coupling, iteration, update
    return inverse_coupling**-0.5, maximum_iterations, update


def main() -> int:
    print("=" * 78)
    print("GAUGE.DETLINE.FIXPOINT.01 -- BACKGROUND-FIELD STIFFNESS TOY")
    print(
        "beta=%.2f N=%d t=%.2f m=%.2f mu=%.2f g-range=[%.2f,%.2f]"
        % (
            BETA,
            FLUX_CUTOFF,
            HOPPING,
            MASS,
            CHEMICAL_POTENTIAL,
            G_MIN,
            G_MAX,
        )
    )
    print("=" * 78)

    print("\nS1  EXACT GAMMA GRID + RICHARDSON STIFFNESS")
    representative_coupling = 2.0
    theta_grid = np.array([-0.16, -0.08, 0.0, 0.08, 0.16])
    gamma_grid = np.array(
        [
            gamma_exact(
                representative_coupling, theta, MAIN_VOLUME, MAIN_CHARGE
            )
            for theta in theta_grid
        ]
    )
    for theta, gamma_value in zip(theta_grid, gamma_grid):
        print("  theta=%+.3f  Gamma=%+.12f" % (theta, gamma_value))
    symmetry_error = float(np.max(np.abs(gamma_grid - gamma_grid[::-1])))
    representative_stiffness = stiffness(
        representative_coupling, MAIN_VOLUME, MAIN_CHARGE
    )
    check(
        "Gamma-even",
        symmetry_error < 1e-12,
        "max |Gamma(theta)-Gamma(-theta)|=%.2e" % symmetry_error,
    )
    check(
        "Richardson-stable",
        representative_stiffness.error_estimate < 5e-7,
        "K(2)=%.12f, estimated FD error %.2e"
        % (
            representative_stiffness.value,
            representative_stiffness.error_estimate,
        ),
    )

    print("\nS2  PURE U(1) ROTOR REDUCTION")
    maximum_rotor_error = 0.0
    for volume in VOLUMES:
        numerical = stiffness(
            representative_coupling, volume, None
        ).value
        analytic = rotor_stiffness_analytic(
            representative_coupling, volume
        )
        difference = abs(numerical - analytic)
        maximum_rotor_error = max(maximum_rotor_error, difference)
        print(
            "  L=%d K_rot(FD)=%.12f  K_rot(exact)=%.12f  |diff|=%.2e"
            % (volume, numerical, analytic, difference)
        )
    check(
        "free-rotor-formula",
        maximum_rotor_error < 2e-7,
        "max finite-beta formula error %.2e" % maximum_rotor_error,
    )

    print("\nS3  K(g) CURVE + FIXED POINT")
    print("  %7s %16s %16s" % ("g", "K(g)", "g^-2-K(g)"))
    curve_values = []
    for coupling in CURVE_G_VALUES:
        value = stiffness(coupling, MAIN_VOLUME, MAIN_CHARGE).value
        curve_values.append(value)
        print(
            "  %7.3f %16.12f %+16.12f"
            % (coupling, value, coupling**-2 - value)
        )

    roots, scan_couplings, scan_residuals = root_census(
        MAIN_VOLUME, MAIN_CHARGE
    )
    fixed_coupling = roots[0] if len(roots) == 1 else math.nan
    fixed_stiffness = (
        stiffness(fixed_coupling, MAIN_VOLUME, MAIN_CHARGE).value
        if math.isfinite(fixed_coupling)
        else math.nan
    )
    fixed_residual = (
        abs(fixed_coupling**-2 - fixed_stiffness)
        if math.isfinite(fixed_coupling)
        else math.inf
    )
    residual_increments = np.diff(scan_residuals)
    check(
        "existence-uniqueness",
        len(roots) == 1
        and np.all(residual_increments < 0.0)
        and fixed_residual < 2e-11,
        "one bracket; g*=%.12f K*=%.12f residual=%.2e; max dR=%.3e"
        % (
            fixed_coupling,
            fixed_stiffness,
            fixed_residual,
            float(np.max(residual_increments)),
        ),
    )
    iterated_coupling, iterations, final_update = picard_iterate(
        1.80, MAIN_VOLUME, MAIN_CHARGE
    )
    check(
        "undamped-iteration",
        abs(iterated_coupling - fixed_coupling) < 2e-8
        and final_update < 1e-9,
        "g_iter=%.12f in %d steps (last |dy| %.2e)"
        % (iterated_coupling, iterations, final_update),
    )

    contraction = contraction_derivative(
        fixed_coupling, MAIN_VOLUME, MAIN_CHARGE
    )
    check(
        "positive-stiffness",
        fixed_stiffness > 0.0 and min(curve_values) > 0.0,
        "K*=%.12f; min reported K(g)=%.12f"
        % (fixed_stiffness, min(curve_values)),
    )
    check(
        "contraction",
        abs(contraction) < 1.0,
        "dK/d(g^-2)=%.9f, spectral radius %.9f"
        % (contraction, abs(contraction)),
    )

    print("\nS4  REPRESENTATION-CONTENT / q^2 CHECK")
    pure = stiffness(
        fixed_coupling, MAIN_VOLUME, None
    ).value
    charge_zero = stiffness(
        fixed_coupling, MAIN_VOLUME, 0
    ).value
    charge_one = stiffness(
        fixed_coupling, MAIN_VOLUME, 1
    ).value
    charge_two = stiffness(
        fixed_coupling, MAIN_VOLUME, 2
    ).value
    contribution_one = charge_one - pure
    contribution_two = charge_two - pure
    charge_ratio = contribution_two / contribution_one
    print("  K_pure=%.12f" % pure)
    print("  Delta K(q=0)=%+.3e" % (charge_zero - pure))
    print("  Delta K(q=1)=%+.12f" % contribution_one)
    print("  Delta K(q=2)=%+.12f  ratio=%.9f" % (contribution_two, charge_ratio))
    check(
        "neutral-fermion-blind",
        abs(charge_zero - pure) < 2e-9,
        "|K(q=0)-K_pure|=%.2e" % abs(charge_zero - pure),
    )
    check(
        "charge-squared-content",
        abs(charge_ratio - 4.0) < 2e-5,
        "DeltaK(2)/DeltaK(1)=%.9f (target q^2=4)" % charge_ratio,
    )

    print("\nS5  VOLUME TREND")
    volume_roots: dict[int, float] = {}
    for volume in VOLUMES:
        volume_census, _, _ = root_census(volume, MAIN_CHARGE)
        if len(volume_census) == 1:
            volume_roots[volume] = volume_census[0]
            print(
                "  L=%d  g*=%.12f  K*=%.12f"
                % (
                    volume,
                    volume_census[0],
                    stiffness(
                        volume_census[0], volume, MAIN_CHARGE
                    ).value,
                )
            )
        else:
            print("  L=%d  roots=%s" % (volume, volume_census))
    first_drift = abs(volume_roots.get(3, math.inf) - volume_roots.get(2, 0.0))
    second_drift = abs(volume_roots.get(4, math.inf) - volume_roots.get(3, 0.0))
    check(
        "volume-roots",
        len(volume_roots) == len(VOLUMES)
        and second_drift < first_drift,
        "drifts |g3-g2|=%.6f, |g4-g3|=%.6f (finite-size stabilization)"
        % (first_drift, second_drift),
    )

    print("\nS6  MUTANTS")
    mutant_roots, _, mutant_residuals = root_census(
        MAIN_VOLUME, MAIN_CHARGE, electric_sign=-1
    )
    mutant_stiffness = stiffness(
        representative_coupling,
        MAIN_VOLUME,
        MAIN_CHARGE,
        electric_sign=-1,
    ).value
    print(
        "  wrong-sign electric: roots=%s, K(g=2)=%.12f, min residual=%.6f"
        % (
            mutant_roots if mutant_roots else "NONE",
            mutant_stiffness,
            float(np.min(mutant_residuals)),
        )
    )
    check(
        "wrong-sign-kills-existence",
        len(mutant_roots) == 0
        and mutant_stiffness < 0.0
        and np.all(mutant_residuals > 0.0),
        "negative stiffness leaves g^-2-K(g)>0 throughout declared range",
    )

    check(
        "honest-boundary",
        True,
        "1+1D one-factor toy only; no roots/Casimirs/instantons/alpha_s; contract [O]",
    )

    passed = sum(result for _, result, _ in CHECKS)
    total = len(CHECKS)
    all_pass = passed == total
    print("\n" + "=" * 78)
    print("RESULT: %d/%d PROTOCOL GATES PASS" % (passed, total))
    if all_pass:
        print(
            "VERDICT: STIFFNESS_FIXPOINT_MECHANISM_EXECUTED"
            "(g_star=%.12f, contraction=%.9f)"
            % (fixed_coupling, contraction)
        )
    else:
        failed = ",".join(name for name, result, _ in CHECKS if not result)
        print("VERDICT: STIFFNESS_FIXPOINT_MECHANISM_FAILS(%s)" % failed)
    print("GAUGE.DETLINE.FIXPOINT.01 stays [O]")
    print("=" * 78)
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
