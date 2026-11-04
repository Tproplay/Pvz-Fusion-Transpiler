from enum import Enum


class BuffType(Enum):
    """BuffType enum in PvZ Fusion."""

    UnlockPlant = 0
    AdvancedBuff = 1
    UltimateBuff = 2
    Debuff = 3
    InvestmentBuff = 4


__all__ = ["BuffType"]
