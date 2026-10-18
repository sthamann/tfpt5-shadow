# p9-forecast — der gemeinsame 5-Jahres-Power-Forecast der Kamm-Front

**P9-FORECAST-Scheibe (Strategierats-Disziplin):** BEVOR ein weiterer
Daten-Kanal analysiert wird — welcher Kanal könnte das gemeinsame TFPT-Signal
(Kamm-Frequenz `ω = 2π/ln((3/2)⁶) = 2.5827069463082895`, Amplitude
`ε = exp(−π²/ln λ) = 0.01730246011431484`) mit einem realistischen
5-Jahres-Programm überhaupt sehen (80-%-Power-Gate)?

> **Firewall:** Reiner Forecast. Es werden **keine** Daten analysiert; nichts
> hier ist Evidenz für oder gegen TFPT. Alle Kanal-Semantiken erben die
> Geschwister-Firewalls (surface / horizon-residual / universal-DSI / bridge):
> selbst eine künftige Detektion in einem einzelnen Kanal wäre eine
> Universal-DSI-Koinzidenz, keine TFPT-Bestätigung, bis sie in ≥ 2
> unabhängigen Welten repliziert. Nichts wird nach `[E]`/`\veri{}` gehoben.

Prereg (eingefroren **vor** jedem Monte-Carlo-Lauf):
[`hypotheses/p9_forecast_v1.yaml`](hypotheses/p9_forecast_v1.yaml).
GO-Empfehlung als **eingefrorene Prereg v1** (2026-08-04, vor dem erwarteten
Vela-Glitch-Fenster 2026/27 — kein Riesen-Glitch seit 2024-04-29, Rate ~1/2,5 a):
[`hypotheses/p9_go_programmes_v1.yaml`](hypotheses/p9_go_programmes_v1.yaml).

## Run

```bash
cd experiments/p9-forecast
python tests/test_kernel_frozen.py          # Kernel-Freeze-Guard (4/4 PASS)
PYTHONPATH=src python -m p9_forecast.cli analyze --seed 0   # ~100 s
```

Deterministische Ausgabe: [`results/results.json`](results/results.json).

## Methode

Kein neuer Statistik-Erfindungsreichtum: pro Kanal wird die **existierende
Geschwister-Pipeline** (frozen Detektoren) auf synthetischen Kampagnen
betrieben, deren **Rauschmodelle an den publizierten
Injektions-/Surrogat-Kalibrierungen der Geschwister verankert** sind (C3-Gate:
jeder Anker muss ±0.20 reproduziert werden, sonst zählt der Kanal nicht fürs
Gate). Power = P(Detektion | Signal wahr, α = 0.05) via Injection-Recovery-MC
(400 Null- / 240 Signal-Läufe, Phase pro Session/Glitch frei).

**Kanal-Inventar (P9.INV)** — nur dimensionslos kalibrierbare Amplituden:
PSR (Recovery-Modulation), FRB (Raten-Modulation), GW (Echo-Amplitude relativ
A220, Transfer-Ziel = **Decke** `(2/3)⁶ = 0.0878`, nicht das 0.0173-ε — Stage 2
hat maschinell gezeigt, dass ein einzelner monotoner Ringdown den Kamm nicht
trägt), UHECR (Spektrum-Modulation in ln E), CMB (δP/P-Log-Oszillation),
LNFLUX (ln-Flux-Kurven A1/A4/A5), CRUST. **Ausgeschlossen** (ehrliche Gründe im
Prereg-YAML): A3/A3b (linear + Rohdaten fehlen), PG.05 (linear ν̇), PG.06b als
Kanal (ε₉₀ zensiert; lebt als X-RAY-Programmvariante weiter), A2 (unter SNR),
QPE (range-blind), strange-metal (Labor, kein 5-Jahres-Astroprogramm).

**Anker (C3, alle PASS):** PG.08 J1740−3015 Power@ε=0.30: Modell 0.45/0.40
(power-/rms-matched) vs publiziert 0.50; PG.06b-2019 ν-Raum: invertierte
Slow-Amplitude 1.58 µHz → Power@ε=0.55 = 0.458 vs publiziert 0.458 (ε₅₀=0.55);
RC-Validierung (φ=0-Bett des Geschwisters exakt gespiegelt): 0.958 vs 0.9375;
GW Stage 1h: Recovery@ε₉₀ = 0.907 vs 0.90; UHECR Open-Data-N: 0.225 vs 0.233.

## Ergebnis (Seed 0): Kanal × Programm × Power @ ε = 0.0173

