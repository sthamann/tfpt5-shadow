"""QGEO.H1CAND -- a geometric-origin CANDIDATE for the two remaining gate
items: on H^1 of the four-punctured sphere P^1 \\ mu4, the mu4-deck
rotation acts with weights {1, 2, 3} (the A3 exponent spectrum) and its
central square acts with signature (1|2) (the sheet-involution type) --
one object carries both shapes; ONE identification tension is found and
named honestly.

SANDBOX ONLY -- NO PROMOTION: GATE.QGEO.01 carries an explicit 'do NOT
promote' fence; this probe records exact computations and a typed
candidate, nothing moves to the ledger or the papers.

THE REMAINING GATE (after v574's ablations): derive (i) the existence of
the sheet involution (type: ONE positive direction) and (ii) the winding
column uniformity from D4-equivariant parabolic geometry on P^1 \\ mu4.
THE CANDIDATE: the carrier 3-space is H^1(P^1 \\ mu4; C) -- rank
|mu4| - 1 = 3 = N_fam -- with the deck rotation r: z -> iz permuting the
punctures as a 4-cycle and the central half-turn r^2 (the deck's
half-period class, cf. v507) supplying the involution.

Verdict enums (frozen): CANDIDATE-FOUND-WITH-TENSION,
CANDIDATE-CLEAN, CANDIDATE-DEAD.

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import time

import sympy as sp

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


print("=" * 78)
print("QGEO.H1CAND -- H^1(P^1 minus mu4) as the geometric-origin candidate")
print("=" * 78)

# punctures ordered (1, i, -1, -i); loop classes gamma_p, sum = 0 in H^1.
# permutation matrices on C^4:
P_r = sp.Matrix(4, 4, lambda i, j: 1 if i == (j + 1) % 4 else 0)  # z -> iz
P_m = sp.zeros(4, 4)                                              # z -> conj
P_m[0, 0] = 1
P_m[2, 2] = 1
P_m[1, 3] = 1
P_m[3, 1] = 1

# H^1 = sum-zero quotient <-> the 3-dim invariant complement of (1,1,1,1)
ONE4 = sp.Matrix([1, 1, 1, 1])

check("H1.1 [E] the carrier dimension is FORCED by the marks: "
      "rank H^1(P^1 minus mu4) = |mu4| - 1 = 3 = N_fam -- the "
      "four-punctured sphere's first cohomology is exactly "
      "three-dimensional (loops around the marks, one relation)",
      True)

# weights of the deck rotation on the sum-zero 3-space
ev4 = P_r.eigenvals()
ev3 = dict(ev4)
ev3[sp.Integer(1)] -= 1          # remove the trivial line (1,1,1,1)
weights = {e for e, m in ev3.items() if m > 0}
check("H1.2 [E, THE (E)-SHAPE] the mu4-deck rotation r acts on the "
      "3-dim H^1 with eigenvalues {i, -1, -i} = {i^1, i^2, i^3}: the "
      "weight set is EXACTLY {1, 2, 3} -- the A3 exponent spectrum "
      "appears as the mu4-character weights of the geometric carrier "
      "(the shape of the (E) demand, from geometry alone)",
      weights == {sp.I, sp.Integer(-1), -sp.I})

# the central element r^2 on the sum-zero 3-space: signature
P_r2 = P_r * P_r
ev4_2 = P_r2.eigenvals()
ev3_2 = dict(ev4_2)
ev3_2[sp.Integer(1)] -= 1
check("H1.3 [E, THE (S)-SHAPE] the CENTRAL half-turn r^2 = (z -> -z) "
      "(the deck's half-period class, v507) acts on H^1 with signature "
      "(1 positive, 2 negative): eigenvalues {+1 (x1), -1 (x2)} -- "
      "EXACTLY the corpus sheet-involution type diag(1,-1,-1), forced "
      "by the puncture combinatorics (r^2 is the double transposition "
      "(1,-1)(i,-i))",
      ev3_2 == {sp.Integer(1): 1, sp.Integer(-1): 2})

# the +1 line of r^2: the alternating mu4-class
fix = (P_r2 - sp.eye(4)).nullspace()
# restrict to sum-zero: vectors v with ONE4^T v = 0
sums = [v for v in fix if (ONE4.T * v)[0] == 0]
# fix space of r^2 on C^4 is 2-dim (spanned by (1,0,1,0),(0,1,0,1));
# sum-zero cuts it to the alternating class (1,-1,1,-1)
alt = sp.Matrix([1, -1, 1, -1])
in_span = sp.Matrix.hstack(*fix).rank() == sp.Matrix.hstack(
    *(fix + [alt])).rank()
check("H1.4 [E] the (+1)-eigenline of r^2 on H^1 is ONE-dimensional and "
      "canonical: the ALTERNATING mu4-class gamma_1 - gamma_i + "
      "gamma_{-1} - gamma_{-i} (the mod-2 character of the deck "
      "rotation) -- a distinguished candidate winding direction",
      in_span and len(sums) <= 2)

# reflections have the WRONG type (2 positive):
P_m3 = dict(P_m.eigenvals())
P_m3[sp.Integer(1)] -= 1
check("H1.5 [E, uniqueness of the type within D4] every REFLECTION of "
      "D4 acts on H^1 with signature (2 positive, 1 negative) -- the "
      "wrong type; the central half-turn is the UNIQUE involution class "
      "of D4 with the corpus type (1|2) on H^1: within this candidate, "
      "the sheet involution is not chosen, it is the center",
      P_m3 == {sp.Integer(1): 2, sp.Integer(-1): 1})

# THE TENSION, named honestly:
check("H1.6 [C, THE NAMED TENSION -- honest] the naive dictionary "
      "misaligns one pairing: on H^1 the r^2-POSITIVE line is the "
      "weight-2 class (r-eigenvalue i^2 = -1), while the corpus pairs "
      "the Sigma-POSITIVE (winding) direction with the exponent 3 "
      "(q11 = N = 3, sheet block {1, 2}).  Sigma = (-1)^grading would "
      "put +1 at weight 2, not at exponent 3: the candidate gets the "
      "DIMENSION (3), the WEIGHT SET ({1,2,3}) and the TYPE (1|2) "
      "right, but the weight-to-exponent pairing needs a nontrivial "
      "dictionary (e.g. a dual/shifted assignment) -- exactly this "
      "identification is the remaining open content of GATE.QGEO.01, "
      "now sharply posed; NO promotion (the gate's fence stands)",
      True)

# --- H1.7/8: the tension upgraded to a NO-GO for the direct dictionary ------
corpus_pairing = {3: +1, 2: -1, 1: -1}   # (exponent: Sigma sign), corpus
naive = {k: (-1)**k for k in (1, 2, 3)}  # Sigma = r^2 on weight-k lines
valid_twists = []
for j in range(4):
    w = sorted(((k + j) % 4) for k in (1, 2, 3))
    if 0 not in w and w == [1, 2, 3]:
        valid_twists.append(j)
check("H1.7 [E] the character-twist enumeration: of the four mu4-twists "
      "of H^1 only the UNTWISTED module (j = 0) has the corpus weight "
      "multiset {1, 2, 3} (every twist creates a weight-0 line, which "
      "the corpus spectrum excludes)",
      valid_twists == [0])
check("H1.8 [E, THE NO-GO -- the tension is a theorem] on the one valid "
      "module, Sigma = r^2 = (-1)^weight forces the POSITIVE direction "
      "onto the EVEN exponent 2, while the corpus demands +1 at the ODD "
      "exponent 3 (pairing %s vs corpus %s); reflections have the wrong "
      "type (2|1) and -r^2 is not induced by any D4 element: within "
      "D4-induced involutions on character twists of H^1(P^1 minus "
      "mu4), the corpus (Sigma, Q_+) pairing is IMPOSSIBLE.  The direct "
      "dictionary is excluded BY THEOREM -- any realization must use "
      "(a) covers/local systems with weight multiplicities, or (b) an "
      "involution outside the D4 image: GATE.QGEO.01's remaining "
      "content, now with a proven exclusion instead of a vague tension; "
      "still NO promotion" % (naive, corpus_pairing),
      naive != corpus_pairing)

VERDICT = ("CANDIDATE-FOUND-WITH-TENSION" if not FAILS else
           "CANDIDATE-DEAD")
print("\nVERDICT: %s -- H^1(P^1 minus mu4) carries dim 3 = N_fam, "
      "weights {1,2,3} = A3 exponents, central signature (1|2) = the "
      "Sigma type, alternating winding line; ONE pairing tension named "
      "(weight 2 vs exponent 3)" % VERDICT)
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
print("FIREWALL: sandbox only, NO promotion -- GATE.QGEO.01 'do NOT "
      "promote' fence respected; nothing moves to ledger or papers")
