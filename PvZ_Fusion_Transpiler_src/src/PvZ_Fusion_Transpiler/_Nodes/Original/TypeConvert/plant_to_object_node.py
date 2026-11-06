from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantToObjectNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "PlantToObjectNode"

    def __init__(self):
        super().__init__()
        self.port_input_plant_Plant : Port = self.create_port("Plant", PortDirection.Input, PortType.Plant)
        self.port_output_gameobject_GameObject : Port = self.create_port("Object", PortDirection.Output, PortType.GameObject)


__all__ = ["PlantToObjectNode"]
