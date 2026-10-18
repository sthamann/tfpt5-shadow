# RH-Programm – Tagesbilanz 4. September 2026

Claim boundary: Forschungsprotokoll; kein Anspruch für oder gegen RH.

## Infrastruktur (neu, läuft)

- **Semantischer Katalog** `rh/catalog/`: 728 → **2035 Datensätze** (1060 kuratiert), 18 Fragmente, Schema/Taxonomie, CLI `rhcat`, LLM-Konsistenzprüfung, Hook/Rule/Skill, in `build.sh audit` verdrahtet. Konflikte 84 → 0, Ehrlichkeits-Flags 0.
- **Viewer** `rh/catalog/viewer/` (Vite + sigma.js **WebGL**, Layout zur Build-Zeit): Netzwerk, Zeitleiste, Matrizen, Kill-Roots, **Konzeptkarte** mit GAPS-Panel und Pfadfinder; Export SVG/PNG/CSV/JSON/GraphML/GEXF/ZIP. Erster Frame ≈ 80 ms, ≥ 80 FPS. Start: `cd rh/catalog/viewer && npm run build && npx vite preview --port 4177` → http://127.0.0.1:4177/
- **Konzeptkarte** `rh/catalog/map/`: **271 Knoten / 838 Kanten**, typisiert (äquivalent / impliziert / blockiert durch / würde schließen), CLI `rhmap path|gaps|equivalents`. Kopie in `_newest/graph/`.

## Der blinde Fleck

Der Katalog kannte nur `rh/` und die späten Probes. **295 Verification-Module (v535–v954), 185 [E]-Ledgerzeilen, `tfpt_prime_front.tex`, die Website-Erzählung** fehlten. Nach Aufnahme: 101 nie weiterverwendete [E]-Identitäten – Triage: **0 Hebel** (69 Endlich-Fenster, 29 formal, 3 strukturell ohne Ungleichung). Der frühe Stack war Buchhaltung, keine Munition.

## Kills heute (alle mit Kontrollen, exakt)

| Probe | Verdict | Kern |
|---|---|---|
| `kneser_groupoid_halfdensity_probe.py` | KILLED(K1) | Δ ≡ 1 für p = 3, 5, 7, alle markierten Kanäle |
| `parabolic_detline2_probe.py` | KILLED(K2) | Fixpunktspur symmetrisch 2q^{−m/2}/(1−q^{−m}), aber Ungerade-Potenz-Resummation ≠ Weil-Gewichte |
| `clock_combination_spectrum_probe.py` | KILLED 63/63 | endliche Uhren Rang 1; Resummationsturm log-rational, nicht kanonisch; Koide nur 6·log(3/2) |
| `hecke_index_theorem_probe.py` (L2) | KILLED(K2) | kein Korpus-Zustand, dessen Modularfluss der Indexfluss ist (Haar ⇒ Δ = 1) |
| Lean `SelectedArchErrorQuadraticRate` (feste Konstante) | **FALSIFIZIERT** | 8.0283 > 4.1259765625 im Kleinträger-Regime – galt bisher als „sealed“ (r475) |

## Bewiesen / konstruiert

