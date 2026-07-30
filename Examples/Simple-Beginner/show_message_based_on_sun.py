import PvzRH_node as pvn

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")
pvn.settings.group_level = 1

def show_message_based_on_sun():
    with pvn.If(pvn.Board.Sun >= 1000) as flow:
        pvn.InGameUI.display_text("You have a lot of sun!",duration=1.5)
    with flow.Elif(pvn.Board.Sun >= 500) as flow:
        pvn.InGameUI.display_text("You have some sun!",duration=1.5)
    with flow.Else:
        pvn.InGameUI.display_text("You have little sun!",duration=1.5)

def main():
    with pvn.Trigger.OnGameStart(): # Start the process after the Ready, Set, Go! message appears
        with pvn.Time.OnFixedUpdate(4):
            show_message_based_on_sun()
            
pvn.add_graph(main)