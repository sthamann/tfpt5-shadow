"""Shared comb detectors, byte-compatible with the sibling searches.

Two detector families are reused unchanged (no new statistics are invented
for the forecast -- the point is to forecast the power of the EXISTING
pipelines):

  * curve detector (PG.05/PG.07/PG.08 / recovery-comb-domains): fractional
    variance the cos/sin(omega ln t) pair explains on top of a degree-2
    polynomial-in-ln(t) baseline, ranked against off-kernel log-frequencies
    on the SAME curve (self-calibrating periodogram rank);
  * point-process detector (RC.02 / repeater-cascade): Rayleigh power
    z(omega) of the burst phases omega*ln(tau), calibrated against the
    session's smooth rate envelope (rate-preserving surrogate null).
"""

from __future__ import annotations

import numpy as np

from .constants import OMEGA

DETREND_DEG = 2


def comb_gain(lt: np.ndarray, y: np.ndarray, omega: float,
              deg: int = DETREND_DEG) -> float:
    """Fractional variance the cos/sin(omega ln t) pair explains on top of a
    polynomial baseline (identical to tfpt_pulsar.nu_recovery._comb_gain)."""
    P = np.vander(lt, deg + 1)
    b0, *_ = np.linalg.lstsq(P, y, rcond=None)
    ss0 = float(np.sum((y - P @ b0) ** 2))
    X = np.column_stack([P, np.cos(omega * lt), np.sin(omega * lt)])
    b1, *_ = np.linalg.lstsq(X, y, rcond=None)
    ss1 = float(np.sum((y - X @ b1) ** 2))
    return max(0.0, (ss0 - ss1) / (ss0 + 1e-12))


def comb_gain_bank(lt: np.ndarray, y: np.ndarray, freqs: np.ndarray,
                   deg: int = DETREND_DEG) -> np.ndarray:
    """Vectorised comb gains at many frequencies (algebraically identical to
    per-frequency ``comb_gain``): project the cos/sin pair onto the orthogonal
    complement of the polynomial baseline, then a 2x2 solve per frequency."""
    P = np.vander(lt, deg + 1)
    Q, _ = np.linalg.qr(P)
    r0 = y - Q @ (Q.T @ y)
    ss0 = float(r0 @ r0) + 1e-12
    ph = np.outer(freqs, lt)                     # (F, n)
    C = np.stack([np.cos(ph), np.sin(ph)], axis=2)          # (F, n, 2)
    QtC = np.einsum("nk,fnj->fkj", Q, C)                    # (F, q, 2)
    Ct = C - np.einsum("nk,fkj->fnj", Q, QtC)               # residualised pair
    G = np.einsum("fni,fnj->fij", Ct, Ct)                   # (F, 2, 2)
    b = np.einsum("fni,n->fi", Ct, r0)                      # (F, 2)
    G += 1e-12 * np.eye(2)[None, :, :]
    sol = np.linalg.solve(G, b[:, :, None])[:, :, 0]
    explained = np.einsum("fi,fi->f", b, sol)
    return np.clip(explained / ss0, 0.0, None)


def detect_comb(tau: np.ndarray, rec: np.ndarray, omega: float = OMEGA, *,
                deg: int = DETREND_DEG, n_freq: int = 200,
                seed: int = 0) -> tuple[float, float]:
    """Off-kernel periodogram rank p of the comb gain at ``omega`` (identical
    construction to tfpt_pulsar.nu_recovery.detect_comb; vectorised bank)."""
    m = tau > 0
    lt, y = np.log(tau[m]), rec[m]
    if len(lt) < 6:
        return 0.0, 1.0
    ln_range = float(lt.max() - lt.min()) or 1.0
    f_lo = max(0.9, 2.0 * np.pi / ln_range)
    rng = np.random.default_rng(seed)
    fs = rng.uniform(f_lo, max(6.0, 2.5 * omega), n_freq)
    fs = fs[np.abs(fs - omega) > 0.1 * omega]
    gains = comb_gain_bank(lt, y, np.concatenate([[omega], fs]), deg)
    g0, null = float(gains[0]), gains[1:]
    p = float((1 + np.sum(null >= g0)) / (len(null) + 1))
    return g0, p


def rayleigh_z(u: np.ndarray, w: float) -> float:
    """Rayleigh power z(w) = |sum exp(i w u)|^2 / n (RC.02 statistic)."""
    ph = np.exp(1j * w * u)
    return float(np.abs(ph.sum()) ** 2 / len(u))


def fisher_p(pvals: list[float], p_floor: float) -> float:
    """Fisher combination with the discrete-floor guard used by the siblings."""
    from scipy.stats import chi2

    p = np.clip(np.asarray(pvals, dtype=float), p_floor, 1.0)
    if len(p) == 0:
        return float("nan")
    stat = -2.0 * np.sum(np.log(p))
    return float(chi2.sf(stat, df=2 * len(p)))
