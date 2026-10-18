#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v857 -- E8.SIMPLEX.FOURIER.01 + FLAVOR.WINDING.QUADRATIC.01: the E8 audits, part I -- the Gaussian census IS a Fourier law and v817's per-prime measurement is the prime restriction of a CHARACTER THEOREM (mh2(n) = -1/15 as an integer identity at EVERY odd n <= 16500), and the tfpt_2 winding line collapses to ONE rank-one determinant quadratic q_wind = t^2 - g_car t + |Z2| with the triple lock s = 6 and the reality threshold typed, ONE module from two probes (26/26 + 20/20 checks, zero fails, verdicts SIMPLEX-FOURIER-EXACT + INTERTWINER-IDENTIFIED and WINDING-QUADRATIC-EXACT; discovery probes simplex_fourier_probe.py and flavor_winding_quadratic_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, exact integer/Fraction/sympy arithmetic, ~2 s).  PART A, THE FOURIER LAW (audit package A): the Construction-A rebuild is warded (30 placements, 2 invariant under pi_J and pi_sigma; 240 roots, all norm 4, all in L; the quotient V = L/(1+i)L = F_2^4 with class addition well-defined on all 256 pairs and every class 2-torsion), the census r = (0; 16^15) (zero class EMPTY, v833/v844) has the EXACT Walsh transform rhat = (240; -16 x15) with the inversion sum rule, i.e. the normalized spectrum {1, (-1/15)^15}: the uniform-nonzero channel P = (J - I)/15 entrywise in Fractions (doubly stochastic; eigenaction exact on all 16 characters; two-step P^2 = (I + 14J)/225 with contraction 1/225); THE FIVE-LINE THEOREM measured at every level: (i) RAMIFICATION -- Theta_0(n) = 0 for EVERY odd n <= 16 with the one-line proof (x = (1+i)y forces even level) and Theta_0(2m) = 240 sigma_3(m); (ii) EQUIDISTRIBUTION -- Theta_v(n) is ONE value over the 15 nonzero classes at every level n <= 16 (the Sp(4,2) footprint); (iii) hence Thetahat_u(odd n) = -Theta_L(n)/15; (iv) THE INTERTWINER IDENTITY -- the v817 packet numerator (Th0-Th1+Th2-Th3)(n) EQUALS the code Walsh transform Thetahat_u(n) for every nonzero u at EVERY level n <= 16, odd AND even (both ladders read [-16, 112, -448, 1136, -2016, 3136, -5504, 9328] at n = 1..8; the Eisenstein normal form 15 Theta_D8 = 7 Theta_L + 8 Theta_0 across machineries); (v) THE VALUE THEOREM -- 15 (Th0-Th1+Th2-Th3)(n) = -240 sigma_3(n) for EVERY odd n <= 16500, hence mh2(odd n) = -1/15 IDENTICALLY, covering all 1911 odd primes <= 16500: v817's per-prime measurement is a character theorem of the code, one Walsh transform away from the deployed census with NO new input.  THE HONEST TYPE (measured, kept): the identification is SPECTRAL (numerator q-series equal) -- the packet 5|3-parity grading (52, 60, 128) and the code grading (15 x 16) do NOT refine each other (the S6.3 cross table: 4 + 3 + 8 mixed classes); the spinor halving Th1 = Th3 stays numerical fiat (typed); 52 = 40 + 12 = |R(D5)| + |R(A3)| is the seam reading.  Controls fire (occupied zero class, one class at 15, wrong quotient dim F_2^3 -- each breaks the law at a stated integer), invariances hold (24 explicit isometries of (L, J) preserve census and spectrum; the OTHER invariant placement C** gives the identical law).  PART B, THE WINDING QUADRATIC (audit package for tfpt_2, section I.5): against the deployed residue matrix (det R = 8 = h(D5), tr R = 9, PrinMin2 = (5,3,2), SNF (1,1,8), anchor R e1 = (1,1,2), cofactor seam normal adj(R) row 1 = (5,-9,6) with n.1 = 2 = |Z2|), THE MINI-THEOREM: chi_{R_s} - chi_R = -s q_wind with q_wind = e1^T adj(tI - R) 1 = t^2 - 5t + 2 = t^2 - g_car t + |Z2| EXACT in sympy -- the whole winding line is one rank-one matrix-determinant lemma; the keybox coefficients (9+s, 10+5s, 8+2s), the per-winding det increment d(det R_s)/ds = q_wind(0) = 2 = |Z2| and the minor law PrinMin2(R_s) = (5, 3(s+1), 2(s+1)) (carrier minor 5 s-INVARIANT) are all readouts of the single quadratic; q_wind is irreducible over Q (disc 17 nonsquare) and the two base points are s-invariant (rem(chi_{R_s}, q_wind) = -12t, s-free); THE TRIPLE LOCK: trace (tr R_s = 15), determinant (det R_s = 20) and Coxeter lift ((R_s^T a)_1 = 30) each solve to s = 6 ALONE, intersection {6} = {|R+(A3)|}, and at s = 6: chi_L = t^3 - 15t^2 + 40t - 20 with (15, 40, 20) = (dim A3, |R(D5)|, |R(A4)|), 3 real positive roots; THE LOCUS (exact Sturm/resultant): Delta(s) = disc_t chi_{R_s} = 17s^4 - 18s^3 + 709s^2 + 588s - 7996 (irreducible), Delta(6) = 39200 = 2^5 5^2 7^2 = 2 x 140^2 > 0 -- s = 6 is NOT a collision point; the reality threshold is the unique Delta-root in (2, 3), s* ~ 2.8250 (matching the deployed ~2.83; Sturm real-eigenvalue counts jump 1 -> 3 between s = 2 and s = 3); the integer-window census types s = 6 as the ONLY 2xsquare hit in s = -2..12 (measured, typed -- and q_wind(6) = 8 = det R reported as a measured coincidence).  Controls fire: the sibling directions 1 e2^T and 1 e3^T change the quadratic AND break the lock (intersections EMPTY; 1 e3^T even reducible), the sibling ROW transport e1 1^T keeps -g_car t but LOSES |Z2| (locks pairwise disjoint 6/12/24), and the sibling minor branch {1,3,4} is unreachable on the whole winding line (integer scan s = -100..100 empty; the carrier minor 5 invariant) -- the triple (1, -5, 2) is direction-specific.  Both parts are exact-arithmetic corpus compressions and audits of DEPLOYED claims (v817, v833, v844, v4/v94 keyboxes) -- normal forms and identities, no new physical claim, no marker moves.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes simplex_fourier_probe.py (26/26,
verdict SIMPLEX-FOURIER-EXACT + INTERTWINER-IDENTIFIED) and
flavor_winding_quadratic_probe.py (20/20, verdict
WINDING-QUADRATIC-EXACT), both 2026-08-08, re-run identically at
promotion.  ROUND-31 EMBEDDING CONVENTION: both frozen sources are
embedded BYTE-EXACT (raw strings below) and executed verbatim in
isolated module namespaces registered under their canonical import
names -- the printed FROZEN_SPEC SHA-256 values reproduce exactly,
and when the original files are present the harness verifies
byte-equality (provenance ward inside the pattern gate).  The
original probe files live verbatim in experiments/tfpt-discovery/.

FIREWALL: exact integer / Fraction / sympy arithmetic throughout;
own sieves (sigma_3, theta series by residue DP); no zeros, no
prime tables, no floats in any load-bearing identity.  NO RH claim.
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

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_FOURIER = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""simplex_fourier_probe -- E8.SIMPLEX.FOURIER.01 (audit package A of the
2026-08-08 morning analysis): the Fourier law of the Gaussian census and
the intertwiner check against the prime-packet m2 channel.

FROZEN CLAIMS (2026-08-08, frozen + SHA-hashed before first run):

PART (a) -- THE FOURIER LAW on V = L/(1+i)L = F_2^4:
 S1  REBUILD (read-only machinery, v833/v844 S2-S3 rebuilt inline):
     Construction-A Gaussian E8 over the unique mu4/sigma-invariant
     placement C* (2 of 30, the W0246 pick); 240 roots, all norm 4;
     the quotient Q = L/(1+i)L has EXACTLY 16 classes, every class is
     2-torsion (2x = -i(1+i)^2 x in (1+i)L, typed + verified), the
     class addition closes and coordinatizes as F_2^4 (4 independent
     generators, 16 sums bijective); the root multiplicity function is
     r(0) = 0 (zero class EMPTY), r(v) = 16 for ALL 15 nonzero v
     (the census 240 = 15 x 16, v844 S3.1 rebuilt).
 S2  WALSH TRANSFORM (exact integers): rhat(u) = sum_v (-1)^{u.v} r(v):
     rhat(0) = 240; rhat(u) = -16 for ALL 15 nonzero u; inversion sum
     rule sum_u rhat(u) = 16 r(0) = 0; normalized spectrum
     rhat(u)/rhat(0) = {1, (-1/15)^15} with -16/240 = -1/15 exact.
 S3  THE CHANNEL (exact Fractions): the transition matrix of "add a
     uniformly random NONZERO class", P[x][y] = r(y-x)/240, equals
     (J - I)/15 ENTRYWISE on all 256 cells (J = all-ones, 16 x 16);
     doubly stochastic; eigenaction EXACT on all 16 characters:
     P chi_0 = chi_0 and P chi_u = (-1/15) chi_u for all 15 nonzero u
     (spec {1, (-1/15)^15}); two-step contraction: P^2 = (I + 14J)/225
     with nonzero-character eigenvalue exactly 1/225.

