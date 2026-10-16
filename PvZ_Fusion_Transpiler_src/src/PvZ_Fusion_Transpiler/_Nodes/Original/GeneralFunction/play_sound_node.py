from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlaySoundNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "PlaySoundNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_int_SoundId : Port = self.create_port("音效ID", PortDirection.Input, PortType.Int)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)


__all__ = ["PlaySoundNode"]
