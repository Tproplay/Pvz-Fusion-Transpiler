# 🧩 Extensions Coverage Proposal: Closing the Last 44 Original Nodes

**Goal:** every one of the 240 original nodes becomes reachable through an Extension, using a C#-style API.
**Today:** 196 / 240 are wrapped. This file specifies the API for the remaining **44** (5 + 31 + 4 + 3 + 1, per the gap analysis).

Design principles:

1. **One generic `List[T]` instead of 31+ new classes.** It mirrors C#'s `List<T>`, and the 33 list nodes collapse into one set of members.
2. **Everything else slots into classes that already exist** (`Board.Sun`, `Board.Money`, `Tool`, `Time`, `MultiSelectMenu`, `Game`). No new top-level concepts except `DoOnce` and `Pulse`.
3. **Nothing is unreachable.** Nodes the team does not want people using are still exposed, but marked `[Obsolete]` so the transpiler warns.

---

## 1. Naming Conventions (C#-style)

| Rule | Convention | Example |
| :--- | :--- | :--- |
| Members | `PascalCase` methods and properties. Existing `snake_case` names stay as aliases, so nothing breaks. | `Board.Sun.Add(50)` |
| Fallible ops | `TryX` returns a tuple `(value, ok)`, where `ok` is the node's `有效` / `存在` / `包含` port | `value, ok = items.TryGetValue(i)` |
| Unchecked ops | `Cast`, indexers and plain getters ignore the validity port | `items[i]` |
| Generics | Subscript syntax | `List[Int]`, `Object.TryCast[Plant](obj)` |
| Multi-exit nodes | Context manager, branches named after the exit port | `.Failed`, `.OnComplete`, `.OnTimeout` |
| Enum values | `PascalCase` members auto-lower to the matching `*TypeValueNode` when used as a port | `ToolType.Shovel` |
| Discouraged API | `@Obsolete("use X")` emits the node plus a transpile-time warning | `Game.GetTravelEntry()` |

### Optional aliases for already-covered nodes (no new node coverage, only C# feel)

| C#-style alias | Wraps (already implemented) | Replaces |
| :--- | :--- | :--- |
| `Object.TryCast[Plant](obj)` → `(Plant, ok)` | `ObjectToPlantNode` | `WorldObject.try_cast_to_plant()` |
| `Object.TryCast[Zombie](obj)` → `(Zombie, ok)` | `ObjectToZombieNode` | `WorldObject.try_cast_to_zombie()` |
| `Object.Cast[Plant](obj)` / `Object.Cast[Zombie](obj)` | `ObjectToPlantNode` / `ObjectToZombieNode` | `WorldObject.to_plant()` / `to_zombie()` |
| `Int.TryParse(text)` → `(value, ok)` | `StringToIntNode` | `Int.Cast(string)` |
| `Float.TryParse(text)` → `(value, ok)` | `StringToFloatNode` | `Float.Cast(string)` |
| `PlantType.TryParse(text)` / `ZombieType.TryParse(text)` | `StringToPlantTypeNode` / `StringToZombieTypeNode` | `String.to_plant_type()` / `to_zombie_type()` |
| `Math.Pow(x, y)`, `Math.Log(x, b)` → `(result, ok)` via `Math.TryPow` / `Math.TryLog` | `PowerNode`, `LogarithmNode` (both expose `有效`) | `Math.pow`, `Math.log` |

---

## 2. Coverage Summary

| Gap group | Nodes | Proposed API | Section |
| :--- | :---: | :--- | :---: |
| Deferred list nodes | 31 | `List[T]` (generic, 7 element types) | 3 |
| Zombie list Insert/Replace (in `nodes.py`) | 2 | `List[ZombieType]` / `ZombieTypeList.Insert`, `.Replace` | 3 |
| `GetSunNode`, `GetMoneyNode` | 2 | `Board.Sun.Add()`, `Board.Money.Add()` | 4 |
| `ToolTypeValueNode` | 1 | `ToolType.X` (implicit) and `Tool.Value()` | 5 |
| `DoOnce`, `Pulse`, `RepeatUntil`, `WaitUntil` | 4 | `DoOnce`, `Pulse`, `Time.RepeatUntil`, `Time.WaitUntil` | 6 |
| `TypedChoice*` | 3 | `MultiSelectMenu(kind=MenuKind.Typed)` | 7 |
| `GetTravelEntryNode` | 1 | `[Obsolete] Game.GetTravelEntry()` | 8 |
| **Total** | **44** | | |

