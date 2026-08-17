from enum import Enum


class SceneType(Enum):
    Day = 0
    Night = 1
    Pool = 2
    NightPool = 3
    Roof = 4
    NightRoof = 5
    Day_6 = 6
    Night_6 = 7
    SuperDay = 8
    SuperPool = 9
    Travel_roof = 10
    Test_green = 11
    Travel_roof_dusk = 12
    Travel_roof_night = 13
    MidDay = 14
    BilliardBallDay = 15
    BilliardBallMidDay = 16
    PVPScaryPot = 17
    Snow = 18
    Chess = 19
    Snow_6 = 20
    ReversalPool = 21
    BigPool = 22
    Roof_Pool = 23
    River = 24
    IZDay = 25
    SnowPool = 26
    LongMap = 27
    TreasureBeach = 28
    MidMap = 29
    LavaBeach = 30
    NormalBeach = 31
    SnowPool_night = 32
    RoofPool_dusk = 33
    RoofPool_night = 34
    Day_bubble = 35
    AutoChess = 36
    LavaPool = 37
    PVPRandom = 38
    LongMap_rhy = 39
    NightSnow = 40
    ShootingDay = 41
    NightWinter = 42
    Desert = 43

class LevelType(Enum):
    Nothing = -1
    Advanture = 0
    Challenge = 1
    IZ = 2
    Survival = 3
    Explore = 4
    TravelAdvanture = 5
    SkinLevel = 6
    AbyssRealm = 7
    NewAdvanture = 8
    TowerLevel = 9
    StarAdvanture = 10
    CustomLevel = 11
    
