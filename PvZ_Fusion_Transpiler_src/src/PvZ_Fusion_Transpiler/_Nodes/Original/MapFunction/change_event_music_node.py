from typing import Any
from ...._Data.MusicType import MusicType
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class ChangeEventMusicNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ChangeEventMusicNode"

    def __init__(self, music: Any = MusicType.Day, **kwargs: Any):
        super().__init__(**kwargs)
        m = kwargs.get("music", music)
        self.music: MusicType = validate_enum_field(m, MusicType, "music", default=MusicType.Day)
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["ChangeEventMusicNode"]
