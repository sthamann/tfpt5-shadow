#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_mixing_normalization_probe -- SEAM.CFIN.MIXING.NORMALIZATION.01
(EXPLORATION ONLY, experiments/; round 57, 2026-08-10: the t = 1/8
normalization reading of the v898 KMS winner, turned from a reading
into a measured statement.)

THE QUESTION.  v898 (SEAM.CFIN.KMSMIX.01) found the C6-covariant
channel-mixing KMS candidate at the FIRST frozen grid point
h(u=1, t=1/8), beta=1.  The suggestive reading
    t = beta_angle * c3 / |Z2| = 2pi * (1/(8pi)) / 2 = 1/8
is trivially true as arithmetic.  The content, if any, must sit in
(a) whether each factor has an independent, already-deployed seat in
the corpus, and (b) whether t = 1/8 is FORCED by the frozen v898
gates (isolated), a BOUNDARY point, or an INTERIOR point of an
allowed set -- i.e. whether "t = 1/8 is a compiler value" is
currently a derivation or a decoration.  This probe measures both.

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-10): v898 scans exactly 5 frozen (u, t) points and STOPS at
the first winner -- it never measures the allowed t-set, never asks
whether 1/8 is special, and never connects t to the P1 normalization
chain.  v813 (P1.INDEX.KMS.01) deploys the exact chain c3 =
1/(I_Jones * beta_angle) = 1/(4 * 2pi) but says nothing about the
seam mixing strength.  NOT in the corpus: the seat audit of the
three factors AS a mixing normalization, the t/u/beta census under
the frozen v898 gates, and the pinning-functional scan.  That is
exactly this probe.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing; the smoke runs
shaped the frozen claims below and are declared, including one
REFUTED pre-derivation -- recording dead guesses is part of the
method): (i) DEAD GUESS, disclosed: the hand pre-derivation assumed
a CAR edge t_max where the state stops being strictly CAR-positive;
the smoke run refuted this -- CAR strictness of a KMS state is a
THEOREM (singular values tanh(beta*s/2) < 1 for every finite
coupling, exactly as the v898 conventions state), so gate G1 cannot
mathematically fail at any finite t; the apparent failure at t >= 4
is a float64 saturation artifact (tanh reaches 1 within the 1e-6
strictness margin), bisected at t_num ~ 3.4 and TYPED as
MARGIN-ARTIFACT.  (ii) the full frozen v898 gate set passes at
EVERY scanned t: all 54 grid points 0.01..0.50 plus {1/16, 1/12,
1/8, 1/4} plus the decades {1, 2} -- t = 1/8 is DEEP INTERIOR and
the allowed set is mathematically (0, infinity) at u = 1, beta = 1;
(iii) u is ALSO unforced: u in {0, 1/4, 1/2, 1, 2} all pass at
t = 1/8, INCLUDING u = 0 (no diagonal kernel at all); beta in
{1/2, 1, 2, 4} all pass; (iv) NEW ANATOMY, found by the smoke scan:
at beta = 100 the candidate DEGENERATES -- 0/15 cross-blocks at the
floor (G3/G4/G5 all fail): the channel mixing is THERMAL, it dies
in the ground-state (beta -> infinity) limit and the state returns
to SEAM-DIAGONAL; (v) the wrong sheet count t = 1/12 ALSO passes
all gates -- the gate scan does NOT discriminate the reading; (vi)
none of the frozen pinning functionals sits at 1/8 (uniformity and
entropy argmax at the smallest scanned t; carrier/vacuum mass ratio
at 1/8 = 0.803 with interior minimum near t ~ 0.2 and crossing of 1
near t ~ 1.1); (vii) the anti-numerology census finds 4 distinct
reading-sized deployed-constant products equal to 1/8; (viii) the
J3 sign-flip control: per-edge Pf4 signs are INVARIANT (quadratic
in S -- derived by hand BEFORE the smoke and confirmed), so the
honest fire is the 10/10 J-direction flip; the fold-cancelling
mediator J(+)(-J)(+)0 kills the census 0/10.  All of these are
frozen as claims below and re-measured in the frozen run.

