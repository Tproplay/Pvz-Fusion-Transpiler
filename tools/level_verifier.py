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
import sys
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
    """Compare two payload values with float tolerance and int coercion."""
    if v1 is None and v2 is None:
        return True
    if v1 is None or v2 is None:
        return False
    if isinstance(v1, (int, float)) and isinstance(v2, (int, float)):
        return math.isclose(float(v1), float(v2), rel_tol=1e-5, abs_tol=1e-5)
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
        nodes: Dict[str, GraphNode] = {}
        for item in data.get("references", {}).get("RefIds", []):
            data_block = item.get("data", {})
            nid = data_block.get("nodeId") or data_block.get("id") or str(item.get("rid"))
            
            raw_type = data_block.get("nodeType")
            if not raw_type and "type" in item:
                t = item["type"]
                raw_type = t.get("class") if isinstance(t, dict) else str(t).split(".")[-1]
            node_type = str(raw_type or "UnknownNode")

            payload = _clean_payload(data_block)
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
                rid=item.get("rid"),
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

        return cls(nodes=nodes, connections=connections, source_desc=source_desc)

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
        nodes: Dict[str, GraphNode] = {}
        for n in _ctx.nodes:
            nid = getattr(n, "id", str(id(n)))
            node_type = getattr(n, "node_type", n.__class__.__name__)
            
            raw_data = n.dump_data() if hasattr(n, "dump_data") else {}
            payload = _clean_payload(raw_data)
            
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
        for c in ConnectionManager.get_connections():
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

        return cls(nodes=nodes, connections=connections, source_desc=source_desc)

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

    def assert_no_floating_nodes(self, graph: LevelGraph) -> None:
        findings = [f for f in graph.analyze_optimizations() if f.kind == "FLOATING_NODE"]
        if findings:
            details = "\n".join(f"  - {f.message}" for f in findings)
            self.fail(f"Graph has {len(findings)} floating nodes:\n{details}")


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
