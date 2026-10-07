"""
Rhythm Level Data schema matching Unity rhythmLevelData.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List


@dataclass
class RhythmLevelData:
    musicType: int = 13
    musicName: str = "song"
    fallTime: float = 1.0
    bpm: float = 160.0
    audioOffset: float = 0.0
    notes: List[Any] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> RhythmLevelData:
        field_names = set(cls.__dataclass_fields__.keys())
        filtered = {k: v for k, v in data.items() if k in field_names}
        return cls(**filtered)
