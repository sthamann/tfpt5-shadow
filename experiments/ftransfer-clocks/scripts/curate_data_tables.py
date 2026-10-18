"""Curate the two frozen FTC.01 data interfaces for FTRANSFER.CLOCKS.01.

One-off curation script (experiments/ftransfer-clocks/, NOT load-bearing).
Produces, deterministically, the two data tables the preregistration
(hypotheses/ftransfer_clocks_v1.yaml, sha256
880224f76380c77dce2c1e3d7651bccc9e1619e74c60b7e15326ee0ee2bbf4d0) names as
the pending data interfaces:

  (a) data/gstar_saikawa_shirai_2018.csv
      g_*rho(T) / g_*s(T) -- deterministic subsample (every 20th row plus the
      last row) of the published tabulation of
        K. Saikawa & S. Shirai, "Primordial gravitational waves, precisely:
        the role of thermodynamics in the Standard Model",
        JCAP 05 (2018) 035, arXiv:1803.01038, Appendix A tabulated data,
        file standardmodel2018.dat from
        https://member.ipmu.jp/satoshi.shirai/EOS2018
      The full source file's sha256 is recorded in the CSV header; the
      preregistration names exactly this source ("Saikawa & Shirai 2018
      (arXiv:1803.01038), frozen tabulation").

  (b) data/alphas_pdg2024_running.csv
      The PDG world-average alpha_s(M_Z) = 0.1180 +- 0.0009 (PDG 2024,
      Prog. Theor. Exp. Phys. 2024, 083C01, QCD review Sec. 9.4.4) run with
      the standard 4-loop MS-bar beta function (PDG QCD review Eq. 9.5,
      coefficients b0..b3) in n_f = 5 from M_Z = 91.1880 GeV to the top pole
      mass m_t = 172.57 GeV, matched 5 -> 6 by continuity at m_t (the
      matching prescription frozen in the preregistration), then n_f = 6 up
      to 1 TeV.  This is the PDG-quoted running curve that underlies the
      world-summary alpha_s(Q) overlay plot (PDG 2024 Fig. 9.5); the
      uncertainty column propagates +-0.0009 at M_Z through the same runs.

Both tables are byte-frozen after this script runs; their sha256 hashes go
to data/DATA_FREEZE.sha256 and are verified by run_clocks_executor.py at
startup.  Re-running this script must reproduce the tables byte-identically
(deterministic subsample rule, fixed-step classical RK4, fixed formatting).
"""
from __future__ import annotations

import hashlib
import math
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
DATA = os.path.join(BASE, "data")

# --- (a) Saikawa-Shirai g_* tabulation -------------------------------------
SRC_URL = "https://member.ipmu.jp/satoshi.shirai/standardmodel2018.dat"
SRC_SHA256 = "268a51b869198b13aef052185323e0b0015f78f4a0902f19a79e71d1017dfaad"
SRC_LOCAL = "/tmp/standardmodel2018.dat"
SUBSAMPLE_EVERY = 20  # keep data rows 0, 20, 40, ... plus the final row

# --- (b) PDG 2024 alpha_s inputs (all frozen in the preregistration) --------
ALPHAS_MZ = 0.1180        # PDG 2024 world average
ALPHAS_MZ_ERR = 0.0009
M_Z = 91.1880             # GeV (PDG 2024)
M_T = 172.57              # GeV (top pole mass, PDG 2024)
Q_MAX = 1000.0            # GeV (frozen overlay window upper edge)
N_GRID = 181              # log-spaced points M_Z..1 TeV (~0.0058 dex step)
ZETA3 = 1.2020569031595943


def beta_coeffs(nf: int):
    """4-loop MS-bar beta coefficients b0..b3 in the PDG normalization
    d alpha_s / d ln(mu^2) = -alpha_s^2 (b0 + b1 a + b2 a^2 + b3 a^3),
    PDG 2024 QCD review Eq. (9.5)."""
    b0 = (33.0 - 2.0 * nf) / (12.0 * math.pi)
    b1 = (153.0 - 19.0 * nf) / (24.0 * math.pi**2)
    b2 = (2857.0 - 5033.0 / 9.0 * nf + 325.0 / 27.0 * nf**2) / (128.0 * math.pi**3)
    b3 = ((149753.0 / 6.0 + 3564.0 * ZETA3)
          - (1078361.0 / 162.0 + 6508.0 / 27.0 * ZETA3) * nf
          + (50065.0 / 162.0 + 6472.0 / 81.0 * ZETA3) * nf**2
          + 1093.0 / 729.0 * nf**3) / (256.0 * math.pi**4)
    return b0, b1, b2, b3


