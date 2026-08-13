import PvzRH_node as pvn
from PvzRH_node import Mathf

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
                pvn.InGameUI.display_text("abs(-5) = ", Mathf.abs(-5))
                n += 1
            with switch.case(1):
                pvn.InGameUI.display_text("ceil(3.2) = ", Mathf.ceil(3.2))
                n += 1
            with switch.case(2):
                pvn.InGameUI.display_text("floor(3.8) = ", Mathf.floor(3.8))
                n += 1
            with switch.case(3):
                pvn.InGameUI.display_text("round(3.5) = ", Mathf.round(3.5))
                n += 1
            with switch.case(4):
                pvn.InGameUI.display_text("max(1, 5) = ", Mathf.max(1, 5))
                n += 1
            with switch.case(5):
                pvn.InGameUI.display_text("min(-1, -5) = ", Mathf.min(-1, -5))
                n += 1
            with switch.case(6):
                pvn.InGameUI.display_text("clamp(5, 1, 10) = ", Mathf.clamp(5, 1, 10))
                n += 1
            with switch.case(7):
                pvn.InGameUI.display_text("clamp01(15) = ", Mathf.clamp01(15))
                n += 1
            with switch.case(8):
                pvn.InGameUI.display_text("lerp(0, 10, 0.5) = ", Mathf.lerp(0, 10, 0.5))
                n += 1
            with switch.case(9):
                pvn.InGameUI.display_text("lerp_unclamped(0, 10, 1.5) = ", Mathf.lerp_unclamped(0, 10, 1.5))
                n += 1
            with switch.case(10):
                pvn.InGameUI.display_text("sign(-10) = ", Mathf.sign(-10))
                n += 1
            with switch.case(11):
                pvn.InGameUI.display_text("copy_sign(5, -2) = ", Mathf.copy_sign(5, -2))
                n += 1
            with switch.case(12):
                pvn.InGameUI.display_text("PI= ", Mathf.PI, " E= ", Mathf.E, " TAU= ", Mathf.TAU)
                n += 1
            with switch.case(13):
                pvn.InGameUI.display_text("sqrt(16) = ", Mathf.sqrt(16))
                n += 1
            with switch.case(14):
                pvn.InGameUI.display_text("cbrt(8) = ", Mathf.cbrt(8))
                n += 1
            with switch.case(15):
                pvn.InGameUI.display_text("natural_pow(2, 3) = ", Mathf.natural_pow(2, 3))
                n += 1
            with switch.case(16):
                pvn.InGameUI.display_text("sqrt(n) = ", Mathf.sqrt(n))
                n += 1
            with switch.case(17):
                pvn.InGameUI.display_text("is_prime(n) = ", Mathf.is_prime(n))
                n += 1
            with switch.default:
                pvn.InGameUI.display_text("No more Mathf examples.")
                n.set(0)

pvn.add_graph(main)