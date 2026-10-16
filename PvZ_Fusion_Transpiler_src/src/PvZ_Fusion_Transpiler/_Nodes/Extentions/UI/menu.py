from __future__ import annotations

from typing import Any, Callable, List, Optional, TypeAlias, overload
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self  # type: ignore
from ....Core.context import _ctx
from ..Abstract.execution_path import ExecutionPath
from ....Data.TypeMgr import PlantType, ZombieType
from .... import nodes


class Option:
    """Standalone multiple-choice option card.

    Instantiates an option node and compiles its callback graph once for reuse
    across multiple menus.
    """

    def __init__(
        self,
        title: str,
        description: str,
        callback: Optional[Callable[[], None]] = None,
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
            z_val = -1
        elif p_val == -1 and z_val == -1:
            p_val = 254

        self.title: str = title
        self.description: str = description
        self.callback: Optional[Callable[[], None]] = callback
        self.plant_type: int = p_val
        self.zombie_type: int = z_val

        self.node = nodes.add_multiple_choice_option(
            title=self.title,
            description=self.description,
            plant_type=self.plant_type,
            zombie_type=self.zombie_type,
        )
        self.node_id: str = self.node.id

        if self.callback:
            saved_stack = _ctx.trigger_stack[:]
            _ctx.trigger_stack.clear()
            _ctx.trigger_stack.append(ExecutionPath(self.node.port_output_trigger_OnOptionClicked))
            try:
                self.callback()
            finally:
                _ctx.trigger_stack.clear()
                _ctx.trigger_stack.extend(saved_stack)

    @property
    def output_port(self) -> Any:
        return self.node.port_output_choiceoptions_OptionList

    def _get_primary_port(self) -> Any:
        return self.output_port


class MultiSelectMenu:
    """Deferred UI builder for pop-up selection windows.

    Collects multiple `Option` cards, merges them into an option list graph, and displays
    a selection window during gameplay.
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
        self.refreshable: bool = is_rerollable
        self.refreshCount: int = reroll_count
        self.cancelable: bool = is_skippable
        self.windowCount: int = window_count

        self._options: List[Option] = []
        self._show_node_id: Optional[str] = None
        self.node: Any = None
        self.Output: MultiSelectMenu._Outputs = self._Outputs(self)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass

    @property
    def _get_show_node_id(self) -> str:
        if self._show_node_id is None:
            raise RuntimeError(
                "ShowMultipleChoiceMenuNode has not been generated yet. Call menu.show() first."
            )
        return self._show_node_id

    @overload
    def add_option(self, option: Option) -> Option: ...

    @overload
    def add_option(
        self,
        title: str,
        description: str,
        callback: Optional[Callable[[], None]] = None,
        plant_type: int | PlantType = 254,
        zombie_type: int | ZombieType = -1,
    ) -> Option: ...

    def add_option(self, *args: Any, **kwargs: Any) -> Option:
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
        self.node = nodes.show_multiple_choice_menu()
        self.node.refreshable = self.refreshable
        self.node.refreshCount = self.refreshCount
        self.node.cancelable = self.cancelable
        self.node.windowCount = self.windowCount
        self._show_node_id = self.node.id

        if _ctx.trigger_stack:
            current_execution = _ctx.trigger_stack[-1]
            prev_id = getattr(current_execution, "id", str(current_execution))
            prev_trig = getattr(current_execution, "out_trigger", "触发")
            _ctx.add_connection(
                prev_id,
                prev_trig,
                self._show_node_id,
                "触发",
            )

        if self._options:
            if len(self._options) == 1:
                _ctx.add_connection(
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
                prev_port = first_merge.port_output_choiceoptions_MergedList

                for next_opt in self._options[2:]:
                    next_merge = nodes.merge_multiple_choice_option_lists(
                        list1=prev_port,
                        list2=next_opt.output_port,
                    )
                    prev_port = next_merge.port_output_choiceoptions_MergedList

                prev_port.connect(self.node.port_input_choiceoptions_OptionList)

        if _ctx.trigger_stack and self.node is not None:
            _ctx.trigger_stack[-1] = ExecutionPath(self.node.port_output_trigger_OnExit)

    class _Outputs:
        def __init__(self, parent: MultiSelectMenu) -> None:
            self._parent = parent

        @property
        def OnExit(self) -> ExecutionPath:
            return ExecutionPath(self._parent.node.port_output_trigger_OnExit)

        @property
        def OnRefresh(self) -> ExecutionPath:
            return ExecutionPath(self._parent.node.port_output_trigger_OnRefresh)

        def on_exit(self) -> ExecutionPath:
            return self.OnExit

        def on_refresh(self) -> ExecutionPath:
            return self.OnRefresh


__all__ = ["Option", "MultiSelectMenu"]
