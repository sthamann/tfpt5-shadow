/-
  GaussianCodeBridge — E8(ℤ[i])/(1+i) ≅ F₂⁴, the finite certificate core.
  ========================================================================

  Machine-checked algebraic core of the theorem candidate
  E8.GAUSSIAN.CODE.01 (the Gaussian code bridge): the μ4 complex
  structure J turns the Construction-A lattice L = A(C*) of the
  equivariant [8,4,4] Hamming placement C* (= `HammingCode.code`, the
  weight-4 supports match the v638 placement verbatim) into a rank-4
  ℤ[i]-lattice; reduction modulo the ramified Gaussian prime (1+i)
  gives L/(1+i)L ≅ F₂⁴, the 240 roots equidistribute 15 × 16 over the
  15 nonzero classes (zero class EMPTY), the classes are μ4-stable,
  and σ acts on the quotient as an order-3 map with a 2-dimensional
  fixed space whose coordinate-class label is the sum of the three
  family labels.  Numeric counterpart:
  experiments/tfpt-discovery/gaussian_code_bridge_probe.py (26/26,
  verdict GAUSSIAN-CODE-BRIDGE-EXACT).

  Certified here, kernel `decide` only (SNF-certificate style as in
  CoverEmbedding.lean: matrix-product identities, no determinant
  expansions; all data explicit integers):

  G1 (the ℤ[i]-module and the Smith certificate):
    * the code layer: `HammingCode.code` is invariant under the
      in-pair swap πJ and the pair 3-cycle πσ (the equivariance that
      singles out C* among the 30 placements);
    * J is an integral orthogonal complex structure (J² = −1,
      (1+J)ᵀ(1+J) = 2·1 — the norm-doubling certificate), σ³ = 1,
      [J, σ] = 0, and both preserve L: B·J = C_J·B, B·σ = C_σ·B;
    * (1+i)L in the L-basis is the integer matrix A: B·(1+J) = A·B;
    * SNF certificate: P·A·Q = D = diag(1,1,1,1,2,2,2,2) with P, Q
      unimodular in BOTH directions (P·P⁻¹ = P⁻¹·P = 1, same for Q),
      plus the converse ingredient D·Q⁻¹ = P·A; the diagonal reads
      off index 16 = 2⁴ = N(1+i)⁴ (det D = 16) and exponent 2 (every
      elementary divisor is 1 or 2, and 2 occurs).

  G2 (the root census as a finite decision):
    * `rootCoords` = the 240 roots of L in the L-basis (explicit,
      pairwise distinct); their ambient vectors c·B all have norm 4
      and reduce mod 2 into the code (Construction-A membership);
    * the class map `labelOf` (last four coordinates of c·Q mod 2 —
      exactly the SNF residue map) sends NO root to the zero class,
      and hits each of the 15 nonzero classes EXACTLY 16 times;
    * μ4-stability: relabeling after the J-action returns the same
      label list (and the transport certificate: (Q⁻¹·C_J·Q) mod 2
      acts as the identity on the label block).

  G3 (σ on the quotient F₂⁴):
    * transport certificate C_σ·Q = Q·R with the mod-2 block law:
      the label block of R is the explicit matrix Mσ (top-right
      block even — well-definedness on labels);
    * Mσ³ = 1, Mσ ≠ 1, exactly 4 fixed labels (fixed space of
      dimension 2, i.e. 3 nonzero fixed labels);
    * the family/anchor basis: labels F1 → F2 → F3 → F1 (a genuine
      3-cycle), an independent σ-fixed anchor, the four spanning
      F₂⁴, and the COORDINATE-CLASS LAW: the label of the coordinate
      root (2,0,…,0) equals F1 + F2 + F3 (σ-fixed).

  HONEST SCOPE.  The quotient L/(1+i)L itself is not built as a
  Mathlib quotient module; the statements are about the explicit SNF
  residue map and the explicit matrices (the standard SNF argument
  that P·A·Q = D with bidirectionally unimodular P, Q identifies the
  quotient as (ℤ/1)⁴ × (ℤ/2)⁴ ≅ F₂⁴ is cited, not formalized).
  Completeness of the root list (that the 240 vectors are ALL norm-4
  vectors of L) is the probe's exhaustive-enumeration job, not
  re-proved here.  The identification of σ with the RM(1,3) family
  permutation up to the 18-element residual gauge (probe I2.6e) is
  numeric context, not formalized.

  Machine counterpart: experiments/tfpt-discovery/
  gaussian_code_bridge_probe.py (26/26).
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic
import TfptCarrier.HammingCode

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.GaussianCodeBridge

open Matrix

/-! ### 0. Parity helpers -/

/-- Parity of an integer, as an element of F₂. -/
def par (n : ℤ) : ZMod 2 := if n % 2 = 0 then 0 else 1

/-- Componentwise mod-2 reduction ℤ⁸ → F₂⁸. -/
def mod2 (v : Fin 8 → ℤ) : Fin 8 → ZMod 2 := fun i => par (v i)

/-! ### 1. The code layer: C* is the equivariant placement -/

/-- The in-pair swap πJ (μ4 pairs (01)(23)(45)(67)). -/
def piJ : Fin 8 → Fin 8 := ![1, 0, 3, 2, 5, 4, 7, 6]

/-- The pair 3-cycle πσ (σ = c⁴: pairs (01) → (23) → (45) → (01),
anchor pair (67) fixed). -/
def piSig : Fin 8 → Fin 8 := ![4, 5, 0, 1, 2, 3, 6, 7]

