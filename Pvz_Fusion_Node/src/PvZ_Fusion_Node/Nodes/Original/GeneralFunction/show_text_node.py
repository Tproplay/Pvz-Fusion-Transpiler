from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ShowTextNode(Node):
    node_type = "ShowTextNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "文本": PortDef("文本", PortDirection.Input, PortType.String),
        "持续时间": PortDef("持续时间", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        display_text: str = "示例文本",
        duration: float = 3.0,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="ShowTextNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("displayText", str(display_text))
        self.set_property("duration", float(duration))

    @property
    def display_text(self) -> str:
        return self.get_property("displayText", "示例文本")

    @display_text.setter
    def display_text(self, val: str) -> None:
        self.set_property("displayText", str(val))

    @property
    def duration(self) -> float:
        return self.get_property("duration", 3.0)

    @duration.setter
    def duration(self, val: float) -> None:
        self.set_property("duration", float(val))

    def dump_data(self):
        data = super().dump_data()
        data["trigger_PortName"] = "触发"
        data["text_PortName"] = "文本"
        data["duration_PortName"] = "持续时间"
        return data
