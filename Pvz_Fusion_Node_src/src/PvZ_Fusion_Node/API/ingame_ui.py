"""
PvZ Fusion In-Game User Interface Subsystem.
Handles on-screen banners, text popups, seed packet management, and card notifications.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Callable, Optional, Union

from .. import nodes
from ..Core.context import ctx, ExecutionPath
from ..Nodes.Extentions.extensions import InfoCard
from ..Extras.TypeMgr import PlantType


class InGameUI:
    """Static helpers for on-screen UI: info cards, seed packet cards, and text popups."""

    @staticmethod
    def display_info_card(
        big_title: Any,
        small_title: Any,
        on_clicked: Optional[Callable[[], None]] = None,
    ) -> InfoCard:
        """Displays an in-game Info Card popup.

        Args:
            big_title: Main header text, or a text/variable port.
            small_title: Secondary/subtitle text, or a text/variable port.
            on_clicked: Callback to execute when the player clicks the card.

        Returns:
            InfoCard: The card object with `.Output.OnCardClicked` execution path.
        """
        return InfoCard(big_title, small_title, callback=on_clicked)

    @staticmethod
    def give_plant_card(
        plant_type: Union[int, PlantType, Any],
        cooldown: float = 7.5,
        cost: int = 100,
        use_default: bool = True,
    ) -> None:
        """Adds a seed packet card for the given plant to the player's card selection."""
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        p_type = nodes.plant_type_value(val=plant_type)
        nodes.add_plant_card(p_type=p_type, cd=cooldown, cost=cost, default_data=use_default)

    @staticmethod
    def remove_plant_card(plant_type: Union[int, PlantType, Any]) -> None:
        """Removes a plant's seed packet card from the player's card selection."""
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        p_type = nodes.plant_type_value(val=plant_type)
        nodes.delete_card_by_type(plant_type=p_type)

    @staticmethod
    def spawn_dropped_card(
        row: Union[int, Any],
        col: Union[int, Any],
        plant_type: Union[int, PlantType, Any],
    ) -> None:
        """Spawns a pickup-able plant card at a board location."""
        if isinstance(plant_type, Enum):
            plant_type = plant_type.value
        p_type = nodes.plant_type_value(val=plant_type)
        nodes.create_plant_card(row=row, column=col, plant_type=p_type)

    @staticmethod
    def display_text(*args: Any, duration: float = 3.0) -> None:
        """Formats and displays text, variables, and ports on screen.

        Supports dynamic boolean branching when BoolVar or logic ports are passed.
        """
        from ..Nodes.Extentions.extensions import BoolVar, If
        from ..Libraries.StdLib import format_string
        from ..node_base import PortReference
        from ..nodes import show_text

        BOOL_NODE_TYPES = {
            "BoolVariableNode", "GetBoolVariableValueNode", "CompareIntNode",
            "CompareFloatNode", "CompareGameObjectNode", "AndNode", "OrNode",
            "NotNode", "ToggleNode",
        }

        bool_arg = None
        for arg in args:
            if isinstance(arg, BoolVar):
                bool_arg = arg.value
                break
            elif isinstance(arg, PortReference) or hasattr(arg, "node"):
                node_type = getattr(getattr(arg, "node", None), "type", "")
                if node_type in BOOL_NODE_TYPES:
                    bool_arg = arg
                    break

        if bool_arg is not None:
            formatted_args_true = []
            for arg in args:
                if arg is bool_arg or (isinstance(arg, BoolVar) and arg.value is bool_arg):
                    formatted_args_true.append("True")
                else:
                    formatted_args_true.append(arg)

            formatted_args_false = []
            for arg in args:
                if arg is bool_arg or (isinstance(arg, BoolVar) and arg.value is bool_arg):
                    formatted_args_false.append("False")
                else:
                    formatted_args_false.append(arg)

            with If(bool_arg) as branch:
                show_text(
                    display_text=format_string(*formatted_args_true),
                    duration=duration,
                )

            with branch.Else:
                show_text(
                    display_text=format_string(*formatted_args_false),
                    duration=duration,
                )
        else:
            show_text(
                display_text=format_string(*args),
                duration=duration,
            )

    class InfoCard:
        """Context manager style for displaying an in-game Info Card popup.

        Example:
            ```python
            with pvn.InGameUI.InfoCard("New Wave!", "A horde approaches"):
                pvn.Print("Card dismissed")
            ```
        """

        def __init__(self, big_title: str, small_title: str = "") -> None:
            self.node = nodes.create_info_card(big_title=big_title, small_title=small_title)

        def __enter__(self) -> "InGameUI.InfoCard":
            ctx.trigger_stack.append(ExecutionPath(self.node.id, "点击卡牌时触发"))
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            if ctx.trigger_stack:
                ctx.trigger_stack.pop()


def Print(*args: Any, duration: float = 3.0) -> None:
    """Alias for InGameUI.display_text."""
    InGameUI.display_text(*args, duration=duration)
