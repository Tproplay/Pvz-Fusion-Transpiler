import unittest
from pathlib import Path
from tools.level_verifier import (
    LevelGraph,
    LevelTestCase,
    assert_level_matches,
)
import PvZ_Fusion_Transpiler as pft


REPO_ROOT = Path(__file__).resolve().parent.parent
BIN_TEST_PY = REPO_ROOT / "bin" / "test.py"
APP_DATA_TEST_JSON = Path(
    r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels\Test.json"
)


DISPLAY_TEXT_FIXTURE = {
    "eventNodeGraph": {
        "nodes": [{"rid": 1000}, {"rid": 1001}, {"rid": 1002}, {"rid": 1003}, {"rid": 1004}],
        "connections": [
            {"sourceNodeId": "", "sourcePortName": "", "targetNodeId": "", "targetPortName": ""},
            {"sourceNodeId": "int-id", "sourcePortName": "值", "targetNodeId": "conv-id", "targetPortName": "Value"},
            {"sourceNodeId": "start-id", "sourcePortName": "触发", "targetNodeId": "show-id", "targetPortName": "触发"},
            {"sourceNodeId": "conv-id", "sourcePortName": "String", "targetNodeId": "show-id", "targetPortName": "文本"},
            {"sourceNodeId": "flt-id", "sourcePortName": "值", "targetNodeId": "show-id", "targetPortName": "持续时间"},
        ],
        "variables": [],
    },
    "references": {
        "version": 2,
        "RefIds": [
            {"rid": 1000, "type": {"class": "OnGameStartNode"}, "data": {"nodeId": "start-id", "nodeType": "OnGameStartNode"}},
            {"rid": 1001, "type": {"class": "IntValueNode"}, "data": {"nodeId": "int-id", "nodeType": "IntValueNode", "value": 5}},
            {"rid": 1002, "type": {"class": "IntToStringNode"}, "data": {"nodeId": "conv-id", "nodeType": "IntToStringNode"}},
            {"rid": 1003, "type": {"class": "ShowTextNode"}, "data": {"nodeId": "show-id", "nodeType": "ShowTextNode", "displayText": "示例文本"}},
            {"rid": 1004, "type": {"class": "FloatValueNode"}, "data": {"nodeId": "flt-id", "nodeType": "FloatValueNode", "value": 3.0}},
        ],
    },
}


VAR_ARITHMETIC_FIXTURE = {
    "eventNodeGraph": {
        "nodes": [
            {"rid": 1000}, {"rid": 1001}, {"rid": 1002},
            {"rid": 1003}, {"rid": 1004}, {"rid": 1005}, {"rid": 1006},
        ],
        "connections": [
            {"sourceNodeId": "", "sourcePortName": "", "targetNodeId": "", "targetPortName": ""},
            {"sourceNodeId": "var-id", "sourcePortName": "变量", "targetNodeId": "get-id", "targetPortName": "变量"},
            {"sourceNodeId": "get-id", "sourcePortName": "值", "targetNodeId": "mul-id", "targetPortName": "A"},
            {"sourceNodeId": "int5-id", "sourcePortName": "值", "targetNodeId": "mul-id", "targetPortName": "B"},
            {"sourceNodeId": "mul-id", "sourcePortName": "积", "targetNodeId": "i2f-id", "targetPortName": "Integer"},
            {"sourceNodeId": "i2f-id", "sourcePortName": "Float", "targetNodeId": "div-id", "targetPortName": "被除数"},
            {"sourceNodeId": "flt2-id", "sourcePortName": "值", "targetNodeId": "div-id", "targetPortName": "除数"},
        ],
        "variables": [{"rid": 1007}],
    },
    "references": {
        "version": 2,
        "RefIds": [
            {"rid": 1000, "type": {"class": "IntVariableNode"}, "data": {"nodeId": "var-id", "nodeType": "IntVariableNode", "asset": {"rid": 1007}}},
            {"rid": 1001, "type": {"class": "GetIntVariableValueNode"}, "data": {"nodeId": "get-id", "nodeType": "GetIntVariableValueNode", "value": 0}},
            {"rid": 1002, "type": {"class": "IntMultiplyNode"}, "data": {"nodeId": "mul-id", "nodeType": "IntMultiplyNode"}},
            {"rid": 1003, "type": {"class": "IntValueNode"}, "data": {"nodeId": "int5-id", "nodeType": "IntValueNode", "value": 5}},
            {"rid": 1004, "type": {"class": "FloatValueNode"}, "data": {"nodeId": "flt2-id", "nodeType": "FloatValueNode", "value": 2.0}},
            {"rid": 1005, "type": {"class": "IntToFloatNode"}, "data": {"nodeId": "i2f-id", "nodeType": "IntToFloatNode"}},
            {"rid": 1006, "type": {"class": "DivideNode"}, "data": {"nodeId": "div-id", "nodeType": "DivideNode"}},
            {"rid": 1007, "type": {"class": "IntVariableAsset"}, "data": {"name": "Integer", "variableId": "vid", "referencedNodeIds": ["var-id"], "value": 10}},
        ],
    },
}


