from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class BulletTypeValueNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "BulletTypeValueNode"

    def __init__(self):
        super().__init__()
        self.port_output_bullettype_BulletType : Port = self.create_port("子弹类型", PortDirection.Output, PortType.BulletType)


__all__ = ["BulletTypeValueNode"]
