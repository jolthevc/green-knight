"""Synthetic temporary fixtures exercise readiness failures, never real episodes."""
import copy
import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import validate as validator
from episode_check import inspect_story


class WorkflowIntegrity(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(validator.BUSINESS, self.root / "business",
                        ignore=shutil.ignore_patterns("__pycache__"))
        self.business = self.root / "business"
        self.patch_root = patch.object(validator, "ROOT", self.root)
        self.patch_business = patch.object(validator, "BUSINESS", self.business)
        self.patch_root.start()
        self.patch_business.start()
        self.addCleanup(self.patch_root.stop)
        self.addCleanup(self.patch_business.stop)

    def read(self, path):
        return json.loads(path.read_text())

    def write(self, path, value):
        path.write_text(json.dumps(value, indent=2))

    def story(self):
        self.path = self.business / "channels/pretty-penny/stories/PP-V9000-synthetic-fixture"
        shutil.copytree(self.business / "templates/story", self.path,
                        ignore=shutil.ignore_patterns("README.md"))
        for name in validator.ARTIFACTS:
            if name.endswith(".md"):
                (self.path / name).write_text("# Synthetic fixture\n\nPopulated structural test material, not real reporting.\n")
        text = "This is a synthetic test passage. " + "A simple model explains the payment. " * 210
        (self.path / "script.txt").write_text(text)
        self.digest = hashlib.sha256(text.encode()).hexdigest()
        cue = self.read(self.path / "delivery-cues.json")
        cue.update(script_version=1, script_sha256=self.digest, cues=[{
            "paragraph_id": "P001", "anchor": "This is a synthetic test passage.",
            "pace": "natural", "intent": "matter_of_fact", "inflection": "settled",
            "emphasis": ["synthetic"], "pause_after_seconds": 0, "pronunciation_notes": []}])
        self.write(self.path / "delivery-cues.json", cue)
        meta = self.read(self.path / "metadata.json")
        # Count using the same documented word definition, independently from runtime metadata.
        import re
        words = len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", text))
        meta.update(idea_id="PP-I9000", story_id="PP-V9000", channel="pretty-penny",
                    title="Synthetic fixture", status="scripted", script_version=1,
                    script_sha256=self.digest, created_at="2026-10-10", updated_at="2026-10-10")
        meta["runtime"].update(word_count=words, estimated_seconds=words / 150 * 60)
        meta["editorial"].update(passed=True, reviewed_by="synthetic fixture",
                                  reviewed_at="2026-10-10", reviewed_script_sha256=self.digest)
        self.write(self.path / "metadata.json", meta)
        evidence = {"schema_version": 1, "script_version": 1, "script_sha256": self.digest,
                    "sources": [{"id": "S001", "publisher": "Synthetic test source",
                        "title": "Not real reporting", "url": "https://example.org/test",
                        "accessed_at": "2026-10-10", "locator": "Synthetic fixture",
                        "access_status": "opened"}],
                    "claims": [{"id": "C001", "paragraph_id": "P001",
                        "anchor": "This is a synthetic test passage.", "claim": "Synthetic test claim",
                        "source_ids": ["S001"], "status": "verified", "basis": "Synthetic fixture only"}],
                    "scenes": [{"id": "SC001", "paragraphs": [{"paragraph_id": "P001",
                        "anchor": "This is a synthetic test passage."}], "purpose": "Synthetic visual",
                        "evidence_type": "illustration", "source_ids": []}]}
        self.write(self.path / "evidence.json", evidence)
        ledger = self.read(self.business / "ideas/registry.json")
        ledger["ideas"].append({"id": "PP-I9000", "channel": "pretty-penny",
            "title": "Synthetic fixture", "aliases": [], "subject": "Synthetic",
            "mechanism": "Synthetic model", "viewer_promise": "Synthetic test",
            "status": "scripted", "related_idea_ids": [], "story_id": "PP-V9000",
            "story_path": str(self.path.relative_to(self.root)), "created_at": "2026-10-10",
            "updated_at": "2026-10-10", "history": [{"date": "2026-10-10", "status": "scripted",
                "note": "Synthetic fixture, not a real completed script", "actor": "test"}]})
        self.write(self.business / "ideas/registry.json", ledger)
        return meta

    def set_status(self, status):
        meta = self.read(self.path / "metadata.json")
        meta["status"] = status
        self.write(self.path / "metadata.json", meta)
        ledger = self.read(self.business / "ideas/registry.json")
        row = ledger["ideas"][-1]
        row["status"] = status
        row["history"].append({"date": "2026-10-10", "status": status,
                              "note": "Synthetic stage test", "actor": "test"})
        self.write(self.business / "ideas/registry.json", ledger)

    def approved_profiles(self):
        folder = self.business / "channels/pretty-penny"
        profile = self.read(folder / "narration.json")
        profile.update(version=1, status="approved", kind="synthetic", provider="test-provider",
                       model_id="test-model", voice_id="test-voice", observed_wpm=150,
                       reference_audio_url="https://example.org/reference.wav",
                       approved_by="test", approved_at="2026-10-10")
        self.write(folder / "narration.json", profile)
        config = self.read(folder / "channel.json")
        config["visual_profile"].update(version=1, status="approved", approved_by="test",
            approved_at="2026-10-10", reference_urls=["https://example.org/visual.png"])
        self.write(folder / "channel.json", config)
        meta = self.read(self.path / "metadata.json")
        for key in ("kind", "provider", "model_id", "voice_id", "performer_name",
                    "locale", "accent", "settings", "reference_audio_url"):
            meta["narration"][key] = profile.get(key)
        meta["narration"].update(profile_id=profile["profile_id"], profile_version=1, audition_approved=True)
        meta["visual"].update(approved=True, profile_version=1,
                             reference_urls=config["visual_profile"]["reference_urls"])
        self.write(self.path / "metadata.json", meta)

    def assert_error(self, phrase):
        self.assertTrue(any(phrase in e for e in validator.validate()), validator.validate())

    def test_real_scaffold_passes(self):
        self.assertEqual(validator.validate(), [])

    def test_complete_scripted_fixture_passes(self):
        self.story()
        self.assertEqual(validator.validate(), [])

    def test_changed_sentence_with_same_anchor_is_stale(self):
        self.story()
        p = self.path / "script.txt"
        p.write_text(p.read_text().replace("explains", "clarifies", 1))
        self.assert_error("hash mismatch")

    def test_unfilled_template_cannot_pass(self):
        self.story()
        shutil.copyfile(self.business / "templates/story/qa.md", self.path / "qa.md")
        self.assert_error("Missing/unfilled artifact")

    def test_lead_only_claim_source_is_rejected(self):
        self.story()
        p = self.path / "evidence.json"
        v = self.read(p)
        v["sources"][0]["access_status"] = "lead_only"
        self.write(p, v)
        self.assert_error("lead-only source")

    def test_missing_visual_coverage_is_rejected(self):
        self.story()
        p = self.path / "evidence.json"
        v = self.read(p); v["scenes"] = []; self.write(p, v)
        self.assert_error("Missing visual coverage")

    def test_stale_claim_anchor_is_rejected(self):
        self.story()
        p = self.path / "evidence.json"
        v = self.read(p); v["claims"][0]["anchor"] = "A different opening"; self.write(p, v)
        self.assert_error("opening anchor mismatch")

    def test_malformed_cue_fails_without_crash(self):
        self.story()
        p = self.path / "delivery-cues.json"
        v = self.read(p); v["cues"] = ["wrong type"]; self.write(p, v)
        self.assert_error("Each cue must be an object")

    def test_hidden_inline_cue_is_rejected(self):
        self.story()
        p = self.path / "script.txt"; p.write_text(p.read_text() + " [pause]")
        issues, _ = inspect_story(self.path)
        self.assertTrue(any("Bracketed" in i for i in issues))

    def test_out_of_range_measured_runtime_is_rejected(self):
        self.story()
        p = self.path / "metadata.json"; v = self.read(p)
        v["runtime"]["actual_video_seconds"] = 610; self.write(p, v)
        self.assert_error("runtime outside")

    def test_ready_requires_real_channel_profiles(self):
        self.story(); self.set_status("production_ready")
        self.assert_error("Approved channel voice required")

    def test_ready_profiles_pass_then_voice_drift_fails(self):
        self.story(); self.approved_profiles(); self.set_status("production_ready")
        self.assertEqual(validator.validate(), [])
        p = self.path / "metadata.json"; v = self.read(p)
        v["narration"]["voice_id"] = "another-voice"; self.write(p, v)
        self.assert_error("snapshot voice_id mismatch")

    def test_published_requires_full_cut_review(self):
        self.story(); self.approved_profiles(); self.set_status("published")
        p = self.path / "metadata.json"; v = self.read(p)
        v.update(published_url="https://youtu.be/TESTVIDEO01", published_at="2026-10-10")
        v["runtime"]["actual_video_seconds"] = 590; self.write(p, v)
        self.assert_error("Final audio/cut review")

    def test_orphan_story_is_rejected(self):
        (self.business / "channels/pretty-penny/stories/PP-V9999-orphan").mkdir()
        self.assert_error("Orphan story")

    def test_wrong_channel_prefix_is_rejected(self):
        p = self.business / "ideas/registry.json"; v = self.read(p)
        v["ideas"][0]["id"] = "SS-I9999"; self.write(p, v)
        self.assert_error("Wrong channel idea prefix")

    def test_old_profile_archive_preserves_ready_snapshot(self):
        self.story(); self.approved_profiles(); self.set_status("production_ready")
        folder = self.business / "channels/pretty-penny"
        old = self.read(folder / "narration.json")
        archive = folder / "narration-history"; archive.mkdir()
        self.write(archive / "v0001.json", old)
        newer = copy.deepcopy(old); newer.update(version=2, voice_id="new-test-voice")
        self.write(folder / "narration.json", newer)
        self.assertEqual(validator.validate(), [])

    def test_complete_published_fixture_passes(self):
        self.story(); self.approved_profiles(); self.set_status("published")
        p = self.path / "metadata.json"; v = self.read(p)
        public_url = "https://youtu.be/TESTVIDEO01"
        v.update(published_url=public_url, published_at="2026-10-10")
        v["runtime"]["actual_video_seconds"] = 590
        audio, cut = "https://example.org/audio.wav", "https://example.org/cut.mp4"
        v["assets"].update(audio_url=audio, final_video_url=cut)
        v["production_review"].update(passed=True, full_audio_listened=True,
            reviewed_by="synthetic fixture", reviewed_at="2026-10-10",
            reviewed_script_sha256=self.digest, audio_url=audio, final_cut_url=cut)
        self.write(p, v)
        ledger = self.read(self.business / "ideas/registry.json")
        ledger["ideas"][-1].update(published_url=public_url, published_at="2026-10-10")
        self.write(self.business / "ideas/registry.json", ledger)
        (self.path / "voice-production.md").write_text("Synthetic full-review record, not an actual recording.")
        self.assertEqual(validator.validate(), [])

    def test_publication_url_requires_video_not_channel(self):
        self.assertFalse(validator.youtube_video("https://youtube.com/@channel"))
        self.assertFalse(validator.youtube_video("https://example.org/video"))
        self.assertTrue(validator.youtube_video("https://youtu.be/TESTVIDEO01"))

    def test_nonfinite_timing_rejected(self):
        self.story()
        p = self.path / "delivery-cues.json"
        v = self.read(p); v["assumed_or_observed_wpm"] = float("nan")
        self.write(p, v)
        with self.assertRaises(ValueError):
            inspect_story(self.path)


if __name__ == "__main__":
    unittest.main()
