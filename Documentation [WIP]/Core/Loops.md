# 🔄 Loops & Iteration

Control flow structures for repeating execution logic within a single game frame.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import For, While
from PvZ_Fusion_Transpiler.Types import PlantType, KeyCode
```

---

## 1. The `For` Loop

The `pft.For` construct transpiles into a visual `LoopNode` that executes its body a fixed number of times in a single frame. Capture the context manager to access the current iteration index.

### Standard Iteration

```python
with pft.Trigger.OnBoardStart():
    with pft.For(5) as loop:
        pft.InGameUI.display_text("Loop tick!")
```

### Driving Logic with `.index`

The `.index` property acts as a live numeric output port tracking the 0-based iteration index. Pass it directly into coordinates or math expressions:

```python
with pft.Trigger.OnGameStart():
    # Spawns a full row of 9 Peashooters on row 2 (col 0 to 8)
    with pft.For(9) as loop:
        pft.Spawner.Set_Plant(row=2, col=loop.index, plant_type=PlantType.Peashooter)
```

---

## 2. The `While` Loop

The `pft.While` construct evaluates a condition, executes the block if `True`, and loops until the condition evaluates to `False`.

> [!WARNING]
> **Single-Frame Execution Warning**: Visual script `While` loops evaluate synchronously within a single frame. If the condition cannot become `False` through operations executed exclusively inside the loop body, the engine will freeze in an infinite loop.

```python
with pft.Trigger.OnKeyDown(KeyCode.Space):
    # Drains sun until below 100
    with pft.While(pft.Board.Sun >= 100):
        pft.Board.Sun -= 100
        pft.Board.Money += 10
```


---

## 3. Entity & Collection Iteration (`Loops/for_each.py`)

In addition to numeric loops, the transpiler provides high-level iteration context managers over live entities and generic collections:

### Looping Over Plants & Zombies
```python
# Iterate through all living plants
all_plants = pft.Lawnf.get_all_plants()
with pft.ForEachPlant(all_plants) as plant:
    plant.heal(500)

# Iterate through all living zombies on the board directly
with pft.ForEachAllZombies() as zombie:
    zombie.damage(200)

# Iterate through a specific zombie collection
with pft.ForEachZombie(zombie_list) as zombie:
    zombie.set_speed(0.5)
```

### Generic `List[T]` Iteration
```python
my_list = pft.List[int]("MyScores")
with my_list.ForEach() as (item, idx):
    pft.InGameUI.display_text(pft.String.Cast(item))
```

---

## Quick Reference

| Class / Method | Syntax | Iteration Variable | Description |
| :--- | :--- | :--- | :--- |
| `For` | `with For(count) as loop:` | `loop.index` (Int) | Fixed-count synchronous loop |
| `While` | `with While(condition):` | — | Condition-based synchronous loop |
| `ForEachPlant` | `with ForEachPlant(plant_list) as plant:` | `Plant` wrapper | Loops over entities in a plant list |
| `ForEachZombie` | `with ForEachZombie(zombie_list) as zombie:` | `Zombie` wrapper | Loops over entities in a zombie list |
| `ForEachAllZombies` | `with ForEachAllZombies() as zombie:` | `Zombie` wrapper | Loops over all active zombies on the lawn |
| `ForEachPlantType` | `with ForEachPlantType(type_list) as ptype:` | `PlantType` port | Loops over plant type collection |
| `ForEachZombieType`| `with ForEachZombieType(type_list) as ztype:` | `ZombieType` port | Loops over zombie type collection |
| `List[T].ForEach` | `with my_list.ForEach() as (item, idx):` | `(T, Int)` | Iterates generic list variable elements |

