# 🎲 Randomization & Probability

The `pft.Random` namespace provides non-deterministic random functions, execution path scramblers, and a deterministic Linear Congruential Generator (LCG) built entirely out of native visual script nodes.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import Random
from PvZ_Fusion_Transpiler.Types import PlantType
```

---

## 1. Value Generation

Generate inline random numbers to feed into node parameters (coordinates, multipliers, delays):

```python
with pft.Trigger.OnZombieSpawn() as zombie:
    # Random integer between 1 and 5
    rand_lane = pft.Random.randint(1, 5)
    
    # Random float multiplier between 0.8 and 1.5
    speed_mod = pft.Random.randf(0.8, 1.5)
    
    # Normalized random float (0.0 to 1.0)
    chance_val = pft.Random.value
    
    zombie.set_speed_multiplier(speed_mod)
```

---

## 2. Probability Triggers

### `TriggerChance` (Percentage-Based Execution)

Executes the block if a random roll falls within the probability threshold (`0.0` to `1.0`):

```python
with pft.Trigger.OnZombieDeath():
    # 25% chance to drop 50 extra sun
    with pft.Random.TriggerChance(0.25):
        pft.Board.Sun += 50
```

### `RandomTrigger` (Path Scrambling)

Randomly selects one or more connected child execution paths:

```python
with pft.Trigger.OnWave():
    # Triggers exactly 1 of the child execution chains
    with pft.Random.RandomTrigger(count=1):
        pft.InGameUI.display_text("Outcome A")
```

---

## 3. Seeded Deterministic PRNG (`Random.Seeded`)

For procedural generation or reproducible custom levels, the `Seeded` class implements a deterministic Linear Congruential Generator using node variables. It guarantees the identical numeric sequence on every run.

### Initialization & Setup

```python
rng = pft.Random.Seeded(seed=9999, name="Level_RNG_State")
```

### Seeded Methods

```python
with pft.Trigger.OnGameStart():
    # Generates identical values every time the level restarts
    seeded_col = rng.randint(2, 6)
    pft.Spawner.Set_Plant(row=2, col=seeded_col, plant_type=PlantType.Repeater)

with pft.Trigger.OnZombieDeath():
    # 10% deterministic chance to reward coins
    with rng.TriggerChance(0.1):
        pft.Board.Money += 15
```

### Dynamic Re-Seeding

Reset or alter the seed during gameplay using `.set_seed()`:

```python
with pft.Trigger.OnWave() as wave_num:
    rng.set_seed(wave_num * 100)
```

---

## Quick Reference

| Method | Type | Description |
| :--- | :--- | :--- |
| `Random.randint(a, b)` | Integer Port | Random integer between `a` and `b` inclusive |
| `Random.randf(a, b)` | Float Port | Random float between `a` and `b` |
| `Random.value` | Float Port | Random float between `0.0` and `1.0` |
| `Random.TriggerChance(prob)` | Context Manager | Executes body with probability `prob` (`0.0` to `1.0`) |
| `Random.RandomTrigger(count)`| Context Manager | Randomly picks `count` child paths |
| `Random.Seeded(seed, name)` | Generator Class | Seeded reproducible pseudo-random generator |
