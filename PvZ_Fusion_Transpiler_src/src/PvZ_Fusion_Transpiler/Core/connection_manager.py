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
        ConnectionManager.add_connection(self.node, self, other_port.node, other_port)
    def get_connections(self):
        return [conn for conn in ConnectionManager.get_connections() 
                if conn.source_node == self.node and conn.source_port == self or 
                conn.target_node == self.node and conn.target_port == self]

@dataclass
class Connection:
    source_node : Node
    source_port : Port
    target_node : Node
    target_port : Port

class ConnectionManager:
    """Manages connections between nodes and their ports."""
    
    connections : List[Connection] = []
    
    @staticmethod
    def add_connection(source_node : Node, source_port : Port, target_node : Node, target_port : Port) -> None:
        connection = Connection(source_node, source_port, target_node, target_port)
        ConnectionManager.connections.append(connection)

    @staticmethod
    def remove_connection(source_node : Node, source_port : Port, target_node : Node, target_port : Port) -> None:
        connection = Connection(source_node, source_port, target_node, target_port)
        if connection in ConnectionManager.connections:
            ConnectionManager.connections.remove(connection)

    @staticmethod
    def get_connections() -> List[Connection]:
        return ConnectionManager.connections

