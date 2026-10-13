# PvZ Fusion Node Transpiler - Changelog v4.0.5

## Release Highlights
- **130+ New Native Nodes Implemented**: Comprehensive integration of all newly introduced PvZ Fusion engine visual scripting nodes across Extensions, API, Math, and StdLib.
- **Architectural Modularization**:
  - `Nodes/Extentions/` modularized into structured feature subdirectories (`Bullet/`, `GameObject/`, `Logic/`, `Entity/`, `Variables/`, `UI/`, `Input/`, `Loops/`, `Time/`, `Branching/`, `Random/`).
  - `API/` separated into cohesive domain subsystems (`board.py`, `triggers.py`, `ingame_ui.py`, `lawnf.py`, `spawner.py`).
- **Complete Node Status Coverage**: All Original node files in `Nodes/Original/` updated with `# Status in Extensions: Implemented`.
- **Zero Workarounds**: Upgraded high-level libraries (`Math.py`, `StdLib.py`) to utilize native calculate, type convert, and logic nodes rather than approximation loops or unrolled node chains.

---

## 1. Extension Modules (`Nodes/Extentions`)

### 1.1 Bullet System (`Nodes/Extentions/Bullet`)
- **`Bullet` Class**:
  - `Bullet.shoot(bullet_type, position=None, x=0, y=0, z=0)`: Emits `ShootEventBulletNode` with automatic Vector3 positioning.
  - `Bullet.create_type(bullet_type)`: Emits `BulletTypeValueNode` producing typed bullet enum ports.
  - `Bullet.modify(speed=..., damage=..., penetration=...)`: Emits `ModifyEventBulletNode` to tweak active projectile properties.

### 1.2 GameObject System (`Nodes/Extentions/GameObject`)
- **`GameObject` Class**:
  - `GameObject.create(prefab_name, position=None, x=0, y=0, z=0)`: Spawns scene objects via `CreateEventObjectNode`.
  - `GameObject.destroy(game_object)`: Cleans up objects via `DestroyEventObjectNode`.
  - `GameObject.bind(game_object, target_object)`: Binds objects together via `BindObjectNode`.
  - `GameObject.get_transform(game_object)` / `set_transform(game_object, position)`: Queries and sets world transforms via `GetObjectTransformNode` and `SetEventObjectTransformNode`.
  - `GameObject.to_plant(game_object)` / `to_zombie(game_object)`: Type casting to `Plant` and `Zombie` handles via `ObjectToPlantNode` and `ObjectToZombieNode`.
- **`Vector3(x, y, z)` Helper**: Emits `MakeVector3Node` for 3D coordinates.

### 1.3 Logic Flow Controls (`Nodes/Extentions/Logic`)
- **`DoOnce`**: Context manager emitting `DoOnceNode` to guarantee single execution per condition cycle.
- **`RepeatUntil(condition)`**: Context manager emitting `RepeatUntilNode` for condition-terminated loops.
- **`WaitUntil(condition)`**: Context manager emitting `WaitUntilNode` for asynchronous engine pauses.

### 1.4 Entity Enhancements (`Nodes/Extentions/Entity`)
- **`Plant` Extensions**:
  - Status & Buffs: `.curse()`, `.silence()`, `.feed_golden_bean()`, `.super_skill()`, `.upgrade()`.
  - Combat Timers: `.set_attack_speed()`, `.get_attack_speed()`, `.set_attack_interval()`, `.set_attribute_countdown()`, `.get_attribute_countdown()`.
  - Introspection & Binding: `.get_components()`, `.bind()`, `.get_bound()`, `.to_object()`.
- **`Zombie` Extensions**:
  - Stats & Status: `.get_stats()`, `.set_stats()`, `.get_status()`, `.set_status()`.
  - Binding & Casting: `.bind()`, `.get_bound()`, `.to_object()`.
- **Iteration Context Managers**:
  - `ForEachZombie(zombie_list)`: Emits `ForEachZombieNode` to iterate specific zombie arrays.
  - `ForEachAllZombies()`: Emits `ForEachAllZombiesNode` to iterate every zombie currently on the board.

### 1.5 UI Extensions (`Nodes/Extentions/UI`)
- **`TypedChoiceOption` & `TypedChoiceMenu`**: Full support for typed dynamic branching menus, wrapping `TypedChoiceOptionNode`, `TypedChoiceMenuNode`, and `TypedChoiceMergeNode`.

