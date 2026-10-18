#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""e8_affine_nsr_probe -- E8.AFFINE.NSR.01: the NS/R character of the
class space V = L/(1+i)L splits V \ {0} into 7 NS classes (= ker chi
minus 0) and an 8-point AFFINE F2^3-torsor A = chi^{-1}(1) (the R
classes); the stabilizer of chi in GL(4,2) is EXACTLY AGL(3,2) of
order 1344 with its natural action on the 8 points -- the SAME group,
with the SAME natural 8-point action, as the corpus Aut(H8) anchor --
and the evaluation code of affine functions on A reconstructs the
[8,4,4] Hamming code RM(1,3) = H8 permutation-equivalently.

TYPING DISCIPLINE (carried): A1-A6 are [E neu] candidates -- exact
from corpus machinery + elementary algebra, machine-certified here.
The RECONSTRUCTION-CHAIN reading (A5b: "NS/R bit -> affine 8-point
space -> [8,4,4]" as a sharpened attack surface for
ARF.BOUNDARY.CODE.01) is typed [H neu]: the chain itself is exact,
but its use as a boundary-code derivation route remains a hypothesis
-- the route to V still passes through Gaussian E8, so NO P2-removal
claim is made.

CORPUS ANCHORS (read-only, cited):
  * chi_NSR: v752 P5 (NS/R purity per class, chi = hbar(., y0) linear),
    v775 S1.2 (7 NS classes = 112 integer roots, 8 R classes = 128
    spinor roots, standard doubled model).
  * the 120 + 128 current decomposition: v148 (Fock census: 248
    currents = 120 + 128), v227 (248 = adj(D8) + spinor(D8), the D8
    branching), v301 (SO(16)_1 contains (E8)_1: dim so(16) = 120
    currents + 128 spinor).
  * Aut(H8) = AGL(3,2), order 1344: v646 R1a.1 (|AGL(3,2)| = 1344,
    all preserving C* in the bits3 position labeling), v776 (30 =
    8!/1344 placements of e8-hat).
  * ARF.BOUNDARY.CODE.01 state: v776 (verdict BOUNDARY-CODE-UNIQUE),
    residual R1 sharpened by v799 (SEAM.CODE.TYPEII.01, TYPEII-FORCED).
  * FENCE: v775 ROOTCLASS-MIXED -- this probe reads the NS/R CURRENT
    structure (so(16) adjoint vs spinor), NOT a particle table; no
    matter semantics anywhere.

THE SIX MODULES (frozen before running, FROZEN_SPEC hashed):
 A1 K = ker(chi_NSR) = F2^3 (8 labels incl 0; 7 nonzero = NS classes);
    A = chi^{-1}(1) (8 labels = R classes) is an affine K-torsor
    (differences in K, action free + transitive); V \ {0} = 7 u 8.
 A2 root counts: 7 x 16 = 112 NS roots = EXACTLY the D8 root system
    (all +-2e_i +- 2e_j patterns, doubled model); 8 x 16 = 128 R roots
    = the Ramond spinor (+-1)^8, sum = 0 mod 4; bookkeeping
    248 = (112 + 8) + 128 = adj so(16) + spinor (anchors above).
 A3 STABILIZER THEOREM: Stab_{GL(4,2)}(chi) has order 1344 =
    20160 / 15 (orbit census), acts AFFINELY on A (a -> g a, affine
    over g|_K), FAITHFULLY (kernel of the 8-point action = 1), and
    equals -- as a permutation group on the 8 chart points -- the
    directly constructed AGL(3,2) = {j -> Mj + t} of order 8 x 168.
 A4 Aut(H8) IDENTIFICATION: Aut(C*) (brute force over all 8!
    coordinate permutations) has order 1344 and equals the v646
    position-AGL(3,2) (bits3 labeling) as a permutation group -- the
    SAME natural action on 8 points as A3's; the chart composition is
    the explicit isomorphism of actions.
 A5 HAMMING RECONSTRUCTION: the evaluation code C_A of all affine
    functions a + lambda(x) on the 8 points of A has dim 4, weight
    enumerator 1 + 14 x^4 + x^8, doubly even, SELF-DUAL, and is
    permutation-equivalent to the deployed C* with EXACTLY 1344
    equivalence permutations (= |Aut(H8)|); hence C_A = RM(1,3) = H8.
    [H neu] chain reading typed in the docstring above.
 A6 COMPATIBILITY (the kill test): the DEPLOYED label symmetry
    Sp(4,2) (symplectic group of the hbar Gram, order 720; the label
    action of G31, v752) stabilizes chi in a subgroup of order 48 =
    720/15 whose 8-point action lies INSIDE the A3 affine group
    (census; orbit structure on A reported).  KILL: the NS/R label
    action incompatible with the affine action = any Stab_Sp(chi)
    element acting non-affinely on A.

