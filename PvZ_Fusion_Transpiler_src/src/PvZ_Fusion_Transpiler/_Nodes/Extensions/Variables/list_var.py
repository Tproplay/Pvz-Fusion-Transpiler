from __future__ import annotations

from enum import Enum
from typing import Any, Tuple, TypeVar, Generic, Sequence, Optional
from ....Core.context import _ctx
from ..Abstract import ExecutionPath
from .... import nodes
from ....port_types import to_port, to_int_port, to_float_port, to_bool_port, to_string_port
from ...._Data.PlantType import PlantType
from ...._Data.ZombieType import ZombieType
from ..Types import Int, Float, Bool, String

T = TypeVar("T")


class ListOperation:
    """Represents a state-mutating list operation with execution branches."""

    def __init__(self, node: Any) -> None:
        self.node = node
        complete_port = getattr(node, "port_output_trigger_Complete", None)
        failed_port = getattr(node, "port_output_trigger_Failed", None)

        if complete_port is not None:
            self._complete_path = ExecutionPath(complete_port)
        else:
            self._complete_path = ExecutionPath(node, "Complete")

        if failed_port is not None:
            self._failed_path = ExecutionPath(failed_port)
        else:
            self._failed_path = ExecutionPath(node, "Failed")

        if _ctx.trigger_stack:
            _ctx.trigger_stack[-1] = self._complete_path

    def __enter__(self) -> ListOperation:
        self._complete_path.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self._complete_path.__exit__(exc_type, exc_val, exc_tb)

    @property
    def OnSuccess(self) -> ExecutionPath:
        return self._complete_path

    @property
    def OnComplete(self) -> ExecutionPath:
        return self._complete_path

    @property
    def Complete(self) -> ExecutionPath:
        return self._complete_path

    @property
    def complete(self) -> ExecutionPath:
        return self._complete_path

    @property
    def Failed(self) -> ExecutionPath:
        return self._failed_path

    @property
    def failed(self) -> ExecutionPath:
        return self._failed_path

    @property
    def OnFailed(self) -> ExecutionPath:
        return self._failed_path


_TYPE_KEYS: dict[Any, str] = {
    int: "int",
    float: "float",
    bool: "bool",
    str: "string",
    Int: "int",
    Float: "float",
    Bool: "bool",
    String: "string",
    PlantType: "plant_type",
    ZombieType: "zombie_type",
    "int": "int",
    "float": "float",
    "bool": "bool",
    "string": "string",
    "object": "object",
    "plant_type": "plant_type",
    "zombie_type": "zombie_type",
}


def _resolve_type_key(elem_type: Any) -> str:
    """Normalizes an element type specification into a canonical type string."""
    if elem_type is None:
        raise TypeError(
            "List requires an explicit element type. "
            "Use subscript syntax (e.g. List[Int]()) or a type alias (e.g. IntList())."
        )
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
        if key in ("planttype", "plant_type", "plant_types"):
            return "plant_type"
        if key in ("zombietype", "zombie_type", "zombie_types"):
            return "zombie_type"

    name = getattr(elem_type, "__name__", str(elem_type))
    if name in ("GameObject", "WorldObject"):
        return "object"
    if name in ("PlantType",):
        return "plant_type"
    if name in ("ZombieType",):
        return "zombie_type"

    try:
        return _TYPE_KEYS[elem_type]
    except (KeyError, TypeError):
        raise TypeError(
            f"Unsupported List element type: {elem_type!r}. "
            "Supported types are Int, Float, Bool, String, GameObject, PlantType, ZombieType."
        )


_OPS: dict[str, dict[str, Any]] = {
    "int": {
        "append": nodes.append_int_list,
        "insert": nodes.insert_int_list,
        "replace": nodes.replace_int_list,
        "get": nodes.get_int_list_item,
        "find": nodes.find_int_list_value,
        "value_port": "port_output_int_Value",
    },
    "float": {
        "append": nodes.append_float_list,
        "insert": nodes.insert_float_list,
        "replace": nodes.replace_float_list,
        "get": nodes.get_float_list_item,
        "find": nodes.find_float_list_value,
        "value_port": "port_output_float_Value",
    },
    "bool": {
        "append": nodes.append_bool_list,
        "insert": nodes.insert_bool_list,
        "replace": nodes.replace_bool_list,
        "get": nodes.get_bool_list_item,
        "find": nodes.find_bool_list_value,
        "value_port": "port_output_bool_Value",
    },
    "string": {
        "append": nodes.append_string_list,
        "insert": nodes.insert_string_list,
        "replace": nodes.replace_string_list,
        "get": nodes.get_string_list_item,
        "find": nodes.find_string_list_value,
        "value_port": "port_output_string_Value",
    },
    "plant_type": {
        "append": nodes.append_plant_type_list,
        "insert": nodes.insert_plant_type_list,
        "replace": nodes.replace_plant_type_list,
        "get": nodes.get_plant_type_list_item,
        "find": nodes.find_plant_type_list_value,
        "value_port": "port_output_planttype_Value",
    },
    "zombie_type": {
        "append": nodes.append_zombie_type_list,
        "insert": nodes.insert_zombie_type_list,
        "replace": nodes.replace_zombie_type_list,
        "get": nodes.get_zombie_type_list_item,
        "find": nodes.find_zombie_type_list_value,
        "value_port": "port_output_zombietype_Value",
    },
    "object": {
        "append": nodes.append_object_list,
        "insert": nodes.insert_object_list,
        "replace": nodes.replace_object_list,
        "get": nodes.get_object_list_item,
        "find": nodes.find_object_list_value,
        "value_port": "port_output_gameobject_Value",
    },
}

