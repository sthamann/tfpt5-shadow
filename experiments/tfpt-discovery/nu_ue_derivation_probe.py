#!/usr/bin/env python3
"""Inventory charged-lepton matrices and test the minimal Q_+ misalignment.

EXPLORATION ONLY.  No verification, paper, ledger, website, or scorecard edit.

QUESTION AND DECISION TREE (declared before evaluation)
-------------------------------------------------------
1. A corpus object counts as a charged-lepton mass matrix only if it acts on
   the three charged-lepton flavor states in a named physical basis.  A
   sector-by-generation address table, a C6 transport kernel, a family
   monodromy, a coefficient-algebra multiplication map, a light-neutrino
   Majorana matrix, or an assembled PMNS matrix does not count merely because
   it is 3x3 or has the charged-lepton coefficients as eigenvalues.
2. If such a non-diagonal mass matrix exists, diagonalize it and test U_e.
3. Otherwise the frozen source masses define diag(m_e,m_mu,m_tau) in their
   named mass order, so U_e=I up to phases/permutations.  Then test the minimal
   neutrino-side misalignment

       U = U_v9 R_13(theta, phase),

   where U_v9 has the frozen v9 angles
   sin^2(theta12)=1/3-phi0/2, sin^2(theta23)=1/2, theta13=0.
   Right R_13 is the unique elementary mass-eigenline rotation that creates
   U_e3 while preserving the v9 second eigenline.  It is not asserted to be a
   corpus derivation.

ANALYTIC TWO-PARAMETER SOLVE (no optimizer)
-------------------------------------------
With s0^2=1/3-phi0/2, c0^2=1-s0^2, x13=sin^2(theta13),
x23=sin^2(theta23), s=sin(theta), c=cos(theta),

    s^2 = x13/c0^2,
    cos(phase) =
      [c^2+s0^2 s^2-2 x23(1-x13)] / [2 c s0 s].

NuFIT 6.0 x13 and x23 determine (theta,phase).  The unused third datum,
x12=0.307+/-0.012, is the overdetermination check because

    sin^2(theta12)_pred = s0^2/(1-x13).

All three angles within their frozen one-sigma intervals means
MISALIGNMENT_CONSISTENT; otherwise MISALIGNMENT_OVERDETERMINED_KILL.

ONE PRE-DECLARED LADDER CHECK (LEE-honest)
------------------------------------------
After solving, and only once:
* compare sin(theta) with the already-frozen 255-member scalar grammar from
  nu_ratio_grammar_probe.py in the one-sigma interval induced by x13;
* compare phase with the six mu6 phases in the one-sigma rectangle induced by
  x13 and x23.
The inherited significance rule is E_chance<0.1.  No new atom, fitted window,
second grammar, or rescue branch is allowed.

CIRCULARITY FIREWALL
--------------------
theta and phase are DATA-CONSTRAINED missing-object targets, not predictions.
x13 and x23 are used in the solve; x12 is held out.  The TFPT reactor value
sqrt(phi0 exp(-5/6)) and phase 4pi/3 are compared only after the solve.  A
ladder proximity cannot promote the result unless the inherited LEE rule
passes.  No v3 freeze is permitted for a data-constrained or LEE-null result.
"""

from __future__ import annotations

import hashlib
import math
import os
import sys
from dataclasses import dataclass

import mpmath as mp
import numpy as np
import sympy as sp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
VERIFICATION = os.path.join(REPO, "verification")
sys.path.insert(0, VERIFICATION)
sys.path.insert(0, HERE)

from tfpt_constants import phi0  # noqa: E402
from nu_ratio_grammar_probe import (  # noqa: E402
    DM2_21_EV2,
    M2_GEV,
    M3_GEV,
    V_EW_GEV,
    build_candidates,
    light_mass_ev,
    run_sm_up,
    yukawa_from_mass,
)


mp.mp.dps = 60

PHI0 = mp.mpf(phi0)
S12_V9 = mp.mpf(1) / 3 - PHI0 / 2
S23_V9 = mp.mpf("0.5")

# Frozen NuFIT 6.0 snapshot already used by nu_texture_census_probe.py.
NUFIT = {
    "sin2_theta12": (mp.mpf("0.307"), mp.mpf("0.012")),
    "sin2_theta13": (mp.mpf("0.02195"), mp.mpf("0.00058")),
    "sin2_theta23": (mp.mpf("0.470"), mp.mpf("0.017")),
}
TFPT_SIN2_THETA13 = PHI0 * mp.exp(-mp.mpf(5) / 6)
TFPT_SIN_THETA13 = mp.sqrt(TFPT_SIN2_THETA13)
TFPT_PHASE = 4 * mp.pi / 3
LEE_MAX = mp.mpf("0.1")

