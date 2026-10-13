"""
Virtual data structures and collections using native variable nodes and logic graphs.
"""

from __future__ import annotations
from typing import Any
from enum import Enum

from ...node_base import PortReference
from ...Core.context import ctx, ExecutionPath
from ...Nodes.Extentions.extensions import IntVar, FloatVar, BoolVar, If
from ... import nodes


class ZombieTypeList:
    """A static wrapper representing a list of Zombie Types.

    Since native zombie list storage nodes are unavailable, this manages a Python-side 
    set and dynamically generates an OR-chained comparison graph at transpilation time.

    Example:
    ```python
    bosses = pvn.StdLib.ZombieTypeList([ZombieType.Gargantuar, ZombieType.BungeeZombie])
    
    with pvn.Trigger.OnZombieSpawn() as zombie:
        with pvn.If(bosses.contains(zombie.zombieType)):
            pvn.Print("A boss has appeared!")
    ```
    """

    def __init__(self, initial: Any | None = None):
        self._items: set[int] = set()
        if initial is not None:
            self.add(initial)

    def _extract_id(self, item: Any) -> int:
        """Helper to extract the raw integer ID from an Enum, int, or wrapped value."""
        if hasattr(item, "value"):
            return int(item.value)
        return int(item)

    def add(self, item: Any) -> ZombieTypeList:
        """Adds a zombie type or collection of types to the static list."""
        if isinstance(item, (list, tuple, set)) and not isinstance(item, PortReference):
            for i in item:
                self.add(i)
        elif isinstance(item, ZombieTypeList):
            self._items.update(item._items)
        else:
            self._items.add(self._extract_id(item))
        return self

    def remove(self, item: Any) -> ZombieTypeList:
        """Removes a zombie type or collection of types from the static list."""
        if isinstance(item, (list, tuple, set)) and not isinstance(item, PortReference):
            for i in item:
                self.remove(i)
        elif isinstance(item, ZombieTypeList):
            self._items.difference_update(item._items)
        else:
            self._items.discard(self._extract_id(item))
        return self

    def __iadd__(self, other: Any) -> ZombieTypeList:
        return self.add(other)

    def __add__(self, other: Any) -> ZombieTypeList:
        copy_list = ZombieTypeList(self._items)
        return copy_list.add(other)

    def __isub__(self, other: Any) -> ZombieTypeList:
        return self.remove(other)

    def __sub__(self, other: Any) -> ZombieTypeList:
        copy_list = ZombieTypeList(self._items)
        return copy_list.remove(other)

    @property
    def count(self) -> PortReference:
        """Returns a graph node representing the static length of this list."""
        return nodes.int_value(val=len(self._items)).value  # type: ignore

    def contains(self, target_type: PortReference | Enum | int | Any) -> PortReference:
        """Builds a runtime node graph to check if target_type is in this static list.
        
        Generates a sequence of compare_zombie_type nodes chained with logical OR (`|`).
        """
        if not self._items:
            return nodes.bool_value(val=False).value  # type: ignore

        if not isinstance(target_type, PortReference) and not hasattr(target_type, "node"):
            target_id = self._extract_id(target_type)
            return nodes.bool_value(val=(target_id in self._items)).value  # type: ignore

        result_wire = None
        for z_id in self._items:
            z_node = nodes.zombie_type_value(val=z_id)
            z_port = z_node.value if hasattr(z_node, "value") else z_node
            compare_node = nodes.compare_zombie_type(a=target_type, b=z_port)
            is_equal = compare_node.equal

            if result_wire is None:
                result_wire = is_equal
            else:
                result_wire = result_wire | is_equal

        return result_wire  # type: ignore


