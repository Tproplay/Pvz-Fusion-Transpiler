import PvZ_Fusion_Transpiler as pft

pft.Config(output="./", name="DisplayTextCase")

with pft.Trigger.OnGameStart():
    pft.InGameUI.display_text(5)
