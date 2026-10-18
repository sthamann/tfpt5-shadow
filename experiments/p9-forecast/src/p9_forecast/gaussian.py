"""External-likelihood channels: Gaussian amplitude beds (CMB, LNFLUX) and the
interpolated crust-cooling injection curve.

CMB: the published log-oscillation bounds are one-sided 95% amplitude limits;
sigma = bound95 / z95. Power to detect eps at one-sided alpha=0.05:
    power = Phi(eps/sigma - z95).

LNFLUX: the comb-meta-limit HKSJ stack gives sigma_amp = 0.037658 today
(A1+A4+A5, k=3); a programme with an n_curves multiplier m scales
sigma -> sigma/sqrt(m).

CRUST: the sibling measured the injection power curve on the real sampling
{eps: power} = {0.02: 0.025, 0.05: 0.525, 0.15: 1.0}; we interpolate
log-linearly in eps and fold a statistics multiplier m as an effective
amplitude factor sqrt(m) (noncentrality scaling).
"""

from __future__ import annotations

import numpy as np
from scipy.stats import norm

from .constants import Z80, Z95

LNFLUX_SIGMA_TODAY = 0.037658          # comb-meta-limit results.json (HKSJ, k=3)
CRUST_CURVE = ((0.02, 0.025), (0.05, 0.525), (0.15, 1.0))


def gaussian_power(eps: float, sigma: float) -> float:
    return float(norm.cdf(eps / sigma - Z95))


def gaussian_sigma_required(eps: float, power: float = 0.80) -> float:
    """sigma needed for the target power (80% -> eps / (z95 + z80))."""
    return eps / (Z95 + float(norm.ppf(power)))


def gaussian_samples(eps: float, sigma: float, n: int,
                     seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    return rng.normal(eps / sigma, 1.0, n), rng.normal(0.0, 1.0, n)


def crust_power(eps: float, n_scale: float = 1.0) -> float:
    """Interpolated sibling injection power at effective eps*sqrt(n_scale)."""
    e = eps * float(np.sqrt(n_scale))
    xs = np.log([c[0] for c in CRUST_CURVE])
    ys = [c[1] for c in CRUST_CURVE]
    if e <= CRUST_CURVE[0][0]:
        # below the measured grid: scale the lowest measured point by the
        # Gaussian noncentrality ratio (conservative, floored at 0)
        return float(max(0.0, CRUST_CURVE[0][1] * (e / CRUST_CURVE[0][0]) ** 2))
    return float(np.interp(np.log(e), xs, ys))


REQUIRED_POWER_NOTE = f"80% power needs eps/sigma >= z95+z80 = {Z95 + Z80:.3f}"
