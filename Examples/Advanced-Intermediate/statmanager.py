import PvzRH_node as pvn
from PvzRH_node.StdLib import StatManager
from PvzRH_node.Types import PlantType, ZombieType, KeyCode

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

pvn.settings.group_level = 1

# 1. Initialize StatManager
stats = StatManager(base_plant_stat=0, base_zombie_hp_mult=1.0)

# 2. Register Category Tags
stats.create_tag("PeaFamily", [PlantType.Peashooter, PlantType.GatlingPea])
stats.create_zombie_tag("ToughZombies", [ZombieType.BucketZombie, ZombieType.Gargantuar])

def main():
    # Hook stats into spawn triggers
    with pvn.Trigger.OnPlantCreate() as plant:
        stats.apply_stats_to_plant(plant)

    with pvn.Trigger.OnZombieSpawn() as zombie:
        stats.apply_stats_to_zombie(zombie)

    # Dynamic Buffs: Wave 5+ Tough Zombies gain +20% HP
    with pvn.Trigger.OnWave() as wave_num:
        with pvn.If(wave_num >= 5):
            stats.add_zombie_tag_hp("ToughZombies", 0.20)

    # Key [1]: Upgrade Pea Family ATK (+25%) for 200 Sun
    with pvn.Trigger.OnKeyDown(KeyCode.Alpha1):
        with pvn.Board.Sun.SpendSun(200):
            stats.add_tag_atk("PeaFamily", 0.25)
            stats.refresh_all_plants()

    # Key [2]: Upgrade Gatling Pea individually (+50% ATK)
    with pvn.Trigger.OnKeyDown(KeyCode.Alpha2):
        with pvn.Board.Sun.SpendSun(300):
            stats.add_plant_atk(PlantType.GatlingPea, 0.50)
            stats.refresh_all_plants()

pvn.add_graph(main)