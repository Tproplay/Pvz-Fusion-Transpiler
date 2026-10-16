from __future__ import annotations

from typing import Any, Optional
from ._Nodes.Original import *
from .typing import to_port, to_int_port, to_float_port, to_bool_port, to_string_port


def _wire_node_kwargs(node: Any, kwargs: dict[str, Any]) -> Any:
    for k, v in kwargs.items():
        if v is None:
            continue
        try:
            inp = node.get_input(k)
            to_port(v).connect(inp)
        except Exception:
            pass
    return node


# =============================================================================
# CONSTANTS & VALUE NODES
# =============================================================================

def int_value(val: int = 1, **kwargs: Any) -> IntValueNode:
    return IntValueNode(value=val, **kwargs)

def float_value(val: float = 3.0, **kwargs: Any) -> FloatValueNode:
    return FloatValueNode(value=val, **kwargs)

def bool_value(val: bool = False, **kwargs: Any) -> BoolValueNode:
    return BoolValueNode(value=val, **kwargs)

def string_value(val: str = "", **kwargs: Any) -> StringValueNode:
    return StringValueNode(value=val, **kwargs)

def plant_type_value(val: int = 0, **kwargs: Any) -> PlantTypeValueNode:
    return PlantTypeValueNode(value=val, **kwargs)

def zombie_type_value(val: int = 0, **kwargs: Any) -> ZombieTypeValueNode:
    return ZombieTypeValueNode(value=val, **kwargs)


# =============================================================================
# VARIABLES
# =============================================================================

def int_variable(var_name: str = "整数", initial_value: int = 0, asset: Any = None, **kwargs: Any) -> IntVariableNode:
    return IntVariableNode(name=var_name, value=initial_value, asset=asset, **kwargs)

def float_variable(var_name: str = "浮点数", initial_value: float = 0.0, asset: Any = None, **kwargs: Any) -> FloatVariableNode:
    return FloatVariableNode(name=var_name, value=initial_value, asset=asset, **kwargs)

def bool_variable(var_name: str = "布尔值", initial_value: bool = False, asset: Any = None, **kwargs: Any) -> BoolVariableNode:
    return BoolVariableNode(name=var_name, value=initial_value, asset=asset, **kwargs)

def string_variable(var_name: str = "字符串", initial_value: str = "", asset: Any = None, **kwargs: Any) -> StringVariableNode:
    return StringVariableNode(name=var_name, value=initial_value, asset=asset, **kwargs)

def get_int_variable_value(variable: Any = None, **kwargs: Any) -> GetIntVariableValueNode:
    node = GetIntVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_intvariable_Variable)
    return node

def get_float_variable_value(variable: Any = None, **kwargs: Any) -> GetFloatVariableValueNode:
    node = GetFloatVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_floatvariable_Variable)
    return node

def get_bool_variable_value(variable: Any = None, **kwargs: Any) -> GetBoolVariableValueNode:
    node = GetBoolVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_boolvariable_Variable)
    return node

def get_string_variable_value(variable: Any = None, **kwargs: Any) -> GetStringVariableValueNode:
    node = GetStringVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_stringvariable_Variable)
    return node

def set_int_variable_value(variable: Any = None, value: Any = None, **kwargs: Any) -> SetIntVariableValueNode:
    node = SetIntVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_intvariable_Variable)
    if value is not None:
        to_port(value).connect(node.port_input_int_NewValue)
    return node

def set_float_variable_value(variable: Any = None, value: Any = None, **kwargs: Any) -> SetFloatVariableValueNode:
    node = SetFloatVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_floatvariable_Variable)
    if value is not None:
        to_port(value).connect(node.port_input_float_NewValue)
    return node

def set_bool_variable_value(variable: Any = None, value: Any = None, **kwargs: Any) -> SetBoolVariableValueNode:
    node = SetBoolVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_boolvariable_Variable)
    if value is not None:
        to_port(value).connect(node.port_input_bool_NewValue)
    return node

def set_string_variable_value(variable: Any = None, value: Any = None, **kwargs: Any) -> SetStringVariableValueNode:
    node = SetStringVariableValueNode(**kwargs)
    if variable is not None:
        to_port(variable).connect(node.port_input_stringvariable_Variable)
    if value is not None:
        to_port(value).connect(node.port_input_string_NewValue)
    return node


# =============================================================================
# ARITHMETIC & TYPE CONVERSION
# =============================================================================

