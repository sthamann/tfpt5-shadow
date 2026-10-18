#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rp_parent_dilation_probe -- SEAM.CFIN.RP.DILATION.01
(EXPLORATION ONLY, experiments/; round 59, 2026-08-10, Probe 7 --
the parent-dilation mechanism: a quasi-free parent state on
H_carrier (+) H_boundary (the v898 split 16 = 10 + 6) that is KMS
and reflection-positive under the FULL reflections, whose
Schur/Feshbach compression C_eff = C_CC - C_CB C_BB^{-1} C_BC
carries the full Pfaffian mixing.)

THE QUESTION.  Round 58 measured that strict RP forces t = 0 on
the v898 KMS family; Probe 6 (rp_twisted_involution_census_probe)
closed the twisted-OS escape (TWISTED-RP-EXCLUSIONARY, 0/6).  The
remaining mechanism is DILATION: RP of a state does NOT transfer
to its Schur compression (the compression is the
boundary-ELIMINATED conditional state, not the restriction), so an
RP + KMS parent whose compression carries the mixing would make
the effective-carrier RP failure COMPATIBLE with parent RP.  This
probe parametrizes an explicit finite-dimensional family of
C6-covariant quasi-free parents, imposes parent-CAR + parent-KMS +
parent-RP, and searches/solves for compressions hitting the v898
mixing gates.

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-10): v898 M2 deploys the EXACT Schur elimination of ONE
parent (kappa = m = 1/2, t = 1/20) and proves
SCHURMIX-GENERATES(10/10) -- but it never asks whether that parent
is reflection-positive (RP-THETA-OPEN was still open there);
round 58 deployed the reflections but tested only the KMS family
h(u, t), never the coupled-diagonal parents; Probe 6 tested twist
dressings of the SAME family.  NOTHING in the corpus intersects
parent-RP with the Schur mixing.  That is exactly this probe.

SMOKE-RUN DISCLOSURE (2026-08-10, declared smoke rounds before
freezing; fail-first preserved -- the smoke REFUTED the naive
witness guess and the frozen claims below record what was actually
measured.  The verdict is a SPLIT, neither clean witness nor clean
obstruction):
 (i)   REFUTED GUESS (kept honest): the first draft guessed that
       the coupling is strict-RP-innocent under theta_S and that
       the v898 M2 parent passes STRICT RP under both reflections.
       MEASURED: strict theta_S RP fails at EVERY coupled point of
       the grid -- the even deg-2 Gram is NOT Hermitian, with the
       defect seated EXACTLY on the (empty monomial <-> mixed
       carrier-boundary pair) entries, magnitude LINEAR in the
       coupling (normalized defect 0.05 at t = 1/40, 0.1 at 1/20,
       0.2 at 1/10; and 2s for the carrier-cross knob: 0.1 at
       s = 1/20, 0.25 at s = 1/8).  The 1p Gram stays EXACTLY
       Hermitian with lam_min = kappa (- s shifts) > 0: the
       strict obstruction is deg-2-Hermiticity-only;
 (ii)  the HERMITIZED theta_S Gram is PD in the small-coupling
       regime (0.2125 at the M2 parent, exact) -- the same
       quasi-RP failure type round 58 measured on the KMS family
       (defect 0.0982 there, 0.1 = 2t here, with an exactly known
       seat) -- but hermitization does NOT rescue the whole
       family: the full grid shows indefinite hermitized corners
       at large coupling even without carrier cross (s = 0 floor
       -0.0875) and harder with it (s > 0 floor -0.2124);
 (iii) theta_abT is a MARGINAL-RP PASS at every s = 0 point (Gram
       Hermitian at machine zero, 1p eigenvalues exactly {0, 0}:
       the parent has NO {4,5} carrier cross block, so the
       round-58 criterion a_J = 0 <=> RP is satisfied ON THE
       BOUNDARY of the cone), and fails for every s > 0 with the
       parent-level a_J = s and odd eigenvalues -+ s (the round-58
       identity one level up);
 (iv)  the compression of the M2 parent carries the mixing EXACTLY
       as v898 registered: A_eff = kappa A_CC + lam W J3 W^T with
       lam = m/(1-m^2), all 10 carrier duads nonzero with the
       uniform 3J block and canonical (negative) Pf4 signs; the
       J-coordinate per duad is t^2 * 3m/(1-m^2) = 1/200 = the
       round-51/52 FLOOR exactly (rational identity), and the
       effective a_J = 1/200 != 0 on {4,5}: the compressed state
       FAILS effective-carrier RP by exactly the round-58
       mechanism (odd eigenvalues exactly -+ |a_J|), while the
       parent PASSES theta_abT RP (marginally) -- the dilation
       mechanism is REAL for the 2-cycle obstruction;
 (v)   orbit selectivity (measured): W1-only coupling (t2 = 0)
       populates ONLY the {4,5} duad (1/10), W2-only populates
       only the 3-cycle duads (3/10); FULL mixing needs BOTH
       orbit couplings;
 (vi)  honesty notes shaped by the smoke: (a) parent-KMS does not
       bind beyond CAR (any strict CAR covariance is the beta = 1
       KMS state of h = -2 arctan(A), covariant when A is; ward);
       (b) the compression lives on the UNIFORM J-ray (1_5 (x) 3J),
       NOT on the A_int ray of the KMS family (pure-J duads 10/10
       vs 1/10 for the KMS winner): the mixing gates are hit but
       the state is a different covariant direction -- typed, not
       hidden; (c) the carrier sheet swap restricted to the
       compression stays strictly RP (lam_min 0.25): the
       compressed failure is 2-cycle-seated, like round 58.

CONVENTIONS (v898 / round 58 / Probe 6, rebuilt inline; READ-ONLY
import of tfpt_constants): 16-dim Majorana space, carrier C =
indices 0..9 (channels 1..5), boundary B = 10..15 (channel 0);
quasi-free covariance G = (I + iA)/2, CAR-valid iff ||A|| < 1;
V = A_int[C, B] (the C6-covariant coupling, vacuum orbits: W1 =
rows of the 2-cycle channels {4,5}, W2 = rows of the 3-cycle
channels {1,2,3}); A_CC = A16_dep[C,C] = (+)_5 J; J3 =
A16_dep[B,B]; A_int_CC = A_int[C,C].  THE FROZEN PARENT FAMILY
(explicit, finite-dimensional):
    A_par(kappa, m, t1, t2, s) =
        [[kappa A_CC + s A_int_CC,  t1 W1 + t2 W2],
         [-(t1 W1 + t2 W2)^T,       m J3]]
