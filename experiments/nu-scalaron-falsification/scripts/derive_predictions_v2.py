#!/usr/bin/env python3
"""nu-scalaron-falsification -- v2 spectral-matrix prediction pass (no RNG).

Derives, from the FROZEN hypothesis set hypotheses/nu_scalaron_v2.yaml,
the type-I seesaw of the review-wave-3 repaired operator

    M_R = M_scal * diag(eps, 2 eps, 3)
    eps = phi0^2 / A_Lambda

in the Q_+ eigenbasis (v69), and compares against the frozen dated
snapshot.  Writes results/results_v2.json.

CRITICAL HONESTY: the corpus does not freeze a 3x3 Dirac Y_nu (v481
freezes only y3 = y_t [P]; v9 is a light Majorana texture; v263's
diag(0.3,1,1) is an existence example).  This pass therefore

  (i)  runs the named naive diagnostic Y = y_t(M3) * I  -- expected
       to overshoot, and typed as a kill of the UNTEXTURED operator;
  (ii) inverts the aligned (eigenbasis-diagonal) seesaw for the (y1, y2)
       the data require, with y3 = y_t(M3) frozen -- typed
       DATA_CONSTRAINS_TEXTURE, not a hit.

Usage:  python scripts/derive_predictions_v2.py
"""
import hashlib
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(ROOT))
sys.path.insert(0, os.path.join(REPO, "verification"))
from tfpt_constants import c3, Mbar, phi0, g_car  # noqa: E402

C3 = float(c3)
MBARF = float(Mbar)
PHI0 = float(phi0)
A_LAMBDA = 2.0 * float(g_car)     # 10
MZ, V_EW = 91.1876, 246.22
YT_MZ = math.sqrt(2) * 162.5 / V_EW
LAM_MZ = 0.130
A_INV_MZ = (59.01, 29.59, 8.44)

DM2_21_MEAS = 7.49e-5
DM2_3L_MEAS = 2.513e-3
SIGMA_BOUND = 0.0642
MBETA_BOUND = 0.45
MBB_BOUND = (0.028, 0.122)

with open(os.path.join(ROOT, "hypotheses", "nu_scalaron_v2.yaml"), "rb") as f:
    HYP_SHA = hashlib.sha256(f.read()).hexdigest()[:16]


def run_sm_up(mu_hi, n=20000):
    """frozen v481 1-loop SM runner (verbatim tool)."""
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
        dyt = k * yt * (4.5 * yt * yt - 8 * g3 * g3 - 2.25 * g2 * g2
                        - (17 / 20) * g1 * g1)
        dlam = k * (24 * lam * lam - 6 * yt ** 4 + 12 * lam * yt * yt
                    - 3 * lam * (3 * g2 * g2 + 0.6 * g1 * g1)
                    + 0.375 * (2 * g2 ** 4
                               + (g2 * g2 + 0.6 * g1 * g1) ** 2))
        g1 += h * dg1
        g2 += h * dg2
        g3 += h * dg3
        yt += h * dyt
        lam += h * dlam
    return yt, math.exp(-I_alpha / (16 * math.pi ** 2))


def m_from_y(y, M, R):
    """light mass in eV: m = (y v / sqrt(2))^2 / M * R."""
    return (y * V_EW / math.sqrt(2)) ** 2 / M * R * 1e9


def y_from_m(m_eV, M, R):
    """invert the seesaw for a real Yukawa at matching (m in eV, M in GeV)."""
    return math.sqrt(m_eV * M / R / 1e9 * 2.0 / V_EW ** 2)


