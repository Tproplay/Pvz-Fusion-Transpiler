from __future__ import annotations

from enum import Enum
from typing import Any
from ..Abstract.execution_path import ExecutionPath
from ..Entity.plant import Plant
from ..Entity.zombie import Zombie
from .... import nodes


class SpawnedPlant(Plant):
    """A wrapped Plant entity created via Spawner.Set_Plant, providing lifecycle execution paths."""

    def __init__(self, node: Any) -> None:
        super().__init__(node.port_output_plant_Plant)
        self.node = node

    @property
    def on_created(self) -> ExecutionPath:
        return ExecutionPath(self.node.port_output_trigger_OnCreated)

    @property
    def on_failed(self) -> ExecutionPath:
        return ExecutionPath(self.node.port_output_trigger_OnFailed)


class SpawnedZombie(Zombie):
    """A wrapped Zombie entity created via Spawner.Set_Zombie, providing lifecycle execution paths."""

    def __init__(self, node: Any) -> None:
        super().__init__(node.port_output_zombie_Zombie)
        self.node = node

    @property
    def on_created(self) -> ExecutionPath:
        return ExecutionPath(self.node.port_output_trigger_OnCreated)


class Spawner:
    """Namespace for dynamically spawning plant and zombie entities into the board."""

    class Set_Plant(SpawnedPlant):
        """Spawns a plant at the specified grid coordinates and returns a wrapped Plant instance."""

        def __init__(self, row: Any, col: Any, plant_type: Any, force: bool = False) -> None:
            if isinstance(plant_type, int) and not isinstance(plant_type, Enum):
                raise TypeError("PlantType must be handled through the PlantType enum, direct int input is not allowed.")
            if isinstance(plant_type, Enum):
                p_val: Any = nodes.plant_type_value(val=int(plant_type.value))
            else:
                p_val = plant_type

            node = nodes.set_plant(
                row=row,
                column=col,
                plant_type=p_val,
                force_plant=force,
            )
            super().__init__(node)

    class Set_Zombie(SpawnedZombie):
        """Spawns a zombie at the specified grid coordinates and returns a wrapped Zombie instance."""

        def __init__(self, row: Any, col: Any, zombie_type: Any, mind_controlled: bool = False) -> None:
            if isinstance(zombie_type, int) and not isinstance(zombie_type, Enum):
                raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
            if isinstance(zombie_type, Enum):
                z_val: Any = nodes.zombie_type_value(val=int(zombie_type.value))
            else:
                z_val = zombie_type

            node = nodes.create_zombie(
                row=row,
                column=col,
                zombie_type=z_val,
                mind_controlled=mind_controlled,
            )
            super().__init__(node)


__all__ = ["Spawner", "SpawnedPlant", "SpawnedZombie"]
