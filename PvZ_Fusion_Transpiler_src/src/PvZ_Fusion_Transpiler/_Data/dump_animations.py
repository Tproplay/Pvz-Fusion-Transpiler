import os
import re
from typing import Optional


def dump_zombie_animations(
    log_path: Optional[str] = None,
    output_path: Optional[str] = None,
) -> None:
    """Internal utility to parse a MelonLoader dump log and generate ZombieAnimations.py."""
    if log_path is None:
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Dumps", "LatestAnimations.log")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    if output_path is None:
        output_path = os.path.join(base_dir, "ZombieAnimations.py")

    try:
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Could not find dump log at '{log_path}'")
        return

    zombies: dict[str, list[str]] = {}
    current_zombie: Optional[str] = None
    for line in lines:
        if "ZombieType:" in line:
            match = re.search(r"ZombieType:\s*([a-zA-Z0-9__]+)", line)
            if match:
                zombie_name = match.group(1)
                current_zombie = zombie_name
                zombies[zombie_name] = []
        elif "-> Clip:" in line and current_zombie:
            match = re.search(r"->\s*Clip:\s*(.*)", line)
            if match:
                clip_name = match.group(1).strip()
                zombies[current_zombie].append(clip_name)

    if not zombies:
        print(f"No zombie animation configurations parsed from '{log_path}'.")
        return

    code_lines = [
        "# Generated automatically from MelonLoader Zombie Prefab Dump Log",
        "from enum import Enum",
        "",
        "",
        "class ZombieAnimation:",
    ]

    for zombie_type, clips in zombies.items():
        if not clips:
            continue
        code_lines.append(f"    class {zombie_type}(Enum):")
        unique_clips = sorted(list(set(clips)))
        used_keys: set[str] = set()
        for clip in unique_clips:
            enum_key = clip.replace(" ", "_").replace("-", "_").upper()
            enum_key = re.sub(r"[^A-Z0-9_]", "_", enum_key)
            if enum_key and enum_key[0].isdigit():
                enum_key = f"ANIM_{enum_key}"
            base_key = enum_key
            suffix = 2
            while enum_key in used_keys:
                enum_key = f"{base_key}_{suffix}"
                suffix += 1
            used_keys.add(enum_key)
            code_lines.append(f'        {enum_key} = "{clip}"')
        code_lines.append("")

    code_lines.append("ZombieAnimations = ZombieAnimation")
    code_lines.append('__all__ = ["ZombieAnimations", "ZombieAnimation"]')
    code_lines.append("")

    full_code = "\n".join(code_lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_code)

    print(f"Successfully compiled nested enums for {len(zombies)} zombies from '{log_path}' into '{output_path}'.")


if __name__ == "__main__":
    dump_zombie_animations()
