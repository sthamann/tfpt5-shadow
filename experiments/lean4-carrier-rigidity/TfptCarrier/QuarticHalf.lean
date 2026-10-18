/-
  QuarticHalf — the μ4 orbit factor and f₄ = 576·q², certified.
  ==============================================================

  Machine-checked algebraic cores of the PROVABLE part of the theorem
  candidate E8.QUARTIC.HALF.01 (the quartic invariant restriction:
  restricting the W(E8) root power sums F_d to the holomorphic
  eigenspace V^{1,0} = ker(J − i) kills exactly the degrees d ≢ 0
  mod 4).  Numeric counterpart:
  experiments/tfpt-discovery/quartic_half_probe.py (22/22, verdict
  QUARTIC-HALF-ALIVE).

  Q1 — the μ4-orbit mechanism (probe layer L1, a symbolic PROOF of
  the vanishing half, honest: it is mod-4-trivial, not
  degree-list-specific):
    * `orbit_factor_vanishes` / `orbit_factor_multiple` /
      `orbit_factor_iff`: 1 + (−i)^d + (−1)^d + i^d = 0 ⟺ d ≢ 0
      mod 4 (value 4 at multiples of 4), over ℂ;
    * `weight_pair_J`: the per-pair weight law of the probe (II2.1):
      the holomorphic weight of the J-image pair (a,b) ↦ (−b,a) is
      −i times the weight, (−b) − i·a = −i·(a − i·b);
    * `orbit_powersum_vanishes`: consequently every μ4 orbit
      {α, Jα, −α, −Jα} with weights {t, −i·t, −t, i·t} contributes
      t^d·(1 + (−i)^d + (−1)^d + i^d) = 0 to F_d| for ALL d ≢ 0
      mod 4 — the entire vanishing half {2,14,18,30} (and the
      non-listed 6, 10, 22, 26 alike, `vanishing_half_orbit` /
      `trivial_extras_mod_four`);
    * the degree bookkeeping: Deg W(E8) = {2,8,12,14,18,20,24,30}
      splits mod 4 into the G31 half {8,12,20,24} and the vanishing
      half {2,14,18,30} (`deg_we8_mod_four_split`).

  Q2 — the first invariant-theory layer (probe II2.3/II2.5): the full
  symbolic 8-variable identity over the explicit 240 doubled E8 roots

      Σ_{α ∈ rd240} ⟨α, x⟩⁴ = 576·(Σᵢ xᵢ²)²    (`quartic_powersum`),

  proved by `ring` over any commutative ring after unfolding the
  explicit 240-element root list (split into the 112 D8-type and the
  128 spinor roots, `quartic_d8_block` / `quartic_spinor_block`).
  Corollaries: V^{1,0} is q-isotropic (`holomorphic_isotropy`,
  1 + (−i)² = 0 per pair), hence F₄|_{V^{1,0}} = 0 identically
  (`quartic_restriction_vanishes`) — W(E8) has no basic invariant in
  degree 4, the first G31-consistency point.

  Root-list integrity is kernel `decide`: 240 pairwise-distinct
  tuples, all of ambient norm 8 (doubled coordinates), closed under
  the μ4 rotation J.

  HONEST SCOPE.  The load-bearing G31 content of the candidate — that
  F₈|, F₁₂|, F₂₀|, F₂₄| are G31-invariant, algebraically independent
  and (via Chevalley + the Molien-unique degree quadruple) a system
  of BASIC invariants generating the full G31 ring — is NOT
  formalized here; it rests on the probe's exact-point Jacobian and
  reflection checks plus the cited Chevalley theorem (probe layers
  L3/L4).  What is formal is the μ4 vanishing mechanism (Q1) and the
  degree-4 collapse f₄ = 576·q² (Q2).
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.QuarticHalf

/-! ### Q1. The μ4 orbit factor over ℂ -/

theorem I_pow_four : Complex.I ^ 4 = 1 := by
  have h : Complex.I ^ 4 = (Complex.I ^ 2) ^ 2 := by ring
  rw [h, Complex.I_sq]; norm_num

theorem neg_I_pow_four : (-Complex.I) ^ 4 = 1 := by
  have h : (-Complex.I) ^ 4 = (Complex.I ^ 2) ^ 2 := by ring
  rw [h, Complex.I_sq]; norm_num

