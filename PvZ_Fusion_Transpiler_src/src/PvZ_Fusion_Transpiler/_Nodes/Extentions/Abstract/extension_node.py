from __future__ import annotations

from abc import ABC
from typing import Any, List, Optional, Union
from ....Core.connection_manager import Port
from ...Original.node import Node
from ....typing import to_port


class ExtensionNode(ABC):
    """Abstract base class for all composite extensions and wrappers."""

    def __init__(self, root_node: Optional[Node] = None) -> None:
        self._nodes: List[Node] = []
        if root_node is not None:
            self._nodes.append(root_node)

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
        n1 = getattr(self, "_node", None)
        if isinstance(n1, Node):
            return n1
        n2 = getattr(self, "node", None)
        if isinstance(n2, Node):
            return n2
        return None

    @property
    def id(self) -> str:
        """Returns the node id of the root node or a unique identifier."""
        custom_id = getattr(self, "_custom_node_id", None)
        if custom_id:
            return custom_id
        root = self.root_node
        if root is not None:
            return root.id
        return str(id(self))

    @id.setter
    def id(self, value: str) -> None:
        self._custom_node_id = str(value)

    def get_primary_port(self) -> Optional[Port]:
        """Returns the primary data or flow port representing this extension."""
        primary = getattr(self, "_primary_port", None)
        if primary is not None:
            return to_port(primary)
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
        return self.get_primary_port()

    def get_port(self, name: str) -> Port:
        root = self.root_node
        if root is not None:
            return root.get_port(name)
        raise AttributeError(f"Extension '{self.__class__.__name__}' has no root node to retrieve port '{name}'")

    def get_input(self, name: str) -> Port:
        root = self.root_node
        if root is not None:
            return root.get_input(name)
        raise AttributeError(f"Extension '{self.__class__.__name__}' has no root node to retrieve input port '{name}'")

    def get_output(self, name: str) -> Port:
        root = self.root_node
        if root is not None:
            return root.get_output(name)
        raise AttributeError(f"Extension '{self.__class__.__name__}' has no root node to retrieve output port '{name}'")

    @property
    def Output(self) -> Any:
        root = self.root_node
        if root is not None:
            return root.Output
        from .execution_path import PathAccessor
        return PathAccessor(self)

    def path(self, trigger_name: str) -> Any:
        root = self.root_node
        if root is not None:
            return root.path(trigger_name)
        from .execution_path import ExecutionPath
        return ExecutionPath(self.id, trigger_name)

    def connect(self, target: Any, source_port_name: Optional[str] = None) -> Any:
        if source_port_name:
            src = self.get_output(source_port_name)
        else:
            src = self.get_primary_port()

        dst = to_port(target) if not isinstance(target, Port) else target
        if src is not None and dst is not None:
            src.connect(dst)
        return target

    def __rshift__(self, target: Any) -> Any:
        return self.connect(target)

    def __enter__(self) -> Any:
        root = self.root_node
        if root is not None and hasattr(root, "__enter__"):
            return root.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        root = self.root_node
        if root is not None and hasattr(root, "__exit__"):
            root.__exit__(exc_type, exc_val, exc_tb)

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


__all__ = ["ExtensionNode"]
