from typing import Optional
from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port
from ...VariableAsset import FloatVariableAsset


class FloatVariableNode(EventNodeBase):
    node_type = "FloatVariableNode"

    def __init__(
        self,
        name: str = "浮点数",
        value: float = 0.0,
        asset: Optional[FloatVariableAsset] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        if asset is not None:
            self.asset = asset
        else:
            self.asset = FloatVariableAsset(name=name, initial_value=value)
        self.asset.add_reference(self.id)
        self.port_output_floatvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.FloatVariable)


__all__ = ["FloatVariableNode"]
