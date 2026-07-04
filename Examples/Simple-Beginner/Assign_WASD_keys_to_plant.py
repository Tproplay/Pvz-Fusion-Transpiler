import PvzRH_node as pvn
from PvzRH_node.StdLib import WASDPlant

pvn.settings.group_level = 1

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

def main():
    with pvn.Trigger.OnPlantClicked() as plant:
        WASDPlant(plant).Start()
        pvn.InGameUI.display_text("You selected the plant: <color=blue>", plant.plantType, "</color>!")
    
pvn.add_graph(main)