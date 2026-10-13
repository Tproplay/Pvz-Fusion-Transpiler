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

    @staticmethod
    def delete_all_info_cards() -> None:
        """Deletes all active info cards from the screen."""
        nodes.DeleteInfoCardsNode()

    @staticmethod
    def get_held_tool() -> Any:
        """Returns the output port representing the player's currently held tool type."""
        from ..Nodes.Original.GeneralFunction.get_held_tool_node import GetHeldToolNode
        return nodes.GetHeldToolNode().get_output(GetHeldToolNode.ToolType_output_tooltype)

    @staticmethod
    def get_tool_cooldown(tool_type: Any) -> Any:
        """Returns the cooldown duration port for the specified tool type."""
        from ..Nodes.Original.Node import to_port
        from ..Nodes.Original.GeneralFunction.get_tool_cooldown_node import GetToolCooldownNode
        from ..Nodes.Original.GeneralFunction.tool_type_value_node import ToolTypeValueNode
        if hasattr(tool_type, "value") and not hasattr(tool_type, "node"):
            tool_type = tool_type.value
        if isinstance(tool_type, int):
            t_port = nodes.ToolTypeValueNode(tool_type=tool_type).get_output(ToolTypeValueNode.ToolType_output_tooltype)
        else:
            t_port = to_port(tool_type)
        node = nodes.GetToolCooldownNode()
        t_port.connect(node.get_input(GetToolCooldownNode.ToolType_input_tooltype))
        return node.get_output(GetToolCooldownNode.Cooldown_output_float)

    @staticmethod
    def set_tool_cooldown(tool_type: Any, cooldown: Any) -> None:
        """Sets the cooldown duration for a specific tool type."""
        from ..Nodes.Original.Node import to_port
        from ..Nodes.Original.GeneralFunction.set_tool_cooldown_node import SetToolCooldownNode
        from ..Nodes.Original.GeneralFunction.tool_type_value_node import ToolTypeValueNode
        if hasattr(tool_type, "value") and not hasattr(tool_type, "node"):
            tool_type = tool_type.value
        if isinstance(tool_type, int):
            t_port = nodes.ToolTypeValueNode(tool_type=tool_type).get_output(ToolTypeValueNode.ToolType_output_tooltype)
        else:
            t_port = to_port(tool_type)
        node = nodes.SetToolCooldownNode()
        t_port.connect(node.get_input(SetToolCooldownNode.ToolType_input_tooltype))
        to_port(cooldown).connect(node.get_input(SetToolCooldownNode.Cooldown_input_float))

    @staticmethod
    def give_zombie_card(zombie_type: Any) -> None:
        """Adds a zombie card of specified type to the player's selection."""
        from ..Nodes.Original.Node import to_port
        from ..Nodes.Original.ZombieFunction.add_zombie_card_node import AddZombieCardNode
        from ..Nodes.Original.ZombieFunction.zombie_type_value_node import ZombieTypeValueNode
        if hasattr(zombie_type, "value") and not hasattr(zombie_type, "node"):
            zombie_type = zombie_type.value
        if isinstance(zombie_type, int):
            z_port = nodes.ZombieTypeValueNode(zombie_type=zombie_type).get_output(ZombieTypeValueNode.ZombieType_output_zombietype)
        else:
            z_port = to_port(zombie_type)
        node = nodes.AddZombieCardNode()
        z_port.connect(node.get_input(AddZombieCardNode.ZombieType_input_zombietype))

    @staticmethod
    def remove_all_zombie_cards(zombie_type: Any = None) -> None:
        """Removes zombie card(s) of specified type from the player's selection."""
        from ..Nodes.Original.Node import to_port
        from ..Nodes.Original.ZombieFunction.delete_zombie_cards_node import DeleteZombieCardsNode
        from ..Nodes.Original.ZombieFunction.zombie_type_value_node import ZombieTypeValueNode
        node = nodes.DeleteZombieCardsNode()
        if zombie_type is not None:
            if hasattr(zombie_type, "value") and not hasattr(zombie_type, "node"):
                zombie_type = zombie_type.value
            if isinstance(zombie_type, int):
                z_port = nodes.ZombieTypeValueNode(zombie_type=zombie_type).get_output(ZombieTypeValueNode.ZombieType_output_zombietype)
            else:
                z_port = to_port(zombie_type)
            z_port.connect(node.get_input(DeleteZombieCardsNode.ZombieType_input_zombietype))

    @staticmethod
    def set_zombie_card_cooldown(zombie_type: Any, cooldown: Any) -> None:
        """Sets the cooldown for a specific zombie card."""
        from ..Nodes.Original.Node import to_port
        from ..Nodes.Original.ZombieFunction.set_zombie_card_cooldown_node import SetZombieCardCooldownNode
        from ..Nodes.Original.ZombieFunction.zombie_type_value_node import ZombieTypeValueNode
        if hasattr(zombie_type, "value") and not hasattr(zombie_type, "node"):
            zombie_type = zombie_type.value
        if isinstance(zombie_type, int):
            z_port = nodes.ZombieTypeValueNode(zombie_type=zombie_type).get_output(ZombieTypeValueNode.ZombieType_output_zombietype)
        else:
            z_port = to_port(zombie_type)
        node = nodes.SetZombieCardCooldownNode()
        z_port.connect(node.get_input(SetZombieCardCooldownNode.ZombieType_input_zombietype))
        to_port(cooldown).connect(node.get_input(SetZombieCardCooldownNode.Cooldown_input_float))

    show_text = display_text

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
            from ..Nodes.Original.GeneralFunction.create_info_card_node import CreateInfoCardNode
            ctx.trigger_stack.append(ExecutionPath(self.node.id, CreateInfoCardNode.OnCardClicked_output_trigger))
            return self

        def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
            if ctx.trigger_stack:
                ctx.trigger_stack.pop()


def Print(*args: Any, duration: float = 3.0) -> None:
    """Alias for InGameUI.display_text."""
    InGameUI.display_text(*args, duration=duration)
