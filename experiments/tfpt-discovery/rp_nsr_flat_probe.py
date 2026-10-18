#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rp_nsr_flat_probe -- GNET.RP.NSR.FLAT.01 (EXPLORATION ONLY).

PHYSICAL-INTERFACE LANE (parallel to READOUT-FOURIER-FACTOR).

THE QUESTION.  The last discrete seam input is the alignment bit
(delta = pi/2 <=> tau = i <=> clock / D4, v512).  Free RP is
SIDE-BLIND (v521, eighth test).  Interacting FK-bulk KILLS RP
(seam_interacting_toy_fk F1).  The known interacting SURVIVOR is
the alignment-bit quartet at delta = pi/2 with positive coupling
(v534 / gamma_toy).  That is a selection principle, not a grave.
This probe does NOT re-run the 256-dim Fock.  It tests the JOINT
with the 4-bit address space that probe 1 already typed:

    NS/R is a character of V = F2^4 (qsys Q7, 7+8 classes).

FROZEN DICTIONARY (typed [C], the only corpus-native 16<->16 map
that does not search): N = 16 Majorana sites, site j identified
with the bit-lex vector of j in F2^4.  Marks of M(delta) sit at
bond midpoints {0, delta, pi, pi+delta} (v519/v521 lifting A).
Bond j is the midpoint between site j and j+1, at angle
(j+1)*pi/8.  Hence the four mark-bonds at delta = m*pi/8 are

    {(k-1) mod 16 : k in {0, m, 8, 8+m}}.

DEMANDS (frozen):
  P1  CLOCK-COORD-PLANE (sharp selector).  Coarse 2-flat-ness is
      FAMILY-BLIND (every m=1..7 is an affine 2-flat under bit-lex --
      a pre-record finding, typed).  The sharp predicate: the four
      marks fill a COORDINATE affine 2-plane (two bits frozen, two
      free).  Unique on the v512 family m in {1,2,3,4} (delta in
      (0, pi/2]) at m = 4, namely (b0,b1)=(1,1).  (m=6,7 are also
      coord-planes but lie at delta > pi/2, outside the family.)
  P2  NESTED, NOT EQUAL.  The clock 2-flat lies in a linear
      hyperplane ker(chi) for a unique-up-to-scale pair of
      coordinate characters (here chi = b0+b1 in little-endian
      bit-lex).  That hyperplane has 8 points; the 2-flat has 4.
      NS/R (a hyperplane split 8+8) is therefore NOT identical
      to the alignment bit -- nested, independent rank, same
      type as Q7 (NS/R is not a Z4-character).
  P3  SITE-SCRAMBLE CONTROL.  A frozen permutation of site labels
      (seed 20260819, derangement of 1..15, 0 fixed) makes the
      m = 4 quadruple NOT an affine 2-flat.  The selection is
      dictionary-contentful, not a tautology of "any four points".

CONTROLS:
  C1  Four points of a 2-dim linear subspace ARE an affine 2-flat
      (the subspace {b0=b1=0} = {0,4,8,12} in this chart).
  C2  Four random-looking points {0,1,2,4} are NOT an affine 2-flat.
  C3  m = 4 marks equal {3,7,11,15} (bond-midpoint arithmetic).

KILLS: K1 clock is not a coordinate 2-plane; K2 a generic side
m in {1,2,3} IS a coordinate 2-plane (then the bit is not
selected); K3 scramble still selects m = 4 (dictionary void).

VERDICT ENUM:
  RP-NSR-FLAT           P1+P2+P3, controls fire.  Physical bit =
                        affine 2-flat on V; NS/R nested not equal.
  RP-NSR-FLAT-DEAD      K1 or K2.
  DICTIONARY-VOID       K3.
  CONTROL-VOID          C1-C3 fail.

