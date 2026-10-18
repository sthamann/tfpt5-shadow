"""Guards: frozen YAML hash, frozen numbers, fitter self-test (no data)."""

import math
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from eb_comb import analyze as an  # noqa: E402

checks = [
    ("hypotheses hash frozen", an.yaml_sha16() == an.YAML_SHA16),
    ("omega_+ frozen", abs(an.OMEGA_PLUS - 2.58270695) < 1e-8),
    ("omega_- frozen", abs(an.OMEGA_MINUS - 0.95320029) < 1e-8),
    ("bins frozen", (an.ELL_MIN, an.ELL_MAX, an.DELTA_ELL) == (51, 1490, 20)
     and len(an.bin_labels()) == 72),
    ("reach sub-gate disclosed",
     math.log(an.ELL_MAX / an.ELL_MIN) * an.OMEGA_PLUS / (2 * math.pi)
     < an.REACH_GATE),
]

# fitter self-test on synthetic data (no real data touched)
rng = np.random.default_rng(1)
centers = an.bin_centers()
t = 1e-2 * (centers / 300.0) ** -1.5          # synthetic smooth template
sig = 0.05 * t + 1e-5
lnx = np.log(centers / an.ELL_STAR)
y_comb = 0.8 * t * (1 + 0.12 * np.cos(an.OMEGA_PLUS * lnx + 1.1))
y_null = 0.8 * t
f1 = an.fit_comb(y_comb, sig, t, an.OMEGA_PLUS, centers)
f0 = an.fit_comb(y_null, sig, t, an.OMEGA_PLUS, centers)
checks += [
    ("fitter recovers injected A=0.12",
     abs(f1["A"] - 0.12) < 0.01 and abs((f1["phi"] - 1.1)) < 0.05),
    ("fitter finds nothing on pure baseline", f0["dchi2"] < 1e-12),
    ("A95 covers injected amplitude",
     an.a95_profile(y_comb, sig, t, an.OMEGA_PLUS, centers,
                    f1["chi2_comb"]) > 0.12),
]

for n, ok in checks:
    print(("PASS" if ok else "FAIL"), n)
print(f"{sum(ok for _, ok in checks)}/{len(checks)} pass")
if not all(ok for _, ok in checks):
    raise SystemExit(1)
