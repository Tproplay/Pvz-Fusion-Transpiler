# Auto-generated helper methods with default parameter values for IDE tooltips.
from typing import Dict, Any

class PlantDataMethodsMixin:
    @classmethod
    def Peashooter(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Peashooter (0)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(0, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunFlower(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SunFlower (1)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryBomb(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryBomb (2)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(2, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WallNut(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WallNut (3)
        Defaults: Cost=50 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(3, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoMine(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoMine (4)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(4, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Chomper(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Chomper (5)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(5, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SmallPuff(
        cls,
        cost: int = 0,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SmallPuff (6)
        Defaults: Cost=0 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(6, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FumeShroom(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FumeShroom (7)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(7, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoShroom(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoShroom (8)
        Defaults: Cost=75 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(8, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyShroom(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyShroom (9)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(9, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceShroom(
        cls,
        cost: int = 75,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceShroom (10)
        Defaults: Cost=75 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(10, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomShroom(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomShroom (11)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(11, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LilyPad(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LilyPad (12)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(12, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Squash(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Squash (13)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(13, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreePeater(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreePeater (14)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(14, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tanglekelp(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tanglekelp (15)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(15, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Jalapeno(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Jalapeno (16)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(16, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Caltrop(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Caltrop (17)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(17, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchWood(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchWood (18)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(18, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaShroom(
        cls,
        cost: int = 0,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaShroom (19)
        Defaults: Cost=0 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(19, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Plantern(
        cls,
        cost: int = 25,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Plantern (20)
        Defaults: Cost=25 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(20, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Cactus(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Cactus (21)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(21, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Blover(
        cls,
        cost: int = 100,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Blover (22)
        Defaults: Cost=100 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(22, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarFruit(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarFruit (23)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(23, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Pumpkin(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Pumpkin (24)
        Defaults: Cost=125 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(24, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Magnetshroom(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Magnetshroom (25)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(25, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Cabbagepult(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Cabbagepult (26)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(26, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Pot(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Pot (27)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(27, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Cornpult(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Cornpult (28)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(28, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Garlic(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Garlic (29)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(29, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Umbrellaleaf(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Umbrellaleaf (30)
        Defaults: Cost=100 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(30, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Marigold(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.Marigold (31)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(31, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Melonpult(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Melonpult (32)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(32, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Shulkflower(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 8,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Shulkflower (33)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=8 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(33, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ElectricOnion(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ElectricOnion (34)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=100 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(34, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PineFurnace(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PineFurnace (35)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(35, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SpruceShooter(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SpruceShooter (36)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(36, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceLotus(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceLotus (37)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(37, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WaterAloes(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WaterAloes (38)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(38, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Bamboo(
        cls,
        cost: int = 50,
        cd: float = 15.0,
        max_health: int = 1500,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Bamboo (39)
        Defaults: Cost=50 | CD=15.0s | HP=1500 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(39, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Thorns(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Thorns (40)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(40, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HolographicPlant(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HolographicPlant (217)
        Defaults: Cost=50 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(217, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Pudding(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Pudding (218)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(218, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def VectorPlant(
        cls,
        cost: int = 0,
        cd: float = 0.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.VectorPlant (219)
        Defaults: Cost=0 | CD=0.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(219, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldScaryPot(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldScaryPot (220)
        Defaults: Cost=200 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(220, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MixAnim(
        cls,
        cost: int = 0,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MixAnim (221)
        Defaults: Cost=0 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(221, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Firecracker(
        cls,
        cost: int = 275,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Firecracker (222)
        Defaults: Cost=275 | CD=50.0s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(222, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Apple(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Apple (223)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(223, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BucketPlant(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 2000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BucketPlant (224)
        Defaults: Cost=100 | CD=30.0s | HP=2000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(224, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HelmetPlant(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HelmetPlant (225)
        Defaults: Cost=200 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(225, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def XXSPot(
        cls,
        cost: int = 75,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.XXSPot (226)
        Defaults: Cost=75 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(226, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DiamondImitater(
        cls,
        cost: int = 25,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DiamondImitater (227)
        Defaults: Cost=25 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(227, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ZombieEndoFlame(
        cls,
        cost: int = -125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ZombieEndoFlame (228)
        Defaults: Cost=-125 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(228, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LuckyBlover(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LuckyBlover (229)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(229, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireSunshroom_a(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.FireSunshroom_a (230)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(230, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireSunshroom_b(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.FireSunshroom_b (231)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(231, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireSunshroom_c(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.FireSunshroom_c (232)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(232, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SnowPresent(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SnowPresent (233)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(233, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DiamondPotatoNut(
        cls,
        cost: int = 400,
        cd: float = 90.0,
        max_health: int = 32000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DiamondPotatoNut (234)
        Defaults: Cost=400 | CD=90.0s | HP=32000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(234, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PassionFruit(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PassionFruit (235)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(235, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FrozenPear(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FrozenPear (236)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(236, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IcePeach(
        cls,
        cost: int = 325,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IcePeach (237)
        Defaults: Cost=325 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(237, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Chrysantheautumn(
        cls,
        cost: int = 100,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Chrysantheautumn (238)
        Defaults: Cost=100 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(238, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Gravebuster(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Gravebuster (239)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(239, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ObsidianWheat(
        cls,
        cost: int = 500,
        cd: float = 70.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ObsidianWheat (240)
        Defaults: Cost=500 | CD=70.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(240, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceBean(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceBean (241)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(241, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def EndoFlameGirl(
        cls,
        cost: int = 200,
        cd: float = 90.0,
        max_health: int = 1000,
        attack_damage: int = 50,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.EndoFlameGirl (242)
        Defaults: Cost=200 | CD=90.0s | HP=1000 | DMG=50 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(242, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Hamburger(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 1000,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.Hamburger (243)
        Defaults: Cost=125 | CD=30.0s | HP=1000 | DMG=20 | AtkInt=3.0s | ProdInt=25.0s
        """
        return cls.create(243, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MixBomb(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MixBomb (244)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(244, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Imitater(
        cls,
        cost: int = 100,
        cd: float = 300.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Imitater (245)
        Defaults: Cost=100 | CD=300.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(245, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetBox(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetBox (246)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(246, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetInterface(
        cls,
        cost: int = 0,
        cd: float = 3.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetInterface (247)
        Defaults: Cost=0 | CD=3.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(247, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Squalour(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Squalour (248)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(248, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SwordStar(
        cls,
        cost: int = 325,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 200,
        attack_interval: float = 6.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SwordStar (249)
        Defaults: Cost=325 | CD=30.0s | HP=300 | DMG=200 | AtkInt=6.0s | ProdInt=0.0s
        """
        return cls.create(249, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PresentZombie(
        cls,
        cost: int = -100,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PresentZombie (250)
        Defaults: Cost=-100 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(250, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigSunNut(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BigSunNut (251)
        Defaults: Cost=100 | CD=30.0s | HP=4000 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(251, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CattailGirl(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CattailGirl (252)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(252, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Wheat(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Wheat (253)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(253, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def EndoFlame(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.EndoFlame (254)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(254, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigWallNut(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BigWallNut (255)
        Defaults: Cost=100 | CD=30.0s | HP=4000 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(255, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Present(
        cls,
        cost: int = 100,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Present (256)
        Defaults: Cost=100 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(256, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def AbyssSwordStar(
        cls,
        cost: int = 750,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 6.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.AbyssSwordStar (300)
        Defaults: Cost=750 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=6.0s | ProdInt=0.0s
        """
        return cls.create(300, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateMinigun(
        cls,
        cost: int = 1000,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateMinigun (301)
        Defaults: Cost=1000 | CD=90.0s | HP=300 | DMG=300 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(301, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateRedLunar(
        cls,
        cost: int = 850,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateRedLunar (302)
        Defaults: Cost=850 | CD=50.0s | HP=300 | DMG=300 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(302, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ImitateWheat(
        cls,
        cost: int = 500,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ImitateWheat (303)
        Defaults: Cost=500 | CD=90.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(303, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SolarSunflower(
        cls,
        cost: int = 800,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 3.0,
    ) -> Dict[str, Any]:
        """PlantType.SolarSunflower (304)
        Defaults: Cost=800 | CD=90.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=3.0s
        """
        return cls.create(304, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateHypnoDoom(
        cls,
        cost: int = 1500,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateHypnoDoom (305)
        Defaults: Cost=1500 | CD=90.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(305, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimatePoisonFume(
        cls,
        cost: int = 850,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimatePoisonFume (306)
        Defaults: Cost=850 | CD=90.0s | HP=300 | DMG=20 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(306, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def AcientSunNut(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.AcientSunNut (307)
        Defaults: Cost=150 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(307, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BedRockTallNut(
        cls,
        cost: int = 900,
        cd: float = 90.0,
        max_health: int = 640000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BedRockTallNut (308)
        Defaults: Cost=900 | CD=90.0s | HP=640000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(308, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSniperGatling(
        cls,
        cost: int = 800,
        cd: float = 90.0,
        max_health: int = 8000,
        attack_damage: int = 1800,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSniperGatling (309)
        Defaults: Cost=800 | CD=90.0s | HP=8000 | DMG=1800 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(309, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_peasunflower(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_peasunflower (350)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(350, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_BigSunShroom(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 20.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_BigSunShroom (351)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=0 | AtkInt=20.0s | ProdInt=0.0s
        """
        return cls.create(351, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_cherryShooter(
        cls,
        cost: int = 400,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_cherryShooter (352)
        Defaults: Cost=400 | CD=50.0s | HP=300 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(352, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_starNut(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 10,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_starNut (353)
        Defaults: Cost=200 | CD=30.0s | HP=4000 | DMG=10 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(353, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_sunmine(
        cls,
        cost: int = 25,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1000,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_sunmine (354)
        Defaults: Cost=25 | CD=50.0s | HP=300 | DMG=1000 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(354, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_iceGloom(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 5,
        attack_interval: float = 3.8,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_iceGloom (355)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=5 | AtkInt=3.8s | ProdInt=0.0s
        """
        return cls.create(355, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_cherryChomper(
        cls,
        cost: int = 500,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1000,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_cherryChomper (356)
        Defaults: Cost=500 | CD=50.0s | HP=300 | DMG=1000 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(356, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_electricOnion(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_electricOnion (357)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(357, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_peaPuff(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 10,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_peaPuff (358)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=10 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(358, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_sunShroom(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 25.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_sunShroom (359)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=25.0s | ProdInt=0.0s
        """
        return cls.create(359, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_doomFume(
        cls,
        cost: int = 500,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1000,
        attack_interval: float = 60.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_doomFume (360)
        Defaults: Cost=500 | CD=50.0s | HP=300 | DMG=1000 | AtkInt=60.0s | ProdInt=0.0s
        """
        return cls.create(360, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_gravebuster(
        cls,
        cost: int = 0,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_gravebuster (361)
        Defaults: Cost=0 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(361, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_scaredyfume(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_scaredyfume (362)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(362, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_iceblover(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_iceblover (363)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=1 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(363, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_doomStar(
        cls,
        cost: int = 175,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1000,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_doomStar (364)
        Defaults: Cost=175 | CD=90.0s | HP=300 | DMG=1000 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(364, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_waterCan(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_waterCan (365)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(365, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_lilyPad(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_lilyPad (366)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(366, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_squashNut(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 1000,
        attack_damage: int = 80,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_squashNut (367)
        Defaults: Cost=75 | CD=30.0s | HP=1000 | DMG=80 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(367, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Tower_threeMine(
        cls,
        cost: int = 400,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Tower_threeMine (368)
        Defaults: Cost=400 | CD=30.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(368, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoEmperor(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoEmperor (900)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(900, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateGatling(
        cls,
        cost: int = 950,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateGatling (901)
        Defaults: Cost=950 | CD=90.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(901, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateTorch(
        cls,
        cost: int = 600,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateTorch (902)
        Defaults: Cost=600 | CD=90.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(902, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateChomper(
        cls,
        cost: int = 600,
        cd: float = 90.0,
        max_health: int = 8000,
        attack_damage: int = 1000,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateChomper (903)
        Defaults: Cost=600 | CD=90.0s | HP=8000 | DMG=1000 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(903, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateFume(
        cls,
        cost: int = 425,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateFume (904)
        Defaults: Cost=425 | CD=90.0s | HP=300 | DMG=100 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(904, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperSunNut(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperSunNut (905)
        Defaults: Cost=150 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(905, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ObsidianSpike(
        cls,
        cost: int = 650,
        cd: float = 50.0,
        max_health: int = 8000,
        attack_damage: int = 300,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ObsidianSpike (906)
        Defaults: Cost=650 | CD=50.0s | HP=8000 | DMG=300 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(906, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomGatling(
        cls,
        cost: int = 525,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomGatling (907)
        Defaults: Cost=525 | CD=50.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(907, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SnowGatlingPuff(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SnowGatlingPuff (908)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(908, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateStar(
        cls,
        cost: int = 450,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateStar (909)
        Defaults: Cost=450 | CD=90.0s | HP=300 | DMG=30 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(909, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateGloom(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 1.9,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateGloom (910)
        Defaults: Cost=525 | CD=90.0s | HP=300 | DMG=100 | AtkInt=1.9s | ProdInt=0.0s
        """
        return cls.create(910, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimatePumpkin(
        cls,
        cost: int = 525,
        cd: float = 50.0,
        max_health: int = 16000,
        attack_damage: int = 200,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimatePumpkin (911)
        Defaults: Cost=525 | CD=50.0s | HP=16000 | DMG=200 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(911, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateFly(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 200,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateFly (912)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=200 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(912, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateTallNut(
        cls,
        cost: int = 450,
        cd: float = 90.0,
        max_health: int = 32000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateTallNut (913)
        Defaults: Cost=450 | CD=90.0s | HP=32000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(913, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateMelon(
        cls,
        cost: int = 900,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateMelon (914)
        Defaults: Cost=900 | CD=90.0s | HP=300 | DMG=120 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(914, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateCannon(
        cls,
        cost: int = 575,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 35.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateCannon (915)
        Defaults: Cost=575 | CD=90.0s | HP=300 | DMG=1800 | AtkInt=35.0s | ProdInt=0.0s
        """
        return cls.create(915, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def EmeraldUmbrella(
        cls,
        cost: int = 475,
        cd: float = 90.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.EmeraldUmbrella (916)
        Defaults: Cost=475 | CD=90.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(916, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoQueen(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoQueen (917)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(917, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def AshThreePeater(
        cls,
        cost: int = 400,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.AshThreePeater (918)
        Defaults: Cost=400 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(918, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperThreePeater(
        cls,
        cost: int = 650,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 160,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperThreePeater (919)
        Defaults: Cost=650 | CD=90.0s | HP=300 | DMG=160 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(919, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateBlover(
        cls,
        cost: int = 450,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateBlover (920)
        Defaults: Cost=450 | CD=90.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(920, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicUltimateChomper(
        cls,
        cost: int = 600,
        cd: float = 90.0,
        max_health: int = 8000,
        attack_damage: int = 1000,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicUltimateChomper (921)
        Defaults: Cost=600 | CD=90.0s | HP=8000 | DMG=1000 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(921, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryUltimatePumpkin(
        cls,
        cost: int = 525,
        cd: float = 50.0,
        max_health: int = 16000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryUltimatePumpkin (922)
        Defaults: Cost=525 | CD=50.0s | HP=16000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(922, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def RedEmeraldUmbrella(
        cls,
        cost: int = 475,
        cd: float = 90.0,
        max_health: int = 4000,
        attack_damage: int = 80,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.RedEmeraldUmbrella (923)
        Defaults: Cost=475 | CD=90.0s | HP=4000 | DMG=80 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(923, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateHypno(
        cls,
        cost: int = 350,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateHypno (924)
        Defaults: Cost=350 | CD=90.0s | HP=300 | DMG=120 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(924, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimatePotatoNut(
        cls,
        cost: int = 350,
        cd: float = 90.0,
        max_health: int = 32000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimatePotatoNut (925)
        Defaults: Cost=350 | CD=90.0s | HP=32000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(925, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CattailLour(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 160,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CattailLour (926)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=160 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(926, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateBigGatling(
        cls,
        cost: int = 1000,
        cd: float = 90.0,
        max_health: int = 8000,
        attack_damage: int = 80,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateBigGatling (927)
        Defaults: Cost=1000 | CD=90.0s | HP=8000 | DMG=80 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(927, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperHypnoDoom(
        cls,
        cost: int = 325,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperHypnoDoom (928)
        Defaults: Cost=325 | CD=90.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(928, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunGatlingPuff(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunGatlingPuff (929)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(929, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GatlingDoomScaredy(
        cls,
        cost: int = 525,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GatlingDoomScaredy (930)
        Defaults: Cost=525 | CD=50.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(930, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ObsidianWallNut(
        cls,
        cost: int = 450,
        cd: float = 50.0,
        max_health: int = 16000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ObsidianWallNut (931)
        Defaults: Cost=450 | CD=50.0s | HP=16000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(931, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldThreeTorch(
        cls,
        cost: int = 575,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldThreeTorch (932)
        Defaults: Cost=575 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(932, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateCactus(
        cls,
        cost: int = 425,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateCactus (933)
        Defaults: Cost=425 | CD=90.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(933, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateCabbage(
        cls,
        cost: int = 375,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateCabbage (934)
        Defaults: Cost=375 | CD=50.0s | HP=300 | DMG=300 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(934, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IFVPumpkin(
        cls,
        cost: int = 325,
        cd: float = 50.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IFVPumpkin (935)
        Defaults: Cost=325 | CD=50.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(935, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SolarPot(
        cls,
        cost: int = 500,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 15.0,
    ) -> Dict[str, Any]:
        """PlantType.SolarPot (936)
        Defaults: Cost=500 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=15.0s
        """
        return cls.create(936, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LaserUmbrella(
        cls,
        cost: int = 275,
        cd: float = 50.0,
        max_health: int = 1000,
        attack_damage: int = 300,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LaserUmbrella (937)
        Defaults: Cost=275 | CD=50.0s | HP=1000 | DMG=300 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(937, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldHypnoDoom(
        cls,
        cost: int = 325,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldHypnoDoom (938)
        Defaults: Cost=325 | CD=90.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(938, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateGatlingBlover(
        cls,
        cost: int = 950,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateGatlingBlover (939)
        Defaults: Cost=950 | CD=90.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(939, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSpring(
        cls,
        cost: int = 500,
        cd: float = 90.0,
        max_health: int = 3000,
        attack_damage: int = 300,
        attack_interval: float = 6.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSpring (940)
        Defaults: Cost=500 | CD=90.0s | HP=3000 | DMG=300 | AtkInt=6.0s | ProdInt=0.0s
        """
        return cls.create(940, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateKelp(
        cls,
        cost: int = 400,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 5.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateKelp (941)
        Defaults: Cost=400 | CD=90.0s | HP=300 | DMG=40 | AtkInt=5.0s | ProdInt=0.0s
        """
        return cls.create(941, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IFVIronPuff(
        cls,
        cost: int = 475,
        cd: float = 50.0,
        max_health: int = 6000,
        attack_damage: int = 80,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IFVIronPuff (942)
        Defaults: Cost=475 | CD=50.0s | HP=6000 | DMG=80 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(942, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateCorn(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateCorn (943)
        Defaults: Cost=525 | CD=90.0s | HP=300 | DMG=300 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(943, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateMagnet(
        cls,
        cost: int = 375,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateMagnet (944)
        Defaults: Cost=375 | CD=50.0s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(944, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimatePortalNut(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 16000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimatePortalNut (945)
        Defaults: Cost=525 | CD=90.0s | HP=16000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(945, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateBigSniper(
        cls,
        cost: int = 1000,
        cd: float = 90.0,
        max_health: int = 8000,
        attack_damage: int = 300,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateBigSniper (946)
        Defaults: Cost=1000 | CD=90.0s | HP=8000 | DMG=300 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(946, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSpruce(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSpruce (947)
        Defaults: Cost=525 | CD=90.0s | HP=300 | DMG=60 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(947, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateStarTorch(
        cls,
        cost: int = 600,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateStarTorch (948)
        Defaults: Cost=600 | CD=90.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(948, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimatePlantern(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimatePlantern (949)
        Defaults: Cost=525 | CD=90.0s | HP=300 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(949, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SolarLily(
        cls,
        cost: int = 500,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 15.0,
    ) -> Dict[str, Any]:
        """PlantType.SolarLily (950)
        Defaults: Cost=500 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=15.0s
        """
        return cls.create(950, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateBigChomper(
        cls,
        cost: int = 625,
        cd: float = 7.5,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateBigChomper (951)
        Defaults: Cost=625 | CD=7.5s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(951, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateMelonPuff(
        cls,
        cost: int = 900,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateMelonPuff (952)
        Defaults: Cost=900 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(952, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateExplodeCannon(
        cls,
        cost: int = 700,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 3600,
        attack_interval: float = 35.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateExplodeCannon (953)
        Defaults: Cost=700 | CD=90.0s | HP=300 | DMG=3600 | AtkInt=35.0s | ProdInt=0.0s
        """
        return cls.create(953, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSunflower(
        cls,
        cost: int = 350,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 3.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSunflower (954)
        Defaults: Cost=350 | CD=90.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=3.0s
        """
        return cls.create(954, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateLunarCabbage(
        cls,
        cost: int = 375,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateLunarCabbage (955)
        Defaults: Cost=375 | CD=50.0s | HP=300 | DMG=300 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(955, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DeathChomper(
        cls,
        cost: int = 425,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DeathChomper (956)
        Defaults: Cost=425 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(956, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateWinterMelon(
        cls,
        cost: int = 875,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateWinterMelon (957)
        Defaults: Cost=875 | CD=90.0s | HP=300 | DMG=300 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(957, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateCattail(
        cls,
        cost: int = 500,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateCattail (958)
        Defaults: Cost=500 | CD=90.0s | HP=300 | DMG=300 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(958, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NuclearDoomCherry(
        cls,
        cost: int = 425,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 3600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NuclearDoomCherry (959)
        Defaults: Cost=425 | CD=90.0s | HP=300 | DMG=3600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(959, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSeaShroom(
        cls,
        cost: int = 150,
        cd: float = 90.0,
        max_health: int = 8000,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSeaShroom (960)
        Defaults: Cost=150 | CD=90.0s | HP=8000 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(960, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IFVBlover(
        cls,
        cost: int = 475,
        cd: float = 50.0,
        max_health: int = 6000,
        attack_damage: int = 80,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IFVBlover (961)
        Defaults: Cost=475 | CD=50.0s | HP=6000 | DMG=80 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(961, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FlyingThreePeater(
        cls,
        cost: int = 650,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 160,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FlyingThreePeater (962)
        Defaults: Cost=650 | CD=90.0s | HP=300 | DMG=160 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(962, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSunNut(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSunNut (963)
        Defaults: Cost=200 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(963, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateMelonCannon(
        cls,
        cost: int = 575,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 35.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateMelonCannon (964)
        Defaults: Cost=575 | CD=90.0s | HP=300 | DMG=1800 | AtkInt=35.0s | ProdInt=0.0s
        """
        return cls.create(964, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NuclearSquash(
        cls,
        cost: int = 425,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 3600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NuclearSquash (965)
        Defaults: Cost=425 | CD=90.0s | HP=300 | DMG=3600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(965, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateCabbageCannon(
        cls,
        cost: int = 700,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.75,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateCabbageCannon (966)
        Defaults: Cost=700 | CD=90.0s | HP=300 | DMG=300 | AtkInt=0.75s | ProdInt=0.0s
        """
        return cls.create(966, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateHypnoPumpkin(
        cls,
        cost: int = 350,
        cd: float = 90.0,
        max_health: int = 4000,
        attack_damage: int = 120,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateHypnoPumpkin (967)
        Defaults: Cost=350 | CD=90.0s | HP=4000 | DMG=120 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(967, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperJalaNut(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperJalaNut (968)
        Defaults: Cost=150 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(968, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateJalaNut(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateJalaNut (969)
        Defaults: Cost=200 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(969, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperCaltrop(
        cls,
        cost: int = 350,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperCaltrop (970)
        Defaults: Cost=350 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(970, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateDoomGatling(
        cls,
        cost: int = 650,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateDoomGatling (971)
        Defaults: Cost=650 | CD=50.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(971, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateDoomScaredy(
        cls,
        cost: int = 650,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateDoomScaredy (972)
        Defaults: Cost=650 | CD=50.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(972, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PinkOnion(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PinkOnion (973)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=100 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(973, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSunMagnet(
        cls,
        cost: int = 375,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSunMagnet (974)
        Defaults: Cost=375 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(974, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceLaserUmbrella(
        cls,
        cost: int = 275,
        cd: float = 50.0,
        max_health: int = 1000,
        attack_damage: int = 80,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceLaserUmbrella (975)
        Defaults: Cost=275 | CD=50.0s | HP=1000 | DMG=80 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(975, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IFVStar(
        cls,
        cost: int = 325,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 160,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IFVStar (976)
        Defaults: Cost=325 | CD=7.5s | HP=300 | DMG=160 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(976, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateJalapeno(
        cls,
        cost: int = 400,
        cd: float = 90.0,
        max_health: int = 64000,
        attack_damage: int = 3600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateJalapeno (977)
        Defaults: Cost=400 | CD=90.0s | HP=64000 | DMG=3600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(977, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperCaltropPot(
        cls,
        cost: int = 350,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperCaltropPot (978)
        Defaults: Cost=350 | CD=7.5s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(978, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BambooDragon(
        cls,
        cost: int = 550,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 200,
        attack_interval: float = 4.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BambooDragon (979)
        Defaults: Cost=550 | CD=90.0s | HP=300 | DMG=200 | AtkInt=4.0s | ProdInt=0.0s
        """
        return cls.create(979, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateBamboo(
        cls,
        cost: int = 575,
        cd: float = 90.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateBamboo (980)
        Defaults: Cost=575 | CD=90.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(980, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateIceDoom(
        cls,
        cost: int = 875,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 3600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateIceDoom (981)
        Defaults: Cost=875 | CD=90.0s | HP=300 | DMG=3600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(981, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldThreePlantern(
        cls,
        cost: int = 575,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldThreePlantern (982)
        Defaults: Cost=575 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(982, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DeathMine(
        cls,
        cost: int = 425,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DeathMine (983)
        Defaults: Cost=425 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(983, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateLanternSplit(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateLanternSplit (984)
        Defaults: Cost=525 | CD=90.0s | HP=300 | DMG=40 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(984, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateHelmetGatling(
        cls,
        cost: int = 700,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 80,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateHelmetGatling (985)
        Defaults: Cost=700 | CD=50.0s | HP=4000 | DMG=80 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(985, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimatePortalSniper(
        cls,
        cost: int = 700,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 900,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimatePortalSniper (986)
        Defaults: Cost=700 | CD=50.0s | HP=300 | DMG=900 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(986, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSnowGatlingPuff(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSnowGatlingPuff (987)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(987, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateSunGatlingPuff(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateSunGatlingPuff (988)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(988, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateGarlicSplit(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateGarlicSplit (989)
        Defaults: Cost=525 | CD=90.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(989, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateJalaPuff(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 8000,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateJalaPuff (990)
        Defaults: Cost=150 | CD=30.0s | HP=8000 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(990, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateCornFume(
        cls,
        cost: int = 500,
        cd: float = 90.0,
        max_health: int = 3000,
        attack_damage: int = 300,
        attack_interval: float = 6.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateCornFume (991)
        Defaults: Cost=500 | CD=90.0s | HP=3000 | DMG=300 | AtkInt=6.0s | ProdInt=0.0s
        """
        return cls.create(991, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateIceShroom(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateIceShroom (992)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(992, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoCattailGirl(
        cls,
        cost: int = 275,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoCattailGirl (993)
        Defaults: Cost=275 | CD=90.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(993, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoCattailGirl_land(
        cls,
        cost: int = 275,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoCattailGirl_land (994)
        Defaults: Cost=275 | CD=90.0s | HP=300 | DMG=300 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(994, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateIceShroom2(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateIceShroom2 (995)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(995, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateFireSeaShroom(
        cls,
        cost: int = 500,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateFireSeaShroom (996)
        Defaults: Cost=500 | CD=50.0s | HP=300 | DMG=100 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(996, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UltimateHugeNut(
        cls,
        cost: int = 525,
        cd: float = 90.0,
        max_health: int = 64000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UltimateHugeNut (997)
        Defaults: Cost=525 | CD=90.0s | HP=64000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(997, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperHurricaneBlover(
        cls,
        cost: int = 300,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperHurricaneBlover (998)
        Defaults: Cost=300 | CD=30.0s | HP=300 | DMG=0 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(998, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperThreePeater_sp(
        cls,
        cost: int = 775,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 180,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperThreePeater_sp (999)
        Defaults: Cost=775 | CD=90.0s | HP=300 | DMG=180 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(999, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaSunFlower(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaSunFlower (1000)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=25.0s
        """
        return cls.create(1000, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Cherryshooter(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Cherryshooter (1001)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1001, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunBomb(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunBomb (1002)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1002, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryNut(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryNut (1003)
        Defaults: Cost=200 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1003, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaNut(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaNut (1004)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1004, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperCherryShooter(
        cls,
        cost: int = 400,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperCherryShooter (1005)
        Defaults: Cost=400 | CD=50.0s | HP=300 | DMG=300 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1005, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunNut(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 15.0,
    ) -> Dict[str, Any]:
        """PlantType.SunNut (1006)
        Defaults: Cost=100 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=15.0s
        """
        return cls.create(1006, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaMine(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaMine (1007)
        Defaults: Cost=75 | CD=30.0s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1007, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoubleCherry(
        cls,
        cost: int = 350,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoubleCherry (1008)
        Defaults: Cost=350 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1008, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunMine(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 15.0,
    ) -> Dict[str, Any]:
        """PlantType.SunMine (1009)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=15.0s
        """
        return cls.create(1009, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoNut(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoNut (1010)
        Defaults: Cost=75 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1010, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaChomper(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaChomper (1011)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1011, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NutChomper(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NutChomper (1012)
        Defaults: Cost=200 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1012, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperChomper(
        cls,
        cost: int = 300,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 200,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperChomper (1013)
        Defaults: Cost=300 | CD=30.0s | HP=4000 | DMG=200 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1013, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunChomper(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunChomper (1014)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1014, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoChomper(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoChomper (1015)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1015, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryChomper(
        cls,
        cost: int = 300,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryChomper (1016)
        Defaults: Cost=300 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1016, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryGatling(
        cls,
        cost: int = 550,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryGatling (1017)
        Defaults: Cost=550 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1017, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaPuff(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 2.25,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaPuff (1018)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=20 | AtkInt=2.25s | ProdInt=0.0s
        """
        return cls.create(1018, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoublePuff(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 2.25,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoublePuff (1019)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=20 | AtkInt=2.25s | ProdInt=0.0s
        """
        return cls.create(1019, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronPea(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 2000,
        attack_damage: int = 80,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronPea (1020)
        Defaults: Cost=200 | CD=7.5s | HP=2000 | DMG=80 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1020, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PuffNut(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 2000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PuffNut (1021)
        Defaults: Cost=25 | CD=30.0s | HP=2000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1021, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoPuff(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoPuff (1022)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1022, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoFume(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoFume (1023)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1023, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyHypno(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyHypno (1024)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1024, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredFume(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredFume (1025)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1025, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperHypno(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperHypno (1026)
        Defaults: Cost=175 | CD=30.0s | HP=300 | DMG=120 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1026, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TallNut(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TallNut (1027)
        Defaults: Cost=125 | CD=50.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1027, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TallNutFootball(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 16000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TallNutFootball (1028)
        Defaults: Cost=175 | CD=50.0s | HP=16000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1028, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronNut(
        cls,
        cost: int = 100,
        cd: float = 50.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronNut (1029)
        Defaults: Cost=100 | CD=50.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1029, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoubleShooter(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoubleShooter (1030)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1030, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunShroom(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SunShroom (1031)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1031, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GatlingPea(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GatlingPea (1032)
        Defaults: Cost=400 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1032, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TwinFlower(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 20.0,
    ) -> Dict[str, Any]:
        """PlantType.TwinFlower (1033)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=20.0s
        """
        return cls.create(1033, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SnowPeaShooter(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SnowPeaShooter (1034)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1034, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IcePuff(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 2.25,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IcePuff (1035)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=20 | AtkInt=2.25s | ProdInt=0.0s
        """
        return cls.create(1035, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SmallIceShroom(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SmallIceShroom (1036)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1036, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceFumeShroom(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceFumeShroom (1037)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1037, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceScaredyShroom(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceScaredyShroom (1038)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1038, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TallIceNut(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TallIceNut (1039)
        Defaults: Cost=200 | CD=50.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1039, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceDoom(
        cls,
        cost: int = 200,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceDoom (1040)
        Defaults: Cost=200 | CD=90.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1040, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceHypno(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceHypno (1041)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1041, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyDoom(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyDoom (1042)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1042, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomFume(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 60.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomFume (1043)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=60.0s | ProdInt=0.0s
        """
        return cls.create(1043, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PuffDoom(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PuffDoom (1044)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1044, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoDoom(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoDoom (1045)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1045, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperFume(
        cls,
        cost: int = 275,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperFume (1046)
        Defaults: Cost=275 | CD=50.0s | HP=300 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1046, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeSquash(
        cls,
        cost: int = 325,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeSquash (1047)
        Defaults: Cost=325 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1047, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CaltropNut(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CaltropNut (1048)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1048, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Jalakelp(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Jalakelp (1049)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1049, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Squashkelp(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Squashkelp (1050)
        Defaults: Cost=75 | CD=30.0s | HP=300 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1050, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Threekelp(
        cls,
        cost: int = 300,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Threekelp (1051)
        Defaults: Cost=300 | CD=30.0s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1051, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperTorch(
        cls,
        cost: int = 425,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperTorch (1052)
        Defaults: Cost=425 | CD=50.0s | HP=300 | DMG=40 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1052, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaTorch(
        cls,
        cost: int = 300,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaTorch (1053)
        Defaults: Cost=300 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1053, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaSquash(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaSquash (1054)
        Defaults: Cost=175 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1054, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeTorch(
        cls,
        cost: int = 450,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeTorch (1055)
        Defaults: Cost=450 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1055, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def KelpTorch(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.KelpTorch (1056)
        Defaults: Cost=175 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1056, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireSquash(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireSquash (1057)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1057, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DarkThreePeater(
        cls,
        cost: int = 400,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DarkThreePeater (1058)
        Defaults: Cost=400 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1058, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SquashTorch(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SquashTorch (1059)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1059, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SpikeRock(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 450,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SpikeRock (1060)
        Defaults: Cost=125 | CD=50.0s | HP=450 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1060, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchSpike(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchSpike (1061)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1061, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaCaltrop(
        cls,
        cost: int = 225,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaCaltrop (1062)
        Defaults: Cost=225 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1062, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SquashSpike(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SquashSpike (1063)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1063, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeSpike(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 5,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeSpike (1064)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=5 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1064, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GatlingPuff(
        cls,
        cost: int = 100,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 2.25,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GatlingPuff (1065)
        Defaults: Cost=100 | CD=50.0s | HP=300 | DMG=20 | AtkInt=2.25s | ProdInt=0.0s
        """
        return cls.create(1065, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperKelp(
        cls,
        cost: int = 350,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperKelp (1066)
        Defaults: Cost=350 | CD=30.0s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1066, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CattailPlant(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CattailPlant (1067)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1067, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceCattail(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceCattail (1068)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1068, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireCattail(
        cls,
        cost: int = 225,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireCattail (1069)
        Defaults: Cost=225 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1069, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GloomShroom(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.9,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GloomShroom (1070)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=20 | AtkInt=1.9s | ProdInt=0.0s
        """
        return cls.create(1070, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireGloom(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.9,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireGloom (1071)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.9s | ProdInt=0.0s
        """
        return cls.create(1071, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceGloom(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.9,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceGloom (1072)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.9s | ProdInt=0.0s
        """
        return cls.create(1072, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TallFireNut(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TallFireNut (1073)
        Defaults: Cost=250 | CD=50.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1073, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceSpikeRock(
        cls,
        cost: int = 300,
        cd: float = 50.0,
        max_health: int = 450,
        attack_damage: int = 40,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceSpikeRock (1074)
        Defaults: Cost=300 | CD=50.0s | HP=450 | DMG=40 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1074, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireSpikeRock(
        cls,
        cost: int = 350,
        cd: float = 50.0,
        max_health: int = 450,
        attack_damage: int = 40,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireSpikeRock (1075)
        Defaults: Cost=350 | CD=50.0s | HP=450 | DMG=40 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1075, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaCactus(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaCactus (1076)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1076, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaSunShroom(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 15.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaSunShroom (1077)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=15.0s
        """
        return cls.create(1077, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaLantern(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaLantern (1078)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1078, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternCactus(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternCactus (1079)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1079, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternBlover(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternBlover (1080)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1080, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternStar(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternStar (1081)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1081, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CactusBlover(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CactusBlover (1082)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1082, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaStarfruit(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaStarfruit (1083)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1083, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarBlover(
        cls,
        cost: int = 225,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarBlover (1084)
        Defaults: Cost=225 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1084, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CacstusStar(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CacstusStar (1085)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1085, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaBlover(
        cls,
        cost: int = 50,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaBlover (1086)
        Defaults: Cost=50 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1086, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternPumpkin(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternPumpkin (1087)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1087, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CactusPumpkin(
        cls,
        cost: int = 250,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CactusPumpkin (1088)
        Defaults: Cost=250 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1088, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarPumpkin(
        cls,
        cost: int = 250,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarPumpkin (1089)
        Defaults: Cost=250 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1089, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SplitPea(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SplitPea (1090)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1090, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BlowerPumpkin(
        cls,
        cost: int = 225,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BlowerPumpkin (1091)
        Defaults: Cost=225 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1091, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetPumpkin(
        cls,
        cost: int = 225,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetPumpkin (1092)
        Defaults: Cost=225 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1092, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetStar(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetStar (1093)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1093, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JackboxStar(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JackboxStar (1094)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1094, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PickaxeStar(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PickaxeStar (1095)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1095, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronStar(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 2000,
        attack_damage: int = 80,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronStar (1096)
        Defaults: Cost=275 | CD=7.5s | HP=2000 | DMG=80 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1096, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronPumpkin(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronPumpkin (1097)
        Defaults: Cost=275 | CD=30.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1097, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JackboxPumpkin(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JackboxPumpkin (1098)
        Defaults: Cost=275 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1098, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PickaxePumpkin(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PickaxePumpkin (1099)
        Defaults: Cost=275 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1099, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternMagnet(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 200,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternMagnet (1100)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=200 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1100, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaMagnet(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaMagnet (1101)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1101, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetBlover(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetBlover (1102)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1102, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetCactus(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetCactus (1103)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1103, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperStar(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperStar (1104)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1104, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoubleSnow(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoubleSnow (1105)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1105, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SnowGatling(
        cls,
        cost: int = 475,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SnowGatling (1106)
        Defaults: Cost=475 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1106, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SnowSplit(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SnowSplit (1107)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1107, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherrySplit(
        cls,
        cost: int = 450,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherrySplit (1108)
        Defaults: Cost=450 | CD=50.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1108, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SniperPea(
        cls,
        cost: int = 600,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 500,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SniperPea (1109)
        Defaults: Cost=600 | CD=7.5s | HP=300 | DMG=500 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1109, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperPumpkin(
        cls,
        cost: int = 325,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperPumpkin (1110)
        Defaults: Cost=325 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1110, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunCabbage(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 50,
        attack_interval: float = 5.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunCabbage (1111)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=50 | AtkInt=5.0s | ProdInt=0.0s
        """
        return cls.create(1111, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbagePot(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbagePot (1112)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1112, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornCabbage(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornCabbage (1113)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1113, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornPot(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornPot (1114)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1114, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornUmbrella(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornUmbrella (1115)
        Defaults: Cost=200 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1115, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WinterMelon(
        cls,
        cost: int = 375,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WinterMelon (1116)
        Defaults: Cost=375 | CD=50.0s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1116, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicCorn(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicCorn (1117)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1117, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicCabbage(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicCabbage (1118)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1118, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicMelon(
        cls,
        cost: int = 350,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicMelon (1119)
        Defaults: Cost=350 | CD=7.5s | HP=300 | DMG=100 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1119, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CobCannon(
        cls,
        cost: int = 300,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 35.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CobCannon (1120)
        Defaults: Cost=300 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=35.0s | ProdInt=0.0s
        """
        return cls.create(1120, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornMelon(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 140,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornMelon (1121)
        Defaults: Cost=400 | CD=7.5s | HP=300 | DMG=140 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1121, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireCannon(
        cls,
        cost: int = 425,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 3240,
        attack_interval: float = 35.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireCannon (1122)
        Defaults: Cost=425 | CD=50.0s | HP=300 | DMG=3240 | AtkInt=35.0s | ProdInt=0.0s
        """
        return cls.create(1122, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceCannon(
        cls,
        cost: int = 375,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 3240,
        attack_interval: float = 35.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceCannon (1123)
        Defaults: Cost=375 | CD=50.0s | HP=300 | DMG=3240 | AtkInt=35.0s | ProdInt=0.0s
        """
        return cls.create(1123, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageMelon(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageMelon (1124)
        Defaults: Cost=400 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1124, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonPot(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonPot (1125)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1125, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperMelon(
        cls,
        cost: int = 500,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 140,
        attack_interval: float = 5.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperMelon (1126)
        Defaults: Cost=500 | CD=7.5s | HP=300 | DMG=140 | AtkInt=5.0s | ProdInt=0.0s
        """
        return cls.create(1126, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicUmbrella(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicUmbrella (1127)
        Defaults: Cost=150 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1127, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageUmbrella(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageUmbrella (1128)
        Defaults: Cost=200 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1128, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MachineNut(
        cls,
        cost: int = 100,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MachineNut (1129)
        Defaults: Cost=100 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1129, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicPot(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicPot (1130)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1130, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonUmbrella(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 2000,
        attack_damage: int = 80,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonUmbrella (1131)
        Defaults: Cost=400 | CD=7.5s | HP=2000 | DMG=80 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1131, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonCannon(
        cls,
        cost: int = 750,
        cd: float = 50.0,
        max_health: int = 1000,
        attack_damage: int = 200,
        attack_interval: float = 35.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonCannon (1132)
        Defaults: Cost=750 | CD=50.0s | HP=1000 | DMG=200 | AtkInt=35.0s | ProdInt=0.0s
        """
        return cls.create(1132, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def UmbrellaPot(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.UmbrellaPot (1133)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1133, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverCabbage(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverCabbage (1134)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1134, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldCabbage(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldCabbage (1135)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1135, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverPot(
        cls,
        cost: int = 0,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverPot (1136)
        Defaults: Cost=0 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1136, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldPot(
        cls,
        cost: int = 9999,
        cd: float = 90.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldPot (1137)
        Defaults: Cost=9999 | CD=90.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1137, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverCorn(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverCorn (1138)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1138, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldCorn(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldCorn (1139)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1139, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TwinMarigold(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 20.0,
    ) -> Dict[str, Any]:
        """PlantType.TwinMarigold (1140)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=20.0s
        """
        return cls.create(1140, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverMelon(
        cls,
        cost: int = 325,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverMelon (1141)
        Defaults: Cost=325 | CD=7.5s | HP=300 | DMG=100 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1141, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldMelon(
        cls,
        cost: int = 525,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldMelon (1142)
        Defaults: Cost=525 | CD=7.5s | HP=300 | DMG=120 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1142, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverUmbrella(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverUmbrella (1143)
        Defaults: Cost=125 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1143, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldUmbrella(
        cls,
        cost: int = 225,
        cd: float = 15.0,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldUmbrella (1144)
        Defaults: Cost=225 | CD=15.0s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1144, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverGarlic(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 600,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverGarlic (1145)
        Defaults: Cost=75 | CD=7.5s | HP=600 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1145, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldGarlic(
        cls,
        cost: int = 125,
        cd: float = 15.0,
        max_health: int = 900,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldGarlic (1146)
        Defaults: Cost=125 | CD=15.0s | HP=900 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1146, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoNut(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoNut (1147)
        Defaults: Cost=125 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1147, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperUmbrella(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperUmbrella (1148)
        Defaults: Cost=275 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1148, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireMelon(
        cls,
        cost: int = 425,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireMelon (1149)
        Defaults: Cost=425 | CD=7.5s | HP=300 | DMG=120 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1149, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldMagnet(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldMagnet (1150)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1150, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperMachineNut(
        cls,
        cost: int = 600,
        cd: float = 30.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperMachineNut (1151)
        Defaults: Cost=600 | CD=30.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1151, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronPuff(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 80,
        attack_interval: float = 2.25,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronPuff (1152)
        Defaults: Cost=125 | CD=7.5s | HP=1000 | DMG=80 | AtkInt=2.25s | ProdInt=0.0s
        """
        return cls.create(1152, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SplitPuff(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 2.25,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SplitPuff (1153)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=20 | AtkInt=2.25s | ProdInt=0.0s
        """
        return cls.create(1153, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunMagnet(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SunMagnet (1154)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1154, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireCaltrop(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireCaltrop (1155)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1155, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Firekelp(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Firekelp (1156)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1156, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoMagnet(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoMagnet (1157)
        Defaults: Cost=175 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1157, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetFume(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetFume (1158)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1158, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronFume(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 2000,
        attack_damage: int = 50,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronFume (1159)
        Defaults: Cost=225 | CD=7.5s | HP=2000 | DMG=50 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1159, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HelmetFume(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 3000,
        attack_damage: int = 100,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HelmetFume (1160)
        Defaults: Cost=300 | CD=7.5s | HP=3000 | DMG=100 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1160, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigGatling(
        cls,
        cost: int = 800,
        cd: float = 30.0,
        max_health: int = 1000,
        attack_damage: int = 20,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BigGatling (1161)
        Defaults: Cost=800 | CD=30.0s | HP=1000 | DMG=20 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(1161, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryMine(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryMine (1162)
        Defaults: Cost=175 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1162, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaMine(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaMine (1163)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1163, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryPumpkin(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryPumpkin (1164)
        Defaults: Cost=275 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1164, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperSnowGatling(
        cls,
        cost: int = 675,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperSnowGatling (1165)
        Defaults: Cost=675 | CD=50.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1165, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryMagnet(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryMagnet (1166)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1166, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireSniper(
        cls,
        cost: int = 725,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireSniper (1167)
        Defaults: Cost=725 | CD=30.0s | HP=300 | DMG=300 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1167, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperGatling(
        cls,
        cost: int = 600,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperGatling (1168)
        Defaults: Cost=600 | CD=50.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1168, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigPumpkin(
        cls,
        cost: int = 450,
        cd: float = 50.0,
        max_health: int = 12000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BigPumpkin (1169)
        Defaults: Cost=450 | CD=50.0s | HP=12000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1169, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoPuff(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoPuff (1170)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=20 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(1170, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyPotato(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyPotato (1171)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=600 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1171, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicFume(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicFume (1172)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1172, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ObsidianJalapeno(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 32000,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ObsidianJalapeno (1173)
        Defaults: Cost=200 | CD=50.0s | HP=32000 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1173, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigChomper(
        cls,
        cost: int = 450,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BigChomper (1174)
        Defaults: Cost=450 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1174, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigSeaShroom(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 1000,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BigSeaShroom (1175)
        Defaults: Cost=150 | CD=30.0s | HP=1000 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1175, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoBlover(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoBlover (1176)
        Defaults: Cost=175 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1176, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Twinshulk(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 8,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Twinshulk (1177)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=8 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1177, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryTorch(
        cls,
        cost: int = 325,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryTorch (1178)
        Defaults: Cost=325 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1178, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryJalapeno(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryJalapeno (1179)
        Defaults: Cost=275 | CD=30.0s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1179, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceCaltrop(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceCaltrop (1180)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1180, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicBlover(
        cls,
        cost: int = 150,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicBlover (1181)
        Defaults: Cost=150 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1181, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceTorch(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceTorch (1182)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1182, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarPuff(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 2.25,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarPuff (1183)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=20 | AtkInt=2.25s | ProdInt=0.0s
        """
        return cls.create(1183, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunPot(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SunPot (1184)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1184, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternUmbrella(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternUmbrella (1185)
        Defaults: Cost=125 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1185, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CactusUmbrella(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CactusUmbrella (1186)
        Defaults: Cost=225 | CD=7.5s | HP=1000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1186, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverSunflower(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 15.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverSunflower (1187)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=15.0s
        """
        return cls.create(1187, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldSunflower(
        cls,
        cost: int = 9999,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldSunflower (1188)
        Defaults: Cost=9999 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1188, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceNut(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceNut (1189)
        Defaults: Cost=125 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1189, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoPumpkin(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoPumpkin (1190)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1190, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomCactus(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomCactus (1191)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1191, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomChomper(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomChomper (1192)
        Defaults: Cost=275 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1192, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireFume(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 1,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireFume (1193)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=1 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1193, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomPeashooter(
        cls,
        cost: int = 225,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomPeashooter (1194)
        Defaults: Cost=225 | CD=30.0s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1194, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternPot(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternPot (1195)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1195, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonFume(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonFume (1196)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=120 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1196, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarTorch(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarTorch (1197)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1197, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaStar(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaStar (1198)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1198, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomTorch(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomTorch (1199)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1199, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyPumpkin(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 2000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyPumpkin (1200)
        Defaults: Cost=150 | CD=30.0s | HP=2000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1200, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyStar(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 0.75,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyStar (1201)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=20 | AtkInt=0.75s | ProdInt=0.0s
        """
        return cls.create(1201, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SquashPumpkin(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SquashPumpkin (1202)
        Defaults: Cost=175 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1202, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornPuff(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornPuff (1203)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1203, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BloverUmbrella(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BloverUmbrella (1204)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1204, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoPumpkin(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoPumpkin (1205)
        Defaults: Cost=200 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1205, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NutUmbrella(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NutUmbrella (1206)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1206, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryUmbrella(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 600,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryUmbrella (1207)
        Defaults: Cost=250 | CD=7.5s | HP=600 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1207, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PortalPea(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PortalPea (1208)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=0 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1208, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetCorn(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetCorn (1209)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1209, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PortalCorn(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PortalCorn (1210)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1210, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronCorn(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 2000,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronCorn (1211)
        Defaults: Cost=250 | CD=7.5s | HP=2000 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1211, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceCherry(
        cls,
        cost: int = 225,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceCherry (1212)
        Defaults: Cost=225 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1212, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetDoom(
        cls,
        cost: int = 225,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetDoom (1213)
        Defaults: Cost=225 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1213, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PortalDoom(
        cls,
        cost: int = 325,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 3240,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PortalDoom (1214)
        Defaults: Cost=325 | CD=50.0s | HP=300 | DMG=3240 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1214, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PortalNut(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PortalNut (1215)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1215, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaBlover(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaBlover (1216)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1216, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SpruceShulk(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SpruceShulk (1217)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1217, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WaterShulk(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 8,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WaterShulk (1218)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=8 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1218, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WaterSpruce(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 50,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WaterSpruce (1219)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=50 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1219, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperSpruce(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 5,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperSpruce (1220)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=5 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1220, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LotusSpruce(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LotusSpruce (1221)
        Defaults: Cost=175 | CD=30.0s | HP=300 | DMG=100 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1221, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ShulkLotus(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ShulkLotus (1222)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1222, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SpruceFurnace(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SpruceFurnace (1223)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1223, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ShulkFurnace(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ShulkFurnace (1224)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1224, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceFurnace(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceFurnace (1225)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1225, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WaterFurnace(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WaterFurnace (1226)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1226, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LotusAloes(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LotusAloes (1227)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1227, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceSquash(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceSquash (1228)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1228, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoSquash(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoSquash (1229)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1229, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoGarlic(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoGarlic (1230)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1230, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoMine(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoMine (1231)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1231, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def KelpMine_land(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.KelpMine_land (1232)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1232, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def KelpMine_water(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.KelpMine_water (1233)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1233, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperFurnace(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperFurnace (1234)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1234, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireNut(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireNut (1235)
        Defaults: Cost=175 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1235, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomNut(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomNut (1236)
        Defaults: Cost=175 | CD=50.0s | HP=4000 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1236, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CaltropKelp_water(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CaltropKelp_water (1237)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1237, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CaltropKelp_land(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CaltropKelp_land (1238)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1238, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BucketDoom(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 3240,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BucketDoom (1239)
        Defaults: Cost=175 | CD=50.0s | HP=300 | DMG=3240 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1239, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeMine(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeMine (1240)
        Defaults: Cost=300 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1240, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternChomper(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternChomper (1241)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1241, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JackboxDoom(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 3240,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JackboxDoom (1242)
        Defaults: Cost=175 | CD=50.0s | HP=300 | DMG=3240 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1242, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryPot(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryPot (1243)
        Defaults: Cost=175 | CD=30.0s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1243, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryBlover(
        cls,
        cost: int = 250,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryBlover (1244)
        Defaults: Cost=250 | CD=30.0s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1244, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigSunShroom(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 20.0,
    ) -> Dict[str, Any]:
        """PlantType.BigSunShroom (1245)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=20.0s
        """
        return cls.create(1245, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredSun(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredSun (1246)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1246, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SpruceBallista(
        cls,
        cost: int = 300,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SpruceBallista (1247)
        Defaults: Cost=300 | CD=50.0s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1247, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomSunflower(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 50.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomSunflower (1248)
        Defaults: Cost=175 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=50.0s
        """
        return cls.create(1248, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomSeed(
        cls,
        cost: int = 0,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomSeed (1249)
        Defaults: Cost=0 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1249, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SquashNut(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 160,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SquashNut (1250)
        Defaults: Cost=100 | CD=30.0s | HP=4000 | DMG=160 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1250, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverDoom(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverDoom (1251)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1251, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldDoom(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldDoom (1252)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1252, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronSquash(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 1000,
        attack_damage: int = 3240,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronSquash (1253)
        Defaults: Cost=100 | CD=30.0s | HP=1000 | DMG=3240 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1253, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WaterBallista(
        cls,
        cost: int = 375,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WaterBallista (1254)
        Defaults: Cost=375 | CD=50.0s | HP=300 | DMG=80 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1254, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NutBlover(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NutBlover (1255)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1255, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CactusNut(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CactusNut (1256)
        Defaults: Cost=175 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1256, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarNut(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarNut (1257)
        Defaults: Cost=175 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1257, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LotusBamboo(
        cls,
        cost: int = 100,
        cd: float = 15.0,
        max_health: int = 1500,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LotusBamboo (1258)
        Defaults: Cost=100 | CD=15.0s | HP=1500 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1258, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def WaterBamboo(
        cls,
        cost: int = 125,
        cd: float = 15.0,
        max_health: int = 1500,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.WaterBamboo (1259)
        Defaults: Cost=125 | CD=15.0s | HP=1500 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1259, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BambooSpruce(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 1800,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BambooSpruce (1260)
        Defaults: Cost=175 | CD=7.5s | HP=1800 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1260, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonNut(
        cls,
        cost: int = 350,
        cd: float = 30.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonNut (1261)
        Defaults: Cost=350 | CD=30.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1261, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageNut(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageNut (1262)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1262, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornNut(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornNut (1263)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1263, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ShulkBamboo(
        cls,
        cost: int = 150,
        cd: float = 15.0,
        max_health: int = 1500,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ShulkBamboo (1264)
        Defaults: Cost=150 | CD=15.0s | HP=1500 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1264, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BambooFurnace(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BambooFurnace (1265)
        Defaults: Cost=75 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1265, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HugeWallNut(
        cls,
        cost: int = 325,
        cd: float = 50.0,
        max_health: int = 32000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HugeWallNut (1266)
        Defaults: Cost=325 | CD=50.0s | HP=32000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1266, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoPeashooter(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoPeashooter (1267)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1267, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoRepeater(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoRepeater (1268)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1268, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoSplit(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoSplit (1269)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1269, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoGatling(
        cls,
        cost: int = 475,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoGatling (1270)
        Defaults: Cost=475 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1270, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperThreeGatling(
        cls,
        cost: int = 875,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperThreeGatling (1271)
        Defaults: Cost=875 | CD=50.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1271, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomSniper(
        cls,
        cost: int = 675,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 0.3,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomSniper (1272)
        Defaults: Cost=675 | CD=50.0s | HP=300 | DMG=100 | AtkInt=0.3s | ProdInt=0.0s
        """
        return cls.create(1272, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyBlover(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyBlover (1273)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1273, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryScaredy(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryScaredy (1274)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1274, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomBlover(
        cls,
        cost: int = 225,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 180,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomBlover (1275)
        Defaults: Cost=225 | CD=50.0s | HP=300 | DMG=180 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1275, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceBlover(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceBlover (1276)
        Defaults: Cost=175 | CD=50.0s | HP=300 | DMG=1 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1276, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomStar(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomStar (1277)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1277, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicNut(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicNut (1278)
        Defaults: Cost=100 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1278, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetNut(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetNut (1279)
        Defaults: Cost=150 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1279, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonPuff(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonPuff (1280)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1280, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbagePuff(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbagePuff (1281)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1281, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NutTorch(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NutTorch (1282)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1282, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchFireNut(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchFireNut (1283)
        Defaults: Cost=50 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1283, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverNut(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 6000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverNut (1284)
        Defaults: Cost=75 | CD=30.0s | HP=6000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1284, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldNut(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldNut (1285)
        Defaults: Cost=100 | CD=30.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1285, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoMelon(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoMelon (1286)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=120 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1286, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IcePot(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IcePot (1287)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1287, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchPumpkin(
        cls,
        cost: int = 300,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchPumpkin (1288)
        Defaults: Cost=300 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1288, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchFirePumpkin(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchFirePumpkin (1289)
        Defaults: Cost=125 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1289, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SniperPuff(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 500,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SniperPuff (1290)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=500 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1290, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaFume(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaFume (1291)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1291, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperHypnoGatling(
        cls,
        cost: int = 675,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperHypnoGatling (1292)
        Defaults: Cost=675 | CD=50.0s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1292, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaNut(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 2000,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaNut (1293)
        Defaults: Cost=50 | CD=30.0s | HP=2000 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1293, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaScaredyshroom(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 0.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaScaredyshroom (1294)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=20 | AtkInt=0.5s | ProdInt=0.0s
        """
        return cls.create(1294, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeNut(
        cls,
        cost: int = 325,
        cd: float = 30.0,
        max_health: int = 12000,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeNut (1295)
        Defaults: Cost=325 | CD=30.0s | HP=12000 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1295, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TreasureMine(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TreasureMine (1296)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1296, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceSeashroom(
        cls,
        cost: int = 75,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceSeashroom (1297)
        Defaults: Cost=75 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1297, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaFume(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaFume (1298)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1298, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NutPumpkin(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NutPumpkin (1299)
        Defaults: Cost=175 | CD=30.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1299, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BigGloom(
        cls,
        cost: int = 300,
        cd: float = 7.5,
        max_health: int = 1000,
        attack_damage: int = 20,
        attack_interval: float = 1.9,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BigGloom (1300)
        Defaults: Cost=300 | CD=7.5s | HP=1000 | DMG=20 | AtkInt=1.9s | ProdInt=0.0s
        """
        return cls.create(1300, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SmallUmbrella(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SmallUmbrella (1301)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1301, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PuffSeaShroom(
        cls,
        cost: int = 0,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PuffSeaShroom (1302)
        Defaults: Cost=0 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1302, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomSeaShroom(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomSeaShroom (1303)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1303, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchSunflower(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchSunflower (1304)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1304, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaHypno(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaHypno (1305)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1305, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HelmetGatling(
        cls,
        cost: int = 500,
        cd: float = 30.0,
        max_health: int = 3000,
        attack_damage: int = 80,
        attack_interval: float = 2.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HelmetGatling (1306)
        Defaults: Cost=500 | CD=30.0s | HP=3000 | DMG=80 | AtkInt=2.0s | ProdInt=0.0s
        """
        return cls.create(1306, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunStar(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunStar (1307)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=100 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1307, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunJalapeno(
        cls,
        cost: int = 175,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunJalapeno (1308)
        Defaults: Cost=175 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1308, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternNut(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternNut (1309)
        Defaults: Cost=75 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1309, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyNut(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyNut (1310)
        Defaults: Cost=75 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1310, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NutPot(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NutPot (1311)
        Defaults: Cost=75 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1311, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def NutFume(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.NutFume (1312)
        Defaults: Cost=125 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1312, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def KelpNut(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.KelpNut (1313)
        Defaults: Cost=75 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1313, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MagnetMelon(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MagnetMelon (1314)
        Defaults: Cost=400 | CD=7.5s | HP=300 | DMG=120 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1314, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IronMelon(
        cls,
        cost: int = 450,
        cd: float = 7.5,
        max_health: int = 2000,
        attack_damage: int = 200,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IronMelon (1315)
        Defaults: Cost=450 | CD=7.5s | HP=2000 | DMG=200 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1315, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PortalMelon(
        cls,
        cost: int = 500,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PortalMelon (1316)
        Defaults: Cost=500 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1316, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomJalapeno(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomJalapeno (1317)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1317, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaPumpkin(
        cls,
        cost: int = 225,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaPumpkin (1318)
        Defaults: Cost=225 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1318, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaPeashooter(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaPeashooter (1319)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1319, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaDoubleshooter(
        cls,
        cost: int = 325,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaDoubleshooter (1320)
        Defaults: Cost=325 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1320, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaSplit(
        cls,
        cost: int = 425,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaSplit (1321)
        Defaults: Cost=425 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1321, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaGatling(
        cls,
        cost: int = 525,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaGatling (1322)
        Defaults: Cost=525 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1322, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicPumpkin(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicPumpkin (1323)
        Defaults: Cost=175 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1323, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunPumpkin(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SunPumpkin (1324)
        Defaults: Cost=175 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1324, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunIceShroom(
        cls,
        cost: int = 125,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SunIceShroom (1325)
        Defaults: Cost=125 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1325, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunHypno(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 200,
        attack_interval: float = 0.0,
        produce_interval: float = 25.0,
    ) -> Dict[str, Any]:
        """PlantType.SunHypno (1326)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=200 | AtkInt=0.0s | ProdInt=25.0s
        """
        return cls.create(1326, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ChomperPumpkin(
        cls,
        cost: int = 275,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ChomperPumpkin (1327)
        Defaults: Cost=275 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1327, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicThreePeater(
        cls,
        cost: int = 325,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicThreePeater (1328)
        Defaults: Cost=325 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1328, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicSniper(
        cls,
        cost: int = 650,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 500,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicSniper (1329)
        Defaults: Cost=650 | CD=7.5s | HP=300 | DMG=500 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1329, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryThreePeater(
        cls,
        cost: int = 425,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryThreePeater (1330)
        Defaults: Cost=425 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1330, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperCherryGatling(
        cls,
        cost: int = 750,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperCherryGatling (1331)
        Defaults: Cost=750 | CD=50.0s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1331, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomCherry(
        cls,
        cost: int = 275,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomCherry (1332)
        Defaults: Cost=275 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1332, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryHypno(
        cls,
        cost: int = 225,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryHypno (1333)
        Defaults: Cost=225 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1333, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaPumpkin(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaPumpkin (1334)
        Defaults: Cost=125 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1334, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoChomper(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoChomper (1335)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1335, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoJalapeno(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoJalapeno (1336)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1336, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornCaltrop(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornCaltrop (1337)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1337, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IcePlantern(
        cls,
        cost: int = 100,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IcePlantern (1338)
        Defaults: Cost=100 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1338, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaMine_land(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaMine_land (1339)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1339, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaMine_water(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaMine_water (1340)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1340, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomPlantern(
        cls,
        cost: int = 150,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomPlantern (1341)
        Defaults: Cost=150 | CD=15.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1341, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageCannon(
        cls,
        cost: int = 400,
        cd: float = 30.0,
        max_health: int = 1000,
        attack_damage: int = 40,
        attack_interval: float = 0.75,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageCannon (1342)
        Defaults: Cost=400 | CD=30.0s | HP=1000 | DMG=40 | AtkInt=0.75s | ProdInt=0.0s
        """
        return cls.create(1342, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SquashMelon(
        cls,
        cost: int = 350,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 120,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SquashMelon (1343)
        Defaults: Cost=350 | CD=15.0s | HP=300 | DMG=120 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1343, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherrySquash(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherrySquash (1344)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1344, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomSquash(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomSquash (1345)
        Defaults: Cost=250 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1345, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornFume(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornFume (1346)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1346, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def AllPeater(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.AllPeater (1347)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1347, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunBlover(
        cls,
        cost: int = 150,
        cd: float = 15.0,
        max_health: int = 300,
        attack_damage: int = 10,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunBlover (1348)
        Defaults: Cost=150 | CD=15.0s | HP=300 | DMG=10 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1348, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PuffPumpkin(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PuffPumpkin (1349)
        Defaults: Cost=125 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1349, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FumePumpkin(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FumePumpkin (1350)
        Defaults: Cost=200 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1350, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunSquash(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunSquash (1351)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1351, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonPumpkin(
        cls,
        cost: int = 425,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 80,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonPumpkin (1352)
        Defaults: Cost=425 | CD=30.0s | HP=4000 | DMG=80 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1352, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoSquashBody(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoSquashBody (1353)
        Defaults: Cost=75 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1353, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoSquash(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoSquash (1354)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1354, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomGarlic(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomGarlic (1355)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1355, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarFume(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarFume (1356)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1356, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ScaredyPot(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ScaredyPot (1357)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1357, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternFume(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 10,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternFume (1358)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=10 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1358, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageBlover(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageBlover (1359)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1359, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CornBlover(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CornBlover (1360)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1360, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonBlover(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonBlover (1361)
        Defaults: Cost=400 | CD=7.5s | HP=300 | DMG=80 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1361, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoFume(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoFume (1362)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1362, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SquashCorn(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SquashCorn (1363)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1363, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PotatoDoom(
        cls,
        cost: int = 150,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PotatoDoom (1364)
        Defaults: Cost=150 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1364, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarHypno(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarHypno (1365)
        Defaults: Cost=200 | CD=30.0s | HP=300 | DMG=20 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1365, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaSquash(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaSquash (1366)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1366, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SilverIceShroom(
        cls,
        cost: int = 100,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SilverIceShroom (1367)
        Defaults: Cost=100 | CD=50.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1367, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GoldIceShroom(
        cls,
        cost: int = 200,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 200,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GoldIceShroom (1368)
        Defaults: Cost=200 | CD=50.0s | HP=300 | DMG=200 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1368, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageFume(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageFume (1369)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1369, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PuffSquash(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 300,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PuffSquash (1370)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=300 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1370, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomPumpkin(
        cls,
        cost: int = 250,
        cd: float = 50.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomPumpkin (1371)
        Defaults: Cost=250 | CD=50.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1371, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CaltropPot(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CaltropPot (1372)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1372, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternPea(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 10,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternPea (1373)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=10 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1373, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SquashBlover(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 100,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SquashBlover (1374)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=100 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1374, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceCabbage(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceCabbage (1375)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1375, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceCorn(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceCorn (1376)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1376, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def KelpPuff(
        cls,
        cost: int = 25,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.KelpPuff (1377)
        Defaults: Cost=25 | CD=7.5s | HP=300 | DMG=20 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1377, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageSquash(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageSquash (1378)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1378, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreePlantern(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreePlantern (1379)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=30 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1379, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoPot(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoPot (1380)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1380, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternRepeater(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 10,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternRepeater (1381)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=10 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1381, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternSplit(
        cls,
        cost: int = 325,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 10,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternSplit (1382)
        Defaults: Cost=325 | CD=7.5s | HP=300 | DMG=10 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1382, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def LanternGatling(
        cls,
        cost: int = 425,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 10,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.LanternGatling (1383)
        Defaults: Cost=425 | CD=7.5s | HP=300 | DMG=10 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1383, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PuffJalapeno(
        cls,
        cost: int = 50,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 600,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PuffJalapeno (1384)
        Defaults: Cost=50 | CD=7.5s | HP=300 | DMG=600 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1384, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicPea(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicPea (1385)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1385, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicRepeater(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicRepeater (1386)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1386, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicSplit(
        cls,
        cost: int = 350,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicSplit (1387)
        Defaults: Cost=350 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1387, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicGatling(
        cls,
        cost: int = 450,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicGatling (1388)
        Defaults: Cost=450 | CD=7.5s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1388, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchFume(
        cls,
        cost: int = 250,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchFume (1389)
        Defaults: Cost=250 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1389, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ChomperSquash(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ChomperSquash (1390)
        Defaults: Cost=200 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1390, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def GarlicTorch(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.GarlicTorch (1391)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1391, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SeaSquash(
        cls,
        cost: int = 50,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SeaSquash (1392)
        Defaults: Cost=50 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1392, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CactusFume(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CactusFume (1393)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1393, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HypnoTorch(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HypnoTorch (1394)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1394, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def KelpFume(
        cls,
        cost: int = 100,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.KelpFume (1395)
        Defaults: Cost=100 | CD=7.5s | HP=300 | DMG=30 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1395, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SpreadFume(
        cls,
        cost: int = 75,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SpreadFume (1396)
        Defaults: Cost=75 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1396, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SpreadScaredyShroom(
        cls,
        cost: int = 75,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SpreadScaredyShroom (1397)
        Defaults: Cost=75 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1397, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireCabbage(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 60,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireCabbage (1398)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=60 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1398, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomCabbage(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 15.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomCabbage (1399)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=1800 | AtkInt=15.0s | ProdInt=0.0s
        """
        return cls.create(1399, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaCorn(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaCorn (1400)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=30 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1400, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceMine(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceMine (1401)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1401, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThornsBamboo(
        cls,
        cost: int = 150,
        cd: float = 15.0,
        max_health: int = 1500,
        attack_damage: int = 100,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThornsBamboo (1402)
        Defaults: Cost=150 | CD=15.0s | HP=1500 | DMG=100 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1402, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThornsLotus(
        cls,
        cost: int = 100,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThornsLotus (1403)
        Defaults: Cost=100 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1403, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaPot(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaPot (1404)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1404, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SniperPot(
        cls,
        cost: int = 625,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SniperPot (1405)
        Defaults: Cost=625 | CD=30.0s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1405, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThornsSpruce(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 200,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThornsSpruce (1406)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=200 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1406, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperGatlingPumpkin(
        cls,
        cost: int = 725,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperGatlingPumpkin (1407)
        Defaults: Cost=725 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1407, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomMelon(
        cls,
        cost: int = 425,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomMelon (1408)
        Defaults: Cost=425 | CD=50.0s | HP=300 | DMG=1800 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1408, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThronsAloes(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThronsAloes (1409)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1409, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Pumpiner(
        cls,
        cost: int = 250,
        cd: float = 30.0,
        max_health: int = 8000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Pumpiner (1410)
        Defaults: Cost=250 | CD=30.0s | HP=8000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1410, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomCorn(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomCorn (1411)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=40 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1411, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarPea(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarPea (1412)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1412, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def JalaPumpkin(
        cls,
        cost: int = 250,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 20,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.JalaPumpkin (1413)
        Defaults: Cost=250 | CD=30.0s | HP=4000 | DMG=20 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1413, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomKelp(
        cls,
        cost: int = 150,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomKelp (1414)
        Defaults: Cost=150 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1414, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CactusCaltrop(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CactusCaltrop (1415)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1415, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThornsShulk(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 5,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThornsShulk (1416)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=5 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1416, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CabbageCaltrop(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CabbageCaltrop (1417)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1417, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def MelonCaltrop(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.MelonCaltrop (1418)
        Defaults: Cost=400 | CD=7.5s | HP=300 | DMG=80 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1418, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SunCaltrop(
        cls,
        cost: int = 150,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SunCaltrop (1419)
        Defaults: Cost=150 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.0s | ProdInt=0.0s
        """
        return cls.create(1419, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def HurricaneBlover(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.HurricaneBlover (1420)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=0 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1420, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchMine(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchMine (1421)
        Defaults: Cost=200 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1421, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireMine(
        cls,
        cost: int = 25,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireMine (1422)
        Defaults: Cost=25 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1422, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperNutShooter(
        cls,
        cost: int = 650,
        cd: float = 50.0,
        max_health: int = 8000,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperNutShooter (1423)
        Defaults: Cost=650 | CD=50.0s | HP=8000 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1423, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SniperChomper(
        cls,
        cost: int = 750,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 500,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SniperChomper (1424)
        Defaults: Cost=750 | CD=7.5s | HP=300 | DMG=500 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1424, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def PeaScaredy(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.PeaScaredy (1425)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1425, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BloverMine(
        cls,
        cost: int = 125,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 1800,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BloverMine (1426)
        Defaults: Cost=125 | CD=30.0s | HP=300 | DMG=1800 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1426, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IceCactus(
        cls,
        cost: int = 200,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IceCactus (1427)
        Defaults: Cost=200 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1427, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CherryFume(
        cls,
        cost: int = 225,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CherryFume (1428)
        Defaults: Cost=225 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1428, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarSniper(
        cls,
        cost: int = 725,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 500,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarSniper (1429)
        Defaults: Cost=725 | CD=7.5s | HP=300 | DMG=500 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(1429, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def TorchSeaShroom(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.TorchSeaShroom (1430)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1430, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FireSeaShroom(
        cls,
        cost: int = 0,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FireSeaShroom (1431)
        Defaults: Cost=0 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1431, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def SuperGatlingPeaMine(
        cls,
        cost: int = 625,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 30,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.SuperGatlingPeaMine (1432)
        Defaults: Cost=625 | CD=50.0s | HP=300 | DMG=30 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1432, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeMelon(
        cls,
        cost: int = 575,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 80,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeMelon (1433)
        Defaults: Cost=575 | CD=7.5s | HP=300 | DMG=80 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1433, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeCorn(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 20,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeCorn (1434)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=20 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1434, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreePumpkin(
        cls,
        cost: int = 400,
        cd: float = 0.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreePumpkin (1435)
        Defaults: Cost=400 | CD=0.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1435, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def IcePumpkin(
        cls,
        cost: int = 200,
        cd: float = 30.0,
        max_health: int = 4000,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.IcePumpkin (1436)
        Defaults: Cost=200 | CD=30.0s | HP=4000 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1436, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def BloverPot(
        cls,
        cost: int = 125,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.BloverPot (1437)
        Defaults: Cost=125 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1437, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def CaltropFume(
        cls,
        cost: int = 175,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.CaltropFume (1438)
        Defaults: Cost=175 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1438, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreeCabbage(
        cls,
        cost: int = 375,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreeCabbage (1439)
        Defaults: Cost=375 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1439, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def DoomThreePeater(
        cls,
        cost: int = 400,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 40,
        attack_interval: float = 1.5,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.DoomThreePeater (1440)
        Defaults: Cost=400 | CD=7.5s | HP=300 | DMG=40 | AtkInt=1.5s | ProdInt=0.0s
        """
        return cls.create(1440, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def StarSquash(
        cls,
        cost: int = 175,
        cd: float = 30.0,
        max_health: int = 300,
        attack_damage: int = 900,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.StarSquash (1441)
        Defaults: Cost=175 | CD=30.0s | HP=300 | DMG=900 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1441, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def ThreePot(
        cls,
        cost: int = 275,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 0,
        attack_interval: float = 0.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.ThreePot (1442)
        Defaults: Cost=275 | CD=7.5s | HP=300 | DMG=0 | AtkInt=0.0s | ProdInt=0.0s
        """
        return cls.create(1442, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def Ulti_cherryGatling(
        cls,
        cost: int = 950,
        cd: float = 7.5,
        max_health: int = 300,
        attack_damage: int = 1,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.Ulti_cherryGatling (3000)
        Defaults: Cost=950 | CD=7.5s | HP=300 | DMG=1 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(3000, cost, cd, max_health, attack_damage, attack_interval, produce_interval)

    @classmethod
    def FlyingThreePeater_sp(
        cls,
        cost: int = 775,
        cd: float = 50.0,
        max_health: int = 300,
        attack_damage: int = 180,
        attack_interval: float = 3.0,
        produce_interval: float = 0.0,
    ) -> Dict[str, Any]:
        """PlantType.FlyingThreePeater_sp (5000)
        Defaults: Cost=775 | CD=50.0s | HP=300 | DMG=180 | AtkInt=3.0s | ProdInt=0.0s
        """
        return cls.create(5000, cost, cd, max_health, attack_damage, attack_interval, produce_interval)
