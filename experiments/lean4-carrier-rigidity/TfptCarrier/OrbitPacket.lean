/-
  OrbitPacket — the Gaussian orbit packet lemma on L/(1+i)L ≅ F₂⁴.
  ==================================================================

  Machine-checked core of the review contract
  E8.GAUSSCODE.ORBIT_PACKET.01, on top of the proven Gaussian code
  bridge (`GaussianCodeBridge`: L/(1+i)L ≅ F₂⁴ via the Smith
  certificate, 240 roots = 15 nonzero classes × 16 with the label
  list `labelData`, σ acting on labels as the explicit matrix `Msig`)
  and the code layer (`HammingCode`: the equivariant [8,4,4]
  placement C* with its 16 coset leaders).  Numeric counterpart:
  experiments/tfpt-discovery/orbit_packet_probe.py (26/26, verdict
  ORBIT-PACKET-EXACT).

  Certified here, kernel `decide` / `norm_num` only (no sorry, no
  native_decide):

  B (Burnside orbit count):
    * fixed-point counts of ⟨σ⟩ on the 15 nonzero labels:
      |Fix id| = 15, |Fix σ| = 3, |Fix σ²| = 3; Burnside
      (15+3+3)/3 = 7; the DIRECT orbit count is 7 = 3 singleton
      orbits + 4 three-cycles — the scalaron count 7 as an orbit
      count, agreeing with the previous reading 7 = 4 + 3.

  P (the canonical packet partition 240 = 5 × 48):
    * five explicit label blocks — the σ-fixed block Bfix (3 labels)
      and the four σ-orbits O1–O4 (3 labels each) — cover the 15
      nonzero labels disjointly; Bfix is EXACTLY the set of nonzero
      σ-fixed labels and each Oi is a genuine σ-orbit (canonicity:
      the partition is forced by σ; only the ordering of O1–O4 is
      conventional); on the 240-root label list each block carries
      EXACTLY 48 roots: 240 = 5 · 48, and g_car = 1 + 4 = 5.
      (That each 48-block is a union of 12 Gaussian lines is the
      probe's job — here μ4-stability of labels is already certified
      in `GaussianCodeBridge.census_mu4_stable`.)

  A (the anchor weights from the fixed syndromes):
    * σ = πσ acts on the cosets of C* (σ-fixedness of a coset is
      well defined on representatives); of the 16 coset leaders
      EXACTLY 4 lie in σ-fixed cosets; their leader weights are
      (0, 1, 1, 2); the two weight-1 fixed cosets are led by e₆ and
      e₇ — the v638 anchor pair {6,7}; the nontrivial weight vector
      a = (1,1,2) has elementary symmetric functions e₁ = 4, e₂ = 5,
      e₃ = 2.

  Q (the q-normal form, documented arithmetic):
    * q = |F₂⁴| = 16 (the order of the CANONICAL quotient
      L/(1+i)L): 240 = q(q−1) and 248 = q(q−1) + 2·log₂ q.

  F (σ-class specificity, the must-fail witness):
    * an explicit fixed-point-free order-3 matrix on F₂⁴ (companion
      of x²+x+1, twice) has orbit census 5 × {three-cycle}:
      Burnside (15+0+0)/3 = 5 ≠ 7 and packet count 1 + 5 = 6 ≠ 5 —
      order 3 ALONE does not imply the 1 + 4 packet law (the probe
      shows the free class is REALIZED inside G31: 160 of the 800
      order-3 elements).

  CIRCULARITY FENCE (prominent, review honesty).  The code C*, the
  lattice L, the complex structure J and the clock σ are all built
  FROM E8 (v626/v634/v638/v689).  The theorems
  `c3_coefficient_reconstruction` and `gCar_reconstruction` below
  read c₃ = 1/(2π·dim V) = 1/(8π) and g_car = 1 + #moved orbits = 5
  back out of the quotient — they are EXACT INTERNAL RECONSTRUCTIONS
  (consistency identities of the E8 compiler), NOT independent
  derivations of the axioms P1/P2.  A non-circular derivation would
  have to construct the code/quotient directly from the boundary
  datum (seam/horizon data) without E8 input.  Until that exists the
  correct type is RECONSTRUCTION, not DERIVATION.

  HONEST SCOPE.  The syndrome space F₂⁸/C* (part A) and the Gaussian
  quotient L/(1+i)L (parts B/P) are DIFFERENT F₂⁴'s; both carry σ
  with a 2-dimensional fixed space, but no canonical identification
  between them is claimed or formalized.  The identification of the
  elementary symmetric values (4, 5, 2) with |μ₄|, g_car, N(1+i) is
  the review's interpretation, recorded in the probe, not a theorem.

  Machine counterpart: experiments/tfpt-discovery/
  orbit_packet_probe.py (26/26, ORBIT-PACKET-EXACT).
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic
import TfptCarrier.HammingCode
import TfptCarrier.GaussianCodeBridge

set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

namespace TfptCarrier.OrbitPacket

open TfptCarrier.HammingCode TfptCarrier.GaussianCodeBridge

/-! ### 0. The label space V = L/(1+i)L ≅ F₂⁴ and the σ-action -/

/-- The label space V ≅ F₂⁴ (SNF residue labels of `GaussianCodeBridge`). -/
abbrev Label := Fin 4 → ZMod 2

/-- σ on labels: the row action l ↦ l·Mσ (`GaussianCodeBridge.Msig`,
certified there by the transport C_σ·Q = Q·R). -/
def sigL (l : Label) : Label := rowMul4 l Msig

/-- The 15 nonzero labels (the classes hit by the 240 roots). -/
def nonzeroLabels : Finset Label := Finset.univ.filter (· ≠ 0)

/-- The ⟨σ⟩-orbit of a label (σ³ = 1, so three steps suffice). -/
def orbitOf (l : Label) : Finset Label := {l, sigL l, sigL (sigL l)}

/-! ### 1. B — the Burnside orbit count: (15 + 3 + 3)/3 = 7 -/

/-- |Fix id| = 15 on V \ {0}. -/
theorem fix_id_card : nonzeroLabels.card = 15 := by decide

/-- |Fix σ| = 3 on V \ {0}. -/
theorem fix_sigma_card :
    (nonzeroLabels.filter fun l => sigL l = l).card = 3 := by decide

/-- |Fix σ²| = 3 on V \ {0}. -/
theorem fix_sigma_sq_card :
    (nonzeroLabels.filter fun l => sigL (sigL l) = l).card = 3 := by decide

/-- Burnside arithmetic: N_orbit = (15 + 3 + 3)/3 = 7. -/
theorem burnside_arithmetic : (15 + 3 + 3) / 3 = 7 := by norm_num

/-- **The direct orbit count is 7** — the scalaron count as an orbit
count on the nonzero Gaussian classes. -/
theorem orbit_count : (nonzeroLabels.image orbitOf).card = 7 := by decide

/-- 3 of the 7 orbits are singletons (σ-fixed classes). -/
theorem fixed_orbit_count :
    ((nonzeroLabels.image orbitOf).filter fun o => o.card = 1).card = 3 := by
  decide

/-- 4 of the 7 orbits are three-cycles (moved families). -/
theorem moved_orbit_count :
    ((nonzeroLabels.image orbitOf).filter fun o => o.card = 3).card = 4 := by
  decide

/-- Every orbit is a singleton or a three-cycle (σ³ = 1, no 2-orbits;
element-level form): a nonzero label is either σ-fixed or its three
σ-iterates are pairwise distinct — so the two readings
7 = (15+3+3)/3 and 7 = 3 + 4 agree. -/
theorem orbit_sizes_exhaustive :
    ∀ l : Label, l ≠ 0 →
      (sigL l = l ∨
        (sigL l ≠ l ∧ sigL (sigL l) ≠ l ∧ sigL (sigL l) ≠ sigL l)) := by
  decide

