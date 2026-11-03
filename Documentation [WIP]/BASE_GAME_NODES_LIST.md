# 🎮 Base Game Original Nodes Inventory

This document contains an exhaustive, structured inventory of all **240 base game visual scripting nodes** defined in the `_Nodes/Original/` directory, mirroring the official *Plants vs. Zombies: Fusion* IL2CPP reflection metadata.

---

## 📊 Summary Statistics

| Metric | Count | Description |
| :--- | :--- | :--- |
| **Total Original Nodes** | **240** | Total base game IL2CPP node classes in `_Nodes/Original/` |
| **Implemented in Extensions** | **196** | Wrapped with high-level Pythonic DSL context managers, methods, or operators |
| **Available in nodes.py only** | **5** | Defined in `nodes.py` factory, ready to be bound to an Extension interface |
| **Deferred List Variable Nodes** | **31** | Dynamic typed collections deferred pending user architectural specification |
| **Omitted (Optimizer-Internal)** | **4** | Control-flow nodes reserved for compiler optimizer (`DoOnce`, `Pulse`, `RepeatUntil`, `WaitUntil`) |
| **Omitted (Duplicate / Redundant)** | **3** | Redundant alternatives (`TypedChoiceMenuNode`, `TypedChoiceMergeNode`, `TypedChoiceOptionNode`) |
| **Omitted (Deprecated Engine Node)** | **1** | Deprecated in the original game engine (`GetTravelEntryNode`) |

### Category Breakdown

| Category | Total Nodes | Implemented | Pending / Deferred / Omitted |
| :--- | :---: | :---: | :---: |
| **BulletManipulation** | 3 | 3 | 0 |
| **Calculate** | 14 | 14 | 0 |
| **Comparison** | 3 | 3 | 0 |
| **Constants** | 5 | 5 | 0 |
| **Deprecated** | 1 | 0 | 1 |
| **GameFlow** | 3 | 3 | 0 |
| **GeneralFunction** | 26 | 23 | 3 |
| **Logic** | 13 | 9 | 4 |
| **MapFunction** | 14 | 14 | 0 |
| **ObjectBinding** | 4 | 4 | 0 |
| **ObjectOperation** | 7 | 7 | 0 |
| **PlantFunction** | 33 | 33 | 0 |
| **RewardOption** | 3 | 0 | 3 |
| **Trigger** | 16 | 16 | 0 |
| **TypeConvert** | 20 | 20 | 0 |
| **Variables/Boolean** | 3 | 3 | 0 |
| **Variables/Float** | 4 | 4 | 0 |
| **Variables/Integer** | 4 | 4 | 0 |
| **Variables/List** | 41 | 8 | 33 |
| **Variables/String** | 3 | 3 | 0 |
| **ZombieFunction** | 20 | 20 | 0 |

---

## 📑 Detailed Node Inventory by Category

### BulletManipulation (3 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BulletTypeValueNode` | `BulletTypeValueNode` | *(None)* | `子弹类型` (BulletType) | *(None)* | **Implemented in Extensions** | **Extensions:** `Spawner\spawner.py`<br>**nodes.py:** `bullet_type_value()` |
| `ModifyEventBulletNode` | `ModifyEventBulletNode` | `触发` (Trigger)<br>`子弹` (Bullet)<br>`数值` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\bullet.py`<br>**nodes.py:** `modify_event_bullet()` |
| `ShootEventBulletNode` | `ShootEventBulletNode` | `触发` (Trigger)<br>`子弹类型` (BulletType)<br>`在鼠标处` (Bool)<br>`行` (Int)<br>`列` (Float)<br>`僵尸阵营` (Bool)<br>`伤害` (Int)<br>`速度` (Float)<br>`角度` (Float)<br>`大小倍率` (Float) | `完成` (Trigger)<br>`失败` (Trigger)<br>`子弹` (Bullet) | *(None)* | **Implemented in Extensions** | **Extensions:** `Spawner\spawner.py`<br>**nodes.py:** `shoot_event_bullet()` |

### Calculate (14 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AddNode` | `AddNode` | `A` (Float)<br>`B` (Float) | `结果` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `add_node()` |
| `DivideNode` | `DivideNode` | `被除数` (Float)<br>`除数` (Float) | `商` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `divide_node()` |
| `IntAddNode` | `IntAddNode` | `A` (Int)<br>`B` (Int) | `和` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`, `Entity\zombie_type_list.py`, `Variables\variables.py`<br>**nodes.py:** `int_add()` |
| `IntDivideNode` | `IntDivideNode` | `被除数` (Int)<br>`除数` (Int) | `商` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `int_divide()` |
| `IntModuloNode` | `IntModuloNode` | `被除数` (Int)<br>`除数` (Int) | `余数` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `int_modulo()` |
| `IntMultiplyNode` | `IntMultiplyNode` | `A` (Int)<br>`B` (Int) | `积` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `int_multiply()` |
| `IntSubtractNode` | `IntSubtractNode` | `被减数` (Int)<br>`减数` (Int) | `差` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`, `Entity\zombie_type_list.py`, `Variables\variables.py`<br>**nodes.py:** `int_subtract()` |
| `LogarithmNode` | `LogarithmNode` | `数值` (Float)<br>`底数` (Float) | `结果` (Float)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Math\calc.py`<br>**nodes.py:** `logarithm()` |
| `MultiplyNode` | `MultiplyNode` | `A` (Float)<br>`B` (Float) | `积` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `multiply_node()` |
| `PowerNode` | `PowerNode` | `数值` (Float)<br>`指数` (Float) | `结果` (Float)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Math\calc.py`<br>**nodes.py:** `power()` |
| `RandomFloatNode` | `RandomFloatNode` | `最小值` (Float)<br>`最大值` (Float) | `随机浮点数` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Random\random_ext.py`<br>**nodes.py:** `random_float()` |
| `RandomIntNode` | `RandomIntNode` | `最小值` (Int)<br>`最大值` (Int) | `随机整数` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Random\random_ext.py`<br>**nodes.py:** `random_int()` |
| `StringConcatNode` | `StringConcatNode` | `A` (String)<br>`B` (String) | `结果` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\format_string.py`, `Variables\string_var.py`<br>**nodes.py:** `string_concat()` |
| `SubtractNode` | `SubtractNode` | `被减数` (Float)<br>`减数` (Float) | `差` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `subtract_node()` |

### Comparison (3 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `CompareFloatNode` | `CompareFloatNode` | `值A` (Float)<br>`值B` (Float) | `大于` (Bool)<br>`小于` (Bool)<br>`等于` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Math\calc.py`<br>**nodes.py:** `compare_float()` |
| `CompareGameObjectNode` | `CompareGameObjectNode` | `对象A` (GameObject)<br>`对象B` (GameObject) | `相同` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Math\calc.py`<br>**nodes.py:** `compare_game_object()` |
| `CompareIntNode` | `CompareIntNode` | `值A` (Int)<br>`值B` (Int) | `大于` (Bool)<br>`小于` (Bool)<br>`等于` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Math\calc.py`<br>**nodes.py:** `compare_int()` |

