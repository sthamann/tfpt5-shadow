# TFPT inflation — Starobinsky/scalaron `n_s`, `r`, `A_s`

The low-curvature gravity branch is `R + R²` (spectral action), so inflation is
**Starobinsky** with the scalaron mass fixed by the compiler:

```
M_scal = c₃^{7/2} · M̄ ≈ 3.06×10¹³ GeV
n_s = 1 − 2/N_⋆      r = 12/N_⋆²      A_s = N_⋆²/(24π²)·c₃⁷
```

`N_⋆` (e-folds) is a reheating/observational input (marker `[C]`, band [50,60]); the
slow Higgs-channel reheating computation pins the point `N_⋆ = 51.4`. `M_scal` and the
`R+R²` form are `[E]`.

## Result (deterministic; published values in `data/measurements.json`)

| observable | TFPT (N_⋆=51.4) | data | verdict |
|---|---|---|---|
| `n_s` | 0.9611 | Planck 0.9649±0.0042 | **−0.91σ (consistent)** |
| `n_s` | 0.9611 | P-ACT-LB+DESI 0.9743±0.0034 | **−3.9σ (tension)** |
| `r` | 0.0045 | BICEP/Keck BK18 <0.036 | below (ok) |
| `r` | 0.0045 | CMB-S4 σ_r≈5×10⁻⁴ | **9σ future falsifier** |
| `A_s` | 1.76×10⁻⁹ | Planck 2.10×10⁻⁹±0.03 | **−11.3σ** → prefers N_⋆≈56 |

→ honest, sharp, falsifiable: `n_s` consistent with Planck but in tension with the
DESI-combined value; `r≈0.0045` is the headline future falsifier (CMB-S4 will detect or
exclude it at ~9σ); the measured `A_s` requires faster reheating (`N_⋆≈56`) than the slow
Higgs-channel point — so the slow-channel point is `A_s`-disfavoured (matches the theory's
own scorecard).

## Reheating-free closure invariant (`closure_invariant.py`) — `N_⋆` eliminated

Eliminating `N_⋆` from the three read-offs gives exact, parameter-free relations
(pure algebra, machine-guarded for every `N`):

```
A_s·r = c₃⁷/(2π²) = 7.998e-12      r = 3(1−n_s)²      α_s = −r/6  (LO)
C_inf = 6π²·A_s·(1−n_s)²/c₃⁷ = 1   (scalar-only, testable with Planck alone)
```

| check | value | verdict |
|---|---|---|
| `C_inf` (Planck 2018 A_s+n_s) | 0.970 ± 0.233 | **−0.13σ (consistent)** |
| `C_inf` (P-ACT-LB+DESI n_s) | 0.520 ± 0.138 | **−3.48σ** — the known n_s tension in N-free form |
| N-free `r(A_s)` | 0.00381 ± 0.00005 | below BK18 <0.036; CMB-S4 7.6σ decider |
| N-free `n_s(A_s)` | 0.9644 | −0.13σ Planck / −2.91σ P-ACT-LB+DESI |
| `α_s = −r/6` | −6.35×10⁻⁴ | +0.58σ vs Planck −0.0045±0.0067 |

→ **consistent with the parameter-free TFPT curve on the Planck legs** — typing only,
not a detection. Caveats: the `A_s`–`n_s` covariance is *not* modelled (Gaussian,
cov=0, flagged in the output); `α_s = −r/6` is the leading slow-roll identity (exact
SR differs by ~7%); the invariant repackages the same information as the profiled-`A_s`
reading (scorecard `alternative_group: Nstar_branch` — never an independent hit).
**Dated decider:** a robust future bound `r < 0.0037` kills this normalisation; a
detection at `r≈0.0038` together with `α_s≈−r/6` escalates far beyond a generic
Starobinsky match.

## Reproduce

```bash
python -m venv .venv && . .venv/bin/activate && pip install -e .
tfpt-inflation analyze    # or: PYTHONPATH=src python -m tfpt_inflation.cli analyze
```
