from __future__ import annotations
from typing import Any, Callable, Optional, TypeAlias, overload, Union
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self
from ..extension_node import ExtensionNode
from .... import nodes
from ....Core.context import ctx, ExecutionPath
from ....Extras.TypeMgr import PlantType, ZombieType

class Option(ExtensionNode):
    """Standalone multiple-choice option card.

    Instantiates an option node and compiles its callback graph once for reuse
    across multiple menus.

    Args:
        title (str): Header title displayed on the option card.
        description (str): Explanatory text or perk details displayed on the card.
        callback (Callable[[], None] | None): Function executed when the option is selected.
        plant_type (int | PlantType): Plant icon ID or PlantType enum. Defaults to 254 (None).
        zombie_type (int | ZombieType): Zombie icon ID or ZombieType enum. Defaults to -1 (None).

    Example:
        ```python
        heal_perk = Option(
            title="Field Repair",
            description="Restore all active plants to full health",
            callback=lambda: pvn.Print("Repaired all plants!"),
            plant_type=PlantType.WallNut,
        )
        ```
    """

    def __init__(
        self,
        title: str,
        description: str,
        callback: Callable[[], None] | None = None,
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
    ) -> None:
        p_val = (
            plant_type.value if isinstance(plant_type, PlantType) else plant_type
        )
        z_val = (
            zombie_type.value
            if isinstance(zombie_type, ZombieType)
            else zombie_type
        )

        if p_val != -1 and p_val != 254 and z_val != -1:
            print(
                "[Warning] Option: Cannot set both Plant and Zombie type. Defaulting to Plant."
            )
            z_val = -1
        elif p_val == -1 and z_val == -1:
            p_val = 254

        self.title: str = title
        self.description: str = description
        self.callback: Callable[[], None] | None = callback
        self.plant_type: int = p_val
        self.zombie_type: int = z_val

        self.node_id: str = ctx._generate_uuid()
        self._build_node()
        super().__init__(root_node=self.node)

    def _build_node(self) -> None:
        self.node = nodes.AddMultipleChoiceOptionNode(
            title=self.title,
            description=self.description,
            plant_type=self.plant_type,
            zombie_type=self.zombie_type,
            node_id=self.node_id,
        )

        if self.callback:
            saved_stack = ctx.trigger_stack[:]
            ctx.trigger_stack.clear()
            ctx.trigger_stack.append(ExecutionPath(self.node_id, "选项被点击"))
            try:
                self.callback()
            finally:
                ctx.trigger_stack.clear()
                ctx.trigger_stack.extend(saved_stack)

    @property
    def output_port(self) -> Any:
        """Output port for this option card."""
        return self.node.get_output("选项列表")

    def get_primary_port(self) -> Any:
        return self.output_port

    def _get_primary_port(self) -> Any:
        return self.output_port


