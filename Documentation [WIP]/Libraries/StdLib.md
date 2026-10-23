# 📚 Standard Library (`StdLib`)

The `StdLib` module provides pre-built gameplay abstractions, advanced virtual data structures, and formatting helpers to simplify complex logic in visual script graphs.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.StdLib import Dictionary, Array, WASDPlant, format_string
from PvZ_Fusion_Transpiler.Types import KeyCode, PlantType
```

---

## 1. String Formatting (`format_string`)

Dynamically concatenates mixed types (text, numbers, booleans, enums, and node output ports) into a single string port by chaining `StringConcat` nodes:

```python
with pft.Trigger.OnWave() as wave_num:
    msg = format_string("Wave ", wave_num, " incoming! Sun: ", pft.Board.Sun)
    pft.InGameUI.display_text(msg)
```

> **Note:** `format_string` is also available directly on the root namespace (`pft.format_string`).

---

## 2. Virtual Data Structures

### Virtual `Dictionary`

Provides a string-keyed dictionary that registers individual `BoolVar`, `FloatVar`, or `IntVar` nodes on the graph. You can read and write to it dynamically using standard Python dot-notation or brackets:

```python
# Initialize schema
player_state = Dictionary({
    "level": 1,
    "speed": 1.0,
    "has_shield": False,
})

# Mutate state across events
with pft.Trigger.OnZombieDeath():
    player_state.level += 1

with pft.Trigger.OnKeyDown(KeyCode.S):
    player_state.has_shield.toggle()
```

### Virtual `Array`

Allocates a contiguous block of identically typed variables (`int`, `float`, or `bool`). Arrays allow you to read and write variables dynamically using a runtime index port instead of static references:

```python
# Create an array of 5 integers (default 0)
lane_health = Array(size=5, default_val=0)

with pft.Trigger.OnZombieSpawn() as zombie:
    # Dynamically write 100 to the index matching the zombie's row
    lane_health.write(index_port=zombie.row, value=100)
```

---

## 3. Player Movement Mechanics (`WASDPlant`)

Automatically sets up keyboard listeners mapping the `W`, `A`, `S`, `D` keys to grid-based relative movement for a target `Plant` entity:

```python
with pft.Trigger.OnGameStart():
    hero = pft.Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.Peashooter)
    WASDPlant(hero).Start()
```

---

## Quick Reference

| Class / Function | Description |
| :--- | :--- |
| `format_string(*args)` | Concatenates text, numbers, and ports into a single string port |
| `Dictionary(schema)` | Virtual string-keyed dictionary of stateful variables |
| `Array(size, default_val)` | Pre-allocated virtual array supporting port-based index reads and writes |
| `WASDPlant(plant)` | Binds W, A, S, D keyboard listeners to control a plant's position |
