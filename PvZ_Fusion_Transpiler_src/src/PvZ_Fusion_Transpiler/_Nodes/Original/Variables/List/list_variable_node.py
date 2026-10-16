from __future__ import annotations

from typing import Any, List, Optional
from ...node import EventNodeBase, PortDirection, PortType, Port
from ...VariableAsset import ListVariableAsset


class ListVariableNode(EventNodeBase):
    node_type = "ListVariableNode"

    def __init__(
        self,
        name: str = "列表",
        value: Optional[List[Any]] = None,
        asset: Optional[ListVariableAsset] = None,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        if asset is not None:
            self.asset = asset
        else:
            self.asset = ListVariableAsset(name=name, initial_value=value or [])
        self.asset.add_reference(self.id)
        self.port_output_listvariable_Variable: Port = self.create_port(
            "变量", PortDirection.Output, PortType.ListVariable
        )
        self.port_output_listvariable_List: Port = self.port_output_listvariable_Variable


__all__ = ["ListVariableNode"]
