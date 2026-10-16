from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantTypeValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "PlantTypeValueNode"

    def __init__(self):
        super().__init__()
        self.port_output_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Output, PortType.PlantType)


__all__ = ["PlantTypeValueNode"]