A node-by-node checklist is in **Appendix A**.

---

## 3. `List[T]`: Dynamic Lists (33 nodes)

### 3.1 Why generic

The node graph has one `ListVariableNode` plus per-type Append/Get/Insert/Replace/Find nodes. A single `List[T]` class picks the right node from `T` at transpile time, so users never think about it. That is exactly how C# generics read, and it enforces element type at compile time (the `ListVariableNode` itself carries no type).

`IntList`, `StringList` and so on can exist as plain aliases (`IntList = List[Int]`) for people who prefer them.

### 3.2 Element-type dispatch

| `T` | Append | Get Item | Insert | Replace | Find Value | Status today |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Bool` | `AppendBoolListNode` | `GetBoolListItemNode` | `InsertBoolListNode` | `ReplaceBoolListNode` | `FindBoolListValueNode` | all deferred |
| `Float` | `AppendFloatListNode` | `GetFloatListItemNode` | `InsertFloatListNode` | `ReplaceFloatListNode` | `FindFloatListValueNode` | all deferred |
| `Int` | `AppendIntListNode` | `GetIntListItemNode` | `InsertIntListNode` | `ReplaceIntListNode` | `FindIntListValueNode` | all deferred |
| `String` | `AppendStringListNode` | `GetStringListItemNode` | `InsertStringListNode` | `ReplaceStringListNode` | `FindStringListValueNode` | all deferred |
| `GameObject` | `AppendObjectListNode` | `GetObjectListItemNode` | `InsertObjectListNode` | `ReplaceObjectListNode` | `FindObjectListValueNode` | all deferred |
| `PlantType` | `AppendPlantTypeListNode` | `GetPlantTypeListItemNode` | `InsertPlantTypeListNode` | `ReplacePlantTypeListNode` | `FindPlantTypeListValueNode` | all deferred |
| `ZombieType` | `AppendZombieTypeListNode` ✅ | `GetZombieTypeListItemNode` ✅ | `InsertZombieTypeListNode` (nodes.py) | `ReplaceZombieTypeListNode` (nodes.py) | `FindZombieTypeListValueNode` ✅ | partial |

Type-independent nodes (already implemented, reused by every `T`): `ListVariableNode`, `GetListLengthNode`, `RemoveListItemNode`, `ClearListValuesNode`.
Type-independent, **new**: `CopyListValuesNode`.

### 3.3 Members

| C# member | Python DSL | Lowers to | Notes |
| :--- | :--- | :--- | :--- |
| `list.Add(item)` | `items.Add(x)` | `Append{T}ListNode` | Statement. Use `with items.Add(x) as op:` + `op.Failed` for the failure exit |
| `list.Insert(i, item)` | `items.Insert(i, x)` | `Insert{T}ListNode` | Same `.Failed` pattern |
| `list[i]` | `items[i]` | `Get{T}ListItemNode.值` | Ignores validity |
| `list.TryGetValue(i, out v)` | `v, ok = items.TryGetValue(i)` | `Get{T}ListItemNode` (`值`, `有效`) | |
| `list[i] = x` / `list.Replace(i, x)` | `items[i] = x` | `Replace{T}ListNode` | |
| `list.IndexOf(x)` | `items.IndexOf(x)` | `Find{T}ListValueNode.索引` | Not-found value must be verified (see §9) |
| `list.Contains(x)` | `items.Contains(x)` | `Find{T}ListValueNode.包含` | Returns a Bool port, usable in `If(...)` |
| `list.TryFindIndex(x)` | `i, found = items.TryFindIndex(x)` | `Find{T}ListValueNode` (`索引`, `包含`) | |
| `list.RemoveAt(i)` | `items.RemoveAt(i)` | `RemoveListItemNode` | Already in `ZombieTypeList` as `remove_at` |
| `list.Clear()` | `items.Clear()` | `ClearListValuesNode` | |
| `list.Count` | `items.Count` | `GetListLengthNode` | Property, returns Int port |
| `list.CopyTo(dest)` | `items.CopyTo(other)` | `CopyListValuesNode` | **New node** |
| `list.Clone()` | `items.Clone()` | `ListVariableNode` + `CopyListValuesNode` | Composite helper |
| `foreach (var x in list)` | `with ForEach(items) as x:` | `ForLoopNode(Count)` + `Get{T}ListItemNode` | Composite, see §3.5 |

All `.Failed` exits map to the `失败` trigger port of the corresponding node.

### 3.4 Example

```python
queue = List[Int](name='spawn_queue')

