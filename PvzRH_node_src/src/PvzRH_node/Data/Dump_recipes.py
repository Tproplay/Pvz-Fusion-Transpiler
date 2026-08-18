import re
from pathlib import Path

# Regex to extract (id1) + (id2) -> (result_id)
RECIPE_PATTERN = re.compile(
    r"Found recipe:\s*[\w\s]+\((\d+)\)\s*\+\s*[\w\s]+\((\d+)\)\s*->\s*[\w\s]+\((\d+)\)"
)


def generate_recipe_file(
    input_filename: str = "recipes.log", output_filename: str = "recipe_data.py"
):
    current_dir = Path(__file__).resolve().parent.parent
    raw_file = current_dir / "Assets" / input_filename

    if not raw_file.exists():
        raise FileNotFoundError(f"Could not find recipe log dump at: {raw_file}")

    text = raw_file.read_text(encoding="utf-8", errors="ignore")

    pair_to_result = {}
    ingredient_to_results = {}
    result_to_parents = {}

    for match in RECIPE_PATTERN.finditer(text):
        p1 = int(match.group(1))
        p2 = int(match.group(2))
        res = int(match.group(3))

        pair = tuple(sorted((p1, p2)))
        pair_to_result[pair] = res

        ingredient_to_results.setdefault(p1, set()).add(res)
        ingredient_to_results.setdefault(p2, set()).add(res)

        parents = result_to_parents.setdefault(res, [])
        if pair not in parents:
            parents.append(pair)

    # Format into valid Python code
    lines = [
        "# Auto-generated recipe database. Do not edit manually.",
        "from typing import Dict, List, Set, Tuple",
        "",
        "# Map: (min(p1, p2), max(p1, p2)) -> result_id",
        "PAIR_TO_RESULT: Dict[Tuple[int, int], int] = {",
    ]

    for pair, res in sorted(pair_to_result.items()):
        lines.append(f"    {pair}: {res},")
    lines.append("}\n")

    lines.append("# Map: ingredient_id -> set of result_ids")
    lines.append("INGREDIENT_TO_RESULTS: Dict[int, Set[int]] = {")
    for ing, results in sorted(ingredient_to_results.items()):
        lines.append(f"    {ing}: {set(sorted(list(results)))},")
    lines.append("}\n")

    lines.append("# Map: result_id -> list of valid parent pairs [(p1, p2), ...]")
    lines.append("RESULT_TO_PARENTS: Dict[int, List[Tuple[int, int]]] = {")
    for res, parents in sorted(result_to_parents.items()):
        lines.append(f"    {res}: {parents},")
    lines.append("}\n")

    out_path = current_dir / "Data" / output_filename
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {out_path.name} with {len(pair_to_result)} unique recipes.")


if __name__ == "__main__":
    generate_recipe_file()