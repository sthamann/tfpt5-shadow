# RH-Faktenblatt 2026-09-04/05

Forschungsdokumentation. **Kein RH-Claim** in beide Richtungen. Jede Zeile ist eine sourced fact; Werte aus Dateien, nicht aus Erinnerung.

## 1. Sweep und Katalog

| Größe | Wert | Quelle |
|---|---|---|
| Claim-Grenze Sweep | Research documentation. NOT evidence for or against RH. NO RH CLAIM. | `full_tree_sweep.json:claim_boundary` |
| Katalog zum Sweep: Records | 1691 | `full_tree_sweep.json:catalog_at_sweep.n_records` |
| davon curated (kein Draft) | 728 | `catalog_at_sweep.n_curated_no_draft_flag` |
| Prefix-Zählung Sweep | experiments 1262 / rh 404 / verification 24 / `tfpt_prime_front.tex` 1 | `catalog_at_sweep.path_prefixes` |
| Website-Pfade im Katalog (Sweep) | 0 | `catalog_at_sweep.website_paths_in_catalog` |
| A1 Keyword-Hits (Docstring/Kopf) | 548; im Katalog 23; fehlend 525 | `A1.docstring_or_head_keyword_hits` / `of_those_missing` |
| A1 PRIME/HECKE-Module | 318; fehlend 295 | `A1.A1_prime_hecke_scripts` / `A1_prime_hecke_missing` |
| A2 Ledger-Zeilen (Prefix/Mention) | 606 | `A2.selected_rows_prefix_or_mention` |
| A2 Prefix PRIME / QGEO / E8 / HECKE / RH | 379 / 77 / 44 / 12 / 2 | `A2.prefix_counts` |
| A2 Marker | [E] 397, [C] 151, [O] 159, [X] 9, NO_BRACKET 142 | `A2.marker_counts_among_selected_rows` |
| A2 strikte Prefix-Zeilen PRIME/RH/WEIL/MELLIN/HECKE | 393 | `A2.strict_prefix_rows_PRIME_RH_WEIL_MELLIN_HECKE` |
| A2 [E]-Zeilen, Modul nicht im Katalog | 185; unique-Module-Liste 188 | `A2.E_rows_strict_prefix_module_not_in_catalog` / `E_missing_unique_modules` |
| A3 §1 How to read | Z. 290 | `A3.tfpt_prime_front_sections[0]` |
| A3 §2 Motivation | Z. 630 `sec:motivation` | dass. |
| A3 §3 Big picture | Z. 706 `sec:bigpicture` | dass. |
| A3 §4 Verified layer (49 Module) | Z. 988 `sec:verified` | dass. |
| A3 §5 Localization I5 | Z. 3313 `sec:i5` | dass. |
| A3 §6 Handover T95–T101 | Z. 3430 `sec:handover` | dass. |
| A3 §7 Certification T102–T125 | Z. 3537 `sec:certification` | dass. |
| A3 §8 Kill list | Z. 5498 `sec:kills` | dass. |
| A3 §9 Series balance | Z. 5583 `sec:balance` | dass. |
| A3 §10 Phase 2 T126–T199 | Z. 5680 `sec:phase2` | dass. |
| A3 §11 Closed-form parity | Z. 11441 `sec:theory` | dass. |
| A3 §12 Operator/keystone | Z. 11796 `sec:frontier` | dass. |
| A3 §13 Status | Z. 23239 `sec:status` | dass. |
| A3 App Probe-Index | Z. 23725 `app:index` | dass. |
| A3 App Symbols | Z. 23946 `app:symbols` | dass. |
| A3 Programm-These | `tfpt_prime_front.tex:120-268`, `:630-880`; `rh_program.tex:59-146` | `A3.program_statement_thesis` |
| A3 P1–P7 Härte | `tfpt_prime_front.tex:4089-4235` (T112–T114) | `A3.P1_P7_requirements` |
| A3 λ* (v540) vs λ_* | `tfpt_prime_front.tex:1130-1131`; L* `rh_program.tex:733-787` | `A3.Terminal_Lstar_lambdastar` |
| A4 Website-Treffer | 9 Dateien/Globs; narrates_RH_program true | `A4.website_files_matching` |
| A5 Lean außerhalb `rh/` | 121 Dateien, Root `experiments/lean4-carrier-rigidity/` | `A5.lean_outside_rh_count` |
| A5 RH-relevante Lean | `DenseWeilCore.lean`, `WeilDictionary.lean` | `A5.rh_relevant_lean` |
| A6 gelöschte Matches | 0 | `A6.deleted_matching_user_command` |
| A6 Commit-Grep RH/riemann/weil/prime-front | 694 | `A6.commit_grep_count_RH_riemann_weil_prime_front` |
| A7 Codex-Outputs | unlesbar (macOS TCC) | `A7.readable=false` |
| part_8 nach Sweep | 322 Records; 295 verification / 25 documentation / 48 formalization | `part_8` |
| part_8 Build | 2013 Records, 1050 curated, 963 drafts; vorher 728 | `part_8.build` |
| B2 [E]-Claims | 11 Einträge | `B2_E_claims` |
| B2 v1017 Marker-Spannung | Paper [E] Z. 359; Website „Numerical/certified“ | `B2_E_claims` + `v1017` Docstring Z. 26–27 |
| B3 Overlooked | 10 Kandidaten | `B3_overlooked_candidates` |

**Live-Katalog** (`rh/catalog/stats.json`, `inventory_generated=2026-09-04`; Paths-Report-Meta `2026-09-05`):

| Größe | Wert | Quelle |
|---|---|---|
| n_records | 2039 | `stats.json:n_records` |
| Fragmente / Drafts / needs_review | 1065 / 974 / 974 | `n_from_fragments` / `n_from_drafts` |
| Fragment-Dateien | 18 (`part_15` fehlt) | `n_fragment_files` |
| INVENTORY-Einträge | 668 | `n_inventory_entries` |
| reusable / killed / load_bearing_open | 1064 / 399 / 119 | `stats.json` |
| certified_or_proved | 584 | `certified_or_proved` |
| Confidence high/med/low | 629 / 426 / 984 | `by_confidence` |
| Outcome CERTIFIED/KILLED/MEASURED/OPEN/PROVED/INCONCLUSIVE/SEALED/RESTATED | 469 / 399 / 408 / 415 / 115 / 122 / 63 / 48 | `by_outcome` |
| Kind ATTACK/FOUNDATION/CONTROL/DOCUMENTATION/FORMALIZATION | 1099 / 261 / 251 / 189 / 110 | `by_kind` |
| Familie WEIL / SCREW / LATTICE_E8 / OPERATOR / RHP | 821 / 228 / 165 / 129 / 106 | `by_family` |
| Validation-Verletzungen | 0 | `n_validation_violations` |

**Fragmente `len(part_*.json)`:** 1=112, 2=112, 3=112, 4=112, 5=112, 6=107, 7=61, 8=322, 9=2, 10–14+16–18 je 1, 19=5; Summe 1065. `part_15.json` existiert nicht.

**Paths-Report T1–T7** (`paths_report.json`; curated 1065, drafts ignoriert 974):

| Größe | Wert | Quelle |
|---|---|---|
| T1 Familien | 19 | `T1_matrix` Länge |
| T1 WEIL curated / all | 397 / 821 | `T1_matrix[0]` |
| T1 SCREW | 226 / 228 | dass. |
| T1 LEAN / EXPLICIT / OPERATOR / RHP / TOEPLITZ / MELLIN / LATTICE | 50 / 28 / 69 / 94 / 22 / 18 / 44 | `T1_matrix` |
| T1 ADELIC / ARAKELOV / CM / DYNAMICS / SELBERG / EVENTLOG / SIEVE / CERT / EXT / OTHER | 9 / 1 / 1 / 6 / 4 / 4 / 28 / 37 / 6 / 21 | dass. |
| T2 killed_total | 317 | `T2_kill_roots.killed_total` |
| T2 Root-Cluster | structural mismatch 91; lossy constant 55; no bridge 48; world-blind 38; RH-near circular 21; restatement 15; fit/alias 9; float64 9; no source-pure 7; cone/sign 7; no cofinal 6; bound>margin 4; compact vs primes 3; Hankel not Toeplitz 1; factor-2 1; renamed 1; unclustered 1 | `T2_kill_roots.by_recurring_root` |
| T3 eligible / ranked / v535–v954 [E]-orphans | 64 / 12 / 100 | `T3_orphan_foundations` |
| T4 Familien / beobachtete Paare / never-tried / early×late | 19 / 72 / 99 / 45 | `T4_never_tried` |
| T5 Widersprüche | 0 | `T5_contradictions` |
| T6 surviving / nearest | 0 / 6; Verdict: no independent path | `T6_candidate_paths` |
| T7 classical bricks / RH-strength holes | 3 / 6 | `T7_formalization_targets` |
| Round-Bänder curated | v535–v600:47; v601–v700:55; v701–v800:69; v801–v900:72; v901–v954:50; v1017–v1019:3; r600+ probes:60 | `meta.round_bands` |

**Diff** (`paths_report_diff.json`): alt 1701/728/973 → neu 2039/1065/974. T2 killed 179→317; T2 clusters 20→17; T3 eligible 80→64; T3 ranked 5→12; T4 115→99; T5 26→0; T6 misses 3→6.

**Orphan-Triage** (`orphan_triage.md`; 101 nicht 102): FINITE_WINDOW 69 / FORMAL 29 / STRUCTURAL 3. LEVER 0 / INPUT 67 / DEAD_END 34. Feeds: LSTAR 11; QN_TERMINAL 8; I5_WEIL_WALL 49; WEIGHT4_GL1 10; HALFDENSITY 12; PRIME_PHASE 18; SCALE_LAW 22; NONE 8 — alle LEVER=0. DEAD_END-Gründe: Fenster 13; failed 10; restatement 5; superseded 3; obstruction 2; lossy 1.

