# ⏱️ Time & Delays

The `pft.Time` module provides high-level constructs for asynchronous delays, recurring fixed-interval update loops, and global game time tracking on the visual node canvas.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import Time
from PvZ_Fusion_Transpiler.Types import KeyCode
```

---

## 1. Pausing Execution (`Time.Wait`)

The `Wait` context manager pauses the current execution timeline for a specified duration (in seconds) without blocking the engine. Any logic nested inside the block executes after the timer completes.

```python
with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text("Ready...")
    
    # Pause execution for 2 seconds
    with pft.Time.Wait(2.0):
        pft.InGameUI.display_text("Set...")
        
        # Pause for another 1 second
        with pft.Time.Wait(1.0):
            pft.InGameUI.display_text("PLANT!")
```

---

## 2. Recurring Loops (`Time.OnFixedUpdate`)

`OnFixedUpdate` creates a recurring execution loop driven by the engine's native `ToggleCycleNode`. It is ideal for continuous monitoring, custom physics, or damage-over-time effects.

### Basic Interval Looping

```python
with pft.Trigger.OnGameStart():
    # Grant 1 Sun every 0.5 seconds
    with pft.Time.OnFixedUpdate(interval=0.5):
        pft.Board.Sun += 1
```

### Tick Tracking & Branching

The `.tick` property acts as a lazy-loaded `CounterNode` output port tracking how many times the loop has cycled:

```python
with pft.Trigger.OnBoardStart():
    with pft.Time.OnFixedUpdate(interval=1.0) as update:
        # Trigger an event exactly on the 60th second
        with pft.If(update.tick == 60):
            pft.InGameUI.display_text("1 minute has elapsed!")
```

### Toggling & Lifecycle Events

Dynamically start or stop the loop using `.toggle()`. Hook into specific lifecycle execution paths (`on_enable`, `on_disable`, `on_cycle`):

```python
timer_loop = pft.Time.OnFixedUpdate(interval=0.1)

with pft.Trigger.OnKeyDown(KeyCode.T):
    # Turn the loop on/off
    timer_loop.toggle()

# Logic when switched on
with timer_loop.on_enable:
    pft.InGameUI.display_text("Timer activated")

# Recurring cycle logic
with timer_loop.on_cycle:
    pft.Board.Money += 1
```

---

## 3. Global Time Tracking

The `Time` module exposes lazy-loaded global float variables tracking elapsed seconds:

* **`Time.time_since_start`**: Tracks seconds starting from the first frame of board load (includes introductory panning).
* **`Time.time_since_game_start`**: Tracks seconds starting only after active gameplay begins.

```python
with pft.Trigger.OnZombieSpawn() as zombie:
    # Scale zombie speed based on active gameplay elapsed time
    with pft.If(pft.Time.time_since_game_start > 120.0):
        zombie.set_speed_multiplier(1.3)
```

---

## Quick Reference

| Class / Property | Type | Description |
| :--- | :--- | :--- |
| `Time.Wait(duration)` | Context Manager | Delays execution of nested logic by `duration` seconds |
| `Time.OnFixedUpdate(interval)` | Context Manager | Repeats nested logic every `interval` seconds |
| `update.tick` | Output Port | Integer count of completed loop cycles |
| `update.toggle()` | Method | Dynamically turns recurring loop on or off |
| `Time.time_since_start` | Output Port | Elapsed seconds since board initialization |
| `Time.time_since_game_start` | Output Port | Elapsed seconds since active gameplay started |
