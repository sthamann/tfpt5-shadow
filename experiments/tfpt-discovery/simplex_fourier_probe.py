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
