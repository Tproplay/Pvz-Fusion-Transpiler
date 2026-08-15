from .node_base import BaseNode, ExecutionPath
from typing import Any, Union

class PortReference(tuple):
    # Document math and comparison operations to silence Pylance strict-mode
    def __add__(self, other: Any) -> 'PortReference': ...
    def __sub__(self, other: Any) -> 'PortReference': ...
    def __mul__(self, other: Any) -> 'PortReference': ...
    def __truediv__(self, other: Any) -> 'PortReference': ...
    def __mod__(self, other: Any) -> 'PortReference': ...
    def __radd__(self, other: Any) -> 'PortReference': ...
    def __rsub__(self, other: Any) -> 'PortReference': ...
    def __rmul__(self, other: Any) -> 'PortReference': ...
    def __rtruediv__(self, other: Any) -> 'PortReference': ...
    def __rmod__(self, other: Any) -> 'PortReference': ...
    def __eq__(self, other: Any) -> 'PortReference': ...
    def __ne__(self, other: Any) -> 'PortReference': ...
    def __gt__(self, other: Any) -> 'PortReference': ...
    def __lt__(self, other: Any) -> 'PortReference': ...
    def __ge__(self, other: Any) -> 'PortReference': ...
    def __le__(self, other: Any) -> 'PortReference': ...
    # THE CRITICAL LINE: Tell Pylance that & and | return a PortReference chain link
    def __and__(self, other: Any) -> 'PortReference': ...
    def __or__(self, other: Any) -> 'PortReference': ...

class _on_board_startPaths:
    Trigger: ExecutionPath

