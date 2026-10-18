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