**LLM-Konsistenz** (`llm_consistency.json`): n_records 1690; n_disagreements 134 (kind 133, family 2, outcome 2, failure_class 1); n_errors 0; Modell `gpt-4.1-nano`.

## 2. Früher Stack (v535–v541, v1017, Paper)

| Größe | Wert | Quelle |
|---|---|---|
| dim_Q V | 7 = 5 E4-Kopien (Level 1,2,4,8,16) + 2 f8-Kopien | `v535_hecke_from_geometry.py:26-27,733-795` |
| f8 | η(2τ)⁴η(4τ)⁴; a_p(3,5,7)=(−4,−2,24) | `v535:597-602`; LMFDB 8.4.a.a in `geometry_audit.md:140-148` |
| a_p-Regel | a_p = −c(p)/8 (Census-Koeffizient) | `prime_story.md:28` |
| Kneser | ν_p = aI + b T_p, a_p = b − σ₃(p) | `v535:6-29`; `prime_story.md:14` |
| Shimura-Zeuge g | θ₂(q²)² θ₃(q²) θ₄ θ₄(q²); Sh(g)=−8 f8; U₄(g)=0 | `v537:7-30` |
| Monoid | 70 Objekte Gewicht 5/2; Unique −8-Scale | `v537:7-16` |
| Waldspurger R(d) | 23.1873585645…, Spread ≤ 10⁻¹², 10 Diskriminanten d≡1 mod 8 | `v537:33-38` |
| v540 λ* | FE-kovarianter Gap; C_L3 = {n≡6 mod 8}; Farkas-Zeuge | `v540:55-87` |
| v540 Theta | θ₂(q²)² θ₃(q) θ₃(q²)²; Eisenstein T(p²)-EW 1+p³ | `v540:16-20` |
| v540 FE-Zentrum | 5/4; Plus-Balance s=1, Off-Centre 1/4 | `v540:47-54` |
| E8-Eisenstein | L=ζ(s)ζ(s−3); Nullmenge {ρ}∪{ρ+3}; RH-neutral (Identität) | `prime_story.md:32`; `v535:41-48` |
| v1017 Ledger-Text | Numerical/certified (G1/G3/A3); Identity für A2 | `v1017:26-27` |
| Terminal q_N | D_N>0 ⇔ q_N<1; t^*=q_N; 5/7 aus min 1.4278 (Marge 0.028) | `rh_program.tex:313-324` |
| Firewall-Tabelle | main p_max=184; scramble/epstein/smooth 21/25/27 | `rh_program.tex:327-333` |
| q-Census 42 Sprossen | min/med/max 0.0015/0.4188/0.9805; Marge 0.0139 | `rh_program.tex:336-340` |
| L* | ∫p²dν < ∫p²dμ, deg p < N_w; ⇔ λ_max(E_{N_w})<1; [O] | `rh_program.tex:774-791` |
| Frame-Zeugen | 1.25×10⁻¹³ vs 1.25×10² | `rh_program.tex:770-771` |

## 3. Sonden (Result-JSONs)

### Kneser-Gruppoid (`kneser_groupoid_halfdensity_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Vertrag / Verdict | `KNESER.GROUPOID.HALFDENSITY.01` / KILLED(K1) | `contract` / `verdict` |
| Testprimzahlen | 3, 5, 7 | `tested_primes` |
| SPEC_SHA | 212aaef89bc61621…4db93bb9 | `spec_sha256` |
| p=3 Grade | ALL_KNESER 1120; AFFINE 448; HECKE 672; TYPE_A 1120 | `prime_results[p=3].channels.*.degree_per_mark` |
| p=5 Grade | 19656 / 4032 / 15624 / 7560 / TYPE_B 12096 | `prime_results[p=5]` |
| p=7 Grade | 137600 / 11008 / 126592 / 13760 / TYPE_B 123840 | `prime_results[p=7]` |
| Δ auf allen markierten Kanälen | identisch 1 | `delta_min`/`delta_max`; `triggered_criteria` |
| C1 unmarked E8 Fasern | p=3:1120; p=5:19656; p=7:137600 | `controls.C1_unmarked_E8` |
| C2 Baum Δ | 1/3, 1/5, 1/7 (Halbdichte p^{−1/2}) | `controls.C2_nonunimodular_tree` |
| C3 Scramble | pass (Fasern invariant) | `controls.C3_scrambled_marks` |

