# PvZ Fusion Transpiler Documentation

Welcome to the documentation for the **PvZ Fusion Transpiler** codebase. This project provides a powerful Python-based domain-specific language (DSL) and compiler pipeline that transpiles Python scripts into native, game-ready visual node graphs (`.json` level data) for *Plants vs. Zombies: Fusion* (PvZ Fusion).

---

## Documentation Index

- [**Full Documentation Suite**](<../Documentation [WIP]/README.md>)
  Comprehensive guides for all core modules (`Spawning`, `Board`, `Triggers`, `Tools`, `Variables`, `Conditionals`, `Loops`, `Lists`, `Menus`, `Random`, `Time`, `Config`), types, and standard library.
- [**AI Agent Workflow Guide** (`AI_AGENT_WORKFLOW.md`)](AI_AGENT_WORKFLOW.md)
  *Essential reading if you or an AI agent are forking, extending, or maintaining this codebase.* Contains the 6 Core Rules, agent prompting templates, verification requirements, git branching strategy, and common traps.
- [**Architecture & System Design** (`ARCHITECTURE.md`)](ARCHITECTURE.md)
  Deep dive into the 3-layer architecture, IL2CPP reflection schema, context & trigger autowiring, and level JSON serialization format.
- [**Contributing & Forking Guide** (`CONTRIBUTING.md`)](CONTRIBUTING.md)
  Setup guide for local development, dependency management, adding tests, and pull request workflows.

---

## High-Level Overview

```
                      +-----------------------------+
                      |     User Python Script      |
                      |   (Extension Methods/DSL)   |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |   _Nodes/Extentions Layer   |
                      |  (Plant, Zombie, Trigger,   |
                      |   Spawner, Lawnf, Game...)  |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |     nodes.py Factory        |
                      |  Auto-wiring, Enum Casts,   |
                      |     Port Type Resolution    |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |   _Nodes/Original Layer     |
                      | 240+ IL2CPP Node Classes    |
                      | Schema via definitions.py   |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |    Core Serialization       |
                      | (Context, ConnectionManager,|
                      |  VariableAssets, dump_ref)  |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |  Native Level JSON File     |
                      |  ("references", "graph")    |
                      +-----------------------------+
```

### Key Capabilities
1. **Full Engine Node Coverage**: Over 240 Unity IL2CPP visual script nodes faithfully modeled in Python with exact port typings.
2. **Reflection-Driven Schema Validation**: Node data serializes with exact Unity field names (e.g. `bindingName`, `stageName`, `_PortName`), matching official game dumps 1:1.
3. **High-Level Pythonic Extensions**: Write game logic with context managers (`with Trigger.OnPlantCreated() as p:`, `with If(cond):`, `with ForEachZombie() as z:`), operator overloading (`IntVar += 5`), and wrapped entities (`Plant`, `Zombie`, `Bullet`).
4. **Strong Typing & Safety**: Type-checked via Pyright in strict environments; enums enforce valid IDs (`PlantType`, `ZombieType`, `ToolType`, `BulletType`, `KeyCode`).
5. **Headless & Embedded Compilation**: Can run standalone, via pytest/unittest suites, or integrated into a level editor or live-reload pipeline.

---

## Quick Reference

| Component | Path | Description |
| :--- | :--- | :--- |
| **Global Package Entry** | `PvZ_Fusion_Transpiler/` | Main package root with convenient exports. |
| **Core Engine** | `Core/` | Context (`_ctx`), connection graph, UUIDs, export engine. |
| **Data & Enums** | `_Data/` | Strongly-typed enums (`PlantType`, `ZombieType`, `ToolType`, etc.). |
| **Node Registry** | `nodes.py` | Factory functions constructing and connecting native nodes. |
| **Native Nodes** | `_Nodes/Original/` | Exact 1:1 classes representing game's visual scripting nodes. |
| **Extensions** | `_Nodes/Extentions/` | Ergonomic abstractions and context managers. |
| **Standard Library** | `StdLib.py` | Virtual arrays, dictionaries, and utility game behaviors. |
| **Unit Tests** | `tests/` | Comprehensive test suite ensuring graph & export validity. |
