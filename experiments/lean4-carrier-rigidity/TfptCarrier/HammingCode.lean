/-
  HammingCode — the extended [8,4,4] Hamming code as F₂ structure.
  =================================================================

  The self-dual extended Hamming code (= Reed–Muller RM(1,3)) is the
  code layer of the TFPT self-code rounds (v626/v638 context: the
  E8/code semantics audits).  This module certifies its finite
  structure by kernel `decide` on the explicit 16 codewords:

    (a) SELF-DUALITY: every pair of codewords is orthogonal under the
        F₂ dot product (in particular the code is self-orthogonal of
        dimension 4 = 8/2, hence self-dual);
    (b) WEIGHT DISTRIBUTION: {0:1, 4:14, 8:1} — the weight enumerator
        of the unique [8,4,4] self-dual code with all weights ≡ 0
        mod 4 (doubly-even);
    (c) COSET-LEADER WEIGHT DISTRIBUTION: {0:1, 1:8, 2:7} — the 16
        explicit leaders have pairwise distinct syndromes (so all 16
        syndromes occur), carry weights 0/1/2 with multiplicities
        1/8/7, and each is of MINIMAL weight in its coset ℓ + code
        (covering radius 2).

  Also certified: closure under addition and 0 ∈ code (so `code` is a
  subgroup and ℓ + code is genuinely the coset of ℓ), syndrome 0 on
  every codeword, and Nodup/cardinality 16 = 2⁴.

  All data are explicit witnesses (leaders precomputed by exhaustive
  search over F₂⁸); every statement quantifies only over the explicit
  16-element lists, so `decide` stays cheap (no 256-element pi-type
  enumeration is needed).
-/
import Mathlib.Tactic
import Mathlib.Data.ZMod.Basic
import Mathlib.LinearAlgebra.Matrix.Notation

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.HammingCode

/-- F₂⁸, the ambient space of the extended Hamming code. -/
abbrev V8 := Fin 8 → ZMod 2

/-- The 16 codewords of the extended [8,4,4] Hamming code
(= RM(1,3), spanned by 11111111, 01010101, 00110011, 00001111). -/
def code : List V8 :=
  [![0,0,0,0,0,0,0,0],
   ![0,0,0,0,1,1,1,1],
   ![0,0,1,1,0,0,1,1],
   ![0,0,1,1,1,1,0,0],
   ![0,1,0,1,0,1,0,1],
   ![0,1,0,1,1,0,1,0],
   ![0,1,1,0,0,1,1,0],
   ![0,1,1,0,1,0,0,1],
   ![1,0,0,1,0,1,1,0],
   ![1,0,0,1,1,0,0,1],
   ![1,0,1,0,0,1,0,1],
   ![1,0,1,0,1,0,1,0],
   ![1,1,0,0,0,0,1,1],
   ![1,1,0,0,1,1,0,0],
   ![1,1,1,1,0,0,0,0],
   ![1,1,1,1,1,1,1,1]]

/-- The F₂ dot product on F₂⁸. -/
def dot (u v : V8) : ZMod 2 := ∑ i, u i * v i

/-- Hamming weight. -/
def wt (v : V8) : ℕ := (Finset.univ.filter fun i => v i ≠ 0).card

/-- The parity-check matrix rows = the generator rows (self-dual code). -/
def H : Fin 4 → V8 :=
  ![![1,1,1,1,1,1,1,1],
    ![0,1,0,1,0,1,0,1],
    ![0,0,1,1,0,0,1,1],
    ![0,0,0,0,1,1,1,1]]

/-- The syndrome map F₂⁸ → F₂⁴. -/
def syndrome (v : V8) : Fin 4 → ZMod 2 := fun j => dot (H j) v

/-- 16 = 2⁴ distinct codewords. -/
theorem code_card : code.length = 16 ∧ code.Nodup := by decide

/-- The zero word is a codeword and the code is closed under addition:
`code` is an F₂-subgroup (hence `ℓ + code` below is genuinely the
coset of ℓ). -/
theorem code_subgroup :
    (fun _ => 0 : V8) ∈ code ∧ ∀ u ∈ code, ∀ v ∈ code, u + v ∈ code := by
  decide

/-- **(a) Self-duality**: every pair of codewords is orthogonal. -/
theorem code_self_dual : ∀ u ∈ code, ∀ v ∈ code, dot u v = 0 := by decide

/-- Every codeword has syndrome 0. -/
theorem code_syndrome_zero : ∀ c ∈ code, syndrome c = 0 := by decide

/-- **(b) The weight distribution** {0:1, 4:14, 8:1}: doubly-even,
minimum distance 4. -/
theorem code_weight_distribution :
    (code.countP fun v => wt v = 0) = 1 ∧
    (code.countP fun v => wt v = 4) = 14 ∧
    (code.countP fun v => wt v = 8) = 1 := by decide

/-- The 16 coset leaders (one per syndrome, precomputed minimal). -/
def leaders : List V8 :=
  [![0,0,0,0,0,0,0,0],
   ![0,0,0,1,0,0,0,1],
   ![0,0,0,0,0,1,0,1],
   ![0,0,0,1,0,1,0,0],
   ![0,0,0,0,0,0,1,1],
   ![0,0,0,1,0,0,1,0],
   ![0,0,0,0,0,1,1,0],
   ![0,0,0,1,1,0,0,0],
   ![1,0,0,0,0,0,0,0],
   ![0,0,0,0,1,0,0,0],
   ![0,0,1,0,0,0,0,0],
   ![0,0,0,0,0,0,1,0],
   ![0,1,0,0,0,0,0,0],
   ![0,0,0,0,0,1,0,0],
   ![0,0,0,1,0,0,0,0],
   ![0,0,0,0,0,0,0,1]]

/-- The 16 leaders hit all 16 syndromes (pairwise distinct syndromes
in a 16-element syndrome space). -/
theorem leaders_syndromes_complete :
    (leaders.map syndrome).Nodup ∧ leaders.length = 16 := by decide

/-- Stronger, direct form: EVERY syndrome is realized by a leader. -/
theorem leaders_syndromes_surjective :
    ∀ s : Fin 4 → ZMod 2, s ∈ leaders.map syndrome := by decide

/-- **(c) The coset-leader weight distribution** {0:1, 1:8, 2:7}. -/
theorem leaders_weight_distribution :
    (leaders.countP fun v => wt v = 0) = 1 ∧
    (leaders.countP fun v => wt v = 1) = 8 ∧
    (leaders.countP fun v => wt v = 2) = 7 := by decide

/-- **(c) Minimality**: each leader has minimal weight in its coset
`ℓ + code` — no coset element is lighter (covering radius 2, since all
leader weights are ≤ 2). -/
theorem leaders_minimal :
    ∀ l ∈ leaders, ∀ c ∈ code, wt l ≤ wt (l + c) := by decide

end TfptCarrier.HammingCode
