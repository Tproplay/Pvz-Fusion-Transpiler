from enum import Enum


class TravelBuffType(Enum):
    """Combined travel buff and debuff enumeration in PvZ Fusion."""

    # ==========================================
    # ADVANCED BUFFS (AdvBuff)
    # ==========================================
    CallToArms = ("AdvBuff", 0)
    """Call to Arms: Enchantress-shroom Subspecies Unlocked | Empress-shroom & Enchantress-shroom: Summon Interval 30s → 10s"""

    EliteCorps = ("AdvBuff", 1)
    """Elite Corps: Empress-shroom & Enchantress-shroom: Can now summon Odyssey Zombies"""

    Overclock = ("AdvBuff", 2)
    """Overclock: Gatling Frenzy-shroom Subspecies Unlocked | Gatling Doom: No more rest after firing an Ultimate Doom Shell | Effects also apply to SP variants"""

    Overkill = ("AdvBuff", 3)
    """Overkill: Gatling Doom: Now fires an Ultimate Doom Shell every round instead of every 4th round | Gatling Frenzy-shroom: Now fires an Ultimate Doom Shell every 4 attacks | Effects also apply to SP variants"""

    Photosynthesis = ("AdvBuff", 4)
    """Photosynthesis: Twin Solar-nut: Click Cost 500 → 200 Sun | Twin Inferno-nut: Healing amount ×2 | Effects also apply to SP variants"""

    Hematopoiesis = ("AdvBuff", 5)
    """Hematopoiesis: Twin Inferno-nut Subspecies Unlocked | Twin Solar-nut: Toughness reduces by 10 for each hit instead of 50 | Twin Inferno-nut: Click cost 500 → 200 HP | Effects also apply to SP variants"""

    PathOfPain = ("AdvBuff", 6)
    """Path of Pain: Obsidian Spike-nut Subspecies Unlocked | Obsidian Spikerock & Spike-nut: Damage multiplied by 5"""

    SkinOfSteel = ("AdvBuff", 7)
    """Skin of Steel: Obsidian Spikerock & Spike-nut: Gains 95% DMG Reduction"""

    PiercingFlame = ("AdvBuff", 8)
    """Piercing Flame: Phoenix Drone Subspecies Unlocked | Phoenix Threepeater & Phoenix Drone: Shots can now pierce infinitely and cause Enflamed explosions upon impact | Effects also apply to SP variants"""

    MeltingPoint = ("AdvBuff", 9)
    """Melting Point: Phoenix Threepeater & Phoenix Drone: Global enflamed damage bonus 50% → 150%, and regular ignited projectiles can now inflict the debuff  | Effects also apply to SP variants"""

    Shattershot = ("AdvBuff", 10)
    """Shattershot: Gatling Icicle-shroom & Sunburst-shroom: Icicles now pierce infinitely and split into two diagonal icicles upon impact the first five times | Effects also apply to SP variants"""

    Icebreaker = ("AdvBuff", 11)
    """Icebreaker: Gatling Sunburst-shroom Subspecies Unlocked | Gatling Icicle-shroom: Damage to Frozen/Chill-immune zombies 4× → 12× | Effects also apply to SP variants"""

    PennyPincher = ("AdvBuff", 12)
    """Penny Pincher: Radiant Pot: Upgrade costs from Silver Pots to Golden Pots will not exceed 8k"""

    SolarEconomy = ("AdvBuff", 13)
    """Solar Economy: Radiant Pot: Coins exceeding the maximum amount will be converted into Sun at a rate of 2:1"""

    SmartShield = ("AdvBuff", 14)
    """Smart Shield: Aegis Umbrella Subspecies Unlocked | Midas Umbrella & Aegis Umbrella: Activates Ultimate automatically if zombies are near"""

    HomeRun = ("AdvBuff", 15)
    """Home Run: Midas Umbrella: Damage Boost 100% → 300%"""

    DroneMaster = ("AdvBuff", 16)
    """Drone Master: Aristocattail: Drone Attack Damage ×3 | Thunder Bunnyon: Summoned Drone is no longer nerfed and fires 60 shots normally"""

    Needlework = ("AdvBuff", 17)
    """Needlework: Thunder Bunnyon Subspecies Unlocked | Aristocattail: Regular Attack Damage ×5 | Thunder Bunnyon: Attack Damage ×3"""

    ControlledFusion = ("AdvBuff", 18)
    """Controlled Fusion: Avarice-shroom Subspecies Unlocked | Calamity-shroom: All Doom-shroom explosions are now craterless"""

    WarMachine = ("AdvBuff", 19)
    """War Machine: Calamity-shroom: Now spawns 3 extra Hypnotized Armored Gargantuars and Zombonis when it explodes"""

    NumismaticEngine = ("AdvBuff", 20)
    """Numismatic Engine: Tycoonwood & Magnate Plantern: 1% Damage increase to Coin projectiles/lasers for every 1000 Coins you have"""

    GoldenRain = ("AdvBuff", 21)
    """Golden Rain: Magnate Plantern Subspecies Unlocked | Tycoonwood: Coin projectiles now deal splash damage"""

    CrystalDynamo = ("AdvBuff", 22)
    """Crystal Dynamo: Boreas Umbrella Subspecies Unlocked | Pharos Umbrella: Energy Limit ×10, Recovery Speed ×20, Healing Speed ×2 | Boreas Umbrella: Damage in Scatter Mode increases linearly up to ×4, Damage in Focus Mode ×4"""

    EnergyFocus = ("AdvBuff", 23)
    """Energy Focus: Pharos Umbrella: Normal Attack Damage ×3, Explosion Damage ×10, Attack Interval → 2s | Boreas Umbrella: Cryo-beam in Focus Mode now applies Freeze for 1s"""

    Deadeye = ("AdvBuff", 24)
    """Deadeye: Buck-shroom Squad:  Expected Sniper headshot frequency increased to once every 5s | Buck-strike Squadron: Attack damage ×3"""

    ShellShock = ("AdvBuff", 25)
    """Shell Shock: Buck-strike Squadron Subspecies Unlocked | Buck-shroom Squad: Flak cannon knockback ×2, attack damage ×3 | Buck-strike Squadron: Attack damage ×3"""

    FluxDrive = ("AdvBuff", 26)
    """Flux Drive: Dyson Magnet Subspecies Unlocked | Tesla Magnet: Attack Range ×2 | Dyson Magnet: Metal Production CD halved"""

    Magnetomania = ("AdvBuff", 27)
    """Magnetomania: Tesla Magnet: Absorbs 3 Metal Objects at once, damage to Giga Trident-nut Zombies or Giga Football-nut Zombies ×3 | Dyson Magnet: Heal amount ×3, extra Metal Object production limit (3 + (n/m)/4) → (3 + (n/m)/3)"""

    CertainDoom = ("AdvBuff", 28)
    """Certain Doom: Wicked Undertater Subspecies Unlocked | Grim Arbiter & Wicked Undertater: Seed packet drop is now guaranteed"""

    EldritchLink = ("AdvBuff", 29)
    """Eldritch Link: Grim Arbiter & Wicked Undertater: Zombie Soul damage transfer ×2"""

    LingeringFallout = ("AdvBuff", 30)
    """Lingering Fallout: Big Bang Cherry & Big Crunch Squash: Particle Soup initial duration increased from 7s to 10s"""

    ChainReaction = ("AdvBuff", 31)
    """Chain Reaction: Big Crunch Squash Subspecies Unlocked | Big Bang Cherry & Big Crunch Squash: Explosive and doom projectiles have a small chance of transforming into Cosmic Debris with 12× damage when they hit zombies"""

    StickierButter = ("AdvBuff", 32)
    """Stickier Butter: Cornposter Pot Subspecies Unlocked | Cornveyor Weed & Cornposter Pot: Cornveyor and Cornposter's Butter stun duration ×3"""

    SlideShow = ("AdvBuff", 33)
    """Slide Show: Cornveyor Weed: Now makes zombies on it to continuously slide to the right | Cornposter Pot: Butter Chance for the plant above 50% → 100%"""

    MagneticResonance = ("AdvBuff", 34)
    """Magnetic Resonance: Omni Pumpkin: On entry, grants all connected Magnetic Plants a Shield equal to 30 × number of Magnetic Plants | Quasar: On entry, resets and grants them an Attack buff of 0.5% × number of Magnetic Plants instead"""

    DualPolarity = ("AdvBuff", 35)
    """Dual Polarity: Omni Pumpkin & Quasar: Now counts twice towards the number of Magnetic Plants"""

    ExplosiveBreath = ("AdvBuff", 36)
    """Explosive Breath: Pyroboros Pot Subspecies Unlocked | Dragonbreath Torcher: Explosion Frequency ×2"""

    HeatMomentum = ("AdvBuff", 37)
    """Heat Momentum: Dragonbreath Torcher: Each zombie hit by Dragonbreath Torcher's fire breath increases the damage of the next hit of that same attack by 1%, stacking up to 400%"""

    ColdFront = ("AdvBuff", 38)
    """Cold Front: Oblivion-shroom Subspecies Unlocked | Avalanche-shroom: +100 Initial Energy | Oblivion-shroom: Damage ×2"""

    FrozenHorizon = ("AdvBuff", 39)
    """Frozen Horizon: Avalanche-shroom: Attack Radius ×2 | Oblivion-shroom: Attack Interval halved"""

    ArcaneProwess = ("AdvBuff", 40)
    """Arcane Prowess: Mesmer Cattail: Ability CD Halved, Ability radius +0.5 tiles"""

    Lovebite = ("AdvBuff", 41)
    """Lovebite: Mesmer Cattail: Hypnotized zombies spawned by her ability deal an additional 30% true damage that ignores damage reduction when biting"""

    WeatheringGale = ("AdvBuff", 42)
    """Weathering Gale: Quetzalcoatl Blover: Dizzy effect damage bonus 20% → 40%, and attacks reduce DR value by 10"""

    SwiftWinds = ("AdvBuff", 43)
    """Swift Winds: Quetzalcoatl Blover: Blover spawning CD 10s → 3s"""

    HatTrick = ("AdvBuff", 44)
    """Hat Trick: SP Cryomancer Pea: Everytime Cryomancer Pea's projectile ricochets, its damage increases by 10%. At Level 2, ricochet amount ×3"""

    Spellbound = ("AdvBuff", 45)
    """Spellbound: SP Cryomancer Pea: Cryomancer Pea's projectiles now prioritize targetting bosses with the highest HP when ricocheting. At Level 2, zombies hit by ricocheting projectiles take +10% extra damage"""

    SalvageScavenger = ("AdvBuff", 46)
    """Salvage Scavenger: Ender Pumpkin Chest: Can store metal objects dropped and uses them to heal Giga Mecha-nuts; prioritizing the one with the lowest HP first"""

    LargeEnderChest = ("AdvBuff", 47)
    """Large Ender Chest: Ender Pumpkin Chest: The stack limit for each individual slot is now doubled for all Pumpkin Chests."""

    QuickHands = ("AdvBuff", 1000)
    """Quick Hands: Gloves' cooldown is reduced by 10s (No CD for the plant Glove), and can now move Mini-bosses"""

    BackupSupply = ("AdvBuff", 1001)
    """Backup Supply: All Plants' recharge is halved"""

    AbundantSun = ("AdvBuff", 1002)
    """Abundant Sun: Each Sun now gives more value | 5 → 15 → 25 → 50 → 75"""

    Dexterity = ("AdvBuff", 1003)
    """Dexterity: Gloves' cooldown is halved, and can now move Mini-bosses"""

    FastCopy = ("AdvBuff", 1004)
    """Fast Copy: Imitater's Recharge: 5mins → 50s"""

    HammerTime = ("AdvBuff", 1005)
    """Hammer Time: Mallet's cooldown is reduced to 6s"""

    FlexibleLoadout = ("AdvBuff", 1006)
    """Flexible Loadout: You now have the option to re-pick your Plant Loadout during the game"""

    CoupDeGrace = ("AdvBuff", 1007)
    """Coup de Grâce: Zombies take an additional 1800 damage when they take more than 1800 damage (after damage reduction)"""

    Strength = ("AdvBuff", 1008)
    """Strength: Plants' Damage is increased by 20%"""

    SunderingSmite = ("AdvBuff", 1009)
    """Sundering Smite: Zombies receive 20% more damage"""

    Resourcefulness = ("AdvBuff", 1010)
    """Resourcefulness: Modifier reroll times +2"""

    Cryostasis = ("AdvBuff", 1011)
    """Cryostasis: The freeze time of all zombies is increased by 25%, and the slow rate from chill is increased by 10%"""

    SolarReserve = ("AdvBuff", 1012)
    """Solar Reserve: Gain 3000 Sun, then double your total amount of Sun after | Sun Cap 50k → 100k"""

    CherryOnTop = ("AdvBuff", 1013)
    """Cherry on Top: True Cherry Bomb: Explosive cherries will now deal at least 1800 damage, have increased explosion range and cause Cremator damage"""

    Recycling = ("AdvBuff", 1014)
    """Recycling: Clicking on the same plant when you have it on your Glove will disassemble it at the cost of 500 Sun | 20s cooldown"""

    Phalanx = ("AdvBuff", 1015)
    """Phalanx: When two identical plants are placed one above the other (adjacent in the same column), they gain a 50% damage bonus and a 50% damage reduction"""

    RevitalizingCharm = ("AdvBuff", 1016)
    """Revitalizing Charm: Hypnotized zombies gain a 500% damage buff and 80% damage reduction (WARNING: Also causes Cherry Newspaper Zombies from Empress/Enchantress-shroom to not lose their newspaper on summon!!)"""

    CosmicCascade = ("AdvBuff", 1017)
    """Cosmic Cascade: All Meteors' attack cooldowns are halved | Base Meteor DMG increased by 300 for every Magnetar in the field"""

    Enlightenment = ("AdvBuff", 1018)
    """Enlightenment: Adds 4 Lumos Levels for the entire field"""

    SecondWind = ("AdvBuff", 1019)
    """Second Wind: After a plant is healed, they heal for 5% of their current health per second for the next 3s (unstackable)"""

    HealingBoost = ("AdvBuff", 1020)
    """Healing Boost: Plants gain a 20% healing bonus"""

    ColdsnapInsightI = ("AdvBuff", 1021)
    """Coldsnap Insight I: Upgrade Cryomancer Pea to SP Cryomancer Pea (Level 1)"""

    ColdsnapInsightII = ("AdvBuff", 1022)
    """Coldsnap Insight II: Upgrade SP Cryomancer Pea to Level 2"""

    Doomsday = ("AdvBuff", 2000)
    """Doomsday: True Doom-shroom: Doom Shells will now release a craterless Doom-shroom explosion upon impact"""

    LineFormation = ("AdvBuff", 2001)
    """Line Formation: Enable Column Planting"""

    Transcendence = ("AdvBuff", 2002)
    """Transcendence: You can upgrade 1 upgradable Epic Modifier"""

    ApexDefender = ("AdvBuff", 2003)
    """Apex Defender: If a Plant Type has dealt the highest total damage on the field, its attacks deal an extra 30% of original damage as true damage"""

    TriggerHappy = ("AdvBuff", 2004)
    """Trigger Happy: After firing 50 times (25 for catapults), plants gain an unlimited attack speed for 1s"""

    LifeSteal = ("AdvBuff", 2005)
    """Life Steal: Plants gain 1% life steal, applied to the plant with the lowest HP percentage on the field"""

    AmbushTactics = ("AdvBuff", 2006)
    """Ambush Tactics: The longer since a zombie was last damaged, the more damage it takes from the next hit. <1s: Damage * (1 + 9t); ≥1s: Damage * (10 + 9ln(t))"""

    CorruptingTouch = ("AdvBuff", 2007)
    """Corrupting Touch: All zombies are now under the Corruption effect: each time a zombie is damaged, the next instance of damage to that zombie is increased by 5% (stacks infinitely)"""

    Purification = ("AdvBuff", 2008)
    """Purification: You can remove 1 non-mini-boss Zombie Modifier from the View Modifier menu"""

    BlazeOfGlory = ("AdvBuff", 2009)
    """Blaze of Glory: When hypnotized zombies die, they explode, dealing damage equal to 150% of their max HP to nearby zombies"""

    MomentumSync = ("AdvBuff", 2010)
    """Momentum Sync: For each 1% attack speed bonus a plant gains, it also receives 1% attack damage bonus"""

    EternalBulwark = ("AdvBuff", 3000)
    """Eternal Bulwark: When Cherrizilla and Obsidian Tall-nut (or their subspecies) are both present, Cherrizilla/Garlizilla no longer has a maximum Toughness cap, and Obsidian Tall-nut/Obsidian Mine gains a 90% damage reduction"""

    AstralConvergence = ("AdvBuff", 3001)
    """Astral Convergence: If there are at least 6 Magnetars and 6 Helios Cabbages on the field, the Mini Sun summoned by the Helios Cabbage will never disappear, and will keep summoning Helios Meteors, while Magnetars can consume sun for more damage but can only attacks its lane"""

    TotalFirepower = ("AdvBuff", 3002)
    """Total Firepower: Gatling Cherrybomber now spreads its shots evenly across three lanes with sine and cosine trajectories, Jalapeno blasts Infernal Squashwoods acquire properties of Cherry Bomb explosions, and explosive cherries deal more damage proportionate to number of Gatling Cherrybombers after passing through Infernal Squashwoods"""

    CelestialBeacon = ("AdvBuff", 3003)
    """Celestial Beacon: When there are at least 6 Magnetars and 6 Selene Cabbages on the field, Selene's summoned Mini Moon will not disappear and each Selene provides massive Lumos levels, while Magnetars deal extra damage to the zombie with the highest amount of HP"""

    EventHorizon = ("AdvBuff", 3004)
    """Event Horizon: Hail melons from Maelonstrom's Nebula Rifts now deal 6× damage and create Singularities, and Cosmo-pult always lob Ultimate Black Holes. When an Ultimate Black Hole collapses, it also detonates all Singularities to further increase its own damage"""

    HeavensWrath = ("AdvBuff", 3005)
    """Heaven's Wrath: Click on a reloaded Vulcannon while holding an Epic Twin Inferno-nut with the Glove to make all reloaded Vulcannon on the field perform a synergized attack towards the sky. Every 8th Inferno Shell shot calls down an Inferno Meteor dealing 80× damage, decimating all zombies on the screen"""

    BulletHell = ("AdvBuff", 3006)
    """Bullet Hell: When Cherrybomber Drone is placed above Epic Gatling Frenzy-shroom, the more they attack, the more bullets they fire in the next volley. This bonus decays after they stop attacking. (WARNING: Will lead to cancerous amounts of projectiles!!)"""

    Ultranova = ("AdvBuff", 3007)
    """Ultranova: Photon Splitter can lock onto any Atomheart Plantern ahead (click to select) to charge it. When energy exceeds 10k, its brightness increases, dealing heavy damage and slowing zombies in its radius. At 100k, collapses into a black hole and explodes, devastating all zombies on screen. (WARNING: Contains flashing lights)"""

    LittleMiracle = ("AdvBuff", 3008)
    """Little Miracle: When Litter-pult and SP Gatling Icicle-shroom are planted on the same tile, the latter's projectiles split one additional time. Both plants' normal and special projectiles inherit some properties from each other's shots. (WARNING: Will cause lag)"""

    ElementalFury = ("AdvBuff", 3009)
    """Elemental Fury: Doominator now spawns Obsidian Tall-nut Iceclaw Zombies, Napalm-shroom's main projectile will split into an additional Obsidian Melon; dealing AoE damage equal to the melon's original attack power which increases by 100% for each ice, snow and fire plant present on the lawn, and a synergy between the Enflamed and Chill debuffs is unlocked"""

    OmnicidalInferno = ("AdvBuff", 3010)
    """Omnicidal Inferno: Infernal Sparkwood now ignites the lawn instead of a single lane on spawning Spicy plant. SP Phoenix Threepeater and Drone projectiles splits into all lanes on passing through Infernal Sparkwood"""

    AbyssalChibi = ("AdvBuff", 4000)
    """Abyssal Chibi: Summons an Abyssal Chibi to fight for you (replaces current Pet). His hammer smash damages both nearby plants and zombies, grants damage reduction to affected plants, and deals increased damage to zombies based on nearby plants' HP. Hammer effects scale with XP level."""

    StrikerJunior = ("AdvBuff", 4001)
    """Striker Junior: Summons a Striker Junior to fight for you (replaces current Pet). Every 3s, he moves to the plant with the lowest HP percentage and rallies the area, healing nearby plants and increasing damage taken by zombies. Rally effects scale with xp level"""

    PrototypeIceborg = ("AdvBuff", 4002)
    """Prototype Iceborg: Summons a Prototype Iceborg to fight for you (replaces current Pet). She targets the highest-HP lane and fires ice projectiles. Damage increases based on the number of chilled/frozen zombies, and gains infinite pierce & bonus xp if the Iceborg Executrix is on the field. Projectile damage scale with xp level"""

    BabyJill = ("AdvBuff", 4003)
    """Baby Jill: Summons a Baby Jill to fight for you (replaces current Pet). Every 15s, she performs a random attack: summons high-tier hypnotized Clown-in-the-Box zombies per lane or throws out explosives (lane-wide or global). Explosion damage scales with xp level"""

    MiniPozeidon = ("AdvBuff", 4004)
    """Mini Pozeidon: Summons a Mini Pozeidon to fight for you (replaces current Pet). Every 5s, he throws his trident ahead, which pierces and damages zombies with explosions. If the mini-boss Pozeidon is present, throws 4 tridents in each lane every 10s instead"""

    YoungDuke = ("AdvBuff", 4005)
    """Young Duke: Summons a Young Duke to fight for you (replaces current Pet). Rapidly fires iron pea bullets forward, and every 20 seconds she summons a column of mini warhorses to charge at the zombies and create Zombie Souls of the ones they hit. If the mini-boss Archduke Deathrider is present, her summoning interval is halved. (WARNING: Will cause MASSIVE lag!!)"""

    ImperorHatchling = ("AdvBuff", 4006)
    """Imperor Hatchling: Summons an Imperor Hatchling to fight for you (replaces current Pet). Every 10 seconds, he will transform a certain number of zombies (based on XP level) into Chicken Jockey or Hydrofowl Zombies. If the mini-boss Imperor's Ark of the Duck is present, the maximum number of transformations is doubled."""

    SkygliderMecha = ("AdvBuff", 4007)
    """Skyglider Mecha: Summons a Skyglider Mecha to fight for you (replaces current Pet). Increases damage from plant-side Jack-in-the-Box explosions, and fires an explosive at zombies every 1.5s (every 3rd attack is fired across each row). If the mini-boss Skystrider Mecha is present, the pet's attack interval is halved."""

    GoliathSlayer = ("AdvBuff", 5000)
    """Goliath Slayer: Plants deal +100% to Mini-bosses and Bosses"""

    AdverseAdaptation = ("AdvBuff", 5001)
    """Adverse Adaptation: Plants gain a 5% damage bonus for every Zombie Modifier you have"""

    DivineBlade = ("AdvBuff", 5002)
    """Divine Blade: Unlock Swordsage Starfruit"""

    CurseOfPride = ("AdvBuff", 5003)
    """Curse of Pride: Odyssey Plants' Attack and max HP reduced by 90%, but all other plants now have 40× Attack & max HP, and 2× Attack Speed"""

    CurseOfGreed = ("AdvBuff", 5004)
    """Curse of Greed: Seed packets no longer need recharge but each use costs 15× their base Sun + 50% of the player's current Sun"""

    FinalFrontier = ("AdvBuff", 6000)
    """Final Frontier: Lawnmowers: Final damage +200%, Attack speed +300%"""

    CherrizillaMasteryI = ("AdvBuff", 6001)
    """Cherrizilla Mastery I: Cherrizilla: Healing Power +100%"""

    CherrizillaMasteryII = ("AdvBuff", 6002)
    """Cherrizilla Mastery II: Cherrizilla: Attack Damage +50%"""

    GatlingCherrybomberMasteryI = ("AdvBuff", 6003)
    """Gatling Cherrybomber Mastery I: Gatling Cherrybomber: Cherry and other variants of projectiles' explosion radius +50% and damage +100%"""

    GatlingCherrybomberMasteryII = ("AdvBuff", 6004)
    """Gatling Cherrybomber Mastery II: Gatling Cherrybomber: Cherry and other variants of projectiles' explosion radius -50%  but damage +300%"""

    DoominatorMasteryI = ("AdvBuff", 6005)
    """Doominator Mastery I: Doominator: Frozen zombies take +50% more damage"""

    DoominatorMasteryII = ("AdvBuff", 6006)
    """Doominator Mastery II: Doominator: Hypnotized zombies deal 3× damage"""

    InfernalSquashwoodMasteryI = ("AdvBuff", 6007)
    """Infernal Squashwood Mastery I: Infernal Squashwood: Jalapeno effect changes from instant to DoT, dealing 1/3 the original damage 10 times within 1s"""

    InfernalSquashwoodMasteryII = ("AdvBuff", 6008)
    """Infernal Squashwood Mastery II: Infernal Squashwood: Grants projectiles +50% damage before igniting them"""

    BacklineBastion = ("AdvBuff", 6009)
    """Backline Bastion: Plants in the fifth column get 50% increased maximum Toughness and 50% damage reduction. Each column to the left reduces damage cap by 10% and increases damage reduction by 10%"""

    SPEvolution_DoomGatling = ("AdvBuff", 7000)
    """SP Evolution: Unlock SP Gatling Doom and SP Gatling Frenzy-shroom
    Use Doom-shroom to upgrade
    """

    SPEvolution_TwinNut = ("AdvBuff", 7001)
    """SP Evolution: Unlock SP Twin Solar-nut and SP Twin Inferno-nut
    Use Wall-nut to upgrade
    """

    SPEvolution_Phoenix = ("AdvBuff", 7002)
    """SP Evolution: Unlock SP Phoenix Threepeater and SP Phoenix Drone
    Use Jalapeno to upgrade
    """

    SPEvolution_GatlingIcicle = ("AdvBuff", 7003)
    """SP Evolution: Unlock SP Gatling Icicle-shroom and SP Gatling Sunburst-shroom
    Use Peashooter to upgrade
    """

    SolarGrace = ("AdvBuff", 10000)
    """Solar Grace: Immediately gain 100k Sun | Sun Cap +100k"""

    GigaGuardian = ("AdvBuff", 10001)
    """Giga Guardian: Immediately gain 3 Giga Mecha-nut seed packets which start with 640k HP"""

    InstantPromotion = ("AdvBuff", 10002)
    """Instant Promotion: Upgrade (1+n) random plants to Tier 1, where n is the number of Plant modifiers you currently have"""

    Accelerator = ("AdvBuff", 10003)
    """Accelerator: Increase the speed of (1+n) random plants, where n is the number of Plant modifiers you currently have"""

    TotemOfUndying = ("AdvBuff", 10004)
    """Totem of Undying: The next time zombies reach the house, it is ignored for 3s and knock all zombies back to the start"""

    SupplyDrop = ("AdvBuff", 10005)
    """Supply Drop: Obtain a Pumpkin Chest that has many seed packets for Odyssey Fusions (no Subspecies)"""

    DeusExMachina = ("AdvBuff", 10006)
    """Deus Ex Machina: Knock all zombies back to the start, then instantly defeat all zombies"""

    WintersChosenOne = ("AdvBuff", 10007)
    """Winter's Chosen One: Gain a Super Blizzard Commando with +1500% damage and HP, +1000% speed, and gain an extra Coldsnap Bean"""

    HeatRiser = ("AdvBuff", 10008)
    """Heat Riser: Gain a random Odyssey plant. Each new zombie wave, it gains +25% damage, +25% HP, and +10% speed"""

    PactOfCorruption = ("AdvBuff", 10009)
    """Pact of Corruption: Gain a Shroomageddon seed packet. Planting it ACCEPTS the challenge:
    Summon 3-6 random Odyssey zombies in each lane (yeah, ALL possible ones)
    Defeat them all to unlock the Modifier "Corrupting Touch"
    """

    LimitBreak = ("AdvBuff", 10010)
    """Limit Break: All plant attack damage ×2"""

    ForceShield = ("AdvBuff", 10011)
    """Force Shield: All plants gain 50 + (2% max HP) shield per second"""

    TheLastDitch = ("AdvBuff", 10012)
    """The Last Ditch: When you have 20 or more plants on the field, zombies reaching the house no longer results in game over, but causes all plants to have 1/3 chance to die instead"""

    PactOfPromotion = ("AdvBuff", 10013)
    """Pact of Promotion: Gain an Omni Pumpkin seed packet. Planting it ACCEPTS the challenge:
    The number of zombies in the next 20 waves are doubled
    Get through and all plants on the Omni Pumpkin's tile will be promoted to Tier 3
    """

    LawnSweeper = ("AdvBuff", 10014)
    """Lawn Sweeper: Unleash all current lawnmowers and restore one full column of them"""

    DelayOfFate = ("AdvBuff", 10015)
    """Delay of Fate: You will not game over if you manage to kill the zombie reaching your house within 1.5s"""

    CloneArmy = ("AdvBuff", 10016)
    """Clone Army: Immediately gain 5 Imitater seed packets"""

    SharedRoots = ("AdvBuff", 10017)
    """Shared Roots: Upon gaining a second copy of any plant for the first time, you receive an additional seed packet of that plant"""

    EvolutionCatalyst = ("AdvBuff", 10018)
    """Evolution Catalyst: Using the glove to move a plant onto another plant of the same type and tier upgrades it by 1 tier"""

    FateReforged = ("AdvBuff", 10019)
    """Fate Reforged: Immediately gain 10 Golden Recycling Vases. Additionally, receive 1 per wave and 5 per flag (huge wave)"""

    SpeedyDeployment = ("AdvBuff", 11000)
    """Speedy Deployment: Level gimmick: Wheelbarrow's cooldown is reduced to 3 seconds"""

    InstantGrowth = ("AdvBuff", 11001)
    """Instant Growth: Level gimmick: Deucalion-shroom starts with 1000 Growth Stages"""

    Ascend_Inferno = ("AdvBuff", 12000)
    """Ascend: Inferno: Napalm-shroom's melons create an extra sea of fire upon hitting the ground and can split up to 2 more times when hitting zombies"""

    Ascend_Burst = ("AdvBuff", 12001)
    """Ascend: Burst: When Apeacalypse Minigun is casting its ultimate ability, they will release 4 extra waves of Frostflame dealing 50 instances of damage each. Each instance deals damage equal to 10,000% of the turret's attack power to a random zombie in range"""

    Ascend_TrueAim = ("AdvBuff", 12002)
    """Ascend: True Aim: Berserker Snipea's critical hit will now be guaranteed"""

    Ascend_Blasting = ("AdvBuff", 12003)
    """Ascend: Blasting: Threepeatato-mine's projectiles will now trigger a Potato Mine explosion when hitting a zombie"""

    Ascend_Doom = ("AdvBuff", 12004)
    """Ascend: Doom: When Doom Chomper attacks, it will trigger a Doom explosion regardless of if it swallows a zombie or not. If it swallows a zombie, it will trigger two Doom explosions"""

    Ascend_Oblivion = ("AdvBuff", 12005)
    """Ascend: Oblivion: Shroomageddon releases a 1-million damage Doom-shroom explosion upon death"""

    Ascend_ShieldOfLight = ("AdvBuff", 12006)
    """Ascend: Shield of Light: Pharos Umbrella can consume energy to knock back zombies in a 3×3 area and regular attacks can have ×3 targets"""

    Ascend_Gravity = ("AdvBuff", 12007)
    """Ascend: Gravity: Black holes will attract zombies with less than 50% max HP"""

    Ascend_Penetration = ("AdvBuff", 12008)
    """Ascend: Penetration: Phoenix Threepeater now shoots in all lanes and its projectiles pierce infinitely"""

    Ascend_TheMaw = ("AdvBuff", 12009)
    """Ascend: The Maw: Tyrannoflora Lux attraction range after digestion is vastly increased"""

    Ascend_ChaosBeam = ("AdvBuff", 12010)
    """Ascend: Chaos Beam: Adjacent 2 Celestial Beams releases mini black hole explosions periodically"""

    Ascend_Ricochet = ("AdvBuff", 12011)
    """Ascend: Ricochet: Buck-shroom Squad can no longer headshot but projectiles ricochet on lawn edges (like Split Pea), up to (number of pierces + 2) times"""

    Ascend_Veterancy = ("AdvBuff", 12012)
    """Ascend: Veterancy: Empress-shroom now summons zombies with greatly increased stats"""

    Ascend_Density = ("AdvBuff", 12013)
    """Ascend: Density: Buckshot Commando shoots even larger, stronger projectiles during Ultimate Moves"""

    Ascend_Hemorrhage = ("AdvBuff", 12014)
    """Ascend: Hemorrhage: Zombies targeted by any Spikerock continuously lose HP equal to 400% the attack for 2s"""

    Ascend_Fortune = ("AdvBuff", 12015)
    """Ascend: Fortune: Soulrender Bamboo can now follow mouse movements with attack speed upgrades increasing the movement speed, deal damage to any zombies caught in its way"""

    Ascend_Decryption = ("AdvBuff", 12016)
    """Ascend: Decryption: Zombies that spawn will be cursed with 3 stacks of Decryption Magic. Every wave, the zombie with the highest HP will gain 100 stacks of Decryption. Each stack increases the damage a zombie takes by 100%, and when a zombie cursed with Decryption dies their stacks will be spread to nearby zombies."""

    Ascend_Clusterbomb = ("AdvBuff", 12017)
    """Ascend: Clusterbomb: Melon-nut's projectile explodes mid-air and splits into several Mini Watermelons thrown at zombies across the field"""

    Ascend_GoldenBarrage = ("AdvBuff", 12018)
    """Ascend: Golden Barrage: Golden Melon's Ultimate additionally launches Golden melons at all zombies, and the Ultimate's split count ×2"""

    Ascend_HardenedSaw = ("AdvBuff", 12019)
    """Ascend: Hardened Saw: Lifereaver Spruce's projectiles gain an additional 0.6% of its current Shield as Attack Damage, capped at 300% of its base Attack"""

    Ascend_TotalEruption = ("AdvBuff", 12020)
    """Ascend: Total Eruption: Kaledera Eruptor's targeting range is +1 lane above and below, and fires at all targets simultaneously (if the number of targets is less than the max scatter count, the leftover shots are evenly distributed among the targets) | Projectile flight time reduced by 50%"""

    Ascend_Swordsmanship = ("AdvBuff", 12021)
    """Ascend: Swordsmanship: For every 2 giant swords summoned Swordsage Starfruit, each attack additionally fires 1 spinning shortsword"""

    Ascend_CircleOfDeath = ("AdvBuff", 12022)
    """Ascend: Circle of Death: Projectiles surrounding Mag-nut can now pierce infinitely, but their duration is reduced to 10s"""

    Ascend_Conflagration = ("AdvBuff", 12023)
    """Ascend: Conflagration: Dragonbreath Torcher's attacks additionally release Jalapeno effects in all lanes"""

    Ascend_Gigantism = ("AdvBuff", 12024)
    """Ascend: Gigantism: Obsidian Tall-nut and its holographic projections have vastly larger hitboxes and are immune to crushing from bosses
    Healing CD: 15s → 10s
    """

    Ascend_Evocation = ("AdvBuff", 12025)
    """Ascend: Evocation: Hypnotized Abyssal Gargantuar spawns hypnotized Abyssal Imp when smashing"""

    Ascend_MagicalIndex = ("AdvBuff", 12026)
    """Ascend: Magical Index: Apeacalypse Railgun now fires a continuous light beam"""

    Ascend_Sorrow = ("AdvBuff", 12027)
    """Ascend: Sorrow: Melancholy Commando now always unleashes its Ultimate, but with half the projectiles"""

    BlastProtection = ("AdvBuff", 13000)
    """Blast Protection: Damage from Zombie Jack-in-the-Box explosions is reduced to 1000"""

    EnchantedShield = ("AdvBuff", 13001)
    """Enchanted Shield: Plants with Shield recover HP equal to 0.1% of their Shield every second"""

    VoodooDummy = ("AdvBuff", 13002)
    """Voodoo Dummy: Summons a Dummy Zombie on the lawn which distributes 60% of damage taken equally among all zombies; can be moved with Zombie Glove.
    Instantly eliminates touched hypnotized zombies
    """

    VoodooDummy_A = ("AdvBuff", 13003)
    """Voodoo Dummy - A: The Dummy Zombie now distributes 100% of the damage it takes among all zombies"""

    VoodooDummy_B = ("AdvBuff", 13004)
    """Voodoo Dummy - B: Summons an additional Dummy Zombie"""

    VoodooDummy_X = ("AdvBuff", 13005)
    """Voodoo Dummy - X: When the Dummy Zombie takes damage, it also deals 100% of that damage to the zombie with the highest HP on the lawn"""

    SolarBlast = ("AdvBuff", 13006)
    """Solar Blast: Summons a Solar Reactor that periodically damages all zombies on the lawn"""

    SolarBlast_A = ("AdvBuff", 13007)
    """Solar Blast - A: Reduces the Solar Reactor's attack CD by 50%"""

    SolarBlast_B = ("AdvBuff", 13008)
    """Solar Blast - B: Increases the Solar Reactor's damage by 100%"""

    SolarBlast_X = ("AdvBuff", 13009)
    """Solar Blast - X: The Solar Reactor additionally calls down a Helios Meteor whenever it attacks"""

    Warhammer = ("AdvBuff", 13010)
    """Warhammer: Reduces the Mallet's damage, but reduces its CD to 3s"""

    Warhammer_A = ("AdvBuff", 13011)
    """Warhammer - A: Greatly increases the effective range of the Mallet's attack"""

    Warhammer_B = ("AdvBuff", 13012)
    """Warhammer - B: Further reduces the Mallet's CD"""

    Warhammer_X = ("AdvBuff", 13013)
    """Warhammer - X: When the Mallet hits a zombie, summons a large hammer at its location that continuously damages zombies before disappearing after a while"""

    GFishBomber = ("AdvBuff", 13014)
    """G-fish Bomber: A Skyglider Mecha will fight for you"""

    GFishBomber_A = ("AdvBuff", 13015)
    """G-fish Bomber - A: Number of attacks required for Skyglider Mecha to fire a Barrage -1"""

    GFishBomber_B = ("AdvBuff", 13016)
    """G-fish Bomber - B: Reduces Skyglider Mecha's attack CD"""

    GFishBomber_X = ("AdvBuff", 13017)
    """G-fish Bomber - X: Barrage shells from Skyglider Mecha can keep splitting while airborne"""

    MoonlightVeil = ("AdvBuff", 13018)
    """Moonlight Veil: Summons a Lunar Reactor that periodically restores HP to all plants on the lawn"""

    MoonlightVeil_A = ("AdvBuff", 13019)
    """Moonlight Veil - A: Greatly increases the amount of HP restored by the Lunar Reactor"""

    MoonlightVeil_B = ("AdvBuff", 13020)
    """Moonlight Veil - B: Grants all plants on the lawn a 1000-HP shield whenever the Lunar Reactor activates"""

    MoonlightVeil_X = ("AdvBuff", 13021)
    """Moonlight Veil - X: Whenever the Lunar Reactor activates, moonlight descends upon every plant on the lawn, which instantly kills regular Zombies within a 3x3 area and makes plants invincible for a short time"""

    IronCurtain = ("AdvBuff", 13022)
    """Iron Curtain: Reduces damage taken by all plants by 20%"""

    IronCurtain_A = ("AdvBuff", 13023)
    """Iron Curtain - A: Reduces damage taken by all plants by 40%"""

    IronCurtain_B = ("AdvBuff", 13024)
    """Iron Curtain - B: Reduces damage taken by all plants by 60%"""

    IronCurtain_X = ("AdvBuff", 13025)
    """Iron Curtain - X: Reduces damage taken by all plants by 90%; whenever a plant loses HP, it fires a pea projectile from its position with damage equal to its max HP | If the zombie has the Counterstrike Modifier, effect is changed to reducing damage taken by 99%"""

    LuckLoan = ("AdvBuff", 13026)
    """Luck • Loan: Gain one Modifier draw at 500 Luck, then lose 25 Luck"""

    LuckLoan_A = ("AdvBuff", 13027)
    """Luck • Loan - A: Gain one Modifier draw at 1000 Luck, then lose 50 Luck"""

    LuckLoan_B = ("AdvBuff", 13028)
    """Luck • Loan - B: Gain one Modifier draw at 1500 Luck, then lose 75 Luck"""

    LuckLoan_X = ("AdvBuff", 13029)
    """Luck • Loan - X: Set your Luck to 250 immediately and Rerolls to 5, triple your Luck cap, and permanently prevent you from selecting Luck Modifiers and [Resourcefulness]
    Each Modifier draw grants 25 Luck, plus an additional amount equal to 20% of your current Luck (up to 100); choosing Bronze, Silver, Gold/Random, or Diamond/Prismatic/Curse costs 20/40/60/100 Luck respectively; each reroll costs 50 Luck
    """

    LuckBounty = ("AdvBuff", 13030)
    """Luck • Bounty: Immediately spawns a wave of zombies with 2× HP and speed; defeating all of them grants a Modifier draw at 500 Luck"""

    LuckBounty_A = ("AdvBuff", 13031)
    """Luck • Bounty - A: Immediately spawns a wave of zombies with 3× HP and speed; defeating all of them grants a Modifier draw at 1000 Luck"""

    LuckBounty_B = ("AdvBuff", 13032)
    """Luck • Bounty - B: Immediately spawns a wave of zombies with 4× HP and speed; defeating all of them grants a Modifier draw at 1500 Luck"""

    LuckBounty_X = ("AdvBuff", 13033)
    """Luck • Bounty - X: Immediately doubles your current Luck and Luck cap (if your Luck is negative, its absolute value is taken before doubling, e.g.: -50 Luck → 100)"""

    InfernalCombustion = ("AdvBuff", 13034)
    """Infernal Combustion: Clicking anywhere releases an Infernal Combustion at the clicked location, with a 10s CD, or 1 second if it kills a zombie"""

    InfernalCombustion_A = ("AdvBuff", 13035)
    """Infernal Combustion - A: Increases Infernal Combustion damage by 100%"""

    InfernalCombustion_B = ("AdvBuff", 13036)
    """Infernal Combustion - B: Decreases Infernal Combustion CD and CD on kill by 50%"""

    InfernalCombustion_X = ("AdvBuff", 13037)
    """Infernal Combustion - X: Infernal Combustion can now damage plants; killing a plant triggers Jalapeno effects on all lanes and refreshes the CD; damage increases based on the total number of Modifiers the plant has"""

    PrismFighter = ("AdvBuff", 13038)
    """Prism Fighter: Gains a Mecha Fighter that continuously locks onto and attacks the leftmost zombie"""

    PrismFighter_A = ("AdvBuff", 13039)
    """Prism Fighter - A: Increases the number of refractions of Mecha Fighter's attack by 1"""

    PrismFighter_B = ("AdvBuff", 13040)
    """Prism Fighter - B: Increases the number of refractions of Mecha Fighter's attack by 2"""

    PrismFighter_X = ("AdvBuff", 13041)
    """Prism Fighter - X: Mecha Figher's Prism attacks gain infinite pierce, and refractions can hit the same target repeatedly"""

    LightningStorm = ("AdvBuff", 13042)
    """Lightning Storm: Summons Lightning Bolts to fight for you, periodically damaging zombies on the lawn"""

    LightningStorm_A = ("AdvBuff", 13043)
    """Lightning Storm - A: Increases Lightning Bolt duration by 100%"""

    LightningStorm_B = ("AdvBuff", 13044)
    """Lightning Storm - B: Increases Lightning Bolt attack frequency by 100%"""

    LightningStorm_X = ("AdvBuff", 13045)
    """Lightning Storm - X: The Lightning Bolts now attack continuously without interruption"""

    Omnipotence = ("AdvBuff", 13046)
    """Omnipotence: Increase Luck by 25, overall attack damage by 10%, 1 reroll, and respawn timer reduction by 10%"""

    Omnipotence_A = ("AdvBuff", 13047)
    """Omnipotence - A: Increase Luck by 50, overall attack damage by 20%, 2 rerolls, and respawn timer reduction by 20%"""

    Omnipotence_B = ("AdvBuff", 13048)
    """Omnipotence - B: Increase Luck by 75, overall attack damage by 10%, 3 rerolls, and respawn timer reduction by 30%"""

    Omnipotence_X = ("AdvBuff", 13049)
    """Omnipotence - X: All plants on the lawn receive 500% bonus HP, 300% independent bonus attack damage, 200% bonus attack speed, 60% crit chance and 150% crit damage"""

    NoPainsNoGains = ("AdvBuff", 14000)
    """No Pains No Gains: Kill all of your plants, and halve the independent damage and speed buffs for all your plants;
    The same will happen after 20 waves, but this time the buffs are doubled
    """

    AllOrNothing = ("AdvBuff", 14001)
    """All or Nothing: If your Luck is below 75, immediately set it to 75. When not protected by the pity system, Silver and Golden modifiers are downgraded to Bronze quality, while Diamond ones are upgraded to Prismatic quality"""

    HighGrounds = ("AdvBuff", 14002)
    """High Grounds: Plants deal 30% more damage when above zombies and 30% less damage when below zombies, determined by their vertical sprite positions on the screen"""

    PredatorInstinct = ("AdvBuff", 14003)
    """Predator Instinct: Plants deal 30% more damage to zombies that are above 50% health, and 30% less damage to those below 50% health"""

    CurseOfMCDXXXVII = ("AdvBuff", 15000)
    """Curse of MCDXXXVII: Magnetar's attack speed is halved. After 1,437 attacks, reverse the curse, with each volley counting as 5 attacks
    Reversal effect: Quasar projectiles from Magnetar gain an additional 1,437 base damage
    """

    BlessingOfMCDXXXVII = ("AdvBuff", 15001)
    """Blessing of MCDXXXVII: Quasar projectiles from Magnetar gain an additional 1,437 base damage"""

    CurseOfAggression = ("AdvBuff", 15002)
    """Curse of Aggression: Gatling Cherrybomber's damage is reduced by 50%. After dealing a cumulative 300M damage, reverse the curse
    Reversal effect: Each time Gatling Cherrybomber attacks, it additionally fires several projectiles from the left side of the screen, with attack equal to 0.0001% of the cumulative damage dealt by other plants
    """

    BlessingOfAggression = ("AdvBuff", 15003)
    """Blessing of Aggression: Each time Gatling Cherrybomber attacks, it additionally fires several projectiles from the left side of the screen, with attack equal to 0.0001% of the cumulative damage dealt by other plants"""

    CurseOfEquity = ("AdvBuff", 15004)
    """Curse of Equity: For each target Kaledera Eruptor has, its projectile damage is reduced by 1%, up to a max reduction of 70%. After a cumulative reduction of 50,000% through this effect, reverse the curse
    Reversal effect: For each target Kaledera Eruptor has, its projectile damage is increased by 1%
    """

    BlessingOfEquity = ("AdvBuff", 15005)
    """Blessing of Equity: For each target Kaledera Eruptor has, its projectile damage is increased by 1%"""

    CurseOfEndurance = ("AdvBuff", 15006)
    """Curse of Endurance: Mag-nut no longer fires projectiles. After attracting 5,000 projectiles, reverse the curse
    Reversal effect: Each time Mag-nut attacks, it additionally fires one projectile of the type it has attracted the most
    """

    BlessingOfEndurance = ("AdvBuff", 15007)
    """Blessing of Endurance: Each time Mag-nut attacks, it additionally fires one projectile of the type it has attracted the most"""

    # Chinese Aliases
    撒豆成兵 = ("AdvBuff", 0)
    精兵强将 = ("AdvBuff", 1)
    枕戈待旦 = ("AdvBuff", 2)
    核能威慑 = ("AdvBuff", 3)
    妙手回春 = ("AdvBuff", 4)
    无关痛痒 = ("AdvBuff", 5)
    尸愁之路 = ("AdvBuff", 6)
    百炼成钢 = ("AdvBuff", 7)
    百步穿杨 = ("AdvBuff", 8)
    怒火攻心 = ("AdvBuff", 9)
    势如破竹 = ("AdvBuff", 10)
    冻彻心扉 = ("AdvBuff", 11)
    多多益善 = ("AdvBuff", 12)
    等价交换 = ("AdvBuff", 13)
    人工智能 = ("AdvBuff", 14)
    弹射起步 = ("AdvBuff", 15)
    特制弹药 = ("AdvBuff", 16)
    一针见血 = ("AdvBuff", 17)
    可控核聚变 = ("AdvBuff", 18)
    人多势众 = ("AdvBuff", 19)
    大富翁 = ("AdvBuff", 20)
    好运连连 = ("AdvBuff", 21)
    量子护盾 = ("AdvBuff", 22)
    高能射线 = ("AdvBuff", 23)
    枪枪爆头 = ("AdvBuff", 24)
    开炮 = ("AdvBuff", 25)
    电磁涡轮 = ("AdvBuff", 26)
    万磁王 = ("AdvBuff", 27)
    罪恶之力 = ("AdvBuff", 28)
    深度定制 = ("AdvBuff", 29)
    核能射线 = ("AdvBuff", 30)
    链式反应 = ("AdvBuff", 31)
    尸愁之路II = ("AdvBuff", 32)
    滑滑梯 = ("AdvBuff", 33)
    磁力护盾 = ("AdvBuff", 34)
    磁能科技 = ("AdvBuff", 35)
    爆裂连珠 = ("AdvBuff", 36)
    烈火锋芒 = ("AdvBuff", 37)
    冷寂寒冰1 = ("AdvBuff", 38)
    冷寂寒冰2 = ("AdvBuff", 39)
    泳池派对 = ("AdvBuff", 40)
    爱与记忆 = ("AdvBuff", 41)
    风刃 = ("AdvBuff", 42)
    狂风肆虐 = ("AdvBuff", 43)
    举世无双 = ("AdvBuff", 44)
    聪明绝顶 = ("AdvBuff", 45)
    自动化升级 = ("AdvBuff", 46)
    堆叠升级 = ("AdvBuff", 47)
    至极手速 = ("AdvBuff", 1000)
    全息制冷 = ("AdvBuff", 1001)
    熠熠生辉 = ("AdvBuff", 1002)
    极速战备 = ("AdvBuff", 1003)
    复制中心 = ("AdvBuff", 1004)
    运斤如风 = ("AdvBuff", 1005)
    全副武装 = ("AdvBuff", 1006)
    致命一击 = ("AdvBuff", 1007)
    强力打击 = ("AdvBuff", 1008)
    精准打击 = ("AdvBuff", 1009)
    合理投资 = ("AdvBuff", 1010)
    极致之冰 = ("AdvBuff", 1011)
    聚光盆 = ("AdvBuff", 1012)
    真樱 = ("AdvBuff", 1013)
    拆分 = ("AdvBuff", 1014)
    连连看 = ("AdvBuff", 1015)
    肉身成圣 = ("AdvBuff", 1016)
    斗转星移 = ("AdvBuff", 1017)
    灯火通明 = ("AdvBuff", 1018)
    强心针 = ("AdvBuff", 1019)
    高效恢复 = ("AdvBuff", 1020)
    魔力升级 = ("AdvBuff", 1021)
    魔力升级II = ("AdvBuff", 1022)
    真毁 = ("AdvBuff", 2000)
    排山倒海 = ("AdvBuff", 2001)
    升级 = ("AdvBuff", 2002)
    绝对力量 = ("AdvBuff", 2003)
    爽快射击 = ("AdvBuff", 2004)
    生命偷取 = ("AdvBuff", 2005)
    过载 = ("AdvBuff", 2006)
    腐化 = ("AdvBuff", 2007)
    净化 = ("AdvBuff", 2008)
    定时炸弹 = ("AdvBuff", 2009)
    电力相生 = ("AdvBuff", 2010)
    我是传奇 = ("AdvBuff", 3000)
    星神合一 = ("AdvBuff", 3001)
    火力全开 = ("AdvBuff", 3002)
    星月护符 = ("AdvBuff", 3003)
    永寂新星 = ("AdvBuff", 3004)
    力量会给予希望 = ("AdvBuff", 3005)
    无限火力 = ("AdvBuff", 3006)
    超新星爆发 = ("AdvBuff", 3007)
    小小作战 = ("AdvBuff", 3008)
    元素反应 = ("AdvBuff", 3009)
    星火燎原 = ("AdvBuff", 3010)
    迷你巨人 = ("AdvBuff", 4000)
    迷你将军 = ("AdvBuff", 4001)
    迷你雪皇 = ("AdvBuff", 4002)
    迷你丑皇 = ("AdvBuff", 4003)
    迷你渊海 = ("AdvBuff", 4004)
    迷你大帅 = ("AdvBuff", 4005)
    迷你鬼王 = ("AdvBuff", 4006)
    迷你基洛夫 = ("AdvBuff", 4007)
    Curse_巨人杀手 = ("AdvBuff", 5000)
    Curse_诅咒之力 = ("AdvBuff", 5001)
    Curse_诸神黄昏 = ("AdvBuff", 5002)
    Curse_倒反天罡 = ("AdvBuff", 5003)
    Curse_贪婪诅咒 = ("AdvBuff", 5004)
    Rogue_后备能源 = ("AdvBuff", 6000)
    Rogue_究极樱桃战神专精I = ("AdvBuff", 6001)
    Rogue_究极樱桃战神专精II = ("AdvBuff", 6002)
    Rogue_究极樱桃射手专精I = ("AdvBuff", 6003)
    Rogue_究极樱桃射手专精II = ("AdvBuff", 6004)
    Rogue_究极大喷菇专精I = ("AdvBuff", 6005)
    Rogue_究极大喷菇专精II = ("AdvBuff", 6006)
    Rogue_究极窝炬专精I = ("AdvBuff", 6007)
    Rogue_究极窝炬专精II = ("AdvBuff", 6008)
    Rogue_推车保护 = ("AdvBuff", 6009)
    UltimateDoomGatling = ("AdvBuff", 7000)
    UltimateSunNut = ("AdvBuff", 7001)
    SuperThreePeater_sp = ("AdvBuff", 7002)
    UltimateSnowGatlingPuff = ("AdvBuff", 7003)
    Random_超多阳光 = ("AdvBuff", 10000)
    Random_鱼丸护体 = ("AdvBuff", 10001)
    Random_超级高手 = ("AdvBuff", 10002)
    Random_唯快不破 = ("AdvBuff", 10003)
    Random_不死图腾 = ("AdvBuff", 10004)
    Random_应有尽有 = ("AdvBuff", 10005)
    Random_规则之力 = ("AdvBuff", 10006)
    Random_英雄登场 = ("AdvBuff", 10007)
    Random_战力飙升 = ("AdvBuff", 10008)
    Random_腐化契约 = ("AdvBuff", 10009)
    Random_终极时刻 = ("AdvBuff", 10010)
    Random_力场护盾 = ("AdvBuff", 10011)
    Random_力挽狂澜 = ("AdvBuff", 10012)
    Random_英雄契约 = ("AdvBuff", 10013)
    Random_草坪清理大师 = ("AdvBuff", 10014)
    Random_起死回生 = ("AdvBuff", 10015)
    Random_小复制 = ("AdvBuff", 10016)
    Random_共生之礼 = ("AdvBuff", 10017)
    Random_融合召唤 = ("AdvBuff", 10018)
    Random_回收计划 = ("AdvBuff", 10019)
    Tool_手拖车 = ("AdvBuff", 11000)
    究海蘑菇成长 = ("AdvBuff", 11001)
    Shooting_火神质变 = ("AdvBuff", 12000)
    Shooting_炮台质变 = ("AdvBuff", 12001)
    Shooting_死神狙质变 = ("AdvBuff", 12002)
    Shooting_三线雷质变 = ("AdvBuff", 12003)
    Shooting_毁灭嘴质变 = ("AdvBuff", 12004)
    Shooting_曾哥质变 = ("AdvBuff", 12005)
    Shooting_流光伞质变 = ("AdvBuff", 12006)
    Shooting_究玉质变 = ("AdvBuff", 12007)
    Shooting_浴火质变 = ("AdvBuff", 12008)
    Shooting_巨嘴质变 = ("AdvBuff", 12009)
    Shooting_流光裂荚质变 = ("AdvBuff", 12010)
    Shooting_铁豆质变 = ("AdvBuff", 12011)
    Shooting_魅帝菇质变 = ("AdvBuff", 12012)
    Shooting_黑大哥质变 = ("AdvBuff", 12013)
    Shooting_玄钢刺质变 = ("AdvBuff", 12014)
    Shooting_冬笋质变 = ("AdvBuff", 12015)
    Shooting_魔法寒冰质变 = ("AdvBuff", 12016)
    Shooting_西瓜坚果质变 = ("AdvBuff", 12017)
    Shooting_金瓜质变 = ("AdvBuff", 12018)
    Shooting_云杉质变 = ("AdvBuff", 12019)
    Shooting_火菜炮质变 = ("AdvBuff", 12020)
    Shooting_剑仙质变 = ("AdvBuff", 12021)
    Shooting_磁坚质变 = ("AdvBuff", 12022)
    Shooting_竹龙质变 = ("AdvBuff", 12023)
    Shooting_黑高质变 = ("AdvBuff", 12024)
    Shooting_无妄菇质变 = ("AdvBuff", 12025)
    Shooting_激光炮台质变 = ("AdvBuff", 12026)
    Shooting_超级机枪曾哥质变 = ("AdvBuff", 12027)
    Shooting_爆炸保护 = ("AdvBuff", 13000)
    Shooting_护盾保护 = ("AdvBuff", 13001)
    Shooting_木桩1 = ("AdvBuff", 13002)
    Shooting_木桩2 = ("AdvBuff", 13003)
    Shooting_木桩3 = ("AdvBuff", 13004)
    Shooting_木桩Max = ("AdvBuff", 13005)
    Shooting_烈阳1 = ("AdvBuff", 13006)
    Shooting_烈阳2 = ("AdvBuff", 13007)
    Shooting_烈阳3 = ("AdvBuff", 13008)
    Shooting_烈阳Max = ("AdvBuff", 13009)
    Shooting_战锤1 = ("AdvBuff", 13010)
    Shooting_战锤2 = ("AdvBuff", 13011)
    Shooting_战锤3 = ("AdvBuff", 13012)
    Shooting_战锤Max = ("AdvBuff", 13013)
    Shooting_裂空1 = ("AdvBuff", 13014)
    Shooting_裂空2 = ("AdvBuff", 13015)
    Shooting_裂空3 = ("AdvBuff", 13016)
    Shooting_裂空Max = ("AdvBuff", 13017)
    Shooting_明月1 = ("AdvBuff", 13018)
    Shooting_明月2 = ("AdvBuff", 13019)
    Shooting_明月3 = ("AdvBuff", 13020)
    Shooting_明月Max = ("AdvBuff", 13021)
    Shooting_硬化1 = ("AdvBuff", 13022)
    Shooting_硬化2 = ("AdvBuff", 13023)
    Shooting_硬化3 = ("AdvBuff", 13024)
    Shooting_硬化Max = ("AdvBuff", 13025)
    Shooting_交易1 = ("AdvBuff", 13026)
    Shooting_交易2 = ("AdvBuff", 13027)
    Shooting_交易3 = ("AdvBuff", 13028)
    Shooting_交易Max = ("AdvBuff", 13029)
    Shooting_宝藏1 = ("AdvBuff", 13030)
    Shooting_宝藏2 = ("AdvBuff", 13031)
    Shooting_宝藏3 = ("AdvBuff", 13032)
    Shooting_宝藏Max = ("AdvBuff", 13033)
    Shooting_业火1 = ("AdvBuff", 13034)
    Shooting_业火2 = ("AdvBuff", 13035)
    Shooting_业火3 = ("AdvBuff", 13036)
    Shooting_业火Max = ("AdvBuff", 13037)
    Shooting_光棱1 = ("AdvBuff", 13038)
    Shooting_光棱2 = ("AdvBuff", 13039)
    Shooting_光棱3 = ("AdvBuff", 13040)
    Shooting_光棱Max = ("AdvBuff", 13041)
    Shooting_天罚1 = ("AdvBuff", 13042)
    Shooting_天罚2 = ("AdvBuff", 13043)
    Shooting_天罚3 = ("AdvBuff", 13044)
    Shooting_天罚Max = ("AdvBuff", 13045)
    Shooting_全能1 = ("AdvBuff", 13046)
    Shooting_全能2 = ("AdvBuff", 13047)
    Shooting_全能3 = ("AdvBuff", 13048)
    Shooting_全能Max = ("AdvBuff", 13049)
    Shooting_不破不立 = ("AdvBuff", 14000)
    Shooting_两极分化 = ("AdvBuff", 14001)
    Shooting_傲慢之罚 = ("AdvBuff", 14002)
    Shooting_嫉妒之惩 = ("AdvBuff", 14003)
    Shooting_大帝诅咒 = ("AdvBuff", 15000)
    Shooting_大帝祝福 = ("AdvBuff", 15001)
    Shooting_究樱诅咒 = ("AdvBuff", 15002)
    Shooting_究樱祝福 = ("AdvBuff", 15003)
    Shooting_火菜炮诅咒 = ("AdvBuff", 15004)
    Shooting_火菜炮祝福 = ("AdvBuff", 15005)
    Shooting_磁坚诅咒 = ("AdvBuff", 15006)
    Shooting_磁坚祝福 = ("AdvBuff", 15007)

    # Legacy Aliases
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
    ADV_PET_ABYSSAL_CHIBI = ("AdvBuff", 4000)
    ADV_PET_STRIKER_JUNIOR = ("AdvBuff", 4001)
    ADV_PET_PROTOTYPE_ICEBORG = ("AdvBuff", 4002)
    ADV_PET_BABY_JILL = ("AdvBuff", 4003)
    ADV_PET_MINI_POZEIDON = ("AdvBuff", 4004)
    ADV_PET_YOUNG_DUKE = ("AdvBuff", 4005)
    ADV_PET_IMPEROR_HATCHLING = ("AdvBuff", 4006)
    ADV_PET_SKYGLIDER_MECHA = ("AdvBuff", 4007)
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
    ADV_WHEELBARROW_CD_REDUCED = ("AdvBuff", 11000)
    ADV_NAPALM_SHROOM_SEA_OF_FIRE = ("AdvBuff", 12000)
    ADV_APEACALYPSE_FROSTFLAME = ("AdvBuff", 12001)
    ADV_BERSERKER_SNIPEA_CRIT = ("AdvBuff", 12002)
    ADV_THREEPEATATO_MINE_EXPLODE = ("AdvBuff", 12003)
    ADV_DOOM_CHOMPER_EXPLOSIONS = ("AdvBuff", 12004)
    ADV_SHROOMAGEDDON_DEATH_DOOM = ("AdvBuff", 12005)

    # ==========================================
    # ULTIMATE BUFFS (UltiBuff)
    # ==========================================
    嗜血如命 = ("UltiBuff", 0)
    极速吞噬 = ("UltiBuff", 1)
    力大砖飞 = ("UltiBuff", 2)
    快速填装 = ("UltiBuff", 3)
    凛风刺骨 = ("UltiBuff", 4)
    三尺之寒 = ("UltiBuff", 5)
    事半功倍 = ("UltiBuff", 6)
    窝红温了 = ("UltiBuff", 7)
    流星雨 = ("UltiBuff", 8)
    众星之力 = ("UltiBuff", 9)
    万籁俱寂 = ("UltiBuff", 10)
    以爆制爆 = ("UltiBuff", 11)
    见者有份 = ("UltiBuff", 12)
    蒜毒骤发 = ("UltiBuff", 13)
    中心爆破 = ("UltiBuff", 14)
    兵贵神速 = ("UltiBuff", 15)
    世纪之盾 = ("UltiBuff", 16)
    两肋插刀 = ("UltiBuff", 17)
    普度众生 = ("UltiBuff", 18)
    永动机 = ("UltiBuff", 19)
    阻冲之 = ("UltiBuff", 20)
    狂战士 = ("UltiBuff", 21)
    金光闪闪 = ("UltiBuff", 22)
    人造太阳 = ("UltiBuff", 23)
    三位一体 = ("UltiBuff", 24)
    镭射激光 = ("UltiBuff", 25)
    气定神闲 = ("UltiBuff", 26)
    僵尸试图在火海中游泳 = ("UltiBuff", 27)
    厚积薄发 = ("UltiBuff", 28)
    匣中惊喜 = ("UltiBuff", 29)
    无尽贪婪 = ("UltiBuff", 30)
    万劫不复 = ("UltiBuff", 31)
    延时飞刃 = ("UltiBuff", 32)
    生机永驻 = ("UltiBuff", 33)
    深渊巨口 = ("UltiBuff", 34)
    光芒四射 = ("UltiBuff", 35)
    爆米花 = ("UltiBuff", 36)
    超载 = ("UltiBuff", 37)
    连锁反应 = ("UltiBuff", 38)
    大容量 = ("UltiBuff", 39)
    集中轰炸 = ("UltiBuff", 40)
    聚精会神 = ("UltiBuff", 41)
    炙热射线 = ("UltiBuff", 42)
    三昧真火 = ("UltiBuff", 43)
    深海恐惧 = ("UltiBuff", 44)
    群体出动 = ("UltiBuff", 45)
    斩将祭旗 = ("UltiBuff", 46)
    黑曜护体 = ("UltiBuff", 47)
    蓄能帆 = ("UltiBuff", 48)
    能源补偿 = ("UltiBuff", 49)
    极速爆发 = ("UltiBuff", 50)
    精准射击 = ("UltiBuff", 51)
    堡垒1 = ("UltiBuff", 52)
    堡垒2 = ("UltiBuff", 53)
    究炉回韧 = ("UltiBuff", 54)
    究炉恢复 = ("UltiBuff", 55)
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
    二爷无视植物 = ("TravelDebuff", 0)
    二爷免疫状态异常 = ("TravelDebuff", 1)
    黑橄榄禁疗 = ("TravelDebuff", 2)
    黑橄榄易伤 = ("TravelDebuff", 3)
    机鱼加速 = ("TravelDebuff", 4)
    机鱼减伤 = ("TravelDebuff", 5)
    基洛夫加速 = ("TravelDebuff", 6)
    基洛夫加血 = ("TravelDebuff", 7)
    丑跳一定炸 = ("TravelDebuff", 8)
    变身成丑跳 = ("TravelDebuff", 9)
    三叉戟散射 = ("TravelDebuff", 10)
    三叉戟随机叉 = ("TravelDebuff", 11)
    召唤白色撑杆舞王 = ("TravelDebuff", 12)
    白舞王无视植物 = ("TravelDebuff", 13)
    尸王物理伤害 = ("TravelDebuff", 14)
    尸王加速 = ("TravelDebuff", 15)
    冲车投掷多 = ("TravelDebuff", 16)
    冲车提前攻击 = ("TravelDebuff", 17)
    每关黑车 = ("TravelDebuff", 18)
    黑车加速 = ("TravelDebuff", 19)
    蹦极 = ("TravelDebuff", 20)
    阿尔法复苏 = ("TravelDebuff", 21)
    旅行飞碟1 = ("TravelDebuff", 22)
    旅行飞碟2 = ("TravelDebuff", 23)
    特种巨人1 = ("TravelDebuff", 24)
    特种巨人2 = ("TravelDebuff", 25)
    堡巨填装 = ("TravelDebuff", 26)
    堡巨回血 = ("TravelDebuff", 27)
    鱼丸1 = ("TravelDebuff", 28)
    鱼丸2 = ("TravelDebuff", 29)
    战象1 = ("TravelDebuff", 30)
    战象2 = ("TravelDebuff", 31)
    列车1 = ("TravelDebuff", 32)
    列车2 = ("TravelDebuff", 33)
    黑武士1 = ("TravelDebuff", 34)
    黑武士2 = ("TravelDebuff", 35)
    死亡行军 = ("TravelDebuff", 36)
    苦难恶化 = ("TravelDebuff", 37)
    恶意过载 = ("TravelDebuff", 38)
    血肉戏法 = ("TravelDebuff", 39)
    爆裂骸骨 = ("TravelDebuff", 40)
    死追不放 = ("TravelDebuff", 41)
    阳光归零 = ("TravelDebuff", 1000)
    积分归零 = ("TravelDebuff", 1001)
    植物数量限制 = ("TravelDebuff", 1002)
    植物概率死亡 = ("TravelDebuff", 1003)
    高效成长 = ("TravelDebuff", 1004)
    僵尸复活 = ("TravelDebuff", 1005)
    更多僵尸 = ("TravelDebuff", 1006)
    精英部队 = ("TravelDebuff", 1007)
    重症难题 = ("TravelDebuff", 1008)
    永久创伤 = ("TravelDebuff", 1009)
    经济危机 = ("TravelDebuff", 1010)
    急行军 = ("TravelDebuff", 1011)
    荆枝易折 = ("TravelDebuff", 1012)
    领袖强化 = ("TravelDebuff", 1013)
    随从强化 = ("TravelDebuff", 1014)
    空军强化 = ("TravelDebuff", 1015)
    霸凌弱者 = ("TravelDebuff", 1016)
    全民皆兵 = ("TravelDebuff", 1017)
    信息封锁I = ("TravelDebuff", 1018)
    信息封锁II = ("TravelDebuff", 1019)
    特种黄金巨人 = ("TravelDebuff", 2000)
    毁灭机枪二爷 = ("TravelDebuff", 2001)
    特种机械飞碟 = ("TravelDebuff", 2002)
    阿尔法狙击手 = ("TravelDebuff", 2003)
    黑橄榄骑兵团长 = ("TravelDebuff", 2004)
    旗帜黑橄榄高坚果 = ("TravelDebuff", 2005)
    超级寒冰三叉戟 = ("TravelDebuff", 2006)
    究极黑巨 = ("TravelDebuff", 3000)
    黑巨词条 = ("TravelDebuff", 3001)
    究极鬼王 = ("TravelDebuff", 3002)
    鬼王词条 = ("TravelDebuff", 3003)
    究极白车 = ("TravelDebuff", 3004)
    白车词条 = ("TravelDebuff", 3005)
    究极将军 = ("TravelDebuff", 3006)
    将军词条 = ("TravelDebuff", 3007)
    究极马超 = ("TravelDebuff", 3008)
    究极鱼丸 = ("TravelDebuff", 3010)
    究极裂空 = ("TravelDebuff", 3012)
    究极读报 = ("TravelDebuff", 3014)
    究极丑皇 = ("TravelDebuff", 3016)
    究极阿尔法 = ("TravelDebuff", 3018)
    究极大帅 = ("TravelDebuff", 3020)
    大帅词条 = ("TravelDebuff", 3021)
    究极万年不化骨 = ("TravelDebuff", 3022)
    究极海豚 = ("TravelDebuff", 3024)
    究极僵尸火红莲 = ("TravelDebuff", 3026)
    领袖特质_黑巨 = ("TravelDebuff", 4000)
    领袖特质_鬼王 = ("TravelDebuff", 4001)
    领袖特质_将军 = ("TravelDebuff", 4002)
    领袖特质_白车 = ("TravelDebuff", 4003)
    领袖特质_大帅 = ("TravelDebuff", 4004)
    忍无可忍 = ("TravelDebuff", 5000)
    战争激励 = ("TravelDebuff", 5001)
    适应之力 = ("TravelDebuff", 5002)
    格挡反击 = ("TravelDebuff", 5003)
    一马平川 = ("TravelDebuff", 5004)
    Shooting_丢失幸运 = ("TravelDebuff", 10000)
    Shooting_第一轮强化 = ("TravelDebuff", 10001)
    Shooting_第二轮强化 = ("TravelDebuff", 10002)
    Shooting_第三轮强化 = ("TravelDebuff", 10003)
    Shooting_领袖危机 = ("TravelDebuff", 10004)
    Shooting_植物熄火 = ("TravelDebuff", 10005)
    Shooting_榜样激励 = ("TravelDebuff", 10006)
    Shooting_人才引进 = ("TravelDebuff", 10007)
    Shooting_成群结队 = ("TravelDebuff", 10008)
    Shooting_特立独行 = ("TravelDebuff", 10009)
    Shooting_冷冻冬眠 = ("TravelDebuff", 10010)
    Shooting_神魂不稳 = ("TravelDebuff", 10011)
    Shooting_步步紧逼 = ("TravelDebuff", 10012)
    Shooting_抢你小车 = ("TravelDebuff", 10013)
    Shooting_生化危机 = ("TravelDebuff", 10014)
    Shooting_舞影重重 = ("TravelDebuff", 10015)
    Shooting_危机四伏 = ("TravelDebuff", 10016)
    Shooting_英雄退场 = ("TravelDebuff", 10017)
    Shooting_正当防卫 = ("TravelDebuff", 10018)
    Shooting_人才下沉 = ("TravelDebuff", 10019)
    Shooting_老当益壮 = ("TravelDebuff", 10020)
    Shooting_飞来横祸 = ("TravelDebuff", 10021)
    Shooting_幸运贷款 = ("TravelDebuff", 10022)
    Shooting_永眠之地 = ("TravelDebuff", 10023)
    Shooting_闪电突袭 = ("TravelDebuff", 10024)
    Shooting_腐朽之息 = ("TravelDebuff", 10025)
    Shooting_秽土转生 = ("TravelDebuff", 10026)
    Shooting_真实伤害 = ("TravelDebuff", 10027)
    Shooting_同步治疗 = ("TravelDebuff", 10028)
    Shooting_斗转星移 = ("TravelDebuff", 10029)
    Shooting_战个痛快 = ("TravelDebuff", 10030)
    Shooting_小丑派对 = ("TravelDebuff", 10031)
    Shooting_随从号令 = ("TravelDebuff", 10032)
    Shooting_首领号令 = ("TravelDebuff", 10033)
    Shooting_小鬼当家 = ("TravelDebuff", 10034)
    Shooting_膨胀危机 = ("TravelDebuff", 10035)
    Shooting_廉价审美 = ("TravelDebuff", 10036)
    Shooting_高贵审美 = ("TravelDebuff", 10037)
    Shooting_点钻成金 = ("TravelDebuff", 10038)
    Shooting_恃强凌弱 = ("TravelDebuff", 10039)
    Shooting_白银时代 = ("TravelDebuff", 10040)
    Shooting_猫瓜纪元 = ("TravelDebuff", 10041)
    Shooting_积重难返 = ("TravelDebuff", 10042)
    Shooting_无理投资 = ("TravelDebuff", 10043)
    Shooting_命运无常 = ("TravelDebuff", 10044)
    DEBUFF_SUN_RESET_TO_0 = ("TravelDebuff", 1000)
    DEBUFF_POINTS_RESET_TO_0 = ("TravelDebuff", 1001)
    DEBUFF_PLANT_LIMIT_120 = ("TravelDebuff", 1002)
    DEBUFF_PLANT_PERISH_CHANCE = ("TravelDebuff", 1003)
    DEBUFF_ZOMBIE_HP_INCREMENT_ROUND = ("TravelDebuff", 1004)
    DEBUFF_ZOMBIE_REVIVE_CHANCE = ("TravelDebuff", 1005)
    DEBUFF_PLANTS_COST_3X_SUN = ("TravelDebuff", 1010)
    DEBUFF_WAVE_INTERVAL_REDUCED = ("TravelDebuff", 1011)
    DEBUFF_PLANT_DEATH_AOE_SUICIDE = ("TravelDebuff", 1016)


__all__ = ["TravelBuffType"]
