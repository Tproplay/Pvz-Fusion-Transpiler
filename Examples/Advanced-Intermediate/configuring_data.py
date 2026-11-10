import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import (
    PlantType,
    ZombieType,
    PlantData,
    PlantEntry,
    OrderedSpawn,
)
from PvZ_Fusion_Transpiler.Types import (
    SceneType,
    LevelType,
    TravelBuffType,
)

# =====================================================================
# 1. FILE & COMPILER CONFIGURATION
# =====================================================================
pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

# =====================================================================
# 2. GENERAL LEVEL METADATA (via pft.level_config)
# =====================================================================
pft.level_config.level_number = 8001
pft.level_config.scene_type = SceneType.SnowPool
pft.level_config.level_type = LevelType.CustomLevel
pft.level_config.start_sun = 1500
pft.level_config.max_wave = 10
pft.level_config.card_count = 8
pft.level_config.victory_type = 0  # 0: Defeat all waves

# Pre-selected Card Deck & Available Spawner Pool (Enums unwrapped automatically)
pft.level_config.pre_select_cards = [
    PlantType.SunFlower,
    PlantType.Peashooter,
    PlantType.WallNut,
    PlantType.CherryBomb,
    PlantType.LilyPad,
    PlantType.Squash,
]

pft.level_config.pre_select_cards_zombie = [
    ZombieType.NormalZombie,
    ZombieType.ConeZombie,
]

pft.level_config.spawn_zombies = [
    ZombieType.NormalZombie,
    ZombieType.ConeZombie,
    ZombieType.BucketZombie,
    ZombieType.FootballZombie,
    ZombieType.Gargantuar,
]

# Buff & Debuff Arrays
pft.level_config.adv_buffs = [
    TravelBuffType.BackupSupply,
    TravelBuffType.SolarReserve,
]
pft.level_config.ulti_buffs = [0, 2]
pft.level_config.ulti_buffs2 = [1]
pft.level_config.travel_debuffs = []

# =====================================================================
# 3. BOARD CONFIGURATION (pft.level_config.board_config)
# =====================================================================
pft.level_config.board_config.startTip = "Welcome to the Complete Configuration Demo!"
pft.level_config.board_config.tipTime = 7.0
pft.level_config.board_config.redLineColumn = 4
pft.level_config.board_config.waveInterval = 25.0
pft.level_config.board_config.firstWaveArrivedTimer = 15.0
pft.level_config.board_config.conveyInterval = 5.0
pft.level_config.board_config.gloveSpeed = 12.0

# Multipliers
pft.level_config.board_config.zombieHealthMultiplier = 1.2
pft.level_config.board_config.zombieDamageMultiplier = 1.0
pft.level_config.board_config.zombieSpeedMultiplier = 1.1
pft.level_config.board_config.zombieCountMultiplier = 1.0
pft.level_config.board_config.zombieStartAmmor = 0.0

# Speed limits
pft.level_config.board_config.minOriginalSpeed = 1.0
pft.level_config.board_config.maxOriginalSpeed = 1.5

# Hold Timers
pft.level_config.board_config.holdTimer = 4.0
pft.level_config.board_config.holdTimer2 = 2.0
pft.level_config.board_config.holdTimer3 = 5.0

# Randomizer Scaling Bounds
pft.level_config.board_config.applyRandomData = True
pft.level_config.board_config.plantModifyMin = 0.5
pft.level_config.board_config.plantModifyMax = 3.0
pft.level_config.board_config.plantSpeedMin = 0.5
pft.level_config.board_config.plantSpeedMax = 2.5
pft.level_config.board_config.plantSpeedAvg = 1.5
pft.level_config.board_config.zombieModifyMin = 0.5
pft.level_config.board_config.zombieModifyMax = 5.0
pft.level_config.board_config.zombieModifyAvg = 2.0
pft.level_config.board_config.zombieSpeedMin = 0.5
pft.level_config.board_config.zombieSpeedMax = 3.0
pft.level_config.board_config.zombieSpeedAvg = 1.2
pft.level_config.board_config.zombieScaleMin = 0.8
pft.level_config.board_config.zombieScaleMax = 1.8
pft.level_config.board_config.zombieScaleAvg = 1.0

# =====================================================================
# 4. BOARD TAG MODIFIERS (pft.level_config.board_tag)
# =====================================================================
pft.level_config.board_tag.isNight = True
pft.level_config.board_tag.disableMower = False
pft.level_config.board_tag.zombieDropSun = True
pft.level_config.board_tag.waveLeaders = True
pft.level_config.board_tag.enableTravelBuff = True
pft.level_config.board_tag.isFreeCardSelect = False
pft.level_config.board_tag.disableNormalSun = False

# =====================================================================
# 5. CUSTOM PLANT STAT OVERRIDES (plantDatas)
# =====================================================================
# Override Sunflower cost, recharge, and health
pft.level_config.add_plant_data(
    PlantData.create(
        plant_type=PlantType.SunFlower,
        cost=25,
        cd=3.0,
        max_health=500,
        produce_interval=15.0,
    )
)

# Override Peashooter damage
pft.level_config.add_plant_data(
    PlantData.create(
        plant_type=PlantType.Peashooter,
        cost=100,
        cd=5.0,
        max_health=300,
        attack_damage=40,
        attack_interval=1.2,
    )
)

# =====================================================================
# 6. INITIAL PRE-PLACED PLANTS (plants)
# =====================================================================
# Place a Wall-Nut at row 3, col 2 with 8000 HP
pft.level_config.add_plant(
    PlantEntry.create(
        row=3,
        col=2,
        plant_type=PlantType.WallNut,
        health=8000,
    )
)

# Place a Sunflower at row 2, col 1
pft.level_config.add_plant(
    PlantEntry.create(
        row=2,
        col=1,
        plant_type=PlantType.SunFlower,
        health=500,
    )
)

# =====================================================================
# 7. WAVE ORDERED SPAWN LAYOUT (orderedSpawns)
# =====================================================================
# Add Wave 5 using OrderedSpawn.create() with (ZombieType, row) tuples
pft.level_config.add_ordered_spawn(
    OrderedSpawn.create(
        wave=5,
        zombies=[ZombieType.FlagZombie],
        zombies_with_row=[
            (ZombieType.FootballZombie, 3),
            (ZombieType.Gargantuar, 3),
        ],
    )
)
