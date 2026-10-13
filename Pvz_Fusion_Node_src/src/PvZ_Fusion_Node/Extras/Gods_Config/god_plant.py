"""
God Shooting Plant configuration representing playable/ally combat units.
"""

from __future__ import annotations
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class GodPlantConfig:
    plantType: int = 0
    column: int = 2
    row: int = 2
    health: float = 300.0
    maxHealth: float = 300.0
    attack: float = 20.0
    attackInterval: float = 1.5
    speed: float = 3.0
    bulletType: int = 0
    bulletSpeed: float = 6.0
    bulletCount: int = 1
    isPlayer: bool = True
    skills: List[Dict[str, Any]] = field(default_factory=list)
    customProperties: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "plantType": self.plantType,
            "column": self.column,
            "row": self.row,
            "health": self.health,
            "maxHealth": self.maxHealth,
            "attack": self.attack,
            "attackInterval": self.attackInterval,
            "speed": self.speed,
            "bulletType": self.bulletType,
            "bulletSpeed": self.bulletSpeed,
            "bulletCount": self.bulletCount,
            "isPlayer": self.isPlayer,
            "skills": list(self.skills),
        }
        data.update(self.customProperties)
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> GodPlantConfig:
        known = {
            "plantType", "column", "row", "health", "maxHealth",
            "attack", "attackInterval", "speed", "bulletType",
            "bulletSpeed", "bulletCount", "isPlayer", "skills"
        }
        filtered = {k: v for k, v in data.items() if k in known}
        custom = {k: v for k, v in data.items() if k not in known}
        return cls(**filtered, customProperties=custom)