class Dictionary:
    """A Virtual Dictionary utilizing persistent Native Variables.

    Allows you to define a string-keyed dictionary schema that transpiles into individual
    Int, Float, and Bool variable nodes on the visual canvas.

    Example:
    ```python
    player_stats = pvn.StdLib.Dictionary({
        "kills": 0,
        "speed": 1.5,
        "is_poisoned": False
    })
    
    with pvn.Trigger.OnZombieDeath():
        player_stats.kills += 1
    ```
    """

    def __init__(self, schema: dict | None = None):  # type: ignore
        self._store = {}
        if schema:
            for key, initial_val in schema.items():
                self.add_key(key, initial_val)

    def add_key(self, key: str, initial_val: Any) -> None:
        """Registers a new variable under the specified key."""
        if key in self._store:
            raise KeyError(f"Key '{key}' already exists!")

        if isinstance(initial_val, bool):
            self._store[key] = BoolVar(start_val=initial_val, name=f"dict_{key}")
        elif isinstance(initial_val, float):
            self._store[key] = FloatVar(start_val=initial_val, name=f"dict_{key}")
        elif isinstance(initial_val, int):
            self._store[key] = IntVar(start_val=initial_val, name=f"dict_{key}")
        else:
            raise TypeError("Unsupported Dictionary type. Use int, float, or bool.")

    def __getitem__(self, key: str) -> Any:
        return self._store[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._store[key].set(value)

    def __getattr__(self, key: str) -> Any:
        return self._store[key]

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "_store":
            super().__setattr__(key, value)
        else:
            self._store[key].set(value)


class Array:
    """A Pre-Allocated Virtual Array utilizing persistent Native Variables.

    Transpiles a contiguous block of identically typed variable nodes that can be read 
    or written to via index ports at runtime.

    Example:
    ```python
    lane_health = pvn.StdLib.Array(size=5, default_val=100)
    
    with pvn.Trigger.OnZombieSpawn() as zombie:
        lane_health.write(zombie.row, 50)
    ```
    """

    def __init__(self, size: int, default_val: Any = 0):
        self.size = size
        self._store = []

        for i in range(size):
            if isinstance(default_val, bool):
                self._store.append(BoolVar(start_val=default_val, name=f"arr_{i}"))
            elif isinstance(default_val, float):
                self._store.append(FloatVar(start_val=default_val, name=f"arr_{i}"))
            elif isinstance(default_val, int):
                self._store.append(IntVar(start_val=default_val, name=f"arr_{i}"))

    def __getitem__(self, index: int) -> Any:
        return self._store[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._store[index].set(value)

    def __len__(self) -> int:
        return self.size

    def read(self, index_port: Any, on_read_callback: Any) -> None:
        """Reads a value from the array dynamically using a node port index.

        Args:
            index_port (Any): The numeric port specifying which array index to read.
            on_read_callback (Callable): Function that receives the retrieved variable.
        """
        for i in range(self.size):
            with If(index_port == i):
                on_read_callback(self._store[i])

    def write(self, index_port: Any, value: Any) -> None:
        """Writes a value to the array dynamically using a node port index.

        Args:
            index_port (Any): The numeric port specifying which array index to write to.
            value (Any): The value to store.
        """
        for i in range(self.size):
            with If(index_port == i):
                self._store[i].set(value)


class Counter:
    """A high-level wrapper for the Engine's native CounterNode.

    Tracks an integer count and fires its `on_count` completion path when a target is reached,
    acting as an objective tracker or multi-hit trigger.

    Example:
    ```python
    zombie_counter = pvn.StdLib.Counter(start_val=0)

    with pvn.Trigger.OnZombieDeath():
        zombie_counter.up()
        
    with zombie_counter.on_count:
        pvn.Print("Objective complete!")
    ```
    """

    def __init__(self, start_val: int = 0, reset_condition: Any = None):
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        self.ref = nodes.counter_node(start_val=start_val, reset=reset_condition)

        ctx.trigger_stack.extend(saved_stack)

    def up(self) -> Counter:
        """Increments the counter by 1 manually along the current execution timeline track."""
        from ...Nodes.Original.Constants.counter_node import CounterNode
        if ctx.trigger_stack:
            previous_exec = ctx.trigger_stack[-1]
            ctx.add_connection(
                previous_exec.id, previous_exec.out_trigger, self.ref.id, CounterNode.Trigger_input_trigger
            )

            ctx.trigger_stack[-1] = ExecutionPath(self.ref.id, CounterNode.Trigger_input_trigger)
        return self

    @property
    def value(self) -> Any:
        """Returns the data output port reference containing the current count."""
        return self.ref.count

    @property
    def on_count(self) -> Any:
        """Exposes the 'Count Complete' execution track as a context manager timeline path."""
        from ...Nodes.Original.Constants.counter_node import CounterNode
        return self.ref.path(CounterNode.CountComplete_output_trigger)


__all__ = [
    "ZombieTypeList",
    "Dictionary",
    "Array",
    "Counter",
]
