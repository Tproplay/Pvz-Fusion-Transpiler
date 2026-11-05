# AI Agent Workflow & Forking Guide

This guide is specifically designed for developers and AI agents (such as Google Antigravity, Claude Code, Cursor, Copilot Workspace, Devin) working on, extending, or maintaining a fork of the **PvZ Fusion Transpiler**.

---

## 1. Quick-Start System Prompt for AI Agents

If you are initializing a new AI agent session or subagent to work on this codebase, provide it with the following core prompt:

```markdown
You are an expert compiler and visual scripting engineer working on the PvZ Fusion Transpiler.
Your task is to implement features, extend node mappings, or maintain the visual node graph transpiler.

STRICT OPERATING RULES:
1. Always wrap entities (Plant, Zombie, Bullet, WorldObject) in their respective extension wrapper classes. Raw Plant/Zombie ports never leave an extension.
2. Maintain clean __init__.py files in every directory. Extensions create nodes ONLY through factory functions in nodes.py, never by importing Original node classes.
3. Keep functions short (< 40 lines) and avoid if/elif ladders over variants (use lookup tables/dispatch dictionaries).
4. Enforce strict Enum usage for PlantType, ZombieType, ToolType, BulletType, SceneType, MusicType, etc. Reject raw integer literals and sentinel ints like -1.
5. Never hardcode localized port strings in execution paths (e.g. '创建成功'); always reference port properties: `self.node.port_output_plant_Plant.name`.
6. Extensions must strictly represent Original node capabilities with clean ergonomics; do not invent unbacked runtime concepts in the base library.
7. Public API uses C#-style PascalCase (Add, TryGetValue, OnComplete). Old snake_case names stay as aliases.
8. No silent fallbacks. Unsupported types or arguments raise TypeError or ValueError. Operator traps (__len__, __contains__, __bool__) raise helpful errors.
9. Python-side state must not depend on execution paths; object port references remain immutable across branches.
10. Every new public API gets a snapshot test.
11. Unverified behavior is marked with @experimental.
12. Always work on a dedicated temporary branch (e.g., temp-working). Commit directly after each prompt. Only merge when given explicit user approval ("green flag").
13. Always verify changes using:
    - `python tools/check_rules_and_coverage.py` (0 rule violations, 100% native coverage)
    - `npx pyright` (0 errors, 0 warnings)
    - `python -m unittest discover tests` (all unit tests must pass)
```

---

## 2. The 11 Non-Negotiable Architectural Rules

These 11 rules are defined in [`_Nodes/RULES.txt`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/RULES.txt) and are strictly checked by [`tools/check_rules_and_coverage.py`](../tools/check_rules_and_coverage.py):

### Rule 1: Always Wrap Entity Pointers
- **Never** return raw port references or raw node instances from user-facing APIs.
- Spawner methods like `Spawner.Set_Plant()` must return a wrapped [`Plant`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/Entity/plant.py) instance.
- Spawner methods like `Spawner.Set_Zombie()` and loops like `ForEachZombie()` must yield a wrapped [`Zombie`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/Entity/zombie.py) instance.
- Bullet operations must return a wrapped [`Bullet`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/Entity/bullet.py) instance.
- Generic GameObject operations must return a wrapped [`WorldObject`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Extensions/World/world_object.py) instance.
- Values returned from loops, triggers, `TryX` helpers, and containers must always be wrapped.

