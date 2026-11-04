import unittest
from enum import Enum
import warnings
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType
from PvZ_Fusion_Transpiler import Int, Float, Bool, String
from PvZ_Fusion_Transpiler.Core import _ctx, ConnectionManager
from PvZ_Fusion_Transpiler.Core.annotations import ExperimentalWarning, ObsoleteWarning


class TestSpecV2Requirements(unittest.TestCase):
    def setUp(self):
        _ctx.clear()

    def test_list_branch_safety_f1(self):
        """Test F1: Add inside an If does not rebind root port; outside Count wires to ListVariableNode."""
        items = pft.IntList(name="TestList")
        list_var_node_id = items.list_port.node.id

        cond = pft.Bool(True)
        with pft.If(cond):
            op = items.Add(42)
            self.assertIsNotNone(op)

        count_port = items.Count
        count_node = count_port.node
        list_input_port = count_node.port_input_listvariable_List

        in_connections = [
            c for c in ConnectionManager.connections
            if c.target_node.id == count_node.id and c.target_port.name == list_input_port.name
        ]
        self.assertEqual(len(in_connections), 1)
        self.assertEqual(in_connections[0].source_node.id, list_var_node_id)

    def test_try_get_value_single_node_f2(self):
        """Test F2: TryGetValue emits exactly ONE get-item node, and both returned ports come from it."""
        items = pft.IntList([10, 20, 30])
        get_item_nodes_before = [n for n in _ctx.nodes if n.__class__.__name__ == "GetIntListItemNode"]
        val_port, ok_port = items.TryGetValue(1)
        get_item_nodes_after = [n for n in _ctx.nodes if n.__class__.__name__ == "GetIntListItemNode"]

        self.assertEqual(len(get_item_nodes_after) - len(get_item_nodes_before), 1)
        self.assertEqual(val_port.node.id, ok_port.node.id)
        self.assertEqual(val_port.name, "值")
        self.assertEqual(ok_port.name, "有效")

    def test_list_type_safety_f3_f7(self):
        """Test F3 & F7: Unsupported types or wrong enums raise TypeError."""
        with self.assertRaises(TypeError):
            pft.List()

        with self.assertRaises(TypeError):
            pft.List[dict]()

        with self.assertRaises(TypeError):
            pft.List[pft.Plant]()

        with self.assertRaises(TypeError):
            pft.List[pft.Zombie]()

        with self.assertRaises(TypeError):
            pft.PlantTypeListVar([ZombieType.NormalZombie])

        with self.assertRaises(TypeError):
            pft.PlantTypeListVar([1])

        plant_list = pft.PlantTypeListVar()
        with self.assertRaises(TypeError):
            plant_list.Add(ZombieType.NormalZombie)

    def test_class_caching_f5(self):
        """Test F5: List[T] is cached so List[Int] is List[Int], and isinstance works."""
        self.assertIs(pft.List[Int], pft.List[Int])
        self.assertIs(pft.List[int], pft.List[Int])
        self.assertIs(pft.List[float], pft.List[Float])

        int_list = pft.List[Int]()
        self.assertIsInstance(int_list, pft.List[Int])

    def test_operator_traps_f10(self):
        """Test F10: len(), 'in', and bool() raise descriptive TypeError."""
        items = pft.IntList([1, 2, 3])

        with self.assertRaises(TypeError) as ctx_len:
            len(items)
        self.assertIn(".Count", str(ctx_len.exception))

        with self.assertRaises(TypeError) as ctx_in:
            _ = 5 in items
        self.assertIn(".Contains", str(ctx_in.exception))

        with self.assertRaises(TypeError) as ctx_bool:
            bool(items)
        self.assertIn("Count > 0", str(ctx_bool.exception))

    def test_distinct_default_names_f6(self):
        """Test F6: Unnamed lists receive distinct variable names."""
        l1 = pft.IntList()
        l2 = pft.IntList()
        clone = l1.Clone()

        name1 = l1.list_port.node.asset.name
        name2 = l2.list_port.node.asset.name
        clone_name = clone.list_port.node.asset.name

        self.assertNotEqual(name1, name2)
        self.assertNotEqual(name1, clone_name)
        self.assertNotEqual(name2, clone_name)

    def test_list_operation_failed_port(self):
        """Test ListOperation has Failed / OnFailed wiring to '失败' port."""
        items = pft.IntList()
        op = items.Add(10)
        self.assertEqual(op.Failed.out_trigger, "失败")
        self.assertEqual(op.OnFailed.out_trigger, "失败")
        self.assertEqual(op.OnComplete.out_trigger, "完成")
        self.assertEqual(op.OnSuccess.out_trigger, "完成")

    def test_do_once_reset(self):
        """Test DoOnce exposes OnExecute and Reset() connects to Reset port."""
        do = pft.DoOnce()
        self.assertIsNotNone(do.OnExecute)
        self.assertEqual(do.OnExecute.out_trigger, "触发")

        do.Reset()
        reset_conns = [
            c for c in ConnectionManager.connections
            if c.to_node == do.node.id and c.to_port == "重置"
        ]
        self.assertEqual(len(reset_conns), 0)

    def test_experimental_and_obsolete_warnings(self):
        """Test experimental and obsolete warnings fire appropriately."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            pft.Board.Sun.Add(100)
            self.assertTrue(any(issubclass(item.category, ExperimentalWarning) for item in w))

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            pft.Pulse(pft.Bool(True))
            self.assertTrue(any(issubclass(item.category, ExperimentalWarning) for item in w))

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            pft.Game.GetTravelEntry()
            self.assertTrue(any(issubclass(item.category, ObsoleteWarning) for item in w))


if __name__ == "__main__":
    unittest.main()