### Parabel-Detlinie (`parabolic_detline2_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Vertrag / Verdict | `PRIME.PARABOLIC.DETLINE.02` / KILLED_K2 | `contract` / `verdict` |
| L1 Formel | 2 q^{−m/2}/(1−q^{−m}) vs Connes 2 q^{−m/2} | `L1` |
| L2 Zylinder-Limit | q^{m/2}+q^{−m/2}, unabhängig von N | `L2.orthonormal_limit` |
| L4 Fixed-Point-Summe | −2.1049002297579167… | `L4.fixed_point_total` |
| L4 Differenz Fixed−Weil | −0.8640350619049233… | `L4.difference_fixed_minus_weil` |
| L4 Weil-Total (Differenz) | −1.2408651678529934… | aus `fixed_point_total − difference` |
| Controls / Runtime / dps | pass; 0.0010 s; mp_dps 60 | `controls_pass` / `runtime_s` / `mp_dps` |
| SPEC_SHA | f8eb970aa50051c1…31cfefd | `spec_sha` |

### Positive-Kegel-Blindheit (`positive_cone_blindness_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Lemma-Verdict | LEMMA_PROVED | `lemma.verdict` / `T5.verdict` |
| t* | 9/2 | `T2.finite_window.scaling_threshold_t_star` |
| λ_min unter/über | +1 (t=4, PD) / −1 (t=5, indefinit) | `finite_window.below/above.lambda_min` |
| Blind-Hash | c7ecbcf69349edac (identisch) | `blind_data_hash_*` |
| Waldspurger-Block | positive_functional 3; Source 2,3,5 | `T2.waldspurger_block` |
| Farkas | target [1,−1]; library [1,3,2]; witness_on_target −1; Klasse n≡6 mod 8 | `T2` Farkas-Felder |
| T3 Klassen | 8× BLIND + 3× METRIC (Loewner, Chuk, L*) | `T3` |
| T5 remaining | L* metrisch; Operator+EF-Brücke | `T5.remaining_targets` |

### Clock-Kombination (`clock_combination_spectrum_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Combos / Checks / Survivors | 63 / 73/73 / 0 | `combination_count` / `checks` / `survived_bc_candidates` |
| Verdict | NO_SURVIVED_BC_CANDIDATE | `verdict` |
| Resummiert Ränge N=3,4,5,6,8,16,30,240 | 2,2,3,3,4,6,10,52 | `compiler_necessity.md:118`; `resummed_clocks` |
| Koide Fixpunkte / Multiplikatoren | 2, 5; 64/729 und 729/64; 6 log(3/2) | `koide_mobius_flow` |
| Modular v446 | 28 Eigenwert-Verhältnisse; 0 ganzzahlig; PSLQ unbestätigt | `modular_clock_v446` |
| Scale-Gitter | formal Rang 3: α⁻¹, L₀, log(8π) | `scale_lattice` |

### Archimedische π-Konformität (`archimedean_pi_conformity_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Vertrag / Verdict | `ARCHIMEDEAN.PI.CONFORMITY.01` / MEASURED | `contract` / `verdict` |
| λ_min L=0.50/0.65/0.80 | 9.3365673259644e-7 / 3.9470557473553e-11 / 1.6429649175891e-17 | `windows` / `pi_prime_correlations.md:122-125` |
| Zertifikat L=0.8 | 1.0276885835726054e-17 | `certificate_context.certified_constant` |
| Γ-Kreuzungen ε* | 8.4031787651584e-6 / 2.1019189641437e-10 / 7.0083853843393e-17 | `pi_prime_correlations.md:135-137` |
| π-Term/Marge | 10^{6.09} / 10^{10.46} / 10^{16.84} | `pi_prime_correlations.md:141` |
| Scramble λ_min | 1.5927292634053e-5 / −0.42659006784434 / −0.30343508319531 | `windows` scramble |
| Ziffern r / p | −0.00300484 / 0.33; Blöcke r=−0.00262089 p=0.406 | `digit_null_test` |
| Kontrolle 1_P vs Λ/log | r=0.998926 p=0.002 | dass. |
| Runtime | 51.7279 s | `runtime_sec` |

### Census-QSM (`census_qsm_normflow_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Vertrag / Verdict | `CENSUS.QSM.NORMFLOW.01` / CONSTRUCTED_CANONICAL_CLASSICAL | `contract` / `verdict` |
| Checks | 8/8 | `checks_passed`/`checks_total` |
| a(n) Kopf | 1,15,0,155,312,0,0,1395,820,4680,0,0,4760 | `enumeration.a_n_head` |
| Dirichlet-Koeff. | 200/200 Matches | `dirichlet_identity.coefficient_matches` |
| KMS-Checks | 15 (alle in `kms_checks`) | `kms_checks` |
| β_c | 4 | `dirichlet_identity.critical_inverse_temperature` |
| O2 Hecke-Phase | 0.507324477483 (obstructed) | `o2_hecke_obstruction.phase_mismatch` |
| RH-Delivery | A CONSTRUCTED; B BLIND; C keine Nullstellen-Kodierung | `rh_delivery` |

### Hecke-Index (`hecke_index_theorem_result.json` + `.md`)

