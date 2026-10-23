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

## Quick Reference

| Class | Syntax | Key Properties | Description |
| :--- | :--- | :--- | :--- |
| `For` | `with For(count) as loop:` | `loop.index` | Loops `count` times synchronously |
| `While` | `with While(condition):` | — | Loops while `condition` remains `True` |
