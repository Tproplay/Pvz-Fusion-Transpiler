# System Architecture & Technical Design

This document details the internal architecture, serialization pipeline, and design conventions of the **PvZ Fusion Transpiler**.

---

## 1. Architectural Layers

The codebase is organized into three distinct layers, separating low-level game serialization mechanics from high-level gameplay scripting:

```
+-----------------------------------------------------------------------------------+
| LAYER 3: HIGH-LEVEL EXTENSIONS (_Nodes/Extensions/)                               |
|   - Ergonomic Entity Wrappers: Plant, Zombie, Bullet, WorldObject                 |
|   - Scoped Context Managers: Trigger (OnStageEnter, OnPlantCreate, OnKeyPress)   |
|   - Control Flow Blocks: If, While, Switch, ForEachZombie, ForEachPlant           |
|   - Engine Facades: Lawnf, Game, Board, InGameUI, Tool, Spawner                   |
|   - Collections: Generic List[T], IntList, ZombieTypeListVar                      |
|   - Virtual Types: IntVar, FloatVar, BoolVar, StringVar, Int, Float, String, Bool |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 2: NODE FACTORY & AUTO-WIRING (nodes.py, Core/connection_manager.py)       |
|   - Factory functions (e.g. bind_plant, change_event_map, shoot_event_bullet)    |
|   - Type enforcement (_validate_plant_type, _validate_tool_type, etc.)            |
|   - Automatic Port Type casting & constant synthesis (to_float_port, to_port)     |
|   - Trigger Stack Auto-Wiring (_ctx.trigger_stack context tracking)               |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 1: NATIVE IL2CPP ENGINE NODES (_Nodes/Original/)                            |
|   - Base Classes: Node, EventNodeBase, EventSuggestedNode                         |
|   - 240 Native Game Node Classes mirroring Unity Assembly-CSharp IL2CPP dump      |
|   - In-Editor UI Controls & Node Fields (ShowEditorUI slot 12 reflection)         |
|   - Reflection Schema Loader: definitions.py & EventNodes_Definitions.txt         |
|   - Serialization protocol: dump_data() & dump_ref()                              |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CORE SYSTEM & EXPORT PIPELINE (Core/)                                             |
|   - Context Manager (_ctx) registering nodes, variables, and connections          |
|   - Graph Layout Engine (automatic square / grid coordinates)                     |
|   - Node ID Generator (Core/node_id.py)                                           |
|   - JSON Level Exporter: Injects into existing level JSON or creates new level    |
+-----------------------------------------------------------------------------------+
```

---

## 2. In-Editor UI Controls & Field Serialization

In PvZ Fusion's Level Event Editor, nodes interact with editor GUI controls through `RuntimeNodeUI.CreateValueEditUI(EventNodeBase node)`, which dispatches virtual method slot 12:
```csharp
public virtual int ShowEditorUI(RuntimeNodeUI ui);
```
Across the entire game assembly (`dump.cs`), **exactly 34 classes** override `ShowEditorUI`:
- **14 classes** inherit directly from `EventSuggestedNode` and use `NodeEditorControls.Enum<T>(ui, this.field, ...)` to render an enum dropdown.
- **20 classes** inherit directly from `EventNodeBase` and render text fields, numeric/bool input toggles, dropdowns, or almanac card pickers.

### Field Serialization in `Node.dump_data()`
Unlike input ports which represent directed data wires, in-editor UI controls bind directly to C# instance fields. When Unity saves a level graph to JSON, these fields are stored inside `eventNodeGraph.nodes[i].data`:

