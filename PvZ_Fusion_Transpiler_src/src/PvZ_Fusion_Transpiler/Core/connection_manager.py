from __future__ import annotations
from enum import IntEnum
from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from .._Nodes.Original.node import Node


class PortDirection(IntEnum):
    Input = 0
    Output = 1
class PortType(IntEnum):
    Trigger = 0
    Int = 1
    IntVariable = 2
    Float = 3
    FloatVariable = 4
    String = 5
    Bool = 6
    BoolVariable = 7
    Vector3 = 8
    PlantType = 9
    ZombieType = 10
    Plant = 11
    Zombie = 12
    GameObject = 13
    PlantList = 14
    ZombieList = 15
    PlantTypeList = 16
    ZombieTypeList = 17
    ChoiceOptions = 18
    StringVariable = 19
    ListVariable = 20
    Bullet = 21
    ToolType = 22
    BulletType = 23
    
    @property
    def is_trigger(self) -> bool:
        return self == PortType.Trigger

class Port:
    def __init__(self, node : Node, name : str, direction : PortDirection, port_type : PortType):
        self.node : Node = node
        self.name : str = name
        self.direction : PortDirection = direction
        self.port_type : PortType = port_type

    def connect(self, other_port : Port):
        if self.direction == other_port.direction:
            raise ValueError("Cannot connect ports with the same direction.")
        if self.port_type != other_port.port_type:
            raise ValueError("Cannot connect ports with different types.")
        if self.direction == PortDirection.Output:
            ConnectionManager.add_connection(self.node, self, other_port.node, other_port)
        else:
            ConnectionManager.add_connection(other_port.node, other_port, self.node, self)

    def get_connections(self):
        return [conn for conn in ConnectionManager.get_connections() 
                if (conn.source_node == self.node and conn.source_port == self) or 
                   (conn.target_node == self.node and conn.target_port == self)]

    def __repr__(self) -> str:
        node_name = getattr(self.node, "node_type", self.node.__class__.__name__)
        return f"<Port {node_name}.{self.name} dir={self.direction.name} type={self.port_type.name}>"

@dataclass
class Connection:
    source_node : Node
    source_port : Port
    target_node : Node
    target_port : Port

    def to_dict(self) -> dict[str, str]:
        return {
            "sourceNodeId": getattr(self.source_node, "id", str(self.source_node)),
            "sourcePortName": getattr(self.source_port, "name", str(self.source_port)),
            "targetNodeId": getattr(self.target_node, "id", str(self.target_node)),
            "targetPortName": getattr(self.target_port, "name", str(self.target_port)),
        }

    def __repr__(self) -> str:
        src_name = getattr(self.source_node, "node_type", self.source_node.__class__.__name__)
        tgt_name = getattr(self.target_node, "node_type", self.target_node.__class__.__name__)
        return f"<Connection {src_name}.{self.source_port.name} -> {tgt_name}.{self.target_port.name}>"

class ConnectionManager:
    """Manages connections between nodes and their ports."""
    
    connections : List[Connection] = []
    
    @classmethod
    def add_connection(cls, source_node : Node, source_port : Port, target_node : Node, target_port : Port) -> Connection:
        if getattr(source_port, "direction", None) == PortDirection.Input and getattr(target_port, "direction", None) == PortDirection.Output:
            source_node, source_port, target_node, target_port = target_node, target_port, source_node, source_port

        connection = Connection(source_node, source_port, target_node, target_port)
        for conn in cls.connections:
            if (conn.source_node == source_node and
                conn.source_port == source_port and
                conn.target_node == target_node and
                conn.target_port == target_port):
                return conn
        cls.connections.append(connection)
        return connection

    @classmethod
    def remove_connection(cls, source_node : Node, source_port : Port, target_node : Node, target_port : Port) -> None:
        for conn in list(cls.connections):
            if (conn.source_node == source_node and
                conn.source_port == source_port and
                conn.target_node == target_node and
                conn.target_port == target_port):
                cls.connections.remove(conn)

    @classmethod
    def get_connections(cls) -> List[Connection]:
        return cls.connections

    @classmethod
    def clear(cls) -> None:
        cls.connections.clear()