/-- At multiples of 4 the μ4 orbit factor is 4 (nonzero). -/
theorem orbit_factor_multiple (d : ℕ) (hd : d % 4 = 0) :
    (1 : ℂ) + (-Complex.I) ^ d + (-1) ^ d + Complex.I ^ d = 4 := by
  obtain ⟨q, rfl⟩ : ∃ q, d = 4 * q := ⟨d / 4, by omega⟩
  rw [pow_mul, pow_mul, pow_mul, neg_I_pow_four, I_pow_four,
    show ((-1 : ℂ)) ^ 4 = 1 by norm_num]
  norm_num

/-- **The μ4 orbit factor**: 1 + (−i)^d + (−1)^d + i^d = 0 for every
d ≢ 0 mod 4 (case split on d mod 4). -/
theorem orbit_factor_vanishes (d : ℕ) (hd : d % 4 ≠ 0) :
    (1 : ℂ) + (-Complex.I) ^ d + (-1) ^ d + Complex.I ^ d = 0 := by
  obtain ⟨q, r, hr, rfl⟩ : ∃ q r, r < 4 ∧ d = 4 * q + r :=
    ⟨d / 4, d % 4, Nat.mod_lt _ (by norm_num), (Nat.div_add_mod d 4).symm⟩
  rw [pow_add, pow_add, pow_add, pow_mul, pow_mul, pow_mul,
    neg_I_pow_four, I_pow_four, show ((-1 : ℂ)) ^ 4 = 1 by norm_num]
  simp only [one_pow, one_mul]
  interval_cases r
  · exfalso; omega
  · ring
  · linear_combination (2 : ℂ) * Complex.I_sq
  · ring

/-- The full characterisation: the orbit factor vanishes iff d ≢ 0
mod 4. -/
theorem orbit_factor_iff (d : ℕ) :
    ((1 : ℂ) + (-Complex.I) ^ d + (-1) ^ d + Complex.I ^ d = 0)
      ↔ d % 4 ≠ 0 := by
  constructor
  · intro h hd
    rw [orbit_factor_multiple d hd] at h
    norm_num at h
  · exact orbit_factor_vanishes d

/-- **The weight law W(Jα) = −i·W(α)** (probe II2.1), per μ4 pair: the
holomorphic weight a − i·b of a coordinate pair (a, b) transforms
under J : (a, b) ↦ (−b, a) by the factor −i. -/
theorem weight_pair_J (a b : ℂ) :
    (-b) - Complex.I * a = -Complex.I * (a - Complex.I * b) := by
  linear_combination (-b) * Complex.I_sq

/-- **The orbit power-sum kill**: an μ4 orbit {α, Jα, −α, −Jα} has
holomorphic weights {t, −i·t, −t, i·t} (by `weight_pair_J`), so its
contribution to F_d| vanishes identically for every d ≢ 0 mod 4. -/
theorem orbit_powersum_vanishes (t : ℂ) (d : ℕ) (hd : d % 4 ≠ 0) :
    t ^ d + (-Complex.I * t) ^ d + (-t) ^ d + (Complex.I * t) ^ d = 0 := by
  have expand : t ^ d + (-Complex.I * t) ^ d + (-t) ^ d
      + (Complex.I * t) ^ d
      = (1 + (-Complex.I) ^ d + (-1) ^ d + Complex.I ^ d) * t ^ d := by
    rw [mul_pow, mul_pow, show (-t) = (-1 : ℂ) * t by ring, mul_pow]
    ring
  rw [expand, orbit_factor_vanishes d hd, zero_mul]

/-- The review's vanishing half {2, 14, 18, 30} is all ≢ 0 mod 4. -/
theorem vanishing_half_mod_four :
    ∀ d ∈ ([2, 14, 18, 30] : List ℕ), d % 4 ≠ 0 := by decide

/-- HONESTY (probe II2.2): the mechanism also kills 6, 10, 22, 26 —
the vanishing half is mod-4-trivial, not degree-list-specific. -/
theorem trivial_extras_mod_four :
    ∀ d ∈ ([6, 10, 22, 26] : List ℕ), d % 4 ≠ 0 := by decide

/-- The surviving G31 half {8, 12, 20, 24} is all ≡ 0 mod 4. -/
theorem g31_half_mod_four :
    ∀ d ∈ ([8, 12, 20, 24] : List ℕ), d % 4 = 0 := by decide

