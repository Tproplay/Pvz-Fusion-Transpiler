from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class FloatToStringNode(Node):
    node_type = "FloatToStringNode"
    _class_ports = {
        "数值": PortDef("数值", PortDirection.Input, PortType.Float),
        "小数位数": PortDef("小数位数", PortDirection.Input, PortType.Int),
        "字符串": PortDef("字符串", PortDirection.Output, PortType.String),
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
            node_type="FloatToStringNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["value_PortName"] = "数值"
        data["decimals_PortName"] = "小数位数"
        data["result_PortName"] = "字符串"
        return data