class PlantType(Enum):
    Nothing = -1,
    Peashooter = 0,
    SunFlower = 1,
    CherryBomb = 2,
    WallNut = 3,
    PotatoMine = 4,
    Chomper = 5,
    SmallPuff = 6,
    FumeShroom = 7,
    HypnoShroom = 8,
    ScaredyShroom = 9,
    IceShroom = 10,
    DoomShroom = 11,
    LilyPad = 12,
    Squash = 13,
    ThreePeater = 14,
    Tanglekelp = 15,
    Jalapeno = 16,
    Caltrop = 17,
    TorchWood = 18,
    SeaShroom = 19,
    Plantern = 20,
    Cactus = 21,
    Blover = 22,
    StarFruit = 23,
    Pumpkin = 24,
    Magnetshroom = 25,
    Cabbagepult = 26,
    Pot = 27,
    Cornpult = 28,
    Garlic = 29,
    Umbrellaleaf = 30,
    Marigold = 31,
    Melonpult = 32,
    Shulkflower = 33,
    ElectricOnion = 34,
    PineFurnace = 35,
    SpruceShooter = 36,
    IceLotus = 37,
    WaterAloes = 38,
    Bamboo = 39,
    Thorns = 40,
    JackboxPlant = 212,
    PickaxePlant = 213,
    PortalPlant = 214,
    MachineShardPlant = 215,
    SuperMachineShardPlant = 216,
    HolographicPlant = 217,
    Pudding = 218,
    VectorPlant = 219,
    GoldScaryPot = 220,
    MixAnim = 221,
    Firecracker = 222,
    Apple = 223,
    BucketPlant = 224,
    HelmetPlant = 225,
    XXSPot = 226,
    DiamondImitater = 227,
    ZombieEndoFlame = 228,
    LuckyBlover = 229,
    FireSunshroom_a = 230,
    FireSunshroom_b = 231,
    FireSunshroom_c = 232,
    SnowPresent = 233,
    DiamondPotatoNut = 234,
    PassionFruit = 235,
    FrozenPear = 236,
    IcePeach = 237,
    Chrysantheautumn = 238,
    Gravebuster = 239,
    ObsidianWheat = 240,
    IceBean = 241,
    EndoFlameGirl = 242,
    Hamburger = 243,
    MixBomb = 244,
    Imitater = 245,
    MagnetBox = 246,
    MagnetInterface = 247,
    Squalour = 248,
    SwordStar = 249,
    PresentZombie = 250,
    BigSunNut = 251,
    CattailGirl = 252,
    Wheat = 253,
    EndoFlame = 254,
    BigWallNut = 255,
    Present = 256,
    AbyssSwordStar = 300,
    UltimateMinigun = 301,
    UltimateRedLunar = 302,
    ImitateWheat = 303,
    SolarSunflower = 304,
    UltimateHypnoDoom = 305,
    UltimatePoisonFume = 306,
    AcientSunNut = 307,
    BedRockTallNut = 308,
    UltimateSniperGatling = 309,
    UltimateMachineNut = 310,
    Tower_peasunflower = 350,
    Tower_BigSunShroom = 351,
    Tower_cherryShooter = 352,
    Tower_starNut = 353,
    Tower_sunmine = 354,
    Tower_iceGloom = 355,
    Tower_cherryChomper = 356,
    Tower_electricOnion = 357,
    Tower_peaPuff = 358,
    Tower_sunShroom = 359,
    Tower_doomFume = 360,
    Tower_gravebuster = 361,
    Tower_scaredyfume = 362,
    Tower_iceblover = 363,
    Tower_doomStar = 364,
    Tower_waterCan = 365,
    Tower_lilyPad = 366,
    Tower_squashNut = 367,
    Tower_threeMine = 368,
    HypnoEmperor = 900,
    UltimateGatling = 901,
    UltimateTorch = 902,
    UltimateChomper = 903,
    UltimateFume = 904,
    SuperSunNut = 905,
    ObsidianSpike = 906,
    DoomGatling = 907,
    SnowGatlingPuff = 908,
    UltimateStar = 909,
    UltimateGloom = 910,
    UltimatePumpkin = 911,
    UltimateFly = 912,
    UltimateTallNut = 913,
    UltimateMelon = 914,
    UltimateCannon = 915,
    EmeraldUmbrella = 916,
    HypnoQueen = 917,
    AshThreePeater = 918,
    SuperThreePeater = 919,
    UltimateBlover = 920,
    GarlicUltimateChomper = 921,
    CherryUltimatePumpkin = 922,
    RedEmeraldUmbrella = 923,
    UltimateHypno = 924,
    UltimatePotatoNut = 925,
    CattailLour = 926,
    UltimateBigGatling = 927,
    SuperHypnoDoom = 928,
    SunGatlingPuff = 929,
    GatlingDoomScaredy = 930,
    ObsidianWallNut = 931,
    GoldThreeTorch = 932,
    UltimateCactus = 933,
    UltimateCabbage = 934,
    IFVPumpkin = 935,
    SolarPot = 936,
    LaserUmbrella = 937,
    GoldHypnoDoom = 938,
    UltimateGatlingBlover = 939,
    UltimateSpring = 940,
    UltimateKelp = 941,
    IFVIronPuff = 942,
    UltimateCorn = 943,
    UltimateMagnet = 944,
    UltimatePortalNut = 945,
    UltimateBigSniper = 946,
    UltimateSpruce = 947,
    UltimateStarTorch = 948,
    UltimatePlantern = 949,
    SolarLily = 950,
    UltimateBigChomper = 951,
    UltimateMelonPuff = 952,
    UltimateExplodeCannon = 953,
    UltimateSunflower = 954,
    UltimateLunarCabbage = 955,
    DeathChomper = 956,
    UltimateWinterMelon = 957,
    UltimateCattail = 958,
    NuclearDoomCherry = 959,
    UltimateSeaShroom = 960,
    IFVBlover = 961,
    FlyingThreePeater = 962,
    UltimateSunNut = 963,
    UltimateMelonCannon = 964,
    NuclearSquash = 965,
    UltimateCabbageCannon = 966,
    UltimateHypnoPumpkin = 967,
    SuperJalaNut = 968,
    UltimateJalaNut = 969,
    SuperCaltrop = 970,
    UltimateDoomGatling = 971,
    UltimateDoomScaredy = 972,
    PinkOnion = 973,
    UltimateSunMagnet = 974,
    IceLaserUmbrella = 975,
    IFVStar = 976,
    UltimateJalapeno = 977,
    SuperCaltropPot = 978,
    BambooDragon = 979,
    UltimateBamboo = 980,
    UltimateIceDoom = 981,
    GoldThreePlantern = 982,
    DeathMine = 983,
    UltimateLanternSplit = 984,
    UltimateHelmetGatling = 985,
    UltimatePortalSniper = 986,
    UltimateSnowGatlingPuff = 987,
    UltimateSunGatlingPuff = 988,
    UltimateGarlicSplit = 989,
    UltimateJalaPuff = 990,
    UltimateCornFume = 991,
    UltimateIceShroom = 992,
    HypnoCattailGirl = 993,
    HypnoCattailGirl_land = 994,
    UltimateIceShroom2 = 995,
    UltimateFireSeaShroom = 996,
    UltimateHugeNut = 997,
    SuperHurricaneBlover = 998,
    SuperThreePeater_sp = 999,
    PeaSunFlower = 1000,
    Cherryshooter = 1001,
    SunBomb = 1002,
    CherryNut = 1003,
    PeaNut = 1004,
    SuperCherryShooter = 1005,
    SunNut = 1006,
    PeaMine = 1007,
    DoubleCherry = 1008,
    SunMine = 1009,
    PotatoNut = 1010,
    PeaChomper = 1011,
    NutChomper = 1012,
    SuperChomper = 1013,
    SunChomper = 1014,
    PotatoChomper = 1015,
    CherryChomper = 1016,
    CherryGatling = 1017,
    PeaPuff = 1018,
    DoublePuff = 1019,
    IronPea = 1020,
    PuffNut = 1021,
    HypnoPuff = 1022,
    HypnoFume = 1023,
    ScaredyHypno = 1024,
    ScaredFume = 1025,
    SuperHypno = 1026,
    TallNut = 1027,
    TallNutFootball = 1028,
    IronNut = 1029,
    DoubleShooter = 1030,
    SunShroom = 1031,
    GatlingPea = 1032,
    TwinFlower = 1033,
    SnowPeaShooter = 1034,
    IcePuff = 1035,
    SmallIceShroom = 1036,
    IceFumeShroom = 1037,
    IceScaredyShroom = 1038,
    TallIceNut = 1039,
    IceDoom = 1040,
    IceHypno = 1041,
    ScaredyDoom = 1042,
    DoomFume = 1043,
    PuffDoom = 1044,
    HypnoDoom = 1045,
    SuperFume = 1046,
    ThreeSquash = 1047,
    CaltropNut = 1048,
    Jalakelp = 1049,
    Squashkelp = 1050,
    Threekelp = 1051,
    SuperTorch = 1052,
    JalaTorch = 1053,
    JalaSquash = 1054,
    ThreeTorch = 1055,
    KelpTorch = 1056,
    FireSquash = 1057,
    DarkThreePeater = 1058,
    SquashTorch = 1059,
    SpikeRock = 1060,
    TorchSpike = 1061,
    JalaCaltrop = 1062,
    SquashSpike = 1063,
    ThreeSpike = 1064,
    GatlingPuff = 1065,
    SuperKelp = 1066,
    CattailPlant = 1067,
    IceCattail = 1068,
    FireCattail = 1069,
    GloomShroom = 1070,
    FireGloom = 1071,
    IceGloom = 1072,
    TallFireNut = 1073,
    IceSpikeRock = 1074,
    FireSpikeRock = 1075,
    SeaCactus = 1076,
    SeaSunShroom = 1077,
    SeaLantern = 1078,
    LanternCactus = 1079,
    LanternBlover = 1080,
    LanternStar = 1081,
    CactusBlover = 1082,
    SeaStarfruit = 1083,
    StarBlover = 1084,
    CacstusStar = 1085,
    SeaBlover = 1086,
    LanternPumpkin = 1087,
    CactusPumpkin = 1088,
    StarPumpkin = 1089,
    SplitPea = 1090,
    BlowerPumpkin = 1091,
    MagnetPumpkin = 1092,
    MagnetStar = 1093,
    JackboxStar = 1094,
    PickaxeStar = 1095,
    IronStar = 1096,
    IronPumpkin = 1097,
    JackboxPumpkin = 1098,
    PickaxePumpkin = 1099,
    LanternMagnet = 1100,
    SeaMagnet = 1101,
    MagnetBlover = 1102,
    MagnetCactus = 1103,
    SuperStar = 1104,
    DoubleSnow = 1105,
    SnowGatling = 1106,
    SnowSplit = 1107,
    CherrySplit = 1108,
    SniperPea = 1109,
    SuperPumpkin = 1110,
    SunCabbage = 1111,
    CabbagePot = 1112,
    CornCabbage = 1113,
    CornPot = 1114,
    CornUmbrella = 1115,
    WinterMelon = 1116,
    GarlicCorn = 1117,
    GarlicCabbage = 1118,
    GarlicMelon = 1119,
    CobCannon = 1120,
    CornMelon = 1121,
    FireCannon = 1122,
    IceCannon = 1123,
    CabbageMelon = 1124,
    MelonPot = 1125,
    SuperMelon = 1126,
    GarlicUmbrella = 1127,
    CabbageUmbrella = 1128,
    MachineNut = 1129,
    GarlicPot = 1130,
    MelonUmbrella = 1131,
    MelonCannon = 1132,
    UmbrellaPot = 1133,
    SilverCabbage = 1134,
    GoldCabbage = 1135,
    SilverPot = 1136,
    GoldPot = 1137,
    SilverCorn = 1138,
    GoldCorn = 1139,
    TwinMarigold = 1140,
    SilverMelon = 1141,
    GoldMelon = 1142,
    SilverUmbrella = 1143,
    GoldUmbrella = 1144,
    SilverGarlic = 1145,
    GoldGarlic = 1146,
    HypnoNut = 1147,
    SuperUmbrella = 1148,
    FireMelon = 1149,
    GoldMagnet = 1150,
    SuperMachineNut = 1151,
    IronPuff = 1152,
    SplitPuff = 1153,
    SunMagnet = 1154,
    FireCaltrop = 1155,
    Firekelp = 1156,
    HypnoMagnet = 1157,
    MagnetFume = 1158,
    IronFume = 1159,
    HelmetFume = 1160,
    BigGatling = 1161,
    CherryMine = 1162,
    JalaMine = 1163,
    CherryPumpkin = 1164,
    SuperSnowGatling = 1165,
    CherryMagnet = 1166,
    FireSniper = 1167,
    SuperGatling = 1168,
    BigPumpkin = 1169,
    PotatoPuff = 1170,
    ScaredyPotato = 1171,
    GarlicFume = 1172,
    ObsidianJalapeno = 1173,
    BigChomper = 1174,
    BigSeaShroom = 1175,
    HypnoBlover = 1176,
    Twinshulk = 1177,
    CherryTorch = 1178,
    CherryJalapeno = 1179,
    IceCaltrop = 1180,
    GarlicBlover = 1181,
    IceTorch = 1182,
    StarPuff = 1183,
    SunPot = 1184,
    LanternUmbrella = 1185,
    CactusUmbrella = 1186,
    SilverSunflower = 1187,
    GoldSunflower = 1188,
    IceNut = 1189,
    PotatoPumpkin = 1190,
    DoomCactus = 1191,
    DoomChomper = 1192,
    FireFume = 1193,
    DoomPeashooter = 1194,
    LanternPot = 1195,
    MelonFume = 1196,
    StarTorch = 1197,
    JalaStar = 1198,
    DoomTorch = 1199,
    ScaredyPumpkin = 1200,
    ScaredyStar = 1201,
    SquashPumpkin = 1202,
    CornPuff = 1203,
    BloverUmbrella = 1204,
    HypnoPumpkin = 1205,
    NutUmbrella = 1206,
    CherryUmbrella = 1207,
    PortalPea = 1208,
    MagnetCorn = 1209,
    PortalCorn = 1210,
    IronCorn = 1211,
    IceCherry = 1212,
    MagnetDoom = 1213,
    PortalDoom = 1214,
    PortalNut = 1215,
    PeaBlover = 1216,
    SpruceShulk = 1217,
    WaterShulk = 1218,
    WaterSpruce = 1219,
    SuperSpruce = 1220,
    LotusSpruce = 1221,
    ShulkLotus = 1222,
    SpruceFurnace = 1223,
    ShulkFurnace = 1224,
    IceFurnace = 1225,
    WaterFurnace = 1226,
    LotusAloes = 1227,
    IceSquash = 1228,
    HypnoSquash = 1229,
    HypnoGarlic = 1230,
    HypnoMine = 1231,
    KelpMine_land = 1232,
    KelpMine_water = 1233,
    SuperFurnace = 1234,
    FireNut = 1235,
    DoomNut = 1236,
    CaltropKelp_water = 1237,
    CaltropKelp_land = 1238,
    BucketDoom = 1239,
    ThreeMine = 1240,
    LanternChomper = 1241,
    JackboxDoom = 1242,
    CherryPot = 1243,
    CherryBlover = 1244,
    BigSunShroom = 1245,
    ScaredSun = 1246,
    SpruceBallista = 1247,
    DoomSunflower = 1248,
    DoomSeed = 1249,
    SquashNut = 1250,
    SilverDoom = 1251,
    GoldDoom = 1252,
    IronSquash = 1253,
    WaterBallista = 1254,
    NutBlover = 1255,
    CactusNut = 1256,
    StarNut = 1257,
    LotusBamboo = 1258,
    WaterBamboo = 1259,
    BambooSpruce = 1260,
    MelonNut = 1261,
    CabbageNut = 1262,
    CornNut = 1263,
    ShulkBamboo = 1264,
    BambooFurnace = 1265,
    HugeWallNut = 1266,
    HypnoPeashooter = 1267,
    HypnoRepeater = 1268,
    HypnoSplit = 1269,
    HypnoGatling = 1270,
    SuperThreeGatling = 1271,
    DoomSniper = 1272,
    ScaredyBlover = 1273,
    CherryScaredy = 1274,
    DoomBlover = 1275,
    IceBlover = 1276,
    DoomStar = 1277,
    GarlicNut = 1278,
    MagnetNut = 1279,
    MelonPuff = 1280,
    CabbagePuff = 1281,
    NutTorch = 1282,
    TorchFireNut = 1283,
    SilverNut = 1284,
    GoldNut = 1285,
    HypnoMelon = 1286,
    IcePot = 1287,
    TorchPumpkin = 1288,
    TorchFirePumpkin = 1289,
    SniperPuff = 1290,
    SeaFume = 1291,
    SuperHypnoGatling = 1292,
    SeaNut = 1293,
    SeaScaredyshroom = 1294,
    ThreeNut = 1295,
    TreasureMine = 1296,
    IceSeashroom = 1297,
    PeaFume = 1298,
    NutPumpkin = 1299,
    BigGloom = 1300,
    SmallUmbrella = 1301,
    PuffSeaShroom = 1302,
    DoomSeaShroom = 1303,
    TorchSunflower = 1304,
    SeaHypno = 1305,
    HelmetGatling = 1306,
    SunStar = 1307,
    SunJalapeno = 1308,
    LanternNut = 1309,
    ScaredyNut = 1310,
    NutPot = 1311,
    NutFume = 1312,
    KelpNut = 1313,
    MagnetMelon = 1314,
    IronMelon = 1315,
    PortalMelon = 1316,
    DoomJalapeno = 1317,
    PeaPumpkin = 1318,
    JalaPeashooter = 1319,
    JalaDoubleshooter = 1320,
    JalaSplit = 1321,
    JalaGatling = 1322,
    GarlicPumpkin = 1323,
    SunPumpkin = 1324,
    SunIceShroom = 1325,
    SunHypno = 1326,
    ChomperPumpkin = 1327,
    GarlicThreePeater = 1328,
    GarlicSniper = 1329,
    CherryThreePeater = 1330,
    SuperCherryGatling = 1331,
    DoomCherry = 1332,
    CherryHypno = 1333,
    SeaPumpkin = 1334,
    HypnoChomper = 1335,
    HypnoJalapeno = 1336,
    CornCaltrop = 1337,
    IcePlantern = 1338,
    SeaMine_land = 1339,
    SeaMine_water = 1340,
    DoomPlantern = 1341,
    CabbageCannon = 1342,
    SquashMelon = 1343,
    CherrySquash = 1344,
    DoomSquash = 1345,
    CornFume = 1346,
    AllPeater = 1347,
    SunBlover = 1348,
    PuffPumpkin = 1349,
    FumePumpkin = 1350,
    SunSquash = 1351,
    MelonPumpkin = 1352,
    PotatoSquashBody = 1353,
    PotatoSquash = 1354,
    DoomGarlic = 1355,
    StarFume = 1356,
    ScaredyPot = 1357,
    LanternFume = 1358,
    CabbageBlover = 1359,
    CornBlover = 1360,
    MelonBlover = 1361,
    PotatoFume = 1362,
    SquashCorn = 1363,
    PotatoDoom = 1364,
    StarHypno = 1365,
    PeaSquash = 1366,
    SilverIceShroom = 1367,
    GoldIceShroom = 1368,
    CabbageFume = 1369,
    PuffSquash = 1370,
    DoomPumpkin = 1371,
    CaltropPot = 1372,
    LanternPea = 1373,
    SquashBlover = 1374,
    IceCabbage = 1375,
    IceCorn = 1376,
    KelpPuff = 1377,
    CabbageSquash = 1378,
    ThreePlantern = 1379,
    HypnoPot = 1380,
    LanternRepeater = 1381,
    LanternSplit = 1382,
    LanternGatling = 1383,
    PuffJalapeno = 1384,
    GarlicPea = 1385,
    GarlicRepeater = 1386,
    GarlicSplit = 1387,
    GarlicGatling = 1388,
    TorchFume = 1389,
    ChomperSquash = 1390,
    GarlicTorch = 1391,
    SeaSquash = 1392,
    CactusFume = 1393,
    HypnoTorch = 1394,
    KelpFume = 1395,
    SpreadFume = 1396,
    SpreadScaredyShroom = 1397,
    FireCabbage = 1398,
    DoomCabbage = 1399,
    JalaCorn = 1400,
    IceMine = 1401,
    ThornsBamboo = 1402,
    ThornsLotus = 1403,
    PeaPot = 1404,
    SniperPot = 1405,
    ThornsSpruce = 1406,
    SuperGatlingPumpkin = 1407,
    DoomMelon = 1408,
    ThronsAloes = 1409,
    Pumpiner = 1410,
    DoomCorn = 1411,
    StarPea = 1412,
    JalaPumpkin = 1413,
    DoomKelp = 1414,
    CactusCaltrop = 1415,
    ThornsShulk = 1416,
    CabbageCaltrop = 1417,
    MelonCaltrop = 1418,
    SunCaltrop = 1419,
    HurricaneBlover = 1420,
    TorchMine = 1421,
    FireMine = 1422,
    SuperNutShooter = 1423,
    SniperChomper = 1424,
    PeaScaredy = 1425,
    BloverMine = 1426,
    IceCactus = 1427,
    CherryFume = 1428,
    StarSniper = 1429,
    TorchSeaShroom = 1430,
    FireSeaShroom = 1431,
    SuperGatlingPeaMine = 1432,
    ThreeMelon = 1433,
    ThreeCorn = 1434,
    ThreePumpkin = 1435,
    IcePumpkin = 1436,
    BloverPot = 1437,
    CaltropFume = 1438,
    ThreeCabbage = 1439,
    DoomThreePeater = 1440,
    StarSquash = 1441,
    ThreePot = 1442,
    MagicSnowPea = 1443,
    EnderPumpkin = 1444,
    SuperGatlingFume = 1445,
    CoinShroom = 1446,
    BigCoinShroom = 1447,
    SniperScaredy = 1448,
    SilverHypnoShroom = 1449,
    GoldHypnoShroom = 1450,
    CherryPuff = 1451,
    ChomperScaredy = 1452,
    UmbrellaFume = 1453,
    DoomPot = 1454,
    DoomUmbrella = 1455,
    SeaChomper = 1456,
    IceStar = 1457,
    FumeChomper = 1458,
    PuffChomper = 1459,
    SeaPot = 1460,
    GarlicStar = 1461,
    Ulti_cherryGatling = 3000,
    FlyingThreePeater_sp = 5000,
    MagicSnowPea2 = 5001,
    EndPumpiner = 5002,
    UltimatePresentKelp = 5003,
    UltimateFurnace = 5004

