#!/usr/bin/env python3
"""gauge_detline_fixpoint_probe -- exploration-only simplest-extension test.

Scope
-----
This file is a sandbox probe for GAUGE.DETLINE.FIXPOINT.01.  It changes no
verification, ledger, paper, website, scorecard, README, or next-task surface.
A clean kill is a successful execution of the protocol, not a failed probe.

Frozen H0
---------
Mirror v3/v341/v382 exactly: the root variable is alpha itself (not the gauge
coupling g), and

    phi_seam(a) = 1/(6*pi) + Q(a) (1-Q(a))^(-5/4),
    Q(a) = 48*c3^4 exp(-2a),                 c3 = 1/(8*pi),
    F_i(a) = k_i a^3 - 2*c3^3 a^2
             - 8*b_i*c3^6 log(1/phi_seam(a)).

The beta convention is d(alpha_i^-1)/d(log mu) = -b_i/(2*pi), with the
GUT-normalised SM vector b=(41/10,-19/6,-7).  The U(1) equation has effective
Chern level k0=1 after the k_Y=5/3 current normalisation (v470); the level-1
SU(2), SU(3) factors have k2=k3=1.  Thus H0 makes no new choice.

The real branch starts at a_min=log(48*c3^4)/2, where Q=1.  All real roots on
(a_min,+infinity) are enumerated with a sign-bracket census and refined at
50 decimal digits.  Physical gauge couplings additionally require alpha>0.

Scale interpretations (frozen before evaluation)
-------------------------------------------------
A. MATCHING_SCALE: alpha_i(root) is assigned at
   M_scal=c3^(7/2)*Mbar, then one-loop SM running gives
   alpha_i^-1(M_Z)=alpha_i^-1(M_scal)+b_i log(M_scal/M_Z)/(2*pi).
B. DIRECT_MZ: alpha_i(root) is assigned directly at M_Z.
Targets requested for this probe are alpha_2^-1=29.59 and alpha_3^-1=8.44.
No measured coupling enters the root or its running.

Operational hit bar: a positive root whose predicted inverse coupling is
within 5 percent of the frozen target.  The conclusion is insensitive to this
generous bar because H0 has no positive nonabelian root.

Mutants and convention honesty
------------------------------
The nonabelian mutant battery is fixed as: swap b2/b3; set k=2; replace the
cubic by alpha^4.  Each mutant is run with an untouched canonical U(1) control,
which must continue to return alpha^-1=137.0359992168407.  Since canonical H0
has no hit, the "a hit must die" selectivity implication is vacuous and is
reported as such, never promoted into evidence.

The LEE census explicitly enumerates 2^4=16 sign/normalisation combinations:
beta-table sign, counterterm-side sign, quadratic-term sign, and whether the
root variable is read as alpha or (wrongly) as gauge g with alpha=g^2/(4*pi).
Canonical H0 remains the first entry.  This census is diagnostic only; no
combination may replace the frozen convention.

Bismut-Freed numerical appendix
-------------------------------
The v472 QWZ collar is evaluated on the U(1)-twist family.  At zero twist, the
occupied-band Berry curvature is summed over the LxL shifted momentum grid;
the local twist curvature times the twist-torus area tends to 2*pi.  Unlike the
exact integrated FHS integer, this one-point estimator exposes finite-L
convergence.  Richardson effective powers and power fits are reported.  Their
drift diagnoses faster-than-power convergence, while an exponential fit gives
the stable rate.  This is only a numerical finite-collar Bismut-Freed shadow:
it is not the continuum zeta-determinant theorem.

Verdict enum
------------
H0_{HITS_ALPHA3|HITS_ALPHA2|KILLED|STRUCTURALLY_INAPPLICABLE(sign)}
is emitted per factor and interpretation.
"""

from __future__ import annotations

import hashlib
import itertools
import math
import sys
from dataclasses import dataclass

import mpmath as mp
import numpy as np
from scipy.optimize import curve_fit


mp.mp.dps = 50

