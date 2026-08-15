from .node_base import BaseNode
from .typing import enforce_int, enforce_float, enforce_bool, enforce_string
from .core import ctx

FLOAT_OUTPUT_NODES = {
    "FloatValueNode", "RandomFloatNode", "IntToFloatNode", 
    "AddNode", "SubtractNode", "MultiplyNode", "DivideNode", 
    "GetFloatVariableValueNode", "FloatVariableNode"
}

INT_OUTPUT_NODES = {
    "IntValueNode", "RandomIntNode", "FloatToIntNode", 
    "IntAddNode", "IntSubtractNode", "IntMultiplyNode", 
    "IntDivideNode", "IntModuloNode", "CounterNode", 
    "GetSunAmountNode", "GetIntVariableValueNode", "IntVariableNode"
}

def wire(val, target_id, target_port, enforce_func=None):
    if val is None:
        return
    
    # 1. Safely unwrap Port / Variable wrappers
    if hasattr(val, '_get_primary_port'):
        val = val._get_primary_port() if callable(val._get_primary_port) else val._get_primary_port
    elif hasattr(val, 'value'):
        val = val.value

    # 2. Dynamic Port References
    if isinstance(val, (tuple, list)) and len(val) == 2:
        src, src_port = val
        src_id = src.id if hasattr(src, "id") else src
        node_type = getattr(src, "type", "")
        
        is_float = (node_type in FLOAT_OUTPUT_NODES) or (
            getattr(val, "_is_float_port", lambda: False)() if hasattr(val, "_is_float_port") else False
        )
        is_int = (node_type in INT_OUTPUT_NODES) or not is_float

        if enforce_func == enforce_float:
            if is_int and node_type != "IntToFloatNode":
                from .nodes import int_to_float
                conv = int_to_float(int_val=val)
                src_id, src_port = conv.id, "浮点数"

        elif enforce_func == enforce_int:
            if is_float and node_type != "FloatToIntNode":
                from .nodes import float_to_int
                conv = float_to_int(float_val=val)
                src_id, src_port = conv.id, "整数"

        ctx.add_connection(src_id, src_port, target_id, target_port)
        return

    # 3. Static Primitives
    if enforce_func:
        val_id = enforce_func(val)
        ctx.add_connection(val_id, "值", target_id, target_port)
    elif isinstance(val, bool):
        from .nodes import bool_value
        ctx.add_connection(bool_value(val).id, "值", target_id, target_port)
    elif isinstance(val, int):
        from .nodes import int_value
        ctx.add_connection(int_value(val).id, "值", target_id, target_port)
    elif isinstance(val, float):
        from .nodes import float_value
        ctx.add_connection(float_value(val).id, "值", target_id, target_port)
    elif isinstance(val, str):
        from .nodes import string_value
        ctx.add_connection(string_value(val).id, "值", target_id, target_port)

# ==========================================
# EVENTS
# ==========================================
class on_board_start(BaseNode):
    def __init__(self): super().__init__("OnBoardStartNode", trigger_PortName="触发")

class on_wave(BaseNode):
    def __init__(self, wave=None):
        super().__init__("WaveEventNode", trigger_PortName="触发", wave_PortName="波次")
        wire(wave, self.id, "波次", enforce_int)

class on_mouse_click(BaseNode):
    def __init__(self): super().__init__("OnMouseClickNode", trigger_PortName="触发", row_PortName="行", column_PortName="列", item_PortName="手上的物品", isLeftButton_PortName="是左键")

class on_key_press(BaseNode):
    def __init__(self, target_key=0): super().__init__("OnKeyPressNode", trigger_PortName="触发", targetKey=target_key)

class on_plant_create(BaseNode):
    def __init__(self): super().__init__("OnPlantCreateNode", trigger_PortName="触发", plant_PortName="植物")

class on_plant_click(BaseNode):
    def __init__(self): super().__init__("OnPlantClickNode", trigger_PortName="触发", plant_PortName="植物")

class on_plant_die(BaseNode):
    def __init__(self): super().__init__("OnPlantDieNode", trigger_PortName="触发", plant_PortName="植物")

class on_zombie_die(BaseNode):
    def __init__(self): super().__init__("OnZombieDieNode", trigger_PortName="触发", zombie_PortName="僵尸")

class on_zombie_spawn(BaseNode):
    def __init__(self): super().__init__("OnZombieSpawnNode", trigger_PortName="触发", zombie_PortName="僵尸")


# ==========================================
# PLANT ACTIONS
# ==========================================
class set_plant(BaseNode):
    def __init__(self, column=None, row=None, plant_type=None, force_plant=None):
        super().__init__("SetPlantNode", trigger_PortName="触发", column_PortName="列", row_PortName="行", plantType_PortName="植物编号", forcePlant_PortName="强制种植", onCreated_PortName="创建成功", onCreateFailed_PortName="创建失败", plant_PortName="植物")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)
        wire(plant_type, self.id, "植物编号", enforce_int)
        wire(force_plant, self.id, "强制种植", enforce_bool)

