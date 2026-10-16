from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantToObjectNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "PlantToObjectNode"

    def __init__(self):
        super().__init__()
        self.port_input_plant_Plant : Port = self.create_port("植物", PortDirection.Input, PortType.Plant)
        self.port_output_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Output, PortType.GameObject)


__all__ = ["PlantToObjectNode"]