class MultiSelectMenu(ExtensionNode):
    """Deferred UI builder for pop-up selection windows.

    Collects multiple `Option` cards, merges them into an option list graph, and displays
    a selection window during gameplay.

    Args:
        is_rerollable (bool): Whether players can roll for different options. Defaults to True.
        reroll_count (int): Maximum number of allowed rerolls. Defaults to 3.
        is_skippable (bool): Whether the selection menu can be closed without choosing. Defaults to False.
        window_count (int): Total number of option cards presented simultaneously. Defaults to 3.

    Example:
        ```python
        menu = MultiSelectMenu(is_rerollable=True, reroll_count=2, window_count=3)

        @menu.option(title="Solar Surge", description="Gain +200 Sun immediately", plant_type=PlantType.SunFlower)
        def sun_surge():
            ... # Logic for granting sun bonus

        with pvn.Trigger.OnWave() as wave_num:
            with pvn.If(wave_num == 5):
                menu.show()
        ```
    """

    _Callback: TypeAlias = Callable[[], None]
    _OptionDecorator: TypeAlias = Callable[[_Callback], Option]
    
    def __init__(
        self,
        is_rerollable: bool = True,
        reroll_count: int = 3,
        is_skippable: bool = False,
        window_count: int = 3,
    ) -> None:
        super().__init__()
        self.refreshable: bool = is_rerollable
        self.refreshCount: int = reroll_count
        self.cancelable: bool = is_skippable
        self.windowCount: int = window_count

        self._options: list[Option] = []
        self._show_node_id: str | None = None
        self.Output: MultiSelectMenu._Outputs = self._Outputs(self)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    @property
    def _get_show_node_id(self) -> str:
        if self._show_node_id is None:
            raise RuntimeError(
                "ShowMultipleChoiceMenuNode has not been generated yet. Call menu.show() first."
            )
        return self._show_node_id

    @overload
    def add_option(self, option: Option) -> Option:
        """Adds a pre-instantiated Option object to the menu."""

    @overload
    def add_option(
        self,
        title: str,
        description: str,
        callback: Callable[[], None] | None = None,
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
    ) -> Option:
        """Creates and registers an option card inline."""

    def add_option(self, *args: Any, **kwargs: Any) -> Option:
        """Registers an option card to the menu, supporting both pre-made Option instances and inline configurations."""
        if args and isinstance(args[0], Option):
            opt = args[0]
        elif "option" in kwargs and isinstance(kwargs["option"], Option):
            opt = kwargs["option"]
        else:
            title = args[0] if len(args) > 0 else kwargs.get("title", "")
            description = (
                args[1] if len(args) > 1 else kwargs.get("description", "")
            )
            callback = (
                args[2] if len(args) > 2 else kwargs.get("callback", None)
            )
            plant_type = (
                args[3] if len(args) > 3 else kwargs.get("plant_type", 254)
            )
            zombie_type = (
                args[4] if len(args) > 4 else kwargs.get("zombie_type", -1)
            )

            opt = Option(
                title=title,
                description=description,
                callback=callback,
                plant_type=plant_type,
                zombie_type=zombie_type,
            )

        self._options.append(opt)
        return opt

    def option(
        self,
        title: str,
        description: str,
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
    ) -> _OptionDecorator:
        """Decorator to register a choice callback function inline onto the menu.

        Args:
            title (str): Header title of the option card.
            description (str): Description text of the option card.
            plant_type (int | PlantType): Optional plant icon ID or enum. Defaults to 254.
            zombie_type (int | ZombieType): Optional zombie icon ID or enum. Defaults to -1.

        Returns:
            Callable[[Callable[[], None]], Option]: Decorator capturing the choice logic.
        """

        def decorator(func: Callable[[], None]) -> Option:
            opt = Option(
                title=title,
                description=description,
                callback=func,
                plant_type=plant_type,
                zombie_type=zombie_type,
            )
            self._options.append(opt)
            return opt

        return decorator

    def show(self) -> None:
        """Transpiles all option merge nodes, links the menu window, and attaches it to the execution stream."""
        self._show_node_id = ctx._generate_uuid()
        self._show_node = nodes.ShowMultipleChoiceMenuNode(
            refreshable=self.refreshable,
            refresh_count=self.refreshCount,
            cancelable=self.cancelable,
            window_count=self.windowCount,
            node_id=self._show_node_id,
        )

        current_execution = ctx.trigger_stack[-1]
        ctx.add_connection(
            current_execution.id,
            current_execution.out_trigger,
            self._show_node_id,
            "触发",
        )

        if self._options:
            if len(self._options) == 1:
                ctx.add_connection(
                    self._options[0].node_id,
                    "选项列表",
                    self._show_node_id,
                    "选项列表",
                )
            else:
                first_merge = nodes.merge_multiple_choice_option_lists(
                    list1=self._options[0].output_port,
                    list2=self._options[1].output_port,
                )

                prev_node = first_merge

                for next_opt in self._options[2:]:
                    next_merge = nodes.merge_multiple_choice_option_lists(
                        list1=prev_node.get_output("合并列表"),
                        list2=next_opt.output_port,
                    )
                    prev_node = next_merge

                ctx.add_connection(
                    prev_node.node_id, "合并列表", self._show_node_id, "选项列表"
                )

        ctx.trigger_stack[-1] = ExecutionPath(self._show_node_id, "退出时触发")

    class _Outputs:
        """Execution path outputs from the menu window."""

        def __init__(self, parent: MultiSelectMenu) -> None:
            self._parent = parent

        @property
        def OnExit(self) -> ExecutionPath:
            """Execution path triggered immediately after the menu window closes."""
            return ExecutionPath(self._parent._get_show_node_id, "退出时触发")

        @property
        def OnRefresh(self) -> ExecutionPath:
            """Execution path triggered whenever the player rerolls the option list."""
            return ExecutionPath(self._parent._get_show_node_id, "刷新时触发")

        def on_exit(self) -> ExecutionPath:
            """Execution path triggered immediately after the menu window closes."""
            return self.OnExit

        def on_refresh(self) -> ExecutionPath:
            """Execution path triggered whenever the player rerolls the option list."""
            return self.OnRefresh


