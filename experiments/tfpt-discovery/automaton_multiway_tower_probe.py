#!/usr/bin/env python3
"""automaton_multiway_tower_probe.py -- AUTOMATON.MULTIWAY.01 (Explorations-Probe):
Kann TFPT als Automat (Zuse) / Hypergraph-Rewriting-System (Wolfram) aufgesetzt
werden -- und bringt die Lesart NEUE pruefbare Struktur oder nur Umbenennung?

KORPUS-STAND (ehrlich, vorab):
  *  Die Wolfram-Bruecke existiert BEREITS fuer die Carrier-Schicht:
     v298 (E8-Skelett = Netzwerk-Attraktor), v299 (autonomes Wachstum
     E6->E7->E8->E8-hat), v312 (Substrat-Abgrenzung), v324 (gefasertes
     Substrat), v327 (minimales Rewrite liefert 2/3), v345 (Plumbing-Link =
     Poincare-Sphaere), v395 (gekoppeltes Rewrite) -- plus die redaktionelle
     Positionierung Zuse--Schmidhuber--Wolfram in introduction.tex (2026-07-19)
     und der Zuse-Runden-Kontrakt glue01_dynamical_selection.py (2026-07-10).
  *  NICHT existiert: die Multiway-/Causal-Invariance-/Branchial-Lesart der
     NEUEN Strukturen (v714 Z[i]-E8-Hecke-Turm, v702 Flow-Verifier, v689/v736
     Gaussian Code, v623 48-Site-Lift, hecke_mod_ramified-Kanaele).  Die Worte
     "multiway", "causal invariance", "branchial" kommen im Theorie-Korpus
     nicht vor.  Genau diese Luecke prototypisiert diese Probe.

DIE VIER ABBILDUNGEN (A1 prototypisiert, A2-A4 formal typisiert):

  A1 [Turm als Multiway-System, PROTOTYP]:
     Zustaende  = Z[i]-Untermoduln M von L = Z[i]^4 (der Gaussian-E8-Rahmen
                  v689/v714), graduiert nach abelschem Index n = N(det).
     Rewrites   = Index-N(pi)-Uebergaenge M -> M' (die Hecke-Korrespondenzen
                  v714), ein Regeltyp pro Gauss-Primideal pi.
     Zeit       = Grad-Graduierung t(M) = log n (Foliation).
     Gemessen:
       (i)   KONFLUENZ / CAUSAL INVARIANCE: fuer verschiedene Primideale
             (p,q) endet JEDE p-dann-q-Kette im selben Zustandsmultiset wie
             die q-dann-p-Kette, mit per-Endpunkt-Multiplizitaet exakt 1
             (Diamant-Eigenschaft; das ist Hecke-Kommutativitaet als
             Automaten-Aussage -- mathematisch durch Primaerzerlegung/CRT
             erzwungen, hier explizit ausgezaehlt).
       (ii)  BRANCHIAL-STRUKTUR: bei GLEICHEM Primideal (pi-dann-pi) mergen
             die Branch-Paare NICHT 1:1 -- das Multiplizitaetsspektrum ist
             {1 (zyklischer Quotient), q+1 (Typ (1,1))} und die Anzahl der
             Typ-(1,1)-Endpunkte ist der Gauss-Binomialkoeffizient [4,2]_q
             (Grassmann-Geometrie).  Der v714-Zell-Normalisierer
             1/(1+n+n^2+n^3) ist in dieser Lesart die Branchial-Volumen-
             Normalisierung.
       (iii) PFAD-ZAEHLUNG vs Lambda-Rekursion (v714): a_n log n =
             sum_{d|n} Lambda_A(d) a_{n/d}; Off-Support-Verschwinden an
             quadratfreien Komposita ist AEQUIVALENT zur Diamant-Eigenschaft;
             On-Support Lambda_A(N(pi)^k) = log N(pi) * sum_j N(pi)^{kj}
             (geschlossene Form, gemessen).  Kettenzahlen C_n rekursiv und
             gegen die explizite Enumeration geprueft.
       (iv)  KAUSAL-NETZ: Foliation = Grad-Schichten (Index-Multiplikativitaet
             entlang jeder Kante, in der Konstruktion mit-gecheckt);
             Ereignis-Typen = Gauss-Primideale; sigma-Aktion (Konjugation)
             klassifiziert die Ereignis-Typen: ramifiziert (sigma trivial auf
             der ganzen Schicht), inert (semilineare Aktion, Fixpunkte =
             F_p-rationale Hyperebenen), split (freier Schicht-Tausch) --
             die Zustands-Verfeinerung des v714-sigma-Descents.

  A2 [48-Site-Lift als zellulaerer Automat]: der v623-Lift wird als Automat
     nachgebaut (16-Site-Basis, mu3-Cover, Marken bei {0,4,8,12}).  Update-
     Regel EXPLIZIT: in Walk-Koordinaten ist die Uhr L ein reiner Shift um 4
     (Radius 4, lokal); Konnektivitaets-Zensus (j=1,2: EIN 48-Zykel; j=0 und
     alternierend: 3 Zykel) reproduziert v623-V1; L^4 = Deck, ord(L) = 12.
     Deck-Sektor-Erhaltung: ja -- aber TRIVIAL (jeder Shift kommutiert mit
     jedem Shift; Fourier-Sektoren sind fuer Shift-Automaten immer erhalten).
     Kontrolle: eine lokale Nicht-Shift-Regel bricht die Sektoren sofort.
     => Die "Erhaltungsgroesse" ist exakt v623s L^4 = Deck, umbenannt.

  A3 [Computational Irreducibility, quantitativ -- Typisierung]: v702-Zahlen
     als ZITAT (declared, nicht neu gemessen): der Fluss ist VERIFIZIERER
     (voller Kamm 913 >= 898, jeder Fake stirbt >= 184 Lags frueher), nicht
     GENERATOR (autonom 2-4 Slots); pro-Slot-Verstaerkung g ~ 5-12 =>
     Lyapunov-Analogon lambda = ln g pro Slot; nutzbare Kettenlaenge
     N* ~ 1 + ln(Toleranz/eps)/ln(g).  Konsistenz-Check hier: die Formel
     reproduziert das gemessene Bruchfenster.  Wolfram-Typ: die Atom-Schicht
     ist (relativ zur Fluss-Aufloesung) computationally irreducible, die
     Arch-Schicht reducible (geschlossene Gamma-Formen).

  A4 [Code als endlicher Automat -- Typisierung]: (V = F2^4, sigma) ist ein
     PERMUTATIONS-Automat (Transitionsgruppe C3): Zykeltyp 1^4 3^4, Burnside
     (15+3+3)/3 = 7 Orbits auf V\\{0} (v736).  "Attraktor-Struktur" ist ein
     Fehlgriff: reversible Automaten haben keine echten Attraktoren, nur
     Orbits.  Hecke-Kanaele als Automaten-Homomorphismen: auf der ungeraden
     Seite TRIVIAL (deg * id, hecke_mod_ramified), nur die ramifizierte
     Schicht traegt Struktur (15 Hyperebenen, 2:1) -- hier nachgerechnet:
     sigma-Orbit-Zensus auf Klassen (1+3+4x3) und Hyperebenen (3+4x3).

ADJUDIKATION (Enums eingefroren, am Ende gedruckt):
  pro Abbildung: NEUE-STRUKTUR / AEQUIVALENT-NUETZLICH / UMBENENNUNG;
  gesamt: FORSCHUNGSPROGRAMM / ERZAEHL-SCHICHT / GEMISCHT.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface beruehrt.
Ring-intern: KEINE Primzahltabelle, kein sympy, kein zeta -- die Gauss-Prime
kommen aus einem Norm-Scan + Irreduzibilitaetstest (AST-geprueft auf dieser
Datei).  Exakte Ganzzahl-Arithmetik im gesamten A1-Teil.

Run: experiments/tfpt-discovery/.venv/bin/python \\
     experiments/tfpt-discovery/automaton_multiway_tower_probe.py
"""