class on_board_start(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_board_startPaths
    def __getattr__(self, name: str) -> PortReference: ...

class _on_wavePaths:
    Trigger: ExecutionPath

class on_wave(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_wavePaths
    wave: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _on_mouse_clickPaths:
    Trigger: ExecutionPath

class on_mouse_click(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_mouse_clickPaths
    item: PortReference
    column: PortReference
    isLeftButton: PortReference
    row: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _on_key_pressPaths:
    Trigger: ExecutionPath

class on_key_press(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_key_pressPaths
    def __getattr__(self, name: str) -> PortReference: ...

class _on_plant_createPaths:
    Trigger: ExecutionPath

class on_plant_create(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_plant_createPaths
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _on_plant_clickPaths:
    Trigger: ExecutionPath

class on_plant_click(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_plant_clickPaths
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _on_plant_diePaths:
    Trigger: ExecutionPath

class on_plant_die(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_plant_diePaths
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _on_zombie_diePaths:
    Trigger: ExecutionPath

class on_zombie_die(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_zombie_diePaths
    zombie: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _on_zombie_spawnPaths:
    Trigger: ExecutionPath

class on_zombie_spawn(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_zombie_spawnPaths
    zombie: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _set_plantPaths:
    OnCreated: ExecutionPath
    OnCreateFailed: ExecutionPath
    Trigger: ExecutionPath

class set_plant(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _set_plantPaths
    forcePlant: PortReference
    column: PortReference
    plant: PortReference
    row: PortReference
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _move_plantPaths:
    OnMoved: ExecutionPath
    Trigger: ExecutionPath

class move_plant(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _move_plantPaths
    force: PortReference
    column: PortReference
    plant: PortReference
    row: PortReference
    movedPlant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _heal_plantPaths:
    OnHealed: ExecutionPath
    Trigger: ExecutionPath

class heal_plant(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _heal_plantPaths
    healAmount: PortReference
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _damage_plantPaths:
    Trigger: ExecutionPath

class damage_plant(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _damage_plantPaths
    damage: PortReference
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _give_plant_shieldPaths:
    Trigger: ExecutionPath

class give_plant_shield(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _give_plant_shieldPaths
    shieldAmount: PortReference
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _modify_plant_attackPaths:
    OnModified: ExecutionPath
    Trigger: ExecutionPath

class modify_plant_attack(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _modify_plant_attackPaths
    multiplier: PortReference
    plant: PortReference
    plantOut: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _modify_plant_healthPaths:
    OnModified: ExecutionPath
    Trigger: ExecutionPath

class modify_plant_health(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _modify_plant_healthPaths
    multiplier: PortReference
    plant: PortReference
    plantOut: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _plant_splitPaths:
    pass

class plant_split(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _plant_splitPaths
    column: PortReference
    plant: PortReference
    row: PortReference
    attributeCountdown: PortReference
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_plants_in_cellPaths:
    pass

class get_plants_in_cell(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_plants_in_cellPaths
    row: PortReference
    plants: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _for_each_plantPaths:
    LoopBody: ExecutionPath
    OnCompleted: ExecutionPath
    Trigger: ExecutionPath

class for_each_plant(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _for_each_plantPaths
    currentIndex: PortReference
    plantList: PortReference
    currentPlant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _for_each_plant_typePaths:
    LoopBody: ExecutionPath
    OnCompleted: ExecutionPath
    Trigger: ExecutionPath

class for_each_plant_type(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _for_each_plant_typePaths
    plantTypeList: PortReference
    currentPlantType: PortReference
    currentIndex: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _plant_type_valuePaths:
    pass

class plant_type_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _plant_type_valuePaths
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _compare_plant_typePaths:
    Equal: ExecutionPath

class compare_plant_type(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _compare_plant_typePaths
    plantTypeA: PortReference
    plantTypeB: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _single_plant_type_listPaths:
    pass

class single_plant_type_list(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _single_plant_type_listPaths
    plantTypeList: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _plant_type_list_storagePaths:
    OnComplete: ExecutionPath
    Trigger: ExecutionPath

class plant_type_list_storage(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _plant_type_list_storagePaths
    list: PortReference
    count: PortReference
    currentList: PortReference
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _merge_plant_type_listsPaths:
    pass

class merge_plant_type_lists(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _merge_plant_type_listsPaths
    count: PortReference
    listB: PortReference
    listA: PortReference
    mergedList: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_random_plant_typePaths:
    pass

class get_random_plant_type(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_random_plant_typePaths
    list: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _remove_plant_typePaths:
    Success: ExecutionPath

class remove_plant_type(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _remove_plant_typePaths
    list: PortReference
    resultList: PortReference
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_zombiePaths:
    OnCreated: ExecutionPath
    Trigger: ExecutionPath

class create_zombie(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_zombiePaths
    zombieType: PortReference
    column: PortReference
    isMindControlled: PortReference
    zombie: PortReference
    row: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _damage_zombiePaths:
    Trigger: ExecutionPath

class damage_zombie(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _damage_zombiePaths
    damage: PortReference
    zombie: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _set_zombie_mind_controlledPaths:
    Trigger: ExecutionPath

class set_zombie_mind_controlled(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _set_zombie_mind_controlledPaths
    zombie: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_nearest_zombiePaths:
    pass

class get_nearest_zombie(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_nearest_zombiePaths
    row: PortReference
    zombie: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _modify_zombie_healthPaths:
    OnModified: ExecutionPath
    Trigger: ExecutionPath

class modify_zombie_health(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _modify_zombie_healthPaths
    zombieOut: PortReference
    ratio: PortReference
    zombie: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _zombie_splitPaths:
    pass

class zombie_split(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _zombie_splitPaths
    zombieType: PortReference
    isHypnotized: PortReference
    column: PortReference
    zombie: PortReference
    row: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _zombie_type_valuePaths:
    pass

class zombie_type_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _zombie_type_valuePaths
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _compare_zombie_typePaths:
    Equal: ExecutionPath

class compare_zombie_type(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _compare_zombie_typePaths
    zombieTypeB: PortReference
    zombieTypeA: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _show_textPaths:
    Trigger: ExecutionPath

class show_text(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _show_textPaths
    duration: PortReference
    text: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_travel_entryPaths:
    Trigger: ExecutionPath

class get_travel_entry(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_travel_entryPaths
    def __getattr__(self, name: str) -> PortReference: ...

class _create_gravePaths:
    Trigger: ExecutionPath

class create_grave(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_gravePaths
    row: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _add_sunPaths:
    Trigger: ExecutionPath

class add_sun(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _add_sunPaths
    sunAmount: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _use_sunPaths:
    OnFailed: ExecutionPath
    Trigger: ExecutionPath
    OnSuccess: ExecutionPath

class use_sun(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _use_sunPaths
    sunAmount: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _add_moneyPaths:
    Trigger: ExecutionPath

class add_money(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _add_moneyPaths
    moneyAmount: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _use_moneyPaths:
    OnFailed: ExecutionPath
    Trigger: ExecutionPath
    OnSuccess: ExecutionPath

class use_money(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _use_moneyPaths
    moneyAmount: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _game_overPaths:
    Trigger: ExecutionPath

class game_over(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _game_overPaths
    reason: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _game_winPaths:
    Trigger: ExecutionPath

class game_win(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _game_winPaths
    def __getattr__(self, name: str) -> PortReference: ...

class _show_multiple_choice_menuPaths:
    ActionOnExit: ExecutionPath
    ActionOnRefresh: ExecutionPath
    Trigger: ExecutionPath

class show_multiple_choice_menu(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _show_multiple_choice_menuPaths
    refreshCount: PortReference
    options: PortReference
    cancelable: PortReference
    refreshable: PortReference
    windowCount: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _add_multiple_choice_optionPaths:
    pass

class add_multiple_choice_option(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _add_multiple_choice_optionPaths
    zombieType: PortReference
    description: PortReference
    title: PortReference
    list: PortReference
    optionSelected: PortReference
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _merge_multiple_choice_option_listsPaths:
    pass

class merge_multiple_choice_option_lists(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _merge_multiple_choice_option_listsPaths
    list2: PortReference
    list1: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _delete_card_by_typePaths:
    Trigger: ExecutionPath
    Completed: ExecutionPath

class delete_card_by_type(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _delete_card_by_typePaths
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_plant_cardPaths:
    OnCreated: ExecutionPath
    Trigger: ExecutionPath

class create_plant_card(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_plant_cardPaths
    column: PortReference
    row: PortReference
    outPlantType: PortReference
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _add_plant_cardPaths:
    OnPlant: ExecutionPath
    Failed: ExecutionPath
    Success: ExecutionPath
    Trigger: ExecutionPath

class add_plant_card(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _add_plant_cardPaths
    cost: PortReference
    plantedPlant: PortReference
    cooldown: PortReference
    useDefaultData: PortReference
    plantType: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_ice_shroom_effectPaths:
    Trigger: ExecutionPath

class create_ice_shroom_effect(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_ice_shroom_effectPaths
    duration: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_jalapeno_effectPaths:
    Trigger: ExecutionPath

class create_jalapeno_effect(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_jalapeno_effectPaths
    row: PortReference
    damage: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_doom_shroom_effectPaths:
    Trigger: ExecutionPath

class create_doom_shroom_effect(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_doom_shroom_effectPaths
    column: PortReference
    damage: PortReference
    row: PortReference
    setPit: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_cherry_explodePaths:
    Trigger: ExecutionPath

class create_cherry_explode(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_cherry_explodePaths
    row: PortReference
    damage: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_ladderPaths:
    Trigger: ExecutionPath

class create_ladder(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_ladderPaths
    row: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_craterPaths:
    Trigger: ExecutionPath

class create_crater(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_craterPaths
    row: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_ice_blockPaths:
    Trigger: ExecutionPath

class create_ice_block(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_ice_blockPaths
    row: PortReference
    plantType: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_zombie_explodePaths:
    Trigger: ExecutionPath

class create_zombie_explode(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_zombie_explodePaths
    row: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _branch_nodePaths:
    Trigger: ExecutionPath
    Else: ExecutionPath
    Then: ExecutionPath

class branch_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _branch_nodePaths
    condition: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _wait_nodePaths:
    Trigger: ExecutionPath
    Output: ExecutionPath

class wait_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _wait_nodePaths
    duration: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _for_loop_nodePaths:
    Trigger: ExecutionPath
    Output: ExecutionPath

class for_loop_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _for_loop_nodePaths
    count: PortReference
    index: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _toggle_cycle_nodePaths:
    OnEnable: ExecutionPath
    Cycle: ExecutionPath
    Trigger: ExecutionPath
    OnDisable: ExecutionPath

class toggle_cycle_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _toggle_cycle_nodePaths
    interval: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _toggle_nodePaths:
    Trigger: ExecutionPath
    OnChanged: ExecutionPath

class toggle_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _toggle_nodePaths
    state: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _pulse_nodePaths:
    Trigger: ExecutionPath
    OnPulse: ExecutionPath

class pulse_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _pulse_nodePaths
    state: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _counter_nodePaths:
    OnCount: ExecutionPath
    Trigger: ExecutionPath

class counter_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _counter_nodePaths
    count: PortReference
    shouldReset: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _not_nodePaths:
    Output: ExecutionPath

class not_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _not_nodePaths
    input: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _and_nodePaths:
    Output: ExecutionPath

class and_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _and_nodePaths
    a: PortReference
    b: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _or_nodePaths:
    Output: ExecutionPath

class or_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _or_nodePaths
    a: PortReference
    b: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _compare_intPaths:
    Greater: ExecutionPath
    Equal: ExecutionPath
    Less: ExecutionPath

class compare_int(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _compare_intPaths
    valueB: PortReference
    valueA: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _compare_floatPaths:
    Greater: ExecutionPath
    Equal: ExecutionPath
    Less: ExecutionPath

class compare_float(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _compare_floatPaths
    valueB: PortReference
    valueA: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _compare_game_objectPaths:
    Equal: ExecutionPath

class compare_game_object(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _compare_game_objectPaths
    gameObjectA: PortReference
    gameObjectB: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _add_nodePaths:
    pass

class add_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _add_nodePaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _subtract_nodePaths:
    pass

class subtract_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _subtract_nodePaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _multiply_nodePaths:
    pass

class multiply_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _multiply_nodePaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _divide_nodePaths:
    pass

class divide_node(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _divide_nodePaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_addPaths:
    pass

class int_add(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_addPaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_subtractPaths:
    pass

class int_subtract(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_subtractPaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_multiplyPaths:
    pass

class int_multiply(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_multiplyPaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_dividePaths:
    pass

class int_divide(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_dividePaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_moduloPaths:
    pass

class int_modulo(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_moduloPaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _string_concatPaths:
    pass

class string_concat(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _string_concatPaths
    a: PortReference
    b: PortReference
    result: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _random_intPaths:
    pass

class random_int(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _random_intPaths
    min: PortReference
    result: PortReference
    max: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _random_floatPaths:
    pass

class random_float(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _random_floatPaths
    min: PortReference
    result: PortReference
    max: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_to_floatPaths:
    pass

class int_to_float(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_to_floatPaths
    float: PortReference
    int: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _float_to_intPaths:
    pass

class float_to_int(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _float_to_intPaths
    float: PortReference
    int: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _float_to_stringPaths:
    pass

class float_to_string(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _float_to_stringPaths
    result: PortReference
    value: PortReference
    decimals: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_sun_amountPaths:
    pass

class get_sun_amount(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_sun_amountPaths
    sunAmount: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_valuePaths:
    pass

class int_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_valuePaths
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _float_valuePaths:
    pass

class float_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _float_valuePaths
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _bool_valuePaths:
    pass

class bool_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _bool_valuePaths
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _string_valuePaths:
    pass

class string_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _string_valuePaths
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _on_game_startPaths:
    Trigger: ExecutionPath

class on_game_start(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_game_startPaths
    def __getattr__(self, name: str) -> PortReference: ...

class _on_plant_death_completePaths:
    Trigger: ExecutionPath

class on_plant_death_complete(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _on_plant_death_completePaths
    dieReason: PortReference
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _die_plantPaths:
    Trigger: ExecutionPath
    OnCompleted: ExecutionPath

class die_plant(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _die_plantPaths
    plant: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_all_plantsPaths:
    pass

class get_all_plants(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_all_plantsPaths
    plants: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _move_zombiePaths:
    OnMoved: ExecutionPath
    Trigger: ExecutionPath

class move_zombie(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _move_zombiePaths
    column: PortReference
    movedZombie: PortReference
    zombie: PortReference
    row: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _play_zombie_animPaths:
    Trigger: ExecutionPath

class play_zombie_anim(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _play_zombie_animPaths
    zombie: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _play_soundPaths:
    Trigger: ExecutionPath

class play_sound(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _play_soundPaths
    soundId: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_particlePaths:
    Trigger: ExecutionPath

class create_particle(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_particlePaths
    row: PortReference
    column: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _create_info_cardPaths:
    Trigger: ExecutionPath
    OnCardClicked: ExecutionPath

class create_info_card(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _create_info_cardPaths
    smallTitle: PortReference
    bigTitle: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _random_triggerPaths:
    Trigger: ExecutionPath
    Output: ExecutionPath

class random_trigger(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _random_triggerPaths
    count: PortReference
    allowRepeat: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_travel_buffPaths:
    Trigger: ExecutionPath
    OnSuccess: ExecutionPath

class get_travel_buff(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_travel_buffPaths
    def __getattr__(self, name: str) -> PortReference: ...

class _get_int_variable_valuePaths:
    pass

class get_int_variable_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_int_variable_valuePaths
    variable: PortReference
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _set_int_variable_valuePaths:
    OnComplete: ExecutionPath
    Trigger: ExecutionPath

class set_int_variable_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _set_int_variable_valuePaths
    value: PortReference
    variableOut: PortReference
    variable: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_float_variable_valuePaths:
    pass

class get_float_variable_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_float_variable_valuePaths
    variable: PortReference
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _set_float_variable_valuePaths:
    OnComplete: ExecutionPath
    Trigger: ExecutionPath

class set_float_variable_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _set_float_variable_valuePaths
    value: PortReference
    variableOut: PortReference
    variable: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _get_bool_variable_valuePaths:
    pass

class get_bool_variable_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _get_bool_variable_valuePaths
    variable: PortReference
    value: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _set_bool_variable_valuePaths:
    OnComplete: ExecutionPath
    Trigger: ExecutionPath

class set_bool_variable_value(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _set_bool_variable_valuePaths
    value: PortReference
    variableOut: PortReference
    variable: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _int_variablePaths:
    pass

class int_variable(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _int_variablePaths
    variable: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _float_variablePaths:
    pass

class float_variable(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _float_variablePaths
    variable: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _bool_variablePaths:
    pass

class bool_variable(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _bool_variablePaths
    variable: PortReference
    def __getattr__(self, name: str) -> PortReference: ...

class _multi_plant_type_listPaths:
    pass

class multi_plant_type_list(BaseNode):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    Output: _multi_plant_type_listPaths
    plantTypeList: PortReference
    def __getattr__(self, name: str) -> PortReference: ...
