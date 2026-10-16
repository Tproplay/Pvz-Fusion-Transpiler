from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class BindZombieNode(EventNodeBase):
    # Status in Extensions: Implemented
    node_type = "BindZombieNode"

    def __init__(self, bindingName: str = "首领", **kwargs: Any):
        super().__init__(**kwargs)
        self.bindingName: str = kwargs.get("binding_name", bindingName)
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombie_Zombie : Port = self.create_port("僵尸", PortDirection.Input, PortType.Zombie)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)

    @property
    def binding_name(self) -> str:
        return self.bindingName

    @binding_name.setter
    def binding_name(self, value: str) -> None:
        self.bindingName = value


__all__ = ["BindZombieNode"]