import ast
import math
import os
import sys
import time
from collections import Counter
from itertools import product

import numpy as np

RANK = 4                 # Z[i]-Rang des Gaussian-E8-Moduls (v689/v714)
X_NORM = 50              # Norm-Horizont der Multiway-Schichten (Aufgabe)
N_HNF_SELFTEST = 200     # Zufalls-Selbsttests der kanonischen HNF

FAILURES = []
CHECKS = [0]


def check(name, ok, detail=""):
    CHECKS[0] += 1
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILURES.append(name)
    print("[%s] %s%s" % (tag, name, (" -- " + detail) if detail else ""))


# ===========================================================================
# G0 -- Firewall + exakte Gauss-Arithmetik + kanonische HNF (Selbsttests)
# ===========================================================================

BANNED = {"sympy", "isprime", "primerange", "nextprime", "primepi",
          "sieve", "zetazero", "zeta", "factorint"}


def g0_ast_firewall():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in BANNED:
            hits.add(node.id)
        if isinstance(node, ast.Attribute) and node.attr in BANNED:
            hits.add(node.attr)
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                names.append(node.module)
            for nm in names:
                if nm.split(".")[0] in BANNED:
                    hits.add(nm)
    return hits


ZERO = (0, 0)
ONE = (1, 0)
UNITS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gconj(x):
    return (x[0], -x[1])


def gnorm(x):
    return x[0] * x[0] + x[1] * x[1]


def _round_half(num, den):
    # floor(num/den + 1/2), den > 0, exakt in Ganzzahlen; vertraeglich mit
    # ganzzahligen Shifts => kanonische Restklassenvertreter.
    return (2 * num + den) // (2 * den)


def gdivmod(x, d):
    n = gnorm(d)
    t = gmul(x, gconj(d))
    q = (_round_half(t[0], n), _round_half(t[1], n))
    return q, gsub(x, gmul(q, d))


def gcanon_unit(z):
    """Einheit u mit u*z = kanonischer Assoziierter (re>0, im>=0)."""
    if z == ZERO:
        return ONE
    for u in UNITS:
        w = gmul(u, z)
        if w[0] > 0 and w[1] >= 0:
            return u
    raise AssertionError("kein kanonischer Assoziierter: %r" % (z,))


def gext_gcd(a, b):
    r0, r1 = a, b
    u0, u1 = ONE, ZERO
    while r1 != ZERO:
        q, r = gdivmod(r0, r1)
        r0, r1 = r1, r
        u0, u1 = u1, gsub(u0, gmul(q, u1))
    return r0, u0


