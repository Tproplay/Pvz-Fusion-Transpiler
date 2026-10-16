from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class OnMouseClickNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "OnMouseClickNode"

    def __init__(self):
        super().__init__()
        self.port_output_trigger_Trigger : Port = self.create_port("触发", PortDirection.Output, PortType.Trigger)
        self.port_output_int_Row : Port = self.create_port("行", PortDirection.Output, PortType.Int)
        self.port_output_int_Col : Port = self.create_port("列", PortDirection.Output, PortType.Int)
        self.port_output_tooltype_HeldItem : Port = self.create_port("手上的物品", PortDirection.Output, PortType.ToolType)
        self.port_output_bool_IsLeftButton : Port = self.create_port("是左键", PortDirection.Output, PortType.Bool)


__all__ = ["OnMouseClickNode"]
