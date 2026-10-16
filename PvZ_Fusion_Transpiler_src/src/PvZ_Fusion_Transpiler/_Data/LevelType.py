from enum import Enum


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
    

__all__ = ["LevelType"]