/-! ### 2. P — the canonical packet partition 240 = 5 × 48 -/

/-- The σ-fixed packet: the 3 nonzero σ-fixed labels (the anchor
label, the coordinate-class label F1+F2+F3, and their sum). -/
def Bfix : List Label := [![1, 0, 0, 0], ![0, 0, 0, 1], ![1, 0, 0, 1]]

/-- Moved packet 1: the family orbit {F1, F2, F3}. -/
def O1 : List Label := [![0, 0, 1, 0], ![0, 1, 0, 1], ![0, 1, 1, 0]]

/-- Moved packet 2. -/
def O2 : List Label := [![0, 1, 0, 0], ![0, 1, 1, 1], ![0, 0, 1, 1]]

/-- Moved packet 3 (= anchor + O1). -/
def O3 : List Label := [![1, 0, 1, 0], ![1, 1, 0, 1], ![1, 1, 1, 0]]

/-- Moved packet 4 (= anchor + O2). -/
def O4 : List Label := [![1, 1, 0, 0], ![1, 1, 1, 1], ![1, 0, 1, 1]]

/-- The five blocks cover every nonzero label. -/
theorem blocks_cover :
    ∀ l : Label, l ≠ 0 →
      (l ∈ Bfix ∨ l ∈ O1 ∨ l ∈ O2 ∨ l ∈ O3 ∨ l ∈ O4) := by decide

/-- The five blocks are pairwise disjoint (15 distinct labels in
total): together with `blocks_cover` this is a PARTITION of V \ {0}. -/
theorem blocks_disjoint :
    (Bfix ++ O1 ++ O2 ++ O3 ++ O4).Nodup ∧
    (Bfix ++ O1 ++ O2 ++ O3 ++ O4).length = 15 := by decide

/-- **Canonicity of the fixed packet**: Bfix is EXACTLY the set of
nonzero σ-fixed labels — no choice enters. -/
theorem fix_block_canonical :
    ∀ l : Label, (l ∈ Bfix ↔ (l ≠ 0 ∧ sigL l = l)) := by decide

/-- **Canonicity of the moved packets**: each Oi is a genuine σ-orbit
(the orbit of each of its members is the block itself); the only
residual freedom in the partition is the ORDERING of O1–O4. -/
theorem moved_blocks_canonical :
    (∀ l ∈ O1, orbitOf l = ({![0, 0, 1, 0], ![0, 1, 0, 1], ![0, 1, 1, 0]} :
        Finset Label)) ∧
    (∀ l ∈ O2, orbitOf l = ({![0, 1, 0, 0], ![0, 1, 1, 1], ![0, 0, 1, 1]} :
        Finset Label)) ∧
    (∀ l ∈ O3, orbitOf l = ({![1, 0, 1, 0], ![1, 1, 0, 1], ![1, 1, 1, 0]} :
        Finset Label)) ∧
    (∀ l ∈ O4, orbitOf l = ({![1, 1, 0, 0], ![1, 1, 1, 1], ![1, 0, 1, 1]} :
        Finset Label)) := by decide

/-- The first moved packet is the family orbit of the bridge:
O1 = [F1, F2, F3] verbatim. -/
theorem O1_is_family_orbit : O1 = [F1, F2, F3] := by decide

/-- The fixed packet in bridge coordinates: the anchor label, the
coordinate-class label F1+F2+F3 (`coord_class_eq_family_sum`), and
their sum. -/
theorem Bfix_contents :
    Bfix = [anchor, F1 + F2 + F3, anchor + (F1 + F2 + F3)] := by decide

set_option maxHeartbeats 12000000 in
/-- **The packet counts on the 240 roots**: each of the five blocks
carries EXACTLY 48 of the 240 root labels — 240 = 5 × 48. -/
theorem packet_counts :
    labelData.countP (· ∈ Bfix) = 48 ∧
    labelData.countP (· ∈ O1) = 48 ∧
    labelData.countP (· ∈ O2) = 48 ∧
    labelData.countP (· ∈ O3) = 48 ∧
    labelData.countP (· ∈ O4) = 48 := by decide

/-- The packet arithmetic: 5 · 48 = 240 = |R(E8)| (the label list has
length 240 by `GaussianCodeBridge.labelData_length`). -/
theorem packet_partition_240 : 5 * 48 = 240 := by norm_num

/-! ### 3. g_car = 1 + 4 (the P2 reconstruction, typed) -/

/-- **P2 reconstruction** (EXACT INTERNAL RECONSTRUCTION, NOT a
derivation — see the circularity fence in the module docstring):
g_car = 1 (σ-fixed packet) + #moved orbits = 1 + 4 = 5, tied to the
certified orbit census. -/
theorem gCar_reconstruction :
    1 + ((nonzeroLabels.image orbitOf).filter fun o => o.card = 3).card
      = 5 := by decide

/-- The packet reading of g_car: 5 packets × 48 roots = 240. -/
theorem gCar_packet_reading : (1 + 4) * 48 = 240 := by norm_num

/-! ### 4. A — the anchor weights (0,1,1,2) from the fixed syndromes -/

/-- σ on F₂⁸: the pair 3-cycle πσ (coordinates: new k = old (πσ k)),
exactly the permutation under which C* is invariant
(`GaussianCodeBridge.code_piSig_invariant`). -/
def sigV8 (x : V8) : V8 := fun k => x (piSig k)

/-- σ-fixedness of the coset x + C*: σx − x ∈ C* (over F₂, − = +). -/
def cosetFixed (x : V8) : Prop := (sigV8 x + x) ∈ code

instance : DecidablePred cosetFixed := fun x =>
  inferInstanceAs (Decidable ((sigV8 x + x) ∈ code))

set_option maxHeartbeats 12000000 in
/-- σ-fixedness is well defined on cosets: it does not depend on the
chosen representative of ℓ + C*. -/
theorem cosetFixed_well_defined :
    ∀ l ∈ leaders, ∀ c ∈ code, (cosetFixed (l + c) ↔ cosetFixed l) := by
  decide

/-- **Exactly 4 of the 16 cosets are σ-fixed** (the leaders enumerate
all 16 cosets: `HammingCode.leaders_syndromes_complete`). -/
theorem fixed_coset_count :
    (leaders.countP fun l => cosetFixed l) = 4 := by decide

/-- **The anchor weight lemma**: the coset-leader weights of the four
σ-fixed cosets are (0, 1, 1, 2) — in the leader-list order the
weights read [0, 2, 1, 1] (leaders are coset-minimal by
`HammingCode.leaders_minimal`). -/
theorem anchor_weights :
    ((leaders.filter fun l => cosetFixed l).map wt) = [0, 2, 1, 1] := by
  decide

/-- The multiset form: weight 0 once, weight 1 twice, weight 2 once. -/
theorem anchor_weights_multiset :
    ((leaders.filter fun l => cosetFixed l).countP fun l => wt l = 0) = 1 ∧
    ((leaders.filter fun l => cosetFixed l).countP fun l => wt l = 1) = 2 ∧
    ((leaders.filter fun l => cosetFixed l).countP fun l => wt l = 2) = 1 := by
  decide

/-- The two weight-1 fixed cosets are led by e₆ and e₇ — the v638
anchor pair {6,7} — and the weight-2 fixed coset by e₆ + e₇. -/
theorem anchor_pair_leaders :
    (![0, 0, 0, 0, 0, 0, 1, 0] : V8) ∈
      (leaders.filter fun l => cosetFixed l) ∧
    (![0, 0, 0, 0, 0, 0, 0, 1] : V8) ∈
      (leaders.filter fun l => cosetFixed l) ∧
    (![0, 0, 0, 0, 0, 0, 1, 1] : V8) ∈
      (leaders.filter fun l => cosetFixed l) := by decide