### Rule 2: Clean Module Export Hierarchy & No Direct Original Imports
- Every subfolder in `_Nodes/`, `_Data/`, and `Core/` must contain an `__init__.py` file exporting public symbols via `__all__`.
- Extensions create nodes **only** through factory functions in [`nodes.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/nodes.py), **never** by importing concrete node classes from `_Nodes/Original/`.
- Between extension modules, prefer importing from the package (the folder's `__init__.py`) over importing from an internal file.

### Rule 3: Single Responsibility, Modular Classes & Table Dispatch
- Do not accumulate large functions. Target about 40 lines or fewer per function.
- No `if/elif` ladders that branch over types or operations. Use lookup tables and dictionary dispatch instead.
- Divide domain logic into dedicated folders in `_Nodes/Extensions/`:
  - `Entity/` for plant, zombie, and bullet controls
  - `Game/` for global game, camera, and stage operations
  - `Lawn/` for board, cell, grid items, and map manipulation
  - `UI/` for in-game HUD, cards, dialogs, and text display
  - `Input/` for tools, mouse, and keyboard listeners
  - `World/` for GameObject transforms, audio, and binding
  - `Branching/` for control-flow branching (`If`, `Switch`, `DoOnce`, `Pulse`)
  - `Loops/` for loops and entity iterators (`For`, `While`, `ForEach`)

### Rule 4: Type-Safe Enum Enforcement & Sentinel Rejection
- Direct integers are **strictly disallowed** where an enum exists:
  - `Spawner.Set_Plant(0, 0, 1)` ❌ (Must be `PlantType.SunFlower`)
  - `Spawner.Set_Zombie(0, 0, 5)` ❌ (Must be `ZombieType.ConeZombie`)
  - `Tool.is_held(1)` ❌ (Must be `ToolType.Shovel`)
  - `Lawnf.change_map(0)` ❌ (Must be `SceneType.Day`)
  - `Lawnf.change_music(2)` ❌ (Must be `MusicType.Day`)
- Integer sentinels such as `-1` are not allowed either: use `None` or an explicit enum member (`PlantType.Nothing`).
- Passing an enum of the wrong type (e.g. passing a `ZombieType` where a `PlantType` is expected) must raise `TypeError`.
- Existing APIs that still accept integers keep working for backward compatibility but emit a `DeprecationWarning`.

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
- The base extension library must strictly provide clean, thin abstractions over **native visual scripting nodes** (e.g. `List[T]` over list nodes, `Time.WaitUntil`).
- Complex simulated data structures (hash dictionaries, associative arrays, seeded RNG simulation) belong in `StdLib.py` or separate user packages, **not** in core extensions.

### Rule 7: Public API C#-Style PascalCase
- Public extension APIs use C#-style PascalCase (`Add`, `Count`, `TryGetValue`, `OnComplete`, `ChangeMap`, `DeleteGridItems`).
- Old `snake_case` names are retained as aliases for backward compatibility.
- Operations that can fail expose `TryX` returning `(value, ok)`.
- Exit branches use standard names: `OnSuccess`, `Failed` / `OnFailed`, `OnComplete`, `OnTimeout`.

### Rule 8: No Silent Fallbacks & Operator Traps
- Unsupported types or arguments must raise `TypeError` or `ValueError` with a clear message indicating what type is expected. Never default silently to `"int"` or the first match.
- Python operators that cannot work on visual graph values (`len()`, `"in"`, `bool()`, direct iteration) must raise descriptive `TypeError`s pointing to the correct API (e.g. `.Count`, `.Contains()`).

### Rule 9: Execution-Path Invariance
- Python-side state must not depend on which visual execution path runs at runtime.
- Methods called inside a branch or loop must not rebind an extension object's internal node or port pointers (`_root_port` immutability). The same Python object refers to the same node output across every path.

### Rule 10: Snapshot Testing
- Every new public API gets an automated snapshot test verifying the exact nodes and connections emitted.
- Existing transpiled output must not change unless documented in the agent report.

### Rule 11: Experimental Annotations
- Behavior that has not been verified against the live in-game engine must be marked with `@experimental` (e.g. `Board.Sun.Add()`, `Board.Money.Add()`, `Pulse`, `MenuKind.Typed`).

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

1. **Active Branch**: Stay on `temp-working` during implementation.
2. **Commit Directly per Prompt**: Commit working progress to the temporary branch at the end of every prompt turn:
   ```bash
   git add -A
   git commit -m "feat: description of work"
   git push origin temp-working
   ```
3. **Never Merge Without Approval**: Do not merge back into `main` or `root-rewrite` until the user explicitly responds with green-flag approval (e.g. "approved", "go ahead and merge", "green flag").

---

## 4. Verification Checklist

Before finishing any task, run all three verification commands:

1. **Automated Rules & Coverage Auditor**:
   ```bash
   python tools/check_rules_and_coverage.py
   ```
   *Requirement*: 0 violations, 100% native coverage (240/240).

2. **Type Checker**:
   ```bash
   npx pyright
   ```
   *Requirement*: 0 errors, 0 warnings, 0 informations.

3. **Unit Test Suite**:
   ```bash
   python -m unittest discover tests
   ```
   *Requirement*: All unit tests must pass (OK).

---

## 5. Common Pitfalls & Solutions

| Issue | Symptom | Solution |
| :--- | :--- | :--- |
| **Enum bypass** | `TypeError: PlantType must be handled through the PlantType enum` | Pass an instance of `PlantType`, not an integer literal. |
| **Dual-Import Enum Mismatch** | `TypeError: Expected BulletType ... received BulletType` | Use `validate_enum_field()` in `node.py`, which checks `type(val).__name__ == enum_cls.__name__`. |
| **Leaking raw node** | User code calls `.damage()` on a raw output port | Wrap the output port in `Zombie(node.port_output_zombie_Zombie)`. |
| **Silent missing port** | Port name changed or not found in reflection definitions | Check [`definitions.py`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/Original/definitions.py) and test against IL2CPP dump. |
| **PowerShell wildcard** | `Get-ChildItem "Documentation [WIP]"` returns nothing | In PowerShell, `[` and `]` are wildcards. Use `-LiteralPath "Documentation [WIP]"`. |
| **Markdown links on GitHub** | Absolute file links (`file:///...`) break on remote web UI | Use relative repository paths (e.g. `[Plant](../PvZ_Fusion_Transpiler_src/src/...)`). |