### 1.6 Variable List Operations (`Nodes/Extentions/Variables`)
- **`ListVar` Enhancements**:
  - Added native node support for `insert()`, `replace()`, and `find()` across all 7 supported data types:
    - Boolean: `InsertBoolListNode`, `ReplaceBoolListNode`, `FindBoolListValueNode`.
    - Float: `InsertFloatListNode`, `ReplaceFloatListNode`, `FindFloatListValueNode`.
    - Integer: `InsertIntListNode`, `ReplaceIntListNode`, `FindIntListValueNode`.
    - GameObject: `InsertObjectListNode`, `ReplaceObjectListNode`, `FindObjectListValueNode`.
    - PlantType: `InsertPlantTypeListNode`, `ReplacePlantTypeListNode`, `FindPlantTypeListNode`.
    - String: `InsertStringListNode`, `ReplaceStringListNode`, `FindStringListValueNode`.
    - ZombieType: `InsertZombieTypeListNode`, `ReplaceZombieTypeListNode`, `FindZombieTypeListNode`.
  - Arithmetic Variable support: Integrated `FloatVariableArithmeticNode` and `IntVariableArithmeticNode`.

### 1.7 Input Extensions (`Nodes/Extentions/Input`)
- **`Mouse.world_position`**: High-level property wrapping `GetMouseWorldPositionNode`.

---

## 2. High-Level Game API (`API`)

### 2.1 Event Triggers (`API.Trigger`)
- `Trigger.OnPlantMixed`: Fires when plants are spliced/fused via `OnPlantMixedNode`.
- `Trigger.OnWaveCleared`: Fires when a wave is cleared via `OnWaveClearedNode`.
- `Trigger.OnWorldPlantEffect(effect)`: Fires on global plant activations via `OnWorldPlantEffectNode`.
- `Trigger.OnZombieClick`: Fires when clicking zombies via `OnZombieClickNode`.
- `Trigger.OnZombieHealthBelow`: Fires on zombie low-health events via `OnZombieHealthBelowNode`.
- `Trigger.WaveEvent(wave)`: Fires on target wave index via `WaveEventNode`.
- `Trigger.OnStageEnter(stage_name)`: Fires upon entering game stage via `OnStageEnterNode`.

### 2.2 Board Resources & Lifecycle (`API.Board`)
- `Board.change_stage(stage_name)`: Emits `ChangeStageNode`.
- `Board.get_stage()`: Returns current stage port via `GetStageNode`.
- `Board.change_map(scene)`: Emits `ChangeEventMapNode`.
- `Board.change_music(music)`: Emits `ChangeEventMusicNode`.
- `Board.pause_wave_countdown()`: Emits `SetWaveCountdownPausedNode`.
- `Board.set_zombie_house_rule()`: Emits `SetZombieHouseRuleNode`.
- `Board.remove_travel_entry(kind)`: Emits `RemoveTravelEntryNode`.
- `Board.Money.value` / `Board.Money.get()`: Direct access to persistent coin balance port via `GetMoneyAmountNode`.

### 2.3 Lawn Effects & Entities (`API.Lawnf`)
- `Lawnf.delete_grid_items(item_type)`: Emits `DeleteGridItemsNode`.
- `Lawnf.get_plants_on_layer(layer)`: Returns layer plant list port via `GetPlantsOnLayerNode`.
- `Lawnf.get_all_zombies()`: Returns active zombie list port via `GetAllZombiesNode`.
- `Lawnf.shoot_bullet(bullet_type, position)`: High-level helper dispatching `Bullet.shoot()`.
- `Lawnf.for_each_zombie` / `Lawnf.for_each_all_zombies`: Context managers for lawn zombie iteration.

### 2.4 User Interface (`API.InGameUI`)
- `InGameUI.delete_all_info_cards()`: Emits `DeleteInfoCardsNode`.
- `InGameUI.get_held_tool()`: Returns active tool port via `GetHeldToolNode`.
- `InGameUI.get_tool_cooldown(tool_type)` / `set_tool_cooldown(tool_type, cooldown)`: Emits `GetToolCooldownNode` and `SetToolCooldownNode`.
- `InGameUI.give_zombie_card(zombie_type)` / `remove_all_zombie_cards(zombie_type)`: Seed packets for zombies via `AddZombieCardNode` and `DeleteZombieCardsNode`.
- `InGameUI.set_zombie_card_cooldown(zombie_type, cooldown)`: Emits `SetZombieCardCooldownNode`.
- `InGameUI.show_text()`: Direct function alias for `display_text()`.

