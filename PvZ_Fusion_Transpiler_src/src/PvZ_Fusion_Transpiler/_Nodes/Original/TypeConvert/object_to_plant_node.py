from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ObjectToPlantNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ObjectToPlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Input, PortType.GameObject)
        self.port_output_plant_Plant : Port = self.create_port("植物", PortDirection.Output, PortType.Plant)
        self.port_output_bool_Exists : Port = self.create_port("存在", PortDirection.Output, PortType.Bool)


__all__ = ["ObjectToPlantNode"]
