from typing import Any, Dict, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetTravelBuffNode(Node):
    node_type = "GetTravelBuffNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "成功": PortDef("成功", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        buff: Optional[Dict[str, Any]] = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="GetTravelBuffNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("buff", buff or {"rid": -2})

    @property
    def buff(self) -> Dict[str, Any]:
        return self.get_property("buff", {"rid": -2})

    @buff.setter
    def buff(self, val: Dict[str, Any]) -> None:
        self.set_property("buff", val)

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["onSuccess_PortName"] = "成功"
        return data
