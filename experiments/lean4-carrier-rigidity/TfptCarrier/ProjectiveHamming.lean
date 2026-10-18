/-
  ProjectiveHamming — the projective Hamming incidence lemma on
  V = L/(1+i)L ≅ F₂⁴.
  ==================================================================

  Machine-checked core of review module 1 (contract candidate
  E8.PROJHAMMING.01).  Numeric counterpart:
  experiments/tfpt-discovery/projective_hamming_incidence_probe.py
  (36/36, verdict PROJ-HAMMING-EXACT, fully deterministic).

  THE IDENTIFICATION (documented, probe-certified).  On the proven
  Gaussian quotient V = L/(1+i)L ≅ F₂⁴ (v689) the hermitian form
  h(x,y) = (⟨x,y⟩ + i⟨x,Jy⟩)/2 of the unimodular hermitian E8
  lattice (Z[i]-Gram determinant = 1, probe P1.3) reduces mod the
  ramified prime (1+i) to an F₂-bilinear form h̄.  The probe
  certifies from the concrete lattice (P1.1–P1.6): h̄ is well
  defined, ALTERNATING (doubly-even: all lattice norms lie in 4Z,
  so h(x,x) = ⟨x,x⟩/2 ∈ 2Z ⊆ (1+i)Z[i]) and NON-DEGENERATE, and in
  the family/anchor basis (F1, F2, F3, ANC) its Gram matrix is
  EXACTLY the matrix `G` below (all ones off the diagonal).  By the
  classification of non-degenerate alternating forms over F₂ every
  such form is equivalent to the standard symplectic form; the
  probe's explicit Darboux transform is certified here as
  `darboux_transform` / `P_invertible` — so working with the
  concrete G is the same as working with the standard form.

  Certified here, kernel `decide` / `norm_num` only (no sorry, no
  native_decide):

  S (the symplectic structure):
    * G is symmetric with zero diagonal; the induced form `symp` is
      bilinear, alternating (symp x x = 0) and non-degenerate;
      Fintype.card Label = 16, 15 nonzero labels.
    * explicit Darboux matrix P with Pᵀ·G·P = standard symplectic
      form and explicit inverse (the classification identification).

  H (the hyperplane counts, stage 2):
    * |H_y| = |{x ∈ P : symp x y = 0}| = 7 for every nonzero y
      (and y ∈ H_y — every point lies on its own polar hyperplane);
    * |H_y ∩ H_z| = 3 for all pairs y ≠ z.

  B (the core identity, stage 3):
    * B ∈ {0,1}¹⁵ˣ¹⁵ over ℤ with B_xy = [symp x y = 0] on the
      explicit point enumeration `pt`: B symmetric, unit diagonal,
      row sums 7, and **B·Bᵀ = 4·I + 3·J EXACTLY**; B·1 = 7·1;
      trace B = 15, trace B² = 105; the annihilation identity
      (B·B − 4·I)·(B − 7·I) = 0 pins the eigenvalues to {7, ±2}
      (with tr B = 15, tr B² = 105 the multiplicities are
      7¹, (+2)⁹, (−2)⁵ — singular values {7, 2¹⁴}; the full
      characteristic polynomial (x−7)(x−2)⁹(x+2)⁵ is the probe's
      job, P3.3).

  K (the channel, stage 4):
    * K = B/7 over ℚ: **K² = (4/49)·I + (45/49)·Π₀** with
      Π₀ = J/15 (scalar algebra + norm_num on the decide-certified
      integer identity); K is doubly stochastic (row sums 1).
      HONESTY: K itself is NOT psd (eigenvalues {1, ±2/7}); the
      depolarizing form is a statement about K².

  N (the 7/8 parity count, stage 5):
    * EVERY nonzero linear functional χ has exactly 7 nonzero
      kernel labels and 8 labels with χ = 1 (generic); every
      functional is symp(·, y) for a unique point y
      (non-degeneracy).  The v722/v738 NS/R character is the
      ANCHOR BIT χ(x) = x₃ = symp(x, y₀) with y₀ = F1+F2+F3 =
      (1,1,1,0) — the checksum label (sum of the family classes =
      the coordinate class; probe P5.3, σ-fixed).  Arithmetic:
      7·16 = 112 NS roots + 8·16 = 128 R roots = 240, plus 8
      Cartan: 248 = 120_NS + 128_R (the SO(16) decomposition).

  F (must-fail witnesses, stage 7):
    * degenerate form: a nonzero y whose "hyperplane" is ALL of P
      (count 15 ≠ 7) — B·Bᵀ = 4I + 3J breaks (probe P7.1);
    * non-alternating dot form: only 7 of 15 points lie on their
      own polar (unit diagonal breaks; the probe shows B·Bᵀ =
      4I + 3J still HOLDS there — the bare identity tests only
      non-degeneracy, while the (1,9,5) eigenvalue multiplicities
      are the symplectic signature, P7.2).

  HONEST SCOPE.  σ-equivariance of h̄, the spectral multiplicities
  (1,9,5), the NS/R purity of the 240 concrete roots, and the
  SEAM48 explanation (35 two-dimensional subspaces, the ū-orbit
  derivation of the v737 incidence distribution 0:96/1:64/2:64/3:16
  and the unique ū-invariant spread with incidence ≡ 1) are
  certified by the probe, not formalized here.  The identification
  of V with F₂⁴ and of h̄ with G rests on the probe's exact lattice
  computation (P1.5: all 256 label pairs).

  Standalone module: no imports from other TfptCarrier files (built
  while round 15 holds the TfptCarrier.lean import list).
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.ProjectiveHamming

