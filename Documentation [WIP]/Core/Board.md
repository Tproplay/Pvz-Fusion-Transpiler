# 🎮 Board State & Economy

The `pvn.Board` interface gives direct access to game resources (Sun, Money) and runtime board state without manually constructing resource nodes.

---

## 1. Sun Management (`Board.Sun`)

`Board.Sun` manages Sun operations, mathematical expressions, and conditional spending.

### Adding & Subtracting Sun

Use in-place operators (`+=`, `-=`) to add or remove Sun:

```python
with pvn.Trigger.OnGameStart():
    pvn.Board.Sun += 150   # Adds 150 Sun

with pvn.Trigger.OnWave():
    pvn.Board.Sun -= 50    # Deducts 50 Sun
```

### Direct Assignment

Assigning directly calculates the delta and emits the required modification nodes:

```python
with pvn.Trigger.OnGameStart():
    pvn.Board.Sun = 500    # Adjusts Sun balance to 500
```

### Sun Conditions & Math

Compare or calculate using `Board.Sun`:

```python
with pvn.Trigger.OnWave() as wave_num:
    with pvn.If(pvn.Board.Sun < 100):
        pvn.Board.Sun += 200
```

### Safe Spending (`SpendSun`)

Use the `SpendSun` context manager to check Sun before executing an action:

```python
with pvn.Trigger.OnKeyDown(pvn.KeyCode.Space):
    with pvn.Board.Sun.SpendSun(100) as tx:
        ...
        
    with tx.Failed:
        pvn.Print("Not enough Sun for Cherry Bomb!")
```

---

## 2. Money Management (`Board.Money`)

`Board.Money` manages persistent coin modifications and purchases.

> **Note:** Direct assignment (`Board.Money = X`) is not supported by the game engine. Use `+=`, `-=`, or `SpendMoney` instead.

### Adding & Removing Coins

```python
with pvn.Trigger.OnZombieDeath():
    pvn.Board.Money += 10    # Grants 10 coins

with pvn.Trigger.OnKeyDown(KeyCode.B):
    pvn.Board.Money -= 50    # Deducts 50 coins
```

### Safe Spending (`SpendMoney`)

Ensures sufficient balance before running purchase logic:

```python
with pvn.Trigger.OnKeyDown(pvn.KeyCode.B):
    with pvn.Board.Money.SpendMoney(100) as purchase:
        pvn.Board.Sun += 300
        
    with purchase.Failed:
        pvn.Print("Insufficient coins to buy Sun!")
```

### Balance Check (`check_money`)

Checks affordability non-destructively without permanently consuming coins:

```python
def on_affordable():
    pvn.Print("Player can afford the perk!")

def on_unaffordable():
    pvn.Print("Perk locked: insufficient coins.")

pvn.Board.Money.check_money(250, on_true_callback=on_affordable, on_false_callback=on_unaffordable)
```

---

## 3. Wave Tracker (`Board.Wave`)

`Board.Wave` returns the current wave number output port:

```python
with pvn.Trigger.OnZombieSpawn() as zombie:
    with pvn.If(pvn.Board.Wave >= 10):
        ...
```

---

## Quick Reference

| Property / Helper | Supported Operations | Description |
| --- | --- | --- |
| `Board.Sun` | `+=`, `-=`, `*=`, `/=`, `=`, comparisons | Manages current level Sun balance |
| `Board.Sun.SpendSun(cost)` | Context manager (`enter`, `.Failed`) | Safely deducts Sun if balance permits |
| `Board.Money` | `+=`, `-=` | Adjusts level coin count |
| `Board.Money.SpendMoney(cost)` | Context manager (`enter`, `.Failed`) | Safely deducts coins if balance permits |
| `Board.Money.check_money(cost, ...)` | Callbacks (`on_true`, `on_false`) | Verifies coin balance non-destructively |
| `Board.Wave` | Read-only output port | Current active wave index |
