from __future__ import annotations

import copy
import json
import math
import os
import uuid
from functools import wraps
from typing import Any, List, Optional

from .Data.DataFactory import _to_json_val


class CompilerSetting:
    """Configures layout, spacing, and grouping behavior for exported node graphs."""

    group_level: int = 0
    """Controls how nodes are visually organized into groups on the canvas:
    
    0: Disabled (default). Nodes are arranged in a flat, topological grid.
    
    1+: Enabled. Groups nodes by code statements, scopes, and decorators in a square grid layout.
    """

    fold_all_groups: bool = False
    """When True, all visual node groups are collapsed/folded by default in the editor.
    
    Folded groups occupy a compact 1-node footprint on the global layout grid.
    """

    spacing_x: float = 220.0
    """Horizontal grid spacing between adjacent nodes when group_level = 0."""

    spacing_y: float = 170.0
    """Vertical grid spacing between adjacent nodes when group_level = 0."""

    hierarchical_spacing_x: float = 240.0
    """Horizontal grid spacing between nodes inside visual groups when group_level >= 1."""

    hierarchical_spacing_y: float = 180.0
    """Vertical grid spacing between nodes inside visual groups when group_level >= 1."""


settings = CompilerSetting()
"""Configures layout, spacing, and grouping behavior for exported node graphs."""

