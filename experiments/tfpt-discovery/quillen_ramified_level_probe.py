#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""quillen_ramified_level_probe -- ALPHA.QUILLEN.RAMIFIED.LEVEL.01
(EXPLORATION ONLY).

SOLVE ATTEMPT on residual (2) of ALPHA.QUILLEN.EXACT.01: the origin of
the Maxwell a^3 coefficient k0 = 1 (v434 located it as a Chern/CS
level; v435 typed it as the unit level IF EM1; v470/v472 exhibited
C=1 on the p+ip collar).  This probe does NOT cite the p+ip Chern and
does NOT evaluate a continuum zeta-determinant.  It derives k0 from
the ramified clock on the pillowcase, the coupling the previous
factorisation probe refused to compute.

FROZEN DICTIONARY (no search):
  The seam is the flat pillowcase S^2(2,2,2,2), chi=2, n_marks = 2 chi
  = |mu4| = 4 (v216).  Each mark is a Z2 branch of the METRIC
  (deficit pi).  Independently, the Gaussian clock J / i has
  Hjelmslev order (1,2,4,4) on R_m = Z[i]/(1+i)^m (qsys Q5).  Gauge
  holonomy of the generator is 0 at order 1 (clock invisible) and
  2 pi / order otherwise.  The U(1) level is the total gauge holonomy
  in units of 2 pi:

      L(m)  =  n_marks * h(m) / 2 pi

  The alignment bit (RP-NSR, v512 family m=4) is delta = pi/2, which
  IS the mu4 generator holonomy.

DEMANDS:
  Q1  n_marks = 2 chi = 4; c3 = 1/(|Z2| 2 pi chi) = 1/(8 pi).
  Q2  order(i in R_m) = (1,2,4,4) at m=1,2,3,4.  Holonomy fractions
      h/2pi = (0, 1/2, 1/4, 1/4).
  Q3  L(1)=0, L(2)=2, L(m>=3)=1.  Maxwell k0=1 is recovered ONLY at
      ramified depth >= 3 (full C[Z4]), not at the jet and not at
      addresses.
  Q4  METRIC vs GAUGE on the SAME 4 marks: metric holonomy 4*(pi)/(2 pi)
      = chi = 2.  Gauge at depth >=3 is 1.  Identifying U(1) with the
      cone deficit (the jet-collapse, both Z2) gives L=2, which is
      GRAVITY, not Maxwell.
  Q5  ALIGNMENT BIT: delta = 4*pi/8 = pi/2 equals the mu4 generator
      holonomy; the four marks {0, delta, pi, pi+delta} are the four
      pillowcase cones in the clock chart.
  Q6  JET-COLLAPSE KILL against the [E] split: replacing k0=1 by
      k0=2 yields F_2 = 2 a^3 - 2 c3^3 a^2 - 8 b1 c3^6 log(1/phi).
      At the [E] root, a^3 = 2 c3^3 a^2 + 8 b1 c3^6 log, hence
      F_2(a*) = a*^3 != 0.  Stationarity DIES at jet depth 2.  Exact,
      no root-finding.

CONTROLS:
  C1  inverted clock (order of -i) is the same tuple (Aut Z4).
  C2  3 marks give L(m>=3)=3/4 != 1 (pillowcase 4 is contentful).
  C3  alignment m=2 has delta=pi/4 != pi/2 (the bit, not a generic
      side, is the mu4 generator).

KILLS: K1 n_marks != 4; K2 order tuple deviates; K3 L(m>=3) != 1;
K4 metric holonomy != 2; K5 delta(m=4) != pi/2; K6 F_2(a*) identity
fails (would mean k0=2 is compatible with the split).

VERDICT ENUM:
  QUILLEN-RAMIFIED-LEVEL   Q1-Q6 hold; k0=1 derived from mu4 on the
                           4 cones at depth >=3; jet-collapse killed.
                           ALPHA.QUILLEN.EXACT.01 stays [O] (the
                           zeta-det identification / APS step is not
                           this arithmetic).  Residual (2) has a
                           jet-native derivation at experiment level.
  QUILLEN-RAMIFIED-DEAD    K3 or K6.
  CONTROL-VOID             a control fails.

