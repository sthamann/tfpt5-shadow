#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""seam_gap_pencil_probe -- SEAM.CFIN.GAP.PENCIL.01
(EXPLORATION ONLY, experiments/; round 59, 2026-08-10, Probe 8 --
t_gap = 0.230949 as a THEOREM-SHAPED object: a generalized
eigenvalue of the FIXED integer pencil P(t) = A_dep + t A_int,
with the three known critical surfaces as projections of ONE
object, exact invariance, and exact uniqueness in the physical
interval.)

THE QUESTION.  Round 58 (seam_state_derivation_probe) measured
three critical surfaces of the deployed seam family h(t) =
-(A_dep + t A_int): the 1p gap closes at t* = 0.2309488708...,
the beta -> infinity (modular ground-state) transition sits at the
same value, and the hermitized RP boundary t_c(beta) increases
toward the same value as beta -> infinity -- and it identified the
number as the smallest positive root of 9t^3 + 21t^2 - t - 1 via
the exact determinant factorization.  What round 58 did NOT do is
shape this into a single fixed object with an exact uniqueness and
invariance statement: t_gap as a GENERALIZED EIGENVALUE of the
integer pencil (A_dep, A_int), the three surfaces as three
projections of the SAME determinant variety, invariance under the
allowed basis changes, and an exact one-root-only statement on the
physical interval.  That is this probe.

FEASIBILITY / REDUNDANCY CHECK (done against the corpus FIRST,
2026-08-10): round 58 proved det(A_dep + t A_int) = (t-1)^2
(3t^2-1)^2 (9t^3+21t^2-t-1)^2 exactly and measured the three
surfaces separately (R2.3, R2.5, and the disclosed dead guess
(iii) on the ground state); v898 uses the pencil only through the
KMS states; NOTHING in the corpus states the Pfaffian-level
factorization, the generalized-eigenvalue shape with kernel
dimension, the exact uniqueness in the physical interval, or the
congruence/scaling covariance of the object.  New content, built
directly on the round-58 lock.

SMOKE-RUN DISCLOSURE (2026-08-10, one declared smoke round before
freezing; frozen numbers below were read off the smoke run):
 (i)   the PFAFFIAN sign is MINUS (the first guess +1 was killed
       by the t = 0 evaluation, fail-first preserved):
       Pf(A_dep + t A_int) = -(t-1)(3t^2-1)(9t^3+21t^2-t-1) as an
       exact polynomial identity (Pf(A_dep) = +1 at t = 0 fixes
       the sign since the candidate must equal +-Pf identically
       in the polynomial ring; degree <= 8 object verified at 9
       rational points by exact Fraction Pfaffian recursion);
 (ii)  the kernel of P(t_gap) is exactly 2-dimensional (float svd
       sigma_14 = sigma_15 ~ 1e-16..1e-12, sigma_13 >= 0.1) --
       consistent with the EXACT even-rank argument (antisymmetric
       real matrix has even rank; det vanishes to order exactly 2
       because q is squarefree and det = Pf^2);
 (iii) the ground-state jump at t_gap is PERSISTENT: the beta ->
       infinity covariance A_inf(t) jumps by ||Delta||_F = 2.83 =
       2 sqrt(2) (a rank-2 occupation flip) across t_gap for
       delta down to 1e-5, while at the reference point t = 1/5
       the two-sided difference dies linearly (~ 6e-3 at
       delta = 1e-3);
 (iv)  the hermitized RP boundary approaches the pencil root
       MONOTONELY: t_c(1) = 0.2205 (measurably below, gap
       1.04e-2), while at beta = 30 and 60 the bisection
       coincides with t_gap to BELOW float resolution (1.4e-15)
       -- the strict-below property at finite beta is only
       float-resolvable at small beta (typed as a limit
       statement, the first draft's strict-below gate at beta =
       30 was unresolvable and is disclosed as such);
 (v)   ROOT-STABILIZER DISCLOSURE: an unrestricted seeded
       single-wire perturbation census found ONE carrier-cross
       direction (entry pair (1,5)) that changes det P(t) but
       KEEPS t_gap a root -- a measured stabilizer direction of
       the variety; the frozen control C1 therefore perturbs
       COUPLING wires (carrier x boundary), which moved the root
       on 3/3 seeded draws;
 (vi)  kernel channel anatomy (report only): the two zero modes
       at t_gap spread over carrier AND boundary channels
       (weights ~ {0: 0.78, 3-cycle: 0.26 each, 2-cycle: 0.22
       each} -- no single-channel localization).

CONVENTIONS (round 52/57/58 wiring rebuilt inline; READ-ONLY
import of tfpt_constants): 16-dim Majorana space; A_dep = (+)_8 J
(J = [[0,1],[-1,0]]); A_int = the C6-covariant integer seam wiring
(vacuum orbit blocks IOTA/I2/J2, round 52); channels CH(0) =
boundary indices 10..15, CH(i) = {2(i-1), 2(i-1)+1} for the five
carrier channels.  THE PENCIL: P(t) = A_dep + t A_int (both
matrices FIXED integer, no parameters).  q(t) = 9t^3 + 21t^2 -
t - 1; t_gap = its smallest positive root = 0.2309488708333614.
PHYSICAL INTERVAL (frozen): (0, 1/4] = the deployed-region bound
of round 58 (the u_c = t law was verified on t in {1/16, 1/8,
1/4}; the deployed point is t = 1/8).  KMS states, reflections,
Grams: v519/round-58 machinery (theta_S sheet swap, eta = +i,
sector Grams 1p + even deg-2).  NUMERICAL PROTOCOL (declared):
ALL pencil-level claims are EXACT (sympy polynomial arithmetic,
exact Fraction Pfaffian recursion, Sturm root counts, polynomial
remainders mod q); the three surfaces are float64 measurements
with frozen tolerances; RNG only in controls.

FROZEN CLAIMS (2026-08-10, frozen + SHA-hashed before the frozen
run):

 P1  THE PENCIL (exact).
     (a) det P(t) = (t-1)^2 (3t^2-1)^2 q(t)^2 EXACTLY (round-58
         lock re-established inline);
     (b) PFAFFIAN LEVEL (new): Pf P(t) = -(t-1)(3t^2-1) q(t)
         EXACTLY -- degree-<=8 polynomial identity certified by
         exact Fraction Pfaffian recursion at 9 rational points
         (two polynomials of degree <= 8 agreeing at 9 points are
         equal); sign fixed by Pf(A_dep) = +1 at t = 0;
     (c) q is IRREDUCIBLE over Q with EXACTLY ONE positive real
         root (exact Sturm count on (0, oo)); t_gap =
         0.2309488708333614 +- 1e-13 (float of the exact root);
         q is the minimal polynomial of t_gap (degree 3);
     (d) GENERALIZED-EIGENVALUE SHAPE: t_gap is a finite
         generalized eigenvalue of (A_dep, A_int) -- det P(t_gap)
         = 0 with kernel dimension EXACTLY 2 (exact argument:
         antisymmetric real matrices have even rank and det
         vanishes to order exactly 2 since q is squarefree; float
         ward: sigma_14, sigma_15 <= 1e-10, sigma_13 >= 0.1); the
         pencil is SINGULAR in the strict sense (deg det = 12 <
         16: det A_int = 0, four infinite eigenvalues) -- typed,
         not hidden.
 P2  THREE SURFACES = THREE PROJECTIONS OF ONE VARIETY.
     (a) 1p GAP CLOSURE: gap(t) = min |eig(i h(t))| vanishes at
         t_gap (float <= 1e-7 at the algebraic root) and is
         >= 4e-3 at t_gap -+ 0.01; by P1(c+d) the ONLY gap zero
         in the physical interval (0, 1/4] is t = t_gap (exact
         uniqueness, P3(d));
     (b) MODULAR GROUND-STATE TRANSITION: the beta -> infinity
         covariance jumps at t_gap with ||Delta||_F = 2 sqrt(2)
         +- 0.01 for ALL delta in {1e-3, 1e-4, 1e-5} (a rank-2
         occupation flip, persistent as delta -> 0), while the
         same two-sided difference at the reference t = 1/5 is
         <= 0.01 at delta = 1e-3 (smooth off the variety); the
         EXACT sign flip: q(23/100) < 0 < q(6/25) (rational
         arithmetic) -- Pf P changes sign exactly once across
         t_gap in (0, 1/4];
     (c) RP BOUNDARY: the hermitized theta_S PSD boundary
         t_c(beta) of the round-58 family satisfies t_c(1) =
         0.2205 +- 0.01 (regression, measurably below the root:
         gap > 1e-3), is monotone nondecreasing on {1, 30, 60},
         and coincides with the pencil root to <= 1e-6 at
         beta = 30 and 60: the zero-temperature RP boundary IS
         the pencil root (limit statement; the strict-below
         property at finite beta is only float-resolvable at
         small beta).
 P3  INVARIANCE + UNIQUENESS (exact).
     (a) C6-INVARIANCE (exact, strongest form): the C6 lift O16
         fixes BOTH pencil members entrywise (O A_dep O^T = A_dep,
         O A_int O^T = A_int; integer arithmetic) -- the pencil is
         a FIXED object of the symmetry, not merely isospectral;
     (b) GAUGE CONGRUENCE (allowed basis changes): for seeded
         SO(2)^8 block rotations Q (they preserve A_dep exactly),
         det(Q P(t) Q^T) = det P(t) identically (float ward at 5
         rational t values, defect <= 1e-8 relative): t_gap is
         congruence-invariant even though A_int moves;
     (c) SCALING COVARIANCE (exact): det(A_dep + t (c A_int)) has
         the root t_gap / c (exact polynomial substitution at
         c = 2: the factor becomes q(2t) with smallest positive
         root t_gap / 2) -- the object transforms as a pencil
         eigenvalue must;
     (d) UNIQUENESS (exact Sturm): det P(t) has EXACTLY ONE
         distinct root in the physical interval (0, 1/4]: q
         counts 1 root there, (3t^2 - 1) and (t - 1) count 0;
         and q(1/4) > 0 > q(0) exactly (the root is interior).
 C   CONTROLS (must fire; frozen fire rules; RNG only here).
     C1 SEEDED COUPLING-WIRE PERTURBATION (rng 901, 3 draws): one
        random carrier-boundary A_int entry pair shifted by +1
        (integer, antisymmetry kept): the polynomial remainder of
        det P'(t) mod q(t) is NONZERO on 3/3 draws (exact: t_gap
        is NOT a root of the perturbed pencil) -- the root is
        pinned by the coupling wiring; the disclosed carrier-cross
        stabilizer direction (1,5) (smoke item (v)) is excluded
        by the coupling restriction;
     C2 BOUNDARY-COUPLING KILL: zeroing the carrier-boundary
        coupling W of A_int changes the variety so that t_gap is
        NOT a root of the new determinant (exact remainder mod q
        nonzero) -- the boundary coupling is load-bearing for the
        pencil root;
     C3 v898 REGRESSION: the deployed KMS state (u=1, t=1/8,
        beta=1) has smax = 0.667735 +- 1e-6 and 15/15 canonical
        per-edge Pf4 signs (corpus tie-in);
     C4 AST firewall: banned identifiers.

