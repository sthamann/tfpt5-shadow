# The Floor and the Detector: A Measuring Device That Finds Zeros Without Knowing Them

*A field report on rounds 23 through 27 at the prime front (August 6–7, 2026): the big open inequality shrinks to a single ratio, its skeleton gets certified bone by bone, a positivity object turns out to be a zero-locating instrument — and the wall behind it all is surveyed three independent ways and given a name. Up front, as always: at the end of this article the Riemann Hypothesis is still unproven, and not a single number here claims otherwise.*

---

## Where we left off

The previous article in this series ended on August 3 with a question that had transformed twice: from "prove one inequality for all windows" via "find one geometric operator" to "explain one selection principle inside a finite corridor." Since then the verification suite has turned five more rounds (modules v814 through v836; the suite now stands at 829 modules and nearly 9,700 automated checks), and the question has transformed once more — this time into its most compact shape yet.

A reminder of the tool: the theory packs finite excerpts of the prime data into matrices ("window forms") that are provably discretizations of the classical Weil operator. Positivity of these forms, uniformly across all windows and depths, is a known reformulation of the Riemann Hypothesis. That is the wall. Everything below is work at, in front of, and with this wall — not through it.

## Round 23: the floor becomes a single inequality

The first move is a radical reduction. The "sector floor" — the statement that the load-bearing block of the window form stays positive — compresses, after nine modules of exact algebra, into a single ratio:

**ρ(X) = τ / τ_pnt > 0.**

In words: the prime comb, measured against its own mean density, must never push a certain quotient below zero. No more operator zoo, no window casuistry — one number per depth, and the question is whether it stays positive.

This is not a mere rephrasing. The reduction comes with structure: the relevant two-mode block is provably a faithful witness of the full floor (Cauchy interlacing, capture factor median 1.53), the capture angle is certified (cos θ median 0.990), and the direction of the effect follows a rotation law that closes symbolically — sympy residual exactly zero. The whole thing was registered as contract `PRIME.FLOOR.RATIO.01`, status open, with frozen kill criteria: if the envelope fails in depth or the angle collapses (cos²θ < 1/2), the route dies — publicly.

## Rounds 24–25: the certified skeleton

Then the skeleton of this one inequality was laid bare, bone by bone.

**The floor is an exact sum of squares.** A Lagrange identity decomposes the load-bearing determinant into a sum of squares over pairs of rank-1 carriers — every zero layer of the master identity is exactly rank 1, and the identity holds to machine precision on all 14 rungs of the deployed ladder. No cancellation miracle: manifest positivity, term by term.

**One pair carries, and it is certified.** Inside each of these sums of squares, a single pair dominates: the pole of the zeta function against the first zero γ₁ = 14.13. That pair is certified as a strictly positive interval, 14 of 14 rungs — after a tail repair cut the error budget by a median of **9.8 orders of magnitude**.

**The family exhausts.** What the one pair does not carry, a certified family of the 100 strongest pairs does: at full sieve depth, 97.7% to 98.1% of the entire floor, all carriers provably on the critical line (up to height 2 × 10⁴, classically verified — citation grade, no self-check).

**The remainder is closed — for all h.** The tail beyond the family is bounded with explicit, unconditional constants from the classical literature (Trudgian; the Platt–Trudgian horizon T = 3 × 10¹²) for **all** window depths h, with margins between 10³ and 10⁶. A previous validity horizon at α* ≈ 11 turned out along the way to be an artifact of the program's own float bookkeeping: the frozen quadratic error convention was four orders of magnitude too coarse. The honest, Higham-linear error chain (compensated summation, exact dot products) is 7 to 171 times tighter and closes the family gate at citation grade at full sieve depth, 6 of 6.

The result of the two rounds is a **certified explicit envelope**:

**ρ ≥ 4.335 · h^(−3/2), on 73 of 73 frames, non-decreasing.**

![The certified envelope](figures/a3_huellkurve.png)

And because the program does not trust its own optimism, the contract's frozen kill gates were deliberately played: sieve depth doubled (X = 18.4 to 25.5), dimension decoupled — if ρ were secretly a depth law, the kill would have fired. It did not fire. The margins grew monotonically, from ×5.8 to ×8.9; the smallest capture angle stayed at cos²θ = 0.849, far above the kill threshold of 0.5. One typed finding came for free: the single pair collapses in depth (its gap to the floor grows from a factor of 40 to 673) — and the certified family takes over. That is exactly what it was there for.

