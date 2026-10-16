from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class MakeVector3Node(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "MakeVector3Node"

    def __init__(self):
        super().__init__()
        self.port_input_float_X : Port = self.create_port("X", PortDirection.Input, PortType.Float)
        self.port_input_float_Y : Port = self.create_port("Y", PortDirection.Input, PortType.Float)
        self.port_input_float_Z : Port = self.create_port("Z", PortDirection.Input, PortType.Float)
        self.port_output_vector3_Vector : Port = self.create_port("坐标", PortDirection.Output, PortType.Vector3)


__all__ = ["MakeVector3Node"]
