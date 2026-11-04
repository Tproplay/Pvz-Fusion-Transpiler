import unittest
import PvZ_Fusion_Transpiler as pft
from PvZ_Fusion_Transpiler.Types import PlantType, ZombieType


class TestGenericList(unittest.TestCase):
    def setUp(self):
        pft._ctx.clear()

    def test_list_int_operations(self):
        with pft.Trigger.OnBoardStart():
            q = pft.List[pft.Int](name="my_ints")
            q.Add(10)
            q.Add(20)
            q.Insert(1, 15)
            q[0] = 5

            val = q[1]
            self.assertIsNotNone(val)

            val2, ok = q.TryGetValue(2)
            self.assertIsNotNone(val2)
            self.assertIsNotNone(ok)

            idx = q.IndexOf(15)
            self.assertIsNotNone(idx)

            has_15 = q.Contains(15)
            self.assertIsNotNone(has_15)

            idx2, found = q.TryFindIndex(20)
            self.assertIsNotNone(idx2)
            self.assertIsNotNone(found)

            q.RemoveAt(0)
            q.Clear()

            count = q.Count
            self.assertIsNotNone(count)

    def test_list_float_and_bool_and_string(self):
        with pft.Trigger.OnBoardStart():
            f_list = pft.FloatList(name="my_floats")
            f_list.Add(1.5)
            f_list.Insert(0, 0.5)
            f_list[0] = 2.5
            self.assertIsNotNone(f_list[0])
            self.assertIsNotNone(f_list.Contains(1.5))

            b_list = pft.BoolList(name="my_bools")
            b_list.Add(True)
            b_list.Insert(0, False)
            b_list[0] = True
            self.assertIsNotNone(b_list[0])
            self.assertIsNotNone(b_list.Contains(True))

            s_list = pft.StringList(name="my_strings")
            s_list.Add("hello")
            s_list.Insert(0, "start")
            s_list[0] = "world"
            self.assertIsNotNone(s_list[0])
            self.assertIsNotNone(s_list.Contains("hello"))

    def test_list_object_and_plant_type(self):
        with pft.Trigger.OnBoardStart():
            obj_list = pft.ObjectList(name="my_objects")
            obj = pft.WorldObject.create(name="MyObject")
            obj_list.Add(obj)
            self.assertIsNotNone(obj_list[0])

            pt_list = pft.List[PlantType](name="my_plants")
            pt_list.Add(PlantType.Peashooter)
            pt_list.Insert(0, PlantType.SunFlower)
            pt_list[0] = PlantType.WallNut
            self.assertIsNotNone(pt_list[0])
            self.assertIsNotNone(pt_list.Contains(PlantType.Peashooter))

    def test_list_copy_and_clone(self):
        with pft.Trigger.OnBoardStart():
            q1 = pft.List[pft.Int](name="q1")
            q1.Add(100)
            q2 = pft.List[pft.Int](name="q2")
            q1.CopyTo(q2)
            cloned = q1.Clone(name="q1_clone")
            self.assertIsNotNone(cloned)

    def test_list_for_each(self):
        with pft.Trigger.OnBoardStart():
            items = pft.List[pft.Int](name="items")
            items.Add(1)
            items.Add(2)

            with pft.ForEach(items) as item:
                self.assertIsNotNone(item)

    def test_list_context_manager_failed_exit(self):
        with pft.Trigger.OnBoardStart():
            q = pft.List[pft.Int](name="fail_test")
            with q.Add(42) as op:
                with op.Failed:
                    pft.InGameUI.display_text("Failed to add")

    def test_zombie_type_list_extensions(self):
        with pft.Trigger.OnBoardStart():
            zt_list = pft.ZombieTypeList([ZombieType.NormalZombie, ZombieType.FlagZombie])
            zt_list.Add(ZombieType.ConeZombie)
            zt_list.Insert(1, ZombieType.BucketZombie)
            zt_list[0] = ZombieType.Gargantuar

            self.assertIsNotNone(zt_list[0])
            self.assertIsNotNone(zt_list.Contains(ZombieType.Gargantuar))
            zt_list.remove_at(0)
            self.assertIsNotNone(zt_list.count)


if __name__ == "__main__":
    unittest.main()
