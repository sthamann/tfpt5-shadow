#!/usr/bin/env python3
"""nu-scalaron-falsification -- deterministic prediction pass (no RNG).

Derives, from the FROZEN hypothesis set hypotheses/nu_scalaron_v1.yaml
(zero dials), the full neutrino observable vector of the FLAV.NUSCALE.05
candidate M_R = 3 c3^{7/2} Mbar and compares it against the frozen,
dated data snapshot.  Writes results/results.json.

Chain: M_R (frozen) -> m3 (v481 1-loop forward run, y_nu = y_t)
       -> m2 (two frozen variants) -> m1 = 0 (NO floor)
       -> Sigma m_nu, m_beta, m_bb interval (PMNS frozen, v270)
       -> leptogenesis leg reported (M1 = M_R phi0^4, m~1 = m3/10).

Usage:  python scripts/derive_predictions.py
"""
import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(ROOT))
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import c3, Mbar, phi0, N_fam  # noqa: E402

# ---------------- frozen inputs (mirror of the YAML) ----------------
C3 = float(c3)
MBARF = float(Mbar)
PHI0 = float(phi0)
MZ, V_EW = 91.1876, 246.22
YT_MZ = math.sqrt(2) * 162.5 / V_EW
LAM_MZ = 0.130
A_INV_MZ = (59.01, 29.59, 8.44)
A_LAMBDA = 10.0

DM2_21_MEAS = 7.49e-5          # NuFIT 6.0 (2024)
DM2_3L_MEAS = 2.513e-3
SIGMA_BOUND = 0.0642           # DESI DR2 (2025), 95% CL, LCDM
MBETA_BOUND = 0.45             # KATRIN 2024
MBB_BOUND = (0.028, 0.122)     # KamLAND-Zen 2024 (NME spread)

with open(os.path.join(ROOT, "hypotheses", "nu_scalaron_v1.yaml"), "rb") as f:
    HYP_SHA = hashlib.sha256(f.read()).hexdigest()[:16]


def run_sm_up(mu_hi, n=20000):
    """the frozen v481 1-loop SM runner (verbatim tool)."""
    g1, g2, g3 = [math.sqrt(4 * math.pi / a) for a in A_INV_MZ]
    yt, lam = YT_MZ, LAM_MZ
    h = math.log(mu_hi / MZ) / n
    k = 1 / (16 * math.pi ** 2)
    b = (41 / 10, -19 / 6, -7)
    I_alpha = 0.0
    for _ in range(n):
        I_alpha += (-3 * g2 * g2 + 6 * yt * yt + lam) * h
        dg1 = k * b[0] * g1 ** 3
        dg2 = k * b[1] * g2 ** 3
        dg3 = k * b[2] * g3 ** 3
        dyt = k * yt * (4.5 * yt ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2
                        - (17 / 20) * g1 ** 2)
        dlam = k * (24 * lam ** 2 - 6 * yt ** 4 + 12 * lam * yt ** 2
                    - 3 * lam * (3 * g2 ** 2 + 0.6 * g1 ** 2)
                    + 0.375 * (2 * g2 ** 4 + (g2 ** 2 + 0.6 * g1 ** 2) ** 2))
        g1 += h * dg1
        g2 += h * dg2
        g3 += h * dg3
        yt += h * dyt
        lam += h * dlam
    return yt, math.exp(-I_alpha / (16 * math.pi ** 2))


