# ⚡ Event Triggers

Triggers are context managers that listen to game lifecycle events, user inputs, combat reactions, and entity milestones to execute visual script streams.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import KeyCode
```

---

## 1. Lifecycle Triggers

### `OnBoardStart`
Fires on the very first frame of level initialization, before card selection or introductory cinematics:
```python
with pft.Trigger.OnBoardStart():
    pft.Board.Sun = 500
```

### `OnGameStart`
Fires immediately after the intro sequence ("Ready, Set, Plant!") completes and active gameplay begins:
```python
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text("Game Started!", duration=3.0)
```

### `OnWave`
Fires on every wave arrival. Yields the current wave number integer output port:
```python
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 10):
        pft.InGameUI.display_text("Wave 10 Boss Wave!")
```

### `OnWaveCleared`
Fires when all zombies belonging to the current wave have been defeated:
```python
with pft.Trigger.OnWaveCleared() as wave_num:
    pft.Board.Sun += 100
```

### `OnWaveEvent`
Fires when an internal wave milestone event is broadcast by the engine:
```python
with pft.Trigger.OnWaveEvent() as wave_num:
    pft.InGameUI.display_text("Wave Milestone Reached!")
```

### `OnStageEnter`
Fires when the level transitions to a specified stage name (default `"战斗"`):
```python
with pft.Trigger.OnStageEnter(stage_name="二阶段"):
    pft.InGameUI.display_text("Entering Boss Phase 2!")
```

---

## 2. Input Triggers

### `OnMouseClick`
Fires when the user clicks the mouse on the lawn. Yields a `Mouse` helper instance exposing cursor position and click state:
```python
with pft.Trigger.OnMouseClick() as mouse:
    # mouse.row, mouse.col, mouse.is_left_click, mouse.item
    with pft.If(mouse.is_left_click):
        pft.Lawnf.spawn_particle(row=mouse.row, col=mouse.col)
```

### `OnKeyDown`
Fires when a specific keyboard key is pressed. Accepts a `KeyCode` enum member:
```python
with pft.Trigger.OnKeyDown(KeyCode.Space):
    pft.Board.Sun += 50
```

---

## 3. Plant Triggers

### `OnPlantCreate`
Fires whenever a plant is planted or spawned onto the lawn. Yields the created `Plant` entity:
```python
with pft.Trigger.OnPlantCreate() as plant:
    plant.add_shield(200)
```

### `OnPlantClick` (alias `OnPlantClicked`)
Fires when the player clicks on a plant on the lawn. Yields the clicked `Plant`:
```python
with pft.Trigger.OnPlantClick() as plant:
    plant.heal(500)
```

### `OnPlantDie` (alias `OnPlantDeath`)
Fires right before a plant is destroyed:
```python
with pft.Trigger.OnPlantDie() as plant:
    pft.InGameUI.display_text("A plant has fallen!")
```

### `OnPlantDeathComplete`
Fires after a plant's removal/fade animation has fully completed:
```python
with pft.Trigger.OnPlantDeathComplete() as plant:
    pft.Board.Sun += 25
```

### `OnPlantMixed`
Fires when two plants are fused/mixed into a new fusion hybrid on the lawn. Yields the resulting hybrid `Plant`:
```python
with pft.Trigger.OnPlantMixed() as hybrid_plant:
    pft.InGameUI.display_text("Hybrid plant created!")
    hybrid_plant.modify_health(1.5)
```

### `OnWorldPlantEffect`
Fires when a global plant effect activates. Yields the affected row integer output port:
```python
with pft.Trigger.OnWorldPlantEffect() as affected_row:
    pft.Lawnf.trigger_jalapeno(row=affected_row, damage=1000)
```

---

## 4. Zombie Triggers

### `OnZombieSpawn`
Fires whenever a zombie enters the lawn. Yields the spawned `Zombie` entity:
```python
with pft.Trigger.OnZombieSpawn() as zombie:
    zombie.set_speed_multiplier(1.1)
```

### `OnZombieDie` (alias `OnZombieDeath`)
Fires when a zombie runs out of health and dies. Yields the defeated `Zombie`:
```python
with pft.Trigger.OnZombieDie() as zombie:
    pft.Board.Money += 10
```

### `OnZombieClick`
Fires when the player clicks on a zombie. Yields the clicked `Zombie`:
```python
with pft.Trigger.OnZombieClick() as zombie:
    zombie.damage(100)
```

### `OnZombieHealthBelow`
Fires when a zombie's health drops below its critical threshold. Yields the `Zombie`:
```python
with pft.Trigger.OnZombieHealthBelow() as zombie:
    zombie.set_speed_multiplier(1.5)  # Enrage mechanic
```

---

## Quick Reference

| Trigger | Yields | Description |
| :--- | :--- | :--- |
| `OnBoardStart` | `None` | Fires on first level initialization frame |
| `OnGameStart` | `None` | Fires after "Ready, Set, Plant!" sequence |
| `OnWave` | `int` (wave index) | Fires on each wave spawn |
| `OnWaveCleared` | `int` (wave index) | Fires when active wave is wiped |
| `OnWaveEvent` | `int` (wave index) | Fires on wave milestone events |
| `OnStageEnter` | `None` | Fires when entering a named stage |
| `OnMouseClick` | `Mouse` | Fires on mouse clicks |
| `OnKeyDown` | `None` | Fires when specified `KeyCode` is pressed |
| `OnPlantCreate` | `Plant` | Fires when a plant is planted/spawned |
| `OnPlantClick` | `Plant` | Fires when a player clicks a plant |
| `OnPlantDie` | `Plant` | Fires before non-instant plant death |
| `OnPlantDeathComplete` | `Plant` | Fires after plant death animation |
| `OnPlantMixed` | `Plant` | Fires when plants are fused/mixed |
| `OnWorldPlantEffect` | `int` (row) | Fires on global world plant effects |
| `OnZombieSpawn` | `Zombie` | Fires when a zombie spawns |
| `OnZombieDie` | `Zombie` | Fires when a zombie dies |
| `OnZombieClick` | `Zombie` | Fires when player clicks a zombie |
| `OnZombieHealthBelow` | `Zombie` | Fires when zombie health is critical |
