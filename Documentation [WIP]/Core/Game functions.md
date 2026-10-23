# 🛠️ Game Functions (`InGameUI` & `Lawnf`)

`pvn.InGameUI` covers on-screen UI: info cards, seed packet cards, and text popups.
`pvn.Lawnf` covers lawn props, area-of-effect abilities, sound, game state, and plant/zombie queries.

```python
import PvzRH_node as pvn
from PvzRH_node import PlantType, ZombieType
from PvzRH_node.Types import SoundType, TravelBuffType
```

---

## 1. Info Cards

There are two equivalent ways to show an info card popup — both drive the same underlying node, so pick whichever style reads better for your logic.

### Callback Style (`display_info_card`)

```python
pvn.InGameUI.display_info_card(
    "New Wave!",
    "A horde approaches",
    on_clicked=lambda: pvn.Print("Card dismissed"),
)
```

You can also attach the click handler after the fact with `.on_click(...)`, or reach the execution path directly via `.Output.OnCardClicked`.

### Context Manager Style (`InGameUI.InfoCard`)

```python
with pvn.InGameUI.InfoCard("New Wave!", "A horde approaches"):
    pvn.Print("Card dismissed")
```

### Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `big_title` | `Any` | *Required* | Main header text, or a text/variable port. |
| `small_title` | `Any` | `""` for the `with` form; *Required* for `display_info_card` | Secondary/subtitle text. |
| `on_clicked` | `Callable` | `None` | *(`display_info_card` only)* Logic run when the card is clicked. |

---

## 2. Plant Cards

Manage the seed packet cards available to the player during a level.

```python
# Grants a new card, overriding cost/cooldown
pvn.InGameUI.give_plant_card(PlantType.SunFlower, cooldown=5.0, cost=50, use_default=False)

# Removes a card entirely
pvn.InGameUI.remove_plant_card(PlantType.SunFlower)

# Spawns a pickup-able card drop on the lawn (e.g. from a defeated zombie)
pvn.InGameUI.spawn_dropped_card(row=2, col=5, plant_type=PlantType.WallNut)
```

| Function | Parameters | Description |
| --- | --- | --- |
| `give_plant_card` | `plant_type, cooldown=7.5, cost=100, use_default=True` | Adds a seed packet card to the player's selection. |
| `remove_plant_card` | `plant_type` | Removes a plant's card from the player's selection. |
| `spawn_dropped_card` | `row, col, plant_type` | Spawns a pickup-able card at a board location. |

> **Note:** `use_default=True` uses the plant's official base stats for display instead of `cooldown`/`cost`.

---

## 3. Text (`Print`)

`pvn.Print` (an alias for `InGameUI.display_text`) formats and displays a mix of text, variables, and node ports on screen.

```python
with pvn.Trigger.OnWave() as wave_num:
    pvn.Print("Wave ", wave_num, " incoming!")
```

If any argument is a boolean expression (`BoolVar`, or a comparison/logic node port), the message is automatically compiled into two branches — the correct wording is shown depending on the runtime value, without you writing an `If` yourself:

```python
hard_mode = pvn.BoolVar(start_val=False, name="HardMode")
pvn.Print("Hard mode: ", hard_mode)   # Displays "Hard mode: True" or "Hard mode: False"
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*args` | `Any` | *Required* | Strings, numbers, variables, or node ports — concatenated in order. |
| `duration` | `float` | `3.0` | Seconds the text stays on screen. |

---

## 4. Lawn Props

Cosmetic props placed directly onto lawn tiles.

```python
pvn.Lawnf.spawn_grave(row=1, col=4)
pvn.Lawnf.spawn_crater(row=2, col=6)
pvn.Lawnf.spawn_ladder(row=3, col=0)
pvn.Lawnf.spawn_particle(row=0, col=8)
pvn.Lawnf.spawn_ice_block(row=2, col=3, plant_type=PlantType.Peashooter)
```

| Function | Parameters | Description |
| --- | --- | --- |
| `spawn_particle` | `row, col` | Decorative particle effect at a tile. |
| `spawn_grave` | `row, col` | Gravestone prop. |
| `spawn_crater` | `row, col` | Crater prop (e.g. explosion aftermath). |
| `spawn_ladder` | `row, col` | Pool ladder, letting zombies climb out of the pool at that tile. |
| `spawn_ice_block` | `row, col, plant_type=-1` | Ice block prop, optionally encasing a plant model (`-1` = bare ice block). |

