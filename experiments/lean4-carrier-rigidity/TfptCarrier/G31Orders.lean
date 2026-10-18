/-
  G31Orders — the G31 / glue order identities (v629 context), certified.
  ======================================================================

  Pure integer arithmetic around the Shephard–Todd complex reflection
  group G31 and the free mu4 clock action on the 240 E8 roots
  (v629, E8.INCIDENCE.01):

    * |G31| = 46080 = 1920 · 24 = |W(D5)| · |W(A3)| — the glue-order
      factorization (D5 ⊕ A3 glue architecture);
    * 1920 = 2⁴ · 5! and 24 = 4! — the two Weyl orders spelled out;
    * the degree product 8 · 12 · 20 · 24 = 46080 = |G31|;
    * the reflection count Σ (dᵢ − 1) = 7 + 11 + 19 + 23 = 60 — which
      is EXACTLY the number of free mu4 clock orbits on the 240 roots
      certified numerically in v629 (60 = D_start);
    * 240 = 4 · 60 — the free mu4 action: |roots| = |mu4| · (orbits).

  All proofs are `norm_num`/`decide` on natural-number literals.
  Machine counterpart: verification/v629_root_incidence.py (R3).
-/
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic

namespace TfptCarrier.G31Orders

/-- `|W(D5)| = 1920 = 2⁴ · 5!`. -/
theorem wd5_order : (1920 : ℕ) = 2 ^ 4 * Nat.factorial 5 := by decide

/-- `|W(A3)| = 24 = 4!`. -/
theorem wa3_order : (24 : ℕ) = Nat.factorial 4 := by decide

/-- **The glue-order factorization**: `|G31| = 46080 = 1920 · 24
= |W(D5)| · |W(A3)|` — the G31 order is the product of the two glue
Weyl orders. -/
theorem g31_order_factorization : (46080 : ℕ) = 1920 * 24 := by norm_num

/-- The G31 degree product: `8 · 12 · 20 · 24 = 46080 = |G31|`. -/
theorem g31_degree_product : (8 : ℕ) * 12 * 20 * 24 = 46080 := by norm_num

/-- The G31 reflection count: `Σ (dᵢ − 1) = 7 + 11 + 19 + 23 = 60` —
the number of reflections equals the number of free mu4 clock orbits
on the 240 E8 roots (v629 R3: 60 = D_start). -/
theorem g31_reflection_count :
    (8 - 1) + (12 - 1) + (20 - 1) + (24 - 1) = (60 : ℕ) := by norm_num

/-- **The free mu4 clock action** (v629 R3): `240 = 4 · 60` — the 240
E8 roots split into exactly 60 free orbits of the order-4 clock. -/
theorem clock_orbit_count : (240 : ℕ) = 4 * 60 := by norm_num

end TfptCarrier.G31Orders
