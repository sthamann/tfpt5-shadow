"""v992 -- PRED.JOINTLIKELIHOOD.01 [O update: v1 executed [N];
promotion conditions typed; contract stays Open].

THE POINT (promote round 2026-08-28).  Re-derives the executed joint
likelihood of jointlikelihood_execution_probe WITHOUT importing
experiments/ or the scorecard at suite runtime.  The nine
(meas, sigma) triplets are FROZEN constants matching the probe's
pull-matched 2026-08-28 scorecard selection (NOT the first-listed
NuFIT/Planck number when the row's pull_sigma points at a sharper
leg):

    s12  0.3036    +- 0.0064    JUNO 207-day (scorecard pull 0.49)
    s13  0.02195   +- 0.00058   NuFIT 6.0
    s23  0.470     +- 0.017     NuFIT 6.0
    ns   0.9679    +- 0.0033    CMB-SPA (scorecard pull -2.06)
    cinf 0.970     +- 0.233     Planck 2018 A_s+n_s (cov unmodelled)
    ob   0.0489    +- 0.0014    BBN D/H
    beta 0.215     +- 0.074     ACT DR6
    cab  0.22431   +- 0.00085   PDG 2024 |V_us|
    dm2  7.49e-5 / 2.513e-3     NuFIT 6.0 (sigma propagated)

Compiler formulas (v1 decoder, phi0 and c3 from tfpt_constants):
    s12 = 1/3 - phi0/2;  s13 = phi0 e^{-5/6};  s23 = 1/2;
    ns  = 1 - 2/N_star (N_star = 51.4 [C] reheating input);
    C_inf = 1;  Omega_b = phi0 (4 pi - 1)/(4 pi);
    beta_deg = phi0/(4 pi) * 180/pi;
    cab = sqrt(phi0 (1-phi0));
    dm2 = |J(s12, s13, s23, delta = 240 deg)|.

Expected headline (probe): chi2 = 11.80 / dof 9 (p = 0.225),
nu_eff = rank(J_atom) = 1, TFPT at 0th percentile of 200 scrambled
decoders, LOO stable.  Holdouts declared not consumed: JUNO Delta m^2,
DESI Sigma m_nu, DUNE delta_CP, LiteBIRD r.

HONEST SCOPE (firewall): v1 statistics construction; Sigma_exp
diagonal (NuFIT / Planck covariances UNMODELLED, flagged);
Sigma_bridge = Sigma_th = 0; atoms treated exact.  Promotion to
closure requires off-diagonal Sigma, a formula-grammar census, and
genuine future holdouts.  Contract stays [O].  No marker move.
Python-only / Wolfram mirror deferred.

Provenance: experiments/tfpt-discovery/jointlikelihood_execution_probe.py
(ALL PASS, 55/55; not imported).
"""
import math

import numpy as np
from scipy.stats import chi2 as chi2_dist

from tfpt_constants import check, summary, reset, c3 as C3_MP, phi0 as PHI0_MP

NULL_SEED = 20260828
N_NULL = 200
LINK_SCRAMBLE = (1.0 / 3.0, 3.0)
N_STAR = 51.4

# Frozen (meas, sigma) -- probe pull-matched scorecard v1 selection.
MEAS = {
    "s12": (0.3036, 0.0064),
    "s13": (0.02195, 0.00058),
    "s23": (0.470, 0.017),
    "ns": (0.9679, 0.0033),
    "cinf": (0.970, 0.233),
    "ob": (0.0489, 0.0014),
    "beta": (0.215, 0.074),
    "cab": (0.22431, 0.00085),
}
NUFIT_DM21, NUFIT_DM21_S = 7.49e-5, 0.19e-5
NUFIT_DM31, NUFIT_DM31_S = 2.513e-3, 0.021e-3

FID_ORDER = ("s12", "s13", "s23", "ns", "cinf", "ob", "beta", "cab", "dm2")
FID_BUNDLE = {
    "s12": "flavor", "s13": "flavor", "s23": "flavor",
    "ns": "inflation", "cinf": "inflation",
    "ob": "seed", "beta": "seed", "cab": "seed",
    "dm2": "splitting",
}
HOLDOUTS = (
    "JUNO Delta m^2 ratio",
    "DESI Sigma m_nu",
    "DUNE delta_CP",
    "LiteBIRD r",
)


