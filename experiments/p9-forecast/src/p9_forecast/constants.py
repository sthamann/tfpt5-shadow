"""Frozen TFPT kernel + forecast gate constants for the P9-FORECAST slice.

Everything kernel-side is *derived* from the two TFPT axioms (identical to
``verification/tfpt_constants.py`` and every sibling comb search):

    P1   c3    = 1 / (8*pi)          seam / boundary constant
    P2   g_car = 5                   carrier rank

No fitted number enters. The values must match
``hypotheses/p9_forecast_v1.yaml`` byte-for-byte (guarded in tests/).
"""

from __future__ import annotations

import math

PI: float = math.pi
C3: float = 1.0 / (8.0 * PI)                              # P1
G_CAR: int = 5                                            # P2

N_FAM: int = 3
P2_EXP: int = 6                                           # |R^+(A_3)| transport-cycle exponent

LAMBDA_CASCADE: float = 1.5**P2_EXP                       # (3/2)^6 = 11.390625
LN_LAMBDA: float = math.log(LAMBDA_CASCADE)               # 2.4327906486489863
OMEGA: float = 2.0 * PI / LN_LAMBDA                       # 2.5827069463082895
EPS_PREDICTED: float = math.exp(-PI**2 / LN_LAMBDA)       # 0.01730246011431484
GW_ECHO_CEILING: float = (2.0 / 3.0) ** 6                 # 0.08779149519890261
REACH_GATE_PERIODS: float = 2.8                           # PG.06 machine-checked gate
EPS_REFERENCE: float = 0.30                               # sibling injection reference

# forecast protocol (prereg-frozen, NOT kernel-derived)
DETECTION_ALPHA: float = 0.05                             # sibling P_THRESHOLD
POWER_GATE: float = 0.80                                  # the strategy-council gate
N_MC_NULL: int = 400
N_MC_SIGNAL: int = 240
Z95: float = 1.6448536269514722                           # Phi^-1(0.95)
Z80: float = 0.8416212335729143                           # Phi^-1(0.80)


def summary() -> dict[str, float]:
    return {
        "c3": C3, "g_car": float(G_CAR), "N_fam": float(N_FAM),
        "lambda=(3/2)^6": LAMBDA_CASCADE, "omega=2pi/ln(lambda)": OMEGA,
        "eps_predicted": EPS_PREDICTED, "gw_echo_ceiling=(2/3)^6": GW_ECHO_CEILING,
        "reach_gate_periods": REACH_GATE_PERIODS, "eps_reference": EPS_REFERENCE,
        "detection_alpha": DETECTION_ALPHA, "power_gate": POWER_GATE,
    }
