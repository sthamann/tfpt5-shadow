/-
  FlavorFeedback — the Flavour Feedback Normal Form, kernel-checked.
  ================================================================

  THE OBJECTS (2026-08-08 evening plan, module 1).  The concrete
  flavour matrix over ℤ,

      R = [1 3 0; 1 5 2; 2 5 3],

  its RANK-ONE FEEDBACK DEFORMATION R_s = R + s·(𝟙 column)·(e₁ row)
  (the deformation acts on the first column only — the feedback
  enters through the first flavour slot), and the basis-change
  matrix

      P = [2 0 0; 2 0 2; 2 1 3]      (columns b₀, b₁, b₂).

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`; all statements over ℤ with a SYMBOLIC s — no
  numeric specialization is smuggled in).

    (1) THE ACTION IDENTITIES: on the columns of P,
          R_s·b₀ = (s+4)·b₀ + 4·b₂,
          R_s·b₁ = b₂,
          R_s·b₂ = 3·b₀ − 2·b₁ + 5·b₂
        (`action_b0/b1/b2`) — b₁ and b₂ have zero first
        coordinate, so the deformation parameter s enters the
        action ONLY through b₀: the feedback is confined to one
        basis direction.

    (2) THE CONJUGATION (`conjugation`): P·F_s = R_s·P with the
        companion-feedback form

          F_s = [s+4 0 3; 0 0 −2; 4 1 5].

        Stated as the inverse-free identity over ℤ (the house
        pattern: no ℚ, no P⁻¹); since det P = −4 ≠ 0, over ℚ this
        IS P⁻¹R_sP = F_s.

    (3) THE CHARACTERISTIC POLYNOMIAL (`charpoly_Rs`): in ℤ[X],

          χ_{R_s}(X) = (X − (s+4))·(X² − 5X + 2) − 12X,

        via `Matrix.charpoly` and the 3×3 determinant expansion —
        the feedback shifts ONE factor linearly and couples through
        the fixed −12X term.  The s = 6 instance (`charpoly_L`):
        χ_L = X³ − 15X² + 40X − 20.

    (4) THE LATTICE INDEX (`det_P`, `snf_gcd_entries`,
        `snf_gcd_minors`, `natAbs_det_P`): det P = −4, the gcd of
        the 1×1 minors (entries) is 1 and the gcd of the 2×2
        minors is 2 — with |det P| = 4 these are exactly the
        determinantal-divisor facts d₁ = 1, d₁d₂ = 2, d₁d₂d₃ = 4,
        hence the invariant factors are (1, 2, 2) and the Smith
        normal form is diag(1, 2, 2).

        THE HONEST TYPING (doc-level, deliberately NOT a claimed
        isomorphism): P·ℤ³ is an INDEX-4 sublattice of ℤ³ with
        quotient ℤ/1 ⊕ ℤ/2 ⊕ ℤ/2 ≅ ℤ₂² — a group of CARDINALITY
        4 = |μ₄|, but ℤ₂² ≇ μ₄ ≅ ℤ₄ AS GROUPS.  The coincidence
        with the carrier index 4 is a cardinality statement only;
        the SNF computed here is what makes that distinction
        kernel-checked rather than blurred.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Charpoly.Basic
import Mathlib.Tactic

namespace TfptCarrier
namespace FlavorFeedback

open Matrix Polynomial

/-! ### The objects -/

/-- The flavour matrix R. -/
def R : Matrix (Fin 3) (Fin 3) ℤ := !![1, 3, 0; 1, 5, 2; 2, 5, 3]

/-- The rank-one deformation direction: (𝟙 column)·(e₁ row) — all
mass in the first column. -/
def deform : Matrix (Fin 3) (Fin 3) ℤ :=
  vecMulVec ![1, 1, 1] ![1, 0, 0]

/-- The deformed flavour matrix R_s = R + s·deform. -/
def Rs (s : ℤ) : Matrix (Fin 3) (Fin 3) ℤ := R + s • deform

/-- The basis-change matrix P (columns b₀, b₁, b₂). -/
def P : Matrix (Fin 3) (Fin 3) ℤ := !![2, 0, 0; 2, 0, 2; 2, 1, 3]

/-- First basis column of P. -/
def b0 : Fin 3 → ℤ := ![2, 2, 2]

/-- Second basis column of P. -/
def b1 : Fin 3 → ℤ := ![0, 0, 1]

/-- Third basis column of P. -/
def b2 : Fin 3 → ℤ := ![0, 2, 3]

/-- The companion-feedback normal form F_s. -/
def F (s : ℤ) : Matrix (Fin 3) (Fin 3) ℤ :=
  !![s + 4, 0, 3; 0, 0, -2; 4, 1, 5]

/-- The deformation in explicit entries: s is added to the first
column of every row. -/
theorem Rs_eq (s : ℤ) :
    Rs s = !![1 + s, 3, 0; 1 + s, 5, 2; 2 + s, 5, 3] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Rs, R, deform]

/-! ### (1) The action identities -/

/-- **Action on b₀**: R_s·b₀ = (s+4)·b₀ + 4·b₂ — the ONLY basis
direction through which the feedback parameter s acts. -/
theorem action_b0 (s : ℤ) :
    Rs s *ᵥ b0 = (s + 4) • b0 + 4 • b2 := by
  rw [Rs_eq]
  funext i
  fin_cases i <;>
    simp [b0, b2, Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;>
    ring

/-- **Action on b₁**: R_s·b₁ = b₂ — s-free (b₁ has zero first
coordinate: the deformation cannot see it). -/
theorem action_b1 (s : ℤ) : Rs s *ᵥ b1 = b2 := by
  rw [Rs_eq]
  funext i
  fin_cases i <;>
    simp [b1, b2, Matrix.mulVec, dotProduct, Fin.sum_univ_three]

/-- **Action on b₂**: R_s·b₂ = 3·b₀ − 2·b₁ + 5·b₂ — also s-free. -/
theorem action_b2 (s : ℤ) :
    Rs s *ᵥ b2 = (3 : ℤ) • b0 - (2 : ℤ) • b1 + (5 : ℤ) • b2 := by
  rw [Rs_eq]
  funext i
  fin_cases i <;>
    simp [b0, b1, b2, Matrix.mulVec, dotProduct, Fin.sum_univ_three]

/-! ### (2) The conjugation to the companion-feedback form -/

/-- **THE CONJUGATION**: P·F_s = R_s·P, over ℤ, for every s — the
inverse-free statement of P⁻¹R_sP = F_s (det P = −4 ≠ 0, so P is
invertible over ℚ and the identity divides through).  The three
action identities are exactly the three columns of this one
equation. -/
theorem conjugation (s : ℤ) : P * F s = Rs s * P := by
  rw [Rs_eq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [P, F, Matrix.mul_apply, Fin.sum_univ_three] <;> ring

/-! ### (3) The characteristic polynomial -/

/-- **THE CHARACTERISTIC POLYNOMIAL IDENTITY** in ℤ[X]:

    χ_{R_s}(X) = (X − (s+4))·(X² − 5X + 2) − 12X.

The feedback deforms the linear factor only; the −12X coupling term
is s-INDEPENDENT — the normal-form reading of the conjugation. -/
theorem charpoly_Rs (s : ℤ) :
    (Rs s).charpoly
      = (X - C (s + 4)) * (X ^ 2 - C 5 * X + C 2) - C 12 * X := by
  rw [Rs_eq, Matrix.charpoly, Matrix.det_fin_three]
  simp [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons, map_add, map_ofNat]
  ring

/-- The s = 6 instance: χ_L = X³ − 15X² + 40X − 20. -/
theorem charpoly_L :
    (Rs 6).charpoly = X ^ 3 - 15 * X ^ 2 + 40 * X - 20 := by
  rw [charpoly_Rs, show (6 : ℤ) + 4 = 10 by norm_num]
  simp only [map_ofNat]
  ring

/-! ### (4) det P and the Smith normal form facts -/

/-- det P = −4: the column lattice of P has index 4 in ℤ³. -/
theorem det_P : P.det = -4 := by decide

/-- |det P| = 4 — the third determinantal divisor d₁d₂d₃. -/
theorem natAbs_det_P : P.det.natAbs = 4 := by
  rw [det_P]; rfl

/-- The 2×2 minor of a 3×3 integer matrix at (i, j) (the cofactor
submatrix determinant, unsigned). -/
def minor2 (A : Matrix (Fin 3) (Fin 3) ℤ) (i j : Fin 3) : ℤ :=
  (A.submatrix i.succAbove j.succAbove).det

/-- **SNF fact d₁ = 1**: the gcd of all entries (1×1 minors) of P
is 1 — the first determinantal divisor. -/
theorem snf_gcd_entries :
    (Finset.univ.gcd fun p : Fin 3 × Fin 3 => P p.1 p.2) = 1 := by
  decide

/-- **SNF fact d₁d₂ = 2**: the gcd of all 2×2 minors of P is 2 —
the second determinantal divisor.  With d₁ = 1 and
d₁d₂d₃ = |det P| = 4 this forces the invariant factors (1, 2, 2):
the Smith normal form of P is diag(1, 2, 2), the quotient
ℤ³/Pℤ³ ≅ ℤ₂ ⊕ ℤ₂ — an index-4 sublattice whose quotient has the
CARDINALITY of μ₄ but is NOT μ₄ ≅ ℤ₄ as a group (the honest
typing; see the module doc). -/
theorem snf_gcd_minors :
    (Finset.univ.gcd fun p : Fin 3 × Fin 3 => minor2 P p.1 p.2)
      = 2 := by
  decide

end FlavorFeedback
end TfptCarrier
