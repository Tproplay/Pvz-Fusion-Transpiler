import PvzRH_node as pvn
from PvzRH_node import KeyCode, PlantType

pvn.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test"
)
pvn.settings.group_level = 1

# 🎲 Global Seeded PRNG Instance (Seed: 777)
rng = pvn.Random.Seeded(seed=777, name="Demo_PRNG_State")

def main():
    # 1. Level Initialization
    with pvn.Trigger.OnBoardStart():
        pvn.InGameUI.display_text("Seeded PRNG Active! Press [X] to Spawn, [R] to Reset Seed.", duration=5.0)

    # 2. Press [X] to generate deterministic random entities
    with pvn.Trigger.OnKeyDown(KeyCode.X):
        # Generate seeded integer coordinates
        rand_row = rng.randint(0, 5) # change to 4 if playing on a 5-row map
        rand_col = rng.randint(0, 9)
        
        # Generate a single seeded roll percentage (0.0 - 100.0)
        roll_percent = rng.randf(0.0, 100.0)

        # True 60% / 40% decision branch using the exact roll_percent value
        with pvn.If(roll_percent <= 60.0) as flow:
            pvn.Spawner.Set_Plant(row=rand_row, col=rand_col, plant_type=PlantType.SunShroom)
            pvn.InGameUI.display_text("[Roll: ", roll_percent, "] Spawned SunShroom at (", rand_row, ", ", rand_col, ")")
            
        with flow.Else:
            pvn.Spawner.Set_Plant(row=rand_row, col=rand_col, plant_type=PlantType.DoomFume)
            pvn.InGameUI.display_text("[Roll: ", roll_percent, "] Spawned DoomFume at (", rand_row, ", ", rand_col, ")")

    # 3. Press [R] to reset seed (Proves determinism: pressing SPACE after R produces identical results)
    with pvn.Trigger.OnKeyDown(KeyCode.R):
        rng.set_seed(777)
        pvn.InGameUI.display_text("Seed reset to 777! Re-run sequence for identical spawns.", duration=3.0)

pvn.add_graph(main)