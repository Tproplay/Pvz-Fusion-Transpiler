# ⏱️ Time & Delays

The `pvn.Time` module provides high-level constructs for asynchronous delays, recurring fixed-interval update loops, and global game time tracking on the visual node canvas.

```python
import PvzRH_node as pvn
```

---

## 1. Pausing Execution (`Time.Wait`)

The `Wait` context manager pauses the current execution timeline for a specified duration (in seconds) without blocking the main game engine thread. Any logic nested inside the block will execute after the timer finishes.

```python
with pvn.Trigger.OnGameStart():
    pvn.Print("Ready...")
    
    # Pause execution for 2 seconds
    with pvn.Time.Wait(2.0):
        pvn.Print("Set...")
        
        # Pause for another 1 second
        with pvn.Time.Wait(1.0):
            pvn.Print("PLANT!")
```

---

## 2. High-Frequency Loops (`Time.OnFixedUpdate`)

`OnFixedUpdate` creates a recurring execution loop driven by the engine's native `ToggleCycleNode`. It is ideal for continuous monitoring, custom physics, or damage-over-time effects.

### Basic Interval Looping

By default, the block executes every `0.1` seconds (10 ticks per second) immediately upon entering the context.

```python
with pvn.Trigger.OnGameStart():
    # Continuously grant 1 Sun every 0.5 seconds
    with pvn.Time.OnFixedUpdate(interval=0.5):
        pvn.Board.Sun += 1
```

### Tick Tracking & Branching

The `.tick` property acts as a lazy-loaded `CounterNode` output port that tracks how many times the loop has executed.

```python
with pvn.Trigger.OnBoardStart():
    with pvn.Time.OnFixedUpdate(interval=1.0) as update:
        # Trigger an event exactly on the 60th tick (1 minute mark)
        with pvn.If(update.tick == 60):
            pvn.Print("60 seconds have passed!")
```

### Toggling & Lifecycle Events

The loop can be turned on or off dynamically using `.toggle()`. You can also hook into specific lifecycle execution paths (`on_enable`, `on_disable`, `on_cycle`).

```python
timer_loop = pvn.Time.OnFixedUpdate(interval=0.1)

with pvn.Trigger.OnKeyDown(KeyCode.T):
    # Turn the loop on/off
    timer_loop.toggle()

# Execute logic exactly when the loop is switched on
with timer_loop.on_enable:
    pvn.Print("Timer activated.")

# Define the recurring behavior
with timer_loop.on_cycle:
    pvn.Board.Money += 10
```

---

## 3. Global Time Tracking

The `Time` module exposes lazy-loaded global float variables that track the elapsed time in seconds. When first accessed, the transpiler automatically generates the necessary background increment loops.

* **`Time.time_since_start`**: Tracks time starting from the very first frame of level initialization (includes the "Ready, Set, Plant" panning sequence).
* **`Time.time_since_game_start`**: Tracks time starting only after active gameplay begins.

```python
with pvn.Trigger.OnZombieSpawn() as zombie:
    # Scale zombie health based on how long the active game has been running
    health_boost = Math.lerp(1.0, 3.0, pvn.Time.time_since_game_start / 300.0)
    zombie.set_health_multiplier(health_boost)
```

---

## Quick Reference

| Class / Property | Type | Description |
| --- | --- | --- |
| `Time.Wait(duration)` | Context Manager | Delays execution of nested logic by `duration` seconds |
| `Time.OnFixedUpdate(interval)` | Context Manager | Repeats nested logic every `interval` seconds |
| `update.tick` | Output Port | The integer count of how many times the loop has cycled |
| `update.toggle()` | Method | Dynamically turns the recurring loop on or off |
| `Time.time_since_start` | Output Port | Float seconds elapsed since board initialization |
| `Time.time_since_game_start` | Output Port | Float seconds elapsed since active gameplay started |