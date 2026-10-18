#!/usr/bin/env python3
"""look_elsewhere_probe.py -- LOOKELSEWHERE.01: das Bingo-Budget der
getypten [C]-Koinzidenz-Beobachtungen, quantifiziert.

Die haerteste quantitative Anti-Numerologie-Waffe: fuer jede aktuell im
Korpus getypte numerische [C]-Koinzidenz wird EHRLICH gezaehlt, wie viele
Kandidaten-"Slots" die Struktur-Seite anbot (das Budget), und wie
wahrscheinlich ein zufaelliges Struktur-Zahlen-Set gleicher Groesse und
Groessenverteilung mindestens ebenso viele Treffer in der VOR der Rechnung
eingefrorenen Compiler-Ziel-Liste landet.  Methodik-Vorbild:
verification/v100_numerology_null_mc.py (exakter Look-Elsewhere-Zensus +
MC + Negativ-Kontrollen + Fairness-Checks; dort 13/13 vs 200k Pseudo-
Theorien).  Dieses Modul wendet denselben Standard auf die NEUEN
diskreten Koinzidenzen der E8.CODE/CODESEM/INCIDENCE/ST31/EXTREV-Runden an.

RADIKALE EHRLICHKEIT: Ziel ist NICHT, alle Beobachtungen zu retten.
Beobachtungen, die unter dem Null-Modell unauffaellig sind, werden GENAU SO
dokumentiert (das ist der Wert des Moduls: es trennt selbst).  Erzwungene
Treffer (mathematisch eindeutig bestimmte Zahlen, z.B. die Parameter des
eindeutigen selbstdualen [8,4,4]-Codes) tragen KEINE freie Koinzidenz-
Masse und werden als FORCED gekennzeichnet.

L1 [ZENSUS]: die getypten [C]-Beobachtungen (a)-(h), gruppiert in sechs
    Budget-Einheiten B1-B6 (Analyse-Einheit = Modul/Zensus-Familie):
      (a) 60 = D_start als freier Clock-Orbit-Zaehler   (v629 R3 / v633 Q1)
      (b) 12 sigma-fixierte Wurzeln = 12 gehobene Marks (v629 R3)
      (c) G31-Grade (8,12,20,24) <-> (Rang, Uhr-Ordnung, 240/12, |W(A3)|)
                                                        (v634 T2 / v647)
      (d) 48 = 240/5 (u^4-Zensus {5:48}) = Omega_adm    (v647 S3)
      (e) 14 = A_4 des Hamming-Codes = 2 x 7 Parabolik  (v626 E5)
      (f) 16 = |C| = Traeger-Halbspinor = Seam-Sites    (v626 E5)
      (g) 6  = Index der Lorentz-Kongruenz = p_2(a)     (v624 C2)
      (h) CODESEM-Batterie: Anker-Norm 6 = (1,1,2).(1,1,2) u.a.
                                                        (v638 / v646 R2)
    NICHT einbezogen als Beobachtung (bereits GETOETET, zaehlen als
    Disziplin-Erfolge und gehen ins Trial-Budget): 46080 = |W(D5)|x|W(A3)|
    als Untergruppen-Lesart (v634 T1 KILL), p_n = 2+2^n Bytecode-Code-
    Lesart (v646 R2.4 KILL, 0/11 Familien), c = w^2 (v647 S2 KILL),
    48 x 5-Inzidenz (v629 R2 KILL), 60 -> 6 Kaskaden-Quotient (v633 Q8
    KILL), naive Placement-Semantik (v638 S4 KILL).

L2 [NULL-MODELLE]: pro Budget-Einheit die eingefrorene Slot-Liste
    (alle im Docstring/Ledger AUFGETAUCHTEN Zahlen 2..300, abzueglich
    Konstruktions-Inputs, Input-Echos, woertlicher Fakten-Duplikate und
    0/1-Trivia -- Regel im CONFIG-Block).  Drei Null-Modelle:
      U  uniform auf [2, 300]
      D  teilergewichtet auf [2, 300] (P(n) ~ d(n); Gruppen-/Gitter-
         Invarianten sind zu glatten Zahlen verzerrt -- wie die Ziele)
      M  groessengefenstert: Slot s -> uniform auf [ceil(s/2), min(2s,300)]
         (das "gleiche Groesse/Verteilung"-Modell; fuer kleine Zahlen
         BRUTAL ehrlich, weil kleine Ziele dicht liegen)
    Exakte Poisson-Binomial-Tails (Fraction-DP) + 100k-MC (Seed fixiert)
    als Kreuzcheck.  Pro Beobachtung: roher Match (1/|Fenster|),
    Budget n, korrigiertes p pro Modell, p_max = konservativstes Modell.

L3 [FAMILIEN-KORREKTUR]: globales Look-Elsewhere-korrigiertes p ueber
    ALLE Budget-Slots gemeinsam (N Slots, K Treffer), zusaetzlich mit den
    getoeteten Kandidaten als 0-Treffer-Trials (Kills VERGROESSERN das
    korrigierte p -- die ehrliche Richtung).  Lesarten-Ebene separat
    dokumentiert: 6 bestaetigte vs 6 getoetete Struktur-Lesarten.

L4 [KONTROLLE]: (A) 2000 zufaellige Pseudo-Ziel-Listen gleicher Groesse
    und Groessenverteilung -- deren korrigierte p muessen unauffaellig
    verteilt sein; Perzentil der echten Liste = empirische Familien-
    Korrektur ueber die Theorie-Wahl selbst.  (B) Kalibrierung: 2000
    synthetische Slot-Ziehungen unter M gegen die ECHTE Ziel-Liste;
    die p-Werte muessen konservativ-uniform sein.

L5 [FAZIT]: ehrliche Dreiteilung nach p_max: SIGNIFIKANT (p < 0.01),
    SUGGESTIV (0.01..0.1), UNAUFFAELLIG (> 0.1 -> "Beobachtung ohne
    statistisches Gewicht", namentlich gelistet).  Fertiger Diary-/
    Ledger-Notiz-Text wird ausgegeben.

Verdikt-Enums (eingefroren): LOOKELSEWHERE-QUANTIFIED (alle Checks PASS;
die Dreiteilung selbst ist ERGEBNIS, kein Check), MIXED, MACHINERY-FAILS.

FIREWALL: Sandbox-Probe in experiments/tfpt-discovery/ -- KEINE Marker-
Aenderungen, KEINE Ledger-/Paper-/Website-Edits; die empfohlenen
Re-Typisierungen sind VORSCHLAGSTEXT fuer den Diary/Ledger-Workflow.
Standalone, nur Standardbibliothek, exakte Arithmetik wo moeglich.

PROVENANCE der eingefrorenen Zahlen: v624_external_lattice_audit.py,
v626_e8_code.py, v629_root_incidence.py, v633_orbit60_quotient.py,
v634_st31_structure.py, v638_code_semantics.py, v646_rm13_reverse.py,
v647_st31_degree24.py, status_ledger.csv (EXTREV.LATTICE.01, E8.CODE.01,
E8.CODESEM.01, E8.INCIDENCE.01, E8.ZIQUOTIENT.01, E8.ST31.01,
E8.ST31DEG.01, E8.RM13REV.01); B1 und B5 werden im Modul unabhaengig
re-deriviert (exakt), B2/B3/B4/B6 sind mit Quellenangabe eingefroren.

Ausfuehren:
  experiments/tfpt-discovery/.venv/bin/python \
      experiments/tfpt-discovery/look_elsewhere_probe.py
"""

