import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import KeyCode, PlantType

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

# Global Seeded PRNG Instance (Seed: 777)
rng = pft.Random.Seeded(seed=777, name="Demo_PRNG_State")

# 1. Level Initialization
with pft.Trigger.OnBoardStart():
    pft.InGameUI.display_text("Seeded PRNG Active! Press [X] to Spawn, [R] to Reset Seed.", duration=5.0)

# 2. Press [X] to generate deterministic random entities
with pft.Trigger.OnKeyDown(KeyCode.X):
    # Generate seeded integer coordinates
    rand_row = rng.randint(0, 5)  # change to 4 if playing on a 5-row map
    rand_col = rng.randint(0, 9)

    # Generate a single seeded roll percentage (0.0 - 100.0)
    roll_percent = rng.randf(0.0, 100.0)

    # True 60% / 40% decision branch using the exact roll_percent value
    with pft.If(roll_percent <= 60.0) as flow:
        pft.Spawner.Set_Plant(row=rand_row, col=rand_col, plant_type=PlantType.SunShroom)
        pft.InGameUI.display_text("[Roll: ", roll_percent, "] Spawned SunShroom at (", rand_row, ", ", rand_col, ")")

    with flow.Else:
        pft.Spawner.Set_Plant(row=rand_row, col=rand_col, plant_type=PlantType.DoomFume)
        pft.InGameUI.display_text("[Roll: ", roll_percent, "] Spawned DoomFume at (", rand_row, ", ", rand_col, ")")

# 3. Press [R] to reset seed (Proves determinism: pressing X after R produces identical results)
with pft.Trigger.OnKeyDown(KeyCode.R):
    rng.set_seed(777)
    pft.InGameUI.display_text("Seed reset to 777! Re-run sequence for identical spawns.", duration=3.0)