### Constants (5 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BoolValueNode` | `BoolValueNode` | *(None)* | `值` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`, `Entity\zombie_type_list.py`, `Types\conversions.py`<br>**nodes.py:** `bool_value()` |
| `CounterNode` | `CounterNode` | `触发` (Trigger)<br>`是否重置` (Bool) | `计数` (Int)<br>`计数完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Time\time_ext.py`<br>**nodes.py:** `counter_node()` |
| `FloatValueNode` | `FloatValueNode` | *(None)* | `值` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `float_value()` |
| `IntValueNode` | `IntValueNode` | *(None)* | `值` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`, `Entity\zombie_type_list.py`, `Types\conversions.py`, `Variables\variables.py`<br>**nodes.py:** `int_value()` |
| `StringValueNode` | `StringValueNode` | *(None)* | `值` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`, `UI\format_string.py`<br>**nodes.py:** `string_value()` |

### Deprecated (1 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GetTravelEntryNode` | `GetTravelEntryNode` | `触发` (Trigger) | `完成` (Trigger) | *(None)* | **Omitted (Deprecated engine node)** | *(None)* |

### GameFlow (3 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `ChangeStageNode` | `ChangeStageNode` | `触发` (Trigger) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\game.py`<br>**nodes.py:** `change_stage()` |
| `GetStageNode` | `GetStageNode` | *(None)* | `阶段名` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\game.py`<br>**nodes.py:** `get_stage()` |
| `OnStageEnterNode` | `OnStageEnterNode` | *(None)* | `触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_stage_enter()` |

### GeneralFunction (26 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AddMultipleChoiceOptionNode` | `AddMultipleChoiceOptionNode` | `标题` (String)<br>`描述` (String)<br>`植物类型` (PlantType)<br>`僵尸类型` (ZombieType) | `选项列表` (ChoiceOptions)<br>`选项被点击` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\menu.py`<br>**nodes.py:** `add_multiple_choice_option()` |
| `AddPlantCardNode` | `AddPlantCardNode` | `触发` (Trigger)<br>`植物类型` (PlantType)<br>`冷却时间` (Float)<br>`价格` (Int)<br>`使用默认数据` (Bool) | `添加成功` (Trigger)<br>`添加失败` (Trigger)<br>`种植时触发` (Trigger)<br>`种植的植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `add_plant_card()` |
| `CompareToolTypeNode` | `CompareToolTypeNode` | `A` (ToolType)<br>`B` (ToolType) | `相等` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Input\tool.py`<br>**nodes.py:** `compare_tool_type()` |
| `CreateGraveNode` | `CreateGraveNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_grave()` |
| `CreateInfoCardNode` | `CreateInfoCardNode` | `触发` (Trigger)<br>`大标题` (String)<br>`小标题` (String) | `点击卡牌时触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`, `UI\info_card.py`<br>**nodes.py:** `create_info_card()` |
| `CreateParticleNode` | `CreateParticleNode` | `触发` (Trigger)<br>`行` (Int)<br>`列` (Int) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_particle()` |
| `DeleteCardByTypeNode` | `DeleteCardByTypeNode` | `触发` (Trigger)<br>`植物类型` (PlantType) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `delete_card_by_type()` |
| `DeleteInfoCardsNode` | `DeleteInfoCardsNode` | `触发` (Trigger)<br>`卡牌对象` (GameObject)<br>`全部` (Bool) | `完成` (Trigger)<br>`删除数量` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `delete_info_cards()` |
| `GameOverNode` | `GameOverNode` | `触发` (Trigger)<br>`失败原因` (String) | *(None)* | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\game.py`, `Lawn\lawnf.py`<br>**nodes.py:** `game_over()` |
| `GameWinNode` | `GameWinNode` | `触发` (Trigger) | *(None)* | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\game.py`, `Lawn\lawnf.py`<br>**nodes.py:** `game_win()` |
| `GetEventPositionNode` | `GetEventPositionNode` | *(None)* | `位置` (Vector3) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `get_event_position()` |
| `GetHeldToolNode` | `GetHeldToolNode` | *(None)* | `对象` (GameObject)<br>`类型` (ToolType) | *(None)* | **Implemented in Extensions** | **Extensions:** `Input\tool.py`<br>**nodes.py:** `get_held_tool()` |
| `GetMoneyAmountNode` | `GetMoneyAmountNode` | *(None)* | `金币` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\money.py`<br>**nodes.py:** `get_money_amount()` |
| `GetMoneyNode` | `GetMoneyNode` | `触发` (Trigger)<br>`金币数量` (Int) | `完成` (Trigger) | *(None)* | **Available in nodes.py (not in Extensions)** | **nodes.py:** `get_money()` |
| `GetSunAmountNode` | `GetSunAmountNode` | *(None)* | `阳光数量` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\sun.py`<br>**nodes.py:** `get_sun_amount()` |
| `GetSunNode` | `GetSunNode` | `触发` (Trigger)<br>`阳光数量` (Int) | `完成` (Trigger) | *(None)* | **Available in nodes.py (not in Extensions)** | **nodes.py:** `get_sun()` |
| `GetToolCooldownNode` | `GetToolCooldownNode` | `类型` (ToolType) | `总秒数` (Float)<br>`剩余秒数` (Float)<br>`存在` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Input\tool.py`<br>**nodes.py:** `get_tool_cooldown()` |
| `GetTravelBuffNode` | `GetTravelBuffNode` | `触发` (Trigger) | `成功` (Trigger) | `buff`=None | **Implemented in Extensions** | **Extensions:** `Game\game.py`, `Lawn\lawnf.py`<br>**nodes.py:** `get_travel_buff()` |
| `MergeMultipleChoiceOptionListsNode` | `MergeMultipleChoiceOptionListsNode` | `列表1` (ChoiceOptions)<br>`列表2` (ChoiceOptions) | `合并列表` (ChoiceOptions) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\menu.py`<br>**nodes.py:** `merge_multiple_choice_option_lists()` |
| `PlaySoundNode` | `PlaySoundNode` | `触发` (Trigger)<br>`音效ID` (Int) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `play_sound()` |
| `SetToolCooldownNode` | `SetToolCooldownNode` | `触发` (Trigger)<br>`类型` (ToolType)<br>`总秒数` (Float)<br>`剩余秒数` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Input\tool.py`<br>**nodes.py:** `set_tool_cooldown()` |
| `ShowMultipleChoiceMenuNode` | `ShowMultipleChoiceMenuNode` | `触发` (Trigger)<br>`选项列表` (ChoiceOptions)<br>`可刷新` (Bool)<br>`刷新次数` (Int)<br>`可取消` (Bool)<br>`窗口数量` (Int) | `退出时触发` (Trigger)<br>`刷新时触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\menu.py`<br>**nodes.py:** `show_multiple_choice_menu()` |
| `ShowTextNode` | `ShowTextNode` | `触发` (Trigger)<br>`文本` (String)<br>`持续时间` (Float) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `show_text()` |
| `ToolTypeValueNode` | `ToolTypeValueNode` | *(None)* | `类型` (ToolType) | *(None)* | **Available in nodes.py (not in Extensions)** | **nodes.py:** `tool_type_value()` |
| `UseMoneyNode` | `UseMoneyNode` | `触发` (Trigger)<br>`金币数量` (Int) | `消耗成功` (Trigger)<br>`金币不足` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\money.py`<br>**nodes.py:** `use_money()` |
| `UseSunNode` | `UseSunNode` | `触发` (Trigger)<br>`阳光数量` (Int) | `消耗成功` (Trigger)<br>`阳光不足` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\sun.py`<br>**nodes.py:** `use_sun()` |

### Logic (13 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AndNode` | `AndNode` | `条件A` (Bool)<br>`条件B` (Bool) | `结果` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`, `Entity\zombie_type_list.py`, `Variables\variables.py`<br>**nodes.py:** `and_node()` |
| `BranchNode` | `BranchNode` | `触发` (Trigger)<br>`条件` (Bool) | `真（触发）` (Trigger)<br>`假（停止）` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Branching\branching.py`, `Entity\plant_type_list.py`, `Loops\loops.py`<br>**nodes.py:** `branch_node()` |
| `DoOnceNode` | `DoOnceNode` | `触发` (Trigger)<br>`重置` (Trigger) | `触发` (Trigger) | *(None)* | **Omitted (Optimizer-internal)** | *(None)* |
| `ForLoopNode` | `ForLoopNode` | `触发` (Trigger)<br>`循环次数` (Int) | `循环体` (Trigger)<br>`当前索引` (Int)<br>`完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Loops\loops.py`<br>**nodes.py:** `for_loop_node()` |
| `NotNode` | `NotNode` | `输入` (Bool) | `输出` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `not_node()` |
| `OrNode` | `OrNode` | `条件A` (Bool)<br>`条件B` (Bool) | `结果` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `or_node()` |
| `PulseNode` | `PulseNode` | `触发` (Trigger)<br>`状态` (Bool) | `脉冲触发时` (Trigger) | *(None)* | **Omitted (Optimizer-internal)** | *(None)* |
| `RandomTriggerNode` | `RandomTriggerNode` | `触发` (Trigger)<br>`触发数量` (Int)<br>`重复触发` (Bool) | `触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Random\random_ext.py`<br>**nodes.py:** `random_trigger()` |
| `RepeatUntilNode` | `RepeatUntilNode` | `触发` (Trigger)<br>`条件` (Bool)<br>`间隔秒数` (Float)<br>`最多检查次数` (Int) | `完成` (Trigger)<br>`超时` (Trigger)<br>`失败` (Trigger)<br>`每次循环` (Trigger) | *(None)* | **Omitted (Optimizer-internal)** | *(None)* |
| `ToggleCycleNode` | `ToggleCycleNode` | `触发` (Trigger)<br>`周期间隔` (Float) | `周期事件` (Trigger)<br>`切换开始时` (Trigger)<br>`切换关闭时` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Time\time_ext.py`<br>**nodes.py:** `toggle_cycle_node()` |
| `ToggleNode` | `ToggleNode` | `触发` (Trigger) | `状态` (Bool)<br>`状态改变时` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`<br>**nodes.py:** `toggle_node()` |
| `WaitNode` | `WaitNode` | `触发` (Trigger)<br>`等待时间` (Float) | `触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Time\time_ext.py`<br>**nodes.py:** `wait_node()` |
| `WaitUntilNode` | `WaitUntilNode` | `触发` (Trigger)<br>`条件` (Bool)<br>`间隔秒数` (Float)<br>`最多检查次数` (Int) | `完成` (Trigger)<br>`超时` (Trigger)<br>`失败` (Trigger) | *(None)* | **Omitted (Optimizer-internal)** | *(None)* |

