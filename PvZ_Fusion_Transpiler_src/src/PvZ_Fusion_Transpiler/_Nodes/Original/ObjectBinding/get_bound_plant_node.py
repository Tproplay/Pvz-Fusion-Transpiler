from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetBoundPlantNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "GetBoundPlantNode"

    def __init__(self, bindingName: str = "守护目标", **kwargs: Any):
        super().__init__(**kwargs)
        self.bindingName: str = kwargs.get("binding_name", bindingName)
        self.port_input_string_Name : Port = self.create_port("Name", PortDirection.Input, PortType.String)
        self.port_output_plant_Plant : Port = self.create_port("Plant", PortDirection.Output, PortType.Plant)
        self.port_output_bool_Exists : Port = self.create_port("Exists", PortDirection.Output, PortType.Bool)

    @property
    def binding_name(self) -> str:
        return self.bindingName

    @binding_name.setter
    def binding_name(self, value: str) -> None:
        self.bindingName = value


__all__ = ["GetBoundPlantNode"]
