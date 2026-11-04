from typing import Any
from ...._Data.Layer import Layer
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port, validate_enum_field


class GetPlantsOnLayerNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "GetPlantsOnLayerNode"

    def __init__(self, layer: Any = Layer.Default, **kwargs: Any):
        super().__init__(**kwargs)
        l = kwargs.get("layer", layer)
        self.layer: Layer = validate_enum_field(l, Layer, "layer", default=Layer.Default)
        self.port_output_plantlist_PlantList : Port = self.create_port("植物列表", PortDirection.Output, PortType.PlantList)


__all__ = ["GetPlantsOnLayerNode"]
