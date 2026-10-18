#!/usr/bin/env python3
"""Build WebVTT subtitle tracks for the prime-front explainer.

- en.vtt: English sentences timed from the edge-tts word timestamps.
- de.vtt: German translation track — sentences map 1:1 onto the English
  sentences per frame, so the German cues reuse the English cue windows
  (the video carries the English narration).
"""

import json
import re
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
FRAME_STARTS = [0.0, 16.872, 30.72, 46.008, 70.368, 88.512, 107.856, 124.032, 143.616,
                159.12]


def parse_script(md: str):
    out = {}
    cur = None
    for line in md.splitlines():
        h = re.match(r"^#{2,3}\s+.*?\(frame\s+(\d+)\)", line, re.I)
        if h:
            cur = int(h.group(1))
            out[cur] = ""
            continue
        if cur is None or re.match(r"^\s*\*\*", line):
            continue
        m = re.match(r"^(?: {4,}|\t)(.+)$", line)
        if m:
            out[cur] += (" " if out[cur] else "") + m.group(1).strip()
    return out


def sentences(text: str):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p]


def fmt(t: float) -> str:
    ms = int(round(t * 1000))
    h, rem = divmod(ms, 3600000)
    m, rem = divmod(rem, 60000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def build():
    en = parse_script((PROJECT / "SCRIPT.md").read_text(encoding="utf-8"))
    de = parse_script((PROJECT / "SCRIPT.de.md").read_text(encoding="utf-8"))
    meta = json.loads((PROJECT / "audio_meta.json").read_text(encoding="utf-8"))
    voices = {v["frame"]: v for v in meta["voices"]}

    cues_en, cues_de = [], []
    for frame in sorted(en):
        base = FRAME_STARTS[frame - 1]
        words = voices[frame]["words"]
        sents_en = sentences(en[frame])
        sents_de = sentences(de[frame])
        assert len(sents_en) == len(sents_de), (
            f"frame {frame}: {len(sents_en)} EN vs {len(sents_de)} DE sentences")

        tokens = [len(s.split()) for s in sents_en]
        total = sum(tokens)
        W = len(words)
        # proportional index mapping — robust against tokenizer differences
        cum = 0
        bounds = []
        for n in tokens:
            i0 = round(cum / total * W)
            cum += n
            i1 = round(cum / total * W)
            bounds.append((i0, max(i1, i0 + 1)))
        for (i0, i1), s_en, s_de in zip(bounds, sents_en, sents_de):
            start = base + words[min(i0, W - 1)]["start"]
            end = base + words[min(i1 - 1, W - 1)]["end"] + 0.15
            cues_en.append((start, end, s_en))
            cues_de.append((start, end, s_de))

    for cues, lang in ((cues_en, "en"), (cues_de, "de")):
        # clamp overlaps
        for i in range(len(cues) - 1):
            s, e, t = cues[i]
            ns = cues[i + 1][0]
            if e > ns:
                cues[i] = (s, ns - 0.05, t)
        lines = ["WEBVTT", ""]
        for i, (s, e, t) in enumerate(cues, 1):
            lines += [str(i), f"{fmt(s)} --> {fmt(e)}", t, ""]
        out = PROJECT / "renders" / f"prime-front-explained.{lang}.vtt"
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"  {out.name}: {len(cues)} cues")


if __name__ == "__main__":
    build()
