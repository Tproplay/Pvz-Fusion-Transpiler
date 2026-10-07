from typing import Optional
from ...Node import Node, PortDef, PortDirection, PortType


class SetIntVariableValueNode(Node):
    node_type = "SetIntVariableValueNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "变量": PortDef("变量", PortDirection.Input, PortType.IntVariable),
        "新值": PortDef("新值", PortDirection.Input, PortType.Int),
        "变量Out": PortDef("变量", PortDirection.Output, PortType.IntVariable),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="SetIntVariableValueNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        # SetIntVariableValueNode maps variableOut_PortName to "变量"
        data["variableOut_PortName"] = "变量"
        data["onComplete_PortName"] = "完成"
        return data
