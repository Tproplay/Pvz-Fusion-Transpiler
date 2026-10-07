"""
Sample Test Suite for PvZ Fusion Visual Script Transpiler & Level Compiler.
Verifies level creation, node addition, connection wiring, layout, compilation, and serialization.
"""

import os
import sys
import unittest

# Ensure src directory is in sys.path
_src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

from Core import Compiler, Level
from Nodes.Original.Trigger import OnGameStartNode, OnWaveClearedNode
from Nodes.Original.PlantFunction import SetPlantNode
from Nodes.Original.ZombieFunction import CreateZombieNode, DamageZombieNode
from Nodes.Original.GeneralFunction import ShowTextNode
from Nodes.Extentions.Variables import IntVar


class TestLevelCompiler(unittest.TestCase):
    def setUp(self):
        self.level = Level(
            name="SampleTestLevel",
            level_number=9998,
            level_type=11,
            start_sun=1000,
            max_wave=15,
            card_count=14,
        )

    def test_board_configuration(self):
        """Tests that BoardConfig and BoardTag parameters and presets work properly."""
        self.assertEqual(self.level.startSun, 1000)
        self.level.boardConfig.zombieHealthMultiplier = 1.5
        self.level.boardConfig.waveInterval = 25.0
        self.assertEqual(self.level.boardConfig.zombieHealthMultiplier, 1.5)

        self.level.boardTag.enable_endless()
        self.assertTrue(self.level.boardTag.isEndless)

    def test_god_shooting_config(self):
        """Tests that God Shooting mode configuration adds plants correctly."""
        self.level.godShootingConfig.add_plant(
            plant_type=0, column=2, row=2, health=500.0, attack=30.0, is_player=True
        )
        self.assertEqual(len(self.level.godShootingConfig.plants), 1)
        self.assertEqual(self.level.godShootingConfig.plants[0].health, 500.0)

    def test_nodes_and_connections(self):
        """Tests adding nodes and wiring execution connections."""
        on_start = self.level.add_node(OnGameStartNode())
        banner = self.level.add_node(ShowTextNode(display_text="关卡开始！", duration=3.0))
        spawn_plant = self.level.add_node(SetPlantNode())

        conn1 = self.level.connect(on_start, "触发", banner, "触发")
        conn2 = self.level.connect(banner, "完成", spawn_plant, "触发")

        self.assertEqual(len(self.level.graph.nodes), 3)
        self.assertEqual(len(self.level.graph.connections), 2)
        self.assertEqual(conn1.fromPortName, "触发")
        self.assertEqual(conn2.toPortName, "触发")

    def test_canvas_variable_registration(self):
        """Tests that reactive canvas variables register with assets and get allocated RIDs."""
        var = self.level.add_node(IntVar(name="WaveCounter", start_val=0))
        self.assertIsNotNone(var.asset.rid)
        self.assertIn(var.asset, self.level.registry._registered_items)

    def test_compiler_pipeline(self):
        """Tests end-to-end compilation, topological layout, and dictionary emission."""
        on_start = self.level.add_node(OnGameStartNode())
        banner = self.level.add_node(ShowTextNode(display_text="测试", duration=3.0))
        self.level.connect(on_start, "触发", banner, "触发")

        compiler = Compiler(auto_layout=True, optimize=True)
        compiled_data = compiler.compile(self.level)

        self.assertIn("boardConfig", compiled_data)
        self.assertIn("boardTag", compiled_data)
        self.assertIn("eventNodeGraph", compiled_data)
        self.assertIn("references", compiled_data)

        # Check references RefIds
        ref_ids = compiled_data["references"]["RefIds"]
        self.assertGreater(len(ref_ids), 0)

        # Ensure node layout was computed and not left at default zero
        self.assertNotEqual(on_start.position_x, 0.0)

    def test_save_and_decompile(self):
        """Tests compiling to JSON file and loading it back."""
        test_file = "test_output_level.json"
        try:
            compiler = Compiler(auto_layout=True, optimize=True)
            compiler.compile_to_file(self.level, test_file)

            self.assertTrue(os.path.exists(test_file))
            decompiled_lvl = Compiler.decompile(test_file)
            self.assertEqual(decompiled_lvl.name, "SampleTestLevel")
            self.assertEqual(decompiled_lvl.startSun, 1000)
            self.assertEqual(decompiled_lvl.levelNumber, 9998)
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