| Größe | Wert | Quelle |
|---|---|---|
| Vertrag / Checks / Verdict | `TFPT.HECKE.INDEX.01`; 7/7; L1_PROVED_CLASSICAL + L2_KILLED(K2) + EQUALITY_HUNT=CONNES_DICHOTOMY | `verdict` / `hecke_index_theorem.md:209` |
| Fasern \|det A\| | 2→2, 3→3, 5→5, 6→6, 7→7, 9→9, 10→10 | `hecke_index_theorem.md:63-66` |
| Primzahlen ≤50 | 15/15 | `hecke_index_theorem.md:75-76` |
| Gauß-Index | p=2 und p≡1 mod 4: Index p; p≡3 mod 4: p² | `T2_index_theorem.gaussian_rank4` |
| Heat-Shifts | {0,3,12,27} (nicht log 2) | `hecke_index_theorem.md:114-116` |
| Untergruppen-Zeta | 30/30 HNF; a₈(1..10)=1,255,3280,43435,97656,836400,960800,6347715,8069620,24902280 | `hecke_index_theorem.md:134-138` |
| Torus-Cutoff | (π⁴/24) Λ⁸; nicht h(0) log Λ | `hecke_index_theorem.md:181-188` |
| SPEC_SHA | 6a48c0512e2dceb5…0287dc81 | `spec_sha256` |

### Evolve (`evolve/results/evolution_result.json`, `evolve_props_report.md`)

| Größe | Wert | Quelle |
|---|---|---|
| Seed / Vertrag | 20260904 / `PRIME.RDAGGER.PROGRAM_EVOLUTION.01` | `seed` / `contract` |
| T1 beste Konstante | 0.3312992322932612; 0/72 Verletzungen; worst ratio 0.999999999999 | `T1.best` |
| T1 Alternativ | 0.33353094534733335 (sup_d2), ebenfalls 0/72 | `T1.candidates` |
| T3 k=5…16 | alle 12 Fenster gut; k=5 Marge 2.21356e-2 … k=16 1.15514e-6 | `evolve_props_report.md:141-150` |
| T3 Null | 1000-fache Permutation ebenfalls 100 % | `evolve_props_report.md:152-153` |
| API | Schätzung $0.001723; spent $0 | `api.estimate.total_usd` / `spent_usd` |
| Runtime | 0.6301 s (Report 0.633 s); 92 Programme | `runtime_seconds`; `evolve_props_report.md:187` |
| Klassifikation | T1 CLASSICAL-PROVABLE (nicht bewiesen); T2 INCONCLUSIVE; T3 RH-HARD; 3→2 offene Props | `evolve_props_report.md:83-178` |

### Heat-Gabor (`heat_gabor_restatement_probe_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Verdict | RESTATED | `verdict` |
| a=1/4 exact / PNT / slack | 6.28702320666 / 8.26546270824 / 7.38905609893 | `prime_budget`; `external_proposals_heat_nb.md:65` |
| a=1/8 | 17.0801282518 / 19.2721163788 / 16.9188286786 | dass. |
| a=1/16 | 70.6972910416 / 74.0864677617 / 54.5981500331 | dass. |
| a=1/32 | 428.739250714 / 774.181610229 / 286.246763854 | dass. |
| a=1/4 Quelle (Pole/Prim/Arch) | 41.4368850548 / 31.5184602662 / −9.91842478862; Rest 2.70e-12 | `external_proposals_heat_nb.md:75-77` |
| Digamma vs Vasyunin | max 2.64×10⁻⁸² (80 Stellen) | `external_proposals_heat_nb.md:30`; NB-JSON `2.63554948581e-82` |

### NB-dyadisch (`nb_dyadic_capture_probe_result.json`)

| Größe | Wert | Quelle |
|---|---|---|
| Verdict | MEASURED | `verdict` |
| N=8 E_N / η_k / kη_k / cond | 0.024244525307 / 0.0639854156 / 0.1919562468 / 5.37e1 | `rows`; `external_proposals_heat_nb.md:99` |
| N=16 | 0.017936267020 / 0.1007401959 / 0.4029607835 / 3.08e2 | dass. |
| N=32 | 0.014077011415 / 0.1200395213 / 0.6001976066 / 1.74e3 | dass. |
| N=64 | 0.011392474680 / 0.1152003874 / 0.6912023245 / 8.08e3 | dass. |
| N=128 | 0.009670345448 / 0.1252601699 / 0.8768211893 / 3.82e4 | dass. |
| N=256 | 0.008242256028 / 0.0906767057 / 0.7254136455 / 1.67e5 | dass. |
| N=512 | 0.007393375337 / 0.1104454847 / 0.9940093619 / 7.24e5 | dass. |
| C_fit vs C_BD | 0.046249285476 vs 0.046191417932 (Faktor 1.001253) | `rate_comparison` / `burnol` |

## 4. Analysen

### Prime-Story (`prime_story.md`)

