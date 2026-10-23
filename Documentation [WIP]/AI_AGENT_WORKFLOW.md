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
2. **Commit Directly per Prompt**: Commit working progress to the temporary branch at the end of every prompt turn:
   ```bash
   git add -A
   git commit -m "feat: description of work"
   ```
3. **Never Merge Without Approval**: Do not merge back into `main` or `root-rewrite` until the user explicitly responds with green-flag approval (e.g. "approved", "go ahead and merge", "green flag").

---

## 4. Verification Checklist

Before finishing any task, run both of these commands:

1. **Type Checker**:
   ```bash
   npx pyright
   ```
   *Requirement*: 0 errors, 0 warnings, 0 informations.

2. **Unit Test Suite**:
   ```bash
   .venv\Scripts\python.exe -m unittest discover tests
   ```
   *Requirement*: All tests must pass (OK).

---

## 5. Common Pitfalls & Solutions

| Issue | Symptom | Solution |
| :--- | :--- | :--- |
| **Enum bypass** | `TypeError: PlantType must be handled through the PlantType enum` | Pass an instance of `PlantType`, not an integer literal. |
| **Leaking raw node** | User code calls `.modify_health()` on a raw output port | Wrap the output port in `Plant(node.port_output_plant_Plant)`. |
| **Silent missing port** | Port name changed or not found in reflection definitions | Check [`definitions.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/definitions.py) and test against IL2CPP dump. |
| **PowerShell wildcard** | `Get-ChildItem "Documentation [WIP]"` returns nothing | In PowerShell, `[` and `]` are wildcards. Use `-LiteralPath "Documentation [WIP]"`. |
| **Markdown links on GitHub** | Absolute file links (`file:///...`) break on remote web UI | Use relative repository paths (e.g. `[Plant](../PvZ_Fusion_Transpiler_src/src/...)`). |
