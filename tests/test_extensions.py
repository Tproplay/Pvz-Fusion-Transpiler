import unittest
import json
import os
import shutil
import tempfile

import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Core.context import _ctx
from PvZ_Fusion_Transpiler.Core.connection_manager import PortType, ConnectionManager
from PvZ_Fusion_Transpiler.Data.TypeMgr import PlantType, ZombieType, KeyCode, TravelBuffType, SoundType, BulletType
from PvZ_Fusion_Transpiler._Nodes.Extentions import (
    If,
    Switch,
    IntVar,
    FloatVar,
    BoolVar,
    Plant,
    Zombie,
    Bullet,
    ForEachPlant,
    ForEachPlantType,
    ForEachZombieType,
    PlantTypeList,
    ZombieTypeList,
    While,
    For,
    Time,
    Mouse,
    Random,
    Option,
    MultiSelectMenu,
    InfoCard,
    Trigger,
    Spawner,
    SpawnedPlant,
    SpawnedZombie,
    SpawnedBullet,
    Game,
    Board,
    Lawnf,
    InGameUI,
    format_string,
)



class TestExtensions(unittest.TestCase):

    def setUp(self):
        _ctx.clear()
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        _ctx.clear()
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_variables_arithmetic_and_comparison(self):
        i1 = IntVar(10, name="VarA")
        i2 = IntVar(20, name="VarB")
        
        # Test operators create nodes
        add_port = i1 + i2
        self.assertIsNotNone(add_port)
        
        cmp_port = i1 < i2
        self.assertIsNotNone(cmp_port)

        # In-place operations
        i1 += 5
        self.assertGreater(len(_ctx.nodes), 2)

        # FloatVar
        f1 = FloatVar(3.14, name="FloatA")
        f2 = f1 * 2.0
        self.assertIsNotNone(f2)

        # BoolVar
        b1 = BoolVar(True, name="BoolA")
        not_b = ~b1
        self.assertIsNotNone(not_b)

    def test_branching_if(self):
        x = IntVar(5, name="X")
        with Trigger.OnGameStart():
            with If(x == 5) as branch:
                x.set(10)
                with branch.Else:
                    x.set(0)

        self.assertGreater(len(_ctx.nodes), 2)
        self.assertGreater(len(pft.ConnectionManager.get_connections()), 0)

    def test_branching_switch(self):
        x = IntVar(2, name="Choice")
        with Trigger.OnGameStart():
            with Switch(x) as sw:
                with sw.case(1):
                    x.set(100)
                with sw.case(2):
                    x.set(200)
                with sw.default:
                    x.set(-1)

        self.assertGreater(len(_ctx.nodes), 3)

    def test_loops_while_and_for(self):
        counter = IntVar(0, name="LoopCounter")
        with Trigger.OnGameStart():
            with While(counter < 5):
                counter += 1

            with For(10) as loop:
                idx = loop.index
                self.assertIsNotNone(idx)

    def test_time_extensions(self):
        with Trigger.OnBoardStart():
            with Time.Wait(2.5):
                with Time.OnFixedUpdate(interval=0.2) as update:
                    tick = update.tick
                    self.assertIsNotNone(tick)

    def test_triggers_and_mouse(self):
        with Trigger.OnMouseClick() as mouse:
            col = mouse.col
            row = mouse.row
            is_left = mouse.isLeftClick
            self.assertIsNotNone(col)
            self.assertIsNotNone(row)
            self.assertIsNotNone(is_left)

        with Trigger.OnKeyDown(KeyCode.Space):
            pass

        with Trigger.OnWave() as wave_num:
            self.assertIsNotNone(wave_num)

        with Trigger.OnPlantCreate() as plant:
            ptype = plant.plantType
            self.assertIsNotNone(ptype)

        with Trigger.OnZombieSpawn() as zombie:
            ztype = zombie.zombieType
            self.assertIsNotNone(ztype)

    def test_random_extensions(self):
        r_int = Random.randint(1, 100)
        self.assertIsNotNone(r_int)

        r_float = Random.randf(0.0, 1.0)
        self.assertIsNotNone(r_float)

        with Trigger.OnGameStart():
            with Random.TriggerChance(0.5):
                pass
            with Random.RandomTrigger(count=1):
                pass

        # Seeded
        rng = Random.Seeded(42, name="TestRNG")
        val = rng.randint(5, 15)
        self.assertIsNotNone(val)

    def test_ui_extensions(self):
        card = InfoCard("Title", "Subtitle")
        self.assertIsNotNone(card.node)

        menu = MultiSelectMenu(is_rerollable=True, reroll_count=2)
        menu.add_option(
            title="Option 1",
            description="First choice",
            plant_type=PlantType.Peashooter,
        )
        menu.add_option(
            title="Option 2",
            description="Second choice",
            plant_type=PlantType.SunFlower,
        )

        with Trigger.OnGameStart():
            menu.show()

        self.assertIsNotNone(menu._show_node_id)

    def test_spawner(self):
        with Trigger.OnGameStart():
            p_spawn = Spawner.Set_Plant(row=1, col=2, plant_type=PlantType.Peashooter)
            self.assertIsInstance(p_spawn, Plant)
            self.assertIsInstance(p_spawn, SpawnedPlant)
            self.assertIsNotNone(p_spawn.ref)
            self.assertIsNotNone(p_spawn.on_created)
            self.assertIsNotNone(p_spawn.on_failed)

            z_spawn = Spawner.Set_Zombie(row=2, col=3, zombie_type=ZombieType.NormalZombie)
            self.assertIsInstance(z_spawn, Zombie)
            self.assertIsInstance(z_spawn, SpawnedZombie)
            self.assertIsNotNone(z_spawn.ref)
            self.assertIsNotNone(z_spawn.on_created)

            # Rule 4: direct int must raise TypeError
            with self.assertRaises(TypeError):
                Spawner.Set_Plant(row=1, col=2, plant_type=0)
            with self.assertRaises(TypeError):
                Spawner.Set_Zombie(row=1, col=2, zombie_type=0)

    def test_game_sun_and_money(self):
        # Arithmetic on Game.Sun
        add_port = Game.Sun + 50
        self.assertIsNotNone(add_port)
        radd_port = 50 + Game.Sun
        self.assertIsNotNone(radd_port)
        sub_port = Game.Sun - 25
        self.assertIsNotNone(sub_port)
        mul_port = Game.Sun * 2
        self.assertIsNotNone(mul_port)
        div_port = Game.Sun / 2
        self.assertIsNotNone(div_port)
        fdiv_port = Game.Sun // 2
        self.assertIsNotNone(fdiv_port)
        mod_port = Game.Sun % 50
        self.assertIsNotNone(mod_port)

        # Comparisons
        self.assertIsNotNone(Game.Sun == 100)
        self.assertIsNotNone(Game.Sun != 100)
        self.assertIsNotNone(Game.Sun < 100)
        self.assertIsNotNone(Game.Sun <= 100)
        self.assertIsNotNone(Game.Sun > 100)
        self.assertIsNotNone(Game.Sun >= 100)

        # In-place ops and set/get
        with Trigger.OnGameStart():
            Game.Sun += 100
            Game.Sun -= 50
            Game.Sun *= 2
            Game.Sun /= 2
            Game.Sun.set(500)
            val = Game.Sun.get()
            self.assertIsNotNone(val)

            with Game.Sun.SpendSun(100) as spend:
                pass
            with spend.Failed:
                pass

        # Game.Money
        self.assertIsNotNone(Game.Money + 10)
        self.assertIsNotNone(Game.Money < 100)
        with Trigger.OnGameStart():
            Game.Money += 50
            Game.Money -= 20
            Game.Money.set(200)
            val_m = Game.Money.get()
            self.assertIsNotNone(val_m)

            with Game.Money.SpendMoney(10) as spend_m:
                pass
            with spend_m.Failed:
                pass

            Game.Money.check_money(50)

        # Board aliases
        self.assertIsNotNone(Board.Sun + 10)
        self.assertIsNotNone(Board.Money + 10)
        self.assertIsNotNone(Board.Wave)
        self.assertIsNotNone(Game.Wave)

    def test_game_buff_and_lifecycle(self):
        with Trigger.OnGameStart():
            Game.get_buff(TravelBuffType.ADV_ENCHANTRESS_SUBSPECIES)
            Game.trigger_game_over("Defeated!")
            Game.trigger_game_win()

    def test_lawnf(self):
        with Trigger.OnGameStart():
            Lawnf.spawn_particle(1, 2)
            Lawnf.spawn_grave(2, 3)
            Lawnf.spawn_crater(3, 4)
            Lawnf.spawn_ladder(4, 5)
            Lawnf.spawn_ice_block(1, 1, plant_type=PlantType.Peashooter)
            Lawnf.trigger_cherry_explosion(1, 2, damage=1800)
            Lawnf.trigger_doom_explosion(2, 3, damage=1800, create_pit=True)
            Lawnf.trigger_zombie_explosion(3, 4)
            Lawnf.trigger_jalapeno(2, damage=1800)
            Lawnf.trigger_ice_shroom(duration=4.0)
            Lawnf.play_sound(SoundType.Tap)
            Lawnf.trigger_game_over("Lost!")
            Lawnf.trigger_game_win()
            Lawnf.get_buff(TravelBuffType.ADV_OBSIDIAN_SPIKE_DAMAGE)

            closest_z = Lawnf.get_closest_zombie(1, 2)
            self.assertIsInstance(closest_z, Zombie)

            plants_cell = Lawnf.get_plants_at(1, 2)
            self.assertIsNotNone(plants_cell)

            all_plants = Lawnf.get_all_plants()
            self.assertIsNotNone(all_plants)

            with Lawnf.for_each_plant_on_lawn() as plant_entity:
                self.assertIsInstance(plant_entity, Plant)

    def test_ingame_ui(self):
        with Trigger.OnGameStart():
            InGameUI.display_info_card("Big Title", "Small Title")
            InGameUI.give_plant_card(PlantType.Peashooter, cooldown=5.0, cost=100)
            InGameUI.remove_plant_card(PlantType.Peashooter)
            InGameUI.spawn_dropped_card(1, 2, PlantType.Peashooter)
            InGameUI.display_text("Sun remaining: ", Game.Sun, duration=5.0)

            # Rule 4: raw int for card must raise TypeError
            with self.assertRaises(TypeError):
                InGameUI.give_plant_card(0)
            with self.assertRaises(TypeError):
                InGameUI.remove_plant_card(0)
            with self.assertRaises(TypeError):
                InGameUI.spawn_dropped_card(1, 2, 0)

    def test_stdlib(self):
        # format_string
        s = pft.StdLib.format_string("Level ", 1, " Wave ", Game.Wave)
        self.assertIsNotNone(s)

        # Dictionary
        d = pft.StdLib.Dictionary({"score": 0, "multiplier": 1.5, "is_active": True})
        self.assertIsNotNone(d["score"])
        self.assertIsNotNone(d.multiplier)

        # Array
        arr = pft.StdLib.Array(size=3, default_val=10)
        self.assertEqual(len(arr), 3)
        self.assertIsNotNone(arr[0])

        with Trigger.OnGameStart():
            d.score.set(100)
            arr[0].set(50)
            arr.write(0, 99)
            arr.read(0, lambda val: val.set(10))

            p = Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.Peashooter)
            wasd = pft.StdLib.WASDPlant(p)
            wasd.Start()

    def test_full_level_export_with_extensions(self):
        out_file = os.path.join(self.test_dir, "ExtLevel.json")
        pft.Config(output=self.test_dir, name="ExtLevel")

        counter = IntVar(0, name="LevelCounter")

        with Trigger.OnGameStart():
            with Time.OnFixedUpdate(interval=1.0):
                counter += 1
                with If(counter == 10):
                    Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.CherryBomb, force=True)

        pft.export()

        self.assertTrue(os.path.exists(out_file))
        with open(out_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("references", data)
        self.assertIn("eventNodeGraph", data)
        self.assertGreater(len(data["eventNodeGraph"]["nodes"]), 5)
    def test_spawner_plant_type_port_type(self):
        # Item 1: Verify connecting PlantType PortType instead of Int in Spawner.Set_Plant
        spawn = Spawner.Set_Plant(0, 0, PlantType.AbyssSwordStar)
        set_node = spawn.node
        plant_type_input = set_node.port_input_planttype_PlantType
        self.assertEqual(plant_type_input.port_type, PortType.PlantType)

        conns = plant_type_input.get_connections()
        self.assertEqual(len(conns), 1)
        src_port = conns[0].source_port
        # Crucial check: source port MUST be PlantType, not Int!
        self.assertEqual(src_port.port_type, PortType.PlantType)
        self.assertEqual(src_port.node.node_type, "PlantTypeValueNode")

    def test_spawner_context_managers(self):
        # Item 2: Verify __enter__ in Spawner classes is triggered on On Success / On Created
        with Trigger.OnGameStart():
            with Spawner.Set_Plant(0, 0, PlantType.Peashooter) as plant:
                heal_node = plant.heal(50)
                # Verify that the heal node's trigger was connected to SetPlant's OnCreated output
                heal_trigger_in = heal_node.get_input("触发")
                conns = heal_trigger_in.get_connections()
                self.assertEqual(len(conns), 1)
                self.assertEqual(conns[0].source_node.id, plant.node.id)
                self.assertEqual(conns[0].source_port.name, plant.node.port_output_trigger_OnCreated.name)

            with Spawner.Set_Zombie(0, 0, ZombieType.NormalZombie) as zombie:
                hyp_node = zombie.hypnotize()
                hyp_trigger_in = hyp_node.get_input("触发")
                conns = hyp_trigger_in.get_connections()
                self.assertEqual(len(conns), 1)
                self.assertEqual(conns[0].source_node.id, zombie.node.id)
                self.assertEqual(conns[0].source_port.name, zombie.node.port_output_trigger_OnCreated.name)

            with Spawner.Set_Bullet(row=1, col=2.0, bullet_type=BulletType.Pea) as bullet:
                mod_node = bullet.modify(15.0)
                mod_trigger_in = mod_node.get_input("触发")
                conns = mod_trigger_in.get_connections()
                self.assertEqual(len(conns), 1)
                self.assertEqual(conns[0].source_node.id, bullet.node.id)
                self.assertEqual(conns[0].source_port.name, bullet.node.port_output_trigger_Complete.name)

    def test_spawner_set_bullet_and_bullet_manipulation(self):
        # Item 3 & 6: SetBullet in Spawner and Bullet Manipulation nodes
        spawn_bullet = Spawner.Set_Bullet(
            row=1,
            col=2.5,
            bullet_type=BulletType.FirePea,
            damage=50,
            speed=8.0,
            angle=0.0,
            scale_multiplier=1.2,
        )
        self.assertIsInstance(spawn_bullet, Bullet)
        self.assertIsInstance(spawn_bullet, SpawnedBullet)
        self.assertEqual(spawn_bullet.node.node_type, "ShootEventBulletNode")
        self.assertEqual(spawn_bullet.ref.port_type, PortType.Bullet)

        # Spawner.SetBullet alias
        alias_bullet = Spawner.SetBullet(row=0, col=0.0, bullet_type=BulletType.Star)
        self.assertIsInstance(alias_bullet, SpawnedBullet)

        # BulletType strict enum check (Rule 4)
        with self.assertRaises(TypeError):
            Spawner.Set_Bullet(row=0, col=0.0, bullet_type=0)
        with self.assertRaises(TypeError):
            pft.nodes.bullet_type_value(val=0)

        # modify_event_bullet and bullet_type_value nodes directly
        bt_node = pft.nodes.bullet_type_value(val=BulletType.Melon)
        self.assertEqual(bt_node.port_output_bullettype_BulletType.port_type, PortType.BulletType)
        mod_node = spawn_bullet.modify(25.0)
        self.assertEqual(mod_node.node_type, "ModifyEventBulletNode")

    def test_plant_and_zombie_to_string(self):
        # Item 5: .ToString in Plant and Zombie wrappers
        p = Spawner.Set_Plant(0, 0, PlantType.Peashooter)
        p_str = p.ToString()
        self.assertEqual(p_str.port_type, PortType.String)
        self.assertEqual(p_str.node.node_type, "PlantTypeToStringNode")
        self.assertEqual(p.to_string().port_type, PortType.String)

        z = Spawner.Set_Zombie(0, 0, ZombieType.NormalZombie)
        z_str = z.ToString()
        self.assertEqual(z_str.port_type, PortType.String)
        self.assertEqual(z_str.node.node_type, "ZombieTypeToStringNode")
        self.assertEqual(z.to_string().port_type, PortType.String)

    def test_zombie_type_list_and_for_each(self):
        # Item 4: Zombie Type List and iteration
        zt_list = ZombieTypeList([ZombieType.NormalZombie, ZombieType.LegionZombie])
        self.assertIsNotNone(zt_list.list_port)
        self.assertEqual(zt_list.list_port.port_type, PortType.ListVariable)

        # contains
        contains_port = zt_list.contains(ZombieType.LegionZombie)
        self.assertEqual(contains_port.port_type, PortType.Bool)

        # append
        zt_list.append(ZombieType.DoomPaper)

        # index access
        first_item = zt_list[0]
        self.assertEqual(first_item.port_type, PortType.ZombieType)

        # ForEachZombieType loop
        with Trigger.OnGameStart():
            with ForEachZombieType(zt_list) as loop:
                curr_type = loop.zombie_type
                self.assertEqual(curr_type.port_type, PortType.ZombieType)
                idx = loop.index
                self.assertEqual(idx.port_type, PortType.Int)

            self.assertIsNotNone(loop.on_complete)

        # Rule 4 strict check on ZombieType input
        with self.assertRaises(TypeError):
            ZombieTypeList([0])
        with self.assertRaises(TypeError):
            zt_list.contains(0)
        with self.assertRaises(TypeError):
            zt_list.append(0)


if __name__ == "__main__":
    unittest.main()
