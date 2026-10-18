"""Guard: frozen targets + published-bound values (typing cannot drift)."""

import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from tfpt_cmblog import analysis as a  # noqa: E402
from tfpt_cmblog import omega_minus as om  # noqa: E402

checks = [
    ("omega frozen", abs(a.OMEGA - 2.0 * math.pi / math.log((3 / 2) ** 6)) < 1e-15),
    ("log10 omega in Planck prior", 0.0 <= math.log10(a.OMEGA) <= 2.1),
    ("epsilon value", abs(a.EPS_PRED - 0.0173025) < 1e-6),
    ("bounds on record", a.BOUND_95 == {"planck2018_x": 0.03, "combined_2024plus": 0.029}),
    ("windows frozen", a.K_FULL == (1e-4, 0.2) and a.K_CONSERVATIVE == (0.005, 0.2)),
    ("prediction below tightest bound", a.EPS_PRED < min(a.BOUND_95.values())),
    ("omega_minus frozen", abs(om.OMEGA_MINUS - 2.0 * math.pi / math.log(3 ** 6)) < 1e-15
     and abs(om.OMEGA_MINUS - 0.95320029) < 1e-8),
    ("even-tone set frozen", abs(om.EVEN_TONES["omega_plus_half"] - a.OMEGA / 2) < 1e-12
     and abs(om.EVEN_TONES["omega_minus_half"] - om.OMEGA_MINUS / 2) < 1e-12),
    ("2025 coverage on record", om.COMBINED_2025_OMEGA_PRIOR == (0.0, 100.0)
     and om.COMBINED_2025_ALOG_95_GLOBAL == 0.0286),
    ("omega_minus period-starved everywhere",
     om.periods_simple(om.K_FULL, om.DELTA_MINUS) < om.REACH_GATE
     and om.periods_simple(om.K_OPTIMISTIC, om.DELTA_MINUS) < om.REACH_GATE),
]
for n, ok in checks:
    print(("PASS" if ok else "FAIL"), n)
print(f"{sum(ok for _, ok in checks)}/{len(checks)} pass")
if not all(ok for _, ok in checks):
    raise SystemExit(1)
