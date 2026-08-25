import PvzRH_node as pvn
from PvzRH_node.Types import SceneType, PlantType
from PvzRH_node.Math import perlin_noise

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

pvn.settings.group_level = 1

pvn.level_config.scene_type = SceneType.SuperDay # Use the big map, 18 row, 24 col

def main():
    with pvn.Trigger.OnGameStart():
        for row in range(18):
            for col in range(24):
                with pvn.If(perlin_noise(col*0.3,row*0.3)>=0.5):
                    pvn.Spawner.Set_Plant(row,col,PlantType.Bamboo)
    
pvn.add_graph(main)