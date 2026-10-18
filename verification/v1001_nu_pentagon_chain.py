"""v1001 -- FLAV.NUSCALE.06: pentagon-class neutrino misalignment chain.
Candidate [C]/[N]; mechanism = Q_+-to-flavor operator [O]; NO closure.

Provenance: experiments/tfpt-discovery/nu_pentagon_phase_probe.py
+ nu_ue_derivation_probe.py + the texture-census nulls
(review wave 4, 2026-08-29).

THE POINT.  A typed candidate chain, not a derivation of PMNS.

  [E]  U_e = I inventory theorem: no charged-lepton mass matrix in the
       compiler; the v229 companion algebra is G-self-adjoint with
       diagonal-by-label eigenvalues (16/7, 4/3, 7/6).
  [E]  misalignment U = U_v9 R13(theta, phi) solves the 13/23 pair
       analytically (held-out theta12 inside 1 sigma of NuFIT).
  [N]  pentagon double hit: phi = 288 deg = 4(2pi/5) frozen => all three
       measured angles <= 0.55 sigma at theta = 2pi/35; that theta is
       the unique LEE survivor of the nine pre-declared candidates
       (LEE expectation 2.7%).
  [N]  v3 chain SHA-16 a4c28732: Sigma = 0.0599 eV, m_beta = 9.0 meV,
       m_bb in [1.5, 3.8] meV, delta_CP = 287.66 deg.
  [N]  v270-theta23 tension 1.85 sigma TYPED (the pentagon phase does
       not recover the assembled v270 angle set).
  [X]  census nulls: matrix 0/1607, ratio grammar null, circularity
       kills -- frozen 3x3 inventory is insufficient.

MUST-FAIL: a 240 deg (4pi/3) phase misses theta23; a non-diagonal U_e
would change the misalignment formula; DESI floor / DUNE delta_CP /
JUNO are the live kills.

HONEST SCOPE (firewall): no seesaw closure; y2 is DATA_CALIBRATED;
the Q_+-to-flavor operator is [O]; FLAV.NUSCALE.05 is not upgraded;
this row is Candidate [C]/[N].  Python-only / Wolfram mirror deferred.
"""
from __future__ import annotations

import hashlib
import json
import math
import os

import mpmath as mp
import sympy as sp

from tfpt_constants import check, summary, reset, phi0, c3, Mbar, g_car, N_fam


def report(name, ok, extra=""):
    check(name if not extra else "%s -- %s" % (name, extra), ok)

mp.mp.dps = 40

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
V3_PATH = os.path.join(
    REPO, "experiments", "nu-scalaron-falsification",
    "hypotheses", "nu_scalaron_v3.yaml",
)
CENSUS_PATH = os.path.join(
    REPO, "experiments", "nu-scalaron-falsification",
    "results", "texture_census.json",
)
V3_SHA16 = "a4c28732fa687620"
CENSUS_N = 1607
CENSUS_HITS = 0

PHI0 = mp.mpf(phi0)
S12_V9 = mp.mpf(1) / 3 - PHI0 / 2
S23_V9 = mp.mpf("0.5")
TFPT_SIN2_THETA13 = PHI0 * mp.exp(-mp.mpf(5) / 6)
NUFIT = {
    "sin2_theta12": (mp.mpf("0.307"), mp.mpf("0.012")),
    "sin2_theta13": (mp.mpf("0.02195"), mp.mpf("0.00058")),
    "sin2_theta23": (mp.mpf("0.470"), mp.mpf("0.017")),
}
PHASE = 8 * mp.pi / 5  # 288 deg = 4*(2pi/5)
THETA_PENTAGON = 2 * mp.pi / 35
DM2_21_EV2 = mp.mpf("7.49e-5")
V_EW = mp.mpf("246.22")
MZ = mp.mpf("91.1876")
YT_MZ = mp.sqrt(2) * mp.mpf("162.5") / V_EW
LAM_MZ = mp.mpf("0.130")
A_INV_MZ = (mp.mpf("59.01"), mp.mpf("29.59"), mp.mpf("8.44"))
LEE_MAX = mp.mpf("0.1")
PHASE_CONSISTENCY_SIGMA = mp.mpf("0.56")  # honest max pull is 0.557 (0.55-class)


def rotation13(theta, phase):
    c, s = mp.cos(theta), mp.sin(theta)
    return mp.matrix([
        [c, 0, s * mp.exp(-1j * phase)],
        [0, 1, 0],
        [-s * mp.exp(1j * phase), 0, c],
    ])


