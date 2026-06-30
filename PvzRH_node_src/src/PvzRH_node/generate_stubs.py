import os
import sys
import re
import shutil

def build_autocomplete_stubs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    nodes_file = os.path.join(script_dir, "nodes.py")

    if not os.path.exists(nodes_file):
        print(f"Error: Could not find 'nodes.py' at: {nodes_file}")
        return

    with open(nodes_file, "r", encoding="utf-8") as f:
        code = f.read()

    # Setup the header for the Type Stub file with strict Pylance operator mappings
    stub_lines = [
        "from .node_base import BaseNode, ExecutionPath",
        "from typing import Any, Union",
        "",
        "class PortReference(tuple):",
        "    # Document math and comparison operations to silence Pylance strict-mode",
        "    def __add__(self, other: Any) -> 'PortReference': ...",
        "    def __sub__(self, other: Any) -> 'PortReference': ...",
        "    def __mul__(self, other: Any) -> 'PortReference': ...",
        "    def __truediv__(self, other: Any) -> 'PortReference': ...",
        "    def __mod__(self, other: Any) -> 'PortReference': ...",
        "    def __radd__(self, other: Any) -> 'PortReference': ...",
        "    def __rsub__(self, other: Any) -> 'PortReference': ...",
        "    def __rmul__(self, other: Any) -> 'PortReference': ...",
        "    def __rtruediv__(self, other: Any) -> 'PortReference': ...",
        "    def __rmod__(self, other: Any) -> 'PortReference': ...",
        "    def __eq__(self, other: Any) -> 'PortReference': ...",
        "    def __ne__(self, other: Any) -> 'PortReference': ...",
        "    def __gt__(self, other: Any) -> 'PortReference': ...",
        "    def __lt__(self, other: Any) -> 'PortReference': ...",
        "    def __ge__(self, other: Any) -> 'PortReference': ...",
        "    def __le__(self, other: Any) -> 'PortReference': ...",
        "    # THE CRITICAL LINE: Tell Pylance that & and | return a PortReference chain link",
        "    def __and__(self, other: Any) -> 'PortReference': ...",
        "    def __or__(self, other: Any) -> 'PortReference': ...",
        ""
    ]

    class_blocks = re.split(r'^class ', code, flags=re.MULTILINE)[1:]

    for block in class_blocks:
        if not block.strip():
            continue
            
        class_name = block.split('(')[0].strip()
        ports = set(re.findall(r'([a-zA-Z0-9_]+)_PortName=', block))
        
        # --- THE FIX: SMART FILTERING ---
        # Separate Execution Triggers from Data Variables
        flow_ports = []
        data_ports = []
        
        for p in ports:
            pl = p.lower()
            # If it sounds like an event or is a known trigger logic port
            if pl.startswith("on") or pl.startswith("action") or p in [
                "trigger", "then", "else", "output", "loopBody", "cycle", 
                "completed", "success", "failed", "equal", "greater", "less"
            ]:
                flow_ports.append(p)
            else:
                data_ports.append(p)
        
        # 1. Build the .Output Path Accessor (ONLY Triggers, strictly PascalCase)
        accessor_name = f"_{class_name}Paths"
        stub_lines.append(f"class {accessor_name}:")
        if not flow_ports:
            stub_lines.append("    pass")
        else:
            for p in flow_ports:
                pascal_case = p[0].upper() + p[1:]
                stub_lines.append(f"    {pascal_case}: ExecutionPath")
        
        # 2. Build the Main Node Class (ONLY Data Variables, strictly exact case)
        stub_lines.append(f"\nclass {class_name}(BaseNode):")
        stub_lines.append("    def __init__(self, *args: Any, **kwargs: Any) -> None: ...")
        stub_lines.append(f"    Output: {accessor_name}")
        
        if not data_ports:
            # Even if a node has no default data variables, allow fallback property lookups safely
            stub_lines.append("    def __getattr__(self, name: str) -> PortReference: ...")
        else:
            for p in data_ports:
                stub_lines.append(f"    {p}: PortReference")
            # This catch-all line completely completely eliminates Pylance "Unknown Attribute" red lines
            stub_lines.append("    def __getattr__(self, name: str) -> PortReference: ...")
        stub_lines.append("")

    # Write to local workspace
    local_stub_path = os.path.join(script_dir, "nodes.pyi")
    with open(local_stub_path, "w", encoding="utf-8") as f:
        f.write("\n".join(stub_lines))
    print(f"✔ Cleaned up double-paths! Local stub generated at: {local_stub_path}")

    # Synchronize with Virtual Environment if applicable
    if sys.prefix != sys.base_prefix:
        for path in sys.path:
            if "site-packages" in path and path.startswith(sys.prefix):
                target_package_dir = os.path.join(path, "PvZRH_node")
                if os.path.exists(target_package_dir):
                    venv_stub_dest = os.path.join(target_package_dir, "nodes.pyi")
                    if os.path.abspath(local_stub_path) != os.path.abspath(venv_stub_dest):
                        shutil.copyfile(local_stub_path, venv_stub_dest)
                        print(f"✔ Synchronized clean stubs to virtual environment: {venv_stub_dest}")
                        break

if __name__ == "__main__":
    build_autocomplete_stubs()