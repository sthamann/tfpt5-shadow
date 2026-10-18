#!/usr/bin/env python3
"""nu_texture_census_probe -- SIMPLEST-FIRST, EXPLORATION ONLY.

Question
--------
Does any already-frozen corpus 3x3 object, interpreted as a Dirac texture
Y_nu and given only the single frozen normalization

    sigma_max(Y_nu) = y_t(M3) = 0.44197399765711176,

reproduce low-energy neutrino data through

    M_R = M_scal diag(epsilon, 2 epsilon, 3),
    epsilon = phi0^2 / A_Lambda,
    M_nu(match) = -(v_EW^2/2) Y_nu^T M_R^-1 Y_nu?

This is an exploratory census, not a derivation of Y_nu.  The global
singular-value normalization is the unique basis-independent reading of
"up to y3"; there is no continuous fit and no per-entry rescaling.

FULL CANDIDATE GRAMMAR -- DECLARED BEFORE EVALUATION
----------------------------------------------------
Named frozen matrices:

  R = [[1,3,0],[1,5,2],[2,5,3]]                 (v85/v121)
  Q = [[3,1,0],[3,2,0],[3,2,1]]                 (v85)
  K = [[4,2,0],[4,3,2],[5,3,2]]                 (v85)
  L = K+Q = [[7,3,0],[7,5,2],[8,5,3]]           (v85/v121)
  F = R+Q = [[4,4,0],[4,7,2],[5,7,4]]           (v94/v183)
  Q+ = [[3,0,0],[0,2,0],[0,2,1]]                (v50)
  D263 = diag(3/10,1,1)                          (v263; EXAMPLE)
  T9 = [[-eta,1,1],[1,1,0],[1,0,1]], with eta
       fixed by epsilon9=3 phi0/4                 (v9 light-Majorana
                                                   texture; REUSED AS
                                                   AN EXAMPLE Y only)
  P1,P2,P3 = the exact Q+ Lagrange projectors     (v50 polynomial)

For each named matrix A include A, A^T, and (A+A^T)/2, with exact
duplicates removed.

Small independent-projector grammar:

  sum_i c_i P_i, c_i in
  Csmall={0,1,phi0,phi0^2,phi0^3,53/54,5/3,2/3}, not all zero.

Frozen-ladder tail (to include phi0^n through n=6 without opening the
independent grammar):

  r phi0^n sum_{i in S} P_i,
  n in {4,5,6}, r in {1,53/54,5/3,2/3},
  empty != S subset {1,2,3}.

Again include raw, transpose, and Hermitian (= symmetric here) parts,
then remove exact duplicates.  No entries, signs, rotations, phases, or
continuous coefficients exist outside this grammar.

DATA METRIC -- DECLARED BEFORE EVALUATION
-----------------------------------------
NuFIT 6.0 frozen snapshot:
  dm21 = (7.49 +/- 0.19)e-5 eV^2
  dm31 = (2.513 +/- 0.021)e-3 eV^2
  s12 = 0.307 +/- 0.012
  s13 = 0.02195 +/- 0.00058
  s23 = 0.470 +/- 0.017
and DESI DR2 LCDM Sigma < 0.0642 eV.

The splitting comparator is r=dm21/dm31 with independent Gaussian error
propagation.  HIT means all four NuFIT pulls are <=3 and Sigma is below
the bound.  Define miss_factor=max(pull_i/3, Sigma/0.0642); a non-hit
with miss_factor<=10 is a NEAR_MISS ("within 10x").  TFPT v270 angle
pulls are reported with the same NuFIT sigmas but do not replace the
experimental hit gate.

LOW-ENERGY CONVENTION
---------------------
The exact matching matrix above is retained.  For comparison with
low-energy data, mirror v2's already-frozen per-heavy-line ADKLR factors:

  M_nu(low) = -(v_EW^2/2) Y^T diag(R1/M1,R2/M2,R3/M3) Y.

This is not an RG re-derivation or fit of Y.  It is the v2 frozen
low-energy map (R1,R2,R3) applied linearly to the three threshold
contributions.  The charged-lepton basis is assumed to coincide with
the published generation/address basis and the v69 ordering of M_R.

NULL
----
Exactly 200 seeded integer 3x3 matrices, entries uniform over the full
integer entry range of the raw frozen inventory [-2,8], receive the
same normalization and score.  This control is exploratory: the corpus
candidates are correlated by construction.

HONEST BOUNDARY
---------------
Tree-level type-I seesaw plus the inherited v2 low-energy factors;
normal ordering; fixed charged-lepton-basis identification; no
continuous fitting; no RG re-derivation of Y; no claim that v9 or v263
is a frozen Dirac Yukawa; no closure of FLAV.NUSCALE.05.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import sys
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Iterable

import mpmath as mp
import numpy as np
import sympy as sp


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
NU_ROOT = os.path.join(REPO, "experiments", "nu-scalaron-falsification")
RESULT_PATH = os.path.join(NU_ROOT, "results", "texture_census.json")
V3_PATH = os.path.join(NU_ROOT, "hypotheses", "nu_scalaron_v3.yaml")
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import Mbar as MBAR_CORPUS  # noqa: E402


mp.mp.dps = 60

# Frozen constants.  y_t and R_i are copied from the already-executed v2
# result, not rerun or adjusted in this census.
V_EW_GEV = mp.mpf("246.22")
Y3_FROZEN = mp.mpf("0.44197399765711176")
M_BAR_GEV = mp.mpf(str(MBAR_CORPUS))
A_LAMBDA = mp.mpf("10")
R_DOWN = (
    mp.mpf("0.8167477841848322"),
    mp.mpf("0.814380979370167"),
    mp.mpf("0.7944014076884586"),
)

C3 = mp.mpf(1) / (8 * mp.pi)
PHI0 = mp.mpf(4) * C3 / 3 + 48 * C3**4
M_SCAL_GEV = C3 ** mp.mpf("3.5") * M_BAR_GEV
EPSILON = PHI0**2 / A_LAMBDA
M_HEAVY_GEV = (
    EPSILON * M_SCAL_GEV,
    2 * EPSILON * M_SCAL_GEV,
    3 * M_SCAL_GEV,
)

# NuFIT 6.0 / DESI comparators, all predeclared.
DM21 = mp.mpf("7.49e-5")
DM21_SIGMA = mp.mpf("0.19e-5")
DM31 = mp.mpf("2.513e-3")
DM31_SIGMA = mp.mpf("0.021e-3")
RATIO_TARGET = DM21 / DM31
RATIO_SIGMA = RATIO_TARGET * mp.sqrt(
    (DM21_SIGMA / DM21) ** 2 + (DM31_SIGMA / DM31) ** 2
)
ANGLE_DATA = {
    "sin2_theta12": (mp.mpf("0.307"), mp.mpf("0.012")),
    "sin2_theta13": (mp.mpf("0.02195"), mp.mpf("0.00058")),
    "sin2_theta23": (mp.mpf("0.470"), mp.mpf("0.017")),
}
TFPT_ANGLES = {
    "sin2_theta12": mp.mpf(1) / 3 - PHI0 / 2,
    "sin2_theta13": PHI0 * mp.exp(-mp.mpf(5) / 6),
    "sin2_theta23": mp.mpf("0.5"),
}
SIGMA_BOUND_EV = mp.mpf("0.0642")
NULL_SEED = 20260828
N_NULL = 200
NULL_ENTRY_MIN = -2
NULL_ENTRY_MAX = 8


@dataclass
class Candidate:
    name: str
    matrix: sp.Matrix
    provenance: str
    aliases: list[str] = field(default_factory=list)


def _sympy_phi0() -> sp.Expr:
    c3 = sp.Rational(1, 8) / sp.pi
    return sp.Rational(4, 3) * c3 + 48 * c3**4


PHI0_S = _sympy_phi0()
I3 = sp.eye(3)
R_MAT = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
Q_MAT = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
K_MAT = sp.Matrix([[4, 2, 0], [4, 3, 2], [5, 3, 2]])
L_MAT = K_MAT + Q_MAT
F_MAT = R_MAT + Q_MAT
SIGMA = sp.diag(1, -1, -1)
Q_PLUS = sp.simplify((Q_MAT + SIGMA * Q_MAT * SIGMA) / 2)
P1 = sp.simplify((Q_PLUS - 2 * I3) * (Q_PLUS - 3 * I3) / 2)
P2 = sp.simplify(-(Q_PLUS - I3) * (Q_PLUS - 3 * I3))
P3 = sp.simplify((Q_PLUS - I3) * (Q_PLUS - 2 * I3) / 2)
D263 = sp.diag(sp.Rational(3, 10), 1, 1)
EPS9 = 3 * PHI0_S / 4
S12_9 = sp.Rational(1, 3) * (1 - 2 * EPS9)
COS2_9 = 1 - 2 * S12_9
TAN2_9 = sp.sqrt(1 - COS2_9**2) / COS2_9
ETA9 = sp.simplify(2 * sp.sqrt(2) / TAN2_9 - 1)
T9 = sp.Matrix([[-ETA9, 1, 1], [1, 1, 0], [1, 0, 1]])

NAMED_PRIMITIVES = (
    ("R", R_MAT, "v85/v121 frozen residue/address matrix"),
    ("Q", Q_MAT, "v85 frozen address operator"),
    ("K", K_MAT, "v85 frozen sheet-diamond corner"),
    ("L", L_MAT, "v85/v121 frozen word table; L=K+Q"),
    ("F", F_MAT, "v94/v183 frozen missing corner; F=R+Q"),
    ("Qplus", Q_PLUS, "v50 Sigma-even generation matrix"),
    ("D263_example", D263, "v263 existence example, not a frozen Dirac Yukawa"),
    ("T9_reused", T9, "v9 light-Majorana texture reused only as an example Y"),
    ("P1", P1, "v50 Qplus Lagrange projector"),
    ("P2", P2, "v50 Qplus Lagrange projector"),
    ("P3", P3, "v50 Qplus Lagrange projector"),
)

SMALL_COEFFICIENTS = (
    ("0", sp.Integer(0)),
    ("1", sp.Integer(1)),
    ("phi", PHI0_S),
    ("phi2", PHI0_S**2),
    ("phi3", PHI0_S**3),
    ("53/54", sp.Rational(53, 54)),
    ("5/3", sp.Rational(5, 3)),
    ("2/3", sp.Rational(2, 3)),
)
TAIL_RATIONALS = (
    ("1", sp.Integer(1)),
    ("53/54", sp.Rational(53, 54)),
    ("5/3", sp.Rational(5, 3)),
    ("2/3", sp.Rational(2, 3)),
)
PROJECTORS = (P1, P2, P3)


def matrix_key(matrix: sp.Matrix) -> tuple[str, ...]:
    """Stable high-precision key; exact grammar makes accidental collision remote."""
    return tuple(str(sp.N(sp.simplify(x), 50)) for x in matrix)


def add_candidate(
    candidates: dict[tuple[str, ...], Candidate],
    name: str,
    matrix: sp.Matrix,
    provenance: str,
) -> None:
    key = matrix_key(matrix)
    if key in candidates:
        candidates[key].aliases.append(name)
    else:
        candidates[key] = Candidate(name, matrix, provenance)


def add_with_involutions(
    candidates: dict[tuple[str, ...], Candidate],
    name: str,
    matrix: sp.Matrix,
    provenance: str,
) -> None:
    add_candidate(candidates, name, matrix, provenance)
    add_candidate(candidates, name + ".T", matrix.T, provenance + "; transpose")
    add_candidate(
        candidates,
        name + ".H",
        sp.simplify((matrix + matrix.T) / 2),
        provenance + "; Hermitian/symmetric part",
    )


def build_candidates() -> list[Candidate]:
    """Enumerate only the grammar printed in this file's module docstring."""
    unique: dict[tuple[str, ...], Candidate] = {}
    for name, matrix, provenance in NAMED_PRIMITIVES:
        add_with_involutions(unique, name, matrix, provenance)

    for choices in itertools.product(SMALL_COEFFICIENTS, repeat=3):
        if all(label == "0" for label, _value in choices):
            continue
        labels = [choice[0] for choice in choices]
        values = [choice[1] for choice in choices]
        matrix = sp.zeros(3)
        for coefficient, projector in zip(values, PROJECTORS):
            matrix += coefficient * projector
        name = "spec[" + ",".join(labels) + "]"
        add_with_involutions(
            unique,
            name,
            sp.simplify(matrix),
            "small independent Qplus-projector grammar",
        )

    for power in (4, 5, 6):
        for rational_label, rational in TAIL_RATIONALS:
            for mask in range(1, 8):
                subset = [i + 1 for i in range(3) if mask & (1 << i)]
                matrix = sum(
                    (PROJECTORS[i - 1] for i in subset),
                    start=sp.zeros(3),
                )
                matrix = sp.simplify(rational * PHI0_S**power * matrix)
                name = "tail[%s*phi%d;P%s]" % (
                    rational_label,
                    power,
                    "".join(str(i) for i in subset),
                )
                add_with_involutions(
                    unique,
                    name,
                    matrix,
                    "uniform frozen phi0-ladder tail on a projector subset",
                )
    return list(unique.values())


