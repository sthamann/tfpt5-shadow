/-
  ArfSpinorCompiler — the Arf/spinor compiler on V = L/(1+i)L ≅ F₂⁴.
  ==================================================================

  Machine-checked finite-algebra kernel of the Arf compiler programme
  Priority 1 (contract candidate ARF.SPINORCOMPILER.01).  Numeric
  counterpart: experiments/tfpt-discovery/arf_spinor_compiler_probe.py
  (46/46, verdict ARF-SPINOR-EXACT, fully deterministic, exact
  integer/F₂/Fraction arithmetic).

  THE SETTING.  V = L/(1+i)L ≅ F₂⁴ in the family/anchor basis
  (F1, F2, F3, A) with the reduced hermitian form h̄ whose Gram
  matrix is all ones off the diagonal (probe S1, = ProjectiveHamming
  G; certified from the concrete lattice by v752).  The parity lift
  ι(v) = (f1, f2, f3, a, f1+f2+f3+a) embeds V as the even-weight
  code C_even(5) on the five carrier slots of S⁺_{D5} = Λ^even ℂ⁵
  (v2/v310, CAR.SM.01), and q*(v) = wt(ι(v))/2 mod 2 is the
  canonical quadratic refinement of h̄.

  Certified here, kernel `decide` / `norm_num` only (no sorry, no
  native_decide):

  L (the parity lift, crosslink 1):
    * `iota_even`      — every ι(v) has even weight (ι lands in
      C_even(5));
    * `iota_injective` — ι is injective (16 = |C_even(5)| words);
    * `beta_eq_symp`   — β(v,w) = ι(v)·ι(w) mod 2 EQUALS h̄(v,w) in
      all 256 cells: the dot product of the carrier slots IS the
      symplectic form of the Gaussian quotient.

  Q (the canonical refinement and the selector):
    * `qstar_refines`  — q*(v+w) + q*(v) + q*(w) = h̄(v,w) for all
      256 pairs (q* is a quadratic refinement);
    * `qstar_sigma_invariant` — q* ∘ σ = q* for the family 3-cycle
      σ(f1,f2,f3,a) = (f3,f1,f2,a);
    * `selector_unique` — inside the parametrization
      q_c = q* + h̄(·,c) of ALL 16 refinements (probe S2/S6:
      brute force over all 2¹⁶ functions finds exactly these), the
      frozen selector (σ-invariance ∧ q(A) = 1 ∧ q(F_Σ) = 0) holds
      IFF c = 0 — q* is the unique selected form.

  A (the Arf census 6 + 10 and the 1 + 5̄ + 10 decomposition):
    * `qc_injective`   — the 16 refinements q_c are pairwise
      distinct;
    * `arf_offset_law` — zeros(q_c) = 6 if q*(c) = 0 else 10 (the
      Arf discriminant law Arf(q + h̄(·,c)) = Arf(q) + q(c));
    * `arf_census`     — exactly 6 offsets c with zeros(q_c) = 6
      (Arf 1) and 10 with zeros(q_c) = 10 (Arf 0);
    * `word_decomposition` — |{v ≠ 0 : q*(v) = 0}| = 5 (the 5̄) and
      |{v : q*(v) = 1}| = 10 (the 10): 16 = 1 + 5 + 10 — the Pascal
      row of the carrier (v2) as Arf geometry;
    * `orbit_partition_counts` — the same 1/5/10 as the offset
      partition {0} ⊔ {c ≠ 0, q*(c) = 0} ⊔ {q*(c) = 1} (the
      Stab(q*)-orbit sizes; transitivity of the S₅-action is the
      probe's job, S7).

  X (the hypercharge code polynomial, exact integer statements):
    * `X_traceless` / `X_primitive` — X = (-2,-2,-2,3,3) sums to 0,
      gcd = 1;
    * `moment_card` / `moment_one` / `moment_two` / `moment_three` —
      the Euler moments of P_X(z) = Σ_v z^{X(ι(v))}: P(1) = 16,
      DP(1) = Σ X = 0, D²P(1) = Σ X² = 120 (the master moment
      Tr_{S⁺} X² = 120 = 5! = |R⁺(E8)|, v2), D³P(1) = Σ X³ = 0;
    * `moment_chain`   — 120/3 = 40, 40+1 = 41 (= 10·b₁), 2·120 =
      240, 240+8 = 248.

  N (NS/R and Pati–Salam bookkeeping):
    * `chiNSR_is_anchor_bit` — h̄(v, F_Σ) = a: the NS/R parity IS
      the fourth information bit (v752 P5.3 in this basis);
    * `ps_split` — the p_F = f1+f2+f3 parity splits the 16 words
      8 + 8 (the (4,2,1) ⊕ (4̄,1,2) counting);
    * `sigma_slot_split` — ι ∘ σ cycles the first three carrier
      slots and fixes the last two: the SAME σ that is the family
      3-cycle A3^Fam on the message bits acts on the five carrier
      slots as the 3+2 split (A3^PS register).  NAMING DISCIPLINE
      (user's correction): two different registers of one group
      element — no physics claim.

  F (must-fail control):
    * `dot_form_no_refinement` — the non-alternating dot form on V
      admits NO quadratic refinement (witness v = e₀ with
      b(v,v) = 1 ≠ 0 forced to 0 by the refinement identity).

  HONEST SCOPE.  The completeness of the 16-family q_c (that NO
  further function refines h̄) is the probe's 2¹⁶ brute force (S2);
  Sp(4,2) ≅ S₆, the transitivity of the Stab(q*)-orbits, the K6
  duad model, B = I + A_{KG(6,2)}, the ovoid eigenvectors and the
  spread census are certified by the probe (S3–S10), not
  re-formalized here.  The identification of V, h̄ and the basis
  with the concrete E8 lattice is v752's exact lattice computation
  (mirrored in ProjectiveHamming.lean).  The PHYSICAL reading of
  q*/Arf as a matter classifier is NOT claimed — that is Priority
  2's separate kill test.

  Standalone module: no imports from other TfptCarrier files.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.ArfSpinorCompiler

/-! ### 0. The label space and the reduced form (v752 basis) -/

/-- The label space V = L/(1+i)L ≅ F₂⁴ in the family/anchor basis
(F1, F2, F3, A). -/
abbrev Label := Fin 4 → ZMod 2

/-- Gram matrix of h̄ in the family/anchor basis: all ones off the
diagonal (probe S1.3, = ProjectiveHamming.G). -/
def G : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![0, 1, 1, 1;
     1, 0, 1, 1;
     1, 1, 0, 1;
     1, 1, 1, 0]

/-- The reduced hermitian form h̄. -/
def symp (x y : Label) : ZMod 2 := ∑ i, ∑ j, x i * G i j * y j

/-- The family 3-cycle σ: F1 → F2 → F3 → F1, A fixed; on coordinates
(f1,f2,f3,a) ↦ (f3,f1,f2,a) (probe S1.5). -/
def sigmaMap (v : Label) : Label := ![v 2, v 0, v 1, v 3]

/-- σ is symplectic for h̄ (all 256 pairs). -/
theorem sigma_symplectic :
    ∀ x y : Label, symp (sigmaMap x) (sigmaMap y) = symp x y := by
  decide

/-! ### 1. L — the parity lift ι and β = h̄ (crosslink 1) -/

/-- The parity lift into the five carrier slots:
ι(v) = (f1, f2, f3, a, f1+f2+f3+a). -/
def iota (v : Label) : Fin 5 → ZMod 2 :=
  ![v 0, v 1, v 2, v 3, v 0 + v 1 + v 2 + v 3]

/-- ι lands in the even-weight code C_even(5): Σ slots = 0. -/
theorem iota_even : ∀ v : Label, (∑ i, iota v i) = 0 := by decide

/-- ι is injective — V ≅ C_even(5) as sets of 16 words. -/
theorem iota_injective :
    ∀ v w : Label, iota v = iota w → v = w := by decide

/-- The slot dot product β(v,w) = ι(v)·ι(w). -/
def beta (v w : Label) : ZMod 2 := ∑ i, iota v i * iota w i

/-- **CROSSLINK 1**: β = h̄ in all 256 cells — the carrier-slot dot
product IS the symplectic form of the Gaussian quotient. -/
theorem beta_eq_symp : ∀ v w : Label, beta v w = symp v w := by decide

/-! ### 2. Q — the canonical refinement q* and the frozen selector -/

/-- Weight of ι(v) as a natural number. -/
def wtIota (v : Label) : ℕ :=
  (Finset.univ.filter fun i : Fin 5 => iota v i = 1).card

/-- The canonical quadratic refinement: q*(v) = wt(ι(v))/2 mod 2. -/
def qstar (v : Label) : ZMod 2 := ((wtIota v / 2) % 2 : ℕ)

/-- q* REFINES h̄: q*(v+w) + q*(v) + q*(w) = h̄(v,w) (all 256
pairs). -/
theorem qstar_refines :
    ∀ v w : Label, qstar (v + w) + qstar v + qstar w = symp v w := by
  decide

/-- q* is σ-invariant. -/
theorem qstar_sigma_invariant :
    ∀ v : Label, qstar (sigmaMap v) = qstar v := by decide

/-- The offset family q_c = q* + h̄(·,c) — by the probe's 2¹⁶ brute
force (S2) these are ALL 16 quadratic refinements of h̄. -/
def qc (c v : Label) : ZMod 2 := qstar v + symp v c

/-- The 16 refinements are pairwise distinct (the parametrization is
faithful). -/
theorem qc_injective :
    ∀ c c' : Label, (∀ v, qc c v = qc c' v) → c = c' := by decide

/-- The anchor label A = (0,0,0,1). -/
def anchorA : Label := ![0, 0, 0, 1]

/-- The checksum label F_Σ = F1+F2+F3 = (1,1,1,0). -/
def Fsigma : Label := ![1, 1, 1, 0]

/-- **THE FROZEN SELECTOR IS UNIQUE**: within the 16 refinements,
σ-invariance ∧ q(A) = 1 ∧ q(F_Σ) = 0 holds iff c = 0, i.e. exactly
for q* itself (probe S4: census 4 → 2 → 1). -/
theorem selector_unique :
    ∀ c : Label,
      ((∀ v, qc c (sigmaMap v) = qc c v) ∧ qc c anchorA = 1 ∧
        qc c Fsigma = 0) ↔ c = 0 := by decide

/-! ### 3. A — the Arf census 6 + 10 and the 1 + 5̄ + 10 -/

/-- Zero count of a refinement (the Arf discriminant: 6 zeros ⇔
Arf 1, 10 zeros ⇔ Arf 0). -/
def zeros (c : Label) : ℕ :=
  (Finset.univ.filter fun v : Label => qc c v = 0).card

/-- The Arf offset law: zeros(q_c) = 6 if q*(c) = 0 else 10 — the
discriminant identity Arf(q + h̄(·,c)) = Arf(q) + q(c) in counting
form. -/
theorem arf_offset_law :
    ∀ c : Label, zeros c = if qstar c = 0 then 6 else 10 := by decide

/-- **THE ARF CENSUS**: exactly 6 refinements of Arf type 1 (6
zeros) and 10 of Arf type 0 (10 zeros). -/
theorem arf_census :
    (Finset.univ.filter fun c : Label => zeros c = 6).card = 6 ∧
    (Finset.univ.filter fun c : Label => zeros c = 10).card = 10 := by
  decide

/-- **THE WORD DECOMPOSITION 16 = 1 + 5̄ + 10**: q* has exactly 5
nonzero zeros (the 5̄) and 10 ones (the 10) — the Pascal row
(1, 5, 10) of the carrier S⁺ = Λ^even ℂ⁵ as Arf geometry. -/
theorem word_decomposition :
    (Finset.univ.filter fun v : Label => v ≠ 0 ∧ qstar v = 0).card = 5
    ∧ (Finset.univ.filter fun v : Label => qstar v = 1).card = 10 := by
  decide

/-- The offset partition mirrors the Stab(q*)-orbit sizes: {0} ⊔
{c ≠ 0 : q*(c) = 0} (the 5 remaining Arf-1 forms) ⊔ {c : q*(c) = 1}
(the 10 Arf-0 forms) — counts 1, 5, 10 (transitivity: probe S7). -/
theorem orbit_partition_counts :
    (Finset.univ.filter fun c : Label => c = 0).card = 1 ∧
    (Finset.univ.filter fun c : Label => c ≠ 0 ∧ qstar c = 0).card = 5
    ∧ (Finset.univ.filter fun c : Label => qstar c = 1).card = 10 := by
  decide

/-! ### 4. X — the hypercharge code polynomial (exact over ℤ) -/

/-- The hypercharge generator X = (-2,-2,-2,3,3) on the five carrier
slots. -/
def X : Fin 5 → ℤ := ![-2, -2, -2, 3, 3]

/-- X is traceless: Σ X = 0. -/
theorem X_traceless : (∑ i, X i) = 0 := by decide

/-- X is primitive: gcd of the entries is 1. -/
theorem X_primitive :
    Nat.gcd (Int.natAbs (X 0)) (Nat.gcd (Int.natAbs (X 3))
      (Int.natAbs (X 4))) = 1 := by decide

/-- The X-weight of a word: X(v) = Σ_{slots with ι(v) = 1} X_i. -/
def Xw (v : Label) : ℤ := ∑ i, if iota v i = 1 then X i else 0

/-- P_X(1) = 16: the 16 words of the carrier. -/
theorem moment_card : Fintype.card Label = 16 := by decide

/-- DP_X(1) = Σ X(v) = 0 (tracelessness of the code polynomial). -/
theorem moment_one : (∑ v : Label, Xw v) = 0 := by decide

/-- **THE MASTER MOMENT**: D²P_X(1) = Σ X(v)² = 120 = Tr_{S⁺} X² =
5! = |R⁺(E8)| (v2_carrier_pascal). -/
theorem moment_two : (∑ v : Label, Xw v ^ 2) = 120 := by decide

/-- D³P_X(1) = Σ X(v)³ = 0 (odd-moment vanishing — the cubic
anomaly). -/
theorem moment_three : (∑ v : Label, Xw v ^ 3) = 0 := by decide

/-- The chain: 120/3 = 40, 40+1 = 41 (= 10·b₁), 2·120 = 240,
240+8 = 248 = dim E8. -/
theorem moment_chain :
    120 / 3 = 40 ∧ 40 + 1 = 41 ∧ 2 * 120 = 240 ∧ 240 + 8 = 248 := by
  norm_num

/-! ### 5. N — NS/R and Pati–Salam bookkeeping -/

/-- **χ_NSR IS THE FOURTH INFORMATION BIT**: h̄(v, F_Σ) = a for
every word (v752 P5.3 in the family/anchor basis). -/
theorem chiNSR_is_anchor_bit :
    ∀ v : Label, symp v Fsigma = v 3 := by decide

/-- The Pati–Salam parity p_F = f1+f2+f3 splits 16 = 8 + 8 (the
(4,2,1) ⊕ (4̄,1,2) counting; the A bit is the isospin index on each
side, probe S13.1). -/
theorem ps_split :
    (Finset.univ.filter fun v : Label => v 0 + v 1 + v 2 = 1).card = 8
    ∧ (Finset.univ.filter fun v : Label =>
        v 0 + v 1 + v 2 = 0).card = 8 := by decide

/-- **THE 3+2 SLOT SPLIT**: ι ∘ σ permutes the five carrier slots by
the 3-cycle (1 2 3) and fixes slots 4, 5 — the SAME group element σ
is the family 3-cycle A3^Fam on the message bits and the 3+2
(colour+weak style) partition A3^PS on the carrier slots.  Naming
discipline; no physics claim. -/
theorem sigma_slot_split :
    ∀ v : Label,
      iota (sigmaMap v)
        = ![iota v 2, iota v 0, iota v 1, iota v 3, iota v 4] := by
  decide

/-! ### 6. F — must-fail control -/

/-- The non-alternating dot form on V. -/
def dotForm (v w : Label) : ZMod 2 := ∑ i, v i * w i

/-- The witness word e₀ = F1. -/
def e0 : Label := ![1, 0, 0, 0]

/-- **Must-fail**: the dot form admits NO quadratic refinement —
diagonalizing the refinement identity forces q(0) = b(v,v) for every
v, but the dot form has b(0,0) = 0 and b(e₀,e₀) = 1 (probe C1: the
full 2¹⁶ census finds zero refinements). -/
theorem dot_form_no_refinement :
    ¬ ∃ q : Label → ZMod 2,
      ∀ v w : Label, q (v + w) + q v + q w = dotForm v w := by
  rintro ⟨q, hq⟩
  have hz : (0 : Label) + 0 = 0 := by decide
  have hee : e0 + e0 = 0 := by decide
  have hd0 : dotForm 0 0 = 0 := by decide
  have hd1 : dotForm e0 e0 = 1 := by decide
  have key : ∀ a b : ZMod 2, a + b + b = a := by decide
  have h0 := hq 0 0
  rw [hz, hd0, key] at h0
  have h1 := hq e0 e0
  rw [hee, hd1, key] at h1
  rw [h0] at h1
  exact absurd h1 (by decide)

end TfptCarrier.ArfSpinorCompiler
