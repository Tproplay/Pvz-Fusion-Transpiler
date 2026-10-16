from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class GetStageNode(EventNodeBase):
    # Status in Extensions: Not implemented
    node_type = "GetStageNode"

    def __init__(self):
        super().__init__()
        self.port_output_string_StageName : Port = self.create_port("阶段名", PortDirection.Output, PortType.String)


__all__ = ["GetStageNode"]
