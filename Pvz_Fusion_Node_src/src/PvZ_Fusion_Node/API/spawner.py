"""
PvZ Fusion Spawner Subsystem.
Provides methods to place plants and spawn zombies at specific grid locations with event outcome hooks.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Union

from .. import nodes
from ..Core.context import ExecutionPath
from ..Nodes.Extentions.extensions import Plant, Zombie
from ..Extras.TypeMgr import PlantType, ZombieType


from ..Nodes.Original.PlantFunction.set_plant_node import SetPlantNode
from ..Nodes.Original.ZombieFunction.create_zombie_node import CreateZombieNode


class SpawnedPlant(Plant):
    """A `Plant` returned by `Spawner.Set_Plant`, carrying spawn-outcome execution paths."""
    node: Any
    on_created: ExecutionPath
    on_failed: ExecutionPath


class SpawnedZombie(Zombie):
    """A `Zombie` returned by `Spawner.Set_Zombie`, carrying a spawn-outcome execution path."""
    node: Any
    on_created: ExecutionPath


class Spawner:
    """Static entity factory for planting plants and spawning zombies on the lawn."""

    @staticmethod
    def Set_Plant(
        row: Union[int, Any],
        col: Union[int, Any],
        plant_type: Union[int, PlantType, Any],
        force: bool = False,
    ) -> SpawnedPlant:
        """Spawns a plant at the specified grid coordinates.

        Args:
            row: Lawn row index (0-based).
            col: Lawn column index (0-based).
            plant_type: PlantType enum member or numeric ID.
            force: Force planting even if the cell is occupied.

        Returns:
            SpawnedPlant: The spawned plant with `.on_created` and `.on_failed` execution paths.
        """
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value

        node = nodes.set_plant(
            row=row,
            column=col,
            plant_type=nodes.plant_type_value(val=plant_type),
            force_plant=force,
        )

        plant = SpawnedPlant(node.plant)
        plant.node = node
        plant.on_created = ExecutionPath(node.id, SetPlantNode.OnCreated_output_trigger)
        plant.on_failed = ExecutionPath(node.id, SetPlantNode.OnFailed_output_trigger)
        return plant

    @staticmethod
    def Set_Zombie(
        row: Union[int, Any],
        col: Union[int, Any],
        zombie_type: Union[int, ZombieType, Any],
        mind_controlled: bool = False,
    ) -> SpawnedZombie:
        """Spawns a zombie at the specified grid coordinates.

        Args:
            row: Lawn row index.
            col: Lawn column index.
            zombie_type: ZombieType enum member or numeric ID.
            mind_controlled: Whether the zombie is hypno-induced / friendly.

        Returns:
            SpawnedZombie: The spawned zombie with `.on_created` execution path.
        """
        if isinstance(zombie_type, Enum):
            zombie_type = zombie_type.value

        node = nodes.create_zombie(
            row=row,
            column=col,
            zombie_type=nodes.zombie_type_value(val=zombie_type),
            mind_controlled=mind_controlled,
        )

        zombie = SpawnedZombie(node.zombie)
        zombie.node = node
        zombie.on_created = ExecutionPath(node.id, CreateZombieNode.OnCreated_output_trigger)
        return zombie

    @staticmethod
    def set_bullet(
        bullet_type: Any,
        position: Any = None,
        x: float = 0.0,
        y: float = 0.0,
        z: float = 0.0,
    ) -> Any:
        """Shoots / spawns a bullet of specified type at given position."""
        from ..Nodes.Extentions.Bullet.bullet_ext import Bullet
        return Bullet.shoot(bullet_type=bullet_type, position=position, x=x, y=y, z=z)

    Set_Bullet = set_bullet