import itertools
import random
import time
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from math import comb

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


# ======================================================================
# L0: EINGEFRORENE KONFIGURATION (vor jeder Rechnung fixiert)
# ======================================================================
SEED = 20260802          # Datum der E8.CODE/CODESEM/ST31-Runden
MC_TRIALS = 100_000      # MC-Samples pro Tail (Aufgabenvorgabe)
N_MAX = 300              # Zahlenuniversum [2, N_MAX]
R_CONTROL = 2000         # Pseudo-Ziel-Listen / Kalibrierungs-Ziehungen
P_SIG = 0.01             # SIGNIFIKANT-Schwelle
P_SUG = 0.10             # SUGGESTIV-Schwelle

# ---- die eingefrorene Compiler-Ziel-Liste T (VOR der Rechnung) -------
# Begruendung aus dem Korpus (rg-verifizierte Quellen); Wert 1 gehoert
# formal dazu (unimodulare Determinante, mu-Index 1), wird aber auf
# beiden Seiten von der 0/1-Trivia-Regel vom Scoring ausgeschlossen.
TARGETS_SRC = [
    (1,   "unimodulare det(E8) = 1; mu-Index 1 (v92/v234) -- Trivia, kein Scoring"),
    (2,   "e3 = 2 Blatt-Involution; |Z2| (v624 B; chi_a = (t-1)^2(t-2))"),
    (3,   "N_fam = 3 Familien (tfpt_constants: (2^4-1)/5)"),
    (4,   "d = 4 Marks = |mu4| (AX.P2.01; v624 A: dreifach erzwungen)"),
    (5,   "g_car = 5 Traeger (Axiom P2)"),
    (6,   "p_2(a) = 6 = A3-Positivwurzeln; (1,1,2).(1,1,2) (v624 C2)"),
    (7,   "7-dim Parabolik (v600; QGEO.EQORDER.01)"),
    (8,   "rank(E8) = 8 = g_car + N_fam (tfpt_constants)"),
    (12,  "Uhr-Ordnung |<J,sigma>| = 12; 12 gehobene Marks (v623/v629)"),
    (14,  "2 x 7 Parabolik-Dimension; v605-Nenner 14 (E8.CODE.01)"),
    (16,  "dim S+ = 2^(g_car-1) = 16 Seam-Sites (tfpt_constants; v512)"),
    (20,  "240/12 = 20 freier Kamm (v634 T2)"),
    (24,  "|W(A3)| = 24 (v5-IR-Produkt 46080 = 1920 x 24)"),
    (27,  "Saturationsindex 3^3 = 27 (QGEO.EQORDER.01)"),
    (48,  "Omega_adm = N_fam x dim S+ = 48 (tfpt_constants)"),
    (60,  "D_start = 60 Kaskadenstart (v5; v37)"),
    (81,  "Parabolik-Index 3^4 = 81 (v600; QGEO.EQORDER.01)"),
    (240, "|R(E8)| = 240 (v5/v625/v626)"),
    (248, "dim E8 = 248 (v624 B: 240 + 8)"),
]
TARGETS = [t for t, _ in TARGETS_SRC]
T_EFF = sorted(t for t in TARGETS if 2 <= t <= N_MAX)   # Scoring-Ziele
T_SET = set(T_EFF)

# ---- Null-Modell-Bausteine ------------------------------------------


def window(s):
    """Groessenfenster W(s) = [max(2, ceil(s/2)), min(2s, N_MAX)]."""
    lo = max(2, (s + 1) // 2)
    hi = min(2 * s, N_MAX)
    return lo, hi


def win_size(s):
    lo, hi = window(s)
    return hi - lo + 1


def targets_in_window(s):
    lo, hi = window(s)
    return [t for t in T_EFF if lo <= t <= hi]


# Teilerfunktion d(n) auf [2, N_MAX] (Sieb)
DIV = [0] * (N_MAX + 1)
for d_ in range(1, N_MAX + 1):
    for m_ in range(d_, N_MAX + 1, d_):
        DIV[m_] += 1
D_SUM = sum(DIV[2:N_MAX + 1])
D_TGT = sum(DIV[t] for t in T_EFF)

# EINGEFRORENE SLOT-REGEL (gilt fuer alle Budgets):
#   Slots = alle im Modul-Docstring / Ledger-Eintrag AUFGETAUCHTEN
#   ganzzahligen Rechen-OUTPUTS (Zensus-, Orbit-, Ordnungs-, Index-,
#   Determinanten-, Dimensions-Zahlen) im Bereich [2, 300], distinct
#   pro Budget, ABZUEGLICH:
#     (i)   deklarierte Konstruktions-Inputs und ihre Echos
#     (ii)  woertliche Re-Derivationen desselben Fakts (Anti-Doppelzaehlung)
#     (iii) Parameter-Echos (Zahlen, die arithmetisch aus bereits
#           budgetierten Zahlen der Konstruktion folgen)
#     (iv)  0/1-Trivia und Werte quadratischer Formen (durch Konstruktion
#           beschraenkt)
#     (v)   Zahlen > 300 (46080, 11520, 720, 768, 1770, 2160 -- notiert)
#   Kompositions-Treffer (240+8 = 248, 60 = 7+11+19+23, 46080 = 1920*24)
#   sind eine ANDERE Grammatik und werden separat dokumentiert, nicht
#   in T gescort.

# ======================================================================
# L1a: Re-Derivation B1 -- der v629/v633-Orbit-Zensus (exakt, doubled)
# ======================================================================
section("L1a: Re-Derivation B1 -- Clock/sigma-Zensus auf den 240 Wurzeln")

_roots = []
for v in itertools.product(range(-1, 2), repeat=8):
    if sum(a * a for a in v) == 2 and sum(v) % 2 == 0:
        _roots.append(tuple(2 * a for a in v))
n_int = len(_roots)
for y in itertools.product((0, -1), repeat=8):
    v = tuple(2 * a + 1 for a in y)
    if sum(a * a for a in v) == 8 and sum(v) % 4 == 0:
        _roots.append(v)
n_half = len(_roots) - n_int
ROOTS240 = _roots
RSET240 = set(ROOTS240)


def J_vec(x):
    out = []
    for i in range(0, 8, 2):
        a, b = x[i], x[i + 1]
        out += [-b, a]
    return tuple(out)


def sig_vec(x):
    return (x[4], x[5], x[0], x[1], x[2], x[3], x[6], x[7])


def census(f):
    seen, cen = set(), Counter()
    for x in ROOTS240:
        if x in seen:
            continue
        orb = [x]
        y = f(x)
        while y != x:
            orb.append(y)
            y = f(y)
        seen.update(orb)
        cen[len(orb)] += 1
    return dict(cen)


cen_J = census(J_vec)
cen_J2 = census(lambda x: J_vec(J_vec(x)))
cen_sig = census(sig_vec)
cen_g = census(lambda x: J_vec(sig_vec(x)))
check("B1-Rederivation: 240 Wurzeln (112 + 128), J frei {4: 60}, "
      "J^2 {2: 120}, sigma {1: 12, 3: 76}, g = J o sigma {12: 19, 4: 3}",
      len(ROOTS240) == 240 and n_int == 112 and n_half == 128
      and cen_J == {4: 60} and cen_J2 == {2: 120}
      and cen_sig == {1: 12, 3: 76} and cen_g == {12: 19, 4: 3},
      "J %s | J^2 %s | sigma %s | g %s"
      % (cen_J, cen_J2, cen_sig, cen_g))

# ======================================================================
# L1b: Re-Derivation B5 -- die 42er-Invarianten-Batterie (v638/v646)
# ======================================================================
section("L1b: Re-Derivation B5 -- Hamming-Placement C* und die Batterie")

G_NAIVE = [(1, 0, 0, 0, 0, 1, 1, 1),
           (0, 1, 0, 0, 1, 0, 1, 1),
           (0, 0, 1, 0, 1, 1, 0, 1),
           (0, 0, 0, 1, 1, 1, 1, 0)]
C_NAIVE = frozenset(tuple(sum(m[k] * G_NAIVE[k][j] for k in range(4)) % 2
                          for j in range(8))
                    for m in itertools.product((0, 1), repeat=4))
PI_J = (1, 0, 3, 2, 5, 4, 7, 6)
PI_SIG = (4, 5, 0, 1, 2, 3, 6, 7)
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7)]


