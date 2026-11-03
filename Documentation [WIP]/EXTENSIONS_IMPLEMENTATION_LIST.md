# 🧩 Transpiler Extensions Implementation Guide & Gaps

This document details all **high-level Extension implementations** currently available in `PvZ_Fusion_Transpiler` (`_Nodes/Extentions/`, `StdLib.py`, `Core/`), showing how they abstract raw IL2CPP nodes into Pythonic DSL syntax, and provides a **Gap Analysis** of unextended nodes to guide future extension alignment.

---

## 📦 Extensions Coverage Summary

| Domain / Module | Key Classes | Primary Responsibilities | Original Nodes Wrapped |
| :--- | :--- | :--- | :--- |
| **Entity: Plant** | `Plant`, `ForEachPlant`, `ForEachPlantType`, `PlantTypeList` | Plant combat, buffs, status, splitting, layer queries, card pools | 29 PlantFunction & TypeConvert nodes |
| **Entity: Zombie** | `Zombie`, `ForEachZombie`, `ForEachAllZombies`, `ZombieTypeList`, `ForEachZombieType` | Zombie stats, speed, damage, animation, mind control, queries | 19 ZombieFunction & List nodes |
| **Entity: Bullet** | `Bullet`, `SpawnedBullet` | Bullet modification, destruction, damage scaling, redirection | 2 BulletManipulation nodes |
| **Spawner** | `Spawner.Set_Plant`, `Spawner.Set_Zombie`, `Spawner.Set_Bullet` | Spawning entities with lifecycle context paths (`on_created`, `on_failed`) | `SetPlantNode`, `CreateZombieNode`, `ShootEventBulletNode` |
| **Game & Board** | `Game`, `Board`, `_SunManager`, `_MoneyManager`, `Game.Stage` | Economy management, wave countdown pause, game win/over, stage change | 10 GeneralFunction, GameFlow & MapFunction nodes |
| **Lawn & Map** | `Lawnf` | Area spells, props, explosions, grave, crater, particles, sound | 14 MapFunction & GeneralFunction nodes |
| **Event Triggers** | `Trigger` (18 nested triggers) | Listening to lifecycle, board start, wave milestones, clicks, combat | 16 Trigger nodes |
| **Control Flow** | `If`, `Switch`, `For`, `While`, `ExecutionPath` | Branching, case cascades, synchronous single-frame loops | `BranchNode`, `MultiBranchNode`, `LoopNode`, `WhileNode` |
| **State Variables** | `IntVar`, `FloatVar`, `BoolVar`, `StringVar` | Stateful engine variables with arithmetic operator overloading | 15 Variables nodes |
| **Types & Conversions** | `Int`, `Float`, `String`, `Bool` | Static type casting helpers and constant value constructors | 15 TypeConvert & Constants nodes |
| **Input & Tools** | `Mouse`, `Tool`, `ToolCooldown` | Mouse click data, tool cooldowns, query currently held tool | `GetHeldToolNode`, `GetToolCooldownNode`, `SetToolCooldownNode`, `CompareToolTypeNode` |
| **World & Objects** | `WorldObject`, `GameObject`, `Vector3`, `ObjectTransform` | Event game object transforms, entity casting, named plant/zombie bindings | `CreateEventObjectNode`, `BindPlantNode`, `BindZombieNode`, `ObjectToPlantNode`, etc. |
| **Math & Logic** | `Math`, `Compare` | Exponential, logarithm, type-aware float/int comparisons, same object | `PowerNode`, `LogarithmNode`, `CompareIntNode`, `CompareFloatNode`, etc. |
| **UI & Menus** | `MultiSelectMenu`, `Option`, `InfoCard`, `InGameUI`, `format_string` | Perk selection popups, modal info dialogs, text banners, string formatting | 8 GeneralFunction & UI nodes |
| **Randomization** | `Random`, `Random.Seeded`, `TriggerChance`, `RandomTrigger` | Random numbers, execution path scrambler, deterministic LCG | `RandomIntNode`, `RandomFloatNode`, `RandomTriggerNode` |
| **Time & Delays** | `Time.Wait`, `Time.OnFixedUpdate`, `Time.time_since_start` | Non-blocking execution delays, high-frequency update loops, game clocks | `WaitNode`, `ToggleCycleNode`, `CounterNode` |
| **Standard Library** | `Dictionary`, `Array`, `WASDPlant` | High-level data structures and gameplay mechanics in `StdLib.py` | Built on Variables, Branching & Triggers |