- **Positive-Cone-Blindness-Lemma** (`positive_cone_blindness_probe.py`, exakt): Zertifikate aus positiven Maßen/Quadraten sind blind für das Verhältnis ν/μ (Skalenschwelle t* = 9/2). Klassifiziert alle „unabhängigen Positivitätsquellen“ (Waldspurger, Siegel–Weil, Rankin–Selberg, Cohen, SOS, Kasteleyn, Gibbs) als ungeeignet. Nur metrisch (L*) oder Operator (Hilbert–Pólya) bleibt.
- **Notwendigkeitssatz** (`compiler_necessity.md`): multiplikative Komposition + monotone additive Information ⇒ I(n) = c·log n; Primzahlen = unzerlegbare Erzeuger von ℕ×. Kein Orakel nötig – wenn ein kanonisches physikalisches Kompositionsgesetz existiert.
- **Brücke 1 konstruiert** (`census_qsm_normflow_probe.py`, CONSTRUCTED_CANONICAL_CLASSICAL): Zensus-QSM auf dem Gaußschen Rang-4-E8-Modul, Zeit = Index^{it}, H = log[M:L], KMS 15/15, Z = ∏_{j=0}^{3} ζ_{ℚ(i)}(s−j) 200/200 (Solomon). Connes–Marcolli-Typ mit TFPT-Modul; keine Nullstelleninformation; Gibbs-Positivität blind.
- **Indexsatz L1** (`hecke_index_theorem_probe.py`): Index = Überlagerungsgrad |det A|, alle Primzahlen ≤ 50 (Rang 8 über ℤ); Gaußsch nur p = 2, p ≡ 1 mod 4 → Ziel wird GRH(ζ·L(χ₋₄)). Kompakter Torus: Cutoff wächst wie Λ⁸, nicht log Λ – Connes' Term braucht den adelischen Quotienten.
- **Lean** (`rh/lean/RH/SelectedArchErrorQuadraticRateClassical.lean`): neue Schnittstelle `SelectedArchErrorQuadraticRateExists` (∃C); bewiesen sind (i) der nachgelagerte Konvergenzsatz aus dieser Form und (ii) die Implikation „gewichtete Interpolationsschranke ⇒ ∃C-Form“; die ∃C-Form selbst ist damit *bedingt* auf die noch offene Transkriptionsschranke; sechs sorry-freie Bausteine (1/12-Schranke, Knick-Defekt −θ(1−θ)/2, Konstantenlücke, Endpunktkorrektur (⌊b/Δ⌋+1)Δ). Offen: `SelectedArchWeightedInterpolationEstimate` (Summen/Integral-Transkription; numerische Identität 2.3e−25). Build 3578 Jobs grün, fünf geschützte `sorry`s unverändert.

## Analysen (Register: bewiesen / gemessen / behauptet)

