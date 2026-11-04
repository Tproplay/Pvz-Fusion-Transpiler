from __future__ import annotations

from enum import Enum
from typing import Any, Optional, Union, Sequence, TypeVar, Generic, Tuple
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....typing import to_port, to_int_port, to_float_port, to_bool_port, to_string_port


class ListOperation:
    """Represents a state-mutating list operation with execution branches."""

    def __init__(self, node: Any) -> None:
        self.node = node
        self._complete_path = ExecutionPath(self.node, "完成")
        self._failed_path = ExecutionPath(self.node, "失败")
        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = self._complete_path

    def __enter__(self) -> ListOperation:
        self._complete_path.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self._complete_path.__exit__(exc_type, exc_val, exc_tb)

    @property
    def Failed(self) -> ExecutionPath:
        return self._failed_path

    @property
    def failed(self) -> ExecutionPath:
        return self._failed_path

    @property
    def Complete(self) -> ExecutionPath:
        return self._complete_path

    @property
    def complete(self) -> ExecutionPath:
        return self._complete_path


def _resolve_type_key(elem_type: Any) -> str:
    """Normalizes an element type specification into a canonical type string."""
    if elem_type is None:
        return "int"

    if isinstance(elem_type, str):
        key = elem_type.strip().lower()
        if key in ("int", "integer"):
            return "int"
        if key in ("float", "single", "double"):
            return "float"
        if key in ("bool", "boolean"):
            return "bool"
        if key in ("str", "string", "text"):
            return "string"
        if key in ("gameobject", "worldobject", "object", "entity"):
            return "object"
        if key in ("planttype", "plant_type", "plant"):
            return "plant_type"
        if key in ("zombietype", "zombie_type", "zombie"):
            return "zombie_type"
        return key

    name = getattr(elem_type, "__name__", str(elem_type)).lower()
    if "zombie" in name:
        return "zombie_type"
    if "plant" in name:
        return "plant_type"
    if "gameobject" in name or "worldobject" in name or name == "object":
        return "object"
    if "int" in name:
        return "int"
    if "float" in name:
        return "float"
    if "bool" in name:
        return "bool"
    if "str" in name:
        return "string"

    return "int"


