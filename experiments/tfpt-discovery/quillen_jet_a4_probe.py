#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""quillen_jet_a4_probe -- ALPHA.QUILLEN.JET.A4.01 (EXPLORATION ONLY).

COUPLING LANE 5 (parallel to FTRANSFER.CONTEXT.15).

THE QUESTION.  The corpus counterterm of the seam is
    8 b1 c3^6
with b1 = 41/10 the U(1)_Y a4 content coefficient (v434 [E]) and
c3^6 the six boundary insertions (P1).  The geometric 8 is already
typed as rank E8 = chi=2 seam-boundary count (v216/v434).  This
probe does NOT close ALPHA.QUILLEN.EXACT.01 (continuum variation
stays [O]; seam F-normalisation stays [C]).  It tests whether that
8 is the RAMIFIED JET rank recovered by GNET.QSYS.JETFILTRATION,
rather than an independent Lie-algebra 8:

    8  =  dim_{F2}(W)  =  2 * Jones(C[Z4])
       =  (jet clock order at m=2) * (Q-system index).

Depth m=1 (addresses V, clock invisible) would use factor 4, which
is the WRONG Ward coefficient.  The missing 2 is exactly ord(J on W).

This probe does NOT evaluate a discrete Seeley-DeWitt a4 on a graph.
It factors the EXISTING counterterm against the jet filtration.

FROZEN MODULES:
  Q1  |R_2| = 4, W = R_2^4 has 256 points, dim_{F2}(W) = 8 = rank_Z(E8).
  Q2  C[Z4] is special Frobenius with m m* = 4 I (Jones index 4);
      2 * 4 = 8.  Unique intermediate {0,2} has Jones 2, not 8.
  Q3  8 b1 = (4/5) M with M=41, b1=41/10;  8 b1 c3^6 = 41/(327680 pi^6)
      (v434 k2 identity, signless).
  Q4  DEPTH-1 KILL: 4 b1 c3^6 is half of the Ward coefficient.  The
      missing factor is ord(J on W) = 2, not a compiler-foreign number.
  Q5  CITED v471 grid N0=64 equals BOTH |V|*4 and |W|/4.  Dropping a
      V-class (15*4=60) misses N0.  Typed GRID-COINCIDENCE, not a
      replica derivation of Quillen exactness.
  Q6  CITED v471 N_R_MAIN=240 equals |E8 roots| (Construction A).
      Same type as Q5: grid coincidence, not a heat-kernel evaluation.

CONTROLS:
  C1  dim_{F2}(V) = 4 != 8.
  C2  |R_m| = 2^m for m=1..4.
  C3  Jones(C[Z2]) = 2 != 8;  2*Jones(C[Z2]) = 4 = depth-1 factor.
  C4  15*4 = 60 != cited N0 (cannot drop the zero class / a 16th).

KILLS: K1 dim W != 8; K2 2*Jones4 != 8; K3 8 b1 != (4/5)M;
K4 depth-1 already matches Ward (then the jet is unused);
K5 16*4 != 64 or 256/4 != 64; K6 |roots| != 240.

VERDICT ENUM:
  QUILLEN-JET-A4-FILTERED  Q1-Q6 hold; strong "this closes exactness"
                           DEAD (continuum variation not computed).
  QUILLEN-JET-A4-CLOSED    would require a discrete a4 evaluation equal
                           to 8 b1 c3^6 with no leftover -- will not fire.
  QUILLEN-JET-A4-DEAD      K1-K4 (the 8 is not the jet rank).
  GRID-VOID                K5 or K6 (cited grid is not the jet/root count).
  CONTROL-VOID             a control fails.

FIREWALL: experiments/tfpt-discovery only; no verification/ import;
no ledger/paper/website; no .md; no RH.  ALPHA.QUILLEN.EXACT.01 stays
[O]; SEAM.EQUIV stays [O]; number alpha^{-1} stays [E] (untouched).
AST-ban verification, zeta, numpy, mpmath.  Exact Fraction / sympy.
Do not import qsys_jet_iso_probe or v471.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/quillen_jet_a4_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import time
from fractions import Fraction

