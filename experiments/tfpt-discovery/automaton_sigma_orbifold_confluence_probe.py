#!/usr/bin/env python3
"""automaton_sigma_orbifold_confluence_probe.py -- AUTOMATON.ORBIFOLD.01
(Explorations-Probe, Abschluss-Sonde zu AUTOMATON.MULTIWAY.01):
Bleibt die Diamant-Eigenschaft (Konfluenz / Causal Invariance) im
sigma-QUOTIENTEN des Z[i]^4-Hecke-Multiway-Turms erhalten -- insbesondere
(a) an der ramifizierten Stelle (die einzige Kommutativitaets-Ausnahme des
Korpus: [D,A] != 0 auf der Nullklasse, hecke_mod_ramified_probe) und
(b) an den inerten Halborbits (40 sigma-fixe + 390 freie Paare auf der
(3)-Schicht, AUTOMATON.MULTIWAY.01 S4.3)?

DAS ORBIFOLD-SYSTEM (O1) -- zwei Buchfuehrungen, sauber getrennt:

  (Z) ORBIT-ZAEHLUNG (kanonische Groupoid-Faltung): Zustaende = sigma-Orbits
      [M] = {M, sigma M}; Regelklassen = sigma-Orbits von Primidealen
      (ramifiziert {(1+i)}, inert {(3)}, split-Paar {(2+i),(1+2i)} -- die
      Regel "mal (2-i)" ist assoziiert zu (1+2i), das sigma-getauschte
      Paar wird also zu EINER Regelklasse verklebt); Uebergangs-
      Multiplizitaet [M] -> [M'] = Anzahl der Uebergaenge vom REPRAESEN-
      TANTEN M in den Ziel-Orbit [M'] (wohldefiniert, weil sigma jede
      Regelklasse als Ganzes erhaelt -- die Wohldefiniertheit wird an
      freien Zustaenden explizit MITGEMESSEN, nicht angenommen).
  (W) HALBORBIT-GEWICHTUNG (Isotropie-Masse, das v714-Descent-Motiv
      "mu2-Isotropie => halbe Masse", hier als Zustands-Gewicht auf den
      ZWISCHEN-Zustaenden der Diamanten): jede Kette traegt das Gewicht
      w(x) des durchlaufenen Zwischenzustands, w = 1/2 falls sigma x = x,
      sonst 1 (gerechnet in Halb-Einheiten, exakt ganzzahlig).
      EHRLICHKEITS-FENCE: (W) ist eine KONSTRUKTIONSWAHL dieser Probe --
      v714s Halborbit-Konvention betrifft die LAENGEN geschlossener
      Orbits im Kamm, nicht Multiway-Zustandsmassen; ein Bruch von (W)
      ist also eine Aussage ueber DIESE Quotienten-Buchfuehrung, kein
      Widerspruch zu v714.

PREREGISTRIERTE ERWARTUNG (vor der Messung, radikale Ehrlichkeit):
  *  (Z) sollte UEBERALL exakt halten -- der Vererbungs-Grund: sigma ist
     ein Multiway-Automorphismus, die Faltung kommutiert mit den (oben
     exakt kommutierenden) Hecke-Schritten.  Ein Bruch wuerde den
     Vererbungs-Beweis oder die Implementierung falsifizieren.
  *  (W) sollte exakt dort brechen, wo eine Diamant-Seite durch sigma-FIXE
     Zwischenzustaende laeuft und die andere durch FREIE: die ramifizierte
     Schicht ist die einzige KOMPLETT sigma-fixe Schicht (15/15) =>
     maximaler Bruch (Faktor 2 auf jedem Endpunkt) fuer ram x split;
     partieller Bruch fuer ram x inert (nur Endpunkte mit freiem inerten
     Zwischenzustand).

GEMESSENE FAELLE (alle exakt, Ganzzahl-Arithmetik):
  O1.a  ram x split5   [(1+i) x {(2+i),(1+2i)}]  -- beide Ordnungen (Z)+(W)
  O1.b  ram x inert3   [(1+i) x (3)]             -- beide Ordnungen (Z)+(W)
  O1.c  ram x ram      [(1+i)^2]  -- Quotienten-Branchial-Spektrum
  O1.d  inert3 x inert3 [(3)^2]   -- Quotienten-Branchial-Spektrum (gross)
  O1.e  split5 x split5 [inkl. (2+i)x(2-i)-Kreuzterm: der Quotient
        VERKLEBT die beiden Schichten]           -- Glue-Zensus
  O1.f  Wohldefiniertheit: Quotienten-Zaehler vom Repraesentanten M ==
        vom Repraesentanten sigma M (freie Test-Zustaende)

O2: Anatomie der (W)-Ausnahme (exakte Orbit-Klassen + Multiplizitaeten);
    Abgleich mit der [D,A]-Ausnahme (Ort vs Objekt, ehrlich); falls (Z)
    ueberall haelt: der kleine Satz-Kandidat wird formuliert.
O3: Final-Adjudikation der gesamten Zuse/Wolfram-Frage.

FIREWALL: experiments/-Probe; EINE neue Datei; schreibt nichts; kein
verification/-, Paper-, Ledger-, Changelog- oder Website-Surface beruehrt.
Keine Primzahltabelle / kein zeta (AST-geprueft); die Gauss/HNF-Maschinerie
wird aus automaton_multiway_tower_probe.py importiert (24/24 PASS,
Selbsttests dort: HNF-Unimodular-Invarianz 200/200, ring-interner
Prime-Scan).

Run: experiments/tfpt-discovery/.venv/bin/python \\
     experiments/tfpt-discovery/automaton_sigma_orbifold_confluence_probe.py
"""

