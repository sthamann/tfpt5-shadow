# nu-scalaron-falsification

Preregistered falsification project for the **FLAV.NUSCALE.05 scalaron-trace
rung** (`verification/v986_nu_scalaron_rung.py`, [C]/[N] candidate, mechanism
[O]):

```
M_R = N_fam * M_scal = 3 * c3^(7/2) * Mbar = 9.180e13 GeV      (zero dials)
```

## Firewall

This is an `experiments/` consistency-and-kill project, **not** a claim.
Nothing here moves a ledger marker, closes the seesaw, or counts as blind
confirmation — the input channels (m3 seesaw machinery, PMNS angles) were
known before this project existed. Only **future** data releases (DESI DR3+,
KATRIN final, LEGEND-1000, JUNO ordering) count as new evidence against the
frozen predictions below.

## Frozen chain (hypotheses/nu_scalaron_v1.yaml, SHA-16 `4941b396729636de`)

`M_R` (frozen) → `m3` via the verbatim v481 1-loop runner under the named
premise `y_nu = y_t` [P] → `m2` (two declared variants: TFPT-internal
`m3·sqrt(|J_PMNS|)` and hybrid `sqrt(dm2_21)`) → `m1 = 0` (NO floor) →
`Sigma m_nu`, `m_beta`, `m_bb` interval (PMNS = frozen v270 channels;
Majorana phases unconstrained → exact interval) + leptogenesis leg reported
(`M1 = M_R·phi0^4`, `m~1 = m3/10`, v184 relations).

## Frozen predictions (2026-08-28 pass)

| observable | prediction | comparator (dated) | verdict |
|---|---|---|---|
| m3 | 0.05124 eV | NuFIT 6.0 sqrt(dm2_3l) = 0.05013 eV (+2.2%) | consistent (inside >50% RG envelope, v482) |
| Sigma m_nu (NO) | 0.0600 / 0.0599 eV (variants a/b) | DESI DR2 2025 LCDM 95% UL 0.0642 eV (margin +0.004) | consistent w.r.t. UL; **model-dependent tension** under the LCDM posterior squeeze (corpus sum-m_nu row) |
| m_beta | 0.0092 eV | KATRIN 2024 < 0.45 eV | consistent (~50x below bound; not near-term) |
| m_bb (NO, phase interval) | [1.4, 3.8] meV | KamLAND-Zen 2024 < 28–122 meV | consistent (LEGEND-1000-class kills only IO) |
| leptogenesis leg | see leptogenesis pass below | BDP ODE (v372 tools) | decuple route consistent (×1.06) |

First data contact for this comparison pass: 2026-08-28 (all comparators are
published, dated values frozen in the YAML before the pass).

## Leptogenesis pass (2026-08-28, declared follow-up — executed)

`scripts/leptogenesis_pass.py` sends the frozen chain through the verbatim
v372 BDP Boltzmann network (K = 4.74, κ_f = 0.0886). The corpus carries two
M1 conventions; under the frozen `M_R = 3M_scal` both become zero-dial
numbers and η_B **discriminates** them:

| route | M1 | η_B | vs observed 6.1e-10 |
|---|---|---|---|
| v212 decuple `M1 = M_scal·φ0²/A_Λ` | 8.65e9 GeV | 6.44e-10 | ×1.06 — **inside** [obs/3, 3·obs] |
| v184 scenario `M1 = M_R·φ0⁴` | 7.34e8 GeV | 5.5e-11 | ×0.09 — **outside** band |

Honesty: v372 already sat at ×1.07 with its own frozen inputs — the
candidate chain *preserves* that hit (it does not improve it); the new
content is the discriminator: the frozen candidate **selects the decuple
convention** and disfavors the v184 scenario relation. M1 reproducing the
observation exactly: 8.20e9 GeV (decuple off by ×1.06).

## Kill conditions (frozen)

- **K1**: robust cosmological `Sigma m_nu` bound below 0.0599 eV (within the
  stated 2% RG envelope) → candidate dead.
- **K2**: the required `M_R` under the same frozen premise chain shifts by
  more than ~5% (better RG inputs) → candidate dead.
- **K3**: established inverted ordering → chain dead (NO assumed).
- **K4**: `m_bb` measured above the frozen NO interval → interval statement
  dead.

## Verdict (v1 pass)

`consistent` — with the honest caveat that the entire NO branch (floor
0.0588 eV, this candidate 0.0600 eV) sits under the model-dependent DESI
LCDM posterior squeeze already typed as `tension` in the evidence scorecard.
The candidate is maximally exposed: **one DESI-class improvement decides.**

## v2 — Q₊ spectral Majorana (review wave 3, 2026-08-28)

Preregistered in `hypotheses/nu_scalaron_v2.yaml` (SHA-16 `c912e95e91a247ac`),
frozen **before** this comparison.  Probe:
`experiments/tfpt-discovery/nu_qplus_spectral_matrix_probe.py`.