def add_node(a: Any = None, b: Any = None, **kwargs: Any) -> AddNode:
    node = AddNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_float_A)
    if b is not None:
        to_port(b).connect(node.port_input_float_B)
    return node

def subtract_node(a: Any = None, b: Any = None, **kwargs: Any) -> SubtractNode:
    node = SubtractNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_float_Minuend)
    if b is not None:
        to_port(b).connect(node.port_input_float_Subtrahend)
    return node

def multiply_node(a: Any = None, b: Any = None, **kwargs: Any) -> MultiplyNode:
    node = MultiplyNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_float_A)
    if b is not None:
        to_port(b).connect(node.port_input_float_B)
    return node

def divide_node(a: Any = None, b: Any = None, **kwargs: Any) -> DivideNode:
    node = DivideNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_float_Dividend)
    if b is not None:
        to_port(b).connect(node.port_input_float_Divisor)
    return node

def int_add(a: Any = None, b: Any = None, **kwargs: Any) -> IntAddNode:
    node = IntAddNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_int_A)
    if b is not None:
        to_port(b).connect(node.port_input_int_B)
    return node

def int_subtract(a: Any = None, b: Any = None, **kwargs: Any) -> IntSubtractNode:
    node = IntSubtractNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_int_Minuend)
    if b is not None:
        to_port(b).connect(node.port_input_int_Subtrahend)
    return node

def int_multiply(a: Any = None, b: Any = None, **kwargs: Any) -> IntMultiplyNode:
    node = IntMultiplyNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_int_A)
    if b is not None:
        to_port(b).connect(node.port_input_int_B)
    return node

def int_divide(a: Any = None, b: Any = None, **kwargs: Any) -> IntDivideNode:
    node = IntDivideNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_int_Dividend)
    if b is not None:
        to_port(b).connect(node.port_input_int_Divisor)
    return node

def int_modulo(a: Any = None, b: Any = None, **kwargs: Any) -> IntModuloNode:
    node = IntModuloNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_int_Dividend)
    if b is not None:
        to_port(b).connect(node.port_input_int_Divisor)
    return node

def int_to_float(int_val: Any = None, **kwargs: Any) -> IntToFloatNode:
    node = IntToFloatNode(**kwargs)
    if int_val is not None:
        to_port(int_val).connect(node.port_input_int_IntValue)
    return node

def float_to_int(float_val: Any = None, **kwargs: Any) -> FloatToIntNode:
    node = FloatToIntNode(**kwargs)
    if float_val is not None:
        to_port(float_val).connect(node.port_input_float_FloatValue)
    return node

def float_to_string(float_val: Any = None, decimals: Any = None, **kwargs: Any) -> FloatToStringNode:
    node = FloatToStringNode(**kwargs)
    if float_val is not None:
        to_port(float_val).connect(node.port_input_float_FloatValue)
    if decimals is not None:
        to_port(decimals).connect(node.port_input_int_Decimals)
    return node


# =============================================================================
# LOGIC & BRANCHING
# =============================================================================

def branch_node(condition: Any = None, **kwargs: Any) -> BranchNode:
    node = BranchNode(**kwargs)
    if condition is not None:
        to_port(condition).connect(node.port_input_bool_Condition)
    return node

def and_node(a: Any = None, b: Any = None, **kwargs: Any) -> AndNode:
    node = AndNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_bool_A)
    if b is not None:
        to_port(b).connect(node.port_input_bool_B)
    return node

def or_node(a: Any = None, b: Any = None, **kwargs: Any) -> OrNode:
    node = OrNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_bool_A)
    if b is not None:
        to_port(b).connect(node.port_input_bool_B)
    return node

def not_node(input: Any = None, **kwargs: Any) -> NotNode:
    node = NotNode(**kwargs)
    if input is not None:
        to_port(input).connect(node.port_input_bool_Input)
    return node

def compare_int(a: Any = None, b: Any = None, **kwargs: Any) -> CompareIntNode:
    node = CompareIntNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_int_ValueA)
    if b is not None:
        to_port(b).connect(node.port_input_int_ValueB)
    return node

def compare_plant_type(a: Any = None, b: Any = None, **kwargs: Any) -> ComparePlantTypeNode:
    node = ComparePlantTypeNode(**kwargs)
    if a is not None:
        to_port(a).connect(node.port_input_planttype_PlantTypeA)
    if b is not None:
        to_port(b).connect(node.port_input_planttype_PlantTypeB)
    return node

