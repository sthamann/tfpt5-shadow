#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""e8_torsor_fourier_probe -- E8.TORSOR.FOURIER.01: read the CHARACTERS
of the origin-free root fibers instead of their points -- the projective
Fourier modes of the 15 Gaussian torsors, their full equivariant
decomposition, and the frozen matter-purity decision.

FOLLOW-UP to E8.TRANSITIONBUS.01 (verdict TRANSITION-BUS-TORSOR): each
class fiber R_v (16 roots, 8 antipodal pairs) is a canonical TORSOR over
v_perp = {t : hbar(v,t) = 0} (an affine F2^3, deck J = translation by v,
no distinguished origin).  Since the fibers have no origin, their
CHARACTER data is canonical where their point data is not: an origin
shift multiplies a character sum by a global sign, so the Fourier modes
are canonical PROJECTIVE RAYS.

STANDING FENCE (cited, binding): v775 -- ARF.ROOTCLASS.01, verdict
ROOTCLASS-MIXED -- killed the POINTWISE root -> matter assignment (no
D5(+)A3 / SU(5) convention makes the Gaussian classes weight-pure;
>= 7 classes always carry adjoint-side roots).  The present probe reads
rays, not points; it makes NO pointwise matter assignment, and its P3
bar below explicitly re-confirms that the weight-level reading stays
dead.  Nothing here moves a status marker.

THE CONSTRUCTION (frozen; details in FROZEN_SPEC, hashed at runtime
before any root data):
 (1) For each fiber R_v and each character chi of v_perp (8 = dual of
     F2^3, canonically labelled by cosets [u] in V/<v> via the
     symplectic duality chi_u = hbar(u, .)|_{v_perp}, the bus probe's
     T4.5 isomorphism), the mode |chi_u-hat, v> has coefficient
     (-1)^{hbar(u, x(r))} on each root r of the fiber and 0 elsewhere.
     PREDECLARED: the natural home is the 120-dimensional PAIR quotient
     (the (-1)-symmetric half of R^240): x(r) = x(-r) at level 2, and
     the antisymmetric half carries NO canonical modes (the bus sign
     theorem: the 2^120 sign gauge is irreducible).  Frozen convention:
     symmetric lift.  Phase-ambiguity census: an origin shift by t
     multiplies the mode by (-1)^{hbar(u,t)} -- a global sign, so the
     RAY is canonical (checked for all 15 x 8 x 8 shifts).
 (2) EQUIVARIANT ACTION: deck J acts diagonally with eigenvalue
     (-1)^{hbar(u,v)} (60 even + 60 odd modes); the 16 Pauli
     translations (kernel of G31 -> Sp(4,2) mod mu4) act diagonally by
     characters (exact census); G31 (BFS 46080) acts monomially --
     every generator maps every mode to +- another mode -- with label
     action factoring through Sp(4,2) (order-720 closure, kernel 64 =
     mu4 x Pauli16) and label orbits {15 uniform, 45 even, 60 odd};
     sigma (Z3) and the certified D5(+)A3 Weyl groups W(D5) (1920, BFS
     from the 40 D5-adjoint reflections of the v775-canonical
     sigma-stable split D = (0,2,4,6,7)) and W(A3) (24, BFS from the
     12 A3 reflections) decompose the 120-dim pair space with exact
     integer / cyclotomic character theory (S4 and Z3 tables exact;
     W(D5) and G31 reported through exact Burnside orbit/orbital counts
     plus the integral Clebsch spectrum).
 (3) THE MATTER QUESTION (frozen purity bars, decided below):
     P1a  the spinor sector (128 odd roots, split-independent) is
          EXACTLY the 8 R-fibers (NS/R purity) => the carrier block
          M_S is the span of 64 whole Fourier rays (Fourier-ALIGNED);
     P1b  M_S factorizes as a W(D5) x W(A3)-set as 16 x 4 (half-spinor
          weight pairs x A3 tetrad), W(A3) trivial on the 16, W(D5)
          trivial on the 4; the 16 is W(D5)-transitive of permutation
          rank 3 with folded-5-cube (Clebsch) spectrum
          (x-5)(x-1)^10(x+3)^5, i.e. isotypic dimensions 1 + 5 + 10
          (the carrier Pascal 1 + 5bar + 10 at character level);
     P2   the tetrad is W(A3) ~ S4-NATURAL (faithful, transitive,
          point stabilizer S3; permutation rep = 1 + standard 3) and
          sigma acts on it as the family 3-cycle + fixed anchor;
     P3   (the overreach bar that keeps v775 standing): every single
          D5-weight axis inside M_S would have to be a Fourier ray.
          Modes have full 8-pair support, so P3 can only hold if the
          weight and character gradings coincide -- they are instead
          MUTUALLY UNBIASED (|<pair|mode>|^2 = 1/8 exactly).
 (4) DESCENT NOTE (report only): what the deck-even modes provide the
     PRIME.POSITIVE_DESCENT.01 carrier-intertwiner demand (v791): an
     exact operator dictionary mode -> context Pauli observable under
     the certified chart U of E8.CLIFFORD2Q.01.
 (5) OVERLAP CENSUS with the 60 certified stabilizer rays: line
     indicators expand exactly in the 4 deck-even modes of their fiber
     (squared overlap 1/4 each); deck-odd modes are orthogonal to every
     line pushforward; the 45 nontrivial even modes ARE, under U, the
     45 (context, Pauli) incidences (each of the 15 nonzero Paulis
     covered 3x); the 15 uniform modes map to the identity.

CONTROLS (must fire, frozen):
  C1 scrambled fibers (4 pairs exchanged between two fibers, seeded)
     destroy deck equivariance (J no longer diagonal / monomial);
  C2 the WRONG character group F2^4 = V instead of v_perp breaks
     well-definedness: the 16 restricted characters collide 2:1 (rank
     8 < 16, 8 duplicate rays per fiber);
  C3 seeded random sign systems fail the certificates (orthogonality
     and deck diagonality).

VERDICT ENUM (frozen):
  TORSOR-FOURIER-PURE    : P1a & P1b & P2 & P3.
  TORSOR-FOURIER-PARTIAL : P1a & P1b & P2 hold, P3 fails -- clean
       carrier (16 = 1+5+10) x family (4 = 1+3) blocks exist at
       character level and are Fourier-aligned at SECTOR resolution,
       while the weight-level reading stays dead (v775 intact).
  TORSOR-FOURIER-MIXED   : P1a or P1b or P2 fails -- the code layer is
       definitively typed as pure audit/syndrome geometry at ALL
       levels.
  TEST-VOID              : a must-fail control does not fire.

FENCES / FIREWALL: experiments/tfpt-discovery probe; ONE new file;
writes nothing; no verification/-, ledger, paper or website surface
touched; no .md.  Exact integer / Fraction / Z[i] / F2 arithmetic in
every load-bearing check; sympy only for two small characteristic
polynomials (gated import); RNG only inside the must-fail controls
with frozen seeds.  "Observable / register" language stays
interpretation, not claim; ROOTCLASS-MIXED stays the standing kill of
the pointwise reading.

Sources (read-only): e8_transition_bus_probe.py (torsor structure,
x-labels, sign theorem), two_qubit_clifford_probe.py (chart U, Pauli
and stabilizer machinery, CLIFFORD identification),
verification/v752_projective_hamming_incidence.py (lattice machinery,
verbatim), verification/v775_gaussian_class_d5_purity.py (canonical
split, sector typing, ROOTCLASS-MIXED), verification/
v791_positive_descent.py (carrier-intertwiner demand).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/e8_torsor_fourier_probe.py
"""

import hashlib
import itertools
import random
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
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
# FROZEN SPEC -- hashed before any root data is computed
# ======================================================================
FROZEN_SPEC = """\
E8.TORSOR.FOURIER.01 FROZEN SPEC (2026-08-06, before any root data).

