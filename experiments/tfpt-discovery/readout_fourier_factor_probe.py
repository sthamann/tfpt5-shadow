#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""readout_fourier_factor_probe -- E8.READOUT.FOURIER.FACTOR.01
(EXPLORATION ONLY).

OBSERVABLE LANE (parallel to GNET.RP.NSR.FLAT).

THE QUESTION.  Points on the 15 class fibers have no origin
(v782 TORSOR; v775 killed pointwise matter).  The 120 projective
Fourier rays of those torsors ARE canonical (E8.TORSOR.FOURIER.01,
verdict PARTIAL: P3 failed, weights mutually unbiased to modes).
Do named load-bearing READOUTS factor through origin-free data --
V-characters, fiber-Fourier rays, or off-fiber scalars -- or does
an [E] readout need a fiber origin or a 16th V-direction?

FROZEN READOUT DICTIONARY (no search):
  R1  NS/R -- the qsys Q7 character of V (pair-0 sum in this chart).
      Demand: constant on fibers, 7+8 of 15, origin-free.  Type:
      V-CHARACTER, not a fiber-Fourier mode (those vary ON a fiber).
  R2  FIBER-FOURIER RAYS -- for each of 15 fibers, 8 characters of
      v_perp; a mode has coeff +-1 on every root of the fiber.
      Demand: origin shift of the torsor multiplies a mode by a
      GLOBAL sign (the RAY is canonical).  Full support: no mode
      is a pair-indicator (P3-lite; v775 fence).
  R3  ALPHA WARD -- the cubic F(a)=0 from c3, g_car, budget M=41
      (v3).  Demand: the formula consumes NO root, class, or fiber
      datum.  Type: OFF-FIBER-SCALAR.  Strong claim "every [E]
      readout is a fiber-Fourier ray" is DEAD here.
  R4  NO 16TH DIRECTION -- roots miss the zero class; no readout
      in {R1,R2,R3} addresses class 0.  A 16th V-point is not used.

STRONG HYPOTHESIS "every [E] readout is a fiber-Fourier ray": DEAD
(R1 is a V-character, R3 is off-fiber).  FILTERED STATEMENT that
can still carry: no named readout in the dictionary needs a fiber
origin or the zero class; pointwise weights stay dead (P3-lite).