| Kanal | Programm (5 J, konkret) | Power | Anmerkung |
|---|---|---|---|
| PSR | RADIO-NU **(SET-B)** — Vela-Trigger, 581 TOAs/Glitch, τ 0.05–1000 d = 4.07 Perioden, σ_TOA 50 µs, 2 Glitches | **0.954** | **GATE PASS**, konditional (s.u.) |
| PSR | RADIO-NU (SET-A, konservativ) | 0.063 | 0.46 @ ε=0.30 — Range-Wand behoben, Amplitude bleibt Wand |
| PSR | RADIO-PHASE (SET-B / SET-A) | 0.408 / 0.075 | Phasen-Integration verschmiert den Kamm (PG.08-Pipeline-Eigenschaft) |
| PSR | XRAY (SET-B, σ_ν=0.6 µHz, eXTP/NICER) | 0.113 | 0.64 @ ε=0.10 — Röntgen-σ_ν ist die Wand |
| FRB | BASEBAND: 200 Sessions × ~150 Bursts (M≈30 000) | 0.096 | ε₈₀=0.096 ⇒ bräuchte M≈9.3×10⁵ |
| FRB | EXTREME: 100 × ~1000 (M≈100 000) | 0.067 | ε₈₀=0.077 ⇒ M≈2.0×10⁶; Envelope-Leckage ist der physische Kern der Amplitudenwand |
| FRB | Upgrade-Detektor (Envelope-subtrahiert, Best Case) | 0.083–0.167 | Einzelsession-Wand: **67 199 Bursts in EINER Session** |
| GW | O5/A+: 6 × GW150914-Klasse (ε₉₀=0.42) + 20 laute | 0.425* | *Obergrenze (Signal = Decke 0.0878); 80 % bräuchte **18** GW150914-Klasse-Events |
| GW | 3G (ET/CE, ×10): 40 laute Ringdowns | 1.000* | **nicht** im 5-Jahres-Horizont |
| UHECR | Auger-Volldaten-Reanalyse (×10 Open Data; N=760 050) | **0.896** | **GATE PASS**; Daten existieren bereits — Analyse-Proposal, kein neues Observatorium |
| CMB | SO-Klasse (Bound₉₅ 0.023) | 0.342 | 80 % bräuchte Bound₉₅ ≤ **0.0114** |
| CMB | S4-Klasse (Bound₉₅ 0.017) | 0.512 | nicht im 5-Jahres-Horizont |
| LNFLUX | ×3 Kurven / ×10 Archiv-Reanalyse | 0.198 / 0.424 | 80 % bräuchte **×29.3** der heutigen Kurvenzahl |
| CRUST | +2 Kühl-Episoden | 0.023 | tot bei der vorhergesagten Amplitude |

**Hierarchische Kombination (P9.COMB)** — gemeinsame Likelihood
(matched-sum über standardisierte Kanalstatistiken, MC-kalibriert; realistisches
Set = PSR-SET-A + FRB-BASEBAND + GW-O5 + UHECR-FULL + CMB-SO + LNFLUX-×10):
**0.955** vs bester Einzelkanal 0.896 (Fisher-Kombination 0.964; joint-FP 0.050).
Leave-one-out: ohne UHECR 0.902, ohne GW 0.919, ohne CMB 0.941 — kein Kanal
unverzichtbar, kein LOO-Anstieg über MC-Toleranz (C4 PASS).

## VERDICT: **P9-FORECAST-GO**

Kanal-Liste: **[PSR/Vela-RADIO-NU(SET-B) 0.95, UHECR/Auger-Volldaten 0.90]**
— plus Kombination 0.955 über dem Gate ohne Abhängigkeit von einem Einzelkanal.

**Radikale Ehrlichkeit — die drei tragenden Konditionale:**

1. **PSR-GO ist konditional** auf die Long-Komponenten-Transfer-Lesart: Die
   Power 0.954 gilt nur, wenn der multiplikative Kamm auf *allen*
   Recovery-Komponenten inkl. der 2021-PuMA-Slow-Komponente (4.94 µHz @
   502.6 d) reitet — das ist die frozen Injektions-Semantik von PG.07/PG.08,
   aber die 502-d-Komponente könnte teilweise re-absorbierte ν̇-Evolution
   sein. Unter dem 2024-Kurzzeit-Envelope (SET-A) fällt dieselbe Kampagne auf
   0.063. Der Prereg-Entwurf benennt das als Named Assumption mit
   Entscheidungsregel.
2. **UHECR-GO setzt Kollaborationszugang voraus** (Volldaten oder publiziertes
   Full-Statistics-Binned-Spektrum) und ein Modell-Adequacy-Gate: die
   frozen-Knot-Smooth-Familie muss bei ×10-Statistik re-verifiziert werden.
   Phase marginalisiert (Anker mit φ=0 reproduziert 0.225 vs 0.233 publiziert).
3. **GW-Zahlen sind Obergrenzen** (Signal an der Decke `(2/3)⁶`; TFPT sagt ≤).

**PASS/FAIL:** C1 Kernel frozen PASS · C2 False-Positive-Kalibrierung PASS
(PSR-Kampagnenschwellen null-MC-kalibriert; roher p<0.05-Entscheid ist unter
Random-Walk-Rauschen antikonservativ, raw-fp bis 0.22 — als Diagnose
mitgeführt) · C3 Anker PASS (5/5) · C4 LOO PASS · Gate erreicht: **GO**.

## Grenzen

- Synthetische Betten: PSR-Rotrauschen als Phasen-Random-Walk modelliert
  (rms-matched an PG.08: J1740 200 µs/√d, Vela 106 µs/√d); reale
  Rot-Spektren können abweichen — deshalb kampagnenweise MC-Kalibrierung der
  Schwelle statt roher p-Schwellen.
- FRB-Envelope-Tilt +0.3 (Programm) / +0.2 (Anker, RC-exakt); reale Sessions
  streuen. Die Leckage-Interferenz ist der physische Grund, warum „~10⁵
  Bursts/Session" die Wand ist — mit frozen Detektor eher 10⁶ verteilt, bzw.
  67k in *einer* Session mit Envelope-Subtraktion.
- CMB/LNFLUX/CRUST als Gauß-/Interpolations-Betten auf publizierten
  Bounds/Injektionen — keine eigene Likelihood-Reanalyse.
- Kein Scorecard-Eintrag: Forecast erzeugt keine Evidenzzeile; Aufnahme erst,
  wenn eines der GO-Programme als echtes Experiment mit eigener Prereg startet.
