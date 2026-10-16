from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CompareGameObjectNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "CompareGameObjectNode"

    def __init__(self):
        super().__init__()
        self.port_input_gameobject_GameObjectA : Port = self.create_port("对象A", PortDirection.Input, PortType.GameObject)
        self.port_input_gameobject_GameObjectB : Port = self.create_port("对象B", PortDirection.Input, PortType.GameObject)
        self.port_output_bool_Same : Port = self.create_port("相同", PortDirection.Output, PortType.Bool)


__all__ = ["CompareGameObjectNode"]
