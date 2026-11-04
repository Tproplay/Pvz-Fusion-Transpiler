from __future__ import annotations

from typing import Any
from ...._Data import EventBulletProperty
from .... import nodes
from ....port_types import to_float_port


class Bullet:
    """Smart wrapper around a runtime Bullet entity pointer.

    Provides bullet modification actions and property access.
    """

    def __init__(self, bullet_ref: Any) -> None:
        if isinstance(bullet_ref, Bullet):
            self.ref: Any = bullet_ref.ref
        else:
            self.ref = bullet_ref

    def modify(self, value: Any, prop: Any = EventBulletProperty.ScaleMultiplier) -> Any:
        float_val = to_float_port(value)
        return nodes.modify_event_bullet(bullet=self.ref, value=float_val, prop=prop)

    Modify = modify

    def set_scale(self, scale: Any) -> Any:
        return self.modify(scale, prop=EventBulletProperty.ScaleMultiplier)

    SetScale = set_scale

    def set_speed(self, speed: Any) -> Any:
        return self.modify(speed, prop=EventBulletProperty.Speed)

    SetSpeed = set_speed

    def set_damage(self, damage: Any) -> Any:
        return self.modify(damage, prop=EventBulletProperty.Damage)

    SetDamage = set_damage

    def set_direction(self, angle: Any) -> Any:
        return self.modify(angle, prop=EventBulletProperty.DirectionAngle)

    SetDirection = set_direction

    def _get_primary_port(self) -> Any:
        return self.ref


__all__ = ["Bullet"]