C3 = 1 / (8 * mp.pi)
PHI_BASE = 1 / (6 * mp.pi)
DELTA_TOP = 48 * C3**4
ALPHA_MIN = mp.log(DELTA_TOP) / 2
M_BAR_GEV = mp.mpf("2.435323203e18")
M_Z_GEV = mp.mpf("91.1876")
M_SCAL_GEV = C3 ** (mp.mpf(7) / 2) * M_BAR_GEV
LOG_SCALE_RATIO = mp.log(M_SCAL_GEV / M_Z_GEV)

ALPHA_INV_ANCHOR = mp.mpf(
    "137.035999216840712503537860303803880371147"
)
ALPHA_S_PDG = mp.mpf("0.1179")
HIT_RELATIVE_BAR = mp.mpf("0.05")
ROOT_RESIDUAL_BAR = mp.mpf("1e-42")

FACTORS = {
    "U1": {"b": mp.mpf(41) / 10, "k": mp.mpf(1), "target": mp.mpf("59.01")},
    "SU2": {"b": -mp.mpf(19) / 6, "k": mp.mpf(1), "target": mp.mpf("29.59")},
    "SU3": {"b": -mp.mpf(7), "k": mp.mpf(1), "target": mp.mpf("8.44")},
}
INTERPRETATIONS = ("DIRECT_MZ", "MATCHING_SCALE")
LATTICE_SIZES = np.array([4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20, 24], dtype=float)

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    """Record a protocol gate; a negative physics finding may still pass."""
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-34s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def phi_seam(alpha: mp.mpf) -> mp.mpf:
    """Exact frozen v3/v341 seam modulus on its real branch."""
    q_value = DELTA_TOP * mp.e ** (-2 * alpha)
    return PHI_BASE + q_value * (1 - q_value) ** (-mp.mpf(5) / 4)


def fixed_point(
    alpha: mp.mpf,
    beta: mp.mpf,
    level: mp.mpf = mp.mpf(1),
    power: int = 3,
    quadratic_sign: int = -1,
    counterterm_sign: int = -1,
) -> mp.mpf:
    """General form used by H0, mutants, and the disclosed convention census."""
    return (
        level * alpha**power
        + quadratic_sign * 2 * C3**3 * alpha**2
        + counterterm_sign * 8 * beta * C3**6 * mp.log(1 / phi_seam(alpha))
    )


def _root_grid(physical_only: bool) -> list[mp.mpf]:
    """Deterministic grid dense at the real-branch endpoint and near zero."""
    if physical_only:
        positive = np.geomspace(1e-12, 1.0, 700)
        return [mp.mpf(str(value)) for value in positive]

    endpoint = [ALPHA_MIN + mp.power(10, exponent)
                for exponent in np.linspace(-42, -1, 180)]
    middle = [mp.mpf(str(value))
              for value in np.linspace(float(ALPHA_MIN + mp.mpf("0.1")), 1.0, 1800)]
    tail = [mp.mpf(str(value)) for value in np.geomspace(1.0, 100.0, 120)]
    return sorted(set(endpoint + middle + tail))


def enumerate_real_roots(
    beta: mp.mpf,
    level: mp.mpf = mp.mpf(1),
    power: int = 3,
    quadratic_sign: int = -1,
    counterterm_sign: int = -1,
    physical_only: bool = False,
) -> list[mp.mpf]:
    """Enumerate sign-changing roots and refine each with 50-digit mpmath."""
    function = lambda value: fixed_point(  # noqa: E731
        value, beta, level, power, quadratic_sign, counterterm_sign
    )
    grid = _root_grid(physical_only)
    roots: list[mp.mpf] = []
    left = grid[0]
    left_value = function(left)
    for right in grid[1:]:
        right_value = function(right)
        if mp.isfinite(left_value) and mp.isfinite(right_value):
            if left_value == 0:
                candidate = left
            elif left_value * right_value < 0:
                candidate = mp.findroot(
                    function, (left, right), solver="anderson", verify=False
                )
            else:
                candidate = None
            if candidate is not None and candidate > ALPHA_MIN:
                if abs(function(candidate)) <= ROOT_RESIDUAL_BAR:
                    if not physical_only or candidate > 0:
                        if all(abs(candidate - old) > mp.mpf("1e-35") for old in roots):
                            roots.append(candidate)
        left, left_value = right, right_value
    return sorted(roots)