class TypedChoiceOption(ExtensionNode):
    """Multiple-choice option card with typed plant/zombie icons."""

    def __init__(
        self,
        title: str = "选项",
        description: str = "",
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
        callback: Optional[Callable[[], None]] = None,
    ) -> None:
        from ...Original.RewardOption.typed_choice_option_node import TypedChoiceOptionNode
        p_val = plant_type.value if isinstance(plant_type, PlantType) else plant_type
        z_val = zombie_type.value if isinstance(zombie_type, ZombieType) else zombie_type

        self.node = TypedChoiceOptionNode(
            title=title,
            description=description,
            plant_type=p_val,
            zombie_type=z_val,
        )
        super().__init__(root_node=self.node)
        self.output_port = self.node.get_output(TypedChoiceOptionNode.OptionList_output_choiceoptions)
        self.on_clicked = ExecutionPath(self.node.node_id, TypedChoiceOptionNode.OnOptionClicked_output_trigger)

        if callback is not None:
            ctx.trigger_stack.append(self.on_clicked)
            try:
                callback()
            finally:
                ctx.trigger_stack.pop()


class TypedChoiceMenu(ExtensionNode):
    """Multiple-choice popup menu rendering typed choices."""

    def __init__(
        self,
        refreshable: bool = False,
        refresh_count: int = 3,
        cancelable: bool = True,
        window_count: int = 3,
    ) -> None:
        super().__init__()
        self.refreshable = refreshable
        self.refresh_count = refresh_count
        self.cancelable = cancelable
        self.window_count = window_count
        self._options: list[TypedChoiceOption] = []
        self._node_id: Optional[str] = None

    def add_option(self, option: TypedChoiceOption) -> TypedChoiceOption:
        self._options.append(option)
        return option

    def show(self) -> None:
        from ...Original.RewardOption.typed_choice_menu_node import TypedChoiceMenuNode
        from ...Original.RewardOption.typed_choice_merge_node import TypedChoiceMergeNode
        self._node_id = ctx._generate_uuid()
        menu_node = TypedChoiceMenuNode(
            refreshable=self.refreshable,
            refresh_count=self.refresh_count,
            cancelable=self.cancelable,
            window_count=self.window_count,
            node_id=self._node_id,
        )
        if ctx.trigger_stack:
            prev = ctx.trigger_stack[-1]
            ctx.add_connection(prev.id, prev.out_trigger, self._node_id, TypedChoiceMenuNode.Trigger_input_trigger)

        if self._options:
            if len(self._options) == 1:
                self._options[0].output_port.connect(menu_node.get_input(TypedChoiceMenuNode.OptionList_input_choiceoptions))
            else:
                prev_port = self._options[0].output_port
                for opt in self._options[1:]:
                    merge_node = TypedChoiceMergeNode()
                    prev_port.connect(merge_node.get_input(TypedChoiceMergeNode.List1_input_choiceoptions))
                    opt.output_port.connect(merge_node.get_input(TypedChoiceMergeNode.List2_input_choiceoptions))
                    prev_port = merge_node.get_output(TypedChoiceMergeNode.MergedList_output_choiceoptions)
                prev_port.connect(menu_node.get_input(TypedChoiceMenuNode.OptionList_input_choiceoptions))

        if ctx.trigger_stack:
            ctx.trigger_stack[-1] = ExecutionPath(self._node_id, TypedChoiceMenuNode.OnExit_output_trigger)

    @property
    def OnExit(self) -> ExecutionPath:
        from ...Original.RewardOption.typed_choice_menu_node import TypedChoiceMenuNode
        return ExecutionPath(self._node_id or "", TypedChoiceMenuNode.OnExit_output_trigger)

    @property
    def OnRefresh(self) -> ExecutionPath:
        from ...Original.RewardOption.typed_choice_menu_node import TypedChoiceMenuNode
        return ExecutionPath(self._node_id or "", TypedChoiceMenuNode.OnRefresh_output_trigger)


__all__ = [
    "Option",
    "MultiSelectMenu",
    "TypedChoiceOption",
    "TypedChoiceMenu",
]