![Family share and the kill test](figures/a3_familien_anteil.png)

Said honestly, in the ledger's own language: this is **not a positivity theorem**. It is battery-relative (the deployed window family is frozen and finite), it lives on the necessary side, and the envelope stands "certified-explicit," not "proven." The difference is precisely the content of the last section of this article.

## The inversion: the positivity test bench becomes a measuring device

Now the story you can tell at the kitchen table.

The ladder of certified positivity rungs (each with a rigorous eigenvalue certificate: Cholesky factorization with Higham backward error plus Rayleigh enclosure; the deepest rung sits at X = 25.5) can be **inverted**. A positive rung does not just say "everything is fine here" — via a classical identity (Guinand), it excludes entire regions for hypothetical off-line zeros. And where there is exclusion, there is information: the width profile of these exclusion regions **peaks at the true zeros**. The mechanism is the redundancy of the explicit formula — a real zero makes the injected test intruder redundant, and the admissible margin rises exactly there.

From this, a locating instrument was built — by the rules the program enforces on itself:

- **Version 1 failed honestly.** 12 of 13 peaks hit, but 61% false peaks — the frozen gates said "failed," and that is what the record says.
- **Version 2 was preregistered**, SHA-256 hash frozen *before* any evaluation, and then tested on an **untouched, disjoint window**: the zero ordinates between 60 and 120, which had appeared in no calibration.
- Out-of-sample result: **20 of 24 zeros detected (83%), zero false positives.** With growing sieve depth, the detection rate rose 54% → 62% → 83%.

The point not to skim past: **not a single zero position** is built into this device. It knows primes up to a cap of 1.2 × 10¹¹, a window, and a positivity certificate. It finds the zeros anyway — a measuring device that finds zeros without knowing them.

![The exclusion detector and the zero locator](figures/a3_ausschluss_detektor.png)

The keystone is the **window verification**: on the window γ ∈ (60, 120], one single certified positivity object delivers three things at once — **location** (21 of 25 ordinates to within ±0.25, maximum error 0.242, zero unexplained peaks), **exclusion** (a pointwise certified off-line strip), and a **census** (21 hits plus 4 typed misses = 25 = exactly the rounded Riemann–von Mangoldt main term, 25.237 → 25). The four misses are not noise but dissected: one pair merge below the grid resolution and three prominence-limited cases — and the recovery prediction ("at the next deeper rung, exactly these will not reappear") was verified as typed at the new deepest certified rung X = 25.5. Scramble the primes, and the device breaks on all three axes simultaneously. Registered as contract `PRIME.DETECTOR.WINDOW.01`, status open.

And now the mandatory typing, verbatim from the suite: classical methods (Turing) prove the zero count exactly and their location with δ = 0 — the comb reaches 21 of 25, leaves a residual strip open, and can **never** close it at exponential cost. Strictly weaker than classical verification on every axis, reach limited to the Nyquist window, no new territory beyond the verified strip. The device is a **consistency demonstration of the explicit-formula reading on the necessary side** — not an RH statement. It is remarkable all the same: the same structure that carries the floor knows where the zeros sit.

## The wall, typed three ways

Which leaves the question: why is the envelope "certified" but not "proven"? The answer from rounds 26 and 27 is perhaps the most valuable part of the protocol — three independent attempts to close the gap, and three precise, documented closures of the respective routes. A map of impossibility is knowledge too. Here it is.

![The wall, surveyed three ways](figures/a3_wand_triptychon.png)

**Closure 1: the alias second moment (the analytic route).** The named proof blocker of the envelope was "alias phase correlations" — a random-phase model predicts an h⁻¹ law for the load-bearing quantity τ, while the tower measures h^(−2.5). Round 26 computed the bilinear form exactly (sympy-proven) and overturned the premise: **it is not the phases that carry the gap, it is the amplitudes.** The tower law decomposes exactly into an amplitude law (−3.17) plus a fading alignment (+0.67). And the Guinand split shows what is actually happening: the smooth part (−994.15) and the prime-comb fluctuation (+995.15) — each roughly a thousand times larger than the residual — cancel each other down to **1% of the scale a random comb would set**. Scramble the comb, and the coherent sum explodes by a factor of 2 × 10⁶ to 1.7 × 10⁷. The cancellation *is* the arithmetic. The honest conclusion is a **typed circularity boundary**: bounding an oscillating prime sum at its own square-root scale is variance control — pair-correlation-equivalent substance, and via Guinand the comb's self-cancellation is the zero-side floor statement *itself*. The analytic envelope route is thereby honestly closed and stop-listed.