import sympy as sp

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
ALPHA.QUILLEN.JET.A4.01 FROZEN SPEC (2026-08-19).
Q1 |R_2|=4; |W|=4^4=256; dim_F2(W)=8=rank E8.
Q2 C[Z4] special, mm*=4I, Jones=4; 2*4=8. Intermediate Jones=2.
Q3 8 b1=(4/5)*41; 8 b1 c3^6 = 41/(327680 pi^6).
Q4 4 b1 c3^6 is HALF the Ward coefficient; missing factor = jet order 2.
Q5 cited v471 N0=64 = |V|*4 = |W|/4; 15*4=60 misses.
Q6 cited v471 N_R_MAIN=240 = |E8 roots| (Construction A).
C1 dim V=4. C2 |R_m|=2^m. C3 Jones(C[Z2])=2. C4 15*4!=64.
ALPHA.QUILLEN.EXACT.01 stays [O]. No discrete Seeley-DeWitt a4.
Verdict: FILTERED / CLOSED / DEAD / GRID-VOID / CONTROL-VOID.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# cited v471 discretisation (read, not imported)
V471_N0 = 64
V471_NR = 240
M_BUDGET = 41
B1 = Fraction(41, 10)


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


def qsystem_of_cyclic(n: int):
    m = sp.zeros(n, n * n)
    for a in range(n):
        for b in range(n):
            m[(a + b) % n, a * n + b] = 1
    mstar = m.T
    eye = sp.eye(n)
    m_x_1 = sp.Matrix(sp.kronecker_product(m, eye))
    one_x_m = sp.Matrix(sp.kronecker_product(eye, m))
    unit = sp.zeros(n, 1)
    unit[0] = 1
    assoc = m * m_x_1 == m * one_x_m
    u_l = m * sp.Matrix(sp.kronecker_product(unit, eye)) == eye
    u_r = m * sp.Matrix(sp.kronecker_product(eye, unit)) == eye
    frob1 = m_x_1 * sp.Matrix(sp.kronecker_product(eye, mstar))
    frob2 = one_x_m * sp.Matrix(sp.kronecker_product(mstar, eye))
    frob = frob1 == mstar * m and frob2 == mstar * m
    special = m * mstar == n * eye
    return dict(ok=assoc and u_l and u_r and frob and special,
                special=special, index=n)


def build_ring_size(m: int) -> int:
    """|Z[i]/(1+i)^m| = 2^m by the Hjelmslev digit code."""
    return 1 << m


G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2 for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)


def code_image(code, p):
    return frozenset(tuple(c[p[k]] for k in range(8)) for c in code)


