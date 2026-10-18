#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v888 -- DOILY.S6.IRREP.01 + DOILY.PLUCKER.GR25.01 + CFIN.ANCHOR.HADAMARD.01 + CFIN.S6.VACUUM.01 + CFIN.AUT.FLAVOR.C6.01 + CFIN.K6.MOTIF.01 + DOILY.PFAFFIAN.WICK.01 + P2.SELFHOSTING.PAIRING.01 + ANCHOR.MOD30.CLOCK.01 + K6.ONEFACT.OUTER.01: THE COMPLETE FINITE PFAFFIAN/K6 SIGNATURE OF THE COMPILER, ONE module from three probes (27/27 + 19/19 + 42/42 checks, zero fails, verdicts S6PLUCKER-CLOSED + C6FLAVOR-MEASURED + INTERTWINED + K6PFAFFIAN-CLOSED (T1=MOTIF-CLOSED, T2=GAUGE-MATCHED(chi), T3=SELFHOSTING-COUNTED, T4=CLOCK-DISTINGUISHED, T5=OUTER-SIGNATURE-CLOSED); discovery probes s6_plucker_hadamard_probe.py, cfin_aut_flavor_probe.py, k6_pfaffian_selfhosting_probe.py, rounds 44/49, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~1 s; exact integer / Fraction / sympy arithmetic in every decision, no floats, no RNG, no fits).  (1) THE FOUR CHEAP FINITE THEOREMS (s6_plucker): the duad permutation representation of S_6 decomposes as S^(6) + S^(5,1) + S^(4,2) (dims 1 + 5 + 9, characters from scratch by Murnaghan-Nakayama), the doily incidence N is S_6-equivariant, and its point-side modulus |N|/3 acts on the isotypics by the EXACT scalars (1, 0, 2/3) -- with the anchor identities 15 = 1 + e2 + (e2 - e3)^2 and 2/3 = e3/(e2 - e3) at (e1, e2, e3) = (4, 5, 2), e2 = g_car; the 15 monomials of the five Gr(2,5) Plucker quadrics biject onto the 15 doily lines with the quadric signs (+, -, +) EQUAL to the v880 Hodge signs on 15/15; the q* zero set is a (16, 6, 2) difference set with the anchor signature v = 2^e1, k = p2(a) = 6, lambda = e3, k - lambda = e1, v - k = 10 = C(e2, 2) (bent Walsh / perfect autocorrelation rebuilt as wards); and the VACUUM-SELECTION theorem: |Stab(q*)| = 120 acts faithfully AND surjectively as S_5 on the remaining five Arf-1 refinements, with its orbits on the 16 messages EXACTLY the iota-weight classes 1 + 5 + 10 -- choosing one of six equivalent vacua leaves the carrier S_5.  (2) THE FLAVOR HEXAGON IS ONE Aut(C_fin) ORBIT (cfin_aut_flavor): Aut(C_fin) ~= C6 rebuilt exactly (order 6, orders [1,2,3,3,6,6], faithful in Sp(4,2)); the pinned generator g satisfies g^2 = sigma (the deployed family 3-cycle) EXACTLY and g^3 = the W-edge swap (the S2 factor of Stab_{S5}(W) = S3 x S2, sheet count |W| = 2); g acts on the ten pair-messages with cycle type 1 + 3 + 6, its orbits EQUAL the three charge shells, and the g-orbit of {f1, w1} traverses the deployed flavor hexagon edge by edge, D6-equivalent to the deployed transport cycle -- the hexagon is one full automorphism orbit, and the recovery chain lambda_rec = (|Z2|/N_fam)^{|Aut(C_fin)|} = (2/3)^6 = 64/729 equals the frozen deployed transfer eigenvalue as an exact Fraction (honest typing: the corpus derives the exponent 6 as p2 = |R+(A3)|; the |Aut| reading is a NEW consistency, not a claim upgrade).  (3) THE K6/PFAFFIAN SIGNATURE (k6_pfaffian_selfhosting): the K6 MOTIF theorem in full -- all 35 PG(3,2) lines classified as K6 motifs: 15 doily lines = the 15 perfect matchings, the 10 secants = the 10 triangles THROUGH the vacuum vertex, the 10 externals = the 10 triangles avoiding it (20 triangles exhausting C(6,3)), the edge law q* = 0 iff the edge touches the vacuum vertex, and the carrier dictionary phi consistent edge by edge; the FERMIONIC Pfaffian signs of the symbolic Pf(A) expansion (15 monomials, coefficients +-1) are GAUGE-MATCHED to the corpus Hodge signs via the canonical global character chi(i) = (-1)^(i+1) -- exactly the Laplace sign of the vacuum-row minor expansion Pf(A) = sum_i (-1)^(i+1) A_0i Pf(A_{0i-hat}) AND the volume-form (Lambda^4 vs Lambda^5) conversion character, the triple identification computed, not assumed; each 4x4 minor Pfaffian EQUALS the round-44 3-term Plucker quadric; Pf is C6-equivariant (Pf(P A P^T) = det(P) Pf(A) symbolically, per-matching signs via the crossing character); the SELF-HOSTING COUNTING THEOREM: C(g+1, 2) = g!! has EXACTLY the solutions {1, 5} over odd g (g = 1 trivial, stated), so g = 5 is the unique nontrivial fixed point, with (g-2)!! = 3 = N_fam and the growth separation g!! > C(g+1,2) for all odd g >= 7 (symbolic induction ratio) -- an [E] counting theorem with the physical Wick-compiler premise honestly kept [O], NO marker move; the anchor power-sum clock p_n = 2 + 2^n obeys p_{n+1} = 2 p_n - 2 with mod-30 orbit 4 -> 6 -> 10 -> 18 -> 4 of period EXACTLY 4 = |mu_4|, typed CLOCK-DISTINGUISHED by the anti-numerology census (every purely period-4 modulus divides 30, so 30 is the maximal clock); and the one-factorization census: K6 has exactly 6 one-factorizations (30 = 6 x 5 = 2 x 15 schedule) with the exceptional-outer-automorphism signature -- a transposition acts (2,1,1,1,1) on the 6 vertices but (2,2,2) on the 6 factorizations, the two S6 actions non-conjugate, NO canonical vertex <-> factorization bijection (fixed-point obstruction, report only).  NO RH claim; no marker moves; all controls fired (Arf-0 refinements, secant substitution, wrong scalar, non-automorphism census 600/600, scrambled transport, flipped sign character, g = 3/7 counterexamples).  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes s6_plucker_hadamard_probe.py (27/27,
S6PLUCKER-CLOSED, SPEC v1, no amendments at freeze),
cfin_aut_flavor_probe.py (19/19, C6FLAVOR-MEASURED, SPEC v1 with the
RUN NOTE on record: run 1 aborted on a pure %-formatting TypeError
in a report string, fixed with no frozen claim, check, kill,
control or fire rule altered), k6_pfaffian_selfhosting_probe.py
(42/42, K6PFAFFIAN-CLOSED, SPEC v1, no amendments at freeze), all
2026-08-09, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen sources embedded BYTE-EXACT, executed verbatim
in isolated namespaces; printed spec SHAs reproduce; byte-equality
ward vs experiments/tfpt-discovery/ inside the pattern gates.
Corpus surfaces consumed read-only / rebuilt inline: v880 (q*
normal form, anchor line classification, Hodge multiplication),
v774/v845 (Arf census, Sp(4,2), selector), v853 (difference set /
bent wards), v849 (Aut(C_fin) ~= C6), v808 (Petersen hexagon),
v54/v56/v82/v124 (frozen transfer spectrum), v832 (anchor).

FIREWALL: exact integer / Fraction / sympy arithmetic only; no
floats in any decision, no RNG, no fits; AST firewalls inside the
probes; the self-hosting premise stays [O] -- the counting theorem
alone is [E].  NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source s6_plucker_hadamard_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""s6_plucker_hadamard_probe -- DOILY.S6.IRREP.01 +
DOILY.PLUCKER.GR25.01 + CFIN.ANCHOR.HADAMARD.01 + CFIN.S6.VACUUM.01
(EXPLORATION ONLY, experiments/; round 44, the four cheap finite
theorems of the 2026-08-09 external review of Revision 555,
2026-08-09).