8-Schritt-Anatomie [E]: P1/P2→E8→θ=E4, N(n)=240σ₃(n)→μ4/χ₋₄→Kneser/Hecke→7-dim Census→Shimura→RTF. Primzahl erstmals als Hecke-Index p (`v535:6-20`). Event-Log-Metapher: 5 statische Folgen. r635 LEAD_PARTIAL, r636 LEAD_LAW_NULL. g_car: 0 Vorkommen in v535/v536 (`prime_story.md:48`). Q4: 8 ungetestete Paare, je 0 shared curated records.

### Event-Log (`event_log_function.md`)

| Größe | Wert | Quelle |
|---|---|---|
| TeX-Hits / Dateien | 3765 in 11/11 | Z. 9–10 |
| v.py-Hits / Dateien | 25046 in 901/984 | Z. 10 |
| 11 Mechanismen Q2 | Translation, Resummed, μ4, Koide, F_transfer, Modular, Wick, Scale-Gitter, 4D, QCA, Lorentz | Tabelle Q2 |
| Absence | foliation/3+1/emergent time/scaling flow/ideles/Q*₊ = 0 | Z. 53–55 |
| log p | 1 Treffer (gescheiterter Surrogat) | Z. 55 |
| unitar* | 21 TeX / 42 Skripte | Z. 56 |
| TeX-Konzentration | 2357/3765 in `tfpt_3` + `tfpt_research_contracts` | Z. 28–29 |
| Q4 Klassifikationen | PNT THEOREM; von Koch RH_EQUIVALENT; Q-Unabhängigkeit THEOREM; 4D-Privileg FALSE | Q4 |

### Compiler-Notwendigkeit (`compiler_necessity.md`)

A1: I(n)=c log n [T]; FTA-Isomorphismus. A3 v740: 1 = p⁻¹ (KMS unmöglich, `v740:31-47`). v740 lokale Gram 55296 Monome. Clock-Probe 73/73, 63 Combos, 0 Survivor. B-Tabelle: K1/K2/K3 wie Clock-JSON. C-Tabelle: nur Census-QSM-Vertrag „worth one frozen contract“.

### π–Prim (`pi_prime_correlations.md`)

L(1,χ₋₄)=π/4 nicht im Korpus ausgerechnet. c₃=1/(8π)=1/(32 L(1,χ₋₄)) als **Koinzidenz**. B1 THEOREM; B2 RH_EQUIVALENT (volle Weil; L* nur Fenster); B5 FALSE/UNTESTABLE (π-Ziffern).

### Positivitäts-Ursprung (`positivity_origin_search.md`)

16+ Strukturen (Tabelle P1 Zeilen 1–20). Spektralzeta 240(8π²)^{−s} ζ(s)ζ(s−3). Schalen (n,N)=(1,240),(2,2160),(3,6720),(4,17520),(5,30240). r129: Θ+Θ*=I ⇒ W≥1/4; Commit `d58cb7e3`; failure_class NOT_APPLICABLE. Wortzählung self-dual/Poisson/adele/idele/Tate: origin 0/0/0/0/0; tfpt_1 4/0/0/0/2; prime_front 14/1/0/0/5. Origin-Baum: `:85,:534,:642,:669,:984,:1026,:1101,:1166,:1455,:1504,:1632`.

### Bridge 2 direkt / Objekt (`bridge2_direct_search.md`, `bridge2_object_search.md`)

Solomon r=8: ζ(s)…ζ(s−7); Z[i]-Modul 200/200. 12-Zeilen-Literatur (Connes DOI 10.1007/s000290050042 … Bost–Connes). Yoshida 2L≤log 2 ⇒ L≤0.34657359. Chuk Q≥8.9e-18, ≤2.27e-17 auf [−0.8,0.8]; n=2,3,4 im Fenster; Faktor 2.3 vs klassisch. Platt–Trudgian H=3 000 175 332 800. W1: v643 11/11. W2: c₀=0.306. W3/W4: Wand / Transfer [O]. Semidefinite Arch−Prim-Zerlegung **falsch** (2 cos(aξ) wechselt Vorzeichen). Compact support ≠ Höhen-Cutoff. Status Bridge 2: OPEN.

### Geometrie-Audit (`geometry_audit.md`, Stand 2026-09-04)

| Größe | Wert | Quelle |
|---|---|---|
| G1 zero-attempt (damals) | 182 | `geometry_audit.md:22` |
| G1 live (`gaps_report.json`) | 205 | `gaps_report.json` G1-Länge |
| G2–G6 live | 9 / 262 / 30 / 14 / 29 | dass. |
| Quasikristall | NEUTRAL; Kurasov–Sarnak: Guinand **kein** FQ; Corpus 10 Dateien / 22 Zeilen | B1 |
| Quantum-Graph | NO-GO connected noncancelling; Kuipers–Hummel–Richter arXiv:1307.6055; Corpus 0 | B2 |
| CY3 / f8 | LMFDB 8.4.a.a; Hulek–Verrill arXiv:math/0504070; COVERED/NEUTRAL | B3 |
| K3 | H² ≅ 3U⊕2E₈(−1), Signatur (3,19) | B4 |
| Lapidus–Maier | DOI 10.1112/jlms/52.1.15; NEUTRAL (RESTATEMENT) | B6 |
| Deninger | arXiv:2301.11643, 2410.20758; COVERED if constructed | B4 |
| Möbius-Hits | 393 (meist Sieb) | B5 |

