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

## Documentation

Full documentation is available in the [`docs/`](file:///c:/Users/Tproplay/Desktop/Programming/Pvz%20Fusion%20Transpiler/docs/) directory:

- [**AI Agent Workflow Guide**](file:///c:/Users/Tproplay/Desktop/Programming/Pvz%20Fusion%20Transpiler/docs/AI_AGENT_WORKFLOW.md): Complete instructions, core rules, system prompt templates, and best practices for developers and AI coding agents forking or maintaining this repository.
- [**Architecture & System Design**](file:///c:/Users/Tproplay/Desktop/Programming/Pvz%20Fusion%20Transpiler/docs/ARCHITECTURE.md): Deep dive into the 3-layer architecture, reflection engine, context manager, and JSON level serialization.
- [**Contributing Guidelines**](file:///c:/Users/Tproplay/Desktop/Programming/Pvz%20Fusion%20Transpiler/docs/CONTRIBUTING.md): Environment setup, testing instructions, and pull request procedures.

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
