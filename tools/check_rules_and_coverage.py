#!/usr/bin/env python3
"""Automated Rules Linter and Node Coverage Auditor for PvZ Fusion Transpiler."""

from __future__ import annotations

import ast
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = WORKSPACE_ROOT / "PvZ_Fusion_Transpiler_src" / "src" / "PvZ_Fusion_Transpiler"
NODES_ROOT = PACKAGE_ROOT / "_Nodes"
ORIGINAL_ROOT = NODES_ROOT / "Original"
EXTENSIONS_ROOT = NODES_ROOT / "Extensions"


def check_rule_2_init_files() -> List[str]:
    """Rule 2a: Every folder under _Nodes must have an __init__.py."""
    violations: List[str] = []
    for root, dirs, files in os.walk(NODES_ROOT):
        # Skip __pycache__
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        dir_path = Path(root)
        if "__init__.py" not in files:
            violations.append(f"Missing __init__.py in: {dir_path.relative_to(PACKAGE_ROOT)}")
    return violations


def check_rule_2_original_imports() -> List[str]:
    """Rule 2b: No direct imports of node classes from _Nodes/Original/* inside Extensions."""
    violations: List[str] = []
    if not EXTENSIONS_ROOT.exists():
        return violations

    for py_file in EXTENSIONS_ROOT.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue
        try:
            content = py_file.read_text(encoding="utf-8")
        except Exception:
            continue

        tree = ast.parse(content, filename=str(py_file))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                # Check for imports like 'from ..Original... import SomeNode'
                if "Original" in mod:
                    for alias in node.names:
                        if alias.name.endswith("Node") and alias.name != "Node":
                            violations.append(
                                f"{py_file.name}:{node.lineno} imports concrete node class '{alias.name}' directly from Original ({mod})"
                            )
    return violations


def check_rule_5_cjk_port_literals() -> List[str]:
    """Rule 5: No CJK string literals passed to ExecutionPath(...) or get_output(...)."""
    violations: List[str] = []
    cjk_pattern = re.compile(r"[\u4e00-\u9fff]")

    for py_file in EXTENSIONS_ROOT.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue
        try:
            content = py_file.read_text(encoding="utf-8")
        except Exception:
            continue

        tree = ast.parse(content, filename=str(py_file))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func_name = ""
                if isinstance(node.func, ast.Name):
                    func_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    func_name = node.func.attr

                if func_name in ("ExecutionPath", "get_output", "get_input", "get_port"):
                    for arg in node.args:
                        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                            if cjk_pattern.search(arg.value):
                                violations.append(
                                    f"{py_file.name}:{node.lineno} passes literal CJK '{arg.value}' to {func_name}()"
                                )
    return violations


def check_rule_3_function_length(threshold: int = 40) -> List[str]:
    """Rule 3: Guideline check for functions longer than threshold lines."""
    warnings: List[str] = []
    for py_file in EXTENSIONS_ROOT.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue
        try:
            content = py_file.read_text(encoding="utf-8")
            tree = ast.parse(content, filename=str(py_file))
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                end_lineno = getattr(node, "end_lineno", node.lineno)
                lines = end_lineno - node.lineno + 1
                if lines > threshold:
                    warnings.append(f"{py_file.name}:{node.lineno} def {node.name}() is {lines} lines (> {threshold})")
    return warnings


def check_rule_4_int_sentinels() -> List[str]:
    """Rule 4: PlantType/ZombieType parameters should not default to raw int sentinels."""
    warnings: List[str] = []
    for py_file in EXTENSIONS_ROOT.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue
        try:
            content = py_file.read_text(encoding="utf-8")
            tree = ast.parse(content, filename=str(py_file))
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Inspect default argument values
                defaults = node.args.defaults
                args = node.args.args[-len(defaults):] if defaults else []
                for arg, default in zip(args, defaults):
                    if any(t in arg.arg.lower() for t in ("plant_type", "zombie_type")):
                        if isinstance(default, ast.UnaryOp) and isinstance(default.op, ast.USub):
                            if isinstance(default.operand, ast.Constant) and isinstance(default.operand.value, (int, float)):
                                warnings.append(
                                    f"{py_file.name}:{node.lineno} arg '{arg.arg}' defaults to raw int (-{default.operand.value})"
                                )
                        elif isinstance(default, ast.Constant) and isinstance(default.value, (int, float)):
                            warnings.append(
                                f"{py_file.name}:{node.lineno} arg '{arg.arg}' defaults to raw int ({default.value})"
                            )
    return warnings


