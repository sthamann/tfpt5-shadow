#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""e8_ramified_jetcode_probe -- E8.RAMIFIED.JETCODE.01: the jet-code
normal form of the Gaussian E8 compiler -- W = L/2L is the free rank-4
module over the DUAL NUMBERS F2[eps]/(eps^2) = Z[i]/(2) (2 ramifies:
2 = -i(1+i)^2), the class space V = L/(1+i)L is the canonical exact
self-extension quotient with ker(eps) = im(eps) (the self-dual
differential code), the deck J = 1 + eps EXPLAINS the certified v782
transition-bus torsor (J-translation = the eps-jet of the address),
the no-canonical-origin obstruction IS the non-splitness of the
extension, and the 120 root pairs are exactly the q = 1 unit shell.

TYPING DISCIPLINE (carried): every J-check below is an [E neu]
candidate -- exact from corpus machinery + elementary algebra,
machine-certified here; no [H] content in this probe.

STANDING CONTEXT (read-only, cited): v752/v689 (deployed rank-4 Z[i]
lattice L = Construction A over C*, class space V = L/(1+i)L = F2^4,
15 x 16 root census), v782 -- E8.TRANSITIONBUS.01 (TRANSITION-BUS-
TORSOR: pair fibers = rho_v + iota(v_perp), q = 1 shell, no
distinguished origin), e8_torsor_fourier_probe.py (TORSOR-FOURIER-
PARTIAL).  v775 ROOTCLASS-MIXED is unaffected: no matter semantics
anywhere in this probe.

