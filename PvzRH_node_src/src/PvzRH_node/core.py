import uuid
import os
import json
import math
from typing import Dict, List, Any

class CompilerSettings:
    def __init__(self):
        # 0 = Heavy optimization + grid deduplication (Default production mode)
        # 1 = Group per line
        # 2 = Group by immediate parent indentation block
        # 3 = Group by outer grandparent indentation block
        self.group_level = 0

    def export_file(self, group_level=0):
        """Configures the structural layout pass mapping system."""
        self.group_level = group_level

settings = CompilerSettings()

class CompilerState:
    config: Dict[str, Any]
    nodes: List[Dict[str, Any]]
    connections: List[Dict[str, Any]]
    trigger_stack: List[Any]
    registry: Dict[str, Any]
    variables: List[Dict[str, Any]] 

    def __init__(self) -> None:
        self.config = {"output": "./", "name": "Custom_Level"}
        self.nodes = []
        self.connections = []
        self.trigger_stack = [] 
        self.registry = {}      
        self.variables = []
        self.groups_map = {}  # Tracks line-by-line source statements

    def generate_uuid(self) -> str:
        return str(uuid.uuid4())

    def add_connection(self, source_id: str, source_port: str, target_id: str, target_port: str) -> None:
        """Explicitly draws a wire between two node ports."""
        self.connections.append({
            "sourceNodeId": source_id,
            "sourcePortName": source_port,
            "targetNodeId": target_id,
            "targetPortName": target_port
        })

    def remove_connection(self, source_id: str = None, source_port: str = None, #type: ignore
                          target_id: str = None, target_port: str = None): #type: ignore
        """
        Removes connections from the compiler state that match the given parameters.
        Any parameter left as None acts as a wildcard.
        """
        original_count = len(self.connections)
        
        self.connections = [
            conn for conn in self.connections
            if not (
                (source_id is None or conn["sourceNodeId"] == source_id) and
                (source_port is None or conn["sourcePortName"] == source_port) and
                (target_id is None or conn["targetNodeId"] == target_id) and
                (target_port is None or conn["targetPortName"] == target_port)
            )
        ]
        
        return original_count - len(self.connections)
    
    def export(self) -> None:
        from .core import settings  # Import locally to prevent circular locks
        
        file_path = os.path.join(self.config["output"], f"{self.config['name']}.json")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        level_data = {}
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    level_data = json.load(f)
                print(f"Modifying existing premade level data found at: {file_path}")
            except Exception as e:
                print(f"Warning: Failed to read existing file ({e}). Creating a fresh level instead.")
                level_data = {}

        # =====================================================================
        # PASS 1: GRAPH OPTIMIZATION (DEDUFICATION) - Activated ONLY at Level 0
        # =====================================================================
        if settings.group_level == 0:
            DEDUPE_TYPES = {
                "IntValueNode", "FloatValueNode", "BoolValueNode", "StringValueNode",
                "OnBoardStartNode", "OnPlantCreateNode", "OnPlantClickNode", 
                "OnPlantDieNode", "OnZombieDieNode", "OnZombieSpawnNode", "WaveEventNode",
                "OnMouseClickNode", "OnKeyPressNode", "OnPlantDeathCompleteNode"
            }

            unique_nodes = {} 
            remap_dict = {}   
            optimized_nodes = []

            for node in self.nodes:
                if node["type"] in DEDUPE_TYPES:
                    kwargs_signature = json.dumps(node.get("kwargs", {}), sort_keys=True)
                    signature = f"{node['type']}_{kwargs_signature}"
                    
                    if signature in unique_nodes:
                        remap_dict[node["id"]] = unique_nodes[signature]
                    else:
                        unique_nodes[signature] = node["id"]
                        optimized_nodes.append(node)
                else:
                    optimized_nodes.append(node)
                    
            self.nodes = optimized_nodes

            optimized_conns = []
            unique_conn_signatures = set()
            
            for conn in self.connections:
                src = remap_dict.get(conn["sourceNodeId"], conn["sourceNodeId"])
                tgt = remap_dict.get(conn["targetNodeId"], conn["targetNodeId"])
                
                conn_signature = f"{src}:{conn['sourcePortName']}->{tgt}:{conn['targetPortName']}"
                
                if conn_signature not in unique_conn_signatures:
                    unique_conn_signatures.add(conn_signature)
                    optimized_conns.append({
                        "sourceNodeId": src,
                        "sourcePortName": conn["sourcePortName"],
                        "targetNodeId": tgt,
                        "targetPortName": conn["targetPortName"]
                    })
            self.connections = optimized_conns

        # =====================================================================
        # PASS 2: LAYOUT ENGINE (Standard Word-Wrap vs Hierarchical Square Grids)
        # =====================================================================
        node_positions = {}

        if settings.group_level == 0:
            # High-efficiency Production Packing Grid Layout
            N = len(self.nodes)
            grid_size = int(math.ceil(math.sqrt(N))) if N > 0 else 1
            X_SPACING = 220.0
            Y_SPACING = 170.0
            
            in_degree = {node["id"]: 0 for node in self.nodes}
            adj = {node["id"]: [] for node in self.nodes}
            
            for conn in self.connections:
                src = conn["sourceNodeId"]
                tgt = conn["targetNodeId"]
                if src in in_degree and tgt in in_degree:
                    adj[src].append(tgt)
                    in_degree[tgt] += 1
                    
            queue = [n_id for n_id, deg in in_degree.items() if deg == 0]
            sorted_nodes = []
            
            while queue:
                curr = queue.pop(0)
                sorted_nodes.append(curr)
                for neighbor in adj[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
                        
            visited = set(sorted_nodes)
            for node in self.nodes:
                if node["id"] not in visited:
                    sorted_nodes.append(node["id"])
                    
            for index, n_id in enumerate(sorted_nodes):
                col = index % grid_size
                row = index // grid_size
                node_positions[n_id] = {"x": col * X_SPACING, "y": row * Y_SPACING}
        else:
            current_x = 0.0
            current_y = 120.0
            
            X_SPACING = 240.0
            Y_SPACING = 180.0
            ROW_RESET_LIMIT = 3.0
            
            group_index = 0
            max_row_height = 0.0
            
            for code_line, grp in self.groups_map.items():
                num_nodes = len(grp["nodeIds"])
                if num_nodes == 0:
                    continue
                
                if group_index > 0 and group_index % ROW_RESET_LIMIT == 0:
                    current_x = 0.0
                    current_y += max_row_height + 150.0 
                    max_row_height = 0.0
                
                group_grid_size = int(math.ceil(math.sqrt(num_nodes)))
                
                for index, n_id in enumerate(grp["nodeIds"]):
                    col = index % group_grid_size
                    row = index // group_grid_size
                    
                    node_positions[n_id] = {
                        "x": current_x + (col * X_SPACING),
                        "y": current_y + 80.0 + (row * Y_SPACING)
                    }
                    
                    node_height = 80.0 + (row * Y_SPACING)
                    if node_height > max_row_height:
                        max_row_height = node_height
                
                grp["position"] = {"x": current_x - 30.0, "y": current_y}
                
                actual_cols = min(num_nodes, group_grid_size)
                group_width = actual_cols * X_SPACING
                current_x += group_width + 120.0
                
                group_index += 1

        # =====================================================================
        # PASS 3: NATIVE SCHEMA EXPORT STITCHING
        # =====================================================================
        level_data["eventNodeGraph"] = {
            "nodes": [],
            "connections": self.connections,
            "variables": [],
            "groups": []
        }
        level_data["references"] = {"version": 2, "RefIds": []}

        num_nodes = len(self.nodes)
        
        active_groups = []
        if settings.group_level >= 1:
            active_groups = [grp for grp in self.groups_map.values() if grp["nodeIds"]]
            
        num_groups = len(active_groups)
        
        asset_rid_map = {}
        variables_list = getattr(self, "variables", [])
        
        next_asset_rid = 1000 + num_nodes + num_groups
        
        for var_asset in variables_list:
            old_rid = var_asset["rid"]
            asset_rid_map[old_rid] = next_asset_rid
            var_asset["rid"] = next_asset_rid
            next_asset_rid += 1

        current_rid = 1000
        for node in self.nodes:
            level_data["eventNodeGraph"]["nodes"].append({"rid": current_rid})
            pos = node_positions.get(node["id"], {"x": 0.0, "y": 0.0})

            node_data = {
                "nodeId": node["id"],
                "nodeType": node["type"],
                "position": pos,
                "nodeName": node["type"]
            }
            for key, value in node.get("kwargs", {}).items():
                node_data[key] = value

            if "asset" in node_data and isinstance(node_data["asset"], dict) and "rid" in node_data["asset"]:
                old_rid = node_data["asset"]["rid"]
                if old_rid in asset_rid_map:
                    node_data["asset"]["rid"] = asset_rid_map[old_rid]

            level_data["references"]["RefIds"].append({
                "rid": current_rid,
                "type": {"class": node["type"], "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp"},
                "data": node_data
            })
            current_rid += 1

        # Only register NodeGroup structures if grouping is active (>= 1)
        if settings.group_level >= 1:
            for code_line, grp in self.groups_map.items():
                if not grp["nodeIds"]:
                    continue
                
                level_data["eventNodeGraph"]["groups"].append({"rid": current_rid})
                level_data["references"]["RefIds"].append({
                    "rid": current_rid,
                    "type": {"class": "NodeGroup", "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp"},
                    "data": {
                        "groupId": grp["groupId"],
                        "title": code_line,
                        "nodeIds": grp["nodeIds"],
                        "position": grp["position"],
                        "isFolded": False
                    }
                })
                current_rid += 1

        for var_asset in variables_list:
            level_data["eventNodeGraph"]["variables"].append({"rid": var_asset["rid"]})
            level_data["references"]["RefIds"].append(var_asset)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(level_data, f, indent=4, ensure_ascii=False)
            
        print(f"Successfully Packed and Exported to: {file_path}")


ctx = CompilerState()