/-- Deg W(E8) = {2,8,12,14,18,20,24,30} splits mod 4 into the G31 half
and the vanishing half (probe II1.4). -/
theorem deg_we8_mod_four_split :
    (([2, 8, 12, 14, 18, 20, 24, 30] : List ℕ).filter
        fun d => d % 4 == 0) = [8, 12, 20, 24] ∧
    (([2, 8, 12, 14, 18, 20, 24, 30] : List ℕ).filter
        fun d => d % 4 != 0) = [2, 14, 18, 30] := by decide

/-- The vanishing half, orbitwise: for d ∈ {2, 14, 18, 30} every μ4
orbit power sum dies. -/
theorem vanishing_half_orbit (d : ℕ) (hd : d ∈ ([2, 14, 18, 30] : List ℕ))
    (t : ℂ) :
    t ^ d + (-Complex.I * t) ^ d + (-t) ^ d + (Complex.I * t) ^ d = 0 :=
  orbit_powersum_vanishes t d (vanishing_half_mod_four d hd)

/-! ### Q2. The 240 doubled E8 roots and f₄ = 576·q² -/

/-- An E8 root in doubled integer coordinates. -/
abbrev Z8 := ℤ × ℤ × ℤ × ℤ × ℤ × ℤ × ℤ × ℤ

set_option synthInstance.maxSize 512 in
/-- Decidable equality for the 8-fold product (the nested instance
term exceeds the default `synthInstance.maxSize`). -/
instance : DecidableEq Z8 :=
  inferInstanceAs (DecidableEq (ℤ × ℤ × ℤ × ℤ × ℤ × ℤ × ℤ × ℤ))

