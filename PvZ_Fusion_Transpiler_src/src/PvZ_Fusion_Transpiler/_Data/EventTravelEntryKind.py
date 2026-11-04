from enum import Enum


class EventTravelEntryKind(Enum):
    """EventTravelEntryKind enum in PvZ Fusion."""

    CommonModifier = 0
    UltimateModifier = 1
    ZombieModifier = 2


__all__ = ["EventTravelEntryKind"]
