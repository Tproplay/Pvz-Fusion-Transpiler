# 🧮 Math & Comparisons (`Math`, `Compare`)

The `pft.Math` (aliased as `pft.Compare`) interface provides native node wrappers for exponential calculations, logarithms, type-aware numeric comparisons, and GameObject reference equality.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import Math, Compare
```

---

## 1. Advanced Math Operations

### Power (`Math.pow` / `Math.power`)
Calculates a base value raised to an exponent, emitting a `PowerNode`:

```python
with pft.Trigger.OnWave() as wave_num:
    # Scales zombie damage exponentially: 20 * (1.1 ^ wave)
    scale_factor = pft.Math.pow(1.1, wave_num)
```

### Logarithm (`Math.log` / `Math.logarithm`)
Calculates the logarithm of a value with a specified base (default $e \approx 2.71828$), emitting a `LogarithmNode`:

```python
log_val = pft.Math.log(value=input_val, base=10.0)
```

---

## 2. Comparison Functions

While Python comparison operators (`<`, `>`, `==`, `!=`, `<=`, `>=`) work directly on `IntVar`, `FloatVar`, and entity properties, `Math` provides explicit comparison functions that auto-select between `CompareIntNode` and `CompareFloatNode`:

### Greater Than (`Math.greater`)
Returns a boolean port indicating whether $a > b$:
```python
is_high_wave = pft.Math.greater(wave_num, 10)
```

### Less Than (`Math.less`)
Returns a boolean port indicating whether $a < b$:
```python
is_low_sun = pft.Math.less(pft.Board.Sun, 100)
```

### Equal (`Math.equal`)
Returns a boolean port indicating whether $a == b$:
```python
is_exact = pft.Math.equal(wave_num, 5)
```

---

## 3. Object Reference Equality (`Math.same_object`)

Checks if two `WorldObject` or `GameObject` ports refer to the exact same runtime object in Unity:

```python
with pft.Trigger.OnPlantClick() as clicked_plant:
    target_plant = pft.WorldObject.get_bound_plant(name="守护目标")
    
    # Check if clicked plant is the guarded plant
    is_same = pft.Math.same_object(clicked_plant.ref, target_plant.ref)
    with pft.If(is_same):
        pft.InGameUI.display_text("Guarded plant clicked!")
```

---

## Quick Reference

| Method | Emitted Node | Description |
| :--- | :--- | :--- |
| `Math.pow(val, exp)` | `PowerNode` | Returns `val` raised to `exp` |
| `Math.log(val, base=e)`| `LogarithmNode` | Returns logarithm of `val` with base `base` |
| `Math.greater(a, b)` | `CompareIntNode` / `CompareFloatNode` | Returns bool port for $a > b$ |
| `Math.less(a, b)` | `CompareIntNode` / `CompareFloatNode` | Returns bool port for $a < b$ |
| `Math.equal(a, b)` | `CompareIntNode` / `CompareFloatNode` | Returns bool port for $a == b$ |
| `Math.same_object(a, b)`| `CompareGameObjectNode` | Returns bool port for GameObject equality |