THE FIVE MODULES (all frozen before running, FROZEN_SPEC hashed):
 J1 RING: Z[i]/(2) = F2[eps]/(eps^2) with eps = 1 + i; the iso is
    UNIQUE (the only nonzero nilpotent is 1+i); 2 = -i(1+i)^2 exact.
 J2 MODULE: W := L/2L is FREE of rank 4 over the dual numbers: an
    explicit Z[i]-basis of L is constructed (greedy over roots,
    covolume-certified), and the 4^4 = 256 dual-number combinations
    enumerate W bijectively.
 J3 EXTENSION: 0 -> eps W -> W -> V -> 0 exact; eps-multiplication
    induces the canonical iso V = eps W ([x] -> eps x, well-defined,
    bijective); ker(eps|W) = im(eps|W) -- the self-dual differential
    code (eps^2 = 0, ker = im), censused on all 256 points.
 J4 TORSOR EXPLANATION (the payoff): i = 1 + eps on W, so
    J w = w + eps w for every w (256/256); on every root, rho(J r) =
    rho(r) + iota(v) with iota = the J3 iso image of the class v --
    the FULL v782 fiber-translation table re-derived from ring
    algebra (15-row table printed).  NON-SPLITNESS: the extension
    admits ZERO mu4-equivariant linear splittings (census over all
    16^4 = 65536 linear sections; -1 = +1 mod 2, so mu4-equivariance
    = J-equivariance; a J-fixed section would land in ker eps = eps W,
    contradicting complementarity) -- "the product decomposition must
    fail" = W is not J-trivially V x V; equivalently J moves exactly
    the 240 classes outside eps W.
 J5 UNIT SHELL: q(w) = (<x,x>/4 mod 2) (the v782 convention, frozen;
    well-definedness re-censused) has exactly 120 + 136 = q^-1(1) +
    q^-1(0) points (PLUS type, Arf 0 by count), the 120 root pairs
    biject onto q^-1(1), each class fiber is the affine coset
    rho_v + iota(v_perp), and every root is exactly the triple
    (address v, admissible error jet w in q^-1(1) over v,
    orientation +-): 240 = 120 x 2.  Polarization census: b(w,w') =
    q(w+w')+q(w)+q(w') = <x,y>/2 mod 2 with trivial radical.

KILL (frozen): any module or root action contradicting the jet
structure (a failed census above).  CONTROLS (must fire): C1 the
WRONG RING F2 x F2 (split, unramified reading of 2) is NOT isomorphic
to Z[i]/(2) (idempotent/nilpotent census; all 4! bijections fail) --
the extension needs the ramified ring; C2 a seeded scramble of the
root -> W assignment breaks the q = 1 shell.

VERDICT ENUM (frozen): JETCODE-EXACT (all J1-J5 exact + controls
fire) / JETCODE-PARTIAL (controls fire, >= 1 module fails -> name
it) / JETCODE-DEAD (J2 or J3 fails: no jet structure) / TEST-VOID.

FENCES / FIREWALL: experiments/tfpt-discovery probe; ONE new file;
writes nothing; no verification/-, ledger, paper or website surface
touched; no .md.  Exact integer / Fraction / F2 arithmetic in every
load-bearing check; RNG only in control C2 (seed frozen 20260806).
No physics, no matter semantics (ROOTCLASS-MIXED cited above).

Run:
    python3 experiments/tfpt-discovery/e8_ramified_jetcode_probe.py
"""

import hashlib
import itertools
import random
import time
from collections import Counter
from fractions import Fraction as Fr

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


FROZEN_SPEC = """\
E8.RAMIFIED.JETCODE.01 FROZEN SPEC (2026-08-06, before any root data).
J1 ring iso Z[i]/(2) = F2[eps]/(eps2), eps = 1+i, unique; 2 = -i(1+i)^2.
J2 W = L/2L free rank 4 over the dual numbers (explicit Z[i]-basis,
covolume-certified; 256 combinations bijective).
J3 0 -> eps W -> W -> V -> 0 exact; V = eps W via [x] -> eps x;
ker(eps) = im(eps) (self-dual differential code).
J4 J = 1 + eps (256/256); rho(Jr) = rho(r) + iota(v) for all 240 roots
(v782 torsor re-derived); ZERO mu4-equivariant splittings among all
65536 linear sections (-1 = +1 mod 2 => mu4-equiv = J-equiv).
J5 q(w) = <x,x>/4 mod 2 (v782 convention frozen): 120 ones / 136 zeros
(plus type, Arf 0), root pairs = q^-1(1) bijectively, fibers = affine
cosets rho_v + iota(v_perp), roots = (address, jet, orientation).
CONTROLS: C1 F2 x F2 not isomorphic (idempotent census 4 vs 2,
nilpotent census 0 vs 1, all 24 bijections fail); C2 LCG scramble
(seed 20260806) of pair images breaks q = 1.  VERDICT enum:
JETCODE-EXACT / PARTIAL / DEAD / TEST-VOID as in the docstring.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# ======================================================================
# v752/v689 machinery (verbatim, read-only source)
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


def rank_Q(rows):
    """rank over Q of integer rows (Fraction elimination)."""
    A = [[Fr(v) for v in r] for r in rows]
    rank = 0
    ncol = len(A[0]) if A else 0
    row = 0
    for col in range(ncol):
        piv = next((r for r in range(row, len(A)) if A[r][col] != 0),
                   None)
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        inv = 1 / A[row][col]
        A[row] = [a * inv for a in A[row]]
        for r in range(len(A)):
            if r != row and A[r][col] != 0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[row])]
        row += 1
        rank += 1
    return rank


