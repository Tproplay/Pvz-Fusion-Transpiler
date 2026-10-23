# AI Agent Workflow & Forking Guide

This guide is specifically designed for developers and AI agents (such as Google Antigravity, Claude Code, Cursor, Copilot Workspace, Devin) working on, extending, or maintaining a fork of the **PvZ Fusion Transpiler**.

---

## 1. Quick-Start System Prompt for AI Agents

If you are initializing a new AI agent session or subagent to work on a fork of this codebase, provide it with the following core prompt:

```markdown
You are an expert compiler and visual scripting engineer working on the PvZ Fusion Transpiler.
Your task is to implement features, extend node mappings, or maintain the visual node graph transpiler.

STRICT OPERATING RULES:
1. Always wrap entities (Plant, Zombie, Bullet, WorldObject) in their respective extension wrapper classes. Never leak raw node ports to users.
2. Maintain clean __init__.py files in every directory. Never use brittle relative deep imports across submodules.
3. Keep files and functions modular. Decompose large methods into clear helper classes and functions.
4. Enforce strict Enum usage for PlantType, ZombieType, ToolType, BulletType, and KeyCode. Reject raw integer literals.
5. Never hardcode localized port strings in execution paths (e.g. '创建成功'); always reference port properties: `self.node.port_output_plant_Plant.name`.
6. Extensions must strictly represent Original node capabilities with clean ergonomics; do not invent unbacked runtime concepts in the base library.
7. Always work on a dedicated temporary branch. Commit directly after each prompt. Only merge to the base branch when given explicit user approval ("green flag").
8. Always verify changes using:
   - `npx pyright` (must pass with 0 errors, 0 warnings, 0 informations)
   - `.venv\Scripts\python.exe -m unittest discover tests` (all unit tests must pass)
```

---

## 2. The 6 Non-Negotiable Architectural Rules

These rules are enforced across all extensions and node mappings:

### Rule 1: Always Wrap Entity Pointers
- **Never** return raw port references or raw node instances from user-facing APIs.
- Spawner methods like `Spawner.Set_Plant()` must return a wrapped [`Plant`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/Entity/plant.py) instance.
- Spawner methods like `Spawner.Set_Zombie()` and loops like `ForEachZombie()` must yield a wrapped [`Zombie`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/Entity/zombie.py) instance.
- Bullet operations must return a wrapped [`Bullet`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/Entity/bullet.py) instance.
- Generic GameObject operations must return a wrapped [`WorldObject`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extentions/World/world_object.py) instance.

### Rule 2: Clean Module Export Hierarchy
- Every subfolder in `_Nodes/`, `_Data/`, and `Core/` must contain an `__init__.py` file exporting public symbols via `__all__`.
- Cross-folder imports should consume from module roots (e.g. `from ..Original import BindPlantNode` rather than `from ..Original.ObjectBinding.bind_plant_node import BindPlantNode`).

### Rule 3: Single Responsibility & Modular Classes
- Do not accumulate hundreds of helper functions into a single file.
- Divide domain logic into dedicated folders and files:
  - `_Nodes/Extentions/Entity/` for entity controls
  - `_Nodes/Extentions/Game/` for global game & stage operations
  - `_Nodes/Extentions/Lawn/` for board, cell, and map manipulation
  - `_Nodes/Extentions/UI/` for in-game HUD, cards, and text display
  - `_Nodes/Extentions/Input/` for tools, mouse, and keyboard listeners
  - `_Nodes/Extentions/World/` for GameObject transforms and binding

### Rule 4: Type-Safe Enum Enforcement
- Direct integers are **strictly disallowed** where an enum exists:
  - `Spawner.Set_Plant(0, 0, 1)` ❌ (Must be `PlantType.SunFlower`)
  - `Spawner.Set_Zombie(0, 0, 5)` ❌ (Must be `ZombieType.ConeZombie`)
  - `Tool.is_held(1)` ❌ (Must be `ToolType.Shovel`)
