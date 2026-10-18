"""Faithful-class omega_minus typing (post sheetflip-bridge, 2026-08-27).

The character/bridge chain (doubletone_character_transduction_probe 10/10 +
sheetflip_skyparity_bridge_probe 13/13, experiments/tfpt-discovery) proves:
under a covariant (CPT-typed) coupling the parity-EVEN channels (TT/TE/EE)
carry only the even-sector tones

    omega_-   = 2 pi / ln(3^6)      = 0.953200   (bare Delta_-)
    omega_-/2 = 0.476600            (2 Delta_-)
    omega_+/2 = 1.291354            (2 Delta_+)

while the bare omega_+ = 2.5827 tone is FORBIDDEN in TT and lives in TB/EB.
This module types the omega_- (faithful-class TT) tone against the published
record and against the project's own frozen period gate.

Published coverage (new, 2025): the combined Planck + ACT DR6 + SPT-3G scan
(arXiv:2507.17276) uses the IDENTICAL template
P = P0 [1 + A_log cos(omega ln(k/k*) + phi)], pivot k* = 0.05/Mpc, with a
FLAT prior omega in [0, 100] -- unlike the old Planck-2018-X prior
(log10 omega in [0, 2.1]), this COVERS omega_- = 0.953: A_log < 0.0286
(95%, global), per-frequency 2-sigma limits consistently below 0.05, no
detection (omega unconstrained).

Structural reach result (machine-checked below): at omega_- the full Planck
likelihood window holds only ~1.15 comb periods (< the frozen 2.8 gate),
and even an optimistic single k-window [1e-4, 1] Mpc^-1 holds < 1.4 -- the
faithful-class TT tone is PERIOD-STARVED in every realistic window (an
S15-class structural statement: the theory predicts where it is hard to
see).  The faithful class's gate-passing home is TB/EB at omega_+ -- where
no published comb search exists at all (recorded).

Amplitude typing: the QT.02 amplitude eps = 0.0173 was frozen for the
omega_+ recovery comb; whether it carries to the even-sector omega_- tone
is OPEN -- eps is recorded as the candidate scale, flagged, not frozen.
"""

from __future__ import annotations

import math

DELTA_PLUS = math.log((3.0 / 2.0) ** 6)
DELTA_MINUS = math.log(3.0 ** 6)
OMEGA_MINUS = 2.0 * math.pi / DELTA_MINUS            # 0.953200
EVEN_TONES = {
    "omega_minus": OMEGA_MINUS,
    "omega_minus_half": 2.0 * math.pi / (2.0 * DELTA_MINUS),
    "omega_plus_half": 2.0 * math.pi / (2.0 * DELTA_PLUS),
}

# published 2025 combined scan covering omega < 1 (arXiv:2507.17276)
COMBINED_2025_OMEGA_PRIOR = (0.0, 100.0)             # flat, log template
COMBINED_2025_ALOG_95_GLOBAL = 0.0286
COMBINED_2025_ALOG_95_PERFREQ = 0.05                 # "consistently below"
EPS_CANDIDATE = math.exp(-math.pi ** 2 / DELTA_PLUS)  # flagged, NOT frozen

K_FULL = (1e-4, 0.2)                                 # Planck likelihood
K_OPTIMISTIC = (1e-4, 1.0)                           # CMB+LSS single window
REACH_GATE = 2.8                                     # frozen project gate


def periods_simple(k_window: tuple[float, float], gap: float) -> float:
    """ln-range divided by the comb period (= gap) in ln k."""
    return math.log(k_window[1] / k_window[0]) / gap


def analyze_omega_minus() -> dict:
    p_full = periods_simple(K_FULL, DELTA_MINUS)
    p_opt = periods_simple(K_OPTIMISTIC, DELTA_MINUS)
    p_full_2dp = periods_simple(K_FULL, 2.0 * DELTA_PLUS)
    covered = (COMBINED_2025_OMEGA_PRIOR[0] <= OMEGA_MINUS
               <= COMBINED_2025_OMEGA_PRIOR[1])
    below_global = EPS_CANDIDATE < COMBINED_2025_ALOG_95_GLOBAL
    below_perfreq = EPS_CANDIDATE < COMBINED_2025_ALOG_95_PERFREQ

    checks = {
        "omega_minus_inside_2025_flat_prior": covered,
        "reach_full_periods_omega_minus": round(p_full, 3),
        "reach_optimistic_periods_omega_minus": round(p_opt, 3),
        "reach_full_periods_omega_plus_half": round(p_full_2dp, 3),
        "gate_fails_everywhere": (p_full < REACH_GATE and p_opt < REACH_GATE
                                  and p_full_2dp < REACH_GATE),
        "eps_candidate_below_global_bound": below_global,
        "eps_candidate_below_perfreq_bound": below_perfreq,
    }
    verdict = "data_limited" if (covered and below_perfreq) else "tension"
    return {
        "module": "faithful_class_omega_minus (post sheetflip-bridge)",
        "frozen_tones_even_channel": {k: round(v, 6)
                                      for k, v in EVEN_TONES.items()},
        "published_coverage": {
            "source": "arXiv:2507.17276 (Planck+ACT DR6+SPT-3G, 2025)",
            "template": "P0 [1 + A_log cos(omega ln(k/k*) + phi)], "
                        "k* = 0.05/Mpc (identical class)",
            "omega_prior_flat": COMBINED_2025_OMEGA_PRIOR,
            "A_log_95_global": COMBINED_2025_ALOG_95_GLOBAL,
            "A_log_95_perfreq_ceiling": COMBINED_2025_ALOG_95_PERFREQ,
            "detection": "none (omega unconstrained)",
        },
        "amplitude_typing": {
            "eps_candidate": round(EPS_CANDIDATE, 6),
            "status": "OPEN -- QT.02 eps was frozen for the omega_+ comb; "
                      "carry-over to the even sector is not derived",
        },
        "checks": checks,
        "structural_note": (
            "omega_- is now COVERED by a published scan (flat prior) but "
            "PERIOD-STARVED: 1.15 periods in the full Planck window, "
            "< 1.4 even in an optimistic [1e-4, 1] Mpc^-1 window -- the "
            "frozen 2.8-period gate cannot be reached by any realistic "
            "single k-window (needs ~8 decades in k). The faithful "
            "class's gate-passing channel is TB/EB at omega_+ = 2.5827, "
            "where NO published comb search exists (open target)."),
        "verdict": verdict,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(analyze_omega_minus(), indent=2))
