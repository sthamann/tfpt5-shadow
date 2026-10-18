#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v844 -- MESSAGE.LADDER.01 + DOILY.PASCAL.RANK.01: the E8 addressing formula and the Doily-Pascal rank theorem -- two exact corpus compressions, ONE module from two probes (23/23 + 16/16 checks, verdicts MESSAGE-LADDER-EXACT and DOILY-PASCAL-RANK-EXACT; discovery probes binary_message_ladder_probe.py and doily_pascal_rank_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~2 s).  PART A, THE MESSAGE LADDER: M_n = 15 * Delta p_n = 15 * 2^n (anchor a = (1,1,2) with p_n = 2 + 2^n, v832 [E]; 15 = the nonzero classes of V = L/(1+i)L, v833 [E]) certified against the ACTUAL rebuilt objects with ONE NAMED STRUCTURE PER RUNG: M_0 = 15 = the address space (classes); M_1 = 30 = h(E8) derived HERE from the rebuilt root system, not cited (exactly 8 simple roots; connected simply-laced Cartan matrix, det 1, degree sequence [1,1,1,2,2,2,2,3] = the E8 diagram; every positive root with exact nonnegative INTEGER simple-root coordinates; the highest root UNIQUE at height 29 with marks {2,2,3,3,4,4,5,6}; h = 1 + 29 = 30 = |R|/rank); M_2 = 60 = the Gaussian root lines (mu4 orbits, all of size 4, exactly 4 per class); M_3 = 120 = |R+(E8)| (exact generic functional f(v) = Sum v_k 10^k) = the sign pairs; M_4 = 240 = |R(E8)| with the census 240 = 15 x 16 (zero class EMPTY); the CODA 248 = 15*16 + 8 = M_4 + rank checked against the actual census and the actual HNF rank; the structural doubling 60 -> 120 -> 240 (each line = exactly 2 sign pairs, each pair = 2 roots) and the halving 60 -> 30 = |mu4| vs rank typed.  The tfpt_1 budget lines |R| = 240 / dim E8 = 248 / h = 30 and v832 S3.1-S3.3 are ALL instances of this one formula.  Controls fire: the wrong anchor (1,2,2) gives (45,105,225,465) missing all four targets with recursion offset 1; the wrong multipliers 14 (the weight-4 codeword count) and 16 (the class size) miss all four targets and break the coda (232/264 != 248).  PART B, THE DOILY-PASCAL RANK THEOREM: the duad-syntheme incidence N of the Cremona-Richmond doily (15 duads x 15 synthemes, 3-regular in rows AND columns) and the symplectic point incidence B on PG(3,2) (B B^T = 4I + 3J entrywise on all 225 cells, charpoly (x-7)(x-2)^9(x+2)^5 exact, v774 S9 rebuilt) are ONE object: via the K6 duad model D(v) = {q Arf-1 : q(v) = 0} (exactly 16 quadratic refinements by brute force over 2^16, Arf census 6 + 10) the bijection point <-> duad carries N N^T onto B + 2I ENTRYWISE -- duad collinearity = symplectic orthogonality, and the spectrum shift 7/2/-2 -> 9/4/0 makes v774's (-2)-eigenspace v814's kernel.  THE RANK THEOREM (exact Fraction/sympy): charpoly(N N^T) = (x-9)(x-4)^9 x^5, so sing(N) = {3^1, 2^9, 0^5}: rank N = 10 = A_Lambda = C(g_car, 2) (the decuple sector), dim ker N = dim ker N^T = 5 = g_car (the five-slot carrier), multiplicity 9 = N_fam^2, top singular value 3 = N_fam, and the SIX ovoid indicators 3*1_{O_q} - 1 (q Arf-1) lie in ker N^T and SPAN it -- the P2 integers are the singular-value data of the Cremona-Richmond incidence.  THE RECOVERY VALUE: sing(N/3) = {1, 2/3 x9, 0 x5} exact, 2/3 = (N_fam - 1)/N_fam (the corpus recovery survival, v327); THE EXPONENTIATION IDENTITY: charpoly(((N/3)(N^T/3))^3) = (x-1)(x-64/729)^9 x^5 exact with 64/729 = (2/3)^6 = the deployed lambda_2 of {1, (2/3)^6, (1/3)^6} (v330/v486; the sixth power is the compiler clock, v814); TYPED GAP re-affirmed with NO upgrade: 1/729 is NOT a root of the six-step charpoly -- the deployed (1/3)^6 stays on the clock side (v814 SIXSTEP-CLOCK-ONLY [E], cited, consistent).  Controls fire: the circulant and the frozen-seed LCG 3-regular pairings (same row/col sums 3) give rank 13 != 10, kernel 2 != 5 and the wrong charpoly.  Exact integer/Fraction/sympy arithmetic; no floats, no fit; the only RNG is the frozen-seed LCG of control C2 (v775 C2 precedent).  No marker moves; the compression is a normal form, not a new claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes binary_message_ladder_probe.py (23/23,
verdict MESSAGE-LADDER-EXACT) and doily_pascal_rank_probe.py (16/16,
verdict DOILY-PASCAL-RANK-EXACT), both 2026-08-07, re-run identically
at promotion; this module runs both frozen protocols VERBATIM (the
probe docstrings are embedded byte-exact as _DOC_A/_DOC_B so the
printed FROZEN_SPEC SHA-256 values reproduce; runtime ~2 s).  The
original probe files live verbatim in experiments/tfpt-discovery/.

