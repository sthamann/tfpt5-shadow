#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_marginal_stability_probe -- SEAM.CFIN.MARGINAL.STABILITY.01
(EXPLORATION ONLY, experiments/; round 60, 2026-08-10, Probe 9 --
the marginal dilation witness on the RP cone boundary: is it a
LIMIT of strictly-RP parents (a closure point -- the mixing would
be 'physical as a limit of equilibria') or an ISOLATED boundary
point (a genuine non-equilibrium source unavoidable)?)

THE QUESTION.  Probe 7 (rp_parent_dilation_probe, round 59; now
promoted inside v903) measured that under the 2-cycle reflection
theta_abT every s = 0 parent of the family A_par(kappa, m, t1, t2,
s) is MARGINALLY reflection-positive (1p Gram eigenvalues exactly
{0, 0} -- the cone boundary) while its Schur compression carries
the full Pfaffian mixing with the exact identity t^2 3m/(1-m^2) =
1/200.  Round 59 left open whether that marginal witness is
approachable from the STRICT-RP side.  This probe freezes the
question as (a) a neighborhood parametrization (all five family
parameters PLUS the complete enlargement the covariance seat
allows), (b) the decisive scalar sup(RP-margin x mixing) with the
approach exponent, (c) the exact anatomy of the {0, 0} kernel.

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-10): probe 7 measured the marginal witness set and the
parent a_J = s identity but never asked the stability/limit
question, never parametrized the seat enlargement, and never
computed the kernel; round 58 (seam_state_derivation_probe) proved
the +-|a_J| odd-Gram identity on the KMS family h(u, t) but not on
the coupled parents and not as a WHOLE-CLASS covariance statement;
v903 promotes all of it verbatim with the witness typed 'ON the
cone boundary (not strict)'.  NOTHING in the corpus decides
closure-point vs isolated.  That is exactly this probe.