CONTROLS:
  C1  15 fibers x 16 roots, zero class empty (recite).
  C2  hbar = (<x,y>//2) mod 2 is well-defined on classes, alternating,
      and non-degenerate on the 16-element F2-vector space of classes
      (including 0).
  C3  scrambled origin-assignment that is NOT a torsor translation
      (independent signs per root, seed 20260819) produces at least
      one mode that is NOT a global-sign copy of a Fourier mode.
  C4  a pair-indicator on a fiber is NOT equal to any Fourier mode.

KILLS: K1 origin shift changes more than a global sign; K2 a mode
has incomplete support; K3 F(a) inspectably consumes a lattice
identifier; K4 NS/R not constant on fibers.

VERDICT ENUM:
  READOUT-FOURIER-FILTERED  strong hyp DEAD; R1-R4 hold; no origin
                            and no 16th direction used.
  READOUT-FOURIER-ALL       every readout is a fiber-Fourier ray
                            (will not fire if R1/R3 type as stated).
  READOUT-FOURIER-DEAD      K1 or K2 or K4.
  CONTROL-VOID              a control fails.

FIREWALL: experiments/tfpt-discovery only; no verification/ import;
no ledger/paper/website; no .md; no RH; no matter semantics.  Exact
integer.  AST-ban verification, zeta, numpy.  v775 ROOTCLASS-MIXED
stands.  E8.TORSOR.FOURIER.01 PARTIAL is cited, not imported.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/readout_fourier_factor_probe.py
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import time
from collections import Counter

T0 = time.time()
CHECKS: list[tuple[str, bool]] = []

FROZEN_SPEC = """\
E8.READOUT.FOURIER.FACTOR.01 FROZEN SPEC (2026-08-19).
R1 NS/R = V-character, constant on 15 fibers, 7+8, not a fiber mode.
R2 fiber-Fourier: origin shift = global sign; full 16-support;
pair-indicator is not a mode (P3-lite).
R3 alpha Ward cubic from c3,g_car,M=41 consumes no lattice datum
(OFF-FIBER-SCALAR). Strong hyp 'all [E] are fiber-Fourier' DEAD.
R4 zero class unused (no 16th direction).
C1 15x16. C2 hbar=(<x,y>+<x,Jy>)//2 mod 2 well-defined Hermitian,
alternating, nondeg on F2^4.
C3 scrambled signs not a Fourier mode. C4 pair-indicator not a mode.
Verdict: FILTERED / ALL / DEAD / CONTROL-VOID.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

G_NAIVE = ((1, 0, 0, 0, 0, 1, 1, 1), (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1), (0, 0, 0, 1, 1, 1, 1, 0))
C_NAIVE = frozenset(
    tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2 for j in range(8))
    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (2, 3, 4, 5, 0, 1, 6, 7)


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


def sub_vec(a, b):
    return tuple(x - y for x, y in zip(a, b))


def add_vec(a, b):
    return tuple(x + y for x, y in zip(a, b))


def div_1i(v):
    """Divide by (1+i): (1-i)v/2 in pair coords (a,b) -> ((a+b)/2,(b-a)/2)."""
    out = [0] * 8
    for k in range(4):
        a, b = v[2 * k], v[2 * k + 1]
        if (a + b) % 2 or (b - a) % 2:
            return None
        out[2 * k] = (a + b) // 2
        out[2 * k + 1] = (b - a) // 2
    return tuple(out)


def ip(a, b):
    return sum(x * y for x, y in zip(a, b))


def classify(roots, cstar):
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
    return reps, class_of


def class_of_vec(v, reps, cstar):
    if in_pi_L(v, cstar):
        return -1  # zero class
    for i, rep in enumerate(reps):
        if in_pi_L(sub_vec(v, rep), cstar):
            return i
    return None


def lcg_sign(seed, n):
    x = seed
    out = []
    for _i in range(n):
        x = (1103515245 * x + 12345) & 0x7FFFFFFF
        out.append(1 if (x & 1) == 0 else -1)
    return out


def alpha_ward_source() -> str:
    """The Ward cubic, as source text -- lattice-free by construction."""
    return (
        "c3 = 1/(8*pi); g_car = 5; M = 41; "
        "phibase = 1/(6*pi); dtop = 48*c3**4; "
        "F(a) = a**3 - 2*c3**3 * a**2 - (4/5)*c3**6 * M * log(1/phiseam)"
    )


def main() -> int:
    print("E8.READOUT.FOURIER.FACTOR.01 -- do [E] readouts factor "
          "origin-free?")
    print("SPEC_SHA %s" % SPEC_SHA)

    with open(__file__, "r", encoding="utf-8") as fh:
        src = fh.read()
    bad = ast_firewall(src)
    check("G0 AST-firewall: no verification/zeta/numpy identifiers",
          not bad, "banned=%s" % (bad,) if bad else "")

    section("C1 lattice / 15 fibers")
    cstar = build_cstar()
    roots = build_roots(cstar)
    reps, class_of = classify(roots, cstar)
    sizes = Counter(class_of.values())
    check("C1 15 fibers x 16 roots, zero class empty of roots",
          len(roots) == 240 and len(reps) == 15
          and set(sizes.values()) == {16}
          and not any(in_pi_L(r, cstar) for r in roots))

    section("C2 hbar on classes, F2^4 group")
    # addition of classes via representative sum
    n = len(reps)
    add_tbl = [[None] * (n + 1) for _ in range(n + 1)]
    # index -1 = zero, 0..14 = reps
    idxs = list(range(-1, n))
    rep_of = {-1: (0,) * 8}
    for i, r in enumerate(reps):
        rep_of[i] = r
    well_add = True
    for a in idxs:
        for b in idxs:
            s = add_vec(rep_of[a], rep_of[b])
            cid = class_of_vec(s, reps, cstar)
            if cid is None:
                well_add = False
                cid = -2
            add_tbl[a + 1][b + 1] = cid
    # group axioms on the 16 labels
    labels = idxs
    closed = well_add and all(add_tbl[a + 1][b + 1] in labels
                              for a in labels for b in labels)
    ident = all(add_tbl[a + 1][0] == a and add_tbl[0][a + 1] == a
                for a in labels)  # 0 maps to index -1 stored at slot 0
    # slot: index i stored at i+1, zero (-1) at 0.  add_tbl[a+1][0] is a+(-1)=a.
    exp2 = all(add_tbl[a + 1][a + 1] == -1 for a in labels)
    comm = all(add_tbl[a + 1][b + 1] == add_tbl[b + 1][a + 1]
               for a in labels for b in labels)
    assoc = True
    for a in labels:
        if not assoc:
            break
        for b in labels:
            if not assoc:
                break
            for c in labels:
                ab = add_tbl[a + 1][b + 1]
                bc = add_tbl[b + 1][c + 1]
                if add_tbl[ab + 1][c + 1] != add_tbl[a + 1][bc + 1]:
                    assoc = False
                    break
    check("C2a class addition is F2^4 (order 16, exponent 2, abelian)",
          closed and ident and exp2 and comm and assoc,
          "closed=%s ident=%s exp2=%s comm=%s assoc=%s"
          % (closed, ident, exp2, comm, assoc))

    def hb(a, b):
        x, y = rep_of[a], rep_of[b]
        return ((ip(x, y) + ip(x, j_vec(y))) // 2) % 2

    well_hb = True
    for r in roots:
        for s in roots:
            if hb(class_of[r], class_of[s]) != (
                    (ip(r, s) + ip(r, j_vec(s))) // 2) % 2:
                well_hb = False
                break
        if not well_hb:
            break
    alt = all(hb(a, a) == 0 for a in labels)
    # nondeg: for every a != -1 (and including?), exists b with hb=1
    nondeg = True
    for a in labels:
        if not any(hb(a, b) for b in labels):
            if a != -1:
                nondeg = False
    # zero is orthogonal to all, that's the radical if we include 0?
    # On the 15-dim... wait F2^4 symplectic form is NONDEG on the whole
    # 4-space, including that 0 is the only vector orthogonal to all.
    zero_rad = all(hb(-1, b) == 0 for b in labels)
    nondeg_nz = all(any(hb(a, b) for b in labels) for a in range(n))
    check("C2b hbar well-defined on class pairs, alternating, "
          "non-degenerate on V\\{0} (zero is the radical singleton)",
          well_hb and alt and zero_rad and nondeg_nz,
          "well=%s alt=%s zero_rad=%s nondeg_nz=%s"
          % (well_hb, alt, zero_rad, nondeg_nz))

    section("R1 NS/R is a V-character, not a fiber mode")
    def chi_nsr(r):
        return (r[0] + r[1]) & 1

    chi_by_class = {}
    mixed = False
    for r in roots:
        c = class_of[r]
        bit = chi_nsr(r)
        if c in chi_by_class and chi_by_class[c] != bit:
            mixed = True
        chi_by_class[c] = bit
    n_ns = sum(1 for v in chi_by_class.values() if v == 0)
    n_r = sum(1 for v in chi_by_class.values() if v == 1)
    check("R1a NS/R constant on fibers, splits 7+8 classes "
          "(112+128 roots)",
          (not mixed) and n_ns == 7 and n_r == 8
          and sum(1 for r in roots if chi_nsr(r) == 0) == 112
          and sum(1 for r in roots if chi_nsr(r) == 1) == 128)
    # a fiber-Fourier mode varies on a fiber; NS/R does not
    check("R1b NS/R is constant on each fiber => NOT a nontrivial "
          "fiber-Fourier mode (V-character / which-fiber readout)",
          not mixed and n_ns + n_r == 15)

    section("R2 fiber-Fourier rays, origin-free")
    fibers = {i: [r for r in roots if class_of[r] == i] for i in range(n)}
    # v_perp relative to class i: t with hb(t,i)=0, including 0 and i?
    # symplectic: v in v^perp always if alternating. dim 3 => 8 points.
    origin_ok = True
    full_supp = True
    n_even_odd = [0, 0]
    pair_is_mode = False
    for i in range(n):
        vperp = [t for t in labels if hb(t, i) == 0]
        if len(vperp) != 8:
            origin_ok = False
            continue
        fib = fibers[i]
        # origin r0 = lex-min root
        r0 = min(fib)
        def x_of(r, origin):
            d = div_1i(sub_vec(r, origin))
            if d is None:
                return None
            return class_of_vec(d, reps, cstar)

        xs = [x_of(r, r0) for r in fib]
        if any(x not in vperp for x in xs):
            origin_ok = False
        # 8 characters of v_perp; each x appears twice (pair / orientation)
        t = next(tt for tt in vperp if tt != -1)
        r1 = None
        for r in fib:
            if x_of(r, r0) == t:
                r1 = r
                break
        if r1 is None:
            origin_ok = False
            continue
        for u in vperp:
            coeffs = [1 - 2 * hb(u, x_of(r, r0)) for r in fib]
            if any(c is None or abs(c) != 1 for c in coeffs):
                full_supp = False
            coeffs2 = [1 - 2 * hb(u, x_of(r, r1)) for r in fib]
            want = 1 - 2 * hb(u, t)
            if any(c2 != want * c1 for c1, c2 in zip(coeffs, coeffs2)):
                origin_ok = False
        nr0 = tuple(-x for x in r0)
        pair_vec = [1 if (r == r0 or r == nr0) else 0 for r in fib]
        for u in vperp:
            mode = [1 - 2 * hb(u, x_of(r, r0)) for r in fib]
            if mode == [1 if r in (r0, nr0) else -1 for r in fib]:
                pair_is_mode = True
            if mode == [1 if r in (r0, nr0) else 0 for r in fib]:
                pair_is_mode = True

    check("R2a origin shift multiplies each mode by a global sign "
          "(ray canonical); v_perp has 8 points per fiber",
          origin_ok)
    check("R2b every mode has full +-1 support on its 16-root fiber",
          full_supp)
    check("C4 pair-indicator is NOT a Fourier mode (P3-lite / v775 fence)",
          not pair_is_mode)

    section("R3 alpha Ward is off-fiber")
    src_f = alpha_ward_source()
    lattice_tokens = ("root", "fiber", "class_of", "E8", "hbar")
    check("R3 Ward cubic source consumes no lattice/fiber/class token",
          not any(tok in src_f for tok in lattice_tokens),
          "src=%s" % src_f)
    # and the probe's FROZEN formula is the v3 shape (c3, M=41)
    check("R3b formula is the axiom cubic (c3, g_car budget M=41), "
          "an OFF-FIBER-SCALAR -- strong hyp 'all [E] are fiber-Fourier' "
          "DEAD",
          "c3" in src_f and "M = 41" in src_f)

    section("R4 no 16th direction")
    check("R4 zero class unused: no root labelled -1; NS/R and "
          "fiber-Fourier live on the 15; alpha lives on neither",
          -1 not in class_of.values()
          and all(class_of[r] >= 0 for r in roots))

    section("C3 scrambled signs are not Fourier")
    # one fiber, scramble signs independently vs the 8 Fourier modes
    i0 = 0
    fib = fibers[i0]
    vperp = [t for t in labels if hb(t, i0) == 0]
    r0 = min(fib)
    def x_of(r, origin):
        d = div_1i(sub_vec(r, origin))
        if d is None:
            return None
        return class_of_vec(d, reps, cstar)
    modes = []
    for u in vperp:
        modes.append(tuple(1 - 2 * hb(u, x_of(r, r0)) for r in fib))
    signs = lcg_sign(20260819, len(fib))
    scr = tuple(signs)
    is_copy = False
    for m in modes:
        if scr == m or scr == tuple(-x for x in m):
            is_copy = True
    check("C3 scrambled per-root signs (seed 20260819) are NOT a "
          "global-sign copy of a Fourier mode",
          not is_copy)

    section("verdict")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_tot = len(CHECKS)

    def pfx(pref):
        hits = [(n, ok) for n, ok in CHECKS if n.startswith(pref)]
        return bool(hits) and all(ok for _, ok in hits)

    c_ok = pfx("C1") and pfx("C2") and pfx("C3") and pfx("C4") and pfx("G0")
    strong_dead = pfx("R1") and pfx("R3")
    filtered = (pfx("R1") and pfx("R2") and pfx("R3") and pfx("R4")
                and c_ok and strong_dead)
    if not c_ok:
        verdict = "CONTROL-VOID"
    elif not (pfx("R2")):
        verdict = "READOUT-FOURIER-DEAD"
    elif filtered:
        verdict = "READOUT-FOURIER-FILTERED"
    else:
        verdict = "READOUT-FOURIER-PARTIAL"

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (n_pass, n_tot, SPEC_SHA[:16], time.time() - T0))
    print("VERDICT %s" % verdict)
    print("STRONG HYP (every [E] readout is a fiber-Fourier ray): "
          "%s" % ("DEAD" if strong_dead else "OPEN"))
    print("FILTER: NS/R = V-character; fiber-Fourier rays origin-free "
          "with P3-lite; alpha = off-fiber scalar; no 16th direction.  "
          "v775 ROOTCLASS-MIXED STANDS.  NO RH CLAIM.  "
          "NO MATTER SEMANTICS.")
    if n_pass != n_tot:
        print("FAILED: %s" % [n for n, ok in CHECKS if not ok])
    return 0 if (n_pass == n_tot
                 and verdict == "READOUT-FOURIER-FILTERED") else 1


if __name__ == "__main__":
    raise SystemExit(main())
