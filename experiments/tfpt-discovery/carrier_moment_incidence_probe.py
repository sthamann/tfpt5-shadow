#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""carrier_moment_incidence_probe -- CARRIER.MOMENT.INCIDENCE.01 (K5
round, cut-code strand, probe 2): the one-line master-moment derivation
from K5 incidence, the characteristic polynomial of the hypercharge
vector, and the FROZEN decision on the fourth moment p4(X) = 210.

SETTING.  X = (-2, -2, -2, 3, 3) is the certified primitive traceless
hypercharge vector on the five carrier slots (v774 / v2 / v310); the 16
carrier states are C_even(5) with X-values xval(v) = sum_i X_i iota(v)_i
and master moment Tr_{S+} X^2 = 120 (v2_carrier_pascal, v774 S12).

STEPS (frozen BEFORE running):
 S1  ONE-LINE MASTER MOMENT [E neu]:
     (a) |X|^2 = 3*4 + 2*9 = 30 = h(E8) (Coxeter number; corpus v55,
         cross-check h = |R(E8)|/rank = 240/8).
     (b) traceless-vector identity, proved SYMBOLICALLY for ALL
         5-vectors (sympy):  sum_{i<j} (X_i + X_j)^2 - 3 sum_i X_i^2
         = (sum_i X_i)^2, hence = 0 on the traceless locus.
     (c) hence Tr_10 X^2 = sum_{i<j}(X_i+X_j)^2 = 3|X|^2 = 90 (the ten
         wt-2 words carry xval = X_i + X_j on the duad {i,j});
         Tr_5bar X^2 = sum_i (-X_i)^2 = |X|^2 = 30 (the five wt-4
         words carry xval = -X_i by tracelessness); Tr_singlet = 0;
         TOTAL Tr_{S+} X^2 = 4 |X|^2 = 4 h(E8) = 120 == the v2/v774
         master moment (full census cross-check).
     (d) chain re-anchored: 120/3 = 40, +1 = 41 = 10 b1
         (tfpt_constants, read-only), 2*120 = 240, +8 = 248.
 S2  CHARACTERISTIC POLYNOMIAL: chi_X(t) = (t+2)^3 (t-3)^2
     = t^5 - 15 t^3 - 10 t^2 + 60 t + 72 (sympy expand, exact);
     elementary symmetric (e1..e5) = (0, -15, 10, 60, -72).
     TYPED: 15 = dim A3 (v91), 10 = |E(K5)| = dim of the 10, 60 = the
     mu4-lines (v700) as AUDIT FINGERPRINTS [C]; 72 explicitly
     AUDIT-ONLY, NO morphism claimed (honesty bar).
 S3  FOURTH MOMENT p4(X) = 3*2^4 + 2*3^4 = 48 + 162 = 210 [H neu ->
     the cheap test]: 210 = C(10,4) = the quartic level of the
     certified Clifford tower 1 + 45 + 210 = 256 (v109/v111; the
     quartic words are the wt-4 monomials in the 10 gammas of Cl(10),
     paired 2-per-slot).  FROZEN CANDIDATE LIST (the decision is the
     deliverable, either way):
     I1  bare numeric: p4 = C(10,4) = 210; Newton tie on the traceless
         locus p4 = 2 e2^2 - 4 e4 = 2*225 - 240 = 210 (generic
         symmetric-function algebra, typed [C] audit, NOT a map).
     I2  EQUIVARIANT BIJECTION candidate: a G-equivariant map from the
         210 quartic basis words onto the 5 slots with fiber sizes
         X_i^4 = (16, 16, 16, 81, 81), for G in {S3 x S2 (the slot
         stabiliser of X, order 12), Z2^5 semidirect (S3 x S2) (with
         within-pair gamma swaps, order 384)}, and for BOTH indexings
         (4-subsets of the 10 paired gammas; 4-subsets of E(K5)).
         DECISION by exact census: orbit decomposition, fixed-point
         obstruction (a G-fixed 4-subset must map to a G-fixed slot;
         the slot orbits are {1,2,3} and {4,5}, no fixed slot), and
         exhaustive enumeration of ALL total equivariant assignments.
     I3  SLOT-LOCAL WEIGHTED IDENTITY candidates: weights w(S) =
         prod_i c_{m_i}(X_i) over the occupancy pattern m (m_i = #
         gammas of slot i in S), generating function
         N(X) = [t^4] prod_i (c_0(X_i) + 2 t c_1(X_i) + t^2 c_2(X_i));
         frozen list c = (c_0, c_1, c_2) in { (1, x, x^2),
         (1, x^2, x^4), (1, 0, x^2), (1, 0, x^4), (1, x, x^4),
         (1, x^2, x^2) }; test N(X) == p4(X) symbolically (general and
         traceless) and numerically at the frozen X.
     I4  PARTIAL miss-slot map (reported honestly): the 80 type-
         (1,1,1,1) subsets (one gamma from each of 4 slots) map
         canonically to their MISSED slot with uniform fiber 2^4 = 16;
         this matches X_i^4 = 16 exactly on the three colour slots and
         fails on the weak slots (81 != 16); deficit 2*65 = 130 = 10
         (type (2,2)) + 120 (type (2,1,1)) pair-containing subsets.
     I5  alphabet reading (recorded): p4 = sum_i |X_i|^4 = # of pairs
         (slot i, 4-letter word over an alphabet of size |X_i|); the
         gamma pairs provide alphabet size 2 on every slot, so no
         canonical alphabet-3 structure exists on the weak slots in
         the frozen corpus objects.
     RULE (frozen): a canonical bijection/weighted identity from the
     frozen list certifies [E neu]; if ALL frozen candidates fail, the
     210 is typed DECORATIVE (audit fingerprint at counting level).
 S4  occupancy census: 210 = 10 (type (2,2)) + 120 (type (2,1,1)) +
     80 (type (1,1,1,1)); tower check 1 + 45 + 210 = 256 = 16^2,
     C(10,2) = 45, C(10,4) = 210.