---

## 5. Explosions & Area Effects

```python
pvn.Lawnf.trigger_cherry_explosion(row=2, col=4, damage=1800)
pvn.Lawnf.trigger_doom_explosion(row=2, col=4, damage=1800, create_pit=True)
pvn.Lawnf.trigger_zombie_explosion(row=2, col=4)
pvn.Lawnf.trigger_jalapeno(row=3, damage=1800)
pvn.Lawnf.trigger_ice_shroom(duration=5.0)
```

| Function | Parameters | Description |
| --- | --- | --- |
| `trigger_cherry_explosion` | `row, col, damage=1800` | Cherry Bomb-style explosion at a tile. |
| `trigger_doom_explosion` | `row, col, damage=1800, create_pit=True` | Doom-shroom-style explosion, optionally leaving a pit. |
| `trigger_zombie_explosion` | `row, col` | Zombie-explosion visual (no damage). |
| `trigger_jalapeno` | `row, damage=1800` | Jalapeno-style row-wide fire effect. |
| `trigger_ice_shroom` | `duration` | Freezes all zombies on the board for `duration` seconds. |

---

## 6. Sound

```python
pvn.Lawnf.play_sound(SoundType.Buzzer)
```

Accepts a `SoundType` enum member (from `PvzRH_node.Types`) or a raw integer ID.

---

## 7. Game State

```python
with pvn.If(pvn.Board.Sun < 0):
    pvn.Lawnf.trigger_game_over(reason="Ran out of Sun!")

with pvn.If(pvn.Board.Wave >= final_wave):
    pvn.Lawnf.trigger_game_win()
```

| Function | Parameters | Description |
| --- | --- | --- |
| `trigger_game_over` | `reason="Defeated!"` | Ends the level in defeat, displaying `reason`. |
| `trigger_game_win` | — | Ends the level in victory. |

---

## 8. Buffs

```python
pvn.Lawnf.get_buff(TravelBuffType.SomeBuff)
```

Grants a travel buff for the current level. Accepts a `TravelBuffType` enum member (from `PvzRH_node.Types`) or a raw integer ID.

---

## 9. Plant & Zombie Queries

```python
zombie = pvn.Lawnf.get_closest_zombie(row=2, col=8)
zombie.damage(500)

with pvn.Lawnf.for_each_plant_on_lawn() as plant:
    plant.heal(50)
```

| Function | Parameters | Returns | Description |
| --- | --- | --- | --- |
| `get_closest_zombie` | `row, col` | `Zombie` | Nearest zombie to the given tile. |
| `get_plants_at` | `row, col` | list port | Plants in a specific cell — feed into a list-consuming node/loop. |
| `get_all_plants` | — | list port | All plants on the board — feed into a list-consuming node/loop. |
| `for_each_plant_on_lawn` | — (context manager) | `Plant` per iteration | Loops over every plant on the board. |

---

## Quick Reference

| Class | Category | Members |
| --- | --- | --- |
| `InGameUI` | Info cards | `display_info_card`, `InfoCard` |
| `InGameUI` | Plant cards | `give_plant_card`, `remove_plant_card`, `spawn_dropped_card` |
| `InGameUI` | Text | `display_text` (aka `pvn.Print`) |
| `Lawnf` | Props | `spawn_particle`, `spawn_grave`, `spawn_crater`, `spawn_ladder`, `spawn_ice_block` |
| `Lawnf` | Effects | `trigger_cherry_explosion`, `trigger_doom_explosion`, `trigger_zombie_explosion`, `trigger_jalapeno`, `trigger_ice_shroom` |
| `Lawnf` | Sound | `play_sound` |
| `Lawnf` | Game state | `trigger_game_over`, `trigger_game_win` |
| `Lawnf` | Buffs | `get_buff` |
| `Lawnf` | Queries & loops | `get_closest_zombie`, `get_plants_at`, `get_all_plants`, `for_each_plant_on_lawn` |
