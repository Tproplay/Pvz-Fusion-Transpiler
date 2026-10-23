# 🔁 Lists & Collections

The transpiler provides native node-based iteration constructs and type lists, allowing you to manipulate groups of runtime entities or define dynamic card and zombie pools.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import (
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

## 1. Plant Type Lists (`PlantTypeList`)

`PlantTypeList` represents a dynamic collection of plant type enums on the node canvas. Use it to build rogue-lite card pools, random spawner bags, or category lists.

### Initialization & Mutation

```python
# Create from standard Python list
seed_pool = pft.PlantTypeList([PlantType.Peashooter, PlantType.WallNut, PlantType.SunFlower])

# Create an empty dynamic list
custom_deck = pft.PlantTypeList()

with pft.Trigger.OnGameStart():
    # Add a single type
    custom_deck += PlantType.CherryBomb
    
    # Merge another list
    custom_deck += seed_pool
    
    # Remove a specific type
    custom_deck -= PlantType.SunFlower
```

### Logic Checks & Random Retrieval

```python
with pft.Trigger.OnPlantCreate() as plant:
    # Check if placed plant is part of the deck
    with pft.If(custom_deck.contains(plant.plantType)):
        plant.add_shield(500)

with pft.Trigger.OnWave():
    # Pull a random plant type and spawn it
    random_plant = custom_deck.get_random()
    pft.Spawner.Set_Plant(row=2, col=3, plant_type=random_plant)
```

---

## 2. Zombie Type Lists (`ZombieTypeList`)

`ZombieTypeList` maintains a collection of zombie types, transpiling into optimized logical checks when queried:

```python
bosses = pft.ZombieTypeList([ZombieType.Gargantuar, ZombieType.PolevaulterZombie])
bosses += ZombieType.NewspaperZombie

with pft.Trigger.OnZombieSpawn() as zombie:
    with pft.If(bosses.contains(zombie.zombieType)):
        zombie.set_speed_multiplier(1.2)
        zombie.set_health_multiplier(2.0)
```

---

## 3. Iterating Over Entities

### Iterating All Zombies on Board (`ForEachAllZombies`)

Loop through every living zombie currently on the lawn:

```python
with pft.Trigger.OnKeyDown(pft.KeyCode.Space):
    with pft.ForEachAllZombies() as zombie:
        zombie.damage(200)
```

### Iterating Plant Entities (`ForEachPlant`)

When receiving a list of plants from board queries (e.g. `Lawnf.get_all_plants()` or `Lawnf.get_plants_at(row, col)`), use `ForEachPlant` to loop over live entities:

```python
with pft.Trigger.OnGameStart():
    all_plants = pft.Lawnf.get_all_plants()
    
    with pft.ForEachPlant(all_plants) as plant:
        with pft.If(plant.row == 2):
            plant.heal(500)
            plant.add_shield(1000)
```

### Iterating All Plants on Lawn (`Lawnf.for_each_plant_on_lawn`)

Convenience context manager directly on `Lawnf`:

```python
with pft.Trigger.OnWave():
    with pft.Lawnf.for_each_plant_on_lawn() as plant:
        plant.heal(50)
```

---

## Quick Reference

| Class | Type | Description |
| :--- | :--- | :--- |
| `PlantTypeList` | Collection | Dynamic array of `PlantType` enums |
| `ZombieTypeList` | Collection | Dynamic set of `ZombieType` enums |
| `ForEachPlant` | Context Manager | Loops over a plant list port |
| `ForEachZombie` | Context Manager | Loops over a zombie list port |
| `ForEachAllZombies`| Context Manager | Loops over all living zombies on the board |
| `ForEachPlantType` | Context Manager | Loops over items in a `PlantTypeList` |
| `ForEachZombieType`| Context Manager | Loops over items in a `ZombieTypeList` |
