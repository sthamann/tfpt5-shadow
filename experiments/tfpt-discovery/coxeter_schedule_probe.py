#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""coxeter_schedule_probe -- CFIN.K6.COXETER_SCHEDULE.01 (round 49,
from the third 2026-08-09 external review): does the 30-entry K6
pairing schedule (6 one-factorizations x 5 matchings = 30 = 2 x 15)
intertwine with the E8 Coxeter element of order 30 = h(E8)?

WHY NEW (redundancy check against the corpus FIRST): v1 and the
architecture paper carry h(E8) = 30 = 2 N_fam g_car as a COUNTING
identity; v880 has 30 = M_1 = the doily transport-incidence budget
(counting only, no bijection claimed); v845/v880 have the Gaussian
register V = L/(1+i)L with census 240 = 15 x 16; the s6 duad model
maps the 15 nonzero classes onto the 15 duads of K6 with doily lines
= perfect matchings; cfin_aut_flavor pins the C6 generator g (g^2 =
sigma).  NOT in the corpus: any CONSTRUCTION of the Coxeter element,
its orbit census on the 240 roots, the class sequence along a Coxeter
orbit, or any linearization of the 30-entry (factorization, matching)
schedule.  The review's hypothesis: 30 is not just group theory but
an OPERATIVE program length -- the execution schedule of the pair
compiler.  This probe freezes exactly that hypothesis test.  An
honest DEAD is a fine outcome.

STRUCTURAL FACTS PREDECLARED (stated before first run; each is
re-verified by measurement inside the probe):
 (i)   S6 has NO element of order 30 (max element order in S6 is 6;
       measured over all 720).  So the K6 side has NO canonical
       order-30 cyclic action on the 6 VERTICES; the schedule clock,
       if it exists, must act on the 30 ENTRIES (pairs), living in a
       product of the factorization phase (order 6) and the matching
       phase (order 5) -- exactly the review's actual claim, tested
       as such.
 (ii)  ALL eight E8 Coxeter exponents {1,7,11,13,17,19,23,29} are
       ODD, hence w^15 = -1 (the central involution); and 2L is
       contained in (1+i)L, so class(-r) = class(r) -- the class
       sequence of EVERY root orbit satisfies c_{k+15} = c_k
       AUTOMATICALLY.  The 15-shift spacing therefore carries no
       information by itself; the binary content of C3 is whether an
       orbit's 15 antipodal pairs BIJECT onto the 15 nonzero classes
       (each class exactly twice <=> first 15 entries all distinct).
 (iii) IF any two of the six one-factorizations share exactly one
       matching (measured; then the 15 matchings biject onto the 15
       factorization PAIRS = a K6 on factorizations), then in ANY
       6 x 5 CRT schedule the two occurrences of a matching are 15
       apart iff its two host factorizations sit 3 apart in the
       6-cycle AND its within-index repeats -- at most 3 of the 15
       matchings can realize the sheet spacing (pigeonhole: only 3
       antipodal factorization pairs exist).  The schedule side
       CANNOT mirror a full 15 x 2 sheet pattern; measured exactly.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
