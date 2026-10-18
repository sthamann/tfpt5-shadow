"""The full rotation fingerprint of a constant birefringence angle beta_TFPT.

A uniform, frequency-independent rotation by beta (with vanishing primordial
TB/EB) fixes the ENTIRE spectral morphology, not just one angle:

    C_l^TB / C_l^TE                  = tan(2 beta)   (all l, all frequencies)
    2 C_l^EB / (C_l^EE - C_l^BB)     = tan(4 beta)   (all l, all frequencies)

plus five frozen null/sign properties of the TFPT global-seed reading:

    1. positive monopole of exactly beta = phi0/(4 pi) = 0.242435 deg
    2. frequency exponent n = 0            (beta_nu = beta_0 (nu/nu_0)^n)
    3. no anisotropic rotation             (C_L^{alpha alpha} = 0, L > 0)
    4. null alpha-T/E/B cross-correlations
    5. residual parity-odd spectra vanish after de-rotation:
           C_l^TB - tan(2 beta) C_l^TE                     = 0
           2 C_l^EB - tan(4 beta) (C_l^EE - C_l^BB)        = 0

Firewall: a consistency TYPING against published constraints — never a
detection.  Properties 2-4 cannot alone distinguish TFPT from LCDM (both
predict the nulls); they only KILL the seed reading if violated.  The
published legs share Planck data and calibration systematics, so NO joint
significance is formed.  The rotation-quotient / residual legs (the sharp
morphology test) need per-frequency PR4 EB/TB spectra and are typed
``not_yet_tested`` with frozen targets.  The internal-Z2 -> E/B parity
transduction is NOT proven (OBS.TRANSDUCTION.01), so everything here stays
exploratory.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path

from . import constants

DATA = Path(__file__).resolve().parents[2] / "data" / "measurements.json"

# ---- frozen fingerprint (all from c3; no measured input) ---------------------
TAN_2BETA: float = math.tan(2.0 * constants.BETA_RAD)   # C_l^TB / C_l^TE
TAN_4BETA: float = math.tan(4.0 * constants.BETA_RAD)   # 2 C_l^EB / (C_l^EE - C_l^BB)
FREQ_EXPONENT_PRED: float = 0.0                         # frequency-independent seed
ANISOTROPY_PRED: float = 0.0                            # C_L^{alpha alpha} = 0 (L>0)

CONSISTENT_Z = 2.0


@dataclass
class FingerprintResult:
    frozen: dict = field(default_factory=dict)
    legs: list[dict] = field(default_factory=list)
    verdict: str = ""


def _z_asymmetric(pred: float, value: float, sig_plus: float, sig_minus: float) -> float:
    """z of pred against an asymmetric-error measurement (side toward pred)."""
    sig = sig_plus if pred >= value else sig_minus
    return (pred - value) / sig


def run_fingerprint() -> FingerprintResult:
    m = json.loads(DATA.read_text(encoding="utf-8"))
    res = FingerprintResult()
    res.frozen = {
        "beta_deg": constants.BETA_DEG,
        "tan_2beta": TAN_2BETA,
        "tan_4beta": TAN_4BETA,
        "freq_exponent": FREQ_EXPONENT_PRED,
        "C_L_alphaalpha": ANISOTROPY_PRED,
        "residual_TB": "C_l^TB - tan(2b) C_l^TE = 0",
        "residual_EB": "2 C_l^EB - tan(4b) (C_l^EE - C_l^BB) = 0",
    }

    # --- leg 1: monopole magnitude AND sign (published beta fits) -------------
    for x in m["beta_birefringence_deg"]:
        if "SUPERSEDED" in x.get("note", ""):
            continue
        z = (constants.BETA_DEG - x["value"]) / x["sigma"]
        res.legs.append({
            "property": "monopole", "experiment": x["experiment"],
            "measured": x["value"], "sigma": x["sigma"], "predicted": constants.BETA_DEG,
            "z": z, "sign_matches": x["value"] > 0.0,
            "status": "consistent" if abs(z) <= CONSISTENT_Z and x["value"] > 0 else "tension",
        })

    # --- leg 2: frequency exponent n vs 0 --------------------------------------
    fx = m["beta_frequency_exponent"][0]
    z_n = _z_asymmetric(FREQ_EXPONENT_PRED, fx["value"], fx["sigma_plus"], fx["sigma_minus"])
    res.legs.append({
        "property": "frequency_exponent", "experiment": fx["experiment"],
        "measured": fx["value"], "sigma_plus": fx["sigma_plus"],
        "sigma_minus": fx["sigma_minus"], "predicted": FREQ_EXPONENT_PRED, "z": z_n,
        "status": "consistent" if abs(z_n) <= CONSISTENT_Z else "tension",
    })

    # --- leg 3: anisotropic rotation power (upper limit vs predicted 0) --------
    an = m["anisotropic_birefringence"][0]
    res.legs.append({
        "property": "anisotropy_null", "experiment": an["experiment"],
        "limit_95CL_deg2": an["A_CB_limit_95CL_deg2"], "predicted": ANISOTROPY_PRED,
        "status": "consistent_null",
        "note": "prediction 0 below the published bound; LCDM predicts the same "
                "null -> kill-only leg, no positive evidence",
    })

    # --- leg 4: alpha x T/E/B cross-correlations (published null) --------------
    xc = m["birefringence_cross_correlations"][0]
    res.legs.append({
        "property": "cross_correlation_null", "experiment": xc["experiment"],
        "L_max": xc["L_max"], "predicted": 0.0,
        "status": "consistent_null" if xc["compatible_with_null"] else "tension",
        "note": "kill-only leg (LCDM identical)",
    })

    # --- leg 5: rotation-quotient morphology + de-rotation residuals -----------
    res.legs.append({
        "property": "rotation_quotients", "experiment": "none yet",
        "target_TB_over_TE": TAN_2BETA, "target_2EB_over_EEmBB": TAN_4BETA,
        "status": "not_yet_tested",
        "note": "needs per-frequency PR4/NPIPE EB+TB spectra with splits, masks, "
                "beams and dust nulls frozen BEFORE data contact",
    })
    res.legs.append({
        "property": "derotation_residuals", "experiment": "none yet",
        "target": "both residual spectra = 0 at every l",
        "status": "not_yet_tested",
        "note": "distinguishes a late uniform rotation from genuinely parity-odd "
                "primordial physics; same data requirements as rotation_quotients",
    })

    n_cons = sum(1 for g in res.legs if g["status"].startswith("consistent"))
    n_open = sum(1 for g in res.legs if g["status"] == "not_yet_tested")
    n_bad = sum(1 for g in res.legs if g["status"] == "tension")
    res.verdict = (
        f"fingerprint typing: {n_cons} legs consistent, {n_open} not yet tested, "
        f"{n_bad} in tension. Frozen targets: beta = {constants.BETA_DEG:.6f} deg, "
        f"TB/TE = {TAN_2BETA:.8f}, 2EB/(EE-BB) = {TAN_4BETA:.8f}, n = 0, "
        f"C_L^aa = 0. Published legs share Planck data/calibration -> NO joint "
        f"significance claimed; nulls are kill-only (LCDM identical); the "
        f"Z2 -> E/B transduction is unproven (OBS.TRANSDUCTION.01) -> exploratory."
    )
    return res
