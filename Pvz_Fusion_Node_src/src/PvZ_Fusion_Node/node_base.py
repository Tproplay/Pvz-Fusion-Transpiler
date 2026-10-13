from __future__ import annotations
from typing import Any, Optional

from .Core.context import ctx, ExecutionPath
from .Nodes.Original.Node import Node, Port, to_port

BaseNode = Node


class _PortReferenceMeta(type):
    def __instancecheck__(cls, instance: Any) -> bool:
        return isinstance(instance, Port) or (isinstance(instance, (tuple, list)) and len(instance) == 2)


class PortReference(metaclass=_PortReferenceMeta):
    """Bridge for referencing a port on a node canvas."""

    def __new__(cls, node: Any, port_name: str) -> Any:
        if hasattr(node, "get_port"):
            try:
                return node.get_port(port_name)
            except Exception:
                pass
        return to_port((node, port_name))
