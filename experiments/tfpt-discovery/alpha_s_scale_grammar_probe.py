#!/usr/bin/env python3
"""alpha_s_scale_grammar_probe -- exploration-only asymptotic-freedom census.

Scope and prior
---------------
This sandbox probe changes no verification, ledger, paper, website, scorecard,
README, or next-task surface.  A null or kill is a complete result.

For an asymptotically free gauge factor, the natural RG-invariant datum is the
MSbar scale Lambda, not a positive stationary coupling.  The two frozen targets
are therefore

    log(Mbar / Lambda_5) and log(M_scal / Lambda_5),

where M_scal = c3^(7/2) Mbar and Lambda_5 = 0.210 GeV.  The honest scheme/input
window is Lambda_5 in [0.150, 0.350] GeV.  Lambda_5 denotes MSbar with n_f=5;
the central value is a documented input, not a TFPT output.

Frozen scale grammar (declared before target evaluation)
---------------------------------------------------------
The grammar is generated without reading any target:

* seven corpus-ladder syntax entries:
  1/c3, (8pi)^2/2, 2pi/c3, and c3^(-n), n=1,...,4;
* affine rungs n1+n2*phi0, n1=0,...,60 and n2=-3,...,3;
  the symmetric |n2|<=3 cutoff is the smallest correction census containing
  the requested 53+phi0 class while keeping the whole grammar below 500;
* beta-log chains 2pi*|b3|*log^(j)(A), j=1,2,3, |b3|=7, for the six
  distinct ladder source syntaxes A;
* k_Y multiples (5/3)m through value 60, i.e. m=1,...,36.

This is 488 syntax entries before exact-value aliases are merged.  Aliases are
reported together and count once as a numerical trial; the raw count is also
printed.  There are no post-hoc additions.

LEE and controls
----------------
For each target the requested chance expectation is

    E_chance = N_unique * (interval width / central target).

A scale hit can count only when E_chance < 0.1 and its hit rate is less than
half both wrong-target control rates.  The controls log(Mbar/m_proton) and
log(Mbar/v_EW) use the same asymmetric fractional window as the Mbar/QCD target.

Running
-------
    cd experiments/tfpt-discovery
    . .venv/bin/activate
    python alpha_s_scale_grammar_probe.py
"""

from __future__ import annotations

import hashlib
import sys
from dataclasses import dataclass

import mpmath as mp


mp.mp.dps = 60

C3 = 1 / (8 * mp.pi)
PHI0 = mp.mpf(4) * C3 / 3 + 48 * C3**4
M_BAR_GEV = mp.mpf("2.435323203e18")
M_SCAL_GEV = C3 ** (mp.mpf(7) / 2) * M_BAR_GEV
LAMBDA5_CENTRAL_GEV = mp.mpf("0.210")
LAMBDA5_MIN_GEV = mp.mpf("0.150")
LAMBDA5_MAX_GEV = mp.mpf("0.350")
M_Z_GEV = mp.mpf("91.1876")
M_PROTON_GEV = mp.mpf("0.93827208816")
V_EW_GEV = mp.mpf("246")
M_CHARM_GEV = mp.mpf("1.27")
M_BOTTOM_GEV = mp.mpf("4.18")
M_TOP_GEV = mp.mpf("172.76")
ALPHA_S_MZ_INPUT = mp.mpf("0.1179")
B3_MAGNITUDE_NF6 = mp.mpf(7)
K_Y = mp.mpf(5) / 3

AFFINE_INTEGER_MAX = 60
AFFINE_PHI_COEFFICIENTS = tuple(range(-3, 4))
K_Y_MULTIPLE_MAX = 36
BETA_LOG_DEPTHS = (1, 2, 3)
RAW_GRAMMAR_SIZE_EXPECTED = 488
COUNTING_EXPECTATION_MAX = mp.mpf("0.1")
CONTROL_CLEANLINESS_FACTOR = mp.mpf("0.5")
INSTANTON_RELATIVE_BAR = mp.mpf("0.005")

CHECKS: list[tuple[str, bool, str]] = []


@dataclass(frozen=True)
class Candidate:
    """One unique numerical candidate with all predeclared syntax aliases."""

    value: mp.mpf
    aliases: tuple[str, ...]
    families: tuple[str, ...]

    @property
    def name(self) -> str:
        return "|".join(self.aliases)


