from enum import Enum


class MusicType(Enum):
    """MusicType enum in PvZ Fusion."""

    MainMenu = 0
    SelectCard = 1
    Day = 2
    Day_drum = 3
    Night = 4
    Night_drum = 5
    Pool = 6
    Pool_drum = 7
    Fog = 8
    Fog_drum = 9
    Roof = 10
    Roof_drum = 11
    Roof_pre = 12
    Loon = 13
    UltimateBattle = 14
    IZ = 15
    Garden = 16
    Boss = 17
    Boss2 = 18
    Snow = 19
    Snow_drum = 20
    Snow_boss = 21
    RoofPool = 22
    RoofPool_drum = 23
    NightSnow = 24
    NightSnow_drum = 25
    HorseBoss = 26
    SeaBoss = 27


__all__ = ["MusicType"]
