import PvzRH_node as pvn

pvn.settings.group_level = 1

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

menu = pvn.MultiSelectMenu()

@menu.option("Give Sun", "Gives 200 sun to the player.", plant_type=pvn.PlantType.SunFlower)
def Give_Sun():
    pvn.Board.Sun += 200

@menu.option("Give Money", "Gives 2000 money to the player.", plant_type=pvn.PlantType.SunFlower)
def Give_Money():
    pvn.Board.Money += 2000
    
with pvn.Trigger.OnWave():
    menu.show()    

