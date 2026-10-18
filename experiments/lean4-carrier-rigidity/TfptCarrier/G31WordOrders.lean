/-
  G31WordOrders — the exact orders of the regular G31 words, certified.
  =====================================================================

  The ST31 structure round (v634, E8.ST31.01; degree-24 probe S1.6/S3)
  identifies the characteristic polynomials of the regular order-24 and
  order-20 elements of G31 as explicit Z[i]-quartics:

      χ_w = X⁴ + i·X² − 1     (the regular 24-clock w),
      χ_u = X⁴ − i·X³ − X² + i·X + 1     (the regular 20-element u).

  This module certifies the ORDER statements at the polynomial level:

    * χ_w ∣ X²⁴ − 1 and χ_u ∣ X²⁰ − 1 — via explicit quotient
      witnesses (χ_w·χ̄_w = Φ₂₄ and χ_u·χ̄_u = Φ₂₀, the conjugate
      quartics; `linear_combination` closes the ring identity modulo
      (C i)² = −1);
    * χ_w divides NO X^d − 1 for a proper divisor d ∣ 24
      (d ∈ {1,2,3,4,6,8,12}), and χ_u none for d ∣ 20
      (d ∈ {1,2,4,5,10}) — via the companion matrices W, U: any such
      divisibility forces W^d = 1 (evaluation at W kills χ_w), and
      W^d ≠ 1 is kernel `decide` on 4×4 Gaussian-integer matrices.

  Consequently all four eigenvalues of w (resp. u) are PRIMITIVE 24th
  (resp. 20th) roots of unity — the ζ₂₄- and ζ₂₀-regular spectra of
  the probe.  Free corollaries: W²⁴ = 1, U²⁰ = 1 (no extra decide).

  Machine counterpart: experiments/tfpt-discovery/st31_degree24_probe.py
  (S1.6, S3) in the v634 context; witnesses precomputed symbolically.
-/
import Mathlib.Tactic
import Mathlib.NumberTheory.Zsqrtd.GaussianInt
import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.LinearAlgebra.Matrix.Notation

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.G31WordOrders

open Polynomial

/-- The Gaussian unit `i` in ℤ[i]. -/
def gi : GaussianInt := ⟨0, 1⟩

theorem gi_sq : gi ^ 2 = -1 := by decide

/-- `i² = −1` transported into the polynomial ring ℤ[i][X]. -/
theorem C_gi_sq : (C gi : Polynomial GaussianInt) ^ 2 = -1 := by
  rw [← map_pow, gi_sq, map_neg, map_one]

/-- χ_w = X⁴ + i·X² − 1, the characteristic polynomial of the regular
24-clock w of G31 (a ℤ[i]-quartic factor of Φ₂₄). -/
noncomputable def chiW : Polynomial GaussianInt :=
  X ^ 4 + C gi * X ^ 2 - 1

/-- χ_u = X⁴ − i·X³ − X² + i·X + 1, the characteristic polynomial of
the regular order-20 element u of G31 (a ℤ[i]-quartic factor of Φ₂₀). -/
noncomputable def chiU : Polynomial GaussianInt :=
  X ^ 4 - C gi * X ^ 3 - X ^ 2 + C gi * X + 1

/-! ### The positive halves: χ_w ∣ X²⁴ − 1, χ_u ∣ X²⁰ − 1 -/

/-- χ_w divides X²⁴ − 1, with the explicit quotient
`(X⁸−1)(X⁸+X⁴+1)·χ̄_w` (conjugate quartic: χ_w·χ̄_w = Φ₂₄). -/
theorem chiW_dvd : chiW ∣ (X : Polynomial GaussianInt) ^ 24 - 1 := by
  refine ⟨(X ^ 8 - 1) * (X ^ 8 + X ^ 4 + 1) * (X ^ 4 - C gi * X ^ 2 - 1), ?_⟩
  unfold chiW
  linear_combination (X ^ 4 * (X ^ 8 - 1) * (X ^ 8 + X ^ 4 + 1) :
    Polynomial GaussianInt) * C_gi_sq

/-- χ_u divides X²⁰ − 1, with the explicit quotient
`(X¹⁰−1)(X²+1)·χ̄_u` (conjugate quartic: χ_u·χ̄_u = Φ₂₀). -/
theorem chiU_dvd : chiU ∣ (X : Polynomial GaussianInt) ^ 20 - 1 := by
  refine ⟨(X ^ 10 - 1) * (X ^ 2 + 1) *
    (X ^ 4 + C gi * X ^ 3 - X ^ 2 - C gi * X + 1), ?_⟩
  unfold chiU
  linear_combination ((X ^ 10 - 1) * (X ^ 2 + 1) * (X ^ 3 - X) ^ 2 :
    Polynomial GaussianInt) * C_gi_sq