- **Mechanismus-Anatomie** (`prime_story.md`): 8 Schritte P1/P2 → E8+μ4 → θ = E₄, 240σ₃ → χ₋₄-Zensus → Kneser/Hecke → 5 E₄-Altformen + 2 f₈ → Shimura → RTF. Primzahlen treten als Hecke-Index ein; TFPT-spezifisch nur χ₋₄ und f₈; g_car = 5 kommt in v535/v536 nicht vor (die „5“ sind die Teiler 1, 2, 4, 8, 16).
- **Ereignislog** (`event_log_function.md`): fünf statische Folgen; Λ(n) ist in jeder Probe Input; [E] endliche E8/Coxeter/μ4-Uhren können {log p} nicht (kommensurabel vs ℚ-unabhängig). Physikseite: keine Vorhersage hängt von Primzahlen ab; Nullfunde: foliation 0, 3+1 0, emergent time 0, scaling flow 0, ideles 0, ℚ*₊ 0; kein Unitaritätsaxiom für emergente Zeit. Checksum-Intuition ψ(x) − x = O(√x log²x) ⇔ RH (von Koch).
- **π** (`pi_prime_correlations.md`, `archimedean_pi_conformity_probe.py`): Primzahlen bestimmen π (Satz); π/4 = L(1,χ₋₄) mit 4 = |μ4| (Klassenzahlformel ℚ(i)). Messung: δ* = λ_min exakt (log π wirkt im Fenster als Vielfaches der Identität): 9.3e−7 / 3.9e−11 / 1.6e−17 bei L = 0.5 / 0.65 / 0.8; Scramble-Welt negativ (−0.43, −0.30). Numerologie c₃ = 1/(32·L(1,χ₋₄)) markiert (0 Herleitungstreffer). π-Ziffern ↔ Primzahlen: null (p = 0.33). Konditionierung, keine Feinabstimmung.
- **Richter (Opus)**: Waldspurger × Zensus = Kategorienfehler (direkte Summe; positive Maßquelle vs signiertes Defektmaß); Cohen-Seeds und Rankin–Selberg klassisch-neutral; Siegel–Weil echt, aber ¼-Shift zum Zentrum = Weil-Kriterium + Farkas-Zeuge n ≡ 6 mod 8; additive Adele × Siegel–Weil = Tate/Connes–Meyer-Restatement; Ereignislog-Test wohlgestellt, Ausgang bereits bewiesen. Keine der vier Kombinationen laufen lassen.
- **Brücke 2 – Gestalt** (`bridge2_direct_search.md`): einzig zulässige Gestalt = manifest positive (Markov-)Skalen-Halbgruppe mit Funktionalgleichung als Reflexion, deren *Generator selbst* die Nullstellen trägt (Bochner ⇔ OS-Reflexionspositivität ⇔ Hilbert–Pólya). TFPT hat davon nur die Euler-Seite (Untergitter-RG auf ℝ⁸/E8, Zweipunktfunktion = Solomon-Zeta, per Term positiv ⇒ blind). Alle heutigen Kills sind dieselbe Tatsache.
- **Brücke 2 – Literatur/Korpus** (`bridge2_object_search.md`, `positivity_origin_search.md`): 16 Positivitätsstrukturen der Ursprungsschicht, nur E8-Theta/Heat trägt beide Datensorten, Spektrum diskret. 12 Arbeiten (Connes/Meyer; Connes–Consani; Connes–Consani–Moscovici 2025 endliche selbstadjungierte Störungen, Konvergenz offen; Suzuki 2022–2026 Schraubenfunktion/A_a, Positivität nur für kleine a; Conrey–Li: de-Branges-Positivität scheitert für ξ – Operatorpositivität kann stärker als RH sein; Yoshida/Bombieri 2L ≤ log 2; Chuk L = 0.8 = 2.3× klassische Reichweite). Korpus: W1 geschlossen, W2 partiell, uniformes W3 = Wand, W4 offen, L* = metrische Lücke. Korrigiert: keine semidefinite Arch/Prim-Zerlegung (2cos(aξ) wechselt Vorzeichen); kompakter Träger ≠ endlicher Höhen-Cutoff (Paley–Wiener).
- **Programm-Evolution** (`experiments/tfpt-discovery/evolve/`): T1-Schranke 0.3313(‖g″‖₁ + ‖g‖_{H²})Δ², 0/72 Verletzungen; T2 kein Approximationslemma (Kanal-Brücke); T3 alle k = 5…16 positiv (kein Signal). Ohne API-Key deterministisch, 0 $.

## Offen – präzise

1. **Kegelsatz** `frequently_selected_augDualResolvent_ge_half` – uniforme untere Schranke R†(W_k) ⪰ ½I entlang einer kofinalen Teilfolge (RH-schwer).
2. **Kanal-Brücke** `SelectedPolynomialApproximatesGrid` – enthält die Positivität (fullRead ≥ −err_arch), r473 NO_BRIDGE.
3. **Arch-Rate ∃C** – klassische Transkription `SelectedArchWeightedInterpolationEstimate` (nicht schwer, nicht fertig).
4. Substanzieller nächster Weg laut Literatur und Korpus: **uniforme Resolventen-/Determinantenkonvergenz mit expliziter Tail-Norm** (TEL-B Bound B `BOUND_B_SKETCH_INCOMPLETE`, relative Determinante, Suzuki A_a, CCM-Störungen).

## Stand in einem Satz

Brücke 1 steht (Zeit mit Primzahlen als Erzeuger, orakelfrei, klassisch); Brücke 2 ist offen, ihre einzig zulässige Gestalt ist fixiert; TFPT besitzt davon nur die Euler-Seite; die Lean-Route hat zwei schwere und einen klassischen offenen Satz, und ein bisher als „sealed“ geführter Satz ist falsifiziert und additiv repariert.