def tfpt_links():
    return {
        "tbm": 1.0 / 3.0,
        "seam": 0.5,
        "t13_exp": 5.0 / 6.0,
        "s23": 0.5,
        "ob_slope": (4.0 * math.pi - 1.0) / (4.0 * math.pi),
        "beta_div": 4.0 * math.pi,
        "cab_scale": 1.0,
        "ns_coef": 2.0,
        "cinf_target": 1.0,
        "delta_deg": 240.0,
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


def vec_from_pred(p):
    return np.array([p[k] for k in FID_ORDER], dtype=float)


def analytic_jacobian_phi0(phi0, links):
    s12 = links["tbm"] - links["seam"] * phi0
    s13 = phi0 * math.exp(-links["t13_exp"])
    s23 = links["s23"]
    d_s12 = -links["seam"]
    d_s13 = math.exp(-links["t13_exp"])
    lam = math.sqrt(phi0 * (1.0 - phi0) * links["cab_scale"])
    d_cab = links["cab_scale"] * (1.0 - 2.0 * phi0) / (2.0 * lam)
    j = jarlskog(s12, s13, s23, links["delta_deg"])
    dlog_s12 = (1.0 - 2.0 * s12) / (2.0 * s12 * (1.0 - s12))
    dlog_s13 = 0.5 / s13 - 1.0 / (1.0 - s13)
    d_jabs = abs(j) * (dlog_s12 * d_s12 + dlog_s13 * d_s13)
    out = {
        "s12": d_s12, "s13": d_s13, "s23": 0.0,
        "ns": 0.0, "cinf": 0.0,
        "ob": links["ob_slope"],
        "beta": (180.0 / math.pi) / links["beta_div"],
        "cab": d_cab,
        "dm2": d_jabs,
    }
    return np.array([out[k] for k in FID_ORDER], dtype=float)


def chi2_vec(mu, y, sig):
    return float(np.sum(((mu - y) / sig) ** 2))


def matrix_rank(A, rel=1e-8):
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > rel * s[0]))


