import copy
import json
import unittest
from pathlib import Path
from tools.level_verifier import (
    LevelTestCase,
    assert_snapshot_matches,
)


CASES_DIR = Path(__file__).resolve().parent / "level_cases"


class TestLevelSnapshotCases(LevelTestCase):
    """Automatically discovers and verifies all paired (.py, .json) snapshot cases in tests/level_cases/."""

    def test_all_level_cases_match_stripped_json(self):
        """Build every .py case in tests/level_cases/ and verify exported JSON matches its stripped .json."""
        py_files = sorted(CASES_DIR.glob("*.py"))
        self.assertGreater(len(py_files), 0, f"No .py cases found in {CASES_DIR}")

        for py_path in py_files:
            json_path = py_path.with_suffix(".json")
            self.assertTrue(
                json_path.is_file(),
                f"Missing matching expected JSON snapshot for {py_path.name}: expected {json_path.name}",
            )
            with self.subTest(case=py_path.stem):
                result = self.assert_snapshot_matches(py_path, json_path)
                self.assertTrue(result.matched)

    def test_snapshot_regex_field_matcher(self):
        """Verify explicit {'$regex': ...} field patterns work inside stripped JSON templates."""
        code = """
import PvZ_Fusion_Transpiler as pft
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text(5)
"""
        with open(CASES_DIR / "01_display_text.json", "r", encoding="utf-8") as f:
            tmpl = json.load(f)

        # Replace ShowTextNode.displayText exact string with a regex pattern matcher
        for item in tmpl["references"]["RefIds"]:
            if item["type"]["class"] == "ShowTextNode":
                item["data"]["displayText"] = {"$regex": "^示.*本$"}

        res = assert_snapshot_matches(code, tmpl)
        self.assertTrue(res.matched)

        # Now ensure non-matching regex fails cleanly
        tmpl_bad = copy.deepcopy(tmpl)
        for item in tmpl_bad["references"]["RefIds"]:
            if item["type"]["class"] == "ShowTextNode":
                item["data"]["displayText"] = {"$regex": "^DoesNotMatch.*"}

        with self.assertRaises(AssertionError) as ctx:
            assert_snapshot_matches(code, tmpl_bad)
        self.assertIn("FAIL (MISMATCH)", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
