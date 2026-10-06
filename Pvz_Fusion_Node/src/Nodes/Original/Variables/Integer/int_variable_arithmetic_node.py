from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType


class IntVariableArithmeticNode(Node):
    node_type = "IntVariableArithmeticNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "变量": PortDef("变量", PortDirection.Input, PortType.IntVariable),
        "操作数": PortDef("操作数", PortDirection.Input, PortType.Int),
        "变量Out": PortDef("变量", PortDirection.Output, PortType.IntVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

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
            node_type="IntVariableArithmeticNode",
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