class List:
    """Generic list variable wrapper representing a C#-style List<T> on the node canvas."""

    _element_type_spec: Any = "int"

    def __class_getitem__(cls, item: Any) -> type[List]:
        type_key = _resolve_type_key(item)

        class _BoundList(cls):
            _element_type_spec = type_key

        item_name = getattr(item, "__name__", str(item))
        _BoundList.__name__ = f"List[{item_name}]"
        _BoundList.__qualname__ = f"List[{item_name}]"
        return _BoundList

    def __init__(
        self,
        initial: Any = None,
        name: str = "列表",
        element_type: Any = None,
    ) -> None:
        if element_type is not None:
            self._type_key: str = _resolve_type_key(element_type)
        else:
            self._type_key = _resolve_type_key(getattr(self, "_element_type_spec", "int"))

        self._current_port: Any = None

        if initial is None:
            var_node = nodes.list_variable(name=name, value=[])
            self._current_port = var_node.port_output_listvariable_Variable
        elif isinstance(initial, List):
            self._current_port = initial.list_port
        elif isinstance(initial, (list, tuple, set)):
            items = list(initial)
            if self._type_key == "zombie_type":
                for item in items:
                    if isinstance(item, (int, float)) and not isinstance(item, Enum):
                        raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
            elif self._type_key == "plant_type":
                for item in items:
                    if isinstance(item, (int, float)) and not isinstance(item, Enum):
                        raise TypeError("PlantType must be handled through the PlantType enum, direct int input is not allowed.")
            raw_items = [
                int(item.value) if isinstance(item, Enum) else item
                for item in items
            ]
            var_node = nodes.list_variable(name=name, value=raw_items)
            self._current_port = var_node.port_output_listvariable_Variable
        elif hasattr(initial, "list_port"):
            self._current_port = initial.list_port
        else:
            # Check if it's already a Port
            self._current_port = to_port(initial)

    @property
    def list_port(self) -> Any:
        return self._current_port

    def _get_primary_port(self) -> Any:
        return self._current_port

    @property
    def Count(self) -> Any:
        """Returns the length port (Int) of this list."""
        return nodes.get_list_length(list_var=self._current_port).port_output_int_Length

    count = Count

    # -------------------------------------------------------------------------
    # Value Coercion by Element Type
    # -------------------------------------------------------------------------
    def _coerce_item_port(self, val: Any) -> Any:
        key = self._type_key
        if key == "int":
            return to_int_port(val)
        elif key == "float":
            return to_float_port(val)
        elif key == "bool":
            return to_bool_port(val)
        elif key == "string":
            return to_string_port(val)
        elif key == "plant_type":
            if isinstance(val, (int, float)) and not isinstance(val, Enum):
                raise TypeError("PlantType must be handled through the PlantType enum, direct int input is not allowed.")
            if isinstance(val, Enum):
                return nodes.plant_type_value(plant_type=val).port_output_planttype_PlantType
            return to_port(val)
        elif key == "zombie_type":
            if isinstance(val, (int, float)) and not isinstance(val, Enum):
                raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
            if isinstance(val, Enum):
                return nodes.zombie_type_value(zombie_type=val).port_output_zombietype_ZombieType
            return to_port(val)
        elif key == "object":
            return to_port(val)
        return to_port(val)

    # -------------------------------------------------------------------------
    # Add / Append
    # -------------------------------------------------------------------------
    def Add(self, item: Any) -> ListOperation:
        """Appends an item to the end of the list."""
        port = self._coerce_item_port(item)
        key = self._type_key
        if key == "int":
            node = nodes.append_int_list(list_var=self._current_port, value=port)
        elif key == "float":
            node = nodes.append_float_list(list_var=self._current_port, value=port)
        elif key == "bool":
            node = nodes.append_bool_list(list_var=self._current_port, value=port)
        elif key == "string":
            node = nodes.append_string_list(list_var=self._current_port, value=port)
        elif key == "plant_type":
            node = nodes.append_plant_type_list(list_var=self._current_port, value=port)
        elif key == "zombie_type":
            node = nodes.append_zombie_type_list(list_var=self._current_port, value=port)
        elif key == "object":
            node = nodes.append_object_list(list_var=self._current_port, value=port)
        else:
            node = nodes.append_int_list(list_var=self._current_port, value=port)

        self._current_port = node.port_output_listvariable_List
        return ListOperation(node)

    add = Add
    append = Add

    # -------------------------------------------------------------------------
    # Insert
    # -------------------------------------------------------------------------
    def Insert(self, index: Any, item: Any) -> ListOperation:
        """Inserts an item into the list at the specified index."""
        idx_port = to_int_port(index)
        val_port = self._coerce_item_port(item)
        key = self._type_key
        if key == "int":
            node = nodes.insert_int_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "float":
            node = nodes.insert_float_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "bool":
            node = nodes.insert_bool_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "string":
            node = nodes.insert_string_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "plant_type":
            node = nodes.insert_plant_type_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "zombie_type":
            node = nodes.insert_zombie_type_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "object":
            node = nodes.insert_object_list(list_var=self._current_port, index=idx_port, value=val_port)
        else:
            node = nodes.insert_int_list(list_var=self._current_port, index=idx_port, value=val_port)

        self._current_port = node.port_output_listvariable_List
        return ListOperation(node)

    insert = Insert

    # -------------------------------------------------------------------------
    # Replace / Indexer Assignment
    # -------------------------------------------------------------------------
    def Replace(self, index: Any, item: Any) -> ListOperation:
        """Replaces the element at the specified index with a new item."""
        idx_port = to_int_port(index)
        val_port = self._coerce_item_port(item)
        key = self._type_key
        if key == "int":
            node = nodes.replace_int_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "float":
            node = nodes.replace_float_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "bool":
            node = nodes.replace_bool_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "string":
            node = nodes.replace_string_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "plant_type":
            node = nodes.replace_plant_type_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "zombie_type":
            node = nodes.replace_zombie_type_list(list_var=self._current_port, index=idx_port, value=val_port)
        elif key == "object":
            node = nodes.replace_object_list(list_var=self._current_port, index=idx_port, value=val_port)
        else:
            node = nodes.replace_int_list(list_var=self._current_port, index=idx_port, value=val_port)

        self._current_port = node.port_output_listvariable_List
        return ListOperation(node)

    replace = Replace

    def __setitem__(self, index: Any, item: Any) -> None:
        self.Replace(index, item)

    # -------------------------------------------------------------------------
    # GetItem / Indexer Lookup & TryGetValue
    # -------------------------------------------------------------------------
    def _get_item_node(self, index: Any) -> Any:
        idx_port = to_int_port(index)
        key = self._type_key
        if key == "int":
            return nodes.get_int_list_item(list_var=self._current_port, index=idx_port)
        elif key == "float":
            return nodes.get_float_list_item(list_var=self._current_port, index=idx_port)
        elif key == "bool":
            return nodes.get_bool_list_item(list_var=self._current_port, index=idx_port)
        elif key == "string":
            return nodes.get_string_list_item(list_var=self._current_port, index=idx_port)
        elif key == "plant_type":
            return nodes.get_plant_type_list_item(list_var=self._current_port, index=idx_port)
        elif key == "zombie_type":
            return nodes.get_zombie_type_list_item(list_var=self._current_port, index=idx_port)
        elif key == "object":
            return nodes.get_object_list_item(list_var=self._current_port, index=idx_port)
        return nodes.get_int_list_item(list_var=self._current_port, index=idx_port)

    def __getitem__(self, index: Any) -> Any:
        node = self._get_item_node(index)
        for attr in ("port_output_int_Value", "port_output_float_Value", "port_output_bool_Value",
                     "port_output_string_Value", "port_output_planttype_Value",
                     "port_output_zombietype_Value", "port_output_gameobject_Value"):
            if hasattr(node, attr):
                return getattr(node, attr)
        return node.get_output("值")

    get_item = __getitem__
    Get = __getitem__

    def TryGetValue(self, index: Any) -> Tuple[Any, Any]:
        """Returns a tuple (value_port, ok_port) checking whether index access is valid."""
        node = self._get_item_node(index)
        val_port = self[index]
        ok_port = getattr(node, "port_output_bool_Valid", node.get_output("有效"))
        return val_port, ok_port

    try_get_value = TryGetValue

    # -------------------------------------------------------------------------
    # IndexOf / Contains / TryFindIndex
    # -------------------------------------------------------------------------
    def _find_value_node(self, item: Any) -> Any:
        val_port = self._coerce_item_port(item)
        key = self._type_key
        if key == "int":
            return nodes.find_int_list_value(list_var=self._current_port, value=val_port)
        elif key == "float":
            return nodes.find_float_list_value(list_var=self._current_port, value=val_port)
        elif key == "bool":
            return nodes.find_bool_list_value(list_var=self._current_port, value=val_port)
        elif key == "string":
            return nodes.find_string_list_value(list_var=self._current_port, value=val_port)
        elif key == "plant_type":
            return nodes.find_plant_type_list_value(list_var=self._current_port, value=val_port)
        elif key == "zombie_type":
            return nodes.find_zombie_type_list_value(list_var=self._current_port, value=val_port)
        elif key == "object":
            return nodes.find_object_list_value(list_var=self._current_port, value=val_port)
        return nodes.find_int_list_value(list_var=self._current_port, value=val_port)

    def IndexOf(self, item: Any) -> Any:
        """Returns the index port of the searched item in the list."""
        node = self._find_value_node(item)
        return node.port_output_int_Index

    index_of = IndexOf
    find_index = IndexOf

    def Contains(self, item: Any) -> Any:
        """Returns a Bool port indicating whether the item exists in the list."""
        node = self._find_value_node(item)
        return node.port_output_bool_Contains

    contains = Contains

    def TryFindIndex(self, item: Any) -> Tuple[Any, Any]:
        """Returns a tuple (index_port, found_port)."""
        node = self._find_value_node(item)
        return node.port_output_int_Index, node.port_output_bool_Contains

    try_find_index = TryFindIndex

    # -------------------------------------------------------------------------
    # RemoveAt / Clear
    # -------------------------------------------------------------------------
    def RemoveAt(self, index: Any) -> ListOperation:
        """Removes the item at the specified index from the list."""
        idx_port = to_int_port(index)
        node = nodes.remove_list_item(list_var=self._current_port, index=idx_port)
        return ListOperation(node)

    remove_at = RemoveAt

    def Clear(self) -> ListOperation:
        """Clears all elements from the list."""
        node = nodes.clear_list_values(list_var=self._current_port)
        return ListOperation(node)

    clear = Clear

    # -------------------------------------------------------------------------
    # CopyTo / Clone
    # -------------------------------------------------------------------------
    def CopyTo(self, target: Any) -> ListOperation:
        """Copies all elements from this list into the target list."""
        target_port = target.list_port if hasattr(target, "list_port") else to_port(target)
        node = nodes.copy_list_values(source_list=self._current_port, target_list=target_port)
        return ListOperation(node)

    copy_to = CopyTo

    def Clone(self, name: str = "克隆列表") -> List:
        """Creates a new list variable of the same type and copies values into it."""
        new_list: List = List(name=name, element_type=self._type_key)
        self.CopyTo(new_list)
        return new_list

    clone = Clone

    # -------------------------------------------------------------------------
    # Operator Overloads
    # -------------------------------------------------------------------------
    def __iadd__(self, other: Any) -> List:
        if isinstance(other, (list, tuple, set)):
            for item in other:
                self.Add(item)
        elif isinstance(other, List):
            with ForEach(other) as loop_item:
                self.Add(loop_item)
        else:
            self.Add(other)
        return self

    def __iter__(self) -> Any:
        raise TypeError(
            "Direct Python iteration over a List canvas variable is not supported. "
            "Use 'with ForEach(list) as item:' to iterate on the graph canvas."
        )