class Plant_DieReason(Enum):
    Default = 0,
    ByWheat = 1,
    ByMix = 2,
    ByDisMix = 3,
    ByLevelUp = 4,
    BySteal = 5,
    ByBejeweled = 6,
    ByShovel = 7,
    BySelf = 8,
    ByFreeze = 9,
    Hid = 10,
    CrashInWater = 11,
    Crash = 12,
    Wheel = 13

class ZombieType(Enum):
    Nothing = -1,
    NormalZombie = 0,
    FlagZombie = 1,
    ConeZombie = 2,
    PolevaulterZombie = 3,
    BucketZombie = 4,
    PaperZombie = 5,
    DancePolZombie = 6,
    DancePolZombie2 = 7,
    DoorZombie = 8,
    FootballZombie = 9,
    JacksonZombie = 10,
    ZombieDuck = 11,
    ConeZombieDuck = 12,
    BucketZombieDuck = 13,
    SubmarineZombie = 14,
    ElitePaperZombie = 15,
    DriverZombie = 16,
    SnorkleZombie = 17,
    SuperDriver = 18,
    Dolphinrider = 19,
    DrownZombie = 20,
    DollDiamond = 21,
    DollGold = 22,
    DollSilver = 23,
    JackboxZombie = 24,
    BalloonZombie = 25,
    KirovZombie = 26,
    SnowDolphinrider = 27,
    MinerZombie = 28,
    IronBalloonZombie = 29,
    SuperJackboxZombie = 30,
    CatapultZombie = 31,
    PogoZombie = 32,
    LadderZombie = 33,
    SuperPogoZombie = 34,
    Gargantuar = 35,
    RedGargantuar = 36,
    ImpZombie = 37,
    IronGargantuar = 38,
    IronRedGargantuar = 39,
    MachineNutZombie = 40,
    SilverZombie = 41,
    GoldZombie = 42,
    SuperGargantuar = 43,
    ZombieBoss = 44,
    BungiZombie = 45,
    ZombieBoss2 = 46,
    SnowZombie = 47,
    NewYearZombie = 48,
    SnowGunZombie = 49,
    SnowShieldZombie = 50,
    SnowDrownZombie = 51,
    ProtalZombie = 52,
    LevatationZombie = 53,
    TrainingDummy = 54,
    SnowConeZombie = 55,
    SnowMonsterZombie = 56,
    SuperSnowMonsterZombie = 57,
    PickaxeZombie = 58,
    DolphinPaper = 59,
    ProjectileZombie = 60,
    FootballDolphin = 61,
    MiniSnowMonster = 62,
    GoldBungiZombie = 63,
    SandJackson = 64,
    StoneDancer = 65,
    FlagFootball = 66,
    MiniSandMonster = 67,
    ChickenImp = 68,
    HorseZombie = 69,
    SuperHorse = 70,
    BoatImp = 71,
    SuperLadderZombie = 72,
    EndoFlameZombie = 73,
    HypnoJalapenoZombie = 74,
    HypnoJalapenoPickaxeZombie = 75,
    DrownGargantuar = 76,
    SuperPolevaulter = 77,
    WhiteFootball = 78,
    YellowFootball = 79,
    PortalPolevaulter = 80,
    CoachPaper = 81,
    BucketPaper = 82,
    PenguinZombie = 83,
    SnowNormalZombie = 84,
    SnowBucketZombie = 85,
    SuperPenguinZombie = 86,
    IronConeZombie = 87,
    ElephantZombie = 88,
    ZombieLoonNut = 89,
    RedZombieLoonNut = 90,
    PolFootballZombie = 91,
    PeaShooterZombie = 100,
    CherryShooterZombie = 101,
    SuperCherryShooterZombie = 102,
    WallNutZombie = 103,
    CherryPaperZombie = 104,
    RandomZombie = 105,
    BucketNutZombie = 106,
    CherryNutZombie = 107,
    IronPeaZombie = 108,
    TallNutFootballZombie = 109,
    RandomPlusZombie = 110,
    TallIceNutZombie = 111,
    CherryCatapultZombie = 112,
    DolphinPeaZombie = 113,
    IronPeaDoorZombie = 114,
    SquashZombie = 115,
    JalaSquashZombie = 116,
    JalapenoZombie = 117,
    GatlingFootballZombie = 118,
    IronBalloonZombie2 = 119,
    DoomZombie = 120,
    RandomGargantuar = 121,
    BlueGargantuar = 122,
    GreenGargantuar = 123,
    YellowGargantuar = 124,
    Zombie9527 = 125,
    TallFireNutZombie = 126,
    ObsidianTallNutZombie = 127,
    SunNutZombie = 128,
    SuperSunNutZombie = 129,
    GatlingPeaZombie = 130,
    SnowGatlingPeaZombie = 131,
    BedRockSnowZombie = 132,
    SqualourZombie = 133,
    SuperSubmarine = 200,
    JacksonDriver = 201,
    FootballDrown = 202,
    CherryPaperZ95 = 203,
    BlackFootball = 204,
    SuperKirov = 205,
    SuperBombThrower = 206,
    QuickJacksonZombie = 207,
    QingZombie = 208,
    JackboxJumpZombie = 209,
    SuperMachineNutZombie = 210,
    LandSubmarine = 211,
    UltimateGargantuar = 212,
    ObsidianImpZombie = 213,
    DolphinGatlingZombie = 214,
    DiamondRandomZombie = 215,
    DrownpultZombie = 216,
    SuperDancePolZombie = 217,
    UltimateFootballDrown = 218,
    UltimateMachineNutZombie = 219,
    UltimateFootballZombie = 220,
    UltimateKirovZombie = 221,
    UltimateJacksonDriver = 222,
    UltimatePaperZombie = 223,
    UltimateJackboxZombie = 224,
    GatlingBlackFootball = 225,
    LegionZombie = 226,
    IceClawZombie = 227,
    UltimateSnowZombie = 228,
    UltimateHorse = 229,
    UltimateHorse2 = 230,
    HorseBoss = 231,
    SummonedHorse = 232,
    ArmedGargantuar = 233,
    UltimateImpKing = 234,
    ImpKing = 235,
    SuperLevatation = 236,
    CherrySubmarine = 237,
    SnowMonsterRider = 238,
    WaterJackboxJumpZombie = 239,
    UltiWaterGargantuar = 240,
    UltimateGoldGargantuar = 241,
    DoomPaper = 242,
    UltimateLegionZombie = 243,
    UltimateSwordZombie = 244,
    MachineLevatation = 245,
    LegionSniperZombie = 246,
    VoodooDollZombie = 247,
    ObsidianClawZombie = 248,
    UltimateDolphin = 249,
    PortalBalloonZombie = 250,
    BlackHorse = 251,
    SuperBlackHorse = 252,
    BlackJackboxZombie = 253,
    BlackElephantZombie = 254,
    BlackTrainZombie = 255,
    BlackFlagFootball = 256,
    SuperBlackFootball = 257,
    ArmoredImpZombie = 258,
    UltimateEndoflameZombie = 259,
    FootballBoss = 260,
    JacksonDriverBoss = 261,
    GatlingPaper_a = 300,
    GatlingPaper_b = 301,
    GatlingPaper_c = 302,
    BlackFootball_a = 303,
    BlackFootball_b = 304,
    BlackFootball_c = 305,
    BlackFootball_c2 = 306,
    Jackson_a = 307,
    Jackson_b = 308,
    Jackson_c = 309,
    Submarine_a = 310,
    Submarine_b = 311,
    Submarine_b2 = 312,
    Submarine_c = 313,
    Submarine_c2 = 314,
    Drown_a = 315,
    Drown_b = 316,
    Drown_c = 317,
    Pickaxe_a = 318,
    Pickaxe_b = 319,
    Pickaxe_c = 320,
    Driver_a = 321,
    Driver_b = 322,
    Driver_c = 323,
    Jackbox_a = 324,
    Jackbox_b = 325,
    Jackbox_c = 326,
    Kirov_a = 327,
    Kirov_b = 328,
    Kirov_c = 329,
    EternalZombie_a = 330,
    EternalZombie_b = 331,
    EternalZombie_c = 332,
    Drownpult_a = 333,
    Drownpult_b = 334,
    Drownpult_c = 335,
    ElephantZombie_a = 336,
    ElephantZombie_b = 337,
    ElephantZombie_c = 338