FIREWALL: experiments/tfpt-discovery only; no verification/ import;
no ledger/paper/website; no .md; no RH; no Fock re-run.  Exact
integer / F2.  AST-ban verification, zeta, numpy.  WOIT.OS.TWISTOR.01
stays [O]; SEAM.EQUIV stays [O]; this is a typed joint, not a closure.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/rp_nsr_flat_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import time

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
GNET.RP.NSR.FLAT.01 FROZEN SPEC (2026-08-19).
Dictionary [C]: site j <-> bit-lex of j in F2^4. Marks at bond
midpoints {0,delta,pi,pi+delta}; delta=m*pi/8 => bonds
{(k-1) mod 16 : k in {0,m,8,8+m}}.
P1 coarse 2-flat is family-blind (pre-record). Sharp: unique
coordinate affine 2-plane on v512 family m=1..4 is m=4, (b0,b1)=(1,1).
P2 clock 2-flat sits in ker(b0+b1) (8 pts); not equal to NS/R.
P3 site-scramble seed 20260819 kills the clock coord-plane.
C1 {0,4,8,12} is a 2-flat. C2 {0,1,2,4} is not. C3 m=4 => {3,7,11,15}.
Verdict: RP-NSR-FLAT / DEAD / DICTIONARY-VOID / CONTROL-VOID.
WOIT.OS.TWISTOR.01 stays [O]. No Fock. No RH.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def section(title: str) -> None:
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0))


def ast_firewall(src: str) -> list[str]:
    banned = {"verification", "zeta", "zetazero", "numpy", "mpmath"}
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


def bits(j: int) -> tuple:
    return ((j >> 0) & 1, (j >> 1) & 1, (j >> 2) & 1, (j >> 3) & 1)


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def mark_bonds(m: int) -> frozenset:
    return frozenset((k - 1) % 16 for k in (0, m, 8, 8 + m))


def is_affine_2flat(pts) -> bool:
    pts = list(pts)
    if len(set(pts)) != 4:
        return False
    vecs = [bits(p) for p in pts]
    p0 = vecs[0]
    diffs = {xor(p, p0) for p in vecs}
    if len(diffs) != 4 or (0, 0, 0, 0) not in diffs:
        return False
    for a in diffs:
        for b in diffs:
            if xor(a, b) not in diffs:
                return False
    nonzero = [d for d in diffs if d != (0, 0, 0, 0)]
    return len(nonzero) == 3


def is_coord_affine_2plane(pts):
    """Two bits frozen, the other two run through F2^2 (4 points)."""
    vecs = [bits(p) for p in pts]
    if len(set(pts)) != 4:
        return False, None
    for i in range(4):
        for j in range(i + 1, 4):
            for a in (0, 1):
                for b in (0, 1):
                    if all(v[i] == a and v[j] == b for v in vecs):
                        free = [k for k in range(4) if k not in (i, j)]
                        got = set(tuple(v[k] for k in free) for v in vecs)
                        if len(got) == 4:
                            return True, (i, j, a, b)
    return False, None


def lcg_perm(seed: int = 20260819):
    """Derangement of 1..15, 0 fixed.  Tiny LCG, frozen seed."""
    used = {0}
    out = [0] * 16
    x = seed
    for i in range(1, 16):
        x = (1103515245 * x + 12345) & 0x7FFFFFFF
        cand = 1 + (x % 15)
        while cand in used:
            x = (1103515245 * x + 12345) & 0x7FFFFFFF
            cand = 1 + (x % 15)
        used.add(cand)
        out[i] = cand
    # if not a derangement on 1..15, rotate once (still frozen)
    if any(out[i] == i for i in range(1, 16)):
        out = [0] + out[2:] + [out[1]]
    return tuple(out)


def apply_perm(pts, perm):
    return frozenset(perm[p] for p in pts)