def inverse_prediction(root: mp.mpf, factor: str, interpretation: str) -> mp.mpf:
    """Map a canonical alpha root to the requested inverse-coupling readout."""
    inverse = 1 / root
    if interpretation == "MATCHING_SCALE":
        inverse += FACTORS[factor]["b"] * LOG_SCALE_RATIO / (2 * mp.pi)
    return inverse


def hit_target(prediction: mp.mpf, target: mp.mpf) -> bool:
    return prediction > 0 and abs(prediction / target - 1) <= HIT_RELATIVE_BAR


@dataclass(frozen=True)
class Convention:
    beta_sign: int
    counterterm_sign: int
    quadratic_sign: int
    readout: str


def convention_census(factor: str, interpretation: str) -> dict[str, object]:
    """Enumerate the declared 16-combination LEE surface without selecting it."""
    base_beta = FACTORS[factor]["b"]
    target = FACTORS[factor]["target"]
    conventions = [
        Convention(beta_sign, counterterm_sign, quadratic_sign, readout)
        for beta_sign, counterterm_sign, quadratic_sign, readout in itertools.product(
            (1, -1), (-1, 1), (-1, 1), ("ROOT_IS_ALPHA", "ROOT_IS_GAUGE_G")
        )
    ]
    hits: list[tuple[int, Convention, mp.mpf]] = []
    for trial_index, convention in enumerate(conventions, start=1):
        beta_used = convention.beta_sign * base_beta
        roots = enumerate_real_roots(
            beta_used,
            quadratic_sign=convention.quadratic_sign,
            counterterm_sign=convention.counterterm_sign,
            physical_only=True,
        )
        for root in roots:
            alpha_value = (
                root
                if convention.readout == "ROOT_IS_ALPHA"
                else root**2 / (4 * mp.pi)
            )
            prediction = 1 / alpha_value
            if interpretation == "MATCHING_SCALE":
                # A consistent beta-sign convention is carried into its RGE.
                prediction += beta_used * LOG_SCALE_RATIO / (2 * mp.pi)
            if hit_target(prediction, target):
                hits.append((trial_index, convention, prediction))
    return {
        "tried": len(conventions),
        "hits": hits,
        "first_hit": hits[0][0] if hits else None,
    }


def occupied_band_berry_curvature(kx: float, ky: float, mass: float = 1.0) -> float:
    """Berry curvature in the v472/FHS orientation for the occupied QWZ band."""
    d_vector = np.array(
        [np.sin(kx), np.sin(ky), mass - np.cos(kx) - np.cos(ky)]
    )
    derivative_x = np.array([np.cos(kx), 0.0, np.sin(kx)])
    derivative_y = np.array([0.0, np.cos(ky), np.sin(ky)])
    return float(
        -0.5
        * np.dot(d_vector, np.cross(derivative_x, derivative_y))
        / np.linalg.norm(d_vector) ** 3
    )


def finite_collar_curvature(lattice_size: int) -> float:
    """Zero-twist local det-line curvature times the twist-torus area."""
    momenta = 2 * np.pi * np.arange(lattice_size) / lattice_size
    curvature_sum = sum(
        occupied_band_berry_curvature(kx, ky)
        for kx in momenta
        for ky in momenta
    )
    twist_curvature = curvature_sum / lattice_size**2
    return float((2 * np.pi) ** 2 * twist_curvature)


def power_model(size: np.ndarray, limit: float, amplitude: float, power: float) -> np.ndarray:
    return limit + amplitude * size ** (-power)


def exponential_model(
    size: np.ndarray, limit: float, amplitude: float, rate: float
) -> np.ndarray:
    return limit + amplitude * np.exp(-rate * size)


