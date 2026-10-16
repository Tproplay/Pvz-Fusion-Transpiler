from typing import Optional
from ...node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port
from ...VariableAsset import StringVariableAsset


class StringVariableNode(EventNodeBase):
    node_type = "StringVariableNode"

    def __init__(
        self,
        name: str = "字符串",
        value: str = "",
        asset: Optional[StringVariableAsset] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        if asset is not None:
            self.asset = asset
        else:
            self.asset = StringVariableAsset(name=name, initial_value=value)
        self.asset.add_reference(self.id)
        self.port_output_stringvariable_Variable : Port = self.create_port("变量", PortDirection.Output, PortType.StringVariable)


__all__ = ["StringVariableNode"]
