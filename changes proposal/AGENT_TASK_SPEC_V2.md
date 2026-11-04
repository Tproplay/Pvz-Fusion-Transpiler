# 🤖 Agent Task Spec v2: Complete Extension Coverage for PvZ_Fusion_Transpiler

> **This file supersedes `AGENT_TASK_SPEC.md` and `AGENT_TASK_SPEC_ADDENDUM.md`.** It merges both and adds the review of `list_var.py`. The agent is already partway through (roughly 20%); the *Status* table below says what is known to exist so work is continued, not redone.
>
> **v2.1:** adds compliance with the project's `RULES.txt` (§1a), new fixes F14-F16, a rules lint, and moves the entity-list sugar out of scope (RULES.txt #6). Spec "Ground Rules" are written as *Ground Rule N*; project rules as *RULES.txt #N*.

---

## 0. Mission

Make **all 240 original nodes** reachable through Extensions, using the C#-style API defined in `EXTENSIONS_COVERAGE_PROPOSAL.md`, after a small set of consistency cleanups.

**Inputs (read all before touching code):**

| File | Purpose |
| :--- | :--- |
| `BASE_GAME_NODES_LIST.md` | Inventory of the 240 original nodes (ports, status) |
| `EXTENSIONS_IMPLEMENTATION_LIST.md` | What is wrapped today, plus the 44-node gap analysis |
| `EXTENSIONS_COVERAGE_PROPOSAL.md` | Target API for the 44 missing nodes (**source of truth for API shapes**) |
| `_Nodes/RULES.txt` | **Binding project rules** (six rules, see §1a). A proposed update is in `RULES_PROPOSED.txt` |
| `_Nodes/NOT_IMPLEMENTED.txt` | Existing skip decisions (read in Phase 0) |

**Code locations:** `_Nodes/Original/`, `_Nodes/Extentions/`, `nodes.py`, `StdLib.py`, `Core/`, `_Data/`.

### Status (known so far)

| Item | State |
| :--- | :--- |
| Node classes for all 240 nodes in `_Nodes/Original/` | ✅ already exist (including `do_once`, `pulse`, `repeat_until`, `wait_until`, `typed_choice_*`, `get_travel_entry`, all list nodes) |
| `Extentions/Variables/list_var.py` (`List[T]`, `ListOperation`, `ForEach`) | 🟡 first draft exists; needs the fixes in **§4** |
| `.gitignore` | ✅ present |
| `nodes.py` factories for the 39 gap nodes | ❓ verify which are missing (only 5 are known to exist) |
| Tests / example scripts | ❓ none visible in the package tree |

---

## 1. Ground Rules

1. **Never break existing public API.** Do not rename or delete a current class, method or property *during Phases 0-10*. Renames happen by adding a PascalCase alias next to the old name. (Structural renames are deferred to Phase 11, deliberately.)
2. **No change to existing output.** Before any edit, snapshot the transpiled output of every existing example or test script. After each phase those snapshots must be **byte-identical**, except where a phase says otherwise.
3. **Read ports from the node definitions, not from the docs.** If a doc and `_Nodes/Original/*` disagree, the node definition wins; log the mismatch in `AGENT_REPORT.md`.
4. **`RULES.txt` is binding** (see §1a). Where it conflicts with this spec, `RULES.txt` wins. The C#-style naming goal does not conflict with any current rule. If you find a real conflict, stop on that item and report it.
5. **Do not guess semantics.** Items marked 🔒 depend on unverified in-game behaviour. Implement them behind `@experimental` (transpile-time warning) and do not change any existing lowering because of them.
6. **One commit per phase**, each with passing tests.
7. **When something is ambiguous, stop on that item**, log it under *Open Questions* in `AGENT_REPORT.md` with the options you see, and continue with the rest.

---

## 1a. Project Rules (`RULES.txt`) and What They Mean Here

