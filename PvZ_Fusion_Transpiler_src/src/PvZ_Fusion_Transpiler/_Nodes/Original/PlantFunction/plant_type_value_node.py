from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantTypeValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "PlantTypeValueNode"

    def __init__(self, value: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.value: int = int(value)
        self.port_output_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Output, PortType.PlantType)


__all__ = ["PlantTypeValueNode"]