with Trigger.OnBoardStart():
    queue.Add(3)
    queue.Add(5)
    queue.Insert(0, 1)                      # InsertIntListNode

    with queue.Add(9) as op:                # optional failure branch
        with op.Failed:
            InGameUI.display_text('add failed')

    value, ok = queue.TryGetValue(2)
    with If(ok):
        Board.Sun.Add(value * 25)

    with If(queue.Contains(5)):
        queue[0] = 7                        # ReplaceIntListNode
```

### 3.5 `ForEach` lowering

`ForEachPlantNode`, `ForEachZombieNode` and `ForEachPlantTypeNode` take typed *value* lists, not `ListVariable`s, so a `List[T]` cannot be iterated by a native node. Lower it as a composite:

```python
with ForEach(queue) as item:                # → For(queue.Count) + queue[loop.index]
    Board.Sun.Add(item)
# Exposes: item (value), ForEach.index, ForEach.on_complete
```

### 3.6 Relationship to existing list classes

| Class | Backing | Plan |
| :--- | :--- | :--- |
| `ZombieTypeList` | `ListVariable` of ZombieType | Becomes `List[ZombieType]` plus PascalCase aliases (`Append`→`Add`, `find_index`→`IndexOf`, `get_item`→indexer). Gains `Insert` / `Replace` |
| `PlantTypeList` | Value-type list (`Single/Multi/Merge/Remove...`) | **Stays as-is.** It is a different port type (`PlantTypeList`, not `ListVariable`) |
| `List[PlantType]` | `ListVariable` of PlantType | New. Mutable container. (A `ToPlantTypeList()` bridge is **out of scope** for the base library, see RULES.txt #6) |

### 3.7 Entity lists: **out of scope for the base library**

> RULES.txt #6 says extensions must not add new functionality; this belongs in an extra library. In the base library, `List[Plant]` / `List[Zombie]` raise `TypeError`. Kept here as a design sketch only.

`List[Plant]` and `List[Zombie]` as thin wrappers over `List[GameObject]`:

```python
guards = List[Plant]()
guards.Add(plant)                           # PlantToObjectNode + AppendObjectListNode
p, ok = guards.TryGetValue(0)               # GetObjectListItemNode + ObjectToPlantNode
                                            # ok = valid AND still exists
```

This reuses the cast nodes already wrapped. The `存在` flag is what protects against entities that died after being stored. Skip this if you would rather keep `List[GameObject]` explicit.

---

## 4. `Board.Sun` / `Board.Money`: `GetSunNode`, `GetMoneyNode`

```python
Board.Sun.Add(50)         # GetSunNode
Board.Money.Add(100)      # GetMoneyNode
```

⚠️ **The current gap analysis describes these as "alternative sequential getters". Their ports say otherwise.** Both take `触发` + an amount as *inputs* and return only `完成`, the same shape as `UseSunNode` / `UseMoneyNode`. A getter would have the amount as an *output*. This reads as a **"gain sun/money" action** (获得 = obtain). If confirmed in-game:

- `Board.Sun += x` and `Board.Money += x` should lower to this single node instead of a read-modify-write chain, which saves nodes.
- `Add` pairs naturally with the existing `SpendSun` / `SpendMoney`.

---

## 5. `ToolType`: `ToolTypeValueNode`

```python
Tool.Value(ToolType.Shovel)               # explicit ToolTypeValueNode port

# Implicit lowering: any ToolType enum member used where a ToolType port
# is expected emits ToolTypeValueNode automatically (same as PlantType today).
if_shovel = (mouse.Item == ToolType.Shovel)   # CompareToolTypeNode via __eq__
```

`Tool.IsHeld()`, `Tool.GetCooldown()` and `Tool.SetCooldown()` keep working. They just stop being the only users of this node.

---

## 6. Flow Nodes: `DoOnce`, `Pulse`, `WaitUntil`, `RepeatUntil`

The existing guide says these are optimizer-internal because `BoolVar` gating, `Time.OnFixedUpdate` and `While` can replace them. Two of those substitutions are not equivalent (see below), so exposing the nodes is a correctness win, not just coverage. The optimizer can still pattern-match and collapse hand-written gates into them.

### 6.1 `DoOnce`: `DoOnceNode` (`触发`, `重置` → `触发`)

```python
once = DoOnce()
with once:                                  # body runs only on the first pass
    Board.Sun.Add(500)

