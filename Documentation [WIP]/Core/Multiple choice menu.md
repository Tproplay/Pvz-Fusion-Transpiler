# 📋 Multiple Choice UI Menus

The Multiple Choice system lets you design in-game perk cards, rogue-lite selection pop-ups, and interactive dialogs.

```python
import PvzRH_node as pvn
from PvzRH_node import MultiSelectMenu, Option, PlantType, ZombieType
```

---

## 1. Quick Start: Using Decorators

The easiest way to define selection choices is using the `@menu.option` decorator syntax:

```python
menu = MultiSelectMenu(
    is_rerollable=True,
    reroll_count=3,
    is_skippable=False,
    window_count=3,
)

@menu.option(title="Solar Surplus", description="Gain +150 Sun instantly", plant_type=PlantType.SunFlower)
def choose_sun():
    pvn.Board.Sun += 150

@menu.option(title="Reinforce Line", description="Spawn a Wall-Nut at row 3, col 4", plant_type=PlantType.WallNut)
def choose_defense():
    pvn.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut)

@menu.option(title="Tactical Bomb", description="Trigger Cherry Bomb explosion", plant_type=PlantType.CherryBomb)
def choose_bomb():
    pvn.Spawner.Set_Plant(row=2, col=9, plant_type=PlantType.CherryBomb)

# Open the menu during a wave
with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(wave_num == 5):
        menu.show()
```

> **Note:** A menu can carry a `plant_type` *or* a `zombie_type` icon, never both — if both are set, the plant icon takes priority and the zombie type is dropped with a warning.

---

## 2. Reusable Option Cards

For complex rogue-lite setups, you can define standalone `Option` instances once and share them across multiple different menus:

```python
# Standalone Option definition
speed_boost = Option(
    title="Nitro Turf",
    description="Boost plant attack speed by 25%",
    callback=lambda: pvn.Print("Speed boost active!"),
    plant_type=PlantType.DoubleShooter,
)

# Attach the pre-instantiated option to multiple menus
menu_a = MultiSelectMenu()
menu_a.add_option(speed_boost)

menu_b = MultiSelectMenu()
menu_b.add_option(speed_boost)
```

`add_option` also accepts the same inline arguments as `Option(...)` directly, so `menu.add_option(title=..., description=..., callback=..., plant_type=...)` works without constructing an `Option` first.

---

## 3. Menu Exit & Refresh Events

You can hook additional logic to fire when a player closes or rerolls a menu using `.Output`. These must be accessed **after** `menu.show()` has run, since the underlying node isn't created until then:

```python
menu = MultiSelectMenu(is_rerollable=True, reroll_count=2)

with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(wave_num == 5):
        menu.show()

# Trigger logic when the window finishes closing
with menu.Output.OnExit:
    pvn.Print("Menu closed, resuming gameplay.")

# Trigger logic every time the user clicks reroll
with menu.Output.OnRefresh:
    pvn.Print("Player used a reroll.")
```

---

## Configuration Reference

### MultiSelectMenu Settings

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `is_rerollable` | `bool` | `True` | Enables the reroll/refresh button on the window |
| `reroll_count` | `int` | `3` | Number of times the player is allowed to reroll |
| `is_skippable` | `bool` | `False` | Allows the player to close the window without selecting |
| `window_count` | `int` | `3` | Total number of card options presented simultaneously |

### Option Settings

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | *Required* | Card header title |
| `description` | `str` | *Required* | Card description or perk detail |
| `callback` | `Callable` | `None` | Logic executed when the player clicks this card |
| `plant_type` | `PlantType` | `254` (None) | Plant icon shown on the card |
| `zombie_type` | `ZombieType` | `-1` (None) | Zombie icon shown on the card |
