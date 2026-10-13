from __future__ import annotations
from typing import Any, Optional
from ..extension_node import ExtensionNode
from ....Core.context import ctx, ExecutionPath
from ...Original.Logic.do_once_node import DoOnceNode
from ...Original.Logic.repeat_until_node import RepeatUntilNode
from ...Original.Logic.wait_until_node import WaitUntilNode
from ...Original.Node import to_port


class DoOnce(ExtensionNode):
    """Context manager that executes a block of visual logic only once."""

    def __init__(self, reset_trigger: Optional[Any] = None) -> None:
        self.node = DoOnceNode()
        super().__init__(root_node=self.node)

        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, self.node.node_id, DoOnceNode.Trigger_input_trigger)

        if reset_trigger is not None:
            to_port(reset_trigger).connect(self.node.get_input(DoOnceNode.Reset_input_trigger))

    def __enter__(self) -> DoOnce:
        ctx.trigger_stack.append(ExecutionPath(self.node.node_id, DoOnceNode.Port_output_trigger))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if ctx.trigger_stack:
            ctx.trigger_stack.pop()

    @property
    def Reset(self) -> Any:
        return self.node.get_input(DoOnceNode.Reset_input_trigger)


class RepeatUntil(ExtensionNode):
    """Context manager that loops execution until a given boolean condition evaluates to True."""

    def __init__(self, condition: Any) -> None:
        self.node = RepeatUntilNode()
        super().__init__(root_node=self.node)

        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, self.node.node_id, RepeatUntilNode.Trigger_input_trigger)

        to_port(condition).connect(self.node.get_input(RepeatUntilNode.Condition_input_bool))

    def __enter__(self) -> RepeatUntil:
        ctx.trigger_stack.append(ExecutionPath(self.node.node_id, RepeatUntilNode.LoopBody_output_trigger))
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if ctx.trigger_stack:
            ctx.trigger_stack.pop()
        ctx.trigger_stack.append(ExecutionPath(self.node.node_id, RepeatUntilNode.Complete_output_trigger))

    @property
    def OnComplete(self) -> ExecutionPath:
        return ExecutionPath(self.node.node_id, RepeatUntilNode.Complete_output_trigger)


class WaitUntil(ExtensionNode):
    """Context manager / statement that pauses execution until condition becomes True."""

    def __init__(self, condition: Any) -> None:
        self.node = WaitUntilNode()
        super().__init__(root_node=self.node)

        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, self.node.node_id, WaitUntilNode.Trigger_input_trigger)

        to_port(condition).connect(self.node.get_input(WaitUntilNode.Condition_input_bool))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(self.node.node_id, WaitUntilNode.Complete_output_trigger)

    def __enter__(self) -> WaitUntil:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass
