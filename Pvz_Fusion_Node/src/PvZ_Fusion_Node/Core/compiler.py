"""
Transpiler Compiler Pipeline for PvZ Fusion / PvzRH Level Visual Scripting.
"""

from __future__ import annotations
import json
import os
from typing import Any, Callable, Dict, Optional, Union

try:
    from .connection import Connection
    from .graph import EventNodeGraph
    from .layout import GraphLayoutEngine
    from .level import Level
    from .registry import SymbolRegistry
except (ImportError, ValueError):
    from connection import Connection
    from graph import EventNodeGraph
    from layout import GraphLayoutEngine
    from level import Level
    from registry import SymbolRegistry

try:
    from ..Utils.Optimizer import GraphOptimizer
except (ImportError, ValueError):
    try:
        from Utils.Optimizer import GraphOptimizer
    except (ImportError, ValueError):
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

    def compile(self, level: Level) -> Dict[str, Any]:
        """Lowers and validates a Level instance into complete Unity level JSON."""
        # 1. Run optimization passes
        if self.optimize:
            self.optimizer.optimize(level.graph)

        # 2. Run automated layout engine
        if self.auto_layout:
            self.layout_engine.apply_layout(level.graph)

        # 3. Export complete level document
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