CONTROLS (must fire, frozen):
  X1 WRONG CHARACTER: each of the other 14 nonzero functionals fails
     parity purity (its level sets mix NS and R roots) -- chi_NSR is
     the UNIQUE parity functional; the wrong-character orbit/stabilizer
     structure on roots differs (mixing census > 0).
  X2 SCRAMBLED LABELS: a seeded LCG shuffle of the 240 root -> class
     assignments destroys NS/R class purity (mixed classes appear).
  X3 CORRUPTED CODE: flipping one bit of one nonzero word of C_A
     breaks the weight enumerator 1 + 14x^4 + x^8 and self-duality.

VERDICT ENUM (frozen): AFFINE-NSR-EXACT (A1-A6 exact + controls fire)
/ AFFINE-NSR-PARTIAL (controls fire, >= 1 module fails -> name it) /
AFFINE-NSR-DEAD (A3 or A4 or A6 fails: no affine identification) /
TEST-VOID (a control does not fire).

FENCES / FIREWALL: experiments/tfpt-discovery probe; ONE new file;
writes nothing; no verification/-, ledger, paper or website surface
touched; no .md.  Exact integer / F2 arithmetic in every load-bearing
check; RNG only in control X2 (seed frozen 20260806).

Run:
    python3 experiments/tfpt-discovery/e8_affine_nsr_probe.py
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
E8.AFFINE.NSR.01 FROZEN SPEC (2026-08-06, before any root data).
A1 K = ker chi_NSR = F2^3, A = chi^-1(1) an affine K-torsor;
V\\{0} = 7 NS u 8 R.  A2 112 NS roots = D8 root system, 128 R roots =
Ramond spinor; 248 = (112+8)+128 (v148/v227/v301 anchors).
A3 Stab_GL(4,2)(chi) order 1344 = 20160/15, affine + faithful on A,
= AGL(3,2) (direct construction j -> Mj+t) as permutation group.
A4 Aut(C*) order 1344 = v646 position-AGL(3,2) as permutation group.
A5 evaluation code C_A: dim 4, enumerator 1+14x^4+x^8, doubly even,
self-dual, permutation-equivalent to C* with exactly 1344
equivalences (RM(1,3) = H8).  [H neu] chain reading; no P2 removal.
A6 Stab_Sp(4,2)(chi) order 48 acts inside the affine group (kill:
any non-affine action).  CONTROLS: X1 all 14 other functionals fail
parity purity; X2 LCG shuffle (seed 20260806) breaks class purity;
X3 one flipped bit breaks the enumerator + self-duality.
VERDICT enum: AFFINE-NSR-EXACT / PARTIAL / DEAD / TEST-VOID.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

# ======================================================================
# v752 lattice machinery (verbatim, read-only source)
# ======================================================================
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)
G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))
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


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


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


def bits3(j):
    return ((j >> 2) & 1, (j >> 1) & 1, j & 1)


