# 🌱 Spawning Plants, Zombies & Bullets

The `pft.Spawner` interface places plants, zombies, and bullets onto the board at runtime, returning wrapped entity objects directly with lifecycle execution paths.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType, BulletType, KeyCode
```

> [!IMPORTANT]
> **Strict Enum Requirement**: Raw integer IDs are strictly forbidden for `plant_type`, `zombie_type`, and `bullet_type`. Passing integers raises a `TypeError`. Always use the corresponding `PlantType`, `ZombieType`, or `BulletType` enum member.

---

## 1. Spawning Plants (`Spawner.Set_Plant`)

Spawns a plant at the specified lawn grid coordinates and returns a `SpawnedPlant` object (which inherits all methods of `Plant`).

```python
plant = pft.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut)
```

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `row` | `int \| Any` | *Required* | Target row on the lawn grid (0-indexed). |
| `col` / `column` | `int \| float \| Any` | *Required* | Target column on the lawn grid. |
| `plant_type` | `PlantType` | *Required* | Plant to spawn. **Must be a `PlantType` enum member.** |
| `force` | `bool` | `False` | If `True`, forces placement even if the cell is occupied. |

### Context Manager Syntax

You can use `Spawner.Set_Plant` directly as a context manager:

```python
with pft.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut) as plant:
    pft.InGameUI.display_text("Wall-Nut successfully planted!")
    plant.add_shield(500)
```

### Success & Failure Execution Paths

The returned `SpawnedPlant` instance provides dedicated execution paths to branch on spawn success or failure:

```python
with pft.Trigger.OnKeyDown(KeyCode.Space):
    plant = pft.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut, force=False)

    with plant.on_created:  # alias: plant.on_success
        pft.InGameUI.display_text("Wall-Nut planted!")
        plant.modify_health(2.0)

    with plant.on_failed:
        pft.InGameUI.display_text("Could not plant here (cell occupied)!")
```

---

## 2. Spawning Zombies (`Spawner.Set_Zombie`)

Spawns a zombie at the specified grid coordinates and returns a `SpawnedZombie` object (inheriting all methods of `Zombie`).

```python
zombie = pft.Spawner.Set_Zombie(row=4, col=8, zombie_type=ZombieType.Gargantuar)
```

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `row` | `int \| Any` | *Required* | Target row on the lawn grid (0-indexed). |
| `col` / `column` | `int \| float \| Any` | *Required* | Target column on the lawn grid. |
| `zombie_type` | `ZombieType` | *Required* | Zombie to spawn. **Must be a `ZombieType` enum member.** |
| `mind_controlled` | `bool` | `False` | If `True`, spawns the zombie fighting for the player's side. |

### Context Manager & Success Path

```python
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 10):
        with pft.Spawner.Set_Zombie(row=2, col=9, zombie_type=ZombieType.Gargantuar) as zombie:
            pft.InGameUI.display_text("Gargantuar has arrived!")
            zombie.set_speed_multiplier(1.2)
            zombie.set_health_multiplier(1.5)
```

Alternatively, attach to `.on_created`:
```python
zombie = pft.Spawner.Set_Zombie(row=2, col=9, zombie_type=ZombieType.Gargantuar)
with zombie.on_created:
    pft.InGameUI.display_text("Spawned via on_created path!")
```

---

## 3. Spawning Bullets (`Spawner.Set_Bullet`)

Shoots an event bullet with custom physics, damage, direction, or tracking. Returns a `SpawnedBullet` object (inheriting from `Bullet`).

```python
bullet = pft.Spawner.Set_Bullet(
    row=2,
    col=3.0,
    bullet_type=BulletType.Pea,
    damage=40.0,
    speed=300.0,
    angle=0.0,
)
```

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `row` | `int \| Any` | `0` | Origin row coordinate. |
| `col` / `column` | `float \| Any` | `0.0` | Origin column coordinate. |
| `bullet_type` | `BulletType` | *Required* | Type of projectile. **Must be a `BulletType` enum member.** |
| `damage` | `float \| Any` | `None` | Custom damage value override. |
| `speed` | `float \| Any` | `None` | Custom projectile speed override. |
| `angle` | `float \| Any` | `None` | Flight trajectory angle in degrees. |
| `scale_multiplier`| `float \| Any` | `None` | Size scale multiplier. |
| `at_mouse` | `bool \| Any` | `False` | If `True`, fires toward current mouse position. |
| `zombie_camp` | `bool \| Any` | `False` | If `True`, bullet is owned by zombie faction (damages plants). |

### Context Manager & Lifecycle Paths

```python
with pft.Trigger.OnMouseClick() as mouse:
    with pft.Spawner.Set_Bullet(
        row=mouse.row,
        col=mouse.col,
        bullet_type=BulletType.FirePea,
        damage=80.0,
        at_mouse=True,
    ) as bullet:
        pft.InGameUI.display_text("Bullet shot towards mouse!")
```

Supports `.on_created` and `.on_failed` execution branches:
```python
with bullet.on_created:
    pft.InGameUI.display_text("Bullet launched!")

with bullet.on_failed:
    pft.InGameUI.display_text("Bullet creation failed!")
```

---

## Quick Reference

| Method | Returns | Context Manager | Lifecycle Paths | Strict Enum |
| --- | --- | --- | --- | --- |
| `Spawner.Set_Plant` | `SpawnedPlant` | `with Spawner.Set_Plant(...) as plant:` | `.on_created`, `.on_failed` | `PlantType` |
| `Spawner.Set_Zombie` | `SpawnedZombie` | `with Spawner.Set_Zombie(...) as zombie:` | `.on_created` | `ZombieType` |
| `Spawner.Set_Bullet` | `SpawnedBullet` | `with Spawner.Set_Bullet(...) as bullet:` | `.on_created`, `.on_failed` | `BulletType` |
