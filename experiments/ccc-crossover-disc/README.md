# CCC crossover-disc search (`ccc-crossover-disc/`)

**Status: `data_pass_run` — verdict: `null` (SMICA single-map pass, 2026-08-24).**
Hypotheses frozen 2026-08-24 before any CMB data contact (the sealed
YAML keeps its freeze-time `status:` field as part of the hash trail).

## Firewall (read first)

This project searches CMB temperature maps for **crossover-relic disc
signatures** under the TFPT **cyclic `[C]` reading** (origin_theory).
It is a **search target, not a claim**:

- A null result does **not** damage the TFPT compiler core — the cyclic
  reading is `[C]`, not `[E]`, and stays so regardless of outcome.
- A hit is a **candidate**, not a confirmation, until it passes the
  frozen decision rule (replication + BH-q < 0.01).
- The observable is a residual boundary/crossover-relic pattern — **not**
  direct Hawking radiation, **not** new gravity.
- Nothing here moves markers, ledger rows or paper text; promotion (if
  ever) goes through the `promote-to-verification` skill.

## What is frozen (and where it comes from)

Three freeze stages, hashed, recomputed by `freeze-check` and guarded by
`tests/` (provenance: `experiments/tfpt-discovery/` rounds DLIII–DLV):

| Stage | Content | SHA-16 |
|---|---|---|
| v1 | two-mode kernel shape: rates `ln(729/64)`, `ln 729`, ratio `ln3/ln(3/2) = 2.709511`; defect sign table | `1df51166d0a2ef5b` |
| v2 | geometry: `theta_max = eta_rec/(eta_0 − eta_rec)` ≈ 1.16°; rim-ring topology (reading R2) | `a795401accbebdb4` |
| v3 | kappa derived from the v526 seam-KMS normalisation (`beta_angle = 2π = 1/(4c3)`): radial contrast ≤ 3.3e−4 ⇒ **template = causal top-hat disc** (reading R1) | `4cafe0457e0e89a1` |

**Primary template (R1):** sharp-edged top-hat disc, radius scanned only
over the frozen band **1.0–1.3°**. Discriminators: (i) the sharp causal
edge (vs Gaussian spots — the class HawkingNet scanned), (ii) the frozen
**sign-pairing statistics** (pair-class relics come as opposite-sign
equal-amplitude pairs — the sheet-parity bit; anchor-class relics carry
no pair component), (iii) the radius band itself.
**Fallback (R2, only if K6 fires):** the freeze-v2 rim-brightened ring
with edge-rate ratio 2.7095.

Kill conditions K1–K6, null battery and the decision rule are frozen in
`hypotheses/ccc_disc_v1.yaml`.

## Observable semantics

Relic amplitude = matched-filter response of the **temperature** map to
the top-hat template (µK). Signs are physical (the sheet-parity bit);
no absolute-value fitting. The radius is **not** a free parameter.

## Setup & run

```bash
cd experiments/ccc-crossover-disc
PYTHONPATH=src python -m ccc_disc.cli freeze-check   # audit (no data)
python -m pytest tests/ -q                            # freeze guards
```

The data pass (executed 2026-08-24, ~23 s on the shared
`experiments/tfpt-discovery/.venv`):

```bash
PYTHONPATH=src python -m ccc_disc.cli analyze \
    --map data/COM_CMB_IQU-smica_2048_R3.00_full.fits
```

Deterministic (global seed 20260824 pinned before the null battery);
invoking `analyze` without `--map` still prints the frozen pipeline
plan and exits 3. First data contact is logged below.

## Data-contact log

- **2026-08-24** — first data contact: Planck PR3 SMICA
  `COM_CMB_IQU-smica_2048_R3.00_full.fits` (IRSA, 2 013 312 960 bytes),
  single-map pass per the frozen pipeline (NSIDE 256, frozen radius band,
  100 Gaussian nulls, injection-recovery). Hypotheses were frozen and
  hashed BEFORE this download.

## Verdict (current)

**`null` (SMICA single-map pass, 2026-08-24, corrected pipeline,
seed-pinned):** max |SNR| = 5.12 with **p_global = 0.673**, candidate
counts at **p_counts = 0.446**, **BH-q_min = 0.673** (frozen rule needs
q < 0.01) — no top-hat disc excess over the Gaussian null battery in
either statistic, well-powered at the frozen radius band.
Injection-recovery of 200 µK discs: **100%** (detector validated with
the optimal filter). Kill criteria K1–K6: all **NA** (they fire only on
a resolved relic detection; none exists). Replication legs
(Commander/NILC, half-mission) are not required for a null and remain
available for any future candidate. Deterministic: reruns are
bit-identical (seed 20260824, data SHA-256 `60952c64…ce4f9ac`).
Full numbers: `results/results.json`.

**Seed amendment (disclosed, 2026-08-24):** the corrected pass was
first run with an unpinned global RNG in `hp.synfast` (null battery not
reproducible; it gave p_global = 0.683, p_counts = 0.287 — same
verdict). The prereg demands pinned seeds, so the global NumPy RNG is
now seeded (20260824) in `analyze.py` before the sims. Execution
mechanics only — template, radius band, statistics, thresholds and
decision rule untouched.

**Pipeline correction (disclosed, 2026-08-24):** the first executed
pass used a matched filter with an incorrect ℓ-weighting
(`F_ℓ ∝ τ_ℓ/C_ℓ` instead of the optimal `F_ℓ ∝ τ_ℓ/((2ℓ+1)C_ℓ)`) and
generated the null simulations from the pseudo-spectrum with a second
mask convolution. That run gave p_global = 0.238, p_counts = 0.040
(marginal) — the marginal count excess was an artifact of the sim
spectral-shape inconsistency and disappears under the corrected
estimator. The frozen template, radius band, kill criteria and
decision rule were never touched; the correction is estimator-level
only. Both runs are recorded here for the audit trail.