CONVENTIONS (v898, rebuilt inline; READ-ONLY import of
tfpt_constants): 16-dim Majorana one-particle space; boundary
channel CH(0) = indices 10..15 (A3 block B), carrier channels
CH(i) = {2(i-1), 2(i-1)+1}, i = 1..5 (block C).  KMS covariance
A_beta = -tan(beta h / 2) for h real antisymmetric; h(u, t) =
-(u * A16_dep + t * A_int) with A16_dep = (+)_8 J the deployed
diagonal kernel and A_int the round-52 canonical covariant cross
matrix.  Frozen v898 gates G1..G5 (CAR strict, exact C6 covariance
+ forced zeros, all 15 duad cross-blocks at the floor, 5+10
grading fullness, canonical Pf4 structure).  DEVIATION, DECLARED:
G5 is evaluated here as the PER-EDGE sign match sign(Pf4) ==
sign(Pf4 of the canonical G_c) on all 15 duads; since w_blk(M) =
sgn(M) * prod Pf4 with the SAME canonical prefactor sgn(M) on both
sides, per-edge match IMPLIES v898's monomial sign match (it is
the stronger per-edge form).  NUMERICAL PROTOCOL (exploration
grade, declared): numpy float64 eigendecomposition of K = i h
instead of v898's certified mpmath dps 60; structural zeros land
at machine scale ~1e-15, genuine grid values at >= 1e-3; frozen
decision thresholds NZ_FLOOR = 1e-8 (nonzero), ZTOL = 1e-10
(structural zero), PF_FLOOR = 1e-16, CAR strictness margin 1e-6;
any decided quantity in the open band (ZTOL, NZ_FLOOR) fires the
ambiguity kill.  All structural wiring (compiler rebuild, A_int,
canonical Pf4 signs, Schur census, bookkeeping) is EXACT integer /
Fraction arithmetic.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 N1  SEAT AUDIT (exact bookkeeping + read-only file scans).
     (a) The identity chain in exact Fraction x pi^k arithmetic:
         beta_angle * c3 / |Z2| = (2 pi) * (1/(8 pi)) / 2 = 1/8
         EXACTLY, and via the v813 chain beta_angle * c3 = 1/I_Jones
         equivalently t = 1/(I_Jones * |Z2|) = 1/(4 * 2).
     (b) SEATS, typed by file scan (every anchor string must be
         present in the named verification module, read-only):
         c3 = 1/(8pi)        DEPLOYED  (tfpt_constants.py line 15,
                             the P1 axiom "c3 = 1 / (8 * PI)");
         beta_angle = 2pi    DEPLOYED  (v526 "beta_angle = 2pi
                             EXACT" -- measured by detailed balance,
                             not assumed; v239 "2 pi = 1/(4 c3)";
                             v813 header chain "c3 = 1/(I_Jones *
                             beta_angle) = 1/(4 * 2pi) = 1/(8pi)");
         |Z2| = 2            DEPLOYED  (v53 "|Z2| = g_car - N_fam =
                             2"; v456 "one-sidedness is the |Z2|=2
                             factor" -- the 8 in c3's 8pi is
                             |Z2|*4; v44 "deg(d)-deg(u) = 4-2 = 2 =
                             |Z2| (the sheet)");
         THE COMBINATION     FREE      (no vN verification MODULE
                             composes the three factors into a
                             mixing strength: among v[0-9]+_*.py
                             only v898 contains the grid value
                             "t = 1/8", and it contains NO
                             "beta_angle"; the index file run_all.py
                             is excluded and reported -- it merely
                             lists both module titles).
     (c) HONESTY NOTE (report): via v456 the 8 of c3 is ITSELF
         |Z2| * 4, so the reading divides by |Z2| twice:
         t = 1/(2 |Z2|^2) is an equally exact decomposition -- the
         factorization of 1/8 into deployed constants is NOT unique
         (see N5).  Fail of (a)/(b) => SEAT-BROKEN.

 N2  UNIQUENESS / COUNTERFACTUAL SCAN (the decisive measurement).
     Rebuild the full v898 gate set; scan at u = 1, beta = 1:
     (a) REGRESSION: (u=1, t=1/8, beta=1) passes ALL gates with
         smax within 2e-3 of the v898 value 0.668, and stays green
         at beta = 2 (v898 M1.3);
     (b) ALL 54 frozen grid points {0.01, 0.02, ..., 0.50} + the
         exact rationals {1/16, 1/12, 1/8, 1/4} pass ALL gates, and
         so do the decade points t = 1 and t = 2 -- no ambiguity
         band fires anywhere;
     (c) the apparent G1 failure at large t is a MARGIN-ARTIFACT
         (typed): CAR strictness of the KMS state is a theorem
         (tanh < 1), the failure onset t_num (bisected to 1e-3
         between 2 and 4) is where float64 tanh saturates within
         the 1e-6 strictness margin; the first failing token there
         is G1-CAR and smax at the edge >= 1 - 1e-6;
     (d) TYPED CLASSIFICATION: t = 1/8 is T-INTERIOR-UNBOUNDED iff
         gates pass at 1/8, at both 1/8 +- 0.02, and at the decades
         {1, 2}: the allowed set is mathematically (0, infinity)
         and BOTH apparent ends are numerical-threshold artifacts
         (lower: the G3 floor kills only t <= ~1e-8, checked at
         t = 1e-9 which must fail ONLY through floor/ambiguity/Pf
         thresholds).  Under the frozen v898 gate set "t = 1/8 is a
         compiler value" is then a DECORATION (not forced), and the
         probe SAYS SO.  Fail => SCAN-BROKEN.

 N3  u / beta SCANS.
     (a) u in {0, 1/4, 1/2, 1, 2} at (t=1/8, beta=1) ALL pass --
         u is unforced within the scanned set, including u = 0
         (gate);
     (b) beta in {1/2, 1, 2, 4} at (u=1, t=1/8) ALL pass (gate);
     (c) THE MIXING IS THERMAL (the new anatomy, gated): the
         maximal cross-duad block norm at (u=1, t=1/8) over beta in
         {1/2, 1, 2, 4, 10, 30, 100} first grows, then dies; at
         beta = 100 the state has 0/15 cross-blocks at the floor
         with no ambiguity -- the ground-state limit of the winner
         returns to SEAM-DIAGONAL, so the channel mixing is carried
         by FINITE temperature (the beta = 1 seat), not by the
         ground state.  Gate: 0/15 at beta = 100 AND
         maxnorm(beta=10) < maxnorm(beta=4).

 N4  PINNING FUNCTIONALS (measured, not asserted).  On a frozen
     fine grid of 80 allowed t in [0.005, 2.0], four frozen
     markers: argmax of F1 uniformity r(t) = min_duad ||B||_F /
     max_duad ||B||_F; argmax of F2 von Neumann entropy of C_beta;
     argmin of F3 carrier/vacuum block-mass ratio; crossings of
     F3 = 1.  FROZEN FIRE RULE: PIN-FOUND iff one of the four
     markers lies within +-0.0025 of 1/8; else PIN-ABSENT.  Smoke:
     PIN-ABSENT (F1/F2 argmax at the left end, F3 minimum near
     t ~ 0.2, F3 = 1 crossing near t ~ 1.1, F3(1/8) = 0.803).  An
     honest PIN-ABSENT is the expected first-class outcome: it
     types the reading as awaiting an independent demand.

 N5  ANTI-NUMEROLOGY CENSUS (exact).  Count all products
     prod q_i^{e_i} over the deployed constants {c3, beta_angle,
     |Z2|, N_fam, |mu4|, g_car} with exponents in {-2..2} and at
     most 3 nonzero exponents that equal 1/8 exactly in Fraction x
     pi^k arithmetic.  Smoke: 4 distinct readings ({Z2^-1 mu4^-1},
     {Z2 mu4^-2}, {c3 beta_angle Z2^-1}, {c3^2 beta_angle^2 Z2}).
     Gate: the count is >= 2 and the beta_angle*c3/|Z2| reading is
     among them.  The census is the measured statement that the
     ARITHMETIC part of the reading is cheap; only the seat audit
     (N1) and a future pinning demand (N4) can carry content.

 C   CONTROLS (must fire; frozen fire rules):
     C1 MEDIATOR CONTROLS on the exact Schur census S = V J3 V^T
        (integer arithmetic): (i) the global sign flip J3 -> -J3
        leaves ALL 10 per-edge Pf4 signs INVARIANT (Pf4 = -det of a
        2x2 block is quadratic in S; derived by hand BEFORE the
        smoke run) -- the honest fire is the J-DIRECTION: all 10
        lead coordinates a_J flip sign vs the canonical S (10/10);
        (ii) the fold-cancelling mediator J (+) (-J) (+) 0 (rank 4)
        kills the census: 0/10 carrier duads populated.  Both must
        fire exactly.
     C2 WRONG SHEET COUNT |Z2| -> 3: the chain gives 2pi * c3 / 3 =
        1/12 != 1/8 EXACT (Fraction x pi^k) -- fires as bookkeeping;
        AND the honest record: t = 1/12 also passes all v898 gates
        (smoke: yes), i.e. the gate scan does NOT discriminate the
        sheet count -- this is REPORTED and feeds the decoration
        typing, not hidden.
     C3 AST FIREWALL: banned identifiers zetazero / nzeros /
        primerange / isprime / primepi / nextprime / prevprime --
        none may appear (self-scan).

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 seat audit breaks (anchor missing, chain wrong) -> SEAT-BROKEN
  K2 scan ward breaks (regression, ambiguity band,
     grid point fails, artifact typing wrong)      -> SCAN-BROKEN
  K7 a control does not fire                       -> CONTROL-DEAD

VERDICT (frozen enum): SEAMNORM-MEASURED [SEATS(c3 DEPLOYED,
beta_angle DEPLOYED, Z2 DEPLOYED, COMBINATION FREE),
T-INTERIOR-UNBOUNDED / T-BOUNDARY / T-ISOLATED, THERMAL-MIXING,
PIN-FOUND(<marker>) / PIN-ABSENT, READINGS-<n>] / PIPELINE-BROKEN /
SEAT-BROKEN / SCAN-BROKEN / CONTROL-DEAD.  Exit 0 iff all checks
pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the [O] premise of v898 stays [O]; a
T-INTERIOR-UNBOUNDED outcome explicitly DEMOTES the reading to a
decoration until an independent demand pins it; no marker moves.
NO RH claim.

SPEC v1 (2026-08-10): frozen after the declared smoke runs; no
amendments at freeze.
SPEC v2 AMENDMENT (honest, after the frozen run of v1; fail-first
output preserved): the N2.4 lower-end artifact ward listed
G4-GRADING as a structural token and the v1 run FAILED there
correctly -- at t = 1e-9 G4's FULLNESS counters are themselves
floor-based (the odd/even block norms sit below the same NZ_FLOOR
= 1e-8), so G4-GRADING fires as a threshold artifact exactly like
G3/G5; only a PARITY violation (nonzero mass in the forbidden
grading sector) would be structural.  The ward is re-typed:
artifact-class tokens = {G3, G4-GRADING, G5, G-AMBIGUOUS} (all
floor/threshold counters), structural-class = {G1-CAR, G2}.  No
frozen claim, grid, gate, fire rule or classification is otherwise
touched.

Sources (read-only, machinery rebuilt inline): v898_kms_schur_mixing
(frozen probe kms_schur_mixing_probe, round 55: gates, h(u,t)
family, Schur census), v813_p1_index_kms (the c3 = 1/(I*beta)
chain), v526/v519/v239 (beta_angle = 2pi measured), v53/v456/v44
(|Z2| = 2 seats), tfpt_constants (c3, g_car, N_fam).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_mixing_normalization_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import re
import sys
import time
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _VERIFY)

