import PvzRH_node as pvn
from PvzRH_node import (
    SceneType, LevelType, PlantType, ZombieType, KeyCode,
    PlantData, PlantEntry, OrderedSpawn, TravelBuffType
)

# =====================================================================
# 1. FILE & COMPILER CONFIGURATION
# =====================================================================
pvn.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test"
)
# =====================================================================
# 2. GENERAL LEVEL METADATA (via pvn.level_config)
# =====================================================================
pvn.level_config.level_number = 8001
pvn.level_config.scene_type = SceneType.SnowPool
pvn.level_config.level_type = LevelType.CustomLevel
pvn.level_config.start_sun = 1500
pvn.level_config.max_wave = 10
pvn.level_config.card_count = 8
pvn.level_config.victory_type = 0  # 0: Defeat all waves

# Pre-selected Card Deck & Available Spawner Pool (Enums unwrapped automatically)
pvn.level_config.pre_select_cards = [
    PlantType.SunFlower,
    PlantType.Peashooter,
    PlantType.WallNut,
    PlantType.CherryBomb,
    PlantType.LilyPad,
    PlantType.Squash
]

pvn.level_config.pre_select_cards_zombie = [
    ZombieType.NormalZombie,
    ZombieType.ConeZombie
]

pvn.level_config.spawn_zombies = [
    ZombieType.NormalZombie,
    ZombieType.ConeZombie,
    ZombieType.BucketZombie,
    ZombieType.FootballZombie,
    ZombieType.Gargantuar
]

# Buff & Debuff Arrays
pvn.level_config.adv_buffs = [
    TravelBuffType.ADV_PLANT_RECHARGE_HALVED.value[1],
    TravelBuffType.ADV_DOUBLE_SUN_CAP_100K.value[1]
]
pvn.level_config.ulti_buffs = [0, 2]
pvn.level_config.ulti_buffs2 = [1]
pvn.level_config.travel_debuffs = []

# =====================================================================
# 3. BOARD CONFIGURATION (pvn.level_config.board_config)
# =====================================================================
pvn.level_config.board_config.startTip = "Welcome to the Complete Configuration Demo!"
pvn.level_config.board_config.tipTime = 7.0
pvn.level_config.board_config.redLineColumn = 4
pvn.level_config.board_config.waveInterval = 25.0
pvn.level_config.board_config.firstWaveArrivedTimer = 15.0
pvn.level_config.board_config.conveyInterval = 5.0
pvn.level_config.board_config.gloveSpeed = 12.0

# Multipliers
pvn.level_config.board_config.zombieHealthMultiplier = 1.2
pvn.level_config.board_config.zombieDamageMultiplier = 1.0
pvn.level_config.board_config.zombieSpeedMultiplier = 1.1
pvn.level_config.board_config.zombieCountMultiplier = 1.0
pvn.level_config.board_config.zombieStartAmmor = 0.0

# Speed limits
pvn.level_config.board_config.minOriginalSpeed = 1.0
pvn.level_config.board_config.maxOriginalSpeed = 1.5

# Hold Timers
pvn.level_config.board_config.holdTimer = 4.0
pvn.level_config.board_config.holdTimer2 = 2.0
pvn.level_config.board_config.holdTimer3 = 5.0

# Randomizer Scaling Bounds
pvn.level_config.board_config.applyRandomData = True
pvn.level_config.board_config.plantModifyMin = 0.5
pvn.level_config.board_config.plantModifyMax = 3.0
pvn.level_config.board_config.plantSpeedMin = 0.5
pvn.level_config.board_config.plantSpeedMax = 2.5
pvn.level_config.board_config.plantSpeedAvg = 1.5
pvn.level_config.board_config.zombieModifyMin = 0.5
pvn.level_config.board_config.zombieModifyMax = 5.0
pvn.level_config.board_config.zombieModifyAvg = 2.0
pvn.level_config.board_config.zombieSpeedMin = 0.5
pvn.level_config.board_config.zombieSpeedMax = 3.0
pvn.level_config.board_config.zombieSpeedAvg = 1.2
pvn.level_config.board_config.zombieScaleMin = 0.8
pvn.level_config.board_config.zombieScaleMax = 1.8
pvn.level_config.board_config.zombieScaleAvg = 1.0

