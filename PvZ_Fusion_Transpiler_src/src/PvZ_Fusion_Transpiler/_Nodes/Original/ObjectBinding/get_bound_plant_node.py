from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetBoundPlantNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetBoundPlantNode"

    def __init__(self):
        super().__init__()
        self.port_output_plant_Plant : Port = self.create_port("植物", PortDirection.Output, PortType.Plant)


__all__ = ["GetBoundPlantNode"]
