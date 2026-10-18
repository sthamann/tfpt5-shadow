#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_minimal_mediator_probe -- SEAM.CFIN.MINIMAL.MEDIATOR.01
(EXPLORATION ONLY, experiments/; round 57, 2026-08-10: is
N_fam = 3 the MINIMAL boundary mediation rank of the v898 Schur
mechanism?  Measured answer: NO at the census/sign demand level --
and the probe says exactly which demand DOES pin 3.)

THE CLAIMED INTERPRETATION (to be measured, from the round-56
research plan): "the three families are the minimal boundary
mediation rank -- the mixing term V J3 V^T has rank <= 3 and
creates all ten carrier pair correlations."  v898 proved the exact
Schur identity A_eff = kappa A_CC + (t^2 m/(1-m^2)) V J3 V^T and
the 10/10 census; it never measured rank(V J3 V^T), never asked
whether a LOWER-rank boundary mediator could do the same job, and
never formalized "minimal mediation rank".  That is exactly this
probe.  RANK CONVENTION (frozen): a real antisymmetric mediator M
on the 6-dim boundary has even matrix rank 2r; its SYMPLECTIC rank
r = number of J-planes is the honest "number of mediating boundary
pairs"; the deployed J3 = (+)_3 J has symplectic rank 3 = N_fam.

PREMISE DISCREPANCIES FOUND BY READING v898 (before any run,
verified below): (i) "rank <= 3" is NOT a v898 statement, and it is
WEAK: antisymmetric matrices have even rank, and the deployed
census matrix S = V J3 V^T is measured here to have matrix rank
EXACTLY 2 (S = ones(5x5) (x) 3J exactly) -- the deployed 3-plane
mediator acts through the coupling fold on ONE effective carrier
plane; (ii) "mediator candidates compatible with the C6 covariance
constraint": the deployed C6 lift O16 is the IDENTITY on the A3
boundary block (v898 CAR convention), so covariance does NOT
constrain the mediator AT ALL -- it constrains the COUPLING V (the
24-dim covariant space, within-orbit row-block repetition).  Both
are measured as checks, not narrated.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing; the smoke run
confirmed the hand pre-derivations, produced the exact numbers
frozen below, and killed ONE dead control guess -- recorded): the
3-value structure theorem holds symbolically; det(B_cross) =
gamma_ab * gamma_cde holds symbolically for every symplectic-
rank-1 mediator; the explicit rank-1 witness J(+)0(+)0 with the
deployed coupling passes 10/10 duads with 10/10 canonical signs
(parent norm 0.6333); the randomized census matches the sign law
on 2000/2000 seeded trials (1883 passing); rank(S) = 2 and
S = ones (x) 3J exact; the rank-3 regression reproduces the v898
census (uniform 3J, det = 9 on all 10); the purity census gives
mixed-line defects {0, 4, 2} for {J3, rank-1, fold-cancel}.  DEAD
GUESS, disclosed: the first covariance-breaking control (globally
NEGATED channel-1 row-block) fired NOTHING -- the per-channel
wedge w_i = p_i /\ q_i is QUADRATIC in the row-block, so a global
sign is invisible (0 positive Pf4; fail-first output preserved in
the smoke log); the honest symmetry-breaking move is the
ORIENTATION-REVERSED (row-swapped) channel block, which flips
w_1 -> -w_1 and reaches positive Pf4 on exactly the four {1,j}
duads.  The C2 fire rule below is frozen in that corrected form.

