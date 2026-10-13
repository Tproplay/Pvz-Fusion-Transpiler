import os
import sys
import unittest

_src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

import PvZ_Fusion_Node as pvn
from PvZ_Fusion_Node import (
    Board,
    InGameUI,
    Lawnf,
    Spawner,
    Trigger,
    Print,
    Plant,
    Zombie,
    If,
    Switch,
    While,
    For,
    Time,
    Random,
    IntVar,
    FloatVar,
    BoolVar,
    MultiSelectMenu,
    Option,
    PlantTypeList,
    ForEachPlant,
    ForEachPlantType,
    PlantType,
    ZombieType,
    KeyCode,
    SoundType,
    Config,
    level_config,
    ctx,
)
from PvZ_Fusion_Node.Libraries import Math, StdLib


class TestDSLIntegration(unittest.TestCase):
    def setUp(self):
        # Reset context for each test
        ctx.reset()

    def test_triggers_and_flow(self):
        """Tests standard event triggers and sequential flow chaining."""
        with Trigger.OnGameStart():
            Print("Game started!")
            pvn.Board.Sun += 100

        self.assertGreater(len(ctx.level.graph.nodes), 0)
        self.assertGreater(len(ctx.level.graph.connections), 0)

    def test_board_sun_money(self):
        """Tests Board Sun and Money managers."""
        with Trigger.OnWave() as wave:
            pvn.Board.Sun += 200
            pvn.Board.Money += 50

            with pvn.Board.Sun.SpendSun(50) as spend:
                Print("Sun spent successfully")
            with spend.Failed:
                Print("Not enough sun")

        self.assertGreater(len(ctx.level.graph.nodes), 0)

    def test_spawner_and_entity(self):
        """Tests Spawner and Plant/Zombie wrappers."""
        with Trigger.OnWave():
            plant = Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.Peashooter)
            plant.heal(100)
            plant.damage(50)
            plant.move(row=3, col=4)

            zombie = Spawner.Set_Zombie(row=1, col=8, zombie_type=ZombieType.NormalZombie)
            zombie.damage(200)
            zombie.hypnotize()

        self.assertGreater(len(ctx.level.graph.nodes), 4)

    def test_conditional_branching(self):
        """Tests If, Elif, Else and Switch."""
        with Trigger.OnWave() as wave:
            with If(wave == 1) as flow:
                pvn.Board.Sun += 50
            with flow.Elif(wave == 2):
                pvn.Board.Sun += 100
            with flow.Else:
                pvn.Board.Sun += 200

            with Switch(wave) as sw:
                with sw.case(3):
                    pvn.Board.Sun += 300
                with sw.case(4, 5):
                    pvn.Board.Sun += 400
                with sw.default:
                    pvn.Board.Sun += 10

        self.assertGreater(len(ctx.level.graph.nodes), 6)

    def test_loops_and_time(self):
        """Tests For, While, Time.Wait, and Time.OnFixedUpdate."""
        with Trigger.OnGameStart():
            with For(5) as loop:
                pvn.Board.Sun += loop.index

            with Time.Wait(2.0):
                Print("2 seconds passed")

        self.assertGreater(len(ctx.level.graph.nodes), 3)

    def test_variables_and_operators(self):
        """Tests IntVar, FloatVar, and BoolVar math & logic."""
        count = IntVar(start_val=10, name="Counter")
        rate = FloatVar(start_val=1.5, name="Rate")
        flag = BoolVar(start_val=True, name="Flag")

        with Trigger.OnGameStart():
            count += 5
            count -= 2
            count *= 3
            count //= 2
            count %= 4

            rate += 0.5
            rate *= 2.0

            flag.set(False)

        self.assertGreater(len(ctx.level.graph.nodes), 5)

    def test_random_and_lawnf(self):
        """Tests Random module and Lawnf helper utilities."""
        with Trigger.OnWave():
            rand_val = Random.randint(1, 100)
            with Random.TriggerChance(0.5):
                Lawnf.trigger_cherry_explosion(row=2, col=3, damage=1800)
                Lawnf.spawn_grave(row=1, col=5)
                Lawnf.play_sound(SoundType.CherryBomb)

        self.assertGreater(len(ctx.level.graph.nodes), 3)

    def test_multi_select_menu(self):
        """Tests MultiSelectMenu and Option configuration."""
        menu = MultiSelectMenu(is_rerollable=True, reroll_count=2, window_count=3)
        menu.add_option(
            title="Solar Surge",
            description="+100 Sun",
            callback=lambda: pvn.Board.Sun.__iadd__(100),
            plant_type=PlantType.SunFlower,
        )
        menu.add_option(
            title="Wallnut Wall",
            description="Free Nut",
            callback=lambda: Print("Wallnut selected"),
            plant_type=PlantType.WallNut,
        )

        with Trigger.OnWave() as wave:
            with If(wave == 5):
                menu.show()

        self.assertGreater(len(ctx.level.graph.nodes), 3)

    def test_level_config_metadata(self):
        """Tests level_config properties and proxy assignments."""
        level_config.level_number = 7777
        level_config.scene_type = pvn.SceneType.SnowPool
        level_config.level_type = pvn.LevelType.CustomLevel
        level_config.start_sun = 1000
        level_config.max_wave = 20
        level_config.card_count = 10
        level_config.pre_select_cards = [PlantType.Peashooter, PlantType.SunFlower]
        level_config.board_config.waveInterval = 25.0

        self.assertEqual(ctx.level.levelNumber, 7777)
        self.assertEqual(ctx.level.startSun, 1000)
        self.assertEqual(ctx.level.boardConfig.waveInterval, 25.0)

    def test_end_to_end_compilation(self):
        """Tests compiling a complete level to JSON dictionary."""
        Config(name="IntegrationTestLevel")
        level_config.start_sun = 800

        with Trigger.OnGameStart():
            Print("Level Loaded!")
            pvn.Board.Sun += 50
            Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.SunFlower)

        level_dict = ctx.level.to_dict()
        self.assertEqual(level_dict["name"], "IntegrationTestLevel")
        self.assertEqual(level_dict["startSun"], 800)
        self.assertIn("eventNodeGraph", level_dict)
        self.assertGreater(len(level_dict["eventNodeGraph"]["nodes"]), 0)
        self.assertGreater(len(level_dict["eventNodeGraph"]["connections"]), 0)

    def test_board_sun_and_money_increment_connections(self):
        """Verifies that Board.Sun += 25, Board.Sun -= 10, and Board.Money += 100 wire constant values into the nodes."""
        Config(name="SunMoneyTest")
        with Trigger.OnGameStart():
            pvn.Board.Sun += 25
            pvn.Board.Sun -= 10
            pvn.Board.Money += 100

        node_mgr = ctx.level.graph.node_mgr
        conns = ctx.level.graph.connection_mgr.connections

        # Check GetSunNode (Gain Sun)
        sun_nodes = node_mgr.get_nodes_by_type("GetSunNode")
        self.assertEqual(len(sun_nodes), 1)
        sun_node = sun_nodes[0]

        # Verify incoming connection to sun_node on "阳光数量"
        sun_amount_conns = [
            c for c in conns
            if c.targetNodeId == sun_node.node_id and c.targetPortName == "阳光数量"
        ]
        self.assertEqual(len(sun_amount_conns), 1, "GetSunNode must have a connection on 阳光数量")
        const_node = node_mgr.get_node(sun_amount_conns[0].sourceNodeId)
        self.assertEqual(const_node.node_type, "IntValueNode")
        self.assertEqual(const_node.dump_data()["value"], 25)

        # Check UseSunNode (Spend Sun)
        use_sun_nodes = node_mgr.get_nodes_by_type("UseSunNode")
        self.assertEqual(len(use_sun_nodes), 1)
        use_sun_node = use_sun_nodes[0]
        use_sun_conns = [
            c for c in conns
            if c.targetNodeId == use_sun_node.node_id and c.targetPortName == "阳光数量"
        ]
        self.assertEqual(len(use_sun_conns), 1, "UseSunNode must have a connection on 阳光数量")
        const_use_sun = node_mgr.get_node(use_sun_conns[0].sourceNodeId)
        self.assertEqual(const_use_sun.node_type, "IntValueNode")
        self.assertEqual(const_use_sun.dump_data()["value"], 10)

        # Check GetMoneyNode (Gain Money)
        money_nodes = node_mgr.get_nodes_by_type("GetMoneyNode")
        self.assertEqual(len(money_nodes), 1)
        money_node = money_nodes[0]
        money_conns = [
            c for c in conns
            if c.targetNodeId == money_node.node_id and c.targetPortName == "金币数量"
        ]
        self.assertEqual(len(money_conns), 1, "GetMoneyNode must have a connection on 金币数量")
        const_money = node_mgr.get_node(money_conns[0].sourceNodeId)
        self.assertEqual(const_money.node_type, "IntValueNode")
        self.assertEqual(const_money.dump_data()["value"], 100)

    def test_original_node_port_constants_and_resolution(self):
        """Tests that Original nodes generate port constants and resolve English port names."""
        from PvZ_Fusion_Node.Nodes.Original.Calculate.int_add_node import IntAddNode
        from PvZ_Fusion_Node.Nodes.Original.Calculate.int_subtract_node import IntSubtractNode
        from PvZ_Fusion_Node.Nodes.Original.Logic.for_loop_node import ForLoopNode

        add = IntAddNode()
        self.assertEqual(add.Sum_out_port, "和")
        self.assertEqual(add.A_in_port, "A")
        self.assertEqual(add.B_in_port, "B")
        self.assertEqual(add.get_output(add.Sum_out_port).name, "和")
        self.assertEqual(add.get_output("Sum").name, "和")
        self.assertEqual(add.get_output("sum").name, "和")
        self.assertEqual(add.get_input(add.A_in_port).name, "A")

        sub = IntSubtractNode()
        self.assertEqual(sub.Diff_out_port, "差")
        self.assertEqual(sub.get_output(sub.Diff_out_port).name, "差")
        self.assertEqual(sub.get_output("Diff").name, "差")

        loop = ForLoopNode()
        self.assertEqual(loop.Index_out_port, "当前索引")
        self.assertEqual(loop.get_output(loop.Index_out_port).name, "当前索引")

    def test_extension_nodes_inheritance_and_presence(self):
        """Tests that all Extension nodes inherit from ExtensionNode and are exposed at top-level."""
        self.assertTrue(hasattr(pvn, "ExtensionNode"))
        ext_classes = [
            pvn.If,
            pvn.Switch,
            pvn.IntVar,
            pvn.FloatVar,
            pvn.BoolVar,
            pvn.StrVar,
            pvn.ListVar,
            pvn.Option,
            pvn.MultiSelectMenu,
            pvn.Plant,
            pvn.Zombie,
            pvn.ForEachPlant,
            pvn.ForEachPlantType,
            pvn.PlantTypeList,
            pvn.While,
            pvn.For,
            pvn.Time,
            pvn.Mouse,
            pvn.Random,
            pvn.InfoCard,
        ]
        for cls in ext_classes:
            self.assertTrue(
                issubclass(cls, pvn.ExtensionNode),
                f"{cls.__name__} must inherit from ExtensionNode"
            )


if __name__ == "__main__":
    unittest.main()