---

## 🔍 Detailed Domain Implementation Breakdown

### 1. Entity Manipulation (`Entity/`)
*Wraps game entities (`Plant`, `Zombie`, `Bullet`) to enforce encapsulation and type safety without leaking raw node ports.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Plant(ref)` | Entity wrapper for plant pointers | Exposes `.heal(amount)`, `.damage(amount)`, `.curse(duration)`, `.silence(duration)`, `.feed_golden_bean()`, `.upgrade()`, `.try_super_skill()`, `.add_shield(amount)`, `.modify_health(mult)`, `.modify_attack(mult)`, `.set_attack_speed(speed)`, `.set_attack_interval(interval)`, `.get_components()`, `.get_attribute_countdown()`, `.split()`, `.die(reason)` | `CursePlantNode, DamagePlantNode, DiePlantNode, FeedGoldenBeanNode, GetPlantAttackSpeedNode, GetPlantAttributeCountdownNode, GetPlantBasicComponentsNode, GivePlantShieldNode, HealPlantNode, ModifyPlantAttackNode, ModifyPlantHealthNode, MovePlantNode, PlantSplitNode, SetPlantAttackIntervalNode, SetPlantAttackSpeedNode, SetPlantAttributeCountdownNode, SilencePlantNode, TryPlantSuperSkillNode, UpgradeEventPlantNode` |
| `Zombie(ref)` | Entity wrapper for zombie pointers | Exposes `.damage(amount)`, `.modify_health(mult)`, `.set_stats(hp, speed, ...)` (`SetZombieStatsNode`), `.get_stats()` (`GetZombieStatsNode`), `.set_status(flag, ...)` (`SetZombieStatusNode`), `.get_status()` (`GetZombieStatusNode`), `.hypnotize()` (`SetZombieMindControlledNode`), `.move(row, col)` (`MoveZombieNode`), `.play_animation(name)` (`PlayZombieAnimNode`), `.split()` (`ZombieSplitNode`) | `DamageZombieNode, GetZombieStatsNode, GetZombieStatusNode, ModifyZombieHealthNode, MoveZombieNode, PlayZombieAnimNode, SetZombieMindControlledNode, SetZombieStatsNode, SetZombieStatusNode, ZombieSplitNode` |
| `Bullet(ref)` | Entity wrapper for projectile pointers | Exposes `.destroy()`, `.modify(value)` | `ModifyEventBulletNode` |
| `ForEachPlant(list_port)` | Context manager looping over plant entity list | Iterates live plant entities; loop variable acts as transparent `Plant` proxy. Has `.on_complete` branch. | `ForEachPlantNode` |
| `ForEachZombie(list_port)` | Context manager looping over zombie entity list | Iterates live zombie entities; loop variable acts as transparent `Zombie` proxy. Has `.on_complete` branch. | `ForEachZombieNode` |
| `ForEachAllZombies()` | Context manager looping over ALL living zombies on lawn | Loops over every zombie on the board without querying first. | `ForEachAllZombiesNode` |
| `PlantTypeList([types])` | Dynamic plant type collection on node canvas | Supports `+=`, `-=`, `.contains(type)`, `.get_random()`, `.for_each()` | `SinglePlantTypeListNode, MultiPlantTypeListNode, MergePlantTypeListsNode, RemovePlantTypeNode, GetRandomPlantTypeNode, ForEachPlantTypeNode, PlantTypeListStorageNode` |
| `ZombieTypeList([types])` | Dynamic zombie type collection on node canvas | Supports `+=`, `append(type)`, `contains(type)`, `find_index(type)`, `get_item(index)`, `remove_at(index)`, `clear()` | `AppendZombieTypeListNode, FindZombieTypeListValueNode, GetZombieTypeListItemNode, GetListLengthNode, RemoveListItemNode, ClearListValuesNode` |

### 2. Spawning Entities (`Spawner/`)
*Constructs new entities at runtime with dedicated execution branches for placement success and failure.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Spawner.Set_Plant(row, col, plant_type, force=False)` | Spawns plant and returns `SpawnedPlant` | Can be used as context manager `with Spawner.Set_Plant(...) as plant:`. Exposes `.on_created` (alias `.on_success`) and `.on_failed` branches. Enforces strict `PlantType` enum. | `SetPlantNode, PlantTypeValueNode` |
| `Spawner.Set_Zombie(row, col, zombie_type, mind_controlled=False)` | Spawns zombie and returns `SpawnedZombie` | Can be used as context manager `with Spawner.Set_Zombie(...) as zombie:`. Exposes `.on_created` branch. Enforces strict `ZombieType` enum. | `CreateZombieNode, ZombieTypeValueNode` |
| `Spawner.Set_Bullet(row, col, bullet_type, damage, speed, angle, ...)` | Fires event bullet and returns `SpawnedBullet` | Can be used as context manager `with Spawner.Set_Bullet(...) as bullet:`. Exposes `.on_created` and `.on_failed` branches. Enforces strict `BulletType` enum. | `ShootEventBulletNode, BulletTypeValueNode` |

