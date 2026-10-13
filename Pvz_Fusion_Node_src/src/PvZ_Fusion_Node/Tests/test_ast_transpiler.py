"""
Unit Tests for PvZ Fusion AST Transpiler.
"""

from __future__ import annotations

import unittest
import PvZ_Fusion_Node as pvn
from PvZ_Fusion_Node import (
    Trigger,
    Board,
    Spawner,
    PlantType,
    ZombieType,
    IntVar,
    FloatVar,
    BoolVar,
    ctx,
)
from PvZ_Fusion_Node.AST import (
    transpile_source,
    transpile_to_ast,
    compile_ast,
    compile_level,
)


class TestASTTranspiler(unittest.TestCase):
    def setUp(self):
        ctx.reset()

    def test_transpile_simple_if(self):
        code = """
if Board.Sun < 100:
    Board.Sun += 50
"""
        dsl = transpile_source(code)
        self.assertIn("with pvn.If(Board.Sun < 100):", dsl)
        self.assertIn("Board.Sun += 50", dsl)

    def test_transpile_if_elif_else_chain(self):
        code = """
if wave == 1:
    Board.Sun += 100
elif wave == 2:
    Board.Sun += 200
else:
    Board.Sun += 300
"""
        dsl = transpile_source(code)
        self.assertIn("with pvn.If(wave == 1) as _branch_0:", dsl)
        self.assertIn("with _branch_0.Elif(wave == 2) as _branch_0:", dsl)
        self.assertIn("with _branch_0.Else:", dsl)

    def test_transpile_while_loop(self):
        code = """
while Board.Sun < 500:
    Board.Sun += 50
"""
        dsl = transpile_source(code)
        self.assertIn("with pvn.While(Board.Sun < 500):", dsl)
        self.assertIn("Board.Sun += 50", dsl)

    def test_transpile_for_range(self):
        code = """
for i in range(5):
    Spawner.Set_Plant(row=2, col=i, plant_type=PlantType.Peashooter)
"""
        dsl = transpile_source(code)
        self.assertIn("with pvn.For(5) as _loop_0:", dsl)
        self.assertIn("i = _loop_0.index", dsl)
        self.assertIn("Spawner.Set_Plant", dsl)

    def test_transpile_for_range_with_start_stop(self):
        code = """
for i in range(2, 6):
    Spawner.Set_Plant(row=1, col=i, plant_type=PlantType.WallNut)
"""
        dsl = transpile_source(code)
        self.assertIn("with pvn.For(6 - 2) as _loop_0:", dsl)
        self.assertIn("i = 2 + _loop_0.index", dsl)

    def test_transpile_match_case(self):
        code = """
match plant_type:
    case PlantType.SunFlower:
        Board.Sun += 25
    case PlantType.WallNut:
        Board.Sun += 50
    case _:
        Board.Sun += 10
"""
        dsl = transpile_source(code)
        self.assertIn("with pvn.Switch(plant_type) as _sw_0:", dsl)
        self.assertIn("with _sw_0.case(PlantType.SunFlower):", dsl)
        self.assertIn("with _sw_0.case(PlantType.WallNut):", dsl)
        self.assertIn("with _sw_0.default:", dsl)

    def test_transpile_print(self):
        code = """
print("Wave incoming!", wave)
"""
        dsl = transpile_source(code)
        self.assertIn("pvn.Print('Wave incoming!', wave)", dsl)

    def test_transpile_var_reassignment(self):
        code = """
counter = IntVar(0)
counter = 42
"""
        dsl = transpile_source(code)
        self.assertIn("counter = IntVar(0)", dsl)
        self.assertIn("counter.set(42)", dsl)

    def test_compile_level_decorator(self):
        @compile_level(name="ASTDecoratedLevel")
        def define_level():
            with Trigger.OnGameStart():
                Board.Sun += 100
                for i in range(3):
                    Spawner.Set_Plant(row=0, col=i, plant_type=PlantType.Peashooter)
                if Board.Sun > 50:
                    print("Sun ready!")

        level = define_level()
        level_dict = level.to_dict()

        self.assertEqual(level_dict["name"], "ASTDecoratedLevel")
        self.assertGreater(len(level_dict["eventNodeGraph"]["nodes"]), 3)
        self.assertGreater(len(level_dict["eventNodeGraph"]["connections"]), 2)

    def test_end_to_end_ast_script_compilation(self):
        script = """
with Trigger.OnGameStart():
    Board.Sun += 200
    for col in range(5):
        Spawner.Set_Plant(row=2, col=col, plant_type=PlantType.SunFlower)

    if Board.Sun >= 200:
        print("Rich on start!")
    else:
        print("Standard start.")
"""
        level = compile_ast(script)
        level_dict = level.to_dict()

        self.assertIn("eventNodeGraph", level_dict)
        self.assertGreater(len(level_dict["eventNodeGraph"]["nodes"]), 5)
        self.assertGreater(len(level_dict["eventNodeGraph"]["connections"]), 3)


if __name__ == "__main__":
    unittest.main()