def to_mp_matrix(matrix: sp.Matrix) -> mp.matrix:
    return mp.matrix(
        [
            [mp.mpf(str(sp.N(matrix[i, j], 70))) for j in range(3)]
            for i in range(3)
        ]
    )


def spectral_norm(matrix: mp.matrix) -> mp.mpf:
    values, _vectors = mp.eigsy(matrix.T * matrix)
    return mp.sqrt(max(mp.mpf("0"), max(values)))


def normalize_texture(matrix: mp.matrix) -> tuple[mp.matrix, mp.mpf]:
    norm = spectral_norm(matrix)
    if norm <= mp.mpf("1e-50"):
        raise ValueError("zero texture cannot be normalized")
    return matrix * (Y3_FROZEN / norm), norm


def takagi_real_symmetric(matrix: mp.matrix) -> tuple[list[mp.mpf], mp.matrix]:
    """Takagi data for a real symmetric matrix via its exact eigensystem."""
    eigenvalues, vectors = mp.eigsy(matrix)
    order = sorted(range(3), key=lambda i: abs(eigenvalues[i]))
    masses = [abs(eigenvalues[i]) for i in order]
    takagi = mp.matrix(3, 3)
    for new_column, old_column in enumerate(order):
        phase = 1j if eigenvalues[old_column] < 0 else 1
        for row in range(3):
            takagi[row, new_column] = vectors[row, old_column] * phase
    return masses, takagi


