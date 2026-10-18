"""UHECR channel forecast: the uhecr-energy-dsi two-stage detector on
synthetic Auger-shaped spectra.

Mirrors tfpt_uhecr.analysis exactly: binned Poisson per array, piecewise-linear
log-density with knots FROZEN at the published features (0.16/5.0/12.6/45.7
EeV), smooth refit per draw, then one shared multiplicative comb (a, b) at the
frozen omega; statistic Lambda = 2(lnL_comb - lnL_smooth); detection at the
95th percentile of the null-Lambda distribution.

The synthetic bed is generated at the BINNED level, exactly like the
sibling's own MC/injection (mc_counts): expected counts mu0 lie INSIDE the
frozen-knot smooth family (piecewise power law with published indices
3.29 / 2.51 / 3.05 / 5.1 across the features, normalised to the programme's
event counts), and draws are Poisson(mu0 * (1 + eps cos(omega x + phi))).
Event-level sampling would put kink/bin-straddling misfit OUTSIDE the smooth
family and inflate Lambda linearly with N -- the sibling calibrates its null
with in-family draws, so the forecast must too. The ANCHOR (open-data counts
N = 21571 + 54434, phi = 0 like the sibling injection) must reproduce the
published power 0.233 +/- 0.20 at eps = 0.0173. Honest caveat: a real
full-statistics reanalysis must re-verify the knot family's adequacy
(real-spectrum misfit grows with N).
"""

from __future__ import annotations

import math

import numpy as np

from .constants import OMEGA

KNOTS_EEV = (0.16, 5.0, 12.6, 45.7)
# d ln(dN/dx) / dx slopes between features (x = ln E), from published indices
SLOPES = (-2.0, -2.29, -1.51, -2.05, -4.1)
ARRAYS = {"sd1500": {"lo": 2.5, "hi": 144.0},
          "sd750": {"lo": 0.1, "hi": 35.0}}
N_BINS = 200


def _logdensity(x: np.ndarray) -> np.ndarray:
    """Piecewise-linear log-density at x = ln E (published-index slopes with
    breaks exactly at the frozen knots) -- INSIDE the smooth fit family."""
    kx = np.array([math.log(k) for k in KNOTS_EEV])
    out = SLOPES[0] * x
    for i, k in enumerate(kx):
        out = out + (SLOPES[i + 1] - SLOPES[i]) * np.clip(x - k, 0.0, None)
    return out


# ------------------------------------------------------- two-stage (mirrored)
def _design(x_centres: np.ndarray, knots_x: np.ndarray) -> np.ndarray:
    cols = [np.ones_like(x_centres), x_centres]
    cols += [np.clip(x_centres - k, 0.0, None) for k in knots_x]
    return np.column_stack(cols)


def _fit_poisson(counts: np.ndarray, A: np.ndarray, n_iter: int = 200) -> np.ndarray:
    beta = np.zeros(A.shape[1])
    beta[0] = math.log(max(counts.mean(), 0.1))
    for _ in range(n_iter):
        mu = np.exp(np.clip(A @ beta, -30, 30))
        g = A.T @ (counts - mu)
        H = (A * mu[:, None]).T @ A + 1e-9 * np.eye(A.shape[1])
        step = np.linalg.solve(H, g)
        beta += step
        if np.max(np.abs(step)) < 1e-10:
            break
    return beta


def _loglik(counts: np.ndarray, mu: np.ndarray) -> float:
    mu = np.clip(mu, 1e-12, None)
    return float(np.sum(counts * np.log(mu) - mu))


class Bed:
    """Fixed binning + design matrices + in-family expected counts."""

    def __init__(self) -> None:
        self.arrays = {}
        for name, cfg in ARRAYS.items():
            lo, hi = math.log(cfg["lo"]), math.log(cfg["hi"]) + 1e-9
            edges = np.linspace(lo, hi, N_BINS + 1)
            centres = 0.5 * (edges[:-1] + edges[1:])
            knots = np.array([math.log(k) for k in KNOTS_EEV if lo < math.log(k) < hi])
            dens = np.exp(_logdensity(centres))
            self.arrays[name] = {"edges": edges, "centres": centres,
                                 "A": _design(centres, knots),
                                 "shape": dens / dens.sum()}

    def counts(self, n_events: dict[str, int], eps: float, rng: np.random.Generator,
               phi: float | None = None) -> dict[str, np.ndarray]:
        """Poisson draws from mu0 * (1 + eps cos(omega x + phi)); mu0 lies in
        the smooth family (mirrors the sibling's mc_counts + injection;
        phi = 0.0 mirrors its fixed-phase injection, None marginalises)."""
        if phi is None:
            phi = float(rng.uniform(0.0, 2.0 * np.pi))
        out = {}
        for name, arr in self.arrays.items():
            mu0 = n_events[name] * arr["shape"]
            f = 1.0 + eps * np.cos(OMEGA * arr["centres"] + phi) if eps else 1.0
            out[name] = rng.poisson(mu0 * f).astype(float)
        return out

    def lam(self, counts: dict[str, np.ndarray], omega: float = OMEGA) -> float:
        """Smooth refit + shared-comb Lambda (mirrors TwoStage.lam)."""
        mu0 = {n: np.exp(np.clip(a["A"] @ _fit_poisson(counts[n], a["A"]), -30, 30))
               for n, a in self.arrays.items()}
        ab = np.zeros(2)
        for _ in range(60):
            g = np.zeros(2)
            H = np.zeros((2, 2)) + 1e-9 * np.eye(2)
            for n, arr in self.arrays.items():
                ph = omega * arr["centres"]
                B = np.column_stack([np.cos(ph), np.sin(ph)])
                f = np.clip(1.0 + B @ ab, 1e-3, None)
                mu = mu0[n] * f
                g += B.T @ ((counts[n] - mu) / f)
                H += (B * (mu / f**2)[:, None]).T @ B
            step = np.linalg.solve(H, g)
            ab += step
            if np.max(np.abs(step)) < 1e-12:
                break
        ll0 = ll1 = 0.0
        for n, arr in self.arrays.items():
            ph = omega * arr["centres"]
            f = np.clip(1.0 + ab[0] * np.cos(ph) + ab[1] * np.sin(ph), 1e-3, None)
            ll0 += _loglik(counts[n], mu0[n])
            ll1 += _loglik(counts[n], mu0[n] * f)
        return 2.0 * (ll1 - ll0)


def programme_power(n_events: dict[str, int], eps: float, *, n_mc_null: int,
                    n_mc_signal: int, seed: int, phi: float | None = None
                    ) -> tuple[float, np.ndarray, np.ndarray, float]:
    """(power, signal Lambda samples, null Lambda samples, fp_rate).
    phi = 0.0 mirrors the sibling's fixed-phase injection (anchor);
    phi = None marginalises the unknown phase (programme forecast)."""
    bed = Bed()
    rng = np.random.default_rng(seed)
    nul = np.array([bed.lam(bed.counts(n_events, 0.0, rng)) for _ in range(n_mc_null)])
    thr = float(np.quantile(nul, 0.95))
    sig = np.array([bed.lam(bed.counts(n_events, eps, rng, phi=phi))
                    for _ in range(n_mc_signal)])
    return float(np.mean(sig >= thr)), sig, nul, float(np.mean(nul >= thr))
