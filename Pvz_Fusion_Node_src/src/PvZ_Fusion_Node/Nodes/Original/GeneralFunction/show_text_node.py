from typing import Any, Optional
from ..Node import Node, PortDef, PortDirection, PortType


class ShowTextNode(Node):
    # Status in Extensions: Implemented
    node_type = "ShowTextNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "文本": PortDef("文本", PortDirection.Input, PortType.String),
        "持续时间": PortDef("持续时间", PortDirection.Input, PortType.Float),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    # Port name constants
    Trigger_input_trigger : str = "触发"
    Text_input_string : str = "文本"
    Duration_input_float : str = "持续时间"
    Complete_output_trigger : str = "完成"

    def __init__(
        self,
        display_text: Any = None,
        duration: Any = None,
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        dt = display_text if display_text is not None else kwargs.pop("text", kwargs.pop("display_text", None))
        dur = duration if duration is not None else kwargs.pop("duration", None)

        if dt is not None:
            kwargs["text"] = dt
        if dur is not None:
            kwargs["duration"] = dur

        super().__init__(
            node_type="ShowTextNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )

        raw_text = dt if dt is not None else "示例文本"
        if not hasattr(raw_text, "node") and not hasattr(raw_text, "port_type"):
            self.set_property("displayText", str(raw_text))
        else:
            self.set_property("displayText", "示例文本")

        raw_dur = dur if dur is not None else 3.0
        if not hasattr(raw_dur, "node") and not hasattr(raw_dur, "port_type"):
            try:
                self.set_property("duration", float(raw_dur))
            except Exception:
                self.set_property("duration", 3.0)
        else:
            self.set_property("duration", 3.0)

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
        data["onComplete_PortName"] = "完成"
        return data