### MapFunction (14 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `ChangeEventMapNode` | `ChangeEventMapNode` | `触发` (Trigger) | `完成` (Trigger)<br>`失败` (Trigger)<br>`失败原因` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `change_event_map()` |
| `ChangeEventMusicNode` | `ChangeEventMusicNode` | `触发` (Trigger) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `change_event_music()` |
| `CreateCherryExplodeNode` | `CreateCherryExplodeNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int)<br>`伤害值` (Float) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_cherry_explode()` |
| `CreateCraterNode` | `CreateCraterNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_crater()` |
| `CreateDoomShroomEffectNode` | `CreateDoomShroomEffectNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int)<br>`伤害值` (Float)<br>`创建弹坑` (Bool) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_doom_shroom_effect()` |
| `CreateIceBlockNode` | `CreateIceBlockNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int)<br>`冻住的植物` (PlantType) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_ice_block()` |
| `CreateIceShroomEffectNode` | `CreateIceShroomEffectNode` | `触发` (Trigger)<br>`冻结时间` (Float) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_ice_shroom_effect()` |
| `CreateJalapenoEffectNode` | `CreateJalapenoEffectNode` | `触发` (Trigger)<br>`行` (Int)<br>`伤害值` (Float) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_jalapeno_effect()` |
| `CreateLadderNode` | `CreateLadderNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_ladder()` |
| `CreateZombieExplodeNode` | `CreateZombieExplodeNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `create_zombie_explode()` |
| `DeleteGridItemsNode` | `DeleteGridItemsNode` | `触发` (Trigger)<br>`行` (Int)<br>`列` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`删除数量` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `delete_grid_items()` |
| `RemoveTravelEntryNode` | `RemoveTravelEntryNode` | `触发` (Trigger)<br>`名称或编号` (String) | `完成` (Trigger)<br>`失败` (Trigger)<br>`已移除` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `remove_travel_entry()` |
| `SetWaveCountdownPausedNode` | `SetWaveCountdownPausedNode` | `触发` (Trigger)<br>`暂停` (Bool) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\game.py`<br>**nodes.py:** `set_wave_countdown_paused()` |
| `SetZombieHouseRuleNode` | `SetZombieHouseRuleNode` | `触发` (Trigger)<br>`进家失败` (Bool) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `set_zombie_house_rule()` |

