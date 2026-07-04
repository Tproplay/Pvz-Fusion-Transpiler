import PvzRH_node as pvn

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

pvn.settings.group_level = 1

def main():
    with pvn.Trigger.OnGameStart(): # Start the process after the Ready, Set, Go! message appears
        with pvn.Time.OnFixedUpdate(1):
            with pvn.If(pvn.Board.Sun < 500):
                pvn.Board.Sun += 25
                pvn.InGameUI.display_text("You have received 25 sun!")
    
pvn.add_graph(main)