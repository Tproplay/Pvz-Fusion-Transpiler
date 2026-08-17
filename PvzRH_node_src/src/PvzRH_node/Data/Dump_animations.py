import re

def generate_enum_file(log_path=r"C:\Users\Tproplay\Games\Pvz\Fusion RH\English 3.9\MelonLoader\Latest.log", output_path="zombie_animations.py"):
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Could not find {log_path}")
        return

    zombies = {}
    current_zombie = None

    # Step 1: Parse line-by-line to extract zombie types and animation clips safely
    for line in lines:
        if "ZombieType:" in line:
            match = re.search(r"ZombieType:\s*([a-zA-Z0-9__]+)", line)
            if match:
                current_zombie = match.group(1)
                zombies[current_zombie] = []
        elif "-> Clip:" in line and current_zombie:
            match = re.search(r"->\s*Clip:\s*(.*)", line)
            if match:
                clip_name = match.group(1).strip()
                zombies[current_zombie].append(clip_name)

    if not zombies:
        print("No zombie animation configurations parsed. Double check file path contents.")
        return

    # Step 2: Assemble the structured python nested enum definitions
    code_lines = [
        "# Generated automatically from Magnetar Client Zombie Prefab Dump Log",
        "from enum import Enum",
        "",
        "class ZombieAnimation:"
    ]

    for zombie_type, clips in zombies.items():
        if not clips:
            continue
        
        code_lines.append(f"    class {zombie_type}(Enum):")
        
        # Deduplicate clips while keeping their internal names intact
        unique_clips = sorted(list(set(clips)))
        for clip in unique_clips:
            # Format the identifier to match standard UPPER_CASE styling
            enum_key = clip.replace(" ", "_").replace("-", "_").upper()
            
            # Prefix numeric keys to ensure valid python naming syntax
            if enum_key and enum_key[0].isdigit():
                enum_key = f"ANIM_{enum_key}"
                
            code_lines.append(f'        {enum_key} = "{clip}"')
        code_lines.append("") # Spacer between classes

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(code_lines))

    print(f"Successfully compiled nested enums for {len(zombies)} zombies into: {output_path}")

if __name__ == "__main__":
    generate_enum_file()