#!/usr/bin/env python3
"""Probe a seam-Schur construction of the v3 heavy-neutrino texture.

EXPLORATION ONLY.  This script reads no measured neutrino data and edits no
files.  It constructs the three charged sectors directly from the frozen v983
lattice glue, then evaluates a finite candidate family declared below.

ANTI-NUMEROLOGY / LOOK-ELSEWHERE DECLARATION
--------------------------------------------
The main family contains exactly four K_Sigma forms crossed with exactly two
residue normalizations, hence 8 trials and no fitted parameters:

K1 ``h``       : conformal Hamiltonian restricted to charged sectors.
K2 ``exp(+2pi h)``: positive KMS/modular Boltzmann inverse-weight convention.
K3 ``exp(-2pi h)``: positive KMS/modular Boltzmann weight convention.
K4 ``d``       : charged-sector root multiplicity (dimension proxy).

B1 ``unit``           : the Schur intertwiner is isometric in character basis.
B2 ``sqrt_dimension`` : |b_k| = sqrt(d_k), the residue/multiplicity norm.

No overall rescaling is fitted: M_R/M_scal = B^dag K_Sigma^{-1} B is evaluated
literally.  Reflection fixes |b_1|=|b_3|.  The target
``(epsilon, 2 epsilon, 3)`` is introduced only after all structural matrices
have been built.  Acceptance requires all three pre-declared tests:

1. k=3 is strictly dominant and its eigenvalue lies in [3/2, 6];
2. lambda_1/lambda_3 lies within a factor 2 of epsilon/3;
3. lambda_2/lambda_1 lies within 10% of 2.

If all 8 trials fail, required K spectra are inverted exactly for both B
normalizations.  One separately counted, pre-declared final comparison uses
exactly 9 corpus-built vectors: the four K forms above and
``phi0**p * Spec(Q_+)`` for p in {-2,-1,0,1,2}.  It uses fixed character order,
no permutations or rescalings, and a componentwise factor-2 match.  The
phi0/Q_+ products are comparison grammar, not claimed frozen seam operators.
Thus the complete look-elsewhere accounting is 8 main trials plus 9 diagnostic
required-spectrum comparators.
"""

from __future__ import annotations

import inspect
import itertools
import math
import os
import sys
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable

import mpmath as mp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import g_car, phi0  # noqa: E402


mp.mp.dps = 60

# Frozen v983 glue vector lambda = (omega_s, omega_f), in exact coordinates.
OMEGA_S = (Fraction(1, 2),) * 5
OMEGA_F = (
    Fraction(3, 4),
    Fraction(-1, 4),
    Fraction(-1, 4),
    Fraction(-1, 4),
)
LAMBDA = OMEGA_S + OMEGA_F
NORM_CUTOFF = Fraction(2)
D5_COORDINATE_RANGE = range(-5, 4)
A3_FREE_COORDINATE_RANGE = range(-6, 7)

# Main candidate names and rationales are frozen before target evaluation.
K_FORM_DECLARATIONS = (
    ("h", "charged-sector conformal Hamiltonian"),
    ("exp(+2pi h)", "positive KMS inverse-weight convention"),
    ("exp(-2pi h)", "positive KMS weight convention"),
    ("d", "charged-sector root multiplicity"),
)
B_NORMALIZATION_DECLARATIONS = (
    ("unit", "isometric Schur intertwiner"),
    ("sqrt_dimension", "residue norm |b_k|=sqrt(d_k)"),
)
MAIN_TRIAL_COUNT = len(K_FORM_DECLARATIONS) * len(B_NORMALIZATION_DECLARATIONS)

# Separate inversion-diagnostic grammar, also frozen before target evaluation.
PHI0_QPLUS_EXPONENTS = (-2, -1, 0, 1, 2)
INVERSION_COMPARATOR_COUNT = len(K_FORM_DECLARATIONS) + len(PHI0_QPLUS_EXPONENTS)
QPLUS_SPECTRUM = (mp.mpf(1), mp.mpf(2), mp.mpf(3))

# Acceptance constants are declarations, not inferred from outcomes.
DOMINANT_SCALE_INTERVAL = (mp.mpf("1.5"), mp.mpf("6"))
HIERARCHY_FACTOR_TOLERANCE = mp.mpf(2)
LIGHT_PAIR_RELATIVE_TOLERANCE = mp.mpf("0.10")
INVERSION_COMPONENT_FACTOR_TOLERANCE = mp.mpf(2)