def pmns_observables(
    masses: list[mp.mpf], pmns: mp.matrix
) -> dict[str, mp.mpf | None]:
    denominator = 1 - abs(pmns[0, 2]) ** 2
    if denominator <= mp.mpf("1e-30"):
        return {
            "sin2_theta12": mp.nan,
            "sin2_theta13": abs(pmns[0, 2]) ** 2,
            "sin2_theta23": mp.nan,
            "delta_deg": None,
            "J_CP": mp.nan,
            "m_beta_eV": mp.nan,
            "m_bb_eV": mp.nan,
        }
    s13sq = abs(pmns[0, 2]) ** 2
    s12sq = abs(pmns[0, 1]) ** 2 / denominator
    s23sq = abs(pmns[1, 2]) ** 2 / denominator
    j_cp = mp.im(
        pmns[0, 0]
        * pmns[1, 1]
        * mp.conj(pmns[0, 1])
        * mp.conj(pmns[1, 0])
    )
    s12 = mp.sqrt(max(mp.mpf("0"), s12sq))
    c12 = mp.sqrt(max(mp.mpf("0"), 1 - s12sq))
    s13 = mp.sqrt(max(mp.mpf("0"), s13sq))
    c13 = mp.sqrt(max(mp.mpf("0"), 1 - s13sq))
    s23 = mp.sqrt(max(mp.mpf("0"), s23sq))
    c23 = mp.sqrt(max(mp.mpf("0"), 1 - s23sq))
    phase_denominator = s12 * c12 * s23 * c23 * s13 * c13**2
    delta_deg: mp.mpf | None = None
    if phase_denominator > mp.mpf("1e-20"):
        sin_delta = max(
            mp.mpf("-1"), min(mp.mpf("1"), j_cp / phase_denominator)
        )
        mu1sq = abs(pmns[1, 0]) ** 2
        cos_delta = (
            mu1sq
            - s12sq * c23**2
            - c12**2 * s23sq * s13sq
        ) / (2 * s12 * c12 * s23 * c23 * s13)
        cos_delta = max(mp.mpf("-1"), min(mp.mpf("1"), cos_delta))
        delta = mp.atan2(sin_delta, cos_delta)
        if delta < 0:
            delta += 2 * mp.pi
        delta_deg = 180 * delta / mp.pi
    m_beta = mp.sqrt(sum(abs(pmns[0, i]) ** 2 * masses[i] ** 2 for i in range(3)))
    m_bb = abs(sum(pmns[0, i] ** 2 * masses[i] for i in range(3)))
    return {
        "sin2_theta12": s12sq,
        "sin2_theta13": s13sq,
        "sin2_theta23": s23sq,
        "delta_deg": delta_deg,
        "J_CP": j_cp,
        "m_beta_eV": m_beta,
        "m_bb_eV": m_bb,
    }