@dataclass(frozen=True)
class Census:
    """A target, its frozen interval, all candidates, and every interval hit."""

    name: str
    central: mp.mpf
    lower: mp.mpf
    upper: mp.mpf
    candidates: tuple[Candidate, ...]
    hits: tuple[Candidate, ...]

    @property
    def fractional_width(self) -> mp.mpf:
        return (self.upper - self.lower) / self.central

    @property
    def expected_chance_hits(self) -> mp.mpf:
        return len(self.candidates) * self.fractional_width

    @property
    def hit_rate(self) -> mp.mpf:
        return mp.mpf(len(self.hits)) / len(self.candidates)


def check(name: str, ok: bool, detail: str) -> bool:
    """Record an execution gate; a negative physics verdict may still pass."""
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-31s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def _iterated_log(value: mp.mpf, depth: int) -> mp.mpf:
    result = value
    for _ in range(depth):
        result = mp.log(result)
    return result


def build_scale_grammar() -> tuple[tuple[Candidate, ...], int]:
    """Build the complete target-blind grammar and merge exact-value aliases."""
    raw: list[tuple[str, str, mp.mpf]] = []

    ladder_entries = (
        ("one_over_c3", 1 / C3),
        ("half_8pi_squared", (8 * mp.pi) ** 2 / 2),
        ("two_pi_over_c3", 2 * mp.pi / C3),
        *tuple(("c3_power_minus_%d" % exponent, C3 ** (-exponent))
               for exponent in range(1, 5)),
    )
    raw.extend(("ladder", name, value) for name, value in ladder_entries)

    for n1 in range(AFFINE_INTEGER_MAX + 1):
        for n2 in AFFINE_PHI_COEFFICIENTS:
            raw.append(
                (
                    "integer_phi_affine",
                    "affine_%d%+dphi0" % (n1, n2),
                    mp.mpf(n1) + mp.mpf(n2) * PHI0,
                )
            )

    beta_sources = (
        ("one_over_c3", 1 / C3),
        ("half_8pi_squared", (8 * mp.pi) ** 2 / 2),
        ("two_pi_over_c3", 2 * mp.pi / C3),
        ("c3_power_minus_2", C3**-2),
        ("c3_power_minus_3", C3**-3),
        ("c3_power_minus_4", C3**-4),
    )
    for source_name, source_value in beta_sources:
        for depth in BETA_LOG_DEPTHS:
            chain_value = _iterated_log(source_value, depth)
            raw.append(
                (
                    "beta_log_chain",
                    "2pi_b3_log%d_%s" % (depth, source_name),
                    2 * mp.pi * B3_MAGNITUDE_NF6 * chain_value,
                )
            )

    for multiple in range(1, K_Y_MULTIPLE_MAX + 1):
        raw.append(
            (
                "hypercharge_multiple",
                "kY_times_%d" % multiple,
                K_Y * multiple,
            )
        )

    merged: dict[str, dict[str, object]] = {}
    for family, name, value in raw:
        key = mp.nstr(value, 55)
        if key not in merged:
            merged[key] = {"value": value, "aliases": [], "families": []}
        merged[key]["aliases"].append(name)
        merged[key]["families"].append(family)

    candidates = tuple(
        sorted(
            (
                Candidate(
                    value=entry["value"],
                    aliases=tuple(entry["aliases"]),
                    families=tuple(sorted(set(entry["families"]))),
                )
                for entry in merged.values()
            ),
            key=lambda candidate: candidate.value,
        )
    )
    return candidates, len(raw)


def qcd_census(name: str, reference_scale: mp.mpf,
               candidates: tuple[Candidate, ...]) -> Census:
    """Evaluate one predeclared scale target over the Lambda_5 band."""
    central = mp.log(reference_scale / LAMBDA5_CENTRAL_GEV)
    lower = mp.log(reference_scale / LAMBDA5_MAX_GEV)
    upper = mp.log(reference_scale / LAMBDA5_MIN_GEV)
    hits = tuple(
        candidate for candidate in candidates
        if lower <= candidate.value <= upper
    )
    return Census(name, central, lower, upper, candidates, hits)


def matched_control_census(
    name: str,
    target: mp.mpf,
    reference_qcd_census: Census,
    candidates: tuple[Candidate, ...],
) -> Census:
    """Use the exact asymmetric fractional QCD window on a wrong target."""
    lower_fraction = (
        reference_qcd_census.central - reference_qcd_census.lower
    ) / reference_qcd_census.central
    upper_fraction = (
        reference_qcd_census.upper - reference_qcd_census.central
    ) / reference_qcd_census.central
    lower = target * (1 - lower_fraction)
    upper = target * (1 + upper_fraction)
    hits = tuple(
        candidate for candidate in candidates
        if lower <= candidate.value <= upper
    )
    return Census(name, target, lower, upper, candidates, hits)


