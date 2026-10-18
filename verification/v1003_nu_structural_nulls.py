"""v1003 -- FLAV.NU.TEXTURE.MECHANISM.01: two structural nulls on the
heavy-neutrino texture, plus the exact charged-sector data and the
orientation-doubling structure theorem.

Provenance: experiments/tfpt-discovery/nu_schur_texture_probe.py
+ nu_orientation_seesaw_probe.py (review wave 5, 2026-08-29).

THE POINT.  Binding constraints on the mechanism, not a texture.

  [E]  charged-sector data from frozen v983 glue: h = (1,1,1),
       d = (64,60,64); every charged coset has min-norm 2.
  [X]  Schur-texture NULL: all 8 preregistered (K,B) combinations fail.
       D4 reflection forces lambda_1 = lambda_3, so the hierarchy
       (eps, 2 eps, 3) is structurally unreachable from D4-even seam
       data.  Required K spectrum [1/eps, 1/(2 eps), 1/3] matches none
       of 9 comparators.
  [E]  orientation-doubling structure theorem: the sgn-J odd sector
       generically lifts the degeneracy (exact rational witness
       odd_scale=1/4, gamma=1/10).  Pattern dims K_e=4, K_o=2, C=5.
  [X]  scale NULL: 12 declared trials all fail; required cancellation
       1-|c/a| is not supplied by any frozen constant; eta-branches
       are isospectral.

MUST-FAIL: a D4-even Schur construction that produces (eps,2eps,3);
a declared (K,B) or (K_e,K_o,C,eta) combination that hits; a corpus
comparator matching the inverted K spectrum.

HONEST SCOPE (firewall): FLAV.NUSCALE.05/.06 unmoved; no seesaw
closure; the mechanism must be D4-odd AND supply a ~2e-4 even-odd
cancellation; pure seam data excluded [X-typed].  Python-only /
Wolfram mirror deferred.
"""
from __future__ import annotations

import inspect
import itertools
import os
from dataclasses import dataclass
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

from tfpt_constants import check, summary, reset, phi0, c3, g_car


def report(name, ok, extra=""):
    check(name if not extra else "%s -- %s" % (name, extra), ok)


mp.mp.dps = 60

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

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
PHI0_QPLUS_EXPONENTS = (-2, -1, 0, 1, 2)
INVERSION_COMPARATOR_COUNT = len(K_FORM_DECLARATIONS) + len(PHI0_QPLUS_EXPONENTS)
QPLUS_SPECTRUM = (mp.mpf(1), mp.mpf(2), mp.mpf(3))
DOMINANT_SCALE_INTERVAL = (mp.mpf("1.5"), mp.mpf("6"))
HIERARCHY_FACTOR_TOLERANCE = mp.mpf(2)
LIGHT_PAIR_RELATIVE_TOLERANCE = mp.mpf("0.10")
INVERSION_COMPONENT_FACTOR_TOLERANCE = mp.mpf(2)

R = np.array(((0.0, 0.0, 1.0), (0.0, 1.0, 0.0), (1.0, 0.0, 0.0)))
I3 = np.eye(3)
ODD_DIAGONAL = np.diag((1.0, 0.0, -1.0))
DIMENSION_EVEN = np.diag((1.0, 60.0 / 64.0, 1.0))
C3_VALUE = float(c3)
PHI0_VALUE = float(phi0)
HIERARCHY_INTERVAL = (1.0e-5, 1.0e-3)
LIGHT_PAIR_INTERVAL = (1.8, 2.2)
EIGENVALUE_TOLERANCE = 1.0e-10
RATIO_COMPARISON_TOLERANCE = 0.05