/-- The [8,4,4] code of `HammingCode` is πJ-invariant: the ℤ[i]-module
structure below exists over THIS placement. -/
theorem code_piJ_invariant :
    ∀ c ∈ HammingCode.code, (fun k => c (piJ k)) ∈ HammingCode.code := by
  decide

/-- The code is also πσ-invariant: the placement is the equivariant
C* (probe I0.1: exactly 2 of 30 placements are both-invariant). -/
theorem code_piSig_invariant :
    ∀ c ∈ HammingCode.code, (fun k => c (piSig k)) ∈ HammingCode.code := by
  decide

/-! ### 2. J and σ on the ambient ℤ⁸ (row-vector action x ↦ x·M) -/

/-- The μ4 complex structure J: (x₀,…,x₇) ↦ (−x₁,x₀,−x₃,x₂,−x₅,x₄,−x₇,x₆). -/
def Jmat : Matrix (Fin 8) (Fin 8) ℤ :=
  !![0, 1, 0, 0, 0, 0, 0, 0;
     -1, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 0, 0, 0;
     0, 0, -1, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 1, 0, 0;
     0, 0, 0, 0, -1, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 0, 0, -1, 0]

/-- The clock σ: (x₀,…,x₇) ↦ (x₄,x₅,x₀,x₁,x₂,x₃,x₆,x₇). -/
def Smat : Matrix (Fin 8) (Fin 8) ℤ :=
  !![0, 0, 1, 0, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 0, 0, 0;
     0, 0, 0, 0, 1, 0, 0, 0;
     0, 0, 0, 0, 0, 1, 0, 0;
     1, 0, 0, 0, 0, 0, 0, 0;
     0, 1, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1, 0;
     0, 0, 0, 0, 0, 0, 0, 1]

/-- J² = −1: a genuine complex structure. -/
theorem J_sq : Jmat * Jmat = -1 := by decide

/-- J is orthogonal and skew: Jᵀ = −J (so x·Jx = 0 for all x). -/
theorem J_skew : Jmat.transpose = -Jmat := by decide

/-- **Norm doubling**: (1+J)ᵀ(1+J) = 2·1, i.e. |(1+i)x|² = 2|x|²
exactly — the proof-grade ingredient of the empty zero class
(min L = 4 ⟹ min (1+i)L = 8 > 4, probe I2.2). -/
theorem one_add_J_gram :
    (1 + Jmat).transpose * (1 + Jmat) = (2 : ℤ) • 1 := by decide

/-- σ³ = 1. -/
theorem sigma_cubed_ambient : Smat * Smat * Smat = 1 := by decide

/-- [J, σ] = 0: σ is ℤ[i]-linear on the lattice. -/
theorem J_sigma_commute : Jmat * Smat = Smat * Jmat := by decide

/-! ### 3. The lattice L = A(C*) and its ℤ-basis B -/

/-- ℤ-basis of L = Construction A(C*): four codeword lifts (the F₂-rref
of the code) followed by four doubled unit vectors (2e₃, 2e₅, 2e₆, 2e₇
— the non-pivot columns). |det B| = 16 = [ℤ⁸ : L]. -/
def Bmat : Matrix (Fin 8) (Fin 8) ℤ :=
  !![1, 1, 1, 1, 1, 1, 1, 1;
     0, 0, 0, 0, 1, 1, 1, 1;
     0, 0, 1, 1, 0, 0, 1, 1;
     0, 1, 0, 1, 0, 1, 0, 1;
     0, 0, 0, 2, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 2, 0, 0;
     0, 0, 0, 0, 0, 0, 2, 0;
     0, 0, 0, 0, 0, 0, 0, 2]

/-- Every basis row reduces mod 2 into the code: B really spans inside
Construction A(C*). -/
theorem basis_rows_in_code :
    ∀ i : Fin 8, mod2 (Bmat i) ∈ HammingCode.code := by decide

/-- J(bᵢ) in the L-basis: J preserves L (the ℤ[i]-module exists). -/
def CJ : Matrix (Fin 8) (Fin 8) ℤ :=
  !![-1, 0, 0, 2, 0, 0, 0, 0;
     0, -1, 0, 0, 0, 1, 0, 1;
     0, 0, -1, 0, 1, 0, 0, 1;
     -1, 0, 0, 1, 0, 0, 0, 0;
     0, 0, -2, 0, 1, 0, 1, 1;
     0, -2, 0, 0, 0, 1, 1, 1;
     0, 0, 0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 0, 0, -1, 0]

/-- σ(bᵢ) in the L-basis: σ preserves L. -/
def CS : Matrix (Fin 8) (Fin 8) ℤ :=
  !![1, 0, 0, 0, 0, 0, 0, 0;
     1, -1, -1, 0, 0, 0, 1, 1;
     0, 1, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 1, 0, 0;
     0, 0, 0, 2, -1, -1, 0, -1;
     0, 0, 0, 0, 0, 0, 1, 0;
     0, 0, 0, 0, 0, 0, 0, 1]

/-- (1+J)(bᵢ) in the L-basis: the sublattice (1+i)L. -/
def Amat : Matrix (Fin 8) (Fin 8) ℤ :=
  !![0, 0, 0, 2, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 1, 0, 1;
     0, 0, 0, 0, 1, 0, 0, 1;
     -1, 0, 0, 2, 0, 0, 0, 0;
     0, 0, -2, 0, 2, 0, 1, 1;
     0, -2, 0, 0, 0, 2, 1, 1;
     0, 0, 0, 0, 0, 0, 1, 1;
     0, 0, 0, 0, 0, 0, -1, 1]