def toggle_node(initial_state: bool = False, **kwargs: Any) -> ToggleNode:
    node = ToggleNode(**kwargs)
    return node

def toggle_cycle_node(interval: float = 0.1, **kwargs: Any) -> ToggleCycleNode:
    node = ToggleCycleNode(**kwargs)
    to_port(interval).connect(node.port_input_float_CycleInterval)
    return node

def counter_node(start_val: int = 0, reset: Any = None, **kwargs: Any) -> CounterNode:
    node = CounterNode(**kwargs)
    if reset is not None:
        to_port(reset).connect(node.port_input_bool_IsReset)
    return node

def wait_node(duration: float = 1.0, **kwargs: Any) -> WaitNode:
    node = WaitNode(**kwargs)
    to_port(duration).connect(node.port_input_float_Duration)
    return node

def random_int(min_val: int = 0, max_val: int = 10, **kwargs: Any) -> RandomIntNode:
    node = RandomIntNode(**kwargs)
    to_port(min_val).connect(node.port_input_int_Min)
    to_port(max_val).connect(node.port_input_int_Max)
    return node

def random_float(min_val: float = 0.0, max_val: float = 1.0, **kwargs: Any) -> RandomFloatNode:
    node = RandomFloatNode(**kwargs)
    to_port(min_val).connect(node.port_input_float_Min)
    to_port(max_val).connect(node.port_input_float_Max)
    return node

def random_trigger(count: int = 1, allow_repeat: bool = False, **kwargs: Any) -> RandomTriggerNode:
    node = RandomTriggerNode(**kwargs)
    to_port(count).connect(node.port_input_int_TriggerCount)
    to_port(allow_repeat).connect(node.port_input_bool_RepeatTrigger)
    return node

def for_loop_node(count: Any = 1, **kwargs: Any) -> ForLoopNode:
    node = ForLoopNode(**kwargs)
    to_port(count).connect(node.port_input_int_LoopCount)
    return node


# =============================================================================
# ENTITIES & COLLECTIONS
# =============================================================================

def for_each_plant(plant_list: Any = None, **kwargs: Any) -> ForEachPlantNode:
    node = ForEachPlantNode(**kwargs)
    if plant_list is not None:
        to_port(plant_list).connect(node.port_input_plantlist_PlantList)
    return node

def for_each_plant_type(type_list: Any = None, **kwargs: Any) -> ForEachPlantTypeNode:
    node = ForEachPlantTypeNode(**kwargs)
    if type_list is not None:
        to_port(type_list).connect(node.port_input_planttypelist_PlantTypeList)
    return node

def plant_split(plant: Any = None, **kwargs: Any) -> PlantSplitNode:
    node = PlantSplitNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    return node

def zombie_split(zombie: Any = None, **kwargs: Any) -> ZombieSplitNode:
    node = ZombieSplitNode(**kwargs)
    if zombie is not None:
        to_port(zombie).connect(node.port_input_zombie_Zombie)
    return node

def die_plant(plant: Any = None, **kwargs: Any) -> DiePlantNode:
    node = DiePlantNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    return node

def damage_plant(plant: Any = None, damage: Any = None, **kwargs: Any) -> DamagePlantNode:
    node = DamagePlantNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    if damage is not None:
        to_port(damage).connect(node.port_input_float_Damage)
    return node

def heal_plant(plant: Any = None, heal_amount: Any = None, **kwargs: Any) -> HealPlantNode:
    node = HealPlantNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    if heal_amount is not None:
        to_port(heal_amount).connect(node.port_input_float_HealAmount)
    return node

def give_plant_shield(plant: Any = None, shield: Any = None, **kwargs: Any) -> GivePlantShieldNode:
    node = GivePlantShieldNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    if shield is not None:
        to_port(shield).connect(node.port_input_float_Shield)
    return node

def move_plant(plant: Any = None, row: Any = None, column: Any = None, force: Any = False, **kwargs: Any) -> MovePlantNode:
    node = MovePlantNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if force is not None:
        to_bool_port(force).connect(node.port_input_bool_Force)
    return node

def modify_plant_attack(plant: Any = None, multiplier: Any = None, **kwargs: Any) -> ModifyPlantAttackNode:
    node = ModifyPlantAttackNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    if multiplier is not None:
        to_float_port(multiplier).connect(node.port_input_float_Multiplier)
    return node

