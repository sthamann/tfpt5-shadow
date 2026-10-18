"""``tfpt-inflation analyze`` -- Starobinsky/scalaron n_s, r, A_s vs CMB data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import constants
from .branch_resolver import resolve as resolve_branch
from .closure_invariant import run_closure
from .inflation_test import run_inflation

RESULTS = Path(__file__).resolve().parents[2] / "results"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="TFPT Starobinsky/scalaron inflation vs CMB")
    ap.add_argument("command", choices=["audit", "analyze"], nargs="?", default="analyze")
    args = ap.parse_args(argv)

    print("=" * 72)
    print("TFPT Starobinsky/scalaron inflation (R+R^2; M_scal = c3^{7/2} Mbar)")
    print("=" * 72)
    c = constants.summary()
    print(f"  M_scal = {c['M_scal_GeV']:.3e} GeV ; N_star point = {c['N_star_point']}")
    print(f"  n_s = 1-2/N_star: point {c['n_s_point']:.4f}, band {c['n_s_band']}")
    print(f"  r   = 12/N_star^2: point {c['r_point']:.4f}, band {c['r_band']}")
    print(f"  A_s = N_star^2/(24pi^2) c3^7: point {c['A_s_point']:.3e}")
    if args.command == "audit":
        return 0

    r = run_inflation()
    print("\n[n_s]")
    for ch in r.n_s_checks:
        print(f"    {ch['measured']:.4f}+/-{ch['sigma']:.4f} vs {ch['tfpt']:.4f} -> "
              f"{ch['z']:+.2f} sigma ({'ok' if ch['consistent'] else 'tension'})  {ch['experiment']}")
    print("\n[r]")
    for ch in r.r_checks:
        if "limit_95CL" in ch:
            print(f"    TFPT {ch['tfpt']:.4f} vs <{ch['limit_95CL']} (95%CL) -> "
                  f"{'below (ok)' if ch['below_limit'] else 'ABOVE'}  {ch['experiment']}")
        else:
            print(f"    TFPT {ch['tfpt']:.4f}; forecast sigma_r={ch['sigma_forecast']:.0e} -> "
                  f"{ch['detection_sigma']:.0f} sigma detectability  {ch['experiment']}")
    print("\n[A_s]")
    a = r.a_s_check
    print(f"    point {a['tfpt_point']:.3e} vs {a['measured']:.2e}+/-{a['sigma']:.0e} -> "
          f"{a['z_point']:+.1f} sigma; A_s-preferred N_star = {r.a_s_preferred_n_star:.1f}")
    print(f"\n-> {r.verdict}")

    br = resolve_branch()
    print("\n[branch_resolver]")
    print(f"    fixed  N*=51.4: n_s={br.fixed['n_s']:.4f}, r={br.fixed['r']:.4f}, "
          f"A_s {br.fixed['z_A_s_planck']:+.1f}s -> {br.fixed['status']}")
    print(f"    profiled N*={br.profiled['N_star_from_A_s']:.1f}: n_s={br.profiled['n_s']:.4f} "
          f"({br.profiled['z_n_s_planck']:+.1f}s Planck), r={br.profiled['r']:.4f} -> "
          f"{br.profiled['status']}")
    print("    Bayes factor ln(B_profiled/fixed):")
    for exp, b in br.bayes.items():
        print(f"      {b['ln_bayes_factor_BA']:+8.1f}  ({b['preferred']})  {exp}")
    s4 = br.s4_forecast
    print(f"    CMB-S4: r_point={s4['r_point']:.4f} -> {s4['S4_detection_sigma_point']:.0f} sigma "
          f"(sigma_r={s4['sigma_r_S4']:.0e})")
    print(f"    -> {br.decision}")

    # ---- reheating-free closure invariant: N_star eliminated -----------------
    ci = run_closure()
    print("\n[closure_invariant]  N_star eliminated: A_s*r = c3^7/(2pi^2), "
          "r = 3(1-n_s)^2, alpha_s = -r/6")
    print(f"    frozen product A_s*r = c3^7/(2pi^2) = {ci.k_asr:.6e}")
    for ch in ci.closure_checks:
        print(f"    C_inf = {ch['C_inf']:.4f} +/- {ch['sigma']:.4f} vs 1 -> "
              f"{ch['z_vs_1']:+.2f} sigma ({'ok' if ch['consistent'] else 'tension'})  "
              f"[n_s: {ch['experiment']}; cov(A_s,n_s) NOT modelled]")
    rp = ci.r_pred
    print(f"    N-free r(A_s) = {rp['r_from_As']:.5f} +/- {rp['sigma']:.5f}  "
          f"({rp['limit_experiment']} <{rp['limit_95CL']}: "
          f"{'below (ok)' if rp['below_limit'] else 'ABOVE'}; "
          f"CMB-S4 {rp['S4_detection_sigma']:.1f} sigma)")
    for ch in ci.ns_pred_checks:
        print(f"    N-free n_s(A_s) = {ch['ns_from_As']:.4f} vs "
              f"{ch['measured']:.4f}+/-{ch['sigma']:.4f} -> {ch['z']:+.2f} sigma "
              f"({'ok' if ch['consistent'] else 'tension'})  {ch['experiment']}")
    ac = ci.alpha_s_check
    print(f"    alpha_s = -r/6 = {ac['alpha_s_pred']:.2e} vs "
          f"{ac['measured']:.4f}+/-{ac['sigma']:.4f} -> {ac['z']:+.2f} sigma "
          f"({'ok' if ac['consistent'] else 'tension'})  {ac['experiment']}")
    print(f"    -> {ci.verdict}")

    RESULTS.mkdir(exist_ok=True)
    out = {"constants": c, "n_s_checks": r.n_s_checks, "r_checks": r.r_checks,
           "a_s_check": r.a_s_check, "a_s_preferred_n_star": r.a_s_preferred_n_star,
           "verdict": r.verdict,
           "closure_invariant": {"k_asr": ci.k_asr, "closure_checks": ci.closure_checks,
                                 "r_pred": ci.r_pred, "ns_pred_checks": ci.ns_pred_checks,
                                 "alpha_s_check": ci.alpha_s_check, "verdict": ci.verdict},
           "branch_resolver": {"fixed": br.fixed, "profiled": br.profiled,
                               "bayes": br.bayes, "s4_forecast": br.s4_forecast,
                               "decision": br.decision}}
    (RESULTS / "results.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\nWrote {RESULTS / 'results.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