### 3. Game Economy & Stage Management (`Game/`)
*Direct access to level Sun, Money, wave counters, stage transitions, and victory conditions.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Board.Sun / Game.Sun` | Sun balance property manager | Supports `+=`, `-=`, `*=`, `/=`, `= DirectValue`, conditions (`<`, `>`, `==`), and `with Board.Sun.SpendSun(cost) as tx: ... with tx.Failed: ...` | `GetSunAmountNode, UseSunNode, AddNode, SubtractNode, MultiplyNode, DivideNode, IntToFloatNode` |
| `Board.Money / Game.Money` | Coin balance property manager | Supports `+=`, `-=`, and `with Board.Money.SpendMoney(cost) as tx: ... with tx.Failed: ...`, plus `Board.Money.check_money(cost, on_true, on_false)` | `GetMoneyAmountNode, UseMoneyNode, IntAddNode, IntSubtractNode` |
| `Board.Wave` | Current active wave index port | Read-only integer output port | `OnWaveNode` |
| `Game.pause_wave_timer(paused=True)` | Pauses/resumes automatic wave countdown | Emits pause toggle node | `SetWaveCountdownPausedNode` |
| `Game.Stage.change(stage_name='战斗')` | Transitions level to named stage | Emits stage transition node with custom stageName string | `ChangeStageNode` |
| `Game.Stage.get_current()` | Returns current stage name string port | Query stage name | `GetStageNode` |
| `Game.trigger_game_win()` | Instant victory trigger | Ends level in victory | `GameWinNode` |
| `Game.trigger_game_over(reason='Defeated!')` | Instant defeat trigger | Ends level in defeat with message | `GameOverNode` |
| `Game.get_buff(buff_enum)` | Grants travel buff to player | Accepts AdvBuff, UltiBuff, TravelDebuff, or TravelBuffType | `GetTravelBuffNode` |

### 4. Lawn & Board Props (`Lawn/`)
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
| `Lawnf.delete_grid_items(row, col)` | Clears grid item props at tile | Removes graves/ladders | `DeleteGridItemsNode` |
| `Lawnf.change_event_map(map_id)` | Changes visual event map background | Map change | `ChangeEventMapNode` |
| `Lawnf.change_event_music(music_id)` | Changes active background music | BGM change | `ChangeEventMusicNode` |
| `Lawnf.set_zombie_house_rule(rule_id)` | Sets zombie house rules | Custom gameplay rule | `SetZombieHouseRuleNode` |

### 5. Event Triggers (`Triggers/`)
*Context managers that capture event execution streams and auto-wire sequential triggers.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Trigger.OnBoardStart()` | First frame of level loading | Initializes board setups and starting resources | `OnBoardStartNode` |
| `Trigger.OnGameStart()` | After 'Ready, Set, Plant!' finishes | Active gameplay kickoff | `OnGameStartNode` |
| `Trigger.OnWave()` | Wave arrival event | Yields current wave number output port | `OnWaveNode` |
| `Trigger.OnWaveCleared()` | Wave wiped event | Fires when all zombies in wave die. Yields wave number. | `OnWaveClearedNode` |
| `Trigger.OnWaveEvent()` | Wave milestone event | Engine wave event broadcast. Yields wave number. | `WaveEventNode` |
| `Trigger.OnStageEnter(stage_name='战斗')` | Level enters named stage | Fires on stage transition. Configurable stageName. | `OnStageEnterNode` |
| `Trigger.OnMouseClick()` | Player clicks mouse on lawn | Yields wrapped `Mouse` object (row, col, is_left_click, item) | `OnMouseClickNode` |
| `Trigger.OnKeyDown(key_code)` | Keyboard key pressed down | Accepts KeyCode enum or int | `OnKeyPressNode` |
| `Trigger.OnPlantCreate()` | Plant placed or spawned | Yields wrapped `Plant` instance | `OnPlantCreateNode` |
| `Trigger.OnPlantClick() / OnPlantClicked()` | Player clicks plant on lawn | Yields wrapped `Plant` instance | `OnPlantClickNode` |
| `Trigger.OnPlantDie() / OnPlantDeath()` | Plant dies (pre-removal) | Yields wrapped `Plant` instance | `OnPlantDieNode` |
| `Trigger.OnPlantDeathComplete()` | Plant death animation finishes | Yields wrapped `Plant` instance | `OnPlantDeathCompleteNode` |
| `Trigger.OnPlantMixed()` | Two plants fused/mixed on lawn | Yields wrapped hybrid `Plant` instance | `OnPlantMixedNode` |
| `Trigger.OnWorldPlantEffect()` | Global world plant effect activates | Yields affected row index integer port | `OnWorldPlantEffectNode` |
| `Trigger.OnZombieSpawn()` | Zombie enters lawn | Yields wrapped `Zombie` instance | `OnZombieSpawnNode` |
| `Trigger.OnZombieDie() / OnZombieDeath()` | Zombie health drops to 0 | Yields defeated `Zombie` instance | `OnZombieDieNode` |
| `Trigger.OnZombieClick()` | Player clicks zombie on screen | Yields clicked `Zombie` instance | `OnZombieClickNode` |
| `Trigger.OnZombieHealthBelow()` | Zombie health drops below threshold | Yields critical `Zombie` instance | `OnZombieHealthBelowNode` |