def finite(value: mp.mpf) -> bool:
    return bool(mp.isfinite(value))


def evaluate_matrix(name: str, raw_matrix: mp.matrix) -> dict[str, object]:
    texture, raw_norm = normalize_texture(raw_matrix)
    inverse_match = mp.diag([1 / mass for mass in M_HEAVY_GEV])
    inverse_low = mp.diag(
        [factor / mass for factor, mass in zip(R_DOWN, M_HEAVY_GEV)]
    )
    prefactor = -(V_EW_GEV**2) / 2
    mnu_match = prefactor * texture.T * inverse_match * texture
    mnu_low = prefactor * texture.T * inverse_low * texture
    symmetry_residual = mp.norm(mnu_low - mnu_low.T)

    masses_gev, pmns = takagi_real_symmetric(mnu_low)
    masses = [mass * mp.mpf("1e9") for mass in masses_gev]
    observables = pmns_observables(masses, pmns)
    dm21 = masses[1] ** 2 - masses[0] ** 2
    dm31 = masses[2] ** 2 - masses[0] ** 2
    ratio = dm21 / dm31 if dm31 > mp.mpf("1e-40") else mp.inf
    sigma = sum(masses)

    values_for_gate = [
        ratio,
        observables["sin2_theta12"],
        observables["sin2_theta13"],
        observables["sin2_theta23"],
    ]
    valid = all(value is not None and finite(value) for value in values_for_gate)
    pulls: dict[str, mp.mpf] = {}
    if valid:
        pulls["dm2_ratio"] = abs(ratio - RATIO_TARGET) / RATIO_SIGMA
        for key, (target, uncertainty) in ANGLE_DATA.items():
            value = observables[key]
            assert isinstance(value, mp.mpf)
            pulls[key] = abs(value - target) / uncertainty
        miss_factor = max(
            [pull / 3 for pull in pulls.values()] + [sigma / SIGMA_BOUND_EV]
        )
        hit = all(pull <= 3 for pull in pulls.values()) and sigma < SIGMA_BOUND_EV
        near = (not hit) and miss_factor <= 10
    else:
        pulls = {
            "dm2_ratio": mp.inf,
            "sin2_theta12": mp.inf,
            "sin2_theta13": mp.inf,
            "sin2_theta23": mp.inf,
        }
        miss_factor = mp.inf
        hit = False
        near = False

    tfpt_pulls = {}
    for key, target in TFPT_ANGLES.items():
        value = observables[key]
        uncertainty = ANGLE_DATA[key][1]
        tfpt_pulls[key] = (
            abs(value - target) / uncertainty
            if isinstance(value, mp.mpf) and finite(value)
            else mp.inf
        )

    def f(value: mp.mpf | None) -> float | None:
        return None if value is None or not mp.isfinite(value) else float(value)

    return {
        "name": name,
        "hit": hit,
        "near_miss": near,
        "miss_factor": f(miss_factor),
        "raw_spectral_norm": f(raw_norm),
        "normalized_spectral_norm": f(spectral_norm(texture)),
        "masses_eV": [f(mass) for mass in masses],
        "dm2_21_eV2": f(dm21),
        "dm2_31_eV2": f(dm31),
        "dm2_ratio": f(ratio),
        "sigma_mnu_eV": f(sigma),
        "sin2_theta12": f(observables["sin2_theta12"]),
        "sin2_theta13": f(observables["sin2_theta13"]),
        "sin2_theta23": f(observables["sin2_theta23"]),
        "delta_deg": f(observables["delta_deg"]),
        "J_CP": f(observables["J_CP"]),
        "m_beta_eV": f(observables["m_beta_eV"]),
        "m_bb_eV": f(observables["m_bb_eV"]),
        "pulls_nufit": {key: f(value) for key, value in pulls.items()},
        "pulls_tfpt_angles": {key: f(value) for key, value in tfpt_pulls.items()},
        "matching_masses_eV": [
            f(mass * mp.mpf("1e9"))
            for mass in takagi_real_symmetric(mnu_match)[0]
        ],
        "symmetry_residual": f(symmetry_residual),
    }