PART (b) -- THE INTERTWINER CHECK (the five-line theorem, measured):
 S4  CODE SIDE AT ALL LEVELS (exact python-int DP over the 4096 mod-4
     residues of L; class label from x mod 4 since 4Z^8 in 2L in
     (1+i)L): the 16 class thetas Theta_v(n) = #{x in L : |x|^2 = 4n,
     x = v mod (1+i)L} for 1 <= n <= NCAP = 16, gated by the
     independent sigma_3 sieve (sum_v Theta_v(n) = 240 sigma_3(n)) and
     by the level-1 census (= r); residue fibers all 256.
     S4.2 RAMIFICATION: Theta_0(n) = 0 for EVERY odd n (typed one-line
     proof: x = (1+i)y => |x|^2 = 2|y|^2 with |y|^2 in 4Z => level
     even) and Theta_0(2m) = 240 sigma_3(m) (the (1+i)-scaling
     Theta_0 = Theta_L(q^2)).
     S4.3 EQUIDISTRIBUTION AT EVERY LEVEL: Theta_v(n) equal over the
     15 nonzero v for all n <= NCAP (the Sp(4,2)-transitivity
     footprint, MEASURED not cited).
     S4.4 THE CHARACTER THEOREM: hence Thetahat_u(n) is one value for
     all 15 nonzero u, = (16 Theta_0(n) - Theta_L(n))/15; at odd n
     (ramification) Thetahat_u(n) = -Theta_L(n)/15, i.e. the
     normalized Walsh coefficient is EXACTLY -1/15 at every odd level.
 S5  PACKET SIDE (v817 packet machinery rebuilt read-only, VERBATIM
     semantics; numpy int64 with v817's own exactness certificates --
     the divisibility gates and the glue identity; N_THETA = 16500):
     S5.1 re-gate v817 C1: theta heads (Th_0..Th_3)(1) = (52,64,60,64);
     glue identity Th_0+Th_1+Th_2+Th_3 = 240 sigma_3(n) for ALL
     n <= 16500; Th_1 = Th_3; Th_0 - Th_2 = -8 f8 on ALL odd n.
     S5.2 THE m2 CHANNEL TYPED: in v817 event_profile the j = 2 sector
     multiplier is mh[2](n) = (Th_0 - Th_1 + Th_2 - Th_3)(n) /
     (240 sigma_3(n)) -- the order-2 character of the Z4 factor of the
     register G = C2 x F_2^4 x Z4; the packet's level-1 classes are
     the 5|3 PARITY classes of the standard model: (52, 60, 128) =
     (D8-even, D8-odd, spinor), re-derived HERE from the actual 240
     standard-model roots, with 52 = 40 + 12 = |R(D5)| + |R(A3)| (the
     seam reading) and 128 = 2 x 64 (the spinor halving Th_1 = Th_3 is
     numerical fiat in v817, not a set partition -- typed).
     S5.3 THE VALUE THEOREM (exact integer identity, ALL odd levels):
     15 (Th_0 - Th_1 + Th_2 - Th_3)(n) = -240 sigma_3(n) for EVERY odd
     n <= 16500, hence mh2(n) = -1/15 identically on odd levels; the
     v817 statement "mh2(p) = -1/15 for every odd prime" is the prime
     restriction (count of odd primes covered reported).
 S6  THE IDENTIFICATION (cross-machinery, the decision):
     S6.1 THE INTERTWINER IDENTITY: the packet numerator EQUALS the
     code Walsh transform, (Th_0 - Th_1 + Th_2 - Th_3)(n) =
     Thetahat_u(n) for EVERY nonzero u and EVERY level 1 <= n <= NCAP
     (odd AND even); equivalently the Eisenstein normal form
     15 Theta_D8(n) = 7 Theta_L(n) + 8 Theta_0(n) with Theta_D8 =
     Th_0 + Th_2 taken from the PACKET machinery and Theta_L, Theta_0
     from the CODE machinery.  Level 1 is the census law -16 = rhat(u).
     S6.2 hence the packet's m2 multiplier at odd events IS the
     nontrivial eigenvalue of the Walsh channel P: mh2(odd) = -1/15 =
     spec(P)|_{u != 0}, a CHARACTER THEOREM of the code (ramification
     S4.2 + equidistribution S4.3), not a per-prime computation; the
     two-odd-event contraction is the two-step 1/225 of S3.
     S6.3 TYPED TRANSVERSALITY (measured, no narrative): on the SAME
     240 standard-model roots the code census (15 x 16, zero empty --
     model-independence witnessed) and the packet parity partition
     (52, 60, 128) do NOT refine each other (52 and 60 are not
     multiples of 16; contingency table printed) -- the identification
     is SPECTRAL (equality of numerator q-series), not a quotient-map
     intertwiner.  This is a report line, not a kill, either way.

 C   MUST-BREAK CONTROLS (each must fire):
     C1 OCCUPIED ZERO CLASS: r'(0) = 16 (keep 15 x 16): Walsh becomes
        (256; 0 x15), normalized {1, 0^15} != {1, (-1/15)^15}; the
        two-step contraction becomes 0 != 1/225.
     C2 PERTURBED MULTIPLICITY: one nonzero class at 15: Walsh multiset
        on u != 0 becomes {-17 x7, -15 x8} (u.x0 = 0 seven times) --
        NOT uniform, and no value equals -16; the -1/15 law breaks.
     C3 WRONG QUOTIENT DIM (F_2^3): 240/7 is NOT an integer (uniform
        integer multiplicity impossible); the uniform nonzero channel
        on F_2^3 has eigenvalue -1/7 != -1/15 and two-step 1/49 !=
        1/225.
 I   MUST-BE-INVARIANT:
     I1 SYMPLECTIC/ISOMETRY RELABELING: explicit isometries of (L, J)
        -- sigma (PI_SIG), the C*-preserving pair permutations (of the
        24 order-preserving pair perms), the C*-preserving single-pair
        quarter turns (measured which); global J and -1 induce the
        IDENTITY on V (verified); each accepted isometry induces a
        WELL-DEFINED F_2-linear map on V (verified on all 240 roots),
        preserves the census, and preserves the Walsh spectrum as a
        multiset.  (Full Sp(4,2)-orbit transitivity is DELEGATED to
        the measured per-level equidistribution S4.3.)
     I2 EQUIVALENT CONSTRUCTION-A REPRESENTATIVE: the OTHER
        mu4/sigma-invariant placement C** (the second of the 2): full
        rebuild gives the SAME census (15 x 16, zero empty) and the
        SAME Walsh spectrum (240; -16 x15).

KILLS (any one fires => typed failure):
  K1 rebuild / quotient / census breaks             -> FOURIER-CENSUS
  K2 Walsh law (S2) breaks                          -> FOURIER-LAW
  K3 channel identity / spectrum (S3) breaks        -> FOURIER-CHANNEL
  K4 a control does not fire                        -> CONTROL-DEAD
  K5 an invariance breaks                           -> INVARIANCE-BROKEN
  K6 code-side law (S4) breaks                      -> INTERTWINER-GAP-CODE
  K7 packet re-gate (S5.1/S5.2) breaks              -> INTERTWINER-GAP-PACKET
  K8 value theorem (S5.3) breaks                    -> INTERTWINER-GAP-VALUE
  K9 bridge identity (S6.1) breaks                  -> INTERTWINER-GAP-BRIDGE

VERDICT (frozen enum): "SIMPLEX-FOURIER-EXACT + INTERTWINER-IDENTIFIED"
/ "SIMPLEX-FOURIER-EXACT + INTERTWINER-GAP-<TYPE>" / typed failure
(FOURIER-MISMATCH-<K>, CONTROL-DEAD, INVARIANCE-BROKEN).

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact integer/Fraction arithmetic; the packet
layer uses numpy int64 with v817's own exact-equality certificates; no
floats in any decision, no RNG, no fits.  NO physics claim, NO RH
claim.  Runtime cap: minutes.

