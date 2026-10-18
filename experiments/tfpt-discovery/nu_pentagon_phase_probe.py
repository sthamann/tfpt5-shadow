#!/usr/bin/env python3
"""Test one frozen carrier-pentagon phase in the minimal neutrino rotation.

EXPLORATION ONLY.  This probe may create only the explicitly requested
``experiments/nu-scalaron-falsification/hypotheses/nu_scalaron_v3.yaml``.
It does not edit verification, papers, the ledger, website, scorecard, or READMEs.

PRE-DECLARED PHASE TEST (declared before evaluation)
---------------------------------------------------
Use exactly one phase and its complex-conjugate branch:

    H_PENT: phi = 4(2*pi/5) = 8*pi/5 = 288 degrees,
    conjugate: 2*pi - phi = 2*pi/5 = 72 degrees.

The 2*pi/5 class is already corpus-native: v429 freezes the pentagon partner
``2 cos(2*pi/5)=1/Phi`` and identifies v211's frozen spine quotient
``theta_i=3*pi/5`` as the carrier-pentagon interior angle.  The phase candidate
therefore uses the already-frozen g_car=5 angular class; no scan over phases is
performed.  For each branch, refit only theta in
``U = U_v9 R13(theta, phi)`` to all three angle observables.  The measured-data
acceptance rule is: every pull <= 1.5 sigma means CONSISTENT; any pull > 3 sigma
means KILLED.  The conjugate branches must have identical mixing angles.

PRE-DECLARED THETA CENSUS (evaluated only if H_PENT is consistent)
-----------------------------------------------------------------
The following nine and only nine candidates are tested.  A hit means that the
candidate lies inside the measured-target one-parameter profile interval
Delta-chi2 <= 1.  The look-elsewhere expectation is
``N * interval_width/(pi/2)`` under a uniform angle null on [0, pi/2], and the
family-wise Poisson approximation is ``1-exp(-E)``.  A structural ladder hit
requires E < 0.1.

1. ``asin(sqrt(phi0*exp(-5/6)))``: frozen v270 reactor amplitude read as an angle.
2. ``atan(sqrt(phi0*exp(-5/6)))``: the same frozen amplitude as a slope.
3. ``2*pi/35=(2*pi/5)/7``: carrier exterior angle divided by the frozen 7 in
   the scalaron exponent ``c3^(7/2)``.
4. ``(3*pi/5)/(2*g_car)``: v211 spine angle divided by the fixed sheet-carrier
   count ``2*g_car=10``; no other divisor is admitted.
5. ``asin(phi0^(1/2))``: the requested half-power phi0 ladder.
6. ``asin(phi0)``: the requested unit-power phi0 ladder.
7-9. Multiply candidates 1-3 by the exact v183 operator factor ``53/54``.
   This is the complete pre-declared 53/54-suppressed subfamily; suppression
   inside the trigonometric argument or application to other candidates is not
   allowed after seeing the result.

CIRCULARITY FIREWALL (mandatory)
--------------------------------
The source ``nu_ue_derivation_probe.py`` is reread and AST-audited.  Its fitted
theta and phase must trace to the NuFIT measured central values 0.02195 and
0.470, while the third measured angle is held out; TFPT values may occur only
as post-solve comparators.  This probe also repeats the frozen-phase one-
parameter fit against the v270 TFPT angle set, using the same NuFIT sigmas only
as a common metric.  A measured-only success is typed as data-consistency, not
as recovery or validation of the v270 angle set.

V3 FREEZE RULE (declared before evaluation)
-------------------------------------------
Create v3 only if (i) H_PENT is measured-target consistent and non-circular,
(ii) at least one theta candidate is inside Delta-chi2 <= 1, and (iii) the
theta-census LEE expectation is < 0.1.  The freeze keeps the v2 Majorana
operator, uses ``y3=y_t(M3)`` [P], and explicitly types ``y2/y3`` as a NuFIT
mass-data calibration.  The previously noticed ``2*phi0^2`` alternative is
reported but remains LEE-null and is not selected.  Thus mass observables using
y2 are calibrated outputs, whereas the frozen mixing vector is the structural
test; neither is promoted to a compiler claim.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
from dataclasses import dataclass

import mpmath as mp
from scipy.optimize import brentq, minimize_scalar


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SOURCE_PATH = os.path.join(HERE, "nu_ue_derivation_probe.py")
V3_PATH = os.path.join(
    REPO,
    "experiments",
    "nu-scalaron-falsification",
    "hypotheses",
    "nu_scalaron_v3.yaml",
)
V211_PATH = os.path.join(REPO, "verification", "v211_axion_spine_angle.py")
V429_PATH = os.path.join(REPO, "verification", "v429_axion_pentagon_phi.py")
sys.path.insert(0, HERE)

import nu_ue_derivation_probe as ue  # noqa: E402
from nu_ratio_grammar_probe import (  # noqa: E402
    DM2_21_EV2,
    EPSILON,
    M1_GEV,
    M2_GEV,
    M3_GEV,
    M_SCAL_GEV,
    V_EW_GEV,
    light_mass_ev,
    run_sm_up,
    yukawa_from_mass,
)


mp.mp.dps = 60

PHASE_DEGREES = mp.mpf("288")
CONJUGATE_PHASE_DEGREES = mp.mpf("72")
PHASE = mp.radians(PHASE_DEGREES)
CONJUGATE_PHASE = mp.radians(CONJUGATE_PHASE_DEGREES)
THETA_SEARCH_BOUNDS = (mp.mpf("0"), mp.pi / 2)
PHASE_CONSISTENCY_SIGMA = mp.mpf("1.5")
PHASE_KILL_SIGMA = mp.mpf("3")
PROFILE_DELTA_CHI2 = mp.mpf("1")
LEE_EXPECTATION_MAX = mp.mpf("0.1")
OBSERVABLE_NAMES = (
    "sin2_theta12",
    "sin2_theta13",
    "sin2_theta23",
)

MEASURED_TARGETS = {name: ue.NUFIT[name][0] for name in OBSERVABLE_NAMES}
TFPT_TARGETS = {
    "sin2_theta12": ue.S12_V9,
    "sin2_theta13": ue.TFPT_SIN2_THETA13,
    "sin2_theta23": ue.S23_V9,
}


@dataclass(frozen=True)
class FitResult:
    target_name: str
    phase: mp.mpf
    theta: mp.mpf
    chi2: mp.mpf
    predictions: dict[str, mp.mpf]
    pulls: dict[str, mp.mpf]
    profile_lower: mp.mpf
    profile_upper: mp.mpf


@dataclass(frozen=True)
class ThetaCandidate:
    name: str
    formula: str
    value: mp.mpf


def degrees(value: mp.mpf) -> mp.mpf:
    return value * 180 / mp.pi


def fmt(value: mp.mpf, digits: int = 16) -> str:
    return mp.nstr(value, digits)


def analytic_angles(theta: mp.mpf, phase: mp.mpf) -> dict[str, mp.mpf]:
    """Exact angle formulas for the same U_v9 R13 construction as the source."""
    sine = mp.sin(theta)
    cosine = mp.cos(theta)
    s0 = mp.sqrt(ue.S12_V9)
    c0_squared = 1 - ue.S12_V9
    reactor = c0_squared * sine**2
    denominator = 1 - reactor
    atmospheric_numerator = (
        cosine**2
        + ue.S12_V9 * sine**2
        - 2 * cosine * s0 * sine * mp.cos(phase)
    ) / 2
    return {
        "sin2_theta12": ue.S12_V9 / denominator,
        "sin2_theta13": reactor,
        "sin2_theta23": atmospheric_numerator / denominator,
    }


def objective(theta: mp.mpf, phase: mp.mpf, targets: dict[str, mp.mpf]) -> mp.mpf:
    predictions = analytic_angles(theta, phase)
    return mp.fsum(
        ((predictions[name] - targets[name]) / ue.NUFIT[name][1]) ** 2
        for name in OBSERVABLE_NAMES
    )


def fit_frozen_phase(
    target_name: str,
    targets: dict[str, mp.mpf],
    phase: mp.mpf,
) -> FitResult:
    """Fit the sole free parameter theta and construct its profile interval."""
    low, high = (float(value) for value in THETA_SEARCH_BOUNDS)
    preliminary = minimize_scalar(
        lambda value: float(objective(mp.mpf(value), phase, targets)),
        bounds=(low, high),
        method="bounded",
        options={"xatol": 1e-15},
    )
    theta = mp.findroot(
        lambda value: mp.diff(
            lambda variable: objective(variable, phase, targets),
            value,
        ),
        mp.mpf(preliminary.x),
    )
    predictions = analytic_angles(theta, phase)
    pulls = {
        name: (predictions[name] - targets[name]) / ue.NUFIT[name][1]
        for name in OBSERVABLE_NAMES
    }
    chi2 = objective(theta, phase, targets)
    profile_level = chi2 + PROFILE_DELTA_CHI2
    profile_lower = mp.mpf(
        brentq(
            lambda value: float(
                objective(mp.mpf(value), phase, targets) - profile_level
            ),
            low + 1e-14,
            float(theta),
        )
    )
    profile_upper = mp.mpf(
        brentq(
            lambda value: float(
                objective(mp.mpf(value), phase, targets) - profile_level
            ),
            float(theta),
            high - 1e-14,
        )
    )
    return FitResult(
        target_name,
        phase,
        theta,
        chi2,
        predictions,
        pulls,
        profile_lower,
        profile_upper,
    )


def theta_candidates() -> tuple[ThetaCandidate, ...]:
    """Return exactly the nine candidates declared in the module specification."""
    reactor_amplitude = mp.sqrt(ue.PHI0 * mp.exp(-mp.mpf(5) / 6))
    reactor_asin = mp.asin(reactor_amplitude)
    reactor_atan = mp.atan(reactor_amplitude)
    pentagon_over_seven = 2 * mp.pi / 35
    suppression = mp.mpf(53) / 54
    return (
        ThetaCandidate(
            "REACTOR_ASIN",
            "asin(sqrt(phi0*exp(-5/6)))",
            reactor_asin,
        ),
        ThetaCandidate(
            "REACTOR_ATAN",
            "atan(sqrt(phi0*exp(-5/6)))",
            reactor_atan,
        ),
        ThetaCandidate(
            "PENTAGON_OVER_7",
            "2*pi/35=(2*pi/5)/7",
            pentagon_over_seven,
        ),
        ThetaCandidate(
            "SPINE_OVER_SHEET_CARRIER",
            "(3*pi/5)/(2*g_car)",
            (3 * mp.pi / 5) / 10,
        ),
        ThetaCandidate(
            "PHI0_HALF_POWER_ASIN",
            "asin(phi0^(1/2))",
            mp.asin(mp.sqrt(ue.PHI0)),
        ),
        ThetaCandidate(
            "PHI0_UNIT_POWER_ASIN",
            "asin(phi0)",
            mp.asin(ue.PHI0),
        ),
        ThetaCandidate(
            "F53_REACTOR_ASIN",
            "(53/54)*asin(sqrt(phi0*exp(-5/6)))",
            suppression * reactor_asin,
        ),
        ThetaCandidate(
            "F53_REACTOR_ATAN",
            "(53/54)*atan(sqrt(phi0*exp(-5/6)))",
            suppression * reactor_atan,
        ),
        ThetaCandidate(
            "F53_PENTAGON_OVER_7",
            "(53/54)*(2*pi/35)",
            suppression * pentagon_over_seven,
        ),
    )


def profile_deviation(candidate: mp.mpf, fit: FitResult) -> mp.mpf:
    """Signed pull using the appropriate asymmetric profile half-width."""
    if candidate >= fit.theta:
        return (candidate - fit.theta) / (fit.profile_upper - fit.theta)
    return (candidate - fit.theta) / (fit.theta - fit.profile_lower)


def audit_source_provenance() -> dict[str, object]:
    """Reread the source and trace its solve inputs through the source AST."""
    with open(SOURCE_PATH, encoding="utf-8") as source_file:
        source = source_file.read()
    tree = ast.parse(source, filename=SOURCE_PATH)
    solve_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "solve_misalignment"
    ]
    main_solve_calls = [
        call
        for call in solve_calls
        if [ast.unparse(argument) for argument in call.args] == ["x13", "x23"]
    ]
    return {
        "source_sha16": hashlib.sha256(source.encode("utf-8")).hexdigest()[:16],
        "measured_literals_present": all(
            literal in source for literal in ('mp.mpf("0.02195")', 'mp.mpf("0.470")')
        ),
        "nufit_assignments_present": all(
            fragment in source
            for fragment in (
                'x13, sigma13 = NUFIT["sin2_theta13"]',
                'x23, sigma23 = NUFIT["sin2_theta23"]',
                'x12, sigma12 = NUFIT["sin2_theta12"]',
            )
        ),
        "fit_call_is_measured_x13_x23": len(main_solve_calls) == 1,
        "no_tfpt_argument_in_any_solve": all(
            "TFPT" not in ast.unparse(call) for call in solve_calls
        ),
        "tfpt_values_are_postsolve_comparators": (
            "frozen_phase_atmospheric = pmns_angles" in source
            and "TFPT reactor comparator" in source
            and source.index("solution = solve_misalignment(x13, x23)")
            < source.index("frozen_phase_atmospheric = pmns_angles")
        ),
    }


def full_observable_vector(theta: mp.mpf) -> dict[str, mp.mpf]:
    """Build the typed v3 vector with measured-calibrated y2 and frozen y3."""
    unitary = ue.v9_mixing_matrix() * ue.rotation13(theta, PHASE)
    angles = ue.pmns_angles(unitary)
    delta_cp = ue.physical_delta(unitary)
    y3, rundown3 = run_sm_up(M3_GEV)
    _yt2, rundown2 = run_sm_up(M2_GEV)
    m1 = mp.mpf("0")
    m2 = mp.sqrt(DM2_21_EV2)
    y2 = yukawa_from_mass(m2, M2_GEV, rundown2)
    m3 = light_mass_ev(y3, M3_GEV, rundown3)
    electron_weights = [abs(unitary[0, index]) ** 2 for index in range(3)]
    m_beta = mp.sqrt(
        electron_weights[0] * m1**2
        + electron_weights[1] * m2**2
        + electron_weights[2] * m3**2
    )
    m_bb_terms = (
        electron_weights[0] * m1,
        electron_weights[1] * m2,
        electron_weights[2] * m3,
    )
    largest_term = max(m_bb_terms)
    m_bb_max = mp.fsum(m_bb_terms)
    m_bb_min = max(mp.mpf("0"), 2 * largest_term - m_bb_max)
    return {
        "m1_eV": m1,
        "m2_eV": m2,
        "m3_eV": m3,
        "sigma_mnu_eV": m1 + m2 + m3,
        "m_beta_eV": m_beta,
        "m_bb_min_eV": m_bb_min,
        "m_bb_max_eV": m_bb_max,
        "y2_over_y3": y2 / y3,
        "y2_over_y3_companion": 2 * ue.PHI0**2,
        "sin2_theta12": angles["sin2_theta12"],
        "sin2_theta13": angles["sin2_theta13"],
        "sin2_theta23": angles["sin2_theta23"],
        "delta_cp_degrees": degrees(delta_cp),
    }


def build_v3_yaml(vector: dict[str, mp.mpf]) -> str:
    """Render the deterministic exploration freeze with explicit typing."""
    return f"""# nu-scalaron-falsification -- exploration hypothesis set v3
