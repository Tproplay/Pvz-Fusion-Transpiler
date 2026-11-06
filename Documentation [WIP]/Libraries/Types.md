# 🏷️ Types, Enums & Constants

The `PvZ_Fusion_Transpiler.Types` module exposes all essential game enumerations, keycodes, bullet types, tool types, in-editor dropdown enums, and zombie animation clip constants.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import (
    PlantType,
    ZombieType,
    ToolType,
    EventToolType,
    BulletType,
    KeyCode,
    SoundType,
    MusicType,
    SceneType,
    LevelType,
    EventGridObstacle,
    EventZombieStat,
    EventZombieStatus,
    EventBulletProperty,
    EventWorldEffect,
    EventTravelEntryKind,
    EventArithmeticOperation,
    Layer,
    ListStorageOperation,
    BuffType,
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
> **Strict Enum Enforcement**: The transpiler enforces type safety per Rule 4 by requiring enum instances for all enum-backed inputs (`PlantType`, `ZombieType`, `ToolType`, `BulletType`, `MusicType`, `SceneType`, etc.). Direct integer literals emit `DeprecationWarning` and wrong enum types raise `TypeError`.

### `PlantType`
Encompasses all vanilla and fusion plants:
```python
pft.Spawner.Set_Plant(row=2, col=2, plant_type=PlantType.Peashooter)
pft.Spawner.Set_Plant(row=2, col=3, plant_type=PlantType.SuperMachineNut)
```

### `ZombieType`
Encompasses all vanilla and custom fusion zombies:
```python
pft.Spawner.Set_Zombie(row=3, col=9, zombie_type=ZombieType.NormalZombie)
pft.Spawner.Set_Zombie(row=1, col=9, zombie_type=ZombieType.Gargantuar)
```

### `BulletType`
Identifies projectile models when firing via `Spawner.Set_Bullet`:
```python
pft.Spawner.Set_Bullet(row=2, col=3.0, bullet_type=BulletType.Bullet_pea, damage=80.0)
```

### `ToolType` (alias: `EventToolType`)
Represents player tool types handled by the game engine:

| Enum Member | Game Name | Value | Description |
| :--- | :--- | :--- | :--- |
| `ToolType.None_` | 无 | 0 | No tool currently held |
| `ToolType.Shovel` | 铲子 | 1 | Dig up / remove plants |
| `ToolType.Glove` | 手套 | 2 | Move / reposition plants |
| `ToolType.Hammer` | 锤子 | 3 | Smash objects or zombies |
| `ToolType.LawnMower` | 小推车 | 4 | Deploy lawn cleaner mower |
| `ToolType.GoldCoffeeBean` | 金咖啡豆 | 5 | Awaken mushrooms in daytime |
| `ToolType.Bucket` | 桶 | 6 | Water bucket / fertilizer |
| `ToolType.CannonTarget` | 加农炮目标 | 7 | Target reticle for Cob Cannons |
| `ToolType.PlantPreview` | 植物预览 | 8 | Plant placement preview |
| `ToolType.ZombiePreview` | 僵尸预览 | 9 | Zombie cursor preview |
| `ToolType.Other` | 其他 | 10 | Miscellaneous engine tools |

---

## 2. In-Editor UI Dropdown Enums

These enums directly correspond to the in-editor dropdown selectors (`NodeEditorControls.Enum<T>`) reverse-engineered from PvZ Fusion's Level Event Editor:

### `MusicType`
Background music tracks selected by `ChangeEventMusicNode` / `Lawnf.change_music()`:

| Value | Member | Description |
| :--- | :--- | :--- |
| 0 | `MusicType.MainMenu` | Main Menu theme |
| 1 | `MusicType.SelectCard` | Seed packet selection screen |
| 2 | `MusicType.Day` | Daytime lawn music |
| 3 | `MusicType.Day_drum` | Daytime battle drums |
| 4 | `MusicType.Night` | Nighttime music |
| 5 | `MusicType.Night_drum` | Nighttime battle drums |
| 6 | `MusicType.Pool` | Pool daytime music |
| 7 | `MusicType.Pool_drum` | Pool battle drums |
| 8 | `MusicType.Fog` | Fog stage music |
| 9 | `MusicType.Fog_drum` | Fog battle drums |
| 10 | `MusicType.Roof` | Roof stage music |
| 11 | `MusicType.Roof_drum` | Roof battle drums |
| 12 | `MusicType.Roof_pre` | Roof introductory music |
| 13 | `MusicType.Loon` | Loonboon mini-game theme |
| 14 | `MusicType.UltimateBattle`| Ultimate Battle track |
| 15 | `MusicType.IZ` | I, Zombie theme |
| 16 | `MusicType.Garden` | Zen Garden theme |
| 17 | `MusicType.Boss` | Zomboss battle 1 |
| 18 | `MusicType.Boss2` | Zomboss battle 2 |
| 19 | `MusicType.Snow` | Snow lawn music |
| 20 | `MusicType.Snow_drum` | Snow battle drums |
| 21 | `MusicType.Snow_boss` | Snow boss battle |
| 22 | `MusicType.RoofPool` | Roof Pool hybrid music |
| 23 | `MusicType.RoofPool_drum`| Roof Pool battle drums |
| 24 | `MusicType.NightSnow` | Night Snow music |
| 25 | `MusicType.NightSnow_drum`| Night Snow battle drums |
| 26 | `MusicType.HorseBoss` | Horse boss battle |
| 27 | `MusicType.SeaBoss` | Sea boss battle |

### `EventGridObstacle`
Obstacle types deleted by `DeleteGridItemsNode` / `Lawnf.delete_grid_items()`:
- `EventGridObstacle.Grave` (0): Tombstone / grave
- `EventGridObstacle.Crater` (1): Doom-shroom explosion crater
- `EventGridObstacle.Ladder` (2): Ladder placed on plants
- `EventGridObstacle.IceBlock` (3): Frozen ice block

### `EventZombieStat`
Target stat read/modified by `GetZombieStatsNode` & `SetZombieStatsNode`:
- `EventZombieStat.AttackPower` (0): Zombie DPS / bite damage
- `EventZombieStat.Armor1HP` (1): Primary armor health (Cone, Bucket, Door)
- `EventZombieStat.Armor2HP` (2): Secondary armor health
- `EventZombieStat.BaseSpeed` (3): Base walking speed
- `EventZombieStat.Size` (4): Visual scale multiplier
- `EventZombieStat.BodyHP` (5): Core body hitpoints
- `EventZombieStat.MaxBodyHP` (6): Maximum body hitpoints

### `EventZombieStatus`
Status effects read/applied by `GetZombieStatusNode` & `SetZombieStatusNode`:
- `EventZombieStatus.ChillSeconds` (0): Slowdown duration
- `EventZombieStatus.Enraged` (1): Enraged speed/damage buff
- `EventZombieStatus.Embers` (2): Fire/burning damage stacks
- `EventZombieStatus.PoisonSeconds` (3): Poison damage over time duration
- `EventZombieStatus.GarlicStacks` (4): Garlic diversion stacks
- `EventZombieStatus.KelpStacks` (5): Tangle Kelp pull stacks
- `EventZombieStatus.FreezeStacks` (6): Accumulating freeze counter
- `EventZombieStatus.FreezeSeconds` (7): Complete frozen state duration
- `EventZombieStatus.TeleportSeconds` (8): Spatial warp / teleport duration

### `EventBulletProperty`
Bullet physics property modified by `ModifyEventBulletNode` / `Bullet.modify()`:
- `EventBulletProperty.ScaleMultiplier` (0): Projectile scale
- `EventBulletProperty.Speed` (1): Velocity in pixels/sec
- `EventBulletProperty.Damage` (2): Direct impact damage
- `EventBulletProperty.DirectionAngle` (3): Trajectory angle in degrees

### `EventWorldEffect`
Global spell event listened to by `OnWorldPlantEffectNode` / `Trigger.OnWorldPlantEffect()`:
- `EventWorldEffect.IceShroom` (0): Global ice screen freeze
- `EventWorldEffect.Jalapeno` (1): Row-wide flame explosion

### `EventTravelEntryKind`
Buff modifier category removed by `RemoveTravelEntryNode` / `Lawnf.remove_travel_entry()`:
- `EventTravelEntryKind.CommonModifier` (0): General travel perks
- `EventTravelEntryKind.UltimateModifier` (1): Ultimate travel perks
- `EventTravelEntryKind.ZombieModifier` (2): Zombie travel curses / debuffs

### `EventArithmeticOperation`
Mathematical operations performed by `IntVariableArithmeticNode` & `FloatVariableArithmeticNode`:
- `EventArithmeticOperation.Add` (0)
- `EventArithmeticOperation.Subtract` (1)
- `EventArithmeticOperation.Multiply` (2)
- `EventArithmeticOperation.Divide` (3)
- `EventArithmeticOperation.Modulo` (4)

### `Layer`
Grid placement layer queried by `GetPlantsOnLayerNode`:
- `Layer.Default` (0): Ground plants
- `Layer.Lily` (1): Water plants / Lily pads
- `Layer.Pumpkin` (2): Protective pumpkins
- `Layer.Pot` (3): Roof flower pots
- `Layer.Fly` (4): Airborne / flying plants

### `ListStorageOperation`
List mutations performed by `PlantTypeListStorageNode`:
- `ListStorageOperation.Set` (0)
- `ListStorageOperation.Add` (1)
- `ListStorageOperation.Remove` (2)

### `BuffType`
Rogue-lite buff category selected by `GetTravelEntryNode`:
- `BuffType.UnlockPlant` (0)
- `BuffType.AdvancedBuff` (1)
- `BuffType.UltimateBuff` (2)
- `BuffType.Debuff` (3)
- `BuffType.InvestmentBuff` (4)

---

## 3. Environment & Audio Enums

### `SceneType`
Defines lawn background layout (0–46):
- `SceneType.Day` (0), `SceneType.Night` (1), `SceneType.Pool` (2), `SceneType.NightPool` (3), `SceneType.Roof` (4), `SceneType.NightRoof` (5)
- Special maps: `SuperDay` (8), `SuperPool` (9), `Travel_roof` (10), `Snow` (18), `Chess` (19), `Swamp` (46), `ClassicTowerLawn` (44), `ClassicTowerLawn2` (45).

### `SoundType`
Audio sound clip effect IDs for `Lawnf.play_sound`:
`SoundType.Buzzer`, `SoundType.CherryBomb`, `SoundType.Splat`, `SoundType.HugeWave`, etc.

### `KeyCode`
Keyboard keycodes for `Trigger.OnKeyDown`:
`KeyCode.Space`, `KeyCode.W`, `KeyCode.A`, `KeyCode.S`, `KeyCode.D`, `KeyCode.Return`, etc.

---

## 4. Buff Registries (`AdvBuff`, `UltiBuff`, `TravelDebuff`)

- **`AdvBuff`**: 232 advanced travel buffs with official English PascalCase names, full in-editor effect descriptions in attribute docstrings, and Chinese / legacy aliases (e.g. `AdvBuff.CallToArms`, `AdvBuff.Overclock`, `AdvBuff.Overkill`, `AdvBuff.SPEvolution_DoomGatling`, `AdvBuff.Ascend_Inferno`, `AdvBuff.BlessingOfEndurance`).
- **`UltiBuff`**: 56 ultimate buffs (e.g. `UltiBuff.嗜血如命`, `UltiBuff.流星雨`, `UltiBuff.究炉恢复`).
- **`TravelDebuff`**: 143 travel debuffs (e.g. `TravelDebuff.二爷无视植物`, `TravelDebuff.阳光归零`).
- **`TravelBuffType`**: Unified composite enum linking all buff/debuff types with bilingual English and Chinese identifiers.

```python
# Granting an advanced travel buff
pft.Game.get_buff(AdvBuff.CallToArms)
pft.Game.get_buff(AdvBuff.Overkill)
```

---

## 5. Zombie Animations (`ZombieAnimations`)

`ZombieAnimations` (alias `ZombieAnimation`) provides nested enumerations containing exact animation clip names for every zombie model:

```python
with pft.Trigger.OnZombieSpawn() as zombie:
    with pft.If(zombie.zombieType == ZombieType.PolevaulterZombie):
        zombie.play_animation(ZombieAnimations.PolevaulterZombie.ZOMBIE_POLEVAULTER_RUN)
```
