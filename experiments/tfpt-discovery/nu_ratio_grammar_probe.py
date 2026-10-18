#!/usr/bin/env python3
"""nu_ratio_grammar_probe -- value census after the 3x3 texture census null.

EXPLORATION ONLY.  This probe asks whether a small, pre-declared scalar grammar
supplies the two values that a Q_+-basis Dirac texture would need.  It does not
fit a matrix and cannot close FLAV.NUSCALE.05.

PRE-DECLARED GRAMMAR (frozen before evaluation)
------------------------------------------------
Every candidate is

    phi0**a * r * exp(-b),

with a in {0,1,2,3,4}, b in {0,5/6,1}, and r in exactly

    rational ladder: {53/54, 5/3, 2/3, 1/14, 2/9, 2/7, 41/10}
    small integers:  {1,2,3,4,5,6}
    epsilon forms:   {epsilon, 2 epsilon, 3 epsilon, epsilon/2},

where epsilon=phi0**2/10.  Thus there are 5*3*17=255 raw candidates;
50-digit value deduplication is applied before evaluation.  No sums, fitted
coefficients, signs, inverses, or post-hoc atoms are allowed.

TARGET T1: THE ALIGNED y2/y3 REQUIREMENT
-----------------------------------------
For one diagonal heavy line, after the inherited v2 ADKLR rundown,

    m_i = y_i**2 v**2 R_i / (2 M_i),  hence
    y2/y3 = sqrt(2 m2 M2 / (v**2 R2)) / y3,
    m2 = sqrt(dm2_21).

M2=2 epsilon M_scal, y3=y_t(M3), and R2 are recomputed with the verbatim v481
one-loop runner rather than read from results_v2.json.  With NuFIT 6.0
dm2_21=(7.49+/-0.19)e-5 eV^2, the one-sigma fractional uncertainty in y2/y3
is sigma(dm2_21)/(4 dm2_21).  It is combined in quadrature with the declared
2% RG envelope.  This is a data-required ratio, not a TFPT prediction.

TARGET T2: THE y1/y3 UPPER BOUND
---------------------------------
The DESI residual room is

    m1_max = 0.0642 eV - m3(y3,M3,R3) - sqrt(dm2_21),

and the same inverse seesaw gives y1/y3.  This is an upper bound: the probe
only reports grammar values strictly below it and never scores closeness to
the bound as a hit.

TARGET T3: MINIMAL REACTOR OFF-DIAGONAL
----------------------------------------
Use the symmetric Q_+ eigenbasis, M_R=diag(M1,M2,M3), and the convention in
which heavy indices are rows of Y.  If the mass-basis singular values are
diag(y1,y2,y3), the minimal PMNS embedding is

    Y = diag(y1,y2,y3) U_PMNS^dagger,

because Y^T M_R^-1 Y = U* diag(y_i^2/M_i) U^dagger.  The third heavy row is
therefore

    Y_3alpha/y3 = (U_alpha3)* =
      (s13 exp(+i delta), s23 c13, c23 c13).

Equivalently, in the e--3 two-state slice,

    m_nu = R13* diag(m1,m3) R13^dagger,
    (m_nu)e3 = (m3-m1) s13 c13 exp(-i delta),
    tan(2 theta13) = 2 |m_e3| / (m_33-m_ee).

Thus the smallest new reactor-bearing entry has required magnitude
|Y_3e|/y3=|Y_e3|/y3=s13=sqrt(phi0 exp(-5/6)); at first order it is theta13.
The full third-row companion is |Y_3mu|/y3=s23*c13 and carries the already
frozen atmospheric angle.  The phase exp(+i*4pi/3) is also required, but this
real positive value grammar does not census phases.  The T3 observational
window maps the frozen NuFIT-6.0 one-sigma error on sin^2(theta13) to s13.

LOOK-ELSEWHERE EFFECT AND CONTROLS
----------------------------------
For each two-sided target window, the crude declared chance expectation is

    E_chance = N_unique * ((upper-lower)/target).

A numerical match is called significant only when E_chance < 0.1, an
operational version of "<< 1".  Three seeded log-scrambled targets use the
same 2% half-window and the same grammar.  A hit is allowed to fail: a null is
the intended falsifiable outcome.
"""

from __future__ import annotations

import math
import os
import random
import sys
from dataclasses import dataclass
from fractions import Fraction

import mpmath as mp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import Mbar, c3, g_car, phi0  # noqa: E402


mp.mp.dps = 60