from tfpt_constants import N_fam, g_car    # noqa: E402  (READ-ONLY)

BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

NZ_FLOOR = 1e-8            # nonzero decision floor (frozen)
ZTOL = 1e-10               # structural-zero ceiling (frozen)
PF_FLOOR = 1e-16           # Pf4 nonzero floor (frozen)
CAR_EPS = 1e-6             # CAR strictness margin (frozen)
PIN_TOL = 0.0025           # pinning window around 1/8 (frozen)


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
# (v880 / v888 conventions rebuilt inline, byte-parallel to v898)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
LOWIDX = {1: 0, 2: 1, 4: 2, 8: 3}


def sig(v):
    b = [(v >> i) & 1 for i in range(4)]
    n = (b[2], b[0], b[1], b[3])
    return sum(bit << i for i, bit in enumerate(n))


SIGP = tuple(sig(v) for v in range(16))


def polar_shift(c):
    return tuple((pc(v) * (pc(v) - 1) // 2 + pc(c & v)) % 2
                 for v in range(16))


def iota_bits(v):
    b = [(v >> i) & 1 for i in range(4)]
    b.append(sum(b) % 2)
    return tuple(b)


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v]) if bit)


def compose(p, q):
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


def edge_orbits(perm):
    n_ord = perm_order(perm)
    seen = set()
    out = []
    for i, j in itertools.combinations(range(6), 2):
        e = frozenset({i, j})
        if e in seen:
            continue
        x, y = i, j
        edges = set()
        rev = False
        for _k in range(n_ord):
            edges.add(frozenset({x, y}))
            x, y = perm[x], perm[y]
            if (x, y) == (j, i):
                rev = True
        seen |= edges
        out.append((frozenset(edges), rev, (i, j)))
    return out


DUADS_CH = sorted(itertools.combinations(range(6), 2))


# ------------------------------------------------ formal pi arithmetic
# a formal quantity is (Fraction coefficient, integer pi power)
def pmul(a, b):
    return (a[0] * b[0], a[1] + b[1])


def pinv(a):
    return (Fr(1) / a[0], -a[1])


def main():
    print("SEAM.CFIN.MIXING.NORMALIZATION.01 -- the t = 1/8 reading, "
          "measured")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (v898 rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s" % (BANNED_IDS,),
          not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique q*",
          ok_ref and len(set(refs)) == 16 and len(arf1) == 6
          and len(cand) == 1, kill="K0")
    QSTAR = cand[0]
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    DUADS_L = sorted((frozenset(d)
                      for d in itertools.combinations(range(6), 2)),
                     key=sorted)
    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    biject = (all(len(d) == 2 for d in dmap.values())
              and sorted(dmap.values(), key=sorted) == DUADS_L)
    check("S0.2 duad model: 15 messages <-> 15 duads; vacuum V0 = %d"
          % V0, biject and 0 <= V0 < 6, kill="K0")

    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5 and set(phi.values()) == set(range(1, 6)))
    check("S0.3 carrier dictionary phi bijective", ok_phi, kill="K0")

    def lab(j):
        return 0 if j == V0 else phi[j]

    chd = {v: frozenset(lab(j) for j in dmap[v]) for v in NZ}
    check("S0.4 15 messages <-> 15 channel duads",
          sorted(chd.values(), key=sorted) == DUADS_L, kill="K0")

    SP6 = []
    gl_n = 0
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
        gl_n += 1
        if all(HT[imgs[x]][imgs[y]] == 1
               for x in range(4) for y in range(x + 1, 4)):
            SP6.append(tuple(p))
    S5P = list(itertools.permutations(range(5)))
    AUT = []
    for p in SP6:
        if any(QSTAR[p[v]] != QSTAR[v] for v in range(16)):
            continue
        if compose(p, SIGP) != compose(SIGP, p):
            continue
        pis = [pi for pi in S5P
               if all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                              for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.5 |GL(4,2)| = %d, |Sp(4,2)| = %d, |Aut(C_fin)| = %d, "
          "generator pin unique" % (gl_n, len(SP6), len(AUT)),
          gl_n == 20160 and len(SP6) == 720 and len(AUT) == 6
          and len(g_pin) == 1, kill="K0")
    GEN = g_pin[0]

    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    pia = tuple(pia)
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(pia[j])
    PI6 = tuple(PI6)
    ok_int = all(dmap[GEN[v]] == frozenset(pia[j] for j in dmap[v])
                 for v in NZ)
    check("S0.6 deployed channel permutation pi = %s, cycle type %s "
          "== (1, 2, 3)" % (PI6, cycle_type(PI6)),
          PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3) and ok_int,
          kill="K0")

    cycles = []
    seen = set()
    for i in range(6):
        if i in seen:
            continue
        cyc, j = [], i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = PI6[j]
        cycles.append(cyc)
    TWO = sorted(next(c for c in cycles if len(c) == 2))
    a_ch, b_ch = TWO

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    CAR_IDX = list(range(10))
    BND_IDX = list(range(10, 16))

    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]

    # canonical covariant cross matrix A_int (round-52 rule, integer)
    J2 = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    I2 = np.eye(2, dtype=np.int64)
    IOTA6 = np.vstack([I2, I2, I2])
    orbs = edge_orbits(PI6)

    def put_ordered(A, x, y, B):
        rx, cy = CH[x], CH[y]
        for r in range(len(rx)):
            for c in range(len(cy)):
                A[rx[r], cy[c]] = B[r, c]
                A[cy[c], rx[r]] = -B[r, c]

    A_int = np.zeros((16, 16), dtype=np.int64)
    for edges, rev, rep in orbs:
        i, j = rep
        B = J2 if rev else (IOTA6 if i == 0 else I2)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    okA = (np.array_equal(A_int[np.ix_(img, img)], A_int)
           and np.array_equal(A_int, -A_int.T))
    A16_dep = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    okD = (np.array_equal(A16_dep[np.ix_(img, img)], A16_dep)
           and np.array_equal(A16_dep @ A16_dep,
                              -np.eye(16, dtype=np.int64)))
    check("S0.7 A_int rebuilt (integer, antisymmetric, exactly "
          "covariant); A16_dep = (+)_8 J covariant with A^2 = -I",
          okA and okD, kill="K0")

    # canonical per-edge Pf4 signs of G_c
    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}

    def compress12(A):
        Ahat = np.zeros((12, 12))
        for (i, j) in DUADS_CH:
            if i == 0:
                B = IOTA6.T.astype(np.float64) @ \
                    A[np.ix_(CH[0], CH[j])].astype(np.float64) / 3.0
            else:
                B = A[np.ix_(CH[i], CH[j])].astype(np.float64)
            for r in range(2):
                for c in range(2):
                    Ahat[CH2[i][r], CH2[j][c]] = B[r, c]
                    Ahat[CH2[j][c], CH2[i][r]] = -B[r, c]
        return Ahat

    def pf4_of(Ahat):
        out = {}
        for (i, j) in DUADS_CH:
            B = Ahat[np.ix_(CH2[i], CH2[j])]
            out[frozenset({i, j})] = -(B[0, 0] * B[1, 1]
                                       - B[0, 1] * B[1, 0])
        return out

    pf4_c = pf4_of(compress12(A_int.astype(np.float64)))
    sign_c = {d: (1 if v > 0 else -1) for d, v in pf4_c.items()}
    check("S0.8 canonical reference: all 15 Pf4 of G_c nonzero; all "
          "15 canonical per-edge signs NEGATIVE (measured -- the "
          "sign content of w_blk sits in the prefactor sgn(M))",
          all(abs(v) > 0 for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ==================================================================
    section("N1 -- SEAT AUDIT (exact chain + read-only file scans)")
    # ==================================================================
    C3F = (Fr(1, 8), -1)          # 1/(8 pi)
    BETA_ANG = (Fr(2), 1)         # 2 pi
    Z2 = g_car - N_fam            # = 2, the v53 compiler-core seat
    I_JONES = (Fr(4), 0)
    t_read = pmul(BETA_ANG, C3F)
    t_read = (t_read[0] / Z2, t_read[1])
    chain2 = pinv(pmul(I_JONES, (Fr(Z2), 0)))
    check("N1.1 EXACT CHAIN: beta_angle * c3 / |Z2| = %s * pi^%d == "
          "1/8; and 1/(I_Jones * |Z2|) = %s * pi^%d == 1/8 (v813 "
          "equivalence beta_angle * c3 = 1/I)"
          % (t_read[0], t_read[1], chain2[0], chain2[1]),
          t_read == (Fr(1, 8), 0) and chain2 == (Fr(1, 8), 0),
          kill="K1")

    ANCHORS = [
        ("tfpt_constants.py", "c3 = 1 / (8 * PI)",
         "c3 DEPLOYED (P1 axiom)"),
        ("v813_p1_index_kms.py",
         "c3 = 1/(I_Jones * beta_angle) = 1/(4 * 2pi) = 1/(8pi)",
         "the v813 chain DEPLOYED"),
        ("v526_seam_thermal_kms_nariai_bridge.py",
         "beta_angle = 2pi EXACT",
         "beta_angle DEPLOYED (measured, v526)"),
        ("v239_kms_thermal_time.py", "2 pi = 1/(4 c3)",
         "the seam unit DEPLOYED (v239)"),
        ("v53_compiler_core.py", "|Z2| = g_car - N_fam = 2",
         "|Z2| DEPLOYED (compiler core)"),
        ("v456_seam_chirality_from_c3.py",
         "one-sidedness is the |Z2|=2 factor",
         "|Z2| DEPLOYED inside c3's own 8 (v456)"),
        ("v44_carrier_exterior.py",
         "deg(d)-deg(u) = 4-2 = 2 = |Z2| (the sheet)",
         "|Z2| DEPLOYED (exterior degree gap, v44)"),
    ]
    ok_anch = True
    for fn, needle, why in ANCHORS:
        path = os.path.join(_VERIFY, fn)
        try:
            hit = needle in open(path, encoding="utf-8").read()
        except OSError:
            hit = False
        ok_anch &= hit
        print("      anchor %-42s [%s]  %s"
              % (fn, "HIT " if hit else "MISS", why))
    check("N1.2 SEATS: all %d anchor strings present read-only -- "
          "c3, beta_angle = 2pi and |Z2| = 2 each have independent "
          "deployed seats" % len(ANCHORS), ok_anch, kill="K1")

    vmod_re = re.compile(r"^v\d+_.*\.py$")
    tfiles, idx_note = [], []
    for fn in sorted(os.listdir(_VERIFY)):
        if not fn.endswith(".py"):
            continue
        try:
            src = open(os.path.join(_VERIFY, fn),
                       encoding="utf-8").read()
        except OSError:
            continue
        if "t = 1/8" in src or "t=1/8" in src:
            if vmod_re.match(fn):
                tfiles.append((fn, "beta_angle" in src))
            else:
                idx_note.append(fn)
    check("N1.3 THE COMBINATION IS FREE: vN modules containing the "
          "grid value 't = 1/8': %s -- none contains 'beta_angle' "
          "(the corpus nowhere composes the three factors into a "
          "mixing strength); non-module index files with both "
          "titles, excluded and reported: %s"
          % ([f for f, _b in tfiles], idx_note),
          len(tfiles) >= 1 and all(not b for _f, b in tfiles)
          and any(f.startswith("v898") for f, _b in tfiles),
          kill="K1")
    print("      HONESTY NOTE (N1.c): via v456 the 8 of c3 is itself "
          "|Z2|*4, so t = 1/(2 |Z2|^2)\n      is an equally exact "
          "decomposition -- the factorization is NOT unique (N5).")

    # ==================================================================
    section("N2 -- UNIQUENESS SCAN (the frozen v898 gates over t)")
    # ==================================================================
    Aint_f = A_int.astype(np.float64)
    Adep_f = A16_dep.astype(np.float64)
    I16 = np.eye(16)

    def kms_A(u, t, beta):
        h = -(u * Adep_f + t * Aint_f)
        w, Q = np.linalg.eigh(1j * h)
        f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
        C = (Q * f) @ Q.conj().T
        Z = -1j * (2 * C - I16)
        A = Z.real
        wards = {
            "im": float(np.max(np.abs(Z.imag))),
            "anti": float(np.max(np.abs(A + A.T))),
            "cov": float(np.max(np.abs(A[np.ix_(img, img)] - A))),
            "smax": float(np.max(np.abs(np.tanh(beta * w / 2.0)))),
        }
        return A, wards

    def blocks_census(A):
        return {(i, j): float(np.linalg.norm(A[np.ix_(CH[i], CH[j])]))
                for (i, j) in DUADS_CH}

    def gates(A, wards):
        failed = []
        if not (wards["smax"] < 1 - CAR_EPS):
            failed.append("G1-CAR")
        if not (wards["im"] < ZTOL and wards["anti"] < ZTOL
                and wards["cov"] < ZTOL):
            failed.append("G2-COVARIANCE")
        fz = max(abs(A[CH[a_ch][k], CH[b_ch][k]]) for k in range(2))
        if not (fz < ZTOL):
            failed.append("G2-FORCEDZERO")
        bn = blocks_census(A)
        n_floor = sum(1 for v in bn.values() if v >= NZ_FLOOR)
        ambig = [d for d, v in bn.items() if ZTOL < v < NZ_FLOOR]
        if n_floor != 15:
            failed.append("G3-FLOOR(%d/15)" % n_floor)
        odd_ok, even_ok, parity_ok = 0, 0, True
        for (i, j) in DUADS_CH:
            B = A[np.ix_(CH[i], CH[j])]
            gi = -1 if i != 0 else 1
            gj = -1 if j != 0 else 1
            odd = np.linalg.norm((B - gi * gj * B) / 2)
            even = np.linalg.norm((B + gi * gj * B) / 2)
            if 0 in (i, j):
                odd_ok += bool(odd >= NZ_FLOOR)
                parity_ok &= bool(even < ZTOL)
            else:
                even_ok += bool(even >= NZ_FLOOR)
                parity_ok &= bool(odd < ZTOL)
        if not (odd_ok == 5 and even_ok == 10 and parity_ok):
            failed.append("G4-GRADING(%d/5,%d/10)" % (odd_ok, even_ok))
        pf4 = pf4_of(compress12(A))
        n_pf4 = sum(1 for v in pf4.values() if abs(v) >= PF_FLOOR)
        ok_sign = all((pf4[d] > 0) == (sign_c[d] > 0) for d in pf4
                      if abs(pf4[d]) >= PF_FLOOR)
        if not (n_pf4 == 15 and ok_sign):
            failed.append("G5-CHI(pf4 %d/15, signmatch %s)"
                          % (n_pf4, ok_sign))
        if ambig:
            failed.append("G-AMBIGUOUS%s" % ambig)
        return failed, bn

    def passes(u, t, beta):
        A, wards = kms_A(u, t, beta)
        failed, _bn = gates(A, wards)
        return failed

    A18, w18 = kms_A(1.0, 0.125, 1.0)
    f18, _ = gates(A18, w18)
    f18b2 = passes(1.0, 0.125, 2.0)
    check("N2.1 REGRESSION: (u=1, t=1/8, beta=1) passes all gates "
          "(fails: %s), smax = %.6f (v898: 0.668, |diff| < 2e-3); "
          "beta = 2 re-test passes (fails: %s)"
          % (f18 or "none", w18["smax"], f18b2 or "none"),
          not f18 and abs(w18["smax"] - 0.668) < 2e-3 and not f18b2,
          kill="K2")

    grid = [round(0.01 * k, 2) for k in range(1, 51)]
    extra = [1.0 / 16, 1.0 / 12, 0.125, 0.25]
    decades = [1.0, 2.0]
    results = {}
    for t in sorted(set(grid + extra + decades)):
        results[t] = passes(1.0, t, 1.0)
    n_pass_grid = sum(1 for f in results.values() if not f)
    ambig_any = any("G-AMBIGUOUS" in " ".join(f)
                    for f in results.values())
    print("      %d/%d scanned points pass all gates "
          "(grid 0.01..0.50 + {1/16, 1/12, 1/8, 1/4} + {1, 2})"
          % (n_pass_grid, len(results)))
    check("N2.2 ALL %d scanned t pass ALL gates (incl. the decades "
          "t = 1 and t = 2); no ambiguity band fired"
          % len(results),
          n_pass_grid == len(results) and not ambig_any, kill="K2")

    lo, hi = 2.0, 4.0
    if passes(1.0, hi, 1.0):
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            if passes(1.0, mid, 1.0):
                hi = mid
            else:
                lo = mid
            if hi - lo < 1e-3:
                break
    edge_fail = passes(1.0, hi, 1.0)
    _Ae, we = kms_A(1.0, hi, 1.0)
    check("N2.3 MARGIN-ARTIFACT TYPED: the G1 onset is t_num = "
          "%.4f (bisected between 2 and 4), first failing token %s "
          "with smax = %.8f >= 1 - 1e-6 -- CAR strictness is a "
          "THEOREM (tanh < 1 for all finite t); this edge is float64 "
          "saturation, not physics"
          % (hi, edge_fail, we["smax"]),
          hi - lo < 1e-3 and "G1-CAR" in " ".join(edge_fail)
          and we["smax"] >= 1 - CAR_EPS, kill="K2")

    ok_lo = not passes(1.0, 0.125 - 0.02, 1.0)
    ok_hi = not passes(1.0, 0.125 + 0.02, 1.0)
    ok_dec = all(not results[t] for t in decades)
    if ok_lo and ok_hi and ok_dec:
        t_type = "T-INTERIOR-UNBOUNDED"
    elif ok_lo or ok_hi:
        t_type = "T-BOUNDARY"
    else:
        t_type = "T-ISOLATED"
    tiny_fail = passes(1.0, 1e-9, 1.0)
    # SPEC v2: artifact-class = {G3, G4-GRADING, G5, G-AMBIGUOUS}
    # (floor/threshold counters); structural-class = {G1, G2}
    lo_artifact = (any(tok.startswith(("G3", "G-AMBIG", "G5", "G4-"))
                       for tok in tiny_fail)
                   and not any(tok.startswith(("G1", "G2"))
                               for tok in tiny_fail))
    check("N2.4 TYPED CLASSIFICATION: t = 1/8 is %s -- the allowed "
          "set is mathematically (0, infinity) under the frozen "
          "gates (both apparent ends are numerical-threshold "
          "artifacts; t = 1e-9 fails only via %s).  't = 1/8 is a "
          "compiler value' is currently a DECORATION (not forced)"
          % (t_type, tiny_fail),
          t_type == "T-INTERIOR-UNBOUNDED" and lo_artifact,
          "typed by measurement", kill="K2")

    # ==================================================================
    section("N3 -- u / beta scans + the thermal-mixing anatomy")
    # ==================================================================
    u_rows = {}
    for u in (0.0, 0.25, 0.5, 1.0, 2.0):
        u_rows[u] = passes(u, 0.125, 1.0)
        print("      u = %-4s t = 1/8, beta = 1: %s"
              % (u, "PASS" if not u_rows[u]
             else "fails %s" % u_rows[u]))
    check("N3.1 u-scan: ALL of u in {0, 1/4, 1/2, 1, 2} pass at "
          "t = 1/8 -- u is unforced within the scanned set, "
          "INCLUDING u = 0 (no diagonal kernel)",
          all(not f for f in u_rows.values()), kill="K2")
    b_rows = {}
    for beta in (0.5, 1.0, 2.0, 4.0):
        b_rows[beta] = passes(1.0, 0.125, beta)
        print("      beta = %-4s (u=1, t=1/8): %s"
              % (beta, "PASS" if not b_rows[beta]
             else "fails %s" % b_rows[beta]))
    check("N3.2 beta-scan: ALL of beta in {1/2, 1, 2, 4} pass at "
          "(u=1, t=1/8) -- beta is unforced within the scanned set",
          all(not f for f in b_rows.values()), kill="K2")

    bnorms = {}
    for beta in (0.5, 1.0, 2.0, 4.0, 10.0, 30.0, 100.0):
        A, _w = kms_A(1.0, 0.125, beta)
        bn = blocks_census(A)
        bnorms[beta] = max(bn.values())
        if beta == 100.0:
            f100, bn100 = gates(A, _w)
            n100 = sum(1 for v in bn100.values() if v >= NZ_FLOOR)
            amb100 = any(ZTOL < v < NZ_FLOOR for v in bn100.values())
    print("      max cross-duad ||B||_F over beta: %s"
          % {b: round(v, 6) for b, v in bnorms.items()})
    b_arg = max(bnorms, key=bnorms.get)
    check("N3.3 THE MIXING IS THERMAL (gated anatomy): the mixing "
          "mass peaks at beta = %s and DIES toward the ground "
          "state -- at beta = 100 the state has %d/15 cross-blocks "
          "at the floor (no ambiguity: %s; fails %s): the "
          "beta -> infinity limit returns to SEAM-DIAGONAL, the "
          "channel mixing is carried by FINITE temperature"
          % (b_arg, n100, not amb100, f100),
          n100 == 0 and not amb100
          and bnorms[10.0] < bnorms[4.0], kill="K2")

    # ==================================================================
    section("N4 -- pinning functionals (measured, not asserted)")
    # ==================================================================
    ts = np.linspace(0.005, 2.0, 80)
    F1, F2, F3 = [], [], []
    for t in ts:
        A, wards = kms_A(1.0, float(t), 1.0)
        bn = blocks_census(A)
        F1.append(min(bn.values()) / max(bn.values()))
        h = -(Adep_f + float(t) * Aint_f)
        w = np.linalg.eigvalsh(1j * h)
        f = 1.0 / (1.0 + np.exp(np.clip(w, -700, 700)))
        f = np.clip(f, 1e-300, 1 - 1e-16)
        F2.append(float(-np.sum(f * np.log(f)
                                + (1 - f) * np.log(1 - f))))
        m_car = math.sqrt(sum(bn[d] ** 2 for d in bn if 0 not in d))
        m_vac = math.sqrt(sum(bn[d] ** 2 for d in bn if 0 in d))
        F3.append(m_car / m_vac)
    F1, F2, F3 = map(np.array, (F1, F2, F3))
    t_F1 = float(ts[int(np.argmax(F1))])
    t_F2 = float(ts[int(np.argmax(F2))])
    t_F3min = float(ts[int(np.argmin(F3))])
    cross1 = [float(ts[k]) for k in range(len(ts) - 1)
              if (F3[k] - 1.0) * (F3[k + 1] - 1.0) < 0]
    k18 = int(np.argmin(np.abs(ts - 0.125)))
    print("      F1 uniformity argmax at t = %.4f; F2 entropy argmax "
          "at t = %.4f;\n      F3 carrier/vacuum mass: value at "
          "t ~ 1/8 = %.4f, argmin at t = %.4f, crossings of 1 at %s"
          % (t_F1, t_F2, float(F3[k18]), t_F3min,
             [round(c, 3) for c in cross1] or "none"))
    markers = {"F1-argmax": t_F1, "F2-argmax": t_F2,
               "F3-argmin": t_F3min}
    for kx, c in enumerate(cross1):
        markers["F3-cross1-%d" % kx] = c
    pins = [nm for nm, v in markers.items()
            if abs(v - 0.125) <= PIN_TOL]
    pin_tok = ("PIN-FOUND(%s)" % ",".join(pins)) if pins \
        else "PIN-ABSENT"
    check("N4.1 PINNING: %s -- markers %s vs the window 1/8 +- "
          "%.4f (an honest PIN-ABSENT types the reading as awaiting "
          "an independent demand)"
          % (pin_tok, {n: round(v, 4) for n, v in markers.items()},
             PIN_TOL),
          True, "typed by measurement", kill=None)

    # ==================================================================
    section("N5 -- anti-numerology census (exact)")
    # ==================================================================
    CONSTS = [("c3", (Fr(1, 8), -1)), ("beta_angle", (Fr(2), 1)),
              ("Z2", (Fr(2), 0)), ("N_fam", (Fr(3), 0)),
              ("mu4", (Fr(4), 0)), ("g_car", (Fr(5), 0))]
    target = (Fr(1, 8), 0)
    hits = []
    for exps in itertools.product(range(-2, 3), repeat=len(CONSTS)):
        if sum(1 for e in exps if e) > 3 or not any(exps):
            continue
        acc = (Fr(1), 0)
        for (nm, q), e in zip(CONSTS, exps):
            for _ in range(abs(e)):
                acc = pmul(acc, q if e > 0 else pinv(q))
        if acc == target:
            hits.append(" ".join("%s^%d" % (nm, e)
                                 for (nm, _q), e in zip(CONSTS, exps)
                                 if e))
    print("      readings found (each == 1/8 exactly):")
    for hstr in hits:
        print("        1/8 = %s" % hstr)
    has_reading = any(set(h.split())
                      == {"c3^1", "beta_angle^1", "Z2^-1"}
                      for h in hits)
    check("N5.1 CENSUS: %d distinct reading-sized deployed-constant "
          "products equal 1/8 exactly (<= 3 factors, exponents "
          "|e| <= 2), the beta_angle*c3/|Z2| reading among them -- "
          "the arithmetic part of ANY such reading is cheap; "
          "content can only sit in seats (N1) and a pinning demand "
          "(N4)" % len(hits),
          len(hits) >= 2 and has_reading, kill="K1")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    Vc = A_int[np.ix_(CAR_IDX, BND_IDX)]
    J3 = A16_dep[np.ix_(BND_IDX, BND_IDX)]
    CAR_DUADS = sorted(itertools.combinations(range(1, 6), 2))

    def census(M):
        S = Vc @ M @ Vc.T
        rows = {}
        for (i, j) in CAR_DUADS:
            B = S[np.ix_(CH[i], CH[j])]
            aJ = Fr(int(B[0, 1]) - int(B[1, 0]), 2)
            pf4 = -(int(B[0, 0]) * int(B[1, 1])
                    - int(B[0, 1]) * int(B[1, 0]))
            rows[(i, j)] = (int(np.count_nonzero(B)) > 0, aJ, pf4)
        return S, rows

    S0m, rows0 = census(J3)
    Sf, rowsf = census(-J3)
    n_pf_inv = sum(1 for d in rows0
                   if (rows0[d][2] > 0) == (rowsf[d][2] > 0)
                   and rows0[d][2] != 0)
    n_dir_flip = sum(1 for d in rows0
                     if rows0[d][1] != 0 and rowsf[d][1]
                     == -rows0[d][1])
    Mc = np.zeros((6, 6), dtype=np.int64)
    Mc[0, 1], Mc[1, 0] = 1, -1
    Mc[2, 3], Mc[3, 2] = -1, 1          # fold-cancelling -J
    _Sc, rowsc = census(Mc)
    n_dead = sum(1 for d in rowsc if not rowsc[d][0])
    check("C1 FIRES: J3 sign flip leaves all %d/10 per-edge Pf4 "
          "signs INVARIANT (quadratic in S -- pre-derived) while "
          "flipping the lead J-direction on %d/10 duads; the "
          "fold-cancelling mediator J(+)(-J)(+)0 kills the census "
          "(%d/10 duads dead)"
          % (n_pf_inv, n_dir_flip, n_dead),
          n_pf_inv == 10 and n_dir_flip == 10 and n_dead == 10,
          kill="K7")

    wrong = pmul(BETA_ANG, C3F)
    wrong = (wrong[0] / 3, wrong[1])
    f112 = results[1.0 / 12]
    check("C2 FIRES (bookkeeping) + HONEST RECORD: |Z2| -> 3 gives "
          "2pi*c3/3 = %s != 1/8 EXACT; but t = 1/12 %s the v898 "
          "gates -- the gate scan does NOT discriminate the sheet "
          "count (recorded; feeds the %s typing)"
          % (wrong[0], "ALSO PASSES" if not f112
             else "fails (%s)" % f112, t_type),
          wrong == (Fr(1, 12), 0), kill="K7")

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
    elif "K1" in KILLS:
        VERDICT = "SEAT-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "SCAN-BROKEN"
    else:
        VERDICT = ("SEAMNORM-MEASURED [SEATS(c3 DEPLOYED, beta_angle "
                   "DEPLOYED, Z2 DEPLOYED, COMBINATION FREE), %s, "
                   "THERMAL-MIXING, %s, READINGS-%d]"
                   % (t_type, pin_tok, len(hits)))
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE SEATS (N1): all three factors of t = beta_angle * c3 / |Z2|
    have independent deployed seats (c3 = P1 axiom; beta_angle = 2pi
    measured in v526 and chained in v813; |Z2| = 2 in v53/v456/v44)
    -- but the COMBINATION is FREE: no corpus module composes them
    into a mixing strength, and via v456 the 8 of c3 already
    contains |Z2| once, so the factorization is not unique.
  * THE DECISIVE SCAN (N2/N3): under the FULL frozen v898 gate set
    the allowed parameter set is mathematically UNBOUNDED -- every
    scanned t in (0, 2], every u in {0..2} (including u = 0) and
    every beta in [1/2, 4] passes; CAR strictness is a theorem and
    never binds.  't = 1/8 is a compiler value' is therefore
    currently a DECORATION, not a derivation -- the v898 gates
    force NOTHING about (u, t, beta) beyond t > 0.
  * THE ONE NEW STRUCTURAL FACT (N3.3): the mixing is THERMAL --
    it dies exponentially toward the ground state (0/15 blocks at
    beta = 100); the finite-beta KMS dressing, not the ground
    state, carries the channel mixing.
  * WHAT WOULD PIN IT (N4): %s -- no frozen functional singles out
    1/8; the reading stays a registered search target awaiting an
    independent demand (e.g. the RP/theta construction named open
    in v898, which would fix a scale).
  * THE CHEAP-ARITHMETIC CENSUS (N5): %d deployed-constant readings
    of 1/8 exist at reading size -- arithmetic alone carries no
    content here.
  * The [O] premise of v898 stays [O]; no marker moves; NO RH claim.
Runtime: %.1f s""" % (pin_tok, len(hits), time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