import ast
import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import automaton_multiway_tower_probe as base  # noqa: E402

FAILURES = []
CHECKS = [0]


def check(name, ok, detail=""):
    CHECKS[0] += 1
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILURES.append(name)
    print("[%s] %s%s" % (tag, name, (" -- " + detail) if detail else ""))


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


# ---------------------------------------------------------------- Schluessel
def key(H):
    """Kompakter Byte-Schluessel eines HNF-Zustands (exakt, kollisionfrei
    fuer die hier auftretenden kleinen Eintraege; Bereichs-Assert)."""
    out = bytearray()
    for r in H:
        for z in r:
            a, b = z
            assert -120 <= a <= 120 and -120 <= b <= 120, (a, b)
            out.append(a + 128)
            out.append(b + 128)
    return bytes(out)


def okey_fixed(H):
    """(Orbit-Schluessel, sigma-fix?) eines Zustands."""
    k = key(H)
    ks = key(base.sigma_module(H))
    return (k if k <= ks else ks), (k == ks)


def compose_orbifold(P, Q, weighted=True, start=None):
    """Alle Ketten start ->(pi in P) x ->(pi' in Q) y, gefaltet auf
    sigma-Orbits.  Rueckgabe: (Zaehl-Counter, Gewichts-Counter in
    HALB-Einheiten [fix=1, frei=2], fixflag-Dict der Endpunkt-Orbits)."""
    if start is None:
        start = base.ID_BASIS
    plain = Counter()
    wtd = Counter()
    fixflag = {}
    for (p1, r1) in P:
        for x in base.down_layer(start, p1, r1):
            if weighted:
                _, fx = okey_fixed(x)
                wx = 1 if fx else 2
            for (p2, r2) in Q:
                for y in base.down_layer(x, p2, r2):
                    ok, fy = okey_fixed(y)
                    plain[ok] += 1
                    if weighted:
                        wtd[ok] += wx
                    fixflag[ok] = fy
    return plain, wtd, fixflag


def one_layer_orbits(P, start=None):
    """Eine Regelklasse ab start, gefaltet: Counter + fixflag."""
    if start is None:
        start = base.ID_BASIS
    plain = Counter()
    fixflag = {}
    for (p1, r1) in P:
        for x in base.down_layer(start, p1, r1):
            ok, fx = okey_fixed(x)
            plain[ok] += 1
            fixflag[ok] = fx
    return plain, fixflag


def spectrum(plain):
    return dict(sorted(Counter(plain.values()).items()))


