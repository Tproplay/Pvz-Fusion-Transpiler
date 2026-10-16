from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetToolCooldownNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "GetToolCooldownNode"

    def __init__(self):
        super().__init__()
        self.port_input_tooltype_ToolType : Port = self.create_port("类型", PortDirection.Input, PortType.ToolType)
        self.port_output_float_TotalSeconds : Port = self.create_port("总秒数", PortDirection.Output, PortType.Float)
        self.port_output_float_RemainingSeconds : Port = self.create_port("剩余秒数", PortDirection.Output, PortType.Float)
        self.port_output_bool_Exists : Port = self.create_port("存在", PortDirection.Output, PortType.Bool)


__all__ = ["GetToolCooldownNode"]
