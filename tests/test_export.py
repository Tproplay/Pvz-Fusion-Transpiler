import json
import os
import shutil
import subprocess
import sys
import unittest

from PvZ_Fusion_Transpiler.Core import Config, _ctx, export, ConnectionManager
from PvZ_Fusion_Transpiler.Core.connection_manager import PortDirection, PortType
from PvZ_Fusion_Transpiler._Nodes import (
    OnGameStartNode,
    ShowTextNode,
    CompareIntNode,
    GetMouseWorldPositionNode,
    Node,
)


class TestExportSystem(unittest.TestCase):
    def setUp(self):
        _ctx.clear()
        self.test_dir = os.path.abspath("./tests_output_tmp")
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        _ctx.clear()
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_config_function(self):
        """Test that Config updates _ctx.config properly."""
        Config(output=self.test_dir, name="CustomLevel")
        self.assertEqual(_ctx.config["output"], self.test_dir)
        self.assertEqual(_ctx.config["name"], "CustomLevel")

        # Test defaults
        Config()
        self.assertEqual(_ctx.config["output"], "./")
        self.assertEqual(_ctx.config["name"], "Untitled")

    def test_node_auto_registration(self):
        """Test that instantiating nodes automatically registers them in _ctx."""
        self.assertEqual(len(_ctx.nodes), 0)
        start = OnGameStartNode()
        text = ShowTextNode()
        self.assertEqual(len(_ctx.nodes), 2)
        self.assertIn(start, _ctx.nodes)
        self.assertIn(text, _ctx.nodes)
        self.assertTrue(hasattr(start, "id"))
        self.assertTrue(hasattr(text, "id"))
        self.assertNotEqual(start.id, text.id)

    def test_connection_wiring(self):
        """Test port connection wiring and direction normalization."""
        start = OnGameStartNode()
        text = ShowTextNode()

        # Connect Output to Input
        start.port_output_trigger_Trigger.connect(text.port_input_trigger_Trigger)
        conns = ConnectionManager.get_connections()
        self.assertEqual(len(conns), 1)
        self.assertEqual(conns[0].source_node, start)
        self.assertEqual(conns[0].target_node, text)
        self.assertEqual(conns[0].source_port.name, "触发")
        self.assertEqual(conns[0].target_port.name, "触发")

        conn_dict = conns[0].to_dict()
        self.assertEqual(conn_dict["sourceNodeId"], start.id)
        self.assertEqual(conn_dict["sourcePortName"], "触发")
        self.assertEqual(conn_dict["targetNodeId"], text.id)
        self.assertEqual(conn_dict["targetPortName"], "触发")

    def test_connection_inverse_wiring(self):
        """Test connecting Input to Output normalizes so Output is source."""
        start = OnGameStartNode()
        text = ShowTextNode()

        # Connect Input to Output
        text.port_input_trigger_Trigger.connect(start.port_output_trigger_Trigger)
        conns = ConnectionManager.get_connections()
        self.assertEqual(len(conns), 1)
        self.assertEqual(conns[0].source_node, start)
        self.assertEqual(conns[0].target_node, text)

    def test_export_new_level(self):
        """Test exporting a level to a new JSON file."""
        Config(output=self.test_dir, name="BrandNewLevel")
        start = OnGameStartNode()
        text = ShowTextNode()
        start.port_output_trigger_Trigger.connect(text.port_input_trigger_Trigger)

        exported_path = export()
        expected_path = os.path.join(self.test_dir, "BrandNewLevel.json")
        self.assertEqual(os.path.abspath(exported_path), os.path.abspath(expected_path))
        self.assertTrue(os.path.isfile(expected_path))

        with open(expected_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(set(data.keys()), {"eventNodeGraph", "references"})

        # Check nodes
        graph_nodes = data["eventNodeGraph"]["nodes"]
        self.assertEqual(len(graph_nodes), 2)
        self.assertEqual(graph_nodes[0]["rid"], 1000)
        self.assertEqual(graph_nodes[1]["rid"], 1001)

        # Check connections: index 0 must be dummy
        connections = data["eventNodeGraph"]["connections"]
        self.assertEqual(len(connections), 2)
        self.assertEqual(connections[0], {
            "sourceNodeId": "",
            "sourcePortName": "",
            "targetNodeId": "",
            "targetPortName": "",
        })
        self.assertEqual(connections[1]["sourceNodeId"], start.id)
        self.assertEqual(connections[1]["sourcePortName"], "触发")
        self.assertEqual(connections[1]["targetNodeId"], text.id)
        self.assertEqual(connections[1]["targetPortName"], "触发")

        # Check references
        ref_ids = data["references"]["RefIds"]
        self.assertEqual(len(ref_ids), 2)
        self.assertEqual(ref_ids[0]["rid"], 1000)
        self.assertEqual(ref_ids[0]["type"]["class"], "OnGameStartNode")
        self.assertEqual(ref_ids[0]["data"]["nodeId"], start.id)
        self.assertEqual(ref_ids[0]["data"]["trigger_PortName"], "触发")

        self.assertEqual(ref_ids[1]["rid"], 1001)
        self.assertEqual(ref_ids[1]["type"]["class"], "ShowTextNode")
        self.assertEqual(ref_ids[1]["data"]["nodeId"], text.id)
        self.assertEqual(ref_ids[1]["data"]["trigger_PortName"], "触发")
        self.assertEqual(ref_ids[1]["data"]["text_PortName"], "文本")
        self.assertEqual(ref_ids[1]["data"]["duration_PortName"], "持续时间")

    def test_square_pattern_layout(self):
        """Test that nodes are arranged in a square pattern (ceil(sqrt(N)) columns)."""
        Config(output=self.test_dir, name="SquareLayoutTest")
        n1 = OnGameStartNode()
        n2 = ShowTextNode()
        n3 = CompareIntNode()
        n4 = GetMouseWorldPositionNode()

        export()
        file_path = os.path.join(self.test_dir, "SquareLayoutTest.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        ref_ids = data["references"]["RefIds"]
        self.assertEqual(len(ref_ids), 4)

        # 4 nodes -> cols = 2
        # (c=0, r=0): x = -800.0, y = 400.0
        # (c=1, r=0): x = -560.0, y = 400.0
        # (c=0, r=1): x = -800.0, y = 240.0
        # (c=1, r=1): x = -560.0, y = 240.0
        self.assertEqual(ref_ids[0]["data"]["position"], {"x": -800.0, "y": 400.0})
        self.assertEqual(ref_ids[1]["data"]["position"], {"x": -560.0, "y": 400.0})
        self.assertEqual(ref_ids[2]["data"]["position"], {"x": -800.0, "y": 240.0})
        self.assertEqual(ref_ids[3]["data"]["position"], {"x": -560.0, "y": 240.0})

    def test_export_overwrite_existing_level(self):
        """Test that if file already exists, its NodeGraph and Connections are overwritten while other fields are preserved."""
        file_path = os.path.join(self.test_dir, "ExistingLevel.json")
        initial_content = {
            "name": "ExistingLevel",
            "startSun": 12345,
            "maxWave": 99,
            "cardCount": 20,
            "scaryPots": ["pot1", "pot2"],
            "boardConfig": {"customValue": 42},
            "eventNodeGraph": {
                "nodes": [{"rid": 500}],
                "connections": [{"sourceNodeId": "old", "sourcePortName": "old", "targetNodeId": "old", "targetPortName": "old"}],
                "executionVersion": 3,
                "graphId": "existing-graph-id-777",
            },
            "references": {
                "version": 2,
                "RefIds": [{"rid": 500, "type": {}, "data": {}}],
            },
        }
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(initial_content, f)

        # Configure to target the existing file
        Config(output=self.test_dir, name="ExistingLevel")
        cmp_node = CompareIntNode()
        mouse_node = GetMouseWorldPositionNode()

        export()

        with open(file_path, "r", encoding="utf-8") as f:
            updated = json.load(f)

        # Check preserved level configuration fields
        self.assertEqual(updated["startSun"], 12345)
        self.assertEqual(updated["maxWave"], 99)
        self.assertEqual(updated["cardCount"], 20)
        self.assertEqual(updated["scaryPots"], ["pot1", "pot2"])
        self.assertEqual(updated["boardConfig"], {"customValue": 42})
        self.assertEqual(updated["eventNodeGraph"]["graphId"], "existing-graph-id-777")
        self.assertEqual(updated["eventNodeGraph"]["executionVersion"], 3)

        # Check overwritten NodeGraph and Connections
        self.assertEqual(len(updated["eventNodeGraph"]["nodes"]), 2)
        self.assertEqual(updated["eventNodeGraph"]["nodes"][0]["rid"], 1000)
        self.assertEqual(updated["eventNodeGraph"]["nodes"][1]["rid"], 1001)

        # Only dummy connection because none were wired
        self.assertEqual(len(updated["eventNodeGraph"]["connections"]), 1)
        self.assertEqual(updated["eventNodeGraph"]["connections"][0]["sourceNodeId"], "")

        # References updated
        self.assertEqual(len(updated["references"]["RefIds"]), 2)
        self.assertEqual(updated["references"]["RefIds"][0]["type"]["class"], "CompareIntNode")
        self.assertEqual(updated["references"]["RefIds"][1]["type"]["class"], "GetMouseWorldPositionNode")

    def test_auto_export_subprocess(self):
        """Test that a script automatically exports via atexit without calling export() explicitly."""
        script_path = os.path.join(self.test_dir, "run_script.py")
        code = f"""
import sys
from PvZ_Fusion_Transpiler.Core import Config
from PvZ_Fusion_Transpiler._Nodes import OnGameStartNode, ShowTextNode

Config(output=r"{self.test_dir}", name="AutoExported")
start = OnGameStartNode()
text = ShowTextNode()
start.port_output_trigger_Trigger.connect(text.port_input_trigger_Trigger)
"""
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(code)

        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr}")

        exported_file = os.path.join(self.test_dir, "AutoExported.json")
        self.assertTrue(os.path.isfile(exported_file), "File was not auto-exported on exit!")

        with open(exported_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data["eventNodeGraph"]["nodes"]), 2)
        self.assertEqual(len(data["eventNodeGraph"]["connections"]), 2)

    def test_auto_export_skip_on_script_error(self):
        """Test that atexit does not export if script terminates due to an unhandled exception."""
        script_path = os.path.join(self.test_dir, "crash_script.py")
        code = f"""
import sys
from PvZ_Fusion_Transpiler.Core import Config
from PvZ_Fusion_Transpiler._Nodes import OnGameStartNode

Config(output=r"{self.test_dir}", name="ShouldNotExist")
start = OnGameStartNode()
raise RuntimeError("Intentional error to test exception handling")
"""
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(code)

        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)

        exported_file = os.path.join(self.test_dir, "ShouldNotExist.json")
        self.assertFalse(os.path.exists(exported_file), "File should not be exported when script crashes!")


if __name__ == "__main__":
    unittest.main()
