from __future__ import annotations

from enum import Enum
from typing import Any
from ...._Data import EventZombieStat, EventZombieStatus
from .... import nodes
from ....port_types import to_float_port, to_int_port


class Zombie:
    """Smart wrapper around a runtime Zombie entity pointer.

    Provides combat actions, mind control overrides, position shifts, animation triggers,
    stat/status queries and modifications, and destructuring properties.
    """

    def __init__(self, zombie_ref: Any) -> None:
        if isinstance(zombie_ref, Zombie):
            self.ref: Any = zombie_ref.ref
        else:
            self.ref = zombie_ref
        self._split_cache: Any = None

    def damage(self, amount: Any) -> Any:
        return nodes.damage_zombie(zombie=self.ref, damage=amount)

    Damage = damage

    def set_health_multiplier(self, ratio: Any) -> Any:
        float_ratio = to_float_port(ratio)
        return nodes.modify_zombie_health(zombie=self.ref, ratio=float_ratio)

    SetHealthMultiplier = set_health_multiplier

    def hypnotize(self) -> Any:
        return nodes.set_zombie_mind_controlled(zombie=self.ref)

    Hypnotize = hypnotize

    def move(self, row: Any, col: Any) -> Any:
        int_row = to_int_port(row)
        int_col = to_int_port(col)
        return nodes.move_zombie(zombie=self.ref, row=int_row, column=int_col)

    Move = move

    def move_relative(self, row_diff: Any = 0, col_diff: Any = 0) -> Any:
        return self.move(row=self.row + row_diff, col=self.col + col_diff)

    MoveRelative = move_relative

    def play_animation(self, anim_name: str | Enum | Any = "idle") -> Any:
        if isinstance(anim_name, Enum):
            anim_name = anim_name.value
        return nodes.play_zombie_anim(zombie=self.ref, animation_name=anim_name)

    PlayAnimation = play_animation

    @property
    def split(self) -> Any:
        if self._split_cache is None:
            self._split_cache = nodes.zombie_split(zombie=self.ref)
        return self._split_cache

    @property
    def zombieType(self) -> Any:
        return self.split.port_output_zombietype_ZombieType

    ZombieType = zombieType

    @property
    def row(self) -> Any:
        return self.split.port_output_int_Row

    Row = row

    @property
    def col(self) -> Any:
        return self.split.port_output_int_Col

    Col = col

    def get_stats(self, stat: Any = EventZombieStat.AttackPower) -> Any:
        return nodes.get_zombie_stats(zombie=self.ref, stat=stat).port_output_float_Value

    GetStats = get_stats

    def set_stats(self, value: Any, stat: Any = EventZombieStat.AttackPower) -> Any:
        return nodes.set_zombie_stats(zombie=self.ref, value=value, stat=stat)

    SetStats = set_stats

    def get_status(self, status: Any = EventZombieStatus.ChillSeconds) -> Any:
        return nodes.get_zombie_status(zombie=self.ref, status=status).port_output_float_Value

    GetStatus = get_status

    def set_status(self, value: Any, status: Any = EventZombieStatus.ChillSeconds) -> Any:
        return nodes.set_zombie_status(zombie=self.ref, value=value, status=status)

    SetStatus = set_status

    # Convenience stat properties & methods
    @property
    def hp(self) -> Any:
        return self.get_stats(EventZombieStat.BodyHP)

    Hp = hp

    @property
    def max_hp(self) -> Any:
        return self.get_stats(EventZombieStat.MaxBodyHP)

    MaxHp = max_hp

    @property
    def speed(self) -> Any:
        return self.get_stats(EventZombieStat.BaseSpeed)

    Speed = speed

    @property
    def size(self) -> Any:
        return self.get_stats(EventZombieStat.Size)

    Size = size

    @property
    def attack_power(self) -> Any:
        return self.get_stats(EventZombieStat.AttackPower)

    AttackPower = attack_power

    @property
    def armor1_hp(self) -> Any:
        return self.get_stats(EventZombieStat.Armor1HP)

    Armor1Hp = armor1_hp

    @property
    def armor2_hp(self) -> Any:
        return self.get_stats(EventZombieStat.Armor2HP)

    Armor2Hp = armor2_hp

    def set_hp(self, val: Any) -> Any:
        return self.set_stats(val, EventZombieStat.BodyHP)

    SetHp = set_hp

    def set_speed(self, val: Any) -> Any:
        return self.set_stats(val, EventZombieStat.BaseSpeed)

    SetSpeed = set_speed

    def set_size(self, val: Any) -> Any:
        return self.set_stats(val, EventZombieStat.Size)

    SetSize = set_size

    def set_attack_power(self, val: Any) -> Any:
        return self.set_stats(val, EventZombieStat.AttackPower)

    SetAttackPower = set_attack_power

    def is_type(self, zombie_type: Any) -> Any:
        return nodes.compare_zombie_type(a=self.zombieType, b=zombie_type).port_output_bool_Same

    IsType = is_type

    def to_object(self) -> Any:
        return nodes.zombie_to_object(zombie=self.ref).port_output_gameobject_GameObject

    ToObject = to_object

    def ToString(self) -> Any:
        conv = nodes.zombie_type_to_string(zombie_type=self.zombieType)
        return conv.port_output_string_String

    to_string = ToString


__all__ = ["Zombie"]
