"""
Execution Context, CompilerState, and Flow Scoping for PvZ Fusion Node Transpiler.
"""

from __future__ import annotations

import atexit
import inspect
import os
import sys
import uuid
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Union

from .connection import Connection
from .group import NodeGroup
from .level import Level
from .compiler import Compiler
from .connection_mgr import ConnectionMgr
from .node_mgr import NodeMgr


class CompilerSetting:
    """Configures layout, spacing, and grouping behavior for exported node graphs."""

    group_level: int = 0
    fold_all_groups: bool = False
    advanced_formatting: bool = False
    spacing_x: float = 220.0
    spacing_y: float = 170.0
    hierarchical_spacing_x: float = 240.0
    hierarchical_spacing_y: float = 180.0


settings = CompilerSetting()


class ExecutionPath:
    """Represents an active outgoing execution pin on a node for block scoping."""

    def __init__(self, parent_id: str, out_trigger: str):
        self.id = parent_id
        self.out_trigger = out_trigger

    def __enter__(self) -> ExecutionPath:
        ctx.trigger_stack.append(self)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if ctx.trigger_stack and ctx.trigger_stack[-1] is self:
            ctx.trigger_stack.pop()


class PathAccessor:
    """Exposes node trigger outputs as friendly camelCase / TitleCase attributes."""

    def __init__(self, node: Any):
        self._node = node

    def __getattr__(self, name: str) -> ExecutionPath:
        # Check node's port mapping
        port_name = self._node.resolve_port_name(name) if hasattr(self._node, "resolve_port_name") else name
        return self._node.path(port_name) if hasattr(self._node, "path") else ExecutionPath(self._node.node_id, port_name)


