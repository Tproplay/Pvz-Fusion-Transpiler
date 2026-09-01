# 📚 Standard Library (`StdLib`)

The `StdLib` library provides pre-built game mechanics, advanced data structures, and formatting utilities to streamline complex logic in your visual script graphs.

```python
import PvzRH_node as pvn
from PvzRH_node.StdLib import Dictionary, Array, StatManager
```

---

## 1. String Formatting

### `format_string(*args)`

Dynamically concatenates mixed types (text, numbers, booleans, enums, and output ports) into a single string by constructing a chain of `StringConcat` nodes.

```python
with pvn.Trigger.OnWave() as wave_num:
    msg = pvn.StdLib.format_string("Wave ", wave_num, " incoming! Sun: ", pvn.Board.Sun)
    pvn.Print(msg)
```

---

## 2. Data Structures

### Virtual `Dictionary`

Provides a string-keyed dictionary that automatically registers individual `BoolVar`, `FloatVar`, or `IntVar` nodes on the graph. You can read and write to it dynamically using standard Python property dot-notation or brackets.

```python
# Initialize schema
player = pvn.StdLib.Dictionary({
    "level": 1,
    "speed": 1.0,
    "has_shield": False
})

# Mutate state across events
with pvn.Trigger.OnZombieDeath():
    player.level += 1
    
with pvn.Trigger.OnKeyDown(KeyCode.S):
    player.has_shield.toggle()
```

### Virtual `Array`

Allocates a contiguous block of identically typed variables. Arrays allow you to read and write variables dynamically using an index port instead of static references.

```python
# Create an array of 5 integers (default 0)
lane_health = pvn.StdLib.Array(size=5, default_val=0)

with pvn.Trigger.OnZombieSpawn() as zombie:
    # Dynamically write 100 to the index matching the zombie's row
    lane_health.write(index_port=zombie.row, value=100)
```

---

## 3. Lists & Collections

### `ZombieTypeList`

A static counterpart to `PlantTypeList`. Because the engine lacks native zombie list storage nodes, `ZombieTypeList` maintains a Python set during transpilation and converts it into a chain of logical `OR` (`|`) gates when queried at runtime.

```python
bosses = pvn.StdLib.ZombieTypeList([pvn.ZombieType.Gargantuar, pvn.ZombieType.BungeeZombie])
bosses += pvn.ZombieType.Zomboni

with pvn.Trigger.OnZombieSpawn() as zombie:
    with pvn.If(bosses.contains(zombie.zombieType)):
        zombie.set_health_multiplier(2.0)
```

---

## 4. Game Mechanics

### `Counter`

Wraps the engine's internal `CounterNode`. Useful for tracking objectives (like "Kill 5 Zombies") and firing an execution track exactly once the threshold is met.

```python
kills_needed = pvn.StdLib.Counter(start_val=0)

with pvn.Trigger.OnZombieDeath():
    kills_needed.up()
    
# Triggers when 'up()' executes enough times to hit the counter's internal limit
with kills_needed.on_count:
    pvn.Board.Sun += 500
```

### `WASDPlant`

Automatically sets up keyboard listeners mapping the `W`, `A`, `S`, `D` keys to grid-based relative movement for a specific `Plant` entity.

```python
with pvn.Trigger.OnGameStart():
    hero = pvn.Spawner.Set_Plant(row=2, col=2, plant_type=pvn.PlantType.Peashooter)
    pvn.StdLib.WASDPlant(hero).Start()
```

---

## 5. `StatManager` (RPG System)

The `StatManager` simplifies complex buff tracking. It resolves global modifiers, category tags, and individual stat bonuses into a single unified ATK or HP calculation for entities at runtime.

### 1. Registration

Configure your base stats and register your categories (tags).

```python
stats = pvn.StdLib.StatManager(base_plant_stat=1.0, base_zombie_hp_mult=1.0)

# Create a tag grouping explosive plants
stats.create_tag("Explosives", [pvn.PlantType.CherryBomb, pvn.PlantType.DoomShroom])
```

### 2. Modification

Apply buffs to globals, tags, or individual units.

```python
# Give all explosives +50% ATK
stats.add_tag_atk("Explosives", 0.5)

# Give Peashooters specifically +10% ATK
stats.add_plant_atk(pvn.PlantType.Peashooter, 0.1)

# Give every plant on the board +5% HP
stats.global_hp += 0.05
```

### 3. Application

Call the compiler hooks during spawn events to apply the calculated totals to the entities.

```python
with pvn.Trigger.OnPlantCreate() as plant:
    # Automatically resolves and applies all relevant ATK and HP buffs
    stats.apply_stats_to_plant(plant)

with pvn.Trigger.OnZombieSpawn() as zombie:
    # Automatically applies HP scaling multipliers
    stats.apply_stats_to_zombie(zombie)
```
