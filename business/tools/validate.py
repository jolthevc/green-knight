"""Validate six channel definitions, ledger, stage gates and script-linked evidence."""
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from episode_check import inspect_story, load_json, number, paragraph_ref, script_info

ROOT = Path(__file__).resolve().parents[2]
BUSINESS = ROOT / "business"
CHANNELS = {"pretty-penny", "money-moves", "fallen-angels", "changing-hands", "fools-gold", "silver-spoon"}
STATUSES = {"proposed", "selected", "researching", "researched", "scripted",
            "production_ready", "in_production", "published", "blocked", "rejected", "archived"}
COMPLETE = {"scripted", "production_ready", "in_production", "published"}
READY = {"production_ready", "in_production", "published"}
ARTIFACTS = ["brief.md", "research.md", "sources-and-claims.md", "synthesis-and-outline.md",
             "script.txt", "delivery-cues.json", "evidence.json", "visual-plan.md",
             "packaging.md", "handoff.md", "qa.md"]
CHANNEL_FILES = ["README.md", "CHANNEL.md", "STYLE.md", "VOICE.md", "SCRIPT_STANDARD.md",
                 "START_A_CHAT.md", "narration.json", "stories/README.md"]


def url(value):
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"https", "http"} and bool(parsed.netloc)


def youtube_video(value):
    if not url(value):
        return False
    parsed = urlparse(value)
    if parsed.hostname == "youtu.be":
        video_id = parsed.path.strip("/")
    elif parsed.hostname in {"youtube.com", "www.youtube.com", "m.youtube.com"} and parsed.path == "/watch":
        video_id = parse_qs(parsed.query).get("v", [""])[0]
    else:
        return False
    return bool(re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id))


def date(value):
    if not isinstance(value, str) or not re.match(r"^\d{4}-\d{2}-\d{2}(?:$|T)", value):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def strings(value):
    return isinstance(value, list) and all(isinstance(v, str) and v for v in value)


def filled(path):
    if not path.is_file():
        return False
    content = path.read_text(encoding="utf-8").strip()
    return bool(content) and not re.search(r"(?im)^Template:", content)


def profile_errors(profile, label):
    errors = []
    if not isinstance(profile, dict):
        return [f"{label}: narrator profile must be an object"]
    if profile.get("status") not in {"unselected", "approved"}:
        errors.append(f"{label}: invalid narrator status")
    if not isinstance(profile.get("version"), int) or isinstance(profile.get("version"), bool) or profile["version"] < 0:
        errors.append(f"{label}: invalid narrator version")
    if not isinstance(profile.get("settings"), dict) or not isinstance(profile.get("pronunciations"), list):
        errors.append(f"{label}: invalid settings/pronunciation types")
    if profile.get("status") == "approved":
        if not number(profile.get("version"), positive=True):
            errors.append(f"{label}: approved narrator requires a positive version")
        if not url(profile.get("reference_audio_url")) or not profile.get("approved_by") or not date(profile.get("approved_at")):
            errors.append(f"{label}: approved narrator lacks audition evidence")
        if not number(profile.get("observed_wpm"), positive=True):
            errors.append(f"{label}: approved narrator lacks measured WPM")
        if profile.get("kind") == "synthetic":
            if not all(profile.get(key) for key in ("provider", "model_id", "voice_id")):
                errors.append(f"{label}: synthetic profile lacks provider/model/voice")
        elif profile.get("kind") == "human":
            if not profile.get("performer_name"):
                errors.append(f"{label}: human profile lacks performer")
        else:
            errors.append(f"{label}: narrator kind must be synthetic or human")
    return errors