MUST-FAIL CONTROLS (frozen):
 C1  non-traceless X' = (-2,-2,-2,3,4): the 3-Sigma identity usage
     breaks (residual (sum X')^2 = 1 != 0) and the master-moment
     census != 120.
 C2  mutated X'' = (-2,-2,-2,3,2): p4 = 145 != 210 and the
     characteristic polynomial deviates from the frozen one.

KILLS:
 K1  any S1 census/identity fails (moments, symbolic identity, chain).
 K2  the characteristic polynomial or the elementary symmetric values
     deviate.
 (S3 has NO kill: either outcome of the 210 decision is the
  deliverable; S4 occupancy arithmetic failing is K1-grade.)

VERDICTS (frozen): MOMENT-INCIDENCE-EXACT (S1+S2 green AND a frozen
210-candidate certifies a canonical map) / MOMENT-INCIDENCE-PARTIAL
(S1+S2 green, ALL frozen 210-candidates fail -> 210 decorative) /
MOMENT-INCIDENCE-DEAD (K1 or K2 fires) / TEST-VOID (a must-fail
control does not fire).

HONESTY FENCE: exact integer/symbolic algebra; the moment derivation
reproduces the certified 120 from K5 incidence [E neu candidate]; the
15/10/60 charpoly coefficients and the Newton tie are audit
fingerprints [C]; 72 is audit-only with NO morphism; the 210 decision
is preregistered with either outcome acceptable.  No physics claim, no
marker move; ROOTCLASS-MIXED (v775) untouched.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface
beruehrt.  Exakte Ganzzahl-Arithmetik; sympy nur fuer die symbolischen
Identitaeten und das charakteristische Polynom (gated); keine Floats,
kein RNG, kein Fit, kein freier Parameter.

Sources (read-only): verification/v774_arf_spinor_compiler.py /
experiments/tfpt-discovery/arf_spinor_compiler_probe.py (X, iota,
master moment), verification/v2_carrier_pascal.py (Tr X^2 = 120),
verification/v55_coxeter_cycle.py (h(E8) = 30),
verification/v109_sheet_pairing.py + v111_quadratic_transport.py (the
tower 1 + 45 + 210 = 256; the 210 quartics), verification/
v700_orbit60_census.py (60 lines), v91 (dim A3 = 15),
verification/tfpt_constants.py (b1).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/carrier_moment_incidence_probe.py
"""

import itertools
import os
import sys
import time
from collections import Counter
from math import comb

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _VERIFY)

T0 = time.time()
CHECKS = []
KILLS = []


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ======================================================================
# carrier layer (verbatim conventions of v774)
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
X5 = (-2, -2, -2, 3, 3)
COLOUR = (0, 1, 2)                   # slots with X = -2
WEAK = (3, 4)                        # slots with X = 3


def iota(v):
    f1, f2, f3, a = v
    return (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)


def xval(v, X=X5):
    return sum(x * b for x, b in zip(X, iota(v)))


PAIRS = [(i, j) for i in range(5) for j in range(i + 1, 5)]


# ======================================================================
# S1 -- the one-line master moment
# ======================================================================
def s1_master_moment():
    section("S1: the one-line master moment from K5 incidence")
    norm2 = sum(x * x for x in X5)
    check("S1.1 |X|^2 = 3*4 + 2*9 = %d == 30 = h(E8) (v55; cross-check "
          "h = |R(E8)|/rank = 240/8 = %d)" % (norm2, 240 // 8),
          norm2 == 30 and 240 // 8 == 30 and 3 * 4 + 2 * 9 == 30,
          kill="K1")

    import sympy as sp               # gated: symbolic identities only
    xs = sp.symbols("x1:6")
    lhs = sum((xs[i] + xs[j]) ** 2 for i, j in PAIRS)
    diff = sp.expand(lhs - 3 * sum(x ** 2 for x in xs)
                     - (sum(xs)) ** 2)
    tr_sub = {xs[4]: -(xs[0] + xs[1] + xs[2] + xs[3])}
    diff_tr = sp.expand((lhs - 3 * sum(x ** 2 for x in xs)).subs(tr_sub))
    check("S1.2 SYMBOLIC IDENTITY (all 5-vectors): sum_{i<j}(x_i+x_j)^2 "
          "- 3 sum x_i^2 == (sum x_i)^2; hence == 0 for ALL traceless "
          "5-vectors (sympy, both expansions identically zero)",
          diff == 0 and diff_tr == 0, kill="K1")

    # the ten wt-2 words carry xval = X_i + X_j; the five wt-4 words
    # carry xval = -X_i (tracelessness)
    ten = [v for v in W16 if sum(iota(v)) == 2]
    five = [v for v in W16 if sum(iota(v)) == 4]
    ok_ten = True
    for v in ten:
        supp = tuple(k for k in range(5) if iota(v)[k] == 1)
        if xval(v) != X5[supp[0]] + X5[supp[1]]:
            ok_ten = False
    ok_five = True
    for v in five:
        miss = [k for k in range(5) if iota(v)[k] == 0][0]
        if xval(v) != -X5[miss]:
            ok_five = False
    tr10 = sum(xval(v) ** 2 for v in ten)
    tr5 = sum(xval(v) ** 2 for v in five)
    tr_all = sum(xval(v) ** 2 for v in W16)
    check("S1.3 MOMENT LADDER: Tr_10 X^2 = sum_{i<j}(X_i+X_j)^2 = %d == "
          "90 = 3|X|^2; Tr_5bar X^2 = sum_i X_i^2 = %d == 30; singlet 0; "
          "TOTAL Tr_{S+} X^2 = %d == 120 = 4|X|^2 = 4 h(E8) == the "
          "v2/v774 master moment (full census)" % (tr10, tr5, tr_all),
          ok_ten and ok_five and tr10 == 90 and tr5 == 30
          and tr_all == 120 and tr_all == 4 * 30
          and len(ten) == 10 and len(five) == 5, kill="K1")

    from tfpt_constants import b1    # read-only corpus import
    check("S1.4 CHAIN re-anchored: 120/3 = 40, +1 = 41 = 10 b1 "
          "(tfpt_constants), 2*120 = 240, +8 = 248",
          120 // 3 == 40 and 41 == 40 + 1 and int(10 * b1) == 41
          and 2 * 120 == 240 and 240 + 8 == 248, kill="K1")


# ======================================================================
# S2 -- the characteristic polynomial
# ======================================================================
def s2_charpoly():
    section("S2: chi_X(t) = (t+2)^3 (t-3)^2 -- fingerprints 15/10/60, "
            "72 audit-only")
    import sympy as sp
    t = sp.symbols("t")
    chi = sp.expand(sp.prod(t - x for x in X5))
    chi_fact = sp.expand((t + 2) ** 3 * (t - 3) ** 2)
    chi_frozen = t ** 5 - 15 * t ** 3 - 10 * t ** 2 + 60 * t + 72
    check("S2.1 chi_X(t) = (t+2)^3 (t-3)^2 = t^5 - 15 t^3 - 10 t^2 + "
          "60 t + 72 (exact expansion, both routes)",
          sp.expand(chi - chi_fact) == 0
          and sp.expand(chi - chi_frozen) == 0, kill="K2")

    es = [0] * 6
    for k in range(1, 6):
        es[k] = sum(sp.prod(c) for c in itertools.combinations(X5, k))
    check("S2.2 elementary symmetric (e1..e5) = (%d, %d, %d, %d, %d) == "
          "(0, -15, 10, 60, -72); TYPED [C] audit fingerprints: 15 = "
          "dim A3 (v91), 10 = |E(K5)|, 60 = mu4-lines (v700); 72 "
          "AUDIT-ONLY, no morphism (honesty bar)"
          % (es[1], es[2], es[3], es[4], es[5]),
          (es[1], es[2], es[3], es[4], es[5]) == (0, -15, 10, 60, -72),
          kill="K2")


# ======================================================================
# S3/S4 -- the fourth moment 210: frozen candidate analysis
# ======================================================================
GAMMAS = list(range(10))             # gamma g lives in slot g // 2


def slot_of(g):
    return g // 2


def lift_slot_perm(pi):
    """slot permutation -> gamma permutation (pairs as blocks)."""
    return tuple(2 * pi[g // 2] + (g % 2) for g in GAMMAS)


def slot_group_S3xS2():
    perms = []
    for p3 in itertools.permutations(COLOUR):
        for p2 in itertools.permutations(WEAK):
            pi = list(range(5))
            for a, b in zip(COLOUR, p3):
                pi[a] = b
            for a, b in zip(WEAK, p2):
                pi[a] = b
            perms.append(tuple(pi))
    return perms


def gamma_group(with_flips):
    """G as list of (gamma-perm, slot-perm) pairs."""
    out = []
    for pi in slot_group_S3xS2():
        base = lift_slot_perm(pi)
        if not with_flips:
            out.append((base, pi))
            continue
        for flips in itertools.product((0, 1), repeat=5):
            g = tuple(base[gg] ^ flips[slot_of(base[gg])]
                      for gg in GAMMAS)
            out.append((g, pi))
    return out


def act_subset(perm, S):
    return frozenset(perm[g] for g in S)


def occupancy(S):
    m = [0] * 5
    for g in S:
        m[slot_of(g)] += 1
    return tuple(m)


def orbit_census(group, subsets):
    orbits = []
    seen = set()
    for S in subsets:
        if S in seen:
            continue
        orb = {act_subset(g, S) for g, _ in group}
        seen |= orb
        orbits.append(sorted(orb, key=sorted))
    return orbits


def equivariant_total_maps(group, orbits, fibers_wanted):
    """enumerate ALL total G-equivariant maps subsets -> slots; return
    (n_obstructed_orbits, all_solutions).  A map on a transitive orbit
    with representative x and stabiliser H sends x to a slot fixed by H
    (else ill-defined); the orbit then surjects onto the G-orbit of
    that slot with equal fibers |O| / |G.s|."""
    slot_orbit = {}
    for s in range(5):
        slot_orbit[s] = frozenset(pi[s] for _, pi in group)
    choices = []
    n_obstructed = 0
    for orb in orbits:
        x = orb[0]
        H = [pi for g, pi in group if act_subset(g, x) == x]
        allowed = [s for s in range(5) if all(pi[s] == s for pi in H)]
        # well-defined equivariant image also needs equal fibers:
        # |O| divisible by |G.s|
        allowed = [s for s in allowed
                   if len(orb) % len(slot_orbit[s]) == 0]
        if not allowed:
            n_obstructed += 1
        choices.append((orb, allowed))
    if n_obstructed:
        return n_obstructed, []
    sols = []
    def rec(k, fib):
        if k == len(choices):
            if tuple(fib) == tuple(fibers_wanted):
                sols.append(tuple())
            return
        orb, allowed = choices[k]
        for s in allowed:
            so = slot_orbit[s]
            share = len(orb) // len(so)
            fib2 = list(fib)
            ok = True
            for s2 in so:
                fib2[s2] += share
                if fib2[s2] > fibers_wanted[s2]:
                    ok = False
            if ok:
                rec(k + 1, fib2)
    rec(0, [0] * 5)
    return 0, sols


def s3_fourth_moment():
    section("S3: p4(X) = 210 -- the frozen candidate analysis")
    p4 = sum(x ** 4 for x in X5)
    check("S3.1 [I1] p4(X) = 3*2^4 + 2*3^4 = 48 + 162 = %d == 210 = "
          "C(10,4) = the quartic level of the tower 1 + 45 + 210 = 256 "
          "(v109/v111); C(10,2) = 45; 256 = 16^2" % p4,
          p4 == 210 and comb(10, 4) == 210 and comb(10, 2) == 45
          and 1 + 45 + 210 == 256 == 16 ** 2)

    # Newton tie on the traceless locus: p4 = 2 e2^2 - 4 e4
    import sympy as sp
    xs = sp.symbols("x1:6")
    e2 = sum(sp.prod(c) for c in itertools.combinations(xs, 2))
    e4 = sum(sp.prod(c) for c in itertools.combinations(xs, 4))
    p4s = sum(x ** 4 for x in xs)
    tr_sub = {xs[4]: -(xs[0] + xs[1] + xs[2] + xs[3])}
    newton_tr = sp.expand((p4s - 2 * e2 ** 2 + 4 * e4).subs(tr_sub))
    check("S3.2 [I1] NEWTON TIE (traceless locus, symbolic): p4 = "
          "2 e2^2 - 4 e4; numerically 2*(-15)^2 - 4*60 = 450 - 240 = "
          "210 -- generic symmetric-function algebra, typed [C] audit, "
          "NOT an operator map",
          newton_tr == 0 and 2 * (-15) ** 2 - 4 * 60 == 210)

    subsets = [frozenset(c) for c in itertools.combinations(GAMMAS, 4)]
    occ = Counter()
    for S in subsets:
        m = occupancy(S)
        n2 = sum(1 for a in m if a == 2)
        n1 = sum(1 for a in m if a == 1)
        occ[(n2, n1)] += 1
    check("S4.1 OCCUPANCY CENSUS: 210 = %d (type (2,2)) + %d (type "
          "(2,1,1)) + %d (type (1,1,1,1)) == 10 + 120 + 80"
          % (occ[(2, 0)], occ[(1, 2)], occ[(0, 4)]),
          occ[(2, 0)] == 10 and occ[(1, 2)] == 120 and occ[(0, 4)] == 80
          and len(subsets) == 210, kill="K1")

    fibers = tuple(x ** 4 for x in X5)      # (16, 16, 16, 81, 81)
    verdict_I2 = {}
    for name, with_flips in (("S3xS2 (order 12)", False),
                             ("Z2^5 : (S3xS2) (order 384)", True)):
        G = gamma_group(with_flips)
        orbits = orbit_census(G, subsets)
        sizes = sorted(len(o) for o in orbits)
        fixed = [o[0] for o in orbits if len(o) == 1]
        n_obs, sols = equivariant_total_maps(G, orbits, fibers)
        verdict_I2[name] = (len(orbits), sizes, fixed, n_obs, len(sols))
        print("    [I2/gammas, G = %s] %d orbits, sizes %s" %
              (name, len(orbits), sizes))
        print("        G-fixed 4-subsets: %s" %
              [sorted(f) for f in fixed])
        check("S3.3 [I2] G = %s on gamma 4-subsets: FIXED-POINT "
              "OBSTRUCTION -- the fixed subset {6,7,8,9} (both weak "
              "pairs) exists, NO G-fixed slot exists, so %d orbit(s) "
              "admit no equivariant image; total equivariant maps with "
              "fibers (16,16,16,81,81): %d == 0 -- candidate KILLED"
              % (name, n_obs, len(sols)),
              frozenset({6, 7, 8, 9}) in fixed and n_obs >= 1
              and len(sols) == 0)

    # I2 on the K5-edge indexing (G = S3 x S2 on vertices -> edges)
    eidx = {e: k for k, e in enumerate(PAIRS)}
    edge_perms = []
    for pi in slot_group_S3xS2():
        edge_perms.append((tuple(eidx[tuple(sorted((pi[a], pi[b])))]
                                 for (a, b) in PAIRS), pi))
    esubsets = [frozenset(c) for c in itertools.combinations(range(10), 4)]
    eorbits = orbit_census(edge_perms, esubsets)
    efixed = [o[0] for o in eorbits if len(o) == 1]
    fixed_expected = frozenset({eidx[(3, 4)], eidx[(0, 1)],
                                eidx[(0, 2)], eidx[(1, 2)]})
    n_obs_e, sols_e = equivariant_total_maps(edge_perms, eorbits, fibers)
    check("S3.4 [I2] K5-EDGE indexing (C(10,4) on E(K5), G = S3xS2): "
          "fixed 4-subset {edge 45 + triangle 123} exists, no fixed "
          "vertex; obstructed orbits %d >= 1; total equivariant maps: "
          "%d == 0 -- candidate KILLED" % (n_obs_e, len(sols_e)),
          fixed_expected in efixed and n_obs_e >= 1 and len(sols_e) == 0)

    # I3: slot-local weighted identities (symbolic generating function)
    t = sp.symbols("t")
    x = sp.symbols("x")
    CANDS = [("(1, x, x^2)", (sp.Integer(1), x, x ** 2)),
             ("(1, x^2, x^4)", (sp.Integer(1), x ** 2, x ** 4)),
             ("(1, 0, x^2)", (sp.Integer(1), sp.Integer(0), x ** 2)),
             ("(1, 0, x^4)", (sp.Integer(1), sp.Integer(0), x ** 4)),
             ("(1, x, x^4)", (sp.Integer(1), x, x ** 4)),
             ("(1, x^2, x^2)", (sp.Integer(1), x ** 2, x ** 2))]
    p4s_tr = sp.expand(p4s.subs(tr_sub))
    any_identity = False
    for cname, (c0, c1, c2) in CANDS:
        prod = sp.Integer(1)
        for xi in xs:
            prod *= (c0.subs(x, xi) + 2 * t * c1.subs(x, xi)
                     + t ** 2 * c2.subs(x, xi))
        N = sp.expand(prod).coeff(t, 4)
        gen_ok = sp.expand(N - p4s) == 0
        tr_ok = sp.expand(sp.expand(N).subs(tr_sub) - p4s_tr) == 0
        Nnum = N.subs({xs[i]: X5[i] for i in range(5)})
        if gen_ok or tr_ok:
            any_identity = True
        print("    [I3] c = %-14s N(X frozen) = %6s; identity general: "
              "%s; traceless: %s" % (cname, Nnum, gen_ok, tr_ok))
    check("S3.5 [I3] NONE of the six frozen slot-local weight families "
          "reproduces p4(X) (neither generally nor on the traceless "
          "locus) -- no weighted identity in the frozen list",
          not any_identity)

    # I4: the partial miss-slot map on the 80 type-(1,1,1,1) subsets
    miss_fibers = Counter()
    for S in subsets:
        m = occupancy(S)
        if sorted(m) == [0, 1, 1, 1, 1]:
            miss_fibers[m.index(0)] += 1
    leftover = 210 - sum(miss_fibers.values())
    deficit = [fibers[s] - miss_fibers[s] for s in range(5)]
    check("S3.6 [I4] PARTIAL miss-slot map: the 80 type-(1,1,1,1) "
          "subsets -> missed slot, uniform fibers %s == 16 = 2^4 = "
          "X_i^4 on the COLOUR slots exactly; weak slots need 81, "
          "deficit %s; leftover 130 = 10 + 120 pair-containing -- an "
          "honest PARTIAL structure, not a bijection"
          % (dict(sorted(miss_fibers.items())), deficit[3:]),
          all(miss_fibers[s] == 16 for s in range(5))
          and deficit[:3] == [0, 0, 0] and deficit[3:] == [65, 65]
          and leftover == 130)

    print("    [I5] alphabet reading recorded: p4 = sum |X_i|^4 = # "
          "(slot, 4-word over alphabet |X_i|); gamma pairs give "
          "alphabet 2 on every slot -- no canonical alphabet-3 "
          "structure on the weak slots in the frozen corpus objects.")
    return any_identity


# ======================================================================
# C -- must-fail controls
# ======================================================================
def c_controls():
    section("C: must-fail controls")
    Xp = (-2, -2, -2, 3, 4)
    resid = (sum((Xp[i] + Xp[j]) ** 2 for i, j in PAIRS)
             - 3 * sum(x * x for x in Xp))
    mm = sum(xval(v, Xp) ** 2 for v in W16)
    check("C1 CONTROL FIRES: non-traceless X' = (-2,-2,-2,3,4): "
          "sum_{i<j}(X'_i+X'_j)^2 - 3|X'|^2 = %d = (sum X')^2 != 0, and "
          "the master-moment census gives %d != 120" % (resid, mm),
          resid == 1 and sum(Xp) == 1 and mm != 120)

    Xpp = (-2, -2, -2, 3, 2)
    p4pp = sum(x ** 4 for x in Xpp)
    import sympy as sp
    t = sp.symbols("t")
    chi_pp = sp.expand(sp.prod(t - x for x in Xpp))
    chi_frozen = t ** 5 - 15 * t ** 3 - 10 * t ** 2 + 60 * t + 72
    check("C2 CONTROL FIRES: mutated X'' = (-2,-2,-2,3,2): p4 = %d != "
          "210 and chi_X'' != the frozen charpoly" % p4pp,
          p4pp == 145 and sp.expand(chi_pp - chi_frozen) != 0)


# ======================================================================
def main():
    print("=" * 78)
    print("CARRIER.MOMENT.INCIDENCE.01 -- master moment from K5 "
          "incidence; charpoly; the 210 decision")
    print("=" * 78, flush=True)
    s1_master_moment()
    s2_charpoly()
    found_210_map = s3_fourth_moment()
    c_controls()

    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    controls_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    print("%d/%d checks passed" % (n_pass, n_all))
    if not controls_ok:
        verdict = "TEST-VOID"
        print("VERDICT: TEST-VOID -- a must-fail control does not fire; "
              "the test measures nothing.")
    elif KILLS:
        verdict = "MOMENT-INCIDENCE-DEAD"
        print("VERDICT: MOMENT-INCIDENCE-DEAD -- kills fired: %s"
              % sorted(set(KILLS)))
    elif n_pass == n_all and found_210_map:
        verdict = "MOMENT-INCIDENCE-EXACT"
        print("VERDICT: MOMENT-INCIDENCE-EXACT -- moments + charpoly "
              "exact AND a frozen 210-candidate certified.")
    elif n_pass == n_all:
        verdict = "MOMENT-INCIDENCE-PARTIAL"
        print("VERDICT: MOMENT-INCIDENCE-PARTIAL -- the one-line master "
              "moment Tr_{S+} X^2 = 4|X|^2 = 4 h(E8) = 120 and the "
              "charpoly (t+2)^3 (t-3)^2 are EXACT [E neu candidates]; "
              "the fourth moment p4 = 210 = C(10,4) stays DECORATIVE: "
              "the equivariant-bijection candidates are killed by the "
              "fixed-point obstruction (both groups, both indexings), "
              "no frozen weighted identity holds, and only the partial "
              "miss-slot map (80 -> 5 x 16) survives -- an audit "
              "fingerprint at counting level, per the frozen rule.")
    else:
        verdict = "MOMENT-INCIDENCE-DEAD"
        print("VERDICT: MOMENT-INCIDENCE-DEAD -- non-kill check failed; "
              "see FAIL lines.")
    print("Verdict enum: %s" % verdict)
    print("Runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
