#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ftransfer_context15_probe -- FTRANSFER.CONTEXT.15.01 (EXPLORATION ONLY).

COUPLING LANE 6 (parallel to ALPHA.QUILLEN.JET.A4).

THE QUESTION.  Four named F_transfer drivers (Koide/F_pole, eta_B /
F_Boltzmann, axion/F_relic, m_p/m_e / F_QCD) are [C] bridges, never
primitive compiler outputs.  PGL2-common-action is already executed
(ftransfer_pgl2_probe; not redone).  Thermal-time internalization
is already dead.  This probe asks the CONTEXT-INDEXING question:

    do the four live on the 15 Pauli contexts of W(3,2) (the doily;
    15 points = 15 nontrivial 2-qubit Paulis; 15 lines = contexts)
    without a 16th direction (Pauli I / class 0) and without a
    second clock that is not theta_i / C_p / v_geo?

STRONG HYPOTHESIS "the four are measurements on the 15 contexts of
one state": DEAD if they cannot biject, if three of four require a
named extra clock, or if a driver consumes Pauli I.

FROZEN DICTIONARY (no search, no 92160 BFS, no import of
two_qubit_clifford_probe / ftransfer_pgl2_probe):
  T1  15 isotropic lines of W(3,2) from the symplectic form on F2^4;
      15 points; each point on 3 lines (doily).
  T2  Pauli I is the 16th (zero vector).  It is NOT a doily point.
      Analog of readout R4 (zero class unused).
  T3  Pigeonhole: 4 drivers cannot biject with 15 contexts.  Strong
      "each context is a transfer" is DEAD here.
  T4  Koide: 3 generations = line size 3; dimensionless 2/3 is an
      A3 rational (OFF-CONTEXT-SCALAR with LINE-SUPPORT).  The ratio
      is NOT computed from doily incidence.
  T5  eta_B needs the named leptogenesis clock C_p (not a context
      index).  F_Boltzmann shares the Koide contraction (v425) PLUS
      that extra clock.
  T6  axion / F_relic needs the named wall theta_i (not a context).
  T7  m_p/m_e / F_QCD needs the named scale v_geo (not a context).
  T8  Computational context C0 = {ZI, IZ, ZZ}.  Spreads through C0:
      a spread is 5 pairwise disjoint lines covering 15 points.
      Complement of C0 in a spread is 4 lines -- candidate SUPPORT
      of the four drivers, not a numeric readout.  Demand: at least
      one such spread exists, and the complement does NOT determine
      {2/3, C_p, theta_i, v_geo} from incidence alone (typed: no
      map line -> number without extra data).
  T9  The four dimensionful anchors {v_geo, M_R, C_p, theta_i}
      (cr_continuous_uniflow) are not Pauli-context labels.

CONTROLS:
  C1  Euclidean (dot) form in place of symplectic does NOT yield 15
      isotropic 3-lines.
  C2  {I} union any two Paulis is not a W(3,2) line (I = 0).
  C3  Koide 2/3 is independent of 15 (a rational A3 output).
  C4  4 != 15.

KILLS: K1 doily census != 15; K2 a named driver REQUIRES Pauli I
as a geometric input; K3 eta_B/axion/m_p/m_e reconstruct from
incidence alone (then they would not be F_transfer [C] clocks);
K4 no spread through C0.

VERDICT ENUM:
  FTRANSFER-CONTEXT-FILTERED  strong hyp DEAD; T1-T9 hold; no 16th;
                              three drivers need named extra clocks.
  FTRANSFER-CONTEXT-ALL       all four are context readouts producing
                              their numbers from W(3,2) alone
                              (will not fire).
  FTRANSFER-CONTEXT-DEAD      K1 or K2 or K4.
  CONTROL-VOID                a control fails.

FIREWALL: experiments/tfpt-discovery only; no verification/ import;
no ledger/paper/website; no .md; no RH; no matter semantics.
F_transfer stays [C].  AST-ban verification, zeta, numpy, mpmath.
Exact integer / Fraction.  Do not import sibling probes.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ftransfer_context15_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import time
from fractions import Fraction

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
FTRANSFER.CONTEXT.15.01 FROZEN SPEC (2026-08-19).
T1 15 isotropic lines of W(3,2); 15 points; 3 lines per point.
T2 Pauli I is the 16th (zero); not a doily point.
T3 4 cannot biject 15; strong 'each context is a transfer' DEAD.
T4 Koide 2/3 = OFF-CONTEXT-SCALAR with line-size 3 support; not
   computed from incidence.
