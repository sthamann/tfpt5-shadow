#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v782 -- E8.TRANSITIONBUS.01: the canonical v-perp pair-torsor structure on R(E8) -- each of the 15 Gaussian class fibers (240 = 15 x 16 roots; within-class Gram census {4:1, -4:1, 0:14} for all 240 roots, i.e. 15 disjoint 8-frames/cross-polytopes) maps 2:1 (r ~ -r) onto exactly the 120 q = 1 points of the plus-type quadratic space (L/2L, q), and the 8 pair images of class v are exactly the coset rho_v + iota(v_perp): a canonical affine 3-space (TORSOR) under v_perp with no distinguished origin (35/35 checks, ~2 s, verdict TRANSITION-BUS-TORSOR; discovery probe e8_transition_bus_probe.py, 2026-08-05).  THE FROZEN PREDICATE P (RULE_TEXT hashed before verification, SHA-256 baae8b8d68f3e7f05f3f93c8b2755d5f8300c5db8cbf75e3466b6b8b91f34220) reproduces ALL 57600 = 240 x 240 ordered inner products exactly: |<r,r'>| = 4 iff rho = rho', = 2 iff q(rho + rho') = 1, else 0 (57600/57600); the x-form q(rho+rho') = C(v,v') + hbar(v,x') + hbar(v',x) holds on all 53760/53760 cross-class pairs; value census {+4:240, -4:240, +2:13440, -2:13440, 0:30240}; SIGN LAW: every one of the 14400 realized (v,x,v',x') keys carries a sign-symmetric value set (the central -1 is provably NOT (x,v)-functional); the h-refinement partitions the hermitian values exactly as frozen; C(v,v') is basepoint-gauge data, not a function of hbar alone (gauge census {(0,0):36, (0,1):54, (1,0):40, (1,1):80}).  THE OBSTRUCTION (why TORSOR, not CANONICAL): deck J = mu4 acts on each pair fiber as translation by v but has cycle type 4+4+4+4 on every 16-root fiber, and -1 = J^2 is free on the 240 roots yet trivial on V x (V\{0}) -- no bijection R(E8) -> V x (V\{0}) is deck-equivariant; the level-3 coset property FAILS (measured branch, typed, not a kill), so the certified structure is the pair torsor plus an unoriented sign (exact freedom: 15 independent v_perp basepoints + 2^120 signs); 8 of 15 lex basepoint shifts under sigma are nonzero (exactly the torsor freedom).  SPREAD REFINEMENT: 56 PG(3,2) spreads, 15 isotropic lines, 6 Lagrangian spreads; the first partitions 240 = 5 x 3 x 16 (context x family direction x state) with q*-signature (1 of the 5bar, 2 of the 10) per block, q* = q_wt the unique arf-selected refinement among all 16.  A15 COMPARISON quantified: A15's 240 roots ARE literally the transitions e_x - e_{x+v} of V x (V\{0}); same within-class cross-polytope frame; cross-class census {+1:2, -1:2, 0:12} (pointer predicate) vs E8 {+2:4, -2:4, 0:8} (affine parity predicate) -- 13440 vs 26880 non-orthogonal ordered cross pairs, exactly 2x; Gram rank 15 vs 8; unoriented duality V/<v> ~ (v_perp)* exact for all 15 v.  All three must-fail controls fire (seeded per-class x-relabelings break the x-form on 26880/53760 cross pairs; the first wrong alternating form leaves a non-constant residual on 180/210 class pairs; scrambling the class assignment breaks the frame law on 128 same-tag pairs and the x-form on 3264 cross-tag pairs).  ROOTCLASS-MIXED (v775, ARF.ROOTCLASS.01) is unaffected: nothing here assigns SM states to classes; "transition bus" language stays interpretation, not claim.  No marker move, NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe e8_transition_bus_probe.py (2026-08-05, 35/35, ~1.6 s, TRANSITION-BUS-TORSOR; the DISCLOSED SPEC CORRECTION from the probe docstring carried verbatim below: the original C3 control transposed two class LABELS -- a global relabeling that preserves the class partition and is therefore vacuous, correctly caught as TEST-VOID -- and was corrected to scramble the class ASSIGNMENT itself, no result changed); re-run identically at promotion.  Promoted verbatim (top-level executable statements T0, C_NAIVE and RULE_SHA moved unchanged into main(); main() returns the verdict alongside the exit code so run() can gate the enum; numbers unchanged).  run() encodes the all-pass 35/35 TRANSITION-BUS-TORSOR pattern (v757 precedent).

Original e8_transition_bus_probe.py docstring (verbatim):
e8_transition_bus_probe -- E8.TRANSITIONBUS.01: is R(E8) canonically
V x (V \ {0}) as a STRUCTURED set (start state x, direction v), with a
fixed symplectic predicate reproducing all 240 x 240 inner products?