class CompilerContext:
    """Singleton compiler state managing active level, execution stacks, and export settings."""

    _instance: Optional[CompilerContext] = None

    def __init__(self) -> None:
        self.config: Dict[str, Any] = {"output": "./Levels", "name": "CustomLevel"}
        self.settings: CompilerSetting = settings
        self.trigger_stack: List[Any] = []
        self.groups_map: Dict[str, Dict[str, Any]] = {}
        self._file_cache: Dict[str, List[str]] = {}
        self._has_registered_atexit: bool = False
        self._level: Level = Level(name="CustomLevel")
        NodeMgr.set_active(self._level.graph.node_mgr)
        ConnectionMgr.set_active(self._level.graph.connection_mgr)

    def reset(self) -> None:
        """Resets the context for a new level compilation."""
        self.config = {"output": "./Levels", "name": "CustomLevel"}
        self.trigger_stack.clear()
        self.groups_map.clear()
        self._level = Level(name="CustomLevel")
        NodeMgr.set_active(self._level.graph.node_mgr)
        ConnectionMgr.set_active(self._level.graph.connection_mgr)

    @classmethod
    def get_instance(cls) -> CompilerContext:
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def level(self) -> Level:
        if self._level is None:
            self._level = Level(name=self.config.get("name", "CustomLevel"))
            NodeMgr.set_active(self._level.graph.node_mgr)
            ConnectionMgr.set_active(self._level.graph.connection_mgr)
        return self._level

    @level.setter
    def level(self, lvl: Level) -> None:
        self._level = lvl
        NodeMgr.set_active(lvl.graph.node_mgr)
        ConnectionMgr.set_active(lvl.graph.connection_mgr)

    def set_active_level(self, lvl: Level) -> None:
        self.level = lvl

    def get_active_level(self) -> Level:
        return self.level

    def add_connection(
        self,
        from_node: Any,
        from_port: Union[str, Any],
        to_node: Any,
        to_port: Union[str, Any],
    ) -> Connection:
        return self.level.connect(from_node, from_port, to_node, to_port)

    def add_node(self, node: Any) -> Any:
        return self.level.add_node(node)

    def generate_uuid(self) -> str:
        return str(uuid.uuid4())

    _generate_uuid = generate_uuid

    def record_node_group(self, node: Any) -> None:
        """Inspects caller frame to associate node with a visual group if group_level >= 1."""
        if self.settings.group_level < 1:
            return

        target_line = None
        user_frame_info = None

        for frame_info in inspect.stack():
            filename = frame_info.filename
            if not any(pkg in filename for pkg in ["PvZ_Fusion_Node", "PvzRH_node"]):
                user_frame_info = frame_info
                break

        if user_frame_info:
            filename = user_frame_info.filename
            lineno = user_frame_info.lineno

            if filename not in self._file_cache:
                try:
                    with open(filename, "r", encoding="utf-8") as f:
                        self._file_cache[filename] = f.readlines()
                except Exception:
                    self._file_cache[filename] = []

            lines = self._file_cache[filename]
            idx = lineno - 1
            if 0 <= idx < len(lines):
                target_line = lines[idx].strip()

        if not target_line:
            target_line = "Script Logic"

        if target_line not in self.groups_map:
            self.groups_map[target_line] = {
                "groupId": self.generate_uuid(),
                "nodeIds": [],
                "position": {"x": 0.0, "y": 0.0},
                "title": target_line,
                "isFolded": self.settings.fold_all_groups,
            }

        node_id = getattr(node, "node_id", str(node))
        if node_id not in self.groups_map[target_line]["nodeIds"]:
            self.groups_map[target_line]["nodeIds"].append(node_id)

    def export(self, filepath: Optional[str] = None) -> Optional[str]:
        """Compiles and exports the active level if nodes exist."""
        if self._level is None or len(self._level.graph.nodes) == 0:
            return None

        # Transfer groups to graph
        if self.groups_map:
            existing_group_ids = {
                (g.group_id if hasattr(g, "group_id") else g.get("groupId"))
                for g in self._level.graph.groups
            }
            for grp in self.groups_map.values():
                node_ids = grp.get("nodeIds") if isinstance(grp, dict) else getattr(grp, "node_ids", [])
                if not node_ids:
                    continue
                gid = grp.get("groupId") if isinstance(grp, dict) else getattr(grp, "group_id", None)
                if gid not in existing_group_ids:
                    node_group = NodeGroup.from_dict(grp) if isinstance(grp, dict) else grp
                    self._level.graph.groups.append(node_group)
                    if gid:
                        existing_group_ids.add(gid)

        # Determine target file
        if not filepath:
            out_dir = self.config.get("output", "./Levels")
            lvl_name = self.config.get("name", self._level.name)
            if not lvl_name.endswith(".json"):
                lvl_name += ".json"
            filepath = os.path.join(out_dir, lvl_name)

        compiler = Compiler(auto_layout=True, optimize=True)
        return compiler.compile_to_file(self._level, filepath)


ctx = CompilerContext.get_instance()


def _to_json_val(val: Any) -> Any:
    if hasattr(val, "value"):
        return _to_json_val(val.value)
    if isinstance(val, dict):
        return {k: _to_json_val(v) for k, v in val.items()}
    if isinstance(val, (list, tuple, set)):
        return [_to_json_val(v) for v in val]
    return val


