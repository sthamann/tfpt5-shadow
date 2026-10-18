# TFPT Carrier Rigidity — Formal Verification in Lean 4

This directory contains a **machine-checked proof in Lean 4** of the
load-bearing algebraic content of Paper 2 of the TFPT 4.5 series
(*Carrier Rigidity, Hypercharge, and the Standard Model Packet from
Boundary Polarization*).

## What is proved

> **Theorem (Carrier polynomial — corollary of boundary polarization).**
> Let `A` be a ring and let `P₋, P₊ ∈ A` be two orthogonal
> idempotents summing to `1`. Define the integer-scaled generator
>
> ```
> sixY := -2 · P₋ + 3 · P₊      (= 6 · Y)
> ```
>
> Then
>
> ```
> sixY² − sixY − 6 = 0,
> ```
>
> which, after dividing by `6` in a `ℚ`-algebra, is the determinant-
> normalised carrier polynomial `6 Y² − Y − 1 = 0` with
> `Y = -P₋/3 + P₊/2`.
>
> Formally verified: `TFPT.Carrier.Polarization.sixY_carrier_polynomial`.

> **Theorem (Discrete rigidity).** The integer pair `(q₋, q₊)` satisfying
>
> * `3 q₋ + 2 q₊ = 0`
> * `q₋ < 0 < q₊`
> * `Int.gcd q₋ q₊ = 1`
>
> is unique: `(q₋, q₊) = (-2, 3)`.
> After determinant normalisation `Y := (q₋ P₋ + q₊ P₊)/6` this fixes
> the rational eigenvalues `-1/3` and `1/2`.
>
> Formally verified: `TFPT.Carrier.Rigidity.unique_carrier_pair`.

> **Corollary (Hypercharge spectrum).** In the canonical 5×5
> diagonal model with `dim E₋ = 3, dim E₊ = 2`,
>
> ```
> Y = diag(-1/3, -1/3, -1/3, 1/2, 1/2),    tr Y = 0,
> 6 Y² − Y − 1 = 0.
> ```
>
> This is the Standard-Model hypercharge vector of the first chiral
> family in the carrier basis.
>
> Formally verified: `TFPT.Carrier.Hypercharge.trace_Y` and
> `TFPT.Carrier.Hypercharge.Y_carrier_polynomial`.

> **Theorem (Glue uniqueness + carrier index, v89/v92 cores; added
> 2026-06-10).** On the carrier discriminant form `A = ℤ₄ × ℤ₄` with
> `qZ(x,y) = (5x² + 3y²) mod 8`:
>
> * the isotropic elements are exactly
>   `{(0,0), (1,1), (1,3), (2,2), (3,1), (3,3)}`;
> * the order-4 isotropic elements generate exactly **two** cyclic
>   subgroups `H₁ = ⟨(1,1)⟩`, `H₂ = ⟨(1,3)⟩`, the unique Klein
>   four-subgroup is **not** isotropic, and the spinor swap
>   `(x,y) ↦ (x,−y)` provably exchanges `H₁ ↔ H₂` — the Lagrangian
>   (`μ₄`) glue is **unique up to the sheet**;
> * the unique isotropic order-2 element is `(2,2)` (the `SO(16)₁`
>   halfway stage of the extension tower);
> * carrier index arithmetic: `μ(D₅)·μ(A₃) = 16`, `[B:A]² = 16 ⇒`
>   Jones index `4 = |μ₄| = |ℤ₂|²`, and `16/4² = 1` (μ-additivity:
>   holomorphy follows from index 4); glue sectors are `h = 1`
>   currents and `248 = 45+15+64+64+60`.
>
> All by kernel `decide` (no `native_decide`).
> Formally verified: `TFPT.Carrier.GlueUniqueness.*` (ten theorems,
> wired into `AxiomCheck`/`AuditCheck`; mirrors
> `verification/v89_carrier_index_lemma.py` and
> `verification/v92_glue_uniqueness.py`, ledger `FORM.GLUE.01`).

