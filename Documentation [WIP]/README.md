# PvZ Fusion Transpiler Documentation [WIP]

Welcome to the documentation suite for the **PvZ Fusion Transpiler** (`PvZ_Fusion_Transpiler`). This library provides a Python-based visual scripting compiler and Domain-Specific Language (DSL) that transpiles high-level Python scripts directly into native level event node graphs (`.json` level data) for *Plants vs. Zombies: Fusion* (PvZ Fusion).

---

## 📖 Documentation Index

### Guides & Architecture
- [**AI Agent Workflow Guide**](AI_AGENT_WORKFLOW.md) — 6 non-negotiable rules, agent prompt templates, git workflow, and developer instructions for AI agents and forks.
- [**System Architecture & Design**](ARCHITECTURE.md) — 3-layer architecture, reflection engine, trigger auto-wiring stack, and JSON serialization format.
- [**Contributing Guidelines**](CONTRIBUTING.md) — Environment setup, dependency installation, running Pyright and unit tests, and commit guidelines.
- [**WIP Roadmap & Node Status**](WIP_ROADMAP.md) — Implemented nodes, extension mappings, and nodes reserved for optimizer/compiler internals.

### Core Documentation (`Core/`)
- [**Spawning Entities**](Core/Spawning.md) — Spawning plants, zombies, and bullets (`Spawner.Set_Plant`, `Spawner.Set_Zombie`, `Spawner.Set_Bullet`), enum enforcement, and context managers.
- [**Board State & Economy**](Core/Board.md) — Sun balance, coins/money management, wave tracking, and stage transitions (`Board`, `Game`, `Game.Stage`).
- [**Event Triggers**](Core/Triggers.md) — Board lifecycle, wave triggers, mouse and keyboard input, plant and zombie event hooks (`OnStageEnter`, `OnPlantMixed`, `OnZombieClick`, etc.).
- [**Game Functions & Tools**](Core/Game%20functions.md) — Lawn props, board queries, area explosions, `InGameUI` popups, and the player `Tool` namespace (`Tool.get_held`, `ToolType`).
- [**Variables & Casting**](Core/Variables.md) — Stateful variables (`IntVar`, `FloatVar`, `BoolVar`, `StringVar`), in-place mutation, and conversion classes (`Int`, `Float`, `String`, `Bool`).
- [**Conditional Statements**](Core/Conditional%20statements.md) — Branching execution via `If`, `Elif`, `Else`, and `Switch` / `case`.
- [**Loops & Iteration**](Core/Loops.md) — Frame-level iteration using `For` and `While`.
- [**Lists & Collections**](Core/Lists.md) — Dynamic plant and zombie type lists (`PlantTypeList`, `ZombieTypeList`) and entity iteration (`ForEachPlant`, `ForEachZombie`).
- [**Multiple Choice Menus**](Core/Multiple%20choice%20menu.md) — In-game perk selection cards, dialogs, and rogue-lite upgrade choices (`MultiSelectMenu`, `Option`).
- [**Randomization**](Core/Random.md) — Random values, execution path scrambling (`TriggerChance`, `RandomTrigger`), and deterministic seeded RNG (`Random.Seeded`).
- [**Time & Delays**](Core/Time.md) — Asynchronous delays (`Time.Wait`), recurring interval loops (`Time.OnFixedUpdate`), and elapsed game timers.
- [**Configuration & Export**](Core/Config.md) — Compiler target configuration (`Config`), graph export mechanics (`export`), and preserving existing level data.

### Libraries (`Libraries/`)
- [**Types & Enums**](Libraries/Types.md) — Enums for `PlantType`, `ZombieType`, `ToolType`, `BulletType`, `KeyCode`, `SoundType`, `SceneType`, `LevelType`, `TravelBuffType`, and `ZombieAnimations`.
- [**Standard Library**](Libraries/StdLib.md) — Virtual data structures (`Dictionary`, `Array`), `format_string`, and player controls (`WASDPlant`).
- [**Math & Comparisons**](Libraries/Math.md) — Mathematical operations (`pow`, `log`), comparative helpers (`Math.greater`, `Math.less`, `Math.equal`), and GameObject equality.

---

## 🚀 Quick Start

### 1. Basic Import
```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import (
    PlantType,
    ZombieType,
    ToolType,
    BulletType,
    KeyCode,
)
```

The top-level `PvZ_Fusion_Transpiler` (`pft`) namespace exports all core gameplay extensions, triggers, variables, and engine facades. Enumerations are imported cleanly from `PvZ_Fusion_Transpiler.Types`.

### 2. Creating a Custom Level Script
```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType, KeyCode

# 1. Configure output target
pft.Config(output="./output", name="MyCustomLevel")

# 2. Add an initialization trigger
with pft.Trigger.OnGameStart():
    # Set starting resources
    pft.Board.Sun = 500
    
    # Spawn a defensive plant
    plant = pft.Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.WallNut)
    
    # Display welcome message
    pft.InGameUI.display_text("Survive the onslaught!", duration=4.0)

# 3. Add wave reactive logic
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 5):
        pft.Spawner.Set_Zombie(row=2, col=9, zombie_type=ZombieType.Gargantuar)
        pft.InGameUI.display_text("A Gargantuar approaches!", duration=3.0)

# 4. Export to JSON (also auto-exports upon script exit)
pft.export()
```

---

## 🛠️ Export Mechanics

Exporting is completely automated:
- **Compile & Save**: Run your script with Python. Upon script termination, an `atexit` hook automatically calls `pft.export()`. You can also trigger compilation manually via `pft.export()`.
- **Merge into Existing Levels**: If the target `.json` file already exists, the transpiler **preserves** existing board settings, scary pot layouts, cards, and custom wave lists while updating only the `eventNodeGraph` and `references` sections.
- **New Files**: If the destination file does not exist, a clean level JSON containing the compiled node graph and references is created.