### 6. Branching & Control Flow (`Branching/`, `Loops/`)
*Conditional execution paths and synchronous single-frame loops.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `If(condition) as branch` | Branch execution on boolean condition | Provides `.Elif(condition)` and `.Else` chaining | `BranchNode` |
| `Switch(variable) as sw` | Multi-branch value matching | Provides `with sw.case(val1, val2): ...` and `with sw.default: ...` | `MultiBranchNode` |
| `For(count) as loop` | Fixed-iteration loop | Executes `count` times synchronously. Exposes `loop.index` port. | `ForLoopNode` |
| `While(condition)` | Conditional single-frame while loop | Executes until condition is False | `WhileNode` |
| `ExecutionPath(port)` | Internal execution path sequencer | Manages trigger stack context entering/exiting | `(Context Engine)` |

### 7. Variables & Conversions (`Variables/`, `Types/`)
*Persistent engine variables and type conversion utilities.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `IntVar(start_val=0, name='...')` | 32-bit signed integer variable | Exposes `.set(val)`, `+=`, `-=`, `*=`, `//=`, `%=`, `.add_in_place(val)`, `.to_string(decimals=0)` | `IntVariableNode, SetIntVariableValueNode, GetIntVariableValueNode, IntVariableArithmeticNode` |
| `FloatVar(start_val=0.0, name='...')` | Floating-point variable | Exposes `.set(val)`, `+=`, `-=`, `*=`, `/=`, `.to_string(decimals=2)` | `FloatVariableNode, SetFloatVariableValueNode, GetFloatVariableValueNode, FloatVariableArithmeticNode` |
| `BoolVar(start_val=False, name='...')` | Boolean flag variable | Exposes `.set(val)`, `.toggle()`, `&`, `|`, `~` | `BoolVariableNode, SetBoolVariableValueNode, GetBoolVariableValueNode` |
| `StringVar(start_val='', name='...')` | String variable | Exposes `.set(val)`, `+=`, `+`, `.to_string()` | `StringVariableNode, SetStringVariableValueNode, GetStringVariableValueNode, StringConcatNode` |
| `Int(val) / Int.Cast(val)` | Int constant & type casting | Constructs IntValueNode; `.Cast()` converts float/string/port to Int; `from_ascii(text, idx)` extracts ASCII | `IntValueNode, FloatToIntNode, StringToIntNode, StringToAsciiNode` |
| `Float(val) / Float.Cast(val)` | Float constant & type casting | Constructs FloatValueNode; `.Cast()` converts int/string/port to Float | `FloatValueNode, IntToFloatNode, StringToFloatNode` |
| `String(val) / String.Cast(val)` | String constant & type casting | Constructs StringValueNode; `.Cast()` converts any num/entity/enum port to String; `from_ascii()`, `to_plant_type()`, `to_zombie_type()`, `to_object()` | `StringValueNode, IntToStringNode, FloatToStringNode, AsciiToStringNode, StringToPlantTypeNode, StringToZombieTypeNode, StringToObjectNode` |
| `Bool(val) / Bool.Cast(val)` | Bool constant & type casting | Constructs BoolValueNode; `.Cast()` converts int/float to Bool | `BoolValueNode, IntToBoolNode, FloatToBoolNode` |

