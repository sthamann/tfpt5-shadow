/-
  GaussianShells — the global shell theorem's FORMAL SKELETON.
  ================================================================

  THE PATTERN (2026-08-08 evening plan, module 2; the house
  discipline): the ARITHMETIC CONSEQUENCE CHAIN is kernel-checked
  here, while the finite/structural inputs stay NAMED hypotheses
  with their verification provenance typed on each field.  What the
  probes and the classical literature supply is bundled in
  `ShellSystem`; what follows from it is theorems — so the global
  shell statement can never hide a gap between the two.

  THE SETTING (abstract — no lattice is enumerated here).  Three
  integer sequences: ΘL n (the full-lattice shell count at norm n),
  Θ0 n (the zero-coset shell count), Θv n (the COMMON shell count
  of each of the 15 nonzero cosets).  The three inputs:

    (H1) EQUIDISTRIBUTION: 15·Θv n = ΘL n − Θ0 n exactly — the 15
         nonzero cosets share the remainder equally.
    (H2) DOUBLING: Θ0(2m) = ΘL(m) and Θ0(2m+1) = 0 — the zero
         coset is the (1+i)-rescaled full lattice.
    (H3) THETA IDENTITY: ΘL n = 240·σ₃(n) for n ≥ 1 — the E₈/E₄
         Eisenstein identity.

  WHAT THIS MODULE PROVES from (H1)–(H3), kernel-checked (no
  `sorry`, no `native_decide`; every statement is an EXACT integer
  identity — the −1/15 ratio is stated multiplied out, no division
  ever appears):

    * `decomposition` / `dvd_diff` — ΘL n = Θ0 n + 15·Θv n and the
      exactness 15 ∣ (ΘL n − Θ0 n) (H1 restated; the division in
      the informal Θv = (ΘL − Θ0)/15 is exact).
    * `walsh_formula` — THE WALSH FORMULA: for the nontrivial
      Walsh coefficient Θ̂u := Θ0 − Θv (of 16 cosets, 8 carry +,
      8 carry −; the zero coset always +; definition below):
          15·Θ̂u n = 16·Θ0 n − ΘL n.
    * `theta_v_odd` — odd shells: Θv(2m+1) = 16·σ₃(2m+1) (the
      exact division of 240 by 15).
    * `walsh_odd` — THE ODD-SHELL THEOREM:
          Θ̂u(2m+1) = −16·σ₃(2m+1),
      and `walsh_odd_ratio` — the exact-ratio form
          15·Θ̂u(2m+1) = −ΘL(2m+1)
      (the "−1/15 of the full theta" statement as an integer
      identity).
    * `walsh_even` — THE EVEN-SHELL FORMULA: for m ≥ 1,
          Θ̂u(2m) = 16·(16·σ₃(m) − σ₃(2m)).

  PROVENANCE OF THE INPUTS (typed on the fields, named — not
  proven here):
    (H1) the Sp(4,2) transitivity on the 15 nonzero cosets plus
         shell invariance of the deck action — machine-verified in
         the shell probes (finite range).
    (H2) the (1+i) norm-doubling bijection — exact by the Gaussian
         integer factorization 2 = −i(1+i)².
    (H3) classical (Jacobi/Eisenstein E₄ = theta of the even
         unimodular rank-8 lattice) — CITED, plus finite-range
         machine verification in the probes.
  σ₃ itself is mathlib's `ArithmeticFunction.sigma 3` — nothing
  bespoke.  No modular-forms machinery is imported or claimed; the
  skeleton is exactly the integer arithmetic of the argument.
-/
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Tactic

namespace TfptCarrier
namespace GaussianShells

open ArithmeticFunction