def audit_node_coverage() -> Tuple[int, int, List[str]]:
    """Audits coverage of all 240 original nodes in nodes.py and Extensions."""
    original_nodes: Set[str] = set()

    for py_file in ORIGINAL_ROOT.rglob("*.py"):
        if "__pycache__" in str(py_file):
            continue
        content = py_file.read_text(encoding="utf-8")
        tree = ast.parse(content, filename=str(py_file))
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name.endswith("Node") and node.name not in ("Node", "EventNodeBase", "EventSuggestedNode"):
                original_nodes.add(node.name)

    nodes_py_content = (PACKAGE_ROOT / "nodes.py").read_text(encoding="utf-8")
    missing_in_nodes_py = [n for n in sorted(original_nodes) if n not in nodes_py_content]

    return len(original_nodes), len(original_nodes) - len(missing_in_nodes_py), missing_in_nodes_py


def main() -> int:
    # Ensure stdout handles utf-8 cleanly
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
        except Exception:
            pass

    print("=" * 80)
    print("PvZ Fusion Transpiler -- Rules Lint & Node Coverage Auditor")
    print("=" * 80)

    # 1. Coverage
    total_nodes, covered_nodes, missing = audit_node_coverage()
    pct = (covered_nodes / total_nodes * 100.0) if total_nodes else 0
    print(f"\n[Coverage] Native Node Coverage: {covered_nodes} / {total_nodes} ({pct:.1f}%)")
    if missing:
        print("  [WARN] Nodes missing in nodes.py:")
        for m in missing:
            print(f"    - {m}")
    else:
        print("  [OK] All original nodes are implemented in nodes.py and exposed!")

    # 2. Rule 2
    r2_init = check_rule_2_init_files()
    print(f"\n[Rule 2a] Folder __init__.py check: {len(r2_init)} violations")
    for v in r2_init:
        print(f"  [FAIL] {v}")
    if not r2_init:
        print("  [OK] Every directory under _Nodes has an __init__.py")

    r2_imports = check_rule_2_original_imports()
    print(f"\n[Rule 2b] Direct Original Node Imports in Extensions: {len(r2_imports)} violations")
    for v in r2_imports:
        print(f"  [FAIL] {v}")
    if not r2_imports:
        print("  [OK] Extensions create nodes cleanly through nodes.* factories")

    # 3. Rule 5
    r5 = check_rule_5_cjk_port_literals()
    print(f"\n[Rule 5] Hardcoded CJK Port Literals: {len(r5)} violations")
    for v in r5:
        print(f"  [FAIL] {v}")
    if not r5:
        print("  [OK] Zero CJK string literals passed to port lookups")

    # 4. Rule 4 Warnings
    r4 = check_rule_4_int_sentinels()
    print(f"\n[Rule 4] Enum Input Sentinels Audit: {len(r4)} warnings")
    for w in r4:
        print(f"  [WARN] {w}")

    # 5. Rule 3 Function Length Warnings
    r3 = check_rule_3_function_length(threshold=40)
    print(f"\n[Rule 3] Function Length > 40 Lines Guideline: {len(r3)} functions")
    for w in r3:
        print(f"  [INFO] {w}")

    print("\n" + "=" * 80)
    if r2_init or r2_imports or r5 or missing:
        print("[RESULT] LINT FAILED: Please fix the errors above.")
        return 1
    print("[RESULT] ALL BINDING RULES AND COVERAGE CHECKS PASSED!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
