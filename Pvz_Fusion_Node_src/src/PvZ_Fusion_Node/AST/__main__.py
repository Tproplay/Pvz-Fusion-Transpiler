"""
Command Line Interface for PvZ Fusion AST Transpiler.

Usage:
    python -m PvZ_Fusion_Node.AST input_script.py [-o output.json] [--dsl]
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from .transpiler import transpile_source, compile_ast
from ..Core.context import ctx


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transpile and compile Python level scripts to PvZ Fusion node graphs."
    )
    parser.add_argument("script", help="Path to input Python script")
    parser.add_argument(
        "-o", "--output",
        help="Path to output JSON file (defaults to ./Levels/<script_name>.json)",
        default=None,
    )
    parser.add_argument(
        "--dsl",
        action="store_true",
        help="Print the generated DSL Python code instead of compiling to JSON",
    )

    args = parser.parse_args()

    if not os.path.exists(args.script):
        print(f"Error: Script file not found: {args.script}", file=sys.stderr)
        sys.exit(1)

    with open(args.script, "r", encoding="utf-8") as f:
        source = f.read()

    if args.dsl:
        dsl_code = transpile_source(source)
        print(dsl_code)
        return

    # Compile to level JSON
    ctx.reset()
    level = compile_ast(source)
    level_dict = level.to_dict()

    out_path = args.output
    if not out_path:
        base_name = os.path.splitext(os.path.basename(args.script))[0]
        os.makedirs("./Levels", exist_ok=True)
        out_path = os.path.join("./Levels", f"{base_name}.json")

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(level_dict, f, ensure_ascii=False, indent=2)

    print(f"Successfully compiled '{args.script}' to '{out_path}'.")


if __name__ == "__main__":
    main()
