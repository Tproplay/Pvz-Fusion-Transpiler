"""
High-level ListVar managing ListVariableAsset and unified list operations.
"""

from __future__ import annotations
from typing import Any, Iterable, List, Optional, Union

from ...Original.Node import Node, Port, PortType, PortDirection
from ..extension_node import ExtensionNode
from ...Original.Variables.List.list_variable_asset import ListVariableAsset, ListElementType
from ...Original.Variables.List.list_nodes import (
    AppendIntListNode, AppendFloatListNode, AppendBoolListNode, AppendStringListNode,
    AppendPlantTypeListNode, AppendZombieTypeListNode, AppendObjectListNode,
    GetIntListItemNode, GetFloatListItemNode, GetBoolListItemNode, GetStringListItemNode,
    GetPlantTypeListItemNode, GetZombieTypeListItemNode, GetObjectListItemNode,
    ClearListValuesNode, RemoveListItemNode, GetListLengthNode
)


class ListVar(ExtensionNode):
    """High-level unified List Variable for runtime visual scripting."""

    def __init__(
        self,
        name: str = "列表",
        element_type: Union[ListElementType, int] = ListElementType.Integer,
        initial_values: Optional[Iterable[Any]] = None,
        variable_id: Optional[str] = None,
        rid: Optional[int] = None,
    ):
        super().__init__()
        self.element_type = ListElementType(element_type)
        self.asset = ListVariableAsset(
            name=name,
            element_type=self.element_type,
            initial_values=list(initial_values) if initial_values is not None else [],
            variable_id=variable_id,
            rid=rid,
        )

    @property
    def name(self) -> str:
        return self.asset.name

    def get_primary_port(self) -> Optional[Port]:
        # ListVariable itself is referenced through its asset RID on list operations
        return None

    def append(self, value: Any) -> Node:
        """Appends an element to the list by emitting the type-specific append node."""
        if self.element_type == ListElementType.Integer:
            n = AppendIntListNode()
        elif self.element_type == ListElementType.Float:
            n = AppendFloatListNode()
        elif self.element_type == ListElementType.Bool:
            n = AppendBoolListNode()
        elif self.element_type == ListElementType.String:
            n = AppendStringListNode()
        elif self.element_type == ListElementType.PlantType:
            n = AppendPlantTypeListNode()
        elif self.element_type == ListElementType.ZombieType:
            n = AppendZombieTypeListNode()
        else:
            n = AppendObjectListNode()
        self.attach_node(n)
        return n

    def get_at(self, index: Any) -> Node:
        """Retrieves an element at the specified index."""
        if self.element_type == ListElementType.Integer:
            n = GetIntListItemNode()
        elif self.element_type == ListElementType.Float:
            n = GetFloatListItemNode()
        elif self.element_type == ListElementType.Bool:
            n = GetBoolListItemNode()
        elif self.element_type == ListElementType.String:
            n = GetStringListItemNode()
        elif self.element_type == ListElementType.PlantType:
            n = GetPlantTypeListItemNode()
        elif self.element_type == ListElementType.ZombieType:
            n = GetZombieTypeListItemNode()
        else:
            n = GetObjectListItemNode()
        self.attach_node(n)
        return n

    def clear(self) -> Node:
        n = ClearListValuesNode()
        self.attach_node(n)
        return n

    def remove_at(self, index: Any) -> Node:
        n = RemoveListItemNode()
        self.attach_node(n)
        return n

    def length(self) -> Node:
        n = GetListLengthNode()
        self.attach_node(n)
        return n
