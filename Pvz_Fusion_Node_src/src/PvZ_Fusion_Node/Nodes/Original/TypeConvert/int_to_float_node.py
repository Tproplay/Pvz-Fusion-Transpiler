from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class IntToFloatNode(Node):
    node_type = "IntToFloatNode"
    _class_ports = {
        "整数": PortDef("整数", PortDirection.Input, PortType.Int),
        "浮点数": PortDef("浮点数", PortDirection.Output, PortType.Float),
    }

    def __init__(
        self,
        int_val: Optional[Any] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        val = int_val if int_val is not None else kwargs.pop("int", kwargs.pop("int_val", kwargs.pop("value", kwargs.pop("val", None))))
        if val is not None:
            kwargs["int"] = val

        super().__init__(
            node_type="IntToFloatNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["int_PortName"] = "整数"
        data["float_PortName"] = "浮点数"
        return data