/-! ### 0. The label space V ≅ F₂⁴ and the reduced hermitian form -/

/-- The label space V = L/(1+i)L ≅ F₂⁴ in the family/anchor basis
(F1, F2, F3, ANC) of the Gaussian code bridge (v689). -/
abbrev Label := Fin 4 → ZMod 2

/-- The Gram matrix of the reduced hermitian form h̄ in the
family/anchor basis — probe output P1.5 (exact lattice computation,
all 256 label pairs): zero diagonal, all ones off the diagonal. -/
def G : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![0, 1, 1, 1;
     1, 0, 1, 1;
     1, 1, 0, 1;
     1, 1, 1, 0]

/-- The reduced hermitian form h̄ as an F₂-bilinear form. -/
def symp (x y : Label) : ZMod 2 := ∑ i, ∑ j, x i * G i j * y j

/-- |V| = 16 = 2⁴ (the q of the q-normal form). -/
theorem card_label : Fintype.card Label = 16 := by decide

/-- The 15 nonzero labels — the point set P of PG(3,2). -/
def points : Finset Label := Finset.univ.filter (· ≠ 0)

theorem points_card : points.card = 15 := by decide

/-! ### 1. S — the symplectic structure (stage 1) -/

/-- G is symmetric. -/
theorem G_symm : G.transpose = G := by decide

/-- h̄ is ALTERNATING: symp x x = 0 for every label (the doubly-even
reduction h(x,x) = ⟨x,x⟩/2 ∈ 2Z ⊆ (1+i)Z[i], probe P1.2). -/
theorem symp_alternating : ∀ x : Label, symp x x = 0 := by decide

/-- h̄ is symmetric (alternating bilinear over F₂ ⇒ symmetric). -/
theorem symp_symmetric : ∀ x y : Label, symp x y = symp y x := by decide

/-- h̄ is additive in the first slot (bilinearity over F₂; the second
slot follows by symmetry). -/
theorem symp_add_left :
    ∀ x y z : Label, symp (x + y) z = symp x z + symp y z := by decide

/-- h̄ is NON-DEGENERATE: only 0 pairs to zero with everything —
(V, h̄) is a symplectic F₂-space. -/
theorem symp_nondegenerate :
    ∀ x : Label, (∀ y : Label, symp x y = 0) → x = 0 := by decide

/-- The standard symplectic form on F₂⁴ (two hyperbolic planes). -/
def Gstd : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![0, 1, 0, 0;
     1, 0, 0, 0;
     0, 0, 0, 1;
     0, 0, 1, 0]

/-- The explicit Darboux basis change (probe P1.6, columns
e1 = (0,0,0,1), f1 = (0,0,1,0), e2 = (0,1,1,1), f2 = (1,0,1,1)). -/
def P : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![0, 0, 0, 1;
     0, 0, 1, 0;
     0, 1, 1, 1;
     1, 0, 1, 1]

/-- Explicit inverse of P over F₂. -/
def Pinv : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![1, 1, 0, 1;
     1, 1, 1, 0;
     0, 1, 0, 0;
     1, 0, 0, 0]