### ObjectBinding (4 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BindPlantNode` | `BindPlantNode` | `触发` (Trigger)<br>`植物` (Plant) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `bind_plant()` |
| `BindZombieNode` | `BindZombieNode` | `触发` (Trigger)<br>`僵尸` (Zombie) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `bind_zombie()` |
| `GetBoundPlantNode` | `GetBoundPlantNode` | *(None)* | `植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `get_bound_plant()` |
| `GetBoundZombieNode` | `GetBoundZombieNode` | *(None)* | `僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `get_bound_zombie()` |

### ObjectOperation (7 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BindObjectNode` | `BindObjectNode` | `触发` (Trigger)<br>`名称` (String)<br>`对象` (GameObject) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `bind_object()` |
| `CreateEventObjectNode` | `CreateEventObjectNode` | `触发` (Trigger)<br>`名称` (String)<br>`位置` (Vector3)<br>`图标植物` (PlantType) | `完成` (Trigger)<br>`失败` (Trigger)<br>`对象` (GameObject) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `create_event_object()` |
| `DestroyEventObjectNode` | `DestroyEventObjectNode` | `触发` (Trigger)<br>`对象` (GameObject) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `destroy_event_object()` |
| `GetMouseWorldPositionNode` | `GetMouseWorldPositionNode` | *(None)* | `坐标` (Vector3)<br>`行` (Int)<br>`列` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `get_mouse_world_position()` |
| `GetObjectTransformNode` | `GetObjectTransformNode` | `对象` (GameObject) | `位置` (Vector3)<br>`大小` (Vector3)<br>`存在` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `get_object_transform()` |
| `MakeVector3Node` | `MakeVector3Node` | `X` (Float)<br>`Y` (Float)<br>`Z` (Float) | `坐标` (Vector3) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `make_vector3()` |
| `SetEventObjectTransformNode` | `SetEventObjectTransformNode` | `触发` (Trigger)<br>`对象` (GameObject)<br>`位置` (Vector3)<br>`大小倍率` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `set_event_object_transform()` |

