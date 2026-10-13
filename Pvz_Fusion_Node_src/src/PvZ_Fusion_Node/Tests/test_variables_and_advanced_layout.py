import os
import sys
import unittest
import math

_src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

import PvZ_Fusion_Node as pvn
from PvZ_Fusion_Node import (
    Trigger,
    Print,
    IntVar,
    FloatVar,
    BoolVar,
    StrVar,
    ctx,
)
from PvZ_Fusion_Node.Core.compiler import Compiler
from PvZ_Fusion_Node.Core.group import NodeGroup


class TestVariablesAndAdvancedLayout(unittest.TestCase):
    def setUp(self):
        ctx.reset()
        pvn.settings.advanced_formatting = False
        pvn.settings.group_level = 0

    def test_int_var_wiring_and_assets(self):
        """Verifies IntVar registers its asset with valid RID and wires both '变量' and '新值' ports."""
        v = IntVar(start_val=5, name="PlayerHealth")
        with Trigger.OnPlantCreate():
            v.set(20)
            Print(v.value)

        compiled = ctx.level.to_dict()

        # 1. Variables list in eventNodeGraph
        vars_list = compiled["eventNodeGraph"]["variables"]
        self.assertGreater(len(vars_list), 0, "eventNodeGraph.variables must not be empty")
        var_rid = vars_list[0]["rid"]
        self.assertIsInstance(var_rid, int)
        self.assertGreater(var_rid, 0)

        # 2. Check variable asset in references.RefIds
        ref_ids = compiled["references"]["RefIds"]
        var_refs = [r for r in ref_ids if r.get("data", {}).get("name") == "PlayerHealth"]
        self.assertEqual(len(var_refs), 1)
        var_ref = var_refs[0]
        self.assertEqual(var_ref["rid"], var_rid)
        self.assertIn("referencedNodeIds", var_ref["data"])
        self.assertGreater(len(var_ref["data"]["referencedNodeIds"]), 0)

        # 3. Check connections
        connections = compiled["eventNodeGraph"]["connections"]
        # Dummy connection at index 0
        self.assertEqual(connections[0], {"sourceNodeId": "", "sourcePortName": "", "targetNodeId": "", "targetPortName": ""})

        # Find connections on "变量" and "新值"
        var_conns = [c for c in connections if c.get("sourcePortName") == "变量" and c.get("targetPortName") == "变量"]
        new_val_conns = [c for c in connections if c.get("targetPortName") == "新值"]

        self.assertGreater(len(var_conns), 0, "At least one '变量' port connection must exist")
        self.assertGreater(len(new_val_conns), 0, "At least one '新值' port connection must exist")

    def test_float_bool_str_var_wiring(self):
        """Verifies FloatVar, BoolVar, and StrVar wire ports and register assets."""
        f = FloatVar(start_val=3.14, name="Pi")
        b = BoolVar(start_val=True, name="IsActive")
        s = StrVar(start_val="PvZ", name="GameName")

        with Trigger.OnBoardStart():
            f.set(6.28)
            b.set(False)
            s.set("Fusion")
            Print(f.value)
            Print(b.value)
            Print(s.value)

        compiled = ctx.level.to_dict()
        vars_list = compiled["eventNodeGraph"]["variables"]
        self.assertEqual(len(vars_list), 3, "All 3 variables must be listed in eventNodeGraph.variables")

        connections = compiled["eventNodeGraph"]["connections"]
        var_port_conns = [c for c in connections if c.get("sourcePortName") == "变量" and c.get("targetPortName") == "变量"]
        self.assertGreaterEqual(len(var_port_conns), 3, "Each variable must connect to its Get/Set node '变量' ports")

    def test_square_pattern_layout_group_level_0(self):
        """Verifies square pattern grid when advanced_formatting=False and group_level=0."""
        pvn.settings.advanced_formatting = False
        pvn.settings.group_level = 0

        # Create 9 nodes
        created = [pvn.nodes.int_value(val=i) for i in range(9)]

        compiler = Compiler(auto_layout=True)
        compiler.compile(ctx.level)

        # 9 nodes in square grid: cols = ceil(sqrt(9)) = 3, rows = 3
        # Check positions
        xs = sorted(list({round(n.position_x, 1) for n in created}))
        ys = sorted(list({round(n.position_y, 1) for n in created}))
        self.assertEqual(len(xs), 3, f"Expected 3 distinct columns, got {len(xs)}")
        self.assertEqual(len(ys), 3, f"Expected 3 distinct rows, got {len(ys)}")

    def test_square_pattern_layout_group_level_1(self):
        """Verifies square pattern layout for both nodes within groups and groups across canvas."""
        pvn.settings.advanced_formatting = False
        pvn.settings.group_level = 1

        # Create 4 groups with 4 nodes each
        all_nodes = []
        for g_idx in range(4):
            grp_nodes = [pvn.nodes.int_value(val=g_idx * 10 + i) for i in range(4)]
            grp = NodeGroup(title=f"Group_{g_idx}", node_ids=[n.node_id for n in grp_nodes])
            ctx.level.graph.groups.append(grp)
            all_nodes.extend(grp_nodes)

        compiler = Compiler(auto_layout=True)
        compiler.compile(ctx.level)

        # In each group: 4 nodes -> cols=2, rows=2
        for grp in ctx.level.graph.groups:
            nids = grp.node_ids
            gnodes = [n for n in all_nodes if n.node_id in nids]
            g_xs = {round(n.position_x, 1) for n in gnodes}
            g_ys = {round(n.position_y, 1) for n in gnodes}
            self.assertEqual(len(g_xs), 2, "Nodes inside group must form 2 columns")
            self.assertEqual(len(g_ys), 2, "Nodes inside group must form 2 rows")

        # Across groups: 4 groups -> g_cols=2, g_rows=2
        group_centers_x = {round(g.position["x"], 1) for g in ctx.level.graph.groups}
        group_centers_y = {round(g.position["y"], 1) for g in ctx.level.graph.groups}
        self.assertEqual(len(group_centers_x), 2, "Groups across canvas must form 2 distinct X columns")
        self.assertEqual(len(group_centers_y), 2, "Groups across canvas must form 2 distinct Y rows")

    def test_advanced_formatting_layout(self):
        """Verifies advanced formatting:
        1. Non-connected node blocks are separated.
        2. Execution flows left-to-right (lower rank on left, higher rank on right).
        3. Input data providers are to the left of consumers.
        4. Connected nodes are close to each other.
        """
        pvn.settings.advanced_formatting = True
        pvn.settings.group_level = 0

        # Global Constant
        c = pvn.nodes.int_value(val=42)

        # Block 1: OnGameStart -> Print
        with Trigger.OnGameStart() as root1:
            p1 = Print("Start")

        # Block 2: OnPlantCreate -> Print
        with Trigger.OnPlantCreate() as root2:
            p2 = Print("Plant Created")

        compiler = Compiler(auto_layout=True)
        compiler.compile(ctx.level)

        # 1. Left-to-right execution in Block 1
        start_node = ctx.level.graph.node_mgr.get_node(root1.node.id)
        # Find ShowTextNode connected from start_node
        show_nodes = [n for n in ctx.level.graph.nodes if n.node_type == "ShowTextNode"]
        self.assertGreaterEqual(len(show_nodes), 2)
        print1_node = show_nodes[0]
        self.assertLess(start_node.position_x, print1_node.position_x, "Execution must flow left to right")

        # 2. Left-to-right execution in Block 2
        plant_node = ctx.level.graph.node_mgr.get_nodes_by_type("OnPlantCreateNode")[0]
        print2_node = show_nodes[1]
        self.assertLess(plant_node.position_x, print2_node.position_x, "Execution must flow left to right")




        # 3. Block separation: Block 1 and Block 2 must have distinct vertical bands
        b1_y_min = min(start_node.position_y, print1_node.position_y)
        b2_y_max = max(plant_node.position_y, print2_node.position_y)
        self.assertNotEqual(round(start_node.position_y, 0), round(plant_node.position_y, 0), "Non-connected blocks must be vertically separated")

        # 4. Global constants placed at top-left
        self.assertEqual(c.position_x, compiler.layout_engine.start_x)

    def test_constant_nodes_connection_and_dump(self):
        """Verifies IntValueNode, StringValueNode, FloatValueNode, and BoolValueNode dump value, value_PortName, and connect properly."""
        with Trigger.OnGameStart():
            Print("Hello World", duration=2.5)

        compiled = ctx.level.to_dict()
        refids = compiled["references"]["RefIds"]

        str_nodes = [r for r in refids if r.get("type", {}).get("class") == "StringValueNode"]
        float_nodes = [r for r in refids if r.get("type", {}).get("class") == "FloatValueNode"]

        self.assertGreaterEqual(len(str_nodes), 1)
        self.assertEqual(str_nodes[0]["data"]["value"], "Hello World")
        self.assertEqual(str_nodes[0]["data"]["value_PortName"], "值")

        self.assertGreaterEqual(len(float_nodes), 1)
        self.assertEqual(float_nodes[0]["data"]["value"], 2.5)
        self.assertEqual(float_nodes[0]["data"]["value_PortName"], "值")

        # Check ShowTextNode connections
        show_nodes = [r for r in refids if r.get("type", {}).get("class") == "ShowTextNode"]
        self.assertEqual(len(show_nodes), 1)
        show_id = show_nodes[0]["data"]["nodeId"]

        conns = compiled["eventNodeGraph"]["connections"]
        text_conns = [c for c in conns if c["targetNodeId"] == show_id and c["targetPortName"] == "文本"]
        dur_conns = [c for c in conns if c["targetNodeId"] == show_id and c["targetPortName"] == "持续时间"]

        self.assertEqual(len(text_conns), 1, "ShowTextNode must have an incoming connection on '文本' port")
        self.assertEqual(text_conns[0]["sourcePortName"], "值")
        self.assertEqual(text_conns[0]["sourceNodeId"], str_nodes[0]["data"]["nodeId"])

        self.assertEqual(len(dur_conns), 1, "ShowTextNode must have an incoming connection on '持续时间' port")
        self.assertEqual(dur_conns[0]["sourcePortName"], "值")
        self.assertEqual(dur_conns[0]["sourceNodeId"], float_nodes[0]["data"]["nodeId"])

    def test_connected_constants_placed_immediately_behind_consumers(self):
        """Verifies that in advanced formatting, connected constant nodes are placed directly to the left (behind) the consumer."""
        pvn.settings.advanced_formatting = True
        with Trigger.OnGameStart() as start:
            show = Print("Sample Msg", duration=1.5)

        compiler = Compiler(auto_layout=True)
        compiler.compile(ctx.level)

        compiled = ctx.level.to_dict()
        refids = {r["data"]["nodeId"]: r for r in compiled["references"]["RefIds"] if "data" in r and "nodeId" in r["data"]}

        show_node = [r for r in refids.values() if r.get("type", {}).get("class") == "ShowTextNode"][0]
        show_x = show_node["data"]["position"]["x"]
        show_y = show_node["data"]["position"]["y"]

        # Constants feeding into show_node
        str_node = [r for r in refids.values() if r.get("type", {}).get("class") == "StringValueNode"][0]
        float_node = [r for r in refids.values() if r.get("type", {}).get("class") == "FloatValueNode"][0]

        str_x = str_node["data"]["position"]["x"]
        str_y = str_node["data"]["position"]["y"]

        float_x = float_node["data"]["position"]["x"]
        float_y = float_node["data"]["position"]["y"]

        expected_const_x = show_x - (compiler.layout_engine.node_width + compiler.layout_engine.horizontal_gap)
        self.assertEqual(round(str_x, 1), round(expected_const_x, 1), "String constant must be directly in the column to the left of ShowTextNode")
        self.assertEqual(round(float_x, 1), round(expected_const_x, 1), "Float duration constant must be directly in the column to the left of ShowTextNode")

        # They must be near show_y vertically (not far away in a separate tower)
        self.assertLess(abs(str_y - show_y), 300.0, "String constant must be vertically close to consumer")
        self.assertLess(abs(float_y - show_y), 300.0, "Float constant must be vertically close to consumer")

    def test_get_variable_and_type_convert_connections(self):
        """Verifies that GetIntVariableValue, IntToFloat, and FloatToString connect all input/output wires."""
        v = IntVar(name="my_test_var")
        s = v.to_string(decimals=0)

        conns = ctx.level.graph.connection_mgr.connections
        node_mgr = ctx.level.graph.node_mgr

        conn_pairs = []
        for c in conns:
            src = node_mgr.get_node(c.sourceNodeId)
            dst = node_mgr.get_node(c.targetNodeId)
            if src and dst:
                conn_pairs.append((src.node_type, c.sourcePortName, dst.node_type, c.targetPortName))

        self.assertIn(
            ("IntVariableNode", "变量", "GetIntVariableValueNode", "变量"),
            conn_pairs,
            "IntVariableNode must connect to GetIntVariableValueNode"
        )
        self.assertIn(
            ("GetIntVariableValueNode", "值", "IntToFloatNode", "整数"),
            conn_pairs,
            "GetIntVariableValueNode must connect to IntToFloatNode"
        )
        self.assertIn(
            ("IntToFloatNode", "浮点数", "FloatToStringNode", "数值"),
            conn_pairs,
            "IntToFloatNode must connect to FloatToStringNode"
        )
        self.assertIn(
            ("IntValueNode", "值", "FloatToStringNode", "小数位数"),
            conn_pairs,
            "IntValueNode (decimals) must connect to FloatToStringNode"
        )

    def test_float_to_int_and_math_floor_connections(self):
        """Verifies that Math.floor and FloatToInt connect variables and conversion nodes properly."""
        from PvZ_Fusion_Node import Math
        f = FloatVar(name="float_test")
        fl = Math.floor(f)

        conns = ctx.level.graph.connection_mgr.connections
        node_mgr = ctx.level.graph.node_mgr

        conn_pairs = []
        for c in conns:
            src = node_mgr.get_node(c.sourceNodeId)
            dst = node_mgr.get_node(c.targetNodeId)
            if src and dst:
                conn_pairs.append((src.node_type, c.sourcePortName, dst.node_type, c.targetPortName))

        self.assertIn(
            ("FloatVariableNode", "变量", "GetFloatVariableValueNode", "变量"),
            conn_pairs,
            "FloatVariableNode must connect to GetFloatVariableValueNode"
        )
        self.assertIn(
            ("GetFloatVariableValueNode", "值", "FloatToIntNode", "浮点数"),
            conn_pairs,
            "GetFloatVariableValueNode must connect to FloatToIntNode"
        )
        self.assertIn(
            ("FloatToIntNode", "整数", "IntToFloatNode", "整数"),
            conn_pairs,
            "FloatToIntNode must connect to IntToFloatNode"
        )


if __name__ == "__main__":
    unittest.main()