Sources (read-only, machinery rebuilt inline): verification/
v833_gaussian_ramification_ladder.py + v844_message_doily_rank.py
(Construction A, census, class machinery), v817_positive_descent_
master.py (packet thetas, event_profile m2 channel), v634_st31_
structure.py (standard-model roots + J), v800_e8_torsor_fourier.py
(Fourier precedent), tfpt_2/tfpt_1 budget lines (240 = 15 x 16).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/simplex_fourier_probe.py
"""
import hashlib
import itertools
import math
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
CHECKS = []
KILLS = []

NCAP = 16          # code-side theta levels (exact python ints)
N_THETA = 16500    # packet-side reach (v817 value)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("=" * 74)
print("E8.SIMPLEX.FOURIER.01 -- the Fourier law of the Gaussian census and")
print("the prime-packet m2 intertwiner (audit package A)")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

# ======================================================================
section("S1: Construction-A rebuild + the quotient V = L/(1+i)L (v833/v844)")
# ======================================================================
G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2 for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)
W0246 = (1, 0, 1, 0, 1, 0, 1, 0)


def code_image(code, perm):
    return frozenset(tuple(c[perm[k]] for k in range(8)) for c in code)


placements = set()
for perm in itertools.permutations(range(8)):
    placements.add(code_image(C_NAIVE, perm))
BOTH = [c for c in placements
        if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
check("S1.1 placement census: %d placements, %d invariant under pi_J and "
      "pi_sigma (v833 R1.3); C* = the W0246 pick"
      % (len(placements), len(BOTH)),
      len(placements) == 30 and len(BOTH) == 2
      and sum(1 for c in BOTH if W0246 in c) == 1, kill="K1")
CSTAR = next(c for c in BOTH if W0246 in c)
CSTAR2 = next(c for c in BOTH if W0246 not in c)


def build_roots(code):
    roots = []
    for k in range(8):
        for s in (2, -2):
            v = [0] * 8
            v[k] = s
            roots.append(tuple(v))
    for c in (c for c in code if sum(c) == 4):
        sup = [k for k in range(8) if c[k]]
        for signs in itertools.product((1, -1), repeat=4):
            v = [0] * 8
            for k, s in zip(sup, signs):
                v[k] = s
            roots.append(tuple(v))
    return roots


def J_vec(v):
    out = [0] * 8
    for k in range(4):
        out[2 * k] = -v[2 * k + 1]
        out[2 * k + 1] = v[2 * k]
    return tuple(out)


def make_tests(code):
    def in_L(v):
        return tuple(x % 2 for x in v) in code

    def in_pi2L(v):
        # x in (1+i)L  <=>  (1-J)x/2 in L   (v844 S3 machinery)
        w = [0] * 8
        for k in range(4):
            w[2 * k] = v[2 * k] + v[2 * k + 1]
            w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
        if any(x % 2 for x in w):
            return False
        return in_L([x // 2 for x in w])

    return in_L, in_pi2L


in_L, in_pi2L = make_tests(CSTAR)
ROOTS = build_roots(CSTAR)
check("S1.2 root census: %d roots, distinct, all norm 4, all in L"
      % len(ROOTS),
      len(ROOTS) == 240 and len(set(ROOTS)) == 240
      and all(sum(x * x for x in r) == 4 for r in ROOTS)
      and all(in_L(r) for r in ROOTS), kill="K1")


def class_reps(roots, test):
    reps = []
    label = {}
    for r in roots:
        for li, rep in enumerate(reps):
            if test(tuple(x - y for x, y in zip(r, rep))):
                label[r] = li
                break
        else:
            label[r] = len(reps)
            reps.append(r)
    return reps, label


reps15, label = class_reps(ROOTS, in_pi2L)
ZERO = (0,) * 8
REPS16 = [ZERO] + list(reps15)


def cls16(v):
    hits = [k for k in range(16)
            if in_pi2L(tuple(a - b for a, b in zip(v, REPS16[k])))]
    return hits


# group law on the 16 classes (verify uniqueness of the sum class)
ADD = [[None] * 16 for _ in range(16)]
add_unique = True
for a in range(16):
    for b in range(16):
        s = tuple(x + y for x, y in zip(REPS16[a], REPS16[b]))
        hits = cls16(s)
        if len(hits) != 1:
            add_unique = False
        else:
            ADD[a][b] = hits[0]
two_torsion = all(ADD[a][a] == 0 for a in range(16))
check("S1.3 quotient: 1 + %d = 16 classes; class addition well-defined "
      "(unique sum class on all 256 pairs); EVERY class 2-torsion "
      "(2x = -i(1+i)^2 x in (1+i)L)" % len(reps15),
      len(reps15) == 15 and add_unique and two_torsion, kill="K1")

# coordinatize as F_2^4
basis = []
span = {0}
for k in range(1, 16):
    if k not in span:
        basis.append(k)
        span = {ADD[x][y] for x in span for y in span | {k}} | span | {k}
        closure = {0}
        frontier = [0]
        gens = list(basis)
        seen = {0}
        while frontier:
            x = frontier.pop()
            for g in gens:
                y = ADD[x][g]
                if y not in seen:
                    seen.add(y)
                    frontier.append(y)
        span = seen
COORD = {}
ok_coord = (len(basis) == 4)
if ok_coord:
    for bits in itertools.product((0, 1), repeat=4):
        c = 0
        for i, b in enumerate(bits):
            if b:
                c = ADD[c][basis[i]]
        if c in COORD:
            ok_coord = False
        COORD[c] = bits
check("S1.4 coordinatization: %d independent generators; the 16 subset "
      "sums biject onto the 16 classes (V = F_2^4)" % len(basis),
      ok_coord and len(COORD) == 16, kill="K1")

r_census = [0] * 16
for r in ROOTS:
    hits = cls16(r)
    r_census[hits[0]] += 1
check("S1.5 multiplicity function: r(0) = %d (zero class EMPTY); "
      "r(v) = 16 for all 15 nonzero v (census 240 = 15 x 16, v844 S3.1)"
      % r_census[0],
      r_census[0] == 0 and sorted(r_census[1:]) == [16] * 15, kill="K1")

# ======================================================================
section("S2: the Walsh transform of the census (exact integers)")
# ======================================================================


def walsh(census):
    out = {}
    for u in itertools.product((0, 1), repeat=4):
        acc = 0
        for k in range(16):
            v = COORD[k]
            dot = sum(a * b for a, b in zip(u, v)) % 2
            acc += (-1) ** dot * census[k]
        out[u] = acc
    return out


RHAT = walsh(r_census)
U0 = (0, 0, 0, 0)
nonzero_vals = [RHAT[u] for u in RHAT if u != U0]
check("S2.1 rhat(0) = %d == 240; inversion sum rule sum_u rhat(u) = %d "
      "== 16 r(0) = 0" % (RHAT[U0], sum(RHAT.values())),
      RHAT[U0] == 240 and sum(RHAT.values()) == 0, kill="K2")
check("S2.2 rhat(u) = -16 for ALL 15 nonzero u (values %s)"
      % sorted(set(nonzero_vals)),
      nonzero_vals == [-16] * 15, kill="K2")
check("S2.3 normalized spectrum {1, (-1/15)^15}: -16/240 = %s == -1/15"
      % Fr(-16, 240),
      Fr(-16, 240) == Fr(-1, 15)
      and sorted(Fr(RHAT[u], RHAT[U0]) for u in RHAT)
      == [Fr(-1, 15)] * 15 + [Fr(1)], kill="K2")

# ======================================================================
section("S3: the channel P = (J - I)/15 (exact Fractions)")
# ======================================================================
P = [[Fr(r_census[ADD[x][y]], 240) for x in range(16)] for y in range(16)]
ok_P = all(P[y][x] == (Fr(0) if x == y else Fr(1, 15))
           for x in range(16) for y in range(16))
ok_stoch = (all(sum(P[y][x] for y in range(16)) == 1 for x in range(16))
            and all(sum(P[y][x] for x in range(16)) == 1 for y in range(16)))
check("S3.1 P[x][y] = r(y-x)/240 == (J - I)/15 ENTRYWISE (256 cells); "
      "doubly stochastic", ok_P and ok_stoch, kill="K3")

ok_eig = True
for u in itertools.product((0, 1), repeat=4):
    chi = [Fr((-1) ** (sum(a * b for a, b in zip(u, COORD[k])) % 2))
           for k in range(16)]
    Pchi = [sum(P[y][x] * chi[x] for x in range(16)) for y in range(16)]
    lam = Fr(1) if u == U0 else Fr(-1, 15)
    if Pchi != [lam * c for c in chi]:
        ok_eig = False
check("S3.2 eigenaction exact on all 16 characters: P chi_0 = chi_0, "
      "P chi_u = (-1/15) chi_u (spec {1, (-1/15)^15})", ok_eig, kill="K3")

P2 = [[sum(P[y][z] * P[z][x] for z in range(16)) for x in range(16)]
      for y in range(16)]
ok_P2 = all(P2[y][x] == (Fr(15, 225) if x == y else Fr(14, 225))
            for x in range(16) for y in range(16))
check("S3.3 two-step: P^2 = (I + 14J)/225 entrywise; nonzero-character "
      "eigenvalue (-1/15)^2 = %s == 1/225" % (Fr(-1, 15) ** 2,),
      ok_P2 and Fr(-1, 15) ** 2 == Fr(1, 225), kill="K3")

# ======================================================================
section("S4: code side at all levels -- class thetas by mod-4 residue DP")
# ======================================================================
EMAX = 4 * NCAP
DIGIT_THETA = {}
for d in range(4):
    poly = {}
    for z in range(-8, 9):
        e = (d + 4 * z) ** 2
        if e <= EMAX:
            poly[e] = poly.get(e, 0) + 1
    DIGIT_THETA[d] = poly


def poly_mul(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = ea + eb
            if e <= EMAX:
                out[e] = out.get(e, 0) + ca * cb
    return out


THETA = [[0] * (NCAP + 1) for _ in range(16)]
fibers = [0] * 16
for c in CSTAR:
    for sbits in itertools.product((0, 1), repeat=8):
        rvec = tuple(c[i] + 2 * sbits[i] for i in range(8))
        hits = cls16(rvec)
        assert len(hits) == 1
        k = hits[0]
        fibers[k] += 1
        poly = {0: 1}
        for i in range(8):
            poly = poly_mul(poly, DIGIT_THETA[rvec[i]])
        for n in range(NCAP + 1):
            THETA[k][n] += poly.get(4 * n, 0)

sigma3 = [0] * (2 * N_THETA + 1)
for d in range(1, 2 * N_THETA + 1):
    for m in range(d, 2 * N_THETA + 1, d):
        sigma3[m] += d ** 3

tot_ok = all(sum(THETA[k][n] for k in range(16)) == 240 * sigma3[n]
             for n in range(1, NCAP + 1))
lvl1 = [THETA[k][1] for k in range(16)]
check("S4.1 DP gates: residue fibers all 256 (%s); sum_v Theta_v(n) = "
      "240 sigma_3(n) for 1 <= n <= %d (independent sieve); level-1 "
      "census == r" % (sorted(set(fibers)), NCAP),
      sorted(set(fibers)) == [256] and tot_ok and lvl1 == r_census,
      kill="K6")

odd_zero = all(THETA[0][n] == 0 for n in range(1, NCAP + 1, 2))
even_scale = all(THETA[0][2 * m] == 240 * sigma3[m]
                 for m in range(1, NCAP // 2 + 1))
check("S4.2 RAMIFICATION: Theta_0(n) = 0 for EVERY odd n <= %d (proof: "
      "x = (1+i)y => |x|^2 = 2|y|^2 in 8Z => level even); Theta_0(2m) = "
      "240 sigma_3(m) (the (1+i)-scaling)" % NCAP,
      odd_zero and even_scale, kill="K6")

equi = all(len(set(THETA[k][n] for k in range(1, 16))) == 1
           for n in range(1, NCAP + 1))
check("S4.3 EQUIDISTRIBUTION at EVERY level n <= %d: Theta_v(n) is one "
      "value over the 15 nonzero classes (Sp(4,2) footprint, measured)"
      % NCAP, equi, kill="K6")

THAT = {}
for u in itertools.product((0, 1), repeat=4):
    THAT[u] = [sum((-1) ** (sum(a * b for a, b in zip(u, COORD[k])) % 2)
                   * THETA[k][n] for k in range(16))
               for n in range(NCAP + 1)]
one_val = all(len(set(THAT[u][n] for u in THAT if u != U0)) == 1
              for n in range(1, NCAP + 1))
uref = next(u for u in THAT if u != U0)
law_all = all(15 * THAT[uref][n] == 16 * THETA[0][n] - 240 * sigma3[n]
              for n in range(1, NCAP + 1))
law_odd = all(15 * THAT[uref][n] == -240 * sigma3[n]
              for n in range(1, NCAP + 1, 2))
check("S4.4 CHARACTER THEOREM: Thetahat_u(n) is ONE value for all 15 "
      "nonzero u, = (16 Theta_0 - Theta_L)/15; at odd n it is "
      "-Theta_L(n)/15, i.e. normalized ratio -1/15 at every odd level",
      one_val and law_all and law_odd, kill="K6")
print("      levels 1..8 of Thetahat_u (u != 0): %s"
      % [THAT[uref][n] for n in range(1, 9)])

# ======================================================================
section("S5: packet side -- v817 machinery rebuilt read-only (int64 + "
        "certificates)")
# ======================================================================


def sparse_theta_terms(kind, cap):
    out = []
    if kind in ("th3", "th4"):
        out.append((0, 1))
        n = 1
        while n * n <= cap:
            out.append((n * n, 2 if kind == "th3" else 2 * ((-1) ** n)))
            n += 1
    else:                                   # th2-type: odd squares
        o = 1
        while o * o <= cap:
            out.append((o * o, 2))
            o += 2
    return out


def sparse_mul(dense, terms):
    out = np.zeros_like(dense)
    for e, c in terms:
        if e == 0:
            out += c * dense
        else:
            out[e:] += c * dense[:-e]
    return out


def build_thetas():
    """exact class thetas Th_j, sigma3, f8 coefficients to N_THETA
    (v817 build_thetas, rebuilt verbatim)."""
    sig3 = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(1, N_THETA + 1):
        sig3[d::d] += d ** 3
    scap = 2 * N_THETA
    t3 = sparse_theta_terms("th3", scap)
    t4 = sparse_theta_terms("th4", scap)
    one = np.zeros(scap + 1, dtype=np.int64)
    one[0] = 1
    p3 = one.copy()
    p4 = one.copy()
    for _ in range(8):
        p3 = sparse_mul(p3, t3)
        p4 = sparse_mul(p4, t4)
    m53 = one.copy()
    for _ in range(5):
        m53 = sparse_mul(m53, t3)
    for _ in range(3):
        m53 = sparse_mul(m53, t4)
    m35 = one.copy()
    for _ in range(5):
        m35 = sparse_mul(m35, t4)
    for _ in range(3):
        m35 = sparse_mul(m35, t3)
    num0 = p3 + m53 + m35 + p4
    num2 = p3 - m53 - m35 + p4
    ok_div = bool(np.all(num0 % 4 == 0) and np.all(num2 % 4 == 0))
    Th0 = (num0 // 4)[::2][:N_THETA + 1].copy()
    Th2 = (num2 // 4)[::2][:N_THETA + 1].copy()
    tcap = 8 * N_THETA
    t2 = sparse_theta_terms("th2", tcap)
    acc = np.zeros(tcap + 1, dtype=np.int64)
    acc[0] = 1
    for _ in range(8):
        acc = sparse_mul(acc, t2)
    ok_div &= bool(np.all(acc[::8][:N_THETA + 1] % 4 == 0))
    Th1 = (acc[::8][:N_THETA + 1] // 4).copy()
    tk = np.zeros(N_THETA + 1, dtype=np.int64)
    for d in range(2, N_THETA + 1, 2):
        tk[d::d] += d * (4 + (4 if d % 4 == 0 else 0))
    g = np.zeros(N_THETA, dtype=np.int64)
    g[0] = 1
    for n in range(1, N_THETA):
        s = int(np.dot(tk[1:n + 1], g[n - 1::-1]))
        q, rr = divmod(-s, n)
        if rr != 0:
            return None
        g[n] = q
    a = np.zeros(N_THETA + 1, dtype=np.int64)
    a[1:] = g
    return dict(sig3=sig3, Th_real=(Th0, Th1, Th2, Th1), a=a,
                ok_div=ok_div)


TH = build_thetas()
Th0, Th1, Th2, Th3 = TH["Th_real"]
sig3p = TH["sig3"]
heads = (int(Th0[1]), int(Th1[1]), int(Th2[1]), int(Th3[1]))
glue = bool(np.all((Th0 + Th1 + Th2 + Th3)[1:] == 240 * sig3p[1:]))
f8ok = bool(np.all((Th0 - Th2 + 8 * TH["a"])[1:N_THETA:2] == 0))
sig_agree = all(int(sig3p[n]) == sigma3[n] for n in range(1, NCAP + 1))
check("S5.1 v817 C1 re-gated: heads %s == (52,64,60,64); glue identity "
      "ALL n <= %d; Th1 == Th3; Th0 - Th2 = -8 f8 on ALL odd n; "
      "divisibility gates; sieve agreement" % (str(heads), N_THETA),
      TH["ok_div"] and heads == (52, 64, 60, 64) and glue and f8ok
      and bool(np.all(Th1 == Th3)) and sig_agree, kill="K7")

# the packet parity classes re-derived from the actual standard model
STD = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        STD.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        STD.append(v)
STD = sorted(STD)
j0 = j2 = spin = 0
j0_d5 = j0_a3 = 0
for x in STD:
    if all(t % 2 == 0 for t in x):
        a = [t // 2 for t in x]
        A, B = sum(a[:5]) % 2, sum(a[5:]) % 2
        if A == 0 and B == 0:
            j0 += 1
            sup = [i for i in range(8) if a[i]]
            if all(i < 5 for i in sup):
                j0_d5 += 1
            elif all(i >= 5 for i in sup):
                j0_a3 += 1
        elif A == 1 and B == 1:
            j2 += 1
    else:
        spin += 1
check("S5.2 m2 CHANNEL TYPED: mh[2] = (Th0-Th1+Th2-Th3)/(240 sigma_3) = "
      "the order-2 Z4 character of the register (v817 event_profile); "
      "packet level-1 classes from the ACTUAL 240 std roots: "
      "(j0, j2, spin) = (%d, %d, %d) == (52, 60, 128); 52 = %d + %d = "
      "|R(D5)| + |R(A3)| (seam reading); spinor halving Th1 = Th3 is "
      "numerical fiat (typed)" % (j0, j2, spin, j0_d5, j0_a3),
      len(STD) == 240 and (j0, j2, spin) == (52, 60, 128)
      and (j0_d5, j0_a3) == (40, 12), kill="K7")

num2c = Th0 - Th1 + Th2 - Th3
odd_idx = np.arange(1, N_THETA + 1, 2)
value_thm = bool(np.all(15 * num2c[odd_idx] == -240 * sig3p[odd_idx]))
primes = []
s = np.ones(N_THETA + 1, bool)
s[:2] = False
for i in range(2, int(N_THETA ** 0.5) + 1):
    if s[i]:
        s[i * i::i] = False
odd_primes = [int(p) for p in np.nonzero(s)[0] if p % 2 == 1]
check("S5.3 VALUE THEOREM: 15 (Th0-Th1+Th2-Th3)(n) = -240 sigma_3(n) "
      "for EVERY odd n <= %d => mh2(odd n) = -1/15 identically; covers "
      "all %d odd primes <= %d (v817's measured claim = the prime "
      "restriction)" % (N_THETA, len(odd_primes), N_THETA),
      value_thm and Fr(int(num2c[3]), int(240 * sig3p[3])) == Fr(-1, 15)
      and Fr(int(num2c[odd_primes[-1]]),
             int(240 * sig3p[odd_primes[-1]])) == Fr(-1, 15), kill="K8")

# ======================================================================
section("S6: the identification (cross-machinery)")
# ======================================================================
bridge = all(int(num2c[n]) == THAT[u][n]
             for u in THAT if u != U0 for n in range(1, NCAP + 1))
eisen = all(15 * int((Th0 + Th2)[n]) == 7 * (240 * sigma3[n])
            + 8 * THETA[0][n] for n in range(1, NCAP + 1))
check("S6.1 INTERTWINER IDENTITY: packet numerator == code Walsh "
      "transform, (Th0-Th1+Th2-Th3)(n) == Thetahat_u(n) for EVERY "
      "nonzero u and EVERY level n <= %d (odd AND even); Eisenstein "
      "normal form 15 Theta_D8 = 7 Theta_L + 8 Theta_0 across "
      "machineries; level 1 = the census law (-16)" % NCAP,
      bridge and eisen and int(num2c[1]) == -16 == RHAT[uref],
      kill="K9")
print("      packet numerator n=1..8: %s"
      % [int(num2c[n]) for n in range(1, 9)])
print("      code Walsh       n=1..8: %s"
      % [THAT[uref][n] for n in range(1, 9)])

check("S6.2 m2 = P-eigenvalue: mh2(odd) = -1/15 == spec(P)|_{u!=0} "
      "(character theorem: ramification S4.2 + equidistribution S4.3); "
      "two-odd-event contraction = two-step 1/225 (S3.3)",
      value_thm and law_odd and Fr(-1, 15) ** 2 == Fr(1, 225),
      kill="K9")

# transversality (typed report, no kill): code census on the SAME std model
def in_L_std(v):
    if all(t % 2 == 0 for t in v):
        return sum(t // 2 for t in v) % 2 == 0
    if all(t % 2 == 1 for t in v):
        return sum(v) % 4 == 0
    return False


def in_pi2L_std(v):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L_std([x // 2 for x in w])


reps_std, label_std = class_reps(STD, in_pi2L_std)
std_census = Counter(label_std.values())
std_ok = (len(reps_std) == 15
          and sorted(std_census.values()) == [16] * 15
          and not any(in_pi2L_std(x) for x in STD))
cont = {}
for x in STD:
    if all(t % 2 == 0 for t in x):
        a = [t // 2 for t in x]
        pj = "j0" if sum(a[:5]) % 2 == 0 else "j2"
    else:
        pj = "spin"
    cont[(label_std[x], pj)] = cont.get((label_std[x], pj), 0) + 1
code_ref = all(len({pj for (li, pj) in cont if li == l}) == 1
               for l in range(15))
packet_ref = (52 % 16 == 0 and 60 % 16 == 0)
row_profile = Counter(
    tuple(sorted((pj, n) for (li, pj), n in cont.items() if li == l))
    for l in range(15))
check("S6.3 TYPED TRANSVERSALITY (report, no kill): std-model code census "
      "15 x 16 zero-empty (model independence: %s); code refines packet: "
      "%s; packet refines code: %s (52,60 not multiples of 16) -- the "
      "identification is SPECTRAL, not a quotient-map intertwiner"
      % (std_ok, code_ref, packet_ref), std_ok, kill=None)
for prof, cnt in sorted(row_profile.items()):
    print("      %2d code classes with packet profile %s" % (cnt, prof))

# ======================================================================
section("C: must-break controls")
# ======================================================================
r1 = list(r_census)
r1[0] = 16
W1 = walsh(r1)
vals1 = sorted(W1[u] for u in W1 if u != U0)
check("C1 FIRES: occupied zero class r(0)=16: Walsh (%d; %s), normalized "
      "{1, 0^15} != law; two-step 0 != 1/225"
      % (W1[U0], sorted(set(vals1))),
      W1[U0] == 256 and vals1 == [0] * 15
      and Fr(0, 256) ** 2 != Fr(1, 225), kill="K4")

r2 = list(r_census)
r2[1] -= 1                      # one nonzero class at 15
W2 = walsh(r2)
mult2 = Counter(W2[u] for u in W2 if u != U0)
check("C2 FIRES: one class at 15: Walsh multiset on u != 0 = %s == "
      "{-17: 7, -15: 8}; NOT uniform, no value -16, ratios != -1/15"
      % dict(sorted(mult2.items())),
      dict(mult2) == {-17: 7, -15: 8}
      and all(Fr(v, W2[U0]) != Fr(-1, 15) for v in mult2), kill="K4")

check("C3 FIRES: wrong quotient dim F_2^3: 240 %% 7 = %d != 0 (uniform "
      "integer multiplicity impossible); uniform channel eigenvalue "
      "-1/7 != -1/15; two-step 1/49 != 1/225" % (240 % 7),
      240 % 7 != 0 and Fr(-1, 7) != Fr(-1, 15)
      and Fr(1, 49) != Fr(1, 225), kill="K4")

# ======================================================================
section("I: must-be-invariant")
# ======================================================================
ISOS = [("sigma", lambda v: tuple(v[PI_SIG[k]] for k in range(8)))]
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7)]
for pp in itertools.permutations(range(4)):
    if pp == (0, 1, 2, 3):
        continue
    perm = [0] * 8
    for k in range(4):
        perm[2 * k], perm[2 * k + 1] = PAIRS[pp[k]]
    if code_image(CSTAR, tuple(perm)) == CSTAR:
        ISOS.append(("pairperm%s" % (pp,),
                     (lambda pm: lambda v: tuple(v[pm[k]]
                                                 for k in range(8)))(perm)))
for k in range(4):
    swap = list(range(8))
    swap[2 * k], swap[2 * k + 1] = swap[2 * k + 1], swap[2 * k]
    if code_image(CSTAR, tuple(swap)) == CSTAR:
        def U_k(v, kk=k):
            out = list(v)
            out[2 * kk], out[2 * kk + 1] = -v[2 * kk + 1], v[2 * kk]
            return tuple(out)
        ISOS.append(("unit%d" % k, U_k))

j_triv = all(label[r] == label.get(J_vec(r), label[r])
             and cls16(J_vec(r))[0] == cls16(r)[0] for r in ROOTS)
neg_triv = all(cls16(tuple(-t for t in r))[0] == cls16(r)[0] for r in ROOTS)
ok_iso = True
nontriv = 0
maps_seen = set()
for name, f in ISOS:
    imgs = [f(r) for r in ROOTS]
    if sorted(imgs) != sorted(ROOTS):
        ok_iso = False
        continue
    gbar = {}
    well = True
    for r in ROOTS:
        a, b = cls16(r)[0], cls16(f(r))[0]
        if a in gbar and gbar[a] != b:
            well = False
        gbar[a] = b
    gbar[0] = cls16(f(ZERO))[0]
    lin = all(gbar[ADD[a][b]] == ADD[gbar[a]][gbar[b]]
              for a in gbar for b in gbar)
    censusg = [0] * 16
    for r in ROOTS:
        censusg[gbar[cls16(r)[0]]] += 1
    Wg = walsh(censusg)
    spec_ok = (sorted(Wg.values()) == sorted(RHAT.values()))
    if not (well and lin and censusg == r_census and spec_ok):
        ok_iso = False
    key = tuple(gbar[k] for k in range(16))
    if key != tuple(range(16)):
        nontriv += 1
    maps_seen.add(key)
check("I1 INVARIANT: %d explicit isometries of (L, J) (sigma, %d "
      "pair-perms, %d unit turns): each induces a well-defined F_2-"
      "linear map on V, preserves the census and the Walsh spectrum; "
      "%d nontrivial induced maps; J and -1 induce the identity on V "
      "(%s, %s)" % (len(ISOS), sum(1 for n, _ in ISOS if "pairperm" in n),
                    sum(1 for n, _ in ISOS if "unit" in n), nontriv,
                    j_triv, neg_triv),
      ok_iso and nontriv >= 1 and j_triv and neg_triv, kill="K5")

in_L2, in_pi2L2 = make_tests(CSTAR2)
ROOTS2 = build_roots(CSTAR2)
reps2, label2 = class_reps(ROOTS2, in_pi2L2)
ZERO2 = (0,) * 8
REPS16_2 = [ZERO2] + list(reps2)
cens2 = [0] * 16
ok2 = len(reps2) == 15
for r in ROOTS2:
    hits = [k for k in range(16)
            if in_pi2L2(tuple(a - b for a, b in zip(r, REPS16_2[k])))]
    if len(hits) != 1:
        ok2 = False
        break
    cens2[hits[0]] += 1
# Walsh spectrum of the second placement: uniform census => same multiset
w2_0 = sum(cens2)
w2_vals_ok = (cens2[0] == 0 and sorted(cens2[1:]) == [16] * 15)
check("I2 INVARIANT: the OTHER mu4/sigma-invariant placement C**: %d "
      "roots, census (zero; nonzero) = (%d; %s) => identical Walsh "
      "spectrum (240; -16 x15) by the same uniform law"
      % (len(ROOTS2), cens2[0], sorted(set(cens2[1:]))),
      len(ROOTS2) == 240 and ok2 and w2_vals_ok and w2_0 == 240,
      kill="K5")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
kills_a = [k for k in KILLS if k in ("K1", "K2", "K3", "K4", "K5")]
kills_b = [k for k in KILLS if k in ("K6", "K7", "K8", "K9")]
if kills_a:
    va = {"K1": "FOURIER-MISMATCH-CENSUS", "K2": "FOURIER-MISMATCH-LAW",
          "K3": "FOURIER-MISMATCH-CHANNEL", "K4": "CONTROL-DEAD",
          "K5": "INVARIANCE-BROKEN"}[kills_a[0]]
else:
    va = "SIMPLEX-FOURIER-EXACT"
if kills_b:
    vb = {"K6": "INTERTWINER-GAP-CODE", "K7": "INTERTWINER-GAP-PACKET",
          "K8": "INTERTWINER-GAP-VALUE",
          "K9": "INTERTWINER-GAP-BRIDGE"}[kills_b[0]]
else:
    vb = "INTERTWINER-IDENTIFIED"
VERDICT = "%s + %s" % (va, vb)
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION NOTES (report only -- no promotion, no edits):")
print("  * THE FOURIER LAW: the v833/v844 census 240 = 15 x 16 (zero class")
print("    empty) IS the spectral statement rhat = (240; -16 x15), i.e. the")
print("    uniform-nonzero channel P = (J-I)/15 with spec {1, (-1/15)^15}")
print("    and two-step contraction 1/225 -- one Walsh transform away from")
print("    the deployed census, no new input.")
print("  * THE FIVE-LINE THEOREM (measured here): (i) zero class empty at")
print("    ALL odd levels (ramification, one-line proof), (ii) nonzero")
print("    classes equidistribute at every level (Sp(4,2) footprint),")
print("    (iii) hence Thetahat_u(odd n) = -Theta_L(n)/15, (iv) the packet")
print("    numerator Th0-Th1+Th2-Th3 EQUALS Thetahat_u at every computed")
print("    level (15 Theta_D8 = 7 Theta_L + 8 Theta_0), (v) hence")
print("    mh2(odd) = -1/15 = spec(P)|_{u!=0}: v817's per-prime measurement")
print("    is a CHARACTER THEOREM of the code.")
print("  * HONEST TYPE: the identification is spectral (numerator q-series")
print("    equal); the packet 5|3-parity grading (52,60,128) and the code")
print("    grading (15 x 16) do NOT refine each other (S6.3 table).")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
'''

_SRC_WINDING = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""flavor_winding_quadratic_probe -- FLAVOR.WINDING.QUADRATIC.01 (the
I.5 mini-theorem of the 2026-08-08 morning analysis): the winding
deformation of the flavor residue matrix is controlled by ONE quadratic
q_wind(t) = t^2 - g_car t + |Z2|, exactly.

FROZEN CLAIMS (2026-08-08, frozen + SHA-hashed before first run):

 S1  THE RESIDUE MATRIX re-verified against the deployed invariants
     (v4_flavor_matrix.py + tfpt_2 winding boxes, read-only):
     R = [[1,3,0],[1,5,2],[2,5,3]]; det R = 8 = h(D5); tr R = 9;
     chi_R = t^3 - 9t^2 + 10t - 8; principal 2x2 minors (5,3,2)
     (deletion order), sorted {2,3,5}; SNF (1,1,8); ||R||_F^2 = 78;
     anchor column R e1 = a = (1,1,2); column sums (4,13,5);
     R^T a = (6,18,8); the cofactor seam normal n = (5,-9,6) = the
     common first adjugate row of R AND L, with n.1 = 2 = |Z2| and
     n^T R = (8,0,0) (tfpt_2 Winding Line box).
 S2  THE MINI-THEOREM (sympy, exact, symbols s and t): for
     R_s = R + s 1 e1^T:
       chi_{R_s}(t) = det(tI - R_s)
                    = t^3 - (9+s) t^2 + (10+5s) t - (8+2s)
     identically; equivalently  chi_{R_s} - chi_R = -s q_wind(t)  with
       q_wind(t) = t^2 - 5t + 2 = t^2 - g_car t + |Z2|
     (coefficient triple (1, -g_car, |Z2|), magnitudes (1,5,2)).
     SIGN CONVENTION typed: in the det(R_s - tI) convention (odd
     dimension) the deformation term is +s q_wind(t) -- the morning
     note's "+" form -- BOTH computed exactly.  The structural origin:
     the matrix determinant lemma gives q_wind(t) = e1^T adj(tI-R) 1
     (verified symbolically), so d(det R_s)/ds = q_wind(0) = 2 = |Z2|
     (the per-winding determinant increment of the deployed Winding
     Line box).  q_wind is irreducible over Q (disc = 17, nonsquare);
     the pencil has two s-INVARIANT base points: rem(chi_{R_s},
     q_wind, t) is s-free and equals rem(chi_R, q_wind, t).
     MEASURED COINCIDENCE (report): q_wind(6) = 8 = det R.
 S3  THE TRIPLE LOCK (three independent fixings, each solved exactly):
     tr R_s = 15 = dim A3      => s = 6;
     det R_s = 8 + 2s = 20 = 2 A_Lambda = |R(A4)|  => s = 6;
     Coxeter lift (R_s^T a)_1 = 6 + 4s = 30 = h(E8) => s = 6
     (the 4 is 1^T a = |mu4|); intersection = {6} = {|R+(A3)|}.
     At s = 6: chi_L = t^3 - 15t^2 + 40t - 20 with (15,40,20) =
     (dim A3, |R(D5)|, |R(A4)|); PrinMin2(R_s) = (5, 3(s+1), 2(s+1))
     symbolically, hence PrinMin2(L) = (5,21,14) = (g_car, 3x7, 2x7)
     (carrier minor 5 is s-INVARIANT); R_s^{-1} 1 = (1,1,-1)/(4+s);
     L = R + 6W rows = word lengths (7,3,0),(7,5,2),(8,5,3) (v4).
 S4  THE ROOT LOCUS (measure, don't narrate; exact Sturm/resultant):
     Delta(s) = disc_t(chi_{R_s}) computed exactly as a polynomial in
     s; FROZEN VALUES: Delta(0) = -7996 = -2^2 x 1999 (complex pair at
     s = 0, deployed) and Delta(6) = 39200 = 2^5 5^2 7^2 = 2 x 140^2
     > 0 (three real eigenvalues, deployed); s = 6 is NOT on the
     discriminant locus (Delta(6) != 0); the reality threshold s* lies
     in (2,3) (deployed ~2.83): exactly one real root of Delta in
     (2,3), and the real-eigenvalue count of chi_{R_s} jumps 1 -> 3
     between s = 2 and s = 3 (Sturm counts); at s = 6 the spectrum is
     3 real POSITIVE roots.  MEASURED AND TYPED (no frozen
     prediction): the full real-root census of Delta (count, factor
     decomposition over Q, rational isolations, minimal polynomial of
     s*), whether any collision point exists at s > 6, and the integer
     window s = -2..12 of Delta values with square / 2 x square
     typing (is 6 distinguished in the window? -- reported either
     way).
 C   CONTROLS (each must fire; exact):
     C1 direction 1 e2^T: the deformation quadratic is
        e2^T adj(tI-R) 1 = t^2 - t + 2 != q_wind (middle coefficient
        1 != g_car); the triple lock BREAKS: trace-fix {6}, det-fix
        {6} (constant term coincides -- typed honestly), Coxeter-fix
        EMPTY ((R_s^T a)_1 = 6 s-free) => intersection EMPTY.
     C2 direction 1 e3^T: quadratic t^2 + t - 2 = (t+2)(t-1) !=
        q_wind AND reducible (typed); det-fix {-6}, trace-fix {6},
        Coxeter-fix EMPTY => intersection EMPTY.
     C3 THE SIBLING ROW TRANSPORT e1 1^T (row instead of column):
        quadratic 1^T adj(tI-R) e1 = t^2 - 5t + 1: keeps the g_car
        coefficient, LOSES the |Z2| constant; fixings {6}, {12}, {24}
        pairwise disjoint (the measured doubling chain) =>
        intersection EMPTY.
     C4 THE SIBLING MINOR BRANCH (v4's control transported): the
        sibling triple {1,3,4} is unreachable on the whole winding
        line: 5 in PrinMin2(R_s) for EVERY s (the invariant carrier
        minor), 5 not in {1,3,4}; ratio 3:2 of the moving minors is
        s-invariant.

KILLS (any one fires => typed failure):
  K1 deployed residue invariants break        -> RESIDUE-MISMATCH
  K2 the quadratic law (S2) breaks            -> QUADRATIC-MISMATCH
  K3 the triple lock (S3) breaks              -> LOCK-BROKEN
  K4 the frozen locus values/counts break     -> LOCUS-BROKEN
  K5 a control does not fire                  -> CONTROL-DEAD

VERDICT (frozen enum): WINDING-QUADRATIC-EXACT / RESIDUE-MISMATCH /
QUADRATIC-MISMATCH / LOCK-BROKEN / LOCUS-BROKEN / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface;
no .md, no commits.  Exact sympy/integer arithmetic in every decision;
floats only in report-line prints of algebraic numbers; no RNG, no
fits.  NO physics claim.  Runtime cap: minutes.

Sources (read-only): verification/v4_flavor_matrix.py (R, sibling
branch), v10_projection_involution.py (6W forcing), v134_dual_anchor.py
(dual anchor), tfpt_2_standard_model.tex (winding-deformation keybox +
Winding Line box: chi_{R_s}, triple lock, disc values, s* ~ 2.83).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/flavor_winding_quadratic_probe.py
"""
import hashlib
import math
import time

