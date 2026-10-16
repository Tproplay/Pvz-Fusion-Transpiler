from __future__ import annotations

from typing import Any, Optional
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from .... import nodes
from ....typing import _staticproperty
from ..Variables.variables import FloatVar


class Time:
    """Namespace for time manipulation, delays, and loop tracking."""

    _time_since_start_var: Optional[FloatVar] = None
    _time_since_game_start_var: Optional[FloatVar] = None

    class OnFixedUpdate:
        """High-frequency/timed event loop driven natively by ToggleCycleNode.
        
        Runs 10 times a second by default. Features a lazy-loaded frame tracker.

        Example:
            ```python
            with Time.OnFixedUpdate(interval=0.1) as update:
                with If(update.tick == 100):
                    ...
            ```
        """

        def __init__(self, interval: float | Any = 0.1) -> None:
            saved_stack = _ctx.trigger_stack[:]
            _ctx.trigger_stack.clear()

            self.ref = nodes.toggle_cycle_node(interval=interval)

            _ctx.trigger_stack.extend(saved_stack)

            if _ctx.trigger_stack:
                previous_exec = _ctx.trigger_stack[-1]
                _ctx.add_connection(
                    previous_exec.id, previous_exec.out_trigger, self.ref.id, self.ref.port_input_trigger_Trigger.name
                )

            self._counter: Any = None

        def __enter__(self) -> Time.OnFixedUpdate:
            _ctx.trigger_stack.append(ExecutionPath(self.ref.port_output_trigger_OnCycle))
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            _ctx.trigger_stack.pop()

        def toggle(self) -> Time.OnFixedUpdate:
            if _ctx.trigger_stack:
                current_exec = _ctx.trigger_stack[-1]
                _ctx.add_connection(
                    current_exec.id, current_exec.out_trigger, self.ref.id, self.ref.port_input_trigger_Trigger.name
                )
                _ctx.trigger_stack[-1] = ExecutionPath(self.ref.port_output_trigger_OnEnable)
            return self

        @property
        def tick(self) -> Any:
            if self._counter is None:
                saved_stack = _ctx.trigger_stack[:]
                _ctx.trigger_stack.clear()

                self._counter = nodes.counter_node(start_val=0, reset=None)
                _ctx.add_connection(self.ref.id, self.ref.port_output_trigger_OnCycle.name, self._counter.id, self._counter.port_input_trigger_Trigger.name)

                _ctx.trigger_stack.extend(saved_stack)

            return self._counter.port_output_int_Count

        @property
        def on_cycle(self) -> ExecutionPath:
            return ExecutionPath(self.ref.port_output_trigger_OnCycle)

        @property
        def on_enable(self) -> ExecutionPath:
            return ExecutionPath(self.ref.port_output_trigger_OnEnable)

        @property
        def on_disable(self) -> ExecutionPath:
            return ExecutionPath(self.ref.port_output_trigger_OnDisable)

    class Wait:
        """A clean context manager to pause execution timelines."""

        def __init__(self, duration: Any) -> None:
            self.node = nodes.wait_node(duration=duration)

        def __enter__(self) -> Time.Wait:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            _ctx.trigger_stack.pop()

    @_staticproperty
    def time_since_start(owner: Any = None) -> Any:
        if Time._time_since_start_var is None:
            saved_stack = _ctx.trigger_stack[:]
            _ctx.trigger_stack.clear()

            Time._time_since_start_var = FloatVar(
                start_val=0.0, name="TimeSinceBoardStart"
            )

            start = nodes.on_board_start()
            with ExecutionPath(start.port_output_trigger_Trigger):
                with Time.OnFixedUpdate(interval=0.1):
                    Time._time_since_start_var += 0.1

            _ctx.trigger_stack.extend(saved_stack)

        return Time._time_since_start_var.value

    @_staticproperty
    def time_since_game_start(owner: Any = None) -> Any:
        if Time._time_since_game_start_var is None:
            saved_stack = _ctx.trigger_stack[:]
            _ctx.trigger_stack.clear()

            Time._time_since_game_start_var = FloatVar(
                start_val=0.0, name="TimeSinceGameStart"
            )

            start = nodes.on_game_start()
            with ExecutionPath(start.port_output_trigger_Trigger):
                with Time.OnFixedUpdate(interval=0.1):
                    Time._time_since_game_start_var += 0.1

            _ctx.trigger_stack.extend(saved_stack)

        return Time._time_since_game_start_var.value


__all__ = ["Time"]