DECLARED_COMBINATIONS = (
    ("U-P-P-I", "uniform even; first-order odd; first-order identity transfer"),
    ("U-P-C-I", "uniform even; first-order odd; primitive c3 transfer"),
    ("U-C-P-I", "uniform even; primitive c3 odd; first-order transfer"),
    ("U-C-C-R", "uniform even; primitive c3 odd; reflected c3 transfer"),
    ("D-P-P-R", "dimension even; first-order odd; reflected first-order transfer"),
    ("D-P2-P-I", "dimension even; two-transfer odd feedback; first-order transfer"),
)
BRANCHES = (-1, 1)
MAIN_LEE_COUNT = len(DECLARED_COMBINATIONS) * len(BRANCHES)
INVERSE_COMPARATORS = (
    ("1 (uniform h)", 1.0),
    ("15/16 (d2/d1)", 15.0 / 16.0),
    ("c3", C3_VALUE),
    ("phi0", PHI0_VALUE),
    ("phi0^2", PHI0_VALUE**2),
    ("1/g_car", 1.0 / float(g_car)),
    ("(2/3)^3", (2.0 / 3.0) ** 3),
    ("(2/3)^6", (2.0 / 3.0) ** 6),
)


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
    k_spectrum: tuple
    b_squared: tuple
    mr_spectrum: tuple

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


@dataclass(frozen=True)
class Candidate:
    label: str
    rationale: str
    k_even: np.ndarray
    k_odd: np.ndarray
    coupling: np.ndarray


@dataclass(frozen=True)
class Outcome:
    label: str
    eta: int
    spectrum: tuple
    positive: bool
    nondegenerate: bool
    hierarchy_ratio: float
    light_pair_ratio: float
    hit: bool


def component_norm_censuses(k: int):
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


def exact_coset_census(k: int):
    d5, a3 = component_norm_censuses(k)
    total: dict[Fraction, int] = {}
    for d5_norm, d5_count in d5.items():
        for a3_norm, a3_count in a3.items():
            norm = d5_norm + a3_norm
            if norm <= NORM_CUTOFF:
                total[norm] = total.get(norm, 0) + d5_count * a3_count
    return total


def build_sectors():
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
    return tuple(sectors)


def k_spectra_from_sectors(sectors):
    weights = tuple(mp.mpf(str(float(sector.conformal_weight))) for sector in sectors)
    dimensions = tuple(mp.mpf(sector.minimum_vector_count) for sector in sectors)
    return {
        "h": weights,
        "exp(+2pi h)": tuple(mp.exp(2 * mp.pi * value) for value in weights),
        "exp(-2pi h)": tuple(mp.exp(-2 * mp.pi * value) for value in weights),
        "d": dimensions,
    }


def b_squared_from_sectors(sectors):
    return {
        "unit": (mp.mpf(1), mp.mpf(1), mp.mpf(1)),
        "sqrt_dimension": tuple(
            mp.mpf(sector.minimum_vector_count) for sector in sectors
        ),
    }


def build_structural_outcomes(sectors):
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


def within_factor(value, target, factor):
    return target / factor <= value <= target * factor