> **Theorem (Seam-deck closure — the `QGEO.SYM.01` conditional theorem;
> added 2026-06-15).** The last open premise of TFPT, `QGEO.SYM.01`
> ("the carrier μ₄ clock is the conformal deck of the seam"), reduces
> (v201/v210) to: *the raw seam DtN sub-principal symbol is mark-local*
> ⇒ *the carrier clock preserves the quasi-free state* (`ω∘ρ=ω`). This
> module formalises that **implication**:
>
> * `geom_sum_fourth_root`: for `ζ : ℂ` with `ζ⁴ = 1`,
>   `Σ_{j<4} ζ^j = if ζ = 1 then 4 else 0` (4th-root character
>   orthogonality — the kernel that makes a μ₄-mark sum vanish off
>   `mod 4`);
> * `clock_gen_pow_four`, `mark_sum_residue_nonzero`: the clock
>   generator `-i` has order 4 and the three non-trivial residues give a
>   vanishing mark sum, so a μ₄-mark-sourced curvature is supported only
>   on modes `≡ 0 (mod 4)`;
> * `markLocal_blockDiagonal`: a mark-local Toeplitz symbol connects only
>   equal clock-characters (`f_{n-n'} ≠ 0 ⇒ (n ≡ n' mod 4)`), i.e.
>   `[ρ, M_f] = 0`;
> * `SeamDeckPremise` (structure): the **physical premise** that the raw
>   seam DtN is mark-local — a typed target consumed, *not* proved,
>   exactly as `CalderonProjector` encodes the Paper-1 analytic input;
> * `SeamDeckPremise.clock_invariant`: **given** the premise, the clock
>   commutes with the DtN ⇒ the quasi-free state is invariant (`ω∘ρ=ω`).
>
> So the **implication** mark-local ⇒ `ω∘ρ=ω` is `[F]` (machine-proved);
> the **premise** (the physical seam *is* mark-local) stays `[O]` — the
> one fundamental seam-identification postulate, **not** closed here.
> Formally verified: `TFPT.Carrier.SeamDeckClosure.*` (mirrors
> `verification/v201_seam_subprincipal_marks.py` and
> `verification/v210_mark_local_dtn.py`, ledger `FORM.QGEO.01`).

> **Theorem (Möbius uniformisation — the `QGEO.UNIFORM.01` normal form;
> added 2026-06-15).** The constructive `UNIFORM` node of the QGEO proof
> tree (v177): a genus-0 curve with four reduced marks and a faithful
> order-4 clock rotating them is Möbius-equivalent to `(ℙ¹, μ₄)`.
> Machine-proved (`TfptCarrier/MobiusUniformisation.lean`):
>
> * `rho_pow_four`, `rho_order_exactly_four`: the clock `ρ : z ↦ i z`
>   satisfies `ρ⁴ = id` and `ρ² ≠ id` (order exactly 4);
> * `sigma_invol`, `sigma_rho_sigma`: the reflection `σ : z ↦ 1/z` is an
>   involution with `σρσ = ρ⁻¹` — so `⟨ρ, σ⟩` is the dihedral `D₄` of
>   order 8 (the faithful `D₄` of v168);
> * `orbit_scales_to_mu4`: a non-fixed point `a ≠ 0` has orbit
>   `{a, ia, -a, -ia}`, scaling (`z ↦ z/a`) to `μ₄ = {1, i, -1, -i}`;
> * `sigma_perm_mu4`: `σ` permutes `μ₄` (fixes `1, -1`, swaps `i, -i`);
> * `mult_order_four_iff`: a multiplier map `z ↦ ζ z` has order exactly 4
>   iff `ζ = i ∨ ζ = -i` — the canonical representative is `z ↦ i z`.
>
> The geometric half of the seam realisation is thus `[F]`, **given** the
> four marks and the clock; the raw-seam marking obligation
> `QGEO.MARKS.01` stays `[O]`. Bundled as `uniformisation_normal_form`
> and signature-locked in `AuditContract.lean`. Formally verified:
> `TFPT.Carrier.MobiusUniformisation.*` (mirrors
> `verification/v177_seam_marking_kernel.py`, ledger `FORM.QGEO.02`).