### Externe Vorschläge / Evolve-Report

Siehe Heat-Gabor- und NB-Tabellen; Evolve-Abschnitt. Heat: Verdict A RESTATED. NB: Verdict B MEASURED; η_k≥c/k CONJECTURE.

## 5. Lean

| Größe | Wert | Quelle |
|---|---|---|
| Modul `SelectedArchErrorQuadraticRateClassical.lean` | 238 Zeilen | `INVENTORY.json` r475-repair status |
| `intervalIntegral_affineInterpolation_error_le_one_twelfth` | bewiesen | `SelectedArchErrorQuadraticRateClassical.lean:117` |
| `endpointKink_cell_integral_defect` | −θ(1−θ)/2 | `:163` |
| `meshSix_endpointCoefficient_exceeds_archRateConst` | 4(1+1/64)²=4.1259765625 < 6 | `:214-217` |
| Falsifikation | 8.0283458222 > 4.1259765625; auch 4.4488, 7.13–7.24 | `INVENTORY` r475-repair; `README.md:109` |
| Gemessene Verhältnisse | 3.9893 (k=5–8), 3.8466 (k=9–12) | `Open.lean:499`; `InnerBridges.lean:464` |
| Halving-Faktor | 0.2411 | STATE/INVENTORY-Kontext r475 (O(Δ²) nicht widerlegt) |
| Grid-Identität | `selectedArchGridEndpoint` vs `selectedArchError` 2.3e-25 | `INVENTORY` r475-repair |
| `SelectedArchErrorQuadraticRateExists` | ∃C-Interface | `:52` |
| `SelectedArchWeightedInterpolationEstimate` | OPEN | `:60` |
| `selectedArchErrorQuadraticRateExists_of_weightedInterpolationEstimate` | bewiesen bedingt | `:76` |
| `selectedArchError_tendsto_zero_of_rateExists` | bewiesen | `:88` |
| `selectedArchErrorQuadraticRateExists_of_fixed` | bewiesen | `:104` |
| `selectedArchErrorQuadraticRate_holds` | bedingt | `:222` |
| lake build | 3578 jobs; 5 intentionale sorries | `rh/lean/README.md:161` |
| 5 geschützte sorries | `ExternalBridges.lean:15706`; `Source.lean:1008`; `Canonical.lean:264,273,396` | Dateizeilen `sorry` |
| FREQ-Props | `frequently_selected_augDualResolvent_ge_half` :294; `weil_nonneg_of_frequently_plain` :358; `internal_weil_nonneg_of_frequently_selected_of_A_cap` :458 | `FrequentlySelected.lean` |
| Bewiesene Sätze | `selected_polynomial_nonneg_of_cone` :488; `frequently_of_pos_lower_density` :535 | dass. |
| Sorry-Census | 5 (r376→r638L) | `README.md:10-57` |
| Audit-Layer | `#print axioms` mit/ohne sorryAx | `Audit.lean` + `README.md:295-333` |

## 6. Richter-Verdikte (Opus / Canvas)

| Größe | Wert | Quelle |
|---|---|---|
| J1a Waldspurger × Census | CATEGORY_ERROR (F2 fail; direkte Summe) | Canvas `RH-research-audit.canvas.tsx:190-194`; L3-Urteil 2026-09-04 |
| J1b Cohen-Keime | CLASSICAL_NEUTRAL | Canvas :196-199 |
| J1c Rankin–Selberg | CLASSICAL_NEUTRAL | Canvas :201-205 |
| J2 Siegel–Weil | GENUINE_BUT_BLOCKED | Canvas :207-211 |
| J3 Adele × Siegel–Weil | CLASSICAL_NEUTRAL (Restatement) | L3-Urteil |
| J4 Event-Log-Test | wohlgestellt, bereits entschieden (kein autonomer Generator) | L3-Urteil; Canvas :220-223 OPEN/nicht wohlgestellt für STAGE1-Vertrag |
| Positive-Kegel | LEMMA_PROVED | Canvas :214-217 |

## 7. Infrastruktur und Repo

