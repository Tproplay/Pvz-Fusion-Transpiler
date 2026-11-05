# 🔁 Lists & Collections

The transpiler provides both native node-based collections (`List[T]`) and iteration constructs (`ForEach`), allowing you to manipulate groups of runtime entities, manage stateful lists, or define dynamic card and zombie pools.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import (
    List,
    IntList,
    FloatList,
    BoolList,
    StringList,
    PlantListVar,
    PlantTypeListVar,
    ZombieListVar,
    ZombieTypeListVar,
    PlantTypeList,
    ZombieTypeList,
    ForEachPlant,
    ForEachZombie,
    ForEachAllZombies,
    ForEachPlantType,
    ForEachZombieType,
)
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType
```

---

## 1. Generic State Variable Lists (`List[T]`)

`List[T]` creates a stateful `ListVariableAsset` in the compiled graph that persists throughout the level. It supports type subscripting and class caching:
`List[Int] is List[Int]` evaluates to `True`.

### Supported Element Types
- `List[Int]` (alias: `IntList`)
- `List[Float]` (alias: `FloatList`)
- `List[Bool]` (alias: `BoolList`)
- `List[String]` (alias: `StringList`)
- `List[Plant]` (alias: `PlantListVar`)
- `List[PlantType]` (alias: `PlantTypeListVar`)
- `List[Zombie]` (alias: `ZombieListVar`)
- `List[ZombieType]` (alias: `ZombieTypeListVar`)

### Declaration & Initialization
```python
# Create an integer list with initial values
scores = pft.IntList([10, 20, 30], name="Scores")

# Create a typed generic list of PlantType
deck = pft.List[pft.PlantType]([PlantType.Peashooter, PlantType.WallNut])

# Create a zombie list
waves = pft.ZombieTypeListVar([ZombieType.NormalZombie, ZombieType.ConeZombie])
```

> [!NOTE]
> Lists must be initialized with a sequence (`list` or `tuple`). Passing an unordered `set` raises a `TypeError` per Rule 8.

---

## 2. List Operations (C#-Style PascalCase & Aliases)

Per Rule 7, all list methods expose standard C#-style PascalCase methods alongside legacy `snake_case` aliases:

```python
with pft.Trigger.OnGameStart():
    # 1. Add / Append
    scores.Add(100)
    scores.append(200)

    # 2. Count / Size
    total_elements = scores.Count  # Returns PortType.Int

    # 3. Contains / Check membership
    with pft.If(scores.Contains(100)):
        pft.InGameUI.display_text("100 is in scores!", duration=3.0)

    # 4. TryGetValue (Emits a single node projecting (Value, Valid))
    val_port, is_valid = scores.TryGetValue(0)
    with pft.If(is_valid):
        pft.InGameUI.display_text("First element retrieved!", duration=2.0)

    # 5. Insert at index
    scores.Insert(0, 50)

    # 6. Replace item at index
    scores.Replace(1, 75)

    # 7. Remove item at index
    scores.RemoveAt(0)

    # 8. Clear entire list
    scores.Clear()
```

### Python Operator Traps (Rule 8)
Python built-ins cannot resolve visual node graph values at transpile time. To prevent silent bugs, standard operator traps are enforced:
- `len(items)` ➔ Raises `TypeError: len() cannot resolve graph size at transpile time. Use items.Count instead.`
- `item in items` ➔ Raises `TypeError: The 'in' operator cannot evaluate at transpile time. Use items.Contains(val) instead.`
- `bool(items)` ➔ Raises `TypeError: Cannot evaluate graph list as a boolean.`

### Branch Safety & Root-Port Immutability (Rule 9)
All mutating operations wire to the immutable `_root_port` of the underlying `ListVariableNode`. Calling `.Add()` or `.Clear()` inside a conditional branch (`with If(cond): ...`) does not rebind or diverge graph state for code outside the branch.

---

## 3. Specialized Type Lists (`PlantTypeList` & `ZombieTypeList`)

### `PlantTypeList`
`PlantTypeList` provides plant-card pool management with operator overloading:

```python
seed_pool = pft.PlantTypeList([PlantType.Peashooter, PlantType.WallNut, PlantType.SunFlower])
custom_deck = pft.PlantTypeList()

with pft.Trigger.OnGameStart():
    # Append
    custom_deck += PlantType.CherryBomb
    # Merge
    custom_deck += seed_pool
    # Remove
    custom_deck -= PlantType.SunFlower

with pft.Trigger.OnWave():
    # Retrieve a random plant type from the list
    rand_type = custom_deck.get_random()
    pft.Spawner.Set_Plant(row=2, col=3, plant_type=rand_type)
```

### `ZombieTypeList`
```python
bosses = pft.ZombieTypeList([ZombieType.NormalZombie, ZombieType.PolevaulterZombie])

with pft.Trigger.OnZombieSpawn() as zombie:
    with pft.If(bosses.contains(zombie.zombieType)):
        zombie.set_health_multiplier(2.0)
        zombie.set_speed(1.5)
```

---

## 4. Entity Loops (`ForEach`)

All entity loops are consolidated into `_Nodes/Extensions/Loops/for_each.py` and yield wrapped entity instances:

### Iterating All Living Zombies (`ForEachAllZombies`)
```python
with pft.Trigger.OnKeyDown(pft.KeyCode.Space):
    with pft.ForEachAllZombies() as zombie:
        # zombie is an Extensions.Entity.Zombie instance
        zombie.damage(200)
```

### Iterating Plants on the Lawn (`ForEachPlant`)
```python
with pft.Trigger.OnGameStart():
    all_plants = pft.Lawnf.get_all_plants()
    with pft.ForEachPlant(all_plants) as plant:
        # plant is an Extensions.Entity.Plant instance
        with pft.If(plant.row == 2):
            plant.heal(500)
            plant.add_shield(1000)
```

### Iterating Type Lists
```python
with pft.Trigger.OnGameStart():
    with pft.ForEachPlantType(custom_deck) as pt:
        # pt is an Output port of PortType.PlantType
        pass

    with pft.ForEachZombieType(bosses) as zt:
        # zt is an Output port of PortType.ZombieType
        pass
```

---

## Quick Reference

| Class / Type | Category | Description |
| :--- | :--- | :--- |
| `List[T]` | Collection | Generic state list (`List[Int]`, `List[Float]`, `List[Plant]`, etc.) |
| `IntList` | Alias | `List[Int]` |
| `FloatList` | Alias | `List[Float]` |
| `BoolList` | Alias | `List[Bool]` |
| `StringList` | Alias | `List[String]` |
| `PlantTypeList` | Collection | Specialized `PlantType` bag with `+=`, `-=`, and `.get_random()` |
| `ZombieTypeList` | Collection | Specialized `ZombieType` set with `.contains()` |
| `ForEachAllZombies`| Context Manager | Loops over all living zombies on the lawn (yields `Zombie`) |
| `ForEachPlant` | Context Manager | Loops over a plant list port (yields `Plant`) |
| `ForEachZombie` | Context Manager | Loops over a zombie list port (yields `Zombie`) |
| `ForEachPlantType` | Context Manager | Loops over items in a `PlantTypeList` |
| `ForEachZombieType`| Context Manager | Loops over items in a `ZombieTypeList` |
