"""
EventNodeGraph container managing nodes, connections, variables, and visual groups.
Delegates operations to NodeMgr and ConnectionMgr.
"""

from __future__ import annotations

import uuid
from typing import Any, Dict, List, Optional, Union

from .connection import Connection
from .connection_mgr import ConnectionMgr
from .group import NodeGroup
from .node_mgr import NodeMgr
from .registry import SymbolRegistry


class EventNodeGraph:
    """Manages the visual graph state for a Level via NodeMgr and ConnectionMgr."""

    def __init__(
        self,
        graph_id: Optional[str] = None,
        execution_version: int = 1,
    ):
        self.graph_id: str = graph_id or uuid.uuid4().hex
        self.execution_version: int = execution_version

        # Dedicated managers
        self.node_mgr: NodeMgr = NodeMgr()
        self.connection_mgr: ConnectionMgr = ConnectionMgr()
        self.groups: List[NodeGroup] = []

    # =========================================================================
    # COMPATIBILITY ACCESSORS
    # =========================================================================

    @property
    def nodes(self) -> List[Any]:
        return self.node_mgr.get_all_nodes()

    @property
    def connections(self) -> List[Connection]:
        return self.connection_mgr.connections

    @connections.setter
    def connections(self, new_connections: List[Connection]) -> None:
        self.connection_mgr.clear()
        for c in new_connections:
            self.connection_mgr.add_connection(c)

    @property
    def variables(self) -> List[Any]:
        return self.node_mgr.get_all_variables()

    # =========================================================================
    # DELEGATED ACTIONS
    # =========================================================================

    def add_node(self, node: Any, registry: SymbolRegistry) -> Any:
        return self.node_mgr.register_node(node, registry)

    def add_variable(self, asset: Any, registry: SymbolRegistry) -> Any:
        return self.node_mgr.register_variable(asset, registry)

    def add_group(
        self,
        group: Union[NodeGroup, Dict[str, Any]],
        registry: Optional[SymbolRegistry] = None,
    ) -> NodeGroup:
        """Registers a NodeGroup visual container and allocates a RID if needed."""
        if isinstance(group, dict):
            group = NodeGroup.from_dict(group)
        if registry is not None and hasattr(registry, "register"):
            group = registry.register(group)
        if group not in self.groups:
            self.groups.append(group)
        return group

    def connect(
        self,
        from_node: Any,
        from_port: str,
        to_node: Any,
        to_port: str,
    ) -> Connection:
        return self.connection_mgr.connect(from_node, from_port, to_node, to_port)

    # =========================================================================
    # GRAPH EXPORT
    # =========================================================================

    def to_dict(self) -> Dict[str, Any]:
        """Dumps the eventNodeGraph block using NodeMgr, ConnectionMgr, and groups."""
        groups_list: List[Dict[str, int]] = []
        for g in self.groups:
            if hasattr(g, "rid") and g.rid is not None:
                groups_list.append({"rid": g.rid})
            elif isinstance(g, dict) and "rid" in g:
                groups_list.append({"rid": g["rid"]})

        return {
            "nodes": self.node_mgr.to_nodes_list(),
            "connections": self.connection_mgr.to_list(),
            "variables": self.node_mgr.to_variables_list(),
            "groups": groups_list,
            "executionVersion": self.execution_version,
            "graphId": self.graph_id,
        }