### Premise

**`PREMISE_FOUND`.**  The corpus already owns a family operator `Q_+` with
`Spec(Q_+) = {1,2,3}`:

- generation / flavor-address basis (v10/v50):
  `Q_+ = (Q + Σ Q Σ)/2 = [[3,0,0],[0,2,0],[0,2,1]]`,
  `χ = (t-1)(t-2)(t-3)`;
- cusp eigenbasis (v69/v72): `Q_+ = 3 diag({0,1/3,2/3}) + 1 = diag(1,2,3)`.

Same spectrum, two coordinate representations.  Not reconstructed.  The
nearest-object fallback was not needed.  (v986's `Tr I = 3` motivation is
a **trace** argument — `Spec(I) = {1,1,1}` — and is hereby retyped; the
candidate row already had mechanism `[O]`, so this is not a ledger error.)

Lagrange spectral projectors of the v50 matrix (exact, sympy):

```
P_1 = (Q_+ - 2I)(Q_+ - 3I)/2 = [[0,0,0],[0,0,0],[0,-2,1]]
P_2 = -(Q_+ - I)(Q_+ - 3I)    = [[0,0,0],[0,1,0],[0,2,0]]
P_3 = (Q_+ - I)(Q_+ - 2I)/2   = [[1,0,0],[0,0,0],[0,0,0]]
```

Idempotent, mutually annihilating, complete (`P_1+P_2+P_3 = I`), and
`Q_+ = 1 P_1 + 2 P_2 + 3 P_3`.  These are polynomial spectral projectors
of a diagonalizable non-symmetric matrix, not Hermitian Hilbert-space
projectors.

### Frozen Majorana operator

A Majorana `M_R` must be symmetric.  The v50 generation-basis combination
`ε P_1 + 2ε P_2 + 3 P_3 = [[3,0,0],[0,2ε,0],[0,2ε,ε]]` is **not**
symmetric.  The frozen operator is the unique symmetric matrix with those
eigenvalues on the `Q_+` eigenlines — the v69 eigenbasis form

```
M_R = M_scal * diag(ε, 2ε, 3),     ε = (φ₀^ret)² / A_Λ,     A_Λ = 10
```

| eigenvalue | formula | value | vs corpus |
|---|---|---|---|
| M₁ | ε M_scal | 8.651×10⁹ GeV | **=** v212/v372 decuple `M_scal φ₀²/A_Λ` **by definition of ε** |
| M₂ | 2ε M_scal | 1.730×10¹⁰ GeV | **new prediction** (no prior corpus scale) |
| M₃ | 3 M_scal | 9.180×10¹³ GeV | **=** v986 scalaron-trace rung |

The mixed insertion (ε on the `{1,2}`-subspace, unsuppressed 3 on `P_3`)
is a **reviewer ansatz**: `Q_+` supplies the spectrum `{1,2,3}` but does
not decide which eigenvalues carry ε.  Unification of leptogenesis and
seesaw in one operator is therefore a **reparametrization** of two
existing scales plus one interpolation rule, exact by construction for
`M_1` and `M_3`.  What is genuinely new is `M_2`.

### Frozen Dirac choice (and what is *not* frozen)

**No frozen 3×3 `Y_ν` exists in the corpus.**  v481 freezes only the
third-generation carrier normalisation `y_ν = y_t` `[P]` at matching.
v9 is a *light* Majorana `M_ν` texture (μ–τ), not a Dirac Yukawa.  v263
shows the seesaw map can land in the v9 class; its `m_D = diag(0.3,1,1)`
is an existence example, not a frozen Yukawa.  This pass does **not**
invent a texture.

Frozen: `y_3 = y_t(M_3) = 0.44197` (verbatim v481 1-loop runner).
Unfrozen: `y_1`, `y_2`.  Named diagnostic: `Y_ν = y_t(M_3) I`.
Aligned diagnostic: diagonal `Y_ν` in the `Q_+` eigenbasis (where `M_R`
is diagonal).  Seesaw: `M_ν = −(v²/2) Y_νᵀ M_R⁻¹ Y_ν` with `v = 246.22 GeV`.

### Naive (untextured) pass — K5 triggered

`Y_ν = y_t(M_3) I` into the hierarchical `M_R`.  The seesaw weights the
**light** heavy states.  After ADKLR rundown:

| observable | naive prediction | comparator | verdict |
|---|---|---|---|
| (m on Q₊-line 1, 2, 3) | 559, 279, 0.05124 eV | NuFIT 6.0 m₃ = 0.05013 eV | **killed** (×11151 on the heaviest light state) |
| Δm²₂₁ | 7.77×10⁴ eV² | 7.49×10⁻⁵ eV² | **killed** |
| Δm²₃₁ | 3.12×10⁵ eV² | 2.513×10⁻³ eV² | **killed** |
| Σ m_ν | 838 eV | DESI DR2 95% UL 0.0642 eV | **killed** (×13000) |
| m_β, m_ββ | not reported | KATRIN / KamLAND-Zen | need a 3×3 `Y_ν` in the charged-lepton basis |