def hnf(rows):
    """Kanonische Zeilen-HNF eines vollrangigen Untermoduls von Z[i]^RANK.

    Obere Dreiecksform, Diagonale = kanonische Assoziierte, Eintraege ueber
    der Diagonale = kanonische Reste mod Spalten-Diagonale (gdivmod ist
    coset-konstant).  Eingabe: m >= RANK Erzeuger-Zeilen."""
    rows = [list(r) for r in rows]
    m = len(rows)
    piv = 0
    for col in range(RANK):
        while True:
            nz = [r for r in range(piv, m) if rows[r][col] != ZERO]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda r: gnorm(rows[r][col]))
            r0 = nz[0]
            for r in nz[1:]:
                q, _ = gdivmod(rows[r][col], rows[r0][col])
                rows[r] = [gsub(rows[r][c], gmul(q, rows[r0][c]))
                           for c in range(RANK)]
        nz = [r for r in range(piv, m) if rows[r][col] != ZERO]
        if not nz:
            raise ValueError("Rang-Defekt")
        r0 = nz[0]
        rows[piv], rows[r0] = rows[r0], rows[piv]
        u = gcanon_unit(rows[piv][col])
        if u != ONE:
            rows[piv] = [gmul(u, c) for c in rows[piv]]
        for r in range(piv):
            q, _ = gdivmod(rows[r][col], rows[piv][col])
            if q != ZERO:
                rows[r] = [gsub(rows[r][c], gmul(q, rows[piv][c]))
                           for c in range(RANK)]
        piv += 1
    return tuple(tuple(rows[r][c] for c in range(RANK)) for r in range(RANK))


def hnf_index(H):
    d = ONE
    for j in range(RANK):
        d = gmul(d, H[j][j])
    return gnorm(d)


ID_BASIS = tuple(tuple(ONE if i == j else ZERO for j in range(RANK))
                 for i in range(RANK))


def g0_hnf_selftest(rng):
    """Zufalls-Unimodular-Invarianz der kanonischen HNF."""
    bad = 0
    for _ in range(N_HNF_SELFTEST):
        # zufaelliger vollrangiger Untermodul: obere Dreiecksmatrix
        B = [[ZERO] * RANK for _ in range(RANK)]
        for j in range(RANK):
            B[j][j] = (int(rng.integers(1, 4)), int(rng.integers(0, 3)))
            if B[j][j] == ZERO:
                B[j][j] = ONE
            for c in range(j + 1, RANK):
                B[j][c] = (int(rng.integers(-3, 4)), int(rng.integers(-3, 4)))
        H0 = hnf(B)
        # zufaellige unimodulare Zeilen-Ops
        rows = [list(r) for r in H0]
        for _ in range(12):
            a, b = rng.integers(0, RANK, size=2)
            if a == b:
                u = UNITS[int(rng.integers(0, 4))]
                rows[a] = [gmul(u, c) for c in rows[a]]
            else:
                k = (int(rng.integers(-2, 3)), int(rng.integers(-2, 3)))
                rows[a] = [gadd(rows[a][c], gmul(k, rows[b][c]))
                           for c in range(RANK)]
        if hnf(rows) != H0:
            bad += 1
    return bad


def gaussian_primes(limit):
    """Ring-interner Prime-Scan: kanonische Assoziierte, Norm <= limit,
    irreduzibel = kein echter Teiler mit 1 < N(d) < N(z).  KEINE
    Primzahltabelle."""
    cands = []
    B = int(math.isqrt(limit)) + 1
    for a in range(0, B + 1):
        for b in range(0, B + 1):
            z = (a, b)
            n = gnorm(z)
            if n < 2 or n > limit:
                continue
            if gcanon_unit(z) != ONE:
                continue
            cands.append(z)
    cands.sort(key=gnorm)
    primes = []
    for z in cands:
        nz = gnorm(z)
        red = False
        for d in cands:
            nd = gnorm(d)
            if nd >= nz:
                break
            if nd < 2:
                continue
            _, r = gdivmod(z, d)
            if r == ZERO:
                red = True
                break
        if not red:
            primes.append(z)
    return primes


def residues_mod(pi):
    q = gnorm(pi)
    seen = set()
    out = []
    for a in range(-4, 5):
        for b in range(-4, 5):
            _, r = gdivmod((a, b), pi)
            if r not in seen:
                seen.add(r)
                out.append(r)
    assert len(out) == q, (pi, len(out))
    return out


# ===========================================================================
# A1 -- das Multiway-System des Hecke-Turms
# ===========================================================================

def down_layer(B, pi, res):
    """Alle Index-N(pi)-Untermoduln des von den Zeilen B erzeugten Moduls
    (Hyperebenen von B/pi B), als kanonische HNF-Schluessel.  Der Index-Check
    N(det) = q * N(det B) ist die Foliation-Kante (Zeit-Additivitaet)."""
    q = len(res)
    base_idx = hnf_index(hnf(B))
    out = []
    for lead in range(RANK):
        for tail in product(res, repeat=RANK - 1 - lead):
            f = [ZERO] * lead + [ONE] + list(tail)
            gens = []
            for j in range(RANK):
                if j == lead:
                    continue
                gens.append([gsub(B[j][c], gmul(f[j], B[lead][c]))
                             for c in range(RANK)])
            for j in range(RANK):
                gens.append([gmul(pi, B[j][c]) for c in range(RANK)])
            H = hnf(gens)
            assert hnf_index(H) == q * base_idx, "Foliation-Kante verletzt"
            out.append(H)
    return out