/-- **The classification identification**: Pᵀ·G·P is EXACTLY the
standard symplectic form — the concrete lattice form h̄ is the (up to
basis change unique) non-degenerate alternating form on F₂⁴. -/
theorem darboux_transform : P.transpose * G * P = Gstd := by decide

/-- P is invertible (both-sided explicit inverse). -/
theorem P_invertible : P * Pinv = 1 ∧ Pinv * P = 1 := by decide

/-! ### 2. H — the hyperplane counts (stage 2) -/

/-- **|H_y| = 7** for every nonzero y: exactly 7 of the 15 points lie
on the polar hyperplane of y. -/
theorem hyperplane_card :
    ∀ y : Label, y ≠ 0 →
      (Finset.univ.filter fun x : Label => x ≠ 0 ∧ symp x y = 0).card
        = 7 := by decide

/-- Every point lies on its OWN polar hyperplane (y ∈ H_y) — the
alternating signature of the symplectic polarity. -/
theorem self_incidence : ∀ y : Label, y ≠ 0 → symp y y = 0 := by decide

/-- **|H_y ∩ H_z| = 3** for all pairs y ≠ z (the intersection of two
distinct hyperplanes is a projective line of PG(3,2)). -/
theorem hyperplane_pair_card :
    ∀ y z : Label, y ≠ 0 → z ≠ 0 → y ≠ z →
      (Finset.univ.filter fun x : Label =>
        x ≠ 0 ∧ symp x y = 0 ∧ symp x z = 0).card = 3 := by decide

/-! ### 3. B — the core identity B·Bᵀ = 4·I + 3·J (stage 3) -/

/-- Explicit enumeration of the 15 points: pt i = the binary digits
of i+1 (an enumeration of V \ {0}). -/
def pt (i : Fin 15) : Label :=
  fun j => ((((i : ℕ) + 1) / 2 ^ (j : ℕ)) % 2 : ℕ)

/-- The enumeration is faithful: pt is injective and never 0. -/
theorem pt_faithful :
    (∀ i : Fin 15, pt i ≠ 0) ∧
    (∀ i j : Fin 15, pt i = pt j → i = j) := by decide

/-- The incidence matrix B over ℤ: B_ij = 1 iff symp (pt i) (pt j)
= 0. -/
def B : Matrix (Fin 15) (Fin 15) ℤ :=
  Matrix.of fun i j => if symp (pt i) (pt j) = 0 then 1 else 0

/-- The all-ones matrix J₁₅. -/
def Jmat : Matrix (Fin 15) (Fin 15) ℤ := Matrix.of fun _ _ => 1

/-- B is symmetric with UNIT diagonal (h̄ symmetric + alternating). -/
theorem B_symm_unit_diag :
    B.transpose = B ∧ ∀ i : Fin 15, B i i = 1 := by decide

/-- Row sums 7 (= |H_y|; column sums follow by symmetry). -/
theorem B_row_sums : ∀ i : Fin 15, (∑ j, B i j) = 7 := by decide

set_option maxHeartbeats 12000000 in
/-- **THE CORE IDENTITY**: B·Bᵀ = 4·I₁₅ + 3·J₁₅ EXACTLY (all 225
entries, kernel-checked over ℤ). -/
theorem B_mul_Bt : B * B.transpose = (4 : ℤ) • 1 + (3 : ℤ) • Jmat := by
  decide

set_option maxHeartbeats 12000000 in
/-- B is symmetric, so the core identity is B² = 4·I + 3·J. -/
theorem B_sq : B * B = (4 : ℤ) • 1 + (3 : ℤ) • Jmat := by decide

/-- The constant vector is the 7-eigenvector: B·1 = 7·1 (the
singular value 7 lives on the constant vector). -/
theorem B_mulVec_ones :
    B.mulVec (fun _ => 1) = fun _ => 7 := by decide

/-- Trace bookkeeping: tr B = 15 and tr B² = 105 = 49 + 4·14 — with
`B_annihilated` this pins the eigenvalue multiplicities to 7¹, (+2)⁹,
(−2)⁵, i.e. SINGULAR VALUES {7 (constant vector), 2 (multiplicity
14)}. -/
theorem B_traces :
    (∑ i, B i i) = 15 ∧ (∑ i, (B * B) i i) = 105 := by decide

