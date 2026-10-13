from typing import Optional, Any
from ...Node import Node, PortDef, PortDirection, PortType
from .string_variable_asset import StringVariableAsset


class StringVariableNode(Node):
    # Status in Extensions: Implemented
    node_type = "StringVariableNode"
    _class_ports = {
        "变量": PortDef("变量", PortDirection.Output, PortType.StringVariable),
    }

    # Port name constants
    Variable_output_stringvariable : str = "变量"

    def __init__(
        self,
        var_name: str = "字符串",
        initial_value: str = "",
        asset: Optional[StringVariableAsset] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs: Any,
    ):
        self.asset: StringVariableAsset = asset or StringVariableAsset(name=var_name, initial_value=initial_value)
        super().__init__(
            node_type="StringVariableNode",
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
