"""
PvZ Fusion Lawn Effects, Environment, and Query Utilities.
Provides props, explosions, sound, buffs, victory conditions, and entity iteration on the board.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Union

from .. import nodes
from ..Core.context import ctx, ExecutionPath
from ..Nodes.Extentions.extensions import Plant, Zombie
from ..Extras.TypeMgr import PlantType, SoundType, TravelBuffType
from ..typing import to_int_port


class Lawnf:
    """Static helpers for lawn props, area effects, sound, game state, and plant/zombie queries."""

    # ==========================================================
    # PROPS
    # ==========================================================
    @staticmethod
    def spawn_particle(row: Union[int, Any], col: Union[int, Any]) -> None:
        """Spawns an imitator particle effect at the given cell."""
        nodes.create_particle(row=row, column=col)

    @staticmethod
    def spawn_grave(row: Union[int, Any], col: Union[int, Any]) -> None:
        """Spawns a gravestone prop on the given tile."""
        nodes.create_grave(row=row, column=col)

    @staticmethod
    def spawn_crater(row: Union[int, Any], col: Union[int, Any]) -> None:
        """Spawns a crater prop on the given tile."""
        nodes.create_crater(row=row, column=col)

    @staticmethod
    def spawn_ladder(row: Union[int, Any], col: Union[int, Any]) -> None:
        """Spawns a pool ladder prop on the given tile."""
        nodes.create_ladder(row=row, column=col)

    @staticmethod
    def spawn_ice_block(
        row: Union[int, Any],
        col: Union[int, Any],
        plant_type: Union[PlantType, int] = -1,
    ) -> None:
        """Spawns an ice block prop on the given tile, optionally encasing a plant."""
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        p_type = nodes.plant_type_value(val=plant_type)
        nodes.create_ice_block(row=row, column=col, plant_type=p_type)

    # ==========================================================
    # EXPLOSIONS & AREA EFFECTS
    # ==========================================================
    @staticmethod
    def trigger_cherry_explosion(
        row: Union[int, Any],
        col: Union[int, Any],
        damage: Union[int, Any] = 1800,
    ) -> None:
        """Triggers a Cherry Bomb-style explosion effect and damage at the given tile."""
        nodes.create_cherry_explode(row=row, column=col, damage=to_int_port(damage))

    @staticmethod
    def trigger_doom_explosion(
        row: Union[int, Any],
        col: Union[int, Any],
        damage: Union[int, Any] = 1800,
        create_pit: bool = True,
    ) -> None:
        """Triggers a Doom-shroom-style explosion effect and damage at the given tile."""
        nodes.create_doom_shroom_effect(
            row=row, column=col, damage=to_int_port(damage), set_pit=create_pit
        )

    @staticmethod
    def trigger_zombie_explosion(row: Union[int, Any], col: Union[int, Any]) -> None:
        """Triggers a zombie-explosion visual effect at the given tile (no damage)."""
        nodes.create_zombie_explode(row=row, column=col)

    @staticmethod
    def trigger_jalapeno(row: Union[int, Any], damage: Union[int, Any] = 1800) -> None:
        """Triggers a Jalapeno-style row-wide fire effect and damage."""
        nodes.create_jalapeno_effect(row=row, damage=to_int_port(damage))

    @staticmethod
    def trigger_ice_shroom(duration: Union[float, Any]) -> None:
        """Triggers an Ice-shroom-style effect, freezing all zombies on the board."""
        nodes.create_ice_shroom_effect(duration=duration)

    # ==========================================================
    # SOUND
    # ==========================================================
    @staticmethod
    def play_sound(sound_id: Union[SoundType, int]) -> None:
        """Plays a one-shot sound effect."""
        if isinstance(sound_id, Enum):
            sound_id = sound_id.value
        nodes.play_sound(sound_id=sound_id)

    # ==========================================================
    # GAME STATE
    # ==========================================================
    @staticmethod
    def trigger_game_over(reason: Any = "Defeated!") -> None:
        """Ends the level in defeat, displaying the given reason text."""
        from ..Libraries.StdLib import format_string
        nodes.game_over(reason=format_string(reason))

    @staticmethod
    def trigger_game_win() -> None:
        """Ends the level in victory."""
        nodes.game_win()

    # ==========================================================
    # BUFFS
    # ==========================================================
    @staticmethod
    def get_buff(buff_enum: Union[TravelBuffType, int]) -> None:
        """Grants a travel buff for the current level."""
        if isinstance(buff_enum, Enum):
            buff_enum = buff_enum.value
        nodes.get_travel_buff(buff_enum=buff_enum)

    # ==========================================================
    # QUERIES & LOOPS
    # ==========================================================
    @staticmethod
    def get_closest_zombie(row: Union[int, Any], col: Union[int, Any]) -> Zombie:
        """Finds the zombie nearest to the given tile."""
        n = nodes.get_nearest_zombie(row=row, column=col)
        return Zombie(n.zombie)

    @staticmethod
    def get_plants_at(row: Union[int, Any], col: Union[int, Any]) -> Any:
        """Returns the plant-list output port for a specific cell."""
        return nodes.get_plants_in_cell(row=row, column=col).plants

    @staticmethod
    def get_all_plants() -> Any:
        """Returns the plant-list output port for every plant on the board."""
        return nodes.get_all_plants().plants

    class for_each_plant_on_lawn:
        """Context manager that loops over every plant currently on the board.

        Example:
            ```python
            with pvn.Lawnf.for_each_plant_on_lawn() as plant:
                plant.heal(50)
            ```
        """

        def __init__(self) -> None:
            self.list_port = nodes.get_all_plants().plants
            self.loop_node = nodes.for_each_plant(plant_list=self.list_port)

        def __enter__(self) -> Plant:
            ctx.trigger_stack.append(ExecutionPath(self.loop_node.id, "循环体"))
            return Plant(self.loop_node.currentPlant)

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            ctx.trigger_stack.pop()