with Trigger.OnWaveCleared():
    once.Reset()                            # wires the 重置 trigger port
```

One node instead of a `BoolVar` + `Get` + `Branch` + `Set` gate (4 nodes).

### 6.2 `Pulse`: `PulseNode` (`触发`, `状态` → `脉冲触发时`)

```python
pulse = Pulse(state=is_active)              # state is a Bool port
with pulse.OnPulse:
    InGameUI.display_text('pulse!')
```

⚠️ The guide calls this a *periodic* pulse generator, but the node has **no interval input**. Its ports look like an edge/gate detector driven by `状态`. Verify the behaviour in-game before documenting it (see §9). Use `Time.OnFixedUpdate` for periodic work in the meantime.

### 6.3 `Time.WaitUntil`: `WaitUntilNode` (`触发`, `条件`, `间隔秒数`, `最多检查次数` → `完成`, `超时`, `失败`)

```python
with Time.WaitUntil(Board.Sun >= 100, interval=0.5, max_checks=40) as wait:
    InGameUI.display_text('Enough sun!')    # body = 完成, same convention as Time.Wait
    with wait.OnTimeout:
        InGameUI.display_text('Gave up waiting')
    with wait.OnFailed:
        ...
```

### 6.4 `Time.RepeatUntil`: `RepeatUntilNode` (adds `每次循环`)

```python
with Time.RepeatUntil(zombie_count == 0, interval=1.0, max_checks=60) as loop:
    with loop.OnEach:                       # 每次循环, runs every check
        InGameUI.display_text('Still fighting...')
    with loop.OnComplete: ...               # 完成
    with loop.OnTimeout:  ...               # 超时
    with loop.OnFailed:   ...               # 失败
```

⚠️ **`While` is not a substitute for either node.** `While` is a synchronous single-frame loop. `WaitUntil` / `RepeatUntil` poll a condition **over real time** (`间隔秒数`) with a timeout (`最多检查次数`). A `While(cond)` on a condition that only changes in a later frame cannot wait for it. This is the only way to express "wait for X, but give up after N seconds" in the DSL.

The Bool condition is a live data wire and must be re-evaluated on every check. The transpiler must not constant-fold or cache it.

---

## 7. Typed Choice Menus: `TypedChoiceMenuNode`, `TypedChoiceOptionNode`, `TypedChoiceMergeNode`

These three have **identical ports** to `ShowMultipleChoiceMenuNode` / `AddMultipleChoiceOptionNode` / `MergeMultipleChoiceOptionListsNode`. Rather than add new classes, switch the node family on the existing wrapper:

```python
menu = MultiSelectMenu(is_rerollable=True, reroll_count=2, kind=MenuKind.Typed)

@menu.option(title='More sun', description='+500 sun', plant_type=PlantType.SunFlower)
def pick_sun():
    Board.Sun.Add(500)
