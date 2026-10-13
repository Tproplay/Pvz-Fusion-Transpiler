from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class FloatToIntNode(Node):
    node_type = "FloatToIntNode"
    _class_ports = {
        "浮点数": PortDef("浮点数", PortDirection.Input, PortType.Float),
        "整数": PortDef("整数", PortDirection.Output, PortType.Int),
    }

    def __init__(
        self,
        float_val: Optional[Any] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        val = float_val if float_val is not None else kwargs.pop("float", kwargs.pop("float_val", kwargs.pop("value", kwargs.pop("val", None))))
        if val is not None:
            kwargs["float"] = val

        super().__init__(
            node_type="FloatToIntNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["float_PortName"] = "浮点数"
        data["int_PortName"] = "整数"
        return data