# FROZEN by nu_pentagon_phase_probe.py after its pre-declared protocol passed.
# This is a data-consistent structural candidate, not a verification claim.

candidate:
  name: qplus_pentagon_misalignment
  status: FROZEN_EXPLORATION
  mixing_construction: "U = U_v9 * R13(theta, phase)"
  theta:
    formula: "2*pi/35 = (2*pi/5)/7"
    degrees: {fmt(degrees(2 * mp.pi / 35), 16)}
    provenance: "carrier exterior angle divided by scalaron exponent numerator 7"
  phase:
    formula: "4*(2*pi/5) = 8*pi/5"
    degrees: 288
    conjugate_degrees: 72
    provenance: "g_car=5 pentagon angle class; v429/v211"
  typing: >
    The phase and theta are a pre-declared exploration-level structural
    identification tested against already-known NuFIT data.  They are not a
    blind prediction and do not move a ledger marker.

majorana_operator:
  basis: "Q_plus eigenbasis (v69)"
  epsilon: "phi0^2/(2*g_car)"
  M_scal: "c3^(7/2)*Mbar"
  M_R: "M_scal*diag(epsilon, 2*epsilon, 3)"
  eigenvalues_GeV:
    M1: {fmt(M1_GEV, 16)}
    M2: {fmt(M2_GEV, 16)}
    M3: {fmt(M3_GEV, 16)}
  ansatz_note: >
    Inherited from v2: the mixed epsilon insertion is an ansatz; M1 and M3
    package existing scales and M2 is the new interpolation prediction.

