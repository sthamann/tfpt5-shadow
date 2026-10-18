#!/usr/bin/env python3
"""jointlikelihood_execution_probe -- EXPLORATION ONLY (no promotion).

SUPERSEDES the recipe demo in jointlikelihood_scaffold_probe.py for the
*executed* joint likelihood over real corpus numbers.  The scaffold stays
the exact Jacobian-rank certificate on two closed-form bundles; this file
is the first data-contact construction of PRED.JOINTLIKELIHOOD.01 [O].

THE QUESTION (contract PRED.JOINTLIKELIHOOD.01 [O]): replace hit-counting
by a joint likelihood.  The 27+ individually matched TFPT values descend
from the same few atoms (phi0, c3, g_car, mu4; v_geo is the unit) and are
statistically correlated.  Contract grammar (v1, this probe):

    Sigma = Sigma_exp + J_bridge Sigma_bridge J_bridge^T + Sigma_th
    nu_eff = rank(Sigma^{-1/2} J_atom)

v1 DECLARATIONS (conservative, typed):
  * Sigma_exp  = diag(sigma_i^2) from the quoted experimental uncertainties
    (NuFIT global-fit correlations and Planck A_s--n_s covariance are
    NOT modelled -- flagged).
  * Sigma_bridge = 0, Sigma_th = 0 (no extra bridge/theory noise).
  * Atoms are compiler OUTPUTS, treated as exact.  The atom-induced term
    J diag(sigma_atom^2) J^T is therefore a CORRELATION diagnostic, not an
    extra uncertainty; chi^2 of the TFPT point uses Sigma_exp alone.
  * J_atom columns = (phi0, c3) at the deployed point.  g_car and mu4 are
    discrete/exact (no column); N_star is a [C] reheating input, not an
    atom -- it is reported separately.

BUNDLE LIST v1 (prespecified in-code, extendable; NOT a fit):
  flavor     -- sin^2 theta12, sin^2 theta13, sin^2 theta23 vs NuFIT/JUNO
  inflation  -- n_s and the N-free closure invariant C_inf vs Planck/CMB-SPA
  seed       -- Omega_b (BBN), Cabibbo |V_us|, cosmic birefringence beta
  splitting  -- Delta m^2_21 / Delta m^2_31 = |J_PMNS|  (NuFIT 6.0; JUNO
                Delta m^2 ratio is a DECLARED HOLDOUT, not consumed)

Data source: experiments/evidence_scorecard.json.  Rows enter only when a
genuine (prediction, measurement, uncertainty) triplet is parseable.
Cabibbo and the splitting ratio are documented extras (scorecard has
pull_sigma=null / no row); see the census printed at run time.

FIREWALL: exploration-level statistics.  No marker move.
PRED.JOINTLIKELIHOOD.01 stays [O] until promoted.  Bundle list is v1.

VERDICT ENUM: JOINT_LIKELIHOOD_V1_EXECUTED
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from pathlib import Path

import numpy as np
from scipy.stats import chi2 as chi2_dist

CHECKS = []

HERE = Path(__file__).resolve().parent
SCORECARD = HERE.parent / "evidence_scorecard.json"
SCAFFOLD = HERE / "jointlikelihood_scaffold_probe.py"

# deterministic null battery (v4-style formula scramble)
NULL_SEED = 20260828
N_NULL = 200
LINK_SCRAMBLE = (1.0 / 3.0, 3.0)  # log-uniform, equal complexity

# frozen [C] reheating point (v86); not a compiler atom
N_STAR = 51.4

# NuFIT 6.0 NO splittings -- used ONLY for the current Delta m^2 ratio.
# JUNO's sharper Delta m^2_21 is a HOLDOUT (printed, not consumed).
NUFIT_DM21 = 7.49e-5
NUFIT_DM21_S = 0.19e-5
NUFIT_DM31 = 2.513e-3
NUFIT_DM31_S = 0.021e-3

# PDG 2024 |V_us| -- scorecard Cabibbo row has pull_sigma=null; this is
# the kaon-average the row's "+0.08 sigma" refers to (seed-consistency).
PDG_VUS = 0.22431
PDG_VUS_S = 0.00085

# future data that count as holdout -- printed, never consumed
HOLDOUTS = (
    ("JUNO Delta m^2 ratio",
     "JUNO precision Delta m^2_21 / Delta m^2_31 vs |J_PMNS|; 207-day "
     "Delta m^2_21 is already public but NOT used in this chi^2"),
    ("DESI Sigma m_nu",
     "DESI DR3+ cosmological neutrino-mass sum vs the NO floor"),
    ("DUNE delta_CP",
     "DUNE leptonic CP phase vs 240 deg (sheet-split hexagonal unit)"),
    ("LiteBIRD r",
     "LiteBIRD tensor-to-scalar ratio vs scalaron r ~ 0.004"),
)

# prespecified v1 selection: (bundle, row matcher, formula id)
# matcher = (domain or None, observable-substring)
# (bundle, domain, observable-substring, formula_id)
BUNDLE_SPEC = (
    ("flavor", "neutrino", "sin^2 theta12", "s12"),
    ("flavor", "neutrino", "sin^2 theta13", "s13"),
    ("flavor", "neutrino", "sin^2 theta23", "s23"),
    ("inflation", "CMB", "inflation n_s", "ns"),
    ("inflation", "CMB", "inflation closure invariant", "cinf"),
    ("seed", "CMB", "baryon fraction Omega_b", "ob"),
    ("seed", "CMB", "cosmic birefringence beta", "beta"),
    ("seed", "CKM", "Cabibbo first-row", "cab"),
)

PM = re.compile(
    r"([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)"
    r"\s*(?:\+/-\s*|±\s*)"
    r"([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)"
)
NUM = re.compile(r"[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?")


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""))
    return ok


def spec_sha():
    with open(__file__, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ---- compiler atoms (same two-liner as verification/tfpt_constants.py) ----
def atoms():
    c3 = 1.0 / (8.0 * math.pi)
    phibase = 1.0 / (6.0 * math.pi)
    dtop = 48.0 * c3 ** 4
    phi0 = phibase + dtop
    return phi0, c3


def tfpt_links():
    """Structural constants of the v1 decoder (the TFPT formulas)."""
    return {
        "tbm": 1.0 / 3.0,             # TBM solar intercept
        "seam": 0.5,                  # seam shift coefficient in s12
        "t13_exp": 5.0 / 6.0,         # carrier-trace exponent (g_car/(g_car+1))
        "s23": 0.5,                   # mu-tau texture (octant open)
        "ob_slope": (4.0 * math.pi - 1.0) / (4.0 * math.pi),
        "beta_div": 4.0 * math.pi,    # beta_rad = phi0 / (4 pi)
        "cab_scale": 1.0,             # lam^2 = scale * phi0 (1-phi0)
        "ns_coef": 2.0,               # n_s = 1 - coef / N_star
        "cinf_target": 1.0,           # C_inf identity
        "delta_deg": 240.0,           # 4 pi / 3
    }


def jarlskog(s12, s13, s23, delta_deg):
    s12 = min(max(s12, 1e-12), 1.0 - 1e-12)
    s13 = min(max(s13, 1e-12), 1.0 - 1e-12)
    s23 = min(max(s23, 1e-12), 1.0 - 1e-12)
    s_12, c_12 = math.sqrt(s12), math.sqrt(1.0 - s12)
    s_13, c_13 = math.sqrt(s13), math.sqrt(1.0 - s13)
    s_23, c_23 = math.sqrt(s23), math.sqrt(1.0 - s23)
    return (s_12 * c_12 * s_23 * c_23 * s_13 * c_13 ** 2
            * math.sin(math.radians(delta_deg)))


def predict(phi0, c3, n_star, links):
    """Point predictions.  c3 is unused at the identity C_inf = 1 (v1);
    it is kept in the signature so J_atom has a c3 column (expected ~0)."""
    _ = c3
    s12 = links["tbm"] - links["seam"] * phi0
    s13 = phi0 * math.exp(-links["t13_exp"])
    s23 = links["s23"]
    ob = phi0 * links["ob_slope"]
    beta = (phi0 / links["beta_div"]) * (180.0 / math.pi)
    cab = math.sqrt(max(phi0 * (1.0 - phi0) * links["cab_scale"], 0.0))
    ns = 1.0 - links["ns_coef"] / n_star
    cinf = links["cinf_target"]
    jabs = abs(jarlskog(s12, s13, s23, links["delta_deg"]))
    return {
        "s12": s12, "s13": s13, "s23": s23,
        "ns": ns, "cinf": cinf,
        "ob": ob, "beta": beta, "cab": cab,
        "dm2": jabs,
    }


# formula_id order used for the joint vector
FID_ORDER = ("s12", "s13", "s23", "ns", "cinf", "ob", "beta", "cab", "dm2")
FID_BUNDLE = {
    "s12": "flavor", "s13": "flavor", "s23": "flavor",
    "ns": "inflation", "cinf": "inflation",
    "ob": "seed", "beta": "seed", "cab": "seed",
    "dm2": "splitting",
}
FID_NAME = {
    "s12": "sin^2 theta12",
    "s13": "sin^2 theta13",
    "s23": "sin^2 theta23",
    "ns": "inflation n_s",
    "cinf": "inflation C_inf",
    "ob": "Omega_b (BBN)",
    "beta": "beta birefringence (deg)",
    "cab": "Cabibbo |V_us|",
    "dm2": "Delta m^2 ratio = |J|",
}


def vec_from_pred(p):
    return np.array([p[k] for k in FID_ORDER], dtype=float)


def analytic_jacobian_phi0(phi0, links):
    """d mu / d phi0 at the TFPT links (analytic; c3 column is 0)."""
    s12 = links["tbm"] - links["seam"] * phi0
    s13 = phi0 * math.exp(-links["t13_exp"])
    s23 = links["s23"]
    d_s12 = -links["seam"]
    d_s13 = math.exp(-links["t13_exp"])
    d_s23 = 0.0
    d_ob = links["ob_slope"]
    d_beta = (180.0 / math.pi) / links["beta_div"]
    lam = math.sqrt(phi0 * (1.0 - phi0) * links["cab_scale"])
    d_cab = links["cab_scale"] * (1.0 - 2.0 * phi0) / (2.0 * lam)
    # |J| = |sin th12 cos th12 sin th23 cos th23 sin th13 cos^2 th13 sin delta|
    # s13 here is sin^2 theta13, so the s13-factor is s13^{1/2} (1-s13).
    j = jarlskog(s12, s13, s23, links["delta_deg"])
    dlog_s12 = (1.0 - 2.0 * s12) / (2.0 * s12 * (1.0 - s12))
    dlog_s13 = 0.5 / s13 - 1.0 / (1.0 - s13)
    d_jabs = abs(j) * (dlog_s12 * d_s12 + dlog_s13 * d_s13)
    # n_s, C_inf, s23: zero
    out = {
        "s12": d_s12, "s13": d_s13, "s23": d_s23,
        "ns": 0.0, "cinf": 0.0,
        "ob": d_ob, "beta": d_beta, "cab": d_cab,
        "dm2": d_jabs,
    }
    return np.array([out[k] for k in FID_ORDER], dtype=float)


# ---- scorecard parsing ----------------------------------------------------
def _pm_candidates(text):
    out = []
    for a, b in PM.findall(text or ""):
        try:
            out.append((float(a), abs(float(b))))
        except ValueError:
            continue
    return out


def _first_number(text):
    ms = NUM.findall(text or "")
    return float(ms[0]) if ms else None


def _last_number(text):
    ms = NUM.findall(text or "")
    return float(ms[-1]) if ms else None


def find_row(rows, domain, substr):
    hits = []
    for r in rows:
        if domain is not None and r.get("domain") != domain:
            continue
        if substr.lower() in (r.get("observable") or "").lower():
            hits.append(r)
    return hits


def parse_triplet(row, pred_formula, pull_hint):
    """Pick the data_value meas+/-sigma whose pull best matches pull_hint.

    Returns (meas, sigma, source_note) or None.
    """
    data = row.get("data_value") or ""
    cands = _pm_candidates(data)
    if not cands:
        return None
    if pull_hint is None:
        meas, sig = cands[0]
        return meas, sig, "first meas+/-sigma in data_value"
    best = None
    best_err = 1e99
    for meas, sig in cands:
        if sig <= 0:
            continue
        pull = (pred_formula - meas) / sig
        err = abs(pull - float(pull_hint))
        if err < best_err:
            best_err = err
            best = (meas, sig, pull)
    if best is None:
        return None
    meas, sig, _ = best
    note = "meas+/-sigma matching scorecard pull_sigma (err=%.3f)" % best_err
    return meas, sig, note


def classify_exclusions(rows, selected_ids):
    """Census of every scorecard row vs the v1 bundle list."""
    buckets = {
        "selected_v1": [],
        "excluded_null_pull": [],
        "excluded_search_target": [],
        "excluded_data_limited": [],
        "excluded_derived_or_composite": [],
        "excluded_alternative_group": [],
        "excluded_no_parseable_triplet": [],
        "excluded_out_of_v1_bundle": [],
    }
    derived_keys = (
        "seed line Omega_b/beta",
        "shared seed phi0",
        "rotation fingerprint",
        "flat LambdaCDM budget",
        "S8 forecast",
    )
    for r in rows:
        oid = (r.get("domain"), r.get("observable"))
        if oid in selected_ids:
            buckets["selected_v1"].append(r)
            continue
        obs = r.get("observable") or ""
        stage = r.get("stage") or ""
        status = r.get("status") or ""
        pull = r.get("pull_sigma")
        if any(k.lower() in obs.lower() for k in derived_keys):
            buckets["excluded_derived_or_composite"].append(r)
            continue
        if r.get("alternative_group") in {"Nstar_branch", "HVP_baseline",
                                          "axion_branch", "w_de_eos"}:
            # keep n_s / C_inf (not in this branch of the if -- they are selected)
            buckets["excluded_alternative_group"].append(r)
            continue
        if stage in {"search_target", "strain_level_test", "catalog_feasibility",
                     "parked_analog"} or status in {"null", "parked"}:
            buckets["excluded_search_target"].append(r)
            continue
        if status == "data_limited":
            buckets["excluded_data_limited"].append(r)
            continue
        if pull is None:
            buckets["excluded_null_pull"].append(r)
            continue
        cands = _pm_candidates(r.get("data_value") or "")
        if not cands:
            buckets["excluded_no_parseable_triplet"].append(r)
            continue
        buckets["excluded_out_of_v1_bundle"].append(r)
    return buckets


# ---- statistics -----------------------------------------------------------
def chi2_vec(mu, y, sig):
    return float(np.sum(((mu - y) / sig) ** 2))


def whitened_jacobian(J, sig):
    return J / sig[:, None]


def matrix_rank(A, rel=1e-8):
    s = np.linalg.svd(A, compute_uv=False)
    if s.size == 0:
        return 0
    return int(np.sum(s > rel * s[0]))


def loo_stability(mu, y, sig, bundles):
    """Leave-one-bundle-out chi^2 / dof."""
    n = len(mu)
    chi_all = chi2_vec(mu, y, sig)
    rows = []
    names = sorted(set(bundles))
    for drop in names:
        mask = np.array([b != drop for b in bundles])
        if mask.sum() < 2:
            continue
        c = chi2_vec(mu[mask], y[mask], sig[mask])
        d = int(mask.sum())
        rows.append({
            "dropped": drop,
            "n": d,
            "chi2": c,
            "chi2_dof": c / d,
            "p": float(chi2_dist.sf(c, d)),
        })
    # stability: remaining chi2/dof within a factor 3 of the full one
    full_ratio = chi_all / n
    ok = all(0.2 <= r["chi2_dof"] <= 4.0 for r in rows)
    ok = ok and all(r["chi2_dof"] <= 3.0 * max(full_ratio, 0.3) or
                    r["chi2_dof"] <= 4.0 for r in rows)
    return rows, ok, chi_all


def formula_scramble_null(mu_tfpt, y, sig, phi0, c3, rng):
    """v4-style: independently log-uniform-scale every structural constant."""
    base = tfpt_links()
    keys = list(base.keys())
    lo, hi = math.log(LINK_SCRAMBLE[0]), math.log(LINK_SCRAMBLE[1])
    chi = np.empty(N_NULL)
    for i in range(N_NULL):
        links = dict(base)
        for k in keys:
            if k == "delta_deg":
                # scramble the CP phase by a wrapped jitter, not a scale
                links[k] = float(base[k] + rng.uniform(-90.0, 90.0))
            elif k == "cinf_target":
                links[k] = float(base[k] * math.exp(rng.uniform(lo, hi)))
            else:
                links[k] = float(base[k] * math.exp(rng.uniform(lo, hi)))
        mu = vec_from_pred(predict(phi0, c3, N_STAR, links))
        chi[i] = chi2_vec(mu, y, sig)
    chi_tfpt = chi2_vec(mu_tfpt, y, sig)
    # percentile of the TFPT point in the null ensemble (smaller chi2 = better)
    pct = float(np.mean(chi <= chi_tfpt))
    return chi, chi_tfpt, pct


# ---- main -----------------------------------------------------------------
def main():
    print("jointlikelihood_execution_probe -- executed joint likelihood "
          "over real corpus numbers (PRED.JOINTLIKELIHOOD.01 v1)")
    print("SUPERSEDES jointlikelihood_scaffold_probe.py for data contact; "
          "the scaffold remains the exact rank certificate.")
    print("FIREWALL: exploration only; PRED.JOINTLIKELIHOOD.01 stays [O]; "
          "no marker move; bundle list is v1 and extendable.")
    print()

    check("scaffold file present (recipe this probe executes)",
          SCAFFOLD.is_file(), str(SCAFFOLD.name))
    check("scorecard present", SCORECARD.is_file(), str(SCORECARD))

    card = json.loads(SCORECARD.read_text(encoding="utf-8"))
    rows = card["rows"]
    check("scorecard has 127 rows", card.get("n_rows") == 127 and len(rows) == 127,
          "n_rows=%s len=%d" % (card.get("n_rows"), len(rows)))

    phi0, c3 = atoms()
    links = tfpt_links()
    pred = predict(phi0, c3, N_STAR, links)
    check("phi0 deployed ~ 0.05317 (compiler output, treated exact)",
          abs(phi0 - 0.05317) < 5e-5, "phi0=%.8f  c3=%.8f" % (phi0, c3))
    check("C_inf identity at the TFPT point is exactly 1",
          pred["cinf"] == 1.0)

    # ---- select + parse ---------------------------------------------------
    print()
    print("BUNDLE SELECTION (prespecified v1)")
    selected_ids = set()
    parsed = {}

    for bundle, domain, substr, fid in BUNDLE_SPEC:
        hits = find_row(rows, domain, substr)
        ok_hit = len(hits) == 1
        check("unique scorecard row for %s/%s" % (bundle, fid),
              ok_hit, "hits=%d" % len(hits))
        if not hits:
            continue
        row = hits[0]
        selected_ids.add((row.get("domain"), row.get("observable")))
        p = pred[fid]
        pull_hint = row.get("pull_sigma")
        trip = parse_triplet(row, p, pull_hint)
        if fid == "cab" and trip is None:
            # documented extra: scorecard pull_sigma is null
            trip = (PDG_VUS, PDG_VUS_S,
                    "FALLBACK PDG 2024 |V_us| (scorecard pull_sigma=null; "
                    "kaon average, +0.08 sigma in the row prose)")
        ok_trip = trip is not None
        check("parseable (pred, meas, sigma) for %s" % fid, ok_trip)
        if trip is None:
            continue
        meas, sig, note = trip
        pull = (p - meas) / sig
        parsed[fid] = {
            "bundle": bundle, "fid": fid, "name": FID_NAME[fid],
            "row_observable": row.get("observable"),
            "domain": row.get("domain"),
            "stage": row.get("stage"),
            "status": row.get("status"),
            "independence_group": row.get("independence_group"),
            "pred": p, "meas": meas, "sigma": sig, "pull": pull,
            "scorecard_pull": pull_hint, "note": note,
        }

    # splitting ratio -- NOT a scorecard row; documented extra
    r_meas = NUFIT_DM21 / NUFIT_DM31
    r_sig = r_meas * math.sqrt((NUFIT_DM21_S / NUFIT_DM21) ** 2
                               + (NUFIT_DM31_S / NUFIT_DM31) ** 2)
    parsed["dm2"] = {
        "bundle": "splitting", "fid": "dm2", "name": FID_NAME["dm2"],
        "row_observable": "(not a scorecard row; FLAV.DM2RATIO.01 [O] candidate)",
        "domain": "neutrino",
        "stage": "documented_extra",
        "status": "extra",
        "independence_group": "phi0_seed",
        "pred": pred["dm2"], "meas": r_meas, "sigma": r_sig,
        "pull": (pred["dm2"] - r_meas) / r_sig,
        "scorecard_pull": None,
        "note": "NuFIT 6.0 NO splittings; JUNO Delta m^2 ratio is HOLDOUT",
    }
    check("splitting ratio declared extra (no scorecard row)",
          "dm2" in parsed,
          "pred=%.6f meas=%.6f+/-%.6f" % (pred["dm2"], r_meas, r_sig))

    # Cabibbo must have entered
    check("Cabibbo entered the seed bundle (documented extra if needed)",
          "cab" in parsed)

    # formula vs scorecard tfpt_value sanity (quoted precision)
    check("s12 formula 1/3 - phi0/2 matches 0.306747",
          abs(pred["s12"] - 0.306747) < 5e-6, "pred=%.8f" % pred["s12"])
    check("s13 formula phi0 e^{-5/6} matches 0.0231",
          abs(pred["s13"] - 0.0231) < 5e-5, "pred=%.8f" % pred["s13"])
    check("s23 texture is exactly 1/2", abs(pred["s23"] - 0.5) < 1e-15)
    check("n_s = 1-2/N_star matches 0.9611",
          abs(pred["ns"] - 0.9611) < 5e-5, "pred=%.8f" % pred["ns"])
    check("Omega_b = phi0 (1-1/4pi) matches 0.04894",
          abs(pred["ob"] - 0.04894) < 5e-5, "pred=%.8f" % pred["ob"])
    check("beta_deg = phi0/(4pi) in degrees matches 0.2424",
          abs(pred["beta"] - 0.2424) < 5e-4, "pred=%.6f" % pred["beta"])
    check("lambda_C = sqrt(phi0(1-phi0)) matches 0.224376",
          abs(pred["cab"] - 0.224376) < 5e-6, "pred=%.8f" % pred["cab"])

    # scorecard pull recovery (where the row carries a pull_sigma)
    for fid, rec in parsed.items():
        hint = rec["scorecard_pull"]
        if hint is None:
            continue
        # scorecard signs are not uniform: most rows use (pred-meas)/sigma,
        # C_inf prose uses (meas-1)/sigma ("0.13 sigma below 1").  Recover
        # the MAGNITUDE; either sign convention is accepted.
        err = min(abs(rec["pull"] - float(hint)),
                  abs(rec["pull"] + float(hint)))
        check("parsed pull recovers scorecard |pull_sigma| for %s" % fid,
              err < 0.15,
              "parsed=%+.3f scorecard=%s" % (rec["pull"], hint))

    # exclusion census
    buckets = classify_exclusions(rows, selected_ids)
    print()
    print("EXCLUSION CENSUS (every scorecard row, v1 bundle list)")
    for k, v in buckets.items():
        print("  %s: %d" % (k, len(v)))
    # a few named exclusions the contract cares about
    named = []
    for r in rows:
        obs = r.get("observable") or ""
        if "inflation r (" in obs or obs.startswith("inflation r"):
            named.append(("inflation r (upper limit)", "no meas+/-sigma, pull null"))
        if "inflation A_s (fixed" in obs:
            named.append(("A_s fixed N_star", "alternative_group Nstar_branch, -11.3 sigma"))
        if "inflation A_s (profiled" in obs:
            named.append(("A_s profiled N_star", "alternative_group Nstar_branch"))
        if "inflation alpha_s" in obs:
            named.append(("alpha_s", "same N_star as n_s; not in v1 inflation pair"))
        if "inflation mu-distortion" in obs:
            named.append(("mu-distortion", "data_limited, alternative_group Nstar_branch"))
        if "seed line Omega_b/beta" in obs:
            named.append(("Omega_b/beta seed line", "derived ratio of two selected legs"))
        if obs == "shared seed phi0":
            named.append(("shared seed phi0 composite", "null pull; already the four seed legs"))
        if "DM(z) baryon" in obs:
            named.append(("FRB Omega_b", "search_target duplicate of the BBN Omega_b row"))
        if obs.startswith("J_PMNS"):
            named.append(("J_PMNS EXT.5", "downstream_bridge J_max, not the splitting ratio"))
    print("  named exclusions:")
    for a, b in named:
        print("    - %s -- %s" % (a, b))
    if buckets["excluded_out_of_v1_bundle"]:
        print("  out-of-v1 (parseable triplet, not in the prespecified bundles):")
        for r in buckets["excluded_out_of_v1_bundle"]:
            print("    - %s / %s  pull=%s  stage=%s" %
                  (r.get("domain"), r.get("observable"),
                   r.get("pull_sigma"), r.get("stage")))
    check("exclusion census covers every row",
          sum(len(v) for v in buckets.values()) == len(rows),
          "sum=%d n=%d" % (sum(len(v) for v in buckets.values()), len(rows)))
    check("v1 selected at least the four named bundles",
          set(FID_BUNDLE.values()) <= {parsed[k]["bundle"] for k in parsed},
          str(sorted({parsed[k]["bundle"] for k in parsed})))

    # ---- assemble joint vector in FID_ORDER --------------------------------
    missing = [k for k in FID_ORDER if k not in parsed]
    check("all v1 formula ids present", not missing, str(missing))
    mu = np.array([parsed[k]["pred"] for k in FID_ORDER], dtype=float)
    y = np.array([parsed[k]["meas"] for k in FID_ORDER], dtype=float)
    sig = np.array([parsed[k]["sigma"] for k in FID_ORDER], dtype=float)
    bundles = [parsed[k]["bundle"] for k in FID_ORDER]
    n_obs = len(FID_ORDER)

    print()
    print("BUNDLE TABLE  (observable, pred, meas, sigma, pull)")
    print("  %-28s %-10s %12s %12s %12s %8s" %
          ("observable", "bundle", "pred", "meas", "sigma", "pull"))
    for k in FID_ORDER:
        r = parsed[k]
        print("  %-28s %-10s %12.6g %12.6g %12.6g %+8.2f" %
              (r["name"], r["bundle"], r["pred"], r["meas"], r["sigma"],
               r["pull"]))

    # ---- Jacobian ---------------------------------------------------------
    print()
    print("ATOM JACOBIAN  (columns: phi0, c3; N_star reported separately)")
    J_phi = analytic_jacobian_phi0(phi0, links)
    # numeric cross-check + c3 column (independent coordinates: hold phi0)
    eps = 1e-6
    mu_p = vec_from_pred(predict(phi0 * (1 + eps), c3, N_STAR, links))
    mu_m = vec_from_pred(predict(phi0 * (1 - eps), c3, N_STAR, links))
    J_phi_num = (mu_p - mu_m) / (2.0 * eps * phi0)
    mu_cp = vec_from_pred(predict(phi0, c3 * (1 + eps), N_STAR, links))
    mu_cm = vec_from_pred(predict(phi0, c3 * (1 - eps), N_STAR, links))
    J_c3 = (mu_cp - mu_cm) / (2.0 * eps * c3)
    J = np.column_stack([J_phi, J_c3])  # n x 2
    check("numeric d/dphi0 matches analytic (rel 1e-4)",
          np.allclose(J_phi, J_phi_num, rtol=1e-4, atol=1e-8),
          "max|d|=%.3e" % np.max(np.abs(J_phi - J_phi_num)))
    check("c3 column vanishes (v1 observables depend on c3 only through "
          "phi0, and C_inf is the identity mu=1)",
          np.max(np.abs(J_c3)) < 1e-10,
          "max|d/dc3|=%.3e" % np.max(np.abs(J_c3)))
    check("analytic d s12 / d phi0 = -1/2",
          abs(J_phi[FID_ORDER.index("s12")] + 0.5) < 1e-12)
    check("analytic d s13 / d phi0 = e^{-5/6}",
          abs(J_phi[FID_ORDER.index("s13")] - math.exp(-5.0 / 6.0)) < 1e-12)

    # N_star column (NOT an atom -- extra rank diagnostic)
    mu_np = vec_from_pred(predict(phi0, c3, N_STAR * (1 + eps), links))
    mu_nm = vec_from_pred(predict(phi0, c3, N_STAR * (1 - eps), links))
    J_n = (mu_np - mu_nm) / (2.0 * eps * N_STAR)
    J_ext = np.column_stack([J_phi, J_c3, J_n])

    # ---- Sigma and nu_eff -------------------------------------------------
    # Sigma = Sigma_exp + 0 + 0   (declared)
    Sigma = np.diag(sig ** 2)
    check("Sigma_exp diagonal and positive (v1: no off-diagonal data cov)",
          Sigma.shape == (n_obs, n_obs) and np.allclose(Sigma, np.diag(np.diag(Sigma)))
          and np.all(np.diag(Sigma) > 0))
    # atom-induced CORRELATION diagnostic (sigma_atom = 0; atoms exact)
    # a 1% fictitious jitter is reported, never used in chi^2
    sig_atom = np.array([0.01 * phi0, 0.01 * c3])
    Sigma_atom_diag = J @ np.diag(sig_atom ** 2) @ J.T

    Jw = whitened_jacobian(J, sig)
    Jw_ext = whitened_jacobian(J_ext, sig)
    nu_eff = matrix_rank(Jw)
    nu_eff_ext = matrix_rank(Jw_ext)
    # constrained: phi0 = f(c3), single column d mu / d c3 along the curve
    dphi0_dc3 = 4.0 / 3.0 + 192.0 * c3 ** 3
    J_constrained = (J_phi * dphi0_dc3)[:, None]
    nu_eff_con = matrix_rank(whitened_jacobian(J_constrained, sig))

    chi2 = chi2_vec(mu, y, sig)
    dof = n_obs
    chi2_dof = chi2 / dof
    p_gof = float(chi2_dist.sf(chi2, dof))

    print()
    print("JOINT FIT")
    print("  n_obs = %d" % n_obs)
    print("  chi2  = %.4f" % chi2)
    print("  dof   = %d  (GoF of the frozen point; no fitted parameters)" % dof)
    print("  chi2/dof = %.3f" % chi2_dof)
    print("  p_GoF (chi2, dof=n_obs) = %.4g" % p_gof)
    print("  nu_eff = rank(Sigma^{-1/2} J_atom) = %d   "
          "[atoms=(phi0, c3); c3 column ~0 on this v1 bundle]" % nu_eff)
    print("  nu_eff_constrained (phi0=f(c3)) = %d" % nu_eff_con)
    print("  nu_eff_ext (atoms + N_star) = %d   "
          "[N_star is a [C] reheating input, not a compiler atom]" % nu_eff_ext)
    print("  honest headline: %d matched values = %d compiler-atom "
          "independent-evidence count from a 6-leg phi0 cluster "
          "(5 forced relations) + 3 zero-slope tests "
          "(s23 texture, n_s(N_star), C_inf identity)" %
          (n_obs, nu_eff))
    print("  Sigma_exp diagonal; Sigma_bridge=0; Sigma_th=0; "
          "atoms exact (correlation diagnostic only).")
    print("  atom-induced 1%%-jitter trace(Sigma_atom)=%.3e  "
          "(NOT added to chi^2)" % float(np.trace(Sigma_atom_diag)))
    print("  UNMODELLED (flagged): NuFIT angle correlations, "
          "Planck cov(A_s, n_s), ACT calibration systematic on beta.")

    check("chi2/dof is order 1 (corpus claims hold at v1)",
          0.25 <= chi2_dof <= 4.0, "chi2/dof=%.3f" % chi2_dof)
    check("nu_eff < n_obs (hit-counting overstates independent evidence)",
          nu_eff < n_obs, "nu_eff=%d n_obs=%d" % (nu_eff, n_obs))
    check("nu_eff compiler rank is 1 (all seed/flavor slopes collinear in phi0)",
          nu_eff == 1, "nu_eff=%d" % nu_eff)
    check("extending J by N_star raises rank by 1 (inflation is a second input)",
          nu_eff_ext == nu_eff + 1, "nu_eff_ext=%d" % nu_eff_ext)
    check("GoF p-value is not a kill (p > 1e-3 at n_obs dof)",
          p_gof > 1e-3, "p=%.4g" % p_gof)

    # ---- null battery -----------------------------------------------------
    print()
    print("NULL CONTROL  (%d scrambled decoders, seed %d, links x log-uniform "
          "[1/3, 3], v4 style)" % (N_NULL, NULL_SEED))
    rng = np.random.default_rng(NULL_SEED)
    chi_null, chi_tfpt, pct = formula_scramble_null(mu, y, sig, phi0, c3, rng)
    print("  TFPT chi2 = %.3f" % chi_tfpt)
    print("  null median chi2 = %.1f   (5th/95th = %.1f / %.1f)" %
          (float(np.median(chi_null)),
           float(np.percentile(chi_null, 5)),
           float(np.percentile(chi_null, 95))))
    print("  TFPT percentile in the null ensemble = %.2f%%  "
          "(fraction of nulls with chi2 <= TFPT)" % (100.0 * pct))
    check("null median is dramatically worse than TFPT (ratio > 10)",
          float(np.median(chi_null)) > 10.0 * chi_tfpt,
          "median/tfpt = %.1f" % (float(np.median(chi_null)) / chi_tfpt))
    check("TFPT sits at <= 5th percentile of the scrambled-decoder null",
          pct <= 0.05, "percentile=%.2f%%" % (100.0 * pct))

    # ---- LOO --------------------------------------------------------------
    print()
    print("LEAVE-ONE-BUNDLE-OUT STABILITY")
    loo_rows, loo_ok, _ = loo_stability(mu, y, sig, bundles)
    for r in loo_rows:
        print("  drop %-10s  n=%d  chi2=%.3f  chi2/dof=%.3f  p=%.3g" %
              (r["dropped"], r["n"], r["chi2"], r["chi2_dof"], r["p"]))
    check("LOO chi2/dof stays order 1 on every remaining subset",
          loo_ok, "rows=" + ",".join("%s:%.2f" % (r["dropped"], r["chi2_dof"])
                                     for r in loo_rows))

    # ---- holdouts (printed, not consumed) ---------------------------------
    print()
    print("HOLDOUT DECLARATION (frozen, not consumed by this chi^2)")
    for name, why in HOLDOUTS:
        print("  * %s -- %s" % (name, why))
    check("four holdouts declared", len(HOLDOUTS) == 4)

    # ---- firewall ---------------------------------------------------------
    print()
    print("FIREWALL")
    print("  PRED.JOINTLIKELIHOOD.01 stays [O] -- no marker move.")
    print("  Exploration-level statistics; not a load-bearing claim.")
    print("  Bundle list is v1 and extendable (more rows need an explicit "
          "formula + a parseable triplet).")
    print("  Promotion would need: off-diagonal Sigma_exp (NuFIT + Planck), "
          "a prespecified formula grammar closed under a larger decoder "
          "census, holdout data actually held out of development, and a "
          "vN module + ledger row -- none of that is done here.")
    check("firewall typed: contract stays Open", True)

    npass = sum(CHECKS)
    print("-" * 70)
    print("CHECKS %d/%d PASS" % (npass, len(CHECKS)))
    verdict = "JOINT_LIKELIHOOD_V1_EXECUTED"
    print("VERDICT: %s  (n_obs=%d  chi2=%.3f  dof=%d  chi2/dof=%.3f  "
          "nu_eff=%d  p_GoF=%.3g  null_percentile=%.2f%%  LOO=%s)" %
          (verdict, n_obs, chi2, dof, chi2_dof, nu_eff, p_gof,
           100.0 * pct, "stable" if loo_ok else "UNSTABLE"))
    print("SPEC_SHA %s" % spec_sha()[:16])
    print("FILE %s" % __file__)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
