from enum import Enum


class UltiBuff(Enum):
    """UltiBuff enum in PvZ Fusion (TypeDefIndex: 2758)."""

    嗜血如命 = 0
    极速吞噬 = 1
    力大砖飞 = 2
    快速填装 = 3
    凛风刺骨 = 4
    三尺之寒 = 5
    事半功倍 = 6
    窝红温了 = 7
    流星雨 = 8
    众星之力 = 9
    万籁俱寂 = 10
    以爆制爆 = 11
    见者有份 = 12
    蒜毒骤发 = 13
    中心爆破 = 14
    兵贵神速 = 15
    世纪之盾 = 16
    两肋插刀 = 17
    普度众生 = 18
    永动机 = 19
    阻冲之 = 20
    狂战士 = 21
    金光闪闪 = 22
    人造太阳 = 23
    三位一体 = 24
    镭射激光 = 25
    气定神闲 = 26
    僵尸试图在火海中游泳 = 27
    厚积薄发 = 28
    匣中惊喜 = 29
    无尽贪婪 = 30
    万劫不复 = 31
    延时飞刃 = 32
    生机永驻 = 33
    深渊巨口 = 34
    光芒四射 = 35
    爆米花 = 36
    超载 = 37
    连锁反应 = 38
    大容量 = 39
    集中轰炸 = 40
    聚精会神 = 41
    炙热射线 = 42
    三昧真火 = 43
    深海恐惧 = 44
    群体出动 = 45
    斩将祭旗 = 46
    黑曜护体 = 47
    蓄能帆 = 48
    能源补偿 = 49
    极速爆发 = 50
    精准射击 = 51
    堡垒1 = 52
    堡垒2 = 53
    究炉回韧 = 54
    究炉恢复 = 55

    # Aliases for backward compatibility
    ULTI_CHERRIZILLA_RECOVERY = 0
    ULTI_CHERRIZILLA_DEVOUR_CD = 1
    ULTI_GATLING_CHERRY_EXPLOSION = 2
    ULTI_GATLING_CHERRY_SPEED = 3
    ULTI_DOOMINATOR_SPEED_X3 = 4
    ULTI_DOOMINATOR_UNFREEZE_DMG = 5
    ULTI_INFERNAL_SQUASH_SPICY_HALVED = 6
    ULTI_INFERNAL_SQUASH_AUTO_IGNITE = 7
    ULTI_MAGNETAR_INTERVAL_REDUCED = 8
    ULTI_MAGNETAR_CAP_REMOVED = 9


__all__ = ["UltiBuff"]
