from enum import Enum


class Layer(Enum):
    """Layer enum in PvZ Fusion for plant placement layers."""

    Default = 0
    Lily = 1
    Pumpkin = 2
    Pot = 3
    Fly = 4


__all__ = ["Layer"]
