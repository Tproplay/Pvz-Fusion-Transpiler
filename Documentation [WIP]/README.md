
# Importing & Exporting guide

## Core

```python
import PvzRH_node as pvn
```

This import contains everything you will need for creating most simple levels.

> All of the methods/classes from this library are listed [here](https://github.com/Tproplay/Pvz-Fusion-Transpiler/tree/main/Documentation%20%5BWIP%5D/Core)

---

## Exporting the level

Exporting your level is fully automated. You do not need to manually create JSON files or format strings.

- **The Process**: Simply execute your Python script file.
- **The Output**: The compiler looks for the specific JSON path configured in your script. It will **either overwrite the existing file** with your updated graph data or **create a brand-new file** if it does not yet exist.

## Export settings

### Output folder

```python
pvn.Config(output="Levels", name="My Level")
```

You can specify the output folder and level file name. If the file already exists, its level configuration and graph data will be updated.

### Output formatting

This library allows you to customize the organization, folding, and visual layout of the generated node canvas.

`pvn.settings` contains all compiler layout configurations:

* **`group_level`** *(int)* — Controls how nodes are organized into visual groups on the canvas:


* **`0` (Default)**: Disables code grouping. Nodes are placed in a flat execution grid.


* **`1+`**: Enables hierarchical grouping. Groups nodes by code statements and scopes, arranging them in a clean square grid pattern.




* **`fold_all_groups`** *(bool)* — Default: `False`. When set to `True`, all generated groups are collapsed by default in the visual editor. Folded groups occupy a compact single-node slot on the canvas grid.


* **`spacing_x` / `spacing_y`** *(float)* — Horizontal and vertical grid spacing for ungrouped nodes (`group_level = 0`).


* **`hierarchical_spacing_x` / `hierarchical_spacing_y`** *(float)* — Grid spacing for nodes inside groups (`group_level >= 1`).



---

## Grouping Tools

### `@pvn.node_group` Decorator

When building helper functions or third-party libraries across multiple files, use the `@pvn.node_group` decorator. It intercepts and captures all nodes generated during that function's execution, pulling them out of line-by-line groups and bundling them into an isolated group:

```python
from typing import Optional
import PvzRH_node as pvn
from PvzRH_node import FloatVar, IntVar


@pvn.node_group("Custom Damage Calculation", folded=True)
def calculate_damage(base_damage: IntVar, multiplier: float) -> IntVar:
    result = IntVar(name="Calculated_Damage")
    result.set(base_damage * multiplier)
    return result

```

Parameters:

* **`name`** *(Optional[str])*: The display title of the node group box. If omitted or `None`, it defaults to the function name.


* **`folded`** *(Optional[bool])*: Explicitly collapses or expands the group box. If `None`, it defaults to `pvn.settings.fold_all_groups`.