### 8. Player Input & Tools (`Input/`)
*Handles cursor input and player cursor tool interactions.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Mouse(node)` | Mouse event helper | Exposes `.row`, `.col`, `.is_left_click`, `.item` | `OnMouseClickNode` |
| `Tool.get_held()` | Returns (GameObject, ToolType) | Queries tool held on player cursor | `GetHeldToolNode` |
| `Tool.is_held(tool_type)` | Checks if specific ToolType is held | Returns boolean port | `GetHeldToolNode, CompareToolTypeNode, ToolTypeValueNode` |
| `Tool.get_cooldown(tool_type)` | Queries tool cooldown | Returns `ToolCooldown(total_seconds, remaining_seconds, exists)` | `GetToolCooldownNode, ToolTypeValueNode` |
| `Tool.set_cooldown(tool_type, ratio)` | Sets tool cooldown ratio | 0.0 = ready, 1.0 = max cooldown | `SetToolCooldownNode, ToolTypeValueNode` |

### 9. World & GameObjects (`World/`)
*GameObject transforms, entity casting, and named bindings.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `WorldObject.create(name, position, icon_plant)` | Creates custom event game object | Instantiates GameObject on canvas | `CreateEventObjectNode` |
| `WorldObject.destroy()` | Destroys GameObject | Destruction | `DestroyEventObjectNode` |
| `WorldObject.get_transform()` | Returns ObjectTransform | Reads `position`, `scale`, `exists` | `GetObjectTransformNode` |
| `WorldObject.set_transform(position, scale)` | Updates 3D transform | Sets position and scale | `SetEventObjectTransformNode` |
| `WorldObject.to_plant() / try_cast_to_plant()` | Casts GameObject to Plant | Returns `Plant` / `(Plant, exists_port)` | `ObjectToPlantNode` |
| `WorldObject.to_zombie() / try_cast_to_zombie()` | Casts GameObject to Zombie | Returns `Zombie` / `(Zombie, exists_port)` | `ObjectToZombieNode` |
| `WorldObject.bind_plant(plant, name='守护目标')` | Binds plant under named alias | Saves plant binding reference | `BindPlantNode` |
| `WorldObject.get_bound_plant(name='守护目标')` | Retrieves bound plant by name | Returns wrapped `Plant` | `GetBoundPlantNode` |
| `WorldObject.bind_zombie(zombie, name='首领')` | Binds zombie under named alias | Saves zombie binding reference | `BindZombieNode` |
| `WorldObject.get_bound_zombie(name='首领')` | Retrieves bound zombie by name | Returns wrapped `Zombie` | `GetBoundZombieNode` |
| `WorldObject.vector3(x, y, z)` | Constructs Vector3 port | 3D coordinate node | `MakeVector3Node` |
| `WorldObject.mouse_world_position()` | Returns cursor world position | Mouse 3D coordinate | `GetMouseWorldPositionNode` |
| `WorldObject.event_position()` | Returns event world position | Event 3D coordinate | `GetEventPositionNode` |

### 10. Math & Comparisons (`Math/`)
*Math functions and type-aware comparisons.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Math.pow(val, exp)` | Exponential calculation | Emits PowerNode | `PowerNode` |
| `Math.log(val, base=e)` | Logarithm calculation | Emits LogarithmNode | `LogarithmNode` |
| `Math.greater(a, b)` | Compares if a > b | Auto-selects CompareIntNode or CompareFloatNode | `CompareIntNode, CompareFloatNode` |
| `Math.less(a, b)` | Compares if a < b | Auto-selects CompareIntNode or CompareFloatNode | `CompareIntNode, CompareFloatNode` |
| `Math.equal(a, b)` | Compares if a == b | Auto-selects CompareIntNode or CompareFloatNode | `CompareIntNode, CompareFloatNode` |
| `Math.same_object(a, b)` | GameObject reference equality | Checks if two GameObjects are identical | `CompareGameObjectNode` |