**Closure 2: the character corner (the structural route).** The second attempt tried to represent τ as a positive "corner" — the expectation of a manifestly positive object under a projection, which would deliver positivity immediately. The result is a clean dichotomy: the corner identity **holds** — even as polynomial algebra in free event weights, that is, for arbitrary comb data. Which is exactly why it is **comb-blind**: the entire equality step consumes precisely one piece of arithmetic (a gluing identity that forces the character value ĉ = −1 for all 136 events), and the identity-bearing object is not positive. The systematic door census over all 128 characters of the register closed both typed escape routes: **visibility and identity are mutually exclusive** — every cell of the class map that carries the identity is placement-blind, and every placement-sensitive cell breaks the identity. Verdict: DOORS-CLOSED. Structural positivity can be had, but it cannot see the primes; the arithmetic lives entirely in the identification step.

**Closure 3: the SOS dual certificate (the algebraic route).** The third attempt asked: can a sum-of-squares rearrangement inside the commutant algebra (39-dimensional, with a canonical five-dimensional abelian subalgebra) rewrite the floor positively? Answer: no, and provably so. The exact reduction lemma collapses the semidefinite program onto a rational linear program whose **only** feasible point is the trivial diagonal rewrite. And the relevant determinant form has signature (1,2) — coefficient matching forces a non-positive Gram matrix, with a rational dual certificate as the death certificate: q(0,1,0) = −1 < 0. No cross-sector positive transfer exists. The nontrivial version of what is missing here *is* pair-correlation substance.

Three times the same address. The wall now has a registered name: **`PRIME.FLOOR.PAIRCORR.01`** — the floor–pair-correlation bridge, status open, with a declared entry point (an unconditional variance bound for the anisotropy of the prime comb at its square-root scale), frozen kill criteria, and the explicit note that the contract **promises no unconditional proof**: the proof direction contains pair-correlation arithmetic, and that is fenced in writing.

## What holds — and what does not

**What does not hold:** No RH proof, anywhere — the suite carries that as a typed statement. No positivity theorem for the floor: the envelope is certified-explicit on a frozen, finite battery, not proven at infinity. The detector is strictly weaker than classical zero verification on every axis and operates inside the classically verified strip — consistency, not new territory. And the three route closures are closures: the analytic, the structural, and the algebraic shortcut are dead, documented by name, stop-listed.

**What holds:** The open question has its most compact form so far — one ratio, one envelope, one named bridge to pair correlation. The skeleton underneath is not hope but certified mathematics: an exact sum-of-squares identity, a certified load-bearing pair, a family with 97.7–98.1% exhaustion, a remainder closed for all depths. The kill gates were deliberately played and survived, with growing margins. And as a by-product there now exists a preregistered, out-of-sample-validated instrument that locates zeta zeros from pure prime data — 83% detection, zero false positives, zero built-in zero knowledge.

Every number in this text is a named, runnable script: 829 modules, nearly 9,700 checks, all green; the status ledger (914 rows) carries 330 buried hypotheses — including the three new obituaries from this article. Perhaps that is the real point of the five rounds: a program that surveys its failures as precisely as its successes has turned a wall into a map. The door is still shut. But it now says on it where it is — and what it costs.

## Same-day addendum: four closures, the GUE boundary — and a door that opens

*This section was added on the afternoon of August 7: eleven more frozen probes, 136 checks, all green — probe level (`experiments/`), verdicts machine-checked, promotion into the verification suite under way as this text is written. And up front, as always: at the end of this addendum the Riemann Hypothesis is still unproven. What changed is something else — and it is the densest story this protocol has produced so far. Three acts.*

**Act one: the map of impossibility becomes complete.** The main text above ends with a dichotomy from the character corner: visibility and identity exclude each other. The afternoon turned that into four machine-checked impossibility theorems, with their quantifiers measured out:

- **All corners** (DOORS-CLOSED): the register's 128 characters collapse exactly to 18 classes, and the complete class map — five dressing sides times 18 classes, 90 cells — contains not a single cell carrying identity *and* visibility *and* placement sensitivity. Cell by cell: the same equation that grants the identity pins the corner block in place. Whoever carries is blind; whoever sees has paid.
- **All tower levels** (LEVEL2-CLOSED): the chain-ring ladder above does not help either — 2,048 characters at level m = 2, 32,768 at m = 3, all measured. The non-splitting jet does open new arithmetic modes (the one honestly typed hope), but they read position-blind, at every level.
- **The entire compression toolkit** (EXPECTATION-CLOSED): all 5,276 subgroups of the register, 74,259 expectation components — exactly two subgroups retain the identity component at all, and not one component of any expectation carries identity and visibility together. The full pinching and the Stinespring dilation with its 105 flag legs end in the same equation: the position data *is* in the dilation — but the identity freezes the reading to the constant 1.
- **Position-dependent carriers** (POSITION-CARRIER-TRADEOFF): the last escape route would have been to build the positions into the carrier construction itself. The structural pattern that closes it now has a name: **extremal pinning**. The identity demands the extreme point ĉ = −1 from the carrier — the entire mass locked, zero first-order freedom. What position dependence survives is a consistency defect that vanishes identically on *every* self-consistent comb, real or fake. Which distills the missing datum: *which self-consistent comb is the real one?*

Four closures are not four defeats. A complete impossibility map is an instruction — it says precisely that what is missing is not the compression but the **input**.

**Act two: the wall acquires a physics.** In parallel, the program measured where the floor demand sits relative to the random-matrix statistics of the zeros (Montgomery/GUE). Answer: **exactly at the boundary** (GUE-SATURATING). The demand-to-GUE-supply ratio runs to a plateau at 1.11, squarely inside the frozen saturation band; the load-bearing band sits at α ∈ 1–2 in the unfolded coordinate — immediately beyond Montgomery's window. And this is structural, not a knob artifact (SATURATION-STRUCTURAL): six of six source-native tower variants land at the same plateau (1.06 to 1.20), and the band does *not* move with the grid — it is a property of the unfolded zeros, not of the lattice.

Then the bootstrap question this forces: does the certified floor at depth X supply the statistics bound the floor at depth X′ > X demands — does an induction close the ladder? The answer is an exact loss law (LOOP-SHORT): **g = 1/(k²R²c_sup)**. Even an *ideal* supply (exact GUE, no measurement error, no certificate discipline) gives g = 1/R² = 0.65 < 1; measured it is 0.53, and with certificate discipline k = 2 it drops to 0.13 — zero sustainable induction steps. **The wall conserves itself through the saturation:** the ladder supplies exactly the statistics of the zeros, never more — and the floor demands a trace more than those statistics guarantee.

The flip side is the actual news. The GUE-rms bound closes only 39 of the 73 rungs; on the rest the measured demand exceeds the typical GUE scale. The positivity measured everywhere is therefore **finer-than-statistical information about the zeros** — no statistics theorem, not even a conjectural one, can deliver it.

**Act three: the door.** The closure theorems said: single events — a mass here, a position there — cannot do it; the missing datum is relations *between* events. And that is exactly **multiplicativity**: the Euler product, Λ = μ∗log — the convolution relations of the prime comb. It is precisely the datum that separates the zeta function from the classical Epstein fakes with class number ≥ 2 (x² + 5y², h = 2): there, 21 = 3 × 7 is represented while neither factor is — the class-group obstruction, exactly localized.

The relationally routed carrier is the first structure in the program to pass **all four gates** (RELATION-CARRIER-EXISTS) — including the self-consistency null where every compression and every single-event carrier had died: 14 of the null comb's 70 events carry missing product relations (18 is present, its divisors 3 and 6 are not), and the corner reads an excess of −0.30 there — against exactly 0 at the truth. State preserved exactly, identity inherited verbatim, τ_X reproduced. The second stage wires the reading at amplitude grade (exact fractions) and makes it L-function-safe: honest L-functions with an Euler product read as exactly zero — Selberg-correct blindness, the *right* behaviour, not a bug.

