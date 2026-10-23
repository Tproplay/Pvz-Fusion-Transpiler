# WIP Roadmap & Node Implementation Status

This document tracks the implementation coverage of native Unity visual nodes in the **PvZ Fusion Transpiler**, mapping high-level extension interfaces to native IL2CPP engine nodes, and documenting intentionally omitted, deferred, or compiler-internal nodes.

---

## 1. Extension Coverage Overview

| Category | Native Nodes Represented | Extension API | Status |
| :--- | :--- | :--- | :--- |
| **Spawning** | `SetPlantNode`, `CreateZombieNode`, `ShootEventBulletNode` | `Spawner.Set_Plant`, `Spawner.Set_Zombie`, `Spawner.Set_Bullet` | ✅ Fully Implemented |
| **Plant Manipulation** | `CursePlantNode`, `SilencePlantNode`, `FeedGoldenBeanNode`, `UpgradePlantNode`, `TrySuperSkillNode`, etc. | `Plant` wrapper | ✅ Fully Implemented |
| **Zombie Manipulation** | `DamageZombieNode`, `SetZombieSpeedMultiplierNode`, `HypnotizeZombieNode`, `PlayZombieAnimationNode`, etc. | `Zombie` wrapper | ✅ Fully Implemented |
| **Bullet Manipulation** | `DestroyBulletNode`, `RedirectBulletNode`, `ScaleBulletDamageNode` | `Bullet` wrapper | ✅ Fully Implemented |
| **Game State & Stages** | `ChangeStageNode`, `GetStageNode`, `GameOverNode`, `GameWinNode`, `PauseWaveCountdownNode` | `Game`, `Board`, `Game.Stage` | ✅ Fully Implemented |
| **Player Tools** | `GetHeldToolNode`, `CompareToolTypeNode`, `GetToolCooldownNode`, `SetToolCooldownNode` | `Tool`, `ToolCooldown`, `ToolType` | ✅ Fully Implemented |
| **Game Objects & World**| `CreateEventObjectNode`, `DestroyEventObjectNode`, `GetObjectTransformNode`, `BindPlantNode`, `BindZombieNode`, `ObjectToPlantNode`, `ObjectToZombieNode` | `WorldObject`, `GameObject`, `Vector3` | ✅ Fully Implemented |
| **Triggers** | `OnGameStartNode`, `OnBoardStartNode`, `OnWaveNode`, `OnPlantCreateNode`, `OnPlantDieNode`, `OnStageEnterNode`, `OnPlantMixedNode`, `OnZombieClickNode`, etc. | `Trigger` namespace | ✅ Fully Implemented |
| **Branching & Loops** | `BranchNode`, `MultiBranchNode`, `LoopNode`, `WhileNode` | `If`, `Switch`, `For`, `While` | ✅ Fully Implemented |
| **Variables & Types** | `IntVariableNode`, `FloatVariableNode`, `BoolVariableNode`, `StringVariableNode`, conversion nodes | `IntVar`, `FloatVar`, `BoolVar`, `StringVar`, `Int`, `Float`, `String`, `Bool` | ✅ Fully Implemented |
| **Math & Logic** | `PowerNode`, `LogarithmNode`, `CompareFloatNode`, `CompareIntNode`, `CompareGameObjectNode` | `Math`, `Compare` | ✅ Fully Implemented |

---

## 2. Intentionally Omitted & Optimization-Only Nodes

As documented in [`_Nodes/NOT_IMPLEMENTED.txt`](../PvZ_Fusion_Transpiler_src/src/PvZ_Fusion_Transpiler/_Nodes/NOT_IMPLEMENTED.txt):

### Duplicate UI Menus
- `TypedChoiceMenuNode`, `TypedChoiceMergeNode`, `TypedChoiceOptionNode`
  - *Reason*: Redundant duplicate of `MultipleChoiceMenu` (`MultiSelectMenu`).

### Optimizer-Internal Nodes
- `PulseNode`, `DoOnceNode`, `RepeatUntilNode`
  - *Reason*: Not useful as standalone user-facing extension nodes; reserved for internal graph compiler optimizer to reduce generated node count.
- `WaitUntilNode`
  - *Reason*: Deemed redundant / useless as an extension node in PvZ Fusion visual script logic.

### Deprecated Engine Nodes
- `GetTravelEntryNode`
  - *Reason*: Deprecated in the original PvZ Fusion game engine.

---

## 3. Deferred Nodes (Pending Specifications)

- **List Variables (33 nodes)**:
  - `Append*ListNode`, `ClearListValuesNode`, `CopyListValuesNode`, `Find*ListValueNode`, `Get*ListItemNode`, `Insert*ListNode`, `Replace*ListNode`.
  - *Reason*: Waiting for detailed user requirements on how collections/list variables should be structured and accessed.