/-- The 112 D8-type roots 2(±eᵢ ± eⱼ). -/
def rdD8 : List (Z8) :=
  [(-2, -2, 0, 0, 0, 0, 0, 0),
   (-2, 0, -2, 0, 0, 0, 0, 0),
   (-2, 0, 0, -2, 0, 0, 0, 0),
   (-2, 0, 0, 0, -2, 0, 0, 0),
   (-2, 0, 0, 0, 0, -2, 0, 0),
   (-2, 0, 0, 0, 0, 0, -2, 0),
   (-2, 0, 0, 0, 0, 0, 0, -2),
   (-2, 0, 0, 0, 0, 0, 0, 2),
   (-2, 0, 0, 0, 0, 0, 2, 0),
   (-2, 0, 0, 0, 0, 2, 0, 0),
   (-2, 0, 0, 0, 2, 0, 0, 0),
   (-2, 0, 0, 2, 0, 0, 0, 0),
   (-2, 0, 2, 0, 0, 0, 0, 0),
   (-2, 2, 0, 0, 0, 0, 0, 0),
   (0, -2, -2, 0, 0, 0, 0, 0),
   (0, -2, 0, -2, 0, 0, 0, 0),
   (0, -2, 0, 0, -2, 0, 0, 0),
   (0, -2, 0, 0, 0, -2, 0, 0),
   (0, -2, 0, 0, 0, 0, -2, 0),
   (0, -2, 0, 0, 0, 0, 0, -2),
   (0, -2, 0, 0, 0, 0, 0, 2),
   (0, -2, 0, 0, 0, 0, 2, 0),
   (0, -2, 0, 0, 0, 2, 0, 0),
   (0, -2, 0, 0, 2, 0, 0, 0),
   (0, -2, 0, 2, 0, 0, 0, 0),
   (0, -2, 2, 0, 0, 0, 0, 0),
   (0, 0, -2, -2, 0, 0, 0, 0),
   (0, 0, -2, 0, -2, 0, 0, 0),
   (0, 0, -2, 0, 0, -2, 0, 0),
   (0, 0, -2, 0, 0, 0, -2, 0),
   (0, 0, -2, 0, 0, 0, 0, -2),
   (0, 0, -2, 0, 0, 0, 0, 2),
   (0, 0, -2, 0, 0, 0, 2, 0),
   (0, 0, -2, 0, 0, 2, 0, 0),
   (0, 0, -2, 0, 2, 0, 0, 0),
   (0, 0, -2, 2, 0, 0, 0, 0),
   (0, 0, 0, -2, -2, 0, 0, 0),
   (0, 0, 0, -2, 0, -2, 0, 0),
   (0, 0, 0, -2, 0, 0, -2, 0),
   (0, 0, 0, -2, 0, 0, 0, -2),
   (0, 0, 0, -2, 0, 0, 0, 2),
   (0, 0, 0, -2, 0, 0, 2, 0),
   (0, 0, 0, -2, 0, 2, 0, 0),
   (0, 0, 0, -2, 2, 0, 0, 0),
   (0, 0, 0, 0, -2, -2, 0, 0),
   (0, 0, 0, 0, -2, 0, -2, 0),
   (0, 0, 0, 0, -2, 0, 0, -2),
   (0, 0, 0, 0, -2, 0, 0, 2),
   (0, 0, 0, 0, -2, 0, 2, 0),
   (0, 0, 0, 0, -2, 2, 0, 0),
   (0, 0, 0, 0, 0, -2, -2, 0),
   (0, 0, 0, 0, 0, -2, 0, -2),
   (0, 0, 0, 0, 0, -2, 0, 2),
   (0, 0, 0, 0, 0, -2, 2, 0),
   (0, 0, 0, 0, 0, 0, -2, -2),
   (0, 0, 0, 0, 0, 0, -2, 2),
   (0, 0, 0, 0, 0, 0, 2, -2),
   (0, 0, 0, 0, 0, 0, 2, 2),
   (0, 0, 0, 0, 0, 2, -2, 0),
   (0, 0, 0, 0, 0, 2, 0, -2),
   (0, 0, 0, 0, 0, 2, 0, 2),
   (0, 0, 0, 0, 0, 2, 2, 0),
   (0, 0, 0, 0, 2, -2, 0, 0),
   (0, 0, 0, 0, 2, 0, -2, 0),
   (0, 0, 0, 0, 2, 0, 0, -2),
   (0, 0, 0, 0, 2, 0, 0, 2),
   (0, 0, 0, 0, 2, 0, 2, 0),
   (0, 0, 0, 0, 2, 2, 0, 0),
   (0, 0, 0, 2, -2, 0, 0, 0),
   (0, 0, 0, 2, 0, -2, 0, 0),
   (0, 0, 0, 2, 0, 0, -2, 0),
   (0, 0, 0, 2, 0, 0, 0, -2),
   (0, 0, 0, 2, 0, 0, 0, 2),
   (0, 0, 0, 2, 0, 0, 2, 0),
   (0, 0, 0, 2, 0, 2, 0, 0),
   (0, 0, 0, 2, 2, 0, 0, 0),
   (0, 0, 2, -2, 0, 0, 0, 0),
   (0, 0, 2, 0, -2, 0, 0, 0),
   (0, 0, 2, 0, 0, -2, 0, 0),
   (0, 0, 2, 0, 0, 0, -2, 0),
   (0, 0, 2, 0, 0, 0, 0, -2),
   (0, 0, 2, 0, 0, 0, 0, 2),
   (0, 0, 2, 0, 0, 0, 2, 0),
   (0, 0, 2, 0, 0, 2, 0, 0),
   (0, 0, 2, 0, 2, 0, 0, 0),
   (0, 0, 2, 2, 0, 0, 0, 0),
   (0, 2, -2, 0, 0, 0, 0, 0),
   (0, 2, 0, -2, 0, 0, 0, 0),
   (0, 2, 0, 0, -2, 0, 0, 0),
   (0, 2, 0, 0, 0, -2, 0, 0),
   (0, 2, 0, 0, 0, 0, -2, 0),
   (0, 2, 0, 0, 0, 0, 0, -2),
   (0, 2, 0, 0, 0, 0, 0, 2),
   (0, 2, 0, 0, 0, 0, 2, 0),
   (0, 2, 0, 0, 0, 2, 0, 0),
   (0, 2, 0, 0, 2, 0, 0, 0),
   (0, 2, 0, 2, 0, 0, 0, 0),
   (0, 2, 2, 0, 0, 0, 0, 0),
   (2, -2, 0, 0, 0, 0, 0, 0),
   (2, 0, -2, 0, 0, 0, 0, 0),
   (2, 0, 0, -2, 0, 0, 0, 0),
   (2, 0, 0, 0, -2, 0, 0, 0),
   (2, 0, 0, 0, 0, -2, 0, 0),
   (2, 0, 0, 0, 0, 0, -2, 0),
   (2, 0, 0, 0, 0, 0, 0, -2),
   (2, 0, 0, 0, 0, 0, 0, 2),
   (2, 0, 0, 0, 0, 0, 2, 0),
   (2, 0, 0, 0, 0, 2, 0, 0),
   (2, 0, 0, 0, 2, 0, 0, 0),
   (2, 0, 0, 2, 0, 0, 0, 0),
   (2, 0, 2, 0, 0, 0, 0, 0),
   (2, 2, 0, 0, 0, 0, 0, 0)]