def matrix_to_json(matrix: sp.Matrix) -> list[list[str]]:
    return [
        [str(sp.N(matrix[i, j], 14)) for j in range(3)]
        for i in range(3)
    ]


def build_null() -> list[tuple[str, mp.matrix]]:
    rng = np.random.default_rng(NULL_SEED)
    controls: list[tuple[str, mp.matrix]] = []
    while len(controls) < N_NULL:
        values = rng.integers(
            NULL_ENTRY_MIN,
            NULL_ENTRY_MAX + 1,
            size=(3, 3),
        )
        if np.any(values):
            controls.append(
                (
                    "null_%03d" % len(controls),
                    mp.matrix([[int(values[i, j]) for j in range(3)] for i in range(3)]),
                )
            )
    return controls


def kappa_f_bdp(k_wash: float) -> float:
    """Verbatim v372/v1 BDP network, evaluated only if a census hit exists."""
    from scipy.integrate import solve_ivp
    from scipy.special import kn

    def n1eq(z: float) -> float:
        return 0.5 * z * z * kn(2, z)

    def rhs(z: float, y: Iterable[float]) -> list[float]:
        n1, nbl = y
        k1, k2 = kn(1, z), kn(2, z)
        decay = k_wash * z * k1 / k2
        washout = 0.25 * k_wash * z**3 * k1
        source = -decay * (n1 - n1eq(z))
        return [source, source - washout * nbl]

    solution = solve_ivp(
        rhs,
        (0.1, 25.0),
        [n1eq(0.1), 0.0],
        method="LSODA",
        rtol=1e-8,
        atol=1e-12,
    )
    return float(abs(solution.y[1, -1]))