> **Theorem (Cohomology grading — the `QGEO.COHOM.01` character node +
> MODULE parity; added 2026-06-15).** The constructive `COHOM` node of
> the QGEO proof tree (v177). Machine-proved
> (`TfptCarrier/CohomologyGrading.lean`):
>
> * `omega1/2/3_pullback`: the three `H^1(P^1 \ mu4)` eigenforms
>   `omega_k = z^(k-1)/(z^4-1)` have pullback character
>   `rho^* omega_k = i^k omega_k` under the clock `rho : z ↦ i z`
>   (`i^1 = i`, `i^2 = -1`, `i^3 = -i`) — each an exact rational-function
>   identity (the denominator is clock-invariant, `(iz)^4-1 = z^4-1`);
> * `character_grading`: the eigenvalues `(i, -1, -i)` are the characters
>   of weights `(1,2,3)` = the `A_3` exponents = `Spec(Q_+)`, rank
>   `3 = N_fam`;
> * `omega1/2/3_reflection` (MODULE parity): the reflection
>   `sigma : z ↦ 1/z` satisfies `sigma^* omega_1 = omega_3`,
>   `sigma^* omega_2 = omega_2`, `sigma^* omega_3 = omega_1` — the
>   integer-model parity `w_1 <-> w_3`, `w_2` fixed.
>
> The geometric `COHOM`/`MODULE`-parity nodes are thus `[F]`, given the
> marked curve `(P^1, mu4)` and the clock; the `MARKS`/`KERNEL`
> obligations and the MODULE *uniqueness* (multiplicity-free + residue
> normalisation) stay `[O]`/symbolic. Bundled as `cohom_grading` and
> signature-locked in `AuditContract.lean`. Formally verified:
> `TFPT.Carrier.CohomologyGrading.*` (mirrors
> `verification/v177_seam_marking_kernel.py`, ledger `FORM.QGEO.03`).

> **Theorem (Anchor rank-gap uniqueness — `ANCHOR.RANKGAP.UNIQUENESS`;
> added 2026-07-07).** The anchor ladder module (`AnchorLadder.lean`)
> reads `p₄ − p₃ = 8 = rank E₈` off the anchor `a = (1,1,2)`
> (`rank_step`). The new converse `rankgap_uniqueness` shows the
> equation *selects* the anchor: for any positive integers `x, y, z`
> with `x⁴+y⁴+z⁴ = x³+y³+z³+8`, the triple is `(1,1,2)` up to
> permutation — the per-entry contribution `w³(w−1)` is `0` at `w = 1`,
> `8` at `w = 2` and `≥ 54` for `w ≥ 3` (`cube_step_ge_54`,
> `overshoot_ge_three`), so exactly one entry is `2`. Axiom footprint:
> `[propext, Classical.choice, Quot.sound]` only. Scope (honest): this
> forces the anchor *within* positive integer triples of length 3; that
> the anchor is such a triple, and that the rank gap is the right
> normalisation, remain the axiom-side inputs.
> Formally verified: `TFPT.Carrier.AnchorLadder.rankgap_uniqueness`.

> **Cofinal-index noninterference hardening (added 2026-08-13).**
> `TfptCarrier/CofinalPredefinition.lean` separates the mathematical
> extraction theorem from the provenance premise that had previously
> appeared only in prose:
>
> * `cofinal_weil_for_fixed_idx` proves the extraction implication for an
>   arbitrary explicit `idx` with `StrictMono`, PSD, and form-convergence
>   hypotheses. Binder order prevents the theorem body from choosing
>   `idx`; it does **not** prove how the caller computed it.
> * `old_api_accepts_sign_mined_idx` is a kernel-checked negative example:
>   the former mathematical payload accepts a selector that branches on
>   measured signs.
> * `signMinedIndex_not_familyNoninterfering` rejects that exposed
>   selector under the natural extensional noninterference predicate.
> * `PredefinedCofinalHypothesis` and `cofinal_weil_predefined` require an
>   explicit `NoninterferenceContract.Predefined A idx` certificate.
> * `constantizedSelector_familyNoninterfering` proves the residual
>   limitation: after construction, any selected value can be presented
>   by a constant selector with the same output. Lean therefore cannot
>   recover algorithmic provenance from the extensional value `idx`.
>
> Exact residual external premise: a concrete application must define
> and audit the `Predefined` relation/source boundary so it excludes
> `A` and its sign outputs. Full kernel enforcement of historical
> information flow would require formalizing the construction language
> (or an equivalent trusted effect/provenance system). No RH statement
> is made.

