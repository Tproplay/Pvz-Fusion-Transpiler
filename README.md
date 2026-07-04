# Plants vs. Zombies Fusion Transpiler

An advanced scripting compiler designed to convert logic directly into complex visual node graphs for the **Plants vs. Zombies Fusion Custom Level Editor**.

This python library allows map designers, content creators, and modders to construct highly intricate custom levels, minigames, and interactive events using sequential text scripting instead of manually connecting hundreds of messy visual nodes inside the in-game editor interface 🎮.

---

## 🌟 Key Features

* **🔮 Visual Graph Transpilation**: Converts high-level structured text blocks straight into the game engine's native JSON layout formats.
* **📐 Smart Layout Engine**: Automatically organizes node positioning, maps group structures, and links frame execution lines flawlessly on the editor grid canvas.
* **⚡ Built-in Circuit Optimizations**: Includes automatic wire deduplication to keep custom levels memory-safe and prevent the game from lagging or freezing.
* **🔄 Advanced Control Flow**: Seamlessly handles loop architectures, complex if/else decision trees, and timed update behaviors.
* **🎯 Interactive UI Capabilities**: Supports generating multi-choice dynamic item selector menus natively inside your level loops.

---

## 💾 Installation Guide

The framework is packaged as a pre-built Python Wheel file (`.whl`) for easy, localized installation. Follow the steps below to set it up on your system ✨.

### 📋 Prerequisites
* **Python**: Ensure Python 3.10 or higher is installed on your computer 🐍.
* **Pip**: Make sure the Python package installer (`pip`) is updated to the latest version.

### 📦 Step 1: Download the Wheel File
Obtain the latest compiled release file from the repository's [releases section](https://github.com/Tproplay/Pvz-Fusion-Transpiler/releases).

### 💻 Step 2: Install via Command Line
Open your terminal or command prompt, navigate to the folder containing your downloaded `.whl` file, and execute the following installation command:

`pip install PvzRH_node-<version>-py3-none-any.whl`

*(Alternatively, if you are installing it directly to a local development sandbox environment, use: `pip install --force-reinstall PvzRH_node-<version>-py3-none-any.whl`)*

---

## 📁 Level Export Configuration

Once installed, the framework outputs your script files straight into the default custom levels sandbox storage folder of your Plants vs. Zombies Fusion game directory 📂.

### 🛠️ Default Save Target Configuration
To ensure your custom levels compile directly into the game's menu loader, point your level configuration script path to your game's app data directory structure.

---

## 🗺️ Visual Organization System

When generating intricate logic, the framework features adjustable organizational layout states to keep your canvas manageable 📑:

1. **Production Mode (Level 0) ⚙️**: Maximizes optimization and automatically removes overlapping nodes to save memory.
2. **Indentation Grouping (Level 1+) 🗂️**: Automatically wraps sequences inside collapsible text banners in the visual graph viewer based on your script layout lines, making manual edits inside the game simple and organized.