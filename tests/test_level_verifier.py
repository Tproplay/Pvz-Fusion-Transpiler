import os
import unittest
from pathlib import Path
from tools.level_verifier import (
    LevelGraph,
    LevelTestCase,
    LevelVerifier,
    assert_level_matches,
)
import PvZ_Fusion_Transpiler as pft


REPO_ROOT = Path(__file__).resolve().parent.parent
BIN_TEST_PY = REPO_ROOT / "bin" / "test.py"
APP_DATA_TEST_JSON = Path(
    r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels\Test.json"
)


class TestLevelVerifierSystem(LevelTestCase):
    """Test suite for the automated level graph and optimization verifier."""

    def test_bin_test_py_matches_exported_level(self):
        """Verify that bin/test.py generates the exact graph exported in Test.json."""
        if not APP_DATA_TEST_JSON.is_file():
            self.skipTest(f"Test.json not found at {APP_DATA_TEST_JSON}")

        result = self.assert_level_matches(
            code_or_file=BIN_TEST_PY,
            expected_level_or_file=APP_DATA_TEST_JSON,
            check_payloads=True,
        )
        self.assertTrue(result.matched)
        self.assertEqual(len(result.missing_nodes), 0)
        self.assertEqual(len(result.missing_connections), 0)
        self.assertEqual(len(result.property_mismatches), 0)

    def test_inline_code_string_matches_exported_level(self):
        """Verify that equivalent inline Python code matches Test.json."""
        if not APP_DATA_TEST_JSON.is_file():
            self.skipTest(f"Test.json not found at {APP_DATA_TEST_JSON}")

        code = """
import PvZ_Fusion_Transpiler as pft
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text(5)
"""
        result = assert_level_matches(code, APP_DATA_TEST_JSON)
        self.assertTrue(result.matched)

    def test_callable_function_matches(self):
        """Verify that passing a Python builder function matches Test.json."""
        if not APP_DATA_TEST_JSON.is_file():
            self.skipTest(f"Test.json not found at {APP_DATA_TEST_JSON}")

        def build_level():
            with pft.Trigger.OnGameStart():
                pft.InGameUI.display_text(5)

        result = assert_level_matches(build_level, APP_DATA_TEST_JSON)
        self.assertTrue(result.matched)

    def test_detects_value_property_mismatch(self):
        """Verify that an incorrect parameter value is detected with pinpoint diagnostics."""
        if not APP_DATA_TEST_JSON.is_file():
            self.skipTest(f"Test.json not found at {APP_DATA_TEST_JSON}")

        code = """
import PvZ_Fusion_Transpiler as pft
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text(999)
"""
        with self.assertRaises(AssertionError) as ctx:
            assert_level_matches(code, APP_DATA_TEST_JSON)

        err_msg = str(ctx.exception)
        self.assertIn("FAIL (MISMATCH)", err_msg)
        self.assertIn("IntValueNode.value", err_msg)
        self.assertIn("999", err_msg)

    def test_detects_disconnected_trigger_and_unreached_node(self):
        """Verify that omitting a trigger block flags missing connection and unreached node."""
        if not APP_DATA_TEST_JSON.is_file():
            self.skipTest(f"Test.json not found at {APP_DATA_TEST_JSON}")

        code = """
import PvZ_Fusion_Transpiler as pft
# Intentionally disconnected:
pft.Trigger.OnGameStart()
pft.InGameUI.display_text(5)
"""
        with self.assertRaises(AssertionError) as ctx:
            assert_level_matches(code, APP_DATA_TEST_JSON)

        err_msg = str(ctx.exception)
        self.assertIn("Missing Connections", err_msg)
        self.assertIn("OnGameStartNode", err_msg)
        self.assertIn("FLOATING_NODE", err_msg)
        self.assertIn("UNREACHED_NODE", err_msg)

    def test_optimization_analysis_finds_redundant_constants(self):
        """Verify that multiple duplicate constant nodes are flagged for deduplication."""
        code = """
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.nodes import int_value

val1 = int_value(42)
val2 = int_value(42)
"""
        graph = LevelGraph.from_code(code)
        findings = graph.analyze_optimizations()
        redundant = [f for f in findings if f.kind == "REDUNDANT_CONSTANT"]
        self.assertEqual(len(redundant), 1)
        self.assertIn("Multiple IntValueNode nodes (2) found with value 42", redundant[0].message)


if __name__ == "__main__":
    unittest.main()
