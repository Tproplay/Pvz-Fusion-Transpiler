"""
Topological Graph Layout Engine for PvZ Fusion Visual Scripting Graphs.
Applies rank layering, dual-lane partitioning (execution vs. data pins),
and collision avoidance to position nodes cleanly on the canvas.
"""

from __future__ import annotations
from collections import defaultdict, deque
from typing import Any, Dict, List, Tuple


class GraphLayoutEngine:
    """Computes readable 2D (X, Y) canvas coordinates for EventNodeGraph nodes."""

    def __init__(
        self,
        node_width: float = 240.0,
        node_height_base: float = 80.0,
        port_height: float = 24.0,
        horizontal_gap: float = 140.0,
        vertical_gap: float = 60.0,
        start_x: float = -800.0,
        start_y: float = 400.0,
    ):
        self.node_width = node_width
        self.node_height_base = node_height_base
        self.port_height = port_height
        self.horizontal_gap = horizontal_gap
        self.vertical_gap = vertical_gap
        self.start_x = start_x
        self.start_y = start_y

    def estimate_node_height(self, node: Any) -> float:
        """Estimates height based on port count."""
        in_count = len(getattr(node, "inputs", {}))
        out_count = len(getattr(node, "outputs", {}))
        ports_count = max(in_count, out_count, 1)
        return self.node_height_base + (ports_count * self.port_height)

    def apply_layout(self, graph: Any) -> None:
        """Calculates and writes position_x and position_y to all nodes in the graph."""
        nodes: List[Any] = graph.nodes
        connections: List[Any] = graph.connections

        if not nodes:
            return

        adj_forward: Dict[str, List[str]] = defaultdict(list)
        adj_backward: Dict[str, List[str]] = defaultdict(list)

        for conn in connections:
            fn_id = conn.fromNodeId
            tn_id = conn.toNodeId
            adj_forward[fn_id].append(tn_id)
            adj_backward[tn_id].append(fn_id)

        # 1. Identify Root nodes (in-degree == 0, prioritize Triggers)
        in_degrees: Dict[str, int] = {n.node_id: len(adj_backward[n.node_id]) for n in nodes}
        ranks: Dict[str, int] = {}

        roots = [n.node_id for n in nodes if in_degrees[n.node_id] == 0]
        if not roots:
            roots = [nodes[0].node_id]

        # 2. Assign topological rank
        queue = deque(roots)
        for r in roots:
            ranks[r] = 0

        while queue:
            curr_id = queue.popleft()
            curr_rank = ranks[curr_id]

            for next_id in adj_forward[curr_id]:
                ranks[next_id] = max(ranks.get(next_id, 0), curr_rank + 1)
                in_degrees[next_id] -= 1
                if in_degrees[next_id] <= 0:
                    queue.append(next_id)

        for n in nodes:
            if n.node_id not in ranks:
                ranks[n.node_id] = 0

        # Group nodes by rank
        rank_groups: Dict[int, List[Any]] = defaultdict(list)
        for n in nodes:
            rank_groups[ranks[n.node_id]].append(n)

        min_rank = min(ranks.values()) if ranks else 0
        sorted_ranks = sorted(rank_groups.keys())

        # 3. Position nodes per rank column
        for r in sorted_ranks:
            group = rank_groups[r]
            exec_nodes = []
            data_nodes = []
            for n in group:
                ntype = getattr(n, "node_type", "")
                is_exec = (
                    "Node" in ntype and any(k in ntype for k in ("On", "Set", "Do", "Wait", "Loop", "Branch", "Play", "Damage", "Move", "Create", "Shoot", "Die", "Kill"))
                    or any(getattr(p, "is_trigger", False) for p in getattr(n, "outputs", {}).values())
                )
                if is_exec:
                    exec_nodes.append(n)
                else:
                    data_nodes.append(n)

            current_y = self.start_y
            col_x = self.start_x + ((r - min_rank) * (self.node_width + self.horizontal_gap))

            # Main execution flow (upper lane)
            for en in exec_nodes:
                en.position_x = float(col_x)
                en.position_y = float(current_y)
                current_y -= (self.estimate_node_height(en) + self.vertical_gap)

            # Data nodes (lower lane)
            current_y -= self.vertical_gap
            for dn in data_nodes:
                dn.position_x = float(col_x)
                dn.position_y = float(current_y)
                current_y -= (self.estimate_node_height(dn) + self.vertical_gap)
