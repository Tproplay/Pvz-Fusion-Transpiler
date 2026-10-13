"""
Node Manager for PvZ Fusion Visual Scripting Graphs.
Handles registration, composite unpacking, variable asset isolation, and graph export lists.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


class NodeMgr:
    """Central registry and manager for all Nodes and VariableAssets in a graph."""

    _active_instance: Optional[NodeMgr] = None

    def __init__(self) -> None:
        self._nodes: Dict[str, Any] = {}
        self._node_order: List[str] = []
        self._nodes_by_type: Dict[str, List[Any]] = {}

        self._variables: Dict[str, Any] = {}
        self._variable_order: List[str] = []

    # =========================================================================
    # ACTIVE CONTEXT ACCESSORS
    # =========================================================================

    @classmethod
    def get_active(cls) -> Optional[NodeMgr]:
        """Returns the currently active NodeMgr in context, if any."""
        return cls._active_instance

    @classmethod
    def set_active(cls, mgr: Optional[NodeMgr]) -> None:
        """Sets the globally active NodeMgr."""
        cls._active_instance = mgr

    def __enter__(self) -> NodeMgr:
        NodeMgr.set_active(self)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if NodeMgr.get_active() is self:
            NodeMgr.set_active(None)

    # =========================================================================
    # NODE REGISTRATION & COMPOSITION
    # =========================================================================

    def register_node(self, node: Any, registry: Optional[Any] = None) -> Any:
        """Registers a low-level node or composite extension into the manager.
        
        Recursively unpacks composite extension nodes (.nodes) and registers
        attached variable assets (.asset).
        """
        # Composite / ExtensionNode unpacking
        if hasattr(node, "nodes") and isinstance(node.nodes, (list, tuple)):
            for inner in node.nodes:
                self.register_node(inner, registry)
            if hasattr(node, "asset") and node.asset:
                self.register_variable(node.asset, registry)
            return node

        # Assign deterministic RID if a SymbolRegistry was provided
        if registry is not None and hasattr(registry, "register"):
            node = registry.register(node)

        # Register variable asset if this node holds one
        if hasattr(node, "asset") and node.asset:
            self.register_variable(node.asset, registry)

        node_id = getattr(node, "node_id", None)
        if not node_id:
            raise AttributeError(f"Registered node of type {type(node).__name__} lacks a 'node_id'.")

        if node_id not in self._nodes:
            self._nodes[node_id] = node
            self._node_order.append(node_id)

            ntype = getattr(node, "node_type", type(node).__name__)
            self._nodes_by_type.setdefault(ntype, []).append(node)

        return node

    def register_variable(self, asset: Any, registry: Optional[Any] = None) -> Any:
        """Registers a persistent canvas variable asset."""
        if registry is not None and hasattr(registry, "register"):
            asset = registry.register(asset)

        var_id = getattr(asset, "variable_id", str(id(asset)))
        if var_id not in self._variables:
            self._variables[var_id] = asset
            self._variable_order.append(var_id)

        return asset

    # =========================================================================
    # QUERY & RETRIEVAL
    # =========================================================================

    def get_node(self, node_id: str) -> Optional[Any]:
        """Retrieves a node by its unique node_id."""
        return self._nodes.get(node_id)

    def has_node(self, node_id: str) -> bool:
        """Checks if a node is currently registered."""
        return node_id in self._nodes

    def get_all_nodes(self) -> List[Any]:
        """Returns all registered nodes in insertion order."""
        return [self._nodes[nid] for nid in self._node_order]

    def get_all_variables(self) -> List[Any]:
        """Returns all registered variable assets in insertion order."""
        return [self._variables[vid] for vid in self._variable_order]

    def get_nodes_by_type(self, node_type: str) -> List[Any]:
        """Finds all nodes matching the given node_type string."""
        return list(self._nodes_by_type.get(node_type, []))

    def remove_node(self, node_id: str) -> Optional[Any]:
        """Removes and returns a node by ID."""
        if node_id in self._nodes:
            node = self._nodes.pop(node_id)
            self._node_order.remove(node_id)
            ntype = getattr(node, "node_type", type(node).__name__)
            if ntype in self._nodes_by_type and node in self._nodes_by_type[ntype]:
                self._nodes_by_type[ntype].remove(node)
            return node
        return None

    def clear(self) -> None:
        """Clears all stored nodes and variables."""
        self._nodes.clear()
        self._node_order.clear()
        self._nodes_by_type.clear()
        self._variables.clear()
        self._variable_order.clear()

    # =========================================================================
    # EXPORT SERIALIZATION
    # =========================================================================

    def to_nodes_list(self) -> List[Dict[str, int]]:
        """Serializes the compact node reference list for eventNodeGraph.nodes."""
        return [
            {"rid": n.rid}
            for n in self.get_all_nodes()
            if getattr(n, "rid", None) is not None
        ]

    def to_variables_list(self) -> List[Dict[str, int]]:
        """Serializes the compact variable reference list for eventNodeGraph.variables."""
        return [
            {"rid": v.rid}
            for v in self.get_all_variables()
            if getattr(v, "rid", None) is not None
        ]

    def __len__(self) -> int:
        return len(self._nodes)

    def __repr__(self) -> str:
        return f"<NodeMgr total_nodes={len(self._nodes)} total_vars={len(self._variables)}>"