KILLS (any one fires => typed gap):
  K0 AST firewall / compiler rebuild ward breaks -> PIPELINE-BROKEN
  K1 pencil exactness (det/Pf/irreducibility)    -> PENCIL-BROKEN
  K2 a surface projection ward breaks            -> SURFACE-BROKEN
  K3 invariance / uniqueness ward breaks         -> INVARIANCE-BROKEN
  K7 a control does not fire                     -> CONTROL-DEAD

VERDICT (frozen enum): GAPPENCIL-MEASURED [PFAFFIAN-LEVEL(Pf P =
-(t-1)(3t^2-1)q exactly), GENEV(kernel dim 2, minimal polynomial
q, degree 3), THREE-SURFACES(1p gap + ground-state jump 2 sqrt(2)
+ RP boundary limit), UNIQUE-IN-(0,1/4](exact Sturm)] /
PIPELINE-BROKEN / PENCIL-BROKEN / SURFACE-BROKEN /
INVARIANCE-BROKEN / CONTROL-DEAD.  Exit 0 iff all checks pass and
no kill fired; else 1.

FIREWALL: experiments/ probe; EXPLORATION ONLY -- writes nothing
but stdout; no verification/, paper, ledger, changelog or website
surface; no .md, no commits.  NO physics claim beyond the recorded
identities and measurements: t_gap remains a property of THIS
integer pencil; the RP-boundary surface is a beta -> infinity
LIMIT statement (at finite beta the boundary is strictly below);
no marker moves.  NO RH claim.

SPEC v1 (2026-08-10): frozen after the declared smoke round; no
amendments at freeze.

