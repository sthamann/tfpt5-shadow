#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v737 -- E8.SEAM48.01: der Seam-48-Intertwiner-Test -- der
schaerfste Struktur-Kill des Review-Morgens (SEAM48-DEAD).


FRAGE (externes Review, schaerfster Struktur-Test): Bilden die fuenf
kanonischen 48er-Codebloecke (aus der bewiesenen sigma-Orbitstruktur der
15 x 16 Gauss-Klassen; gaussian_code_bridge_probe I5 im Standardmodell)
und die 48 regulaeren Fuenferzyklen (des ZERTIFIZIERTEN regulaeren
G31-Operators; v647: u regulaer der Ordnung 20, u^5 = +-J zentral,
u^4 frei mit Zensus {5:48}) eine exakte 5 x 48-Koordinatisierung
von R(E8)?

DIE VIER KRITERIEN (Review woertlich, bindend -- KEINE Relabeling-Suche):
 (1) Die fuenf 48er-Bloecke AUSSCHLIESSLICH aus der bewiesenen
     sigma-Orbitstruktur: Fixblock = die 3 sigma-fixen Klassen,
     vier bewegte Bloecke = die 4 Dreierorbits (je 3 Klassen x 16).
 (2) Der Fuenfer-Operator ist der bereits zertifizierte G31-Operator:
     u = ERSTES Element mit freiem Zensus {20:12} in der
     v647-Enumerationsreihenfolge (Wurzel-Sortierung, Linien-Reps,
     Spiegelungs-BFS, Zensus-Pass -- alles bit-identisch zu v647
     repliziert). Der Fuenfer-Operator ist u^4. Keine Neuwahl.
 (3) KERN-TEST: die 48 x 5-Inzidenzmatrix (Zyklus x Block -> Anzahl
     gemeinsamer Wurzeln) muss EXAKT ueberall 1 sein.
 (4) Der induzierte Ordnung-12-Operator auf dem 48er-Quotienten muss
     dieselben Charakter-Traces, Deck-Sektoren (3 x 16) und
     mu4-Fixspuren wie der v623-Seam-Lift besitzen (Charakter-
     Tabellen-Vergleich, exakt).  Da der Fixpunktvektor
     (fix(g^k))_{k=0..11} die Charaktertafel einer Z12-Permutations-
     darstellung VOLLSTAENDIG bestimmt, ist der exakte Vergleich der
     Fixvektoren der exakte Tafelvergleich.  Der Transport auf den
     48er-Quotienten geschieht ueber die fuenf Block-Sektionen
     (Zykeltyp ist transport-invariant); ZUSAETZLICH wird gemessen,
     welche Elemente von G31 ueberhaupt auf dem Zyklen-Quotienten
     wirken (Partitions-Stabilisator) -- radikale Ehrlichkeit darueber,
     ob "der" induzierte Operator sektionsfrei existiert.

MUST-FAIL-KONTROLLE: zufaellige FREIE Ordnung-5-Operatoren aus W(E8)
(Zensus {5:48}) duerfen die Inzidenz-1-Eigenschaft nicht haben --
sonst misst der Test nichts.

VERDIKTE (eingefroren):
  SEAM48-INTERTWINED  -- alle vier Kriterien;
  SEAM48-GRID-ONLY    -- Inzidenz ueberall 1, aber Charaktere weichen
                         ab (Abweichungsort exakt dokumentiert);
  SEAM48-DEAD         -- Inzidenz != 1 (Verteilung angegeben);
  TEST-VOID           -- die Must-fail-Kontrolle feuert nicht.

FIREWALL: experiments/-Probe; schreibt nichts; kein verification/-,
Paper-, Ledger- oder Website-Surface beruehrt.  Exakte Ganzzahl/
Fraction-Arithmetik durchgehend (keine Gleitkommazahlen).

Quellen (read-only): v647_st31_degree24.py (zertifizierter Operator,
Konstruktion repliziert), gaussian_code_bridge_probe.py I5 (Klassen im
Standardmodell), v634_st31_structure.py (G31), v623_covered_seam.py
(48-Site-Seam-Lift), v629_root_incidence.py (naive 48 x 5 Compiler-Uhr:
KILL -- hier bewusst der REGULAERE Operator, nicht die Compiler-Uhr).