class SoundType(Enum):
    Splat = 0,
    Splat2 = 1,
    Splat3 = 2,
    Throw = 3,
    Throw2 = 4,
    ZombieFalling1 = 5,
    ZombieFalling2 = 6,
    LimbsPop = 7,
    Chomp = 8,
    Chomp2 = 9,
    ChompSoft = 10,
    Gulp = 11,
    PlasticHit = 12,
    PlasticHit2 = 13,
    ShieldHit = 14,
    ShieldHit2 = 15,
    Points = 16,
    Coin = 17,
    Tap = 19,
    Tap2 = 20,
    Shovel = 21,
    Plant = 22,
    Plant2 = 23,
    PlantWater = 24,
    SeedLift = 25,
    Buzzer = 26,
    Bleep = 27,
    GraveButton = 28,
    ButtonClick = 29,
    Pause = 30,
    ReadySetPlant = 31,
    HugeWave = 32,
    FinalWave = 33,
    Awooga = 34,
    Siren = 35,
    LightFill = 37,
    RollIn = 38,
    ReverseExplosion = 39,
    CherryBomb = 40,
    DoomShroom = 41,
    Jalapeno = 42,
    Explosion = 43,
    SmallDoom = 70,
    WaterBomb = 139,
    NewspaperRip = 44,
    NewspaperRargh = 45,
    NewspaperRargh2 = 46,
    PotatoMine = 47,
    DirtRise = 48,
    BigChomp = 49,
    GrassStep = 50,
    PoleVault = 51,
    LoseMusic = 52,
    Bowling = 53,
    BowlingImpact = 54,
    BowlingImpact2 = 55,
    PlantGrow = 56,
    Puff = 57,
    Fume = 58,
    Ignite = 59,
    Ignite2 = 60,
    FirePea = 61,
    Floop = 62,
    MindControlled = 63,
    Bonk = 64,
    Fertilizer = 65,
    Prize = 66,
    Swing = 93,
    BugSpray = 115,
    Phonograph = 116,
    Chime = 117,
    VaseBreaking = 126,
    Frozen = 67,
    SnowPeaSparkles = 68,
    Dancer = 69,
    SquashHmm = 72,
    SquashHmm2 = 73,
    GargantuarThump = 74,
    ZombieSplash = 75,
    Zamboni = 76,
    BalloonPop = 77,
    DolphinAppears = 78,
    DolphinBeforeJumping = 79,
    CattailHit = 80,
    CattailPlant1 = 81,
    CattailPlant2 = 82,
    MagnetShroom = 83,
    WinMusic = 84,
    Pattern = 85,
    BalloonInflate = 86,
    Blover = 87,
    JackintheBox = 89,
    JackSurprise = 90,
    JackSurprise2 = 91,
    KirovReproting = 92,
    WakeUp = 94,
    Portal = 95,
    Lighting = 96,
    MoneyFalls = 97,
    KernelPult = 98,
    KernelPult2 = 99,
    Butter = 100,
    Basketball = 101,
    Yuck = 102,
    Yuck2 = 103,
    MelonImpact = 104,
    MelonImpact2 = 105,
    Boing = 106,
    CobLaunch = 107,
    Shoop = 108,
    PogoZombie = 109,
    Imp = 110,
    Imp2 = 111,
    GargantuarDeath = 112,
    Watering = 113,
    Ceramic = 114,
    RVthrow = 120,
    Diamond = 125,
    LaserCharge = 127,
    Laser = 128,
    SnowShield = 129,
    SnowShield2 = 130,
    SnowShield3 = 131,
    GraveBusterChomp = 132,
    Sword = 133,
    ExplodeSword = 134,
    BigSniper = 135,
    LawnMower = 136,
    PoolCleaner = 137,
    Knife = 138,
    DoomSniperShoot = 140,
    HorseHit = 141,
    HorseDie = 142,
    Bubble = 143,
    LaserLong = 144,
    CannonShoot = 145,
    bungee_scream1 = 146,
    bungee_scream2 = 147,
    bungee_scream3 = 148,
    hydraulic = 149,
    hydraulic_short = 150,
    bossboulderattack = 151,
    HypnoCattail1 = 152,
    HypnoCattail2 = 153,
    HypnoCattail3 = 154

class KeyCode(Enum):
    None_ = 0
    Backspace = 8
    Tab = 9
    Clear = 12
    Return = 13
    Pause = 19
    Escape = 27
    Space = 32
    Exclaim = 33
    DoubleQuote = 34
    Hash = 35
    Dollar = 36
    Percent = 37
    Ampersand = 38
    Quote = 39
    LeftParen = 40
    RightParen = 41
    Asterisk = 42
    Plus = 43
    Comma = 44
    Minus = 45
    Period = 46
    Slash = 47
    
    # --- Top Row Digits ---
    Alpha0 = 48
    Alpha1 = 49
    Alpha2 = 50
    Alpha3 = 51
    Alpha4 = 52
    Alpha5 = 53
    Alpha6 = 54
    Alpha7 = 55
    Alpha8 = 56
    Alpha9 = 57
    
    Colon = 58
    Semicolon = 59
    Less = 60
    Equals = 61
    Greater = 62
    Question = 63
    At = 64
    LeftBracket = 91
    Backslash = 92
    RightBracket = 93
    Caret = 94
    Underscore = 95
    BackQuote = 96
    
    # --- Alphabet Keys ---
    A = 97
    B = 98
    C = 99
    D = 100
    E = 101
    F = 102
    G = 103
    H = 104
    I = 105
    J = 106
    K = 107
    L = 108
    M = 109
    N = 110
    O = 111
    P = 112
    Q = 113
    R = 114
    S = 115
    T = 116
    Y = 117
    V = 118
    W = 119
    X = 120
    U = 121
    Z = 122
    
    LeftCurlyBracket = 123
    Pipe = 124
    RightCurlyBracket = 125
    Tilde = 126
    Delete = 127
    
    # --- Numpad Keys ---
    Keypad0 = 256
    Keypad1 = 257
    Keypad2 = 258
    Keypad3 = 259
    Keypad4 = 260
    Keypad5 = 261
    Keypad6 = 262
    Keypad7 = 263
    Keypad8 = 264
    Keypad9 = 265
    KeypadPeriod = 266
    KeypadDivide = 267
    KeypadMultiply = 268
    KeypadMinus = 269
    KeypadPlus = 270
    KeypadEnter = 271
    KeypadEquals = 272
    
    # --- Control / Navigation Keys ---
    UpArrow = 273
    DownArrow = 274
    RightArrow = 275
    LeftArrow = 276
    Insert = 277
    Home = 278
    End = 279
    PageUp = 280
    PageDown = 281
    
    # --- Function Keys ---
    F1 = 282
    F2 = 283
    F3 = 284
    F4 = 285
    F5 = 286
    F6 = 287
    F7 = 288
    F8 = 289
    F9 = 290
    F10 = 291
    F11 = 292
    F12 = 293
    F13 = 294
    F14 = 295
    F15 = 296
    
    # --- Modifiers & Toggles ---
    Numlock = 300
    Capslock = 301
    ScrollLock = 302
    RightShift = 303
    LeftShift = 304
    RightControl = 305
    LeftControl = 306
    RightAlt = 307
    LeftAlt = 308
    RightCommand = 309
    LeftCommand = 310
    LeftSuper = 311
    RightSuper = 312
    AltGr = 313
    Help = 315
    Print = 316
    SysReq = 317
    Break = 318
    Menu = 319
    
    # --- Mouse Action Flags ---
    Mouse0 = 323  # Left click
    Mouse1 = 324  # Right click
    Mouse2 = 325  # Middle click
    Mouse3 = 326
    Mouse4 = 327
    Mouse5 = 328
    Mouse6 = 329