@dataclass(frozen=True)
class ChargedSector:
    k: int
    minimum_norm: Fraction
    conformal_weight: Fraction
    minimum_vector_count: int


@dataclass(frozen=True)
class StructuralOutcome:
    k_form: str
    b_normalization: str
    k_spectrum: tuple[mp.mpf, mp.mpf, mp.mpf]
    b_squared: tuple[mp.mpf, mp.mpf, mp.mpf]
    mr_spectrum: tuple[mp.mpf, mp.mpf, mp.mpf]

    @property
    def label(self) -> str:
        return f"{self.k_form} x {self.b_normalization}"


@dataclass(frozen=True)
class Acceptance:
    dominant_scale: bool
    hierarchy: bool
    light_pair: bool

    @property
    def hit(self) -> bool:
        return self.dominant_scale and self.hierarchy and self.light_pair


def component_norm_censuses(
    k: int,
) -> tuple[dict[Fraction, int], dict[Fraction, int]]:
    """Enumerate exact D5 and A3 norm censuses up to the norm-2 cutoff.

    The ranges are the frozen v983 ranges.  They are exhaustive below the
    cutoff: any omitted base coordinate has shifted absolute value greater
    than sqrt(2), so it cannot contribute to a total norm at most 2.
    """
    shift = tuple(Fraction(k) * value for value in LAMBDA)
    d5: dict[Fraction, int] = {}
    for coordinates in itertools.product(D5_COORDINATE_RANGE, repeat=5):
        if sum(coordinates) % 2:
            continue
        norm = sum(
            (Fraction(coordinates[index]) + shift[index]) ** 2
            for index in range(5)
        )
        if norm <= NORM_CUTOFF:
            d5[norm] = d5.get(norm, 0) + 1

    a3: dict[Fraction, int] = {}
    for free_coordinates in itertools.product(A3_FREE_COORDINATE_RANGE, repeat=3):
        coordinates = free_coordinates + (-sum(free_coordinates),)
        norm = sum(
            (Fraction(coordinates[index]) + shift[5 + index]) ** 2
            for index in range(4)
        )
        if norm <= NORM_CUTOFF:
            a3[norm] = a3.get(norm, 0) + 1
    return d5, a3


def exact_coset_census(k: int) -> dict[Fraction, int]:
    """Return exact total-norm multiplicities in L0 + k*lambda up to norm 2."""
    d5, a3 = component_norm_censuses(k)
    total: dict[Fraction, int] = {}
    for d5_norm, d5_count in d5.items():
        for a3_norm, a3_count in a3.items():
            norm = d5_norm + a3_norm
            if norm <= NORM_CUTOFF:
                total[norm] = total.get(norm, 0) + d5_count * a3_count
    return total


def build_sectors() -> tuple[ChargedSector, ChargedSector, ChargedSector]:
    """Construct k=1,2,3 sectors solely from exact frozen lattice arithmetic."""
    sectors = []
    for k in (1, 2, 3):
        census = exact_coset_census(k)
        minimum_norm = min(census)
        sectors.append(
            ChargedSector(
                k=k,
                minimum_norm=minimum_norm,
                conformal_weight=minimum_norm / 2,
                minimum_vector_count=census[minimum_norm],
            )
        )
    return tuple(sectors)  # type: ignore[return-value]


def k_spectra_from_sectors(
    sectors: tuple[ChargedSector, ChargedSector, ChargedSector],
) -> dict[str, tuple[mp.mpf, mp.mpf, mp.mpf]]:
    """Build exactly the four pre-declared positive K_Sigma candidates."""
    weights = tuple(mp.mpf(str(float(sector.conformal_weight))) for sector in sectors)
    dimensions = tuple(mp.mpf(sector.minimum_vector_count) for sector in sectors)
    return {
        "h": weights,
        "exp(+2pi h)": tuple(mp.exp(2 * mp.pi * value) for value in weights),
        "exp(-2pi h)": tuple(mp.exp(-2 * mp.pi * value) for value in weights),
        "d": dimensions,
    }


