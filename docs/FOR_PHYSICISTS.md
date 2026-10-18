# TFPT for physicists

> A 10-minute orientation: the assumptions, what is derived vs. identified, and where the theory
> is honestly incomplete.

> **Strict TOE scope (2026-09-05).** The strongest closed statements below belong to the
> dimensionless compiler or to finite subgates. Round 3 (`v1022`–`v1025`) does not close a TOE
> gate: T1–T8 and `TFPT.TOE.COMPLETE.01` all remain `[O]`, and one shared 3+1D parent satisfying
> T3–T8 is still absent. In particular, the gravity route is conditional on the missing 4D QFT
> package; it is not a construction of that package.

## The two assumptions

TFPT starts from exactly two dimensionless inputs, and claims both are *not* free:

1. **P1 — the seam constant** `c₃ = 1/(8π)`. This is the Einstein/Jacobson `8π` coefficient. It is
   the elementary-symmetric datum `1/(2·e₁(a)·π)` of the anchor `a = (1,1,2)`, and it is triply
   over-determined — anchor, one-sided Gauss–Bonnet geometry (`|μ₄| = |ℤ₂|·χ(S²) = 4`), and
   Hawking/Einstein thermodynamics all fix the same `8π` (`v358`/`v359`).
2. **P2 — the carrier rank** `g_car = 5`. This is the unique Pascal solution of
   `2^(g−1) = C(g,0)+C(g,1)+C(g,2)` and an *over-determined bootstrap fixed point* forced three
   independent ways via the `E8` closure (`v2`, `v14`, `v23`).

So on the dimensionless axis there is **no free load-bearing number** — only `π` is primitive. The
sharpest statement is a candidate: *a parameter-free compiler for the dimensionless structure of
fundamental physics.*

## What is derived (in the compiler)

Read [`tfpt_1_architecture_e8.tex`](../tfpt_1_architecture_e8.tex) (core) and
[`tfpt_2_standard_model.tex`](../tfpt_2_standard_model.tex) (SM):

- **Gauge group + one Higgs + three generations** from the carrier `D5 ⊕ A3 + μ4` and its half-spinor
  (`sin²θ_W = 3/8` at the carrier scale; `N_fam = 3 = rank A3`).
- **`α⁻¹ = 137.0359992`** as the unique root of a boundary `U(1)` Ward identity (existence +
  uniqueness, interval-arithmetic, `v3`).
- **Flavor**: an integer operator ladder (`det(Q,K,R,L) = (3,4,8,20)`, `∏ = 1920 = |W(D5)|`);
  charged-lepton coefficients `(16/7, 4/3, 7/6)` exactly; quark mass *ratios* as integer Plücker
  readouts. Absolute amplitudes need one declared normalisation (`U_point`).
- **Gravity (conditional route)**: assuming the required local 4D QFT and
  entanglement-equilibrium hypotheses, the entanglement first law with TFPT's atoms gives
  `G_ab + Λ g_ab = c₃⁻¹ T_ab`, both coefficients fixed, `Λ` from `α` (`v60`, `v358`/`v359`).
- **Cosmology**: `Ω_b`, the Starobinsky scalaron mass, `Λ ~ e^(−2α⁻¹)`, cosmic birefringence
  `β = φ₀/(4π) ≈ 0.2424°`.

## What is *identified*, not derived

TFPT is scrupulous about this line. The **physical identification** of the boundary "seam" object
(what it *is*, physically) and the transport operator behind the interfaces stay `[P]`/`[C]`. See
[`CLAIMS.md`](CLAIMS.md) for the marker system.

## What is *not* claimed (the frontier)

Read [`tfpt_4_frontier.tex`](../tfpt_4_frontier.tex). These are deliberately typed as **interfaces**,
never quoted as compiler outputs:

- The strict physical completeness contract `TFPT.TOE.COMPLETE.01`: all gates T1–T8 remain
  `[O]`; the shared 3+1D parent, chiral measure/mirror continuum, IR reconstruction, physical
  flavor texture, microscopic TFPT massless spin-2 embedding and unique global initial state
  are not constructed. Round 7 constructs a separate positive local covariant free curvature
  field with helicities ±2 (`v1031`/`v1032`); this does not derive the shared parent or universal
  nonlinear coupling. Prescribed-source Ward propagation (`v1035`) is only a linear target result.
- `m_p/m_e` (QCD scale), `η_B` (leptogenesis), Koide `Q`, the axion relic abundance — one transfer
  functor `F_transfer` with typed runnable solvers and kill tests (`v371`–`v374`, guarded by `v187`).
- The full non-perturbative ambient quantum-gravity measure (`QG.AMB.01`) — a `[C]` redundancy,
  gap-decoupled from every frozen readout (`v369`, `v423`).
- One dimensionful anchor — the metrology unit `v_geo` (`= 1/√G`), which the No-Unit Theorem shows a
  scale-invariant `c=8` seam *cannot* produce internally.

## The red team

[`tfpt_5_redteam.tex`](../tfpt_5_redteam.tex) is an adversarial stress test of the five load-bearing
reductions (Targets A–E): where each would fail and which assumptions are truly necessary. It is run
by `verification/redteam/run_redteam.py`.

## Run it

```bash
pip install -r requirements.txt
./verify            # headline check
./verify --full     # the whole suite
```

Then read the interactive [reading guide](https://www.fixpoint-theory.com/orientation) and the
[falsification page](https://www.fixpoint-theory.com/falsification). The kill tests are in
[`FALSIFICATION.md`](FALSIFICATION.md).