## Dateien

- Graph-Kopie: `_newest/graph/` (rh_concept_map.json, gaps_report.json, graph.json, concepts.json, GraphML/DOT/CSV/SVG-Exporte, Screenshots)
- Analysen: `rh/catalog/analysis/*.md|json`
- Probes: `experiments/tfpt-discovery/*_probe.py` + `*_result.json`
- Canvas: `canvases/RH-research-audit.canvas.tsx`

## Geometrie-Audit (Nachtrag 19:00)

G1: 66 gestaltrelevante Nullversuch-Konzepte klassifiziert; keines echt neu und formrelevant. Karte 253→271 Knoten / 838 Kanten. Kein RH-Claim.

Verdikte gegen die fixierte Brücke-2-Gestalt (I1–I5):

- Quasikristalle (Dyson, renormalisiert) und Fraktalsaiten (Lapidus–Maier) = RH-Umformulierungen; erzeugen keine fehlende Positivität.
- Quantum-Graphen = bedingtes No-Go: verbundene Graphen erzeugen gemischte log(pq)-Bahnen (no-composite-orbits); Auslöschungskonstruktionen existieren, liefern aber keinen kanonischen globalen Graphen.
- f8 = LMFDB 8.4.a.a = H³-L-Funktion starrer Calabi–Yau-Dreifaltigkeiten (Hulek–Verrill, arXiv:math/0504070) — echte Geometrie, für ζ RH-neutral.
- Möbius-Skalengruppe reduziert auf Tate / Berry–Keating / Connes; Möbiusband gestaltirrelevant.
- K3-Hodge-Index und Rosati-Positivität gelten lokal und sind global blind.
- Hyperbolische Ruelle-Zeta: bekanntes Längenspektrum ≠ {log p}; kein Starrheitssatz gegen jedes Mannigfaltigkeitsmodell.
- Einziger überlebender Vertrag: adelische stochastische Skalen-Halbgruppe / Deninger–Arakelov-Realisierung (bereits die Brücke-2-Lücke).
- Zentrale Anforderung: Produkt über alle Stellen — nur so sind Primorbit p, Wiederholungen p^k, archimedischer Faktor und Skalenreflexion dasselbe Objekt.

Nachbarn von `no-composite-orbits`: quantum-metric-graph / hyperbolic-ruelle-dynamics BLOCKED_BY; decoupling-lemma REDUCES_TO; adele-class-space und stochastische Skalen-Halbgruppe REQUIRES. G1=199, G2=8, G4 enthält die neue Barriere (killed_by=0).

## Nachtrag 5. Sep – externe Vorschläge (Wärme-Gabor, dyadisches Nyman–Beurling)

A **RESTATED.** \(\mathcal H\) ist die Gauß-geglättete reelle Nullstellendichte (\(\pi\sqrt{2\pi}\,K_a*\operatorname{Re}\mu_\zeta\)). Budget \(a=1/32\): Primseite 429 exakt / 774 PNT gegen Spielraum 286; Härte unverändert (\(e^{1/(8a)}\) gegen \(e^{1/\sqrt a}\)).

B **MEASURED.** Tabelle bis \(N=512\) auf 12 Stellen reproduziert. \(k\cdot\eta_k\): 0.19, 0.40, 0.60, 0.69, 0.88, 0.73, 0.99 — nicht monoton. Fit \(C=0.046249\) gegen Báez-Duarte \(2+\gamma-\log 4\pi=0.046191\). Burnol-Bound nur Linien-Nullstellen. \(\eta_k\ge c/k\) stärker als die Ratenvermutung; kein Rechenkontrakt; offene Frage in der Karte.

Kein RH-Claim. Artefakte: `heat_gabor_restatement_probe.py`, `nb_dyadic_capture_probe.py`, `external_proposals_heat_nb.md`.
