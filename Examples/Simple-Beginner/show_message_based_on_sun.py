import PvZ_Fusion_Transpiler as pft

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)


def show_message_based_on_sun():
    with pft.If(pft.Board.Sun >= 1000) as flow:
        pft.InGameUI.display_text("You have a lot of sun!", duration=1.5)
    with flow.Elif(pft.Board.Sun >= 500) as flow:
        pft.InGameUI.display_text("You have some sun!", duration=1.5)
    with flow.Else:
        pft.InGameUI.display_text("You have little sun!", duration=1.5)


with pft.Trigger.OnGameStart():  # Start the process after the Ready, Set, Go! message appears
    with pft.Time.OnFixedUpdate(4):
        show_message_based_on_sun()
