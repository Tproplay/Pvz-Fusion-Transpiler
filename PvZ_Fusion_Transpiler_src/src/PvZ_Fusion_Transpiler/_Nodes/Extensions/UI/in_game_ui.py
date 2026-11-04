from __future__ import annotations

from enum import Enum
from typing import Any
from .format_string import format_string
from .... import nodes


class InGameUI:
    """Namespace for manipulating in-game HUD, cards, info banners, and screen messages."""

    @staticmethod
    def display_info_card(big_title: Any, small_title: Any) -> Any:
        return nodes.create_info_card(
            big_title=format_string(big_title),
            small_title=format_string(small_title),
        )

    @staticmethod
    def give_plant_card(
        plant_type: Any,
        cooldown: Any = 7.5,
        cost: Any = 100,
        use_default: Any = True,
    ) -> Any:
        if isinstance(plant_type, (int, float)) and not isinstance(plant_type, Enum):
            raise TypeError("PlantType must be an Enum instance (e.g. PlantType.PEASHOOTER); direct int is not allowed.")
        if isinstance(plant_type, Enum):
            plant_type = nodes.plant_type_value(val=plant_type)
        return nodes.add_plant_card(
            p_type=plant_type,
            cd=cooldown,
            cost=cost,
            default_data=use_default,
        )

    @staticmethod
    def remove_plant_card(plant_type: Any) -> Any:
        if isinstance(plant_type, (int, float)) and not isinstance(plant_type, Enum):
            raise TypeError("PlantType must be an Enum instance; direct int is not allowed.")
        if isinstance(plant_type, Enum):
            plant_type = nodes.plant_type_value(val=plant_type)
        return nodes.delete_card_by_type(plant_type=plant_type)

    @staticmethod
    def spawn_dropped_card(row: Any, col: Any, plant_type: Any) -> Any:
        if isinstance(plant_type, (int, float)) and not isinstance(plant_type, Enum):
            raise TypeError("PlantType must be an Enum instance; direct int is not allowed.")
        if isinstance(plant_type, Enum):
            plant_type = nodes.plant_type_value(val=plant_type)
        return nodes.create_plant_card(row=row, column=col, plant_type=plant_type)

    @staticmethod
    def display_text(*args: Any, duration: Any = 3.0) -> Any:
        """Pass any mix of text and variables to auto-format and display them on screen."""
        final_text = format_string(*args)
        return nodes.show_text(text=final_text, duration=duration)

    show_text = display_text

    @staticmethod
    def give_zombie_card(
        zombie_type: Any,
        cooldown: Any = 7.5,
        cost: Any = 50,
        use_default: Any = True,
    ) -> Any:
        if isinstance(zombie_type, (int, float)) and not isinstance(zombie_type, Enum):
            raise TypeError("ZombieType must be an Enum instance (e.g. ZombieType.NormalZombie); direct int is not allowed.")
        return nodes.add_zombie_card(
            zombie_type=zombie_type,
            cd=cooldown,
            cost=cost,
            default_data=use_default,
        )

    @staticmethod
    def remove_zombie_cards(zombie_type: Any = None) -> Any:
        if zombie_type is not None and isinstance(zombie_type, (int, float)) and not isinstance(zombie_type, Enum):
            raise TypeError("ZombieType must be an Enum instance; direct int is not allowed.")
        return nodes.delete_zombie_cards(zombie_type=zombie_type)

    @staticmethod
    def set_zombie_card_cooldown(zombie_type: Any, total: Any = None, remaining: Any = None) -> Any:
        if isinstance(zombie_type, (int, float)) and not isinstance(zombie_type, Enum):
            raise TypeError("ZombieType must be an Enum instance; direct int is not allowed.")
        return nodes.set_zombie_card_cooldown(zombie_type=zombie_type, total=total, remaining=remaining)

    @staticmethod
    def clear_info_cards(card_object: Any = None, all_cards: Any = True) -> Any:
        return nodes.delete_info_cards(card_object=card_object, all_cards=all_cards)

    delete_info_cards = clear_info_cards


__all__ = ["InGameUI"]
