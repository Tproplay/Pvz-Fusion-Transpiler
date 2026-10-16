from __future__ import annotations

from enum import Enum
from typing import Any
from .... import nodes
from ....typing import to_float_port, to_int_port


class Zombie:
    """Smart wrapper around a runtime Zombie entity pointer.

    Provides combat actions, mind control overrides, position shifts, animation triggers,
    and destructuring properties.
    """

    def __init__(self, zombie_ref: Any) -> None:
        if isinstance(zombie_ref, Zombie):
            self.ref: Any = zombie_ref.ref
        else:
            self.ref = zombie_ref
        self._split_cache: Any = None

    def damage(self, amount: Any) -> Any:
        return nodes.damage_zombie(zombie=self.ref, damage=amount)

    def set_health_multiplier(self, ratio: Any) -> Any:
        float_ratio = to_float_port(ratio)
        return nodes.modify_zombie_health(zombie=self.ref, ratio=float_ratio)

    def hypnotize(self) -> Any:
        return nodes.set_zombie_mind_controlled(zombie=self.ref)

    def move(self, row: Any, col: Any) -> Any:
        int_row = to_int_port(row)
        int_col = to_int_port(col)
        return nodes.move_zombie(zombie=self.ref, row=int_row, column=int_col)

    def move_relative(self, row_diff: Any = 0, col_diff: Any = 0) -> Any:
        return self.move(row=self.row + row_diff, col=self.col + col_diff)

    def play_animation(self, anim_name: str | Enum | Any = "idle") -> Any:
        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        return nodes.play_zombie_anim(zombie=self.ref, animation_name=anim_name)

    @property
    def split(self) -> Any:
        if self._split_cache is None:
            self._split_cache = nodes.zombie_split(zombie=self.ref)
        return self._split_cache

    @property
    def zombieType(self) -> Any:
        return self.split.port_output_zombietype_ZombieType

    @property
    def row(self) -> Any:
        return self.split.port_output_int_Row

    @property
    def col(self) -> Any:
        return self.split.port_output_int_Col

    def ToString(self) -> Any:
        conv = nodes.zombie_type_to_string(zombie_type=self.zombieType)
        return conv.port_output_string_String

    to_string = ToString


__all__ = ["Zombie"]
