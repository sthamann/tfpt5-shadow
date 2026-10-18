"""``python -m eb_comb.cli {freeze-check,fetch,analyze}``"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

from . import analyze as an

DATA_URL = ("https://raw.githubusercontent.com/LilleJohs/"
            "Observed-EB-Power-Spectrum/main/HFI_f_sky_092_EB_o.npy")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="EB log-comb search (prereg v1)")
    ap.add_argument("command", choices=["freeze-check", "fetch", "analyze"])
    args = ap.parse_args(argv)

    if args.command == "freeze-check":
        sha = an.yaml_sha16()
        ok = sha == an.YAML_SHA16
        print(f"hypotheses SHA-16 = {sha} ({'OK' if ok else 'MISMATCH'})")
        print(f"frozen: omega_+ = {an.OMEGA_PLUS:.8f}, omega_- control = "
              f"{an.OMEGA_MINUS:.8f}, ell* = {an.ELL_STAR}, "
              f"eps candidate = {an.EPS_CANDIDATE}")
        import math
        reach = math.log(an.ELL_MAX / an.ELL_MIN) * an.OMEGA_PLUS / (2 * math.pi)
        print(f"reach = {reach:.3f} periods (gate {an.REACH_GATE} -> "
              f"{'SUB-GATE: no detection claim possible' if reach < an.REACH_GATE else 'ok'})")
        return 0 if ok else 1

    if args.command == "fetch":
        if an.DATA.exists():
            print(f"{an.DATA} exists -- refusing to re-fetch")
            return 1
        an.DATA.parent.mkdir(exist_ok=True)
        print(f"fetching {DATA_URL}")
        urllib.request.urlretrieve(DATA_URL, an.DATA)
        sha = hashlib.sha256(an.DATA.read_bytes()).hexdigest()
        print(f"wrote {an.DATA} ({an.DATA.stat().st_size} B), SHA-256 = {sha}")
        print("FIRST DATA CONTACT -- log this in the README")
        return 0

    if not an.DATA.exists():
        print("no data; run fetch first", file=sys.stderr)
        return 3
    out = an.analyze()
    fp, fm = out["fit_omega_plus"], out["fit_omega_minus"]
    print(f"data SHA-256 = {out['data']['sha256'][:16]}...")
    print(f"reach = {out['frozen']['reach_periods']} periods "
          f"(sub-gate: {out['frozen']['sub_gate']})")
    print(f"omega_+ = {an.OMEGA_PLUS:.6f}: dchi2 = {fp['dchi2']:.3f}, "
          f"A = {fp['A']:.4f}, p = {out['p_omega_plus']:.3f}")
    a95 = out["A95_omega_plus"]
    if a95 == a95 and a95 is not None:
        print(f"A_95(omega_+) = {a95:.4f}  "
              f"(eps candidate 0.0173 -> ratio {out['eps_vs_A95']:.2f})")
    else:
        print("A_95(omega_+) > 0.5 (no crossing below the frozen A cap -- "
              "the diagonal-error data cannot bound A at 95% here)")
    print(f"omega_- control: dchi2 = {fm['dchi2']:.3f}, "
          f"p = {out['p_omega_minus_control']:.3f}")
    print(f"LEE: rank of frozen omega = {out['lee']['rank_of_frozen']}/60, "
          f"p_global = {out['lee']['p_global']:.3f}")
    print(f"scramble control dchi2 = {out['scramble_dchi2']:.3f}")
    print(f"VERDICT: {out['verdict']}")
    print(f"wrote {an.RESULTS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