def leptogenesis_for_hit(candidate: Candidate, result: dict[str, object]) -> dict[str, object]:
    texture, _norm = normalize_texture(to_mp_matrix(candidate.matrix))
    row1_norm_sq = sum(abs(texture[0, j]) ** 2 for j in range(3))
    washout_ev = (
        V_EW_GEV**2 / 2 * row1_norm_sq / M_HEAVY_GEV[0] * mp.mpf("1e9")
    )
    mstar_ev = mp.mpf("1.08e-3")
    k_wash = washout_ev / mstar_ev
    efficiency = kappa_f_bdp(float(k_wash))
    delta_deg = result["delta_deg"]
    sin_eff = (
        abs(math.sin(math.radians(float(delta_deg))))
        if delta_deg is not None
        else 0.0
    )
    masses = result["masses_eV"]
    assert isinstance(masses, list)
    m3_ev = float(masses[2])
    v174 = 174.0
    epsilon1 = (
        3.0
        / (16.0 * math.pi)
        * float(M_HEAVY_GEV[0])
        * (m3_ev * 1e-9)
        / v174**2
        * sin_eff
    )
    eta_b = 0.96e-2 * epsilon1 * efficiency
    eta_observed = 6.1e-10
    ratio = eta_b / eta_observed
    return {
        "method": "v372-style single-flavor BDP ODE with texture-derived washout",
        "M1_GeV": float(M_HEAVY_GEV[0]),
        "M2_GeV": float(M_HEAVY_GEV[1]),
        "washout_mtilde1_eV": float(washout_ev),
        "K": float(k_wash),
        "kappa_f": efficiency,
        "delta_input_deg": delta_deg,
        "sin_delta_abs": sin_eff,
        "epsilon1_DI": epsilon1,
        "eta_B": eta_b,
        "eta_B_observed": eta_observed,
        "eta_over_observed": ratio,
        "survives_obs_over_3_to_3obs": bool(1 / 3 <= ratio <= 3),
        "honesty": (
            "DI source uses the texture-derived low-energy delta; real census "
            "textures have no CP source. This is a transfer diagnostic, not a "
            "full flavored leptogenesis calculation."
        ),
    }


def yaml_scalar(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value)
    return json.dumps(str(value))


def freeze_v3(
    candidate: Candidate,
    result: dict[str, object],
    leptogenesis: dict[str, object],
) -> str:
    """Freeze a hit only; return SHA-16 of the written hypothesis."""
    texture, _norm = normalize_texture(to_mp_matrix(candidate.matrix))
    matrix_rows = [
        "[" + ", ".join(mp.nstr(texture[i, j], 18) for j in range(3)) + "]"
        for i in range(3)
    ]
    lines = [
        "# nu-scalaron-falsification -- hypothesis v3",
        "# AUTO-FROZEN by nu_texture_census_probe.py only after the predeclared HIT gate.",
        "# EXPLORATION ONLY; does not close FLAV.NUSCALE.05.",
        "candidate:",
        "  name: " + json.dumps(candidate.name),
        "  provenance: " + json.dumps(candidate.provenance),
        "  normalization: \"sigma_max(Y_nu) = y_t(M3)\"",
        "  y3_frozen: " + mp.nstr(Y3_FROZEN, 18),
        "  Y_nu:",
    ]
    lines.extend("    - " + row for row in matrix_rows)
    lines.extend(
        [
            "majorana:",
            "  formula: \"M_scal * diag(epsilon, 2 epsilon, 3)\"",
            "  M1_GeV: " + mp.nstr(M_HEAVY_GEV[0], 18),
            "  M2_GeV: " + mp.nstr(M_HEAVY_GEV[1], 18),
            "  M3_GeV: " + mp.nstr(M_HEAVY_GEV[2], 18),
            "predictions:",
        ]
    )
    for key in (
        "masses_eV",
        "dm2_21_eV2",
        "dm2_31_eV2",
        "dm2_ratio",
        "sigma_mnu_eV",
        "sin2_theta12",
        "sin2_theta13",
        "sin2_theta23",
        "delta_deg",
        "J_CP",
        "m_beta_eV",
        "m_bb_eV",
    ):
        lines.append("  %s: %s" % (key, yaml_scalar(result[key])))
    lines.append("leptogenesis:")
    for key, value in leptogenesis.items():
        lines.append("  %s: %s" % (key, yaml_scalar(value)))
    lines.extend(
        [
            "honest_scope: >",
            "  Tree-level type-I seesaw with inherited v2 low-energy factors;",
            "  charged-lepton/address basis identification assumed; no continuous fit;",
            "  no RG re-derivation of Y; no closure of FLAV.NUSCALE.05.",
            "",
        ]
    )
    payload = "\n".join(lines)
    with open(V3_PATH, "w", encoding="utf-8") as handle:
        handle.write(payload)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def print_candidate_declaration(candidates: list[Candidate]) -> None:
    print("CANDIDATE DECLARATION (before evaluation)")
    for name, matrix, provenance in NAMED_PRIMITIVES:
        print("  %-13s %s  | %s" % (name, matrix.tolist(), provenance))
    print("  independent coefficients:",
          [label for label, _value in SMALL_COEFFICIENTS])
    print("  tail: n={4,5,6}, r={1,53/54,5/3,2/3}, "
          "all 7 nonempty projector subsets")
    print("  involutions: raw, transpose, Hermitian/symmetric; exact deduplication")
    print("  unique census size:", len(candidates))


