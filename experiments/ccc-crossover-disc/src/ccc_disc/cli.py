"""CLI of the preregistered CCC crossover-disc search.

Commands:
  freeze-check   recompute the three frozen kernel hashes (runs WITHOUT
                 data; this is the preregistration audit surface)
  analyze        the data pass -- NOT EXECUTED at the preregistered
                 stage; running it without maps prints the frozen
                 pipeline plan and exits with code 3.

Usage:
  PYTHONPATH=src python -m ccc_disc.cli freeze-check
  PYTHONPATH=src python -m ccc_disc.cli analyze --map <planck.fits>
"""

import argparse
import os
import sys

from . import kernel


def cmd_freeze_check():
    print("CCC crossover-disc search -- frozen kernel audit")
    print(f"  theta_max = {kernel.theta_max_deg():.4f} deg"
          " (= eta_rec/(eta_0 - eta_rec), typed externals)")
    print(f"  rate ratio Delta3/Delta2 = {kernel.RATE_RATIO:.6f}"
          " (= ln 3 / ln(3/2), exact)")
    print(f"  contrast bound across kappa band = "
          f"{kernel.contrast_bound():.3e} => template: causal top-hat")
    ok_all = True
    for name, (got, exp, ok) in kernel.freeze_status().items():
        print(f"  freeze {name}: recomputed {got}  expected {exp}"
              f"  [{'OK' if ok else 'MISMATCH'}]")
        ok_all &= ok
    print("FREEZE " + ("INTACT" if ok_all else "BROKEN"))
    return 0 if ok_all else 1


def cmd_analyze(args):
    if args.map and os.path.exists(args.map):
        from . import analyze
        analyze.run_analysis(args.map, os.path.join(
            os.path.dirname(__file__), "..", "..", "results",
            "results.json"))
        return 0
    if not args.map:
        print("PREREGISTERED STAGE -- no data pass has been run.")
        print("The frozen pipeline (to be executed only against the")
        print("hypotheses in hypotheses/ccc_disc_v1.yaml):")
        print("  1. input: Planck PR3 component-separated temperature")
        print("     maps (SMICA primary; Commander + NILC replication;")
        print("     half-mission splits), common mask.")
        print("  2. matched filter: sharp-edged top-hat discs, radius")
        print("     scan over the frozen band 1.0-1.3 deg ONLY.")
        print("  3. statistics: per-candidate amplitude + sign;")
        print("     sign-pairing test of the frozen defect-class table.")
        print("  4. nulls: Gaussian LCDM simulations (matched mask +")
        print("     beam), rotation shuffles, injection-recovery.")
        print("  5. decision: support requires BH-q < 0.01 AND")
        print("     replication across half-missions and >= 2 component")
        print("     separations; otherwise verdict enum per README.")
        return 3
    print("ERROR: the data pass is intentionally not implemented at the"
          " preregistered stage.", file=sys.stderr)
    return 3


def main():
    ap = argparse.ArgumentParser(prog="ccc_disc")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("freeze-check")
    ana = sub.add_parser("analyze")
    ana.add_argument("--map", default=None)
    ana.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    if args.cmd == "freeze-check":
        return cmd_freeze_check()
    return cmd_analyze(args)


if __name__ == "__main__":
    raise SystemExit(main())