import sympy as sp

T0 = time.time()
CHECKS = []
KILLS = []

G_CAR = 5
Z2 = 2
N_FAM = 3
MU4 = 4
H_E8 = 30
DIM_A3 = 15
R_D5 = 40
R_A4 = 20
A_LAMBDA = 10
RP_A3 = 6


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


print("=" * 74)
print("FLAVOR.WINDING.QUADRATIC.01 -- chi_{R_s} = chi_R - s q_wind,")
print("q_wind = t^2 - g_car t + |Z2|; triple lock s = 6; root locus")
print("=" * 74)
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())

t, s = sp.symbols("t s")
R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
ONES = sp.Matrix([1, 1, 1])
E1 = sp.Matrix([[1, 0, 0]])
A = sp.Matrix([1, 1, 2])
L = R + 6 * sp.Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])

# ======================================================================
section("S1: the residue matrix against the deployed invariants (v4)")
# ======================================================================
chiR = sp.expand(R.charpoly(t).as_expr())
minors = [sp.det(R.minor_submatrix(k, k)) for k in range(3)]
from sympy.matrices.normalforms import smith_normal_form
snf = sorted(abs(int(x)) for x in smith_normal_form(R, domain=sp.ZZ)
             .diagonal())
check("S1.1 det R = %d == 8 = h(D5); tr R = %d == 9; chi_R = %s"
      % (R.det(), R.trace(), chiR),
      R.det() == 8 and R.trace() == 9
      and chiR == t ** 3 - 9 * t ** 2 + 10 * t - 8, kill="K1")