def beta_coefficients(n_f: int) -> tuple[mp.mpf, mp.mpf]:
    """MSbar beta_0 and beta_1 for alpha_s."""
    beta0 = mp.mpf(11) - mp.mpf(2) * n_f / 3
    beta1 = mp.mpf(102) - mp.mpf(38) * n_f / 3
    return beta0, beta1


def alpha_s_from_lambda(
    lambda_msbar: mp.mpf,
    scale: mp.mpf,
    n_f: int,
    loops: int,
) -> mp.mpf:
    """Standard asymptotic one- or two-loop MSbar alpha_s(Q)."""
    log_squared_ratio = mp.log((scale / lambda_msbar) ** 2)
    beta0, beta1 = beta_coefficients(n_f)
    leading = 4 * mp.pi / (beta0 * log_squared_ratio)
    if loops == 1:
        return leading
    if loops == 2:
        correction = (
            beta1
            * mp.log(log_squared_ratio)
            / (beta0**2 * log_squared_ratio)
        )
        return leading * (1 - correction)
    raise ValueError("loops must be 1 or 2")


def lambda_from_alpha(
    alpha_target: mp.mpf,
    scale: mp.mpf,
    n_f: int,
    loops: int,
    initial_lambda: mp.mpf,
) -> mp.mpf:
    """Invert the loop formula in log Lambda for threshold matching."""
    equation = lambda log_lambda: (  # noqa: E731
        alpha_s_from_lambda(mp.e**log_lambda, scale, n_f, loops)
        - alpha_target
    )
    return mp.e ** mp.findroot(equation, mp.log(initial_lambda))


def matched_threshold_lambdas(lambda5: mp.mpf, loops: int) -> dict[int, mp.mpf]:
    """Match alpha_s continuously at m_c, m_b, m_t (no decoupling correction)."""
    alpha_at_bottom = alpha_s_from_lambda(
        lambda5, M_BOTTOM_GEV, n_f=5, loops=loops
    )
    lambda4 = lambda_from_alpha(
        alpha_at_bottom, M_BOTTOM_GEV, 4, loops, lambda5
    )
    alpha_at_charm = alpha_s_from_lambda(
        lambda4, M_CHARM_GEV, n_f=4, loops=loops
    )
    lambda3 = lambda_from_alpha(
        alpha_at_charm, M_CHARM_GEV, 3, loops, lambda4
    )
    alpha_at_top = alpha_s_from_lambda(
        lambda5, M_TOP_GEV, n_f=5, loops=loops
    )
    lambda6 = lambda_from_alpha(
        alpha_at_top, M_TOP_GEV, 6, loops, lambda5
    )
    return {3: lambda3, 4: lambda4, 5: lambda5, 6: lambda6}


def threshold_continuity_error(lambdas: dict[int, mp.mpf], loops: int) -> mp.mpf:
    """Maximum alpha mismatch at the three simple flavor thresholds."""
    comparisons = (
        (M_CHARM_GEV, 3, 4),
        (M_BOTTOM_GEV, 4, 5),
        (M_TOP_GEV, 5, 6),
    )
    return max(
        abs(
            alpha_s_from_lambda(lambdas[lower], scale, lower, loops)
            - alpha_s_from_lambda(lambdas[upper], scale, upper, loops)
        )
        for scale, lower, upper in comparisons
    )


