# 🏷️ Types, Enums & Constants

The `PvZ_Fusion_Transpiler.Types` module exposes all essential game enumerations, keycodes, bullet types, tool types, and zombie animation clip constants.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import (
    PlantType,
    ZombieType,
    ToolType,
    BulletType,
    KeyCode,
    SoundType,
    SceneType,
    LevelType,
    TravelBuffType,
    AdvBuff,
    UltiBuff,
    TravelDebuff,
    ZombieAnimations,
    ZombieAnimation,
    Plant_DieReason,
)
```

---

## 1. Core Entity Enums

> [!IMPORTANT]
> **Strict Enum Enforcement**: The transpiler enforces type safety by requiring enum instances for `PlantType`, `ZombieType`, `ToolType`, and `BulletType`. Direct integer literals are rejected at compile time.

### `PlantType`
Encompasses all vanilla and fusion plants:
```python
pft.Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.Peashooter)
pft.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.SuperMachineNut)
```

### `ZombieType`
Encompasses all vanilla and custom fusion zombies:
```python
pft.Spawner.Set_Zombie(row=3, col=9, zombie_type=ZombieType.Gargantuar)
pft.Spawner.Set_Zombie(row=1, col=9, zombie_type=ZombieType.UltimateFootballZombie)
```

### `BulletType`
Identifies projectile models when firing via `Spawner.Set_Bullet`:
```python
pft.Spawner.Set_Bullet(row=2, col=3.0, bullet_type=BulletType.FirePea, damage=80.0)
```

### `ToolType`
Represents the 11 player tool types handled by the game engine:

| Enum Member | Game Name | Description |
| :--- | :--- | :--- |
| `ToolType.None_` | 无 | No tool currently held |
| `ToolType.Shovel` | 铲子 | Dig up / remove plants |
| `ToolType.Glove` | 手套 | Move / reposition plants |
| `ToolType.Hammer` | 锤子 | Smash objects or zombies |
| `ToolType.LawnCleaner` | 小推车 | Deploy lawn cleaner mower |
| `ToolType.GoldCoffeeBean` | 金咖啡豆 | Awaken mushrooms in daytime |
| `ToolType.Bucket` | 桶 | Water bucket / fertilizer |
| `ToolType.CannonTarget` | 加农炮目标 | Target reticle for Cob Cannons |
| `ToolType.PlantPreview` | 植物预览 | Plant placement preview |
| `ToolType.ZombiePreview` | 僵尸预览 | Zombie cursor preview |
| `ToolType.Other` | 其他 | Miscellaneous engine tools |

---

## 2. Input & Environment Enums

### `KeyCode`
Maps keyboard inputs for use with `Trigger.OnKeyDown`:
```python
with pft.Trigger.OnKeyDown(KeyCode.Space):
    pft.Board.Sun += 100
```

### `SceneType`
Defines lawn background and pool layouts:
`SceneType.Day`, `SceneType.Night`, `SceneType.Pool`, `SceneType.Fog`, `SceneType.Roof`, `SceneType.SnowPool`, etc.

### `LevelType`
Defines the gameplay mode:
`LevelType.CustomLevel`, `LevelType.Survival`, `LevelType.IZombie`, etc.

### `SoundType`
Audio clip sound IDs for `Lawnf.play_sound`:
`SoundType.Buzzer`, `SoundType.CherryBomb`, `SoundType.Splat`, `SoundType.HugeWave`, etc.

### `AdvBuff`, `UltiBuff`, `TravelDebuff` & `TravelBuffType`
Registries of rogue-lite travel buffs, ultimate abilities, and debuff modifiers (from game reflection `TypeDefIndex: 2757`, `2758`, `2759`):

- **`AdvBuff`**: 232 advanced travel buffs (e.g. `AdvBuff.撒豆成兵`, `AdvBuff.核能威慑`, `AdvBuff.UltimateDoomGatling`, `AdvBuff.Shooting_火神质变`).
- **`UltiBuff`**: 56 ultimate buffs (e.g. `UltiBuff.嗜血如命`, `UltiBuff.流星雨`, `UltiBuff.究炉恢复`).
- **`TravelDebuff`**: 143 travel debuffs (e.g. `TravelDebuff.二爷无视植物`, `TravelDebuff.阳光归零`, `TravelDebuff.Shooting_命运无常`).
- **`TravelBuffType`**: Unified composite enum linking all buff/debuff types with backward-compatible English and Chinese identifiers.

```python
# Apply buffs via Game or Lawnf
pft.Game.get_buff(AdvBuff.撒豆成兵)
pft.Lawnf.get_buff(UltiBuff.流星雨)
pft.Game.get_buff(TravelDebuff.二爷无视植物)
```

### `Plant_DieReason`
Constants representing reasons for plant destruction:
`ByZombie`, `ByShovel`, `ByLevelUp`, etc.

---

## 3. Zombie Animations (`ZombieAnimations`)

`ZombieAnimations` (aliased as `ZombieAnimation`) provides nested enumerations containing the exact animation clip names for every zombie model dumped from the game engine.

```python
with pft.Trigger.OnZombieSpawn() as zombie:
    with pft.If(zombie.zombieType == ZombieType.PolevaulterZombie):
        # Play exact animation clip safely
        zombie.play_animation(ZombieAnimations.PolevaulterZombie.ZOMBIE_POLEVAULTER_RUN)
```
