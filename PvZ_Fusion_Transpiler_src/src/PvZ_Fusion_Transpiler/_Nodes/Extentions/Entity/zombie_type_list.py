from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
from typing import Any
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....typing import to_port, to_int_port


class ZombieTypeList:
    """A smart wrapper representing a dynamic or static list of Zombie Types on the node canvas.

    Supports native collection operations (addition, searching, indexing, contains checks)
    directly translated into graph nodes.
    """

    def __init__(self, initial: Any | None = None, initialize_empty: bool = True) -> None:
        self._current_port: Any = None
        self._count_port: Any = None

        if initial is None:
            var_node = nodes.list_variable(name="僵尸类型列表", value=[])
            self._current_port = var_node.port_output_listvariable_Variable
            self._count_port = nodes.int_value(val=0).port_output_int_Value

        elif isinstance(initial, (Enum, int)):
            if isinstance(initial, int) and not isinstance(initial, Enum):
                raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
            val = int(initial.value)
            var_node = nodes.list_variable(name="僵尸类型列表", value=[val])
            self._current_port = var_node.port_output_listvariable_Variable
            self._count_port = nodes.int_value(val=1).port_output_int_Value

        elif isinstance(initial, (list, tuple, set)):
            items = list(initial)
            for item in items:
                if isinstance(item, int) and not isinstance(item, Enum):
                    raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
            raw_types = [
                int(item.value) if isinstance(item, Enum) else int(item)
                for item in items
            ]
            var_node = nodes.list_variable(name="僵尸类型列表", value=raw_types)
            self._current_port = var_node.port_output_listvariable_Variable
            self._count_port = nodes.int_value(val=len(raw_types)).port_output_int_Value

        elif isinstance(initial, ZombieTypeList):
            self._current_port = initial.list_port
            self._count_port = initial.count
        else:
            self._current_port = to_port(initial)
            self._count_port = nodes.get_list_length(list_var=self._current_port).port_output_int_Length

    @property
    def list_port(self) -> Any:
        return self._current_port

    @property
    def count(self) -> Any:
        if self._count_port is not None:
            return self._count_port
        return self._current_port

    def set(self, other: ZombieTypeList | Iterable | Enum | int | Any) -> ZombieTypeList:
        new_list = ZombieTypeList(other)
        self._current_port = new_list.list_port
        self._count_port = new_list.count
        return self

    def _contains_single(self, target_type: Any) -> Any:
        if isinstance(target_type, (int, float)) and not isinstance(target_type, Enum):
            raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
        if isinstance(target_type, Enum):
            target_port = nodes.zombie_type_value(val=target_type).port_output_zombietype_ZombieType
        else:
            target_port = to_port(target_type)

        find_node = nodes.find_zombie_type_list_value(
            list_var=self._current_port,
            value=target_port,
        )
        return find_node.port_output_bool_Contains

    def contains(self, zombie_type: Enum | int | Iterable | Any) -> Any:
        if isinstance(zombie_type, (list, set, tuple)):
            items = list(zombie_type)
            if not items:
                return nodes.bool_value(val=True).port_output_bool_Value
            acc = self._contains_single(items[0])
            for item in items[1:]:
                acc = nodes.and_node(a=acc, b=self._contains_single(item)).port_output_bool_Result
            return acc
        return self._contains_single(zombie_type)

    def find_index(self, zombie_type: Any) -> Any:
        if isinstance(zombie_type, (int, float)) and not isinstance(zombie_type, Enum):
            raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
        if isinstance(zombie_type, Enum):
            target_port = nodes.zombie_type_value(val=zombie_type).port_output_zombietype_ZombieType
        else:
            target_port = to_port(zombie_type)

        find_node = nodes.find_zombie_type_list_value(
            list_var=self._current_port,
            value=target_port,
        )
        return find_node.port_output_int_Index

    def append(self, zombie_type: Any) -> ZombieTypeList:
        if isinstance(zombie_type, (int, float)) and not isinstance(zombie_type, Enum):
            raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
        if isinstance(zombie_type, Enum):
            target_port = nodes.zombie_type_value(val=zombie_type).port_output_zombietype_ZombieType
        else:
            target_port = to_port(zombie_type)

        app_node = nodes.append_zombie_type_list(
            list_var=self._current_port,
            value=target_port,
        )
        self._current_port = app_node.port_output_listvariable_List
        self._count_port = nodes.int_add(a=self.count, b=1).port_output_int_Sum
        return self

    def __add__(self, other: Any) -> ZombieTypeList:
        merged = ZombieTypeList(self)
        merged += other
        return merged

    def __iadd__(self, other: Any) -> ZombieTypeList:
        if isinstance(other, (Enum, int)):
            self.append(other)
        elif isinstance(other, (list, set, tuple)):
            for item in other:
                self.append(item)
        elif isinstance(other, ZombieTypeList):
            # Loop and append items or connect
            with ForEachZombieType(other) as loop:
                self.append(loop.zombie_type)
        return self

    def __getitem__(self, index: Any) -> Any:
        idx_port = to_int_port(index)
        item_node = nodes.get_zombie_type_list_item(
            list_var=self._current_port,
            index=idx_port,
        )
        return item_node.port_output_zombietype_Value

    get_item = __getitem__

    def clear(self) -> ZombieTypeList:
        clr = nodes.clear_list_values(list_var=self._current_port)
        self._current_port = clr.port_output_listvariable_List
        self._count_port = nodes.int_value(val=0).port_output_int_Value
        return self

    def remove_at(self, index: Any) -> ZombieTypeList:
        idx_port = to_int_port(index)
        rem = nodes.remove_list_item(list_var=self._current_port, index=idx_port)
        self._current_port = rem.port_output_listvariable_List
        self._count_port = nodes.int_subtract(a=self.count, b=1).port_output_int_Difference
        return self

    def _get_primary_port(self) -> Any:
        return self.list_port


class ForEachZombieType:
    """Context manager that iterates through a ZombieTypeList on the node canvas."""

    def __init__(self, type_list: Any) -> None:
        if hasattr(type_list, "list_port"):
            self.list_port = type_list.list_port
            self.count_port = type_list.count
        else:
            self.list_port = to_port(type_list)
            self.count_port = nodes.get_list_length(list_var=self.list_port).port_output_int_Length

        self.loop_node = nodes.for_loop(count=self.count_port)
        self.item_node = nodes.get_zombie_type_list_item(
            list_var=self.list_port,
            index=self.loop_node.port_output_int_Index,
        )

    def __enter__(self) -> ForEachZombieType:
        _ctx.trigger_stack.append(ExecutionPath(self.loop_node, self.loop_node.port_output_trigger_LoopBody.name))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if _ctx.trigger_stack and _ctx.trigger_stack[-1].id == self.loop_node.id:
            _ctx.trigger_stack.pop()

    @property
    def on_complete(self) -> Any:
        return ExecutionPath(self.loop_node, self.loop_node.port_output_trigger_Complete.name)

    @property
    def zombie_type(self) -> Any:
        return self.item_node.port_output_zombietype_Value

    type = zombie_type
    value = zombie_type

    @property
    def index(self) -> Any:
        return self.loop_node.port_output_int_Index

    def _get_primary_port(self) -> Any:
        return self.zombie_type

    def __eq__(self, other: Any) -> Any:
        return self.zombie_type == other

    def __ne__(self, other: Any) -> Any:
        return self.zombie_type != other


__all__ = ["ZombieTypeList", "ForEachZombieType"]