PROVENANCE: discovery probe seam48_intertwiner_probe.py (2026-08-04,
24/24 machinery checks, verdict SEAM48-DEAD: the preregistered
criterion-3 kill fires -- the 48 x 5 incidence matrix is NOT
identically 1 (entry distribution 0:96 / 1:64 / 2:64 / 3:16),
representative-independent (0 of 2304 order-5 elements of G31 have
the incidence-1 property against the fixed blocks), and the must-fail
control fires (0 of 25 random operators pass); valuable residues: the
4 moved blocks carry the v623 character table EXACTLY while the fixed
block deviates exactly by the 12 lifted marks, and the 5-period lemma
u^5 = +/-J holds exactly.  240 = 48 x 5 remains a factorization
WITHOUT coordinatization).  Promoted verbatim; numbers unchanged.
"""

import itertools
import random
import time
from collections import Counter
from fractions import Fraction as Fr
from math import lcm

import numpy as np

T0 = time.time()
CHECKS = []          # Maschinerie- und Kontroll-Checks (muessen bestehen)
CRIT = {}            # die vier Review-Kriterien (Messergebnis, ehrlich)
N240 = 240


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (" -- " + detail) if detail else ""), flush=True)


def criterion(key, ok, text):
    CRIT[key] = bool(ok)
    print("[%s] KRITERIUM %s: %s" % ("PASS" if ok else "FAIL", key, text),
          flush=True)


def section(title):
    print("=" * 78)
    print(title)
    print("=" * 78, flush=True)


# ==================================================================== K0
section("K0: Wurzeln, J, sigma, c (verdoppelte Standard-Koordinaten, "
        "bit-identisch zu v647)")

_roots = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        _roots.append(tuple(2 * a for a in v))
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        _roots.append(v)
RD = np.array(sorted(_roots), dtype=np.int64)
ridx = {tuple(int(a) for a in RD[i]): i for i in range(N240)}
check("K0.1 240 verdoppelte E8-Wurzeln rekonstruiert", RD.shape == (240, 8))


def J_vec_np(x):
    out = np.empty_like(x)
    out[0::2] = -x[1::2]
    out[1::2] = x[0::2]
    return out


def J_vec(x):
    out = []
    for k in range(0, 8, 2):
        out += [-x[k + 1], x[k]]
    return tuple(out)


SIGMA_IDX = [4, 5, 0, 1, 2, 3, 6, 7]


def sig_vec(x):
    return tuple(x[i] for i in SIGMA_IDX)


def perm_from_map(f):
    return np.array([ridx[tuple(int(a) for a in f(RD[i]))]
                     for i in range(N240)], dtype=np.int16)


Jperm = perm_from_map(J_vec_np)
sigperm = perm_from_map(lambda x: x[SIGMA_IDX])
IDP = np.arange(N240, dtype=np.int16)


def comp(p, q):
    """(p o q)[i] = p[q[i]] (erst q, dann p)."""
    return p[q]


def perm_power(p, k):
    r = IDP
    b = p
    while k:
        if k & 1:
            r = comp(b, r)
        b = comp(b, b)
        k >>= 1
    return r


def census_order(p):
    pl = p.tolist()
    seen = bytearray(N240)
    cen = {}
    for s in range(N240):
        if seen[s]:
            continue
        ln, j = 0, s
        while not seen[j]:
            seen[j] = 1
            j = pl[j]
            ln += 1
        cen[ln] = cen.get(ln, 0) + 1
    o = 1
    for L in cen:
        o = lcm(o, L)
    return tuple(sorted(cen.items())), o


cperm = comp(Jperm, sigperm)
cen_c, ord_c = census_order(cperm)
check("K0.2 Compiler-Uhr c = J o sigma: Ordnung %d, Zensus %s "
      "(v629: 19 x 12 + 3 x 4 -- NICHT frei; darum hier der regulaere "
      "Operator)" % (ord_c, dict(cen_c)),
      ord_c == 12 and dict(cen_c) == {4: 3, 12: 19})

line_of = np.full(N240, -1, dtype=np.int32)
line_reps = []
for i in range(N240):
    if line_of[i] >= 0:
        continue
    orb = [i, int(Jperm[i]), int(Jperm[Jperm[i]]),
           int(Jperm[Jperm[Jperm[i]]])]
    for j in orb:
        line_of[j] = len(line_reps)
    line_reps.append(i)
check("K0.3 60 J-Linien", len(line_reps) == 60)

# ==================================================================== K1
section("K1: die fuenf 48er-Bloecke aus der Gauss-Klassen-"
        "sigma-Orbitstruktur (Kriterium 1)")


def mat_det_inv(rows):
    """exakte Determinante + Inverse (Fractions)."""
    n = len(rows)
    A = [[Fr(v) for v in r] for r in rows]
    I = [[Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
    det = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        assert piv is not None, "singulaere Matrix"
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
    """zeilenweise Hermite-Normalform (obere Dreiecksform, positive
    Diagonale) einer vollrangigen quadratischen Ganzzahlmatrix."""
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


# Standardmodell-Basis (verdoppelte Koordinaten; bridge-Probe I5)
B_STD = [(4, 0, 0, 0, 0, 0, 0, 0),
         (-2, 2, 0, 0, 0, 0, 0, 0),
         (0, -2, 2, 0, 0, 0, 0, 0),
         (0, 0, -2, 2, 0, 0, 0, 0),
         (0, 0, 0, -2, 2, 0, 0, 0),
         (0, 0, 0, 0, -2, 2, 0, 0),
         (0, 0, 0, 0, 0, -2, 2, 0),
         (1, 1, 1, 1, 1, 1, 1, 1)]
detB, BINV = mat_det_inv(B_STD)


def coords(x):
    c = vec_mat(x, BINV)
    assert all(v.denominator == 1 for v in c), "kein Gittervektor"
    return tuple(int(v) for v in c)


AMAT = [coords(tuple(a + b for a, b in zip(brow, J_vec(brow))))
        for brow in B_STD]
detA, _ = mat_det_inv(AMAT)
HNF = row_hnf(AMAT)
check("K1.1 Z[i]-Maschinerie: |det B| = %d (= 2^8, verdoppelt), "
      "Index [L : (1+i)L] = |det A| = %d = 2^4"
      % (abs(int(detB)), abs(int(detA))),
      abs(int(detB)) == 256 and abs(int(detA)) == 16)


def label(x):
    return hnf_reduce(coords(x), HNF)


ZERO_LB = label((0,) * 8)
root_tuples = [tuple(int(a) for a in RD[i]) for i in range(N240)]
root_label = [label(r) for r in root_tuples]
census_cls = Counter(root_label)
check("K1.2 Klassen-Zensus: 15 nichttriviale Klassen x je 16 Wurzeln, "
      "Nullklasse leer (%s)" % dict(Counter(sorted(census_cls.values()))),
      len(census_cls) == 15 and sorted(census_cls.values()) == [16] * 15
      and ZERO_LB not in census_cls)

ok_mu4 = all(root_label[int(Jperm[i])] == root_label[i]
             for i in range(N240))
lines_per_class = Counter()
for a in range(60):
    lines_per_class[root_label[line_reps[a]]] += 1
check("K1.3 Klassen mu4-stabil (alle 240 Wurzeln) und jede Klasse = "
      "Vereinigung von EXAKT 4 der 60 J-Linien",
      ok_mu4 and sorted(lines_per_class.values()) == [4] * 15)

# sigma-Wirkung auf den Klassen (Wohldefiniertheit ueber alle Wurzeln)
sig_of_label = {}
ok_sig_welldef = True
for i in range(N240):
    lb = root_label[i]
    sl = root_label[int(sigperm[i])]
    if lb in sig_of_label and sig_of_label[lb] != sl:
        ok_sig_welldef = False
    sig_of_label[lb] = sl
fixed_labels = [lb for lb in sig_of_label if sig_of_label[lb] == lb]
orbits = []
seen_lb = set()
for lb in sorted(sig_of_label):
    if lb in seen_lb:
        continue
    o1, o2, o3 = lb, sig_of_label[lb], sig_of_label[sig_of_label[lb]]
    orb = {o1, o2, o3}
    seen_lb |= orb
    orbits.append(orb)
orb_census = Counter(len(o) for o in orbits)
check("K1.4 sigma wirkt wohldefiniert auf den 15 Klassen; Orbit-Zensus "
      "%s = 3 fixe Klassen + 4 Dreierorbits"
      % dict(sorted(orb_census.items())),
      ok_sig_welldef and dict(orb_census) == {1: 3, 3: 4}
      and len(fixed_labels) == 3)

# die fuenf Bloecke: Block 0 = Fixblock, Bloecke 1..4 = Dreierorbits
class_roots = {}
for i in range(N240):
    class_roots.setdefault(root_label[i], []).append(i)
fix_block = sorted(j for lb in fixed_labels for j in class_roots[lb])
moved_orbits = [o for o in orbits if len(o) == 3]
moved_blocks = []
for o in moved_orbits:
    blk = sorted(j for lb in o for j in class_roots[lb])
    moved_blocks.append(blk)
moved_blocks.sort(key=lambda blk: blk[0])
BLOCKS = [fix_block] + moved_blocks
block_of = np.full(N240, -1, dtype=np.int8)
for b, blk in enumerate(BLOCKS):
    for j in blk:
        block_of[j] = b
ok_sizes = all(len(blk) == 48 for blk in BLOCKS)
ok_part = int(np.sum(block_of >= 0)) == 240
ok_J_inv = bool(np.all(block_of[Jperm] == block_of))
ok_s_inv = bool(np.all(block_of[sigperm] == block_of))
ok_c_inv = bool(np.all(block_of[cperm] == block_of))
check("K1.5 fuenf Bloecke: Groessen %s, Partition von R(E8), J-invariant "
      "%s, sigma-invariant %s, c-invariant %s (Blockreihenfolge: "
      "Fixblock, dann Dreierorbits nach kleinstem Wurzelindex)"
      % ([len(b) for b in BLOCKS], ok_J_inv, ok_s_inv, ok_c_inv),
      ok_sizes and ok_part and ok_J_inv and ok_s_inv and ok_c_inv)

criterion("1", all(ok for n, ok in CHECKS if n.startswith("K1.")),
          "die fuenf 48er-Bloecke stammen ausschliesslich aus der "
          "bewiesenen sigma-Orbitstruktur (Fixblock + 4 Dreierorbits)")

# ==================================================================== K2
section("K2: der zertifizierte regulaere G31-Operator u und u^4 "
        "(Kriterium 2 -- v647-Konstruktion bit-identisch)")

JRD = np.array([J_vec_np(RD[i]) for i in range(N240)], dtype=np.int64)


def herm4_rowvec(v_i):
    return RD @ RD[v_i], RD @ JRD[v_i]


refl_perms = []
for a in range(60):
    vi = line_reps[a]
    re4, im4 = herm4_rowvec(vi)
    re, im = re4 // 4, im4 // 4
    Y = RD - re[:, None] * RD[vi][None, :] - im[:, None] * JRD[vi][None, :]
    refl_perms.append(np.array([ridx[tuple(int(t) for t in Y[i])]
                                for i in range(N240)], dtype=np.int16))
check("K2.1 60 unitaere Ordnung-2-Spiegelungen erhalten die Wurzeln",
      len({p.tobytes() for p in refl_perms}) == 60
      and all(np.array_equal(comp(p, p), IDP) for p in refl_perms))

t = time.time()
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
check("K2.2 |G31| = %d (BFS, %.1f s)" % (len(Gset), time.time() - t),
      len(Gset) == 46080)
Eall = np.stack(list(Gset.values()))
byte2row = {b: i for i, b in enumerate(Gset.keys())}
check("K2.3 J, sigma, c in G31",
      Jperm.tobytes() in Gset and sigperm.tobytes() in Gset
      and cperm.tobytes() in Gset)


def centralizer_order(x):
    x = np.asarray(x, dtype=np.int16)
    return int(np.sum(np.all(Eall[:, x] == x[Eall], axis=1)))


t = time.time()
cens_all = []
ord_all = np.empty(len(Eall), dtype=np.int32)
for i in range(len(Eall)):
    cen, o = census_order(Eall[i])
    cens_all.append(cen)
    ord_all[i] = o
print("      Zensus/Ordnungs-Pass ueber alle 46080 Elemente: %.1f s"
      % (time.time() - t), flush=True)

# --- v647-Selektion, woertlich: erstes Element mit freiem Zensus {20:12}
rows20 = np.where(ord_all == 20)[0]
reg20_rows = [i for i in rows20 if dict(cens_all[i]) == {20: 12}]
check("K2.4 Ordnung-20-Elemente: %d, davon mit freiem Zensus {20:12}: "
      "%d (v647-Kreuzcheck)" % (len(rows20), len(reg20_rows)),
      len(reg20_rows) > 0)
urow = reg20_rows[0]
u = Eall[urow]
cu = centralizer_order(u)
J2 = comp(Jperm, Jperm)
J3 = comp(J2, Jperm)
u5 = perm_power(u, 5)
u5_is = ("J" if np.array_equal(u5, Jperm)
         else "J^3" if np.array_equal(u5, J3)
         else "-1" if np.array_equal(u5, J2) else "ANDERS")
u4 = perm_power(u, 4)
cen_u4, ord_u4 = census_order(u4)
cu4 = centralizer_order(u4)
print("      Fingerprint u (erste 16 Bilder): %s"
      % [int(x) for x in u[:16]])
check("K2.5 zertifizierter Zeuge u = reg20_rows[0] (v647-Reihenfolge, "
      "KEINE Neuwahl): Zensus %s, |C_G31(u)| = %d = 20 (Springer), "
      "u^5 = %s (zentral)"
      % (dict(cens_all[urow]), cu, u5_is),
      dict(cens_all[urow]) == {20: 12} and cu == 20
      and u5_is in ("J", "J^3"))
check("K2.6 der Fuenfer-Operator u^4: Ordnung %d, wirkt FREI mit Zensus "
      "%s = {5:48}, |C_G31(u^4)| = %d = 20 (zeta5-regulaer, v647 S3.3)"
      % (ord_u4, dict(cen_u4), cu4),
      ord_u4 == 5 and dict(cen_u4) == {5: 48} and cu4 == 20)

criterion("2", all(ok for n, ok in CHECKS if n.startswith("K2.")),
          "der Fuenfer-Operator ist u^4 des zertifizierten v647-Zeugen "
          "(deterministisch, keine Neuwahl)")

# ==================================================================== K3
section("K3: DER KERN-TEST -- die 48 x 5-Inzidenzmatrix (Kriterium 3)")

u4l = u4.tolist()
site_of = np.full(N240, -1, dtype=np.int8)
members = []
for i in range(N240):
    if site_of[i] >= 0:
        continue
    cyc = [i]
    j = u4l[i]
    while j != i:
        cyc.append(j)
        j = u4l[j]
    sid = len(members)
    for j2 in cyc:
        site_of[j2] = sid
    members.append(cyc)
check("K3.1 die 48 Fuenferzyklen von u^4 extrahiert (Sites in "
      "Reihenfolge des kleinsten Wurzelindex)",
      len(members) == 48 and all(len(cyc) == 5 for cyc in members))

INC = [[0] * 5 for _ in range(48)]
for s, cyc in enumerate(members):
    for j in cyc:
        INC[s][int(block_of[j])] += 1
entries = Counter(x for row in INC for x in row)
profiles = Counter(tuple(sorted(row, reverse=True)) for row in INC)
col_sums = [sum(INC[s][b] for s in range(48)) for b in range(5)]
all_one = (entries == Counter({1: 240}))
print("      Eintrags-Verteilung der 240 Matrix-Eintraege: %s"
      % dict(sorted(entries.items())))
print("      Zeilenprofil-Zensus (sortierte Zyklus-Zeilen): %s"
      % {k: v for k, v in sorted(profiles.items(), reverse=True)})
print("      Spaltensummen (Wurzeln pro Block, muss 5 x 48 sein): %s"
      % col_sums)

# Strukturlemma: u^5 = +-J erhaelt die Bloecke -> Blockfaerbung entlang
# jeder u-Bahn ist 5-periodisch; der Kern-Test reduziert sich exakt auf
# die 12 Fuenfer-Fenster der 12 u-Bahnen.
ul = u.tolist()
seen_u = bytearray(N240)
windows = []
ok_period = True
for i in range(N240):
    if seen_u[i]:
        continue
    orb = [i]
    j = ul[i]
    while j != i:
        orb.append(j)
        j = ul[j]
    for j2 in orb:
        seen_u[j2] = 1
    if len(orb) != 20:
        ok_period = False
        continue
    if any(int(block_of[orb[k]]) != int(block_of[orb[k % 5]])
           for k in range(20)):
        ok_period = False
    windows.append((orb[0],
                    tuple(int(block_of[orb[k]]) for k in range(5))))
check("K3.2 Strukturlemma: 12 u-Bahnen der Laenge 20; Blockfaerbung "
      "5-periodisch entlang jeder Bahn (aus u^5 = +-J und "
      "J-Blockinvarianz)", len(windows) == 12 and ok_period)
print("      die 12 Block-Fenster (Bahn-Startwurzel: Fenster; "
      "transversal = alle 5 Bloecke genau einmal):")
n_transversal = 0
for rep, win in windows:
    trans = (sorted(win) == [0, 1, 2, 3, 4])
    n_transversal += trans
    print("        Wurzel %3d: %s %s"
          % (rep, win, "TRANSVERSAL" if trans else "<-- NICHT transversal"))
print("      transversale Fenster: %d / 12" % n_transversal)

criterion("3", all_one,
          "Inzidenzmatrix EXAKT ueberall 1 (Eintrags-Verteilung %s)"
          % dict(sorted(entries.items())))

# ==================================================================== K4
section("K4: der induzierte Ordnung-12-Operator vs v623-Seam-Lift "
        "(Kriterium 4 -- Charaktertafel exakt)")

# ---- v623-Lift in-script rekonstruiert (nichts hartkodiert) ----------
N16, NC = 16, 48
MARK_BONDS = (0, 4, 8, 12)
W623 = (1, 1, 1, 1)


def successor(a, s):
    a2 = (a + 1) % N16
    if a2 in MARK_BONDS:
        s = (s + W623[MARK_BONDS.index(a2)]) % 3
    return a2, s


walk = []
a, s = 0, 0
for _ in range(NC):
    walk.append((a, s))
    a, s = successor(a, s)
widx = {p: i for i, p in enumerate(walk)}
ok_walk = ((a, s) == (0, 0) and len(widx) == NC)


def lift_clock(p):
    aa, ss = p
    for _ in range(4):
        aa, ss = successor(aa, ss)
    return (aa, ss)


Lw = [widx[lift_clock(walk[i])] for i in range(NC)]
ok_shift = all(Lw[i] == (i + 4) % NC for i in range(NC))


def small_pow(p, k):
    r = list(range(len(p)))
    for _ in range(k):
        r = [p[x] for x in r]
    return r


def fixes(p):
    return sum(1 for i, x in enumerate(p) if i == x)


def small_order(p):
    n = len(p)
    seen = [False] * n
    o = 1
    for s0 in range(n):
        if seen[s0]:
            continue
        ln, j = 0, s0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            ln += 1
        o = lcm(o, ln)
    return o


def small_census(p):
    n = len(p)
    seen = [False] * n
    cen = Counter()
    for s0 in range(n):
        if seen[s0]:
            continue
        ln, j = 0, s0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            ln += 1
        cen[ln] += 1
    return dict(cen)


f623 = [fixes(small_pow(Lw, k)) for k in range(12)]
deck623 = small_census(small_pow(Lw, 4))
check("K4.1 v623-Lift rekonstruiert: Walk schliesst nach 48 Schritten "
      "(%s), L = +4-Shift (%s), Ordnung 12, L-Zensus %s, Deck = L^4 "
      "Zensus %s" % (ok_walk, ok_shift, small_census(Lw), deck623),
      ok_walk and ok_shift and small_order(Lw) == 12
      and small_census(Lw) == {12: 4} and deck623 == {3: 16})


def z3_sectors(f0, f4, f8):
    """exakte Z3-Charakter-Multiplizitaeten aus Fixspuren (f4 = f8)."""
    assert f4 == f8
    m0 = Fr(f0 + f4 + f8, 3)
    mw = Fr(f0 - f4, 3)
    assert m0.denominator == 1 and mw.denominator == 1
    return (int(m0), int(mw), int(mw))


def z4_sectors(f0, f3, f6, f9):
    """exakte Z4-Charakter-Multiplizitaeten aus Fixspuren (f3 = f9)."""
    assert f3 == f9
    m0 = Fr(f0 + f3 + f6 + f9, 4)
    m1 = Fr(f0 - f6, 4)
    m2 = Fr(f0 - f3 + f6 - f9, 4)
    assert all(x.denominator == 1 for x in (m0, m1, m2))
    return (int(m0), int(m1), int(m2), int(m1))


sec623_deck = z3_sectors(f623[0], f623[4], f623[8])
sec623_mu4 = z4_sectors(f623[0], f623[3], f623[6], f623[9])
mu4_623 = (f623[3], f623[6], f623[9])
check("K4.2 v623-Referenztafel: Fixvektor %s, Deck-Sektoren %s = 3 x 16, "
      "mu4-Fixspuren (k = 3, 6, 9) = %s, mu4-Sektoren %s"
      % (f623, sec623_deck, mu4_623, sec623_mu4),
      f623 == [48] + [0] * 11 and sec623_deck == (16, 16, 16)
      and mu4_623 == (0, 0, 0) and sec623_mu4 == (12, 12, 12, 12))

# ---- die fuenf Block-Sektionen der Compiler-Uhr c --------------------
print("      Fixvektor-Vergleich fix(g^k), k = 0..11 (exakter "
      "Charaktertafel-Vergleich):")
print("        %-14s %s" % ("v623 L", f623))
cl = cperm.tolist()
block_rows = []
pres_ok_all = []
orders_all = []
all_match = True
for b, blk in enumerate(BLOCKS):
    pos = {j: k for k, j in enumerate(blk)}
    ok_pres = all(cl[j] in pos for j in blk)
    pres_ok_all.append(ok_pres)
    pb = [pos[cl[j]] for j in blk]
    fb = [fixes(small_pow(pb, k)) for k in range(12)]
    ob = small_order(pb)
    orders_all.append(ob)
    cenb = small_census(pb)
    sec_deck = z3_sectors(fb[0], fb[4], fb[8])
    sec_mu4 = z4_sectors(fb[0], fb[3], fb[6], fb[9])
    mu4_b = (fb[3], fb[6], fb[9])
    dev = [k for k in range(12) if fb[k] != f623[k]]
    match = (ok_pres and ob == 12 and fb == f623
             and sec_deck == sec623_deck and mu4_b == mu4_623)
    all_match = all_match and match
    name = "Fixblock B0" if b == 0 else "Block B%d" % b
    block_rows.append((name, fb, cenb, sec_deck, sec_mu4, mu4_b, dev,
                       match))
    print("        %-14s %s%s" % (name, fb,
          ("" if not dev else "   <-- ABWEICHUNG bei k = %s" % dev)))
for name, fb, cenb, sec_deck, sec_mu4, mu4_b, dev, match in block_rows:
    print("      %-14s Ordnung 12, Zensus %s, Deck-Sektoren %s, "
          "mu4-Fixspuren %s, mu4-Sektoren %s -> %s"
          % (name, cenb, sec_deck, mu4_b, sec_mu4,
             "MATCH mit v623" if match else "ABWEICHUNG"))
check("K4.3 c erhaelt jeden Block und hat auf jedem Block Ordnung 12 "
      "(Sektions-Transport wohldefiniert; Zykeltyp = vollstaendige "
      "Z12-Charaktertafel, transport-invariant): Ordnungen %s"
      % orders_all,
      all(pres_ok_all) and all(o == 12 for o in orders_all)
      and all(x[1][0] == 48 for x in block_rows)
      and all(sum(k * v for k, v in x[2].items()) == 48
              for x in block_rows))

# ---- ehrliche Quotienten-Messung: wer wirkt auf den 48 Sites? --------
t = time.time()
site_img = site_of[Eall]                       # (46080, 240) int8
Mflat = np.array([m for cyc in members for m in cyc], dtype=np.int64)
A48 = site_img[:, Mflat].reshape(len(Eall), 48, 5)
pres = np.all(A48 == A48[:, :, :1], axis=(1, 2))
stab_rows = np.where(pres)[0]
first_members = np.array([cyc[0] for cyc in members], dtype=np.int64)
induced = {}
for row in stab_rows:
    g = Eall[row]
    sperm = tuple(int(site_of[int(g[m0])]) for m0 in first_members)
    induced.setdefault(sperm, 0)
    induced[sperm] += 1
ind_orders = Counter(small_order(list(sp)) for sp in induced)
kernel = len(stab_rows) // max(1, len(induced))
j_in = bool(pres[byte2row[Jperm.tobytes()]])
s_in = bool(pres[byte2row[sigperm.tobytes()]])
c_in = bool(pres[byte2row[cperm.tobytes()]])
print("      Partitions-Stabilisator-Scan (%.1f s): |Stab| = %d, "
      "Kern (zyklenweise Wirkung) = %d, induzierte Gruppe auf den 48 "
      "Sites: Ordnung %d, Elementordnungen %s"
      % (time.time() - t, len(stab_rows), kernel, len(induced),
         dict(sorted(ind_orders.items()))))
print("      wirkt auf dem Zyklen-Quotienten: J: %s, sigma: %s, c: %s"
      % (j_in, s_in, c_in))
has12 = 12 in ind_orders
check("K4.4 EHRLICHKEIT Quotient: existiert ein sektionsfreier "
      "Ordnung-12-Operator auf dem 48er-Quotienten (induziert von "
      "G31)? -> %s (gemessen); der Ordnung-12-Vergleich laeuft daher "
      "ueber die fuenf Block-Sektionen (K4.3)"
      % ("JA" if has12 else "NEIN"), True)
if j_in:
    jhat = [int(site_of[int(Jperm[m0])]) for m0 in first_members]
    f_j = [fixes(small_pow(jhat, k)) for k in range(1, 4)]
    print("      mu4 auf den Sites: J induziert Ordnung-%d-Operator, "
          "Zensus %s, Fixspuren (J, J^2, J^3) = %s "
          "(v623-mu4-Fixspuren: %s)"
          % (small_order(jhat), small_census(jhat), tuple(f_j),
             mu4_623))

criterion("4", all_match,
          "alle fuenf Block-Sektionen tragen die v623-Charaktertafel "
          "(Fixvektor + Deck-Sektoren 3 x 16 + mu4-Fixspuren) exakt"
          if all_match else
          "Charaktertafel weicht ab: %s"
          % "; ".join("%s bei k = %s (fix = %s statt %s)"
                      % (r[0], r[6], [r[1][k] for k in r[6]],
                         [f623[k] for k in r[6]])
                      for r in block_rows if not r[7]))

# ==================================================================== K5
section("K5: MUST-FAIL-KONTROLLE -- zufaellige freie Ordnung-5-"
        "Operatoren aus W(E8)")

block_list = block_of.tolist()


def inc_all_one(p):
    """hat p (Ordnung 5, frei) die Inzidenz-1-Eigenschaft gegen die
    fuenf festen Bloecke?"""
    pl = p.tolist() if hasattr(p, "tolist") else list(p)
    seen = bytearray(N240)
    for i in range(N240):
        if seen[i]:
            continue
        cols = 0
        n = 0
        j = i
        while not seen[j]:
            seen[j] = 1
            bbit = 1 << block_list[j]
            if cols & bbit:
                return False
            cols |= bbit
            j = pl[j]
            n += 1
        if n != 5 or cols != 31:
            return False
    return True


# alle 240 reellen Spiegelungen von W(E8) (verdoppelte Wurzeln)
t = time.time()
RPERMS = []
for i in range(N240):
    rd = RD[i]
    ip4 = RD @ rd
    Y = RD - (ip4 // 4)[:, None] * rd[None, :]
    RPERMS.append(np.array([ridx[tuple(int(v) for v in Y[k])]
                            for k in range(N240)], dtype=np.int16))
check("K5.1 240 reelle W(E8)-Spiegelungen gebaut (%.1f s)"
      % (time.time() - t), len(RPERMS) == 240)

rng = random.Random(20260804)
targets = 25
found = []
draws = n_nonfree = n_in_g31 = 0
while len(found) < targets and draws < 6000:
    draws += 1
    g = IDP
    for _ in range(24):
        g = comp(RPERMS[rng.randrange(240)], g)
    cen_g, o_g = census_order(g)
    if o_g % 5:
        continue
    h = perm_power(g, o_g // 5)
    cen_h, o_h = census_order(h)
    if dict(cen_h) != {5: 48}:
        n_nonfree += 1
        continue
    found.append(h)
    if h.tobytes() in Gset:
        n_in_g31 += 1
hits = [inc_all_one(h) for h in found]
n_hits = sum(hits)
check("K5.2 %d zufaellige FREIE Ordnung-5-Operatoren aus W(E8) gezogen "
      "(%d Ziehungen; %d nicht-freie Ordnung-5 verworfen; %d der %d "
      "liegen zufaellig in G31)"
      % (len(found), draws, n_nonfree, n_in_g31, len(found)),
      len(found) == targets)
# Beispiel-Verteilungen der ersten drei Kontrollen (informativ)
for k in range(min(3, len(found))):
    pl = found[k].tolist()
    seen = bytearray(N240)
    prof = Counter()
    for i in range(N240):
        if seen[i]:
            continue
        cyc = [i]
        j = pl[i]
        while j != i:
            cyc.append(j)
            j = pl[j]
        for j2 in cyc:
            seen[j2] = 1
        row = [0] * 5
        for j2 in cyc:
            row[block_list[j2]] += 1
        prof[tuple(sorted(row, reverse=True))] += 1
    print("      Kontrolle %d: Zeilenprofil-Zensus %s"
          % (k + 1, {kk: vv for kk, vv in sorted(prof.items(),
                                                 reverse=True)}))
control_fires = (len(found) == targets and n_hits == 0)
check("K5.3 KONTROLLE FEUERT: KEINER der %d zufaelligen Operatoren hat "
      "die Inzidenz-1-Eigenschaft (Treffer: %d) -- der Test misst "
      "etwas" % (len(found), n_hits), control_fires)

# ==================================================================== K6
section("K6: deterministischer Kontext -- ALLE Ordnung-5-Elemente "
        "von G31 (keine Selektion, nur Zensus)")

rows5 = np.where(ord_all == 5)[0]
all_free5 = all(dict(cens_all[i]) == {5: 48} for i in rows5)
n_allone_g31 = sum(1 for i in rows5 if inc_all_one(Eall[i]))
u4row = byte2row[u4.tobytes()]
check("K6.1 G31 enthaelt %d Ordnung-5-Elemente, alle frei ({5:48}): %s"
      % (len(rows5), all_free5), all_free5)
print("      davon mit Inzidenz-1-Eigenschaft gegen die festen Bloecke: "
      "%d von %d (Anteil exakt %d/%d)"
      % (n_allone_g31, len(rows5), n_allone_g31, len(rows5)))
print("      das zertifizierte u^4 (Zeile %d) hat die Eigenschaft: %s "
      "-- das VERDIKT haengt AUSSCHLIESSLICH am zertifizierten u^4 "
      "(Kriterium 2), dieser Zensus ist reiner Kontext"
      % (u4row, bool(all_one)))

# ============================================================== VERDIKT
section("ZUSAMMENFASSUNG / VERDIKT")
n_pass = sum(1 for _, ok in CHECKS if ok)
machinery_ok = (n_pass == len(CHECKS))
print("Maschinerie-/Kontroll-Checks: %d/%d bestanden" % (n_pass,
                                                         len(CHECKS)))
for k in ("1", "2", "3", "4"):
    print("Kriterium %s: %s" % (k, "PASS" if CRIT.get(k) else "FAIL"))
print("Must-fail-Kontrolle: %s"
      % ("FEUERT (Test misst etwas)" if control_fires
         else "FEUERT NICHT (Test misst nichts)"))
print()
if not control_fires:
    verdict = "TEST-VOID"
    print("VERDIKT: TEST-VOID -- die Must-fail-Kontrolle feuert nicht;")
    print("die Inzidenz-1-Eigenschaft waere generisch, der Test misst")
    print("nichts. Kein positives oder negatives Struktur-Verdikt.")
elif not (CRIT["1"] and CRIT["2"]):
    verdict = "MASCHINERIE-FEHLER"
    print("VERDIKT: MASCHINERIE-FEHLER -- Kriterium 1 oder 2 nicht")
    print("reproduzierbar; siehe FAIL-Zeilen.")
elif CRIT["3"] and CRIT["4"]:
    verdict = "SEAM48-INTERTWINED"
    print("VERDIKT: SEAM48-INTERTWINED -- alle vier Kriterien: R(E8) =")
    print("{5 Carrier-Slots} x {48 Seam-Sites} als echtes Informations-")
    print("raster; Inzidenz exakt 1 und die induzierte Ordnung-12-Uhr")
    print("traegt die v623-Charaktertafel exakt.")
elif CRIT["3"]:
    verdict = "SEAM48-GRID-ONLY"
    print("VERDIKT: SEAM48-GRID-ONLY -- die Inzidenz ist ueberall exakt")
    print("1 (das 5 x 48-Raster EXISTIERT), aber die Charaktertafel des")
    print("induzierten Ordnung-12-Operators weicht vom v623-Seam-Lift")
    print("ab; Abweichungsort exakt dokumentiert (siehe K4).")
else:
    verdict = "SEAM48-DEAD"
    print("VERDIKT: SEAM48-DEAD -- die Inzidenz ist NICHT ueberall 1;")
    print("die Eintrags-Verteilung %s und die 12 Block-Fenster (K3)"
          % dict(sorted(entries.items())))
    print("sind selbst informativ; 240 = 48 x 5 bleibt (mit diesem")
    print("zertifizierten Operator und diesen kanonischen Bloecken)")
    print("eine Faktorisierung OHNE Koordinatisierung.")
print()
print("Verdikt-Enum: %s" % verdict)
print("Laufzeit: %.1f s" % (time.time() - T0))
print("ALLE MASCHINERIE-CHECKS BESTANDEN" if machinery_ok
      else "MASCHINERIE-CHECKS FEHLGESCHLAGEN")

def run():
    """run_all entry point: the checks execute at import time (module level)."""
    return 0 if machinery_ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
