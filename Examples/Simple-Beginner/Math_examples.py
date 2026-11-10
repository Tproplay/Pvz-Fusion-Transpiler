import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler import Math

pft.Config(
    output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
    name="Test",
)

n = pft.IntVar()  # Create an integer variable to keep track of the current example index
Six = pft.IntVar(6)  # Create an integer variable to hold the value 6 for the sine example

with pft.Trigger.OnGameStart():
    update = pft.Time.OnFixedUpdate(2)

with update.on_cycle:
    with pft.Switch(n) as switch:
        with switch.case(0):
            pft.InGameUI.display_text("abs(-5) = ", Math.abs(-5))
            n += 1
        with switch.case(1):
            pft.InGameUI.display_text("floor(3.8) = ", Math.floor(3.8))
            n += 1
        with switch.case(2):
            pft.InGameUI.display_text("min(-1, -5) = ", Math.min(-1, -5))
            n += 1
        with switch.case(3):
            pft.InGameUI.display_text("sqrt(16) = ", Math.sqrt(16))
            n += 1
        with switch.case(4):
            pft.InGameUI.display_text("sin(Math.PI/6) = ", Math.sin(Math.PI / Six))
            n += 1
        with switch.case(5):
            pft.InGameUI.display_text("is_prime(5) = ", Math.is_prime(5))
            n += 1
        with switch.default:
            pft.InGameUI.display_text("No more Math examples.")
            n.set(0)
