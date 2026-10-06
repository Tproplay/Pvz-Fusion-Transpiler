from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class GetTravelEntryNode(Node):
    node_type = "GetTravelEntryNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        buff_type: int = 1,
        entry_index: int = 0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="GetTravelEntryNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("buffType", int(buff_type))
        self.set_property("entryIndex", int(entry_index))

    @property
    def buff_type(self) -> int:
        return self.get_property("buffType", 1)

    @buff_type.setter
    def buff_type(self, val: int) -> None:
        self.set_property("buffType", int(val))

    @property
    def entry_index(self) -> int:
        return self.get_property("entryIndex", 0)

    @entry_index.setter
    def entry_index(self, val: int) -> None:
        self.set_property("entryIndex", int(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        return data
