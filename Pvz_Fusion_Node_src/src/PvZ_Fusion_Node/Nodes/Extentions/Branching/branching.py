"""
Conditional Branching Extensions for PvZ Fusion Visual Scripting.
Provides `If` and `Switch` context managers for conditional execution.
"""

from __future__ import annotations

from typing import Any, Tuple, Union

from ..extension_node import ExtensionNode
from .... import nodes
from ....Core.context import ctx, ExecutionPath


class If(ExtensionNode):
    """Syntactic sugar that acts as a safe visual scripting 'if/elif/else' branching block.

    Instantiates a conditional branch node and scopes child execution logic to its
    'True' branch. Allows chaining alternative paths via `.Elif()` and `.Else`.

    Example:
        ```python
        with pvn.If(wave_num == 1) as branch:
            ...

        with branch.Elif(wave_num == 2) as branch:
            ...

        with branch.Else:
            ...
        ```
    """

    def __init__(self, condition: Any) -> None:
        self.node = nodes.branch_node(condition=condition)
        super().__init__(root_node=self.node)

    def __enter__(self) -> "If":
        self.node.Output.Then.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.node.Output.Then.__exit__(exc_type, exc_val, exc_tb)

    @property
    def Else(self) -> ExecutionPath:
        """Execution path target corresponding to the 'False' branch of this condition."""
        return self.node.Output.Else

    def Elif(self, condition: Any) -> "If":
        """Constructs an alternative conditional branch connected to the 'False' output of this block.

        Args:
            condition: A boolean expression, condition port, or comparison to evaluate.

        Returns:
            If: A new conditional block scoped to the alternate path.
        """
        ctx.trigger_stack.append(self.node.Output.Else)
        new_branch = If(condition)
        ctx.trigger_stack.pop()
        return new_branch


class Switch(ExtensionNode):
    """Syntactic sugar for transpiling 'switch-case' branching statements into chained branch nodes.

    Sequential `.case()` blocks evaluate target values sequentially. If a case matches,
    execution enters that block; otherwise, it passes down the chain to subsequent cases
    or the fallback `.default` block.

    Example:
        ```python
        with pvn.Switch(plant.plantType) as sw:
            with sw.case(PlantType.TwinFlower):
                pvn.Board.Sun += 100

            with sw.case(PlantType.SunFlower):
                pvn.Board.Sun += 50

            with sw.default:
                pvn.Board.Sun += 10
        ```
    """

    def __init__(self, target: Any) -> None:
        super().__init__()
        self.target = target
        self.last_false_path: Any = None
        self.parent_trigger: Any = (
            ctx.trigger_stack[-1] if ctx.trigger_stack else None
        )

    def __enter__(self) -> "Switch":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass

    def case(self, *values: Any) -> "_SwitchCase":
        """Defines a case block evaluated against one or more possible matching values.

        Args:
            *values: Values or enums to check against the switch target.

        Returns:
            _SwitchCase: Context manager handling the execution branch for this case.
        """
        if len(values) == 1 and isinstance(values[0], (list, tuple, set)):
            values = tuple(values[0])
        return _SwitchCase(self, values)

    @property
    def default(self) -> "_SwitchDefault":
        """Fallback context block executed when no preceding `.case()` conditions match."""
        return _SwitchDefault(self)


class _SwitchCase(ExtensionNode):
    """Context manager representing a single evaluated case branch in a Switch construct."""

    def __init__(self, switch_obj: Switch, values: Tuple[Any, ...]) -> None:
        super().__init__()
        self.switch = switch_obj
        self.values = values
        self.branch_node: Any = None

    def __enter__(self) -> "_SwitchCase":
        condition = self.switch.target == self.values[0]
        for val in self.values[1:]:
            condition = condition | (self.switch.target == val)

        # Temporarily hide the stack to prevent parallel auto-wiring
        saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()

        self.branch_node = nodes.branch_node(condition=condition)
        self.attach_node(self.branch_node)

        ctx.trigger_stack.extend(saved_stack)

        from ....Nodes.Original.Logic.branch_node import BranchNode

        # Explicitly wire in a sequential chain (False -> Next Case)
        if self.switch.last_false_path is not None:
            ctx.add_connection(
                self.switch.last_false_path.id,
                self.switch.last_false_path.out_trigger,
                self.branch_node.id,
                BranchNode.Trigger_input_trigger,
            )
        elif ctx.trigger_stack:
            curr = ctx.trigger_stack[-1]
            ctx.add_connection(
                curr.id, curr.out_trigger, self.branch_node.id, BranchNode.Trigger_input_trigger
            )

        # Update the False path chain for the next case or default block
        self.switch.last_false_path = ExecutionPath(
            self.branch_node.id, BranchNode.Else_output_trigger
        )

        # Push the True branch onto trigger stack for statements inside this case
        ctx.trigger_stack.append(
            ExecutionPath(self.branch_node.id, BranchNode.Then_output_trigger)
        )
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        ctx.trigger_stack.pop()


class _SwitchDefault(ExtensionNode):
    """Context manager representing the fallback branch of a Switch construct."""

    def __init__(self, switch_obj: Switch) -> None:
        super().__init__()
        self.switch = switch_obj

    def __enter__(self) -> "_SwitchDefault":
        if self.switch.last_false_path is not None:
            ctx.trigger_stack.append(self.switch.last_false_path)
        elif self.switch.parent_trigger:
            ctx.trigger_stack.append(self.switch.parent_trigger)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        ctx.trigger_stack.pop()


__all__ = ["If", "Switch"]
