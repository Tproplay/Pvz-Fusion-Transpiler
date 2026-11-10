import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import SceneType, PlantType
from PvZ_Fusion_Transpiler.Math import perlin_noise

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

pft.level_config.scene_type = SceneType.SuperDay  # Use the big map, 18 row, 24 col

with pft.Trigger.OnGameStart():
    for row in range(18):
        for col in range(24):
            if perlin_noise(col * 0.3, row * 0.3) >= 0.5:
                pft.Spawner.Set_Plant(row, col, PlantType.Bamboo)
