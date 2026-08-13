import PvzRH_node as pvn
from PvzRH_node import Math
from PvzRH_node.StdLib import format_string

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")
pvn.settings.group_level = 1

def format_time(time_in_seconds):
    minutes = Math.floor(time_in_seconds / 60)
    seconds = Math.floor(time_in_seconds % 60)
    return format_string(minutes, " m ", seconds, " s")

def main():
    with pvn.Trigger.OnPlantCreate():
        with pvn.Time.OnFixedUpdate(0.5):  # Update every 0.5 seconds
            pvn.InGameUI.display_text("Time since start: ", format_time(pvn.Time.time_since_start), duration=0.5)
            
pvn.add_graph(main)