### 11. UI Popups & Menus (`UI/`)
*On-screen cards, popups, and selection dialogs.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `InGameUI.display_text(*args, duration=3.0)` | On-screen text notification (Print) | Concatenates ports/strings | `ShowTextNode, StringConcatNode` |
| `InGameUI.give_plant_card(type, cooldown, cost, ...)` | Grants plant card to selection | Seed packet override | `AddPlantCardNode` |
| `InGameUI.remove_plant_card(type)` | Removes plant card from selection | Removes seed packet | `DeleteCardByTypeNode` |
| `InGameUI.give_zombie_card(type, cooldown, cost, ...)` | Grants zombie card to selection | Zombie seed packet override | `AddZombieCardNode` |
| `InGameUI.remove_zombie_card()` | Removes zombie card from selection | Removes zombie packet | `DeleteZombieCardsNode` |
| `InGameUI.set_zombie_card_cooldown(type, cd)` | Sets cooldown on zombie card | Sets cooldown | `SetZombieCardCooldownNode` |
| `InGameUI.spawn_dropped_card(row, col, plant_type)` | Spawns dropped card pickup on lawn | Pickup card entity | `CreatePlantCardNode` |
| `InGameUI.display_info_card(title, subtitle, on_clicked)` | Displays modal info card | Dismissible card dialog | `CreateInfoCardNode` |
| `InGameUI.InfoCard(title, subtitle)` | Context manager for modal info card | Card dismissal block | `CreateInfoCardNode` |
| `InGameUI.close_all_info_cards()` | Closes all active info cards | Dismisses cards | `DeleteInfoCardsNode` |
| `MultiSelectMenu(is_rerollable, reroll_count, ...)` | Multiple choice perk popup | Supports `@menu.option(...)` and `menu.add_option(Option(...))`; hooks `menu.Output.OnExit` and `menu.Output.OnRefresh` | `ShowMultipleChoiceMenuNode, AddMultipleChoiceOptionNode, MergeMultipleChoiceOptionListsNode` |
| `format_string(*args)` | Chained string concatenation helper | Merges mixed ports into single string port | `StringConcatNode` |

