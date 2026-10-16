from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from ...Core import uuid
from ...Core.connection_manager import PortDirection, PortType, Port


class Node(ABC):
    
    def __init__(self):
        self.id = str(uuid.generate_uuid())
    
    def create_port(self, name : str, direction : PortDirection, port_type : PortType) -> Port:
        return Port(self, name, direction, port_type)


class EventNodeBase(Node):
    """Abstract base class for legacy EventNodeBase nodes."""
    pass


class EventSuggestedNode(Node):
    """Abstract base class for modern EventSuggestedNode nodes."""
    pass
    

