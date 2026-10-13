"""
Level Board Tag schema matching Unity GameLevel boardTag.
Contains all 96 special mode toggles, mutators, and gameplay feature flags.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class BoardTag:
    waveLeaders: bool = False
    evolutionWar: bool = False
    rhythmGame: bool = False
    imZombieBoss: bool = False
    allScaryPotShow: bool = False
    customEdit: bool = False
    allCards: bool = False
    isIZ: bool = False
    HorseBoss: bool = False
    Iz_ai: bool = False
    rShowHealth: bool = False
    lessSun: bool = False
    lessMoney: bool = False
    zombieDropSun: bool = False
    disableNormalSun: bool = False
    zombieRevive: bool = False
    isScaredyDream: bool = False
    isTowerDefence: bool = False
    isShooting: bool = False
    rogueShooting: bool = False
    newShooting: bool = False
    isSeedRain: bool = False
    isIndestructible: bool = False
    isColumn: bool = False
    isSuperRandom: bool = False
    isNormalRandom: bool = False
    isElementRandom: bool = False
    isDrawCards: bool = False
    isUltimateSuperRandom: bool = False
    isNight: bool = False
    isBigMap: bool = False
    freeCamera: bool = False
    isEndless: bool = False
    isTravel: bool = False
    isEasyTravel: bool = False
    randomTravel: bool = False
    superCustomEditorMode: bool = False
    enableTravelPlant: bool = False
    enableAllTravelPlant: bool = False
    enableTravelBuff: bool = False
    isRoof: bool = False
    isGarden: bool = False
    isMirror: bool = False
    isConvey: bool = False
    isExchange: bool = False
    shooting_loon: bool = False
    isBoss: bool = False
    isBoss2: bool = False
    isFreeCardSelect: bool = False
    isTutor: bool = False
    isObsidianImp: bool = False
    isDixMix: bool = False
    isSingle: bool = False
    bungiBattle: bool = False
    isBejeweled: bool = False
    isBubbleGame: bool = False
    isScaryPot: bool = False
    isMidMap: bool = False
    isChess: bool = False
    isMidMap2: bool = False
    isLookStar: bool = False
    isGardenBattle: bool = False
    isRandomMix: bool = False
    isRandomMix2: bool = False
    freeGloveZombie: bool = False
    disableMower: bool = False
    isHappyRandom: bool = False
    oppsiteBuff: bool = False
    pvpScaryPot: bool = False
    pvpRandom: bool = False
    ultimateEndless: bool = False
    isHammerZombie: bool = False
    fastZombie: bool = False
    isHugeGravity: bool = False
    zombieSplit: bool = False
    fullStrike: bool = False
    billiardBall: bool = False
    isSnake: bool = False
    isSquash: bool = False
    zombieBattle: bool = False
    plantingZombie: bool = False
    is2048: bool = False
    isRogue: bool = False
    isFruitNinjia: bool = False
    isFruitNinjia2: bool = False
    lightShadow: bool = False
    isLoonGame: bool = False
    snowBoss: bool = False
    playerShooting: bool = False
    smallZombie: bool = False
    isFlagGame: bool = False
    isTreasure: bool = False
    isBrick: bool = False
    disableSummonZombie: bool = False
    disableSelectCard: bool = False
    disableInInterlude: bool = False

    def to_dict(self) -> Dict[str, bool]:
        """Serializes board tags to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> BoardTag:
        """Constructs BoardTag from raw dictionary."""
        field_names = set(cls.__dataclass_fields__.keys())
        filtered = {k: bool(v) for k, v in data.items() if k in field_names}
        return cls(**filtered)

    # =========================================================================
    # PRESET HELPERS
    # =========================================================================

    def enable_god_shooting(self) -> BoardTag:
        """Enables God Shooting / Player Shooting mode."""
        self.isShooting = True
        self.playerShooting = True
        return self

    def enable_rogue_shooting(self) -> BoardTag:
        """Enables Rogue-like shooting mode."""
        self.isShooting = True
        self.rogueShooting = True
        self.isRogue = True
        return self

    def enable_iz(self, ai: bool = False, boss: bool = False) -> BoardTag:
        """Enables I, Zombie (IZ) mode."""
        self.isIZ = True
        self.Iz_ai = ai
        self.imZombieBoss = boss
        return self

    def enable_endless(self, ultimate: bool = False) -> BoardTag:
        """Enables endless survival mode."""
        self.isEndless = True
        if ultimate:
            self.ultimateEndless = True
        return self

    def enable_travel(self, easy: bool = False, random: bool = False) -> BoardTag:
        """Enables travel / adventure mode with buffs and custom travel plants."""
        self.isTravel = True
        self.isEasyTravel = easy
        self.randomTravel = random
        self.enableTravelPlant = True
        self.enableAllTravelPlant = True
        self.enableTravelBuff = True
        return self