- Validation helpers (`_validate_plant_type`, `_validate_zombie_type`, `_validate_tool_type`, `_validate_bullet_type`) in [`nodes.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/nodes.py) raise `TypeError` when an integer literal is passed directly.

### Rule 5: Dynamic Port Name References
- Unity visual nodes use localized string names internally (e.g. `"触发"`, `"完成"`, `"植物"`).
- In execution path context managers and connection hooks, **never hardcode Chinese strings**:
  ```python
  # INCORRECT:
  with ExecutionPath(self.node, "完成"): ...

  # CORRECT:
  with ExecutionPath(self.node.port_output_trigger_Complete): ...
  ```

### Rule 6: No Fabricated Runtime Constructs in Base Extensions
- The base extension library must strictly provide clean abstractions over **native visual scripting nodes**.
- Complex data structures like virtual arrays and state dictionaries belong in `StdLib.py`, **not** in core node extensions.
- Optimization-only or redundant nodes (documented in [`_Nodes/NOT_IMPLEMENTED.txt`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/NOT_IMPLEMENTED.txt)) should not be exposed as user-facing extension methods.

---

## 3. Git Branching & Staging Workflow

When working on a fork or feature branch with an AI agent, follow this git discipline:

```
[root-rewrite / main] ─── (Branch off) ───> [temp-working]
                                                │
                                                ├─ Prompt 1: Implement & test
                                                │  └─ Directly commit to temp-working
                                                ├─ Prompt 2: Refactor & test
                                                │  └─ Directly commit to temp-working
                                                │
                                    User gives "GREEN FLAG"
                                                │
[root-rewrite / main] <── (Merge) ──────────────┘
```

1. **Create Branch**: Always branch off the target branch before starting work:
   ```bash
   git checkout -b temp-working
   ```
2. **Commit Per Prompt**: After fulfilling each prompt, stage and commit the changes directly to `temp-working`:
   ```bash
   git add -A
   git commit -m "feat: implement <feature-description>"
   ```
3. **Green Flag Merge**: Once the user explicitly approves ("green flag"), merge `temp-working` into the target branch:
   ```bash
   git checkout root-rewrite
   git merge temp-working
   ```

---

## 4. How to Update Nodes from New Game Versions

When a new PvZ Fusion game update is released:

1. **Extract IL2CPP Reflection Dump**:
   - Run the game with MelonLoader dump script.
   - Dump all event node definitions to [`_Nodes/Original/EventNodes_Definitions.txt`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/EventNodes_Definitions.txt).
2. **Run Definition Loader**:
   - [`definitions.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/definitions.py) automatically parses all node classes, string fields, and port names.
3. **Add or Update Node Classes**:
   - If a new node class appeared, add its class file in the appropriate subfolder of `_Nodes/Original/`.
   - Inherit from `EventNodeBase` or `EventSuggestedNode`.
   - Include any class-specific string fields as properties with reflection defaults.
4. **Expose in `nodes.py`**:
   - Add factory function in [`nodes.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/nodes.py) with port auto-wiring.
5. **Add High-Level Extension**:
   - Integrate into the corresponding extension module in `_Nodes/Extentions/`.
6. **Verify with Official Dump**:
   - Compare the exported JSON output against a level JSON generated by the in-game level editor (`Test.json`).

---

## 5. Pre-Completion Quality Checklist for Agents

Before completing any task, every AI agent must execute and verify:

- [ ] **Type Check**: Run `npx pyright` -> **0 errors, 0 warnings, 0 informations**.
- [ ] **Unit Tests**: Run `.venv\Scripts\python.exe -m unittest discover tests` -> **All tests pass**.
- [ ] **Clean Working Tree**: Verify no temporary or scratch files (`inspect_*.py`, `tmp*`, `Untitled.json`) remain untracked.
- [ ] **Direct Commit**: Commit all work to the working branch with a descriptive message.
- [ ] **Clickable Markdown Links**: Present file links in conversation using standard github markdown links with the `file://` scheme.