---

## 3. Modularization of Libraries (`Libraries/Math` & `Libraries/StdLib`)

### 3.1 Math Library Package (`Libraries/Math`)
The single-file `Math.py` was reorganized into a modular package with dedicated submodules:
- **`constants.py`**:
  - Constants: `PI`, `HALF_PI`, `TWO_PI`, `TAU`, `E`, `SQRT2`, `DEG2RAD`, `RAD2DEG`, `EPSILON`, `INFINITY`, `NEGATIVE_INFINITY`.
- **`powers.py`**:
  - `pow(base, exp)` and `natural_pow(base, exp)`: Native `PowerNode` calculation with automatic compile-time evaluation for constants.
  - Operator overloads: `Port.__pow__` and `Port.__rpow__` supporting `base ** exp`.
  - Roots: `sqrt(val)` and `cbrt(val)` utilizing `PowerNode(val, 0.5)` and `PowerNode(val, 1/3)`.
  - Euclidean norm: `hypot(x, y)` (`sqrt(x*x + y*y)`).
  - Logarithms & Exponents: `log(val, base=E)`, `log2(val)`, `log10(val)`, `exp(val)`.
- **`arithmetic.py`**:
  - Basic: `abs()`, `sign()`, `round()`, `floor()`, `ceil()`.
  - Clamping: `clamp(val, min_val, max_val)`, `clamp01(val)`.
  - Min/Max: `min(*args)`, `max(*args)` supporting arbitrary numeric arguments and port wires.
  - Interpolation: `lerp(a, b, t)` (clamped `[0, 1]`), `lerp_unclamped(a, b, t)`.
  - Helpers: `mod(a, b)` (native `IntModuloNode`), `copy_sign(magnitude, sign_val)`.
  - Number Theory: `is_prime(n)` (primality test), `gcd(a, b)` (greatest common divisor via Euclidean algorithm), `lcm(a, b)` (least common multiple).
- **`trigonometry.py`**:
  - Angle Conversions: `deg2rad(deg)`, `rad2deg(rad)`.
  - Angle Normalization: `normalize_angle_360(deg)` (`[0, 360)`), `normalize_angle_180(deg)` (`[-180, 180)`), `delta_angle(current, target)`.
  - Trigonometric Functions: `sin(angle)`, `cos(angle)`, `sincos(angle)` (returns `(sin, cos)` tuple), `tan(angle)`, `cosec(angle)`, `sec(angle)`, `cot(angle)`.
  - Inverse Trigonometric Functions: `asin(val)`, `acos(val)`, `atan(val)`, `atan2(y, x)`, `acosec(val)`, `asec(val)`, `acot(val)`.
- **`interpolation.py`**:
  - `inverse_lerp(a, b, val)`: Calculates normalized `t` in range `[a, b]`.
  - `remap(in_min, in_max, out_min, out_max, val)`: Maps a value between ranges.
  - `smoothstep(edge0, edge1, x)`: Hermite cubic interpolation curve (`3x^2 - 2x^3`).
  - `smootherstep(edge0, edge1, x)`: Quintic interpolation curve (`6x^5 - 15x^4 + 10x^3`).
  - `pingpong(t, length)`: Bounces `t` between 0 and `length`.
  - `repeat(t, length)`: Wraps `t` modulo `length`.
  - `move_towards(current, target, max_delta)`: Moves towards target without overshooting.
  - `move_towards_angle(current, target, max_delta)`: Moves angular degree towards target along shortest turn.
- **`noise.py`**:
  - `perlin_noise(x, y)`: Deterministic procedural pseudo-gradient noise on canvas.
  - `noise1d(x)`: 1D pseudo-random noise slice along `y=0`.
