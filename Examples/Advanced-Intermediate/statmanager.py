import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.StdLib import StatManager
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType, KeyCode

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

# 1. Initialize StatManager
stats = StatManager(base_plant_stat=0, base_zombie_hp_mult=1.0)

# 2. Register Category Tags
stats.create_tag("PeaFamily", [PlantType.Peashooter, PlantType.GatlingPea])
stats.create_zombie_tag("ToughZombies", [ZombieType.BucketZombie, ZombieType.Gargantuar])

# Hook stats into spawn triggers
with pft.Trigger.OnPlantCreate() as plant:
    stats.apply_stats_to_plant(plant)

with pft.Trigger.OnZombieSpawn() as zombie:
    stats.apply_stats_to_zombie(zombie)

# Dynamic Buffs: Wave 5+ Tough Zombies gain +20% HP
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num >= 5):
        stats.add_zombie_tag_hp("ToughZombies", 0.20)

# Key [1]: Upgrade Pea Family ATK (+25%) for 200 Sun
with pft.Trigger.OnKeyDown(KeyCode.Alpha1):
    with pft.Board.Sun.SpendSun(200):
        stats.add_tag_atk("PeaFamily", 0.25)
        stats.refresh_all_plants()

# Key [2]: Upgrade Gatling Pea individually (+50% ATK)
with pft.Trigger.OnKeyDown(KeyCode.Alpha2):
    with pft.Board.Sun.SpendSun(300):
        stats.add_plant_atk(PlantType.GatlingPea, 0.50)
        stats.refresh_all_plants()
