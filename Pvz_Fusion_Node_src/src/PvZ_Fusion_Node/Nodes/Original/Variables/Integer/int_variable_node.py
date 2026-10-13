from typing import Optional, Any
from ...Node import Node, PortDef, PortDirection, PortType
from .int_variable_asset import IntVariableAsset


class IntVariableNode(Node):
    node_type = "IntVariableNode"
    _class_ports = {
        "变量": PortDef("变量", PortDirection.Output, PortType.IntVariable),
    }

    def __init__(
        self,
        var_name: str = "整数",
        initial_value: int = 0,
        asset: Optional[IntVariableAsset] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs: Any,
    ):
        self.asset: IntVariableAsset = asset or IntVariableAsset(name=var_name, initial_value=initial_value)
        super().__init__(
            node_type="IntVariableNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.asset.add_reference(self.node_id)

    def dump_data(self) -> dict[str, Any]:
        data = super().dump_data()
        data["asset"] = {"rid": self.asset.rid}
        data["variable_PortName"] = "变量"
        return data
