from enum import Enum
from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class PlantTypeValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "PlantTypeValueNode"

    def __init__(self, value: Any = None, plant_type: Any = None, plantType: Any = None, **kwargs):
        super().__init__(**kwargs)
        pt = plantType if plantType is not None else (plant_type if plant_type is not None else value)
        if isinstance(pt, (int, float)) and not isinstance(pt, Enum):
            raise TypeError("PlantType must be handled through the PlantType enum, direct int input is not allowed.")
        if pt is not None:
            self.plantType: int = int(getattr(pt, "value", pt))
        else:
            self.plantType = 0
        self.value: int = self.plantType
        self.port_output_planttype_PlantType : Port = self.create_port("植物类型", PortDirection.Output, PortType.PlantType)


__all__ = ["PlantTypeValueNode"]
