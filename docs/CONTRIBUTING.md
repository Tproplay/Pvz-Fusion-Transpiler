# Contributing & Forking Guidelines

Thank you for your interest in contributing to or forking the **PvZ Fusion Transpiler**! This project welcomes improvements, bug fixes, updated game node bindings, and new gameplay DSL features.

---

## 1. Setting Up Your Development Environment

### Prerequisites
- **Python**: 3.10+ (tested up to Python 3.14).
- **Node.js & npm** (optional, for running `npx pyright` type checks).
- **Git**.

### Installation Steps

1. **Clone or Fork the Repository**:
   ```bash
   git clone https://github.com/Tproplay/Pvz-Fusion-Transpiler.git
   cd "Pvz Fusion Transpiler"
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install in Editable Mode**:
   ```bash
   pip install -e PvZ_Fusion_Transpiler_src
   ```

4. **Verify Type Checker Configuration**:
   The project contains a [`pyrightconfig.json`](../pyrightconfig.json) configuring include paths and virtual environment resolution.
   Test pyright via:
   ```bash
   npx pyright
   ```
   Ensure it outputs `0 errors, 0 warnings, 0 informations`.

---

## 2. Running Tests

All unit tests reside in the [`tests/`](../tests/) directory:

```bash
# Run all unit tests
python -m unittest discover tests

# Or run a specific test suite
python -m unittest tests/test_export.py
python -m unittest tests/test_approved_extensions.py
```

When contributing new features:
1. Always add corresponding unit tests in a dedicated or existing test file in `tests/`.
2. Verify both the graph representation and the exported `.json` output.
3. Ensure no regressions in existing tests.

---

## 3. Branching & Commit Conventions

1. **Branches**:
   - Create a feature or bugfix branch off `main` or `root-rewrite`:
     ```bash
     git checkout -b feature/my-new-feature
     ```
2. **Commit Messages**:
   Follow conventional commits:
   - `feat: add support for NewNode`
   - `fix: correct port type validation on SetPlant`
   - `docs: update AI agent workflow instructions`
   - `test: add coverage for stage transitions`

3. **Pull Requests**:
   - Provide a clear description of the change.
   - Attach test results showing all unit tests passing.
   - Include pyright type check logs showing 0 errors and 0 warnings.