def b_squared_from_sectors(
    sectors: tuple[ChargedSector, ChargedSector, ChargedSector],
) -> dict[str, tuple[mp.mpf, mp.mpf, mp.mpf]]:
    """Build the two pre-declared Schur residue normalizations."""
    return {
        "unit": (mp.mpf(1), mp.mpf(1), mp.mpf(1)),
        "sqrt_dimension": tuple(
            mp.mpf(sector.minimum_vector_count) for sector in sectors
        ),
    }


def build_structural_outcomes(
    sectors: tuple[ChargedSector, ChargedSector, ChargedSector],
) -> tuple[StructuralOutcome, ...]:
    """Evaluate B^dag K^{-1} B from charged-sector data alone."""
    k_spectra = k_spectra_from_sectors(sectors)
    b_squared_spectra = b_squared_from_sectors(sectors)
    outcomes = []
    for k_name, _rationale in K_FORM_DECLARATIONS:
        for b_name, _rationale in B_NORMALIZATION_DECLARATIONS:
            k_spectrum = k_spectra[k_name]
            b_squared = b_squared_spectra[b_name]
            outcomes.append(
                StructuralOutcome(
                    k_form=k_name,
                    b_normalization=b_name,
                    k_spectrum=k_spectrum,
                    b_squared=b_squared,
                    mr_spectrum=tuple(
                        b_value / k_value
                        for b_value, k_value in zip(b_squared, k_spectrum)
                    ),
                )
            )
    return tuple(outcomes)


def within_factor(value: mp.mpf, target: mp.mpf, factor: mp.mpf) -> bool:
    return target / factor <= value <= target * factor


def assess_outcome(
    outcome: StructuralOutcome,
    target: tuple[mp.mpf, mp.mpf, mp.mpf],
) -> Acceptance:
    """Compare one already-built structural outcome to the v3 target."""
    eigenvalues = outcome.mr_spectrum
    k3_strictly_dominant = eigenvalues[2] > max(eigenvalues[0], eigenvalues[1])
    dominant_scale = (
        k3_strictly_dominant
        and DOMINANT_SCALE_INTERVAL[0]
        <= eigenvalues[2]
        <= DOMINANT_SCALE_INTERVAL[1]
    )
    hierarchy = within_factor(
        eigenvalues[0] / eigenvalues[2],
        target[0] / target[2],
        HIERARCHY_FACTOR_TOLERANCE,
    )
    light_ratio = eigenvalues[1] / eigenvalues[0]
    light_pair = abs(light_ratio / (target[1] / target[0]) - 1) <= (
        LIGHT_PAIR_RELATIVE_TOLERANCE
    )
    return Acceptance(dominant_scale, hierarchy, light_pair)


