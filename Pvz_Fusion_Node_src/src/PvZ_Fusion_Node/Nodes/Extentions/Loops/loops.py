from __future__ import annotations
from typing import Any
from ..extension_node import ExtensionNode
from .... import nodes
from ....Core.context import ctx, ExecutionPath
from ...Original.Node import Port, to_port
from ....typing import to_int_port


class While(ExtensionNode):
    """A continuous execution loop that runs as long as a condition evaluates to True.

    Creates a cyclic branch node in the execution graph that repeatedly triggers its 
    own input until the provided condition port evaluates to False.

    Args:
        condition (Any): A boolean expression, variable, or condition port to evaluate.

    Example:
        ```python
        with pvn.While(pvn.Board.Sun < 500):
            ...
        ```
    """

    def __init__(self, condition: Any) -> None:
        self.branch = nodes.branch_node(condition=condition)
        super().__init__(root_node=self.branch)

    def __enter__(self) -> "While":
        from ...Original.Logic.branch_node import BranchNode
        ctx.trigger_stack.append(ExecutionPath(self.branch.id, BranchNode.Then_output_trigger))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        from ...Original.Logic.branch_node import BranchNode
        ctx.add_connection(self.branch.id, BranchNode.Then_output_trigger, self.branch.id, BranchNode.Trigger_input_trigger)
        ctx.trigger_stack.pop()


class For(ExtensionNode):
    """A fixed-count loop structure that executes a block a specified number of times.
    
    Yields a context object that dynamically exposes the current loop iteration index.

    Args:
        count (int | Any): The total number of iterations to execute, or a numeric output port.

    Example:
        ```python
        with pvn.For(10) as loop:
            with pvn.Time.Wait(10 * loop.index):
                spawn_zombie()
        ```
    """

    def __init__(self, count: Any) -> None:
        int_count = to_int_port(count)
        self.loop_node = nodes.for_loop_node(count=int_count)
        super().__init__(root_node=self.loop_node)

    def __enter__(self) -> "For":
        from ...Original.Logic.for_loop_node import ForLoopNode
        ctx.trigger_stack.append(ExecutionPath(self.loop_node.id, ForLoopNode.LoopBody_output_trigger))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        ctx.trigger_stack.pop()

    @property
    def index(self) -> Port:
        """Output port representing the 0-based index of the current loop iteration."""
        from ...Original.Logic.for_loop_node import ForLoopNode
        if hasattr(self.loop_node, "get_port"):
            return self.loop_node.get_port(ForLoopNode.Index_output_int)
        return self.loop_node.index

    def get_primary_port(self) -> Port:
        return self.index


__all__ = ["While", "For"]