Then the ladder (EXCESS-NONNEGATIVE): in the identified corner's coordinates the floor decomposes per rung as **τ_X = λ_min(S) + excess** — comb-blind structure plus the prime comb's contribution. On all 67 reachable rungs (α = 2.77 to 6.30, masses to 3 × 10⁵) the excess is strictly positive, rising from +2.29 to +3.70.

And the keystone (SKELETON-CERTIFIED): **two giants, one certified sliver.** The structure sits at ≈ −3, the comb contribution at ≈ +3; their sum is a sliver of 10⁻⁴ to 10⁻⁵ — and that sliver is enclosed by a strictly positive interval on every one of the 67 rungs (widths 5 × 10⁻¹¹ to 7 × 10⁻⁹, three to five orders of magnitude below the margin). The same certificate discipline convicts the fake: the Epstein comb fails its certificate **certified negative** on every anchor. The extrapolated certification horizon (α* ≈ 9.1) lies far beyond the ladder's end — certifiability is not the binding constraint.

![The two giants and the certified sliver](figures/a3_zwei_giganten.png)

![The wall map: four doors closed, one door open](figures/a3_wand_karte.png)

**The wall, in its final form.** Mandatory typing, unabridged: no RH proof, anywhere; necessary side; frozen, finite ladder; the eleven probes are exploration level with frozen specifications and verdict rules, promotion under way. What the afternoon changed is the shape of the open question. It no longer reads "can any corner see the primes?" — yes, this one can, and it is the only one known. It reads: *is the identified object's excess nonnegative at every scale?* **Every finite instance of that question is now proven** — certified, with intervals, the fake certified out. **What stays open is the infinite quantifier:** a uniform lower bound on the margin — and by act two, that is exactly finer-than-statistical information about the zeros. No finite table, certified or not, settles it. The door is open; the wall stands behind it. Same address, `PRIME.FLOOR.PAIRCORR.01` — now in its sharpest coordinate form.

---

**Check it yourself:**

- Interactive overview of the prime front with the round protocols: [fixpoint-theory.com](https://www.fixpoint-theory.com)
- Open scripts (every number in the main text has a module, v814–v836; the addendum's numbers come from eleven frozen, runnable probes in `experiments/tfpt-discovery/`): [github.com/sthamann/tfpt](https://github.com/sthamann/tfpt)
- Archived version with DOI: [Zenodo, 10.5281/zenodo.20846087](https://doi.org/10.5281/zenodo.20846087)

*The contracts `PRIME.FLOOR.RATIO.01`, `PRIME.DETECTOR.WINDOW.01` and `PRIME.FLOOR.PAIRCORR.01` are public, with kill criteria. If you want to attack the bridge, the declared entry point is in the contracts paper.*

---

## LinkedIn summary (~250 words)

A measuring device that finds zeros of the zeta function without knowing them — and, the same afternoon, a door that opens after four impossibility theorems. The state of the prime front (August 6–7, all machine-checked):

— The open positivity question has shrunk to ONE inequality: ρ = τ/τ_pnt > 0 — the prime comb against its own density. Its skeleton is certified: envelope ρ ≥ 4.335·h^(−3/2) on 73/73 frames, kill gates deliberately played and survived.

— The inversion: certified positivity rungs locate zeros. Preregistered, out-of-sample: 83% detection, 0% false positives, census exactly Riemann–von Mangoldt (25 = 25) — with not a single zero position built in.

— The wall was mapped completely: four machine-checked impossibility theorems (all 128 characters in 18 classes, tower levels m ≤ 3, all 5,276 subgroup expectations, extremal pinning of position-dependent carriers). And it has a physics: the demand sits exactly at the GUE boundary (plateau 1.11, structural across all variants), the bootstrap loop gain stays below 1 — the wall conserves itself; the measured positivity is finer-than-statistical information.

— Then the door: the input the map dictated is MULTIPLICATIVITY — the Euler product as relations between events, exactly the datum separating zeta from class-number-2 fakes. The relational carrier passes all four gates (including the null where everything else died), the excess is positive on all 67 rungs, the skeleton strictly interval-certified — the Epstein fake certified negative.

No RH proof. Every finite instance proven; what stays open is the infinite quantifier — a uniform margin, finer than statistics.

All machine-verifiable: fixpoint-theory.com