def apply_perm(c, p):
    return tuple(c[p[k]] for k in range(8))


def compose(p, q):
    return tuple(q[p[k]] for k in range(8))


def code_image(code, p):
    return frozenset(apply_perm(c, p) for c in code)


all_placements = set()
for p in itertools.permutations(range(8)):
    all_placements.add(code_image(C_NAIVE, p))
both_inv = sorted((c for c in all_placements
                   if code_image(c, PI_J) == c and code_image(c, PI_SIG) == c),
                  key=sorted)
T67 = (0, 1, 2, 3, 4, 5, 7, 6)
check("B5-Rederivation: 30 S8-Placements, EXAKT 2 beide-invariant, "
      "durch (67) vertauscht",
      len(all_placements) == 30 and len(both_inv) == 2
      and code_image(both_inv[0], T67) == both_inv[1])
CSTAR = both_inv[0]

# Syndrome ueber 4 unabhaengige Codewoerter (selbstdual: dual = Code)
basis, red = [], []
for w in sorted(CSTAR):
    r = list(w)
    for b in red:
        piv = next(i for i, x in enumerate(b) if x)
        if r[piv]:
            r = [(a + c) % 2 for a, c in zip(r, b)]
    if any(r):
        red.append(tuple(r))
        basis.append(w)
    if len(basis) == 4:
        break
SYND = {}
for v in itertools.product((0, 1), repeat=8):
    SYND[v] = tuple(sum(a * b for a, b in zip(v, h)) % 2 for h in basis)
S0 = SYND[(0,) * 8]
cosets = defaultdict(list)
for v in SYND:
    cosets[SYND[v]].append(v)
LEADERS = {}
for s, vs in cosets.items():
    m = min(sum(v) for v in vs)
    LEADERS[s] = (m, sum(1 for v in vs if sum(v) == m))


def e(i):
    return tuple(1 if k == i else 0 for k in range(8))


q_syn = set(tuple((a + b) % 2 for a, b in zip(SYND[e(2 * k)],
                                              SYND[e(2 * k + 1)]))
            for k in range(4))
check("B5-Rederivation: universelles In-Paar-Syndrom q (1 Wert fuer "
      "alle 4 Paare), Leader-Zensus {0: 1, 1: 8, 2: 7}",
      len(q_syn) == 1
      and dict(Counter(w for w, _ in LEADERS.values())) == {0: 1, 1: 8, 2: 7})
q_syn = q_syn.pop()

# induzierte sigma-Wirkung auf den Syndromen (wohl-definiert fuer C*)
img = {}
well = True
for v in SYND:
    s, si = SYND[v], SYND[apply_perm(v, PI_SIG)]
    if s in img and img[s] != si:
        well = False
    img[s] = si
fixed_synd = [s for s in img if img[s] == s]
anchor_norm = sum(LEADERS[s][0] ** 2 for s in fixed_synd if s != S0)
check("B5-Rederivation: sigma auf Syndromen wohl-definiert; 4 fixierte "
      "Syndrome {0, s(e6), s(e7), q}; Anker-Norm = 6",
      well and len(fixed_synd) == 4 and q_syn in fixed_synd
      and anchor_norm == 6)

# Konstruktion-A-Wurzeln von C* (Norm 4, x mod 2 in C*)
ROOTS_A = []
for w in CSTAR:
    supp = [i for i in range(8) if w[i]]
    if len(supp) == 4:
        for signs in itertools.product((1, -1), repeat=4):
            x = [0] * 8
            for i, sgn in zip(supp, signs):
                x[i] = sgn
            ROOTS_A.append(tuple(x))
for i in range(8):
    for sgn in (2, -2):
        x = [0] * 8
        x[i] = sgn
        ROOTS_A.append(tuple(x))
root_class = Counter(tuple(v % 2 for v in x) for x in ROOTS_A)
RSET_A = set(ROOTS_A)
seen, n_lines, lines_ok = set(), 0, True
for x in ROOTS_A:
    if x in seen:
        continue
    orb = [x]
    y = J_vec(x)
    while y != x:
        lines_ok &= (y in RSET_A)
        orb.append(y)
        y = J_vec(y)
    seen.update(orb)
    n_lines += 1
sig_fixed_roots = [x for x in ROOTS_A if apply_perm(x, PI_SIG) == x]
check("B5-Rederivation: 240 Konstruktion-A-Wurzeln, 15 wurzeltragende "
      "Codewoerter x 16, 60 Clock-Orbits, 12 sigma-fixierte Wurzeln",
      len(ROOTS_A) == 240 and len(root_class) == 15
      and set(root_class.values()) == {16} and lines_ok and n_lines == 60
      and len(sig_fixed_roots) == 12)

# Z6-Orbits
Z6 = {tuple(range(8))}
frontier = [tuple(range(8))]
while frontier:
    p = frontier.pop()
    for g in (PI_J, PI_SIG):
        r = compose(g, p)
        if r not in Z6:
            Z6.add(r)
            frontier.append(r)
Z6 = sorted(Z6)


def orbits_words(words, perms):
    seen_l, orbs = set(), []
    for w in sorted(words):
        if w in seen_l:
            continue
        orb, fr = {w}, [w]
        while fr:
            u = fr.pop()
            for p in perms:
                v = apply_perm(u, p)
                if v not in orb:
                    orb.add(v)
                    fr.append(v)
        seen_l.update(orb)
        orbs.append(orb)
    return orbs


def subset_image(S, p):
    return frozenset(k for k in range(8) if p[k] in S)


def orbits_subsets(subsets, perms):
    seen_l, orbs = set(), []
    for s in sorted(subsets, key=sorted):
        if s in seen_l:
            continue
        orb, fr = {s}, [s]
        while fr:
            u = fr.pop()
            for p in perms:
                v = subset_image(u, p)
                if v not in orb:
                    orb.add(v)
                    fr.append(v)
        seen_l.update(orb)
        orbs.append(orb)
    return orbs


w4_star = [w for w in CSTAR if sum(w) == 4]
info_sets = [frozenset(s) for s in itertools.combinations(range(8), 4)
             if frozenset(s) not in
             {frozenset(i for i in range(8) if w[i]) for w in w4_star}]
w4_all = [w for w in itertools.product((0, 1), repeat=8) if sum(w) == 4]

# die 42er-Batterie (Spiegel von v646 R2, add()-Reihenfolge)
INV = []


def add(name, value):
    INV.append((name, int(value)))


leader_census = Counter(w for w, _ in LEADERS.values())
add("Ueberdeckungsradius", max(leader_census))
for wt, cnt in sorted(leader_census.items()):
    add("#Cosets mit Leader-Gewicht %d" % wt, cnt)
n_leaders = Counter(nl for _, nl in LEADERS.values())
for nl, cnt in sorted(n_leaders.items()):
    add("#Cosets mit %d Leadern" % nl, cnt)
dist_types = Counter()
for s in set(SYND.values()):
    dist = tuple(sorted(Counter(sum(v) for v in SYND
                                if SYND[v] == s).items()))
    dist_types[dist] += 1
for dist, mult in sorted(dist_types.items()):
    for wgt, cnt in dist:
        add("Coset-Verteilung (Typ x%d): #Gewicht-%d-Woerter"
            % (mult, wgt), cnt)
for r in range(1, 5):
    add("|B_%d| Kugelvolumen" % r, sum(comb(8, i) for i in range(r + 1)))
add("n (Laenge)", 8)
add("k (Dimension)", 4)
add("d (Minimalabstand)", 4)
add("#Codewoerter", 16)
add("#Syndrome", 16)
add("A_4 (#Gewicht-4-Woerter)", len(w4_star))
add("#Konstruktion-A-Wurzeln", len(ROOTS_A))
add("#wurzeltragende Codewoerter", len(root_class))
add("Wurzeln pro tragendem Codewort", 16)
add("Wurzeln + n (E8-Dimension)", len(ROOTS_A) + 8)
add("#Clock-Orbits (Wurzeln/4)", n_lines)
add("#sigma-fixierte Wurzeln", len(sig_fixed_roots))
add("#sigma-fixierte Syndrome", len(fixed_synd))
add("Anker-Norm (sigma-fixe Syndrome != 0)", anchor_norm)
add("#Paar-Unionen im Code", sum(
    1 for k1 in range(4) for k2 in range(k1 + 1, 4)
    if tuple(1 if i in PAIRS[k1] + PAIRS[k2] else 0
             for i in range(8)) in CSTAR))
sig_fixed_cw = [w for w in CSTAR if apply_perm(w, PI_SIG) == w]
add("#sigma-fixierte Codewoerter", len(sig_fixed_cw))
add("#sigma-Orbits auf den 16 Codewoertern",
    len(orbits_words(CSTAR, [PI_SIG])))
add("#Informationsmengen", len(info_sets))
add("#Z6-Orbits der Informationsmengen",
    len(orbits_subsets(info_sets, Z6)))
add("#Z6-Orbits auf allen 70 Gewicht-4-Woertern",
    len(orbits_words(w4_all, Z6)))
add("#Z6-Orbits auf F2^8",
    len(orbits_words(list(itertools.product((0, 1), repeat=8)), Z6)))
add("#beide-invariante Placements", len(both_inv))

check("B5-Rederivation: Batterie hat 42 Eintraege; Anker (A_4 = 14, "
      "Info-Mengen 56, Z6-Info-Orbits 10, Radius 2, Kugeln 9/37/93/163, "
      "Paar-Unionen 6) exakt",
      len(INV) == 42 and len(w4_star) == 14 and len(info_sets) == 56
      and dict(INV)["#Z6-Orbits der Informationsmengen"] == 10
      and dict(INV)["Ueberdeckungsradius"] == 2
      and [dict(INV)["|B_%d| Kugelvolumen" % r] for r in (1, 2, 3, 4)]
      == [9, 37, 93, 163]
      and dict(INV)["#Paar-Unionen im Code"] == 6)

# B5-Slots nach der eingefrorenen Regel ableiten:
#   Ausschluesse (dokumentiert):
#     240  = #Wurzeln (E8-Echo, Fakt von v625/v626)
#     248  = 240 + 8 (KOMPOSITIONS-Grammatik, separat notiert)
#     8/4/16 = Code-Parameter n, k, d, |C|, #Syndrome, Wurzeln-pro-CW
#              (B4-Fakten bzw. deren Echos)
#     14   = A_4 (woertlich der B4-Fakt E1.1)   [der Z6-w4-Orbitwert 14
#            ist ein NEUER Fakt und bleibt Slot]
#     60/12 = Clock-Orbits / sigma-fixe Wurzeln (woertliche B1-Fakten,
#            im Code-Rahmen reproduziert)
#     0/1  = Trivia
B5_EXCLUDE_DUP = {240, 248, 60, 12}
B5_PARAM_ECHO_NAMES = {"n (Laenge)", "k (Dimension)", "d (Minimalabstand)",
                       "#Codewoerter", "#Syndrome",
                       "Wurzeln pro tragendem Codewort",
                       "A_4 (#Gewicht-4-Woerter)",
                       "#Konstruktion-A-Wurzeln",
                       "Wurzeln + n (E8-Dimension)",
                       "#Clock-Orbits (Wurzeln/4)",
                       "#sigma-fixierte Wurzeln"}
b5_vals = sorted({v for name, v in INV
                  if 2 <= v <= N_MAX and v not in B5_EXCLUDE_DUP
                  and name not in B5_PARAM_ECHO_NAMES})
print("  B5-Slots (nach Regel): %s" % b5_vals)

