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

# Chinese aliases
ToolType.无 = ToolType.None_  # type: ignore[attr-defined]
ToolType.铲子 = ToolType.Shovel  # type: ignore[attr-defined]
ToolType.手套 = ToolType.Glove  # type: ignore[attr-defined]
ToolType.锤子 = ToolType.Hammer  # type: ignore[attr-defined]
ToolType.小推车 = ToolType.LawnMower  # type: ignore[attr-defined]
ToolType.金咖啡豆 = ToolType.GoldCoffeeBean  # type: ignore[attr-defined]
ToolType.桶 = ToolType.Bucket  # type: ignore[attr-defined]
ToolType.加农炮目标 = ToolType.CannonTarget  # type: ignore[attr-defined]
ToolType.植物预览 = ToolType.PlantPreview  # type: ignore[attr-defined]
ToolType.僵尸预览 = ToolType.ZombiePreview  # type: ignore[attr-defined]
ToolType.其他 = ToolType.Other  # type: ignore[attr-defined]


__all__ = ["ToolType"]