- **`geometry.py`**:
  - **`Vector2(x, y)` Class**:
    - Predefined vectors: `Vector2.zero`, `Vector2.one`, `Vector2.up`, `Vector2.down`, `Vector2.left`, `Vector2.right`.
    - Properties & Methods: `.sqr_magnitude()`, `.magnitude()`, `.normalized()`.
    - Static Methods: `Vector2.dot(v1, v2)`, `Vector2.cross(v1, v2)`, `Vector2.distance(v1, v2)`, `Vector2.lerp(v1, v2, t)`, `Vector2.reflect(in_direction, in_normal)`, `Vector2.angle(from_v, to_v)`.
    - Operator Overloads: `+`, `-`, `*`, `/`, `-v`, `==`.
    - Visual formatting: `.to_string()` formats as `(x, y)` using node canvas string concatenation.
  - Standalone functions: `distance(v1, v2)`, `dot(v1, v2)`, `cross(v1, v2)`, `reflect(in_dir, in_normal)`.

### 3.2 Standard Library Package (`Libraries/StdLib`)
The single-file `StdLib.py` was reorganized into a modular package with dedicated submodules:
- **`formatting.py`**:
  - `format_string(*args)`: Dynamic text concatenation chain on visual canvas with support for strings, numbers, ports, enums, booleans, and custom objects.
- **`collections.py`**:
  - `ZombieTypeList`: Set wrapper generating OR-chained comparison graphs for runtime zombie filtering.
  - `Dictionary`: String-keyed persistent native variable dictionary schema (`IntVar`, `FloatVar`, `BoolVar`).
  - `Array`: Pre-allocated contiguous variable array with dynamic index read/write support.
  - `Counter`: Wrapper for native `CounterNode` with `.up()` and `.on_count` completion path.
- **`controllers.py`**:
  - `_wasd_key`: Struct for default WASD KeyCode bindings.
  - `WASDPlant`: Entity movement controller binding WASD keyboard triggers to plant relative grid shifts.
- **`stat_manager.py`**:
  - `NumericVal`: Union type for numeric inputs, variables, and port references.
  - `StatManager`: RPG-style stat tracking system with global, tag/category, and individual modifiers for Plant ATK/HP and Zombie HP.
  - `PlantStatsManager`: Specialized subclass focused on plant stats.
  - `StatPreset`: Predefined modifier templates (`TANK`, `GLASS_CANNON`, `BALANCED`).
- **`type_conversions.py`**:
  - 20 native type conversion functions: `ascii_to_string()`, `string_to_ascii()`, `int_to_float()`, `float_to_int()`, `int_to_string()`, `string_to_int()`, `float_to_string()`, `string_to_float()`, `int_to_bool()`, `float_to_bool()`, `object_to_string()`, `string_to_object()`, `object_to_plant()`, `plant_to_object()`, `object_to_zombie()`, `zombie_to_object()`, `plant_type_to_string()`, `string_to_plant_type()`, `zombie_type_to_string()`, `string_to_zombie_type()`.
  - Utility functions: `compare_tool_type()`, `get_event_position()`.

---

## 4. Node Status Comment Synchronization
- All 110+ Original Node definitions in `Nodes/Original/` previously tagged with:
  `# Status in Extensions: Not implemented / New`
  have been updated to:
  `# Status in Extensions: Implemented`
- Total unimplemented nodes remaining: **0**.

---

## 5. Import Ergonomics & Top-Level Module Aliases
- **Direct Submodule Imports**:
  - `from PvZ_Fusion_Node.TypeMgr import PlantType, ZombieType, KeyCode` supported via top-level `TypeMgr.py`.
  - `from PvZ_Fusion_Node.StdLib import format_string` supported via top-level `StdLib.py`.
  - `from PvZ_Fusion_Node.Math import pow, sqrt, floor, ceil` supported via top-level `Math.py`.
  - `from PvZ_Fusion_Node import format_string, TypeMgr, StdLib, Math` supported via `__init__.py`.
- **Variable Constructor Overload Support**:
  - `IntVar`, `FloatVar`, `BoolVar`, and `StrVar` now automatically detect when a string name is passed as the first argument (e.g. `IntVar("a", 10)` or `IntVar("a")`), properly initializing variable name and default values without requiring explicit keyword arguments.

---

## 6. Board.Money Enhancements, Spawner Bullet API, and Port Constants Migration

