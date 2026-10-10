"""Validate the manual business ledger and linked story artifacts."""
import json
import re
import sys
from pathlib import Path
from episode_check import inspect_story

ROOT = Path(__file__).resolve().parents[2]
BUSINESS = ROOT / "business"
STATUSES = {"proposed", "selected", "researching", "researched", "scripted",
            "production_ready", "in_production", "published", "blocked", "rejected", "archived"}
CHANNELS = {"pretty-penny", "money-moves", "fallen-angels", "changing-hands", "fools-gold", "silver-spoon"}
EDITORIAL_FILES = ["brief.md", "research.md", "sources-and-claims.md",
                   "synthesis-and-outline.md", "script.txt", "delivery-cues.json",
                   "visual-plan.md", "packaging.md", "handoff.md", "qa.md"]
COMPLETE = {"scripted", "production_ready", "in_production", "published"}


def validate():
    errors = []
    ledger = json.loads((BUSINESS / "ideas/registry.json").read_text())
    if ledger.get("schema_version") != 1:
        errors.append("Unsupported registry schema")
    ideas = ledger.get("ideas")
    if not isinstance(ideas, list):
        return ["Registry ideas must be an array"]
    ids, stories = set(), set()
    for item in ideas:
        ident = item.get("id", "")
        if ident in ids or not re.fullmatch(r"[A-Z]{2,4}-I\d{4,}", ident):
            errors.append(f"Duplicate or invalid idea ID: {ident}")
        ids.add(ident)
        if item.get("channel") not in CHANNELS:
            errors.append(f"Unknown channel: {ident}")
        if item.get("channel") == "pretty-penny" and not ident.startswith("PP-I"):
            errors.append(f"Wrong Pretty Penny idea prefix: {ident}")
        if item.get("status") not in STATUSES:
            errors.append(f"Unknown status: {ident}")
        for field in ("title", "subject", "mechanism", "viewer_promise", "created_at", "updated_at"):
            if not item.get(field):
                errors.append(f"Missing {field}: {ident}")
        for field in ("aliases", "related_idea_ids", "history"):
            if not isinstance(item.get(field), list):
                errors.append(f"{field} must be an array: {ident}")
        history = item.get("history", [])
        if not history:
            errors.append(f"Missing history: {ident}")
        for event in history:
            if not all(event.get(key) for key in ("date", "status", "note", "actor")):
                errors.append(f"Incomplete history event: {ident}")
            if event.get("status") not in STATUSES:
                errors.append(f"Invalid historical status: {ident}")
        if history and history[-1].get("status") != item.get("status"):
            errors.append(f"Latest history status mismatch: {ident}")
        if item.get("status") in {"blocked", "rejected"} and not item.get("rejection_or_block_reason"):
            errors.append(f"Missing blocking/rejection reason: {ident}")
        sid, relative = item.get("story_id"), item.get("story_path")
        if item.get("status") == "proposed" and (sid or relative):
            errors.append(f"Proposed idea already allocated a story: {ident}")
        if item.get("status") not in {"proposed", "rejected", "archived", "blocked"} and not (sid and relative):
            errors.append(f"Missing selected story ID/path: {ident}")
        if bool(sid) != bool(relative):
            errors.append(f"Story ID/path must be supplied together: {ident}")
        if sid:
            if sid in stories or not re.fullmatch(r"[A-Z]{2,4}-V\d{4,}", sid):
                errors.append(f"Duplicate or invalid story ID: {sid}")
            stories.add(sid)
            if item.get("channel") == "pretty-penny" and not sid.startswith("PP-V"):
                errors.append(f"Wrong Pretty Penny story prefix: {sid}")
            path = (ROOT / relative).resolve()
            allowed = (BUSINESS / "channels" / item["channel"] / "stories").resolve()
            if not path.is_relative_to(allowed) or not path.name.startswith(sid + "-"):
                errors.append(f"Invalid story directory: {ident}")
                continue
            if not (path / "metadata.json").exists():
                errors.append(f"Story metadata missing: {ident}")
                continue
            meta = json.loads((path / "metadata.json").read_text())
            for key, expected in (("idea_id", ident), ("story_id", sid),
                                  ("channel", item["channel"]), ("status", item["status"])):
                if meta.get(key) != expected:
                    errors.append(f"Metadata {key} mismatch: {ident}")
            if item["status"] in COMPLETE:
                for name in EDITORIAL_FILES:
                    p = path / name
                    if not p.exists() or not p.read_text().strip():
                        errors.append(f"Missing/empty editorial artifact {name}: {ident}")
                    elif p.suffix == ".md" and "Template: replace all placeholders" in p.read_text():
                        errors.append(f"Unfilled template {name}: {ident}")
                if all((path / n).exists() for n in ("script.txt", "delivery-cues.json")):
                    issues, report = inspect_story(path)
                    if not report["estimate_in_target"] and report["actual_video_seconds"] is None:
                        issues.append("Scripted episode estimate outside 8–10 minutes")
                    errors.extend(f"{ident}: {issue}" for issue in issues)
            if item["status"] in {"production_ready", "in_production", "published"}:
                if meta.get("narration", {}).get("audition_approved") is not True:
                    errors.append(f"Voice audition not approved: {ident}")
            if item["status"] == "published":
                actual = meta.get("runtime", {}).get("actual_video_seconds")
                if not isinstance(actual, (int, float)) or isinstance(actual, bool) or not 480 <= actual <= 600:
                    errors.append(f"Published runtime not verified: {ident}")
                for key in ("published_url", "published_at"):
                    if not item.get(key) or meta.get(key) != item.get(key):
                        errors.append(f"Published {key} missing/mismatched: {ident}")
    for item in ideas:
        for related in item.get("related_idea_ids", []):
            if related not in ids or related == item.get("id"):
                errors.append(f"Invalid related idea: {item.get('id')} -> {related}")
    config = json.loads((BUSINESS / "channels/pretty-penny/channel.json").read_text())
    if config.get("target_runtime_seconds") != {"min": 480, "target": 540, "max": 600}:
        errors.append("Pretty Penny runtime must be 8–10 minutes")
    for p in BUSINESS.rglob("*.json"):
        json.loads(p.read_text())
    for p in BUSINESS.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", p.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#")[0]
            if target and not (p.parent / target).exists():
                errors.append(f"Broken local link in {p.relative_to(ROOT)}: {target}")
    return errors


if __name__ == "__main__":
    try:
        problems = validate()
        for problem in problems:
            print("ERROR:", problem)
        if problems:
            sys.exit(1)
        print("Business registry, configuration, JSON, links and linked stories validated.")
        print("Factual accuracy and final audio/video still require editorial inspection.")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        sys.exit(f"ERROR: {exc}")
