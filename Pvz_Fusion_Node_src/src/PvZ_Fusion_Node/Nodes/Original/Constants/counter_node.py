from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class CounterNode(Node):
    node_type = "CounterNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "是否重置": PortDef("是否重置", PortDirection.Input, PortType.Bool),
        "计数": PortDef("计数", PortDirection.Output, PortType.Int),
        "计数完成": PortDef("计数完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        start_value: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="CounterNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("startValue", int(start_value))

    @property
    def start_value(self) -> int:
        return self.get_property("startValue", 0)

    @start_value.setter
    def start_value(self, val: int) -> None:
        self.set_property("startValue", int(val))
