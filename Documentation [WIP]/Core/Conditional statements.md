# 🔀 Conditional Statements

Conditional constructs allow you to branch execution flow based on runtime variable states, entity types, or mathematical conditions.

```python
import PvzRH_node as pvn
from PvzRH_node import If, Switch
```

## 1. The `If / Elif / Else` Construct

The `pvn.If` construct transpiles Python condition checks into visual `BranchNode` elements.

### Basic If Statement

```python
with pvn.Trigger.OnZombieSpawn() as zombie:
    with pvn.If(zombie.zombieType == ZombieType.Gargantuar):
        ...
```

### Full If-Elif-Else Chain

To chain alternative branches, capture the context instance as a variable:

```python
with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(wave_num == 1) as branch:
        ...
    
    with branch.Elif(wave_num == 2) as branch:
        ...
        
    with branch.Else:
        ...
```

---

## 2. The `Switch / Case` Construct

The `pvn.Switch` construct simplifies multi-target value checks by transpiling them into a sequential cascade of conditions.

### Matching Single Values

```python
with pvn.Trigger.OnPlantCreate() as plant:
    with pvn.Switch(plant.plantType) as sw:
        with sw.case(PlantType.SunFlower):
            ...
            
        with sw.case(PlantType.WallNut):
            ...
            
        with sw.default:
            ...
```

### Matching Multiple Values (OR Logic)

Pass multiple values or tuples into a single `.case()` to trigger the same logic for any matching input:

```python
with pvn.Trigger.OnPlantCreate() as plant:
    with pvn.Switch(plant.plantType) as sw:
        with sw.case(PlantType.Peashooter, PlantType.DoubleShooter, PlantType.GatlingPea):
            ...
            
        with sw.case([PlantType.CherryBomb, PlantType.Jalapeno, PlantType.DoomShroom]):
            ...
```

---

## Logical Operators for Conditions

You can combine multiple conditions using Python's bitwise operator overloading:

| Operator | Meaning |
| --- | --- |
| `&` | **AND** |
| `\|` | **OR** |
| `~` | **NOT** |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparisons |
