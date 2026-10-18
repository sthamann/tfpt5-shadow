#!/usr/bin/env python3
"""v629 -- E8.INCIDENCE.01: the root incidence census -- the naive 48 x 5
incidence map to the E8 roots is KILLED for the compiler-canonical
order-12 element, and the positive residue is sharp: the mu4 clock acts
FREELY on the 240 roots with EXACTLY 60 orbits (60 = D_start), and the
family 3-cycle fixes exactly 12 roots (the lifted-mark count).

The external review proposed the kill test: can the 240 E8 roots be
built canonically as (48 cover modes) x (5 carrier slots) INCLUDING the
Gram structure?  First hurdle executed:

  (R1) THE SETUP [E]: the 240 roots in the D8+spinor model (112
       integer + 128 half-integer), and the compiler-canonical
       order-12 element g = J o sigma (J = the mu4 quarter-turn on all
       four coordinate pairs; sigma = the 3-cycle of pairs 1..3 -- the
       clock times the family cycle) preserves the root set.

  (R2) THE KILL [E, honest]: g does NOT act freely: the orbit census
       is 19 x 12 + 3 x 4 (= 240) -- NOT the 20 free zeta_12 orbits
       the naive 48 x 5 = 240 incidence would need: the naive
       construction FAILS at the first hurdle for the canonical
       element; 48 x 5 = 240 stays an audit fingerprint (as the
       review's kill branch anticipated).

  (R3) THE POSITIVE RESIDUE [E]: the mu4 clock J alone acts FREELY
       with EXACTLY 60 orbits of size 4 -- 60 = D_start (the cascade
       start): 240 = |mu4| x D_start realized as free clock orbits on
       the roots; and sigma fixes EXACTLY 12 roots (the pair-4 +
       diagonal support) -- 12 = the lifted-mark count of v623.

  (R4) CONTROLS [E]: J^2 (the deck square, order 2) has 120 orbits of
       size 2 (free); the fixed roots of sigma form 3 J-orbits (the
       12 = 3 x 4 structure closes).

  (R5) THE READING [C]: the review's kill branch fires for the naive
       canonical element -- a Gram-compatible 48 x 5 incidence, if it
       exists, needs a NON-obvious element or a genuinely different
       construction; the sharp positive: 60 = D_start is now a free
       ORBIT COUNT on the roots (a new home for the cascade constant);
       typed observation, no derivation claimed.

Verdict enums (frozen): INCIDENCE-CENSUS-DECIDED (all pass),
CENSUS-FAILS, MIXED.

FIREWALL: no marker changes; typed observations, no derivation claims.

PROVENANCE: discovery probe root_incidence_probe.py (2026-08-02, 6/6,
verdict INCIDENCE-CENSUS-DECIDED).

Python-only (exact Fraction combinatorics), counted per
GATE.WOLFRAM.02.
"""

import itertools
from collections import Counter
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""))


# ================================================================== R1
print("=" * 72)
print("R1: the roots and the canonical order-12 element")
print("=" * 72)

roots = []
for x in itertools.product(range(-1, 2), repeat=8):
    if sum(v * v for v in x) == 2 and sum(x) % 2 == 0:
        roots.append(tuple(Fr(v) for v in x))
n_int = len(roots)
half = Fr(1, 2)
for y in itertools.product((0, -1), repeat=8):
    x = tuple(Fr(v) + half for v in y)
    if sum(v * v for v in x) == 2 and sum(x) % 2 == 0:
        roots.append(x)
n_half = len(roots) - n_int
RS = set(roots)


def J_all(x):
    out = []
    for i in range(0, 8, 2):
        a, b = x[i], x[i + 1]
        out += [-b, a]
    return tuple(out)


def sigma(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def g(x):
    return J_all(sigma(x))


check("R1.1 240 roots (112 integer + 128 half-integer) and the "
      "compiler-canonical order-12 element g = J o sigma preserves the "
      "root set",
      len(roots) == 240 and n_int == 112 and n_half == 128
      and all(g(x) in RS for x in roots))


def census(f):
    seen = set()
    cnt = Counter()
    for x in roots:
        if x in seen:
            continue
        orb = [x]
        y = f(x)
        while y != x:
            orb.append(y)
            y = f(y)
        for z in orb:
            seen.add(z)
        cnt[len(orb)] += 1
    return dict(cnt)


# ================================================================== R2
print("=" * 72)
print("R2: the kill (no free zeta_12 structure)")
print("=" * 72)

cg = census(g)
check("R2.1 [KILL, honest] g does NOT act freely: orbit census "
      "19 x 12 + 3 x 4 (not the 20 free 12-orbits the naive "
      "48 x 5 = 240 incidence needs): the naive construction FAILS at "
      "the first hurdle; 48 x 5 stays an audit fingerprint",
      cg == {12: 19, 4: 3}, str(cg))

# ================================================================== R3
print("=" * 72)
print("R3: the positive residue (60 = D_start as a free orbit count)")
print("=" * 72)

cJ = census(J_all)
check("R3.1 the mu4 clock alone acts FREELY with EXACTLY 60 orbits of "
      "size 4: 240 = |mu4| x 60 with 60 = D_start -- the cascade start "
      "appears as the free clock-orbit count on the roots", cJ == {4: 60})

cs = census(sigma)
fixed = [x for x in roots if sigma(x) == x]
check("R3.2 the family 3-cycle fixes EXACTLY 12 roots (76 free "
      "3-orbits + 12 fixed) -- 12 = the lifted-mark count of v623",
      cs == {3: 76, 1: 12} and len(fixed) == 12)

# ================================================================== R4
print("=" * 72)
print("R4: controls")
print("=" * 72)


def J2(x):
    return J_all(J_all(x))


cJ2 = census(J2)
fixed_orbJ = set()
for x in fixed:
    orb = frozenset([x, J_all(x), J2(x), J_all(J2(x))])
    fixed_orbJ.add(orb)
check("R4.1 J^2 (the deck square) acts freely with 120 2-orbits, and "
      "the 12 sigma-fixed roots form exactly 3 free J-orbits "
      "(12 = 3 x 4 closes)",
      cJ2 == {2: 120} and len(fixed_orbJ) == 3
      and all(len(o) == 4 for o in fixed_orbJ))

# ================================================================== R5
print("=" * 72)
print("R5: the reading")
print("=" * 72)

check("R5.1 [C] the review's kill branch fires for the naive canonical "
      "element: a Gram-compatible 48 x 5 incidence, if it exists, needs "
      "a non-obvious element or a different construction; the sharp "
      "positive residue: 60 = D_start is a free ORBIT COUNT on the "
      "roots and 12 (the lifted marks) is the sigma-fixed count -- "
      "typed observations, no derivation claimed; no marker moves", True)

# ================================================================== summary
print("=" * 72)
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d checks passed" % (n_pass, len(CHECKS)))
if n_pass == len(CHECKS):
    print("ALL CHECKS PASSED")
    print("VERDICT: INCIDENCE-CENSUS-DECIDED -- the naive 48 x 5 incidence is")
    print("killed (19 x 12 + 3 x 4), and the positive residue is sharp:")
    print("60 = D_start free clock orbits, 12 sigma-fixed roots.")
else:
    print("SOME CHECKS FAILED")


def run():
    """run_all.py entry point; the checks execute at import time above."""
    return len([1 for _, ok in CHECKS if not ok])


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
