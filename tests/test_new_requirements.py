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

    def test_type_convert_node_ports_and_display_text(self):
        from PvZ_Fusion_Transpiler.Core.connection_manager import ConnectionManager
        _ctx.clear()
        ConnectionManager.clear()
        with pft.Trigger.OnGameStart():
            pft.InGameUI.display_text(5)

        # Check IntToStringNode ports & connections
        int_to_str_nodes = [n for n in _ctx.nodes if n.node_type == "IntToStringNode"]
        self.assertEqual(len(int_to_str_nodes), 1)
        node = int_to_str_nodes[0]
        self.assertEqual(node.port_input_int_Value.name, "Value")
        self.assertEqual(node.port_output_string_String.name, "String")

        # Check dump_data does not serialize port into 'value'
        dumped = node.dump_data()
        self.assertNotIn("value", dumped)

        # Check connections
        all_conns = ConnectionManager.get_connections()
        incoming = [c for c in all_conns if c.target_node.id == node.id]
        self.assertEqual(len(incoming), 1)
        self.assertEqual(incoming[0].target_port.name, "Value")

        outgoing = [c for c in all_conns if c.source_node.id == node.id]
        self.assertEqual(len(outgoing), 1)
        self.assertEqual(outgoing[0].source_port.name, "String")
        self.assertEqual(outgoing[0].target_port.name, "文本")

        # Verify other conversion node port names
        from PvZ_Fusion_Transpiler._Nodes.Original.TypeConvert.float_to_string_node import FloatToStringNode
        from PvZ_Fusion_Transpiler._Nodes.Original.TypeConvert.plant_to_object_node import PlantToObjectNode
        f2s = FloatToStringNode()
        self.assertEqual(f2s.port_input_float_Value.name, "Value")
        self.assertEqual(f2s.port_input_int_Decimals.name, "Decimal Place")
        self.assertEqual(f2s.port_output_string_String.name, "String")

        p2o = PlantToObjectNode()
        self.assertEqual(p2o.port_input_plant_Plant.name, "Plant")
        self.assertEqual(p2o.port_output_gameobject_GameObject.name, "Object")

    def test_bool_comparison_and_static_mouse_properties(self):
        from PvZ_Fusion_Transpiler.Core.connection_manager import ConnectionManager
        _ctx.clear()
        ConnectionManager.clear()

        found = pft.BoolVar(name="found")
        other = pft.BoolVar(name="other")

        with pft.Trigger.OnKeyDown(KeyCode.K):
            with pft.Lawnf.for_each_plant_on_lawn() as plant:
                with pft.If((plant.plantType == pft.PlantType.SunFlower) & (found == False)):
                    pft.Object.bind_plant(plant, "sunflower")
                    found.set(True)
                with pft.If(found == other):
                    pass

        with pft.Trigger.OnGameStart():
            with pft.Time.OnFixedUpdate(5):
                pft.Object.get_bound_plant("sunflower").move(pft.Mouse.col, pft.Mouse.row)

        node_types = [n.node_type for n in _ctx.nodes]
        self.assertIn("NotNode", node_types)
        self.assertIn("GetMouseWorldPositionNode", node_types)
        self.assertIn("MovePlantNode", node_types)

        move_node = next(n for n in _ctx.nodes if n.node_type == "MovePlantNode")
        conns = ConnectionManager.get_connections()
        move_inputs = {c.target_port.name: c.source_node.node_type for c in conns if c.target_node.id == move_node.id}
        self.assertEqual(move_inputs.get("列"), "GetMouseWorldPositionNode")
        self.assertEqual(move_inputs.get("行"), "GetMouseWorldPositionNode")

    def test_bind_object_get_bound_plant_and_mouse_runtime_ports(self):
        from PvZ_Fusion_Transpiler.Core.connection_manager import ConnectionManager
        _ctx.clear()
        ConnectionManager.clear()

        found = pft.BoolVar(name="found")
        with pft.Trigger.OnKeyDown(KeyCode.K):
            with pft.Lawnf.for_each_plant_on_lawn() as plant:
                with pft.If((plant.plantType == pft.PlantType.SunFlower) & (found == False)):
                    bind_node = pft.Object.bind(pft.Object.from_plant(plant), "sunflower")
                    found.set(True)

        with pft.Trigger.OnGameStart():
            with pft.Time.OnFixedUpdate(5):
                bound_p = pft.Object.get_bound_plant("sunflower")
                bound_p.move(pft.Mouse.col, pft.Mouse.row)
                pos_port = pft.Mouse.position

        conns = ConnectionManager.get_connections()

        # Verify BindObjectNode runtime ports and connections
        self.assertEqual(bind_node.port_input_trigger_Trigger.name, "Trigger")
        self.assertEqual(bind_node.port_input_string_Name.name, "Name")
        self.assertEqual(bind_node.port_input_gameobject_GameObject.name, "Object")
        self.assertEqual(bind_node.port_output_trigger_Complete.name, "On Complete")
        self.assertEqual(bind_node.port_output_trigger_Failed.name, "Game Over")

        bind_in = {c.target_port.name: (c.source_node.node_type, c.source_port.name) for c in conns if c.target_node.id == bind_node.id}
        self.assertEqual(bind_in.get("Trigger"), ("BranchNode", "真（触发）"))
        self.assertEqual(bind_in.get("Name"), ("StringValueNode", "值"))
        self.assertEqual(bind_in.get("Object"), ("PlantToObjectNode", "Object"))

        # Verify GetBoundPlantNode runtime ports and connections
        gbp_node = next(n for n in _ctx.nodes if n.node_type == "GetBoundPlantNode")
        self.assertEqual(gbp_node.port_input_string_Name.name, "Name")
        self.assertEqual(gbp_node.port_output_plant_Plant.name, "Plant")
        self.assertEqual(gbp_node.port_output_bool_Exists.name, "Exists")
        self.assertEqual(gbp_node.dump_data().get("bindingName"), "sunflower")
        gbp_out = [(c.source_port.name, c.target_node.node_type, c.target_port.name) for c in conns if c.source_node.id == gbp_node.id]
        self.assertEqual(gbp_out, [("Plant", "MovePlantNode", "植物")])

        # Verify GetMouseWorldPositionNode runtime ports and connections
        mouse_nodes = [n for n in _ctx.nodes if n.node_type == "GetMouseWorldPositionNode"]
        self.assertEqual(len(mouse_nodes), 3)
        for mn in mouse_nodes:
            self.assertEqual(mn.port_output_vector3_Position.name, "Coordinates")
            self.assertEqual(mn.port_output_int_Row.name, "Lane")
            self.assertEqual(mn.port_output_int_Col.name, "Column")
        self.assertEqual(pos_port.name, "Coordinates")

        mouse_out_ports = sorted(
            (c.source_port.name, c.target_port.name)
            for c in conns
            if c.source_node.node_type == "GetMouseWorldPositionNode"
        )
        self.assertEqual(mouse_out_ports, [("Column", "列"), ("Lane", "行")])

        # Verify sequential fallback auto-wiring from BindObjectNode when on trigger_stack
        _ctx.clear()
        ConnectionManager.clear()
        with pft.Trigger.OnGameStart():
            _ctx.trigger_stack.pop()
            b = pft.Object.bind(pft.Object.create("Pin"), "pin")
            _ctx.trigger_stack.append(b)
            pft.Game.Stage.change("next")
        seq_conns = ConnectionManager.get_connections()
        b_out = [c for c in seq_conns if c.source_node.id == b.id and c.target_node.node_type == "ChangeStageNode"]
        self.assertEqual(len(b_out), 1)
        self.assertEqual(b_out[0].source_port.name, "On Complete")
        self.assertNotIn("out_trigger", b.dump_data())

        # Verify dynamic StringVar name connects to GetBoundPlantNode.Name input
        _ctx.clear()
        ConnectionManager.clear()
        tag = pft.StringVar("sunflower", name="tag")
        dyn_plant = pft.Object.get_bound_plant(tag)
        self.assertIsNotNone(dyn_plant.ref)
        dyn_gbp = next(n for n in _ctx.nodes if n.node_type == "GetBoundPlantNode")
        dyn_in = [c for c in ConnectionManager.get_connections() if c.target_node.id == dyn_gbp.id]
        self.assertEqual(len(dyn_in), 1)
        self.assertEqual(dyn_in[0].target_port.name, "Name")
        self.assertEqual(dyn_in[0].source_node.node_type, "GetStringVariableValueNode")


if __name__ == "__main__":
    unittest.main()