exact integer/sympy arithmetic in every decision; the single seeded
shuffle lives in control CTRL1 only, seed 49 declared, and never
touches a deployed object):

 C1  THE E8 COXETER ELEMENT (corpus conventions).  Rebuild the
     Gaussian Construction-A E8 (v845: code C* = the mu4/sigma-
     invariant placement, 2 of 30, pinned by containing 10101010;
     roots = 16 (+-2 e_k) + 224 (weight-4 codeword supports, all
     signs), norm^2 = 4 in the doubled frame); register census
     240 = 15 x 16, zero class EMPTY.  Simple roots: frozen
     positivity functional f = (1,2,4,8,16,32,64,128) (nonzero on
     all 240: signed sums of distinct powers of 2 cannot vanish);
     120 positive roots; the 8 indecomposables; Cartan matrix
     (Gram/2) matched to the v1 Bourbaki Cartan by a UNIQUE
     relabeling (E8 diagram is rigid).  FROZEN ORDER: w = s_{a1}
     s_{a2} ... s_{a8} in Bourbaki labels (rightmost applied first);
     any order is conjugate -- ord, charpoly, orbit census are
     conjugation-invariant.  Verify ord(w) = 30 exactly (first
     identity power, exact rational matrix); charpoly(w) ==
     Phi_30(t) = t^8 + t^7 - t^5 - t^4 - t^3 + t + 1 (exact), i.e.
     the 8 exponents are the units mod 30 = {1,7,11,13,17,19,23,29},
     phi(30) = 8; w^15 = -I; class(-r) = class(r) on all 240.
     MEASURED EITHER WAY: does w descend to V = L/(1+i)L?  (w need
     not commute with the complex structure; a congruent root pair
     with incongruent images is the witness.)

 C2  THE SCHEDULE OBJECT (bit model, v845/v880/s6 machinery rebuilt
     inline).  Wards: 16 refinements of the bit form, Arf census
     10 + 6, frozen selector pins q*; duad model D(v) = {i : q_i(v)
     = 0} bijects the 15 nonzero classes onto the 15 duads; doily
     lines = ALL 15 perfect matchings of K6.  Census: EXACTLY 6
     one-factorizations; every matching in EXACTLY 2 of them;
     30 = 6 x 5 = 2 x 15; pair-sharing census (predeclared: every
     two factorizations share exactly one matching).  S6 facts
     measured: max element order = 6 (NO order-30 element -- fact
     (i)); S6 transitive on the 6 factorizations; |Stab(F)| =
     720/6 = 120 (the review's parenthetical '60' is corrected by
     measurement).  THE C6 GENERATOR: Sp(4,2) census (720),
     Aut(C_fin) = C6, g pinned as the unique order-6 element with
     g^2 = sigma (cfin_aut_flavor pin); g fixes the q* vertex,
     vertex cycle type (1,2,3); duad equivariance D(g v) = g_v D(v)
     warded.  g's action on the 6 factorizations MEASURED (outer
     duality predicts a 6-cycle: Out(S6) swaps class (1,2,3) with
     class (6)).  THE PENTAD ROTATION rho (frozen): fixed vertex =
     the q* vertex v*; the other five vertices in ascending label
     order form the 5-cycle a0 -> a1 -> a2 -> a3 -> a4 -> a0;
     starter matching M0 = {{v*,a0},{a1,a4},{a2,a3}} (classical
     Z5 u {inf} starter); F0 = the rho-orbit of M0, warded a
     one-factorization; rho fixes F0 and 5-cycles the other five
     (measured).  COMMUTATION TEST (the review's honest first
     test): does g commute with rho?  Measured; the group <g_v,
     rho> and its order reported; by fact (i) NO single vertex
     element has order 30 regardless.  THE FROZEN CRT SCHEDULE:
     factorization slots F_j = g_F^j(F0), j = 0..5 (requires the
     measured 6-cycle; FROZEN FALLBACK if not: lex order of the
     factorizations and lex within-order, deviation typed);
     within-order M_{j,i} = g^j(rho^i(M0)), i = 0..4 (a matching
     of F_j by construction); entry k = (F_{k mod 6}, M_{k mod 6,
     k mod 5}); T = k -> k+1 is a 30-cycle by CRT, generated by
     the commuting pair (slot shift order 6, phase shift order 5)
     ON ENTRIES.  SHEET CENSUS: for each of the 15 matchings the
     separation (k2 - k1) mod 30 of its two occurrences; count of
     separations == 15 (pigeonhole bound 3 from fact (iii)).

 C3  THE INTERTWINER TEST.  Orbits of w on the 240 roots: exact
     census (the classical structure is 8 orbits of size 30 = rank
     x h; the review's text also floats 30 orbits of size 8 --
     MEASURED, the census decides).  Per orbit (base point = the
     lex-min root, direction = w): the sequence of register classes
     c_k = [w^k r] in V, printed as 4-bit addresses in a frozen
     lex-min family/anchor basis (report-level pin; the census
     below is invariant under any relabeling of V).  Census per
     orbit: number of distinct classes among the 15 antipodal
     pairs; profile; the sheet question = does some orbit realize
     each of the 15 nonzero classes EXACTLY TWICE with the two
     occurrences 15 apart?  (Spacing 15 is automatic by fact (ii)
     whenever the multiset is 15 x 2; both conditions are still
     checked independently and reported.)  Both the schedule
     30-cycle and a root orbit are Z/30 torsors -- trivially
     isomorphic as cyclic sets; the CONTENT is exactly this finer
     2 x 15 class structure, nothing else is claimed.

 C4  THE EXPONENT READING (report, no fit, no marker move).  The
     schedule's natural frequencies are 6 and 5 (30 = 2 N_fam
     g_car = 6 x 5, v1); print the Coxeter exponents mod 6 and mod
     5 and which are +-1 in each.  NUMEROLOGY GUARD (predeclared):
     the exponents are EXACTLY the units mod 30, so mod 6 they are
     automatically the units {1,5} = +-1, and mod 5 automatically
     the units {1,2,3,4}; both readings are GENERIC consequences
     of gcd(m,30) = 1 for ANY h = 30 system and carry NO
     schedule-specific content; significance would require a
     schedule-derived selection among the units mod 30, which the
     corpus does not provide.  Stated plainly either way.

 CTRL CONTROLS (must fire; frozen fire rules):
     CTRL1 RANDOM 30-CYCLE: the ideal sheet sequence (labels
           1..15, 1..15, every separation 15) shuffled by ONE
           seeded Fisher-Yates pass (random.Random(49), declared)
           must BREAK the pairing census (some label's occurrences
           are no longer 15 apart).  Fire iff broken.
     CTRL2 CONTROL ROOT SYSTEM D8 (h = 14): standard simple roots
           e_i - e_{i+1} (i = 1..7), e_7 + e_8; w_D8 = the product
           in that frozen order; verify ord = 14 = h(D8), charpoly
           = Phi_14 Phi_2^2 (exponents 1,3,5,7,7,9,11,13 -- the
           doubled 7 is the Phi_2^2 factor), orbit census on the
           112 roots = 8 orbits of size 14.  Fire iff h = 14 != 30
           and every orbit has length 14 < 30 = 2 x 15, so NO D8
           orbit can realize 15 classes twice -- the 15-pair sheet
           structure is arithmetically impossible at h = 14.

KILLS (any one fires => typed):
  K1 compiler machinery ward breaks (refinement census, selector,
     duad model, matchings, factorization census, Sp order,
     Aut(C_fin), g pin, F0 construction)          -> PIPELINE-BROKEN
  K2 E8 machinery ward breaks (placements, root count, register
     census, simple roots, Cartan match, ord(w), charpoly, w^15,
     orbit census)                                -> PIPELINE-BROKEN
  K3 a control does not fire                      -> CONTROL-DEAD

VERDICT (frozen enum, decision order):
  0. a control does not fire      -> CONTROL-DEAD, exit 1
  1. any kill                     -> PIPELINE-BROKEN, exit 1
  2. otherwise -> COXSCHEDULE-MEASURED + <typed:
       SCHEDULE-INTERTWINED iff some w-orbit realizes each of the
         15 nonzero classes exactly twice AND every pair of
         occurrences is exactly 15 apart;
       SCHEDULE-PARTIAL iff some orbit has each class exactly
         twice but a spacing differs from 15 (impossible if fact
         (ii) holds -- kept for honesty of the enum);
       SCHEDULE-DEAD iff no orbit realizes 15 classes x 2>
     -- an honest DEAD is a fine outcome (the review calls this a
     hypothesis, not a claim).

