from __future__ import annotations

import os
import re
from typing import Any, Dict, List, Optional


_CACHE: Optional[Dict[str, Dict[str, Any]]] = None


def _load_definitions() -> Dict[str, Dict[str, Any]]:
    global _CACHE
    if _CACHE is not None:
        return _CACHE

    defs_path = os.path.join(os.path.dirname(__file__), "EventNodes_Definitions.txt")
    if not os.path.exists(defs_path):
        _CACHE = {}
        return _CACHE

    with open(defs_path, "r", encoding="utf-8") as f:
        text = f.read()

    nodes = text.split("[Node Class]: ")
    definitions: Dict[str, Dict[str, Any]] = {}
    for n in nodes[1:]:
        lines = n.splitlines()
        if not lines:
            continue
        cname = lines[0].strip().split(".")[-1]
        props: Dict[str, Any] = {}
        for l in lines[1:]:
            m = re.match(r"^\s*-\s*\[Property\]\s*(\w+)\s*=\s*(.*)", l)
            if m:
                prop_name = m.group(1)
                val_raw = m.group(2).strip()
                if val_raw.startswith('"') and val_raw.endswith('"'):
                    val: Any = val_raw[1:-1]
                elif val_raw == "null":
                    val = None
                else:
                    val = val_raw
                props[prop_name] = val

        port_names: List[str] = [k for k in props if k.endswith("_PortName")]
        port_defaults: Dict[str, Any] = {k: props[k] for k in port_names}
        custom_props: Dict[str, Any] = {
            k: v
            for k, v in props.items()
            if not k.endswith("_PortName")
            and not k.endswith("SourcePort")
            and k not in ("nodeId", "nodeType", "nodeName")
        }
        definitions[cname] = {
            "port_names": port_names,
            "port_defaults": port_defaults,
            "custom_props": custom_props,
        }

    _CACHE = definitions
    return _CACHE


def get_node_definition(class_name: str) -> Optional[Dict[str, Any]]:
    """Retrieve the reflection definition metadata for a given node class name."""
    defs = _load_definitions()
    return defs.get(class_name)


__all__ = ["get_node_definition"]
