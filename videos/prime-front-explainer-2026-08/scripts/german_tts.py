#!/usr/bin/env python3
"""German TTS for the prime-front explainer.

Kokoro (the offline default of the hyperframes audio engine) has no German
phonemizer, and no HeyGen/ElevenLabs credential is available. This script
fills the same contract with edge-tts (Microsoft neural voices, de-DE):

  SCRIPT.md  ->  assets/voice/NN.wav  +  word timestamps
             ->  audio_engine_meta.json (neutral, id-keyed)
             ->  audio_meta.json       (frame-keyed, consumed by
                                        captions.mjs / assemble-index.mjs)

Word boundaries come from the edge-tts stream (100 ns units), so no Whisper
pass is needed.
"""

import asyncio
import json
import re
import subprocess
import sys
from pathlib import Path

import edge_tts

VOICE = "de-DE-ConradNeural"
PROJECT = Path(__file__).resolve().parent.parent
VOICE_DIR = PROJECT / "assets" / "voice"
HNS = 10_000_000  # 100-ns ticks per second


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


async def synth(frame: int, text: str):
    frame_id = f"{frame:02d}"
    mp3_path = VOICE_DIR / f"{frame_id}.mp3"
    wav_path = VOICE_DIR / f"{frame_id}.wav"

    communicate = edge_tts.Communicate(text, VOICE, boundary="WordBoundary")
    words = []
    with open(mp3_path, "wb") as fh:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                fh.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / HNS
                end = (chunk["offset"] + chunk["duration"]) / HNS
                words.append(
                    {
                        "id": f"w{len(words)}",
                        "text": chunk["text"],
                        "start": round(start, 3),
                        "end": round(end, 3),
                    }
                )

    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3_path),
         "-ar", "44100", "-ac", "1", str(wav_path)],
        check=True,
    )
    mp3_path.unlink()

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(wav_path)],
        check=True, capture_output=True, text=True,
    )
    duration = round(float(probe.stdout.strip()), 3)
    rel = f"assets/voice/{frame_id}.wav"
    print(f"  voice {frame_id}: {rel} ({duration}s, {len(words)} words)")
    return {"id": frame_id, "path": rel, "duration_s": duration, "words": words}


async def main():
    script_md = (PROJECT / "SCRIPT.md").read_text(encoding="utf-8")
    lines = parse_script(script_md)
    if not lines:
        sys.exit("no spoken lines found in SCRIPT.md")
    VOICE_DIR.mkdir(parents=True, exist_ok=True)

    voices = [await synth(frame, text) for frame, text in lines]
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
        json.dumps(neutral, ensure_ascii=False, indent=2), encoding="utf-8"
    )

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
        json.dumps(pl_meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"✓ german_tts: {len(voices)} voices, total {total}s -> audio_meta.json")


if __name__ == "__main__":
    asyncio.run(main())
