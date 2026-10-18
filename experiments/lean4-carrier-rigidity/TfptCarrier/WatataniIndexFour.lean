/-
  WatataniIndexFour — the μ4 index-4 certificate, smallest exact model.
  =====================================================================

  Machine-checked algebraic core of the T2 slice (probe
  experiments/tfpt-discovery/phys_car_pp_index_probe.py, verdict
  T2-SLICE-GO / PP-INDEX-4-ON-LADDER; contract candidate
  GNET.RAMIFIED.01): the μ4-average conditional expectation
  E(x) = ¼·Σ_j U^j x U^{−j} = Σ_q P_q x P_q has Watatani index 4 =
  |μ4| = N(1+i)², certified by an explicit quasi-basis on the
  SMALLEST exact instance — M₄(ℤ[i]) with the charge grading
  U = diag(1, i, −1, −i), one dimension per μ4 sector (exactly the
  probe's quasi-basis {1} ∪ {|q,a⟩⟨q',b|/√n_{q'}} with all n_q = 1:
  every weight is 1, no square roots, everything in ℤ[i]).

  Contents (kernel `decide` on the ℤ and ℤ[i] layers; the ℚ layer W3
  is checked entrywise by `simp`/`norm_num`, since ℚ arithmetic does
  not kernel-reduce under `decide`):
    W0  the clock-derivation shadow (probe G0, smallest instance
        N = 12, integer matrices): the NS-twisted shift has
        S¹² = −1; the half-turn H = L⁶ (L = S^{N/12}) obeys
        H² = S^N = −1 and H⁴ = 1 — μ4-order FORCED by the NS spin
        structure; the deck D = L⁴ has D³ = −1 and [H, D] = 0.
    W1  the model algebra: U unitary of genuine order 4; the sector
        projections are the μ4 Fourier modes of U (denominators
        cleared): 4·P_q = Σ_j conj(χ_q(j))·U^j; pinching = group
        average on the 16 matrix units (an ℤ[i]-basis; both sides
        ℤ[i]-linear — linearity cited, not formalized); E(1) = 1,
        E idempotent, E lands in the fixed algebra = the diagonal
        (Ad-U-commutant certified on the unit basis).
    W2  THE INDEX: the explicit 13-element quasi-basis
        {1} ∪ {e_{ab} : a ≠ b} satisfies the Watatani reconstruction
        x = Σ_v v·E(v*·x) on the unit basis and Σ_v v·v* = 4·1
        EXACTLY (probe QB k: rec_dev / ind_dev = 0 here); index
        4 = N(1+i)² — the ramified-place reading.
    W3  the Pimsner-Popa constant shadow (over ℚ): at the probe's
        mixing minimizer (the all-ones matrix J = 4·|v⟩⟨v|),
        E(J) = 1 and 4·E(J) − J is the K₄ Laplacian, whose quadratic
        form is a sum of six squares (SOS certificate: PP holds at
        λ = ¼); any λ > ¼ FAILS on the mixing vector (4 − 16λ < 0):
        λ* = ¼ exactly (probe lam_star = 0.25).
    W4  controls (probe K4 environment): the μ2 model (M₂, two
        sectors) has index 2 — the certificate separates μ4 from μ2
        (probe lam_z2 = 1/2, Ind 2); the three-sector model (M₃)
        has index 3 — the probe's k = 1 boundary anomaly (only 3
        sectors visible, Ind = 3).  Moral: index = #sectors.
    W5  the dual character picture: character orthogonality on ℤ/4,
        Σ_k χ_k(a)·conj(χ_k(b)) = 4·δ_{ab} — simultaneously the
        Watatani index identity Σ_k v_k v_k* = 4·1 and the Fourier
        reconstruction for the DUAL inclusion ℂ·1 ⊂ C(ℤ/4) (Haar
        average, quasi-basis = the four characters): the
        crossed-product dual of the same μ4 datum.

  HONEST SCOPE.  What this file certifies is the exact ALGEBRAIC
  index-4 structure of a μ4-average conditional expectation in its
  smallest faithful matrix model, plus the clock-order shadow and the
  sharp PP constant at the mixing element.  NOT formalized: the CAR
  algebra / Fock space / Jordan-Wigner layer, Gaussian states and
  Takesaki commutation ([ρ, U] = 0), the k-window sector dimensions
  4^{k−1} ± 2^{k−1} and their irrational quasi-basis weights 1/√n_q
  (k ≥ 2), the N- and k-ladder convergence (probe K3 witnesses
  w_q → ¼, |⟨U^j⟩| → 0), the Ramond zero-mode dressing
  U' = Γ(H_R)·e^{iπn₀/2}, outerness, and the (1+i)/E8 dictionary
  beyond the norm identity 4 = N(1+i)².  The model's U is the CHARGE
  grading (spectrum i^q, U⁴ = 1); the one-particle half-turn with
  H² = −1 lives in W0 — the Fock functor between the two is cited,
  not formalized.
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.NumberTheory.Zsqrtd.Basic
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.WatataniIndexFour

