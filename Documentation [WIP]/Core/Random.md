# 🎲 Randomization & Probability

The `pvn.Random` namespace provides standard non-deterministic random functions, execution path scramblers, and a fully deterministic Linear Congruential Generator (LCG) built entirely out of native math nodes.

```python
import PvzRH_node as pvn
```

---

## 1. Value Generation

Generate inline random numbers to feed into other nodes (like coordinates, delays, or damage scaling).

```python
with pvn.Trigger.OnZombieSpawn() as zombie:
    # Random integer between 1 and 5
    rand_lane = pvn.Random.randint(1, 5)
    
    # Random float multiplier between 0.8 and 1.5
    speed_mod = pvn.Random.randf(0.8, 1.5)
    
    # Random normalized float (0.0 to 1.0)
    chance_val = pvn.Random.value
    
    zombie.move(row=rand_lane, col=9)
    zombie.set_speed(speed_mod)
```

---

## 2. Probability Triggers

Use `TriggerChance` to gate execution behind a specific probability, or `RandomTrigger` to fan out execution unpredictably.

### `TriggerChance` (Percentage-Based Execution)

Executes the block if the random roll falls within the probability threshold (0.0 to 1.0).

```python
with pvn.Trigger.OnZombieDeath():
    # 25% chance to drop 50 extra sun
    with pvn.Random.TriggerChance(0.25):
        pvn.Board.Sun += 50
```

### `RandomTrigger` (Path Scrambling)

Randomly selects one or more connected child execution paths.

```python
with pvn.Trigger.OnWave():
    # Triggers exactly 1 of the child execution chains
    with pvn.Random.RandomTrigger(count=1):
        # ... Chain A
        # ... Chain B
        # ... Chain C
```

---

## 3. Seeded Deterministic PRNG (`Random.Seeded`)

For procedural generation, rogue-like mechanics, or reproducible custom levels, the `Seeded` class implements a deterministic Linear Congruential Generator using node variables. It guarantees the same numeric sequence on every run, carefully avoiding 32-bit integer overflows in the Unity C# backend.

### Initialization & Setup

Declare the generator globally with a chosen seed and variable name.

```python
rng = pvn.Random.Seeded(seed=9999, name="Level_RNG_State")
```

### Seeded Generation Methods

The API perfectly mirrors the standard `Random` methods, but draws from the tracked deterministic sequence.

```python
with pvn.Trigger.OnGameStart():
    # Generates identical values every time the level restarts
    seeded_col = rng.randint(4, 8)
    seeded_delay = rng.randf(1.0, 5.0)
    
    pvn.Spawner.Set_Plant(row=2, col=seeded_col, plant_type=pvn.PlantType.Repeater)

with pvn.Trigger.OnZombieDeath():
    # 10% deterministic chance to heal plants
    with rng.TriggerChance(0.1):
        ...
```

### Dynamic Re-Seeding

You can reset or change the seed dynamically during gameplay using `.set_seed()`.

```python
with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(wave_num == 5):
        # Re-seed using the wave number to guarantee wave 5 behaves consistently
        rng.set_seed(wave_num * 100)
```