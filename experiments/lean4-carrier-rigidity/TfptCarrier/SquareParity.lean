/-
  SquareParity — the parity obstruction of the c = w² kill, certified.
  ====================================================================

  Today's ST31 round asked whether the compiler clock c (order 12,
  root census 19 × 12 + 3 × 4 on the 240 E8 roots, v629 R2 / v634)
  is the SQUARE of an order-24 word w.  The kill is a parity fact
  about cycle types:

    a cycle of ρ of ODD length n squares to one n-cycle; a cycle of
    EVEN length 2m squares to TWO m-cycles (and a 2-cycle dissolves
    into fixed points) — so for every EVEN length L, the L-cycles of
    ρ² arise ONLY from the 2L-cycles of ρ, two per cycle:

        #{L-cycles of ρ²} = 2 · #{2L-cycles of ρ}   (L even).

  The census 19 × 12 + 3 × 4 has NINETEEN 12-cycles — odd — so it
  cannot be the cycle type of any square.

  HONEST SCOPE.  This module formalizes the COMBINATORIAL KERNEL of
  the kill at the multiset level: `squareCycleType` is the cycle-type
  transport of squaring (odd k ↦ {k}; even k ↦ {k/2, k/2}; 2 ↦ ∅),
  and we prove the exact count law `count_squareCycleType`, the parity
  corollary, and the census application `census_not_square`.  The
  permutation-level bridge — cycleType (ρ²) = squareCycleType
  (cycleType ρ) for ρ : Equiv.Perm α — is NOT formalized here: Mathlib
  currently has no cycleType-of-power API, and the even-cycle
  splitting lemma would be a substantial standalone development.  The
  240-point instance is far beyond kernel `decide`.  The multiset law
  below is exactly the arithmetic the v647-context kill consumes.

  Machine counterpart: experiments/tfpt-discovery/st31_degree24_probe.py
  (S2, the full order-24 power scan) in the v634 context.
-/
import Mathlib.Tactic
import Mathlib.Data.Multiset.Bind
import Mathlib.Data.Multiset.Replicate

namespace TfptCarrier.SquareParity

/-- The square of one cycle, at cycle-type level: an odd k-cycle stays
one k-cycle; an even 2m-cycle splits into two m-cycles; a 2-cycle
dissolves into fixed points (which cycle types do not record). -/
def squareTerm (k : ℕ) : Multiset ℕ :=
  if Even k then (if k = 2 then 0 else {k / 2, k / 2}) else {k}

/-- The cycle type of ρ², computed from the cycle type of ρ. -/
def squareCycleType (M : Multiset ℕ) : Multiset ℕ :=
  M.bind squareTerm

theorem squareCycleType_cons (k : ℕ) (M : Multiset ℕ) :
    squareCycleType (k ::ₘ M) = squareTerm k + squareCycleType M := by
  simp [squareCycleType, Multiset.cons_bind]

/-- Per-cycle count law: for EVEN L, one k-cycle contributes L-cycles
to the square only when k = 2L — and then exactly two of them. -/
theorem count_squareTerm {L : ℕ} (hL : Even L) (k : ℕ) :
    (squareTerm k).count L = 2 * (if 2 * L = k then 1 else 0) := by
  have hL2 : L % 2 = 0 := Nat.even_iff.mp hL
  unfold squareTerm
  rcases Nat.even_or_odd k with hk | hk
  · have hk2 : k % 2 = 0 := Nat.even_iff.mp hk
    rw [if_pos hk]
    by_cases h2 : k = 2
    · subst h2
      have hne : 2 * L ≠ 2 := by omega
      simp [hne]
    · rw [if_neg h2]
      by_cases hLk : 2 * L = k
      · rw [if_pos hLk]
        have hhalf : L = k / 2 := by omega
        subst hhalf
        simp [Multiset.insert_eq_cons]
      · rw [if_neg hLk]
        have hhalf : L ≠ k / 2 := by omega
        simp [Multiset.insert_eq_cons, hhalf]
  · have hk2 : k % 2 = 1 := Nat.odd_iff.mp hk
    have hnev : ¬ Even k := by rw [Nat.even_iff]; omega
    rw [if_neg hnev]
    have h1 : L ≠ k := by omega
    have h2 : 2 * L ≠ k := by omega
    simp [h1, h2]

/-- **The pairing law**: for every EVEN length L, the L-cycles of the
square arise only from 2L-cycles, two per cycle:
`count L (squareCycleType M) = 2 · count 2L M`. -/
theorem count_squareCycleType (M : Multiset ℕ) {L : ℕ} (hL : Even L) :
    (squareCycleType M).count L = 2 * M.count (2 * L) := by
  induction M using Multiset.induction_on with
  | empty => simp [squareCycleType]
  | cons k M ih =>
      rw [squareCycleType_cons, Multiset.count_add, ih,
        count_squareTerm hL k, Multiset.count_cons]
      ring

/-- **The parity theorem**: in the cycle type of a square, every even
length occurs an EVEN number of times. -/
theorem even_count_even_length (M : Multiset ℕ) {L : ℕ} (hL : Even L) :
    Even ((squareCycleType M).count L) := by
  rw [count_squareCycleType M hL]
  exact even_two_mul _

/-- **The obstruction**: a cycle type with an ODD number of cycles of
some EVEN length is not the square of any cycle type. -/
theorem ne_of_odd_even_count {T : Multiset ℕ} {L : ℕ} (hL : Even L)
    (hodd : ¬ Even (T.count L)) (M : Multiset ℕ) :
    squareCycleType M ≠ T := by
  intro h
  exact hodd (h ▸ even_count_even_length M hL)

/-- The v629/v634 root census of the compiler clock c on the 240 E8
roots: 19 twelve-cycles and 3 four-cycles. -/
def census : Multiset ℕ :=
  Multiset.replicate 19 12 + Multiset.replicate 3 4

theorem census_count_twelve : census.count 12 = 19 := by
  simp [census]

/-- **The c = w² kill**: the census 19 × 12 + 3 × 4 contains an ODD
number (19) of 12-cycles, so it is not the square of ANY cycle type —
in particular no order-24 word w on the 240 roots can satisfy c = w²
(the arithmetic kernel of the v647-context kill). -/
theorem census_not_square (M : Multiset ℕ) : squareCycleType M ≠ census :=
  ne_of_odd_even_count (L := 12) (by decide)
    (by rw [census_count_twelve]; decide) M

end TfptCarrier.SquareParity
