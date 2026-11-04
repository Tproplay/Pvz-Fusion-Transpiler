from enum import Enum


class EventZombieStat(Enum):
    """EventZombieStat enum in PvZ Fusion."""

    AttackPower = 0
    Armor1HP = 1
    Armor2HP = 2
    BaseSpeed = 3
    Size = 4
    BodyHP = 5
    MaxBodyHP = 6


__all__ = ["EventZombieStat"]