# ======================================================================
# L1c: die eingefrorenen Budgets B1-B6 (Slots mit Quellen)
# ======================================================================
section("L1c: Budgets B1-B6 (eingefrorene Slot-Listen mit Quellen)")

BUDGETS = {
    "B1": dict(
        label="v629/v633 Clock/sigma-Orbit-Zensus",
        slots=[(60, "J-Orbits, frei (v629 R3)"),
               (120, "J^2-Orbits (v629 R4)"),
               (12, "sigma-fixierte Wurzeln (v629 R3)"),
               (76, "sigma-3-Orbits (v633 Q4)"),
               (19, "g-12-Orbits (v629 R2)"),
               (112, "D8-Anteil der Wurzeln (v629 R1)"),
               (128, "Spinor-Anteil der Wurzeln (v629 R1)")],
        excluded="Inputs: 240 Wurzeln, |mu4| = 4, sigma-Ordnung 3, 8 Koord.; "
                 "g-4-Orbit-Zahl 3 als Input-Echo der sigma-Ordnung; "
                 ">300: 1770, 11520, 46080; Formwerte |H|^2"),
    "B2": dict(
        label="v634 G31-Invarianten (Grade, Normalteiler, Zentralisatoren)",
        slots=[(8, "Grad d1 (v634 T2, Molien)"),
               (12, "Grad d2 (v634 T2)"),
               (20, "Grad d3 (v634 T2)"),
               (24, "Grad d4 (v634 T2)"),
               (32, "2^{1+4}-Ordnung (v634 T1.4)"),
               (64, "|Nsmall| = |N64| (v634 T1.4)"),
               (72, "|C(c)| des Compiler-Clocks (v634 T2)"),
               (192, "Wurzelstabilisator = 8-regulaerer Zentralisator "
                     "(v634 T1.6/T2)"),
               (288, "12-regulaerer Zentralisator (v634 T2)")],
        excluded="Inputs/Echos: 240 Wurzeln, 60 Linien (= B1-Fakt), "
                 "|Z(G31)| = 4 = <J> (Input-Echo); >300: 46080, 11520, "
                 "720 (Sp4(2)), 768 (Linienstabilisator); "
                 "W(D5)/S4-Kontrollgrade (Kontrollen, keine Scans)"),
    "B3": dict(
        label="v647 Grad-24/20-Runde (neue Zensus-Zahlen)",
        slots=[(5, "ord(u^4) (v647 S3)"),
               (10, "24-Zensus {24: 10} (v647 S1)"),
               (30, "8-Zensus {8: 30} (v634 T2 / v647)"),
               (48, "5-Zensus {5: 48} (v647 S3)")],
        excluded="bereits budgetiert (B2-Fakten): Grade 8/12/20/24 und "
                 "deren 240/d-Zensen {12: 20}, {20: 12}; |C(w)| = 24, "
                 "|C(u)| = 20, |C(u^4)| = 20 (Springer-Echos der Grade). "
                 "KAVEAT: 48 = 240/5 ist arithmetisch erzwungen, GEGEBEN "
                 "ord-5-frei -- (5, 48) traegt effektiv EINE freie "
                 "Koinzidenz, nicht zwei"),
    "B4": dict(
        label="v626 Code-Parameter des [8,4,4] (freie Anteile)",
        slots=[(14, "A_4 der Gewichtsverteilung (v626 E1)"),
               (16, "|C| Codewoerter (v626 E1)"),
               (128, "korrumpierte Woerter 16 x 8 (v626 E4)")],
        excluded="FORCED-IDENTISCH (keine freie Koinzidenz-Masse): "
                 "8 = n = rank(E8) (Konstruktion-A-Laenge), 4 = d = k "
                 "(erzwungen: der selbstduale doppelt-gerade [8,4]-Code "
                 "ist EINDEUTIG, seine Gewichtsverteilung 1+14x^4+x^8 "
                 "MacWilliams-erzwungen); 240/2160 Schalen (E8-Echo, "
                 ">300 bzw. Echo). ACHTUNG: auch 14 und 16 sind durch "
                 "die Code-Eindeutigkeit erzwungen -- FORCED-Flag in L5"),
    "B5": dict(
        label="v638/v646 CODESEM-Batterie (42 Eintraege, re-deriviert)",
        slots=[(v, "Batterie-Wert (v646 R2, re-deriviert)")
               for v in b5_vals],
        excluded="Dups/Echos: 240, 248 (= 240+8, Komposition), 60, 12, "
                 "8/4/16 (Code-Parameter), A_4 = 14 woertlich; 0/1-Trivia. "
                 "Der Z6-w4-Orbitwert 14 ist ein NEUER Fakt und bleibt. "
                 "3 Familien-Bits + 1 Anker: Input-Echo der sigma-Ordnung "
                 "(kein Slot)"),
    "B6": dict(
        label="v624 Lorentz-Kongruenz (C-Teil)",
        slots=[(6, "Index |det P| der Kongruenz (v624 C2)"),
               (36, "72/2 = 6^2 (v624 C2)"),
               (72, "det J_fix (v624 C2 / v600)"),
               (2, "det J_det Primfront-Form (v624 C1)"),
               (8, "det B komplex (v624 C3)")],
        excluded="Signatur-Trivia (1,2); A-Teil (d = 4 dreifach erzwungen) "
                 "ist DERIVATION [E, konditional], keine Koinzidenz; "
                 "B-Teil p_n-Zahlen -> Kill-Budget (v646 R2.4)"),
}

for bid in sorted(BUDGETS):
    b = BUDGETS[bid]
    vals = [s for s, _ in b["slots"]]
    hits = sorted(v for v in vals if v in T_SET)
    b["vals"], b["hits"] = vals, hits
    print("  %s %-58s n=%2d  Treffer %s"
          % (bid, b["label"], len(vals), hits))

ok_budget = True
for bid, b in BUDGETS.items():
    vs = b["vals"]
    ok_budget &= (len(set(vs)) == len(vs)
                  and all(2 <= v <= N_MAX for v in vs)
                  and all(src for _, src in b["slots"]))
check("Budgets konsistent: Slots distinct, in [2, 300], alle mit Quelle; "
      "Ziel-Liste: 19 Eintraege, distinct, alle mit Korpus-Quelle",
      ok_budget and len(set(TARGETS)) == 19
      and all(src for _, src in TARGETS_SRC) and len(T_EFF) == 18)

