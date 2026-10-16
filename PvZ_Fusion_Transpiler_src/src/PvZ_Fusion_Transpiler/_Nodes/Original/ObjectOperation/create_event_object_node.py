from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class CreateEventObjectNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "CreateEventObjectNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("触发", PortDirection.Input, PortType.Trigger)
        self.port_input_string_Name : Port = self.create_port("名称", PortDirection.Input, PortType.String)
        self.port_input_vector3_Position : Port = self.create_port("位置", PortDirection.Input, PortType.Vector3)
        self.port_input_planttype_IconPlant : Port = self.create_port("图标植物", PortDirection.Input, PortType.PlantType)
        self.port_output_trigger_Complete : Port = self.create_port("完成", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("失败", PortDirection.Output, PortType.Trigger)
        self.port_output_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Output, PortType.GameObject)


__all__ = ["CreateEventObjectNode"]