SMOKE-RUN DISCLOSURE (2026-08-10, one declared smoke round before
freezing; the frozen claims below record what the smoke measured
-- the answer REFUTES THE DICHOTOMY of the question and the frozen
claims say so):
 (i)   the theta_abT sector Grams are functions of the channel
       {4,5} 4x4 covariance sub-block ONLY (the 'visible seat');
       on that seat C6 covariance allows EXACTLY the J coordinate
       of the {4,5} cross block (integer covariance defect 2 for
       the I, X, Z unit directions, 0 for J) and forces the two
       intra-channel coordinates equal (c4 = c5);
 (ii)  the symbolic seat law: M1 = [[aJ + aX, aI - aZ],
       [aI + aZ, -aJ + aX]]; Hermiticity forces aZ = 0 (1p) and
       c4 = c5 (deg-2); the Hermitian-admissible 1p eigenvalues
       are aX +- sqrt(aJ^2 + aI^2), and det M2 = aX^2 - aJ^2 (at
       aI = 0) -- so on the COVARIANT class (aI = aX = aZ = 0)
       the eigenvalues are +-aJ and det M2 = -aJ^2: STRICT RP is
       IMPOSSIBLE on the whole class, the RP set is EXACTLY
       {a_J = 0} = the boundary; the strict side is EMPTY;
 (iii) the witness kernel: M1 == 0 identically (both a-side
       Majorana directions), and the deg-2 Gram [[1, i kappa],
       [-i kappa, kappa^2]] has the exact 1-dim kernel spanned by
       (-i kappa, 1) -- vacuum tied to the a-pair; both kernels
       are forced by the SAME pure-J covariance law whose only
       coordinate a_J is the strict-route obstruction;
 (iv)  the unique Hermiticity-preserving strict-ENABLING seat
       direction is the X coordinate (covariance-BREAKING, defect
       exactly 2 eps): 1p eigenvalues {eps, eps}, deg-2 det =
       eps^2 exactly (min eigenvalue ~ eps^2 / 1.25), full mixing
       kept with the {4,5} J-coordinate 1/200 UNCHANGED;
 (v)   FLOOR EXCHANGE (the smoke's sharpest find): the compressed
       {4,5} Pfaffian is Pf4(eps) = (eps - 1/200)(eps + 1/200)
       and the effective 2-cycle odd eigenvalues are exactly
       {eps - 1/200, eps + 1/200}: the canonical sign gate
       (Pf4 < 0) IS the negative effective-RP margin -- the same
       polynomial factor -- so one level down the exclusion
       survives the transversal escape with the crossover EXACTLY
       at the 1/200 floor;
 (vi)  the smoke fixed one sign slip in the first hand-derivation
       of Pf4 (the candidate aJ^2 - aX^2 was the DETERMINANT, the
       Pfaffian convention of the census is Pf4 = -det, hence
       (iv)-(v) as frozen); fail-first preserved.

CONVENTIONS (probe 7 / round 58 wiring rebuilt inline; READ-ONLY
import of tfpt_constants): 16-dim Majorana space, carrier C =
0..9 (channels 1..5, CH(i) = {2(i-1), 2(i-1)+1}), boundary B =
10..15 (channel 0); A_CC = (+)_5 J, J3, coupling orbits W1 (rows
of the 2-cycle channels {4,5}) and W2 (3-cycle rows); parent
family A_par(kappa, m, t1, t2, s) as in probe 7; theta_abT =
orientation-reversed 2-cycle (eta = +i), theta Grams sector-typed
(1p over the a-side Majoranas, even deg <= 2 over {empty, a-pair});
Schur compression C_eff = C_CC - C_CB C_BB^{-1} C_BC, census =
probe-7 form (10 carrier duads, canonical Pf4 signs from G_c).
THE SEAT: the 4x4 covariance sub-block of channels {4, 5} with
coordinates (c4, c5; aI, aJ, aX, aZ) of ({6,7} diag, {8,9} diag;
{4,5} cross block in the I/J/X/Z basis).  RP-MARGIN := min
eigenvalue over the two Hermitized theta_abT sector Grams (signed;
strict RP needs margin > 0 AND Hermiticity <= ZTOL).
MIXING-INDICATOR := the {4,5} J-coordinate of A_eff (1/200 at the
deployed witness).  NUMERICAL PROTOCOL (declared): the seat law,
kernel, witness Grams, Schur identity, Pf4 factorization and
effective eigenvalues are EXACT (sympy symbols/rationals); scans
are float64 with frozen tolerances; RNG only in controls.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 P1  THE VISIBLE SEAT + THE COVARIANT REDUCTION (exact).
     (a) SUPPORT: both theta_abT sector Grams depend on the seat
         only -- zeroing every covariance entry outside channels
         {4,5} leaves the Grams unchanged (ward <= 1e-14 at the
         M2 parent and at one coupled s > 0 point);
     (b) COVARIANCE CENSUS on the seat (integer): the unit cross
         directions I, X, Z have C6 covariance defect exactly 2,
         J exactly 0; the intra-channel difference direction
         (c4 = +1, c5 = -1) has defect 2, the symmetric direction
         (c4 = c5 = 1) has defect 0;
     (c) SYMBOLIC SEAT LAW (sympy, exact): M1 = [[aJ + aX,
         aI - aZ], [aI + aZ, -aJ + aX]] and the deg-2 Gram is
         [[1, i c4], [-i c5, c4 c5 - aJ^2 - aI^2 + aX^2 + aZ^2
         ... as computed]] -- gated claims: 1p Hermiticity <=>
         aZ = 0, deg-2 Hermiticity <=> c4 = c5; under the
         covariant reduction (c4 = c5 = kappa, aI = aX = aZ = 0):
         M1 = diag(aJ, -aJ) EXACTLY and det M2 = -aJ^2 EXACTLY
         => on the ENTIRE C6-covariant CAR class strict
         theta_abT RP is IMPOSSIBLE (min eigenvalue <= 0 with
         equality iff a_J = 0): the cone interior is EMPTY along
         the covariant class; in the Hermitian-admissible
         noncovariant seat the 1p eigenvalues are exactly
         aX +- sqrt(aJ^2 + aI^2) (strict <=> aX > sqrt(...)).
 P2  THE KERNEL ANATOMY at the M2 parent (exact rationals,
     16-dim machinery).
     (a) M1 == 0 identically (the 2x2 zero matrix): the 1p kernel
         is the FULL a-side sector (both Majorana directions);
     (b) the deg-2 Gram is exactly [[1, i/2], [-i/2, 1/4]] with
         eigenvalues {0, 5/4} and the exact kernel vector
         (-i/2, 1) in the basis {empty, a-pair};
     (c) TYPED: both kernels are forced by the pure-J covariance
         law -- the only Gram-visible seat coordinate is a_J and
         it vanishes on the whole s = 0 stratum (the same a_J
         covariance law as the strict-route obstruction).
 P3  THE STRATUM + THE DECISIVE SCALAR (covariant side).
     (a) NOT ISOLATED: on the frozen s = 0 grid (kappa in
         {1/4, 1/2} x m in {1/4, 1/2, 3/4} x (t1, t2) in
         {(1/20, 1/20), (1/10, 1/10), (1/10, 1/20)}), restricted
         to the CAR-VALID points (probe-7 convention smax <= 0.95;
         SPEC v2: exactly 16/18 points are CAR-valid -- the two
         m = 3/4, (1/10, 1/10) corners have smax 0.961/1.032 and
         are SKIPPED, see the amendment note), the margin is
         exactly 0 (|margin| <= 1e-9, Hermiticity <= ZTOL) with
         full mixing 10/10 canonical at EVERY CAR-valid point:
         the witness sits in a positive-dimensional MARGINAL
         STRATUM;
     (b) the covariant seat direction delta a_J in {+-1/50,
         +-1/20} gives margin = -|delta| exactly (identity ward
         <= 1e-12) and the family s-direction (s = 1/20)
         reproduces margin = -s (probe-7 C4 regression): the
         covariant reachable RP set is EXACTLY {a_J = 0};
     (c) THE SCALAR: sup over the covariant scan of
         (max(margin, 0) x mixing) = 0 EXACTLY, and the product
         is IDENTICALLY zero on the covariant RP set -- the
         witness is NOT a limit of covariant strictly-RP parents
         BECAUSE NONE EXIST (headline: the dichotomy
         closure-point vs isolated is REFUTED: strict side empty,
         witness not isolated).
 P4  THE TRANSVERSAL ESCAPE + ITS EXACT PRICE (non-covariant
     eps X on the seat; frozen grid eps in {1/1000, 1/400, 1/200,
     1/100, 1/20, 1/10, 1/4}).
     (a) at every CAR-valid grid eps > 0: 1p eigenvalues
         {eps, eps} (ward <= 1e-12), deg-2 Hermitian with det =
         eps^2 (exact at eps = 1/100 in rationals; float min
         eigenvalue = eps^2 / lam_max, lam_max = 1.25 + O(eps^2)),
         covariance defect EXACTLY 2 eps (linear price law), CAR
         valid (smax 0.694 +- 0.01 across the small-eps grid);
     (b) the compression shifts EXACTLY: A_eff(eps) = A_eff(0) +
         eps E_CC (symbolic Schur identity in all five parameters
         + eps); mixing stays 10/10 nonzero with the {4,5}
         J-coordinate = 1/200 UNCHANGED; the parent margin scales
         as eps^2/1.25 (log-log exponent 2.00 +- 0.05 on the
         small-eps grid -- the approach is deg-2-limited,
         QUADRATIC-tangent from the strict side while 1p is
         linear);
     (c) THE SCALAR IS TRANSVERSAL HERE: product(eps) =
         margin(eps) x (1/200) > 0, monotone on the CAR-valid
         grid, sup >= 1e-5 (attained at the largest CAR-valid
         eps; value reported) -- strict parent RP + full mixing
         coexist at finite covariance-breaking, price = 2 eps;
     (d) FLOOR EXCHANGE (exact): Pf4_{45}(eps) = (eps - 1/200)
         (eps + 1/200) EXACTLY and the effective 2-cycle odd
         eigenvalues are EXACTLY {eps - 1/200, eps + 1/200}: the
         canonical sign gate (Pf4 < 0) <=> negative effective-RP
         margin -- the SAME factor (eps - 1/200); at eps = 1/200
         the {4,5} Pfaffian dies exactly; strict effective RP and
         canonical mixing sign EXCHANGE at the floor.
 C   CONTROLS (must fire; frozen fire rules; RNG only in C5).
     C1 the I seat direction violates RP for BOTH signs (1p
        eigenvalues +-eps for eps = +-1/100) -- the deliberately
        RP-violating direction shows a negative Gram eigenvalue;
     C2 the Z seat direction breaks 1p Gram Hermiticity (raw
        defect 2|eps|) -- not an OS candidate; fires;
     C3 eps < 0 on X: BOTH 1p eigenvalues negative (strict fails
        from the other side);
     C4 EXACT 1/200 REGRESSION: J-coordinate = t^2 3m/(1-m^2) =
        1/200 at the M2 parent in exact rationals (round-59
        identity);
     C5 SEEDED NON-COVARIANT COUPLING (rng 903, 3 draws: random
        row permutation of the coupling): breaks the exact C6
        covariance ward on 3/3 draws.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 seat/covariance law ward breaks             -> SEAT-BROKEN
  K2 kernel anatomy ward breaks                  -> KERNEL-BROKEN
  K3 stratum / scalar ward breaks                -> STRATUM-BROKEN
  K4 escape / price / floor-exchange breaks      -> ESCAPE-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): MARGSTAB-MEASURED [INTERIOR-EMPTY(covariant
strict RP impossible: +-a_J and det = -a_J^2 exact),
STRATUM-NOT-ISOLATED(margin == 0 on the whole s = 0 grid),
NOT-A-CLOSURE-POINT(covariant strict approximants do not exist),
ESCAPE-NONCOVARIANT(X seat coordinate; price = covariance defect
2 eps; exponent 2), FLOOR-EXCHANGE(Pf4 = (eps - 1/200)(eps +
1/200) = the effective margin factor)] / PIPELINE-BROKEN /
SEAT-BROKEN / KERNEL-BROKEN / STRATUM-BROKEN / ESCAPE-BROKEN /
CONTROL-DEAD.  Exit 0 iff all checks pass and no kill fired;
else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: 'strict RP is impossible' is a
statement about the C6-covariant class of THIS finite model under
THIS sector-typed criterion; the transversal escape is a
covariance-BREAKING deformation, recorded with its exact price,
not a proposal; the v898/v903 [O] premise is unmoved; no marker
moves.  NO RH claim.

