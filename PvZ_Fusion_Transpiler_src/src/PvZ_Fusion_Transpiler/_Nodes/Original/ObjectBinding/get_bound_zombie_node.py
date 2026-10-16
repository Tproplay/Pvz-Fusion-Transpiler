from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetBoundZombieNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "GetBoundZombieNode"

    def __init__(self, bindingName: str = "首领", **kwargs: Any):
        super().__init__(**kwargs)
        self.bindingName: str = kwargs.get("binding_name", bindingName)
        self.port_output_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Output, PortType.Zombie)

    @property
    def binding_name(self) -> str:
        return self.bindingName

    @binding_name.setter
    def binding_name(self, value: str) -> None:
        self.bindingName = value


__all__ = ["GetBoundZombieNode"]