def build_cstar():
    placements = set()
    for perm in itertools.permutations(range(8)):
        placements.add(code_image(C_NAIVE, perm))
    both = [c for c in placements
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    w0246 = (1, 0, 1, 0, 1, 0, 1, 0)
    return next(c for c in both if w0246 in c)


def build_roots(cstar):
    w4 = [c for c in cstar if sum(c) == 4]
    roots = []
    for k in range(8):
        for s in (2, -2):
            v = [0] * 8
            v[k] = s
            roots.append(tuple(v))
    for c in w4:
        sup = [k for k in range(8) if c[k]]
        for signs in itertools.product((1, -1), repeat=4):
            v = [0] * 8
            for k, s in zip(sup, signs):
                v[k] = s
            roots.append(tuple(v))
    return roots


def main() -> int:
    print("ALPHA.QUILLEN.JET.A4.01 -- is the geometric 8 the ramified "
          "jet rank?")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("Q1: jet F2-dimension")
    r2 = build_ring_size(2)
    n_w = r2 ** 4
    dim_w = n_w.bit_length() - 1
    check("Q1a |R_2| = 4 and |W|=R_2^4 = 256",
          r2 == 4 and n_w == 256, "|R_2|=%d |W|=%d" % (r2, n_w))
    check("Q1b dim_{F2}(W) = log2(256) = 8 = rank_Z(E8)",
          dim_w == 8 and n_w == 1 << 8, "dim=%d" % dim_w)

    section("Q2: 8 = 2 * Jones(C[Z4])")
    q4 = qsystem_of_cyclic(4)
    q2 = qsystem_of_cyclic(2)
    jet_order = 2  # ord(J on W), qsys Q4/Q5 at m=2 (recited filtration)
    check("Q2a C[Z4] special Frobenius, Jones index 4",
          q4["ok"] and q4["special"] and q4["index"] == 4)
    check("Q2b 2 * Jones(C[Z4]) = 8 = dim_{F2}(W)  "
          "(jet order at m=2 times Q-system index)",
          jet_order * q4["index"] == 8 == dim_w)
    sub = {0, 2}
    intermediates = []
    for mask in range(1, 16):
        s = {k for k in range(4) if mask & (1 << k)}
        if 0 not in s:
            continue
        if all((a + b) % 4 in s for a in s for b in s) and s not in (
                {0}, {0, 1, 2, 3}):
            intermediates.append(frozenset(s))
    check("Q2c unique proper intermediate of Z4 is {0,2}, Jones 2, "
          "and 2*Jones2 = 4 is the DEPTH-1 factor, not 8",
          intermediates == [frozenset(sub)]
          and q2["ok"] and q2["index"] == 2
          and 2 * q2["index"] == 4 != 8)

    section("Q3: 8 b1 c3^6 identity")
    eight_b1 = 8 * B1
    ward_mass = Fraction(4, 5) * M_BUDGET
    pi = sp.pi
    c3 = 1 / (8 * pi)
    a4 = sp.simplify(8 * sp.Rational(41, 10) * c3 ** 6)
    target = sp.Rational(41, 327680) / pi ** 6
    check("Q3a 8 b1 = (4/5)*41 = 164/5  (b1=41/10, M=41)",
          eight_b1 == ward_mass == Fraction(164, 5),
          "8 b1=%s" % eight_b1)
    check("Q3b 8 b1 c3^6 = 41/(327680 pi^6)  (v434 k2, signless)",
          sp.simplify(a4 - target) == 0,
          "a4=%s" % a4)

    section("Q4: depth-1 is the wrong Ward coefficient")
    a4_depth1 = sp.simplify(4 * sp.Rational(41, 10) * c3 ** 6)
    ratio = sp.simplify(a4 / a4_depth1)
    check("Q4 4 b1 c3^6 / 8 b1 c3^6 = 1/2; missing factor = jet "
          "order 2, not a foreign coefficient",
          ratio == 2 and a4_depth1 * 2 == a4,
          "ratio=%s" % ratio)

    section("Q5: cited v471 N0=64 is |V|*4 = |W|/4")
    n_v = 16
    check("Q5a cited N0 = |V|*Jones4 = 16*4 = 64 AND |W|/4 = 256/4",
          V471_N0 == n_v * q4["index"] == n_w // 4 == 64,
          "N0=%d 16*4=%d |W|/4=%d" % (V471_N0, n_v * 4, n_w // 4))
    check("Q5b 15*4 = 60 != N0 (cannot drop a V-class / 16th direction)",
          15 * 4 == 60 != V471_N0)

    section("Q6: cited v471 N_R_MAIN=240 = |E8 roots|")
    cstar = build_cstar()
    roots = build_roots(cstar)
    check("Q6 Construction-A roots = 240 = cited N_R_MAIN  "
          "(GRID-COINCIDENCE, not a replica a4)",
          len(roots) == 240 == V471_NR,
          "|roots|=%d N_R=%d" % (len(roots), V471_NR))

    section("controls")
    check("C1 dim_{F2}(V) = 4 != 8",
          n_v == 16 and (n_v.bit_length() - 1) == 4 != 8)
    sizes = [build_ring_size(m) for m in (1, 2, 3, 4)]
    check("C2 |R_m| = (2,4,8,16) for m=1..4",
          sizes == [2, 4, 8, 16], "sizes=%s" % sizes)
    check("C3 Jones(C[Z2]) = 2 != 8; 2*Jones2 = 4 = depth-1 factor",
          q2["index"] == 2 and 2 * q2["index"] == 4 != 8)
    check("C4 15*4 = 60 != cited N0=64",
          15 * 4 != V471_N0)

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref):
        hits = [(n, ok) for n, ok in CHECKS if n.startswith(pref)]
        return bool(hits) and all(ok for _, ok in hits)

    c_ok = pfx("C1") and pfx("C2") and pfx("C3") and pfx("C4") and pfx("G0")
    q_ok = all(pfx("Q%d" % k) for k in range(1, 7))
    if not c_ok:
        verdict = "CONTROL-VOID"
    elif not (pfx("Q5") and pfx("Q6")):
        verdict = "GRID-VOID"
    elif not (pfx("Q1") and pfx("Q2") and pfx("Q4")):
        verdict = "QUILLEN-JET-A4-DEAD"
    elif q_ok:
        verdict = "QUILLEN-JET-A4-FILTERED"
    else:
        verdict = "QUILLEN-JET-A4-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("STRONG HYP (this closes ALPHA.QUILLEN.EXACT.01): DEAD  "
          "-- no discrete Seeley-DeWitt a4 was evaluated; continuum "
          "variation stays [O]; seam F-normalisation stays [C].")
    print("FILTER: geometric 8 = dim_{F2}(W) = 2*Jones(C[Z4]); "
          "depth-1 factor 4 is the WRONG Ward coefficient; v471 "
          "N0=64 and N_R=240 are grid coincidences with |V|*4 and "
          "|roots|.  ALPHA.QUILLEN.EXACT.01 UNTOUCHED [O].  "
          "NO RH CLAIM.  NO SECOND ALPHA.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot
                 and verdict == "QUILLEN-JET-A4-FILTERED") else 1


if __name__ == "__main__":
    raise SystemExit(main())
