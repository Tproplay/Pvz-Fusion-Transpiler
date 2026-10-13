from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType


class FloatVariableArithmeticNode(Node):
    # Status in Extensions: Implemented
    node_type = "FloatVariableArithmeticNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "变量": PortDef("变量", PortDirection.Input, PortType.FloatVariable),
        "操作数": PortDef("操作数", PortDirection.Input, PortType.Float),
        "变量Out": PortDef("变量", PortDirection.Output, PortType.FloatVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Variable_input_floatvariable : str = "变量"
    Operand_input_float : str = "操作数"
    VariableOut_output_floatvariable : str = "变量Out"
    Complete_output_trigger : str = "完成"

    def __init__(
        self,
        operation: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="FloatVariableArithmeticNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("operation", int(operation))

    @property
    def operation(self) -> int:
        return self.get_property("operation", 0)

    @operation.setter
    def operation(self, op: int) -> None:
        self.set_property("operation", int(op))

    def dump_data(self):
        data = super().dump_data()
        data["variable_PortName"] = "变量"
        data["operand_PortName"] = "操作数"
        data["variableOut_PortName"] = "变量"
        data["onComplete_PortName"] = "完成"
        return data