class move_plant(BaseNode):
    def __init__(self, plant=None, column=None, row=None, force=None):
        super().__init__("MovePlantNode", trigger_PortName="触发", plant_PortName="植物", column_PortName="列", row_PortName="行", force_PortName="强制", onMoved_PortName="移动成功", movedPlant_PortName="植物")
        wire(plant, self.id, "植物")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)
        wire(force, self.id, "强制", enforce_bool)

class heal_plant(BaseNode):
    def __init__(self, plant=None, heal_amount=None):
        super().__init__("HealPlantNode", trigger_PortName="触发", plant_PortName="植物", healAmount_PortName="回血量", onHealed_PortName="回血成功")
        wire(plant, self.id, "植物")
        wire(heal_amount, self.id, "回血量", enforce_float)

class damage_plant(BaseNode):
    def __init__(self, plant=None, damage=None):
        super().__init__("DamagePlantNode", trigger_PortName="触发", plant_PortName="植物", damage_PortName="伤害值")
        wire(plant, self.id, "植物")
        wire(damage, self.id, "伤害值", enforce_float)

class give_plant_shield(BaseNode):
    def __init__(self, plant=None, shield=None):
        super().__init__("GivePlantShieldNode", trigger_PortName="触发", plant_PortName="植物", shieldAmount_PortName="护盾值")
        wire(plant, self.id, "植物")
        wire(shield, self.id, "护盾值", enforce_float)

class modify_plant_attack(BaseNode):
    def __init__(self, plant=None, multiplier=None):
        super().__init__("ModifyPlantAttackNode", trigger_PortName="触发", plant_PortName="植物", multiplier_PortName="攻击力加成x100%", onModified_PortName="修改成功", plantOut_PortName="植物")
        wire(plant, self.id, "植物")
        wire(multiplier, self.id, "攻击力加成x100%", enforce_float)

class modify_plant_health(BaseNode):
    def __init__(self, plant=None, multiplier=None):
        super().__init__("ModifyPlantHealthNode", trigger_PortName="触发", plant_PortName="植物", multiplier_PortName="血量加成x100%", onModified_PortName="修改成功", plantOut_PortName="植物")
        wire(plant, self.id, "植物")
        wire(multiplier, self.id, "血量加成x100%", enforce_float)

class plant_split(BaseNode):
    def __init__(self, plant=None):
        super().__init__("PlantSplitNode", plant_PortName="植物", column_PortName="列", 
                         row_PortName="行", plantType_PortName="植物类型", attributeCountdown_PortName="属性倒计时")
        wire(plant, self.id, "植物")

class get_plants_in_cell(BaseNode):
    def __init__(self, row=None, column=None):
        super().__init__("GetPlantsInCellNode", row_PortName="行", column_PortName="列", plants_PortName="植物列表")
        wire(row, self.id, "行", enforce_int)
        wire(column, self.id, "列", enforce_int)


# ==========================================
# PLANT LISTS & TYPES
# ==========================================
class for_each_plant(BaseNode):
    def __init__(self, plant_list=None):
        super().__init__("ForEachPlantNode", trigger_PortName="触发", plantList_PortName="植物列表", loopBody_PortName="循环体", currentPlant_PortName="当前植物", currentIndex_PortName="当前索引", onCompleted_PortName="循环完成")
        wire(plant_list, self.id, "植物列表")

class for_each_plant_type(BaseNode):
    def __init__(self, type_list=None):
        super().__init__("ForEachPlantTypeNode", trigger_PortName="触发", plantTypeList_PortName="植物类型列表", loopBody_PortName="循环体", currentPlantType_PortName="当前类型", currentIndex_PortName="当前索引", onCompleted_PortName="循环完成")
        wire(type_list, self.id, "植物类型列表")

class plant_type_value(BaseNode):
    def __init__(self, val=-1): super().__init__("PlantTypeValueNode", value=val, value_PortName="植物类型")

