import PvzRH_node as pvn
from PvzRH_node.Types import PlantType

# Configure the output folder and name
pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

# Configure the grouping level (0 by default)
pvn.settings.group_level = 1

def Give_sun():
    pvn.Board.Sun += 100
    pvn.InGameUI.display_text("Gave ", 100, " sun!")

def main():
    with pvn.Trigger.OnPlantClicked() as plant:
        with pvn.If(plant.plantType == PlantType.SunFlower):
            Give_sun()

pvn.add_graph(main)