/-- The 128 spinor roots (±1,…,±1) with an even number of minus
signs (doubled half-integer vectors). -/
def rdSpinor : List (Z8) :=
  [(-1, -1, -1, -1, -1, -1, -1, -1),
   (-1, -1, -1, -1, -1, -1, 1, 1),
   (-1, -1, -1, -1, -1, 1, -1, 1),
   (-1, -1, -1, -1, -1, 1, 1, -1),
   (-1, -1, -1, -1, 1, -1, -1, 1),
   (-1, -1, -1, -1, 1, -1, 1, -1),
   (-1, -1, -1, -1, 1, 1, -1, -1),
   (-1, -1, -1, -1, 1, 1, 1, 1),
   (-1, -1, -1, 1, -1, -1, -1, 1),
   (-1, -1, -1, 1, -1, -1, 1, -1),
   (-1, -1, -1, 1, -1, 1, -1, -1),
   (-1, -1, -1, 1, -1, 1, 1, 1),
   (-1, -1, -1, 1, 1, -1, -1, -1),
   (-1, -1, -1, 1, 1, -1, 1, 1),
   (-1, -1, -1, 1, 1, 1, -1, 1),
   (-1, -1, -1, 1, 1, 1, 1, -1),
   (-1, -1, 1, -1, -1, -1, -1, 1),
   (-1, -1, 1, -1, -1, -1, 1, -1),
   (-1, -1, 1, -1, -1, 1, -1, -1),
   (-1, -1, 1, -1, -1, 1, 1, 1),
   (-1, -1, 1, -1, 1, -1, -1, -1),
   (-1, -1, 1, -1, 1, -1, 1, 1),
   (-1, -1, 1, -1, 1, 1, -1, 1),
   (-1, -1, 1, -1, 1, 1, 1, -1),
   (-1, -1, 1, 1, -1, -1, -1, -1),
   (-1, -1, 1, 1, -1, -1, 1, 1),
   (-1, -1, 1, 1, -1, 1, -1, 1),
   (-1, -1, 1, 1, -1, 1, 1, -1),
   (-1, -1, 1, 1, 1, -1, -1, 1),
   (-1, -1, 1, 1, 1, -1, 1, -1),
   (-1, -1, 1, 1, 1, 1, -1, -1),
   (-1, -1, 1, 1, 1, 1, 1, 1),
   (-1, 1, -1, -1, -1, -1, -1, 1),
   (-1, 1, -1, -1, -1, -1, 1, -1),
   (-1, 1, -1, -1, -1, 1, -1, -1),
   (-1, 1, -1, -1, -1, 1, 1, 1),
   (-1, 1, -1, -1, 1, -1, -1, -1),
   (-1, 1, -1, -1, 1, -1, 1, 1),
   (-1, 1, -1, -1, 1, 1, -1, 1),
   (-1, 1, -1, -1, 1, 1, 1, -1),
   (-1, 1, -1, 1, -1, -1, -1, -1),
   (-1, 1, -1, 1, -1, -1, 1, 1),
   (-1, 1, -1, 1, -1, 1, -1, 1),
   (-1, 1, -1, 1, -1, 1, 1, -1),
   (-1, 1, -1, 1, 1, -1, -1, 1),
   (-1, 1, -1, 1, 1, -1, 1, -1),
   (-1, 1, -1, 1, 1, 1, -1, -1),
   (-1, 1, -1, 1, 1, 1, 1, 1),
   (-1, 1, 1, -1, -1, -1, -1, -1),
   (-1, 1, 1, -1, -1, -1, 1, 1),
   (-1, 1, 1, -1, -1, 1, -1, 1),
   (-1, 1, 1, -1, -1, 1, 1, -1),
   (-1, 1, 1, -1, 1, -1, -1, 1),
   (-1, 1, 1, -1, 1, -1, 1, -1),
   (-1, 1, 1, -1, 1, 1, -1, -1),
   (-1, 1, 1, -1, 1, 1, 1, 1),
   (-1, 1, 1, 1, -1, -1, -1, 1),
   (-1, 1, 1, 1, -1, -1, 1, -1),
   (-1, 1, 1, 1, -1, 1, -1, -1),
   (-1, 1, 1, 1, -1, 1, 1, 1),
   (-1, 1, 1, 1, 1, -1, -1, -1),
   (-1, 1, 1, 1, 1, -1, 1, 1),
   (-1, 1, 1, 1, 1, 1, -1, 1),
   (-1, 1, 1, 1, 1, 1, 1, -1),
   (1, -1, -1, -1, -1, -1, -1, 1),
   (1, -1, -1, -1, -1, -1, 1, -1),
   (1, -1, -1, -1, -1, 1, -1, -1),
   (1, -1, -1, -1, -1, 1, 1, 1),
   (1, -1, -1, -1, 1, -1, -1, -1),
   (1, -1, -1, -1, 1, -1, 1, 1),
   (1, -1, -1, -1, 1, 1, -1, 1),
   (1, -1, -1, -1, 1, 1, 1, -1),
   (1, -1, -1, 1, -1, -1, -1, -1),
   (1, -1, -1, 1, -1, -1, 1, 1),
   (1, -1, -1, 1, -1, 1, -1, 1),
   (1, -1, -1, 1, -1, 1, 1, -1),
   (1, -1, -1, 1, 1, -1, -1, 1),
   (1, -1, -1, 1, 1, -1, 1, -1),
   (1, -1, -1, 1, 1, 1, -1, -1),
   (1, -1, -1, 1, 1, 1, 1, 1),
   (1, -1, 1, -1, -1, -1, -1, -1),
   (1, -1, 1, -1, -1, -1, 1, 1),
   (1, -1, 1, -1, -1, 1, -1, 1),
   (1, -1, 1, -1, -1, 1, 1, -1),
   (1, -1, 1, -1, 1, -1, -1, 1),
   (1, -1, 1, -1, 1, -1, 1, -1),
   (1, -1, 1, -1, 1, 1, -1, -1),
   (1, -1, 1, -1, 1, 1, 1, 1),
   (1, -1, 1, 1, -1, -1, -1, 1),
   (1, -1, 1, 1, -1, -1, 1, -1),
   (1, -1, 1, 1, -1, 1, -1, -1),
   (1, -1, 1, 1, -1, 1, 1, 1),
   (1, -1, 1, 1, 1, -1, -1, -1),
   (1, -1, 1, 1, 1, -1, 1, 1),
   (1, -1, 1, 1, 1, 1, -1, 1),
   (1, -1, 1, 1, 1, 1, 1, -1),
   (1, 1, -1, -1, -1, -1, -1, -1),
   (1, 1, -1, -1, -1, -1, 1, 1),
   (1, 1, -1, -1, -1, 1, -1, 1),
   (1, 1, -1, -1, -1, 1, 1, -1),
   (1, 1, -1, -1, 1, -1, -1, 1),
   (1, 1, -1, -1, 1, -1, 1, -1),
   (1, 1, -1, -1, 1, 1, -1, -1),
   (1, 1, -1, -1, 1, 1, 1, 1),
   (1, 1, -1, 1, -1, -1, -1, 1),
   (1, 1, -1, 1, -1, -1, 1, -1),
   (1, 1, -1, 1, -1, 1, -1, -1),
   (1, 1, -1, 1, -1, 1, 1, 1),
   (1, 1, -1, 1, 1, -1, -1, -1),
   (1, 1, -1, 1, 1, -1, 1, 1),
   (1, 1, -1, 1, 1, 1, -1, 1),
   (1, 1, -1, 1, 1, 1, 1, -1),
   (1, 1, 1, -1, -1, -1, -1, 1),
   (1, 1, 1, -1, -1, -1, 1, -1),
   (1, 1, 1, -1, -1, 1, -1, -1),
   (1, 1, 1, -1, -1, 1, 1, 1),
   (1, 1, 1, -1, 1, -1, -1, -1),
   (1, 1, 1, -1, 1, -1, 1, 1),
   (1, 1, 1, -1, 1, 1, -1, 1),
   (1, 1, 1, -1, 1, 1, 1, -1),
   (1, 1, 1, 1, -1, -1, -1, -1),
   (1, 1, 1, 1, -1, -1, 1, 1),
   (1, 1, 1, 1, -1, 1, -1, 1),
   (1, 1, 1, 1, -1, 1, 1, -1),
   (1, 1, 1, 1, 1, -1, -1, 1),
   (1, 1, 1, 1, 1, -1, 1, -1),
   (1, 1, 1, 1, 1, 1, -1, -1),
   (1, 1, 1, 1, 1, 1, 1, 1)]

