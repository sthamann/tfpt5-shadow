#!/usr/bin/env python3
"""English TTS for the prime-front explainer (edge-tts, Microsoft Neural).

Same contract as german_tts.py, plus per-line rate fitting: the frame windows
of the composition are frozen to the original narration durations, so each
English line is re-synthesized with a rate offset that lands its duration
just inside the frame window (target - 1.8s .. target - 0.2s where possible).

  SCRIPT.md  ->  assets/voice/NN.wav  +  word timestamps
             ->  audio_engine_meta.json / audio_meta.json

Usage:
  python english_tts.py            # full run (all 10 lines, fitted rates)
  python english_tts.py --sample   # voice comparison sample for line 1
"""

import asyncio
import json
import re
import subprocess
import sys
from pathlib import Path

import edge_tts

VOICE = "en-US-AndrewNeural"
SAMPLE_VOICES = ["en-US-AndrewNeural", "en-GB-RyanNeural"]
PROJECT = Path(__file__).resolve().parent.parent
VOICE_DIR = PROJECT / "assets" / "voice"
HNS = 10_000_000  # 100-ns ticks per second

# Frame windows (s) — frozen from STORYBOARD.md; audio must fit inside.
# Frame 10 (2026-08-13 closing segment) got its window chosen at authoring
# time; from now on it is frozen like the rest.
TARGETS = {1: 16.872, 2: 13.848, 3: 15.288, 4: 24.36, 5: 18.144,
           6: 19.344, 7: 16.176, 8: 19.584, 9: 15.504, 10: 26.0}
FIT_MIN_GAP = 0.2   # leave at least this much air before the frame cut
FIT_MAX_GAP = 1.8   # do not leave more silence than this (keeps pacing tight)
RATE_CLAMP = 18     # max |rate| percent — beyond this the voice degrades


def parse_script(md: str):
    """SCRIPT.md -> [(frame_number, spoken_text)] — same rules as audio.mjs."""
    out = []
    cur = None
    for line in md.splitlines():
        h = re.match(r"^#{2,3}\s+.*?\(frame\s+(\d+)\)", line, re.I)
        if h:
            if cur and cur[1].strip():
                out.append((cur[0], cur[1].strip()))
            cur = [int(h.group(1)), ""]
            continue
        if cur is None:
            continue
        if re.match(r"^\s*\*\*", line):
            continue
        m = re.match(r"^(?: {4,}|\t)(.+)$", line)
        if m:
            cur[1] += (" " if cur[1] else "") + m.group(1).strip()
    if cur and cur[1].strip():
        out.append((cur[0], cur[1].strip()))
    return out


async def synth_once(text: str, voice: str, rate_pct: int, mp3_path: Path):
    rate = f"{rate_pct:+d}%"
    communicate = edge_tts.Communicate(text, voice, rate=rate,
                                       boundary="WordBoundary")
    words = []
    with open(mp3_path, "wb") as fh:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                fh.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / HNS
                end = (chunk["offset"] + chunk["duration"]) / HNS
                words.append({"id": f"w{len(words)}", "text": chunk["text"],
                              "start": round(start, 3), "end": round(end, 3)})
    return words


def mp3_duration(path: Path) -> float:
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        check=True, capture_output=True, text=True)
    return round(float(probe.stdout.strip()), 3)


async def synth_fitted(frame: int, text: str):
    frame_id = f"{frame:02d}"
    mp3_path = VOICE_DIR / f"{frame_id}.mp3"
    wav_path = VOICE_DIR / f"{frame_id}.wav"
    target = TARGETS[frame]

    rate = 0
    words = await synth_once(text, VOICE, rate, mp3_path)
    dur = mp3_duration(mp3_path)
    gap = target - dur

    if gap < FIT_MIN_GAP or gap > FIT_MAX_GAP:
        # duration scales ~ 1/(1 + rate/100); aim for target - 1.0s
        want = target - 1.0
        rate = round((dur / want - 1) * 100)
        rate = max(-RATE_CLAMP, min(RATE_CLAMP, rate))
        words = await synth_once(text, VOICE, rate, mp3_path)
        dur = mp3_duration(mp3_path)
        # one nudge if we overshot the frame window
        while dur > target - FIT_MIN_GAP and rate < RATE_CLAMP:
            rate = min(RATE_CLAMP, rate + 3)
            words = await synth_once(text, VOICE, rate, mp3_path)
            dur = mp3_duration(mp3_path)

    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3_path),
         "-ar", "44100", "-ac", "1", str(wav_path)],
        check=True)
    mp3_path.unlink()
    dur = round(float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(wav_path)],
        check=True, capture_output=True, text=True).stdout.strip()), 3)

    rel = f"assets/voice/{frame_id}.wav"
    print(f"  voice {frame_id}: {dur}s (window {target}s, rate {rate:+d}%, "
          f"{len(words)} words)")
    if dur > target:
        print(f"  !! frame {frame}: audio exceeds window by {dur - target:.2f}s")
    return {"id": frame_id, "path": rel, "duration_s": dur,
            "rate_pct": rate, "words": words}


async def sample():
    lines = parse_script((PROJECT / "SCRIPT.md").read_text(encoding="utf-8"))
    text = lines[0][1]
    out_dir = PROJECT / "assets" / "voice-samples"
    out_dir.mkdir(parents=True, exist_ok=True)
    for voice in SAMPLE_VOICES:
        mp3 = out_dir / f"sample-{voice}.mp3"
        await synth_once(text, voice, 0, mp3)
        print(f"  {voice}: {mp3_duration(mp3)}s -> {mp3}")


async def main():
    lines = parse_script((PROJECT / "SCRIPT.md").read_text(encoding="utf-8"))
    if not lines:
        sys.exit("no spoken lines found in SCRIPT.md")
    VOICE_DIR.mkdir(parents=True, exist_ok=True)

    voices = [await synth_fitted(frame, text) for frame, text in lines]
    total = round(sum(v["duration_s"] for v in voices), 3)

    neutral = {
        "tts_provider": "edge-tts",
        "voice_id": VOICE,
        "bgm": None,
        "bgm_pending": False,
        "voices": voices,
        "sfx": [],
        "total_duration_s": total,
    }
    (PROJECT / "audio_engine_meta.json").write_text(
        json.dumps(neutral, ensure_ascii=False, indent=2), encoding="utf-8")

    pl_meta = {
        "bgm": None,
        "bgm_pending": False,
        "voices": [
            {"frame": int(v["id"]), "path": v["path"],
             "duration_s": v["duration_s"], "words": v["words"]}
            for v in voices
        ],
        "sfx": [],
    }
    (PROJECT / "audio_meta.json").write_text(
        json.dumps(pl_meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ english_tts: {len(voices)} voices, total {total}s -> audio_meta.json")


if __name__ == "__main__":
    if "--sample" in sys.argv:
        asyncio.run(sample())
    else:
        asyncio.run(main())
