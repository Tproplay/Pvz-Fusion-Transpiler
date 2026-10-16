from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ModifyEventBulletNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ModifyEventBulletNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bullet_Bullet : Port = self.create_port("子弹", PortDirection.Input, PortType.Bullet)
        self.port_input_float_Value : Port = self.create_port("数值", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)


__all__ = ["ModifyEventBulletNode"]