/-- The 240 doubled-coordinate E8 roots. -/
def rd240 : List Z8 := rdD8 ++ rdSpinor

theorem rd240_length : rd240.length = 240 := by rfl

set_option maxHeartbeats 12000000 in
/-- The 240 root tuples are pairwise distinct. -/
theorem rd240_nodup : rd240.Nodup := by decide

/-- Every root has norm 8 (doubled coordinates: 8 = 2·|α|² for the
unit-normalised root system). -/
theorem rd240_norm_eight :
    ∀ p ∈ rd240,
      p.1 ^ 2 + p.2.1 ^ 2 + p.2.2.1 ^ 2 + p.2.2.2.1 ^ 2
        + p.2.2.2.2.1 ^ 2 + p.2.2.2.2.2.1 ^ 2 + p.2.2.2.2.2.2.1 ^ 2
        + p.2.2.2.2.2.2.2 ^ 2 = 8 := by decide

/-- The μ4 rotation J on root tuples:
(x₀,…,x₇) ↦ (−x₁,x₀,−x₃,x₂,−x₅,x₄,−x₇,x₆). -/
def Jt (p : Z8) : Z8 :=
  (-p.2.1, p.1, -p.2.2.2.1, p.2.2.1, -p.2.2.2.2.2.1, p.2.2.2.2.1,
   -p.2.2.2.2.2.2.2, p.2.2.2.2.2.2.1)