# ---- die Beobachtungen (a)-(h), auf Budgets gemappt ------------------
OBS = [
    dict(id="a", label="60 = D_start (freie Clock-Orbits)", budget="B1",
         target=60, pres_slot=60, forced=False),
    dict(id="b", label="12 sigma-fixe Wurzeln = 12 Marks", budget="B1",
         target=12, pres_slot=12, forced=False),
    dict(id="c", label="G31-Grade (8,12,20,24) = (Rang,Uhr,Kamm,|W(A3)|)",
         budget="B2", joint=True, pres_slots=[8, 12, 20, 24], forced=False),
    dict(id="d", label="48 = 240/5 = Omega_adm (u^4-Zensus)", budget="B3",
         target=48, pres_slot=48, forced=False,
         note="5 = g_car nur Zensus-Seite; 48 gegeben ord-5-frei erzwungen"),
    dict(id="e", label="14 = A_4 = 2 x 7 Parabolik", budget="B4",
         target=14, pres_slot=14, forced=True),
    dict(id="f", label="16 = |C| = Halbspinor/Seam-Sites", budget="B4",
         target=16, pres_slot=16, forced=True),
    dict(id="g", label="6 = Lorentz-Kongruenz-Index = p_2(a)", budget="B6",
         target=6, pres_slot=6, forced=False),
    dict(id="h", label="CODESEM-Batterie (Anker-Norm 6 u.a.)", budget="B5",
         joint=True, pres_slots=[6], forced=False),
]

# ======================================================================
# L2: Null-Modelle -- exakte Tails + MC
# ======================================================================
section("L2: Null-Modelle U/D/M -- Budget-Tabelle pro Beobachtung")

Q_U = Fr(len(T_EFF), N_MAX - 1)          # uniform [2, 300]
Q_D = Fr(D_TGT, D_SUM)                    # teilergewichtet


def q_slot(s, model, targets=None):
    """P(zufaelliger Slot der Groesse s trifft die Ziel-Liste)."""
    tset = T_SET if targets is None else targets
    if model == "U":
        return Fr(sum(1 for t in tset if 2 <= t <= N_MAX), N_MAX - 1)
    if model == "D":
        return Fr(sum(DIV[t] for t in tset if 2 <= t <= N_MAX), D_SUM)
    lo, hi = window(s)
    k = sum(1 for t in tset if lo <= t <= hi)
    return Fr(k, hi - lo + 1)


def q_slot_target(s, t, model):
    """P(zufaelliger Slot der Groesse s trifft GENAU das Ziel t)."""
    if model == "U":
        return Fr(1, N_MAX - 1)
    if model == "D":
        return Fr(DIV[t], D_SUM)
    lo, hi = window(s)
    return Fr(1, hi - lo + 1) if lo <= t <= hi else Fr(0)


def poisson_binomial_tail(qs, k, exact=True):
    """P(sum Bernoulli(q_i) >= k); Fraction-DP (exact) oder float."""
    if exact:
        dist = [Fr(1)]
        for q in qs:
            new = [dist[0] * (1 - q)]
            for j in range(1, len(dist)):
                new.append(dist[j] * (1 - q) + dist[j - 1] * q)
            new.append(dist[-1] * q)
            dist = new
        return sum(dist[k:], Fr(0))
    dist = [1.0]
    for q in qs:
        fq = float(q)
        new = [dist[0] * (1 - fq)]
        for j in range(1, len(dist)):
            new.append(dist[j] * (1 - fq) + dist[j - 1] * fq)
        new.append(dist[-1] * fq)
        dist = new
    return sum(dist[k:])


def union_p(qs):
    """P(mindestens ein Treffer) = 1 - prod(1 - q_i), exakt."""
    prod = Fr(1)
    for q in qs:
        prod *= (1 - q)
    return 1 - prod


def mc_tail(qs, k, trials, rng):
    fqs = [float(q) for q in qs]
    hit = 0
    for _ in range(trials):
        c = 0
        for fq in fqs:
            if rng.random() < fq:
                c += 1
        if c >= k:
            hit += 1
    return hit / trials


rng = random.Random(SEED)
rows = []
mc_ok = True
print("  Beobachtung                                            Budget  "
      "n   k   roh-p     p_U       p_D       p_M       p_max")
for o in OBS:
    b = BUDGETS[o["budget"]]
    vals = b["vals"]
    n = len(vals)
    if o.get("joint"):
        k_obs = len(b["hits"])
        raw = Fr(1)
        for s in o["pres_slots"]:
            raw *= q_slot_target(s, s, "M")
        ps = {}
        for m in ("U", "D", "M"):
            qs = [q_slot(s, m) for s in vals]
            ps[m] = poisson_binomial_tail(qs, k_obs)
        qs_M = [q_slot(s, "M") for s in vals]
        p_mc = mc_tail(qs_M, k_obs, MC_TRIALS, rng)
        p_ex = float(ps["M"])
    else:
        t = o["target"]
        k_obs = 1
        raw = q_slot_target(o["pres_slot"], t, "M")
        ps = {}
        for m in ("U", "D", "M"):
            qs = [q_slot_target(s, t, m) for s in vals]
            ps[m] = union_p(qs)
        qs_M = [q_slot_target(s, t, "M") for s in vals]
        p_mc = mc_tail(qs_M, 1, MC_TRIALS, rng)
        p_ex = float(ps["M"])
    tol = 5.0 * max((p_ex * (1 - p_ex) / MC_TRIALS) ** 0.5, 1e-5)
    mc_ok &= abs(p_mc - p_ex) <= tol
    p_max = max(ps.values())
    o.update(n=n, k=k_obs, raw=raw, ps=ps, p_max=p_max, p_mc=p_mc)
    rows.append(o)
    print("  (%s) %-50s %s  %3d %3d  %.2e  %.2e  %.2e  %.2e  %.2e%s"
          % (o["id"], o["label"][:50], o["budget"], n, k_obs, float(raw),
             float(ps["U"]), float(ps["D"]), float(ps["M"]), float(p_max),
             "  [FORCED]" if o["forced"] else ""))

check("L2: exakte Poisson-Binomial/Union-Tails und 100k-MC stimmen fuer "
      "alle 8 Beobachtungen ueberein (Modell M, 5-sigma-Toleranz)", mc_ok)
check("L2: Plumbing -- alle Beobachtungen haben p unter allen 3 Modellen, "
      "0 < p_max <= 1",
      all(0 < float(o["p_max"]) <= 1 and len(o["ps"]) == 3 for o in rows))

# ======================================================================
# L3: Familien-Korrektur -- das globale Look-Elsewhere-p
# ======================================================================
section("L3: Familien-Korrektur (alle Slots + Kills als Trials)")

ALL_SLOTS = [s for bid in sorted(BUDGETS) for s in BUDGETS[bid]["vals"]]
K_GLOBAL = sum(len(BUDGETS[bid]["hits"]) for bid in BUDGETS)
N_GLOBAL = len(ALL_SLOTS)
print("  Gesamt-Budget: N = %d Slots, K = %d Treffer (%s)"
      % (N_GLOBAL, K_GLOBAL,
         {bid: BUDGETS[bid]["hits"] for bid in sorted(BUDGETS)}))

glob = {}
for m in ("U", "D", "M"):
    qs = [q_slot(s, m) for s in ALL_SLOTS]
    glob[m] = poisson_binomial_tail(qs, K_GLOBAL)