class CompilerState:
    def __init__(self) -> None:
        from .Data.DataFactory import BoardConfig, BoardTag, LevelConfig

        self.config = {"output": "./", "name": "exported level"}
        self.nodes = []
        self.connections = []
        self.trigger_stack = []
        self.registry = {}
        self.variables = []

        self.group_level = settings.group_level
        self.spacing_x = settings.spacing_x
        self.spacing_y = settings.spacing_y
        self.hierarchical_spacing_x = settings.hierarchical_spacing_x
        self.hierarchical_spacing_y = settings.hierarchical_spacing_y
        self.groups_map = {}

        # LEVEL CONFIGURATION PROXY
        self.level_config = LevelConfig(self)

        self.board_config = BoardConfig()
        self.board_tag = BoardTag()

        self.name: Optional[str] = None
        self.level_number: Optional[int] = None
        self.scene_type: Optional[int] = None
        self.level_type: Optional[int] = None
        self.start_sun: Optional[int] = None
        self.max_wave: Optional[int] = None
        self.card_count: Optional[int] = None
        self.victory_type: Optional[int] = None

        self.plant_datas: Optional[List[dict[str, Any]]] = None
        self.plants: Optional[List[dict[str, Any]]] = None
        self.pre_select_cards: Optional[List[Any]] = None
        self.pre_select_cards_zombie: Optional[List[Any]] = None

        self.adv_buffs: Optional[List[int]] = None
        self.ulti_buffs: Optional[List[int]] = None
        self.ulti_buffs2: Optional[List[int]] = None
        self.travel_debuffs: Optional[List[int]] = None

        self.spawn_zombies: Optional[List[Any]] = None
        self.ordered_spawns: Optional[List[dict[str, Any]]] = None
        self.god_plants: Optional[List[dict[str, Any]]] = None

    def _generate_uuid(self) -> str:
        return str(uuid.uuid4())

    def add_connection(self, source_id: str, source_port: str, target_id: str, target_port: str) -> None:
        self.connections.append(
            {
                "sourceNodeId": source_id,
                "sourcePortName": source_port,
                "targetNodeId": target_id,
                "targetPortName": target_port,
            }
        )

    def remove_connection(
        self,
        source_id: str = None,  # type: ignore
        source_port: str = None,  # type: ignore
        target_id: str = None,  # type: ignore
        target_port: str = None,  # type: ignore
    ):
        original_count = len(self.connections)
        self.connections = [
            conn
            for conn in self.connections
            if not (
                (source_id is None or conn["sourceNodeId"] == source_id)
                and (source_port is None or conn["sourcePortName"] == source_port)
                and (target_id is None or conn["targetNodeId"] == target_id)
                and (target_port is None or conn["targetPortName"] == target_port)
            )
        ]
        return original_count - len(self.connections)

    def export(self) -> None:
        from .Data.DataFactory import DEFAULT_LEVEL_TEMPLATE

        self.group_level = settings.group_level
        self.spacing_x = settings.spacing_x
        self.spacing_y = settings.spacing_y
        self.hierarchical_spacing_x = settings.hierarchical_spacing_x
        self.hierarchical_spacing_y = settings.hierarchical_spacing_y

        file_name = self.config.get("name", "exported level")
        file_path = os.path.join(self.config["output"], f"{file_name}.json")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        is_new_file = not os.path.exists(file_path)
        level_data = {}

        if not is_new_file:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    level_data = json.load(f)
                print(f"Modifying existing premade level data found at: {file_path}")
            except Exception as e:
                print(f"Warning: Failed to read existing file ({e}). Creating a fresh level instead.")
                is_new_file = True
                level_data = copy.deepcopy(DEFAULT_LEVEL_TEMPLATE)
        else:
            level_data = copy.deepcopy(DEFAULT_LEVEL_TEMPLATE)

        # =====================================================================
        # PASS 0: MERGE LEVEL CONFIGURATION DATA SELECTIVELY
        # =====================================================================
        if self.name is not None:
            level_data["name"] = self.name
        elif is_new_file:
            level_data["name"] = file_name if self.config.get("name") else "Unnamed"

        if self.level_number is not None:
            level_data["levelNumber"] = self.level_number
        elif is_new_file:
            level_data["levelNumber"] = 8001

        if self.scene_type is not None:
            level_data["sceneType"] = _to_json_val(self.scene_type)
        if self.level_type is not None:
            level_data["levelType"] = _to_json_val(self.level_type)
        if self.start_sun is not None:
            level_data["startSun"] = self.start_sun
        if self.max_wave is not None:
            level_data["maxWave"] = self.max_wave
        if self.card_count is not None:
            level_data["cardCount"] = self.card_count
        if self.victory_type is not None:
            level_data["victoryType"] = self.victory_type

        if not is_new_file and "boardConfig" in level_data:
            for k in self.board_config._dirty_keys:
                level_data["boardConfig"][k] = getattr(self.board_config, k)
        elif self.board_config._dirty or is_new_file:
            level_data["boardConfig"] = self.board_config.to_dict()

        if not is_new_file and "boardTag" in level_data:
            for k in self.board_tag._dirty_keys:
                level_data["boardTag"][k] = getattr(self.board_tag, k)
        elif self.board_tag._dirty or is_new_file:
            level_data["boardTag"] = self.board_tag.to_dict()

        if self.plant_datas is not None:
            level_data["plantDatas"] = _to_json_val(self.plant_datas)
        if self.plants is not None:
            level_data["plants"] = _to_json_val(self.plants)
            for plant in level_data["plants"]:
                if isinstance(plant, dict):
                    plant["objects"] = []
        if self.pre_select_cards is not None:
            level_data["preSelectCards"] = _to_json_val(self.pre_select_cards)
        if self.pre_select_cards_zombie is not None:
            level_data["preSelectCards_zombie"] = _to_json_val(self.pre_select_cards_zombie)
        if self.adv_buffs is not None:
            level_data["advBuffs"] = _to_json_val(self.adv_buffs)
        if self.ulti_buffs is not None:
            level_data["ultiBuffs"] = _to_json_val(self.ulti_buffs)
        if self.ulti_buffs2 is not None:
            level_data["ultiBuffs2"] = _to_json_val(self.ulti_buffs2)
        if self.travel_debuffs is not None:
            level_data["travelDebuffs"] = _to_json_val(self.travel_debuffs)
        if self.spawn_zombies is not None:
            level_data["SpawnZombies"] = _to_json_val(self.spawn_zombies)
        if self.ordered_spawns is not None:
            level_data["orderedSpawns"] = _to_json_val(self.ordered_spawns)
        if self.god_plants is not None:
            level_data["GodShootingConfig"] = {"plants": _to_json_val(self.god_plants)}

        # =====================================================================
        # PASS 1: GRAPH OPTIMIZATION (DEDUPLICATION)
        # =====================================================================
        if self.group_level == 0:
            DEDUPE_TYPES = {
                "IntValueNode", "FloatValueNode", "BoolValueNode", "StringValueNode",
                "OnBoardStartNode", "OnPlantCreateNode", "OnPlantClickNode",
                "OnPlantDieNode", "OnZombieDieNode", "OnZombieSpawnNode", "WaveEventNode",
                "OnMouseClickNode", "OnKeyPressNode", "OnPlantDeathCompleteNode",
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
                    optimized_conns.append(
                        {
                            "sourceNodeId": src,
                            "sourcePortName": conn["sourcePortName"],
                            "targetNodeId": tgt,
                            "targetPortName": conn["targetPortName"],
                        }
                    )
            self.connections = optimized_conns

        # =====================================================================
        # PASS 2: LAYOUT ENGINE (SQUARE GRID & FOLDED FOOTPRINT AWARE)
        # =====================================================================
        
        node_positions = {}

        if self.group_level == 0:
            N = len(self.nodes)
            grid_size = int(math.ceil(math.sqrt(N))) if N > 0 else 1
            X_SPACING = self.spacing_x
            Y_SPACING = self.spacing_y

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
            X_SPACING = self.hierarchical_spacing_x
            Y_SPACING = self.hierarchical_spacing_y
            GAP_X = 80.0
            GAP_Y = 80.0

            # 1. Collect all explicit groups that have nodes
            all_groups: list[dict[str, Any]] = [
                grp for grp in self.groups_map.values() if grp.get("nodeIds")
            ]

            # 2. Collect any orphaned nodes into the Global Constants group
            grouped_node_ids = set()
            for grp in all_groups:
                grouped_node_ids.update(grp["nodeIds"])

            orphaned_node_ids = [n["id"] for n in self.nodes if n["id"] not in grouped_node_ids]
            if orphaned_node_ids:
                orphan_group = {
                    "groupId": self._generate_uuid(),
                    "title": "Global Constants & Variables",
                    "nodeIds": orphaned_node_ids,
                    "position": {"x": 0.0, "y": 0.0},
                    "isFolded": settings.fold_all_groups,
                }
                self.groups_map["Global Constants & Variables"] = orphan_group
                all_groups.insert(0, orphan_group)

            # 3. Compute bounding dimensions and internal columns for every group
            for grp in all_groups:
                num_nodes = len(grp["nodeIds"])
                is_folded = grp.get("isFolded", settings.fold_all_groups)
                grp["_is_folded"] = is_folded

                # Calculate internal grid layout dimensions
                cols = int(math.ceil(math.sqrt(num_nodes))) if num_nodes > 0 else 1
                rows = int(math.ceil(num_nodes / cols)) if num_nodes > 0 else 1
                grp["_cols"] = cols

                if is_folded:
                    # Canvas spacing allocates 1 compact node slot
                    grp["_layout_w"] = X_SPACING
                    grp["_layout_h"] = 90.0
                else:
                    # Open groups allocate full width and height
                    grp["_layout_w"] = (cols * X_SPACING) + 40.0
                    grp["_layout_h"] = (rows * Y_SPACING) + 70.0

            # 4. Arrange groups in a balanced Square Grid
            total_groups = len(all_groups)
            grid_cols_count = max(1, int(math.ceil(math.sqrt(total_groups))))

            group_rows: list[list[dict[str, Any]]] = []
            current_row: list[dict[str, Any]] = []

            for grp in all_groups:
                current_row.append(grp)
                if len(current_row) >= grid_cols_count:
                    group_rows.append(current_row)
                    current_row = []
            if current_row:
                group_rows.append(current_row)

            # 5. Position groups and place internal nodes in an organized sub-grid
            current_y = 100.0
            for row in group_rows:
                row_max_h = max(g["_layout_h"] for g in row)
                current_x = 100.0

                for grp in row:
                    grp_x = current_x
                    grp_y = current_y
                    grp["position"] = {"x": grp_x, "y": grp_y}

                    cols = grp["_cols"]

                    # Position all child nodes in a clean sub-grid relative to the group
                    for n_idx, n_id in enumerate(grp["nodeIds"]):
                        c = n_idx % cols
                        r = n_idx // cols
                        node_positions[n_id] = {
                            "x": grp_x + 20.0 + (c * X_SPACING),
                            "y": grp_y + 50.0 + (r * Y_SPACING),
                        }

                    current_x += grp["_layout_w"] + GAP_X

                current_y += row_max_h + GAP_Y

        # =====================================================================
        # PASS 3: NATIVE SCHEMA EXPORT STITCHING
        # =====================================================================
        level_data["eventNodeGraph"] = {
            "nodes": [],
            "connections": self.connections,
            "variables": [],
            "groups": [],
        }
        level_data["references"] = {"version": 2, "RefIds": []}

        num_nodes = len(self.nodes)
        active_groups = [grp for grp in self.groups_map.values() if grp["nodeIds"]] if self.group_level >= 1 else []
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
                "nodeName": node["type"],
            }
            for key, value in node.get("kwargs", {}).items():
                node_data[key] = value

            if "asset" in node_data and isinstance(node_data["asset"], dict) and "rid" in node_data["asset"]:
                old_rid = node_data["asset"]["rid"]
                if old_rid in asset_rid_map:
                    node_data["asset"]["rid"] = asset_rid_map[old_rid]

            level_data["references"]["RefIds"].append(
                {
                    "rid": current_rid,
                    "type": {"class": node["type"], "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp"},
                    "data": node_data,
                }
            )
            current_rid += 1

        if self.group_level >= 1:
            for code_line, grp in self.groups_map.items():
                if not grp["nodeIds"]:
                    continue

                level_data["eventNodeGraph"]["groups"].append({"rid": current_rid})
                level_data["references"]["RefIds"].append(
                    {
                        "rid": current_rid,
                        "type": {"class": "NodeGroup", "ns": "GameLevel.EventNodes", "asm": "Assembly-CSharp"},
                        "data": {
                            "groupId": grp["groupId"],
                            "title": grp.get("title", code_line),
                            "nodeIds": grp["nodeIds"],
                            "position": grp["position"],
                            "isFolded": grp.get("isFolded", settings.fold_all_groups),
                        },
                    }
                )
                current_rid += 1

        for var_asset in variables_list:
            level_data["eventNodeGraph"]["variables"].append({"rid": var_asset["rid"]})
            level_data["references"]["RefIds"].append(var_asset)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(level_data, f, indent=4, ensure_ascii=False)

        print(f"Successfully Packed and Exported to: {file_path}")


