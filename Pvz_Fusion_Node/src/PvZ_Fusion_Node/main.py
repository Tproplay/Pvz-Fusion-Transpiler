"""
PvZ Fusion / PvzRH Visual Script Transpiler CLI & Demo Runner.
"""

import argparse
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from Core import Compiler, Level
from Nodes.Original.Trigger import OnGameStartNode, OnWaveClearedNode
from Nodes.Original.PlantFunction import SetPlantNode
from Nodes.Original.ZombieFunction import CreateZombieNode, DamageZombieNode
from Nodes.Original.GeneralFunction import ShowTextNode
from Nodes.Extentions.Variables import IntVar


def run_demo(output_file: str = "output_level.json"):
    print("[Transpiler] Building sample PvZ Fusion level...")

    # 1. Initialize Level
    level = Level(
        name="TranspilerDemoStage",
        level_number=9998,
        level_type=11,
        start_sun=1000,
        max_wave=15,
        card_count=14,
    )

    # 2. Board Configuration & Game Mode Flags
    level.boardConfig.zombieHealthMultiplier = 1.2
    level.boardConfig.waveInterval = 25.0
    level.boardTag.enable_endless()

    # 3. God Shooting Characters
    level.godShootingConfig.add_plant(
        plant_type=0, column=2, row=2, health=600.0, attack=35.0, is_player=True
    )

    # 4. Reactive Canvas Variables
    counter = level.add_node(IntVar(name="WaveCount", start_val=0))

    # 5. Visual Nodes Logic
    on_start = level.add_node(OnGameStartNode())
    banner = level.add_node(ShowTextNode(display_text="关卡开始！", duration=3.0))
    spawn_plant = level.add_node(SetPlantNode())
    spawn_zombie = level.add_node(CreateZombieNode())

    on_wave_clear = level.add_node(OnWaveClearedNode())
    zombie_damage = level.add_node(DamageZombieNode())

    # 6. Graph Connections (Execution Flow)
    level.connect(on_start, "触发", banner, "触发")
    level.connect(banner, "完成", spawn_plant, "触发")
    level.connect(spawn_plant, "创建成功", spawn_zombie, "触发")
    level.connect(on_wave_clear, "触发", zombie_damage, "触发")

    # 7. Compile & Auto-Layout
    compiler = Compiler(auto_layout=True, optimize=True)
    out_path = compiler.compile_to_file(level, output_file)

    print(f"[Transpiler] Level successfully compiled to: {out_path}")
    print(f"             Total Nodes in Graph: {len(level.graph.nodes)}")
    print(f"             Total Connections:    {len(level.graph.connections)}")
    print(f"             Total References:     {len(level.registry._registered_items)}")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="PvZ Fusion Visual Node Transpiler")
    subparsers = parser.add_subparsers(dest="command")

    # Demo
    demo_parser = subparsers.add_parser("demo", help="Generate a demo level JSON")
    demo_parser.add_argument("-o", "--output", default="output_level.json", help="Output path")

    # Test
    test_parser = subparsers.add_parser("test", help="Run automated test suite")

    # Decompile / Inspect
    dec_parser = subparsers.add_parser("inspect", help="Inspect an existing level JSON")
    dec_parser.add_argument("file", help="Path to level JSON file")

    args = parser.parse_args()

    if args.command == "inspect":
        if not os.path.exists(args.file):
            print(f"File not found: {args.file}")
            sys.exit(1)
        lvl = Compiler.decompile(args.file)
        print(f"Level Name:      {lvl.name}")
        print(f"Starting Sun:    {lvl.startSun}")
        print(f"Total Nodes:     {len(lvl.graph.nodes)}")
        print(f"Total Wires:     {len(lvl.graph.connections)}")
    elif args.command == "test":
        import unittest
        from Tests.test_sample import TestLevelCompiler
        suite = unittest.TestLoader().loadTestsFromTestCase(TestLevelCompiler)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    else:
        out = getattr(args, "output", "output_level.json")
        run_demo(out)


if __name__ == "__main__":
    main()
