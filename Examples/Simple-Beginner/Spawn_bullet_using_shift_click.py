import PvZ_Fusion_Node as pvn

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

pvn.settings.group_level = 1

def main():
    with pvn.Trigger.OnMouseClick() as mouse_click:
        pvn.Print("Mouse Clicked at: ", mouse_click.world_position.x, mouse_click.world_position.y)
    
pvn.add_graph(main)