"""
Topological Graph Layout Engine for PvZ Fusion Visual Scripting Graphs.
Provides Dual-Mode Layout:
1. Advanced Formatting (advanced_formatting == True):
   - Isolates Global Constants & Variables into top-left container
   - Partitions non-connected node groups/graphs into distinct blocks
   - Strict left-to-right execution flow (rank ordering)
   - Left-side input providers positioned directly to the left of consumers
   - Tight, compact spacing between connected nodes with barycenter alignment
2. Square Pattern Formatting (advanced_formatting == False):
   - If group_level >= 1: arranges nodes in each group in a square grid (ceil(sqrt(N))),
     and arranges the groups themselves in a square grid (ceil(sqrt(G)))
   - If group_level == 0: arranges all nodes in a single square grid (ceil(sqrt(N)))
"""

from __future__ import annotations
from collections import defaultdict, deque
import math
from typing import Any, Dict, List, Optional, Set, Tuple


class GraphLayoutEngine:
    """Computes readable 2D (X, Y) canvas coordinates for EventNodeGraph nodes."""

    def __init__(
        self,
        node_width: float = 200.0,
        node_height_base: float = 80.0,
        port_height: float = 24.0,
        horizontal_gap: float = 45.0,
        vertical_gap: float = 35.0,
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

    def apply_layout(self, graph: Any, settings: Optional[Any] = None) -> None:
        """Calculates and writes position_x and position_y to all nodes in the graph."""
        nodes: List[Any] = graph.nodes
        if not nodes:
            return

        if settings is None:
            try:
                from .context import ctx
                settings = ctx.settings if ctx else None
            except Exception:
                pass

        advanced = getattr(settings, "advanced_formatting", False)
        if advanced:
            self._layout_advanced_formatting(graph, settings)
        else:
            self._layout_square_pattern(graph, settings)

        self._update_group_bounds(graph)

    def _update_group_bounds(self, graph: Any) -> None:
        """Updates NodeGroup visual boundary positions and sizes."""
        groups = getattr(graph, "groups", [])
        if not groups:
            return
        nodes_by_id = {n.node_id: n for n in graph.nodes if hasattr(n, "node_id")}

        for g in groups:
            nids = getattr(g, "node_ids", None)
            if nids is None and isinstance(g, dict):
                nids = g.get("nodeIds", [])
            gnodes = [nodes_by_id[nid] for nid in nids if nid in nodes_by_id]
            if not gnodes:
                continue

            min_x = min(n.position_x for n in gnodes)
            max_x = max(n.position_x + self.node_width for n in gnodes)
            min_y = min(n.position_y - self.estimate_node_height(n) for n in gnodes)
            max_y = max(n.position_y for n in gnodes)

            padding = 40.0
            width = (max_x - min_x) + 2 * padding
            height = (max_y - min_y) + 2 * padding + 25.0

            center_x = (min_x + max_x) / 2.0
            center_y = (min_y + max_y) / 2.0 + 10.0

            if hasattr(g, "position"):
                g.position = {"x": float(center_x), "y": float(center_y)}
                g.size = {"x": float(width), "y": float(height)}
            elif isinstance(g, dict):
                g["position"] = {"x": float(center_x), "y": float(center_y)}
                g["size"] = {"x": float(width), "y": float(height)}

    def _layout_square_pattern(self, graph: Any, settings: Optional[Any] = None) -> None:
        """Square pattern layout:
        If group_level >= 1, arranges nodes in each group in a square pattern,
        and arranges groups in a square pattern.
        If group_level == 0, arranges all nodes across the canvas in a single square pattern.
        """
        nodes: List[Any] = graph.nodes
        if not nodes:
            return

        group_level = getattr(settings, "group_level", 0) if settings else 0
        spacing_x = getattr(settings, "spacing_x", 240.0) if settings else 240.0
        spacing_y = getattr(settings, "spacing_y", 160.0) if settings else 160.0

        groups = getattr(graph, "groups", [])

        if group_level >= 1 and groups:
            nodes_by_id = {n.node_id: n for n in nodes if hasattr(n, "node_id")}
            grouped_node_ids: Set[str] = set()
            for g in groups:
                nids = getattr(g, "node_ids", None)
                if nids is None and isinstance(g, dict):
                    nids = g.get("nodeIds", [])
                if nids:
                    grouped_node_ids.update(nids)

            ungrouped_nodes = [n for n in nodes if n.node_id not in grouped_node_ids]
            if ungrouped_nodes:
                from .group import NodeGroup
                orphan_grp = NodeGroup(
                    title="Global Constants & Variables",
                    node_ids=[n.node_id for n in ungrouped_nodes],
                )
                groups.insert(0, orphan_grp)

            active_groups = []
            for g in groups:
                nids = getattr(g, "node_ids", None)
                if nids is None and isinstance(g, dict):
                    nids = g.get("nodeIds", [])
                gnodes = [nodes_by_id[nid] for nid in nids if nid in nodes_by_id]
                if gnodes:
                    active_groups.append((g, gnodes))

            if not active_groups:
                self._layout_simple_grid(nodes, spacing_x, spacing_y)
                return

            group_metrics = []
            for g, gnodes in active_groups:
                k = len(gnodes)
                cols = math.ceil(math.sqrt(k))
                rows = math.ceil(k / cols) if cols > 0 else 1
                for idx, n in enumerate(gnodes):
                    c = idx % cols
                    r = idx // cols
                    n._rel_x = c * spacing_x
                    n._rel_y = - r * spacing_y
                gw = max(cols * spacing_x, 260.0)
                gh = max(rows * spacing_y, 160.0)
                group_metrics.append((g, gnodes, gw, gh))

            G = len(group_metrics)
            g_cols = math.ceil(math.sqrt(G))
            g_rows = math.ceil(G / g_cols) if g_cols > 0 else 1

            col_widths = [0.0] * g_cols
            row_heights = [0.0] * g_rows
            for idx, (_, _, gw, gh) in enumerate(group_metrics):
                gc = idx % g_cols
                gr = idx // g_cols
                col_widths[gc] = max(col_widths[gc], gw)
                row_heights[gr] = max(row_heights[gr], gh)

            cum_x = [self.start_x]
            for gc in range(g_cols):
                cum_x.append(cum_x[-1] + col_widths[gc] + 100.0)

            cum_y = [self.start_y]
            for gr in range(g_rows):
                cum_y.append(cum_y[-1] - row_heights[gr] - 100.0)

            for idx, (_, gnodes, _, _) in enumerate(group_metrics):
                gc = idx % g_cols
                gr = idx // g_cols
                gx = cum_x[gc]
                gy = cum_y[gr]
                for n in gnodes:
                    n.position_x = float(gx + getattr(n, "_rel_x", 0.0))
                    n.position_y = float(gy + getattr(n, "_rel_y", 0.0))
        else:
            self._layout_simple_grid(nodes, spacing_x, spacing_y)

    def _layout_simple_grid(self, nodes: List[Any], spacing_x: float, spacing_y: float) -> None:
        """Arranges all nodes in a single square pattern."""
        N = len(nodes)
        cols = math.ceil(math.sqrt(N))
        for idx, n in enumerate(nodes):
            c = idx % cols
            r = idx // cols
            n.position_x = float(self.start_x + c * spacing_x)
            n.position_y = float(self.start_y - r * spacing_y)

    def _layout_advanced_formatting(self, graph: Any, settings: Optional[Any] = None) -> None:
        """Advanced formatting:
        1. Keeps non-connected node groups apart in different blocks.
        2. In each block, execution flows strictly from left to right.
        3. Keeps input providers/constant nodes directly to the left (behind) consumers.
        4. Keeps connected nodes as close to each other as possible.
        """
        nodes: List[Any] = graph.nodes
        connections: List[Any] = graph.connections
        if not nodes:
            return

        nodes_by_id = {n.node_id: n for n in nodes if hasattr(n, "node_id")}

        adj_forward: Dict[str, List[str]] = defaultdict(list)
        adj_backward: Dict[str, List[str]] = defaultdict(list)
        for conn in connections:
            fn = conn.fromNodeId
            tn = conn.toNodeId
            if fn in nodes_by_id and tn in nodes_by_id:
                adj_forward[fn].append(tn)
                adj_backward[tn].append(fn)

        # 1. Identify truly isolated Global Variables / Unconnected Nodes
        global_const_nodes = []
        regular_nodes = []

        for n in nodes:
            nid = n.node_id
            ntype = getattr(n, "node_type", "")
            has_no_outputs = len(adj_forward[nid]) == 0
            has_no_inputs = len(adj_backward[nid]) == 0
            is_var_def = ntype.endswith("VariableNode") and not ntype.startswith("Get") and not ntype.startswith("Set")

            # Only truly isolated/unconnected nodes or standalone variable definitions go to global_const_nodes
            # Any constant node connected to another node MUST stay in regular_nodes!
            if (is_var_def and has_no_outputs and has_no_inputs) or (has_no_outputs and has_no_inputs):
                global_const_nodes.append(n)
            else:
                regular_nodes.append(n)

        current_block_y = self.start_y

        if global_const_nodes:
            gc_cols = min(2, len(global_const_nodes))
            for idx, n in enumerate(global_const_nodes):
                col = idx % gc_cols
                row = idx // gc_cols
                n.position_x = float(self.start_x + col * (self.node_width + self.horizontal_gap))
                n.position_y = float(current_block_y - row * (self.node_height_base + self.vertical_gap))

            gc_rows = math.ceil(len(global_const_nodes) / gc_cols)
            gc_height = gc_rows * (self.node_height_base + self.vertical_gap) + 60.0

            group_level = getattr(settings, "group_level", 0) if settings else 0
            if group_level >= 1 and hasattr(graph, "groups"):
                from .group import NodeGroup
                has_gc_grp = any(
                    (g.title if hasattr(g, "title") else g.get("title", "")) == "Global Constants & Variables"
                    for g in graph.groups
                )
                if not has_gc_grp:
                    gc_grp = NodeGroup(
                        title="Global Constants & Variables",
                        node_ids=[n.node_id for n in global_const_nodes],
                    )
                    graph.groups.insert(0, gc_grp)

            current_block_y -= (gc_height + 80.0)

        if not regular_nodes:
            return

        # 2. Partition regular nodes into weakly connected components
        regular_ids = {n.node_id for n in regular_nodes}
        visited: Set[str] = set()
        components: List[List[Any]] = []

        for rn in regular_nodes:
            nid = rn.node_id
            if nid in visited:
                continue
            comp_nodes = []
            queue = deque([nid])
            visited.add(nid)

            while queue:
                curr = queue.popleft()
                if curr in nodes_by_id:
                    comp_nodes.append(nodes_by_id[curr])
                neighbors = adj_forward[curr] + adj_backward[curr]
                for nbr in neighbors:
                    if nbr in regular_ids and nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)

            components.append(comp_nodes)

        # 3. Layout each component from left to right, stacked vertically
        for comp in components:
            block_height = self._layout_single_component(
                comp,
                adj_forward,
                adj_backward,
                connections,
                start_x=self.start_x,
                start_y=current_block_y,
            )
            current_block_y -= (block_height + 140.0)

    def _layout_single_component(
        self,
        comp_nodes: List[Any],
        adj_forward: Dict[str, List[str]],
        adj_backward: Dict[str, List[str]],
        connections: List[Any],
        start_x: float,
        start_y: float,
    ) -> float:
        comp_ids = {n.node_id for n in comp_nodes}

        local_fwd = {nid: [t for t in adj_forward[nid] if t in comp_ids] for nid in comp_ids}
        local_bwd = {nid: [f for f in adj_backward[nid] if f in comp_ids] for nid in comp_ids}

        self._break_cycles(comp_ids, local_fwd)
        local_bwd = {nid: [] for nid in comp_ids}
        for u, targets in local_fwd.items():
            for v in targets:
                local_bwd[v].append(u)

        in_degrees = {nid: len(local_bwd[nid]) for nid in comp_ids}
        ranks: Dict[str, int] = {}

        roots = [nid for nid in comp_ids if in_degrees[nid] == 0]
        if not roots:
            roots = [comp_nodes[0].node_id]

        queue = deque(roots)
        for r in roots:
            ranks[r] = 0

        while queue:
            curr = queue.popleft()
            curr_rank = ranks[curr]
            for nxt in local_fwd[curr]:
                ranks[nxt] = max(ranks.get(nxt, 0), curr_rank + 1)
                in_degrees[nxt] -= 1
                if in_degrees[nxt] <= 0:
                    queue.append(nxt)

        for nid in comp_ids:
            if nid not in ranks:
                ranks[nid] = 0

        # Adjust data providers: pull them rightward (ALAP) so they are placed
        # directly in the column immediately to the left of their consumers
        TRIGGER_PORTS = {"触发", "完成", "周期事件", "真（触发）", "假（停止）", "循环体", "创建成功", "创建失败"}
        node_has_trigger_input = {}
        for nid in comp_ids:
            has_trig = False
            for conn in connections:
                if getattr(conn, "toNodeId", "") == nid:
                    if getattr(conn, "toPortName", "") in TRIGGER_PORTS or getattr(conn, "fromPortName", "") in TRIGGER_PORTS:
                        has_trig = True
                        break
            node_has_trigger_input[nid] = has_trig

        changed = True
        while changed:
            changed = False
            for nid in comp_ids:
                if not node_has_trigger_input.get(nid, False):
                    consumers = local_fwd[nid]
                    if consumers:
                        min_consumer_rank = min(ranks[c] for c in consumers)
                        target_rank = min_consumer_rank - 1
                        if ranks[nid] < target_rank:
                            ranks[nid] = target_rank
                            changed = True

        min_rank = min(ranks.values()) if ranks else 0
        for nid in ranks:
            ranks[nid] -= min_rank

        max_rank = max(ranks.values()) if ranks else 0

        # Assign initial execution track Y baseline
        exec_y: Dict[str, float] = {}
        trigger_roots = [
            nid for nid in comp_ids
            if not node_has_trigger_input.get(nid, False) and any(
                getattr(conn, "fromNodeId", "") == nid and (getattr(conn, "fromPortName", "") in TRIGGER_PORTS or getattr(conn, "toPortName", "") in TRIGGER_PORTS)
                for conn in connections
            )
        ]
        if not trigger_roots:
            trigger_roots = [nid for nid in comp_ids if ranks[nid] == 0]

        for i, tr in enumerate(trigger_roots):
            exec_y[tr] = start_y - i * 250.0

        # Propagate execution baseline forward along trigger connections
        exec_queue = deque(trigger_roots)
        while exec_queue:
            curr = exec_queue.popleft()
            curr_y = exec_y[curr]
            branch_count = 0
            for conn in connections:
                if getattr(conn, "fromNodeId", "") == curr and getattr(conn, "toNodeId", "") in comp_ids:
                    target_id = getattr(conn, "toNodeId", "")
                    from_p = getattr(conn, "fromPortName", "")
                    to_p = getattr(conn, "toPortName", "")
                    if from_p in TRIGGER_PORTS or to_p in TRIGGER_PORTS:
                        if target_id not in exec_y:
                            if from_p in ("假（停止）", "创建失败"):
                                exec_y[target_id] = curr_y - 140.0
                            elif branch_count > 0:
                                exec_y[target_id] = curr_y - branch_count * 140.0
                            else:
                                exec_y[target_id] = curr_y
                            branch_count += 1
                            exec_queue.append(target_id)

        # Backward propagation of ideal Y for data providers
        ideal_y: Dict[str, float] = dict(exec_y)
        for r in range(max_rank, -1, -1):
            nodes_in_r = [n for n in comp_nodes if ranks[n.node_id] == r]
            for n in nodes_in_r:
                nid = n.node_id
                if nid not in ideal_y:
                    higher_consumers = [c for c in local_fwd[nid] if ranks[c] > r and c in ideal_y]
                    if higher_consumers:
                        ideal_y[nid] = sum(ideal_y[c] for c in higher_consumers) / len(higher_consumers)
                    else:
                        ideal_y[nid] = start_y

        # Place nodes column by column
        rank_columns: Dict[int, List[Any]] = defaultdict(list)
        for n in comp_nodes:
            rank_columns[ranks[n.node_id]].append(n)

        min_comp_y = start_y

        for r in range(max_rank + 1):
            col_nodes = rank_columns[r]
            if not col_nodes:
                continue

            col_x = start_x + r * (self.node_width + self.horizontal_gap)

            col_nodes.sort(
                key=lambda n: (
                    1 if n.node_id in exec_y else 0,
                    ideal_y.get(n.node_id, start_y)
                ),
                reverse=True
            )

            for idx, n in enumerate(col_nodes):
                target_y = ideal_y.get(n.node_id, start_y)
                if idx == 0:
                    n.position_y = float(target_y)
                else:
                    prev_n = col_nodes[idx - 1]
                    prev_h = self.estimate_node_height(prev_n)
                    min_allowed_y = prev_n.position_y - (prev_h + self.vertical_gap)
                    n.position_y = float(min(target_y, min_allowed_y))

                n.position_x = float(col_x)
                ideal_y[n.node_id] = n.position_y

                node_bottom = n.position_y - self.estimate_node_height(n)
                if node_bottom < min_comp_y:
                    min_comp_y = node_bottom

        return max(start_y - min_comp_y, 120.0)

    def _break_cycles(self, node_ids: Set[str], adj: Dict[str, List[str]]) -> None:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {nid: WHITE for nid in node_ids}

        def dfs(u: str) -> None:
            color[u] = GRAY
            for v in list(adj.get(u, [])):
                if v in color:
                    if color[v] == GRAY:
                        adj[u].remove(v)
                    elif color[v] == WHITE:
                        dfs(v)
            color[u] = BLACK

        for nid in node_ids:
            if color[nid] == WHITE:
                dfs(nid)