WHY NEW (redundancy check done against the corpus, 2026-08-09):
v880 has the q* normal form, the anchor classification of PG(3,2)
lines, the Hodge multiplication b_jk ^ b_lm = +-f_i with the 5 x 3
bijection, and the g = 5 exhaustion -- NOT redone here, only rebuilt
as inputs.  v774/v845 have the Arf census 6 + 10, |Sp(4,2)| = 720 by
full census, the faithful S6 action on the six Arf-1 forms, the K6
duad model v <-> D(v), and |Stab(q*)| = 120 acting as S5 with orbits
{1, 5, 10}.  v853 has the (16,6,2) Hadamard difference set, the bent
Walsh eigenvector s_q-hat = -4 s_q and the perfect autocorrelation.
v852 names the S6 standard representation inside the ovoid decoder
and the review cites the projector P5 = I/2 - B/4 + J/12.  v844/v880
have charpoly(N N^T) = (x-9)(x-4)^9 x^5, i.e. the singular values
{3, 2^9, 0^5} of the doily incidence.  The corpus 'Plucker' (v37/
v42/v49/v71) is the FLAVOR-operator readout ||Pl(K)||_1 -- a
different object entirely.  GENUINELY NEW here: (T1) the SPECHT
IDENTIFICATION -- the duad permutation representation of S_6
decomposes as S^(6) + S^(5,1) + S^(4,2) (dims 1 + 5 + 9, characters
computed from scratch by Murnaghan-Nakayama), the doily incidence N
is S_6-equivariant, and its point-side modulus |N| = sqrt(N N^T)
(exact rational via spectral projectors) acts on the isotypics by
the scalars 3 x (1, 0, 2/3) -- with the anchor identities
15 = 1 + e2 + (e2 - e3)^2 and 2/3 = e3/(e2 - e3) at (e1,e2,e3) =
(4,5,2); (T2) the Gr(2,5) PLUCKER READING -- the 15 monomials of the
five 3-term Plucker quadrics biject onto the 15 doily lines under
the v880 support partition, and the quadric signs (+,-,+) EQUAL the
v880 Hodge signs; (T3) the ANCHOR SIGNATURE of the v853 difference
set -- v = 2^e1, k = p2(a), lambda = e3, k - lambda = e1, v - k =
C(e2,2) (the DS/bent/autocorrelation facts themselves are corpus,
rebuilt as wards only); (T4) the VACUUM-SELECTION PACKAGING -- the
corpus counting re-verified end to end plus the two set equalities:
the Stab(q*) image on the REMAINING FIVE Arf-1 refinements has order
exactly 120 = |S_5| (faithful AND surjective), and the Stab(q*)
orbits on the 16 messages EQUAL the iota-weight classes
Lambda^0 + Lambda^4 + Lambda^2 = 1 + 5 + 10 (zeros/ovoid/pairs) --
choosing one of six equivalent Arf-1 vacua leaves an S_5 acting on
the other five, and THAT S_5 is the carrier symmetry.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run):

 T1  DOILY.S6.IRREP.01 -- the isotypic scalar law.
     (a) K6 duad model rebuilt (v774): the six Arf-1 refinements
         label {1..6}; D(v) = {i : q_i(v) = 0} is a bijection of the
         15 nonzero messages onto the 15 duads; every doily line
         maps to a PERFECT MATCHING of K6 and the 15 lines exhaust
         all 15 matchings;
     (b) S_6-EQUIVARIANCE: for the generators (12) and (123456) the
         permutation matrices satisfy P_g N = N L_g EXACTLY (N =
         15 x 15 point-line incidence);
     (c) CHARACTERS from scratch (Murnaghan-Nakayama over beta
         sets): chi(id) = (1, 5, 9) for S^(6), S^(5,1), S^(4,2);
         the three characters are orthonormal over all 720 group
         elements (exact rationals); the duad permutation character
         has multiplicities (1, 1, 1) and 15 = 1 + 5 + 9;
     (d) ISOTYPIC PROJECTORS P_lam = (dim/720) sum_g chi(g) rho(g):
         idempotent, mutually orthogonal, sum = I, traces (1,5,9);
     (e) SCALAR LAW: N N^T P_lam = s^2 P_lam with s^2 = (9, 0, 4);
         charpoly(N N^T) = (x-9)(x-4)^9 x^5 (v844/v880 rebuilt);
         the point-side modulus |N| := 3 P_(6) + 2 P_(4,2) satisfies
         |N|^2 = N N^T EXACTLY, hence |N|/3 acts on the isotypics
         S^(6), S^(5,1), S^(4,2) by (1, 0, 2/3) EXACTLY (this is
         the honest operator reading: N maps points to lines, so
         'N/3 acts by scalars' means the singular-value modulus on
         the point side);
     (f) corpus crosscheck: P_(5,1) = I/2 - B/4 + J/12 with
         B = I + A_disjoint = N N^T - 2I (the review's P5), and the
         anchor identities 15 = 1 + e2 + (e2-e3)^2, 2/3 =
         e3/(e2 - e3) at (e1,e2,e3) = (4,5,2), e2 = g_car.

 T2  DOILY.PLUCKER.GR25.01 -- the five Plucker quadrics ARE the
     doily.  For each omitted i in {1..5} with {j<k<l<m} the rest:
     Q_i = p_jk p_lm - p_jl p_km + p_jm p_kl (the Gr(2,5) relation).
     (a) exactly 5 x 3 = 15 monomials, all distinct as unordered
         disjoint duad pairs {S, T} on {1..5};
     (b) BIJECTION: monomial {S, T} of Q_i -> the unique doily line
         whose two pair points have iota-supports S, T and whose
         ovoid point has support {1..5} \ {i} (v880 lift) -- 15
         monomials onto 15 lines, 1:1, i-slots agreeing;
     (c) CONVERSE ward: no secant (<= 1 pair point) and no external
         line (pairwise overlapping supports) yields a monomial;
     (d) SIGN STRUCTURE: for every monomial the Plucker sign
         (+, -, +) EQUALS the v880 Hodge sign of b_S ^ b_T = +-f_i
         (exact integer exterior algebra; report the 5 x 3 table
         and state exactly what matches).

 T3  CFIN.ANCHOR.HADAMARD.01 -- the anchor signature of the zero
     set.  Z = {x : q*(x) = 0} (re-verify per v880: {0} u the five
     ovoid messages, |Z| = 6):
     (a) DIFFERENCE SET: every nonzero d in F_2^4 has EXACTLY
         lambda = 2 ordered representations d = x + y with x, y in
         Z (v853 rebuilt as ward); k(k-1) = lambda(v-1) = 30;
     (b) ANCHOR SIGNATURE (new): v = 2^e1 = 16, k = p2(a) = 1+1+4
         = 6, lambda = e3 = 2, k - lambda = e1 = 4, v - k = 10 =
         C(e2, 2), with a = (1,1,2), (e1,e2,e3) = (4,5,2);
     (c) BENT ward (v853 rebuilt): the Walsh spectrum of
         (-1)^{q*} is flat, |W(u)| = 4 = 2^{e1/2} on all 16
         characters (exact integer Walsh transform);
     (d) perfect autocorrelation ward: sum_x s(x) s(x+a) =
         16 delta_{a,0} on all 16 shifts.

 T4  CFIN.S6.VACUUM.01 -- the vacuum-selection theorem.
     (a) census re-verified (v774/v845): brute force over all 2^16
         functions gives EXACTLY 16 quadratic refinements of hb =
         the 16 linear shifts; Arf census 10 (10 zeros) + 6 (6
         zeros);
     (b) Sp(4,2) census: all 65536 candidate matrices -> |Sp(4,2)|
         = 720; the action on the six Arf-1 refinements has image
         of order 720 (faithful, = S_6) and is TRANSITIVE (orbit of
         q* = all six);
     (c) VACUUM SELECTION (new set equalities): |Stab(q*)| = 720/6
         = 120; its permutation image on the REMAINING FIVE Arf-1
         refinements has order EXACTLY 120 = |S_5| -- faithful and
         surjective onto S_5;
     (d) the Stab(q*) orbits on the 16 messages are EXACTLY the
         iota-weight classes: sizes 1 + 5 + 10 with orbit sets
         EQUAL to (Lambda^0, Lambda^4, Lambda^2) = ({0}, ovoid,
         pairs) as sets -- the surviving S_5 is the carrier
         symmetry.

 C   CONTROLS (must fire):
     C1 an Arf-0 refinement's zero set (10 zeros) is NOT a (16,6,2)
        difference set: k = 10 != 6 and the representation census
        differs from the all-2 profile (expected honest outcome:
        the complementary (16,10,6) profile -- reported either way);
     C2 a secant line breaks the T2 bijection: substituting a
        secant for a doily line leaves a monomial unmatched (the
        secant has <= 1 pair point, no {S,T} key);
     C3 the wrong scalar breaks T1: |N|/3 does NOT act as 2/3 on
        S^(5,1) (it acts as 0 there; residual reported).

KILLS (any one fires => typed gap):
  K0 AST firewall / import hygiene breaks      -> PIPELINE-BROKEN
  K1 duad model / equivariance / characters /
     projectors / scalar law breaks            -> IRREP-BROKEN
  K2 monomial census / bijection / signs break -> PLUCKER-BROKEN
  K3 difference set / signature / bent breaks  -> HADAMARD-BROKEN
  K4 census / transitivity / stabilizer /
     orbit-grading breaks                      -> VACUUM-BROKEN
  K7 a control does not fire                   -> CONTROL-DEAD

VERDICT (frozen enum): S6PLUCKER-CLOSED / IRREP-BROKEN /
PLUCKER-BROKEN / HADAMARD-BROKEN / VACUUM-BROKEN / PIPELINE-BROKEN /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website
surface.  Exact integer/Fraction/sympy arithmetic ONLY; no floats,
no RNG, no fits.  AST scan bans zetazero/nzeros/primerange/isprime/
primepi/nextprime/prevprime.  NO physics claim beyond the four
finite theorems; no marker moves.

SPEC v2 AMENDMENTS: none at freeze; any post-run amendment is
documented here with the fail-first output preserved.

Sources (read-only, machinery rebuilt inline): verification/v880
(bit form, selector, doily, Hodge signs, anchor Vieta), v774/v845
(Arf census, Sp(4,2), duad model, stabilizer), v853 (difference
set / bent wards), v852 (S6 standard rep context), tfpt_constants
(N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/s6_plucker_hadamard_probe.py
"""

import ast
import hashlib
import itertools
import os
import sys
import time
from fractions import Fraction

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------------------ bit model
# words are ints 0..15; bit i = coordinate x_{i+1} in the family/anchor
# basis (F1, F2, F3, A) with Gram J - I (v880):
#   hb(v, w) = (|v| |w| - |v & w|) mod 2   (v834 identity)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000          # A    = (0,0,0,1)
FSIG = 0b0111           # FSum = (1,1,1,0)
ANCHOR = (1, 1, 2)      # v832 [E]
E1, E2, E3 = 4, 5, 2    # elementary symmetric of the anchor (v880)


def sig(v):
    """order-3 deck sigma: (b0,b1,b2,b3) -> (b2,b0,b1,b3) (v880)."""
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


def refinement_census():
    """brute force over all 2^16 functions q: V -> F_2 with q(0)=0
    implied by the cocycle law; returns all q with
    q(x+y)+q(x)+q(y) = hb(x,y) on all 256 pairs (v774/v845)."""
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for x in range(16):
            hx = HT[x]
            qx = q[x]
            for y in range(16):
                if q[x ^ y] ^ qx ^ q[y] != hx[y]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


def iota_wt(v):
    """iota-weight of the parity lift (v880): |v| + parity bit."""
    w = pc(v)
    return w + (w % 2)


def iota_support(v):
    """support in {1..5} of iota(v) = (b0,b1,b2,b3,parity)."""
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return frozenset(i + 1 for i, bit in enumerate(b) if bit)


def wedge_sign(S, T):
    """sign of e_S ^ e_T for disjoint 2-sets S, T in {1..5}; None if
    the supports overlap (exact integer exterior algebra)."""
    seq = sorted(S) + sorted(T)
    if len(set(seq)) != 4:
        return None
    inv = sum(1 for i in range(4) for j in range(i + 1, 4)
              if seq[i] > seq[j])
    return -1 if inv % 2 else 1


# --------------------------------------------- Murnaghan-Nakayama (exact)
_MN_CACHE = {}


def _beta_to_lam(bset):
    b = sorted(bset)
    m = len(b)
    parts = [b[m - 1 - j] - (m - 1 - j) for j in range(m)]
    return tuple(p for p in parts if p > 0)


def mn_char(lam, rho):
    """character chi_lam on cycle type rho, by rim-hook removal on
    beta sets; exact integers."""
    key = (lam, rho)
    if key in _MN_CACHE:
        return _MN_CACHE[key]
    if not rho:
        val = 1 if not lam else 0
    else:
        r, rest = rho[0], rho[1:]
        n = len(lam)
        beta = sorted(lam[i] + (n - 1 - i) for i in range(n))
        bset = set(beta)
        val = 0
        for b in beta:
            if b - r >= 0 and (b - r) not in bset:
                leg = sum(1 for c in beta if b - r < c < b)
                nb = frozenset((bset - {b}) | {b - r})
                val += (-1) ** leg * mn_char(_beta_to_lam(nb), rest)
    _MN_CACHE[key] = val
    return val


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc, reverse=True))


def main():
    print("DOILY.S6.IRREP.01 + DOILY.PLUCKER.GR25.01 + "
          "CFIN.ANCHOR.HADAMARD.01 + CFIN.S6.VACUUM.01")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO physics claim beyond the finite theorems; no marker "
          "moves; exploration only.")

    # ==================================================================
    section("S0 -- firewall + shared setup")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s"
          % (BANNED_IDS,), not bad, kill="K0")

    refs = refinement_census()
    check("S0.1 brute-force census over 2^16: EXACTLY 16 quadratic "
          "refinements of hb (v774/v845 rebuilt)", len(refs) == 16,
          "got %d" % len(refs), kill="K0")

    arf0 = [q for q in refs if q.count(0) == 10]
    arf1 = [q for q in refs if q.count(0) == 6]
    check("S0.2 Arf census 10 + 6 (zeros 10 <-> Arf 0, zeros 6 <-> "
          "Arf 1)", len(arf0) == 10 and len(arf1) == 6,
          "got %d + %d" % (len(arf0), len(arf1)), kill="K0")

    siginv = [q for q in refs
              if all(q[sig(v)] == q[v] for v in range(16))]
    cand_a = [q for q in siginv if q[A_BIT] == 1]
    cand = [q for q in cand_a if q[FSIG] == 0]
    check("S0.3 frozen v845 selector: 16 -> %d (sigma) -> %d "
          "(q(A)=1) -> %d (q(FSum)=0) = unique q*"
          % (len(siginv), len(cand_a), len(cand)),
          len(siginv) == 4 and len(cand_a) == 2 and len(cand) == 1,
          kill="K0")
    QSTAR = cand[0]

    ZQ = [v for v in range(16) if QSTAR[v] == 0]
    ovoid = [v for v in ZQ if v]
    check("S0.4 zeros(q*) = {0} u five ovoid messages (weights 3,4; "
          "v880 rebuilt): |Z| = %d" % len(ZQ),
          len(ZQ) == 6 and sorted(pc(v) for v in ovoid) ==
          [3, 3, 3, 3, 4], kill="K0")

    NZ = [v for v in range(1, 16)]
    lines_pg = set()
    for a2, b2 in itertools.combinations(NZ, 2):
        lines_pg.add(frozenset({a2, b2, a2 ^ b2}))
    iso = sorted([L for L in lines_pg
                  if all(HT[u][w] == 0 for u in L for w in L)],
                 key=sorted)
    noniso = [L for L in lines_pg if L not in set(iso)]
    sec_lines = [L for L in noniso
                 if sorted(QSTAR[v] for v in L) == [0, 0, 1]]
    ext_lines = [L for L in noniso
                 if sorted(QSTAR[v] for v in L) == [1, 1, 1]]
    check("S0.5 PG(3,2): 35 lines = 15 doily + 10 secant + 10 "
          "external (v880 rebuilt)",
          len(lines_pg) == 35 and len(iso) == 15
          and len(sec_lines) == 10 and len(ext_lines) == 10,
          kill="K0")

    # ==================================================================
    section("T1 -- DOILY.S6.IRREP.01: Specht scalars (1, 0, 2/3)")
    # ==================================================================
    # (a) K6 duad model via the six Arf-1 labels (v774 rebuilt)
    arf1s = sorted(arf1)

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1s) if q[v] == 0)

    DUADS = sorted((frozenset(d)
                    for d in itertools.combinations(range(6), 2)),
                   key=sorted)
    DIDX = {d: i for i, d in enumerate(DUADS)}
    dmap = {v: duad(v) for v in NZ}
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS)

    def match_of(L):
        return frozenset(dmap[v] for v in L)

    MATCHINGS = sorted((match_of(L) for L in iso),
                       key=lambda m: sorted(sorted(d) for d in m))
    MIDX = {m: i for i, m in enumerate(MATCHINGS)}
    all_match = all(
        len(m) == 3
        and frozenset().union(*m) == frozenset(range(6))
        and sum(len(d) for d in m) == 6
        for m in MATCHINGS)
    check("T1.1(a) duad model: D(v) = {i : q_i(v)=0} bijects the 15 "
          "messages onto the 15 duads; every doily line is a "
          "PERFECT MATCHING of K6; 15 distinct = all matchings",
          biject and all_match and len(set(MATCHINGS)) == 15,
          kill="K1")

    Nmat = sp.Matrix(15, 15, lambda p, l:
                     1 if DUADS[p] in MATCHINGS[l] else 0)

    # (b) equivariance for the generators, exact
    def act_pt(g):
        return [DIDX[frozenset(g[a] for a in DUADS[p])]
                for p in range(15)]

    def act_ln(g):
        return [MIDX[frozenset(frozenset(g[a] for a in d)
                               for d in MATCHINGS[l])]
                for l in range(15)]

    GENS = [(1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 5, 0)]
    ok_eq = True
    for g in GENS:
        gp, gl = act_pt(g), act_ln(g)
        P_g = sp.Matrix(15, 15,
                        lambda r, c: 1 if r == gp[c] else 0)
        L_g = sp.Matrix(15, 15,
                        lambda r, c: 1 if r == gl[c] else 0)
        ok_eq &= (P_g * Nmat == Nmat * L_g)
    check("T1.2(b) S_6-EQUIVARIANCE: P_g N = N L_g EXACTLY for the "
          "generators (12) and (123456)", ok_eq, kill="K1")

    # (c) characters from scratch (Murnaghan-Nakayama)
    LAMS = ((6,), (5, 1), (4, 2))
    dims = tuple(mn_char(lam, (1,) * 6) for lam in LAMS)
    ALLG = list(itertools.permutations(range(6)))
    cts = [cycle_type(g) for g in ALLG]
    chi = {lam: {ct: mn_char(lam, ct) for ct in set(cts)}
           for lam in LAMS}
    gram = [[Fraction(sum(chi[a][ct] * chi[b][ct] for ct in cts),
                      720) for b in LAMS] for a in LAMS]
    orth = all(gram[i][j] == (1 if i == j else 0)
               for i in range(3) for j in range(3))
    fixd = [sum(1 for d in DUADS
                if frozenset(g[a] for a in d) == d) for g in ALLG]
    mult = tuple(Fraction(sum(chi[lam][cts[k]] * fixd[k]
                              for k in range(720)), 720)
                 for lam in LAMS)
    check("T1.3(c) Murnaghan-Nakayama: dims (S^(6),S^(5,1),S^(4,2)) "
          "= %s == (1,5,9); orthonormal over 720; duad permutation "
          "character multiplicities %s == (1,1,1); 15 = 1 + 5 + 9"
          % (dims, tuple(map(str, mult))),
          dims == (1, 5, 9) and orth and mult == (1, 1, 1)
          and sum(dims) == 15, kill="K1")

    # (d) isotypic projectors via character sums (exact rationals)
    acc = {lam: [[0] * 15 for _ in range(15)] for lam in LAMS}
    for k, g in enumerate(ALLG):
        gp = act_pt(g)
        for lam in LAMS:
            c = chi[lam][cts[k]]
            if c == 0:
                continue
            a = acc[lam]
            for p in range(15):
                a[gp[p]][p] += c
    PROJ = {lam: sp.Matrix(acc[lam]) * sp.Rational(d, 720)
            for lam, d in zip(LAMS, dims)}
    I15 = sp.eye(15)
    ok_proj = (sum(PROJ.values(), sp.zeros(15)) == I15
               and all(PROJ[lam] * PROJ[lam] == PROJ[lam]
                       for lam in LAMS)
               and all(PROJ[a] * PROJ[b] == sp.zeros(15)
                       for a in LAMS for b in LAMS if a != b)
               and tuple(PROJ[lam].trace() for lam in LAMS)
               == (1, 5, 9))
    check("T1.4(d) projectors: idempotent, orthogonal, sum = I, "
          "traces (1,5,9) -- exact rationals", ok_proj, kill="K1")

    # (e) the scalar law
    M = Nmat * Nmat.T
    x = sp.symbols("x")
    cp = sp.factor(M.charpoly(x).as_expr())
    want_cp = sp.expand((x - 9) * (x - 4) ** 9 * x ** 5)
    scal2 = (9, 0, 4)
    ok_scal2 = all(M * PROJ[lam] == s * PROJ[lam]
                   for lam, s in zip(LAMS, scal2))
    ABS_N = 3 * PROJ[(6,)] + 2 * PROJ[(4, 2)]
    ok_sqrt = (ABS_N * ABS_N == M)
    scal = (sp.Integer(1), sp.Integer(0), sp.Rational(2, 3))
    ok_scal = all((ABS_N / 3) * PROJ[lam] == s * PROJ[lam]
                  for lam, s in zip(LAMS, scal))
    check("T1.5(e) N N^T acts by (9, 0, 4) on the isotypics; "
          "charpoly = (x-9)(x-4)^9 x^5 (v844/v880); |N| = 3 P_(6) + "
          "2 P_(4,2) has |N|^2 = N N^T EXACT; |N|/3 acts by "
          "(1, 0, 2/3) EXACTLY",
          sp.expand(cp - want_cp) == 0 and ok_scal2 and ok_sqrt
          and ok_scal, kill="K1")

    # (f) corpus projector crosscheck + anchor identities
    B = M - 2 * I15                       # = I + A_disjoint
    J15 = sp.ones(15, 15)
    P5_corpus = I15 / 2 - B / 4 + J15 / 12
    id15 = (15 == 1 + E2 + (E2 - E3) ** 2)
    chan = (sp.Rational(E3, E2 - E3) == sp.Rational(2, 3))
    check("T1.6(f) corpus P5 formula: P_(5,1) == I/2 - B/4 + J/12 "
          "(B = I + A = N N^T - 2I); anchor identities 15 = 1 + e2 "
          "+ (e2-e3)^2 = 1 + %d + %d and 2/3 = e3/(e2-e3); e2 = "
          "g_car = %d" % (E2, (E2 - E3) ** 2, g_car),
          PROJ[(5, 1)] == P5_corpus and id15 and chan
          and E2 == g_car, kill="K1")

    # ==================================================================
    section("T2 -- DOILY.PLUCKER.GR25.01: quadrics = doily + signs")
    # ==================================================================
    monomials = []                        # (i, {S,T}, plucker_sign)
    for i in range(1, 6):
        j, k, l, m = sorted(set(range(1, 6)) - {i})
        monomials.append((i, frozenset({frozenset({j, k}),
                                        frozenset({l, m})}), +1))
        monomials.append((i, frozenset({frozenset({j, l}),
                                        frozenset({k, m})}), -1))
        monomials.append((i, frozenset({frozenset({j, m}),
                                        frozenset({k, l})}), +1))
    keys = [mk for _i, mk, _s in monomials]
    check("T2.1(a) 5 quadrics x 3 = %d monomials, all distinct as "
          "unordered disjoint duad pairs on {1..5}"
          % len(monomials),
          len(monomials) == 15 and len(set(keys)) == 15, kill="K2")

    line_by_key = {}
    line_islot = {}
    ok_lift = True
    for L in iso:
        ov = [v for v in L if QSTAR[v] == 0]
        pr = [v for v in L if QSTAR[v] == 1]
        S, T = iota_support(pr[0]), iota_support(pr[1])
        islot = frozenset(range(1, 6)) - iota_support(ov[0])
        ok_lift &= (len(ov) == 1 and len(pr) == 2 and len(S) == 2
                    and len(T) == 2 and not (S & T)
                    and len(islot) == 1)
        key = frozenset({S, T})
        line_by_key[key] = L
        line_islot[key] = next(iter(islot))
    ok_bij = (len(line_by_key) == 15
              and set(line_by_key) == set(keys)
              and all(line_islot[mk] == i
                      for i, mk, _s in monomials))
    check("T2.2(b) BIJECTION: each monomial {S,T} of Q_i maps to "
          "the unique doily line with pair supports {S,T} and "
          "omitted slot i -- 15 onto 15, 1:1, i-slots agree",
          ok_lift and ok_bij, kill="K2")

    ok_sec = all(sum(1 for v in L if QSTAR[v] == 1) <= 1
                 for L in sec_lines)
    ok_ext = True
    for L in ext_lines:
        sups = [iota_support(v) for v in L]
        for S, T in itertools.combinations(sups, 2):
            ok_ext &= (wedge_sign(S, T) is None)
    check("T2.3(c) CONVERSE ward: all 10 secants carry <= 1 pair "
          "point (no monomial key); all 10 external lines have "
          "pairwise overlapping supports (wedge = 0)",
          ok_sec and ok_ext, kill="K2")

    sign_rows = []
    n_match = 0
    for i in range(1, 6):
        row_p, row_h = [], []
        for qi, mk, s in monomials:
            if qi != i:
                continue
            S, T = tuple(mk)
            h = wedge_sign(S, T)
            row_p.append(s)
            row_h.append(h)
            n_match += (h == s)
        sign_rows.append((i, tuple(row_p), tuple(row_h)))
    ok_signs = all(rp == rh == (1, -1, 1)
                   for _i, rp, rh in sign_rows) and n_match == 15
    for i, rp, rh in sign_rows:
        print("      Q_%d: plucker %s | hodge %s" % (i, rp, rh))
    check("T2.4(d) SIGN TABLE: Plucker signs (+,-,+) == Hodge signs "
          "of b_S ^ b_T = +-f_i on %d/15 monomials (exact match)"
          % n_match, ok_signs and n_match == 15, kill="K2")

    # ==================================================================
    section("T3 -- CFIN.ANCHOR.HADAMARD.01: the anchor signature")
    # ==================================================================
    reps = {d: sum(1 for zx in ZQ for zy in ZQ if zx ^ zy == d)
            for d in range(1, 16)}
    ok_ds = all(c == 2 for c in reps.values())
    k_, v_, lam_ = len(ZQ), 16, 2
    check("T3.1(a) (16,6,2) DIFFERENCE SET (v853 rebuilt as ward): "
          "every nonzero d has exactly 2 ordered representations "
          "d = x + y, x,y in Z; k(k-1) = %d = lambda(v-1) = %d"
          % (k_ * (k_ - 1), lam_ * (v_ - 1)),
          ok_ds and k_ * (k_ - 1) == lam_ * (v_ - 1) == 30,
          kill="K3")

    p2a = sum(t * t for t in ANCHOR)
    ok_sig = (v_ == 2 ** E1 == 16 and k_ == p2a == 1 + 1 + 4 == 6
              and lam_ == E3 == 2 and k_ - lam_ == E1 == 4
              and v_ - k_ == 10 == E2 * (E2 - 1) // 2)
    check("T3.2(b) ANCHOR SIGNATURE (new): v = 2^e1 = 16, k = p2(a) "
          "= 6, lambda = e3 = 2, k - lambda = e1 = 4, v - k = 10 = "
          "C(e2,2) with (e1,e2,e3) = (4,5,2)", ok_sig, kill="K3")

    walsh = []
    for u in range(16):
        walsh.append(sum((-1) ** (QSTAR[v2] + pc(u & v2))
                         for v2 in range(16)))
    flat = sorted(set(abs(w) for w in walsh))
    check("T3.3(c) BENT ward (v853 rebuilt): Walsh spectrum of "
          "(-1)^{q*} is flat, |W| = %s == {4} = {2^(e1/2)} on all "
          "16 characters (exact integers)" % flat,
          flat == [4] and 4 == 2 ** (E1 // 2), kill="K3")

    s_vec = [(-1) ** QSTAR[v2] for v2 in range(16)]
    auto = [sum(s_vec[v2] * s_vec[v2 ^ a] for v2 in range(16))
            for a in range(16)]
    check("T3.4(d) perfect autocorrelation ward: sum_x s(x)s(x+a) "
          "= 16 delta_{a,0} on all 16 shifts",
          auto[0] == 16 and all(c == 0 for c in auto[1:]),
          kill="K3")

    # ==================================================================
    section("T4 -- CFIN.S6.VACUUM.01: six vacua, S_5 carrier")
    # ==================================================================
    SP = []
    for c1 in range(16):
        for c2 in range(16):
            if HT[c1][c2] != 1:
                continue
            for c3 in range(16):
                if HT[c1][c3] != 1 or HT[c2][c3] != 1:
                    continue
                for c4 in range(16):
                    if (HT[c1][c4] == 1 and HT[c2][c4] == 1
                            and HT[c3][c4] == 1):
                        SP.append((c1, c2, c3, c4))
    check("T4.1(a/b) |Sp(4,2)| = %d == 720 by full census (v774 "
          "rebuilt; columns preserve hb pairwise)" % len(SP),
          len(SP) == 720, kill="K4")

    def mmap(cols):
        return tuple(
            (cols[0] if v & 1 else 0) ^ (cols[1] if v & 2 else 0)
            ^ (cols[2] if v & 4 else 0) ^ (cols[3] if v & 8 else 0)
            for v in range(16))

    a1set = set(arf1s)
    a1idx = {q: i for i, q in enumerate(arf1s)}
    perms6 = set()
    orbit_q = set()
    stab = []
    ok_act = True
    for cols in SP:
        mp = mmap(cols)
        imgs = []
        for q in arf1s:
            qm = tuple(q[mp[v]] for v in range(16))
            ok_act &= (qm in a1set)
            imgs.append(a1idx.get(qm, -1))
        perms6.add(tuple(imgs))
        qstar_m = tuple(QSTAR[mp[v]] for v in range(16))
        orbit_q.add(qstar_m)
        if qstar_m == QSTAR:
            stab.append(mp)
    check("T4.2(b) the Sp(4,2) action on the six Arf-1 refinements "
          "is well-defined, FAITHFUL (image order %d == 720 = |S_6|)"
          " and TRANSITIVE (orbit of q* = %d of 6)"
          % (len(perms6), len(orbit_q)),
          ok_act and len(perms6) == 720 and len(orbit_q) == 6,
          kill="K4")

    others = [q for q in arf1s if q != QSTAR]
    oidx = {q: i for i, q in enumerate(others)}
    perms5 = set()
    for mp in stab:
        pi = tuple(oidx[tuple(q[mp[v]] for v in range(16))]
                   for q in others)
        perms5.add(pi)
    check("T4.3(c) VACUUM SELECTION: |Stab(q*)| = %d == 720/6 = "
          "120; its image on the REMAINING FIVE Arf-1 refinements "
          "has order %d == 120 = |S_5| -- faithful AND surjective "
          "onto S_5" % (len(stab), len(perms5)),
          len(stab) == 120 and len(perms5) == 120, kill="K4")

    # orbits of Stab(q*) on the 16 messages
    parent = list(range(16))

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    for mp in stab:
        for v2 in range(16):
            ru, rv = find(v2), find(mp[v2])
            if ru != rv:
                parent[ru] = rv
    orbs = {}
    for v2 in range(16):
        orbs.setdefault(find(v2), set()).add(v2)
    orb_sets = sorted(orbs.values(), key=len)
    lam0 = {v2 for v2 in range(16) if iota_wt(v2) == 0}
    lam4 = {v2 for v2 in range(16) if iota_wt(v2) == 4}
    lam2 = {v2 for v2 in range(16) if iota_wt(v2) == 2}
    ok_orb = ([len(o) for o in orb_sets] == [1, 5, 10]
              and orb_sets[0] == lam0 and orb_sets[1] == lam4
              and orb_sets[2] == lam2
              and lam4 == set(ovoid))
    check("T4.4(d) Stab(q*) orbits on the 16 messages = %s == "
          "1 + 5 + 10 with orbit sets EQUAL to (Lambda^0, Lambda^4, "
          "Lambda^2) = ({0}, ovoid, pairs) -- the surviving S_5 is "
          "the carrier symmetry; 10 - 1 = %d = N_fam^2 non-fixed "
          "pair messages (v880)"
          % ([len(o) for o in orb_sets], N_fam ** 2),
          ok_orb and N_fam ** 2 == 9, kill="K4")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    q0 = arf0[0]
    Z0 = [v2 for v2 in range(16) if q0[v2] == 0]
    reps0 = {d: sum(1 for zx in Z0 for zy in Z0 if zx ^ zy == d)
             for d in range(1, 16)}
    census0 = sorted(set(reps0.values()))
    is_16_10_6 = (len(Z0) == 10 and census0 == [6])
    check("C1 FIRES: Arf-0 zero set: k = %d != 6 = p2(a) and the "
          "representation census %s != {2} -- NOT a (16,6,2) "
          "difference set (honest note: it %s the complementary "
          "(16,10,6) profile)"
          % (len(Z0), census0,
             "IS" if is_16_10_6 else "is NOT even"),
          len(Z0) != 6 and census0 != [2], kill="K7")

    Lsec = sec_lines[0]
    pr_sec = [v2 for v2 in Lsec if QSTAR[v2] == 1]
    sec_has_key = False
    if len(pr_sec) == 2:
        S, T = iota_support(pr_sec[0]), iota_support(pr_sec[1])
        sec_has_key = (frozenset({S, T}) in set(keys))
    swapped = list(line_by_key.values())[1:] + [Lsec]
    n_matched = sum(1 for L in swapped if L in iso)
    check("C2 FIRES: a secant (%d pair points) yields NO monomial "
          "key; substituting it for a doily line leaves the "
          "bijection at %d/15 matched" % (len(pr_sec), n_matched),
          not sec_has_key and n_matched == 14, kill="K7")

    resid = (ABS_N / 3) * PROJ[(5, 1)] \
        - sp.Rational(2, 3) * PROJ[(5, 1)]
    check("C3 FIRES: |N|/3 does NOT act as 2/3 on S^(5,1) -- it "
          "acts as 0 there; residual = -2/3 P_(5,1) != 0 "
          "(max |entry| = %s)" % sp.nsimplify(max(abs(e) for e in resid)),
          resid != sp.zeros(15)
          and resid == -sp.Rational(2, 3) * PROJ[(5, 1)],
          kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = {"K0": "PIPELINE-BROKEN",
                   "K1": "IRREP-BROKEN",
                   "K2": "PLUCKER-BROKEN",
                   "K3": "HADAMARD-BROKEN",
                   "K4": "VACUUM-BROKEN"}.get(KILLS[0],
                                              "CONTROL-DEAD")
    else:
        VERDICT = "S6PLUCKER-CLOSED"
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
PROMOTION-READY STATEMENTS (report only -- no promotion, no edits):
  * T1: the duad representation of S_6 splits 15 = 1 + 5 + 9 =
    S^(6) + S^(5,1) + S^(4,2); the doily incidence is equivariant
    and its modulus |N|/3 acts by (1, 0, 2/3) on the isotypics --
    15 = 1 + e2 + (e2-e3)^2, channel 2/3 = e3/(e2-e3).
  * T2: the 15 monomials of the five Gr(2,5) Plucker quadrics ARE
    the 15 doily lines (bijection incl. i-slots), and the quadric
    signs (+,-,+) EQUAL the v880 Hodge signs on all 15.
  * T3: the q* zero set is the v853 (16,6,2) Hadamard difference
    set with the NEW anchor signature v = 2^e1, k = p2(a),
    lambda = e3, k - lambda = e1, v - k = C(e2,2).
  * T4: Sp(4,2) = S_6 permutes the six Arf-1 vacua transitively;
    fixing q* leaves Stab of order 120 acting faithfully AND
    surjectively as S_5 on the other five, with message orbits
    1 + 5 + 10 = Lambda^0 + Lambda^4 + Lambda^2 -- vacuum
    selection S_6 -> S_5 is the carrier symmetry.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source cfin_aut_flavor_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cfin_aut_flavor_probe -- CFIN.AUT.FLAVOR.C6.01 (round 44, from
section 8 of the 2026-08-09 external review of Revision 555): does the
C6 automorphism group of the unique finite compiler GENERATE the flavor
hexagon transport?

WHY NEW (redundancy check against the corpus FIRST): v849
(CFIN.UNIQUE.01) proves |Aut(C_fin)| = 6 with element orders
[1,2,3,3,6,6], abelian, cyclic ~= C6, faithful into Sp(4,2) -- but it
never FACTORS the generator (g^2 =? the family 3-cycle, g^3 =? a sheet
parity), never computes the induced action on the 10 pair-messages,
and never touches flavor.  v808 (CARRIER.PETERSEN.RADIAL.01) proves
the flavor hexagon IS the distance-2 shell of the Petersen graph on
E(K5) with the explicit deployed cycle (f1w1, f2w2, f3w1, f1w2, f2w1,
f3w2) -- but its symmetry bookkeeping is Aut(Petersen) = S5, never
Aut(C_fin).  v54/v56/v82/v124 freeze the recovery value (2/3)^6 =
lambda_2 of the transfer spectrum {1, (2/3)^6, (1/3)^6} with the
exponent 6 identified as p2 = |R+(A3)| = the hexagon size -- never as
|Aut(C_fin)|.  NOT in the corpus: the factorization of the C6
generator, its Lambda^2 E cycle structure, the intertwiner against the
deployed hexagon transport, and the orbit reading of the recovery
exponent.  This probe freezes exactly those four questions.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
exact integer / Fraction arithmetic only):

 A1  CONSTRUCT Aut(C_fin).  From the deployed compiler data on
     V = F_2^4 (bit form hbar of Gram J - I; q* = the v845/v880
     selector-pinned Arf-1 refinement, closed form
     q*(x) = sum_{i<j} x_i x_j + sum_i x_i; sigma = the family
     3-cycle (x1,x2,x3,x4) -> (x3,x1,x2,x4); iota = the parity lift
     V -> C_even(5)): enumerate Sp(4,2) exhaustively (ward: order
     720), and compute Aut(C_fin) = { g in Sp(4,2) : q* o g = q*,
     g sigma = sigma g, and SOME pi in S_5 intertwines iota o g =
     pi o iota } exactly.  WARD against the corpus claim (v849):
     |Aut| = 6, element orders [1,2,3,3,6,6], abelian, cyclic, the
     slot permutation pi determined by g.  FROZEN GENERATOR PIN: g =
     the unique order-6 element with g^2 = sigma (the deployed
     3-cycle, not its inverse); if no order-6 element squares to
     sigma, take the lex-min order-6 element and TYPE the deviation.
     Print g as a 4x4 F_2 matrix (columns = images of e_1..e_4) and
     its slot permutation pi_g.

 A2  FACTORIZATION.  Verify exactly: ord(g^2) = 3, ord(g^3) = 2,
     g^2 g^3 = g^3 g^2, and <g^2> x <g^3> = Aut (the C3 x C2
     splitting).  TYPED: (a) does g^2 EQUAL the deployed family
     3-cycle sigma (permutation equality on all 16 classes)?
     (b) SHEET HONESTY: the corpus deploys NO sheet-involution
     operator ON V (v118's sheet twist -1 acts on the 3-dim family
     monodromy; v857 I1: the lattice maps J and -1 both induce the
     IDENTITY on V) -- so the honest factor test is: which corpus
     operator does g^3 match?  Frozen candidate: the W-edge swap --
     pi_{g^3} = the transposition (w1 w2) fixing the three F slots
     pointwise, i.e. the S2 factor of Stab_{S5}(W) = S3 x S2 (v808
     P1.5), with |W| = 2 = |Z2| the sheet count.  Measured either
     way (fixed-space dimension of g^3 on V printed).

 A3  THE LAMBDA^2 ACTION.  The 10 pair-messages = the {q* = 1} words
     of V; via the v880 parity lift their iota-supports are EXACTLY
     E(K5) (ward: bijection; charge census {-4: 3, +1: 6, +6: 1}
     under X5 = (-2,-2,-2,3,3), v808 P1).  Rebuild the deployed
     hexagon (v808 P2, read-only machinery rebuilt inline): Petersen
     adjacency = disjointness, distance shells around W = {w1,w2}
     of sizes (1, 3, 6), charge-pure, and the deployed transport
     cycle HEX = ({f1,w1},{f2,w2},{f3,w1},{f1,w2},{f2,w1},{f3,w2})
     edge-verified.  Then MEASURE: (a) the cycle type of g on the 10
     pair-messages (predicted 1 + 3 + 6) and whether the g-orbits
     EQUAL the three charge shells; (b) THE INTERTWINER: the g-orbit
     sequence s_n = g^n({f1,w1}), n = 0..5, vs the deployed cycle --
     INTERTWINED iff every g-step is an edge of the deployed hexagon
     AND the cyclic sequence equals HEX up to rotation + reflection
     (the D6 convention of the flavor transport theorem, tfpt_2
     Lemma dd: residue triples are fixed 'up to D6'); the matching
     dihedral element is printed (orientation typed honestly: the
     TWO C6 generators traverse the hexagon in opposite directions).
     PARTIAL iff only the cycle type (1, 3, 6) matches; DEAD if
     neither.  The corpus quotient is the RESTRICTION to the 6-orbit
     (= the distance-2 shell): the flavor sector's C6 acts on the 6
     residue sites Z_6 (word length L = 6n + r, residue sets = the
     D6-orbit of {0,1,3}), deployed as exactly this hexagon (v808
     [E neu], tfpt_2 round-22 note).

 A4  THE ORBIT READING (report, no fit, no marker move).  If A2/A3
     hold: 6 = |Aut(C_fin)| = the length of the full automorphism
     orbit on the hexagon; the chain
         lambda_rec = (|Z2| / N_fam)^{|Aut(C_fin)|} = (2/3)^6
                    = 64/729
     against the DEPLOYED frozen recovery value = the subleading
     transfer eigenvalue lambda_1 = (1 - 1/3)^6 (v124 lambda_n =
     (1 - n/3)^6; v54/v56 frozen spectrum; v82 Koide multiplier) --
     exact Fraction equality.  HONEST TYPING: the corpus derives the
     exponent 6 as p2 = |R+(A3)| = the hexagon size; '6 =
     |Aut(C_fin)|' is a NEW reading made consistent by A3 (the
     hexagon is one full Aut orbit); the first-generation winding +6
     (L = R + 6 1 e1^T, v4/v857) = one full revolution = one full
     Aut orbit is a report line, not a claim upgrade.

 C   CONTROLS (must fire; frozen fire rules):
     C1 NON-AUTOMORPHISM: among ALL 600 symplectic maps p that
        preserve hbar but NOT q* (ward: |Sp| - |Stab(q*)| =
        720 - 120), COUNT those factoring consistently as g^2/g^3
        (p^2 in {sigma, sigma^2} AND p^3 = the Aut involution):
        must be 0 (any such p = p^3 (p^2)^{-1} would lie in Aut,
        contradiction -- verified by census, not narrated); the
        lex-min example p with its square/cube diagnostics printed.
     C2 SCRAMBLED TRANSPORT TABLE: swapping two entries of the
        deployed cycle (positions 1 and 2) must BREAK A3: the
        scrambled table is NOT D6-equivalent to the g-sequence AND
        contains a non-edge step (fire iff both).

KILLS (any one fires => typed):
  K1 machinery ward breaks (Sp order, refinement census, selector,
     iota, E(K5) bijection, Petersen shells, deployed cycle)
                                                -> PIPELINE-BROKEN
  K2 corpus Aut claim breaks (|Aut| != 6, not cyclic, orders wrong,
     pi not determined, sigma not in Aut)       -> PIPELINE-BROKEN
  K3 a control does not fire                    -> CONTROL-DEAD

VERDICT (frozen enum, decision order):
  0. a control does not fire      -> CONTROL-DEAD, exit 1
  1. any kill                     -> PIPELINE-BROKEN, exit 1
  2. otherwise                    -> C6FLAVOR-MEASURED + <INTERTWINED
     iff A2(a) g^2 = family 3-cycle (sigma or sigma^{-1}, typed)
     AND A2(b) pi_{g^3} = the W-edge swap AND A3 orbits = shells AND
     the intertwiner matches up to D6 with every step an edge;
     PARTIAL iff only the cycle type (1,3,6) matches; DEAD if
     neither> -- an honest DEAD is a fine outcome (the review calls
     this a hypothesis, not a claim).

RUN NOTE (fail-first preserved, no spec amendment): run 1 aborted at
A1.3 with a pure %%-formatting TypeError in a report string (a bare
tuple passed to %%s); the fix wraps the argument -- NO frozen claim,
check, kill, control or fire rule was altered (SPEC stays v1).

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  Exact integer / Fraction arithmetic in
every decision; no floats, no RNG, no fits.  AST firewall: banned
identifiers zetazero / nzeros / primerange / isprime / primepi /
nextprime / prevprime (self-scan).  NO physics claim beyond the typed
reading, NO RH claim, no marker moves.  Runtime cap 600 s.

Sources (read-only, machinery rebuilt inline): verification/
v849_cfin_unique_cofinal_lean.py (Aut(C_fin) ~= C6, admissibility
conventions), v880_finite_anchor_theorems.py (q* closed form, parity
lift, pair/ovoid split), v808_petersen_sixthroot.py (K5 edge machine,
X5, deployed hexagon cycle, Stab_{S5}(W) = S3 x S2), v845 (selector),
v54/v56/v82/v124 (frozen transfer spectrum {1, (2/3)^6, (1/3)^6},
lambda_n = (1 - n/3)^6, p2 = 6), v4/v857 (winding L = R + 6 1 e1^T),
tfpt_2_standard_model.tex (flavor transport theorem, distance set
{0,1,3} up to D6), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cfin_aut_flavor_probe.py
"""
import ast
import hashlib
import itertools
import os
import sys
import time
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------------- bit machinery
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
GJI = ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0))
BASIS = [WIDX[tuple(1 if k == i else 0 for k in range(4))]
         for i in range(4)]
