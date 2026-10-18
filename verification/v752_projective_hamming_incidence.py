#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v752 -- E8.PROJHAMMING.01: the projective Hamming incidence lemma on V = L/(1+i)L -- the symplectic F2^4 of the unimodular hermitian E8 lattice, B B^T = 4I + 3J exact, K^2 = (4/49) I + (45/49) Pi0, NS/R as a point of the geometry, and the v737 seam-48 distribution derived (PROJ-HAMMING-EXACT).

PROVENANCE: discovery probe projective_hamming_incidence_probe.py (2026-08-04, 36/36 checks, verdict PROJ-HAMMING-EXACT).  Promoted verbatim (no sibling imports; exact integer/Fraction arithmetic; sympy only for the characteristic polynomial); numbers unchanged.  Companion Lean module TfptCarrier/ProjectiveHamming.lean (32 theorems, kernel-checked).

projective_hamming_incidence_probe -- E8.PROJHAMMING.01 (Review-Modul 1):
das PROJEKTIVE HAMMING-INZIDENZLEMMA auf V = L/(1+i)L = F2^4.

FRAGE (externes Review, Modul 1; jede Stufe einzeln geprueft): Die
reduzierte hermitesche Form auf dem bewiesenen Gauss-Quotienten V =
L/(1+i)L = F2^4 (v689: 240 Wurzeln = 15 Klassen x 16, Nullklasse leer)
macht V zu einem symplektischen F2-Raum; die 15 nichttrivialen Klassen
P = V \\ {0} tragen dann die projektive Inzidenzgeometrie PG(3,2), und
die 15 x 15-Inzidenzmatrix B der "Hyperebenen durch y" erfuellt die
EXAKTE Identitaet  B B^T = 4 I + 3 J  (Zeilensummen 7, Singulaerwerte
{7, 2^14}); der normierte Kanal K = B/7 ist der Depolarisations-Kanal
K^2 = (4/49) I + (45/49) Pi0.  Dazu: die NS/R-Paritaet (v722/v738) als
konkreter Punkt y0 der Geometrie (chi = hbar(., y0)) und die 35
natuerlichen 48er-Bloecke (2D-Unterraeume) als Erklaerung der
v737-SEAM48-Inzidenzverteilung.

DIE SIEBEN STUFEN (Review woertlich, bindend):
 (1) hbar wohldefiniert, alternierend (doubly-even), nicht-entartet
     => (V, hbar) symplektisch ueber F2 -- AUS DEM KONKRETEN GITTER:
     h(x,y) = (<x,y> + i <x,Jy>)/2 (v634/v689-Konvention: h(x,x) =
     <x,x>/2 = 2 auf Wurzeln), Reduktion Z[i] -> Z[i]/(1+i) = F2
     via a+bi |-> (a+b) mod 2, EXPLIZIT; Z[i]-Unimodularitaet des
     hermiteschen Gitters (|det| = 1) mitgeprueft; Darboux-Basis
     (Identifikation mit der Standard-Form, fuer Lean dokumentiert).
 (2) |H_y| = 7 fuer alle 15 y in P; |H_y \\cap H_z| = 3 fuer alle
     105 Paare y != z.
 (3) KERN-IDENTITAET: B in {0,1}^{15x15}, B_{xy} = [hbar(x,y) = 0]:
     B B^T = 4 I + 3 J EXAKT; Zeilen-/Spaltensummen 7; B symmetrisch,
     Diagonale 1; charakteristisches Polynom (x-7)(x-2)^9 (x+2)^5,
     also Singulaerwerte {7 (konstanter Vektor), 2 (Multiplizitaet
     14)}; Eigenwerte {7, +2 (x9), -2 (x5)}.
 (4) KANAL: K = B/7: K^2 = (4/49) I + (45/49) Pi0 exakt (Pi0 = J/15);
     doppelt stochastisch, Eintraege >= 0.  EHRLICH: K selbst ist
     NICHT psd (Eigenwerte {1, 2/7, -2/7}); die Depolarisations-Form
     lebt in K^2.
 (5) NS/R-PARITAET: fuer JEDE nichttriviale Linearform chi: 7 Labels
     mit chi = 0, 8 mit chi = 1 => 112 + 128 = 240 Wurzeln; +8 Cartan
     => 248 = 120_NS + 128_R (SO(16)).  Der GEHALT ist WELCHES chi:
     das v722-NS/R-chi ist chi = hbar(., y0) fuer einen konkreten
     sigma-FIXEN Punkt y0 (v738: NS/R = sigma-fixer Paritaets-
     Charakter) -- y0 wird identifiziert (Familien/Anker-Basis,
     Orbitsummen-Struktur).
 (6) DIE 35 NATUERLICHEN 48er-BLOECKE: alle 35 2D-Unterraeume von V
     (je 3 Labels x 16 = 48 Wurzeln); Vergleich mit den 5 sigma-
     Paketen (v736): welche Pakete sind Unterraum-Bloecke, sigma-
     Wirkung auf den 35, Z12-Charaktere der stabilen Bloecke vs
     v623-Tafel; REVIEW-THESE zur SEAM48-ERKLAERUNG: die gemessene
     v737-Verteilung (0:96/1:64/2:64/3:16) folgt aus dem 35er-Design
     -- der zertifizierte Fuenfer-Operator u^4 (v647/v737, bit-
     identisch repliziert) wirkt auf V als freier Ordnung-5-Operator
     mit 3 Label-Orbits x 5; jeder der 48 Fuenferzyklen ueberdeckt
     genau EINEN Label-Orbit bijektiv, die 48 x 5-Matrix ist 16 x
     die 3 x 5-Label-Tafel; ausserdem: ueber u-invariante SPREADS
     (Partitionen von P in 5 Unterraum-Tripel) EXISTIERT die
     Inzidenz-1-Koordinatisierung -- die sigma-Pakete sind nur kein
     Spread (v737-Kill erklaert, nicht revidiert).
 (7) MUST-FAILS: (a) entartete alternierende Form -> B B^T bricht;
     (b) nicht-alternierende Bilinearform (Standard-Skalarprodukt):
     EHRLICHER BEFUND -- B B^T = 4I + 3J haelt fuer JEDE nicht-
     entartete Form (die nackte Identitaet testet nur Nicht-
     Entartung); was bricht, ist der PROJEKTIVE Teil des Lemmas
     (Diagonale 1 / "H_y durch y" / tr B = 15 / Eigenwert-
     Multiplizitaeten (1, 9, 5)); (c) falsche Norm-Konvention
     (h ohne /2 -> hbar = 0): B B^T bricht.  Jede Kontrolle muss
     das VOLLE Lemma brechen.

VERDIKTE (eingefroren): PROJ-HAMMING-EXACT, PROJ-HAMMING-PARTIAL,
PROJ-HAMMING-KILLED, TEST-VOID (Must-fail feuert nicht).