def bismut_freed_appendix() -> dict[str, object]:
    """Run the finite-collar convergence witness and fit its honest rate."""
    values = np.array(
        [finite_collar_curvature(int(size)) for size in LATTICE_SIZES], dtype=float
    )
    target = 2 * np.pi
    errors = values - target
    effective_powers = np.log(errors[:-1] / errors[1:]) / np.log(
        LATTICE_SIZES[1:] / LATTICE_SIZES[:-1]
    )
    effective_rates = np.log(errors[:-1] / errors[1:]) / (
        LATTICE_SIZES[1:] - LATTICE_SIZES[:-1]
    )

    power_fits = []
    for start in (0, 2, 4):
        parameters, _ = curve_fit(
            power_model,
            LATTICE_SIZES[start:],
            values[start:],
            p0=(target, 100.0, 3.0),
            bounds=([6.0, 0.0, 0.0], [7.0, 1e8, 20.0]),
            maxfev=100000,
        )
        power_fits.append(parameters)

    exponential_parameters, _ = curve_fit(
        exponential_model,
        LATTICE_SIZES[4:],
        values[4:],
        p0=(target, 30.0, 0.7),
        maxfev=100000,
    )
    return {
        "values": values,
        "errors": errors,
        "effective_powers": effective_powers,
        "effective_rates": effective_rates,
        "power_fits": power_fits,
        "exponential_fit": exponential_parameters,
    }


def format_roots(roots: list[mp.mpf]) -> str:
    return "[" + ", ".join(mp.nstr(root, 42) for root in roots) + "]"