/-! ### The negative halves via companion matrices -/

/-- Companion matrix of χ_w (so X⁴ = −i·X² + 1 in the last column). -/
def W : Matrix (Fin 4) (Fin 4) GaussianInt :=
  !![0, 0, 0, 1;
     1, 0, 0, 0;
     0, 1, 0, -gi;
     0, 0, 1, 0]

/-- Companion matrix of χ_u (so X⁴ = i·X³ + X² − i·X − 1). -/
def U : Matrix (Fin 4) (Fin 4) GaussianInt :=
  !![0, 0, 0, -1;
     1, 0, 0, -gi;
     0, 1, 0, 1;
     0, 0, 1, gi]

/-- W is a root of its characteristic polynomial: χ_w(W) = 0. -/
theorem aeval_W_chiW : Polynomial.aeval W chiW = 0 := by
  simp only [chiW, map_add, map_sub, map_mul, map_pow, map_one,
    Polynomial.aeval_X, Polynomial.aeval_C, Algebra.algebraMap_eq_smul_one,
    smul_mul_assoc, one_mul]
  decide

/-- U is a root of its characteristic polynomial: χ_u(U) = 0. -/
theorem aeval_U_chiU : Polynomial.aeval U chiU = 0 := by
  simp only [chiU, map_add, map_sub, map_mul, map_pow, map_one,
    Polynomial.aeval_X, Polynomial.aeval_C, Algebra.algebraMap_eq_smul_one,
    smul_mul_assoc, one_mul]
  decide

/-- Any divisibility χ_w ∣ X^d − 1 forces W^d = 1 (evaluate at W). -/
theorem dvd_implies_W_pow {d : ℕ}
    (h : chiW ∣ (X : Polynomial GaussianInt) ^ d - 1) : W ^ d = 1 := by
  obtain ⟨q, hq⟩ := h
  have h2 := congrArg (Polynomial.aeval W) hq
  simp only [map_sub, map_pow, map_one, map_mul, Polynomial.aeval_X,
    aeval_W_chiW, zero_mul] at h2
  exact sub_eq_zero.mp h2

/-- Any divisibility χ_u ∣ X^d − 1 forces U^d = 1 (evaluate at U). -/
theorem dvd_implies_U_pow {d : ℕ}
    (h : chiU ∣ (X : Polynomial GaussianInt) ^ d - 1) : U ^ d = 1 := by
  obtain ⟨q, hq⟩ := h
  have h2 := congrArg (Polynomial.aeval U) hq
  simp only [map_sub, map_pow, map_one, map_mul, Polynomial.aeval_X,
    aeval_U_chiU, zero_mul] at h2
  exact sub_eq_zero.mp h2

/-- Free corollary of the witness identity: W²⁴ = 1. -/
theorem W_pow_24 : W ^ 24 = 1 := dvd_implies_W_pow chiW_dvd

/-- Free corollary of the witness identity: U²⁰ = 1. -/
theorem U_pow_20 : U ^ 20 = 1 := dvd_implies_U_pow chiU_dvd

/-- **The order of w is exactly 24**: χ_w divides no X^d − 1 for a
proper divisor d of 24 — the four eigenvalues of the regular 24-clock
are primitive 24th roots of unity. -/
theorem chiW_not_dvd_proper :
    ∀ d ∈ [1, 2, 3, 4, 6, 8, 12],
      ¬ chiW ∣ (X : Polynomial GaussianInt) ^ d - 1 := by
  intro d hd h
  have hW := dvd_implies_W_pow h
  fin_cases hd <;> exact absurd hW (by decide)

/-- **The order of u is exactly 20**: χ_u divides no X^d − 1 for a
proper divisor d of 20 — the four eigenvalues of the regular
order-20 element are primitive 20th roots of unity. -/
theorem chiU_not_dvd_proper :
    ∀ d ∈ [1, 2, 4, 5, 10],
      ¬ chiU ∣ (X : Polynomial GaussianInt) ^ d - 1 := by
  intro d hd h
  have hU := dvd_implies_U_pow h
  fin_cases hd <;> exact absurd hU (by decide)

end TfptCarrier.G31WordOrders
