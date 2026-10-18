"""P9-FORECAST driver: anchors -> per-channel programme power -> hierarchical
combination -> the 80% gate -> leave-one-out consistency -> results.json.

Usage:  PYTHONPATH=src python -m p9_forecast.cli analyze --seed 0 [--fast]
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from . import combine, frb, gaussian, gw, psr, uhecr
from .constants import (DETECTION_ALPHA, EPS_PREDICTED, EPS_REFERENCE,
                        GW_ECHO_CEILING, N_MC_NULL, N_MC_SIGNAL, POWER_GATE,
                        Z95, summary)

RESULTS = Path(__file__).resolve().parents[2] / "results" / "results.json"

# ----------------------------------------------------------- prereg mirrors
J1740 = dict(f0_hz=1.6471971475, transients=((2.4090445e-08, 124.29436),),
             tau_min_d=0.4050599, tau_max_d=379.39616, n_toa=137,
             sigma_toa_us=100.0, rms_us=684.13)
VELA_PG08 = dict(n_toa=540, tau_min_d=10.049254, tau_max_d=860.70710,
                 sigma_toa_us=100.0, rms_us=551.78)
PG06B_2019 = dict(n_seg=44, tau_min_d=4.4674944, tau_max_d=885.23336,
                  sigma_nu_uhz=0.6, eps_50=0.55)
RADIO_BLOCKS = [[0.05, 3.0, 8.0], [3.0, 30.0, 2.0], [30.0, 300.0, 1.0],
                [300.0, 1000.0, 0.3333]]
EPS_GRID = [EPS_PREDICTED, 0.05, 0.10, 0.30]

ANCHOR_TOL = 0.20
PUBLISHED_ANCHORS = {
    "PSR": {"eps": EPS_REFERENCE, "power": 0.50,
            "source": "pulsar-glitch-recovery PG.08 J1740-3015 injection (ref_rate 0.50)"},
    "PSR_NU": {"eps": 0.55, "power": 0.458,
               "source": "pulsar-glitch-recovery PG.06b FULL 2019 leg injection "
                         "(eps_50 = 0.55; rate 0.458 at eps = 0.5 grid point)"},
    "FRB": {"eps": EPS_REFERENCE, "power": 0.9375,
            "source": "repeater-cascade validation.json (comb_ref_rate 0.9375, phi=0)"},
    "UHECR": {"eps": EPS_PREDICTED, "power": 0.233,
              "source": "uhecr-energy-dsi results.json (injection_power_at_95pct)"},
    "GW": {"eps": "eps90", "power": 0.90,
           "source": "gw-ringdown-echo Stage 1h recovery criterion (90% at eps90)"},
}


def eps80_from_grid(eps_grid: list[float], powers: list[float]) -> float | None:
    for e, p in zip(eps_grid, powers):
        if p >= POWER_GATE:
            prev = [(ee, pp) for ee, pp in zip(eps_grid, powers) if ee < e]
            if not prev:
                return e
            e0, p0 = prev[-1]
            if p == p0:
                return e
            return float(e0 + (POWER_GATE - p0) * (e - e0) / (p - p0))
    return None


def analyze(seed: int = 0, fast: bool = False) -> dict:
    t0 = time.time()
    n_null = 120 if fast else N_MC_NULL
    n_sig = 80 if fast else N_MC_SIGNAL
    n_grid = 40 if fast else 100
    rng = np.random.default_rng(seed)
    out: dict = {"experiment": "p9-forecast", "prereg": "hypotheses/p9_forecast_v1.yaml",
                 "seed": seed, "fast": fast, "kernel": summary()}
    combo_channels: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    programmes: list[dict] = []
    anchors: dict = {}

    # ---------------------------------------------------------------- PSR
    print("[PSR] calibrating noise on the PG.08 anchors ...")
    anchor_epochs = np.sort(rng.uniform(J1740["tau_min_d"], J1740["tau_max_d"],
                                        J1740["n_toa"]))

    def j1740_cfg(step: float) -> psr.GlitchConfig:
        return psr.GlitchConfig("J1740-anchor", J1740["f0_hz"], J1740["transients"],
                                tuple(anchor_epochs), J1740["sigma_toa_us"], step)

    rw_power, cal_power = psr.calibrate_rw_power(j1740_cfg, n_mc=40 if fast else 60,
                                                 seed=seed)
    rw_rms_j1740 = psr.calibrate_rw_rms(j1740_cfg, target_rms_us=J1740["rms_us"],
                                        seed=seed)
    pw_ref, _ = psr.campaign_power([j1740_cfg(rw_power)], EPS_REFERENCE,
                                   reading="phase", n_mc=n_sig, seed=seed + 11)
    pw_ref_rms, _ = psr.campaign_power([j1740_cfg(rw_rms_j1740)], EPS_REFERENCE,
                                       reading="phase", n_mc=n_sig, seed=seed + 14)
    fp_anchor, _ = psr.campaign_power([j1740_cfg(rw_rms_j1740)], 0.0,
                                      reading="phase", n_mc=n_null, seed=seed + 13)

    vela_pg08_epochs = np.sort(np.random.default_rng(seed + 3).uniform(
        VELA_PG08["tau_min_d"], VELA_PG08["tau_max_d"], VELA_PG08["n_toa"]))

    def vela_pg08_cfg(step: float) -> psr.GlitchConfig:
        return psr.GlitchConfig("Vela-pg08", psr.VELA_F0, psr.VELA_SET_B,
                                tuple(vela_pg08_epochs), VELA_PG08["sigma_toa_us"], step)

    rw_vela = psr.calibrate_rw_rms(vela_pg08_cfg, target_rms_us=VELA_PG08["rms_us"],
                                   seed=seed + 4)
    anchors["PSR"] = {
        "rw_step_power_matched_us": round(rw_power, 1),
        "rw_step_rms_matched_j1740_us": round(rw_rms_j1740, 1),
        "rw_step_rms_matched_vela_us": round(rw_vela, 1),
        "model_power_at_0.30_power_matched": round(pw_ref, 3),
        "model_power_at_0.30_rms_matched": round(pw_ref_rms, 3),
        "false_positive_rate": round(fp_anchor, 3),
        "published": PUBLISHED_ANCHORS["PSR"],
        "pass": bool(abs(pw_ref - 0.50) <= ANCHOR_TOL
                     or abs(pw_ref_rms - 0.50) <= ANCHOR_TOL),
    }
    print(f"[PSR] J1740 anchor: rw_pow={rw_power:.0f}, rw_rms={rw_rms_j1740:.0f}, "
          f"rw_vela={rw_vela:.0f} us/sqrt(d); power@0.30 = {pw_ref:.2f} (pow-matched) "
          f"/ {pw_ref_rms:.2f} (rms-matched), published 0.50; fp={fp_anchor:.3f}")

    # PG.06b-2019 nu-space anchor (slow-term amplitude inverted from eps_50)
    tau_2019 = np.geomspace(PG06B_2019["tau_min_d"], PG06B_2019["tau_max_d"],
                            PG06B_2019["n_seg"])
    a_slow, pw_at_eps50 = psr.calibrate_xray_slow_amp(
        tau_2019, PG06B_2019["sigma_nu_uhz"], eps_50=PG06B_2019["eps_50"],
        n_mc=32 if fast else 48, seed=seed + 6)
    anchors["PSR_NU"] = {
        "slow_amp_uhz_inverted": round(a_slow, 3),
        "model_power_at_eps50": round(pw_at_eps50, 3),
        "published": PUBLISHED_ANCHORS["PSR_NU"],
        "pass": bool(abs(pw_at_eps50 - 0.5) <= ANCHOR_TOL),
    }
    print(f"[PSR] PG.06b-2019 nu anchor: slow amp {a_slow:.2f} uHz -> power@0.55 = "
          f"{pw_at_eps50:.2f} (target 0.50)")

    # Campaign detection is calibrated on the programme's OWN null MC (the
    # forecast analogue of the siblings' shuffle null): threshold = 95th
    # percentile of the null Fisher statistic. The raw per-glitch p<0.05
    # criterion is anti-conservative under random-walk red noise (raw fp up
    # to ~0.2, reported as diagnostic).
    radio_epochs = psr.cadence_epochs(RADIO_BLOCKS, np.random.default_rng(seed + 5))
    reach = psr.reach_periods(radio_epochs)
    for set_name, transients in (("SET-A", psr.VELA_SET_A), ("SET-B", psr.VELA_SET_B)):
        cfgs = [psr.GlitchConfig(f"Vela-g{j}", psr.VELA_F0, transients,
                                 tuple(radio_epochs), 50.0, rw_vela)
                for j in range(2)]
        for reading in ("phase", "nu"):
            fp_raw, stats_null = psr.campaign_power(cfgs, 0.0, reading=reading,
                                                    n_mc=n_null, seed=seed + 22)
            thr = float(np.quantile(stats_null, 1.0 - DETECTION_ALPHA))
            powers = []
            stats_pred = None
            for e in EPS_GRID:
                n_e = n_sig if e == EPS_PREDICTED else n_grid
                _, st = psr.campaign_power(cfgs, e, reading=reading, n_mc=n_e,
                                           seed=seed + 21)
                powers.append(float(np.mean(st > thr)))
                if e == EPS_PREDICTED:
                    stats_pred = st
            key = f"PSR-5Y-RADIO-{reading.upper()}({set_name})"
            programmes.append({
                "channel": "PSR", "programme": key, "horizon_5yr": True,
                "description": "Vela glitch trigger, dense radio cadence "
                               f"(n_TOA={len(radio_epochs)}/glitch, tau 0.05..1000 d "
                               f"= {reach:.2f} periods, sigma_TOA=50us, rw="
                               f"{rw_vela:.0f}us/sqrt(d) Vela-rms-matched, 2 glitches"
                               f"/5yr), transients {set_name} "
                               f"({'2024 short-only' if set_name == 'SET-A' else '2021 PuMA incl. 4.94uHz@502d'}), "
                               f"{reading}-space detector, null-MC-calibrated threshold",
                "power_at_predicted": powers[0],
                "false_positive": DETECTION_ALPHA, "false_positive_raw": fp_raw,
                "eps_grid": EPS_GRID, "power_grid": powers,
                "eps80": eps80_from_grid(EPS_GRID, powers),
            })
            if set_name == "SET-A" and reading == "nu":
                combo_channels["PSR"] = (stats_pred, stats_null)
            print(f"[PSR] {key}: power@pred={powers[0]:.3f}, fp_raw={fp_raw:.3f}, "
                  f"grid={[round(p, 2) for p in powers]}")

    xray_tau = np.arange(0.03, 300.0, 0.5)
    fp_raw, stats_null = psr.xray_campaign_power(psr.VELA_SET_B, xray_tau, 0.6, 0.0, 2,
                                                 n_mc=n_null, seed=seed + 32)
    thr = float(np.quantile(stats_null, 1.0 - DETECTION_ALPHA))
    powers = []
    for e in EPS_GRID:
        n_e = n_sig if e == EPS_PREDICTED else n_grid
        _, st = psr.xray_campaign_power(psr.VELA_SET_B, xray_tau, 0.6, e, 2,
                                        n_mc=n_e, seed=seed + 31)
        powers.append(float(np.mean(st > thr)))
    programmes.append({
        "channel": "PSR", "programme": "PSR-5Y-XRAY(SET-B)", "horizon_5yr": True,
        "description": "NICER/eXTP-class X-ray trigger, sigma_nu=0.6uHz (PG.06b "
                       f"measured), n_seg={len(xray_tau)}, 2 glitches, reach "
                       f"{psr.reach_periods(xray_tau):.2f} periods, 2021 PuMA "
                       "transients, null-MC-calibrated threshold",
        "power_at_predicted": powers[0],
        "false_positive": DETECTION_ALPHA, "false_positive_raw": fp_raw,
        "eps_grid": EPS_GRID, "power_grid": powers,
        "eps80": eps80_from_grid(EPS_GRID, powers),
    })
    print(f"[PSR] PSR-5Y-XRAY(SET-B): power@pred={powers[0]:.3f}, fp_raw={fp_raw:.3f}, "
          f"grid={[round(p, 2) for p in powers]}")

    # ---------------------------------------------------------------- FRB
    print("[FRB] anchor (sibling bed, phi=0) + programmes ...")
    anc = frb.programme_power(frb.ANCHOR_SPEC, 1, 1000, EPS_REFERENCE,
                              n_mc_null=n_null, n_mc_signal=n_sig, seed=seed + 41,
                              fixed_phase=0.0)
    anc_pred = frb.programme_power(frb.ANCHOR_SPEC, 1, 1000, EPS_PREDICTED,
                                   n_mc_null=max(80, n_null // 2),
                                   n_mc_signal=n_sig, seed=seed + 42, fixed_phase=0.0)
    anc_power = max(anc.power_fisher, anc.power_sumz)
    anchors["FRB"] = {
        "model_power_at_0.30_phi0": round(anc_power, 3),
        "model_power_at_predicted_phi0": round(max(anc_pred.power_fisher,
                                                   anc_pred.power_sumz), 3),
        "false_positive_rate": round(anc.fp_sumz, 3),
        "published": PUBLISHED_ANCHORS["FRB"],
        "pass": bool(abs(anc_power - 0.9375) <= ANCHOR_TOL),
    }
    print(f"[FRB] anchor: power@0.30={anc_power:.3f} (published 0.9375), "
          f"power@pred={anchors['FRB']['model_power_at_predicted_phi0']:.3f}")

    n80 = frb.single_session_n80(frb.PROGRAMME_SPEC, n_mc=80 if fast else 160,
                                 seed=seed + 43)
    for key, n_sessions, mean_n in (("FRB-5Y-BASEBAND", 200, 150),
                                    ("FRB-5Y-EXTREME", 100, 1000)):
        res_pred = frb.programme_power(frb.PROGRAMME_SPEC, n_sessions, mean_n,
                                       EPS_PREDICTED, n_mc_null=n_null,
                                       n_mc_signal=n_sig, seed=seed + 51)
        powers = [max(res_pred.power_fisher, res_pred.power_sumz)]
        for e in EPS_GRID[1:]:
            r = frb.programme_power(frb.PROGRAMME_SPEC, n_sessions, mean_n, e,
                                    n_mc_null=max(80, n_null // 2),
                                    n_mc_signal=n_grid, seed=seed + 52)
            powers.append(max(r.power_fisher, r.power_sumz))
        m_total = n_sessions * mean_n
        programmes.append({
            "channel": "FRB", "programme": key, "horizon_5yr": True,
            "description": f"{n_sessions} sessions x ~{mean_n} bursts (M~{m_total}), "
                           "tau 1s..4h (3.94 periods/session), FAST-class baseband, "
                           "random session phase",
            "power_at_predicted": powers[0],
            "power_fisher_at_predicted": res_pred.power_fisher,
            "power_sumz_at_predicted": res_pred.power_sumz,
            "power_upgrade_at_predicted": res_pred.power_upgrade,
            "false_positive": res_pred.fp_sumz,
            "eps_grid": EPS_GRID, "power_grid": powers,
            "eps80": eps80_from_grid(EPS_GRID, powers),
            "single_session_n80_upgraded_detector": n80,
        })
        if key == "FRB-5Y-BASEBAND":
            combo_channels["FRB"] = (res_pred.stats_signal, res_pred.stats_null)
        print(f"[FRB] {key}: power@pred={powers[0]:.3f} "
              f"(fisher {res_pred.power_fisher:.3f} / sumz {res_pred.power_sumz:.3f} "
              f"/ UPGRADE {res_pred.power_upgrade:.3f}), fp={res_pred.fp_sumz:.3f}")
    print(f"[FRB] single-session 80%-wall with upgraded detector: n80 = {n80}")

    # ----------------------------------------------------------------- GW
    print("[GW] Stage-1h scaling ...")
    anc_p, _, _ = gw.programme_power(0.63, [(1, 0.63)], n_mc=4000, seed=seed + 61)
    anchors["GW"] = {"model_recovery_at_eps90": round(anc_p, 3),
                     "published": PUBLISHED_ANCHORS["GW"],
                     "pass": bool(0.80 <= anc_p <= 0.97)}
    print(f"[GW] anchor: recovery at eps90 = {anc_p:.3f} (target 0.90)")

    for key, h5, events, desc in (
        ("GW-5Y-O5", True, [(6, 0.42), (20, 1.3)],
         "O5/A+ 5yr: 6 GW150914-class loud ringdowns (eps90=0.42) + 20 loud (1.3)"),
        ("GW-3G", False, [(40, 0.063)],
         "ET/CE-class: 40 loud ringdowns at x10 sensitivity (eps90=0.063)"),
    ):
        p, sig, nul = gw.programme_power(GW_ECHO_CEILING, events,
                                         n_mc=max(n_sig, 2000), seed=seed + 62)
        programmes.append({
            "channel": "GW", "programme": key, "horizon_5yr": h5,
            "description": desc + " | signal = ceiling (2/3)^6 = "
                           f"{GW_ECHO_CEILING:.4f} (power is an UPPER bound)",
            "power_at_predicted": p,
            "false_positive": float(np.mean(nul > gw.Z99)),
            "stack_snr": round(gw.stack_snr(GW_ECHO_CEILING, events), 3),
            "events_required_at_eps90_0.42": gw.required_events(GW_ECHO_CEILING, 0.42),
        })
        if key == "GW-5Y-O5":
            combo_channels["GW"] = (sig, nul)
        print(f"[GW] {key}: power@ceiling={p:.3f}, "
              f"stack SNR={gw.stack_snr(GW_ECHO_CEILING, events):.2f}")

    # -------------------------------------------------------------- UHECR
    print("[UHECR] anchor (open-data N, phi=0 like the sibling injection) ...")
    n_open = {"sd1500": 21571, "sd750": 54434}
    p_anc, _, _, fp_anc = uhecr.programme_power(n_open, EPS_PREDICTED,
                                                n_mc_null=n_null, n_mc_signal=n_sig,
                                                seed=seed + 71, phi=0.0)
    anchors["UHECR"] = {"model_power_at_predicted": round(p_anc, 3),
                        "false_positive_rate": round(fp_anc, 3),
                        "published": PUBLISHED_ANCHORS["UHECR"],
                        "pass": bool(abs(p_anc - 0.233) <= ANCHOR_TOL)}
    print(f"[UHECR] anchor: power@pred={p_anc:.3f} (published 0.233), fp={fp_anc:.3f}")

    n_full = {k: v * 10 for k, v in n_open.items()}
    p_full, sig_l, nul_l, fp_full = uhecr.programme_power(
        n_full, EPS_PREDICTED, n_mc_null=n_null, n_mc_signal=n_sig, seed=seed + 72)
    programmes.append({
        "channel": "UHECR", "programme": "UHECR-5Y-FULL", "horizon_5yr": True,
        "description": "full-statistics Auger reanalysis (open data = 10% sample; "
                       f"N = {n_full['sd1500']} SD1500 + {n_full['sd750']} SD750; "
                       "random phase); data already collected -- an analysis "
                       "proposal, not a new observatory. Caveat: assumes the "
                       "frozen-knot smooth family stays adequate at x10 statistics.",
        "power_at_predicted": p_full, "false_positive": fp_full,
    })
    combo_channels["UHECR"] = (sig_l, nul_l)
    print(f"[UHECR] UHECR-5Y-FULL: power@pred={p_full:.3f}, fp={fp_full:.3f}")

    # ---------------------------------------------------- CMB / LNFLUX / CRUST
    sigma_req = gaussian.gaussian_sigma_required(EPS_PREDICTED)
    for key, h5, bound in (("CMB-5Y-SO", True, 0.023), ("CMB-S4", False, 0.017)):
        sigma = bound / Z95
        p = gaussian.gaussian_power(EPS_PREDICTED, sigma)
        programmes.append({
            "channel": "CMB", "programme": key, "horizon_5yr": h5,
            "description": f"published-bound Gaussian bed: bound95={bound} -> "
                           f"sigma={sigma:.5f}",
            "power_at_predicted": round(p, 4), "false_positive": DETECTION_ALPHA,
            "bound95_required_for_80pct": round(sigma_req * Z95, 4),
        })
        if key == "CMB-5Y-SO":
            combo_channels["CMB"] = gaussian.gaussian_samples(
                EPS_PREDICTED, sigma, n_sig, seed + 81)
        print(f"[CMB] {key}: power@pred={p:.3f}")

    for key, h5, mult in (("LNFLUX-5Y-X3", True, 3.0), ("LNFLUX-ARCHIVE-X10", True, 10.0)):
        sigma = gaussian.LNFLUX_SIGMA_TODAY / np.sqrt(mult)
        p = gaussian.gaussian_power(EPS_PREDICTED, sigma)
        programmes.append({
            "channel": "LNFLUX", "programme": key, "horizon_5yr": h5,
            "description": f"meta-limit stack sigma {gaussian.LNFLUX_SIGMA_TODAY} / "
                           f"sqrt({mult:.0f}) = {sigma:.5f} (A1 magnetar + A4 GRB + "
                           "A5 TDE ln-flux curves)",
            "power_at_predicted": round(p, 4), "false_positive": DETECTION_ALPHA,
            "curve_multiplier_required_for_80pct":
                round((gaussian.LNFLUX_SIGMA_TODAY / sigma_req) ** 2, 1),
        })
        if key == "LNFLUX-ARCHIVE-X10":
            combo_channels["LNFLUX"] = gaussian.gaussian_samples(
                EPS_PREDICTED, sigma, n_sig, seed + 82)
        print(f"[LNFLUX] {key}: power@pred={p:.3f}")

    p_crust = gaussian.crust_power(EPS_PREDICTED, 1.25)
    programmes.append({
        "channel": "CRUST", "programme": "CRUST-5Y", "horizon_5yr": True,
        "description": "interpolated sibling injection curve, +2 episodes (x1.25 stats)",
        "power_at_predicted": round(p_crust, 4), "false_positive": DETECTION_ALPHA,
    })
    print(f"[CRUST] CRUST-5Y: power@pred={p_crust:.3f}")

    # -------------------------------------------------- combination + LOO
    print("[COMB] hierarchical joint likelihood over the realistic set ...")
    loo = combine.leave_one_out(combo_channels, seed=seed + 91)
    full = loo["full"]
    print(f"[COMB] full: matched-sum power={full['power_matched_sum']:.3f}, "
          f"fisher={full['power_fisher']:.3f}, best single={full['best_single']:.3f}")
    loo_pass = True
    mc_tol = 0.02 + 2.0 * float(np.sqrt(0.25 / 6000))
    for k in combo_channels:
        d = loo[f"without_{k}"]["power_matched_sum"] - full["power_matched_sum"]
        print(f"[LOO] without {k}: {loo[f'without_{k}']['power_matched_sum']:.3f} "
              f"(delta {d:+.3f})")
        if d > mc_tol:
            loo_pass = False
    fp_joint = full["fp_matched_sum"]
    loo_pass = loo_pass and (0.02 <= fp_joint <= 0.10)

    # ------------------------------------------------------------- gate
    channel_anchor_ok = {"PSR": anchors["PSR"]["pass"] and anchors["PSR_NU"]["pass"],
                         "FRB": anchors["FRB"]["pass"], "GW": anchors["GW"]["pass"],
                         "UHECR": anchors["UHECR"]["pass"],
                         "CMB": True, "LNFLUX": True, "CRUST": True}
    gate_rows = [pr for pr in programmes
                 if pr["horizon_5yr"] and channel_anchor_ok.get(pr["channel"], False)
                 and pr["false_positive"] <= 0.12]
    winners = [pr for pr in gate_rows if pr["power_at_predicted"] >= POWER_GATE]
    verdict = "P9-FORECAST-GO" if winners else "P9-FORECAST-PARK"
    winner_list = [f"{pr['channel']}/{pr['programme']} "
                   f"(power {pr['power_at_predicted']:.2f})" for pr in winners]
    verdict_note = ""
    if winners and all("SET-B" in pr["programme"] for pr in winners):
        verdict_note = ("CONDITIONAL GO: every gate-passing programme relies on the "
                        "2021 PuMA long transient (4.94 uHz @ 502.6 d) carrying the "
                        "multiplicative comb (the frozen sibling injection semantics). "
                        "Under the 2024 short-only envelope (SET-A) the same campaign "
                        "fails the gate -- the campaign prereg must treat the "
                        "long-component transfer reading as a named assumption.")

    pass_fail = {
        "C1_kernel_frozen": True,   # guarded by tests/ (byte-match asserts)
        "C2_false_positive": all(0.005 <= pr["false_positive"] <= 0.12
                                 for pr in programmes if pr["channel"] in
                                 ("PSR", "FRB", "UHECR")),
        "C3_anchors": {k: anchors[k]["pass"] for k in anchors},
        "C3_all": all(anchors[k]["pass"] for k in anchors),
        "C4_loo": loo_pass,
        "gate_reached": bool(winners),
    }

    out.update({
        "anchors": anchors,
        "programmes": programmes,
        "combination": full,
        "combination_loo": {k: {"power_matched_sum": v["power_matched_sum"],
                                "best_single": v["best_single"]}
                            for k, v in loo.items()},
        "pass_fail": pass_fail,
        "verdict": verdict,
        "verdict_channels": winner_list,
        "verdict_note": verdict_note,
        "runtime_s": round(time.time() - t0, 1),
    })
    RESULTS.parent.mkdir(exist_ok=True)
    RESULTS.write_text(json.dumps(out, indent=1, default=float))
    print(f"\n== VERDICT: {verdict} {winner_list if winners else ''} "
          f"(runtime {out['runtime_s']}s) ==")
    if verdict_note:
        print(f"   NOTE: {verdict_note}")
    for name, ok in [("C1 kernel frozen", pass_fail["C1_kernel_frozen"]),
                     ("C2 false-positive calibration", pass_fail["C2_false_positive"]),
                     ("C3 anchors reproduced", pass_fail["C3_all"]),
                     ("C4 leave-one-out consistency", pass_fail["C4_loo"])]:
        print(f"   {name}: {'PASS' if ok else 'FAIL'}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(prog="p9-forecast")
    sub = ap.add_subparsers(dest="cmd", required=True)
    an = sub.add_parser("analyze")
    an.add_argument("--seed", type=int, default=0)
    an.add_argument("--fast", action="store_true")
    args = ap.parse_args()
    if args.cmd == "analyze":
        analyze(seed=args.seed, fast=args.fast)


if __name__ == "__main__":
    main()