def modify_plant_health(plant: Any = None, multiplier: Any = None, **kwargs: Any) -> ModifyPlantHealthNode:
    node = ModifyPlantHealthNode(**kwargs)
    if plant is not None:
        to_port(plant).connect(node.port_input_plant_Plant)
    if multiplier is not None:
        to_float_port(multiplier).connect(node.port_input_float_Multiplier)
    return node

def damage_zombie(zombie: Any = None, damage: Any = None, **kwargs: Any) -> DamageZombieNode:
    node = DamageZombieNode(**kwargs)
    if zombie is not None:
        to_port(zombie).connect(node.port_input_zombie_Zombie)
    if damage is not None:
        to_float_port(damage).connect(node.port_input_float_Damage)
    return node

def modify_zombie_health(zombie: Any = None, ratio: Any = None, **kwargs: Any) -> ModifyZombieHealthNode:
    node = ModifyZombieHealthNode(**kwargs)
    if zombie is not None:
        to_port(zombie).connect(node.port_input_zombie_Zombie)
    if ratio is not None:
        to_float_port(ratio).connect(node.port_input_float_Ratio)
    return node

def move_zombie(zombie: Any = None, row: Any = None, column: Any = None, **kwargs: Any) -> MoveZombieNode:
    node = MoveZombieNode(**kwargs)
    if zombie is not None:
        to_port(zombie).connect(node.port_input_zombie_Zombie)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_TargetRow)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_TargetCol)
    return node

def set_zombie_mind_controlled(zombie: Any = None, **kwargs: Any) -> SetZombieMindControlledNode:
    node = SetZombieMindControlledNode(**kwargs)
    if zombie is not None:
        to_port(zombie).connect(node.port_input_zombie_Zombie)
    return node

def play_zombie_anim(zombie: Any = None, animation_name: Any = "idle", **kwargs: Any) -> PlayZombieAnimNode:
    node = PlayZombieAnimNode(**kwargs)
    if zombie is not None:
        to_port(zombie).connect(node.port_input_zombie_Zombie)
    if animation_name is not None:
        to_port(animation_name).connect(node.port_input_string_AnimationName)
    return node

def on_board_start(**kwargs: Any) -> OnBoardStartNode:
    return OnBoardStartNode(**kwargs)

def on_game_start(**kwargs: Any) -> OnGameStartNode:
    return OnGameStartNode(**kwargs)

def on_wave(**kwargs: Any) -> WaveEventNode:
    return WaveEventNode(**kwargs)

def on_mouse_click(**kwargs: Any) -> OnMouseClickNode:
    return OnMouseClickNode(**kwargs)

def on_key_press(target_key: Any = None, **kwargs: Any) -> OnKeyPressNode:
    node = OnKeyPressNode(**kwargs)
    if target_key is not None:
        setattr(node, "target_key", getattr(target_key, "value", target_key))
    return node

def on_plant_create(**kwargs: Any) -> OnPlantCreateNode:
    return OnPlantCreateNode(**kwargs)

def on_plant_die(**kwargs: Any) -> OnPlantDieNode:
    return OnPlantDieNode(**kwargs)

def on_plant_click(**kwargs: Any) -> OnPlantClickNode:
    return OnPlantClickNode(**kwargs)

def on_plant_death_complete(**kwargs: Any) -> OnPlantDeathCompleteNode:
    return OnPlantDeathCompleteNode(**kwargs)

def on_plant_mixed(**kwargs: Any) -> OnPlantMixedNode:
    return OnPlantMixedNode(**kwargs)

def on_zombie_spawn(**kwargs: Any) -> OnZombieSpawnNode:
    return OnZombieSpawnNode(**kwargs)

def on_zombie_die(**kwargs: Any) -> OnZombieDieNode:
    return OnZombieDieNode(**kwargs)

def on_zombie_click(**kwargs: Any) -> OnZombieClickNode:
    return OnZombieClickNode(**kwargs)

def on_zombie_health_below(**kwargs: Any) -> OnZombieHealthBelowNode:
    return OnZombieHealthBelowNode(**kwargs)

def on_wave_cleared(**kwargs: Any) -> OnWaveClearedNode:
    return OnWaveClearedNode(**kwargs)