def compose_two(pi1, res1, pi2, res2):
    """Multiset der Endzustaende aller pi1-dann-pi2-Ketten ab L."""
    c = Counter()
    for M in down_layer(ID_BASIS, pi1, res1):
        for M2 in down_layer(M, pi2, res2):
            c[M2] += 1
    return c


def sigma_module(H):
    return hnf([[gconj(H[j][c]) for c in range(RANK)] for j in range(RANK)])


def gauss_binom_42(q):
    return ((q ** 4 - 1) * (q ** 3 - 1)) // ((q ** 2 - 1) * (q - 1))


# --- Zell-Zensus + Lambda-Rekursion (S3) -----------------------------------

def ideal_counts(primes, limit):
    """iota(n) = #Ideale von Z[i] mit Norm n <= limit (DP ueber die
    kanonischen Primideale)."""
    iota = {1: 1}
    for p in primes:
        q = gnorm(p)
        cur = dict(iota)
        for n, c in iota.items():
            v = n * q
            while v <= limit:
                cur[v] = cur.get(v, 0) + c
                v *= q
        iota = cur
    return iota


def census_cells(iota, limit):
    """a_n = #Index-n-Untermoduln von Z[i]^4 via HNF-Diagonalzellen:
    a_n = sum_{prod nu_i = n} iota(nu_1..4) * nu_1^3 nu_2^2 nu_3^1."""
    a = {}
    norms = sorted(iota)
    for n1 in norms:
        for n2 in norms:
            if n1 * n2 > limit:
                break
            for n3 in norms:
                if n1 * n2 * n3 > limit:
                    break
                for n4 in norms:
                    n = n1 * n2 * n3 * n4
                    if n > limit:
                        break
                    w = (iota[n1] * iota[n2] * iota[n3] * iota[n4]
                         * n1 ** 3 * n2 ** 2 * n3)
                    a[n] = a.get(n, 0) + w
    return a


