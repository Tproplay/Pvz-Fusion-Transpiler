from typing import Optional
from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port
from ...VariableAsset import BoolVariableAsset


class BoolVariableNode(EventNodeBase):
    node_type = "BoolVariableNode"

    def __init__(
        self,
        name: str = "布尔值",
        value: bool = False,
        asset: Optional[BoolVariableAsset] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        if asset is not None:
            self.asset = asset
        else:
            self.asset = BoolVariableAsset(name=name, initial_value=value)
        self.asset.add_reference(self.id)
        self.port_output_boolvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.BoolVariable)


__all__ = ["BoolVariableNode"]