> **The convergence hypothesis becomes the instantiated envelope
> (`CofinalEnvelope.lean`, added 2026-08-13).** `cofinal_weil` consumed
> `hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v) atTop
> (𝓝 (QW v))` as an opaque assumption. That premise is now a theorem on
> the paper side — per-element Galerkin form convergence at the explicit
> rate `O(D² log(1/D)) = O(2^{-2j} j)`, machine-checked in
> `verification/v912_form_convergence_theorem.py` (35/35,
> `FORMCONV-PROVEN`) — and this module carries the change into Lean:
>
> * `formErrorEnvelope` is the explicit level-`j` envelope
>   `(c_log · j + c_const) · D_j²` with `D_j = 2^{-j}`, and
>   `formErrorEnvelope_tendsto_zero` proves it vanishes (`n · rⁿ → 0`).
> * `mesh j = 2^{-j}` also fixes the **order** meant by "cofinal"
>   throughout: `(H_cof)` demands a ladder cofinal in the
>   *mesh-refinement* order in which this envelope holds, never one
>   cofinal only in the window/cap parameter. At fixed mesh `D₀` the
>   deployed read is already exactly cap-independent, so a
>   window-only-cofinal ladder is eventually constant and converges to
>   `QW + W_C[e_{D₀}]`, and positivity along it yields only
>   `QW ≥ −|W_C[e_{D₀}]|`.
> * `FormEnvelope` is the premise as a named structure: per-element
>   constants, a per-element window level (the DELTA-B threshold for
>   (H-grid)/(H-cap)/(H-align)), and the explicit error bound beyond it.
> * `tendsto_of_formEnvelope` **derives** `hconv` from the envelope, so
>   `cofinal_weil_of_envelope`, `cofinal_weil_for_fixed_idx_of_envelope`
>   and `cofinal_weil_predefined_of_envelope` state the extraction
>   theorem with the convergence hypothesis replaced by the instantiated
>   envelope.
> * `envelope_strictly_stronger_than_convergence` is the non-vacuity
>   lock: the convergent ladder `q m = 1/(m+1)` admits no envelope of
>   this shape, so the premise is a strict strengthening of `Tendsto`,
>   not a renaming of it; `witnessEnvelope`/`witness_cofinal_weil`
>   supply an inhabited instance with genuinely nonzero error at the
>   envelope rate and run the full assembly end to end.
>
> Axiom footprint `[propext, Classical.choice, Quot.sound]` only, no
> `sorry`, no `native_decide`. **Honest boundary:** the envelope itself
> is *not* discharged inside the kernel — it is a hypothesis of every
> theorem in the module, proved on paper plus the v912 gates. The
> formalisation gap is reduced (the assumption now has an explicit,
> checkable shape), not closed. The cofinal positivity hypothesis
> `(H_cof)` is untouched. No RH statement is made.

## Why this is interesting

* The carrier polynomial `6 Y² − Y − 1 = 0` is in earlier TFPT drafts
  *assumed*. Paper 2 demoted it to a **corollary** of the orthogonal-
  idempotent axioms + the integer Diophantine rigidity. This repo
  formalises that demotion in a proof assistant — so the SM hypercharge
  multiplet becomes a *theorem in a computer algebra system*, not an
  empirical input.

* The proof uses only four abstract axioms:
  `P₋² = P₋`, `P₊² = P₊`, `P₋ P₊ = 0`, `P₊ P₋ = 0`, `P₋ + P₊ = 1`.
  No analytic content, no SI units, no fitted constants.

* If the proof compiles in Lean 4 with Mathlib, it is — barring bugs in
  Lean's kernel itself — a *formal* certificate that the SM hypercharge
  spectrum follows from the TFPT boundary axioms.

## Repository layout

```
lean4-carrier-rigidity/
├── lean-toolchain                 # pinned: leanprover/lean4:v4.29.1
├── lakefile.lean                  # build config, Mathlib v4.29.1
├── TfptCarrier.lean               # full root (includes wall rungs)
└── TfptCarrier/
    ├── Polarization.lean          # Layer 1: sixY² − sixY − 6 = 0
    ├── Rigidity.lean              # Layer 3: (q₋, q₊) = (-2, 3)
    ├── Hypercharge.lean           # Layer 2: 5×5 model + tr Y = 0
    ├── Sanity.lean                # #eval smoke tests
    ├── AxiomCheck.lean            # #print axioms (non-wall headlines)
    ├── CIRoot.lean                # CI / 16 GB root (no wall rungs)
    └── WallLadderAudit.lean       # wall #print axioms / #check / examples (off-CI)
```

## How to build

