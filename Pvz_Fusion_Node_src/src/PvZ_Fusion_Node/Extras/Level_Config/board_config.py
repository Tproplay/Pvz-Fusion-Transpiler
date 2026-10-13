"""
Level Board Configuration schema matching Unity GameLevel boardConfig.
Contains gameplay modifiers, multipliers, conveyor timers, and random scaling bounds.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Any, Dict


@dataclass
class BoardConfig:
    izDropCount: int = 0
    redLineColumn: int = 5
    ignoreZombieHouse: bool = False
    zombieStartAmmor: float = 0.0  # Kept as Unity's original spelling 'Ammor'
    zombieHealthMultiplier: float = 1.0
    zombieDamageMultiplier: float = 1.0
    zombieSpeedMultiplier: float = 1.0
    zombieCountMultiplier: float = 1.0
    minOriginalSpeed: float = 1.0
    maxOriginalSpeed: float = 1.4
    waveInterval: float = 30.0
    firstWaveArrivedTimer: float = 15.0
    conveyInterval: float = 6.0
    gloveSpeed: float = 10.0
    holdTimer: float = 4.2
    holdTimer2: float = 1.8
    holdTimer3: float = 5.0
    startTip: str = ""
    tipTime: float = 6.0
    applyRandomData: bool = False
    plantModifyMin: float = 0.2
    plantModifyMax: float = 6.0
    plantSpeedMin: float = 0.2
    plantSpeedMax: float = 6.0
    plantSpeedAvg: float = 1.5
    zombieModifyMin: float = 0.1
    zombieModifyMax: float = 10.0
    zombieModifyAvg: float = 3.0
    zombieSpeedMin: float = 0.3
    zombieSpeedMax: float = 4.0
    zombieSpeedAvg: float = 1.5
    zombieScaleMin: float = 0.3
    zombieScaleMax: float = 2.5
    zombieScaleAvg: float = 1.0

    def to_dict(self) -> Dict[str, Any]:
        """Serializes board configuration to exact Unity JSON dict."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> BoardConfig:
        """Constructs BoardConfig from a raw dictionary, ignoring unknown keys gracefully."""
        field_names = set(cls.__dataclass_fields__.keys())
        filtered = {k: v for k, v in data.items() if k in field_names}
        return cls(**filtered)
