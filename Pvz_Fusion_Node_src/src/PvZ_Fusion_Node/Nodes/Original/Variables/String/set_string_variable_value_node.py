from typing import Any, Optional
from ...Node import Node, PortDef, PortDirection, PortType


class SetStringVariableValueNode(Node):
    # Status in Extensions: Implemented
    node_type = "SetStringVariableValueNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "变量": PortDef("变量", PortDirection.Input, PortType.StringVariable),
        "新值": PortDef("新值", PortDirection.Input, PortType.String),
        "变量Out": PortDef("变量", PortDirection.Output, PortType.StringVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Variable_input_stringvariable : str = "变量"
    NewValue_input_string : str = "新值"
    VariableOut_output_stringvariable : str = "变量Out"
    Complete_output_trigger : str = "完成"

    def __init__(
        self,
        variable: Optional[Any] = None,
        value: Optional[Any] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        var = variable if variable is not None else kwargs.pop("variable", kwargs.pop("var", None))
        val = value if value is not None else kwargs.pop("value", kwargs.pop("val", kwargs.pop("new_value", None)))
        if var is not None:
            kwargs["variable"] = var
        if val is not None:
            kwargs["value"] = val

        super().__init__(
            node_type="SetStringVariableValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["variable_PortName"] = "变量"
        data["value_PortName"] = "新值"
        data["variableOut_PortName"] = "变量"
        data["onComplete_PortName"] = "完成"
        return data

