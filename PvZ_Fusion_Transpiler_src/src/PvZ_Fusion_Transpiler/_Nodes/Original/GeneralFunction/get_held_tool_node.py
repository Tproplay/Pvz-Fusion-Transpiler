from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetHeldToolNode(EventSuggestedNode):
    # Status in Extensions: Not implemented
    node_type = "GetHeldToolNode"

    def __init__(self):
        super().__init__()
        self.port_output_gameobject_GameObject : Port = self.create_port("对象", PortDirection.Output, PortType.GameObject)
        self.port_output_tooltype_ToolType : Port = self.create_port("类型", PortDirection.Output, PortType.ToolType)


__all__ = ["GetHeldToolNode"]