| # | Rule (short) | What it means for this work | Known violations / actions |
| :---: | :--- | :--- | :--- |
| 1 | Return Plant/Zombie in wrapped classes | Anything handing back a plant or zombie (loops, triggers, `TryCast`) returns the `Entity/plant.py` / `zombie.py` wrapper | None known; check `ForEach*` and `TryCast` outputs |
| 2 | `__init__.py` in every folder; avoid direct imports of Original node classes | Create nodes only through `nodes.*` factories; every new folder (e.g. `Collections/`) gets an `__init__.py`; prefer package imports over file imports | `list_var.py` imports from files (`..Abstract.execution_path`, `..Loops.loops`); see F16 |
| 3 | Keep functions small | No function over ~40 lines; no if/elif ladders over element types (use tables) | `List.__init__`, `_coerce_item_port`, `_resolve_type_key` and the five 7-way ladders in `list_var.py` (F4, F15) |
| 4 | Enums only, never raw ints | PlantType/ZombieType (and other enum-backed inputs) go through the enum. **New** APIs reject ints. **Existing** APIs that accept ints keep working but emit a `DeprecationWarning` (Ground Rule 1) | `list_var.py` accepts any `Enum` (F7); existing code audited in Phase 2f |
| 5 | No port-name literals | Use `self.node.port_output_<type>_<Name>.name` for `ExecutionPath` and port lookups | `ListOperation` uses `"完成"` / `"失败"`, and `list_var.py` uses `get_output("值")` / `get_output("有效")` (F14) |
| 6 | Extensions only wrap Original nodes; no new functionality | Thin wrappers and small compositions of Original nodes are fine (`List[T]`, `ForEach(list)`, `Clone`, `WaitUntil`). New data structures, algorithms and mechanics go in an extra library | **Out of scope:** entity-list sugar and `ToPlantTypeList()`. **Audit:** `StdLib.py` and `Random.Seeded` (Phase 2f, moved in 11f) |

Port names such as `完成`, `失败`, `值`, `有效` appear in this spec and in the proposal only to **describe the game's ports**. They must never appear as string literals in code (RULES.txt #5).

---

## 2. Phases (in this order)

### Phase 0: Baseline

- Locate the directories above and run the existing test suite. Record the result.
- **Tests and examples live outside the package.** The tree shows no `tests/` or `examples/`. Look for them in the parent directory; if none exist, create `tests/` and `examples/` as **siblings of the package** (not inside it), with at least one script per module under `Extentions/*`, *before any other change*.
- Create the golden snapshots described in Ground Rule 2.
- Read `RULES.txt` and `NOT_IMPLEMENTED.txt`. Carry any "why we skipped this" notes into the omission list. Log every conflict with this spec.
- Create `AGENT_REPORT.md` with sections: *Baseline*, *Doc/Code Mismatches*, *Open Questions*, *Decisions Taken*.

### Phase 1: Coverage tooling

Make the inventories generated, not hand-written.