ctx = CompilerState()


def _save_trigger_stack(clear: bool = True) -> list[Any]:
    saved_stack = ctx.trigger_stack[:]
    if clear:
        ctx.trigger_stack.clear()
    return saved_stack


def _restore_trigger_stack(saved_stack: list[Any]) -> None:
    ctx.trigger_stack.clear()
    ctx.trigger_stack.extend(saved_stack)


class IsolatedTriggerScope:
    """Context manager that temporarily isolates the compiler trigger stack.

    Saves and clears the active trigger stack upon entry, allowing internal nodes
    to be registered independently of parent execution chains. Restores the original
    trigger stack upon exiting the scope.
    """
    def __enter__(self):
        self.saved_stack = _save_trigger_stack(clear=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _restore_trigger_stack(self.saved_stack)


# =====================================================================
# LIBRARY & FUNCTION GROUP DECORATOR
# =====================================================================
def single_group(name: Optional[str] = None, folded: Optional[bool] = None):
    """
    Decorator to wrap all nodes generated inside a library function into an isolated, closed group.
    
    Usage:
        @single_group("Custom Math Function", folded=True)
        def complex_math_routine():
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Record number of nodes before function runs
            start_node_count = len(ctx.nodes)
            
            result = func(*args, **kwargs)
            
            end_node_count = len(ctx.nodes)
            
            # If nodes were generated, retroactively group them together
            if end_node_count > start_node_count:
                group_name = name or func.__name__
                is_folded = folded if folded is not None else settings.fold_all_groups
                
                # Initialize group if it doesn't exist yet
                if group_name not in ctx.groups_map:
                    ctx.groups_map[group_name] = {
                        "groupId": ctx._generate_uuid(),
                        "title": group_name,
                        "nodeIds": [],
                        "position": {"x": 0.0, "y": 0.0},
                        "isFolded": is_folded
                    }
                else:
                    ctx.groups_map[group_name]["isFolded"] = is_folded
                    
                new_node_ids = [n["id"] for n in ctx.nodes[start_node_count:end_node_count]]
                
                # Strip these nodes from any default trace-based groups
                for g_name, grp in ctx.groups_map.items():
                    if g_name != group_name:
                        grp["nodeIds"] = [nid for nid in grp["nodeIds"] if nid not in new_node_ids]
                        
                # Attach to our isolated function group
                ctx.groups_map[group_name]["nodeIds"].extend(new_node_ids)
                
            return result
        return wrapper
    return decorator