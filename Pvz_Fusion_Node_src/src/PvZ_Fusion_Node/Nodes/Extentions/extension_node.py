"""
Abstract universal base class for all composite extensions in PvzRH visual scripts.
Provides underlying Node/VariableAsset lifecycle management, sub-node registration,
primary port resolution, operator overloading, and fluent trigger wiring (>>).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union

from ..Original.Node import Node, Port, to_port


class ExtensionNode(ABC):
    """Abstract base class for all composite extensions and wrappers.
    
    Manages internal low-level Node instances, delegating primary ports,
    arithmetic/comparison operators, flow-control wiring, and context manager scopes.
    """

    def __init__(self, root_node: Optional[Node] = None) -> None:
        self._nodes: List[Node] = []
        if root_node is not None:
            self._nodes.append(root_node)

    # =========================================================================
    # COMPOSITION & NODE MANAGEMENT
    # =========================================================================

    @property
    def nodes(self) -> List[Node]:
        """Returns all underlying low-level Node instances managed by this composite."""
        return list(self._nodes)

    def attach_node(self, node: Node) -> Node:
        """Registers an additional internal node into this composite's graph."""
        if node not in self._nodes:
            self._nodes.append(node)
        return node

    @property
    def root_node(self) -> Optional[Node]:
        """Returns the primary or root node of this composite."""
        if self._nodes:
            return self._nodes[0]
        if hasattr(self, "_node") and isinstance(self._node, Node):
            return self._node
        if hasattr(self, "node") and isinstance(self.node, Node):
            return self.node
        return None

    @property
    def id(self) -> str:
        """Returns the node id of the root node or a unique identifier."""
        if hasattr(self, "_custom_node_id") and self._custom_node_id:
            return self._custom_node_id
        root = self.root_node
        if root is not None:
            return root.id
        return str(id(self))

    @id.setter
    def id(self, value: str) -> None:
        self._custom_node_id = str(value)

    @property
    def node_id(self) -> str:
        return self.id

    @node_id.setter
    def node_id(self, value: str) -> None:
        self.id = str(value)

    # =========================================================================
    # PRIMARY PORT & DELEGATION
    # =========================================================================

    def get_primary_port(self) -> Optional[Port]:
        """Returns the primary data or flow port representing this extension.
        Subclasses can override to expose their primary data/trigger port.
        """
        if hasattr(self, "_primary_port") and self._primary_port is not None:
            return to_port(self._primary_port)
        root = self.root_node
        if root is not None and hasattr(root, "port"):
            try:
                return root.port
            except Exception:
                pass
        return None

    @property
    def primary_port(self) -> Optional[Port]:
        return self.get_primary_port()

    @property
    def port(self) -> Optional[Port]:
        return self.get_primary_port()

    def _get_primary_port(self) -> Optional[Port]:
        """Helper for to_port() coercion."""
        return self.get_primary_port()

    def get_port(self, name: str) -> Port:
        """Retrieves a bound Port object from the root node."""
        root = self.root_node
        if root is not None:
            return root.get_port(name)
        raise AttributeError(f"Extension '{self.__class__.__name__}' has no root node to retrieve port '{name}'")

    def get_input(self, name: str) -> Port:
        """Retrieves a bound input Port object from the root node."""
        root = self.root_node
        if root is not None:
            return root.get_input(name)
        raise AttributeError(f"Extension '{self.__class__.__name__}' has no root node to retrieve input port '{name}'")

    def get_output(self, name: str) -> Port:
        """Retrieves a bound output Port object from the root node."""
        root = self.root_node
        if root is not None:
            return root.get_output(name)
        raise AttributeError(f"Extension '{self.__class__.__name__}' has no root node to retrieve output port '{name}'")

    # =========================================================================
    # EXECUTION PATHS & TRIGGER FLOW
    # =========================================================================

    @property
    def Output(self) -> Any:
        """Exposes execution paths on this extension's root node."""
        if hasattr(self, "_output_accessor") and self._output_accessor is not None:
            return self._output_accessor
        root = self.root_node
        if root is not None:
            return root.Output
        from ...Core.context import PathAccessor
        return PathAccessor(self)

    @Output.setter
    def Output(self, value: Any) -> None:
        self._output_accessor = value

    def path(self, trigger_name: str) -> Any:
        """Returns an ExecutionPath targeting the specified output trigger port."""
        root = self.root_node
        if root is not None:
            return root.path(trigger_name)
        from ...Core.context import ExecutionPath
        return ExecutionPath(self.id, trigger_name)

    @staticmethod
    def resolve_port(target: Any) -> Optional[Port]:
        """Extracts the underlying low-level Port from an ExtensionNode or wrapped object."""
        if isinstance(target, Port):
            return target
        if isinstance(target, ExtensionNode):
            return target.get_primary_port()
        if hasattr(target, "get_primary_port") and callable(target.get_primary_port):
            return target.get_primary_port()
        if hasattr(target, "primary_port"):
            return target.primary_port
        if hasattr(target, "port"):
            return target.port
        if hasattr(target, "_get_primary_port"):
            p = target._get_primary_port() if callable(target._get_primary_port) else target._get_primary_port
            if p is not None:
                return to_port(p)
        return None

    def connect(self, target: Any, source_port_name: Optional[str] = None) -> Any:
        """Connects this extension's primary output port (or named port) to a target."""
        if source_port_name:
            src = self.get_output(source_port_name)
        else:
            src = self.get_primary_port()

        dst = to_port(target) if not isinstance(target, Port) else target
        if src is not None and dst is not None:
            src.connect(dst)
        return target

    def __rshift__(self, target: Any) -> Any:
        """Chains execution flow or data connection from this extension: ext >> target."""
        return self.connect(target)

    # =========================================================================
    # CONTEXT MANAGER SUPPORT
    # =========================================================================

    def __enter__(self) -> Any:
        root = self.root_node
        if root is not None and hasattr(root, "__enter__"):
            return root.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        root = self.root_node
        if root is not None and hasattr(root, "__exit__"):
            root.__exit__(exc_type, exc_val, exc_tb)

    # =========================================================================
    # ARITHMETIC & COMPARISON OPERATORS (DELEGATED TO PRIMARY PORT)
    # =========================================================================

    def _require_port(self) -> Port:
        p = self.get_primary_port()
        if p is None:
            raise TypeError(f"Extension '{self.__class__.__name__}' does not expose a primary data Port for operations.")
        return p

    def __add__(self, other: Any) -> Port:
        return self._require_port() + other

    def __radd__(self, other: Any) -> Port:
        return to_port(other) + self._require_port()

    def __sub__(self, other: Any) -> Port:
        return self._require_port() - other

    def __rsub__(self, other: Any) -> Port:
        return to_port(other) - self._require_port()

    def __mul__(self, other: Any) -> Port:
        return self._require_port() * other

    def __rmul__(self, other: Any) -> Port:
        return to_port(other) * self._require_port()

    def __truediv__(self, other: Any) -> Port:
        return self._require_port() / other

    def __rtruediv__(self, other: Any) -> Port:
        return to_port(other) / self._require_port()

    def __floordiv__(self, other: Any) -> Port:
        return self._require_port() // other

    def __rfloordiv__(self, other: Any) -> Port:
        return to_port(other) // self._require_port()

    def __mod__(self, other: Any) -> Port:
        return self._require_port() % other

    def __rmod__(self, other: Any) -> Port:
        return to_port(other) % self._require_port()

    def __eq__(self, other: Any) -> Any:
        p = self.get_primary_port()
        if p is not None:
            return p == other
        return super().__eq__(other)

    def __ne__(self, other: Any) -> Any:
        p = self.get_primary_port()
        if p is not None:
            return p != other
        return super().__ne__(other)

    def __lt__(self, other: Any) -> Port:
        return self._require_port() < other

    def __le__(self, other: Any) -> Port:
        return self._require_port() <= other

    def __gt__(self, other: Any) -> Port:
        return self._require_port() > other

    def __ge__(self, other: Any) -> Port:
        return self._require_port() >= other

    def __and__(self, other: Any) -> Port:
        return self._require_port() & other

    def __rand__(self, other: Any) -> Port:
        return to_port(other) & self._require_port()

    def __or__(self, other: Any) -> Port:
        return self._require_port() | other

    def __ror__(self, other: Any) -> Port:
        return to_port(other) | self._require_port()

    def __neg__(self) -> Port:
        return -self._require_port()

    def __repr__(self) -> str:
        primary = self.primary_port
        port_info = f" primary_port={primary.name}" if primary else ""
        return f"<{self.__class__.__name__} [{len(self._nodes)} inner nodes]{port_info}>"