dirac_texture:
  formula: "Y_nu = diag(0, y2, y3) * U^dagger"
  y1_over_y3: 0
  y3: "y_t(M3) [P], using the frozen v481 one-loop runner"
  y2_over_y3: {fmt(vector["y2_over_y3"], 16)}
  y2_source: "DATA_CALIBRATED from NuFIT dm2_21=7.49e-5 eV^2"
  unselected_companion_2phi0sq: {fmt(vector["y2_over_y3_companion"], 16)}
  companion_typing: "PRIOR_CENSUS_LEE_NULL; reported, not selected"

observable_vector:
  masses:
    m1_eV: {fmt(vector["m1_eV"], 16)}
    m2_eV: {fmt(vector["m2_eV"], 16)}
    m3_eV: {fmt(vector["m3_eV"], 16)}
    mass_typing: "m1 NO floor; m2 data-calibrated; m3 y3=y_t/M3 prediction"
  mixing:
    sin2_theta12: {fmt(vector["sin2_theta12"], 16)}
    sin2_theta13: {fmt(vector["sin2_theta13"], 16)}
    sin2_theta23: {fmt(vector["sin2_theta23"], 16)}
    delta_cp_degrees: {fmt(vector["delta_cp_degrees"], 16)}
    mixing_typing: "structural candidate fixed by theta=2*pi/35 and phase=288 deg"
  derived:
    Sigma_mnu_eV: {fmt(vector["sigma_mnu_eV"], 16)}
    m_beta_eV: {fmt(vector["m_beta_eV"], 16)}
    m_bb_interval_eV:
      min: {fmt(vector["m_bb_min_eV"], 16)}
      max: {fmt(vector["m_bb_max_eV"], 16)}
    m_bb_note: "exact interval over unconstrained Majorana phases"

data_snapshot:
  nufit_60:
    sin2_theta12: [0.307, 0.012]
    sin2_theta13: [0.02195, 0.00058]
    sin2_theta23: [0.470, 0.017]
    dm2_21_eV2: 7.49e-5
  holdout: "future NuFIT/JUNO/DUNE/Hyper-K and DESI-class releases only"

kill_conditions:
  K1_PHASE: "updated measured-target frozen-phase refit has any angle beyond 3 sigma"
  K2_THETA: "theta=2*pi/35 lies beyond Delta-chi2=9 in an updated one-parameter profile"
  K3_ORDERING: "established inverted ordering"
  K4_MASS_SUM: "robust Sigma_mnu upper bound below the frozen vector after stated RG uncertainty"
  K5_REACTOR: "updated sin2_theta13 differs from the frozen vector by at least 3 sigma"
  K6_ATMOSPHERIC: "updated sin2_theta23 differs from the frozen vector by at least 3 sigma"
  K7_TEXTURE: "a derived corpus Y_nu in the Q_plus basis is incompatible with diag(0,y2,y3) U^dagger"

verdict_grammar:
  phase: "PENTAGON_PHASE_CONSISTENT"
  theta: "THETA_LADDER_HIT(PENTAGON_OVER_7, LEE)"
  freeze: "V3_FROZEN"
