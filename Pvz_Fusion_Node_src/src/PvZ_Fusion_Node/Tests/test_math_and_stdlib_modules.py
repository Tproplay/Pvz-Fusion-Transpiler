import unittest
import math
import PvZ_Fusion_Node as pvn
from PvZ_Fusion_Node.Math import (
    PI,
    HALF_PI,
    TWO_PI,
    TAU,
    E,
    SQRT2,
    DEG2RAD,
    RAD2DEG,
    EPSILON,
    pow as math_pow,
    sqrt,
    cbrt,
    hypot,
    log,
    log2,
    log10,
    exp,
    abs as math_abs,
    sign,
    round as math_round,
    floor,
    ceil,
    clamp,
    clamp01,
    min as math_min,
    max as math_max,
    lerp,
    lerp_unclamped,
    mod,
    copy_sign,
    is_prime,
    gcd,
    lcm,
    rad2deg,
    deg2rad,
    normalize_angle_360,
    normalize_angle_180,
    delta_angle,
    sin,
    cos,
    tan,
    sincos,
    atan2,
    inverse_lerp,
    remap,
    smoothstep,
    smootherstep,
    pingpong,
    repeat,
    Vector2,
    distance,
    dot,
    cross,
    reflect,
)
from PvZ_Fusion_Node.StdLib import (
    format_string,
    ZombieTypeList,
    Dictionary,
    Array,
    Counter,
    StatManager,
    PlantStatsManager,
    StatPreset,
    int_to_float,
    float_to_int,
    int_to_string,
    string_to_int,
)
from PvZ_Fusion_Node.TypeMgr import PlantType, ZombieType, KeyCode


class TestMathAndStdLibModules(unittest.TestCase):
    def setUp(self):
        pvn.ctx.reset()

    def test_imports_direct_from_package(self):
        # Ensure direct imports from TypeMgr work
        self.assertEqual(PlantType.Peashooter.value, 0)
        self.assertEqual(KeyCode.W.value, 119)

    def test_math_constants(self):
        self.assertAlmostEqual(PI, math.pi)
        self.assertAlmostEqual(HALF_PI, math.pi / 2.0)
        self.assertAlmostEqual(TWO_PI, math.pi * 2.0)
        self.assertAlmostEqual(TAU, math.tau)
        self.assertAlmostEqual(E, math.e)
        self.assertAlmostEqual(SQRT2, math.sqrt(2.0))
        self.assertAlmostEqual(DEG2RAD, math.pi / 180.0)
        self.assertAlmostEqual(RAD2DEG, 180.0 / math.pi)

    def test_powers_and_roots(self):
        self.assertEqual(math_pow(2, 3), 8)
        self.assertEqual(sqrt(16), 4)
        self.assertAlmostEqual(cbrt(27), 3.0)
        self.assertAlmostEqual(hypot(3, 4), 5.0)
        self.assertAlmostEqual(log(E), 1.0)
        self.assertAlmostEqual(log2(8), 3.0)
        self.assertAlmostEqual(log10(100), 2.0)
        self.assertAlmostEqual(exp(1), E)

    def test_arithmetic_and_number_theory(self):
        self.assertEqual(math_abs(-5), 5)
        self.assertEqual(sign(-10), -1)
        self.assertEqual(sign(10), 1)
        self.assertEqual(sign(0), 0)
        self.assertEqual(math_round(3.6), 4)
        self.assertEqual(floor(3.9), 3)
        self.assertEqual(ceil(3.1), 4)
        self.assertEqual(clamp(15, 0, 10), 10)
        self.assertEqual(clamp(-5, 0, 10), 0)
        self.assertEqual(clamp01(1.5), 1.0)
        self.assertEqual(clamp01(-0.5), 0.0)
        self.assertEqual(math_min(3, 7, 2, 9), 2)
        self.assertEqual(math_max(3, 7, 2, 9), 9)
        self.assertEqual(lerp(0, 10, 0.5), 5.0)
        self.assertEqual(lerp(0, 10, 1.5), 10.0)  # clamped
        self.assertEqual(lerp_unclamped(0, 10, 1.5), 15.0)
        self.assertEqual(mod(10, 3), 1)
        self.assertEqual(copy_sign(5, -1), -5.0)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(lcm(12, 18), 36)

    def test_trigonometry(self):
        self.assertAlmostEqual(deg2rad(180), PI)
        self.assertAlmostEqual(rad2deg(PI), 180.0)
        self.assertAlmostEqual(normalize_angle_360(400), 40.0)
        self.assertAlmostEqual(normalize_angle_180(270), -90.0)
        self.assertAlmostEqual(delta_angle(10, 20), 10.0)
        self.assertAlmostEqual(sin(0), 0.0)
        self.assertAlmostEqual(cos(0), 1.0)
        self.assertAlmostEqual(tan(0), 0.0)
        s, c = sincos(0)
        self.assertAlmostEqual(s, 0.0)
        self.assertAlmostEqual(c, 1.0)
        self.assertAlmostEqual(atan2(0, 1), 0.0)

    def test_interpolation(self):
        self.assertAlmostEqual(inverse_lerp(0, 100, 50), 0.5)
        self.assertAlmostEqual(remap(0, 10, 0, 100, 5), 50.0)
        self.assertAlmostEqual(smoothstep(0, 1, 0.5), 0.5)
        self.assertAlmostEqual(smootherstep(0, 1, 0.5), 0.5)
        self.assertAlmostEqual(pingpong(1.5, 1.0), 0.5)
        self.assertAlmostEqual(repeat(3.5, 2.0), 1.5)

    def test_vector2(self):
        v1 = Vector2(3, 4)
        v2 = Vector2(1, 2)
        v_sum = v1 + v2
        self.assertEqual((v_sum.x, v_sum.y), (4, 6))
        v_sub = v1 - v2
        self.assertEqual((v_sub.x, v_sub.y), (2, 2))
        v_mul = v1 * 2
        self.assertEqual((v_mul.x, v_mul.y), (6, 8))
        v_div = v1 / 2
        self.assertEqual((v_div.x, v_div.y), (1.5, 2.0))
        self.assertEqual(v1.sqr_magnitude(), 25)
        self.assertEqual(v1.magnitude(), 5.0)
        self.assertEqual(Vector2.dot(v1, v2), 3 * 1 + 4 * 2)
        self.assertEqual(Vector2.cross(v1, v2), 3 * 2 - 4 * 1)
        self.assertAlmostEqual(distance(v1, v2), math.hypot(2, 2))

    def test_stdlib_collections_and_formatting(self):
        with pvn.Trigger.OnGameStart():
            # Test format_string with static strings and numbers
            txt = format_string("Hello ", 123, " World")
            self.assertIsNotNone(txt)

            # Test ZombieTypeList
            z_list = ZombieTypeList([ZombieType.NormalZombie, ZombieType.ConeZombie])
            self.assertEqual(len(z_list._items), 2)
            z_list.add(ZombieType.PolevaulterZombie)
            self.assertEqual(len(z_list._items), 3)

            # Test StatManager & PlantStatsManager
            sm = StatManager()
            sm.create_tag("Shooters", [PlantType.Peashooter, PlantType.CherryBomb])
            sm.add_tag_atk("Shooters", 1.5)
            self.assertIn("Shooters", sm.tags)

            psm = PlantStatsManager()
            self.assertIsInstance(psm, StatManager)
            self.assertEqual(StatPreset.TANK_HP, 3.0)


if __name__ == "__main__":
    unittest.main()
