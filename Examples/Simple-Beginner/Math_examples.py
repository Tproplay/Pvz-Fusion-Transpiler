import PvzRH_node as pvn
from PvzRH_node import Math

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

pvn.settings.group_level = 1

n = pvn.IntVar() # Create an integer variable to keep track of the current example index
Six = pvn.IntVar(6) # Create an integer variable to hold the value 6 for the sine example

def main():
    global n
    with pvn.Trigger.OnGameStart():
        update = pvn.Time.OnFixedUpdate(2)
        
    with update.on_cycle:
        with pvn.Switch(n) as switch:
            with switch.case(0):
                pvn.Print("abs(-5) = ", Math.abs(-5))
                n += 1
            with switch.case(1):
                pvn.Print("floor(3.8) = ", Math.floor(3.8))
                n += 1
            with switch.case(2):
                pvn.Print("min(-1, -5) = ", Math.min(-1, -5))
                n += 1
            with switch.case(3):
                pvn.Print("sqrt(16) = ", Math.sqrt(16))
                n += 1
            with switch.case(4):
                pvn.Print("sin(Math.PI/6) = ", Math.sin(Math.PI/Six))
                n += 1
            with switch.case(5):
                pvn.Print("is_prime(5) = ", Math.is_prime(5))
                n += 1
            with switch.default:
                pvn.Print("No more Math examples.")
                n.set(0)

pvn.add_graph(main)