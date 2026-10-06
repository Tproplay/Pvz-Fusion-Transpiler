from abc import ABC
from typing import Any, List, Optional
import uuid


class VariableAsset(ABC):
    """Base class for all persistent level variable assets stored in references.RefIds."""

    asset_class: str = ""
    namespace: str = "GameLevel.EventNodes"
    assembly: str = "Assembly-CSharp"

    def __init__(
        self,
        name: str,
        initial_value: Any,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        self.name: str = name
        self.variable_id: str = variable_id or uuid.uuid4().hex
        self.rid: Optional[int] = rid
        self.referenced_node_ids: List[str] = []
        self._value: Any = initial_value

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, val: Any) -> None:
        self._value = val

    def add_reference(self, node_id: str) -> None:
        if node_id not in self.referenced_node_ids:
            self.referenced_node_ids.append(node_id)

    def dump_data(self) -> dict:
        return {
            "name": self.name,
            "variableId": self.variable_id,
            "referencedNodeIds": list(self.referenced_node_ids),
            "value": self._value,
        }

    def dump_ref(self) -> dict:
        if self.rid is None:
            raise ValueError(f"Variable '{self.name}' ({self.variable_id}) cannot be dumped without an assigned 'rid'.")
        return {
            "rid": self.rid,
            "type": {
                "class": self.asset_class or self.__class__.__name__,
                "ns": self.namespace,
                "asm": self.assembly,
            },
            "data": self.dump_data(),
        }

    def dump_graph_variable(self) -> dict:
        if self.rid is None:
            raise ValueError(f"Variable '{self.name}' ({self.variable_id}) cannot be dumped without an assigned 'rid'.")
        return {"rid": self.rid}

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' rid={self.rid} id={self.variable_id[:8]}>"