qs_M_glob = [q_slot(s, "M") for s in ALL_SLOTS]
mc_glob = {}
for m in ("U", "D", "M"):
    qs = [q_slot(s, m) for s in ALL_SLOTS]
    mc_glob[m] = mc_tail(qs, K_GLOBAL, MC_TRIALS, rng)
print("  global exakt:  p_U = %.3e   p_D = %.3e   p_M = %.3e"
      % (float(glob["U"]), float(glob["D"]), float(glob["M"])))
print("  global MC:     p_U = %.3e   p_D = %.3e   p_M = %.3e  (100k, Seed %d)"
      % (mc_glob["U"], mc_glob["D"], mc_glob["M"], SEED))
ok_g = True
for m in ("U", "D", "M"):
    p_ex = float(glob[m])
    tol = 5.0 * max((p_ex * (1 - p_ex) / MC_TRIALS) ** 0.5, 1e-5)
    ok_g &= abs(mc_glob[m] - p_ex) <= tol
check("L3: globale exakte Tails und 100k-MC stimmen ueberein (U/D/M)", ok_g)

# ---- Kills als Trials -----------------------------------------------
# (1) v646 R2.4: 11 natuerliche Code-Familien gegen die p-Sequenz
#     (4, 6, 10, 18) -- 0 Treffer.  q pro Familie unter M: exakte
#     4er-Sequenz, Produkt der Fenster-Wahrscheinlichkeiten.
P_SEQ = (4, 6, 10, 18)
q_fam = Fr(1)
for s in P_SEQ:
    q_fam *= Fr(1, win_size(s))
KILL_TRIALS = [("v646 R2.4: 11 Familien vs p-Sequenz (0 Treffer)",
                [q_fam] * 11, 0)]
# (2) Lesarten-Ebene (dokumentierte Struktur-Lesarten, je 1 Trial):
READINGS_KILLED = [
    "48 x 5-Inzidenz fuer das kanonische Ordnung-12-Element (v629 R2)",
    "60 -> 6 Kaskaden-Quotient auf den 60 Linien (v633 Q8, 4 Kandidaten)",
    "G31 = W(D5) x W(A3) Untergruppen-Lesart von 46080 (v634 T1)",
    "Compiler-Clock c = w^2 einer 24-Uhr (v647 S2, Paritaets-Theorem)",
    "p_n = 2 + 2^n als Code-Operation (v646 R2.4, 0/11)",
    "naive Placement-Semantik (v638 S4, 28/30 tragen die Symmetrien nicht)",
]
READINGS_CONFIRMED = [
    "E8 = Konstruktion A des [8,4,4] (v626, Theorem)",
    "60 Clock-Orbits = hermitesch-unimodulares Z[i]-E8 (v633 Q1-Q3)",
    "G31 = voller unitaerer Stabilisator, sigma = c^4, J = c^9 (v634)",
    "C* = RM(1,3) auf AG(3,2), Decode = Projektion (v638)",
    "Anker-Selektion: sigma fixiert genau den Anker-Sektor (v646 R1b)",
    "w^6 = +-J / u^5 = +-J: mu4-Zentrum als Uhr-Potenz (v647 S1/S3)",
]
kill_qs = []
for name, qs, hits in KILL_TRIALS:
    kill_qs += qs
    print("  Kill-Trial: %s  (q je %.1e)" % (name, float(qs[0])))
print("  Lesarten-Budget: %d bestaetigt, %d getoetet (Kills = "
      "Disziplin-Erfolge, im Budget):" % (len(READINGS_CONFIRMED),
                                          len(READINGS_KILLED)))
for r in READINGS_KILLED:
    print("    KILL      %s" % r)
for r in READINGS_CONFIRMED:
    print("    CONFIRMED %s" % r)

glob_kill = {}
for m in ("U", "D", "M"):
    qs = [q_slot(s, m) for s in ALL_SLOTS] + kill_qs
    glob_kill[m] = poisson_binomial_tail(qs, K_GLOBAL)
print("  global inkl. Kill-Trials: p_U = %.3e  p_D = %.3e  p_M = %.3e"
      % tuple(float(glob_kill[m]) for m in ("U", "D", "M")))
check("L3: Kill-Trials vergroessern das korrigierte p (konservative "
      "Richtung) in allen Modellen",
      all(glob_kill[m] >= glob[m] for m in ("U", "D", "M")))
P_GLOBAL_MAX = max(glob_kill.values())
print("  GLOBALES KORRIGIERTES p (konservativstes Modell, inkl. Kills): "
      "%.3e" % float(P_GLOBAL_MAX))

# ======================================================================
# L4: Kontrollen
# ======================================================================
section("L4: Kontrollen -- Pseudo-Theorien + Kalibrierung")

# (A) 2000 zufaellige Pseudo-Ziel-Listen gleicher Groesse/Verteilung:
#     T' ~ pro echtem Ziel t ein t' uniform aus W(t), distinct.
rngA = random.Random(SEED + 1)
pseudo_p = []
pseudo_K = []
for _ in range(R_CONTROL):
    tp = set()
    for t in T_EFF:
        lo, hi = window(t)
        v = rngA.randint(lo, hi)
        tries = 0
        while v in tp and tries < 50:
            v = rngA.randint(lo, hi)
            tries += 1
        tp.add(v)
    Kp = sum(1 for s in ALL_SLOTS if s in tp)
    qs = [q_slot(s, "M", targets=tp) for s in ALL_SLOTS]
    pp = poisson_binomial_tail(qs, Kp, exact=False) if Kp > 0 else 1.0
    pseudo_K.append(Kp)
    pseudo_p.append(pp)
