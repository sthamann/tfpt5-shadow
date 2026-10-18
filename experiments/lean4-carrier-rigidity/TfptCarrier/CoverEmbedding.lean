/-
  CoverEmbedding — the v600 joint-embedding integer core, certified.
  ==================================================================

  The compiler pair (U, V) realized on the mu3-cover y^3 = x^4 - 1
  restricts, on the saturated integral fixed lattice of the real
  structure (v599/v600), to the explicit integer matrices C_U, C_V
  below.  This module certifies the finite integer-linear-algebra
  core of QGEO.EMBED.01 (v600), determinant-free via Smith-normal-form
  certificates (only matrix-product identities):

    * the compiler relations of the pair (Cayley–Hamilton forms of
      the spectra x^2(x-3) and x(x-1)(x-2), and the joint traces
      tr(UV) = 3, tr(UV^2) = 6);
    * the seven-word matrix factors as W = T * S (explicit integers);
    * P * T = D with D = diag(1,1,1,3,3,3,3) and P unimodular
      (P * Pinv = 1): the elementary divisors of the transition are
      EXACTLY the v566 self-code pattern (1,1,1,3,3,3,3) — saturation
      index 81 = 3^4;
    * S is primitive: a 7x7 minor of S is unimodular
      (Smin * SminInv = 1), so S spans a saturated sublattice of Z^9
      and 81 is exactly the saturation index of the word Z-order.

  All proofs are kernel `decide` on explicit integer matrix products.
  Machine counterpart: verification/v600_joint_embedding.py (15/15).
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.CoverEmbedding

open Matrix

/-- The winding operator on the saturated integral fixed lattice. -/
def CU : Matrix (Fin 3) (Fin 3) ℤ :=
  !![3, 0, 0; -3, 0, 0; 0, 0, 0]

/-- The sheet operator on the saturated integral fixed lattice. -/
def CV : Matrix (Fin 3) (Fin 3) ℤ :=
  !![2, 1, -1; -2, -1, 2; -2, -1, 2]

/-- Cayley–Hamilton form of Spec C_U = {0,0,3}: the winding operator is
    rank one with C_U^2 = 3 C_U. -/
theorem CU_quadratic : CU * CU = 3 • CU := by decide

/-- trace C_U = 3 = N_fam. -/
theorem CU_trace : Matrix.trace CU = 3 := by decide

/-- Cayley–Hamilton form of Spec C_V = {0,1,2}: V^3 = 3 V^2 - 2 V
    (the binary sheet code). -/
theorem CV_cubic : CV * CV * CV = 3 • (CV * CV) - 2 • CV := by decide

/-- trace C_V = 3. -/
theorem CV_trace : Matrix.trace CV = 3 := by decide

/-- The first compiler joint trace: tr(UV) = 3. -/
theorem joint_trace_UV : Matrix.trace (CU * CV) = 3 := by decide

/-- The second compiler joint trace: tr(UV^2) = 6. -/
theorem joint_trace_UVV : Matrix.trace (CU * CV * CV) = 6 := by decide

/-- The seven-word matrix: rows are 1, U, V, UV, VU, V^2, VUV flattened
    to Z^9 (row-major). -/
def W : Matrix (Fin 7) (Fin 9) ℤ :=
  !![1, 0, 0,  0,  1, 0,  0,  0, 1;
     3, 0, 0, -3,  0, 0,  0,  0, 0;
     2, 1, -1, -2, -1, 2, -2, -1, 2;
     6, 3, -3, -6, -3, 3,  0,  0, 0;
     3, 0, 0, -3,  0, 0, -3,  0, 0;
     4, 2, -2, -6, -3, 4, -6, -3, 4;
     6, 3, -3, -6, -3, 3, -6, -3, 3]

/-- A basis of the SATURATION of the word lattice. -/
def S : Matrix (Fin 7) (Fin 9) ℤ :=
  !![1, 0, 0,  0,  1, 0,  0,  0,  1;
     0, 1, -1, -2, -3, 2, -2, -1,  0;
     0, 0, 0,  2,  1, 0,  2,  1,  0;
     0, 0, 0,  0,  0, 1, -2, -1,  2;
     0, 0, 0,  1,  0, 0,  1,  1, -1;
     0, 0, 0,  0,  0, 0,  1,  0,  0;
     0, 0, 0,  0,  0, 0,  0,  1, -1]

/-- The transition matrix expressing the words in the saturated basis. -/
def T : Matrix (Fin 7) (Fin 7) ℤ :=
  !![1, 0,  0,  0, 0,  0,  0;
     3, 0, -3,  0, 3,  3,  0;
     2, 1,  0,  0, 0,  0,  0;
     6, 3,  0, -3, 0,  0,  0;
     3, 0, -3,  0, 3,  0,  0;
     4, 2, -1,  0, 0,  0,  0;
     6, 3,  0, -3, 0, -6, -3]

