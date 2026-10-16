from __future__ import annotations

from enum import Enum
from typing import Any
from ..Abstract.execution_path import ExecutionPath
from ..Entity.plant import Plant
from ..Entity.zombie import Zombie
from ..UI.format_string import format_string
from .... import nodes


class Lawnf:
    """Contains methods for interacting with the lawn and game events."""

    @staticmethod
    def spawn_particle(row: Any, col: Any) -> Any:
        return nodes.create_particle(row=row, column=col)

    @staticmethod
    def spawn_grave(row: Any, col: Any) -> Any:
        return nodes.create_grave(row=row, column=col)

    @staticmethod
    def spawn_crater(row: Any, col: Any) -> Any:
        return nodes.create_crater(row=row, column=col)

    @staticmethod
    def spawn_ladder(row: Any, col: Any) -> Any:
        return nodes.create_ladder(row=row, column=col)

    @staticmethod
    def spawn_ice_block(row: Any, col: Any, plant_type: Any = None) -> Any:
        if plant_type is not None:
            if isinstance(plant_type, int) and not isinstance(plant_type, Enum):
                raise TypeError("PlantType must be an Enum instance (e.g. PlantType.PEASHOOTER); direct int is not allowed.")
            if isinstance(plant_type, Enum):
                plant_type = nodes.plant_type_value(val=int(plant_type.value))
        return nodes.create_ice_block(row=row, column=col, plant_type=plant_type)

    @staticmethod
    def trigger_cherry_explosion(row: Any, col: Any, damage: Any = 1800) -> Any:
        return nodes.create_cherry_explode(row=row, column=col, damage=damage)

    @staticmethod
    def trigger_doom_explosion(row: Any, col: Any, damage: Any = 1800, create_pit: Any = True) -> Any:
        return nodes.create_doom_shroom_effect(row=row, column=col, damage=damage, set_pit=create_pit)

    @staticmethod
    def trigger_zombie_explode(row: Any, col: Any) -> Any:
        return nodes.create_zombie_explode(row=row, column=col)

    @staticmethod
    def trigger_zombie_explosion(row: Any, col: Any) -> Any:
        return Lawnf.trigger_zombie_explode(row=row, col=col)

    @staticmethod
    def trigger_jalapeno(row: Any, damage: Any = 1800) -> Any:
        return nodes.create_jalapeno_effect(row=row, damage=damage)

    @staticmethod
    def trigger_ice_shroom(duration: Any = 4.0) -> Any:
        return nodes.create_ice_shroom_effect(duration=duration)

    @staticmethod
    def play_sound(sound_id: Any) -> Any:
        if isinstance(sound_id, Enum):
            sound_id = sound_id.value
        return nodes.play_sound(sound_id=sound_id)

    @staticmethod
    def trigger_game_over(reason: Any = "Defeated!") -> Any:
        return nodes.game_over(reason=format_string(reason))

    @staticmethod
    def trigger_game_win() -> Any:
        return nodes.game_win()

    @staticmethod
    def get_buff(buff_enum: Any) -> Any:
        return nodes.get_travel_buff(buff_enum=buff_enum)

    @staticmethod
    def get_closest_zombie(row: Any, col: Any) -> Zombie:
        """Returns a wrapped Zombie Object representing the closest zombie to (row, col)."""
        n = nodes.get_nearest_zombie(row=row, column=col)
        return Zombie(n.port_output_zombie_Zombie)

    @staticmethod
    def get_plants_at(row: Any, col: Any) -> Any:
        """Returns the list port for a specific grid cell, suitable for plant iteration."""
        return nodes.get_plants_in_cell(row=row, column=col).port_output_plantlist_PlantList

    @staticmethod
    def get_all_plants() -> Any:
        """Returns the list port for all plants currently present on the lawn."""
        return nodes.get_all_plants().port_output_plantlist_AllPlants

    class for_each_plant_on_lawn:
        """Context manager that iterates over every plant on the lawn, yielding a wrapped Plant."""

        def __init__(self) -> None:
            self.list_port = Lawnf.get_all_plants()
            self.loop_node = nodes.for_each_plant(plant_list=self.list_port)
            self._path = ExecutionPath(self.loop_node.port_output_trigger_LoopBody)

        def __enter__(self) -> Plant:
            self._path.__enter__()
            return Plant(self.loop_node.port_output_plant_CurrentPlant)

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            self._path.__exit__(exc_type, exc_val, exc_tb)

        @property
        def complete(self) -> ExecutionPath:
            return ExecutionPath(self.loop_node.port_output_trigger_LoopComplete)


__all__ = ["Lawnf"]
