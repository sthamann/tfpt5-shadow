#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v898 -- SEAM.CFIN.KMSMIX.01 + SEAM.CFIN.SCHURMIX.01: THE CHANNEL-MIXING STATE THE BLOCK WICK FUNCTOR AWAITS -- the C6-covariant channel-mixing KMS state EXISTS and the Schur/Feshbach boundary elimination GENERATES all 10 carrier duads exactly, ONE module from one probe (30/30 checks, zero fails, verdict KMSMIX-MEASURED [KMSMIX-FOUND(u=1, t=1/8, beta=1), SCHURMIX-GENERATES(10/10 carrier duads, C6-covariant, J-direction, Pf4 signs canonical), RP-THETA-OPEN]; discovery probe kms_schur_mixing_probe.py, round 55, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~2 s).  THE V896 DEMAND ('a physical channel-mixing mechanism realizing the block functor's value level') now has a CONSTRUCTED CANDIDATE STATE.  (1) THE PARAMETRIZATION (exact orbit walks): the hermitian O16-commutant on the deployed 16-dim one-particle space has dimension 112 = 62 sym + 50 antisym (isotypic mults [10,0,2,2,2,0], sum m^2 ward); the Majorana-compatible Hamiltonians K = i h live in the 50-dim antisymmetric slice = 33 cross-block (EXACTLY the v896 covariant block space; the C<->B mixing block T spans 24) + 17 channel-diagonal, with exactly 2 forced zeros (the diagonal of the transposed {4,5} block).  (2) THE KMS ROUTE: the FIRST point of the frozen grid, h(u=1, t=1/8) = -(A16_dep + (1/8) A_int) at beta = 1, passes ALL gates -- CAR strict (smax 0.668 < 1), exact C6 block covariance with the forced zeros, all 15 duad cross-blocks at the frozen floor, the q*/sheet grading carried EXACTLY (Ad(Gamma16)-odd support = the 5 vacuum blocks 5/5 FULL, even off-diagonal = the 10 carrier blocks 10/10 FULL), and all 15 block Wick monomials nonzero with the CANONICAL Pf4 sign pattern of the v896 block functor G_c; ROBUST at beta = 2 (all gates again); the per-orbit ray anatomy shows the tan/KMS dressing itself MIXES (odd powers of h light duads outside the seeded orbit -- the Schur mechanism operating inside the KMS route).  (3) THE SCHUR ROUTE (EXACT sympy rationals): boundary elimination of the coupled diagonal state A_full = [[kappa A_CC, t V], [-t V^T, m J3]] (kappa = m = 1/2, t = 1/20; validity PROVEN exactly: ||A_full|| <= 1/2 + sqrt(15)/20 < 1) gives the EXACT identity A_eff = kappa A_CC + (t^2 m/(1-m^2)) V J3 V^T, and the census matrix S = V J3 V^T deposits NONZERO correlation on ALL 10 carrier duads (C6-covariant, uniform 3J-block: B = 3J on every carrier duad, pure J on the transposed {4,5} exactly as covariance allows, per-edge Pf4 signs MATCHING the canonical G_c) -- the SAME Schur/Feshbach elimination that creates the RH port creates the carrier channel mixing from a BARE DIAGONAL state: on both fronts (RH port, Wick functor) the real correlation lives in the ELIMINATED boundary, not the bare bulk.  (4) THE FROZEN PREDICTION TABLE: the 15 block-correlation signatures of the winner (zero/nonzero pattern, canonical-unit coordinates and signs, per-edge Pf4 sign, C6 orbit, q* class) are printed as the REGISTERED prediction -- any physical seam state realizing the block functor must reproduce this pattern.  (5) HONEST RP: NO spatial/OS reflection theta is deployed on the 16-dim one-particle space (v155 premise-only, v160 none, v424/v426/v440 = 8-dim collar dictionary); the Majorana real structure Theta_0 satisfies the deployed dictionary AUTOMATICALLY (conj(C_beta) = I - C_beta measured at 7.8e-61) but is particle-hole, NOT spatial; the OS-positivity under a SPATIAL theta is the NAMED OPEN CHECK RP-THETA-OPEN.  CONTROLS FIRE: permuted roles break covariance (defect 0.096), grading commutation (16) and the edge law on EXACTLY 8/15; the bare diagonal state (t = 0) has 0/15 KMS cross-blocks and 0/10 Schur carrier duads.  THE [O] PREMISE IS UNMOVED: these are CANDIDATE states and frozen signatures -- whether the ACTUAL seam realizes any of them is untouched; no marker moves.  NO RH claim (compiler side; no primes, no zeros).  Exact integer / sympy rational arithmetic in every structural decision; the only non-exact step is the certified-precision (mpmath dps 60) KMS transcendental map with FROZEN two-sided decision thresholds (nonzero >= 1e-8, zero <= 1e-40; ambiguity kills).  Deterministic, no RNG.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe kms_schur_mixing_probe.py (30/30,
KMSMIX-MEASURED [KMSMIX-FOUND(u=1, t=1/8, beta=1),
SCHURMIX-GENERATES(10/10), RP-THETA-OPEN], SPEC v1 frozen
2026-08-09 pre-run, no amendments; frozen expectations pre-derived
by hand before the freeze), round 55, 2026-08-09, re-run
identically at promotion.  ROUND-31 EMBEDDING CONVENTION: frozen
source embedded BYTE-EXACT, executed verbatim in an isolated
namespace; printed spec SHA reproduces; byte-equality ward vs
experiments/tfpt-discovery/ inside the pattern gate.  The probe
consumes tfpt_constants (READ-ONLY) and rebuilds the v880/v888/
v113/v896 machinery inline.

FIREWALL: no zeros, no prime-table oracles (AST firewall inside
the probe); NO physics-realization claim -- the [O] premise (the
boundary grammar IS a self-hosting Wick pair compiler) stays [O];
RP-THETA-OPEN is a named open check, not a gate.  NO RH claim.
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

# ------------- frozen probe source kms_schur_mixing_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kms_schur_mixing_probe -- SEAM.CFIN.KMSMIX.01 + SEAM.CFIN.SCHURMIX.01
(EXPLORATION ONLY, experiments/; round 55, reviewer priority 5: the
PHYSICAL MECHANISM the block Wick functor awaits.  Round 52
(wick_block_functor_probe) constructed the canonical C6-covariant
block object G_c on the deployed 16-dim one-particle space and
MEASURED the deployed seam vacuum SEAM-DIAGONAL -- the functor's
value level is a pure candidate awaiting a channel-mixing STATE.
THIS probe constructs that state via the two reviewer routes: (M1)
the fermionic KMS state of a C6-invariant mixing one-particle
Hamiltonian, and (M2) the Schur/Feshbach dressing -- boundary
elimination of a coupled diagonal state -- the SAME operation that
creates the RH port.)

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-09 -- read end to end: wick_block_functor_probe (round 52),
wick_mixing_covariance_probe (round 51), seam_wick_functor_probe
(round 50), v113/v155/v160/v161, v424/v426/v440, v880/v888):
 * round 52 froze the canonical block candidate G_c (all 15
   cross-blocks at FLOOR = 1/200, C6-covariant, CAR-positive, chi
   sign law) and typed the deployed seam SEAM-DIAGONAL; it built NO
   state-generating mechanism (no Hamiltonian, no KMS, no Schur).
 * v426/v440 deploy the KMS/RP dictionary (C_beta = (I+e^{beta
   K})^{-1}; (LTO-RP)/BW <=> Theta K Theta = -K; Theta C_beta Theta
   = I - C_beta) on an 8-dim COLLAR TOY space (4 marks x 2 sides)
   -- NOT on the deployed 16-dim D5+A3 one-particle space; v155
   carries reflection positivity only as the recorded [P] premise
   (no operator); v160 has no reflection operator at all.
 * NOTHING in the corpus parametrizes C6-invariant one-particle
   Hamiltonians on the 16-dim space, computes their KMS states, or
   asks whether boundary elimination (Schur) of the DEPLOYED
   diagonal state generates carrier cross-blocks.  That is exactly
   this probe.