/-! ### W0. The clock-derivation shadow (probe G0, N = 12) -/

/-- The NS-twisted cyclic shift on 12 sites: S·e_j = e_{j+1},
S·e_{11} = −e_0 (the v679 frame at the smallest clock-divisible
size). -/
def Sh : Matrix (Fin 12) (Fin 12) ℤ :=
  Matrix.of fun j k =>
    if (j : ℕ) = (k : ℕ) + 1 then 1
    else if (j : ℕ) = 0 ∧ (k : ℕ) = 11 then -1 else 0

/-- NS spin structure: S¹² = −1 (antiperiodic boundary — the spin
doubling that forces the μ4 order below). -/
theorem ns_shift_order : Sh ^ 12 = -1 := by decide

/-- **μ4 order forced by NS** (probe G0): the half-turn H = L⁶ of the
clock L = S^{N/12} obeys H² = S^N = −1 and H⁴ = 1 — order 4 is not
inserted, it is forced by the NS spin structure. -/
theorem mu4_order_forced_by_ns :
    (Sh ^ 6) * (Sh ^ 6) = -1 ∧ (Sh ^ 6) ^ 4 = 1 := by decide

/-- The deck D = L⁴: D³ = −1 (spin-doubled 3-cycle) and [H, D] = 0
(probe G0: the deck commutes and is NOT used in E). -/
theorem deck_layer :
    (Sh ^ 4) ^ 3 = -1 ∧ (Sh ^ 4) * (Sh ^ 6) = (Sh ^ 6) * (Sh ^ 4) := by
  decide

/-! ### W1. The model algebra M₄(ℤ[i]) with the μ4 charge grading -/

/-- ℤ[i], as the quadratic ring ℤ√(−1). -/
abbrev Zi : Type := Zsqrtd (-1)

/-- The imaginary unit i ∈ ℤ[i]. -/
def gi : Zi := ⟨0, 1⟩

theorem gi_pow : gi * gi = -1 ∧ gi * gi * gi * gi = 1 := by decide

/-- Complex conjugation on ℤ[i] (explicit, kernel-friendly). -/
def gconj (z : Zi) : Zi := ⟨z.re, -z.im⟩

/-- Adjoint (conjugate transpose) of a ℤ[i] matrix. -/
def adj {n : ℕ} (M : Matrix (Fin n) (Fin n) Zi) :
    Matrix (Fin n) (Fin n) Zi :=
  Matrix.of fun j k => gconj (M k j)

/-- The model algebra. -/
abbrev M4 := Matrix (Fin 4) (Fin 4) Zi

/-- The μ4 charge grading U = diag(1, i, −1, −i) = diag(i^q) — the
model of the probe's canonical implementer Γ(H_W) on the four charge
sectors, one dimension per sector. -/
def U : M4 :=
  !![1, 0, 0, 0;
     0, gi, 0, 0;
     0, 0, -1, 0;
     0, 0, 0, -gi]

/-- U is unitary. -/
theorem U_unitary : U * adj U = 1 ∧ adj U * U = 1 := by decide

/-- U has genuine order 4 (U⁴ = 1, U² ≠ 1): the μ4 action is faithful
on the model. -/
theorem U_order_four : U ^ 4 = 1 ∧ U ^ 2 ≠ 1 := by decide

/-- The powers 1, U, U², U³ as an explicit family. -/
def Upow : Fin 4 → M4 := ![1, U, U ^ 2, U ^ 3]

