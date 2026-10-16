"""
PvZ Fusion Board Resources & State Interface.
Provides high-level reactive managers for Sun, Money, and Wave status.
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from .. import nodes
from ..Core.context import ctx, ExecutionPath
from ..Nodes.Extentions.extensions import If


from ..Nodes.Original.GeneralFunction.use_sun_node import UseSunNode
from ..Nodes.Original.GeneralFunction.use_money_node import UseMoneyNode
from ..Nodes.Original.GeneralFunction.get_sun_amount_node import GetSunAmountNode
from ..Nodes.Original.GeneralFunction.get_money_amount_node import GetMoneyAmountNode
from ..Nodes.Original.GameFlow.get_stage_node import GetStageNode
from ..Nodes.Original.Node import Port


class _SunManager:
    """Manages the level's Sun resource with native math and transaction nodes."""

    @property
    def value(self) -> Any:
        """Primary output port representing the current Sun count."""
        return nodes.get_sun_amount().get_output(GetSunAmountNode.SunAmount_output_int)

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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, UseSunNode.OnSuccess_output_trigger))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

        @property
        def Failed(self) -> ExecutionPath:
            """Execution path triggered when the player lacks sufficient Sun."""
            return ExecutionPath(self.node.id, UseSunNode.OnFailed_output_trigger)

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

    def __rfloordiv__(self, other: Any) -> Any:
        return self.value.__rfloordiv__(other)

    def __mod__(self, other: Any) -> Any:
        return self.value % other

    def __rmod__(self, other: Any) -> Any:
        return self.value.__rmod__(other)

    def __pow__(self, other: Any) -> Any:
        return self.value ** other

    def __rpow__(self, other: Any) -> Any:
        return self.value.__rpow__(other)

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
            ctx.trigger_stack[-1] = use_node.path(UseSunNode.OnSuccess_output_trigger)

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
        ctx.trigger_stack[-1] = use_node.path(UseSunNode.OnSuccess_output_trigger)
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

    def __imod__(self, other: Any) -> "_SunManager":
        self.set(self.value % other)
        return self

    def __ipow__(self, other: Any) -> "_SunManager":
        self.set(self.value ** other)
        return self


class _MoneyManager:
    """Manages the level's persistent coin balance with full arithmetic and transaction nodes."""

    @property
    def value(self) -> Any:
        """Primary output port representing the current Money/Coin balance."""
        return nodes.get_money_amount().get_output(GetMoneyAmountNode.MoneyAmount_output_int)

    def _get_primary_port(self) -> Any:
        return self.value

    def get(self) -> Any:
        """Returns the current Money port."""
        return self.value

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
            ctx.trigger_stack.append(ExecutionPath(self.node.id, UseMoneyNode.OnSuccess_output_trigger))
            return self

        def __exit__(self, *args: Any) -> None:
            ctx.trigger_stack.pop()

        @property
        def Failed(self) -> ExecutionPath:
            """Execution path triggered when the player lacks sufficient coins."""
            return ExecutionPath(self.node.id, UseMoneyNode.OnFailed_output_trigger)

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

    def __rfloordiv__(self, other: Any) -> Any:
        return self.value.__rfloordiv__(other)

    def __mod__(self, other: Any) -> Any:
        return self.value % other

    def __rmod__(self, other: Any) -> Any:
        return self.value.__rmod__(other)

    def __pow__(self, other: Any) -> Any:
        return self.value ** other

    def __rpow__(self, other: Any) -> Any:
        return self.value.__rpow__(other)

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

    def set(self, target_value: Any) -> "_MoneyManager":
        """Calculates difference and emits add/use money nodes to match target value."""
        diff = target_value - self.value

        with If(diff > 0) as flow:
            nodes.add_money(amount=diff)

        with flow.Elif(diff < 0):
            abs_diff = diff * -1
            use_node = nodes.use_money(amount=abs_diff)
            ctx.trigger_stack[-1] = use_node.path(UseMoneyNode.OnSuccess_output_trigger)

        return self

    # In-Place Overloads
    def __iadd__(self, other: Any) -> "_MoneyManager":
        nodes.add_money(amount=other)
        return self

    def __isub__(self, other: Any) -> "_MoneyManager":
        use_node = nodes.use_money(amount=other)
        ctx.trigger_stack[-1] = use_node.path(UseMoneyNode.OnSuccess_output_trigger)
        return self

    def __imul__(self, other: Any) -> "_MoneyManager":
        self.set(self.value * other)
        return self

    def __itruediv__(self, other: Any) -> "_MoneyManager":
        self.set(self.value / other)
        return self

    def __ifloordiv__(self, other: Any) -> "_MoneyManager":
        self.set(self.value // other)
        return self

    def __imod__(self, other: Any) -> "_MoneyManager":
        self.set(self.value % other)
        return self

    def __ipow__(self, other: Any) -> "_MoneyManager":
        self.set(self.value ** other)
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
        _MoneyManager().set(value)

    @property
    def Wave(cls) -> Port:
        """Output port reference to the current wave index."""
        return nodes.on_wave().wave


class Board(metaclass=_BoardMeta):
    """Global level interface for accessing game resources and board properties."""

    Sun: _SunManager
    Money: _MoneyManager
    Wave: Port

    def __new__(cls, *args: Any, **kwargs: Any) -> None:
        raise TypeError("Board is a static interface and cannot be instantiated.")

    @staticmethod
    def change_stage(stage_name: str = "战斗") -> None:
        """Switches the game stage (e.g. '战斗', '准备')."""
        nodes.ChangeStageNode(stage_name=stage_name)

    @staticmethod
    def get_stage() -> Any:
        """Returns the output port for the current game stage name."""
        return nodes.GetStageNode().get_output(GetStageNode.StageName_output_string)

    @staticmethod
    def change_map(scene: int = 1) -> None:
        """Switches the background map scene."""
        nodes.ChangeEventMapNode(scene=scene)

    @staticmethod
    def change_music(music: int = 0) -> None:
        """Switches the background music track."""
        nodes.ChangeEventMusicNode(music=music)

    @staticmethod
    def pause_wave_countdown() -> None:
        """Pauses the countdown timer between zombie waves."""
        nodes.SetWaveCountdownPausedNode()

    @staticmethod
    def set_zombie_house_rule() -> None:
        """Applies zombie house entry rules."""
        nodes.SetZombieHouseRuleNode()

    @staticmethod
    def remove_travel_entry(kind: int = 0) -> None:
        """Removes a travel entry/buff."""
        nodes.RemoveTravelEntryNode(kind=kind)