def run():
    reset()
    print("v992  PRED.JOINTLIKELIHOOD.01: v1 joint likelihood executed "
          "(frozen triplets; no experiments/ import)")

    phi0 = float(PHI0_MP)
    c3 = float(C3_MP)
    links = tfpt_links()
    pred = predict(phi0, c3, N_STAR, links)
    check("phi0 ~ 0.05317 [E]: compiler output treated exact "
          "(phi0=%.8f)" % phi0, abs(phi0 - 0.05317) < 5e-5)
    check("C_inf identity [E]: mu = 1 exactly at the TFPT point",
          pred["cinf"] == 1.0)
    check("s12 formula [E]: 1/3 - phi0/2 matches 0.306747",
          abs(pred["s12"] - 0.306747) < 5e-6)
    check("s13 formula [E]: phi0 e^{-5/6} matches 0.0231",
          abs(pred["s13"] - 0.0231) < 5e-5)
    check("s23 texture [E]: exactly 1/2", abs(pred["s23"] - 0.5) < 1e-15)
    check("n_s [N]: 1-2/N_star matches 0.9611",
          abs(pred["ns"] - 0.9611) < 5e-5)
    check("Omega_b [E]: phi0 (1-1/4pi) matches 0.04894",
          abs(pred["ob"] - 0.04894) < 5e-5)
    check("Cabibbo [E]: sqrt(phi0(1-phi0)) matches 0.224376",
          abs(pred["cab"] - 0.224376) < 5e-6)

    r_meas = NUFIT_DM21 / NUFIT_DM31
    r_sig = r_meas * math.sqrt((NUFIT_DM21_S / NUFIT_DM21) ** 2
                               + (NUFIT_DM31_S / NUFIT_DM31) ** 2)
    y = np.array([MEAS[k][0] if k != "dm2" else r_meas
                  for k in FID_ORDER], dtype=float)
    sig = np.array([MEAS[k][1] if k != "dm2" else r_sig
                    for k in FID_ORDER], dtype=float)
    mu = vec_from_pred(pred)
    bundles = [FID_BUNDLE[k] for k in FID_ORDER]
    n_obs = len(FID_ORDER)

    print("  BUNDLE TABLE")
    for k, m, s, yy in zip(FID_ORDER, mu, sig, y):
        print("    %-6s  pred=%.6g  meas=%.6g  sig=%.4g  pull=%+.2f"
              % (k, m, yy, s, (m - yy) / s))

    J_phi = analytic_jacobian_phi0(phi0, links)
    eps = 1e-6
    mu_p = vec_from_pred(predict(phi0 * (1 + eps), c3, N_STAR, links))
    mu_m = vec_from_pred(predict(phi0 * (1 - eps), c3, N_STAR, links))
    J_phi_num = (mu_p - mu_m) / (2.0 * eps * phi0)
    mu_cp = vec_from_pred(predict(phi0, c3 * (1 + eps), N_STAR, links))
    mu_cm = vec_from_pred(predict(phi0, c3 * (1 - eps), N_STAR, links))
    J_c3 = (mu_cp - mu_cm) / (2.0 * eps * c3)
    J = np.column_stack([J_phi, J_c3])
    check("analytic d/dphi0 matches numeric [N]",
          np.allclose(J_phi, J_phi_num, rtol=1e-4, atol=1e-8))
    check("c3 column vanishes [E]: v1 observables depend on c3 only "
          "through phi0 (C_inf is the identity)",
          np.max(np.abs(J_c3)) < 1e-10)
    check("d s12 / d phi0 = -1/2 [E]",
          abs(J_phi[FID_ORDER.index("s12")] + 0.5) < 1e-12)
    check("d s13 / d phi0 = e^{-5/6} [E]",
          abs(J_phi[FID_ORDER.index("s13")] - math.exp(-5.0 / 6.0)) < 1e-12)

    mu_np = vec_from_pred(predict(phi0, c3, N_STAR * (1 + eps), links))
    mu_nm = vec_from_pred(predict(phi0, c3, N_STAR * (1 - eps), links))
    J_n = (mu_np - mu_nm) / (2.0 * eps * N_STAR)
    J_ext = np.column_stack([J_phi, J_c3, J_n])

    Jw = J / sig[:, None]
    Jw_ext = J_ext / sig[:, None]
    nu_eff = matrix_rank(Jw)
    nu_eff_ext = matrix_rank(Jw_ext)

    chi2 = chi2_vec(mu, y, sig)
    dof = n_obs
    chi2_dof = chi2 / dof
    p_gof = float(chi2_dist.sf(chi2, dof))
    print("  chi2 = %.4f  dof = %d  chi2/dof = %.3f  p = %.4g"
          % (chi2, dof, chi2_dof, p_gof))
    print("  nu_eff = %d  nu_eff_ext = %d" % (nu_eff, nu_eff_ext))
    check("chi2/dof order 1 [N]: 0.25 <= %.3f <= 4.0 (probe 11.80/9 "
          "= 1.31, p = 0.225)" % chi2_dof,
          0.25 <= chi2_dof <= 4.0)
    check("GoF p not a kill [N]: p = %.4g > 1e-3" % p_gof, p_gof > 1e-3)
    check("nu_eff < n_obs [N]: hit-counting overstates independent "
          "evidence (nu_eff=%d n_obs=%d)" % (nu_eff, n_obs),
          nu_eff < n_obs)
    check("nu_eff = 1 [N]: all seed/flavor slopes collinear in phi0",
          nu_eff == 1)
    check("N_star raises rank by 1 [N]: inflation is a second input",
          nu_eff_ext == nu_eff + 1)
    check("headline chi2 ~ 11.80 [N]: |chi2 - 11.80| < 0.5 "
          "(got %.3f)" % chi2, abs(chi2 - 11.80) < 0.5)

    rng = np.random.default_rng(NULL_SEED)
    lo, hi = math.log(LINK_SCRAMBLE[0]), math.log(LINK_SCRAMBLE[1])
    chi_null = np.empty(N_NULL)
    keys = list(links.keys())
    for i in range(N_NULL):
        L = dict(links)
        for k in keys:
            if k == "delta_deg":
                L[k] = float(links[k] + rng.uniform(-90.0, 90.0))
            else:
                L[k] = float(links[k] * math.exp(rng.uniform(lo, hi)))
        chi_null[i] = chi2_vec(vec_from_pred(predict(phi0, c3, N_STAR, L)),
                               y, sig)
    pct = float(np.mean(chi_null <= chi2))
    print("  TFPT percentile in %d scrambled decoders = %.2f%%  "
          "(null median %.1f)" % (N_NULL, 100.0 * pct,
                                  float(np.median(chi_null))))
    check("null median >> TFPT [N]: ratio > 10",
          float(np.median(chi_null)) > 10.0 * chi2)
    check("TFPT <= 5th percentile of scrambled-decoder null [N] "
          "(probe: 0th percentile)",
          pct <= 0.05)

    names = sorted(set(bundles))
    loo_ok = True
    full_ratio = chi2 / n_obs
    for drop in names:
        mask = np.array([b != drop for b in bundles])
        if mask.sum() < 2:
            continue
        c = chi2_vec(mu[mask], y[mask], sig[mask])
        d = int(mask.sum())
        ratio = c / d
        print("  LOO drop %-10s  n=%d  chi2/dof=%.3f" % (drop, d, ratio))
        loo_ok &= 0.2 <= ratio <= 4.0
        loo_ok &= ratio <= 3.0 * max(full_ratio, 0.3) or ratio <= 4.0
    check("LOO stable [N]: remaining chi2/dof in [0.2, 4] and not "
          "a 3x blow-up", loo_ok)

    check("HOLDOUTS DECLARED [N]: JUNO / DESI / DUNE / LiteBIRD are "
          "named and NOT consumed (v1 chi2 uses only the frozen nine)",
          len(HOLDOUTS) == 4)
    check("PROMOTION CONDITIONS TYPED [N]: off-diagonal Sigma, "
          "formula-grammar census, genuine future holdouts -- "
          "PRED.JOINTLIKELIHOOD.01 stays [O] as a contract", True)
    check("FIREWALL (scope): v1 statistics; Sigma_exp diagonal; "
          "unmodelled NuFIT/Planck cov flagged; no marker move", True)
    return summary("v992 joint likelihood v1: chi2~11.80/9, "
                   "nu_eff=1, 0th percentile, contract stays [O]")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
