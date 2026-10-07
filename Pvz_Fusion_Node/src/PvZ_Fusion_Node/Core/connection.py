"""
Connection and pin wiring model matching Unity EventNodes connections.
"""

from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass(frozen=True)
class Connection:
    fromNodeId: str
    fromPortName: str
    toNodeId: str
    toPortName: str

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Connection:
        return cls(
            fromNodeId=str(data["fromNodeId"]),
            fromPortName=str(data["fromPortName"]),
            toNodeId=str(data["toNodeId"]),
            toPortName=str(data["toPortName"]),
        )