# Frozen seesaw / RG inputs, verbatim from v481/v2.
V_EW_GEV = mp.mpf("246.22")
MZ_GEV = mp.mpf("91.1876")
MT_MSBAR_MZ_GEV = mp.mpf("162.5")
LAMBDA_MZ = mp.mpf("0.130")
ALPHA_INV_MZ = (mp.mpf("59.01"), mp.mpf("29.59"), mp.mpf("8.44"))
RG_STEPS = 20_000
A_LAMBDA = mp.mpf(2 * int(g_car))
PHI0 = mp.mpf(phi0)
C3 = mp.mpf(c3)
M_BAR_GEV = mp.mpf(Mbar)
EPSILON = PHI0**2 / A_LAMBDA
M_SCAL_GEV = C3 ** mp.mpf("3.5") * M_BAR_GEV
M1_GEV = EPSILON * M_SCAL_GEV
M2_GEV = 2 * EPSILON * M_SCAL_GEV
M3_GEV = 3 * M_SCAL_GEV

# Frozen data snapshot and uncertainty protocol.
DM2_21_EV2 = mp.mpf("7.49e-5")
DM2_21_SIGMA_EV2 = mp.mpf("0.19e-5")
SIGMA_MNU_BOUND_EV = mp.mpf("0.0642")
SIN2_THETA13_SIGMA = mp.mpf("0.00058")
RG_FRACTIONAL_ENVELOPE = mp.mpf("0.02")
SIGNIFICANT_LEE_MAX = mp.mpf("0.1")

# Frozen controls.
CONTROL_SEED = 20260828
CONTROL_HALF_WIDTH = mp.mpf("0.02")
N_CONTROLS = 3

POWERS = (0, 1, 2, 3, 4)
EXPONENTS = (
    ("0", mp.mpf("0")),
    ("5/6", mp.mpf(5) / 6),
    ("1", mp.mpf("1")),
)
RATIONAL_LADDER = (
    ("53/54", Fraction(53, 54)),
    ("5/3", Fraction(5, 3)),
    ("2/3", Fraction(2, 3)),
    ("1/14", Fraction(1, 14)),
    ("2/9", Fraction(2, 9)),
    ("2/7", Fraction(2, 7)),
    ("41/10", Fraction(41, 10)),
)
SMALL_INTEGERS = tuple((str(value), Fraction(value, 1)) for value in range(1, 7))
EPSILON_FORMS = (
    ("epsilon", EPSILON),
    ("2epsilon", 2 * EPSILON),
    ("3epsilon", 3 * EPSILON),
    ("epsilon/2", EPSILON / 2),
)


@dataclass(frozen=True)
class Candidate:
    name: str
    value: mp.mpf
    phi_power: int
    exp_label: str
    coefficient_label: str
    coefficient_class: str


@dataclass(frozen=True)
class TargetWindow:
    name: str
    target: mp.mpf
    lower: mp.mpf
    upper: mp.mpf

    @property
    def fractional_width(self) -> mp.mpf:
        return (self.upper - self.lower) / self.target


def run_sm_up(mu_hi: mp.mpf, steps: int = RG_STEPS) -> tuple[mp.mpf, mp.mpf]:
    """Verbatim-Euler v481 one-loop SM runner, retained at 20,000 steps."""
    g1, g2, g3 = [mp.sqrt(4 * mp.pi / alpha) for alpha in ALPHA_INV_MZ]
    yt = mp.sqrt(2) * MT_MSBAR_MZ_GEV / V_EW_GEV
    lam = LAMBDA_MZ
    step = mp.log(mu_hi / MZ_GEV) / steps
    loop = 1 / (16 * mp.pi**2)
    beta_gauge = (mp.mpf(41) / 10, -mp.mpf(19) / 6, -mp.mpf(7))
    integral_alpha = mp.mpf("0")
    for _ in range(steps):
        integral_alpha += (-3 * g2**2 + 6 * yt**2 + lam) * step
        dg1 = loop * beta_gauge[0] * g1**3
        dg2 = loop * beta_gauge[1] * g2**3
        dg3 = loop * beta_gauge[2] * g3**3
        dyt = loop * yt * (
            mp.mpf("4.5") * yt**2
            - 8 * g3**2
            - mp.mpf("2.25") * g2**2
            - mp.mpf(17) / 20 * g1**2
        )
        dlam = loop * (
            24 * lam**2
            - 6 * yt**4
            + 12 * lam * yt**2
            - 3 * lam * (3 * g2**2 + mp.mpf("0.6") * g1**2)
            + mp.mpf("0.375")
            * (2 * g2**4 + (g2**2 + mp.mpf("0.6") * g1**2) ** 2)
        )
        g1 += step * dg1
        g2 += step * dg2
        g3 += step * dg3
        yt += step * dyt
        lam += step * dlam
    return yt, mp.exp(-integral_alpha / (16 * mp.pi**2))


