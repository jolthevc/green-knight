"""Regression tests for the non-spoken TITLE header in canonical story scripts.

Run: python3 -m unittest discover -s business/tools -p 'test_*.py'
"""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from episode_check import inspect_story, script_info


class ScriptHeaderTest(unittest.TestCase):
    def create_story(self, directory, full_script, metadata_title="An Example Title"):
        path = Path(directory)
        raw = full_script.encode("utf-8")
        (path / "script.txt").write_bytes(raw)
        words = script_info(path / "script.txt")["words"]
        (path / "metadata.json").write_text(json.dumps({
            "title": metadata_title,
            "script_version": 1,
            "script_sha256": hashlib.sha256(raw).hexdigest(),
            "runtime": {
                "target_min_seconds": 480, "target_max_seconds": 600,
                "word_count": words, "extra_pause_seconds": 0,
                "silent_hold_seconds": 0, "assumed_or_observed_wpm": 150,
                "estimated_seconds": words / 150 * 60,
                "actual_video_seconds": None
            }
        }), encoding="utf-8")
        (path / "delivery-cues.json").write_text(json.dumps({
            "schema_version": 2, "script_version": 1,
            "instructions_are_non_spoken": True,
            "script_sha256": hashlib.sha256(raw).hexdigest(),
            "assumed_or_observed_wpm": 150,
            "silent_hold_seconds": 0, "cues": []
        }), encoding="utf-8")
        return path

    def test_title_not_spoken_or_numbered(self):
        with tempfile.TemporaryDirectory() as folder:
            path = self.create_story(
                folder,
                "TITLE: An Example Title\n\nFirst spoken paragraph.\n\nSecond spoken paragraph.\n"
            )
            info = script_info(path / "script.txt")
            self.assertEqual(info["title"], "An Example Title")
            self.assertEqual(info["paragraphs"],
                             ["First spoken paragraph.", "Second spoken paragraph."])
            self.assertEqual(info["words"], 6)
            errors, report = inspect_story(path)
            self.assertEqual(errors, [])
            self.assertEqual(report["title"], "An Example Title")
            self.assertEqual(report["paragraphs"], 2)

    def test_missing_title_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = self.create_story(folder, "First spoken paragraph.\n")
            errors, _ = inspect_story(path)
            self.assertTrue(any("Missing first-line TITLE" in x for x in errors))

    def test_wrong_title_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = self.create_story(folder, "TITLE: Other Title\n\nFirst spoken paragraph.\n")
            errors, _ = inspect_story(path)
            self.assertTrue(any("differs from metadata.title" in x for x in errors))

    def test_no_blank_line_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = self.create_story(folder, "TITLE: An Example Title\nFirst spoken paragraph.\n")
            errors, _ = inspect_story(path)
            self.assertTrue(any("Missing first-line TITLE" in x for x in errors))

    def test_title_changes_hash_but_not_narration(self):
        with tempfile.TemporaryDirectory() as folder:
            a = self.create_story(folder, "TITLE: An Example Title\n\nThe narration stays exactly the same.\n")
            before = script_info(a / "script.txt")
            (a / "script.txt").write_text(
                "TITLE: Another Title\n\nThe narration stays exactly the same.\n", encoding="utf-8"
            )
            after = script_info(a / "script.txt")
            self.assertNotEqual(before["sha256"], after["sha256"])
            self.assertEqual(before["paragraphs"], after["paragraphs"])
            self.assertEqual(before["words"], after["words"])


if __name__ == "__main__":
    unittest.main()
