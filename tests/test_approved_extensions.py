import unittest
from enum import Enum
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Core import _ctx
from PvZ_Fusion_Transpiler.Types import (
    PlantType,
    ZombieType,
    ToolType,
)


class TestApprovedExtensions(unittest.TestCase):
    def setUp(self):
        _ctx.clear()

    def tearDown(self):
        _ctx.clear()

    # 1. Plant extension methods
    def test_plant_extension_methods(self):
        plant = pft.Spawner.Set_Plant(0, 0, PlantType.Peashooter)
        self.assertIsNotNone(plant.curse(10.0))
        self.assertIsNotNone(plant.silence(5.0))
        self.assertIsNotNone(plant.feed_golden_bean())
        self.assertIsNotNone(plant.try_super_skill())
        self.assertIsNotNone(plant.upgrade(target_level=2, star=True))
        self.assertIsNotNone(plant.get_attack_speed())
        self.assertIsNotNone(plant.set_attack_speed(2.0))
        self.assertIsNotNone(plant.set_attack_interval(1.5))
        self.assertIsNotNone(plant.get_attribute_countdown())
        self.assertIsNotNone(plant.set_attribute_countdown(remaining=3.0, max_seconds=10.0))
        self.assertIsNotNone(plant.get_basic_components())
        self.assertIsNotNone(plant.to_object())

    # 2. Zombie extension methods
    def test_zombie_extension_methods(self):
        zombie = pft.Spawner.Set_Zombie(0, 0, ZombieType.NormalZombie)
        self.assertIsNotNone(zombie.get_stats())
        self.assertIsNotNone(zombie.set_stats(500.0))
        self.assertIsNotNone(zombie.get_status())
        self.assertIsNotNone(zombie.set_status(1.0))
        self.assertIsNotNone(zombie.is_type(ZombieType.NormalZombie))
        self.assertIsNotNone(zombie.to_object())

    # 3. Zombie loops yielding Zombie directly (no index)
    def test_zombie_loops(self):
        with pft.ForEachAllZombies() as zombie:
            self.assertIsInstance(zombie, pft.Zombie)
            zombie.damage(50.0)

        all_zombies_list = pft.Lawnf.get_all_zombies()
        with pft.ForEachZombie(all_zombies_list) as zombie:
            self.assertIsInstance(zombie, pft.Zombie)
            zombie.set_stats(100.0)

    # 4. Lawnf extension methods
    def test_lawnf_methods(self):
        self.assertIsNotNone(pft.Lawnf.get_all_plants())
        self.assertIsNotNone(pft.Lawnf.get_plants_on_layer(0, 0, 0))
        self.assertIsNotNone(pft.Lawnf.get_random_plant_type())
        self.assertIsNotNone(pft.Lawnf.get_all_zombies())
        self.assertIsNotNone(pft.Lawnf.delete_grid_items(0, 0))
        self.assertIsNotNone(pft.Lawnf.clear_cell(1, 1))
        self.assertIsNotNone(pft.Lawnf.change_map())
        self.assertIsNotNone(pft.Lawnf.change_music())
        self.assertIsNotNone(pft.Lawnf.set_zombie_house_rule(True))
        self.assertIsNotNone(pft.Lawnf.remove_travel_entry("entry_1"))

    # 5. Trigger extension hooks
    def test_trigger_hooks(self):
        with pft.Trigger.OnPlantMixed() as plant:
            self.assertIsInstance(plant, pft.Plant)

        with pft.Trigger.OnWorldPlantEffect() as row:
            self.assertIsNotNone(row)

        with pft.Trigger.OnZombieClick() as zombie:
            self.assertIsInstance(zombie, pft.Zombie)

        with pft.Trigger.OnZombieHealthBelow() as zombie:
            self.assertIsInstance(zombie, pft.Zombie)

        with pft.Trigger.OnWaveEvent() as wave:
            self.assertIsNotNone(wave)

        with pft.Trigger.OnStageEnter():
            pass

    # 6. Game & Stage flow
    def test_game_and_stage(self):
        self.assertIsNotNone(pft.Game.pause_wave_timer(True))
        self.assertIsNotNone(pft.Game.pause_wave_countdown(False))
        self.assertIsNotNone(pft.Game.Stage.get_current())
        self.assertIsNotNone(pft.Game.Stage.change())

    # 7. InGameUI Zombie cards
    def test_ingame_ui_zombie_cards(self):
        self.assertIsNotNone(pft.InGameUI.give_zombie_card(ZombieType.ConeZombie, cooldown=5.0, cost=75))
        self.assertIsNotNone(pft.InGameUI.remove_zombie_cards(ZombieType.ConeZombie))
        self.assertIsNotNone(pft.InGameUI.set_zombie_card_cooldown(ZombieType.ConeZombie, total=10.0, remaining=5.0))
        self.assertIsNotNone(pft.InGameUI.clear_info_cards())

    # 8. Tool extension
    def test_tool_methods(self):
        obj, tool_type = pft.Tool.get_held()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(tool_type)

        class DummyTool(Enum):
            Shovel = 0

        val = pft.nodes.tool_type_value(DummyTool.Shovel)
        self.assertIsNotNone(pft.Tool.is_held(val))
        cd = pft.Tool.get_cooldown(val)
        self.assertIsNotNone(cd.total_seconds)
        self.assertIsNotNone(cd.remaining_seconds)
        self.assertIsNotNone(cd.exists)
        self.assertIsNotNone(pft.Tool.set_cooldown(val, ratio=0.5))

    # 9. StringVar
    def test_string_var(self):
        s = pft.StringVar("Hello", name="MyText")
        self.assertIsNotNone(s.value)
        s.set("World")
        s += "!"
        self.assertIsNotNone(s.to_string())

    # 10. Variable in-place arithmetic
    def test_variable_arithmetic_in_place(self):
        iv = pft.IntVar(10)
        iv.add_in_place(5)
        fv = pft.FloatVar(2.5)
        fv.add_in_place(1.5)

    # 13. WorldObject / Object
    def test_world_object(self):
        obj = pft.WorldObject.create("Marker", position=pft.WorldObject.vector3(1.0, 2.0, 3.0))
        self.assertIsNotNone(obj.ref)
        self.assertIsNotNone(pft.WorldObject.mouse_world_position())
        self.assertIsNotNone(pft.WorldObject.event_position())
        plant = obj.to_plant()
        self.assertIsInstance(plant, pft.Plant)
        plant_try, exists = obj.try_cast_to_plant()
        self.assertIsInstance(plant_try, pft.Plant)
        self.assertIsNotNone(exists)
        zombie = obj.to_zombie()
        self.assertIsInstance(zombie, pft.Zombie)
        zombie_try, exists_z = obj.try_cast_to_zombie()
        self.assertIsInstance(zombie_try, pft.Zombie)
        self.assertIsNotNone(exists_z)
        self.assertIsNotNone(obj.set_transform(position=pft.WorldObject.vector3(0, 0, 0), scale_multiplier=1.0))
        self.assertIsNotNone(obj.get_transform())
        self.assertIsNotNone(obj.destroy())

    # 15. Math & Conversions
    def test_math_and_conversions(self):
        self.assertIsNotNone(pft.Math.pow(2.0, 3.0))
        self.assertIsNotNone(pft.Math.log(10.0))
        self.assertIsNotNone(pft.Math.greater(5, 3))
        self.assertIsNotNone(pft.Math.less(2.0, 4.0))
        self.assertIsNotNone(pft.Math.equal(1, 1))

        # Constructors
        self.assertIsNotNone(pft.Int(5))
        self.assertIsNotNone(pft.Float(2.5))
        self.assertIsNotNone(pft.String("hello"))
        self.assertIsNotNone(pft.Bool(True))

        # Cast static methods
        self.assertIsNotNone(pft.Int.Cast(3.14))
        self.assertIsNotNone(pft.Float.Cast(10))
        self.assertIsNotNone(pft.String.Cast(100))
        self.assertIsNotNone(pft.Bool.Cast(1))


if __name__ == "__main__":
    unittest.main()
