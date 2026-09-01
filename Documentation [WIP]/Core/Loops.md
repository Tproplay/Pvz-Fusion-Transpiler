# 🔄 Loops & Iteration

Control flow structures for repeating execution logic within a single game frame.

```python
import PvzRH_node as pvn
```

---

## 1. The `For` Loop

The `pvn.For` construct transplies into a visual node loop that executes its body a specific number of times. Capture the context manager to access the current iteration index.

### Standard Iteration

```python
with pvn.Trigger.OnBoardStart():
    with pvn.For(5) as loop:
        ...
```

### Driving Logic with `.index`

The `.index` property acts as a live numeric output port tracking the 0-based iteration number. You can pass it directly into node inputs, coordinates, or math operations:

```python
with pvn.Trigger.OnGameStart():
    # Spawns a row of 9 Peashooters
    with pvn.For(9) as loop:
        pvn.Spawner.Set_Plant(row=2, col=loop.index, plant_type=pvn.PlantType.Peashooter)
```

---

## 2. The `While` Loop

The `pvn.While` construct evaluates a condition, executes the block if `True`, and recursively triggers itself until the condition becomes `False`.

> **⚠️ Engine Warning:** Visual scripting `While` loops evaluate synchronously in a single frame. If the condition cannot become `False` through the logic executed exclusively inside the loop body, the game engine will freeze in an infinite cycle.

### Standard Condition Checks

```python
with pvn.Trigger.OnKeyDown(pvn.KeyCode.Space):
    with pvn.While(pvn.Board.Sun < 1000):
        ...
```