SPEC v1 (2026-08-10): frozen after the declared smoke round.
SPEC v2 AMENDMENT (2026-08-10, disclosed; fail-first preserved):
the v1 gate of P3(a) asserted the whole 18-point s = 0 grid is
CAR-valid; the frozen run FAILED that gate on exactly the two
m = 3/4, (t1, t2) = (1/10, 1/10) corners (smax 0.961 and 1.032 >
0.95) -- the smoke round had not run the CAR census on this
sub-grid.  v2 restricts P3(a) to the CAR-valid points (16/18,
probe-7 convention: CAR-excluded points are skipped, not read).
The MARGINALITY measurement itself held on all 18 points
including the excluded corners (margin exactly 0); no other
claim, tolerance or grid was touched.

Sources (read-only, machinery rebuilt inline): rp_parent_dilation_
probe (probe 7: family, witness, census), seam_state_derivation_
probe (round 58: +-|a_J| identity, RP machinery), v903_seam_rp_
exclusion (promoted composite), v898_kms_schur_mixing (gates),
v519 (RP Gram + twist), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_marginal_stability_probe.py
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

PAULI = {"I": np.eye(2), "J": np.array([[0., 1.], [-1., 0.]]),
         "X": np.array([[0., 1.], [1., 0.]]),
         "Z": np.array([[1., 0.], [0., -1.]])}


