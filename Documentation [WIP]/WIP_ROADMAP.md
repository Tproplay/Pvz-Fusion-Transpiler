# WIP Roadmap & Node Implementation Status

This document tracks the implementation coverage of native Unity visual nodes in the **PvZ Fusion Transpiler**, mapping high-level extension interfaces to native IL2CPP engine nodes.

---

## 1. Extension Coverage Overview

**Total Base Game Native Nodes**: 240  
**High-Level Extension Coverage**: 240 / 240 (100% Native Coverage)

| Category | Native Nodes Represented | Extension API | Status |
| :--- | :--- | :--- | :--- |
| **Spawning** | `SetPlantNode`, `CreateZombieNode`, `ShootEventBulletNode` | `Spawner.Set_Plant`, `Spawner.Set_Zombie`, `Spawner.Set_Bullet` | ✅ Fully Implemented |
| **Plant Manipulation** | `CursePlantNode`, `SilencePlantNode`, `FeedGoldenBeanNode`, `UpgradePlantNode`, `TrySuperSkillNode`, etc. | `Plant` wrapper | ✅ Fully Implemented |
| **Zombie Manipulation** | `DamageZombieNode`, `SetZombieSpeedMultiplierNode`, `HypnotizeZombieNode`, `PlayZombieAnimationNode`, etc. | `Zombie` wrapper, `ZombieTypeList` | ✅ Fully Implemented |
| **Bullet Manipulation** | `DestroyBulletNode`, `RedirectBulletNode`, `ScaleBulletDamageNode` | `Bullet` wrapper | ✅ Fully Implemented |
| **Game State & Stages** | `ChangeStageNode`, `GetStageNode`, `GameOverNode`, `GameWinNode`, `PauseWaveCountdownNode`, `GetSunNode`, `GetMoneyNode`, `GetTravelEntryNode` | `Game`, `Board`, `Game.Stage`, `_SunManager`, `_MoneyManager` | ✅ Fully Implemented |
| **Player Tools** | `GetHeldToolNode`, `CompareToolTypeNode`, `GetToolCooldownNode`, `SetToolCooldownNode`, `ToolTypeValueNode` | `Tool`, `ToolCooldown`, `ToolType` | ✅ Fully Implemented |
| **Game Objects & World**| `CreateEventObjectNode`, `DestroyEventObjectNode`, `GetObjectTransformNode`, `BindPlantNode`, `BindZombieNode`, `ObjectToPlantNode`, `ObjectToZombieNode` | `WorldObject`, `GameObject`, `Vector3` | ✅ Fully Implemented |
| **Triggers** | `OnGameStartNode`, `OnBoardStartNode`, `OnWaveNode`, `OnPlantCreateNode`, `OnPlantDieNode`, `OnStageEnterNode`, `OnPlantMixedNode`, `OnZombieClickNode`, etc. | `Trigger` namespace | ✅ Fully Implemented |
| **Branching & Control Flow** | `BranchNode`, `MultiBranchNode`, `LoopNode`, `WhileNode`, `DoOnceNode`, `PulseNode` | `If`, `Switch`, `For`, `While`, `DoOnce`, `Pulse` | ✅ Fully Implemented |
| **Time & Polling** | `WaitNode`, `WaitUntilNode`, `RepeatUntilNode`, `ToggleCycleNode`, `CounterNode` | `Time.Wait`, `Time.WaitUntil`, `Time.RepeatUntil`, `Time.OnFixedUpdate` | ✅ Fully Implemented |
| **Generic Collections & Lists** | All 35 typed list manipulation nodes (`Append*`, `Get*Item`, `Insert*`, `Replace*`, `Find*`, `CopyListValues`, `ClearListValues`, `RemoveListItem`, `GetListLength`) | `List[T]`, `IntList`, `FloatList`, `BoolList`, `StringList`, `ObjectList`, `PlantTypeListVar`, `ZombieTypeList`, `ListOperation`, `ForEach` | ✅ Fully Implemented |
| **Variables & Types** | `IntVariableNode`, `FloatVariableNode`, `BoolVariableNode`, `StringVariableNode`, conversion nodes | `IntVar`, `FloatVar`, `BoolVar`, `StringVar`, `Int`, `Float`, `String`, `Bool` | ✅ Fully Implemented |
| **Math & Logic** | `PowerNode`, `LogarithmNode`, `CompareFloatNode`, `CompareIntNode`, `CompareGameObjectNode` | `Math`, `Compare` | ✅ Fully Implemented |
| **UI & Menus** | `ShowMultipleChoiceMenuNode`, `AddMultipleChoiceOptionNode`, `MergeMultipleChoiceOptionListsNode`, `TypedChoiceMenuNode`, `TypedChoiceOptionNode`, `TypedChoiceMergeNode`, `CreateInfoCardNode`, etc. | `MultiSelectMenu` (with `MenuKind.Standard` and `MenuKind.Typed`), `InfoCard`, `InGameUI` | ✅ Fully Implemented |

---

## 2. All 44 Gap Nodes Resolved

All previously unextended native nodes were implemented and verified across 7 sequential rollout phases:

1. **Generic `List[T]` & Collection Operations (33 nodes)**:
   - Dynamic lists for `int`, `float`, `bool`, `str`, `GameObject`, `PlantType`, and `ZombieType`.
   - Comprehensive operations: `Add` (`+=`), `Insert`, `Replace`, `RemoveAt`, `Clear`, `CopyTo`, `Clone`, `TryGetValue`, `TryFindIndex`, and `ForEach`.