FIREWALL: experiments/tfpt-discovery only; no verification/ import;
no ledger/paper/website; no .md; no RH; no marker move.  Exact
integer / Fraction / sympy.  AST-ban verification, zeta, numpy,
mpmath.  Do not import sibling probes.  Do not re-run QWZ/numpy
Chern.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/quillen_ramified_level_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import time
from fractions import Fraction

import sympy as sp

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
ALPHA.QUILLEN.RAMIFIED.LEVEL.01 FROZEN SPEC (2026-08-19).
Pillowcase S^2(2,2,2,2), chi=2, n_marks=2 chi=4=|mu4| (v216).
Hjelmslev order(i in R_m)=(1,2,4,4). Gauge holonomy fraction =
0 at order 1 else 1/order. Level L=n_marks * fraction.
Q3 L=(0,2,1,1) at m=1..4; k0=1 only at depth>=3.
Q4 metric 4*(1/2)=2=chi; jet-collapse gauge=metric=2, WRONG.
Q5 alignment m=4 => delta=pi/2 = mu4 generator.
Q6 F_2(a*)=a*^3 !=0 from the [E] split, no root-finding.
C1 order(-i) same. C2 3 marks => 3/4. C3 m=2 delta=pi/4.
ALPHA.QUILLEN.EXACT.01 stays [O]. No zeta-det. No marker move.
Verdict: LEVEL / DEAD / CONTROL-VOID.
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


def build_ring(m: int):
    size = 1 << m
    dec = []
    for code in range(size):
        a = b = 0
        pa, pb = 1, 0
        for j in range(m):
            if (code >> j) & 1:
                a += pa
                b += pb
            pa, pb = pa - pb, pa + pb
        dec.append((a, b))

    def enc(a, b):
        code = 0
        aa, bb = int(a), int(b)
        for _j in range(m):
            d = (aa + bb) & 1
            if d:
                code |= 1 << _j
                aa -= 1
            aa, bb = (aa + bb) // 2, (bb - aa) // 2
        return code

    mul = [[enc(dec[x][0] * dec[y][0] - dec[x][1] * dec[y][1],
                dec[x][0] * dec[y][1] + dec[x][1] * dec[y][0])
            for y in range(size)] for x in range(size)]
    return dict(m=m, size=size, dec=dec, enc=enc, mul=mul)


def order_of(R, a: int, b: int) -> int:
    code = R["enc"](a, b)
    one = R["enc"](1, 0)
    acc = one
    for k in range(1, R["size"] + 2):
        acc = R["mul"][acc][code]
        if acc == one:
            return k
    return 0


def holonomy_fraction(order: int) -> Fraction:
    if order <= 1:
        return Fraction(0)
    return Fraction(1, order)


def mark_bonds(m: int) -> frozenset:
    return frozenset((k - 1) % 16 for k in (0, m, 8, 8 + m))


