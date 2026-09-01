
# Importing & Exporting Guide

## Core

```python
import PvzRH_node as pvn
```

This import contains everything you need for creating most simple levels — triggers, control flow, variables, board/economy helpers, spawning, and UI.

> All of the methods/classes from this library are listed [here](https://github.com/Tproplay/Pvz-Fusion-Transpiler/tree/main/Documentation%20%5BWIP%5D/Core)

### Additional Imports

A few pieces live in separate modules and are not part of the main `pvn` namespace. Import whichever of these you need:

```python
from PvzRH_node.Types import *   # KeyCode, SoundType, SceneType, LevelType,
                                  # TravelBuffType, ZombieAnimation, Plant_DieReason, RecipeData
from PvzRH_node.Math import *    # Math helper functions (abs, max, min, ...) and constants (PI, E, TAU, ...)
from PvzRH_node.StdLib import *  # String/utility helpers such as format_string
```

> **Note:** `PlantType` and `ZombieType` are the exception — they're already available directly from `pvn` (`pvn.PlantType`, `pvn.ZombieType`), so you don't need `PvzRH_node.Types` for those two.

---

## Exporting the Level

Exporting your level is fully automated. You do not need to manually create JSON files or format strings.

- **The Process**: Simply execute your Python script file.
- **The Output**: The compiler looks for the specific JSON path configured in your script. It will **either overwrite the existing file** with your updated graph data or **create a brand-new file** if it does not yet exist.

## Export Settings

### Output Folder

```python
pvn.Config(output="Levels", name="My Level")
```

You can specify the output folder and level file name. If the file already exists, its level configuration and graph data will be updated.

### Output Formatting

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

### `@pvn.single_group` Decorator

When building helper functions or third-party libraries across multiple files, use the `@pvn.single_group` decorator. It intercepts all nodes generated during that function's execution, pulls them out of their default line-by-line groups, and bundles them into a single isolated group:

```python
from typing import Optional
import PvzRH_node as pvn
from PvzRH_node import FloatVar, IntVar


@pvn.single_group("Custom Damage Calculation", folded=True)
def calculate_damage(base_damage: IntVar, multiplier: float) -> IntVar:
    result = IntVar(name="Calculated_Damage")
    result.set(base_damage * multiplier)
    return result
```

Parameters:

* **`name`** *(Optional[str])*: The display title of the node group box. If omitted or `None`, it defaults to the function name.
* **`folded`** *(Optional[bool])*: Explicitly collapses or expands the group box. If `None`, it defaults to `pvn.settings.fold_all_groups`.

> **Note:** Groups are only visible in the exported canvas when `pvn.settings.group_level` is `1` or higher (see [Output Formatting](#output-formatting) above). With the default `group_level = 0`, nodes are still tagged internally but rendered in the flat grid instead.
