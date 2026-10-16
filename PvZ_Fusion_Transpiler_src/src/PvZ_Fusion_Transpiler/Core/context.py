from __future__ import annotations

import atexit
import json
import math
import os
import sys
import uuid
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set

from .connection_manager import ConnectionManager, Connection, Port

if TYPE_CHECKING:
    from .._Nodes.Original.node import Node


def apply_square_layout(
    nodes: List[Any],
    start_x: float = -800.0,
    start_y: float = 400.0,
    spacing_x: float = 240.0,
    spacing_y: float = 160.0,
) -> None:
    """Arranges nodes in a square pattern (ceil(sqrt(N)) columns)."""
    if not nodes:
        return

    # If any node has a non-zero position set by the user, preserve user layout
    if any(getattr(n, "x", 0.0) != 0.0 or getattr(n, "y", 0.0) != 0.0 for n in nodes):
        return

    N = len(nodes)
    cols = math.ceil(math.sqrt(N)) if N > 0 else 1
    for idx, node in enumerate(nodes):
        c = idx % cols
        r = idx // cols
        node.x = float(start_x + c * spacing_x)
        node.y = float(start_y - r * spacing_y)


class CompilerContext:
    """Global compilation context managing configuration, nodes, and export."""

    def __init__(self) -> None:
        self.config: Dict[str, Any] = {
            "output": "./",
            "name": "Untitled",
        }
        self.nodes: List[Any] = []
        self._node_set: Set[str] = set()
        self._node_map: Dict[str, Any] = {}
        self.variables: List[Any] = []
        self._variable_set: Set[str] = set()
        self.trigger_stack: List[Any] = []
        self._configured: bool = False
        self._exported_file: Optional[str] = None

    def _generate_uuid(self) -> str:
        return uuid.uuid4().hex

    def get_node(self, node_id: str) -> Optional[Any]:
        return self._node_map.get(node_id)

    def add_node(self, node: Any) -> None:
        node_id = getattr(node, "id", None)
        if node_id:
            self._node_map[node_id] = node
            if node_id not in self._node_set:
                self._node_set.add(node_id)
                self.nodes.append(node)
        elif node not in self.nodes:
            self.nodes.append(node)

    def add_variable(self, var: Any) -> None:
        vid = getattr(var, "variable_id", None)
        if vid and vid not in self._variable_set:
            self._variable_set.add(vid)
            self.variables.append(var)
        elif not vid and var not in self.variables:
            self.variables.append(var)

    def add_connection(
        self,
        source: Any,
        source_port: Any,
        target: Any,
        target_port: Any,
    ) -> Any:
        src_node = self._node_map.get(source) if isinstance(source, str) else source
        tgt_node = self._node_map.get(target) if isinstance(target, str) else target

        if src_node is not None and tgt_node is not None:
            src_p: Any = source_port
            tgt_p: Any = target_port
            if isinstance(source_port, str) and hasattr(src_node, "get_output"):
                try:
                    src_p = src_node.get_output(source_port)
                except Exception:
                    src_p = src_node.get_port(source_port) if hasattr(src_node, "get_port") else source_port

            if isinstance(target_port, str) and hasattr(tgt_node, "get_input"):
                try:
                    tgt_p = tgt_node.get_input(target_port)
                except Exception:
                    tgt_p = tgt_node.get_port(target_port) if hasattr(tgt_node, "get_port") else target_port

            if isinstance(src_p, Port) and isinstance(tgt_p, Port):
                src_p.connect(tgt_p)
                return
            elif hasattr(src_p, "connect") and tgt_p is not None:
                getattr(src_p, "connect")(tgt_p)
                return
            elif hasattr(tgt_p, "connect") and src_p is not None:
                getattr(tgt_p, "connect")(src_p)
                return

        ConnectionManager.add_connection(src_node or source, source_port, tgt_node or target, target_port)  # type: ignore

    def clear(self) -> None:
        self.config = {
            "output": "./",
            "name": "Untitled",
        }
        self.nodes.clear()
        self._node_set.clear()
        self._node_map.clear()
        self.variables.clear()
        self._variable_set.clear()
        self.trigger_stack.clear()
        self._configured = False
        self._exported_file = None
        ConnectionManager.clear()

    def export(self, filepath: Optional[str] = None) -> Optional[str]:
        """Compiles and exports the level to a JSON file.
        
        If the file exists on the destination, changes its references and eventNodeGraph,
        leaving everything else as it is. If the file doesn't exist, dumps references and eventNodeGraph.
        """
        if filepath is not None:
            target_path = filepath
        else:
            output_dir = self.config.get("output", "./")
            name = self.config.get("name", "Untitled")

            if name.lower().endswith(".json"):
                filename = name
            else:
                filename = f"{name}.json"

            exact_path = os.path.join(output_dir, name)
            json_path = os.path.join(output_dir, filename)

            # Check if exact file without extension exists
            if os.path.isfile(exact_path) and not os.path.isfile(json_path):
                target_path = exact_path
            else:
                target_path = json_path

        # Collect nodes
        all_nodes = list(self.nodes)
        existing_node_ids = {getattr(n, "id", None) for n in all_nodes}

        connections = list(ConnectionManager.get_connections())
        for conn in connections:
            if conn.source_node and getattr(conn.source_node, "id", None) not in existing_node_ids:
                all_nodes.append(conn.source_node)
                existing_node_ids.add(conn.source_node.id)
            if conn.target_node and getattr(conn.target_node, "id", None) not in existing_node_ids:
                all_nodes.append(conn.target_node)
                existing_node_ids.add(conn.target_node.id)

        # Collect variables
        all_variables = list(self.variables)
        existing_var_ids = {getattr(v, "variable_id", None) for v in all_variables}

        for node in all_nodes:
            if hasattr(node, "asset") and getattr(node, "asset") is not None:
                asset_obj = getattr(node, "asset")
                vid = getattr(asset_obj, "variable_id", None)
                if vid and vid not in existing_var_ids:
                    all_variables.append(asset_obj)
                    existing_var_ids.add(vid)
                if hasattr(asset_obj, "add_reference"):
                    asset_obj.add_reference(node.id)

        # Allocate RIDs starting at 1000
        for idx, node in enumerate(all_nodes):
            node.rid = 1000 + idx

        var_start_rid = 1000 + len(all_nodes)
        for idx, var in enumerate(all_variables):
            var.rid = var_start_rid + idx

        # Arrange nodes in a square pattern
        apply_square_layout(all_nodes)

        # Build EventNodeGraph block
        dummy_conn = {
            "sourceNodeId": "",
            "sourcePortName": "",
            "targetNodeId": "",
            "targetPortName": "",
        }
        event_node_graph: Dict[str, Any] = {
            "nodes": [{"rid": n.rid} for n in all_nodes],
            "connections": [dummy_conn] + [c.to_dict() for c in connections],
            "variables": [{"rid": v.rid} for v in all_variables],
            "groups": [],
            "executionVersion": 1,
            "graphId": uuid.uuid4().hex,
        }

        references: Dict[str, Any] = {
            "version": 2,
            "RefIds": [n.dump_ref() for n in all_nodes] + [v.dump_ref() for v in all_variables],
        }

        # If file exists, update references and eventNodeGraph, leave everything else as it is.
        # If file doesn't exist, just dump references and eventNodeGraph.
        if os.path.isfile(target_path):
            with open(target_path, "r", encoding="utf-8") as f:
                level_data = json.load(f)

            if "eventNodeGraph" in level_data and isinstance(level_data["eventNodeGraph"], dict):
                gid = level_data["eventNodeGraph"].get("graphId")
                if gid:
                    event_node_graph["graphId"] = gid
                ev = level_data["eventNodeGraph"].get("executionVersion")
                if ev:
                    event_node_graph["executionVersion"] = ev

            level_data["eventNodeGraph"] = event_node_graph
            level_data["references"] = references
        else:
            level_data = {
                "eventNodeGraph": event_node_graph,
                "references": references,
            }

        os.makedirs(os.path.dirname(os.path.abspath(target_path)), exist_ok=True)
        with open(target_path, "w", encoding="utf-8") as f:
            json.dump(level_data, f, ensure_ascii=False, indent=4)

        self._exported_file = target_path
        return target_path


_ctx = CompilerContext()


def Config(output="./", name="Untitled"):
    """Specify the Output folder and Name.
    If the file already exists, its NodeGraph and Connections will be overwritten."""
    _ctx.config["output"] = output
    _ctx.config["name"] = name
    _ctx._configured = True


def export(filepath: Optional[str] = None) -> Optional[str]:
    """Manually export the current level graph to JSON."""
    return _ctx.export(filepath=filepath)


_script_has_error = False

_orig_excepthook = sys.excepthook

def _custom_excepthook(exc_type, exc_value, exc_traceback):
    global _script_has_error
    _script_has_error = True
    return _orig_excepthook(exc_type, exc_value, exc_traceback)

sys.excepthook = _custom_excepthook


def _auto_export() -> None:
    if _script_has_error:
        return
    # Auto-export if nodes exist, connections exist, or Config was explicitly called
    if len(_ctx.nodes) > 0 or len(ConnectionManager.get_connections()) > 0 or _ctx._configured:
        try:
            _ctx.export()
        except Exception:
            import traceback
            traceback.print_exc()


atexit.register(_auto_export)
