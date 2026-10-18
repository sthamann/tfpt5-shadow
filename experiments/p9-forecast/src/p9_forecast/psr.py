"""PSR channel forecast: the sibling pulsar pipelines on synthetic triggered
campaigns.

Two detector readings of the SAME simulated campaign data, mirroring the two
sibling pipelines:

  * PHASE reading (PG.08 semantics): comb ripple on the transient nudot
    recovery integrated to phase -> time residuals; refit-absorption basis
    {1, tau, tau^2, exp(-tau/tau_d_i)} projected out; detect_comb on the
    residuals. (The phase integration smears the log-periodicity -- the honest
    property of this pipeline.)
  * NU reading (PG.06b/PG.07 semantics): local frequency estimates from
    adjacent-TOA phase differencing (the standard nu(t) product); whitened
    absorption projection in nu space; detect_comb on delta-nu(tau).

Noise model (prereg): white per-TOA sigma_toa + a phase RANDOM WALK. Two
calibrations against PG.08:
  * power-matched: rw step bisected so the J1740-3015 anchor reproduces its
    published injection power 0.50 at eps = 0.30 (found: white-only suffices);
  * rms-matched (conservative): rw step bisected so the simulated
    post-projection residual rms matches the published PG.08 rms
    (J1740: 684 us; Vela leg: 552 us).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .constants import DETECTION_ALPHA, EPS_PREDICTED, EPS_REFERENCE, LN_LAMBDA, OMEGA
from .detectors import detect_comb, fisher_p

DAY_S = 86400.0
N_FREQ = 200
P_FLOOR = 1.0 / (N_FREQ + 1)

# Vela transient sets (honesty band for the campaign signal envelope):
# SET_A -- 2024 public release (PG.07; 122-d window, short components only)
VELA_SET_A = ((1.5014095e-07, 15.115506), (1.2377972e-07, 2.4466279),
              (1.8532683e-07, 0.39430499))
# SET_B -- 2021 PuMA phase-connected glitch model (PG.08 par file; includes the
# 502-d component GLF0D_3 = 4.94 uHz, on which the frozen sibling injection
# semantics puts the same multiplicative ripple)
VELA_SET_B = ((3.0925245e-08, 6.3888889), (1.0056589e-07, 1.0030303),
              (4.9357251e-06, 502.64713))
VELA_F0 = 11.1861692


@dataclass(frozen=True)
class GlitchConfig:
    name: str
    f0_hz: float
    transients: tuple[tuple[float, float], ...]   # (GLF0D [Hz], GLTD [days])
    tau_days: tuple[float, ...]
    sigma_toa_us: float
    rw_step_us: float                             # random-walk step per sqrt(day)


def cadence_epochs(blocks: list[list[float]], rng: np.random.Generator) -> np.ndarray:
    taus: list[float] = []
    for lo, hi, per_day in blocks:
        n = max(2, int(round((hi - lo) * per_day)))
        base = np.linspace(lo, hi, n, endpoint=False)
        taus.extend(base + rng.uniform(0.0, (hi - lo) / n, n))
    return np.sort(np.array(taus))


def comb_phase_residual_us(tau_days: np.ndarray, transients: tuple[tuple[float, float], ...],
                           f0: float, eps: float, phi: float) -> np.ndarray:
    """Time residuals induced by the ripple on the transient recovery
    (identical to tfpt_pulsar.puma_iar.comb_phase_residual_us)."""
    if not transients:
        return np.zeros_like(tau_days)
    grid = np.geomspace(max(1e-4, tau_days.min() / 30.0), tau_days.max(), 4000)
    dnu = eps * np.cos(OMEGA * np.log(grid) + phi) * sum(
        a * np.exp(-grid / td) for a, td in transients)
    dphi = np.concatenate([[0.0], np.cumsum(0.5 * (dnu[1:] + dnu[:-1])
                                            * np.diff(grid) * DAY_S)])
    dphi_at = np.interp(tau_days, grid, dphi)
    return dphi_at / f0 * 1e6


def refit_projection(tau_days: np.ndarray, transients: tuple[tuple[float, float], ...],
                     y: np.ndarray, w: np.ndarray | None = None) -> np.ndarray:
    """Project out what a glitch-model refit would absorb (PG.08 semantics);
    optionally weighted (whitened) least squares."""
    cols = [np.ones_like(tau_days), tau_days, tau_days**2]
    cols += [np.exp(-tau_days / td) for _, td in transients if td > 0]
    X = np.column_stack(cols)
    if w is not None:
        Xw, yw = X * w[:, None], y * w
        beta, *_ = np.linalg.lstsq(Xw, yw, rcond=None)
    else:
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ beta


def noise_us(cfg: GlitchConfig, rng: np.random.Generator) -> np.ndarray:
    white = rng.normal(0.0, cfg.sigma_toa_us, len(cfg.tau_days))
    dts = np.diff(np.concatenate([[0.0], np.asarray(cfg.tau_days)]))
    rw = np.cumsum(rng.normal(0.0, cfg.rw_step_us * np.sqrt(np.clip(dts, 0.0, None))))
    return white + rw


# --------------------------------------------------------------- PHASE reading
def glitch_p_phase(cfg: GlitchConfig, eps: float, rng: np.random.Generator,
                   seed: int) -> float:
    tau = np.asarray(cfg.tau_days)
    phi = float(rng.uniform(0.0, 2.0 * np.pi))
    y = noise_us(cfg, rng) + comb_phase_residual_us(tau, cfg.transients, cfg.f0_hz,
                                                    eps, phi)
    y = refit_projection(tau, cfg.transients, y)
    _, p = detect_comb(tau, y, OMEGA, n_freq=N_FREQ, seed=seed)
    return p


# ------------------------------------------------------------------ NU reading
def glitch_p_nu(cfg: GlitchConfig, eps: float, rng: np.random.Generator,
                seed: int) -> float:
    """Adjacent-TOA phase differencing -> local nu(tau) estimates (uHz),
    whitened by the analytic per-pair noise, absorption-projected, then the
    same off-kernel rank detector."""
    tau = np.asarray(cfg.tau_days)
    phi = float(rng.uniform(0.0, 2.0 * np.pi))
    r_us = noise_us(cfg, rng) + comb_phase_residual_us(tau, cfg.transients,
                                                       cfg.f0_hz, eps, phi)
    dt_d = np.diff(tau)
    ok = dt_d > 1e-6
    # residual phase (cycles) = r(s) * F0; nu (Hz) = dphi / dt(s)
    dphi_cyc = np.diff(r_us) * 1e-6 * cfg.f0_hz
    nu_uhz = dphi_cyc / (dt_d * DAY_S) * 1e6
    tau_mid = 0.5 * (tau[1:] + tau[:-1])
    # analytic per-pair noise: white (2 sigma^2) + random walk (step^2 * dt)
    var_us2 = 2.0 * cfg.sigma_toa_us**2 + cfg.rw_step_us**2 * dt_d
    sigma_nu = np.sqrt(var_us2) * 1e-6 * cfg.f0_hz / (dt_d * DAY_S) * 1e6
    y = nu_uhz[ok] / sigma_nu[ok]
    tm = tau_mid[ok]
    # whitened absorption basis in nu space: {1, tau, tau^2, exp(-tau/tau_d)}
    cols = [np.ones_like(tm), tm, tm**2]
    cols += [np.exp(-tm / td) for _, td in cfg.transients if td > 0]
    X = np.column_stack(cols) / sigma_nu[ok][:, None]
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    y = y - X @ beta
    _, p = detect_comb(tm, y, OMEGA, n_freq=N_FREQ, seed=seed)
    return p


def campaign_power(cfgs: list[GlitchConfig], eps: float, *, reading: str,
                   n_mc: int, seed: int) -> tuple[float, np.ndarray]:
    """Power of a multi-glitch campaign (Fisher over glitches) + per-run
    Fisher-statistic samples. reading = 'phase' | 'nu'."""
    fn = glitch_p_phase if reading == "phase" else glitch_p_nu
    stats = np.empty(n_mc)
    hits = 0
    for k in range(n_mc):
        rng = np.random.default_rng(seed + 1009 * k)
        ps = [fn(c, eps, rng, seed=seed + 1009 * k + 7919 * (j + 1))
              for j, c in enumerate(cfgs)]
        pf = fisher_p(ps, P_FLOOR)
        stats[k] = -2.0 * float(np.sum(np.log(np.clip(ps, P_FLOOR, 1.0))))
        hits += int(pf < DETECTION_ALPHA)
    return hits / n_mc, stats


# ----------------------------------------------------------------- calibration
def calibrate_rw_power(anchor_cfg_fn, *, target: float = 0.50, tol: float = 0.15,
                       n_mc: int = 60, seed: int = 0) -> tuple[float, float]:
    """Bisect the rw step so the anchor reproduces the published power at
    eps = 0.30 (monotone decreasing). Returns (step, achieved power)."""
    def power_at(step: float) -> float:
        pw, _ = campaign_power([anchor_cfg_fn(step)], EPS_REFERENCE,
                               reading="phase", n_mc=n_mc, seed=seed)
        return pw

    lo, hi = 0.0, 4000.0
    pw_lo = power_at(lo)
    if pw_lo < target + 0.5 * tol:
        return lo, pw_lo
    step, pw = hi, power_at(hi)
    for _ in range(9):
        mid = 0.5 * (lo + hi)
        pw = power_at(mid)
        if abs(pw - target) <= 0.5 * tol:
            return mid, pw
        if pw > target:
            lo = mid
        else:
            hi = mid
        step = mid
    return step, pw


def calibrate_rw_rms(anchor_cfg_fn, *, target_rms_us: float, n_draws: int = 12,
                     seed: int = 0) -> float:
    """Bisect the rw step so the mean post-projection residual rms matches the
    published PG.08 rms (rms is monotone increasing in the step)."""
    def rms_at(step: float) -> float:
        cfg = anchor_cfg_fn(step)
        tau = np.asarray(cfg.tau_days)
        vals = []
        for k in range(n_draws):
            rng = np.random.default_rng(seed + 31 * k)
            y = refit_projection(tau, cfg.transients, noise_us(cfg, rng))
            vals.append(float(np.std(y)))
        return float(np.mean(vals))

    lo, hi = 0.0, 4000.0
    if rms_at(lo) >= target_rms_us:
        return lo
    for _ in range(24):
        mid = 0.5 * (lo + hi)
        if rms_at(mid) < target_rms_us:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ------------------------------------------------------------------ X-ray leg
def xray_glitch_p(transients: tuple[tuple[float, float], ...], tau: np.ndarray,
                  sigma_nu_uhz: float, eps: float, rng: np.random.Generator,
                  seed: int) -> float:
    """PG.06b semantics: direct nu(tau) segments (uHz) + white sigma_nu;
    absorption projection in nu space; off-kernel rank detector."""
    phi = float(rng.uniform(0.0, 2.0 * np.pi))
    signal = eps * np.cos(OMEGA * np.log(tau) + phi) * sum(
        a * np.exp(-tau / td) for a, td in transients) * 1e6
    y = signal + rng.normal(0.0, sigma_nu_uhz, len(tau))
    y = refit_projection(tau, transients, y)
    _, p = detect_comb(tau, y, OMEGA, n_freq=N_FREQ, seed=seed)
    return p


def xray_campaign_power(transients: tuple[tuple[float, float], ...], tau: np.ndarray,
                        sigma_nu_uhz: float, eps: float, n_glitches: int, *,
                        n_mc: int, seed: int) -> tuple[float, np.ndarray]:
    stats = np.empty(n_mc)
    hits = 0
    for k in range(n_mc):
        rng = np.random.default_rng(seed + 1009 * k)
        ps = [xray_glitch_p(transients, tau, sigma_nu_uhz, eps, rng,
                            seed=seed + 1009 * k + 7919 * (j + 1))
              for j in range(n_glitches)]
        pf = fisher_p(ps, P_FLOOR)
        stats[k] = -2.0 * float(np.sum(np.log(np.clip(ps, P_FLOOR, 1.0))))
        hits += int(pf < DETECTION_ALPHA)
    return hits / n_mc, stats


def calibrate_xray_slow_amp(tau: np.ndarray, sigma_nu_uhz: float, *,
                            eps_50: float = 0.55, tau_slow_d: float = 100.0,
                            n_mc: int = 48, seed: int = 0) -> tuple[float, float]:
    """PG.06b-2019 anchor: its slow-term amplitude was FITTED (no public
    model), so we invert it from the published injection curve: bisect the
    slow amplitude A (envelope A*exp(-tau/100d)) so that the detection power
    at the published eps_50 = 0.55 is ~0.50. Returns (A_uhz, power)."""
    def power_at(a_uhz: float) -> float:
        tr = ((a_uhz * 1e-6, tau_slow_d),)
        pw, _ = xray_campaign_power(tr, tau, sigma_nu_uhz, eps_50, 1,
                                    n_mc=n_mc, seed=seed)
        return pw

    lo, hi = 0.05, 50.0
    if power_at(hi) < 0.5:
        return hi, power_at(hi)
    for _ in range(10):
        mid = float(np.sqrt(lo * hi))
        pw = power_at(mid)
        if abs(pw - 0.5) <= 0.12:
            return mid, pw
        if pw < 0.5:
            lo = mid
        else:
            hi = mid
    return mid, pw


def reach_periods(tau_days: np.ndarray) -> float:
    t = np.asarray(tau_days)
    return float(np.log(t.max() / t.min()) / LN_LAMBDA)


__all__ = ["GlitchConfig", "VELA_SET_A", "VELA_SET_B", "VELA_F0", "cadence_epochs",
           "campaign_power", "calibrate_rw_power", "calibrate_rw_rms",
           "calibrate_xray_slow_amp", "comb_phase_residual_us", "refit_projection",
           "reach_periods", "xray_campaign_power", "EPS_PREDICTED", "P_FLOOR"]
