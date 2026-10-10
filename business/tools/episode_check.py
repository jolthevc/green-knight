"""Validate a spoken script and sidecar; estimate, never certify, runtime."""
import json
import re
import sys
from pathlib import Path


def inspect_story(path):
    path = Path(path)
    errors = []
    meta = json.loads((path / "metadata.json").read_text())
    sidecar = json.loads((path / "delivery-cues.json").read_text())
    script = (path / "script.txt").read_text().strip()
    paragraphs = re.split(r"\n\s*\n", script) if script else []
    words = len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", script))
    if not script:
        errors.append("Empty spoken script")
    if re.search(r"(?im)^\s*(#|NON-SPOKEN|SCENE\s+\d|\[\s*(pause|slow|voice|emphasis|S\d))", script):
        errors.append("Possible heading, citation or delivery direction in spoken script")
    if sidecar.get("instructions_are_non_spoken") is not True:
        errors.append("Sidecar must explicitly be non-spoken")
    if sidecar.get("script_version") != meta.get("script_version"):
        errors.append("Cue script_version differs from metadata")
    wpm = sidecar.get("assumed_or_observed_wpm")
    hold = sidecar.get("silent_hold_seconds", 0)
    if not isinstance(wpm, (int, float)) or isinstance(wpm, bool) or wpm <= 0:
        errors.append("WPM must be a positive number")
        wpm = 150
    if not isinstance(hold, (int, float)) or isinstance(hold, bool) or hold < 0:
        errors.append("Silent hold seconds must be nonnegative")
        hold = 0
    pauses = 0
    seen = set()
    cues = sidecar.get("cues", [])
    if not isinstance(cues, list):
        errors.append("cues must be an array")
        cues = []
    for cue in cues:
        pid = cue.get("paragraph_id", "")
        match = re.fullmatch(r"P(\d{3,})", pid)
        index = int(match[1]) - 1 if match else -1
        if pid in seen:
            errors.append(f"Duplicate cue paragraph: {pid}; combine its directions")
        seen.add(pid)
        if not 0 <= index < len(paragraphs):
            errors.append(f"Missing paragraph: {pid}")
            continue
        text = paragraphs[index]
        anchor = cue.get("anchor")
        if not isinstance(anchor, str) or not anchor or not text.startswith(anchor):
            errors.append(f"Opening anchor mismatch: {pid}")
        if cue.get("pace") not in {"natural", "slower", "brisk"}:
            errors.append(f"Unsupported pace: {pid}")
        if cue.get("intent") not in {"curious", "matter_of_fact", "skeptical", "amused", "reflective"}:
            errors.append(f"Unsupported intent: {pid}")
        for phrase in cue.get("emphasis", []):
            if not phrase or phrase not in text:
                errors.append(f"Emphasis phrase absent: {pid}")
        pause = cue.get("pause_after_seconds", 0)
        if not isinstance(pause, (int, float)) or isinstance(pause, bool) or pause < 0:
            errors.append(f"Invalid extra pause: {pid}")
        else:
            pauses += pause
    estimated = words / wpm * 60 + pauses + hold
    runtime = meta.get("runtime", {})
    for field, computed in (("word_count", words), ("extra_pause_seconds", pauses),
                            ("silent_hold_seconds", hold), ("assumed_or_observed_wpm", wpm)):
        saved = runtime.get(field)
        if saved is not None and saved != computed:
            errors.append(f"Stale metadata {field}: saved {saved}, computed {computed}")
    saved_estimate = runtime.get("estimated_seconds")
    if saved_estimate is not None and abs(saved_estimate - estimated) > 1:
        errors.append("Saved runtime estimate differs by more than one second")
    actual = runtime.get("actual_video_seconds")
    if actual is not None:
        if not isinstance(actual, (int, float)) or isinstance(actual, bool) or not 480 <= actual <= 600:
            errors.append("Measured video runtime outside 480–600 seconds")
    return errors, {"words": words, "paragraphs": len(paragraphs), "wpm": wpm,
                    "extra_pause_seconds": pauses, "silent_hold_seconds": hold,
                    "estimated_seconds": round(estimated, 1),
                    "actual_video_seconds": actual,
                    "estimate_in_target": 480 <= estimated <= 600}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 business/tools/episode_check.py STORY_DIRECTORY")
    try:
        problems, report = inspect_story(sys.argv[1])
        print(json.dumps(report, indent=2))
        for problem in problems:
            print("ERROR:", problem)
        if not report["estimate_in_target"]:
            print("REVIEW: provisional estimate is outside 8–10 minutes")
        print("Actual rendered duration must be checked by the editor.")
        sys.exit(bool(problems))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        sys.exit(f"ERROR: {exc}")