theorem lattice_J : Bmat * Jmat = CJ * Bmat := by decide

theorem lattice_sigma : Bmat * Smat = CS * Bmat := by decide

/-- The sublattice matrix: B·(1+J) = A·B, i.e. row i of A expresses
(1+i)bᵢ in the basis B. -/
theorem lattice_one_add_J : Bmat * (1 + Jmat) = Amat * Bmat := by decide

/-! ### 4. G1 — the Smith certificate P·A·Q = diag(1,1,1,1,2,2,2,2) -/

/-- The elementary divisors of (1+i)L ⊂ L. -/
def snfDiag : Fin 8 → ℤ := ![1, 1, 1, 1, 2, 2, 2, 2]

/-- The Smith diagonal. -/
def Dsnf : Matrix (Fin 8) (Fin 8) ℤ := Matrix.diagonal snfDiag

/-- Unimodular row transform of the Smith certificate. -/
def Pmat : Matrix (Fin 8) (Fin 8) ℤ :=
  !![0, 1, 0, 0, 0, 0, 0, 0;
     0, 0, 1, 0, 0, 0, 0, 0;
     0, 0, 0, -1, 0, 0, 0, 0;
     0, 0, -2, 0, 1, 0, 0, 0;
     1, 0, 0, 0, 0, 0, 0, 0;
     0, -2, 2, 0, -1, 1, 0, 0;
     0, 2, 0, 0, 0, -1, 1, 0;
     0, 0, 0, 0, 0, 0, 1, 1]

/-- Integer inverse of P. -/
def Pinv : Matrix (Fin 8) (Fin 8) ℤ :=
  !![0, 0, 0, 0, 1, 0, 0, 0;
     1, 0, 0, 0, 0, 0, 0, 0;
     0, 1, 0, 0, 0, 0, 0, 0;
     0, 0, -1, 0, 0, 0, 0, 0;
     0, 2, 0, 1, 0, 0, 0, 0;
     2, 0, 0, 1, 0, 1, 0, 0;
     0, 0, 0, 1, 0, 1, 1, 0;
     0, 0, 0, -1, 0, -1, -1, 1]

/-- Unimodular column transform of the Smith certificate. -/
def Qmat : Matrix (Fin 8) (Fin 8) ℤ :=
  !![0, 0, 1, 0, 2, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1, -1;
     0, 0, 0, 0, 0, 1, 1, -1;
     0, 0, 0, 0, 1, 0, 0, 0;
     0, 1, 0, 0, 0, 0, 0, -1;
     1, 0, 0, 0, 0, 0, 0, -1;
     0, 0, 0, 1, 0, 2, 2, -1;
     0, 0, 0, 0, 0, 0, 0, 1]

/-- Integer inverse of Q. -/
def Qinv : Matrix (Fin 8) (Fin 8) ℤ :=
  !![0, 0, 0, 0, 0, 1, 0, 1;
     0, 0, 0, 0, 1, 0, 0, 1;
     1, 0, 0, -2, 0, 0, 0, 0;
     0, 0, -2, 0, 0, 0, 1, -1;
     0, 0, 0, 1, 0, 0, 0, 0;
     0, -1, 1, 0, 0, 0, 0, 0;
     0, 1, 0, 0, 0, 0, 0, 1;
     0, 0, 0, 0, 0, 0, 0, 1]

/-- P is unimodular in both directions. -/
theorem P_unimodular : Pmat * Pinv = 1 ∧ Pinv * Pmat = 1 := by decide

/-- Q is unimodular in both directions. -/
theorem Q_unimodular : Qmat * Qinv = 1 ∧ Qinv * Qmat = 1 := by decide

/-- **The Smith certificate**: P·A·Q = D = diag(1,1,1,1,2,2,2,2).
With `P_unimodular` and `Q_unimodular` this identifies the elementary
divisors of (1+i)L ⊂ L as EXACTLY (1,1,1,1,2,2,2,2), so
L/(1+i)L ≅ (ℤ/2)⁴ = F₂⁴ (standard SNF argument, cited). -/
theorem smith_certificate : Pmat * Amat * Qmat = Dsnf := by decide

/-- The converse ingredient D·Q⁻¹ = P·A: any coordinate vector whose
Q-image lies in the row space of D lies in the row space of A. -/
theorem smith_converse_ingredient : Dsnf * Qinv = Pmat * Amat := by decide

/-- Index [L : (1+i)L] = det D = 16 = 2⁴ = N(1+i)⁴. -/
theorem index_sixteen : Dsnf.det = 16 := by
  simp only [Dsnf, Matrix.det_diagonal]
  decide

theorem index_is_norm_pow_four : (16 : ℤ) = 2 ^ 4 := by norm_num

/-- **Exponent 2**: every elementary divisor is 1 or 2, and 2 occurs —
the quotient is elementary abelian of exponent 2 (rank 4). -/
theorem snf_exponent_two :
    (∀ i : Fin 8, snfDiag i = 1 ∨ snfDiag i = 2) ∧ snfDiag 7 = 2 := by
  decide

/-! ### 5. The class map (the SNF residue map) -/

/-- Row vector times matrix (exact). -/
def rowMul (c : Fin 8 → ℤ) (M : Matrix (Fin 8) (Fin 8) ℤ) : Fin 8 → ℤ :=
  fun j => ∑ i, c i * M i j

