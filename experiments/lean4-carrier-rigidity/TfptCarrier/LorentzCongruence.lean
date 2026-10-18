/-
  LorentzCongruence — the v624 Lorentz congruence, certified.
  ============================================================

  The external-review lattice audit (v624, EXTREV.LATTICE.01, part C)
  identifies the prime-front determinant form and the v604 cover
  polarization lattice as the SAME rational quadratic form:

    * J_det = [[0,1,0],[1,0,0],[0,0,-2]] is the determinant form of the
      prime front (det X = (1/2) yᵀ J_det y for y = (X11, X22, X12)),
      det J_det = 2, Lorentz signature (1,2);
    * J_fix is the restricted polarization form on the saturated fixed
      lattice of the mu3-cover (v604, already certified in
      `CoverEmbedding.Jfix` — the congruence below lands EXACTLY on
      that object);
    * the explicit integer matrix P with det P = -6 realizes

          Pᵀ · J_det · P = J_fix         (exactly, over ℤ):

      the cover polarization lattice is an INDEX-6 sublattice of the
      prime-front determinant lattice, and the determinants close:
      72 = 2 · 6² (Jfix_det = 72 in CoverEmbedding, det J_det = 2,
      index 6 = |det P|).

  All proofs are kernel `decide` on explicit 3×3 integer matrices, in
  the style of `CoverEmbedding.lean`.  Machine counterpart:
  verification/v624_external_lattice_audit.py (part C, sympy-exact).
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic
import TfptCarrier.CoverEmbedding

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.LorentzCongruence

open Matrix

/-- The congruence matrix (columns = the cover-lattice basis expressed
in prime-front determinant coordinates). -/
def P : Matrix (Fin 3) (Fin 3) ℤ :=
  !![3, 0, 0; 3, 0, 2; -1, 1, -1]

/-- The prime-front determinant form: `det X = (1/2)·yᵀ J_det y` for
`y = (X11, X22, X12)`; Lorentz signature (1,2). -/
def Jdet : Matrix (Fin 3) (Fin 3) ℤ :=
  !![0, 1, 0; 1, 0, 0; 0, 0, -2]

/-- **The Lorentz congruence** (v624 C2): `Pᵀ · J_det · P = J_fix`
EXACTLY, where `J_fix` is the v604 restricted polarization form already
certified in `CoverEmbedding` — the prime-front determinant form and
the cover polarization lattice are the same rational quadratic form. -/
theorem lorentz_congruence :
    P.transpose * Jdet * P = CoverEmbedding.Jfix := by decide

/-- The congruence has index 6: `det P = -6`. -/
theorem P_det : P.det = -6 := by decide

/-- The two determinants: `det J_det = 2` and `det J_fix = 72`. -/
theorem Jdet_det : Jdet.det = 2 ∧ CoverEmbedding.Jfix.det = 72 := by
  exact ⟨by decide, CoverEmbedding.Jfix_det⟩

/-- The index-6 sublattice fact as a determinant identity:
`72 = 2 · 6²` (det J_fix = det J_det · (det P)²). -/
theorem Jfix_det_index_six : (72 : ℤ) = 2 * 6 ^ 2 := by norm_num

end TfptCarrier.LorentzCongruence
