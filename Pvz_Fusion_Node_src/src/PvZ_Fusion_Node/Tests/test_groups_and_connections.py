"""
Unit tests for Connection schema, ConnectionMgr, NodeGroup, and Unity level compatibility.
"""

from __future__ import annotations

import os
import sys
import unittest

_src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

import PvZ_Fusion_Node as pvn
from PvZ_Fusion_Node.Core import Compiler, Connection, ConnectionMgr, Level, NodeGroup, SymbolRegistry
from PvZ_Fusion_Node.Nodes.Original.Trigger import OnGameStartNode
from PvZ_Fusion_Node.Nodes.Original.GeneralFunction import ShowTextNode
from PvZ_Fusion_Node.Nodes.Original.PlantFunction import SetPlantNode


class TestGroupsAndConnections(unittest.TestCase):
    def setUp(self):
        pvn.ctx.reset()

    def test_connection_dataclass_schema(self):
        """Tests that Connection serializes to sourceNodeId/targetNodeId and supports legacy aliases."""
        conn1 = Connection(
            sourceNodeId="node-a",
            sourcePortName="触发",
            targetNodeId="node-b",
            targetPortName="触发",
        )
        self.assertEqual(conn1.sourceNodeId, "node-a")
        self.assertEqual(conn1.fromNodeId, "node-a")
        self.assertEqual(conn1.targetNodeId, "node-b")
        self.assertEqual(conn1.toNodeId, "node-b")
        self.assertEqual(conn1.sourcePortName, "触发")
        self.assertEqual(conn1.fromPortName, "触发")

        d = conn1.to_dict()
        self.assertIn("sourceNodeId", d)
        self.assertIn("sourcePortName", d)
        self.assertIn("targetNodeId", d)
        self.assertIn("targetPortName", d)
        self.assertEqual(d["sourceNodeId"], "node-a")
        self.assertEqual(d["targetNodeId"], "node-b")

        # Legacy initialization
        conn2 = Connection(
            fromNodeId="node-c",
            fromPortName="out",
            toNodeId="node-d",
            toPortName="in",
        )
        self.assertEqual(conn2.sourceNodeId, "node-c")
        self.assertEqual(conn2.targetNodeId, "node-d")

    def test_connection_mgr_dummy_index_zero(self):
        """Tests that eventNodeGraph.connections always has dummy empty connection at index 0."""
        mgr = ConnectionMgr()
        # Empty manager should still have dummy connection
        lst = mgr.to_list()
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst[0], {"sourceNodeId": "", "sourcePortName": "", "targetNodeId": "", "targetPortName": ""})

        conn = mgr.connect("node-1", "触发", "node-2", "触发")
        self.assertEqual(len(mgr.connections), 1)

        lst2 = mgr.to_list()
        self.assertEqual(len(lst2), 2)
        self.assertEqual(lst2[0]["sourceNodeId"], "")
        self.assertEqual(lst2[1]["sourceNodeId"], "node-1")
        self.assertEqual(lst2[1]["targetNodeId"], "node-2")

    def test_nodegroup_model_and_registration(self):
        """Tests NodeGroup serialization matching Unity's Assembly-CSharp NodeGroup schema."""
        registry = SymbolRegistry()
        grp = NodeGroup(
            title="My Logic Group",
            node_ids=["id-1", "id-2"],
            is_folded=False,
        )
        self.assertIsNone(grp.rid)
        registry.register(grp)
        self.assertIsNotNone(grp.rid)
        self.assertGreaterEqual(grp.rid, 1000)

        ref_entry = grp.dump_ref()
        self.assertEqual(ref_entry["rid"], grp.rid)
        self.assertEqual(ref_entry["type"]["class"], "NodeGroup")
        self.assertEqual(ref_entry["type"]["ns"], "GameLevel.EventNodes")
        self.assertEqual(ref_entry["type"]["asm"], "Assembly-CSharp")

        data = ref_entry["data"]
        self.assertEqual(data["title"], "My Logic Group")
        self.assertEqual(data["nodeIds"], ["id-1", "id-2"])
        self.assertIn("backgroundColor", data)
        self.assertIn("position", data)
        self.assertIn("size", data)
        self.assertFalse(data["isFolded"])

        # Compact graph reference
        graph_ref = grp.dump_graph_group()
        self.assertEqual(graph_ref, {"rid": grp.rid})

    def test_level_compilation_with_groups_and_connections(self):
        """Tests that compiling a level produces valid groups and connections without -2 RIDs."""
        lvl = Level(name="TestLevel")
        n1 = lvl.add_node(OnGameStartNode())
        n2 = lvl.add_node(ShowTextNode(display_text="Hello"))
        lvl.connect(n1, "触发", n2, "触发")

        grp = lvl.add_group(NodeGroup(title="Intro Sequence", node_ids=[n1.node_id, n2.node_id]))

        compiler = Compiler(auto_layout=True, optimize=True)
        compiled = compiler.compile(lvl)

        graph_data = compiled["eventNodeGraph"]
        # Connections check
        self.assertEqual(len(graph_data["connections"]), 2)
        self.assertEqual(graph_data["connections"][0]["sourceNodeId"], "")
        self.assertEqual(graph_data["connections"][1]["sourceNodeId"], n1.node_id)
        self.assertEqual(graph_data["connections"][1]["targetNodeId"], n2.node_id)

        # Groups check
        self.assertEqual(len(graph_data["groups"]), 1)
        self.assertEqual(graph_data["groups"][0]["rid"], grp.rid)
        self.assertNotEqual(graph_data["groups"][0]["rid"], -2)

        # RefIds check
        ref_ids = compiled["references"]["RefIds"]
        group_refs = [r for r in ref_ids if r.get("type", {}).get("class") == "NodeGroup"]
        self.assertEqual(len(group_refs), 1)
        self.assertEqual(group_refs[0]["rid"], grp.rid)
        self.assertEqual(group_refs[0]["data"]["title"], "Intro Sequence")
        self.assertEqual(group_refs[0]["data"]["nodeIds"], [n1.node_id, n2.node_id])

        # Group bounding box check
        pos = group_refs[0]["data"]["position"]
        sz = group_refs[0]["data"]["size"]
        self.assertGreater(sz["x"], 0)
        self.assertGreater(sz["y"], 0)

    def test_context_group_level_auto_grouping(self):
        """Tests that group_level=1 automatically creates valid NodeGroups upon export."""
        pvn.Config(output=".", name="AutoGroupTest")
        pvn.settings.group_level = 1

        with pvn.Trigger.OnGameStart():
            pvn.Print("Auto group test")

        compiled = pvn.ctx.level.to_dict()
        # Transfer groups
        pvn.ctx.export()

        compiled_after_export = Compiler(auto_layout=True).compile(pvn.ctx.level)
        groups = compiled_after_export["eventNodeGraph"]["groups"]
        self.assertGreater(len(groups), 0)
        for g in groups:
            self.assertIn("rid", g)
            self.assertNotEqual(g["rid"], -2)

        ref_ids = compiled_after_export["references"]["RefIds"]
        group_ref_ids = [r["rid"] for r in ref_ids if r.get("type", {}).get("class") == "NodeGroup"]
        for g in groups:
            self.assertIn(g["rid"], group_ref_ids)


if __name__ == "__main__":
    unittest.main()