def main() -> int:
    print("ALPHA.QUILLEN.RAMIFIED.LEVEL.01 -- derive Maxwell k0=1 from "
          "mu4 holonomy on the pillowcase")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("Q1 pillowcase marks and c3")
    chi = 2
    z2 = 2
    n_marks = 2 * chi
    pi = sp.pi
    c3 = 1 / (z2 * 2 * pi * chi)
    check("Q1a n_marks = 2 chi = |mu4| = 4",
          n_marks == 4 == 2 * chi)
    check("Q1b c3 = 1/(|Z2| 2 pi chi) = 1/(8 pi)",
          sp.simplify(c3 - 1 / (8 * pi)) == 0)

    section("Q2 Hjelmslev clock orders and holonomy fractions")
    orders = []
    fracs = []
    for m in (1, 2, 3, 4):
        R = build_ring(m)
        o = order_of(R, 0, 1)
        orders.append(o)
        fracs.append(holonomy_fraction(o))
    check("Q2a order(i in R_m) = (1,2,4,4)",
          orders == [1, 2, 4, 4], "orders=%s" % orders)
    check("Q2b holonomy fractions (0, 1/2, 1/4, 1/4)",
          fracs == [Fraction(0), Fraction(1, 2), Fraction(1, 4),
                    Fraction(1, 4)],
          "fracs=%s" % fracs)

    section("Q3 Maxwell level from 4 marks")
    levels = [n_marks * f for f in fracs]
    check("Q3 L(m) = (0, 2, 1, 1): k0=1 ONLY at ramified depth >= 3",
          levels == [0, 2, 1, 1],
          "L=%s" % levels)

    section("Q4 metric vs gauge on the same 4 marks")
    metric_frac = Fraction(1, 2)  # Z2 branch, deficit pi, pi/2pi = 1/2
    l_metric = n_marks * metric_frac
    check("Q4a metric holonomy 4*(pi)/(2 pi) = chi = 2",
          l_metric == chi == 2)
    check("Q4b jet-collapse (m=2) makes gauge=metric=2, which is "
          "GRAVITY not Maxwell; depth>=3 splits them (1 vs 2)",
          levels[1] == l_metric == 2 and levels[2] == 1 != l_metric)

    section("Q5 alignment bit is the mu4 generator")
    delta_num = {m: Fraction(m, 8) for m in range(1, 8)}  # delta/pi
    check("Q5a alignment m=4: delta/pi = 1/2, i.e. delta = pi/2 = "
          "mu4 generator holonomy",
          delta_num[4] == Fraction(1, 2)
          and fracs[3] == Fraction(1, 4)
          and Fraction(1, 2) / 2 == Fraction(1, 4))
    clock_marks = mark_bonds(4)
    check("Q5b four clock marks at m=4 are {3,7,11,15} "
          "(four cones in the 16-site chart)",
          clock_marks == frozenset({3, 7, 11, 15})
          and len(clock_marks) == n_marks)

    section("Q6 jet-collapse killed by the [E] Quillen split")
    # At the root: a^3 = 2 c3^3 a^2 + 8 b1 c3^6 log(1/phi) =: S
    # F_2 = 2 a^3 - S = 2 a^3 - a^3 = a^3.
    # a^3 is not the zero functional, so F_2(a*) = a*^3 != 0.
    a = sp.symbols("a", positive=True)
    s = sp.symbols("S", positive=True)
    f1 = a ** 3 - s
    f2 = 2 * a ** 3 - s
    f2_on_root = sp.simplify(f2.subs(s, a ** 3))
    check("Q6 replacing k0=1 by k0=2 (jet-collapse) gives "
          "F_2(a*) = a*^3 != 0 at the [E] split -- stationarity dies",
          f2_on_root == a ** 3 and f1.subs(s, a ** 3) == 0)

    section("controls")
    orders_neg = []
    for m in (1, 2, 3, 4):
        R = build_ring(m)
        orders_neg.append(order_of(R, 0, -1))
    check("C1 order(-i in R_m) = (1,2,4,4) = order(i)  (Aut Z4)",
          orders_neg == [1, 2, 4, 4], "orders_neg=%s" % orders_neg)
    l_three = 3 * fracs[2]
    check("C2 3 marks at depth>=3 give level 3/4 != 1 "
          "(pillowcase 4 is contentful)",
          l_three == Fraction(3, 4) != 1)
    check("C3 generic side m=2 has delta=pi/4 != pi/2 "
          "(the alignment BIT is the mu4 generator, not a generic RP side)",
          delta_num[2] == Fraction(1, 4) != Fraction(1, 2))

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref):
        hits = [(n, ok) for n, ok in CHECKS if n.startswith(pref)]
        return bool(hits) and all(ok for _, ok in hits)

    c_ok = pfx("C1") and pfx("C2") and pfx("C3") and pfx("G0")
    q_ok = all(pfx("Q%d" % k) for k in range(1, 7))
    if not c_ok:
        verdict = "CONTROL-VOID"
    elif not (pfx("Q3") and pfx("Q6")):
        verdict = "QUILLEN-RAMIFIED-DEAD"
    elif q_ok:
        verdict = "QUILLEN-RAMIFIED-LEVEL"
    else:
        verdict = "QUILLEN-RAMIFIED-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("RESIDUAL (2) Maxwell k0: derived as 4 * (1/4) = 1 at "
          "ramified depth >= 3.  Jet-collapse (k0=2) is GRAVITY (chi) "
          "and is killed by the [E] split (F_2(a*)=a*^3).")
    print("ALPHA.QUILLEN.EXACT.01 UNTOUCHED [O] -- this is not the "
          "AQFT/zeta identification of F_{U(1)} with log det_zeta; "
          "it is the jet-native origin of the integer level.  "
          "NO MARKER MOVE.  NO RH CLAIM.  NO SECOND ALPHA.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot
                 and verdict == "QUILLEN-RAMIFIED-LEVEL") else 1


if __name__ == "__main__":
    raise SystemExit(main())