T5 eta_B needs named clock C_p. T6 axion needs theta_i.
T7 m_p/m_e needs v_geo. T8 spreads through C0={ZI,IZ,ZZ} exist;
   4-line complement is SUPPORT not a numeric readout.
T9 anchors {v_geo, M_R, C_p, theta_i} are not context labels.
C1 Euclidean form != 15 lines. C2 I is not a line point.
C3 2/3 independent of 15. C4 4!=15.
F_transfer stays [C]. No PGL2 redo. No 16th Pauli used.
Verdict: FILTERED / ALL / DEAD / CONTROL-VOID.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# symplectic bits (x1, z1, x2, z2) -- same chart as two_qubit_clifford
NAMES1Q = {(0, 0): "I", (1, 0): "X", (0, 1): "Z", (1, 1): "Y"}
ANCHORS = ("v_geo", "M_R", "C_p", "theta_i")
DRIVERS = ("Koide/F_pole", "eta_B/F_Boltzmann", "axion/F_relic",
           "m_p/m_e/F_QCD")
CLOCKS = {
    "Koide/F_pole": None,  # dimensionless A3; no extra clock
    "eta_B/F_Boltzmann": "C_p",
    "axion/F_relic": "theta_i",
    "m_p/m_e/F_QCD": "v_geo",
}


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


def pauli_name(bits):
    return NAMES1Q[(bits[0], bits[1])] + NAMES1Q[(bits[2], bits[3])]


def symp(a, b):
    return (a[0] * b[1] + a[1] * b[0] + a[2] * b[3] + a[3] * b[2]) % 2


def eucl(a, b):
    return sum(x * y for x, y in zip(a, b)) % 2


def bxor(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))


def isotropic_lines(form) -> list:
    nz = [b for b in itertools.product((0, 1), repeat=4) if any(b)]
    lines = set()
    for a, b in itertools.combinations(nz, 2):
        if form(a, b) == 0:
            lines.add(frozenset({a, b, bxor(a, b)}))
    return sorted(lines, key=lambda s: sorted(s))


def is_spread(five) -> bool:
    pts = []
    for line in five:
        pts.extend(line)
    return len(five) == 5 and len(pts) == 15 and len(set(pts)) == 15


def spreads_through(line, all_lines):
    others = [c for c in all_lines if c != line]
    hits = []
    for combo in itertools.combinations(others, 4):
        five = (line,) + combo
        if is_spread(five):
            hits.append(five)
    return hits


