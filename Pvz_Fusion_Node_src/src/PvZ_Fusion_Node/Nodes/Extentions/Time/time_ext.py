from __future__ import annotations
from typing import Any, Optional
from ..extension_node import ExtensionNode
from .... import nodes, api
from ....Core.context import ctx, ExecutionPath
from ....typing import _staticproperty
from ..Branching.branching import If
from ..Variables.variables import FloatVar
from ....Nodes.Original import ToggleCycleNode, CounterNode, WaitNode


class Time(ExtensionNode):
    """Namespace for time manipulation, delays, and loop tracking."""

    _time_since_start_var = None
    _time_since_game_start_var = None

    class OnFixedUpdate(ExtensionNode):
        """High-frequency/timed event loop driven natively by ToggleCycleNode.
        
        Runs 10 times a second by default. Features a lazy-loaded frame tracker.

        ### Usage:
            with pvn.Time.OnFixedUpdate(interval=0.1) as update:
                pvn.Board.Sun += 1
                with pvn.If(update.tick == 100):
                    pvn.Print("100 ticks have passed!")
        """

        def __init__(self, interval: float | Any = 0.1) -> None:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()

            self.ref = nodes.toggle_cycle_node(interval=interval)

            ctx.trigger_stack.extend(saved_stack)

            if ctx.trigger_stack:
                previous_exec = ctx.trigger_stack[-1]
                ctx.add_connection(
                    previous_exec.id, previous_exec.out_trigger, self.ref.id, ToggleCycleNode.Trigger_input_trigger
                )

            super().__init__(root_node=self.ref)
            self._counter = None

        def __enter__(self) -> "Time.OnFixedUpdate":
            """Defaults straight into the repeating execution track loop body."""
            ctx.trigger_stack.append(ExecutionPath(self.ref.id, ToggleCycleNode.OnCycle_output_trigger))
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            ctx.trigger_stack.pop()

        def toggle(self) -> "Time.OnFixedUpdate":
            if ctx.trigger_stack:
                current_exec = ctx.trigger_stack[-1]
                ctx.add_connection(
                    current_exec.id, current_exec.out_trigger, self.ref.id, ToggleCycleNode.Trigger_input_trigger
                )
                ctx.trigger_stack[-1] = ExecutionPath(self.ref.id, ToggleCycleNode.OnEnable_output_trigger)
            return self

        @property
        def tick(self) -> Any:
            """Lazy getter. Spawns and wires an active CounterNode tracking the loop
            the very first time this property is read in a level script.
            """
            if self._counter is None:
                saved_stack = ctx.trigger_stack[:]
                ctx.trigger_stack.clear()

                self._counter = nodes.counter_node(start_val=0, reset=None)

                ctx.add_connection(self.ref.id, ToggleCycleNode.OnCycle_output_trigger, self._counter.id, CounterNode.Trigger_input_trigger)

                ctx.trigger_stack.extend(saved_stack)
                self.attach_node(self._counter)

            return self._counter.count

        @property
        def on_cycle(self) -> ExecutionPath:
            """Explicit access to the repeating loop execution track."""
            return ExecutionPath(self.ref.id, ToggleCycleNode.OnCycle_output_trigger)

        @property
        def on_enable(self) -> ExecutionPath:
            """Timeline track fired the exact instant the loop engine activates."""
            return ExecutionPath(self.ref.id, ToggleCycleNode.OnEnable_output_trigger)

        @property
        def on_disable(self) -> ExecutionPath:
            """Timeline track fired when the loop engine is turned off."""
            return ExecutionPath(self.ref.id, ToggleCycleNode.OnDisable_output_trigger)

    class Wait(ExtensionNode):
        """A clean Syntactic Sugar context manager to pause execution timelines."""

        def __init__(self, duration: Any) -> None:
            self.node = nodes.wait_node(duration=duration)
            super().__init__(root_node=self.node)

        def __enter__(self) -> "Time.Wait":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, WaitNode.Trigger_input_trigger))
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            ctx.trigger_stack.pop()

    @_staticproperty
    def time_since_start():
        """Returns the time in seconds since the level started (from `OnBoardStart`)."""
        if Time._time_since_start_var is None:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()

            Time._time_since_start_var = FloatVar(
                start_val=0.0, name="TimeSinceBoardStart"
            )

            with api.Trigger.OnBoardStart():
                with Time.OnFixedUpdate(interval=0.1):
                    Time._time_since_start_var += 0.1

            ctx.trigger_stack.extend(saved_stack)

        return Time._time_since_start_var.value

    @_staticproperty
    def time_since_game_start():
        """Returns the time in seconds since the game started (from `OnGameStart`,
        i.e. after the 'Ready, Set, Plant!' sequence).
        """
        if Time._time_since_game_start_var is None:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()

            Time._time_since_game_start_var = FloatVar(
                start_val=0.0, name="TimeSinceGameStart"
            )

            with api.Trigger.OnGameStart():
                with Time.OnFixedUpdate(interval=0.1):
                    Time._time_since_game_start_var += 0.1

            ctx.trigger_stack.extend(saved_stack)

        return Time._time_since_game_start_var.value


__all__ = ["Time"]