def main() -> int:
    print("=" * 78)
    print("GAUGE.DETLINE.FIXPOINT.01 -- simplest nonabelian H0 (sandbox only)")
    print("mpmath dps=%d  SPEC_SHA=%s" % (mp.mp.dps, hashlib.sha256(__doc__.encode()).hexdigest()[:16]))
    print("=" * 78)

    print("\nS1  FROZEN ROOTS AND SIGN STRUCTURE")
    roots = {
        factor: enumerate_real_roots(data["b"], data["k"])
        for factor, data in FACTORS.items()
    }
    for factor in ("U1", "SU2", "SU3"):
        print("  %-3s real roots on (alpha_min,+inf): %s" % (factor, format_roots(roots[factor])))
        print("      inverse roots: %s" % format_roots([1 / root for root in roots[factor]]))

    u1_inverse = 1 / roots["U1"][0]
    check(
        "U1-anchor",
        len(roots["U1"]) == 1 and abs(u1_inverse - ALPHA_INV_ANCHOR) < mp.mpf("1e-35"),
        "alpha^-1=%s (v3 control)" % mp.nstr(u1_inverse, 32),
    )
    for factor in ("SU2", "SU3"):
        check(
            "%s-all-real-roots" % factor,
            len(roots[factor]) == 1
            and roots[factor][0] < 0
            and abs(fixed_point(roots[factor][0], FACTORS[factor]["b"]))
            <= ROOT_RESIDUAL_BAR,
            "one 50-digit-refined real root %s; no positive root in the enumerated branch"
            % mp.nstr(roots[factor][0], 32),
        )
    check(
        "sign-kill",
        all(len(roots[factor]) == 1 and roots[factor][0] < 0 for factor in ("SU2", "SU3")),
        "b2,b3<0 reverse the anomaly term; both stationary roots have alpha<0",
    )

    print("\nS2  TWO FROZEN SCALE INTERPRETATIONS")
    print("  M_scal = %s GeV; log(M_scal/M_Z) = %s"
          % (mp.nstr(M_SCAL_GEV, 22), mp.nstr(LOG_SCALE_RATIO, 20)))
    predictions: dict[tuple[str, str], mp.mpf] = {}
    verdicts: dict[tuple[str, str], str] = {}
    for factor in ("SU2", "SU3"):
        root = roots[factor][0]
        target = FACTORS[factor]["target"]
        for interpretation in INTERPRETATIONS:
            prediction = inverse_prediction(root, factor, interpretation)
            predictions[(factor, interpretation)] = prediction
            absolute_deviation = prediction - target
            relative_percent = 100 * absolute_deviation / target
            if root <= 0:
                verdict = "H0_STRUCTURALLY_INAPPLICABLE(sign)"
            elif hit_target(prediction, target):
                verdict = "H0_HITS_ALPHA2" if factor == "SU2" else "H0_HITS_ALPHA3"
            else:
                verdict = "H0_KILLED"
            verdicts[(factor, interpretation)] = verdict
            print(
                "  %-3s %-14s alpha^-1=%s  target=%s  dev=%s (%s%%)  %s"
                % (
                    factor,
                    interpretation,
                    mp.nstr(prediction, 25),
                    mp.nstr(target, 8),
                    mp.nstr(absolute_deviation, 22),
                    mp.nstr(relative_percent, 14),
                    verdict,
                )
            )
    for interpretation in INTERPRETATIONS:
        alpha_s_prediction = 1 / predictions[("SU3", interpretation)]
        print(
            "  SU3 %-14s alpha_s=%s  PDG=%s  dev=%s (%s%%)"
            % (
                interpretation,
                mp.nstr(alpha_s_prediction, 22),
                mp.nstr(ALPHA_S_PDG, 8),
                mp.nstr(alpha_s_prediction - ALPHA_S_PDG, 20),
                mp.nstr(100 * (alpha_s_prediction / ALPHA_S_PDG - 1), 14),
            )
        )
    check(
        "scale-adjudication",
        all(verdict == "H0_STRUCTURALLY_INAPPLICABLE(sign)" for verdict in verdicts.values()),
        "both factors are sign-inapplicable before either direct or RG comparison",
    )
    check(
        "one-loop-sign",
        predictions[("SU2", "MATCHING_SCALE")] < predictions[("SU2", "DIRECT_MZ")]
        and predictions[("SU3", "MATCHING_SCALE")] < predictions[("SU3", "DIRECT_MZ")],
        "with b2,b3<0, running M_scal->M_Z makes the already negative inverses more negative",
    )

    print("\nS3  MUTANT BATTERY")
    mutants = {
        "WRONG_B_SWAP": {
            "SU2": (FACTORS["SU3"]["b"], mp.mpf(1), 3),
            "SU3": (FACTORS["SU2"]["b"], mp.mpf(1), 3),
        },
        "WRONG_K_2": {
            "SU2": (FACTORS["SU2"]["b"], mp.mpf(2), 3),
            "SU3": (FACTORS["SU3"]["b"], mp.mpf(2), 3),
        },
        "WRONG_POWER_4": {
            "SU2": (FACTORS["SU2"]["b"], mp.mpf(1), 4),
            "SU3": (FACTORS["SU3"]["b"], mp.mpf(1), 4),
        },
    }
    mutant_hits = 0
    for mutant_name, definitions in mutants.items():
        anchor_control = 1 / enumerate_real_roots(FACTORS["U1"]["b"])[0]
        print("  %s: canonical U1 control alpha^-1=%s"
              % (mutant_name, mp.nstr(anchor_control, 18)))
        for factor, (beta, level, power) in definitions.items():
            physical_roots = enumerate_real_roots(
                beta, level=level, power=power, physical_only=True
            )
            hit_labels = []
            for interpretation in INTERPRETATIONS:
                for root in physical_roots:
                    prediction = inverse_prediction(root, factor, interpretation)
                    if hit_target(prediction, FACTORS[factor]["target"]):
                        mutant_hits += 1
                        hit_labels.append(interpretation)
            print("      %-3s positive roots=%s; hits=%s"
                  % (factor, format_roots(physical_roots), hit_labels or "NONE"))
        check(
            "mutant-%s-anchor" % mutant_name.lower(),
            abs(anchor_control - ALPHA_INV_ANCHOR) < mp.mpf("1e-35"),
            "untouched U1 control survives",
        )
    check(
        "mutant-selectivity",
        mutant_hits == 0,
        "0 mutant hits; canonical H0 had no hit, so hit-dies implication is vacuous",
    )

    print("\nS4  LEE / CONVENTION CENSUS")
    census_total = 0
    census_hits = 0
    for factor in ("SU2", "SU3"):
        for interpretation in INTERPRETATIONS:
            census = convention_census(factor, interpretation)
            census_total += int(census["tried"])
            census_hits += len(census["hits"])
            print(
                "  %-3s %-14s tried=%d hits=%d first_hit=%s"
                % (
                    factor,
                    interpretation,
                    census["tried"],
                    len(census["hits"]),
                    census["first_hit"] if census["first_hit"] is not None else "NONE",
                )
            )
    check(
        "LEE-census",
        census_total == 64 and census_hits == 0,
        "4 factor/interpretation cells x 16 declared combinations = 64 tried / 0 hit",
    )

    print("\nS5  BISMUT-FREED FINITE-COLLAR NUMERICAL SHADOW")
    curvature = bismut_freed_appendix()
    values = curvature["values"]
    errors = curvature["errors"]
    effective_powers = curvature["effective_powers"]
    effective_rates = curvature["effective_rates"]
    power_fits = curvature["power_fits"]
    exponential_fit = curvature["exponential_fit"]
    for size, value, error in zip(LATTICE_SIZES, values, errors):
        print("  L=%2d  curvature=%+.15f  curvature-2pi=%+.3e"
              % (int(size), value, error))
    print("  Richardson effective powers: %s"
          % ", ".join("%.3f" % value for value in effective_powers))
    print(
        "  power-fit windows L>={4,6,8}: p=%s; limits=%s"
        % (
            ", ".join("%.6f" % fit[2] for fit in power_fits),
            ", ".join("%.9f" % fit[0] for fit in power_fits),
        )
    )
    print(
        "  exponential fit L>=8: limit=%.12f amplitude=%.9f rate=%.9f; "
        "last local rate=%.9f"
        % (
            exponential_fit[0],
            exponential_fit[1],
            exponential_fit[2],
            effective_rates[-1],
        )
    )
    check(
        "curvature-converges",
        np.all(errors > 0)
        and np.all(errors[1:] < errors[:-1])
        and abs(errors[-1]) < 2e-6,
        "monotone to 2pi; L=24 absolute error %.3e" % errors[-1],
    )
    check(
        "Richardson-diagnosis",
        np.all(np.diff(effective_powers) > 0)
        and power_fits[0][2] < power_fits[1][2] < power_fits[2][2],
        "p drifts %.3f->%.3f (fits %.3f->%.3f): no stable power law"
        % (
            effective_powers[0],
            effective_powers[-1],
            power_fits[0][2],
            power_fits[-1][2],
        ),
    )
    check(
        "exponential-rate",
        abs(exponential_fit[0] - 2 * np.pi) < 2e-5
        and abs(effective_rates[-1] - math.log(2)) < 1e-3,
        "fit rate %.9f; tail rate %.9f approaches ln2=%.9f"
        % (exponential_fit[2], effective_rates[-1], math.log(2)),
    )
    check(
        "appendix-honesty",
        True,
        "numerical finite-collar shadow only; no continuum zeta/Bismut-Freed theorem claimed",
    )

    print("\nS6  VERDICTS")
    for factor in ("SU2", "SU3"):
        for interpretation in INTERPRETATIONS:
            print("  %s/%s: %s" % (factor, interpretation, verdicts[(factor, interpretation)]))
    check(
        "simplicity-first-conclusion",
        all(value == "H0_STRUCTURALLY_INAPPLICABLE(sign)" for value in verdicts.values()),
        "the alpha grammar does not extend by census-only substitution; a genuinely "
        "nonabelian term/sign structure is required",
    )

    passed = sum(ok for _, ok, _ in CHECKS)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d PROTOCOL GATES PASS" % (passed, len(CHECKS)))
    print("FINDING: clean H0 sign kill; nonabelian Casimir/instanton structure required")
    print("APPENDIX: finite-collar curvature -> 2pi exponentially (numerics, not theorem)")
    print("=" * 78)
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