THE HYPOTHESIS (frozen before running).  Each of the 240 roots of the
unimodular hermitian E8 lattice L over Z[i] (v752 machinery, read-only)
is canonically a pair (x, v): a start state x in V = L/(1+i)L = F2^4
and a nonzero direction v = class(r) (certified: 15 classes x 16 roots,
v689/v752).  The decisive content is NOT the counting 240 = 16 x 15
(trivial) but:

 (T1) a CANONICAL x-labeling of the 16 roots inside each class, derived
      from the lattice alone.  The candidate levels are the (1+i)-adic
      refinements of the class map:
        level 1:  V   = L/(1+i)L        (the certified class map)
        level 2:  L/2L = L/(1+i)^2 L    ((1+i)^2 = 2i, 2iL = 2L)
        level 3:  L/(1+i)^3 L           ((1+i)^3 L = 2(1+i)L)
      PREDECLARED structural facts to establish (exact, each a check):
        (a) each class fiber is a coordinate FRAME: 8 mutually
            orthogonal antipodal pairs (cross-polytope), so the 240
            roots are 15 disjoint 8-frames;
        (b) on L/2L the quadratic form q(y) = <y,y>/4 mod 2 is well
            defined (L is <,>-even with values in 2Z, norms in 4Z);
            r |-> r mod 2L is exactly 2:1 (r ~ -r) and the 120 root
            PAIRS are precisely the 120 q = 1 points of the plus-type
            quadratic space (L/2L, q);
        (c) the 8 pair-images of class v form a COSET of
            (1+i)*(v_perp) inside the 16-element fiber of
            L/2L -> V over v, where v_perp = {t : hbar(v,t) = 0}
            (dim 3; contains v since hbar is alternating): the pair
            fiber is a canonical TORSOR under v_perp -- an affine
            3-space over F2 with no distinguished origin;
        (d) the deck generator J (multiplication by i; mu4) acts on
            the pair fiber as TRANSLATION BY v; -1 = J^2 acts
            trivially on L/2L;
        (e) OBSTRUCTION census: -1 acts freely on the 240 roots but
            trivially on V x (V\{0}) (2x in (1+i)L for all x), and J
            acts on each 16-root fiber with cycle type 4+4+4+4 while
            any torsor translation has order <= 2.  Hence NO bijection
            R(E8) -> V x (V\{0}) can be equivariant under the deployed
            deck symmetries: if the strict 16-state labeling exists at
            all it is pure bookkeeping.  The honest structured object
            is the PAIR level torsor (c) plus an unoriented sign.
        (f) level-3 investigation (open, graded either way): whether
            the 16-root fiber mod (1+i)^3 L is a coset of a canonical
            order-16 group G_v < (1+i)L/(1+i)^3 L (extension of
            v_perp by the antipode translation (1+i)^2 v).  If yes,
            the FULL fiber is canonically a G_v-torsor (G_v class-
            dependent, abstractly F2^4, NOT canonically V); if no,
            the certified structure stays (c) + sign gauge.

 (T2) a FIXED symplectic predicate.  Frozen dictionary (derived from
      the level-2 structure on a frozen 3-class-pair training set,
      hashed, then verified on all 57600 ordered pairs):
        data per root: v = class(r), rho = r mod 2L,
        basepoint rule: rho_v = lex-min pair image of class v (frozen
        v752 coordinates), x = iota^{-1}(rho + rho_v) in v_perp with
        iota = multiplication by (1+i): V -> (1+i)L/2L,
        C(v,v') = q(rho_v + rho_{v'}).
        DICTIONARY (norm-4 scaling; norm-2 values are half these):
          rho = rho'                      -> <,> = +-4   (r' = +-r)
          v = v', rho != rho'             -> <,> = 0     (frame)
          v != v': q(rho + rho') = C(v,v') + hbar(v,x') + hbar(v',x);
                   bit 1 -> <,> = +-2, bit 0 -> <,> = 0.
        SIGN LAW (part of the frozen claim): the sign on |<,>| in
        {4, 2} is NOT a function of (x, v, x', v') -- the central -1
        is invisible at every mod-(1+i)^2 level; every realized key
        must carry the sign-symmetric value set.  h-REFINEMENT:
        hbar(v,v') = |h(r,r')|^2 mod 2 and q(rho+rho') = Re h mod 2,
        so (q-bit, hbar) = (1,1) -> h in {+-1}; (1,0) -> {+-1+-i};
        (0,1) -> {+-i}; (0,0) -> {0, +-2, +-2i}.

 (T3) the spread refinement 240 = 5 x 3 x 16 (context x family
      direction x state) via the certified ISOTROPIC spreads of
      arf_spinor_compiler_probe.py S10: the 15 classes partition into
      5 totally isotropic (Lagrangian) blocks of 3; each block carries
      q*-signature (1 of the 5bar, 2 of the 10) with the arf-certified
      selector q* (sigma-invariant, q(A) = 1, q(F_Sigma) = 0, unique).

 (T4) A15 COMPARISON (the compression reading, honest): A15's 240
      roots ARE literally the transitions e_x - e_{x+v} of 16 states
      (x in V, v != 0) -- a strict V x (V\{0}) bus.  Preserved by E8:
      the transition count 240 = 16 x 15, the direction fibration
      (15 classes x 16), the within-class cross-polytope frame, an
      involution acting as translation-by-v on class fibers (A15: -1;
      E8: deck J on pairs), and the 8-element unoriented fiber with
      the canonical duality V/<v> ~ (v_perp)* via hbar.  Different:
      Gram rank 15 vs 8; cross-class incidence per root and foreign
      class {+1:2, -1:2, 0:12} (pointer/equality predicate) vs
      {+2:4, -2:4, 0:8} (affine parity predicate) -- exactly doubled
      non-orthogonality (13440 vs 26880 ordered cross pairs); A15 has
      a canonical start state, E8 provably has none (T1e).

CONTROLS (must fire, frozen):
  C1 random x-relabelings (seeded, per-class permutations of v_perp)
     break the frozen x-form of the predicate;
  C2 a wrong form (first of the 27 non-canonical nondegenerate
     alternating forms on F2^4, sorted order) breaks the predicate:
     for ANY constant C' some class pair has a non-constant residual;
  C3 scrambled classes break the frame purity and the predicate
     census.  DISCLOSED SPEC CORRECTION (first run, control-design
     bug, no result changed): the original C3 transposed two class
     LABELS -- a global relabeling that preserves the class partition
     (same-tag iff same-class) and is therefore VACUOUS (0 violations,
     verdict gate correctly returned TEST-VOID).  C3 now scrambles the
     class ASSIGNMENT itself: the 8 lexicographically first roots of
     the first two classes exchange their class tags, so each
     scrambled 'fiber' mixes two true frames.

VERDICT ENUM (frozen):
  TRANSITION-BUS-CANONICAL : a deck-equivariant root-level labeling
      R(E8) = V x (V\{0}) exists and the frozen predicate reproduces
      all 57600 products (promotion-grade claim text).
  TRANSITION-BUS-TORSOR    : the labeling exists only up to a global/
      per-class torsor (exact freedom stated); the frozen predicate
      holds on the canonical (difference/pair) data for all 57600
      products.  Still a real structure theorem.
  TRANSITION-BUS-DEAD      : no labeling makes the inner products
      class-functional; the counting stays decorative.
  TEST-VOID                : a must-fail control does not fire.
Frozen rule: DEAD if any T-check fails; TEST-VOID if any C-control
does not fire; CANONICAL only if the T1e obstruction is ABSENT and an
explicit equivariant V-labeling is constructed; otherwise TORSOR.

FENCES: finite exact algebra only (integers / Fractions / F2; no
floats in any claim, RNG only inside the must-fail control C1 with a
frozen seed).  No physics: "transition bus / instruction set" language
stays interpretation, not claim.  ROOTCLASS-MIXED (v775, ARF.ROOTCLASS
.01) is UNAFFECTED: the matter-classifier reading of the Gaussian
classes stays dead at root level; nothing here assigns SM states to
classes.  Nothing in this file moves a status marker.

FIREWALL: experiments/-probe; ONE new file; writes nothing; no
verification/-, paper-, ledger-, changelog- or website surface
touched.

Sources (read-only): verification/v752_projective_hamming_incidence.py
(lattice machinery, verbatim), experiments/tfpt-discovery/
arf_spinor_compiler_probe.py (spread + q* selector machinery),
verification/v775_gaussian_class_d5_purity.py (ROOTCLASS-MIXED fence).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/e8_transition_bus_probe.py
"""

import hashlib
import itertools
import random
import time
from collections import Counter
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)
    return bool(ok)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ======================================================================
# v752 machinery, copied VERBATIM (deterministic; read-only source)
# ======================================================================
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)
CSTAR_SUPPORTS_EXPECTED = [
    (0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6), (0, 2, 5, 7),
    (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7), (1, 2, 5, 6), (1, 3, 4, 6),
    (1, 3, 5, 7), (2, 3, 4, 5), (2, 3, 6, 7), (4, 5, 6, 7)]


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


def supports_w4(code):
    return sorted(tuple(i for i in range(8) if w[i])
                  for w in code if sum(w) == 4)


def mat_det_inv(rows):
    n = len(rows)
    A = [[Fr(v) for v in r] for r in rows]
    I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        if piv is None:
            return Fr(0), None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            I[col], I[piv] = I[piv], I[col]
            det = -det
        det *= A[col][col]
        inv = 1 / A[col][col]
        A[col] = [a * inv for a in A[col]]
        I[col] = [a * inv for a in I[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
                I[r] = [a - f * b for a, b in zip(I[r], I[col])]
    return det, I


def vec_mat(x, M):
    n = len(M)
    return tuple(sum(x[i] * M[i][j] for i in range(n)) for j in range(n))


def row_hnf(rows):
    M = [list(map(int, r)) for r in rows]
    m = len(M)
    for col in range(m):
        piv = next(r for r in range(col, m) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        for r in range(col + 1, m):
            while M[r][col] != 0:
                q = M[col][col] // M[r][col]
                M[col] = [a - q * b for a, b in zip(M[col], M[r])]
                M[col], M[r] = M[r], M[col]
        if M[col][col] < 0:
            M[col] = [-a for a in M[col]]
    return M


def hnf_reduce(c, H):
    c = list(c)
    for i in range(len(H)):
        q = c[i] // H[i][i]
        if q:
            c = [a - q * b for a, b in zip(c, H[i])]
    return tuple(c)


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def add_vec(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub_vec(x, y):
    return tuple(a - b for a, b in zip(x, y))


def neg_vec(x):
    return tuple(-a for a in x)


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


def f2_rref(words):
    rows = [list(w) for w in sorted(words, reverse=True) if any(w)]
    basis, pivots = [], []
    for r in rows:
        r = r[:]
        for b, pv in zip(basis, pivots):
            if r[pv]:
                r = [(a + c) % 2 for a, c in zip(r, b)]
        if any(r):
            basis.append(r)
            pivots.append(next(i for i, a in enumerate(r) if a))
    return basis, pivots


def make_lattice(in_lat, basis_rows):
    det, Binv = mat_det_inv(basis_rows)
    lat = {"in": in_lat, "B": basis_rows, "det": det, "Binv": Binv}

    def coords(x):
        c = vec_mat(x, Binv)
        assert all(v.denominator == 1 for v in c), "not a lattice vector"
        return tuple(int(v) for v in c)

    A = [coords(add_vec(b, J_vec(b))) for b in basis_rows]
    H = row_hnf(A)
    lat["coords"] = coords
    lat["A"] = A
    lat["H"] = H
    lat["label"] = lambda x: hnf_reduce(coords(x), H)
    return lat


def constrA_lattice(code):
    cb, pivots = f2_rref(code)
    rows = [tuple(r) for r in cb]
    rows += [tuple(2 if i == j else 0 for i in range(8))
             for j in range(8) if j not in pivots]
    return make_lattice(lambda x: tuple(v % 2 for v in x) in code, rows)


def constrA_roots(code):
    return [x for x in itertools.product(range(-2, 3), repeat=8)
            if sum(v * v for v in x) == 4
            and tuple(v % 2 for v in x) in code]


def label_group(lat):
    reps = {hnf_reduce((0,) * 8, lat["H"]): (0,) * 8}
    frontier = [(0,) * 8]
    while frontier:
        v = frontier.pop()
        for b in lat["B"]:
            w = add_vec(v, b)
            l = lat["label"](w)
            if l not in reps:
                reps[l] = w
                frontier.append(w)
    return reps


def family_anchor_basis(lat, reps, zero_label, sig_label_fn):
    fixed_labels = [lb for lb in reps if sig_label_fn(lb) == lb]
    fam_basis = None
    for lb in reps:
        if lb == zero_label or sig_label_fn(lb) == lb:
            continue
        o1 = lb
        o2 = sig_label_fn(lb)
        o3 = sig_label_fn(o2)
        s = lat["label"](add_vec(add_vec(reps[o1], reps[o2]), reps[o3]))
        if s == zero_label:
            continue
        span3 = set()
        for bits in itertools.product((0, 1), repeat=3):
            w = (0,) * 8
            for bit, l2 in zip(bits, (o1, o2, o3)):
                if bit:
                    w = add_vec(w, reps[l2])
            span3.add(lat["label"](w))
        if len(span3) != 8:
            continue
        anchor = next(l2 for l2 in fixed_labels
                      if l2 != zero_label and l2 not in span3)
        fam_basis = (o1, o2, o3, anchor, s)
        break
    assert fam_basis is not None
    o1, o2, o3, anc, fsum = fam_basis
    bits_of = {}
    for bits in itertools.product((0, 1), repeat=4):
        v = (0,) * 8
        for bit, l2 in zip(bits, (o1, o2, o3, anc)):
            if bit:
                v = add_vec(v, reps[l2])
        bits_of[lat["label"](v)] = bits
    return fam_basis, bits_of


def herm(x, y):
    """h(x,y) = (<x,y> + i <x,Jy>)/2 as a pair (Re, Im) in Z[i]."""
    re2, im2 = ip(x, y), ip(x, J_vec(y))
    assert re2 % 2 == 0 and im2 % 2 == 0, "h not Z[i]-valued"
    return (re2 // 2, im2 // 2)


def hbar_vec(x, y):
    h = herm(x, y)
    return (h[0] + h[1]) % 2


# ======================================================================
# frozen predicate text (T2), hashed before the full verification loop
# ======================================================================
RULE_TEXT = """E8.TRANSITIONBUS.01 frozen predicate P (pair level):
data per root r: v = class(r) in V\\{0}; rho = r mod 2L in L/2L
  (coordinates in the frozen v752 basis B8, reduced mod 2).
basepoint rule: rho_v = lexicographically smallest rho among the 8
  pair images of class v; x = iota^{-1}(rho + rho_v) in v_perp,
  iota = multiplication by (1+i): V -> (1+i)L/2L.
C(v,v') = q(rho_v + rho_{v'}), q(y) = <y,y>/4 mod 2 on L/2L.
DICTIONARY (|<r,r'>| in the norm-4 scaling):
  rho == rho'                          -> |<,>| = 4  (r' = +-r)
  v == v', rho != rho'                 -> <,>  = 0  (frame; q-bit 0)
  v != v': q(rho+rho') = C(v,v') + hbar(v,x') + hbar(v',x);
           bit 1 -> |<,>| = 2 ; bit 0 -> <,> = 0.
SIGN LAW: the sign on |<,>| in {4,2} is NOT a function of
  (v,x,v',x'); every realized key carries the sign-symmetric set.
h-REFINEMENT: hbar(v,v') = |h|^2 mod 2, q(rho+rho') = Re h mod 2:
  (1,1) -> h in {+-1}; (1,0) -> h in {+-1+-i};
  (0,1) -> h in {+-i}; (0,0) -> h in {0,+-2,+-2i}."""


def main():
    T0 = time.time()
    C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                              for j in range(8))
                        for m in itertools.product((0, 1), repeat=4))
    RULE_SHA = hashlib.sha256(RULE_TEXT.encode()).hexdigest()
    print("=" * 78)
    print("E8.TRANSITIONBUS.01 -- the E8 transition-bus hypothesis "
          "(exploration probe)")
    print("=" * 78, flush=True)

    # ------------------------------------------------------------- P0
    section("P0: the certified v752 state (C*, L, 15 x 16 classes, "
            "family basis)")
    all_placements = set()
    for p in itertools.permutations(range(8)):
        all_placements.add(code_image(C_NAIVE, p))
    both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
                if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
    CSTAR = [c for c in both_inv if W0246 in c][0]
    ROOTS = sorted(constrA_roots(CSTAR))
    LAT = constrA_lattice(CSTAR)
    REPS = label_group(LAT)
    ZERO = LAT["label"]((0,) * 8)
    coords = LAT["coords"]
    root_label = {r: LAT["label"](r) for r in ROOTS}
    census = Counter(root_label.values())
    check("P0.1 C* deterministic (v638 recipe), 240 roots, census "
          "15 x 16, zero class empty",
          supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED
          and len(ROOTS) == 240 and len(REPS) == 16 and len(census) == 15
          and sorted(census.values()) == [16] * 15 and ZERO not in census)

    def sig_label(lb):
        return LAT["label"](sig_vec(REPS[lb]))

    FAM, BITS = family_anchor_basis(LAT, REPS, ZERO, sig_label)
    F1L, F2L, F3L, ANCL, FSUML = FAM
    LBLS = sorted(REPS)
    P15 = [lb for lb in LBLS if lb != ZERO]
    HB = {(a, b): hbar_vec(REPS[a], REPS[b]) for a in LBLS for b in LBLS}
    ADDV = {(a, b): LAT["label"](add_vec(REPS[a], REPS[b]))
            for a in LBLS for b in LBLS}
    VPERP = {v: [t for t in LBLS if HB[(t, v)] == 0] for v in P15}
    check("P0.2 (V, hbar) symplectic: hbar alternating, nondegenerate; "
          "|v_perp| = 8 for all 15 v (v in v_perp)",
          all(HB[(a, a)] == 0 for a in LBLS)
          and all(any(HB[(a, b)] for b in LBLS)
                  for a in LBLS if a != ZERO)
          and all(len(VPERP[v]) == 8 and v in VPERP[v] for v in P15))

    FIBER = {v: [r for r in ROOTS if root_label[r] == v] for v in P15}

    # ------------------------------------------------------------- T1a
    section("T1a: each class fiber is a coordinate FRAME "
            "(8 orthogonal antipodal pairs)")
    ok_frame = True
    for v in P15:
        for r in FIBER[v]:
            cen = Counter(ip(r, r2) for r2 in FIBER[v])
            if cen != Counter({0: 14, 4: 1, -4: 1}):
                ok_frame = False
    check("T1a.1 within-class Gram census per root = {4:1 (self), "
          "-4:1 (antipode), 0:14} for all 240 roots: the 240 roots are "
          "15 disjoint 8-frames (cross-polytopes)", ok_frame)

    # ------------------------------------------------------------- T1b
    section("T1b: level 2 -- L/2L = L/(1+i)^2 L, the quadratic form q, "
            "and the pair torsor")

    def rho_of(r):
        return tuple(c % 2 for c in coords(r))

    def lift2(rho):
        w = (0,) * 8
        for i, bit in enumerate(rho):
            if bit:
                w = add_vec(w, LAT["B"][i])
        return w

    RHO256 = list(itertools.product((0, 1), repeat=8))
    ok_q_wd = True
    Q2 = {}
    for rho in RHO256:
        w = lift2(rho)
        n = ip(w, w)
        assert n % 4 == 0
        Q2[rho] = (n // 4) % 2
        for b in LAT["B"]:
            w2 = add_vec(w, tuple(2 * a for a in b))
            if (ip(w2, w2) // 4) % 2 != Q2[rho]:
                ok_q_wd = False
    check("T1b.1 q(y) = <y,y>/4 mod 2 is WELL DEFINED on L/2L "
          "(all 256 classes x 8 basis shifts exact)", ok_q_wd)

    ok_quad = True
    for rho in RHO256:
        for tau in RHO256[:32]:
            s = tuple((a + b) % 2 for a, b in zip(rho, tau))
            crs = (ip(lift2(rho), lift2(tau)) // 2) % 2
            if Q2[s] != (Q2[rho] + Q2[tau] + crs) % 2:
                ok_quad = False
    n_q1 = sum(Q2[rho] for rho in RHO256)
    check("T1b.2 q is quadratic w.r.t. cross(y,z) = <y,z>/2 mod 2 "
          "(256 x 32 cells); # q = 1 classes = %d == 120 (plus type)"
          % n_q1, ok_quad and n_q1 == 120)

    ROOT_RHO = {r: rho_of(r) for r in ROOTS}
    rho_census = Counter(ROOT_RHO.values())
    ok_2to1 = (len(rho_census) == 120
               and sorted(rho_census.values()) == [2] * 120
               and all(ROOT_RHO[r] == ROOT_RHO[neg_vec(r)] for r in ROOTS)
               and all(Q2[ROOT_RHO[r]] == 1 for r in ROOTS))
    check("T1b.3 r -> r mod 2L is exactly 2:1 (r ~ -r); the 120 pair "
          "images are precisely the 120 q = 1 points", ok_2to1)

    # class of a level-2 point, and the (1+i)-lift iota: V -> (1+i)L/2L
    RHO_CLASS = {rho: LAT["label"](lift2(rho)) for rho in RHO256}
    IOTA = {}
    ok_iota = True
    for lb in LBLS:
        x = REPS[lb]
        IOTA[lb] = rho_of(add_vec(x, J_vec(x)))          # (1+i) x mod 2L
    INV_IOTA = {IOTA[lb]: lb for lb in LBLS}
    ker = [rho for rho in RHO256 if RHO_CLASS[rho] == ZERO]
    ok_iota = (len(INV_IOTA) == 16 and sorted(ker) == sorted(IOTA.values())
               and all(IOTA[ADDV[(a, b)]]
                       == tuple((p + q) % 2
                                for p, q in zip(IOTA[a], IOTA[b]))
                       for a in LBLS for b in LBLS))
    check("T1b.4 iota = mult by (1+i): V -> (1+i)L/2L is an additive "
          "bijection onto the kernel of L/2L -> V (16 = 16)", ok_iota)

    PAIR_IMG = {v: sorted(set(ROOT_RHO[r] for r in FIBER[v]))
                for v in P15}
    RHO_BASE = {v: PAIR_IMG[v][0] for v in P15}           # frozen lex rule
    ok_coset = True
    for v in P15:
        want = sorted(tuple((a + b) % 2
                            for a, b in zip(RHO_BASE[v], IOTA[t]))
                      for t in VPERP[v])
        if PAIR_IMG[v] != want:
            ok_coset = False
    check("T1b.5 PAIR TORSOR: the 8 pair images of class v are exactly "
          "the coset rho_v + iota(v_perp) inside the 16-element fiber "
          "of L/2L -> V (all 15 classes): canonical affine 3-space "
          "over v_perp, no distinguished origin", ok_coset)

    # x-labeling from the frozen basepoint rule
    XLAB = {}
    ok_x = True
    for r in ROOTS:
        v = root_label[r]
        d = tuple((a + b) % 2
                  for a, b in zip(ROOT_RHO[r], RHO_BASE[v]))
        x = INV_IOTA.get(d)
        if x is None or HB[(x, v)] != 0:
            ok_x = False
        XLAB[r] = x
    x_census_ok = all(
        Counter(XLAB[r] for r in FIBER[v])
        == Counter({t: 2 for t in VPERP[v]}) for v in P15)
    check("T1b.6 x-labeling: x(r) in v_perp for all 240 roots; each of "
          "the 8 states is hit by exactly 2 roots (+-)",
          ok_x and x_census_ok)

    # ------------------------------------------------------------- T1c
    section("T1c: deployed symmetries on the labeling "
            "(deck J = mu4, -1, sigma)")
    ok_J = all(
        ROOT_RHO[tuple(J_vec(r))]
        == tuple((a + b) % 2
                 for a, b in zip(ROOT_RHO[r], IOTA[root_label[r]]))
        for r in ROOTS)
    ok_Jx = all(XLAB[tuple(J_vec(r))]
                == ADDV[(XLAB[r], root_label[r])] for r in ROOTS)
    check("T1c.1 deck J acts on each pair fiber as TRANSLATION BY v: "
          "rho(Jr) = rho(r) + iota(v), x(Jr) = x(r) + v (240 exact)",
          ok_J and ok_Jx)
    ok_neg = all(ROOT_RHO[neg_vec(r)] == ROOT_RHO[r]
                 and XLAB[neg_vec(r)] == XLAB[r]
                 and neg_vec(r) != r for r in ROOTS)
    check("T1c.2 -1 = J^2 acts freely on the 240 roots but TRIVIALLY "
          "on all (x, v) data (2x in (1+i)L)", ok_neg)

    ok_sig_diff = True
    n_shift = 0
    for v in P15:
        w = sig_label(v)
        shifts = set()
        for r in FIBER[v]:
            rs = tuple(sig_vec(r))
            d = ADDV[(XLAB[rs], sig_label(XLAB[r]))]
            shifts.add(d)
        if len(shifts) != 1:
            ok_sig_diff = False
        elif next(iter(shifts)) != ZERO:
            n_shift += 1
    check("T1c.3 sigma equivariance census: x(sigma r) = sigma(x(r)) + "
          "delta(v) with a SINGLE per-class shift delta(v) (torsor "
          "differences fully sigma-equivariant); %d of 15 basepoint "
          "shifts nonzero (lex basepoints are not natural -- exactly "
          "the torsor freedom)" % n_shift, ok_sig_diff)

    # ------------------------------------------------------------- T1d
    section("T1d: the OBSTRUCTION -- no deck-equivariant V-labeling of "
            "the 16-root fibers")
    ok_cyc = True
    for v in P15:
        seen = set()
        cyc = []
        for r in FIBER[v]:
            if r in seen:
                continue
            orb = [r]
            s = tuple(J_vec(r))
            while s != r:
                orb.append(s)
                s = tuple(J_vec(s))
            seen |= set(orb)
            cyc.append(len(orb))
        if sorted(cyc) != [4, 4, 4, 4]:
            ok_cyc = False
    obstruction = ok_cyc and ok_neg
    check("T1d.1 J has cycle type 4+4+4+4 on every 16-root fiber; any "
          "translation of an F2^4-torsor has order <= 2; and -1 is free "
          "on roots, trivial on V x (V\\{0}).  CONCLUSION: no bijection "
          "R(E8) -> V x (V\\{0}) is equivariant under the deployed deck "
          "symmetries -- the strict 16-state labeling cannot be "
          "canonical", obstruction)

    # ------------------------------------------------------------- T1e
    section("T1e: level 3 -- is the 16-root fiber mod (1+i)^3 L a coset "
            "of a canonical order-16 group G_v?")
    H3 = row_hnf([[2 * a for a in row] for row in LAT["A"]])

    def lab3(x):
        return hnf_reduce(coords(x), H3)

    ZERO3 = lab3((0,) * 8)
    coset_all = True
    ok_ker = True
    ok_proj = True
    ok_Jstab = True
    for v in P15:
        S = FIBER[v]
        r0 = S[0]
        diffs = [sub_vec(r, r0) for r in S]
        D = {lab3(d): d for d in diffs}
        if len(D) != 16:
            coset_all = False
            continue
        Dset = set(D)
        for d1 in diffs:
            for d2 in diffs:
                if lab3(add_vec(d1, d2)) not in Dset:
                    coset_all = False
        # kernel part: elements of D lying in (1+i)^2 L = 2L
        kerD = sorted(l3 for l3, d in D.items()
                      if all(c % 2 == 0 for c in coords(d)))
        anti = lab3(tuple(2 * a for a in J_vec(REPS[v])))   # (1+i)^2 v
        if kerD != sorted([ZERO3, lab3(sub_vec(neg_vec(r0), r0))]) \
                or lab3(sub_vec(neg_vec(r0), r0)) != anti:
            ok_ker = False
        # projection to level 2 = iota(v_perp)
        proj = sorted(set(rho_of(d) for d in diffs))
        if proj != sorted(set(IOTA[t] for t in VPERP[v])):
            ok_proj = False
        if {lab3(J_vec(d)) for d in diffs} != Dset:
            ok_Jstab = False
    print("    coset property over all 15 classes: %s" % coset_all)
    if coset_all:
        check("T1e.1 LEVEL-3 TORSOR: for every class the 16-root fiber "
              "mod (1+i)^3 L IS a coset of an order-16 elementary-"
              "abelian group G_v < (1+i)L/(1+i)^3 L; kernel part "
              "{0, (1+i)^2 v} (antipode translation), projection "
              "iota(v_perp), J-stable -- the FULL fiber is canonically "
              "a G_v-torsor with G_v the class-dependent extension "
              "0 -> <(1+i)^2 v> -> G_v -> v_perp -> 0 (abstractly "
              "F2^4, NOT canonically V)",
              coset_all and ok_ker and ok_proj and ok_Jstab)
    else:
        check("T1e.1 level-3 coset property FAILS somewhere: the "
              "certified structure stays the pair torsor (T1b.5) plus "
              "an unoriented sign; graded, not a kill", True,
              "coset=False (branch typed in header)")

    # ------------------------------------------------------------- T2a
    section("T2a: derive the predicate on the frozen training subset "
            "(one class pair per relation type)")
    vA = P15[0]
    trainB = next((v, w) for v in P15 for w in P15
                  if w != v and HB[(v, w)] == 0)
    trainC = next((v, w) for v in P15 for w in P15
                  if w != v and HB[(v, w)] == 1)
    print("    training pairs: A (same class) = (%s, %s)" % (vA, vA))
    print("                    B (hbar = 0)   = (%s, %s)" % trainB)
    print("                    C (hbar = 1)   = (%s, %s)" % trainC)

    ok_trainA = True
    for r in FIBER[vA]:
        for s in FIBER[vA]:
            rho_s = tuple((a + b) % 2
                          for a, b in zip(ROOT_RHO[r], ROOT_RHO[s]))
            if Q2[rho_s] != 0:
                ok_trainA = False
            want = 4 if ROOT_RHO[r] == ROOT_RHO[s] else 0
            if abs(ip(r, s)) != want:
                ok_trainA = False
    check("T2a.1 type A (same class): q(rho+rho') = 0 always; "
          "|<,>| = 4 iff rho = rho', else 0 (frame law derived)",
          ok_trainA)

    def fit_C(v, w):
        vals = set()
        for r in FIBER[v]:
            for s in FIBER[w]:
                rho_s = tuple((a + b) % 2
                              for a, b in zip(ROOT_RHO[r], ROOT_RHO[s]))
                bit = (Q2[rho_s] + HB[(XLAB[s], v)]
                       + HB[(XLAB[r], w)]) % 2
                vals.add(bit)
        return vals

    def base_C(v, w):
        rho_s = tuple((a + b) % 2
                      for a, b in zip(RHO_BASE[v], RHO_BASE[w]))
        return Q2[rho_s]

    okB = fit_C(*trainB) == {base_C(*trainB)}
    okC = fit_C(*trainC) == {base_C(*trainC)}
    ok_absB = all((abs(ip(r, s)) == 2)
                  == (Q2[tuple((a + b) % 2 for a, b in
                               zip(ROOT_RHO[r], ROOT_RHO[s]))] == 1)
                  for r in FIBER[trainB[0]] for s in FIBER[trainB[1]])
    check("T2a.2 types B and C (cross class): q(rho+rho') - hbar(v,x') "
          "- hbar(v',x) is CONSTANT = C(v,v') = q(rho_v + rho_v') on "
          "all 256 training pairs each; |<,>| = 2 iff q-bit = 1 "
          "(affine law derived)", okB and okC and ok_absB)

    print("    FROZEN RULE (verbatim in source, hashed now, verified "
          "next on all 57600):")
    print("    RULE SHA-256 = %s" % RULE_SHA)

    # ------------------------------------------------------------- T2b
    section("T2b: FULL VERIFICATION -- all 240 x 240 = 57600 ordered "
            "pairs against the frozen dictionary")
    CMAT = {(v, w): base_C(v, w) for v in P15 for w in P15 if v != w}
    n_match = 0
    n_xform = 0
    n_xform_tot = 0
    val_census = Counter()
    sign_keys = {}
    h_census = {}
    cross_deg_ok = True
    for r in ROOTS:
        v = root_label[r]
        xr = XLAB[r]
        rr = ROOT_RHO[r]
        per_class = {}
        for s in ROOTS:
            w = root_label[s]
            actual = ip(r, s)
            val_census[actual] += 1
            rho_s = tuple((a + b) % 2 for a, b in zip(rr, ROOT_RHO[s]))
            qbit = Q2[rho_s]
            if rr == ROOT_RHO[s]:
                pred = 4
            elif qbit == 1:
                pred = 2
            else:
                pred = 0
            if abs(actual) == pred:
                n_match += 1
            if v != w:
                n_xform_tot += 1
                bit = (CMAT[(v, w)] + HB[(XLAB[s], v)]
                       + HB[(xr, w)]) % 2
                if bit == qbit:
                    n_xform += 1
                per_class.setdefault(w, Counter())[actual] += 1
            key = (v, xr, w, XLAB[s])
            sign_keys.setdefault(key, set()).add(actual)
            hv = herm(r, s)
            h_census.setdefault((qbit, HB[(v, w)]),
                                Counter())[hv] += 1
        for w, cen in per_class.items():
            if cen != Counter({0: 8, 2: 4, -2: 4}):
                cross_deg_ok = False
    check("T2b.1 DICTIONARY EXACT: predicted |<,>| matches on "
          "%d / 57600 ordered pairs" % n_match, n_match == 57600)
    check("T2b.2 x-FORM EXACT: q(rho+rho') = C(v,v') + hbar(v,x') + "
          "hbar(v',x) on %d / %d cross-class pairs"
          % (n_xform, n_xform_tot),
          n_xform == n_xform_tot == 240 * 224)
    check("T2b.3 value census: {4:240, -4:240, +2:13440, -2:13440, "
          "0:30240} -- got %s"
          % dict(sorted(val_census.items())),
          val_census == Counter({4: 240, -4: 240, 2: 13440,
                                 -2: 13440, 0: 30240}))
    ok_sign = all(vals in ({0}, {2, -2}, {4, -4})
                  for vals in sign_keys.values())
    n_keys = len(sign_keys)
    check("T2b.4 SIGN LAW: every one of the %d realized (v,x,v',x') "
          "keys carries a sign-symmetric value set {0} / {+-2} / "
          "{+-4}: the sign is provably NOT (x,v)-functional (central "
          "-1 gauge)" % n_keys, ok_sign and n_keys == 14400)
    check("T2b.5 cross-class regularity: per root and foreign class "
          "the signed census is ALWAYS {+2:4, -2:4, 0:8}", cross_deg_ok)

    H_EXPECT = {
        (1, 1): {(1, 0), (-1, 0)},
        (1, 0): {(1, 1), (1, -1), (-1, 1), (-1, -1)},
        (0, 1): {(0, 1), (0, -1)},
        (0, 0): {(0, 0), (2, 0), (-2, 0), (0, 2), (0, -2)}}
    ok_h = all(set(cen) == H_EXPECT[k] for k, cen in h_census.items())
    print("    h-value census by (q-bit, hbar(v,v')):")
    for k in sorted(h_census):
        print("      (q=%d, hbar=%d): %s"
              % (k[0], k[1], dict(sorted(h_census[k].items()))))
    check("T2b.6 h-REFINEMENT exact: hbar(v,v') = |h|^2 mod 2 and "
          "q-bit = Re h mod 2 partition the hermitian values as "
          "frozen", ok_h)

    c_by_hbar = Counter((HB[(v, w)], CMAT[(v, w)])
                        for v in P15 for w in P15 if v != w)
    print("    gauge census: (hbar(v,v'), C(v,v')) over the 210 "
          "ordered class pairs: %s" % dict(sorted(c_by_hbar.items())))
    check("T2b.7 C(v,v') is basepoint-gauge data, NOT a function of "
          "hbar(v,v') alone (both C values occur for some hbar value) "
          "-- the gauge-free predicate is q(rho+rho') itself",
          len(c_by_hbar) > 2)

    # ------------------------------------------------------------- T3
    section("T3: the spread refinement 240 = 5 x 3 x 16 "
            "(context x family direction x state)")
    lines = set()
    for a, b in itertools.combinations(P15, 2):
        lines.add(frozenset({a, b, ADDV[(a, b)]}))
    by_pt = {}
    for L in lines:
        for p in L:
            by_pt.setdefault(p, []).append(L)

    def find_spreads(covered, used):
        if len(covered) == 15:
            return [frozenset(used)]
        p = next(x for x in P15 if x not in covered)
        out = []
        for L in by_pt[p]:
            if covered & L:
                continue
            out += find_spreads(covered | L, used + [L])
        return out

    spreads = set(find_spreads(frozenset(), []))
    iso_line = {L: all(HB[(a, b)] == 0 for a in L for b in L)
                for L in lines}
    iso_spreads = sorted(
        (S for S in spreads if all(iso_line[L] for L in S)),
        key=lambda s: sorted(sorted(w) for w in s))
    check("T3.1 56 PG(3,2) spreads, 15 isotropic lines (GQ(2,2)); "
          "%d fully isotropic (Lagrangian) spreads (arf S10 machinery, "
          "deterministic order)" % len(iso_spreads),
          len(spreads) == 56
          and sum(1 for L in lines if iso_line[L]) == 15
          and len(iso_spreads) >= 1)
    S0 = iso_spreads[0]
    S0_blocks = sorted(S0, key=sorted)
    ok_part = (sorted(lb for B in S0_blocks for lb in B) == sorted(P15)
               and all(sum(census[lb] for lb in B) == 48
                       for B in S0_blocks))
    check("T3.2 the first isotropic spread partitions the 240 roots as "
          "5 contexts x 3 family directions x 16 states = 5 x 48; "
          "each block is a totally isotropic 2D subspace (all "
          "within-context class pairs have hbar = 0, i.e. h-values "
          "in the even register)", ok_part)

    # q* via the arf-frozen selector (refinements built directly)
    W16b = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
    GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]

    def hbbits(a, b):
        return sum(a[i] * GJI[i][j] * b[j]
                   for i in range(4) for j in range(4)) % 2

    ok_bits = all(HB[(a, b)] == hbbits(BITS[a], BITS[b])
                  for a in LBLS for b in LBLS)

    def iota5(w):
        return (w[0], w[1], w[2], w[3],
                (w[0] + w[1] + w[2] + w[3]) % 2)

    def qwt(w):
        return (sum(iota5(w)) // 2) % 2

    refs = []
    for c in W16b:
        q = {w: (qwt(w) + hbbits(w, c)) % 2 for w in W16b}
        is_ref = all(
            (q[tuple((a + b) % 2 for a, b in zip(v2, w2))]
             + q[v2] + q[w2]) % 2 == hbbits(v2, w2)
            for v2 in W16b for w2 in W16b)
        if is_ref:
            refs.append(tuple(q[w] for w in W16b))
    A_BIT, FSIG = (0, 0, 0, 1), (1, 1, 1, 0)
    WIDXb = {w: i for i, w in enumerate(W16b)}

    def sig_bits(w):
        return (w[2], w[0], w[1], w[3])

    siginv = [q for q in set(refs)
              if all(q[WIDXb[sig_bits(w)]] == q[WIDXb[w]] for w in W16b)]
    cand = [q for q in siginv
            if q[WIDXb[A_BIT]] == 1 and q[WIDXb[FSIG]] == 0]
    qstar = tuple(qwt(w) for w in W16b)
    check("T3.3 the 16 refinements q_c = q_wt + hbar(.,c) all verify "
          "and are distinct (difference of two refinements is linear "
          "=> these are ALL, arf S2 brute-force certified); the arf "
          "selector (sigma-invariant, q(A)=1, q(F_Sigma)=0) picks "
          "exactly q* = q_wt",
          ok_bits and len(refs) == 16 and len(set(refs)) == 16
          and len(cand) == 1 and cand[0] == qstar)

    ok_sig_blocks = True
    for B in S0_blocks:
        n0 = sum(1 for lb in B if qstar[WIDXb[BITS[lb]]] == 0)
        n1 = sum(1 for lb in B if qstar[WIDXb[BITS[lb]]] == 1)
        if (n0, n1) != (1, 2):
            ok_sig_blocks = False
    check("T3.4 q*-signature per context block = (1 of the 5bar, 2 of "
          "the 10) -- the arf-certified spread refinement "
          "240 = 5 x (1+2) x 16", ok_sig_blocks)
    print("    contexts (blocks of the first isotropic spread):")
    for k, B in enumerate(S0_blocks):
        print("      block %d: classes %s" % (k, sorted(B)))

    # ------------------------------------------------------------- T4
    section("T4: A15 comparison -- the literal 16-state transition bus")
    # A15 roots as e_x - e_{x+v} on the 16 states = V (labels)
    LIDX = {lb: i for i, lb in enumerate(LBLS)}
    a15 = []
    for x in LBLS:
        for v in P15:
            vec = [0] * 16
            vec[LIDX[x]] += 1
            vec[LIDX[ADDV[(x, v)]]] -= 1
            a15.append((x, v, tuple(vec)))
    ok_a15 = (len(set(t[2] for t in a15)) == 240
              and all(sum(a * a for a in t[2]) == 2 for t in a15))
    check("T4.1 A15 root system built as the 240 transitions "
          "e_x - e_{x+v}: R(A15) IS V x (V\\{0}) literally (bijection "
          "by construction), 15 direction classes x 16 start states",
          ok_a15)

    ok_within = True
    ok_cross = True
    n_nonzero_cross = 0
    for x, v, vec in a15:
        cen_own = Counter()
        cross_cen = {}
        for x2, v2, vec2 in a15:
            d = ip(vec, vec2)
            if v2 == v:
                cen_own[d] += 1
            else:
                cross_cen.setdefault(v2, Counter())[d] += 1
                if d != 0:
                    n_nonzero_cross += 1
        if cen_own != Counter({2: 1, -2: 1, 0: 14}):
            ok_within = False
        for v2, cen in cross_cen.items():
            if cen != Counter({1: 2, -1: 2, 0: 12}):
                ok_cross = False
    check("T4.2 A15 within-class census {+2:1, -2:1, 0:14}: the SAME "
          "cross-polytope frame as every E8 class (T1a; E8 values 4 = "
          "2 x norm-2 scaling); -1 acts on the A15 class fiber as "
          "translation by v (e_{x+v} - e_x = -(e_x - e_{x+v})), the "
          "role deck J plays for E8 pairs (T1c.1)", ok_within)
    check("T4.3 A15 cross-class census per root and foreign class = "
          "{+1:2, -1:2, 0:12} (pointer/equality predicate: share a "
          "state) vs E8 {+2:4, -2:4, 0:8} (affine parity predicate): "
          "non-orthogonal ordered cross pairs %d vs 26880 = exactly "
          "2x" % n_nonzero_cross,
          ok_cross and n_nonzero_cross == 13440
          and 2 * n_nonzero_cross == 26880)

    def frac_rank(rows):
        M = [[Fr(x) for x in r] for r in rows]
        rank = 0
        nrows, ncols = len(M), len(M[0])
        for col in range(ncols):
            piv = next((r for r in range(rank, nrows)
                        if M[r][col] != 0), None)
            if piv is None:
                continue
            M[rank], M[piv] = M[piv], M[rank]
            inv = 1 / M[rank][col]
            M[rank] = [y * inv for y in M[rank]]
            for r2 in range(nrows):
                if r2 != rank and M[r2][col] != 0:
                    f = M[r2][col]
                    M[r2] = [y - f * z
                             for y, z in zip(M[r2], M[rank])]
            rank += 1
            if rank == nrows:
                break
        return rank

    rkE8 = frac_rank([list(r) for r in ROOTS])
    rkA15 = frac_rank([list(t[2]) for t in a15])
    check("T4.4 Gram rank (= rank of the root coordinate matrix): "
          "E8 = %d, A15 = %d -- the compression is 15 -> 8"
          % (rkE8, rkA15), rkE8 == 8 and rkA15 == 15)

    ok_dual = True
    for v in P15:
        cosets = {}
        for u in LBLS:
            key = frozenset({u, ADDV[(u, v)]})
            cosets[key] = tuple(HB[(u, t)] for t in VPERP[v])
        if len(set(cosets.values())) != 8:
            ok_dual = False
    check("T4.5 unoriented duality: for every v the map "
          "V/<v> -> (v_perp)*, [u] -> hbar(u,.)|_{v_perp} is a "
          "bijection (8 = 8): A15's unoriented class fiber V/<v> is "
          "canonically the DUAL of E8's pair-torsor group v_perp",
          ok_dual)

    # ------------------------------------------------------------- C
    section("C: must-fail controls (frozen)")
    rng = random.Random(20260805)
    XSCR = dict(XLAB)
    nontriv = False
    for v in P15:
        perm = list(VPERP[v])
        rng.shuffle(perm)
        pmap = dict(zip(sorted(VPERP[v]), perm))
        if any(a != b for a, b in pmap.items()):
            nontriv = True
        for r in FIBER[v]:
            XSCR[r] = pmap[XLAB[r]]
    n_bad1 = 0
    for r in ROOTS:
        v = root_label[r]
        for s in ROOTS:
            w = root_label[s]
            if v == w:
                continue
            rho_s = tuple((a + b) % 2
                          for a, b in zip(ROOT_RHO[r], ROOT_RHO[s]))
            bit = (CMAT[(v, w)] + HB[(XSCR[s], v)]
                   + HB[(XSCR[r], w)]) % 2
            if bit != Q2[rho_s]:
                n_bad1 += 1
    check("C1 CONTROL FIRES: seeded random per-class x-relabelings "
          "(nontrivial: %s) break the x-form on %d / 53760 cross "
          "pairs" % (nontriv, n_bad1), nontriv and n_bad1 > 0)

    alt_forms = []
    for bits in itertools.product((0, 1), repeat=6):
        G = [[0] * 4 for _ in range(4)]
        k = 0
        for i in range(4):
            for j in range(i + 1, 4):
                G[i][j] = G[j][i] = bits[k]
                k += 1
        rank = len([r for r in f2_rref([tuple(row) for row in G])[0]])
        if rank == 4:
            alt_forms.append(tuple(tuple(row) for row in G))
    alt_forms.sort()
    GWRONG = next(G for G in alt_forms
                  if G != tuple(tuple(r) for r in GJI))

    def hbwrong(a, b):
        return sum(a[i] * GWRONG[i][j] * b[j]
                   for i in range(4) for j in range(4)) % 2

    n_nonconst = 0
    for v in P15:
        for w in P15:
            if w == v:
                continue
            vals = set()
            for r in FIBER[v]:
                for s in FIBER[w]:
                    rho_s = tuple(
                        (a + b) % 2
                        for a, b in zip(ROOT_RHO[r], ROOT_RHO[s]))
                    vals.add((Q2[rho_s]
                              + hbwrong(BITS[v], BITS[XLAB[s]])
                              + hbwrong(BITS[w], BITS[XLAB[r]])) % 2)
            if len(vals) > 1:
                n_nonconst += 1
    check("C2 CONTROL FIRES: 28 nondegenerate alternating forms on "
          "F2^4 (1 canonical + 27 wrong); the first wrong form leaves "
          "a NON-CONSTANT residual on %d / 210 ordered class pairs -- "
          "no constant C' can repair it" % n_nonconst,
          len(alt_forms) == 28 and n_nonconst > 0)

    va, vb = P15[0], P15[1]
    scram_tag = dict(root_label)
    for r in sorted(FIBER[va])[:8]:
        scram_tag[r] = vb
    for r in sorted(FIBER[vb])[:8]:
        scram_tag[r] = va
    n_frame_bad = 0
    n_pred_bad = 0
    for r in ROOTS:
        v = scram_tag[r]
        for s in ROOTS:
            w = scram_tag[s]
            if v == w and abs(ip(r, s)) == 2:
                n_frame_bad += 1
            if v != w:
                rho_s = tuple((a + b) % 2
                              for a, b in zip(ROOT_RHO[r], ROOT_RHO[s]))
                bit = (CMAT[(v, w)] + HB[(XLAB[s], v)]
                       + HB[(XLAB[r], w)]) % 2
                if bit != Q2[rho_s]:
                    n_pred_bad += 1
    check("C3 CONTROL FIRES: scrambling the class ASSIGNMENT (8 roots "
          "exchanged between the first two fibers) breaks the frame "
          "law on %d same-tag pairs (|<,>| = 2 inside a 'class') and "
          "the x-form on %d cross-tag pairs"
          % (n_frame_bad, n_pred_bad),
          n_frame_bad > 0 and n_pred_bad > 0)

    # -------------------------------------------------------- verdict
    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    core_ok = all(ok for nm, ok in CHECKS if not nm.startswith("C"))
    ctrl_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    print("%d/%d checks passed" % (n_pass, n_all))
    print("frozen rule SHA-256: %s" % RULE_SHA)
    if not ctrl_ok:
        verdict = "TEST-VOID"
    elif not core_ok:
        verdict = "TRANSITION-BUS-DEAD"
    elif obstruction:
        verdict = "TRANSITION-BUS-TORSOR"
    else:
        verdict = "TRANSITION-BUS-CANONICAL"
    print("VERDICT: %s" % verdict)
    if verdict == "TRANSITION-BUS-TORSOR":
        print("""
EXACT FREEDOM (stated precisely):
  * pair level (r ~ -r): each class fiber is a canonical TORSOR under
    v_perp (8 states, affine, level-2 certified) -- freedom = one
    basepoint per class, 15 independent v_perp-torsor choices;
  * root level: additionally one sign per pair (2^120), NOT reducible:
    -1 is invisible at every mod-(1+i)^2 level and J is a 4-cycle on
    fibers, so no V-valued state label is deck-equivariant (T1d);
  * level 3: see T1e branch above (G_v-torsor if coset held).
  The predicate itself is GAUGE-FREE on canonical data: |<r,r'>| is a
  function of (rho, rho') alone via q(rho + rho'); the (x, v)-form
  holds for every basepoint choice with C(v,v') = q(rho_v + rho_v').
ROOTCLASS-MIXED (v775) unaffected: no matter assignment made here.""")
    print("runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return (0 if n_pass == n_all else 1), verdict


def run():
    """run_all entry point (v757 precedent): expected pattern 35/35 with
    verdict TRANSITION-BUS-TORSOR (CANONICAL, DEAD or TEST-VOID breaks
    the suite)."""
    rc, verdict = main()
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    ok = (rc == 0 and n_pass == n_all == 35
          and verdict == "TRANSITION-BUS-TORSOR")
    print("\n[%s] PATTERN GATE: expected 35/35 TRANSITION-BUS-TORSOR; got "
          "%d/%d %s" % ("PASS" if ok else "FAIL", n_pass, n_all, verdict))
    print("\nADJUDICATION: %s -- TRANSITION-BUS-TORSOR: each of the 15 "
          "Gaussian class fibers of R(E8) is a canonical v_perp pair-"
          "torsor (coset rho_v + iota(v_perp) in L/2L, all 15 classes); "
          "the frozen predicate P reproduces all 57600 ordered inner "
          "products exactly (x-form on all 53760 cross-class pairs, sign "
          "law on all 14400 keys); the T1d obstruction (J cycle type "
          "4+4+4+4, -1 free on roots / trivial on V x (V\\{0})) rules out "
          "a canonical strict 16-state labeling; A15 comparison "
          "quantified (13440 vs 26880 cross pairs, Gram rank 15 vs 8); "
          "all three controls fire.  ROOTCLASS-MIXED (v775) unaffected.  "
          "NO RH claim." % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
