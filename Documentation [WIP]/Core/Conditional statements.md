# 🔀 Conditional Statements

Conditional constructs allow you to branch execution flow based on runtime variable states, entity types, or mathematical conditions.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import If, Switch
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType
```

---

## 1. The `If / Elif / Else` Construct

The `pft.If` construct transpiles Python condition checks into visual `BranchNode` elements.

### Basic If Statement

```python
with pft.Trigger.OnZombieSpawn() as zombie:
    with pft.If(zombie.zombieType == ZombieType.Gargantuar):
        zombie.set_speed_multiplier(1.2)
```

### Full If-Elif-Else Chain

To chain alternative branches, capture the context instance as a variable:

```python
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 1) as branch:
        pft.InGameUI.display_text("Wave 1!")
    
    with branch.Elif(wave_num == 5) as branch:
        pft.InGameUI.display_text("Halfway through!")
        
    with branch.Else:
        pft.InGameUI.display_text("Standard wave.")
```

---

## 2. The `Switch / Case` Construct

The `pft.Switch` construct simplifies multi-target value checks by transpiling them into a sequential cascade of conditions.

### Matching Single Values

```python
with pft.Trigger.OnPlantCreate() as plant:
    with pft.Switch(plant.plantType) as sw:
        with sw.case(PlantType.SunFlower):
            pft.Board.Sun += 50
            
        with sw.case(PlantType.WallNut):
            plant.add_shield(500)
            
        with sw.default:
            pft.InGameUI.display_text("Other plant placed")
```

### Matching Multiple Values (OR Logic)

Pass multiple values or a list into `.case()` to trigger the same logic for any matching input:

```python
with pft.Trigger.OnPlantCreate() as plant:
    with pft.Switch(plant.plantType) as sw:
        with sw.case(PlantType.Peashooter, PlantType.Repeater, PlantType.GatlingPea):
            plant.modify_attack(1.2)
            
        with sw.case([PlantType.CherryBomb, PlantType.Jalapeno, PlantType.DoomShroom]):
            pft.InGameUI.display_text("Explosive plant placed!")
```

---

## 3. Logical Operators for Conditions

Combine multiple conditions using Python operator overloading:

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `&` | **AND** | `with pft.If((wave_num >= 5) & (pft.Board.Sun < 200)):` |
| `\|` | **OR** | `with pft.If((plant.row == 0) \| (plant.row == 4)):` |
| `~` | **NOT** | `with pft.If(~hard_mode):` |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparisons | `with pft.If(pft.Board.Sun >= 500):` |
