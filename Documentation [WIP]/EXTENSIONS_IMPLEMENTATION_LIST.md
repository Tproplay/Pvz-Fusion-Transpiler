# 🧩 Transpiler Extensions Implementation Guide & Complete Coverage

This document details all **high-level Extension implementations** in `PvZ_Fusion_Transpiler` (`_Nodes/Extensions/`, `StdLib.py`, `Core/`), showing how they abstract raw IL2CPP nodes into Pythonic DSL syntax.

> [!NOTE]
> **Full Native Node Coverage: 240 / 240 (100%)**
> Every base game Original visual node supported by the PvZ Fusion IL2CPP engine has a corresponding high-level Pythonic extension class or method.

---

## 📦 Extensions Coverage Summary

| Domain / Module | Key Classes | Primary Responsibilities | Original Nodes Wrapped |
| :--- | :--- | :--- | :--- |
| **Generic Collections & Lists** | `List[T]`, `IntList`, `FloatList`, `BoolList`, `StringList`, `ObjectList`, `PlantTypeListVar`, `ZombieTypeList`, `ListOperation`, `ForEach` | Strongly-typed variable lists, index operations, searches, iteration, copying | 35 List & Collection nodes (`Append*`, `Get*Item`, `Insert*`, `Replace*`, `Find*`, `CopyListValues`, `ClearListValues`, `RemoveListItem`, `GetListLength`) |
| **Entity: Plant** | `Plant`, `ForEachPlant`, `ForEachPlantType`, `PlantTypeList` | Plant combat, buffs, status, splitting, layer queries, card pools | 29 PlantFunction & TypeConvert nodes |
| **Entity: Zombie** | `Zombie`, `ForEachZombie`, `ForEachAllZombies`, `ZombieTypeList`, `ForEachZombieType` | Zombie stats, speed, damage, animation, mind control, queries | 21 ZombieFunction & List nodes |
| **Entity: Bullet** | `Bullet`, `SpawnedBullet` | Bullet modification, destruction, damage scaling, redirection | 2 BulletManipulation nodes + `BulletTypeValueNode` |
| **Spawner** | `Spawner.Set_Plant`, `Spawner.Set_Zombie`, `Spawner.Set_Bullet` | Spawning entities with lifecycle context paths (`on_created`, `on_failed`) | `SetPlantNode`, `CreateZombieNode`, `ShootEventBulletNode` |
| **Game & Board** | `Game`, `Board`, `_SunManager`, `_MoneyManager`, `Game.Stage` | Economy management (`Add`, `Spend`, `Use`), wave countdown pause, game win/over, stage change, travel buffs | 12 GeneralFunction, GameFlow & MapFunction nodes (including `GetSunNode`, `GetMoneyNode`, `GetTravelEntryNode`) |
| **Lawn & Map** | `Lawnf` | Area spells, props, explosions, grave, crater, particles, sound | 14 MapFunction & GeneralFunction nodes |
| **Event Triggers** | `Trigger` (18 nested triggers) | Listening to lifecycle, board start, wave milestones, clicks, combat | 16 Trigger nodes |
| **Control Flow & Branching** | `If`, `Switch`, `For`, `While`, `DoOnce`, `Pulse`, `ExecutionPath` | Branching, case cascades, synchronous loops, one-shot gating, periodic pulse | 6 Branching & Loop nodes (`BranchNode`, `MultiBranchNode`, `LoopNode`, `WhileNode`, `DoOnceNode`, `PulseNode`) |
| **Time & Polling** | `Time.Wait`, `Time.WaitUntil`, `Time.RepeatUntil`, `Time.OnFixedUpdate` | Non-blocking execution delays, condition polling loops, timeout branches, game clocks | 5 Time & Counter nodes (`WaitNode`, `WaitUntilNode`, `RepeatUntilNode`, `ToggleCycleNode`, `CounterNode`) |
| **State Variables** | `IntVar`, `FloatVar`, `BoolVar`, `StringVar` | Stateful engine variables with arithmetic operator overloading | 15 Variables nodes |
| **Types & Conversions** | `Int`, `Float`, `String`, `Bool` | Static type casting helpers and constant value constructors | 15 TypeConvert & Constants nodes |
| **Input & Tools** | `Mouse`, `Tool`, `ToolCooldown`, `ToolType` | Mouse click data, tool cooldowns, held tool queries, tool enum literals | 5 Tool & Input nodes (`GetHeldToolNode`, `GetToolCooldownNode`, `SetToolCooldownNode`, `CompareToolTypeNode`, `ToolTypeValueNode`) |
| **World & Objects** | `WorldObject`, `GameObject`, `Vector3`, `ObjectTransform` | Event game object transforms, entity casting, named plant/zombie bindings | 8 World & Object nodes |
| **Math & Logic** | `Math`, `Compare` | Exponential, logarithm, type-aware float/int comparisons, same object | 14 Math & Comparison nodes |
| **UI & Menus** | `MultiSelectMenu`, `Option`, `MenuKind`, `InfoCard`, `InGameUI`, `format_string` | Perk selection popups (Standard & Typed), modal info dialogs, text banners, string formatting | 11 UI & String nodes |
| **Randomization** | `Random`, `Random.Seeded`, `TriggerChance`, `RandomTrigger` | Random numbers, execution path scrambler, deterministic LCG | 3 Randomization nodes |
| **Standard Library** | `Dictionary`, `Array`, `WASDPlant` | High-level data structures and gameplay mechanics in `StdLib.py` | Built on Variables, Branching & Triggers |