/-- σ₃ as an integer-valued function: the sum of cubes of divisors
(mathlib's `ArithmeticFunction.sigma 3`, cast to ℤ). -/
def sigma3 (n : ℕ) : ℤ := (sigma 3 n : ℤ)

/-- **THE NAMED INPUT BUNDLE** — the three structural hypotheses of
the global shell theorem, as data a consumer must supply.  The
consequence chain below is proven FROM this structure; nothing in
this module proves any field. -/
structure ShellSystem where
  /-- Full-lattice shell count at norm n. -/
  ΘL : ℕ → ℤ
  /-- Zero-coset shell count at norm n. -/
  Θ0 : ℕ → ℤ
  /-- The common shell count of each of the 15 nonzero cosets. -/
  Θv : ℕ → ℤ
  /-- **(H1) EQUIDISTRIBUTION**: the 15 nonzero cosets share the
  complement equally — 15·Θv n = ΘL n − Θ0 n exactly (the informal
  Θv = (ΘL − Θ0)/15 with the division certified exact).
  PROVENANCE: Sp(4,2) transitivity on the nonzero cosets + shell
  invariance of the deck action — machine-verified in the shell
  probes (finite range); named here, not proven. -/
  equidist : ∀ n, 15 * Θv n = ΘL n - Θ0 n
  /-- **(H2a) DOUBLING, even**: Θ0(2m) = ΘL(m) — the zero coset is
  the (1+i)-rescaled copy of the full lattice; multiplication by
  (1+i) doubles the norm.  PROVENANCE: exact, from the Gaussian
  factorization 2 = −i(1+i)²; named here, not proven. -/
  doubling_even : ∀ m, Θ0 (2 * m) = ΘL m
  /-- **(H2b) DOUBLING, odd**: Θ0(2m+1) = 0 — the (1+i)-multiples
  have even norm only.  PROVENANCE: as (H2a). -/
  doubling_odd : ∀ m, Θ0 (2 * m + 1) = 0
  /-- **(H3) THE THETA IDENTITY**: ΘL n = 240·σ₃(n) for n ≥ 1 —
  the Eisenstein identity E₄ = theta series of the even unimodular
  rank-8 lattice.  PROVENANCE: classical (Jacobi/Eisenstein),
  CITED; finite-range machine verification in the probes; named
  here, not proven. -/
  theta_id : ∀ n, n ≠ 0 → ΘL n = 240 * sigma3 n

namespace ShellSystem

variable (S : ShellSystem)

/-! ### The exactness of (H1) -/

/-- The division in Θv = (ΘL − Θ0)/15 is exact. -/
theorem dvd_diff (n : ℕ) : (15 : ℤ) ∣ S.ΘL n - S.Θ0 n :=
  ⟨S.Θv n, (S.equidist n).symm⟩

/-- The shell decomposition: ΘL n = Θ0 n + 15·Θv n — the zero coset
plus the 15 equal nonzero cosets. -/
theorem decomposition (n : ℕ) : S.ΘL n = S.Θ0 n + 15 * S.Θv n := by
  have h := S.equidist n
  linarith

/-! ### The Walsh coefficient -/

/-- **The nontrivial Walsh coefficient** Θ̂u := Θ0 − Θv.  Of the 16
cosets, a nontrivial character u is +1 on 8 (among them the zero
coset) and −1 on 8; with all 15 nonzero cosets equal (H1) the
signed sum Θ0 + 7·Θv − 8·Θv collapses to Θ0 − Θv — that finite
Walsh combinatorics is absorbed into this DEFINITION (typed here,
so nothing informal remains behind it). -/
def walshU (n : ℕ) : ℤ := S.Θ0 n - S.Θv n

/-- **THE WALSH FORMULA**: 15·Θ̂u n = 16·Θ0 n − ΘL n — the exact
integer form of Θ̂u = (16·Θ0 − ΘL)/15, pure algebra from (H1). -/
theorem walsh_formula (n : ℕ) :
    15 * S.walshU n = 16 * S.Θ0 n - S.ΘL n := by
  have h := S.equidist n
  simp only [walshU]
  linarith

/-! ### Odd shells -/

/-- Odd shells of the nonzero cosets: Θv(2m+1) = 16·σ₃(2m+1) — the
240/15 division, exact ((H1) + (H2b) + (H3)). -/
theorem theta_v_odd (m : ℕ) :
    S.Θv (2 * m + 1) = 16 * sigma3 (2 * m + 1) := by
  have h := S.equidist (2 * m + 1)
  rw [S.doubling_odd m, sub_zero,
    S.theta_id (2 * m + 1) (by omega)] at h
  exact mul_left_cancel₀ (by norm_num : (15 : ℤ) ≠ 0)
    (by linarith)

/-- **THE ODD-SHELL THEOREM**: Θ̂u(2m+1) = −16·σ₃(2m+1) — the
nontrivial Walsh coefficient on odd shells is exactly −16 times the
divisor cube sum. -/
theorem walsh_odd (m : ℕ) :
    S.walshU (2 * m + 1) = -16 * sigma3 (2 * m + 1) := by
  simp only [walshU, S.doubling_odd m, S.theta_v_odd m]
  ring

/-- **The exact-ratio form**: 15·Θ̂u(2m+1) = −ΘL(2m+1) — "the
nontrivial Walsh coefficient is −1/15 of the full theta on odd
shells", as an integer identity with no division anywhere. -/
theorem walsh_odd_ratio (m : ℕ) :
    15 * S.walshU (2 * m + 1) = -S.ΘL (2 * m + 1) := by
  rw [S.walsh_formula, S.doubling_odd m]
  ring

/-! ### Even shells -/

/-- **THE EVEN-SHELL FORMULA**: for m ≥ 1,
Θ̂u(2m) = 16·(16·σ₃(m) − σ₃(2m)) — the doubling (H2a) routes the
even shells through the theta identity at BOTH m and 2m. -/
theorem walsh_even (m : ℕ) (hm : m ≠ 0) :
    S.walshU (2 * m) = 16 * (16 * sigma3 m - sigma3 (2 * m)) := by
  refine mul_left_cancel₀ (by norm_num : (15 : ℤ) ≠ 0) ?_
  rw [S.walsh_formula, S.doubling_even m, S.theta_id m hm,
    S.theta_id (2 * m) (by omega)]
  ring

end ShellSystem

end GaussianShells
end TfptCarrier