check("S1.2 PrinMin2(R) = %s == (5,3,2); sorted {2,3,5}; SNF %s == "
      "(1,1,8); ||R||_F^2 = %d == 78"
      % (tuple(minors), tuple(snf), sum(x ** 2 for x in R)),
      tuple(minors) == (5, 3, 2) and snf == [1, 1, 8]
      and sum(x ** 2 for x in R) == 78, kill="K1")
n_vec = R.adjugate().row(0)
check("S1.3 anchor R e1 = %s == (1,1,2); column sums %s == (4,13,5); "
      "R^T a = %s == (6,18,8)"
      % (tuple(R.col(0)), tuple(ONES.T * R), tuple(R.T * A)),
      tuple(R.col(0)) == (1, 1, 2)
      and tuple(ONES.T * R) == (4, 13, 5)
      and tuple(R.T * A) == (6, 18, 8), kill="K1")
check("S1.4 cofactor seam normal: adj(R) row 1 = %s == (5,-9,6) == "
      "adj(L) row 1; n.1 = %s == 2 = |Z2|; n^T R = %s == (8,0,0)"
      % (tuple(n_vec), (n_vec * ONES)[0], tuple(n_vec * R)),
      tuple(n_vec) == (5, -9, 6)
      and tuple(L.adjugate().row(0)) == (5, -9, 6)
      and (n_vec * ONES)[0] == 2 and tuple(n_vec * R) == (8, 0, 0),
      kill="K1")