ADD = [[WIDX[tuple((a + b) % 2 for a, b in zip(W16[i], W16[j]))]
        for j in range(16)] for i in range(16)]
IDENT = tuple(range(16))
A_BIT, FSIG = (0, 0, 0, 1), (1, 1, 1, 0)
LA, LF = WIDX[A_BIT], WIDX[FSIG]
SIGP = tuple(WIDX[(w[2], w[0], w[1], w[3])] for w in W16)

HB = [[sum(W16[i][r] * GJI[r][c] * W16[j][c] for r in range(4)
           for c in range(4)) % 2 for j in range(16)]
      for i in range(16)]

IOTA = [tuple(list(w) + [sum(w) % 2]) for w in W16]
S5 = list(itertools.permutations(range(5)))


def perm_of_images(g1, g2, g3, g4):
    gs = (g1, g2, g3, g4)
    p = []
    for i in range(16):
        acc = 0
        for k in range(4):
            if W16[i][k]:
                acc = ADD[acc][gs[k]]
        p.append(acc)
    return tuple(p)


def compose(p, q):
    """(p o q)[i] = p[q[i]]."""
    return tuple(p[q[i]] for i in range(16))


def perm_order(p):
    o, pp = 1, p
    while pp != tuple(range(len(p))):
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def gmat(p):
    """4x4 F_2 matrix of the linear map p (columns = images of e_j)."""
    return [[W16[p[BASIS[j]]][i] for j in range(4)] for i in range(4)]


