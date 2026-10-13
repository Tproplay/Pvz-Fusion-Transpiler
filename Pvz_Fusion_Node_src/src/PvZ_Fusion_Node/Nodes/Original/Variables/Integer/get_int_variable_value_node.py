from typing import Any, Optional
from ...Node import Node, PortDef, PortDirection, PortType


class GetIntVariableValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "GetIntVariableValueNode"
    _class_ports = {
        "变量": PortDef("变量", PortDirection.Input, PortType.IntVariable),
        "值": PortDef("值", PortDirection.Output, PortType.Int),
    }

    # Port name constants
    Variable_input_intvariable : str = "变量"
    Value_output_int : str = "值"

    def __init__(
        self,
        variable: Optional[Any] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        var = variable if variable is not None else kwargs.pop("variable", kwargs.pop("var", None))
        if var is not None:
            kwargs["variable"] = var

        super().__init__(
            node_type="GetIntVariableValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["variable_PortName"] = "变量"
        data["value_PortName"] = "值"
        return data