set_option maxHeartbeats 12000000 in
/-- The root list is closed under J (μ4 acts on the 240 roots; probe
S0.2 — freeness/60 orbits is numeric context). -/
theorem rd240_mu4_closed : ∀ p ∈ rd240, Jt p ∈ rd240 := by decide

variable {R : Type*} [CommRing R]

/-- ⟨α, x⟩⁴ for one root tuple α at the point (x₀, …, x₇). -/
def quartic (x0 x1 x2 x3 x4 x5 x6 x7 : R) (p : Z8) : R :=
  ((p.1 : R) * x0 + (p.2.1 : R) * x1 + (p.2.2.1 : R) * x2
    + (p.2.2.2.1 : R) * x3 + (p.2.2.2.2.1 : R) * x4
    + (p.2.2.2.2.2.1 : R) * x5 + (p.2.2.2.2.2.2.1 : R) * x6
    + (p.2.2.2.2.2.2.2 : R) * x7) ^ 4

set_option maxHeartbeats 32000000 in
/-- The D8 block: Σ_{α D8-type} ⟨α, x⟩⁴ = 448·Σxᵢ⁴ + 384·Σ_{i<j}xᵢ²xⱼ². -/
theorem quartic_d8_block (x0 x1 x2 x3 x4 x5 x6 x7 : R) :
    (rdD8.map (quartic x0 x1 x2 x3 x4 x5 x6 x7)).sum
      = 448 * (x0 ^ 4 + x1 ^ 4 + x2 ^ 4 + x3 ^ 4 + x4 ^ 4 + x5 ^ 4
          + x6 ^ 4 + x7 ^ 4)
        + 384 * (x0 ^ 2 * x1 ^ 2 + x0 ^ 2 * x2 ^ 2 + x0 ^ 2 * x3 ^ 2
          + x0 ^ 2 * x4 ^ 2 + x0 ^ 2 * x5 ^ 2 + x0 ^ 2 * x6 ^ 2
          + x0 ^ 2 * x7 ^ 2 + x1 ^ 2 * x2 ^ 2 + x1 ^ 2 * x3 ^ 2
          + x1 ^ 2 * x4 ^ 2 + x1 ^ 2 * x5 ^ 2 + x1 ^ 2 * x6 ^ 2
          + x1 ^ 2 * x7 ^ 2 + x2 ^ 2 * x3 ^ 2 + x2 ^ 2 * x4 ^ 2
          + x2 ^ 2 * x5 ^ 2 + x2 ^ 2 * x6 ^ 2 + x2 ^ 2 * x7 ^ 2
          + x3 ^ 2 * x4 ^ 2 + x3 ^ 2 * x5 ^ 2 + x3 ^ 2 * x6 ^ 2
          + x3 ^ 2 * x7 ^ 2 + x4 ^ 2 * x5 ^ 2 + x4 ^ 2 * x6 ^ 2
          + x4 ^ 2 * x7 ^ 2 + x5 ^ 2 * x6 ^ 2 + x5 ^ 2 * x7 ^ 2
          + x6 ^ 2 * x7 ^ 2) := by
  simp only [rdD8, quartic, List.map_cons, List.map_nil, List.sum_cons,
    List.sum_nil]
  push_cast
  ring

