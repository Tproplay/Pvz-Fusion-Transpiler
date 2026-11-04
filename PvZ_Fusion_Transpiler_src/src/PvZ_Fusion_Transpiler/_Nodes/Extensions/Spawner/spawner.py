from __future__ import annotations

from enum import Enum
from typing import Any
from ..Abstract.execution_path import ExecutionPath
from ..Entity.plant import Plant
from ..Entity.zombie import Zombie
from ..Entity.bullet import Bullet
from .... import nodes


class SpawnedPlant(Plant):
    """A wrapped Plant entity created via Spawner.Set_Plant, providing lifecycle execution paths."""

    def __init__(self, node: Any) -> None:
        super().__init__(node.port_output_plant_Plant)
        self.node = node

    @property
    def on_created(self) -> ExecutionPath:
        return ExecutionPath(self.node, self.node.port_output_trigger_OnCreated.name)

    on_success = on_created

    @property
    def on_failed(self) -> ExecutionPath:
        return ExecutionPath(self.node, self.node.port_output_trigger_OnFailed.name)

    def __enter__(self) -> SpawnedPlant:
        self.on_created.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.on_created.__exit__(exc_type, exc_val, exc_tb)


class SpawnedZombie(Zombie):
    """A wrapped Zombie entity created via Spawner.Set_Zombie, providing lifecycle execution paths."""

    def __init__(self, node: Any) -> None:
        super().__init__(node.port_output_zombie_Zombie)
        self.node = node

    @property
    def on_created(self) -> ExecutionPath:
        return ExecutionPath(self.node, self.node.port_output_trigger_OnCreated.name)

    on_success = on_created

    def __enter__(self) -> SpawnedZombie:
        self.on_created.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.on_created.__exit__(exc_type, exc_val, exc_tb)


class SpawnedBullet(Bullet):
    """A wrapped Bullet entity created via Spawner.Set_Bullet, providing lifecycle execution paths."""

    def __init__(self, node: Any) -> None:
        super().__init__(node.port_output_bullet_Bullet)
        self.node = node

    @property
    def on_created(self) -> ExecutionPath:
        return ExecutionPath(self.node, self.node.port_output_trigger_Complete.name)

    on_success = on_created

    @property
    def on_failed(self) -> ExecutionPath:
        return ExecutionPath(self.node, self.node.port_output_trigger_Failed.name)

    def __enter__(self) -> SpawnedBullet:
        self.on_created.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.on_created.__exit__(exc_type, exc_val, exc_tb)


class Spawner:
    """Namespace for dynamically spawning plant, zombie, and bullet entities into the board."""

    class Set_Plant(SpawnedPlant):
        """Spawns a plant at the specified grid coordinates and returns a wrapped Plant instance."""

        def __init__(self, row: Any, col: Any, plant_type: Any, force: bool = False, column: Any = None) -> None:
            if isinstance(plant_type, (int, float)) and not isinstance(plant_type, Enum):
                raise TypeError("PlantType must be handled through the PlantType enum, direct int input is not allowed.")
            if isinstance(plant_type, Enum):
                p_val: Any = nodes.plant_type_value(val=plant_type).port_output_planttype_PlantType
            else:
                p_val = plant_type

            actual_col = column if column is not None else col
            node = nodes.set_plant(
                row=row,
                column=actual_col,
                plant_type=p_val,
                force_plant=force,
            )
            super().__init__(node)

    SetPlant = Set_Plant

    class Set_Zombie(SpawnedZombie):
        """Spawns a zombie at the specified grid coordinates and returns a wrapped Zombie instance."""

        def __init__(self, row: Any, col: Any, zombie_type: Any, mind_controlled: bool = False, column: Any = None) -> None:
            if isinstance(zombie_type, (int, float)) and not isinstance(zombie_type, Enum):
                raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
            if isinstance(zombie_type, Enum):
                z_val: Any = nodes.zombie_type_value(val=zombie_type).port_output_zombietype_ZombieType
            else:
                z_val = zombie_type

            actual_col = column if column is not None else col
            node = nodes.create_zombie(
                row=row,
                column=actual_col,
                zombie_type=z_val,
                mind_controlled=mind_controlled,
            )
            super().__init__(node)

    SetZombie = Set_Zombie

    class Set_Bullet(SpawnedBullet):
        """Spawns/shoots a bullet with specified parameters and returns a wrapped Bullet instance."""

        def __init__(
            self,
            row: Any = 0,
            col: Any = 0.0,
            bullet_type: Any = None,
            damage: Any = None,
            speed: Any = None,
            angle: Any = None,
            scale_multiplier: Any = None,
            at_mouse: Any = False,
            zombie_camp: Any = False,
            column: Any = None,
        ) -> None:
            if isinstance(bullet_type, (int, float)) and not isinstance(bullet_type, Enum):
                raise TypeError("BulletType must be handled through the BulletType enum, direct int input is not allowed.")
            if isinstance(bullet_type, Enum):
                b_val: Any = nodes.bullet_type_value(val=bullet_type).port_output_bullettype_BulletType
            else:
                b_val = bullet_type

            actual_col = column if column is not None else col
            node = nodes.shoot_event_bullet(
                row=row,
                col=actual_col,
                bullet_type=b_val,
                damage=damage,
                speed=speed,
                angle=angle,
                scale_multiplier=scale_multiplier,
                at_mouse=at_mouse,
                zombie_camp=zombie_camp,
            )
            super().__init__(node)

    SetBullet = Set_Bullet


__all__ = ["Spawner", "SpawnedPlant", "SpawnedZombie", "SpawnedBullet"]