### 6.1 `Board.Money` Setter & Full Dunder Arithmetic Suite
- **`Board.Money` Assignment & Modification**:
  - Implemented `_MoneyManager.set(target_value)` with automatic calculation of diff and emitting `add_money(diff)` or `use_money(abs_diff)` with `UseMoneyNode.OnSuccess_output_trigger`.
  - Added full operator overloads on `Board.Money` and `_MoneyManager`:
    - Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**` (`__add__`, `__radd__`, `__sub__`, `__rsub__`, `__mul__`, `__rmul__`, `__truediv__`, `__rtruediv__`, `__floordiv__`, `__rfloordiv__`, `__mod__`, `__rmod__`, `__pow__`, `__rpow__`).
    - Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=` (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`).
    - In-place assignment: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` (`__iadd__`, `__isub__`, `__imul__`, `__itruediv__`, `__ifloordiv__`, `__imod__`, `__ipow__`).
  - Updated `_BoardMeta.Money.setter` to directly route assignments (e.g. `pvn.Board.Money = 500`) to `_MoneyManager().set(value)` without error.

### 6.2 `Spawner.set_bullet` & Lawnf Bullet Migration
- **Bullet Spawning Centralization**:
  - Moved bullet spawning capability to `Spawner.set_bullet(bullet_type, position=None, x=0.0, y=0.0, z=0.0)` with camel-case alias `Spawner.Set_Bullet`.
  - Updated `Lawnf.shoot_bullet` to delegate cleanly to `Spawner.set_bullet` to preserve backward compatibility.

### 6.3 Codebase-Wide Port Name Constants Migration
- **Zero Hardcoded Port Name Strings**:
  - Migrated all hardcoded string literals (e.g. Chinese port names) across `Nodes/Extentions/`, `API/`, and `Libraries/` to class port constants:
    - **`API/board.py`**: `GetSunAmountNode.SunAmount_output_int`, `GetMoneyAmountNode.MoneyAmount_output_int`, `UseSunNode.OnSuccess_output_trigger`, `UseMoneyNode.OnSuccess_output_trigger`, `GetStageNode.StageName_output_string`.
    - **`API/spawner.py`**: `SetPlantNode.OnCreated_output_trigger`, `SetPlantNode.OnFailed_output_trigger`, `CreateZombieNode.OnCreated_output_trigger`.
    - **`API/lawnf.py`**: `GetAllZombiesNode.AllZombies_output_zombielist`, `ForEachPlantNode.LoopBody_output_trigger`.
    - **`API/ingame_ui.py`**: Port constants for `GetHeldToolNode`, `GetToolCooldownNode`, `SetToolCooldownNode`, `AddZombieCardNode`, `DeleteZombieCardsNode`, `SetZombieCardCooldownNode`, and `CreateInfoCardNode`.
    - **`API/triggers.py`**: Output trigger references mapped via `self.node.Trigger_output_trigger`.
    - **`Libraries/Math/`**: Port constants in `powers.py` (`PowerNode`, `LogarithmNode`) and `arithmetic.py` (`BranchNode`, `SetIntVariableValueNode`, `PulseNode`, `ForLoopNode`, `IntModuloNode`).
    - **`Libraries/StdLib/`**: Port constants in `collections.py` (`CounterNode`) and `type_conversions.py` (20+ type conversion nodes).
    - **`Nodes/Extentions/`**:
      - `Branching/branching.py`: `BranchNode.Trigger_input_trigger`, `BranchNode.Then_output_trigger`, `BranchNode.Else_output_trigger`.
      - `Loops/loops.py`: `BranchNode`, `ForLoopNode.LoopBody_output_trigger`, `ForLoopNode.Index_output_int`.
      - `Entity/entities.py`: `ForEachPlantNode`, `ForEachPlantTypeNode`, `ToggleNode`.
      - `Random/random_ext.py`: `RandomTriggerNode.Output_output_trigger`.
      - `Time/time_ext.py`: `ToggleCycleNode`, `CounterNode`, `WaitNode`.
      - `UI/menu.py` & `UI/ui_ext.py`: `AddMultipleChoiceOptionNode`, `ShowMultipleChoiceMenuNode`, `MergeMultipleChoiceOptionListsNode`, `CreateInfoCardNode`.
      - `Variables/variables.py`: `OnBoardStartNode`, `SetIntVariableValueNode`, `SetFloatVariableValueNode`, `SetBoolVariableValueNode`, `SetStringVariableValueNode`, `StringVariableNode`, and list node port attributes.