CORPUS SURFACES COMPRESSED (sources): the tfpt_1 budget lines
|R(E8)| = 240 / dim E8 = 248 / h(E8) = 30, the v832 anchor affine
block, the v833 census 15 x 16 and 60 Gaussian lines (rungs 0 and 2),
the v774 S9 symplectic incidence and ovoid eigenspace, the v814 A1
doily route with sv(N/3) = {1, 2/3 x9, 0 x5} and the six-step
(2/3)^6, the v330/v486 deployed transfer spectrum.  No marker moves.
"""
import hashlib
import itertools
import time
from fractions import Fraction as Fr

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

from tfpt_constants import N_fam, g_car

EXPECTED_A = "MESSAGE-LADDER-EXACT"
EXPECTED_B = "DOILY-PASCAL-RANK-EXACT"
N_CHECKS_A = 23
N_CHECKS_B = 16

_DOC_A = r"""binary_message_ladder_probe -- MESSAGE.LADDER.01: the E8 addressing
formula M_n = 15 * Delta p_n = 15 * 2^n, verified against the ACTUAL
objects, not just arithmetic.

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; work
package A of the v5.4 strategy, "formally close the finite normal form";
follow-up to v832 ANCHOR.AFFINE.01 and v833 GAUSSIAN.RAMLADDER.01):

The anchor a = (1,1,2) has power sums p_n = 2 + 2^n and binary shift
Delta p_n = p_n - 2 = 2^n (v832 [E]).  The MESSAGE LADDER is
      M_n = 15 * Delta p_n = 15 * 2^n,
where 15 = the number of nonzero classes of V = L/(1+i)L (the address
space, v833 R1.8 [E]).  Frozen rung claims, EACH verified against the
actual structure rebuilt from scratch (the Gaussian Construction-A E8 of
v833/v834, read-only machinery rebuilt inline):

 S1  LADDER ARITHMETIC (sympy, symbolic): p_n = 2 + 2^n, Delta p_n =
     2^n identically; M_0..M_4 = (15, 30, 60, 120, 240); the coda
     248 = 15*16 + 8 = M_4 + 8.

 S2  THE CARRIER OBJECT: rebuild the Gaussian E8 (Construction A over
     the unique mu4/sigma-invariant placement C*, 2 of 30); 240 roots,
     all norm 4; lattice rank 8 with [Z^8 : L] = 16 (HNF).

 S3  RUNG 4 (M_4 = 240 = |R(E8)|): the root census is EXACTLY 240 and
     distributes 240 = 15 x 16 over the 15 nonzero Gaussian classes
     (zero class empty) -- the 15 of the ladder IS the class count and
     16 = Delta p_4.  CODA: dim E8 = |R| + rank = 240 + 8 = 248 =
     15*16 + 8 against the actual census and the actual rank.

 S4  RUNG 3 (M_3 = 120 = |R+(E8)|): with the exact generic functional
     f(v) = Sum v_k 10^k (injective on {-2..2}^8 digits), the positive
     system has EXACTLY 120 roots and R = R+ u -R+.

 S5  RUNG 2 (M_2 = 60 = Gaussian root lines): the mu4-orbits
     {+-r, +-Jr} all have size 4; there are EXACTLY 60 lines; each of
     the 15 classes is a union of exactly 4 lines (v833 R1.9 rebuilt);
     each line contains exactly 2 of the 120 sign-pairs {+-r} (the
     structural doubling 60 -> 120 -> 240).

 S6  RUNG 1 (M_1 = 30 = h(E8), the Coxeter number FROM THE ROOT
     SYSTEM): the simple system of R+ (positive roots that are not a
     sum of two positive roots) has exactly 8 elements; its Cartan
     matrix <a_i, a_j>/2 is a valid connected simply-laced Cartan
     matrix with det = 1 and degree sequence [1,1,1,2,2,2,2,3] (the E8
     diagram); every positive root has nonnegative integer coordinates
     in the simple basis (exact Fraction solve); the height maximum is
     29, attained by a UNIQUE highest root with mark multiset
     {2,2,3,3,4,4,5,6}; h(E8) = 1 + 29 = 30, cross-checked against
     h = |R| / rank = 240/8 = 30.

 S7  INTERPRETATION ADDRESSES (typed, one structure per rung):
     M_0 = 15 = address space; M_1 = 30 = h(E8) = |R|/rank;
     M_2 = 60 = |R|/|mu4| (lines); M_3 = 120 = |R|/2 (sign pairs) =
     |R+|; M_4 = 240 = |R|; the rung-to-rung doubling is realized
     structurally for 60 -> 120 -> 240 (line = 2 sign-pairs, pair = 2
     roots) and the halving 60 -> 30 is |mu4| vs rank (rank 8 =
     2 * |mu4|).

 C   CONTROLS (must fire):
     C1 the wrong anchor a' = (1,2,2): Delta p'_n = 2^{n+1} - 1 gives
        M'_1..M'_4 = (45, 105, 225, 465) -- misses ALL FOUR targets;
        and the affine recursion p'_{n+1} = 2 p'_n - 2 fails (offset
        -1, v832 C2).
     C2 the wrong multiplier 14 (the weight-4 codeword count): 14*2^n
        = (28, 56, 112, 224) misses all four targets and 14*16 + 8 =
        232 != 248.
     C3 the wrong multiplier 16 (the class size): 16*2^n = (32, 64,
        128, 256) misses all four targets and 16*16 + 8 = 264 != 248.

KILLS (any one fires => MESSAGE-LADDER-MISMATCH-<type>):
  K1 ladder arithmetic fails                          -> ARITHMETIC
  K2 root census / class census / rank deviates       -> CENSUS
  K3 positive system != 120 or lines != 60            -> HALVING
  K4 the Coxeter computation from the root system     -> COXETER
     does not give 30 (simple system, highest root)
  K5 a control does not fire                          -> CONTROL-DEAD

VERDICT (frozen enum): MESSAGE-LADDER-EXACT /
MESSAGE-LADDER-MISMATCH-<type> / CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface.
Exact integer/Fraction/sympy arithmetic; no floats, no RNG, no fit.

Sources (read-only, machinery rebuilt inline): verification/
v832_anchor_flavor_checksum.py (the affine ladder), v833_gaussian_
ramification_ladder.py (C*, census, lines), v834_pg32_flag_completion.py
(rebuild precedent), note_e8_gaussian_code / v689 (census provenance).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/binary_message_ladder_probe.py
"""

_DOC_B = r"""doily_pascal_rank_probe -- DOILY.PASCAL.RANK.01: the Doily-Pascal
rank theorem -- the recovery value 2/3, the five-slot carrier and the
decuple sector are the singular values / kernel / rank of ONE incidence
map (the duad-syntheme incidence of the Cremona-Richmond doily).

