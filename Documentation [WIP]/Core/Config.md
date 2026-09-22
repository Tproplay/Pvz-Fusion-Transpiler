# ⚙️ Level & Compiler Configuration

The `pvn.level_config` proxy and `pvn.settings` allow you to define level metadata, board dynamics, randomizer constraints, and output formatting for your generated level JSON files.

```python
import PvzRH_node as pvn
from PvzRH_node import PlantType, ZombieType
from PvzRH_node.Types import SceneType, LevelType
```

---

## 1. Compiler & Export Settings

### Export Location

Set the destination path and file name for the compiled JSON level. If the file exists, the transpiler will update its graph and configuration data.

```python
pvn.Config(
    output=r"C:\Path\To\Saves\LevelData\Levels",
    name="MyCustomLevel"
)
```

### Visual Layout (`pvn.settings`)

The `CompilerSetting` class controls how the node graph is arranged in the visual editor.

* **`group_level`**: Set to `0` (default) for a flat grid, or `1+` to group nodes hierarchically by code statements and scopes.


* **`fold_all_groups`**: When `True`, generated groups collapse into a compact 1-node footprint.


* **`spacing_x` / `spacing_y`**: The horizontal/vertical padding between ungrouped nodes (defaults: 220.0, 170.0).


* **`hierarchical_spacing_x` / `hierarchical_spacing_y`**: The spacing between nodes inside visual groups (defaults: 240.0, 180.0).



---

## 2. Level Metadata

The `pvn.level_config` object acts as a proxy to configure the core attributes of the level.

```python
pvn.level_config.level_number = 8001
pvn.level_config.scene_type = SceneType.SnowPool
pvn.level_config.level_type = LevelType.CustomLevel
pvn.level_config.start_sun = 1500
pvn.level_config.max_wave = 10
pvn.level_config.card_count = 8
pvn.level_config.victory_type = 0  # 0: Normal, 1: IZombie
```

### Card Decks & Zombie Pools

Define which plants and zombies are available or forced in the level.

```python
# Unremovable pre-selected cards
pvn.level_config.pre_select_cards = [PlantType.SunFlower, PlantType.Peashooter]
pvn.level_config.pre_select_cards_zombie = [ZombieType.NormalZombie]

# The allowed zombie types that can spawn
pvn.level_config.spawn_zombies = [ZombieType.NormalZombie, ZombieType.ConeZombie]
```

---

## 3. Board Dynamics (`board_config`)

The `board_config` attribute modifies runtime timing, stat multipliers, and Gacha randomization rules.

```python
# Timers & UI 
pvn.level_config.board_config.startTip = "Survive the winter!"
pvn.level_config.board_config.tipTime = 6.0                 # Seconds tip is shown
pvn.level_config.board_config.waveInterval = 30.0           # Seconds between waves
pvn.level_config.board_config.firstWaveArrivedTimer = 15.0  # Initial spawn delay

# Stat Multipliers
pvn.level_config.board_config.zombieHealthMultiplier = 1.2
pvn.level_config.board_config.zombieSpeedMultiplier = 1.1

# Enable Randomizer bounds
pvn.level_config.board_config.applyRandomData = True
pvn.level_config.board_config.zombieScaleMin = 0.8
pvn.level_config.board_config.zombieScaleMax = 1.8
```

---

## 4. Game Modifiers (`board_tag`)

The `board_tag` attribute stores boolean flags for enabling specialized modes or mechanics.

| Flag | Description |
| --- | --- |
| `isNight` | Sets the level rule to night (mushrooms don't sleep). |
| `disableNormalSun` | Stops natural sun from falling from the sky. |
| `zombieDropSun` | Zombies drop sun upon taking damage or dying. |
| `disableSelectCard` | Skips the seed selection screen entirely. |
| `disableInInterlude` | Skips the initial pan-camera movement sequence. |
| `disableMower` | Removes lawnmowers from the board. |


```python
pvn.level_config.board_tag.isNight = True
pvn.level_config.board_tag.disableMower = True
```

---

## 5. Custom Entities & Spawns

### Pre-Placed Plants

Use `PlantEntry.create()` to place plants on the grid before the level begins.

```python
pvn.level_config.add_plant(
    PlantEntry.create(
        row=3,
        col=2,
        plant_type=PlantType.WallNut,
        health=8000
    )
)
```

### Custom Plant Stats

Use `add_plant_data()` to inject modified base stats (cost, cooldown, damage) for specific plants.

```python
pvn.level_config.add_plant_data(
    PlantData.create(
        plant_type=PlantType.Peashooter,
        cost=100,
        cd=5.0,
        max_health=300,
        attack_damage=40
    )
)
```

### Custom Wave Spawns

Use `OrderedSpawn.create()` to dictate exactly which zombies spawn on specific waves and rows.

```python
pvn.level_config.add_ordered_spawn(
    OrderedSpawn.create(
        wave=5,
        zombies=[ZombieType.FlagZombie],                   # Random row placement
        zombies_with_row=[(ZombieType.Gargantuar, 2)]      # Fixed row placement (Type, Row)
    )
)
```

### God Mode Plants

Use the `GodPlant` builder to configure upgrade routes and scaling stages for custom modular plants.

```python
god_peashooter = pvn.GodPlant(PlantType.Peashooter)
god_peashooter.add_route("Gatling Route")
god_peashooter.add_stage(plant_type=PlantType.Repeater, cost=200, attack_damage=40)

pvn.level_config.add_god_plant(god_peashooter)
```