### 12. Randomization (`Random/`)
*Random values, path scrambling, and seeded LCG.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Random.randint(min, max)` | Random integer in [min, max] | Returns integer output port | `RandomIntNode` |
| `Random.randf(min, max)` | Random float in [min, max] | Returns float output port | `RandomFloatNode` |
| `Random.value` | Normalized random float in [0.0, 1.0] | Returns float output port | `RandomFloatNode` |
| `Random.TriggerChance(probability)` | Context manager gating execution by probability | Rolls float check | `RandomFloatNode, CompareFloatNode, BranchNode` |
| `Random.RandomTrigger(count=1)` | Context manager randomly picking child paths | Path scrambler | `RandomTriggerNode` |
| `Random.Seeded(seed, name)` | Deterministic Linear Congruential Generator | Guaranteed reproducible sequence using node math | `IntVariableNode, MultiplyNode, AddNode, IntModuloNode` |

### 13. Time & Clocks (`Time/`)
*Asynchronous delays, recurring loops, and elapsed timers.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Time.Wait(duration)` | Context manager delaying nested execution | Non-blocking game delay | `WaitNode` |
| `Time.OnFixedUpdate(interval=0.1) as update` | Recurring execution loop | Provides `update.tick`, `.toggle()`, `.on_enable`, `.on_disable`, `.on_cycle` | `ToggleCycleNode, CounterNode` |
| `Time.time_since_start` | Seconds elapsed since board initialization | Float output port | `FloatVariableNode, ToggleCycleNode` |
| `Time.time_since_game_start` | Seconds elapsed since active gameplay began | Float output port | `FloatVariableNode, ToggleCycleNode` |

### 14. Standard Library (`StdLib.py`)
*Higher-level utility collections and player control abstractions.*

| Interface / Method | Purpose | Capabilities | Underlying Original Nodes |
| :--- | :--- | :--- | :--- |
| `Dictionary(schema)` | Virtual string-keyed dictionary of stateful variables | Supports reading/writing using dot-notation or brackets | `IntVar, FloatVar, BoolVar` |
| `Array(size, default_val)` | Virtual fixed-size array supporting port-based index access | Supports `.read(index_port, callback)` and `.write(index_port, value)` | `IntVar, FloatVar, BoolVar, BranchNode` |
| `WASDPlant(plant)` | Maps keyboard W, A, S, D keys to relative plant motion | Binds arrow listeners to `plant.move_relative()` | `OnKeyPressNode, MovePlantNode` |

---

## 🎯 Gap Analysis: Nodes Not Yet Exposed in Extensions

The following **44 base game Original nodes** are currently not exposed as high-level Extension methods, categorized by their implementation readiness and architectural purpose:

### Group 1: Available in `nodes.py` (Ready for Direct Extension Binding) - 5 Nodes
These nodes already have complete factory functions and port plumbing in `nodes.py`. They can be bound to high-level classes immediately upon user design confirmation:

