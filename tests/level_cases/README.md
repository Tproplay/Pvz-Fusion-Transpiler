# Level Snapshot Test Cases (`tests/level_cases/`)

Each test case consists of a paired `.py` script and a stripped `.json` expected output in this directory:

* `<case_name>.py` — Python DSL script using `PvZ_Fusion_Transpiler`.
* `<case_name>.json` — Stripped PvZ Fusion snapshot containing `eventNodeGraph` and `references` (without layout positions, `inputDefaults`, `*_PortName`, or board config noise), using symbolic ID bindings (`@node_X`, `@rid_X`, `@var_X`) and `{"$regex": "..."}` patterns.

### Adding a New Case

1. Place your level script at `tests/level_cases/03_my_case.py`.
2. Export your ground-truth level JSON from the game or compiler, then strip it into the snapshot template:
   ```powershell
   python tools/strip_level.py "path/to/Test.json" "tests/level_cases/03_my_case.json"
   ```
3. Run the automated verification suite:
   ```powershell
   python -m unittest tests/test_level_cases.py
   ```
