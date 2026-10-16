from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class ShootEventBulletNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "ShootEventBulletNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_bullettype_BulletType : Port = self.create_port("子弹类型", PortDirection.Input, PortType.BulletType)
        self.port_input_bool_AtMouse : Port = self.create_port("在鼠标处", PortDirection.Input, PortType.Bool)
        self.port_input_int_Row : Port = self.create_port("行", PortDirection.Input, PortType.Int)
        self.port_input_float_Col : Port = self.create_port("列", PortDirection.Input, PortType.Float)
        self.port_input_bool_ZombieCamp : Port = self.create_port("僵尸阵营", PortDirection.Input, PortType.Bool)
        self.port_input_int_Damage : Port = self.create_port("伤害", PortDirection.Input, PortType.Int)
        self.port_input_float_Speed : Port = self.create_port("速度", PortDirection.Input, PortType.Float)
        self.port_input_float_Angle : Port = self.create_port("角度", PortDirection.Input, PortType.Float)
        self.port_input_float_ScaleMultiplier : Port = self.create_port("大小倍率", PortDirection.Input, PortType.Float)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_bullet_Bullet : Port = self.create_port("子弹", PortDirection.Output, PortType.Bullet)


__all__ = ["ShootEventBulletNode"]