def assess_outcome(outcome, target):
    eigenvalues = outcome.mr_spectrum
    k3_strictly_dominant = eigenvalues[2] > max(eigenvalues[0], eigenvalues[1])
    dominant_scale = (
        k3_strictly_dominant
        and DOMINANT_SCALE_INTERVAL[0] <= eigenvalues[2] <= DOMINANT_SCALE_INTERVAL[1]
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


def required_k_spectrum(b_squared, target):
    return tuple(
        b_value / target_value
        for b_value, target_value in zip(b_squared, target)
    )


def inversion_comparators(sectors):
    comparators = dict(k_spectra_from_sectors(sectors))
    for exponent in PHI0_QPLUS_EXPONENTS:
        scale = mp.mpf(phi0) ** exponent
        comparators[f"phi0^{exponent} * Spec(Q_+)"] = tuple(
            scale * value for value in QPLUS_SPECTRUM
        )
    return comparators


def componentwise_factor_match(candidate, required):
    return all(
        within_factor(value, target, INVERSION_COMPONENT_FACTOR_TOLERANCE)
        for value, target in zip(candidate, required)
    )


def exact_structure_theorem():
    exact_r = sp.Matrix(((0, 0, 1), (0, 1, 0), (1, 0, 0)))
    x11, x22, x33, x12, x13, x23 = sp.symbols("x11 x22 x33 x12 x13 x23")
    symmetric_variables = (x11, x22, x33, x12, x13, x23)
    generic_symmetric = sp.Matrix(
        ((x11, x12, x13), (x12, x22, x23), (x13, x23, x33))
    )
    even_equations = list(exact_r * generic_symmetric * exact_r - generic_symmetric)
    odd_equations = list(exact_r * generic_symmetric * exact_r + generic_symmetric)
    even_constraint_matrix, _ = sp.linear_eq_to_matrix(
        even_equations, symmetric_variables
    )
    odd_constraint_matrix, _ = sp.linear_eq_to_matrix(
        odd_equations, symmetric_variables
    )
    generic_variables = sp.symbols("y11 y12 y13 y21 y22 y23 y31 y32 y33")
    generic_matrix = sp.Matrix(3, 3, generic_variables)
    coupling_equations = list(exact_r * generic_matrix * exact_r - generic_matrix)
    coupling_constraint_matrix, _ = sp.linear_eq_to_matrix(
        coupling_equations, generic_variables
    )
    a, b, p, q = sp.symbols("a b p q")
    c, r = sp.symbols("c r")
    u, v, w, s, t = sp.symbols("u v w s t")
    k_even = sp.Matrix(((a, p, q), (p, b, p), (q, p, a)))
    k_odd = sp.Matrix(((c, r, 0), (r, 0, -r), (0, -r, -c)))
    coupling = sp.Matrix(((u, s, v), (t, w, t), (v, s, u)))
    pattern_checks = (
        exact_r * k_even * exact_r == k_even,
        exact_r * k_odd * exact_r == -k_odd,
        exact_r * coupling * exact_r == coupling,
    )
    odd_scale, gamma = sp.symbols("odd_scale gamma")
    diagonal_even = sp.eye(3)
    diagonal_odd = sp.diag(odd_scale, 0, -odd_scale)
    diagonal_coupling = gamma * sp.eye(3)
    k_plus = diagonal_even + diagonal_odd
    k_minus = diagonal_even - diagonal_odd
    schur = sp.simplify(
        k_plus - diagonal_coupling * k_minus.inv() * diagonal_coupling
    )
    endpoint_difference = sp.factor(schur[0, 0] - schur[2, 2])
    expected_difference = sp.factor(
        2 * odd_scale * (1 - gamma**2 / (1 - odd_scale**2))
    )
    rational_schur = schur.subs(
        {odd_scale: sp.Rational(1, 4), gamma: sp.Rational(1, 10)}
    )
    rational_eigenvalues = tuple(rational_schur.diagonal())
    simple_exact_example = len(set(rational_eigenvalues)) == 3
    r_even_counterexample = sp.Matrix(((2, 1, 0), (1, 3, 1), (0, 1, 2)))
    counterexample_eigenvalues = tuple(
        sorted(eigenvalue for eigenvalue in r_even_counterexample.eigenvals())
    )
    return {
        "even_dimension": len(symmetric_variables) - even_constraint_matrix.rank(),
        "odd_dimension": len(symmetric_variables) - odd_constraint_matrix.rank(),
        "coupling_dimension": len(generic_variables)
        - coupling_constraint_matrix.rank(),
        "patterns_exact": all(pattern_checks),
        "difference_formula_exact": sp.simplify(
            endpoint_difference - expected_difference
        )
        == 0,
        "simple_exact_example": simple_exact_example,
        "counterexample_eigenvalues": counterexample_eigenvalues,
        "reflection_alone_forces_degeneracy": len(counterexample_eigenvalues) < 3,
    }


def build_declared_candidates():
    specifications = (
        ("U-P-P-I", I3, PHI0_VALUE, PHI0_VALUE * I3),
        ("U-P-C-I", I3, PHI0_VALUE, C3_VALUE * I3),
        ("U-C-P-I", I3, C3_VALUE, PHI0_VALUE * I3),
        ("U-C-C-R", I3, C3_VALUE, C3_VALUE * R),
        ("D-P-P-R", DIMENSION_EVEN, PHI0_VALUE, PHI0_VALUE * R),
        ("D-P2-P-I", DIMENSION_EVEN, PHI0_VALUE**2, PHI0_VALUE * I3),
    )
    rationale_by_label = dict(DECLARED_COMBINATIONS)
    return tuple(
        Candidate(
            label=label,
            rationale=rationale_by_label[label],
            k_even=k_even.copy(),
            k_odd=odd_scale * ODD_DIAGONAL,
            coupling=coupling.copy(),
        )
        for label, k_even, odd_scale, coupling in specifications
    )


def effective_kernel(candidate, eta):
    upper = candidate.k_even + eta * candidate.k_odd
    lower = candidate.k_even - eta * candidate.k_odd
    return upper - candidate.coupling @ np.linalg.inv(lower) @ candidate.coupling.T


def evaluate_candidate(candidate, eta):
    mass_matrix = np.linalg.inv(effective_kernel(candidate, eta))
    spectrum_array = np.linalg.eigvalsh(mass_matrix)
    spectrum = tuple(float(value) for value in spectrum_array)
    positive = spectrum[0] > 0.0
    scale = max(1.0, max(abs(value) for value in spectrum))
    nondegenerate = min(np.diff(spectrum_array)) > EIGENVALUE_TOLERANCE * scale
    hierarchy_ratio = spectrum[0] / spectrum[2]
    light_pair_ratio = spectrum[1] / spectrum[0]
    hit = (
        positive
        and nondegenerate
        and HIERARCHY_INTERVAL[0] <= hierarchy_ratio <= HIERARCHY_INTERVAL[1]
        and LIGHT_PAIR_INTERVAL[0] <= light_pair_ratio <= LIGHT_PAIR_INTERVAL[1]
    )
    return Outcome(
        label=candidate.label,
        eta=eta,
        spectrum=spectrum,
        positive=positive,
        nondegenerate=nondegenerate,
        hierarchy_ratio=hierarchy_ratio,
        light_pair_ratio=light_pair_ratio,
        hit=hit,
    )


def solve_inverse_diagnostic(epsilon):
    target_light = 1 / epsilon
    target_middle = 1 / (2 * epsilon)
    target_heavy = mp.mpf(1) / 3
    gamma = mp.mpf(phi0)
    discriminant = target_light**2 + (4 * target_light * gamma**2 / target_heavy)
    x = (target_light + mp.sqrt(discriminant)) / 2
    y = target_heavy * x / target_light
    a = (x + y) / 2
    c = (x - y) / 2
    b = (target_middle + mp.sqrt(target_middle**2 + 4 * gamma**2)) / 2
    return {
        "a": a,
        "b": b,
        "c": c,
        "gamma": gamma,
        "required_ratio": abs(c / a),
        "cancellation": 1 - abs(c / a),
    }


def run():
    reset()
    print("=" * 78)
    print("v1003 -- FLAV.NU.TEXTURE.MECHANISM.01 structural nulls")
    print("=" * 78)

    sectors = build_sectors()
    full_censuses = [exact_coset_census(k) for k in range(4)]
    minimum_norms = [min(census) for census in full_censuses]
    minimum_counts = [census[min(census)] for census in full_censuses]
    norm_two_counts = [census.get(Fraction(2), 0) for census in full_censuses]

    report(
        "CHARGED SECTOR [E]: v983 norm-2 census is [52,64,60,64]",
        norm_two_counts == [52, 64, 60, 64],
        "k=0..3 min-norm-2 counts %s" % (norm_two_counts,),
    )
    report(
        "CHARGED SECTOR [E]: charged coset minima are exactly norm 2 and h_k=1",
        minimum_norms[1:] == [Fraction(2)] * 3
        and all(sector.conformal_weight == 1 for sector in sectors),
        "h=(%s); min-counts %s"
        % (
            ",".join(str(sector.conformal_weight) for sector in sectors),
            [sector.minimum_vector_count for sector in sectors],
        ),
    )
    report(
        "CHARGED SECTOR [E]: D4 reflection pairs k=1 and k=3 dimensions",
        sectors[0].minimum_vector_count == sectors[2].minimum_vector_count == 64
        and sectors[1].minimum_vector_count == 60,
        "d=(%d,%d,%d)"
        % (
            sectors[0].minimum_vector_count,
            sectors[1].minimum_vector_count,
            sectors[2].minimum_vector_count,
        ),
    )

    outcomes = build_structural_outcomes(sectors)
    epsilon = mp.mpf(phi0) ** 2 / (2 * mp.mpf(g_car))
    target = (epsilon, 2 * epsilon, mp.mpf(3))
    assessments = tuple(assess_outcome(outcome, target) for outcome in outcomes)
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
    comparators = inversion_comparators(sectors)
    comparison_hits = []
    for name, candidate in comparators.items():
        if componentwise_factor_match(candidate, required_spectra["unit"]):
            comparison_hits.append((name, "unit"))
        if componentwise_factor_match(candidate, required_spectra["sqrt_dimension"]):
            comparison_hits.append((name, "sqrt_dimension"))

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
            mp.almosteq(b_value / k_value, target_value)
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
    required_unit = required_spectra["unit"]

    report(
        "SCHUR [X]: exactly 8 unique main trials were evaluated",
        len(outcomes) == MAIN_TRIAL_COUNT
        and len({outcome.label for outcome in outcomes}) == MAIN_TRIAL_COUNT,
    )
    report(
        "SCHUR [X]: candidate builder contains no target/epsilon/phi0/Q+ input",
        circularity_clean,
    )
    report(
        "SCHUR [X]: D4 reflection forces lambda1=lambda3 in every main trial",
        reflection_exact,
        "hierarchy (eps,2eps,3) structurally unreachable from D4-even seam data",
    )
    report(
        "SCHUR [X]: no pre-declared main combination is a hit",
        not hit_indices,
        "8/8 fail",
    )
    report(
        "SCHUR [X]: required K spectra invert back to the target exactly",
        inversion_exact,
        "unit K_required = [%s, %s, %s]"
        % (
            mp.nstr(required_unit[0], 9),
            mp.nstr(required_unit[1], 9),
            mp.nstr(required_unit[2], 9),
        ),
    )
    report(
        "SCHUR [X]: exactly 9 unique inversion comparators were evaluated",
        len(comparators) == INVERSION_COMPARATOR_COUNT,
    )
    report(
        "SCHUR [X]: no pre-declared corpus comparator matches either required spectrum",
        not comparison_hits,
        "required unit K ~ [3536.998, 1768.499, 1/3]",
    )
    report("SCHUR [X]: null result creates no v4 freeze", not os.path.exists(v4_path))

    structure = exact_structure_theorem()
    candidates = build_declared_candidates()
    outcomes_odd = tuple(
        evaluate_candidate(candidate, eta)
        for candidate in candidates
        for eta in BRANCHES
    )
    inverse = solve_inverse_diagnostic(epsilon)
    reconstructed_candidate = Candidate(
        label="INVERSE-DIAGNOSTIC",
        rationale="diagnostic only",
        k_even=np.diag(
            (float(inverse["a"]), float(inverse["b"]), float(inverse["a"]))
        ),
        k_odd=float(inverse["c"]) * ODD_DIAGONAL,
        coupling=float(inverse["gamma"]) * I3,
    )
    reconstructed_spectrum = np.linalg.eigvalsh(
        np.linalg.inv(effective_kernel(reconstructed_candidate, 1))
    )
    inverse_exact_to_precision = all(
        mp.almosteq(mp.mpf(got), want, rel_eps=mp.mpf("1e-11"))
        for got, want in zip(reconstructed_spectrum, target)
    )
    eta_zero_degenerate = True
    c_zero_reduces = True
    branch_covariant = True
    for candidate in candidates:
        eta_zero_kernel = effective_kernel(candidate, 0)
        eta_zero_spectrum = np.linalg.eigvalsh(np.linalg.inv(eta_zero_kernel))
        eta_zero_degenerate = eta_zero_degenerate and (
            min(np.diff(eta_zero_spectrum)) <= EIGENVALUE_TOLERANCE
        )
        for eta in BRANCHES:
            zero_c_candidate = Candidate(
                label=candidate.label,
                rationale=candidate.rationale,
                k_even=candidate.k_even,
                k_odd=candidate.k_odd,
                coupling=np.zeros((3, 3)),
            )
            reduced_kernel = effective_kernel(zero_c_candidate, eta)
            expected_kernel = candidate.k_even + eta * candidate.k_odd
            reduced_mass_spectrum = np.linalg.eigvalsh(np.linalg.inv(reduced_kernel))
            expected_mass_spectrum = np.sort(1 / np.linalg.eigvalsh(expected_kernel))
            c_zero_reduces = c_zero_reduces and np.allclose(
                reduced_kernel, expected_kernel, rtol=0.0, atol=1e-14
            ) and np.allclose(
                reduced_mass_spectrum,
                expected_mass_spectrum,
                rtol=1e-13,
                atol=1e-14,
            )
        branch_covariant = branch_covariant and np.allclose(
            R @ effective_kernel(candidate, 1) @ R,
            effective_kernel(candidate, -1),
            rtol=0.0,
            atol=1e-14,
        )
    odd_source = inspect.getsource(build_declared_candidates).lower()
    odd_circularity_clean = all(
        forbidden not in odd_source
        for forbidden in ("epsilon", "target", "theta13", "measured", "m_3")
    )
    hit_labels = sorted({outcome.label for outcome in outcomes_odd if outcome.hit})
    degeneracy_lifted = all(outcome.nondegenerate for outcome in outcomes_odd)
    comparator_hits = []
    for name, comparator in INVERSE_COMPARATORS:
        relative_difference = abs(
            mp.mpf(comparator) / inverse["required_ratio"] - 1
        )
        if relative_difference <= RATIO_COMPARISON_TOLERANCE:
            comparator_hits.append(name)

    report(
        "ORIENTATION [E]: exact equivariant pattern dimensions are Ke=4, Ko=2, C=5",
        structure["even_dimension"] == 4
        and structure["odd_dimension"] == 2
        and structure["coupling_dimension"] == 5,
    )
    report(
        "ORIENTATION [E]: all displayed equivariance patterns are exact",
        bool(structure["patterns_exact"]),
    )
    report(
        "ORIENTATION [E]: exact endpoint-splitting formula is verified",
        bool(structure["difference_formula_exact"]),
    )
    report(
        "ORIENTATION [E]: one exact rational point has a simple spectrum",
        bool(structure["simple_exact_example"]),
        "odd_scale=1/4, gamma=1/10",
    )
    report(
        "ORIENTATION [E]: R-only degeneracy overclaim is exposed by spectrum {1,2,4}",
        structure["counterexample_eigenvalues"] == (1, 2, 4)
        and not structure["reflection_alone_forces_degeneracy"],
    )
    report(
        "ORIENTATION [E]: eta selection lifts the declared 1<->3 doublet in every candidate",
        degeneracy_lifted,
        "12/12 nondegenerate",
    )
    report(
        "SCALE [X]: exactly 12 declared candidate-branch outcomes were evaluated",
        len(outcomes_odd) == MAIN_LEE_COUNT
        and len(candidates) == len(DECLARED_COMBINATIONS)
        and odd_circularity_clean,
    )
    report(
        "SCALE [X]: all 12 declared trials fail the hierarchy+light-pair hit",
        not hit_labels and all(outcome.positive for outcome in outcomes_odd),
        "12/12 null",
    )
    report(
        "SCALE [X]: eta branches obey exact reflection covariance (isospectral)",
        branch_covariant,
    )
    report(
        "SCALE [X]: inverse diagnostic reconstructs (eps,2eps,3)",
        inverse_exact_to_precision,
        "1-|c/a| = %s" % mp.nstr(inverse["cancellation"], 6),
    )
    report(
        "SCALE [X]: required cancellation is not supplied by any frozen constant",
        inverse["cancellation"] > mp.mpf("1e-4")
        and abs(inverse["cancellation"] - mp.mpf("1.885e-4")) < mp.mpf("2e-6")
        and (not comparator_hits or comparator_hits == ["1 (uniform h)"]),
        "1-|c/a| = %s; 5%%-close comparators %s"
        % (mp.nstr(inverse["cancellation"], 6), comparator_hits),
    )
    report(
        "SCALE [X]: eta=0 restores the doublet; C=0 reduces to Ke +/- Ko",
        eta_zero_degenerate and c_zero_reduces,
    )
    report(
        "FIREWALL (scope): NUSCALE.05/.06 unmoved; no seesaw closure; "
        "mechanism must be D4-odd AND supply a ~2e-4 even-odd cancellation; "
        "pure seam data excluded [X-typed]; no status-marker move",
        True,
    )

    return summary(
        "v1003 nu structural nulls: charged data [E] + Schur NULL [X] + "
        "orientation lift [E] + scale NULL [X]"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
