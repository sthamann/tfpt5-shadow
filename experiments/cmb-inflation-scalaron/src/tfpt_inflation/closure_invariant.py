"""Reheating-free closure invariant: eliminate N_star from the scalaron read-offs.

The three Starobinsky read-offs

    n_s = 1 - 2/N,   r = 12/N^2,   A_s = N^2/(24 pi^2) c3^7

depend on the reheating input N_star ([C]).  Eliminating N gives three
EXACT, parameter-free relations (pure algebra, no new physics input):

    A_s * r              = c3^7 / (2 pi^2)              (product invariant)
    r                    = 3 (1 - n_s)^2                (consistency curve)
    alpha_s = dn_s/dlnk  = -2/N^2 = -r/6                (leading slow-roll order)

and the scalar-only closure invariant, testable with Planck alone:

    C_inf = 6 pi^2 A_s (1 - n_s)^2 / c3^7  =  1 .

Firewall: this is a consistency TYPING of published scalar parameters —
not a detection, never load-bearing.  The A_s--n_s covariance is NOT
modelled (Gaussian error propagation with cov=0, flagged in the output);
alpha_s is the leading-order Starobinsky running.  The r legs inherit the
[C] status of the R+R^2 -> P(k) bridge.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path

from . import constants

DATA = Path(__file__).resolve().parents[2] / "data" / "measurements.json"

# frozen product invariant A_s * r = c3^7/(2 pi^2)  (exact for every N)
K_ASR: float = constants.C3**7 / (2.0 * math.pi**2)   # 7.998181e-12

CONSISTENT_Z = 2.0


def r_from_ns(ns: float) -> float:
    """Exact N-elimination: r = 3 (1 - n_s)^2."""
    return 3.0 * (1.0 - ns) ** 2


def r_from_as(a_s: float) -> float:
    """Exact N-elimination: r = K_ASR / A_s."""
    return K_ASR / a_s


def closure(a_s: float, ns: float) -> float:
    """C_inf = 6 pi^2 A_s (1-n_s)^2 / c3^7 ; == 1 exactly on the TFPT curve."""
    return 6.0 * math.pi**2 * a_s * (1.0 - ns) ** 2 / constants.C3**7


def _exactness_guard() -> None:
    """The relations must be algebraically exact for every N (guards the freeze)."""
    for n in (50.0, 51.4, 56.0, 60.0):
        a_s = constants.a_s(n)
        ns = constants.n_s(n)
        rr = constants.r_tensor(n)
        assert abs(a_s * rr / K_ASR - 1.0) < 1e-12
        assert abs(rr / r_from_ns(ns) - 1.0) < 1e-12
        assert abs(closure(a_s, ns) - 1.0) < 1e-12


@dataclass
class ClosureResult:
    k_asr: float = K_ASR
    closure_checks: list[dict] = field(default_factory=list)
    r_pred: dict = field(default_factory=dict)
    ns_pred_checks: list[dict] = field(default_factory=list)
    alpha_s_check: dict = field(default_factory=dict)
    verdict: str = ""


def run_closure() -> ClosureResult:
    _exactness_guard()
    m = json.loads(DATA.read_text(encoding="utf-8"))
    res = ClosureResult()

    a_s = m["A_s"][0]
    as_v, as_s = a_s["value"], a_s["sigma"]

    # --- 1. scalar-only closure invariant C_inf vs 1 (per n_s measurement) ----
    for x in m["n_s"]:
        ns_v, ns_s = x["value"], x["sigma"]
        c = closure(as_v, ns_v)
        # Gaussian propagation, cov(A_s, n_s) = 0 (NOT modelled -> flagged)
        rel = math.sqrt((as_s / as_v) ** 2 + (2.0 * ns_s / (1.0 - ns_v)) ** 2)
        sig = c * rel
        z = (c - 1.0) / sig
        res.closure_checks.append({
            "experiment": x["experiment"], "A_s_source": a_s["experiment"],
            "C_inf": c, "sigma": sig, "z_vs_1": z,
            "consistent": abs(z) <= CONSISTENT_Z,
            "covariance_modelled": False,
        })

    # --- 2. N-free r prediction from A_s alone -------------------------------
    r_as = r_from_as(as_v)
    r_as_sig = r_as * as_s / as_v
    r_pred = {"r_from_As": r_as, "sigma": r_as_sig,
              "alpha_s_pred": -r_as / 6.0}
    for x in m["r_tensor"]:
        if "limit_95CL" in x:
            r_pred["limit_experiment"] = x["experiment"]
            r_pred["limit_95CL"] = x["limit_95CL"]
            r_pred["below_limit"] = r_as < x["limit_95CL"]
        elif "sigma_forecast" in x:
            r_pred["S4_detection_sigma"] = r_as / x["sigma_forecast"]
    res.r_pred = r_pred

    # --- 3. N-free n_s prediction from A_s alone -----------------------------
    ns_as = 1.0 - math.sqrt(r_as / 3.0)
    # d n_s / d A_s = (1/2) sqrt(r/3) / A_s
    ns_as_sig = 0.5 * math.sqrt(r_as / 3.0) * as_s / as_v
    for x in m["n_s"]:
        z = (ns_as - x["value"]) / math.hypot(x["sigma"], ns_as_sig)
        res.ns_pred_checks.append({
            "experiment": x["experiment"], "measured": x["value"], "sigma": x["sigma"],
            "ns_from_As": ns_as, "ns_from_As_sigma": ns_as_sig, "z": z,
            "consistent": abs(z) <= CONSISTENT_Z,
        })

    # --- 4. running alpha_s = -r/6 vs the measured running -------------------
    al = m["alpha_s"][0]
    alpha_pred = -r_as / 6.0
    z_al = (alpha_pred - al["value"]) / al["sigma"]
    res.alpha_s_check = {
        "experiment": al["experiment"], "measured": al["value"], "sigma": al["sigma"],
        "alpha_s_pred": alpha_pred, "z": z_al, "consistent": abs(z_al) <= CONSISTENT_Z,
    }

    c0 = res.closure_checks[0]
    all_ok = (all(c["consistent"] for c in res.closure_checks[:1])
              and res.alpha_s_check["consistent"]
              and r_pred.get("below_limit", False))
    res.verdict = (
        f"closure C_inf = {c0['C_inf']:.3f} +/- {c0['sigma']:.3f} vs 1 "
        f"({c0['z_vs_1']:+.2f} sigma, Planck n_s leg; A_s-n_s covariance NOT modelled); "
        f"N-free r = {r_as:.5f} +/- {r_as_sig:.5f} (below BK18; CMB-S4 "
        f"{r_pred.get('S4_detection_sigma', float('nan')):.1f} sigma decider); "
        f"alpha_s = -r/6 = {alpha_pred:.2e} vs measured "
        f"{al['value']:.4f} +/- {al['sigma']:.4f} ({z_al:+.2f} sigma). "
        f"{'CONSISTENT with the parameter-free TFPT curve' if all_ok else 'TENSION'} "
        f"-- typing only, not a detection; a robust future bound r < "
        f"{r_as - 2 * r_as_sig:.4f} kills this normalisation."
    )
    return res
