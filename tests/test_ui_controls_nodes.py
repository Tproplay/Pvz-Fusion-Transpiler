import unittest
import warnings
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import (
    MusicType,
    SceneType,
    BulletType,
    ToolType,
    EventToolType,
    EventGridObstacle,
    EventZombieStat,
    EventZombieStatus,
    EventBulletProperty,
    EventWorldEffect,
    EventTravelEntryKind,
    EventArithmeticOperation,
    Layer,
    ListStorageOperation,
    BuffType,
    PlantType,
    ZombieType,
)
from PvZ_Fusion_Transpiler.Core import _ctx
from PvZ_Fusion_Transpiler.Core.connection_manager import Port, PortDirection, PortType as CorePortType
from PvZ_Fusion_Transpiler._Nodes.Original.node import Node
from PvZ_Fusion_Transpiler import nodes


class DummyEntityNode(Node):
    node_type = "DummyEntityNode"

    def __init__(self):
        super().__init__()
        self.port_zombie = self.create_port("僵尸", PortDirection.Output, CorePortType.Zombie)
        self.port_bullet = self.create_port("子弹", PortDirection.Output, CorePortType.Bullet)


class TestUIControlsNodes(unittest.TestCase):
    def setUp(self):
        _ctx.clear()

    def test_suggested_nodes_field_serialization(self):
        """Test all 14 EventSuggestedNode subclasses serialize their in-editor UI fields to JSON."""
        # 1. ChangeEventMusicNode
        m_node = nodes.change_event_music(music=MusicType.Night)
        m_data = m_node.dump_data()
        self.assertEqual(m_data["music"], int(MusicType.Night.value))

        # 2. ChangeEventMapNode
        map_node = nodes.change_event_map(scene=SceneType.Roof)
        map_data = map_node.dump_data()
        self.assertEqual(map_data["scene"], int(SceneType.Roof.value))

        # 3. BulletTypeValueNode
        b_node = nodes.bullet_type_value(bullet_type=BulletType.Bullet_pea)
        b_data = b_node.dump_data()
        self.assertEqual(b_data["bulletType"], int(BulletType.Bullet_pea.value))

        # 4. ToolTypeValueNode
        t_node = nodes.tool_type_value(tool_type=ToolType.Hammer)
        t_data = t_node.dump_data()
        self.assertEqual(t_data["toolType"], int(ToolType.Hammer.value))

        # 5. DeleteGridItemsNode
        d_node = nodes.delete_grid_items(row=1, column=2, kind=EventGridObstacle.Ladder)
        d_data = d_node.dump_data()
        self.assertEqual(d_data["kind"], int(EventGridObstacle.Ladder.value))

        # 6. FloatVariableArithmeticNode
        f_node = nodes.float_variable_arithmetic(operation=EventArithmeticOperation.Multiply)
        f_data = f_node.dump_data()
        self.assertEqual(f_data["operation"], int(EventArithmeticOperation.Multiply.value))

        # 7. IntVariableArithmeticNode
        i_node = nodes.int_variable_arithmetic(operation=EventArithmeticOperation.Subtract)
        i_data = i_node.dump_data()
        self.assertEqual(i_data["operation"], int(EventArithmeticOperation.Subtract.value))

        # 8. GetZombieStatsNode
        gz_node = nodes.get_zombie_stats(stat=EventZombieStat.BodyHP)
        gz_data = gz_node.dump_data()
        self.assertEqual(gz_data["stat"], int(EventZombieStat.BodyHP.value))

        # 9. SetZombieStatsNode
        sz_node = nodes.set_zombie_stats(value=500.0, stat=EventZombieStat.BaseSpeed)
        sz_data = sz_node.dump_data()
        self.assertEqual(sz_data["stat"], int(EventZombieStat.BaseSpeed.value))

        # 10. GetZombieStatusNode
        gst_node = nodes.get_zombie_status(status=EventZombieStatus.FreezeSeconds)
        gst_data = gst_node.dump_data()
        self.assertEqual(gst_data["status"], int(EventZombieStatus.FreezeSeconds.value))

        # 11. SetZombieStatusNode
        sst_node = nodes.set_zombie_status(value=5.0, status=EventZombieStatus.PoisonSeconds)
        sst_data = sst_node.dump_data()
        self.assertEqual(sst_data["status"], int(EventZombieStatus.PoisonSeconds.value))

        # 12. ModifyEventBulletNode
        mb_node = nodes.modify_event_bullet(prop=EventBulletProperty.Damage)
        mb_data = mb_node.dump_data()
        self.assertEqual(mb_data["property"], int(EventBulletProperty.Damage.value))

        # 13. OnWorldPlantEffectNode
        we_node = nodes.on_world_plant_effect(effect=EventWorldEffect.Jalapeno)
        we_data = we_node.dump_data()
        self.assertEqual(we_data["effect"], int(EventWorldEffect.Jalapeno.value))

        # 14. RemoveTravelEntryNode
        re_node = nodes.remove_travel_entry(name_or_id="buff1", kind=EventTravelEntryKind.UltimateModifier)
        re_data = re_node.dump_data()
        self.assertEqual(re_data["kind"], int(EventTravelEntryKind.UltimateModifier.value))

    def test_event_node_base_ui_serialization(self):
        """Test EventNodeBase subclasses with UI controls serialize their fields."""
        # Layer node
        layer_node = nodes.get_plants_on_layer(layer=Layer.Pumpkin)
        l_data = layer_node.dump_data()
        self.assertEqual(l_data["layer"], int(Layer.Pumpkin.value))

        # PlantTypeListStorageNode
        storage_node = nodes.plant_type_list_storage(operation=ListStorageOperation.Remove)
        s_data = storage_node.dump_data()
        self.assertEqual(s_data["operation"], int(ListStorageOperation.Remove.value))

        # GetTravelEntryNode
        travel_node = nodes.get_travel_entry(buff_type=BuffType.Debuff, entry_index=3)
        t_data = travel_node.dump_data()
        self.assertEqual(t_data["buffType"], int(BuffType.Debuff.value))
        self.assertEqual(t_data["entryIndex"], 3)

    def test_rule_4_enum_validation(self):
        """Test Rule 4: mismatched enum types raise TypeError, int emits DeprecationWarning."""
        # Mismatched enum raises TypeError
        with self.assertRaises(TypeError):
            nodes.change_event_music(music=ZombieType.NormalZombie)

        with self.assertRaises(TypeError):
            nodes.change_event_map(scene=PlantType.Peashooter)

        # Passing raw int emits DeprecationWarning and succeeds
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            node = nodes.change_event_music(music=4)
            self.assertEqual(node.music, MusicType.Night)
            self.assertTrue(any(issubclass(item.category, DeprecationWarning) for item in w))

    def test_high_level_extensions_ui_controls(self):
        """Test high-level extensions pass typed enum arguments cleanly."""
        # Lawnf
        m_res = pft.Lawnf.change_music(MusicType.Loon)
        self.assertIsNotNone(m_res)

        map_res = pft.Lawnf.change_map(SceneType.Night)
        self.assertIsNotNone(map_res)

        del_res = pft.Lawnf.delete_grid_items(0, 0, EventGridObstacle.Crater)
        self.assertIsNotNone(del_res)

        # Zombie convenience methods with properly-typed Zombie Port
        dummy = DummyEntityNode()
        z_dummy = pft.Zombie(dummy.port_zombie)
        hp_port = z_dummy.hp
        self.assertEqual(hp_port.node.stat, EventZombieStat.BodyHP)

        speed_port = z_dummy.speed
        self.assertEqual(speed_port.node.stat, EventZombieStat.BaseSpeed)

        sz_op = z_dummy.set_hp(300.0)
        self.assertEqual(sz_op.stat, EventZombieStat.BodyHP)

        # Bullet convenience methods with properly-typed Bullet Port
        b_dummy = pft.Bullet(dummy.port_bullet)
        b_op = b_dummy.set_speed(3.5)
        self.assertEqual(b_op.property, EventBulletProperty.Speed)

        b_dmg = b_dummy.set_damage(100.0)
        self.assertEqual(b_dmg.property, EventBulletProperty.Damage)

        # Trigger
        with pft.Trigger.OnWorldPlantEffect(EventWorldEffect.Jalapeno) as row_port:
            self.assertIsNotNone(row_port)


if __name__ == "__main__":
    unittest.main()