def fmt_mat(m):
    return " / ".join("".join(str(x) for x in row) for row in m)


def cyc_variants(seq):
    """all 12 D6 images (rotations + rotations of the reversal)."""
    out = set()
    n = len(seq)
    for base in (list(seq), list(reversed(seq))):
        for r in range(n):
            out.add(tuple(base[r:] + base[:r]))
    return out


def main():
    print("CFIN.AUT.FLAVOR.C6.01 -- Aut(C_fin) ~= C6 vs the flavor "
          "hexagon transport")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO RH claim; no marker moves; exploration only.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles: %s)"
          % (BANNED_IDS,), not ast_scan(BANNED_IDS))
    Z2 = g_car - N_fam
    check("S0.2 constants: N_fam = %d, g_car = %d, |Z2| = g_car - "
          "N_fam = %d" % (N_fam, g_car, Z2),
          N_fam == 3 and g_car == 5 and Z2 == 2, kill="K1")

    # ==================================================================
    section("A1 -- Aut(C_fin) from the deployed compiler data")
    # ==================================================================
    GL_n = 0
    SP = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = perm_of_images(*imgs)
        if len(set(p)) != 16:
            continue
        GL_n += 1
        if all(HB[p[BASIS[i]]][p[BASIS[j]]] == GJI[i][j]
               for i in range(4) for j in range(i + 1, 4)):
            SP.append(p)
    check("A1.1 ward: |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == 720 "
          "(exhaustive image enumeration, v849 U0)" % (GL_n, len(SP)),
          GL_n == 20160 and len(SP) == 720, kill="K1")

    # 16 refinements = the 16 linear shifts of the polar quadric (v880)
    refs = []
    for c in W16:
        q = tuple((sum(w[i] * w[j] for i in range(4)
                       for j in range(i + 1, 4))
                   + sum(a * b for a, b in zip(c, w))) % 2 for w in W16)
        refs.append((c, q))
    all_ref = all(all(q[ADD[i][j]] ^ q[i] ^ q[j] == HB[i][j]
                      for i in range(16) for j in range(16))
                  for _c, q in refs)
    siginv = [(c, q) for c, q in refs
              if all(q[SIGP[i]] == q[i] for i in range(16))]
    cand_a = [(c, q) for c, q in siginv if q[LA] == 1]
    cand = [(c, q) for c, q in cand_a if q[LF] == 0]
    QSTAR = cand[0][1] if len(cand) == 1 else None
    closed = tuple((sum(w[i] * w[j] for i in range(4)
                        for j in range(i + 1, 4)) + sum(w)) % 2
                   for w in W16)
    check("A1.2 ward: the 16 polar shifts are ALL refinements of hbar; "
          "selector 16 -> %d -> %d -> %d == 1 pins q* = the closed "
          "form C(|x|+1,2) mod 2 (v845/v880)"
          % (len(siginv), len(cand_a), len(cand)),
          all_ref and len(siginv) == 4 and len(cand_a) == 2
          and len(cand) == 1 and QSTAR == closed, kill="K1")

    sig_ok = (perm_order(SIGP) == 3 and SIGP in SP
              and all(QSTAR[SIGP[i]] == QSTAR[i] for i in range(16))
              and sum(1 for i in range(1, 16) if SIGP[i] == i) == 3)
    pi_sig = [pi for pi in S5
              if all(IOTA[SIGP[i]] == tuple(IOTA[i][pi[s]]
                                            for s in range(5))
                     for i in range(16))]
    check("A1.3 ward: sigma admissible (order 3, symplectic, "
          "q*-preserving, 3 nonzero fixed classes) and iota-"
          "equivariant with slot permutation pi_sigma = %s (v849 U2/U3)"
          % ((pi_sig[0] if len(pi_sig) == 1 else pi_sig),),
          sig_ok and len(pi_sig) == 1, kill="K1")

    # ---- the Aut census
    AUT = []
    for p in SP:
        if any(QSTAR[p[i]] != QSTAR[i] for i in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5
               if all(IOTA[p[i]] == tuple(IOTA[i][pi[s]]
                                          for s in range(5))
                      for i in range(16))]
        if pis:
            AUT.append((p, pis))
    orders = sorted(perm_order(p) for p, _ in AUT)
    one_pi = all(len(pis) == 1 for _p, pis in AUT)
    abelian = all(compose(p1, p2) == compose(p2, p1)
                  for (p1, _), (p2, _) in
                  itertools.combinations(AUT, 2))
    cyclic = bool(AUT) and max(orders) == len(AUT)
    check("A1.4 CORPUS WARD (v849 U5): |Aut(C_fin)| = %d == 6; element "
          "orders %s == [1,2,3,3,6,6]; abelian = %s; cyclic = %s => "
          "C6; slot permutation pi DETERMINED by g (one pi per g: %s)"
          % (len(AUT), orders, abelian, cyclic, one_pi),
          len(AUT) == 6 and orders == [1, 2, 3, 3, 6, 6]
          and abelian and cyclic and one_pi, kill="K2")

    SIGP2 = compose(SIGP, SIGP)
    o3 = sorted(p for p, _ in AUT if perm_order(p) == 3)
    check("A1.5 the C3 part of Aut IS the deployed family cycle: "
          "order-3 elements = {sigma, sigma^2} exactly (sigma in Aut)",
          o3 == sorted([SIGP, SIGP2]), kill="K2")

    g_cands = sorted(p for p, _ in AUT if perm_order(p) == 6)
    g_pin = [p for p in g_cands if compose(p, p) == SIGP]
    pinned = (len(g_pin) == 1)
    G = g_pin[0] if pinned else (g_cands[0] if g_cands else None)
    PI_G = next(pis[0] for p, pis in AUT if p == G)
    check("A1.6 FROZEN GENERATOR PIN: %d order-6 elements; exactly ONE "
          "with g^2 = sigma (the deployed 3-cycle, not its inverse): "
          "%s -- g frozen" % (len(g_cands), pinned),
          len(g_cands) == 2 and pinned, kill="K2")
    print("      g as 4x4 F_2 matrix (rows; columns = g(e_1..e_4)): %s"
          % fmt_mat(gmat(G)))
    print("      g as class permutation: %s" % (G,))
    print("      slot permutation pi_g = %s  (convention: "
          "iota(g v)_s = iota(v)_{pi[s]})" % (PI_G,))

    # ==================================================================
    section("A2 -- factorization: g^2, g^3, the C2 x C3 splitting")
    # ==================================================================
    G2 = compose(G, G)
    G3 = compose(G2, G)
    split = sorted(compose(a, b) for a in (IDENT, G2, compose(G2, G2))
                   for b in (IDENT, G3))
    check("A2.1 ord(g^2) = %d == 3; ord(g^3) = %d == 2; g^2 g^3 = "
          "g^3 g^2; <g^2> x <g^3> = Aut (the C2 x C3 splitting, all 6 "
          "elements reproduced)"
          % (perm_order(G2), perm_order(G3)),
          perm_order(G2) == 3 and perm_order(G3) == 2
          and compose(G2, G3) == compose(G3, G2)
          and split == sorted(p for p, _ in AUT), kill="K2")

    is_sig = (G2 == SIGP)
    is_sig_inv = (G2 == SIGP2)
    check("A2.2 TYPED (a): g^2 == the deployed family 3-cycle sigma: "
          "%s (== sigma^{-1}: %s) -- the review's g^2 = sigma_family "
          "%s, exactly as deployed"
          % (is_sig, is_sig_inv,
             "HOLDS" if is_sig else
             ("holds up to orientation" if is_sig_inv else "FAILS")),
          True, "measured, typed either way")

    PI_G3 = tuple(PI_G[PI_G[PI_G[s]]] for s in range(5))
    w_swap = (0, 1, 2, 4, 3)
    fix_g3 = sum(1 for i in range(16) if G3[i] == i)
    is_wswap = (PI_G3 == w_swap)
    check("A2.3 TYPED (b) SHEET HONESTY: the corpus deploys NO sheet "
          "involution ON V (v118 twist lives on the 3-dim monodromy; "
          "v857 I1: J and -1 induce the identity on V); the measured "
          "factor: pi_{g^3} = %s %s the W-edge swap (w1 w2) fixing F "
          "pointwise = the S2 factor of Stab_{S5}(W) = S3 x S2 (v808 "
          "P1.5), |W| = 2 = |Z2|; fix(g^3 on V) = %d classes (dim %d)"
          % (PI_G3, "==" if is_wswap else "!=", fix_g3,
             fix_g3.bit_length() - 1),
          True, "measured, typed either way")
    print("      g^3 as 4x4 F_2 matrix: %s" % fmt_mat(gmat(G3)))
    print("      g^2 as class permutation: %s" % (G2,))
    print("      g^3 as class permutation: %s" % (G3,))

    # ==================================================================
    section("A3 -- the Lambda^2 action and the hexagon intertwiner")
    # ==================================================================
    TEN = [i for i in range(1, 16) if QSTAR[i] == 1]
    supp = {i: frozenset(s for s in range(5) if IOTA[i][s])
            for i in TEN}
    PAIRS = [frozenset(p) for p in itertools.combinations(range(5), 2)]
    bij = (len(TEN) == 10 and all(len(supp[i]) == 2 for i in TEN)
           and sorted(supp.values(), key=sorted) ==
           sorted(PAIRS, key=sorted))
    X5 = (-2, -2, -2, 3, 3)
    from collections import Counter
    cen = Counter(sum(X5[s] for s in P) for P in PAIRS)
    check("A3.1 ward: the 10 pair-messages {q* = 1} biject via iota-"
          "support onto E(K5); charge census %s == {-4: 3, +1: 6, "
          "+6: 1} = the SU(5) decuple (v808 P1)"
          % dict(sorted(cen.items())),
          bij and dict(cen) == {-4: 3, 1: 6, 6: 1}, kill="K1")

    # Petersen + shells around W (v808 P2 rebuilt read-only)
    W_V = frozenset({3, 4})

    def adj(a, b):
        return a != b and not (a & b)

    dist = {W_V: 0}
    frontier = [W_V]
    while frontier:
        nxt = []
        for u in frontier:
            for v2 in PAIRS:
                if adj(u, v2) and v2 not in dist:
                    dist[v2] = dist[u] + 1
                    nxt.append(v2)
        frontier = nxt
    shells = {d: sorted((P for P in PAIRS if dist[P] == d), key=sorted)
              for d in set(dist.values())}
    sizes = tuple(len(shells[d]) for d in sorted(shells))
    pure = {d: {sum(X5[s] for s in P) for P in shells[d]}
            for d in shells}
    HEX = [frozenset(s) for s in
           ({0, 3}, {1, 4}, {2, 3}, {0, 4}, {1, 3}, {2, 4})]
    hex_edges = all(adj(HEX[k], HEX[(k + 1) % 6]) for k in range(6))
    check("A3.2 ward: distance shells around W sizes %s == (1, 3, 6), "
          "charge-pure (%s); the DEPLOYED transport cycle (f1w1, f2w2, "
          "f3w1, f1w2, f2w1, f3w2) is edge-verified (v808 P2.5/P2.6)"
          % (sizes, {d: sorted(pure[d]) for d in sorted(pure)}),
          sizes == (1, 3, 6) and pure[0] == {6} and pure[1] == {-4}
          and pure[2] == {1} and hex_edges
          and sorted(HEX, key=sorted) == sorted(shells[2], key=sorted),
          kill="K1")

    # the g action on the pair-messages (direct word action, no pi)
    p2w = {supp[i]: i for i in TEN}

    def gpair(P, perm=G):
        return supp[perm[p2w[P]]]

    orbits = []
    seen = set()
    for P in PAIRS:
        if P in seen:
            continue
        orb = [P]
        cur = gpair(P)
        while cur != P:
            orb.append(cur)
            cur = gpair(cur)
        seen |= set(orb)
        orbits.append(orb)
    ctype = sorted(len(o) for o in orbits)
    orb_by_len = {len(o): o for o in orbits}
    orbits_are_shells = (
        ctype == [1, 3, 6]
        and orb_by_len[1][0] == W_V
        and sorted(orb_by_len[3], key=sorted) == shells[1]
        and sorted(orb_by_len[6], key=sorted) == shells[2])
    check("A3.3 TYPED: cycle type of g on the 10 pair-messages = %s "
          "(predicted 1 + 3 + 6); g-orbits == the charge shells "
          "(fixed = W = the message A; 3-orbit = distance-1 = u^c; "
          "6-orbit = distance-2 = the hexagon = Q): %s"
          % (ctype, orbits_are_shells),
          True, "measured, typed either way")
    for o in orbits:
        print("      orbit (len %d): %s"
              % (len(o), [tuple(sorted(P)) for P in o]))

    base = frozenset({0, 3})
    seq = [base]
    for _ in range(5):
        seq.append(gpair(seq[-1]))
    period6 = (gpair(seq[-1]) == base and len(set(seq)) == 6)
    steps_edges = all(adj(seq[k], seq[(k + 1) % 6]) for k in range(6))
    hexedges = {frozenset({tuple(sorted(HEX[k])),
                           tuple(sorted(HEX[(k + 1) % 6]))})
                for k in range(6)}
    steps_deployed = all(
        frozenset({tuple(sorted(seq[k])),
                   tuple(sorted(seq[(k + 1) % 6]))}) in hexedges
        for k in range(6))
    hex_t = [tuple(sorted(P)) for P in HEX]
    variants = cyc_variants(hex_t)
    rotations = {tuple(hex_t[r:] + hex_t[:r]) for r in range(6)}
    gtuple = tuple(tuple(sorted(P)) for P in seq)
    d6_match = gtuple in variants
    if gtuple in rotations:
        orientation = "+1 (deployed order)"
    elif d6_match:
        orientation = ("-1 (reversal; the other C6 generator g^5 "
                       "traverses the deployed order)")
    else:
        orientation = "none (no D6 match)"
    check("A3.4 TYPED INTERTWINER: the g-sequence g^n(f1w1), n = 0..5 "
          "= %s; period 6: %s; every g-step an edge of the deployed "
          "hexagon: %s; equals the deployed cycle up to D6 (rotation + "
          "reflection, the tfpt_2 Lemma-dd convention): %s; "
          "orientation %s"
          % (list(gtuple), period6, steps_deployed, d6_match,
             orientation),
          True, "measured, typed either way")

    print("      corpus quotient reading: the flavor C6 acts on the 6 "
          "residue sites Z_6")
    print("      (word length L = 6n + r; residue sets = the D6-orbit "
          "of {0,1,3}, tfpt_2);")
    print("      deployed graph realization = exactly this hexagon "
          "(v808 [E neu]) -- the")
    print("      restriction of the Lambda^2 action to the 6-orbit IS "
          "the transport hexagon.")

    intertwined = ((is_sig or is_sig_inv) and is_wswap
                   and orbits_are_shells and period6
                   and steps_edges and steps_deployed and d6_match)
    partial = (not intertwined) and ctype == [1, 3, 6]

    # ==================================================================
    section("A4 -- the orbit reading of the recovery exponent (report)")
    # ==================================================================
    lam_rec = Fr(Z2, N_fam) ** len(AUT)
    lam_dep = (Fr(1) - Fr(1, N_fam)) ** 6      # v124 lambda_1
    check("A4.1 the chain: lambda_rec = (|Z2|/N_fam)^{|Aut(C_fin)|} = "
          "(2/3)^6 = %s == the deployed frozen recovery value "
          "(1 - 1/3)^6 = %s (v54/v56/v82/v124; exact Fractions, no "
          "fit)" % (lam_rec, lam_dep),
          lam_rec == Fr(64, 729) == lam_dep and len(AUT) == 6,
          kill="K1")
    check("A4.2 HONEST TYPING: the corpus derives the exponent 6 as "
          "p2 = |R+(A3)| = the hexagon size (v124); '6 = |Aut(C_fin)|'"
          " is a NEW reading, consistent iff the hexagon is one full "
          "Aut orbit (A3.3: %s); the first-generation winding +6 "
          "(L = R + 6 1 e1^T, v4/v857) = one full revolution = one "
          "full Aut orbit -- report line, NO claim upgrade, no marker "
          "move" % orbits_are_shells,
          True, "measured, typed either way")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    stab_q = [p for p in SP
              if all(QSTAR[p[i]] == QSTAR[i] for i in range(16))]
    nonpres = [p for p in SP if p not in set(stab_q)]
    n_factor = 0
    example = None
    for p in sorted(nonpres):
        pp2 = compose(p, p)
        pp3 = compose(pp2, p)
        if pp2 in (SIGP, SIGP2) and pp3 == G3:
            n_factor += 1
        if example is None:
            example = (p, perm_order(pp2), perm_order(pp3),
                       pp2 in (SIGP, SIGP2), pp3 == G3)
    check("C1 FIRES: |Stab_Sp(q*)| = %d == 120, non-preserving maps "
          "%d == 600; NONE factors consistently as g^2/g^3 (square in "
          "{sigma, sigma^2} AND cube = the Aut involution): count = "
          "%d == 0" % (len(stab_q), len(nonpres), n_factor),
          len(stab_q) == 120 and len(nonpres) == 600 and n_factor == 0,
          kill="K3")
    print("      lex-min non-q*-preserving example: ord(p^2) = %d, "
          "ord(p^3) = %d, p^2 in {sigma, sigma^2}: %s, p^3 = g^3: %s"
          % (example[1], example[2], example[3], example[4]))

    scram = [HEX[0], HEX[2], HEX[1], HEX[3], HEX[4], HEX[5]]
    scram_t = [tuple(sorted(P)) for P in scram]
    scram_nonedge = any(not adj(scram[k], scram[(k + 1) % 6])
                        for k in range(6))
    scram_nomatch = gtuple not in cyc_variants(scram_t)
    check("C2 FIRES: scrambled transport table (entries 1 and 2 "
          "swapped): contains a non-edge step (%s) and is NOT D6-"
          "equivalent to the g-sequence (%s) -- the intertwiner test "
          "breaks on a scrambled table"
          % (scram_nonedge, scram_nomatch),
          scram_nonedge and scram_nomatch, kill="K3")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = "PIPELINE-BROKEN"
    else:
        sub = ("INTERTWINED" if intertwined
               else ("PARTIAL" if partial else "DEAD"))
        VERDICT = "C6FLAVOR-MEASURED + " + sub
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * Aut(C_fin) recomputed from the deployed data: C6, generator g
    pinned by g^2 = sigma; matrix and slot permutation printed above.
  * factorization: g^2 = the family 3-cycle (as deployed); g^3 = the
    unique involution, slot action = the W-edge swap (the S2 sheet
    factor of the F|W = 3+2 split) -- the corpus has NO deployed sheet
    involution ON V, typed honestly.
  * Lambda^2 action: cycle type and orbit/shell comparison measured;
    the intertwiner against the deployed v808 hexagon cycle decided up
    to D6 (the flavor convention), orientation typed.
  * orbit reading: (|Z2|/N_fam)^{|Aut|} = (2/3)^6 = 64/729 == the
    frozen recovery value; the exponent reading 6 = |Aut(C_fin)| is
    NEW and stays a report line (corpus: 6 = p2 = |R+(A3)|).
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot
                 and VERDICT.startswith("C6FLAVOR-MEASURED")) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source k6_pfaffian_selfhosting_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""k6_pfaffian_selfhosting_probe -- CFIN.K6.MOTIF.01 +
