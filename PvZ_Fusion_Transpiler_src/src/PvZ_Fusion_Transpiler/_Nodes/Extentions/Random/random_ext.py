from __future__ import annotations

from typing import Any, Optional
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from ..Branching.branching import If
from ..Variables.variables import IntVar
from .... import nodes
from ....typing import _staticproperty


class Random:
    """Namespace for standard and deterministic random number generation and probability triggers."""

    class TriggerChance:
        """Context manager that executes its block based on a random probability.

        Args:
            probability (float | Any): A float between 0.0 and 1.0 (e.g., 0.5 for 50%).
        """

        def __init__(self, probability: Any) -> None:
            rand = Random.randf(0.0, 1.0)
            self.flow = If(rand <= probability)

        def __enter__(self) -> Any:
            self.flow.__enter__()
            return self

        def __exit__(self, *args: Any) -> None:
            self.flow.__exit__(*args)

    class RandomTrigger:
        """Branches execution to one or more random connected paths.

        Args:
            count (int): Number of paths to trigger simultaneously.
            allow_repeat (bool): If True, the same path can be selected multiple times.
        """

        def __init__(self, count: int = 1, allow_repeat: bool = False) -> None:
            self.node = nodes.random_trigger(count=count, allow_repeat=allow_repeat)

        def __enter__(self) -> Any:
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_Trigger))
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            _ctx.trigger_stack.pop()

    @staticmethod
    def randint(min_val: int | Any, max_val: int | Any) -> Any:
        """Returns a random integer output port between min_val and max_val (inclusive)."""
        return nodes.random_int(min_val=min_val, max_val=max_val).result

    @staticmethod
    def randf(min_val: float | Any, max_val: float | Any) -> Any:
        """Returns a random float output port between min_val and max_val."""
        return nodes.random_float(min_val=min_val, max_val=max_val).result

    @_staticproperty
    def value(owner: Any = None) -> Any:
        """Returns a random float output port between 0.0 and 1.0."""
        return Random.randf(0.0, 1.0)

    class Seeded:
        """Deterministic pseudo-random number generator (LCG) built on visual script nodes.

        Uses overflow-safe LCG constants (a=75, c=74, m=65537) ensuring mathematical
        safety against 32-bit integer wrapping in the C# backend.
        """

        def __init__(self, seed: int = 12345, name: str = "PRNG_State") -> None:
            safe_seed = (abs(seed) % 65537) or 1
            self.state = IntVar(start_val=safe_seed, name=name)

            self.a = 75
            self.c = 74
            self.m = 65537

        def set_seed(self, seed_value: Any) -> Any:
            """Re-initializes the active random seed dynamically during gameplay."""
            safe_seed = (abs(seed_value) % self.m) or 1
            return self.state.set(safe_seed)

        def _next(self) -> Any:
            next_state = ((self.state * self.a) + self.c) % self.m
            self.state.set(next_state)
            return self.state.value

        def randint(self, min_val: int, max_val: int) -> Any:
            """Generates a seeded random integer within [min_val, max_val]."""
            range_size = (max_val - min_val) + 1
            raw_val = self._next()
            return min_val + (raw_val % range_size)

        def randf(self, min_val: float = 0.0, max_val: float = 1.0) -> Any:
            """Generates a seeded random float within [min_val, max_val]."""
            raw_val = self._next()
            normalized = raw_val / float(self.m - 1)
            return min_val + (normalized * (max_val - min_val))

        class TriggerChance:
            """Context manager that fires based on a seeded probability."""

            def __init__(self, rng: Random.Seeded, probability: float | Any) -> None:
                roll = rng.randf(0.0, 1.0)
                self.flow = If(roll <= probability)

            def __enter__(self) -> Any:
                self.flow.__enter__()
                return self

            def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
                self.flow.__exit__(exc_type, exc_val, exc_tb)


__all__ = ["Random"]