CAR CONVENTION (FROZEN, v113 / rounds 50-52): 16-dim real Majorana
one-particle space; channels CH(0) = Majoranas 10..15 (A3 boundary
block B, dim 6), CH(i) = {2(i-1), 2(i-1)+1} for i = 1..5 (D5 slot
pairs; carrier block C = indices 0..9).  A quasifree CAR covariance
is G = (I + iA)/2 with A REAL ANTISYMMETRIC; CAR positivity 0 <= G
<= I <=> spec-norm(A) <= 1.  A quadratic Majorana Hamiltonian has
one-particle operator K = i h with h REAL ANTISYMMETRIC (K
hermitian, K^T = -K); the beta-KMS covariance is C_beta = (I +
e^{beta K})^{-1}, equivalently A_beta = -tan(beta h / 2) (exact
identity: iA = 2C - I = -tanh(beta K/2), tanh(i x) = i tan(x)) --
AUTOMATICALLY 0 < C_beta < I (singular values tanh(beta s/2) < 1).
C6 acts by the round-50 lift O16 (slot pairs as units by pi = (0)
(a b)(c d e), identity on the A3 block); Gamma16 = (-I on C) (+)
(+I on B) is the q* grading operator (round 52).

THE TWO FROZEN CONSTRUCTIONS:

 M1 THE KMS ROUTE.  Parametrize K = i h = [[K_C, T],[T*, K_B]]
    with h in the EXACT real-antisymmetric O16-commutant (the
    Majorana-compatible slice of the hermitian commutant; both
    dimensions measured by exact signed orbit walks: hermitian side
    expected 112 = 62 sym + 50 antisym, cross/mixing part 33 =
    round-52 block space, of which the C<->B mixing block T spans
    24).  FROZEN scan family (coarse grid + natural rays -- no
    fitting):
        h(u, t) = -( u * A16_dep + t * A_int ),
    where A16_dep = (+)_8 J is the DEPLOYED diagonal kernel
    (v113/v155 hull) and A_int is the round-52 canonical integer
    covariant cross matrix (units [I2;I2;I2] / I2 / J, orientation-
    propagated).  The overall sign -1 is the FROZEN convention
    aligning the beta -> 0+ linearization A ~ (beta/2)(u A16_dep +
    t A_int) with the canonical orientation of G_c (structural
    rule, frozen before first run; the + branch is reported in the
    anatomy).  Grid (frozen order, beta = 1 primary): (u, t) in
    [(1, 1/8), (1, 1/4), (1, 1/2), (1, 1), (0, 1/4)]; winner = the
    FIRST grid point passing all gates; robustness re-test of the
    winner at beta = 2 (report, not gate).  Gates per candidate:
      (G1) CAR: 0 < C < I strict (theorem; measured ward);
      (G2) exact C6 block covariance + the round-51/52 forced
           zeros on the diagonal of the transposed {a,b} block;
      (G3) all 15 duad cross-blocks nonzero at the frozen floor;
      (G4) the q*/sheet grading carried (round-52 test: [Gamma16,
           O16] = 0, edge law on all 15 messages, Ad(Gamma16)-odd
           support = the 5 vacuum blocks 5/5 FULL, even off-diag =
           the 10 carrier blocks 10/10 FULL);
      (G5) the canonical Pfaffian/chi structure (round-52 test):
           Iota/3-compressed Ahat, all 15 per-edge Pf4 nonzero,
           all 15 block Wick monomials w_blk(M) = sgn(M) prod Pf4
           nonzero, interleaving ward Pf(Ahat|_M) == prod Pf4, and
           the SIGN MATCH sign(w_blk) == sign(w_blk of the
           canonical G_c) on all 15 matchings.
    TYPED: KMSMIX-FOUND(u, t, beta) / KMSMIX-OBSTRUCTED(per-point
    failing gates).  ANATOMY (report): per-orbit rays (u = 1, one
    edge orbit of A_int at t = 1/4) -- which duads each ray LIGHTS
    UP under the tan dressing (the KMS map itself mixes: odd powers
    of h generate blocks outside the seeded orbit -- the Schur
    mechanism inside the KMS route); the + sign branch.
 M1(iv) REFLECTION POSITIVITY (typed honestly).  The corpus
    answer, measured by reading: NO canonical spatial/OS reflection
    theta is deployed on the 16-dim one-particle space (v155:
    premise only; v160: none; v424/v426/v440: the dictionary Theta
    K Theta = -K, Theta C_beta Theta = I - C_beta -- deployed on an
    8-dim collar toy, not on D5+A3).  What CAN be tested: the
    MAJORANA REAL STRUCTURE Theta_0 = complex conjugation in the
    deployed Majorana basis is antiunitary, commutes with O16 and
    Gamma16, and satisfies the deployed v426/v440 dictionary
    AUTOMATICALLY for every K = i h (h real): Theta_0 K Theta_0 =
    conj(K) = -K (BW form) and conj(C_beta) = I - C_beta (the v440
    reflection relation) -- both verified on the winner.  The
    OS-positivity of the two-point block under a SPATIAL seam
    reflection is typed as the NAMED OPEN CHECK RP-THETA-OPEN (no
    deployed theta; the check awaits one).  NOT a gate.
 M2 THE SCHUR ROUTE (the deep cross-connection).  Parent state:
    the deployed DIAGONAL kernel with a C6-invariant carrier-to-
    boundary coupling (the T-block of M1's parametrization, i.e.
    the vacuum blocks of A_int: V = A_int[C, B]):
        A_full = [[kappa A_CC, t V], [-t V^T, m J3]],
    frozen kappa = m = 1/2 (the same KMS-mixing scale on both
    sides; boundary invertible), t = 1/20 (validity PROVEN exactly:
    ||A_full|| <= max(kappa, m) + t * sqrt(lam_max(V V^T)) < 1 by
    the triangle inequality + exact eigenvalue).  Boundary
    elimination (Schur/Feshbach -- the SAME operation that creates
    the RH port):  C_eff = C_CC - C_CB C_BB^{-1} C_BC.  EXACT
    consequence (sympy rationals):
        A_eff = kappa A_CC + (t^2 m / (1 - m^2)) * S,
        S := V J3 V^T   (the boundary-mediated census matrix),
    plus the pure-boundary pseudo-inverse variant (C_BB^+ = C_BB
    for the deployed projection): A_eff+ = A_CC - (t^2/4) S (sign
    flip; report).  MEASURE exactly: the 10 carrier duad blocks of
    S (nonzero census, C6 covariance, unit decomposition a*I2 +
    b*J + traceless-sym, per-edge Pf4 signs vs canonical, {a,b}
    compatibility).  TYPED: SCHURMIX-GENERATES(census) /
    SCHURMIX-DIAGONAL.  If GENERATES: print the unified reading --
    on both fronts (RH port, Wick functor) the real correlation
    lives in the ELIMINATED boundary, not the bare bulk.
 M3 THE 15-SIGNATURE FREEZE (deliverable): the 15 block-correlation
    signatures of the best M1 candidate -- zero/nonzero pattern,
    canonical-unit coordinates and signs, per-edge Pf4 sign, C6
    orbit, q* class -- printed as a FROZEN prediction table (the
    reviewer's 'freeze before any simulation' demand): any physical
    seam state realizing the block functor must reproduce this
    pattern.
 C  CONTROLS (must fire; frozen fire rules):
    C1 PERMUTED ROLES (round-52 rule): conjugating pi by the
       carrier transposition (a, c) and lifting: the covariance of
       the M1 winner breaks (defect >= NZ_FLOOR); the wrong vacuum
       grading Gamma' does NOT commute with the deployed O16; the
       wrong vacuum Arf label breaks the message edge law on
       EXACTLY 8 of 15.
    C2 THE BARE DIAGONAL STATE: t = 0 (KMS of the uncoupled
       deployed kernel): 0/15 cross-blocks at the floor, all 15
       Wick monomials vanish (fails G3 + G5); Schur with t = 0:
       A_eff = kappa A_CC exactly, 0/10 carrier cross-blocks.

FROZEN NUMERICAL PROTOCOL (the ONLY non-exact step is the
transcendental KMS map): exact integer / sympy rational arithmetic
in every structural decision (commutant walks, orbit census,
grading wiring, the ENTIRE M2 route, controls C1-wiring/C2-Schur);
the KMS map is evaluated by certified-precision mpmath at DPS =
60 via the exact hermitian eigendecomposition of K = i h (C_beta
= Q diag(1/(1 + e^{beta lam})) Q^H -- no large-exponential loss),
with the FROZEN two-sided decision thresholds: a quantity is
NONZERO iff |x| >= NZ_FLOOR = 1e-8, ZERO iff |x| <= ZTOL = 1e-40
(structural zeros and exact identities land < ~1e-58 at 60
digits; genuine grid values are >= ~1e-6); any decided quantity
in the open gap fires K2 (ambiguous -- the honest failure).  Pf4
nonzero floor PF_FLOOR = 1e-16 (quadratic in block scale); Wick
monomial floor PF_FLOOR^3.  No RNG, no fits.

KILLS (any one fires => typed gap):
  K0 AST firewall / setup ward breaks              -> PIPELINE-BROKEN
  K1 commutant walk / isotypic ward incoherent     -> COMMUTANT-BROKEN
  K2 KMS route ward breaks (realness, antisymmetry,
     covariance, CAR, threshold ambiguity)         -> KMSROUTE-BROKEN
  K3 Schur route exact algebra breaks              -> SCHURROUTE-BROKEN
  K5 freeze table incoherent with the winner       -> FREEZE-BROKEN
  K7 a control does not fire                       -> CONTROL-DEAD

VERDICT (frozen enum): KMSMIX-MEASURED [typed KMSMIX-FOUND(params)
/ KMSMIX-OBSTRUCTED(<gates>), SCHURMIX-GENERATES(<census>) /
SCHURMIX-DIAGONAL, RP-THETA-OPEN / RP-TESTED(<theta>)] (no kills;
honest OBSTRUCTED / DIAGONAL are first-class outcomes) /
KMSMIX-PARTIAL [kill tokens] / PIPELINE-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  AST firewall: banned identifiers
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime (self-scan).  NO physics-realization claim: the [O]
premise (the boundary grammar IS a self-hosting Wick pair
compiler) stays [O]; this probe constructs CANDIDATE states and
freezes signatures -- whether the ACTUAL seam realizes any of them
is untouched; no marker moves.

SPEC v2 AMENDMENTS (fail-first preserved): none at freeze; any
post-run amendment is documented here with the fail-first output
preserved.  (Frozen expectations pre-derived by hand and cross-
checked against an independent scratch derivation of the walk
counts (52 + 10 orbits, 2 forced), the isotypic mults
[10,0,2,2,2,0], the exact Schur identity, and lam_max(V V^T) = 15
BEFORE the freeze; the probe re-measures all of them.)

Sources (read-only, machinery rebuilt inline): wick_block_functor_
probe (round 52: 16-dim layout, O16, A_int frozen rule, Gamma16,
chi/qsign/sgn, Iota/3 compression, FLOOR), wick_mixing_covariance_
probe (round 51: CAR conventions, orbit walk), v113 (Majorana CAR,
JW kernel, A16 hull), v155/v160 (RP premise census), v424/v426/
v440 (the deployed KMS/RP dictionary; 8-dim collar), v880/v888
(q*, duads, phi), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/kms_schur_mixing_probe.py
"""

import ast
import hashlib
import itertools
import os
import sys
import time

import mpmath as mp
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

FLOOR = sp.Rational(1, 200)          # round-51/52 frozen floor (G_c)
DPS = 60                             # certified precision (frozen)
NZ_FLOOR = mp.mpf("1e-8")            # nonzero decision floor (frozen)
ZTOL = mp.mpf("1e-40")               # zero decision ceiling (frozen)
PF_FLOOR = mp.mpf("1e-16")           # Pf4 nonzero floor (frozen)

mp.mp.dps = DPS


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
# (v880 / v888 conventions rebuilt inline; family/anchor basis)
def pc(v):
    return bin(v).count("1")


HT = [[(pc(v) * pc(w) - pc(v & w)) % 2 for w in range(16)]
      for v in range(16)]
A_BIT = 0b1000
FSIG = 0b0111
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


IOTA_MSG = [iota_bits(v) for v in range(16)]


def iota_support(v):
    return frozenset(i + 1 for i, bit in enumerate(IOTA_MSG[v])
                     if bit)


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


def fro2(M):
    """exact squared Frobenius norm of a sympy matrix."""
    return sum(x * x for x in M)


def edge_orbits(perm):
    """orbits of perm on the 15 unordered duads of {0..5}, each
    with the ORIENTATION-REVERSAL flag (round-51 convention)."""
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


def pf_of(mat, idx):
    """recursive Pfaffian expansion (sympy)."""
    if not idx:
        return sp.Integer(1)
    i0, rest0 = idx[0], idx[1:]
    tot = sp.Integer(0)
    for k, j in enumerate(rest0):
        sub = [t for t in rest0 if t != j]
        tot += sp.Integer(-1) ** k * mat[i0, j] * pf_of(mat, sub)
    return tot


def pf_num(rows, idx):
    """Pfaffian of an mp-float matrix (list of lists) on idx, with
    exact-zero skip (the restricted matrices are sparse by
    construction)."""
    memo = {}

    def rec(t):
        if not t:
            return mp.mpf(1)
        if t in memo:
            return memo[t]
        i0, rest = t[0], t[1:]
        tot = mp.mpf(0)
        for k, j in enumerate(rest):
            aij = rows[i0][j]
            if aij != 0:
                sub = tuple(x for x in rest if x != j)
                tot += (-1) ** k * aij * rec(sub)
        memo[t] = tot
        return tot

    return rec(tuple(sorted(idx)))


DUADS_CH = sorted(itertools.combinations(range(6), 2))
J2 = sp.Matrix([[0, 1], [-1, 0]])
I2 = sp.eye(2)
IOTA6 = sp.Matrix.vstack(I2, I2, I2)   # the frozen 6x2 compression


def sp_to_mp(M):
    """sympy rational matrix -> nested list of mpf (exact)."""
    r, c = M.shape
    return [[mp.mpf(int(M[i, j].p)) / mp.mpf(int(M[i, j].q))
             if M[i, j] != 0 else mp.mpf(0)
             for j in range(c)] for i in range(r)]


def main():
    print("SEAM.CFIN.KMSMIX.01 + SEAM.CFIN.SCHURMIX.01 -- the "
          "channel-mixing STATE (KMS + Schur routes)")
    print("FROZEN_SPEC SHA-256: %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("NO physics-realization claim; the [O] premise stays "
          "[O]; exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (corpus rebuilt)")
    # ==================================================================
    bad = ast_scan(BANNED_IDS)
    check("S0.0 AST firewall: no banned identifiers %s"
          % (BANNED_IDS,), not bad, kill="K0")

    refs = [polar_shift(c) for c in range(16)]
    ok_ref = all(
        all(q[x ^ y] ^ q[x] ^ q[y] == HT[x][y]
            for x in range(16) for y in range(16)) for q in refs)
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    siginv = [q for q in refs
              if all(q[SIGP[v]] == q[v] for v in range(16))]
    cand = [q for q in siginv if q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique "
          "q* under the frozen selector",
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
    check("S0.2 duad model: 15 messages <-> 15 duads; vacuum label "
          "V0 = %d" % V0, biject and 0 <= V0 < 6, kill="K0")

    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5
               and set(phi.values()) == set(range(1, 6)))
    check("S0.3 carrier dictionary phi (ovoid-induced) bijective: "
          "%s" % (sorted(phi.items()),), ok_phi, kill="K0")

    def lab(j):
        return 0 if j == V0 else phi[j]

    def chduad(v):
        return frozenset(lab(j) for j in dmap[v])

    chd = {v: chduad(v) for v in NZ}
    inv_chd = {frozenset(d): v for v, d in chd.items()}
    check("S0.4 the 15 messages map bijectively onto the 15 "
          "channel duads (V0 -> channel 0)",
          sorted(chd.values(), key=sorted) == DUADS_L, kill="K0")

    # deployed C6: Sp(4,2) census + Aut pin (rounds 50-52 rebuilt)
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
    check("S0.5 |GL(4,2)| = %d == 20160, |Sp(4,2)| = %d == 720, "
          "|Aut(C_fin)| = %d == 6, generator pin g^2 = sigma unique"
          % (gl_n, len(SP6), len(AUT)),
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
    ct6 = cycle_type(PI6)
    ok_int = all(dmap[GEN[v]] == frozenset(pia[j] for j in dmap[v])
                 for v in NZ)
    check("S0.6 DEPLOYED channel permutation pi = %s: fixes "
          "channel 0, cycle type %s == (1, 2, 3); intertwines the "
          "duad action on all 15" % (PI6, ct6),
          PI6[0] == 0 and ct6 == (1, 2, 3) and ok_int, kill="K0")

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
    THREE = next(c for c in cycles if len(c) == 3)
    a_ch, b_ch = TWO
    c_ch = THREE[0]
    print("      pi cycles: fixed 0, 2-cycle %s, 3-cycle %s"
          % (TWO, sorted(THREE)))
    chi = {i: (-1) ** (i + 1) for i in range(1, 6)}

    # deployed one-particle layout + the round-50 lift O16
    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    dims = {i: len(CH[i]) for i in CH}
    CAR_IDX = list(range(10))
    BND_IDX = list(range(10, 16))

    def lift16(perm6):
        O = sp.zeros(16)
        for r in CH[0]:
            O[r, r] = 1
        for i in range(1, 6):
            src, dst = CH[i], CH[perm6[i]]
            O[dst[0], src[0]] = 1
            O[dst[1], src[1]] = 1
        return O

    O16 = lift16(PI6)
    # image map: index s in channel i, position k -> CH[pi(i)][k]
    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]
    check("S0.7 deployed lift O16 orthogonal integer (slot pairs "
          "as units, identity on the A3 block)",
          sp.simplify(O16 * O16.T) == sp.eye(16), kill="K0")

    # the round-52 canonical integer covariant cross matrix A_int
    orbs = edge_orbits(PI6)

    def put_ordered(A, x, y, B):
        for r in range(len(CH[x])):
            for c in range(len(CH[y])):
                A[CH[x][r], CH[y][c]] = B[r, c]
                A[CH[y][c], CH[x][r]] = -B[r, c]

    A_int = sp.zeros(16)
    for edges, rev, rep in orbs:
        i, j = rep
        if rev:
            B = J2
        elif i == 0:
            B = IOTA6
        else:
            B = I2
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    ok_aint = (sp.simplify(O16 * A_int * O16.T - A_int)
               == sp.zeros(16)
               and sp.simplify(A_int + A_int.T) == sp.zeros(16))
    check("S0.8 round-52 canonical A_int rebuilt: integer, "
          "antisymmetric, O16-covariant EXACTLY; the canonical "
          "candidate G_c = (I + i FLOOR A_int)/2",
          ok_aint, kill="K0")

    # deployed diagonal kernel A16_dep = (+)_8 J (v113/v155 hull)
    A16_dep = sp.zeros(16)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    ok_dep = (sp.simplify(O16 * A16_dep * O16.T - A16_dep)
              == sp.zeros(16)
              and sp.simplify(A16_dep * A16_dep + sp.eye(16))
              == sp.zeros(16))
    n_dep_cross = sum(
        1 for (i, j) in DUADS_CH
        if fro2(A16_dep.extract(CH[i], CH[j])) != 0)
    check("S0.9 deployed diagonal kernel A16_dep = (+)_8 J: "
          "covariant, A^2 = -I (pure), cross-blocks %d/15 == 0 "
          "(SEAM-DIAGONAL, round 52)" % n_dep_cross,
          ok_dep and n_dep_cross == 0, kill="K0")

    Gamma16 = sp.diag(*([-1] * 10 + [1] * 6))
    ok_gp = (sp.simplify(Gamma16 * O16 - O16 * Gamma16)
             == sp.zeros(16))
    edge_law = all((QSTAR[v] == 0) == (0 in chd[v]) for v in NZ)
    check("S0.10 grading operator Gamma16 = (-I on C) (+) (+I on "
          "B): [Gamma16, O16] == 0 (%s); edge law q*(v)=0 iff duad "
          "touches channel 0 on all 15 (%s)" % (ok_gp, edge_law),
          ok_gp and edge_law, kill="K0")

    vac_duads = {frozenset(chd[v]) for v in NZ if QSTAR[v] == 0}
    car_duads = {frozenset(chd[v]) for v in NZ if QSTAR[v] == 1}

    # canonical chi / qsign / sgn(M) machinery (round 49/52)
    SYM = {}
    for i in range(6):
        for j in range(i + 1, 6):
            SYM[(i, j)] = sp.Symbol("a_%d%d" % (i, j))
    G6 = sp.Matrix(6, 6, lambda r, c:
                   SYM[(r, c)] if r < c
                   else (-SYM[(c, r)] if r > c else 0))
    PF6 = sp.expand(pf_of(G6, list(range(6))))
    cdict = PF6.as_coefficients_dict()
    MSLOT = all_matchings(range(6))

    def mono_of(m):
        out = sp.Integer(1)
        for e in m:
            out *= SYM[tuple(sorted(e))]
        return out

    sgn = {}
    ok_c = True
    for m in MSLOT:
        c = cdict.get(mono_of(m), 0)
        ok_c &= (c in (1, -1))
        sgn[frozenset(m)] = int(c)

    def m_ist(m):
        vac_e = next(e for e in m if 0 in e)
        i = next(iter(vac_e - {0}))
        S, T = sorted((tuple(sorted(e)) for e in m if e != vac_e))
        return i, S, T

    def qsign(i, S, T):
        j, k, l, m4 = sorted(set(range(1, 6)) - {i})
        three = [frozenset({frozenset({j, k}), frozenset({l, m4})}),
                 frozenset({frozenset({j, l}), frozenset({k, m4})}),
                 frozenset({frozenset({j, m4}), frozenset({k, l})})]
        key = frozenset({frozenset(S), frozenset(T)})
        return (1, -1, 1)[three.index(key)]

    ok_gauge = all(
        sgn[frozenset(m)]
        == chi[m_ist(m)[0]] * qsign(*m_ist(m)) for m in MSLOT)
    check("S0.11 symbolic scalar ward: Pf(6x6 generic) = 15 "
          "monomials, sgn(M) == chi(i) * qsign(S,T), chi(i) = "
          "(-1)^(i+1) (round-49 gauge)",
          len(cdict) == 15 and ok_c and ok_gauge, kill="K0")

    # canonical reference sign pattern (exact, from G_c = FLOOR A_int)
    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}

    def compress12(A16m):
        """Iota/3 compression: 16-dim covariant -> 12-dim block
        matrix (sympy)."""
        Ahat = sp.zeros(12)
        for (i, j) in DUADS_CH:
            if i == 0:
                B = (IOTA6.T * A16m.extract(CH[0], CH[j])) / 3
            else:
                B = A16m.extract(CH[i], CH[j])
            for r in range(2):
                for c in range(2):
                    Ahat[CH2[i][r], CH2[j][c]] = B[r, c]
                    Ahat[CH2[j][c], CH2[i][r]] = -B[r, c]
        return Ahat

    Ahat_c = compress12(FLOOR * A_int)
    pf4_c = {}
    for (i, j) in DUADS_CH:
        Bh = Ahat_c.extract(CH2[i], CH2[j])
        pf4_c[frozenset({i, j})] = -Bh.det()
    wblk_c = {}
    for m in MSLOT:
        prod = sp.Integer(1)
        for e in m:
            prod *= pf4_c[frozenset(e)]
        wblk_c[frozenset(m)] = sgn[frozenset(m)] * prod
    ok_ref15 = (all(v != 0 for v in pf4_c.values())
                and all(v != 0 for v in wblk_c.values()))
    check("S0.12 canonical reference pattern (exact): all 15 Pf4 "
          "and all 15 w_blk of G_c nonzero (the round-52 chi "
          "structure rebuilt)", ok_ref15, kill="K0")

    # ==================================================================
    section("H1 -- THE COMMUTANT (hermitian side; exact orbit "
            "walks)")
    # ==================================================================
    # signed walk on unordered index pairs (r < c): antisymmetric
    # covariant dimension = orientation-consistent orbits; forced
    # zeros = reversal-forced orbits.
    all_pairs = [(r, c) for r in range(16) for c in range(r + 1, 16)]
    visited = set()
    n_anti_free = 0
    n_anti_forced = 0
    forced_reps = []
    n_pair_orbits = 0
    for p0 in all_pairs:
        if p0 in visited:
            continue
        n_pair_orbits += 1
        orb = {}
        cur, s = p0, 1
        forcedq = False
        while True:
            if cur in orb:
                if orb[cur] != s:
                    forcedq = True
                break
            orb[cur] = s
            r, c = img[cur[0]], img[cur[1]]
            if r > c:
                r, c, s = c, r, -s
            cur = (r, c)
        visited |= set(orb)
        if forcedq:
            n_anti_forced += 1
            forced_reps.append(p0)
        else:
            n_anti_free += 1
    # symmetric side: unordered-pair orbits (no sign obstruction)
    # + diagonal orbits
    diag_orbits = 0
    seen_d = set()
    for r in range(16):
        if r in seen_d:
            continue
        diag_orbits += 1
        x = r
        while x not in seen_d:
            seen_d.add(x)
            x = img[x]
    dim_anti = n_anti_free
    dim_sym = n_pair_orbits + diag_orbits
    dim_herm = dim_sym + dim_anti
    # isotypic ward: fix counts of O16 powers -> sum of mult^2
    fixs = []
    pk = tuple(range(6))
    for _k in range(6):
        fixs.append(6 + 2 * sum(1 for i in range(1, 6)
                                if pk[i] == i))
        pk = compose(PI6, pk)
    zeta = sp.exp(2 * sp.pi * sp.I / 6)
    mults = [sp.nsimplify(sp.simplify(
        sp.Rational(1, 6) * sum(fixs[k] * zeta ** (-j * k)
                                for k in range(6))))
        for j in range(6)]
    sum_sq = sum(m ** 2 for m in mults)
    check("H1.1 HERMITIAN-SIDE COMMUTANT of O16 (exact walks): "
          "dim = %d = %d sym + %d antisym; isotypic mults %s, "
          "sum m^2 = %s == dim (ward); the Majorana-compatible "
          "slice K = i h is the %d-dim antisymmetric part"
          % (dim_herm, dim_sym, dim_anti, mults, sum_sq, dim_anti),
          sum_sq == dim_herm and sum(mults) == 16, kill="K1")

    # cross / diagonal split of the antisymmetric side
    ch_of = {}
    for i in range(6):
        for s in CH[i]:
            ch_of[s] = i
    visited2 = set()
    n_cross_free = 0
    n_diag_free = 0
    for p0 in all_pairs:
        if p0 in visited2:
            continue
        orb = {}
        cur, s = p0, 1
        forcedq = False
        while True:
            if cur in orb:
                if orb[cur] != s:
                    forcedq = True
                break
            orb[cur] = s
            r, c = img[cur[0]], img[cur[1]]
            if r > c:
                r, c, s = c, r, -s
            cur = (r, c)
        visited2 |= set(orb)
        if not forcedq:
            if ch_of[p0[0]] != ch_of[p0[1]]:
                n_cross_free += 1
            else:
                n_diag_free += 1
    check("H1.2 antisymmetric split: cross-block (mixing) part = "
          "%d == 33 (the round-52 covariant block space; the "
          "C<->B mixing block T spans the 2 vacuum orbits, dim "
          "12 + 12 = 24), channel-diagonal part = %d (A3 antisym "
          "15 + slot-orbit J's 2); forced-zero orbits = %d == 2 "
          "(the diagonal of the transposed {%d,%d} block)"
          % (n_cross_free, n_diag_free, n_anti_forced, a_ch, b_ch),
          n_cross_free == 33 and n_diag_free == 17
          and n_anti_forced == 2
          and dim_anti == n_cross_free + n_diag_free, kill="K1")

    # ==================================================================
    section("M1 -- THE KMS ROUTE (frozen grid scan, beta = 1)")
    # ==================================================================
    O16_mp = sp_to_mp(O16)
    Aint_mp = sp_to_mp(A_int)
    Adep_mp = sp_to_mp(A16_dep)
    IOTA_mp = sp_to_mp(IOTA6)

    def kms_C(h_mp, beta):
        """C_beta = (I + e^{beta K})^{-1} for K = i h (h real
        antisymmetric, mp rows), via the exact hermitian
        eigendecomposition (certified mpmath at DPS digits).
        Returns C as nested mpc lists."""
        K = mp.matrix(16, 16)
        for r in range(16):
            for c in range(16):
                if h_mp[r][c] != 0:
                    K[r, c] = mp.mpc(0, h_mp[r][c])
        Ev, Q = mp.eighe(K)
        f = [1 / (1 + mp.e ** (mp.mpf(beta) * Ev[k]))
             for k in range(16)]
        return [[sum(Q[r, k] * f[k] * mp.conj(Q[c, k])
                     for k in range(16)) for c in range(16)]
                for r in range(16)]

    def kms_A_from_h(h_mp, beta):
        """A_beta = -i (2 C_beta - I) = -tan(beta h / 2); returns
        (A rows, wards dict)."""
        C = kms_C(h_mp, beta)
        A = [[mp.mpf(0)] * 16 for _ in range(16)]
        im_max = mp.mpf(0)
        for r in range(16):
            for c in range(16):
                z = -1j * (2 * C[r][c] - (1 if r == c else 0))
                im_max = max(im_max, abs(mp.im(z)))
                A[r][c] = mp.re(z)
        anti = max(abs(A[r][c] + A[c][r])
                   for r in range(16) for c in range(16))
        cov = max(abs(A[img[r]][img[c]] - A[r][c])
                  for r in range(16) for c in range(16))
        H = mp.matrix(16, 16)
        for r in range(16):
            for c in range(16):
                H[r, c] = mp.mpc(0, A[r][c])
        ev = mp.eighe(H, eigvals_only=True)
        smax = max(abs(x) for x in ev)
        return A, {"im": im_max, "anti": anti, "cov": cov,
                   "smax": smax}

    def h_grid(u, t):
        """frozen family h(u, t) = -(u A16_dep + t A_int), mp."""
        uf = (mp.mpf(int(sp.Rational(u).p))
              / int(sp.Rational(u).q))
        tf = (mp.mpf(int(sp.Rational(t).p))
              / int(sp.Rational(t).q))
        return [[-(uf * Adep_mp[r][c] + tf * Aint_mp[r][c])
                 for c in range(16)] for r in range(16)]

    def blocks_census(A):
        """per-duad Frobenius norms of the mp matrix A."""
        out = {}
        for (i, j) in DUADS_CH:
            s = mp.mpf(0)
            for r in CH[i]:
                for c in CH[j]:
                    s += A[r][c] ** 2
            out[(i, j)] = mp.sqrt(s)
        return out

    def compress_mp(A):
        """Iota/3 compression of an mp 16-dim covariant matrix."""
        Ahat = [[mp.mpf(0)] * 12 for _ in range(12)]
        for (i, j) in DUADS_CH:
            if i == 0:
                B = [[sum(IOTA_mp[r][rr] * A[CH[0][r]][CH[j][c]]
                          for r in range(6)) / 3
                      for c in range(2)] for rr in range(2)]
            else:
                B = [[A[CH[i][r]][CH[j][c]] for c in range(2)]
                     for r in range(2)]
            for r in range(2):
                for c in range(2):
                    Ahat[CH2[i][r]][CH2[j][c]] = B[r][c]
                    Ahat[CH2[j][c]][CH2[i][r]] = -B[r][c]
        return Ahat

    def gates(A, wards):
        """evaluate the frozen gates G1..G5 on an mp candidate;
        returns (passed set, failed list, diagnostics)."""
        diag = {}
        failed = []
        # G1 CAR strict
        if not (wards["smax"] < 1 - mp.mpf("1e-6")):
            failed.append("G1-CAR")
        # G2 covariance + forced zeros ({a,b} block diagonal)
        if not (wards["im"] < ZTOL and wards["anti"] < ZTOL
                and wards["cov"] < ZTOL):
            failed.append("G2-COVARIANCE")
        fz = max(abs(A[CH[a_ch][k]][CH[b_ch][k]]) for k in range(2))
        if not (fz < ZTOL):
            failed.append("G2-FORCEDZERO")
        # G3 floor census (with ambiguity band -> K2)
        bn = blocks_census(A)
        n_floor = sum(1 for v in bn.values() if v >= NZ_FLOOR)
        ambig = [d for d, v in bn.items() if ZTOL < v < NZ_FLOOR]
        diag["blocks"] = bn
        diag["ambig"] = ambig
        if n_floor != 15:
            failed.append("G3-FLOOR(%d/15)" % n_floor)
        # G4 grading fullness (odd = vacuum, even = carrier)
        odd_ok, even_ok, parity_ok = 0, 0, True
        for (i, j) in DUADS_CH:
            so, se = mp.mpf(0), mp.mpf(0)
            gi = -1 if i != 0 else 1
            gj = -1 if j != 0 else 1
            for r in CH[i]:
                for c in CH[j]:
                    o = (A[r][c] - gi * gj * A[r][c]) / 2
                    e = (A[r][c] + gi * gj * A[r][c]) / 2
                    so += o ** 2
                    se += e ** 2
            if 0 in (i, j):
                odd_ok += bool(mp.sqrt(so) >= NZ_FLOOR)
                parity_ok &= bool(mp.sqrt(se) < ZTOL)
            else:
                even_ok += bool(mp.sqrt(se) >= NZ_FLOOR)
                parity_ok &= bool(mp.sqrt(so) < ZTOL)
        diag["grading"] = (odd_ok, even_ok)
        if not (odd_ok == 5 and even_ok == 10 and parity_ok):
            failed.append("G4-GRADING(%d/5,%d/10)"
                          % (odd_ok, even_ok))
        # G5 Pfaffian / chi structure + sign match to canonical
        Ahat = compress_mp(A)
        pf4 = {}
        for (i, j) in DUADS_CH:
            B = [[Ahat[CH2[i][r]][CH2[j][c]] for c in range(2)]
                 for r in range(2)]
            pf4[frozenset({i, j})] = -(B[0][0] * B[1][1]
                                       - B[0][1] * B[1][0])
        diag["pf4"] = pf4
        n_pf4 = sum(1 for v in pf4.values() if abs(v) >= PF_FLOOR)
        wb = {}
        ok_sign, ok_ward, n_wb = True, True, 0
        for m in MSLOT:
            prod = mp.mpf(1)
            for e in m:
                prod *= pf4[frozenset(e)]
            w = sgn[frozenset(m)] * prod
            wb[frozenset(m)] = w
            if abs(w) >= PF_FLOOR ** 3:
                n_wb += 1
            # interleaving ward Pf(Ahat|_M) == prod Pf4
            X = [[mp.mpf(0)] * 12 for _ in range(12)]
            for e in m:
                i, j = sorted(e)
                for r in range(2):
                    for c in range(2):
                        X[CH2[i][r]][CH2[j][c]] = \
                            Ahat[CH2[i][r]][CH2[j][c]]
                        X[CH2[j][c]][CH2[i][r]] = \
                            -Ahat[CH2[i][r]][CH2[j][c]]
            pfm = pf_num(X, range(12))
            ok_ward &= bool(abs(pfm - prod)
                            <= mp.mpf("1e-30") * (1 + abs(prod)))
            ok_sign &= bool((w > 0)
                            == (wblk_c[frozenset(m)] > 0))
        diag["wblk"] = wb
        if not (n_pf4 == 15 and n_wb == 15 and ok_ward
                and ok_sign):
            failed.append("G5-CHI(pf4 %d/15, wb %d/15, ward %s, "
                          "signmatch %s)"
                          % (n_pf4, n_wb, ok_ward, ok_sign))
        if ambig:
            failed.append("G-AMBIGUOUS%s" % ambig)
        return failed, diag

    SCAN = [(sp.Integer(1), sp.Rational(1, 8)),
            (sp.Integer(1), sp.Rational(1, 4)),
            (sp.Integer(1), sp.Rational(1, 2)),
            (sp.Integer(1), sp.Integer(1)),
            (sp.Integer(0), sp.Rational(1, 4))]
    winner = None
    win_data = None
    scan_rows = []
    for (u, t) in SCAN:
        A, wards = kms_A_from_h(h_grid(u, t), 1)
        failed, diag = gates(A, wards)
        scan_rows.append(((u, t), failed))
        print("      grid (u=%s, t=%s, beta=1): smax=%s  %s"
              % (u, t, mp.nstr(wards["smax"], 8),
                 "PASS all gates" if not failed
                 else "fails %s" % failed))
        if not failed and winner is None:
            winner = (u, t)
            win_data = (A, wards, diag)
    ok_amb = all("G-AMBIGUOUS" not in " ".join(f)
                 for _p, f in scan_rows)
    check("M1.1 frozen grid scan complete (%d points, frozen "
          "order); no threshold ambiguity fired"
          % len(SCAN), ok_amb, kill="K2")

    if winner is not None:
        t_m1 = "KMSMIX-FOUND(u=%s, t=%s, beta=1)" % winner
    else:
        t_m1 = "KMSMIX-OBSTRUCTED(%s)" % (
            "; ".join("(u=%s,t=%s):%s" % (p[0], p[1], f)
                      for p, f in scan_rows))
    check("M1.2 TYPED KMS OUTCOME: %s -- the KMS state of a "
          "C6-invariant mixing Hamiltonian %s the full round-52 "
          "block structure (all 15 blocks at the floor, grading "
          "5/5 + 10/10, all 15 Wick monomials with the canonical "
          "sign pattern)"
          % (t_m1, "CARRIES" if winner else "does NOT carry"),
          winner is not None or "OBSTRUCTED" in t_m1,
          "typed by measurement", kill="K2")

    beta2_note = "not evaluated"
    if winner is not None:
        A2m, wards2 = kms_A_from_h(h_grid(*winner), 2)
        failed2, _diag2 = gates(A2m, wards2)
        beta2_note = ("PASSES all gates" if not failed2
                      else "fails %s" % failed2)
        check("M1.3 ROBUSTNESS at beta = 2 (winner re-tested): %s"
              % beta2_note, not failed2,
              "report-grade robustness", kill=None)

    # anatomy: per-orbit rays (report only)
    print("      ANATOMY (report): per-orbit rays h = -(A16_dep + "
          "1/4 E_orb) -- duads LIT (>= floor) vs duads SEEDED:")
    for edges, rev, rep in orbs:
        E_orb = sp.zeros(16)
        i, j = rep
        B = J2 if rev else (IOTA6 if i == 0 else I2)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(E_orb, x, y, B)
            x, y = PI6[x], PI6[y]
        Er = sp_to_mp(E_orb)
        tf = mp.mpf(1) / 4
        h_ray = [[-(Adep_mp[r][c] + tf * Er[r][c])
                  for c in range(16)] for r in range(16)]
        Ar, _w = kms_A_from_h(h_ray, 1)
        bn = blocks_census(Ar)
        lit = sorted(d for d, v in bn.items() if v >= NZ_FLOOR)
        seeded = sorted(tuple(sorted(e)) for e in edges)
        print("        orbit rep %s (size %d%s): seeded %s -> lit "
              "%d/15 %s"
              % (rep, len(edges), ", reversed" if rev else "",
                 seeded, len(lit), lit))
    check("M1.4 anatomy printed: the tan/KMS dressing itself "
          "MIXES -- odd powers of h generate blocks outside the "
          "seeded orbit (the Schur mechanism operating inside the "
          "KMS route); report only", True, "no decision")

    # ==================================================================
    section("R1 -- REFLECTION POSITIVITY (the honest typed answer)")
    # ==================================================================
    check("R1.1 CORPUS ANSWER (measured by reading, frozen): NO "
          "canonical spatial/OS reflection theta is deployed on "
          "the 16-dim one-particle space -- v155 carries RP only "
          "as the recorded [P] premise (no operator), v160 has no "
          "reflection operator, v424/v426/v440 deploy the "
          "dictionary (Theta K Theta = -K, Theta C_beta Theta = "
          "I - C_beta) on an 8-dim COLLAR TOY (4 marks x 2 "
          "sides), not on D5+A3", True, "typed, honest")
    if winner is not None:
        # Theta_0 = complex conjugation in the Majorana basis:
        # Theta_0 K Theta_0 = conj(K) = -K exact-structural for
        # K = i h, h real -- measured via conj(C_beta) = I - C_beta.
        C = kms_C(h_grid(*winner), 1)
        d_refl = mp.mpf(0)
        for r in range(16):
            for c in range(16):
                tgt = (1 if r == c else 0) - C[r][c]
                d_refl = max(d_refl, abs(mp.conj(C[r][c]) - tgt))
        ok_o16 = True   # conjugation commutes with real O16
        check("R1.2 THE MAJORANA REAL STRUCTURE Theta_0 (antiunitary "
              "conjugation in the deployed basis, commutes with "
              "O16 and Gamma16): satisfies the deployed v426/v440 "
              "dictionary AUTOMATICALLY -- Theta_0 K Theta_0 = "
              "conj(K) = -K (BW form, structural for K = i h, h "
              "real) and conj(C_beta) = I - C_beta measured on the "
              "winner (defect %s < ZTOL)"
              % mp.nstr(d_refl, 6),
              ok_o16 and d_refl < ZTOL, kill="K2")
    check("R1.3 NAMED OPEN CHECK -- RP-THETA-OPEN: Theta_0 is the "
          "Majorana real structure (particle-hole), NOT a spatial "
          "seam reflection; the OS-positivity of the two-point "
          "block under a SPATIAL theta (the Hankel/reflection "
          "Gram of v379-type) cannot be tested until a theta is "
          "deployed on the 16-dim space -- typed as the named "
          "open check, NOT a gate; no marker moves", True,
          "typed open")
    t_rp = "RP-THETA-OPEN"

    # ==================================================================
    section("M2 -- THE SCHUR ROUTE (exact; boundary elimination)")
    # ==================================================================
    # parent state: deployed diagonal + C6-invariant C<->B coupling
    kap = sp.Rational(1, 2)
    m_mix = sp.Rational(1, 2)
    t_cpl = sp.Rational(1, 20)
    A_CC = A16_dep.extract(CAR_IDX, CAR_IDX)
    J3 = A16_dep.extract(BND_IDX, BND_IDX)
    V = A_int.extract(CAR_IDX, BND_IDX)      # the T-block (vacuum)
    ok_cov_V = (sp.simplify(
        O16.extract(CAR_IDX, CAR_IDX) * V - V) == sp.zeros(10, 6))
    check("M2.1 the coupling T-block V = A_int[C, B] (the M1 "
          "parametrization's mixing block, vacuum orbits, dim 24 "
          "space; canonical element): O_C V = V (C6-invariant "
          "coupling, exact)", ok_cov_V, kill="K3")

    # validity of the parent state (exact triangle bound)
    VVt = V * V.T
    lam_max = max(VVt.eigenvals().keys(), key=lambda e: sp.N(e))
    norm_bound = sp.Rational(1, 2) + t_cpl * sp.sqrt(lam_max)
    check("M2.2 PARENT VALIDITY (exact): A_full = [[kappa A_CC, "
          "t V], [-t V^T, m J3]], kappa = m = 1/2, t = 1/20; "
          "||A_full|| <= max(kappa, m) + t sqrt(lam_max(V V^T)) = "
          "1/2 + (1/20) sqrt(%s) = %s < 1 EXACT => 0 < C_full < I "
          "=> the Schur complement C_eff is a valid covariance"
          % (lam_max, norm_bound),
          bool(norm_bound < 1), kill="K3")

    # exact Schur elimination:
    # C_eff = C_CC - C_CB C_BB^{-1} C_BC
    #       = (I + i kap A_CC)/2
    #         - (t^2/2)/(1-m^2) (V V^T - i m V J3 V^T)
    # antisym part: A_eff = kap A_CC + (t^2 m/(1-m^2)) S,
    # S = V J3 V^T  (derived in the docstring; verified here)
    S_mat = V * J3 * V.T
    C_BB = (sp.eye(6) + sp.I * m_mix * J3) / 2
    C_BB_inv = 2 * (sp.eye(6) - sp.I * m_mix * J3) / (1 - m_mix**2)
    ok_inv = sp.simplify(C_BB * C_BB_inv - sp.eye(6)) == sp.zeros(6)
    C_CC = (sp.eye(10) + sp.I * kap * A_CC) / 2
    C_CB = sp.I * t_cpl * V / 2
    C_BC = -sp.I * t_cpl * V.T / 2
    C_eff = sp.expand(C_CC - C_CB * C_BB_inv * C_BC)
    A_eff_formula = kap * A_CC + (t_cpl ** 2 * m_mix
                                  / (1 - m_mix ** 2)) * S_mat
    # C_eff = R + i A_eff/2, A_eff real antisymmetric
    A_eff = sp.Matrix(10, 10,
                      lambda r, c: sp.im(sp.expand(2 * C_eff[r, c])))
    ok_schur = (sp.simplify(A_eff - A_eff_formula) == sp.zeros(10)
                and sp.simplify(A_eff + A_eff.T) == sp.zeros(10))
    check("M2.3 EXACT SCHUR IDENTITY: the eliminated-boundary "
          "covariance C_eff = C_CC - C_CB C_BB^{-1} C_BC has "
          "antisymmetric (correlation) part A_eff = kappa A_CC + "
          "(t^2 m/(1-m^2)) V J3 V^T EXACTLY (%s); the census "
          "matrix is S := V J3 V^T"
          % ok_schur, ok_inv and ok_schur, kill="K3")

    ok_cov_S = (sp.simplify(
        O16.extract(CAR_IDX, CAR_IDX) * S_mat
        * O16.extract(CAR_IDX, CAR_IDX).T - S_mat)
        == sp.zeros(10))
    n_cross = 0
    print("      10-duad census of S = V J3 V^T (carrier duads; "
          "unit decomposition B = aI I2 + aJ J + sym-traceless):")
    unit_rows = {}
    for (i, j) in itertools.combinations(range(1, 6), 2):
        B = S_mat.extract(CH[i], CH[j])
        aI = (B[0, 0] + B[1, 1]) / 2
        aJ = (B[0, 1] - B[1, 0]) / 2
        aX = (B[0, 1] + B[1, 0]) / 2
        aZ = (B[0, 0] - B[1, 1]) / 2
        nz = fro2(B) != 0
        n_cross += bool(nz)
        unit_rows[(i, j)] = (aI, aJ, aX, aZ)
        v = inv_chd[frozenset({i, j})]
        print("        {%d,%d}  q*=%d  B = %s I2 + %s J + (X:%s, "
              "Z:%s)%s"
              % (i, j, QSTAR[v], aI, aJ, aX, aZ,
                 "" if nz else "  << ZERO"))
    ok_ab_unit = (unit_rows[(a_ch, b_ch)][0] == 0
                  and unit_rows[(a_ch, b_ch)][1] != 0)
    check("M2.4 SCHUR-GENERATION CENSUS (exact): %d/10 carrier "
          "cross-blocks NONZERO from the BARE diagonal state + "
          "C6-invariant coupling alone; S is C6-covariant (%s); "
          "the transposed {%d,%d} block is PURE J (I2 coord 0, J "
          "coord %s) -- exactly the direction covariance allows "
          "there" % (n_cross, ok_cov_S, a_ch, b_ch,
                     unit_rows[(a_ch, b_ch)][1]),
          n_cross == 10 and ok_cov_S and ok_ab_unit, kill="K3")

    # per-edge Pf4 signs of the dressed carrier object vs canonical
    lam_eff = t_cpl ** 2 * m_mix / (1 - m_mix ** 2)
    ok_pf_car = True
    for (i, j) in itertools.combinations(range(1, 6), 2):
        B = lam_eff * S_mat.extract(CH[i], CH[j])
        pf4 = -B.det()
        pf4_can = pf4_c[frozenset({i, j})]
        ok_pf_car &= (sp.sign(pf4) == sp.sign(pf4_can) != 0)
    t_m2 = ("SCHURMIX-GENERATES(10/10 carrier duads, C6-covariant,"
            " J-direction, Pf4 signs canonical)"
            if n_cross == 10 and ok_cov_S else "SCHURMIX-DIAGONAL")
    check("M2.5 TYPED SCHUR OUTCOME: %s -- per-edge Pf4 = "
          "-det(block) signs MATCH the canonical G_c on all 10 "
          "carrier duads (%s); the pseudo-inverse (pure-boundary "
          "C_BB^+ = C_BB) variant gives A_eff+ = A_CC - (t^2/4) S "
          "-- same census, OPPOSITE dressing sign (report)"
          % (t_m2, ok_pf_car),
          t_m2.startswith("SCHURMIX-") and ok_pf_car, kill="K3")

    if t_m2.startswith("SCHURMIX-GENERATES"):
        print("""      THE UNIFIED READING (the reviewer's cross-connection
      made concrete): the SAME Schur/Feshbach elimination that
      creates the RH port (dressing by the eliminated block's
      resolvent) here creates the carrier channel mixing: the
      bare carrier state is EXACTLY diagonal (round 52,
      SEAM-DIAGONAL), the bare boundary state is diagonal, and
      the C6-invariant carrier-boundary coupling alone -- after
      the boundary is ELIMINATED -- deposits nonzero correlation
      on ALL 10 carrier duads with the covariant J-structure and
      the canonical Pf4 signs.  On both fronts the real
      correlation lives in the ELIMINATED boundary, not the bare
      bulk.""")

    # ==================================================================
    section("M3 -- THE 15-SIGNATURE FREEZE (frozen prediction "
            "table)")
    # ==================================================================
    if winner is not None:
        A, wards, diag = win_data
        bn = diag["blocks"]
        pf4 = diag["pf4"]
        orb_of = {}
        for oi, (edges, rev, rep) in enumerate(orbs):
            for e in edges:
                orb_of[frozenset(e)] = (oi, len(edges), rev)
        print("      FROZEN 15-SIGNATURE PREDICTION TABLE (best "
              "candidate: KMS %s; any physical seam state "
              "realizing the block functor must reproduce the "
              "zero/nonzero + sign pattern):" % (t_m1,))
        print("        duad  class q* orbit(size)  ||B||_F"
              "        unit-coords (sign)         sign Pf4")
        ok_tab = True
        for (i, j) in DUADS_CH:
            v = inv_chd[frozenset({i, j})]
            oi, osz, orev = orb_of[frozenset({i, j})]
            if i == 0:
                # coordinate along the frozen vacuum unit Iota
                coord = sum(IOTA_mp[r][rr] * A[CH[0][r]][CH[j][rr]]
                            for r in range(6)
                            for rr in range(2)) / 6
                coords = "Iota: %s" % mp.nstr(coord, 6)
                lead = coord
            else:
                B = [[A[CH[i][r]][CH[j][c]] for c in range(2)]
                     for r in range(2)]
                aI = (B[0][0] + B[1][1]) / 2
                aJ = (B[0][1] - B[1][0]) / 2
                coords = "I2: %s, J: %s" % (mp.nstr(aI, 6),
                                            mp.nstr(aJ, 6))
                lead = aJ if (i, j) == (a_ch, b_ch) else aI
            p4 = pf4[frozenset({i, j})]
            ok_tab &= bool(bn[(i, j)] >= NZ_FLOOR
                           and abs(p4) >= PF_FLOOR)
            print("        {%d,%d}  %s  %d  #%d(%d%s)  %s  [%s]  "
                  "lead %s  %s"
                  % (i, j, "vac" if 0 in (i, j) else "car",
                     QSTAR[v], oi, osz, "R" if orev else "",
                     mp.nstr(bn[(i, j)], 6), coords,
                     "+" if lead > 0 else "-",
                     "+" if p4 > 0 else "-"))
        check("M3.1 FREEZE: all 15 signatures nonzero with signs "
              "printed; coherent with the winner's gate data",
              ok_tab, kill="K5")
    else:
        check("M3.1 FREEZE: skipped -- no KMS candidate passed "
              "the gates (typed OBSTRUCTED above); the Schur-side "
              "10-duad census (M2.4) stands as the frozen partial "
              "signature", True, "typed", kill=None)

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    # C1 permuted roles (round-52 rule) on the M1 winner
    rho = list(range(6))
    rho[a_ch], rho[c_ch] = rho[c_ch], rho[a_ch]
    rho = tuple(rho)
    PIW = tuple(rho[PI6[rho[x]]] for x in range(6))
    O16w = lift16(PIW)
    imgw = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            imgw[s] = CH[PIW[i]][k]
    if winner is not None:
        A = win_data[0]
        defw = max(abs(A[imgw[r]][imgw[c]] - A[r][c])
                   for r in range(16) for c in range(16))
    else:
        Ac_mp = sp_to_mp(FLOOR * A_int)
        defw = max(abs(Ac_mp[imgw[r]][imgw[c]] - Ac_mp[r][c])
                   for r in range(16) for c in range(16))
    Gw = sp.diag(*[1 if r in CH[a_ch] else -1 for r in range(16)])
    gw = fro2(Gw * O16 - O16 * Gw)
    w_arf = next(j for j in range(6) if lab(j) == a_ch)
    mism = sum(1 for v in NZ
               if (QSTAR[v] == 0) != (w_arf in dmap[v]))
    check("C1 FIRES: PERMUTED ROLES (pi conjugated by the carrier "
          "transposition (%d, %d), lifted): covariance of the "
          "candidate breaks (max entry defect %s >= NZ_FLOOR); "
          "wrong vacuum grading Gamma' does NOT commute with the "
          "deployed O16 (||.||_F^2 = %s != 0); wrong vacuum Arf "
          "label breaks the edge law on EXACTLY %d == 8 of 15"
          % (a_ch, c_ch, mp.nstr(defw, 6), gw, mism),
          defw >= NZ_FLOOR and gw != 0 and mism == 8, kill="K7")

    # C2 the bare diagonal state (t = 0)
    A0, wards0 = kms_A_from_h(h_grid(1, 0), 1)
    bn0 = blocks_census(A0)
    n0 = sum(1 for v in bn0.values() if v >= NZ_FLOOR)
    Ahat0 = compress_mp(A0)
    n_pf0 = 0
    for (i, j) in DUADS_CH:
        B = [[Ahat0[CH2[i][r]][CH2[j][c]] for c in range(2)]
             for r in range(2)]
        p4 = -(B[0][0] * B[1][1] - B[0][1] * B[1][0])
        n_pf0 += bool(abs(p4) >= PF_FLOOR)
    A_eff0 = kap * A_CC       # exact Schur with t = 0
    n_s0 = sum(1 for (i, j) in itertools.combinations(range(1, 6), 2)
               if fro2(A_eff0.extract(CH[i], CH[j])) != 0)
    check("C2 FIRES: THE BARE DIAGONAL STATE (t = 0): KMS of the "
          "uncoupled deployed kernel has %d/15 cross-blocks at "
          "the floor and %d/15 per-edge Pf4 nonzero (fails G3 + "
          "G5); Schur with t = 0 gives A_eff = kappa A_CC exactly "
          "-- %d/10 carrier cross-blocks"
          % (n0, n_pf0, n_s0),
          n0 == 0 and n_pf0 == 0 and n_s0 == 0, kill="K7")

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
    elif KILLS:
        VERDICT = "KMSMIX-PARTIAL [%s]" % ", ".join(
            sorted(set({"K1": "COMMUTANT-BROKEN",
                        "K2": "KMSROUTE-BROKEN",
                        "K3": "SCHURROUTE-BROKEN",
                        "K5": "FREEZE-BROKEN"}.get(k, k)
                       for k in KILLS)))
    else:
        VERDICT = "KMSMIX-MEASURED [%s, %s, %s]" % (t_m1, t_m2,
                                                    t_rp)
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE PARAMETRIZATION (H1): the hermitian O16-commutant on the
    deployed 16-dim space has dimension %d = %d sym + %d antisym
    (exact orbit walks; isotypic ward sum m^2); the Majorana-
    compatible Hamiltonians K = i h live in the %d-dim
    antisymmetric slice = 33 cross (the round-52 covariant block
    space; the C<->B mixing block T spans 24) + 17 diagonal; the
    only forced zeros remain the 2 diagonal coordinates of the
    transposed {%d,%d} block.
  * THE KMS ROUTE (M1): %s.  beta = 2 robustness: %s.  The KMS
    dressing A = -tan(beta h/2) is itself a mixing machine: the
    per-orbit ray anatomy shows odd powers of h lighting duads far
    outside the seeded orbit -- the Schur mechanism operating
    inside the KMS route.
  * THE RP ANSWER (R1, honest): NO deployed spatial/OS reflection
    theta exists on the 16-dim one-particle space (v155 premise-
    only, v160 none, v426/v440 = 8-dim collar dictionary).  The
    Majorana real structure Theta_0 satisfies the deployed
    v426/v440 dictionary automatically (conj(C_beta) = I - C_beta
    measured); the OS-positivity of the two-point block under a
    SPATIAL theta is the named open check RP-THETA-OPEN.
  * THE SCHUR ROUTE (M2, exact): %s.  From the bare DEPLOYED
    diagonal state + the C6-invariant coupling alone, boundary
    elimination deposits S = V J3 V^T on ALL 10 carrier duads
    (C6-covariant, J-direction, {%d,%d}-compatible, canonical Pf4
    signs) -- the reviewer's cross-connection made concrete: on
    both fronts (RH port, Wick functor) the real correlation
    lives in the ELIMINATED boundary, not the bare bulk.
  * THE FREEZE (M3): the 15 block-correlation signatures of the
    best candidate printed as the frozen prediction table.
  * The [O] premise (the boundary grammar IS a self-hosting Wick
    pair compiler) stays [O]; these are CANDIDATE states + frozen
    signatures; no marker moves.
Runtime: %.1f s""" % (dim_herm, dim_sym, dim_anti, dim_anti,
                      a_ch, b_ch, t_m1, beta2_note, t_m2,
                      a_ch, b_ch, time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


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
    ('kms_schur_mixing_probe', _SRC_0, 30, (), 'KMSMIX-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v898 -- SEAM.CFIN.KMSMIX.01 + SEAM.CFIN.SCHURMIX.01: the channel-mixing state the block Wick functor awaits -- the C6-covariant mixing KMS state EXISTS (u=1, t=1/8, beta=1; all 15 blocks, grading 5/5+10/10, canonical Pf4 signs; beta=2 robust) and the exact Schur elimination GENERATES all 10 carrier duads from the bare diagonal state; RP-THETA-OPEN named; the [O] premise unmoved')
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
    print("v898: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the mixing mechanism has a constructed candidate: KMS state + exact Schur generation; the 15-signature table is the registered prediction')
    print("[%s] v898 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
