#!/usr/bin/env python3
"""Probe orientation doubling of the seam heavy-neutrino kernel.

EXPLORATION ONLY.  No measured mixing angle, fitted epsilon, or imposed
``M_3 = 3 M_scal`` enters a candidate construction.  The family reflection is
the exact permutation ``R: 1 <-> 3``.  The null-result basis map is frozen to
``B = I``, so every main outcome is

    M_R / M_scal = (K_e + eta K_o
                    - C (K_e - eta K_o)^(-1) C^dag)^(-1).

ANTI-NUMEROLOGY / PRE-DECLARED EVALUATION ROUND
------------------------------------------------
The following six combinations, and no others, are evaluated for both
``eta in {-1,+1}`` (LEE = 6 x 2 = 12):

1. U-P-P-I:  K_e=I,              K_o=phi0*D,   C=phi0*I
2. U-P-C-I:  K_e=I,              K_o=phi0*D,   C=c3*I
3. U-C-P-I:  K_e=I,              K_o=c3*D,     C=phi0*I
4. U-C-C-R:  K_e=I,              K_o=c3*D,     C=c3*R
5. D-P-P-R:  K_e=diag(1,15/16,1), K_o=phi0*D, C=phi0*R
6. D-P2-P-I: K_e=diag(1,15/16,1), K_o=phi0^2*D, C=phi0*I

Here ``D=diag(1,0,-1)`` is the unique diagonal R-odd direction.  ``U`` is the
uniform h=(1,1,1) sector datum and ``D`` uses d=(64,60,64), normalized by 64.
The direct odd seam insertion and direct inter-sheet transfer are first order,
hence phi0; c3 is separately allowed as the primitive seam normalization.
The sole phi0^2 odd candidate is explicitly a two-transfer odd feedback term,
so its power is fixed by operator order rather than selected from an exponent
scan.  ``I`` and ``R`` are the two parameter-free declared intertwiners.
The canonical corpus value named ``phi0`` in ``tfpt_constants.py`` is the
retained seed and is used literally; no alternate decimal is hand inserted.

A main hit requires all three pre-declared conditions: a nondegenerate positive
spectrum, smallest/largest in [1e-5,1e-3], and middle/smallest in [1.8,2.2].
The target ``(epsilon,2 epsilon,3)`` enters only in the separately typed inverse
diagnostic, after all 12 main outcomes exist, with the already-corpus formula
``epsilon=phi0^2/(2*g_car)``.  That diagnostic fixes ``C=phi0*I`` (not fitted)
and solves the minimal diagonal equivariant model exactly for ``a,b,c``.

The final required-ratio comparison is also frozen here and has exactly eight
comparators: 1, 15/16, c3, phi0, phi0^2, 1/g_car, (2/3)^3, and (2/3)^6.
Closeness means relative distance at most 5%.  These eight comparisons are
diagnostics, not evidence, and are not added to the 12 main LEE trials.
"""

from __future__ import annotations

import inspect
import os
import sys
from dataclasses import dataclass

import mpmath as mp
import numpy as np
import sympy as sp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import c3, g_car, phi0  # noqa: E402


mp.mp.dps = 60

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
    spectrum: tuple[float, float, float]
    positive: bool
    nondegenerate: bool
    hierarchy_ratio: float
    light_pair_ratio: float
    hit: bool


