from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class OnKeyPressNode(Node):
    node_type = "OnKeyPressNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        target_key: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="OnKeyPressNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("targetKey", int(target_key))

    @property
    def target_key(self) -> int:
        return self.get_property("targetKey", 0)

    @target_key.setter
    def target_key(self, val: int) -> None:
        self.set_property("targetKey", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        return data
