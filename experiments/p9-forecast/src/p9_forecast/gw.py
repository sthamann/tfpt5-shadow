"""GW channel forecast: Stage-1h echo-limit scaling to programme catalogues.

The GW transfer target is NOT the 0.0173 comb (Stage 2 machine-checked that a
single monotone ringdown cannot carry it) but the first-echo amplitude
CEILING (2/3)^6 = 0.0878 relative to the fitted A220. Stage 1h measured
event-level 90% recovery limits eps90 (0.63 for GW200129, 0.69 for GW150914)
under the criterion p_raw = 0.01 / 90% recovery.

Gaussian matched-filter model (prereg): a template search at the predicted
lag has echo SNR = (eps_true / eps90_event) * SNR90 with
SNR90 = z(0.99) + z(0.90) = 3.608 -- by construction the anchor recovers
90% detection at eps = eps90 for a single event. An N-event coherent stack
adds SNR in quadrature. Detection: N(SNR_stack, 1) > z(0.99).

Computed power at eps_true = ceiling is an UPPER bound on the true power
(TFPT predicts <= ceiling).
"""

from __future__ import annotations

import numpy as np
from scipy.stats import norm

Z99 = float(norm.ppf(0.99))          # Stage-1h p_raw = 0.01
SNR90 = Z99 + float(norm.ppf(0.90))  # 3.608...


def stack_snr(eps_true: float, events: list[tuple[int, float]]) -> float:
    """Coherent-stack echo SNR for a catalogue [(n_events, eps90_event), ...]."""
    s2 = sum(n * (eps_true / e90 * SNR90) ** 2 for n, e90 in events)
    return float(np.sqrt(s2))


def programme_power(eps_true: float, events: list[tuple[int, float]], *,
                    n_mc: int, seed: int) -> tuple[float, np.ndarray, np.ndarray]:
    """(power, signal z samples, null z samples) for the stack detection."""
    rng = np.random.default_rng(seed)
    mu = stack_snr(eps_true, events)
    sig = rng.normal(mu, 1.0, n_mc)
    nul = rng.normal(0.0, 1.0, n_mc)
    return float(np.mean(sig > Z99)), sig, nul


def required_events(eps_true: float, eps90_event: float, *, power: float = 0.80,
                    alpha_z: float = Z99) -> int:
    """Events of one class needed for the target power (analytic Gaussian)."""
    z_pow = float(norm.ppf(power))
    need_snr = alpha_z + z_pow
    per_event = eps_true / eps90_event * SNR90
    return int(np.ceil((need_snr / per_event) ** 2))
