from enum import Enum


class ToolType(Enum):
    """EventToolType enum in PvZ Fusion."""

    None_ = 0
    Shovel = 1
    Glove = 2
    Hammer = 3
    LawnMower = 4
    GoldCoffeeBean = 5
    Bucket = 6
    CannonTarget = 7
    PlantPreview = 8
    ZombiePreview = 9
    Other = 10


# Aliases for convenience / naming variations
ToolType.NoneTool = ToolType.None_  # type: ignore[attr-defined]
ToolType.Cart = ToolType.LawnMower  # type: ignore[attr-defined]
ToolType.CoffeeBean = ToolType.GoldCoffeeBean  # type: ignore[attr-defined]


__all__ = ["ToolType"]
