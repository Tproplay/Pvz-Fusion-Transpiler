# ⚡ Event Triggers

Triggers are context managers that listen to in-game lifecycle events, input actions, and entity state changes to execute custom node graphs.


## Lifecycle Triggers

### `OnBoardStart`

Fires on the very first frame of level initialization, before card selection and intro cinematics.

```python
with pvn.Trigger.OnBoardStart():
    ...
```

### `OnGameStart`

Fires immediately after the intro countdown ("Ready, Set, Plant!") ends and active gameplay starts.

```python
with pvn.Trigger.OnGameStart():
    ...
```

### `OnWave`

Fires on every wave arrival. Yields the current wave number index as a reference value.

```python
with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(wave_num == 10):
        ...
```

---

## Input Triggers

### `OnMouseClick`

Fires when the mouse button is pressed. Yields a `Mouse` helper object providing cursor coordinates and grid positions.

```python
with pvn.Trigger.OnMouseClick() as mouse:
    ...
```

### `OnKeyDown`

Fires when the specified key is pressed down.

```python
with pvn.Trigger.OnKeyDown(KeyCode.Space):
    ...
```

---

## Plant Triggers

### `OnPlantCreate`

Fires whenever a plant is planted or spawned onto the lawn. Yields the created `Plant` entity.

```python
with pvn.Trigger.OnPlantCreate() as plant:
    ...
```

### `OnPlantClicked`

Fires when a plant on the lawn is clicked by the player. Yields the clicked `Plant` entity.

```python
with pvn.Trigger.OnPlantClicked() as plant:
    ...
```

### `OnPlantDeath`

Fires right before a plant is destroyed.

> **Note:** Does not fire for instant single-use plants like Cherry Bomb or Doom-shroom.

```python
with pvn.Trigger.OnPlantDeath() as plant:
    ...
```

### `OnPlantDeathComplete`

Fires after a plant's removal/fade animation has fully completed.

```python
with pvn.Trigger.OnPlantDeathComplete() as plant:
    ...
```

---

## Zombie Triggers

### `OnZombieSpawn`

Fires whenever a zombie enters the board. Yields the spawned `Zombie` entity.

```python
with pvn.Trigger.OnZombieSpawn() as zombie:
    ...
```

### `OnZombieDeath`

Fires when a zombie runs out of health and dies. Yields the defeated `Zombie` entity.

```python
with pvn.Trigger.OnZombieDeath() as zombie:
    ...
```

---

## Quick Reference

| Trigger Class | Returns / Yields | Description |
| --- | --- | --- |
| `OnBoardStart` | `None` | Fires on first level initialization frame |
| `OnGameStart` | `None` | Fires after the "Ready, Set, Plant!" sequence |
| `OnWave` | `int` (wave index) | Fires on each wave spawn |
| `OnMouseClick` | `Mouse` | Fires on mouse clicks |
| `OnKeyDown` | `None` | Fires on keyboard key press |
| `OnPlantCreate` | `Plant` | Fires when a plant is placed or created |
| `OnPlantClicked` | `Plant` | Fires when a plant is clicked |
| `OnPlantDeath` | `Plant` | Fires before non-instant plant death |
| `OnPlantDeathComplete` | `Plant` | Fires after plant death animation ends |
| `OnZombieSpawn` | `Zombie` | Fires when a zombie spawns |
| `OnZombieDeath` | `Zombie` | Fires when a zombie dies |