FIREWALL: experiments/-Probe; schreibt nichts; kein verification/-,
Paper-, Ledger- oder Website-Surface beruehrt.  Exakte Ganzzahl/
Fraction-Arithmetik durchgehend; sympy nur fuer das charakteristische
Polynom; numpy nur fuer die G31-Permutationsmaschinerie (Ganzzahl-
Indizes, keine Floats); vollstaendig deterministisch (kein RNG).

Quellen (read-only): v689_gaussian_code_bridge.py (L, J, Klassen),
v634_st31_structure.py (G31, h-Konvention), v722_phys_ramified_ns_r.py
(NS/R-Paritaet), v736_orbit_packet.py (5 Pakete), v737_seam48_
intertwiner.py (zertifizierter Operator, Inzidenzverteilung),
v738_hecke_mod_ramified.py (chi_par sigma-fix).

Lean-Gegenstueck: experiments/lean4-carrier-rigidity/TfptCarrier/
ProjectiveHamming.lean (kernel decide / norm_num, kein sorry /
native_decide; standalone gebaut).
"""

import itertools
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


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ---------------------------------------------------------------- codes
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


# ------------------------------------------------------- linear algebra
def mat_det_inv(rows):
    """exakte Determinante + Inverse (Fractions)."""
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


# --------------------------------------------------------- J und sigma
def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def add_vec(x, y):
    return tuple(a + b for a, b in zip(x, y))


def ip(x, y):
    return sum(a * b for a, b in zip(x, y))


# --------------------------------------------------- Gitter-Maschinerie
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
        assert all(v.denominator == 1 for v in c), "kein Gittervektor"
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
    """v689-I2.6-Rezept: (F1, F2, F3, ANC)-Basis + Bit-Koordinaten."""
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


# ==================================================================== P0
section("P0: der bewiesene v689-Zustand (C*, L, 15 x 16 Klassen, sigma)")

all_placements = set()
for p in itertools.permutations(range(8)):
    all_placements.add(code_image(C_NAIVE, p))
both_inv = [c for c in sorted(all_placements, key=lambda c: sorted(c))
            if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c]
W0246 = tuple(1 if i in (0, 2, 4, 6) else 0 for i in range(8))
CSTAR = [c for c in both_inv if W0246 in c][0]
ROOTS = constrA_roots(CSTAR)
LAT = constrA_lattice(CSTAR)
REPS = label_group(LAT)
ZERO = LAT["label"]((0,) * 8)
root_label = {r: LAT["label"](r) for r in ROOTS}
census = Counter(root_label.values())
check("P0.1 C* deterministisch (v638-Rezept), 240 Wurzeln, 16 Klassen, "
      "Zensus 15 x 16, Nullklasse leer",
      supports_w4(CSTAR) == CSTAR_SUPPORTS_EXPECTED and len(ROOTS) == 240
      and len(REPS) == 16 and len(census) == 15
      and sorted(census.values()) == [16] * 15 and ZERO not in census)


def sig_label(lb):
    return LAT["label"](sig_vec(REPS[lb]))


fixed_nz = [lb for lb in REPS if lb != ZERO and sig_label(lb) == lb]
check("P0.2 sigma-Struktur: sigma^3 = id auf den Labels, 3 fixe Klassen "
      "+ 4 Dreierorbits",
      all(sig_label(sig_label(sig_label(lb))) == lb for lb in REPS)
      and len(fixed_nz) == 3)

FAM, BITS = family_anchor_basis(LAT, REPS, ZERO, sig_label)
F1L, F2L, F3L, ANCL, FSUML = FAM
FAM_VECS = [REPS[F1L], REPS[F2L], REPS[F3L], REPS[ANCL]]
inv_bits = {v: k for k, v in BITS.items()}

# ==================================================================== P1
section("P1: die hermitesche Form h und die Reduktion hbar (Stufe 1)")

B8 = LAT["B"]


def herm(x, y):
    """h(x,y) = (<x,y> + i <x,Jy>)/2 als Paar (Re, Im) in Z[i]."""
    re2, im2 = ip(x, y), ip(x, J_vec(y))
    assert re2 % 2 == 0 and im2 % 2 == 0, "h nicht Z[i]-wertig"
    return (re2 // 2, im2 // 2)


ok_int = ok_lin = ok_conj = True
for bx in B8:
    for by in B8:
        h = herm(bx, by)                       # Integralitaet via assert
        hj = herm(J_vec(bx), by)
        if hj != (-h[1], h[0]):                # h(Jx,y) = i h(x,y)
            ok_lin = False
        hc = herm(by, bx)
        if hc != (h[0], -h[1]):                # h(y,x) = conj h(x,y)
            ok_conj = False
ok_root_norm = all(herm(r, r) == (2, 0) for r in ROOTS)
check("P1.1 h Z[i]-wertig auf allen 64 Basis-Paaren, h(Jx,y) = i h(x,y), "
      "h(y,x) = conj h(x,y); h(r,r) = <r,r>/2 = 2 auf allen 240 Wurzeln "
      "(v634/v689-Konvention)",
      ok_int and ok_lin and ok_conj and ok_root_norm)

ok_de = all(sum(c) % 4 == 0 for c in CSTAR)
ok_norm4 = all(ip(b, b) % 4 == 0 for b in B8)
ok_hxx = all(herm(REPS[lb], REPS[lb])[0] % 2 == 0
             and herm(REPS[lb], REPS[lb])[1] == 0 for lb in REPS)
check("P1.2 doubly-even: alle 16 Codeworte von C* haben Gewicht 0 mod 4, "
      "alle Basisnormen in 4Z => h(x,x) = <x,x>/2 in 2Z (auf allen 16 "
      "Repraesentanten geprueft); 2 = -i(1+i)^2, also h(x,x) = 0 mod "
      "(1+i): hbar ist ALTERNIEREND via doubly-even",
      ok_de and ok_norm4 and ok_hxx)

# Z[i]-Basis {b_i} mit {b_i, J b_i} Z-Basis von L; hermitesche Gram-Det
zbasis = None
for sub in itertools.combinations(range(8), 4):
    rows = []
    for k in sub:
        rows.append(B8[k])
        rows.append(J_vec(B8[k]))
    det, _ = mat_det_inv(rows)
    if abs(det) == 16:                # = |det L-Basis| => Z-Basis von L
        zbasis = [B8[k] for k in sub]
        break
assert zbasis is not None
H4 = [[herm(bi, bj) for bj in zbasis] for bi in zbasis]


def zi_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def zi_det4(M):
    det = (0, 0)
    for perm in itertools.permutations(range(4)):
        sign = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sign = -sign
        t = (sign, 0)
        for i in range(4):
            t = zi_mul(t, M[i][perm[i]])
        det = (det[0] + t[0], det[1] + t[1])
    return det


detH = zi_det4(H4)
check("P1.3 Z[i]-UNIMODULAR: Z[i]-Basis gefunden ({b, Jb} hat |det| = 16 "
      "= [Z^8 : L]-Kovolumen), hermitesche 4x4-Gram-Determinante = "
      "%s + %si, |det|^2 = %d = 1 (Einheit): (L, h) ist das unimodulare "
      "hermitesche E8-Gitter ueber Z[i]"
      % (detH[0], detH[1], detH[0] ** 2 + detH[1] ** 2),
      detH[0] ** 2 + detH[1] ** 2 == 1)


def hbar_vec(x, y):
    """hbar: Z[i]/(1+i) = F2, a+bi |-> (a+b) mod 2."""
    h = herm(x, y)
    return (h[0] + h[1]) % 2


ok_wd = True
for lx in REPS:
    x = REPS[lx]
    for b in B8:
        sh = add_vec(b, J_vec(b))              # (1+i) b
        xs = add_vec(x, sh)
        for ly in REPS:
            y = REPS[ly]
            if hbar_vec(xs, y) != hbar_vec(x, y):
                ok_wd = False
            if hbar_vec(y, xs) != hbar_vec(y, x):
                ok_wd = False
check("P1.4 hbar WOHLDEFINIERT auf V: Verschieben eines Arguments um "
      "(1+i)b aendert hbar nicht (alle 16 Reps x 8 Basisshifts x 16 "
      "Partner x beide Slots = 4096 exakte Tests; konzeptionell: "
      "h((1+i)a, y) = (1+i)h(a,y), h(x, (1+i)b) = (1-i)h(x,b), beide "
      "in (1+i)Z[i])", ok_wd)

GFAM = [[hbar_vec(FAM_VECS[i], FAM_VECS[j]) for j in range(4)]
        for i in range(4)]
print("    Gram-Matrix von hbar in der Familien/Anker-Basis "
      "(F1, F2, F3, ANC):")
for row in GFAM:
    print("      %s" % (row,))


def gform(G, a, b):
    return sum(a[i] * G[i][j] * b[j] for i in range(4)
               for j in range(4)) % 2


ok_repr = all(hbar_vec(REPS[lx], REPS[ly])
              == gform(GFAM, BITS[lx], BITS[ly])
              for lx in REPS for ly in REPS)
kernel = [lb for lb in REPS
          if all(hbar_vec(REPS[lb], REPS[ly]) == 0 for ly in REPS)]
ok_alt = all(GFAM[i][i] == 0 for i in range(4))
ok_sym = all(GFAM[i][j] == GFAM[j][i] for i in range(4) for j in range(4))
check("P1.5 hbar = Bilinearform der Gram-Matrix (alle 256 Label-Paare), "
      "alternierend (Diagonale 0), symmetrisch, NICHT-ENTARTET (Kern = "
      "{0}: %d Kern-Label) => (V, hbar) ist symplektisch ueber F2"
      % len(kernel),
      ok_repr and ok_alt and ok_sym and kernel == [ZERO])

# Darboux-Basis: hbar ~ Standard-Form (Klassifikation, fuer Lean)
GSTD = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
E4 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
NZ16 = [b for b in itertools.product((0, 1), repeat=4) if any(b)]
e1 = NZ16[0]
f1 = next(v for v in NZ16 if gform(GFAM, e1, v) == 1)
perp = [v for v in NZ16
        if gform(GFAM, e1, v) == 0 and gform(GFAM, f1, v) == 0]
e2 = perp[0]
f2 = next(v for v in perp if gform(GFAM, e2, v) == 1)
P4 = [[e1[i], f1[i], e2[i], f2[i]] for i in range(4)]  # Spalten e1,f1,e2,f2
PtGP = [[sum(P4[a][i] * GFAM[a][b] * P4[b][j]
             for a in range(4) for b in range(4)) % 2
         for j in range(4)] for i in range(4)]
detP, _ = mat_det_inv(P4)
ok_sig_h = all(hbar_vec(sig_vec(REPS[lx]), sig_vec(REPS[ly]))
               == hbar_vec(REPS[lx], REPS[ly])
               for lx in REPS for ly in REPS)
print("    Darboux-Basis (Spalten von P, Fam-Koordinaten): e1=%s f1=%s "
      "e2=%s f2=%s" % (e1, f1, e2, f2))
check("P1.6 DARBOUX/KLASSIFIKATION: explizites P mit P^T G P = "
      "Standard-Symplektik [[0,1],[1,0]] + [[0,1],[1,0]], P invertierbar "
      "(det ungerade: %s) -- jede nicht-entartete alternierende Form auf "
      "F2^4 ist zur Standard-Form aequivalent (Lean-Identifikation); "
      "sigma erhaelt hbar (alle 256 Paare)"
      % detP,
      PtGP == GSTD and int(detP) % 2 == 1 and ok_sig_h)

# ==================================================================== P2
section("P2: |H_y| = 7 und |H_y ^ H_z| = 3 (Stufe 2)")

POINTS = sorted(lb for lb in REPS if lb != ZERO)
HPL = {y: frozenset(x for x in POINTS if hbar_vec(REPS[x], REPS[y]) == 0)
       for y in POINTS}
sizes = sorted(len(HPL[y]) for y in POINTS)
check("P2.1 |H_y| = 7 fuer ALLE 15 Punkte y in P (H_y = Hyperebene durch "
      "y, da hbar(y,y) = 0): Groessen %s"
      % dict(Counter(sizes)), sizes == [7] * 15)

pair_sizes = sorted(len(HPL[y] & HPL[z])
                    for y, z in itertools.combinations(POINTS, 2))
check("P2.2 |H_y ^ H_z| = 3 fuer ALLE 105 Paare y != z: Groessen %s "
      "(= Gerade der PG(3,2)-Geometrie: Schnitt zweier Hyperebenen "
      "minus 0)" % dict(Counter(pair_sizes)),
      pair_sizes == [3] * 105)

# ==================================================================== P3
section("P3: die Kern-Identitaet B B^T = 4 I + 3 J (Stufe 3)")

B15 = [[1 if hbar_vec(REPS[x], REPS[y]) == 0 else 0 for y in POINTS]
       for x in POINTS]
ok_symm = all(B15[i][j] == B15[j][i] for i in range(15) for j in range(15))
ok_diag = all(B15[i][i] == 1 for i in range(15))
rowsums = [sum(row) for row in B15]
colsums = [sum(B15[i][j] for i in range(15)) for j in range(15)]
check("P3.1 B symmetrisch, Diagonale 1 (hbar alternierend), Zeilen- und "
      "Spaltensummen alle 7",
      ok_symm and ok_diag and rowsums == [7] * 15 and colsums == [7] * 15)

BBt = [[sum(B15[i][k] * B15[j][k] for k in range(15)) for j in range(15)]
       for i in range(15)]
TARGET = [[4 + 3 if i == j else 3 for j in range(15)] for i in range(15)]
check("P3.2 KERN-IDENTITAET: B B^T = 4 I + 3 J EXAKT (alle 225 "
      "Eintraege; Diagonale 7 = 4 + 3, ausserdiagonal 3)",
      BBt == TARGET)

from sympy import Matrix, symbols, expand, Poly            # noqa: E402
xs = symbols("x")
cp = Matrix(B15).charpoly(xs).as_expr()
cp_target = expand((xs - 7) * (xs - 2) ** 9 * (xs + 2) ** 5)
ones15 = [1] * 15
B_ones = [sum(B15[i][j] * ones15[j] for j in range(15)) for i in range(15)]
trB = sum(B15[i][i] for i in range(15))
trB2 = sum(BBt[i][i] for i in range(15))
check("P3.3 SPEKTRUM exakt: char. Polynom = (x-7)(x-2)^9(x+2)^5 (%s); "
      "B 1 = 7 1 (konstanter Vektor); tr B = %d = 7+2*9-2*5, tr B^2 = %d "
      "= 49+4*14 => SINGULAERWERTE {7 (x1, konstanter Vektor), "
      "2 (x14)}, Eigenwerte {7, +2 (x9), -2 (x5)}"
      % (expand(cp - cp_target) == 0, trB, trB2),
      expand(cp - cp_target) == 0 and B_ones == [7] * 15
      and trB == 15 and trB2 == 105)

# ==================================================================== P4
section("P4: der Kanal K = B/7 (Stufe 4)")

K = [[Fr(B15[i][j], 7) for j in range(15)] for i in range(15)]
K2 = [[sum(K[i][k] * K[k][j] for k in range(15)) for j in range(15)]
      for i in range(15)]
PI0 = [[Fr(1, 15) for _ in range(15)] for _ in range(15)]
K2_target = [[Fr(4, 49) * (1 if i == j else 0) + Fr(45, 49) * PI0[i][j]
              for j in range(15)] for i in range(15)]
check("P4.1 K^2 = (4/49) I + (45/49) Pi0 EXAKT (Pi0 = J/15; alle 225 "
      "Eintraege in exakter Fraction-Arithmetik): Diagonale %s, "
      "ausserdiagonal %s"
      % (K2[0][0], K2[0][1]), K2 == K2_target)

ok_stoch = (all(sum(row) == 1 for row in K)
            and all(sum(K[i][j] for i in range(15)) == 1
                    for j in range(15)))
ok_pos = all(K[i][j] >= 0 for i in range(15) for j in range(15))
check("P4.2 K doppelt stochastisch, Eintraege >= 0 (Werte {0, 1/7}); "
      "EHRLICH: K selbst hat Eigenwerte {1, +2/7 (x9), -2/7 (x5)} und "
      "ist NICHT psd -- die Depolarisations-Form (4/49) I + (45/49) Pi0 "
      "ist die Aussage ueber K^2, nicht ueber K",
      ok_stoch and ok_pos)

# ==================================================================== P5
section("P5: NS/R-Paritaet als Punkt der Geometrie (Stufe 5)")

# Standardmodell (verdoppelte Koordinaten), v689-I5 / v722-Rahmen

def in_E8_std(x):
    par = {v % 2 for v in x}
    return len(par) == 1 and sum(x) % 4 == 0


B_STD = [(4, 0, 0, 0, 0, 0, 0, 0),
         (-2, 2, 0, 0, 0, 0, 0, 0),
         (0, -2, 2, 0, 0, 0, 0, 0),
         (0, 0, -2, 2, 0, 0, 0, 0),
         (0, 0, 0, -2, 2, 0, 0, 0),
         (0, 0, 0, 0, -2, 2, 0, 0),
         (0, 0, 0, 0, 0, -2, 2, 0),
         (1, 1, 1, 1, 1, 1, 1, 1)]
LATS = make_lattice(in_E8_std, list(B_STD))
ZEROS = LATS["label"]((0,) * 8)
roots_std = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        roots_std.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        roots_std.append(v)
REPS_S = label_group(LATS)
rl_std = {r: LATS["label"](r) for r in roots_std}
census_s = Counter(rl_std.values())


def parity(w):
    return w[0] % 2                      # 0 = integer/NS, 1 = spinor/R


class_par = {}
pure = True
for r, lb in rl_std.items():
    p = parity(r)
    if lb in class_par and class_par[lb] != p:
        pure = False
    class_par[lb] = p
ns_cls = [lb for lb in class_par if class_par[lb] == 0]
r_cls = [lb for lb in class_par if class_par[lb] == 1]
check("P5.1 Standardmodell-Zensus 15 x 16 re-etabliert; NS/R-PURITAET "
      "pro Klasse; 7 NS-Klassen (112 Wurzeln) + 8 R-Klassen (128 "
      "Wurzeln) -- v722 re-deriviert",
      len(census_s) == 15 and sorted(census_s.values()) == [16] * 15
      and ZEROS not in census_s and pure
      and len(ns_cls) == 7 and len(r_cls) == 8)

chi = {lb: parity(REPS_S[lb]) % 2 for lb in REPS_S}
ok_chi_class = all(chi[lb] == class_par[lb] for lb in class_par)
ok_hom = all(chi[LATS["label"](add_vec(REPS_S[a], REPS_S[b]))]
             == (chi[a] + chi[b]) % 2 for a in REPS_S for b in REPS_S)


def sig_label_s(lb):
    return LATS["label"](sig_vec(REPS_S[lb]))


ok_sig_chi = all(chi[sig_label_s(lb)] == chi[lb] for lb in REPS_S)
check("P5.2 chi_NSR ist eine LINEARFORM auf V (Homomorphismus, alle 256 "
      "Paare) und SIGMA-INVARIANT (chi o sigma = chi) -- v738-Abgleich: "
      "NS/R = der sigma-fixe Paritaets-Charakter",
      ok_chi_class and ok_hom and ok_sig_chi)


def herm_std(w, v):
    re4, im4 = ip(w, v), ip(w, J_vec(v))
    assert re4 % 4 == 0 and im4 % 4 == 0
    return (re4 // 4, im4 // 4)


def hbar_std(w, v):
    h = herm_std(w, v)
    return (h[0] + h[1]) % 2


y0 = [lb for lb in REPS_S if lb != ZEROS
      and all(hbar_std(REPS_S[lx], REPS_S[lb]) == chi[lx]
              for lx in REPS_S)]
fixed_s = [lb for lb in REPS_S if lb != ZEROS and sig_label_s(lb) == lb]
FAM_S, BITS_S = family_anchor_basis(LATS, REPS_S, ZEROS, sig_label_s)
F1S, F2S, F3S, ANCS, FSUMS = FAM_S
y0_lb = y0[0] if y0 else None
y0_name = None
if y0_lb is not None:
    y0_name = ("FSUM (Summe der Familien-Klassen = Koordinatenklasse)"
               if y0_lb == FSUMS else
               "ANC (Anker-Klasse)" if y0_lb == ANCS else
               "ANC + FSUM" if BITS_S[y0_lb] == (1, 1, 1, 1) else
               "NICHT sigma-fix")
chi_coeff = tuple(chi[lb] for lb in (F1S, F2S, F3S, ANCS))
check("P5.3 chi_NSR = hbar(., y0) fuer EINEN eindeutigen Punkt y0 der "
      "Geometrie (Nicht-Entartung): %d Loesung(en); y0 ist SIGMA-FIX "
      "(%s); y0 = %s; chi-Koeffizienten in der (F1,F2,F3,ANC)-Basis: "
      "%s; y0-Bits: %s"
      % (len(y0), y0_lb in fixed_s if y0_lb else "-", y0_name,
         chi_coeff, BITS_S[y0_lb] if y0_lb else "-"),
      len(y0) == 1 and y0_lb in fixed_s)

# Orbitsummen-Struktur: die 4 bewegten Orbits summieren auf {0} u T
orbits_s = []
seen = set()
for lb in sorted(REPS_S):
    if lb == ZEROS or lb in seen or sig_label_s(lb) == lb:
        continue
    o = (lb, sig_label_s(lb), sig_label_s(sig_label_s(lb)))
    seen |= set(o)
    orbits_s.append(o)
orb_sums = [LATS["label"](add_vec(add_vec(REPS_S[o[0]], REPS_S[o[1]]),
                                  REPS_S[o[2]])) for o in orbits_s]
sum_set = sorted(orb_sums)
expected_sums = sorted([ZEROS] + fixed_s)
print("    Orbitsummen der 4 bewegten Dreierorbits (Bits): %s"
      % [BITS_S[s] for s in orb_sums])
check("P5.4 ORBITSUMMEN-STRUKTUR: die 4 bewegten Orbits summieren "
      "BIJEKTIV auf {0} + die 3 sigma-fixen Labels (jeder fixe Punkt "
      "ist Summe genau EINES bewegten Orbits; einer summiert auf 0 -- "
      "d.h. genau ein bewegtes Paket ist selbst ein 2D-Unterraum)",
      sum_set == expected_sums and len(set(orb_sums)) == 4)

n_zero_chi = sum(1 for lb in REPS_S if lb != ZEROS and chi[lb] == 0)
n_one_chi = sum(1 for lb in REPS_S if chi[lb] == 1)
generic = all(
    (sum(1 for lb in REPS_S if lb != ZEROS
         and hbar_std(REPS_S[lb], REPS_S[ly]) == 0) == 7
     and sum(1 for lb in REPS_S
             if hbar_std(REPS_S[lb], REPS_S[ly]) == 1) == 8)
    for ly in REPS_S if ly != ZEROS)
check("P5.5 7/8-ZAEHLUNG: chi_NSR hat 7 Kern-Labels + 8 chi=1-Labels; "
      "GENERISCH fuer jede nichttriviale Linearform (alle 15 geprueft) "
      "-- der Gehalt von Stufe 5 ist WELCHES chi (P5.3), nicht die "
      "Zaehlung; 7*16 = 112 NS + 8*16 = 128 R = 240; +8 Cartan (NS): "
      "120 + 128 = 248 = dim E8 (SO(16)-Zerlegung)",
      n_zero_chi == 7 and n_one_chi == 8 and generic
      and 7 * 16 == 112 and 8 * 16 == 128 and 112 + 128 == 240
      and 112 + 8 == 120 and 120 + 128 == 248)

# ==================================================================== P6
section("P6: die 35 natuerlichen 48er-Bloecke und die SEAM48-Erklaerung "
        "(Stufe 6)")

# Label-Addition im Standardmodell
LBL_S = sorted(REPS_S)
addtab = {(a, b): LATS["label"](add_vec(REPS_S[a], REPS_S[b]))
          for a in LBL_S for b in LBL_S}
POINTS_S = [lb for lb in LBL_S if lb != ZEROS]
subspaces = set()
for a, b in itertools.combinations(POINTS_S, 2):
    c = addtab[(a, b)]
    subspaces.add(frozenset({a, b, c}))
subspaces = sorted(subspaces, key=lambda s: sorted(s))
blk_roots = {W: sum(census_s[lb] for lb in W) for W in subspaces}
check("P6.1 ALLE 35 zweidimensionalen Unterraeume von V erzeugt "
      "(Tripel {a, b, a+b}); jeder traegt 3 x 16 = 48 Wurzeln: %d "
      "Unterraeume, Blockgroessen %s"
      % (len(subspaces), sorted(set(blk_roots.values()))),
      len(subspaces) == 35 and all(v == 48 for v in blk_roots.values()))

# die 5 sigma-Pakete (v736): Fixtripel + 4 Orbittripel
T_fix = frozenset(fixed_s)
packet_triples = [T_fix] + [frozenset(o) for o in orbits_s]
is_sub = [t in set(subspaces) for t in packet_triples]
check("P6.2 sigma-PAKETE vs UNTERRAEUME: das Fixtripel T ist ein "
      "2D-Unterraum (%s); von den 4 bewegten Orbittripeln ist GENAU "
      "EINES ein Unterraum (%s -- das Orbit mit Summe 0, P5.4); die "
      "anderen drei sind KEINE Unterraeume: nur 2 der 5 v736-Pakete "
      "sind Bloecke des 35er-Designs"
      % (is_sub[0], [is_sub[k] for k in range(1, 5)]),
      is_sub[0] and sum(is_sub[1:]) == 1)

# sigma-Wirkung auf den 35 (c wirkt auf V wie sigma, da Jbar = id)
ok_Jbar = all(rl_std[tuple(int(a) for a in J_vec(r))] == rl_std[r]
              for r in roots_std)


def sig_sub(W):
    return frozenset(sig_label_s(lb) for lb in W)


stable35 = [W for W in subspaces if sig_sub(W) == W]
seen_w = set()
orb35 = Counter()
for W in subspaces:
    if W in seen_w:
        continue
    o = {W, sig_sub(W), sig_sub(sig_sub(W))}
    seen_w |= o
    orb35[len(o)] += 1
check("P6.3a Jbar = id auf V ((i-1) = i(1+i)), also cbar = sigmabar; "
      "sigma-Wirkung auf den 35 Unterraeumen: %d stabil, Orbit-Zensus "
      "%s" % (len(stable35), dict(sorted(orb35.items()))),
      ok_Jbar and len(stable35) + 3 * orb35[3] == 35)

# Z12-Charaktere: c-stabile Unterraum-Bloecke vs v623-Tafel [48,0,...,0]
cl_map = {r: tuple(int(a) for a in J_vec(sig_vec(r))) for r in roots_std}
root_list = sorted(roots_std)
ridx_s = {r: k for k, r in enumerate(root_list)}
cperm_s = [ridx_s[cl_map[r]] for r in root_list]


def fix_vector(block_idx):
    pos = {j: k for k, j in enumerate(block_idx)}
    pb = [pos[cperm_s[j]] for j in block_idx]
    out = []
    cur = list(range(len(pb)))
    for _ in range(12):
        out.append(sum(1 for i, x in enumerate(cur) if i == x))
        cur = [pb[x] for x in cur]
    return out


F623 = [48] + [0] * 11
class_idx = {}
for r in root_list:
    class_idx.setdefault(rl_std[r], []).append(ridx_s[r])
fixvecs = {}
for W in stable35:
    idxs = sorted(i for lb in W for i in class_idx[lb])
    if all(cperm_s[j] in set(idxs) for j in idxs):
        fixvecs[W] = fix_vector(idxs)
n_match = sum(1 for v in fixvecs.values() if v == F623)
dev = {tuple(v) for v in fixvecs.values() if v != F623}
print("    Z12-Fixvektoren der %d c-stabilen Unterraum-Bloecke: %d x "
      "v623-Tafel %s, Abweichler: %s"
      % (len(fixvecs), n_match, F623,
         [list(d) for d in dev] if dev else "keine"))
T_fixvec = fixvecs.get(T_fix)
check("P6.3b CHARAKTER-VERGLEICH: alle c-stabilen Unterraum-Bloecke "
      "tragen eine Z12-Tafel; das Fixtripel T traegt %s (v737: der "
      "Fixblock weicht exakt um die 12 gelifteten Marken ab, die "
      "bewegten Bloecke tragen die v623-Tafel %s)"
      % (T_fixvec, F623),
      len(fixvecs) >= 1 and T_fixvec is not None)

# ---- der zertifizierte Operator u (v647/v737, bit-identisch) ---------
print("    baue G31 (BFS ueber die 60 unitaeren Spiegelungen, v737-"
      "identisch) ...", flush=True)
N240 = 240
RD = np.array(root_list, dtype=np.int64)
ridx_np = {tuple(int(a) for a in RD[i]): i for i in range(N240)}


def J_vec_np(x):
    out = np.empty_like(x)
    out[0::2] = -x[1::2]
    out[1::2] = x[0::2]
    return out


Jperm = np.array([ridx_np[tuple(int(a) for a in J_vec_np(RD[i]))]
                  for i in range(N240)], dtype=np.int16)
sigperm = np.array([ridx_np[tuple(int(a) for a in RD[i][[4, 5, 0, 1,
                                                         2, 3, 6, 7]])]
                    for i in range(N240)], dtype=np.int16)
IDP = np.arange(N240, dtype=np.int16)
JRD = np.array([J_vec_np(RD[i]) for i in range(N240)], dtype=np.int64)

line_of_np = np.full(N240, -1, dtype=np.int32)
line_reps = []
for i in range(N240):
    if line_of_np[i] >= 0:
        continue
    orb = [i, int(Jperm[i]), int(Jperm[Jperm[i]]),
           int(Jperm[Jperm[Jperm[i]]])]
    for j in orb:
        line_of_np[j] = len(line_reps)
    line_reps.append(i)

refl_perms = []
for a in range(60):
    vi = line_reps[a]
    re4 = RD @ RD[vi]
    im4 = RD @ JRD[vi]
    re, im = re4 // 4, im4 // 4
    Y = RD - re[:, None] * RD[vi][None, :] - im[:, None] * JRD[vi][None, :]
    refl_perms.append(np.array([ridx_np[tuple(int(t) for t in Y[i])]
                                for i in range(N240)], dtype=np.int16))

t_bfs = time.time()
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
Eall = np.stack(list(Gset.values()))
check("P6.4a |G31| = %d = 46080 (BFS %.1f s)"
      % (len(Gset), time.time() - t_bfs), len(Gset) == 46080)

from math import lcm                                        # noqa: E402


def census_order(p):
    pl = p.tolist()
    seen_b = bytearray(N240)
    cen = {}
    for s in range(N240):
        if seen_b[s]:
            continue
        ln, j = 0, s
        while not seen_b[j]:
            seen_b[j] = 1
            j = pl[j]
            ln += 1
        cen[ln] = cen.get(ln, 0) + 1
    o = 1
    for L in cen:
        o = lcm(o, L)
    return cen, o


t_cls = time.time()
rows20 = []
for i in range(len(Eall)):
    cen, o = census_order(Eall[i])
    if o == 20 and cen == {20: 12}:
        rows20.append(i)
print("    Zensus-Pass ueber 46080 Elemente: %.1f s, %d regulaere "
      "Ordnung-20-Elemente" % (time.time() - t_cls, len(rows20)),
      flush=True)
u = Eall[rows20[0]]                       # v647/v737: ERSTES Element


def perm_power(p, k):
    r = IDP
    b = p
    while k:
        if k & 1:
            r = b[r]
        b = b[b]
        k >>= 1
    return r


u5 = perm_power(u, 5)
J3 = Jperm[Jperm[Jperm]]
u4 = perm_power(u, 4)
cen4, o4 = census_order(u4)
check("P6.4b zertifizierter Zeuge u = reg20[0] (v647-Reihenfolge, keine "
      "Neuwahl): u^5 = %s (zentral), Fuenfer-Operator u^4 frei mit "
      "Zensus %s"
      % ("J" if np.array_equal(u5, Jperm)
         else "J^3" if np.array_equal(u5, J3) else "ANDERS", cen4),
      (np.array_equal(u5, Jperm) or np.array_equal(u5, J3))
      and o4 == 5 and cen4 == {5: 48})

# ubar: die induzierte Wirkung von u^4 auf den 15 Labels
lab_arr = [rl_std[r] for r in root_list]
ubar = {}
ok_ubar = True
for i in range(N240):
    src, dst = lab_arr[i], lab_arr[int(u4[i])]
    if src in ubar and ubar[src] != dst:
        ok_ubar = False
    ubar[src] = dst
ub_orbits = []
seen_l = set()
for lb in POINTS_S:
    if lb in seen_l:
        continue
    o = [lb]
    x = ubar[lb]
    while x != lb:
        o.append(x)
        x = ubar[x]
    seen_l |= set(o)
    ub_orbits.append(o)
check("P6.5a ubar = u^4 mod (1+i) WOHLDEFINIERT auf den Labels (alle "
      "240 Wurzeln), FREI von Ordnung 5: %d Label-Orbits der Groessen %s "
      "(ubar^5 = ubar von J = id)"
      % (len(ub_orbits), sorted(len(o) for o in ub_orbits)),
      ok_ubar and sorted(len(o) for o in ub_orbits) == [5, 5, 5])

# 48 Fuenferzyklen von u^4 und ihre Label-Fenster
u4l = u4.tolist()
seen_c = bytearray(N240)
cycles = []
for i in range(N240):
    if seen_c[i]:
        continue
    cyc = [i]
    j = u4l[i]
    while j != i:
        cyc.append(j)
        j = u4l[j]
    for j2 in cyc:
        seen_c[j2] = 1
    cycles.append(cyc)
ok_biject = all(len({lab_arr[j] for j in cyc}) == 5 for cyc in cycles)
orb_of_cycle = []
orb_index = {frozenset(o): k for k, o in enumerate(ub_orbits)}
for cyc in cycles:
    orb_of_cycle.append(orb_index[frozenset(lab_arr[j] for j in cyc)])
cyc_per_orbit = Counter(orb_of_cycle)
check("P6.5b jeder der 48 Fuenferzyklen ueberdeckt genau EINEN "
      "ubar-Label-Orbit BIJEKTIV (5 verschiedene Labels); Zyklen pro "
      "Orbit: %s = 16 je Orbit (80 Wurzeln / Orbit)"
      % dict(sorted(cyc_per_orbit.items())),
      len(cycles) == 48 and ok_biject
      and sorted(cyc_per_orbit.values()) == [16, 16, 16])

# Label-Tafel T (3 Orbits x 5 Pakete) und die abgeleitete Verteilung
Tlab = [[len(set(o) & t) for t in packet_triples] for o in ub_orbits]
print("    Label-Tafel |Orbit ^ Paket| (Zeilen = 3 ubar-Orbits, Spalten "
      "= [T_fix, O1..O4]):")
for row in Tlab:
    print("      %s" % (row,))
derived = Counter()
for row in Tlab:
    for e in row:
        derived[e] += 16
# direkte v737-Inzidenz (Zyklus x Paket) zum Abgleich
packet_of = {}
for k, t in enumerate(packet_triples):
    for lb in t:
        packet_of[lb] = k
INC = Counter()
for cyc in cycles:
    row = [0] * 5
    for j in cyc:
        row[packet_of[lab_arr[j]]] += 1
    for e in row:
        INC[e] += 1
V737 = {0: 96, 1: 64, 2: 64, 3: 16}
check("P6.5c SEAM48-VERTEILUNG ABGELEITET: 48 x 5-Inzidenz = 16 x die "
      "3 x 5-Label-Tafel; abgeleitet %s = direkt gemessen %s = v737 "
      "EXAKT %s -- die Verteilung ist reine Label-Geometrie "
      "(Fuenferzyklen sehen ubar-Orbits, nicht sigma-Pakete)"
      % (dict(sorted(derived.items())), dict(sorted(INC.items())), V737),
      dict(derived) == V737 and dict(INC) == V737)

# Strukturaussage (EHRLICH, gemessen): NICHT das Fixtripel traegt den
# 3:16-Eintrag -- die Review-Vermutung "T ganz in einem Orbit" ist
# FALSIFIZIERT.  Gemessen liegt genau EIN Paket-Tripel ganz in einem
# ubar-Orbit, und zwar das BEWEGTE Orbit mit Orbitsumme FSUM = y0 (das
# Familien-Paket, dessen Summe der NS/R-Punkt ist); T_fix und die drei
# anderen bewegten Tripel schneiden die Orbits (2,1,0).
profiles = [tuple(sorted((Tlab[a][p] for a in range(3)), reverse=True))
            for p in range(5)]
whole = [p for p in range(5) if profiles[p] == (3, 0, 0)]
entry_multiset = Counter(e for row in Tlab for e in row)
whole_is_family = (len(whole) == 1 and whole[0] >= 1
                   and orb_sums[whole[0] - 1] == FSUMS
                   and y0_lb == FSUMS)
check("P6.5d STRUKTUR (gemessen, Review-Vermutung korrigiert): genau "
      "EIN Paket-Tripel liegt ganz in einem ubar-Orbit -- NICHT das "
      "Fixtripel T (Profil %s), sondern das bewegte Orbit mit "
      "Orbitsumme FSUM = y0 (Paket %d, Profile %s); alle anderen "
      "Tripel schneiden (2,1,0); Label-Multiset %s = 0:6/1:4/2:4/3:1, "
      "x16 = die v737-Verteilung"
      % (profiles[0], whole[0] if whole else -1, profiles,
         dict(sorted(entry_multiset.items()))),
      len(whole) == 1 and whole_is_family
      and profiles[0] == (2, 1, 0)
      and all(profiles[p] == (2, 1, 0) for p in range(5)
              if p != whole[0])
      and dict(entry_multiset) == {0: 6, 1: 4, 2: 4, 3: 1})

# Spreads: Partitionen von P in 5 Unterraum-Tripel
sub_list = subspaces
by_label = {}
for W in sub_list:
    for lb in W:
        by_label.setdefault(lb, []).append(W)


def find_spreads(covered, used):
    if len(covered) == 15:
        return [frozenset(used)]
    lb = next(l for l in POINTS_S if l not in covered)
    out = []
    for W in by_label[lb]:
        if covered & W:
            continue
        out += find_spreads(covered | W, used + [W])
    return out


spreads = sorted(set(find_spreads(frozenset(), [])),
                 key=lambda s: sorted(sorted(w) for w in s))
check("P6.6a SPREADS: genau %d Partitionen von P in 5 disjunkte "
      "2D-Unterraum-Tripel (PG(3,2)-Klassik: 56)"
      % len(spreads), len(spreads) == 56)


def ubar_sub(W):
    return frozenset(ubar[lb] for lb in W)


inv_spreads = [S for S in spreads
               if {ubar_sub(W) for W in S} == set(S)]
all1_spreads = [S for S in spreads
                if all(len(set(o) & W) == 1
                       for o in ub_orbits for W in S)]
sig_stable_spreads = [S for S in inv_spreads
                      if {sig_sub(W) for W in S} == set(S)]
packet_set = set(packet_triples)
overlap = [sorted(len(set(S) & packet_set) for S in inv_spreads)]
check("P6.6b REVIEW-THESE BESTAETIGT: %d der 56 Spreads sind "
      "ubar-invariant, und GENAU diese haben die Inzidenz-1-Eigenschaft "
      "(alle 3 Orbits treffen jedes Spread-Tripel genau einmal): all-1 "
      "= %d Spreads, Mengen identisch %s -- ueber 2D-UNTERRAUM-Spreads "
      "EXISTIERT die 5 x 48-Koordinatisierung, die v737 mit den "
      "sigma-Paketen nicht fand"
      % (len(inv_spreads), len(all1_spreads),
         set(inv_spreads) == set(all1_spreads)),
      len(inv_spreads) >= 1
      and set(inv_spreads) == set(all1_spreads))

# Wurzel-Ebene: erster invarianter Spread -> 48 x 5 exakt alle 1
S0 = sorted(inv_spreads, key=lambda s: sorted(sorted(w) for w in s))[0]
S0_list = sorted(S0, key=sorted)
blk_of_lb = {}
for k, W in enumerate(S0_list):
    for lb in W:
        blk_of_lb[lb] = k
inc_root = Counter()
for cyc in cycles:
    row = [0] * 5
    for j in cyc:
        row[blk_of_lb[lab_arr[j]]] += 1
    for e in row:
        inc_root[e] += 1
n_pack_in_S0 = len(set(S0) & packet_set)
check("P6.6c WURZEL-EBENE: der erste ubar-invariante Spread liefert "
      "fuenf 48er-Bloecke mit 48 x 5-Inzidenz EXAKT ueberall 1 (%s); "
      "er teilt %d Tripel mit den sigma-Paketen und ist sigma-stabil: "
      "%s -- der v737-Kill ist ERKLAERT (falsche Bloecke), nicht "
      "revidiert (die sigma-Pakete bleiben kein Spread)"
      % (dict(inc_root), n_pack_in_S0,
         S0 in sig_stable_spreads),
      dict(inc_root) == {1: 240})
print("    ubar-invariante Spreads: %d, davon sigma-stabil: %d; "
      "Tripel-Ueberlapp mit den 5 sigma-Paketen: %s"
      % (len(inv_spreads), len(sig_stable_spreads),
         sorted(len(set(S) & packet_set) for S in inv_spreads)))

# ==================================================================== P7
section("P7: MUST-FAILS (Stufe 7) -- die Identitaet muss brechen")


def B_of_form(formfn):
    return [[1 if formfn(BITS[x], BITS[y]) == 0 else 0 for y in POINTS]
            for x in POINTS]


def bbt_ok(Bm):
    bbt = [[sum(Bm[i][k] * Bm[j][k] for k in range(15))
            for j in range(15)] for i in range(15)]
    return bbt == TARGET


GDEG = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Bdeg = B_of_form(lambda a, b: gform(GDEG, a, b))
rows_deg = sorted(set(sum(r) for r in Bdeg))
check("P7.1 KONTROLLE FEUERT (entartete Form, Rang 2): Zeilensummen %s "
      "statt {7} (Kernpunkte sehen ALLE 15), B B^T != 4I + 3J: %s"
      % (rows_deg, not bbt_ok(Bdeg)),
      rows_deg != [7] and not bbt_ok(Bdeg))

GDOT = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
Bdot = B_of_form(lambda a, b: gform(GDOT, a, b))
diag_dot = [Bdot[i][i] for i in range(15)]
tr_dot = sum(diag_dot)
cp_dot = Matrix(Bdot).charpoly(xs).as_expr()
cp_dot_777 = expand((xs - 7) * (xs - 2) ** 7 * (xs + 2) ** 7)
check("P7.2 KONTROLLE FEUERT (nicht-alternierendes Standard-"
      "Skalarprodukt) -- EHRLICHER BEFUND: B B^T = 4I + 3J HAELT "
      "sogar hier (%s; die nackte Identitaet testet NUR Nicht-"
      "Entartung, nicht Symplektizitaet), aber der PROJEKTIVE Teil "
      "des Lemmas bricht exakt: Diagonale %s statt alle 1 (8 Punkte "
      "liegen NICHT auf ihrer Polaren: q(x) = sum x_i != 0), tr B = "
      "%d != 15, char. Polynom = (x-7)(x-2)^7(x+2)^7 (%s) statt "
      "(x-7)(x-2)^9(x+2)^5 -- die Eigenwert-Multiplizitaeten (1,9,5) "
      "sind die SYMPLEKTIK-Signatur des Lemmas"
      % (bbt_ok(Bdot), dict(Counter(diag_dot)), tr_dot,
         expand(cp_dot - cp_dot_777) == 0),
      bbt_ok(Bdot) and set(diag_dot) != {1} and tr_dot == 7
      and expand(cp_dot - cp_dot_777) == 0)

hbar_wrong = {}
all_zero = True
for lx in REPS:
    for ly in REPS:
        v = (ip(REPS[lx], REPS[ly]) + ip(REPS[lx], J_vec(REPS[ly]))) % 2
        if v:
            all_zero = False
Bwrong = [[1 for _ in POINTS] for _ in POINTS]      # hbar' = 0 => B = J
check("P7.3 KONTROLLE FEUERT (falsche Norm-Konvention, h ohne /2): die "
      "reduzierte Form ist IDENTISCH NULL (alle <x,y> und <x,Jy> gerade "
      "auf L), B' = J (alle 1), B'B'^T = 15 J != 4I + 3J: %s"
      % (not bbt_ok(Bwrong)),
      all_zero and not bbt_ok(Bwrong))

# ============================================================== VERDIKT
section("ZUSAMMENFASSUNG / VERDIKT")
n_pass = sum(1 for _, ok in CHECKS if ok)
print("%d/%d Checks bestanden" % (n_pass, len(CHECKS)))
core = all(ok for n, ok in CHECKS if not n.startswith("P7"))
controls = all(ok for n, ok in CHECKS if n.startswith("P7"))
if core and controls:
    verdict = "PROJ-HAMMING-EXACT"
    print("VERDIKT: PROJ-HAMMING-EXACT -- (V, hbar) ist der symplektische")
    print("F2^4 des unimodularen hermiteschen E8-Gitters; |H_y| = 7,")
    print("Schnitte 3, B B^T = 4I + 3J exakt (Singulaerwerte {7, 2^14}),")
    print("K^2 = (4/49)I + (45/49)Pi0; NS/R = hbar(., y0) mit sigma-fixem")
    print("y0; die v737-Verteilung 0:96/1:64/2:64/3:16 folgt aus dem")
    print("35er-Design (Fuenferzyklen sehen ubar-Orbits), und ueber")
    print("ubar-invariante Spreads existiert die Inzidenz-1-")
    print("Koordinatisierung.")
elif controls:
    verdict = "PROJ-HAMMING-PARTIAL"
    print("VERDIKT: PROJ-HAMMING-PARTIAL -- Kontrollen feuern, aber ein")
    print("Kern-Check scheiterte; siehe FAIL-Zeilen.")
else:
    verdict = "TEST-VOID"
    print("VERDIKT: TEST-VOID -- eine Must-fail-Kontrolle feuert nicht;")
    print("die Identitaet waere generisch, der Test misst nichts.")
print("Verdikt-Enum: %s" % verdict)
print("Laufzeit: %.1f s" % (time.time() - T0))
print("ALLE CHECKS BESTANDEN" if n_pass == len(CHECKS)
      else "CHECKS FEHLGESCHLAGEN")


def run():
    """run_all-Einstiegspunkt (Checks laufen auf Modulebene)."""
    return len(CHECKS) - n_pass


if __name__ == "__main__":
    raise SystemExit(0 if n_pass == len(CHECKS) else 1)
