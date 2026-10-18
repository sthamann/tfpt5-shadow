# Prime Front explainer video (English, 2026-08)

HyperFrames project for the Prime Front explainer film
(3:05 min, 1920×1080, H.264 + AAC). Embedded on the website at
`/prime-front` (files in `website/public/prime-front/`).

Originally produced in German (de-DE-ConradNeural); switched to English on
2026-08-03 because the website is English. The frame windows stay frozen to
the original narration durations — the English narration was rate-fitted into
the same windows, so all frame timings, transitions and shot sequences are
unchanged. `SCRIPT.de.md` keeps the German script (source of the `de.vtt`
translation track).

Refreshed 2026-08-10: the stale module-count line of frame 9 updated to the
current suite state ("Almost nine hundred modules"; on-screen stat
"893 modules · machine-checked · 84 Lean files"), full TTS + captions + render
re-run through the frozen frame windows (still 2:39.1); the pre-existing
beat-1/beat-2 palimpsest layering in frame 9 is now annotated
`data-layout-allow-overlap` so `hyperframes check` passes clean (0 errors).
All other narration, timings and visuals unchanged.

Extended 2026-08-13: new closing frame 10 ("Das regionale Theorem und das
kofinale Problem", 26.0 s window, audio 25.2 s at rate +0%) — the σ-chain coda:
the regional finite positivity theorem (M ≻ 0 for every matrix with entry data
in the certified region K; 151/151 cells, SOS proof object, 202-line stdlib
checker) and the single open cofinal construction problem, closing on "The
proof object is ready for audit — the RH quantifier is not." Frames 1–9 keep
their frozen windows (full TTS re-run, all lines rate +0%); total now 3:05.1
(185.12 s), frame 10 starts at 159.12 s. `hyperframes check` clean (0 errors).

## Content (10 frames, ~185 s)

1. The music of the primes (RH, critical line) — 0:00
2. Geometry first (E₈ → Θ=E₄ → Hecke → ζ, v625) — 0:17
3. The window matrix is a Weil operator (W1 theorem, v643, erratum) — 0:31
4. Detector & falsifier (Ramanujan passes, Epstein breaks 0.803; matched filter) — 0:46
5. Two surface theorems (det S > 0 on 67/67, ×634; T-B 60/70) — 1:10
6. Ihara blueprint: the missing engine Z1 (Hilbert–Pólya) — 1:29
7. The measure from the geometry (Λ_geo = Λ; Γ flow forces masses 0.11%) — 1:48
8. The corridor and the 0.53 (Levinson 0.14%; "Explain the selection") — 2:04
9. Honest: no proof of RH — 893 modules, 84 Lean files — 2:24
10. Coda: the regional theorem & the open cofinal problem — 2:39

Source: `big_picture_2026-08-02_de.tex` (arcs D–G, erratum/theorem, climbing
round, door handle, the two August-3 chapters); frame 10 from the σ-chain
chapter 32 of `website/app/prime-front/page.tsx` (freeze rounds 73–75 + the
package round); terminology checked against
`website/app/prime-front/page.tsx`. No RH claim — the program's honesty
discipline holds in the film too.

## Pipeline (faceless-explainer skill)

- `STORYBOARD.md` — 10 frames with time-coded shot sequences (VO-paced)
- `SCRIPT.md` — English narration (TTS source); `SCRIPT.de.md` — German original
  (frames 1–9) + the German translation of frame 10 (source of the `de.vtt` track)
- `frame.md` — design system: broadside preset remixed onto the website colors
  (slate #020617, text #e2e8f0, accent sky #38bdf8; Newsreader/Inter/JetBrains Mono)
- `scripts/english_tts.py` — English TTS via **edge-tts**
  (en-US-AndrewNeural, word timestamps, per-line rate fitting into the frozen
  frame windows). `scripts/german_tts.py` — the original German TTS. Venv: `.venv-tts/`
- `scripts/build_vtt.py` — builds `renders/prime-front-explained.{en,de}.vtt`
  (37 cues each; the German track reuses the English cue windows, sentences 1:1)
- Captions (English, burned in) from the word timestamps; skin in
  `.hyperframes/caption-skin.html`
- `renders/video.mp4` (30.4 MB), `renders/poster.jpg`

## Rebuild

```bash
.venv-tts/bin/python scripts/english_tts.py    # TTS + audio_meta.json
# do NOT run sync-durations — frame windows are frozen to the original durations
node <skill>/scripts/captions.mjs build --storyboard ./STORYBOARD.md --audio-meta ./audio_meta.json --hyperframes . --out ./caption_groups.json
node <skill>/scripts/assemble-index.mjs --storyboard ./STORYBOARD.md --hyperframes .
node <skill>/scripts/transitions.mjs inject --storyboard ./STORYBOARD.md --hyperframes .
npx hyperframes lint && npx hyperframes validate && npx hyperframes inspect
npx hyperframes render --quality high --output renders/video.mp4
.venv-tts/bin/python scripts/build_vtt.py      # subtitle tracks
```

`<skill>` = `~/.claude/skills/faceless-explainer`. Preview: `npx hyperframes preview`.
