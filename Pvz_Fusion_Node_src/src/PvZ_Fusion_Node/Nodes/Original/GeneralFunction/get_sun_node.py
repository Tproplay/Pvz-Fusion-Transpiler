from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetSunNode(Node):
    node_type = "GetSunNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "阳光数量": PortDef("阳光数量", PortDirection.Input, PortType.Int),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        amount: Optional[Any] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        amt = amount if amount is not None else kwargs.pop("amount", kwargs.pop("sun_amount", kwargs.pop("sunAmount", kwargs.pop("sun", kwargs.pop("value", kwargs.pop("val", None))))))
        if amt is not None:
            kwargs["sunAmount"] = amt

        super().__init__(
            node_type="GetSunNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["sunAmount_PortName"] = "阳光数量"
        return data
