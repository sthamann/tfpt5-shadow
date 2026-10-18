"""FRB channel forecast: the RC.02 detector on synthetic baseband campaigns.

Session bed (RC construction): n bursts per session, arrival log-times
u = ln(tau) drawn from a smooth exponential-tilt envelope; comb signal =
thinning by (1 + eps cos(omega u + phi)).

ANCHOR bed mirrors the sibling validation byte-for-byte in its physics:
rate ~ tau^-0.8 on [0.3 s, 5400 s] (density tilt +0.2 in u = ln tau),
N = 1000, injection phase FIXED at phi = 0 (the sibling's construction) --
published power 0.9375 at eps = 0.30.

PROGRAMME beds use a random phase per session (a real campaign does not know
the onset phase) and tilt +0.3 over [1 s, 4 h].

Detector (frozen, sibling RC.02): Rayleigh z at omega, null = rate-preserving
surrogate bank (envelope known by construction; amortised per burst-count).
The dominant power limit is ENVELOPE LEAKAGE: the smooth session envelope
contributes n*|c_env(omega)|^2 to z, and its random-phase interference with
the signal vector dominates the variance -- this is the physical content of
the RC 'amplitude wall'.

Proposed-upgrade statistic (reported separately, NOT the frozen detector):
envelope-subtracted matched filter z' = |R - n c_env|^2 / n, which removes
the leakage term. In the forecast bed c_env is exact; a real implementation
must estimate it per session (surrogate mean), so the upgrade numbers are a
best case.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .constants import DETECTION_ALPHA, EPS_PREDICTED, OMEGA
from .detectors import fisher_p

N_BANK = 2000
P_FLOOR = 1.0 / (N_BANK + 1)


@dataclass(frozen=True)
class SessionSpec:
    tau_min_s: float
    tau_max_s: float
    tilt: float                    # d ln(density) / d u,  u = ln tau

    @property
    def u_lo(self) -> float:
        return float(np.log(self.tau_min_s))

    @property
    def u_hi(self) -> float:
        return float(np.log(self.tau_max_s))

    def c_env(self, omega: float = OMEGA) -> complex:
        """Exact envelope Fourier coefficient E[exp(i omega u)]."""
        a = self.tilt
        lo, hi = self.u_lo, self.u_hi
        num = (np.exp((a + 1j * omega) * hi) - np.exp((a + 1j * omega) * lo)) / (a + 1j * omega)
        den = (np.exp(a * hi) - np.exp(a * lo)) / a
        return complex(num / den)


ANCHOR_SPEC = SessionSpec(0.3, 5400.0, 0.2)      # sibling validation bed
PROGRAMME_SPEC = SessionSpec(1.0, 14400.0, 0.3)


def draw_session_u(spec: SessionSpec, n: int, eps: float,
                   rng: np.random.Generator, phi: float | None = None) -> np.ndarray:
    """n burst log-times from the tilted envelope, comb-thinned.
    phi = None -> random session phase; phi = 0.0 mirrors the sibling anchor."""
    lo, hi = spec.u_lo, spec.u_hi
    if phi is None:
        phi = float(rng.uniform(0.0, 2.0 * np.pi))
    a = spec.tilt
    out = np.empty(n)
    filled = 0
    while filled < n:
        m = 2 * (n - filled) + 16
        r = rng.uniform(0.0, 1.0, m)
        u = np.log(np.exp(a * lo) + r * (np.exp(a * hi) - np.exp(a * lo))) / a
        if eps > 0.0:
            keep = rng.uniform(0.0, 1.0, m) < (1.0 + eps * np.cos(OMEGA * u + phi)) / (1.0 + eps)
            u = u[keep]
        take = min(len(u), n - filled)
        out[filled:filled + take] = u[:take]
        filled += take
    return out


def _z_pair(u: np.ndarray, c_env: complex) -> tuple[float, float]:
    """(frozen Rayleigh z, envelope-subtracted z') for one session."""
    n = len(u)
    R = np.exp(1j * OMEGA * u).sum()
    z = float(abs(R) ** 2 / n)
    zp = float(abs(R - n * c_env) ** 2 / n)
    return z, zp


def surrogate_bank(spec: SessionSpec, n_grid: np.ndarray,
                   seed: int) -> dict[int, tuple[np.ndarray, np.ndarray]]:
    """Sorted null banks per burst count for both statistics."""
    bank: dict[int, tuple[np.ndarray, np.ndarray]] = {}
    rng = np.random.default_rng(seed)
    c_env = spec.c_env()
    for n in n_grid:
        zs = np.empty(N_BANK)
        zps = np.empty(N_BANK)
        for k in range(N_BANK):
            z, zp = _z_pair(draw_session_u(spec, int(n), 0.0, rng), c_env)
            zs[k], zps[k] = z, zp
        bank[int(n)] = (np.sort(zs), np.sort(zps))
    return bank


def _rank_p(x: float, sorted_null: np.ndarray) -> float:
    idx = np.searchsorted(sorted_null, x, side="left")
    return float((1 + len(sorted_null) - idx) / (len(sorted_null) + 1))


@dataclass
class ProgrammeResult:
    power_fisher: float           # frozen detector, Fisher over sessions
    power_sumz: float             # frozen detector, hierarchical sum-z
    power_upgrade: float          # envelope-subtracted sum-z' (best case)
    fp_fisher: float
    fp_sumz: float
    fp_upgrade: float
    stats_signal: np.ndarray      # per-run frozen sum-z (for the combination)
    stats_null: np.ndarray


def programme_power(spec: SessionSpec, n_sessions: int, mean_bursts: int, eps: float, *,
                    n_mc_null: int, n_mc_signal: int, seed: int,
                    fixed_phase: float | None = None) -> ProgrammeResult:
    rng = np.random.default_rng(seed)
    sd = max(np.sqrt(mean_bursts), 1.0)
    n_lo = max(30, int(mean_bursts - 4 * sd))
    n_hi = int(mean_bursts + 4 * sd)
    n_grid = np.unique(np.linspace(n_lo, n_hi, 9).astype(int))
    bank = surrogate_bank(spec, n_grid, seed + 7)
    c_env = spec.c_env()

    def one_run(eps_run: float, run_seed: int) -> tuple[float, float, float]:
        r = np.random.default_rng(run_seed)
        T = Tp = 0.0
        ps = np.empty(n_sessions)
        for s in range(n_sessions):
            n = max(30, int(r.poisson(mean_bursts)))
            u = draw_session_u(spec, n, eps_run, r, phi=fixed_phase)
            z, zp = _z_pair(u, c_env)
            key = min(bank.keys(), key=lambda kk: abs(kk - n))
            ps[s] = _rank_p(z, bank[key][0])
            T += z
            Tp += zp
        return T, Tp, fisher_p(list(ps), P_FLOOR)

    null_T = np.empty(n_mc_null)
    null_Tp = np.empty(n_mc_null)
    null_fisher = 0
    for k in range(n_mc_null):
        t, tp, pf = one_run(0.0, seed + 100 + k)
        null_T[k], null_Tp[k] = t, tp
        null_fisher += int(pf < DETECTION_ALPHA)
    thr = float(np.quantile(null_T, 1.0 - DETECTION_ALPHA))
    thr_p = float(np.quantile(null_Tp, 1.0 - DETECTION_ALPHA))

    sig_T = np.empty(n_mc_signal)
    hits_f = hits_s = hits_u = 0
    for k in range(n_mc_signal):
        t, tp, pf = one_run(eps, seed + 100000 + k)
        sig_T[k] = t
        hits_f += int(pf < DETECTION_ALPHA)
        hits_s += int(t > thr)
        hits_u += int(tp > thr_p)

    return ProgrammeResult(
        power_fisher=hits_f / n_mc_signal, power_sumz=hits_s / n_mc_signal,
        power_upgrade=hits_u / n_mc_signal,
        fp_fisher=null_fisher / n_mc_null,
        fp_sumz=float(np.mean(null_T > thr)),
        fp_upgrade=float(np.mean(null_Tp > thr_p)),
        stats_signal=sig_T, stats_null=null_T)


def single_session_n80(spec: SessionSpec, *, eps: float = EPS_PREDICTED,
                       n_mc: int = 160, seed: int = 0) -> int | None:
    """Bursts needed in ONE session for 80% power with the upgraded
    (envelope-subtracted) statistic -- the best-case single-session wall."""
    c_env = spec.c_env()
    rng = np.random.default_rng(seed)

    def power_at(n: int) -> float:
        null = np.empty(400)
        for k in range(400):
            _, zp = _z_pair(draw_session_u(spec, n, 0.0, rng), c_env)
            null[k] = zp
        thr = float(np.quantile(null, 1.0 - DETECTION_ALPHA))
        hits = 0
        for k in range(n_mc):
            _, zp = _z_pair(draw_session_u(spec, n, eps, rng), c_env)
            hits += int(zp > thr)
        return hits / n_mc

    grid = [2000, 5000, 10000, 20000, 40000, 80000, 160000]
    powers = [power_at(n) for n in grid]
    for (n0, p0), (n1, p1) in zip(zip(grid, powers), zip(grid[1:], powers[1:])):
        if p0 < 0.80 <= p1:
            f = (0.80 - p0) / (p1 - p0 + 1e-12)
            return int(n0 + f * (n1 - n0))
    return None if powers[-1] < 0.80 else grid[0]
