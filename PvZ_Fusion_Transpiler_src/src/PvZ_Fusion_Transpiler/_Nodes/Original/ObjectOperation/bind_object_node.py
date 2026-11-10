from ..node import Node, EventNodeBase, EventSuggestedNode, PortDirection, PortType, Port


class BindObjectNode(EventSuggestedNode):
    # Status in Extensions: Implemented
    node_type = "BindObjectNode"

    def __init__(self):
        super().__init__()
        self.port_input_trigger_Trigger : Port = self.create_port("Trigger", PortDirection.Input, PortType.Trigger)
        self.port_input_string_Name : Port = self.create_port("Name", PortDirection.Input, PortType.String)
        self.port_input_gameobject_GameObject : Port = self.create_port("Object", PortDirection.Input, PortType.GameObject)
        self.port_output_trigger_Complete : Port = self.create_port("On Complete", PortDirection.Output, PortType.Trigger)
        self.port_output_trigger_Failed : Port = self.create_port("Game Over", PortDirection.Output, PortType.Trigger)


__all__ = ["BindObjectNode"]