class ZombieAnimation:
    class NormalZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class FlagZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        FLAG = "flag"
        IDLE = "idle"
        WALK = "walk"

    class ConeZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class PolevaulterZombie(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_JUMP = "Zombie_polevaulter_jump"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"

    class BucketZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class PaperZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        WALK = "walk"
        WALK2 = "walk2"

    class DancePolZombie(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_JUMP_1 = "Zombie_polevaulter_jump 1"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"

    class DancePolZombie2(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_JUMP = "Zombie_polevaulter_jump"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"

    class DoorZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        LOSEWALK = "losewalk"
        LOSEWALK2 = "losewalk2"
        WALK = "walk"
        WALK2 = "walk2"

    class FootballZombie(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class JacksonZombie(Enum):
        ARMRAISE = "armraise"
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        MOONWALK = "moonwalk"
        POINT = "point"
        WALK = "walk"

    class ZombieDuck(Enum):
        ATTACK = "attack"
        ATTACK_WATER = "attack_water"
        DIE = "die"
        DROWNING = "drowning"
        IDLE = "idle"
        SWIM = "swim"
        WALK = "walk"
        WALK2 = "walk2"
        WATER = "water"

    class ConeZombieDuck(Enum):
        ATTACK = "attack"
        ATTACK_WATER = "attack_water"
        DIE = "die"
        DROWNING = "drowning"
        IDLE = "idle"
        SWIM = "swim"
        WALK = "walk"
        WALK2 = "walk2"
        WATER = "water"

    class BucketZombieDuck(Enum):
        ATTACK = "attack"
        ATTACK_WATER = "attack_water"
        DIE = "die"
        DROWNING = "drowning"
        IDLE = "idle"
        SWIM = "swim"
        WALK = "walk"
        WALK2 = "walk2"
        WATER = "water"

    class SubmarineZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class ElitePaperZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        WALK = "walk"
        WALK2 = "walk2"

    class DriverZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"

    class SnorkleZombie(Enum):
        BACKTOSWIM = "backtoswim"
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        SWIM = "swim"
        UPTOEAT = "uptoeat"
        WATER = "water"

    class SuperDriver(Enum):
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"

    class Dolphinrider(Enum):
        DIE = "die"
        DOLPHINJUMP = "dolphinjump"
        EAT = "eat"
        IDLE = "idle"
        RIDE = "ride"
        SWIM = "swim"
        WATER = "water"

    class DrownZombie(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"
        THROW = "throw"

    class DollDiamond(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class DollGold(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class DollSilver(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class JackboxZombie(Enum):
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        POP = "pop"
        WALK = "walk"

    class BalloonZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        FALL = "fall"
        FLY = "fly"
        IDLE = "idle"
        PROPELLER = "propeller"
        WALK = "walk"

    class KirovZombie(Enum):
        CRASH = "crash"
        IDLE = "idle"
        THROW = "throw"

    class SnowDolphinrider(Enum):
        DIE = "die"
        DOLPHINJUMP = "dolphinjump"
        EAT = "eat"
        IDLE = "idle"
        RIDE = "ride"
        SWIM = "swim"
        WATER = "water"

    class MinerZombie(Enum):
        DEATH = "death"
        DIG = "dig"
        DIZZY = "dizzy"
        EAT = "eat"
        IDLE = "idle"
        LANDING = "landing"
        LANDING_1 = "landing 1"
        WALK = "walk"

    class IronBalloonZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        FALL = "fall"
        FLY = "fly"
        IDLE = "idle"
        PETALS = "petals"
        WALK = "walk"

    class SuperJackboxZombie(Enum):
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        POP = "pop"
        WALK = "walk"

    class CatapultZombie(Enum):
        CRANK = "crank"
        IDLE = "idle"
        REST = "rest"
        SHAKE = "shake"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class PogoZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        WALK = "walk"

    class LadderZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        SET = "set"
        WALK = "walk"
        WALK2 = "walk2"

    class SuperPogoZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        JUMP2 = "jump2"
        WALK = "walk"

    class Gargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class RedGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class ImpZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        LAND = "land"
        THROWN = "thrown"
        WALK = "walk"

    class IronGargantuar(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class IronRedGargantuar(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class MachineNutZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class SilverZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class GoldZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class SuperGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class ZombieBoss(Enum):
        RV_LEG = "RV_leg"
        BUNGEE_1_ENTER = "bungee_1_enter"
        BUNGEE_1_LEAVE = "bungee_1_leave"
        DEATH = "death"
        ENTER = "enter"
        HEAD_ATTACK_1 = "head_attack_1"
        HEAD_ATTACK_2 = "head_attack_2"
        HEAD_ATTACK_3 = "head_attack_3"
        HEAD_ATTACK_4 = "head_attack_4"
        HEAD_ATTACK_5 = "head_attack_5"
        HEAD_ENTER = "head_enter"
        HEAD_IDLE = "head_idle"
        HEAD_LEAVE = "head_leave"
        IDLE = "idle"
        SPAWN_1 = "spawn_1"
        SPAWN_2 = "spawn_2"
        SPAWN_3 = "spawn_3"
        SPAWN_4 = "spawn_4"
        SPAWN_5 = "spawn_5"
        STOMP_1 = "stomp_1"
        STOMP_2 = "stomp_2"
        STOMP_3 = "stomp_3"
        STOMP_4 = "stomp_4"

    class BungiZombie(Enum):
        ATTACK = "attack"
        IDLE = "idle"
        SETZOMBIE = "setzombie"

    class ZombieBoss2(Enum):
        RV_LEG = "RV_leg"
        BUNGEE_1_ENTER = "bungee_1_enter"
        BUNGEE_1_LEAVE = "bungee_1_leave"
        DEATH = "death"
        ENTER = "enter"
        HEAD_ATTACK_1 = "head_attack_1"
        HEAD_ATTACK_2 = "head_attack_2"
        HEAD_ATTACK_3 = "head_attack_3"
        HEAD_ATTACK_4 = "head_attack_4"
        HEAD_ATTACK_5 = "head_attack_5"
        HEAD_ENTER = "head_enter"
        HEAD_IDLE = "head_idle"
        HEAD_LEAVE = "head_leave"
        IDLE = "idle"
        SPAWN_1 = "spawn_1"
        SPAWN_2 = "spawn_2"
        SPAWN_3 = "spawn_3"
        SPAWN_4 = "spawn_4"
        SPAWN_5 = "spawn_5"
        STOMP_1 = "stomp_1"
        STOMP_2 = "stomp_2"
        STOMP_3 = "stomp_3"
        STOMP_4 = "stomp_4"

    class SnowZombie(Enum):
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class NewYearZombie(Enum):
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class SnowGunZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        RUN = "run"
        SHOOT = "shoot"

    class SnowShieldZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        REBOUND = "rebound"
        WALK = "walk"
        WALK2 = "walk2"

    class SnowDrownZombie(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"
        THROW = "throw"

    class ProtalZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        LOSEWALK2 = "losewalk2"
        SHOOT = "shoot"
        WALK2 = "walk2"

    class LevatationZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class TrainingDummy(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class SnowConeZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class SnowMonsterZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        WALK = "walk"

    class SuperSnowMonsterZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        WALK = "walk"

    class PickaxeZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class DolphinPaper(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        WALK = "walk"
        WALK2 = "walk2"

    class FootballDolphin(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class MiniSnowMonster(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class GoldBungiZombie(Enum):
        ATTACK = "attack"
        IDLE = "idle"
        SETZOMBIE = "setzombie"

    class SandJackson(Enum):
        ARMRAISE = "armraise"
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        MOONWALK = "moonwalk"
        POINT = "point"
        WALK = "walk"

    class StoneDancer(Enum):
        IDLE = "idle"
        WALK = "walk"

    class FlagFootball(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        ROLL = "roll"
        WALK = "walk"

    class MiniSandMonster(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class ChickenImp(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class HorseZombie(Enum):
        DIE = "die"
        HIT = "hit"
        IDLE = "idle"
        IDLE_1 = "idle_1"
        WAITING = "waiting"
        WALK = "walk"

    class SuperHorse(Enum):
        DIE = "die"
        FLAGUP = "flagup"
        HIT = "hit"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class BoatImp(Enum):
        IDLE = "idle"
        POP = "pop"
        WALK = "walk"
        WATER = "water"

    class SuperLadderZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        SET = "set"
        WALK = "walk"
        WALK2 = "walk2"

    class EndoFlameZombie(Enum):
        ENTER = "enter"
        IDLE = "idle"

    class HypnoJalapenoZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class HypnoJalapenoPickaxeZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        DIG = "dig"
        IDLE = "idle"
        RISE_HYPNO = "rise_hypno"
        WALK = "walk"

    class DrownGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"
        WATER = "water"

    class SuperPolevaulter(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"
        JUMP = "jump"

    class WhiteFootball(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class YellowFootball(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class PortalPolevaulter(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_JUMP = "Zombie_polevaulter_jump"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"

    class CoachPaper(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        WALK = "walk"
        WALK2 = "walk2"

    class BucketPaper(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        WALK = "walk"
        WALK2 = "walk2"

    class PenguinZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        SKATING = "skating"
        WALK = "walk"

    class SnowNormalZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class SnowBucketZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class SuperPenguinZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        SKATING = "skating"
        WALK = "walk"

    class IronConeZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class ElephantZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class ZombieLoonNut(Enum):
        IDLE = "idle"
        WALK = "walk"

    class RedZombieLoonNut(Enum):
        IDLE = "idle"
        WALK = "walk"

    class PolFootballZombie(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        JUMP = "jump"
        WALK = "walk"
        WALK2 = "walk2"

    class PeaShooterZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK2 = "walk2"

    class CherryShooterZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK2 = "walk2"

    class SuperCherryShooterZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK2 = "walk2"

    class WallNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class CherryPaperZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class RandomZombie(Enum):
        ATTACK = "attack"
        ATTACK_WATER = "attack_water"
        DIE = "die"
        DROWNING = "drowning"
        IDLE = "idle"
        SWIM = "swim"
        WALK = "walk"
        WALK2 = "walk2"
        WATER = "water"

    class BucketNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class CherryNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class IronPeaZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK2 = "walk2"

    class TallNutFootballZombie(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class RandomPlusZombie(Enum):
        ATTACK = "attack"
        ATTACK_WATER = "attack_water"
        DIE = "die"
        DROWNING = "drowning"
        IDLE = "idle"
        SWIM = "swim"
        WALK = "walk"
        WALK2 = "walk2"
        WATER = "water"

    class TallIceNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class CherryCatapultZombie(Enum):
        CRANK = "crank"
        IDLE = "idle"
        REST = "rest"
        SHAKE = "shake"
        SHOOT = "shoot"
        SHOOT2 = "shoot2"
        WALK = "walk"
        WALK1 = "walk1"
        WALK2 = "walk2"

    class DolphinPeaZombie(Enum):
        DIE = "die"
        DOLPHINJUMP = "dolphinjump"
        EAT = "eat"
        IDLE = "idle"
        RIDE = "ride"
        SHOOT = "shoot"
        SWIM = "swim"
        WATER = "water"

    class IronPeaDoorZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        LOSEWALK = "losewalk"
        SHOOT = "shoot"
        WALK = "walk"

    class SquashZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK2 = "walk2"

    class JalaSquashZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK2 = "walk2"

    class JalapenoZombie(Enum):
        ATTACK = "attack"
        ATTACK_LOSE = "attack_lose"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class GatlingFootballZombie(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class IronBalloonZombie2(Enum):
        ATTACK = "attack"
        DIE = "die"
        FALL = "fall"
        FLY = "fly"
        IDLE = "idle"
        PETALS = "petals"
        SHOOT = "shoot"
        WALK = "walk"

    class DoomZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class RandomGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class BlueGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class GreenGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class YellowGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class Zombie9527(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"

    class TallFireNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class ObsidianTallNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class SunNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class SuperSunNutZombie(Enum):
        ATTACKW = "attackW"
        DIE = "die"
        IDLEW = "idleW"
        WALK2W = "walk2W"

    class GatlingPeaZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK2 = "walk2"

    class SnowGatlingPeaZombie(Enum):
        ATTACK_SNOW = "attack_snow"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK2 = "walk2"

    class BedRockSnowZombie(Enum):
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class SqualourZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        WALK2 = "walk2"

    class SuperSubmarine(Enum):
        IDLE = "idle"
        MOVE = "move"
        WATER = "water"

    class JacksonDriver(Enum):
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"

    class FootballDrown(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"
        THROW = "throw"

    class CherryPaperZ95(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class BlackFootball(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class SuperKirov(Enum):
        CRASH = "crash"
        IDLE = "idle"
        THROW = "throw"

    class SuperBombThrower(Enum):
        CRASH = "crash"
        IDLE = "idle"
        LEVITATION = "levitation"
        THROW = "throw"

    class QuickJacksonZombie(Enum):
        ARMRAISE = "armraise"
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        MOONWALK = "moonwalk"
        POINT = "point"
        WALK = "walk"

    class QingZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"
        WALK = "walk"

    class JackboxJumpZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        JUMP2 = "jump2"
        WALK = "walk"

    class SuperMachineNutZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class LandSubmarine(Enum):
        IDLE_LAND = "idle_land"
        MOVE_LAND = "move_land"

    class UltimateGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class ObsidianImpZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"
        WALK2 = "walk2"

    class DolphinGatlingZombie(Enum):
        DIE = "die"
        DOLPHINJUMP = "dolphinjump"
        EAT = "eat"
        IDLE = "idle"
        RIDE = "ride"
        SHOOT = "shoot"
        SWIM = "swim"
        WATER = "water"

    class DiamondRandomZombie(Enum):
        ATTACK = "attack"
        ATTACK_WATER = "attack_water"
        DIE = "die"
        DROWNING = "drowning"
        IDLE = "idle"
        SWIM = "swim"
        WALK = "walk"
        WALK2 = "walk2"
        WATER = "water"

    class DrownpultZombie(Enum):
        ATTACK = "attack"
        CRASH = "crash"
        IDLE = "idle"
        RELOAD = "reload"
        SHACK = "shack"
        WALK = "walk"
        WALK2 = "walk2"

    class SuperDancePolZombie(Enum):
        ZOMBIE_POLEVAULTER_DIE = "Zombie_polevaulter_die"
        ZOMBIE_POLEVAULTER_EAT = "Zombie_polevaulter_eat"
        ZOMBIE_POLEVAULTER_IDLE = "Zombie_polevaulter_idle"
        ZOMBIE_POLEVAULTER_JUMP_1 = "Zombie_polevaulter_jump 1"
        ZOMBIE_POLEVAULTER_RUN = "Zombie_polevaulter_run"
        ZOMBIE_POLEVAULTER_WALK = "Zombie_polevaulter_walk"

    class UltimateFootballDrown(Enum):
        BAJIAN = "Bajian"
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"

    class UltimateMachineNutZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class UltimateFootballZombie(Enum):
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        WALK = "walk"

    class UltimateKirovZombie(Enum):
        IDLE = "Idle"
        QIFEI = "Qifei"
        FLYING = "flying"
        SHOOT = "shoot"
        WALK = "walk"

    class UltimateJacksonDriver(Enum):
        IDLE_CAR = "idle car"

    class UltimatePaperZombie(Enum):
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        SHOOT = "shoot"
        SHOOTBACK = "shootback"
        STOPWALKING = "stopwalking"
        USE = "use"
        WALK = "walk"
        WALK2 = "walk2"

    class UltimateJackboxZombie(Enum):
        IDLE = "idle"
        SUOHUI = "suohui"
        TIAOCHU = "tiaochu"
        WALK = "walk"

    class GatlingBlackFootball(Enum):
        DIE = "die"
        EAT_BLACK = "eat_black"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK_BLACK = "walk_black"

    class LegionZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        FAKEDIE = "fakedie"
        IDLE = "idle"
        QUICKMOVE = "quickmove"
        WALK = "walk"

    class IceClawZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class UltimateSnowZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        ATTACK3 = "attack3"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class UltimateHorse(Enum):
        FLAGUP = "flagup"
        HIT = "hit"
        HIT2 = "hit2"
        IDLE = "idle"
        RUN = "run"
        SHOOT = "shoot"
        TOHORSE = "tohorse"
        WALK = "walk"

    class UltimateHorse2(Enum):
        ATTACK = "attack"
        DIE = "die"
        EAT = "eat"
        IDLE = "idle"
        JUMP = "jump"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class HorseBoss(Enum):
        CHARGEBACK = "chargeBack"
        CHARGEFORWARD = "chargeForward"
        DIE = "die"
        ENTER = "enter"
        FLAG3 = "flag3"
        FLAGUP = "flagup"
        FLAGUP2 = "flagup2"
        IDLE = "idle"
        JUMP = "jump"
        RISE = "rise"

    class SummonedHorse(Enum):
        DIE = "die"
        IDLE = "idle"
        RUN = "run"

    class ArmedGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        JUMPATTACK = "jumpAttack"
        WALK = "walk"

    class UltimateImpKing(Enum):
        DIE = "die"
        IDLE = "idle"
        LANDDIE = "landdie"
        LANDWALK = "landwalk"
        WALK = "walk"
        WATER = "water"

    class ImpKing(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        LAND = "land"
        THROWN = "thrown"
        WALK = "walk"

    class SuperLevatation(Enum):
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class CherrySubmarine(Enum):
        IDLE = "idle"
        MOVE = "move"
        WATER = "water"

    class SnowMonsterRider(Enum):
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        WALK = "walk"

    class WaterJackboxJumpZombie(Enum):
        IDLE = "idle"
        WALK = "walk"
        WATER = "water"

    class UltiWaterGargantuar(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        THROW = "throw"
        WALK = "walk"
        WATER = "water"

    class UltimateGoldGargantuar(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        RISE = "rise"
        WALK = "walk"

    class DoomPaper(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class UltimateLegionZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        FAKEDIE = "fakedie"
        IDLE = "idle"
        QUICKMOVE = "quickmove"
        WALK = "walk"

    class UltimateSwordZombie(Enum):
        DIE = "die"
        DRAGON = "dragon"
        ENTER = "enter"
        IDLE = "idle"
        IDLE1TO2 = "idle1to2"
        IDLE2 = "idle2"
        IDLE2TO3 = "idle2to3"
        IDLE3 = "idle3"
        IDLE_DRAGON = "idle_dragon"
        SKILL = "skill"

    class MachineLevatation(Enum):
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class LegionSniperZombie(Enum):
        DIE = "die"
        IDLE = "idle"
        PRESHOOT = "preshoot"
        SHOOT = "shoot"
        WALK = "walk"

    class VoodooDollZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class ObsidianClawZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class UltimateDolphin(Enum):
        JUMP = "Jump"
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class PortalBalloonZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        FALL = "fall"
        FLY = "fly"
        IDLE = "idle"
        PETALS = "petals"
        WALK = "walk"

    class BlackHorse(Enum):
        HIT = "hit"
        HIT2 = "hit2"
        IDLE = "idle"
        RUN = "run"
        WALK = "walk"

    class SuperBlackHorse(Enum):
        BLACKSHOOT = "blackshoot"
        FLAGUP = "flagup"
        HIT = "hit"
        IDLE = "idle"
        WALK = "walk"

    class BlackJackboxZombie(Enum):
        DEATH = "death"
        EAT = "eat"
        IDLE = "idle"
        POP = "pop"
        THROW = "throw"
        WALK = "walk"

    class BlackElephantZombie(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class BlackTrainZombie(Enum):
        IDLE = "idle"
        WALK = "walk"

    class BlackFlagFootball(Enum):
        DIE = "die"
        EAT_BLACK = "eat_black"
        IDLE = "idle"
        ROLL = "roll"
        WALK_BLACK = "walk_black"

    class SuperBlackFootball(Enum):
        DIE = "die"
        EAT_BLACK = "eat_black"
        IDLE = "idle"
        ROLL = "roll"
        WALK_BLACK = "walk_black"

    class ArmoredImpZombie(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class UltimateEndoflameZombie(Enum):
        BLOOM = "bloom"
        BLOOMED = "bloomed"
        BUD = "bud"
        BUDED = "buded"
        DIE = "die"
        FIRE = "fire"
        FLOWER = "flower"
        IDLE = "idle"
        OPENFIRE = "openFire"

    class FootballBoss(Enum):
        DIE = "die"
        ENTER = "enter"
        ENTER2 = "enter2"
        IDLE = "idle"
        JUMP = "jump"
        LAND = "land"
        ROLL = "roll"
        WALK = "walk"

    class JacksonDriverBoss(Enum):
        IDLE = "idle"
        WALK = "walk"

    class GatlingPaper_a(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class GatlingPaper_b(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class GatlingPaper_c(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        LOSEPAPER = "losePaper"
        SHOOT = "shoot"
        SHOOT_GUN = "shoot_gun"
        TAKEGUN = "takeGun"
        WALK = "walk"
        WALK2 = "walk2"

    class BlackFootball_a(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class BlackFootball_b(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class BlackFootball_c(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class BlackFootball_c2(Enum):
        DIE = "die"
        EAT_BLACK = "eat_black"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK_BLACK = "walk_black"

    class Jackson_a(Enum):
        ARMRAISE = "armraise"
        ATTACK = "attack"
        DEATH = "death"
        IDLE = "idle"
        MOONWALK = "moonwalk"
        POINT = "point"
        WALK = "walk"

    class Jackson_b(Enum):
        ARMRAISE = "armraise"
        ATTACK = "attack"
        DEATH = "death"
        IDLE = "idle"
        MOONWALK = "moonwalk"
        POINT = "point"
        WALK = "walk"

    class Jackson_c(Enum):
        ARMRAISE = "armraise"
        ATTACK = "attack"
        DEATH = "death"
        IDLE = "idle"
        MOONWALK = "moonwalk"
        POINT = "point"
        WALK = "walk"

    class Submarine_a(Enum):
        IDLE = "idle"
        MOVE = "move"
        SHOOT = "shoot"
        WATER = "water"

    class Submarine_b(Enum):
        IDLE = "idle"
        MOVE = "move"
        SHOOT = "shoot"
        WATER = "water"

    class Submarine_b2(Enum):
        IDLE = "idle"
        MOVE = "move"
        SHOOT = "shoot"
        WATER = "water"

    class Submarine_c(Enum):
        IDLE = "idle"
        MOVE = "move"
        RAISED = "raised"
        RISE = "rise"
        SHOOT = "shoot"
        SUB = "sub"
        WATER = "water"

    class Submarine_c2(Enum):
        IDLE = "idle"
        MOVE = "move"
        SHOOT = "shoot"
        WATER = "water"

    class Drown_a(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        RUN = "run"
        SHOOT = "shoot"
        WALK = "walk"

    class Drown_b(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class Drown_c(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"
        WALK2 = "walk2"

    class Pickaxe_a(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class Pickaxe_b(Enum):
        ATTACK = "attack"
        DIE = "die"
        DIG = "dig"
        IDLE = "idle"
        RISE = "rise"
        WALK = "walk"

    class Pickaxe_c(Enum):
        ATTACK = "attack"
        DIE = "die"
        DIG = "dig"
        IDLE = "idle"
        RISE = "rise"
        WALK = "walk"

    class Driver_a(Enum):
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"
        WALK = "walk"

    class Driver_b(Enum):
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"
        WALK = "walk"

    class Driver_c(Enum):
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"
        WALK = "walk"

    class Jackbox_a(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        JUMP2 = "jump2"
        WALK = "walk"

    class Jackbox_b(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        JUMP2 = "jump2"
        WALK = "walk"

    class Jackbox_c(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        JUMP = "jump"
        JUMP2 = "jump2"
        WALK = "walk"

    class Kirov_a(Enum):
        CRASH = "crash"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class Kirov_b(Enum):
        CRASH = "crash"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class Kirov_c(Enum):
        CRASH = "crash"
        FLAME = "flame"
        IDLE = "idle"
        SHOOT = "shoot"
        WALK = "walk"

    class EternalZombie_a(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"
        WALK = "walk"

    class EternalZombie_b(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"
        WALK = "walk"

    class EternalZombie_c(Enum):
        ATTACK = "attack"
        DIE = "die"
        IDLE = "idle"
        SHAKE = "shake"
        SKILL = "skill"
        SKILLING = "skilling"
        WALK = "walk"

    class Drownpult_a(Enum):
        ATTACK = "attack"
        CRASH = "crash"
        IDLE = "idle"
        RELOAD = "reload"
        SHACK = "shack"
        WALK = "walk"
        WALK2 = "walk2"

    class Drownpult_b(Enum):
        ATTACK = "attack"
        CRASH = "crash"
        IDLE = "idle"
        RELOAD = "reload"
        SHACK = "shack"
        WALK = "walk"
        WALK2 = "walk2"

    class Drownpult_c(Enum):
        ATTACK = "attack"
        CRASH = "crash"
        IDLE = "idle"
        RELOAD = "reload"
        SHACK = "shack"
        WALK = "walk"
        WALK2 = "walk2"

    class ElephantZombie_a(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class ElephantZombie_b(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"

    class ElephantZombie_c(Enum):
        ATTACK = "attack"
        ATTACK2 = "attack2"
        DIE = "die"
        IDLE = "idle"
        WALK = "walk"


class TravelBuffType(Enum):
    ADV_ENCHANTRESS_SUBSPECIES = ("AdvBuff", 0)
    ADV_ENCHANTRESS_ODYSSEY = ("AdvBuff", 1)
    ADV_GATLING_FRENZY_NO_REST = ("AdvBuff", 2)
    ADV_GATLING_FRENZY_EVERY_4 = ("AdvBuff", 3)
    ADV_TWIN_SOLAR_REDUCE_COST = ("AdvBuff", 4)
    ADV_TWIN_INFERNO_SUBSPECIES = ("AdvBuff", 5)
    ADV_OBSIDIAN_SPIKE_DAMAGE = ("AdvBuff", 6)
    ADV_OBSIDIAN_SPIKE_REDUCTION = ("AdvBuff", 7)
    ADV_PHOENIX_DRONE_SUBSPECIES = ("AdvBuff", 8)
    ADV_PHOENIX_THREEPEATER_BUFF = ("AdvBuff", 9)
    ADV_GATLING_ICICLE_PIERCE = ("AdvBuff", 10)
    ADV_GATLING_SUNBURST_SUBSPECIES = ("AdvBuff", 11)
    ADV_RADIANT_POT_GOLDEN_LIMIT = ("AdvBuff", 12)
    ADV_RADIANT_POT_COIN_CONVERSION = ("AdvBuff", 13)
    ADV_AEGIS_UMBRELLA_AUTO = ("AdvBuff", 14)
    ADV_MIDAS_UMBRELLA_BOOST = ("AdvBuff", 15)
    ADV_ARISTOCATTAIL_DRONE_DMG = ("AdvBuff", 16)
    ADV_THUNDER_BUNNYON_SUBSPECIES = ("AdvBuff", 17)
    ADV_AVARICE_SHROOM_CRATERLESS = ("AdvBuff", 18)
    ADV_CALAMITY_SHROOM_SPAWNS = ("AdvBuff", 19)
    ADV_TYCOONWOOD_COIN_LASER = ("AdvBuff", 20)
    ADV_MAGNATE_PLANTERN_SUBSPECIES = ("AdvBuff", 21)
    ADV_PHAROS_UMBRELLA_LIMIT = ("AdvBuff", 22)
    ADV_BOREAS_UMBRELLA_CRYOBEAM = ("AdvBuff", 23)
    ADV_BUCK_SHROOM_HEADSHOT = ("AdvBuff", 24)
    ADV_BUCK_STRIKE_SUBSPECIES = ("AdvBuff", 25)
    ADV_TESLA_MAGNET_RANGE = ("AdvBuff", 26)
    ADV_DYSON_MAGNET_LIMIT = ("AdvBuff", 27)
    ADV_GRIM_ARBITER_GUARANTEED = ("AdvBuff", 28)
    ADV_WICKED_UNDERTAKER_SOUL = ("AdvBuff", 29)
    ADV_BIG_BANG_SOUP_DURATION = ("AdvBuff", 30)
    ADV_BIG_CRUNCH_SUBSPECIES = ("AdvBuff", 31)
    ADV_CORNVEYOR_WEED_BUTTER = ("AdvBuff", 32)
    ADV_CORNPOSTER_POT_CHANCE = ("AdvBuff", 33)
    ADV_OMNI_PUMPKIN_SHIELD = ("AdvBuff", 34)
    ADV_QUASAR_MAGNETIC_COUNT = ("AdvBuff", 35)
    ADV_DRAGONBREATH_FREQUENCY = ("AdvBuff", 36)
    ADV_DRAGONBREATH_STACKING = ("AdvBuff", 37)
    ADV_TUNDRAL_GLACIER_ENERGY = ("AdvBuff", 38)
    ADV_LETHAL_GLACIER_SUBSPECIES = ("AdvBuff", 39)
    ADV_MESMER_CATTAIL_RADIUS = ("AdvBuff", 40)
    ADV_MESMER_CATTAIL_TRUE_DMG = ("AdvBuff", 41)
    
    # General & Utility Modifiers (1000+)
    ADV_GLOVE_COOLDOWN_REDUCED = ("AdvBuff", 1000)
    ADV_PLANT_RECHARGE_HALVED = ("AdvBuff", 1001)
    ADV_SUN_VALUE_UPGRADE = ("AdvBuff", 1002)
    ADV_GLOVE_HALF_CD = ("AdvBuff", 1003)
    ADV_IMITATER_FAST_RECHARGE = ("AdvBuff", 1004)
    ADV_MALLET_CD_REDUCED = ("AdvBuff", 1005)
    ADV_MID_GAME_LOADOUT_REPICK = ("AdvBuff", 1006)
    ADV_MASSIVE_DAMAGE_PROC = ("AdvBuff", 1007)
    ADV_PLANT_DMG_BOOST_20 = ("AdvBuff", 1008)
    ADV_ZOMBIE_RECEIVE_MORE_DMG = ("AdvBuff", 1009)
    ADV_MODIFIER_REROLL_PLUS_2 = ("AdvBuff", 1010)
    ADV_FREEZE_TIME_INCREASED = ("AdvBuff", 1011)
    ADV_DOUBLE_SUN_CAP_100K = ("AdvBuff", 1012)
    ADV_TRUE_CHERRY_CREMATOR = ("AdvBuff", 1013)
    ADV_GLOVE_DISASSEMBLE_PLANT = ("AdvBuff", 1014)
    ADV_VERTICAL_STACK_BONUS = ("AdvBuff", 1015)
    ADV_HYPNO_ZOMBIE_MASSIVE_BUFF = ("AdvBuff", 1016)
    ADV_METEOR_CD_HALVED = ("AdvBuff", 1017)
    ADV_ADD_4_LUMOS_LEVELS = ("AdvBuff", 1018)
    ADV_HYPNO_DEATH_EXPLOSION = ("AdvBuff", 1019)
    ADV_HEAL_REGENERATION_BUFF = ("AdvBuff", 1020)
    ADV_PLANT_HEALING_BONUS_20 = ("AdvBuff", 1021)

    # Masteries & Epic Synergies (2000+ / 3000+)
    ADV_TRUE_DOOM_SHROOM = ("AdvBuff", 2000)
    ADV_COLUMN_PLANTING_ENABLED = ("AdvBuff", 2001)
    ADV_UPGRADE_EPIC_MODIFIER = ("AdvBuff", 2002)
    ADV_TOP_DAMAGE_TRUE_DAMAGE = ("AdvBuff", 2003)
    ADV_UNLIMITED_ATTACK_SPEED_1S = ("AdvBuff", 2004)
    ADV_PLANT_LIFE_STEAL_1 = ("AdvBuff", 2005)
    ADV_DAMAGE_DELAY_SCALING = ("AdvBuff", 2006)
    ADV_CORRUPT_SAC_EFFECT = ("AdvBuff", 2007)
    ADV_REMOVE_NON_MINIBOSS_MOD = ("AdvBuff", 2008)

    ADV_SYNERGY_CHERRIZILLA_OBSIDIAN = ("AdvBuff", 3000)
    ADV_SYNERGY_MAGNETAR_HELIOS = ("AdvBuff", 3001)
    ADV_SYNERGY_CHERRYBOMBER_SINE = ("AdvBuff", 3002)
    ADV_SYNERGY_MAGNETAR_SELENE = ("AdvBuff", 3003)
    ADV_SYNERGY_MAELONSTROM_QUANTUM = ("AdvBuff", 3004)
    ADV_SYNERGY_VULCANNON_INFERNO = ("AdvBuff", 3005)
    ADV_SYNERGY_CHERRYBOMBER_GATLING = ("AdvBuff", 3006)
    ADV_SYNERGY_PHOTON_ATOMHEART = ("AdvBuff", 3007)
    ADV_SYNERGY_LITTERPULT_ICICLE = ("AdvBuff", 3008)
    ADV_SYNERGY_DOOMINATOR_NAPALM = ("AdvBuff", 3009)

    # Summoned Pets (4000+)
    ADV_PET_ABYSSAL_CHIBI = ("AdvBuff", 4000)
    ADV_PET_STRIKER_JUNIOR = ("AdvBuff", 4001)
    ADV_PET_PROTOTYPE_ICEBORG = ("AdvBuff", 4002)
    ADV_PET_BABY_JILL = ("AdvBuff", 4003)
    ADV_PET_MINI_POZEIDON = ("AdvBuff", 4004)
    ADV_PET_YOUNG_DUKE = ("AdvBuff", 4005)
    ADV_PET_IMPEROR_HATCHLING = ("AdvBuff", 4006)
    ADV_PET_SKYGLIDER_MECHA = ("AdvBuff", 4007)

    # Risk-Reward / General Boss Modifiers (5000+ / 6000+)
    ADV_BOSS_DAMAGE_BONUS_100 = ("AdvBuff", 5000)
    ADV_PLANT_DMG_PER_MODIFIER = ("AdvBuff", 5001)
    ADV_UNLOCK_SWORDSAGE_STARFRUIT = ("AdvBuff", 5002)
    ADV_GLASS_CANNON_MODIFIER = ("AdvBuff", 5003)
    ADV_SEED_PACKET_SUN_TAX = ("AdvBuff", 5004)
    
    ADV_LAWNMOWER_MAXIMUM_MASTERY = ("AdvBuff", 6000)
    ADV_CHERRIZILLA_MASTERY_HEAL = ("AdvBuff", 6001)
    ADV_CHERRIZILLA_MASTERY_DMG = ("AdvBuff", 6002)
    ADV_GATLING_CHERRY_MASTERY_RADIUS = ("AdvBuff", 6003)
    ADV_GATLING_CHERRY_MASTERY_DMG = ("AdvBuff", 6004)
    ADV_DOOMINATOR_MASTERY_FROZEN = ("AdvBuff", 6005)
    ADV_DOOMINATOR_MASTERY_HYPNO = ("AdvBuff", 6006)
    ADV_INFERNAL_SQUASH_MASTERY_DOT = ("AdvBuff", 6007)
    ADV_INFERNAL_SQUASH_MASTERY_BUFF = ("AdvBuff", 6008)
    ADV_FIFTH_COLUMN_TOUGHNESS = ("AdvBuff", 6009)

    # Instant Legendary Artifacts (10000+)
    ADV_INSTANT_100K_SUN = ("AdvBuff", 10000)
    ADV_INSTANT_GIGA_MECHA_NUT = ("AdvBuff", 10001)
    ADV_INSTANT_TIER_1_UPGRADE = ("AdvBuff", 10002)
    ADV_INSTANT_PLANT_SPEEDRUN = ("AdvBuff", 10003)
    ADV_UNDYING_TOTEM_ACQUIRED = ("AdvBuff", 10004)
    ADV_EPIC_PUMPKIN_STORAGE = ("AdvBuff", 10005)
    ADV_FULL_BOARD_CLEAR_KNOCKBACK = ("AdvBuff", 10006)
    ADV_SUPER_BLIZZARD_COMMANDO = ("AdvBuff", 10007)
    ADV_EVOLVING_ODYSSEY_PLANT = ("AdvBuff", 10008)
    ADV_SHROOMAGEDDON_CHALLENGE = ("AdvBuff", 10009)
    ADV_GLOBAL_PLANT_DMG_X2 = ("AdvBuff", 10010)
    ADV_REGENERATING_SHIELD = ("AdvBuff", 10011)
    ADV_SAURIAN_MEDALLION = ("AdvBuff", 10012)
    ADV_OMNI_PUMPKIN_CHALLENGE = ("AdvBuff", 10013)
    ADV_LAWNMOWER_RESTORATION = ("AdvBuff", 10014)
    ADV_LAST_SECOND_HOUSE_SAVE = ("AdvBuff", 10015)
    ADV_IMMEDIATE_5_IMITATERS = ("AdvBuff", 10016)
    ADV_DUPLICATE_COPY_BONUS = ("AdvBuff", 10017)
    ADV_GLOVE_MERGE_UPGRADE = ("AdvBuff", 10018)
    ADV_GOLDEN_RECYCLING_VASES = ("AdvBuff", 10019)

    # Cooldown Modifiers (11000+)
    ADV_WHEELBARROW_CD_REDUCED = ("AdvBuff", 11000)

    # Ultimate Attack Enhancements (12000+)
    ADV_NAPALM_SHROOM_SEA_OF_FIRE = ("AdvBuff", 12000)
    ADV_APEACALYPSE_FROSTFLAME = ("AdvBuff", 12001)
    ADV_BERSERKER_SNIPEA_CRIT = ("AdvBuff", 12002)
    ADV_THREEPEATATO_MINE_EXPLODE = ("AdvBuff", 12003)
    ADV_DOOM_CHOMPER_EXPLOSIONS = ("AdvBuff", 12004)
    ADV_SHROOMAGEDDON_DEATH_DOOM = ("AdvBuff", 12005)

    # ==========================================
    # ULTIMATE BUFFS (UltiBuff)
    # ==========================================
    ULTI_CHERRIZILLA_RECOVERY = ("UltiBuff", 0)
    ULTI_CHERRIZILLA_DEVOUR_CD = ("UltiBuff", 1)
    ULTI_GATLING_CHERRY_EXPLOSION = ("UltiBuff", 2)
    ULTI_GATLING_CHERRY_SPEED = ("UltiBuff", 3)
    ULTI_DOOMINATOR_SPEED_X3 = ("UltiBuff", 4)
    ULTI_DOOMINATOR_UNFREEZE_DMG = ("UltiBuff", 5)
    ULTI_INFERNAL_SQUASH_SPICY_HALVED = ("UltiBuff", 6)
    ULTI_INFERNAL_SQUASH_AUTO_IGNITE = ("UltiBuff", 7)
    ULTI_MAGNETAR_INTERVAL_REDUCED = ("UltiBuff", 8)
    ULTI_MAGNETAR_CAP_REMOVED = ("UltiBuff", 9)

    # ==========================================
    # TRAVEL DEBUFFS (TravelDebuff)
    # ==========================================
    DEBUFF_SUN_RESET_TO_0 = ("TravelDebuff", 1000)
    DEBUFF_POINTS_RESET_TO_0 = ("TravelDebuff", 1001)
    DEBUFF_PLANT_LIMIT_120 = ("TravelDebuff", 1002)
    DEBUFF_PLANT_PERISH_CHANCE = ("TravelDebuff", 1003)
    DEBUFF_ZOMBIE_HP_INCREMENT_ROUND = ("TravelDebuff", 1004)
    DEBUFF_ZOMBIE_REVIVE_CHANCE = ("TravelDebuff", 1005)
    DEBUFF_PLANTS_COST_3X_SUN = ("TravelDebuff", 1010)
    DEBUFF_WAVE_INTERVAL_REDUCED = ("TravelDebuff", 1011)
    DEBUFF_PLANT_DEATH_AOE_SUICIDE = ("TravelDebuff", 1016)