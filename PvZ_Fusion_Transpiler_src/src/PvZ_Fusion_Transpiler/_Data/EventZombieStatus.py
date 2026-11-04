from enum import Enum


class EventZombieStatus(Enum):
    """EventZombieStatus enum in PvZ Fusion."""

    ChillSeconds = 0
    Enraged = 1
    Embers = 2
    PoisonSeconds = 3
    GarlicStacks = 4
    KelpStacks = 5
    FreezeStacks = 6
    FreezeSeconds = 7
    TeleportSeconds = 8


__all__ = ["EventZombieStatus"]