| Node Class Name | C# Field | Enum / Type | Serialized Key | Default Value |
| :--- | :--- | :--- | :--- | :--- |
| **`ChangeEventMusicNode`** | `MusicType music` | `MusicType` | `"music"` | `0` (`MusicType.MainMenu`) |
| **`ChangeEventMapNode`** | `SceneType scene` | `SceneType` | `"scene"` | `0` (`SceneType.Day`) |
| **`BulletTypeValueNode`** | `BulletType bulletType` | `BulletType` | `"bulletType"` | `0` (`BulletType.Bullet_pea`) |
| **`ToolTypeValueNode`** | `ToolType toolType` | `ToolType` | `"toolType"` | `0` (`ToolType.None_`) |
| **`DeleteGridItemsNode`** | `EventGridObstacle kind` | `EventGridObstacle` | `"kind"` | `0` (`EventGridObstacle.Grave`) |
| **`FloatVariableArithmeticNode`** | `EventArithmeticOperation operation`| `EventArithmeticOperation` | `"operation"` | `0` (`Add`) |
| **`IntVariableArithmeticNode`** | `EventArithmeticOperation operation`| `EventArithmeticOperation` | `"operation"` | `0` (`Add`) |
| **`GetZombieStatsNode`** | `EventZombieStat stat` | `EventZombieStat` | `"stat"` | `0` (`AttackPower`) |
| **`SetZombieStatsNode`** | `EventZombieStat stat` | `EventZombieStat` | `"stat"` | `0` (`AttackPower`) |
| **`GetZombieStatusNode`** | `EventZombieStatus status` | `EventZombieStatus` | `"status"` | `0` (`ChillSeconds`) |
| **`SetZombieStatusNode`** | `EventZombieStatus status` | `EventZombieStatus` | `"status"` | `0` (`ChillSeconds`) |
| **`ModifyEventBulletNode`** | `EventBulletProperty property` | `EventBulletProperty` | `"property"` | `0` (`ScaleMultiplier`) |
| **`OnWorldPlantEffectNode`** | `EventWorldEffect effect` | `EventWorldEffect` | `"effect"` | `0` (`IceShroom`) |
| **`RemoveTravelEntryNode`** | `EventTravelEntryKind kind` | `EventTravelEntryKind` | `"kind"` | `0` (`CommonModifier`) |
| **`GetPlantsOnLayerNode`** | `Layer layer` | `Layer` | `"layer"` | `0` (`Default`) |
| **`PlantTypeListStorageNode`**| `ListStorageOperation operation`| `ListStorageOperation` | `"operation"` | `1` (`Add`) |
| **`GetTravelEntryNode`** | `BuffType buffType` + `int entryIndex` | `BuffType` + `int` | `"buffType"`, `"entryIndex"` | `0`, `0` |

### Enum Validation (`validate_enum_field`)
All enum fields are validated through `validate_enum_field()` in [`node.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/node.py):
- Validates the input against the required enum class.
- Guards against Python dual-import mismatches (`type(val).__name__ == enum_cls.__name__`).
- Raises `TypeError` on mismatched enum types (e.g. passing `ZombieType` where `MusicType` is expected).
- Emits a `DeprecationWarning` when raw integers are passed per Rule 4, casting to the enum member.

---

## 3. Dynamic Reflection & IL2CPP Schema

In *Plants vs. Zombies: Fusion*, visual scripting nodes inherit either from `EventNodeBase` or `EventSuggestedNode`:
- **`EventSuggestedNode`**: Modern nodes where input and output ports are inferred from suggested metadata. They typically do **not** define `_PortName` properties in Unity.
- **`EventNodeBase`**: Specialized nodes. In IL2CPP, some of these define string properties for port names (e.g., `trigger_PortName = "触发"`), while others define custom string fields without port name properties.

### Schema Resolution (`definitions.py`)
Rather than hardcoding field rules per class, [`definitions.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/definitions.py) reads [`EventNodes_Definitions.txt`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/EventNodes_Definitions.txt) directly:
1. **Port Names (`port_names`)**: If and only if a node class explicitly defined `_PortName` properties in the reflection dump, they are emitted into the serialized JSON.
2. **Custom String Fields (`custom_props`)**: Class-specific fields (e.g. `bindingName = "守护目标"`, `stageName = "战斗"`, `displayText = "示例文本"`, `animationName = "idle"`) are registered with their reflection defaults and serialized into `data`.
3. **Dedicated Value Nodes**: `IntValueNode`, `FloatValueNode`, `BoolValueNode`, `StringValueNode`, `PlantTypeValueNode`, `ZombieTypeValueNode`, `ToolTypeValueNode`, `BulletTypeValueNode` emit their dedicated field payload (`value`, `plantType`, `zombieType`, `toolType`, `bulletType`).

---

## 4. The Execution Context & Auto-Wiring

