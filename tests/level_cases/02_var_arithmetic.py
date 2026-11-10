import PvZ_Fusion_Transpiler as pft

pft.Config(output="./", name="VarArithmeticCase")

a = pft.IntVar(10)
a = a * 5
a = a / 2.0