FROZEN CLAIMS (2026-08-07, frozen + SHA-hashed before first run; work
package A of the v5.4 strategy; follow-up to v774 ARF.SPINORCOMPILER.01
S9, v814 K5.SIXSTEP.TRANSPORT.01 A1, v811/v815 doily machinery):

 S1  THE DOILY INCIDENCE: N = the 15 duads x 15 synthemes incidence of
     the 6-element set (duad in syntheme), built explicitly; N is
     3-regular in rows AND columns (each duad in 3 synthemes, each
     syntheme = 3 duads) -- the classical Cremona-Richmond / GQ(2,2)
     point-line structure.

 S2  THE SYMPLECTIC SIDE: on the 15 points of PG(3,2) = nonzero
     vectors of V = F2^4 with the corpus form hbar (Gram J - I in the
     family/anchor basis, v752/v774), B[x][y] = 1 iff hbar(x,y) = 0;
     row sums 7; B B^T = 4I + 3J ENTRYWISE; charpoly(B) =
     (x-7)(x-2)^9(x+2)^5 (v774 S9.2 rebuilt).

 S3  THE BRIDGE (the rank theorem's two sides are ONE object): via the
     K6 duad model D(v) = {q Arf-1 : q(v) = 0} (16 quadratic
     refinements by brute force over 2^16, Arf census 6 + 10, v774
     S2/S3/S8 rebuilt), the bijection point <-> duad carries
     N N^T onto B + 2I ENTRYWISE (all 225 cells) -- collinearity of
     duads = symplectic orthogonality of points.

 S4  THE RANK THEOREM (exact Fraction arithmetic):
     charpoly(N N^T) = (x-9)(x-4)^9 x^5, i.e. sing(N) = {3^1, 2^9,
     0^5}; rank N = 10 = A_Lambda = C(g_car, 2) (the decuple sector);
     dim ker N = dim ker N^T = 5 = g_car (the five-slot carrier);
     multiplicity 9 = N_fam^2; top value 3 = N_fam; the SIX ovoid
     indicator vectors 3*1_{O_q} - 1 (q Arf-1), transported to duad
     indexing, all lie in ker N^T and SPAN it (rank exactly 5).

 S5  THE RECOVERY VALUE: sing(N/3) = {1, 2/3 x9, 0 x5} exact
     (charpoly of (N/3)(N/3)^T = (x-1)(x-4/9)^9 x^5); 2/3 =
     (N_fam - 1)/N_fam = the corpus recovery survival (v327).

 S6  THE COMPILER CLOCK CROSS-CHECK: the deployed recovery spectrum is
     {1, (2/3)^6, (1/3)^6} (v330/v486; the sixth power is the compiler
     clock, v814 SIXSTEP-CLOCK-ONLY).  Verified here EXACTLY: the
     three PSD double-steps ((N/3)(N^T/3))^3 have charpoly
     (x-1)(x-64/729)^9 x^5 with 64/729 = (2/3)^6 = the deployed
     lambda_2 (the exponentiation identity); TYPED GAP re-affirmed:
     the doily channel has NO (1/3)^6 mode (1/729 is NOT an eigenvalue
     of the six-step alternation) -- the (1/3)^6 line of the deployed
     spectrum lives on the clock side (v814 [E], cited, consistent).

 C   CONTROLS (must fire; wrong pairing with the SAME row sums):
     C1 the circulant 3-regular bipartite pairing N'[i][j] = 1 iff
        (j - i) mod 15 in {0,1,2}: row/col sums 3, but rank != 10 and
        dim ker != 5 and charpoly(N'N'^T) != the doily target.
     C2 the frozen-seed LCG pairing (sum of 3 pairwise-disjoint random
        permutation matrices; row/col sums 3): (rank, charpoly) !=
        (10, doily target).

KILLS (any one fires => typed failure):
  K1 doily census / regularity breaks                -> DOILY-BROKEN
  K2 B B^T != 4I+3J or spectrum 7/2^9/(-2)^5 breaks  -> GRAM-BROKEN
  K3 N N^T != B + 2I in any cell                     -> BRIDGE-BROKEN
  K4 rank != 10 or kernel != 5 or spectrum deviates  -> RANK-MISMATCH
  K5 the (2/3)^6 exponentiation identity fails, or a
     spurious (1/3)^6 mode appears                   -> CLOCK-MISMATCH
  K6 a control does not fire                         -> CONTROL-DEAD

VERDICT (frozen enum): DOILY-PASCAL-RANK-EXACT / DOILY-BROKEN /
GRAM-BROKEN / BRIDGE-BROKEN / RANK-MISMATCH / CLOCK-MISMATCH /
CONTROL-DEAD.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing but
stdout; no verification/, paper, ledger, changelog or website surface.
Exact integer/Fraction/sympy arithmetic; the only RNG is the frozen-
seed LCG of control C2 (v775 C2 precedent); no floats, no fit.

Sources (read-only): verification/v774_arf_spinor_compiler.py (S2/S3/
S8/S9 machinery rebuilt inline), v814_k5_sixstep_transport.py (A1 doily
route), v811/v815 (doily Kraus corpus), v330/v486 (deployed transfer
spectrum), v327 (2/3 recovery survival), tfpt_constants (g_car, N_fam).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/doily_pascal_rank_probe.py
"""


def part_a():
    T0 = time.time()
    CHECKS = []
    KILLS = []


    def check(name, ok, detail="", kill=None):
        CHECKS.append((name, bool(ok)))
        if kill and not ok:
            KILLS.append(kill)
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                               ("  -- " + detail) if detail else ""), flush=True)
        return bool(ok)


    def section(title):
        print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


    print("MESSAGE.LADDER.01 -- the E8 addressing formula M_n = 15 * 2^n")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(_DOC_A.encode("utf-8")).hexdigest())

    # ----------------------------------------------------------------------
    section("S1: ladder arithmetic (sympy, symbolic)")
    # ----------------------------------------------------------------------
    n = sp.symbols("n")
    pn = sp.Integer(2) + 2 ** n
    dpn = pn - 2
    a = (1, 1, 2)
    p = lambda k: sum(sp.Integer(ai) ** k for ai in a)
    check("S1.1 p_n(1,1,2) = 2 + 2^n (p_0..p_5 agree), Delta p_n = 2^n "
          "identically",
          all(p(k) == pn.subs(n, k) for k in range(6))
          and sp.simplify(dpn - 2 ** n) == 0, kill="K1")
    M = {k: 15 * 2 ** k for k in range(5)}
    check("S1.2 M_n = 15 * Delta p_n: (M_0..M_4) = %s == (15, 30, 60, 120, "
          "240)" % ([M[k] for k in range(5)],),
          [M[k] for k in range(5)] == [15, 30, 60, 120, 240], kill="K1")
    check("S1.3 CODA: 248 = 15*16 + 8 = M_4 + 8 (arithmetic layer)",
          15 * 16 + 8 == 248 == M[4] + 8, kill="K1")

    # ----------------------------------------------------------------------
    section("S2: rebuild the Gaussian E8 (Construction A over C*, v833)")
    # ----------------------------------------------------------------------
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


    placements = set()
    for perm in itertools.permutations(range(8)):
        placements.add(code_image(C_NAIVE, perm))
    both = [c for c in placements
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = (1, 0, 1, 0, 1, 0, 1, 0)
    check("S2.1 placement census: %d placements, %d invariant under both "
          "pi_J and pi_sigma (v833 R1.3)" % (len(placements), len(both)),
          len(placements) == 30 and len(both) == 2, kill="K2")
    CSTAR = next(c for c in both if W0246 in c)

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
    check("S2.2 root census: %d roots, all distinct, all norm 4, all in L"
          % len(ROOTS),
          len(ROOTS) == 240 and len(set(ROOTS)) == 240
          and all(sum(x * x for x in r) == 4 for r in ROOTS)
          and all(tuple(abs(x) % 2 for x in r) in CSTAR for r in ROOTS),
          kill="K2")

    gens = sp.Matrix([list(c) for c in sorted(CSTAR)]
                     + [[2 * (r == k) for k in range(8)]
                        for r in range(8)]).T
    Bc = hermite_normal_form(gens)
    detB = abs(Bc.det())
    check("S2.3 lattice rank 8, HNF |det| = %d == 16 = [Z^8 : L] "
          "(v833 R1.10)" % detB,
          Bc.shape == (8, 8) and Bc.rank() == 8 and detB == 16, kill="K2")

    # ----------------------------------------------------------------------
    section("S3: RUNG 4 -- M_4 = 240 = |R(E8)| and the 15 x 16 census")
    # ----------------------------------------------------------------------


    def J_vec(v):
        out = [0] * 8
        for k in range(4):
            out[2 * k] = -v[2 * k + 1]
            out[2 * k + 1] = v[2 * k]
        return tuple(out)


    def in_L(v):
        return tuple(x % 2 for x in v) in CSTAR


    def in_pi2L(v):
        # x in (1+i)L  <=>  (1-J)x/2 in L
        w = [0] * 8
        for k in range(4):
            w[2 * k] = v[2 * k] + v[2 * k + 1]
            w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
        if any(x % 2 for x in w):
            return False
        return in_L([x // 2 for x in w])


    labels = {}
    reps = []
    for r in ROOTS:
        for li, rep in enumerate(reps):
            if in_pi2L(tuple(x - y for x, y in zip(r, rep))):
                labels[r] = li
                break
        else:
            labels[r] = len(reps)
            reps.append(r)
    counts = sorted(sum(1 for r in ROOTS if labels[r] == li)
                    for li in range(len(reps)))
    check("S3.1 M_4 = 240 = |R(E8)|: the census distributes 240 = 15 x 16 "
          "over %d nonzero classes (sizes %s); zero class empty (%d/240 in "
          "(1+i)L) -- 15 = the ladder base, 16 = Delta p_4"
          % (len(reps), sorted(set(counts)),
             sum(1 for r in ROOTS if in_pi2L(r))),
          len(ROOTS) == M[4] and len(reps) == 15 and counts == [16] * 15
          and not any(in_pi2L(r) for r in ROOTS), kill="K2")
    check("S3.2 CODA against the actual objects: dim E8 = |R| + rank = "
          "%d + %d = %d == 248 == 15*16 + 8" % (len(ROOTS), 8, len(ROOTS) + 8),
          len(ROOTS) + Bc.rank() == 248 == 15 * 16 + 8, kill="K2")

    # ----------------------------------------------------------------------
    section("S4: RUNG 3 -- M_3 = 120 = |R+(E8)| (exact generic functional)")
    # ----------------------------------------------------------------------
    WTS = [10 ** k for k in range(8)]


    def fgen(r):
        return sum(r[k] * WTS[k] for k in range(8))


    check("S4.1 f(v) = Sum v_k 10^k is injective-signed on the roots: "
          "f(r) != 0 for all 240 (digits |v_k| <= 2 < 10)",
          all(fgen(r) != 0 for r in ROOTS), kill="K3")
    POS = [r for r in ROOTS if fgen(r) > 0]
    POSSET = set(POS)
    check("S4.2 M_3 = 120 = |R+|: positive system has %d roots and "
          "R = R+ u -R+" % len(POS),
          len(POS) == M[3]
          and all((r in POSSET) != (tuple(-x for x in r) in POSSET)
                  for r in ROOTS), kill="K3")

    # ----------------------------------------------------------------------
    section("S5: RUNG 2 -- M_2 = 60 Gaussian root lines (mu4 orbits)")
    # ----------------------------------------------------------------------
    lines = set()
    for r in ROOTS:
        lines.add(frozenset([r, J_vec(r), tuple(-x for x in r),
                             tuple(-x for x in J_vec(r))]))
    check("S5.1 M_2 = 60 = Gaussian lines: %d mu4-orbits, all of size 4 "
          "(J free on roots, v833 R1.9)" % len(lines),
          len(lines) == M[2] and all(len(ln) == 4 for ln in lines),
          kill="K3")
    check("S5.2 each of the 15 classes is a union of exactly 4 lines "
          "(60 = 15 x 4)",
          all(sum(1 for ln in lines if labels[next(iter(ln))] == li) == 4
              for li in range(15)), kill="K3")
    pairs = {frozenset([r, tuple(-x for x in r)]) for r in ROOTS}
    check("S5.3 STRUCTURAL DOUBLING 60 -> 120 -> 240: %d sign-pairs {+-r}; "
          "each line contains exactly 2 pairs; each pair exactly 2 roots"
          % len(pairs),
          len(pairs) == 120
          and all(sum(1 for pr in pairs if pr <= ln) == 2 for ln in lines),
          kill="K3")

    # ----------------------------------------------------------------------
    section("S6: RUNG 1 -- M_1 = 30 = h(E8) FROM the root system")
    # ----------------------------------------------------------------------
    SIMPLE = [r for r in POS
              if not any(tuple(x - y for x, y in zip(r, s)) in POSSET
                         for s in POSSET if s != r)]
    check("S6.1 simple system: exactly %d simple roots (positive roots "
          "that are not a sum of two positive roots)" % len(SIMPLE),
          len(SIMPLE) == 8, kill="K4")


    def ip(x, y):
        return sum(a * b for a, b in zip(x, y))


    CART = [[ip(SIMPLE[i], SIMPLE[j]) // 2 for j in range(8)]
            for i in range(8)]
    deg = sorted(sum(1 for j in range(8) if i != j and CART[i][j] != 0)
                 for i in range(8))
    adj_ok = all(CART[i][i] == 2 and all(CART[i][j] in (0, -1)
                                         for j in range(8) if j != i)
                 for i in range(8))
    # connectivity
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v2 in range(8):
            if v2 not in seen and CART[u][v2] == -1:
                seen.add(v2)
                stack.append(v2)
    detC = sp.Matrix(CART).det()
    check("S6.2 Cartan matrix <a_i,a_j>/2: diag 2, offdiag in {0,-1}, "
          "connected, det = %s == 1, degree sequence %s == [1,1,1,2,2,2,2,3]"
          " -- the E8 diagram" % (detC, deg),
          adj_ok and len(seen) == 8 and detC == 1
          and deg == [1, 1, 1, 2, 2, 2, 2, 3], kill="K4")

    S8 = sp.Matrix([[SIMPLE[j][i] for j in range(8)] for i in range(8)])
    S8inv = S8.inv()
    heights = {}
    all_int = True
    for r in POS:
        co = S8inv * sp.Matrix(r)
        if not all(x.is_Integer and x >= 0 for x in co):
            all_int = False
        heights[r] = sum(co)
    hmax = max(heights.values())
    top = [r for r in POS if heights[r] == hmax]
    marks = sorted((S8inv * sp.Matrix(top[0])) if top else [])
    check("S6.3 every positive root has nonnegative INTEGER simple-root "
          "coordinates (exact); height max = %s, attained by %d root(s)"
          % (hmax, len(top)),
          all_int and hmax == 29 and len(top) == 1, kill="K4")
    check("S6.4 highest-root marks (sorted) = %s == [2,2,3,3,4,4,5,6] "
          "(sum 29)" % (marks,),
          marks == [2, 2, 3, 3, 4, 4, 5, 6] and sum(marks) == 29, kill="K4")
    h_cox = 1 + hmax
    check("S6.5 M_1 = 30 = h(E8): 1 + ht(theta) = %d == 30 == |R|/rank = "
          "%d/8 (both readings of the Coxeter number agree)"
          % (h_cox, len(ROOTS)),
          h_cox == M[1] == len(ROOTS) // 8, kill="K4")

    # ----------------------------------------------------------------------
    section("S7: interpretation addresses (typed, one structure per rung)")
    # ----------------------------------------------------------------------
    check("S7.1 RUNG TABLE: M_0 = 15 = address space (classes); M_1 = 30 = "
          "h(E8) = |R|/rank; M_2 = 60 = |R|/|mu4| (lines); M_3 = 120 = "
          "|R|/2 (sign pairs) = |R+|; M_4 = 240 = |R|",
          len(reps) == M[0] and h_cox == M[1] == len(ROOTS) // 8
          and len(lines) == M[2] == len(ROOTS) // 4
          and len(pairs) == M[3] == len(ROOTS) // 2 == len(POS)
          and len(ROOTS) == M[4], kill="K2")
    check("S7.2 the halving 60 -> 30 is |mu4| vs rank: lines = |R|/4, "
          "h = |R|/8, rank 8 = 2 * |mu4| = 2 * 4",
          len(lines) == len(ROOTS) // 4 and h_cox == len(ROOTS) // 8
          and 8 == 2 * 4, kill="K2")

    # ----------------------------------------------------------------------
    section("C: controls (must fire)")
    # ----------------------------------------------------------------------
    TARGETS = {30, 60, 120, 240}
    ap = (1, 2, 2)
    pp = lambda k: sum(ai ** k for ai in ap)
    Mw = [15 * (pp(k) - 2) for k in range(1, 5)]
    viol = [pp(k + 1) - (2 * pp(k) - 2) for k in range(4)]
    check("C1 FIRES: wrong anchor (1,2,2): M'_1..M'_4 = %s -- misses all "
          "four targets; recursion offset %s != 0" % (Mw, viol),
          not (set(Mw) & TARGETS) and all(v == 1 for v in viol), kill="K5")
    M14 = [14 * 2 ** k for k in range(1, 5)]
    check("C2 FIRES: wrong multiplier 14 (the weight-4 codeword count): "
          "%s misses all four targets; 14*16 + 8 = %d != 248"
          % (M14, 14 * 16 + 8),
          not (set(M14) & TARGETS) and 14 * 16 + 8 != 248
          and sum(1 for c in CSTAR if sum(c) == 4) == 14, kill="K5")
    M16 = [16 * 2 ** k for k in range(1, 5)]
    check("C3 FIRES: wrong multiplier 16 (the class size): %s misses all "
          "four targets; 16*16 + 8 = %d != 248" % (M16, 16 * 16 + 8),
          not (set(M16) & TARGETS) and 16 * 16 + 8 != 248, kill="K5")

    # ----------------------------------------------------------------------
    section("VERDICT")
    # ----------------------------------------------------------------------
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = "MESSAGE-LADDER-MISMATCH-%s" % KILLS[0]
    else:
        VERDICT = "MESSAGE-LADDER-EXACT"
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)

    print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
    print("  * tfpt_1 budget lines |R(E8)| = 240 / dim E8 = 248 / h = 30 and")
    print("    v832 S3.1-S3.3 (240 = p1p2p3, 30 = p2p3/2, 248 = 240 + q3):")
    print("    ALL are instances of ONE formula M_n = 15 * Delta p_n, with")
    print("    each rung realized by a NAMED structure of the SAME object")
    print("    (address space / Coxeter number / Gaussian lines / positive")
    print("    system / root census).")
    print("  * v833 R1.8/R1.9 (census 15 x 16, 60 lines): the 15 and the 60")
    print("    are rungs 0 and 2 of the ladder.")
    print("  * NEW here: h(E8) = 30 certified from the rebuilt root system")
    print("    (simple system -> highest root height 29 -> h = 30), not")
    print("    cited; the doubling chain 60 -> 120 -> 240 typed structurally.")
    print("Runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return n_pass, n_tot, VERDICT


def part_b():
    T0 = time.time()
    CHECKS = []
    KILLS = []


    def check(name, ok, detail="", kill=None):
        CHECKS.append((name, bool(ok)))
        if kill and not ok:
            KILLS.append(kill)
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                               ("  -- " + detail) if detail else ""), flush=True)
        return bool(ok)


    def section(title):
        print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0), flush=True)


    print("DOILY.PASCAL.RANK.01 -- rank/kernel/singular values of the "
          "duad-syntheme incidence")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(_DOC_B.encode("utf-8")).hexdigest())

    A_LAMBDA = g_car * (g_car - 1) // 2      # 10 = C(5,2), the decuple sector

    # ----------------------------------------------------------------------
    section("S1: the Cremona-Richmond doily incidence N (duads x synthemes)")
    # ----------------------------------------------------------------------
    DUADS = [frozenset(p) for p in itertools.combinations(range(6), 2)]
    SYNTHEMES = []
    for m in itertools.permutations(range(6)):
        s = frozenset(frozenset({m[2 * k], m[2 * k + 1]}) for k in range(3))
        if s not in SYNTHEMES:
            SYNTHEMES.append(s)
    N = [[1 if DUADS[i] in SYNTHEMES[j] else 0 for j in range(len(SYNTHEMES))]
         for i in range(15)]
    rows = [sum(N[i]) for i in range(15)]
    cols = [sum(N[i][j] for i in range(15)) for j in range(len(SYNTHEMES))]
    check("S1.1 15 duads, %d synthemes (perfect matchings of the 6-set); "
          "N is 3-regular in rows and columns" % len(SYNTHEMES),
          len(SYNTHEMES) == 15 and rows == [3] * 15 and cols == [3] * 15,
          kill="K1")

    # ----------------------------------------------------------------------
    section("S2: the symplectic point incidence B on PG(3,2) (v774 S9)")
    # ----------------------------------------------------------------------
    W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
    WIDX = {w: i for i, w in enumerate(W16)}
    GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]  # J - I


    def hb(v, w):
        return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
                   for j in range(4)) % 2


    NZ15 = sorted(w for w in W16 if any(w))
    B = [[1 if hb(x, y) == 0 else 0 for y in NZ15] for x in NZ15]
    BBt = [[sum(B[i][k] * B[j][k] for k in range(15)) for j in range(15)]
           for i in range(15)]
    ok_bbt = all(BBt[i][j] == (7 if i == j else 3)
                 for i in range(15) for j in range(15))
    x = sp.symbols("x")
    cpB = sp.Matrix(B).charpoly(x).as_expr()
    cpB_t = sp.expand((x - 7) * (x - 2) ** 9 * (x + 2) ** 5)
    check("S2.1 hbar alternating + nondegenerate; B row sums all 7; "
          "B B^T == 4I + 3J ENTRYWISE (225 cells)",
          all(hb(v, v) == 0 for v in W16)
          and all(any(hb(v, w) for w in NZ15) for v in NZ15)
          and all(sum(r) == 7 for r in B) and ok_bbt, kill="K2")
    check("S2.2 charpoly(B) = (x-7)(x-2)^9(x+2)^5 exact (spectrum "
          "7^1 2^9 (-2)^5, v774 S9.2)",
          sp.expand(cpB - cpB_t) == 0, kill="K2")

    # ----------------------------------------------------------------------
    section("S3: the bridge -- N N^T = B + 2I via the K6 duad model")
    # ----------------------------------------------------------------------
    refs = []
    for mask in range(1 << 16):
        q = [(mask >> i) & 1 for i in range(16)]
        ok = True
        for i in range(16):
            qi = q[i]
            vi = W16[i]
            for j in range(16):
                vj = W16[j]
                vs = tuple((a + b) % 2 for a, b in zip(vi, vj))
                if q[WIDX[vs]] ^ qi ^ q[j] != hb(vi, vj):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            refs.append(tuple(q))
    arf1 = sorted(q for q in refs
                  if sum(1 for i in range(16) if q[i] == 0) == 6)
    check("S3.1 exactly 16 quadratic refinements of hbar (brute force over "
          "2^16); Arf census 6 + 10 (v774 S2/S3)",
          len(refs) == 16 and len(arf1) == 6
          and sum(1 for q in refs
                  if sum(1 for i in range(16) if q[i] == 0) == 10) == 10,
          kill="K3")

    duad_of = {}
    ok_two = True
    for v in NZ15:
        dv = frozenset(k for k, q in enumerate(arf1) if q[WIDX[v]] == 0)
        if len(dv) != 2:
            ok_two = False
        duad_of[v] = dv
    check("S3.2 K6 duad model: D(v) = {q Arf-1 : q(v) = 0} is a 2-set for "
          "every v != 0 and v <-> D(v) is a bijection onto the 15 duads "
          "(v774 S8)",
          ok_two and len(set(duad_of.values())) == 15, kill="K3")

    didx = {frozenset(p): i for i, p in enumerate(DUADS)}
    NNt = [[sum(N[i][k] * N[j][k] for k in range(15)) for j in range(15)]
           for i in range(15)]
    ok_bridge = True
    for vi, v in enumerate(NZ15):
        for wi, w in enumerate(NZ15):
            lhs = NNt[didx[duad_of[v]]][didx[duad_of[w]]]
            rhs = B[vi][wi] + (2 if vi == wi else 0)
            if lhs != rhs:
                ok_bridge = False
    check("S3.3 THE BRIDGE: N N^T == B + 2I ENTRYWISE under the duad "
          "bijection (all 225 cells) -- duad collinearity = symplectic "
          "orthogonality", ok_bridge, kill="K3")

    # ----------------------------------------------------------------------
    section("S4: the rank theorem -- rank 10 = A_Lambda, kernel 5 = g_car")
    # ----------------------------------------------------------------------
    cpNNt = sp.Matrix(NNt).charpoly(x).as_expr()
    cpNNt_t = sp.expand((x - 9) * (x - 4) ** 9 * x ** 5)
    check("S4.1 charpoly(N N^T) = (x-9)(x-4)^9 x^5 exact -- sing(N) = "
          "{3^1, 2^9, 0^5}", sp.expand(cpNNt - cpNNt_t) == 0, kill="K4")


    def frac_rank(rows_):
        M = [[Fr(e) for e in r] for r in rows_]
        rank = 0
        nrows, ncols = len(M), len(M[0])
        for col in range(ncols):
            piv = next((r for r in range(rank, nrows) if M[r][col] != 0),
                       None)
            if piv is None:
                continue
            M[rank], M[piv] = M[piv], M[rank]
            inv = 1 / M[rank][col]
            M[rank] = [e * inv for e in M[rank]]
            for r in range(nrows):
                if r != rank and M[r][col] != 0:
                    f = M[r][col]
                    M[r] = [e - f * g for e, g in zip(M[r], M[rank])]
            rank += 1
            if rank == nrows:
                break
        return rank


    rkN = frac_rank(N)
    rkNT = frac_rank([[N[i][j] for i in range(15)] for j in range(15)])
    check("S4.2 rank N = %d == 10 == A_Lambda = C(g_car,2) (the decuple "
          "sector); dim ker N = dim ker N^T = %d == 5 == g_car (the "
          "five-slot carrier)" % (rkN, 15 - rkN),
          rkN == rkNT == 10 == A_LAMBDA and 15 - rkN == 5 == g_car,
          kill="K4")
    check("S4.3 multiplicity 9 = N_fam^2 = %d; top singular value 3 = "
          "N_fam (row regularity)" % (N_fam ** 2),
          N_fam ** 2 == 9 and N_fam == 3 and rows == [N_fam] * 15,
          kill="K4")

    ovoid_rows = []
    ok_ker = True
    for q in arf1:
        u = [0] * 15
        for v in NZ15:
            u[didx[duad_of[v]]] = 3 * (1 if q[WIDX[v]] == 0 else 0) - 1
        ovoid_rows.append(u)
        Ntu = [sum(N[i][j] * u[i] for i in range(15)) for j in range(15)]
        if any(e != 0 for e in Ntu):
            ok_ker = False
    rk_ov = frac_rank(ovoid_rows)
    check("S4.4 the SIX ovoid indicators 3*1_{O_q} - 1 (q Arf-1) lie in "
          "ker N^T and SPAN it: rank = %d == 5 (v774 S9.4 transported)"
          % rk_ov, ok_ker and rk_ov == 5, kill="K4")

    # ----------------------------------------------------------------------
    section("S5: the recovery value -- sing(N/3) = {1, 2/3 x9, 0 x5}")
    # ----------------------------------------------------------------------
    X9 = sp.Matrix(NNt) / 9
    cpX = X9.charpoly(x).as_expr()
    cpX_t = sp.expand((x - 1) * (x - sp.Rational(4, 9)) ** 9 * x ** 5)
    check("S5.1 charpoly((N/3)(N/3)^T) = (x-1)(x-4/9)^9 x^5 exact -- "
          "sing(N/3) = {1, 2/3 x9, 0 x5}: THE RECOVERY VALUE 2/3",
          sp.expand(cpX - cpX_t) == 0, kill="K4")
    check("S5.2 2/3 = (N_fam - 1)/N_fam = %s (the corpus recovery "
          "survival, v327)" % Fr(N_fam - 1, N_fam),
          Fr(N_fam - 1, N_fam) == Fr(2, 3), kill="K4")

    # ----------------------------------------------------------------------
    section("S6: the compiler clock -- (2/3)^6 exponentiation identity")
    # ----------------------------------------------------------------------
    X3 = X9 ** 3        # three PSD double-steps = six channel legs
    cpX3 = X3.charpoly(x).as_expr()
    cpX3_t = sp.expand((x - 1) * (x - sp.Rational(64, 729)) ** 9 * x ** 5)
    check("S6.1 EXPONENTIATION IDENTITY: charpoly(((N/3)(N^T/3))^3) = "
          "(x-1)(x-64/729)^9 x^5 exact, and 64/729 == (2/3)^6 == the "
          "deployed lambda_2 of {1, (2/3)^6, (1/3)^6} (v330/v486; the "
          "sixth power is the compiler clock, v814)",
          sp.expand(cpX3 - cpX3_t) == 0
          and Fr(2, 3) ** 6 == Fr(64, 729), kill="K5")
    check("S6.2 TYPED GAP re-affirmed: NO (1/3)^6 mode in the doily "
          "channel -- 1/729 is NOT a root of the six-step charpoly (the "
          "deployed (1/3)^6 lives on the clock side, v814 "
          "SIXSTEP-CLOCK-ONLY [E], cited, consistent)",
          cpX3.subs(x, sp.Rational(1, 729)) != 0
          and Fr(1, 3) ** 6 == Fr(1, 729), kill="K5")

    # ----------------------------------------------------------------------
    section("C: controls (must fire; same row sums, wrong pairing)")
    # ----------------------------------------------------------------------
    TARGET_CP = cpNNt_t
    N1 = [[1 if (j - i) % 15 in (0, 1, 2) else 0 for j in range(15)]
          for i in range(15)]
    rk1 = frac_rank(N1)
    N1N1t = [[sum(N1[i][k] * N1[j][k] for k in range(15))
              for j in range(15)] for i in range(15)]
    cp1 = sp.Matrix(N1N1t).charpoly(x).as_expr()
    check("C1 FIRES: circulant 3-regular pairing: row/col sums 3, but "
          "rank = %d != 10, dim ker = %d != 5, charpoly(N'N'^T) != target"
          % (rk1, 15 - rk1),
          all(sum(r) == 3 for r in N1)
          and all(sum(N1[i][j] for i in range(15)) == 3 for j in range(15))
          and rk1 != 10 and (15 - rk1) != 5
          and sp.expand(cp1 - TARGET_CP) != 0, kill="K6")

    _LCG = [20260807]


    def lcg():
        _LCG[0] = (6364136223846793005 * _LCG[0]
                   + 1442695040888963407) % (1 << 64)
        return _LCG[0]


    def rand_perm():
        p = list(range(15))
        for i in range(14, 0, -1):
            j = lcg() % (i + 1)
            p[i], p[j] = p[j], p[i]
        return p


    perms = []
    while len(perms) < 3:
        cand = rand_perm()
        if all(all(cand[i] != q[i] for i in range(15)) for q in perms):
            perms.append(cand)
    N2 = [[sum(1 for q in perms if q[i] == j) for j in range(15)]
          for i in range(15)]
    rk2 = frac_rank(N2)
    N2N2t = [[sum(N2[i][k] * N2[j][k] for k in range(15))
              for j in range(15)] for i in range(15)]
    cp2 = sp.Matrix(N2N2t).charpoly(x).as_expr()
    check("C2 FIRES: frozen-seed LCG pairing (3 disjoint permutations, "
          "row/col sums 3): (rank, charpoly) = (%d, ...) != (10, doily "
          "target)" % rk2,
          all(sum(r) == 3 for r in N2)
          and all(sum(N2[i][j] for i in range(15)) == 3 for j in range(15))
          and not (rk2 == 10 and sp.expand(cp2 - TARGET_CP) == 0),
          kill="K6")

    # ----------------------------------------------------------------------
    section("VERDICT")
    # ----------------------------------------------------------------------
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    if not controls_ok:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = {"K1": "DOILY-BROKEN", "K2": "GRAM-BROKEN",
                   "K3": "BRIDGE-BROKEN", "K4": "RANK-MISMATCH",
                   "K5": "CLOCK-MISMATCH"}.get(KILLS[0], "CONTROL-DEAD")
    else:
        VERDICT = "DOILY-PASCAL-RANK-EXACT"
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)

    print("\nCORPUS COMPRESSION REPORT (report only -- promotion separate):")
    print("  * v774 S9 (B = I + A_KG(6,2), B B^T = 4I + 3J, spectrum")
    print("    7/2^9/(-2)^5, ovoid (-2)-eigenspace) and v814 A1 (doily")
    print("    route, sv(N/3) = {1, 2/3 x9, 0 x5}, six-step (2/3)^6):")
    print("    both sides are ONE incidence map -- N N^T = B + 2I shifts")
    print("    the spectrum 7/2/-2 -> 9/4/0, so v774's (-2)-eigenspace IS")
    print("    v814's kernel.")
    print("  * THE RANK THEOREM (new normal form): rank N = 10 = A_Lambda")
    print("    (decuple), dim ker N = 5 = g_car (carrier), multiplicity")
    print("    9 = N_fam^2, top 3 = N_fam, recovery 2/3 = (N_fam-1)/N_fam")
    print("    -- the P2 integers are the singular-value data of the")
    print("    Cremona-Richmond incidence.")
    print("  * v330/v486 deployed transfer {1,(2/3)^6,(1/3)^6}: lambda_2")
    print("    reproduced exactly by the six-leg alternation; the (1/3)^6")
    print("    gap stays typed on the clock side (v814, no upgrade).")
    print("Runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return n_pass, n_tot, VERDICT


def run():
    t_all = time.time()
    print("=" * 74)
    print("v844 -- MESSAGE.LADDER.01 + DOILY.PASCAL.RANK.01 (two exact "
          "corpus")
    print("compressions, one module from two probes; promoted verbatim)")
    print("=" * 74)
    print("\nv844 PART A -- MESSAGE.LADDER.01 "
          "(binary_message_ladder_probe, verbatim)\n")
    n_a, t_a, v_a = part_a()
    print("\nv844 PART B -- DOILY.PASCAL.RANK.01 "
          "(doily_pascal_rank_probe, verbatim)\n")
    n_b, t_b, v_b = part_b()
    ok = (n_a == t_a == N_CHECKS_A and v_a == EXPECTED_A
          and n_b == t_b == N_CHECKS_B and v_b == EXPECTED_B)
    print("\n" + "=" * 74)
    print("v844: %d/%d checks passed | verdicts %s + %s | runtime %.1f s"
          % (n_a + n_b, t_a + t_b, v_a, v_b, time.time() - t_all))
    print("[%s] PATTERN GATE: expected %d + %d checks, zero fails, "
          "verdicts %s + %s (got %d + %d, verdicts %s + %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS_A, N_CHECKS_B,
             EXPECTED_A, EXPECTED_B, n_a, n_b, v_a, v_b))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
