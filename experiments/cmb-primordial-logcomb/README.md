# CMB primordial log-comb — the frozen ω against the Planck feature search

> **Firewall:** a consistency **typing** against published constraints — never
> load-bearing, never `[E]`. No raw likelihood is re-fit; the experiment
> machine-checks the confrontation and states the dated decider. Preregistered
> in `hypotheses/cmb_logcomb_v1.yaml`.

## Why this bed is categorically special

Every astrophysical comb search so far ran on observer time with an
**unjustified clock** (the S14 lesson — all those nulls are bridge nulls). The
primordial power spectrum is the **one natural-data bed where the log-clock is
motivated**: inflation e-folds *are* a log-clock (modes exit the horizon at
ln k ∝ N). If the seed epoch carried the seam recovery, its log-comb would be
imprinted **in ln k** — and Planck already searched exactly this template:

```
P(k) = P0(k) · [1 + A_log · cos(ω_log · ln(k/k*) + φ)]      (Planck 2018 X, Sect. 7)
```

The frozen TFPT frequency `ω = 2π/ln((3/2)⁶) = 2.5827` (log₁₀ω = 0.412) lies
**inside** the Planck search prior (log₁₀ω ∈ [0, 2.1]). What is *not* derived
(flagged bridge, S15): that the recovery comb transfers multiplicatively into
P(k), and that the amplitude is the QT.02 value ε = e^(−π²/lnΛ) = 0.0173.

## Result (machine-checked typing) — **data_limited**

| check | value |
|---|---|
| ω inside the published search band | yes (0.412 ∈ [0, 2.1]) |
| reach, full likelihood window (k = 10⁻⁴–0.2 Mpc⁻¹, ℓ = 2–2500) | **3.12 comb periods** (> 2.8 gate) |
| reach, conservative window (k = 0.005–0.2) | 1.52 periods (sub-gate; the gate passes only with the cosmic-variance-dominated low-ℓ leg) |
| published detection at any ω | none (Planck: Δχ² ~ 10 typed as noise/217-GHz artefact) |
| published 95 % amplitude bound | ≈ 0.03 (Planck 2018 X, Fig. 28); ≈ 0.029 combined Planck+SPT-3G+ACT |
| predicted amplitude | ε = 0.0173 — a factor **1.7 below** today's bound |

**Verdict: `data_limited`.** The predicted comb is currently invisible by a
factor ~1.7 in amplitude. **Dated decider:** CMB-S4-class combined bounds reach
the 0.017 level — a future 95 % bound `A_log(ω = 2.583) < 0.017` with no
detection **kills** the primordial-DSI bridge reading; a detection *at* the
frozen ω (phase-coherent across TT/TE/EE) escalates. Either way this is one of
the few dated, external, zero-parameter decision points of the program (the
frequency has no tunable freedom).

## Bridge-class note (2026-08-27, typed — no change to the freeze)

The internal character theorem (`experiments/tfpt-discovery/
doubletone_character_transduction_probe.py`, 10/10) proves that the
`ω = 2.5827` tone is the **odd** character of the transfer operator while
the monopole and the `ω₋ = 0.9532` tone share the **even** character.
Under a *character-faithful* transduction (internal parity → E/B parity,
pinned even→even by the monopole), the TT channel would carry
`{0.9532, 0.4766, 1.2914}` and `2.5827` would be **forbidden** in TT —
the frozen search above then belongs to the *character-blind* (S15
multiplicative) bridge class. Both classes stay open until
OBS.TRANSDUCTION.01 is proven; the freeze is **not** retracted.
Update 2026-08-27: the bridge is now *reduced* — `sheetflip_skyparity_bridge_probe.py`
(13/13) proves that geometric covariance of the coupling + the CPT typing of the
sheet flip **imply** the faithful dictionary (equivariance theorem, sky-parity law
machine-verified); the sole remaining premise is the covariance axiom TE, which for
the CPT representative is CPT invariance — a theorem inside any local 4D QFT, i.e.
TE rides on the existing QFT4D.OS.RECON.01 contract rather than a new assumption.

## Faithful-class ω₋ typing (`omega_minus.py`, 2026-08-27) — **data_limited**

The 2025 combined scan (Planck + ACT DR6 + SPT-3G, arXiv:2507.17276) uses the
**identical template** with a **flat prior ω ∈ [0, 100]** — unlike Planck 2018 X,
this *covers* ω₋ = 0.953: `A_log < 0.0286` (95%, global), per-frequency 2σ limits
≲ 0.05, no detection. Machine-checked typing:

| check | value |
|---|---|
| ω₋ inside the 2025 flat prior | yes |
| reach at ω₋, full Planck window | **1.15 periods** (< 2.8 gate) |
| reach at ω₋, optimistic [10⁻⁴, 1] Mpc⁻¹ | 1.40 (still sub-gate) |
| reach at ω₊/2 = 1.291 (2Δ₊ tone) | 1.56 (sub-gate) |
| ε candidate 0.0173 vs bounds | below both (global 0.0286 / per-freq 0.05) |

→ **`data_limited`, structurally**: ω₋ is frequency-covered but *period-starved* —
no realistic single k-window reaches the frozen 2.8-period gate (that needs ~8
decades in k). The amplitude carry-over of ε to the even sector is typed OPEN.
Consequence of the bridge theorem: under the faithful class, **no** even-channel
TFPT tone is gate-testable in TT today; the gate-passing home of the faithful
class is **TB/EB at ω₊ = 2.5827 — where no published comb search exists** (the
open target this experiment now names). New dated
decision structure: a TT detection at 2.5827 refutes the faithful class;
a TT detection at 0.9532/1.2914 supports it (note: log₁₀(0.9532) = −0.021
sits just *below* the published Planck search prior [0, 2.1]); TB/EB
structure at 2.5827 is the faithful class's own positive channel.

## Reproduce

```bash
cd experiments/cmb-primordial-logcomb
python tests/test_frozen_targets.py          # 6/6 guard
PYTHONPATH=src python -m tfpt_cmblog.analysis   # -> results/results.json
```

## References

Planck 2018 results X (A&A 641, A10), Sect. 7–8 + Fig. 28 (log-oscillation
template, priors, bounds); combined Planck+SPT-3G+ACT feature constraints
(A_log ≲ 0.029 at 95 %); Planck 2018 VI/IX for the underlying likelihoods.