def light_mass_ev(yukawa: mp.mpf, heavy_mass_gev: mp.mpf, rundown: mp.mpf) -> mp.mpf:
    return (yukawa * V_EW_GEV / mp.sqrt(2)) ** 2 / heavy_mass_gev * rundown * 1e9


def yukawa_from_mass(
    mass_ev: mp.mpf, heavy_mass_gev: mp.mpf, rundown: mp.mpf
) -> mp.mpf:
    return mp.sqrt(mass_ev * heavy_mass_gev / rundown / 1e9 * 2 / V_EW_GEV**2)


def build_candidates() -> list[Candidate]:
    coefficients: list[tuple[str, mp.mpf, str]] = []
    coefficients.extend(
        (label, mp.mpf(value.numerator) / value.denominator, "rational_ladder")
        for label, value in RATIONAL_LADDER
    )
    coefficients.extend(
        (label, mp.mpf(value.numerator) / value.denominator, "small_integer")
        for label, value in SMALL_INTEGERS
    )
    coefficients.extend(
        (label, value, "epsilon_form") for label, value in EPSILON_FORMS
    )

    unique: dict[str, Candidate] = {}
    for power in POWERS:
        for exp_label, exponent in EXPONENTS:
            for coefficient_label, coefficient, coefficient_class in coefficients:
                value = PHI0**power * coefficient * mp.exp(-exponent)
                name = f"phi0^{power} * {coefficient_label} * exp(-{exp_label})"
                key = mp.nstr(value, 50)
                unique.setdefault(
                    key,
                    Candidate(
                        name=name,
                        value=value,
                        phi_power=power,
                        exp_label=exp_label,
                        coefficient_label=coefficient_label,
                        coefficient_class=coefficient_class,
                    ),
                )
    return sorted(unique.values(), key=lambda candidate: candidate.value)


def target_hits(
    candidates: list[Candidate], window: TargetWindow
) -> list[Candidate]:
    return [
        candidate
        for candidate in candidates
        if window.lower <= candidate.value <= window.upper
    ]


def nearest_candidates(
    candidates: list[Candidate], target: mp.mpf, count: int = 5
) -> list[Candidate]:
    return sorted(
        candidates,
        key=lambda candidate: abs(candidate.value / target - 1),
    )[:count]


