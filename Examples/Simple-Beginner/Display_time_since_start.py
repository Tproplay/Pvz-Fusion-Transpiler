import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import Math
from PvZ_Fusion_Transpiler.StdLib import format_string

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)


def format_time(time_in_seconds):
    minutes = Math.floor(time_in_seconds / 60)
    seconds = time_in_seconds % 60
    return format_string(minutes, " m ", seconds, " s")


with pft.Trigger.OnPlantCreate():
    with pft.Time.OnFixedUpdate(0.5):  # Update every 0.5 seconds
        pft.InGameUI.display_text("Time since start: ", format_time(pft.Time.time_since_start), duration=0.5)
