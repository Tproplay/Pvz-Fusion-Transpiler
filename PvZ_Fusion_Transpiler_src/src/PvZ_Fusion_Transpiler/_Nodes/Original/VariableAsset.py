from __future__ import annotations

import uuid
from typing import Any, Dict, List, Optional
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


class VariableAsset:
    """Base class for persistent level variable assets stored in references.RefIds and eventNodeGraph.variables."""

    ns: str = "GameLevel.EventNodes"
    asm: str = "Assembly-CSharp"
    asset_class: str = ""

    def __init__(
        self,
        name: str = "变量",
        initial_value: Any = 0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        self.name: str = name
        self.variable_id: str = variable_id or uuid.uuid4().hex
        self.rid: Optional[int] = rid
        self.referenced_node_ids: List[str] = []
        self.value: Any = initial_value
        _ctx.add_variable(self)

    def add_reference(self, node_id: str) -> None:
        if node_id not in self.referenced_node_ids:
            self.referenced_node_ids.append(node_id)

    def dump_data(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "variableId": self.variable_id,
            "referencedNodeIds": list(self.referenced_node_ids),
            "value": _sanitize_for_json(self.value),
        }

    def dump_ref(self) -> Dict[str, Any]:
        return {
            "rid": self.rid if self.rid is not None else 1000,
            "type": {
                "class": self.asset_class or self.__class__.__name__,
                "ns": self.ns,
                "asm": self.asm,
            },
            "data": self.dump_data(),
        }

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name={self.name!r} val={self.value!r} rid={self.rid}>"


class IntVariableAsset(VariableAsset):
    asset_class = "IntVariableAsset"

    def __init__(
        self,
        name: str = "整数",
        initial_value: int = 0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=int(initial_value),
            variable_id=variable_id,
            rid=rid,
        )


class FloatVariableAsset(VariableAsset):
    asset_class = "FloatVariableAsset"

    def __init__(
        self,
        name: str = "浮点数",
        initial_value: float = 0.0,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=float(initial_value),
            variable_id=variable_id,
            rid=rid,
        )


class BoolVariableAsset(VariableAsset):
    asset_class = "BoolVariableAsset"

    def __init__(
        self,
        name: str = "布尔值",
        initial_value: bool = False,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=bool(initial_value),
            variable_id=variable_id,
            rid=rid,
        )


class StringVariableAsset(VariableAsset):
    asset_class = "StringVariableAsset"

    def __init__(
        self,
        name: str = "字符串",
        initial_value: str = "",
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__(
            name=name,
            initial_value=str(initial_value),
            variable_id=variable_id,
            rid=rid,
        )


__all__ = [
    "VariableAsset",
    "IntVariableAsset",
    "FloatVariableAsset",
    "BoolVariableAsset",
    "StringVariableAsset",
]