```

- `MenuKind.Standard` (default): emits the current `*MultipleChoice*` nodes.
- `MenuKind.Typed`: emits `TypedChoiceOption` per option, `TypedChoiceMerge` when merging, `TypedChoiceMenu` for the popup.
- Options always inherit the menu's kind, so users cannot mix families by accident.

The functional difference between the two families is not visible from the ports (see §9).

---

## 8. Deprecated: `GetTravelEntryNode`

```python
@Obsolete("Use Game.GetBuff(); the game replaced travel entries with travel buffs")
Game.GetTravelEntry()                       # emits GetTravelEntryNode (触发 → 完成)
```

Emits the raw node so the base inventory is fully reachable, plus a transpile-time warning. No behaviour is promised.

---

## 9. Verify In-Game Before Implementing

| # | Question | Affects |
| :---: | :--- | :--- |
| 1 | Does `GetSunNode` / `GetMoneyNode` **add** the amount (as the ports suggest)? | §4 and the lowering of `Board.Sun += x` |
| 2 | What exactly does `PulseNode` do with `状态`: rising edge, any change, or "fire while true"? | §6.2 |
| 3 | How do `TypedChoice*` differ from `MultipleChoice*` (UI, reward hooks, return values)? Can their `ChoiceOptions` wires be mixed? | §7 |
| 4 | `Find*ListValueNode`: what is `索引` when the value is absent (`-1`, `0`)? Does `IndexOf` need to guard with `包含`? | §3.3 |
| 5 | `Wait/RepeatUntil`: what does `最多检查次数 = 0` or negative mean (unlimited?), and when does `失败` fire as opposed to `超时`? | §6.3, §6.4 |
| 6 | Does the game type-check `ListVariable` contents at runtime (e.g. `GetIntListItem` on a string list → `有效 = false`)? | Whether `List[T]` is the only guard |
| 7 | Can a stored `GameObject` reference to a dead plant/zombie be cast safely (`存在 = false`) rather than crashing? | §3.7 |

---

## 10. Suggested Implementation Order

| Step | Work | Nodes covered | Cumulative |
| :---: | :--- | :---: | :---: |
| 1 | `List[T]` core: `Add`, indexer, `Count`, `IndexOf`, `Contains`, `RemoveAt`, `Clear`, `TryGetValue` for all 7 types | 31 + 2 | 229 |
| 2 | `Board.Sun.Add` / `Board.Money.Add` (after §9 #1) | 2 | 231 |
| 3 | `ToolType` implicit lowering + `Tool.Value()` | 1 | 232 |
| 4 | `Time.WaitUntil`, `Time.RepeatUntil`, `DoOnce` | 3 | 235 |
| 5 | `Pulse` (after §9 #2) | 1 | 236 |
| 6 | `MenuKind.Typed` (after §9 #3) | 3 | 239 |
| 7 | `[Obsolete] Game.GetTravelEntry()` | 1 | **240** |

---

## Appendix A: Node → API Checklist (all 44)

| # | Original Node | Proposed API |
| :---: | :--- | :--- |
| 1 | `InsertZombieTypeListNode` | `List[ZombieType].Insert(i, x)` |
| 2 | `ReplaceZombieTypeListNode` | `List[ZombieType][i] = x` / `.Replace(i, x)` |
| 3 | `ToolTypeValueNode` | `ToolType.X` (implicit) / `Tool.Value(t)` |
| 4 | `GetSunNode` | `Board.Sun.Add(n)` |
| 5 | `GetMoneyNode` | `Board.Money.Add(n)` |
| 6-11 | `AppendBoolListNode`, `AppendFloatListNode`, `AppendIntListNode`, `AppendStringListNode`, `AppendObjectListNode`, `AppendPlantTypeListNode` | `List[T].Add(x)` |
| 12-17 | `GetBoolListItemNode`, `GetFloatListItemNode`, `GetIntListItemNode`, `GetStringListItemNode`, `GetObjectListItemNode`, `GetPlantTypeListItemNode` | `List[T][i]` / `.TryGetValue(i)` |
| 18-23 | `InsertBoolListNode`, `InsertFloatListNode`, `InsertIntListNode`, `InsertStringListNode`, `InsertObjectListNode`, `InsertPlantTypeListNode` | `List[T].Insert(i, x)` |
| 24-29 | `ReplaceBoolListNode`, `ReplaceFloatListNode`, `ReplaceIntListNode`, `ReplaceStringListNode`, `ReplaceObjectListNode`, `ReplacePlantTypeListNode` | `List[T][i] = x` / `.Replace(i, x)` |
| 30-35 | `FindBoolListValueNode`, `FindFloatListValueNode`, `FindIntListValueNode`, `FindStringListValueNode`, `FindObjectListValueNode`, `FindPlantTypeListValueNode` | `List[T].IndexOf(x)` / `.Contains(x)` / `.TryFindIndex(x)` |
| 36 | `CopyListValuesNode` | `list.CopyTo(dest)` / `list.Clone()` |
| 37 | `DoOnceNode` | `DoOnce()` + `.Reset()` |
| 38 | `PulseNode` | `Pulse(state)` + `.OnPulse` |
| 39 | `RepeatUntilNode` | `Time.RepeatUntil(cond, interval, max_checks)` |
| 40 | `WaitUntilNode` | `Time.WaitUntil(cond, interval, max_checks)` |
| 41 | `TypedChoiceMenuNode` | `MultiSelectMenu(kind=MenuKind.Typed)` |
| 42 | `TypedChoiceOptionNode` | `@menu.option(...)` on a Typed menu |
| 43 | `TypedChoiceMergeNode` | Typed menu's internal option merge |
| 44 | `GetTravelEntryNode` | `[Obsolete] Game.GetTravelEntry()` |

Rows 6-35 expand to 30 nodes, so the list rows plus rows 1-2 and 36 account for the 33 list nodes (31 deferred + 2 in `nodes.py`).
