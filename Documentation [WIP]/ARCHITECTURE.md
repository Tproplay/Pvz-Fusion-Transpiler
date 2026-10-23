# System Architecture & Technical Design

This document details the internal architecture, serialization pipeline, and design conventions of the **PvZ Fusion Transpiler**.

---

## 1. Architectural Layers

The codebase is organized into three distinct layers, separating low-level game serialization mechanics from high-level gameplay scripting:

```
+-----------------------------------------------------------------------------------+
| LAYER 3: HIGH-LEVEL EXTENSIONS (_Nodes/Extentions/)                               |
|   - Ergonomic Entity Wrappers: Plant, Zombie, Bullet, WorldObject                 |
|   - Scoped Context Managers: Trigger (OnStageEnter, OnPlantCreate, OnKeyPress)   |
|   - Control Flow Blocks: If, While, Switch, ForEachZombie                         |
|   - Engine Facades: Lawnf, Game, Board, InGameUI, Tool, Spawner                   |
|   - Virtual Types: IntVar, FloatVar, BoolVar, StringVar, Int, Float, String, Bool |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 2: NODE FACTORY & AUTO-WIRING (nodes.py, Core/connection_manager.py)       |
|   - Factory functions (e.g. bind_plant, change_stage, shoot_event_bullet)        |
|   - Type enforcement (_validate_plant_type, _validate_tool_type)                  |
|   - Automatic Port Type casting & constant synthesis (to_float_port, to_port)     |
|   - Trigger Stack Auto-Wiring (_ctx.trigger_stack context tracking)               |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| LAYER 1: NATIVE IL2CPP ENGINE NODES (_Nodes/Original/)                            |
|   - Base Classes: Node, EventNodeBase, EventSuggestedNode                         |
|   - 240+ Game Node Classes mirroring Unity Assembly-CSharp IL2CPP dump            |
|   - Reflection Schema Loader: definitions.py & EventNodes_Definitions.txt         |
|   - Serialization protocol: dump_data() & dump_ref()                              |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
| CORE SYSTEM & EXPORT PIPELINE (Core/)                                             |
|   - Context Manager (_ctx) registering nodes, variables, and connections          |
|   - Graph Layout Engine (automatic square / grid coordinates)                     |
|   - JSON Level Exporter: Injects into existing level JSON or creates new level    |
+-----------------------------------------------------------------------------------+
```

---

## 2. Dynamic Reflection & IL2CPP Schema

In *Plants vs. Zombies: Fusion*, visual scripting nodes inherit either from `EventNodeBase` or `EventSuggestedNode`:
- **`EventSuggestedNode`**: Modern nodes where input and output ports are inferred from suggested metadata. They typically do **not** define `_PortName` properties in Unity.
- **`EventNodeBase`**: Older or specialized nodes. In IL2CPP, some of these define string properties for port names (e.g., `trigger_PortName = "触发"`), while others (such as `BindPlantNode` and `ChangeStageNode`) define custom string fields without port name properties.

### Schema Resolution (`definitions.py`)
Rather than hardcoding field rules per class, [`definitions.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/definitions.py) reads [`EventNodes_Definitions.txt`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/EventNodes_Definitions.txt) directly:
1. **Port Names (`port_names`)**: If and only if a node class explicitly defined `_PortName` properties in the reflection dump, they are emitted into the serialized JSON.
2. **Custom String Fields (`custom_props`)**: Class-specific fields (e.g. `bindingName = "守护目标"`, `stageName = "战斗"`, `displayText = "示例文本"`, `animationName = "idle"`) are registered with their reflection defaults and serialized into `data`.
3. **Dedicated Value Nodes**: `IntValueNode`, `FloatValueNode`, `BoolValueNode`, `StringValueNode`, `PlantTypeValueNode`, `ZombieTypeValueNode`, `ToolTypeValueNode`, `BulletTypeValueNode` emit their dedicated field payload (`value`, `plantType`, `zombieType`, `toolType`, `bulletType`).

---

## 3. The Execution Context & Auto-Wiring

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

## 4. Entity Wrapper Pattern

To enforce separation of concerns and prevent raw node output ports from leaking into user code:
- **`Plant`** ([`Extentions/Entity/plant.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/Entity/plant.py)): Wraps a plant entity reference. Exposes combat operations (`curse`, `silence`, `feed_golden_bean`, `try_super_skill`, `upgrade`), speed modifiers (`attack_speed`, `set_attack_interval`), attribute countdowns, and component inspection.
- **`Zombie`** ([`Extentions/Entity/zombie.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/Entity/zombie.py)): Wraps a zombie entity reference. Exposes damage, stat modifiers (`set_stats`), status effects (`set_status`), hypnotize, move, split destructuring, and animations (`play_animation`).
- **`Bullet`** ([`Extentions/Entity/bullet.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/Entity/bullet.py)): Wraps bullet entity manipulation (destroy, redirect, damage scale).
- **`WorldObject`** ([`Extentions/World/world_object.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/World/world_object.py)): Universal wrapper for `GameObject`. Supports `create`, `destroy`, `get_transform`, `set_transform`, casting to `Plant`/`Zombie` (`cast_to_plant`, `try_cast_to_plant`), and named entity bindings (`bind_plant`, `get_bound_plant`).

---

## 5. Level JSON Output Specification

When `export()` is called:
1. **Target Inspection**: If the destination JSON file exists, existing board settings, scary pot layouts, cards, and spawn waves are preserved; only `eventNodeGraph` and `references` are updated.
2. **RID Assignment**: Every node and variable asset is assigned a unique reference ID (`rid: 1000`, `1001`, etc.).
3. **Graph Payload**:
   - `nodes`: Serialized representations of each node, its position (`x`, `y`), and its RID.
   - `connections`: Serialized list of port connections matching Unity visual graph connection specs.
   - `variables`: Serialized list of runtime variable assets (`IntVariableAsset`, `FloatVariableAsset`, `BoolVariableAsset`, `StringVariableAsset`, `ListVariableAsset`).