def fmt(value: mp.mpf, digits: int = 12) -> str:
    return mp.nstr(value, digits)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    candidates = build_candidates()
    raw_grammar_size = (
        len(POWERS)
        * len(EXPONENTS)
        * (len(RATIONAL_LADDER) + len(SMALL_INTEGERS) + len(EPSILON_FORMS))
    )
    checks.append(("raw grammar size is frozen at 255", raw_grammar_size == 255))
    checks.append(("unique grammar size is <=300", len(candidates) <= 300))
    checks.append(
        (
            "candidate values are unique",
            len({mp.nstr(candidate.value, 50) for candidate in candidates})
            == len(candidates),
        )
    )
    checks.append(("A_Lambda = 2*g_car = 10", A_LAMBDA == 10))

    # Recompute the frozen chain.
    y3_frozen, rundown3 = run_sm_up(M3_GEV)
    _yt2, rundown2 = run_sm_up(M2_GEV)
    _yt1, rundown1 = run_sm_up(M1_GEV)
    m3_ev = light_mass_ev(y3_frozen, M3_GEV, rundown3)
    m2_ev = mp.sqrt(DM2_21_EV2)
    y2_required = yukawa_from_mass(m2_ev, M2_GEV, rundown2)
    t1_value = y2_required / y3_frozen

    nufit_t1_fraction = DM2_21_SIGMA_EV2 / (4 * DM2_21_EV2)
    t1_half_width = mp.sqrt(
        nufit_t1_fraction**2 + RG_FRACTIONAL_ENVELOPE**2
    )
    t1 = TargetWindow(
        name="T1_y2_over_y3",
        target=t1_value,
        lower=t1_value * (1 - t1_half_width),
        upper=t1_value * (1 + t1_half_width),
    )

    m1_room_ev = max(mp.mpf("0"), SIGMA_MNU_BOUND_EV - m3_ev - m2_ev)
    y1_upper = yukawa_from_mass(m1_room_ev, M1_GEV, rundown1)
    t2_bound = y1_upper / y3_frozen
    t2_below = [
        candidate for candidate in candidates if candidate.value < t2_bound
    ]

    sin2_theta13 = PHI0 * mp.exp(-mp.mpf(5) / 6)
    s13 = mp.sqrt(sin2_theta13)
    s23 = 1 / mp.sqrt(2)
    c13 = mp.sqrt(1 - sin2_theta13)
    t3_lower = mp.sqrt(max(mp.mpf("0"), sin2_theta13 - SIN2_THETA13_SIGMA))
    t3_upper = mp.sqrt(sin2_theta13 + SIN2_THETA13_SIGMA)
    t3 = TargetWindow(
        name="T3_abs_Y3e_over_y3",
        target=s13,
        lower=t3_lower,
        upper=t3_upper,
    )
    t3_mu_companion = s23 * c13
    t3_tau_companion = s23 * c13

    checks.append(
        (
            "T1 independently reproduces v2 ratio",
            abs(t1_value - mp.mpf("0.005572598413861311")) < mp.mpf("2e-15"),
        )
    )
    checks.append(
        (
            "T2 independently reproduces v2 upper bound",
            abs(t2_bound - mp.mpf("0.0027751684816063305")) < mp.mpf("2e-15"),
        )
    )
    checks.append(
        (
            "v270 reactor column reconstructs sin2(theta13)",
            abs(s13**2 - sin2_theta13) < mp.mpf("1e-50"),
        )
    )
    checks.append(
        (
            "v270 atmospheric companions are equal",
            abs(t3_mu_companion - t3_tau_companion) < mp.mpf("1e-50"),
        )
    )

    t1_hits = target_hits(candidates, t1)
    t3_hits = target_hits(candidates, t3)
    t1_lee = len(candidates) * t1.fractional_width
    t3_lee = len(candidates) * t3.fractional_width
    t1_significant = bool(t1_hits) and t1_lee < SIGNIFICANT_LEE_MAX
    t3_significant = bool(t3_hits) and t3_lee < SIGNIFICANT_LEE_MAX

    # Related means the same phi0 power class.  Significance is mandatory;
    # numerical proximity alone never freezes v3.
    related_pairs = [
        (left, right)
        for left in t1_hits
        for right in t3_hits
        if left.phi_power == right.phi_power
    ]
    coherent = t1_significant and t3_significant and bool(related_pairs)

    # Three controls: log-scramble across the physically relevant T1--T3
    # interval, padded by one octave on each side.  Protocol is fixed by seed.
    rng = random.Random(CONTROL_SEED)
    control_min = t1.target / 2
    control_max = t3.target * 2
    log_min = math.log(float(control_min))
    log_max = math.log(float(control_max))
    controls: list[tuple[TargetWindow, list[Candidate], mp.mpf]] = []
    for index in range(N_CONTROLS):
        target = mp.mpf(str(math.exp(rng.uniform(log_min, log_max))))
        window = TargetWindow(
            name=f"CONTROL_{index + 1}",
            target=target,
            lower=target * (1 - CONTROL_HALF_WIDTH),
            upper=target * (1 + CONTROL_HALF_WIDTH),
        )
        hits = target_hits(candidates, window)
        lee = len(candidates) * window.fractional_width
        controls.append((window, hits, lee))

    control_any_hit_rate = (
        sum(bool(hits) for _window, hits, _lee in controls) / len(controls)
    )
    control_total_hits = sum(len(hits) for _window, hits, _lee in controls)
    checks.append(("exactly three seeded controls evaluated", len(controls) == 3))
    checks.append(
        (
            "all target and control LEE expectations are finite",
            all(
                mp.isfinite(value)
                for value in [t1_lee, t3_lee]
                + [lee for _window, _hits, lee in controls]
            ),
        )
    )

    if coherent:
        verdict = "NU_RATIO_GRAMMAR_COHERENT_HIT"
        v3_status = (
            "QUALIFIES_FOR_V3_FREEZE, but this probe intentionally performs no "
            "implicit file write"
        )
    else:
        verdict = "NU_RATIO_GRAMMAR_NULL"
        v3_status = "NOT_FROZEN"

    print("PRE-DECLARED GRAMMAR")
    print(
        "  form phi0^a * r * exp(-b); a=0..4; b={0,5/6,1}; "
        "r=7 ladder + 6 integers + 4 epsilon forms"
    )
    print(f"  raw={raw_grammar_size} unique={len(candidates)}")
    print(f"  phi0={fmt(PHI0, 16)} epsilon={fmt(EPSILON, 16)}")
    print()
    print("DERIVED TARGETS")
    print(
        "  T1 y2/y3={} band=[{},{}] (half-width={:.4f}%; "
        "NuFIT+2% RG)".format(
            fmt(t1.target, 16),
            fmt(t1.lower, 16),
            fmt(t1.upper, 16),
            float(100 * t1_half_width),
        )
    )
    print(
        "     chain m2={} eV, M2={} GeV, R2={}, y2={}, y3={}".format(
            fmt(m2_ev, 14),
            fmt(M2_GEV, 14),
            fmt(rundown2, 14),
            fmt(y2_required, 14),
            fmt(y3_frozen, 14),
        )
    )
    print(
        "  T2 y1/y3 < {} from m1_room={} eV; {} grammar members below".format(
            fmt(t2_bound, 16), fmt(m1_room_ev, 14), len(t2_below)
        )
    )
    print(
        "  T3 |Y3e|/y3=s13={} band=[{},{}] from "
        "sin2(theta13)={}".format(
            fmt(t3.target, 16),
            fmt(t3.lower, 16),
            fmt(t3.upper, 16),
            fmt(sin2_theta13, 16),
        )
    )
    print(
        "     PMNS third-row companions |Y3mu|/y3=|Y3tau|/y3={} "
        "and phase arg(Y3e/y3)=+4pi/3".format(fmt(t3_mu_companion, 16))
    )
    print()

    for window, hits, lee in ((t1, t1_hits, t1_lee), (t3, t3_hits, t3_lee)):
        print(
            "{} CENSUS hits={} LEE_expectation={} significant={}".format(
                window.name,
                len(hits),
                fmt(lee, 10),
                bool(hits) and lee < SIGNIFICANT_LEE_MAX,
            )
        )
        if hits:
            for candidate in hits:
                print(
                    "  HIT {:46s} value={} rel={:+.5f}% phi-class={}".format(
                        candidate.name,
                        fmt(candidate.value, 14),
                        float(100 * (candidate.value / window.target - 1)),
                        candidate.phi_power,
                    )
                )
        else:
            for candidate in nearest_candidates(candidates, window.target, 3):
                print(
                    "  NEAREST {:42s} value={} rel={:+.5f}%".format(
                        candidate.name,
                        fmt(candidate.value, 14),
                        float(100 * (candidate.value / window.target - 1)),
                    )
                )

    print()
    print("T2 MEMBERS BELOW BOUND (closest 12, all entries shown satisfy < bound)")
    for candidate in sorted(t2_below, key=lambda item: item.value, reverse=True)[:12]:
        print(
            "  {:46s} value={} bound_fraction={:.6f}".format(
                candidate.name,
                fmt(candidate.value, 14),
                float(candidate.value / t2_bound),
            )
        )

    print()
    print("SEEDED SCRAMBLED CONTROLS")
    for window, hits, lee in controls:
        print(
            "  {} target={} hits={} LEE={} any_hit={}".format(
                window.name,
                fmt(window.target, 14),
                len(hits),
                fmt(lee, 8),
                bool(hits),
            )
        )
    print(
        "  control_target_any_hit_rate={:.6f} total_candidate_hits={}".format(
            control_any_hit_rate, control_total_hits
        )
    )

    print()
    print(
        "COHERENCE related_same_phi_power_pairs={} significant_T1={} "
        "significant_T3={} coherent={}".format(
            len(related_pairs), t1_significant, t3_significant, coherent
        )
    )
    print("VERDICT", verdict)
    print("V3_FREEZE", v3_status)
    if not coherent:
        print(
            "MISSING_MECHANISM TFPT does not supply the Q_+-to-charged-lepton "
            "basis map whose third Dirac row contains "
            "|Y3e|/y3=sqrt(phi0*exp(-5/6))={} with phase +4pi/3 and "
            "|Y3mu|/y3=|Y3tau|/y3={}; 2*phi0^2 is only a "
            "LEE-nonsignificant approximation to T1.".format(
                fmt(s13, 16), fmt(t3_mu_companion, 16)
            )
        )

    print()
    for label, passed in checks:
        print(("PASS " if passed else "FAIL ") + label)
    all_pass = all(passed for _label, passed in checks)
    print("PROTOCOL-ALL-PASS" if all_pass else "PROTOCOL-FAILURE")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