def inspect_evidence(path, meta, scripted):
    errors = []
    evidence = load_json(path / "evidence.json")
    if not isinstance(evidence, dict):
        return ["Evidence must be an object"]
    if evidence.get("schema_version") != 1:
        errors.append("Unsupported evidence schema")
    info = script_info(path / "script.txt") if scripted else None
    if scripted:
        if evidence.get("script_version") != meta.get("script_version") or evidence.get("script_sha256") != info["sha256"]:
            errors.append("Evidence script version/hash mismatch")
    sources = {}
    rows = evidence.get("sources")
    if not isinstance(rows, list) or not rows:
        errors.append("Evidence sources must be a populated array")
        rows = []
    for source in rows:
        if not isinstance(source, dict):
            errors.append("Source must be an object")
            continue
        sid = source.get("id")
        if not isinstance(sid, str) or not re.fullmatch(r"S\d{3,}", sid) or sid in sources:
            errors.append(f"Duplicate/invalid source ID: {sid}")
            continue
        sources[sid] = source
        if not all(isinstance(source.get(k), str) and source[k] for k in ("publisher", "title")):
            errors.append(f"Missing source publisher/title: {sid}")
        if not url(source.get("url")) or not date(source.get("accessed_at")):
            errors.append(f"Missing/invalid source URL/access date: {sid}")
        if source.get("access_status") not in {"opened", "partial", "lead_only"}:
            errors.append(f"Invalid source access status: {sid}")
        if source.get("access_status") != "lead_only" and not source.get("locator"):
            errors.append(f"Opened/partial source needs supporting locator: {sid}")

    def source_refs(record, label, required):
        refs = record.get("source_ids")
        if not isinstance(refs, list) or any(not isinstance(v, str) for v in refs):
            errors.append(f"{label}: source_ids must be an array of strings")
            return
        if required and not refs:
            errors.append(f"{label}: supporting sources required")
        for sid in refs:
            if sid not in sources:
                errors.append(f"{label}: unknown source {sid}")
            elif sources[sid].get("access_status") == "lead_only":
                errors.append(f"{label}: lead-only source cannot support completed evidence")

    claims = evidence.get("claims")
    if not isinstance(claims, list) or not claims:
        errors.append("Evidence claims must be a populated array")
        claims = []
    seen = set()
    for claim in claims:
        if not isinstance(claim, dict):
            errors.append("Claim must be an object")
            continue
        cid = claim.get("id")
        if not isinstance(cid, str) or not re.fullmatch(r"C\d{3,}", cid) or cid in seen:
            errors.append(f"Duplicate/invalid claim ID: {cid}")
        else:
            seen.add(cid)
        if not claim.get("claim") or not claim.get("basis"):
            errors.append(f"Missing claim/basis: {cid}")
        status = claim.get("status")
        if status not in {"verified", "inference", "illustrative"}:
            errors.append(f"Invalid claim status: {cid}")
        source_refs(claim, str(cid), status != "illustrative")
        if scripted:
            paragraph_ref(claim, info["paragraphs"], errors, str(cid))
    scenes = evidence.get("scenes")
    if not isinstance(scenes, list):
        errors.append("Scenes must be an array")
        scenes = []
    if scripted:
        coverage, seen = set(), set()
        for scene in scenes:
            if not isinstance(scene, dict):
                errors.append("Scene must be an object")
                continue
            sid = scene.get("id")
            if not isinstance(sid, str) or not re.fullmatch(r"SC\d{3,}", sid) or sid in seen:
                errors.append(f"Duplicate/invalid scene ID: {sid}")
            else:
                seen.add(sid)
            kind = scene.get("evidence_type")
            if kind not in {"illustration", "document", "data", "reconstruction"} or not scene.get("purpose"):
                errors.append(f"Scene lacks valid evidence type/purpose: {sid}")
            source_refs(scene, str(sid), kind in {"document", "data"})
            refs = scene.get("paragraphs")
            if not isinstance(refs, list) or not refs:
                errors.append(f"Scene paragraph references required: {sid}")
                continue
            for ref in refs:
                index = paragraph_ref(ref, info["paragraphs"], errors, str(sid))
                if index is not None:
                    coverage.add(index)
        missing = [f"P{i+1:03}" for i in range(len(info["paragraphs"])) if i not in coverage]
        if missing:
            errors.append("Missing visual coverage: " + ", ".join(missing))
    return errors


