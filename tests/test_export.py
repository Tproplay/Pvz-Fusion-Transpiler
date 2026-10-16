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
    IntValueNode,
    FloatValueNode,
    BoolValueNode,
    StringValueNode,
    IntVariableNode,
    FloatVariableNode,
    BoolVariableNode,
    StringVariableNode,
    VariableAsset,
    IntVariableAsset,
    FloatVariableAsset,
    BoolVariableAsset,
    StringVariableAsset,
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
        self.assertEqual(os.path.abspath(exported_path), os.path.abspath(expected_path)) #type: ignore
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

    def test_value_nodes_export(self):
        """Test value nodes (Int, Float, Bool, String) serialize value and value_PortName."""
        Config(output=self.test_dir, name="ValueNodesTest")
        int_n = IntValueNode(value=42)
        float_n = FloatValueNode(value=3.14)
        bool_n = BoolValueNode(value=True)
        str_n = StringValueNode(value="CustomString")

        export()
        file_path = os.path.join(self.test_dir, "ValueNodesTest.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        ref_ids = data["references"]["RefIds"]
        self.assertEqual(len(ref_ids), 4)

        # IntValueNode
        self.assertEqual(ref_ids[0]["type"]["class"], "IntValueNode")
        self.assertEqual(ref_ids[0]["data"]["value"], 42)
        self.assertEqual(ref_ids[0]["data"]["value_PortName"], "值")

        # FloatValueNode
        self.assertEqual(ref_ids[1]["type"]["class"], "FloatValueNode")
        self.assertAlmostEqual(ref_ids[1]["data"]["value"], 3.14)
        self.assertEqual(ref_ids[1]["data"]["value_PortName"], "值")

        # BoolValueNode
        self.assertEqual(ref_ids[2]["type"]["class"], "BoolValueNode")
        self.assertEqual(ref_ids[2]["data"]["value"], True)
        self.assertEqual(ref_ids[2]["data"]["value_PortName"], "值")

        # StringValueNode
        self.assertEqual(ref_ids[3]["type"]["class"], "StringValueNode")
        self.assertEqual(ref_ids[3]["data"]["value"], "CustomString")
        self.assertEqual(ref_ids[3]["data"]["value_PortName"], "值")

    def test_variable_nodes_and_assets_export(self):
        """Test variable nodes and variable assets linking, RID assignment, and referencedNodeIds."""
        Config(output=self.test_dir, name="VariablesTest")

        # Shared asset
        shared_int = IntVariableAsset(name="共享整数", initial_value=100)
        n1 = IntVariableNode(asset=shared_int)
        n2 = IntVariableNode(asset=shared_int)

        # Dedicated asset node
        n3 = IntVariableNode(name="独立整数", value=200)

        # Standalone unreferenced asset
        f_asset = FloatVariableAsset(name="未引用浮点", initial_value=9.99)

        export()
        file_path = os.path.join(self.test_dir, "VariablesTest.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Graph should have 3 nodes and 3 variables
        self.assertEqual(len(data["eventNodeGraph"]["nodes"]), 3)
        self.assertEqual(len(data["eventNodeGraph"]["variables"]), 3)
        self.assertEqual(data["eventNodeGraph"]["nodes"], [{"rid": 1000}, {"rid": 1001}, {"rid": 1002}])
        self.assertEqual(data["eventNodeGraph"]["variables"], [{"rid": 1003}, {"rid": 1004}, {"rid": 1005}])

        # References
        ref_ids = data["references"]["RefIds"]
        self.assertEqual(len(ref_ids), 6)

        # Node 1 and Node 2 point to shared asset rid 1003
        self.assertEqual(ref_ids[0]["rid"], 1000)
        self.assertEqual(ref_ids[0]["data"]["asset"]["rid"], 1003)
        self.assertEqual(ref_ids[0]["data"]["variable_PortName"], "变量")

        self.assertEqual(ref_ids[1]["rid"], 1001)
        self.assertEqual(ref_ids[1]["data"]["asset"]["rid"], 1003)
        self.assertEqual(ref_ids[1]["data"]["variable_PortName"], "变量")

        # Node 3 points to dedicated asset rid 1004
        self.assertEqual(ref_ids[2]["rid"], 1002)
        self.assertEqual(ref_ids[2]["data"]["asset"]["rid"], 1004)
        self.assertEqual(ref_ids[2]["data"]["variable_PortName"], "变量")

        # Shared asset has both n1.id and n2.id in referencedNodeIds
        self.assertEqual(ref_ids[3]["rid"], 1003)
        self.assertEqual(ref_ids[3]["type"]["class"], "IntVariableAsset")
        self.assertEqual(ref_ids[3]["data"]["name"], "共享整数")
        self.assertEqual(ref_ids[3]["data"]["value"], 100)
        self.assertCountEqual(ref_ids[3]["data"]["referencedNodeIds"], [n1.id, n2.id])

        # Dedicated asset has n3.id in referencedNodeIds
        self.assertEqual(ref_ids[4]["rid"], 1004)
        self.assertEqual(ref_ids[4]["type"]["class"], "IntVariableAsset")
        self.assertEqual(ref_ids[4]["data"]["name"], "独立整数")
        self.assertEqual(ref_ids[4]["data"]["value"], 200)
        self.assertEqual(ref_ids[4]["data"]["referencedNodeIds"], [n3.id])

        # Unreferenced asset has empty referencedNodeIds
        self.assertEqual(ref_ids[5]["rid"], 1005)
        self.assertEqual(ref_ids[5]["type"]["class"], "FloatVariableAsset")
        self.assertEqual(ref_ids[5]["data"]["name"], "未引用浮点")
        self.assertAlmostEqual(ref_ids[5]["data"]["value"], 9.99)
        self.assertEqual(ref_ids[5]["data"]["referencedNodeIds"], [])

    def test_all_typed_variable_nodes(self):
        """Test FloatVariableNode, BoolVariableNode, StringVariableNode."""
        Config(output=self.test_dir, name="AllTypedVarsTest")
        fn = FloatVariableNode(name="我的浮点", value=12.5)
        bn = BoolVariableNode(name="我的布尔", value=True)
        sn = StringVariableNode(name="我的文本", value="PvZ Fusion")

        export()
        file_path = os.path.join(self.test_dir, "AllTypedVarsTest.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        ref_ids = data["references"]["RefIds"]
        self.assertEqual(len(ref_ids), 6)  # 3 nodes + 3 assets

        # Assets
        asset_f = ref_ids[3]
        self.assertEqual(asset_f["type"]["class"], "FloatVariableAsset")
        self.assertEqual(asset_f["data"]["name"], "我的浮点")
        self.assertAlmostEqual(asset_f["data"]["value"], 12.5)
        self.assertEqual(asset_f["data"]["referencedNodeIds"], [fn.id])

        asset_b = ref_ids[4]
        self.assertEqual(asset_b["type"]["class"], "BoolVariableAsset")
        self.assertEqual(asset_b["data"]["name"], "我的布尔")
        self.assertEqual(asset_b["data"]["value"], True)
        self.assertEqual(asset_b["data"]["referencedNodeIds"], [bn.id])

        asset_s = ref_ids[5]
        self.assertEqual(asset_s["type"]["class"], "StringVariableAsset")
        self.assertEqual(asset_s["data"]["name"], "我的文本")
        self.assertEqual(asset_s["data"]["value"], "PvZ Fusion")
        self.assertEqual(asset_s["data"]["referencedNodeIds"], [sn.id])

    def test_string_fields_export(self):
        """Test dumping string fields like bindingName and stageName matching Test.json."""
        from PvZ_Fusion_Transpiler._Nodes import (
            BindPlantNode,
            ChangeStageNode,
            OnStageEnterNode,
            GetBoundZombieNode,
        )

        Config(output=self.test_dir, name="StringFieldsTest")
        bp1 = BindPlantNode()  # default "守护目标"
        bp2 = BindPlantNode(bindingName="守护VIP")
        cs1 = ChangeStageNode()  # default "战斗"
        cs2 = ChangeStageNode(stage_name="最终对决")
        ose = OnStageEnterNode(stage_name="阶段二")
        gbz = GetBoundZombieNode(binding_name="僵尸王")

        export()
        file_path = os.path.join(self.test_dir, "StringFieldsTest.json")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        ref_ids = data["references"]["RefIds"]
        self.assertEqual(len(ref_ids), 6)

        # bp1: BindPlantNode default
        self.assertEqual(ref_ids[0]["data"]["bindingName"], "守护目标")
        self.assertNotIn("trigger_PortName", ref_ids[0]["data"])
        self.assertNotIn("plant_PortName", ref_ids[0]["data"])

        # bp2: BindPlantNode custom
        self.assertEqual(ref_ids[1]["data"]["bindingName"], "守护VIP")

        # cs1: ChangeStageNode default
        self.assertEqual(ref_ids[2]["data"]["stageName"], "战斗")
        self.assertNotIn("trigger_PortName", ref_ids[2]["data"])

        # cs2: ChangeStageNode custom
        self.assertEqual(ref_ids[3]["data"]["stageName"], "最终对决")

        # ose: OnStageEnterNode
        self.assertEqual(ref_ids[4]["data"]["stageName"], "阶段二")

        # gbz: GetBoundZombieNode
        self.assertEqual(ref_ids[5]["data"]["bindingName"], "僵尸王")


if __name__ == "__main__":
    unittest.main()