/-- The nontrivial anchor weight vector a = (1, 1, 2): elementary
symmetric functions e₁ = 4, e₂ = 5, e₃ = 2 (the review reads these as
|μ₄|, g_car, N(1+i) — an interpretation, not a theorem; see the
module docstring). -/
theorem anchor_elementary_symmetric :
    (1 + 1 + 2 = 4) ∧ (1 * 1 + 1 * 2 + 2 * 1 = 5) ∧ (1 * 1 * 2 = 2) := by
  norm_num

/-! ### 5. Q — the q-normal form (documented arithmetic) -/

/-- q = 16 is the order of the CANONICAL quotient L/(1+i)L ≅ F₂⁴ (not
a fitted parameter). -/
theorem q_is_quotient_order : Fintype.card Label = 16 := by decide

/-- |R(E8)| = q(q − 1) = 16 · 15 = 240. -/
theorem q_normal_roots : 16 * 15 = 240 := by norm_num

/-- log₂ q = 4 exactly (q = 2⁴). -/
theorem q_log_two : 2 ^ 4 = 16 := by norm_num

/-- dim E8 = q(q − 1) + 2·log₂ q = 240 + 8 = 248. -/
theorem q_normal_dim : 16 * 15 + 2 * 4 = 248 := by norm_num

/-! ### 6. The P1 reconstruction (typed, with fence) -/

/-- **P1 reconstruction** (EXACT INTERNAL RECONSTRUCTION, NOT a
derivation — see the circularity fence in the module docstring): the
rational coefficient of c₃ = 1/(2π·dim V) with dim V = 4 = rank_F₂ of
the quotient: 1/(2·4) = 1/8, i.e. c₃ = 1/(8π). -/
theorem c3_coefficient_reconstruction : (1 : ℚ) / (2 * 4) = 1 / 8 := by
  norm_num

/-- dim V = 4 ties to the quotient order: 2⁴ = |V|. -/
theorem c3_dim_ties_to_quotient : 2 ^ 4 = Fintype.card Label := by decide

/-! ### 7. F — σ-class specificity (the must-fail witness) -/

/-- A fixed-point-free order-3 matrix on F₂⁴: the companion matrix of
x² + x + 1, twice (the OTHER order-3 class of GL(4, F₂); the probe
shows this class is realized by 160 of the 800 order-3 elements of
G31). -/
def Mfree : Matrix (Fin 4) (Fin 4) (ZMod 2) :=
  !![0, 1, 0, 0;
     1, 1, 0, 0;
     0, 0, 0, 1;
     0, 0, 1, 1]

/-- Mfree has order 3. -/
theorem Mfree_cubed : Mfree * Mfree * Mfree = 1 := by decide

/-- Mfree is fixed-point FREE on V \ {0}. -/
theorem Mfree_fixed_point_free :
    ∀ l : Label, rowMul4 l Mfree = l → l = 0 := by decide

/-- **The must-fail census**: the free class has FIVE orbits on
V \ {0} (all three-cycles) — Burnside (15+0+0)/3 = 5 ≠ 7 and a packet
reading 1 + 5 = 6 ≠ 5 = g_car: the 3-fixed + 4-moved packet law is
σ-CLASS-specific (it needs the 2-dimensional fixed space of
σ = c⁴), NOT an order-3 tautology. -/
theorem Mfree_orbit_count :
    (nonzeroLabels.image fun l =>
      ({l, rowMul4 l Mfree, rowMul4 (rowMul4 l Mfree) Mfree} :
        Finset Label)).card = 5 := by decide

/-- Burnside arithmetic for the free class: (15 + 0 + 0)/3 = 5 ≠ 7. -/
theorem burnside_free_class : (15 + 0 + 0) / 3 = 5 ∧ (5 : ℕ) ≠ 7 := by
  norm_num

end TfptCarrier.OrbitPacket