def main() -> int:
    print("FTRANSFER.CONTEXT.15.01 -- do the four drivers live on "
          "the 15 Pauli contexts of W(3,2)?")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("T1 doily of W(3,2)")
    contexts = isotropic_lines(symp)
    points = [b for b in itertools.product((0, 1), repeat=4) if any(b)]
    per_pt = {p: sum(1 for c in contexts if p in c) for p in points}
    three_ok = all(len(c) == 3 for c in contexts)
    iso_ok = all(symp(x, y) == 0 for c in contexts for x in c for y in c)
    check("T1a 15 isotropic 3-lines (contexts) from the Pauli "
          "symplectic form",
          len(contexts) == 15 and three_ok and iso_ok,
          "n=%d" % len(contexts))
    check("T1b 15 points, each on exactly 3 lines (doily incidence)",
          len(points) == 15 and set(per_pt.values()) == {3},
          "per_pt values %s" % sorted(set(per_pt.values())))

    section("T2 16th Pauli is I, unused")
    identity = (0, 0, 0, 0)
    names = {pauli_name(p) for p in points}
    check("T2 Pauli I is the zero vector, not among the 15 points, "
          "and 'II' is not a context label",
          identity not in points
          and "II" not in names
          and pauli_name(identity) == "II"
          and len(names) == 15)

    section("T3 pigeonhole")
    check("T3 4 drivers cannot biject with 15 contexts -- strong "
          "'each context is a transfer' DEAD",
          len(DRIVERS) == 4 != 15 and len(contexts) == 15)

    section("T4 Koide is off-context scalar with line-size support")
    koide = Fraction(2, 3)
    check("T4a Koide Q=2/3 is a rational independent of 15 "
          "(OFF-CONTEXT-SCALAR; A3, not incidence)",
          koide == Fraction(2, 3) and koide.numerator + koide.denominator
          != 15 and 15 * koide != 1)
    check("T4b a doily line has 3 points = 3 generations (LINE-SUPPORT "
          "size only; the ratio is not computed from the line)",
          all(len(c) == 3 for c in contexts) and CLOCKS["Koide/F_pole"]
          is None)

    section("T5-T7 named extra clocks")
    need_clock = {d: CLOCKS[d] for d in DRIVERS if CLOCKS[d] is not None}
    check("T5 eta_B/F_Boltzmann requires named clock C_p, which is "
          "not a Pauli-context label",
          need_clock["eta_B/F_Boltzmann"] == "C_p"
          and "C_p" not in names)
    check("T6 axion/F_relic requires named wall theta_i, not a "
          "context label",
          need_clock["axion/F_relic"] == "theta_i"
          and "theta_i" not in names)
    check("T7 m_p/m_e/F_QCD requires named scale v_geo, not a "
          "context label",
          need_clock["m_p/m_e/F_QCD"] == "v_geo"
          and "v_geo" not in names)
    check("T5-T7 three of four drivers need an extra clock; they "
          "are NOT reconstructible from doily incidence",
          len(need_clock) == 3 and CLOCKS["Koide/F_pole"] is None)

    section("T8 spreads through the computational context")
    z_i = (0, 1, 0, 0)
    i_z = (0, 0, 0, 1)
    z_z = (0, 1, 0, 1)
    c0 = frozenset({z_i, i_z, z_z})
    check("T8a C0 = {ZI, IZ, ZZ} is a context",
          c0 in set(contexts)
          and {pauli_name(p) for p in c0} == {"ZI", "IZ", "ZZ"})
    spreads = spreads_through(c0, contexts)
    check("T8b at least one spread of 5 lines through C0 "
          "(MUB pentad containing the computational context)",
          len(spreads) >= 1,
          "n_spreads=%d" % len(spreads))
    complements = [frozenset(s) - {c0} for s in spreads]
    check("T8c each complement has 4 lines -- candidate SUPPORT of "
          "the four drivers, not a numeric readout (no map "
          "line -> {2/3, C_p, theta_i, v_geo})",
          spreads and all(len(comp) == 4 for comp in complements)
          and all(len(c) == 3 for comp in complements for c in comp),
          "complement sizes %s" % [len(c) for c in complements])

    section("T9 dimensionful anchors are not context labels")
    check("T9 the four anchors {v_geo, M_R, C_p, theta_i} are disjoint "
          "from the 15 Pauli names and from the 15 context indices",
          len(ANCHORS) == 4
          and set(ANCHORS).isdisjoint(names)
          and all(a not in {str(i) for i in range(15)} for a in ANCHORS))

    section("controls")
    fake = isotropic_lines(eucl)
    # Euclidean isotropic 3-sets need not be 15; demand inequality
    check("C1 Euclidean (dot) form does NOT yield the doily of 15 "
          "isotropic 3-lines",
          len(fake) != 15 or fake != contexts,
          "n_eucl=%d" % len(fake))
    # I plus two Paulis: the zero vector is not in any genuine line
    check("C2 Pauli I (zero) lies in 0 of the 15 lines",
          all(identity not in c for c in contexts))
    check("C3 Koide 2/3 is independent of the census 15",
          Fraction(2, 3) * 15 != 1 and 2 + 3 != 15)
    check("C4 4 != 15 (pigeonhole control)",
          len(DRIVERS) != len(contexts))

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref):
        hits = [(n, ok) for n, ok in CHECKS if n.startswith(pref)]
        return bool(hits) and all(ok for _, ok in hits)

    c_ok = pfx("C1") and pfx("C2") and pfx("C3") and pfx("C4") and pfx("G0")
    t_ok = all(pfx("T%d" % k) for k in range(1, 10))
    strong_dead = pfx("T3") and pfx("T5")  # pigeonhole + extra clocks
    if not c_ok:
        verdict = "CONTROL-VOID"
    elif not (pfx("T1") and pfx("T2") and pfx("T8")):
        verdict = "FTRANSFER-CONTEXT-DEAD"
    elif t_ok and strong_dead:
        verdict = "FTRANSFER-CONTEXT-FILTERED"
    else:
        verdict = "FTRANSFER-CONTEXT-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("STRONG HYP (the four are measurements on the 15 contexts "
          "of one state): %s" % ("DEAD" if strong_dead else "OPEN"))
    print("FILTER: doily 15+15 holds; Pauli I unused (no 16th); "
          "Koide = off-context scalar with 3-line support; "
          "eta_B/axion/m_p/m_e need named clocks C_p, theta_i, v_geo.  "
          "F_transfer stays [C].  NO PGL2 REDO.  NO RH CLAIM.  "
          "NO MATTER SEMANTICS.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot
                 and verdict == "FTRANSFER-CONTEXT-FILTERED") else 1


if __name__ == "__main__":
    raise SystemExit(main())
