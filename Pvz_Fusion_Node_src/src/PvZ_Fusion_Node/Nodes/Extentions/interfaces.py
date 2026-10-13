"""
Core interfaces and protocols for visual script composite extensions.
Covers equality, arithmetic, logic, branching (If/Switch), menus, and entities.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Protocol, Union, runtime_checkable

# =============================================================================
# OPERATOR & EXPRESSION PROTOCOLS
# =============================================================================

@runtime_checkable
class IEquatable(Protocol):
    """Protocol for nodes/expressions supporting equality checks (==, !=)."""

    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def equals(self, other: Any) -> Any: ...


@runtime_checkable
class IComparable(Protocol):
    """Protocol for nodes/expressions supporting ordering comparisons (<, <=, >, >=)."""

    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def compare_to(self, other: Any) -> Any: ...


@runtime_checkable
class IArithmetic(Protocol):
    """Protocol for numeric nodes supporting mathematical operators (+, -, *, /, %)."""

    def __add__(self, other: Any) -> Any: ...
    def __sub__(self, other: Any) -> Any: ...
    def __mul__(self, other: Any) -> Any: ...
    def __truediv__(self, other: Any) -> Any: ...
    def __mod__(self, other: Any) -> Any: ...


@runtime_checkable
class ILogical(Protocol):
    """Protocol for condition nodes supporting boolean algebra (&, |, ~)."""

    def __and__(self, other: Any) -> Any: ...
    def __or__(self, other: Any) -> Any: ...
    def __invert__(self) -> Any: ...


# =============================================================================
# FLOW CONTROL PROTOCOLS (If, Switch)
# =============================================================================

@runtime_checkable
class IConditionalBranch(Protocol):
    """Protocol for binary branching structures (e.g., If / Else)."""

    @property
    def condition(self) -> Any:
        """The boolean signal or port driving the branch."""
        ...

    @property
    def then_flow(self) -> Any:
        """Trigger flow emitted when condition resolves to True."""
        ...

    @property
    def else_flow(self) -> Any:
        """Trigger flow emitted when condition resolves to False."""
        ...


@runtime_checkable
class IMultiBranch(Protocol):
    """Protocol for multi-case dispatch structures (e.g., Switch)."""

    @property
    def selector(self) -> Any:
        """The evaluation key/port used for case matching."""
        ...

    def add_case(self, match_val: Any, target_flow: Optional[Any] = None) -> Any:
        """Registers a case branch matching match_val."""
        ...

    @property
    def default_flow(self) -> Any:
        """Trigger flow executed when no cases match."""
        ...


# =============================================================================
# UI & SELECTION PROTOCOLS (MultiSelectMenu)
# =============================================================================

@runtime_checkable
class IMenuOption(Protocol):
    """Protocol for individual selectable choices in a menu."""

    @property
    def title(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def on_selected_flow(self) -> Any: ...


@runtime_checkable
class IMenuContainer(Protocol):
    """Protocol for interactive choice dialogs."""

    def add_option(
        self,
        title: str,
        description: str = "",
        plant_type: int = 254,
        zombie_type: int = -1,
        **kwargs: Any,
    ) -> Any:
        """Appends a choice option to this menu."""
        ...

    @property
    def on_exit_flow(self) -> Any: ...
    @property
    def on_refresh_flow(self) -> Any: ...


# =============================================================================
# ENTITY PROTOCOLS (Plant, Zombie)
# =============================================================================

@runtime_checkable
class IPlantEntity(Protocol):
    """Protocol for high-level Plant actor extensions."""

    @property
    def plant_port(self) -> Any:
        """The underlying Plant entity port."""
        ...

    def heal(self, amount: Union[float, Any]) -> Any: ...
    def damage(self, amount: Union[float, Any]) -> Any: ...
    def kill(self) -> Any: ...
    def move(self, col: int, row: int, force: bool = False) -> Any: ...
    def give_shield(self, amount: Union[float, Any]) -> Any: ...
    def apply_buff(self, attack_mult: float = 1.0, health_mult: float = 1.0) -> Any: ...


@runtime_checkable
class IZombieEntity(Protocol):
    """Protocol for high-level Zombie actor extensions."""

    @property
    def zombie_port(self) -> Any:
        """The underlying Zombie entity port."""
        ...

    def damage(self, amount: Union[float, Any]) -> Any: ...
    def hypnotize(self) -> Any: ...
    def move(self, col: int, row: int) -> Any: ...
    def modify_health(self, ratio: float) -> Any: ...
    def play_anim(self, anim_name: str) -> Any: ...


# =============================================================================
# VARIABLE PROTOCOL
# =============================================================================

@runtime_checkable
class IVariable(Protocol):
    """Protocol for persistent canvas variables and state containers."""

    @property
    def name(self) -> str: ...
    @property
    def asset(self) -> Any: ...
    @property
    def variable_id(self) -> str: ...

    def get(self) -> Any:
        """Emits or returns a getter node for this variable's current value."""
        ...

    def set(self, new_val: Any) -> Any:
        """Emits a setter node assigning a new value to this variable."""
        ...