class compare_plant_type(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("ComparePlantTypeNode", plantTypeA_PortName="植物类型A", plantTypeB_PortName="植物类型B", equal_PortName="相同")
        wire(a, self.id, "植物类型A")
        wire(b, self.id, "植物类型B")

class single_plant_type_list(BaseNode):
    def __init__(self, plant_type=-1): super().__init__("SinglePlantTypeListNode", plantType=plant_type, plantTypeList_PortName="植物类型列表")

class plant_type_list_storage(BaseNode):
    def __init__(self, list_in=None, plant_type=None, op=0, init_empty=True):
        super().__init__("PlantTypeListStorageNode", trigger_PortName="触发", list_PortName="列表", plantType_PortName="植物类型", currentList_PortName="当前列表", count_PortName="列表长度", onComplete_PortName="完成", operation=op, initializeEmpty=init_empty)
        wire(list_in, self.id, "列表")
        wire(plant_type, self.id, "植物类型", enforce_int)

class merge_plant_type_lists(BaseNode):
    def __init__(self, list_a=None, list_b=None):
        super().__init__("MergePlantTypeListsNode", listA_PortName="列表A", listB_PortName="列表B", mergedList_PortName="合并列表", count_PortName="列表长度")
        wire(list_a, self.id, "列表A")
        wire(list_b, self.id, "列表B")

class get_random_plant_type(BaseNode):
    def __init__(self, list_in=None):
        super().__init__("GetRandomPlantTypeNode", list_PortName="植物类型列表", result_PortName="随机植物类型")
        wire(list_in, self.id, "植物类型列表")

class remove_plant_type(BaseNode):
    def __init__(self, list_in=None, plant_type=None):
        super().__init__("RemovePlantTypeNode", list_PortName="植物类型列表", plantType_PortName="要删除的类型", resultList_PortName="结果列表", success_PortName="是否成功")
        wire(list_in, self.id, "植物类型列表")
        wire(plant_type, self.id, "要删除的类型", enforce_int)


# ==========================================
# ZOMBIE ACTIONS
# ==========================================
class create_zombie(BaseNode):
    def __init__(self, row=None, column=None, zombie_type=None, mind_controlled=None):
        super().__init__("CreateZombieNode", trigger_PortName="触发", row_PortName="行", column_PortName="列", zombieType_PortName="僵尸类型", isMindControlled_PortName="是否魅惑", onCreated_PortName="创建成功", zombie_PortName="僵尸")
        wire(row, self.id, "行", enforce_int)
        wire(column, self.id, "列", enforce_int)
        wire(zombie_type, self.id, "僵尸类型", enforce_int)
        wire(mind_controlled, self.id, "是否魅惑", enforce_bool)

class damage_zombie(BaseNode):
    def __init__(self, zombie=None, damage=None):
        super().__init__("DamageZombieNode", trigger_PortName="触发", zombie_PortName="僵尸", damage_PortName="伤害值")
        wire(zombie, self.id, "僵尸")
        wire(damage, self.id, "伤害值", enforce_float)

class set_zombie_mind_controlled(BaseNode):
    def __init__(self, zombie=None):
        super().__init__("SetZombieMindControlledNode", trigger_PortName="触发", zombie_PortName="僵尸")
        wire(zombie, self.id, "僵尸")

class get_nearest_zombie(BaseNode):
    def __init__(self, row=None, column=None):
        super().__init__("GetNearestZombieNode", row_PortName="行", column_PortName="列", zombie_PortName="僵尸")
        wire(row, self.id, "行", enforce_int)
        wire(column, self.id, "列", enforce_int)

class modify_zombie_health(BaseNode):
    def __init__(self, zombie=None, ratio=None):
        super().__init__("ModifyZombieHealthNode", trigger_PortName="触发", zombie_PortName="僵尸", ratio_PortName="血量倍率", onModified_PortName="修改成功", zombieOut_PortName="僵尸")
        wire(zombie, self.id, "僵尸")
        wire(ratio, self.id, "血量倍率", enforce_float)

class zombie_split(BaseNode):
    def __init__(self, zombie=None):
        super().__init__("ZombieSplitNode", zombie_PortName="僵尸", column_PortName="列", row_PortName="行", zombieType_PortName="僵尸类型", isHypnotized_PortName="是否被魅惑")
        wire(zombie, self.id, "僵尸")

class zombie_type_value(BaseNode):
    def __init__(self, val=0): super().__init__("ZombieTypeValueNode", value=val, value_PortName="僵尸类型")

class compare_zombie_type(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("CompareZombieTypeNode", zombieTypeA_PortName="僵尸类型A", zombieTypeB_PortName="僵尸类型B", equal_PortName="相同")
        wire(a, self.id, "僵尸类型A")
        wire(b, self.id, "僵尸类型B")


# ==========================================
# GAME & UI
# ==========================================
class show_text(BaseNode):
    def __init__(self, text=None, duration=None, display_text="示例文本", def_duration=3.0):
        super().__init__("ShowTextNode", trigger_PortName="触发", text_PortName="文本", duration_PortName="持续时间", displayText=display_text, duration=def_duration)
        wire(text, self.id, "文本", enforce_string)
        wire(duration, self.id, "持续时间", enforce_float)

class get_travel_entry(BaseNode):
    """Deprecated"""
    def __init__(self, buff_type=1, entry_index=0): super().__init__("GetTravelEntryNode", trigger_PortName="触发", buffType=buff_type, entryIndex=entry_index)

class create_grave(BaseNode):
    def __init__(self, column=None, row=None):
        super().__init__("CreateGraveNode", trigger_PortName="触发", column_PortName="列", row_PortName="行")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)

class add_sun(BaseNode):
    def __init__(self, amount=None):
        super().__init__("GetSunNode", trigger_PortName="触发", sunAmount_PortName="阳光数量")
        wire(amount, self.id, "阳光数量", enforce_int)

class use_sun(BaseNode):
    def __init__(self, amount=None):
        super().__init__("UseSunNode", trigger_PortName="触发", sunAmount_PortName="阳光数量", onSuccess_PortName="消耗成功", onFailed_PortName="阳光不足")
        wire(amount, self.id, "阳光数量", enforce_int)

class add_money(BaseNode):
    def __init__(self, amount=None):
        super().__init__("GetMoneyNode", trigger_PortName="触发", moneyAmount_PortName="金币数量")
        wire(amount, self.id, "金币数量", enforce_int)

class use_money(BaseNode):
    def __init__(self, amount=None):
        super().__init__("UseMoneyNode", trigger_PortName="触发", moneyAmount_PortName="金币数量", onSuccess_PortName="消耗成功", onFailed_PortName="金币不足")
        wire(amount, self.id, "金币数量", enforce_int)

class game_over(BaseNode):
    def __init__(self, reason=None):
        super().__init__("GameOverNode", trigger_PortName="触发", reason_PortName="失败原因")
        wire(reason, self.id, "失败原因", enforce_string)

class game_win(BaseNode):
    def __init__(self): super().__init__("GameWinNode", trigger_PortName="触发")

class show_multiple_choice_menu(BaseNode):
    def __init__(self, options=None, refresh=False, ref_count=3, cancel=True, win_count=3):
        super().__init__("ShowMultipleChoiceMenuNode", trigger_PortName="触发", options_PortName="选项列表", refreshable_PortName="可刷新", refreshCount_PortName="刷新次数", cancelable_PortName="可取消", windowCount_PortName="窗口数量", actionOnExit_PortName="退出时触发", actionOnRefresh_PortName="刷新时触发", refreshable=refresh, refreshCount=ref_count, cancelable=cancel, windowCount=win_count)
        wire(options, self.id, "选项列表")

class add_multiple_choice_option(BaseNode):
    def __init__(self, list_in=None, title_val="选项", desc_val="选项描述", p_type=254, z_type=-1):
        super().__init__("AddMultipleChoiceOptionNode", list_PortName="选项列表", title_PortName="标题", description_PortName="描述", plantType_PortName="植物类型", zombieType_PortName="僵尸类型", optionSelected_PortName="选项被点击", title=title_val, description=desc_val, plantType=p_type, zombieType=z_type)
        wire(list_in, self.id, "选项列表")

class merge_multiple_choice_option_lists(BaseNode):
    def __init__(self, list1=None, list2=None):
        super().__init__("MergeMultipleChoiceOptionListsNode", list1_PortName="列表1", list2_PortName="列表2")
        wire(list1, self.id, "列表1")
        wire(list2, self.id, "列表2")

class delete_card_by_type(BaseNode):
    def __init__(self, plant_type=None, type_val=0):
        super().__init__("DeleteCardByTypeNode", trigger_PortName="触发", plantType_PortName="植物类型", completed_PortName="完成", plantType=type_val)
        wire(plant_type, self.id, "植物类型", enforce_int)

class create_plant_card(BaseNode):
    def __init__(self, column=None, row=None, plant_type=None):
        super().__init__("CreatePlantCardNode", trigger_PortName="触发", column_PortName="列", row_PortName="行", plantType_PortName="植物类型", onCreated_PortName="创建成功", outPlantType_PortName="植物类型")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)
        wire(plant_type, self.id, "植物类型", enforce_int)

