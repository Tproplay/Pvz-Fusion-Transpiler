from __future__ import annotations

from typing import Any
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes


class Pulse:
    """Flow control node that fires its output trigger when state pulses or is active."""

    def __init__(self, state: Any) -> None:
        self.node = nodes.pulse_node(state=state)
        self._on_pulse_path = ExecutionPath(self.node.port_output_trigger_OnPulse)

    def __enter__(self) -> Pulse:
        self._on_pulse_path.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self._on_pulse_path.__exit__(exc_type, exc_val, exc_tb)

    @property
    def OnPulse(self) -> ExecutionPath:
        return self._on_pulse_path

    @property
    def on_pulse(self) -> ExecutionPath:
        return self._on_pulse_path


__all__ = ["Pulse"]