---

## 🔍 Detailed Domain Implementation Breakdown

### 1. Generic Collections & Lists (`Variables/list_var.py`, `Entity/zombie_type_list.py`)
*Provides C#-style strongly typed dynamic lists wrapping all native list manipulation nodes with full type inference.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `List[T](name)` | Generic strongly-typed list variable | Parameterized via `List[int]`, `List[float]`, `List[bool]`, `List[str]`, `List[GameObject]`, `List[PlantType]`. Aliases: `IntList`, `FloatList`, `BoolList`, `StringList`, `ObjectList`, `PlantTypeListVar`. | `*VariableNode`, `Append*ListNode`, `Get*ListItemNode`, `Insert*ListNode`, `Replace*ListNode`, `Find*ListValueNode`, `CopyListValuesNode`, `ClearListValuesNode`, `RemoveListItemNode`, `GetListLengthNode` |
| `list.Add(val)` / `list.append(val)` / `list += val` | Appends item to end of list | Returns `ListOperation` with `.Completed` branch | `Append*ListNode` (`AppendIntListNode`, `AppendFloatListNode`, etc.) |
| `list.Insert(index, val)` / `list.insert(...)` | Inserts item at index | Returns `ListOperation` with `.Completed` branch | `Insert*ListNode` (`InsertIntListNode`, `InsertFloatListNode`, etc.) |
| `list.Replace(index, val)` / `list.replace(...)` | Replaces element at index | Returns `ListOperation` with `.Completed` branch | `Replace*ListNode` (`ReplaceIntListNode`, etc.) |
| `list.RemoveAt(index)` / `list.remove_at(...)` | Removes element at index | Returns `ListOperation` with `.Completed` branch | `RemoveListItemNode` |
| `list.Clear()` / `list.clear()` | Removes all elements from list | Clears storage | `ClearListValuesNode` |
| `list.CopyTo(target_list)` | Deep copies all items into target list | Sequential copy operation | `CopyListValuesNode` |
| `list.Clone(new_name)` | Creates new list and copies items into it | Instantiates new list & copies | `CopyListValuesNode` |
| `list.TryGetValue(index)` | Looks up element at index | Single native node returning `(Value, Valid)` ports | `Get*ListItemNode` (`GetIntListItemNode`, etc.) |
| `list.TryFindIndex(value)` | Searches for index of value | Single native node returning `(Index, Found)` ports | `Find*ListValueNode` (`FindIntListValueNode`, etc.) |
| `list.Count` / `list.Length` | Number of elements in list | Returns integer port | `GetListLengthNode` |
| `list.Contains(value)` | Tests if value is present in list | Returns boolean condition port | `Find*ListValueNode` |
| `list.ForEach() as (item, index)` | Iterates list items | Context manager with `.OnComplete` exit branch | `GetListLengthNode`, `LoopNode`, `Get*ListItemNode` |
| `ZombieTypeList([types])` | Specialized zombie type list | Inherits from `List[ZombieType]`, supporting all list operations | `*ZombieTypeListNode`, `RemoveListItemNode`, `ClearListValuesNode` |

### 2. Entity Manipulation (`Entity/`)
*Wraps game entities (`Plant`, `Zombie`, `Bullet`) to enforce encapsulation and type safety without leaking raw node ports.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Plant(ref)` | Entity wrapper for plant pointers | Exposes `.heal(amount)`, `.damage(amount)`, `.curse(duration)`, `.silence(duration)`, `.feed_golden_bean()`, `.upgrade()`, `.try_super_skill()`, `.add_shield(amount)`, `.modify_health(mult)`, `.modify_attack(mult)`, `.set_attack_speed(speed)`, `.set_attack_interval(interval)`, `.get_components()`, `.get_attribute_countdown()`, `.split()`, `.die(reason)` | `CursePlantNode, DamagePlantNode, DiePlantNode, FeedGoldenBeanNode, GetPlantAttackSpeedNode, GetPlantAttributeCountdownNode, GetPlantBasicComponentsNode, GivePlantShieldNode, HealPlantNode, ModifyPlantAttackNode, ModifyPlantHealthNode, MovePlantNode, PlantSplitNode, SetPlantAttackIntervalNode, SetPlantAttackSpeedNode, SetPlantAttributeCountdownNode, SilencePlantNode, TryPlantSuperSkillNode, UpgradeEventPlantNode` |
| `Zombie(ref)` | Entity wrapper for zombie pointers | Exposes `.damage(amount)`, `.modify_health(mult)`, `.set_hp(hp)`, `.set_speed(speed)`, `.set_size(size)`, `.set_attack_power(power)`, `.get_stats(stat=EventZombieStat.Hp)` (`GetZombieStatsNode`), `.set_stats(stat, val)` (`SetZombieStatsNode`), `.get_status(status=EventZombieStatus.Freeze)` (`GetZombieStatusNode`), `.set_status(status, val)` (`SetZombieStatusNode`), `.hypnotize()` (`SetZombieMindControlledNode`), `.move(row, col)` (`MoveZombieNode`), `.play_animation(name)` (`PlayZombieAnimNode`), `.split()` (`ZombieSplitNode`). Live properties: `.hp`, `.max_hp`, `.speed`, `.size`, `.attack_power`, `.armor1_hp`, `.armor2_hp`. | `DamageZombieNode, GetZombieStatsNode, GetZombieStatusNode, ModifyZombieHealthNode, MoveZombieNode, PlayZombieAnimNode, SetZombieMindControlledNode, SetZombieStatsNode, SetZombieStatusNode, ZombieSplitNode` |
| `Bullet(ref)` | Entity wrapper for projectile pointers | Exposes `.destroy()`, `.modify(value, property=EventBulletProperty.Speed)`, `.set_speed(speed)`, `.set_damage(damage)`, `.set_scale(scale)`, `.set_direction(direction)` | `ModifyEventBulletNode` |
| `ForEachPlant(list_port)` | Context manager looping over plant entity list | Iterates live plant entities; loop variable acts as transparent `Plant` proxy. Has `.on_complete` branch. | `ForEachPlantNode` |
| `ForEachZombie(list_port)` | Context manager looping over zombie entity list | Iterates live zombie entities; loop variable acts as transparent `Zombie` proxy. Has `.on_complete` branch. | `ForEachZombieNode` |
| `ForEachAllZombies()` | Context manager looping over ALL living zombies on lawn | Loops over every zombie on the board without querying first. | `ForEachAllZombiesNode` |
| `PlantTypeList([types])` | Dynamic plant type collection on node canvas | Supports `+=`, `-=`, `.contains(type)`, `.get_random()`, `.for_each()` | `SinglePlantTypeListNode, MultiPlantTypeListNode, MergePlantTypeListsNode, RemovePlantTypeNode, GetRandomPlantTypeNode, ForEachPlantTypeNode, PlantTypeListStorageNode` |

### 3. Spawning Entities (`Spawner/`)
*Constructs new entities at runtime with dedicated execution branches for placement success and failure.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Spawner.Set_Plant(row, col, plant_type, force=False)` | Spawns plant and returns `SpawnedPlant` | Can be used as context manager `with Spawner.Set_Plant(...) as plant:`. Exposes `.on_created` (alias `.on_success`) and `.on_failed` branches. Enforces strict `PlantType` enum. | `SetPlantNode, PlantTypeValueNode` |
| `Spawner.Set_Zombie(row, col, zombie_type, mind_controlled=False)` | Spawns zombie and returns `SpawnedZombie` | Can be used as context manager `with Spawner.Set_Zombie(...) as zombie:`. Exposes `.on_created` branch. Enforces strict `ZombieType` enum. | `CreateZombieNode, ZombieTypeValueNode` |
| `Spawner.Set_Bullet(row, col, bullet_type, damage, speed, angle, ...)` | Fires event bullet and returns `SpawnedBullet` | Can be used as context manager `with Spawner.Set_Bullet(...) as bullet:`. Exposes `.on_created` and `.on_failed` branches. Enforces strict `BulletType` enum. | `ShootEventBulletNode, BulletTypeValueNode` |

### 4. Game Economy & Stage Management (`Game/`)
*Direct access to level Sun, Money, wave counters, stage transitions, travel entries, and victory conditions.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Board.Sun / Game.Sun` | Sun balance property manager | Supports `+=`, `-=`, `*=`, `/=`, `= DirectValue`, conditions (`<`, `>`, `==`), and `with Board.Sun.SpendSun(cost) as tx: ... with tx.Failed: ...` | `GetSunAmountNode, UseSunNode, AddNode, SubtractNode, MultiplyNode, DivideNode, IntToFloatNode` |
| `Board.Sun.Add(amount)` | Sequential sun grant | Emits native sequential `GetSunNode` to award sun directly into game pool | `GetSunNode` |
| `Board.Money / Game.Money` | Coin balance property manager | Supports `+=`, `-=`, and `with Board.Money.SpendMoney(cost) as tx: ... with tx.Failed: ...`, plus `Board.Money.check_money(cost, on_true, on_false)` | `GetMoneyAmountNode, UseMoneyNode, IntAddNode, IntSubtractNode` |
| `Board.Money.Add(amount)` | Sequential money grant | Emits native sequential `GetMoneyNode` to award money directly into game pool | `GetMoneyNode` |
| `Board.Wave` | Current active wave index port | Read-only integer output port | `OnWaveNode` |
| `Game.pause_wave_timer(paused=True)` | Pauses/resumes automatic wave countdown | Emits pause toggle node | `SetWaveCountdownPausedNode` |
| `Game.Stage.change(stage_name='战斗')` | Transitions level to named stage | Emits stage transition node with custom stageName string | `ChangeStageNode` |
| `Game.Stage.get_current()` | Returns current stage name string port | Query stage name | `GetStageNode` |
| `Game.trigger_game_win()` | Instant victory trigger | Ends level in victory | `GameWinNode` |
| `Game.trigger_game_over(reason='Defeated!')` | Instant defeat trigger | Ends level in defeat with message | `GameOverNode` |
| `Game.get_buff(buff_enum)` | Grants travel buff to player | Accepts AdvBuff, UltiBuff, TravelDebuff, or TravelBuffType | `GetTravelBuffNode` |
| `Game.GetTravelEntry()` / `Lawnf.GetTravelEntry()` | Obsolete travel entry getter | Issues `DeprecationWarning`; returns entry port | `GetTravelEntryNode` |

### 5. Lawn & Board Props (`Lawn/`)
*Cosmetic props, area spells, explosive effects, audio triggers, and board-level plant/zombie queries.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Lawnf.spawn_grave(row, col)` | Spawns gravestone prop | Places grave tile | `CreateGraveNode` |
| `Lawnf.spawn_crater(row, col)` | Spawns explosion crater prop | Places crater tile | `CreateCraterNode` |
| `Lawnf.spawn_ladder(row, col)` | Spawns pool ladder prop | Places pool ladder | `CreateLadderNode` |
| `Lawnf.spawn_particle(row, col)` | Spawns decorative particle | Emits visual particle effect | `CreateParticleNode` |
| `Lawnf.spawn_ice_block(row, col, plant_type=-1)` | Spawns ice block prop encasing optional plant | Places frozen ice block | `CreateIceBlockNode` |
| `Lawnf.trigger_cherry_explosion(row, col, damage=1800)` | Cherry Bomb area blast | Deals explosion damage | `CreateCherryExplodeNode` |
| `Lawnf.trigger_doom_explosion(row, col, damage=1800, create_pit=True)` | Doom-shroom nuclear blast | Deals massive damage, leaves crater | `CreateDoomShroomEffectNode` |
| `Lawnf.trigger_jalapeno(row, damage=1800)` | Jalapeno lane inferno | Deals row-wide fire damage | `CreateJalapenoEffectNode` |
| `Lawnf.trigger_ice_shroom(duration=5.0)` | Ice-shroom full-screen freeze | Freezes all zombies | `CreateIceShroomEffectNode` |
| `Lawnf.trigger_zombie_explosion(row, col)` | Zombie gib explosion visual | Decorative zombie explode | `CreateZombieExplodeNode` |
| `Lawnf.play_sound(sound_type)` | Plays audio sound clip | Accepts SoundType enum | `PlaySoundNode` |
| `Lawnf.get_closest_zombie(row, col)` | Finds nearest zombie to tile | Returns wrapped Zombie | `GetNearestZombieNode` |
| `Lawnf.get_plants_at(row, col)` | Returns list port of plants in grid cell | Query plants in cell | `GetPlantsInCellNode` |
| `Lawnf.get_all_plants()` | Returns list port of all living plants | Query all plants | `GetAllPlantsNode` |
| `Lawnf.for_each_plant_on_lawn()` | Context manager looping over all plants on board | Convenience iterator | `GetAllPlantsNode, ForEachPlantNode` |
| `Lawnf.delete_grid_items(row, col, kind=EventGridObstacle.All)` | Clears grid item props at tile | Removes graves/ladders/craters/all | `DeleteGridItemsNode` |
| `Lawnf.change_map(scene=SceneType.Day)` | Changes visual event map background | Map change (typed `SceneType`, alias `change_event_map`) | `ChangeEventMapNode` |
| `Lawnf.change_music(music=MusicType.Day)` | Changes active background music | BGM change (typed `MusicType`, alias `change_event_music`) | `ChangeEventMusicNode` |
| `Lawnf.remove_travel_entry(name_or_id, kind=EventTravelEntryKind.All)` | Removes travel/rogue entry by name/ID | Travel entry removal (typed `EventTravelEntryKind`) | `RemoveTravelEntryNode` |
| `Lawnf.set_zombie_house_rule(rule_id)` | Sets zombie house rules | Custom gameplay rule | `SetZombieHouseRuleNode` |

### 6. Event Triggers (`Triggers/`)
*Context managers that capture event execution streams and auto-wire sequential triggers.*

| Interface / Method | Event Description | Output Arguments / Injected Objects | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Trigger.OnGameStart` | Level initialization | None | `OnGameStartNode` |
| `Trigger.OnBoardStart` | Active board startup | None | `OnBoardStartNode` |
| `Trigger.OnWave` | Wave milestones | `wave_index` | `OnWaveNode` |
| `Trigger.OnPlantCreate` | Plant placement | `plant` (`Plant` wrapper) | `OnPlantCreateNode` |
| `Trigger.OnPlantDie` | Plant death | `plant` (`Plant` wrapper) | `OnPlantDieNode` |
| `Trigger.OnZombieSpawn` | Zombie arrival | `zombie` (`Zombie` wrapper) | `OnZombieSpawnNode` |
| `Trigger.OnZombieDie` | Zombie defeat | `zombie` (`Zombie` wrapper) | `OnZombieDieNode` |
| `Trigger.OnStageEnter` | Stage transition | `stage_name` | `OnStageEnterNode` |
| `Trigger.OnPlantMixed` | Plant fusion | `plant` (`Plant` wrapper) | `OnPlantMixedNode` |
| `Trigger.OnWorldPlantEffect(effect=EventWorldEffect.Explode)` | World-wide plant effect | `lane` (Row index integer port) | `OnWorldPlantEffectNode` |
| `Trigger.OnZombieClick` | Player clicks zombie | `zombie` (`Zombie` wrapper) | `OnZombieClickNode` |
| `Trigger.OnCustomKey` | Custom keyboard input | `key` | `OnKeyPressNode` |
| `Trigger.OnMouseClick` | Mouse click on board | `x`, `y` coordinates | `OnMouseClickNode` |
| `Trigger.OnCardClick` | Seed card clicked in bar | `card_index` | `OnCardClickNode` |
| `Trigger.OnBulletCreate` | Projectile fired | `bullet` (`Bullet` wrapper) | `OnBulletCreateNode` |
| `Trigger.OnBulletHit` | Projectile impacts target | `bullet`, `zombie` | `OnBulletHitNode` |
| `Trigger.OnCustomEvent` | User-defined event signal | `event_name` | `OnCustomEventNode` |

### 7. Control Flow & Branching (`Branching/`, `Loops/`)
*Structured execution branching, multi-case matching, single-frame loops, and execution guards.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `If(condition)` | Boolean conditional branch | Supports `.ElseIf(cond)`, `.Else`, and `with If(cond):` | `BranchNode` |
| `Switch(target)` | Multi-way value branching | Supports `.Case(val)`, `.Default`, and chained case matching | `MultiBranchNode` |
| `For(count)` | Fixed-count synchronous loop | Loop variable yields current integer iteration port. Has `.OnComplete` exit branch. | `LoopNode` |
| `While(condition)` | Condition-based synchronous loop | Repeats within frame until condition is false. Has `.OnComplete` exit branch. | `WhileNode` |
| `DoOnce(name=None)` | Executes nested block exactly once | Can be used as context manager `with DoOnce():` or via `do = DoOnce(); with do.OnExecute:` | `DoOnceNode` |
| `Pulse(interval)` | Periodic execution pulse generator | Supports context manager `with Pulse(0.5):` or via `p = Pulse(0.5); with p.OnPulse:` | `PulseNode` |

### 8. Time & Delays (`Time/`)
*Asynchronous delays, real-time polling loops, timeout exits, and elapsed clocks.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Time.Wait(duration)` | Context manager delaying nested execution | Non-blocking game delay | `WaitNode` |
| `Time.WaitUntil(condition, interval=0.1, max_checks=100)` | Polls condition across frames until true | Context manager with `.OnComplete`, `.OnTimeout`, and `.OnFailed` branches | `WaitUntilNode` |
| `Time.RepeatUntil(condition, interval=0.1, max_checks=100)` | Recurring execution until condition becomes true | Context manager with `.OnEach`, `.OnComplete`, `.OnTimeout`, and `.OnFailed` branches | `RepeatUntilNode` |
| `Time.OnFixedUpdate(interval=0.1) as update` | Recurring execution loop | Provides `update.tick`, `.toggle()`, `.on_enable`, `.on_disable`, `.on_cycle` | `ToggleCycleNode, CounterNode` |
| `Time.time_since_start` | Seconds elapsed since board initialization | Float output port | `FloatVariableNode, ToggleCycleNode` |
| `Time.time_since_game_start` | Seconds elapsed since active gameplay began | Float output port | `FloatVariableNode, ToggleCycleNode` |

### 9. State Variables (`Variables/`)
*Engine variables persisted across frames with arithmetic operator overloading.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `IntVar(name, initial=0)` | Integer state variable | Supports `+=`, `-=`, `*=`, `/=`, `%=`, `= DirectValue`, conditions (`<`, `>`, `==`, `!=`) | `IntVariableNode, AddNode, SubtractNode, MultiplyNode, DivideNode, IntModuloNode, CompareIntNode` |
| `FloatVar(name, initial=0.0)` | Floating-point state variable | Supports `+=`, `-=`, `*=`, `/=`, `= DirectValue`, conditions (`<`, `>`, `==`, `!=`) | `FloatVariableNode, AddNode, SubtractNode, MultiplyNode, DivideNode, CompareFloatNode` |
| `BoolVar(name, initial=False)` | Boolean flag variable | Supports `= True/False`, `.toggle()`, `if var:` conditions | `BoolVariableNode` |
| `StringVar(name, initial="")` | String state variable | Supports `= "text"`, `.set(val)` | `StringVariableNode` |

### 10. Types & Conversions (`Types/`)
*Explicit type conversions, string formatting, and constant constructors.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Int(val)` | Converts port to integer | Truncates float or converts string | `FloatToIntNode, StringToIntNode, IntToFloatNode` |
| `Float(val)` | Converts port to float | Converts int or string to float | `IntToFloatNode, StringToFloatNode` |
| `String(val)` | Converts port to string | Converts int/float/bool to string | `IntToStringNode, FloatToStringNode, BoolToStringNode` |
| `Bool(val)` | Converts port to boolean | Converts numeric port to boolean | `IntToBoolNode` |

### 11. Input & Tools (`Input/`)
*Mouse position queries, tool selection, cooldowns, and tool enum literals.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Mouse.get_position()` | Reads active cursor coordinates | Returns `(x, y)` float ports | `GetMousePositionNode` |
| `Tool.is_held(tool_type)` | Tests if player currently holds tool | Returns boolean condition port | `GetHeldToolNode, CompareToolTypeNode, ToolTypeValueNode` |
| `Tool.get_cooldown(tool_type)` | Reads cooldown remaining on tool | Returns float port | `GetToolCooldownNode, ToolTypeValueNode` |
| `Tool.set_cooldown(tool_type, seconds)` | Sets cooldown on tool | Emits cooldown update node | `SetToolCooldownNode, ToolTypeValueNode` |
| `Tool.Value(tool_type)` | Emits constant tool type port | Parameterized by `ToolType` enum with Chinese aliases (`ToolType.铲子`, `ToolType.锤子`, etc.) | `ToolTypeValueNode` |

### 12. World & Game Objects (`World/`)
*Event objects, hierarchy queries, and transform manipulations.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `WorldObject.create(prefab_name, position)` | Spawns visual game object | Returns wrapped `WorldObject` | `CreateEventObjectNode` |
| `WorldObject.destroy(obj)` | Destroys event object | Cleans up object | `DestroyEventObjectNode` |
| `WorldObject.get_transform(obj)` | Reads object transform | Returns position/rotation/scale | `GetObjectTransformNode` |
| `WorldObject.bind_plant(obj, plant)` | Attaches object to plant | Parent-child link | `BindPlantNode` |
| `WorldObject.bind_zombie(obj, zombie)` | Attaches object to zombie | Parent-child link | `BindZombieNode` |
| `WorldObject.to_plant(obj)` | Casts object to plant wrapper | Returns `Plant` | `ObjectToPlantNode` |
| `WorldObject.to_zombie(obj)` | Casts object to zombie wrapper | Returns `Zombie` | `ObjectToZombieNode` |
| `Vector3(x, y, z)` | 3D coordinate vector | Used for object positions | `Vector3ValueNode` |

### 13. Math & Logic (`Math/`)
*Mathematical functions and safe comparison helpers.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Math.power(base, exponent)` | Exponential calculation | Computes $base^{exponent}$ | `PowerNode` |
| `Math.log(value, base)` | Logarithm calculation | Computes $\log_{base}(value)$ | `LogarithmNode` |
| `Compare.equal(a, b)` | Equality check | Type-aware equality | `CompareIntNode, CompareFloatNode, CompareGameObjectNode` |
| `Compare.greater(a, b)` | Greater than | Strict inequality | `CompareIntNode, CompareFloatNode` |
| `Compare.less(a, b)` | Less than | Strict inequality | `CompareIntNode, CompareFloatNode` |

### 14. UI & Menus (`UI/`)
*Perk selection dialogs (both Standard and Typed), info popups, and HUD banners.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `InGameUI.show_banner(text, duration)` | Displays floating banner | On-screen message | `InGameUINode` |
| `InGameUI.InfoCard(title, subtitle)` | Context manager for modal info card | Card dismissal block | `CreateInfoCardNode` |
| `InGameUI.close_all_info_cards()` | Closes all active info cards | Dismisses cards | `DeleteInfoCardsNode` |
| `MultiSelectMenu(..., kind=MenuKind.Standard)` | Standard perk selection popup | Supports `@menu.option(...)` and `menu.add_option(Option(...))`; hooks `menu.Output.OnExit` and `menu.Output.OnRefresh` | `ShowMultipleChoiceMenuNode, AddMultipleChoiceOptionNode, MergeMultipleChoiceOptionListsNode` |
| `MultiSelectMenu(..., kind=MenuKind.Typed)` | Typed perk selection popup | Uses engine's typed choice nodes for alternative UI layouts | `TypedChoiceMenuNode, TypedChoiceOptionNode, TypedChoiceMergeNode` |
| `format_string(*args)` | Chained string concatenation helper | Merges mixed ports into single string port | `StringConcatNode` |

### 15. Randomization (`Random/`)
*Random values, path scrambling, and seeded LCG.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Random.randint(min, max)` | Random integer in [min, max] | Returns integer output port | `RandomIntNode` |
| `Random.randf(min, max)` | Random float in [min, max] | Returns float output port | `RandomFloatNode` |
| `Random.value` | Normalized random float in [0.0, 1.0] | Returns float output port | `RandomFloatNode` |
| `Random.TriggerChance(probability)` | Context manager gating execution by probability | Rolls float check | `RandomFloatNode, CompareFloatNode, BranchNode` |
| `Random.RandomTrigger(count=1)` | Context manager randomly picking child paths | Path scrambler | `RandomTriggerNode` |
| `Random.Seeded(seed, name)` | Deterministic Linear Congruential Generator | Guaranteed reproducible sequence using node math | `IntVariableNode, MultiplyNode, AddNode, IntModuloNode` |