### 1. Install `elan` (Lean's toolchain manager)

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh -s -- -y --default-toolchain none
export PATH="$HOME/.elan/bin:$PATH"
```

### 2. Build the project

From this directory:

```bash
lake update                # fetch Mathlib v4.29.1 and run cache hooks
lake exe cache get         # download pre-built Mathlib oleans (~3 min)
lake build TfptCarrier.CIRoot   # CI / 16 GB: every non-wall module
# lake build                 # full target — needs wall-rung oleans, see §4
```

The first `lake update` clones Mathlib (~500 MB). The cache step
downloads ~8 200 pre-built `.olean` files (~1 GB). GitHub Actions
runs `scripts/audit.sh --core`, which builds `TfptCarrier.CIRoot`
rather than the default `lake build` (the latter fans out over the
generated wall rungs and is SIGTERM/OOM on a 16 GB runner).

### 3. Re-check just the proofs

```bash
lake build TfptCarrier.CIRoot   # CI core (no wall rungs)
./scripts/audit.sh --core       # same target + the audit gate
lake build TfptCarrier          # full root, after §4
```

A successful core build elaborates every non-wall module plus
`AxiomCheck` / `AuditCheck` / `AuditContract`. The `#eval` outputs
from `Sanity.lean` and the axiom listings from `AxiomCheck.lean`
appear in the lake log. Any `sorry`, `admit`, kernel error, or
non-standard axiom dependency will be flagged. Wall-rung `#print axioms`
live in `WallLadderAudit.lean` and are checked only by a full
`./scripts/audit.sh`.

### 4. Rebuild the generated wall-ladder rungs (high memory)

`TfptCarrier/WallLadder/RungKz*.lean` are **generated** certificate
modules: each one drives a single kernel `decide` over a packed
Cholesky witness, so each is a multi-GB-to-multi-tens-of-GB elaboration
in its own right. `lakefile.lean` therefore pins a deliberately low
default per-process ceiling (`leanMemoryMb = 12288`, handed to Lean as
`-M`): with an uncapped Lake fan-out on a many-core machine, a plain
`lake build` would otherwise start every rung at once and exhaust
physical RAM. The default is a safety valve, not a build recipe — the
rungs **fail at 12 GB by design**, which is why a fresh clone cannot
pass a *full* `scripts/audit.sh` until the rung `.olean` files exist.
GitHub Actions never builds them: it uses `TfptCarrier.CIRoot` /
`scripts/audit.sh --core`. `WallCertifiedHead` and `WallLadderAudit`
stay off-CI with the rungs.

Build them with a raised ceiling and bounded concurrency:

```bash
./scripts/build_wall_ladder.sh                       # all missing rungs
BATCH=2 MEM_MB=163840 ./scripts/build_wall_ladder.sh # 2 at a time, 160 GB each
./scripts/build_wall_ladder.sh RungKz25 RungKz59     # named rungs only
```

`BATCH` bounds how many rungs are handed to one `lake build`
invocation (Lake 5 has no `-j`, so the number of targets *is* the
concurrency once the rest of the library is built), `MEM_MB` sets the
per-process `-M` ceiling, and `ONLY_MISSING=1` (the default) skips
rungs whose `.olean` is already present, so an interrupted run can
simply be restarted. Each batch reports its wall time and the peak
summed RSS of all live `lean` processes, so the cost is measured
rather than guessed.

Measured cost on this repository's 18 rungs (512 GB Apple-silicon
machine, Lean v4.29.1). Both time and memory grow steeply with the size
of the generated rung source — time roughly as its square, memory
faster than linearly:

| rung | source | wall time | peak RSS |
| --- | --- | --- | --- |
| `RungKz12` | 0.12 MB | 189 s | — |
| `RungKz20` | 0.15 MB | 253 s | ≤ 46 GB (pair peak 92.8 GB) |
| `RungKz14` | 0.17 MB | 363 s | > 48 GB |
| `RungKz32` | 0.32 MB | 1011 s | ~93 GB (pair peak 185.1 GB) |
| `RungKz39`+`RungKz46` | 0.37 + 0.39 MB | 1598 s | 360.3 GB for the pair |
| `RungKz27` | 0.41 MB | 1700 s | 200.4 GB, single process |

`RungKz14` is the cautionary entry: at a 48 GB ceiling it does not warn,
it **fails** after 987 s with `(kernel) excessive memory consumption
detected`. Budget accordingly — `BATCH=2` at `MEM_MB=163840` is
comfortable up to ~0.35 MB rungs on 512 GB, and from ~0.4 MB upward one
rung alone wants 200 GB or more, so use `BATCH=1` with a
several-hundred-GB ceiling there. Do not raise `BATCH` blindly: an
uncapped fan-out on this project has already exhausted 512 GB of RAM and
tripped the WindowServer watchdog, which is why the low default ceiling
exists. On a machine that cannot host the largest rungs, build what fits
and report the rungs you could not build; a partial rung set means
full `scripts/audit.sh` check (1) is *not* satisfied. The CI core
target (`./scripts/audit.sh --core`) does not require any rung
`.olean`.

