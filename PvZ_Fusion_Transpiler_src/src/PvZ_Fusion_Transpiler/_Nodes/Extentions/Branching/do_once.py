from __future__ import annotations

from typing import Any
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes


class DoOnce:
    """Flow control that executes its body only on the first pass until reset."""

    def __init__(self) -> None:
        self.node = nodes.do_once()

    def __enter__(self) -> DoOnce:
        _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if _ctx.trigger_stack and _ctx.trigger_stack[-1].id == self.node.id:
            _ctx.trigger_stack.pop()

    def Reset(self) -> None:
        """Triggers the reset input port of the DoOnce node."""
        if _ctx.trigger_stack:
            prev = _ctx.trigger_stack[-1]
            prev_id = getattr(prev, "id", str(prev))
            prev_trig = getattr(prev, "out_trigger", "触发")
            _ctx.add_connection(prev_id, prev_trig, self.node.id, self.node.port_input_trigger_Reset.name)

    reset = Reset


__all__ = ["DoOnce"]