def set_plant(row: Any = None, column: Any = None, plant_type: Any = None, force_plant: Any = False, **kwargs: Any) -> SetPlantNode:
    node = SetPlantNode(**kwargs)
    if row is not None:
        to_port(row).connect(node.port_input_int_Row)
    if column is not None:
        to_port(column).connect(node.port_input_int_Col)
    if plant_type is not None:
        to_port(plant_type).connect(node.port_input_planttype_PlantType)
    if force_plant is not None:
        to_port(force_plant).connect(node.port_input_bool_ForcePlant)
    return node

def create_zombie(row: Any = None, column: Any = None, zombie_type: Any = None, mind_controlled: Any = False, **kwargs: Any) -> CreateZombieNode:
    node = CreateZombieNode(**kwargs)
    if row is not None:
        to_port(row).connect(node.port_input_int_Row)
    if column is not None:
        to_port(column).connect(node.port_input_int_Col)
    if zombie_type is not None:
        to_port(zombie_type).connect(node.port_input_zombietype_ZombieType)
    if mind_controlled is not None:
        to_port(mind_controlled).connect(node.port_input_bool_IsHypnotized)
    return node

def add_multiple_choice_option(title: Any = None, description: Any = None, plant_type: Any = None, zombie_type: Any = None, **kwargs: Any) -> AddMultipleChoiceOptionNode:
    node = AddMultipleChoiceOptionNode(**kwargs)
    if title is not None:
        to_port(title).connect(node.port_input_string_Title)
    if description is not None:
        to_port(description).connect(node.port_input_string_Description)
    if plant_type is not None:
        to_port(plant_type).connect(node.port_input_planttype_PlantType)
    if zombie_type is not None:
        to_port(zombie_type).connect(node.port_input_zombietype_ZombieType)
    return node

def create_info_card(big_title: Any = None, small_title: Any = None, **kwargs: Any) -> CreateInfoCardNode:
    node = CreateInfoCardNode(**kwargs)
    if big_title is not None:
        to_port(big_title).connect(node.port_input_string_BigTitle)
    if small_title is not None:
        to_port(small_title).connect(node.port_input_string_SmallTitle)
    return node

def multi_plant_type_list(plant_types: Any = None, **kwargs: Any) -> MultiPlantTypeListNode:
    return MultiPlantTypeListNode(**kwargs)

def single_plant_type_list(plant_type: Any = None, **kwargs: Any) -> SinglePlantTypeListNode:
    node = SinglePlantTypeListNode(**kwargs)
    if plant_type is not None:
        to_port(plant_type).connect(node.port_input_planttype_PlantType)
    return node

def plant_type_list_storage(op: int = 0, init_empty: bool = True, **kwargs: Any) -> PlantTypeListStorageNode:
    return PlantTypeListStorageNode(**kwargs)

def merge_plant_type_lists(list_a: Any = None, list_b: Any = None, **kwargs: Any) -> MergePlantTypeListsNode:
    node = MergePlantTypeListsNode(**kwargs)
    if list_a is not None:
        to_port(list_a).connect(node.port_input_planttypelist_ListA)
    if list_b is not None:
        to_port(list_b).connect(node.port_input_planttypelist_ListB)
    return node

def remove_plant_type(type_list: Any = None, target_type: Any = None, **kwargs: Any) -> RemovePlantTypeNode:
    node = RemovePlantTypeNode(**kwargs)
    if type_list is not None:
        to_port(type_list).connect(node.port_input_planttypelist_List)
    if target_type is not None:
        to_port(target_type).connect(node.port_input_planttype_Type)
    return node

def get_random_plant_type(**kwargs: Any) -> GetRandomPlantTypeNode:
    return GetRandomPlantTypeNode(**kwargs)

def merge_multiple_choice_option_lists(list_a: Any = None, list_b: Any = None, list1: Any = None, list2: Any = None, **kwargs: Any) -> MergeMultipleChoiceOptionListsNode:
    node = MergeMultipleChoiceOptionListsNode(**kwargs)
    first = list1 if list1 is not None else list_a
    second = list2 if list2 is not None else list_b
    if first is not None:
        to_port(first).connect(node.port_input_choiceoptions_List1)
    if second is not None:
        to_port(second).connect(node.port_input_choiceoptions_List2)
    return node

def show_multiple_choice_menu(**kwargs: Any) -> ShowMultipleChoiceMenuNode:
    return ShowMultipleChoiceMenuNode(**kwargs)


# =============================================================================
# SUN & MONEY
# =============================================================================

