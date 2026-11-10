import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.StdLib import WASDPlant

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

with pft.Trigger.OnPlantClicked() as plant:
    WASDPlant(plant).Start()
    pft.InGameUI.display_text("You selected the plant: <color=blue>", plant.plantType, "</color>!")
