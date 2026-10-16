from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetMouseWorldPositionNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetMouseWorldPositionNode"

    def __init__(self):
        super().__init__()
        self.port_output_vector3_Position : Port = self.create_port("坐标", PortDirection.Output, PortType.Vector3)
        self.port_output_int_Row : Port = self.create_port("行", PortDirection.Output, PortType.Int)
        self.port_output_int_Col : Port = self.create_port("列", PortDirection.Output, PortType.Int)


__all__ = ["GetMouseWorldPositionNode"]