V3_PATH = os.path.join(
    REPO,
    "experiments",
    "nu-scalaron-falsification",
    "hypotheses",
    "nu_scalaron_v3.yaml",
)

SOURCES = {
    "v4": os.path.join(VERIFICATION, "v4_flavor_matrix.py"),
    "v9": os.path.join(VERIFICATION, "v9_neutrino_texture.py"),
    "v10": os.path.join(VERIFICATION, "v10_projection_involution.py"),
    "v17": os.path.join(VERIFICATION, "v17_hexagonal_resolvent.py"),
    "v18": os.path.join(VERIFICATION, "v18_quark_yukawa.py"),
    "v20": os.path.join(VERIFICATION, "v20_lepton_c_derivation.py"),
    "v118": os.path.join(VERIFICATION, "v118_hexagon_family_dictionary.py"),
    "v120": os.path.join(VERIFICATION, "v120_address_table.py"),
    "v121": os.path.join(VERIFICATION, "v121_address_pinning.py"),
    "v163": os.path.join(VERIFICATION, "v163_rg_stability_flavor.py"),
    "v229": os.path.join(VERIFICATION, "v229_lepton_frobenius_algebra.py"),
    "v263": os.path.join(VERIFICATION, "v263_mnu_from_df.py"),
    "v270": os.path.join(VERIFICATION, "v270_pmns_jarlskog_assembly.py"),
    "v530": os.path.join(VERIFICATION, "v530_center_quotient_compiler.py"),
    "tfpt2": os.path.join(REPO, "tfpt_2_standard_model.tex"),
}


@dataclass(frozen=True)
class InventoryEntry:
    object_name: str
    matrix_status: str
    basis: str
    mass_operator_verdict: str


@dataclass(frozen=True)
class MisalignmentSolution:
    theta: mp.mpf
    phase_positive: mp.mpf
    phase_negative_cp: mp.mpf
    predicted_sin2_theta12: mp.mpf


def read_sources() -> dict[str, str]:
    payloads: dict[str, str] = {}
    for name, path in SOURCES.items():
        with open(path, encoding="utf-8") as handle:
            payloads[name] = handle.read()
    return payloads


def build_inventory() -> list[InventoryEntry]:
    return [
        InventoryEntry(
            "v20/v18 coefficients and master formula",
            "three scalar masses/eigenvalues",
            "named (e,mu,tau) mass order",
            "diagonal-by-label; no off-diagonal Y_e",
        ),
        InventoryEntry(
            "v229 A=Q[t]/(m), multiplication by t",
            "implicit non-diagonal 3x3 companion",
            "polynomial basis (1,t,t^2), not flavor",
            "coefficient algebra, not a physical mass matrix",
        ),
        InventoryEntry(
            "v17/v229 C6 shift and resolvent",
            "explicit 6x6 cyclic transport matrix",
            "six hexagon sites = family x sheet",
            "transport kernel, not charged-lepton mass",
        ),
        InventoryEntry(
            "v118 M0 family monodromy",
            "explicit complex 3x3 matrix",
            "wall-monodromy family basis",
            "determinants yield c_l; leg assignment remains input",
        ),
        InventoryEntry(
            "v4/v10/v120/v121 R,Q,K,L",
            "explicit 3x3 integer tables",
            "rows=(up,down,lepton), cols=generation",
            "lepton rows are addresses, not operators on e/mu/tau",
        ),
        InventoryEntry(
            "v530 C and quotient A",
            "explicit 3x3/2x2 integer operators",
            "compiler center / quotient lattice",
            "atom compiler, not charged-lepton mass",
        ),
        InventoryEntry(
            "v9 texture",
            "explicit non-diagonal 3x3",
            "(nu_e,nu_mu,nu_tau) light-neutrino flavor",
            "Majorana M_nu, not charged-lepton M_e",
        ),
        InventoryEntry(
            "v263 D_F seesaw examples",
            "3x3 m_D, M_R, M_nu examples",
            "neutrino generation space",
            "existence examples; no frozen charged-lepton Y_e",
        ),
        InventoryEntry(
            "tfpt_2 seam R12(epsilon)",
            "rotation asserted, no parent mass matrix",
            "charged-lepton rows relative to v9/TBM",
            "conditional input, not diagonalization of M_e",
        ),
        InventoryEntry(
            "v270 U_PMNS",
            "explicit assembled complex 3x3",
            "PDG mixing convention",
            "assembled observable, not U_e derived from M_e",
        ),
    ]


