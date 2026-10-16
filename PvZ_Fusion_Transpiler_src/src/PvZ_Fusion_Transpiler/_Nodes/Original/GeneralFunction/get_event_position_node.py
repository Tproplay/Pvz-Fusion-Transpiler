from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetEventPositionNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetEventPositionNode"

    def __init__(self):
        super().__init__()
        self.port_output_vector3_Position : Port = self.create_port("位置", PortDirection.Output, PortType.Vector3)


__all__ = ["GetEventPositionNode"]
