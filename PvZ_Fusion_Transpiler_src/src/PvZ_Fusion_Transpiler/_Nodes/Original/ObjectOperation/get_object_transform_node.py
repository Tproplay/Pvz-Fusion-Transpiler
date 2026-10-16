from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetObjectTransformNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetObjectTransformNode"

    def __init__(self):
        super().__init__()
        self.port_input_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Input, PortType.GameObject)
        self.port_output_vector3_Position : Port = self.create_port("位置", PortDirection.Output, PortType.Vector3)
        self.port_output_vector3_Scale : Port = self.create_port("大小", PortDirection.Output, PortType.Vector3)
        self.port_output_bool_Exists : Port = self.create_port("存在", PortDirection.Output, PortType.Bool)


__all__ = ["GetObjectTransformNode"]