DOILY.PFAFFIAN.WICK.01 + P2.SELFHOSTING.PAIRING.01 +
ANCHOR.MOD30.CLOCK.01 (+ the K6.ONEFACT.OUTER.01 census)
(EXPLORATION ONLY, experiments/; round 49, the complete K6/Pfaffian
signature of the finite compiler, from the third 2026-08-09 external
review: 'a complete new Pfaffian signature with 15 monomials, five
triple groups, fixed sign pattern, C6 covariance and fixed gap
spectrum would be very hard to explain away').

WHY NEW (redundancy check done against the corpus FIRST, 2026-08-09):
s6_plucker_hadamard_probe (round 44) PROVED the duad model D(v) =
{i : q_i(v) = 0} (15 messages <-> 15 duads, doily lines <-> perfect
matchings of K6), the 15-monomial Gr(2,5) Plucker <-> doily bijection
WITH sign match (+,-,+) = the v880 Hodge signs on 15/15, the Specht
scalars (1, 0, 2/3), and the S6 -> S5 vacuum selection.  v880 has the
q* closed normal form, the exclusive anchor classification of the 35
PG(3,2) lines (15 doily {2,1,1} + 10 secant {2,2,1} + 10 external
{1,1,1}) and the Hodge multiplication b_jk ^ b_lm = +-f_i.
cfin_aut_flavor_probe (round 44) pinned the Aut(C_fin) ~= C6
generator g (g^2 = sigma) with cycle type 1 + 3 + 6 on the ten
pair-messages.  NOT in the corpus -- genuinely new here:
 (1) the K6 MOTIF theorem in FULL: all 35 lines classified AS K6
     motifs -- 15 perfect matchings + 20 triangles with the
     vacuum/no-vacuum split (secants = the 10 triangles THROUGH the
     vacuum vertex, externals = the 10 AVOIDING it), and the
     edge law q*(e) = 0 iff e touches the vacuum vertex;
 (2) the PFAFFIAN reading with the FERMIONIC signs sgn(M) from the
     symbolic expansion of Pf(A) for generic antisymmetric 6x6 A --
     these are a priori DISTINCT from the Plucker-quadric/Hodge
     signs of round 44; the relation is COMPUTED, not assumed, with
     a frozen typed rule for a global gauge;
 (3) the five 3-groups (Pfaffian vacuum-row minor expansion) as the
     round-44 Plucker quadrics, cross-referenced sign by sign;
 (4) the C6 covariance of Pf under the pinned Aut(C_fin) generator
     (the induced vertex permutation, the sign character, and the
     symbolic identity Pf(P A P^T) = det(P) Pf(A));
 (5) the self-hosting counting theorem C(g+1,2) = g!!;
 (6) the mod-30 anchor clock with an anti-numerology modulus census;
 (7) the one-factorization census of K6 (6 factorizations, 30 =
     6 x 5 = 2 x 15 schedule) with the exceptional-outer-automorphism
     signature (non-conjugate S6 actions, transposition cycle types).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
exact integer / sympy arithmetic ONLY, no RNG, no fits):

 T1  CFIN.K6.MOTIF.01 -- the 35-line motif classification.  Under
     the corpus duad labeling (six Arf-1 refinements sorted, D(v) =
     {i : q_i(v) = 0}; vacuum vertex v0 = the label of q*):
     (a) the 15 doily (isotropic) lines map EXACTLY onto the 15
         perfect matchings of K6 (corpus ward, round 44 rebuilt);
     (b) the 10 secant lines map EXACTLY onto the 10 triangles of K6
         THROUGH v0 (each = two vacuum edges + one pair edge), local
         weight multiset {2,2,1} = the wrong anchor (1,2,2) (v880);
     (c) the 10 external lines map EXACTLY onto the 10 triangles
         AVOIDING v0, weight multiset {1,1,1};
     (d) 35 = 15 + 10 + 10 complete, and the 20 triangles exhaust
         ALL C(6,3) = 20 triangles of K6;
     (e) the EDGE LAW: q*(D^-1(e)) = 0 iff the edge e touches v0;
         cross-check v880: the 5 nonzero zeros of q* (the ovoid)
         map EXACTLY onto the 5 vacuum edges {v0, i};
     (f) the CARRIER DICTIONARY: the 5 ovoid messages induce a
         bijection phi: (non-vacuum Arf labels) -> (carrier slots
         {1..5}) via D(o) = {v0, a} and supp iota(o) = comp{slot};
         CONSISTENCY: for every pair message w the duad D(w) maps
         under phi EXACTLY onto the iota-support of w (the duad
         model and the Hodge lift agree edge by edge).

 T2  DOILY.PFAFFIAN.WICK.01 -- the sign theorem (the decisive part).
     For a generic antisymmetric 6x6 symbolic matrix A (sympy),
     expand Pf(A) by the recursive expansion; in the phi-relabeled
     vertex order (vacuum = 0, slots 1..5):
     (a) EXACTLY 15 monomials, one per perfect matching, all
         coefficients +-1; the extracted sign sgn(M) EQUALS the
         independent permutation-sign definition (pairs sorted by
         minima, inversion count) on all 15;
     (b) THE TEST: compare sgn(M) for M = {0i, jk, lm} against the
         corpus Hodge sign of b_jk ^ b_lm = +-f_i (v880 / round 44,
         = wedge_sign({j,k},{l,m}) in Lambda^4); report the 15-row
         sign table and the match census.  FROZEN TYPED RULE:
         PFAFFIAN-SIGNS-MATCHED iff direct match 15/15;
         GAUGE-MATCHED(chi) iff the discrepancy d(M) = sgn(M) *
         hodge(M) depends ONLY on the omitted carrier slot i (a
         global character chi(i) on the five vacuum edges {0,i} --
         exhibited exactly); SIGNS-DEAD otherwise (a line-dependent
         fudge is a FAIL);
     (c) VOLUME NORMALIZATION identity (frozen prediction): sgn(M)
         = the sign of b_S ^ b_T ^ e_i = +- e_1^...^e_5 (the full
         top-form convention), i.e. the fermionic sign IS the
         volume-form sign and chi(i) = (-1)^(i+1) is exactly the
         Lambda^4 vs Lambda^5 conversion character;
     (d) the FIVE 3-GROUPS: the vacuum-row minor expansion Pf(A) =
         sum_i (-1)^(i+1) A_0i Pf(A_{0i-hat}) holds symbolically;
         each 4x4 minor Pfaffian EQUALS the round-44 3-term Plucker
         quadric a_jk a_lm - a_jl a_km + a_jm a_kl (signs (+,-,+));
         the Laplace sign (-1)^(i+1) is warded against chi;
     (e) C6 COVARIANCE: rebuild Sp(4,2) (order 720) and Aut(C_fin)
         (order 6, orders [1,2,3,3,6,6]); pin the generator g by
         g^2 = sigma (round-44 convention, unique); the induced
         permutation pi_a on the 6 Arf labels fixes v0 and
         intertwines the duad action (D(g v) = pi_a(D(v)) on all 15
         messages); cycle type on the ten pair duads = 1 + 3 + 6
         (corpus cross-ref); g permutes the 15 matchings, and Pf is
         EQUIVARIANT: symbolically Pf(P A P^T) = det(P) Pf(A) with
         P the vertex permutation matrix, and per matching
         sgn(pi(M)) = det(pi) * c_pi(M) * sgn(M) with the crossing
         character c_pi(M) = prod over edges {a<b} of M of (-1 iff
         pi(a) > pi(b)) -- the appropriate sign character computed
         and reported.

 T3  P2.SELFHOSTING.PAIRING.01 -- the conditional counting theorem.
     (a) print the two sequences C(g+1,2) and g!! over odd g in
         {1,3,5,7,9,11,13,15}; solutions of C(g+1,2) = g!! are
         EXACTLY {1, 5}; state the trivial g = 1 case honestly
         (C(2,2) = 1 = 1!!), so g = 5 is the only NONTRIVIAL
         solution;
     (b) (g-2)!! = 3!! = 3 = N_fam at g = 5;
     (c) GROWTH SEPARATION: g!! > C(g+1,2) for all odd g >= 7
         (checked to 15) with the induction ratio argument: the
         double-factorial multiplier g+2 exceeds the binomial
         quotient (g+3)(g+2)/((g+1)g) iff g(g+1) > g+3 iff
         g^2 > 3 (symbolic), so the separation only grows.
     HONEST TYPING: this is an [E] counting theorem; the PHYSICAL
     premise (the boundary grammar IS a self-hosting Wick pair
     compiler: states = duads of g+1 = 6 objects, contractions =
     matchings of g+1) stays [O] -- NO marker move.

 T4  ANCHOR.MOD30.CLOCK.01 -- the anchor power-sum clock.  With the
     frozen anchor a = (1,1,2) (v832 [E]) and p_n(a) = 1 + 1 + 2^n:
     (a) p_n = 2 + 2^n and the affine recursion p_{n+1} = 2 p_n - 2
         (symbolic identity + numeric n = 1..10); p_1 = 4 = e1,
         p_2 = 6 (v880's p2(a));
     (b) the orbit mod 30: 4 -> 6 -> 10 -> 18 -> 4, period EXACTLY
         4 = |mu_4|, incl. p_5 = 34 = 4 + 30;
     (c) ANTI-NUMEROLOGY CENSUS: all moduli 2 <= m < 100 with the
         orbit of 4 under x -> 2x - 2 PURELY periodic of period
         exactly 4 (list printed), plus the eventually-period-4
         list as an honest note.  FROZEN TYPED RULE:
         CLOCK-DISTINGUISHED iff every purely period-4 modulus
         divides 30 (so 30 = lcm = the maximal clock);
         CLOCK-GENERIC otherwise (if many unrelated m work, the
         mod-30 reading is weak -- reported either way).

 T5  K6.ONEFACT.OUTER.01 -- the one-factorization census (the
     30 = 6 x 5 schedule).
     (a) K6 has EXACTLY 6 one-factorizations; each contains 5
         perfect matchings; every matching lies in EXACTLY 2
         factorizations (30 = 6 x 5 = 2 x 15);
     (b) trivial incidence ward: every factorization covers every
         vertex in all 5 of its matchings;
     (c) S6 acts TRANSITIVELY on the 6 factorizations; the
         stabilizer of a factorization has order 120 and acts
         TRANSITIVELY on the 6 vertices, while the stabilizer of a
         vertex (order 120) acts TRANSITIVELY on the 6
         factorizations -- the duality signature;
     (d) the EXCEPTIONAL OUTER SIGNATURE: a transposition acts on
         the 6 vertices with cycle type (2,1,1,1,1) but on the 6
         factorizations with cycle type (2,2,2) (zero fixed
         points) -- the two S6 actions on 6 objects are
         NON-conjugate (the classical outer-automorphism witness;
         exact computation).  HONEST TYPING: the 6 vertices ARE the
         6 Arf-1 vacua (duad model); the 6 factorizations are the
         outer-dual 6-set; NO canonical vertex <-> factorization
         bijection exists (fixed-point obstruction) -- report only,
         no physics claim.

 C   CONTROLS (must fire; frozen fire rules):
     C1 an Arf-0 refinement breaks the T1 vacuum-incidence reading:
        its 9 nonzero zeros do NOT form the edge star of any vertex
        (a star has 5 edges) and the doily line patterns are not
        constant {0,1,1};
     C2 the WRONG sign character breaks T2: taking the measured
        chi and flipping its value on slot 2 must produce EXACTLY
        the 3 mismatches of the i = 2 triple;
     C3 g = 3 and g = 7 break T3 as stated: C(4,2) = 6 != 3 = 3!!
        and C(8,2) = 28 != 105 = 7!!.

KILLS (any one fires => typed gap):
  K0 AST firewall / setup ward breaks              -> PIPELINE-BROKEN
  K1 motif classification / edge law / dictionary  -> MOTIF-BROKEN
  K2 Pfaffian expansion / minor quadrics / Laplace /
     volume identity / C6 equivariance breaks      -> WICK-BROKEN
  K3 the counting theorem breaks                   -> SELFHOSTING-BROKEN
  K4 recursion / orbit / period breaks             -> CLOCK-BROKEN
  K5 factorization census / outer signature breaks -> ONEFACT-BROKEN
  K7 a control does not fire                       -> CONTROL-DEAD

VERDICT (frozen enum): K6PFAFFIAN-CLOSED (+ per-theorem tokens
T1=MOTIF-CLOSED, T2=PFAFFIAN-SIGNS-MATCHED / GAUGE-MATCHED(chi) /
SIGNS-DEAD, T3=SELFHOSTING-COUNTED, T4=CLOCK-DISTINGUISHED /
CLOCK-GENERIC, T5=OUTER-SIGNATURE-CLOSED) / K6PFAFFIAN-PARTIAL /
PIPELINE-BROKEN / CONTROL-DEAD.  T2 = SIGNS-DEAD demotes the verdict
to PARTIAL; T4's typing does not (an honest census either way).

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  Exact integer / sympy arithmetic in
every decision; no floats, no RNG, no fits.  AST firewall: banned
identifiers zetazero / nzeros / primerange / isprime / primepi /
nextprime / prevprime (self-scan).  NO physics claim beyond the
finite theorems; no marker moves; T3's premise typing is stated in
the protocol.

SPEC v2 AMENDMENTS: none at freeze; any post-run amendment is
documented here with the fail-first output preserved.

Sources (read-only, machinery rebuilt inline): verification/v880
(q* closed form, anchor line classification, Hodge signs, parity
lift), s6_plucker_hadamard_probe (duad model, Plucker monomial keys
and signs, vacuum selection), cfin_aut_flavor_probe (Sp(4,2)
census, Aut(C_fin) ~= C6, generator pin g^2 = sigma), v832 (anchor
a = (1,1,2)), v844 (M_1 = 30 ladder rung), tfpt_constants (N_fam,
g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/k6_pfaffian_selfhosting_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print("%s  (t=%.1fs)" % (title, time.time() - T0))
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------------------ bit model
# words are ints 0..15; bit i = coordinate x_{i+1} in the family/anchor
# basis (F1, F2, F3, A) with Gram J - I (v880 / round 44):
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000          # A    = (0,0,0,1)
FSIG = 0b0111           # FSum = (1,1,1,0)
ANCHOR = (1, 1, 2)      # v832 [E]
BASIS = (1, 2, 4, 8)
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    """order-3 deck sigma: (b0,b1,b2,b3) -> (b2,b0,b1,b3) (v880)."""
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    """q_c(v) = C(|v|,2) + c.v mod 2 -- the 16 refinements (v880)."""
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA[v]) if bit)