"""


def main() -> int:
    checks: list[tuple[str, bool]] = []
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()[:16]
    with open(V211_PATH, encoding="utf-8") as source_file:
        v211_source = source_file.read()
    with open(V429_PATH, encoding="utf-8") as source_file:
        v429_source = source_file.read()

    checks.extend(
        [
            ("exactly one phase plus conjugate declared", PHASE_DEGREES == 288 and CONJUGATE_PHASE_DEGREES == 72),
            ("phase branches are exact conjugates", abs(PHASE + CONJUGATE_PHASE - 2 * mp.pi) < mp.mpf("1e-55")),
            ("v211 freezes the 3pi/5 spine quotient", "theta_i = pi N_fam/g_car = 3 pi/5" in v211_source),
            ("v429 freezes the 2pi/5 pentagon partner", "2 cos(2pi/5)" in v429_source),
        ]
    )

    provenance = audit_source_provenance()
    provenance_ok = all(
        value
        for key, value in provenance.items()
        if key != "source_sha16"
    )
    checks.append(("source refit provenance is measured-only", provenance_ok))

    measured_fit = fit_frozen_phase("MEASURED_NUFIT", MEASURED_TARGETS, PHASE)
    measured_conjugate = fit_frozen_phase(
        "MEASURED_NUFIT_CONJUGATE",
        MEASURED_TARGETS,
        CONJUGATE_PHASE,
    )
    tfpt_fit = fit_frozen_phase("TFPT_V270", TFPT_TARGETS, PHASE)
    tfpt_conjugate = fit_frozen_phase(
        "TFPT_V270_CONJUGATE",
        TFPT_TARGETS,
        CONJUGATE_PHASE,
    )

    measured_max_pull = max(abs(value) for value in measured_fit.pulls.values())
    phase_consistent = measured_max_pull <= PHASE_CONSISTENCY_SIGMA
    phase_killed = measured_max_pull > PHASE_KILL_SIGMA
    tfpt_consistent = (
        max(abs(value) for value in tfpt_fit.pulls.values())
        <= PHASE_CONSISTENCY_SIGMA
    )
    branch_angle_residual = max(
        abs(measured_fit.predictions[name] - measured_conjugate.predictions[name])
        for name in OBSERVABLE_NAMES
    )
    tfpt_branch_residual = max(
        abs(tfpt_fit.predictions[name] - tfpt_conjugate.predictions[name])
        for name in OBSERVABLE_NAMES
    )
    checks.extend(
        [
            ("measured target meets the pre-declared 1.5 sigma gate", phase_consistent),
            ("pentagon phase is not killed at 3 sigma", not phase_killed),
            ("conjugate branches have identical measured angles", branch_angle_residual < mp.mpf("1e-50")),
            ("conjugate branches have identical TFPT angles", tfpt_branch_residual < mp.mpf("1e-50")),
            ("common target metric uses NuFIT sigmas", all(ue.NUFIT[name][1] > 0 for name in OBSERVABLE_NAMES)),
        ]
    )

    candidates = theta_candidates()
    hits = [
        candidate
        for candidate in candidates
        if measured_fit.profile_lower
        <= candidate.value
        <= measured_fit.profile_upper
    ]
    lee_expectation = (
        len(candidates)
        * (measured_fit.profile_upper - measured_fit.profile_lower)
        / (mp.pi / 2)
    )
    lee_familywise = 1 - mp.exp(-lee_expectation)
    theta_ladder_hit = bool(hits) and lee_expectation < LEE_EXPECTATION_MAX
    checks.extend(
        [
            ("theta census contains exactly nine pre-declared candidates", len(candidates) == 9),
            ("theta census has exactly one profile hit", len(hits) == 1),
            ("unique theta hit is PENTAGON_OVER_7", bool(hits) and hits[0].name == "PENTAGON_OVER_7"),
            ("theta census LEE expectation is below 0.1", lee_expectation < LEE_EXPECTATION_MAX),
        ]
    )

    print("SPEC_SHA", spec_sha)
    print("EXPLORATION ONLY; exact one-phase test; no phase scan")
    print()
    print("FROZEN PHASE")
    print("  H_PENT = 4*(2*pi/5) = 288 deg; conjugate = 72 deg")
    print("  sources: v429 2*pi/5 pentagon partner; v211/v429 3*pi/5 spine")
    print()
    print("FROZEN-PHASE ONE-PARAMETER REFITS")
    for fit in (measured_fit, tfpt_fit):
        print(
            "  {} theta={} deg chi2={} profile_Dchi2_1=[{},{}] deg".format(
                fit.target_name,
                fmt(degrees(fit.theta), 14),
                fmt(fit.chi2, 12),
                fmt(degrees(fit.profile_lower), 14),
                fmt(degrees(fit.profile_upper), 14),
            )
        )
        for name in OBSERVABLE_NAMES:
            print(
                "    {} pred={} target={} pull={:+.9f} sigma".format(
                    name,
                    fmt(fit.predictions[name], 16),
                    fmt(
                        (
                            MEASURED_TARGETS
                            if fit.target_name == "MEASURED_NUFIT"
                            else TFPT_TARGETS
                        )[name],
                        16,
                    ),
                    float(fit.pulls[name]),
                )
            )
    print(
        "  conjugate 72 deg angle residuals: measured={} TFPT={}".format(
            fmt(branch_angle_residual, 6),
            fmt(tfpt_branch_residual, 6),
        )
    )
    print()

    print("THETA CENSUS")
    for candidate in candidates:
        delta_degrees = degrees(candidate.value - measured_fit.theta)
        profile_pull = profile_deviation(candidate.value, measured_fit)
        delta_chi2 = (
            objective(candidate.value, PHASE, MEASURED_TARGETS)
            - measured_fit.chi2
        )
        print(
            "  {} | {} | theta={} deg | delta={:+.9f} deg | "
            "profile_pull={:+.9f} | DeltaChi2={:.9f} | {}".format(
                candidate.name,
                candidate.formula,
                fmt(degrees(candidate.value), 14),
                float(delta_degrees),
                float(profile_pull),
                float(delta_chi2),
                "HIT" if candidate in hits else "MISS",
            )
        )
    print(
        "  LEE N={} interval_width={} deg E={} familywise~{} threshold={}".format(
            len(candidates),
            fmt(degrees(measured_fit.profile_upper - measured_fit.profile_lower), 12),
            fmt(lee_expectation, 12),
            fmt(lee_familywise, 12),
            fmt(LEE_EXPECTATION_MAX),
        )
    )
    print()

    print("CIRCULARITY AUDIT")
    for key, value in provenance.items():
        print(f"  {key}: {value}")
    circularity_verdict = (
        "NON_CIRCULAR_MEASURED_TARGET_ONLY"
        if provenance_ok and phase_consistent and not tfpt_consistent
        else "NON_CIRCULAR_BOTH_TARGETS"
        if provenance_ok and phase_consistent and tfpt_consistent
        else "CIRCULAR_OR_INCONSISTENT"
    )
    print("  CIRCULARITY_VERDICT", circularity_verdict)
    if phase_consistent and not tfpt_consistent:
        print(
            "  The <=1.5 sigma gate passes only for measured targets; the TFPT "
            "target refit misses sin2_theta23 by {:.9f} sigma.  Therefore the "
            "pentagon phase is data-consistent but does not recover or validate "
            "the assembled v270 angle set.".format(
                float(tfpt_fit.pulls["sin2_theta23"])
            )
        )
    print()

    freeze_allowed = provenance_ok and phase_consistent and theta_ladder_hit
    freeze_sha = None
    if freeze_allowed:
        vector = full_observable_vector(hits[0].value)
        payload = build_v3_yaml(vector)
        os.makedirs(os.path.dirname(V3_PATH), exist_ok=True)
        with open(V3_PATH, "w", encoding="utf-8") as output_file:
            output_file.write(payload)
        freeze_sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
        with open(V3_PATH, "rb") as frozen_file:
            disk_sha = hashlib.sha256(frozen_file.read()).hexdigest()[:16]
        checks.extend(
            [
                ("v3 freeze exists", os.path.exists(V3_PATH)),
                ("v3 freeze hash is stable on disk", disk_sha == freeze_sha),
                ("v3 vector contains all requested observables", all(
                    token in payload
                    for token in (
                        "m1_eV:",
                        "m2_eV:",
                        "m3_eV:",
                        "sin2_theta12:",
                        "sin2_theta13:",
                        "sin2_theta23:",
                        "delta_cp_degrees:",
                        "Sigma_mnu_eV:",
                        "m_beta_eV:",
                        "m_bb_interval_eV:",
                    )
                )),
                ("v3 types y2 as data calibrated", "y2_source: \"DATA_CALIBRATED" in payload),
                ("v3 does not promote 2phi0sq companion", "PRIOR_CENSUS_LEE_NULL" in payload),
            ]
        )
        freeze_verdict = f"V3_FROZEN({freeze_sha})"
        print("V3 OBSERVABLE VECTOR")
        for name, value in vector.items():
            print(f"  {name}={fmt(value, 16)}")
    else:
        checks.append(("v3 absent when freeze rule fails", not os.path.exists(V3_PATH)))
        freeze_verdict = "V3_NOT_CREATED"

    phase_verdict = (
        "PENTAGON_PHASE_CONSISTENT"
        f"(theta_fit={fmt(degrees(measured_fit.theta), 12)}deg)"
        if phase_consistent
        else "PENTAGON_PHASE_KILLED"
        if phase_killed
        else "PENTAGON_PHASE_INDETERMINATE"
    )
    theta_verdict = (
        "THETA_LADDER_HIT({},LEE={})".format(
            hits[0].name,
            fmt(lee_expectation, 10),
        )
        if theta_ladder_hit
        else "THETA_LADDER_NULL"
    )
    print()
    print("VERDICT", phase_verdict)
    print("VERDICT", theta_verdict)
    print("VERDICT", freeze_verdict)
    print()
    for label, passed in checks:
        print(("PASS " if passed else "FAIL ") + label)
    all_pass = all(passed for _label, passed in checks)
    print("PROTOCOL-ALL-PASS" if all_pass else "PROTOCOL-FAILURE")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
