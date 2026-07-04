import PvzRH_node as pvn

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")
pvn.settings.group_level = 1

def main():
    with pvn.Trigger.OnKeyDown(pvn.KeyCode.Delete):
        with pvn.Lawnf.for_each_plant_on_lawn() as plant:
            plant.die()
        pvn.InGameUI.display_text("All plants have been removed!")

pvn.add_graph(main)