| Größe | Wert | Quelle |
|---|---|---|
| Viewer-Stack | sigma 3.0.3, graphology, FA2 + noverlap, seed 32 | `rh/catalog/viewer/package.json`; `viewer/README.md:35` |
| Erstes Frame / Refresh | 73–88 ms / 6–12 ms | Canvas `viewerPerfRows` :667-668 |
| Payload | 5.0 → 0.82 MB Kern | Canvas :669 |
| Tagesbilanz-Viewer | ≈80 ms, ≥80 FPS | `_newest/RH_Tagesbilanz_2026-09-04.md:8` |
| Hover 0.1 ms / Click 11 ms / Bundle 319 kB / 93.6 kB gzip / lazy 3.0 MB / vorher 2.7 FPS | nicht als Messdatei im Repo | — |
| Karte Progression | 158→190→233→253→271→**285** Knoten; Kanten 521→629→748→797→838→**882** | Commit-Messages `f89c22dd`, `106f27b0`; live `rh_concept_map.json` |
| Katalog-Progression | 728→1050 curated; Records 2013→…→**2039** | Sweep `part_8.build`; `stats.json` |
| Commit `f89c22dd` | 294 Dateien, +319126 / −477 | `git show --stat` |
| Commit `106f27b0` | 27 Dateien, +4098 / −877; Karte 253→271 | `git log` / `--stat` |
| HEAD-4 | `106f27b0`, `f89c22dd`, `936288a6`, `01789659` | `git log --oneline -4` |
| INVENTORY | 668 Einträge, davon pin=true **555**; generated 2026-09-05 | `INVENTORY.json` |
| vN-Skripte / Registry | 1019 Dateien / 1018 Registry-Zeilen | `ls verification/v*.py`; `script_registry.csv` |
| Ledger-Zeilen | 1184 | `status_ledger.csv` |
| Manifest | 1109 Zeilen | `manifest.sha256` |
| Gates (Soll-Text) | AUDIT OK; RH SUITE ALL CHECKS PASSED | `docs/VERIFICATION.md`; `run_rh.py:689` |

## Offene Aussagen (exakt)

- L* / `PRIME.LSTAR.SUBORDINATION.01` [O]: ∫p²dν<∫p²dμ auf deg p<N_w (`rh_program.tex:774-791`).
- v540 λ* auf C_L3={n≡6 mod 8} bleibt benannte Grenze (`v540:83-87`).
- Gewicht-4 → GL(1) offen (`v535:41-48`).
- Bridge 2 OPEN: kein Markov/OS-Generator mit Zeta-Ordinaten (`bridge2_*.md`).
- `SelectedArchWeightedInterpolationEstimate` OPEN; feste `archRateConst` FALSIFIED.
- T2/T3 FREQ: Jackson liefert nicht die skalare Kanaltoleranz; T3 RH-HARD.
- η_k≥c/k unbewiesene Block-Vermutung (`external_proposals_heat_nb.md:34`).
- W2 formal/Mosco offen; uniform W3 = Wand; W4 Transfer [O].
- Kein physischer 4D-OS-Raum mit ρ_n für alle n (`hecke_index_theorem.md:30-42`).
- Census-QSM: Euler-Seite konstruiert, Positivität BLIND (`rh_delivery`).
- Event-Log: kein autonomer Skalengenerator mit Perioden log p (`event_log_function.md` Q5/Q6).
- G1-Restform: stochastische Skalenhalbgruppe auf Connes-Kokern / Deninger–Arakelov (`geometry_audit.md:238-245`).

## Korrekturen an eigenen Annahmen

- Semidefinite Arch-minus-Prim-Zerlegung ist **falsch** (`bridge2_object_search.md:90-100`).
- Kompakter Träger ≠ Höhen-Cutoff; Platt–Trudgian schneidet L²[-L,L] nicht ab (`bridge2_object_search.md:118-137`).
- Torus-Cutoff ist Λ⁸ (Vol B₈=π⁴/24), nicht log Λ (`hecke_index_theorem.md:179-195`).
- r129 gilt nur interior Θ+Θ*=I, nicht für selbstduales Haar (`positivity_origin_search.md:72-78`).
- g_car=5 hat **keinen** bewiesenen Mechanismus zu den fünf E4-Leveln (`prime_story.md:48`).
- „Positivität aus Axiom“ wird **nicht** behauptet (`full_tree_sweep.json` B3 rank 10; `positivity_origin_search.md:39-42`).
- π-„17 Stellen“ ist Eigenwert-Marge 1.64×10⁻¹⁷, nicht 17 korrekte Ziffern von π (`archimedean_pi_conformity_result.json`; `pi_prime_correlations.md:168-171`).
- Orphan-Zahl 101, nicht 102 (`orphan_triage.md:5`).
- A1-PRIME-Module 318, nicht „~304“ (`A1.A1_prime_hecke_scripts`).
- Untracked 74, nicht 171 (Git-Stand der Richter-Runde; Arbeitsbaum driftet).
- FREQ-Props an `FrequentlySelected.lean:294/358/458` (nicht frei verschiebbare Zeilen); Sätze :488/:535.
- `axiom`-Stringhits ≠ Deklarationen: 0 `axiom`-Decls in `rh/lean/RH` (Audit: nur sorryAx/propext/choice/Quot).
- v1017 ist im Paper [E], Ledger/Website Numerical/certified (`B2` + `v1017:26`).
- Heat/NB-Dateinamen tragen `_probe_result.json`.
- Karte/Katalog sind weitergewachsen: 285/882 bzw. 2039 Records (live, nicht der Sweep-Schnappschuss 1691/728).