_BOUND_LIST_CACHE: dict[tuple[type, str], type[List]] = {}
_list_counter = 0


def _get_default_list_name() -> str:
    global _list_counter
    _list_counter += 1
    return f"列表_{_list_counter}"


def _validate_initial_items(items: list[Any], type_key: str) -> list[Any]:
    if type_key == "plant_type":
        for item in items:
            if isinstance(item, (int, float)) and not isinstance(item, Enum):
                raise TypeError("PlantType must be handled through the PlantType enum; direct int input is not allowed.")
            if isinstance(item, Enum) and type(item).__name__ != "PlantType":
                raise TypeError(f"Expected PlantType enum member in initial list, got {type(item).__name__}: {item!r}")
    elif type_key == "zombie_type":
        for item in items:
            if isinstance(item, (int, float)) and not isinstance(item, Enum):
                raise TypeError("ZombieType must be handled through the ZombieType enum; direct int input is not allowed.")
            if isinstance(item, Enum) and type(item).__name__ != "ZombieType":
                raise TypeError(f"Expected ZombieType enum member in initial list, got {type(item).__name__}: {item!r}")
    return [int(item.value) if isinstance(item, Enum) else item for item in items]


class List(Generic[T]):
    """Generic list variable wrapper representing a C#-style List<T> on the node canvas."""

    _element_type_spec: Optional[str] = None

    def __class_getitem__(cls, item: Any) -> type[List]:
        type_key = _resolve_type_key(item)
        cache_key = (cls, type_key)
        if cache_key in _BOUND_LIST_CACHE:
            return _BOUND_LIST_CACHE[cache_key]

        class _BoundList(cls):
            _element_type_spec = type_key

        item_name = getattr(item, "__name__", str(item))
        _BoundList.__name__ = f"List[{item_name}]"
        _BoundList.__qualname__ = f"List[{item_name}]"
        _BOUND_LIST_CACHE[cache_key] = _BoundList
        return _BoundList

    def __init__(
        self,
        initial: Any = None,
        name: Optional[str] = None,
        element_type: Any = None,
    ) -> None:
        if element_type is not None:
            self._type_key: str = _resolve_type_key(element_type)
        elif self._element_type_spec is not None:
            self._type_key = self._element_type_spec
        else:
            raise TypeError(
                "List requires an explicit element type. "
                "Use subscript syntax (e.g. List[Int]()) or a type alias (e.g. IntList())."
            )

        var_name = name if name is not None else _get_default_list_name()

        if isinstance(initial, set):
            raise TypeError("Unordered collections (set) cannot be used to initialize an ordered List. Use list or tuple instead.")

        if initial is None:
            var_node = nodes.list_variable(name=var_name, value=[])
            self._root_port = var_node.port_output_listvariable_Variable
        elif isinstance(initial, List):
            self._root_port = initial.list_port
        elif isinstance(initial, (list, tuple)):
            raw_items = _validate_initial_items(list(initial), self._type_key)
            var_node = nodes.list_variable(name=var_name, value=raw_items)
            self._root_port = var_node.port_output_listvariable_Variable
        elif hasattr(initial, "list_port"):
            self._root_port = initial.list_port
        else:
            self._root_port = to_port(initial)

    @property
    def list_port(self) -> Any:
        return self._root_port

    def _get_primary_port(self) -> Any:
        return self._root_port

    @property
    def Count(self) -> Any:
        """Returns the length port (Int) of this list."""
        return nodes.get_list_length(list_var=self._root_port).port_output_int_Length

    count = Count

    def _coerce_item_port(self, val: Any) -> Any:
        key = self._type_key
        if key == "int":
            return to_int_port(val)
        if key == "float":
            return to_float_port(val)
        if key == "bool":
            return to_bool_port(val)
        if key == "string":
            return to_string_port(val)
        if key == "plant_type":
            if isinstance(val, (int, float)) and not isinstance(val, Enum):
                raise TypeError("PlantType must be handled through the PlantType enum; direct int input is not allowed.")
            if isinstance(val, Enum):
                if type(val).__name__ != "PlantType":
                    raise TypeError(f"Expected PlantType enum member, got {type(val).__name__}: {val!r}")
                return nodes.plant_type_value(plant_type=val).port_output_planttype_PlantType
            return to_port(val)
        if key == "zombie_type":
            if isinstance(val, (int, float)) and not isinstance(val, Enum):
                raise TypeError("ZombieType must be handled through the ZombieType enum; direct int input is not allowed.")
            if isinstance(val, Enum):
                if type(val).__name__ != "ZombieType":
                    raise TypeError(f"Expected ZombieType enum member, got {type(val).__name__}: {val!r}")
                return nodes.zombie_type_value(zombie_type=val).port_output_zombietype_ZombieType
            return to_port(val)
        return to_port(val)

    def _value_port(self, node: Any) -> Any:
        attr = _OPS[self._type_key]["value_port"]
        return getattr(node, attr)

    # -------------------------------------------------------------------------
    # Add / Append
    # -------------------------------------------------------------------------
    def Add(self, item: Any) -> ListOperation:
        """Appends an item to the end of the list."""
        node = _OPS[self._type_key]["append"](
            list_var=self._root_port,
            value=self._coerce_item_port(item),
        )
        return ListOperation(node)

    add = Add
    append = Add

    # -------------------------------------------------------------------------
    # Insert
    # -------------------------------------------------------------------------
    def Insert(self, index: Any, item: Any) -> ListOperation:
        """Inserts an item into the list at the specified index."""
        node = _OPS[self._type_key]["insert"](
            list_var=self._root_port,
            index=to_int_port(index),
            value=self._coerce_item_port(item),
        )
        return ListOperation(node)

    insert = Insert

    # -------------------------------------------------------------------------
    # Replace / Indexer Assignment
    # -------------------------------------------------------------------------
    def Replace(self, index: Any, item: Any) -> ListOperation:
        """Replaces the element at the specified index with a new item."""
        node = _OPS[self._type_key]["replace"](
            list_var=self._root_port,
            index=to_int_port(index),
            value=self._coerce_item_port(item),
        )
        return ListOperation(node)

    replace = Replace

    def __setitem__(self, index: Any, item: Any) -> None:
        self.Replace(index, item)

    # -------------------------------------------------------------------------
    # GetItem / Indexer Lookup & TryGetValue
    # -------------------------------------------------------------------------
    def _get_item_node(self, index: Any) -> Any:
        return _OPS[self._type_key]["get"](
            list_var=self._root_port,
            index=to_int_port(index),
        )

    def __getitem__(self, index: Any) -> Any:
        node = self._get_item_node(index)
        return self._value_port(node)

    get_item = __getitem__
    Get = __getitem__

    def TryGetValue(self, index: Any) -> Tuple[Any, Any]:
        """Returns a tuple (value_port, ok_port) checking whether index access is valid."""
        node = self._get_item_node(index)
        val_port = self._value_port(node)
        ok_port = node.port_output_bool_Valid
        return val_port, ok_port

    try_get_value = TryGetValue

    # -------------------------------------------------------------------------
    # IndexOf / Contains / TryFindIndex
    # -------------------------------------------------------------------------
    def _find_value_node(self, item: Any) -> Any:
        return _OPS[self._type_key]["find"](
            list_var=self._root_port,
            value=self._coerce_item_port(item),
        )

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
        node = nodes.remove_list_item(list_var=self._root_port, index=to_int_port(index))
        return ListOperation(node)

    remove_at = RemoveAt

    def Clear(self) -> ListOperation:
        """Clears all elements from the list."""
        node = nodes.clear_list_values(list_var=self._root_port)
        return ListOperation(node)

    clear = Clear

    # -------------------------------------------------------------------------
    # CopyTo / Clone
    # -------------------------------------------------------------------------
    def CopyTo(self, target: Any) -> ListOperation:
        """Copies all elements from this list into the target list."""
        target_port = target.list_port if hasattr(target, "list_port") else to_port(target)
        node = nodes.copy_list_values(source_list=self._root_port, target_list=target_port)
        return ListOperation(node)

    copy_to = CopyTo

    def Clone(self, name: Optional[str] = None) -> List[T]:
        """Creates a new list variable of the same type and copies values into it."""
        clone_name = name if name is not None else _get_default_list_name()
        new_list: List[T] = List(name=clone_name, element_type=self._type_key)
        self.CopyTo(new_list)
        return new_list

    clone = Clone

    # -------------------------------------------------------------------------
    # Operator Overloads & Safety Guards
    # -------------------------------------------------------------------------
    def __iadd__(self, other: Any) -> List[T]:
        if isinstance(other, (list, tuple)):
            for item in other:
                self.Add(item)
        elif isinstance(other, List):
            with ForEach(other) as loop_item:
                self.Add(loop_item)
        else:
            self.Add(other)
        return self

    def __len__(self) -> int:
        raise TypeError(
            "len() is not supported on graph List variables at transpile time. "
            "Use '.Count' to obtain an Int graph port representing list length."
        )

    def __contains__(self, item: Any) -> bool:
        raise TypeError(
            "'in' operator is not supported on graph List variables at transpile time. "
            "Use '.Contains(item)' to obtain a Bool graph condition port."
        )

    def __bool__(self) -> bool:
        raise TypeError(
            "Boolean evaluation of a graph List variable is ambiguous at transpile time. "
            "Use 'If(list.Count > 0)' to check if list is non-empty."
        )

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
PlantTypeListVar = List[PlantType]
ZombieTypeListVar = List[ZombieType]


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
    "ZombieTypeListVar",
]