set_option maxHeartbeats 32000000 in
/-- The spinor block: Σ_{α spinor} ⟨α, x⟩⁴ = 384·(Σxᵢ²)² − 256·Σxᵢ⁴. -/
theorem quartic_spinor_block (x0 x1 x2 x3 x4 x5 x6 x7 : R) :
    (rdSpinor.map (quartic x0 x1 x2 x3 x4 x5 x6 x7)).sum
      = 384 * (x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2 + x5 ^ 2
          + x6 ^ 2 + x7 ^ 2) ^ 2
        - 256 * (x0 ^ 4 + x1 ^ 4 + x2 ^ 4 + x3 ^ 4 + x4 ^ 4 + x5 ^ 4
          + x6 ^ 4 + x7 ^ 4) := by
  simp only [rdSpinor, quartic, List.map_cons, List.map_nil, List.sum_cons,
    List.sum_nil]
  push_cast
  ring

/-- **f₄ = 576·q²** (probe II2.3): the full symbolic 8-variable
identity Σ_{α ∈ rd240} ⟨α, x⟩⁴ = 576·(Σᵢ xᵢ²)² over any commutative
ring — W(E8) has no basic invariant in degree 4. -/
theorem quartic_powersum (x0 x1 x2 x3 x4 x5 x6 x7 : R) :
    (rd240.map (quartic x0 x1 x2 x3 x4 x5 x6 x7)).sum
      = 576 * (x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2 + x5 ^ 2
          + x6 ^ 2 + x7 ^ 2) ^ 2 := by
  rw [show rd240 = rdD8 ++ rdSpinor from rfl, List.map_append,
    List.sum_append, quartic_d8_block, quartic_spinor_block]
  ring

/-- V^{1,0} is q-isotropic: on the holomorphic point
x = (w₀, −i·w₀, …, w₃, −i·w₃) the quadric Σxᵢ² collapses pairwise via
1 + (−i)² = 0 (probe II2.4). -/
theorem holomorphic_isotropy (w0 w1 w2 w3 : ℂ) :
    w0 ^ 2 + (-Complex.I * w0) ^ 2 + w1 ^ 2 + (-Complex.I * w1) ^ 2
      + w2 ^ 2 + (-Complex.I * w2) ^ 2 + w3 ^ 2 + (-Complex.I * w3) ^ 2
      = 0 := by
  linear_combination (w0 ^ 2 + w1 ^ 2 + w2 ^ 2 + w3 ^ 2) * Complex.I_sq

/-- **F₄|_{V^{1,0}} = 0** (probe II2.5): the restriction of the quartic
root power sum to the holomorphic eigenspace vanishes identically —
the first G31-consistency point (mod 4 alone would allow F₄ ≠ 0; the
invariant theory forbids it). -/
theorem quartic_restriction_vanishes (w0 w1 w2 w3 : ℂ) :
    (rd240.map (quartic w0 (-Complex.I * w0) w1 (-Complex.I * w1)
        w2 (-Complex.I * w2) w3 (-Complex.I * w3))).sum = 0 := by
  rw [quartic_powersum, holomorphic_isotropy]
  norm_num

end TfptCarrier.QuarticHalf
