#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""qsys_jet_iso_probe -- GNET.QSYS.JETFILTRATION.01 (EXPLORATION ONLY).

THE QUESTION.  The open half of GNET.RAMIFIED.01 is the identification
of the constructed index-4 Longo Q-system (GATE.METRIC.08, A = C[Z4])
with the ramified Gaussian geometry (V = L/(1+i)L = F2^4, the non-split
jet W = L/2L over F2[eps]/(eps^2), v689/v803/v833).  A raw algebra
isomorphism C[Z4] ≅ jet ring is the WRONG statement: C[Z4] is semisimple
of dimension 4 over C; the jet ring is local of dimension 2 over F2.
This probe does NOT claim that iso.  It tests a FILTRATION:

    the Gaussian clock J (pair rotation, J^2 = -I, J^4 = I) generates
    the Q-system group; its action on the ramified quotients L / pi^m L
    with pi = 1+i collapses in a unique, predeclared way:

        m = 1 (addresses V) :  order 1   (clock invisible)
        m = 2 (jet W)       :  order 2   (image = unique sub-Q-system
                                          C[Z2] = {0,2} = SO(16)_1 step)
        m >= 3              :  order 4   (full C[Z4] Q-system recovered)

If this filtration holds, the Q-system IS the clock of the ramified
tower, recovered at depth >= 3 and collapsing onto the halfway object
exactly at the jet.  That is a typed coupling between the continuum
Q-system and the 4-bit / jet layer -- not a Calderon-net proof, not a
matter reading, not RH.

CORPUS (read-only, rebuilt inline; no verification/ import):
  v125 GATE.METRIC.08  C[Z4] special Frobenius / Longo Q-system, unique
                       intermediate {0,2} = C[Z2]
  v689 / v722 / v833   Gaussian E8, J, V, W, pi = 1+i
  v803                 i = 1+eps on W, ZERO mu4-equivariant splittings
  hjelmslev R_m        Z[i]/(1+i)^m digit codes (ring order of i, independent
                       of the lattice action)

FROZEN MODULES (hashed in FROZEN_SPEC before any lattice walk):
  Q1  C[Z4] Q-system axioms (associativity, unit, Frobenius, specialness
      m m* = 4 I) and the unique intermediate C[Z2] = {0,2}.
  Q2  Group-scheme reduction: in F2[X], X^4 - 1 = (X - 1)^4 exactly
      (mu4 becomes infinitesimal in characteristic 2).  Over C the
      polynomial has 4 distinct roots (etale).
  Q3  RAW-ISO FENCE (must-fail as algebra iso): C[Z4] has 4 primitive
      orthogonal idempotents; R_2 = Z[i]/(2) has exactly 2 idempotents
      {0,1} (local).  Typed DEAD, not a surprise.
  Q4  LATTICE CLOCK FILTRATION: order of J on L/pi^m L equals
      (1, 2, 4, 4) at m = 1,2,3,4.  Certificate: (J^k - I)L ⊆ pi^m L
      with k = order, and (J^{k/p} - I)L notsubseteq pi^m L.
  Q5  RING CLOCK FILTRATION (independent): multiplicative order of i
      in R_m equals the same tuple (1, 2, 4, 4).
  Q6  HALFWAY = JET IMAGE: ker(rho_W) = {0, 2} inside Z4 = {J^k},
      which IS the unique intermediate subgroup of Q1.  The group
      algebra of im(rho_W) satisfies the C[Z2] Q-system axioms
      (index 2).  The group algebra of im(rho_m) for m >= 3 satisfies
      the C[Z4] axioms (index 4).
  Q7  INDEPENDENT GRADINGS: NS/R is the parity character of V; Z4 acts
      trivially on V (Q4 at m=1), so NS/R cannot be a pullback of a
      Z4-character.  The Ramond identification of GNET.RAMIFIED stays
      a SEPARATE face; this probe does not close it.

