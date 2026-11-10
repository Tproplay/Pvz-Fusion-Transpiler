import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import PlantType

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

menu = pft.MultiSelectMenu()


@menu.option("Give Sun", "Gives 200 sun to the player.", plant_type=PlantType.SunFlower)
def Give_Sun():
    pft.Board.Sun += 200


@menu.option("Give Money", "Gives 2000 money to the player.", plant_type=PlantType.SunFlower)
def Give_Money():
    pft.Board.Money += 2000


with pft.Trigger.OnWave():
    menu.show()