class LevelConfigProxy:
    """Proxy object providing fluent access to Level metadata and board configurations."""

    @property
    def level(self) -> Level:
        return ctx.level

    @property
    def board_config(self) -> Any:
        return self.level.boardConfig

    @property
    def board_tag(self) -> Any:
        return self.level.boardTag

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ("level", "board_config", "board_tag"):
            super().__setattr__(name, value)
            return
        val = _to_json_val(value)
        alias_map = {
            "level_number": "levelNumber",
            "level_type": "levelType",
            "scene_type": "sceneType",
            "start_sun": "startSun",
            "max_wave": "maxWave",
            "card_count": "cardCount",
            "victory_type": "victoryType",
            "pre_select_cards": "preSelectCards",
            "pre_select_cards_zombie": "preSelectCards_zombie",
            "spawn_zombies": "SpawnZombies",
            "ordered_spawns": "orderedSpawns",
            "plant_datas": "plantDatas",
        }
        target_name = alias_map.get(name, name)
        setattr(self.level, target_name, val)

    def __getattr__(self, name: str) -> Any:
        alias_map = {
            "level_number": "levelNumber",
            "level_type": "levelType",
            "scene_type": "sceneType",
            "start_sun": "startSun",
            "max_wave": "maxWave",
            "card_count": "cardCount",
            "victory_type": "victoryType",
            "pre_select_cards": "preSelectCards",
            "pre_select_cards_zombie": "preSelectCards_zombie",
            "spawn_zombies": "SpawnZombies",
            "ordered_spawns": "orderedSpawns",
            "plant_datas": "plantDatas",
        }
        target_name = alias_map.get(name, name)
        if hasattr(self.level, target_name):
            return getattr(self.level, target_name)
        raise AttributeError(f"'LevelConfigProxy' has no attribute '{name}'")

    def add_plant(self, plant_entry: Any) -> None:
        self.level.plants.append(_to_json_val(plant_entry))

    def add_plant_data(self, plant_data: Any) -> None:
        self.level.plantDatas.append(_to_json_val(plant_data))

    def add_ordered_spawn(self, spawn_entry: Any) -> None:
        self.level.orderedSpawns.append(_to_json_val(spawn_entry))


level_config = LevelConfigProxy()
ctx.level_config = level_config


def Config(output: str = "./Levels", name: str = "CustomLevel", **kwargs: Any) -> None:
    """Configures destination directory and level properties for compilation."""
    ctx.config["output"] = output
    ctx.config["name"] = name
    ctx.level.name = name

    for k, v in kwargs.items():
        if hasattr(ctx.level, k):
            setattr(ctx.level, k, v)


def add_graph(*funcs: Callable[[], Any]) -> None:
    """Executes graph-generating functions sequentially."""
    for f in funcs:
        f()


class IsolatedTriggerScope:
    """Context manager that temporarily isolates the active trigger stack."""

    def __enter__(self) -> IsolatedTriggerScope:
        self.saved_stack = ctx.trigger_stack[:]
        ctx.trigger_stack.clear()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        ctx.trigger_stack.clear()
        ctx.trigger_stack.extend(self.saved_stack)


def single_group(name: Optional[str] = None, folded: Optional[bool] = None) -> Callable:
    """Decorator to encapsulate all nodes created in a function into a dedicated visual group."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            lvl = ctx.level
            start_nodes = len(lvl.graph.nodes)
            res = func(*args, **kwargs)
            end_nodes = len(lvl.graph.nodes)

            if end_nodes > start_nodes:
                group_name = name or func.__name__
                is_folded = folded if folded is not None else ctx.settings.fold_all_groups

                if group_name not in ctx.groups_map:
                    ctx.groups_map[group_name] = {
                        "groupId": ctx.generate_uuid(),
                        "title": group_name,
                        "nodeIds": [],
                        "position": {"x": 0.0, "y": 0.0},
                        "isFolded": is_folded,
                    }

                new_node_ids = [n.node_id for n in lvl.graph.nodes[start_nodes:end_nodes]]
                # Remove from other groups
                for g_title, grp in ctx.groups_map.items():
                    if g_title != group_name:
                        grp["nodeIds"] = [nid for nid in grp["nodeIds"] if nid not in new_node_ids]

                ctx.groups_map[group_name]["nodeIds"].extend(new_node_ids)

            return res

        return wrapper

    return decorator


# Auto-register export upon clean script exit
def _auto_export():
    try:
        ctx.export()
    except Exception as e:
        # Don't silence catastrophic failures, but avoid masking script crashes
        pass

atexit.register(_auto_export)