/-- The class map on L-coordinates: the last four coordinates of c·Q,
mod 2 — the SNF residue of c modulo the row space of A. -/
def labelOf (c : Fin 8 → ℤ) : Fin 4 → ZMod 2 :=
  fun j => par (rowMul c Qmat (Fin.natAdd 4 j))

/-- The label kills (1+i)L: every row of A·Q has even entries in the
label block (columns 4–7) — the class map is well defined on
L/(1+i)L. -/
theorem label_kills_one_add_J :
    ∀ i : Fin 8, ∀ j : Fin 4,
      par ((Amat * Qmat) i (Fin.natAdd 4 j)) = 0 := by decide

/-! ### 6. G2 — the census of the 240 roots as a finite decision -/

/-- The 240 roots of L in the L-basis (coordinates w.r.t. B; explicit
data extracted with exact integer arithmetic, probe I1/I2). -/
def rootCoords : List (Fin 8 → ℤ) :=
  [![-2, 2, 2, 2, -1, -1, -1, -2],
   ![-1, 1, 0, 0, 0, 0, 0, 0],
   ![-1, 1, 0, 0, 1, 0, 0, 0],
   ![-1, 0, 1, 0, 0, 0, 0, 0],
   ![-1, 0, 1, 0, 0, 1, 0, 0],
   ![-1, 1, 1, 0, 0, 0, -1, -1],
   ![-1, 1, 1, 0, 0, 0, -1, 0],
   ![-1, 1, 1, 0, 0, 0, 0, -1],
   ![-1, 1, 1, 0, 0, 0, 0, 0],
   ![-1, 2, 1, 0, 0, -1, -1, -1],
   ![-1, 2, 1, 0, 0, 0, -1, -1],
   ![-1, 1, 2, 0, -1, 0, -1, -1],
   ![-1, 1, 2, 0, 0, 0, -1, -1],
   ![-1, 0, 0, 1, 0, 0, 0, 0],
   ![-1, 0, 0, 1, 0, 0, 1, 0],
   ![-1, 1, 0, 1, 0, -1, 0, -1],
   ![-1, 1, 0, 1, 0, -1, 0, 0],
   ![-1, 1, 0, 1, 0, 0, 0, -1],
   ![-1, 1, 0, 1, 0, 0, 0, 0],
   ![-1, 2, 0, 1, 0, -1, -1, -1],
   ![-1, 2, 0, 1, 0, -1, 0, -1],
   ![-1, 0, 1, 1, -1, 0, 0, -1],
   ![-1, 0, 1, 1, -1, 0, 0, 0],
   ![-1, 1, 1, 1, -1, -1, -1, -1],
   ![-1, 1, 1, 1, -1, -1, 0, -1],
   ![-1, 1, 1, 1, -1, 0, -1, -1],
   ![-1, 1, 1, 1, -1, 0, 0, -1],
   ![-1, 2, 1, 1, -1, -1, -1, -2],
   ![-1, 2, 1, 1, -1, -1, -1, -1],
   ![-1, 0, 1, 1, 0, 0, 0, -1],
   ![-1, 0, 1, 1, 0, 0, 0, 0],
   ![-1, 1, 1, 1, 0, -1, -1, -1],
   ![-1, 1, 1, 1, 0, -1, 0, -1],
   ![-1, 1, 1, 1, 0, 0, -1, -1],
   ![-1, 1, 1, 1, 0, 0, 0, -1],
   ![-1, 2, 1, 1, 0, -1, -1, -2],
   ![-1, 2, 1, 1, 0, -1, -1, -1],
   ![-1, 0, 2, 1, -1, 0, -1, -1],
   ![-1, 0, 2, 1, -1, 0, 0, -1],
   ![-1, 1, 2, 1, -1, -1, -1, -2],
   ![-1, 1, 2, 1, -1, -1, -1, -1],
   ![-1, 1, 2, 1, -1, 0, -1, -2],
   ![-1, 1, 2, 1, -1, 0, -1, -1],
   ![-1, 2, 2, 1, -1, -1, -2, -2],
   ![-1, 2, 2, 1, -1, -1, -1, -2],
   ![-1, 1, 0, 2, -1, -1, 0, -1],
   ![-1, 1, 0, 2, 0, -1, 0, -1],
   ![-1, 0, 1, 2, -1, -1, 0, -1],
   ![-1, 0, 1, 2, -1, 0, 0, -1],
   ![-1, 1, 1, 2, -1, -1, -1, -2],
   ![-1, 1, 1, 2, -1, -1, -1, -1],
   ![-1, 1, 1, 2, -1, -1, 0, -2],
   ![-1, 1, 1, 2, -1, -1, 0, -1],
   ![-1, 2, 1, 2, -1, -2, -1, -2],
   ![-1, 2, 1, 2, -1, -1, -1, -2],
   ![-1, 1, 2, 2, -2, -1, -1, -2],
   ![-1, 1, 2, 2, -1, -1, -1, -2],
   ![0, 0, 0, -2, 1, 1, 0, 1],
   ![0, -1, -1, -1, 1, 1, 1, 1],
   ![0, -1, -1, -1, 1, 1, 1, 2],
   ![0, 0, -1, -1, 1, 0, 0, 1],
   ![0, 0, -1, -1, 1, 0, 1, 1],
   ![0, 0, -1, -1, 1, 1, 0, 1],
   ![0, 0, -1, -1, 1, 1, 1, 1],
   ![0, 1, -1, -1, 1, 0, 0, 0],
   ![0, 1, -1, -1, 1, 0, 0, 1],
   ![0, -1, 0, -1, 0, 1, 0, 1],
   ![0, -1, 0, -1, 0, 1, 1, 1],
   ![0, 0, 0, -1, 0, 0, 0, 0],
   ![0, 0, 0, -1, 0, 0, 0, 1],
   ![0, 0, 0, -1, 0, 1, 0, 0],
   ![0, 0, 0, -1, 0, 1, 0, 1],
   ![0, 1, 0, -1, 0, 0, -1, 0],
   ![0, 1, 0, -1, 0, 0, 0, 0],
   ![0, -1, 0, -1, 1, 1, 0, 1],
   ![0, -1, 0, -1, 1, 1, 1, 1],
   ![0, 0, 0, -1, 1, 0, 0, 0],
   ![0, 0, 0, -1, 1, 0, 0, 1],
   ![0, 0, 0, -1, 1, 1, 0, 0],
   ![0, 0, 0, -1, 1, 1, 0, 1],
   ![0, 1, 0, -1, 1, 0, -1, 0],
   ![0, 1, 0, -1, 1, 0, 0, 0],
   ![0, -1, 1, -1, 0, 1, 0, 0],
   ![0, -1, 1, -1, 0, 1, 0, 1],
   ![0, 0, 1, -1, 0, 0, -1, 0],
   ![0, 0, 1, -1, 0, 0, 0, 0],
   ![0, 0, 1, -1, 0, 1, -1, 0],
   ![0, 0, 1, -1, 0, 1, 0, 0],
   ![0, 1, 1, -1, 0, 0, -1, -1],
   ![0, 1, 1, -1, 0, 0, -1, 0],
   ![0, 0, -2, 0, 1, 0, 1, 1],
   ![0, -1, -1, 0, 0, 0, 1, 1],
   ![0, -1, -1, 0, 0, 1, 1, 1],
   ![0, 0, -1, 0, 0, 0, 0, 0],
   ![0, 0, -1, 0, 0, 0, 0, 1],
   ![0, 0, -1, 0, 0, 0, 1, 0],
   ![0, 0, -1, 0, 0, 0, 1, 1],
   ![0, 1, -1, 0, 0, -1, 0, 0],
   ![0, 1, -1, 0, 0, 0, 0, 0],
   ![0, -1, -1, 0, 1, 0, 1, 1],
   ![0, -1, -1, 0, 1, 1, 1, 1],
   ![0, 0, -1, 0, 1, 0, 0, 0],
   ![0, 0, -1, 0, 1, 0, 0, 1],
   ![0, 0, -1, 0, 1, 0, 1, 0],
   ![0, 0, -1, 0, 1, 0, 1, 1],
   ![0, 1, -1, 0, 1, -1, 0, 0],
   ![0, 1, -1, 0, 1, 0, 0, 0],
   ![0, 0, 0, 0, -1, 0, 0, 0],
   ![0, -2, 0, 0, 0, 1, 1, 1],
   ![0, -1, 0, 0, 0, 0, 0, 0],
   ![0, -1, 0, 0, 0, 0, 0, 1],
   ![0, -1, 0, 0, 0, 0, 1, 0],
   ![0, -1, 0, 0, 0, 0, 1, 1],
   ![0, -1, 0, 0, 0, 1, 0, 0],
   ![0, -1, 0, 0, 0, 1, 0, 1],
   ![0, -1, 0, 0, 0, 1, 1, 0],
   ![0, -1, 0, 0, 0, 1, 1, 1],
   ![0, 0, 0, 0, 0, -1, 0, 0],
   ![0, 0, 0, 0, 0, 0, -1, 0],
   ![0, 0, 0, 0, 0, 0, 0, -1],
   ![0, 0, 0, 0, 0, 0, 0, 1],
   ![0, 0, 0, 0, 0, 0, 1, 0],
   ![0, 0, 0, 0, 0, 1, 0, 0],
   ![0, 1, 0, 0, 0, -1, -1, -1],
   ![0, 1, 0, 0, 0, -1, -1, 0],
   ![0, 1, 0, 0, 0, -1, 0, -1],
   ![0, 1, 0, 0, 0, -1, 0, 0],
   ![0, 1, 0, 0, 0, 0, -1, -1],
   ![0, 1, 0, 0, 0, 0, -1, 0],
   ![0, 1, 0, 0, 0, 0, 0, -1],
   ![0, 1, 0, 0, 0, 0, 0, 0],
   ![0, 2, 0, 0, 0, -1, -1, -1],
   ![0, 0, 0, 0, 1, 0, 0, 0],
   ![0, -1, 1, 0, -1, 0, 0, 0],
   ![0, -1, 1, 0, -1, 1, 0, 0],
   ![0, 0, 1, 0, -1, 0, -1, -1],
   ![0, 0, 1, 0, -1, 0, -1, 0],
   ![0, 0, 1, 0, -1, 0, 0, -1],
   ![0, 0, 1, 0, -1, 0, 0, 0],
   ![0, 1, 1, 0, -1, -1, -1, -1],
   ![0, 1, 1, 0, -1, 0, -1, -1],
   ![0, -1, 1, 0, 0, 0, 0, 0],
   ![0, -1, 1, 0, 0, 1, 0, 0],
   ![0, 0, 1, 0, 0, 0, -1, -1],
   ![0, 0, 1, 0, 0, 0, -1, 0],
   ![0, 0, 1, 0, 0, 0, 0, -1],
   ![0, 0, 1, 0, 0, 0, 0, 0],
   ![0, 1, 1, 0, 0, -1, -1, -1],
   ![0, 1, 1, 0, 0, 0, -1, -1],
   ![0, 0, 2, 0, -1, 0, -1, -1],
   ![0, -1, -1, 1, 0, 0, 1, 0],
   ![0, -1, -1, 1, 0, 0, 1, 1],
   ![0, 0, -1, 1, 0, -1, 0, 0],
   ![0, 0, -1, 1, 0, -1, 1, 0],
   ![0, 0, -1, 1, 0, 0, 0, 0],
   ![0, 0, -1, 1, 0, 0, 1, 0],
   ![0, 1, -1, 1, 0, -1, 0, -1],
   ![0, 1, -1, 1, 0, -1, 0, 0],
   ![0, -1, 0, 1, -1, 0, 0, 0],
   ![0, -1, 0, 1, -1, 0, 1, 0],
   ![0, 0, 0, 1, -1, -1, 0, -1],
   ![0, 0, 0, 1, -1, -1, 0, 0],
   ![0, 0, 0, 1, -1, 0, 0, -1],
   ![0, 0, 0, 1, -1, 0, 0, 0],
   ![0, 1, 0, 1, -1, -1, -1, -1],
   ![0, 1, 0, 1, -1, -1, 0, -1],
   ![0, -1, 0, 1, 0, 0, 0, 0],
   ![0, -1, 0, 1, 0, 0, 1, 0],
   ![0, 0, 0, 1, 0, -1, 0, -1],
   ![0, 0, 0, 1, 0, -1, 0, 0],
   ![0, 0, 0, 1, 0, 0, 0, -1],
   ![0, 0, 0, 1, 0, 0, 0, 0],
   ![0, 1, 0, 1, 0, -1, -1, -1],
   ![0, 1, 0, 1, 0, -1, 0, -1],
   ![0, -1, 1, 1, -1, 0, 0, -1],
   ![0, -1, 1, 1, -1, 0, 0, 0],
   ![0, 0, 1, 1, -1, -1, -1, -1],
   ![0, 0, 1, 1, -1, -1, 0, -1],
   ![0, 0, 1, 1, -1, 0, -1, -1],
   ![0, 0, 1, 1, -1, 0, 0, -1],
   ![0, 1, 1, 1, -1, -1, -1, -2],
   ![0, 1, 1, 1, -1, -1, -1, -1],
   ![0, 0, 0, 2, -1, -1, 0, -1],
   ![1, -1, -2, -2, 1, 1, 1, 2],
   ![1, -1, -2, -2, 2, 1, 1, 2],
   ![1, -2, -1, -2, 1, 1, 1, 2],
   ![1, -2, -1, -2, 1, 2, 1, 2],
   ![1, -1, -1, -2, 1, 1, 0, 1],
   ![1, -1, -1, -2, 1, 1, 0, 2],
   ![1, -1, -1, -2, 1, 1, 1, 1],
   ![1, -1, -1, -2, 1, 1, 1, 2],
   ![1, 0, -1, -2, 1, 0, 0, 1],
   ![1, 0, -1, -2, 1, 1, 0, 1],
   ![1, -1, 0, -2, 0, 1, 0, 1],
   ![1, -1, 0, -2, 1, 1, 0, 1],
   ![1, -2, -2, -1, 1, 1, 1, 2],
   ![1, -2, -2, -1, 1, 1, 2, 2],
   ![1, -1, -2, -1, 1, 0, 1, 1],
   ![1, -1, -2, -1, 1, 0, 1, 2],
   ![1, -1, -2, -1, 1, 1, 1, 1],
   ![1, -1, -2, -1, 1, 1, 1, 2],
   ![1, 0, -2, -1, 1, 0, 0, 1],
   ![1, 0, -2, -1, 1, 0, 1, 1],
   ![1, -2, -1, -1, 0, 1, 1, 1],
   ![1, -2, -1, -1, 0, 1, 1, 2],
   ![1, -1, -1, -1, 0, 0, 0, 1],
   ![1, -1, -1, -1, 0, 0, 1, 1],
   ![1, -1, -1, -1, 0, 1, 0, 1],
   ![1, -1, -1, -1, 0, 1, 1, 1],
   ![1, 0, -1, -1, 0, 0, 0, 0],
   ![1, 0, -1, -1, 0, 0, 0, 1],
   ![1, -2, -1, -1, 1, 1, 1, 1],
   ![1, -2, -1, -1, 1, 1, 1, 2],
   ![1, -1, -1, -1, 1, 0, 0, 1],
   ![1, -1, -1, -1, 1, 0, 1, 1],
   ![1, -1, -1, -1, 1, 1, 0, 1],
   ![1, -1, -1, -1, 1, 1, 1, 1],
   ![1, 0, -1, -1, 1, 0, 0, 0],
   ![1, 0, -1, -1, 1, 0, 0, 1],
   ![1, -2, 0, -1, 0, 1, 0, 1],
   ![1, -2, 0, -1, 0, 1, 1, 1],
   ![1, -1, 0, -1, 0, 0, 0, 0],
   ![1, -1, 0, -1, 0, 0, 0, 1],
   ![1, -1, 0, -1, 0, 1, 0, 0],
   ![1, -1, 0, -1, 0, 1, 0, 1],
   ![1, 0, 0, -1, 0, 0, -1, 0],
   ![1, 0, 0, -1, 0, 0, 0, 0],
   ![1, -1, -2, 0, 0, 0, 1, 1],
   ![1, -1, -2, 0, 1, 0, 1, 1],
   ![1, -2, -1, 0, 0, 0, 1, 1],
   ![1, -2, -1, 0, 0, 1, 1, 1],
   ![1, -1, -1, 0, 0, 0, 0, 0],
   ![1, -1, -1, 0, 0, 0, 0, 1],
   ![1, -1, -1, 0, 0, 0, 1, 0],
   ![1, -1, -1, 0, 0, 0, 1, 1],
   ![1, 0, -1, 0, 0, -1, 0, 0],
   ![1, 0, -1, 0, 0, 0, 0, 0],
   ![1, -1, 0, 0, -1, 0, 0, 0],
   ![1, -1, 0, 0, 0, 0, 0, 0],
   ![2, -2, -2, -2, 1, 1, 1, 2]]