def get_sun_amount(**kwargs: Any) -> GetSunAmountNode:
    return GetSunAmountNode(**kwargs)

def get_sun(amount: Any = None, **kwargs: Any) -> GetSunNode:
    node = GetSunNode(**kwargs)
    if amount is not None:
        to_int_port(amount).connect(node.port_input_int_SunAmount)
    return node

def add_sun(amount: Any = None, **kwargs: Any) -> GetSunNode:
    return get_sun(amount=amount, **kwargs)

def use_sun(amount: Any = None, **kwargs: Any) -> UseSunNode:
    node = UseSunNode(**kwargs)
    if amount is not None:
        to_int_port(amount).connect(node.port_input_int_SunAmount)
    return node

def get_money_amount(**kwargs: Any) -> GetMoneyAmountNode:
    return GetMoneyAmountNode(**kwargs)

def get_money(amount: Any = None, **kwargs: Any) -> GetMoneyNode:
    node = GetMoneyNode(**kwargs)
    if amount is not None:
        to_int_port(amount).connect(node.port_input_int_MoneyAmount)
    return node

def add_money(amount: Any = None, **kwargs: Any) -> GetMoneyNode:
    return get_money(amount=amount, **kwargs)

def use_money(amount: Any = None, **kwargs: Any) -> UseMoneyNode:
    node = UseMoneyNode(**kwargs)
    if amount is not None:
        to_int_port(amount).connect(node.port_input_int_MoneyAmount)
    return node


# =============================================================================
# MAP & ENVIRONMENT EFFECTS
# =============================================================================

def create_particle(row: Any = None, column: Any = None, **kwargs: Any) -> CreateParticleNode:
    node = CreateParticleNode(**kwargs)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    return node

def create_grave(row: Any = None, column: Any = None, **kwargs: Any) -> CreateGraveNode:
    node = CreateGraveNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    return node

def create_crater(row: Any = None, column: Any = None, **kwargs: Any) -> CreateCraterNode:
    node = CreateCraterNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    return node

def create_ladder(row: Any = None, column: Any = None, **kwargs: Any) -> CreateLadderNode:
    node = CreateLadderNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    return node

def create_ice_block(row: Any = None, column: Any = None, plant_type: Any = None, **kwargs: Any) -> CreateIceBlockNode:
    node = CreateIceBlockNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if plant_type is not None:
        to_port(plant_type).connect(node.port_input_planttype_FrozenPlant)
    return node

def create_cherry_explode(row: Any = None, column: Any = None, damage: Any = 1800, **kwargs: Any) -> CreateCherryExplodeNode:
    node = CreateCherryExplodeNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if damage is not None:
        to_float_port(damage).connect(node.port_input_float_Damage)
    return node

def create_doom_shroom_effect(row: Any = None, column: Any = None, damage: Any = 1800, set_pit: Any = True, **kwargs: Any) -> CreateDoomShroomEffectNode:
    node = CreateDoomShroomEffectNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if damage is not None:
        to_float_port(damage).connect(node.port_input_float_Damage)
    if set_pit is not None:
        to_bool_port(set_pit).connect(node.port_input_bool_CreateCrater)
    return node

def create_zombie_explode(row: Any = None, column: Any = None, **kwargs: Any) -> CreateZombieExplodeNode:
    node = CreateZombieExplodeNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    return node

def create_jalapeno_effect(row: Any = None, damage: Any = 1800, **kwargs: Any) -> CreateJalapenoEffectNode:
    node = CreateJalapenoEffectNode(**kwargs)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if damage is not None:
        to_float_port(damage).connect(node.port_input_float_Damage)
    return node

def create_ice_shroom_effect(duration: Any = 4.0, **kwargs: Any) -> CreateIceShroomEffectNode:
    node = CreateIceShroomEffectNode(**kwargs)
    if duration is not None:
        to_float_port(duration).connect(node.port_input_float_FreezeTime)
    return node


# =============================================================================
# AUDIO & GAME FLOW
# =============================================================================

def play_sound(sound_id: Any = None, **kwargs: Any) -> PlaySoundNode:
    node = PlaySoundNode(**kwargs)
    if sound_id is not None:
        to_int_port(sound_id).connect(node.port_input_int_SoundId)
    return node

def game_over(reason: Any = "Defeated!", **kwargs: Any) -> GameOverNode:
    node = GameOverNode(**kwargs)
    if reason is not None:
        to_string_port(reason).connect(node.port_input_string_FailureReason)
    return node