class add_plant_card(BaseNode):
    def __init__(self, p_type=None, cd=None, cost=None, default_data=None, type_val=0, cd_val=7.5, cost_val=100, def_val=True):
        super().__init__("AddPlantCardNode", trigger_PortName="触发", plantType_PortName="植物类型", cooldown_PortName="冷却时间", cost_PortName="价格", useDefaultData_PortName="使用默认数据", success_PortName="添加成功", failed_PortName="添加失败", onPlant_PortName="种植时触发", plantedPlant_PortName="种植的植物", plantType=type_val, cooldown=cd_val, cost=cost_val, useDefaultData=def_val)
        wire(p_type, self.id, "植物类型", enforce_int)
        wire(cd, self.id, "冷却时间", enforce_float)
        wire(cost, self.id, "价格", enforce_int)
        wire(default_data, self.id, "使用默认数据", enforce_bool)


# ==========================================
# EFFECTS
# ==========================================
class create_ice_shroom_effect(BaseNode):
    def __init__(self, duration=None):
        super().__init__("CreateIceShroomEffectNode", trigger_PortName="触发", duration_PortName="冻结时间")
        wire(duration, self.id, "冻结时间", enforce_float)

class create_jalapeno_effect(BaseNode):
    def __init__(self, row=None, damage=None):
        super().__init__("CreateJalapenoEffectNode", trigger_PortName="触发", row_PortName="行", damage_PortName="伤害值")
        wire(row, self.id, "行", enforce_int)
        wire(damage, self.id, "伤害值", enforce_float)

