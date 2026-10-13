from __future__ import annotations

from typing import Any, Optional, Union
from .Core.context import ctx
from .Nodes.Original import *
from .Nodes.Original.Node import to_port, Port, Node


def wire(val: Any, target_id: Any, target_port: str, enforce_func: Optional[Any] = None) -> None:
    """Wires a source value or output port to a target node's input port."""
    if val is None:
        return

    # Safely unwrap port reference or variable
    if hasattr(val, "_get_primary_port"):
        val = val._get_primary_port() if callable(val._get_primary_port) else val._get_primary_port
    elif hasattr(val, "value"):
        val = val.value

    # If val is a Port instance
    if isinstance(val, Port):
        target_node = ctx.level.graph.node_mgr.get_node(target_id)
        if target_node:
            tport = target_node.get_input(target_port)
            val.connect(tport)
        else:
            ctx.add_connection(val.node.node_id, val.name, target_id, target_port)
        return

    # If val is a tuple of (src_node_or_id, src_port_name)
    if isinstance(val, (tuple, list)) and len(val) == 2:
        src, src_port = val
        src_id = src.id if hasattr(src, "id") else (src.node_id if hasattr(src, "node_id") else src)
        ctx.add_connection(src_id, src_port, target_id, target_port)
        return

    # Primitive or auto-castable value
    src_port = to_port(val)
    target_node = ctx.level.graph.node_mgr.get_node(target_id)
    if target_node:
        tport = target_node.get_input(target_port)
        src_port.connect(tport)
    else:
        ctx.add_connection(src_port.node.node_id, src_port.name, target_id, target_port)


# =============================================================================
# SNAKE_CASE ALIASES FOR BACKWARD COMPATIBILITY & VISUAL SCRIPTING CONVENIENCE
# =============================================================================

# Events
on_board_start = OnBoardStartNode
on_game_start = OnGameStartNode
on_wave = WaveEventNode
on_mouse_click = OnMouseClickNode
on_key_press = OnKeyPressNode
on_plant_create = OnPlantCreateNode
on_plant_click = OnPlantClickNode
on_plant_die = OnPlantDieNode
on_plant_death_complete = OnPlantDeathCompleteNode
on_zombie_spawn = OnZombieSpawnNode
on_zombie_die = OnZombieDieNode
on_zombie_click = OnZombieClickNode
on_wave_cleared = OnWaveClearedNode
on_plant_mixed = OnPlantMixedNode
on_zombie_health_below = OnZombieHealthBelowNode
on_world_plant_effect = OnWorldPlantEffectNode

# Plant Actions
set_plant = SetPlantNode
move_plant = MovePlantNode
heal_plant = HealPlantNode
damage_plant = DamagePlantNode
give_plant_shield = GivePlantShieldNode
modify_plant_attack = ModifyPlantAttackNode
modify_plant_health = ModifyPlantHealthNode
plant_split = PlantSplitNode
die_plant = DiePlantNode
get_plants_in_cell = GetPlantsInCellNode
get_all_plants = GetAllPlantsNode
get_plants_on_layer = GetPlantsOnLayerNode
for_each_plant = ForEachPlantNode
for_each_plant_type = ForEachPlantTypeNode
plant_type_value = PlantTypeValueNode
compare_plant_type = ComparePlantTypeNode
single_plant_type_list = SinglePlantTypeListNode
multi_plant_type_list = MultiPlantTypeListNode
plant_type_list_storage = PlantTypeListStorageNode
merge_plant_type_lists = MergePlantTypeListsNode
get_random_plant_type = GetRandomPlantTypeNode
remove_plant_type = RemovePlantTypeNode
create_plant_card = CreatePlantCardNode
add_plant_card = AddPlantCardNode