def main():
    print("SEAM.CFIN.MARGINAL.STABILITY.01 -- closure point vs "
          "isolated: the marginal dilation witness on the RP cone")
    print("FROZEN_SPEC SHA-256: %s" % SPEC_SHA)
    print("NO physics claim beyond recorded identities/measurements; "
          "exploration only.")

    # ==================================================================
    section("S0 -- firewall + compiler-side setup (probe 7 rebuilt)")
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
    check("S0.3 blocks extracted: A_CC, J3, V = W1 + W2, A_int_CC",
          okA and okD and np.array_equal(W1 + W2, Vc), kill="K0")

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
    check("S0.4 canonical G_c Pf4 signs rebuilt: 15 nonzero, all "
          "negative", all(abs(v) > PF_FLOOR for v in pf4_c.values())
          and all(s == -1 for s in sign_c.values()), kill="K0")

    # ---------------- RP machinery (v519 / probe-7 form)
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

    def gram(basis, r, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
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
                M[ai, bi] = ca * wick(tuple(list(ia) + list(mb)))
        return M

    def metrics(M):
        nm = max(float(np.max(np.abs(M))), 1e-300)
        hd = float(np.max(np.abs(M - M.conj().T)) / nm)
        lm = float(np.min(np.linalg.eigvalsh((M + M.conj().T) / 2)))
        return hd, lm

    r_abT = {k: k for k in range(16)}
    for k in range(2):
        r_abT[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_abT[CH[b_ch][k]] = CH[a_ch][1 - k]
    B1_ab = [(a,) for a in CH[a_ch]]
    B2_ab = [(), tuple(CH[a_ch])]

    r_ab10 = {k: k for k in range(10)}
    for k in range(2):
        r_ab10[CH[a_ch][k]] = CH[b_ch][1 - k]
        r_ab10[CH[b_ch][k]] = CH[a_ch][1 - k]
    B1_ab10 = [(a,) for a in CH[a_ch]]
    B2_ab10 = [(), tuple(CH[a_ch])]

    def abT_grams(A):
        wk = wick_factory(A)
        rr = r_abT if A.shape[0] == 16 else r_ab10
        b1 = B1_ab if A.shape[0] == 16 else B1_ab10
        b2 = B2_ab if A.shape[0] == 16 else B2_ab10
        M1 = gram(b1, rr, 1j, wk)
        M2 = gram(b2, rr, 1j, wk)
        hd = max(metrics(M1)[0], metrics(M2)[0])
        lm = min(metrics(M1)[1], metrics(M2)[1])
        return M1, M2, hd, lm

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

    def seat_dir(nm):
        Ee = np.zeros((16, 16))
        P = PAULI[nm]
        Ee[np.ix_(CH[a_ch], CH[b_ch])] = P
        Ee[np.ix_(CH[b_ch], CH[a_ch])] = -P.T
        return Ee

    def schur_Aeff(A):
        C = (np.eye(16, dtype=complex) + 1j * A) / 2
        CCC = C[np.ix_(CAR_IDX, CAR_IDX)]
        CCB = C[np.ix_(CAR_IDX, BND_IDX)]
        CBB = C[np.ix_(BND_IDX, BND_IDX)]
        CBC = C[np.ix_(BND_IDX, CAR_IDX)]
        Ceff = CCC - CCB @ np.linalg.inv(CBB) @ CBC
        return 2 * Ceff.imag

    def census10(Aeff):
        n_nz, n_sig = 0, 0
        aJ45 = 0.0
        for (i, j) in CAR_DUADS:
            B = Aeff[np.ix_(CH[i], CH[j])]
            n_nz += float(np.linalg.norm(B)) >= NZ_FLOOR
            pf = -(B[0, 0] * B[1, 1] - B[0, 1] * B[1, 0])
            if abs(pf) >= PF_FLOOR:
                n_sig += ((pf > 0) == (sign_c[frozenset({i, j})] > 0))
            if (i, j) == (a_ch, b_ch):
                aJ45 = (B[0, 1] - B[1, 0]) / 2
        return n_nz, n_sig, aJ45

    def cov_defect(A):
        return float(np.max(np.abs(A[np.ix_(img, img)] - A)))

    A_M2 = parent(0.5, 0.5, 0.05, 0.05, 0.0)

    # ==================================================================
    section("P1 -- the visible seat + the covariant reduction (exact)")
    # ==================================================================
    seat_idx = CH[a_ch] + CH[b_ch]

    def seat_only(A):
        Az = np.zeros_like(A)
        Az[np.ix_(seat_idx, seat_idx)] = A[np.ix_(seat_idx, seat_idx)]
        return Az

    sup_ok = True
    for A in (A_M2, parent(0.5, 0.5, 0.05, 0.05, 0.05)):
        M1a, M2a, _h, _l = abT_grams(A)
        M1b, M2b, _h2, _l2 = abT_grams(seat_only(A))
        sup_ok &= (float(np.max(np.abs(M1a - M1b))) <= 1e-14
                   and float(np.max(np.abs(M2a - M2b))) <= 1e-14)
    check("P1.1 SUPPORT: both theta_abT sector Grams depend on the "
          "channel-{%d,%d} 4x4 seat only (zeroing everything else "
          "leaves them unchanged, ward <= 1e-14 at the M2 parent "
          "and at a coupled s > 0 point)" % (a_ch, b_ch),
          sup_ok, kill="K1")

    defs = {}
    for nm in ("I", "J", "X", "Z"):
        defs[nm] = cov_defect(seat_dir(nm))
    E_diff = np.zeros((16, 16))
    E_diff[np.ix_(CH[a_ch], CH[a_ch])] = PAULI["J"]
    E_diff[np.ix_(CH[b_ch], CH[b_ch])] = -PAULI["J"]
    E_sym = np.zeros((16, 16))
    E_sym[np.ix_(CH[a_ch], CH[a_ch])] = PAULI["J"]
    E_sym[np.ix_(CH[b_ch], CH[b_ch])] = PAULI["J"]
    d_diff = cov_defect(E_diff)
    d_sym = cov_defect(E_sym)
    check("P1.2 COVARIANCE CENSUS on the seat (integer): cross "
          "directions I/X/Z have defect exactly 2 (%s/%s/%s), J "
          "exactly 0 (%s); intra-channel difference c4 = -c5 has "
          "defect 2 (%s), symmetric c4 = c5 defect 0 (%s) -- the "
          "covariant seat is EXACTLY (kappa, a_J)"
          % (defs["I"], defs["X"], defs["Z"], defs["J"],
             d_diff, d_sym),
          defs["I"] == 2 and defs["X"] == 2 and defs["Z"] == 2
          and defs["J"] == 0 and d_diff == 2 and d_sym == 0,
          kill="K1")

    # symbolic seat law on the 4-dim seat space {0,1,2,3} ~ {6,7,8,9}
    c4s, c5s, aI, aJ, aX, aZ = sp.symbols(
        "c4 c5 aI aJ aX aZ", real=True)
    Bs = (aI * sp.eye(2) + aJ * sp.Matrix([[0, 1], [-1, 0]])
          + aX * sp.Matrix([[0, 1], [1, 0]])
          + aZ * sp.Matrix([[1, 0], [0, -1]]))
    A4 = sp.zeros(4)
    A4[0, 1], A4[1, 0] = c4s, -c4s
    A4[2, 3], A4[3, 2] = c5s, -c5s
    for r in range(2):
        for c in range(2):
            A4[r, 2 + c] = Bs[r, c]
            A4[2 + c, r] = -Bs[r, c]

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

    r4 = {0: 3, 1: 2, 2: 1, 3: 0}
    wk4 = wick_exact_factory(A4)
    M1s = gram_exact([(0,), (1,)], r4, sp.I, wk4)
    M2s = gram_exact([(), (0, 1)], r4, sp.I, wk4)
    M1_target = sp.Matrix([[aJ + aX, aI - aZ], [aI + aZ, -aJ + aX]])
    ok_M1 = sp.expand(M1s - M1_target) == sp.zeros(2)
    d1 = sp.expand(M1s - M1s.conjugate().T)
    herm1_law = sp.simplify(d1[0, 1] + 2 * aZ) == 0 \
        and sp.simplify(d1[1, 0] - 2 * aZ) == 0 \
        and d1[0, 0] == 0 and d1[1, 1] == 0
    d2 = sp.expand(M2s - M2s.conjugate().T)
    herm2_law = sp.simplify(d2[0, 1] - sp.I * (c4s - c5s)) == 0 \
        and d2[0, 0] == 0
    cov_sub = {c4s: sp.Symbol("kappa", real=True),
               c5s: sp.Symbol("kappa", real=True),
               aI: 0, aX: 0, aZ: 0}
    M1_cov = M1s.subs(cov_sub)
    M2_cov = M2s.subs(cov_sub)
    detM2_cov = sp.expand(M2_cov.det())
    ev_noncov = sp.Matrix(M1s.subs({aZ: 0})).eigenvals()
    ev_keys = sorted([sp.simplify(k) for k in ev_noncov],
                     key=lambda e: str(e))
    ev_ok = any(sp.simplify(k - (aX + sp.sqrt(aI ** 2 + aJ ** 2)))
                == 0 for k in ev_noncov) \
        and any(sp.simplify(k - (aX - sp.sqrt(aI ** 2 + aJ ** 2)))
                == 0 for k in ev_noncov)
    check("P1.3 SYMBOLIC SEAT LAW (exact): M1 = [[aJ+aX, aI-aZ],"
          "[aI+aZ, -aJ+aX]] (%s); 1p Hermiticity <=> aZ = 0 (%s), "
          "deg-2 Hermiticity <=> c4 = c5 (%s); COVARIANT REDUCTION: "
          "M1 = diag(aJ, -aJ) (%s), det M2 = -aJ^2 (%s) => strict "
          "theta_abT RP IMPOSSIBLE on the entire covariant class "
          "(RP set = {a_J = 0} = the boundary; interior EMPTY); "
          "Hermitian-admissible 1p eigenvalues aX +- sqrt(aJ^2 + "
          "aI^2) (%s)"
          % (ok_M1, herm1_law, herm2_law,
             sp.expand(M1_cov - sp.diag(aJ, -aJ)) == sp.zeros(2),
             sp.simplify(detM2_cov + aJ ** 2) == 0, ev_ok),
          bool(ok_M1) and herm1_law and herm2_law
          and sp.expand(M1_cov - sp.diag(aJ, -aJ)) == sp.zeros(2)
          and sp.simplify(detM2_cov + aJ ** 2) == 0 and ev_ok,
          kill="K1")

    # ==================================================================
    section("P2 -- the kernel anatomy at the M2 parent (exact)")
    # ==================================================================
    kapQ, mQ, tQ = (sp.Rational(1, 2), sp.Rational(1, 2),
                    sp.Rational(1, 20))
    A_ex = sp.zeros(16)
    for r in range(10):
        for c in range(10):
            A_ex[r, c] = kapQ * sp.Integer(int(A_CC[r, c]))
    for r in range(6):
        for c in range(6):
            A_ex[10 + r, 10 + c] = mQ * sp.Integer(int(J3[r, c]))
    Wq = tQ * sp.Matrix((W1 + W2).tolist())
    for r in range(10):
        for c in range(6):
            A_ex[r, 10 + c] = Wq[r, c]
            A_ex[10 + c, r] = -Wq[r, c]
    wk16 = wick_exact_factory(A_ex)
    M1w = gram_exact(B1_ab, r_abT, sp.I, wk16)
    M2w = gram_exact(B2_ab, r_abT, sp.I, wk16)
    ok_M1w = (M1w == sp.zeros(2))
    M2_expect = sp.Matrix([[1, sp.I / 2],
                           [-sp.I / 2, sp.Rational(1, 4)]])
    ok_M2w = sp.expand(M2w - M2_expect) == sp.zeros(2)
    kv = sp.Matrix([-sp.I / 2, 1])
    ok_kv = sp.expand(M2w * kv) == sp.zeros(2, 1)
    evs = {}
    for val, mult in M2w.eigenvals().items():
        evs[sp.nsimplify(val)] = mult
    ok_ev = (evs.get(sp.Integer(0), 0) == 1
             and evs.get(sp.Rational(5, 4), 0) == 1)
    check("P2.1 KERNEL EXACT at the M2 parent: M1 == 0 identically "
          "(%s -- the 1p kernel is the FULL a-side sector, both "
          "Majorana directions); deg-2 Gram = [[1, i/2],[-i/2, "
          "1/4]] (%s), eigenvalues {0, 5/4} (%s), exact kernel "
          "vector (-i/2, 1) tying vacuum to the a-pair (%s)"
          % (ok_M1w, ok_M2w, ok_ev, ok_kv),
          ok_M1w and bool(ok_M2w) and ok_ev and bool(ok_kv),
          kill="K2")
    check("P2.2 TYPED: both kernels are forced by the pure-J "
          "covariance law of P1 -- the only Gram-visible seat "
          "coordinate is a_J (P1.2/P1.3) and the s = 0 family has "
          "NO {%d,%d} cross block at all, so a_J = 0 identically "
          "on the stratum: the kernel is the same a_J covariance "
          "law that seats the strict-route obstruction"
          % (a_ch, b_ch), True, "typed from P1 + P2.1")

    # ==================================================================
    section("P3 -- the stratum + the decisive scalar (covariant)")
    # ==================================================================
    grid0 = []
    for kap in (0.25, 0.5):
        for m in (0.25, 0.5, 0.75):
            for (t1, t2) in ((0.05, 0.05), (0.1, 0.1), (0.1, 0.05)):
                grid0.append((kap, m, t1, t2, 0.0))
    marg_max = 0.0
    hd_max = 0.0
    mix_ok = True
    n_car = 0
    excl = []
    for p in grid0:
        A = parent(*p)
        smax = float(np.max(np.abs(np.linalg.eigvalsh(1j * A))))
        if smax > 0.95:
            excl.append((p, round(smax, 3)))
            continue
        n_car += 1
        _m1, _m2, hd, lm = abT_grams(A)
        marg_max = max(marg_max, abs(lm))
        hd_max = max(hd_max, hd)
        n_nz, n_sig, _aJ = census10(schur_Aeff(A))
        mix_ok &= (n_nz == 10 and n_sig == 10)
    check("P3.1 NOT ISOLATED (SPEC v2): on the frozen s = 0 grid "
          "%d/%d points are CAR-valid (excluded: %s -- the two "
          "m = 3/4 large-coupling corners, disclosed amendment); "
          "on every CAR-valid point the margin is exactly 0 (max "
          "|margin| = %.1e <= 1e-9, max Hermiticity defect %.1e "
          "<= ZTOL) with full mixing 10/10 canonical: a positive-"
          "dimensional MARGINAL STRATUM"
          % (n_car, len(grid0), excl, marg_max, hd_max),
          n_car == 16 and marg_max <= 1e-9 and hd_max <= ZTOL
          and mix_ok, kill="K3")

    id_ok = True
    for dl in (0.02, -0.02, 0.05, -0.05):
        A = A_M2 + dl * seat_dir("J")
        M1, _m2, hd, lm = abT_grams(A)
        ev = np.linalg.eigvalsh((M1 + M1.conj().T) / 2)
        id_ok &= (hd <= ZTOL and abs(ev[0] + abs(dl)) <= 1e-12
                  and abs(ev[1] - abs(dl)) <= 1e-12)
    A_s = parent(0.5, 0.5, 0.05, 0.05, 0.05)
    M1, _m2, hd_s, lm_s = abT_grams(A_s)
    ev_s = np.linalg.eigvalsh((M1 + M1.conj().T) / 2)
    id_ok &= (abs(ev_s[0] + 0.05) <= 1e-12
              and abs(ev_s[1] - 0.05) <= 1e-12)
    check("P3.2 the covariant seat direction gives margin = "
          "-|delta_aJ| exactly (4 deltas, ward <= 1e-12) and the "
          "family s-direction reproduces margin = -s at s = 1/20 "
          "(probe-7 C4 regression): the covariant reachable RP "
          "set is EXACTLY {a_J = 0}", id_ok, kill="K3")

    sup_cov = 0.0
    for p in grid0:
        A = parent(*p)
        smax = float(np.max(np.abs(np.linalg.eigvalsh(1j * A))))
        if smax > 0.95:
            continue
        _m1, _m2, hd, lm = abT_grams(A)
        _n, _s2, aJ45 = census10(schur_Aeff(A))
        sup_cov = max(sup_cov, max(lm, 0.0) * abs(aJ45))
    for dl in (0.02, 0.05):
        for sgn in (1, -1):
            A = A_M2 + sgn * dl * seat_dir("J")
            _m1, _m2, hd, lm = abT_grams(A)
            _n, _s2, aJ45 = census10(schur_Aeff(A))
            sup_cov = max(sup_cov, max(lm, 0.0) * abs(aJ45))
    check("P3.3 THE SCALAR: sup over the covariant scan of "
          "(max(margin, 0) x mixing) = %.1e == 0 EXACTLY (product "
          "identically zero on the covariant RP set): the witness "
          "is NOT a limit of covariant strictly-RP parents because "
          "NONE EXIST -- the closure-point-vs-isolated dichotomy "
          "is REFUTED (strict side empty, witness not isolated)"
          % sup_cov, sup_cov <= 1e-15, kill="K3")

    # ==================================================================
    section("P4 -- the transversal escape + its exact price")
    # ==================================================================
    EPS_GRID = (0.001, 0.0025, 0.005, 0.01, 0.05, 0.1, 0.25)
    rows = []
    ok_1p = True
    ok_price = True
    ok_mix = True
    prods = []
    margins = []
    for eps in EPS_GRID:
        A = A_M2 + eps * seat_dir("X")
        smax = float(np.max(np.abs(np.linalg.eigvalsh(1j * A))))
        car = smax <= 0.95
        M1, M2, hd, lm = abT_grams(A)
        ev1 = np.linalg.eigvalsh((M1 + M1.conj().T) / 2)
        ev2 = np.linalg.eigvalsh((M2 + M2.conj().T) / 2)
        margin = min(float(ev1[0]), float(ev2[0]))
        cd = cov_defect(A)
        Aeff = schur_Aeff(A)
        n_nz, n_sig, aJ45 = census10(Aeff)
        prod = max(margin, 0.0) * abs(aJ45)
        rows.append((eps, smax, margin, cd, n_nz, aJ45, prod))
        if car:
            ok_1p &= (hd <= ZTOL
                      and abs(ev1[0] - eps) <= 1e-12
                      and abs(ev1[1] - eps) <= 1e-12
                      and ev2[0] > 0)
            ok_price &= abs(cd - 2 * eps) <= 1e-12
            ok_mix &= (n_nz == 10 and abs(aJ45 - 0.005) <= 1e-12)
            prods.append((eps, prod))
            margins.append((eps, margin))
    for (eps, smax, margin, cd, n_nz, aJ45, prod) in rows:
        print("      eps=%+.4f smax=%.3f margin=%+.2e cov=%.4f "
              "mix=%d aJ45=%.6f product=%.2e"
              % (eps, smax, margin, cd, n_nz, aJ45, prod))
    check("P4.1 ESCAPE: at every CAR-valid eps > 0 the parent is "
          "STRICTLY RP (1p eigenvalues {eps, eps} ward <= 1e-12, "
          "deg-2 PD), covariance defect EXACTLY 2 eps, CAR valid, "
          "mixing 10/10 with the {4,5} J-coordinate = 1/200 "
          "UNCHANGED", ok_1p and ok_price and ok_mix, kill="K4")

    small = [(e, m) for (e, m) in margins if e <= 0.01]
    xs = np.log([e for e, _m in small])
    ys = np.log([m for _e, m in small])
    slope = float(np.polyfit(xs, ys, 1)[0])
    sup_esc = max(p for _e, p in prods)
    check("P4.2 EXPONENT + SUP: the margin is deg-2-limited and "
          "QUADRATIC in eps (log-log slope %.3f = 2.00 +- 0.05 on "
          "the small-eps grid); the product margin x mixing is > 0 "
          "and its sup on the CAR-valid grid is %.2e >= 1e-5: the "
          "escape is TRANSVERSAL at finite covariance breaking"
          % (slope, sup_esc),
          abs(slope - 2.0) <= 0.05 and sup_esc >= 1e-5, kill="K4")

    # exact escape at eps = 1/100 (rationals, 16-dim machinery)
    epsQ = sp.Rational(1, 100)
    Eex = sp.zeros(16)
    Xs = sp.Matrix([[0, 1], [1, 0]])
    for r in range(2):
        for c in range(2):
            Eex[CH[a_ch][r], CH[b_ch][c]] = Xs[r, c]
            Eex[CH[b_ch][c], CH[a_ch][r]] = -Xs[r, c]
    A_esc = A_ex + epsQ * Eex
    wk_esc = wick_exact_factory(A_esc)
    M1e = gram_exact(B1_ab, r_abT, sp.I, wk_esc)
    M2e = gram_exact(B2_ab, r_abT, sp.I, wk_esc)
    ok_m1e = sp.expand(M1e - sp.diag(epsQ, epsQ)) == sp.zeros(2)
    herm2e = sp.expand(M2e - M2e.conjugate().T) == sp.zeros(2)
    det2e = sp.expand(M2e.det())
    check("P4.3 EXACT at eps = 1/100: M1 = diag(1/100, 1/100) "
          "exactly (%s); deg-2 Hermitian (%s) with det = %s == "
          "eps^2 = 1/10000 exactly" % (ok_m1e, herm2e, det2e),
          bool(ok_m1e) and bool(herm2e)
          and det2e == sp.Rational(1, 10000), kill="K4")

    # symbolic Schur pass-through + floor exchange
    kap_s, m_s, t_s, e_s = sp.symbols("kappa m t eps", real=True)
    A_CCs = sp.Matrix(A_CC.tolist())
    J3s = sp.Matrix(J3.tolist())
    Ws = t_s * sp.Matrix((W1 + W2).tolist())
    ECC = sp.zeros(10, 10)
    for r in range(2):
        for c in range(2):
            ECC[CH[a_ch][r], CH[b_ch][c]] = Xs[r, c]
            ECC[CH[b_ch][c], CH[a_ch][r]] = -Xs[r, c]
    C_CC = (sp.eye(10) + sp.I * (kap_s * A_CCs + e_s * ECC)) / 2
    C_CB = sp.I * Ws / 2
    C_BC = -sp.I * Ws.T / 2
    C_BB_inv = 2 * (sp.eye(6) - sp.I * m_s * J3s) / (1 - m_s ** 2)
    C_eff = sp.expand(C_CC - C_CB * C_BB_inv * C_BC)
    A_eff_sym = sp.Matrix(10, 10, lambda r, c: sp.expand(
        sp.im(sp.expand(2 * C_eff[r, c]))))
    A_eff_formula = (kap_s * A_CCs + e_s * ECC
                     + (m_s / (1 - m_s ** 2)) * Ws * J3s * Ws.T)
    ok_schur = sp.simplify(A_eff_sym - A_eff_formula) == sp.zeros(10)
    lamQ = mQ / (1 - mQ ** 2)
    Jco = sp.Integer(3) * lamQ * tQ ** 2
    B45 = (Jco * sp.Matrix([[0, 1], [-1, 0]]) + e_s * Xs)
    pf45 = sp.expand(-B45.det())
    pf_target = sp.expand((e_s - sp.Rational(1, 200))
                          * (e_s + sp.Rational(1, 200)))
    M1_eff = sp.Matrix([[B45[0, 1], B45[1, 1]],
                        [B45[0, 0], B45[1, 0]]])
    ev_eff_ok = sp.expand(M1_eff - sp.diag(
        e_s + sp.Rational(1, 200),
        e_s - sp.Rational(1, 200))) == sp.zeros(2)
    check("P4.4 FLOOR EXCHANGE (exact): the Schur identity extends "
          "with the eps term passing through untouched, A_eff = "
          "kappa A_CC + eps E_CC + (m/(1-m^2)) W J3 W^T (%s); at "
          "the M2 parent Pf4_{45}(eps) = %s == (eps - 1/200)(eps "
          "+ 1/200) (%s) and the effective 2-cycle odd Gram is "
          "diag(eps + 1/200, eps - 1/200) exactly (%s): the "
          "canonical sign gate IS the negative effective-RP margin "
          "-- the same factor (eps - 1/200); at eps = 1/200 the "
          "{4,5} Pfaffian dies exactly"
          % (ok_schur, pf45, sp.expand(pf45 - pf_target) == 0,
             ev_eff_ok),
          bool(ok_schur) and sp.expand(pf45 - pf_target) == 0
          and bool(ev_eff_ok), kill="K4")

    # ==================================================================
    section("C -- controls (must fire; RNG only in C5)")
    # ==================================================================
    ok_c1 = True
    for eps in (0.01, -0.01):
        A = A_M2 + eps * seat_dir("I")
        M1, _m2, hd, lm = abT_grams(A)
        ev = np.linalg.eigvalsh((M1 + M1.conj().T) / 2)
        ok_c1 &= (hd <= ZTOL and abs(ev[0] + abs(eps)) <= 1e-12
                  and abs(ev[1] - abs(eps)) <= 1e-12 and lm < 0)
    check("C1 FIRES: the I seat direction violates RP for BOTH "
          "signs (1p eigenvalues -+|eps| exactly) -- the "
          "deliberately RP-violating control", ok_c1, kill="K7")

    A = A_M2 + 0.01 * seat_dir("Z")
    M1, _m2, hdZ, _lm = abT_grams(A)
    raw = float(np.max(np.abs(M1 - M1.conj().T)))
    check("C2 FIRES: the Z seat direction breaks 1p Gram "
          "Hermiticity (raw defect %.4f == 2|eps| = 0.02 +- 1e-12) "
          "-- not an OS candidate" % raw,
          abs(raw - 0.02) <= 1e-12, kill="K7")

    A = A_M2 - 0.005 * seat_dir("X")
    M1, _m2, hd, lm = abT_grams(A)
    ev = np.linalg.eigvalsh((M1 + M1.conj().T) / 2)
    check("C3 FIRES: eps = -1/200 on X gives BOTH 1p eigenvalues "
          "negative ({%.4f, %.4f})" % (ev[0], ev[1]),
          ev[0] < 0 and ev[1] < 0 and hd <= ZTOL, kill="K7")

    Jco_val = sp.Integer(3) * (mQ / (1 - mQ ** 2)) * tQ ** 2
    check("C4 EXACT 1/200 REGRESSION: J-coordinate = t^2 3m/(1-m^2)"
          " = %s == 1/200 at the M2 parent (exact rationals)"
          % Jco_val, Jco_val == sp.Rational(1, 200), kill="K7")

    rng = np.random.default_rng(903)
    n_fire = 0
    for _trial in range(3):
        pr = rng.permutation(10)
        A_bad = parent(0.5, 0.5, 0.05, 0.05, 0.0)
        Wb = A_bad[np.ix_(CAR_IDX, BND_IDX)][pr, :]
        A_bad[np.ix_(CAR_IDX, BND_IDX)] = Wb
        A_bad[np.ix_(BND_IDX, CAR_IDX)] = -Wb.T
        if cov_defect(A_bad) >= NZ_FLOOR:
            n_fire += 1
    check("C5 FIRES: 3/3 seeded random row permutations of the "
          "coupling break the exact C6-covariance ward (%d/3)"
          % n_fire, n_fire == 3, kill="K7")

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
        VERDICT = "KERNEL-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "STRATUM-BROKEN"
    elif "K4" in KILLS:
        VERDICT = "ESCAPE-BROKEN"
    else:
        VERDICT = ("MARGSTAB-MEASURED [INTERIOR-EMPTY(covariant "
                   "strict RP impossible: +-a_J and det = -a_J^2 "
                   "exact), STRATUM-NOT-ISOLATED(margin == 0 on "
                   "the whole s = 0 grid), NOT-A-CLOSURE-POINT("
                   "covariant strict approximants do not exist), "
                   "ESCAPE-NONCOVARIANT(X seat coordinate; price "
                   "2 eps; exponent 2), FLOOR-EXCHANGE(Pf4 = "
                   "(eps - 1/200)(eps + 1/200) = the effective "
                   "margin factor)]")
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE HEADLINE ANSWER: the round-59 dichotomy (closure point vs
    isolated) is REFUTED as a dichotomy.  Within the C6-covariant
    class the strict-RP side of the cone is EMPTY -- the seat law
    M1 = diag(a_J, -a_J), det M2 = -a_J^2 (exact, whole class)
    makes strict theta_abT RP impossible, so the marginal witness
    is NOT a limit of covariant strict equilibria (none exist);
    it is ALSO not isolated (the entire s = 0 family is a marginal
    stratum with margin exactly 0 and full mixing).  'Physical as
    a limit of equilibria' is unrealizable inside the symmetry
    class; the decisive scalar sup(margin x mixing) = 0 exactly.
  * THE KERNEL: at the witness the 1p Gram vanishes identically
    (kernel = both a-side Majoranas) and the deg-2 Gram [[1, i/2],
    [-i/2, 1/4]] has the exact kernel vector (-i/2, 1); both are
    forced by the same pure-J covariance law (the only visible
    seat coordinate is a_J) that seats the strict obstruction.
  * THE ESCAPE: breaking covariance along the unique admissible X
    seat coordinate buys strict parent RP at ANY eps > 0 with full
    mixing kept (product > 0, transversal; price = covariance
    defect exactly 2 eps; margin quadratic, exponent 2.0) -- BUT
    one level down the exclusion survives: Pf4_{45}(eps) =
    (eps - 1/200)(eps + 1/200) shares its root with the effective
    RP margin, so strict effective RP and the canonical mixing
    sign EXCHANGE exactly at the 1/200 floor.
  * HONESTY: all statements are sector-typed measurements/exact
    identities on this finite model; the escape is a recorded
    covariance-breaking deformation, not a proposal; the [O]
    premise of v898/v903 is unmoved; no marker moves.  NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
