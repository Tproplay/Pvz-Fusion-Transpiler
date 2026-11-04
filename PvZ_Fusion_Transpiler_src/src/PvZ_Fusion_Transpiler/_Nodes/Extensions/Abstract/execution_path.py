from __future__ import annotations

from typing import Any
from ....Core.context import _ctx
from ....Core.connection_manager import PortDirection, PortType


class ExecutionPath:
    """Represents an active outgoing execution pin on a node for block scoping."""

    def __init__(self, node_or_id_or_port: Any, out_trigger: Any = None):
        if out_trigger is None:
            # Single argument: should be a Port or object with .node and .name
            if hasattr(node_or_id_or_port, "node") and hasattr(node_or_id_or_port, "name"):
                self.id: str = getattr(node_or_id_or_port.node, "id", str(node_or_id_or_port.node))
                self.out_trigger: str = str(node_or_id_or_port.name)
            else:
                raise ValueError("Single argument to ExecutionPath must be a Port with .node and .name attributes")
        else:
            self.id = getattr(node_or_id_or_port, "id", str(node_or_id_or_port))
            if hasattr(out_trigger, "name"):
                self.out_trigger = str(out_trigger.name)
            else:
                self.out_trigger = str(out_trigger)

    def __enter__(self) -> ExecutionPath:
        _ctx.trigger_stack.append(self)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if _ctx.trigger_stack and _ctx.trigger_stack[-1] is self:
            _ctx.trigger_stack.pop()

    def __repr__(self) -> str:
        return f"<ExecutionPath id={self.id[:8]} trigger={self.out_trigger}>"


class PathAccessor:
    """Exposes node trigger outputs as friendly camelCase / TitleCase attributes."""

    def __init__(self, node: Any):
        self._node = node

    def __getattr__(self, name: str) -> ExecutionPath:
        # Check explicit port attribute on node: e.g. port_output_trigger_OnSuccess
        norm = name.lower().replace("_", "")
        for attr in dir(self._node):
            if attr.startswith("port_output_trigger_"):
                parts = attr.split("_")
                if len(parts) >= 4 and parts[3].lower().replace("_", "") == norm:
                    port = getattr(self._node, attr)
                    return ExecutionPath(port)

        for port in getattr(self._node, "ports", []):
            if port.direction == PortDirection.Output and port.port_type == PortType.Trigger:
                if port.name == name or port.name.lower() == name.lower():
                    return ExecutionPath(port)

        # Fallback to get_output
        if hasattr(self._node, "get_output"):
            try:
                p = self._node.get_output(name)
                if p.port_type == PortType.Trigger:
                    return ExecutionPath(p)
            except Exception:
                pass

        return ExecutionPath(self._node.id, name)


__all__ = ["ExecutionPath", "PathAccessor"]