def main():
    print("=" * 78)
    print("E8.RAMIFIED.JETCODE.01 -- the jet-code normal form "
          "(dual numbers, self-extension, unit shell)")
    print("=" * 78)
    print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA, flush=True)

    # ---------------------------------------------------------------- P0
    section("P0: deployed lattice state (v752/v689 recipe, read-only)")
    all_placements = set()
    for p in itertools.permutations(range(8)):
        all_placements.add(code_image(C_NAIVE, p))
    both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
                if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
    CSTAR = [c for c in both_inv if W0246 in c][0]
    ROOTS = sorted(constrA_roots(CSTAR))
    LAT = constrA_lattice(CSTAR)
    coords = LAT["coords"]
    REPS = label_group(LAT)
    ZERO = LAT["label"]((0,) * 8)
    LBLS = sorted(REPS)
    P15 = [lb for lb in LBLS if lb != ZERO]
    root_label = {r: LAT["label"](r) for r in ROOTS}
    census = Counter(root_label.values())
    check("P0.1 C* deterministic, 240 roots, 15 x 16 class census, zero "
          "class empty (v752 state)",
          supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED
          and len(ROOTS) == 240 and len(census) == 15
          and sorted(census.values()) == [16] * 15 and ZERO not in census)

    # ---------------------------------------------------------------- J1
    section("J1 [E neu]: Z[i]/(2) = F2[eps]/(eps^2), eps = 1 + i "
            "(2 ramifies)")
    check("J1.1 2 = -i (1+i)^2 in Z[i] exact: (0,-1)*(1,1)^2 = (2,0)",
          (lambda s: (0 * s[0] - (-1) * s[1],
                      0 * s[1] + (-1) * s[0]) == (2, 0))
          ((1 * 1 - 1 * 1, 1 * 1 + 1 * 1)))

    # Z[i]/(2): elements (a,b) = a + b i mod 2
    ZI2 = [(a, b) for a in (0, 1) for b in (0, 1)]

    def zi2_add(x, y):
        return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)

    def zi2_mul(x, y):
        return ((x[0] * y[0] - x[1] * y[1]) % 2,
                (x[0] * y[1] + x[1] * y[0]) % 2)

    # F2[eps]/(eps^2): elements (c,d) = c + d eps
    DN = [(c, d) for c in (0, 1) for d in (0, 1)]

    def dn_add(x, y):
        return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)

    def dn_mul(x, y):
        return ((x[0] * y[0]) % 2, (x[0] * y[1] + x[1] * y[0]) % 2)

    def phi(x):  # c + d eps -> (c+d) + d i   (eps = 1 + i)
        return ((x[0] + x[1]) % 2, x[1])

    ok_iso = (len({phi(x) for x in DN}) == 4
              and all(phi(dn_add(x, y)) == zi2_add(phi(x), phi(y))
                      for x in DN for y in DN)
              and all(phi(dn_mul(x, y)) == zi2_mul(phi(x), phi(y))
                      for x in DN for y in DN)
              and phi((1, 0)) == (1, 0) and phi((0, 1)) == (1, 1))
    nilp_zi2 = [x for x in ZI2 if zi2_mul(x, x) == (0, 0) and x != (0, 0)]
    idem_zi2 = [x for x in ZI2 if zi2_mul(x, x) == x]
    check("J1.2 EXPLICIT RING ISO: phi(c + d eps) = (c+d) + d i is a "
          "bijective ring map (16 + 16 products checked); phi(eps) = "
          "1 + i; iso UNIQUE (the only nonzero nilpotent of Z[i]/(2) "
          "is 1+i: %s); idempotents = {0, 1} (local ring): %s"
          % (nilp_zi2, idem_zi2),
          ok_iso and nilp_zi2 == [(1, 1)]
          and sorted(idem_zi2) == [(0, 0), (1, 0)])
    check("J1.3 i = 1 + eps in the quotient: phi(1 + eps) = i "
          "(the deck unit IS the jet unit)",
          phi(dn_add((1, 0), (0, 1))) == (0, 1))

    # ---------------------------------------------------------------- J2
    section("J2 [E neu]: W = L/2L is FREE of rank 4 over the dual "
            "numbers")

    # explicit Z[i]-basis of L via Hermite reduction over the EUCLIDEAN
    # domain Z[i]: chart L into Z[i]^4 (z_k = x_2k + i x_2k+1, J = i),
    # HNF-reduce the 8 Z-basis generators to 4 pivot rows.
    def gadd(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def gsub(a, b):
        return (a[0] - b[0], a[1] - b[1])

    def gmul(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

    def gnorm(a):
        return a[0] * a[0] + a[1] * a[1]

    def gquo(a, b):
        """nearest-integer Gaussian quotient a/b."""
        n = gnorm(b)
        num = gmul(a, (b[0], -b[1]))
        return ((2 * num[0] + n) // (2 * n), (2 * num[1] + n) // (2 * n))

    def chart4(x):
        return tuple((x[2 * k], x[2 * k + 1]) for k in range(4))

    def unchart(z):
        out = []
        for c in z:
            out += [c[0], c[1]]
        return tuple(out)

    gen = [list(chart4(b)) for b in LAT["B"]]
    pivots = []
    for col in range(4):
        live = [g for g in gen if g[col] != (0, 0)]
        rest = [g for g in gen if g[col] == (0, 0)]
        while len(live) > 1:
            live.sort(key=lambda g: gnorm(g[col]))
            a, b = live[0], live[1]
            q = gquo(b[col], a[col])
            for k in range(4):
                b[k] = gsub(b[k], gmul(q, a[k]))
            if b[col] == (0, 0):
                live.pop(1)
                rest.append(b)
            elif gnorm(b[col]) == 0:
                live.pop(1)
        assert live, "rank defect"
        pivots.append(live[0])
        gen = rest
    zbasis = [unchart(p) for p in pivots]
    ok_in_L = all(coords(v) is not None for v in zbasis)  # asserts
    detL = LAT["det"]
    rows = []
    for v in zbasis:
        rows.append(list(v))
        rows.append(list(J_vec(v)))
    det8 = mat_det_inv(rows)[0]
    check("J2.1 explicit Z[i]-basis of L (Hermite over the Euclidean "
          "domain Z[i]): 4 lattice vectors %s; (e_k, J e_k) is a "
          "Z-basis (covolume |det| = %s = |det L| = %s => index 1, "
          "so L is FREE rank 4 over Z[i])"
          % (zbasis, abs(det8), abs(detL)),
          ok_in_L and len(zbasis) == 4 and abs(det8) == abs(detL))

    def rho_of(x):
        return tuple(c % 2 for c in coords(x))

    def lift2(rho):
        w = (0,) * 8
        for i, bit in enumerate(rho):
            if bit:
                w = add_vec(w, LAT["B"][i])
        return w

    # dual-number combinations: sum (a_k + b_k eps) e_k
    combo = {}
    for ab in itertools.product((0, 1), repeat=8):
        w = (0,) * 8
        for k in range(4):
            a, b = ab[2 * k], ab[2 * k + 1]
            if a:
                w = add_vec(w, zbasis[k])
            if b:
                w = add_vec(w, add_vec(zbasis[k], J_vec(zbasis[k])))
        combo[ab] = rho_of(w)
    check("J2.2 FREENESS: the 4^4 = 256 dual-number combinations "
          "Sum (a_k + b_k eps) e_k enumerate W = L/2L bijectively "
          "(%d distinct classes) -- W = (F2[eps]/eps^2)^4 free"
          % len(set(combo.values())), len(set(combo.values())) == 256)

    RHO_ALL = sorted(itertools.product((0, 1), repeat=8))
    LIFT = {rho: lift2(rho) for rho in RHO_ALL}

    def eps_w(rho):
        x = LIFT[rho]
        return rho_of(add_vec(x, J_vec(x)))     # (1+i) x = x + J x

    EPS = {rho: eps_w(rho) for rho in RHO_ALL}
    IW = {rho: rho_of(J_vec(LIFT[rho])) for rho in RHO_ALL}
    ok_mod = all(
        IW[rho] == tuple((a + b) % 2 for a, b in
                         zip(rho, EPS[rho])) for rho in RHO_ALL)
    check("J2.3 module structure transported: multiplication by i on W "
          "equals 1 + eps on all 256 classes (i w = w + eps w)", ok_mod)

    # ---------------------------------------------------------------- J3
    section("J3 [E neu]: the exact self-extension 0 -> eps W -> W -> "
            "V -> 0 and ker(eps) = im(eps)")
    EPSW = sorted({EPS[rho] for rho in RHO_ALL})
    KER = sorted(rho for rho in RHO_ALL
                 if EPS[rho] == (0,) * 8)
    check("J3.1 SELF-DUAL DIFFERENTIAL CODE: |im(eps)| = %d = |ker(eps)|"
          " = %d and ker = im exactly (eps^2 = 0 realized with maximal "
          "rank drop 256 -> 16)" % (len(EPSW), len(KER)),
          len(EPSW) == 16 and KER == EPSW)

    def v_of(rho):
        return LAT["label"](LIFT[rho])

    ok_seq = (sorted({v_of(rho) for rho in EPSW}) == [ZERO]
              and len({v_of(rho) for rho in RHO_ALL}) == 16)
    iota = {}
    ok_wd = True
    for lb in LBLS:
        imgs = set()
        x = REPS[lb]
        for b in [(0,) * 8] + list(LAT["B"]):
            xs = add_vec(x, add_vec(b, J_vec(b)))   # x + (1+i) b
            imgs.add(rho_of(add_vec(xs, J_vec(xs))))
        if len(imgs) != 1:
            ok_wd = False
        iota[lb] = next(iter(imgs))
    ok_bij = len(set(iota.values())) == 16 and set(iota.values()) \
        == set(EPSW) and iota[ZERO] == (0,) * 8
    check("J3.2 EXACTNESS + CANONICAL ISO: eps W maps to 0 in V, "
          "W ->> V (16 classes); eps-multiplication induces "
          "V = eps W: [x] -> eps x well-defined over all lift shifts "
          "(9 lifts per class) and bijective (16 distinct images)",
          ok_seq and ok_wd and ok_bij)

    # ---------------------------------------------------------------- J4
    section("J4 [E neu]: J = 1 + eps explains the v782 torsor; the "
            "extension does NOT split mu4-equivariantly")
    ok_jw = all(IW[rho]
                == tuple((a + b) % 2 for a, b in zip(rho, EPS[rho]))
                for rho in RHO_ALL)
    ROOT_RHO = {r: rho_of(r) for r in ROOTS}
    ok_troot = all(
        ROOT_RHO[tuple(J_vec(r))]
        == tuple((a + b) % 2
                 for a, b in zip(ROOT_RHO[r], iota[root_label[r]]))
        for r in ROOTS)
    check("J4.1 TORSOR EXPLAINED: J w = w + eps w (256/256) and on all "
          "240 roots rho(J r) = rho(r) + iota(v) -- the v782 deck "
          "translation IS multiplication by the jet unit 1 + eps; "
          "translation vector = the J3 iso image of the ADDRESS v",
          ok_jw and ok_troot)
    print("    fiber-translation table (class v -> iota(v)):")
    for lb in P15:
        print("      v = %s  ->  iota(v) = %s" % (lb, iota[lb]))

    n_moved = sum(1 for rho in RHO_ALL if IW[rho] != rho)
    check("J4.2 J moves exactly 240 of the 256 classes (fixes exactly "
          "ker eps = eps W, %d classes): W is NOT a J-trivial product "
          "V x V" % (256 - n_moved), n_moved == 240)

    # non-splitness census: all 16^4 linear sections
    vbasis = []
    seen = {ZERO}
    for lb in P15:
        if lb not in seen:
            vbasis.append(lb)
            new = set()
            for s in seen:
                x = add_vec(REPS[s], REPS[lb])
                new.add(LAT["label"](x))
            seen |= new
        if len(vbasis) == 4:
            break
    cosets = {lb: [rho for rho in RHO_ALL if v_of(rho) == lb]
              for lb in vbasis}
    ok_cosets = all(len(cosets[lb]) == 16 for lb in vbasis)
    n_sections = 0
    n_equivariant = 0
    for choice in itertools.product(*(cosets[lb] for lb in vbasis)):
        n_sections += 1
        if all(EPS[rho] == (0,) * 8 for rho in choice):
            n_equivariant += 1
    n_good_lift = {lb: sum(1 for rho in cosets[lb]
                           if EPS[rho] == (0,) * 8) for lb in vbasis}
    check("J4.3 NON-SPLITNESS (the no-canonical-origin obstruction as "
          "ring algebra): of all %d = 16^4 linear sections V -> W, "
          "EXACTLY %d are mu4-equivariant (-1 = +1 mod 2, so mu4-equiv "
          "= J-equiv = image in ker eps; per-basis good lifts %s): "
          "the product decomposition MUST fail -- expected 0"
          % (n_sections, n_equivariant,
             sorted(n_good_lift.values())),
          ok_cosets and n_sections == 65536 and n_equivariant == 0
          and all(n == 0 for n in n_good_lift.values()))

    # ---------------------------------------------------------------- J5
    section("J5 [E neu]: the unit shell -- 120 root pairs = the q = 1 "
            "points (plus type), roots = (address, jet, orientation)")
    Q2 = {}
    ok_qwd = True
    for rho in RHO_ALL:
        x = LIFT[rho]
        n = ip(x, x)
        assert n % 4 == 0
        Q2[rho] = (n // 4) % 2
        for b in LAT["B"]:
            x2 = add_vec(x, tuple(2 * a for a in b))
            if ((ip(x2, x2) // 4) % 2) != Q2[rho]:
                ok_qwd = False
    n1 = sum(1 for rho in RHO_ALL if Q2[rho] == 1)
    check("J5.1 q(w) = <x,x>/4 mod 2 (v782 convention frozen) "
          "well-defined on W; census %d ones / %d zeros = 120 / 136 "
          "=> PLUS type (Arf 0 by count)" % (n1, 256 - n1),
          ok_qwd and n1 == 120)

    pair_imgs = {ROOT_RHO[r] for r in ROOTS}
    ok_pairs = (len(pair_imgs) == 120
                and all(Q2[rho] == 1 for rho in pair_imgs)
                and all(ROOT_RHO[r] == ROOT_RHO[neg_vec(r)]
                        for r in ROOTS))
    check("J5.2 UNIT SHELL: the 240 roots map 2:1 (r ~ -r) onto "
          "EXACTLY the 120 q = 1 points -- every admissible unit jet "
          "is realized by exactly one root pair", ok_pairs)

    VPERP = {v: [t for t in LBLS
                 if ((ip(REPS[t], REPS[v]) // 2)
                     + (ip(REPS[t], J_vec(REPS[v])) // 2)) % 2 == 0]
             for v in P15}
    ok_fiber = True
    for v in P15:
        fib = sorted(ROOT_RHO[r] for r in ROOTS if root_label[r] == v)
        fib = sorted(set(fib))
        base = fib[0]
        coset = sorted(tuple((a + b) % 2 for a, b in zip(base, iota[t]))
                       for t in VPERP[v])
        if len(VPERP[v]) != 8 or fib != coset:
            ok_fiber = False
    check("J5.3 JET READING CERTIFIED: over each address v the 8 root "
          "pairs are exactly the affine coset rho_v + iota(v_perp) "
          "(the v782 torsor), so every root IS the triple (address v, "
          "admissible error jet, orientation +-): 240 = 15 x 8 x 2",
          ok_fiber)

    ok_pol = True
    for rho in RHO_ALL:
        for rho2 in RHO_ALL:
            b1 = (Q2[tuple((a + b) % 2 for a, b in zip(rho, rho2))]
                  + Q2[rho] + Q2[rho2]) % 2
            b2 = (ip(LIFT[rho], LIFT[rho2]) // 2) % 2
            if b1 != b2:
                ok_pol = False
                break
        if not ok_pol:
            break
    rad = [rho for rho in RHO_ALL
           if all((Q2[tuple((a + b) % 2 for a, b in zip(rho, rho2))]
                   + Q2[rho] + Q2[rho2]) % 2 == 0 for rho2 in RHO_ALL)]
    check("J5.4 polarization census: b(w,w') = q(w+w')+q(w)+q(w') = "
          "<x,y>/2 mod 2 on all 65536 pairs; radical trivial (%d "
          "element): (W, q) is a nondegenerate plus-type quadratic "
          "space O+(8,2)-style" % len(rad),
          ok_pol and rad == [(0,) * 8])

    # ---------------------------------------------------------------- C
    section("C: must-fail controls")
    # C1: the wrong (split/unramified) ring F2 x F2
    F22 = [(a, b) for a in (0, 1) for b in (0, 1)]

    def f22_mul(x, y):
        return ((x[0] * y[0]) % 2, (x[1] * y[1]) % 2)

    idem_f22 = [x for x in F22 if f22_mul(x, x) == x]
    nilp_f22 = [x for x in F22 if f22_mul(x, x) == (0, 0) and x != (0, 0)]
    n_iso = 0
    for pm in itertools.permutations(F22):
        m = dict(zip(F22, pm))
        if m[(0, 0)] != (0, 0):
            continue
        if all(m[zi2_mul(x, y)] == f22_mul(m[x], m[y])
               and m[zi2_add(x, y)] == ((m[x][0] + m[y][0]) % 2,
                                        (m[x][1] + m[y][1]) % 2)
               for x in F22 for y in F22):
            n_iso += 1
    check("C1 CONTROL FIRES: the WRONG RING F2 x F2 (unramified/split "
          "reading of 2) is NOT isomorphic to Z[i]/(2): idempotents "
          "4 vs 2, nonzero nilpotents %d vs 1, all 24 bijections fail "
          "(%d ring isos) -- the extension/jet structure needs the "
          "RAMIFIED ring" % (len(nilp_f22), n_iso),
          len(idem_f22) == 4 and len(nilp_f22) == 0 and n_iso == 0)

    # C2: scrambled lattice assignment breaks q = 1
    rng = random.Random(20260806)
    targets = rng.sample(RHO_ALL, 120)
    n_bad = sum(1 for t in targets if Q2[t] != 1)
    check("C2 CONTROL FIRES: a seeded scramble of the 120 pair images "
          "(random distinct W-points, seed 20260806) leaves the unit "
          "shell: %d/120 scrambled images have q != 1" % n_bad,
          n_bad > 0)

    # ============================================================ VERDICT
    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    ctrl_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
    core = [ok for nm, ok in CHECKS if not nm.startswith("C")]
    print("%d/%d checks passed" % (n_pass, n_all))
    print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    if not ctrl_ok:
        verdict = "TEST-VOID"
    elif all(core):
        verdict = "JETCODE-EXACT"
    elif any(nm.startswith(("J2", "J3")) and not ok
             for nm, ok in CHECKS):
        verdict = "JETCODE-DEAD"
    else:
        verdict = "JETCODE-PARTIAL"
    print("VERDICT: %s" % verdict)
    if verdict == "JETCODE-EXACT":
        print("""
JET-CODE NORMAL FORM (all [E neu], machine-certified above):
  Z[i]/(2) = F2[eps]/(eps^2) (2 ramifies, eps = 1+i, unique iso);
  W = L/2L = (dual numbers)^4 free; 0 -> eps W -> W -> V -> 0 exact
  with V = eps W canonically and ker(eps) = im(eps); the deck is the
  jet unit J = 1 + eps, whence the certified v782 torsor translation
  rho(Jr) = rho(r) + iota(v); the extension admits ZERO mu4-
  equivariant splittings (the no-canonical-origin obstruction IS
  non-splitness); the 120 root pairs are exactly the q = 1 unit
  shell of the plus-type form, so each root is canonically
  (address v, admissible error jet in the affine v_perp coset,
  orientation).  No matter semantics (v775 ROOTCLASS-MIXED cited).""")
    print("runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
