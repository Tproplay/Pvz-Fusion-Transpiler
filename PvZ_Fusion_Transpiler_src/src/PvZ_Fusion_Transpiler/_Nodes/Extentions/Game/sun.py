from __future__ import annotations

from typing import Any
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes


class _SunManager:
    """Get/Set the board Sun value."""

    @property
    def value(self) -> Any:
        return nodes.get_sun_amount().port_output_int_SunAmount

    def _get_primary_port(self) -> Any:
        return self.value

    class SpendSun:
        """Context Manager for spending sun safely."""

        def __init__(self, amount: Any) -> None:
            self.node = nodes.use_sun(amount=amount)
            self._path = ExecutionPath(self.node.port_output_trigger_OnSuccess)

        def __enter__(self) -> _SunManager.SpendSun:
            self._path.__enter__()
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            self._path.__exit__(exc_type, exc_val, exc_tb)

        @property
        def Failed(self) -> ExecutionPath:
            return ExecutionPath(self.node.port_output_trigger_OnFailed)

        @property
        def failed(self) -> ExecutionPath:
            return self.Failed

    def __add__(self, other: Any) -> Any:
        return self.value + other

    def __radd__(self, other: Any) -> Any:
        return self.value.__radd__(other)

    def __sub__(self, other: Any) -> Any:
        return self.value - other

    def __rsub__(self, other: Any) -> Any:
        return self.value.__rsub__(other)

    def __mul__(self, other: Any) -> Any:
        return self.value * other

    def __rmul__(self, other: Any) -> Any:
        return self.value.__rmul__(other)

    def __truediv__(self, other: Any) -> Any:
        return self.value / other

    def __rtruediv__(self, other: Any) -> Any:
        return self.value.__rtruediv__(other)

    def __floordiv__(self, other: Any) -> Any:
        return self.value // other

    def __mod__(self, other: Any) -> Any:
        return self.value % other

    def __eq__(self, other: Any) -> Any:
        return self.value == other

    def __ne__(self, other: Any) -> Any:
        return self.value != other

    def __lt__(self, other: Any) -> Any:
        return self.value < other

    def __le__(self, other: Any) -> Any:
        return self.value <= other

    def __gt__(self, other: Any) -> Any:
        return self.value > other

    def __ge__(self, other: Any) -> Any:
        return self.value >= other

    def set(self, target_value: Any) -> _SunManager:
        """Set the Board Sun value."""
        from ..Branching.branching import If
        diff = target_value - self.value
        with If(diff > 0) as flow:
            nodes.add_sun(amount=diff)
        with flow.Elif(diff < 0):
            abs_diff = diff * -1
            use_node = nodes.use_sun(amount=abs_diff)
            _ctx.trigger_stack[-1] = ExecutionPath(use_node.port_output_trigger_OnSuccess)
        return self

    def get(self) -> Any:
        """Get the Board Sun value."""
        return self.value

    def __iadd__(self, other: Any) -> _SunManager:
        nodes.add_sun(amount=other)
        return self

    def __isub__(self, other: Any) -> _SunManager:
        use_node = nodes.use_sun(amount=other)
        _ctx.trigger_stack[-1] = ExecutionPath(use_node.port_output_trigger_OnSuccess)
        return self

    def __imul__(self, other: Any) -> _SunManager:
        self.set(self.value * other)
        return self

    def __itruediv__(self, other: Any) -> _SunManager:
        self.set(self.value / other)
        return self

    def __ifloordiv__(self, other: Any) -> _SunManager:
        self.set(self.value // other)
        return self

    def __imod__(self, other: Any) -> _SunManager:
        self.set(self.value % other)
        return self


__all__ = ["_SunManager"]