def run():
    t0 = time.time()
    print("=" * 78)
    print("AUTOMATON.MULTIWAY.01 -- Zuse/Wolfram-Lesart der neuen TFPT-Strukturen")
    print("=" * 78)

    # ---------------- G0 ----------------------------------------------------
    print("\n--- G0: Firewall + Selbsttests " + "-" * 46)
    hits = g0_ast_firewall()
    check("G0.1 AST-Firewall (keine Primtabelle/zeta/sympy)", not hits,
          "verbotene Namen: %s" % (sorted(hits) if hits else "keine"))

    rng = np.random.default_rng(714)
    bad = g0_hnf_selftest(rng)
    check("G0.2 kanonische Z[i]-HNF: unimodulare Invarianz", bad == 0,
          "%d/%d Zufallstests invariant" % (N_HNF_SELFTEST - bad,
                                            N_HNF_SELFTEST))

    primes = gaussian_primes(X_NORM)
    norms = sorted(gnorm(p) for p in primes)
    exp_norms = [2, 5, 5, 9, 13, 13, 17, 17, 29, 29, 37, 37, 41, 41, 49]
    check("G0.3 ring-interne Gauss-Prime (Norm <= %d)" % X_NORM,
          norms == exp_norms,
          "Norm-Multiset %s" % norms)
    by_norm = {}
    for p in primes:
        by_norm.setdefault(gnorm(p), []).append(p)
    pi2 = by_norm[2][0]           # (1+i)  ramifiziert
    pi5a, pi5b = by_norm[5]       # (2+i), (1+2i)  split
    pi9 = by_norm[9][0]           # (3)  inert
    res2 = residues_mod(pi2)
    res5a = residues_mod(pi5a)
    res5b = residues_mod(pi5b)
    res9 = residues_mod(pi9)

    # ---------------- S1: Schicht-Zensus (Zustaende) -------------------------
    print("\n--- S1: Schicht-Zensus des Multiway-Graphen (explizit) " + "-" * 22)
    lay2 = down_layer(ID_BASIS, pi2, res2)
    lay5a = down_layer(ID_BASIS, pi5a, res5a)
    lay5b = down_layer(ID_BASIS, pi5b, res5b)
    lay9 = down_layer(ID_BASIS, pi9, res9)
    n13a, n13b = by_norm[13]
    lay13a = down_layer(ID_BASIS, n13a, residues_mod(n13a))
    lay13b = down_layer(ID_BASIS, n13b, residues_mod(n13b))
    counts = (len(set(lay2)), len(set(lay5a)) + len(set(lay5b)),
              len(set(lay9)), len(set(lay13a)) + len(set(lay13b)))
    check("S1.1 Schichten 2/5/9/13 distinct + v714-Zensus",
          counts == (15, 312, 820, 4760)
          and len(lay2) == 15 and len(lay5a) == 156 and len(lay9) == 820,
          "a_2=%d a_5=%d a_9=%d a_13=%d (v714: 15/312/820/4760)" % counts)

    # ---------------- S2: Diamant / Causal Invariance ------------------------
    print("\n--- S2: Konfluenz-Messung (Diamant-Eigenschaft) " + "-" * 29)
    pairs = [("(1+i),(2+i)", pi2, res2, pi5a, res5a),
             ("(2+i),(1+2i)", pi5a, res5a, pi5b, res5b),
             ("(1+i),(3)", pi2, res2, pi9, res9)]
    diamond_all = True
    for label, pa, ra, pb, rb in pairs:
        cab = compose_two(pa, ra, pb, rb)
        cba = compose_two(pb, rb, pa, ra)
        eq = (cab == cba)
        mult1 = all(v == 1 for v in cab.values()) and \
            all(v == 1 for v in cba.values())
        diamond_all = diamond_all and eq and mult1
        check("S2.1 Diamant %s" % label, eq and mult1,
              "p-dann-q == q-dann-p: %s; Endpunkte %d, alle Multiplizitaeten "
              "1: %s (jeder Endpunkt: genau 1 p-Zwischenmodul + 1 q-Zwischen"
              "modul => Branch-Paare mergen in EINEM Schritt)"
              % (eq, len(cab), mult1))

    # gleiche Primstelle: Branchial-Struktur
    print("\n    gleiches Primideal (Branch-Paare mergen NICHT 1:1):")
    for label, pa, ra, hq in [("(1+i)^2", pi2, res2, 2),
                              ("(2+i)^2", pi5a, res5a, 5)]:
        cc = compose_two(pa, ra, pa, ra)
        spec = Counter(cc.values())
        q = hq
        t_exp = gauss_binom_42(q)
        n_tot = (q ** 3 + q ** 2 + q + 1) ** 2
        c_meas = spec.get(1, 0)
        t_meas = spec.get(q + 1, 0)
        ok = (set(spec) == {1, q + 1} and t_meas == t_exp
              and c_meas + (q + 1) * t_meas == n_tot)
        check("S2.2 Branchial-Spektrum %s" % label, ok,
              "Multiplizitaeten %s; Typ-(1,1)-Endpunkte %d == [4,2]_%d = %d "
              "(Grassmann Gr(2,4,F_%d)); zyklisch %d; Ketten %d"
              % (dict(spec), t_meas, q, t_exp, q, c_meas, n_tot))

    # ---------------- S3: Pfad-Zaehlung vs Lambda-Rekursion ------------------
    print("\n--- S3: Zensus-Zellen, Lambda-Rekursion, Kettenzahlen " + "-" * 23)
    iota = ideal_counts(primes, X_NORM)
    a = census_cells(iota, X_NORM)
    ok_census = (a.get(2) == 15 and a.get(5) == 312 and a.get(9) == 820
                 and a.get(13) == 4760 and a.get(4) == 155
                 and a.get(8) == 1395 and a.get(10) == 4680)
    check("S3.1 Zell-Formel == explizite Enumeration + v714-Kalibrierung",
          ok_census,
          "a_2=%s a_4=%s a_5=%s a_8=%s a_9=%s a_10=%s a_13=%s "
          "(v714: 15/155/312/1395/820/4680/4760)"
          % tuple(a.get(k) for k in (2, 4, 5, 8, 9, 10, 13)))

    # Lambda-Extraktion EXAKT: alle Groessen als ganzzahlige Vektoren ueber
    # der Log-Basis {log b}: b = Radikal-Basis der Gauss-Primnormen (ring-
    # intern: b = q falls q kein Quadrat, sonst sqrt(q)); log n hat dann
    # ganzzahlige Koordinaten (Faktorisierung der Schicht-Indizes ist
    # Buchhaltung, kein Prim-Orakel fuer den Kamm).
    bases = sorted({gnorm(p) if math.isqrt(gnorm(p)) ** 2 != gnorm(p)
                    else math.isqrt(gnorm(p)) for p in primes})
    bidx = {b: i for i, b in enumerate(bases)}

    def logvec(n):
        v = [0] * len(bases)
        m = n
        for b in bases:
            while m % b == 0:
                v[bidx[b]] += 1
                m //= b
        assert m == 1, "Index %d faktorisiert nicht ueber die Normbasen" % n
        return tuple(v)

    from fractions import Fraction
    ZV = tuple([0] * len(bases))

    def vadd(u, w, s=1):
        return tuple(a_ + s * b_ for a_, b_ in zip(u, w))

    def vscale(c, u):
        return tuple(c * a_ for a_ in u)

    ns = sorted(k for k in a if k >= 2)
    lam = {}
    for n in ns:
        acc = vscale(Fraction(a[n]), logvec(n))
        for d in ns:
            if d >= n or n % d:
                continue
            if (n // d) in a:
                acc = vadd(acc, vscale(Fraction(a[n // d]), lam[d]), s=-1)
        lam[n] = tuple(Fraction(x) for x in acc)

    # geschlossene Form: Lambda(N(pi)^k) = log N(pi) * sum_{j=0..3} N(pi)^{kj}
    lam_pred = {}
    for p in primes:
        q = gnorm(p)
        k = 1
        while q ** k <= X_NORM:
            n = q ** k
            w = vscale(Fraction(sum(q ** (k * j) for j in range(RANK))),
                       logvec(q))
            lam_pred[n] = vadd(lam_pred.get(n, ZV), w)
            k += 1
    support = sorted(n for n in ns if any(x != 0 for x in lam[n]))
    support_pred = sorted(lam_pred)
    off_zero = all(all(x == 0 for x in lam[n]) for n in ns
                   if n not in lam_pred)
    check("S3.2 Lambda-Support == Primideal-Potenzen (EXAKT)",
          support == support_pred and off_zero,
          "Support %s; Off-Support Lambda == 0 exakt (Bruch-Arithmetik) -- "
          "Lambda(10)=Lambda(18)=...=Lambda(50)=0 IST die Diamant-"
          "Eigenschaft in Log-Form" % (support,))
    closed_ok = all(lam[n] == lam_pred.get(n, ZV) for n in ns)
    check("S3.3 Lambda geschlossene Form (Zell-Summen, EXAKT)", closed_ok,
          "alle Schichten exakt; z.B. Lambda(4) = 85 log2 (85 = 1+4+16+64), "
          "Lambda(25) = 32552 log5 = 2*16276 log5, Lambda(49) = %s log7 "
          "(= 2*(1+49+49^2+49^3), inerte 7: halbe Orbit-Basis log7 = "
          "(1/2) log49)" % (lam[49][bidx[7]],))

    # Kettenzahlen C_n (maximale Ketten L -> Schicht n) + Kreuz-Check
    C = {1: 1}
    h1 = {}
    for p in primes:
        q = gnorm(p)
        h1[q] = q ** 3 + q ** 2 + q + 1
    for n in ns:
        tot = 0
        for p in primes:
            q = gnorm(p)
            if n % q == 0 and (n // q) in C:
                tot += h1[q] * C[n // q]
        C[n] = tot
    # explizite Kreuz-Checks: C_10 aus S2-Zaehlern; per-Endpunkt-Pfadzahl 2
    c10_expl = 0
    for pa, ra, pb, rb in [(pi2, res2, pi5a, res5a), (pi2, res2, pi5b,
                                                      residues_mod(pi5b))]:
        cab = compose_two(pa, ra, pb, rb)
        cba = compose_two(pb, rb, pa, ra)
        c10_expl += sum(cab.values()) + sum(cba.values())
    check("S3.4 Kettenzahl C_10: Rekursion == explizite Zaehlung",
          C[10] == c10_expl == 9360,
          "C_10 = %d (Rekursion) == %d (Enumeration); jeder der 4680 "
          "Endpunkte traegt genau 2 maximale Ketten (Diamant)"
          % (C[10], c10_expl))

    # ---------------- S4: sigma-Klassifikation der Ereignis-Typen ------------
    print("\n--- S4: Kausal-Netz -- sigma-Aktion auf den Ereignis-Schichten " + "-" * 12)
    fix2 = sum(1 for M in lay2 if sigma_module(M) == M)
    s5_img = {sigma_module(M) for M in lay5a}
    swap5 = (s5_img == set(lay5b))
    fix9 = sum(1 for M in lay9 if sigma_module(M) == M)
    fix9_exp = 3 ** 3 + 3 ** 2 + 3 + 1  # F_3-rationale Hyperebenen von F_9^4
    check("S4.1 ramifizierte Schicht (1+i): sigma trivial", fix2 == 15,
          "%d/15 Untermoduln sigma-fix (z-conj(z) = 2 Im z in (1+i))" % fix2)
    check("S4.2 split-Schicht 5: sigma tauscht die Ideal-Schichten frei",
          swap5 and not any(sigma_module(M) == M for M in lay5a),
          "sigma((2+i)-Schicht) == (1+2i)-Schicht: %s; 0 Fixpunkte" % swap5)
    check("S4.3 inerte Schicht (3): Fixpunkte = F_3-rationale Hyperebenen",
          fix9 == fix9_exp,
          "%d sigma-fixe von 820 (erwartet %d = 3^3+3^2+3+1); "
          "(820-%d)/2 = %d freie Paare -- die Zustands-Verfeinerung des "
          "v714-Halborbit-Descents" % (fix9, fix9_exp, fix9,
                                       (820 - fix9) // 2))

    # ---------------- A2 / S5: der 48-Site-Lift als zellulaerer Automat ------
    print("\n--- S5 (A2): 48-Site-Lift als Automat " + "-" * 39)
    NB, NS_ = 16, 3
    marks = {0, 4, 8, 12}

    def step_perm(jw):
        p = {}
        for b in range(NB):
            for s in range(NS_):
                p[(b, s)] = ((b + 1) % NB,
                             (s + (jw if (b + 1) % NB in marks else 0)) % NS_)
        return p

    def n_cycles(p):
        seen, ncyc = set(), 0
        for x in p:
            if x in seen:
                continue
            ncyc += 1
            y = x
            while y not in seen:
                seen.add(y)
                y = p[y]
        return ncyc

    def step_perm_weights(weights):  # weights: dict markpos -> j
        p = {}
        for b in range(NB):
            for s in range(NS_):
                nb = (b + 1) % NB
                p[(b, s)] = (nb, (s + weights.get(nb, 0)) % NS_)
        return p

    cyc_j1 = n_cycles(step_perm(1))
    cyc_j2 = n_cycles(step_perm(2))
    cyc_j0 = n_cycles(step_perm(0))
    alt = step_perm_weights({0: 1, 4: 2, 8: 1, 12: 2})
    cyc_alt = n_cycles(alt)
    check("S5.1 Konnektivitaets-Zensus == v623-V1",
          (cyc_j1, cyc_j2, cyc_j0, cyc_alt) == (1, 1, 3, 3),
          "j=1: %d Zykel, j=2: %d, j=0: %d, alternierend (1,2,1,2): %d "
          "(v623: 1/1/3/3)" % (cyc_j1, cyc_j2, cyc_j0, cyc_alt))

    stp = step_perm(1)

    def perm_pow(p, k):
        out = {x: x for x in p}
        for _ in range(k):
            out = {x: p[out[x]] for x in out}
        return out

    L = perm_pow(stp, 4)
    deck = {(b, s): (b, (s + 1) % NS_) for b in range(NB) for s in range(NS_)}
    L4 = perm_pow(stp, 16)
    ordL = next(k for k in range(1, 49)
                if perm_pow(L, k) == {x: x for x in L})
    check("S5.2 Uhr: L^4 == Deck, ord(L) == 12", L4 == deck and ordL == 12,
          "L^4 == deck: %s; ord(L) = %d" % (L4 == deck, ordL))

    # Walk-Koordinate: L = reiner Shift um 4 (Radius-4-Lokalitaet)
    walk = [(0, 0)]
    for _ in range(47):
        walk.append(stp[walk[-1]])
    widx = {x: i for i, x in enumerate(walk)}
    shifts = {(widx[L[x]] - widx[x]) % 48 for x in walk}
    check("S5.3 Update-Regel explizit: L = Shift um 4 in Walk-Koordinaten",
          shifts == {4},
          "Shift-Menge %s -- ein zyklischer Shift-Automat, Radius 4 "
          "(lokal); Deck = Shift um 16" % shifts)

    # Deck-Sektor-Erhaltung: exakt, aber trivial (Shift kommutiert mit Shift)
    commLD = all(L[deck[x]] == deck[L[x]] for x in L)
    Pmat = np.zeros((48, 48), dtype=complex)
    for x in L:
        Pmat[widx[L[x]], widx[x]] = 1.0
    Dmat = np.zeros((48, 48), dtype=complex)
    for x in deck:
        Dmat[widx[deck[x]], widx[x]] = 1.0
    om = np.exp(2j * np.pi / 3)
    projs = [sum(om ** (-c * t) * np.linalg.matrix_power(Dmat, t)
                 for t in range(3)) / 3.0 for c in range(3)]
    mix_L = max(np.abs(projs[c1] @ Pmat @ projs[c2]).max()
                for c1 in range(3) for c2 in range(3) if c1 != c2)
    # Kontrolle: lokale Nicht-Shift-Regel (Transposition der Walk-Sites 0,1)
    Tmat = np.eye(48, dtype=complex)
    Tmat[[0, 1]] = Tmat[[1, 0]]
    Pbad = Tmat @ Pmat
    mix_bad = max(np.abs(projs[c1] @ Pbad @ projs[c2]).max()
                  for c1 in range(3) for c2 in range(3) if c1 != c2)
    check("S5.4 Deck-Sektoren erhalten -- weil [L, Deck] = 0 (trivial fuer "
          "Shifts); Kontrolle bricht",
          commLD and mix_L < 1e-12 and mix_bad > 0.1,
          "[L,deck]=0: %s; Sektor-Mixing L: %.1e; Mixing der lokalen "
          "Nicht-Shift-Kontrolle: %.3f -- die 'Erhaltungsgroesse' ist exakt "
          "v623s L^4=deck, KEINE neue Invariante" % (commLD, mix_L, mix_bad))

    # ---------------- A4 / S6: der Code als endlicher Automat ----------------
    print("\n--- S6 (A4): (F2^4, sigma) als Permutations-Automat " + "-" * 25)
    states = list(product((0, 1), repeat=4))  # (anchor, f1, f2, f3)

    def sig(v):
        return (v[0], v[3], v[1], v[2])  # 3-Zykel auf den Familien-Bits

    cyc_len = Counter()
    seen = set()
    for v in states:
        if v in seen:
            continue
        orb = [v]
        w = sig(v)
        while w != v:
            orb.append(w)
            w = sig(w)
        seen.update(orb)
        cyc_len[len(orb)] += 1
    burnside = (15 + 3 + 3) // 3
    n_orb_nz = (cyc_len[1] - 1) + cyc_len[3]  # Orbits auf V \ {0}
    check("S6.1 Zykeltyp 1^4 3^4; Burnside-Orbits auf V\\{0} == 7 (v736)",
          cyc_len == Counter({1: 4, 3: 4}) and n_orb_nz == 7 == burnside,
          "Zykeltyp %s; Orbits auf V\\{0}: %d; Transitionsgruppe C3 -- "
          "reversibel, KEINE echten Attraktoren (nur Orbits)"
          % (dict(cyc_len), n_orb_nz))

    # Hyperebenen-Kanaele (Charaktere): sigma-Orbit-Zensus 3 + 4x3
    funcs = [f for f in states if f != (0, 0, 0, 0)]
    fixed_f = [f for f in funcs if sig(f) == f]
    check("S6.2 sigma-Orbit-Zensus der 15 Hyperebenen == 3 fix + 4 Drei-"
          "Zykel (7 Kanaele, hecke_mod_ramified)",
          len(fixed_f) == 3 and (15 - 3) % 3 == 0 and (15 - 3) // 3 == 4,
          "3 sigma-fixe Charaktere + 4 freie Drei-Orbits = 7 nichttriviale "
          "Kanaele (+1 trivial); ungerade Hecke-Schichten wirken als "
          "deg*id (ZITAT hecke_mod_ramified_probe) => als Automaten-"
          "Homomorphismen TRIVIAL, Struktur nur an der ramifizierten Stelle")

    # ---------------- A3 / S7: Irreduzibilitaets-Typisierung (Zitate) --------
    print("\n--- S7 (A3): Computational Irreducibility, quantitativ " + "-" * 21)
    # ZITATE aus verification/v702_z1_lookahead.py, deterministischer
    # Re-Lauf 2026-08-04 (13 PASS / 0 FAIL, 0.5 min):
    CITED_G_POS = 5.5      # Positions-Gain pro Slot (L1.2)
    CITED_G_MASS = 12.0    # Massen-Gain pro Slot (L1.3)
    CITED_EPS = 0.035      # pro-Slot-Residuum in Zellen (L3.1)
    CITED_TOL_LO = 0.15    # Peak-Breite (engste Becken-Skala, L3.1)
    CITED_TOL_HI = 1.0     # B1-Akzeptanz |du| <= 1 Zelle
    CITED_BREAK_LO, CITED_BREAK_HI = 3, 4  # Bruch: Slot 3 (Beam) / 4 (Masse)
    n_lo = 1 + math.log(CITED_TOL_LO / CITED_EPS) / math.log(CITED_G_MASS)
    n_hi = 1 + math.log(CITED_TOL_HI / CITED_EPS) / math.log(CITED_G_POS)
    ok_win = (n_hi >= CITED_BREAK_LO - 0.5 and n_lo <= CITED_BREAK_HI)
    check("S7.1 Lyapunov-Lesart konsistent: N* = 1 + ln(tol/eps)/ln g "
          "umschliesst das Bruchfenster", ok_win,
          "N* in [%.1f, %.1f] (eps=%.3f, tol %.2f-%.1f, g %.1f-%.1f) vs "
          "gemessener Bruch Slot %d-%d (v702-Eigenrechnung: 1.7 Slots); "
          "lambda = ln g in [%.2f, %.2f] nats/Slot"
          % (n_lo, n_hi, CITED_EPS, CITED_TOL_LO, CITED_TOL_HI,
             CITED_G_POS, CITED_G_MASS, CITED_BREAK_LO, CITED_BREAK_HI,
             math.log(CITED_G_POS), math.log(CITED_G_MASS)))
    check("S7.2 Typisierung (Zitat, kein neues Experiment)", True,
          "VERIFIZIERER: voller Kamm 913 >= 898, jeder Fake stirbt >= 184 "
          "Lags frueher; GENERATOR: nein (autonom 2-4 Slots; g_pos=5.5, "
          "g_mass=12.0, konditioniert ~18 Bits/Slot) -- die Atom-"
          "Schicht ist relativ zur Fluss-Aufloesung computationally "
          "irreducible, die Arch-Schicht (geschlossene Gamma-Formen) "
          "reducible; PRUEFBARE Skalierungs-Vorhersage der Lesart: "
          "N* waechst nur LOGARITHMISCH mit dem Praezisions-Budget "
          "(eps -> eps/2 gibt +ln2/ln g ~ +0.3-0.4 Slots)")

    # ---------------- S8: Adjudikation ---------------------------------------
    print("\n--- S8: Adjudikation " + "-" * 56)
    adjud = [
        ("A1 Turm=Multiway", "AEQUIVALENT-NUETZLICH",
         "Konfluenz/Diamant = Hecke-Kommutativitaet = CRT (Theorem, exakt "
         "gemessen); Lambda-Rekursion = Log-Ableitung des Zensus (v714 "
         "umbenannt); NEU nur der Fingerabdruck: Branchial-Spektrum {1,q+1} "
         "mit [4,2]_q Grassmann-Zaehlung + die Lesart des Zell-"
         "Normalisierers als Branchial-Volumen"),
        ("A2 Lift=CA", "UMBENENNUNG",
         "L = Shift-Automat (Radius 4); Deck-Sektor-'Erhaltung' ist fuer "
         "Shifts trivial -- exakt v623 L^4=deck, nichts Neues"),
        ("A3 Irreduzibilitaet", "AEQUIVALENT-NUETZLICH",
         "v702s Verifizierer-nicht-Generator wird als messbare "
         "Irreduzibilitaet typisiert (lambda = ln g); eine pruefbare "
         "log-Skalierungs-Vorhersage, aber keine neue Messung hier"),
        ("A4 Code=DFA", "UMBENENNUNG",
         "Permutations-Automat C3; 'Attraktoren' sind nur Orbits (Burnside "
         "7 = v736); Hecke-Kanaele als Homomorphismen ungerade trivial"),
    ]
    for name, verdict, why in adjud:
        print("    %-22s %-24s %s" % (name, verdict, why))

    overall = "GEMISCHT"
    print("\nGESAMT-VERDIKT: %s -- die Zuse/Wolfram-Lesart ist fuer die "
          "neuen Strukturen KEIN eigenstaendiges Forschungsprogramm und "
          "KEINE reine Erzaehl-Schicht: A2/A4 sind Umbenennungen, A1/A3 "
          "liefern nuetzliche Typisierungen mit je EINEM konkreten "
          "Anschluss-Test (Branchial-Zensus an weiteren Primschichten; "
          "log-Skalierung des autonomen Horizonts)." % overall)

    dt = time.time() - t0
    print("\n" + "=" * 78)
    n_fail = len(FAILURES)
    print("SUMMARY: %d PASS / %d FAIL (%.1f s)"
          % (CHECKS[0] - n_fail, n_fail, dt))
    if FAILURES:
        for f in FAILURES:
            print("  FAIL: %s" % f)
    print("=" * 78)
    return n_fail


if __name__ == "__main__":
    sys.exit(1 if run() else 0)
