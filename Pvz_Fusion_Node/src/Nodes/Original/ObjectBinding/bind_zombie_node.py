from typing import Optional
from ..Node import Node, PortDef, PortDirection, PortType


class BindZombieNode(Node):
    node_type = "BindZombieNode"
    _class_ports = {
        "触发": PortDef("触发", PortDirection.Input, PortType.Trigger),
        "僵尸": PortDef("僵尸", PortDirection.Input, PortType.Zombie),
        "完成": PortDef("完成", PortDirection.Output, PortType.Trigger),
    }

    def __init__(
        self,
        binding_name: str = "首领",
        node_id: Optional[str] = None,
        rid: Optional[int] = None,
        position_x: float = 0.0,
        position_y: float = 0.0,
        **kwargs,
    ):
        super().__init__(
            node_type="BindZombieNode",
            node_id=node_id,
            rid=rid,
            position_x=position_x,
            position_y=position_y,
            **kwargs,
        )
        self.set_property("bindingName", str(binding_name))

    @property
    def binding_name(self) -> str:
        return self.get_property("bindingName", "首领")

    @binding_name.setter
    def binding_name(self, name: str) -> None:
        self.set_property("bindingName", str(name))