/-- The μ4 character table χ_q(j) = i^{q·j}. -/
def chi : Fin 4 → Fin 4 → Zi :=
  ![![1, 1, 1, 1],
    ![1, gi, -1, -gi],
    ![1, -1, 1, -1],
    ![1, -gi, -1, gi]]

/-- The sector projections P_q = e_{qq}. -/
def Psec : Fin 4 → M4 := fun q =>
  Matrix.of fun a b => if a = q ∧ b = q then 1 else 0

/-- The sector projections are complete and orthogonal. -/
theorem Psec_complete :
    (∑ q, Psec q) = 1 ∧
    ∀ q q' : Fin 4, Psec q * Psec q' = if q = q' then Psec q else 0 := by
  decide

/-- **Spectral certificate** (probe `sector_projs`, denominator
cleared): 4·P_q = Σ_j conj(χ_q(j))·U^j — the sector projections are
the μ4 Fourier modes of the grading unitary. -/
theorem sector_projection_fourier :
    ∀ q : Fin 4, (4 : Zi) • Psec q = ∑ j, gconj (chi q j) • Upow j := by
  decide

/-- The μ4-average conditional expectation, in exact pinching form
(no denominator): E(x) = Σ_q P_q x P_q. -/
def Efix (x : M4) : M4 := ∑ q, Psec q * x * Psec q

/-- Matrix units e_{ab}. -/
def Eu (a b : Fin 4) : M4 :=
  Matrix.of fun j k => if j = a ∧ k = b then 1 else 0

/-- **Pinching = group average** (probe `E group-average == pinching`,
denominator cleared), verified on the 16 matrix units — an
ℤ[i]-basis of M₄; both sides are ℤ[i]-linear in x, so this is the
full identity (linearity cited, not formalized). -/
theorem pinching_eq_group_average :
    ∀ a b : Fin 4,
      (∑ j, Upow j * Eu a b * adj (Upow j))
        = (4 : Zi) • Efix (Eu a b) := by decide

/-- E is unital. -/
theorem Efix_unital : Efix 1 = 1 := by decide

/-- E in closed form on the unit basis: E(e_{ab}) = δ_{ab}·e_{aa} —
the range is the diagonal algebra (the μ4 fixed algebra of the
model). -/
theorem Efix_diagonal :
    ∀ a b : Fin 4, Efix (Eu a b) = if a = b then Eu a a else 0 := by
  decide

/-- E is idempotent on the unit basis. -/
theorem Efix_idempotent :
    ∀ a b : Fin 4, Efix (Efix (Eu a b)) = Efix (Eu a b) := by decide

/-- The range of E commutes with U (E maps into the fixed algebra). -/
theorem Efix_range_fixed :
    ∀ a b : Fin 4, U * Efix (Eu a b) = Efix (Eu a b) * U := by decide

/-- The Ad-U fixed algebra is EXACTLY the diagonal, on the unit
basis: e_{ab} commutes with U iff a = b. -/
theorem fixed_units_are_diagonal :
    ∀ a b : Fin 4, (U * Eu a b = Eu a b * U) ↔ a = b := by decide

/-! ### W2. The quasi-basis and the Watatani index -/