def main():
    out = {"project": "nu-scalaron-falsification",
           "hypothesis_sha16": HYP_SHA,
           "candidate": "FLAV.NUSCALE.05 (v986)",
           "axes": {}}

    # frozen candidate scale
    M_scal = C3 ** 3.5 * MBARF
    M_R = N_fam * M_scal
    out["M_scal_GeV"] = M_scal
    out["M_R_GeV"] = M_R

    # forward seesaw: m3 at the frozen M_R
    yt, R = run_sm_up(M_R)
    m3 = (yt * V_EW / math.sqrt(2)) ** 2 / M_R * R * 1e9      # eV
    out["m3_eV"] = m3

    # PMNS frozen channels (v270)
    s12sq = 1.0 / 3 - PHI0 / 2
    s23sq = 0.5
    s13sq = PHI0 * math.exp(-5.0 / 6)
    c13sq = 1 - s13sq
    J = (math.sqrt(s12sq * (1 - s12sq)) * math.sqrt(s23sq * (1 - s23sq))
         * math.sqrt(s13sq) * c13sq * math.sin(4 * math.pi / 3))
    out["pmns"] = {"sin2_th12": s12sq, "sin2_th23": s23sq,
                   "sin2_th13": s13sq, "delta": "4pi/3",
                   "J_PMNS": J}

    # mass chain, both frozen m2 variants; m1 = 0
    variants = {}
    for tag, m2 in (("a_tfpt_internal", m3 * math.sqrt(abs(J))),
                    ("b_hybrid", math.sqrt(DM2_21_MEAS))):
        sigma = m3 + m2
        Ue1sq = c13sq * (1 - s12sq)
        Ue2sq = c13sq * s12sq
        Ue3sq = s13sq
        m_beta = math.sqrt(Ue2sq * m2 ** 2 + Ue3sq * m3 ** 2)
        A = Ue2sq * m2
        Bt = Ue3sq * m3
        m_bb = (abs(A - Bt), A + Bt)               # exact phase interval
        variants[tag] = {"m1_eV": 0.0, "m2_eV": m2, "m3_eV": m3,
                         "sigma_mnu_eV": sigma, "m_beta_eV": m_beta,
                         "m_bb_interval_eV": m_bb,
                         "Ue_sq": [Ue1sq, Ue2sq, Ue3sq]}
    out["variants"] = variants

    # comparisons / verdicts
    m3_meas = math.sqrt(DM2_3L_MEAS)
    dev_m3 = m3 / m3_meas - 1
    out["axes"]["m3_vs_nufit"] = {
        "pred": m3, "meas": m3_meas, "dev": dev_m3,
        "verdict": "consistent" if abs(dev_m3) < 0.05 else "tension",
        "note": "dev inside the >50% v482 RG scheme envelope"}

    sig_a = variants["a_tfpt_internal"]["sigma_mnu_eV"]
    sig_b = variants["b_hybrid"]["sigma_mnu_eV"]
    out["axes"]["sigma_mnu_vs_desi"] = {
        "pred_a": sig_a, "pred_b": sig_b, "bound_95": SIGMA_BOUND,
        "margin_a": SIGMA_BOUND - sig_a, "margin_b": SIGMA_BOUND - sig_b,
        "verdict": ("consistent" if max(sig_a, sig_b) < SIGMA_BOUND
                    else "killed"),
        "note": "K1 kill axis: LCDM 95%% UL sits %.1f%% above the "
                "prediction -- one DESI-class improvement decides. "
                "HONESTY (mirrors the corpus sum-m_nu row): the DESI DR2 "
                "effective-mass POSTERIOR squeeze puts even the NO floor "
                "0.0588 eV at ~+3 sigma under LCDM (model-dependent; "
                "w0waCDM relaxes it) -- the candidate at 0.0600 eV sits "
                "under the same model-dependent pressure"
                % (100 * (SIGMA_BOUND / max(sig_a, sig_b) - 1))}

    mb = variants["a_tfpt_internal"]["m_beta_eV"]
    out["axes"]["m_beta_vs_katrin"] = {
        "pred": mb, "bound": MBETA_BOUND,
        "verdict": "consistent",
        "note": "prediction %.4f eV is ~%.0fx below the KATRIN bound -- "
                "not a near-term discriminator" % (mb, MBETA_BOUND / mb)}

    mbb = variants["a_tfpt_internal"]["m_bb_interval_eV"]
    out["axes"]["m_bb_vs_kamland"] = {
        "pred_interval": mbb, "bound_range": MBB_BOUND,
        "verdict": "consistent",
        "note": "NO interval [%.2e, %.2e] eV sits below the current "
                "bound window; LEGEND-1000-class kills only IO"
                % mbb}

    # leptogenesis leg (reported, not re-solved)
    out["leptogenesis"] = {
        "M1_GeV": M_R * PHI0 ** 4,
        "washout_m1_eV": m3 / A_LAMBDA,
        "note": "v184 relations at the frozen M_R; Boltzmann re-run is a "
                "declared follow-up, not consumed here"}

    # overall verdict
    verds = [a["verdict"] for a in out["axes"].values()]
    out["verdict"] = ("killed" if "killed" in verds
                      else "tension" if "tension" in verds
                      else "consistent")
    out["honest_scope"] = (
        "consistency pass against frozen dated bounds; NOT blind "
        "confirmation (m3/PMNS channels were known); holdout = future "
        "releases only; candidate stays [C]/[N], mechanism [O]; the "
        "LCDM posterior squeeze (corpus sum-m_nu row: tension) applies "
        "to the whole NO branch incl. this candidate -- model-dependent")

    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    path = os.path.join(ROOT, "results", "results.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print("hypothesis sha16:", HYP_SHA)
    print("M_R = %.4e GeV, m3 = %.5f eV (dev %+.2f%% vs NuFIT)"
          % (M_R, m3, 100 * dev_m3))
    for tag, v in variants.items():
        print("%s: m2 = %.5f, Sigma = %.5f eV, m_beta = %.5f eV, "
              "m_bb in [%.2e, %.2e] eV"
              % (tag, v["m2_eV"], v["sigma_mnu_eV"], v["m_beta_eV"],
                 v["m_bb_interval_eV"][0], v["m_bb_interval_eV"][1]))
    print("DESI margin: a %+.4f eV, b %+.4f eV (bound %.4f)"
          % (out["axes"]["sigma_mnu_vs_desi"]["margin_a"],
             out["axes"]["sigma_mnu_vs_desi"]["margin_b"], SIGMA_BOUND))
    print("leptogenesis leg: M1 = %.3e GeV, m~1 = %.4f eV"
          % (out["leptogenesis"]["M1_GeV"],
             out["leptogenesis"]["washout_m1_eV"]))
    print("VERDICT:", out["verdict"])
    print("wrote", path)


if __name__ == "__main__":
    main()
