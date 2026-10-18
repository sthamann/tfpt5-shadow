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
