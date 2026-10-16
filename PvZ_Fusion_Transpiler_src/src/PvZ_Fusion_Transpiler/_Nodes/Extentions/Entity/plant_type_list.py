from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
from typing import Any
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....typing import to_port


class PlantTypeList:
    """A smart wrapper representing a dynamic or static list of Plant Types on the node canvas.

    Supports native collection operations (addition, subtraction, merging) and conditional 
    checks directly translated into graph nodes.
    """

    def __init__(self, initial: Any | None = None, initialize_empty: bool = True) -> None:
        self._current_port: Any = None
        self._count_port: Any = None

        if initial is None:
            storage = nodes.plant_type_list_storage(op=0, init_empty=initialize_empty)
            self._current_port = storage.port_output_planttypelist_CurrentList
            self._count_port = storage.port_output_int_Count

        elif isinstance(initial, (Enum, int)):
            val = initial.value if isinstance(initial, Enum) else int(initial)
            multi_node = nodes.multi_plant_type_list(plant_types=[val])
            self._current_port = multi_node.port_output_planttypelist_PlantTypeList
            self._count_port = nodes.int_value(val=1).port_output_int_Value

        elif isinstance(initial, (list, tuple, set)):
            items = list(initial)
            if len(items) == 0:
                storage = nodes.plant_type_list_storage(op=0, init_empty=initialize_empty)
                self._current_port = storage.port_output_planttypelist_CurrentList
                self._count_port = storage.port_output_int_Count
            else:
                raw_types = [
                    item.value if isinstance(item, Enum) else int(item)
                    for item in items
                ]
                multi_node = nodes.multi_plant_type_list(plant_types=raw_types)
                self._current_port = multi_node.port_output_planttypelist_PlantTypeList
                self._count_port = nodes.int_value(val=len(raw_types)).port_output_int_Value

        elif isinstance(initial, PlantTypeList):
            self._current_port = initial.list_port
            self._count_port = initial.count
        else:
            self._current_port = initial

    @property
    def list_port(self) -> Any:
        return self._current_port

    @property
    def count(self) -> Any:
        if self._count_port is not None:
            return self._count_port
        return self._current_port

    def set(self, other: PlantTypeList | Iterable | Enum | int | Any) -> PlantTypeList:
        new_list = PlantTypeList(other)
        self._current_port = new_list.list_port
        self._count_port = new_list.count
        return self

    def _contains_single(self, target_type: Any) -> Any:
        if isinstance(target_type, (int, float)) and not isinstance(target_type, Enum):
            raise TypeError("PlantType must be handled through the PlantType enum, direct int input is not allowed.")
        if isinstance(target_type, Enum):
            target_port = nodes.plant_type_value(val=target_type).port_output_planttype_PlantType
        elif hasattr(target_type, "_get_primary_port"):
            target_port = target_type._get_primary_port()
        else:
            target_port = to_port(target_type)

        parent_trigger = _ctx.trigger_stack[-1] if _ctx.trigger_stack else None

        saved_stack = _ctx.trigger_stack[:]
        _ctx.trigger_stack.clear()

        match_toggle = nodes.toggle_node(initial_state=False)
        reset_branch = nodes.branch_node(condition=match_toggle.port_output_bool_State)
        loop = nodes.for_each_plant_type(type_list=self._current_port)

        curr_type = loop.port_output_planttype_CurrentPlantType
        is_equal = nodes.compare_plant_type(a=curr_type, b=target_port).port_output_bool_Equal
        match_branch = nodes.branch_node(condition=is_equal)
        state_guard = nodes.branch_node(condition=match_toggle.port_output_bool_State)

        if parent_trigger:
            _ctx.add_connection(
                parent_trigger.id, parent_trigger.out_trigger, reset_branch.id, reset_branch.port_input_trigger_Trigger.name
            )

        _ctx.add_connection(reset_branch.id, reset_branch.port_output_trigger_Then.name, match_toggle.id, match_toggle.port_input_trigger_Trigger.name)
        _ctx.add_connection(reset_branch.id, reset_branch.port_output_trigger_Then.name, loop.id, loop.port_input_trigger_Trigger.name)
        _ctx.add_connection(reset_branch.id, reset_branch.port_output_trigger_Else.name, loop.id, loop.port_input_trigger_Trigger.name)

        _ctx.add_connection(loop.id, loop.port_output_trigger_LoopBody.name, match_branch.id, match_branch.port_input_trigger_Trigger.name)
        _ctx.add_connection(match_branch.id, match_branch.port_output_trigger_Then.name, state_guard.id, state_guard.port_input_trigger_Trigger.name)
        _ctx.add_connection(state_guard.id, state_guard.port_output_trigger_Else.name, match_toggle.id, match_toggle.port_input_trigger_Trigger.name)

        _ctx.trigger_stack.extend(saved_stack)
        _ctx.trigger_stack[-1] = ExecutionPath(loop.port_output_trigger_LoopComplete)

        return match_toggle.port_output_bool_State

    def contains(self, plant_type: Enum | int | Iterable | Any) -> Any:
        if isinstance(plant_type, (list, set)):
            items = list(plant_type)
            if not items:
                return nodes.bool_value(val=True).port_output_bool_Value
            acc = self._contains_single(items[0])
            for item in items[1:]:
                acc = nodes.and_node(a=acc, b=self._contains_single(item)).port_output_bool_Result
            return acc
        return self._contains_single(plant_type)

    def __add__(self, other: Any) -> PlantTypeList:
        merged = PlantTypeList(self)
        merged += other
        return merged

    def __iadd__(self, other: Any) -> PlantTypeList:
        if isinstance(other, (Enum, int)):
            val = other.value if isinstance(other, Enum) else int(other)
            single_node = nodes.single_plant_type_list(plant_type=val)
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port,
                list_b=single_node.port_output_planttypelist_PlantTypeList,
            )
            self._current_port = merge_node.port_output_planttypelist_MergedList
            self._count_port = nodes.int_add(a=self.count, b=1).port_output_int_Sum

        elif isinstance(other, PlantTypeList):
            merge_node = nodes.merge_plant_type_lists(
                list_a=self._current_port, list_b=other.list_port
            )
            self._current_port = merge_node.port_output_planttypelist_MergedList
            self._count_port = nodes.int_add(a=self.count, b=other.count).port_output_int_Sum

        elif isinstance(other, (list, set, tuple)):
            for item in other:
                self += item
        return self

    def __sub__(self, other: Any) -> PlantTypeList:
        subbed = PlantTypeList(self)
        subbed -= other
        return subbed

    def __isub__(self, other: Any) -> PlantTypeList:
        if isinstance(other, (Enum, int)):
            val = other.value if isinstance(other, Enum) else int(other)
            rem_node = nodes.remove_plant_type(
                type_list=self._current_port, target_type=val
            )
            self._current_port = rem_node.port_output_planttypelist_ResultList
            self._count_port = nodes.int_subtract(a=self.count, b=1).port_output_int_Difference
        elif isinstance(other, (list, set, tuple)):
            for item in other:
                self -= item
        return self


__all__ = ["PlantTypeList"]