`-M` is passed via `weakLeanArgs`, i.e. it is not part of Lake's build
trace: an `.olean` produced with a raised ceiling is accepted unchanged
by a later default-ceiling `lake build`, which is what makes this a
legitimate audit path rather than a different build. One caveat the
script handles for you: Lake caches the *elaborated* lakefile, so
`-K leanMemoryMb=…` is silently ignored unless the invocation also
passes `--reconfigure` — without it a build can fail at a ceiling it
never requested.

## Map to TFPT Paper 2

| Lean theorem | Paper 2 reference |
| --- | --- |
| `Polarization` (structure) | §2 "Carrier polynomial as a corollary", eq. for `P_±` |
| `Polarization.sixY_carrier_polynomial` | Theorem (Carrier polynomial from boundary polarization), proof spine |
| `Rigidity.unique_carrier_pair` | Inline integer argument: `3 q₋ + 2 q₊ = 0`, `q₋ < 0 < q₊`, `gcd = 1` |
| `Hypercharge.Y` and `Y_diag_entries` | `Y = diag(-1/3, -1/3, -1/3, 1/2, 1/2)` |
| `Hypercharge.trace_Y` | `tr_E Y = 0` |
| `Hypercharge.Y_carrier_polynomial` | `6 Y² − Y − 1 = 0` on the concrete model |

## Status

> ✅ **Verified on this machine** with `lake build`
> (Lean 4.29.1 + Mathlib v4.29.1, macOS arm64).
> All four theorems compile, zero `sorry`s, no `admit`s.

```
$ lake build
Build completed successfully (1231 jobs).

#eval Y.trace                          -- 0
#eval ((6 : ℚ) • (Y * Y) - Y - 1)      -- !![0,0,0,0,0; 0,0,0,0,0; ...]
```

`#print axioms` for each of the four headline theorems reports only
the three standard Lean axioms `propext`, `Classical.choice`,
`Quot.sound`. No private hypotheses, no `sorry`-laundering, no
domain-specific axioms. The full chain
`Polarization → Rigidity → Hypercharge` is formally verified.

| Module | Status | Lines | Axioms |
| --- | --- | --- | --- |
| `Polarization.lean` | ✅ compiles | ~150 | propext, Classical.choice, Quot.sound |
| `Rigidity.lean`     | ✅ compiles | ~100 | propext, Classical.choice, Quot.sound |
| `Hypercharge.lean`  | ✅ compiles |  ~95 | propext, Classical.choice, Quot.sound |
| `Sanity.lean`       | ✅ `#eval`s match expected output | 30 | n/a |
| `AxiomCheck.lean`   | ✅ `#print axioms` confirms cleanness | 25 | n/a |

## Caveats and audit surface

* This formalises the *algebraic* corollary of Paper 2. The
  representation-theoretic *premises* (compact Higgs index → `dim E₊ = 2`;
  primitive indecomposable Yukawa type → `dim E₋ = 3`) are imported as
  numerical inputs to the `Hypercharge` model. A future Layer 4 would
  formalise those premises directly from the index-theoretic data, which
  is substantially more work and is out of scope here.

* The trace identity uses `Matrix.trace` on `Fin 5 × Fin 5` rational
  matrices. The corresponding abstract statement — `tr Y = 0` for
  *any* faithful finite-dimensional representation with the prescribed
  ranks — is an immediate corollary but is not separately stated.

* Mathlib version is pinned to `v4.29.1` for reproducibility. Pinning
  forward is straightforward, but bumping silently is discouraged.

## Next steps

1. GitHub Actions (`lean.yml`) already runs `scripts/audit.sh --core`
   on `TfptCarrier.CIRoot`. The full wall-rung audit stays off-CI
   (`scripts/build_wall_ladder.sh`, `AUDIT_TRANSCRIPT.txt`).
2. Add a `Tests/Sanity.lean` file with `#eval` checks that print
   the diagonal of `Y` and the value of `trace Y` so that humans can
   read the certificate without running Lean themselves.
3. Extend the formalisation to the discrete `Z₆` gauge quotient
   `G_phys = (SU(3) × SU(2) × U(1)_Y) / Z₆`. This requires
   group-theoretic machinery beyond the current scope.
