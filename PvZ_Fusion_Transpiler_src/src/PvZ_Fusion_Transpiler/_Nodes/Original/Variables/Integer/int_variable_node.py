from typing import Optional
from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port
from ...VariableAsset import IntVariableAsset


class IntVariableNode(EventNodeBase):
    node_type = "IntVariableNode"

    def __init__(
        self,
        name: str = "整数",
        value: int = 0,
        asset: Optional[IntVariableAsset] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        if asset is not None:
            self.asset = asset
        else:
            self.asset = IntVariableAsset(name=name, initial_value=value)
        self.asset.add_reference(self.id)
        self.port_output_intvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.IntVariable)


__all__ = ["IntVariableNode"]