/-- The 240 class labels (values of `labelOf` on `rootCoords`). -/
def labelData : List (Fin 4 → ZMod 2) :=
  [![0, 0, 0, 1],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 0, 1],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![0, 0, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 0, 0, 1],
   ![0, 0, 0, 1],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 0, 1],
   ![0, 0, 0, 1],
   ![0, 0, 0, 1],
   ![0, 0, 0, 1],
   ![0, 0, 0, 1],
   ![0, 0, 0, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 0, 1],
   ![0, 0, 0, 1],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 0, 0, 1],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![0, 0, 0, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 1, 1, 0],
   ![1, 1, 0, 0],
   ![1, 1, 0, 1],
   ![1, 1, 0, 1],
   ![1, 1, 0, 0],
   ![1, 1, 1, 0],
   ![1, 1, 1, 1],
   ![1, 0, 0, 0],
   ![1, 0, 0, 1],
   ![1, 0, 1, 1],
   ![1, 0, 1, 0],
   ![1, 0, 1, 0],
   ![1, 0, 1, 1],
   ![1, 0, 0, 1],
   ![1, 0, 0, 0],
   ![0, 0, 1, 1],
   ![0, 0, 1, 0],
   ![0, 1, 1, 1],
   ![0, 1, 1, 0],
   ![0, 1, 0, 0],
   ![0, 1, 0, 1],
   ![0, 1, 0, 1],
   ![0, 1, 0, 0],
   ![0, 1, 1, 0],
   ![0, 1, 1, 1],
   ![0, 0, 1, 0],
   ![0, 0, 1, 1],
   ![0, 0, 0, 1]]

theorem rootCoords_length : rootCoords.length = 240 := by rfl

theorem labelData_length : labelData.length = 240 := by rfl

set_option maxHeartbeats 12000000 in
/-- The 240 coordinate vectors are pairwise distinct. -/
theorem rootCoords_nodup : rootCoords.Nodup := by decide

set_option maxHeartbeats 12000000 in
/-- Every listed root has ambient norm 4 (c·B is an E8 root vector). -/
theorem roots_norm_four :
    ∀ c ∈ rootCoords, (∑ j, rowMul c Bmat j ^ 2) = 4 := by decide

set_option maxHeartbeats 12000000 in
/-- Every listed root reduces mod 2 into the code: c·B lies in
Construction A(C*). -/
theorem roots_in_code :
    ∀ c ∈ rootCoords, mod2 (rowMul c Bmat) ∈ HammingCode.code := by decide

set_option maxHeartbeats 12000000 in
/-- The label list is exactly `labelOf` applied to the root list. -/
theorem labels_eq : rootCoords.map labelOf = labelData := by decide

/-- **The zero class is EMPTY on roots** (probe I2.2). -/
theorem census_zero_class_empty : ∀ l ∈ labelData, l ≠ 0 := by decide

set_option maxHeartbeats 12000000 in
/-- **Equidistribution** (probe I2.3): each of the 15 nonzero classes
contains EXACTLY 16 of the 240 roots (240 = 15 × 16). -/
theorem census_equidistribution :
    ∀ s : Fin 4 → ZMod 2, s ≠ 0 → labelData.count s = 16 := by decide

