# 🏷️ Types, Enums & Builders

The `PvzRH_node.Types` module exposes all essential game enumerations, input codes, animation constants, and data factory builders required to configure custom levels and script node logic.

```python
import PvzRH_node as pvn
from PvzRH_node.Types import PlantType, ZombieType, KeyCode, PlantEntry
```

---

## 1. Game Enums

Use these Enums to reference game assets and states safely without memorizing raw integer IDs. The transpiler automatically unwraps them into JSON-compatible values.

### Core Entities & States

* **`PlantType`**: Contains IDs for all vanilla and custom modded plants (e.g., `PlantType.Peashooter`, `PlantType.UltimateGatling`, `PlantType.SuperMachineNut`).


* **`ZombieType`**: Contains IDs for all zombies and bosses (e.g., `ZombieType.NormalZombie`, `ZombieType.Gargantuar`, `ZombieType.UltimateFootballZombie`).


* **`SceneType`**: Defines the visual background and lane behavior of the level (e.g., `SceneType.Day`, `SceneType.Pool`, `SceneType.SnowPool`).


* **`LevelType`**: Defines the gameplay mode and UI (e.g., `LevelType.CustomLevel`, `LevelType.Survival`).


* **`SoundType`**: Audio clip IDs for playing SFX (e.g., `SoundType.Splat`, `SoundType.CherryBomb`, `SoundType.HugeWave`).


* **`Plant_DieReason`**: Constants representing how a plant was removed (e.g., `ByZombie`, `ByShovel`, `ByLevelUp`).


* **`TravelBuffType`**: Registry of rogue-lite modifiers and mastery synergies (e.g., `ADV_PLANT_RECHARGE_HALVED`, `ULTI_DOOMINATOR_SPEED_X3`).



---

## 2. Input & Animations

### `KeyCode`

Maps standard keyboard keys to numerical IDs for use with `pvn.Trigger.OnKeyDown` and `OnKeyPress`.

```python
with pvn.Trigger.OnKeyDown(KeyCode.Space):
    pvn.Print("Spacebar pressed!")
```

### `ZombieAnimation`

Provides nested enums containing accurate animation clip string names for every specific zombie model. Use these with `zombie.play_animation()`.

```python
with pvn.Trigger.OnZombieSpawn() as zombie:
    with pvn.If(zombie.zombieType == ZombieType.PolevaulterZombie):
        # Play a specific animation clip safely
        zombie.play_animation(ZombieAnimation.PolevaulterZombie.ZOMBIE_POLEVAULTER_RUN)
```

---

## 3. Data Builders (`DataFactory`)

The `Types` module exposes factory classes to build structured dictionary data for `pvn.level_config`.

### `PlantEntry.create()`

Generates configuration dictionaries for pre-placing plants onto the board before the level begins.

```python
# Places a WallNut with 8000 health at row 2, col 5
entry = PlantEntry.create(row=2, col=5, plant_type=PlantType.WallNut, health=8000)
pvn.level_config.add_plant(entry)
```

### `OrderedSpawn.create()`

Generates wave-specific zombie spawn tables. Allows mixing random row assignments with fixed row assignments.

```python
# Spawns a Gargantuar on row 3 and a random Flag Zombie on wave 10
spawn_data = OrderedSpawn.create(
    wave=10, 
    zombies=[ZombieType.FlagZombie], 
    zombies_with_row=[(ZombieType.Gargantuar, 3)]
)
pvn.level_config.add_ordered_spawn(spawn_data)
```

### `GodPlant` Builder

Constructs upgrade paths and scaling stages for modular "God Mode" plants.

```python
god_pea = GodPlant(PlantType.Peashooter)
god_pea.add_route("Gatling Path")
god_pea.add_stage(plant_type=PlantType.Repeater, cost=200, attack_damage=40)
pvn.level_config.add_god_plant(god_pea)
```

---

## 4. Fusion Recipes (`RecipeData`)

Provides a query interface to programmatically traverse the Plants vs. Zombies Fusion recipe trees.

| Method | Returns | Description |
| --- | --- | --- |
| `get_fusions_from(plant)` | `List[PlantType]` | Returns all plants that can be crafted using the input plant. |
| `get_all_ingredients(plant)` | `List[PlantType]` | Recursively finds all base ingredients required to craft the input plant. |
| `get_fusion_result(p1, p2)` | `PlantType | None` | Returns the resulting plant when combining the two inputs, or None if invalid. |
| `get_direct_parents(plant)` | `List[Tuple]` | Returns pairs of plants that immediately fuse into the target plant. |

```python
# Example: Find out what Pea-Nut is made of
parents = pvn.Types.RecipeData.get_direct_parents(PlantType.PeaNut)
# Returns: [(PlantType.Peashooter, PlantType.WallNut)]
```