# 📦 Variables (`IntVar`, `FloatVar`, `BoolVar`)

Variables represent stateful runtime values that persist and update across game events. They transpile into engine variable asset definitions along with getter and setter nodes.

```python
import PvzRH_node as pvn
from PvzRH_node import BoolVar, FloatVar, IntVar
```

---

## 1. Core Rule: Assignment vs Setting

> ⚠️ **Important:** Do not reassign variables using Python's standard assignment operator (`=`). Use `.set()` or in-place operators (`+=`, `-=`, `*=`, `/=`) to record runtime mutations into the visual script graph.

```python
# ❌ Incorrect: Overwrites the Python reference and disconnects the node graph
count = IntVar(start_val=0)
count = 5

# ✅ Correct: Emits a SetVariableValue node in the execution graph
count = IntVar(start_val=0)
count.set(5)

# ✅ Correct: Uses in-place modification
count += 1
```

---

## 2. Integer Variables (`IntVar`)

Stores 32-bit signed integers for counters, wave tracking, and numeric logic.

### Initialization

```python
# Initialized with a default constant
kills = IntVar(start_val=0, name="ZombieKills")

# Initialized from a dynamic expression (auto-evaluated on level load)
offset = IntVar(start_val=pvn.Random.randint(1, 10), name="WaveOffset")

```

### Arithmetic & Modifiers

`IntVar` supports full operator overloading for both math and condition expressions:

```python
score = IntVar(start_val=100)

with pvn.Trigger.OnZombieDeath():
    score += 25       # In-place addition
    score -= 5        # In-place subtraction
    score *= 2        # In-place multiplication
    score //= 2       # In-place integer division
    score %= 10       # In-place modulo
```

### Type Conversion

* **`to_string(decimals=0)`**: Converts the integer value to a string output port for UI labels or debug logs.

---

## 3. Float Variables (`FloatVar`)

Stores floating-point numbers for speeds, timers, coordinates, and multipliers.

### Initialization

```python
multiplier = FloatVar(start_val=1.0, name="SpeedMultiplier")
timer = FloatVar(start_val=5.5, name="SpawnDelay")
```

### Arithmetic Operations

```python
rate = FloatVar(start_val=1.5)

with pvn.Trigger.OnGameStart():
    rate += 0.25      # In-place addition
    rate *= 1.1       # In-place multiplication
    rate /= 2.0       # In-place true division
```

### Type Conversion

* **`to_string(decimals=2)`**: Formats the floating-point value to a string output port with a specified decimal precision.

---

## 4. Boolean Variables (`BoolVar`)

Stores boolean flags for toggles, one-time switches, and trigger gating.

### Initialization & Setting

```python
is_boss_spawned = BoolVar(start_val=False, name="BossActive")

with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(wave_num == 10):
        is_boss_spawned.set(True)

```

### Toggling & Logical Operators

`BoolVar` supports standard bitwise syntax (`&`, `|`, `~`) and a dedicated `.toggle()` helper:

```python
hard_mode = BoolVar(start_val=False, name="HardMode")
wave_cleared = BoolVar(start_val=True, name="WaveCleared")

# Invert state (True -> False / False -> True)
with pvn.Trigger.OnKeyDown(KeyCode.H):
    hard_mode.toggle()

# Bitwise Logical Operations
with pvn.Trigger.OnWave():
    combined_flag = hard_mode & wave_cleared   # AND node
    either_flag = hard_mode | wave_cleared     # OR node
    inverted = ~hard_mode                      # NOT node
    
    with pvn.If(combined_flag):
        pvn.Board.Sun += 50

```

---

## 5. Scope Resolution

Variables created at module level are registered into the `global` scope. When a variable is accessed or modified within a nested execution scope (such as inside a `with pvn.Trigger` block), the variable dynamically references or duplicates its accessor node to match the local execution context while pointing to the exact same underlying memory asset.

```python
# Shared global asset reference
shared_counter = IntVar(start_val=0, name="SharedCounter")

with pvn.Trigger.OnPlantCreate():
    shared_counter += 1

with pvn.Trigger.OnZombieDeath():
    shared_counter += 1

```

---

## Quick Reference

| Class | Default Start Value | Primary Setter | String Formatting |
| --- | --- | --- | --- |
| `IntVar` | `0` | `.set(int)` | `.to_string(decimals=0)` |
| `FloatVar` | `0.0` | `.set(float)` | `.to_string(decimals=2)` |
| `BoolVar` | `False` | `.set(bool)`, `.toggle()` | `.to_string()` |