/-! ### 7. μ4-stability and the σ-transport (G2/G3 bridge) -/

/-- σ-transport into SNF coordinates: C_σ·Q = Q·R. -/
def Rsig : Matrix (Fin 8) (Fin 8) ℤ :=
  !![-1, -1, 0, 0, 2, 0, 0, 2;
     1, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 1, 0, 0, 0, 0, 0;
     0, 0, 0, 1, 0, 2, 0, 0;
     0, 0, 0, 0, 1, 0, 0, 0;
     0, 0, -1, -1, -2, -1, 1, -3;
     0, 0, 1, 1, 2, 1, 0, 3;
     0, 0, 0, 0, 0, 0, 0, 1]

/-- μ4-transport into SNF coordinates: C_J·Q = Q·R_J. -/
def RJ : Matrix (Fin 8) (Fin 8) ℤ :=
  !![1, 0, 0, 0, 0, 0, -2, 2;
     0, 1, 0, 0, 0, -2, -2, 2;
     0, 0, 1, 0, 2, 0, 0, 0;
     0, -2, 0, 1, 0, 4, 4, -2;
     0, 0, -1, 0, -1, 0, 0, 0;
     -1, 1, 0, 0, 0, -1, 0, 0;
     1, 0, 0, -1, 0, -2, -3, 2;
     0, 0, 0, -1, 0, -2, -2, 1]

/-- σ on the label block F₂⁴ (row-vector action l ↦ l·Mσ). -/
def Msig : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![1, 0, 0, 0;
     0, 1, 1, 1;
     0, 1, 0, 1;
     0, 0, 0, 1]