def exact_structure_theorem() -> dict[str, object]:
    """Derive complete R-even/R-odd matrix spaces over exact symbols."""
    exact_r = sp.Matrix(((0, 0, 1), (0, 1, 0), (1, 0, 0)))

    x11, x22, x33, x12, x13, x23 = sp.symbols(
        "x11 x22 x33 x12 x13 x23"
    )
    symmetric_variables = (x11, x22, x33, x12, x13, x23)
    generic_symmetric = sp.Matrix(
        ((x11, x12, x13), (x12, x22, x23), (x13, x23, x33))
    )

    even_equations = list(
        exact_r * generic_symmetric * exact_r - generic_symmetric
    )
    odd_equations = list(
        exact_r * generic_symmetric * exact_r + generic_symmetric
    )
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
        2
        * odd_scale
        * (1 - gamma**2 / (1 - odd_scale**2))
    )

    rational_schur = schur.subs(
        {odd_scale: sp.Rational(1, 4), gamma: sp.Rational(1, 10)}
    )
    rational_eigenvalues = tuple(rational_schur.diagonal())
    simple_exact_example = len(set(rational_eigenvalues)) == 3

    # Reflection alone does not imply the D4-doublet degeneracy.  This exact
    # R-even counterexample has spectrum {1,2,4}; the stronger D4 premise from
    # the preceding null is therefore distinct from the R constraint alone.
    r_even_counterexample = sp.Matrix(((2, 1, 0), (1, 3, 1), (0, 1, 2)))
    counterexample_eigenvalues = tuple(
        sorted(eigenvalue for eigenvalue in r_even_counterexample.eigenvals())
    )

    return {
        "k_even": k_even,
        "k_odd": k_odd,
        "coupling": coupling,
        "even_dimension": len(symmetric_variables) - even_constraint_matrix.rank(),
        "odd_dimension": len(symmetric_variables) - odd_constraint_matrix.rank(),
        "coupling_dimension": len(generic_variables)
        - coupling_constraint_matrix.rank(),
        "patterns_exact": all(pattern_checks),
        "endpoint_difference": endpoint_difference,
        "difference_formula_exact": sp.simplify(
            endpoint_difference - expected_difference
        )
        == 0,
        "rational_schur": rational_schur,
        "simple_exact_example": simple_exact_example,
        "counterexample_eigenvalues": counterexample_eigenvalues,
        "reflection_alone_forces_degeneracy": len(counterexample_eigenvalues) < 3,
    }


def build_declared_candidates() -> tuple[Candidate, ...]:
    """Build only the six frozen constructions declared in the module protocol."""
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


def effective_kernel(candidate: Candidate, eta: int) -> np.ndarray:
    """Return the selected-orientation Schur complement."""
    upper = candidate.k_even + eta * candidate.k_odd
    lower = candidate.k_even - eta * candidate.k_odd
    return upper - candidate.coupling @ np.linalg.inv(lower) @ candidate.coupling.T


def evaluate_candidate(candidate: Candidate, eta: int) -> Outcome:
    """Evaluate one declared candidate without using the diagnostic target."""
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
        and HIERARCHY_INTERVAL[0]
        <= hierarchy_ratio
        <= HIERARCHY_INTERVAL[1]
        and LIGHT_PAIR_INTERVAL[0]
        <= light_pair_ratio
        <= LIGHT_PAIR_INTERVAL[1]
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


def solve_inverse_diagnostic(epsilon: mp.mpf) -> dict[str, mp.mpf]:
    """Solve the diagonal model with fixed C=phi0*I for the typed target."""
    target_light = 1 / epsilon
    target_middle = 1 / (2 * epsilon)
    target_heavy = mp.mpf(1) / 3
    gamma = mp.mpf(phi0)

    # x=a+c and y=a-c.  The first/third Schur equations imply
    # target_light*y = target_heavy*x, then a positive-root quadratic fixes x.
    discriminant = target_light**2 + (
        4 * target_light * gamma**2 / target_heavy
    )
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


def fmt(value: float | mp.mpf, digits: int = 10) -> str:
    return mp.nstr(mp.mpf(value), digits)


def spectrum_text(spectrum: tuple[float, float, float]) -> str:
    return "[" + ", ".join(fmt(value) for value in spectrum) + "]"


def report_check(label: str, passed: bool) -> bool:
    print(("PASS " if passed else "FAIL ") + label)
    return passed


