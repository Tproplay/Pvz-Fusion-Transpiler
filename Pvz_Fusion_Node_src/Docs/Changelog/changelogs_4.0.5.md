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

## 3. Libraries Upgrades (`Libraries`)

### 3.1 Math Library (`Libraries.Math`)
- **Native Power Calculations**: `pow(base, exp)` and `natural_pow(base, exp)` upgraded to use native `PowerNode`.
- **Operator Overloads**: Added `Port.__pow__` and `Port.__rpow__` supporting Python `base ** exp` syntax directly into `PowerNode`.
- **Native Roots**: `sqrt(val)` and `cbrt(val)` upgraded to use native `PowerNode(val, 0.5)` and `PowerNode(val, 1/3)`.
- **Native Logarithms**: Added `log(val, base)` wrapping native `LogarithmNode`.
- **Native Modulo**: Added `mod(a, b)` wrapping native `IntModuloNode`.

### 3.2 Standard Library (`Libraries.StdLib`)
- **20 Type Conversion Functions**:
  - ASCII: `ascii_to_string()`, `string_to_ascii()`.
  - Numeric & Boolean: `int_to_float()`, `float_to_int()`, `int_to_string()`, `string_to_int()`, `float_to_string()`, `string_to_float()`, `int_to_bool()`, `float_to_bool()`.
  - Object Conversions: `object_to_string()`, `string_to_object()`, `object_to_plant()`, `plant_to_object()`, `object_to_zombie()`, `zombie_to_object()`.
  - Entity Enums: `plant_type_to_string()`, `string_to_plant_type()`, `zombie_type_to_string()`, `string_to_zombie_type()`.
- **Tools & Events**:
  - `compare_tool_type(a, b)`: Wraps `CompareToolTypeNode` with automatic type wiring.
  - `get_event_position()`: Wraps `GetEventPositionNode` returning the 3D position of the triggering event.

---

## 4. Node Status Comment Synchronization
- All 110+ Original Node definitions in `Nodes/Original/` previously tagged with:
  `# Status in Extensions: Not implemented / New`
  have been updated to:
  `# Status in Extensions: Implemented`
- Total unimplemented nodes remaining: **0**.
