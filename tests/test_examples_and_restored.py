import glob
import json
import os
import tempfile
import unittest
from pathlib import Path

import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import Math, PlantData, PlantEntry, OrderedSpawn
from PvZ_Fusion_Transpiler.Core import _ctx
from PvZ_Fusion_Transpiler.StdLib import StatManager
from PvZ_Fusion_Transpiler.Types import (
    KeyCode,
    LevelType,
    PlantType,
    SceneType,
    TravelBuffType,
    ZombieType,
)
from tools.level_verifier import isolate_transpiler_context


class TestExamplesAndRestoredFeatures(unittest.TestCase):
    def setUp(self):
        _ctx.clear()

    def tearDown(self):
        _ctx.clear()

    def test_all_examples_execute_and_export(self):
        """Every example script under Examples/ must execute and export without errors."""
        examples = sorted(glob.glob("Examples/**/*.py", recursive=True))
        self.assertGreaterEqual(len(examples), 10)
        for ex_path in examples:
            with self.subTest(example=ex_path):
                with isolate_transpiler_context():
                    code_text = Path(ex_path).read_text(encoding="utf-8")
                    namespace = {"__file__": ex_path, "__name__": "__main__"}
                    exec(compile(code_text, ex_path, "exec"), namespace)
                    with tempfile.TemporaryDirectory() as tmp:
                        out_file = os.path.join(tmp, "test_out.json")
                        pft.export(out_file)
                        self.assertTrue(os.path.isfile(out_file))
                        with open(out_file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        self.assertIn("eventNodeGraph", data)
                        self.assertIn("references", data)

    def test_level_config_export_schema_and_clean_default(self):
        """Verify level_config merges cleanly when dirty, and emits minimal JSON when clean."""
        with tempfile.TemporaryDirectory() as tmp:
            # 1. Clean export (no level_config changes) -> minimal keys
            clean_path = os.path.join(tmp, "CleanLevel.json")
            with pft.Trigger.OnGameStart():
                pft.InGameUI.display_text("Clean")
            pft.export(clean_path)
            with open(clean_path, "r", encoding="utf-8") as f:
                clean_data = json.load(f)
            self.assertEqual(set(clean_data.keys()), {"eventNodeGraph", "references"})

        _ctx.clear()

        with tempfile.TemporaryDirectory() as tmp:
            # 2. Dirty export -> full level schema with configured overrides
            cfg_path = os.path.join(tmp, "ConfiguredLevel.json")
            pft.level_config.level_number = 8005
            pft.level_config.scene_type = SceneType.SnowPool
            pft.level_config.level_type = LevelType.CustomLevel
            pft.level_config.start_sun = 1500
            pft.level_config.adv_buffs = [
                TravelBuffType.BackupSupply,
                TravelBuffType.SolarReserve,
            ]
            pft.level_config.board_config.startTip = "Hello!"
            pft.level_config.board_tag.isNight = True
            pft.level_config.add_plant_data(
                PlantData.create(plant_type=PlantType.SunFlower, cost=25)
            )
            pft.level_config.add_plant(
                PlantEntry.create(row=1, col=2, plant_type=PlantType.WallNut, health=8000)
            )
            pft.level_config.add_ordered_spawn(
                OrderedSpawn.create(wave=3, zombies=[ZombieType.FlagZombie])
            )

            pft.export(cfg_path)
            with open(cfg_path, "r", encoding="utf-8") as f:
                cfg_data = json.load(f)

            self.assertEqual(cfg_data["levelNumber"], 8005)
            self.assertEqual(cfg_data["sceneType"], SceneType.SnowPool.value)
            self.assertEqual(cfg_data["levelType"], LevelType.CustomLevel.value)
            self.assertEqual(cfg_data["startSun"], 1500)
            self.assertEqual(cfg_data["advBuffs"], [1001, 1012])
            self.assertEqual(cfg_data["boardConfig"]["startTip"], "Hello!")
            self.assertTrue(cfg_data["boardTag"]["isNight"])
            self.assertEqual(cfg_data["plantDatas"][0]["cost"], 25)
            self.assertEqual(cfg_data["plants"][0]["thePlantHealth"], 8000)
            self.assertEqual(cfg_data["orderedSpawns"][0]["wave"], 3)

    def test_restored_math_and_bool_string_conversion(self):
        """Verify restored Math module (static & dynamic) and Bool-to-String formatting."""
        self.assertEqual(Math.abs(-5), 5)
        self.assertEqual(Math.floor(3.8), 3)
        self.assertEqual(Math.min(-1, -5), -5)
        self.assertEqual(Math.sqrt(16), 4.0)
        self.assertTrue(Math.is_prime(5))

        six = pft.IntVar(6)
        with pft.Trigger.OnGameStart():
            dyn_sin = Math.sin(Math.PI / six)
            dyn_abs = Math.abs(six)
            pft.InGameUI.display_text("Sin=", dyn_sin, " Abs=", dyn_abs, " StaticBool=", True)

        self.assertIsNotNone(dyn_sin)
        self.assertIsNotNone(dyn_abs)
        self.assertGreater(len(_ctx.nodes), 5)

    def test_stat_manager_restoration(self):
        """Verify StatManager builds plant & zombie stat modification graphs properly."""
        stats = StatManager(base_plant_stat=0, base_zombie_hp_mult=1.0)
        stats.create_tag("PeaFamily", [PlantType.Peashooter, PlantType.GatlingPea])
        stats.create_zombie_tag("Tough", [ZombieType.BucketZombie])

        with pft.Trigger.OnPlantCreate() as plant:
            stats.apply_stats_to_plant(plant)

        with pft.Trigger.OnZombieSpawn() as zombie:
            stats.apply_stats_to_zombie(zombie)

        with pft.Trigger.OnKeyDown(KeyCode.Alpha1):
            stats.add_tag_atk("PeaFamily", 0.25)
            stats.refresh_all_plants()

        node_types = {n.__class__.__name__ for n in _ctx.nodes}
        self.assertIn("ModifyPlantAttackNode", node_types)
        self.assertIn("ModifyPlantHealthNode", node_types)
        self.assertIn("ModifyZombieHealthNode", node_types)
        self.assertIn("ForEachPlantNode", node_types)


if __name__ == "__main__":
    unittest.main()
