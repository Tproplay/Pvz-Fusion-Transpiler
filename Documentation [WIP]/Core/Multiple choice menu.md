# 📋 Multiple Choice UI Menus

The Multiple Choice system lets you design in-game perk cards, rogue-lite selection pop-ups, and interactive upgrade dialogs.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import MultiSelectMenu, Option
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType
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
    pft.Board.Sun += 150

@menu.option(title="Reinforce Line", description="Spawn a Wall-Nut at row 3, col 4", plant_type=PlantType.WallNut)
def choose_defense():
    pft.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.WallNut)

@menu.option(title="Tactical Bomb", description="Trigger Cherry Bomb explosion", plant_type=PlantType.CherryBomb)
def choose_bomb():
    pft.Lawnf.trigger_cherry_explosion(row=2, col=4, damage=1800)

# Open the menu during a wave
with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 5):
        menu.show()
```

> **Note:** A choice card can carry a `plant_type` *or* a `zombie_type` icon, never both — if both are set, the plant icon takes priority.

---

## 2. Reusable Option Cards

For complex rogue-lite setups, define standalone `Option` instances once and share them across multiple different menus:

```python
speed_boost = Option(
    title="Nitro Turf",
    description="Boost plant attack speed by 25%",
    callback=lambda: pft.InGameUI.display_text("Speed boost active!"),
    plant_type=PlantType.Repeater,
)

menu_a = MultiSelectMenu()
menu_a.add_option(speed_boost)

menu_b = MultiSelectMenu()
menu_b.add_option(speed_boost)
```

---

## 3. Menu Exit & Refresh Events

Hook additional logic to fire when a player closes or rerolls a menu using `.Output`. These must be accessed **after** `menu.show()` has run:

```python
menu = MultiSelectMenu(is_rerollable=True, reroll_count=2)

with pft.Trigger.OnWave() as wave_num:
    with pft.If(wave_num == 5):
        menu.show()

# Fires when the window finishes closing
with menu.Output.OnExit:
    pft.InGameUI.display_text("Menu closed, resuming gameplay.")

# Fires every time the user clicks reroll
with menu.Output.OnRefresh:
    pft.InGameUI.display_text("Player used a reroll.")
```

---

## Quick Reference

| Class | Parameter | Default | Description |
| :--- | :--- | :--- | :--- |
| `MultiSelectMenu` | `is_rerollable` | `True` | Enables the reroll/refresh button |
| `MultiSelectMenu` | `reroll_count` | `3` | Maximum number of allowed rerolls |
| `MultiSelectMenu` | `is_skippable` | `False` | Allows closing the window without selecting |
| `MultiSelectMenu` | `window_count` | `3` | Number of cards shown simultaneously |
| `Option` | `title` | *Required* | Card header text |
| `Option` | `description` | *Required* | Card perk description |
| `Option` | `callback` | `None` | Execution logic when card is clicked |
| `Option` | `plant_type` | `254` (None) | Plant icon displayed on card |
| `Option` | `zombie_type` | `-1` (None) | Zombie icon displayed on card |