This kills the **untextured** operator `Y ∝ I`, not `Q_+` itself.

### Constraint invert — `DATA_CONSTRAINS_TEXTURE`

With `y_3 = y_t(M_3)` frozen, the M₃ slice reproduces the v1 number
`m_3 = 0.05124 eV` (+2.2% vs NuFIT) — same inputs, not a new
confirmation.  Oscillation + DESI then require, in the aligned
eigenbasis:

| entry | constraint | target |
|---|---|---|
| y₃ | 0.4420 (frozen) | y_t(M₃), v481 `[P]` |
| y₂ / y₃ | 5.57×10⁻³ | NuFIT m₂ = √(Δm²₂₁) = 8.65 meV |
| y₂ / y₃ | 5.63×10⁻³ | v1-internal m₂ = m₃ √\|J_PMNS\| = 8.82 meV |
| y₁ / y₃ | 0 | NO floor m₁ = 0 |
| y₁ / y₃ | < 2.78×10⁻³ | DESI 95% residual room m₁ < 4.3 meV |

An aligned diagonal `Y_ν` that saturates those numbers would **tautologically**
reproduce the mass eigenvalues and would **not** produce the v270 PMNS
(`M_ν` would be diagonal in the `Q_+` basis).  `m_β` and `m_ββ` stay
`data_limited` until a frozen 3×3 `Y_ν` exists.

### Kill status (v2)

| id | status |
|---|---|
| K1–K3 | not triggered on the *textured* M₃ slice (same as v1) |
| K4 | not applicable (no m_ββ without 3×3 `Y_ν`) |
| **K5** | **triggered** — `Y ∝ I` is dead |
| K6 | not triggerable (no frozen corpus 3×3 `Y_ν`) |

### Verdict (v2 pass)

`DATA_CONSTRAINS_TEXTURE` — `Q_+` is corpus; the mixed insertion is an
ansatz; `{M_1, M_3}` is a reparametrization; `M_2 = 1.73×10¹⁰ GeV` is
the one new prediction; the untextured seesaw is killed by four orders of
magnitude; data require a hierarchical Dirac texture `|y₁|,|y₂| ~ 10⁻³ y₃`
that the corpus does not freeze.  Candidate row FLAV.NUSCALE.05 stays
`[C]/[N]`, mechanism `[O]`.  Nothing here moves a ledger marker.

## Value-grammar follow-up — `NU_RATIO_GRAMMAR_NULL` (2026-08-28)

After the frozen 3×3 census returned `CENSUS_NULL`, the pre-declared scalar
probe `experiments/tfpt-discovery/nu_ratio_grammar_probe.py` tested 255 unique
values of the form `φ₀^a r exp(-b)` (`a=0…4`, `b∈{0,5/6,1}`, and exactly 17
frozen rational/integer/ε coefficients).  Recomputing the v481/v2 chain gives

- `T1: y₂/y₃ = 0.0055725984`, one-sigma+RG band
  `[0.0054556776, 0.0056895192]`: two numerical hits,
  `φ₀(2/7)e⁻¹` and `2φ₀²`, but the look-elsewhere expectation is `10.7005`,
  so neither counts;
- `T2: y₁/y₃ < 0.0027751685`: 161 grammar values lie below the bound
  (this is not scored as a target hit);
- `T3: |Y₃e|/y₃ = √(φ₀e⁻⁵ᐟ⁶) = 0.1520145886`, mapped NuFIT band
  `[0.1500947539, 0.1539104777]`: zero hits, with look-elsewhere expectation
  `6.40076`.

The minimal PMNS embedding is
`Y = diag(y₁,y₂,y₃) U_PMNS†`; its third heavy row additionally requires
`|Y₃μ|/y₃ = |Y₃τ|/y₃ = 0.6988889629` and reactor phase `+4π/3`.
Three seeded scrambled controls produced a target-level hit rate of `1/3`
(one total candidate hit).  There is no significant related T1+T3 hit set,
so `hypotheses/nu_scalaron_v3.yaml` was **not created**.  The sharp missing
mechanism is a corpus-derived `Q_+`-to-charged-lepton basis map that supplies
the complex normalized entry `Y₃e/y₃ =
0.1520145886 exp(+4πi/3)` together with the atmospheric companion above.

## Reproduce

```bash
python scripts/derive_predictions.py       # v1 -> results/results.json
python scripts/leptogenesis_pass.py        # v1 leptogenesis follow-up
python scripts/derive_predictions_v2.py    # v2 -> results/results_v2.json
python ../tfpt-discovery/nu_qplus_spectral_matrix_probe.py
python ../tfpt-discovery/nu_texture_census_probe.py
python ../tfpt-discovery/nu_ratio_grammar_probe.py
```
