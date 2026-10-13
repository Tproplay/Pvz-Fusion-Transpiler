"""
NodeGroup model matching Unity EventNodes visual grouping.
Provides grouping bounds, titles, node membership, and references.RefIds serialization.
"""

from __future__ import annotations

import uuid
from typing import Any, Dict, List, Optional


class NodeGroup:
    """Represents a visual grouping box enclosing related nodes in the editor."""

    DEFAULT_BACKGROUND_COLOR = {
        "r": 0.20000000298023225,
        "g": 0.4000000059604645,
        "b": 0.800000011920929,
        "a": 0.30000001192092898,
    }

    def __init__(
        self,
        title: str = "Group",
        group_id: Optional[str] = None,
        node_ids: Optional[List[str]] = None,
        position: Optional[Dict[str, float]] = None,
        size: Optional[Dict[str, float]] = None,
        background_color: Optional[Dict[str, float]] = None,
        is_folded: bool = False,
        rid: Optional[int] = None,
    ):
        self.rid: Optional[int] = rid
        self.group_id: str = group_id or str(uuid.uuid4())
        self.title: str = title
        self.node_ids: List[str] = list(node_ids) if node_ids else []
        self.position: Dict[str, float] = dict(position) if position else {"x": 0.0, "y": 0.0}
        self.size: Dict[str, float] = dict(size) if size else {"x": 350.0, "y": 200.0}
        self.background_color: Dict[str, float] = (
            dict(background_color) if background_color else dict(self.DEFAULT_BACKGROUND_COLOR)
        )
        self.is_folded: bool = is_folded

        # Metadata for Unity RefIds serialization
        self.node_type: str = "NodeGroup"
        self.namespace: str = "GameLevel.EventNodes"
        self.assembly: str = "Assembly-CSharp"

    # Convenient camelCase aliases
    @property
    def groupId(self) -> str:
        return self.group_id

    @groupId.setter
    def groupId(self, value: str) -> None:
        self.group_id = value

    @property
    def nodeIds(self) -> List[str]:
        return self.node_ids

    @nodeIds.setter
    def nodeIds(self, value: List[str]) -> None:
        self.node_ids = list(value)

    @property
    def isFolded(self) -> bool:
        return self.is_folded

    @isFolded.setter
    def isFolded(self, value: bool) -> None:
        self.is_folded = value

    @property
    def backgroundColor(self) -> Dict[str, float]:
        return self.background_color

    @backgroundColor.setter
    def backgroundColor(self, value: Dict[str, float]) -> None:
        self.background_color = dict(value)

    def add_node_id(self, node_id: str) -> None:
        if node_id not in self.node_ids:
            self.node_ids.append(node_id)

    def dump_data(self) -> Dict[str, Any]:
        """Serializes the 'data' payload for references.RefIds."""
        return {
            "groupId": self.group_id,
            "title": self.title,
            "backgroundColor": {
                "r": float(self.background_color.get("r", 0.2)),
                "g": float(self.background_color.get("g", 0.4)),
                "b": float(self.background_color.get("b", 0.8)),
                "a": float(self.background_color.get("a", 0.3)),
            },
            "nodeIds": list(self.node_ids),
            "position": {
                "x": float(self.position.get("x", 0.0)),
                "y": float(self.position.get("y", 0.0)),
            },
            "size": {
                "x": float(self.size.get("x", 350.0)),
                "y": float(self.size.get("y", 200.0)),
            },
            "isFolded": bool(self.is_folded),
        }

    def dump_ref(self) -> Dict[str, Any]:
        """Serializes the complete entry for references.RefIds."""
        if self.rid is None:
            raise ValueError(
                f"NodeGroup '{self.title}' ({self.group_id}) cannot be serialized without an assigned 'rid'."
            )
        return {
            "rid": self.rid,
            "type": {
                "class": self.node_type,
                "ns": self.namespace,
                "asm": self.assembly,
            },
            "data": self.dump_data(),
        }

    def dump_graph_group(self) -> Dict[str, int]:
        """Serializes the compact reference for eventNodeGraph.groups."""
        if self.rid is None:
            raise ValueError(
                f"NodeGroup '{self.title}' ({self.group_id}) cannot be serialized without an assigned 'rid'."
            )
        return {"rid": self.rid}

    @classmethod
    def from_dict(cls, data: Dict[str, Any], rid: Optional[int] = None) -> NodeGroup:
        """Constructs a NodeGroup from dictionary data."""
        g_id = data.get("groupId", data.get("group_id"))
        n_ids = data.get("nodeIds", data.get("node_ids", []))
        pos = data.get("position", {"x": 0.0, "y": 0.0})
        sz = data.get("size", {"x": 350.0, "y": 200.0})
        bg = data.get("backgroundColor", data.get("background_color"))
        folded = data.get("isFolded", data.get("is_folded", False))
        assigned_rid = rid if rid is not None else data.get("rid")

        return cls(
            title=data.get("title", "Group"),
            group_id=g_id,
            node_ids=n_ids,
            position=pos,
            size=sz,
            background_color=bg,
            is_folded=folded,
            rid=assigned_rid,
        )

    def __repr__(self) -> str:
        return f"<NodeGroup title='{self.title}' rid={self.rid} id={self.group_id[:8]} nodes={len(self.node_ids)}>"