class TestLevelVerifierSystem(LevelTestCase):
    """Test suite for the automated level graph and optimization verifier."""

    def test_bin_test_py_matches_exported_level(self):
        """Verify that bin/test.py generates the exact graph exported in Test.json."""
        if not BIN_TEST_PY.is_file() or not APP_DATA_TEST_JSON.is_file():
            self.skipTest("bin/test.py or AppData Test.json not present")

        result = self.assert_level_matches(
            code_or_file=BIN_TEST_PY,
            expected_level_or_file=APP_DATA_TEST_JSON,
            check_payloads=True,
        )
        self.assertTrue(result.matched)
        self.assertEqual(len(result.missing_nodes), 0)
        self.assertEqual(len(result.missing_connections), 0)
        self.assertEqual(len(result.property_mismatches), 0)

    def test_display_text_graph_and_callable_match(self):
        """Verify inline Python code and callable match the frozen display_text(5) fixture."""
        code = """
import PvZ_Fusion_Transpiler as pft
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text(5)
"""
        result = assert_level_matches(code, DISPLAY_TEXT_FIXTURE)
        self.assertTrue(result.matched)

        def build_level():
            with pft.Trigger.OnGameStart():
                pft.InGameUI.display_text(5)

        result_fn = assert_level_matches(build_level, DISPLAY_TEXT_FIXTURE)
        self.assertTrue(result_fn.matched)

    def test_variable_arithmetic_graph_matches_and_validates_asset(self):
        """Verify IntVar arithmetic graph matches fixture and detects IntVariableAsset value mismatch."""
        code_ok = """
import PvZ_Fusion_Transpiler as pft
a = pft.IntVar(10)
a = a * 5
a = a / 2.0
"""
        result = self.assert_level_matches(code_ok, VAR_ARITHMETIC_FIXTURE)
        self.assertTrue(result.matched)
        self.assertEqual(len(result.missing_nodes), 0)
        self.assertEqual(len(result.missing_connections), 0)

        # Wrong initial value (99 instead of 10) must be caught on IntVariableNode.asset
        code_bad_init = """
import PvZ_Fusion_Transpiler as pft
a = pft.IntVar(99)
a = a * 5
a = a / 2.0
"""
        with self.assertRaises(AssertionError) as ctx:
            assert_level_matches(code_bad_init, VAR_ARITHMETIC_FIXTURE)
        self.assertIn("IntVariableNode.asset", str(ctx.exception))
        self.assertIn("99", str(ctx.exception))

    def test_detects_value_property_mismatch(self):
        """Verify that an incorrect parameter value is detected with pinpoint diagnostics."""
        code = """
import PvZ_Fusion_Transpiler as pft
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text(999)
"""
        with self.assertRaises(AssertionError) as ctx:
            assert_level_matches(code, DISPLAY_TEXT_FIXTURE)

        err_msg = str(ctx.exception)
        self.assertIn("FAIL (MISMATCH)", err_msg)
        self.assertIn("IntValueNode.value", err_msg)
        self.assertIn("999", err_msg)

    def test_detects_disconnected_trigger_and_unreached_node(self):
        """Verify that omitting a trigger block flags missing connection and unreached node."""
        code = """
import PvZ_Fusion_Transpiler as pft
pft.Trigger.OnGameStart()
pft.InGameUI.display_text(5)
"""
        with self.assertRaises(AssertionError) as ctx:
            assert_level_matches(code, DISPLAY_TEXT_FIXTURE)

        err_msg = str(ctx.exception)
        self.assertIn("Missing Connections", err_msg)
        self.assertIn("OnGameStartNode", err_msg)
        self.assertIn("FLOATING_NODE", err_msg)
        self.assertIn("UNREACHED_NODE", err_msg)

    def test_optimization_analysis_finds_redundant_constants(self):
        """Verify that multiple duplicate constant nodes are flagged for deduplication."""
        code = """
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
