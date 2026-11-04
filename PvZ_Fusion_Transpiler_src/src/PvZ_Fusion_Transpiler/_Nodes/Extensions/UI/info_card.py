from __future__ import annotations

from typing import Any, Callable, Optional
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes


class InfoCard:
    """High-level manager for CreateInfoCardNode.

    Supports callbacks, context managers, decorators, and trigger outputs.
    """

    def __init__(
        self,
        big_title: Any,
        small_title: Any,
        callback: Optional[Callable[[], None]] = None,
    ) -> None:
        self.big_title = big_title
        self.small_title = small_title
        self.callback = callback

        self.node = nodes.create_info_card(
            big_title=self.big_title,
            small_title=self.small_title,
        )
        self.node_id = self.node.id
        self.Output = self._Outputs(self)

        if self.callback:
            self._compile_callback(self.callback)

    def _compile_callback(self, func: Callable[[], None]) -> None:
        """Isolates and compiles the click execution path graph."""
        saved_stack = _ctx.trigger_stack[:]
        _ctx.trigger_stack.clear()
        _ctx.trigger_stack.append(self.Output.OnCardClicked)
        try:
            func()
        finally:
            _ctx.trigger_stack.clear()
            _ctx.trigger_stack.extend(saved_stack)

    def on_click(self, func: Callable[[], None]) -> Callable[[], None]:
        """Decorator syntax for handling card click events."""
        self._compile_callback(func)
        return func

    def __enter__(self) -> InfoCard:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass

    class _Outputs:
        """Execution paths for the card events."""

        def __init__(self, parent: InfoCard) -> None:
            self._parent = parent

        @property
        def OnCardClicked(self) -> ExecutionPath:
            """Triggered when the player clicks this card."""
            return ExecutionPath(self._parent.node.port_output_trigger_OnCardClicked)

        @property
        def on_card_clicked(self) -> ExecutionPath:
            return self.OnCardClicked


__all__ = ["InfoCard"]
