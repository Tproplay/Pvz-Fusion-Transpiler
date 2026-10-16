from __future__ import annotations

from typing import Any
from .sun import _SunManager
from .money import _MoneyManager
from .... import nodes


class _GameMeta(type):
    """Metaclass that exposes properties directly on Game and Board classes."""

    @property
    def Sun(cls) -> _SunManager:
        return _SunManager()

    @Sun.setter
    def Sun(cls, value: Any) -> None:
        if isinstance(value, _SunManager):
            return
        _SunManager().set(value)

    @property
    def Money(cls) -> _MoneyManager:
        return _MoneyManager()

    @Money.setter
    def Money(cls, value: Any) -> None:
        if isinstance(value, _MoneyManager):
            return
        _MoneyManager().set(value)

    @property
    def Wave(cls) -> Any:
        return nodes.on_wave().port_output_int_Wave


class Game(metaclass=_GameMeta):
    """Global game state and stage interface."""

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        raise TypeError(f"{cls.__name__} is a static interface and cannot be instantiated.")

    @staticmethod
    def get_buff(buff_enum: Any) -> Any:
        return nodes.get_travel_buff(buff_enum=buff_enum)

    @staticmethod
    def get_travel_buff(buff_enum: Any) -> Any:
        return nodes.get_travel_buff(buff_enum=buff_enum)

    @staticmethod
    def trigger_game_over(reason: Any = "Defeated!") -> Any:
        return nodes.game_over(reason=reason)

    @staticmethod
    def trigger_game_win() -> Any:
        return nodes.game_win()


class Board(Game):
    """Board interface, aliasing Game for full backwards compatibility."""
    pass


__all__ = ["Game", "Board"]