/-- Column sums 7 in matrix form: J·B = 7·J. -/
theorem J_mul_B : Jmat * B = (7 : ℤ) • Jmat := by decide

/-- The annihilation identity (B² − 4·I)·(B − 7·I) = 0: every
eigenvalue of B lies in {7, +2, −2} (algebraic consequence of `B_sq`
and `J_mul_B`: B² − 4I = 3J and J·(B − 7I) = 0). -/
theorem B_annihilated :
    (B * B - (4 : ℤ) • 1) * (B - (7 : ℤ) • 1) = 0 := by
  have h3 : B * B - (4 : ℤ) • 1 = (3 : ℤ) • Jmat := by
    rw [B_sq]; abel
  rw [h3, Matrix.smul_mul, Matrix.mul_sub, J_mul_B, Matrix.mul_smul,
      Matrix.mul_one]
  simp

/-- Multiplicity arithmetic (with `B_traces`): 1 + 9 + 5 = 15,
7·1 + 2·9 − 2·5 = 15, 49·1 + 4·9 + 4·5 = 105 — the unique solution is
(1, 9, 5). -/
theorem B_multiplicity_arithmetic :
    1 + 9 + 5 = 15 ∧ 7 * 1 + 2 * 9 - 2 * 5 = 15 ∧
    49 * 1 + 4 * 9 + 4 * 5 = 105 := by norm_num

/-! ### 4. K — the depolarizing channel (stage 4) -/

/-- The cast ring hom ℤ →+* ℚ. -/
def castHom : ℤ →+* ℚ := Int.castRingHom ℚ

/-- B over ℚ (entrywise cast of the kernel-checked integer B). -/
def Bq : Matrix (Fin 15) (Fin 15) ℚ := B.map castHom

/-- The all-ones matrix over ℚ. -/
def Jq : Matrix (Fin 15) (Fin 15) ℚ := Jmat.map castHom

/-- The channel K = B/7 (row-stochastic normalization). -/
def K : Matrix (Fin 15) (Fin 15) ℚ := (7 : ℚ)⁻¹ • Bq

/-- The rank-one averaging projector Π₀ = J/15. -/
def Pi0 : Matrix (Fin 15) (Fin 15) ℚ := (15 : ℚ)⁻¹ • Jq

/-- The integer core identity over ℚ, pushed along the cast ring hom
(no rational kernel computation needed — `B_sq` is kernel-checked
over ℤ). -/
theorem Bq_sq : Bq * Bq = (4 : ℚ) • 1 + (3 : ℚ) • Jq := by
  have h := congrArg (castHom.mapMatrix) B_sq
  simp only [map_mul, map_add, map_zsmul, map_one,
    RingHom.mapMatrix_apply] at h
  show B.map castHom * B.map castHom
      = (4 : ℚ) • 1 + (3 : ℚ) • Jmat.map castHom
  rw [h, ← Int.cast_smul_eq_zsmul ℚ ((4 : ℤ)),
      ← Int.cast_smul_eq_zsmul ℚ ((3 : ℤ))]
  norm_cast

/-- **THE CHANNEL FORMULA**: K² = (4/49)·I + (45/49)·Π₀ — the
depolarizing form, derived from the kernel-checked integer identity
by exact scalar algebra over ℚ.  (HONESTY: K itself has eigenvalues
{1, +2/7, −2/7} and is not psd; the depolarizing statement is about
K².) -/
theorem K_sq :
    K * K = (4 / 49 : ℚ) • (1 : Matrix (Fin 15) (Fin 15) ℚ)
      + (45 / 49 : ℚ) • Pi0 := by
  have h : K * K = ((7 : ℚ)⁻¹ * (7 : ℚ)⁻¹) • (Bq * Bq) := by
    simp [K, smul_smul]
  rw [h, Bq_sq, Pi0]
  match_scalars <;> norm_num

/-- K is doubly stochastic: every row sums to 1 (columns by
symmetry). -/
theorem K_row_sums : ∀ i : Fin 15, (∑ j, K i j) = 1 := by
  intro i
  have hZ := B_row_sums i
  have hB : (∑ j, Bq i j) = 7 := by
    have hc : (∑ j, Bq i j) = ((∑ j, B i j : ℤ) : ℚ) := by
      simp [Bq, Matrix.map_apply, castHom]
    rw [hc, hZ]; norm_num
  calc (∑ j, K i j) = (7 : ℚ)⁻¹ * ∑ j, Bq i j := by
        simp [K, Matrix.smul_apply, smul_eq_mul, Finset.mul_sum]
    _ = 1 := by rw [hB]; norm_num

/-! ### 5. N — the 7/8 parity count and the NS/R character (stage 5) -/

/-- A linear functional on V, given by its coefficient vector. -/
def chi (c x : Label) : ZMod 2 := ∑ j, c j * x j

/-- **The 7/8 count is generic**: EVERY nontrivial linear functional
has exactly 7 nonzero kernel labels and 8 labels with value 1. -/
theorem parity_count_generic :
    ∀ c : Label, c ≠ 0 →
      (Finset.univ.filter fun x : Label => x ≠ 0 ∧ chi c x = 0).card = 7
      ∧ (Finset.univ.filter fun x : Label => chi c x = 1).card = 8 := by
  decide

/-- Non-degeneracy in functional form: every functional is
symp(·, y) for SOME point y — characters ARE points of the
geometry. -/
theorem every_character_is_a_point :
    ∀ c : Label, ∃ y : Label, ∀ x : Label, chi c x = symp x y := by
  decide

/-- The NS/R point: y₀ = F1 + F2 + F3 = (1,1,1,0) — the checksum
label (sum of the family classes = the coordinate class), σ-fixed
(probe P5.3). -/
def y0 : Label := ![1, 1, 1, 0]

/-- The v722/v738 NS/R character: χ_NSR = symp(·, y₀). -/
def chiNSR (x : Label) : ZMod 2 := symp x y0

/-- **χ_NSR is the ANCHOR BIT**: symp(x, y₀) = x₃ in the
family/anchor basis (probe P5.3: coefficient vector (0,0,0,1)). -/
theorem chiNSR_is_anchor_bit : ∀ x : Label, chiNSR x = x 3 := by decide

/-- The NS/R instance of the 7/8 count: 7 kernel labels (NS), 8
labels with χ = 1 (R). -/
theorem chiNSR_count :
    (Finset.univ.filter fun x : Label => x ≠ 0 ∧ chiNSR x = 0).card = 7
    ∧ (Finset.univ.filter fun x : Label => chiNSR x = 1).card = 8 := by
  decide

/-- The SO(16) arithmetic: 7·16 = 112 NS roots, 8·16 = 128 R roots,
112 + 128 = 240; with the 8 Cartan generators (NS):
**248 = 120_NS + 128_R**. -/
theorem so16_decomposition :
    7 * 16 = 112 ∧ 8 * 16 = 128 ∧ 112 + 128 = 240 ∧
    112 + 8 = 120 ∧ 120 + 128 = 248 := by norm_num

/-! ### 6. F — must-fail witnesses (stage 7) -/

/-- A DEGENERATE alternating form (rank 2): one hyperbolic plane,
two kernel directions. -/
def Gdeg : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![0, 1, 0, 0;
     1, 0, 0, 0;
     0, 0, 0, 0;
     0, 0, 0, 0]

def sympDeg (x y : Label) : ZMod 2 := ∑ i, ∑ j, x i * Gdeg i j * y j

/-- **Must-fail (degenerate)**: a kernel point sees ALL 15 points —
|H_y| = 15 ≠ 7, so B·Bᵀ = 4I + 3J breaks (probe P7.1). -/
theorem degenerate_breaks :
    ∃ y : Label, y ≠ 0 ∧
      (Finset.univ.filter fun x : Label =>
        x ≠ 0 ∧ sympDeg x y = 0).card = 15 := by decide

/-- The non-alternating dot form x·y (identity Gram matrix). -/
def sympDot (x y : Label) : ZMod 2 := ∑ j, x j * y j

/-- **Must-fail (non-alternating)**: only 7 of the 15 points lie on
their own polar (q(x) = Σxᵢ ≠ 0 on the 8 odd-weight vectors) — the
unit diagonal of B breaks.  The probe (P7.2) shows the bare identity
B·Bᵀ = 4I + 3J still HOLDS for this non-degenerate form: the
(1, 9, 5) eigenvalue multiplicities, not the identity alone, are the
symplectic signature. -/
theorem non_alternating_breaks_diagonal :
    (Finset.univ.filter fun x : Label =>
      x ≠ 0 ∧ sympDot x x = 0).card = 7 := by decide

end TfptCarrier.ProjectiveHamming