class ForEach:
    """Context manager for iterating over a List[T] on the graph canvas."""

    def __init__(self, target_list: Any) -> None:
        if hasattr(target_list, "Count"):
            count_port = target_list.Count
        elif hasattr(target_list, "count"):
            count_port = target_list.count
        else:
            count_port = nodes.get_list_length(list_var=to_port(target_list)).port_output_int_Length

        from ..Loops.loops import For
        self._for_loop = For(count_port)
        self._target_list = target_list
        self._item_port: Any = None

    def __enter__(self) -> Any:
        self._for_loop.__enter__()
        self._item_port = self._target_list[self._for_loop.index]
        return self._item_port

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self._for_loop.__exit__(exc_type, exc_val, exc_tb)

    @property
    def index(self) -> Any:
        return self._for_loop.index

    @property
    def on_complete(self) -> Any:
        return self._for_loop.on_complete

    @property
    def Complete(self) -> Any:
        return self._for_loop.on_complete


# Concrete type aliases
IntList = List[int]
FloatList = List[float]
BoolList = List[bool]
StringList = List[str]
ObjectList = List["object"]
PlantTypeListVar = List["plant_type"]


__all__ = [
    "List",
    "ListOperation",
    "ForEach",
    "IntList",
    "FloatList",
    "BoolList",
    "StringList",
    "ObjectList",
    "PlantTypeListVar",
]