# ======================================================================
section("S2: the mini-theorem -- one quadratic controls the deformation")
# ======================================================================
Rs = R + s * ONES * E1
chiS = sp.expand(Rs.charpoly(t).as_expr())
target = sp.expand(t ** 3 - (9 + s) * t ** 2 + (10 + 5 * s) * t
                   - (8 + 2 * s))
q_wind = t ** 2 - G_CAR * t + Z2
check("S2.1 chi_{R_s}(t) = det(tI - R_s) = t^3 - (9+s)t^2 + (10+5s)t "
      "- (8+2s) EXACT (sympy expand)",
      sp.expand(chiS - target) == 0, kill="K2")
check("S2.2 chi_{R_s} - chi_R = -s q_wind with q_wind = t^2 - 5t + 2 = "
      "t^2 - g_car t + |Z2| (triple (1,-5,2))",
      sp.expand(chiS - chiR + s * q_wind) == 0, kill="K2")
det_conv = sp.expand(sp.det(Rs - t * sp.eye(3)))
check("S2.3 SIGN CONVENTION typed: det(R_s - tI) = (-t^3 + 9t^2 - 10t "
      "+ 8) + s (t^2 - 5t + 2) -- the '+' reading, computed",
      sp.expand(det_conv - (-chiR + s * q_wind)) == 0, kill="K2")
adjP = (t * sp.eye(3) - R).adjugate()
lemma = sp.expand((E1 * adjP * ONES)[0])
check("S2.4 matrix determinant lemma: e1^T adj(tI-R) 1 = %s == q_wind; "
      "d(det R_s)/ds = q_wind(0) = %d == |Z2| (per-winding det "
      "increment)" % (lemma, lemma.subs(t, 0)),
      sp.expand(lemma - q_wind) == 0 and lemma.subs(t, 0) == Z2,
      kill="K2")
rem_s = sp.rem(chiS, q_wind, t)
check("S2.5 q_wind irreducible over Q (disc = %s, nonsquare); the two "
      "base points are s-INVARIANT: rem(chi_{R_s}, q_wind, t) = %s is "
      "s-free and = rem(chi_R, q_wind, t)"
      % (sp.discriminant(q_wind, t), sp.expand(rem_s)),
      sp.discriminant(q_wind, t) == 17
      and not sp.expand(rem_s).has(s)
      and sp.expand(rem_s - sp.rem(chiR, q_wind, t)) == 0, kill="K2")
print("      MEASURED COINCIDENCE (report): q_wind(6) = %s (= det R = 8)"
      % q_wind.subs(t, 6))

# ======================================================================
section("S3: the triple lock s = 6 (three independent exact fixings)")
# ======================================================================
fix_tr = sp.solve(sp.Eq(Rs.trace(), DIM_A3), s)
fix_det = sp.solve(sp.Eq(Rs.det(), R_A4), s)
cox = sp.expand((Rs.T * A)[0])
fix_cox = sp.solve(sp.Eq(cox, H_E8), s)
check("S3.1 tr R_s = 15 => s = %s; det R_s = 8+2s = 20 => s = %s; "
      "(R_s^T a)_1 = %s = 30 => s = %s; intersection {6} = {|R+(A3)|}"
      % (fix_tr, fix_det, cox, fix_cox),
      fix_tr == [6] and fix_det == [6] and fix_cox == [6]
      and sp.expand(cox - (6 + 4 * s)) == 0
      and int((ONES.T * A)[0]) == MU4, kill="K3")
chiL = sp.expand(L.charpoly(t).as_expr())
minorsS = [sp.factor(sp.det(Rs.minor_submatrix(k, k))) for k in range(3)]
check("S3.2 at s = 6: chi_L = %s == t^3 - 15t^2 + 40t - 20 with "
      "(15,40,20) = (dim A3, |R(D5)|, |R(A4)|)" % chiL,
      chiL == t ** 3 - DIM_A3 * t ** 2 + R_D5 * t - R_A4
      and sp.expand(chiS.subs(s, 6) - chiL) == 0, kill="K3")
check("S3.3 PrinMin2(R_s) = %s == (5, 3(s+1), 2(s+1)); at s = 6: "
      "(5,21,14) = (g_car, 3x7, 2x7); carrier minor 5 s-INVARIANT"
      % (tuple(minorsS),),
      sp.expand(minorsS[0] - 5) == 0
      and sp.expand(minorsS[1] - 3 * (s + 1)) == 0
      and sp.expand(minorsS[2] - 2 * (s + 1)) == 0
      and [m.subs(s, 6) for m in minorsS] == [5, 21, 14], kill="K3")
rsinv1 = sp.simplify(Rs.inv() * ONES)
check("S3.4 R_s^{-1} 1 = (1,1,-1)/(4+s) (keybox); L rows = word "
      "lengths (7,3,0),(7,5,2),(8,5,3) (v4)",
      sp.simplify(rsinv1 - sp.Matrix([1, 1, -1]) / (4 + s))
      == sp.zeros(3, 1)
      and [tuple(L.row(i)) for i in range(3)]
      == [(7, 3, 0), (7, 5, 2), (8, 5, 3)], kill="K3")

# ======================================================================
section("S4: the root locus (exact Sturm / resultant measurements)")
# ======================================================================
Delta = sp.expand(sp.discriminant(chiS, t))
D0 = int(Delta.subs(s, 0))
D6 = int(Delta.subs(s, 6))
check("S4.1 Delta(s) = disc_t chi_{R_s} = %s; Delta(0) = %d == -7996 = "
      "-2^2 x 1999; Delta(6) = %d == 39200 = 2^5 5^2 7^2 = 2 x 140^2; "
      "s = 6 NOT on the locus" % (Delta, D0, D6),
      D0 == -7996 and D6 == 39200 and D6 == 2 * 140 ** 2 and D6 != 0,
      kill="K4")