def main():
    out = {
        "project": "nu-scalaron-falsification",
        "pass": "v2 spectral-matrix (review wave 3)",
        "hypothesis_sha16": HYP_SHA,
        "premise": "PREMISE_FOUND (Q_+ at v10/v50/v69, Spec={1,2,3})",
        "axes": {},
    }

    M_scal = C3 ** 3.5 * MBARF
    eps = PHI0 ** 2 / A_LAMBDA
    M1 = eps * M_scal
    M2 = 2.0 * eps * M_scal
    M3 = 3.0 * M_scal
    # symmetric Majorana operator in the Q_+ eigenbasis (v69)
    M_R = np.diag([M1, M2, M3])
    out["M_scal_GeV"] = M_scal
    out["epsilon"] = eps
    out["M_R_eigenvalues_GeV"] = {"M1": M1, "M2": M2, "M3": M3}
    out["unification"] = {
        "M1_equals_v212_decuple_by_definition": True,
        "M1_formula": "eps M_scal == M_scal phi0^2 / A_Lambda",
        "M3_equals_v986_rung": True,
        "M2_is_new_prediction": True,
        "ansatz": "mixed insertion (eps, 2 eps, 3) is reviewer ansatz, "
                  "not derived from Q_+",
        "repackaging": "M1 (v212) and M3 (v986) packaged as eigenvalues; "
                       "the unification is exact-by-construction",
        "new": "M2 = 2 eps M_scal",
    }

    yt3, R3 = run_sm_up(M3)
    yt2, R2 = run_sm_up(M2)
    yt1, R1 = run_sm_up(M1)
    out["rg"] = {
        "yt_at_M3": yt3, "R_at_M3": R3,
        "yt_at_M2": yt2, "R_at_M2": R2,
        "yt_at_M1": yt1, "R_at_M1": R1,
    }

    # ---- (i) naive diagnostic: Y = yt(M3) * I  (FROZEN, named kill) ----
    # Explicit matching-scale matrix, then per-eigenvalue ADKLR rundown.
    Y_naive = yt3 * np.eye(3)
    M_nu_match = -(V_EW ** 2 / 2.0) * (Y_naive.T @ np.linalg.inv(M_R) @ Y_naive)
    evals_match = np.linalg.eigvalsh(M_nu_match)          # GeV, signed
    m_match_eV = sorted(abs(float(x)) * 1e9 for x in evals_match)
    m_naive = [m_from_y(yt3, M, R) for M, R in ((M1, R1), (M2, R2), (M3, R3))]
    m_naive_sorted = sorted(m_naive)
    sigma_naive = sum(m_naive)
    dm2_21_naive = m_naive_sorted[1] ** 2 - m_naive_sorted[0] ** 2
    dm2_31_naive = m_naive_sorted[2] ** 2 - m_naive_sorted[0] ** 2
    out["naive_Y_eq_yt_I"] = {
        "Y_frozen": "y_t(M3) * I, y_t(M3) = %.6f" % yt3,
        "M_nu_formula": "-(v^2/2) Y^T M_R^{-1} Y  (v = 246.22 GeV)",
        "M_nu_match_GeV_diag": [float(M_nu_match[i, i]) for i in range(3)],
        "m_matching_eV_sorted": m_match_eV,
        "m_eV_on_Qplus_eigenlines_RGdown": m_naive,
        "m_sorted_eV": m_naive_sorted,
        "dm2_21_eV2": dm2_21_naive,
        "dm2_31_eV2": dm2_31_naive,
        "sigma_mnu_eV": sigma_naive,
        "note_mixing": "M_nu is diagonal in the Q_+ eigenbasis; this is "
                       "NOT the frozen v270 PMNS -- mass eigenvalues suffice "
                       "to kill.  m_beta/m_bb not reported (need a 3x3 Y_nu "
                       "in the charged-lepton basis).",
    }

    m3_nufit = math.sqrt(DM2_3L_MEAS)
    overshoot = m_naive_sorted[-1] / m3_nufit
    naive_kill = (sigma_naive > SIGMA_BOUND
                  or m_naive_sorted[-1] > MBETA_BOUND)
    out["axes"]["K5_untextured_Y"] = {
        "pred_sigma_eV": sigma_naive,
        "pred_heaviest_eV": m_naive_sorted[-1],
        "nufit_m3_eV": m3_nufit,
        "overshoot_vs_nufit_m3": overshoot,
        "desi_bound_eV": SIGMA_BOUND,
        "katrin_bound_eV": MBETA_BOUND,
        "verdict": "killed" if naive_kill else "consistent",
        "note": "naive m ~ v^2 yt^2 / M_1 is %.0fx NuFIT m3 and "
                "%.0fx the DESI Sigma bound -- texture suppression is "
                "mandatory; this kills Y proportional to I, not Q_+"
                % (overshoot, sigma_naive / SIGMA_BOUND),
    }

    # ---- (ii) constraint invert, y3 = yt(M3) frozen ----
    m3_from_y3 = m_from_y(yt3, M3, R3)          # = v1 m3 (same M3, same runner)
    m2_nufit = math.sqrt(DM2_21_MEAS)           # NO, m1=0 hybrid
    m1_floor = 0.0
    # residual cosmological room for m1 under DESI UL, using v1-like m2+m3
    m1_desi_room = max(0.0, SIGMA_BOUND - m3_from_y3 - m2_nufit)

    y3_frozen = yt3
    y2_for_nufit = y_from_m(m2_nufit, M2, R2)
    y1_for_floor = 0.0
    y1_desi_ul = y_from_m(m1_desi_room, M1, R1) if m1_desi_room > 0 else 0.0

    # v1-internal m2 = m3 * sqrt(|J_PMNS|) with frozen v270 PMNS
    s12sq = 1.0 / 3 - PHI0 / 2
    s23sq = 0.5
    s13sq = PHI0 * math.exp(-5.0 / 6)
    J = (math.sqrt(s12sq * (1 - s12sq)) * math.sqrt(s23sq * (1 - s23sq))
         * math.sqrt(s13sq) * (1 - s13sq) * math.sin(4 * math.pi / 3))
    m2_v1_internal = m3_from_y3 * math.sqrt(abs(J))
    y2_for_v1_internal = y_from_m(m2_v1_internal, M2, R2)

    out["constraint"] = {
        "type": "DATA_CONSTRAINS_TEXTURE",
        "y3_frozen": y3_frozen,
        "y3_equals_yt_M3": True,
        "m3_from_frozen_y3_eV": m3_from_y3,
        "m3_vs_v1": "same M3 = 3 M_scal and same y3 = yt => same m3 as v1",
        "aligned_eigenbasis": {
            "y1_for_m1_eq_0": y1_for_floor,
            "y1_DESI_95UL": y1_desi_ul,
            "y2_for_nufit_m2": y2_for_nufit,
            "y2_for_v1_internal_m2": y2_for_v1_internal,
            "y2_over_y3_nufit": y2_for_nufit / y3_frozen,
            "y1_over_y3_DESI_UL": y1_desi_ul / y3_frozen,
            "y2_over_y3_v1_internal": y2_for_v1_internal / y3_frozen,
        },
        "targets_eV": {
            "m1_floor": m1_floor,
            "m1_DESI_room": m1_desi_room,
            "m2_nufit": m2_nufit,
            "m2_v1_internal": m2_v1_internal,
            "m3_from_y3": m3_from_y3,
            "m3_nufit": m3_nufit,
        },
        "note": "no frozen 3x3 Y_nu exists; numbers above are the "
                "Yukawas the data WOULD require in the aligned "
                "eigenbasis.  They are constraints, not predictions.  "
                "An aligned diagonal Y does not produce v270 PMNS "
                "(M_nu would be diagonal in the Q_+ basis).",
    }

    # observable table for the FROZEN y3 slice (m3 only) vs v1 comparators
    dev_m3 = m3_from_y3 / m3_nufit - 1
    out["axes"]["m3_M3_slice_vs_nufit"] = {
        "pred": m3_from_y3, "meas": m3_nufit, "dev": dev_m3,
        "verdict": "consistent" if abs(dev_m3) < 0.05 else "tension",
        "note": "this is the v1 number: M3 = 3 M_scal and y3 = yt are "
                "the same inputs.  Not a new confirmation.",
    }

    # m_beta / m_bb are NOT predicted without a 3x3 Y_nu
    out["axes"]["m_beta_m_bb"] = {
        "pred": None,
        "verdict": "data_limited",
        "note": "m_beta and m_bb require a full 3x3 Y_nu (and charged-"
                "lepton basis).  Not computed; not invented.",
    }

    out["kill_status"] = {
        "K1": "not triggered (M3-slice Sigma would still sit at v1 "
              "0.060 eV IF y1=y2 were suppressed as constrained; the "
              "untextured operator is already dead on K5)",
        "K2": "not triggered (M3 unchanged vs v1)",
        "K3": "not triggered (NO still assumed)",
        "K4": "not applicable this pass (no m_bb without 3x3 Y_nu)",
        "K5": "TRIGGERED -- untextured Y = yt I is killed",
        "K6": "not triggerable (no frozen corpus 3x3 Y_nu)",
    }

    out["verdict"] = "DATA_CONSTRAINS_TEXTURE"
    out["honest_scope"] = (
        "EXPLORATION.  Q_+ is corpus (PREMISE_FOUND).  The mixed "
        "insertion (eps, 2 eps, 3) is a reviewer ansatz; M1 and M3 "
        "are a reparametrization of two existing scales; M2 is the "
        "one new prediction.  No 3x3 Dirac texture is frozen in the "
        "corpus -- this pass does not invent one.  Untextured Y ~ I "
        "is killed by ~10^4 overshoot.  Data require |y1|/y3 <~ 1e-3 "
        "and |y2|/y3 ~ few 1e-3 in the aligned eigenbasis.  Candidate "
        "row FLAV.NUSCALE.05 stays [C]/[N], mechanism [O]; nothing "
        "here moves a ledger marker."
    )

    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    path = os.path.join(ROOT, "results", "results_v2.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)

    print("hypothesis sha16:", HYP_SHA)
    print("eps = %.6e" % eps)
    print("M1 = %.6e GeV  (v212 decuple, exact-by-construction)" % M1)
    print("M2 = %.6e GeV  (NEW)" % M2)
    print("M3 = %.6e GeV  (v986 rung)" % M3)
    print("naive Y=yt I: m(RG) = [%.4g, %.4g, %.4g] eV  Sigma = %.4g eV  "
          "dm2_31 = %.3g eV^2  overshoot vs NuFIT m3 = x%.0f"
          % (m_naive[0], m_naive[1], m_naive[2], sigma_naive,
             dm2_31_naive, overshoot))
    print("frozen y3 = yt(M3) = %.5f -> m3 = %.5f eV (dev %+.2f%% vs NuFIT)"
          % (y3_frozen, m3_from_y3, 100 * dev_m3))
    print("constraint aligned: y2/y3 (NuFIT m2) = %.4e ; "
          "y1/y3 (DESI room) < %.4e"
          % (y2_for_nufit / y3_frozen, y1_desi_ul / y3_frozen))
    print("K5:", out["axes"]["K5_untextured_Y"]["verdict"])
    print("VERDICT:", out["verdict"])
    print("wrote", path)


if __name__ == "__main__":
    main()