def game_win(**kwargs: Any) -> GameWinNode:
    return GameWinNode(**kwargs)

def get_travel_buff(buff_enum: Any = None, **kwargs: Any) -> GetTravelBuffNode:
    node = GetTravelBuffNode(**kwargs)
    if buff_enum is not None:
        if hasattr(buff_enum, "value"):
            val = buff_enum.value
        else:
            val = buff_enum
        if isinstance(val, (tuple, list)) and len(val) == 2:
            asset_class = str(val[0])
            internal_id = int(val[1])
        elif isinstance(val, (int, str)):
            asset_class = "AdvBuff"
            internal_id = int(val)
        else:
            asset_class = "AdvBuff"
            internal_id = 0
        from ._Nodes.Original.VariableAsset import VariableAsset

        class _BuffAsset(VariableAsset):
            def __init__(self, cls_name: str, val_id: int):
                super().__init__(name="Buff", initial_value=val_id)
                self.asset_class = cls_name
                self.ns = ""
                self.asm = "Assembly-CSharp"

            def dump_ref(self) -> dict[str, Any]:
                return {
                    "rid": self.rid if self.rid is not None else 80000,
                    "type": {
                        "class": self.asset_class,
                        "ns": self.ns,
                        "asm": self.asm,
                    },
                    "data": {
                        "value__": self.value,
                    },
                }

        buff_asset = _BuffAsset(asset_class, internal_id)
        node.buff = buff_asset
    return node


# =============================================================================
# ENTITY QUERY & UI
# =============================================================================

def get_nearest_zombie(row: Any = None, column: Any = None, **kwargs: Any) -> GetNearestZombieNode:
    node = GetNearestZombieNode(**kwargs)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    return node

def get_plants_in_cell(row: Any = None, column: Any = None, **kwargs: Any) -> GetPlantsInCellNode:
    node = GetPlantsInCellNode(**kwargs)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    return node

def get_all_plants(**kwargs: Any) -> GetAllPlantsNode:
    return GetAllPlantsNode(**kwargs)

def add_plant_card(
    plant_type: Any = None,
    cooldown: Any = 7.5,
    cost: Any = 100,
    use_default: Any = True,
    p_type: Any = None,
    cd: Any = None,
    price: Any = None,
    default_data: Any = None,
    **kwargs: Any,
) -> AddPlantCardNode:
    node = AddPlantCardNode(**kwargs)
    pt = plant_type if plant_type is not None else p_type
    c_down = cd if cd is not None else cooldown
    c_cost = price if price is not None else cost
    d_data = default_data if default_data is not None else use_default
    if pt is not None:
        to_port(pt).connect(node.port_input_planttype_PlantType)
    if c_down is not None:
        to_float_port(c_down).connect(node.port_input_float_Cooldown)
    if c_cost is not None:
        to_int_port(c_cost).connect(node.port_input_int_Price)
    if d_data is not None:
        to_bool_port(d_data).connect(node.port_input_bool_UseDefaultData)
    return node

def delete_card_by_type(plant_type: Any = None, **kwargs: Any) -> DeleteCardByTypeNode:
    node = DeleteCardByTypeNode(**kwargs)
    if plant_type is not None:
        to_port(plant_type).connect(node.port_input_planttype_PlantType)
    return node

def create_plant_card(row: Any = None, column: Any = None, plant_type: Any = None, **kwargs: Any) -> CreatePlantCardNode:
    node = CreatePlantCardNode(**kwargs)
    if column is not None:
        to_int_port(column).connect(node.port_input_int_Col)
    if row is not None:
        to_int_port(row).connect(node.port_input_int_Row)
    if plant_type is not None:
        to_port(plant_type).connect(node.port_input_planttype_PlantType)
    return node

def show_text(text: Any = None, duration: Any = 3.0, **kwargs: Any) -> ShowTextNode:
    node = ShowTextNode(**kwargs)
    if text is not None:
        to_string_port(text).connect(node.port_input_string_Text)
    if duration is not None:
        to_float_port(duration).connect(node.port_input_float_Duration)
    return node

def string_concat(a: Any = None, b: Any = None, **kwargs: Any) -> StringConcatNode:
    node = StringConcatNode(**kwargs)
    if a is not None:
        to_string_port(a).connect(node.port_input_string_A)
    if b is not None:
        to_string_port(b).connect(node.port_input_string_B)
    return node