/-- The Watatani quasi-basis of E: {1} ∪ {e_{ab} : a ≠ b}, 13
elements — the probe's {1} ∪ {|q,a⟩⟨q',b|/√n_{q'}} with all
n_q = 1: every weight is exactly 1, no square roots (the smallest
exact instance of the QB(k) layer). -/
def quasibasis : List M4 :=
  [1,
   Eu 0 1, Eu 0 2, Eu 0 3,
   Eu 1 0, Eu 1 2, Eu 1 3,
   Eu 2 0, Eu 2 1, Eu 2 3,
   Eu 3 0, Eu 3 1, Eu 3 2]

theorem quasibasis_length : quasibasis.length = 13 := by rfl

/-- **Quasi-basis reconstruction** (probe QB: `rec_dev`): x = Σ_v
v·E(v*·x) on the 16 matrix units (basis; linearity cited). -/
theorem quasibasis_reconstruction :
    ∀ a b : Fin 4,
      (quasibasis.map fun v => v * Efix (adj v * Eu a b)).sum
        = Eu a b := by decide

/-- **THE WATATANI INDEX** (probe QB: `ind_dev`, headline): Σ_v v·v*
= 4·1 EXACTLY — Index E = 4 = |μ4| on the smallest exact instance
of the CAR-ladder expectation. -/
theorem watatani_index_four :
    (quasibasis.map fun v => v * adj v).sum = (4 : Zi) • 1 := by decide

/-- The ramified-place reading (GNET.RAMIFIED.01 candidate): the
index equals the square of the ℤ[i]-norm of the ramified prime
(1 + i): 4 = N(1+i)². -/
theorem index_eq_ramified_norm_sq : ((⟨1, 1⟩ : Zi).norm) ^ 2 = 4 := by
  decide

/-! ### W3. The Pimsner-Popa constant shadow (over ℚ) -/

/-- Rational sector projections (the pinching is real). -/
def PsecQ : Fin 4 → Matrix (Fin 4) (Fin 4) ℚ := fun q =>
  Matrix.of fun a b => if a = q ∧ b = q then 1 else 0

/-- The rational pinching expectation. -/
def EfixQ (x : Matrix (Fin 4) (Fin 4) ℚ) : Matrix (Fin 4) (Fin 4) ℚ :=
  ∑ q, PsecQ q * x * PsecQ q

/-- The probe's mixing minimizer, as a matrix: J = all-ones = 4·|v⟩⟨v|
for the equal-weight unit vector v across the four sectors. -/
def Jmix : Matrix (Fin 4) (Fin 4) ℚ := Matrix.of fun _ _ => 1

/-- E(J) = 1: the pinching of the mixing matrix is the identity. -/
theorem EfixQ_mixing : EfixQ Jmix = 1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [EfixQ, PsecQ, Jmix, Matrix.sum_apply, Matrix.mul_apply,
      Fin.sum_univ_four, Matrix.of_apply, Finset.filter_eq']

/-- The K₄ Laplacian. -/
def Lap4 : Matrix (Fin 4) (Fin 4) ℚ :=
  Matrix.of fun a b => if a = b then 3 else -1

/-- 4·E(J) − J is the K₄ Laplacian (the PP pencil at λ = ¼,
denominators cleared). -/
theorem pp_pencil_is_laplacian : (4 : ℚ) • EfixQ Jmix - Jmix = Lap4 := by
  rw [EfixQ_mixing]
  ext a b
  fin_cases a <;> fin_cases b <;>
    norm_num [Jmix, Lap4, Matrix.sub_apply, Matrix.smul_apply,
      Matrix.one_apply, Matrix.of_apply]

/-- **SOS certificate** (PP at λ = ¼): xᵀ(4·E(J) − J)x =
Σ_{a<b}(x_a − x_b)² — a sum of six squares, so E(J) − ¼·J ⪰ 0. -/
theorem pp_pencil_sos (v : Fin 4 → ℚ) :
    ∑ j, ∑ k, v j * ((4 : ℚ) • EfixQ Jmix - Jmix) j k * v k
      = (v 0 - v 1) ^ 2 + (v 0 - v 2) ^ 2 + (v 0 - v 3) ^ 2
        + (v 1 - v 2) ^ 2 + (v 1 - v 3) ^ 2 + (v 2 - v 3) ^ 2 := by
  rw [pp_pencil_is_laplacian]
  simp [Fin.sum_univ_four, Lap4, Matrix.of_apply]
  ring

/-- PP holds at λ = ¼: the pencil quadratic form is nonnegative. -/
theorem pp_bound_at_quarter (v : Fin 4 → ℚ) :
    0 ≤ ∑ j, ∑ k, v j * ((4 : ℚ) • EfixQ Jmix - Jmix) j k * v k := by
  rw [pp_pencil_sos v]
  positivity

/-- The equal-weight mixing vector (the probe's explicit minimizer,
unnormalized). -/
def onesQ : Fin 4 → ℚ := fun _ => 1

/-- Pencil value at the mixing vector: vᵀ(E(J) − λ·J)v = 4 − 16λ. -/
theorem pp_pencil_at_mixing (lam : ℚ) :
    ∑ j, ∑ k, onesQ j * (EfixQ Jmix - lam • Jmix) j k * onesQ k
      = 4 - 16 * lam := by
  rw [EfixQ_mixing]
  simp [Jmix, onesQ, Matrix.sub_apply, Matrix.one_apply, Matrix.of_apply]
  ring

/-- **Sharpness** (probe `lam_star == 1/4`): every λ > ¼ fails on the
mixing vector — together with `pp_bound_at_quarter`, the optimal PP
constant of the model expectation is EXACTLY ¼ = 1/|μ4|. -/
theorem pp_constant_sharp (lam : ℚ) (hl : 1 / 4 < lam) :
    ∑ j, ∑ k, onesQ j * (EfixQ Jmix - lam • Jmix) j k * onesQ k < 0 := by
  rw [pp_pencil_at_mixing lam]
  linarith

/-! ### W4. Controls: index = #sectors (μ2 and the k = 1 anomaly) -/

/-- Matrix units on M₂. -/
def Eu2 (a b : Fin 2) : Matrix (Fin 2) (Fin 2) Zi :=
  Matrix.of fun j k => if j = a ∧ k = b then 1 else 0

/-- The μ2 pinching expectation on M₂ (two one-dimensional sectors). -/
def Efix2 (x : Matrix (Fin 2) (Fin 2) Zi) : Matrix (Fin 2) (Fin 2) Zi :=
  ∑ q, Eu2 q q * x * Eu2 q q

/-- The 3-element μ2 quasi-basis. -/
def quasibasis2 : List (Matrix (Fin 2) (Fin 2) Zi) :=
  [1, Eu2 0 1, Eu2 1 0]

/-- **μ2 control** (probe `lam_z2`, `Z2-only average gives Ind = 2`):
the two-sector model has Watatani index 2, with reconstruction — the
certificate separates μ4 from μ2. -/
theorem watatani_index_two :
    (quasibasis2.map fun v => v * adj v).sum = (2 : Zi) • 1 ∧
    ∀ a b : Fin 2,
      (quasibasis2.map fun v => v * Efix2 (adj v * Eu2 a b)).sum
        = Eu2 a b := by decide

/-- Matrix units on M₃. -/
def Eu3 (a b : Fin 3) : Matrix (Fin 3) (Fin 3) Zi :=
  Matrix.of fun j k => if j = a ∧ k = b then 1 else 0

/-- The three-sector pinching expectation on M₃. -/
def Efix3 (x : Matrix (Fin 3) (Fin 3) Zi) : Matrix (Fin 3) (Fin 3) Zi :=
  ∑ q, Eu3 q q * x * Eu3 q q

/-- The 7-element three-sector quasi-basis. -/
def quasibasis3 : List (Matrix (Fin 3) (Fin 3) Zi) :=
  [1, Eu3 0 1, Eu3 0 2, Eu3 1 0, Eu3 1 2, Eu3 2 0, Eu3 2 1]

/-- **k = 1 anomaly control** (probe `W k=1 boundary anomaly: only 3
sectors, Ind = 3`): the three-sector model has Watatani index 3, with
reconstruction — index = #sectors, so the smallest window cannot see
|μ4| = 4. -/
theorem watatani_index_three :
    (quasibasis3.map fun v => v * adj v).sum = (3 : Zi) • 1 ∧
    ∀ a b : Fin 3,
      (quasibasis3.map fun v => v * Efix3 (adj v * Eu3 a b)).sum
        = Eu3 a b := by decide

/-! ### W5. The dual character picture: ℂ·1 ⊂ C(ℤ/4) -/

/-- **Character orthogonality on ℤ/4** = the Watatani identities of
the DUAL inclusion ℂ·1 ⊂ C(ℤ/4) (E = Haar average, quasi-basis = the
four characters): Σ_k χ_k(a)·conj(χ_k(b)) = 4·δ_{ab}.  The diagonal
a = b is Σ_k v_k v_k* = 4·1 (index 4 again); the full identity is the
Fourier reconstruction x = Σ_k χ_k·E(χ_k*·x) on the delta basis —
the crossed-product dual of the same μ4 datum. -/
theorem character_orthogonality :
    ∀ a b : Fin 4,
      (∑ k, chi k a * gconj (chi k b)) = if a = b then 4 else 0 := by
  decide

/-- The characters are exactly the U-eigenvalue lists: U^j has
diagonal entry χ_a(j) at position a (the grading and the character
table are the same datum). -/
theorem Upow_diag_eq_chi : ∀ j a : Fin 4, Upow j a a = chi a j := by
  decide

end TfptCarrier.WatataniIndexFour