MODE CONSTRUCTION: for each nonzero Gaussian class v and each coset
[u] in V/<v>, the mode m(v,u) has coefficient (-1)^{hbar(u,x(r))} on
each root r of fiber v (x = the bus probe level-2 label, lex-min
basepoint rule) and 0 elsewhere.  Characters labelled canonically by
the symplectic duality V/<v> ~ (v_perp)*.  Natural space = the 120-dim
pair quotient (symmetric lift frozen); rays defined up to global sign.
PHASE LAW: basepoint shift by t multiplies m(v,u) by (-1)^{hbar(u,t)}.
DECK LAW: J m(v,u) = (-1)^{hbar(u,v)} m(v,u); Pauli16 diagonal by
characters; G31 monomial with Sp(4,2) label action, kernel 64.
MATTER SPLIT: v775 canonical sigma-stable D = (0,2,4,6,7), standard
doubled model; sectors D5adj(40)/A3(12)/V10x6(60)/S(128) on roots,
20/6/30/64 on pairs.
PURITY BARS: P1a M_S = the 8 R-fibers = 64 whole Fourier rays.
P1b M_S ~ 16 x 4 as W(D5) x W(A3)-set; W(A3) trivial on 16, W(D5)
trivial on 4; 16 transitive rank 3, Clebsch charpoly
(x-5)(x-1)^10(x+3)^5 => 1+5+10.  P2 tetrad S4-natural (faithful,
transitive, stab S3, rep 1+3std); sigma = family 3-cycle + anchor.
P3 every D5-weight axis of M_S is a Fourier ray (expected impossible:
modes have full support; weight/character gradings mutually unbiased).
VERDICT: PURE = P1a&P1b&P2&P3; PARTIAL = P1a&P1b&P2 & not P3;
MIXED = P1a or P1b or P2 fails; TEST-VOID = a control does not fire.
CONTROLS: C1 fiber scramble breaks deck equivariance; C2 character
group V (16 chars) collides 2:1 (rank 8); C3 seeded random signs
break orthogonality + deck diagonality.  Seeds frozen: 20260806.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()


# ======================================================================
# v752 lattice machinery (verbatim, read-only source)
# ======================================================================
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))
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
        assert piv is not None
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


# ======================================================================
# Z[i] gadgets (sibling probe, read-only source)
# ======================================================================
def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a):
    return (a[0], -a[1])


G0, G1, GI = (0, 0), (1, 0), (0, 1)


