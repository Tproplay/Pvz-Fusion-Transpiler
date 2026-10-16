from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import re

from ...Core import uuid
from ...Core.connection_manager import PortDirection, PortType, Port
from ...Core.context import _ctx
from .definitions import get_node_definition


def _camel_to_snake(s: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()


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
        if direction == PortDirection.Input and port_type == PortType.Trigger and name == "触发":
            if _ctx.trigger_stack and not getattr(self, "_skip_auto_wire", False):
                prev = _ctx.trigger_stack[-1]
                prev_id = getattr(prev, "id", str(prev))
                prev_trigger = getattr(prev, "out_trigger", "触发")
                _ctx.add_connection(prev_id, prev_trigger, self.id, name)
                from ..Extentions.Abstract.execution_path import ExecutionPath
                if not isinstance(prev, ExecutionPath):
                    _ctx.trigger_stack[-1] = self
        return port

    def get_port(self, name: str) -> Port:
        for p in self.ports:
            if p.name == name:
                return p
        for attr in dir(self):
            if attr.startswith("port_"):
                val = getattr(self, attr)
                if isinstance(val, Port):
                    parts = attr.split("_")
                    if len(parts) >= 4 and parts[3].lower() == name.lower():
                        return val
        raise KeyError(f"Port '{name}' not found on {self}")

    def get_input(self, name: str) -> Port:
        for p in self.ports:
            if p.direction == PortDirection.Input and p.name == name:
                return p
        for attr in dir(self):
            if attr.startswith("port_input_"):
                val = getattr(self, attr)
                if isinstance(val, Port):
                    parts = attr.split("_")
                    if len(parts) >= 4 and parts[3].lower() == name.lower():
                        return val
        for p in self.ports:
            if p.direction == PortDirection.Input and (
                p.name.lower() == name.lower() or name.lower() in p.name.lower()
            ):
                return p
        raise KeyError(f"Input port '{name}' not found on {self}")

    def get_output(self, name: str) -> Port:
        for p in self.ports:
            if p.direction == PortDirection.Output and p.name == name:
                return p
        for attr in dir(self):
            if attr.startswith("port_output_"):
                val = getattr(self, attr)
                if isinstance(val, Port):
                    parts = attr.split("_")
                    if len(parts) >= 4 and parts[3].lower() == name.lower():
                        return val
        for p in self.ports:
            if p.direction == PortDirection.Output and (
                p.name.lower() == name.lower() or name.lower() in p.name.lower()
            ):
                return p
        raise KeyError(f"Output port '{name}' not found on {self}")

    @property
    def Output(self) -> Any:
        from ..Extentions.Abstract.execution_path import PathAccessor
        return PathAccessor(self)

    def path(self, trigger_name: str) -> Any:
        from ..Extentions.Abstract.execution_path import ExecutionPath
        return ExecutionPath(self.id, trigger_name)

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        for p in getattr(self, "ports", []):
            if p.name == name:
                return p
        normalized_name = name.lower().replace("_", "")
        attr_alias_map = {
            "sun": "sunamount",
            "money": "moneyamount",
            "plants": "plantlist",
            "allplants": "allplants",
            "true": "then",
            "false": "else",
            "triggerfalse": "else",
            "triggertrue": "then",
            "column": "col",
            "portoutputintcolumn": "col",
        }
        target_name = attr_alias_map.get(normalized_name, normalized_name)
        for attr in dir(self):
            if attr.startswith("port_"):
                parts = attr.split("_")
                if len(parts) >= 4:
                    p_norm = parts[3].lower().replace("_", "")
                    if p_norm == target_name or (target_name == "plantlist" and p_norm in ("plantlist", "allplants")):
                        return getattr(self, attr)
        alias_map = {
            "result": ["结果", "和", "差", "积", "商", "余数", "随机整数", "随机浮点数"],
            "equal": ["等于", "相同"],
            "not_equal": ["不等于"],
            "greater": ["大于"],
            "less": ["小于"],
            "condition": ["条件"],
            "count": ["计数", "数量"],
            "state": ["状态"],
            "currentplant": ["当前植物"],
            "currentplanttype": ["当前类型", "当前植物类型"],
            "currentindex": ["当前索引"],
            "index": ["当前索引"],
            "row": ["行"],
            "col": ["列"],
            "column": ["列"],
            "planttype": ["植物类型"],
            "zombietype": ["僵尸类型"],
            "attributecd": ["属性倒计时"],
            "attribute_countdown": ["属性倒计时"],
            "wave": ["波次"],
            "item": ["物品", "手上的物品"],
            "theitemtype": ["手上的物品", "物品"],
            "isleftbutton": ["是否左键", "是左键"],
            "isleftclick": ["是否左键", "是左键"],
            "plant": ["植物", "当前植物"],
            "zombie": ["僵尸", "当前僵尸"],
            "currentlist": ["当前列表"],
            "planttypelist": ["植物类型列表"],
            "variable": ["变量"],
            "value": ["值"],
            "sunamount": ["阳光", "阳光数量"],
            "sun": ["阳光", "阳光数量"],
            "moneyamount": ["金币", "金币数量"],
            "money": ["金币", "金币数量"],
            "plants": ["植物列表", "所有植物"],
            "plantedplant": ["种植的植物"],
        }
        lower_name = name.lower()
        if lower_name in alias_map:
            targets = alias_map[lower_name]
            for p in getattr(self, "ports", []):
                if p.name in targets:
                    return p
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

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

        # Specific TypeValueNodes use dedicated field names instead of 'value'
        if node_type == "BulletTypeValueNode":
            bt = getattr(self, "bulletType", getattr(self, "value", 0))
            data["bulletType"] = _sanitize_for_json(bt)
        elif node_type == "PlantTypeValueNode":
            pt = getattr(self, "plantType", getattr(self, "value", 0))
            data["plantType"] = _sanitize_for_json(pt)
        elif node_type == "ZombieTypeValueNode":
            zt = getattr(self, "zombieType", getattr(self, "value", 0))
            data["zombieType"] = _sanitize_for_json(zt)
        elif node_type == "ToolTypeValueNode":
            tt = getattr(self, "toolType", getattr(self, "value", 0))
            data["toolType"] = _sanitize_for_json(tt)
        elif hasattr(self, "value"):
            data["value"] = _sanitize_for_json(getattr(self, "value"))
        elif node_type.endswith("ValueNode"):
            if "Int" in node_type:
                data["value"] = 0
            elif "Float" in node_type:
                data["value"] = 0.0
            elif "Bool" in node_type:
                data["value"] = False
            elif "String" in node_type:
                data["value"] = ""

        # Specific Event nodes with special fields (e.g. OnKeyPressNode -> targetKey)
        if node_type == "OnKeyPressNode":
            tk = getattr(self, "targetKey", getattr(self, "target_key", None))
            if tk is not None:
                data["targetKey"] = _sanitize_for_json(getattr(tk, "value", tk))

        # Include asset reference if present
        if hasattr(self, "asset") and getattr(self, "asset") is not None:
            asset_obj = getattr(self, "asset")
            if hasattr(asset_obj, "rid"):
                data["asset"] = {"rid": asset_obj.rid}
            elif isinstance(asset_obj, dict):
                data["asset"] = asset_obj

        reserved = {
            "id", "x", "y", "position", "ports", "rid", "node_type", "node_name",
            "input_defaults", "inputDefaults", "value", "asset",
            "bulletType", "plantType", "zombieType", "toolType", "targetKey", "target_key",
        }

        # Check reflection dump definitions
        node_def = get_node_definition(node_type)
        if node_def is not None:
            # 1. Custom string/other properties defined on this class in Unity
            for prop, def_val in node_def.get("custom_props", {}).items():
                snake_prop = _camel_to_snake(prop)
                val = getattr(self, prop, getattr(self, snake_prop, def_val))
                if val is not None or def_val is not None:
                    data[prop] = _sanitize_for_json(val)
                reserved.add(prop)
                reserved.add(snake_prop)

            # 2. PortName properties defined on this class in Unity
            for port_prop in node_def.get("port_names", []):
                port_val = node_def.get("port_defaults", {}).get(port_prop)
                # If the node has a matching Port instance, use its actual name
                prefix = port_prop[:-9].lower() if port_prop.endswith("_PortName") else ""
                for attr in dir(self):
                    if attr.startswith("port_"):
                        p_val = getattr(self, attr)
                        if isinstance(p_val, Port):
                            parts = attr.split("_")
                            if len(parts) >= 4 and parts[3].lower() == prefix:
                                port_val = p_val.name
                                break
                if port_val is not None:
                    data[port_prop] = port_val
                reserved.add(port_prop)
        else:
            # Fallback for classes not present in reflection definitions
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

        for k, v in vars(self).items():
            if k not in reserved and not k.startswith("port_") and not k.startswith("_"):
                if hasattr(v, "rid"):
                    data[k] = {"rid": v.rid}
                else:
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