def coefficient_algebra_certificate() -> tuple[sp.Matrix, sp.Matrix, sp.Expr]:
    """Return multiplication-by-t, trace Gram, and G-self-adjoint residual."""
    ce = sp.Rational(16, 7)
    cmu = sp.Rational(4, 3)
    ctau = sp.Rational(7, 6)
    t = sp.symbols("t")
    polynomial = sp.Poly((t - ce) * (t - cmu) * (t - ctau), t)
    _, a2, a1, a0 = polynomial.all_coeffs()
    multiplication_t = sp.Matrix(
        [
            [0, 0, -a0],
            [1, 0, -a1],
            [0, 1, -a2],
        ]
    )
    roots = (ce, cmu, ctau)
    powers = [sum(root**power for root in roots) for power in range(5)]
    gram = sp.Matrix([[powers[i + j] for j in range(3)] for i in range(3)])
    residual = sp.simplify(multiplication_t.T * gram - gram * multiplication_t)
    return multiplication_t, gram, residual


def rotation13(theta: mp.mpf, phase: mp.mpf) -> mp.matrix:
    c = mp.cos(theta)
    s = mp.sin(theta)
    return mp.matrix(
        [
            [c, 0, s * mp.exp(-1j * phase)],
            [0, 1, 0],
            [-s * mp.exp(1j * phase), 0, c],
        ]
    )


def v9_mixing_matrix() -> mp.matrix:
    s12 = mp.sqrt(S12_V9)
    c12 = mp.sqrt(1 - S12_V9)
    root2 = mp.sqrt(2)
    return mp.matrix(
        [
            [c12, s12, 0],
            [-s12 / root2, c12 / root2, 1 / root2],
            [s12 / root2, -c12 / root2, 1 / root2],
        ]
    )


def pmns_angles(unitary: mp.matrix) -> dict[str, mp.mpf]:
    s13sq = abs(unitary[0, 2]) ** 2
    denominator = 1 - s13sq
    return {
        "sin2_theta12": abs(unitary[0, 1]) ** 2 / denominator,
        "sin2_theta13": s13sq,
        "sin2_theta23": abs(unitary[1, 2]) ** 2 / denominator,
    }


def physical_delta(unitary: mp.matrix) -> mp.mpf:
    angles = pmns_angles(unitary)
    s12sq = angles["sin2_theta12"]
    s13sq = angles["sin2_theta13"]
    s23sq = angles["sin2_theta23"]
    s12, c12 = mp.sqrt(s12sq), mp.sqrt(1 - s12sq)
    s13, c13 = mp.sqrt(s13sq), mp.sqrt(1 - s13sq)
    s23, c23 = mp.sqrt(s23sq), mp.sqrt(1 - s23sq)
    jcp = mp.im(
        unitary[0, 0]
        * unitary[1, 1]
        * mp.conj(unitary[0, 1])
        * mp.conj(unitary[1, 0])
    )
    sin_delta = jcp / (s12 * c12 * s23 * c23 * s13 * c13**2)
    mu1sq = abs(unitary[1, 0]) ** 2
    cos_delta = (
        mu1sq
        - s12sq * c23**2
        - c12**2 * s23sq * s13sq
    ) / (2 * s12 * c12 * s23 * c23 * s13)
    delta = mp.atan2(sin_delta, cos_delta)
    return delta if delta >= 0 else delta + 2 * mp.pi


def solve_misalignment(x13: mp.mpf, x23: mp.mpf) -> MisalignmentSolution:
    c0sq = 1 - S12_V9
    sin_theta = mp.sqrt(x13 / c0sq)
    theta = mp.asin(sin_theta)
    cos_theta = mp.cos(theta)
    cos_phase = (
        cos_theta**2
        + S12_V9 * sin_theta**2
        - 2 * x23 * (1 - x13)
    ) / (2 * cos_theta * mp.sqrt(S12_V9) * sin_theta)
    if abs(cos_phase) > 1:
        raise ValueError("no real phase solves theta23")
    phase_positive = mp.acos(cos_phase)
    phase_negative_cp = 2 * mp.pi - phase_positive
    predicted_s12 = S12_V9 / (1 - x13)
    return MisalignmentSolution(
        theta,
        phase_positive,
        phase_negative_cp,
        predicted_s12,
    )