### PlantFunction (33 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `ComparePlantTypeNode` | `ComparePlantTypeNode` | `植物类型A` (PlantType)<br>`植物类型B` (PlantType) | `相同` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`<br>**nodes.py:** `compare_plant_type()` |
| `CreatePlantCardNode` | `CreatePlantCardNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int)<br>`植物类型` (PlantType) | `创建成功` (Trigger)<br>`植物类型` (PlantType) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `create_plant_card()` |
| `CursePlantNode` | `CursePlantNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`诅咒值` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `curse_plant()` |
| `DamagePlantNode` | `DamagePlantNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`伤害值` (Float) | `伤害完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `damage_plant()` |
| `DiePlantNode` | `DiePlantNode` | `触发` (Trigger)<br>`植物` (Plant) | `死亡完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `die_plant()` |
| `FeedGoldenBeanNode` | `FeedGoldenBeanNode` | `触发` (Trigger)<br>`植物` (Plant) | `完成` (Trigger)<br>`失败` (Trigger)<br>`已生效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `feed_golden_bean()` |
| `ForEachPlantNode` | `ForEachPlantNode` | `触发` (Trigger)<br>`植物列表` (PlantList) | `循环体` (Trigger)<br>`当前植物` (Plant)<br>`当前索引` (Int)<br>`循环完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\loops.py`, `Lawn\lawnf.py`<br>**nodes.py:** `for_each_plant()` |
| `ForEachPlantTypeNode` | `ForEachPlantTypeNode` | `触发` (Trigger)<br>`植物类型列表` (PlantTypeList) | `循环体` (Trigger)<br>`当前类型` (PlantType)<br>`当前索引` (Int)<br>`循环完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\loops.py`, `Entity\plant_type_list.py`<br>**nodes.py:** `for_each_plant_type()` |
| `GetAllPlantsNode` | `GetAllPlantsNode` | *(None)* | `全部植物` (PlantList) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `get_all_plants()` |
| `GetPlantAttackSpeedNode` | `GetPlantAttackSpeedNode` | `植物` (Plant) | `倍率` (Float)<br>`攻击间隔` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `get_plant_attack_speed()` |
| `GetPlantAttributeCountdownNode` | `GetPlantAttributeCountdownNode` | `植物` (Plant) | `剩余秒数` (Float)<br>`最大秒数` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `get_plant_attribute_countdown()` |
| `GetPlantBasicComponentsNode` | `GetPlantBasicComponentsNode` | `植物类型` (PlantType) | `植物类型列表` (PlantTypeList) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `get_plant_basic_components()` |
| `GetPlantsInCellNode` | `GetPlantsInCellNode` | `行` (Int)<br>`列` (Int) | `植物列表` (PlantList) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `get_plants_in_cell()` |
| `GetPlantsOnLayerNode` | `GetPlantsOnLayerNode` | *(None)* | `植物列表` (PlantList) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `get_plants_on_layer()` |
| `GetRandomPlantTypeNode` | `GetRandomPlantTypeNode` | `植物类型列表` (PlantTypeList) | `随机植物类型` (PlantType) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `get_random_plant_type()` |
| `GivePlantShieldNode` | `GivePlantShieldNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`护盾值` (Float) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `give_plant_shield()` |
| `HealPlantNode` | `HealPlantNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`回血量` (Float) | `回血成功` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `heal_plant()` |
| `MergePlantTypeListsNode` | `MergePlantTypeListsNode` | `列表A` (PlantTypeList)<br>`列表B` (PlantTypeList) | `合并列表` (PlantTypeList)<br>`列表长度` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`<br>**nodes.py:** `merge_plant_type_lists()` |
| `ModifyPlantAttackNode` | `ModifyPlantAttackNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`攻击力加成x100%` (Float) | `修改成功` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `modify_plant_attack()` |
| `ModifyPlantHealthNode` | `ModifyPlantHealthNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`血量加成x100%` (Float) | `修改成功` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `modify_plant_health()` |
| `MovePlantNode` | `MovePlantNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`列` (Int)<br>`行` (Int)<br>`强制` (Bool) | `移动成功` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `move_plant()` |
| `MultiPlantTypeListNode` | `MultiPlantTypeListNode` | *(None)* | `植物类型列表` (PlantTypeList) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`<br>**nodes.py:** `multi_plant_type_list()` |
| `PlantSplitNode` | `PlantSplitNode` | `植物` (Plant) | `列` (Int)<br>`行` (Int)<br>`植物类型` (PlantType)<br>`植物血量` (Float)<br>`属性倒计时` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `plant_split()` |
| `PlantTypeValueNode` | `PlantTypeValueNode` | *(None)* | `植物类型` (PlantType) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`, `Lawn\lawnf.py`, `Spawner\spawner.py`, `UI\in_game_ui.py`<br>**nodes.py:** `plant_type_value()` |
| `RemovePlantTypeNode` | `RemovePlantTypeNode` | `植物类型列表` (PlantTypeList)<br>`要删除的类型` (PlantType) | `结果列表` (PlantTypeList)<br>`是否成功` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`<br>**nodes.py:** `remove_plant_type()` |
| `SetPlantAttackIntervalNode` | `SetPlantAttackIntervalNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`秒数` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `set_plant_attack_interval()` |
| `SetPlantAttackSpeedNode` | `SetPlantAttackSpeedNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`倍率` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `set_plant_attack_speed()` |
| `SetPlantAttributeCountdownNode` | `SetPlantAttributeCountdownNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`剩余秒数` (Float)<br>`最大秒数` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `set_plant_attribute_countdown()` |
| `SetPlantNode` | `SetPlantNode` | `触发` (Trigger)<br>`列` (Int)<br>`行` (Int)<br>`植物编号` (PlantType)<br>`强制种植` (Bool) | `创建成功` (Trigger)<br>`创建失败` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Spawner\spawner.py`<br>**nodes.py:** `set_plant()` |
| `SilencePlantNode` | `SilencePlantNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`秒数` (Float)<br>`强制` (Bool) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `silence_plant()` |
| `SinglePlantTypeListNode` | `SinglePlantTypeListNode` | *(None)* | `植物类型列表` (PlantTypeList) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`<br>**nodes.py:** `single_plant_type_list()` |
| `TryPlantSuperSkillNode` | `TryPlantSuperSkillNode` | `触发` (Trigger)<br>`植物` (Plant) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `try_plant_super_skill()` |
| `UpgradeEventPlantNode` | `UpgradeEventPlantNode` | `触发` (Trigger)<br>`植物` (Plant)<br>`目标等级` (Int)<br>`星辉` (Bool) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `upgrade_event_plant()` |

### RewardOption (3 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TypedChoiceMenuNode` | `TypedChoiceMenuNode` | `触发` (Trigger)<br>`选项列表` (ChoiceOptions)<br>`可刷新` (Bool)<br>`刷新次数` (Int)<br>`可取消` (Bool)<br>`窗口数量` (Int) | `退出时触发` (Trigger)<br>`刷新时触发` (Trigger) | *(None)* | **Omitted (Duplicate of MultipleChoiceMenu)** | *(None)* |
| `TypedChoiceMergeNode` | `TypedChoiceMergeNode` | `列表1` (ChoiceOptions)<br>`列表2` (ChoiceOptions) | `合并列表` (ChoiceOptions) | *(None)* | **Omitted (Duplicate of MultipleChoiceMenu)** | *(None)* |
| `TypedChoiceOptionNode` | `TypedChoiceOptionNode` | `标题` (String)<br>`描述` (String)<br>`植物类型` (PlantType)<br>`僵尸类型` (ZombieType) | `选项列表` (ChoiceOptions)<br>`选项被点击` (Trigger) | *(None)* | **Omitted (Duplicate of MultipleChoiceMenu)** | *(None)* |

