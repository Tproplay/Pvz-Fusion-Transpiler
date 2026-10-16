from enum import Enum
from typing import Any
from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ZombieTypeValueNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "ZombieTypeValueNode"

    def __init__(self, value: Any = None, zombie_type: Any = None, zombieType: Any = None, **kwargs):
        super().__init__(**kwargs)
        zt = zombieType if zombieType is not None else (zombie_type if zombie_type is not None else value)
        if isinstance(zt, (int, float)) and not isinstance(zt, Enum):
            raise TypeError("ZombieType must be handled through the ZombieType enum, direct int input is not allowed.")
        if zt is not None:
            self.zombieType: int = int(getattr(zt, "value", zt))
        else:
            self.zombieType = 0
        self.value: int = self.zombieType
        self.port_output_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Output, PortType.ZombieType)


__all__ = ["ZombieTypeValueNode"]