pseudo_p.sort()
med_p = pseudo_p[R_CONTROL // 2]
fr_sig = sum(1 for p in pseudo_p if p < P_SIG) / R_CONTROL
fr_sug = sum(1 for p in pseudo_p if p < P_SUG) / R_CONTROL
K_real = K_GLOBAL
p_real_M = float(glob["M"])
fr_K_ge = sum(1 for Kp in pseudo_K if Kp >= K_real) / R_CONTROL
fr_p_le = sum(1 for p in pseudo_p if p <= p_real_M) / R_CONTROL
print("  Pseudo-Theorien (R = %d, groessengematcht): K' Median = %d, "
      "max = %d; echtes K = %d" % (R_CONTROL,
                                   sorted(pseudo_K)[R_CONTROL // 2],
                                   max(pseudo_K), K_real))
print("  Pseudo-p (Modell M): Median = %.3f, Anteil p' < 0.01: %.4f, "
      "p' < 0.1: %.4f" % (med_p, fr_sig, fr_sug))
print("  EMPIRISCHE FAMILIEN-KORREKTUR ueber die Theorie-Wahl: "
      "Anteil Pseudo-Theorien mit K' >= K_echt: %.4f; "
      "mit p' <= p_echt(M): %.4f" % (fr_K_ge, fr_p_le))
check("L4-A: Pseudo-Theorie-Kontrolle unauffaellig -- Median p' > 0.1 "
      "und Anteil p' < 0.01 unter 5 Prozent",
      med_p > 0.1 and fr_sig < 0.05,
      "Median %.3f, Anteil<0.01 %.4f" % (med_p, fr_sig))

# (B) Kalibrierung: 2000 synthetische Slot-Ziehungen unter M gegen die
#     ECHTE Ziel-Liste; p' muss konservativ-uniform sein.
rngB = random.Random(SEED + 2)
cal_p = []
for _ in range(R_CONTROL):
    Kp = 0
    for s in ALL_SLOTS:
        lo, hi = window(s)
        if rngB.randint(lo, hi) in T_SET:
            Kp += 1
    pp = poisson_binomial_tail(qs_M_glob, Kp, exact=False) if Kp > 0 else 1.0
    cal_p.append(pp)
fr01 = sum(1 for p in cal_p if p <= 0.01) / R_CONTROL
fr10 = sum(1 for p in cal_p if p <= 0.10) / R_CONTROL
print("  Kalibrierung (R = %d): Anteil p' <= 0.01: %.4f (soll <= ~0.01), "
      "p' <= 0.1: %.4f (soll <= ~0.1)" % (R_CONTROL, fr01, fr10))
check("L4-B: Null-Modell-Selbsttest kalibriert/konservativ "
      "(p'<=0.01 in <=2 Prozent, p'<=0.1 in <=12.5 Prozent der Faelle)",
      fr01 <= 0.02 and fr10 <= 0.125)

# ======================================================================
# L5: Dreiteilung + Fazit + Ledger-Notiz
# ======================================================================
section("L5: Dreiteilung (nach p_max, konservativstes Modell)")


def typ(o):
    p = float(o["p_max"])
    if o["forced"]:
        return "FORCED"
    if p < P_SIG:
        return "SIGNIFIKANT"
    if p < P_SUG:
        return "SUGGESTIV"
    return "UNAUFFAELLIG"


cats = {"SIGNIFIKANT": [], "SUGGESTIV": [], "UNAUFFAELLIG": [], "FORCED": []}
for o in rows:
    cats[typ(o)].append(o)
for c in ("SIGNIFIKANT", "SUGGESTIV", "UNAUFFAELLIG", "FORCED"):
    print("  %s:" % c)
    if not cats[c]:
        print("    (keine)")
    for o in cats[c]:
        print("    (%s) %-52s p_max = %.3f  (roh %.1e, Budget n = %d)"
              % (o["id"], o["label"], float(o["p_max"]), float(o["raw"]),
                 o["n"]))
check("L5: Dreiteilung vollstaendig -- jede Beobachtung genau einmal "
      "typisiert", sum(len(v) for v in cats.values()) == len(rows))

n_pass = sum(1 for _, ok in CHECKS if ok)
n_tot = len(CHECKS)
if n_pass == n_tot:
    VERDICT = "LOOKELSEWHERE-QUANTIFIED"
elif n_pass >= 0.8 * n_tot:
    VERDICT = "MIXED"
else:
    VERDICT = "MACHINERY-FAILS"

section("FAZIT + fertiger Diary-/Ledger-Notiz-Text")
sig_ids = ", ".join("(%s) %s" % (o["id"], o["label"])
                    for o in cats["SIGNIFIKANT"]) or "keine"
sug_ids = ", ".join("(%s) %s" % (o["id"], o["label"])
                    for o in cats["SUGGESTIV"]) or "keine"
una_ids = ", ".join("(%s) %s" % (o["id"], o["label"])
                    for o in cats["UNAUFFAELLIG"]) or "keine"
for_ids = ", ".join("(%s) %s" % (o["id"], o["label"])
                    for o in cats["FORCED"]) or "keine"

NOTE = """
LOOKELSEWHERE.01 (Sandbox-Probe look_elsewhere_probe.py, Seed %d,
100k MC, exakte Poisson-Binomial-Tails).  Das Bingo-Budget der
getypten [C]-Koinzidenzen der E8.CODE/CODESEM/INCIDENCE/ST31/EXTREV-
Runden, quantifiziert gegen die VOR der Rechnung eingefrorene
Compiler-Ziel-Liste {1,2,3,4,5,6,7,8,12,14,16,20,24,27,48,60,81,240,248}
unter drei Null-Modellen (uniform / teilergewichtet / groessengefenstert;
Typisierung nach dem KONSERVATIVSTEN Modell).  Budget: N = %d Struktur-
Slots, K = %d Treffer; getoetete Lesarten (%d, inkl. 46080-Untergruppe,
p_n-Bytecode, c = w^2) gehen als 0-Treffer-Trials ins Budget ein.
GLOBAL: korrigiertes Familien-p = %.2e (uniform %.1e, teilergewichtet
%.1e, groessengefenstert %.2e) -- das Ensemble ueberlebt die ehrliche
Korrektur im konservativsten Modell als %s.  Empirische Kontrolle:
von %d groessengematchten Pseudo-Ziel-Listen erreichen %.1f%% die echte
Trefferzahl und %.1f%% das echte p.  DREITEILUNG (p_max):
SIGNIFIKANT (p < 0.01): %s.
SUGGESTIV (0.01..0.1): %s.
UNAUFFAELLIG (p > 0.1, als Beobachtung OHNE statistisches Gewicht zu
fuehren): %s.
FORCED (mathematisch erzwungen, tragen per Konstruktion KEINE freie
Koinzidenz-Masse; ihr Wert ist das Theorem, nicht die Zahl): %s.
Ehrliche Einordnung: KEINE Einzel-Beobachtung ueberlebt fuer sich als
signifikant, sobald das Budget der verfuegbaren Struktur-Zahlen und die
Groessenverteilung der Ziele ehrlich gezaehlt werden; die Substanz der
Runden liegt in den [E]-Strukturtheoremen (RM(1,3)-Woerterbuch,
Z[i]-E8, G31-Identifikation), nicht in den Zahlen-Bingos.  Kills
bestaetigen die Disziplin (6 von 12 Lesarten getoetet).  Verdikt: %s.
""" % (SEED, N_GLOBAL, K_GLOBAL, len(READINGS_KILLED),
       float(P_GLOBAL_MAX), float(glob_kill["U"]), float(glob_kill["D"]),
       float(glob_kill["M"]),
       ("SIGNIFIKANT" if float(P_GLOBAL_MAX) < P_SIG else
        "SUGGESTIV" if float(P_GLOBAL_MAX) < P_SUG else "UNAUFFAELLIG"),
       R_CONTROL, 100.0 * fr_K_ge, 100.0 * fr_p_le,
       sig_ids, sug_ids, una_ids, for_ids, VERDICT)
print(NOTE)

print("=" * 78)
print("VERDIKT: %s  (%d/%d Checks PASS, %.1f s)"
      % (VERDICT, n_pass, n_tot, time.time() - T0))
print("=" * 78)
raise SystemExit(0 if n_pass == n_tot else 1)
