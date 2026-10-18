"""P9.COMB -- hierarchical joint likelihood over channels, and P9.LOO.

Each channel contributes empirical MC samples of its programme-level detection
statistic under the null and under the shared signal. Channels are
independent, so the joint null/signal distributions factorise and can be
resampled channel-wise.

Joint statistic (score form of the shared-eps joint likelihood):
    T = sum_c w_c * z_c,   z_c = (stat_c - mean_null_c) / sd_null_c,
with matched weights w_c = standardised expected signal shift of channel c
(the locally-optimal linear combination). Threshold MC-calibrated at
alpha = 0.05 on the joint null. Compared against Fisher p-value combination
(per-channel empirical p from the null ECDF) and the best single channel.

P9.LOO: leave-one-channel-out joint power + joint false-positive rate.
"""

from __future__ import annotations

import numpy as np

from .constants import DETECTION_ALPHA


def _standardise(sig: np.ndarray, nul: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    mu, sd = float(np.mean(nul)), float(np.std(nul) + 1e-12)
    zs, zn = (sig - mu) / sd, (nul - mu) / sd
    return zs, zn, float(np.mean(zs))


def _ecdf_p(x: np.ndarray, nul_sorted: np.ndarray) -> np.ndarray:
    idx = np.searchsorted(nul_sorted, x, side="left")
    return (1 + len(nul_sorted) - idx) / (len(nul_sorted) + 1.0)


def joint_power(channels: dict[str, tuple[np.ndarray, np.ndarray]], *,
                n_boot: int = 6000, seed: int = 0,
                exclude: tuple[str, ...] = ()) -> dict:
    """channels: name -> (signal samples, null samples). Returns joint power
    for the matched sum, Fisher combination, and the best single channel."""
    keys = [k for k in channels if k not in exclude]
    rng = np.random.default_rng(seed)
    Z = {}
    weights = {}
    for k in keys:
        zs, zn, w = _standardise(*channels[k])
        Z[k] = (zs, zn)
        weights[k] = max(w, 0.0)
    wsum = sum(weights.values()) or 1.0
    weights = {k: v / wsum for k, v in weights.items()}

    def resample(which: int) -> np.ndarray:
        # which: 0 = null, 1 = signal; returns (n_boot, n_channels) draws
        cols = []
        for k in keys:
            pool = Z[k][1] if which == 0 else Z[k][0]
            cols.append(rng.choice(pool, size=n_boot, replace=True))
        return np.column_stack(cols)

    null_draws = resample(0)
    sig_draws = resample(1)
    w = np.array([weights[k] for k in keys])

    T_null = null_draws @ w
    T_sig = sig_draws @ w
    thr = float(np.quantile(T_null, 1.0 - DETECTION_ALPHA))
    power_sum = float(np.mean(T_sig > thr))
    fp_sum = float(np.mean(T_null > thr))

    # Fisher on empirical per-channel p-values
    nul_sorted = {k: np.sort(channels[k][1]) for k in keys}
    def fisher_stat(draws: np.ndarray) -> np.ndarray:
        S = np.zeros(len(draws))
        for j, k in enumerate(keys):
            # de-standardise back to the raw statistic scale
            mu, sd = float(np.mean(channels[k][1])), float(np.std(channels[k][1]) + 1e-12)
            p = _ecdf_p(draws[:, j] * sd + mu, nul_sorted[k])
            S += -2.0 * np.log(np.clip(p, 1e-6, 1.0))
        return S
    F_null = fisher_stat(null_draws)
    F_sig = fisher_stat(sig_draws)
    thr_f = float(np.quantile(F_null, 1.0 - DETECTION_ALPHA))
    power_fisher = float(np.mean(F_sig > thr_f))

    # best single channel at the same alpha
    singles = {}
    for k in keys:
        zs, zn = Z[k]
        t = float(np.quantile(zn, 1.0 - DETECTION_ALPHA))
        singles[k] = float(np.mean(zs > t))
    best_single = max(singles.values()) if singles else 0.0

    return {"channels": keys, "weights": {k: round(weights[k], 4) for k in keys},
            "power_matched_sum": power_sum, "power_fisher": power_fisher,
            "fp_matched_sum": fp_sum, "best_single": best_single,
            "singles": {k: round(v, 4) for k, v in singles.items()}}


def leave_one_out(channels: dict[str, tuple[np.ndarray, np.ndarray]], *,
                  seed: int = 0) -> dict[str, dict]:
    out = {"full": joint_power(channels, seed=seed)}
    for k in channels:
        out[f"without_{k}"] = joint_power(channels, seed=seed, exclude=(k,))
    return out