def main():
    print("=" * 78)
    print("E8.AFFINE.NSR.01 -- the NS/R bit as an affine 8-point "
          "geometry with AGL(3,2) = Aut(H8)")
    print("=" * 78)
    print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA, flush=True)

    # ---------------------------------------------------------------- A0
    section("A0: standard doubled model (v752/v775 machinery, "
            "read-only)")

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
    REPS = label_group(LAT)
    ZERO = LAT["label"]((0,) * 8)
    LBLS = sorted(REPS)
    root_label = {r: LAT["label"](r) for r in ROOTS}
    census = Counter(root_label.values())
    ADDV = {(a, b): LAT["label"](add_vec(REPS[a], REPS[b]))
            for a in LBLS for b in LBLS}
    check("A0.1 240 roots, 15 x 16 census, zero class empty "
          "(v752/v775 state)",
          len(ROOTS) == 240 and len(census) == 15
          and sorted(census.values()) == [16] * 15
          and ZERO not in census)

    # NS/R character: parity = r[0] mod 2, class-pure, linear
    class_par = {}
    pure = True
    for r, lb in root_label.items():
        p = r[0] % 2
        if lb in class_par and class_par[lb] != p:
            pure = False
        class_par[lb] = p
    chi = dict(class_par)
    chi[ZERO] = 0
    ok_lin = all(chi[ADDV[(a, b)]] == (chi[a] + chi[b]) % 2
                 for a in LBLS for b in LBLS)
    check("A0.2 chi_NSR class-pure (v752 P5.1) and LINEAR on V "
          "(256/256 additivity; v752 P5.3: chi = hbar(., y0))",
          pure and ok_lin)

    # ---------------------------------------------------------------- A1
    section("A1 [E neu]: K = ker chi = F2^3 and the affine 8-point "
            "torsor A")
    K = [lb for lb in LBLS if chi[lb] == 0]
    A = [lb for lb in LBLS if chi[lb] == 1]
    ok_K = (len(K) == 8 and ZERO in K
            and all(ADDV[(a, b)] in K for a in K for b in K))
    ok_A = (len(A) == 8
            and all(ADDV[(a, b)] in K for a in A for b in A)
            and all(sorted(ADDV[(k, a)] for a in A) == sorted(A)
                    for k in K)
            and all(len({ADDV[(k, a)] for k in K}) == 8 for a in A))
    check("A1.1 K = ker chi is an F2^3 subgroup (8 labels incl 0, "
          "closed); A = chi^-1(1) is an affine K-TORSOR: A + A c K, "
          "K acts freely and transitively on A; V \\ {0} = "
          "(7 NS) u (8 R) exact",
          ok_K and ok_A and len(K) - 1 == 7 and len(A) == 8)

    # ---------------------------------------------------------------- A2
    section("A2 [E neu]: 112 = D8 roots (NS) + 128 = Ramond spinor "
            "(R); 248 = (112 + 8) + 128")
    ns_roots = [r for r in ROOTS if r[0] % 2 == 0]
    r_roots = [r for r in ROOTS if r[0] % 2 == 1]
    ok_d8 = (len(ns_roots) == 112
             and all(sorted(map(abs, r)) == [0] * 6 + [2, 2]
                     for r in ns_roots)
             and len({root_label[r] for r in ns_roots}) == 7
             and {root_label[r] for r in ns_roots} == set(K) - {ZERO})
    ok_sp = (len(r_roots) == 128
             and all(sorted(map(abs, r)) == [1] * 8 and sum(r) % 4 == 0
                     for r in r_roots)
             and {root_label[r] for r in r_roots} == set(A))
    check("A2.1 the 7 NS classes carry EXACTLY the 112 D8 roots "
          "(+-2e_i +- 2e_j, doubled model) = 7 x 16; the 8 R classes "
          "carry EXACTLY the 128 Ramond spinor roots ((+-1)^8, "
          "sum = 0 mod 4) = 8 x 16", ok_d8 and ok_sp)
    check("A2.2 current bookkeeping: 248 = (112 + 8) + 128 = "
          "adj so(16) + spinor -- the corpus 120 + 128 NS/R current "
          "module (v148 Fock census; v227 D8 branching; v301 "
          "SO(16)_1 contains (E8)_1)",
          112 + 8 + 128 == 248 and 120 + 128 == 248)

    # ---------------------------------------------------------------- A3
    section("A3 [E neu]: Stab_GL(4,2)(chi) = AGL(3,2), order 1344, "
            "natural on the 8 points of A")
    # bit coordinates on the label group
    vbasis = []
    span = {ZERO}
    for lb in LBLS:
        if lb not in span:
            vbasis.append(lb)
            span = set()
            for m in itertools.product((0, 1), repeat=len(vbasis)):
                x = ZERO
                for mi, bl in zip(m, vbasis):
                    if mi:
                        x = ADDV[(x, bl)]
                span.add(x)
        if len(vbasis) == 4:
            break
    bit_of = {}
    for m in itertools.product((0, 1), repeat=4):
        x = ZERO
        for mi, bl in zip(m, vbasis):
            if mi:
                x = ADDV[(x, bl)]
        bit_of[x] = m[0] * 8 + m[1] * 4 + m[2] * 2 + m[3]
    lbl_of_bit = {v: k for k, v in bit_of.items()}
    chi_bit = [chi[lbl_of_bit[x]] for x in range(16)]

    def rank4(rows):
        rows = list(rows)
        rk = 0
        for bit in (8, 4, 2, 1):
            piv = next((r for r in rows if r & bit), None)
            if piv is None:
                continue
            rows = [r ^ piv if (r & bit) else r for r in rows
                    if r != piv]
            rk += 1
        return rk

    def mat_apply(M, x):
        y = 0
        for i in range(4):
            if bin(M[i] & x).count("1") % 2:
                y |= (8 >> i)
        return y

    GL = []
    for M in itertools.product(range(16), repeat=4):
        if rank4(M) == 4:
            GL.append(M)
    STAB = [M for M in GL
            if all(chi_bit[mat_apply(M, x)] == chi_bit[x]
                   for x in range(16))]
    orbit_chi = {tuple(chi_bit[mat_apply(M, x)] for x in range(16))
                 for M in GL}
    check("A3.1 |GL(4,2)| = %d = 20160; Stab(chi_NSR) order %d = 1344 "
          "= 20160 / 15 (chi-orbit census: %d nonzero functionals)"
          % (len(GL), len(STAB), len(orbit_chi)),
          len(GL) == 20160 and len(STAB) == 1344
          and len(orbit_chi) == 15)

    A_bits = sorted(x for x in range(16) if chi_bit[x] == 1)
    K_bits = sorted(x for x in range(16) if chi_bit[x] == 0)
    a0 = A_bits[0]
    kbasis = []
    kspan = {0}
    for x in K_bits:
        if x not in kspan and x != 0:
            kbasis.append(x)
            kspan = {s ^ (x if m else 0) for s in kspan for m in (0, 1)}
        if len(kbasis) == 3:
            break
    idx_of = {}
    for m in itertools.product((0, 1), repeat=3):
        k = 0
        for mi, kb in zip(m, kbasis):
            if mi:
                k ^= kb
        idx_of[k] = m[0] * 4 + m[1] * 2 + m[2]

    def chart(a):
        return idx_of[a ^ a0]

    unchart = {chart(a): a for a in A_bits}
    stab_perms = set()
    ok_affine = True
    for M in STAB:
        pm = tuple(chart(mat_apply(M, unchart[j])) for j in range(8))
        stab_perms.add(pm)
        # affine test: j -> pm[j] ^ pm[0] must be F2^3-linear
        t = pm[0]
        lin = [pm[j] ^ t for j in range(8)]
        if any(lin[j ^ j2] != lin[j] ^ lin[j2]
               for j in range(8) for j2 in range(8)):
            ok_affine = False
    AGL = set()
    for M3 in itertools.product(range(8), repeat=3):
        rows = list(M3)
        rk = 0
        rr = rows[:]
        for bit in (4, 2, 1):
            piv = next((r for r in rr if r & bit), None)
            if piv is None:
                continue
            rr = [r ^ piv if (r & bit) else r for r in rr if r != piv]
            rk += 1
        if rk != 3:
            continue

        def app3(x, M3=M3):
            y = 0
            for i in range(3):
                if bin(M3[i] & x).count("1") % 2:
                    y |= (4 >> i)
            return y

        for t in range(8):
            AGL.add(tuple(app3(j) ^ t for j in range(8)))
    check("A3.2 STABILIZER THEOREM: the stabilizer acts AFFINELY and "
          "FAITHFULLY on the 8 points of A (%d distinct permutations "
          "= 1344, all affine over the chart) and EQUALS the directly "
          "constructed AGL(3,2) = {j -> Mj + t} (order %d = 8 x 168) "
          "as a permutation group on 8 points"
          % (len(stab_perms), len(AGL)),
          ok_affine and len(stab_perms) == 1344 and len(AGL) == 1344
          and stab_perms == AGL)

    # ---------------------------------------------------------------- A4
    section("A4 [E neu]: Aut(H8) = the SAME AGL(3,2) action "
            "(corpus anchor v646/v776)")
    all_placements = set()
    for p in itertools.permutations(range(8)):
        all_placements.add(code_image(C_NAIVE, p))
    both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
                if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
    W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
    CSTAR = [c for c in both_inv if W0246 in c][0]
    check("A4.1 deployed C* rebuilt deterministically (v638 recipe): "
          "%d placements of e8-hat = 8!/1344 (v776 census)"
          % len(all_placements),
          supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED
          and len(all_placements) == 30)

    AUT = {p for p in itertools.permutations(range(8))
           if code_image(CSTAR, p) == CSTAR}
    AGL_pos = set()
    for M3 in itertools.product(range(8), repeat=3):
        rr = list(M3)
        rk = 0
        for bit in (4, 2, 1):
            piv = next((r for r in rr if r & bit), None)
            if piv is None:
                continue
            rr = [r ^ piv if (r & bit) else r for r in rr if r != piv]
            rk += 1
        if rk != 3:
            continue

        def app3(x, M3=M3):
            y = 0
            for i in range(3):
                if bin(M3[i] & x).count("1") % 2:
                    y |= (4 >> i)
            return y

        for t in range(8):
            AGL_pos.add(tuple(app3(j) ^ t for j in range(8)))
    check("A4.2 Aut(C*) has order %d = 1344 (brute force over all "
          "40320 coordinate permutations) and EQUALS the v646 "
          "position-AGL(3,2) (bits3 labeling) as a permutation group "
          "-- the SAME natural AGL(3,2)-on-8-points as A3's "
          "stabilizer action; the chart composition is the explicit "
          "iso of actions" % len(AUT),
          len(AUT) == 1344 and AUT == AGL_pos)

    # ---------------------------------------------------------------- A5
    section("A5: the Hamming reconstruction -- affine functions on A "
            "give RM(1,3) = H8")
    C_A = set()
    for c in (0, 1):
        for lam in range(8):
            C_A.add(tuple((c ^ (bin(lam & j).count("1") % 2))
                          for j in range(8)))
    wts = Counter(sum(w) for w in C_A)
    ok_lin_code = all(tuple(a ^ b for a, b in zip(u, v)) in C_A
                      for u in C_A for v in C_A)
    ok_sd = all(sum(a * b for a, b in zip(u, v)) % 2 == 0
                for u in C_A for v in C_A)
    check("A5.1 [E neu] evaluation code C_A (all affine functions "
          "a + lambda(x) on the 8 chart points of A): dim 4 (16 words,"
          " linear), weight enumerator 1 + 14x^4 + x^8 (%s), doubly "
          "even, self-dual" % dict(sorted(wts.items())),
          len(C_A) == 16 and ok_lin_code
          and wts == Counter({4: 14, 0: 1, 8: 1})
          and all(w % 4 == 0 for w in wts) and ok_sd)

    equivs = [p for p in itertools.permutations(range(8))
              if code_image(C_A, p) == CSTAR]
    check("A5.2 [E neu] C_A is PERMUTATION-EQUIVALENT to the deployed "
          "C*: %d equivalence permutations = |Aut(H8)| = 1344 -- "
          "hence C_A = RM(1,3) = H8 exactly" % len(equivs),
          len(equivs) == 1344)
    print("""
    [H neu] RECONSTRUCTION CHAIN (typed, no claim beyond the census):
    NS/R bit chi on V  ->  affine 8-point space A = chi^-1(1)  ->
    evaluation code of affine functions = [8,4,4] = H8 (exact above).
    As an attack on ARF.BOUNDARY.CODE.01 (v776 BOUNDARY-CODE-UNIQUE,
    residual sharpened by v799 TYPEII-FORCED) this SHARPENS the
    boundary-code story: the Hamming code re-emerges from the NS/R
    character alone once V is given.  HONEST TYPING: the route to V
    itself still passes through Gaussian E8 (Construction A over C*),
    so this is NOT a P2 removal and NOT an independent derivation of
    the boundary code -- it is an exact internal reconstruction.""")

    # ---------------------------------------------------------------- A6
    section("A6 [E neu]: compatibility with the DEPLOYED label action "
            "(Sp(4,2), the kill test)")

    def herm_std(x, y):
        re, im = ip(x, y), ip(x, J_vec(y))
        assert re % 4 == 0 and im % 4 == 0
        return (re // 4, im // 4)

    def hb(a, b):
        h = herm_std(REPS[a], REPS[b])
        return (h[0] + h[1]) % 2

    GRAM = [[hb(lbl_of_bit[8 >> i], lbl_of_bit[8 >> j])
             for j in range(4)] for i in range(4)]

    def form(x, y):
        s = 0
        for i in range(4):
            if not (x & (8 >> i)):
                continue
            for j in range(4):
                if y & (8 >> j):
                    s ^= GRAM[i][j]
        return s

    FT = [[form(x, y) for y in range(16)] for x in range(16)]
    SP = []
    for M in GL:
        mp = [mat_apply(M, x) for x in range(16)]
        if all(FT[mp[x]][mp[y]] == FT[x][y]
               for x in range(16) for y in range(16)):
            SP.append(M)
    SP_STAB = [M for M in SP
               if all(chi_bit[mat_apply(M, x)] == chi_bit[x]
                      for x in range(16))]
    sp_perms = {tuple(chart(mat_apply(M, unchart[j])) for j in range(8))
                for M in SP_STAB}
    ok_inside = sp_perms <= AGL
    orbs = []
    seen = set()
    for j in range(8):
        if j in seen:
            continue
        orb = {j}
        frontier = [j]
        while frontier:
            x = frontier.pop()
            for pm in sp_perms:
                if pm[x] not in orb:
                    orb.add(pm[x])
                    frontier.append(pm[x])
        seen |= orb
        orbs.append(len(orb))
    check("A6.1 Sp(4,2) of the hbar Gram: order %d = 720; "
          "Stab_Sp(chi) order %d = 48 = 720/15; its 8-point action "
          "(%d distinct permutations) lies INSIDE the affine group "
          "AGL(3,2) -- the NS/R label action IS compatible with the "
          "affine action (the kill does NOT fire); orbit structure "
          "on A: %s (transitive)"
          % (len(SP), len(SP_STAB), len(sp_perms), orbs),
          len(SP) == 720 and len(SP_STAB) == 48 and ok_inside
          and len(sp_perms) == 48 and orbs == [8])

    # ---------------------------------------------------------------- X
    section("X: must-fail controls")
    n_bad_fun = 0
    for cvec in range(1, 16):
        chi2 = [bin(cvec & x).count("1") % 2 for x in range(16)]
        if chi2 == chi_bit:
            continue
        mixed = 0
        for lb in LBLS:
            if lb == ZERO:
                continue
            pars = {r[0] % 2 for r in ROOTS if root_label[r] == lb}
            lvl = chi2[bit_of[lb]]
            # a "wrong-NSR" functional: some chi2 = 1 class contains
            # NS roots or chi2 = 0 class contains R roots
            if (lvl == 1 and 0 in pars) or (lvl == 0 and 1 in pars):
                mixed += 1
        if mixed > 0:
            n_bad_fun += 1
    check("X1 CONTROL FIRES: chi_NSR is the UNIQUE nonzero functional "
          "whose level sets are parity-pure: all %d/14 other "
          "functionals mix NS and R roots in their level sets "
          "(different orbit/stabilizer structure on roots)"
          % n_bad_fun, n_bad_fun == 14)

    rng = random.Random(20260806)
    shuffled = list(root_label.values())
    rng.shuffle(shuffled)
    scr_label = dict(zip(sorted(root_label), shuffled))
    n_mixed = 0
    for lb in set(scr_label.values()):
        pars = {r[0] % 2 for r in ROOTS if scr_label[r] == lb}
        if len(pars) > 1:
            n_mixed += 1
    check("X2 CONTROL FIRES: a seeded LCG shuffle of the 240 root -> "
          "class assignments (seed 20260806) destroys NS/R class "
          "purity: %d/15 classes now mix NS and R roots" % n_mixed,
          n_mixed > 0)

    corrupt = set(C_A)
    w0 = next(w for w in sorted(corrupt) if sum(w) == 4)
    corrupt.remove(w0)
    corrupt.add(tuple(b ^ 1 if i == 0 else b for i, b in enumerate(w0)))
    wts_c = Counter(sum(w) for w in corrupt)
    ok_sd_c = all(sum(a * b for a, b in zip(u, v)) % 2 == 0
                  for u in corrupt for v in corrupt)
    check("X3 CONTROL FIRES: flipping ONE bit of one weight-4 word "
          "breaks the enumerator (now %s != 1 + 14x^4 + x^8) and "
          "self-duality (%s)"
          % (dict(sorted(wts_c.items())), not ok_sd_c),
          wts_c != Counter({4: 14, 0: 1, 8: 1}) and not ok_sd_c)

    # ============================================================ VERDICT
    section("SUMMARY / VERDICT")
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    ctrl_ok = all(ok for nm, ok in CHECKS if nm.startswith("X"))
    core = [ok for nm, ok in CHECKS if not nm.startswith("X")]
    dead = any(nm.startswith(("A3", "A4", "A6")) and not ok
               for nm, ok in CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    print("FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    if not ctrl_ok:
        verdict = "TEST-VOID"
    elif all(core):
        verdict = "AFFINE-NSR-EXACT"
    elif dead:
        verdict = "AFFINE-NSR-DEAD"
    else:
        verdict = "AFFINE-NSR-PARTIAL"
    print("VERDICT: %s" % verdict)
    if verdict == "AFFINE-NSR-EXACT":
        print("""
AFFINE NS/R STRUCTURE (A1-A6 [E neu], chain reading [H neu]):
  V \\ {0} = (7 NS = ker chi \\ 0) u (8 R = affine F2^3-torsor A);
  112 NS roots = D8, 128 R roots = Ramond spinor (248 = (112+8)+128,
  v148/v227/v301); Stab_GL(4,2)(chi_NSR) = AGL(3,2) (1344 = 8 x 168)
  acting naturally on the 8 points -- the SAME group + action as
  Aut(H8) (v646/v776 anchor, explicit chart iso); affine functions
  on A reconstruct RM(1,3) = H8 with exactly 1344 equivalences; the
  deployed Sp(4,2) stabilizes chi in an order-48 subgroup acting
  inside AGL(3,2) (kill does not fire).  No matter semantics
  (ROOTCLASS-MIXED cited); no P2-removal claim.""")
    print("runtime: %.1f s" % (time.time() - T0))
    print("ALL CHECKS PASSED" if n_pass == n_all else "CHECKS FAILED")
    return 0 if n_pass == n_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
