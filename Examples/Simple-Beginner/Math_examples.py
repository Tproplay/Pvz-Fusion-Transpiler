import PvzRH_node as pvn
from PvzRH_node import Math

pvn.Config(output=r"C:\Users\Tproplay\AppData\LocalLow\LanPiaoPiao\PlantsVsZombiesRH\Saves\Custm Lvl\LevelData\Levels",
           name="Test")

pvn.settings.group_level = 1

n = pvn.IntVar()

def main():
    global n
    with pvn.Trigger.OnGameStart():
        update = pvn.Time.OnFixedUpdate(2)
        
    with update.on_cycle:
        with pvn.Switch(n) as switch:
            with switch.case(0):
                pvn.InGameUI.display_text("abs(-5) = ", Math.abs(-5))
                n += 1
            with switch.case(1):
                pvn.InGameUI.display_text("ceil(3.2) = ", Math.ceil(3.2))
                n += 1
            with switch.case(2):
                pvn.InGameUI.display_text("floor(3.8) = ", Math.floor(3.8))
                n += 1
            with switch.case(3):
                pvn.InGameUI.display_text("round(3.5) = ", Math.round(3.5))
                n += 1
            with switch.case(4):
                pvn.InGameUI.display_text("max(1, 5) = ", Math.max(1, 5))
                n += 1
            with switch.case(5):
                pvn.InGameUI.display_text("min(-1, -5) = ", Math.min(-1, -5))
                n += 1
            with switch.case(6):
                pvn.InGameUI.display_text("clamp(5, 1, 10) = ", Math.clamp(5, 1, 10))
                n += 1
            with switch.case(7):
                pvn.InGameUI.display_text("clamp01(15) = ", Math.clamp01(15))
                n += 1
            with switch.case(8):
                pvn.InGameUI.display_text("lerp(0, 10, 0.5) = ", Math.lerp(0, 10, 0.5))
                n += 1
            with switch.case(9):
                pvn.InGameUI.display_text("lerp_unclamped(0, 10, 1.5) = ", Math.lerp_unclamped(0, 10, 1.5))
                n += 1
            with switch.case(10):
                pvn.InGameUI.display_text("sign(-10) = ", Math.sign(-10))
                n += 1
            with switch.case(11):
                pvn.InGameUI.display_text("copy_sign(5, -2) = ", Math.copy_sign(5, -2))
                n += 1
            with switch.case(12):
                pvn.InGameUI.display_text("PI= ", Math.PI, " E= ", Math.E, " TAU= ", Math.TAU)
                n += 1
            with switch.case(13):
                pvn.InGameUI.display_text("sqrt(16) = ", Math.sqrt(16))
                n += 1
            with switch.case(14):
                pvn.InGameUI.display_text("cbrt(8) = ", Math.cbrt(8))
                n += 1
            with switch.case(15):
                pvn.InGameUI.display_text("natural_pow(2, 3) = ", Math.natural_pow(2, 3))
                n += 1
            with switch.case(16):
                pvn.InGameUI.display_text("sqrt(n) = ", Math.sqrt(n))
                n += 1
            with switch.case(17):
                pvn.InGameUI.display_text("is_prime(n) = ", Math.is_prime(n))
                n += 1
            with switch.default:
                pvn.InGameUI.display_text("No more Math examples.")
                n.set(0)

pvn.add_graph(main)