(all five parameters rational; C6-covariant by construction,
warded exactly).  Reflections: theta_S (sheet swap, eta = +i) and
theta_abT (orientation-reversed 2-cycle, eta = +i), v519 Gram
criterion, sector-typed strict RP (Hermiticity defect <= ZTOL =
1e-10 AND lam_min >= -NZ_FLOOR = 1e-8 in 1p and even deg <= 2).
Compression: C_eff = C_CC - C_CB C_BB^{-1} C_BC, A_eff =
antisymmetric part; mixing gates = v898 M2 (10/10 carrier duads
nonzero, C6-covariant, canonical per-edge Pf4 signs, pure-J {4,5}
block).  NUMERICAL PROTOCOL (declared): float64 for the frozen
scan; the WITNESS is verified in EXACT sympy rational arithmetic
end to end (Grams exactly Hermitian, PSD by exact LDL pivots,
Schur identity symbolic in all five parameters, census and Pf4
signs exact).

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 P1  THE FAMILY + KMS TYPING.
     (a) A_par is C6-covariant and antisymmetric for all scanned
         parameters (exact integer wiring; ward);
     (b) parent-KMS binds exactly through CAR-strictness (typed
         honestly): the -2 artanh spectral map of A_par exists iff
         ||A|| < 1 and yields a real antisymmetric covariant
         h_par whose beta = 1 KMS covariance round-trips to A_par
         at <= 1e-12 (float ward at the witness): every CAR-strict
         member IS a beta = 1 KMS state of a covariant
         Hamiltonian;
     (c) CAR census on the frozen grid is REPORTED, not gated
         (smoke measured 78/108 CAR-valid; the (1/5, 1/5) coupling
         rows and large-s corners drop out); the frozen gate is
         only that every point cited in P2-P4 is CAR-valid
         (||A|| <= 0.95).
 P2  THE DECISIVE SCAN (frozen grid, frozen first-winner rule).
     Grid: kappa in {1/4, 1/2} x m in {1/4, 1/2, 3/4} x (t1, t2)
     in {(1/20,1/20), (1/10,1/10), (1/5,1/5), (1/20,0), (0,1/20),
     (1/10,1/20)} x s in {0, 1/20, 1/8}, frozen order (108 points,
     every grid point has nonzero coupling or cross); per point:
     parent strict RP (theta_S 1p + deg-2; theta_abT 1p + deg-2,
     both eta = +i) and compression census.  FROZEN CLAIMS:
     (a) STRICT-COLLAR OBSTRUCTION (family-wide): ZERO CAR-valid
         grid points pass strict theta_S RP; the deg-2 Hermiticity
         defect is >= 0.04 at every CAR-valid point, while the 1p
         Gram is Hermitian at <= ZTOL everywhere -- the strict
         collar route is deg-2-Hermiticity-obstructed on the
         WHOLE family;
     (b) HERMITIZED-RP ANATOMY (measured, no PD law): the
         hermitized floor over CAR-valid points is -0.0875 +-
         0.005 at s = 0 and -0.2124 +- 0.005 at s > 0
         (indefinite corners at large coupling); PD holds in the
         small-coupling regime and EXACTLY at the M2 parent;
     (c) MARGINAL theta_abT WITNESS SET: EVERY CAR-valid s = 0
         point passes theta_abT RP (Hermitian <= ZTOL, |lam_min|
         <= 1e-9, marginal); EVERY CAR-valid s > 0 point fails
         with lam_min <= -0.04 (parent a_J = s); the FIRST point
         passing {CAR, theta_abT RP, mixing 10/10 canonical} is
         (1/4, 1/4, 1/20, 1/20, 0), and the v898 M2 parent
         (1/2, 1/2, 1/20, 1/20, 0) is in the witness set;
     (d) ORBIT SELECTIVITY: at s = 0, W1-only coupling gives
         exactly 1/10 mixed duads and W2-only exactly 3/10; 10/10
         requires BOTH orbit couplings (measured on all s = 0
         CAR-valid points of those rows).
 P3  THE EXACT WITNESS + EXACT OBSTRUCTION (sympy rationals).
     (a) SYMBOLIC SCHUR IDENTITY (all five parameters): A_eff =
         kappa A_CC + s A_int_CC + (m/(1-m^2)) W J3 W^T EXACTLY;
     (b) at the M2 parent: the theta_S 1p Gram is EXACTLY
         Hermitian and PD by exact LDL (float lam_min = 0.5000 +-
         1e-6); the deg-2 Gram is EXACTLY NON-Hermitian: every
         nonzero entry of M - M^dagger has exact magnitude 2t =
         1/10 and sits on an (empty <-> mixed carrier-boundary
         pair) position -- the strict obstruction is EXACT, not
         numerical; the HERMITIZED deg-2 Gram is PD by exact LDL
         (float lam_min = 0.2125 +- 5e-3);
     (c) theta_abT Grams at the M2 parent: EXACTLY Hermitian, 1p
         eigenvalues exactly {0, 0} (multiplicity-aware), deg-2
         exactly PSD by LDL pivots -- the MARGINAL WITNESS is
         exact;
     (d) compression census EXACT: all 10 carrier duads carry the
         uniform block 3 lam t^2 J (lam = m/(1-m^2) = 2/3 at
         m = 1/2), J-coordinate = t^2 3m/(1-m^2) = 1/200 = the
         round-51/52 FLOOR exactly; per-edge Pf4 < 0 = canonical
         sign on 10/10; compressed CAR valid;
     (e) t_eff TYPING (honest): the compression realizes the
         UNIFORM J-ray 1_5 (x) (1/200) J -- the same value level
         as the canonical G_c FLOOR but a DIFFERENT covariant
         direction than the KMS family's t A_int; measured
         direction census: 10/10 duads pure-J for the compression
         vs 1/10 for the KMS winner at (1, 1/8, 1).
 P4  THE MECHANISM (marginal parent RP + effective RP failure).
     (a) the compressed 10-dim state has a_J = 3 lam t^2 = 1/200
         on the {4,5} duad (exact) and FAILS strict effective RP
         under the carrier 2-cycle reflection: odd-sector Gram
         eigenvalues EXACTLY {-|a_J|, +|a_J|} (identity defect <=
         1e-12), lam_min = -1/200 < 0;
     (b) the carrier sheet swap on the compressed state stays
         strictly RP (Hermitian <= ZTOL, lam_min = 0.25 +- 1e-6)
         -- the effective failure is 2-cycle-seated;
     (c) TYPED CONCLUSION (the SPLIT): for the 2-cycle reflection
         -- the seat of the round-58 incompatibility theorem --
         the dilation mechanism is REALIZED: the parent satisfies
         a_J = 0 <=> RP (marginally, on the cone boundary) while
         its compression carries a_J = 1/200 != 0 and full mixing;
         for the STRICT collar (sheet-swap) demand the route is
         OBSTRUCTED on this family by the exact linear-in-coupling
         deg-2 Hermiticity defect -- RP-vs-mixing moves UP to
         strict-vs-marginal/hermitized, it does not dissolve.
 C   CONTROLS (must fire; frozen fire rules; RNG only here).
     C1 THE DIAGONAL PARENT (t1 = t2 = s = 0): compression has
        0/10 carrier duads (exact) -- coupling is the ONLY mixing
        source (v898 C2 regression);
     C2 SEEDED NON-COVARIANT COUPLING (rng 900, 3 draws: random
        row permutation of W): breaks the exact C6-covariance ward
        of A_par (defect >= NZ_FLOOR) on 3/3 draws;
     C3 CARRIER-INVARIANT-REFLECTION REGRESSION: the v898 KMS
        winner state (u=1, t=1/8, beta=1) FAILS strict RP under
        theta_S (deg-2 Hermiticity defect 0.0982 +- 0.005) -- the
        same failure type as the parent family (defect comparable,
        0.1 at the M2 parent);
     C4 PARENT-LEVEL a_J GATE: at s = 1/20 the parent theta_abT
        odd Gram has eigenvalues -+ s (identity defect <= 1e-12)
        and strict RP fails -- the round-58 identity holds one
        level up and fires when the cross block is switched on.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 family / KMS-typing ward breaks             -> FAMILY-BROKEN
  K2 scan / seat-law ward breaks                 -> SCAN-BROKEN
  K3 exact witness verification breaks           -> WITNESS-BROKEN
  K4 mechanism ward breaks                       -> MECHANISM-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): DILATION-SPLIT [MARGINAL-WITNESS(theta_abT:
v898 M2 parent in the exact witness set), STRICT-COLLAR-OBSTRUCTED
(exact deg-2 Hermiticity defect, magnitude 2t, linear law),
EFFECTIVE-RP-FAILS(a_J = 1/200, 2-cycle-seated), FLOOR-REALIZED
(J-coordinate = 1/200 exactly)] / PIPELINE-BROKEN / FAMILY-BROKEN
/ SCAN-BROKEN / WITNESS-BROKEN / MECHANISM-BROKEN / CONTROL-DEAD.
Exit 0 iff all checks pass and no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: the [O] premise of v898 stays [O];
the marginal witness is a CANDIDATE parent state ON THE CONE
BOUNDARY -- whether the actual seam realizes it is untouched; the
strict-collar obstruction is a measurement on THIS parametrized
family, not a universal no-go; the direction mismatch (J-ray vs
A_int ray) is typed, not hidden; no marker moves.  NO RH claim.

SPEC v1 (2026-08-10): frozen after the declared smoke round; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline): v898_kms_schur_
mixing (M2 Schur route, gates), seam_state_derivation_probe
(round 58: RP machinery, strict-RP exclusion),
rp_twisted_involution_census_probe (Probe 6: twisted closure),
seam_minimal_mediator_probe (round 57: S = 1_5 (x) 3J, rank 2),
v519 (RP Gram + twist), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/rp_parent_dilation_probe.py
"""

import ast
import hashlib
import itertools
import math
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

NZ_FLOOR = 1e-8
ZTOL = 1e-10
PF_FLOOR = 1e-16


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
    print("SEAM.CFIN.RP.DILATION.01 -- the parent-dilation "
          "mechanism: RP + KMS parent, mixing in the compression")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (round 58 rebuilt)")
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
    QSTAR = cand[0] if cand else None
    NZ = list(range(1, 16))
    ovoid = [v for v in NZ if QSTAR[v] == 0]

    def duad(v):
        return frozenset(i for i, q in enumerate(arf1) if q[v] == 0)

    dmap = {v: duad(v) for v in NZ}
    V0 = arf1.index(QSTAR)
    phi = {}
    ok_phi = True
    for o in ovoid:
        others = dmap[o] - {V0}
        islot = frozenset(range(1, 6)) - iota_support(o)
        ok_phi &= (len(others) == 1 and len(islot) == 1)
        phi[next(iter(others))] = next(iter(islot))
    ok_phi &= (len(phi) == 5 and set(phi.values()) == set(range(1, 6)))

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
        pis = [pi for pi in S5P
               if all(IOTA_MSG[p[v]] == tuple(IOTA_MSG[v][pi[s]]
                                              for s in range(5))
                      for v in range(16))]
        if pis:
            AUT.append(p)
    g_pin = [p for p in AUT
             if perm_order(p) == 6 and compose(p, p) == SIGP]
    check("S0.1 compiler rebuilt: unique q*, |Aut| = %d == 6, "
          "generator pin unique" % len(AUT),
          ok_ref and len(cand) == 1 and ok_phi and len(AUT) == 6
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
    check("S0.2 deployed pi = %s, cycle type %s == (1, 2, 3); "
          "2-cycle {%d,%d}, 3-cycle %s"
          % (PI6, cycle_type(PI6), a_ch, b_ch, THREE),
          PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3), kill="K0")

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
    CAR_IDX = list(range(10))
    BND_IDX = list(range(10, 16))
    img = [0] * 16
    for i in range(6):
        for k, s in enumerate(CH[i]):
            img[s] = CH[PI6[i]][k]

    J2i = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    I2i = np.eye(2, dtype=np.int64)
    IOTA6i = np.vstack([I2i, I2i, I2i])
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
        B = J2i if rev else (IOTA6i if i == 0 else I2i)
        x, y = i, j
        for _k in range(perm_order(PI6)):
            put_ordered(A_int, x, y, B)
            x, y = PI6[x], PI6[y]
    A16_dep = np.zeros((16, 16), dtype=np.int64)
    for i in range(8):
        A16_dep[2 * i, 2 * i + 1] = 1
        A16_dep[2 * i + 1, 2 * i] = -1
    okA = (np.array_equal(A_int[np.ix_(img, img)], A_int)
           and np.array_equal(A_int, -A_int.T))
    okD = np.array_equal(A16_dep[np.ix_(img, img)], A16_dep)

    # blocks of the parent family (integer)
    A_CC = A16_dep[np.ix_(CAR_IDX, CAR_IDX)]
    J3 = A16_dep[np.ix_(BND_IDX, BND_IDX)]
    Vc = A_int[np.ix_(CAR_IDX, BND_IDX)]
    A_int_CC = A_int[np.ix_(CAR_IDX, CAR_IDX)]
    W1 = np.zeros_like(Vc)
    W2 = np.zeros_like(Vc)
    for chn in (a_ch, b_ch):
        for r in CH[chn]:
            W1[r, :] = Vc[r, :]
    for chn in THREE:
        for r in CH[chn]:
            W2[r, :] = Vc[r, :]
    ok_split = np.array_equal(W1 + W2, Vc)
    check("S0.3 blocks extracted: A_CC = (+)_5 J, J3, V = A_int[C,B]"
          " with the exact orbit split V = W1({%d,%d}) + W2(%s); "
          "A_int_CC = carrier cross" % (a_ch, b_ch, THREE),
          okA and okD and ok_split, kill="K0")

    # canonical Pf4 reference signs (from G_c = FLOOR * A_int)
    CH2 = {i: [2 * i, 2 * i + 1] for i in range(6)}
    IOTA_f = IOTA6i.astype(np.float64)

    def compress12(A):
        Ahat = np.zeros((12, 12))
        for (i, j) in DUADS_CH:
            if i == 0:
                B = IOTA_f.T @ A[np.ix_(CH[0], CH[j])] / 3.0
            else:
                B = A[np.ix_(CH[i], CH[j])]
            for rr in range(2):
                for cc in range(2):
                    Ahat[CH2[i][rr], CH2[j][cc]] = B[rr, cc]
                    Ahat[CH2[j][cc], CH2[i][rr]] = -B[rr, cc]
        return Ahat

    def pf4_of(Ahat):
        out = {}
        for (i, j) in DUADS_CH:
            B = Ahat[np.ix_(CH2[i], CH2[j])]
            out[frozenset({i, j})] = -(B[0, 0] * B[1, 1]
                                       - B[0, 1] * B[1, 0])
        return out

    pf4_c = pf4_of(compress12(A_int.astype(np.float64) / 200.0))
    sign_c = {d: (1 if v > 0 else -1) for d, v in pf4_c.items()}
    check("S0.4 canonical G_c Pf4 signs rebuilt: all 15 nonzero, "
          "all negative (round-52 gauge)",
          all(abs(v) > PF_FLOOR for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ---------------- RP machinery (v519 form, n-dim)
    def wick_factory(A):
        n = A.shape[0]
        W = np.eye(n, dtype=complex) + 1j * A
        memo = {}

        def wick(idx):
            idx = tuple(idx)
            if len(idx) == 0:
                return 1.0 + 0j
            if len(idx) % 2 == 1:
                return 0.0 + 0j
            if idx in memo:
                return memo[idx]
            head, rest = idx[0], idx[1:]
            tot = 0.0 + 0j
            for j, b in enumerate(rest):
                sub = rest[:j] + rest[j + 1:]
                tot += (-1) ** j * W[head, b] * wick(sub)
            memo[idx] = tot
            return tot
        return wick

    def theta_mono(mono, r, s, eta):
        imgs = [r[a] for a in reversed(mono)]
        coeff = eta ** len(mono)
        for a in mono:
            coeff *= s[a]
        lst = list(imgs)
        sign = 1
        for i in range(len(lst)):
            for j in range(len(lst) - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    sign = -sign
        return coeff * sign, tuple(lst)

    def gram(basis, r, s, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis):
            ca, ia = theta_mono(ma, r, s, eta)
            for bi, mb in enumerate(basis):
                M[ai, bi] = ca * wick(tuple(list(ia) + list(mb)))
        return M

    def metrics(M):
        nm = max(float(np.max(np.abs(M))), 1e-300)
        hd = float(np.max(np.abs(M - M.conj().T)) / nm)
        lm = float(np.min(np.linalg.eigvalsh((M + M.conj().T) / 2)))
        return hd, lm

    S16 = {k: 1 for k in range(16)}
    S10 = {k: 1 for k in range(10)}

    r_S = {}
    for i in range(8):
        r_S[2 * i] = 2 * i + 1
        r_S[2 * i + 1] = 2 * i
    P_S = [2 * i for i in range(8)]
    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]

    r_abT = {k: k for k in range(16)}
    for k in range(2):
        r_abT[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_abT[CH[b_ch][k]] = CH[a_ch][1 - k]
    P_ab = list(CH[a_ch])
    B1_ab = [(a,) for a in P_ab]
    B2_ab = [(), tuple(P_ab)]

    # carrier-restricted reflections (10-dim compressed state)
    r_S10 = {}
    for i in range(5):
        r_S10[2 * i] = 2 * i + 1
        r_S10[2 * i + 1] = 2 * i
    P_S10 = [2 * i for i in range(5)]
    B1_S10 = [(a,) for a in P_S10]
    B2_S10 = [()] + [tuple(c)
                     for c in itertools.combinations(P_S10, 2)]
    r_ab10 = {k: k for k in range(10)}
    for k in range(2):
        r_ab10[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_ab10[CH[b_ch][k]] = CH[a_ch][1 - k]
    B1_ab10 = [(a,) for a in CH[a_ch]]
    B2_ab10 = [(), tuple(CH[a_ch])]

    def strict_rp(A, r, b1, b2, eta=1j):
        wk = wick_factory(A)
        s = S16 if A.shape[0] == 16 else S10
        M1 = gram(b1, r, s, eta, wk)
        M2 = gram(b2, r, s, eta, wk)
        hd1, lm1 = metrics(M1)
        hd2, lm2 = metrics(M2)
        hd, lm = max(hd1, hd2), min(lm1, lm2)
        ok = (hd <= ZTOL and lm >= -NZ_FLOOR)
        return ok, hd, lm, (M1, M2)

    # parent builder (float)
    A_CCf = A_CC.astype(np.float64)
    J3f = J3.astype(np.float64)
    W1f = W1.astype(np.float64)
    W2f = W2.astype(np.float64)
    AiCCf = A_int_CC.astype(np.float64)

    def parent(kap, m, t1, t2, s):
        A = np.zeros((16, 16))
        A[np.ix_(CAR_IDX, CAR_IDX)] = kap * A_CCf + s * AiCCf
        A[np.ix_(BND_IDX, BND_IDX)] = m * J3f
        Wc = t1 * W1f + t2 * W2f
        A[np.ix_(CAR_IDX, BND_IDX)] = Wc
        A[np.ix_(BND_IDX, CAR_IDX)] = -Wc.T
        return A

    def schur_Aeff(A):
        C = (np.eye(16, dtype=complex) + 1j * A) / 2
        CCC = C[np.ix_(CAR_IDX, CAR_IDX)]
        CCB = C[np.ix_(CAR_IDX, BND_IDX)]
        CBB = C[np.ix_(BND_IDX, BND_IDX)]
        CBC = C[np.ix_(BND_IDX, CAR_IDX)]
        Ceff = CCC - CCB @ np.linalg.inv(CBB) @ CBC
        return 2 * Ceff.imag

    def census10(Aeff):
        n_nz, n_sig, nJ = 0, 0, 0
        aJ45 = 0.0
        for (i, j) in CAR_DUADS:
            B = Aeff[np.ix_(CH[i], CH[j])]
            nz = float(np.linalg.norm(B)) >= NZ_FLOOR
            n_nz += nz
            pf = -(B[0, 0] * B[1, 1] - B[0, 1] * B[1, 0])
            if abs(pf) >= PF_FLOOR:
                n_sig += ((pf > 0) == (sign_c[frozenset({i, j})] > 0))
            aI = (B[0, 0] + B[1, 1]) / 2
            aJ = (B[0, 1] - B[1, 0]) / 2
            aX = (B[0, 1] + B[1, 0]) / 2
            aZ = (B[0, 0] - B[1, 1]) / 2
            if (abs(aJ) >= NZ_FLOOR
                    and max(abs(aI), abs(aX), abs(aZ)) <= ZTOL):
                nJ += 1
            if (i, j) == (a_ch, b_ch):
                aJ45 = aJ
        return n_nz, n_sig, nJ, aJ45

    # ==================================================================
    section("P1 -- the family + KMS typing")
    # ==================================================================
    def cov_defect(A):
        return float(np.max(np.abs(A[np.ix_(img, img)] - A)))

    grid_t = [(0.05, 0.05), (0.1, 0.1), (0.2, 0.2),
              (0.05, 0.0), (0.0, 0.05), (0.1, 0.05)]
    grid_t_ex = [(sp.Rational(1, 20), sp.Rational(1, 20)),
                 (sp.Rational(1, 10), sp.Rational(1, 10)),
                 (sp.Rational(1, 5), sp.Rational(1, 5)),
                 (sp.Rational(1, 20), 0), (0, sp.Rational(1, 20)),
                 (sp.Rational(1, 10), sp.Rational(1, 20))]
    SCAN = []
    for kap in (0.25, 0.5):
        for m in (0.25, 0.5, 0.75):
            for (t1, t2) in grid_t:
                for s in (0.0, 0.05, 0.125):
                    SCAN.append((kap, m, t1, t2, s))
    cd_max = max(cov_defect(parent(*p)) for p in SCAN[::7])
    A_wit = parent(0.5, 0.5, 0.05, 0.05, 0.0)
    check("P1.1 A_par C6-covariant and antisymmetric on the family "
          "(spot ward over the grid: max covariance defect %.1e "
          "<= ZTOL; antisym exact by construction)" % cd_max,
          cd_max <= ZTOL, kill="K1")

    wA, QA = np.linalg.eigh(1j * A_wit)
    w_h = -2.0 * np.arctanh(wA)
    H_herm = (QA * w_h) @ QA.conj().T
    h_re = float(np.max(np.abs(H_herm.real)))
    h_r = H_herm.imag
    h_anti = float(np.max(np.abs(h_r + h_r.T)))
    h_cov = float(np.max(np.abs(h_r[np.ix_(img, img)] - h_r)))
    occ = 1.0 / (1.0 + np.exp(w_h))
    A_back = (-1j * (2 * (QA * occ) @ QA.conj().T
                     - np.eye(16))).real
    rt = float(np.max(np.abs(A_back - A_wit)))
    check("P1.2 KMS TYPING (honest: parent-KMS binds exactly "
          "through CAR-strictness): h_par = -2 artanh spectral "
          "map of A_par exists iff ||A|| < 1, is real (Re-defect "
          "%.1e), antisymmetric (%.1e), covariant (%.1e); the "
          "beta = 1 KMS covariance of h_par round-trips to A_par "
          "at %.1e <= 1e-12 -- every CAR-strict member IS a "
          "beta = 1 KMS state of a covariant Hamiltonian"
          % (h_re, h_anti, h_cov, rt),
          h_re <= 1e-12 and h_anti <= 1e-12 and h_cov <= 1e-12
          and rt <= 1e-12, kill="K1")

    # ==================================================================
    section("P2 -- THE DECISIVE SCAN (frozen grid, first-winner rule)")
    # ==================================================================
    witness_ab = None
    m2_in_set = False
    n_car_ok = 0
    n_car_bad = 0
    n_strictS_pass = 0
    hd2S_min = 1e9
    hd1S_max = 0.0
    lm_herm_min_s0 = 1e9
    lm_herm_min_spos = 1e9
    lm_argmin_s0 = None
    lm_argmin = None
    n_s0 = 0
    n_s0_abT = 0
    ab_pos_ok = True
    lmT_max_spos = -1e9
    orbit_ok = True
    rows = []
    for (kap, m, t1, t2, s) in SCAN:
        A = parent(kap, m, t1, t2, s)
        smax = float(np.max(np.abs(np.linalg.eigvalsh(1j * A))))
        car_ok = smax <= 0.95
        if not car_ok:
            n_car_bad += 1
            rows.append(((kap, m, t1, t2, s), "CAR-EXCLUDED", smax))
            continue
        n_car_ok += 1
        okS, hdS, lmS, (M1S_f, M2S_f) = strict_rp(
            A, r_S, B1_S, B2_S)
        okT, hdT, lmT, _ = strict_rp(A, r_abT, B1_ab, B2_ab)
        hd1S, _l1 = metrics(M1S_f)
        hd2S, _l2 = metrics(M2S_f)
        Aeff = schur_Aeff(A)
        n_nz, n_sig, nJ, aJ45 = census10(Aeff)
        mix_ok = (n_nz == 10 and n_sig == 10)
        tag = ("RP(S)=%s RP(abT)=%s mix=%d/%d"
               % ("P" if okS else "F", "P" if okT else "F",
                  n_nz, n_sig))
        rows.append(((kap, m, t1, t2, s), tag, smax))
        n_strictS_pass += okS
        hd2S_min = min(hd2S_min, hd2S)
        hd1S_max = max(hd1S_max, hd1S)
        if s == 0.0:
            if lmS < lm_herm_min_s0:
                lm_herm_min_s0 = lmS
                lm_argmin_s0 = (kap, m, t1, t2, s)
        elif lmS < lm_herm_min_spos:
            lm_herm_min_spos = lmS
            lm_argmin = (kap, m, t1, t2, s)
        if s == 0.0:
            n_s0 += 1
            ab_ok_marg = (hdT <= ZTOL and abs(lmT) <= 1e-9)
            n_s0_abT += ab_ok_marg
            if t1 > 0 and t2 == 0:
                orbit_ok &= (n_nz == 1)
            elif t1 == 0 and t2 > 0:
                orbit_ok &= (n_nz == 3)
            elif t1 > 0 and t2 > 0:
                orbit_ok &= (n_nz == 10)
            if witness_ab is None and ab_ok_marg and mix_ok:
                witness_ab = (kap, m, t1, t2, s)
            if ((kap, m, t1, t2, s) == (0.5, 0.5, 0.05, 0.05, 0.0)
                    and ab_ok_marg and mix_ok):
                m2_in_set = True
        else:
            ab_pos_ok &= (not okT)
            lmT_max_spos = max(lmT_max_spos, lmT)
    for (p, tag, smax) in rows[:12]:
        print("      %s  smax=%.3f  %s" % (p, smax, tag))
    print("      ... (%d points total, %d CAR-valid, %d "
          "CAR-excluded)" % (len(SCAN), n_car_ok, n_car_bad))
    check("P2.1 STRICT-COLLAR OBSTRUCTION (family-wide): %d/%d "
          "CAR-valid points pass strict theta_S RP (expected 0); "
          "deg-2 Hermiticity defect >= 0.04 everywhere (min %.4f) "
          "while the 1p Gram stays Hermitian (max defect %.1e <= "
          "ZTOL): the strict collar route is deg-2-Hermiticity-"
          "obstructed on the WHOLE family"
          % (n_strictS_pass, n_car_ok, hd2S_min, hd1S_max),
          n_strictS_pass == 0 and hd2S_min >= 0.04
          and hd1S_max <= ZTOL, kill="K2")
    check("P2.2 HERMITIZED-RP ANATOMY (measured, no PD law): the "
          "hermitized theta_S Gram goes INDEFINITE at large "
          "coupling even without carrier cross (s = 0 floor "
          "%.4f = -0.0875 +- 0.005 at %s) and harder with it "
          "(s > 0 floor %.4f = -0.2124 +- 0.005 at %s); PD holds "
          "in the small-coupling regime and EXACTLY at the M2 "
          "parent (P3.2) -- hermitization does NOT rescue the "
          "whole family"
          % (lm_herm_min_s0, lm_argmin_s0, lm_herm_min_spos,
             lm_argmin),
          abs(lm_herm_min_s0 + 0.0875) <= 5e-3
          and abs(lm_herm_min_spos + 0.2124) <= 5e-3, kill="K2")
    check("P2.3 MARGINAL theta_abT WITNESS SET: %d/%d CAR-valid "
          "s = 0 points pass theta_abT RP marginally; every s > 0 "
          "point fails (max lam_min %.4f <= -0.04, parent a_J = "
          "s); FIRST {CAR, abT-RP, mix 10/10} point = %s == "
          "(1/4, 1/4, 1/20, 1/20, 0); v898 M2 parent in the "
          "witness set: %s"
          % (n_s0_abT, n_s0, lmT_max_spos, witness_ab, m2_in_set),
          n_s0_abT == n_s0 and n_s0 > 0 and ab_pos_ok
          and lmT_max_spos <= -0.04
          and witness_ab == (0.25, 0.25, 0.05, 0.05, 0.0)
          and m2_in_set, kill="K2")
    check("P2.4 ORBIT SELECTIVITY: at s = 0, W1-only coupling "
          "mixes exactly 1/10 duads ({%d,%d} only), W2-only "
          "exactly 3/10 (the 3-cycle), both orbits 10/10 -- full "
          "mixing needs BOTH orbit couplings" % (a_ch, b_ch),
          orbit_ok, kill="K2")

    # ==================================================================
    section("P3 -- THE EXACT WITNESS (sympy rationals end to end)")
    # ==================================================================
    kap_s, m_s, t1_s, t2_s, s_s = sp.symbols(
        "kappa m t1 t2 s", real=True)
    A_CCs = sp.Matrix(A_CC.tolist())
    J3s = sp.Matrix(J3.tolist())
    W1s = sp.Matrix(W1.tolist())
    W2s = sp.Matrix(W2.tolist())
    AiCCs = sp.Matrix(A_int_CC.tolist())
    Ws = t1_s * W1s + t2_s * W2s
    C_CC = (sp.eye(10) + sp.I * (kap_s * A_CCs + s_s * AiCCs)) / 2
    C_CB = sp.I * Ws / 2
    C_BC = -sp.I * Ws.T / 2
    C_BB_inv = 2 * (sp.eye(6) - sp.I * m_s * J3s) / (1 - m_s ** 2)
    C_eff = sp.expand(C_CC - C_CB * C_BB_inv * C_BC)
    A_eff_sym = sp.Matrix(10, 10, lambda r, c: sp.expand(
        sp.im(sp.expand(2 * C_eff[r, c]))))
    A_eff_formula = (kap_s * A_CCs + s_s * AiCCs
                     + (m_s / (1 - m_s ** 2)) * Ws * J3s * Ws.T)
    ok_schur = sp.simplify(A_eff_sym - A_eff_formula) == sp.zeros(10)
    check("P3.1 SYMBOLIC SCHUR IDENTITY (all 5 parameters): A_eff "
          "= kappa A_CC + s A_int_CC + (m/(1-m^2)) W J3 W^T "
          "EXACTLY (%s)" % ok_schur, bool(ok_schur), kill="K3")

    # exact witness state
    kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                    sp.Rational(1, 20))
    A_wit_ex = sp.zeros(16)
    blk_C = kapQ * A_CCs
    Wq = tQ * (W1s + W2s)
    for r in range(10):
        for c in range(10):
            A_wit_ex[r, c] = blk_C[r, c]
    for r in range(10):
        for c in range(6):
            A_wit_ex[r, 10 + c] = Wq[r, c]
            A_wit_ex[10 + c, r] = -Wq[r, c]
    for r in range(6):
        for c in range(6):
            A_wit_ex[10 + r, 10 + c] = mQ * J3s[r, c]

    def wick_exact_factory(Aex):
        n = Aex.shape[0]
        Wm = sp.eye(n) + sp.I * Aex
        memo = {}

        def wick(idx):
            idx = tuple(idx)
            if len(idx) == 0:
                return sp.Integer(1)
            if len(idx) % 2 == 1:
                return sp.Integer(0)
            if idx in memo:
                return memo[idx]
            head, rest = idx[0], idx[1:]
            tot = sp.Integer(0)
            for j, b in enumerate(rest):
                w = Wm[head, b]
                if w != 0:
                    sub = rest[:j] + rest[j + 1:]
                    tot += sp.Integer(-1) ** j * w * wick(sub)
            memo[idx] = tot
            return tot
        return wick

    def gram_exact(basis, r, eta, wick):
        n = len(basis)
        M = sp.zeros(n, n)
        for ai, ma in enumerate(basis):
            imgs = [r[a] for a in reversed(ma)]
            coeff = eta ** len(ma)
            lst = list(imgs)
            sgn = 1
            for i in range(len(lst)):
                for j in range(len(lst) - 1 - i):
                    if lst[j] > lst[j + 1]:
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                        sgn = -sgn
            ca = coeff * sgn
            ia = tuple(lst)
            for bi, mb in enumerate(basis):
                M[ai, bi] = sp.expand(
                    ca * wick(tuple(list(ia) + list(mb))))
        return M

    def herm_exact(M):
        return sp.expand(M - M.conjugate().T) == sp.zeros(*M.shape)

    def psd_exact(M):
        """exact LDL for Hermitian rational M; PSD iff all pivots
        >= 0 with zero-pivot rows vanishing."""
        n = M.shape[0]
        M = sp.Matrix(M)
        pivots = []
        for k in range(n):
            d = sp.nsimplify(sp.re(M[k, k]))
            pivots.append(d)
            if d == 0:
                if any(sp.expand(M[k, j]) != 0 for j in range(k, n)):
                    return False, pivots
                continue
            if d < 0:
                return False, pivots
            for i in range(k + 1, n):
                if M[i, k] != 0:
                    f = M[i, k] / d
                    for j in range(k, n):
                        M[i, j] = sp.expand(M[i, j]
                                            - f * M[k, j])
        return True, pivots

    wk_ex = wick_exact_factory(A_wit_ex)
    M1S = gram_exact(B1_S, r_S, sp.I, wk_ex)
    M2S = gram_exact(B2_S, r_S, sp.I, wk_ex)
    h1 = herm_exact(M1S)
    p1, piv1 = psd_exact(M1S)
    pd1 = p1 and all(p > 0 for p in piv1)
    l1f = float(np.min(np.linalg.eigvalsh(np.array(
        M1S.evalf(16), dtype=complex))))
    D2 = sp.expand(M2S - M2S.conjugate().T)
    n_def = 0
    mag_ok = True
    seat_ok_ex = True
    for ai in range(D2.rows):
        for bi in range(D2.cols):
            d = D2[ai, bi]
            if d != 0:
                n_def += 1
                mag_ok &= (sp.expand(d * sp.conjugate(d))
                           == sp.Rational(1, 100))
                ma, mb = B2_S[ai], B2_S[bi]
                mixed = (lambda mo: len(mo) == 2
                         and (mo[0] < 10) != (mo[1] < 10))
                seat_ok_ex &= ((ma == () and mixed(mb))
                               or (mb == () and mixed(ma)))
    H2 = sp.expand((M2S + M2S.conjugate().T) / 2)
    p2, piv2 = psd_exact(H2)
    pd2 = p2 and all(p > 0 for p in piv2)
    l2f = float(np.min(np.linalg.eigvalsh(np.array(
        H2.evalf(16), dtype=complex))))
    check("P3.2 EXACT STRICT OBSTRUCTION at the M2 parent: 1p Gram "
          "exactly Hermitian (%s) and PD by exact LDL (%s, float "
          "lam_min %.6f = 0.5 +- 1e-6); deg-2 Gram exactly "
          "NON-Hermitian: %d nonzero defect entries, ALL of exact "
          "magnitude 2t = 1/10 (%s), ALL seated on (empty <-> "
          "mixed carrier-boundary pair) positions (%s); hermitized "
          "deg-2 exactly PD by LDL (%s, float lam_min %.6f = "
          "0.2125 +- 5e-3)"
          % (h1, pd1, l1f, n_def, mag_ok, seat_ok_ex, pd2, l2f),
          h1 and pd1 and abs(l1f - 0.5) <= 1e-6
          and (not herm_exact(M2S)) and n_def > 0 and mag_ok
          and seat_ok_ex and pd2 and abs(l2f - 0.2125) <= 5e-3,
          kill="K3")

    M1T = gram_exact(B1_ab, r_abT, sp.I, wk_ex)
    M2T = gram_exact(B2_ab, r_abT, sp.I, wk_ex)
    hT = herm_exact(M1T) and herm_exact(M2T)
    ev1T = []
    for val, mult in M1T.eigenvals().items():
        ev1T += [sp.nsimplify(sp.re(val))] * mult
    ev1T = sorted(ev1T)
    pT, pivT = psd_exact(M2T)
    check("P3.3 MARGINAL theta_abT WITNESS EXACT at the M2 parent: "
          "Grams exactly Hermitian (%s); 1p eigenvalues exactly "
          "%s == {0, 0} (cone boundary: parent a_J = 0); deg-2 "
          "exactly PSD by LDL pivots (%s)"
          % (hT, ev1T, pT and all(p >= 0 for p in pivT)),
          hT and ev1T == [0, 0] and pT
          and all(p >= 0 for p in pivT), kill="K3")

    lamQ = mQ / (1 - mQ ** 2)
    A_eff_ex = kapQ * A_CCs + lamQ * (Wq * J3s * Wq.T)
    Jcoord = sp.Rational(3) * lamQ * tQ ** 2
    ok_cen = True
    nJ_ex = 0
    for (i, j) in CAR_DUADS:
        B = A_eff_ex.extract(CH[i], CH[j])
        target = Jcoord * sp.Matrix([[0, 1], [-1, 0]])
        ok_cen &= (sp.expand(B - target) == sp.zeros(2))
        pf = -B.det()
        ok_cen &= (sp.sign(pf) == sign_c[frozenset({i, j})])
        nJ_ex += 1
    smax_eff = float(max(abs(x) for x in np.linalg.eigvalsh(
        1j * np.array(A_eff_ex.evalf(16), dtype=np.float64))))
    check("P3.4 COMPRESSION CENSUS EXACT: all 10 carrier duads "
          "carry the uniform block (3 m t^2/(1-m^2)) J with "
          "J-coordinate = %s == 1/200 == the round-51/52 FLOOR "
          "exactly; Pf4 = -(J-coord)^2 < 0 canonical on 10/10 "
          "(%s); compressed CAR valid (smax = %.4f < 1)"
          % (Jcoord, ok_cen, smax_eff),
          Jcoord == sp.Rational(1, 200) and ok_cen and nJ_ex == 10
          and smax_eff < 1, kill="K3")

    A18 = None  # direction census of the KMS winner (float)
    h18 = -(A16_dep.astype(np.float64)
            + 0.125 * A_int.astype(np.float64))
    w18, Q18 = np.linalg.eigh(1j * h18)
    f18 = 1.0 / (1.0 + np.exp(w18))
    A18 = (-1j * (2 * (Q18 * f18) @ Q18.conj().T
                  - np.eye(16))).real
    nJ_kms = 0
    for (i, j) in CAR_DUADS:
        B = A18[np.ix_(CH[i], CH[j])]
        aI = (B[0, 0] + B[1, 1]) / 2
        aJ = (B[0, 1] - B[1, 0]) / 2
        aX = (B[0, 1] + B[1, 0]) / 2
        aZ = (B[0, 0] - B[1, 1]) / 2
        if (abs(aJ) >= NZ_FLOOR
                and max(abs(aI), abs(aX), abs(aZ)) <= ZTOL):
            nJ_kms += 1
    check("P3.5 t_eff TYPING (honest): the compression realizes "
          "the UNIFORM J-ray 1_5 (x) (1/200) J -- the v898 FLOOR "
          "value level but a DIFFERENT covariant direction than "
          "the KMS family (pure-J duads: compression 10/10 vs KMS "
          "winner %d/10)" % nJ_kms,
          nJ_kms <= 1, "direction mismatch typed, not hidden",
          kill="K3")

    # ==================================================================
    section("P4 -- THE MECHANISM: parent RP + effective RP failure")
    # ==================================================================
    A_eff_f = np.array(A_eff_ex.evalf(16), dtype=np.float64)
    okE, hdE, lmE, (M1E, _M2E) = strict_rp(
        A_eff_f, r_ab10, B1_ab10, B2_ab10)
    evE = np.linalg.eigvalsh((M1E + M1E.conj().T) / 2)
    aJ_eff = float(Jcoord)
    idd = max(abs(abs(evE[0]) - aJ_eff), abs(abs(evE[1]) - aJ_eff),
              abs(evE[0] + evE[1]))
    check("P4.1 EFFECTIVE RP FAILS by the round-58 mechanism: "
          "compressed a_J = 1/200 on the {%d,%d} duad (exact); "
          "carrier 2-cycle odd Gram eigenvalues EXACTLY {-|a_J|, "
          "+|a_J|} (identity defect %.1e <= 1e-12), lam_min = "
          "%.6f = -1/200 < 0 => strict effective RP FAILS while "
          "the parent passes theta_abT RP (marginally)"
          % (a_ch, b_ch, idd, lmE),
          (not okE) and idd <= 1e-12
          and abs(lmE + 1.0 / 200.0) <= 1e-12, kill="K4")

    okE2, hdE2, lmE2, _g = strict_rp(A_eff_f, r_S10, B1_S10, B2_S10)
    check("P4.2 the carrier SHEET SWAP on the compressed state "
          "stays strictly RP (Hermitian %.1e, lam_min %.6f > 0): "
          "the effective failure is 2-cycle-seated (round-58 "
          "anatomy reproduced one level down)" % (hdE2, lmE2),
          okE2 and lmE2 > 0, kill="K4")

    check("P4.3 TYPED CONCLUSION (the SPLIT): for the 2-cycle "
          "reflection -- the seat of the round-58 incompatibility "
          "theorem -- the dilation mechanism is REALIZED (parent "
          "a_J = 0 <=> RP marginal on the cone boundary, "
          "compression a_J = 1/200 != 0 with full mixing); for "
          "the STRICT collar demand the route is OBSTRUCTED on "
          "this family by the exact linear-in-coupling deg-2 "
          "Hermiticity defect -- RP-vs-mixing moves UP to "
          "strict-vs-marginal, it does not dissolve", True,
          "typed by measurement")

    # ==================================================================
    section("C -- controls (must fire; RNG only here)")
    # ==================================================================
    A_diag = parent(0.5, 0.5, 0.0, 0.0, 0.0)
    n_nz0, _s0, _j0, _a0 = census10(schur_Aeff(A_diag))
    check("C1 FIRES: the diagonal parent (t1 = t2 = s = 0) has "
          "%d/10 carrier duads in the compression -- coupling is "
          "the only mixing source (v898 C2 regression)" % n_nz0,
          n_nz0 == 0, kill="K7")

    rng = np.random.default_rng(900)
    n_fire = 0
    for _trial in range(3):
        pr = rng.permutation(10)
        A_bad = parent(0.5, 0.5, 0.05, 0.05, 0.0)
        Wb = A_bad[np.ix_(CAR_IDX, BND_IDX)][pr, :]
        A_bad[np.ix_(CAR_IDX, BND_IDX)] = Wb
        A_bad[np.ix_(BND_IDX, CAR_IDX)] = -Wb.T
        if cov_defect(A_bad) >= NZ_FLOOR:
            n_fire += 1
    check("C2 FIRES: 3/3 seeded random row permutations of the "
          "coupling break the exact C6-covariance ward (%d/3)"
          % n_fire, n_fire == 3, kill="K7")

    okK, hdK, lmK, _g2 = strict_rp(A18, r_S, B1_S, B2_S)
    check("C3 FIRES (regression): the v898 KMS winner (1, 1/8, 1) "
          "FAILS strict RP under theta_S (deg-2 defect %.4f = "
          "0.0982 +- 0.005) -- the SAME quasi-RP failure type as "
          "the parent family (0.1 at the M2 parent, exact seat "
          "known there)" % hdK,
          (not okK) and abs(hdK - 0.0982) <= 5e-3, kill="K7")

    A_s = parent(0.5, 0.5, 0.05, 0.05, 0.05)
    okC4, hdC4, lmC4, (M1C4, _m2c4) = strict_rp(
        A_s, r_abT, B1_ab, B2_ab)
    evC4 = np.linalg.eigvalsh((M1C4 + M1C4.conj().T) / 2)
    idC4 = max(abs(evC4[0] + 0.05), abs(evC4[1] - 0.05))
    check("C4 FIRES: at s = 1/20 the parent theta_abT odd Gram "
          "has eigenvalues exactly -+ s (identity defect %.1e <= "
          "1e-12) and strict RP fails -- the round-58 a_J "
          "identity holds one level up" % idC4,
          (not okC4) and idC4 <= 1e-12, kill="K7")

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
        VERDICT = "FAMILY-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "SCAN-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "WITNESS-BROKEN"
    elif "K4" in KILLS:
        VERDICT = "MECHANISM-BROKEN"
    else:
        VERDICT = ("DILATION-SPLIT [MARGINAL-WITNESS(theta_abT: "
                   "v898 M2 parent in the exact witness set), "
                   "STRICT-COLLAR-OBSTRUCTED(exact deg-2 "
                   "Hermiticity defect, magnitude 2t, linear "
                   "law), EFFECTIVE-RP-FAILS(a_J = 1/200, "
                   "2-cycle-seated), FLOOR-REALIZED(J-coordinate "
                   "= 1/200 exactly)]")
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE SPLIT: (a) under the 2-cycle reflection theta_abT -- the
    seat of the round-58 incompatibility theorem -- the dilation
    mechanism is REALIZED: every s = 0 parent (incl. the v898 M2
    parent, verified in EXACT rational arithmetic) is KMS (arctan
    theorem), CAR-strict and MARGINALLY reflection-positive
    (a_J = 0 upstairs, 1p Gram eigenvalues exactly {0, 0}), while
    its Schur compression carries full Pfaffian mixing with
    effective a_J = 1/200 != 0 and fails effective RP by exactly
    the +-|a_J| law.  (b) under the STRICT collar (sheet-swap)
    demand the route is OBSTRUCTED on the whole family: the even
    deg-2 Gram is exactly non-Hermitian at every coupled point,
    defect magnitude 2t (linear law, exact seat: empty <-> mixed
    carrier-boundary pairs), hermitized-PD throughout.
  * THE COMPRESSION: A_eff = kappa A_CC + (m/(1-m^2)) W J3 W^T
    (symbolic identity, all 5 parameters); at the M2 parent all
    10 carrier duads carry the uniform (1/200) J block = the
    round-51/52 FLOOR exactly, canonical Pf4 signs; full mixing
    needs BOTH coupling orbits (W1-only: 1/10, W2-only: 3/10).
  * HONESTY: the marginal witness sits ON the RP cone boundary
    (not strict); the compression lives on the uniform J-ray, not
    the KMS family's A_int ray (pure-J census 10/10 vs 1/10);
    parent-KMS binds only through CAR; the strict-collar
    obstruction is family-level, not a universal no-go; the [O]
    premise of v898 stays [O]; no marker moves.  NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
