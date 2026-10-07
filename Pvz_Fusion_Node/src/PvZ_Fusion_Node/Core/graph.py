"""
EventNodeGraph container managing nodes, connections, and variables.
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional
import uuid

try:
    from .connection import Connection
    from .registry import SymbolRegistry
except (ImportError, ValueError):
    from connection import Connection
    from registry import SymbolRegistry


class EventNodeGraph:
    def __init__(
        self,
        graph_id: Optional[str] = None,
        execution_version: int = 1,
    ):
        self.graph_id: str = graph_id or uuid.uuid4().hex
        self.execution_version: int = execution_version
        self.nodes: List[Any] = []
        self.connections: List[Connection] = []
        self.variables: List[Any] = []
        self.groups: List[Any] = []

    def add_node(self, node: Any, registry: SymbolRegistry) -> Any:
        # Unpack composite extension nodes
        if hasattr(node, "nodes"):
            for inner in node.nodes:
                self.add_node(inner, registry)
            if hasattr(node, "asset") and node.asset:
                self.add_variable(node.asset, registry)
            return node

        registered = registry.register(node)
        if registered not in self.nodes:
            self.nodes.append(registered)
        return registered

    def add_variable(self, asset: Any, registry: SymbolRegistry) -> Any:
        registered = registry.register(asset)
        if registered not in self.variables:
            self.variables.append(registered)
        return registered

    def connect(self, from_node: Any, from_port: str, to_node: Any, to_port: str) -> Connection:
        c = Connection(
            fromNodeId=from_node.node_id,
            fromPortName=from_port,
            toNodeId=to_node.node_id,
            toPortName=to_port,
        )
        if c not in self.connections:
            self.connections.append(c)
        return c

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nodes": [{"rid": n.rid} for n in self.nodes if getattr(n, "rid", None) is not None],
            "connections": [c.to_dict() for c in self.connections],
            "variables": [{"rid": v.rid} for v in self.variables if getattr(v, "rid", None) is not None],
            "groups": list(self.groups),
            "executionVersion": self.execution_version,
            "graphId": self.graph_id,
        }