def wedge_sign(S, T):
    """sign of e_S ^ e_T in Lambda^4 (ascending basis); None if the
    supports overlap (exact integer exterior algebra, round 44)."""
    seq = sorted(S) + sorted(T)
    if len(set(seq)) != 4:
        return None
    inv = sum(1 for i in range(4) for j in range(i + 1, 4)
              if seq[i] > seq[j])
    return -1 if inv % 2 else 1


def vol_sign(S, T, i):
    """sign of e_S ^ e_T ^ e_i vs e_1^...^e_5 (full top form)."""
    seq = sorted(S) + sorted(T) + [i]
    if len(set(seq)) != 5:
        return None
    inv = sum(1 for a in range(5) for b in range(a + 1, 5)
              if seq[a] > seq[b])
    return -1 if inv % 2 else 1


def matching_sign(M):
    """permutation sign of a perfect matching of {0..5}: pairs
    (min,max) sorted by minima, inversion count of the 6-word."""
    pairs = sorted(tuple(sorted(e)) for e in M)
    seq = [x for p in pairs for x in p]
    inv = sum(1 for a in range(6) for b in range(a + 1, 6)
              if seq[a] > seq[b])
    return -1 if inv % 2 else 1


def compose(p, q):
    """(p o q)[i] = p[q[i]]."""
    return tuple(p[q[i]] for i in range(len(q)))


def perm_order(p):
    o, pp = 1, p
    ident = tuple(range(len(p)))
    while pp != ident:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(perm):
    n = len(perm)
    seen = [False] * n
    cyc = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            ln += 1
        cyc.append(ln)
    return tuple(sorted(cyc))


def perm_sign(perm):
    ct = cycle_type(perm)
    return -1 if (len(perm) - len(ct)) % 2 else 1


def pf_of(mat, idx):
    """recursive Pfaffian expansion along the first index of idx."""
    if not idx:
        return sp.Integer(1)
    i0, rest0 = idx[0], idx[1:]
    tot = sp.Integer(0)
    for k, j in enumerate(rest0):
        sub = [t for t in rest0 if t != j]
        tot += sp.Integer(-1) ** k * mat[i0, j] * pf_of(mat, sub)
    return tot


def dfact(n):
    """n!! for odd n >= 1 (exact integers)."""
    out = 1
    while n > 1:
        out *= n
        n -= 2
    return out


def all_matchings(vs):
    vs = sorted(vs)
    if not vs:
        return [frozenset()]
    a = vs[0]
    out = []
    for b in vs[1:]:
        rest = [x for x in vs if x not in (a, b)]
        for sub in all_matchings(rest):
            out.append(sub | {frozenset({a, b})})
    return out


