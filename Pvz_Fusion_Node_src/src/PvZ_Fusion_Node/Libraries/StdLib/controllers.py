"""
Pre-built gameplay controllers, player input handlers, and movement helpers.
"""

from __future__ import annotations
from typing import Any

from ...Data.TypeMgr import KeyCode
from ...api import Trigger
from ...Nodes.Extentions.extensions import Plant


class _wasd_key:
    """Internal struct for default WASD KeyCode bindings."""
    def __init__(self) -> None:
        self.up = KeyCode.W
        self.down = KeyCode.S
        self.left = KeyCode.A
        self.right = KeyCode.D


class WASDPlant:
    """Assigns WASD keyboard inputs to control the grid movement of a specific Plant entity.

    Example:
    ```python
    with pvn.Trigger.OnGameStart():
        hero = pvn.Spawner.Set_Plant(row=2, col=2, plant_type=pvn.PlantType.Peashooter)
        pvn.StdLib.WASDPlant(hero).Start()
    ```
    """

    def __init__(self, plant: Plant | Any) -> None:
        if isinstance(plant, Plant):
            self.plant = plant
        else:
            self.plant = Plant(plant)

        self.wasd_keys = _wasd_key()

    def Start(self) -> None:
        """Initializes the keyboard triggers and movement bindings."""
        with Trigger.OnKeyDown(self.wasd_keys.up):
            self.plant.move_relative(0, -1)
        with Trigger.OnKeyDown(self.wasd_keys.down):
            self.plant.move_relative(0, 1)
        with Trigger.OnKeyDown(self.wasd_keys.left):
            self.plant.move_relative(-1, 0)
        with Trigger.OnKeyDown(self.wasd_keys.right):
            self.plant.move_relative(1, 0)


__all__ = [
    "_wasd_key",
    "WASDPlant",
]
