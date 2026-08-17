import csv
import importlib.util
from pathlib import Path

current_dir = Path(__file__).resolve().parent
type_mgr_path = current_dir / "TypeMgr.py"

# Dynamically load PlantType from TypeMgr.py
spec = importlib.util.spec_from_file_location("TypeMgr", type_mgr_path)
if spec and spec.loader:
    type_mgr_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(type_mgr_mod)
    PlantType = type_mgr_mod.PlantType
else:
    raise ImportError(f"Could not load TypeMgr from: {type_mgr_path}")

# Build ID -> Enum Name mapping
ID_TO_ENUM_NAME = {member.value: member.name for member in PlantType}


def generate_all():
    current_dir = Path(__file__).resolve().parent
    asset_path = current_dir.parent / "Assets" / "plant_data"

    if not asset_path.exists():
        raise FileNotFoundError(f"Could not find asset file at: {asset_path}")

    raw_bytes = asset_path.read_bytes()
    try:
        content = raw_bytes.decode("gbk")
    except UnicodeDecodeError:
        content = raw_bytes.decode("utf-8-sig", errors="replace")

    reader = csv.reader(content.splitlines())
    _ = next(reader, None)  # Skip header row

    plants = []
    for row in reader:
        if not row or len(row) < 8:
            continue
        try:
            plant_id = int(row[0].strip())
            atk_interval = float(row[1].strip())
            prod_interval = float(row[2].strip())
            atk_dmg = int(float(row[3].strip()))
            max_hp = int(float(row[4].strip()))
            cd = float(row[5].strip())
            cost = int(float(row[6].strip()))
            name = row[7].strip()

            # Resolve function name strictly from PlantType enum
            enum_name = ID_TO_ENUM_NAME.get(plant_id)
            if not enum_name:
                print(f"[Warning] ID {plant_id} ({name}) not found in PlantType enum. Skipping method.")
                continue

            plants.append({
                "id": plant_id,
                "enum_name": enum_name,
                "atk_interval": atk_interval,
                "prod_interval": prod_interval,
                "atk_dmg": atk_dmg,
                "max_hp": max_hp,
                "cd": cd,
                "cost": cost,
                "name": name,
            })
        except ValueError:
            continue

    # 1. Generate plant_defaults.py
    defaults_lines = [
        "# Auto-generated from Assets/plant_data. Do not edit manually.",
        "from typing import Dict, NamedTuple",
        "",
        "class PlantDefaultStats(NamedTuple):",
        "    id: int",
        "    cost: int",
        "    cd: float",
        "    max_health: int",
        "    attack_damage: int",
        "    attack_interval: float",
        "    produce_interval: float",
        "    name: str",
        "",
        "PLANT_DEFAULTS: Dict[int, PlantDefaultStats] = {",
    ]

    for p in plants:
        defaults_lines.append(
            f"    {p['id']}: PlantDefaultStats({p['id']}, {p['cost']}, {p['cd']}, "
            f"{p['max_hp']}, {p['atk_dmg']}, {p['atk_interval']}, {p['prod_interval']}, {p['name']!r}),"
        )
    defaults_lines.append("}\n")

    (current_dir / "plant_defaults.py").write_text("\n".join(defaults_lines), encoding="utf-8")

    # 2. Generate plant_data_methods.py
    method_lines = [
        "# Auto-generated helper methods with default parameter values for IDE tooltips.",
        "from typing import Dict, Any",
        "",
        "class PlantDataMethodsMixin:",
    ]

    for p in plants:
        method_name = p["enum_name"]
        doc = (
            f'        """PlantType.{method_name} ({p["id"]})\n'
            f'        Defaults: Cost={p["cost"]} | CD={p["cd"]}s | HP={p["max_hp"]} | '
            f'DMG={p["atk_dmg"]} | AtkInt={p["atk_interval"]}s | ProdInt={p["prod_interval"]}s\n'
            f'        """'
        )
        method_lines.extend([
            f"    @classmethod",
            f"    def {method_name}(",
            f"        cls,", 
            f"        cost: int = {p['cost']},",
            f"        cd: float = {p['cd']},",
            f"        max_health: int = {p['max_hp']},",
            f"        attack_damage: int = {p['atk_dmg']},",
            f"        attack_interval: float = {p['atk_interval']},",
            f"        produce_interval: float = {p['prod_interval']},",
            f"    ) -> Dict[str, Any]:",
            doc,
            f"        return cls.create({p['id']}, cost, cd, max_health, attack_damage, attack_interval, produce_interval)",
            "",
        ])

    (current_dir / "plant_data_methods.py").write_text("\n".join(method_lines), encoding="utf-8")
    print(f"Successfully generated methods for {len(plants)} plants matching PlantType enum.")


if __name__ == "__main__":
    generate_all()