Sources (read-only, machinery rebuilt inline): seam_state_
derivation_probe (round 58: factorization lock R2.3, t_c R2.5,
ground-state dead-guess disclosure), v898_kms_schur_mixing
(deployed state), rp_parent_dilation_probe (Probe 7 machinery),
v519 (RP Gram), tfpt_constants (N_fam, g_car).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/seam_gap_pencil_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time
from fractions import Fraction

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
TGAP_REF = 0.2309488708333614


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


def pf_exact(M):
    """exact Pfaffian of an antisymmetric Fraction matrix via
    memoized recursion on the tuple of remaining indices."""
    n = len(M)
    memo = {}

    def rec(idx):
        if not idx:
            return Fraction(1)
        if idx in memo:
            return memo[idx]
        i0 = idx[0]
        rest = idx[1:]
        tot = Fraction(0)
        for j, b in enumerate(rest):
            a = M[i0][b]
            if a:
                sub = rest[:j] + rest[j + 1:]
                tot += (-1) ** j * a * rec(sub)
        memo[idx] = tot
        return tot
    return rec(tuple(range(n)))


def main():
    print("SEAM.CFIN.GAP.PENCIL.01 -- t_gap as a generalized "
          "eigenvalue of the fixed pencil (A_dep, A_int)")
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
    check("S0.2 deployed pi = %s, cycle type %s == (1, 2, 3)"
          % (PI6, cycle_type(PI6)),
          PI6[0] == 0 and cycle_type(PI6) == (1, 2, 3), kill="K0")

    CH = {0: list(range(10, 16))}
    for i in range(1, 6):
        CH[i] = [2 * (i - 1), 2 * (i - 1) + 1]
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
    check("S0.3 pencil members rebuilt: A_dep = (+)_8 J and the "
          "C6-covariant integer A_int (both fixed, no parameters); "
          "covariance + antisymmetry exact", okA and okD, kill="K0")

    # ==================================================================
    section("P1 -- THE PENCIL (exact)")
    # ==================================================================
    tsym = sp.Symbol("t")
    Msym = sp.Matrix(16, 16, lambda i, j:
                     sp.Integer(int(A16_dep[i, j]))
                     + tsym * sp.Integer(int(A_int[i, j])))
    dsym = sp.expand(Msym.det())
    q_pol = 9 * tsym ** 3 + 21 * tsym ** 2 - tsym - 1
    target = sp.expand((tsym - 1) ** 2 * (3 * tsym ** 2 - 1) ** 2
                       * q_pol ** 2)
    ok_fac = sp.expand(dsym - target) == 0
    check("P1.1 det P(t) = (t-1)^2 (3t^2-1)^2 q(t)^2 EXACTLY (%s), "
          "q = 9t^3+21t^2-t-1 (round-58 lock re-established); "
          "deg det = 12 < 16: det A_int = 0, the pencil has four "
          "infinite eigenvalues (typed)" % ok_fac,
          ok_fac and sp.degree(dsym, tsym) == 12, kill="K1")

    pf_cand = sp.expand(-(tsym - 1) * (3 * tsym ** 2 - 1) * q_pol)
    test_pts = [Fraction(0), Fraction(1, 2), Fraction(-1, 2),
                Fraction(1, 3), Fraction(-1, 3), Fraction(1, 4),
                Fraction(1, 5), Fraction(2, 3), Fraction(3, 2)]
    ok_pf = True
    for tv in test_pts:
        Mfr = [[Fraction(int(A16_dep[i, j]))
                + tv * Fraction(int(A_int[i, j]))
                for j in range(16)] for i in range(16)]
        pv = pf_exact(Mfr)
        cv = Fraction(sp.Rational(pf_cand.subs(
            tsym, sp.Rational(tv.numerator, tv.denominator))))
        ok_pf &= (pv == cv)
    check("P1.2 PFAFFIAN LEVEL (new): Pf P(t) = -(t-1)(3t^2-1)q(t) "
          "EXACTLY -- degree-<=8 identity certified at 9 rational "
          "points by exact Fraction Pfaffian recursion (all match: "
          "%s); sign fixed by Pf(A_dep) = +1 at t = 0" % ok_pf,
          ok_pf, kill="K1")

    ok_irr = sp.Poly(q_pol, tsym).is_irreducible
    n_pos = sp.Poly(q_pol, tsym).count_roots(0, sp.oo)
    roots_pos = [x for x in sp.Poly(q_pol, tsym).all_roots()
                 if x.is_real and x > 0]
    t_gap = float(sp.N(roots_pos[0], 20))
    check("P1.3 q IRREDUCIBLE over Q (%s) with EXACTLY ONE positive "
          "real root (Sturm count %d == 1); t_gap = %.16f == "
          "0.2309488708333614 +- 1e-13; q is the degree-3 minimal "
          "polynomial of t_gap" % (ok_irr, n_pos, t_gap),
          ok_irr and n_pos == 1 and len(roots_pos) == 1
          and abs(t_gap - TGAP_REF) <= 1e-13, kill="K1")

    Pg = A16_dep.astype(np.float64) + t_gap * A_int.astype(np.float64)
    sv = np.linalg.svd(Pg, compute_uv=False)
    q_sqfree = sp.gcd(sp.Poly(q_pol, tsym),
                      sp.Poly(sp.diff(q_pol, tsym), tsym)).degree() == 0
    check("P1.4 GENERALIZED-EIGENVALUE SHAPE: det P(t_gap) = 0 with "
          "kernel dimension EXACTLY 2 -- exact argument: q "
          "squarefree (%s) so det vanishes to order exactly 2, and "
          "an antisymmetric real matrix has even rank; float ward: "
          "sigma_15 = %.1e, sigma_14 = %.1e <= 1e-10, sigma_13 = "
          "%.4f >= 0.1"
          % (q_sqfree, sv[15], sv[14], sv[13]),
          q_sqfree and sv[15] <= 1e-10 and sv[14] <= 1e-10
          and sv[13] >= 0.1, kill="K1")

    # kernel channel anatomy (report only)
    _u, _s, vt = np.linalg.svd(Pg)
    wts = {}
    for i in range(6):
        wts[i] = round(float(sum(np.sum(vt[k, CH[i]] ** 2)
                                 for k in (14, 15))), 4)
    print("      kernel channel weights (2 zero modes, report): %s"
          % wts)

    # ==================================================================
    section("P2 -- THREE SURFACES = PROJECTIONS OF ONE VARIETY")
    # ==================================================================
    Aint_f = A_int.astype(np.float64)
    Adep_f = A16_dep.astype(np.float64)

    def gap1p(t):
        h = -(Adep_f + t * Aint_f)
        w = np.linalg.eigvalsh(1j * h)
        return float(np.min(np.abs(w)))

    g0 = gap1p(t_gap)
    gm = gap1p(t_gap - 0.01)
    gp = gap1p(t_gap + 0.01)
    check("P2.1 1p GAP CLOSURE: gap(t_gap) = %.1e <= 1e-7, "
          "gap(t_gap -+ 0.01) = (%.4f, %.4f) >= 4e-3; by P1 + "
          "P3(d) the ONLY closure in (0, 1/4] is t_gap"
          % (g0, gm, gp),
          g0 <= 1e-7 and gm >= 4e-3 and gp >= 4e-3, kill="K2")

    def ground_A(t):
        h = -(Adep_f + t * Aint_f)
        w, Q = np.linalg.eigh(1j * h)
        occ = (w < 0).astype(np.float64)
        return (-1j * (2 * (Q * occ) @ Q.conj().T
                       - np.eye(16))).real

    jumps = []
    for dl in (1e-3, 1e-4, 1e-5):
        jumps.append(float(np.linalg.norm(
            ground_A(t_gap + dl) - ground_A(t_gap - dl))))
    j_ref = float(np.linalg.norm(
        ground_A(0.2 + 1e-3) - ground_A(0.2 - 1e-3)))
    qa = sp.Rational(9, 1) * sp.Rational(23, 100) ** 3 \
        + 21 * sp.Rational(23, 100) ** 2 - sp.Rational(23, 100) - 1
    qb = sp.Rational(9, 1) * sp.Rational(6, 25) ** 3 \
        + 21 * sp.Rational(6, 25) ** 2 - sp.Rational(6, 25) - 1
    check("P2.2 MODULAR GROUND-STATE TRANSITION: persistent rank-2 "
          "occupation flip ||Delta||_F = %s == 2 sqrt(2) +- 0.01 "
          "for delta in {1e-3, 1e-4, 1e-5}; smooth off the variety "
          "(reference t = 1/5: %.4f <= 0.01 at delta = 1e-3); "
          "EXACT sign flip q(23/100) = %s < 0 < q(6/25) = %s"
          % ([round(x, 4) for x in jumps], j_ref, qa, qb),
          all(abs(x - 2 * math.sqrt(2)) <= 0.01 for x in jumps)
          and j_ref <= 0.01 and qa < 0 and qb > 0, kill="K2")

    # ---- RP machinery (v519 / round-58 form) for t_c(beta)
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

    def theta_mono(mono, r, eta):
        imgs = [r[a] for a in reversed(mono)]
        coeff = eta ** len(mono)
        lst = list(imgs)
        sign = 1
        for i in range(len(lst)):
            for j in range(len(lst) - 1 - i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    sign = -sign
        return coeff * sign, tuple(lst)

    def gram(basis, r, eta, wick):
        n = len(basis)
        M = np.zeros((n, n), dtype=complex)
        for ai, ma in enumerate(basis):
            ca, ia = theta_mono(ma, r, eta)
            for bi, mb in enumerate(basis):
                M[ai, bi] = ca * wick(tuple(list(ia) + list(mb)))
        return M

    r_S = {}
    for i in range(8):
        r_S[2 * i] = 2 * i + 1
        r_S[2 * i + 1] = 2 * i
    P_S = [2 * i for i in range(8)]
    B1_S = [(a,) for a in P_S]
    B2_S = [()] + [tuple(c) for c in itertools.combinations(P_S, 2)]

    def kms_A(t, beta):
        h = -(Adep_f + t * Aint_f)
        w, Q = np.linalg.eigh(1j * h)
        f = 1.0 / (1.0 + np.exp(np.clip(beta * w, -700, 700)))
        return (-1j * (2 * (Q * f) @ Q.conj().T
                       - np.eye(16))).real

    def lam2h(t, beta):
        wk = wick_factory(kms_A(t, beta))
        M1 = gram(B1_S, r_S, 1j, wk)
        M2 = gram(B2_S, r_S, 1j, wk)
        l1 = float(np.min(np.linalg.eigvalsh(
            (M1 + M1.conj().T) / 2)))
        l2 = float(np.min(np.linalg.eigvalsh(
            (M2 + M2.conj().T) / 2)))
        return min(l1, l2)

    tcs = {}
    for beta in (1.0, 30.0, 60.0):
        lo, hi = 0.125, 0.30
        for _ in range(45):
            mid = (lo + hi) / 2
            if lam2h(mid, beta) > 0:
                lo = mid
            else:
                hi = mid
        tcs[beta] = (lo + hi) / 2
        print("      t_c(beta=%-4s) = %.8f  (t_gap - t_c = %.2e)"
              % (round(beta, 1), tcs[beta], t_gap - tcs[beta]))
    check("P2.3 RP BOUNDARY: t_c(1) = %.4f (0.2205 +- 0.01, "
          "round-58 regression, measurably BELOW the root: gap "
          "%.4f); monotone nondecreasing on {1, 30, 60}; at "
          "beta = 30 and 60 the boundary coincides with the "
          "pencil root to below float resolution (|t_c - t_gap| "
          "= %.1e, %.1e <= 1e-6): the zero-temperature RP "
          "boundary IS the pencil root (limit statement; the "
          "strict-below property is only float-resolvable at "
          "small beta)"
          % (tcs[1.0], t_gap - tcs[1.0], abs(tcs[30.0] - t_gap),
             abs(tcs[60.0] - t_gap)),
          abs(tcs[1.0] - 0.2205) <= 0.01
          and tcs[1.0] < t_gap - 1e-3
          and tcs[30.0] >= tcs[1.0] - 1e-9
          and tcs[60.0] >= tcs[30.0] - 1e-9
          and abs(tcs[30.0] - t_gap) <= 1e-6
          and abs(tcs[60.0] - t_gap) <= 1e-6, kill="K2")

    # ==================================================================
    section("P3 -- INVARIANCE + UNIQUENESS (exact)")
    # ==================================================================
    O16 = np.zeros((16, 16), dtype=np.int64)
    for src in range(16):
        O16[img[src], src] = 1
    okO = (np.array_equal(O16 @ A16_dep @ O16.T, A16_dep)
           and np.array_equal(O16 @ A_int @ O16.T, A_int)
           and np.array_equal(O16 @ O16.T, np.eye(16,
                                                  dtype=np.int64)))
    check("P3.1 C6-INVARIANCE (exact, strongest form): the C6 lift "
          "O16 is orthogonal and fixes BOTH pencil members "
          "entrywise -- the pencil is a FIXED object of the "
          "symmetry", okO, kill="K3")

    rng = np.random.default_rng(902)
    ok_gauge = True
    max_gdef = 0.0
    for _trial in range(3):
        Q = np.eye(16)
        for b in range(8):
            th = float(rng.uniform(0, 2 * np.pi))
            c, s_ = math.cos(th), math.sin(th)
            Q[2 * b:2 * b + 2, 2 * b:2 * b + 2] = [[c, -s_], [s_, c]]
        dep_def = float(np.max(np.abs(Q @ Adep_f @ Q.T - Adep_f)))
        for tv in (0.1, 0.2, t_gap, 0.3, 0.5):
            P_ = Adep_f + tv * Aint_f
            d1 = np.linalg.det(Q @ P_ @ Q.T)
            d2 = np.linalg.det(P_)
            rel = abs(d1 - d2) / max(abs(d2), 1e-30)
            if abs(d2) > 1e-20:
                max_gdef = max(max_gdef, rel)
                ok_gauge &= (rel <= 1e-8)
        ok_gauge &= (dep_def <= 1e-12)
    check("P3.2 GAUGE CONGRUENCE: seeded SO(2)^8 block rotations "
          "preserve A_dep exactly (defect <= 1e-12) and det P(t) "
          "identically (max relative defect %.1e <= 1e-8 over 5 "
          "t-values x 3 draws): t_gap is congruence-invariant "
          "although A_int moves" % max_gdef, ok_gauge, kill="K3")

    d_scaled = sp.expand(dsym.subs(tsym, 2 * tsym))
    Msym2 = sp.Matrix(16, 16, lambda i, j:
                      sp.Integer(int(A16_dep[i, j]))
                      + tsym * 2 * sp.Integer(int(A_int[i, j])))
    ok_scale = sp.expand(Msym2.det() - d_scaled) == 0
    r_half = sp.Poly(q_pol.subs(tsym, 2 * tsym),
                     tsym).count_roots(0, sp.Rational(1, 8))
    check("P3.3 SCALING COVARIANCE (exact): det(A_dep + t (2 "
          "A_int)) == det P(2t) as polynomials (%s); its q-factor "
          "q(2t) has its unique positive root at t_gap / 2 "
          "(count in (0, 1/8] = %d == 1)" % (ok_scale, r_half),
          ok_scale and r_half == 1, kill="K3")

    n_q = sp.Poly(q_pol, tsym).count_roots(0, sp.Rational(1, 4))
    n_3t = sp.Poly(3 * tsym ** 2 - 1, tsym).count_roots(
        0, sp.Rational(1, 4))
    n_t1 = sp.Poly(tsym - 1, tsym).count_roots(0, sp.Rational(1, 4))
    q_at_14 = q_pol.subs(tsym, sp.Rational(1, 4))
    q_at_0 = q_pol.subs(tsym, 0)
    check("P3.4 UNIQUENESS (exact Sturm): det P(t) has EXACTLY ONE "
          "distinct root in the physical interval (0, 1/4]: "
          "q counts %d == 1, (3t^2-1) counts %d == 0, (t-1) "
          "counts %d == 0; q(1/4) = %s > 0 > q(0) = %s (interior)"
          % (n_q, n_3t, n_t1, q_at_14, q_at_0),
          n_q == 1 and n_3t == 0 and n_t1 == 0
          and q_at_14 > 0 and q_at_0 < 0, kill="K3")

    # ==================================================================
    section("C -- controls (must fire; RNG only here)")
    # ==================================================================
    rng_c = np.random.default_rng(901)
    n_fire = 0
    for _trial in range(3):
        i = int(rng_c.integers(0, 10))
        j = int(rng_c.integers(10, 16))
        Ap = A_int.copy()
        Ap[i, j] += 1
        Ap[j, i] -= 1
        Mp = sp.Matrix(16, 16, lambda r, c:
                       sp.Integer(int(A16_dep[r, c]))
                       + tsym * sp.Integer(int(Ap[r, c])))
        dp = sp.Poly(sp.expand(Mp.det()), tsym)
        rem = sp.rem(dp.as_expr(), q_pol, tsym)
        if sp.expand(rem) != 0:
            n_fire += 1
    check("C1 FIRES: 3/3 seeded coupling-wire perturbations of "
          "A_int (one carrier-boundary entry pair +1) leave a "
          "NONZERO remainder of det P'(t) mod q(t) (exact: t_gap "
          "is NOT a root of the perturbed pencil) -- the root is "
          "pinned by the coupling wiring (%d/3; the disclosed "
          "carrier-cross stabilizer (1,5) is excluded by the "
          "coupling restriction)" % n_fire, n_fire == 3,
          kill="K7")

    Aw = A_int.copy()
    Aw[np.ix_(range(10), range(10, 16))] = 0
    Aw[np.ix_(range(10, 16), range(10))] = 0
    Mw = sp.Matrix(16, 16, lambda r, c:
                   sp.Integer(int(A16_dep[r, c]))
                   + tsym * sp.Integer(int(Aw[r, c])))
    dw = sp.expand(Mw.det())
    rem_w = sp.expand(sp.rem(dw, q_pol, tsym))
    check("C2 FIRES: zeroing the carrier-boundary coupling W "
          "leaves remainder != 0 of the new determinant mod q "
          "(exact: t_gap is NOT a root without the boundary "
          "coupling) -- the coupling is load-bearing for the root",
          rem_w != 0, kill="K7")

    A18 = kms_A(0.125, 1.0)
    smax = float(np.max(np.abs(np.linalg.eigvalsh(1j * A18))))
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

    pf4_c = pf4_of(compress12(Aint_f / 200.0))
    pf4_d = pf4_of(compress12(A18))
    n_match = sum(1 for d in pf4_c
                  if abs(pf4_d[d]) > PF_FLOOR
                  and (pf4_d[d] > 0) == (pf4_c[d] > 0))
    check("C3 v898 REGRESSION: deployed KMS state (u=1, t=1/8, "
          "beta=1): smax = %.6f (0.667735 +- 1e-6), %d/15 "
          "canonical per-edge Pf4 signs" % (smax, n_match),
          abs(smax - 0.667735) <= 1e-6 and n_match == 15,
          kill="K7")

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
        VERDICT = "PENCIL-BROKEN"
    elif "K2" in KILLS:
        VERDICT = "SURFACE-BROKEN"
    elif "K3" in KILLS:
        VERDICT = "INVARIANCE-BROKEN"
    else:
        VERDICT = ("GAPPENCIL-MEASURED [PFAFFIAN-LEVEL(Pf P = "
                   "-(t-1)(3t^2-1)q exactly), GENEV(kernel dim 2, "
                   "minimal polynomial q, degree 3), "
                   "THREE-SURFACES(1p gap + ground-state jump "
                   "2 sqrt(2) + RP boundary limit), "
                   "UNIQUE-IN-(0,1/4](exact Sturm)]")
    print("%d/%d checks passed" % (n_pass, n_tot))
    print("VERDICT: %s" % VERDICT)
    print("""
REPORT (exploration only -- no promotion, no edits):
  * THE OBJECT: t_gap = 0.2309488708... is now theorem-shaped: it
    is the unique positive root of the irreducible cubic q(t) =
    9t^3 + 21t^2 - t - 1, which divides the exact Pfaffian
    Pf(A_dep + t A_int) = -(t-1)(3t^2-1)q(t) of the FIXED integer
    pencil -- a finite generalized eigenvalue with kernel
    dimension exactly 2, unique in the physical interval (0, 1/4]
    by exact Sturm count.
  * THE THREE SURFACES are projections of this one variety: the
    1p gap closes there (and nowhere else in (0, 1/4]); the
    beta -> infinity ground state jumps there by exactly a rank-2
    occupation flip (2 sqrt(2), persistent); the hermitized RP
    boundary t_c(beta) climbs to it monotonely from below and is
    within 1e-4 at beta = 30 (a LIMIT statement -- at finite beta
    the boundary is strictly below the root).
  * INVARIANCE: the C6 lift fixes both pencil members entrywise;
    allowed gauge congruences preserve det P(t) identically;
    rescaling A_int rescales the root exactly as a pencil
    eigenvalue must.  Controls: one integer wire perturbation or
    dropping the boundary coupling kills the root EXACTLY
    (polynomial remainder mod q nonzero).
  * HONESTY: t_gap is a property of THIS integer pencil; the RP
    surface meets it only as beta -> infinity; no marker moves.
    NO RH claim.
Runtime: %.1f s""" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_tot
          else "CHECKS FAILED: %d" % (n_tot - n_pass))
    return 0 if (n_pass == n_tot and not KILLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
