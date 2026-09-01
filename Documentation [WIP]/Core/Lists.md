# 🔁 Lists & Loops

The transpiler provides native node-based iteration constructs, allowing you to manipulate groups of runtime entities or define dynamic pools of data via execution graphs.

```python
import PvzRH_node as pvn
from PvzRH_node import PlantType
```

---

## 1. Plant Type Lists (`PlantTypeList`)

The `PlantTypeList` acts as a dynamic array of plant enums that exist purely on the generated node canvas. You can use it to build rogue-lite card pools, random spawner bags, or category lists.

### Initialization

```python
# Create from standard Python lists
seed_pool = pvn.PlantTypeList([PlantType.Peashooter, PlantType.WallNut, PlantType.SunFlower])

# Create an empty dynamic list
custom_deck = pvn.PlantTypeList()
```

### Modifying Lists In-Place

You can add, subtract, or merge types using native Python operators (`+=`, `-=`).

```python
with pvn.Trigger.OnGameStart():
    # Add a single type
    custom_deck += PlantType.CherryBomb
    
    # Merge another list
    custom_deck += seed_pool
    
    # Remove a specific type
    custom_deck -= PlantType.SunFlower
```

### Logic Checks & Retrieval

Check if a list contains a type, or pull a random value from it:

```python
with pvn.Trigger.OnPlantCreate() as plant:
    # Check if the placed plant is part of our custom deck pool
    with pvn.If(custom_deck.contains(plant.plantType)):
        ...
        
with pvn.Trigger.OnWave():
    # Pull a random plant type from the pool and spawn it
    random_plant = custom_deck.get_random()
    pvn.Spawner.Set_Plant(row=2, col=3, plant_type=random_plant)
```

---

## 2. Iterating Plant Types (`ForEachPlantType`)

Use the `ForEachPlantType` context manager (or `.for_each()` on a `PlantTypeList`) to execute a block of logic for every item inside a type list.

```python
# Define a list of explosive plants
explosives = pvn.PlantTypeList([PlantType.CherryBomb, PlantType.DoomShroom, PlantType.Jalapeno])

with pvn.Trigger.OnBoardStart():
    with explosives.for_each() as loop:
        # Loop body executes for each plant type in the list
        ...
        
    # Execute logic after the entire loop finishes
    with loop.on_complete:
        ...
```

---

## 3. Iterating Plant Entities (`ForEachPlant`)

When querying the board for existing `Plant` instances (e.g., getting all plants in a specific row or lane), the game returns a list of plant pointers. Use `ForEachPlant` to loop over these actual live entities.

> **💡 Smart Proxy:** The `ForEachPlant` context block acts as a transparent proxy to the current `Plant` object. You can call `.die()`, `.heal()`, or check `.row` directly on the loop variable!

```python
with pvn.Trigger.OnGameStart():
    all_plants = pvn.Lawnf.get_all_plants()
    
    with pvn.ForEachPlant(all_plants) as plant:
        # Check coordinates directly on the iterator
        with pvn.If(plant.row == 2):
            # Call actions directly on the iterator
            plant.heal(500)
            plant.add_shield(1000)
            plant.modify_attack(1.5)
            
    with plant.on_complete:
        ...
```