### Trigger (16 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `OnBoardStartNode` | `OnBoardStartNode` | *(None)* | `触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Time\time_ext.py`, `Triggers\triggers.py`, `Variables\string_var.py`, `Variables\variables.py`<br>**nodes.py:** `on_board_start()` |
| `OnGameStartNode` | `OnGameStartNode` | *(None)* | `触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Time\time_ext.py`, `Triggers\triggers.py`<br>**nodes.py:** `on_game_start()` |
| `OnKeyPressNode` | `OnKeyPressNode` | *(None)* | `触发` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_key_press()` |
| `OnMouseClickNode` | `OnMouseClickNode` | *(None)* | `触发` (Trigger)<br>`行` (Int)<br>`列` (Int)<br>`手上的物品` (ToolType)<br>`是左键` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Input\mouse_ext.py`, `Triggers\triggers.py`<br>**nodes.py:** `on_mouse_click()` |
| `OnPlantClickNode` | `OnPlantClickNode` | *(None)* | `触发` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_plant_click()` |
| `OnPlantCreateNode` | `OnPlantCreateNode` | *(None)* | `触发` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_plant_create()` |
| `OnPlantDeathCompleteNode` | `OnPlantDeathCompleteNode` | *(None)* | `触发` (Trigger)<br>`植物` (Plant)<br>`死亡原因` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_plant_death_complete()` |
| `OnPlantDieNode` | `OnPlantDieNode` | *(None)* | `触发` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_plant_die()` |
| `OnPlantMixedNode` | `OnPlantMixedNode` | *(None)* | `触发` (Trigger)<br>`植物` (Plant) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_plant_mixed()` |
| `OnWaveClearedNode` | `OnWaveClearedNode` | *(None)* | `触发` (Trigger)<br>`波次` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_wave_cleared()` |
| `OnWorldPlantEffectNode` | `OnWorldPlantEffectNode` | *(None)* | `触发` (Trigger)<br>`行` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_world_plant_effect()` |
| `OnZombieClickNode` | `OnZombieClickNode` | *(None)* | `触发` (Trigger)<br>`僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_zombie_click()` |
| `OnZombieDieNode` | `OnZombieDieNode` | *(None)* | `触发` (Trigger)<br>`僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_zombie_die()` |
| `OnZombieHealthBelowNode` | `OnZombieHealthBelowNode` | *(None)* | `触发` (Trigger)<br>`僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_zombie_health_below()` |
| `OnZombieSpawnNode` | `OnZombieSpawnNode` | *(None)* | `触发` (Trigger)<br>`僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Triggers\triggers.py`<br>**nodes.py:** `on_zombie_spawn()` |
| `WaveEventNode` | `WaveEventNode` | *(None)* | `触发` (Trigger)<br>`波次` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Game\game.py`, `Triggers\triggers.py`<br>**nodes.py:** `on_wave()`, `wave_event()` |

### TypeConvert (20 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AsciiToStringNode` | `AsciiToStringNode` | `ASCII码` (Int) | `字符串` (String)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `ascii_to_string()` |
| `FloatToBoolNode` | `FloatToBoolNode` | `数值` (Float) | `布尔值` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `float_to_bool()` |
| `FloatToIntNode` | `FloatToIntNode` | `浮点数` (Float) | `整数` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`, `Variables\variables.py`<br>**nodes.py:** `float_to_int()` |
| `FloatToStringNode` | `FloatToStringNode` | `数值` (Float)<br>`小数位数` (Int) | `字符串` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`, `Variables\variables.py`<br>**nodes.py:** `float_to_string()` |
| `IntToBoolNode` | `IntToBoolNode` | `数值` (Int) | `布尔值` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `int_to_bool()` |
| `IntToFloatNode` | `IntToFloatNode` | `整数` (Int) | `浮点数` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`, `Variables\variables.py`<br>**nodes.py:** `int_to_float()` |
| `IntToStringNode` | `IntToStringNode` | `值` (Int) | `字符串` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `int_to_string()` |
| `ObjectToPlantNode` | `ObjectToPlantNode` | `对象` (GameObject) | `植物` (Plant)<br>`存在` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `object_to_plant()` |
| `ObjectToStringNode` | `ObjectToStringNode` | `对象` (GameObject) | `文本` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`, `World\world_object.py`<br>**nodes.py:** `object_to_string()` |
| `ObjectToZombieNode` | `ObjectToZombieNode` | `对象` (GameObject) | `僵尸` (Zombie)<br>`存在` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `World\world_object.py`<br>**nodes.py:** `object_to_zombie()` |
| `PlantToObjectNode` | `PlantToObjectNode` | `植物` (Plant) | `对象` (GameObject) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`<br>**nodes.py:** `plant_to_object()` |
| `PlantTypeToStringNode` | `PlantTypeToStringNode` | `值` (PlantType) | `字符串` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant.py`, `Types\conversions.py`<br>**nodes.py:** `plant_type_to_string()` |
| `StringToAsciiNode` | `StringToAsciiNode` | `字符串` (String)<br>`索引` (Int) | `ASCII码` (Int)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `string_to_ascii()` |
| `StringToFloatNode` | `StringToFloatNode` | `字符串` (String) | `值` (Float)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `string_to_float()` |
| `StringToIntNode` | `StringToIntNode` | `字符串` (String) | `值` (Int)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `string_to_int()` |
| `StringToObjectNode` | `StringToObjectNode` | `文本` (String) | `对象` (GameObject)<br>`存在` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`, `World\world_object.py`<br>**nodes.py:** `string_to_object()` |
| `StringToPlantTypeNode` | `StringToPlantTypeNode` | `字符串` (String) | `值` (PlantType)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `string_to_plant_type()` |
| `StringToZombieTypeNode` | `StringToZombieTypeNode` | `字符串` (String) | `值` (ZombieType)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Types\conversions.py`<br>**nodes.py:** `string_to_zombie_type()` |
| `ZombieToObjectNode` | `ZombieToObjectNode` | `僵尸` (Zombie) | `对象` (GameObject) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `zombie_to_object()` |
| `ZombieTypeToStringNode` | `ZombieTypeToStringNode` | `值` (ZombieType) | `字符串` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`, `Types\conversions.py`<br>**nodes.py:** `zombie_type_to_string()` |

### Variables/Boolean (3 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BoolVariableNode` | `BoolVariableNode` | *(None)* | `变量` (BoolVariable) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `bool_variable()` |
| `GetBoolVariableValueNode` | `GetBoolVariableValueNode` | `变量` (BoolVariable) | `值` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `get_bool_variable_value()` |
| `SetBoolVariableValueNode` | `SetBoolVariableValueNode` | `触发` (Trigger)<br>`变量` (BoolVariable)<br>`新值` (Bool) | `变量` (BoolVariable)<br>`完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `set_bool_variable_value()` |

### Variables/Float (4 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FloatVariableArithmeticNode` | `FloatVariableArithmeticNode` | `触发` (Trigger)<br>`变量` (FloatVariable)<br>`操作数` (Float) | `完成` (Trigger)<br>`失败` (Trigger)<br>`变量` (FloatVariable)<br>`结果` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `float_variable_arithmetic()` |
| `FloatVariableNode` | `FloatVariableNode` | *(None)* | `变量` (FloatVariable) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `float_variable()` |
| `GetFloatVariableValueNode` | `GetFloatVariableValueNode` | `变量` (FloatVariable) | `值` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `get_float_variable_value()` |
| `SetFloatVariableValueNode` | `SetFloatVariableValueNode` | `触发` (Trigger)<br>`变量` (FloatVariable)<br>`新值` (Float) | `变量` (FloatVariable)<br>`完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `set_float_variable_value()` |

### Variables/Integer (4 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GetIntVariableValueNode` | `GetIntVariableValueNode` | `变量` (IntVariable) | `值` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `get_int_variable_value()` |
| `IntVariableArithmeticNode` | `IntVariableArithmeticNode` | `触发` (Trigger)<br>`变量` (IntVariable)<br>`操作数` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`变量` (IntVariable)<br>`结果` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `int_variable_arithmetic()` |
| `IntVariableNode` | `IntVariableNode` | *(None)* | `变量` (IntVariable) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `int_variable()` |
| `SetIntVariableValueNode` | `SetIntVariableValueNode` | `触发` (Trigger)<br>`变量` (IntVariable)<br>`新值` (Int) | `变量` (IntVariable)<br>`完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\variables.py`<br>**nodes.py:** `set_int_variable_value()` |