class create_doom_shroom_effect(BaseNode):
    def __init__(self, column=None, row=None, damage=None, set_pit=None):
        super().__init__("CreateDoomShroomEffectNode", trigger_PortName="触发", column_PortName="列", row_PortName="行", damage_PortName="伤害值", setPit_PortName="创建弹坑")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)
        wire(damage, self.id, "伤害值", enforce_float)
        wire(set_pit, self.id, "创建弹坑", enforce_bool)

class create_cherry_explode(BaseNode):
    def __init__(self, column=None, row=None, damage=None):
        super().__init__("CreateCherryExplodeNode", trigger_PortName="触发", column_PortName="列", row_PortName="行", damage_PortName="伤害值")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)
        wire(damage, self.id, "伤害值", enforce_float)

class create_ladder(BaseNode):
    def __init__(self, column=None, row=None):
        super().__init__("CreateLadderNode", trigger_PortName="触发", column_PortName="列", row_PortName="行")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)

class create_crater(BaseNode):
    def __init__(self, column=None, row=None):
        super().__init__("CreateCraterNode", trigger_PortName="触发", column_PortName="列", row_PortName="行")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)

class create_ice_block(BaseNode):
    def __init__(self, column=None, row=None, plant_type=None):
        super().__init__("CreateIceBlockNode", trigger_PortName="触发", column_PortName="列", row_PortName="行", plantType_PortName="冻住的植物")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)
        wire(plant_type, self.id, "冻住的植物", enforce_int)

class create_zombie_explode(BaseNode):
    def __init__(self, column=None, row=None):
        super().__init__("CreateZombieExplodeNode", trigger_PortName="触发", column_PortName="列", row_PortName="行")
        wire(column, self.id, "列", enforce_int)
        wire(row, self.id, "行", enforce_int)


# ==========================================
# FLOW & LOGIC
# ==========================================
class branch_node(BaseNode):
    def __init__(self, condition=None):
        super().__init__("BranchNode", trigger_PortName="触发", condition_PortName="条件", then_PortName="真（触发）", else_PortName="假（停止）")
        wire(condition, self.id, "条件", enforce_bool)

class wait_node(BaseNode):
    def __init__(self, duration=None):
        super().__init__("WaitNode", trigger_PortName="触发", duration_PortName="等待时间", output_PortName="触发")
        wire(duration, self.id, "等待时间", enforce_float)

class for_loop_node(BaseNode):
    def __init__(self, count=None):
        super().__init__("ForLoopNode", trigger_PortName="触发", count_PortName="循环次数", output_PortName="循环体", index_PortName="当前索引")
        wire(count, self.id, "循环次数", enforce_int)

class toggle_cycle_node(BaseNode):
    def __init__(self, interval=None):
        super().__init__("ToggleCycleNode", trigger_PortName="触发", interval_PortName="周期间隔", cycle_PortName="周期事件", onEnable_PortName="切换开始时", onDisable_PortName="切换关闭时")
        wire(interval, self.id, "周期间隔", enforce_float)

class toggle_node(BaseNode):
    def __init__(self, initial_state=False):
        super().__init__(
            "ToggleNode", 
            trigger_PortName="触发", 
            state_PortName="状态", 
            onChanged_PortName="状态改变时",
            state=bool(initial_state)
        )

class pulse_node(BaseNode):
    def __init__(self, state=None):
        super().__init__("PulseNode", trigger_PortName="触发", state_PortName="状态", onPulse_PortName="脉冲触发时")
        wire(state, self.id, "状态", enforce_bool)

class counter_node(BaseNode):
    def __init__(self, reset=None, start_val=0):
        super().__init__("CounterNode", trigger_PortName="触发", shouldReset_PortName="是否重置", count_PortName="计数", onCount_PortName="计数完成", startValue=start_val)
        wire(reset, self.id, "是否重置", enforce_bool)


# ==========================================
# MATH & COMPARISON
# ==========================================
class not_node(BaseNode):
    def __init__(self, inp=None):
        super().__init__("NotNode", input_PortName="输入", output_PortName="输出")
        wire(inp, self.id, "输入", enforce_bool)

