---
format: 1920x1080
duration: 186s
message: "The Prime Front: the TFPT prime line — from the E8 lattice to the Weil operator, to the detector, to the smallest form of the open question. Honest: no proof of RH."
arc: concept-explainer
audience: the author himself and math-curious lay readers (English)
language: en-US
mode: autonomous
music: none
---

## Video direction

- **Palette (aus frame.md, nie erfinden):** Alle Frames im dunklen Register — Grund `ink-black` (#020617, ggf. `ink-black-alt` als Panel-Fläche), Text `cream` (#e2e8f0), Sekundärtext `cream-muted`/`cream-hint`, Hairlines `border-dark`. `fire-orange` (#38bdf8, Sky-Blau) ist der EINZIGE Akzent — Nullstellen-Linie, Zahlen-Highlights, Akzent-Clauses, der Korridor-Punkt. Kein zweiter Farbton; "bricht/negativ" wird über Form (gekreuzter Marker, Nadel unter Null-Hairline, gestrichelte Umrisse) erzählt, nie über Rot.
- **Typo-Rollen:** Newsreader-Serif (display/h1/h2/stat-value) für Statements und Zahlen-Helden; Inter (body/lead) für Erklärzeilen; JetBrains Mono (label) uppercase-getrackt für Kicker, Modul-IDs (v643, v677 …), Achsen und Chrome. Deutsch bleibt in normaler Groß-/Kleinschreibung.
- **Motion-Grammatik + Reveal-Modell:** Smooth long-tail (`power3`), nie bouncy. Jeder Frame reveals VO-getaktet — bei t=0 nur, was gerade gesprochen wird; jedes weitere Element erscheint auf seinem Wort-Cue, verteilt bis in die hintere Hälfte. Interne Nähte als velocity-matched cuts. Während Holds: Stille; höchstens subtle jitter (`sine-wave-loop`, low) oder ein lebendes SVG-Innenleben (Detektor-Nadel, fließende Dash-Linie). Kein Atmen, kein Back-half-Pan/Push.
- **Rhythmus / Held-Frames:** Frame 1 endet auf einem gehaltenen "Unbewiesen"-Read; Frame 8 (Korridor) ist der ruhige Fokus-Frame vor der Landung; Frame 9 ist bewusst langsam — Statement-Beats mit Luft. Frames 4–5 sind die dichtesten; danach fällt die Energie kontrolliert ab.
- **Negativ-Liste:** kein Bouncy/Overshoot, keine Breathing-Loops, kein Slow-Pan in der hinteren Hälfte, keine purple-blue-AI-Gradients, kein Stock-Material, keine Browser/UI-Chrome, kein zweiter Akzent, kein forced lowercase. Beide Failure-Modes verboten: Slideshow (alles bei t=0, dann eingefroren) und Screensaver (alles schwebt unabhängig).
- **Caption-Band:** Untere ~17 % frei halten; zentrierte Helden ankern bei y ≈ 0,42 × Höhe. Hintergrund-Layer (Grid, Glow) dürfen full-bleed.

## Frame 1 — Die Musik der Primzahlen

- scene: Ein Zahlenstrahl baut sich auf, Primzahlen ticken herein; darüber erscheint die kritische Linie, auf der Nullstellen-Punkte einrasten
- voiceover: "The prime numbers look like randomness. But their distribution follows a hidden orchestra: the zeros of the Riemann zeta function. The Riemann Hypothesis says: all of them lie on one single line. Unproven — for more than one hundred and sixty-five years."
- duration: 16.872s
- transition_in: cut
- status: animated
- src: compositions/frames/01-musik-der-primzahlen.html
- type: hook
- persuasion: Visceral metaphor (Orchester) + Konkretisierung (Zahlenstrahl → Linie)
- beat: Neugier + Staunen
- blueprint: dataviz-countup (Adapt)
- focal: die kritische Linie mit einrastenden Nullstellen-Punkten
- roles: Zahlenstrahl mit Prim-Ticks = foreground subject (Akt 1) · kritische Linie + Nullstellen = foreground subject (Akt 2, übernimmt) · Hairline-Grid + dunkler Grund = background (dim) · Mono-Labels (2, 3, 5, 7 … / "Re(s) = 1/2" / "seit 1859") = supporting

Adapt: dataviz-countup — der "Chart" ist der Zahlenstrahl + die kritische Linie; der Camera-Push-Through wird ein sanfter Fokuswechsel vom Strahl zur Linie; Signature (Zahlen/Daten als Held, Push zum Hero-Metric) bleibt: der Hero-"Metric" ist die Linie selbst.
Scene 1 (0.0–2.7s): Dunkler Grund, dezentes Hairline-Grid full-bleed (background, dim ~35%). Ein horizontaler Zahlenstrahl (full-width strip, y ≈ 0,42) zieht sich per SVG self-draw (`svg-path-draw`) auf; Prim-Ticks 2, 3, 5, 7, 11, 13 … poppen unregelmäßig herein (`spring-pop-entrance`, smooth settle) — das unruhige Timing IST das "wie Zufall".
Scene 2 (2.7–8.5s): Auf "verborgenen Orchester" (4.4s) blendet über dem Strahl eine leise Wellen-Schicht ein (2–3 überlagerte Sinus-Züge, SVG self-draw, accent 25%); auf "Nullstellen der Zetafunktion" (6.0s) verdichten sich Wellen-Knoten zu Punkten (`scale-swap-transition` klein). Layout wird asymmetrisch 60/40: Strahl unten, Wellenfeld darüber, 3 Tiefen-Layer.
Scene 3 (8.5–12.6s): Auf "Die Riemannsche Vermutung sagt" (8.6s) zeichnet sich rechts eine vertikale Akzent-Linie (`svg-path-draw`, fire-orange); die Punkte gleiten nacheinander auf die Linie und rasten ein (sequenzielle Reveals, `power3`), Punkt für Punkt bis "einer einzigen Linie" (11.8s) — keyword glow (`asr-keyword-glow`) auf dem letzten einrastenden Punkt. Mono-Label "Re(s) = 1/2" erscheint an der Linie.
Scene 4 (12.6–16.9s): Auf "Unbewiesen" (13.1s) reveals darunter eine Mono-Zeile "SEIT 1859 · UNBEWIESEN" (`discrete-text-sequence`); auf "hundertfünfundsechzig" (14.4s) tickt ein value-scaled counter (`counting-dynamic-scale`) von 0 auf 165+. Danach: gehaltener Read, nur die Nullstellen-Punkte tragen subtle jitter (`sine-wave-loop`, low).

narrativeRole: Öffnet die kognitive Lücke: Chaos (Primzahlen) gegen verborgene Ordnung (eine Linie). Etabliert RH in einem Satz, ohne Formalismus.
keyMessage: Die Riemannsche Vermutung behauptet: Alle Nullstellen der Zetafunktion liegen auf einer einzigen Linie — seit über 165 Jahren unbewiesen.

## Frame 2 — Der TFPT-Zugang: Geometrie zuerst

- scene: Stationen-Kette auf einer Leinwand: E8-Gitter (Punktrosette) → Zählfunktion Θ = E4 → Hecke-Prüfkanäle (2, 3, 5, 7 …) → ζ als Schatten
- voiceover: "The TFPT builds the E8 lattice from two axioms. Its counting function already knows the primes: each one acts as its own Hecke check channel. And the zeta function appears as a shadow of this geometry."
- duration: 13.848s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/02-geometrie-zuerst.html
- type: product_intro
- persuasion: Causal chain (A → B → C) + Signposting
- beat: Orientierung
- blueprint: spatial-pan-stations (Reproduce)
- focal: die E8-Rosette (Station 2) und die Hecke-Kanal-Pills (Station 3)
- roles: Stationen-Karten (Axiome / E8-Rosette / Θ=E4 + Hecke-Pills / ζ-Schatten) = foreground subjects nacheinander · übergroße Leinwand mit Hairline-Verbindungslinien = background · Mono-Kicker "GEOMETRIE ZUERST" + Modul-Tag "v625" = supporting

Reproduce: spatial-pan-stations — vorplatzierte Stationen auf EINER übergroßen Leinwand, eine virtuelle Kamera (`viewport-change` auf einem .world-Wrapper) pannt lateral von Station zu Station; Signature (wiederholte laterale Pans, Landung auf der letzten Station) bleibt wörtlich.
Scene 1 (0.0–2.4s): Kamera steht links: Station 1 — zwei Axiom-Chips "c₃ = 1/(8π)" und "g = 5" (Mono, Hairline-Border) poppen nacheinander (`spring-pop-entrance`, smooth). Verbindungs-Hairline zeichnet nach rechts (`svg-path-draw`).
Scene 2 (2.4–4.4s): Auf "E-acht-Gitter" (2.6s) lateral pan zu Station 2: die E8-Rosette (240-Punkt-Projektion als konzentrischer Vektor-Stern) zeichnet sich selbst (`svg-path-draw`, accent-Hairlines), Punkte cascaden herein (staggered). Mono-Label "E₈ · 240 Wurzeln".
Scene 3 (4.4–9.6s): Pan zu Station 3 auf "Zählfunktion" (4.6s): Karte "Θ_E8 = E₄" mit Schalen-Zeile "240 · σ₃(n)"; auf "Jede wirkt als eigener Prüfkanal" (6.9–8.2s) cascaden Hecke-Pills "T₂ T₃ T₅ T₇ T₁₁ …" herein (`dynamic-content-sequencing`, per-Pill auf den Sprech-Rhythmus).
Scene 4 (9.6–13.8s): Letzter Pan auf "Zetafunktion" (10.2s): Station 4 — ein ζ-Zeichen erscheint als Schatten-Karte (weicher statischer Glow hinter dem Glyph, dim — reiner Stil, kein Loop); auf "Schatten dieser Geometrie" (11.7s) reveals die Mono-Zeile "GEOMETRIE ZUERST — PRIMZAHLEN ALS AUSLESE · v625". Kamera landet, hält; keine Bewegung mehr.

narrativeRole: Führt den Protagonisten ein — die Erklärungsrichtung "Geometrie zuerst, Primzahlen als Auslese" (v625), als Stationen-Kette gepannt.
keyMessage: Aus dem E8-Gitter der TFPT entsteht die klassische Primzahl-Maschinerie: Zählfunktion, Hecke-Kanäle, Zeta als Schatten.

## Frame 3 — Die Fenstermatrix ist ein Weil-Operator

- scene: Zwei Panels klappen auf: links die TFPT-Fenstermatrix (Gitter-Heatmap), rechts Suzukis Weil-Operator (Integral-Kern); ein "="-Badge rastet ein, darunter der Stempel "W1 — Theorem (v643)"
- voiceover: "From this bookkeeping came a window matrix. And it turned out to be something classical: word for word, Suzuki's localized Weil operator. That is the W1 theorem — machine-verified, with one honestly documented erratum."
- duration: 15.288s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-w1-theorem.html
- type: feature_showcase
- persuasion: Comparison of two options → Identifikation (zwei Seiten, ein Objekt)
- beat: Aha + Überraschung
- blueprint: comparison-split (Reproduce)
- focal: das "="-Badge zwischen den beiden Panels
- roles: linkes Panel (TFPT-Fenstermatrix als kleine Zellen-Heatmap in Akzent-Abstufungen) = foreground subject · rechtes Panel (Suzukis Weil-Operator, Integral-Kern-Motiv g″(t)) = foreground subject · "="-Badge + Stempel "W1 · THEOREM · v643" = supporting-Held des Payoffs · Erratum-Chip = supporting · dunkler Grund + Hairline = background

Reproduce: comparison-split — zwei gleichgewichtige Karten treten mit gespiegelten 3D-Book-open-Tilts von den Flügeln ein (`split-tilt-cards`), Inner-edge-Badge spring-poppt als Interpunktion; Signature (mirrored tilts + Badge-Pop) bleibt wörtlich.
Scene 1 (0.0–3.8s): Auf "Fenstermatrix" (1.9s) klappt das LINKE Panel ein (`split-tilt-cards`, von links): Titel "TFPT — Fenstermatrix", darunter eine kleine n×n-Zellen-Heatmap, deren Zellen zeilenweise aufleuchten (staggered reveal); Mono-Tag "aus der E₈-Buchführung". Rechte Hälfte bleibt LEER.
Scene 2 (3.8–9.0s): Auf "etwas Klassisches" (5.1s) klappt das RECHTE Panel gespiegelt ein: Titel "Suzuki — Weil-Operator", Integral-Kern-Motiv (geschwungene g″-Kurve, SVG self-draw) und Mono-Tag "klassische Zahlentheorie · 2026". Auf "Wort für Wort" (6.2s) blinken korrespondierende Zellen/Kurvenpunkte paarweise auf (keyword glow, synchronisiert links↔rechts).
Scene 3 (9.0–12.2s): Auf "W-eins-Theorem" (9.8s) spring-poppt das "="-Badge an der Innenkante (`spring-pop-entrance`, smooth); darunter stempelt "W1 · THEOREM · v643" (hard-cut Reveal, Mono); auf "maschinell verifiziert" (10.7s) keyword glow auf dem Stempel.
Scene 4 (12.2–15.3s): Auf "Erratum" (13.8s) reveals unten ein schmaler ehrlicher Chip: "Erratum: selbst gefunden, am selben Tag korrigiert — dokumentiert" (`discrete-text-sequence`). Hold; nichts bewegt sich mehr.

narrativeRole: Der erste Höhepunkt: Zwei unabhängig entwickelte Objekte — TFPT-Fensterform und Suzukis Weil-Operator — sind dasselbe (W1-Theorem, v643). Die Ehrlichkeit (Erratum am selben Tag) gehört zur Pointe.
keyMessage: Die Fenstermatrix der TFPT IST eine Galerkin-Diskretisierung von Suzukis Weil-Operator — als maschinell verifiziertes Theorem.

## Frame 4 — Der Detektor und der Falsifikator

- scene: Ein Prüfstand-Panel: Zeile "Ramanujan-Graphen" läuft durch und bekommt ein Häkchen (bewiesene Welt, besteht); Zeile "Epstein" schlägt aus — Detektor-Nadel kippt ins Negative, Callout "12 Off-Line-Nullstellen · Bruch vorhergesagt: 0,803"; dann Matched-Filter-Formelkarte
- voiceover: "The same window form is a detector. Calibrated on solved worlds: Ramanujan graphs — where the analogue is proven — pass the test. Epstein zeta functions — with genuine zeros off the line — break it, exactly as predicted. And the matched filter makes this constructive: any off-line zero would produce a computable witness. The object is falsifiable."
- duration: 24.36s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-detektor-falsifikator.html
- type: feature_showcase
- persuasion: Demonstration (Mechanismus läuft) + Counterexample (Epstein bricht)
- beat: Vertrauen + Spannung
- blueprint: agent-progress-theater (Adapt)
- focal: die Detektor-Nadel (λ_min-Zeiger) über der Null-Hairline
- roles: Instrument-Karte mit Nadel + Null-Hairline = foreground subject · Prüf-Zeilen (Ramanujan ✓ / Epstein ✗) = supporting, werden nacheinander zum Fokus · Matched-Filter-Formelkarte = foreground subject des vierten Akts · Callout-Chips (0,803 · 12 Nullstellen · 2αδ ≥ 1,97) = supporting · Grund + Hairline-Chrome = background

Adapt: agent-progress-theater — der "Agent" ist der Prüfstand: Status-Zeilen laufen, die Quittung cascadet als Checkliste mit Badge-Flips. Behalten: Working-State-Theater + Checklisten-Receipt (Signature). Geändert: statt Loader-Spinner eine physikalische Detektor-Nadel; der Abschluss ist keine Konversation, sondern die Formelkarte des Matched Filters.
Scene 1 (0.0–2.8s): Zentriert (~50 %) eine Instrument-Karte: horizontale Skala mit Null-Hairline, eine Nadel ruht knapp ÜBER Null (accent); Mono-Label "λ_min — Positivitäts-Marge". Auf "Detektor" (1.2s) keyword glow auf dem Label. Die Nadel trägt durchgehend ein lebendes Micro-Zittern (`svg-icon-enrichment` — Instrument lebt, Karte atmet nicht).
Scene 2 (2.8–9.2s): Layout evolviert zu asymmetrisch 60/40 (Instrument links, Prüfliste rechts). Auf "Ramanujan-Graphen" (4.6s) slidet Prüf-Zeile 1 ein: "Ramanujan-Trio — RH-Analogon BEWIESEN"; ein Fortschritts-Strich läuft durch (`stat-bars-and-fills`); auf "bestehen den Test" (7.6s) flippt das Badge auf ✓ (hard-cut), die Nadel bleibt ruhig im Positiven.
Scene 3 (9.2–14.6s): Auf "Epstein" (9.4s) slidet Zeile 2 ein: "Epstein-ζ — echte Off-Line-Nullstellen"; der Strich läuft — auf "bricht" (11.9s) kippt die Nadel UNTER die Null-Hairline (schneller, aber smooth-gedämpfter Ausschlag), das Badge flippt auf ein gekreuztes ✗ (Form, kein Rot); auf "vorhergesagt" (13.0s) reveals der Callout-Chip "Zensus: 12 Off-Line-Nullstellen · λ-Ratio 0,803 vorhergesagt" (hard-cut Reveal, `discrete-text-sequence`).
Scene 4 (14.6–21.4s): Velocity-matched cut (cut-the-curve): die Prüfliste schiebt nach oben aus dem Fokus, von unten kommt die Matched-Filter-Karte. Auf "Matched Filter" (15.0s) typt die Formel "x_mf[j] = cos(ω_j γ₀) · sinh(ω_j δ)" zeichenweise (`discrete-text-sequence`); auf "nachrechenbaren Zeugen" (18.8s) reveals die Zeile "jede Off-Line-Nullstelle ⇒ konstruierbarer negativer Testvektor · ab 2αδ ≥ 1,97" per-word (`dynamic-content-sequencing`).
Scene 5 (21.4–24.4s): Auf "falsifizierbar" (22.4s) landet das Statement "Das Objekt ist falsifizierbar." als Serif-Zeile mit keyword glow auf "falsifizierbar"; alles andere dimmt leicht (Opacity-Absenkung der Hintergrund-Karten, kein Blur-Rig). Hold.

narrativeRole: Zeigt, dass die Form in beide Richtungen scharf ist: Sie besteht dort, wo das RH-Analogon bewiesen ist, bricht dort, wo echte Off-Line-Nullstellen sitzen — und jede RH-Verletzung wäre konstruktiv auffindbar (Matched Filter, 46/48 Maskierungen gebrochen).
keyMessage: Die Fensterform ist ein kalibrierter Detektor: Ramanujan besteht, Epstein bricht wie vorhergesagt — jede Off-Line-Nullstelle wäre konstruierbar auffindbar.

## Frame 5 — Zwei Sätze auf der ganzen Fläche

- scene: Stat-Karten bauen sich auf: "det S > 0 — unbedingt, 67/67 Fenster" mit Mini-Zahlenstrahl (Trägerfrequenzen 0,6–1,3 weit unter der ersten Nullstelle 14,13; Dämpfung ×634); daneben Fenster-Karte 60/70 gefüllt, Restliste mit T*-Höhen
- voiceover: "Two theorems stand on the whole surface. The sign of the determinant: unconditionally proven, on all sixty-seven windows — the century-old zero-free region blocks the only escape route. And the margin: sixty of seventy windows, closed with cited classical results."
- duration: 18.144s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-zwei-saetze.html
- type: social_proof
- persuasion: Statistical proof + Worked example (Frequenz-Argument)
- beat: Überzeugung
- blueprint: grid-card-assemble (Adapt)
- focal: die Fenster-Karte (70 Kacheln, 60 füllen sich) und die Stat-Zahl "67/67"
- roles: Stat-Karte 1 "det S > 0" mit Zähler = foreground subject (Akt 1) · Frequenz-Strip (0,6–1,3 vs. 14,13) = supporting-Diagramm · Fenster-Kachel-Karte (70 Squares) = foreground subject (Akt 3) · Mono-Kicker "ZWEI SÄTZE · 3. AUGUST" + Zitat-Tags (Platt–Trudgian · Ingham 2025) = supporting · Grund + Hairline-Chrome = background

Adapt: grid-card-assemble — die Signature (Items cascaden staggered in ein Raster und halten) trägt zwei Assemblies: erst die Stat-Karte + ihr Frequenz-Strip, dann die 70er-Kachelwand. Geändert: kein Zoom-out-Finale; das Raster IST der Beweis-Payoff.
Scene 1 (0.0–3.1s): Mono-Kicker "ZWEI SÄTZE · 3. AUGUST" reveals (label, uppercase); Hairline-Chrome oben/unten zeichnet sich. Bühne sonst leer — Spannung auf die Zwei.
Scene 2 (3.1–8.2s): Auf "Vorzeichen der Determinante" (3.4s) assembliert Stat-Karte 1 links (60/40-Layout): große Serif-Zeile "det S > 0", Subzeile "unbedingt · kein RH-Input"; auf "siebenundsechzig" (6.7s) tickt der Zähler "67/67 Fenster" hoch (`counting-dynamic-scale`, accent).
Scene 3 (8.2–12.8s): Auf "hundertjährige nullstellenfreie Zone" (8.4s) zeichnet sich unter der Karte ein Frequenz-Strip (full-width innerhalb der Kartenspalte): Träger-Band 0,6–1,3 nahe der Null, weit rechts ein Tick "γ₁ = 14,13"; die Lücke füllt eine schraffierte Zone (`svg-path-draw`); auf "Fluchtweg" (11.3s) reveals das Mono-Label "nullstellenfreie Zone · Dämpfung ×634" mit keyword glow.
Scene 4 (12.8–18.1s): Auf "die Marge" (13.1s) cascadet rechts die Fenster-Kachelwand: 70 kleine Squares (`grid-card-assemble`-Stagger); auf "sechzig von siebzig" (13.7–14.4s) füllen sich 60 mit Akzent (sequenzielle Wellen-Füllung, `stat-bars-and-fills`), 10 bleiben als Hairline-Umrisse; auf "zitierter Klassik" (16.2s) reveals die Subzeile "Rest: exakte Liste, T* ≤ 8,5·10¹⁴ · Platt–Trudgian · Ingham 2025". Hold auf dem fertigen Raster.

narrativeRole: Grounding mit den zwei Flächen-Sätzen des 3. August: der unbedingte Vorzeichen-Satz (det S > 0, kein RH-Input) und der T-B-Zensus (60/70 modulo Zitaten) — konkrete Zahlen statt Behauptungen.
keyMessage: Vorzeichen unbedingt bewiesen auf 67/67 Fenstern; die Marge auf 60 von 70 Fenstern mit zitierter Klassik geschlossen.

## Frame 6 — Die Ihara-Blaupause: der fehlende Motor

- scene: Blaupausen-Schema (technische Zeichnung): eine Maschine "A = G_C + G_S" — Bauteil 1 "Chebyshev-Quadratsumme" (immer positiv, montiert), Bauteil 2 "Defekt ⪰ 0 ⟺ Ramanujan" (montiert); daneben dieselbe Maschine auf der ζ-Seite — ein Bauteil-Umriss gestrichelt leer, Label "Z1 — der Motor (Hilbert–Pólya)"
- voiceover: "Then, August third: in the graph laboratory, where the analogue is proven, the target decomposition exists exactly — a sum of squares plus a defect. Our window form is built identically. One part is missing: the engine, Z1. Hilbert–Pólya, in window coordinates."
- duration: 19.344s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-ihara-blaupause.html
- type: feature_showcase
- persuasion: Analogy (baugleiche Maschine) + Frame-then-fill
- beat: Faszination + Klarheit
- blueprint: compose
- focal: der leere, gestrichelte Motor-Slot in der ζ-Maschine
- roles: linke Maschine (Ihara-Labor, komplett montiert) = foreground subject (Akt 1) · rechte Maschine (ζ-Fensterform, ein Slot leer) = foreground subject (Akt 2) · Formel-Zeile "A = G_C + G_S · G_S ⪰ 0 ⟺ Ramanujan" = supporting · Blaupausen-Grid + Eck-Vermassungen = background (dim, technische Zeichnung) · Label "Z1 — der Motor" = supporting-Held des Payoffs

Compose: technische Blaupause in zwei Spiegelhälften; Kern-Move ist Frame-then-fill — erst die komplette Maschine, dann die baugleiche Kopie mit exakt EINEM leeren Slot; Payoff ist ein zoom-to-target auf die Leerstelle.
Scene 1 (0.0–2.1s): Blaupausen-Grund: feines Hairline-Grid, Eck-Vermassungen, Mono-Kicker "3. AUGUST · DAS IHARA-LABOR" reveals. Split-screen-Layout kündigt sich per mittiger Hairline an.
Scene 2 (2.1–8.9s): Links zeichnet sich die Labor-Maschine (`svg-path-draw`, Umriss-Gehäuse); auf "existiert die Ziel-Zerlegung exakt" (5.1–6.6s) rasten zwei Bauteile nacheinander ein (`spring-pop-entrance`, smooth): Block "G_C — Chebyshev-Quadratsumme · immer ⪰ 0" und Block "G_S — Defekt"; auf "Quadratsumme plus Defekt" (7.3–8.3s) typt darunter die Formel-Zeile "A = G_C + G_S · G_S ⪰ 0 ⟺ Ramanujan" (`discrete-text-sequence`). Mono-Tag "hier ist das RH-Analogon BEWIESEN".
Scene 3 (8.9–12.4s): Auf "baugleich" (10.9s) spiegelt sich das Gehäuse nach rechts (velocity-matched cut, beide Hälften kurz in Bewegung): dieselbe Silhouette, Label "ζ-Fensterform", der G_C-Block rastet ein — aber der zweite Slot bleibt ein GESTRICHELTER Umriss (dash-flow lebt subtil, `svg-icon-enrichment`).
Scene 4 (12.4–19.3s): Auf "ein Bauteil" (13.2s) zoom-to-target (`coordinate-target-zoom`) auf den leeren Slot; auf "der Motor" (14.3s) reveals das Label "Z1 — der Motor" (Serif, accent), auf "Hilbert–Pólya" (15.7s) die Subzeile "Hilbert–Pólya, in Fensterkoordinaten · Spuren = Fenstermomente" per-word. Ambient glow (`ambient-glow-bloom`, schwach) pulst EINMAL im leeren Slot, dann Hold.

narrativeRole: Der Verständnis-Kern des 3. August: Die gesuchte Faktorisierung existiert exakt im bewiesenen Labor (Ihara/Ramanujan); die ζ-Fensterform ist strukturell dasselbe Objekt; es fehlt genau Z1 — der selbstadjungierte Operator, dessen Spuren die Fenstermomente sind.
keyMessage: Die Maschine ist baugleich zum bewiesenen Labor — es fehlt genau ein Bauteil, der Motor Z1 (Hilbert–Pólya in Fensterkoordinaten).

## Frame 7 — Die Geometrie liefert das Maß

- scene: Aus dem E8-Schalen-Zähler tickt die von-Mangoldt-Leiter heraus (Λ_geo = Λ, exakt); darunter läuft der Γ-Fluss als Kurve, die an jedem Primpotenz-Slot in eine Singularität liefe — das Atom mit erzwungener Masse fängt sie ab; Zähler "Masse erzwungen: 0,11 % Median"
- voiceover: "And the geometry supplies the measure: the prime atoms can be read off, without circularity, from lattice counting alone. The gamma flow forces their masses to per mille — and their positions. But honestly: as a test bench, not as a generator."
- duration: 16.176s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-mass-gesetz.html
- type: benefit_highlight
- persuasion: Demonstration + ehrliche Grenze (Verifizierer, nicht Generator)
- beat: Momentum + Nüchternheit
- blueprint: dataviz-countup (Adapt)
- focal: die Γ-Fluss-Kurve mit den abfangenden Atom-Massen
- roles: Schalen-Zähler-Chips (240 · 2160 · 6720 …) = supporting (Akt 1) · Λ-Leiter (Ticks bei log 2, log 3, log 4 …) = foreground subject (Akt 2) · Γ-Fluss-Kurve + Atom-Punkte = foreground subject (Akt 3, Held) · Chip "Prüfstand, nicht Generator" = supporting-Landung · Grund + Grid = background

Adapt: dataviz-countup — Daten sind der Held (Zähler-Chips, Leiter, Kurve); die Signature (Push/Scroll DURCH die Daten auf ein Hero-Metric) wird ein vertikaler Fluss von oben (Zählung) nach unten (Kurve), Landung auf "0,11 % Median".
Scene 1 (0.0–2.3s): Oben ein schmaler Chip-Streifen: E8-Schalen-Zähler "240 · 2160 · 6720 · …" ticken nacheinander (`counting-dynamic-scale` klein); Mono-Label "reine Gitterzählung".
Scene 2 (2.3–7.2s): Auf "Primzahl-Atome" (2.5s) fällt aus dem Streifen die Λ-Leiter: vertikale Ticks bei log 2, log 3, log 4, log 5 … mit Höhen = Λ(n), sequenziell (`dynamic-content-sequencing`); auf "zirkelfrei" (3.9s) keyword glow; auf "ablesen" (5.8s) rastet der Formel-Chip "Λ_geo = Λ · exakt · bis n = 20 000" ein.
Scene 3 (7.2–11.8s): Auf "Gamma-Fluss" (7.5s) zeichnet sich darunter die Fluss-Kurve (`svg-path-draw`): sie steilt an jedem Primpotenz-Slot in eine beginnende Singularität auf — ein Atom-Punkt fällt ein und fängt sie ab (drei Slots nacheinander, je: Aufsteilen → Atom → glatter Weiterlauf); auf "Promille" (9.2s) tickt der Zähler "0,11 % Median" (accent); auf "Positionen" (10.3s) rasten kleine Positions-Schlösser an den Slots ein.
Scene 4 (11.8–16.2s): Auf "Aber ehrlich" (12.0s) dimmt die Kurve leicht; der Chip "Prüfstand, nicht Generator" reveals (Serif-Zeile, keyword glow auf "Prüfstand" bei 13.2s); Mono-Subzeile "FLOW-VERIFIER-NOT-GENERATOR · autonom nur 2–4 Slots". Hold.

narrativeRole: Zeigt die Substanz hinter "Primzahlen als Schatten der Geometrie": Maß, Massen und Positionen sind aus der Geometrie erzwungen (Λ_geo = Λ; Shooting 0,11 % Median) — mit der ehrlichen Grenze FLOW-VERIFIER-NOT-GENERATOR.
keyMessage: Die Geometrie kennt Maß, Massen und Positionen der Primzahlen — als Prüfstand, nicht als Generator.

## Frame 8 — Der Korridor und die 0,53

- scene: Ein horizontaler Korridor (Band) mit exakten Rändern; ein Punkt sitzt nicht am Rand, sondern innen — Positions-Skala rastet bei 0,53 ein; kleine Drift-Pfeile Richtung Mitte (log n); Callout "Levinson-Extremum: 0,14 % Median"
- voiceover: "The state today: every mass lives in a corridor with exactly computable edges. The arithmetic does not choose the edge — it chooses an interior point, at zero point five three. An energy extremum hits it to within per mille. The open question: explain the selection inside the corridor."
- duration: 19.584s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-korridor.html
- type: feature_showcase
- persuasion: Concretization (die offene Frage als Bild) + Distillation
- beat: Fokus + gespannte Ruhe
- blueprint: compose
- focal: der Akzent-Punkt im Korridor bei Position 0,53
- roles: Korridor-Band (zwei Hairline-Ränder, full-width strip) = foreground stage · der Punkt = foreground subject (Held) · Positions-Skala 0…1 + Wert-Zähler = supporting · Rand-Labels (1/λ_max · 1/λ_min) + Levinson-Chip = supporting · Grund = background, sehr ruhig

Compose: der ruhigste Frame des Films — ein Bild, ein Punkt, eine Frage. Kern-Move: die Feint-Bewegung des Punkts (Richtung Rand, dann innerer Halt) als Verkörperung von "wählt nicht den Rand".
Scene 1 (0.0–2.9s): Fast leerer Grund, Mono-Kicker "DER STAND" reveals; auf "Korridor" (2.5s) zeichnen sich zwei horizontale Hairline-Ränder (full-width strip, y ≈ 0,42) mit dezenter Band-Füllung (`svg-path-draw`).
Scene 2 (2.9–5.7s): Auf "exakt berechenbaren Rändern" (3.2–4.3s) reveals an den Rändern die Mono-Labels "Rand = w_c − 1/λ_max" (oben) und "Rand = w_c − 1/λ_min" (unten), plus Tag "geschlossene Resolventen-Formel".
Scene 3 (5.7–11.9s): Auf "wählt nicht den Rand" (6.5–7.2s) gleitet der Akzent-Punkt herein und driftet Richtung oberer Rand — bremst — und setzt sich auf "einen inneren Punkt" (8.1–8.8s) ins Innere (smooth long-tail, die Feint-Bewegung ist die Erzählung); auf "null Komma dreiundfünfzig" (9.6–10.1s) rastet unten die Positions-Skala 0…1 ein und der Wert-Zähler tickt auf "0,534 · Median" (`counting-dynamic-scale`); kleine Drift-Pfeile (dim) deuten mit "log n" zur Mitte.
Scene 4 (11.9–15.2s): Auf "Energie-Extremum" (12.2s) reveals der Chip "Levinson-Energie-Extremum · trifft auf 0,14 % Median" (`spring-pop-entrance`, smooth); auf "Promille" (14.0s) kurzer keyword glow auf "0,14 %".
Scene 5 (15.2–19.6s): Auf "Die offene Frage" (15.5s) typt darunter die Serif-Zeile "Erkläre die Selektion im Korridor." (`discrete-text-sequence`, mit Caret); der Punkt bekommt einen einmaligen ambient glow und hält. Stillstand — nur der Punkt trägt subtle jitter (low).

narrativeRole: Verdichtet den Nachmittags-Stand des 3. August auf das eine Bild: der Positivitäts-Korridor mit exakten Rändern, die wahre Masse bei ~0,53, das Levinson-Extremum auf 0,14 % — und die neue Gestalt der offenen Frage.
keyMessage: RH ist im Fluss-Bild zu einer Selektionsfrage in einem expliziten, endlichen Korridor geworden — Punkt bei 0,53, Extremum trifft auf Promille.

## Frame 9 — Ehrlich: kein Beweis. Aber die Frage war nie so klein

- scene: Ruhige Statement-Beats: "Kein Beweis." → "Aber die Frage war nie so klein." → Abschlusskarte "Die Prime Front" mit Zeile "893 Module · maschinell geprüft · 84 Lean-Dateien"
- voiceover: "No proof of RH. This program says so itself, at every step. But the question has never been this small — and never this precise. Almost nine hundred modules, every number machine-checked. This is the Prime Front."
- duration: 15.504s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-ehrlicher-stand.html
- type: branding
- persuasion: Distillation + Callback (Linie aus Frame 1 kehrt als Motiv zurück)
- beat: Nüchterne Zuversicht
- blueprint: kinetic-type-beats (Adapt)
- focal: die Statement-Zeilen, zuletzt die Marken-Karte "Die Prime Front"
- roles: Statement-Beats (Serif, zentriert) = foreground subject · Stat-Zeile (893 Module · 84 Lean-Dateien) = supporting · dünne Akzent-Linie (Callback auf die kritische Linie aus Frame 1) = supporting-Motiv · Grund = background, leer und ruhig

Adapt: kinetic-type-beats — Statement-Beats bauen über Full-Screen-Beats zu einem Payoff; Signature (die Bewegung IST der Text-Wechsel; Beats landen einzeln) bleibt; geändert: langsames, ernstes Tempo statt Punch — jeder Beat hält, bevor der nächste kommt (velocity-matched Waterfall-Seams statt Slams).
Scene 1 (0.0–1.8s): Leerer dunkler Grund; auf "Kein Beweis." (0.1–0.8s) landet die Serif-Zeile "Kein Beweis." zentriert (Centered, ~50 %), allein. Kurzer Hold — die Leere gehört zur Aussage.
Scene 2 (1.8–5.4s): Auf "sagt dieses Programm selbst" (2.0–3.0s) reveals darunter die kleinere Zeile "— sagt dieses Programm selbst, an jeder Stelle." per-word (`dynamic-content-sequencing`, Inter).
Scene 3 (5.4–9.3s): Waterfall-Seam (Text-zu-Text, cut-catalog): Beat 2 — "Aber die Frage war nie so klein." mit "klein" im Akzent (keyword glow auf 6.7s); auf "präzise" (7.7s) hängt sich " — und nie so präzise." an (hard-cut Wort-Reveal).
Scene 4 (9.3–13.5s): Beat 3: die Statements weichen nach oben (scale-swap), eine Stat-Zeile cascadet ein: "893 Module" (Zähler tickt auf "nine hundred" bei ~9.7s) "· maschinell geprüft · 84 Lean-Dateien"; darunter zeichnet sich die dünne Akzent-Linie aus Frame 1 als Callback-Motiv (`svg-path-draw`), Nullstellen-Punkte rasten lautlos ein.
Scene 5 (13.5–15.5s): Auf "Prime Front" (14.0s) lockt die End-Karte: "Die Prime Front" (Serif, groß) über der Akzent-Linie, Mono-Subzeile "fixpoint-theory.com/prime-front". Hold bis zum Schluss — echter Exit gehört diesem letzten Frame: sanftes Settle, dann Stillstand.

narrativeRole: Die ehrliche Landung: kein RH-Claim (Programm-Disziplin), aber die dreifach verkleinerte Frage und die maschinelle Prüfbarkeit als Substanz. Endet auf der Marken-Karte der Prime Front.
keyMessage: Kein Beweis — aber eine präzise, kleine, falsifizierbare Frage, getragen von 893 maschinell geprüften Modulen (84 Lean-Dateien).

## Frame 10 — Das regionale Theorem und das kofinale Problem

- scene: Coda nach der Marken-Karte: die zertifizierte Region K zeichnet sich als umrandete Fläche, zertifizierte Zellen füllen sich Welle für Welle; ein "M ≻ 0"-Statement mit Checker-Chip rastet ein; dann zieht ein gestrichelter Korridor-Pfeil aus der Region in die Tiefe (h → ∞) — Label "kofinal?"; Abschluss als zwei trockene Statement-Zeilen
- voiceover: "Since then, the sigma chain has turned the finite question into a regional theorem: every matrix whose entry data lie in the certified region is positive definite — a proof object, checkable by a tiny program anyone can run. One construction problem remains: a predefined window sequence, cofinal, staying inside the region. The proof object is ready for audit — the RH quantifier is not."
- duration: 26.0s
- transition_in: crossfade
- status: animated
- src: compositions/frames/10-regionales-theorem.html
- type: feature_showcase
- persuasion: Distillation (der ganze Stand in einem Bild) + ehrliche Grenze (Audit ja, Quantor nein)
- beat: Ruhige Klarheit — die Coda nach der Landung
- blueprint: compose
- focal: die Region K mit den gefüllten zertifizierten Zellen und dem gestrichelten Korridor-Pfeil
- roles: Region-K-Umriss + Zellen-Füllung = foreground subject (Akt 1–2) · "M ≻ 0"-Statement + Checker-Chip = supporting-Held des Payoffs · Korridor-Pfeil mit "kofinal?"-Label = foreground subject (Akt 3) · Schluss-Statement-Zeilen = foreground subject (Akt 4) · Grund + Hairline-Chrome = background

Compose: die Coda ist ein einziges Bild mit vier Akten — Region zeichnen, Zellen zertifizieren, Korridor-Frage stellen, trocken schließen. Kern-Move: der gestrichelte Pfeil, der die Region verlässt und offen endet — die Konstruktion, nicht die Behauptung, ist das offene Objekt.
Scene 1 (0.0–6.0s): Mono-Kicker "SEITHER · DIE σ-KETTE" reveals; auf "regional theorem" (~3.5s) zeichnet sich die Region K als geschlossener Umriss (`svg-path-draw`, accent-Hairline), Mono-Label "K — zertifizierte Region".
Scene 2 (6.0–13.0s): Auf "certified region" (~6.5s) füllen sich die Zellen in K wellenweise mit Akzent (`stat-bars-and-fills`-Stagger); auf "positive definite" (~8.5s) rastet das Serif-Statement "M ≻ 0 — auf ganz K" ein; auf "tiny program" (~11s) reveals der Checker-Chip "SOS-Beweisobjekt · 202-Zeilen-stdlib-Checker · 2 s" (`discrete-text-sequence`).
Scene 3 (13.0–18.5s): Auf "One construction problem" (~13s) zieht der gestrichelte Korridor-Pfeil aus dem Inneren von K über den Rand hinaus nach rechts (dash-flow, `svg-path-draw`), Achsen-Label "h → ∞"; auf "cofinal" (~15s) keyword glow auf dem Mono-Label "kofinale Fensterfolge — bleibt sie in K?".
Scene 4 (18.5–26.0s): Auf "ready for audit" (~19s) landet die Serif-Zeile "Das Beweisobjekt ist bereit fürs Audit."; auf "is not" (~21.5s) hängt sich die zweite, trockene Zeile an: "— der RH-Quantor ist es nicht." Hold; nur die Dash-Linie des Pfeils lebt subtil weiter.

narrativeRole: Die Coda vom 13. August: Die σ-Kette hat die endliche Positivitätsfrage in ein regionales Theorem verwandelt (Beweisobjekt + winziger Checker); offen bleibt genau ein Konstruktionsproblem — die vordefinierte kofinale Fensterfolge in der Region. Kein RH-Claim: Audit ja, Quantor nein.
keyMessage: Ein regionales endliches Positivitätstheorem plus ein einziges offenes kofinales Konstruktionsproblem — das Beweisobjekt ist bereit fürs Audit; der RH-Quantor ist es nicht.
