from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetMoneyNode(Node):
    node_type = "GetMoneyNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "金币数量": PortDef("金币数量", PortDirection.Input, PortType.Int),
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
        amt = amount if amount is not None else kwargs.pop("amount", kwargs.pop("money_amount", kwargs.pop("moneyAmount", kwargs.pop("money", kwargs.pop("value", kwargs.pop("val", None))))))
        if amt is not None:
            kwargs["moneyAmount"] = amt

        super().__init__(
            node_type="GetMoneyNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["moneyAmount_PortName"] = "金币数量"
        return data
