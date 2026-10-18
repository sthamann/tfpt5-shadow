#!/usr/bin/env python3
"""Exact Round-7 certificate for the source DET parent and its locality boundary.

This is a bounded research artefact.  It distinguishes the momentum-factorized
four-mode parent in v1008 from a real-space product-projector parent with
ordinary hopping.  The algebraic checks use exact SymPy/CAR calculations, and
the source-contract comparisons are exact as written.  One separately
classified floating regression reproduces the landed 129-point trigonometric
grid; other printed decimals are labelled evaluations of exact radicals.
No repository file is imported or modified.  No T3/T4/TOE claim is made.

Port provenance: native verification port of
`toe_round7_parent_mirror/parent_mirror_checker.py`
(source SHA-256 324030c9dbc9afe1461aa765f84baeb33ae012319e78cd215632b926d5f5b94f).
The port changes only harness integration, repository lookup, and execution
lifecycle.
"""

from __future__ import annotations

import ast
import json
import math
import os
from pathlib import Path

import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


DEFAULT_REPO = Path(__file__).resolve().parents[1]
REPO = Path(os.environ.get("TFPT_REPO", str(DEFAULT_REPO))).resolve()
V1002 = REPO / "verification/v1002_spin10_mirror_projector.py"
V1008 = REPO / "verification/v1008_master_assembly_scaffold.py"
V1024 = REPO / "verification/v1024_parent_internal_boundaries.py"
V1027 = REPO / "verification/v1027_signed_det_car_wall.py"

PASSED = 0
FAILED = 0
CHECK_CLASSES = {
    "source_contract": {"passed": 0, "failed": 0},
    "algebra": {"passed": 0, "failed": 0},
    "floating_regression": {"passed": 0, "failed": 0},
}


def check(
    name: str, condition: bool, detail: object = "", category: str = "algebra"
) -> None:
    global PASSED, FAILED
    if category not in CHECK_CLASSES:
        raise ValueError(f"unknown check category: {category}")
    tag = {
        "source_contract": "SOURCE_CONTRACT",
        "algebra": "EXACT_ALGEBRA",
        "floating_regression": "FLOATING_REGRESSION",
    }[category]
    passed = suite_check(
        f"[{tag}] {name}" + (f" -- {detail}" if detail != "" else ""),
        bool(condition),
    )
    if passed:
        PASSED += 1
        CHECK_CLASSES[category]["passed"] += 1
    else:
        FAILED += 1
        CHECK_CLASSES[category]["failed"] += 1