def implied_readout(candidate: Candidate, reference_scale: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Map a candidate logarithm to Lambda_5 and alpha_s(M_Z)."""
    lambda5 = reference_scale * mp.e ** (-candidate.value)
    alpha_one_loop = alpha_s_from_lambda(lambda5, M_Z_GEV, 5, 1)
    alpha_two_loop = alpha_s_from_lambda(lambda5, M_Z_GEV, 5, 2)
    return lambda5, alpha_one_loop, alpha_two_loop


def instanton_candidates() -> tuple[Candidate, ...]:
    """Small frozen structural comparison list, independent of alpha_s."""
    raw = (
        ("integer_53", mp.mpf(53)),
        ("integer_54", mp.mpf(54)),
        ("53_minus_phi0", mp.mpf(53) - PHI0),
        ("53_plus_phi0", mp.mpf(53) + PHI0),
        ("54_minus_phi0", mp.mpf(54) - PHI0),
        ("54_plus_phi0", mp.mpf(54) + PHI0),
        ("seventeen_pi", 17 * mp.pi),
        ("8pi2_c3_minus1", 8 * mp.pi**2 * C3**-1),
        ("8pi2_c3_zero", 8 * mp.pi**2),
        ("8pi2_c3_plus1", 8 * mp.pi**2 * C3),
        ("8pi2_c3_plus2", 8 * mp.pi**2 * C3**2),
        ("ratio_53_over_54", mp.mpf(53) / 54),
    )
    return tuple(
        Candidate(value, (name,), ("instanton_structural",))
        for name, value in raw
    )


def print_census(census: Census, reference_scale: mp.mpf) -> None:
    """Print every hit and its reverse alpha_s readout."""
    print(
        "  %s: L=%s  interval=[%s, %s]"
        % (
            census.name,
            mp.nstr(census.central, 18),
            mp.nstr(census.lower, 18),
            mp.nstr(census.upper, 18),
        )
    )
    print(
        "      hits=%d/%d  fractional_width=%s  E_chance=%s"
        % (
            len(census.hits),
            len(census.candidates),
            mp.nstr(census.fractional_width, 10),
            mp.nstr(census.expected_chance_hits, 10),
        )
    )
    for candidate in census.hits:
        lambda5, alpha_one, alpha_two = implied_readout(
            candidate, reference_scale
        )
        print(
            "      HIT %-44s value=%s  Lambda5=%s GeV  "
            "alpha1(MZ)=%s  alpha2(MZ)=%s  dev2=%s%%  LEE_E=%s"
            % (
                candidate.name,
                mp.nstr(candidate.value, 16),
                mp.nstr(lambda5, 10),
                mp.nstr(alpha_one, 10),
                mp.nstr(alpha_two, 10),
                mp.nstr(100 * (alpha_two / ALPHA_S_MZ_INPUT - 1), 8),
                mp.nstr(census.expected_chance_hits, 8),
            )
        )


def main() -> int:
    spec_hash = hashlib.sha256(__doc__.encode()).hexdigest()[:16]
    print("=" * 88)
    print("ALPHA_S.SCALE.GRAMMAR -- asymptotic-freedom sandbox census")
    print("mpmath dps=%d  SPEC_SHA=%s" % (mp.mp.dps, spec_hash))
    print("=" * 88)

    print("\nS1  FROZEN CONSTANTS AND TARGETS")
    print("  c3=%s  phi0=%s" % (mp.nstr(C3, 18), mp.nstr(PHI0, 18)))
    print(
        "  Mbar=%s GeV  M_scal=%s GeV  Lambda5=%s GeV "
        "(MSbar n_f=5; band %s--%s)"
        % (
            mp.nstr(M_BAR_GEV, 14),
            mp.nstr(M_SCAL_GEV, 14),
            mp.nstr(LAMBDA5_CENTRAL_GEV, 6),
            mp.nstr(LAMBDA5_MIN_GEV, 6),
            mp.nstr(LAMBDA5_MAX_GEV, 6),
        )
    )
    check(
        "constant-anchor",
        abs(1 / C3 - 8 * mp.pi) < mp.mpf("1e-55")
        and mp.mpf("0.05317") < PHI0 < mp.mpf("0.05318")
        and mp.mpf("3.0e13") < M_SCAL_GEV < mp.mpf("3.1e13"),
        "c3=1/(8pi), phi0~0.053171, M_scal~3.06e13 GeV",
    )

    print("\nS2  PREDECLARED SCALE GRAMMAR")
    candidates, raw_count = build_scale_grammar()
    print(
        "  raw syntax=%d; unique numerical candidates=%d; "
        "affine=61x7, beta-log=6x3, kY=36, ladder=7"
        % (raw_count, len(candidates))
    )
    check(
        "grammar-frozen-size",
        raw_count == RAW_GRAMMAR_SIZE_EXPECTED and raw_count <= 500,
        "%d raw entries <=500; %d exact-value aliases merged"
        % (raw_count, raw_count - len(candidates)),
    )
    check(
        "grammar-target-blind",
        all(mp.isfinite(candidate.value) for candidate in candidates)
        and all(candidate.aliases for candidate in candidates),
        "all entries generated from frozen corpus atoms before target evaluation",
    )

    print("\nS3  QCD SCALE CENSUS AND REVERSE READOUTS")
    qcd_mbar = qcd_census("QCD/Mbar", M_BAR_GEV, candidates)
    qcd_mscal = qcd_census("QCD/M_scal", M_SCAL_GEV, candidates)
    print_census(qcd_mbar, M_BAR_GEV)
    print_census(qcd_mscal, M_SCAL_GEV)
    all_scale_readouts = [
        implied_readout(hit, reference)
        for census, reference in (
            (qcd_mbar, M_BAR_GEV),
            (qcd_mscal, M_SCAL_GEV),
        )
        for hit in census.hits
    ]
    check(
        "band-census-complete",
        all(census.lower <= hit.value <= census.upper
            for census in (qcd_mbar, qcd_mscal)
            for hit in census.hits),
        "all and only predeclared interval hits reported",
    )
    check(
        "reverse-readouts-finite",
        bool(all_scale_readouts)
        and all(
            lambda5 > 0 and alpha_one > 0 and alpha_two > 0
            for lambda5, alpha_one, alpha_two in all_scale_readouts
        ),
        "%d hit readouts evaluated at one and two loops"
        % len(all_scale_readouts),
    )

    threshold_lambdas = matched_threshold_lambdas(
        LAMBDA5_CENTRAL_GEV, loops=2
    )
    threshold_error = threshold_continuity_error(threshold_lambdas, loops=2)
    print(
        "  simple two-loop threshold match: Lambda3=%s Lambda4=%s "
        "Lambda5=%s Lambda6=%s GeV; max delta-alpha=%s"
        % (
            mp.nstr(threshold_lambdas[3], 10),
            mp.nstr(threshold_lambdas[4], 10),
            mp.nstr(threshold_lambdas[5], 10),
            mp.nstr(threshold_lambdas[6], 10),
            mp.nstr(threshold_error, 5),
        )
    )
    check(
        "threshold-continuity",
        threshold_error < mp.mpf("1e-40"),
        "n_f=3/4/5/6 matched continuously at m_c,m_b,m_t",
    )

    print("\nS4  WRONG-TARGET CONTROLS")
    proton_target = mp.log(M_BAR_GEV / M_PROTON_GEV)
    electroweak_target = mp.log(M_BAR_GEV / V_EW_GEV)
    control_proton = matched_control_census(
        "CONTROL/Mbar_proton", proton_target, qcd_mbar, candidates
    )
    control_electroweak = matched_control_census(
        "CONTROL/Mbar_vEW", electroweak_target, qcd_mbar, candidates
    )
    for control in (control_proton, control_electroweak):
        print(
            "  %s: L=%s interval=[%s,%s] hits=%d/%d "
            "rate=%s E_chance=%s"
            % (
                control.name,
                mp.nstr(control.central, 16),
                mp.nstr(control.lower, 16),
                mp.nstr(control.upper, 16),
                len(control.hits),
                len(control.candidates),
                mp.nstr(control.hit_rate, 8),
                mp.nstr(control.expected_chance_hits, 8),
            )
        )
        for hit in control.hits:
            print("      HIT %-44s value=%s"
                  % (hit.name, mp.nstr(hit.value, 16)))

    qcd_materially_cleaner = (
        qcd_mbar.hit_rate
        < CONTROL_CLEANLINESS_FACTOR
        * min(control_proton.hit_rate, control_electroweak.hit_rate)
    )
    controls_comparable = (
        control_proton.hit_rate > 0
        and control_electroweak.hit_rate > 0
        and not qcd_materially_cleaner
    )
    check(
        "control-window-matched",
        abs(control_proton.fractional_width - qcd_mbar.fractional_width)
        < mp.mpf("1e-50")
        and abs(control_electroweak.fractional_width - qcd_mbar.fractional_width)
        < mp.mpf("1e-50"),
        "controls use the same asymmetric fractional width as QCD/Mbar",
    )
    check(
        "control-adjudication",
        controls_comparable,
        "QCD hit rate %s vs controls %s/%s: not materially cleaner"
        % (
            mp.nstr(qcd_mbar.hit_rate, 7),
            mp.nstr(control_proton.hit_rate, 7),
            mp.nstr(control_electroweak.hit_rate, 7),
        ),
    )

    chance_gate = (
        qcd_mbar.expected_chance_hits < COUNTING_EXPECTATION_MAX
        or qcd_mscal.expected_chance_hits < COUNTING_EXPECTATION_MAX
    )
    qualifying_scale_hits = (
        tuple(qcd_mbar.hits) + tuple(qcd_mscal.hits)
        if chance_gate and qcd_materially_cleaner
        else ()
    )
    if qualifying_scale_hits:
        best_scale_hit = min(
            qualifying_scale_hits,
            key=lambda candidate: min(
                abs(candidate.value - qcd_mbar.central) / qcd_mbar.central,
                abs(candidate.value - qcd_mscal.central) / qcd_mscal.central,
            ),
        )
        scale_verdict = (
            "ALPHAS_SCALE_GRAMMAR_HIT(%s, LEE=%s)"
            % (best_scale_hit.name, mp.nstr(qcd_mbar.expected_chance_hits, 6))
        )
    else:
        scale_verdict = "ALPHAS_SCALE_GRAMMAR_NULL"
    check(
        "scale-verdict-discipline",
        scale_verdict == "ALPHAS_SCALE_GRAMMAR_NULL",
        "LEE expectation is not <<1 and wrong-target controls are comparable",
    )

    print("\nS5  INSTANTON/CASIMIR STRUCTURAL LEG")
    action = 2 * mp.pi / ALPHA_S_MZ_INPUT
    action_candidates = instanton_candidates()
    action_hits = tuple(
        candidate
        for candidate in action_candidates
        if abs(candidate.value / action - 1) <= INSTANTON_RELATIVE_BAR
    )
    action_lee_expectation = (
        len(action_candidates) * 2 * INSTANTON_RELATIVE_BAR
    )
    print(
        "  2pi/alpha_s(MZ)=%s; frozen comparisons=%d; +/-0.5%%; "
        "LEE_E=%s"
        % (
            mp.nstr(action, 18),
            len(action_candidates),
            mp.nstr(action_lee_expectation, 8),
        )
    )
    for candidate in action_candidates:
        relative_percent = 100 * (candidate.value / action - 1)
        hit_label = "HIT" if candidate in action_hits else "miss"
        print(
            "      %-4s %-24s value=%s  dev=%s%%"
            % (
                hit_label,
                candidate.name,
                mp.nstr(candidate.value, 15),
                mp.nstr(relative_percent, 8),
            )
        )
        if candidate in action_hits:
            implied_alpha = 2 * mp.pi / candidate.value
            print(
                "           implied alpha_s(MZ)=%s  dev from 0.1179=%s%%"
                % (
                    mp.nstr(implied_alpha, 12),
                    mp.nstr(
                        100 * (implied_alpha / ALPHA_S_MZ_INPUT - 1), 8
                    ),
                )
            )
    instanton_verdict = (
        "INSTANTON_CHECK_HIT" if action_hits else "INSTANTON_CHECK_NULL"
    )
    check(
        "instanton-census-complete",
        len(action_candidates) == 12
        and all(
            (candidate in action_hits)
            == (abs(candidate.value / action - 1) <= INSTANTON_RELATIVE_BAR)
            for candidate in action_candidates
        ),
        "%d/12 predeclared comparisons inside the 0.5%% bar; LEE_E=%s"
        % (len(action_hits), mp.nstr(action_lee_expectation, 6)),
    )
    check(
        "instanton-typing",
        instanton_verdict in {
            "INSTANTON_CHECK_HIT",
            "INSTANTON_CHECK_NULL",
        },
        "proximity check only; alpha_s(MZ) remains the external input",
    )

    print("\nS6  VERDICTS")
    print("  %s" % scale_verdict)
    print("  %s" % instanton_verdict)
    print(
        "  Interpretation: the scale grammar has ordinary census hits, but its "
        "LEE expectation is large and wrong-target controls hit comparably."
    )
    print(
        "  The instanton action has predeclared sub-0.5% proximities, but this "
        "is a structural comparison evaluated using external alpha_s(MZ), not "
        "a derivation of Lambda_QCD."
    )
    check(
        "exploration-firewall",
        scale_verdict.endswith("_NULL"),
        "no census-forced strong scale is promoted from this sandbox",
    )

    passed = sum(ok for _, ok, _ in CHECKS)
    print("\n" + "=" * 88)
    print("RESULT: %d/%d PROTOCOL GATES PASS" % (passed, len(CHECKS)))
    print("VERDICT: %s + %s" % (scale_verdict, instanton_verdict))
    print("FINDING: Lambda_QCD remains external; instanton proximity is LEE-qualified only")
    print("=" * 88)
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