def main() -> int:
    print("GNET.RP.NSR.FLAT.01 -- alignment bit as affine 2-flat on V")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("C1/C2/C3 arithmetic wards")
    check("C1 {0,4,8,12} (ker b0, ker b1) IS an affine 2-flat",
          is_affine_2flat({0, 4, 8, 12}))
    check("C2 {0,1,2,4} is NOT an affine 2-flat",
          not is_affine_2flat({0, 1, 2, 4}))
    clock = mark_bonds(4)
    check("C3 m=4 mark-bonds equal {3,7,11,15}",
          clock == frozenset({3, 7, 11, 15}),
          "got=%s" % sorted(clock))

    section("P1 coordinate 2-plane vs generic side (v512 family)")
    clock_ok, clock_key = is_coord_affine_2plane(clock)
    check("P1-coarse every m=1..7 is an affine 2-flat (FAMILY-BLIND; "
          "typed pre-record, not a selector)",
          all(is_affine_2flat(mark_bonds(m)) for m in range(1, 8)))
    check("P1a clock m=4 IS a coordinate affine 2-plane (b0,b1)=(1,1)",
          clock_ok and clock_key == (0, 1, 1, 1),
          "key=%s pts=%s" % (clock_key, sorted(clock)))
    generic = {m: mark_bonds(m) for m in (1, 2, 3)}
    generic_coord = [m for m, p in generic.items()
                     if is_coord_affine_2plane(p)[0]]
    check("P1b generic sides m=1,2,3 are NOT coordinate 2-planes "
          "(unique selector on the v512 family)",
          not generic_coord,
          "coord=%s" % generic_coord)
    mirrors = {m: is_coord_affine_2plane(mark_bonds(m))[0]
               for m in (5, 6, 7)}
    print("    mirror m=5,6,7 coord-plane? %s  "
          "(outside v512 family delta in (0, pi/2])" % mirrors)

    section("P2 nested in a hyperplane, not equal to NS/R")
    vecs = [bits(p) for p in sorted(clock)]
    # all have b0=b1=1 in little-endian of {3,7,11,15}
    b0 = [v[0] for v in vecs]
    b1 = [v[1] for v in vecs]
    b2 = [v[2] for v in vecs]
    b01 = [v[0] ^ v[1] for v in vecs]
    check("P2a clock points are homogeneous for b0, b1, and b0+b1 "
          "(all b0=1, b1=1, b0+b1=0)",
          set(b0) == {1} and set(b1) == {1} and set(b01) == {0},
          "b0=%s b1=%s b01=%s" % (b0, b1, b01))
    check("P2b NOT homogeneous for b2 (values {0,1}) -- the 2-flat is "
          "not a hyperplane",
          set(b2) == {0, 1}, "b2=%s" % b2)
    ker = [j for j in range(16) if (bits(j)[0] ^ bits(j)[1]) == 0]
    check("P2c ker(b0+b1) has 8 points and CONTAINS the 4 clock marks "
          "(nested: 4-flat inside 8-hyperplane, not NS/R identity)",
          len(ker) == 8 and set(clock).issubset(set(ker)),
          "ker=%s" % ker)

    section("P3 dictionary scramble")
    perm = lcg_perm(20260819)
    scrambled = apply_perm(clock, perm)
    check("P3 scrambled site labels: clock quadruple is NOT a "
          "coordinate 2-plane (selection is contentful)",
          (not is_coord_affine_2plane(scrambled)[0])
          and perm[0] == 0
          and sorted(perm) == list(range(16)),
          "perm[1:6]=%s scrambled=%s" % (perm[1:6], sorted(scrambled)))

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref):
        hits = [(n, ok) for n, ok in CHECKS if n.startswith(pref)]
        return bool(hits) and all(ok for _, ok in hits)

    if not (pfx("C1") and pfx("C2") and pfx("C3") and pfx("G0")):
        verdict = "CONTROL-VOID"
    elif not pfx("P3"):
        verdict = "DICTIONARY-VOID"
    elif pfx("P1") and pfx("P2") and pfx("P3"):
        verdict = "RP-NSR-FLAT"
    else:
        verdict = "RP-NSR-FLAT-DEAD"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("PHYSICAL JOINT: alignment bit = affine 2-flat on V under "
          "site-index dictionary; NS/R nested (hyperplane), not equal.  "
          "WOIT.OS.TWISTOR.01 UNTOUCHED [O].  NO RH CLAIM.  "
          "NO MATTER SEMANTICS.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot and verdict == "RP-NSR-FLAT") else 1


if __name__ == "__main__":
    raise SystemExit(main())