2. **Economy Sequential Grants (2 nodes)**:
   - `Board.Sun.Add(amount)` lowers directly to `GetSunNode`.
   - `Board.Money.Add(amount)` lowers directly to `GetMoneyNode`.
3. **Tool Typing (1 node)**:
   - `Tool.Value(tool_type)` emits `ToolTypeValueNode`.
   - Implicit `to_port` coercion handles `ToolType` enum values with Chinese aliases (`ToolType.铲子`, `ToolType.锤子`, etc.).
4. **Control Flow Guards & Real-Time Polling (3 nodes)**:
   - `DoOnce` wraps `DoOnceNode`.
   - `Time.WaitUntil` and `Time.RepeatUntil` wrap `WaitUntilNode` and `RepeatUntilNode` with `.OnComplete`, `.OnTimeout`, `.OnFailed`, and `.OnEach` branches.
5. **Periodic Pulse (1 node)**:
   - `Pulse` wraps `PulseNode` with `.OnPulse` branch and context manager support.
6. **Typed Menus (3 nodes)**:
   - `MenuKind.Typed` in `MultiSelectMenu` utilizes `TypedChoiceMenuNode`, `TypedChoiceOptionNode`, and `TypedChoiceMergeNode`.
7. **Legacy Travel Entry (1 node)**:
   - `Game.GetTravelEntry()` / `Lawnf.GetTravelEntry()` wraps `GetTravelEntryNode` with explicit `DeprecationWarning`.

Detailed documentation and code samples are in [`BASE_GAME_NODES_LIST.md`](./BASE_GAME_NODES_LIST.md) and [`EXTENSIONS_IMPLEMENTATION_LIST.md`](./EXTENSIONS_IMPLEMENTATION_LIST.md).


---

## 3. Architecture Refactors & In-Editor UI Controls Alignment

### A. Spec v2 Generic `List[T]` Refactor (F1–F16)
- **Root-Port Immutability (`_root_port`)**: Implements immutable root output port references to prevent canvas divergence across branching execution contexts.
- **Single-Node Lookup & Search**: `TryGetValue(index)` returns `(Value, Valid)` ports directly from `Get*ListItemNode`. `TryFindIndex(value)` returns `(Index, Found)` ports directly from `Find*ListValueNode`.
- **Strict Whitelisting**: Parameterized strictly to supported types (`int`, `float`, `bool`, `str`, `GameObject`, `PlantType`, `ZombieType`).
- **Table Dispatch**: All collection operations dispatch via `_OPS` dictionary table, keeping each method under 10 lines.
- **Bound Class Caching**: `_BOUND_LIST_CACHE` guarantees `List[int] is List[int]`.
- **Operator Traps**: Python runtime operators `len(l)`, `x in l`, `bool(l)` raise descriptive `TypeError`s guiding users to `.Count`, `.Contains()`, etc.
- **Generic Typing Stubs**: Full IDE auto-completion provided via `list_var.pyi`.
- **Type Aliases**: Added `ZombieTypeListVar = List[ZombieType]` alongside `IntList`, `FloatList`, `BoolList`, `StringList`, `ObjectList`, and `PlantTypeListVar`.

### B. Phase 11 Structural Renames
- **Stdlib Shadowing Elimination**:
  - `typing.py` -> `port_types.py` (resolves conflicts with Python's standard `typing` module).
  - `Core/uuid.py` -> `Core/node_id.py` (resolves conflicts with Python's standard `uuid` module).
- **Spelling Normalization**:
  - `_Nodes/Extentions` -> `_Nodes/Extensions` (with backward-compatible re-export shims).
- **Consolidated Entity Loops**:
  - Loops migrated to `_Nodes/Extensions/Loops/for_each.py` (`ForEachPlant`, `ForEachZombie`, `ForEachAllZombies`, `ForEachPlantType`, `ForEachZombieType`).

### C. In-Editor UI Controls Alignment (Slot 12 `ShowEditorUI`)
- **Engine Reflection Analysis**: Audited all 34 classes in PvZ Fusion IL2CPP assembly overriding virtual method slot 12 (`ShowEditorUI`).
- **11 New Typed Enums in `_Data/` & `Types`**:
  - `MusicType`, `SceneType` (extended with 44 `ClassicTowerLawn`, 45 `ClassicTowerLawn2`, 46 `Swamp`), `EventGridObstacle`, `EventZombieStat`, `EventZombieStatus`, `EventBulletProperty`, `EventWorldEffect`, `EventTravelEntryKind`, `EventArithmeticOperation`, `Layer`, `ListStorageOperation`, `BuffType`, and aliased `EventToolType = ToolType`.
- **Field Validation & Dual-Import Safety**:
  - `validate_enum_field()` in `node.py` enforces Rule 4 strict enum typing, supports both direct `_Data` and `Types` imports, and issues `DeprecationWarning` on raw int fallback.
- **14 In-Editor Dropdown Node Classes Updated**:
  - All 14 `EventSuggestedNode` subclasses declare their field attributes with defaults and serialize cleanly into level event JSON.
- **Convenience Facades**:
  - Extended `Zombie` (properties `.hp`, `.speed`, `.size`, `.attack_power`; methods `.set_hp`, `.set_speed`, `.set_stats`, `.get_stats`, `.set_status`, `.get_status`).
  - Extended `Bullet` (`.modify`, `.set_speed`, `.set_damage`, `.set_scale`, `.set_direction`).
  - Extended `Lawnf` (`.change_map`, `.change_music`, `.delete_grid_items`, `.remove_travel_entry`).
  - Extended `Trigger.OnWorldPlantEffect(effect)`.
