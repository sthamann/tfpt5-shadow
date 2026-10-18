# EB log-comb search (`cmb-eb-logcomb/`) — the faithful-class positive channel

**Status: `data_pass_run` — verdict: `null` (PR4/NPIPE HFI stacked EB, 2026-08-27).**
Hypotheses frozen and hashed 2026-08-27 **before** any data contact
(`hypotheses/eb_logcomb_v1.yaml`, SHA-16 `e519ca9eb36dbb7a`).

## Firewall (read first)

Search target of the **faithful-class** reading (sheetflip-bridge chain,
DLXIII) — **not** a claim:

- Under a covariant CPT-typed coupling the odd kernel tone
  `ω₊ = 2.58270695` is forbidden in TT/TE/EE and lives in **TB/EB**.
  This is the **first comb search in that channel** (no published one exists).
- A null does **not** damage the compiler core; the faithful bridge premise
  (TE covariance axiom) and the S15 blind bridge both stay open.
- No marker moves; promotion only via `promote-to-verification`.
- The **phase leg is contract-locked** (holonomy intertwiner, DLXII):
  φ is *profiled*, never claimed.

## Frozen (before data contact)

```
model:      EB_b = s0 · T_b · [1 + A cos(ω ln(ℓ_c/150) + φ)]
T_b:        binned ΛCDM (EE−BB), CAMB, tutorial parameters, µK²
ω₊ frozen:  2.58270695      ω₋ control (kill leg): 0.95320029
statistic:  Δχ² (A=0 vs A free), diagonal Gaussian likelihood
nulls:      2000 Gaussian sims around the A=0 best fit, seed 20260827
controls:   60-point ω LEE scan + forbidden-tone ω₋ + bin scramble
reach:      ln(1490/51)·ω₊/2π = 1.39 periods < 2.8 gate — DISCLOSED:
            no detection claim possible; deliverable = first EB-comb
            amplitude statement + dictionary kill-leg test
```

## Data-contact log

- **2026-08-27** — first data contact: `HFI_f_sky_092_EB_o.npy`
  (1280 B, SHA-256 `ae5a6ca11abbdb33…429dea`) from
  [LilleJohs/Observed-EB-Power-Spectrum](https://github.com/LilleJohs/Observed-EB-Power-Spectrum):
  beam-deconvolved stacked observed EB of Planck PR4/NPIPE HFI,
  f_sky = 0.92, PolSpice, bins ℓ = 51–1471 (Δℓ = 20), µK²
  (Eskilt et al. 2023, arXiv:2303.15369). Hypotheses were frozen and
  hashed BEFORE this download.

## Result (deterministic, seed 20260827; `results/results.json`)

| quantity | value |
|---|---|
| Δχ²(ω₊ = 2.5827) | 0.427 (best-fit A = 0.13, meaningless at this S/N) |
| p(ω₊) vs 2000 nulls | **0.813** — no comb |
| ω₋ forbidden-tone control | Δχ² = 0.652, p = 0.737 — **no dictionary violation** |
| LEE scan (60 ω) | frozen ω ranks 56/60; p_global = 0.871 |
| scramble control | Δχ² = 2.11 (consistent with null battery) |
| A₉₅(ω₊) | **> 0.5** (no crossing below the frozen cap) |

**Verdict: `null`.** No log-comb at the frozen frequency in the parity-odd
EB channel, and the even tone does not leak into it (the DLXIII dictionary
survives its first kill-leg exposure). Honest scope: (i) reach is sub-gate
(1.39 < 2.8 periods) — disclosed pre-freeze, so this could never have been
a detection claim; (ii) only diagonal errors are published (no bin-bin
covariance); (iii) a *multiplicative* comb on a baseline detected at only
~3–5σ (β ≈ 0.3° ± 0.1°) is intrinsically weakly bounded — reaching the
candidate amplitude ε = 0.0173 needs a baseline S/N ≳ 60, i.e.
**LiteBIRD/Simons-Observatory-class EB data: the dated decider**. A future
EB detection at that S/N with a comb at ω₊ (and none at ω₋) would be the
faithful dictionary's positive signature; a comb at ω₋ in EB kills it.

## Reproduce

```bash
cd experiments/cmb-eb-logcomb
../tfpt-discovery/.venv/bin/python tests/test_frozen.py        # 8/8 guards
PYTHONPATH=src ../tfpt-discovery/.venv/bin/python -m eb_comb.cli freeze-check
PYTHONPATH=src ../tfpt-discovery/.venv/bin/python -m eb_comb.cli analyze
```

## Layout

```
hypotheses/eb_logcomb_v1.yaml   # frozen pre-data, SHA-16 e519ca9eb36dbb7a
src/eb_comb/analyze.py          # template, linearised comb fit, A95, nulls
src/eb_comb/cli.py              # freeze-check / fetch / analyze
tests/test_frozen.py            # hash + frozen numbers + fitter self-test
data/HFI_f_sky_092_EB_o.npy     # fetched 2026-08-27 (SHA logged above)
results/results.json            # deterministic output
```
