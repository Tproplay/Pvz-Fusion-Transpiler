# Plants vs. Zombies Fusion Transpiler

An advanced scripting compiler designed to convert logic directly into complex visual node graphs for the **Plants vs. Zombies Fusion Custom Level Editor**.

This python library allows level designers, content creators, and modders to construct highly intricate custom levels, minigames, and interactive events using sequential text scripting instead of manually connecting hundreds of messy visual nodes inside the in-game editor interface 🎮.

---

## 🌟 Key Features

* **🔮 Visual Graph Transpilation**: Converts high-level structured text blocks straight into the game engine's native JSON layout formats.
* **📐 Smart Layout Engine**: Automatically organizes node positioning, maps group structures, and links frame execution lines flawlessly on the editor grid canvas.
* **⚡ Built-in Circuit Optimizations**: Includes automatic wire deduplication to keep custom levels memory-safe and prevent the game from lagging or freezing.
* **🔄 Advanced Control Flow**: Seamlessly handles loop architectures, complex if/else decision trees, and timed update behaviors.
* **📚 Built-in libraries**: Have built-in libraries for performing advance mathematics functions.

---

## 💾 Installation Guide

### Prerequisite 

- Python 3.14+
- Basic programming knowledge

### How to install

Open Powershell/terminal and run the following:
```bash
pip install "git+https://github.com/Tproplay/Pvz-Fusion-Transpiler.git#subdirectory=PvzRH_node_src"
```

To update, run the following:
```bash
pip install --upgrade "git+https://github.com/Tproplay/Pvz-Fusion-Transpiler.git#subdirectory=PvzRH_node_src"
```

## 🚀 Getting Started

Follow this curated reading path to quickly get up to speed with the framework, from fundamental compiler mechanics to advanced gameplay systems.

---

### Recommended Reading Order

| Step | Topic | Guide | What You Will Learn |
| :--- | :--- | :--- | :--- |
| **1** | **Level Setup** | [`README.md`](Documentation%20[WIP]/README.md) | Initializing compiler configurations, save directories, and level metadata. |
| **2** | **State Management** | [`Variables.md`](Documentation%20[WIP]/Core/Variables.md) | Working with persistent canvas state nodes (`IntVar`, `FloatVar`, `BoolVar`). |
| **3** | **Event Lifecycle** | [`Triggers.md`](Documentation%20[WIP]/Core/Triggers.md) | Hooking into game lifecycle events (`OnGameStart`, `OnZombieSpawn`, key presses). |
| **4** | **Flow Control** | [`Conditional statements.md`](Documentation%20[WIP]/Core/Conditional%20statements.md) | Routing logic via timeline-safe branching constructs (`If`, `Elif`, `Else`). |
| **5** | **Board & Spawning** | [`Board.md`](Documentation%20[WIP]/Core/Board.md) & [`Spawning.md`](Documentation%20[WIP]/Core/Spawning.md) | Modifying resources, lane conditions, and generating custom wave queues. |

---