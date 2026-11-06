import unittest
from PvZ_Fusion_Transpiler.Core import _ctx
from PvZ_Fusion_Transpiler.Core.connection_manager import ConnectionManager, PortType
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import (
    BulletType,
    KeyCode,
    PlantType,
    ZombieType,
    SceneType,
    LevelType,
    SoundType,
    TravelBuffType,
    AdvBuff,
    UltiBuff,
    TravelDebuff,
    ZombieAnimation,
)


class TestNewRequirements(unittest.TestCase):
    def setUp(self):
        _ctx.clear()

    def tearDown(self):
        _ctx.clear()

    # Requirement 1: Only Enum can be taken as values in plant, zombie, and bullet types
    def test_strict_enum_validation(self):
        # plant_type_value
        with self.assertRaises(TypeError):
            pft.nodes.plant_type_value(val=300)
        with self.assertRaises(TypeError):
            pft.nodes.plant_type_value(val=0)

        # zombie_type_value
        with self.assertRaises(TypeError):
            pft.nodes.zombie_type_value(val=10)
        with self.assertRaises(TypeError):
            pft.nodes.zombie_type_value(val=0)

        # bullet_type_value
        with self.assertRaises(TypeError):
            pft.nodes.bullet_type_value(val=71)
        with self.assertRaises(TypeError):
            pft.nodes.bullet_type_value(val=0)

        # set_plant
        with self.assertRaises(TypeError):
            pft.nodes.set_plant(row=1, column=1, plant_type=10)
        with self.assertRaises(TypeError):
            pft.Spawner.Set_Plant(row=1, col=1, plant_type=10)

        # create_zombie
        with self.assertRaises(TypeError):
            pft.nodes.create_zombie(row=1, column=1, zombie_type=5)
        with self.assertRaises(TypeError):
            pft.Spawner.Set_Zombie(row=1, col=1, zombie_type=5)

        # shoot_event_bullet
        with self.assertRaises(TypeError):
            pft.nodes.shoot_event_bullet(row=1, col=1.0, bullet_type=71)
        with self.assertRaises(TypeError):
            pft.Spawner.Set_Bullet(row=1, col=1.0, bullet_type=71)

        # Direct connection of Int to PlantType, ZombieType, BulletType ports is disallowed
        int_node = pft.nodes.int_value(val=5)
        set_plant_node = pft.nodes.set_plant()
        with self.assertRaises(ValueError):
            int_node.port_output_int_Value.connect(set_plant_node.port_input_planttype_PlantType)

    # Requirement 2 & 3: Types modular files and Types.py
    def test_types_import_and_animation(self):
        from PvZ_Fusion_Transpiler._Data.PlantType import PlantType as PT, Plant_DieReason
        from PvZ_Fusion_Transpiler._Data.ZombieType import ZombieType as ZT
        from PvZ_Fusion_Transpiler._Data.BulletType import BulletType as BT
        from PvZ_Fusion_Transpiler._Data.KeyCode import KeyCode as KC
        from PvZ_Fusion_Transpiler._Data.SceneType import SceneType as ST
        from PvZ_Fusion_Transpiler._Data.LevelType import LevelType as LT
        from PvZ_Fusion_Transpiler._Data.SoundType import SoundType as SndT
        from PvZ_Fusion_Transpiler._Data.TravelBuffType import TravelBuffType as TBT
        from PvZ_Fusion_Transpiler._Data.ZombieAnimations import ZombieAnimation as ZA, ZombieAnimations as ZAs
        from PvZ_Fusion_Transpiler._Data.dump_animations import dump_zombie_animations

        self.assertIs(PlantType, PT)
        self.assertIs(ZombieType, ZT)
        self.assertIs(BulletType, BT)
        self.assertIs(KeyCode, KC)
        self.assertIs(SceneType, ST)
        self.assertIs(LevelType, LT)
        self.assertIs(SoundType, SndT)
        self.assertIs(TravelBuffType, TBT)
        self.assertIs(ZombieAnimation, ZA)
        self.assertIs(ZombieAnimation, ZAs)
        self.assertTrue(callable(dump_zombie_animations))
        self.assertTrue(hasattr(ZombieAnimation, "NormalZombie"))
        self.assertEqual(ZombieAnimation.NormalZombie.WALK.value, "walk")

    def test_dump_animations_internal_from_dump_folder(self):
        from PvZ_Fusion_Transpiler._Data.dump_animations import dump_zombie_animations
        import tempfile
        import os
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = os.path.join(tmpdir, "ZombieAnimations.py")
            dump_zombie_animations(output_path=out_file)
            self.assertTrue(os.path.exists(out_file))
            with open(out_file, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("class ZombieAnimation:", content)
            self.assertIn("class NormalZombie(Enum):", content)
            self.assertIn('WALK = "walk"', content)

    # Requirement 4: OnKeyPressNode targetKey & BulletTypeValueNode bulletType serialization
    def test_key_press_and_bullet_type_serialization(self):
        key_node = pft.nodes.on_key_press(target_key=KeyCode.W)
        data = key_node.dump_data()
        self.assertIn("targetKey", data)
        self.assertNotIn("target_key", data)
        self.assertEqual(data["targetKey"], 119)

        bt_node = pft.nodes.bullet_type_value(val=BulletType.Bullet_superMelon)
        bt_data = bt_node.dump_data()
        self.assertIn("bulletType", bt_data)
        self.assertNotIn("value", bt_data)
        self.assertEqual(bt_data["bulletType"], 71)

        pt_node = pft.nodes.plant_type_value(val=PlantType.Peashooter)
        pt_data = pt_node.dump_data()
        self.assertIn("plantType", pt_data)
        self.assertNotIn("value", pt_data)
        self.assertEqual(pt_data["plantType"], 0)

        zt_node = pft.nodes.zombie_type_value(val=ZombieType.NormalZombie)
        zt_data = zt_node.dump_data()
        self.assertIn("zombieType", zt_data)
        self.assertNotIn("value", zt_data)
        self.assertEqual(zt_data["zombieType"], 0)

    # Requirement 5: Omit false, 0, and 0.0 constant nodes
    def test_omit_default_constants(self):
        # Initially only reset
        self.assertEqual(len(_ctx.nodes), 0)

        # Spawning with default 0 / False values
        shoot_node = pft.nodes.shoot_event_bullet(
            row=0,
            col=0.0,
            bullet_type=BulletType.Bullet_pea,
            at_mouse=False,
            zombie_camp=False,
            damage=0,
            speed=0.0,
            angle=0.0,
            scale_multiplier=0.0,
        )

        # Only ShootEventBulletNode and BulletTypeValueNode should be created
        node_types = [n.node_type for n in _ctx.nodes]
        self.assertIn("ShootEventBulletNode", node_types)
        self.assertIn("BulletTypeValueNode", node_types)
        self.assertNotIn("BoolValueNode", node_types)
        self.assertNotIn("IntValueNode", node_types)
        self.assertNotIn("FloatValueNode", node_types)
        self.assertEqual(len(_ctx.nodes), 2)

        # Clear and test set_plant with row=0, col=0, force=False
        _ctx.clear()
        sp = pft.nodes.set_plant(row=0, column=0, plant_type=PlantType.Peashooter, force_plant=False)
        sp_types = [n.node_type for n in _ctx.nodes]
        self.assertIn("SetPlantNode", sp_types)
        self.assertIn("PlantTypeValueNode", sp_types)
        self.assertNotIn("IntValueNode", sp_types)
        self.assertNotIn("BoolValueNode", sp_types)
        self.assertEqual(len(_ctx.nodes), 2)

    # Requirement 6: Column input float port directly connects FloatValueNode
    def test_column_float_port_direct_connection(self):
        _ctx.clear()

        # Pass integer 2 to col in shoot_event_bullet
        bullet = pft.nodes.shoot_event_bullet(
            col=2,
            bullet_type=BulletType.Bullet_pea,
        )

        node_types = [n.node_type for n in _ctx.nodes]
        self.assertIn("FloatValueNode", node_types)
        self.assertNotIn("IntToFloatNode", node_types)
        self.assertNotIn("IntValueNode", node_types)

        # Verify the float port is directly connected from FloatValueNode
        col_input = bullet.port_input_float_Col
        conns = col_input.get_connections()
        self.assertEqual(len(conns), 1)
        self.assertEqual(conns[0].source_node.node_type, "FloatValueNode")
        self.assertEqual(conns[0].source_node.value, 2.0)

    # Requirement: AdvBuff, UltiBuff, TravelDebuff enums and TravelBuffType updates
    def test_buff_and_debuff_enums(self):
        # 1. AdvBuff membership and values (English PascalCase names & docstrings)
        self.assertEqual(AdvBuff.CallToArms.value, 0)
        self.assertEqual(AdvBuff.BlessingOfEndurance.value, 15007)
        self.assertEqual(AdvBuff.SPEvolution_DoomGatling.value, 7000)
        self.assertEqual(AdvBuff.Ascend_Inferno.value, 12000)
        self.assertEqual(AdvBuff.VoodooDummy_A.value, 13003)
        self.assertEqual(len(AdvBuff.__members__), 232)

        # 2. UltiBuff membership and values
        self.assertEqual(UltiBuff.嗜血如命.value, 0)
        self.assertEqual(UltiBuff.究炉恢复.value, 55)
        self.assertEqual(len(UltiBuff.__members__), 56)

        # 3. TravelDebuff membership and values
        self.assertEqual(TravelDebuff.二爷无视植物.value, 0)
        self.assertEqual(TravelDebuff.Shooting_命运无常.value, 10044)
        self.assertEqual(len(TravelDebuff.__members__), 143)

        # 4. TravelBuffType combined enum
        self.assertEqual(TravelBuffType.CallToArms.value, ("AdvBuff", 0))
        self.assertEqual(TravelBuffType.BlessingOfEndurance.value, ("AdvBuff", 15007))
        self.assertEqual(TravelBuffType.嗜血如命.value, ("UltiBuff", 0))
        self.assertEqual(TravelBuffType.二爷无视植物.value, ("TravelDebuff", 0))
        self.assertEqual(len(TravelBuffType.__members__), 431)

        # 5. nodes.get_travel_buff handling with all enum types
        _ctx.clear()
        node_adv = pft.nodes.get_travel_buff(AdvBuff.CallToArms)
        self.assertIsNotNone(node_adv.buff)
        self.assertEqual(node_adv.buff.asset_class, "AdvBuff")
        self.assertEqual(node_adv.buff.value, 0)
        dump_adv = node_adv.buff.dump_ref()
        self.assertEqual(dump_adv["type"]["class"], "AdvBuff")
        self.assertEqual(dump_adv["data"]["value__"], 0)

        node_ulti = pft.nodes.get_travel_buff(UltiBuff.嗜血如命)
        self.assertIsNotNone(node_ulti.buff)
        self.assertEqual(node_ulti.buff.asset_class, "UltiBuff")
        self.assertEqual(node_ulti.buff.value, 0)
        dump_ulti = node_ulti.buff.dump_ref()
        self.assertEqual(dump_ulti["type"]["class"], "UltiBuff")
        self.assertEqual(dump_ulti["data"]["value__"], 0)

        node_debuff = pft.nodes.get_travel_buff(TravelDebuff.二爷无视植物)
        self.assertIsNotNone(node_debuff.buff)
        self.assertEqual(node_debuff.buff.asset_class, "TravelDebuff")
        self.assertEqual(node_debuff.buff.value, 0)
        dump_debuff = node_debuff.buff.dump_ref()
        self.assertEqual(dump_debuff["type"]["class"], "TravelDebuff")
        self.assertEqual(dump_debuff["data"]["value__"], 0)

        # 6. High level Game.get_buff & Lawnf.get_buff
        pft.Game.get_buff(AdvBuff.Doomsday)
        pft.Lawnf.get_buff(UltiBuff.流星雨)

    def test_sun_money_add_extensions(self):
        with pft.Trigger.OnBoardStart():
            node_sun = pft.Board.Sun.Add(250)
            self.assertEqual(node_sun.node_type, "GetSunNode")

            pft.Board.Sun += 100

            node_money = pft.Board.Money.Add(500)
            self.assertEqual(node_money.node_type, "GetMoneyNode")

            pft.Board.Money += 50

    def test_tool_type_value_and_implicit_lowering(self):
        from PvZ_Fusion_Transpiler.Types import ToolType
        from PvZ_Fusion_Transpiler.port_types import to_port

        # Explicit Tool.Value
        port1 = pft.Tool.Value(ToolType.Shovel)
        self.assertEqual(port1.port_type, PortType.ToolType)

        port2 = pft.Tool.Value(ToolType.铲子)
        self.assertEqual(port2.port_type, PortType.ToolType)

        # Implicit lowering via to_port
        port_implicit = to_port(ToolType.Hammer)
        self.assertEqual(port_implicit.port_type, PortType.ToolType)

        # High-level tool methods
        with pft.Trigger.OnBoardStart():
            is_held = pft.Tool.is_held(ToolType.Shovel)
            self.assertEqual(is_held.port_type, PortType.Bool)

    def test_flow_nodes_do_once_wait_until_repeat_until(self):
        with pft.Trigger.OnBoardStart():
            once = pft.DoOnce()
            with once:
                pft.Board.Sun.Add(500)
            once.Reset()

            with pft.Time.WaitUntil(pft.Board.Sun >= 100, interval=0.5, max_checks=40) as wait:
                pft.InGameUI.display_text("Ready!")
                with wait.OnTimeout:
                    pft.InGameUI.display_text("Timed out")
                with wait.OnFailed:
                    pft.InGameUI.display_text("Failed")

            with pft.Time.RepeatUntil(pft.Board.Sun >= 500, interval=1.0, max_checks=60) as loop:
                with loop.OnEach:
                    pft.InGameUI.display_text("Checking...")
                with loop.OnComplete:
                    pft.InGameUI.display_text("Goal reached!")
                with loop.OnTimeout:
                    pft.InGameUI.display_text("Timeout")

    def test_pulse_node(self):
        with pft.Trigger.OnBoardStart():
            is_active = pft.BoolVar(True, name="IsActive")
            pulse = pft.Pulse(state=is_active)
            with pulse.OnPulse:
                pft.InGameUI.display_text("Pulse fired!")

            with pft.Pulse(state=is_active):
                pft.InGameUI.display_text("Direct enter pulse!")

    def test_typed_choice_menu(self):
        with pft.Trigger.OnBoardStart():
            menu = pft.MultiSelectMenu(
                is_rerollable=True,
                reroll_count=2,
                kind=pft.MenuKind.Typed,
            )

            @menu.option(title="Sun", description="+500 sun", plant_type=PlantType.SunFlower)
            def pick_sun():
                pft.Board.Sun.Add(500)

            @menu.option(title="Nut", description="WallNut", plant_type=PlantType.WallNut)
            def pick_nut():
                pft.Board.Sun.Add(100)

            menu.show()

            self.assertEqual(menu._options[0].node.node_type, "TypedChoiceOptionNode")
            self.assertEqual(menu._options[1].node.node_type, "TypedChoiceOptionNode")
            self.assertEqual(menu.node.node_type, "TypedChoiceMenuNode")

    def test_get_travel_entry_deprecated(self):
        import warnings
        with pft.Trigger.OnBoardStart():
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                node = pft.Game.GetTravelEntry()
                self.assertEqual(node.node_type, "GetTravelEntryNode")
                self.assertTrue(len(w) >= 1)
                self.assertTrue(issubclass(w[-1].category, DeprecationWarning))

            with warnings.catch_warnings(record=True) as w2:
                warnings.simplefilter("always")
                node2 = pft.Lawnf.GetTravelEntry()
                self.assertEqual(node2.node_type, "GetTravelEntryNode")
                self.assertTrue(len(w2) >= 1)
                self.assertTrue(issubclass(w2[-1].category, DeprecationWarning))


if __name__ == "__main__":
    unittest.main()