### Context Manager (`_ctx`)
The singleton [`_ctx`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/Core/context.py) maintains:
- `_ctx.nodes`: List of all instantiated `Node` objects.
- `_ctx.variables`: List of all `VariableAsset` instances.
- `_ctx.connections`: List of directed port connections.
- `_ctx.trigger_stack`: Stack of active execution paths for automatic trigger sequencing.

### Trigger Auto-Wiring
When instantiating a node with an input trigger named `"触发"` while inside an active execution context:
```python
with Trigger.OnPlantCreate() as plant:
    # Trigger.OnPlantCreate pushes its output trigger onto _ctx.trigger_stack
    plant.curse(10.0)       # CursePlantNode has input '触发', auto-connects to OnPlantCreate
    plant.silence(5.0)     # SilencePlantNode has input '触发', auto-connects to CursePlantNode's output
```
This eliminates the need for manual sequential wiring of trigger lines, producing clean and maintainable Python code.

---

## 5. Entity Wrapper Pattern

To enforce separation of concerns and prevent raw node output ports from leaking into user code:
- **`Plant`** ([`Extensions/Entity/plant.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/Entity/plant.py)): Wraps a plant entity reference. Exposes combat operations (`curse`, `silence`, `feed_golden_bean`, `try_super_skill`, `upgrade`), speed modifiers (`attack_speed`, `set_attack_interval`), attribute countdowns, and component inspection.
- **`Zombie`** ([`Extensions/Entity/zombie.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/Entity/zombie.py)): Wraps a zombie entity reference. Exposes combat actions, stat queries/setters (`hp`, `max_hp`, `speed`, `size`, `attack_power`, `armor1_hp`, `armor2_hp`, `get_stats`, `set_stats`), status effects (`get_status`, `set_status`), hypnotize, move, split destructuring, and animations (`play_animation`).
- **`Bullet`** ([`Extensions/Entity/bullet.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/Entity/bullet.py)): Wraps bullet entity manipulation (destroy, redirect, damage scale, speed scale, direction angle).
- **`WorldObject`** ([`Extensions/World/world_object.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/World/world_object.py)): Universal wrapper for `GameObject`. Supports `create`, `destroy`, `get_transform`, `set_transform`, casting to `Plant`/`Zombie` (`cast_to_plant`, `try_cast_to_plant`), and named entity bindings (`bind_plant`, `get_bound_plant`).

---

## 6. Generic Collections & Immutable Root-Port Architecture (`List[T]`)

The collection system in [`list_var.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/Variables/list_var.py) uses an immutable root-port pattern:
- **Root Port Immutability (`_root_port`)**: Every mutating operation (`Add`, `Insert`, `Replace`, `Clear`, `RemoveAt`) wires its list input to the original `ListVariableNode.port_output_listvariable_Variable`. The Python container never rebinds its reference, ensuring that calling methods inside conditional branches (`with If(cond): items.Add(...)`) does not cause graph divergence or leak un-executed port references outside the branch.
- **Single-Node `TryGetValue`**: Emits a single `Get*ListItemNode` and projects both `(Value, Valid)` output ports directly without redundant node allocations.
- **Generic Subscripting & Class Caching**: `List[Int]` caches bound classes via `_BOUND_LIST_CACHE`, ensuring `List[Int] is List[Int]`. Supported types are strictly whitelisted (`Int`, `Float`, `Bool`, `String`, `Plant`, `PlantType`, `Zombie`, `ZombieType`).
- **Table Dispatch**: All operations use an `_OPS` lookup dictionary instead of `if/elif` ladders, keeping all methods short (< 10 lines) per Rule 3.

---

## 7. Level JSON Output Specification

When `export()` is called:
1. **Target Inspection**: If the destination JSON file exists, existing board settings, scary pot layouts, cards, and spawn waves are preserved; only `eventNodeGraph` and `references` are updated.
2. **RID Assignment**: Every node and variable asset is assigned a unique reference ID (`rid: 1000`, `1001`, etc.).
3. **Graph Payload**:
   - `nodes`: Serialized representations of each node, its position (`x`, `y`), its RID, and its fields dictionary.
   - `connections`: Serialized list of port connections matching Unity visual graph connection specs.
   - `variables`: Serialized list of runtime variable assets (`IntVariableAsset`, `FloatVariableAsset`, `BoolVariableAsset`, `StringVariableAsset`, `ListVariableAsset`).
