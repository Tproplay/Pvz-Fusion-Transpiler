from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ObjectToPlantNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "ObjectToPlantNode"

    def __init__(self):
        super().__init__()
        self.port_input_gameobject_GameObject : Port = self.create_port("Object", PortDirection.Input, PortType.GameObject)
        self.port_output_plant_Plant : Port = self.create_port("Plant", PortDirection.Output, PortType.Plant)
        self.port_output_bool_Exists : Port = self.create_port("Exists", PortDirection.Output, PortType.Bool)


__all__ = ["ObjectToPlantNode"]
