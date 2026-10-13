"""
GodShootingConfig container managing custom God Shooting combat rosters.
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional
from .god_plant import GodPlantConfig


class GodShootingConfig:
    def __init__(self, plants: Optional[List[GodPlantConfig]] = None):
        self.plants: List[GodPlantConfig] = list(plants or [])

    def add_plant(
        self,
        plant_type: int = 0,
        column: int = 2,
        row: int = 2,
        health: float = 300.0,
        attack: float = 20.0,
        is_player: bool = True,
        **kwargs: Any,
    ) -> GodPlantConfig:
        plant = GodPlantConfig(
            plantType=plant_type,
            column=column,
            row=row,
            health=health,
            maxHealth=health,
            attack=attack,
            isPlayer=is_player,
            customProperties=kwargs,
        )
        self.plants.append(plant)
        return plant

    def to_dict(self) -> Dict[str, Any]:
        return {
            "plants": [p.to_dict() for p in self.plants]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> GodShootingConfig:
        plants = [GodPlantConfig.from_dict(item) for item in data.get("plants", [])]
        return cls(plants=plants)