theorem sigma_transport : CS * Qmat = Qmat * Rsig := by decide

theorem mu4_transport : CJ * Qmat = Qmat * RJ := by decide

/-- Well-definedness of the σ-action on labels: the top-right block of
R is even (labels of σx depend only on labels of x), and the label
block of R mod 2 is exactly Mσ. -/
theorem sigma_label_block :
    (∀ i : Fin 4, ∀ j : Fin 4,
      par (Rsig (Fin.castAdd 4 i) (Fin.natAdd 4 j)) = 0) ∧
    (∀ i : Fin 4, ∀ j : Fin 4,
      Msig i j = par (Rsig (Fin.natAdd 4 i) (Fin.natAdd 4 j))) := by decide

/-- **μ4-stability certificate** (probe I2.4): in the label block, the
μ4 transport R_J acts as the IDENTITY mod 2 — root ~ i·root, every
class is μ4-stable ((i−1) = i(1+i)). -/
theorem mu4_acts_trivially_on_labels :
    ∀ i : Fin 8, ∀ j : Fin 4,
      par (RJ i (Fin.natAdd 4 j)) = if i = Fin.natAdd 4 j then 1 else 0 := by
  decide

set_option maxHeartbeats 16000000 in
/-- Direct μ4-stability of the census: relabeling all 240 roots after
the J-action reproduces the label list verbatim. -/
theorem census_mu4_stable :
    rootCoords.map (fun c => labelOf (rowMul c CJ)) = labelData := by decide

/-- Row vector times matrix over F₂. -/
def rowMul4 (l : Fin 4 → ZMod 2) (M : Matrix (Fin 4) (Fin 4) (ZMod 2)) :
    Fin 4 → ZMod 2 :=
  fun j => ∑ i, l i * M i j

set_option maxHeartbeats 16000000 in
/-- Direct σ-equivariance of the census: relabeling after the σ-action
equals the Mσ-image of the label list. -/
theorem census_sigma_equivariant :
    rootCoords.map (fun c => labelOf (rowMul c CS))
      = labelData.map (fun l => rowMul4 l Msig) := by decide

/-! ### 8. G3 — σ on F₂⁴: order 3, fixed space dimension 2, families -/

/-- σ³ = 1 on the quotient. -/
theorem sigma_cubed : Msig * Msig * Msig = 1 := by decide

/-- σ ≠ 1 on the quotient. -/
theorem sigma_nontrivial : Msig ≠ 1 := by decide

/-- **Fixed space dimension 2**: exactly 4 = 2² of the 16 labels are
σ-fixed. -/
theorem sigma_fixed_space :
    (Finset.univ.filter fun l : Fin 4 → ZMod 2 =>
      rowMul4 l Msig = l).card = 4 := by decide

/-- Exactly 3 NONZERO labels are σ-fixed (probe I2.6b). -/
theorem sigma_fixed_nontrivial :
    (Finset.univ.filter fun l : Fin 4 → ZMod 2 =>
      l ≠ 0 ∧ rowMul4 l Msig = l).card = 3 := by decide

/-- The first family label. -/
def F1 : Fin 4 → ZMod 2 := ![0, 0, 1, 0]

/-- The second family label (= F1·Mσ). -/
def F2 : Fin 4 → ZMod 2 := ![0, 1, 0, 1]

/-- The third family label (= F2·Mσ). -/
def F3 : Fin 4 → ZMod 2 := ![0, 1, 1, 0]

/-- The σ-fixed anchor label. -/
def anchor : Fin 4 → ZMod 2 := ![1, 0, 0, 0]

/-- σ cycles the three family labels: F1 → F2 → F3 → F1. -/
theorem family_three_cycle :
    rowMul4 F1 Msig = F2 ∧ rowMul4 F2 Msig = F3 ∧ rowMul4 F3 Msig = F1 := by
  decide

/-- The anchor is σ-fixed and nonzero. -/
theorem anchor_fixed : rowMul4 anchor Msig = anchor ∧ anchor ≠ 0 := by decide

/-- (F1, F2, F3, anchor) is an F₂-basis of the quotient: every label is
a (unique, by cardinality) F₂-combination. -/
theorem family_anchor_spans :
    ∀ v : Fin 4 → ZMod 2,
      ∃ a b c d : ZMod 2, v = a • F1 + b • F2 + c • F3 + d • anchor := by
  decide

/-! ### 9. The coordinate class (probe I3) -/

/-- L-coordinates of the coordinate root 2e₀. -/
def cCoord : Fin 8 → ℤ := ![2, -2, -2, -2, 1, 1, 1, 2]

/-- cCoord really is the coordinate root: its ambient vector is
(2,0,0,0,0,0,0,0). -/
theorem coord_root_ambient :
    rowMul cCoord Bmat = ![2, 0, 0, 0, 0, 0, 0, 0] := by decide

/-- The coordinate root is one of the 240 roots. -/
theorem coord_root_in_roots : cCoord ∈ rootCoords := by decide

/-- **The coordinate-class law** (probe I3.2): the label of the
coordinate class is F1 + F2 + F3 — the fifteenth message label is the
sum of the three family labels. -/
theorem coord_class_eq_family_sum : labelOf cCoord = F1 + F2 + F3 := by
  decide

/-- The coordinate class is σ-fixed. -/
theorem coord_class_sigma_fixed :
    rowMul4 (labelOf cCoord) Msig = labelOf cCoord := by decide

end TfptCarrier.GaussianCodeBridge
