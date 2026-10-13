"""
Connection Manager for PvZ Fusion Visual Scripting Graphs.
Provides centralized connection storage, deduplication, port validation, and export formatting.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Set, Tuple, Union

from .connection import Connection


class ConnectionMgr:
    """Central registry and manager for all wire connections in a node graph."""

    _active_instance: Optional[ConnectionMgr] = None

    def __init__(self) -> None:
        self._connections: List[Connection] = []
        self._connection_set: Set[Tuple[str, str, str, str]] = set()

        # Spatial / relational index for fast graph traversals & layout queries
        self._by_source: Dict[str, List[Connection]] = {}
        self._by_target: Dict[str, List[Connection]] = {}

    # =========================================================================
    # ACTIVE CONTEXT ACCESSORS
    # =========================================================================

    @classmethod
    def get_active(cls) -> Optional[ConnectionMgr]:
        """Returns the currently active ConnectionMgr in context, if any."""
        return cls._active_instance

    @classmethod
    def set_active(cls, mgr: Optional[ConnectionMgr]) -> None:
        """Sets the globally active ConnectionMgr."""
        cls._active_instance = mgr

    def __enter__(self) -> ConnectionMgr:
        ConnectionMgr.set_active(self)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if ConnectionMgr.get_active() is self:
            ConnectionMgr.set_active(None)

    # =========================================================================
    # CONNECTION MANAGEMENT
    # =========================================================================

    @property
    def connections(self) -> List[Connection]:
        """Returns all registered Connection instances."""
        return list(self._connections)

    def add_connection(self, connection: Connection) -> Connection:
        """Adds a pre-built Connection instance, preventing duplicates."""
        # Ignore empty dummy connections
        if not connection.sourceNodeId and not connection.targetNodeId:
            return connection

        key = (
            connection.sourceNodeId,
            connection.sourcePortName,
            connection.targetNodeId,
            connection.targetPortName,
        )
        if key not in self._connection_set:
            self._connection_set.add(key)
            self._connections.append(connection)

            self._by_source.setdefault(connection.sourceNodeId, []).append(connection)
            self._by_target.setdefault(connection.targetNodeId, []).append(connection)

        return connection

    def connect(
        self,
        from_node: Any,
        from_port: Union[str, Any],
        to_node: Any,
        to_port: Union[str, Any],
    ) -> Connection:
        """Creates, validates, and stores a connection between two nodes/ports."""
        # Resolve IDs
        from_id = getattr(from_node, "node_id", str(from_node))
        to_id = getattr(to_node, "node_id", str(to_node))

        # Resolve Port Names
        from_pname = getattr(from_port, "name", str(from_port))
        to_pname = getattr(to_port, "name", str(to_port))

        # Validate compatibility if Port objects were supplied
        if hasattr(from_port, "is_compatible_with") and hasattr(to_port, "is_compatible_with"):
            if not from_port.is_compatible_with(to_port):
                raise TypeError(
                    f"Incompatible ports: '{from_id}.{from_pname}' ({from_port.port_type.name}) "
                    f"cannot connect to '{to_id}.{to_pname}' ({to_port.port_type.name})"
                )

        conn = Connection(
            sourceNodeId=from_id,
            sourcePortName=from_pname,
            targetNodeId=to_id,
            targetPortName=to_pname,
        )
        return self.add_connection(conn)

    def get_outgoing(self, node_id: str) -> List[Connection]:
        """Returns all connections originating from the specified node."""
        return list(self._by_source.get(node_id, []))

    def get_incoming(self, node_id: str) -> List[Connection]:
        """Returns all connections targeting the specified node."""
        return list(self._by_target.get(node_id, []))

    def remove_connection(self, connection: Connection) -> bool:
        """Removes a connection if present."""
        key = (
            connection.sourceNodeId,
            connection.sourcePortName,
            connection.targetNodeId,
            connection.targetPortName,
        )
        if key in self._connection_set:
            self._connection_set.remove(key)
            self._connections.remove(connection)
            if connection.sourceNodeId in self._by_source and connection in self._by_source[connection.sourceNodeId]:
                self._by_source[connection.sourceNodeId].remove(connection)
            if connection.targetNodeId in self._by_target and connection in self._by_target[connection.targetNodeId]:
                self._by_target[connection.targetNodeId].remove(connection)
            return True
        return False

    def clear(self) -> None:
        """Clears all stored connections."""
        self._connections.clear()
        self._connection_set.clear()
        self._by_source.clear()
        self._by_target.clear()

    # =========================================================================
    # EXPORT SERIALIZATION
    # =========================================================================

    def to_list(self) -> List[Dict[str, str]]:
        """Serializes connections into the eventNodeGraph.connections JSON array.
        
        Unity's EventNodeGraph requires an initial empty dummy entry at index 0:
        {"sourceNodeId": "", "sourcePortName": "", "targetNodeId": "", "targetPortName": ""}
        """
        dummy = {
            "sourceNodeId": "",
            "sourcePortName": "",
            "targetNodeId": "",
            "targetPortName": "",
        }
        return [dummy] + [c.to_dict() for c in self._connections]

    def __len__(self) -> int:
        return len(self._connections)

    def __repr__(self) -> str:
        return f"<ConnectionMgr total_connections={len(self._connections)}>"