- A script scans `_Nodes/Original/` and the extension sources and emits, per original node: category, ports, which extension modules reference it, and a status (`Implemented`, `Available in nodes.py`, `Omitted (reason)`).
- Regenerate the hard-coded counts (196 / 44 / 31 / etc.) in both inventory files from it.
- Add a check: **every original node is either referenced by at least one extension or on an explicit, reasoned omission list.** It starts failing for the 44 gap nodes; keep an expected-failure list that shrinks as phases complete.
- Add a **rules lint** (report-only at first, enforced for new code): (a) every folder under `_Nodes` has an `__init__.py` (RULES.txt #2); (b) no imports of node classes from `_Nodes/Original/*` inside `Extentions` (#2); (c) no CJK string literal passed to `ExecutionPath(...)` or `get_output(...)` (#5); (d) functions longer than 40 lines are listed (#3); (e) PlantType/ZombieType parameters with int defaults are listed (#4).

### Phase 2: Consistency cleanups (non-breaking)

**2a. Branch/exit naming.** Pick one scheme and add aliases for the old names:

| Meaning | Standard name | Old names kept as aliases |
| :--- | :--- | :--- |
| Success exit | `OnSuccess` | `on_created`, `on_success` |
| Failure exit | `Failed` for `with x.Failed:` bodies, `OnFailed` where it is a stored port | `on_failed`, `tx.Failed` |
| Loop finished | `OnComplete` | `on_complete` |
| Timeout | `OnTimeout` | (new) |

Apply to `Spawner.*`, `Board.Sun/Money` transactions, `ForEach*`, `Time.OnFixedUpdate`.

**2b. Fallible-return rule.** Any node with a validity-style output (`有效`, `存在`, `包含`) exposes a `TryX(...)` returning `(value, ok)`: `Int.TryParse`, `Float.TryParse`, `PlantType.TryParse`, `ZombieType.TryParse`, `Object.TryCast[T]`, `Math.TryPow`, `Math.TryLog` (see proposal §1). Existing methods stay unchanged.

**2c. De-duplicate exposure.** `GameOverNode`, `GameWinNode` and `GetTravelBuffNode` are exposed from both `Game\game.py` and `Lawn\lawnf.py`. Keep `Game` canonical; make the `Lawnf` versions forward to it.

**2d. Signature audit (report only).** Compare each signature to the node's real ports **and fields**, and log the result:

- `Lawnf.set_zombie_house_rule(rule_id)` vs `SetZombieHouseRuleNode` (its input is a Bool, `进家失败`)
- `Zombie.play_animation(name)` vs `PlayZombieAnimNode`
- `Lawnf.change_event_map(map_id)` / `change_event_music(music_id)` vs their nodes

`_Data/` already has `SceneType.py`, `ZombieAnimations.py`, `SoundType.py` and `ToolType.py`. These parameters may be enum-backed node **fields** rather than ports, so check before calling anything a mismatch. There is no music enum and no house-rule enum; if one is needed, propose it in the report without inventing values. Fix only if the correct behaviour is unambiguous.

**2e. (Optional, last) Split `Lawnf`** into props/effects, board queries, audio and map/music/rules modules, keeping `Lawnf.*` as a facade. Skip if it risks Ground Rule 2.

**2f. Rules audit (report; fix only what is unambiguous).** Use the Phase 1 lint and list violations of `RULES.txt` in existing code in `AGENT_REPORT.md`:

- **#5:** hard-coded port-name literals in `ExecutionPath(...)` / `get_output(...)` across `_Nodes/Extentions`. Replace with `node.port_output_<type>_<Name>.name`; transpiled output must stay identical.
- **#4:** enum-backed parameters that accept or default to raw ints. The docs show `Lawnf.spawn_ice_block(..., plant_type=-1)`, `Trigger.OnKeyDown(key_code)` ("enum or int"), and `*_id` parameters on `change_event_map`, `change_event_music` and `set_zombie_house_rule`. Do not remove int support; accept the enum (or `None` instead of `-1`) and emit a `DeprecationWarning` for ints.
- **#6:** `StdLib.py` (`Dictionary`, `Array`, `WASDPlant`) and `Random.Seeded` add new functionality rather than wrapping nodes. Report only; they move out in Phase 11f.
- **#2 / #3:** folders missing `__init__.py`, direct imports of `_Nodes/Original` node classes inside `Extentions`, and functions over 40 lines. Report only; refactor opportunistically when touching a file.

### Phase 3: `List[T]` (33 nodes)

Spec as in proposal §3, with these requirements:

- **Factories first:** for each of the 39 gap nodes without a function in `nodes.py` (list, `DoOnce`, `Pulse`, `RepeatUntil`, `WaitUntil`, `TypedChoice*`, `GetTravelEntry`), add the factory, following the existing factory conventions.
- **Extend `Extentions/Variables/list_var.py`**; do not create a parallel list module. Apply every fix in **§4**.
- `List[T]` for `T` in `Bool, Float, Int, String, GameObject, PlantType, ZombieType`. The element type is chosen at transpile time and enforced.
- Members: `Add`, `Insert`, indexer get/set, `TryGetValue`, `Replace`, `IndexOf`, `Contains`, `TryFindIndex`, `RemoveAt`, `Clear`, `Count`, `CopyTo`, `Clone`, plus `ForEach(list)`.
- **Initial values** (`List[Int]([1, 2, 3])`) are baked into the `ListVariableNode`, not emitted as an Append chain. This is the accepted design (fewer nodes).
- Make `ZombieTypeList` a thin subclass/alias of `List[ZombieType]`; keep every existing method (`append`, `contains`, `find_index`, `get_item`, `remove_at`, `clear`) working and add `Insert` / `Replace`.
- **Leave `PlantTypeList` alone.** It is a different port type (value list, not `ListVariable`).
- Aliases: `IntList`, `FloatList`, `BoolList`, `StringList`, `ObjectList`, `PlantTypeListVar`, **and** `ZombieTypeListVar`.
- **`List[Plant]` / `List[Zombie]` must not silently become `PlantType` / `ZombieType` lists; they raise `TypeError`.** The entity-list sugar (proposal §3.7) and the `List[PlantType].ToPlantTypeList()` bridge are **out of scope** for the base library (RULES.txt #6: new functionality belongs in an extra library). Do not implement them.

**Exception to Ground Rule 2:** existing `ZombieTypeList` methods must keep identical output; new methods may emit new nodes.

### Phase 4: Sun / Money `Add` 🔒

- Add `Board.Sun.Add(n)` → `GetSunNode` and `Board.Money.Add(n)` → `GetMoneyNode`, marked `@experimental`.
- **Do not change how `+=` lowers.** That waits for in-game confirmation that these nodes add the amount.

### Phase 5: `ToolType`

- Implicit lowering of `ToolType.X` to `ToolTypeValueNode` where a ToolType port is expected, plus `Tool.Value(t)`. Use the enum in `_Data/ToolType.py`.
- `mouse.Item == ToolType.X` via `__eq__` → `CompareToolTypeNode`.
- `Tool.IsHeld`, `GetCooldown`, `SetCooldown` output must be unchanged.

### Phase 6: Flow nodes

- `DoOnce()` with `.Reset()` (proposal §6.1).
- `Time.WaitUntil(cond, interval, max_checks)` with body = `完成`, `.OnTimeout`, `.OnFailed` (§6.3).
- `Time.RepeatUntil(cond, interval, max_checks)` with `.OnEach`, `.OnComplete`, `.OnTimeout`, `.OnFailed` (§6.4).
- `cond` is a **live Bool data wire**, re-evaluated each check: it must not be constant-folded, cached or hoisted by the optimizer.
- Do not alter `While`; it is a different construct.

### Phase 7: `Pulse` 🔒

- `Pulse(state)` with `.OnPulse` (§6.2), marked `@experimental`. Document it as "behaviour unverified" and make no claims about periodic behaviour.

### Phase 8: Typed menus 🔒

- `MultiSelectMenu(..., kind=MenuKind.Typed)`; options and merges inherit the menu's kind (§7). Default (`Standard`) output must stay byte-identical. Mark `Typed` `@experimental`.

### Phase 9: Obsolete

- Add an `@Obsolete(message)` decorator that emits a transpile-time warning.
- Expose `Game.GetTravelEntry()` → `GetTravelEntryNode`, marked obsolete (§8).

### Phase 10: Docs

- Regenerate both inventory files with the Phase 1 script.
- Update `EXTENSIONS_IMPLEMENTATION_LIST.md` with the new classes and aliases; replace the gap-analysis section with the remaining `@experimental` items.

### Phase 11: Structural changes (only after Phases 0-10 are done)

Do **not** run these while other phases are in progress; each touches many imports. Re-run the Phase 0 snapshots afterwards.

| # | Change | Why | How |
| :---: | :--- | :--- | :--- |
| 11a | Rename root `typing.py` (e.g. `port_types.py`) | A module named `typing.py` shadows the standard library's `typing` **whenever the package directory itself is on `sys.path`** (script run from inside the root, IDE source root, `python -m` from inside). Then `enum`, `dataclasses` and much of the stdlib break confusingly. | Rename and fix imports (`from ....typing import ...` in `list_var.py` and others). **No `typing.py` shim**: the file name is the problem. Separate internal `from .typing import X` from stdlib `import typing` when searching. If the package folder is ever on `sys.path` directly, do this **first, immediately**. |
| 11b | Rename `Core/uuid.py` (e.g. `node_id.py`) | Same shadowing issue with stdlib `uuid`, lower risk | Rename and fix imports |
| 11c | Rename `Extentions` → `Extensions` | Typo baked into every import path and doc; cheap now, costly later | Rename folder, update imports and docs. Add a deprecated `Extentions` re-export shim **only if** user scripts import from `_Nodes.Extentions` directly |
| 11d | Merge duplicate module name `Entity/loops.py` + `Loops/loops.py` | Same file name for related things | Move `ForEach*` to `Loops/for_each.py`; leave a re-export in `Entity/loops.py` |
| 11e | *(Optional)* `Extensions/Collections/` | After `List[T]` there are three list-ish homes | Move `list_var.py`, `plant_type_list.py`, `zombie_type_list.py` there; keep old import paths as re-exports |
| 11f | Move `StdLib.py` (`Dictionary`, `Array`, `WASDPlant`) and `Random.Seeded` out of the base library | RULES.txt #6: new data structures and mechanics belong in an extra library | Create a separate package that imports from the base. Keep a deprecated re-export in the base for one release if user scripts import them. **Only after the owner confirms the extra library's name and location** |

### Phase 12: Deletions and moves

| Path | Action | Reason |
| :--- | :--- | :--- |
| `project_tree.txt` (root) | Delete from the repo; regenerate when needed | Generated artifact, and saved as **UTF-16**, which breaks most tools. Regenerate with `tree /F /A \| Out-File -Encoding utf8 project_tree.txt` |
| `_Nodes/NOT_IMPLEMENTED.txt` | Delete **after** Phase 1's generated report exists and its notes are carried over | Hand-maintained status list; stale after this work |
| `_Data/Dumps/LatestAnimations.log` | Remove from the repo (already covered by `.gitignore` once removed from tracking) | Generated by `dump_animations.py` |
| `_Data/dump_animations.py` | Move to a `tools/` folder **outside** the package | Developer script shipping inside the runtime package |
| `_Nodes/Original/EventNodes_Definitions.txt`, `EventNodes_PortDefinitions.txt` | **Keep** if `definitions.py` reads them; otherwise move to `docs/reference/` | Raw dumps; check what loads them first |

---

## 3. Required Tests (minimum)

| Area | Test |
| :--- | :--- |
| Regression | Golden snapshots from Phase 0 unchanged after every phase |
| `List[T]` | One snapshot per `T` (all 7) for `Add`, `Insert`, indexer get, indexer set, `IndexOf`, `Contains`, `RemoveAt`, `Clear`, `CopyTo` |
| `List[T]` | `.Failed` branch wires to the `失败` port |
| `List[T]` | **Branch safety:** `Add` inside an `If`, then `.Count` after it: the Count node's list input is wired to the **original `ListVariableNode`**, not to the Append node |
| `List[T]` | `TryGetValue` emits **exactly one** get-item node, and both returned ports come from it |
| `List[T]` | `List()` with no type, `List[Plant]`, `List[Zombie]`, `List["foo"]`, and mixing a ZombieType value into `List[PlantType]` all raise `TypeError` |
| `List[T]` | `List[Int] is List[Int]` is true (cached); `isinstance(x, List[Int])` works |
| `List[T]` | `len(items)`, `5 in items` and `if items:` raise a helpful `TypeError` |
| `List[T]` | Two unnamed lists get **distinct** variable names; a clone gets a name distinct from its source |
| `ForEach(list)` | Emits `ForLoopNode` + item getter; `OnComplete` fires after the loop |
| `ZombieTypeList` | All pre-existing methods produce identical output |
| `ToolType` | Enum member used as a port emits exactly one `ToolTypeValueNode` |
| `WaitUntil` / `RepeatUntil` | Condition wire is connected live (not folded); each exit maps to the right output port |
| `DoOnce` | `.Reset()` wires the `重置` trigger |
| Typed menu | `Standard` output identical to today; `Typed` emits the three `TypedChoice*` nodes |
| `@experimental` / `@Obsolete` | Emit a warning at transpile time |
| Coverage check | Expected-failure list shrinks to the 🔒 items only (or zero once confirmed) |
| Rules lint | Passes for all new code; existing violations are listed in `AGENT_REPORT.md` |
| `ListOperation` | Exec paths are built from the node's port attributes (`.name`); `list_var.py` contains no CJK string literals |

---

## 4. Fixes Required in `Extentions/Variables/list_var.py`

Review of the first draft. Names refer to that file. Priority order: **P1** = likely correctness bug, **P2** = should fix, **P3** = minor.

### P1: Correctness

**F1. Do not rebind `self._current_port` after `Add` / `Insert` / `Replace`.**
These methods set `self._current_port = node.port_output_listvariable_List`. That is Python-level state changing on *every* path, while the graph only changes on paths that execute:

```python
with If(cond):
    items.Add(5)        # _current_port now points at Append's output
n = items.Count         # reads Append's output even when cond was false
```

`RemoveAt`, `Clear` and `CopyTo` do not rebind (they have no list output), which suggests list ops are in-place. Keep one **root port** (the `ListVariableNode` output, `port_output_listvariable_Variable`) and always use it. Delete the three rebinding lines. If `List(initial=other_list)` aliases another list, alias that list's root port.
*Verify in-game (item 8 in §5) that the Append output is the same list reference as its input.*

**F2. `TryGetValue` creates the get-item node twice, and evaluates a fallback eagerly.**
It calls `_get_item_node(index)` and then `self[index]`, which calls it again (a duplicate node on every call). It also uses `getattr(node, "port_output_bool_Valid", node.get_output("有效"))`, where the default argument is evaluated even when the attribute exists. Build one node, then read both ports from it:

```python
def TryGetValue(self, index):
    node = self._get_item_node(index)              # exactly one node
    return self._value_port(node), node.port_output_bool_Valid
```

**F3. Unknown or ambiguous element types must raise, not silently become `int`.**
Today `_resolve_type_key` falls back to `"int"`, passes unknown strings through, and matches by *substring* of the class name (so `List[Plant]` becomes a **PlantType** list). `List()` with no type is silently an int list, and every if/elif chain also defaults to int. Replace with an exact lookup:

```python
_TYPE_KEYS = {
    int: "int", float: "float", bool: "bool", str: "string",
    Int: "int", Float: "float", Bool: "bool", String: "string",   # the DSL classes
    PlantType: "plant_type", ZombieType: "zombie_type", GameObject: "object",
}

def _resolve_type_key(t):
    try:
        return _TYPE_KEYS[t]
    except (KeyError, TypeError):
        raise TypeError(f"Unsupported List element type: {t!r}")
```

Drop the loose string aliases (`"plant"`, `"entity"`, `"text"`, ...) or keep only exact canonical keys. Unsubscripted `List()` with no `element_type` raises with a message pointing to `List[Int]`.

**F14. Port names are hard-coded (RULES.txt #5).** `ListOperation` builds `ExecutionPath(self.node, "完成")` and `ExecutionPath(self.node, "失败")`, and the file calls `node.get_output("值")` / `get_output("有效")`. Replace each with the node's port attribute and its `.name`, following the `port_output_<type>_<Name>` convention used by the node classes in `_Nodes/Original/Variables/List/` (look up the exact attribute names there, and add them to the node classes if they are missing). `ListOperation` is shared by every element type, so this is one fix in one place.

### P2: Should fix

**F4. Replace the repeated if/elif chains with one table (required by RULES.txt #3).**
`Add`, `Insert`, `Replace`, `_get_item_node` and `_find_value_node` each branch over 7 types (35 branches). Use a single table; this also removes the `hasattr` probing in `__getitem__`:

```python
_OPS = {
    "int": dict(append=nodes.append_int_list, insert=nodes.insert_int_list,
                replace=nodes.replace_int_list, get=nodes.get_int_list_item,
                find=nodes.find_int_list_value, value_port="port_output_int_Value"),
    "plant_type": dict(append=nodes.append_plant_type_list, ...,
                       value_port="port_output_planttype_Value"),
    # ... one entry per key in _TYPE_KEYS
}

def Add(self, item):
    node = _OPS[self._type_key]["append"](list_var=self._root_port,
                                          value=self._coerce_item_port(item))
    return ListOperation(node)
```

**F5. Cache the bound classes.** `__class_getitem__` builds a new subclass on every access, so `List[Int] is List[Int]` is false and `isinstance(x, List[Int])` fails. Keep a module-level dict keyed by `(cls, type_key)`.

**F6. Default variable names collide.** Every list defaults to `"列表"` and every clone to `"克隆列表"`. If the game identifies variables by name, unnamed lists could share state. Check how `IntVar` / `FloatVar` pick default names and reuse that mechanism; otherwise generate `f"列表_{n}"` from a counter.

**F7. Validate enums by type (RULES.txt #4).** `_coerce_item_port` accepts *any* `Enum` for plant and zombie lists, so a `ZombieType` value can go into a plant list. Check `isinstance(val, PlantType)` / `isinstance(val, ZombieType)` (or a port), and raise otherwise. Do the same validation for items in `initial`.

**F8. Static typing.** `Generic` / `TypeVar` are imported but unused, and the package ships `py.typed`, so type checkers reject `List[Int]`. Add a `list_var.pyi` stub declaring `class List(Generic[T])` (keeps the runtime `__class_getitem__` untouched). Note that `List` also clashes in name with `typing.List` for anyone who imports both.

**F15. Function size (RULES.txt #3).** F4's table is therefore **required**, not optional. Also split `List.__init__` (building from `initial`), `_coerce_item_port` (per-type coercion) and `_resolve_type_key` into small helpers or per-type strategy objects, each well under 40 lines.

**F16. Imports (RULES.txt #2).** The file imports from modules (`..Abstract.execution_path`, `..Loops.loops`, `....Core.context`). Check how the other extension modules do it. Where a package `__init__.py` already exports the name, import from the package (watch for circular imports; the function-level import of `For` in `ForEach` may need to stay local). Node creation already goes through `nodes.*` factories, which is correct.

### P3: Minor

- **F9.** Remove `set` from the accepted `initial` / `+=` inputs (arbitrary order).
- **F10.** Add `__len__` and `__contains__` that raise `TypeError` ("use `.Count`" / "use `.Contains(item)`"). This also stops `if items:` from being silently always-true.
- **F11.** `List[Int](other_list)` currently aliases the other list, whereas C#'s `new List<int>(other)` copies. Either copy (via `Clone`) or document it clearly.
- **F12.** `with ForEach(items) as item` exposes no `index`. Document `loop = ForEach(items); with loop as item: ... loop.index`.
- **F13.** Add the `ZombieTypeListVar` alias and finish migrating `ZombieTypeList` onto this class.

---

## 5. Human-Owned Verification (the agent cannot do these)

These need in-game testing. Do **not** resolve them by assumption.

| # | Question | Unlocks |
| :---: | :--- | :--- |
| 1 | Does `GetSunNode` / `GetMoneyNode` **add** the amount? | Lowering `Board.Sun += x` / `Board.Money += x` to a single node; removing `@experimental` |
| 2 | What does `PulseNode` do with `状态` (rising edge, any change, or fire while true)? | Documenting `Pulse` |
| 3 | How do `TypedChoice*` differ from `MultipleChoice*`? Can their `ChoiceOptions` wires mix? | Removing `@experimental` from `MenuKind.Typed` |
| 4 | `Find*ListValueNode`: what is `索引` when the value is absent? | Defining `IndexOf` not-found behaviour |
| 5 | `Wait/RepeatUntil`: meaning of `最多检查次数` ≤ 0; when `失败` fires vs `超时` | Documenting defaults |
| 6 | Does the game type-check `ListVariable` contents at runtime? | Whether `List[T]` is the only type guard |
| 7 | Does casting a stored `GameObject` of a dead entity return `存在 = false` safely? | Entity-list sugar |
| 8 | Do `Append/Insert/Replace` mutate the list **in place**, with their `列表` output being the same reference as the input? | F1 (using only the root port) |
| 9 | Are list/variable assets identified by **name** in the game? | F6 (default-name collisions) |

## 6. Still Needed From the Human

1. The contents of `_Nodes/NOT_IMPLEMENTED.txt`. (`RULES.txt` has been reviewed and is reflected in §1a.)
2. Where the existing test/example scripts live (not in the package tree).
3. Whether the package folder is ever on `sys.path` directly. If yes, do Phase 11a first.
4. Approval (or edits) for `RULES_PROPOSED.txt`. Until you approve it, only the six existing rules apply.
5. Where the extra library for `StdLib` / `Random.Seeded` should live (Phase 11f).

---

## 7. Definition of Done

- [ ] Phase 0 snapshots unchanged (except documented exceptions), re-run after Phase 11
- [ ] Coverage check passes for all 240 nodes (🔒 items allowed as `@experimental`)
- [ ] Every new API has the tests in §3
- [ ] All P1 and P2 fixes in §4 applied (P3 applied or logged)
- [ ] Rules lint passes for all new code; existing violations are listed in `AGENT_REPORT.md`
- [ ] Both inventory files regenerated by script
- [ ] Phase 11 and Phase 12 completed (or each skipped item logged with a reason)
- [ ] `AGENT_REPORT.md` lists every doc/code mismatch, open question and decision taken
- [ ] No existing public name removed or renamed before Phase 11
