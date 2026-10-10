"""Check canonical script identity, cue integrity and provisional runtime."""
import hashlib
import json
import math
import re
import sys
from pathlib import Path


def load_json(path):
    def reject_constant(value):
        raise ValueError(f"Non-finite JSON number: {value}")
    return json.loads(Path(path).read_text(encoding="utf-8"), parse_constant=reject_constant)


def number(value, minimum=0, positive=False):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and (value > minimum if positive else value >= minimum))


def script_info(path):
    raw = Path(path).read_bytes()
    text = raw.decode("utf-8").strip()
    return {"text": text, "sha256": hashlib.sha256(raw).hexdigest(),
            "paragraphs": re.split(r"\n\s*\n", text) if text else [],
            "words": len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", text))}


def paragraph_ref(ref, paragraphs, errors, label):
    if not isinstance(ref, dict):
        errors.append(f"{label}: paragraph reference must be an object")
        return None
    pid = ref.get("paragraph_id")
    match = re.fullmatch(r"P(\d{3,})", pid) if isinstance(pid, str) else None
    index = int(match[1]) - 1 if match else -1
    if not 0 <= index < len(paragraphs):
        errors.append(f"{label}: missing paragraph {pid}")
        return None
    anchor = ref.get("anchor")
    if not isinstance(anchor, str) or not anchor or not paragraphs[index].startswith(anchor):
        errors.append(f"{label}: opening anchor mismatch {pid}")
    return index


def inspect_story(path):
    path = Path(path)
    errors = []
    meta = load_json(path / "metadata.json")
    sidecar = load_json(path / "delivery-cues.json")
    if not isinstance(meta, dict) or not isinstance(sidecar, dict):
        return ["Metadata and cues must be objects"], {}
    info = script_info(path / "script.txt")
    text, paragraphs, words = info["text"], info["paragraphs"], info["words"]
    if not text:
        errors.append("Empty spoken script")
    if re.search(r"(?im)^\s*(#{1,6}\s|NON-SPOKEN\b|SCENE\s+\d|(?:\d{1,2}:){1,2}\d{2}\b)", text):
        errors.append("Possible heading or timestamp in spoken script")
    if re.search(r"\[[^\]\n]+\]|</?(?:break|phoneme|prosody|speak)\b", text):
        errors.append("Bracketed citation/direction or synthesis markup in spoken script")
    if "\u2014" in text:
        errors.append("Em dash in spoken script")
    version = meta.get("script_version")
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        errors.append("Recorded script_version must be a positive integer")
    if sidecar.get("schema_version") != 2:
        errors.append("Delivery cue schema_version must be 2")
    if sidecar.get("instructions_are_non_spoken") is not True:
        errors.append("Sidecar must explicitly be non-spoken")
    if sidecar.get("script_version") != version:
        errors.append("Cue script_version differs from metadata")
    for label, value in (("Metadata", meta.get("script_sha256")), ("Cue", sidecar.get("script_sha256"))):
        if value != info["sha256"]:
            errors.append(f"{label} script hash mismatch")
    wpm = sidecar.get("assumed_or_observed_wpm")
    hold = sidecar.get("silent_hold_seconds", 0)
    if not number(wpm, positive=True):
        errors.append("WPM must be a finite positive number")
        wpm = 150
    if not number(hold):
        errors.append("Silent hold seconds must be finite and nonnegative")
        hold = 0
    cues = sidecar.get("cues")
    if not isinstance(cues, list):
        errors.append("cues must be an array")
        cues = []
    pauses, seen = 0, set()
    for cue in cues:
        if not isinstance(cue, dict):
            errors.append("Each cue must be an object")
            continue
        pid = cue.get("paragraph_id")
        index = paragraph_ref(cue, paragraphs, errors, "Cue")
        if isinstance(pid, str):
            if pid in seen:
                errors.append(f"Duplicate cue paragraph: {pid}; combine directions")
            seen.add(pid)
        if cue.get("pace") not in {"natural", "slower", "brisk"}:
            errors.append(f"Unsupported pace: {pid}")
        if cue.get("intent") not in {"curious", "matter_of_fact", "skeptical", "amused", "reflective"}:
            errors.append(f"Unsupported intent: {pid}")
        if cue.get("inflection", "neutral") not in {"neutral", "question", "settled"}:
            errors.append(f"Unsupported inflection: {pid}")
        phrases = cue.get("emphasis", [])
        if not isinstance(phrases, list) or any(not isinstance(p, str) or not p for p in phrases):
            errors.append(f"Emphasis must be an array of nonempty strings: {pid}")
        elif index is not None:
            for phrase in phrases:
                if phrase not in paragraphs[index]:
                    errors.append(f"Emphasis phrase absent: {pid}")
        if not isinstance(cue.get("pronunciation_notes", []), list):
            errors.append(f"Pronunciation notes must be an array: {pid}")
        pause = cue.get("pause_after_seconds", 0)
        if not number(pause):
            errors.append(f"Invalid extra pause: {pid}")
        else:
            pauses += pause
    estimate = words / wpm * 60 + pauses + hold
    runtime = meta.get("runtime")
    if not isinstance(runtime, dict):
        errors.append("Runtime must be an object")
        runtime = {}
    if runtime.get("target_min_seconds") != 480 or runtime.get("target_max_seconds") != 600:
        errors.append("Story target runtime must be 480–600 seconds")
    for field, computed in (("word_count", words), ("extra_pause_seconds", pauses),
                            ("silent_hold_seconds", hold), ("assumed_or_observed_wpm", wpm)):
        saved = runtime.get(field)
        if not number(saved) or abs(saved - computed) > 0.001:
            errors.append(f"Missing/stale metadata {field}; computed {computed}")
    saved = runtime.get("estimated_seconds")
    if not number(saved) or abs(saved - estimate) > 1:
        errors.append("Missing/stale runtime estimate")
    actual = runtime.get("actual_video_seconds")
    if actual is not None and (not number(actual) or not 480 <= actual <= 600):
        errors.append("Measured video runtime outside 480–600 seconds")
    return errors, {"script_sha256": info["sha256"], "approximate_words": words,
                    "paragraphs": len(paragraphs), "wpm": wpm,
                    "extra_pause_seconds": pauses, "silent_hold_seconds": hold,
                    "estimated_seconds": round(estimate, 1), "actual_video_seconds": actual,
                    "estimate_in_target": 480 <= estimate <= 600}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 business/tools/episode_check.py STORY_DIRECTORY")
    try:
        problems, report = inspect_story(sys.argv[1])
        print(json.dumps(report, indent=2))
        for problem in problems:
            print("ERROR:", problem)
        if report and not report["estimate_in_target"]:
            print("REVIEW: provisional estimate is outside 8–10 minutes")
        print("Word count/timing are approximate; final audio/video require actual inspection.")
        sys.exit(bool(problems))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        sys.exit(f"ERROR: {exc}")