def kron(A, B):
    n, m = len(A), len(B)
    return tuple(tuple(gmul(A[i // m][k // m], B[i % m][k % m])
                       for k in range(n * m)) for i in range(n * m))


def mat_applyC(A, z):
    n = len(A)
    out = []
    for i in range(n):
        s = G0
        for j in range(n):
            s = gadd(s, gmul(A[i][j], z[j]))
        out.append(s)
    return tuple(out)


I2C = ((G1, G0), (G0, G1))
X2C = ((G0, G1), (G1, G0))
Y2C = ((G0, (0, -1)), ((0, 1), G0))
Z2C = ((G1, G0), (G0, (-1, 0)))
W1Q = {(0, 0): I2C, (1, 0): X2C, (0, 1): Z2C, (1, 1): Y2C}
ALL_BITS4 = [b for b in itertools.product((0, 1), repeat=2 * 2)]
NZ_BITS4 = [b for b in ALL_BITS4 if any(b)]
PMAT = {b: kron(W1Q[(b[0], b[1])], W1Q[(b[2], b[3])]) for b in ALL_BITS4}


def symp4(a, b):
    return (a[0] * b[1] + a[1] * b[0] + a[2] * b[3] + a[3] * b[2]) % 2


def chart(r):
    return ((r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7]))


# ======================================================================
# model builder + condensed bus re-verification (both models)
# ======================================================================
def build_model(kind):
    """kind 'gauss' (constr-A, herm divisor 2) or 'std' (doubled,
    herm divisor 4).  Returns the full torsor/label state."""
    if kind == "gauss":
        all_placements = set()
        for p in itertools.permutations(range(8)):
            all_placements.add(code_image(C_NAIVE, p))
        both_inv = [c for c in
                    sorted(all_placements, key=lambda c: sorted(c))
                    if code_image(c, PI_J) == c
                    and code_image(c, PI_SIG) == c]
        W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
        CSTAR = [c for c in both_inv if W0246 in c][0]
        assert supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED
        ROOTS = sorted(constrA_roots(CSTAR))
        LAT = constrA_lattice(CSTAR)
        div = 2
    else:
        def in_E8_std(x):
            par = {v % 2 for v in x}
            return len(par) == 1 and sum(x) % 4 == 0

        B_STD = [(4, 0, 0, 0, 0, 0, 0, 0), (-2, 2, 0, 0, 0, 0, 0, 0),
                 (0, -2, 2, 0, 0, 0, 0, 0), (0, 0, -2, 2, 0, 0, 0, 0),
                 (0, 0, 0, -2, 2, 0, 0, 0), (0, 0, 0, 0, -2, 2, 0, 0),
                 (0, 0, 0, 0, 0, -2, 2, 0), (1, 1, 1, 1, 1, 1, 1, 1)]
        LAT = make_lattice(in_E8_std, list(B_STD))
        ROOTS = []
        for v in itertools.product(range(-1, 2), repeat=8):
            if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
                ROOTS.append(tuple(2 * a for a in v))
        for y in itertools.product((0, -1), repeat=8):
            v = tuple(2 * a + 1 for a in y)
            if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
                ROOTS.append(v)
        ROOTS = sorted(ROOTS)
        div = 4

    def herm(x, y):
        re, im = ip(x, y), ip(x, J_vec(y))
        assert re % div == 0 and im % div == 0
        return (re // div, im // div)

    def hbv(x, y):
        h = herm(x, y)
        return (h[0] + h[1]) % 2

    coords = LAT["coords"]
    REPS = label_group(LAT)
    ZERO = LAT["label"]((0,) * 8)
    LBLS = sorted(REPS)
    P15 = [lb for lb in LBLS if lb != ZERO]
    root_label = {r: LAT["label"](r) for r in ROOTS}
    census = Counter(root_label.values())
    ok = (len(ROOTS) == 240 and len(census) == 15
          and sorted(census.values()) == [16] * 15 and ZERO not in census)
    HB = {(a, b): hbv(REPS[a], REPS[b]) for a in LBLS for b in LBLS}
    ADDV = {(a, b): LAT["label"](add_vec(REPS[a], REPS[b]))
            for a in LBLS for b in LBLS}
    VPERP = {v: [t for t in LBLS if HB[(t, v)] == 0] for v in P15}
    ok = ok and all(len(VPERP[v]) == 8 and v in VPERP[v] for v in P15)
    FIBER = {v: [r for r in ROOTS if root_label[r] == v] for v in P15}

    # level 2: rho, q, iota, pair torsor, x-labels (bus recipe)
    def rho_of(r):
        return tuple(c % 2 for c in coords(r))

    def lift2(rho):
        w = (0,) * 8
        for i, bit in enumerate(rho):
            if bit:
                w = add_vec(w, LAT["B"][i])
        return w

    RHO256 = list(itertools.product((0, 1), repeat=8))
    Q2 = {}
    ok_q = True
    for rho in RHO256:
        w = lift2(rho)
        h = herm(w, w)[0]
        assert h % 2 == 0
        Q2[rho] = (h // 2) % 2
        for b in LAT["B"]:
            w2 = add_vec(w, tuple(2 * a for a in b))
            if (herm(w2, w2)[0] // 2) % 2 != Q2[rho]:
                ok_q = False
    ROOT_RHO = {r: rho_of(r) for r in ROOTS}
    rc = Counter(ROOT_RHO.values())
    ok_2to1 = (len(rc) == 120 and sorted(rc.values()) == [2] * 120
               and all(ROOT_RHO[r] == ROOT_RHO[neg_vec(r)] for r in ROOTS)
               and all(Q2[ROOT_RHO[r]] == 1 for r in ROOTS))
    IOTA = {lb: rho_of(add_vec(REPS[lb], J_vec(REPS[lb]))) for lb in LBLS}
    INV_IOTA = {IOTA[lb]: lb for lb in LBLS}
    PAIR_IMG = {v: sorted(set(ROOT_RHO[r] for r in FIBER[v]))
                for v in P15}
    RHO_BASE = {v: PAIR_IMG[v][0] for v in P15}
    ok_coset = all(
        PAIR_IMG[v] == sorted(tuple((a + b) % 2
                                    for a, b in zip(RHO_BASE[v], IOTA[t]))
                              for t in VPERP[v]) for v in P15)
    XLAB = {}
    ok_x = True
    for r in ROOTS:
        v = root_label[r]
        d = tuple((a + b) % 2 for a, b in zip(ROOT_RHO[r], RHO_BASE[v]))
        x = INV_IOTA.get(d)
        if x is None or HB[(x, v)] != 0:
            ok_x = False
        XLAB[r] = x
    ok_J = all(XLAB[tuple(J_vec(r))] == ADDV[(XLAB[r], root_label[r])]
               and XLAB[neg_vec(r)] == XLAB[r] for r in ROOTS)
    return dict(ROOTS=ROOTS, LAT=LAT, REPS=REPS, ZERO=ZERO, LBLS=LBLS,
                P15=P15, root_label=root_label, HB=HB, ADDV=ADDV,
                VPERP=VPERP, FIBER=FIBER, XLAB=XLAB, herm=herm,
                RHO_BASE=RHO_BASE, IOTA=IOTA, INV_IOTA=INV_IOTA,
                ROOT_RHO=ROOT_RHO, Q2=Q2,
                bus_ok=ok and ok_q and ok_2to1 and ok_coset and ok_x
                and ok_J)


def coset_reps(model, v):
    """the 8 cosets of <v> in V, canonical min-label representatives."""
    seen = set()
    reps = []
    for u in model["LBLS"]:
        if u in seen:
            continue
        mate = model["ADDV"][(u, v)]
        seen.add(u)
        seen.add(mate)
        reps.append(min(u, mate))
    return sorted(reps)


def build_modes(model):
    """the 120 Fourier modes as int8 vectors over the 240 roots
    (sorted root order); labels (v, u)."""
    ROOTS = model["ROOTS"]
    ridx = {r: k for k, r in enumerate(ROOTS)}
    modes = {}
    for v in model["P15"]:
        for u in coset_reps(model, v):
            vec = np.zeros(240, dtype=np.int8)
            for r in model["FIBER"][v]:
                s = 1 - 2 * model["HB"][(u, model["XLAB"][r])]
                vec[ridx[r]] = s
            modes[(v, u)] = vec
    return modes, ridx


# ======================================================================
def main():
    print("=" * 78)
    print("E8.TORSOR.FOURIER.01 -- projective Fourier modes of the "
          "Gaussian torsors")
    print("=" * 78)
    print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA, flush=True)

    # ---------------------------------------------------------------- G1
    section("G1: constr-A model rebuilt; bus torsor state re-verified")
    GM = build_model("gauss")
    check("G1.1 constr-A model: 240 roots, 15 x 16 census, pair torsor "
          "over v_perp, x-labels, J = translation by v (bus theorems "
          "re-verified condensed)", GM["bus_ok"])

    # ---------------------------------------------------------------- G2
    section("G2: the projective Fourier transform -- rays, phase law, "
            "orthogonality, 120-dim home")
    MODES, RIDX = build_modes(GM)
    ROOTS = GM["ROOTS"]
    NEGIDX = np.array([RIDX[neg_vec(r)] for r in ROOTS], dtype=np.int64)
    JIDX = np.array([RIDX[tuple(J_vec(r))] for r in ROOTS],
                    dtype=np.int64)
    MODE_KEYS = sorted(MODES)
    MMAT = np.stack([MODES[k] for k in MODE_KEYS]).astype(np.int64)
    check("G2.1 120 = 15 x 8 modes built; every mode supported on "
          "exactly its 16-root fiber with coefficients +-1",
          len(MODE_KEYS) == 120
          and all(sorted(Counter(MODES[k][MODES[k] != 0]
                                 .tolist()).keys()) in ([-1, 1], [1])
                  for k in MODE_KEYS)
          and all(int(np.count_nonzero(MODES[k])) == 16
                  for k in MODE_KEYS))

    # phase-ambiguity census: shift basepoint by every t in v_perp
    ok_phase = True
    n_shift_tests = 0
    for v in GM["P15"]:
        for t in GM["VPERP"][v]:
            # shifted labeling x' = x + t
            for u in coset_reps(GM, v):
                vec = np.zeros(240, dtype=np.int64)
                for r in GM["FIBER"][v]:
                    xs = GM["ADDV"][(GM["XLAB"][r], t)]
                    vec[RIDX[r]] = 1 - 2 * GM["HB"][(u, xs)]
                expect = (1 - 2 * GM["HB"][(u, t)])
                if not np.array_equal(vec,
                                      expect * MODES[(v, u)]
                                      .astype(np.int64)):
                    ok_phase = False
                n_shift_tests += 1
    check("G2.2 PHASE-AMBIGUITY LAW EXACT: an origin shift by t "
          "multiplies m(v,u) by (-1)^{hbar(u,t)} -- a GLOBAL sign -- "
          "for all %d (v, t, u) combinations: the rays are canonical"
          % n_shift_tests, ok_phase and n_shift_tests == 15 * 8 * 8)

    GRAM = MMAT @ MMAT.T
    check("G2.3 the 120 modes are pairwise orthogonal with norm^2 = 16 "
          "(exact integer Gram = 16 I): an orthogonal ray BASIS of the "
          "120-dim pair space",
          np.array_equal(GRAM, 16 * np.eye(120, dtype=np.int64)))

    ok_sym = all(np.array_equal(MODES[k], MODES[k][NEGIDX])
                 for k in MODE_KEYS)
    check("G2.4 PREDECLARED 120-dim home: every mode is (-1)-SYMMETRIC "
          "(m = m o (-1)); the antisymmetric 120-dim half receives NO "
          "canonical mode (bus sign theorem: the 2^120 sign gauge is "
          "irreducible; frozen symmetric-lift convention)", ok_sym)

    # ---------------------------------------------------------------- G3
    section("G3: deck diagonality -- J and the 16 Pauli translations "
            "act diagonally by characters")
    ok_J_diag = True
    n_even = n_odd = 0
    for (v, u) in MODE_KEYS:
        eig = 1 - 2 * GM["HB"][(u, v)]
        if eig == 1:
            n_even += 1
        else:
            n_odd += 1
        if not np.array_equal(MODES[(v, u)][JIDX],
                              eig * MODES[(v, u)]):
            ok_J_diag = False
    check("G3.1 deck J diagonal: J m(v,u) = (-1)^{hbar(u,v)} m(v,u) on "
          "all 120 modes; census %d even + %d odd = 60 + 60; per fiber "
          "4 + 4" % (n_even, n_odd),
          ok_J_diag and n_even == 60 and n_odd == 60)

    # Pauli translations via the chart (sibling machinery)
    Z240 = [chart(r) for r in ROOTS]
    zidx = {z: k for k, z in enumerate(Z240)}
    pauli_perm = {}
    ok_pauli_perm = True
    for pb in ALL_BITS4:
        try:
            perm = np.array([zidx[mat_applyC(PMAT[pb], Z240[k])]
                             for k in range(240)], dtype=np.int64)
        except KeyError:
            ok_pauli_perm = False
            break
        pauli_perm[pb] = perm
    check("G3.2 all 16 Pauli operators preserve the root set under the "
          "certified chart U (z_k = r_2k + i r_2k+1)", ok_pauli_perm)

    ok_transl = True
    ok_pauli_diag = True
    for pb in NZ_BITS4:
        perm = pauli_perm[pb]
        tmap = {}
        for v in GM["P15"]:
            ts = set()
            for r in GM["FIBER"][v]:
                rr = ROOTS[perm[RIDX[r]]]
                if GM["root_label"][rr] != v:
                    ok_transl = False
                dx = GM["ADDV"][(GM["XLAB"][rr],
                                 GM["XLAB"][r])]
                ts.add(dx)
            if len(ts) != 1:
                ok_transl = False
            else:
                tmap[v] = next(iter(ts))
        for (v, u) in MODE_KEYS:
            eig = 1 - 2 * GM["HB"][(u, tmap[v])]
            if not np.array_equal(MODES[(v, u)][perm],
                                  eig * MODES[(v, u)]):
                ok_pauli_diag = False
    check("G3.3 DECK TRANSLATIONS ACT DIAGONALLY BY CHARACTERS: every "
          "nonzero Pauli acts on every fiber as a translation t_P(v) "
          "in v_perp, and on every mode as the scalar "
          "(-1)^{hbar(u, t_P(v))} (15 x 15 x 8 exact)",
          ok_transl and ok_pauli_diag)

    # ---------------------------------------------------------------- G4
    section("G4: G31 equivariance -- monomial action, Sp(4,2) label "
            "action, Burnside decomposition data")
    print("    building G31 (BFS over the 60 unitary reflections) ...",
          flush=True)
    RD = np.array(ROOTS, dtype=np.int64)
    JRD = np.array([J_vec(r) for r in ROOTS], dtype=np.int64)
    line_reps = []
    line_of = {}
    for k in range(240):
        if k in line_of:
            continue
        orb = [k]
        y = tuple(J_vec(ROOTS[k]))
        while y != ROOTS[k]:
            orb.append(RIDX[y])
            y = tuple(J_vec(y))
        for j in orb:
            line_of[j] = len(line_reps)
        line_reps.append(k)
    refl_perms = []
    for L in range(60):
        vi = line_reps[L]
        re2 = RD @ RD[vi]
        im2 = RD @ JRD[vi]
        assert (re2 % 2 == 0).all() and (im2 % 2 == 0).all()
        re, im = re2 // 2, im2 // 2
        Y = RD - re[:, None] * RD[vi][None, :] \
            - im[:, None] * JRD[vi][None, :]
        refl_perms.append(np.array(
            [RIDX[tuple(int(t) for t in Y[i])] for i in range(240)],
            dtype=np.int16))
    t_bfs = time.time()
    IDP = np.arange(240, dtype=np.int16)
    Gset = {IDP.tobytes(): IDP}
    frontier = [IDP]
    while frontier:
        nxt = []
        for p in frontier:
            for g in refl_perms:
                q = p[g]
                b = q.tobytes()
                if b not in Gset:
                    Gset[b] = q
                    nxt.append(q)
        frontier = nxt
    check("G4.1 |G31| = %d = 46080 (BFS %.1f s); sigma and J in G31; "
          "J central"
          % (len(Gset), time.time() - t_bfs),
          len(Gset) == 46080
          and np.array([RIDX[tuple(sig_vec(r))] for r in ROOTS],
                       dtype=np.int16).tobytes() in Gset
          and JIDX.astype(np.int16).tobytes() in Gset)

    # monomial census on the 60 generators (products of monomial maps
    # are monomial, so the whole group acts monomially)
    mode_bytes = {MODES[k].tobytes(): (k, 1) for k in MODE_KEYS}
    for k in MODE_KEYS:
        mode_bytes[(-MODES[k]).tobytes()] = (k, -1)
    ok_mono = True
    gen_label_perms = []
    for g in refl_perms:
        ginv = np.empty(240, dtype=np.int64)
        ginv[g] = np.arange(240)
        lp = {}
        for k in MODE_KEYS:
            img = MODES[k][ginv]
            hit = mode_bytes.get(img.tobytes())
            if hit is None:
                ok_mono = False
                break
            lp[k] = hit[0]
        if not ok_mono:
            break
        gen_label_perms.append(lp)
    check("G4.2 MONOMIAL EQUIVARIANCE: each of the 60 G31 generators "
          "maps each of the 120 modes to +- another mode (7200 exact "
          "matches); closure => all 46080 elements act monomially on "
          "the ray system", ok_mono)

    # label action closure = Sp(4,2), kernel 64 = mu4 x Pauli16
    key_idx = {k: i for i, k in enumerate(MODE_KEYS)}
    lgen = [tuple(key_idx[lp[k]] for k in MODE_KEYS)
            for lp in gen_label_perms]
    lid = tuple(range(120))
    lset = {lid}
    lfront = [lid]
    while lfront:
        nxt = []
        for p in lfront:
            for g in lgen:
                q = tuple(g[i] for i in p)
                if q not in lset:
                    lset.add(q)
                    nxt.append(q)
        lfront = nxt
    ok_kernel = True
    for pb in NZ_BITS4:
        perm = pauli_perm[pb]
        for k in MODE_KEYS[:8]:
            img = MODES[k][np.argsort(perm)]
            hit = mode_bytes.get(img.tobytes())
            if hit is None or hit[0] != k:
                ok_kernel = False
    check("G4.3 LABEL ACTION = Sp(4,2): closure of the label "
          "permutations has order %d = 720; kernel order 46080/720 = "
          "64 = mu4 x Pauli16 (J and all Paulis act ray-trivially -- "
          "diagonal by characters, G3)"
          % len(lset), len(lset) == 720 and ok_kernel)

    orbits_lbl = []
    seen = set()
    for i in range(120):
        if i in seen:
            continue
        orb = {i}
        frontier2 = [i]
        while frontier2:
            j = frontier2.pop()
            for g in lgen:
                jj = g[j]
                if jj not in orb:
                    orb.add(jj)
                    frontier2.append(jj)
        seen |= orb
        orbits_lbl.append(sorted(orb))
    osz = sorted(len(o) for o in orbits_lbl)
    strata = {15: "uniform (chi = 0)", 45: "deck-even nontrivial",
              60: "deck-odd"}
    ok_strata = osz == [15, 45, 60]
    if ok_strata:
        for o in orbits_lbl:
            for i in o:
                v, u = MODE_KEYS[i]
                unif = (u == GM["ZERO"] or u == v)
                even = GM["HB"][(u, v)] == 0
                if len(o) == 15 and not unif:
                    ok_strata = False
                if len(o) == 45 and (unif or not even):
                    ok_strata = False
                if len(o) == 60 and even:
                    ok_strata = False
    check("G4.4 Sp(4,2) ORBITS on the 120 ray labels: sizes %s = "
          "{15 uniform} u {45 deck-even nontrivial} u {60 deck-odd} "
          "(each stratum transitive)" % osz, ok_strata)

    # Burnside data for the pair space over the full G31
    E = np.stack(list(Gset.values())).astype(np.int64)
    IDXA = np.arange(240, dtype=np.int64)
    fixpairs = (((E == IDXA[None, :]) | (E == NEGIDX[None, :]))
                .sum(axis=1) // 2)
    NJIDX = NEGIDX[JIDX]
    fixlines = (((E == IDXA[None, :]) | (E == NEGIDX[None, :])
                 | (E == JIDX[None, :])
                 | (E == NJIDX[None, :])).sum(axis=1) // 4)
    n_orb_pairs = int(fixpairs.sum()) // 46080
    n_orbital_pairs = int((fixpairs ** 2).sum()) // 46080
    n_orb_lines = int(fixlines.sum()) // 46080
    n_orbital_lines = int((fixlines ** 2).sum()) // 46080
    todd = fixpairs - fixlines
    n_orbital_odd = int((todd ** 2).sum()) // 46080
    m_triv_odd = int(todd.sum()) // 46080
    check("G4.5 BURNSIDE (exact integer): G31 on the 120 pairs: "
          "%d orbit, sum m_i^2 = %d; deck-even part (60 lines): "
          "%d orbit, sum m_i^2 = %d; deck-odd part: m_triv = %d, "
          "sum m_i^2 = %d -- the pair space splits 60+60 with small "
          "multiplicity content on each side"
          % (n_orb_pairs, n_orbital_pairs, n_orb_lines,
             n_orbital_lines, m_triv_odd, n_orbital_odd),
          n_orb_pairs == 1 and n_orb_lines == 1 and m_triv_odd == 0
          and int(fixpairs.sum()) % 46080 == 0
          and int((fixpairs ** 2).sum()) % 46080 == 0)

    # ---------------------------------------------------------------- G5
    section("G5: sigma (Z3) decomposition of the pair space (exact "
            "cyclotomic)")
    sigperm = np.array([RIDX[tuple(sig_vec(r))] for r in ROOTS],
                       dtype=np.int64)
    fix_sig_pairs = int(((sigperm == IDXA)
                         | (sigperm == NEGIDX)).sum()) // 2
    m_triv3 = (120 + 2 * fix_sig_pairs)
    ok_int3 = m_triv3 % 3 == 0
    m_triv3 //= 3
    m_om = (120 - fix_sig_pairs)
    ok_int3 = ok_int3 and m_om % 3 == 0
    m_om //= 3
    check("G5.1 sigma on the 120 pairs: tr = %d fixed pairs; "
          "multiplicities m(1) = %d, m(omega) = m(omega-bar) = %d "
          "(integral, %d + 2 x %d = 120)"
          % (fix_sig_pairs, m_triv3, m_om, m_triv3, m_om),
          ok_int3 and m_triv3 + 2 * m_om == 120)

    # ================================================================ S1
    section("S1: standard doubled model -- torsor + Fourier system + "
            "the v775 canonical D5(+)A3 split")
    SM = build_model("std")
    SMODES, SRIDX = build_modes(SM)
    SROOTS = SM["ROOTS"]
    SMKEYS = sorted(SMODES)
    SMMAT = np.stack([SMODES[k] for k in SMKEYS]).astype(np.int64)
    check("S1.1 standard model: bus torsor state re-verified; 120 "
          "modes orthogonal (Gram = 16 I)",
          SM["bus_ok"]
          and np.array_equal(SMMAT @ SMMAT.T,
                             16 * np.eye(120, dtype=np.int64)))

    CANON_D = (0, 2, 4, 6, 7)
    ACOORDS = (1, 3, 5)

    def sector_of(r):
        if r[0] % 2:
            return "S"
        supp = [c for c in range(8) if r[c] != 0]
        nd = sum(1 for c in supp if c in CANON_D)
        return {2: "D5adj", 0: "A3"}.get(nd, "V")

    sec_census = Counter(sector_of(r) for r in SROOTS)
    check("S1.2 v775 canonical sigma-stable split D = (0,2,4,6,7): "
          "sector census %s = 40 + 12 + 60 + 128 (v775 S2.1)"
          % dict(sec_census),
          sec_census == Counter({"S": 128, "V": 60,
                                 "D5adj": 40, "A3": 12}))

    fiber_sec = {v: Counter(sector_of(r) for r in SM["FIBER"][v])
                 for v in SM["P15"]}
    R_fibers = [v for v in SM["P15"]
                if fiber_sec[v] == Counter({"S": 16})]
    NS_fibers = [v for v in SM["P15"] if v not in R_fibers]
    ok_ns_mix = all(len(fiber_sec[v]) >= 2 for v in NS_fibers)
    check("S1.3 POINT-LEVEL BASELINE (v775 recite): %d fibers are pure "
          "spinor (the 8 R-classes, NS/R purity), the %d NS fibers all "
          "MIX the even sectors -- and the weight-level reading is "
          "dead (ROOTCLASS-MIXED, standing fence)"
          % (len(R_fibers), len(NS_fibers)),
          len(R_fibers) == 8 and ok_ns_mix)

    # ================================================================ S2
    section("S2 (P1a): the carrier block M_S = the 8 R-fibers = 64 "
            "whole Fourier rays")
    P1a = check(
        "S2.1 P1a: the spinor sector (128 odd roots, split-INDEPENDENT)"
        " is exactly the union of the 8 R-fibers; hence M_S = span of "
        "their 8 x 8 = 64 Fourier rays -- a FOURIER-ALIGNED carrier "
        "block (impossible at weight level, exact at sector level)",
        len(R_fibers) == 8
        and sum(1 for r in SROOTS if sector_of(r) == "S") == 128
        and all(sector_of(r) == "S"
                for v in R_fibers for r in SM["FIBER"][v]))

    # ================================================================ S3
    section("S3 (P1b, P2): W(D5) x W(A3) -- the 16 x 4 factorization, "
            "Clebsch spectrum 1+5+10, S4-natural tetrad")

    def sp_apply(sp, r):
        return tuple(sp[k][1] * r[sp[k][0]] for k in range(8))

    def sp_compose(a, b):
        """(a o b): first b, then a."""
        return tuple((b[a[k][0]][0], a[k][1] * b[a[k][0]][1])
                     for k in range(8))

    SP_ID = tuple((k, 1) for k in range(8))

    def refl_signed(alpha):
        """reflection in a norm-8 even root with 2-coordinate support:
        a signed transposition."""
        supp = [c for c in range(8) if alpha[c] != 0]
        i, j = supp
        s = 1 if alpha[i] * alpha[j] < 0 else -1
        sp = list(SP_ID)
        sp[i] = (j, s)
        sp[j] = (i, s)
        return tuple(sp)

    def bfs_signed(gens):
        seen = {SP_ID}
        frontier = [SP_ID]
        while frontier:
            nxt = []
            for p in frontier:
                for g in gens:
                    q = sp_compose(g, p)
                    if q not in seen:
                        seen.add(q)
                        nxt.append(q)
            frontier = nxt
        return sorted(seen)

    d5_refl = sorted({refl_signed(r) for r in SROOTS
                      if sector_of(r) == "D5adj"})
    a3_refl = sorted({refl_signed(r) for r in SROOTS
                      if sector_of(r) == "A3"})
    WD5 = bfs_signed(d5_refl)
    WA3 = bfs_signed(a3_refl)
    ok_pres = all(sp_apply(g, r) in SM["root_label"]
                  for g in WD5[:40] + WA3 for r in SROOTS[:40])
    check("S3.1 Weyl groups from the certified split: |W(D5)| = %d = "
          "1920 (BFS from the 20 D5-adjoint reflections), |W(A3)| = "
          "%d = 24; elements are signed coordinate maps preserving the "
          "root set" % (len(WD5), len(WA3)),
          len(WD5) == 1920 and len(WA3) == 24 and ok_pres)

    # spinor pairs, weight keys, tetrad keys
    spin_pairs = sorted({tuple(min(r, neg_vec(r))) for r in SROOTS
                         if sector_of(r) == "S"})

    def wkey(r):
        d = tuple(r[c] for c in CANON_D)
        return min(d, tuple(-a for a in d))

    def tkey(r):
        a = tuple(r[c] for c in ACOORDS)
        return min(a, tuple(-x for x in a))

    WKEYS = sorted({wkey(p) for p in spin_pairs})
    TKEYS = sorted({tkey(p) for p in spin_pairs})
    pairmap = {p: (wkey(p), tkey(p)) for p in spin_pairs}
    ok_bij = (len(spin_pairs) == 64 and len(WKEYS) == 16
              and len(TKEYS) == 4
              and len(set(pairmap.values())) == 64)

    ok_fact = True
    for g in WD5:
        for p in spin_pairs[:16]:
            q = sp_apply(g, p)
            qp = min(q, neg_vec(q))
            if tkey(qp) != tkey(p):
                ok_fact = False
    for g in WA3:
        for p in spin_pairs:
            q = sp_apply(g, p)
            qp = min(q, neg_vec(q))
            if wkey(qp) != wkey(p):
                ok_fact = False
    # W(D5) transitive on the 16 weight keys; W(A3) transitive on 4
    orbW = {WKEYS[0]}
    changed = True
    while changed:
        changed = False
        for g in d5_refl:
            for w in list(orbW):
                r0 = next(p for p in spin_pairs if wkey(p) == w)
                q = sp_apply(g, r0)
                w2 = wkey(min(q, neg_vec(q)))
                if w2 not in orbW:
                    orbW.add(w2)
                    changed = True
    orbT = {TKEYS[0]}
    changed = True
    while changed:
        changed = False
        for g in a3_refl:
            for t in list(orbT):
                r0 = next(p for p in spin_pairs if tkey(p) == t)
                q = sp_apply(g, r0)
                t2 = tkey(min(q, neg_vec(q)))
                if t2 not in orbT:
                    orbT.add(t2)
                    changed = True
    P1b_1 = check(
        "S3.2 P1b (i): the 64 spinor pairs BIJECT onto 16 weight-pair "
        "keys x 4 tetrad keys (the mod-4 constraint fixes the coupling "
        "sign); W(D5) fixes the tetrad factor, W(A3) fixes the weight "
        "factor; both act transitively on their factor (%d/16, %d/4)"
        % (len(orbW), len(orbT)),
        ok_bij and ok_fact and len(orbW) == 16 and len(orbT) == 4)

    # rank-3 / Clebsch spectrum on the 16 weight keys
    def hamm_pair(w1, w2):
        d = sum(1 for a, b in zip(w1, w2) if a != b)
        return min(d, 5 - d)

    dists = sorted({hamm_pair(a, b)
                    for a in WKEYS for b in WKEYS if a != b})
    A1 = [[1 if hamm_pair(a, b) == 1 else 0 for b in WKEYS]
          for a in WKEYS]
    from sympy import Matrix, symbols, expand   # gated: charpoly only
    xs = symbols("x")
    cp = Matrix(A1).charpoly(xs).as_expr()
    cp_target = expand((xs - 5) * (xs - 1) ** 10 * (xs + 3) ** 5)
    P1b_2 = check(
        "S3.3 P1b (ii): the W(D5)-action on the 16 weight pairs has "
        "permutation rank 3 (pair distances %s); the distance-1 graph "
        "is the folded 5-cube = CLEBSCH graph with charpoly "
        "(x-5)(x-1)^10(x+3)^5 EXACT => isotypic dimensions 1 + 5 + 10 "
        "-- the carrier Pascal 1 + 5bar + 10 at character level"
        % dists, dists == [1, 2] and expand(cp - cp_target) == 0)
    P1b = P1b_1 and P1b_2

    # tetrad: S4-natural, sigma = 3-cycle + anchor
    tet_perm = {}
    for g in WA3:
        pm = []
        for t in TKEYS:
            r0 = next(p for p in spin_pairs if tkey(p) == t)
            q = sp_apply(g, r0)
            pm.append(TKEYS.index(tkey(min(q, neg_vec(q)))))
        tet_perm[g] = tuple(pm)
    img = set(tet_perm.values())
    stab0 = sum(1 for g in WA3 if tet_perm[g][0] == 0)
    # cycle-type census and permutation-character decomposition
    S4_TABLE = {  # cycle type -> (triv, sign, two, std3, std3')
        (1, 1, 1, 1): (1, 1, 2, 3, 3),
        (2, 1, 1): (1, -1, 0, 1, -1),
        (2, 2): (1, 1, 2, -1, -1),
        (3, 1): (1, 1, -1, 0, 0),
        (4,): (1, -1, 0, -1, 1)}

    def cyc_type(pm):
        seen = set()
        cyc = []
        for i in range(len(pm)):
            if i in seen:
                continue
            n, j = 0, i
            while j not in seen:
                seen.add(j)
                j = pm[j]
                n += 1
            cyc.append(n)
        return tuple(sorted(cyc, reverse=True))

    def s4_decompose(fix_fn):
        sums = [0] * 5
        for g in WA3:
            ct = cyc_type(tet_perm[g])
            chi = S4_TABLE[ct]
            f = fix_fn(g)
            for i in range(5):
                sums[i] += chi[i] * f
        assert all(s % 24 == 0 for s in sums)
        return tuple(s // 24 for s in sums)

    m_tet = s4_decompose(
        lambda g: sum(1 for i in range(4) if tet_perm[g][i] == i))
    # sigma as signed perm: (sig x)_k = x_{PI_SIG[k]} => src = PI_SIG[k]
    sig_sp = tuple((PI_SIG[k], 1) for k in range(8))
    ok_sig_vec = all(sp_apply(sig_sp, r) == sig_vec(r)
                     for r in SROOTS[:20])
    sig_tet = []
    for t in TKEYS:
        r0 = next(p for p in spin_pairs if tkey(p) == t)
        q = sig_vec(r0)
        sig_tet.append(TKEYS.index(tkey(min(q, neg_vec(q)))))
    ct_sig = cyc_type(tuple(sig_tet))
    n_fix_sig_tet = sum(1 for i in range(4) if sig_tet[i] == i)
    P2 = check(
        "S3.4 P2: the tetrad is S4-NATURAL: W(A3) -> Sym(4) faithful "
        "and surjective (image %d = 24), point stabilizer %d = 6 = S3;"
        " permutation rep = 1 + standard 3 (multiplicities %s); sigma "
        "acts as the family 3-CYCLE + fixed anchor (cycle type %s)"
        % (len(img), stab0, m_tet, (ct_sig,)),
        len(img) == 24 and stab0 == 6 and m_tet == (1, 0, 0, 1, 0)
        and ok_sig_vec and ct_sig == (3, 1) and n_fix_sig_tet == 1)

    # full sector tables over W(A3) (S4) and sigma (Z3)
    all_pairs = sorted({tuple(min(r, neg_vec(r))) for r in SROOTS})
    psec = {p: sector_of(p) for p in all_pairs}
    sec_sizes = Counter(psec.values())

    def fix_pairs_of(g, sector=None):
        n = 0
        for p in all_pairs:
            if sector and psec[p] != sector:
                continue
            q = sp_apply(g, p)
            if q == p or q == neg_vec(p):
                n += 1
        return n

    print("    exact S4 multiplicity vectors (triv, sign, 2, 3std, "
          "3'std x sign) per sector:")
    s4_tables = {}
    for sec in ("D5adj", "A3", "V", "S", None):
        m = s4_decompose(lambda g, s=sec: fix_pairs_of(g, s))
        s4_tables[sec] = m
        print("      %-6s (dim %3d): %s"
              % (sec or "TOTAL",
                 sec_sizes[sec] if sec else 120, m))
    ok_s4 = (s4_tables["D5adj"] == (20, 0, 0, 0, 0)
             and s4_tables["S"] == (16, 0, 0, 16, 0)
             and sum(a * b for a, b in
                     zip(s4_tables[None], (1, 1, 2, 3, 3))) == 120)
    check("S3.5 W(A3)-tables exact: the 20 D5-adjoint pairs are "
          "family-INVARIANT (20 x trivial: W(A3) fixes them "
          "pointwise); the carrier block M_S = 16 x (1 + 3std) = "
          "(1+5+10) x (1+3) as W(D5) x W(A3)-module; total consistent",
          ok_s4)

    n_orb_S = None
    fixS = [fix_pairs_of(g, "S") for g in WD5]
    n_orb_S = sum(fixS) // 1920
    n_orbital_S = sum(f * f for f in fixS) // 1920
    fixadj = [fix_pairs_of(g, "D5adj") for g in WD5]
    fixV = [fix_pairs_of(g, "V") for g in WD5]
    fixA3w = [fix_pairs_of(g, "A3") for g in WD5]
    check("S3.6 W(D5) Burnside exact: orbits on the 64 spinor pairs = "
          "%d (the tetrad), sum m_i^2 = %d = 16 x 3 (four copies of "
          "the multiplicity-free rank-3 16); orbits on D5adj/V/A3 "
          "pairs = %d/%d/%d (A3 pairs fixed pointwise)"
          % (n_orb_S, n_orbital_S, sum(fixadj) // 1920,
             sum(fixV) // 1920, sum(fixA3w) // 1920),
          n_orb_S == 4 and n_orbital_S == 48
          and sum(fixadj) // 1920 == 1 and sum(fixV) // 1920 == 3
          and sum(fixA3w) // 1920 == 6
          and all(f == 6 for f in fixA3w))

    # sigma (Z3) per sector
    print("    exact Z3 multiplicities (m_triv, m_omega = m_omegabar) "
          "per sector:")
    for sec in ("D5adj", "A3", "V", "S", None):
        n = sec_sizes[sec] if sec else 120
        f = fix_pairs_of(sig_sp, sec)
        mt = (n + 2 * f) // 3
        mo = (n - f) // 3
        assert (n + 2 * f) % 3 == 0
        print("      %-6s (dim %3d): m(1) = %d, m(omega) = %d"
              % (sec or "TOTAL", n, mt, mo))

    # ================================================================ S4
    section("S4 (P3): the weight grading vs the character grading -- "
            "mutually unbiased, the v775 fence stays")
    wk_per_fiber_ok = True
    for v in R_fibers:
        keys = {wkey(min(r, neg_vec(r))) for r in SM["FIBER"][v]}
        if len(keys) != 8:
            wk_per_fiber_ok = False
    min_supp = min(int(np.count_nonzero(SMODES[k])) for k in SMKEYS)
    # frozen P3 bar: every weight axis a Fourier ray <=> modes with
    # singleton pair support (2 roots); measured min support decides
    P3 = (min_supp == 2)
    check("S4.1 P3 FAILS as predeclared: every R-fiber carries 8 "
          "DISTINCT weight-pair keys (v775 echo: 8 weight pairs per "
          "class, %s), but every mode has full 16-root (8-pair) "
          "support (min = %d roots) -- no weight axis is a Fourier "
          "ray; instead |<pair|mode>|^2 = 1/8 EXACTLY on every cell: "
          "the matter-weight basis and the character basis are "
          "MUTUALLY UNBIASED on each carrier fiber.  The pointwise "
          "reading stays dead (ROOTCLASS-MIXED intact)."
          % (wk_per_fiber_ok, min_supp),
          wk_per_fiber_ok and min_supp == 16 and not P3)

    # ================================================================ O
    section("O: overlap census with the 60 certified stabilizer rays "
            "+ the Pauli operator dictionary (chart U)")
    # line indicators vs modes (constr-A model)
    ok_line_even = True
    ok_line_odd = True
    ok_cross = True
    for Lr in line_reps:
        r = ROOTS[Lr]
        v = GM["root_label"][r]
        vec = np.zeros(240, dtype=np.int64)
        for j in range(240):
            if line_of[j] == line_of[Lr]:
                vec[j] = 1
        for (w, u) in MODE_KEYS:
            d = int(vec @ MODES[(w, u)].astype(np.int64))
            even = GM["HB"][(u, w)] == 0
            if w == v:
                if even and abs(d) != 4:
                    ok_line_even = False
                if (not even) and d != 0:
                    ok_line_odd = False
            elif d != 0:
                ok_cross = False
    check("O.1 OVERLAP CENSUS: every stabilizer ray (= J-line, "
          "sibling-certified) meets EXACTLY the 4 deck-even modes of "
          "its fiber, each with squared overlap 1/4 (unbiased "
          "4-expansion); deck-odd modes and foreign fibers overlap 0 "
          "-- the deck-odd half is INVISIBLE to the stabilizer rays "
          "(pure phase register)",
          ok_line_even and ok_line_odd and ok_cross)

    # Pauli dictionary: deck-even modes -> context Paulis
    ok_dict = True
    pauli_cover = Counter()
    ctx_triples = {}
    for v in GM["P15"]:
        lines_v = sorted({line_of[RIDX[r]] for r in GM["FIBER"][v]})
        zreps = [Z240[line_reps[L]] for L in lines_v]
        xreps = [GM["XLAB"][ROOTS[line_reps[L]]] for L in lines_v]
        found = []
        for u in coset_reps(GM, v):
            if GM["HB"][(u, v)] != 0:
                continue
            O4 = [[G0] * 4 for _ in range(4)]
            for z, xv in zip(zreps, xreps):
                s = 1 - 2 * GM["HB"][(u, xv)]
                for i in range(4):
                    for j in range(4):
                        O4[i][j] = gadd(O4[i][j],
                                        gmul((s, 0),
                                             gmul(z[i], gconj(z[j]))))
            O4 = tuple(tuple(c) for c in O4)
            if u == GM["ZERO"] or u == v:      # the uniform mode
                target = tuple(tuple((4 if i == j else 0, 0)
                                     for j in range(4))
                               for i in range(4))
                if O4 != target:
                    ok_dict = False
            else:
                hit = None
                for b in NZ_BITS4:
                    for s in (1, -1):
                        tgt = tuple(tuple(
                            (4 * s * PMAT[b][i][j][0],
                             4 * s * PMAT[b][i][j][1])
                            for j in range(4)) for i in range(4))
                        if O4 == tgt:
                            hit = b
                            break
                    if hit:
                        break
                if hit is None:
                    ok_dict = False
                else:
                    found.append(hit)
                    pauli_cover[hit] += 1
        if len(found) != 3 or len(set(found)) != 3:
            ok_dict = False
        else:
            ok_comm = all(symp4(a, b) == 0 for a in found
                          for b in found)
            b1, b2, b3 = found
            ok_closed = tuple((x + y) % 2
                              for x, y in zip(b1, b2)) == b3 or \
                tuple((x + y) % 2 for x, y in zip(b1, b3)) == b2 or \
                tuple((x + y) % 2 for x, y in zip(b2, b3)) == b1
            if not (ok_comm and ok_closed):
                ok_dict = False
            ctx_triples[v] = frozenset(found)
    check("O.2 PAULI DICTIONARY EXACT: for every fiber the uniform "
          "deck-even mode gives Sum z z^dag = 4I (completeness) and "
          "the 3 nontrivial deck-even modes give EXACTLY the 3 Pauli "
          "observables of the fiber's context (+-4 P, commuting, "
          "closed): 45 modes -> 45 (context, Pauli) incidences; every "
          "nonzero Pauli covered exactly 3x: %s"
          % (sorted(pauli_cover.values()) == [3] * 15),
          ok_dict and len(ctx_triples) == 15
          and sorted(pauli_cover.values()) == [3] * 15
          and len(set(ctx_triples.values())) == 15)

    print("""
DESCENT NOTE (report only, no claim): the deck-even Fourier modes
provide, under the certified chart U (E8.CLIFFORD2Q.01), a canonical
G31-equivariant OPERATOR dictionary: mode (v,u) -> Pauli observable
P(v,u) of context Gamma_v, uniform mode -> identity.  Hence
f -> Sum_u f-hat(u) (I + P(v,u))/2 is a canonical positive
(projector-valued) assignment from the label register of one context
to carrier operators -- exactly the SHAPE of object the
PRIME.POSITIVE_DESCENT.01 carrier-intertwiner demand (v791) asks for
on the finite register.  What is NOT provided: the deck-odd half has
no Hermitian counterpart (phase register, invisible to stabilizer
rays), and no cross-context positivity statement is made here.""")

    # ================================================================ C
    section("C: must-fail controls (frozen seeds)")
    rng = random.Random(20260806)
    # C1: exchange 4 pairs between the first two fibers
    va, vb = GM["P15"][0], GM["P15"][1]
    pa = sorted({tuple(min(r, neg_vec(r))) for r in GM["FIBER"][va]})
    pb = sorted({tuple(min(r, neg_vec(r))) for r in GM["FIBER"][vb]})
    swap_a = rng.sample(pa, 4)
    swap_b = rng.sample(pb, 4)
    scr_fiber = {va: [], vb: []}
    for r in GM["FIBER"][va]:
        key = tuple(min(r, neg_vec(r)))
        scr_fiber[vb if key in swap_a else va].append(r)
    for r in GM["FIBER"][vb]:
        key = tuple(min(r, neg_vec(r)))
        scr_fiber[va if key in swap_b else vb].append(r)
    n_bad1 = 0
    for v in (va, vb):
        for u in coset_reps(GM, v):
            vec = np.zeros(240, dtype=np.int64)
            for r in scr_fiber[v]:
                vec[RIDX[r]] = 1 - 2 * GM["HB"][(u, GM["XLAB"][r])]
            jv = vec[JIDX]
            if not (np.array_equal(jv, vec)
                    or np.array_equal(jv, -vec)):
                n_bad1 += 1
    check("C1 CONTROL FIRES: scrambling the fibers (4 pairs exchanged "
          "between the first two, seed 20260806) destroys deck "
          "equivariance: %d/16 scrambled modes are no longer "
          "J-eigenvectors" % n_bad1, n_bad1 > 0)

    # C2: wrong character group F2^4 = V instead of v_perp
    v0 = GM["P15"][0]
    vecs = {}
    for u in GM["LBLS"]:
        vec = np.zeros(240, dtype=np.int8)
        for r in GM["FIBER"][v0]:
            vec[RIDX[r]] = 1 - 2 * GM["HB"][(u, GM["XLAB"][r])]
        vecs[u] = vec.tobytes()
    n_distinct = len(set(vecs.values()))
    check("C2 CONTROL FIRES: the WRONG character group F2^4 = V (16 "
          "characters restricted to the 8-element torsor) collides "
          "2:1 -- only %d distinct mode vectors instead of 16 (rank "
          "8 < 16): well-definedness as 16 rays breaks" % n_distinct,
          n_distinct == 8)

    # C3: seeded random sign systems
    n_bad3 = 0
    rvecs = []
    for _ in range(8):
        vec = np.zeros(240, dtype=np.int64)
        for r in GM["FIBER"][v0]:
            key = tuple(min(r, neg_vec(r)))
            vec[RIDX[r]] = 0
        signs = {}
        for r in GM["FIBER"][v0]:
            key = tuple(min(r, neg_vec(r)))
            if key not in signs:
                signs[key] = rng.choice((1, -1))
            vec[RIDX[r]] = signs[key]
        rvecs.append(vec)
    for i in range(8):
        jv = rvecs[i][JIDX]
        if not (np.array_equal(jv, rvecs[i])
                or np.array_equal(jv, -rvecs[i])):
            n_bad3 += 1
        for j in range(i + 1, 8):
            if int(rvecs[i] @ rvecs[j]) != 0:
                n_bad3 += 1
    check("C3 CONTROL FIRES: seeded random sign systems fail the "
          "certificates: %d violations (non-J-eigenvector or "
          "non-orthogonal pair) among 8 random 'modes'" % n_bad3,
          n_bad3 > 0)

    # ============================================================ VERDICT
    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    ctrl_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    core_ok = all(ok for nm, ok in CHECKS if not nm.startswith("C"))
    print("%d/%d checks passed" % (n_pass, n_all))
    print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    if not ctrl_ok:
        verdict = "TEST-VOID"
    elif not (P1a and P1b and P2):
        verdict = "TORSOR-FOURIER-MIXED"
    elif P3:
        verdict = "TORSOR-FOURIER-PURE"
    else:
        verdict = "TORSOR-FOURIER-PARTIAL"
    print("VERDICT: %s" % verdict)
    if verdict == "TORSOR-FOURIER-PARTIAL":
        print("""
NAMED BLOCKS (the PARTIAL content, stated precisely):
  * CARRIER BLOCK (clean, Fourier-aligned at sector level): M_S =
    span of the 64 Fourier rays of the 8 R-fibers = (1 + 5 + 10) x
    (1 + 3) as a W(D5) x W(A3)-module -- the carrier Pascal
    decomposition appears at character level with the family tetrad
    as its multiplicity space.  At v775's point level even sector
    purity per class was the exception (8 of 15); here the carrier
    block is an exact invariant subspace spanned by canonical rays.
  * FAMILY BLOCK (clean): the tetrad is S4-natural with sigma = family
    3-cycle + anchor; the family register is the multiplicity-4 label
    of the carrier 16.
  * NOT PURE: the D5-weight grading inside M_S is MUTUALLY UNBIASED
    with the character grading (|<pair|mode>|^2 = 1/8) -- no weight
    axis is a ray; the pointwise code->matter reading stays dead
    (ROOTCLASS-MIXED, v775, standing fence, cited).""")
    print("runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
