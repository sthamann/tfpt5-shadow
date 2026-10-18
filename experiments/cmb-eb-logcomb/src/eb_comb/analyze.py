"""EB log-comb search at the frozen kernel frequency (prereg v1).

Model (frozen, hypotheses/eb_logcomb_v1.yaml, SHA-16 e519ca9eb36dbb7a):

    EB_b = s0 * T_b * [1 + A cos(omega ln(ell_c/ell_star) + phi)]

linearised as y = u*T + a*T*cos(omega ln x) + b*T*sin(omega ln x) with
A = sqrt(a^2 + b^2)/|u|, phi profiled.  Gaussian diagonal likelihood.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parents[2]
DATA = HERE / "data" / "HFI_f_sky_092_EB_o.npy"
RESULTS = HERE / "results" / "results.json"
YAML = HERE / "hypotheses" / "eb_logcomb_v1.yaml"
YAML_SHA16 = "e519ca9eb36dbb7a"

# ---- frozen constants (mirror of the YAML) --------------------------------
OMEGA_PLUS = 2.0 * math.pi / math.log((3.0 / 2.0) ** 6)   # 2.58270695
OMEGA_MINUS = 2.0 * math.pi / math.log(3.0 ** 6)          # 0.95320029
ELL_STAR = 150.0
EPS_CANDIDATE = 0.017302
ELL_MIN, ELL_MAX, DELTA_ELL = 51, 1490, 20
N_NULLS = 2000
SEED = 20260827
P_HINT = 0.01
P_ESCALATE = 0.001
LEE_GRID = np.geomspace(0.6, 12.0, 60)
A_MAX = 0.5
REACH_GATE = 2.8

CAMB_PARAMS = dict(tau=0.0544, ns=0.9649, H0=67.36, ombh2=0.02237,
                   omch2=0.12, As=2.1e-9)


def yaml_sha16() -> str:
    return hashlib.sha256(YAML.read_bytes()).hexdigest()[:16]


def bin_labels() -> np.ndarray:
    return np.arange(ELL_MIN, ELL_MAX + 1, DELTA_ELL)


def bin_centers() -> np.ndarray:
    return bin_labels() + (DELTA_ELL - 1) / 2.0


def template_ee_minus_bb() -> np.ndarray:
    """binned LCDM (EE - BB), raw C_ell in muK^2 (tutorial convention)."""
    import camb

    cp = camb.set_params(lmax=ELL_MAX, **CAMB_PARAMS)
    cls = camb.get_results(cp).get_cmb_power_spectra(
        lmax=ELL_MAX, raw_cl=True, CMB_unit="muK")["total"]
    ee_bb = cls[:, 1] - cls[:, 2]
    labels = bin_labels()
    return np.array([ee_bb[lb:lb + DELTA_ELL].mean() for lb in labels])


def fit_comb(y: np.ndarray, sig: np.ndarray, t: np.ndarray,
             omega: float, centers: np.ndarray) -> dict:
    """chi2(A=0), chi2(A free) and (A, phi) at fixed omega (linear lsq)."""
    lnx = np.log(centers / ELL_STAR)
    x0 = t / sig
    xc = t * np.cos(omega * lnx) / sig
    xs = t * np.sin(omega * lnx) / sig
    yw = y / sig

    def lsq(cols):
        m = np.vstack(cols).T
        coef, *_ = np.linalg.lstsq(m, yw, rcond=None)
        r = yw - m @ coef
        return float(r @ r), coef

    chi2_0, c0 = lsq([x0])
    chi2_1, c1 = lsq([x0, xc, xs])
    u, a, b = c1
    amp = math.hypot(a, b) / abs(u) if u != 0 else float("inf")
    phi = math.atan2(-b, a) % (2 * math.pi)
    return {"chi2_null": chi2_0, "chi2_comb": chi2_1,
            "dchi2": chi2_0 - chi2_1, "s0": float(c0[0]),
            "A": float(amp), "phi": float(phi)}


def a95_profile(y, sig, t, omega, centers, chi2_min) -> float:
    """one-sided 95% upper bound: first A0 ABOVE the profile minimum with
    min_phi,s0 chi2(A0) >= chi2_min + 2.71 (profile likelihood, frozen)."""
    lnx = np.log(centers / ELL_STAR)
    phis = np.linspace(0.0, 2 * math.pi, 128, endpoint=False)
    grid = np.linspace(0.0, A_MAX, 501)
    chis = np.empty_like(grid)
    yw = y / sig
    for i, a0 in enumerate(grid):
        best = np.inf
        for ph in phis:
            shape = t * (1.0 + a0 * np.cos(omega * lnx + ph))
            xw = shape / sig
            u = float(xw @ yw) / float(xw @ xw)
            r = yw - u * xw
            best = min(best, float(r @ r))
        chis[i] = best
    i0 = int(np.argmin(chis))
    for i in range(i0, len(grid)):
        if chis[i] >= chi2_min + 2.71:
            return float(grid[i])
    return float("nan")


def analyze() -> dict:
    assert yaml_sha16() == YAML_SHA16, "hypothesis file changed after freeze"
    raw = np.load(DATA)
    y, sig = raw[:, 0], raw[:, 1]
    centers = bin_centers()
    assert raw.shape == (len(centers), 2)
    t = template_ee_minus_bb()
    sha = hashlib.sha256(DATA.read_bytes()).hexdigest()

    reach = math.log(ELL_MAX / ELL_MIN) * OMEGA_PLUS / (2 * math.pi)

    fit_plus = fit_comb(y, sig, t, OMEGA_PLUS, centers)
    fit_minus = fit_comb(y, sig, t, OMEGA_MINUS, centers)
    a95 = a95_profile(y, sig, t, OMEGA_PLUS, centers, fit_plus["chi2_comb"])
    lee_data = np.array([fit_comb(y, sig, t, w, centers)["dchi2"]
                         for w in LEE_GRID])
    rank = int(1 + np.sum(lee_data > fit_plus["dchi2"]))

    # null battery: Gaussian around the A=0 best fit
    rng = np.random.default_rng(SEED)
    base = fit_plus["s0"] * t
    d_plus, d_minus, d_max = [], [], []
    for _ in range(N_NULLS):
        ysim = base + rng.normal(0.0, sig)
        d_plus.append(fit_comb(ysim, sig, t, OMEGA_PLUS, centers)["dchi2"])
        d_minus.append(fit_comb(ysim, sig, t, OMEGA_MINUS, centers)["dchi2"])
    d_plus, d_minus = np.array(d_plus), np.array(d_minus)
    # LEE null (max over grid) on a 200-sim subset (cost control, frozen)
    for i in range(200):
        ysim = base + rng.normal(0.0, sig)
        d_max.append(max(fit_comb(ysim, sig, t, w, centers)["dchi2"]
                         for w in LEE_GRID))
    d_max = np.array(d_max)

    p_plus = float((np.sum(d_plus >= fit_plus["dchi2"]) + 1)
                   / (len(d_plus) + 1))
    p_minus = float((np.sum(d_minus >= fit_minus["dchi2"]) + 1)
                    / (len(d_minus) + 1))
    p_global = float((np.sum(d_max >= max(fit_plus["dchi2"],
                                          float(lee_data.max()))) + 1)
                     / (len(d_max) + 1))

    # scramble control
    perm = rng.permutation(len(y))
    scr = fit_comb(y[perm], sig[perm], t, OMEGA_PLUS, centers)

    # frozen verdict logic
    if p_minus < P_HINT:
        verdict = "dictionary_kill_flag"
    elif p_plus < P_ESCALATE and rank == 1:
        verdict = "escalation_candidate"
    elif p_plus < P_HINT:
        verdict = "hint"
    else:
        verdict = "null"

    out = {
        "experiment": "cmb-eb-logcomb",
        "prereg": {"file": "hypotheses/eb_logcomb_v1.yaml",
                   "sha16": YAML_SHA16},
        "data": {"file": DATA.name, "sha256": sha,
                 "bins": [int(ELL_MIN), int(ELL_MAX), int(DELTA_ELL)],
                 "source": "Eskilt et al. 2023 (arXiv:2303.15369), "
                           "Planck PR4/NPIPE HFI stacked EB, f_sky 0.92"},
        "frozen": {"omega_plus": OMEGA_PLUS, "omega_minus": OMEGA_MINUS,
                   "ell_star": ELL_STAR, "eps_candidate": EPS_CANDIDATE,
                   "reach_periods": round(reach, 3),
                   "reach_gate": REACH_GATE,
                   "sub_gate": reach < REACH_GATE},
        "fit_omega_plus": fit_plus, "fit_omega_minus": fit_minus,
        "A95_omega_plus": a95,
        "eps_vs_A95": (EPS_CANDIDATE / a95) if a95 == a95 else None,
        "p_omega_plus": p_plus, "p_omega_minus_control": p_minus,
        "lee": {"grid": [float(w) for w in LEE_GRID],
                "dchi2": [float(d) for d in lee_data],
                "rank_of_frozen": rank, "p_global": p_global},
        "scramble_dchi2": scr["dchi2"],
        "nulls": {"n": N_NULLS, "seed": SEED,
                  "dchi2_null_mean_plus": float(d_plus.mean()),
                  "dchi2_null_95_plus": float(np.percentile(d_plus, 95))},
        "verdict": verdict,
    }
    RESULTS.parent.mkdir(exist_ok=True)
    RESULTS.write_text(json.dumps(out, indent=2))
    return out