def phase_windows() -> tuple[tuple[mp.mpf, mp.mpf], tuple[mp.mpf, mp.mpf]]:
    """Conservative one-sigma rectangle propagated through the analytic solve."""
    x13, sigma13 = NUFIT["sin2_theta13"]
    x23, sigma23 = NUFIT["sin2_theta23"]
    positives: list[mp.mpf] = []
    negatives: list[mp.mpf] = []
    for reactor in (x13 - sigma13, x13 + sigma13):
        for atmospheric in (x23 - sigma23, x23 + sigma23):
            solution = solve_misalignment(reactor, atmospheric)
            positives.append(solution.phase_positive)
            negatives.append(solution.phase_negative_cp)
    return (
        (min(positives), max(positives)),
        (min(negatives), max(negatives)),
    )


def degrees(value: mp.mpf) -> mp.mpf:
    return value * 180 / mp.pi


def fmt(value: mp.mpf, digits: int = 16) -> str:
    return mp.nstr(value, digits)


def main() -> int:
    checks: list[tuple[str, bool]] = []
    sources = read_sources()
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()[:16]

    # Source-level inventory guards: these prevent the prose classification
    # from silently surviving a changed corpus.
    checks.extend(
        [
            (
                "v20 freezes scalar coefficients, residues, and windings",
                "c_e = mu4**w['e'] * amp2" in sources["v20"]
                and "c_tau = prod / (c_e * c_mu)" in sources["v20"],
            ),
            (
                "v229 defines coefficient algebra in polynomial basis",
                "A = Q[t]/(m)" in sources["v229"]
                and "G = sp.Matrix" in sources["v229"],
            ),
            (
                "v118 explicitly leaves e/mu/tau leg assignment as input",
                "LEG assignment" in sources["v118"]
                and "remains v20's" in sources["v118"],
            ),
            (
                "v121 basis is rows sectors and columns generations",
                "rows (up; down; lepton)" in sources["v121"]
                and "L = sp.Matrix([[7, 3, 0], [7, 5, 2], [8, 5, 3]])"
                in sources["v121"],
            ),
            (
                "master formula is elementwise in labels f,j",
                r"\hat m_{f,j}=\frac{\vgeo}{\sqrt2}\,y_{f,j}" in sources["tfpt2"]
                and r"(\hat m_e,\hat m_\mu,\hat m_\tau)=" in sources["tfpt2"],
            ),
            (
                "tfpt_2 labels charged-lepton misalignment conditional",
                "structural\ninput ``$1$--$2$ charged-lepton misalignment" in sources["tfpt2"],
            ),
            (
                "v9 is explicitly a neutrino Majorana texture",
                "neutrino Majorana texture" in sources["v9"],
            ),
            (
                "v263 says full PMNS dynamics remain open",
                "full PMNS dynamics" in sources["v263"],
            ),
        ]
    )

    # Exact matrix classifications.
    R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
    Q = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
    K = sp.Matrix([[4, 2, 0], [4, 3, 2], [5, 3, 2]])
    L = sp.Matrix([[7, 3, 0], [7, 5, 2], [8, 5, 3]])
    checks.append(
        (
            "address rows are R=(2,5,3), Q=(3,2,1), K=(5,3,2), L=(8,5,3)",
            tuple(R.row(2)) == (2, 5, 3)
            and tuple(Q.row(2)) == (3, 2, 1)
            and tuple(K.row(2)) == (5, 3, 2)
            and tuple(L.row(2)) == (8, 5, 3),
        )
    )

    multiplication_t, gram, frobenius_residual = coefficient_algebra_certificate()
    coefficients = [sp.Rational(16, 7), sp.Rational(4, 3), sp.Rational(7, 6)]
    checks.extend(
        [
            (
                "v229 implicit multiplication-by-t has the coefficient spectrum",
                sorted(multiplication_t.eigenvals().keys()) == sorted(coefficients),
            ),
            (
                "multiplication-by-t is non-diagonal in (1,t,t^2)",
                multiplication_t != sp.diag(*coefficients),
            ),
            (
                "multiplication-by-t is self-adjoint only in trace Gram metric",
                frobenius_residual == sp.zeros(3)
                and gram != sp.eye(3)
                and multiplication_t != multiplication_t.T,
            ),
        ]
    )

    source_mass_operator = sp.diag(
        sp.Rational(16, 7) * sp.Symbol("phi0") ** 5,
        sp.Rational(4, 3) * sp.Symbol("phi0") ** 3,
        sp.Rational(7, 6) * sp.Symbol("phi0") ** 2,
    )
    ue = sp.eye(3)
    checks.append(
        (
            "frozen charged-lepton source mass operator is diagonal by named labels",
            source_mass_operator.is_diagonal() and ue == sp.eye(3),
        )
    )

    print("SPEC_SHA", spec_sha)
    print("EXPLORATION ONLY; corpus files are read-only")
    print()
    print("INVENTORY")
    print("object | matrix or not | basis | charged-lepton mass verdict")
    for entry in build_inventory():
        print(
            "{} | {} | {} | {}".format(
                entry.object_name,
                entry.matrix_status,
                entry.basis,
                entry.mass_operator_verdict,
            )
        )
    print("v229 multiplication-by-t =", multiplication_t.tolist())
    print("v229 trace Gram det =", sp.factor(gram.det()))
    print()

    nufit_s13 = mp.sqrt(NUFIT["sin2_theta13"][0])
    print("U_e RESULT")
    print("  corpus non-diagonal charged-lepton mass matrix: NONE")
    print("  frozen source-basis U_e = I (up to unphysical phases/permutation)")
    print(
        "  |(U_e)13|=0 vs NuFIT sqrt(0.02195)={} and TFPT "
        "sqrt(phi0 exp(-5/6))={}".format(
            fmt(nufit_s13),
            fmt(TFPT_SIN_THETA13),
        )
    )
    print(
        "  named missing object: Q_+-eigenbasis to charged-lepton flavor-basis "
        "misalignment operator"
    )
    print()

    # Analytic two-parameter solve: x13 and x23 fitted, x12 held out.
    x13, sigma13 = NUFIT["sin2_theta13"]
    x23, sigma23 = NUFIT["sin2_theta23"]
    x12, sigma12 = NUFIT["sin2_theta12"]
    solution = solve_misalignment(x13, x23)
    u0 = v9_mixing_matrix()
    rotation = rotation13(solution.theta, solution.phase_negative_cp)
    unitary = u0 * rotation
    angles = pmns_angles(unitary)
    delta = physical_delta(unitary)
    unitarity_residual = mp.norm(unitary.transpose_conj() * unitary - mp.eye(3))

    deviations = {
        name: angles[name] - NUFIT[name][0]
        for name in ("sin2_theta12", "sin2_theta13", "sin2_theta23")
    }
    pulls = {
        name: deviations[name] / NUFIT[name][1]
        for name in deviations
    }
    angle_consistent = all(abs(pull) <= 1 for pull in pulls.values())
    checks.extend(
        [
            ("analytic solve gives a real rotation", 0 < solution.theta < mp.pi / 2),
            ("negative-CP branch gives a real phase", mp.pi < solution.phase_negative_cp < 2 * mp.pi),
            ("constructed U is unitary", unitarity_residual < mp.mpf("1e-50")),
            ("theta13 central value is reproduced", abs(deviations["sin2_theta13"]) < mp.mpf("1e-50")),
            ("theta23 central value is reproduced", abs(deviations["sin2_theta23"]) < mp.mpf("1e-50")),
            ("held-out theta12 is inside one sigma", abs(pulls["sin2_theta12"]) <= 1),
        ]
    )

    print("MINIMAL NEUTRINO-SIDE MISALIGNMENT")
    print("  convention U = U_v9 R13(theta,phase); negative-CP branch")
    print(
        "  theta={} rad = {} deg; sin(theta)={}".format(
            fmt(solution.theta),
            fmt(degrees(solution.theta), 14),
            fmt(mp.sin(solution.theta)),
        )
    )
    print(
        "  phase={} rad = {} deg; conjugate branch={} deg".format(
            fmt(solution.phase_negative_cp),
            fmt(degrees(solution.phase_negative_cp), 14),
            fmt(degrees(solution.phase_positive), 14),
        )
    )
    print(
        "  physical PDG delta={} deg; J_CP={}".format(
            fmt(degrees(delta), 14),
            fmt(
                mp.im(
                    unitary[0, 0]
                    * unitary[1, 1]
                    * mp.conj(unitary[0, 1])
                    * mp.conj(unitary[1, 0])
                ),
                14,
            ),
        )
    )
    print("  angle deviations (prediction - NuFIT central)")
    for name in ("sin2_theta12", "sin2_theta13", "sin2_theta23"):
        prediction = angles[name]
        target, uncertainty = NUFIT[name]
        predicted_deg = degrees(mp.asin(mp.sqrt(prediction)))
        target_deg = degrees(mp.asin(mp.sqrt(target)))
        print(
            "    {}: pred={} target={} delta={} pull={:+.9f} sigma; "
            "angle delta={:+.9f} deg".format(
                name,
                fmt(prediction),
                fmt(target),
                fmt(deviations[name], 12),
                float(pulls[name]),
                float(predicted_deg - target_deg),
            )
        )
    print()

    # Full factorized seesaw check with the frozen heavy masses and v481 runner.
    y3, rundown3 = run_sm_up(M3_GEV)
    _yt2, rundown2 = run_sm_up(M2_GEV)
    m2_ev = mp.sqrt(DM2_21_EV2)
    y2 = yukawa_from_mass(m2_ev, M2_GEV, rundown2)
    m3_ev = light_mass_ev(y3, M3_GEV, rundown3)

    u_np = np.array(
        [[complex(unitary[i, j]) for j in range(3)] for i in range(3)],
        dtype=complex,
    )
    yukawa = np.diag([0.0, float(y2), float(y3)]) @ u_np.conj().T
    threshold_weights = np.diag(
        [
            0.0,
            float(rundown2 / M2_GEV),
            float(rundown3 / M3_GEV),
        ]
    )
    mnu_ev = (
        -float(V_EW_GEV**2 / 2)
        * (yukawa.T @ threshold_weights @ yukawa)
        * 1e9
    )
    expected_mnu_ev = (
        -u_np.conj()
        @ np.diag([0.0, float(m2_ev), float(m3_ev)])
        @ u_np.conj().T
    )
    seesaw_residual = np.linalg.norm(mnu_ev - expected_mnu_ev)
    symmetry_residual = np.linalg.norm(mnu_ev - mnu_ev.T)
    checks.extend(
        [
            ("factorized seesaw reconstructs U* diag(m) U^dagger", seesaw_residual < 1e-14),
            ("complex light Majorana matrix is symmetric", symmetry_residual < 1e-14),
            ("frozen singular hierarchy keeps y1=0<y2<y3", 0 < float(y2) < float(y3)),
        ]
    )

    print("FULL SEESAW CROSS-CHECK")
    print(
        "  M_R=diag(epsilon M_scal,2epsilon M_scal,3M_scal); "
        "Y=diag(0,y2,y3) U^dagger"
    )
    print(
        "  y2/y3={} ; masses=(0,{}, {}) eV; sum={} eV".format(
            fmt(y2 / y3),
            fmt(m2_ev),
            fmt(m3_ev),
            fmt(m2_ev + m3_ev),
        )
    )
    print(
        "  ||Mnu-seesaw - [-U*diag(m)U^dagger]||={} ; symmetry={}".format(
            f"{seesaw_residual:.3e}",
            f"{symmetry_residual:.3e}",
        )
    )
    print(
        "  mass ratios set eigenvalues only; because Y factorizes with U^dagger, "
        "they do not create or tune the mixing angles"
    )
    print()

    # One and only one inherited ladder evaluation.
    scalar_candidates = build_candidates()
    c0sq = 1 - S12_V9
    sin_theta_target = mp.sin(solution.theta)
    sin_theta_lower = mp.sqrt((x13 - sigma13) / c0sq)
    sin_theta_upper = mp.sqrt((x13 + sigma13) / c0sq)
    scalar_hits = [
        candidate
        for candidate in scalar_candidates
        if sin_theta_lower <= candidate.value <= sin_theta_upper
    ]
    scalar_lee = (
        len(scalar_candidates)
        * (sin_theta_upper - sin_theta_lower)
        / sin_theta_target
    )

    positive_window, negative_window = phase_windows()
    mu6_phases = [mp.pi * k / 3 for k in range(6)]
    phase_hits = [
        phase
        for phase in mu6_phases
        if positive_window[0] <= phase <= positive_window[1]
        or negative_window[0] <= phase <= negative_window[1]
    ]
    total_phase_width = (
        positive_window[1]
        - positive_window[0]
        + negative_window[1]
        - negative_window[0]
    )
    phase_lee = len(mu6_phases) * total_phase_width / (2 * mp.pi)
    checks.extend(
        [
            ("inherited scalar grammar has exactly 255 candidates", len(scalar_candidates) == 255),
            ("one-shot scalar ladder has no one-sigma hit", len(scalar_hits) == 0),
            ("scalar LEE expectation is not significant", scalar_lee >= LEE_MAX),
            ("one-shot mu6 phase ladder has no one-sigma hit", len(phase_hits) == 0),
            ("phase LEE expectation is not significant", phase_lee >= LEE_MAX),
        ]
    )

    frozen_phase_atmospheric = pmns_angles(
        u0 * rotation13(solution.theta, TFPT_PHASE)
    )["sin2_theta23"]
    frozen_phase_pull = (
        frozen_phase_atmospheric - x23
    ) / sigma23
    print("ONE-SHOT FROZEN-LADDER CHECK")
    print(
        "  scalar: sin(theta)={} window=[{},{}], hits={}, "
        "E_chance={} (255 tests; not significant)".format(
            fmt(sin_theta_target),
            fmt(sin_theta_lower),
            fmt(sin_theta_upper),
            len(scalar_hits),
            fmt(scalar_lee, 12),
        )
    )
    print(
        "  phase: solved negative-CP={} deg; one-sigma windows "
        "[{},{}] and [{},{}] deg; mu6 hits={}; E_chance={}".format(
            fmt(degrees(solution.phase_negative_cp), 12),
            fmt(degrees(positive_window[0]), 10),
            fmt(degrees(positive_window[1]), 10),
            fmt(degrees(negative_window[0]), 10),
            fmt(degrees(negative_window[1]), 10),
            len(phase_hits),
            fmt(phase_lee, 12),
        )
    )
    print(
        "  TFPT reactor comparator: {} vs NuFIT {} (rel={:+.9f}%, "
        "sin^2 pull={:+.9f} sigma)".format(
            fmt(TFPT_SIN_THETA13),
            fmt(nufit_s13),
            float(100 * (TFPT_SIN_THETA13 / nufit_s13 - 1)),
            float((TFPT_SIN2_THETA13 - x13) / sigma13),
        )
    )
    print(
        "  frozen phase 4pi/3=240 deg would give sin^2(theta23)={} "
        "({:+.9f} sigma vs NuFIT), so it is not the solved phase".format(
            fmt(frozen_phase_atmospheric),
            float(frozen_phase_pull),
        )
    )
    print()

    print("CIRCULARITY ANALYSIS")
    print("  FIT inputs: NuFIT sin2(theta13), sin2(theta23).")
    print("  HELD OUT: NuFIT sin2(theta12); prediction is +0.552631 sigma.")
    print(
        "  POST-SOLVE ONLY: TFPT sqrt(phi0 exp(-5/6)), 4pi/3, "
        "255-member scalar grammar, and six mu6 phases."
    )
    print(
        "  Therefore the rotation is a data-constrained specification of the "
        "missing operator, not a TFPT derivation or confirmation."
    )
    print()

    if angle_consistent:
        verdict = (
            "UE_CORPUS_DIAGONAL+MISALIGNMENT_CONSISTENT"
            "(theta={}deg,phase={}deg)".format(
                fmt(degrees(solution.theta), 12),
                fmt(degrees(solution.phase_negative_cp), 12),
            )
        )
    else:
        verdict = "UE_CORPUS_DIAGONAL+MISALIGNMENT_OVERDETERMINED_KILL"

    freeze_status = "NOT_CREATED_DATA_CONSTRAINED_AND_LADDER_NULL"
    checks.append(("v3 freeze absent", not os.path.exists(V3_PATH)))
    print("VERDICT", verdict)
    print("V3_FREEZE", freeze_status)
    print(
        "MISSING_MECHANISM a corpus-derived Q_+-eigenbasis to charged-lepton "
        "flavor-basis operator; current two-parameter R13 target is not frozen."
    )
    print()

    for label, passed in checks:
        print(("PASS " if passed else "FAIL ") + label)
    all_pass = all(passed for _label, passed in checks)
    print("ALL PASS" if all_pass else "PROTOCOL FAILURE")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