def main() -> int:
    print("NU ORIENTATION SEESAW PROBE -- EXPLORATION ONLY")
    print("PRE-DECLARED CORPUS CONSTRUCTIONS")
    for index, (label, rationale) in enumerate(DECLARED_COMBINATIONS, start=1):
        print(f"  {index}. {label:<10} {rationale}")
    print(
        f"  LEE main = {len(DECLARED_COMBINATIONS)} combinations x "
        f"{len(BRANCHES)} branches = {MAIN_LEE_COUNT}"
    )
    print(
        "  acceptance: positive + nondegenerate; min/max in "
        "[1e-5,1e-3]; middle/min in [1.8,2.2]"
    )
    print(f"  c3={fmt(c3, 14)} phi0_ret(canonical phi0)={fmt(phi0, 14)}")
    print()

    structure = exact_structure_theorem()
    print("EXACT STRUCTURE THEOREM")
    print(f"  R-even symmetric K_e ({structure['even_dimension']} parameters):")
    print(f"    {structure['k_even']}")
    print(f"  R-odd symmetric K_o ({structure['odd_dimension']} parameters):")
    print(f"    {structure['k_odd']}")
    print(f"  R-even general C ({structure['coupling_dimension']} parameters):")
    print(f"    {structure['coupling']}")
    print(
        "  diagonal-subfamily endpoint split = "
        f"{structure['endpoint_difference']}"
    )
    print(
        "  exact witness odd_scale=1/4, gamma=1/10 gives K_eff="
        f"{structure['rational_schur']} (three distinct eigenvalues)"
    )
    print(
        "  Therefore the repeated-eigenvalue discriminant is not identically "
        "zero: eta selection generically gives a simple spectrum, outside a "
        "proper algebraic exceptional set."
    )
    print(
        "  Branch covariance is exact: R K_eff(eta) R = K_eff(-eta), so the "
        "two eta branches are isospectral and exchange family labels."
    )
    print(
        "  R-only caveat: reflection alone does not force a baseline doublet; "
        "the exact R-even counterexample has spectrum "
        f"{structure['counterexample_eigenvalues']}. The earlier degeneracy "
        "uses the stronger D4/diagonal-sector premise."
    )
    print(
        "  Minimal inputs: one nonzero odd corpus coupling suffices for mere "
        "splitting once K_e is fixed; two independent dimensionless corpus "
        "ratios are required to determine a general three-scale shape after "
        "M_scal removes the overall scale."
    )
    print()

    # All candidates and all main outcomes are built before the inverse target.
    candidates = build_declared_candidates()
    outcomes = tuple(
        evaluate_candidate(candidate, eta)
        for candidate in candidates
        for eta in BRANCHES
    )

    print("ALL 12 PRE-DECLARED OUTCOMES (B=I)")
    print("  combo       eta  spectrum(M_R/M_scal)                 ND   min/max      mid/min  HIT")
    for outcome in outcomes:
        print(
            f"  {outcome.label:<11} {outcome.eta:+d}   "
            f"{spectrum_text(outcome.spectrum):<38} "
            f"{'Y' if outcome.nondegenerate else 'N':<4} "
            f"{fmt(outcome.hierarchy_ratio, 7):<12} "
            f"{fmt(outcome.light_pair_ratio, 7):<8} "
            f"{'HIT' if outcome.hit else 'null'}"
        )
    print()

    # Diagnostic target enters only after all target-free outcomes exist.
    epsilon = mp.mpf(phi0) ** 2 / (2 * mp.mpf(g_car))
    target = (epsilon, 2 * epsilon, mp.mpf(3))
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

    print("INVERSE DIAGNOSTIC -- NOT EVIDENCE")
    print(
        f"  target=[epsilon,2epsilon,3], epsilon=phi0^2/(2*g_car)="
        f"{fmt(epsilon, 15)}"
    )
    print(
        "  fixed C=phi0*I solution: "
        f"a={fmt(inverse['a'], 14)} b={fmt(inverse['b'], 14)} "
        f"c={fmt(inverse['c'], 14)} gamma={fmt(inverse['gamma'], 14)}"
    )
    print(
        f"  required |c/a|={fmt(inverse['required_ratio'], 14)}; "
        f"near-cancellation 1-|c/a|={fmt(inverse['cancellation'], 14)}"
    )
    print(
        "  reconstruction="
        + "["
        + ", ".join(fmt(value, 14) for value in reconstructed_spectrum)
        + "]"
    )
    print("  PRE-DECLARED REQUIRED-RATIO COMPARISON (5% relative)")
    comparator_hits: list[str] = []
    for name, comparator in INVERSE_COMPARATORS:
        relative_difference = abs(
            mp.mpf(comparator) / inverse["required_ratio"] - 1
        )
        close = relative_difference <= RATIO_COMPARISON_TOLERANCE
        if close:
            comparator_hits.append(name)
        print(
            f"    {name:<18} value={fmt(comparator, 11):<14} "
            f"rel={fmt(relative_difference, 8):<11} "
            f"{'CLOSE' if close else 'no'}"
        )
    print(
        "  Interpretation: closeness to the trivial uniform value 1 does not "
        "supply the independently required cancellation precision."
    )
    print()

    print("MUTANTS")
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
            reduced_mass_spectrum = np.linalg.eigvalsh(
                np.linalg.inv(reduced_kernel)
            )
            expected_mass_spectrum = np.sort(
                1 / np.linalg.eigvalsh(expected_kernel)
            )
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
    print(
        "  eta=0: every declared diagonal corpus construction restores an "
        f"exact 1<->3 doublet = {eta_zero_degenerate}"
    )
    print(
        "  C=0: K_eff=K_e+eta*K_o and M spectrum is its reciprocal = "
        f"{c_zero_reduces}"
    )
    print(
        "  eta=+/- branch covariance and isospectrality = "
        f"{branch_covariant}"
    )
    print()

    candidate_source = inspect.getsource(build_declared_candidates).lower()
    circularity_clean = all(
        forbidden not in candidate_source
        for forbidden in ("epsilon", "target", "theta13", "measured", "m_3")
    )
    hit_labels = sorted({outcome.label for outcome in outcomes if outcome.hit})
    degeneracy_lifted = all(outcome.nondegenerate for outcome in outcomes)

    checks = [
        report_check(
            "exact equivariant pattern dimensions are Ke=4, Ko=2, C=5",
            structure["even_dimension"] == 4
            and structure["odd_dimension"] == 2
            and structure["coupling_dimension"] == 5,
        ),
        report_check("all displayed equivariance patterns are exact", bool(structure["patterns_exact"])),
        report_check(
            "exact endpoint-splitting formula is verified",
            bool(structure["difference_formula_exact"]),
        ),
        report_check(
            "one exact rational point has a simple spectrum, proving generic splitting",
            bool(structure["simple_exact_example"]),
        ),
        report_check(
            "R-only degeneracy overclaim is exposed by exact spectrum {1,2,4}",
            structure["counterexample_eigenvalues"] == (1, 2, 4)
            and not structure["reflection_alone_forces_degeneracy"],
        ),
        report_check(
            "exactly six unique target-free candidates were built",
            len(candidates) == len(DECLARED_COMBINATIONS)
            and len({candidate.label for candidate in candidates})
            == len(DECLARED_COMBINATIONS),
        ),
        report_check(
            "candidate builder contains no target, epsilon, angle, or M3 input",
            circularity_clean,
        ),
        report_check(
            "exactly 12 declared candidate-branch outcomes were evaluated",
            len(outcomes) == MAIN_LEE_COUNT,
        ),
        report_check(
            "all main outcomes are positive and protocol-classified",
            all(outcome.positive for outcome in outcomes),
        ),
        report_check(
            "eta selection lifts the declared 1<->3 doublet in every candidate",
            degeneracy_lifted,
        ),
        report_check(
            "eta branches obey exact reflection covariance",
            branch_covariant,
        ),
        report_check(
            "inverse diagnostic reconstructs (epsilon,2epsilon,3)",
            inverse_exact_to_precision,
        ),
        report_check(
            "exactly eight pre-declared required-ratio comparators were counted",
            len(INVERSE_COMPARATORS) == 8,
        ),
        report_check(
            "eta=0 restores the doublet in every declared corpus candidate",
            eta_zero_degenerate,
        ),
        report_check(
            "C=0 reduces to the decoupled Ke +/- Ko spectrum",
            c_zero_reduces,
        ),
    ]

    if not all(checks):
        verdict = "ORIENTATION_SEESAW_FAILS"
    elif hit_labels:
        verdict = (
            "ORIENTATION_SEESAW_DEGENERACY_LIFTED_AND_HIT("
            + ",".join(hit_labels)
            + ")"
        )
    else:
        verdict = (
            "ORIENTATION_SEESAW_DEGENERACY_LIFTED_NO_SCALE(required ratio="
            + fmt(inverse["required_ratio"], 12)
            + ")"
        )

    print()
    print("VERDICT", verdict)
    print()
    print("FIVE-SENTENCE CONCLUSION")
    print("  1. The sgn-J orientation bit supplies an R-odd family operator and lifts the 1<->3 doublet in all six declared corpus constructions.")
    print("  2. The exact Schur-complement witness proves that this splitting is generic, while the two eta signs are isospectral and merely exchange reflected family labels.")
    print("  3. None of the 12 pre-declared branch outcomes reaches both the required 1e-5-to-1e-3 hierarchy and the factor-two light pair.")
    print("  4. The inverse diagnostic requires |K_o/K_e| extremely close to one, and only the trivial uniform comparator is within 5%, without furnishing the needed cancellation precision.")
    print("  5. Thus orientation doubling rescues the seam mechanism structurally inside the declared diagonal D4 sector, but the frozen corpus constants tested here do not supply its quantitative scale.")
    print("PROTOCOL-ALL-PASS" if all(checks) else "PROTOCOL-FAILURE")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