def validate():
    errors = []
    ledger = load_json(BUSINESS / "ideas/registry.json")
    if not isinstance(ledger, dict) or ledger.get("schema_version") != 1 or not date(ledger.get("updated_at")):
        return ["Invalid registry schema/date"]
    ideas = ledger.get("ideas")
    if not isinstance(ideas, list):
        return ["Registry ideas must be an array"]
    configs, profiles = {}, {}
    for slug in sorted(CHANNELS):
        folder = BUSINESS / "channels" / slug
        config_path = folder / "channel.json"
        if not config_path.is_file():
            errors.append(f"Missing channel configuration: {slug}")
            continue
        config = load_json(config_path)
        configs[slug] = config
        for name in CHANNEL_FILES:
            if not (folder / name).is_file():
                errors.append(f"Missing channel file: {slug}/{name}")
        if config.get("id") != slug or config.get("target_runtime_seconds") != {"min": 480, "target": 540, "max": 600}:
            errors.append(f"Channel ID/runtime mismatch: {slug}")
        for key, suffix in (("idea_prefix", "-I"), ("story_prefix", "-V")):
            value = config.get(key)
            if not isinstance(value, str) or not re.fullmatch(r"[A-Z]{2,4}" + suffix, value):
                errors.append(f"Invalid {key}: {slug}")
        expected_path = f"business/channels/{slug}/narration.json"
        if config.get("narration", {}).get("profile_path") != expected_path:
            errors.append(f"Narrator profile path mismatch: {slug}")
        if (folder / "narration.json").is_file():
            p = load_json(folder / "narration.json")
            profiles[slug] = p
            errors.extend(profile_errors(p, slug))
            if p.get("profile_id") != config.get("narration", {}).get("profile_id"):
                errors.append(f"Narrator profile ID mismatch: {slug}")
    for key in ("idea_prefix", "story_prefix"):
        values = [c.get(key) for c in configs.values()]
        if len(values) != len(set(values)):
            errors.append(f"Channel {key} values must be unique")
    ids, stories, linked_paths = set(), set(), set()
    for item in ideas:
        if not isinstance(item, dict):
            errors.append("Idea must be an object")
            continue
        ident, slug, status = item.get("id"), item.get("channel"), item.get("status")
        if not isinstance(ident, str) or not re.fullmatch(r"[A-Z]{2,4}-I\d{4,}", ident) or ident in ids:
            errors.append(f"Duplicate/invalid idea ID: {ident}")
            continue
        ids.add(ident)
        config = configs.get(slug)
        if config is None:
            errors.append(f"Unknown/unconfigured channel: {ident}")
            continue
        if not ident.startswith(config["idea_prefix"]):
            errors.append(f"Wrong channel idea prefix: {ident}")
        if status not in STATUSES:
            errors.append(f"Invalid status: {ident}")
        for field in ("title", "subject", "mechanism", "viewer_promise"):
            if not isinstance(item.get(field), str) or not item[field]:
                errors.append(f"Missing {field}: {ident}")
        for field in ("created_at", "updated_at"):
            if not date(item.get(field)):
                errors.append(f"Invalid {field}: {ident}")
        for field in ("aliases", "related_idea_ids"):
            if not isinstance(item.get(field), list) or any(not isinstance(v, str) for v in item[field]):
                errors.append(f"Invalid {field}: {ident}")
        history = item.get("history")
        if not isinstance(history, list) or not history:
            errors.append(f"Missing history: {ident}")
            history = []
        for event in history:
            if not isinstance(event, dict) or not date(event.get("date")) or event.get("status") not in STATUSES or not event.get("actor") or not event.get("note"):
                errors.append(f"Invalid history event: {ident}")
        if history and isinstance(history[-1], dict) and history[-1].get("status") != status:
            errors.append(f"Latest history status mismatch: {ident}")
        if status in {"blocked", "rejected"} and not item.get("rejection_or_block_reason"):
            errors.append(f"Missing blocking/rejection reason: {ident}")
        sid, relative = item.get("story_id"), item.get("story_path")
        if status == "proposed" and (sid or relative):
            errors.append(f"Proposed idea already allocated a story: {ident}")
        if status not in {"proposed", "rejected", "archived", "blocked"} and not (sid and relative):
            errors.append(f"Missing selected story ID/path: {ident}")
        if bool(sid) != bool(relative):
            errors.append(f"Story ID/path must be supplied together: {ident}")
        if not sid:
            continue
        if not isinstance(sid, str) or not re.fullmatch(re.escape(config["story_prefix"]) + r"\d{4,}", sid) or sid in stories:
            errors.append(f"Duplicate/invalid story ID: {sid}")
            continue
        stories.add(sid)
        if not isinstance(relative, str):
            errors.append(f"Invalid story path: {ident}")
            continue
        path = (ROOT / relative).resolve()
        allowed = (BUSINESS / "channels" / slug / "stories").resolve()
        if Path(relative).is_absolute() or not path.is_relative_to(allowed) or path.parent != allowed or not path.name.startswith(sid + "-"):
            errors.append(f"Invalid story directory: {ident}")
            continue
        linked_paths.add(path)
        if not (path / "metadata.json").is_file():
            errors.append(f"Missing story metadata: {ident}")
            continue
        meta = load_json(path / "metadata.json")
        if not isinstance(meta, dict):
            errors.append(f"Story metadata must be an object: {ident}")
            continue
        for key, expected in (("idea_id", ident), ("story_id", sid), ("channel", slug), ("status", status)):
            if meta.get(key) != expected:
                errors.append(f"Metadata {key} mismatch: {ident}")
        if status == "researched":
            for name in ("research.md", "synthesis-and-outline.md", "sources-and-claims.md"):
                if not filled(path / name):
                    errors.append(f"Research artifact incomplete {name}: {ident}")
            if (path / "evidence.json").is_file():
                errors.extend(f"{ident}: {e}" for e in inspect_evidence(path, meta, False))
            else:
                errors.append(f"Missing evidence.json: {ident}")
        if status in COMPLETE:
            for name in ARTIFACTS:
                if not filled(path / name):
                    errors.append(f"Missing/unfilled artifact {name}: {ident}")
            if all((path / n).is_file() for n in ("script.txt", "delivery-cues.json")):
                issues, report = inspect_story(path)
                errors.extend(f"{ident}: {e}" for e in issues)
                if report and not report["estimate_in_target"] and report["actual_video_seconds"] is None:
                    errors.append(f"Script estimate outside 8–10 minutes: {ident}")
            if (path / "evidence.json").is_file() and (path / "script.txt").is_file():
                errors.extend(f"{ident}: {e}" for e in inspect_evidence(path, meta, True))
            editorial = meta.get("editorial", {})
            if (editorial.get("passed") is not True or not editorial.get("reviewed_by")
                    or not date(editorial.get("reviewed_at"))
                    or editorial.get("reviewed_script_sha256") != meta.get("script_sha256")
                    or editorial.get("blocking_issues") != []):
                errors.append(f"Editorial review incomplete/stale: {ident}")
        if status in READY:
            snap = meta.get("narration", {})
            profile = profiles.get(slug, {})
            version = snap.get("profile_version")
            if version != profile.get("version") and isinstance(version, int) and not isinstance(version, bool) and version > 0:
                archive = BUSINESS / "channels" / slug / "narration-history" / f"v{version:04}.json"
                profile = load_json(archive) if archive.is_file() else {}
            errors.extend(profile_errors(profile, f"{ident} profile"))
            if profile.get("status") != "approved" or snap.get("audition_approved") is not True:
                errors.append(f"Approved channel voice required: {ident}")
            if snap.get("profile_id") != profile.get("profile_id") or version != profile.get("version"):
                errors.append(f"Narrator snapshot version mismatch: {ident}")
            for key in ("kind", "provider", "model_id", "voice_id", "performer_name",
                        "locale", "accent", "settings", "reference_audio_url"):
                if snap.get(key) != profile.get(key):
                    errors.append(f"Narrator snapshot {key} mismatch: {ident}")
            visual = meta.get("visual", {})
            vp = config.get("visual_profile", {})
            vv = visual.get("profile_version")
            if vv != vp.get("version") and isinstance(vv, int) and not isinstance(vv, bool) and vv > 0:
                archive = BUSINESS / "channels" / slug / "visual-history" / f"v{vv:04}.json"
                vp = load_json(archive) if archive.is_file() else {}
            refs = vp.get("reference_urls")
            if (visual.get("approved") is not True or vp.get("status") != "approved"
                    or not number(vv, positive=True) or vv != vp.get("version")
                    or not vp.get("approved_by") or not date(vp.get("approved_at"))
                    or not isinstance(refs, list) or not refs or not all(url(v) for v in refs)
                    or visual.get("reference_urls") != refs):
                errors.append(f"Approved visual snapshot required: {ident}")
        if status == "published":
            actual = meta.get("runtime", {}).get("actual_video_seconds")
            if not number(actual) or not 480 <= actual <= 600:
                errors.append(f"Published runtime not verified: {ident}")
            for key in ("published_url", "published_at"):
                valid = youtube_video(item.get(key)) if key == "published_url" else date(item.get(key))
                if not valid or meta.get(key) != item.get(key):
                    errors.append(f"Published {key} missing/mismatched: {ident}")
            review, assets = meta.get("production_review", {}), meta.get("assets", {})
            if (review.get("passed") is not True or review.get("full_audio_listened") is not True
                    or not review.get("reviewed_by") or not date(review.get("reviewed_at"))
                    or review.get("reviewed_script_sha256") != meta.get("script_sha256")
                    or not url(review.get("audio_url")) or not url(review.get("final_cut_url"))
                    or review.get("audio_url") != assets.get("audio_url")
                    or review.get("final_cut_url") != assets.get("final_video_url")
                    or not filled(path / "voice-production.md")):
                errors.append(f"Final audio/cut review incomplete/stale: {ident}")
    for item in ideas:
        if isinstance(item, dict) and isinstance(item.get("related_idea_ids"), list):
            for related in item["related_idea_ids"]:
                if not isinstance(related, str) or related not in ids or related == item.get("id"):
                    errors.append(f"Invalid related idea: {item.get('id')} -> {related}")
    for slug in configs:
        for folder in (BUSINESS / "channels" / slug / "stories").iterdir():
            if folder.is_dir() and folder.resolve() not in linked_paths:
                errors.append(f"Orphan story directory: {folder.relative_to(ROOT)}")
    for p in BUSINESS.rglob("*.json"):
        load_json(p)
    for p in BUSINESS.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
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
        print("Six-channel configuration, profiles, ledger, stage gates and script-linked artifacts validated.")
        print("Source truth, subjective quality and actual listening still require inspection.")
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        sys.exit(f"ERROR: invalid input: {exc}")