Dpoly = sp.Poly(Delta, s)
n_real = Dpoly.count_roots()
n_23 = Dpoly.count_roots(2, 3)
n_after6 = Dpoly.count_roots(6, 10 ** 9)
rr = sp.real_roots(Dpoly)
facs = sp.factor_list(Delta, s)
check("S4.2 FROZEN: exactly one real root of Delta in (2,3) (the "
      "reality threshold s*, deployed ~2.83): count = %d; Sturm real-"
      "eigenvalue counts of chi jump 1 -> 3 between s = 2 and s = 3: "
      "(%d, %d)"
      % (n_23, sp.Poly(chiS.subs(s, 2), t).count_roots(),
         sp.Poly(chiS.subs(s, 3), t).count_roots()),
      n_23 == 1
      and sp.Poly(chiS.subs(s, 2), t).count_roots() == 1
      and sp.Poly(chiS.subs(s, 3), t).count_roots() == 3, kill="K4")
check("S4.3 at s = 6: chi_L has 3 real POSITIVE roots (count all = %d, "
      "count in (0, inf) = %d)"
      % (sp.Poly(chiL, t).count_roots(),
         sp.Poly(chiL, t).count_roots(0, 10 ** 9)),
      sp.Poly(chiL, t).count_roots() == 3
      and sp.Poly(chiL, t).count_roots(0, 10 ** 9) == 3, kill="K4")
print("      MEASURED (typed): Delta real-root census: %d real roots; "
      "collision points at s > 6: %d" % (n_real, n_after6))
print("      factor_list(Delta) = %s" % (facs,))
for r_ in rr:
    print("      real root s* ~ %s  (minpoly %s)"
          % (sp.N(r_, 8), sp.minimal_polynomial(r_, s)))
print("      integer window s = -2..12 (value, square?, 2 x square?):")
for si in range(-2, 13):
    v = int(Delta.subs(s, si))
    sq = v >= 0 and math.isqrt(v) ** 2 == v
    tsq = v >= 0 and v % 2 == 0 and math.isqrt(v // 2) ** 2 == v // 2
    print("        s=%3d  Delta=%10d  square=%s  2xsquare=%s"
          % (si, v, sq, tsq))
window_flags = [si for si in range(-2, 13)
                if (lambda v: v >= 0 and v % 2 == 0
                    and math.isqrt(v // 2) ** 2 == v // 2)
                (int(Delta.subs(s, si)))]
print("      2 x square hits in window: %s (measured, typed)"
      % window_flags)

# ======================================================================
section("C: controls (each must fire)")
# ======================================================================
E2 = sp.Matrix([[0, 1, 0]])
E3 = sp.Matrix([[0, 0, 1]])


def lockset(D):
    """solution sets of the three fixings for deformation matrix D."""
    Ms = R + s * D
    f1 = set(sp.solve(sp.Eq(Ms.trace(), DIM_A3), s))
    f2 = set(sp.solve(sp.Eq(Ms.det(), R_A4), s))
    f3 = set(sp.solve(sp.Eq(sp.expand((Ms.T * A)[0]), H_E8), s))
    return f1, f2, f3


q2 = sp.expand((E2 * adjP * ONES)[0])
l2 = lockset(ONES * E2)
check("C1 FIRES: direction 1 e2^T: quadratic %s != q_wind (triple "
      "(1,-1,2)); locks (tr, det, Cox) = (%s, %s, %s): intersection "
      "EMPTY (det coincides -- typed; Coxeter kills)"
      % (q2, sorted(l2[0]), sorted(l2[1]), sorted(l2[2])),
      sp.expand(q2 - q_wind) != 0
      and q2 == t ** 2 - t + 2
      and l2[0] == {6} and l2[1] == {6} and l2[2] == set()
      and (l2[0] & l2[1] & l2[2]) == set(), kill="K5")

q3 = sp.expand((E3 * adjP * ONES)[0])
l3 = lockset(ONES * E3)
check("C2 FIRES: direction 1 e3^T: quadratic %s = %s != q_wind, "
      "REDUCIBLE (typed); locks (%s, %s, %s): intersection EMPTY"
      % (q3, sp.factor(q3), sorted(l3[0]), sorted(l3[1]), sorted(l3[2])),
      sp.expand(q3 - q_wind) != 0 and q3 == t ** 2 + t - 2
      and sp.factor(q3) == (t + 2) * (t - 1)
      and l3[0] == {6} and l3[1] == {-6} and l3[2] == set()
      and (l3[0] & l3[1] & l3[2]) == set(), kill="K5")

q_row = sp.expand((ONES.T * adjP * E1.T)[0])
lrow = lockset(E1.T * ONES.T)
check("C3 FIRES: sibling ROW transport e1 1^T: quadratic %s: keeps "
      "-g_car t, LOSES |Z2| (constant 1); locks (%s, %s, %s) pairwise "
      "disjoint (measured doubling chain 6/12/24): intersection EMPTY"
      % (q_row, sorted(lrow[0]), sorted(lrow[1]), sorted(lrow[2])),
      q_row == t ** 2 - 5 * t + 1
      and lrow[0] == {6} and lrow[1] == {12} and lrow[2] == {24}
      and (lrow[0] & lrow[1] & lrow[2]) == set(), kill="K5")

sib = sp.solve([sp.Eq(minorsS[1], 3), sp.Eq(minorsS[2], 4)], s)
sib_hit = any(set(int(m.subs(s, sv)) for m in minorsS) == {1, 3, 4}
              for sv in range(-100, 101))
check("C4 FIRES: sibling minor branch {1,3,4} unreachable on the whole "
      "winding line: 5 in PrinMin2(R_s) for EVERY s (invariant carrier "
      "minor), moving minors locked at ratio 3:2 (integer scan "
      "s = -100..100 finds no hit: %s)" % sib_hit,
      minorsS[0] == 5 and not sib_hit
      and sp.simplify(minorsS[1] / minorsS[2] - sp.Rational(3, 2)) == 0,
      kill="K5")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if KILLS:
    VERDICT = {"K1": "RESIDUE-MISMATCH", "K2": "QUADRATIC-MISMATCH",
               "K3": "LOCK-BROKEN", "K4": "LOCUS-BROKEN",
               "K5": "CONTROL-DEAD"}[KILLS[0]]
else:
    VERDICT = "WINDING-QUADRATIC-EXACT"
print("%d/%d checks passed" % (n_pass, n_tot))
print("VERDICT: %s" % VERDICT)

print("\nCORPUS COMPRESSION NOTES (report only -- no promotion, no edits):")
print("  * THE I.5 MINI-THEOREM: the whole winding line chi_{R_s} =")
print("    chi_R - s (t^2 - g_car t + |Z2|) is one rank-one determinant")
print("    lemma; the tfpt_2 keybox coefficients (9+s, 10+5s, 8+2s), the")
print("    det increment 2 = |Z2| and the minor law (5, 3(s+1), 2(s+1))")
print("    are all readouts of the single quadratic e1^T adj(tI-R) 1.")
print("  * THE LOCK: trace/det/Coxeter each solve to s = 6 alone; every")
print("    sibling direction (1e2^T, 1e3^T, e1 1^T) breaks the lock AND")
print("    changes the quadratic -- (1, -5, 2) is direction-specific.")
print("  * THE LOCUS: s = 6 is NOT a collision point (Delta(6) = 39200 =")
print("    2 x 140^2 > 0); the reality threshold is the Delta-root in")
print("    (2,3) (~2.83, deployed); the integer-window 2xsquare census is")
print("    typed above (measured, not narrated).")
print("Runtime: %.1f s" % (time.time() - T0))
print("ALL CHECKS PASSED" if n_pass == n_tot
      else "CHECKS FAILED: %d" % (n_tot - n_pass))
raise SystemExit(0 if (n_pass == n_tot) else 1)
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
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
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
    ("simplex_fourier_probe", _SRC_FOURIER, 26, (),
     "SIMPLEX-FOURIER-EXACT + INTERTWINER-IDENTIFIED", 0),
    ("flavor_winding_quadratic_probe", _SRC_WINDING, 20, (),
     "WINDING-QUADRATIC-EXACT", 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v857 -- E8.SIMPLEX.FOURIER.01 + FLAVOR.WINDING.QUADRATIC.01")
    print("(the census as a Fourier law: mh2(odd) = -1/15 a character "
          "theorem to 16500;")
    print("the winding line as ONE quadratic q_wind = t^2 - g_car t + "
          "|Z2| with the")
    print("triple lock s = 6 and the reality threshold typed; "
          "NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v857: %d/%d probe pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print("Both parts are exact corpus compressions of deployed "
          "claims (v817/v833/v844,")
    print("tfpt_2 I.5 keyboxes) -- identifications typed honestly "
          "(spectral-only; the")
    print("gradings do not refine each other); no new physical claim; "
          "no marker moves.")
    print("[%s] v857 VERDICT GATE: SIMPLEX-FOURIER-EXACT + "
          "INTERTWINER-IDENTIFIED + WINDING-QUADRATIC-EXACT"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