def main() -> int:
    checks: list[tuple[str, bool]] = []
    candidates = build_candidates()
    print_candidate_declaration(candidates)

    checks.append(("Qplus exact", Q_PLUS == sp.Matrix([[3, 0, 0], [0, 2, 0], [0, 2, 1]])))
    checks.append(("projectors complete", sp.simplify(P1 + P2 + P3 - I3) == sp.zeros(3)))
    checks.append(("L=K+Q exact", L_MAT == K_MAT + Q_MAT))
    checks.append(("F=R+Q exact", F_MAT == R_MAT + Q_MAT))
    checks.append(("candidate census nonempty", len(candidates) > 0))
    checks.append(("candidate census below 1e4", len(candidates) < 10_000))
    checks.append(("candidate matrices unique", len({matrix_key(c.matrix) for c in candidates}) == len(candidates)))
    checks.append(("null entry range covers raw inventory", NULL_ENTRY_MIN == -2 and NULL_ENTRY_MAX == 8))

    print("\nEVALUATION")
    corpus_results = [
        evaluate_matrix(candidate.name, to_mp_matrix(candidate.matrix))
        for candidate in candidates
    ]
    null_results = [
        evaluate_matrix(name, matrix)
        for name, matrix in build_null()
    ]
    checks.append(("all corpus candidates evaluated", len(corpus_results) == len(candidates)))
    checks.append(("exactly 200 nulls evaluated", len(null_results) == N_NULL))
    checks.append(
        (
            "all low-energy matrices symmetric",
            all((row["symmetry_residual"] or 0.0) < 1e-45 for row in corpus_results),
        )
    )
    checks.append(
        (
            "single normalization enforced",
            all(
                abs(float(row["normalized_spectral_norm"]) - float(Y3_FROZEN)) < 1e-12
                for row in corpus_results
            ),
        )
    )

    corpus_results.sort(
        key=lambda row: (
            math.inf if row["miss_factor"] is None else float(row["miss_factor"]),
            str(row["name"]),
        )
    )
    null_results.sort(
        key=lambda row: (
            math.inf if row["miss_factor"] is None else float(row["miss_factor"]),
            str(row["name"]),
        )
    )
    hits = [row for row in corpus_results if row["hit"]]
    near_misses = [row for row in corpus_results if row["near_miss"]]
    null_hits = [row for row in null_results if row["hit"]]
    null_near = [row for row in null_results if row["near_miss"]]
    corpus_hit_rate = len(hits) / len(corpus_results)
    null_hit_rate = len(null_hits) / len(null_results)
    enrichment = (
        corpus_hit_rate / null_hit_rate if null_hit_rate > 0 else
        math.inf if corpus_hit_rate > 0 else 0.0
    )

    v3_sha = None
    leptogenesis = None
    if hits:
        top_hit_result = hits[0]
        top_candidate = next(c for c in candidates if c.name == top_hit_result["name"])
        leptogenesis = leptogenesis_for_hit(top_candidate, top_hit_result)
        v3_sha = freeze_v3(top_candidate, top_hit_result, leptogenesis)
        verdict = "NU_TEXTURE_HIT(%s)" % top_hit_result["name"]
    elif near_misses:
        names = ",".join(str(row["name"]) for row in near_misses[:10])
        verdict = "NU_TEXTURE_NEAR_MISS(%s)" % names
    else:
        verdict = "NU_TEXTURE_CENSUS_NULL"

    top_ten = corpus_results[:10]
    output = {
        "project": "nu-scalaron-falsification",
        "probe": "nu_texture_census_probe.py",
        "scope": "EXPLORATION ONLY",
        "protocol": {
            "candidate_grammar": {
                "named": [
                    {
                        "name": name,
                        "matrix": matrix_to_json(matrix),
                        "provenance": provenance,
                    }
                    for name, matrix, provenance in NAMED_PRIMITIVES
                ],
                "small_coefficients": [label for label, _value in SMALL_COEFFICIENTS],
                "small_family": "sum_i c_i P_i, not all c_i zero",
                "tail": "r*phi0^n*sum_{i in S} P_i; n=4..6; four rationals; seven nonempty subsets",
                "involutions": ["raw", "transpose", "Hermitian/symmetric part"],
                "deduplication": "50-digit matrix value key",
            },
            "normalization": "largest singular value = y_t(M3); one global factor",
            "y3_frozen": float(Y3_FROZEN),
            "matching_formula": "-(246.22^2/2) Y^T M_R^-1 Y",
            "low_energy_formula": "-(246.22^2/2) Y^T diag(R_i/M_i) Y",
            "R_down_frozen_v2": [float(value) for value in R_DOWN],
            "charged_lepton_basis_assumption": (
                "published generation/address basis equals charged-lepton basis; "
                "M_R uses v69 ordering"
            ),
            "hit_gate": "all four NuFIT pulls <=3 and Sigma<0.0642 eV",
            "near_gate": "non-hit with max(pull/3, Sigma/0.0642)<=10",
        },
        "constants": {
            "phi0": float(PHI0),
            "epsilon": float(EPSILON),
            "M_scal_GeV": float(M_SCAL_GEV),
            "M1_GeV": float(M_HEAVY_GEV[0]),
            "M2_GeV": float(M_HEAVY_GEV[1]),
            "M3_GeV": float(M_HEAVY_GEV[2]),
            "dm2_ratio_target": float(RATIO_TARGET),
            "dm2_ratio_sigma": float(RATIO_SIGMA),
            "tfpt_v270_angles": {key: float(value) for key, value in TFPT_ANGLES.items()},
        },
        "census": {
            "unique_candidates": len(corpus_results),
            "hits": len(hits),
            "near_misses": len(near_misses),
            "hit_rate": corpus_hit_rate,
            "top_10": top_ten,
            "all_hit_names": [row["name"] for row in hits],
            "all_near_miss_names": [row["name"] for row in near_misses],
        },
        "null": {
            "seed": NULL_SEED,
            "count": N_NULL,
            "integer_entry_range_inclusive": [NULL_ENTRY_MIN, NULL_ENTRY_MAX],
            "hits": len(null_hits),
            "near_misses": len(null_near),
            "hit_rate": null_hit_rate,
            "top_10": null_results[:10],
            "corpus_over_null_hit_rate": (
                None if math.isinf(enrichment) else enrichment
            ),
        },
        "verdict": verdict,
        "v3": {
            "frozen": bool(v3_sha),
            "path": V3_PATH if v3_sha else None,
            "sha16": v3_sha,
            "leptogenesis": leptogenesis,
        },
        "honest_scope": (
            "Tree-level type-I seesaw with inherited frozen v2 low-energy "
            "factors; normal ordering; charged-lepton/address basis assumed; "
            "no continuous fit; no RG re-derivation of Y; v9 and v263 objects "
            "are examples, not frozen Dirac Yukawas; nothing closes "
            "FLAV.NUSCALE.05. Null comparison is exploratory because the "
            "corpus grammar contains correlated candidates."
        ),
    }
    os.makedirs(os.path.dirname(RESULT_PATH), exist_ok=True)
    with open(RESULT_PATH, "w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, sort_keys=False)

    print("\nTOP 10")
    print("rank  name                                      miss      r_dm2      "
          "s12       s13       s23       Sigma[eV] hit near")
    for rank, row in enumerate(top_ten, start=1):
        print(
            "%-5d %-41s %8.3g %10.4g %9.4g %9.4g %9.4g %10.4g  %s   %s"
            % (
                rank,
                str(row["name"])[:41],
                float(row["miss_factor"]),
                float(row["dm2_ratio"]),
                float(row["sin2_theta12"]),
                float(row["sin2_theta13"]),
                float(row["sin2_theta23"]),
                float(row["sigma_mnu_eV"]),
                "Y" if row["hit"] else "N",
                "Y" if row["near_miss"] else "N",
            )
        )
    print(
        "\nNULL COMPARISON: corpus %d/%d hits (%.6g), null %d/%d hits "
        "(%.6g), corpus/null=%s"
        % (
            len(hits),
            len(corpus_results),
            corpus_hit_rate,
            len(null_hits),
            len(null_results),
            null_hit_rate,
            "infinite" if math.isinf(enrichment) else "%.6g" % enrichment,
        )
    )
    print("NEAR MISSES: corpus %d, null %d" % (len(near_misses), len(null_near)))
    print("VERDICT", verdict)
    if v3_sha:
        print("V3 FREEZE", V3_PATH, "SHA-16", v3_sha)
        print("LEPTOGENESIS eta_B", leptogenesis["eta_B"],
              "survives", leptogenesis["survives_obs_over_3_to_3obs"])
    else:
        print("V3 FREEZE not created (no HIT)")
    print("WROTE", RESULT_PATH)

    for label, passed in checks:
        print(("PASS " if passed else "FAIL ") + label)
    all_pass = all(passed for _label, passed in checks)
    print("ALL PASS" if all_pass else "PROTOCOL FAILURE")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
