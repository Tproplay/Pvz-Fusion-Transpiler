# 🌱 Spawning Plants & Zombies

The `pvn.Spawner` interface places plants and zombies onto the board at runtime, returning the spawned entity directly (with extra attributes attached for handling the spawn outcome).

```python
import PvzRH_node as pvn
from PvzRH_node import PlantType, ZombieType
```

---

## 1. Spawning Plants (`Spawner.Set_Plant`)

Spawns a plant at the specified grid coordinates and returns a `Plant` object.

```python
plant = pvn.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut)
```

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `row` | `int` | *Required* | Target row on the lawn grid. |
| `col` | `int` | *Required* | Target column on the lawn grid. |
| `plant_type` | `PlantType \| int` | *Required* | Plant to spawn. Accepts a `PlantType` enum member or a raw integer ID. |
| `force` | `bool` | `False` | If `True`, forces placement even if a plant already occupies the cell (e.g. replacing existing plants). |

### Using the Spawned Plant

Since `Set_Plant` returns a `Plant` directly, you can act on it immediately with any `Plant` method:

```python
plant = pvn.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut)
plant.modify_health(2.0)   # Double the Wall-Nut's health right after creation
```

### Success & Failure Paths

The returned `Plant` also carries two execution-path context managers for handling the outcome of the spawn attempt:

```python
with pvn.Trigger.OnKeyDown(KeyCode.Space):
    plant = pvn.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut, force=True)

    with plant.on_created:
        pvn.Print("Wall-Nut planted!")

    with plant.on_failed:
        pvn.Print("Could not plant here!")
```

* **`on_created`** — Fires if the plant was successfully placed.
* **`on_failed`** — Fires if placement failed (e.g. the cell is blocked and `force=False`).

---

## 2. Spawning Zombies (`Spawner.Set_Zombie`)

Spawns a zombie at the specified grid coordinates and returns a `Zombie` object.

```python
zombie = pvn.Spawner.Set_Zombie(row=4, col=8, zombie_type=ZombieType.Gargantuar)
```

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `row` | `int` | *Required* | Target row on the lawn grid. |
| `col` | `int` | *Required* | Target column on the lawn grid. |
| `zombie_type` | `ZombieType \| int` | *Required* | Zombie to spawn. Accepts a `ZombieType` enum member or a raw integer ID. |
| `mind_controlled` | `bool` | `False` | If `True`, spawns the zombie as mind-controlled (fights for the player's side). |

### Using the Spawned Zombie

```python
zombie = pvn.Spawner.Set_Zombie(row=4, col=8, zombie_type=ZombieType.Gargantuar)
zombie.set_health_multiplier(1.5)   # Buff the Gargantuar's health right after spawning
```

### Success Path

```python
with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(wave_num == 10):
        zombie = pvn.Spawner.Set_Zombie(row=2, col=9, zombie_type=ZombieType.Gargantuar)

        with zombie.on_created:
            pvn.Print("Gargantuar has arrived!")
```

* **`on_created`** — Fires if the zombie was successfully spawned.

> **Note:** Unlike `Set_Plant`, `Set_Zombie` does not currently expose an `on_failed` path.

---

## Quick Reference

| Method | Signature | Returns | Extra Attributes |
| --- | --- | --- | --- |
| `Spawner.Set_Plant` | `(row, col, plant_type, force=False)` | `Plant` | `.on_created`, `.on_failed` |
| `Spawner.Set_Zombie` | `(row, col, zombie_type, mind_controlled=False)` | `Zombie` | `.on_created` |