| Original Node | Factory Function | Target Extension Class | Suggested Alignment |
| :--- | :--- | :--- | :--- |
| `InsertZombieTypeListNode` | `nodes.insert_zombie_type_list(list_var, index, value)` | `ZombieTypeList` | Add `ZombieTypeList.insert(index, zombie_type)` method |
| `ReplaceZombieTypeListNode` | `nodes.replace_zombie_type_list(list_var, index, value)` | `ZombieTypeList` | Add `ZombieTypeList.replace(index, zombie_type)` method |
| `ToolTypeValueNode` | `nodes.tool_type_value(val)` | `Tool` | Used internally by `Tool.is_held()` and `Tool.get_cooldown()`; can be exposed directly as `Tool.Value(tool_type)` if needed |
| `GetSunNode` | `nodes.get_sun()` | `Board.Sun` | Alternative sequential getter with trigger input; currently `GetSunAmountNode` is used for property reads |
| `GetMoneyNode` | `nodes.get_money()` | `Board.Money` | Alternative sequential getter with trigger input; currently `GetMoneyAmountNode` is used for property reads |

### Group 2: Deferred List Variable Nodes - 31 Nodes
These nodes operate on engine dynamic lists for primitive types (`Bool`, `Float`, `Int`, `String`, `GameObject`, `PlantType`). Deferred pending user requirements on whether they should be exposed via unified collection classes (e.g. `IntList`, `FloatList`, `StringList`, `ObjectList`, `PlantTypeList`) or a generic `ListVar[T]` container:

| Operation | Applicable Types | Original Node Names |
| :--- | :--- | :--- |
| **Append** | `Bool`, `Float`, `Int`, `String`, `Object`, `PlantType` | `AppendBoolListNode`, `AppendFloatListNode`, `AppendIntListNode`, `AppendStringListNode`, `AppendObjectListNode`, `AppendPlantTypeListNode` |
| **Get Item** | `Bool`, `Float`, `Int`, `String`, `Object`, `PlantType` | `GetBoolListItemNode`, `GetFloatListItemNode`, `GetIntListItemNode`, `GetStringListItemNode`, `GetObjectListItemNode`, `GetPlantTypeListItemNode` |
| **Insert** | `Bool`, `Float`, `Int`, `String`, `Object`, `PlantType` | `InsertBoolListNode`, `InsertFloatListNode`, `InsertIntListNode`, `InsertStringListNode`, `InsertObjectListNode`, `InsertPlantTypeListNode` |
| **Replace** | `Bool`, `Float`, `Int`, `String`, `Object`, `PlantType` | `ReplaceBoolListNode`, `ReplaceFloatListNode`, `ReplaceIntListNode`, `ReplaceStringListNode`, `ReplaceObjectListNode`, `ReplacePlantTypeListNode` |
| **Find Value** | `Bool`, `Float`, `Int`, `String`, `Object`, `PlantType` | `FindBoolListValueNode`, `FindFloatListValueNode`, `FindIntListValueNode`, `FindStringListValueNode`, `FindObjectListValueNode`, `FindPlantTypeListValueNode` |
| **Copy Values**| Universal | `CopyListValuesNode` |

### Group 3: Optimizer-Internal Nodes - 4 Nodes
These nodes are redundant or unergonomic as user-facing DSL syntax. Per architectural decisions, they are reserved for the compiler optimizer to collapse graphs and reduce node counts:

- `DoOnceNode`: Fires execution path only once. Transpiler achieves this via `BoolVar` gating.
- `PulseNode`: Periodic pulse generator. Transpiler achieves this via `Time.OnFixedUpdate()`.
- `RepeatUntilNode`: Repeat until condition. Transpiler achieves this via `While` loops.
- `WaitUntilNode`: Wait until condition. Deemed redundant in single-frame visual scripting flows.

### Group 4: Duplicate / Redundant Nodes - 3 Nodes
Duplicate engine implementations of the reward / choice system:

- `TypedChoiceMenuNode`, `TypedChoiceMergeNode`, `TypedChoiceOptionNode`: Redundant duplicate of `ShowMultipleChoiceMenuNode`, `AddMultipleChoiceOptionNode`, `MergeMultipleChoiceOptionListsNode`, which are already cleanly wrapped in `MultiSelectMenu`.

### Group 5: Deprecated Engine Nodes - 1 Node
- `GetTravelEntryNode`: Deprecated in original PvZ Fusion game engine; replaced by `GetTravelBuffNode`.

