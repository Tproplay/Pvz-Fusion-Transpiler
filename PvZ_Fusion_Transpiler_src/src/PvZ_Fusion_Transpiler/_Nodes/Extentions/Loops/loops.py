from __future__ import annotations

from typing import Any
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....typing import to_int_port


class While:
    """A continuous execution loop that runs as long as a condition evaluates to True.

    Creates a cyclic branch node in the execution graph that repeatedly triggers its 
    own input until the provided condition port evaluates to False.

    Example:
        ```python
        with While(pvn.Board.Sun < 500):
            ...
        ```
    """

    def __init__(self, condition: Any) -> None:
        self.branch = nodes.branch_node(condition=condition)

    def __enter__(self) -> While:
        _ctx.trigger_stack.append(ExecutionPath(self.branch.port_output_trigger_Then))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        _ctx.add_connection(
            self.branch.id,
            self.branch.port_output_trigger_Then.name,
            self.branch.id,
            self.branch.port_input_trigger_Trigger.name,
        )
        _ctx.trigger_stack.pop()


class For:
    """A fixed-count loop structure that executes a block a specified number of times.
    
    Yields a context object that dynamically exposes the current loop iteration index.

    Example:
        ```python
        with For(10) as loop:
            ...
        ```
    """

    def __init__(self, count: int | Any) -> None:
        int_count = to_int_port(count)
        self.loop_node = nodes.for_loop_node(count=int_count)

    def __enter__(self) -> For:
        _ctx.trigger_stack.append(ExecutionPath(self.loop_node.port_output_trigger_LoopBody))
        return self

    @property
    def index(self) -> Any:
        return self.loop_node.port_output_int_Index

    def _get_primary_port(self) -> Any:
        return self.index

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        _ctx.trigger_stack.pop()


__all__ = ["While", "For"]
