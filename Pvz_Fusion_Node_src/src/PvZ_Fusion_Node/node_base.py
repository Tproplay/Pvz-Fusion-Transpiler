from __future__ import annotations
from typing import Any, Optional

from .Core.context import ctx, ExecutionPath
from .Nodes.Original.Node import Node, Port, to_port

BaseNode = Node


class _PortReferenceMeta(type):
    def __instancecheck__(cls, instance: Any) -> bool:
        if isinstance(instance, Port):
            return True
        if isinstance(instance, (tuple, list)) and len(instance) == 2:
            first, second = instance
            return (isinstance(first, Node) or hasattr(first, "node") or hasattr(first, "id")) and isinstance(second, str)
        return False


class PortReference(metaclass=_PortReferenceMeta):
    """Bridge for referencing a port on a node canvas."""

    def __new__(cls, node: Any, port_name: str) -> Any:
        if hasattr(node, "get_port"):
            try:
                return node.get_port(port_name)
            except Exception:
                pass
        return to_port((node, port_name))

    @staticmethod
    def _float_modulo(val: Any, mod_val: Any) -> Any:
        return Port._float_modulo(val, mod_val)
