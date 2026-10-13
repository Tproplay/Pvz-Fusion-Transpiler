from typing import Optional, Any
from ...Node import Node, PortDef, PortDirection, PortType
from .float_variable_asset import FloatVariableAsset


class FloatVariableNode(Node):
    # Status in Extensions: Implemented
    node_type = "FloatVariableNode"
    _class_ports = {
        "变量": PortDef("变量", PortDirection.Output, PortType.FloatVariable),
    }

    # Port name constants
    Variable_output_floatvariable : str = "变量"

    def __init__(
        self,
        var_name: str = "浮点数",
        initial_value: float = 0.0,
        asset: Optional[FloatVariableAsset] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs: Any,
    ):
        self.asset: FloatVariableAsset = asset or FloatVariableAsset(name=var_name, initial_value=initial_value)
        super().__init__(
            node_type="FloatVariableNode",
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