RANDOMNESS DECLARATION: one seeded shuffle (seed 49) inside CTRL1
only; no RNG in any measurement of a deployed object; no floats, no
fits anywhere.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  AST firewall: banned identifiers
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime (self-scan).  NO physics claim beyond the typed reading,
NO RH claim, no marker moves.  Runtime cap 600 s.

SPEC v2 AMENDMENTS (fail-first preserved): none at freeze; any
post-run amendment is documented here with the fail-first output
preserved.

Sources (read-only, machinery rebuilt inline): verification/
v1_e8_glue.py (Bourbaki simple roots, Cartan conventions, h = 30 =
2 N_fam g_car counting identity), v845_cfin_normal_form.py (Gaussian
Construction-A E8, C* placement, V = L/(1+i)L census, family/anchor
basis), v880_finite_anchor_theorems.py (q* selector, doily,
30 = M_1 budget), experiments/tfpt-discovery/
s6_plucker_hadamard_probe.py (duad model, Sp(4,2) census, vacuum
S5), cfin_aut_flavor_probe.py (Aut(C_fin) = C6, the g pin g^2 =
sigma, slot conventions), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/coxeter_schedule_probe.py
"""
import ast
import hashlib
import itertools
import math
import os
import random
import sys
import time
from collections import Counter

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


# ---------------------------------------------------------- bit model
# words = ints 0..15 in the family/anchor basis (F1,F2,F3,A); the bit
# form via the v834 identity hb(v,w) = (|v||w| - |v&w|) mod 2 (v880).
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111


def sig(v):
    """order-3 deck sigma: (b0,b1,b2,b3) -> (b2,b0,b1,b3) (v880)."""
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))
IOTA = [tuple([(v >> i) & 1 for i in range(4)] + [pc(v) % 2])
        for v in range(16)]
S5 = list(itertools.permutations(range(5)))


def refinement_census():
    out = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for x in range(16):
            hx, qx = HT[x], q[x]
            for y in range(16):
                if q[x ^ y] ^ qx ^ q[y] != hx[y]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(q))
    return out


def compose(p, q):
    """(p o q)[v] = p[q[v]]."""
    return tuple(p[q[v]] for v in range(16))


def perm_order(p):
    o, pp = 1, p
    idp = tuple(range(len(p)))
    while pp != idp:
        pp = tuple(p[x] for x in pp)
        o += 1
    return o


def cycle_type(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        ln, j = 0, i
        while not seen[j]:
            seen[j] = True
            j = p[j]
            ln += 1
        out.append(ln)
    return tuple(sorted(out))


# ------------------------------------------------- Gaussian E8 (v845)
G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
          for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)


def code_image(code, perm):
    return frozenset(tuple(c[perm[k]] for k in range(8)) for c in code)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def main():
    print("CFIN.K6.COXETER_SCHEDULE.01 -- the 30-entry K6 schedule vs "
          "the E8 Coxeter element (h = 30)")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO RH claim; NO physics claim; no marker moves; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + constants")
    # ==================================================================
    check("S0.1 AST firewall clean (no zero/prime oracles: %s)"
          % (BANNED_IDS,), not ast_scan(BANNED_IDS))
    Z2 = g_car - N_fam
    check("S0.2 the corpus counting identity (v1): h(E8) = 30 = "
          "2 N_fam g_car = %d x %d x %d; |Z2| = %d; 30 = 6 x 5 = "
          "2 x 15" % (Z2, N_fam, g_car, Z2),
          Z2 * N_fam * g_car == 30 and 6 * 5 == 30 and 2 * 15 == 30,
          kill="K1")

    # ==================================================================
    section("C1 -- the E8 Coxeter element (Gaussian frame, v845)")
    # ==================================================================
    placements = set()
    for perm in itertools.permutations(range(8)):
        placements.add(code_image(C_NAIVE, perm))
    both = [c for c in placements
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    CSTAR = next(c for c in both if (1, 0, 1, 0, 1, 0, 1, 0) in c)

    ROOTS = []
    for k in range(8):
        for s in (2, -2):
            v = [0] * 8
            v[k] = s
            ROOTS.append(tuple(v))
    for c in (c for c in CSTAR if sum(c) == 4):
        sup = [k for k in range(8) if c[k]]
        for signs in itertools.product((1, -1), repeat=4):
            v = [0] * 8
            for k, s in zip(sup, signs):
                v[k] = s
            ROOTS.append(tuple(v))
    RSET = set(ROOTS)

    def in_L(v):
        return tuple(x % 2 for x in v) in CSTAR

    def in_pi2L(v):
        w = [0] * 8
        for k in range(4):
            w[2 * k] = v[2 * k] + v[2 * k + 1]
            w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
        if any(x % 2 for x in w):
            return False
        return in_L([x // 2 for x in w])

    REPS = [(0,) * 8]
    for r in ROOTS:
        if not any(in_pi2L(tuple(a - b for a, b in zip(r, rep)))
                   for rep in REPS):
            REPS.append(r)

    def label_of(v):
        for li, rep in enumerate(REPS):
            if in_pi2L(tuple(a - b for a, b in zip(v, rep))):
                return li
        raise AssertionError("vector not in L or label table broken")

    LB = {r: label_of(r) for r in ROOTS}
    census = Counter(LB.values())
    check("C1.1 Gaussian E8 rebuilt: 30 placements, 2 invariant, C* "
          "pinned; 240 roots of norm^2 = 4; register census 240 = "
          "15 x 16, zero class EMPTY",
          len(placements) == 30 and len(both) == 2
          and len(ROOTS) == 240 and len(RSET) == 240
          and all(dot(r, r) == 4 for r in ROOTS)
          and len(REPS) == 16 and 0 not in census
          and sorted(census.values()) == [16] * 15, kill="K2")

    FVEC = (1, 2, 4, 8, 16, 32, 64, 128)
    fvals = [dot(FVEC, r) for r in ROOTS]
    POS = [r for r, fv in zip(ROOTS, fvals) if fv > 0]
    PSET = set(POS)
    SIMP = sorted(r for r in POS
                  if not any(tuple(a - b for a, b in zip(r, p)) in PSET
                             for p in POS))
    CG = [[dot(a, b) // 2 for b in SIMP] for a in SIMP]
    ok_cart = (all(CG[i][i] == 2 for i in range(len(SIMP)))
               and all(CG[i][j] in (0, -1)
                       for i in range(len(SIMP))
                       for j in range(len(SIMP)) if i != j))
    check("C1.2 frozen functional f = %s nonzero on all 240; 120 "
          "positive roots; EXACTLY 8 indecomposables; Cartan (Gram/2)"
          " has diag 2, off-diag in {0,-1}" % (FVEC,),
          all(fv != 0 for fv in fvals) and len(POS) == 120
          and len(SIMP) == 8 and ok_cart, kill="K2")

    # v1 Bourbaki Cartan (corpus conventions), exact rationals
    half = sp.Rational(1, 2)
    e = [[sp.Integer(1 if i == j else 0) for j in range(8)]
         for i in range(8)]

    def vsub(*terms):
        out = [sp.Integer(0)] * 8
        for coef, vec in terms:
            for k in range(8):
                out[k] += coef * vec[k]
        return out

    a1 = vsub((half, e[0]), (-half, e[1]), (-half, e[2]),
              (-half, e[3]), (-half, e[4]), (-half, e[5]),
              (-half, e[6]), (half, e[7]))
    a2 = vsub((1, e[0]), (1, e[1]))
    a3 = vsub((1, e[1]), (-1, e[0]))
    a4 = vsub((1, e[2]), (-1, e[1]))
    a5 = vsub((1, e[3]), (-1, e[2]))
    a6 = vsub((1, e[4]), (-1, e[3]))
    a7 = vsub((1, e[5]), (-1, e[4]))
    a8 = vsub((1, e[6]), (-1, e[5]))
    BSR = [a1, a2, a3, a4, a5, a6, a7, a8]
    CB = [[int(sum(x * y for x, y in zip(u, v))) for v in BSR]
          for u in BSR]

    matches = []
    for pi in itertools.permutations(range(8)):
        if all(CG[pi[i]][pi[j]] == CB[i][j]
               for i in range(8) for j in range(i, 8)):
            matches.append(pi)
    check("C1.3 UNIQUE Bourbaki relabeling of the 8 simple roots "
          "(E8 diagram rigid): %d match(es); frozen Coxeter order = "
          "s_a1 ... s_a8 in v1 Bourbaki labels (conjugation-"
          "invariant data below)" % len(matches),
          len(matches) == 1, kill="K2")
    PI_B = matches[0]
    BOUR = [SIMP[PI_B[i]] for i in range(8)]

    def refl(a, x):
        c = dot(x, a)
        assert c % 2 == 0
        return tuple(xi - (c // 2) * ai for xi, ai in zip(x, a))

    def wfun(x):
        y = x
        for a in reversed(BOUR):
            y = refl(a, y)
        return y

    Smats = [sp.eye(8) - sp.Matrix([list(a)]).T
             * sp.Matrix([list(a)]) / 2 for a in BOUR]
    W = sp.eye(8)
    for S in Smats:
        W = W * S
    ok_wf = all(tuple(int(x) for x in (W * sp.Matrix(list(r))))
                == wfun(r) for r in ROOTS[:3])

    P = sp.eye(8)
    first_id = None
    W15 = None
    for n in range(1, 31):
        P = P * W
        if n == 15:
            W15 = P
        if first_id is None and P == sp.eye(8):
            first_id = n
    check("C1.4 ord(w) = %s == 30 = h(E8) EXACTLY (first identity "
          "power over 1..30; exact rationals; matrix/function "
          "convention warded)" % first_id,
          first_id == 30 and ok_wf, kill="K2")

    t = sp.symbols("t")
    cp_w = W.charpoly(t).as_expr()
    phi30 = sp.expand(sp.cyclotomic_poly(30, t))
    expos = [m for m in range(1, 30) if math.gcd(m, 30) == 1]
    check("C1.5 charpoly(w) = %s == Phi_30(t) EXACT => the 8 "
          "exponents are the units mod 30 = %s (phi(30) = 8), all "
          "ODD" % (cp_w, expos),
          sp.expand(cp_w - phi30) == 0
          and expos == [1, 7, 11, 13, 17, 19, 23, 29]
          and all(m % 2 == 1 for m in expos), kill="K2")

    neg_ok = all(LB[tuple(-x for x in r)] == LB[r] for r in ROOTS)
    check("C1.6 w^15 = -I EXACT (all exponents odd) and class(-r) = "
          "class(r) on all 240 (2L in (1+i)L) => c_{k+15} = c_k is "
          "AUTOMATIC on every orbit (predeclared fact (ii))",
          W15 == -sp.eye(8) and neg_ok, kill="K2")

    # does w descend to V?  (measured either way)
    by_class = {}
    for r in ROOTS:
        by_class.setdefault(LB[r], []).append(r)
    witness = None
    for li, rs in sorted(by_class.items()):
        base_img = LB[wfun(rs[0])]
        for r in rs[1:]:
            if LB[wfun(r)] != base_img:
                witness = (li, rs[0], r)
                break
        if witness:
            break
    check("C1.7 TYPED: w %s to V = L/(1+i)L -- %s"
          % ("does NOT descend" if witness else "DESCENDS",
             ("witness class %d: roots %s and %s are congruent, "
              "their w-images are not" % witness) if witness
             else "the induced map on the 16 classes is well-defined"),
          True, "measured, typed either way")

    # ==================================================================
    section("C2 -- the 30-entry K6 schedule (bit model + compiler C6)")
    # ==================================================================
    refs = refinement_census()
    arf0 = [q for q in refs if q.count(0) == 10]
    arf1 = [q for q in refs if q.count(0) == 6]
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand_a = [q for q in siginv if q[A_BIT] == 1]
    cand = [q for q in cand_a if q[FSIG] == 0]
    QSTAR = cand[0] if len(cand) == 1 else None
    check("C2.1 ward: 16 refinements of the bit form; Arf census "
          "10 + 6; frozen selector 16 -> %d -> %d -> %d pins q* "
          "(v845/v880)" % (len(siginv), len(cand_a), len(cand)),
          len(refs) == 16 and len(arf0) == 10 and len(arf1) == 6
          and len(siginv) == 4 and len(cand_a) == 2
          and len(cand) == 1, kill="K1")

    arf1s = sorted(arf1)
    VSTAR = arf1s.index(QSTAR)

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1s) if q[v] == 0)

    DUADS = sorted((frozenset(d)
                    for d in itertools.combinations(range(6), 2)),
                   key=sorted)
    dmap = {v: duad(v) for v in range(1, 16)}
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS)

    lines_pg = set()
    for x, y in itertools.combinations(range(1, 16), 2):
        lines_pg.add(frozenset({x, y, x ^ y}))
    iso = [L for L in lines_pg
           if all(HT[u][w] == 0 for u in L for w in L)]
    MATCH_ISO = {frozenset(dmap[v] for v in L) for L in iso}

    def all_matchings():
        out = []
        verts = list(range(6))

        def grow(rem, acc):
            if not rem:
                out.append(frozenset(acc))
                return
            a = rem[0]
            for b in rem[1:]:
                grow([x for x in rem if x not in (a, b)],
                     acc + [frozenset({a, b})])
        grow(verts, [])
        return out

    MS = sorted(all_matchings(),
                key=lambda m: sorted(sorted(d) for d in m))
    check("C2.2 duad model: 15 nonzero classes <-> 15 duads "
          "(bijection); doily lines = ALL %d perfect matchings of "
          "K6 (s6 probe rebuilt)" % len(MS),
          biject and len(MS) == 15 and MATCH_ISO == set(MS)
          and len(iso) == 15, kill="K1")

    # one-factorization census (exact backtracking)
    EDGES = sorted(DUADS, key=sorted)

    def factorizations():
        out = []

        def grow(cov, acc):
            if len(acc) == 5:
                out.append(frozenset(acc))
                return
            nxt = next(e for e in EDGES if e not in cov)
            for m in MS:
                if nxt in m and all(e not in cov for e in m):
                    grow(cov | set(m), acc + [m])
        grow(set(), [])
        return sorted(set(out),
                      key=lambda F: sorted(
                          sorted(sorted(d) for d in m) for m in F))

    FACTS = factorizations()
    host = {m: [F for F in FACTS if m in F] for m in MS}
    share = {}
    for Fa, Fb in itertools.combinations(FACTS, 2):
        share[(Fa, Fb)] = len(Fa & Fb)
    sharing_one = (len(FACTS) == 6
                   and all(len(h) == 2 for h in host.values())
                   and set(share.values()) == {1})
    check("C2.3 factorization census: EXACTLY %d one-factorizations;"
          " every matching in EXACTLY 2; 30 = 6 x 5 = 2 x 15; every "
          "two factorizations share EXACTLY one matching (the K6 on "
          "factorizations, fact (iii) premise): %s"
          % (len(FACTS), sharing_one),
          len(FACTS) == 6 and all(len(h) == 2 for h in host.values())
          and sharing_one, kill="K1")

    # S6 facts
    ALLG6 = list(itertools.permutations(range(6)))
    max_ord = max(math.lcm(*cycle_type(g)) for g in ALLG6)

    def act_match(p, m):
        return frozenset(frozenset(p[x] for x in ed) for ed in m)

    def act_fact(p, F):
        return frozenset(act_match(p, m) for m in F)

    FSET = set(FACTS)
    orbF0 = {act_fact(g, FACTS[0]) for g in ALLG6}
    stabF0 = sum(1 for g in ALLG6
                 if act_fact(g, FACTS[0]) == FACTS[0])
    check("C2.4 S6 facts MEASURED: max element order in S6 = %d == 6"
          " => NO order-30 element (predeclared fact (i)); S6 "
          "transitive on the 6 factorizations (orbit %d); |Stab(F)| "
          "= %d == 720/6 = 120 (the review's '60' corrected)"
          % (max_ord, len(orbF0), stabF0),
          max_ord == 6 and orbF0 == FSET and len(orbF0) == 6
          and stabF0 == 120, kill="K1")

    # Sp(4,2) census + Aut(C_fin) + the g pin
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

    def mmap(cols):
        return tuple(
            (cols[0] if v & 1 else 0) ^ (cols[1] if v & 2 else 0)
            ^ (cols[2] if v & 4 else 0) ^ (cols[3] if v & 8 else 0)
            for v in range(16))

    SPM = sorted({mmap(cols) for cols in SP})
    AUT = []
    for p in SPM:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        if len(set(p)) != 16:
            continue
        pis = [pi for pi in S5
               if all(IOTA[p[v]] == tuple(IOTA[v][pi[s]]
                                          for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    orders = sorted(perm_order(p) for p in AUT)
    g_cands = sorted(p for p in AUT if perm_order(p) == 6)
    g_pin = [p for p in g_cands if compose(p, p) == SIGP]
    G = g_pin[0] if len(g_pin) == 1 else None
    check("C2.5 Sp(4,2) census %d == 720; Aut(C_fin): |Aut| = %d == "
          "6, orders %s == [1,2,3,3,6,6]; FROZEN PIN g = the unique "
          "order-6 element with g^2 = sigma: %s (cfin_aut_flavor "
          "pin)" % (len(SPM), len(AUT), orders, len(g_pin) == 1),
          len(SPM) == 720 and len(AUT) == 6
          and orders == [1, 2, 3, 3, 6, 6] and len(g_pin) == 1,
          kill="K1")

    GINV = [0] * 16
    for v in range(16):
        GINV[G[v]] = v
    gv = tuple(arf1s.index(tuple(q[GINV[v]] for v in range(16)))
               for q in arf1s)
    ct_gv = cycle_type(gv)
    equiv = all(dmap[G[v]] == frozenset(gv[i] for i in dmap[v])
                for v in range(1, 16))
    check("C2.6 g on the K6 vertices: fixes the q* vertex v* = %d; "
          "vertex cycle type %s == (1,2,3); duad equivariance "
          "D(g v) = g_v D(v) on all 15 classes: %s"
          % (VSTAR, ct_gv, equiv),
          gv[VSTAR] == VSTAR and ct_gv == (1, 2, 3) and equiv,
          kill="K1")

    gF = {F: act_fact(gv, F) for F in FACTS}
    fidx = {F: i for i, F in enumerate(FACTS)}
    gF_perm = tuple(fidx[gF[FACTS[i]]] for i in range(6))
    ct_gF = cycle_type(gF_perm)
    is6cyc = (ct_gF == (6,))
    check("C2.7 TYPED: g on the 6 factorizations has cycle type %s "
          "-- outer duality Out(S6): class (1,2,3) <-> class (6) "
          "%s (a 6-cycle %s)" % (ct_gF,
                                 "CONFIRMED" if is6cyc else "FAILS",
                                 "exists" if is6cyc else "missing"),
          True, "measured, typed either way")

    others = [i for i in range(6) if i != VSTAR]
    rho = [0] * 6
    rho[VSTAR] = VSTAR
    for tpos in range(5):
        rho[others[tpos]] = others[(tpos + 1) % 5]
    rho = tuple(rho)
    M0 = frozenset({frozenset({VSTAR, others[0]}),
                    frozenset({others[1], others[4]}),
                    frozenset({others[2], others[3]})})
    F0_list = []
    m = M0
    for _ in range(5):
        F0_list.append(m)
        m = act_match(rho, m)
    F0 = frozenset(F0_list)
    rhoF_perm = tuple(fidx[act_fact(rho, FACTS[i])] for i in range(6))
    ct_rhoF = cycle_type(rhoF_perm)
    check("C2.8 frozen pentad rotation rho (fixes v*, 5-cycles the "
          "others ascending); starter M0; F0 = rho-orbit of M0 IS a "
          "one-factorization; rho on factorizations has cycle type "
          "%s == (1,5) fixing F0" % (ct_rhoF,),
          len(F0) == 5 and F0 in FSET and ct_rhoF == (1, 5)
          and rhoF_perm[fidx[F0]] == fidx[F0], kill="K1")

    gr = tuple(gv[rho[i]] for i in range(6))
    rg = tuple(rho[gv[i]] for i in range(6))
    commute = (gr == rg)
    grp = {tuple(range(6))}
    frontier = [tuple(range(6))]
    gens = [gv, rho]
    while frontier:
        nxt = []
        for p in frontier:
            for q in gens:
                pq = tuple(q[p[i]] for i in range(6))
                if pq not in grp:
                    grp.add(pq)
                    nxt.append(pq)
        frontier = nxt
    ords_grp = {perm_order(p) for p in grp}
    check("C2.9 TYPED commutation: g_v rho == rho g_v: %s; the "
          "group <g_v, rho> has order %d, element orders %s (max %d "
          "< 30) -- NO single vertex-side element carries the 30-"
          "clock (fact (i)); the 30-cycle lives on the ENTRIES"
          % (commute, len(grp), sorted(ords_grp), max(ords_grp)),
          True, "measured, typed either way")

    # the frozen CRT schedule
    if is6cyc:
        slot = [F0]
        for _ in range(5):
            slot.append(gF[slot[-1]])
        mode = "g-cycle order F_j = g_F^j(F0)"
    else:
        slot = list(FACTS)
        mode = "FALLBACK lex order (g_F not a 6-cycle, typed)"
    gvj = tuple(range(6))
    table = []
    mrow = [M0]
    for _ in range(4):
        mrow.append(act_match(rho, mrow[-1]))
    cur = list(mrow)
    for j in range(6):
        if is6cyc:
            table.append(list(cur))
            cur = [act_match(gv, m) for m in cur]
        else:
            table.append(sorted(slot[j],
                                key=lambda m: sorted(
                                    sorted(d) for d in m)))
    ok_slots = all(set(table[j]) == set(slot[j]) for j in range(6))
    ENT = {}
    for k in range(30):
        ENT[k] = (k % 6, table[k % 6][k % 5])
    pairs30 = {(j, frozenset(m)) for j, m in ENT.values()}
    occur = {}
    for k in range(30):
        occur.setdefault(ENT[k][1], []).append(k)
    check("C2.10 frozen CRT schedule assembled (%s): 30 entries, "
          "every (factorization, matching) pair exactly once; T = "
          "k -> k+1 is a 30-cycle (CRT of the order-6 slot shift "
          "and the order-5 phase shift ON ENTRIES); every matching "
          "occurs exactly twice" % mode,
          ok_slots and len(pairs30) == 30
          and all(len(v) == 2 for v in occur.values()),
          kill="K1")

    seps = sorted((occ[1] - occ[0]) % 30 for occ in occur.values())
    n15 = sum(1 for s in seps if s == 15)
    sheet_schedule = (n15 == 15)
    print("      schedule separations (k2-k1 mod 30) of the 15 "
          "matchings: %s" % seps)
    check("C2.11 TYPED schedule sheet census: %d of 15 matchings "
          "are 15 apart (pigeonhole bound 3 from fact (iii): only "
          "3 antipodal factorization pairs) -- the K6 schedule side "
          "%s realize the full 2 x 15 sheet pattern"
          % (n15, "CANNOT" if not sheet_schedule else "DOES"),
          True, "measured, typed either way")

    # ==================================================================
    section("C3 -- the intertwiner census (w-orbits vs 15 classes)")
    # ==================================================================
    seen = set()
    ORBITS = []
    for r in ROOTS:
        if r in seen:
            continue
        orb = [r]
        cur = wfun(r)
        while cur != r:
            orb.append(cur)
            cur = wfun(cur)
        seen |= set(orb)
        ORBITS.append(orb)
    sizes = sorted(len(o) for o in ORBITS)
    check("C3.1 ORBIT CENSUS: w acts on the 240 roots with %d "
          "orbits of sizes %s == 8 orbits of size 30 (rank x h; "
          "NOT 30 orbits of size 8 -- the review's alternative is "
          "settled by measurement)" % (len(ORBITS), sizes),
          len(ORBITS) == 8 and sizes == [30] * 8, kill="K2")

    # frozen lex-min family/anchor address basis (report-level pin)
    def sig_vec(v):
        return tuple(v[PI_SIG[k]] for k in range(8))

    sigL = [label_of(sig_vec(REPS[li])) for li in range(16)]
    fixed_nz = [li for li in range(1, 16) if sigL[li] == li]

    def lsum(la, lb):
        return label_of(tuple(a + b for a, b in
                              zip(REPS[la], REPS[lb])))

    def hbL(la, lb):
        x, y = REPS[la], REPS[lb]

        def J_vec(v):
            out = [0] * 8
            for k in range(4):
                out[2 * k] = -v[2 * k + 1]
                out[2 * k + 1] = v[2 * k]
            return tuple(out)

        re2, im2 = dot(x, y), dot(x, J_vec(y))
        return ((re2 // 2) + (im2 // 2)) % 2

    basis = None
    for o1 in range(1, 16):
        if o1 in fixed_nz:
            continue
        o2, o3 = sigL[o1], sigL[sigL[o1]]
        if len({o1, o2, o3}) != 3:
            continue
        fsum = lsum(lsum(o1, o2), o3)
        if fsum not in fixed_nz:
            continue
        for A in fixed_nz:
            if A == fsum:
                continue
            gram_ok = (hbL(o1, o1) == 0 and hbL(o2, o2) == 0
                       and hbL(o3, o3) == 0 and hbL(A, A) == 0
                       and all(hbL(x, y) == 1 for x, y in
                               itertools.combinations(
                                   (o1, o2, o3, A), 2)))
            if not gram_ok:
                continue
            span = set()
            for bits in range(16):
                acc = 0
                for pos, base in enumerate((o1, o2, o3, A)):
                    if (bits >> pos) & 1:
                        acc = lsum(acc, base)
                span.add(acc)
            if len(span) == 16:
                basis = (o1, o2, o3, A)
                break
        if basis:
            break
    ADDR = {}
    if basis:
        for bits in range(16):
            acc = 0
            for pos, base in enumerate(basis):
                if (bits >> pos) & 1:
                    acc = lsum(acc, base)
            ADDR[acc] = "".join(str((bits >> p) & 1)
                                for p in range(4))
    check("C3.2 report pin: lex-min family/anchor basis (F1,F2,F3,A)"
          " = labels %s with Gram(hbar) = J - I and sigma family "
          "action; 16 addresses bijective (the C3 census is "
          "invariant under any relabeling of V)" % (basis,),
          basis is not None and len(ADDR) == 16, kill="K2")

    shift_ok = True
    results = []
    for oi, orb in enumerate(ORBITS):
        base = min(orb)
        seq = [base]
        for _ in range(29):
            seq.append(wfun(seq[-1]))
        labs = [LB[r] for r in seq]
        shift_ok &= all(labs[(k + 15) % 30] == labs[k]
                        for k in range(30))
        cnt = Counter(labs)
        ndist = len(cnt)
        prof = sorted(cnt.values())
        fifteen_two = (prof == [2] * 15)
        sp_ok = True
        for lab, c in cnt.items():
            pos = [k for k in range(30) if labs[k] == lab]
            for p1, p2 in itertools.combinations(pos, 2):
                if (p2 - p1) % 30 not in (15,):
                    sp_ok = False
        results.append((oi, ndist, prof, fifteen_two,
                        fifteen_two and sp_ok))
        print("      orbit %d (base %s):" % (oi, (base,)))
        print("        addresses: %s"
              % " ".join(ADDR[lb] for lb in labs))
        print("        distinct classes %d/15; count profile %s; "
              "15x2: %s; all pair spacings = 15: %s"
              % (ndist, dict(Counter(prof)), fifteen_two, sp_ok))
    check("C3.3 ward: c_{k+15} = c_k on ALL 8 orbits (fact (ii) "
          "realized)", shift_ok, kill="K2")

    n_intertwined = sum(1 for r in results if r[4])
    n_partial = sum(1 for r in results if r[3] and not r[4])
    dist_census = sorted(r[1] for r in results)
    if n_intertwined > 0:
        typed = "SCHEDULE-INTERTWINED"
    elif n_partial > 0:
        typed = "SCHEDULE-PARTIAL"
    else:
        typed = "SCHEDULE-DEAD"
    check("C3.4 TYPED INTERTWINER CENSUS over all 8 orbits: "
          "orbits with 15 classes x 2 AND spacing 15: %d; 15 x 2 "
          "but wrong spacing: %d; distinct-class census per orbit "
          "= %s -> %s"
          % (n_intertwined, n_partial, dist_census, typed),
          True, "measured, typed either way")

    # ==================================================================
    section("C4 -- the exponent reading (report; numerology guard)")
    # ==================================================================
    m6 = [m % 6 for m in expos]
    m5 = [m % 5 for m in expos]
    pm1_6 = [m for m in expos if m % 6 in (1, 5)]
    pm1_5 = [m for m in expos if m % 5 in (1, 4)]
    check("C4.1 exponents mod 6 = %s (all in {1,5} = +-1: %d/8); "
          "mod 5 = %s (+-1: %d/8 = %s)"
          % (m6, len(pm1_6), m5, len(pm1_5), pm1_5),
          len(pm1_6) == 8 and len(pm1_5) == 4, kill="K2")
    check("C4.2 NUMEROLOGY GUARD (predeclared): the exponents are "
          "EXACTLY the units mod 30, so 'all +-1 mod 6' and 'units "
          "mod 5' are GENERIC consequences of gcd(m,30) = 1 for ANY "
          "h = 30 system -- NO schedule-specific content; a "
          "significant reading would need a schedule-derived "
          "selection among the units mod 30, which the corpus does "
          "not provide", True, "report line, no claim")

    # ==================================================================
    section("CTRL -- controls (must fire)")
    # ==================================================================
    ideal = list(range(1, 16)) + list(range(1, 16))
    rng = random.Random(49)
    shuf = ideal[:]
    rng.shuffle(shuf)
    broken = False
    for lab in range(1, 16):
        pos = [k for k in range(30) if shuf[k] == lab]
        if (pos[1] - pos[0]) % 30 != 15:
            broken = True
    check("CTRL1 FIRES: the ideal sheet sequence (every separation "
          "15) shuffled once with declared seed 49 BREAKS the "
          "pairing census: %s (counts stay 15 x 2, spacings do not "
          "survive a random 30-cycle)" % broken, broken, kill="K3")

    D8S = []
    for i in range(7):
        v = [0] * 8
        v[i], v[i + 1] = 1, -1
        D8S.append(tuple(v))
    v = [0] * 8
    v[6], v[7] = 1, 1
    D8S.append(tuple(v))

    def refl2(a, x):
        c = dot(x, a)
        return tuple(xi - c * ai for xi, ai in zip(x, a))

    def wD8(x):
        y = x
        for a in reversed(D8S):
            y = refl2(a, y)
        return y

    WD = sp.eye(8)
    for a in D8S:
        WD = WD * (sp.eye(8) - sp.Matrix([list(a)]).T
                   * sp.Matrix([list(a)]))
    PD = sp.eye(8)
    first_d = None
    for n in range(1, 15):
        PD = PD * WD
        if first_d is None and PD == sp.eye(8):
            first_d = n
    cp_d = WD.charpoly(t).as_expr()
    want_d = sp.expand(sp.cyclotomic_poly(14, t)
                       * sp.cyclotomic_poly(2, t) ** 2)
    D8R = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0] * 8
                v[i], v[j] = si, sj
                D8R.append(tuple(v))
    seend = set()
    dorb = []
    for r in D8R:
        if r in seend:
            continue
        orb = [r]
        cur = wD8(r)
        while cur != r:
            orb.append(cur)
            cur = wD8(cur)
        seend |= set(orb)
        dorb.append(len(orb))
    check("CTRL2 FIRES: D8 control: ord(w_D8) = %s == 14 = h(D8) != "
          "30; charpoly = %s == Phi_14 Phi_2^2 (exponents 1,3,5,7,7,"
          "9,11,13); orbits on the 112 roots: %d of sizes %s == 8 x "
          "14; every orbit length 14 < 30 = 2 x 15 => the 15-pair "
          "sheet census is arithmetically IMPOSSIBLE at h = 14"
          % (first_d, sp.factor(cp_d), len(dorb),
             sorted(set(dorb))),
          first_d == 14 and sp.expand(cp_d - want_d) == 0
          and len(dorb) == 8 and sorted(dorb) == [14] * 8
          and 14 < 30, kill="K3")

    # ==================================================================
    section("VERDICT")
    # ==================================================================
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS
                      if nm.startswith("CTRL"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = "PIPELINE-BROKEN"
    else:
        VERDICT = "COXSCHEDULE-MEASURED + " + typed
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * E8 side: ord(w) = 30 exact, charpoly = Phi_30 (exponents = the
    units mod 30, all odd => w^15 = -1); the 240 roots fall into 8
    orbits of size 30 (rank x h), settling 8x30 vs 30x8; the class
    sequence of every orbit repeats after 15 steps AUTOMATICALLY
    (central involution + 2L in (1+i)L), so only the 15-class
    bijection question carries content -- census above.
  * K6 side: 6 factorizations x 5 matchings = 30 = 2 x 15 verified;
    S6 has NO order-30 element (max 6), so the 30-clock lives on
    the ENTRIES (CRT of the C6 slot shift and the C5 phase shift);
    any two factorizations share exactly one matching, so at most
    3 of 15 matchings can sit 15 apart in ANY 6 x 5 CRT schedule --
    the K6 side cannot mirror a full 2 x 15 sheet pattern.
  * The two 30-cycles are Z/30 torsors (trivially isomorphic); the
    review's finer 2 x 15 intertwiner is typed above from the
    measured censuses; no physics claim, no marker move.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot
                 and VERDICT.startswith("COXSCHEDULE-MEASURED")) else 1


if __name__ == "__main__":
    raise SystemExit(main())