/-- Unimodular row-operation matrix bringing T to Smith diagonal form. -/
def P : Matrix (Fin 7) (Fin 7) ℤ :=
  !![1, 0, 0, 0, 0, 0, 0;
     -2, 0, 1, 0, 0, 0, 0;
     0, 0, 2, 0, 0, -1, 0;
     0, 0, 3, -1, 0, 0, 0;
     -3, 0, 6, 0, 1, -3, 0;
     0, 1, 0, 0, -1, 0, 0;
     0, -2, 0, 1, 2, 0, -1]

/-- Integer inverse of P (unimodularity certificate). -/
def Pinv : Matrix (Fin 7) (Fin 7) ℤ :=
  !![1, 0, 0, 0, 0, 0, 0;
     3, 0, -3, 0, 1, 1, 0;
     2, 1, 0, 0, 0, 0, 0;
     6, 3, 0, -1, 0, 0, 0;
     3, 0, -3, 0, 1, 0, 0;
     4, 2, -1, 0, 0, 0, 0;
     6, 3, 0, -1, 0, -2, -1]

/-- The Smith diagonal: the v566 self-code divisor pattern. -/
def D : Matrix (Fin 7) (Fin 7) ℤ :=
  Matrix.diagonal ![1, 1, 1, 3, 3, 3, 3]

/-- The words lie in the lattice spanned by S, with transition T. -/
theorem words_factor : W = T * S := by decide

/-- P is unimodular: P * Pinv = 1. -/
theorem P_unimodular : P * Pinv = 1 := by decide

/-- The Smith certificate: P * T = D = diag(1,1,1,3,3,3,3).  With
    `P_unimodular` this identifies the elementary divisors of the word
    transition as EXACTLY the v566 self-code pattern; the saturation
    index is 1*1*1*3*3*3*3 = 81 = 3^4. -/
theorem smith_certificate : P * T = D := by decide

/-- The 7x7 minor of S on columns (0,1,3,4,5,6,7). -/
def Smin : Matrix (Fin 7) (Fin 7) ℤ :=
  !![1, 0, 0, 1, 0, 0, 0;
     0, 1, -2, -3, 2, -2, -1;
     0, 0, 2, 1, 0, 2, 1;
     0, 0, 0, 0, 1, -2, -1;
     0, 0, 1, 0, 0, 1, 1;
     0, 0, 0, 0, 0, 1, 0;
     0, 0, 0, 0, 0, 0, 1]

/-- Integer inverse of the minor (primitivity certificate for S: the
    minor is unimodular, so S spans a saturated sublattice of Z^9). -/
def SminInv : Matrix (Fin 7) (Fin 7) ℤ :=
  !![1, 0, -1, 0, 2, 0, -1;
     0, 1, 3, -2, -4, -4, 0;
     0, 0, 0, 0, 1, -1, -1;
     0, 0, 1, 0, -2, 0, 1;
     0, 0, 0, 1, 0, 2, 1;
     0, 0, 0, 0, 0, 1, 0;
     0, 0, 0, 0, 0, 0, 1]

theorem S_primitive : Smin * SminInv = 1 := by decide

/-- 81 = 3^4: the certified index is the fourth power of the family
    count. -/
theorem index_is_three_pow_four : (1 * 1 * 1 * 3 * 3 * 3 * 3 : ℤ) = 3 ^ 4 := by
  norm_num

/-! ### The restricted polarization form (v604)

The real structure is an anti-isometry of the polarization
(`M^dagger J M = J^T`, machine-checked in v604), so J restricts to a
real symmetric INTEGER form on the saturated fixed lattice. -/

/-- The restricted polarization form on the fixed lattice. -/
def Jfix : Matrix (Fin 3) (Fin 3) ℤ :=
  !![16, 2, 4; 2, -2, 2; 4, 2, -2]

theorem Jfix_symmetric : Jfix.transpose = Jfix := by decide

/-- det J_fix = 72 = 8 * 9: the polarization determinant times the
    (1-omega)-covolume factor. -/
theorem Jfix_det : Jfix.det = 72 := by decide

theorem Jfix_det_factorization : (72 : ℤ) = 8 * 3 ^ 2 := by norm_num

/-- The J_fix-dual of the sheet operator (the plane-stabilizer half of
    the duality, v602/v604). -/
def CVdual : Matrix (Fin 3) (Fin 3) ℤ :=
  !![1, 0, 0; -2, 0, 0; 2, 1, 2]

/-- Duality certificate: C_V^T * J_fix = J_fix * C_Vdual (the transpose
    with respect to the restricted polarization form is the explicit
    integer dual operator). -/
theorem CV_dual_certificate : CV.transpose * Jfix = Jfix * CVdual := by decide

/-- The dual sheet operator carries the same binary code:
    C_Vdual^3 = 3 C_Vdual^2 - 2 C_Vdual (Spec = {0,1,2}). -/
theorem CVdual_cubic :
    CVdual * CVdual * CVdual = 3 • (CVdual * CVdual) - 2 • CVdual := by decide

/-- Dual joint trace: tr(C_U * C_Vdual) = 3. -/
theorem dual_joint_trace : Matrix.trace (CU * CVdual) = 3 := by decide

end TfptCarrier.CoverEmbedding