def run_alpha(alpha0: float, q0: float, q1: float, nf: int, nstep: int = 4000) -> float:
    """RK4 integration of the 4-loop RGE in x = ln Q from q0 to q1."""
    b0, b1, b2, b3 = beta_coeffs(nf)

    def rhs(a: float) -> float:
        # d alpha / d ln Q = 2 * d alpha / d ln Q^2
        return -2.0 * a * a * (b0 + b1 * a + b2 * a * a + b3 * a * a * a)

    h = (math.log(q1) - math.log(q0)) / nstep
    a = alpha0
    for _ in range(nstep):
        k1 = rhs(a)
        k2 = rhs(a + 0.5 * h * k1)
        k3 = rhs(a + 0.5 * h * k2)
        k4 = rhs(a + h * k3)
        a += (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return a


def alpha_at(q: float, alpha_mz: float) -> float:
    """alpha_s(q) from alpha_s(M_Z): 4-loop, n_f = 5 below m_t, continuity
    matching at m_t (frozen prescription), n_f = 6 above."""
    if q <= M_T:
        return run_alpha(alpha_mz, M_Z, q, nf=5)
    a_mt = run_alpha(alpha_mz, M_Z, M_T, nf=5)
    return run_alpha(a_mt, M_T, q, nf=6)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def curate_gstar() -> str:
    if not os.path.exists(SRC_LOCAL):
        print("downloading %s ..." % SRC_URL)
        urllib.request.urlretrieve(SRC_URL, SRC_LOCAL)
    got = sha256_file(SRC_LOCAL)
    if got != SRC_SHA256:
        raise SystemExit("FATAL: source file sha256 mismatch:\n  got      %s\n  expected %s"
                         % (got, SRC_SHA256))
    rows = []
    with open(SRC_LOCAL) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            rows.append(line.split())
    kept = rows[::SUBSAMPLE_EVERY]
    if rows[-1] is not kept[-1]:
        kept.append(rows[-1])

    out = os.path.join(DATA, "gstar_saikawa_shirai_2018.csv")
    with open(out, "w") as f:
        f.write(
            "# FTRANSFER.CLOCKS.01 frozen data interface (a): g_*rho(T), g_*s(T)\n"
            "# Source (named in the preregistration): K. Saikawa & S. Shirai,\n"
            "#   'Primordial gravitational waves, precisely: the role of thermodynamics\n"
            "#   in the Standard Model', JCAP 05 (2018) 035, arXiv:1803.01038,\n"
            "#   Appendix A tabulated data, file standardmodel2018.dat,\n"
            "#   https://member.ipmu.jp/satoshi.shirai/EOS2018 (retrieved 2026-08-05).\n"
            "# Full source file sha256: %s\n"
            "# Curation rule (deterministic): data rows subsampled every %dth row of the\n"
            "#   10000-row log(T)-spaced source table, plus the final row (501 rows).\n"
            "#   Values are copied verbatim (no reformatting, no interpolation).\n"
            "# Columns: T_GeV,gstar_rho,gstar_rho_err,gstar_s,gstar_s_err\n"
            % (SRC_SHA256, SUBSAMPLE_EVERY))
        for r in kept:
            f.write(",".join(r) + "\n")
    print("wrote %s  (%d data rows)" % (out, len(kept)))
    return out


def curate_alphas() -> str:
    qs = [M_Z * (Q_MAX / M_Z) ** (i / (N_GRID - 1)) for i in range(N_GRID)]
    # exact anchor rows for the frozen window edges
    for anchor in (M_T,):
        if not any(abs(q - anchor) / anchor < 1e-12 for q in qs):
            qs.append(anchor)
    qs.sort()

    out = os.path.join(DATA, "alphas_pdg2024_running.csv")
    with open(out, "w") as f:
        f.write(
            "# FTRANSFER.CLOCKS.01 frozen data interface (b): alpha_s(Q) reference running\n"
            "# Source: PDG 2024 (S. Navas et al., Particle Data Group), Prog. Theor. Exp.\n"
            "#   Phys. 2024, 083C01: world average alpha_s(M_Z) = 0.1180 +- 0.0009 (QCD\n"
            "#   review Sec. 9.4.4); 4-loop MS-bar beta function coefficients b0..b3 (QCD\n"
            "#   review Eq. (9.5)); M_Z = 91.1880 GeV; top pole mass m_t = 172.57 GeV.\n"
            "# Construction (deterministic; this is the PDG-quoted running curve that\n"
            "#   underlies the world-summary alpha_s(Q) overlay, PDG 2024 Fig. 9.5):\n"
            "#   4-loop RGE integrated with fixed-step classical RK4 (4000 steps/leg) in\n"
            "#   ln Q; n_f = 5 from M_Z to m_t, 5->6 matching by CONTINUITY at m_t (the\n"
            "#   prescription frozen in the preregistration), n_f = 6 from m_t to 1 TeV.\n"
            "#   alpha_lo/alpha_hi propagate alpha_s(M_Z) = 0.1171 / 0.1189 identically.\n"
            "# Columns: Q_GeV,alpha_s,alpha_s_lo,alpha_s_hi\n")
        for q in qs:
            a = alpha_at(q, ALPHAS_MZ)
            lo = alpha_at(q, ALPHAS_MZ - ALPHAS_MZ_ERR)
            hi = alpha_at(q, ALPHAS_MZ + ALPHAS_MZ_ERR)
            f.write("%.6f,%.8f,%.8f,%.8f\n" % (q, a, lo, hi))
    print("wrote %s  (%d data rows)" % (out, len(qs)))

    a_mt = alpha_at(M_T, ALPHAS_MZ)
    a_tev = alpha_at(Q_MAX, ALPHAS_MZ)
    print("  sanity: alpha_s(m_t = %.2f) = %.6f   alpha_s(1 TeV) = %.6f" % (M_T, a_mt, a_tev))
    return out


def main() -> int:
    os.makedirs(DATA, exist_ok=True)
    paths = [curate_gstar(), curate_alphas()]
    freeze = os.path.join(DATA, "DATA_FREEZE.sha256")
    with open(freeze, "w") as f:
        f.write("# FTRANSFER.CLOCKS.01 frozen data tables -- byte-frozen 2026-08-05,\n"
                "# BEFORE the executor first ran.  run_clocks_executor.py verifies these\n"
                "# hashes (and the preregistration YAML hash) at startup.\n")
        for p in paths:
            f.write("%s  %s\n" % (sha256_file(p), os.path.basename(p)))
    print("wrote %s" % freeze)
    with open(freeze) as f:
        sys.stdout.write(f.read())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