def required_k_spectrum(
    b_squared: tuple[mp.mpf, mp.mpf, mp.mpf],
    target: tuple[mp.mpf, mp.mpf, mp.mpf],
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Invert target = B^dag K^{-1} B componentwise."""
    return tuple(
        b_value / target_value
        for b_value, target_value in zip(b_squared, target)
    )


def inversion_comparators(
    sectors: tuple[ChargedSector, ChargedSector, ChargedSector],
) -> dict[str, tuple[mp.mpf, mp.mpf, mp.mpf]]:
    """Build the separately declared nine-vector final comparison family."""
    comparators = dict(k_spectra_from_sectors(sectors))
    for exponent in PHI0_QPLUS_EXPONENTS:
        scale = mp.mpf(phi0) ** exponent
        comparators[f"phi0^{exponent} * Spec(Q_+)"] = tuple(
            scale * value for value in QPLUS_SPECTRUM
        )
    return comparators


def componentwise_factor_match(
    candidate: tuple[mp.mpf, mp.mpf, mp.mpf],
    required: tuple[mp.mpf, mp.mpf, mp.mpf],
) -> bool:
    return all(
        within_factor(value, target, INVERSION_COMPONENT_FACTOR_TOLERANCE)
        for value, target in zip(candidate, required)
    )


def fmt(value: mp.mpf, digits: int = 9) -> str:
    return mp.nstr(value, digits)


def spectrum_text(values: tuple[mp.mpf, mp.mpf, mp.mpf]) -> str:
    return "[" + ", ".join(fmt(value) for value in values) + "]"


def report_check(label: str, passed: bool) -> bool:
    print(("PASS " if passed else "FAIL ") + label)
    return passed


def main() -> int:
    print("NU SCHUR TEXTURE PROBE -- EXPLORATION ONLY")
    print("PRE-DECLARED MAIN FAMILY")
    for name, rationale in K_FORM_DECLARATIONS:
        print(f"  K {name:<14} : {rationale}")
    for name, rationale in B_NORMALIZATION_DECLARATIONS:
        print(f"  B {name:<14} : {rationale}")
    print(f"  LEE main trials: {MAIN_TRIAL_COUNT}")
    print(
        "  acceptance: k3 strict dominant and in [1.5,6]; "
        "lambda1/lambda3 within x2 of epsilon/3; "
        "lambda2/lambda1 within 10% of 2"
    )
    print(
        "  final inversion comparison: "
        f"{INVERSION_COMPARATOR_COUNT} separately counted vectors"
    )
    print()

    sectors = build_sectors()
    full_censuses = [exact_coset_census(k) for k in range(4)]
    minimum_norms = [min(census) for census in full_censuses]
    minimum_counts = [census[min(census)] for census in full_censuses]
    norm_two_counts = [census.get(Fraction(2), 0) for census in full_censuses]

    print("EXACT COSET TABLE")
    print("  k  minimum_norm  h_k  min-vector-count  norm-2-count")
    print(
        "  0  {}             {}    {}                 {}".format(
            minimum_norms[0],
            minimum_norms[0] / 2,
            minimum_counts[0],
            norm_two_counts[0],
        )
    )
    for sector in sectors:
        print(
            "  {}  {}             {}    {}                {}".format(
                sector.k,
                sector.minimum_norm,
                sector.conformal_weight,
                sector.minimum_vector_count,
                norm_two_counts[sector.k],
            )
        )
    print()

    # The target enters only here, after lattice, K, B, and all 8 outcomes exist.
    outcomes = build_structural_outcomes(sectors)
    epsilon = mp.mpf(phi0) ** 2 / (2 * mp.mpf(g_car))
    target = (epsilon, 2 * epsilon, mp.mpf(3))
    assessments = tuple(assess_outcome(outcome, target) for outcome in outcomes)

    print("EIGHT PRE-DECLARED OUTCOMES")
    print("  #  K x B                              M_R/M_scal [k1,k2,k3]          D H L HIT")
    for index, (outcome, acceptance) in enumerate(
        zip(outcomes, assessments), start=1
    ):
        flags = " ".join(
            "Y" if value else "N"
            for value in (
                acceptance.dominant_scale,
                acceptance.hierarchy,
                acceptance.light_pair,
                acceptance.hit,
            )
        )
        print(
            f"  {index}  {outcome.label:<35} "
            f"{spectrum_text(outcome.mr_spectrum):<36} {flags}"
        )
    print("  D=dominant-scale, H=epsilon/3 hierarchy, L=light-pair factor 2")
    print()

    hit_indices = [
        index
        for index, acceptance in enumerate(assessments, start=1)
        if acceptance.hit
    ]
    b_spectra = b_squared_from_sectors(sectors)
    required_spectra = {
        name: required_k_spectrum(values, target)
        for name, values in b_spectra.items()
    }

    print("REQUIRED K_Sigma INVERSION")
    print(f"  epsilon = {fmt(epsilon, 14)}")
    for name, required in required_spectra.items():
        print(f"  B={name:<14} K_required = {spectrum_text(required)}")
    print(
        "  unit formula = [1/epsilon, 1/(2 epsilon), 1/3] "
        "(fixed character order)"
    )
    print()

    comparators = inversion_comparators(sectors)
    comparison_hits: list[tuple[str, str]] = []
    print("PRE-DECLARED FINAL REQUIRED-SPECTRUM COMPARISON")
    print(
        "  comparator                              candidate K spectrum"
        "                unit  sqrt_d"
    )
    for name, candidate in comparators.items():
        unit_match = componentwise_factor_match(
            candidate, required_spectra["unit"]
        )
        dimension_match = componentwise_factor_match(
            candidate, required_spectra["sqrt_dimension"]
        )
        if unit_match:
            comparison_hits.append((name, "unit"))
        if dimension_match:
            comparison_hits.append((name, "sqrt_dimension"))
        print(
            f"  {name:<39} {spectrum_text(candidate):<35} "
            f"{'HIT' if unit_match else 'null':<5} "
            f"{'HIT' if dimension_match else 'null'}"
        )
    print(
        f"  LEE accounting: {MAIN_TRIAL_COUNT} main + "
        f"{INVERSION_COMPARATOR_COUNT} inversion diagnostics"
    )
    print()

    candidate_source = inspect.getsource(build_structural_outcomes)
    circularity_clean = all(
        forbidden not in candidate_source
        for forbidden in ("epsilon", "target", "phi0", "QPLUS")
    )
    reflection_exact = all(
        mp.almosteq(outcome.mr_spectrum[0], outcome.mr_spectrum[2])
        for outcome in outcomes
    )
    inversion_exact = all(
        all(
            mp.almosteq(
                b_value / k_value,
                target_value,
            )
            for b_value, k_value, target_value in zip(
                b_spectra[name], required, target
            )
        )
        for name, required in required_spectra.items()
    )
    v4_path = os.path.join(
        REPO,
        "experiments",
        "nu-scalaron-falsification",
        "hypotheses",
        "nu_scalaron_v4.yaml",
    )

    checks = [
        report_check(
            "v983 norm-2 census is [52,64,60,64]",
            norm_two_counts == [52, 64, 60, 64],
        ),
        report_check(
            "charged coset minima are exactly norm 2 and h_k=1",
            minimum_norms[1:] == [Fraction(2)] * 3
            and all(sector.conformal_weight == 1 for sector in sectors),
        ),
        report_check(
            "D4 reflection pairs k=1 and k=3 dimensions",
            sectors[0].minimum_vector_count == sectors[2].minimum_vector_count == 64,
        ),
        report_check(
            "exactly 8 unique main trials were evaluated",
            len(outcomes) == MAIN_TRIAL_COUNT
            and len({outcome.label for outcome in outcomes}) == MAIN_TRIAL_COUNT,
        ),
        report_check(
            "candidate builder contains no target/epsilon/phi0/Q+ input",
            circularity_clean,
        ),
        report_check(
            "D4 reflection forces lambda1=lambda3 in every main trial",
            reflection_exact,
        ),
        report_check("no pre-declared main combination is a hit", not hit_indices),
        report_check(
            "required K spectra invert back to the target exactly",
            inversion_exact,
        ),
        report_check(
            "exactly 9 unique inversion comparators were evaluated",
            len(comparators) == INVERSION_COMPARATOR_COUNT,
        ),
        report_check(
            "no pre-declared corpus comparator matches either required spectrum",
            not comparison_hits,
        ),
        report_check("null result creates no v4 freeze", not os.path.exists(v4_path)),
    ]

    required_unit = required_spectra["unit"]
    verdict = (
        "SCHUR_TEXTURE_HIT(" + ",".join(map(str, hit_indices)) + ")"
        if hit_indices
        else "SCHUR_TEXTURE_NULL(required_spectrum="
        + spectrum_text(required_unit)
        + ")"
    )
    freeze_status = (
        "V4_FREEZE_REQUIRED_BY_HIT"
        if hit_indices
        else "V4_NOT_FROZEN_NULL"
    )
    print()
    print("VERDICT", verdict)
    print("FREEZE_STATUS", freeze_status)
    print()
    print("FIVE-SENTENCE CONCLUSION")
    print("  1. Exact v983 lattice arithmetic gives h_1=h_2=h_3=1 and dimensions 64,60,64.")
    print("  2. The eight declared K/B constructions produce no accepted heavy-neutrino texture.")
    print("  3. D4 reflection makes the first and third Schur eigenvalues equal, excluding the epsilon-to-3 hierarchy structurally.")
    print("  4. The unit-normalized target would require K_Sigma=[1/epsilon,1/(2epsilon),1/3], which none of nine declared corpus comparators supplies.")
    print("  5. Therefore the pentagon-chain scales require mechanism beyond the frozen seam weights, dimensions, and elementary phi0-times-Q+ grammar.")

    all_pass = all(checks)
    print("PROTOCOL-ALL-PASS" if all_pass else "PROTOCOL-FAILURE")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
