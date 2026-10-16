from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional
from ._Nodes.Extentions.UI.format_string import format_string
from ._Nodes.Extentions.Branching import If
from ._Nodes.Extentions.Variables import IntVar, FloatVar, BoolVar
from ._Nodes.Extentions.Entity import Plant
from ._Nodes.Extentions.Triggers import Trigger
from .Data.TypeMgr import KeyCode


class _wasd_key:
    def __init__(self) -> None:
        self.up = KeyCode.W
        self.down = KeyCode.S
        self.left = KeyCode.A
        self.right = KeyCode.D


class WASDPlant:
    """Assigns WASD keys to control a plant's movement across the grid."""

    def __init__(self, plant: Plant | Any) -> None:
        if isinstance(plant, Plant):
            self.plant = plant
        else:
            self.plant = Plant(plant)
        self.wasd_keys = _wasd_key()

    def Start(self) -> None:
        with Trigger.OnKeyDown(self.wasd_keys.up):
            self.plant.move_relative(col_diff=0, row_diff=-1)
        with Trigger.OnKeyDown(self.wasd_keys.down):
            self.plant.move_relative(col_diff=0, row_diff=1)
        with Trigger.OnKeyDown(self.wasd_keys.left):
            self.plant.move_relative(col_diff=-1, row_diff=0)
        with Trigger.OnKeyDown(self.wasd_keys.right):
            self.plant.move_relative(col_diff=1, row_diff=0)


class Dictionary:
    """A Virtual Dictionary (Global State Manager) utilizing Native Variables."""

    def __init__(self, schema: Optional[Dict[str, Any]] = None) -> None:
        self._store: Dict[str, Any] = {}
        if schema:
            for key, initial_val in schema.items():
                self.add_key(key, initial_val)

    def add_key(self, key: str, initial_val: Any) -> None:
        if key in self._store:
            raise KeyError(f"Key '{key}' already exists!")

        if isinstance(initial_val, bool):
            self._store[key] = BoolVar(start_val=initial_val)
        elif isinstance(initial_val, float):
            self._store[key] = FloatVar(start_val=initial_val)
        elif isinstance(initial_val, int):
            self._store[key] = IntVar(start_val=initial_val)
        else:
            raise TypeError("Unsupported Dictionary type. Use int, float, or bool.")

    def __getitem__(self, key: str) -> Any:
        return self._store[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._store[key].set(value)

    def __getattr__(self, key: str) -> Any:
        if key in ("_store",):
            return super().__getattribute__(key)
        if "_store" in self.__dict__ and key in self._store:
            return self._store[key]
        return super().__getattribute__(key)

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "_store":
            super().__setattr__(key, value)
        elif "_store" in self.__dict__ and key in self._store:
            self._store[key].set(value)
        else:
            super().__setattr__(key, value)


class Array:
    """A Pre-Allocated Virtual Array utilizing Native Variables."""

    def __init__(self, size: int, default_val: Any = 0) -> None:
        self.size = size
        self._store: List[Any] = []

        for _ in range(size):
            if isinstance(default_val, bool):
                self._store.append(BoolVar(start_val=default_val))
            elif isinstance(default_val, float):
                self._store.append(FloatVar(start_val=default_val))
            elif isinstance(default_val, int):
                self._store.append(IntVar(start_val=default_val))
            else:
                raise TypeError("Unsupported Array element type. Use int, float, or bool.")

    def __getitem__(self, index: int) -> Any:
        return self._store[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._store[index].set(value)

    def __len__(self) -> int:
        return self.size

    def read(self, index_port: Any, on_read_callback: Callable[[Any], None]) -> None:
        for i in range(self.size):
            with If(index_port == i):
                on_read_callback(self._store[i])

    def write(self, index_port: Any, value: Any) -> None:
        for i in range(self.size):
            with If(index_port == i):
                self._store[i].set(value)


__all__ = ["format_string", "WASDPlant", "Dictionary", "Array"]
