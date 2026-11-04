from __future__ import annotations

from typing import Any, Tuple, Union
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from ..Abstract.extension_node import ExtensionNode
from .... import nodes


class If(ExtensionNode):
    """Syntactic sugar that acts as a safe visual scripting 'if/elif/else' branching block.

    Instantiates a conditional branch node and scopes child execution logic to its
    'True' branch. Allows chaining alternative paths via `.Elif()` and `.Else`.

    Example:
        ```python
        with If(wave_num == 1) as branch:
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

    def __enter__(self) -> If:
        self.node.Output.Then.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.node.Output.Then.__exit__(exc_type, exc_val, exc_tb)

    @property
    def Else(self) -> ExecutionPath:
        """Execution path target corresponding to the 'False' branch of this condition."""
        return self.node.Output.Else

    def Elif(self, condition: Any) -> If:
        """Constructs an alternative conditional branch connected to the 'False' output of this block.

        Args:
            condition: A boolean expression, condition port, or comparison to evaluate.

        Returns:
            If: A new conditional block scoped to the alternate path.
        """
        _ctx.trigger_stack.append(self.node.Output.Else)
        new_branch = If(condition)
        _ctx.trigger_stack.pop()
        return new_branch


class Switch(ExtensionNode):
    """Syntactic sugar for transpiling 'switch-case' branching statements into chained branch nodes.

    Sequential `.case()` blocks evaluate target values sequentially. If a case matches,
    execution enters that block; otherwise, it passes down the chain to subsequent cases
    or the fallback `.default` block.

    Example:
        ```python
        with Switch(plant.plantType) as sw:
            with sw.case(PlantType.TwinFlower):
                ...

            with sw.case(PlantType.SunFlower):
                ...

            with sw.default:
                ...
        ```
    """

    def __init__(self, target: Any) -> None:
        super().__init__()
        self.target = target
        self.last_false_path: Any = None
        self.parent_trigger: Any = (
            _ctx.trigger_stack[-1] if _ctx.trigger_stack else None
        )

    def __enter__(self) -> Switch:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass

    def case(self, *values: Any) -> _SwitchCase:
        """Defines a case block evaluated against one or more possible matching values.

        Args:
            *values: Values or enums to check against the switch target.

        Returns:
            _SwitchCase: Context manager handling the execution branch for this case.
        """
        if len(values) == 1 and isinstance(values[0], (list, tuple, set)):
            values = tuple(values[0])
        return _SwitchCase(self, values)

    Case = case

    @property
    def default(self) -> _SwitchDefault:
        """Fallback context block executed when no preceding `.case()` conditions match."""
        return _SwitchDefault(self)

    @property
    def Default(self) -> _SwitchDefault:
        return self.default


class _SwitchCase(ExtensionNode):
    """Context manager representing a single evaluated case branch in a Switch construct."""

    def __init__(self, switch_obj: Switch, values: Tuple[Any, ...]) -> None:
        super().__init__()
        self.switch = switch_obj
        self.values = values
        self.branch_node: Any = None

    def __enter__(self) -> _SwitchCase:
        condition = self.switch.target == self.values[0]
        for val in self.values[1:]:
            condition = condition | (self.switch.target == val)

        saved_stack = _ctx.trigger_stack[:]
        _ctx.trigger_stack.clear()

        self.branch_node = nodes.branch_node(condition=condition)
        self.attach_node(self.branch_node)

        _ctx.trigger_stack.extend(saved_stack)

        if self.switch.last_false_path is not None:
            _ctx.add_connection(
                self.switch.last_false_path.id,
                self.switch.last_false_path.out_trigger,
                self.branch_node.id,
                self.branch_node.port_input_trigger_Trigger.name,
            )
        elif _ctx.trigger_stack:
            curr = _ctx.trigger_stack[-1]
            _ctx.add_connection(
                curr.id, curr.out_trigger, self.branch_node.id, self.branch_node.port_input_trigger_Trigger.name
            )

        self.switch.last_false_path = ExecutionPath(
            self.branch_node.port_output_trigger_Else
        )

        _ctx.trigger_stack.append(
            ExecutionPath(self.branch_node.port_output_trigger_Then)
        )
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        _ctx.trigger_stack.pop()


class _SwitchDefault(ExtensionNode):
    """Context manager representing the fallback branch of a Switch construct."""

    def __init__(self, switch_obj: Switch) -> None:
        super().__init__()
        self.switch = switch_obj

    def __enter__(self) -> _SwitchDefault:
        if self.switch.last_false_path is not None:
            _ctx.trigger_stack.append(self.switch.last_false_path)
        elif self.switch.parent_trigger:
            _ctx.trigger_stack.append(self.switch.parent_trigger)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        _ctx.trigger_stack.pop()


__all__ = ["If", "Switch", "_SwitchCase", "_SwitchDefault"]