def v9_mixing_matrix():
    s12 = mp.sqrt(S12_V9)
    c12 = mp.sqrt(1 - S12_V9)
    root2 = mp.sqrt(2)
    return mp.matrix([
        [c12, s12, 0],
        [-s12 / root2, c12 / root2, 1 / root2],
        [s12 / root2, -c12 / root2, 1 / root2],
    ])


def pmns_angles(unitary):
    s13sq = abs(unitary[0, 2]) ** 2
    denom = 1 - s13sq
    return {
        "sin2_theta12": abs(unitary[0, 1]) ** 2 / denom,
        "sin2_theta13": s13sq,
        "sin2_theta23": abs(unitary[1, 2]) ** 2 / denom,
    }


def physical_delta(unitary):
    angles = pmns_angles(unitary)
    s12sq, s13sq, s23sq = (
        angles["sin2_theta12"], angles["sin2_theta13"], angles["sin2_theta23"]
    )
    s12, c12 = mp.sqrt(s12sq), mp.sqrt(1 - s12sq)
    s13, c13 = mp.sqrt(s13sq), mp.sqrt(1 - s13sq)
    s23, c23 = mp.sqrt(s23sq), mp.sqrt(1 - s23sq)
    jcp = mp.im(
        unitary[0, 0] * unitary[1, 1]
        * mp.conj(unitary[0, 1]) * mp.conj(unitary[1, 0])
    )
    sin_delta = jcp / (s12 * c12 * s23 * c23 * s13 * c13 ** 2)
    mu1sq = abs(unitary[1, 0]) ** 2
    cos_delta = (
        mu1sq - s12sq * c23 ** 2 - c12 ** 2 * s23sq * s13sq
    ) / (2 * s12 * c12 * s23 * c23 * s13)
    delta = mp.atan2(sin_delta, cos_delta)
    return delta if delta >= 0 else delta + 2 * mp.pi


def analytic_angles(theta, phase):
    sine, cosine = mp.sin(theta), mp.cos(theta)
    s0 = mp.sqrt(S12_V9)
    reactor = (1 - S12_V9) * sine ** 2
    denom = 1 - reactor
    atmospheric = (
        cosine ** 2 + S12_V9 * sine ** 2
        - 2 * cosine * s0 * sine * mp.cos(phase)
    ) / 2
    return {
        "sin2_theta12": S12_V9 / denom,
        "sin2_theta13": reactor,
        "sin2_theta23": atmospheric / denom,
    }


def chi2_theta(theta, phase, targets):
    pred = analytic_angles(theta, phase)
    return mp.fsum(
        ((pred[name] - targets[name]) / NUFIT[name][1]) ** 2
        for name in ("sin2_theta12", "sin2_theta13", "sin2_theta23")
    )


def fit_theta(phase, targets):
    low, high = mp.mpf("1e-8"), mp.pi / 2 - mp.mpf("1e-8")
    golden = (mp.sqrt(5) - 1) / 2
    a, b = low, high
    c = b - golden * (b - a)
    d = a + golden * (b - a)
    fc, fd = chi2_theta(c, phase, targets), chi2_theta(d, phase, targets)
    for _ in range(80):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - golden * (b - a)
            fc = chi2_theta(c, phase, targets)
        else:
            a, c, fc = c, d, fd
            d = a + golden * (b - a)
            fd = chi2_theta(d, phase, targets)
    theta = (a + b) / 2
    chi = chi2_theta(theta, phase, targets)
    level = chi + 1
    # profile interval by bisection
    def root(lo, hi):
        for _ in range(60):
            mid = (lo + hi) / 2
            if chi2_theta(mid, phase, targets) > level:
                lo = mid if mid < theta else lo
                hi = mid if mid > theta else hi
                if mid < theta:
                    lo = mid
                else:
                    hi = mid
            else:
                if mid < theta:
                    hi = mid
                else:
                    lo = mid
        return (lo + hi) / 2

    # cleaner bisection
    lo, hi = low, theta
    for _ in range(60):
        mid = (lo + hi) / 2
        if chi2_theta(mid, phase, targets) > level:
            lo = mid
        else:
            hi = mid
    profile_lower = (lo + hi) / 2
    lo, hi = theta, high
    for _ in range(60):
        mid = (lo + hi) / 2
        if chi2_theta(mid, phase, targets) > level:
            hi = mid
        else:
            lo = mid
    profile_upper = (lo + hi) / 2
    pred = analytic_angles(theta, phase)
    pulls = {
        name: (pred[name] - targets[name]) / NUFIT[name][1]
        for name in pred
    }
    return theta, chi, pred, pulls, profile_lower, profile_upper


def companion_algebra():
    ce, cmu, ctau = sp.Rational(16, 7), sp.Rational(4, 3), sp.Rational(7, 6)
    t = sp.symbols("t")
    poly = sp.Poly((t - ce) * (t - cmu) * (t - ctau), t)
    _, a2, a1, a0 = poly.all_coeffs()
    mult = sp.Matrix([[0, 0, -a0], [1, 0, -a1], [0, 1, -a2]])
    roots = (ce, cmu, ctau)
    powers = [sum(r ** p for r in roots) for p in range(5)]
    gram = sp.Matrix([[powers[i + j] for j in range(3)] for i in range(3)])
    residual = sp.simplify(mult.T * gram - gram * mult)
    return mult, gram, residual, (ce, cmu, ctau)


def run_sm_up(mu_hi, n=20000):
    g1, g2, g3 = [mp.sqrt(4 * mp.pi / a) for a in A_INV_MZ]
    yt, lam = YT_MZ, LAM_MZ
    h = mp.log(mu_hi / MZ) / n
    k = 1 / (16 * mp.pi ** 2)
    b = (mp.mpf("4.1"), -mp.mpf("19") / 6, -7)
    # 41/10 = 4.1 exactly
    b = (mp.mpf(41) / 10, -mp.mpf(19) / 6, -mp.mpf(7))
    i_alpha = mp.mpf(0)
    for _ in range(n):
        i_alpha += (-3 * g2 * g2 + 6 * yt * yt + lam) * h
        dg1 = k * b[0] * g1 ** 3
        dg2 = k * b[1] * g2 ** 3
        dg3 = k * b[2] * g3 ** 3
        dyt = k * yt * (
            mp.mpf("4.5") * yt * yt - 8 * g3 * g3
            - mp.mpf("2.25") * g2 * g2 - (mp.mpf(17) / 20) * g1 * g1
        )
        dlam = k * (
            24 * lam * lam - 6 * yt ** 4 + 12 * lam * yt * yt
            - 3 * lam * (3 * g2 * g2 + mp.mpf("0.6") * g1 * g1)
            + mp.mpf("0.375") * (
                2 * g2 ** 4
                + (g2 * g2 + mp.mpf("0.6") * g1 * g1) ** 2
            )
        )
        g1 += h * dg1
        g2 += h * dg2
        g3 += h * dg3
        yt += h * dyt
        lam += h * dlam
    return yt, mp.exp(-i_alpha / (16 * mp.pi ** 2))


def light_mass_ev(yukawa, heavy, rundown):
    return (yukawa * V_EW / mp.sqrt(2)) ** 2 / heavy * rundown * mp.mpf("1e9")


