from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ShowTextNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "ShowTextNode"

    def __init__(self, displayText: str = "示例文本", **kwargs: Any):
        super().__init__(**kwargs)
        self.displayText: str = kwargs.get("display_text", displayText)
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_string_Text : Port = self.create_port("文本", PortDirection.Input, PortType.String)
        self.port_input_float_Duration : Port = self.create_port("持续时间", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)

    @property
    def display_text(self) -> str:
        return self.displayText

    @display_text.setter
    def display_text(self, value: str) -> None:
        self.displayText = value


__all__ = ["ShowTextNode"]
