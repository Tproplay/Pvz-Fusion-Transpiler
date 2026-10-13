"""
Connection and pin wiring model matching Unity EventNodes connections.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class Connection:
    sourceNodeId: str = ""
    sourcePortName: str = ""
    targetNodeId: str = ""
    targetPortName: str = ""

    def __init__(
        self,
        sourceNodeId: Optional[str] = None,
        sourcePortName: Optional[str] = None,
        targetNodeId: Optional[str] = None,
        targetPortName: Optional[str] = None,
        fromNodeId: Optional[str] = None,
        fromPortName: Optional[str] = None,
        toNodeId: Optional[str] = None,
        toPortName: Optional[str] = None,
    ):
        src_id = str(sourceNodeId if sourceNodeId is not None else (fromNodeId if fromNodeId is not None else ""))
        src_port = str(sourcePortName if sourcePortName is not None else (fromPortName if fromPortName is not None else ""))
        tgt_id = str(targetNodeId if targetNodeId is not None else (toNodeId if toNodeId is not None else ""))
        tgt_port = str(targetPortName if targetPortName is not None else (toPortName if toPortName is not None else ""))
        object.__setattr__(self, "sourceNodeId", src_id)
        object.__setattr__(self, "sourcePortName", src_port)
        object.__setattr__(self, "targetNodeId", tgt_id)
        object.__setattr__(self, "targetPortName", tgt_port)

    # Backward-compatibility aliases for legacy code
    @property
    def fromNodeId(self) -> str:
        return self.sourceNodeId

    @property
    def fromPortName(self) -> str:
        return self.sourcePortName

    @property
    def toNodeId(self) -> str:
        return self.targetNodeId

    @property
    def toPortName(self) -> str:
        return self.targetPortName

    def to_dict(self) -> Dict[str, str]:
        return {
            "sourceNodeId": self.sourceNodeId,
            "sourcePortName": self.sourcePortName,
            "targetNodeId": self.targetNodeId,
            "targetPortName": self.targetPortName,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Connection:
        return cls(
            sourceNodeId=str(data.get("sourceNodeId", data.get("fromNodeId", ""))),
            sourcePortName=str(data.get("sourcePortName", data.get("fromPortName", ""))),
            targetNodeId=str(data.get("targetNodeId", data.get("toNodeId", ""))),
            targetPortName=str(data.get("targetPortName", data.get("toPortName", ""))),
        )
