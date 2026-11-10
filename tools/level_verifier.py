#!/usr/bin/env python3
"""Automated Level Graph Verification and Optimization Analysis System.

Validates transpiled node graphs against exported PvZ Fusion level JSON files,
ensuring all nodes, connections, port wirings, and optimization semantics match.
"""

from __future__ import annotations

import contextlib
import io
import json
import math
import os
import re
import sys
import tempfile
import unittest
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, Iterator, List, Optional, Sequence, Set, Tuple, Union

# Ensure workspace and src are in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = REPO_ROOT / "PvZ_Fusion_Transpiler_src" / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from PvZ_Fusion_Transpiler.Core import _ctx
from PvZ_Fusion_Transpiler.Core.connection_manager import Connection, ConnectionManager, PortDirection


IGNORED_PAYLOAD_KEYS = {
    "inputDefaults",
    "nodeId",
    "id",
    "nodeType",
    "position",
    "nodeName",
    "m_Position",
    "m_Name",
    "m_InputDefaults",
    "m_NodeType",
    "m_ExecutionPath",
}


def _clean_payload(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract semantic payload fields, filtering layout and reflection metadata."""
    cleaned: Dict[str, Any] = {}
    for key, val in raw_data.items():
        if key in IGNORED_PAYLOAD_KEYS:
            continue
        if key.endswith("_PortName") or key.startswith("port_"):
            continue
        cleaned[key] = val
    return cleaned


def _values_match(v1: Any, v2: Any) -> bool:
    """Compare two payload values with float tolerance and recursive dict/list comparison."""
    if v1 is None and v2 is None:
        return True
    if v1 is None or v2 is None:
        return False
    if isinstance(v1, bool) or isinstance(v2, bool):
        return type(v1) is type(v2) and v1 == v2
    if isinstance(v1, (int, float)) and isinstance(v2, (int, float)):
        return math.isclose(float(v1), float(v2), rel_tol=1e-5, abs_tol=1e-5)
    if isinstance(v1, dict) and isinstance(v2, dict):
        if set(v1.keys()) != set(v2.keys()):
            return False
        return all(_values_match(v1[k], v2[k]) for k in v1)
    if isinstance(v1, list) and isinstance(v2, list):
        if len(v1) != len(v2):
            return False
        return all(_values_match(a, b) for a, b in zip(v1, v2))
    return bool(v1 == v2)


@dataclass
class GraphNode:
    """Semantic representation of a node in a level graph."""
    id: str
    node_type: str
    payload: Dict[str, Any] = field(default_factory=dict)
    rid: Optional[int] = None
    input_ports: Set[str] = field(default_factory=set)
    output_ports: Set[str] = field(default_factory=set)

    def matches(self, other: GraphNode, check_payload: bool = True) -> bool:
        if self.node_type != other.node_type:
            return False
        if not check_payload:
            return True
        keys = set(self.payload.keys()) | set(other.payload.keys())
        for k in keys:
            if not _values_match(self.payload.get(k), other.payload.get(k)):
                return False
        return True

    def format_summary(self) -> str:
        fields = ", ".join(f"{k}={v!r}" for k, v in sorted(self.payload.items()))
        return f"{self.node_type}({fields})" if fields else self.node_type


@dataclass(frozen=True)
class GraphConnection:
    """Semantic directed wire between two nodes and their ports."""
    source_id: str
    source_port: str
    target_id: str
    target_port: str

    def format_with_types(self, nodes: Dict[str, GraphNode]) -> str:
        src_name = nodes[self.source_id].node_type if self.source_id in nodes else self.source_id
        tgt_name = nodes[self.target_id].node_type if self.target_id in nodes else self.target_id
        return f"{src_name}[{self.source_port!r}] -> {tgt_name}[{self.target_port!r}]"


@dataclass
class OptimizationFinding:
    """A finding regarding graph cleanliness, dead code, or optimization opportunities."""
    kind: str  # e.g. "FLOATING_NODE", "DEAD_PORT", "REDUNDANT_CONSTANT", "UNREACHED_NODE"
    message: str
    node_id: Optional[str] = None


class LevelGraph:
    """Normalized, UUID-independent representation of a level node graph."""

    def __init__(
        self,
        nodes: Optional[Dict[str, GraphNode]] = None,
        connections: Optional[List[GraphConnection]] = None,
        variables: Optional[List[Dict[str, Any]]] = None,
        source_desc: str = "Unknown",
    ) -> None:
        self.nodes: Dict[str, GraphNode] = nodes or {}
        self.connections: List[GraphConnection] = connections or []
        self.variables: List[Dict[str, Any]] = variables or []
        self.source_desc: str = source_desc

    @classmethod
    def from_json_dict(cls, data: Dict[str, Any], source_desc: str = "JSON Dict") -> LevelGraph:
        ref_ids = data.get("references", {}).get("RefIds", [])
        var_rids = {
            v.get("rid")
            for v in data.get("eventNodeGraph", {}).get("variables", [])
            if isinstance(v, dict) and v.get("rid") is not None
        }

        # Pass 1: Separate VariableAsset records by rid
        vars_by_rid: Dict[int, Dict[str, Any]] = {}
        variables_list: List[Dict[str, Any]] = []
        for item in ref_ids:
            rid = item.get("rid")
            data_block = item.get("data", {})
            raw_type = data_block.get("nodeType")
            if not raw_type and "type" in item:
                t = item["type"]
                raw_type = t.get("class") if isinstance(t, dict) else str(t).split(".")[-1]
            type_str = str(raw_type or "")

            if (rid is not None and rid in var_rids) or type_str.endswith("VariableAsset") or "variableId" in data_block:
                var_info = {
                    "type": type_str,
                    "name": data_block.get("name"),
                    "value": data_block.get("value"),
                }
                if rid is not None:
                    vars_by_rid[rid] = var_info
                variables_list.append(var_info)

        # Pass 2: Extract actual GraphNodes and resolve variable asset links
        nodes: Dict[str, GraphNode] = {}
        for item in ref_ids:
            rid = item.get("rid")
            if rid is not None and rid in vars_by_rid:
                continue
            data_block = item.get("data", {})
            raw_type = data_block.get("nodeType")
            if not raw_type and "type" in item:
                t = item["type"]
                raw_type = t.get("class") if isinstance(t, dict) else str(t).split(".")[-1]
            node_type = str(raw_type or "UnknownNode")
            if node_type.endswith("VariableAsset") or "variableId" in data_block:
                continue

            nid = data_block.get("nodeId") or data_block.get("id") or str(rid)
            payload = _clean_payload(data_block)

            # Resolve {"rid": X} asset link into semantic asset descriptor
            asset_ref = payload.get("asset")
            if isinstance(asset_ref, dict) and asset_ref.get("rid") in vars_by_rid:
                payload["asset"] = vars_by_rid[asset_ref["rid"]]

            in_ports: Set[str] = set()
            out_ports: Set[str] = set()
            for k, v in data_block.items():
                if k.endswith("_PortName") and isinstance(v, str):
                    if "trigger" in k.lower() or "input" in k.lower():
                        in_ports.add(v)
                    else:
                        out_ports.add(v)

            nodes[nid] = GraphNode(
                id=nid,
                node_type=node_type,
                payload=payload,
                rid=rid,
                input_ports=in_ports,
                output_ports=out_ports,
            )

        raw_conns = data.get("eventNodeGraph", {}).get("connections", [])
        connections: List[GraphConnection] = []
        for c in raw_conns:
            src = c.get("sourceNodeId", "").strip()
            tgt = c.get("targetNodeId", "").strip()
            if src and tgt:
                connections.append(
                    GraphConnection(
                        source_id=src,
                        source_port=c.get("sourcePortName", ""),
                        target_id=tgt,
                        target_port=c.get("targetPortName", ""),
                    )
                )

        return cls(nodes=nodes, connections=connections, variables=variables_list, source_desc=source_desc)

    @classmethod
    def from_json_file(cls, filepath: Union[str, Path]) -> LevelGraph:
        path = Path(filepath)
        if not path.is_file():
            raise FileNotFoundError(f"Exported level file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_json_dict(data, source_desc=str(path))

    @classmethod
    def from_context(cls, source_desc: str = "Active Context") -> LevelGraph:
        all_nodes = list(_ctx.nodes)
        existing_ids = {getattr(n, "id", None) for n in all_nodes}
        connections_raw = list(ConnectionManager.get_connections())
        for conn in connections_raw:
            if conn.source_node and getattr(conn.source_node, "id", None) not in existing_ids:
                all_nodes.append(conn.source_node)
                existing_ids.add(conn.source_node.id)
            if conn.target_node and getattr(conn.target_node, "id", None) not in existing_ids:
                all_nodes.append(conn.target_node)
                existing_ids.add(conn.target_node.id)

        nodes: Dict[str, GraphNode] = {}
        variables_list: List[Dict[str, Any]] = []
        seen_vars: Set[int] = set()
        for v in _ctx.variables:
            if id(v) not in seen_vars and hasattr(v, "dump_data"):
                seen_vars.add(id(v))
                vd = v.dump_data()
                variables_list.append({
                    "type": getattr(v, "asset_class", v.__class__.__name__),
                    "name": vd.get("name"),
                    "value": vd.get("value"),
                })

        for n in all_nodes:
            nid = getattr(n, "id", str(id(n)))
            node_type = getattr(n, "node_type", n.__class__.__name__)
            
            raw_data = n.dump_data() if hasattr(n, "dump_data") else {}
            payload = _clean_payload(raw_data)

            asset_obj = getattr(n, "asset", None)
            if asset_obj is not None and hasattr(asset_obj, "dump_data"):
                vd = asset_obj.dump_data()
                var_info = {
                    "type": getattr(asset_obj, "asset_class", asset_obj.__class__.__name__),
                    "name": vd.get("name"),
                    "value": vd.get("value"),
                }
                payload["asset"] = var_info
                if id(asset_obj) not in seen_vars:
                    seen_vars.add(id(asset_obj))
                    variables_list.append(var_info)
            
            in_ports: Set[str] = set()
            out_ports: Set[str] = set()
            for p in getattr(n, "ports", []):
                pname = getattr(p, "name", "")
                pdir = getattr(p, "direction", None)
                if pdir == PortDirection.Input:
                    in_ports.add(pname)
                elif pdir == PortDirection.Output:
                    out_ports.add(pname)

            nodes[nid] = GraphNode(
                id=nid,
                node_type=node_type,
                payload=payload,
                rid=getattr(n, "rid", None),
                input_ports=in_ports,
                output_ports=out_ports,
            )

        connections: List[GraphConnection] = []
        for c in connections_raw:
            src_node = getattr(c, "source_node", None)
            tgt_node = getattr(c, "target_node", None)
            src_port = getattr(c, "source_port", None)
            tgt_port = getattr(c, "target_port", None)
            if src_node and tgt_node and src_port and tgt_port:
                connections.append(
                    GraphConnection(
                        source_id=src_node.id,
                        source_port=src_port.name,
                        target_id=tgt_node.id,
                        target_port=tgt_port.name,
                    )
                )

        return cls(nodes=nodes, connections=connections, variables=variables_list, source_desc=source_desc)

    @classmethod
    def from_code(
        cls,
        code_or_path: Union[str, Path, Callable[[], Any]],
        source_desc: Optional[str] = None,
    ) -> LevelGraph:
        """Run Python DSL code in an isolated transpiler context and return its LevelGraph."""
        with isolate_transpiler_context():
            if callable(code_or_path):
                desc = source_desc or getattr(code_or_path, "__name__", "callable")
                code_or_path()
            else:
                path = Path(code_or_path) if isinstance(code_or_path, (str, Path)) and os.path.exists(str(code_or_path)) else None
                if path and path.is_file():
                    desc = source_desc or str(path)
                    code_text = path.read_text(encoding="utf-8")
                    namespace = {"__file__": str(path), "__name__": "__main__"}
                    exec(compile(code_text, str(path), "exec"), namespace)
                else:
                    code_str = str(code_or_path)
                    desc = source_desc or "Python Code Snippet"
                    namespace = {"__name__": "__main__"}
                    exec(compile(code_str, "<string>", "exec"), namespace)

            return cls.from_context(source_desc=desc)

    def incoming_connections(self, node_id: str) -> List[GraphConnection]:
        return [c for c in self.connections if c.target_id == node_id]

    def outgoing_connections(self, node_id: str) -> List[GraphConnection]:
        return [c for c in self.connections if c.source_id == node_id]

    def analyze_optimizations(self) -> List[OptimizationFinding]:
        """Detect dead nodes, disconnected ports, and duplicate constants."""
        findings: List[OptimizationFinding] = []

        # 1. Floating nodes (0 connections in and out)
        for nid, node in self.nodes.items():
            in_c = self.incoming_connections(nid)
            out_c = self.outgoing_connections(nid)
            if not in_c and not out_c:
                findings.append(
                    OptimizationFinding(
                        kind="FLOATING_NODE",
                        message=f"{node.format_summary()} (id: {nid}) has 0 incoming and 0 outgoing connections.",
                        node_id=nid,
                    )
                )

        # 2. Unreached action nodes (has trigger input port but no incoming trigger connection)
        for nid, node in self.nodes.items():
            if "触发" in node.input_ports or "Trigger" in node.input_ports:
                incoming_triggers = [
                    c for c in self.incoming_connections(nid)
                    if c.target_port in ("触发", "Trigger")
                ]
                if not incoming_triggers:
                    findings.append(
                        OptimizationFinding(
                            kind="UNREACHED_NODE",
                            message=f"{node.format_summary()} has an execution trigger input port but nothing triggers it.",
                            node_id=nid,
                        )
                    )

        # 3. Redundant duplicate constants (same type + exact same value)
        constants: Dict[Tuple[str, str], List[str]] = {}
        for nid, node in self.nodes.items():
            if node.node_type.endswith("ValueNode") and "value" in node.payload:
                key = (node.node_type, str(node.payload["value"]))
                constants.setdefault(key, []).append(nid)

        for (ntype, val), nids in constants.items():
            if len(nids) > 1:
                findings.append(
                    OptimizationFinding(
                        kind="REDUNDANT_CONSTANT",
                        message=f"Multiple {ntype} nodes ({len(nids)}) found with value {val}; could be deduplicated into a single shared node.",
                    )
                )

        return findings


@contextlib.contextmanager
def isolate_transpiler_context() -> Iterator[None]:
    """Isolate _ctx and ConnectionManager so test graph runs do not leak state."""
    prev_nodes = list(_ctx.nodes)
    prev_config = dict(_ctx.config)
    prev_configured = _ctx._configured
    prev_variables = list(_ctx.variables)
    prev_connections = list(ConnectionManager.get_connections())

    _ctx.clear()
    ConnectionManager.clear()
    try:
        yield
    finally:
        _ctx.clear()
        ConnectionManager.clear()
        _ctx.nodes.extend(prev_nodes)
        _ctx.config.update(prev_config)
        _ctx._configured = prev_configured
        _ctx.variables.extend(prev_variables)
        for c in prev_connections:
            ConnectionManager.connections.append(c)


@dataclass
class ComparisonResult:
    """Detailed result of comparing actual graph against expected graph."""
    matched: bool
    actual_desc: str
    expected_desc: str
    missing_nodes: List[str] = field(default_factory=list)
    extra_nodes: List[str] = field(default_factory=list)
    missing_connections: List[str] = field(default_factory=list)
    extra_connections: List[str] = field(default_factory=list)
    property_mismatches: List[str] = field(default_factory=list)
    optimization_findings: List[OptimizationFinding] = field(default_factory=list)
    node_mapping: Dict[str, str] = field(default_factory=dict)  # actual_id -> expected_id

    def render_report(self) -> str:
        lines: List[str] = [
            "=" * 70,
            "LEVEL GRAPH VERIFICATION REPORT",
            "=" * 70,
            f"Actual Source:   {self.actual_desc}",
            f"Expected Source: {self.expected_desc}",
            f"Status:          {'PASS (MATCH)' if self.matched else 'FAIL (MISMATCH)'}",
            "-" * 70,
        ]

        if self.missing_nodes:
            lines.append(f"Missing Nodes ({len(self.missing_nodes)}):")
            for n in self.missing_nodes:
                lines.append(f"  [-] {n}")

        if self.extra_nodes:
            lines.append(f"Unexpected / Extra Nodes ({len(self.extra_nodes)}):")
            for n in self.extra_nodes:
                lines.append(f"  [+] {n}")

        if self.missing_connections:
            lines.append(f"Missing Connections ({len(self.missing_connections)}):")
            for c in self.missing_connections:
                lines.append(f"  [-] {c}")

        if self.extra_connections:
            lines.append(f"Unexpected / Extra Connections ({len(self.extra_connections)}):")
            for c in self.extra_connections:
                lines.append(f"  [+] {c}")

        if self.property_mismatches:
            lines.append(f"Node Property Mismatches ({len(self.property_mismatches)}):")
            for p in self.property_mismatches:
                lines.append(f"  [!] {p}")

        if self.optimization_findings:
            lines.append(f"Optimization & Cleanliness Findings ({len(self.optimization_findings)}):")
            for opt in self.optimization_findings:
                lines.append(f"  [*] [{opt.kind}] {opt.message}")
        else:
            lines.append("Optimization: Graph is clean (no floating nodes or dead triggers).")

        lines.append("=" * 70)
        return "\n".join(lines)


class LevelVerifier:
    """Semantic graph isomorphism and topology verifier."""

    @staticmethod
    def compare(
        actual: LevelGraph,
        expected: LevelGraph,
        check_payloads: bool = True,
        allow_extra_nodes: bool = False,
        allow_extra_connections: bool = False,
    ) -> ComparisonResult:
        actual_nodes = actual.nodes
        expected_nodes = expected.nodes

        # Check type counts
        actual_types: Dict[str, int] = {}
        for n in actual_nodes.values():
            actual_types[n.node_type] = actual_types.get(n.node_type, 0) + 1

        expected_types: Dict[str, int] = {}
        for n in expected_nodes.values():
            expected_types[n.node_type] = expected_types.get(n.node_type, 0) + 1

        missing_nodes: List[str] = []
        extra_nodes: List[str] = []

        for ntype, exp_count in expected_types.items():
            act_count = actual_types.get(ntype, 0)
            if act_count < exp_count:
                missing_nodes.append(f"{ntype} (expected {exp_count}, got {act_count})")

        if not allow_extra_nodes:
            for ntype, act_count in actual_types.items():
                exp_count = expected_types.get(ntype, 0)
                if act_count > exp_count:
                    extra_nodes.append(f"{ntype} (expected {exp_count}, got {act_count})")

        # Find best isomorphism mapping
        mapping = _find_best_isomorphism(
            actual=actual,
            expected=expected,
            check_payloads=check_payloads,
            allow_extra_nodes=allow_extra_nodes,
        )

        missing_conns: List[str] = []
        extra_conns: List[str] = []
        property_mismatches: List[str] = []

        # Analyze connections under this mapping
        mapped_expected_conns: Set[Tuple[str, str, str, str]] = set()
        for c in expected.connections:
            mapped_expected_conns.add((c.source_id, c.source_port, c.target_id, c.target_port))

        mapped_actual_conns: Set[Tuple[str, str, str, str]] = set()
        for c in actual.connections:
            exp_src = mapping.get(c.source_id)
            exp_tgt = mapping.get(c.target_id)
            if exp_src and exp_tgt:
                mapped_actual_conns.add((exp_src, c.source_port, exp_tgt, c.target_port))
            else:
                extra_conns.append(c.format_with_types(actual_nodes))

        # Check missing connections
        for c in expected.connections:
            sig = (c.source_id, c.source_port, c.target_id, c.target_port)
            if sig not in mapped_actual_conns:
                missing_conns.append(c.format_with_types(expected_nodes))

        # Check extra connections
        if not allow_extra_connections:
            for c in actual.connections:
                exp_src = mapping.get(c.source_id)
                exp_tgt = mapping.get(c.target_id)
                if exp_src and exp_tgt:
                    sig = (exp_src, c.source_port, exp_tgt, c.target_port)
                    if sig not in mapped_expected_conns:
                        extra_conns.append(c.format_with_types(actual_nodes))

        # Check property mismatches on mapped pairs
        for act_id, exp_id in mapping.items():
            act_n = actual_nodes[act_id]
            exp_n = expected_nodes[exp_id]
            all_keys = set(act_n.payload.keys()) | set(exp_n.payload.keys())
            for k in all_keys:
                v_act = act_n.payload.get(k)
                v_exp = exp_n.payload.get(k)
                if not _values_match(v_act, v_exp):
                    property_mismatches.append(
                        f"{act_n.node_type}.{k}: expected {v_exp!r}, got {v_act!r}"
                    )

        opt_findings = actual.analyze_optimizations()

        is_match = (
            not missing_nodes
            and not extra_nodes
            and not missing_conns
            and not extra_conns
            and not property_mismatches
        )

        return ComparisonResult(
            matched=is_match,
            actual_desc=actual.source_desc,
            expected_desc=expected.source_desc,
            missing_nodes=missing_nodes,
            extra_nodes=extra_nodes,
            missing_connections=missing_conns,
            extra_connections=extra_conns,
            property_mismatches=property_mismatches,
            optimization_findings=opt_findings,
            node_mapping=mapping,
        )


def _find_best_isomorphism(
    actual: LevelGraph,
    expected: LevelGraph,
    check_payloads: bool,
    allow_extra_nodes: bool,
) -> Dict[str, str]:
    """Find a bijective or maximum-score mapping from actual node IDs to expected node IDs."""
    act_ids = list(actual.nodes.keys())
    exp_ids = list(expected.nodes.keys())

    # Build candidate sets for each actual node (match by node_type, prioritize payload match)
    candidates: Dict[str, List[str]] = {}
    for aid in act_ids:
        an = actual.nodes[aid]
        type_cands = [eid for eid in exp_ids if an.node_type == expected.nodes[eid].node_type]
        type_cands.sort(
            key=lambda eid: 0 if an.matches(expected.nodes[eid], check_payload=True) else 1
        )
        candidates[aid] = type_cands

    # Sort actual nodes by candidate count (MRV)
    sorted_act = sorted(act_ids, key=lambda a: len(candidates[a]))

    best_mapping: Dict[str, str] = {}
    best_score = -1

    expected_edge_set = {
        (c.source_id, c.source_port, c.target_id, c.target_port)
        for c in expected.connections
    }

    def score_mapping(curr: Dict[str, str]) -> int:
        score = len(curr) * 10
        for aid, eid in curr.items():
            if actual.nodes[aid].matches(expected.nodes[eid], check_payload=True):
                score += 10
        for c in actual.connections:
            s_exp = curr.get(c.source_id)
            t_exp = curr.get(c.target_id)
            if s_exp and t_exp and (s_exp, c.source_port, t_exp, c.target_port) in expected_edge_set:
                score += 5
        return score

    def backtrack(idx: int, current: Dict[str, str], used_exp: Set[str]) -> bool:
        nonlocal best_mapping, best_score
        curr_score = score_mapping(current)
        if curr_score > best_score:
            best_score = curr_score
            best_mapping = dict(current)

        if idx >= len(sorted_act):
            return True  # Full mapping found

        aid = sorted_act[idx]
        for eid in candidates[aid]:
            if eid in used_exp:
                continue

            current[aid] = eid
            used_exp.add(eid)

            if backtrack(idx + 1, current, used_exp):
                # If perfect score reached (all nodes and all edges mapped), terminate early
                target_perfect = (len(act_ids) * 10) + (len(actual.connections) * 5)
                if best_score >= target_perfect:
                    return True

            del current[aid]
            used_exp.remove(eid)

        return False

    backtrack(0, {}, set())
    return best_mapping


def assert_level_matches(
    code_or_file: Union[str, Path, Callable[[], Any]],
    expected_level_or_file: Union[str, Path, Dict[str, Any]],
    check_payloads: bool = True,
    allow_extra_nodes: bool = False,
    allow_extra_connections: bool = False,
    msg: Optional[str] = None,
) -> ComparisonResult:
    """Unittest assertion function to verify Python transpiler code against an exported level."""
    actual_graph = LevelGraph.from_code(code_or_file)
    if isinstance(expected_level_or_file, dict):
        expected_graph = LevelGraph.from_json_dict(expected_level_or_file)
    else:
        path = Path(expected_level_or_file)
        if path.is_file():
            expected_graph = LevelGraph.from_json_file(path)
        else:
            expected_graph = LevelGraph.from_json_dict(
                json.loads(str(expected_level_or_file)), source_desc="JSON String"
            )

    result = LevelVerifier.compare(
        actual=actual_graph,
        expected=expected_graph,
        check_payloads=check_payloads,
        allow_extra_nodes=allow_extra_nodes,
        allow_extra_connections=allow_extra_connections,
    )

    if not result.matched:
        report = result.render_report()
        failure_msg = f"{msg}\n{report}" if msg else report
        raise AssertionError(failure_msg)

    return result


class LevelTestCase(unittest.TestCase):
    """Convenient base class for test suites validating level graphs and connections."""

    def assert_level_matches(
        self,
        code_or_file: Union[str, Path, Callable[[], Any]],
        expected_level_or_file: Union[str, Path, Dict[str, Any]],
        **kwargs: Any,
    ) -> ComparisonResult:
        return assert_level_matches(code_or_file, expected_level_or_file, **kwargs)

    def assert_snapshot_matches(
        self,
        code_or_file: Union[str, Path, Callable[[], Any]],
        expected_snapshot_or_file: Union[str, Path, Dict[str, Any]],
        **kwargs: Any,
    ) -> SnapshotVerificationResult:
        return assert_snapshot_matches(code_or_file, expected_snapshot_or_file, **kwargs)

    def assert_no_floating_nodes(self, graph: LevelGraph) -> None:
        findings = [f for f in graph.analyze_optimizations() if f.kind == "FLOATING_NODE"]
        if findings:
            details = "\n".join(f"  - {f.message}" for f in findings)
            self.fail(f"Graph has {len(findings)} floating nodes:\n{details}")


# =====================================================================
# STRIPPED SNAPSHOT FORMAT & REFERENTIAL REGEX VERIFIER
# =====================================================================

_STRIPPED_META_KEYS = {
    "position",
    "m_Position",
    "inputDefaults",
    "m_InputDefaults",
    "nodeName",
    "m_Name",
}

_SYMBOL_FIELDS = {"nodeId", "variableId", "referencedNodeIds", "asset"}


def _is_regex_matcher(val: Any) -> bool:
    return isinstance(val, dict) and set(val.keys()) == {"$regex"} and isinstance(val["$regex"], str)


def _match_pattern_val(exp_val: Any, act_val: Any) -> bool:
    """Compare value or regex pattern dictionary against actual serialized value."""
    if _is_regex_matcher(exp_val):
        if act_val is None:
            return False
        return re.fullmatch(exp_val["$regex"], str(act_val)) is not None
    if isinstance(exp_val, dict) and isinstance(act_val, dict):
        if set(exp_val.keys()) != set(act_val.keys()):
            return False
        return all(_match_pattern_val(exp_val[k], act_val[k]) for k in exp_val)
    if isinstance(exp_val, list) and isinstance(act_val, list):
        if len(exp_val) != len(act_val):
            return False
        return all(_match_pattern_val(a, b) for a, b in zip(exp_val, act_val))
    return _values_match(exp_val, act_val)


def _clean_ref_data_for_snapshot(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        k: v
        for k, v in raw_data.items()
        if k not in _STRIPPED_META_KEYS and not k.endswith("_PortName")
    }


def build_and_export_from_code(
    code_or_path: Union[str, Path, Callable[[], Any]],
) -> Tuple[Dict[str, Any], LevelGraph, str]:
    """Execute Python DSL code in isolation and export to a temporary JSON file cleanly."""
    import PvZ_Fusion_Transpiler as pft

    with isolate_transpiler_context():
        orig_export = _ctx.export
        orig_pft_export = pft.export
        # Prevent script-embedded export() calls from overwriting files on disk during tests
        _ctx.export = lambda filepath=None: None  # type: ignore
        pft.export = lambda filepath=None: None  # type: ignore
        try:
            if callable(code_or_path):
                desc = getattr(code_or_path, "__name__", "callable")
                code_or_path()
            else:
                path = Path(code_or_path) if isinstance(code_or_path, (str, Path)) and os.path.exists(str(code_or_path)) else None
                if path and path.is_file():
                    desc = str(path)
                    code_text = path.read_text(encoding="utf-8")
                    namespace = {"__file__": str(path), "__name__": "__main__"}
                    exec(compile(code_text, str(path), "exec"), namespace)
                else:
                    code_str = str(code_or_path)
                    desc = "Python Code Snippet"
                    namespace = {"__name__": "__main__"}
                    exec(compile(code_str, "<string>", "exec"), namespace)
        finally:
            _ctx.export = orig_export  # type: ignore
            pft.export = orig_pft_export  # type: ignore

        graph = LevelGraph.from_context(source_desc=desc)
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = os.path.join(tmpdir, "level_build.json")
            _ctx.export(filepath=out_path)
            with open(out_path, "r", encoding="utf-8") as f:
                exported_dict = json.load(f)

        return exported_dict, graph, desc


@dataclass
class SnapshotVerificationResult:
    """Result of verifying an exported level JSON against a stripped snapshot template."""
    matched: bool
    actual_desc: str
    expected_desc: str
    format_errors: List[str] = field(default_factory=list)
    missing_refs: List[str] = field(default_factory=list)
    extra_refs: List[str] = field(default_factory=list)
    missing_connections: List[str] = field(default_factory=list)
    extra_connections: List[str] = field(default_factory=list)
    optimization_findings: List[OptimizationFinding] = field(default_factory=list)

    def render_report(self) -> str:
        lines: List[str] = [
            "=" * 70,
            "STRIPPED SNAPSHOT VERIFICATION REPORT",
            "=" * 70,
            f"Actual Source:   {self.actual_desc}",
            f"Expected JSON:   {self.expected_desc}",
            f"Status:          {'PASS (FORMAT & GRAPH MATCH)' if self.matched else 'FAIL (MISMATCH)'}",
            "-" * 70,
        ]
        for title, items in [
            ("Format Errors", self.format_errors),
            ("Missing RefIds", self.missing_refs),
            ("Unexpected RefIds", self.extra_refs),
            ("Missing Connections", self.missing_connections),
            ("Unexpected Connections", self.extra_connections),
        ]:
            if items:
                lines.append(f"{title} ({len(items)}):")
                for item in items:
                    lines.append(f"  [-] {item}")
        if self.optimization_findings:
            lines.append(f"Optimization Findings ({len(self.optimization_findings)}):")
            for opt in self.optimization_findings:
                lines.append(f"  [*] [{opt.kind}] {opt.message}")
        else:
            lines.append("Optimization: Graph is clean (0 floating nodes, 0 dead triggers).")
        lines.append("=" * 70)
        return "\n".join(lines)


def _ref_items_payload_compatible(exp_item: Dict[str, Any], act_item: Dict[str, Any]) -> bool:
    """Check if RefId type metadata and non-symbolic data fields match."""
    if not _match_pattern_val(exp_item.get("type", {}), act_item.get("type", {})):
        return False
    exp_data = exp_item.get("data", {})
    act_data = _clean_ref_data_for_snapshot(act_item.get("data", {}))
    if set(exp_data.keys()) != set(act_data.keys()):
        return False
    for k, ev in exp_data.items():
        if k in _SYMBOL_FIELDS:
            continue
        if not _match_pattern_val(ev, act_data.get(k)):
            return False
    return True


def _bind_symbol(sym: Any, val: Any, bindings: Dict[str, Any], reverse: Dict[str, Any]) -> bool:
    if isinstance(sym, str) and sym.startswith("@"):
        if sym.startswith("@rid_"):
            if not isinstance(val, int) or isinstance(val, bool):
                return False
        else:
            if not isinstance(val, str) or not re.fullmatch(r"[0-9a-f-]{32,36}", val):
                return False
        if sym in bindings:
            return bindings[sym] == val
        # Enforce 1-to-1 bijection per symbol namespace
        prefix = sym.split("_", 1)[0]
        rev_key = f"{prefix}:{val}"
        if rev_key in reverse:
            return False
        bindings[sym] = val
        reverse[rev_key] = sym
        return True
    return _match_pattern_val(sym, val)


def _check_resolved_links(
    exp_refs: List[Dict[str, Any]],
    act_refs: List[Dict[str, Any]],
    exp_to_act: Dict[int, int],
    bindings: Dict[str, Any],
    exp_graph: Dict[str, Any],
    act_graph: Dict[str, Any],
) -> Tuple[List[str], List[str], List[str]]:
    """Verify asset links, referencedNodeIds, nodes, variables, and connections under bindings."""
    fmt_errors: List[str] = []
    # Check asset & referencedNodeIds inside mapped RefIds
    for e_idx, a_idx in exp_to_act.items():
        e_data = exp_refs[e_idx].get("data", {})
        a_data = act_refs[a_idx].get("data", {})
        if "asset" in e_data:
            e_rid = e_data["asset"].get("rid")
            a_rid = a_data.get("asset", {}).get("rid")
            if bindings.get(e_rid, e_rid) != a_rid:
                fmt_errors.append(f"Asset rid mismatch on {e_data.get('nodeType')}: expected {e_rid}, got {a_rid}")
        if "referencedNodeIds" in e_data:
            expected_nids = {bindings.get(n, n) for n in e_data["referencedNodeIds"]}
            actual_nids = set(a_data.get("referencedNodeIds", []))
            if expected_nids != actual_nids:
                fmt_errors.append(f"referencedNodeIds mismatch: expected {sorted(expected_nids)}, got {sorted(actual_nids)}")

    # Check eventNodeGraph.nodes and variables
    exp_node_rids = {bindings.get(n["rid"], n["rid"]) for n in exp_graph.get("nodes", [])}
    act_node_rids = {n["rid"] for n in act_graph.get("nodes", [])}
    if exp_node_rids != act_node_rids:
        fmt_errors.append(f"eventNodeGraph.nodes RID mismatch: expected {sorted(exp_node_rids)}, got {sorted(act_node_rids)}")

    exp_var_rids = {bindings.get(v["rid"], v["rid"]) for v in exp_graph.get("variables", [])}
    act_var_rids = {v["rid"] for v in act_graph.get("variables", [])}
    if exp_var_rids != act_var_rids:
        fmt_errors.append(f"eventNodeGraph.variables RID mismatch: expected {sorted(exp_var_rids)}, got {sorted(act_var_rids)}")

    # Check connections
    act_node_type_by_id = {
        r.get("data", {}).get("nodeId"): r.get("data", {}).get("nodeType", "Unknown")
        for r in act_refs
        if r.get("data", {}).get("nodeId")
    }
    exp_node_type_by_sym = {
        r.get("data", {}).get("nodeId"): r.get("data", {}).get("nodeType", "Unknown")
        for r in exp_refs
        if r.get("data", {}).get("nodeId")
    }

    exp_conns = [c for c in exp_graph.get("connections", []) if c.get("sourceNodeId")]
    act_conns = [c for c in act_graph.get("connections", []) if c.get("sourceNodeId")]

    resolved_exp_set: Dict[Tuple[str, str, str, str], int] = {}
    for c in exp_conns:
        sig = (
            bindings.get(c["sourceNodeId"], c["sourceNodeId"]),
            c.get("sourcePortName", ""),
            bindings.get(c["targetNodeId"], c["targetNodeId"]),
            c.get("targetPortName", ""),
        )
        resolved_exp_set[sig] = resolved_exp_set.get(sig, 0) + 1

    actual_set: Dict[Tuple[str, str, str, str], int] = {}
    for c in act_conns:
        sig = (
            c.get("sourceNodeId", ""),
            c.get("sourcePortName", ""),
            c.get("targetNodeId", ""),
            c.get("targetPortName", ""),
        )
        actual_set[sig] = actual_set.get(sig, 0) + 1

    missing_conns: List[str] = []
    for sig, cnt in resolved_exp_set.items():
        if actual_set.get(sig, 0) < cnt:
            s_t = act_node_type_by_id.get(sig[0], exp_node_type_by_sym.get(sig[0], sig[0]))
            t_t = act_node_type_by_id.get(sig[2], exp_node_type_by_sym.get(sig[2], sig[2]))
            missing_conns.append(f"{s_t}[{sig[1]!r}] -> {t_t}[{sig[3]!r}]")

    extra_conns: List[str] = []
    for sig, cnt in actual_set.items():
        if resolved_exp_set.get(sig, 0) < cnt:
            s_t = act_node_type_by_id.get(sig[0], sig[0])
            t_t = act_node_type_by_id.get(sig[2], sig[2])
            extra_conns.append(f"{s_t}[{sig[1]!r}] -> {t_t}[{sig[3]!r}]")

    return fmt_errors, missing_conns, extra_conns


def verify_snapshot_matches(
    actual_dict: Dict[str, Any],
    expected_template: Dict[str, Any],
    actual_desc: str = "Exported Level",
    expected_desc: str = "Expected Snapshot",
) -> SnapshotVerificationResult:
    """Verify exported JSON structure, regex matchers, symbolic RefIds, and connections."""
    format_errors: List[str] = []

    if "eventNodeGraph" not in actual_dict or "references" not in actual_dict:
        format_errors.append("Root JSON missing required 'eventNodeGraph' or 'references' section.")
        return SnapshotVerificationResult(False, actual_desc, expected_desc, format_errors=format_errors)

    exp_graph = expected_template["eventNodeGraph"]
    act_graph = actual_dict["eventNodeGraph"]
    exp_refs_root = expected_template["references"]
    act_refs_root = actual_dict["references"]

    if exp_refs_root.get("version") != act_refs_root.get("version"):
        format_errors.append(f"references.version mismatch: expected {exp_refs_root.get('version')}, got {act_refs_root.get('version')}")
    if exp_graph.get("executionVersion") != act_graph.get("executionVersion"):
        format_errors.append(f"executionVersion mismatch: expected {exp_graph.get('executionVersion')}, got {act_graph.get('executionVersion')}")
    if "graphId" in exp_graph and not _match_pattern_val(exp_graph["graphId"], act_graph.get("graphId")):
        format_errors.append(f"graphId failed pattern check: {act_graph.get('graphId')!r}")

    exp_conns_all = exp_graph.get("connections", [])
    act_conns_all = act_graph.get("connections", [])
    if exp_conns_all and exp_conns_all[0].get("sourceNodeId") == "":
        if not act_conns_all or act_conns_all[0] != exp_conns_all[0]:
            format_errors.append("eventNodeGraph.connections[0] must be the empty dummy connection.")

    exp_refs: List[Dict[str, Any]] = exp_refs_root.get("RefIds", [])
    act_refs: List[Dict[str, Any]] = act_refs_root.get("RefIds", [])

    candidates: Dict[int, List[int]] = {
        ei: [ai for ai, a in enumerate(act_refs) if _ref_items_payload_compatible(e, a)]
        for ei, e in enumerate(exp_refs)
    }

    sorted_exp = sorted(range(len(exp_refs)), key=lambda i: len(candidates[i]))

    best_result: Optional[Tuple[int, Dict[int, int], Dict[str, Any], List[str], List[str], List[str]]] = None

    def try_assign(idx: int, mapping: Dict[int, int], used_act: Set[int], bindings: Dict[str, Any], reverse: Dict[str, Any]) -> bool:
        nonlocal best_result
        if idx >= len(sorted_exp):
            ferr, mconn, econn = _check_resolved_links(exp_refs, act_refs, mapping, bindings, exp_graph, act_graph)
            penalty = len(ferr) + len(mconn) + len(econn)
            if best_result is None or penalty < best_result[0]:
                best_result = (penalty, dict(mapping), dict(bindings), ferr, mconn, econn)
            return penalty == 0

        ei = sorted_exp[idx]
        e_item = exp_refs[ei]
        for ai in candidates[ei]:
            if ai in used_act:
                continue
            a_item = act_refs[ai]
            b_copy = dict(bindings)
            r_copy = dict(reverse)
            ok = _bind_symbol(e_item.get("rid"), a_item.get("rid"), b_copy, r_copy)
            if ok and "nodeId" in e_item.get("data", {}):
                ok = _bind_symbol(e_item["data"]["nodeId"], a_item.get("data", {}).get("nodeId"), b_copy, r_copy)
            if ok and "variableId" in e_item.get("data", {}):
                ok = _bind_symbol(e_item["data"]["variableId"], a_item.get("data", {}).get("variableId"), b_copy, r_copy)
            if not ok:
                continue
            mapping[ei] = ai
            used_act.add(ai)
            if try_assign(idx + 1, mapping, used_act, b_copy, r_copy):
                return True
            used_act.remove(ai)
            del mapping[ei]
        return False

    if len(exp_refs) == len(act_refs):
        try_assign(0, {}, set(), {}, {})

    missing_refs: List[str] = []
    extra_refs: List[str] = []
    missing_conns: List[str] = []
    extra_conns: List[str] = []

    if best_result is not None:
        _, _, _, lerr, missing_conns, extra_conns = best_result
        format_errors.extend(lerr)
    else:
        exp_classes: Dict[str, int] = {}
        act_classes: Dict[str, int] = {}
        for r in exp_refs:
            c = str(r.get("type", {}).get("class", "Unknown"))
            exp_classes[c] = exp_classes.get(c, 0) + 1
        for r in act_refs:
            c = str(r.get("type", {}).get("class", "Unknown"))
            act_classes[c] = act_classes.get(c, 0) + 1
        for c, cnt in exp_classes.items():
            if act_classes.get(c, 0) < cnt:
                missing_refs.append(f"{c} (expected {cnt}, got {act_classes.get(c, 0)})")
        for c, cnt in act_classes.items():
            if exp_classes.get(c, 0) < cnt:
                extra_refs.append(f"{c} (expected {exp_classes.get(c, 0)}, got {cnt})")
        if not missing_refs and not extra_refs:
            format_errors.append("RefIds node attributes or payloads failed to align with expected snapshot.")

    opt_findings = LevelGraph.from_json_dict(actual_dict, source_desc=actual_desc).analyze_optimizations()
    matched = not (format_errors or missing_refs or extra_refs or missing_conns or extra_conns)
    return SnapshotVerificationResult(
        matched=matched,
        actual_desc=actual_desc,
        expected_desc=expected_desc,
        format_errors=format_errors,
        missing_refs=missing_refs,
        extra_refs=extra_refs,
        missing_connections=missing_conns,
        extra_connections=extra_conns,
        optimization_findings=opt_findings,
    )


def assert_snapshot_matches(
    code_or_file: Union[str, Path, Callable[[], Any]],
    expected_snapshot_or_file: Union[str, Path, Dict[str, Any]],
    msg: Optional[str] = None,
) -> SnapshotVerificationResult:
    """Build level from Python code, export JSON, and verify it meets stripped snapshot format."""
    actual_dict, _, actual_desc = build_and_export_from_code(code_or_file)
    if isinstance(expected_snapshot_or_file, dict):
        expected_template = expected_snapshot_or_file
        expected_desc = "Snapshot Dict"
    else:
        path = Path(expected_snapshot_or_file)
        if not path.is_file():
            raise FileNotFoundError(f"Expected snapshot JSON not found: {path}")
        expected_desc = str(path)
        with open(path, "r", encoding="utf-8") as f:
            expected_template = json.load(f)

    result = verify_snapshot_matches(
        actual_dict=actual_dict,
        expected_template=expected_template,
        actual_desc=actual_desc,
        expected_desc=expected_desc,
    )
    if not result.matched:
        report = result.render_report()
        raise AssertionError(f"{msg}\n{report}" if msg else report)
    return result


def main() -> int:
    """CLI Entry Point: python tools/level_verifier.py <code_file> <level_json>"""
    if len(sys.argv) < 3:
        print("Usage: python tools/level_verifier.py <code_path_or_script> <expected_level_json>")
        return 1

    code_path = sys.argv[1]
    json_path = sys.argv[2]

    try:
        result = assert_level_matches(code_path, json_path)
        print(result.render_report())
        return 0
    except AssertionError as e:
        print(e, file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error during verification: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