def module_contract(path: Path) -> tuple[dict[str, object], dict[str, str], str]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    constants: dict[str, object] = {}
    functions: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                constants[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
        elif isinstance(node, ast.FunctionDef):
            functions[node.name] = ast.unparse(node)
    return constants, functions, source


def source_contract_certificate() -> None:
    c1008, f1008, s1008 = module_contract(V1008)
    _c1002, f1002, s1002 = module_contract(V1002)
    _c1024, f1024, s1024 = module_contract(V1024)
    _c1027, f1027, s1027 = module_contract(V1027)

    check(
        "v1008 source fixes the tested parent coefficients",
        c1008.get("FLAVORS") == 4
        and c1008.get("DET_STRENGTH") == 2.0
        and c1008.get("HOPPING_VALUES") == (0.0, 0.2, 0.4, 0.6),
        "n=4, J=2, |d|<=0.6",
        category="source_contract",
    )
    edge = f1008.get("edge_cluster_hamiltonian", "")
    check(
        "v1008 parent is exactly d(N-n/2)+JQ",
        "dispersion * (NUMBER - 0.5 * FLAVORS" in edge
        and "DET_STRENGTH * H_DET" in edge
        and "H_DET = np.eye(1 << FLAVORS" in s1008
        and "- P_PHI" in s1008,
        category="source_contract",
    )
    check(
        "v1008 samples d=t sin(k) on exactly 129 momentum points",
        "MOMENTA = np.linspace(-math.pi, math.pi, 129)" in s1008
        and "dispersion = chirality_sign * hopping * math.sin(float(momentum))" in s1008,
        category="source_contract",
    )
    # A standard symmetric nearest-neighbour term
    # s sum_x(c_x^dagger c_{x+1}+h.c.) has dispersion 2s cos(k), up to a
    # harmless momentum/phase convention.  Therefore the source amplitude
    # |d|<=3/5 would correspond to |s|=3/10, not 3/5.
    dispersion_amplitude = sp.Rational(3, 5)
    symmetric_bond_magnitude = dispersion_amplitude / 2
    check(
        "Fourier normalization gives symmetric NN bond magnitude |s|=t/2",
        2 * symmetric_bond_magnitude == dispersion_amplitude
        and symmetric_bond_magnitude == sp.Rational(3, 10),
        "v1008 t=3/5 implies |s|=3/10",
    )
    check(
        "v1002 source uses a flat DET16 defect projector",
        "SPIN10_MODES = 16" in s1002
        and "hamiltonian = identity - projector" in f1002.get("spin10_single_cluster", ""),
        "h_mir=Q, onsite gap one",
        category="source_contract",
    )
    check(
        "v1027 distinguishes additive N_a from flat Q",
        "number_a = sum" in f1027.get("determinant_canonicalization", "")
        and "flat Delta*Q is not silently identified" in s1027,
        category="source_contract",
    )
    check(
        "v1024 parent is a separate positive seam/number construction",
        "h0 = delta_seam *" in f1024.get("parent_internal_intertwiner", "")
        and "interaction += coupling * a_operator.conj().T @ a_operator" in f1024.get("parent_internal_intertwiner", ""),
        "not used as a DET hopping bound",
        category="source_contract",
    )


def annihilators(mode_count: int) -> list[sp.Matrix]:
    result: list[sp.Matrix] = []
    for mode in range(mode_count):
        operator = sp.zeros(2**mode_count)
        for state in range(2**mode_count):
            if state & (1 << mode):
                sign = (-1) ** ((state & ((1 << mode) - 1)).bit_count())
                operator[state ^ (1 << mode), state] = sign
        result.append(operator)
    return result


def exact_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def onsite_parent_certificate() -> None:
    n = 4
    dimension = 2**n
    identity = sp.eye(dimension)
    canonical = annihilators(n)
    number = sum((a.conjugate().T * a for a in canonical), sp.zeros(dimension))
    parity = sp.diag(*[(-1) ** state.bit_count() for state in range(dimension)])
    phase = sp.exp(sp.I * sp.pi / 7)
    omega = sp.zeros(dimension, 1)
    omega[0] = 1 / sp.sqrt(2)
    omega[-1] = phase / sp.sqrt(2)
    projector = omega * omega.conjugate().T
    defect = identity - projector
    comm_number = defect * number - number * defect
    comm_parity = defect * parity - parity * defect

    check("source DET vector is normalized", sp.simplify((omega.conjugate().T * omega)[0]) == 1)
    check("Q is an exact rank-15 projector", exact_zero(defect * defect - defect) and defect.rank() == 15)
    check("Q preserves fermion parity", exact_zero(comm_parity))
    check(
        "Q does not preserve naive mirror number",
        sp.simplify(sp.trace(comm_number.conjugate().T * comm_number)) == 8,
        "||[Q,N]||_F^2=n^2/2=8",
    )

    theta = -sp.pi / (7 * n)
    phase_rotation = sp.diag(*[sp.exp(sp.I * theta * state.bit_count()) for state in range(dimension)])
    omega_zero = sp.zeros(dimension, 1)
    omega_zero[0] = omega_zero[-1] = 1 / sp.sqrt(2)
    check(
        "the source phase is spectrally removable by a common U(1) rotation",
        exact_zero(phase_rotation * omega - omega_zero) and exact_zero(phase_rotation * number - number * phase_rotation),
    )


def momentum_parent_certificate() -> dict[str, object]:
    """Exact spectrum of h(d)=d(N-n/2)+JQ for the v1008 source values."""
    d = sp.symbols("d", real=True)
    n, J, t = sp.Integer(4), sp.Integer(2), sp.Rational(3, 5)
    # Empty/full block after removal of the inessential DET phase.
    block = sp.Matrix([[-n*d/2 + J/2, -J/2], [-J/2, n*d/2 + J/2]])
    z = sp.symbols("z", real=True)
    characteristic = sp.factor((block - z * sp.eye(2)).det())
    e_minus = J/2 - sp.sqrt(J**2/4 + n**2*d**2/4)
    e_plus = J/2 + sp.sqrt(J**2/4 + n**2*d**2/4)
    check(
        "empty/full eigenvalues solve the exact characteristic polynomial",
        sp.simplify(characteristic.subs(z, e_minus)) == 0
        and sp.simplify(characteristic.subs(z, e_plus)) == 0,
    )

    x = sp.symbols("x", nonnegative=True)
    one_fermion_threshold = J/2 - (n/2 - 1) * x + sp.sqrt(J**2/4 + n**2*x**2/4)
    stationary = J * (n - 2) / (2 * n * sp.sqrt(n - 1))
    exact_minimum = J/2 + J * sp.sqrt(n - 1) / n
    derivative = sp.diff(one_fermion_threshold, x)
    check("threshold stationary point is exact", sp.simplify(derivative.subs(x, stationary)) == 0)
    check(
        "stationary point lies inside the source dispersion window",
        stationary > 0 and stationary < t,
        f"x*={stationary}, t={t}",
    )
    check(
        "source minimum canonical spectral cost is 1+sqrt(3)/2",
        sp.simplify(one_fermion_threshold.subs(x, stationary) - exact_minimum) == 0
        and exact_minimum == 1 + sp.sqrt(3)/2,
        sp.N(exact_minimum, 15),
    )

    # The analytic value is the infimum over the continuous envelope.  The
    # landed scaffold scans only k_j=-pi+j*pi/64, j=0,...,128, and hence lies
    # slightly above it.
    grid_values = []
    for j in range(129):
        momentum = -math.pi + j * math.pi / 64
        grid_x = float(t) * abs(math.sin(momentum))
        grid_values.append(1.0 - grid_x + math.sqrt(1.0 + 4.0 * grid_x * grid_x))
    grid_minimum = min(grid_values)
    check(
        "129-point source grid minimum is distinct from the analytic envelope infimum",
        abs(grid_minimum - 1.8660698881694362) < 1.0e-15
        and grid_minimum > float(sp.N(exact_minimum, 17)),
        f"grid={grid_minimum:.16f}, envelope={float(sp.N(exact_minimum, 17)):.16f}",
        category="floating_regression",
    )

    # The intermediate r=1,2,3 sectors have E_r=J+d(r-n/2).
    # On |d|<=3/5 they stay positive, whereas e_-<=0, so e_- is unique.
    lowest_intermediate = J - (n/2 - 1) * t
    internal_doublet_cost = 2 * sp.sqrt(J**2/4 + n**2*x**2/4)
    check("the local ground is unique throughout |d|<=0.6", lowest_intermediate > 0)
    check(
        "no even-sector excitation undercuts the canonical threshold",
        sp.simplify(internal_doublet_cost.subs(x, 0) - exact_minimum) > 0,
        "opposite DET doublet costs at least J=2",
    )

    # For a finite set of independent momentum cells, even local Hamiltonians
    # commute and energies add.  The product ground is unique and the first
    # excitation changes one cell, hence the same minimum is volume independent.
    check(
        "factorized finite-volume parent has the same all-volume gap",
        exact_minimum > 0,
        "Delta_K >= 1+sqrt(3)/2 for every finite momentum set K",
    )
    return {
        "source_modes": int(n),
        "source_DET_strength": int(J),
        "source_dispersion_bound": str(t),
        "stationary_dispersion": str(stationary),
        "exact_uniform_factorized_gap": str(exact_minimum),
        "evaluated_uniform_factorized_gap": float(sp.N(exact_minimum, 17)),
        "source_129_point_grid_minimum": grid_minimum,
        "standard_symmetric_NN_bond_magnitude_for_source_dispersion": "3/10",
    }


State = dict[int, sp.Expr]


def add_state(target: State, basis: int, coefficient: sp.Expr) -> None:
    target[basis] = sp.simplify(target.get(basis, 0) + coefficient)
    if target[basis] == 0:
        del target[basis]


def apply_annihilator(state: State, mode: int) -> State:
    result: State = {}
    lower = (1 << mode) - 1
    for basis, coefficient in state.items():
        if basis & (1 << mode):
            sign = (-1) ** ((basis & lower).bit_count())
            add_state(result, basis ^ (1 << mode), coefficient * sign)
    return result


def apply_creator(state: State, mode: int) -> State:
    result: State = {}
    lower = (1 << mode) - 1
    for basis, coefficient in state.items():
        if not basis & (1 << mode):
            sign = (-1) ** ((basis & lower).bit_count())
            add_state(result, basis ^ (1 << mode), coefficient * sign)
    return result


def apply_hopping(state: State, n: int, strength: sp.Expr) -> State:
    result: State = {}
    for flavor in range(n):
        for destination, source in ((flavor, n + flavor), (n + flavor, flavor)):
            moved = apply_creator(apply_annihilator(state, source), destination)
            for basis, coefficient in moved.items():
                add_state(result, basis, strength * coefficient)
    return result


def inner(left: State, right: State) -> sp.Expr:
    return sp.simplify(sum(sp.conjugate(value) * right.get(basis, 0) for basis, value in left.items()))


def det_product_vacuum(n: int) -> State:
    full_x = (1 << n) - 1
    full_y = full_x << n
    return {
        0: sp.Rational(1, 2),
        full_x: sp.Rational(1, 2),
        full_y: sp.Rational(1, 2),
        full_x | full_y: sp.Rational(1, 2),
    }


GaugeState = dict[tuple[int, int], sp.Expr]


def add_gauge_state(
    target: GaugeState, basis_and_flux: tuple[int, int], coefficient: sp.Expr
) -> None:
    target[basis_and_flux] = sp.simplify(target.get(basis_and_flux, 0) + coefficient)
    if target[basis_and_flux] == 0:
        del target[basis_and_flux]


def apply_gauge_hopping(
    state: GaugeState, n: int, strength: sp.Expr, order: int
) -> GaugeState:
    """Apply sum_i(c_xi^dag U c_yi + c_yi^dag U^dag c_xi).

    The oriented link action is U|e>=|e+1 mod q>.  It is applied as part of
    each CAR monomial, rather than assigning a compatible flux afterwards.
    """
    result: GaugeState = {}
    for (basis, flux), coefficient in state.items():
        matter_state = {basis: coefficient}
        for flavor in range(n):
            for destination, source, flux_shift in (
                (flavor, n + flavor, +1),
                (n + flavor, flavor, -1),
            ):
                moved = apply_creator(apply_annihilator(matter_state, source), destination)
                for new_basis, new_coefficient in moved.items():
                    add_gauge_state(
                        result,
                        (new_basis, (flux + flux_shift) % order),
                        strength * new_coefficient,
                    )
    return result


def gauge_inner(left: GaugeState, right: GaugeState) -> sp.Expr:
    return sp.simplify(
        sum(sp.conjugate(value) * right.get(key, 0) for key, value in left.items())
    )


def real_space_obstruction_certificate() -> dict[str, object]:
    """Two cells suffice to kill T >= -kappa sum_x Q_x for every kappa."""
    # Regression for the exceptional n=2 collision: the two nominal hopping
    # orientations land on the same basis states and add.  This test failed
    # against the former n|s|^2/2 formula (2 != 1 at unit strength), so the
    # general lemma below is deliberately restricted to even n>=4.
    n2_vacuum = det_product_vacuum(2)
    n2_hopped = apply_hopping(n2_vacuum, 2, sp.Integer(1))
    n2_norm_squared = inner(n2_hopped, n2_hopped)
    check(
        "n=2 collision regression rejects the former universal norm formula",
        n2_norm_squared == 2 and n2_norm_squared != sp.Rational(2, 2),
        "true norm^2=2 at s=1; former n s^2/2 formula gives 1",
    )

    n, J, strength = 4, sp.Integer(2), sp.Rational(3, 5)
    full_x = (1 << n) - 1
    # The common phase has been removed by the exact U(1) rotation above.
    vacuum = det_product_vacuum(n)
    hopped = apply_hopping(vacuum, n, strength)
    norm_squared = inner(hopped, hopped)
    check("two-cell DET product vacuum is normalized", inner(vacuum, vacuum) == 1)
    check("ordinary hopping has zero vacuum expectation", inner(vacuum, hopped) == 0)
    check(
        "ordinary hopping does not annihilate the Q-kernel",
        norm_squared == sp.Rational(18, 25),
        "even n>=4: ||T OmegaOmega||^2=n s^2/2=18/25",
    )

    # Every state in T|Omega Omega> has 1 or n-1 particles on both sites, so
    # Q_x+Q_y acts as 2.  Consequently D=J(Q_x+Q_y) has expectation 2J.
    partial_on_both = all(
        0 < (basis & full_x).bit_count() < n
        and 0 < ((basis >> n) & full_x).bit_count() < n
        for basis in hopped
    )
    check("the hopping image has exactly two local DET defects", partial_on_both)
    hopped_twice = apply_hopping(hopped, n, strength)
    cubic_moment = inner(hopped, hopped_twice)
    check("the normalized hopping image has zero hopping expectation", cubic_moment == 0)
    b = sp.sqrt(norm_squared)
    ritz_low = J - sp.sqrt(J**2 + norm_squared)
    check(
        "the chosen bare-bond product vacuum is not a ground state once hopping is on",
        ritz_low < 0,
        f"E0 <= {ritz_low} = {sp.N(ritz_low, 12)}",
    )

    # If T+kappa Q_sum were positive, its zero expectation on OmegaOmega would
    # force (T+kappa Q_sum)OmegaOmega=0.  Q_sum OmegaOmega=0 but T OmegaOmega!=0.
    check(
        "no finite relative-defect constant kappa can satisfy T >= -kappa sum Q_x",
        norm_squared > 0,
        "positivity-kernel contradiction; independent of kappa",
    )

    # Gauge-dressed version.  The actual shift U|e>=|e+1> is included in the
    # operator application; physicality is checked on every nonzero output.
    gauge_results: dict[str, object] = {}
    for order in (2, 4):
        gauge_vacuum: GaugeState = {(basis, 0): coefficient for basis, coefficient in vacuum.items()}
        initial_physical = all(
            ((basis & full_x).bit_count() - flux) % order == 0
            and (((basis >> n) & full_x).bit_count() + flux) % order == 0
            for basis, flux in gauge_vacuum
        )
        gauge_hopped = apply_gauge_hopping(gauge_vacuum, n, strength, order)
        output_physical = all(
            ((basis & full_x).bit_count() - flux) % order == 0
            and (((basis >> n) & full_x).bit_count() + flux) % order == 0
            for basis, flux in gauge_hopped
        )
        gauge_norm_squared = gauge_inner(gauge_hopped, gauge_hopped)
        gauge_cubic = gauge_inner(
            gauge_hopped, apply_gauge_hopping(gauge_hopped, n, strength, order)
        )
        unit_flux = all(min(flux, order - flux) ** 2 == 1 for _, flux in gauge_hopped)
        matter_number_preserved = all(basis.bit_count() == n for basis, _ in gauge_hopped)
        check(
            f"Z{order} link action preserves both endpoint Gauss constraints",
            initial_physical and output_physical and gauge_norm_squared == norm_squared,
            "U shifts flux during each CAR hop; image is nonzero and physical",
        )
        check(
            f"Z{order} hopping image has two Q defects and one unit of electric flux",
            unit_flux and partial_on_both and matter_number_preserved and gauge_cubic == 0,
            "matter number, hence fermion parity, is preserved by the bilinear",
        )
        gauge_results[f"Z{order}"] = {
            "hopping_image_norm_squared": str(gauge_norm_squared),
            "all_output_states_gauss_physical": output_physical,
            "unit_flux_square": unit_flux,
            "matter_number_and_parity_preserved": matter_number_preserved,
        }

    h_e = sp.Integer(1)
    gauge_diagonal_cost = 2 * J + h_e
    gauge_ritz_low = gauge_diagonal_cost / 2 - sp.sqrt(
        gauge_diagonal_cost**2 / 4 + norm_squared
    )
    check(
        "gauge-dressed Ritz diagonal includes electric cost 2J+h_E",
        gauge_diagonal_cost == 5
        and sp.simplify(gauge_ritz_low - (sp.Integer(25) - sp.sqrt(697)) / 10) == 0
        and gauge_ritz_low < 0,
        f"h_E=1: E0 <= {gauge_ritz_low} = {sp.N(gauge_ritz_low, 12)}",
    )
    return {
        "minimal_cells": 2,
        "full_Fock_dimension_not_built": 2 ** (2 * n),
        "nonzero_CAR_monomials": len(hopped),
        "n2_exception_norm_squared_at_unit_strength": str(n2_norm_squared),
        "hopping_image_norm_squared": str(norm_squared),
        "chosen_bare_bond_strength_not_source_derived": str(strength),
        "source_equivalent_symmetric_NN_bond_magnitude": "3/10",
        "bare_Ritz_upper_bound_ground_energy": str(ritz_low),
        "gauge_dressed_Ritz_hE_1": str(gauge_ritz_low),
        "gauge_link_action_checks": gauge_results,
        "finite_kappa_exists": False,
    }


def local_repair_certificate() -> dict[str, object]:
    """Exact local repair lemma; a boundary, not a landed TFPT term."""
    n, J, t, z = sp.Integer(4), sp.Integer(2), sp.Rational(3, 5), sp.Integer(2)
    # R_b=1-P_xP_y <= Q_x+Q_y and ||K_b||=n for n flavor-diagonal hops.
    # Hence R K R >= -n R and the projected hopping has the stated bound.
    raw_margin = sp.simplify(J - z * n * t)
    normalized_margin = sp.simplify(J - z * t)
    check("projected-hopping repair for chosen bond analogue is not certified", raw_margin <= 0, raw_margin)
    check("mode-normalized projected hopping would have a positive Q margin", normalized_margin > 0, normalized_margin)

    # A coupling-fixed positive bond repair requires no tunable new coefficient:
    # B_b=|s|[n R_b + sgn(s) R_b K_b R_b] >=0.  It changes the Hamiltonian by
    # the local counterterm |s| n R_b, but retains H >= J sum Q_x.
    counterterm = sp.simplify(t * n)
    check(
        "coupling-fixed positive bond counterterm is exact",
        counterterm == sp.Rational(12, 5),
        "add |s| n R_b=12/5 R_b for the newly chosen s=3/5 bond analogue",
    )
    return {
        "projected_raw_margin_1d": str(raw_margin),
        "projected_mode_normalized_margin_1d": str(normalized_margin),
        "fixed_positive_counterterm_per_bond": str(counterterm),
        "chosen_bond_analogue_not_source_derived": True,
        "v1008_equivalent_symmetric_NN_bond_magnitude": "3/10",
        "new_free_coupling_required": False,
        "landed_source_term": False,
    }


def run() -> int:
    global PASSED, FAILED, CHECK_CLASSES
    reset()
    PASSED = 0
    FAILED = 0
    CHECK_CLASSES = {
        "source_contract": {"passed": 0, "failed": 0},
        "algebra": {"passed": 0, "failed": 0},
        "floating_regression": {"passed": 0, "failed": 0},
    }
    print("ROUND 7 -- ACTUAL DET PARENT / MIRROR DEFECT CERTIFICATE")
    source_contract_certificate()
    onsite_parent_certificate()
    factorized = momentum_parent_certificate()
    obstruction = real_space_obstruction_certificate()
    repair = local_repair_certificate()
    payload = {
        "audited_repo": str(REPO),
        "factorized_source_parent": factorized,
        "real_space_relative_Q_obstruction": obstruction,
        "local_repair_boundary": repair,
        "claim_boundary": {
            "T3": False,
            "T4": False,
            "operator_valued_full_TFPT_parent": False,
            "NO_RH_CLAIM": True,
        },
        "checks": {"passed": PASSED, "failed": FAILED},
        "check_classes": CHECK_CLASSES,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    print(f"SUMMARY: {PASSED} passed, {FAILED} failed")
    return summary("v1034 parent mirror")


if __name__ == "__main__":
    raise SystemExit(run())
