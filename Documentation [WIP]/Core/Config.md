# ⚙️ Level & Compiler Configuration

The `pft.Config` function and export pipeline manage output file destinations, graph layout, and seamless merging into existing game save files.

```python
import PvZ_Fusion_Transpiler as pft
```

---

## 1. Configuring Export Destination (`Config`)

Use `Config()` at the top of your level script to declare where the compiled JSON file will be written:

```python
pft.Config(
    output=r"C:\Users\User\Games\Pvz Fusion\Levels",
    name="MyCustomLevel"
)
```

### Parameters

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `output` | `str` | `"./"` | Target directory for the generated JSON file. |
| `name` | `str` | `"Untitled"` | File name. Appends `.json` automatically if omitted. |

---

## 2. Compilation & Export (`export`)

Exporting can be performed in two ways:

1. **Automatic (`atexit`)**: Running your script directly with Python automatically triggers `pft.export()` when the script finishes executing.
2. **Explicit (`pft.export()`)**: You can invoke `pft.export()` at any point:
   ```python
   # Export to configured path
   pft.export()

   # Or specify an explicit target path
   pft.export(filepath="./output/BossRush.json")
   ```

---

## 3. Preserving Existing Level Settings

When the target `.json` file already exists on disk:
- The transpiler **preserves** all game-level configurations, including:
  - Starting sun, card counts, scene background, victory conditions (`victory_type`)
  - Pre-selected card decks and allowed zombie pools
  - Scary pot definitions and minigame setup tables
  - Custom wave tables and spawn weights
- The transpiler **updates only**:
  - `references`: Dynamic object bindings, variable assets (`IntVariableAsset`, etc.), and node references.
  - `eventNodeGraph`: The complete serialized node graph (`nodes`, `connections`).

If the destination file does not exist, a new standalone level JSON containing the compiled node graph and references is created.

---

## 4. Automatic Node Layout

By default, all instantiated nodes are positioned in a clean square grid pattern using automatic coordinate calculation (`math.ceil(sqrt(N))` columns with spacing), ensuring that the visual node canvas in PvZ Fusion's editor is organized and readable.

If specific nodes have their `x` and `y` coordinates set manually, the compiler respects and preserves your custom layout.
