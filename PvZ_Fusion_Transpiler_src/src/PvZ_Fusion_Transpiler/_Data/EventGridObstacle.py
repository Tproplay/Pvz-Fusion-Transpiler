from enum import Enum


class EventGridObstacle(Enum):
    """EventGridObstacle enum in PvZ Fusion."""

    Grave = 0
    Crater = 1
    Ladder = 2
    IceBlock = 3


__all__ = ["EventGridObstacle"]