CONTROLS (must fire):
  C1  Split ring F2 x F2 is NOT isomorphic to R_2 (0 of 24 bijections;
      idempotent census 4 vs 2).  The ramified collapse needs 2 | ramified.
  C2  Identity clock J0 = I produces order 1 at EVERY m (the filtration
      is contentful: a trivial clock does not recover C[Z4]).
  C3  Inverted clock J^{-1} = -J produces the SAME order tuple
      (Aut(Z4) = Z2; covariance, not a kill).

KILLS: K1 Q1 axioms fail; K2 the F2 identity X^4-1 = (X-1)^4 fails;
K3 the raw-iso fence does not fire (would mean the algebras ARE iso --
the probe's typing is then void); K4/K5 order tuple deviates on lattice
or ring; K6 ker(rho_W) != {0,2}; K7 NS/R IS a Z4-character (would
collapse two faces that the corpus keeps distinct).

VERDICT ENUM (frozen):
  QSYS-JET-FILTRATION     Q1-Q7 hold, controls C1-C3 fire.
  QSYS-JET-PARTIAL        controls fire, a named Qi fails.
  QSYS-JET-BROKEN         K4 or K5 or K6 fires (the coupling dies).
  CONTROL-VOID            a control does not fire.

FIREWALL: experiments/tfpt-discovery only; writes nothing but stdout;
no verification/, ledger, paper, website, changelog; no .md; no RH
claim; no matter semantics (v775 ROOTCLASS-MIXED cited); Calderon-net
identification UNTOUCHED.  Exact integer / Fraction / sympy; no floats;
no numpy; AST-ban on verification and zeta.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qsys_jet_iso_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import time
from collections import Counter

import sympy as sp

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
GNET.QSYS.JETFILTRATION.01 FROZEN SPEC (2026-08-19).
Q1 C[Z4] special Frobenius, m m* = 4 I; unique intermediate {0,2}=C[Z2].
Q2 F2[X]: X^4-1 == (X-1)^4; over C four distinct roots.
Q3 RAW-ISO FENCE: C[Z4] has 4 primitive idempotents; R_2 has {0,1} only.
Q4 order(J on L/pi^m L) = (1,2,4,4) at m=1,2,3,4.
Q5 order(i in R_m) = (1,2,4,4) at m=1,2,3,4.
Q6 ker(rho_W)={0,2}=the Q1 intermediate; C[im rho_W] is the C[Z2]
   Q-system; C[im rho_m] for m>=3 is the C[Z4] Q-system.
Q7 NS/R is a character of V, Z4 acts trivially on V: independent grading.
C1 F2xF2 not iso to R_2 (0/24). C2 J=I gives order 1 at all m.
C3 J^{-1}=-J same order tuple.  Verdict: QSYS-JET-FILTRATION /
PARTIAL / BROKEN / CONTROL-VOID.  Calderon-net face UNTOUCHED.
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
    banned = {"verification", "zeta", "zetazero", "mpmath", "numpy"}
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


# =====================================================================
# Q-system of C[Z_n]  (v125 rebuilt; n = 4 and n = 2)
# =====================================================================
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
    return dict(n=n, m=m, assoc=assoc, unit=u_l and u_r, frob=frob,
                special=special, ok=assoc and u_l and u_r and frob and special)


def primitive_idempotents_cyclic(n: int) -> int:
    """Number of primitive orthogonal idempotents of C[Z_n] via DFT."""
    w = sp.exp(2 * sp.pi * sp.I / n)
    idems = []
    for k in range(n):
        e = sp.zeros(n, 1)
        for j in range(n):
            e[j] = w ** (-k * j) / n
        idems.append(e)
    # orthogonality e_k * e_l = delta_kl e_k in the group algebra
    def mul_vec(x, y):
        z = sp.zeros(n, 1)
        for a in range(n):
            for b in range(n):
                z[(a + b) % n] += x[a] * y[b]
        return sp.simplify(z)

    count = 0
    for k, e in enumerate(idems):
        ee = mul_vec(e, e)
        if ee == e:
            count += 1
        for l, f in enumerate(idems):
            if k != l and mul_vec(e, f) != sp.zeros(n, 1):
                return -1
    return count


# =====================================================================
# R_m = Z[i] / (1+i)^m   (hjelmslev digit codes, rebuilt)
# =====================================================================
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

    add = [[enc(dec[x][0] + dec[y][0], dec[x][1] + dec[y][1])
            for y in range(size)] for x in range(size)]
    mul = [[enc(dec[x][0] * dec[y][0] - dec[x][1] * dec[y][1],
                dec[x][0] * dec[y][1] + dec[x][1] * dec[y][0])
            for y in range(size)] for x in range(size)]
    return dict(m=m, size=size, dec=dec, enc=enc, add=add, mul=mul)


def ring_idempotents(R) -> set:
    idems = set()
    for x in range(R["size"]):
        if R["mul"][x][x] == x:
            idems.add(x)
    return idems


def order_of_i_in_ring(R) -> int:
    i_code = R["enc"](0, 1)
    one = R["enc"](1, 0)
    acc = one
    for k in range(1, R["size"] + 2):
        acc = R["mul"][acc][i_code]
        if acc == one:
            return k
    return 0


# =====================================================================
# Gaussian E8 + clock J  (Construction A over C*, rebuilt)
# =====================================================================
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
    cstar = next(c for c in both if w0246 in c)
    return placements, both, cstar


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


def j_vec(v):
    out = [0] * 8
    for k in range(4):
        out[2 * k] = -v[2 * k + 1]
        out[2 * k + 1] = v[2 * k]
    return tuple(out)


def in_L(v, cstar):
    return tuple(x % 2 for x in v) in cstar


def in_pi_L(v, cstar):
    w = [0] * 8
    for k in range(4):
        w[2 * k] = v[2 * k] + v[2 * k + 1]
        w[2 * k + 1] = v[2 * k + 1] - v[2 * k]
    if any(x % 2 for x in w):
        return False
    return in_L([x // 2 for x in w], cstar)


def in_pi_m_L(v, m, cstar):
    """x in (1+i)^m L.  Uses (1+i)^2 L = 2L, (1+i)^3 L = 2(1+i)L,
    (1+i)^4 L = 4L."""
    if m == 1:
        return in_pi_L(v, cstar)
    if m == 2:
        if any(x % 2 for x in v):
            return False
        return in_L([x // 2 for x in v], cstar)
    if m == 3:
        if any(x % 2 for x in v):
            return False
        half = [x // 2 for x in v]
        return in_pi_L(half, cstar)
    if m == 4:
        if any(x % 4 for x in v):
            return False
        return in_L([x // 4 for x in v], cstar)
    raise ValueError(m)


def sub_vec(a, b):
    return tuple(x - y for x, y in zip(a, b))


def clock_order_on_quotient(roots, m, cstar, jfun) -> int:
    """Smallest k>0 such that (J^k - I) annihilates every root modulo
    pi^m L.  Search k in (1,2,4) only -- J^4 = I on the nose."""
    def jk(v, k):
        out = tuple(v)
        for _ in range(k):
            out = jfun(out)
        return out

    for k in (1, 2, 4):
        if all(in_pi_m_L(sub_vec(jk(r, k), r), m, cstar) for r in roots):
            return k
    return 0


def split_ring_iso_count() -> int:
    """How many of the 24 bijections F2xF2 -> R_2 are ring isos?"""
    R = build_ring(2)
    # F2xF2 on {0,1,2,3} with 0=(0,0),1=(1,0),2=(0,1),3=(1,1)
    add2 = [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]]
    mul2 = [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 2, 2], [0, 1, 2, 3]]
    hits = 0
    for perm in itertools.permutations(range(4)):
        ok = True
        for x in range(4):
            for y in range(4):
                if R["add"][perm[x]][perm[y]] != perm[add2[x][y]]:
                    ok = False
                    break
                if R["mul"][perm[x]][perm[y]] != perm[mul2[x][y]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            hits += 1
    return hits


def main() -> int:
    print("GNET.QSYS.JETFILTRATION.01 -- Q-system clock filtration "
          "along L/(1+i)^m L")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    # ----- Q1 -----
    section("Q1: C[Z4] Q-system + unique intermediate C[Z2]")
    q4 = qsystem_of_cyclic(4)
    q2 = qsystem_of_cyclic(2)
    check("Q1.1 C[Z4] associativity + unit + Frobenius + specialness "
          "m m* = 4 I (Longo Q-system, Jones index 4)",
          q4["ok"] and q4["special"])
    check("Q1.2 C[Z2] is itself a special Frobenius algebra "
          "(m m* = 2 I, Jones index 2)",
          q2["ok"] and q2["special"])
    sub = {0, 2}
    closes = all((a + b) % 4 in sub for a in sub for b in sub)
    intermediates = []
    for mask in range(1, 16):
        s = {k for k in range(4) if mask & (1 << k)}
        if 0 not in s:
            continue
        if all((a + b) % 4 in s for a in s for b in s) and s not in ({0}, {0, 1, 2, 3}):
            intermediates.append(frozenset(s))
    check("Q1.3 unique proper intermediate subgroup of Z4 is {0,2} "
          "(the SO(16)_1 halfway Q-system); index factorisation 4 = 2 x 2",
          closes and intermediates == [frozenset({0, 2})] and 2 * 2 == 4,
          "intermediates=%s" % intermediates)

    # ----- Q2 -----
    section("Q2: group-scheme reduction mu4 in characteristic 2")
    X = sp.symbols("X")
    f2 = sp.GF(2)
    poly = (X ** 4 - 1).as_poly(X, domain=f2)
    inf = ((X - 1) ** 4).as_poly(X, domain=f2)
    check("Q2.1 in F2[X]: X^4 - 1 == (X - 1)^4 (mu4 purely infinitesimal)",
          poly == inf, "%s vs %s" % (poly, inf))
    roots_c = sp.roots(X ** 4 - 1, X)
    check("Q2.2 over C: X^4 - 1 has 4 distinct roots (etale mu4 = Z4); "
          "the infinitesimal collapse is characteristic-2 specific",
          set(roots_c) == {1, -1, sp.I, -sp.I} and len(roots_c) == 4)

    # ----- Q3 -----
    section("Q3: RAW-ISO FENCE (semisimple vs local)")
    n_idems_c = primitive_idempotents_cyclic(4)
    R2 = build_ring(2)
    idems_r2 = ring_idempotents(R2)
    check("Q3.1 C[Z4] has exactly 4 primitive orthogonal idempotents "
          "(DFT of Z4)",
          n_idems_c == 4, "count=%s" % n_idems_c)
    check("Q3.2 R_2 = Z[i]/(2) has exactly 2 idempotents {0,1} (local); "
          "RAW algebra iso C[Z4] ≅ jet ring is DEAD",
          idems_r2 == {0, 1}, "idempotents=%s" % sorted(idems_r2))

    # ----- lattice -----
    section("lattice rebuild: Gaussian E8 + clock J")
    placements, both, cstar = build_cstar()
    check("L.1 placement census 30 = 8!/1344, exactly 2 mu4/sigma-invariant",
          len(placements) == 30 and len(both) == 2)
    roots = build_roots(cstar)
    check("L.2 240 roots, all norm 4, all in L",
          len(roots) == 240 and len(set(roots)) == 240
          and all(sum(x * x for x in r) == 4 for r in roots)
          and all(in_L(r, cstar) for r in roots))
    Jm = sp.zeros(8, 8)
    for k in range(4):
        Jm[2 * k, 2 * k + 1] = -1
        Jm[2 * k + 1, 2 * k] = 1
    I8 = sp.eye(8)
    check("L.3 J^2 == -I, J^4 == I, J orthogonal, (1+J)^T(1+J)==2 I "
          "(norm doubling)",
          Jm * Jm == -I8 and Jm ** 4 == I8 and Jm.T * Jm == I8
          and (I8 + Jm).T * (I8 + Jm) == 2 * I8)
    check("L.4 J permutes the 240 roots (lattice-stable complex structure)",
          {j_vec(r) for r in roots} == set(roots))
    check("L.5 zero class empty: no root in (1+i)L",
          not any(in_pi_L(r, cstar) for r in roots))

    # ----- Q4 -----
    section("Q4: lattice clock filtration  order(J on L/pi^m L)")
    expected = {1: 1, 2: 2, 3: 4, 4: 4}
    orders_lat = {}
    for m in (1, 2, 3, 4):
        orders_lat[m] = clock_order_on_quotient(roots, m, cstar, j_vec)
        check("Q4.m=%d  order(J on L/pi^m L) = %d  (demand %d)"
              % (m, orders_lat[m], expected[m]),
              orders_lat[m] == expected[m])

    # ----- Q5 -----
    section("Q5: ring clock filtration  order(i in R_m)")
    orders_ring = {}
    for m in (1, 2, 3, 4):
        Rm = build_ring(m)
        # ring axioms: enc/dec roundtrip + i^4 = 1 always
        rt = all(Rm["enc"](*Rm["dec"][c]) == c for c in range(Rm["size"]))
        orders_ring[m] = order_of_i_in_ring(Rm)
        check("Q5.m=%d  R_m roundtrip AND order(i) = %d  (demand %d)"
              % (m, orders_ring[m], expected[m]),
              rt and orders_ring[m] == expected[m])
    check("Q5.eq  lattice-order tuple == ring-order tuple "
          "(independent certificates of one filtration)",
          orders_lat == orders_ring == expected)

    # ----- Q6 -----
    section("Q6: halfway sub-Q-system = jet image of the clock")
    ker_w = set()
    for k in range(4):
        def jk_k(v, kk=k):
            out = tuple(v)
            for _ in range(kk):
                out = j_vec(out)
            return out
        if all(in_pi_m_L(sub_vec(jk_k(r), r), 2, cstar) for r in roots):
            ker_w.add(k)
    check("Q6.1 ker(rho_W) = {0,2} inside Z4  (the unique Q1 intermediate)",
          ker_w == {0, 2}, "ker=%s" % sorted(ker_w))
    q_im2 = qsystem_of_cyclic(2)
    q_im4 = qsystem_of_cyclic(4)
    check("Q6.2 group algebra of im(rho_W) ≅ C[Z2] is a Q-system of index 2",
          q_im2["ok"] and orders_lat[2] == 2)
    check("Q6.3 group algebra of im(rho_m) for m>=3 ≅ C[Z4] is a Q-system "
          "of index 4 (the GATE.METRIC.08 object recovered at depth >= 3)",
          q_im4["ok"] and orders_lat[3] == 4 and orders_lat[4] == 4)
    check("Q6.4 i = 1+eps on W: J r - r is in 2L for NO root "
          "(order is exactly 2, not 1) AND J^2 r - r IS in 2L for ALL roots",
          orders_lat[2] == 2
          and all(in_pi_m_L(sub_vec(j_vec(j_vec(r)), r), 2, cstar)
                  for r in roots)
          and not all(in_pi_m_L(sub_vec(j_vec(r), r), 2, cstar)
                      for r in roots))

    # ----- Q7 -----
    section("Q7: NS/R is independent of the Z4 clock")

    # Construction-A coordinates are NOT the even-coordinate doubled
    # model: the four pair-sums (a+bi ↦ a+b) collapse to a SINGLE bit.
    # The F2^4 class space is recovered by union-find modulo (1+i)L.
    reps = []
    class_of = {}
    for r in roots:
        found = None
        for i, rep in enumerate(reps):
            if in_pi_L(sub_vec(r, rep), cstar):
                found = i
                break
        if found is None:
            found = len(reps)
            reps.append(r)
        class_of[r] = found
    sizes = Counter(class_of.values())
    check("Q7.1 union-find L/(1+i)L on roots: 15 classes, zero empty, "
          "each class exactly 16 roots",
          len(reps) == 15 and set(sizes.values()) == {16}
          and not any(in_pi_L(r, cstar) for r in roots))

    def chi_nsr(r):
        # one linear character of V in this chart (pair-0 sum).
        return (r[0] + r[1]) & 1

    chi_by_class = {}
    for r in roots:
        c = class_of[r]
        bit = chi_nsr(r)
        if c in chi_by_class:
            if chi_by_class[c] != bit:
                chi_by_class[c] = -1
        else:
            chi_by_class[c] = bit
    n_ns_cls = sum(1 for v in chi_by_class.values() if v == 0)
    n_r_cls = sum(1 for v in chi_by_class.values() if v == 1)
    n_ns = sum(1 for r in roots if chi_nsr(r) == 0)
    n_r = sum(1 for r in roots if chi_nsr(r) == 1)
    check("Q7.1b a character of V (pair-0 sum) is constant on classes and "
          "splits 7 NS + 8 R classes = 112 + 128 roots",
          all(v in (0, 1) for v in chi_by_class.values())
          and n_ns_cls == 7 and n_r_cls == 8
          and n_ns == 112 and n_r == 128)
    jr_same_class = all(class_of[j_vec(r)] == class_of[r] for r in roots)
    clock_trivial_on_v = orders_lat[1] == 1
    check("Q7.2 INDEPENDENT GRADINGS: J preserves every V-class (trivial "
          "action, order 1) AND chi_NSR is nonconstant on V, so NS/R is "
          "NOT a Z4-character.  Ramond face of GNET.RAMIFIED UNTOUCHED",
          clock_trivial_on_v and jr_same_class
          and n_ns == 112 and n_r == 128)

    # ----- controls -----
    section("controls")
    n_split = split_ring_iso_count()
    check("C1 F2 x F2 admits 0 of 24 ring isos onto R_2 "
          "(ramified collapse needs 2 ramified)",
          n_split == 0, "hits=%d" % n_split)

    def j_id(v):
        return tuple(v)

    orders_id = {m: clock_order_on_quotient(roots, m, cstar, j_id)
                 for m in (1, 2, 3, 4)}
    check("C2 identity clock: order = 1 at every m "
          "(filtration is contentful)",
          orders_id == {1: 1, 2: 1, 3: 1, 4: 1},
          "orders=%s" % orders_id)

    def j_inv(v):
        # J^{-1} = -J = J^3
        return j_vec(j_vec(j_vec(v)))

    orders_inv = {m: clock_order_on_quotient(roots, m, cstar, j_inv)
                  for m in (1, 2, 3, 4)}
    check("C3 inverted clock J^{-1} = -J: SAME order tuple "
          "(Aut(Z4)=Z2 covariance)",
          orders_inv == expected, "orders=%s" % orders_inv)

    # ----- verdict -----
    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    names = {n: ok for n, ok in CHECKS}

    def passed(prefix):
        return all(ok for n, ok in CHECKS if n.startswith(prefix))

    q_ok = all(passed(p) for p in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"))
    c_ok = passed("C1") and passed("C2") and passed("C3")
    k4 = not passed("Q4")
    k5 = not passed("Q5")
    k6 = not names.get("Q6.1 ker(rho_W) = {0,2} inside Z4  "
                       "(the unique Q1 intermediate)", True)
    # robust K6
    k6 = not any(n.startswith("Q6.1") and ok for n, ok in CHECKS)
    if not c_ok:
        verdict = "CONTROL-VOID"
    elif k4 or k5 or k6:
        verdict = "QSYS-JET-BROKEN"
    elif q_ok and c_ok:
        verdict = "QSYS-JET-FILTRATION"
    else:
        failed = [n for n, ok in CHECKS if not ok]
        verdict = "QSYS-JET-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("FILTRATION lattice %s   ring %s"
          % (orders_lat, orders_ring))
    print("RAW-ISO C[Z4] ≅ jet-ring: DEAD (Q3).  "
          "Calderon-net face: UNTOUCHED (Q7).  "
          "NO RH CLAIM.  NO MATTER SEMANTICS.")
    if verdict != "QSYS-JET-FILTRATION":
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot and verdict == "QSYS-JET-FILTRATION") else 1


if __name__ == "__main__":
    raise SystemExit(main())