### 16. Standard Library (`StdLib.py`)
*Higher-level utility collections and player control abstractions.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Dictionary(schema)` | Virtual string-keyed dictionary of stateful variables | Supports reading/writing using dot-notation or brackets | `IntVar, FloatVar, BoolVar` |
| `Array(size, default_val)` | Virtual fixed-size array supporting port-based index access | Supports `.read(index_port, callback)` and `.write(index_port, value)` | `IntVar, FloatVar, BoolVar, BranchNode` |
| `WASDPlant(plant)` | Maps keyboard W, A, S, D keys to relative plant motion | Binds arrow listeners to `plant.move_relative()` | `OnKeyPressNode, MovePlantNode` |

---

## 🎯 100% Coverage Alignment Matrix (All 44 Gap Nodes Resolved)

The table below documents how all 44 previously unextended base game nodes are integrated into the high-level Pythonic API:

| Original Base Game Node | Extension Interface / Method | Module Location |
| :--- | :--- | :--- |
| `AppendBoolListNode` | `BoolList.Add(val)` / `BoolList.append(val)` / `BoolList += val` | `_Nodes/Extensions/Variables/list_var.py` |
| `AppendFloatListNode` | `FloatList.Add(val)` / `FloatList.append(val)` / `FloatList += val` | `_Nodes/Extensions/Variables/list_var.py` |
| `AppendIntListNode` | `IntList.Add(val)` / `IntList.append(val)` / `IntList += val` | `_Nodes/Extensions/Variables/list_var.py` |
| `AppendObjectListNode` | `ObjectList.Add(val)` / `ObjectList.append(val)` / `ObjectList += val` | `_Nodes/Extensions/Variables/list_var.py` |
| `AppendPlantTypeListNode` | `PlantTypeListVar.Add(val)` / `PlantTypeListVar += val` | `_Nodes/Extensions/Variables/list_var.py` |
| `AppendStringListNode` | `StringList.Add(val)` / `StringList.append(val)` / `StringList += val` | `_Nodes/Extensions/Variables/list_var.py` |
| `AppendZombieTypeListNode` | `ZombieTypeList.Add(val)` / `ZombieTypeList.append(val)` / `ZombieTypeList += val` | `_Nodes/Extensions/Entity/zombie_type_list.py` |
| `GetBoolListItemNode` | `BoolList.TryGetValue(index)` / `BoolList.get_item(index)` | `_Nodes/Extensions/Variables/list_var.py` |
| `GetFloatListItemNode` | `FloatList.TryGetValue(index)` / `FloatList.get_item(index)` | `_Nodes/Extensions/Variables/list_var.py` |
| `GetIntListItemNode` | `IntList.TryGetValue(index)` / `IntList.get_item(index)` | `_Nodes/Extensions/Variables/list_var.py` |
| `GetObjectListItemNode` | `ObjectList.TryGetValue(index)` / `ObjectList.get_item(index)` | `_Nodes/Extensions/Variables/list_var.py` |
| `GetPlantTypeListItemNode` | `PlantTypeListVar.TryGetValue(index)` / `PlantTypeListVar.get_item(index)` | `_Nodes/Extensions/Variables/list_var.py` |
| `GetStringListItemNode` | `StringList.TryGetValue(index)` / `StringList.get_item(index)` | `_Nodes/Extensions/Variables/list_var.py` |
| `GetZombieTypeListItemNode` | `ZombieTypeList.TryGetValue(index)` / `ZombieTypeList.get_item(index)` | `_Nodes/Extensions/Entity/zombie_type_list.py` |
| `InsertBoolListNode` | `BoolList.Insert(index, val)` / `BoolList.insert(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `InsertFloatListNode` | `FloatList.Insert(index, val)` / `FloatList.insert(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `InsertIntListNode` | `IntList.Insert(index, val)` / `IntList.insert(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `InsertObjectListNode` | `ObjectList.Insert(index, val)` / `ObjectList.insert(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `InsertPlantTypeListNode` | `PlantTypeListVar.Insert(index, val)` / `PlantTypeListVar.insert(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `InsertStringListNode` | `StringList.Insert(index, val)` / `StringList.insert(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `InsertZombieTypeListNode` | `ZombieTypeList.Insert(index, val)` / `ZombieTypeList.insert(index, val)` | `_Nodes/Extensions/Entity/zombie_type_list.py` |
| `ReplaceBoolListNode` | `BoolList.Replace(index, val)` / `BoolList.replace(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `ReplaceFloatListNode` | `FloatList.Replace(index, val)` / `FloatList.replace(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `ReplaceIntListNode` | `IntList.Replace(index, val)` / `IntList.replace(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `ReplaceObjectListNode` | `ObjectList.Replace(index, val)` / `ObjectList.replace(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `ReplacePlantTypeListNode` | `PlantTypeListVar.Replace(index, val)` / `PlantTypeListVar.replace(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `ReplaceStringListNode` | `StringList.Replace(index, val)` / `StringList.replace(index, val)` | `_Nodes/Extensions/Variables/list_var.py` |
| `ReplaceZombieTypeListNode` | `ZombieTypeList.Replace(index, val)` / `ZombieTypeList.replace(index, val)` | `_Nodes/Extensions/Entity/zombie_type_list.py` |
| `FindBoolListValueNode` | `BoolList.TryFindIndex(value)` / `BoolList.find_index(value)` | `_Nodes/Extensions/Variables/list_var.py` |
| `FindFloatListValueNode` | `FloatList.TryFindIndex(value)` / `FloatList.find_index(value)` | `_Nodes/Extensions/Variables/list_var.py` |
| `FindIntListValueNode` | `IntList.TryFindIndex(value)` / `IntList.find_index(value)` | `_Nodes/Extensions/Variables/list_var.py` |
| `FindObjectListValueNode` | `ObjectList.TryFindIndex(value)` / `ObjectList.find_index(value)` | `_Nodes/Extensions/Variables/list_var.py` |
| `FindPlantTypeListValueNode` | `PlantTypeListVar.TryFindIndex(value)` / `PlantTypeListVar.find_index(value)` | `_Nodes/Extensions/Variables/list_var.py` |
| `FindStringListValueNode` | `StringList.TryFindIndex(value)` / `StringList.find_index(value)` | `_Nodes/Extensions/Variables/list_var.py` |
| `FindZombieTypeListValueNode` | `ZombieTypeList.TryFindIndex(value)` / `ZombieTypeList.find_index(value)` | `_Nodes/Extensions/Entity/zombie_type_list.py` |
| `CopyListValuesNode` | `list.CopyTo(target)` / `list.Clone(name)` | `_Nodes/Extensions/Variables/list_var.py` |
| `GetSunNode` | `Board.Sun.Add(amount)` / `Board.Sun += amount` / `Board.Sun.Spend(...)` | `_Nodes/Extensions/Game/sun.py` |
| `GetMoneyNode` | `Board.Money.Add(amount)` / `Board.Money += amount` / `Board.Money.Spend(...)` | `_Nodes/Extensions/Game/money.py` |
| `ToolTypeValueNode` | `Tool.Value(tool_type)` / automatic `to_port` coercion of `ToolType` | `_Nodes/Extensions/Input/tool.py`, `port_types.py` |
| `DoOnceNode` | `DoOnce(name)` / `with DoOnce():` / `with do.OnExecute:` | `_Nodes/Extensions/Branching/do_once.py` |
| `PulseNode` | `Pulse(interval)` / `with Pulse(0.5):` / `with p.OnPulse:` | `_Nodes/Extensions/Branching/pulse.py` |
| `WaitUntilNode` | `Time.WaitUntil(condition, interval, max_checks)` (.OnComplete, .OnTimeout, .OnFailed) | `_Nodes/Extensions/Time/time_ext.py` |
| `RepeatUntilNode` | `Time.RepeatUntil(condition, interval, max_checks)` (.OnEach, .OnComplete, .OnTimeout, .OnFailed) | `_Nodes/Extensions/Time/time_ext.py` |
| `TypedChoiceMenuNode` | `MultiSelectMenu(..., kind=MenuKind.Typed)` | `_Nodes/Extensions/UI/menu.py` |
| `TypedChoiceOptionNode` | `MultiSelectMenu(..., kind=MenuKind.Typed).option(...)` | `_Nodes/Extensions/UI/menu.py` |
| `TypedChoiceMergeNode` | `MultiSelectMenu(..., kind=MenuKind.Typed)` (internal option merge) | `_Nodes/Extensions/UI/menu.py` |
| `GetTravelEntryNode` | `Game.GetTravelEntry()` / `Lawnf.GetTravelEntry()` (with `DeprecationWarning`) | `_Nodes/Extensions/Game/game.py`, `_Nodes/Extensions/Lawn/lawnf.py` |