# =====================================================================
# 4. BOARD TAG MODIFIERS (pvn.level_config.board_tag)
# =====================================================================
pvn.level_config.board_tag.isNight = True
pvn.level_config.board_tag.disableMower = False
pvn.level_config.board_tag.zombieDropSun = True
pvn.level_config.board_tag.waveLeaders = True
pvn.level_config.board_tag.enableTravelBuff = True
pvn.level_config.board_tag.isFreeCardSelect = False
pvn.level_config.board_tag.disableNormalSun = False

# =====================================================================
# 5. CUSTOM PLANT STAT OVERRIDES (plantDatas)
# =====================================================================
# Override Sunflower cost, recharge, and health
pvn.level_config.add_plant_data(
    PlantData.create(
        plant_type=PlantType.SunFlower,
        cost=25,
        cd=3.0,
        max_health=500,
        produce_interval=15.0
    )
)

# Override Peashooter damage
pvn.level_config.add_plant_data(
    PlantData.create(
        plant_type=PlantType.Peashooter,
        cost=100,
        cd=5.0,
        max_health=300,
        attack_damage=40,
        attack_interval=1.2
    )
)

# =====================================================================
# 6. INITIAL PRE-PLACED PLANTS (plants)
# =====================================================================
# Place a Wall-Nut at row 3, col 2 with 8000 HP
pvn.level_config.add_plant(
    PlantEntry.create(
        row=3,
        col=2,
        plant_type=PlantType.WallNut,
        health=8000
    )
)

# Place a Sunflower at row 2, col 1
pvn.level_config.add_plant(
    PlantEntry.create(
        row=2,
        col=1,
        plant_type=PlantType.SunFlower,
        health=500
    )
)

# =====================================================================
# 7. WAVE ORDERED SPAWN LAYOUT (orderedSpawns)
# =====================================================================

# Add Wave 5 using OrderedSpawn.create() with (ZombieType, row) tuples
pvn.level_config.add_ordered_spawn(
    OrderedSpawn.create(
        wave=5,
        zombies=[ZombieType.FlagZombie],
        zombies_with_row=[
            (ZombieType.FootballZombie, 3),
            (ZombieType.Gargantuar, 3)
        ]
    )
)

# =====================================================================
# 8. GLOBAL VARIABLES & GRAPH EVENT LOGIC
# =====================================================================
rng = pvn.Random.Seeded(seed=12345, name="Demo_PRNG")
spawn_counter = pvn.IntVar(start_val=0, name="Spawns_Count")

def main():
    global rng, spawn_counter
    # Board start event
    with pvn.Trigger.OnBoardStart():
        pvn.InGameUI.display_text("Level Loaded! Press [SPACE] to spawn random plant, [R] to add Sun.", duration=5.0)

    # Key [SPACE]: Spawn seeded random plant
    with pvn.Trigger.OnKeyDown(KeyCode.Space):
        rand_row = rng.randint(1, 5)
        rand_col = rng.randint(1, 8)
        
        pvn.Spawner.Set_Plant(row=rand_row, col=rand_col, plant_type=PlantType.Peashooter)
        spawn_counter += 1
        pvn.InGameUI.display_text("Spawned Peashooter #", spawn_counter, " at (", rand_row, ", ", rand_col, ")")

    # Key [R]: Add 500 Sun
    with pvn.Trigger.OnKeyDown(KeyCode.R):
        pvn.Board.Sun += 500
        pvn.InGameUI.display_text("Added +500 Sun!", duration=2.0)

# Register the logic graph to automatically export JSON on exit
pvn.add_graph(main)