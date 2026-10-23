# 📦 Variables & Type Casting

Variables represent stateful runtime values that persist across events. They transpile into engine variable asset definitions (`IntVariableAsset`, `FloatVariableAsset`, `BoolVariableAsset`, `StringVariableAsset`) along with getters, setters, and arithmetic nodes.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import (
    IntVar,
    FloatVar,
    BoolVar,
    StringVar,
    Int,
    Float,
    String,
    Bool,
)
from PvZ_Fusion_Transpiler.Types import KeyCode
```

---

## 1. Core Rule: Assignment (`=`) vs Mutation (`.set()`)

> [!CAUTION]
> **Do not reassign variables using Python's standard `=` operator.** Reassigning (`x = 5`) replaces the Python object and detaches it from the visual node graph. Use `.set()` or in-place operators (`+=`, `-=`, `*=`, `/=`) to record mutations into the compiled graph.

```python
# ❌ Incorrect: Disconnects the node graph
count = IntVar(start_val=0)
count = 5

# ✅ Correct: Emits a SetVariableValue node
count = IntVar(start_val=0)
count.set(5)

# ✅ Correct: Emits an in-place operator node
count += 1
```

---

## 2. Integer Variables (`IntVar`)

Stores signed integers for counters, wave indices, and score tracking.

```python
score = IntVar(start_val=100, name="PlayerScore")

with pft.Trigger.OnZombieDeath():
    score += 25                  # In-place addition
    score -= 5                   # In-place subtraction
    score *= 2                   # In-place multiplication
    score.add_in_place(10)       # Direct arithmetic node helper
```

### Type Conversion
- `score.to_string(decimals=0)`: Formats the integer value to a string output port.

---

## 3. Float Variables (`FloatVar`)

Stores floating-point values for speeds, delays, coordinates, and scaling factors.

```python
speed = FloatVar(start_val=1.0, name="MoveSpeed")

with pft.Trigger.OnGameStart():
    speed += 0.2
    speed *= 1.5
    speed /= 2.0
```

### Type Conversion
- `speed.to_string(decimals=2)`: Formats the float to a string output port with specified decimal precision.

---

## 4. Boolean Variables (`BoolVar`)

Stores boolean flags for switches, one-time conditions, and toggles.

```python
boss_active = BoolVar(start_val=False, name="BossActive")

# Set boolean value
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 10):
        boss_active.set(True)

# Toggle state (True <-> False)
with pft.Trigger.OnKeyDown(KeyCode.B):
    boss_active.toggle()

# Bitwise Logical Operations
flag_a = BoolVar(start_val=True)
flag_b = BoolVar(start_val=False)

combined = flag_a & flag_b   # AND
either = flag_a | flag_b     # OR
inverted = ~flag_a           # NOT
```

---

## 5. String Variables (`StringVar`)

Stores text values for banners, custom stage names, player names, and UI labels.

```python
status_msg = StringVar(start_val="Normal Mode", name="Status")

# Update string value
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 5):
        status_msg.set("Danger: Wave 5!")

# Append text in-place
with pft.Trigger.OnZombieDeath():
    status_msg += " (Defeated)"

# Print dynamically
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text(status_msg)
```

---

## 6. Type Conversion & Constructor Classes

Use `Int`, `Float`, `String`, and `Bool` to construct value nodes or statically cast ports between different engine types:

### `Int`
```python
# Construct a constant Int value node
val_node = Int(5)

# Cast float or string to int port
int_port = Int.Cast(float_val)

# Extract ASCII code from character at index
ascii_code = Int.from_ascii("Hello", index=0)  # Returns 72 ('H')
```

### `Float`
```python
# Construct a constant Float value node
float_node = Float(3.14)

# Cast int or string to float port
float_port = Float.Cast(int_val)
```

### `String`
```python
# Construct a constant String value node
str_node = String("Welcome!")

# Cast any numeric, entity, or enum port to String
text_port = String.Cast(entity_or_num_port, decimals=2)

# ASCII conversions
char_str = String.from_ascii(ascii_code)        # Int ASCII code -> String char
code = String.to_ascii("World", index=0)         # String char -> Int ASCII code

# Parse string to enum / object ports
plant_type_port = String.to_plant_type("Peashooter")
zombie_type_port = String.to_zombie_type("NormalZombie")
game_object_port = String.to_object("EventObject")
```

### `Bool`
```python
# Construct a constant Bool value node
bool_node = Bool(True)

# Cast numeric int/float port to Bool port
bool_port = Bool.Cast(num_port)
```

---

## Quick Reference

| Class | Default Start | Primary Setter | Operations |
| :--- | :--- | :--- | :--- |
| `IntVar` | `0` | `.set(int)` | `+=`, `-=`, `*=`, `//=`, `%=`, `.add_in_place()` |
| `FloatVar` | `0.0` | `.set(float)` | `+=`, `-=`, `*=`, `/=` |
| `BoolVar` | `False` | `.set(bool)`, `.toggle()` | `&`, `\|`, `~` |
| `StringVar` | `""` | `.set(str)` | `+=`, `+`, `.to_string()` |
| `Int` | — | `Int(val)` constructor | `Int.Cast(val)`, `Int.from_ascii(text, idx)` |
| `Float` | — | `Float(val)` constructor | `Float.Cast(val)` |
| `String` | — | `String(val)` constructor | `String.Cast(val)`, `String.from_ascii()`, `String.to_ascii()`, `String.to_plant_type()`, etc. |
| `Bool` | — | `Bool(val)` constructor | `Bool.Cast(val)` |