FROZEN PROTOCOL (2026-08-10, frozen + SHA-hashed before the frozen
run; exact integer / sympy arithmetic in every structural decision;
the ONLY float step is the CAR-validity eigenvalue bound, declared):

 R1  FORMALIZATION (measured, not assumed).
     (a) O16 restricted to the boundary block == identity EXACTLY
         => C6 covariance places NO constraint on the mediator M;
         the constraint lives in the coupling (premise sharpening);
     (b) the covariant coupling space {V : O_C V = V} has dimension
         EXACTLY 24 (numerical projector rank ward, average over
         the 6 group elements) and consists exactly of the V with
         IDENTICAL 2x6 row-blocks along each pi-orbit ({a,b} and
         {c,d,e}) -- verified both ways;
     (c) THE REQUIREMENT REQ(V, M), frozen: S' = V M V^T must have
         all 10 carrier duad blocks nonzero with the canonical
         per-edge Pfaffian signs (measured in S0: ALL 15 canonical
         Pf4 of G_c are NEGATIVE, so the demand per carrier duad is
         det(block) > 0), inside a CAR-valid parent A_full =
         [[kappa A_CC, t V], [-t V^T, m M]] (validity is SCALABLE:
         for every (V, M) some t > 0 makes ||A_full|| < 1 by the
         triangle inequality; the witness parent is checked
         numerically at kappa = m = 1/2, t = 1/20, declared float).

 R2  STRUCTURE THEOREM (exact sympy, fully generic): for EVERY
     covariant V (24 symbols) and EVERY antisymmetric M (15
     symbols), the 10 carrier blocks of S' take exactly THREE
     values: B_ab = gamma_ab * J on the {a,b} duad, B_cde =
     gamma_cde * J on all three within-{c,d,e} duads, and ONE cross
     block B_x (up to the antisymmetry transpose) on all six cross
     duads.  Within-orbit blocks are pure J AUTOMATICALLY (2x2
     antisymmetric).  The entire REQ therefore reduces to three
     scalar demands: gamma_ab != 0, gamma_cde != 0, det(B_x) > 0.

 R3  RANK-1 EXHAUSTION (the decisive part -- a THEOREM at finite
     size, not a search):
     (a) SYMBOLIC IDENTITY: for M = e wedge f (generic symplectic
         rank 1), det(B_x) = gamma_ab * gamma_cde EXACTLY (sympy
         expansion == 0).  COROLLARY: a rank-1 mediator satisfies
         REQ iff gamma_ab * gamma_cde > 0 -- and then ALL demands
         hold simultaneously; the only rank-1 failure mode is the
         sign obstruction gamma_ab * gamma_cde <= 0 (populated-but-
         wrong-sign on the six cross duads, or dead duads);
     (b) EXPLICIT INTEGER WITNESS: M1 = J (+) 0 (+) 0 (ONE boundary
         pair) with the DEPLOYED coupling V = A_int[C, B]: 10/10
         carrier duads populated, 10/10 canonical Pf4 signs, parent
         CAR-valid -- so the minimal symplectic mediation rank
         under REQ is 1, and N_fam = 3 = "minimal mediator rank" is
         REFUTED at this demand level (typed honestly: the plan's
         expected orbit-counting obstruction CANNOT exist, because
         C6 acts trivially on the boundary);
     (c) RANDOMIZED CENSUS (seeded rng, SEED = 20260810, 2000
         trials, integer entries in [-3, 3]): the measured pass/
         fail of REQ matches the sign law sign(gamma_ab *
         gamma_cde) > 0 on 2000/2000 trials (the discrete
         obstruction certifies each failure: dead duads or wrong
         cross signs);
     (d) rank-2 (symplectic) is then trivially non-minimal: M2 =
         J (+) J (+) 0 also passes REQ (10/10, canonical signs) --
         recorded to complete the exhaustion r in {0, 1, 2, 3}.

 R4  DEPLOYED RANK CENSUS (the premise check): the deployed census
     matrix S = V J3 V^T has matrix rank EXACTLY 2 (exact sympy
     rank over Q) and equals ones(5x5) (x) 3J EXACTLY -- the plan's
     "rank <= 3" is true but the content is rank 2 = ONE symplectic
     plane: the fold Sigma of the coupling collapses the deployed
     3-plane mediator onto a single effective carrier plane.

 R5  RANK-3 REGRESSION (v898 M2.4): M = J3 with the deployed V
     reproduces the v898 census EXACTLY: all 10 blocks = 3J
     (uniform, pure J direction, incl. the transposed {a,b} duad),
     all 10 per-edge Pf4 = -9 < 0 canonical.

 R6  WHAT PINS 3 (measured, not asserted): REQ does NOT pin 3; the
     demand that DOES is boundary NONDEGENERACY: kernel dim of the
     mediator = 6 - 2r, and the beta -> infinity boundary KMS
     spectrum has exactly (6 - 2r) eigenvalues pinned at the
     maximally mixed value 1/2 (measured at beta = 50 for r = 3,
     1, 2-fold-cancel: defects 0, 4, 2).  A PURE boundary ground
     state (defect 0) forces matrix rank 6 <=> symplectic rank 3 =
     N_fam.  TYPED HONESTLY: given dim(A3) = 6 this is DIMENSION
     BOOKKEEPING (6 = |Z2| * N_fam), not a mediation theorem -- the
     honest statement is "N_fam = 3 is seated in the boundary
     DIMENSION; the mediation DEMANDS are already satisfied at
     rank 1".

 C   CONTROLS (must fire; frozen fire rules):
     C1 RANK 0: M = 0 gives 0/10 carrier duads (the v898 C2 Schur
        analogue).
     C2 COVARIANCE IS DOING WORK (the plan's control, in the honest
        direction that exists): under a COVARIANT coupling the
        within-orbit Pf4 is -gamma^2 <= 0 ALWAYS (no covariant
        (V, M) of ANY rank can make a within-orbit Pf4 positive);
        BREAKING covariance enlarges the reachable set: the
        explicit non-covariant V' (deployed V with the channel-1
        row-block ORIENTATION-REVERSED, i.e. its two rows swapped;
        covariance defect measured nonzero) with the SAME rank-1
        M1 produces Pf4 > 0 on exactly the four duads {1,j}, j in
        {2..5} -- a pattern PROVABLY unreachable under covariance.
        (The globally NEGATED block is quadratically invisible and
        fires nothing -- the disclosed dead guess.)  Both halves
        must fire.
     C3 NON-MONOTONE RANK: the fold-cancelling mediator
        J (+) (-J) (+) 0 has matrix rank 4 > 2 yet gives 0/10 --
        "mediation capability" is NOT monotone in rank; the naive
        rank reading dies (must fire).
     C4 AST FIREWALL: banned identifiers zetazero / nzeros /
        primerange / isprime / primepi / nextprime / prevprime --
        none may appear (self-scan).

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 formalization/structure ward breaks         -> STRUCTURE-BROKEN
  K2 rank-1 theorem / witness / census breaks    -> RANK-BROKEN
  K3 deployed rank / regression breaks           -> REGRESSION-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): MEDIATOR-MEASURED [STRUCTURE-3VALUES,
RANK1-SUFFICES(sign law gamma_ab*gamma_cde > 0, integer witness),
DEPLOYED-S-RANK-2, N3-NOT-FORCED-BY-MEDIATION, PURITY-PINS-3
(dimension bookkeeping)] / PIPELINE-BROKEN / STRUCTURE-BROKEN /
RANK-BROKEN / REGRESSION-BROKEN / CONTROL-DEAD.  Exit 0 iff all
checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the [O] premise of v898 stays [O]; a
REFUTED minimality reading is the honest outcome and is typed as
such; no marker moves.  NO RH claim.

SPEC v1 (2026-08-10): frozen after the declared smoke run; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline): v898_kms_schur_mixing
(frozen probe kms_schur_mixing_probe, round 55: Schur identity,
census conventions, H1 commutant walk), v896/wick_block_functor
(canonical G_c, FLOOR, chi structure), v53 (|Z2| = g_car - N_fam),
tfpt_constants (g_car, N_fam).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_minimal_mediator_probe.py
"""

import ast
import hashlib
import itertools
import os
import sys
import time

import numpy as np
import sympy as sp

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
SEED = 20260810
N_TRIALS = 2000


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
CAR_DUADS = sorted(itertools.combinations(range(1, 6), 2))


def main():
    print("SEAM.CFIN.MINIMAL.MEDIATOR.01 -- is N_fam = 3 the minimal "
          "boundary mediation rank?")
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
    arf1 = sorted(q for q in refs if q.count(0) == 6)
    cand = [q for q in refs
            if all(q[SIGP[v]] == q[v] for v in range(16))
            and q[A_BIT] == 1 and q[FSIG] == 0]
    check("S0.1 v880/v845 rebuilt: 16 refinements, 6 Arf-1, unique q*",
          len(set(refs)) == 16 and len(arf1) == 6 and len(cand) == 1,
          kill="K0")
    QSTAR = cand[0]
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]
    dmap = {v: frozenset(i for i, q in enumerate(arf1) if q[v] == 0)
            for v in NZ}
    V0 = arf1.index(QSTAR)
    phi = {}
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        phi[next(iter(others))] = next(iter(islot))

    def lab(j):
        return 0 if j == V0 else phi[j]

    SP6 = []
    for imgs in itertools.product(range(1, 16), repeat=4):
        p = [0] * 16
        for v in range(1, 16):
            lb = v & -v
            p[v] = p[v ^ lb] ^ imgs[LOWIDX[lb]]
        if len(set(p)) != 16:
            continue
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
        if any(all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                           for s in range(5))
                   for v in range(16)) for pi in S5P):
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.2 |Sp(4,2)| = %d == 720, |Aut(C_fin)| = %d == 6, "
          "generator pin unique" % (len(SP6), len(AUT)),
          len(SP6) == 720 and len(AUT) == 6 and len(g_pin) == 1,
          kill="K0")
    GEN = g_pin[0]
    a1idx = {q: i for i, q in enumerate(arf1)}
    tau = [a1idx[tuple(q[GEN[v]] for v in range(16))] for q in arf1]
    pia = [0] * 6
    for j in range(6):
        pia[tau[j]] = j
    PI6 = [0] * 6
    for j in range(6):
        PI6[lab(j)] = lab(tuple(pia)[j])
    PI6 = tuple(PI6)
    check("S0.3 deployed channel permutation pi = %s, cycle type "
          "(1, 2, 3)" % (PI6,),
          PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3), kill="K0")

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
    THREE = sorted(next(c for c in cycles if len(c) == 3))
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

    J2i = sp.Matrix([[0, 1], [-1, 0]])
    I2i = sp.eye(2)
    IOTA6 = sp.Matrix.vstack(I2i, I2i, I2i)
    orbs = edge_orbits(PI6)

    def put_ordered(A, x, y, B):
        rx, cy = CH[x], CH[y]
        for r in range(len(rx)):
            for c in range(len(cy)):
                A[rx[r], cy[c]] = B[r, c]
                A[cy[c], rx[r]] = -B[r, c]

    A_int = sp.zeros(16)
    for edges, rev, rep in orbs:
        i, j = rep
        B = J2i if rev else (IOTA6 if i == 0 else I2i)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    A16_dep = sp.zeros(16)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    O16 = sp.zeros(16)
    for r in range(16):
        O16[img[r], r] = 1
    okA = (sp.simplify(O16 * A_int * O16.T - A_int) == sp.zeros(16)
           and A_int.T == -A_int)
    check("S0.4 A_int rebuilt (integer, antisymmetric, exactly "
          "covariant); O16 orthogonal", okA
          and sp.simplify(O16 * O16.T) == sp.eye(16), kill="K0")

    # canonical per-edge Pf4 signs of G_c (exact; positive scaling
    # irrelevant for signs)
    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}

    def pf4_sign_of_16(A16m):
        out = {}
        for (i, j) in DUADS_CH:
            if i == 0:
                B = (IOTA6.T * A16m.extract(CH[0], CH[j]))
            else:
                B = A16m.extract(CH[i], CH[j])
            pf4 = -B.det()
            out[frozenset({i, j})] = sp.sign(pf4)
        return out

    sgn_c = pf4_sign_of_16(A_int)
    check("S0.5 canonical reference: all 15 per-edge Pf4 signs of "
          "G_c are NEGATIVE (exact) -- the carrier-duad demand is "
          "det(block) > 0",
          all(s == -1 for s in sgn_c.values()), kill="K0")

    V_dep = A_int.extract(CAR_IDX, BND_IDX)     # deployed coupling
    J3 = A16_dep.extract(BND_IDX, BND_IDX)      # deployed mediator
    A_CC = A16_dep.extract(CAR_IDX, CAR_IDX)

    # ==================================================================
    section("R1 -- formalization (measured premises)")
    # ==================================================================
    O_B = O16.extract(BND_IDX, BND_IDX)
    check("R1.1 PREMISE SHARPENED: O16 restricted to the boundary "
          "block is the IDENTITY exactly -- C6 covariance places NO "
          "constraint on the mediator; the constraint lives in the "
          "coupling V (the plan's 'C6-covariant mediator' reading "
          "is vacuous on the boundary side)",
          O_B == sp.eye(6), kill="K1")

    O_C = O16.extract(CAR_IDX, CAR_IDX)
    # projector onto {V : O_C V = V} by group averaging (numerical
    # rank ward + exact structure test)
    rng = np.random.default_rng(SEED)
    OCn = np.array(O_C.tolist(), dtype=np.float64)
    dims = 0
    Vr = rng.standard_normal((10, 6, 40))
    P = np.zeros((10, 6, 40))
    Ok = np.eye(10)
    for _k in range(6):
        P += np.einsum("ij,jkl->ikl", Ok, Vr)
        Ok = OCn @ Ok
    P /= 6.0
    dims = np.linalg.matrix_rank(P.reshape(60, 40))
    # exact both-ways structure test: covariant <=> repeated blocks
    ua = sp.Matrix(2, 6, lambda r, c: sp.Symbol("ua_%d_%d" % (r, c)))
    uc = sp.Matrix(2, 6, lambda r, c: sp.Symbol("uc_%d_%d" % (r, c)))
    Vg = sp.zeros(10, 6)
    for ch in range(1, 6):
        blk = ua if ch in TWO else uc
        for r in range(2):
            for c in range(6):
                Vg[CH[ch][r], c] = blk[r, c]
    ok_rep = sp.simplify(O_C * Vg - Vg) == sp.zeros(10, 6)
    check("R1.2 THE COVARIANT COUPLING SPACE: dim = %d == 24 "
          "(projector rank, seeded probes) and equals EXACTLY the "
          "V with identical 2x6 row-blocks along the pi-orbits "
          "{%d,%d} and %s (symbolic both-ways)"
          % (dims, a_ch, b_ch, THREE),
          dims == 24 and ok_rep, kill="K1")
    ok_dep_cov = sp.simplify(O_C * V_dep - V_dep) == sp.zeros(10, 6)
    check("R1.3 the deployed coupling V = A_int[C, B] is covariant; "
          "REQ(V, M) frozen: all 10 carrier blocks of S' = V M V^T "
          "nonzero with det(block) > 0 (canonical signs), CAR-"
          "scalable parent", ok_dep_cov, kill="K1")

    def census(Vm, M):
        S = Vm * M * Vm.T
        rows = {}
        for (i, j) in CAR_DUADS:
            B = S.extract(CH[i], CH[j])
            nz = any(x != 0 for x in B)
            det = B.det()
            aJ = sp.Rational(B[0, 1] - B[1, 0], 2)
            rows[(i, j)] = (bool(nz), det, aJ)
        return S, rows

    def req_pass(rows):
        dead = [d for d in rows if not rows[d][0]]
        wrong = [d for d in rows if rows[d][0] and rows[d][1] <= 0]
        return dead, wrong

    # ==================================================================
    section("R2 -- the 3-value structure theorem (exact, generic)")
    # ==================================================================
    mg = sp.zeros(6, 6)
    msy = {}
    for r in range(6):
        for c in range(r + 1, 6):
            s = sp.Symbol("m_%d_%d" % (r, c))
            msy[(r, c)] = s
            mg[r, c] = s
            mg[c, r] = -s
    Sg = Vg * mg * Vg.T
    B_ab = Sg.extract(CH[a_ch], CH[b_ch])
    vals_cde = [sp.expand(Sg.extract(CH[i], CH[j]))
                for (i, j) in itertools.combinations(THREE, 2)]
    ok_cde = all(v == vals_cde[0] for v in vals_cde)
    cross = []
    for (i, j) in CAR_DUADS:
        oi = "ab" if i in TWO else "cde"
        oj = "ab" if j in TWO else "cde"
        if {oi, oj} == {"ab", "cde"}:
            B = Sg.extract(CH[i], CH[j])
            # orient every cross block as (cde-side, ab-side)
            if i in TWO:
                B = -B.T
            cross.append(sp.expand(B))
    ok_cross = all(c == cross[0] for c in cross)
    ok_pureJ = (sp.expand(B_ab[0, 0]) == 0
                and sp.expand(B_ab[1, 1]) == 0
                and sp.expand(B_ab[0, 1] + B_ab[1, 0]) == 0
                and sp.expand(vals_cde[0][0, 0]) == 0
                and sp.expand(vals_cde[0][1, 1]) == 0
                and sp.expand(vals_cde[0][0, 1]
                              + vals_cde[0][1, 0]) == 0)
    check("R2.1 STRUCTURE THEOREM (fully generic, 24 + 15 symbols): "
          "the 10 carrier blocks of S' take exactly THREE values -- "
          "gamma_ab J on {%d,%d}, gamma_cde J on all three "
          "within-%s duads (pure J automatic), one repeated cross "
          "block on all six cross duads; REQ reduces to gamma_ab "
          "!= 0, gamma_cde != 0, det(B_x) > 0"
          % (a_ch, b_ch, THREE),
          ok_cde and ok_cross and ok_pureJ, kill="K1")

    # ==================================================================
    section("R3 -- rank-1 exhaustion (theorem + witness + census)")
    # ==================================================================
    ev = sp.Matrix(6, 1, lambda r, _c: sp.Symbol("e_%d" % r))
    fv = sp.Matrix(6, 1, lambda r, _c: sp.Symbol("f_%d" % r))
    M1g = ev * fv.T - fv * ev.T
    S1g = Vg * M1g * Vg.T
    gam_ab = sp.expand(S1g[CH[a_ch][0], CH[b_ch][1]])
    # gamma_ab J means entry (0,1) of the {a,b} block; within-cde:
    c0, c1 = THREE[0], THREE[1]
    gam_cde = sp.expand(S1g[CH[c0][0], CH[c1][1]])
    Bx = S1g.extract(CH[THREE[0]], CH[TWO[0]])
    detBx = sp.expand(Bx.det())
    ident = sp.expand(detBx - gam_cde * gam_ab)
    check("R3.1 SYMBOLIC RANK-1 IDENTITY: det(B_x) - gamma_ab * "
          "gamma_cde == 0 for GENERIC e, f and generic covariant "
          "coupling (sympy expansion; %d-symbol identity) -- the "
          "ONLY rank-1 failure mode is the sign obstruction "
          "gamma_ab * gamma_cde <= 0" % (24 + 12),
          ident == 0, kill="K2")

    M1 = sp.zeros(6, 6)
    M1[0, 1], M1[1, 0] = 1, -1          # J (+) 0 (+) 0
    _S1, rows1 = census(V_dep, M1)
    dead1, wrong1 = req_pass(rows1)
    # CAR validity of the witness parent (declared float step)
    kap, m_mix, t_cpl = sp.Rational(1, 2), sp.Rational(1, 2), \
        sp.Rational(1, 20)
    A_full = sp.Matrix(sp.BlockMatrix(
        [[kap * A_CC, t_cpl * V_dep],
         [-t_cpl * V_dep.T, m_mix * M1]]))
    Af = np.array(A_full.tolist(), dtype=np.float64)
    smax = float(np.max(np.abs(np.linalg.eigvalsh(1j * Af))))
    check("R3.2 EXPLICIT INTEGER WITNESS: M1 = J(+)0(+)0 (ONE "
          "boundary pair, symplectic rank 1) with the DEPLOYED "
          "coupling: %d/10 duads populated, %d wrong signs, parent "
          "||A_full|| = %.4f < 1 (kappa = m = 1/2, t = 1/20) -- "
          "N_fam = 3 = 'minimal mediator rank' is REFUTED at the "
          "REQ demand level: the minimal symplectic rank is 1"
          % (10 - len(dead1), len(wrong1), smax),
          not dead1 and not wrong1 and smax < 1, kill="K2")

    rng2 = np.random.default_rng(SEED)
    n_match = 0
    n_pass_trials = 0
    for _tr in range(N_TRIALS):
        e = rng2.integers(-3, 4, size=6)
        f = rng2.integers(-3, 4, size=6)
        Mnp = np.outer(e, f) - np.outer(f, e)
        Mtr = sp.Matrix(Mnp.tolist())
        _St, rows_t = census(V_dep, Mtr)
        dead_t, wrong_t = req_pass(rows_t)
        ok_t = (not dead_t and not wrong_t)
        gab = rows_t[(a_ch, b_ch)][2]
        gcd = rows_t[(c0, c1)][2]
        predicted = bool(gab * gcd > 0)
        n_match += (ok_t == predicted)
        n_pass_trials += ok_t
    check("R3.3 RANDOMIZED CENSUS (seed %d): measured REQ pass/fail "
          "matches the sign law gamma_ab*gamma_cde > 0 on %d/%d "
          "trials (%d passing); every failure certified by the "
          "discrete obstruction (dead duads / wrong cross signs)"
          % (SEED, n_match, N_TRIALS, n_pass_trials),
          n_match == N_TRIALS and 0 < n_pass_trials < N_TRIALS,
          kill="K2")

    M2 = sp.zeros(6, 6)
    M2[0, 1], M2[1, 0] = 1, -1
    M2[2, 3], M2[3, 2] = 1, -1          # J (+) J (+) 0
    _S2, rows2 = census(V_dep, M2)
    dead2, wrong2 = req_pass(rows2)
    check("R3.4 rank-2 completeness: M2 = J(+)J(+)0 also passes REQ "
          "(%d/10, %d wrong signs) -- exhaustion r in {0, 1, 2, 3} "
          "complete: r = 0 fails (C1), r >= 1 all pass"
          % (10 - len(dead2), len(wrong2)),
          not dead2 and not wrong2, kill="K2")

    # ==================================================================
    section("R4 -- deployed rank census (the premise check)")
    # ==================================================================
    S_dep = V_dep * J3 * V_dep.T
    rank_S = S_dep.rank()
    ones5_3J = sp.Matrix(10, 10, lambda r, c:
                         3 * J2i[r % 2, c % 2]
                         if (r % 2, c % 2) != (0, 0) or True else 0)
    # build ones(5x5) (x) 3J explicitly
    K3J = sp.zeros(10, 10)
    for bi in range(5):
        for bj in range(5):
            for r in range(2):
                for c in range(2):
                    K3J[2 * bi + r, 2 * bj + c] = 3 * J2i[r, c]
    check("R4.1 DEPLOYED RANK: rank(S = V J3 V^T) = %d == 2 EXACT "
          "and S == ones(5x5) (x) 3J EXACT -- the plan's 'rank <= "
          "3' is true but weak (antisymmetric rank is even); the "
          "deployed 3-plane mediator acts through the coupling "
          "fold on ONE effective carrier plane" % rank_S,
          rank_S == 2 and sp.simplify(S_dep - K3J) == sp.zeros(10),
          kill="K3")

    # ==================================================================
    section("R5 -- rank-3 regression (v898 M2.4)")
    # ==================================================================
    _Sd, rowsd = census(V_dep, J3)
    deadd, wrongd = req_pass(rowsd)
    ok_uniform = all(rowsd[d][2] == 3 for d in rowsd)
    ok_pf = all(rowsd[d][1] == 9 for d in rowsd)
    check("R5.1 REGRESSION: M = J3 with the deployed V reproduces "
          "the v898 census EXACTLY -- 10/10 blocks = 3J uniform "
          "(a_J = 3 incl. the transposed {%d,%d} duad), per-edge "
          "det = 9 > 0 (Pf4 = -9 < 0 canonical) on all 10"
          % (a_ch, b_ch),
          not deadd and not wrongd and ok_uniform and ok_pf,
          kill="K3")

    # ==================================================================
    section("R6 -- what pins 3 (measured)")
    # ==================================================================
    defects = {}
    for nm, M in (("J3 (r=3)", J3), ("rank-1", M1),
                  ("fold-cancel (r=2)", None)):
        if M is None:
            M = sp.zeros(6, 6)
            M[0, 1], M[1, 0] = 1, -1
            M[2, 3], M[3, 2] = -1, 1
        Mn = np.array(M.tolist(), dtype=np.float64)
        w = np.linalg.eigvalsh(1j * Mn)
        fB = 1.0 / (1.0 + np.exp(np.clip(50.0 * w, -700, 700)))
        defects[nm] = int(np.sum(np.abs(fB - 0.5) < 1e-6))
    check("R6.1 PURITY CENSUS (beta = 50 boundary KMS spectrum): "
          "eigenvalues pinned at the maximally mixed 1/2: %s == "
          "{0, 4, 2} = kernel dims 6 - 2r; a PURE boundary ground "
          "state forces matrix rank 6 <=> symplectic rank 3 = "
          "N_fam.  TYPED HONESTLY: with dim(A3) = 6 = |Z2| * N_fam "
          "this is DIMENSION BOOKKEEPING, not a mediation theorem "
          "-- N_fam = 3 is seated in the boundary DIMENSION; the "
          "mediation demands are already satisfied at rank 1"
          % ({k: v for k, v in defects.items()},),
          defects["J3 (r=3)"] == 0 and defects["rank-1"] == 4
          and defects["fold-cancel (r=2)"] == 2
          and 6 == (g_car - N_fam) * N_fam, kill="K3")

    # ==================================================================
    section("C -- controls (must fire)")
    # ==================================================================
    _S0, rows_0 = census(V_dep, sp.zeros(6, 6))
    dead0, _w0 = req_pass(rows_0)
    check("C1 FIRES: M = 0 gives %d/10 dead carrier duads (the "
          "v898 C2 Schur analogue)" % len(dead0),
          len(dead0) == 10, kill="K7")

    # covariance is doing work: within-orbit Pf4 can NEVER be
    # positive under covariance (det(gamma J) = gamma^2 => Pf4 =
    # -gamma^2 <= 0, from R2); breaking covariance by ORIENTATION
    # REVERSAL (row swap flips the channel wedge w_1 -> -w_1;
    # the globally negated block is quadratically invisible --
    # the disclosed dead guess) reaches positive Pf4
    Vbrk = sp.Matrix(V_dep)
    r0, r1 = CH[1]
    for c in range(6):
        Vbrk[r0, c], Vbrk[r1, c] = V_dep[r1, c], V_dep[r0, c]
    brk_defect = sp.simplify(O_C * Vbrk - Vbrk) != sp.zeros(10, 6)
    _Sb, rows_b = census(Vbrk, M1)
    pos_duads = sorted(d for d in rows_b if rows_b[d][1] < 0)
    # det < 0 <=> Pf4 = -det > 0  (positive Pf4, unreachable
    # under covariance)
    exp_pos = sorted(d for d in rows_b if 1 in d)
    check("C2 FIRES: BREAKING COVARIANCE ENLARGES LOW RANK -- the "
          "orientation-reversed channel-1 coupling (row swap; "
          "covariance defect nonzero: %s) with the SAME rank-1 M1 "
          "reaches POSITIVE Pf4 on %s (exactly the four {1,j} "
          "duads), a pattern PROVABLY unreachable under covariance "
          "(R2/R3: covariant within-orbit Pf4 = -gamma^2 <= 0 and "
          "cross Pf4 uniform)"
          % (brk_defect, pos_duads),
          brk_defect and pos_duads == exp_pos
          and len(pos_duads) == 4, kill="K7")

    Mfc = sp.zeros(6, 6)
    Mfc[0, 1], Mfc[1, 0] = 1, -1
    Mfc[2, 3], Mfc[3, 2] = -1, 1
    _Sf, rows_f = census(V_dep, Mfc)
    deadf, _wf = req_pass(rows_f)
    check("C3 FIRES: the fold-cancelling J(+)(-J)(+)0 has matrix "
          "rank %d > 2 yet gives %d/10 dead duads -- mediation "
          "capability is NOT monotone in rank; the naive rank "
          "reading dies" % (Mfc.rank(), len(deadf)),
          Mfc.rank() == 4 and len(deadf) == 10, kill="K7")

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
        VERDICT = "STRUCTURE-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "RANK-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "REGRESSION-BROKEN"
    else:
        VERDICT = ("MEDIATOR-MEASURED [STRUCTURE-3VALUES, "
                   "RANK1-SUFFICES(sign law gamma_ab*gamma_cde > 0, "
                   "integer witness J(+)0(+)0), DEPLOYED-S-RANK-2, "
                   "N3-NOT-FORCED-BY-MEDIATION, PURITY-PINS-3"
                   "(dimension bookkeeping)]")
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE FORMALIZATION (R1/R2): C6 acts as the IDENTITY on the A3
    boundary, so covariance constrains the COUPLING, not the
    mediator; under a covariant coupling the whole 10-duad census
    collapses to THREE scalars (gamma_ab, gamma_cde, det B_x).
  * THE DECISIVE ANSWER (R3): rank <= 2 is NOT excluded -- it is
    not even obstructed: ONE boundary pair (symplectic rank 1)
    already populates all ten carrier duads with the canonical
    Pfaffian signs (exact integer witness; exact sign law det(B_x)
    = gamma_ab * gamma_cde proved symbolically; 2000/2000 seeded
    census).  'N_fam = 3 = minimal mediator rank' is REFUTED at
    the census/sign demand level.
  * THE PREMISE CORRECTION (R4): the deployed mixing term V J3 V^T
    has matrix rank EXACTLY 2 (= ones (x) 3J), not 'rank <= 3' as
    a sharp statement -- the fold collapses the deployed 3-plane
    mediator onto one effective carrier plane.
  * WHAT ACTUALLY PINS 3 (R6): boundary NONDEGENERACY (a pure
    ground state, purity defect 0) forces symplectic rank 3 -- but
    with dim(A3) = 6 = |Z2| * N_fam that is dimension bookkeeping,
    not a mediation theorem.  The honest seat of the three
    families on this front remains the boundary dimension.
  * The [O] premise of v898 stays [O]; no marker moves; NO RH
    claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
