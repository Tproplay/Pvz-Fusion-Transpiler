# pyright: reportIncompatibleMethodOverride=none
from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
from typing import Any
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....port_types import to_port, to_int_port
from ..Variables.list_var import List, ListOperation


class ZombieTypeList(List):
    """A smart wrapper representing a dynamic or static list of Zombie Types on the node canvas.

    Supports native collection operations (addition, searching, indexing, contains checks)
    directly translated into graph nodes.
    """

    def __init__(self, initial: Any | None = None, initialize_empty: bool = True) -> None:
        super().__init__(initial=initial, name="僵尸类型列表", element_type="zombie_type")
        self._count_port: Any = None
        if initial is None:
            self._count_port = nodes.int_value(val=0).port_output_int_Value
        elif isinstance(initial, (Enum, int)):
            self._count_port = nodes.int_value(val=1).port_output_int_Value
        elif isinstance(initial, (list, tuple, set)):
            self._count_port = nodes.int_value(val=len(initial)).port_output_int_Value
        elif isinstance(initial, ZombieTypeList) and initial._count_port is not None:
            self._count_port = initial._count_port

    @property
    def count(self) -> Any:
        if self._count_port is not None:
            return self._count_port
        return super().Count

    @property
    def Count(self) -> Any:
        return self.count

    def set(self, other: ZombieTypeList | Iterable | Enum | int | Any) -> ZombieTypeList:
        new_list = ZombieTypeList(other)
        self._root_port = new_list.list_port
        self._count_port = new_list.count
        return self

    def _contains_single(self, target_type: Any) -> Any:
        return self.Contains(target_type)

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

    def append(self, zombie_type: Any) -> ZombieTypeList:
        self.Add(zombie_type)
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
            with ForEachZombieType(other) as loop:
                self.append(loop.zombie_type)
        return self

    def clear(self) -> ZombieTypeList:
        self.Clear()
        self._count_port = nodes.int_value(val=0).port_output_int_Value
        return self

    def remove_at(self, index: Any) -> ZombieTypeList:
        self.RemoveAt(index)
        self._count_port = nodes.int_subtract(a=self.count, b=1).port_output_int_Diff
        return self


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