# Zombie Actions
create_zombie = CreateZombieNode
damage_zombie = DamageZombieNode
set_zombie_mind_controlled = SetZombieMindControlledNode
get_nearest_zombie = GetNearestZombieNode
modify_zombie_health = ModifyZombieHealthNode
zombie_split = ZombieSplitNode
zombie_type_value = ZombieTypeValueNode
compare_zombie_type = CompareZombieTypeNode
move_zombie = MoveZombieNode
play_zombie_anim = PlayZombieAnimNode
get_all_zombies = GetAllZombiesNode
for_each_zombie = ForEachZombieNode
for_each_all_zombies = ForEachAllZombiesNode
set_zombie_status = SetZombieStatusNode
get_zombie_status = GetZombieStatusNode
set_zombie_stats = SetZombieStatsNode
get_zombie_stats = GetZombieStatsNode

# Logic / Flow
branch_node = BranchNode
wait_node = WaitNode
for_loop_node = ForLoopNode
toggle_cycle_node = ToggleCycleNode
toggle_node = ToggleNode
pulse_node = PulseNode
counter_node = CounterNode
not_node = NotNode
and_node = AndNode
or_node = OrNode
random_trigger = RandomTriggerNode
do_once = DoOnceNode
wait_until = WaitUntilNode
repeat_until = RepeatUntilNode

# Comparison
compare_int = CompareIntNode
compare_float = CompareFloatNode
compare_game_object = CompareGameObjectNode

# Calculate
add_node = AddNode
subtract_node = SubtractNode
multiply_node = MultiplyNode
divide_node = DivideNode
int_add = IntAddNode
int_subtract = IntSubtractNode
int_multiply = IntMultiplyNode
int_divide = IntDivideNode
int_modulo = IntModuloNode
string_concat = StringConcatNode
random_int = RandomIntNode
random_float = RandomFloatNode
power_node = PowerNode
logarithm_node = LogarithmNode

# Constants
int_value = IntValueNode
float_value = FloatValueNode
bool_value = BoolValueNode
string_value = StringValueNode

# Type Convert
int_to_float = IntToFloatNode
float_to_int = FloatToIntNode
float_to_string = FloatToStringNode
int_to_string = IntToStringNode

# General / Board / UI
get_sun_amount = GetSunAmountNode
add_sun = GetSunNode
use_sun = UseSunNode
get_money_amount = GetMoneyAmountNode
get_money = GetMoneyNode
add_money = GetMoneyNode
use_money = UseMoneyNode
show_text = ShowTextNode
play_sound = PlaySoundNode
get_travel_buff = GetTravelBuffNode
create_grave = CreateGraveNode
create_particle = CreateParticleNode
game_over = GameOverNode
game_win = GameWinNode
show_multiple_choice_menu = ShowMultipleChoiceMenuNode
add_multiple_choice_option = AddMultipleChoiceOptionNode
merge_multiple_choice_option_lists = MergeMultipleChoiceOptionListsNode
create_info_card = CreateInfoCardNode
delete_card_by_type = DeleteCardByTypeNode
delete_info_cards = DeleteInfoCardsNode

# Lawn Effects
create_ice_shroom_effect = CreateIceShroomEffectNode
create_jalapeno_effect = CreateJalapenoEffectNode
create_doom_shroom_effect = CreateDoomShroomEffectNode
create_cherry_explode = CreateCherryExplodeNode
create_ladder = CreateLadderNode
create_crater = CreateCraterNode
create_ice_block = CreateIceBlockNode
create_zombie_explode = CreateZombieExplodeNode

# Variables
int_variable = IntVariableNode
float_variable = FloatVariableNode
bool_variable = BoolVariableNode
string_variable = StringVariableNode
get_int_variable_value = GetIntVariableValueNode
set_int_variable_value = SetIntVariableValueNode
get_float_variable_value = GetFloatVariableValueNode
set_float_variable_value = SetFloatVariableValueNode
get_bool_variable_value = GetBoolVariableValueNode
set_bool_variable_value = SetBoolVariableValueNode
get_string_variable_value = GetStringVariableValueNode
set_string_variable_value = SetStringVariableValueNode
