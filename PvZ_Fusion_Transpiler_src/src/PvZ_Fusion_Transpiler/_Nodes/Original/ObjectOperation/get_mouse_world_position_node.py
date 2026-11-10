from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetMouseWorldPositionNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetMouseWorldPositionNode"

    def __init__(self):
        super().__init__()
        self.port_output_vector3_Position : Port = self.create_port("Coordinates", PortDirection.Output, PortType.Vector3)
        self.port_output_int_Row : Port = self.create_port("Lane", PortDirection.Output, PortType.Int)
        self.port_output_int_Col : Port = self.create_port("Column", PortDirection.Output, PortType.Int)


__all__ = ["GetMouseWorldPositionNode"]
