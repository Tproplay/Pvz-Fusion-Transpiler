import PvZ_Fusion_Transpiler as pft

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

with pft.Trigger.OnGameStart():  # Start the process after the Ready, Set, Go! message appears
    with pft.Time.OnFixedUpdate(1):
        with pft.If(pft.Board.Sun < 500):
            pft.Board.Sun += 25
            pft.InGameUI.display_text("You have received 25 sun!")