### Variables/List (41 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AppendBoolListNode` | `AppendBoolListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Bool) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `AppendFloatListNode` | `AppendFloatListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Float) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `AppendObjectListNode` | `AppendObjectListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (GameObject) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `AppendPlantTypeListNode` | `AppendPlantTypeListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (PlantType) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `AppendStringListNode` | `AppendStringListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (String) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `AppendZombieTypeListNode` | `AppendZombieTypeListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (ZombieType) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`<br>**nodes.py:** `append_zombie_type_list()` |
| `ClearListValuesNode` | `ClearListValuesNode` | `触发` (Trigger)<br>`列表` (ListVariable) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`<br>**nodes.py:** `clear_list_values()` |
| `CopyListValuesNode` | `CopyListValuesNode` | `触发` (Trigger)<br>`源列表` (ListVariable)<br>`目标列表` (ListVariable) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `FindBoolListValueNode` | `FindBoolListValueNode` | `列表` (ListVariable)<br>`值` (Bool) | `索引` (Int)<br>`包含` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `FindFloatListValueNode` | `FindFloatListValueNode` | `列表` (ListVariable)<br>`值` (Float) | `索引` (Int)<br>`包含` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `FindIntListValueNode` | `FindIntListValueNode` | `列表` (ListVariable)<br>`值` (Int) | `索引` (Int)<br>`包含` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `FindObjectListValueNode` | `FindObjectListValueNode` | `列表` (ListVariable)<br>`值` (GameObject) | `索引` (Int)<br>`包含` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `FindPlantTypeListValueNode` | `FindPlantTypeListValueNode` | `列表` (ListVariable)<br>`值` (PlantType) | `索引` (Int)<br>`包含` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `FindStringListValueNode` | `FindStringListValueNode` | `列表` (ListVariable)<br>`值` (String) | `索引` (Int)<br>`包含` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `FindZombieTypeListValueNode` | `FindZombieTypeListValueNode` | `列表` (ListVariable)<br>`值` (ZombieType) | `索引` (Int)<br>`包含` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`<br>**nodes.py:** `find_zombie_type_list_value()` |
| `GetBoolListItemNode` | `GetBoolListItemNode` | `列表` (ListVariable)<br>`索引` (Int) | `值` (Bool)<br>`有效` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `GetFloatListItemNode` | `GetFloatListItemNode` | `列表` (ListVariable)<br>`索引` (Int) | `值` (Float)<br>`有效` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `GetIntListItemNode` | `GetIntListItemNode` | `列表` (ListVariable)<br>`索引` (Int) | `值` (Int)<br>`有效` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `GetListLengthNode` | `GetListLengthNode` | `列表` (ListVariable) | `长度` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`<br>**nodes.py:** `get_list_length()` |
| `GetObjectListItemNode` | `GetObjectListItemNode` | `列表` (ListVariable)<br>`索引` (Int) | `值` (GameObject)<br>`有效` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `GetPlantTypeListItemNode` | `GetPlantTypeListItemNode` | `列表` (ListVariable)<br>`索引` (Int) | `值` (PlantType)<br>`有效` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `GetStringListItemNode` | `GetStringListItemNode` | `列表` (ListVariable)<br>`索引` (Int) | `值` (String)<br>`有效` (Bool) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `GetZombieTypeListItemNode` | `GetZombieTypeListItemNode` | `列表` (ListVariable)<br>`索引` (Int) | `值` (ZombieType)<br>`有效` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`<br>**nodes.py:** `get_zombie_type_list_item()` |
| `InsertBoolListNode` | `InsertBoolListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Bool)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `InsertFloatListNode` | `InsertFloatListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Float)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `InsertIntListNode` | `InsertIntListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Int)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `InsertObjectListNode` | `InsertObjectListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (GameObject)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `InsertPlantTypeListNode` | `InsertPlantTypeListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (PlantType)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `InsertStringListNode` | `InsertStringListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (String)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `InsertZombieTypeListNode` | `InsertZombieTypeListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (ZombieType)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Available in nodes.py (not in Extensions)** | **nodes.py:** `insert_zombie_type_list()` |
| `AppendIntListNode` | `AppendIntListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `ListVariableNode` | `ListVariableNode` | *(None)* | *(None)* | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`<br>**nodes.py:** `list_variable()` |
| `PlantTypeListStorageNode` | `PlantTypeListStorageNode` | `触发` (Trigger)<br>`列表` (PlantTypeList)<br>`植物类型` (PlantType) | `当前列表` (PlantTypeList)<br>`列表长度` (Int)<br>`完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\plant_type_list.py`<br>**nodes.py:** `plant_type_list_storage()` |
| `RemoveListItemNode` | `RemoveListItemNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`<br>**nodes.py:** `remove_list_item()` |
| `ReplaceBoolListNode` | `ReplaceBoolListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Bool)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `ReplaceFloatListNode` | `ReplaceFloatListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Float)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `ReplaceIntListNode` | `ReplaceIntListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (Int)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `ReplaceObjectListNode` | `ReplaceObjectListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (GameObject)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `ReplacePlantTypeListNode` | `ReplacePlantTypeListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (PlantType)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `ReplaceStringListNode` | `ReplaceStringListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (String)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Deferred (List variable node)** | *(None)* |
| `ReplaceZombieTypeListNode` | `ReplaceZombieTypeListNode` | `触发` (Trigger)<br>`列表` (ListVariable)<br>`值` (ZombieType)<br>`索引` (Int) | `完成` (Trigger)<br>`失败` (Trigger)<br>`列表` (ListVariable) | *(None)* | **Available in nodes.py (not in Extensions)** | **nodes.py:** `replace_zombie_type_list()` |

### Variables/String (3 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GetStringVariableValueNode` | `GetStringVariableValueNode` | `变量` (StringVariable) | `值` (String) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\string_var.py`<br>**nodes.py:** `get_string_variable_value()` |
| `SetStringVariableValueNode` | `SetStringVariableValueNode` | `触发` (Trigger)<br>`变量` (StringVariable)<br>`新值` (String) | `完成` (Trigger)<br>`失败` (Trigger)<br>`变量` (StringVariable) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\string_var.py`<br>**nodes.py:** `set_string_variable_value()` |
| `StringVariableNode` | `StringVariableNode` | *(None)* | `变量` (StringVariable) | *(None)* | **Implemented in Extensions** | **Extensions:** `Variables\string_var.py`<br>**nodes.py:** `string_variable()` |

### ZombieFunction (20 nodes)

| Node Class | IL2CPP Type | Inputs | Outputs | Fields | Status | Extension / nodes.py Mapping |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AddZombieCardNode` | `AddZombieCardNode` | `触发` (Trigger)<br>`僵尸类型` (ZombieType)<br>`价格` (Int)<br>`冷却秒数` (Float)<br>`立即可用` (Bool) | `完成` (Trigger)<br>`失败` (Trigger)<br>`卡牌对象` (GameObject) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `add_zombie_card()` |
| `CompareZombieTypeNode` | `CompareZombieTypeNode` | `僵尸类型A` (ZombieType)<br>`僵尸类型B` (ZombieType) | `相同` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `compare_zombie_type()` |
| `CreateZombieNode` | `CreateZombieNode` | `触发` (Trigger)<br>`行` (Int)<br>`列` (Int)<br>`僵尸类型` (ZombieType)<br>`是否魅惑` (Bool) | `创建成功` (Trigger)<br>`僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Spawner\spawner.py`<br>**nodes.py:** `create_zombie()` |
| `DamageZombieNode` | `DamageZombieNode` | `触发` (Trigger)<br>`僵尸` (Zombie)<br>`伤害值` (Float) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `damage_zombie()` |
| `DeleteZombieCardsNode` | `DeleteZombieCardsNode` | `触发` (Trigger)<br>`僵尸类型` (ZombieType) | `完成` (Trigger)<br>`删除数量` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `delete_zombie_cards()` |
| `ForEachAllZombiesNode` | `ForEachAllZombiesNode` | `触发` (Trigger) | `每次循环` (Trigger)<br>`当前僵尸` (Zombie)<br>`索引` (Int)<br>`完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\loops.py`<br>**nodes.py:** `for_each_all_zombies()` |
| `ForEachZombieNode` | `ForEachZombieNode` | `触发` (Trigger)<br>`僵尸列表` (ZombieList) | `每次循环` (Trigger)<br>`当前僵尸` (Zombie)<br>`索引` (Int)<br>`完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\loops.py`<br>**nodes.py:** `for_each_zombie()` |
| `GetAllZombiesNode` | `GetAllZombiesNode` | *(None)* | `僵尸列表` (ZombieList) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `get_all_zombies()` |
| `GetNearestZombieNode` | `GetNearestZombieNode` | `行` (Int)<br>`列` (Int) | `僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Lawn\lawnf.py`<br>**nodes.py:** `get_nearest_zombie()` |
| `GetZombieStatsNode` | `GetZombieStatsNode` | `僵尸` (Zombie) | `数值` (Float) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `get_zombie_stats()` |
| `GetZombieStatusNode` | `GetZombieStatusNode` | `僵尸` (Zombie) | `数值` (Float)<br>`存在` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `get_zombie_status()` |
| `ModifyZombieHealthNode` | `ModifyZombieHealthNode` | `触发` (Trigger)<br>`僵尸` (Zombie)<br>`血量倍率` (Float) | `修改成功` (Trigger)<br>`僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `modify_zombie_health()` |
| `MoveZombieNode` | `MoveZombieNode` | `触发` (Trigger)<br>`僵尸` (Zombie)<br>`目标列` (Int)<br>`目标行` (Int) | `移动成功` (Trigger)<br>`僵尸` (Zombie) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `move_zombie()` |
| `PlayZombieAnimNode` | `PlayZombieAnimNode` | `触发` (Trigger)<br>`僵尸` (Zombie) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `play_zombie_anim()` |
| `SetZombieCardCooldownNode` | `SetZombieCardCooldownNode` | `触发` (Trigger)<br>`僵尸类型` (ZombieType)<br>`总秒数` (Float)<br>`剩余秒数` (Float) | `完成` (Trigger)<br>`失败` (Trigger)<br>`修改数量` (Int) | *(None)* | **Implemented in Extensions** | **Extensions:** `UI\in_game_ui.py`<br>**nodes.py:** `set_zombie_card_cooldown()` |
| `SetZombieMindControlledNode` | `SetZombieMindControlledNode` | `触发` (Trigger)<br>`僵尸` (Zombie) | `完成` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `set_zombie_mind_controlled()` |
| `SetZombieStatsNode` | `SetZombieStatsNode` | `触发` (Trigger)<br>`僵尸` (Zombie)<br>`数值` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `set_zombie_stats()` |
| `SetZombieStatusNode` | `SetZombieStatusNode` | `触发` (Trigger)<br>`僵尸` (Zombie)<br>`数值` (Float) | `完成` (Trigger)<br>`失败` (Trigger) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `set_zombie_status()` |
| `ZombieSplitNode` | `ZombieSplitNode` | `僵尸` (Zombie) | `列` (Int)<br>`行` (Int)<br>`僵尸类型` (ZombieType)<br>`是否被魅惑` (Bool) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie.py`<br>**nodes.py:** `zombie_split()` |
| `ZombieTypeValueNode` | `ZombieTypeValueNode` | *(None)* | `僵尸类型` (ZombieType) | *(None)* | **Implemented in Extensions** | **Extensions:** `Entity\zombie_type_list.py`, `Spawner\spawner.py`<br>**nodes.py:** `zombie_type_value()` |

