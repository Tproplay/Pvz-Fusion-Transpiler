# 🛠️ Game Functions, Tools & World Objects

This document covers high-level engine services provided by `InGameUI`, `Lawnf`, `Tool`, and `WorldObject`.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType, ToolType, SoundType, TravelBuffType
```

---

## 1. On-Screen UI (`InGameUI`)

### Info Cards

Display modal info cards with titles and click callbacks:

```python
# Callback syntax
pft.InGameUI.display_info_card(
    "Warning!",
    "Massive Zombie Horde Incoming",
    on_clicked=lambda: pft.InGameUI.display_text("Acknowledged"),
)

# Context manager syntax
with pft.InGameUI.InfoCard("Perk Unlocked", "Double Sun Production"):
    pft.InGameUI.display_text("Card Dismissed")
```

### Plant Seed Packets

Control player seed packets during runtime:

```python
# Give a card with custom cooldown/cost
pft.InGameUI.give_plant_card(PlantType.SunFlower, cooldown=5.0, cost=50, use_default=False)

# Remove a plant card from the deck
pft.InGameUI.remove_plant_card(PlantType.SunFlower)

# Spawn a dropped seed packet card pickup on the lawn
pft.InGameUI.spawn_dropped_card(row=2, col=5, plant_type=PlantType.WallNut)
```

### Text Displays (`display_text` / `Print`)

Display text notifications, variable values, or port strings on screen:

```python
with pft.Trigger.OnWave() as wave_num:
    pft.InGameUI.display_text("Wave ", wave_num, " incoming!", duration=4.0)
```

---

## 2. Lawn Props, Spells & Audio (`Lawnf`)

### Lawn Props

Spawn decorative and interactive board props:

```python
pft.Lawnf.spawn_grave(row=1, col=4)
pft.Lawnf.spawn_crater(row=2, col=6)
pft.Lawnf.spawn_ladder(row=3, col=0)
pft.Lawnf.spawn_particle(row=0, col=8)
pft.Lawnf.spawn_ice_block(row=2, col=3, plant_type=PlantType.Peashooter)
```

### Explosions & Area Spells

Trigger instant board effects:

```python
pft.Lawnf.trigger_cherry_explosion(row=2, col=4, damage=1800)
pft.Lawnf.trigger_doom_explosion(row=2, col=4, damage=1800, create_pit=True)
pft.Lawnf.trigger_jalapeno(row=3, damage=1800)
pft.Lawnf.trigger_ice_shroom(duration=5.0)
pft.Lawnf.trigger_zombie_explosion(row=2, col=4)
```

### Sound Effects

```python
pft.Lawnf.play_sound(SoundType.Buzzer)
```

### Queries & Iterators

```python
# Nearest zombie to a tile
zombie = pft.Lawnf.get_closest_zombie(row=2, col=8)
zombie.damage(500)

# Iterate all live plants on the board
with pft.Lawnf.for_each_plant_on_lawn() as plant:
    plant.heal(50)
```

---

## 3. Player Tools (`Tool`)

The `Tool` interface allows inspecting and manipulating tools held by the player (shovel, hammer, glove, etc.) and their cooldown ratios.

```python
# 1. Query currently held tool
game_obj, held_type = pft.Tool.get_held()

# 2. Check if a specific tool is currently held
with pft.Trigger.OnMouseClick():
    is_shovel = pft.Tool.is_held(ToolType.Shovel)
    with pft.If(is_shovel):
        pft.InGameUI.display_text("Player clicked while holding the Shovel!")

# 3. Inspect tool cooldown
cooldown = pft.Tool.get_cooldown(ToolType.Hammer)
# cooldown.total_seconds
# cooldown.remaining_seconds
# cooldown.exists

# 4. Set tool cooldown ratio (0.0 = ready, 1.0 = full cooldown)
pft.Tool.set_cooldown(ToolType.Glove, ratio=0.0)
```

### `ToolType` Enum Reference

| Enum Value | Name | Description |
| :--- | :--- | :--- |
| `ToolType.None_` | 无 | No tool held |
| `ToolType.Shovel` | 铲子 | Plant removal shovel |
| `ToolType.Glove` | 手套 | Plant moving glove |
| `ToolType.Hammer` | 锤子 | Smashing hammer |
| `ToolType.LawnCleaner` | 小推车 | Lawn mower cleaner tool |
| `ToolType.GoldCoffeeBean`| 金咖啡豆 | Golden coffee bean awaken tool |
| `ToolType.Bucket` | 桶 | Water / nutrient bucket |
| `ToolType.CannonTarget` | 加农炮目标 | Target reticle for Cob Cannons |
| `ToolType.PlantPreview` | 植物预览 | Plant cursor preview |
| `ToolType.ZombiePreview`| 僵尸预览 | Zombie cursor preview |
| `ToolType.Other` | 其他 | Other miscellaneous tools |

---

## 4. World Objects & Entity Binding (`WorldObject`)

`WorldObject` (aliased as `GameObject` and `Object`) encapsulates Unity GameObjects, 3D transforms, and entity binding/casting.

```python
# Create a custom event object
obj = pft.WorldObject.create(name="BossMarker", position=pft.WorldObject.vector3(0, 0, 0))

# Query or adjust 3D transform
transform = obj.get_transform()
# transform.position, transform.scale, transform.exists
obj.set_transform(position=pft.WorldObject.vector3(100, 200, 0), scale_multiplier=1.5)

# Cast GameObject to Plant or Zombie
plant_target = obj.to_plant()          # CastTo
plant_target, ok = obj.try_cast_to_plant()  # TryCast (returns plant and exists port)

# Destroy object
obj.destroy()
```

### Named Entity Bindings (`bind_plant` / `bind_zombie`)

Bind specific plant or zombie instances by name (e.g. "守护目标" / "首领") to easily look them up from other triggers:

```python
# Bind target plant
with pft.Trigger.OnPlantCreate() as plant:
    with pft.If(plant.plantType == PlantType.WallNut):
        pft.WorldObject.bind_plant(plant, name="守护目标")

# Retrieve bound plant in another trigger
with pft.Trigger.OnWave() as wave_num:
    guarded_plant = pft.WorldObject.get_bound_plant(name="守护目标")
    guarded_plant.heal(200)

# Bind and retrieve zombie
with pft.Trigger.OnZombieSpawn() as zombie:
    with pft.If(zombie.zombieType == ZombieType.Gargantuar):
        pft.WorldObject.bind_zombie(zombie, name="首领")

boss_zombie = pft.WorldObject.get_bound_zombie(name="首领")
```

---

## Quick Reference

| Class | Category | Key Members |
| --- | --- | --- |
| `InGameUI` | UI Popups | `display_info_card`, `InfoCard`, `display_text` |
| `InGameUI` | Cards | `give_plant_card`, `remove_plant_card`, `spawn_dropped_card` |
| `Lawnf` | Props | `spawn_grave`, `spawn_crater`, `spawn_ladder`, `spawn_particle`, `spawn_ice_block` |
| `Lawnf` | Effects | `trigger_cherry_explosion`, `trigger_doom_explosion`, `trigger_jalapeno`, `trigger_ice_shroom` |
| `Lawnf` | Sound | `play_sound` |
| `Tool` | Tools | `get_held()`, `is_held(tool_type)`, `get_cooldown()`, `set_cooldown()` |
| `WorldObject` | Objects | `create()`, `destroy()`, `get_transform()`, `set_transform()`, `to_plant()`, `to_zombie()` |
| `WorldObject` | Binding | `bind_plant()`, `get_bound_plant()`, `bind_zombie()`, `get_bound_zombie()` |
