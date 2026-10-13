"""
PvZ Fusion Board Resources & State Interface.
Provides high-level reactive managers for Sun, Money, and Wave status.
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from .. import nodes
from ..Core.context import ctx, ExecutionPath
from ..Nodes.Extentions.extensions import If


class _SunManager:
    """Manages the level's Sun resource with native math and transaction nodes."""

    @property
    def value(self) -> Any:
        """Primary output port representing the current Sun count."""
        return nodes.get_sun_amount().sunAmount

    def _get_primary_port(self) -> Any:
        return self.value

    class SpendSun:
        """Context manager for conditional Sun transactions.

        Executes the main body on successful consumption, or routes to `.Failed`
        if Sun is insufficient.

        Example:
            ```python
            with pvn.Board.Sun.SpendSun(50) as spend:
                ...

            with spend.Failed:
                pvn.Print("Not enough Sun!")
            ```
        """

        def __init__(self, amount: Any) -> None:
            self.node = nodes.use_sun(amount=amount)

        def __enter__(self) -> "_SunManager.SpendSun":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "消耗成功"))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

        @property
        def Failed(self) -> ExecutionPath:
            """Execution path triggered when the player lacks sufficient Sun."""
            return ExecutionPath(self.node.id, "阳光不足")

    # Native Math Overloads
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

    # Comparison Overloads
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

    def set(self, target_value: Any) -> "_SunManager":
        """Calculates difference and emits add/use nodes to match the target value."""
        diff = target_value - self.value

        with If(diff > 0) as flow:
            nodes.add_sun(amount=diff)

        with flow.Elif(diff < 0):
            abs_diff = diff * -1
            use_node = nodes.use_sun(amount=abs_diff)
            ctx.trigger_stack[-1] = use_node.path("onSuccess")

        return self

    def get(self) -> Any:
        """Returns the current Sun port."""
        return self.value

    # In-Place Overloads
    def __iadd__(self, other: Any) -> "_SunManager":
        nodes.add_sun(amount=other)
        return self

    def __isub__(self, other: Any) -> "_SunManager":
        use_node = nodes.use_sun(amount=other)
        ctx.trigger_stack[-1] = use_node.path("onSuccess")
        return self

    def __imul__(self, other: Any) -> "_SunManager":
        self.set(self.value * other)
        return self

    def __itruediv__(self, other: Any) -> "_SunManager":
        self.set(self.value / other)
        return self

    def __ifloordiv__(self, other: Any) -> "_SunManager":
        self.set(self.value // other)
        return self


class _MoneyManager:
    """Manages the level's persistent coin balance."""

    @staticmethod
    def check_money(
        amount: Any,
        on_true_callback: Optional[Callable[[], None]] = None,
        on_false_callback: Optional[Callable[[], None]] = None,
    ) -> None:
        """Checks if the player has enough coins by spending and immediately refunding the amount."""
        with nodes.use_money(amount=amount) as node:
            with node.Output.OnSuccess:
                nodes.add_money(amount=amount)
                if on_true_callback:
                    on_true_callback()

            with node.Output.OnFailed:
                if on_false_callback:
                    on_false_callback()

    class SpendMoney:
        """Context manager for conditional coin transactions.

        Executes the main body on successful consumption, or routes to `.Failed`
        if coins are insufficient.
        """

        def __init__(self, amount: Any) -> None:
            self.node = nodes.use_money(amount=amount)

        def __enter__(self) -> "_MoneyManager.SpendMoney":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "消耗成功"))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

        @property
        def Failed(self) -> ExecutionPath:
            """Execution path triggered when the player lacks sufficient coins."""
            return ExecutionPath(self.node.id, "金币不足")

    def __iadd__(self, other: Any) -> "_MoneyManager":
        nodes.add_money(amount=other)
        return self

    def __isub__(self, other: Any) -> "_MoneyManager":
        nodes.use_money(amount=other)
        return self


class _BoardMeta(type):
    """Metaclass exposing static resource accessors on the Board class."""

    @property
    def Sun(cls) -> _SunManager:
        """Board Sun manager for reading, setting, and checking Sun."""
        return _SunManager()

    @Sun.setter
    def Sun(cls, value: Any) -> None:
        if isinstance(value, _SunManager):
            return
        _SunManager().set(value)

    @property
    def Money(cls) -> _MoneyManager:
        """Board Money manager for coin transactions and balance checks."""
        return _MoneyManager()

    @Money.setter
    def Money(cls, value: Any) -> None:
        if isinstance(value, _MoneyManager):
            return
        raise NotImplementedError(
            "Direct assignment `Board.Money = X` is not supported by the game engine. "
            "Use `Board.Money += amount` or `Board.Money -= amount` instead."
        )

    @property
    def Wave(cls) -> Any:
        """Output port reference to the current wave index."""
        return nodes.on_wave().wave


class Board(metaclass=_BoardMeta):
    """Global level interface for accessing game resources and board properties."""

    def __new__(cls, *args: Any, **kwargs: Any) -> None:
        raise TypeError("Board is a static interface and cannot be instantiated.")