class and_node(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("AndNode", a_PortName="条件A", b_PortName="条件B", output_PortName="结果")
        wire(a, self.id, "条件A", enforce_bool)
        wire(b, self.id, "条件B", enforce_bool)

class or_node(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("OrNode", a_PortName="条件A", b_PortName="条件B", output_PortName="结果")
        wire(a, self.id, "条件A", enforce_bool)
        wire(b, self.id, "条件B", enforce_bool)

class compare_int(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("CompareIntNode", valueA_PortName="值A", valueB_PortName="值B", greater_PortName="大于", less_PortName="小于", equal_PortName="等于")
        wire(a, self.id, "值A", enforce_int)
        wire(b, self.id, "值B", enforce_int)

class compare_float(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("CompareFloatNode", valueA_PortName="值A", valueB_PortName="值B", greater_PortName="大于", less_PortName="小于", equal_PortName="等于")
        wire(a, self.id, "值A", enforce_float)
        wire(b, self.id, "值B", enforce_float)

class compare_game_object(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("CompareGameObjectNode", gameObjectA_PortName="对象A", gameObjectB_PortName="对象B", equal_PortName="相同")
        wire(a, self.id, "对象A")
        wire(b, self.id, "对象B")

class add_node(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("AddNode", a_PortName="A", b_PortName="B", result_PortName="结果")
        wire(a, self.id, "A", enforce_float)
        wire(b, self.id, "B", enforce_float)

class subtract_node(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("SubtractNode", a_PortName="被减数", b_PortName="减数", result_PortName="差")
        wire(a, self.id, "被减数", enforce_float)
        wire(b, self.id, "减数", enforce_float)

class multiply_node(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("MultiplyNode", a_PortName="A", b_PortName="B", result_PortName="积")
        wire(a, self.id, "A", enforce_float)
        wire(b, self.id, "B", enforce_float)

class divide_node(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("DivideNode", a_PortName="被除数", b_PortName="除数", result_PortName="商")
        wire(a, self.id, "被除数", enforce_float)
        wire(b, self.id, "除数", enforce_float)

class int_add(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("IntAddNode", a_PortName="A", b_PortName="B", result_PortName="和")
        wire(a, self.id, "A", enforce_int)
        wire(b, self.id, "B", enforce_int)

class int_subtract(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("IntSubtractNode", a_PortName="被减数", b_PortName="减数", result_PortName="差")
        wire(a, self.id, "被减数", enforce_int)
        wire(b, self.id, "减数", enforce_int)

class int_multiply(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("IntMultiplyNode", a_PortName="A", b_PortName="B", result_PortName="积")
        wire(a, self.id, "A", enforce_int)
        wire(b, self.id, "B", enforce_int)

class int_divide(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("IntDivideNode", a_PortName="被除数", b_PortName="除数", result_PortName="商")
        wire(a, self.id, "被除数", enforce_int)
        wire(b, self.id, "除数", enforce_int)

class int_modulo(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("IntModuloNode", a_PortName="被除数", b_PortName="除数", result_PortName="余数")
        wire(a, self.id, "被除数", enforce_int)
        wire(b, self.id, "除数", enforce_int)

class string_concat(BaseNode):
    def __init__(self, a=None, b=None):
        super().__init__("StringConcatNode", a_PortName="A", b_PortName="B", result_PortName="结果")
        wire(a, self.id, "A", enforce_string)
        wire(b, self.id, "B", enforce_string)

class random_int(BaseNode):
    def __init__(self, min_val=None, max_val=None):
        super().__init__("RandomIntNode", min_PortName="最小值", max_PortName="最大值", result_PortName="随机整数")
        wire(min_val, self.id, "最小值", enforce_int)
        wire(max_val, self.id, "最大值", enforce_int)

class random_float(BaseNode):
    def __init__(self, min_val=None, max_val=None):
        super().__init__("RandomFloatNode", min_PortName="最小值", max_PortName="最大值", result_PortName="随机浮点数")
        wire(min_val, self.id, "最小值", enforce_float)
        wire(max_val, self.id, "最大值", enforce_float)

class int_to_float(BaseNode):
    def __init__(self, int_val=None):
        super().__init__("IntToFloatNode", int_PortName="整数", float_PortName="浮点数")
        wire(int_val, self.id, "整数")  # Omit enforce_int to avoid circular recursion

class float_to_int(BaseNode):
    def __init__(self, float_val=None):
        super().__init__("FloatToIntNode", float_PortName="浮点数", int_PortName="整数")
        wire(float_val, self.id, "浮点数")  # Omit enforce_float to avoid circular recursion

class float_to_string(BaseNode):
    def __init__(self, float_val=None, decimals=None):
        super().__init__("FloatToStringNode", value_PortName="数值", decimals_PortName="小数位数", result_PortName="字符串")
        wire(float_val, self.id, "数值", enforce_float)
        wire(decimals, self.id, "小数位数", enforce_int)

# ==========================================
# VALUES
# ==========================================
class get_sun_amount(BaseNode):
    def __init__(self): super().__init__("GetSunAmountNode", sunAmount_PortName="阳光数量")

class int_value(BaseNode):
    def __init__(self, val=1): super().__init__("IntValueNode", value_PortName="值", value=val)

class float_value(BaseNode):
    def __init__(self, val=3.0): super().__init__("FloatValueNode", value_PortName="值", value=val)

class bool_value(BaseNode):
    def __init__(self, val=False): super().__init__("BoolValueNode", value_PortName="值", value=val)

class string_value(BaseNode):
    def __init__(self, val="默认文本"): super().__init__("StringValueNode", value_PortName="值", value=val)
    
# ==========================================
# New Version Nodes 3.7
# ==========================================

class on_game_start(BaseNode):
    def __init__(self):
        super().__init__("OnGameStartNode", trigger_PortName="触发")

class on_plant_death_complete(BaseNode):
    def __init__(self):
        super().__init__("OnPlantDeathCompleteNode", trigger_PortName="触发", plant_PortName="植物", dieReason_PortName="死亡原因")

class die_plant(BaseNode):
    def __init__(self, plant=None):
        super().__init__("DiePlantNode", trigger_PortName="触发", plant_PortName="植物", onCompleted_PortName="死亡完成")
        wire(plant, self.id, "植物")

class get_all_plants(BaseNode):
    def __init__(self):
        super().__init__("GetAllPlantsNode", plants_PortName="全部植物")

class move_zombie(BaseNode):
    def __init__(self, zombie=None, column=None, row=None):
        super().__init__("MoveZombieNode", trigger_PortName="触发", zombie_PortName="僵尸", column_PortName="目标列", row_PortName="目标行", onMoved_PortName="移动成功", movedZombie_PortName="僵尸")
        wire(zombie, self.id, "僵尸")
        wire(column, self.id, "目标列", enforce_int)
        wire(row, self.id, "目标行", enforce_int)

class play_zombie_anim(BaseNode):
    def __init__(self, zombie=None, animation_name="idle"):
        # Note: animationName is stored as an internal string property, not a port.
        super().__init__("PlayZombieAnimNode", animationName=animation_name, trigger_PortName="触发", zombie_PortName="僵尸")
        wire(zombie, self.id, "僵尸")

class play_sound(BaseNode):
    def __init__(self, sound_id=None):
        # soundId is stored as a default internal property, but can also be driven by a port.
        super().__init__("PlaySoundNode", soundId=0, trigger_PortName="触发", soundId_PortName="音效ID")
        wire(sound_id, self.id, "音效ID", enforce_int)

class create_particle(BaseNode):
    def __init__(self, row=None, column=None):
        super().__init__("CreateParticleNode", trigger_PortName="触发", row_PortName="行", column_PortName="列")
        wire(row, self.id, "行", enforce_int)
        wire(column, self.id, "列", enforce_int)

class create_info_card(BaseNode):
    def __init__(self, big_title=None, small_title=None):
        super().__init__("CreateInfoCardNode", trigger_PortName="触发", bigTitle_PortName="大标题", smallTitle_PortName="小标题", onCardClicked_PortName="点击卡牌时触发")
        wire(big_title, self.id, "大标题", enforce_string)
        wire(small_title, self.id, "小标题", enforce_string)

class random_trigger(BaseNode):
    def __init__(self, count=None, allow_repeat=None):
        super().__init__("RandomTriggerNode", trigger_PortName="触发", count_PortName="触发数量", allowRepeat_PortName="重复触发", output_PortName="触发")
        wire(count, self.id, "触发数量", enforce_int)
        wire(allow_repeat, self.id, "重复触发", enforce_bool)

class get_travel_buff(BaseNode):
    def __init__(self, buff_enum):
        super().__init__(
            "GetTravelBuffNode", 
            trigger_PortName="触发", 
            onSuccess_PortName="成功"
        )
        
        if hasattr(buff_enum, "value"):
            asset_class, internal_id = buff_enum.value
        else:
            asset_class, internal_id = buff_enum

        if not hasattr(ctx, 'variables'):
            ctx.variables = []
            
        asset_rid = len(ctx.variables) + 80000 
        
        self.kwargs["buff"] = {"rid": asset_rid}
        
        ctx.variables.append({
            "rid": asset_rid,
            "type": {
                "class": asset_class, 
                "ns": "",
                "asm": "Assembly-CSharp"
            },
            "data": {
                "value__": internal_id
            }
        })
        
# --- INTEGER VARIABLES ---
class get_int_variable_value(BaseNode):
    def __init__(self, variable=None):
        super().__init__("GetIntVariableValueNode", variable_PortName="变量", value_PortName="值")
        wire(variable, self.id, "变量")

class set_int_variable_value(BaseNode):
    def __init__(self, variable=None, value=None):
        super().__init__("SetIntVariableValueNode", trigger_PortName="触发", variable_PortName="变量", value_PortName="新值", variableOut_PortName="变量", onComplete_PortName="完成")
        wire(variable, self.id, "变量")
        wire(value, self.id, "新值", enforce_int)

# --- FLOAT VARIABLES ---
class get_float_variable_value(BaseNode):
    def __init__(self, variable=None):
        super().__init__("GetFloatVariableValueNode", variable_PortName="变量", value_PortName="值")
        wire(variable, self.id, "变量")

class set_float_variable_value(BaseNode):
    def __init__(self, variable=None, value=None):
        super().__init__("SetFloatVariableValueNode", trigger_PortName="触发", variable_PortName="变量", value_PortName="新值", variableOut_PortName="变量", onComplete_PortName="完成")
        wire(variable, self.id, "变量")
        wire(value, self.id, "新值", enforce_float)

# --- BOOL VARIABLES ---
class get_bool_variable_value(BaseNode):
    def __init__(self, variable=None):
        super().__init__("GetBoolVariableValueNode", variable_PortName="变量", value_PortName="值")
        wire(variable, self.id, "变量")

class set_bool_variable_value(BaseNode):
    def __init__(self, variable=None, value=None):
        super().__init__("SetBoolVariableValueNode", trigger_PortName="触发", variable_PortName="变量", value_PortName="新值", variableOut_PortName="变量", onComplete_PortName="完成")
        wire(variable, self.id, "变量")
        wire(value, self.id, "新值", enforce_bool)

# --- VARIABLE ASSETS ---
class int_variable(BaseNode):
    def __init__(self, var_name="整数", initial_value=0, asset_dict=None):
        super().__init__("IntVariableNode", variable_PortName="变量")
        if not hasattr(ctx, 'variables'):
            ctx.variables = []
            
        if asset_dict:
            self.kwargs["asset"] = {"rid": asset_dict["rid"]}
            asset_dict["data"]["referencedNodeIds"].append(self.id)
            self.asset_dict = asset_dict
        else:
            asset_rid = len(ctx.variables) + 50000 
            self.kwargs["asset"] = {"rid": asset_rid}
            self.asset_dict = {
                "rid": asset_rid,
                "type": {
                    "class": "IntVariableAsset",
                    "ns": "GameLevel.EventNodes",
                    "asm": "Assembly-CSharp"
                },
                "data": {
                    "name": var_name,
                    "referencedNodeIds": [self.id], 
                    "value": int(initial_value)
                }
            }
            ctx.variables.append(self.asset_dict)


class float_variable(BaseNode):
    def __init__(self, var_name="浮点数", initial_value=0.0, asset_dict=None):
        super().__init__("FloatVariableNode", variable_PortName="变量")
        if not hasattr(ctx, 'variables'):
            ctx.variables = []
            
        if asset_dict:
            self.kwargs["asset"] = {"rid": asset_dict["rid"]}
            asset_dict["data"]["referencedNodeIds"].append(self.id)
            self.asset_dict = asset_dict
        else:
            asset_rid = len(ctx.variables) + 60000 
            self.kwargs["asset"] = {"rid": asset_rid}
            self.asset_dict = {
                "rid": asset_rid,
                "type": {
                    "class": "FloatVariableAsset",
                    "ns": "GameLevel.EventNodes",
                    "asm": "Assembly-CSharp"
                },
                "data": {
                    "name": var_name,
                    "referencedNodeIds": [self.id], 
                    "value": float(initial_value)
                }
            }
            ctx.variables.append(self.asset_dict)


class bool_variable(BaseNode):
    def __init__(self, var_name="布尔值", initial_value=False, asset_dict=None):
        super().__init__("BoolVariableNode", variable_PortName="变量")
        if not hasattr(ctx, 'variables'):
            ctx.variables = []
            
        if asset_dict:
            self.kwargs["asset"] = {"rid": asset_dict["rid"]}
            asset_dict["data"]["referencedNodeIds"].append(self.id)
            self.asset_dict = asset_dict
        else:
            asset_rid = len(ctx.variables) + 70000 
            self.kwargs["asset"] = {"rid": asset_rid}
            self.asset_dict = {
                "rid": asset_rid,
                "type": {
                    "class": "BoolVariableAsset",
                    "ns": "GameLevel.EventNodes",
                    "asm": "Assembly-CSharp"
                },
                "data": {
                    "name": var_name,
                    "referencedNodeIds": [self.id], 
                    "value": bool(initial_value)
                }
            }
            ctx.variables.append(self.asset_dict)

class multi_plant_type_list(BaseNode):
    def __init__(self, plant_types=None):
        formatted_types = []
        for pt in (plant_types or []):
            if hasattr(pt, "value"):
                formatted_types.append(pt.value)
            else:
                formatted_types.append(int(pt))
        super().__init__(
            "MultiPlantTypeListNode",
            plantTypes=formatted_types,
            plantTypeList_PortName="植物类型列表"
        )
