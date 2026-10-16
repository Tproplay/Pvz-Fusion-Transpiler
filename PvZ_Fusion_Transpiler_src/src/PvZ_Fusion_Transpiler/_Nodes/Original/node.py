from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ...Core import uuid
from ...Core.connection_manager import PortDirection, PortType, Port
from ...Core.context import _ctx


def _sanitize_for_json(val: Any) -> Any:
    if hasattr(val, "value"):
        return _sanitize_for_json(val.value)
    if isinstance(val, dict):
        return {str(k): _sanitize_for_json(v) for k, v in val.items()}
    if isinstance(val, (list, tuple, set)):
        return [_sanitize_for_json(v) for v in val]
    if isinstance(val, (str, int, float, bool)) or val is None:
        return val
    return str(val)


class Node(ABC):
    
    def __init__(self, x: float = 0.0, y: float = 0.0, **kwargs: Any):
        self.id: str = str(uuid.generate_uuid())
        self.x: float = float(x)
        self.y: float = float(y)
        self.ports: List[Port] = []
        self.rid: Optional[int] = None
        for k, v in kwargs.items():
            setattr(self, k, v)
        _ctx.add_node(self)

    @property
    def position(self) -> Dict[str, float]:
        return {"x": self.x, "y": self.y}

    @position.setter
    def position(self, val: Dict[str, float]) -> None:
        if isinstance(val, dict):
            self.x = float(val.get("x", self.x))
            self.y = float(val.get("y", self.y))

    def create_port(self, name : str, direction : PortDirection, port_type : PortType) -> Port:
        port = Port(self, name, direction, port_type)
        self.ports.append(port)
        return port

    def dump_data(self) -> Dict[str, Any]:
        node_type = getattr(self, "node_type", self.__class__.__name__)
        data: Dict[str, Any] = {
            "inputDefaults": getattr(self, "input_defaults", getattr(self, "inputDefaults", [])),
            "nodeId": self.id,
            "nodeType": node_type,
            "position": {
                "x": float(self.x),
                "y": float(self.y),
            },
            "nodeName": getattr(self, "node_name", node_type),
        }

        # Include value if present or for ValueNode types
        if hasattr(self, "value"):
            data["value"] = _sanitize_for_json(getattr(self, "value"))
        elif node_type.endswith("ValueNode"):
            if any(k in node_type for k in ("Int", "PlantType", "ZombieType", "BulletType", "ToolType")):
                data["value"] = 0
            elif "Float" in node_type:
                data["value"] = 0.0
            elif "Bool" in node_type:
                data["value"] = False
            elif "String" in node_type:
                data["value"] = ""

        # Include asset reference if present
        if hasattr(self, "asset") and getattr(self, "asset") is not None:
            asset_obj = getattr(self, "asset")
            if hasattr(asset_obj, "rid"):
                data["asset"] = {"rid": asset_obj.rid}
            elif isinstance(asset_obj, dict):
                data["asset"] = asset_obj

        # For EventNodeBase, populate port name properties
        if isinstance(self, EventNodeBase):
            for attr in dir(self):
                if attr.startswith("port_"):
                    val = getattr(self, attr)
                    if isinstance(val, Port):
                        parts = attr.split("_")
                        if len(parts) >= 4:
                            prop_name = parts[3]
                            camel_prop = prop_name[0].lower() + prop_name[1:]
                            data[f"{camel_prop}_PortName"] = val.name

        reserved = {
            "id", "x", "y", "position", "ports", "rid", "node_type", "node_name",
            "input_defaults", "inputDefaults", "value", "asset",
        }
        for k, v in vars(self).items():
            if k not in reserved and not k.startswith("port_") and not k.startswith("_"):
                data[k] = _sanitize_for_json(v)

        return data

    def dump_ref(self) -> Dict[str, Any]:
        node_type = getattr(self, "node_type", self.__class__.__name__)
        return {
            "rid": self.rid if self.rid is not None else 1000,
            "type": {
                "class": node_type,
                "ns": getattr(self, "ns", "GameLevel.EventNodes"),
                "asm": getattr(self, "asm", "Assembly-CSharp"),
            },
            "data": self.dump_data(),
        }

    def __repr__(self) -> str:
        ntype = getattr(self, "node_type", self.__class__.__name__)
        return f"<{ntype} id={self.id[:8]} rid={self.rid}>"


class EventNodeBase(Node):
    """Abstract base class for legacy EventNodeBase nodes."""
    pass


class EventSuggestedNode(Node):
    """Abstract base class for modern EventSuggestedNode nodes."""
    pass
