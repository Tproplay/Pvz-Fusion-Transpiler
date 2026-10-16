import unittest
import json
import os
import shutil
import tempfile

import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Core.context import _ctx
from PvZ_Fusion_Transpiler.Data.TypeMgr import PlantType, ZombieType, KeyCode, TravelBuffType, SoundType
from PvZ_Fusion_Transpiler._Nodes.Extentions import (
    If,
    Switch,
    IntVar,
    FloatVar,
    BoolVar,
    Plant,
    Zombie,
    ForEachPlant,
    ForEachPlantType,
    PlantTypeList,
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
        self.assertGreater(len(data["eventNodeGraph"]["connections"]), 3)


if __name__ == "__main__":
    unittest.main()
