from enum import Enum


class EventBulletProperty(Enum):
    """EventBulletProperty enum in PvZ Fusion."""

    ScaleMultiplier = 0
    Speed = 1
    Damage = 2
    DirectionAngle = 3


__all__ = ["EventBulletProperty"]
