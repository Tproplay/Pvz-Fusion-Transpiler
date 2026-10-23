# 🎮 Board State, Economy & Stages

The `pft.Board` (and `pft.Game`) interface gives direct access to game resources (Sun, Money), wave progression, timers, and multi-stage level transitions.

```python
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import KeyCode, TravelBuffType
```

> [!NOTE]
> `pft.Board` is an alias of `pft.Game`. All resource and stage methods can be called interchangeably on either `Board` or `Game`.

---

## 1. Sun Management (`Board.Sun`)

`Board.Sun` manages Sun operations, mathematical expressions, and conditional spending.

### Adding & Subtracting Sun

Use in-place operators (`+=`, `-=`) to add or remove Sun:

```python
with pft.Trigger.OnGameStart():
    pft.Board.Sun += 150   # Adds 150 Sun

with pft.Trigger.OnWave():
    pft.Board.Sun -= 50    # Deducts 50 Sun
```

### Direct Assignment

Assigning directly calculates the delta and emits the required modification nodes:

```python
with pft.Trigger.OnGameStart():
    pft.Board.Sun = 500    # Adjusts Sun balance to 500
```

### Sun Conditions & Math

Compare or calculate using `Board.Sun`:

```python
with pft.Trigger.OnWave() as wave_num:
    with pft.If(pft.Board.Sun < 100):
        pft.Board.Sun += 200
```

### Safe Spending (`SpendSun`)

Use the `SpendSun` context manager to check if the player has enough Sun before executing an action:

```python
with pft.Trigger.OnKeyDown(KeyCode.Space):
    with pft.Board.Sun.SpendSun(100) as tx:
        pft.InGameUI.display_text("Spent 100 Sun!")
        
    with tx.Failed:
        pft.InGameUI.display_text("Not enough Sun!")
```

---

## 2. Money Management (`Board.Money`)

`Board.Money` manages level coin balances and purchases.

> **Note:** Direct assignment (`Board.Money = X`) is not supported by the game engine. Use `+=`, `-=`, or `SpendMoney` instead.

### Adding & Removing Coins

```python
with pft.Trigger.OnZombieDeath():
    pft.Board.Money += 10    # Grants 10 coins

with pft.Trigger.OnKeyDown(KeyCode.B):
    pft.Board.Money -= 50    # Deducts 50 coins
```

### Safe Spending (`SpendMoney`)

Ensures sufficient balance before running purchase logic:

```python
with pft.Trigger.OnKeyDown(KeyCode.B):
    with pft.Board.Money.SpendMoney(100) as purchase:
        pft.Board.Sun += 300
        pft.InGameUI.display_text("Bought 300 Sun for 100 coins!")
        
    with purchase.Failed:
        pft.InGameUI.display_text("Insufficient coins!")
```

### Affordability Check (`check_money`)

Checks affordability non-destructively without consuming coins:

```python
def on_affordable():
    pft.InGameUI.display_text("Perk available!")

def on_unaffordable():
    pft.InGameUI.display_text("Perk locked: insufficient coins.")

pft.Board.Money.check_money(250, on_true_callback=on_affordable, on_false_callback=on_unaffordable)
```

---

## 3. Wave & Countdown Control

### Wave Tracker (`Board.Wave`)

`Board.Wave` returns the current active wave integer output port:

```python
with pft.Trigger.OnZombieSpawn() as zombie:
    with pft.If(pft.Board.Wave >= 10):
        zombie.set_speed_multiplier(1.2)
```

### Pausing Wave Countdown

Pause or resume the automatic wave timer:

```python
# Pause wave countdown
pft.Game.pause_wave_timer(paused=True)

# Resume countdown
pft.Game.pause_wave_timer(paused=False)
```

---

## 4. Multi-Stage Levels (`Game.Stage`)

Manage level stages and transitions for complex multi-phase boss fights or minigames:

```python
# Get current stage name port
current_stage = pft.Game.Stage.get_current()

# Transition to a new stage
with pft.Trigger.OnWaveCleared() as wave_num:
    with pft.If(wave_num == 5):
        pft.Game.Stage.change(stage_name="二阶段")  # alias: pft.Game.Stage.next
```

Combine with `Trigger.OnStageEnter` to trigger setup logic upon entering the stage:

```python
with pft.Trigger.OnStageEnter(stage_name="二阶段"):
    pft.InGameUI.display_text("Phase 2 Begins!", duration=5.0)
    pft.Board.Sun += 1000
```

---

## 5. Game Outcome & Buffs

```python
# Trigger victory
pft.Game.trigger_game_win()

# Trigger game over with custom loss message
pft.Game.trigger_game_over(reason="Your lawn was overrun!")

# Grant rogue-lite travel buff
pft.Game.get_buff(TravelBuffType.SomeBuff)
```

---

## Quick Reference

| Property / Helper | Supported Operations | Description |
| --- | --- | --- |
| `Board.Sun` | `+=`, `-=`, `*=`, `/=`, `=`, comparisons | Manages level Sun balance |
| `Board.Sun.SpendSun(cost)` | Context manager (`enter`, `.Failed`) | Safely deducts Sun if balance permits |
| `Board.Money` | `+=`, `-=` | Adjusts level coin count |
| `Board.Money.SpendMoney(cost)` | Context manager (`enter`, `.Failed`) | Safely deducts coins if balance permits |
| `Board.Money.check_money(cost, ...)` | Callbacks (`on_true`, `on_false`) | Verifies coin balance non-destructively |
| `Board.Wave` | Read-only output port | Current active wave index |
| `Game.pause_wave_timer(paused)` | Method | Pauses/resumes wave countdown |
| `Game.Stage.get_current()` | Method (string port) | Current stage name |
| `Game.Stage.change(stage_name)` | Method | Transitions level to named stage |
| `Game.trigger_game_win()` | Method | Triggers immediate victory |
| `Game.trigger_game_over(reason)` | Method | Triggers game over with reason |