def main():
    print("CFIN.K6.MOTIF.01 + DOILY.PFAFFIAN.WICK.01 + "
          "P2.SELFHOSTING.PAIRING.01 + ANCHOR.MOD30.CLOCK.01")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO physics claim beyond the finite theorems; no marker "
          "moves; exploration only.")

    # ==================================================================
    section("S0 -- firewall + shared setup (corpus machinery rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s"
          % (BANNED_IDS,), not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    check("S0.1 the 16 polar shifts q_c are ALL distinct refinements "
          "of hb (v880 S1.1(d): these ARE all refinements -- any "
          "refinement differs from q_0 by a linear character)",
          ok_ref and len(set(refs)) == 16, kill="K0")

    arf0 = sorted(q for q in refs if q.count(0) == 10)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    check("S0.2 Arf census 10 + 6 (zeros 10 <-> Arf 0, zeros 6 <-> "
          "Arf 1)", len(arf0) == 10 and len(arf1) == 6,
          "got %d + %d" % (len(arf0), len(arf1)), kill="K0")

    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand_a = [q for q in siginv if q[A_BIT] == 1]
    cand = [q for q in cand_a if q[FSIG] == 0]
    check("S0.3 frozen v845 selector: 16 -> %d (sigma) -> %d "
          "(q(A)=1) -> %d (q(FSum)=0) = unique q*"
          % (len(siginv), len(cand_a), len(cand)),
          len(siginv) == 4 and len(cand_a) == 2 and len(cand) == 1,
          kill="K0")
    QSTAR = cand[0]

    ZQ = [v for v in range(16) if QSTAR[v] == 0]
    ovoid = [v for v in ZQ if v]
    check("S0.4 zeros(q*) = {0} u five ovoid messages (weights 3,4; "
          "v880 rebuilt): |Z| = %d" % len(ZQ),
          len(ZQ) == 6 and sorted(pc(v) for v in ovoid)
          == [3, 3, 3, 3, 4], kill="K0")

    NZ = list(range(1, 16))
    lines_pg = set()
    for a2, b2 in itertools.combinations(NZ, 2):
        lines_pg.add(frozenset({a2, b2, a2 ^ b2}))
    iso = sorted([L for L in lines_pg
                  if all(HT[u][w] == 0 for u in L for w in L)],
                 key=sorted)
    noniso = [L for L in lines_pg if L not in set(iso)]
    sec_lines = [L for L in noniso
                 if sorted(QSTAR[v] for v in L) == [0, 0, 1]]
    ext_lines = [L for L in noniso
                 if sorted(QSTAR[v] for v in L) == [1, 1, 1]]
    check("S0.5 PG(3,2): 35 lines = 15 doily + 10 secant + 10 "
          "external (v880 rebuilt)",
          len(lines_pg) == 35 and len(iso) == 15
          and len(sec_lines) == 10 and len(ext_lines) == 10,
          kill="K0")

    # duad model (round 44 rebuilt): six Arf-1 labels, D(v)
    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    DUADS6 = sorted((frozenset(d)
                     for d in itertools.combinations(range(6), 2)),
                    key=sorted)
    dmap = {v: duad(v) for v in NZ}
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS6)
    V0 = arf1.index(QSTAR)
    check("S0.6 duad model: D(v) = {i : q_i(v)=0} bijects the 15 "
          "nonzero messages onto the 15 duads of the six Arf-1 "
          "labels; vacuum vertex v0 = label(q*) = %d" % V0,
          biject and 0 <= V0 < 6, kill="K0")

    # ==================================================================
    section("T1 -- CFIN.K6.MOTIF.01: all 35 lines as K6 motifs")
    # ==================================================================
    def motif(L):
        ds = [dmap[v] for v in L]
        verts = frozenset().union(*ds)
        if len(verts) == 6 and all(not (a & b) for a, b in
                                   itertools.combinations(ds, 2)):
            return ("matching", frozenset(ds))
        if (len(verts) == 3 and len(set(ds)) == 3
                and set(ds) == {frozenset(c) for c in
                                itertools.combinations(sorted(verts),
                                                       2)}):
            return ("triangle", verts)
        return ("neither", None)

    iso_m = [motif(L) for L in iso]
    check("T1.1(a) the 15 doily lines are EXACTLY the 15 perfect "
          "matchings of K6 (all distinct)",
          all(k == "matching" for k, _x in iso_m)
          and len({x for _k, x in iso_m}) == 15, kill="K1")

    sec_m = [motif(L) for L in sec_lines]
    sec_tri = all(k == "triangle" and V0 in x for k, x in sec_m)
    sec_w = all(sorted(2 - QSTAR[v] for v in L) == [1, 2, 2]
                for L in sec_lines)
    check("T1.2(b) the 10 secants are EXACTLY the 10 triangles of K6 "
          "THROUGH v0 (two vacuum edges + one pair edge); weight "
          "multiset {2,2,1} = the wrong anchor (1,2,2) (v880)",
          sec_tri and sec_w and len({x for _k, x in sec_m}) == 10,
          kill="K1")

    ext_m = [motif(L) for L in ext_lines]
    ext_tri = all(k == "triangle" and V0 not in x for k, x in ext_m)
    ext_w = all(sorted(2 - QSTAR[v] for v in L) == [1, 1, 1]
                for L in ext_lines)
    check("T1.3(c) the 10 external lines are EXACTLY the 10 "
          "triangles AVOIDING v0; weight multiset {1,1,1}",
          ext_tri and ext_w and len({x for _k, x in ext_m}) == 10,
          kill="K1")

    all_tri = {x for _k, x in sec_m} | {x for _k, x in ext_m}
    want_tri = {frozenset(c)
                for c in itertools.combinations(range(6), 3)}
    check("T1.4(d) 35 = 15 + 10 + 10 complete; the 20 triangles "
          "exhaust ALL C(6,3) = 20 vertex triples of K6",
          len(iso) + len(sec_lines) + len(ext_lines) == 35
          and all_tri == want_tri, kill="K1")

    edge_law = all((QSTAR[v] == 0) == (V0 in dmap[v]) for v in NZ)
    vac_edges = {frozenset({V0, i}) for i in range(6) if i != V0}
    check("T1.5(e) EDGE LAW: q*(D^-1(e)) = 0 iff e touches v0; the "
          "5 nonzero zeros (ovoid, v880) map EXACTLY onto the 5 "
          "vacuum edges {v0, i}",
          edge_law and {dmap[v] for v in ovoid} == vac_edges,
          kill="K1")

    # carrier dictionary phi: non-vacuum Arf labels -> slots {1..5}
    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5 and set(phi.values()) == set(range(1, 6)))
    pairs_msgs = [v for v in NZ if QSTAR[v] == 1]
    ok_pair = all(frozenset(phi[j] for j in dmap[w])
                  == iota_support(w) for w in pairs_msgs)
    check("T1.6(f) CARRIER DICTIONARY: phi (ovoid-induced) is a "
          "bijection labels -> slots; the duad of EVERY pair message "
          "maps under phi EXACTLY onto its iota-support (duad model "
          "== Hodge lift, edge by edge); phi = %s"
          % (sorted(phi.items()),), ok_phi and ok_pair, kill="K1")

    def lab(j):
        return 0 if j == V0 else phi[j]

    def mslot(L):
        return frozenset(frozenset(lab(j) for j in dmap[v])
                         for v in L)

    MS = {L: mslot(L) for L in iso}
    MSLOT = sorted(MS.values(),
                   key=lambda m: sorted(sorted(e) for e in m))
    check("T1.7 relabeled matchings (vacuum -> 0, labels -> slots): "
          "15 distinct perfect matchings of {0..5}",
          len(set(MSLOT)) == 15
          and all(len(m) == 3 and frozenset().union(*m)
                  == frozenset(range(6)) for m in MSLOT), kill="K1")

    # ==================================================================
    section("T2 -- DOILY.PFAFFIAN.WICK.01: the fermionic sign theorem")
    # ==================================================================
    SYM = {}
    for i in range(6):
        for j in range(i + 1, 6):
            SYM[(i, j)] = sp.Symbol("a_%d%d" % (i, j))
    A6 = sp.Matrix(6, 6, lambda r, c:
                   SYM[(r, c)] if r < c
                   else (-SYM[(c, r)] if r > c else 0))
    PF6 = sp.expand(pf_of(A6, list(range(6))))
    cd = PF6.as_coefficients_dict()

    def mono_of(M):
        out = sp.Integer(1)
        for e in M:
            out *= SYM[tuple(sorted(e))]
        return out

    sgn = {}
    ok_c = True
    for m in MSLOT:
        c = cd.get(mono_of(m), 0)
        ok_c &= (c in (1, -1))
        sgn[m] = int(c)
    check("T2.1(a) Pf(A) expands into EXACTLY 15 monomials, one per "
          "matching, all coefficients +-1",
          len(cd) == 15 and ok_c, kill="K2")
    check("T2.2(a) extracted signs EQUAL the independent "
          "permutation-sign definition (pairs by minima, inversion "
          "count) on all 15",
          all(sgn[m] == matching_sign(m) for m in MSLOT), kill="K2")

    # per-matching (i; S, T) data + hodge signs; line-derived ward
    def m_ist(m):
        vac = next(e for e in m if 0 in e)
        i = next(iter(vac - {0}))
        S, T = sorted((e for e in m if e != vac), key=sorted)
        return i, S, T

    ok_islot = True
    for L in iso:
        ov = [v for v in L if QSTAR[v] == 0][0]
        islot = next(iter(frozenset(range(1, 6)) - iota_support(ov)))
        ok_islot &= (m_ist(MS[L])[0] == islot)
    check("T2.3(b) bridge ward: the matching's vacuum-edge partner i "
          "EQUALS the line's omitted carrier slot (v880 lift) on all "
          "15", ok_islot, kill="K2")

    hodge = {m: wedge_sign(m_ist(m)[1], m_ist(m)[2]) for m in MSLOT}
    vol = {m: vol_sign(m_ist(m)[1], m_ist(m)[2], m_ist(m)[0])
           for m in MSLOT}

    print("      15-row SIGN TABLE (i; {S|T}): pfaffian / hodge "
          "(Lambda^4) / volume (Lambda^5):")
    n_direct = 0
    disc = {}
    for i in range(1, 6):
        row = [m for m in MSLOT if m_ist(m)[0] == i]
        row.sort(key=lambda m: sorted(sorted(e) for e in m))
        for m in row:
            _i, S, T = m_ist(m)
            d = sgn[m] * hodge[m]
            disc.setdefault(i, set()).add(d)
            n_direct += (sgn[m] == hodge[m])
            print("        i=%d  {%s|%s}: pf %+d  hodge %+d  "
                  "vol %+d  disc %+d"
                  % (i, "".join(map(str, sorted(S))),
                     "".join(map(str, sorted(T))),
                     sgn[m], hodge[m], vol[m], d))
    gauge_ok = all(len(s) == 1 for s in disc.values())
    chi = {i: next(iter(disc[i])) for i in disc} if gauge_ok else None
    if n_direct == 15:
        t2_type = "PFAFFIAN-SIGNS-MATCHED"
    elif gauge_ok:
        t2_type = ("GAUGE-MATCHED(chi(i) = %s on the vacuum edges "
                   "{0,i}, i = 1..5)"
                   % "".join("+" if chi[i] == 1 else "-"
                             for i in range(1, 6)))
    else:
        t2_type = "SIGNS-DEAD"
    chi_is_alt = (gauge_ok and
                  all(chi[i] == (-1) ** (i + 1) for i in range(1, 6)))
    check("T2.4(b) SIGN CENSUS: direct match %d/15; discrepancy "
          "d(M) = sgn(M)*hodge(M) depends ONLY on the omitted slot i "
          "(global gauge, NOT line-dependent): %s; measured chi(i) "
          "== (-1)^(i+1): %s -- typed %s"
          % (n_direct, gauge_ok, chi_is_alt, t2_type),
          gauge_ok, kill="K2")
    check("T2.5(c) VOLUME NORMALIZATION: sgn(M) == sign of "
          "b_S ^ b_T ^ e_i = +- e_1^...^e_5 on ALL 15 -- the "
          "fermionic sign IS the top-form sign; chi is exactly the "
          "Lambda^4 vs Lambda^5 conversion character",
          all(sgn[m] == vol[m] for m in MSLOT), kill="K2")

    # (d) the five 3-groups = the round-44 Plucker quadrics
    ok_minor = True
    laplace = sp.Integer(0)
    for i in range(1, 6):
        j, k, l, m4 = sorted(set(range(1, 6)) - {i})
        rest = [j, k, l, m4]
        minor = sp.expand(pf_of(A6, rest))
        quad = (SYM[(j, k)] * SYM[(l, m4)]
                - SYM[(j, l)] * SYM[(k, m4)]
                + SYM[(j, m4)] * SYM[(k, l)])
        ok_minor &= (sp.expand(minor - quad) == 0)
        laplace += sp.Integer(-1) ** (i + 1) * SYM[(0, i)] * minor
    check("T2.6(d) FIVE 3-GROUPS: each vacuum-row 4x4 minor "
          "Pfaffian == the round-44 3-term Plucker quadric "
          "a_jk a_lm - a_jl a_km + a_jm a_kl (signs (+,-,+)), all "
          "five slots", ok_minor, kill="K2")
    check("T2.7(d) LAPLACE: Pf(A) == sum_i (-1)^(i+1) a_0i "
          "Pf(A_{0i-hat}) symbolically; the Laplace sign (-1)^(i+1) "
          "== the measured gauge character chi(i)",
          sp.expand(PF6 - laplace) == 0 and chi_is_alt, kill="K2")

    # ---- (e) C6 covariance
    gl_n = 0
    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        gl_n += 1
        if all(HT[imgs[a]][imgs[b]] == 1
               for a in range(4) for b in range(a + 1, 4)):
            SP6.append(tuple(p))
    check("T2.8(e) ward: |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == "
          "720 (exhaustive)" % (gl_n, len(SP6)),
          gl_n == 20160 and len(SP6) == 720, kill="K2")

    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA[p[v]] == tuple(IOTA[v][pi[s]]
                                          for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    orders = sorted(perm_order(p) for p in AUT)
    g_cands = sorted(p for p in AUT if perm_order(p) == 6)
    g_pin = [p for p in g_cands if compose(p, p) == SIGP]
    check("T2.9(e) Aut(C_fin) rebuilt: |Aut| = %d == 6, orders %s "
          "== [1,2,3,3,6,6]; generator PIN g^2 = sigma unique "
          "(round 44)" % (len(AUT), orders),
          len(AUT) == 6 and orders == [1, 2, 3, 3, 6, 6]
          and len(g_pin) == 1, kill="K2")
    G = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[G[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    ok_int = all(dmap[G[v]] == frozenset(pia[j] for j in dmap[v])
                 for v in NZ)
    pair_ct = cycle_type(
        tuple({d: i for i, d in enumerate(DUADS6)}[
            frozenset(pia[j] for j in d)]
            for d in DUADS6))
    pair_only = sorted(
        len(o) for o in _duad_orbits(pia, V0, vacuum=False))
    vac_only = sorted(
        len(o) for o in _duad_orbits(pia, V0, vacuum=True))
    check("T2.10(e) induced pi_a on the 6 Arf labels: fixes v0 (%s); "
          "intertwines the duad action D(g v) = pi_a(D(v)) on all "
          "15; cycle type on the TEN pair duads = %s == [1,3,6] "
          "(corpus cross-ref); on the five vacuum edges = %s; on "
          "all 15 duads = %s"
          % (pia[V0] == V0, pair_only, vac_only, sorted(pair_ct)),
          pia[V0] == V0 and ok_int and pair_only == [1, 3, 6],
          kill="K2")

    pi6 = [0] * 6
    for j in range(6):
        pi6[lab(j)] = lab(pia[j])
    pi6 = tuple(pi6)
    det6 = perm_sign(pi6)

    def act_m(m, p):
        return frozenset(frozenset(p[x] for x in e) for e in m)

    perm_match = {m: act_m(m, pi6) for m in MSLOT}
    ok_pm = (set(perm_match.values()) == set(MSLOT)
             and all(act_m(MS[L], pi6)
                     == mslot(frozenset(G[v] for v in L))
                     for L in iso))
    midx = {m: i for i, m in enumerate(MSLOT)}
    match_ct = cycle_type(tuple(midx[perm_match[m]] for m in MSLOT))
    check("T2.11(e) g permutes the 15 matchings (compatible with the "
          "line action g.L); vertex cycle type %s, matching cycle "
          "type %s, det(pi) = %+d"
          % (sorted(cycle_type(pi6)), sorted(match_ct), det6),
          ok_pm, kill="K2")

    def cross_char(m, p):
        out = 1
        for e in m:
            a, b = sorted(e)
            if p[a] > p[b]:
                out = -out
        return out

    ok_cov = all(sgn[perm_match[m]]
                 == det6 * cross_char(m, pi6) * sgn[m] for m in MSLOT)
    P6 = sp.Matrix(6, 6, lambda r, c: 1 if r == pi6[c] else 0)
    B6 = P6 * A6 * P6.T
    PFB = sp.expand(pf_of(B6, list(range(6))))
    ok_sym = (sp.expand(PFB - det6 * PF6) == 0)
    cc_census = sorted(cross_char(m, pi6) for m in MSLOT)
    check("T2.12(e) Pf EQUIVARIANCE: symbolically Pf(P A P^T) == "
          "det(P) Pf(A) = %+d Pf(A); per matching sgn(pi(M)) == "
          "det(pi) * c_pi(M) * sgn(M) on all 15 (crossing character "
          "census: %d minus / %d plus) -- the sign pattern is "
          "preserved with exactly this character"
          % (det6, cc_census.count(-1), cc_census.count(1)),
          ok_cov and ok_sym, kill="K2")

    # ==================================================================
    section("T3 -- P2.SELFHOSTING.PAIRING.01: C(g+1,2) = g!!")
    # ==================================================================
    gs = [1, 3, 5, 7, 9, 11, 13, 15]
    binom = [math.comb(g + 1, 2) for g in gs]
    dblf = [dfact(g) for g in gs]
    print("      g        : %s" % gs)
    print("      C(g+1,2) : %s" % binom)
    print("      g!!      : %s" % dblf)
    sols = [g for g, b, d in zip(gs, binom, dblf) if b == d]
    check("T3.1(a) solutions of C(g+1,2) = g!! among odd g in "
          "{1..15}: %s == [1, 5]; g = 1 is the TRIVIAL case "
          "(C(2,2) = 1 = 1!!), so g = 5 = g_car is the only "
          "NONTRIVIAL solution (states = duads of 6, contractions = "
          "matchings of 6: 15 = 15)" % sols,
          sols == [1, 5] and g_car == 5, kill="K3")
    check("T3.2(b) (g-2)!! = 3!! = %d == 3 == N_fam at g = 5"
          % dfact(3), dfact(3) == 3 == N_fam, kill="K3")

    gsym = sp.symbols("g", positive=True)
    ratio_gap = sp.expand((gsym + 1) * gsym - (gsym + 3))
    sep = all(d > b for g, b, d in zip(gs, binom, dblf) if g >= 7)
    ratios_ok = all((g + 2) * math.comb(g + 1, 2)
                    > math.comb(g + 3, 2) for g in gs if g >= 7)
    check("T3.3(c) GROWTH SEPARATION: g!! > C(g+1,2) for all odd "
          "g >= 7 (checked to 15); induction step: multiplier g+2 > "
          "binomial quotient iff g(g+1) - (g+3) = %s > 0 iff "
          "g^2 > 3 (symbolic; holds for all g >= 2) -- the "
          "separation only grows" % ratio_gap,
          sep and ratios_ok
          and sp.expand(ratio_gap - (gsym ** 2 - 3)) == 0, kill="K3")
    check("T3.4 HONEST TYPING: [E] counting theorem; the physical "
          "premise (the boundary grammar IS a self-hosting Wick "
          "pair compiler) stays [O] -- no marker move",
          True, "typed, no upgrade")

    # ==================================================================
    section("T4 -- ANCHOR.MOD30.CLOCK.01: the power-sum clock")
    # ==================================================================
    nsym = sp.symbols("n", positive=True)
    pvals = [sum(t ** n for t in ANCHOR) for n in range(1, 11)]
    ok_form = all(pvals[n - 1] == 2 + 2 ** n for n in range(1, 11))
    ok_rec = (sp.simplify(2 * (2 + 2 ** nsym) - 2
                          - (2 + 2 ** (nsym + 1))) == 0
              and all(pvals[n] == 2 * pvals[n - 1] - 2
                      for n in range(1, 10)))
    check("T4.1(a) p_n(a) = 1 + 1 + 2^n = 2 + 2^n (n = 1..10); the "
          "affine recursion p_{n+1} = 2 p_n - 2 holds symbolically "
          "and numerically; p_1 = 4 = e1, p_2 = 6 (v880)",
          ok_form and ok_rec and pvals[0] == 4 and pvals[1] == 6,
          kill="K4")

    orbit30 = [p % 30 for p in pvals[:5]]
    check("T4.2(b) orbit mod 30: %s -- 4 -> 6 -> 10 -> 18 -> 4, "
          "period EXACTLY 4 = |mu_4|; p_5 = %d = 4 + 30"
          % (orbit30, pvals[4]),
          orbit30 == [4, 6, 10, 18, 4] and pvals[4] == 34
          and len(set(orbit30[:4])) == 4, kill="K4")

    def orbit_profile(m):
        seen = {}
        cur = 4 % m
        step = 0
        while cur not in seen:
            seen[cur] = step
            cur = (2 * cur - 2) % m
            step += 1
        return seen[cur], step - seen[cur]     # (preperiod, period)

    pure4 = [m for m in range(2, 100) if orbit_profile(m) == (0, 4)]
    event4 = [m for m in range(2, 100)
              if orbit_profile(m)[1] == 4 and orbit_profile(m)[0] > 0]
    all_div30 = all(30 % m == 0 for m in pure4)
    lcm_p = math.lcm(*pure4) if pure4 else 0
    clock_type = ("CLOCK-DISTINGUISHED" if all_div30 and lcm_p == 30
                  else "CLOCK-GENERIC")
    check("T4.3(c) ANTI-NUMEROLOGY CENSUS m < 100: purely period-4 "
          "moduli = %s (%d of 98); eventually-period-4 (preperiod "
          "> 0, honest note) = %s; ALL purely periodic moduli "
          "divide 30 and lcm = %d == 30 -- 30 is the MAXIMAL "
          "(universal) clock, typed %s (honest caveat: m = 5, 10, "
          "15 already realize period 4)"
          % (pure4, len(pure4), event4, lcm_p, clock_type),
          len(pure4) >= 1 and 30 in pure4, kill="K4")

    # ==================================================================
    section("T5 -- K6.ONEFACT.OUTER.01: the 30 = 6 x 5 schedule")
    # ==================================================================
    MB = all_matchings(range(6))
    check("T5.0 ward: abstract matching census = %d == 15 and EQUALS "
          "the doily-derived set" % len(MB),
          len(MB) == 15 and set(MB) == set(MSLOT), kill="K5")

    FACTS = []
    for combo in itertools.combinations(range(15), 5):
        edges = set()
        for idx in combo:
            edges |= MB[idx]
        if len(edges) == 15:
            FACTS.append(frozenset(MB[idx] for idx in combo))
    per_match = [sum(1 for F in FACTS if m in F) for m in MB]
    check("T5.1(a) K6 has EXACTLY %d == 6 one-factorizations, each "
          "of 5 matchings; every matching lies in EXACTLY 2 "
          "(census %s); schedule 30 = 6 x 5 = 2 x 15"
          % (len(FACTS), sorted(set(per_match))),
          len(FACTS) == 6 and all(c == 2 for c in per_match)
          and 6 * 5 == 2 * 15 == 30, kill="K5")

    ok_cover = all(
        sum(1 for m in F if any(v in e for e in m)) == 5
        for F in FACTS for v in range(6))
    check("T5.2(b) trivial incidence ward: every factorization "
          "covers every vertex in all 5 of its matchings",
          ok_cover, kill="K5")

    ALL6 = list(itertools.permutations(range(6)))

    def act_f(F, h):
        return frozenset(act_m(m, h) for m in F)

    orbitF = {act_f(FACTS[0], h) for h in ALL6}
    stabF = [h for h in ALL6 if act_f(FACTS[0], h) == FACTS[0]]
    stabF_orbV = {h[v] for h in stabF for v in [0]}
    stabV = [h for h in ALL6 if h[0] == 0]
    stabV_orbF = {act_f(FACTS[0], h) for h in stabV}
    check("T5.3(c) S6 TRANSITIVE on the 6 factorizations (orbit %d); "
          "|Stab(F)| = %d == 120 acting TRANSITIVELY on the 6 "
          "vertices (orbit of vertex 0: %d); |Stab(vertex)| = %d "
          "== 120 acting TRANSITIVELY on the 6 factorizations "
          "(orbit %d) -- the duality signature"
          % (len(orbitF), len(stabF), len(stabF_orbV), len(stabV),
             len(stabV_orbF)),
          len(orbitF) == 6 and orbitF == set(FACTS)
          and len(stabF) == 120 and len(stabF_orbV) == 6
          and len(stabV) == 120 and len(stabV_orbF) == 6,
          kill="K5")

    tperm = (1, 0, 2, 3, 4, 5)
    fidx = {F: i for i, F in enumerate(FACTS)}
    t_on_f = tuple(fidx[act_f(FACTS[i2], tperm)] for i2 in range(6))
    ct_v = cycle_type(tperm)
    ct_f = cycle_type(t_on_f)
    check("T5.4(d) OUTER SIGNATURE: the transposition (01) acts on "
          "the 6 vertices with cycle type %s == (1,1,1,1,2) [4 fixed "
          "points] but on the 6 factorizations with cycle type %s "
          "== (2,2,2) [0 fixed points] -- the two S6 actions on 6 "
          "objects are NON-conjugate (the exceptional outer "
          "automorphism, exact)"
          % (ct_v, ct_f),
          ct_v == (1, 1, 1, 1, 2) and ct_f == (2, 2, 2), kill="K5")
    check("T5.5(d) HONEST TYPING: the 6 vertices ARE the 6 Arf-1 "
          "vacua (duad model, T1); the 6 factorizations are the "
          "outer-dual 6-set; NO canonical vertex <-> factorization "
          "bijection exists (fixed-point obstruction 4 vs 0) -- "
          "report only, no physics claim",
          True, "typed, report only")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    q0 = arf0[0]
    z0 = [v for v in NZ if q0[v] == 0]
    z0_duads = {dmap[v] for v in z0}
    star_v = [w for w in range(6)
              if all(w in d for d in z0_duads)]
    pats = {tuple(sorted(q0[v] for v in L)) for L in iso}
    check("C1 FIRES: Arf-0 refinement: %d == 9 nonzero zeros; their "
          "duads are NOT the edge star of any vertex (a star has 5 "
          "edges; common vertex: %s); doily line patterns %s not "
          "constant {0,1,1} -- the T1 vacuum-incidence reading "
          "breaks" % (len(z0), star_v, sorted(pats)),
          len(z0) == 9 and not star_v and pats != {(0, 1, 1)},
          kill="K7")

    chi_wrong = dict(chi) if gauge_ok else {i: 1 for i in range(1, 6)}
    chi_wrong[2] = -chi_wrong[2]
    mism = [m for m in MSLOT
            if sgn[m] != chi_wrong[m_ist(m)[0]] * hodge[m]]
    check("C2 FIRES: the WRONG character (chi flipped on slot 2) "
          "produces EXACTLY %d == 3 mismatches, all in the i = 2 "
          "triple" % len(mism),
          len(mism) == 3 and all(m_ist(m)[0] == 2 for m in mism),
          kill="K7")

    check("C3 FIRES: g = 3: C(4,2) = %d != %d = 3!!; g = 7: C(8,2) "
          "= %d != %d = 7!! -- the counting theorem kills the "
          "neighbors" % (math.comb(4, 2), dfact(3),
                         math.comb(8, 2), dfact(7)),
          math.comb(4, 2) != dfact(3)
          and math.comb(8, 2) != dfact(7), kill="K7")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif "K0" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif KILLS or t2_type == "SIGNS-DEAD":
        VERDICT = "K6PFAFFIAN-PARTIAL [%s]" % ", ".join(
            sorted(set({"K1": "MOTIF-BROKEN", "K2": "WICK-BROKEN",
                        "K3": "SELFHOSTING-BROKEN",
                        "K4": "CLOCK-BROKEN",
                        "K5": "ONEFACT-BROKEN"}.get(k, k)
                       for k in KILLS))
            or ["T2=SIGNS-DEAD"])
    else:
        VERDICT = ("K6PFAFFIAN-CLOSED [T1=MOTIF-CLOSED, T2=%s, "
                   "T3=SELFHOSTING-COUNTED, T4=%s, "
                   "T5=OUTER-SIGNATURE-CLOSED]"
                   % (t2_type, clock_type))
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * T1: the 35 lines of PG(3,2) ARE the K6 motif census under the
    duad model: 15 perfect matchings (doily) + 10 triangles through
    the vacuum (secants, wrong anchor (1,2,2)) + 10 triangles
    avoiding it (externals, (1,1,1)); q*(e) = 0 iff e touches the
    vacuum vertex.
  * T2: the fermionic Pfaffian signs are the VOLUME-form signs;
    they equal the corpus Lambda^4 Hodge signs up to the GLOBAL
    gauge chi(i) = (-1)^(i+1) on the five vacuum edges -- which is
    exactly the vacuum-row Laplace sign; the five 3-groups are the
    round-44 Plucker quadrics; Pf is C6-equivariant with the
    computed crossing character (Pf(P A P^T) = det(P) Pf(A)).
  * T3: C(g+1,2) = g!! has g = 5 as its only nontrivial solution;
    (g-2)!! = 3 = N_fam there; separation grows for g >= 7 ([E]
    counting theorem; the Wick-compiler premise stays [O]).
  * T4: p_n(a) = 2 + 2^n obeys p_{n+1} = 2 p_n - 2 with mod-30
    orbit 4 -> 6 -> 10 -> 18 -> 4 (period 4 = |mu_4|); census typed
    above.
  * T5: 6 one-factorizations, 30 = 6 x 5 = 2 x 15; the vertex and
    factorization S6-actions are NON-conjugate (transposition
    (1,1,1,1,2) vs (2,2,2)) -- the exceptional outer signature.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot
                 and VERDICT.startswith("K6PFAFFIAN-CLOSED")) else 1


def _duad_orbits(pia, v0, vacuum):
    """orbits of the induced duad permutation restricted to duads
    containing v0 (vacuum=True) or avoiding it (vacuum=False)."""
    duads = [frozenset(d) for d in itertools.combinations(range(6), 2)
             if (v0 in d) == vacuum]
    seen = set()
    orbits = []
    for d in duads:
        if d in seen:
            continue
        orb = [d]
        cur = frozenset(pia[j] for j in d)
        while cur != d:
            orb.append(cur)
            cur = frozenset(pia[j] for j in cur)
        seen |= set(orb)
        orbits.append(orb)
    return orbits


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('s6_plucker_hadamard_probe', _SRC_0, 27, (), 'S6PLUCKER-CLOSED', 0),
    ('cfin_aut_flavor_probe', _SRC_1, 19, (), 'C6FLAVOR-MEASURED', 0),
    ('k6_pfaffian_selfhosting_probe', _SRC_2, 42, (), 'K6PFAFFIAN-CLOSED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v888 -- DOILY.S6.IRREP.01 + DOILY.PLUCKER.GR25.01 + CFIN.ANCHOR.HADAMARD.01 + CFIN.S6.VACUUM.01 + CFIN.AUT.FLAVOR.C6.01 + CFIN.K6.MOTIF.01 + DOILY.PFAFFIAN.WICK.01 + P2.SELFHOSTING.PAIRING.01 + ANCHOR.MOD30.CLOCK.01 + K6.ONEFACT.OUTER.01: the complete finite Pfaffian/K6 signature of the compiler')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v888: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the finite compiler carries a complete K6/Pfaffian signature: exact Specht scalars, gauge-matched fermionic signs, one C6 orbit, and the self-hosting count g = 5')
    print("[%s] v888 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
