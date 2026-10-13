"""
Transpiler Compiler Pipeline for PvZ Fusion / PvzRH Level Visual Scripting.
"""

from __future__ import annotations

import json
import os
from typing import Any, Callable, Dict, Optional, Union

from .connection import Connection
from .graph import EventNodeGraph
from .group import NodeGroup
from .layout import GraphLayoutEngine
from .level import Level
from .registry import SymbolRegistry
from ..Utils.Optimizer import GraphOptimizer


class Compiler:
    """Orchestrates compilation, layout, optimization passes, and file export."""

    def __init__(
        self,
        auto_layout: bool = True,
        optimize: bool = True,
        start_rid: int = 1000,
    ):
        self.auto_layout = auto_layout
        self.optimize = optimize
        self.start_rid = start_rid
        self.layout_engine = GraphLayoutEngine()
        self.optimizer = GraphOptimizer()

    def _update_group_bounds(self, level: Level) -> None:
        """Computes bounding boxes (position and size) for NodeGroups based on contained nodes."""
        nodes_by_id = {n.node_id: n for n in level.graph.nodes if hasattr(n, "node_id")}
        for grp in level.graph.groups:
            node_ids = getattr(grp, "node_ids", None)
            if node_ids is None and isinstance(grp, dict):
                node_ids = grp.get("nodeIds", [])
            if not node_ids:
                continue

            grp_nodes = [nodes_by_id[nid] for nid in node_ids if nid in nodes_by_id]
            if not grp_nodes:
                continue

            xs = []
            ys = []
            for n in grp_nodes:
                px = getattr(n, "position_x", None)
                py = getattr(n, "position_y", None)
                if px is not None and py is not None:
                    w = getattr(n, "width", 220.0)
                    h = getattr(n, "height", None) or self.layout_engine.estimate_node_height(n)
                    xs.extend([px, px + w])
                    ys.extend([py - h, py])

            if xs and ys:
                min_x = min(xs)
                max_x = max(xs)
                min_y = min(ys)
                max_y = max(ys)
                pad_x = 40.0
                pad_y = 40.0
                center_x = (min_x + max_x) / 2.0
                center_y = (min_y + max_y) / 2.0
                width = max(max_x - min_x + pad_x * 2, 280.0)
                height = max(max_y - min_y + pad_y * 2, 160.0)

                if hasattr(grp, "position"):
                    grp.position = {"x": float(center_x), "y": float(center_y)}
                    grp.size = {"x": float(width), "y": float(height)}
                elif isinstance(grp, dict):
                    grp["position"] = {"x": float(center_x), "y": float(center_y)}
                    grp["size"] = {"x": float(width), "y": float(height)}

    def compile(self, level: Level) -> Dict[str, Any]:
        """Lowers and validates a Level instance into complete Unity level JSON."""
        # 1. Run optimization passes
        if self.optimize:
            self.optimizer.optimize(level.graph)

        # 2. Run automated layout engine
        if self.auto_layout:
            from .context import ctx
            st = getattr(self, "settings", None) or (ctx.settings if ctx else None)
            self.layout_engine.apply_layout(level.graph, settings=st)


        # 3. Update group bounding boxes to surround member nodes
        self._update_group_bounds(level)

        # 4. Export complete level document
        return level.to_dict()

    def compile_to_file(self, level: Level, output_path: str, indent: int = 4) -> str:
        """Compiles and writes level output to file."""
        data = self.compile(level)
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
        return output_path

    @staticmethod
    def decompile(json_filepath: str) -> Level:
        """Parses an existing level JSON file back into an inspectable Level object."""
        return Level.load(json_filepath)
