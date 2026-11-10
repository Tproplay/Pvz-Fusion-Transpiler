#!/usr/bin/env python3
"""Utility to strip layout/engine bloat from an exported PvZ Fusion level JSON
into a clean, minimal snapshot template with symbolic ID bindings and regex matchers.

Usage:
    python tools/strip_level.py <raw_level.json> <output_stripped.json>
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


STRIPPED_NODE_KEYS = {
    "position",
    "m_Position",
    "inputDefaults",
    "m_InputDefaults",
    "nodeName",
    "m_Name",
}

UUID_REGEX_PATTERN = {"$regex": "^[0-9a-f-]{32,36}$"}


def _clean_node_data(
    raw_data: Dict[str, Any],
    node_id_map: Dict[str, str],
    var_id_map: Dict[str, str],
    rid_map: Dict[int, str],
) -> Dict[str, Any]:
    """Strip UI/port metadata from a single RefIds item data block and symbolize IDs."""
    cleaned: Dict[str, Any] = {}
    for k, v in raw_data.items():
        if k in STRIPPED_NODE_KEYS or k.endswith("_PortName"):
            continue

        if k == "nodeId" and isinstance(v, str) and v in node_id_map:
            cleaned[k] = node_id_map[v]
        elif k == "variableId" and isinstance(v, str) and v in var_id_map:
            cleaned[k] = var_id_map[v]
        elif k == "referencedNodeIds" and isinstance(v, list):
            cleaned[k] = [node_id_map.get(nid, nid) for nid in v]
        elif k == "asset" and isinstance(v, dict):
            asset_copy = dict(v)
            if "rid" in asset_copy and asset_copy["rid"] in rid_map:
                asset_copy["rid"] = rid_map[asset_copy["rid"]]
            cleaned[k] = asset_copy
        else:
            cleaned[k] = copy.deepcopy(v)

    return cleaned


def strip_level_json(raw_level: Dict[str, Any], keep_groups: bool = False) -> Dict[str, Any]:
    """Strip non-graph metadata and symbolize dynamic IDs into a clean snapshot dictionary."""
    event_graph = raw_level.get("eventNodeGraph", {})
    references = raw_level.get("references", {})
    raw_ref_ids: List[Dict[str, Any]] = references.get("RefIds", [])

    # Build deterministic symbol tables in RefIds traversal order
    rid_map: Dict[int, str] = {}
    node_id_map: Dict[str, str] = {}
    var_id_map: Dict[str, str] = {}

    node_counter = 0
    var_counter = 0
    for idx, item in enumerate(raw_ref_ids):
        rid = item.get("rid")
        if isinstance(rid, int):
            rid_map[rid] = f"@rid_{idx}"
        data = item.get("data", {})
        if isinstance(data, dict):
            nid = data.get("nodeId")
            if isinstance(nid, str) and nid:
                node_id_map[nid] = f"@node_{node_counter}"
                node_counter += 1
            vid = data.get("variableId")
            if isinstance(vid, str) and vid:
                var_id_map[vid] = f"@var_{var_counter}"
                var_counter += 1

    # Strip eventNodeGraph
    stripped_nodes = [
        {"rid": rid_map.get(n["rid"], n["rid"])}
        for n in event_graph.get("nodes", [])
        if isinstance(n, dict) and "rid" in n
    ]

    stripped_connections: List[Dict[str, Any]] = []
    for c in event_graph.get("connections", []):
        src = c.get("sourceNodeId", "")
        tgt = c.get("targetNodeId", "")
        stripped_connections.append({
            "sourceNodeId": node_id_map.get(src, src) if src else "",
            "sourcePortName": c.get("sourcePortName", ""),
            "targetNodeId": node_id_map.get(tgt, tgt) if tgt else "",
            "targetPortName": c.get("targetPortName", ""),
        })

    stripped_variables = [
        {"rid": rid_map.get(v["rid"], v["rid"])}
        for v in event_graph.get("variables", [])
        if isinstance(v, dict) and "rid" in v
    ]

    stripped_graph: Dict[str, Any] = {
        "nodes": stripped_nodes,
        "connections": stripped_connections,
        "variables": stripped_variables,
        "executionVersion": event_graph.get("executionVersion", 1),
        "graphId": dict(UUID_REGEX_PATTERN),
    }
    if keep_groups or event_graph.get("groups"):
        stripped_graph["groups"] = copy.deepcopy(event_graph.get("groups", []))

    # Strip references
    stripped_refs: List[Dict[str, Any]] = []
    for item in raw_ref_ids:
        rid = item.get("rid")
        data = item.get("data", {})
        stripped_refs.append({
            "rid": rid_map.get(rid, rid) if isinstance(rid, int) else rid,
            "type": copy.deepcopy(item.get("type", {})),
            "data": _clean_node_data(data, node_id_map, var_id_map, rid_map),
        })

    return {
        "eventNodeGraph": stripped_graph,
        "references": {
            "version": references.get("version", 2),
            "RefIds": stripped_refs,
        },
    }


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python tools/strip_level.py <raw_level.json> [output_stripped.json]")
        return 1

    in_path = Path(sys.argv[1])
    if not in_path.is_file():
        print(f"Error: File not found: {in_path}", file=sys.stderr)
        return 1

    with open(in_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    stripped = strip_level_json(raw_data)
    formatted = json.dumps(stripped, ensure_ascii=False, indent=2)

    if len(sys.argv) >= 3:
        out_path = Path(sys.argv[2])
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(formatted + "\n", encoding="utf-8")
        print(f"Stripped level snapshot saved to: {out_path}")
    else:
        print(formatted.encode("ascii", errors="backslashreplace").decode("ascii"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