def run():
    t0 = time.time()
    print("=" * 78)
    print("AUTOMATON.ORBIFOLD.01 -- Konfluenz des sigma-Quotienten des "
          "Hecke-Multiway-Turms")
    print("=" * 78)

    # ---------------- G0 -----------------------------------------------------
    print("\n--- G0: Firewall + Basis-Maschinerie " + "-" * 40)
    hits = g0_ast_firewall()
    check("G0.1 AST-Firewall (keine Primtabelle/zeta/sympy)", not hits,
          "verbotene Namen: %s" % (sorted(hits) if hits else "keine"))

    primes = base.gaussian_primes(base.X_NORM)
    by_norm = {}
    for p in primes:
        by_norm.setdefault(base.gnorm(p), []).append(p)
    pi2 = by_norm[2][0]
    pi5a, pi5b = by_norm[5]
    pi9 = by_norm[9][0]
    RAM = [(pi2, base.residues_mod(pi2))]
    SPLIT5 = [(pi5a, base.residues_mod(pi5a)),
              (pi5b, base.residues_mod(pi5b))]
    INERT3 = [(pi9, base.residues_mod(pi9))]
    # die "(2-i)-Regel" ist das sigma-Bild der "(2+i)-Regel": conj(2+i) =
    # 2-i ist assoziiert zum ANDEREN Primideal (1+2i) -- das sigma-Paar
    # bildet also EINE Regelklasse (Kontrolle der Verklebung):
    def conj_canon(z):
        w = base.gconj(z)
        return base.gmul(base.gcanon_unit(w), w)

    check("G0.2 conj(pi) assoziiert zum Partner-Ideal: das sigma-Paar ist "
          "EINE Regelklasse",
          conj_canon(pi5a) == pi5b and conj_canon(pi5b) == pi5a,
          "conj(%s) ~ %s und conj(%s) ~ %s (kanonische Assoziierte)"
          % (pi5a, conj_canon(pi5a), pi5b, conj_canon(pi5b)))

    lay2, fix2 = one_layer_orbits(RAM)
    lay5, fix5 = one_layer_orbits(SPLIT5)
    lay9, fix9 = one_layer_orbits(INERT3)
    n_fix9 = sum(1 for v in fix9.values() if v)
    check("G0.3 Schicht-Orbits: ram 15 (alle fix), split5 verklebt "
          "312 -> 156, inert3 820 -> 40 fix + 390 Paare",
          len(lay2) == 15 and all(fix2.values())
          and len(lay5) == 156 and not any(fix5.values())
          and all(v == 2 for v in lay5.values())
          and len(lay9) == 430 and n_fix9 == 40,
          "ram %d Orbits (fix: %s); split5 %d Orbits (alle Zaehlung 2, "
          "frei); inert3 %d Orbits (%d fix + %d Paare)"
          % (len(lay2), all(fix2.values()), len(lay5), len(lay9), n_fix9,
             len(lay9) - n_fix9))

    # ---------------- O1.a: ram x split5 (beide Ordnungen) -------------------
    print("\n--- O1.a: ram x split5 -- die ramifizierte Stelle gegen das "
          "verklebte Paar " + "-" * 4)
    p_rs, w_rs, ff_rs = compose_orbifold(RAM, SPLIT5)
    p_sr, w_sr, ff_sr = compose_orbifold(SPLIT5, RAM)
    check("O1.a1 (Z) Diamant im Quotienten: ram-dann-split == "
          "split-dann-ram", p_rs == p_sr,
          "Orbit-Endpunkte %d == %d; Spektrum %s (alle Endpunkte frei: %s; "
          "Gesamtmasse %d == %d Ketten)"
          % (len(p_rs), len(p_sr), spectrum(p_rs),
             not any(ff_rs.values()), sum(p_rs.values()), 15 * 312))
    ratios = Counter()
    for ok in p_rs:
        ratios[(w_sr[ok], w_rs[ok])] += 1
    only2 = set(ratios) == {(4, 2)}
    check("O1.a2 (W) Halborbit-Gewichtung BRICHT: Faktor exakt 2 auf "
          "JEDEM Endpunkt", (w_rs != w_sr) and only2,
          "alle %d Orbit-Endpunkte: Gewicht split-zuerst 4 vs ram-zuerst 2 "
          "(Halb-Einheiten) -- die ram-Seite laeuft durch die einzige "
          "komplett sigma-fixe Schicht (15/15), die split-Seite durch "
          "lauter freie Zwischenzustaende" % len(p_rs))

    # ---------------- O1.b: ram x inert3 (beide Ordnungen) -------------------
    print("\n--- O1.b: ram x inert3 -- die ramifizierte Stelle gegen die "
          "Halborbits " + "-" * 8)
    p_ri, w_ri, ff_ri = compose_orbifold(RAM, INERT3)
    p_ir, w_ir, ff_ir = compose_orbifold(INERT3, RAM)
    check("O1.b1 (Z) Diamant im Quotienten: ram-dann-inert == "
          "inert-dann-ram", p_ri == p_ir,
          "Orbit-Endpunkte %d == %d; Spektrum %s; Gesamtmasse %d == %d"
          % (len(p_ri), len(p_ir), spectrum(p_ri), sum(p_ri.values()),
             15 * 820))
    n_eq = sum(1 for ok in p_ri if w_ri[ok] == w_ir[ok])
    n_dbl = sum(1 for ok in p_ri if w_ir[ok] == 2 * w_ri[ok])
    n_fix_end = sum(1 for v in ff_ri.values() if v)
    fix_ok = all(w_ri[ok] == w_ir[ok] for ok, v in ff_ri.items() if v)
    check("O1.b2 (W) partieller Bruch: exakt die Endpunkte mit FREIEM "
          "inerten Zwischenzustand", n_eq + n_dbl == len(p_ri)
          and (w_ri != w_ir) and fix_ok,
          "%d Orbit-Endpunkte gleichgewichtet, %d mit Faktor 2 (keine "
          "anderen Diskrepanzen); alle %d sigma-fixen Endpunkte "
          "ungebrochen: %s" % (n_eq, n_dbl, n_fix_end, fix_ok))

    # ---------------- O1.c: ram^2 -- Quotienten-Branchial an (1+i) -----------
    print("\n--- O1.c: (1+i)^2 -- ramifiziert-quadratisch (Grassmann-"
          "Branchials) " + "-" * 9)
    p_rr, _, ff_rr = compose_orbifold(RAM, RAM, weighted=False)
    spec_rr = spectrum(p_rr)
    n_fix4 = sum(1 for v in ff_rr.values() if v)
    mass_cyc = sum(c for c in p_rr.values() if c in (1, 2))
    mass_11 = sum(c for c in p_rr.values() if c in (3, 6))
    ok_rr = (sum(p_rr.values()) == 225 and set(spec_rr) <= {1, 2, 3, 6}
             and mass_cyc == 120 and mass_11 == 105)
    check("O1.c1 (Z) Quotienten-Spektrum konsistent mit Upstairs "
          "{1:120, 3:35}", ok_rr,
          "Spektrum %s; zyklische Masse %d == 120, (1,1)-Masse %d == "
          "3*35; %d von %d Endpunkt-Orbits sigma-fix"
          % (spec_rr, mass_cyc, mass_11, n_fix4, len(p_rr)))

    # ---------------- O1.d: (3)^2 -- inert-quadratisch (gross) ---------------
    print("\n--- O1.d: (3)^2 -- die inerten Halborbits im Quadrat " + "-" * 23)
    t1 = time.time()
    p_ii, _, ff_ii = compose_orbifold(INERT3, INERT3, weighted=False)
    q = 9
    t11 = base.gauss_binom_42(q)
    h2 = (q ** 6 + q ** 5 + 2 * q ** 4 + 2 * q ** 3 + 2 * q ** 2 + q + 1)
    mass_cyc = sum(c for c in p_ii.values() if c in (1, 2))
    mass_11 = sum(c for c in p_ii.values() if c in (10, 20))
    n_fix81 = sum(1 for v in ff_ii.values() if v)
    ok_ii = (sum(p_ii.values()) == 820 * 820
             and set(spectrum(p_ii)) <= {1, 2, 10, 20}
             and mass_cyc == h2 - t11 and mass_11 == 10 * t11)
    check("O1.d1 (Z) Quotienten-Spektrum == gefaltetes Upstairs "
          "{1: h2-[4,2]_9, 10: [4,2]_9}", ok_ii,
          "Spektrum %s; zyklische Masse %d == %d, (1,1)-Masse %d == "
          "10*%d; Orbits %d (%d sigma-fix); %.1f s"
          % (spectrum(p_ii), mass_cyc, h2 - t11, mass_11, t11,
             len(p_ii), n_fix81, time.time() - t1))

    # ---------------- O1.e: split5^2 -- der verklebte Kreuzterm --------------
    print("\n--- O1.e: split5^2 -- (2+i)x(2-i): der Quotient verklebt die "
          "Schichten " + "-" * 6)
    p_ss, _, ff_ss = compose_orbifold(SPLIT5, SPLIT5, weighted=False)
    spec_ss = spectrum(p_ss)
    t11_5 = base.gauss_binom_42(5)
    # erwartete Faltung: p^2/pbar^2-Orbits (frei, verklebt) -> Werte
    # {2: 19500, 12: 806}; p*pbar-Endpunkte (Kreuzterm, upstairs Mult 2,
    # A1-Diamant) -> {2: fix} + {4: freie Paare}
    n2 = spec_ss.get(2, 0)
    n4 = spec_ss.get(4, 0)
    n12 = spec_ss.get(12, 0)
    n_fix25 = sum(1 for v in ff_ss.values() if v)
    mass = sum(p_ss.values())
    # Kreuzterm-Zerlegung: 24336 Kreuz-Ketten * 2 Ordnungen tragen Masse
    # 48672; fixe Kreuz-Endpunkte haben Wert 2 (== zyklische pp-Orbits!),
    # freie Paare Wert 4:
    cross_mass = 2 * 24336
    pp_mass = 2 * (19500 + 6 * 806)
    ok_ss = (mass == 312 * 312 == cross_mass + pp_mass
             and set(spec_ss) <= {2, 4, 12}
             and n12 == 806
             and 2 * n2 + 4 * n4 == cross_mass + 2 * 19500)
    check("O1.e1 (Z) Glue-Zensus: Verklebung exakt buchhaltbar", ok_ss,
          "Spektrum %s; Gesamtmasse %d == 97344; [4,2]_5-Orbits (Wert 12): "
          "%d == 806; sigma-fixe Endpunkt-Orbits: %d (alle im "
          "Kreuzterm p*pbar); Wert-2-Orbits %d = verklebte zyklische "
          "p^2-Paare (19500) + fixe Kreuz-Endpunkte (%d)"
          % (spec_ss, mass, n12, n_fix25, n2, n_fix25))
    # der A1-Diamant des sigma-getauschten Paares, im Quotienten gelesen:
    # jeder Kreuz-Endpunkt traegt upstairs Mult 1 aus p-dann-pbar UND 1 aus
    # pbar-dann-p (A1 S2.1) -- im Quotienten ist das die Aussage, dass die
    # Werte 4 (freie Paare) bzw. 2 (fixe) NIE ungerade sind:
    check("O1.e2 (Z) Kreuzterm-Paritaet == A1-Diamant des getauschten "
          "Paares", all(v % 2 == 0 for v in p_ss.values()),
          "alle Orbit-Werte gerade -- jede (2+i)-dann-(2-i)-Kette hat ihre "
          "(2-i)-dann-(2+i)-Partnerin im selben Endpunkt")

    # ---------------- O1.f: Wohldefiniertheit vom Repraesentanten ------------
    print("\n--- O1.f: Wohldefiniertheit (freie Repraesentanten) " + "-" * 24)
    free9 = [H for (p1, r1) in INERT3
             for H in base.down_layer(base.ID_BASIS, p1, r1)
             if not okey_fixed(H)[1]][:3]
    ok_wd = True
    for M in free9:
        Ms = base.sigma_module(M)
        for rule in (RAM, SPLIT5):
            a1, _ = one_layer_orbits(rule, start=M)
            a2, _ = one_layer_orbits(rule, start=Ms)
            ok_wd = ok_wd and (a1 == a2)
    check("O1.f1 (Z) Quotienten-Zaehler von M == von sigma M", ok_wd,
          "3 freie Norm-9-Zustaende x Regeln {ram, split5}: alle "
          "Orbit-Zaehler identisch -- die Orbit-Zaehlung ist "
          "repraesentanten-unabhaengig (gemessen, nicht angenommen)")

    # ---------------- O2: Anatomie + Satz-Kandidat ---------------------------
    print("\n--- O2: Ausnahme-Anatomie " + "-" * 51)
    check("O2.1 (Z) haelt UEBERALL -- Satz-Kandidat (klein)", 
          p_rs == p_sr and p_ri == p_ir and ok_wd,
          "SATZ-KANDIDAT (Orbifold-Konfluenz): der sigma-Quotient des "
          "Z[i]^4-Hecke-Multiway-Systems ist unter Orbit-Zaehlung "
          "konfluent/kausal-invariant; Grund: sigma ist ein Multiway-"
          "Automorphismus, der jede Regelklasse als Ganzes erhaelt, also "
          "vererbt sich der (CRT-erzwungene) Upstairs-Diamant durch die "
          "Faltung.  Kein Wolfram-Wunder: ein Zwei-Zeilen-Lemma -- aber "
          "als solches benannt und hier vollstaendig ausgemessen")
    check("O2.2 (W) bricht EXAKT an der ramifizierten Stelle + den freien "
          "inerten Zwischenzustaenden",
          only2 and n_dbl > 0 and n_eq + n_dbl == len(p_ri) and fix_ok,
          "ram x split: 100%% der %d Endpunkte Faktor 2; ram x inert: "
          "%d/%d Endpunkte Faktor 2 (die durch die %d freien inerten "
          "Zwischen-Paare laufen), %d gleichgewichtet (durch die 40 fixen); "
          "die Bruch-Lokalisierung ist DECKUNGSGLEICH IM ORT mit der "
          "[D,A]-Ausnahme (die ramifizierte Stelle als einzige komplett "
          "sigma-fixe Struktur), aber NICHT IM OBJEKT ([D,A] lebt auf dem "
          "mod-(1+i)-Faser-Operatorpaar, der (W)-Bruch auf einer "
          "selbstgewaehlten Orbifold-Massen-Konvention)"
          % (len(p_rs), n_dbl, len(p_ri), (820 - 40) // 2, n_eq))
    check("O2.3 NS/R-Interpretation (TYPISIERT ALS INTERPRETATION, kein "
          "Claim)", True,
          "v722: NS/R = Paritaets-Charakter an der ramifizierten Stelle; "
          "dass genau dort (a) die einzige sigma-fixe Volltreffer-Schicht, "
          "(b) die einzige [D,A]-Ausnahme und (c) der maximale (W)-Bruch "
          "zusammenfallen, LIESSE sich lesen als: die fermionische "
          "NS/R-Buchhaltung ist der Ort, an dem Orbifold-Zeitordnung "
          "nicht mehr frei waehlbar ist -- eine Interpretations-Schicht "
          "ohne eigenstaendige Messung; sie erzeugt hier KEINE neue "
          "Vorhersage")

    # ---------------- O3: Final-Adjudikation ---------------------------------
    print("\n--- O3: Final-Adjudikation der Zuse/Wolfram-Frage " + "-" * 27)
    print("    Datum dieser Sonde: der Orbifold-Quotient liefert KEINE "
          "kausale Anomalie --")
    print("    die kanonische Buchfuehrung (Z) ist ueberall konfluent "
          "(Satz-Kandidat, klein),")
    print("    der (W)-Bruch ist eine Eigenschaft der selbstgewaehlten "
          "Massen-Konvention und")
    print("    reproduziert nur den bekannten Sonderstatus der "
          "ramifizierten Stelle.")
    print("")
    print("    GESAMTVERDIKT ZUSE/WOLFRAM-LESART: AEQUIVALENT-NUETZLICH "
          "(nicht NEUE-STRUKTUR,")
    print("    nicht reine ERZAEHL-SCHICHT).  Empfehlung: als dokumentierte "
          "Exploration ruhen")
    print("    lassen (experiments/); KEIN Contracts/Paper-Platz -- "
          "hoechstens ein Verweis-Satz")
    print("    in der bestehenden introduction-Positionierung "
          "(Zuse--Schmidhuber--Wolfram),")
    print("    dass die Multiway-Lesart des Hecke-Turms ausgemessen wurde "
          "und exakt auf die")
    print("    bekannte Struktur zurueckfaellt (Konfluenz = CRT; Branchial "
          "= Grassmann-Zellen;")
    print("    Irreduzibilitaet = v702).")

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
