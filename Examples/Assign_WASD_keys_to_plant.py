import PvzRH_node as pvn
from PvzRH_node.StdLib import WASDPlant

pvn.settings.group_level = 2

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

def main():
    with pvn.Trigger.OnPlantClicked() as plant:
        pvn.GameAPP.display_text("You selected the plant: <color=blue>", plant.plantType, "</color>!")
        WASDPlant(plant).Start()
    
pvn.add_graph(main)