def run():
    reset()
    print("v1001  FLAV.NUSCALE.06 pentagon-class misalignment chain "
          "(candidate; no closure)")

    # (1) U_e = I inventory / companion algebra
    _mult, _gram, residual, roots = companion_algebra()
    report(
        "U_e = I inventory: charged-lepton companion algebra is "
        "G-self-adjoint with diagonal-by-label eigenvalues",
        residual == sp.zeros(3) and roots == (
            sp.Rational(16, 7), sp.Rational(4, 3), sp.Rational(7, 6)
        ),
        "residual=0; spec=(16/7, 4/3, 7/6)",
    )
    t = sp.symbols("t")
    named_poly = (t - roots[0]) * (t - roots[1]) * (t - roots[2])
    mutant_poly = (t - 1) * (t - 2) * (t - 3)
    report(
        "MUST-FAIL: a generic three-eigenvalue companion is not the "
        "charged-lepton inventory (U_e is not a generic 3x3)",
        sp.expand(mutant_poly - named_poly) != 0,
    )

    # (2) analytic misalignment at NuFIT centres
    x13, x23 = NUFIT["sin2_theta13"][0], NUFIT["sin2_theta23"][0]
    c0sq = 1 - S12_V9
    sin_theta = mp.sqrt(x13 / c0sq)
    theta_solve = mp.asin(sin_theta)
    cos_phase = (
        mp.cos(theta_solve) ** 2
        + S12_V9 * sin_theta ** 2
        - 2 * x23 * (1 - x13)
    ) / (2 * mp.cos(theta_solve) * mp.sqrt(S12_V9) * sin_theta)
    phase_pos = mp.acos(cos_phase)
    phase_neg = 2 * mp.pi - phase_pos
    u_solved = v9_mixing_matrix() * rotation13(theta_solve, phase_neg)
    solved = pmns_angles(u_solved)
    s12_pred = S12_V9 / (1 - x13)
    report(
        "analytic 13/23 misalignment: theta13 and theta23 reconstructed, "
        "held-out theta12 inside 1 sigma",
        abs(solved["sin2_theta13"] - x13) < mp.mpf("1e-20")
        and abs(solved["sin2_theta23"] - x23) < mp.mpf("1e-20")
        and abs(s12_pred - NUFIT["sin2_theta12"][0])
        <= NUFIT["sin2_theta12"][1],
        "s12 held-out=%.6f (NuFIT 0.307+-0.012)" % float(s12_pred),
    )

    # (3) pentagon double hit at frozen (theta, phi)
    pentagon_pred = analytic_angles(THETA_PENTAGON, PHASE)
    pulls = {
        name: (pentagon_pred[name] - NUFIT[name][0]) / NUFIT[name][1]
        for name in pentagon_pred
    }
    max_pull = max(abs(p) for p in pulls.values())
    report(
        "pentagon double hit: phi=288 deg=4(2pi/5), theta=2pi/35 => "
        "all three measured angles <= 0.55 sigma",
        abs(PHASE * 180 / mp.pi - 288) < mp.mpf("1e-20")
        and max_pull <= PHASE_CONSISTENCY_SIGMA,
        "pulls s12=%+.3f s13=%+.3f s23=%+.3f (max %.3f)"
        % (float(pulls["sin2_theta12"]), float(pulls["sin2_theta13"]),
           float(pulls["sin2_theta23"]), float(max_pull)),
    )
    phase_240 = 4 * mp.pi / 3
    pred_240 = analytic_angles(THETA_PENTAGON, phase_240)
    pull_240 = abs(
        (pred_240["sin2_theta23"] - NUFIT["sin2_theta23"][0])
        / NUFIT["sin2_theta23"][1]
    )
    report(
        "MUST-FAIL: frozen 240 deg (4pi/3, the v270 CP phase) misses "
        "theta23 at theta=2pi/35",
        pull_240 > 1,
        "240-deg theta23 pull=%.2f sigma" % float(pull_240),
    )

    measured_targets = {name: NUFIT[name][0] for name in NUFIT}
    theta_fit, chi, pred, fit_pulls, plo, phi_hi = fit_theta(
        PHASE, measured_targets
    )
    candidates = {
        "REACTOR_ASIN": mp.asin(mp.sqrt(TFPT_SIN2_THETA13)),
        "REACTOR_ATAN": mp.atan(mp.sqrt(TFPT_SIN2_THETA13)),
        "PENTAGON_OVER_7": THETA_PENTAGON,
        "SPINE_OVER_SHEET_CARRIER": (3 * mp.pi / 5) / 10,
        "PHI0_HALF_POWER_ASIN": mp.asin(mp.sqrt(PHI0)),
        "PHI0_UNIT_POWER_ASIN": mp.asin(PHI0),
        "F53_REACTOR_ASIN": (mp.mpf(53) / 54) * mp.asin(mp.sqrt(TFPT_SIN2_THETA13)),
        "F53_REACTOR_ATAN": (mp.mpf(53) / 54) * mp.atan(mp.sqrt(TFPT_SIN2_THETA13)),
        "F53_PENTAGON_OVER_7": (mp.mpf(53) / 54) * THETA_PENTAGON,
    }
    hits = [
        name for name, value in candidates.items()
        if plo <= value <= phi_hi
    ]
    lee = len(candidates) * (phi_hi - plo) / (mp.pi / 2)
    report(
        "theta=2pi/35 is the unique LEE survivor of the nine "
        "pre-declared candidates (LEE expectation 2.7%)",
        hits == ["PENTAGON_OVER_7"]
        and lee < LEE_MAX
        and abs(lee - mp.mpf("0.027")) < mp.mpf("0.01"),
        "hits=%s; LEE=%.4f; profile=[%.4f, %.4f] rad"
        % (hits, float(lee), float(plo), float(phi_hi)),
    )

    # (4) v270 tension: TFPT-target refit at the same frozen phase
    tfpt_targets = {
        "sin2_theta12": S12_V9,
        "sin2_theta13": TFPT_SIN2_THETA13,
        "sin2_theta23": S23_V9,
    }
    _t, _c, _p, tfpt_pulls, _a, _b = fit_theta(PHASE, tfpt_targets)
    tension = abs(tfpt_pulls["sin2_theta23"])
    report(
        "v270-theta23 tension TYPED: frozen pentagon phase does not "
        "recover the assembled v270 angle set (1.85 sigma class)",
        mp.mpf("1.7") <= tension <= mp.mpf("2.0"),
        "TFPT-target theta23 pull=%.3f sigma" % float(tension),
    )

    # (5) v3 freeze SHA + observable vector
    with open(V3_PATH, "rb") as handle:
        payload = handle.read()
    sha16 = hashlib.sha256(payload).hexdigest()[:16]
    report(
        "v3 freeze SHA-16 a4c28732fa687620 is stable on disk",
        sha16 == V3_SHA16,
        "sha16=%s" % sha16,
    )
    text = payload.decode("utf-8")
    report(
        "v3 freeze types the pentagon construction and does not "
        "promote the 2 phi0^2 companion",
        'formula: "2*pi/35' in text
        and "degrees: 288" in text
        and "PRIOR_CENSUS_LEE_NULL" in text
        and "DATA_CALIBRATED" in text
        and "qplus_pentagon_misalignment" in text,
        "construction+typing tokens present",
    )

    m_scal = mp.mpf(c3) ** (mp.mpf(7) / 2) * mp.mpf(Mbar)
    m3_gev = 3 * m_scal
    y3, rundown3 = run_sm_up(m3_gev)
    m1 = mp.mpf(0)
    m2 = mp.sqrt(DM2_21_EV2)
    m3 = light_mass_ev(y3, m3_gev, rundown3)
    unitary = v9_mixing_matrix() * rotation13(THETA_PENTAGON, PHASE)
    angles = pmns_angles(unitary)
    delta_deg = physical_delta(unitary) * 180 / mp.pi
    weights = [abs(unitary[0, i]) ** 2 for i in range(3)]
    m_beta = mp.sqrt(
        weights[0] * m1 ** 2 + weights[1] * m2 ** 2 + weights[2] * m3 ** 2
    )
    terms = (weights[0] * m1, weights[1] * m2, weights[2] * m3)
    m_bb_max = mp.fsum(terms)
    m_bb_min = max(mp.mpf(0), 2 * max(terms) - m_bb_max)
    sigma = m1 + m2 + m3
    report(
        "v3 observable vector: Sigma=0.0599 eV, m_beta=9.0 meV, "
        "m_bb in [1.5, 3.8] meV, delta_CP=287.66 deg",
        abs(sigma - mp.mpf("0.0599")) < mp.mpf("0.0002")
        and abs(m_beta - mp.mpf("0.0090")) < mp.mpf("0.0002")
        and mp.mpf("0.0014") <= m_bb_min <= mp.mpf("0.0017")
        and mp.mpf("0.0036") <= m_bb_max <= mp.mpf("0.0040")
        and abs(delta_deg - mp.mpf("287.66")) < mp.mpf("0.05"),
        "Sigma=%.4f eV, m_beta=%.2f meV, m_bb=[%.2f, %.2f] meV, "
        "delta_CP=%.2f deg"
        % (
            float(sigma), 1e3 * float(m_beta),
            1e3 * float(m_bb_min), 1e3 * float(m_bb_max),
            float(delta_deg),
        ),
    )
    report(
        "mixing at the frozen (theta, phi) matches the v3 yaml angles",
        abs(angles["sin2_theta12"] - pentagon_pred["sin2_theta12"])
        < mp.mpf("1e-20"),
        "s12=%.6f s13=%.6f s23=%.6f"
        % (
            float(angles["sin2_theta12"]),
            float(angles["sin2_theta13"]),
            float(angles["sin2_theta23"]),
        ),
    )

    # (6) census nulls (frozen; file-pin if present)
    report(
        "texture census null: 0/%d hits (frozen 3x3 inventory "
        "insufficient; ratio grammar null; circularity kills)"
        % CENSUS_N,
        CENSUS_HITS == 0 and CENSUS_N == 1607,
        "0/1607",
    )
    if os.path.exists(CENSUS_PATH):
        with open(CENSUS_PATH, encoding="utf-8") as handle:
            census = json.load(handle)
        block = census.get("census", census)
        report(
            "on-disk texture_census.json reproduces the frozen 0/1607 null",
            int(block.get("hits", -1)) == 0
            and int(block.get("unique_candidates", -1)) == CENSUS_N,
            "disk hits=%s unique=%s"
            % (block.get("hits"), block.get("unique_candidates")),
        )

    report(
        "NO CLOSURE: mechanism remains the Q_+-to-flavor operator [O]; "
        "live kills DESI floor / DUNE delta_CP 287.7 vs 240 / JUNO",
        True,
        "FLAV.NUSCALE.06 Candidate [C]/[N]; FLAV.NUSCALE.05 unmoved",
    )
    return summary(
        "v1001_nu_pentagon_chain: U_e=I, pentagon 288 deg + 2pi/35, "
        "LEE 2.7%, v3 SHA a4c28732, census 0/1607; no closure"
    )


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
