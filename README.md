# PvZ Fusion Transpiler

An advanced Python-based visual scripting compiler and Domain-Specific Language (DSL) that transpiles Python logic directly into native level event node graphs for ***Plants vs. Zombies: Fusion*** (PvZ Fusion).

---

## Key Features

- **240+ Native Visual Nodes**: Faithful 1:1 representations of Unity IL2CPP visual scripting nodes.
- **Reflection-Based Schema Validation**: Automatic property and port name resolution matching official game dumps.
- **Pythonic Extensions**: High-level syntax for triggers, control flows, loops, and gameplay systems (`Plant`, `Zombie`, `Bullet`, `Tool`, `Lawnf`, `Game`, `Trigger`, `InGameUI`, `WorldObject`).
- **Context Manager Trigger Sequencing**: Automatic wiring of sequential execution triggers without manual port plumbing.
- **Robust Level JSON Exporter**: Injects compiled node graphs into existing game level JSON files while preserving board configs, scary pots, cards, and zombie wave tables.

---

## 📖 Documentation

The complete documentation suite is available in the [<ins>**Documentation [WIP]**</ins>](<Documentation [WIP]/README.md>) directory:

- [**Documentation [WIP] Index**](<Documentation [WIP]/README.md>): Complete index covering all core features, triggers, libraries, and guides.
- [**AI Agent Workflow Guide**](<Documentation [WIP]/AI_AGENT_WORKFLOW.md>): Complete instructions, core rules, system prompt templates, and best practices for developers and AI coding agents forking or maintaining this repository.
- [**Architecture & System Design**](<Documentation [WIP]/ARCHITECTURE.md>): Deep dive into the 3-layer architecture, reflection engine, context manager, and JSON level serialization.
- [**Contributing Guidelines**](<Documentation [WIP]/CONTRIBUTING.md>): Environment setup, testing instructions, and pull request procedures.
- [**WIP Roadmap & Node Status**](<Documentation [WIP]/WIP_ROADMAP.md>): Implemented nodes, extension mappings, and compiler-internal nodes.

### Core Modules
- [**Spawning**](<Documentation [WIP]/Core/Spawning.md>) — `Spawner.Set_Plant`, `Spawner.Set_Zombie`, `Spawner.Set_Bullet`
- [**Board & Stages**](<Documentation [WIP]/Core/Board.md>) — Sun, Money, Wave, `Game.Stage`
- [**Event Triggers**](<Documentation [WIP]/Core/Triggers.md>) — Board lifecycle, input, plant/zombie reactions
- [**Game Functions & Tools**](<Documentation [WIP]/Core/Game functions.md>) — `InGameUI`, `Lawnf`, `Tool`, `WorldObject`
- [**Variables & Types**](<Documentation [WIP]/Core/Variables.md>) — `IntVar`, `FloatVar`, `BoolVar`, `StringVar`, `Int`, `Float`, `String`, `Bool`
- [**Conditionals**](<Documentation [WIP]/Core/Conditional statements.md>) — `If`, `Switch`
- [**Loops**](<Documentation [WIP]/Core/Loops.md>) — `For`, `While`
- [**Lists & Collections**](<Documentation [WIP]/Core/Lists.md>) — `PlantTypeList`, `ZombieTypeList`, `ForEachPlant`, `ForEachZombie`
- [**Multiple Choice Menus**](<Documentation [WIP]/Core/Multiple choice menu.md>) — `MultiSelectMenu`, `Option`
- [**Randomization**](<Documentation [WIP]/Core/Random.md>) — `Random`, `Random.Seeded`
- [**Time**](<Documentation [WIP]/Core/Time.md>) — `Time.Wait`, `Time.OnFixedUpdate`
- [**Config & Export**](<Documentation [WIP]/Core/Config.md>) — `Config`, `export`

### Libraries
- [**Types & Enums**](<Documentation [WIP]/Libraries/Types.md>) — `PlantType`, `ZombieType`, `ToolType`, `BulletType`, `KeyCode`, etc.
- [**Standard Library**](<Documentation [WIP]/Libraries/StdLib.md>) — `format_string`, `Dictionary`, `Array`, `WASDPlant`
- [**Math & Comparisons**](<Documentation [WIP]/Libraries/Math.md>) — `Math`, `Compare`

---

## Quick Example

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType, ToolType

# Configure level export
pft.Config(output="./output", name="CustomLevel")

# Set up event trigger
with pft.Trigger.OnBoardStart():
    # Spawn a peashooter at row 2, col 2
    plant = pft.Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.Peashooter)
    
    # Display message
    pft.InGameUI.display_text("Defend the lawn!", duration=4.0)

# Auto-exports on script exit or manual call to pft.export()
pft.export()
```

---

## Running Verification

```bash
# Type check with Pyright
npx pyright

# Run test suite
python -m unittest discover tests
```
