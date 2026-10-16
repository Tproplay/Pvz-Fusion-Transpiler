from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class AddZombieCardNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "AddZombieCardNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_zombietype_ZombieType : Port = self.create_port("僵尸类型", PortDirection.Input, PortType.ZombieType)
        self.port_input_int_Price : Port = self.create_port("价格", PortDirection.Input, PortType.Int)
        self.port_input_float_Cooldown : Port = self.create_port("冷却秒数", PortDirection.Input, PortType.Float)
        self.port_input_bool_AvailableImmediately : Port = self.create_port("立即可用", PortDirection.Input, PortType.Bool)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_gameobject_CardObject : Port = self.create_port("卡牌对象", PortDirection.Output, PortType.GameObject)


__all__ = ["AddZombieCardNode"]
