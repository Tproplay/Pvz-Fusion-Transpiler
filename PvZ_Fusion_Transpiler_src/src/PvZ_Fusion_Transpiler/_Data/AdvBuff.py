from enum import Enum


class AdvBuff(Enum):
    """AdvBuff enum in PvZ Fusion (TypeDefIndex: 2757).

    Contains all Odyssey / Travel adventure buffs with official English names,
    in-editor effect descriptions in docstrings, and Chinese / legacy aliases.
    """

    CallToArms = 0
    """Call to Arms: Enchantress-shroom Subspecies Unlocked | Empress-shroom & Enchantress-shroom: Summon Interval 30s → 10s"""

    EliteCorps = 1
    """Elite Corps: Empress-shroom & Enchantress-shroom: Can now summon Odyssey Zombies"""

    Overclock = 2
    """Overclock: Gatling Frenzy-shroom Subspecies Unlocked | Gatling Doom: No more rest after firing an Ultimate Doom Shell | Effects also apply to SP variants"""

    Overkill = 3
    """Overkill: Gatling Doom: Now fires an Ultimate Doom Shell every round instead of every 4th round | Gatling Frenzy-shroom: Now fires an Ultimate Doom Shell every 4 attacks | Effects also apply to SP variants"""

    Photosynthesis = 4
    """Photosynthesis: Twin Solar-nut: Click Cost 500 → 200 Sun | Twin Inferno-nut: Healing amount ×2 | Effects also apply to SP variants"""

    Hematopoiesis = 5
    """Hematopoiesis: Twin Inferno-nut Subspecies Unlocked | Twin Solar-nut: Toughness reduces by 10 for each hit instead of 50 | Twin Inferno-nut: Click cost 500 → 200 HP | Effects also apply to SP variants"""

    PathOfPain = 6
    """Path of Pain: Obsidian Spike-nut Subspecies Unlocked | Obsidian Spikerock & Spike-nut: Damage multiplied by 5"""

    SkinOfSteel = 7
    """Skin of Steel: Obsidian Spikerock & Spike-nut: Gains 95% DMG Reduction"""

    PiercingFlame = 8
    """Piercing Flame: Phoenix Drone Subspecies Unlocked | Phoenix Threepeater & Phoenix Drone: Shots can now pierce infinitely and cause Enflamed explosions upon impact | Effects also apply to SP variants"""

    MeltingPoint = 9
    """Melting Point: Phoenix Threepeater & Phoenix Drone: Global enflamed damage bonus 50% → 150%, and regular ignited projectiles can now inflict the debuff  | Effects also apply to SP variants"""

    Shattershot = 10
    """Shattershot: Gatling Icicle-shroom & Sunburst-shroom: Icicles now pierce infinitely and split into two diagonal icicles upon impact the first five times | Effects also apply to SP variants"""

    Icebreaker = 11
    """Icebreaker: Gatling Sunburst-shroom Subspecies Unlocked | Gatling Icicle-shroom: Damage to Frozen/Chill-immune zombies 4× → 12× | Effects also apply to SP variants"""

    PennyPincher = 12
    """Penny Pincher: Radiant Pot: Upgrade costs from Silver Pots to Golden Pots will not exceed 8k"""

    SolarEconomy = 13
    """Solar Economy: Radiant Pot: Coins exceeding the maximum amount will be converted into Sun at a rate of 2:1"""

    SmartShield = 14
    """Smart Shield: Aegis Umbrella Subspecies Unlocked | Midas Umbrella & Aegis Umbrella: Activates Ultimate automatically if zombies are near"""

    HomeRun = 15
    """Home Run: Midas Umbrella: Damage Boost 100% → 300%"""

    DroneMaster = 16
    """Drone Master: Aristocattail: Drone Attack Damage ×3 | Thunder Bunnyon: Summoned Drone is no longer nerfed and fires 60 shots normally"""

    Needlework = 17
    """Needlework: Thunder Bunnyon Subspecies Unlocked | Aristocattail: Regular Attack Damage ×5 | Thunder Bunnyon: Attack Damage ×3"""

    ControlledFusion = 18
    """Controlled Fusion: Avarice-shroom Subspecies Unlocked | Calamity-shroom: All Doom-shroom explosions are now craterless"""

    WarMachine = 19
    """War Machine: Calamity-shroom: Now spawns 3 extra Hypnotized Armored Gargantuars and Zombonis when it explodes"""

    NumismaticEngine = 20
    """Numismatic Engine: Tycoonwood & Magnate Plantern: 1% Damage increase to Coin projectiles/lasers for every 1000 Coins you have"""

    GoldenRain = 21
    """Golden Rain: Magnate Plantern Subspecies Unlocked | Tycoonwood: Coin projectiles now deal splash damage"""

    CrystalDynamo = 22
    """Crystal Dynamo: Boreas Umbrella Subspecies Unlocked | Pharos Umbrella: Energy Limit ×10, Recovery Speed ×20, Healing Speed ×2 | Boreas Umbrella: Damage in Scatter Mode increases linearly up to ×4, Damage in Focus Mode ×4"""

    EnergyFocus = 23
    """Energy Focus: Pharos Umbrella: Normal Attack Damage ×3, Explosion Damage ×10, Attack Interval → 2s | Boreas Umbrella: Cryo-beam in Focus Mode now applies Freeze for 1s"""

    Deadeye = 24
    """Deadeye: Buck-shroom Squad:  Expected Sniper headshot frequency increased to once every 5s | Buck-strike Squadron: Attack damage ×3"""

    ShellShock = 25
    """Shell Shock: Buck-strike Squadron Subspecies Unlocked | Buck-shroom Squad: Flak cannon knockback ×2, attack damage ×3 | Buck-strike Squadron: Attack damage ×3"""

    FluxDrive = 26
    """Flux Drive: Dyson Magnet Subspecies Unlocked | Tesla Magnet: Attack Range ×2 | Dyson Magnet: Metal Production CD halved"""

    Magnetomania = 27
    """Magnetomania: Tesla Magnet: Absorbs 3 Metal Objects at once, damage to Giga Trident-nut Zombies or Giga Football-nut Zombies ×3 | Dyson Magnet: Heal amount ×3, extra Metal Object production limit (3 + (n/m)/4) → (3 + (n/m)/3)"""

    CertainDoom = 28
    """Certain Doom: Wicked Undertater Subspecies Unlocked | Grim Arbiter & Wicked Undertater: Seed packet drop is now guaranteed"""

    EldritchLink = 29
    """Eldritch Link: Grim Arbiter & Wicked Undertater: Zombie Soul damage transfer ×2"""

    LingeringFallout = 30
    """Lingering Fallout: Big Bang Cherry & Big Crunch Squash: Particle Soup initial duration increased from 7s to 10s"""

    ChainReaction = 31
    """Chain Reaction: Big Crunch Squash Subspecies Unlocked | Big Bang Cherry & Big Crunch Squash: Explosive and doom projectiles have a small chance of transforming into Cosmic Debris with 12× damage when they hit zombies"""

    StickierButter = 32
    """Stickier Butter: Cornposter Pot Subspecies Unlocked | Cornveyor Weed & Cornposter Pot: Cornveyor and Cornposter's Butter stun duration ×3"""

    SlideShow = 33
    """Slide Show: Cornveyor Weed: Now makes zombies on it to continuously slide to the right | Cornposter Pot: Butter Chance for the plant above 50% → 100%"""

    MagneticResonance = 34
    """Magnetic Resonance: Omni Pumpkin: On entry, grants all connected Magnetic Plants a Shield equal to 30 × number of Magnetic Plants | Quasar: On entry, resets and grants them an Attack buff of 0.5% × number of Magnetic Plants instead"""

    DualPolarity = 35
    """Dual Polarity: Omni Pumpkin & Quasar: Now counts twice towards the number of Magnetic Plants"""

    ExplosiveBreath = 36
    """Explosive Breath: Pyroboros Pot Subspecies Unlocked | Dragonbreath Torcher: Explosion Frequency ×2"""

    HeatMomentum = 37
    """Heat Momentum: Dragonbreath Torcher: Each zombie hit by Dragonbreath Torcher's fire breath increases the damage of the next hit of that same attack by 1%, stacking up to 400%"""

    ColdFront = 38
    """Cold Front: Oblivion-shroom Subspecies Unlocked | Avalanche-shroom: +100 Initial Energy | Oblivion-shroom: Damage ×2"""

    FrozenHorizon = 39
    """Frozen Horizon: Avalanche-shroom: Attack Radius ×2 | Oblivion-shroom: Attack Interval halved"""

    ArcaneProwess = 40
    """Arcane Prowess: Mesmer Cattail: Ability CD Halved, Ability radius +0.5 tiles"""

    Lovebite = 41
    """Lovebite: Mesmer Cattail: Hypnotized zombies spawned by her ability deal an additional 30% true damage that ignores damage reduction when biting"""

    WeatheringGale = 42
    """Weathering Gale: Quetzalcoatl Blover: Dizzy effect damage bonus 20% → 40%, and attacks reduce DR value by 10"""

    SwiftWinds = 43
    """Swift Winds: Quetzalcoatl Blover: Blover spawning CD 10s → 3s"""

    HatTrick = 44
    """Hat Trick: SP Cryomancer Pea: Everytime Cryomancer Pea's projectile ricochets, its damage increases by 10%. At Level 2, ricochet amount ×3"""

    Spellbound = 45
    """Spellbound: SP Cryomancer Pea: Cryomancer Pea's projectiles now prioritize targetting bosses with the highest HP when ricocheting. At Level 2, zombies hit by ricocheting projectiles take +10% extra damage"""

    SalvageScavenger = 46
    """Salvage Scavenger: Ender Pumpkin Chest: Can store metal objects dropped and uses them to heal Giga Mecha-nuts; prioritizing the one with the lowest HP first"""

    LargeEnderChest = 47
    """Large Ender Chest: Ender Pumpkin Chest: The stack limit for each individual slot is now doubled for all Pumpkin Chests."""

    QuickHands = 1000
    """Quick Hands: Gloves' cooldown is reduced by 10s (No CD for the plant Glove), and can now move Mini-bosses"""

    BackupSupply = 1001
    """Backup Supply: All Plants' recharge is halved"""

    AbundantSun = 1002
    """Abundant Sun: Each Sun now gives more value | 5 → 15 → 25 → 50 → 75"""

    Dexterity = 1003
    """Dexterity: Gloves' cooldown is halved, and can now move Mini-bosses"""

    FastCopy = 1004
    """Fast Copy: Imitater's Recharge: 5mins → 50s"""

    HammerTime = 1005
    """Hammer Time: Mallet's cooldown is reduced to 6s"""

    FlexibleLoadout = 1006
    """Flexible Loadout: You now have the option to re-pick your Plant Loadout during the game"""

    CoupDeGrace = 1007
    """Coup de Grâce: Zombies take an additional 1800 damage when they take more than 1800 damage (after damage reduction)"""

    Strength = 1008
    """Strength: Plants' Damage is increased by 20%"""

    SunderingSmite = 1009
    """Sundering Smite: Zombies receive 20% more damage"""

    Resourcefulness = 1010
    """Resourcefulness: Modifier reroll times +2"""

    Cryostasis = 1011
    """Cryostasis: The freeze time of all zombies is increased by 25%, and the slow rate from chill is increased by 10%"""

    SolarReserve = 1012
    """Solar Reserve: Gain 3000 Sun, then double your total amount of Sun after | Sun Cap 50k → 100k"""

    CherryOnTop = 1013
    """Cherry on Top: True Cherry Bomb: Explosive cherries will now deal at least 1800 damage, have increased explosion range and cause Cremator damage"""

    Recycling = 1014
    """Recycling: Clicking on the same plant when you have it on your Glove will disassemble it at the cost of 500 Sun | 20s cooldown"""

    Phalanx = 1015
    """Phalanx: When two identical plants are placed one above the other (adjacent in the same column), they gain a 50% damage bonus and a 50% damage reduction"""

    RevitalizingCharm = 1016
    """Revitalizing Charm: Hypnotized zombies gain a 500% damage buff and 80% damage reduction (WARNING: Also causes Cherry Newspaper Zombies from Empress/Enchantress-shroom to not lose their newspaper on summon!!)"""

    CosmicCascade = 1017
    """Cosmic Cascade: All Meteors' attack cooldowns are halved | Base Meteor DMG increased by 300 for every Magnetar in the field"""

    Enlightenment = 1018
    """Enlightenment: Adds 4 Lumos Levels for the entire field"""

    SecondWind = 1019
    """Second Wind: After a plant is healed, they heal for 5% of their current health per second for the next 3s (unstackable)"""

    HealingBoost = 1020
    """Healing Boost: Plants gain a 20% healing bonus"""

    ColdsnapInsightI = 1021
    """Coldsnap Insight I: Upgrade Cryomancer Pea to SP Cryomancer Pea (Level 1)"""

    ColdsnapInsightII = 1022
    """Coldsnap Insight II: Upgrade SP Cryomancer Pea to Level 2"""

    Doomsday = 2000
    """Doomsday: True Doom-shroom: Doom Shells will now release a craterless Doom-shroom explosion upon impact"""

    LineFormation = 2001
    """Line Formation: Enable Column Planting"""

    Transcendence = 2002
    """Transcendence: You can upgrade 1 upgradable Epic Modifier"""

    ApexDefender = 2003
    """Apex Defender: If a Plant Type has dealt the highest total damage on the field, its attacks deal an extra 30% of original damage as true damage"""

    TriggerHappy = 2004
    """Trigger Happy: After firing 50 times (25 for catapults), plants gain an unlimited attack speed for 1s"""

    LifeSteal = 2005
    """Life Steal: Plants gain 1% life steal, applied to the plant with the lowest HP percentage on the field"""

    AmbushTactics = 2006
    """Ambush Tactics: The longer since a zombie was last damaged, the more damage it takes from the next hit. <1s: Damage * (1 + 9t); ≥1s: Damage * (10 + 9ln(t))"""

    CorruptingTouch = 2007
    """Corrupting Touch: All zombies are now under the Corruption effect: each time a zombie is damaged, the next instance of damage to that zombie is increased by 5% (stacks infinitely)"""

    Purification = 2008
    """Purification: You can remove 1 non-mini-boss Zombie Modifier from the View Modifier menu"""

    BlazeOfGlory = 2009
    """Blaze of Glory: When hypnotized zombies die, they explode, dealing damage equal to 150% of their max HP to nearby zombies"""

    MomentumSync = 2010
    """Momentum Sync: For each 1% attack speed bonus a plant gains, it also receives 1% attack damage bonus"""

    EternalBulwark = 3000
    """Eternal Bulwark: When Cherrizilla and Obsidian Tall-nut (or their subspecies) are both present, Cherrizilla/Garlizilla no longer has a maximum Toughness cap, and Obsidian Tall-nut/Obsidian Mine gains a 90% damage reduction"""

    AstralConvergence = 3001
    """Astral Convergence: If there are at least 6 Magnetars and 6 Helios Cabbages on the field, the Mini Sun summoned by the Helios Cabbage will never disappear, and will keep summoning Helios Meteors, while Magnetars can consume sun for more damage but can only attacks its lane"""

    TotalFirepower = 3002
    """Total Firepower: Gatling Cherrybomber now spreads its shots evenly across three lanes with sine and cosine trajectories, Jalapeno blasts Infernal Squashwoods acquire properties of Cherry Bomb explosions, and explosive cherries deal more damage proportionate to number of Gatling Cherrybombers after passing through Infernal Squashwoods"""

    CelestialBeacon = 3003
    """Celestial Beacon: When there are at least 6 Magnetars and 6 Selene Cabbages on the field, Selene's summoned Mini Moon will not disappear and each Selene provides massive Lumos levels, while Magnetars deal extra damage to the zombie with the highest amount of HP"""

    EventHorizon = 3004
    """Event Horizon: Hail melons from Maelonstrom's Nebula Rifts now deal 6× damage and create Singularities, and Cosmo-pult always lob Ultimate Black Holes. When an Ultimate Black Hole collapses, it also detonates all Singularities to further increase its own damage"""

    HeavensWrath = 3005
    """Heaven's Wrath: Click on a reloaded Vulcannon while holding an Epic Twin Inferno-nut with the Glove to make all reloaded Vulcannon on the field perform a synergized attack towards the sky. Every 8th Inferno Shell shot calls down an Inferno Meteor dealing 80× damage, decimating all zombies on the screen"""

    BulletHell = 3006
    """Bullet Hell: When Cherrybomber Drone is placed above Epic Gatling Frenzy-shroom, the more they attack, the more bullets they fire in the next volley. This bonus decays after they stop attacking. (WARNING: Will lead to cancerous amounts of projectiles!!)"""

    Ultranova = 3007
    """Ultranova: Photon Splitter can lock onto any Atomheart Plantern ahead (click to select) to charge it. When energy exceeds 10k, its brightness increases, dealing heavy damage and slowing zombies in its radius. At 100k, collapses into a black hole and explodes, devastating all zombies on screen. (WARNING: Contains flashing lights)"""

    LittleMiracle = 3008
    """Little Miracle: When Litter-pult and SP Gatling Icicle-shroom are planted on the same tile, the latter's projectiles split one additional time. Both plants' normal and special projectiles inherit some properties from each other's shots. (WARNING: Will cause lag)"""

    ElementalFury = 3009
    """Elemental Fury: Doominator now spawns Obsidian Tall-nut Iceclaw Zombies, Napalm-shroom's main projectile will split into an additional Obsidian Melon; dealing AoE damage equal to the melon's original attack power which increases by 100% for each ice, snow and fire plant present on the lawn, and a synergy between the Enflamed and Chill debuffs is unlocked"""

    OmnicidalInferno = 3010
    """Omnicidal Inferno: Infernal Sparkwood now ignites the lawn instead of a single lane on spawning Spicy plant. SP Phoenix Threepeater and Drone projectiles splits into all lanes on passing through Infernal Sparkwood"""

    AbyssalChibi = 4000
    """Abyssal Chibi: Summons an Abyssal Chibi to fight for you (replaces current Pet). His hammer smash damages both nearby plants and zombies, grants damage reduction to affected plants, and deals increased damage to zombies based on nearby plants' HP. Hammer effects scale with XP level."""

    StrikerJunior = 4001
    """Striker Junior: Summons a Striker Junior to fight for you (replaces current Pet). Every 3s, he moves to the plant with the lowest HP percentage and rallies the area, healing nearby plants and increasing damage taken by zombies. Rally effects scale with xp level"""

    PrototypeIceborg = 4002
    """Prototype Iceborg: Summons a Prototype Iceborg to fight for you (replaces current Pet). She targets the highest-HP lane and fires ice projectiles. Damage increases based on the number of chilled/frozen zombies, and gains infinite pierce & bonus xp if the Iceborg Executrix is on the field. Projectile damage scale with xp level"""

    BabyJill = 4003
    """Baby Jill: Summons a Baby Jill to fight for you (replaces current Pet). Every 15s, she performs a random attack: summons high-tier hypnotized Clown-in-the-Box zombies per lane or throws out explosives (lane-wide or global). Explosion damage scales with xp level"""

    MiniPozeidon = 4004
    """Mini Pozeidon: Summons a Mini Pozeidon to fight for you (replaces current Pet). Every 5s, he throws his trident ahead, which pierces and damages zombies with explosions. If the mini-boss Pozeidon is present, throws 4 tridents in each lane every 10s instead"""

    YoungDuke = 4005
    """Young Duke: Summons a Young Duke to fight for you (replaces current Pet). Rapidly fires iron pea bullets forward, and every 20 seconds she summons a column of mini warhorses to charge at the zombies and create Zombie Souls of the ones they hit. If the mini-boss Archduke Deathrider is present, her summoning interval is halved. (WARNING: Will cause MASSIVE lag!!)"""

    ImperorHatchling = 4006
    """Imperor Hatchling: Summons an Imperor Hatchling to fight for you (replaces current Pet). Every 10 seconds, he will transform a certain number of zombies (based on XP level) into Chicken Jockey or Hydrofowl Zombies. If the mini-boss Imperor's Ark of the Duck is present, the maximum number of transformations is doubled."""

    SkygliderMecha = 4007
    """Skyglider Mecha: Summons a Skyglider Mecha to fight for you (replaces current Pet). Increases damage from plant-side Jack-in-the-Box explosions, and fires an explosive at zombies every 1.5s (every 3rd attack is fired across each row). If the mini-boss Skystrider Mecha is present, the pet's attack interval is halved."""

    GoliathSlayer = 5000
    """Goliath Slayer: Plants deal +100% to Mini-bosses and Bosses"""

    AdverseAdaptation = 5001
    """Adverse Adaptation: Plants gain a 5% damage bonus for every Zombie Modifier you have"""

    DivineBlade = 5002
    """Divine Blade: Unlock Swordsage Starfruit"""

    CurseOfPride = 5003
    """Curse of Pride: Odyssey Plants' Attack and max HP reduced by 90%, but all other plants now have 40× Attack & max HP, and 2× Attack Speed"""

    CurseOfGreed = 5004
    """Curse of Greed: Seed packets no longer need recharge but each use costs 15× their base Sun + 50% of the player's current Sun"""

    FinalFrontier = 6000
    """Final Frontier: Lawnmowers: Final damage +200%, Attack speed +300%"""

    CherrizillaMasteryI = 6001
    """Cherrizilla Mastery I: Cherrizilla: Healing Power +100%"""

    CherrizillaMasteryII = 6002
    """Cherrizilla Mastery II: Cherrizilla: Attack Damage +50%"""

    GatlingCherrybomberMasteryI = 6003
    """Gatling Cherrybomber Mastery I: Gatling Cherrybomber: Cherry and other variants of projectiles' explosion radius +50% and damage +100%"""

    GatlingCherrybomberMasteryII = 6004
    """Gatling Cherrybomber Mastery II: Gatling Cherrybomber: Cherry and other variants of projectiles' explosion radius -50%  but damage +300%"""

    DoominatorMasteryI = 6005
    """Doominator Mastery I: Doominator: Frozen zombies take +50% more damage"""

    DoominatorMasteryII = 6006
    """Doominator Mastery II: Doominator: Hypnotized zombies deal 3× damage"""

    InfernalSquashwoodMasteryI = 6007
    """Infernal Squashwood Mastery I: Infernal Squashwood: Jalapeno effect changes from instant to DoT, dealing 1/3 the original damage 10 times within 1s"""

    InfernalSquashwoodMasteryII = 6008
    """Infernal Squashwood Mastery II: Infernal Squashwood: Grants projectiles +50% damage before igniting them"""

    BacklineBastion = 6009
    """Backline Bastion: Plants in the fifth column get 50% increased maximum Toughness and 50% damage reduction. Each column to the left reduces damage cap by 10% and increases damage reduction by 10%"""

    SPEvolution_DoomGatling = 7000
    """SP Evolution: Unlock SP Gatling Doom and SP Gatling Frenzy-shroom
    Use Doom-shroom to upgrade
    """

    SPEvolution_TwinNut = 7001
    """SP Evolution: Unlock SP Twin Solar-nut and SP Twin Inferno-nut
    Use Wall-nut to upgrade
    """

    SPEvolution_Phoenix = 7002
    """SP Evolution: Unlock SP Phoenix Threepeater and SP Phoenix Drone
    Use Jalapeno to upgrade
    """

    SPEvolution_GatlingIcicle = 7003
    """SP Evolution: Unlock SP Gatling Icicle-shroom and SP Gatling Sunburst-shroom
    Use Peashooter to upgrade
    """

    SolarGrace = 10000
    """Solar Grace: Immediately gain 100k Sun | Sun Cap +100k"""

    GigaGuardian = 10001
    """Giga Guardian: Immediately gain 3 Giga Mecha-nut seed packets which start with 640k HP"""

    InstantPromotion = 10002
    """Instant Promotion: Upgrade (1+n) random plants to Tier 1, where n is the number of Plant modifiers you currently have"""

    Accelerator = 10003
    """Accelerator: Increase the speed of (1+n) random plants, where n is the number of Plant modifiers you currently have"""

    TotemOfUndying = 10004
    """Totem of Undying: The next time zombies reach the house, it is ignored for 3s and knock all zombies back to the start"""

    SupplyDrop = 10005
    """Supply Drop: Obtain a Pumpkin Chest that has many seed packets for Odyssey Fusions (no Subspecies)"""

    DeusExMachina = 10006
    """Deus Ex Machina: Knock all zombies back to the start, then instantly defeat all zombies"""

    WintersChosenOne = 10007
    """Winter's Chosen One: Gain a Super Blizzard Commando with +1500% damage and HP, +1000% speed, and gain an extra Coldsnap Bean"""

    HeatRiser = 10008
    """Heat Riser: Gain a random Odyssey plant. Each new zombie wave, it gains +25% damage, +25% HP, and +10% speed"""

    PactOfCorruption = 10009
    """Pact of Corruption: Gain a Shroomageddon seed packet. Planting it ACCEPTS the challenge:
    Summon 3-6 random Odyssey zombies in each lane (yeah, ALL possible ones)
    Defeat them all to unlock the Modifier "Corrupting Touch"
    """

    LimitBreak = 10010
    """Limit Break: All plant attack damage ×2"""

    ForceShield = 10011
    """Force Shield: All plants gain 50 + (2% max HP) shield per second"""

    TheLastDitch = 10012
    """The Last Ditch: When you have 20 or more plants on the field, zombies reaching the house no longer results in game over, but causes all plants to have 1/3 chance to die instead"""

    PactOfPromotion = 10013
    """Pact of Promotion: Gain an Omni Pumpkin seed packet. Planting it ACCEPTS the challenge:
    The number of zombies in the next 20 waves are doubled
    Get through and all plants on the Omni Pumpkin's tile will be promoted to Tier 3
    """

    LawnSweeper = 10014
    """Lawn Sweeper: Unleash all current lawnmowers and restore one full column of them"""

    DelayOfFate = 10015
    """Delay of Fate: You will not game over if you manage to kill the zombie reaching your house within 1.5s"""

    CloneArmy = 10016
    """Clone Army: Immediately gain 5 Imitater seed packets"""

    SharedRoots = 10017
    """Shared Roots: Upon gaining a second copy of any plant for the first time, you receive an additional seed packet of that plant"""

    EvolutionCatalyst = 10018
    """Evolution Catalyst: Using the glove to move a plant onto another plant of the same type and tier upgrades it by 1 tier"""

    FateReforged = 10019
    """Fate Reforged: Immediately gain 10 Golden Recycling Vases. Additionally, receive 1 per wave and 5 per flag (huge wave)"""

    SpeedyDeployment = 11000
    """Speedy Deployment: Level gimmick: Wheelbarrow's cooldown is reduced to 3 seconds"""

    InstantGrowth = 11001
    """Instant Growth: Level gimmick: Deucalion-shroom starts with 1000 Growth Stages"""

    Ascend_Inferno = 12000
    """Ascend: Inferno: Napalm-shroom's melons create an extra sea of fire upon hitting the ground and can split up to 2 more times when hitting zombies"""

    Ascend_Burst = 12001
    """Ascend: Burst: When Apeacalypse Minigun is casting its ultimate ability, they will release 4 extra waves of Frostflame dealing 50 instances of damage each. Each instance deals damage equal to 10,000% of the turret's attack power to a random zombie in range"""

    Ascend_TrueAim = 12002
    """Ascend: True Aim: Berserker Snipea's critical hit will now be guaranteed"""

    Ascend_Blasting = 12003
    """Ascend: Blasting: Threepeatato-mine's projectiles will now trigger a Potato Mine explosion when hitting a zombie"""

    Ascend_Doom = 12004
    """Ascend: Doom: When Doom Chomper attacks, it will trigger a Doom explosion regardless of if it swallows a zombie or not. If it swallows a zombie, it will trigger two Doom explosions"""

    Ascend_Oblivion = 12005
    """Ascend: Oblivion: Shroomageddon releases a 1-million damage Doom-shroom explosion upon death"""

    Ascend_ShieldOfLight = 12006
    """Ascend: Shield of Light: Pharos Umbrella can consume energy to knock back zombies in a 3×3 area and regular attacks can have ×3 targets"""

    Ascend_Gravity = 12007
    """Ascend: Gravity: Black holes will attract zombies with less than 50% max HP"""

    Ascend_Penetration = 12008
    """Ascend: Penetration: Phoenix Threepeater now shoots in all lanes and its projectiles pierce infinitely"""

    Ascend_TheMaw = 12009
    """Ascend: The Maw: Tyrannoflora Lux attraction range after digestion is vastly increased"""

    Ascend_ChaosBeam = 12010
    """Ascend: Chaos Beam: Adjacent 2 Celestial Beams releases mini black hole explosions periodically"""

    Ascend_Ricochet = 12011
    """Ascend: Ricochet: Buck-shroom Squad can no longer headshot but projectiles ricochet on lawn edges (like Split Pea), up to (number of pierces + 2) times"""

    Ascend_Veterancy = 12012
    """Ascend: Veterancy: Empress-shroom now summons zombies with greatly increased stats"""

    Ascend_Density = 12013
    """Ascend: Density: Buckshot Commando shoots even larger, stronger projectiles during Ultimate Moves"""

    Ascend_Hemorrhage = 12014
    """Ascend: Hemorrhage: Zombies targeted by any Spikerock continuously lose HP equal to 400% the attack for 2s"""

    Ascend_Fortune = 12015
    """Ascend: Fortune: Soulrender Bamboo can now follow mouse movements with attack speed upgrades increasing the movement speed, deal damage to any zombies caught in its way"""

    Ascend_Decryption = 12016
    """Ascend: Decryption: Zombies that spawn will be cursed with 3 stacks of Decryption Magic. Every wave, the zombie with the highest HP will gain 100 stacks of Decryption. Each stack increases the damage a zombie takes by 100%, and when a zombie cursed with Decryption dies their stacks will be spread to nearby zombies."""

    Ascend_Clusterbomb = 12017
    """Ascend: Clusterbomb: Melon-nut's projectile explodes mid-air and splits into several Mini Watermelons thrown at zombies across the field"""

    Ascend_GoldenBarrage = 12018
    """Ascend: Golden Barrage: Golden Melon's Ultimate additionally launches Golden melons at all zombies, and the Ultimate's split count ×2"""

    Ascend_HardenedSaw = 12019
    """Ascend: Hardened Saw: Lifereaver Spruce's projectiles gain an additional 0.6% of its current Shield as Attack Damage, capped at 300% of its base Attack"""

    Ascend_TotalEruption = 12020
    """Ascend: Total Eruption: Kaledera Eruptor's targeting range is +1 lane above and below, and fires at all targets simultaneously (if the number of targets is less than the max scatter count, the leftover shots are evenly distributed among the targets) | Projectile flight time reduced by 50%"""

    Ascend_Swordsmanship = 12021
    """Ascend: Swordsmanship: For every 2 giant swords summoned Swordsage Starfruit, each attack additionally fires 1 spinning shortsword"""

    Ascend_CircleOfDeath = 12022
    """Ascend: Circle of Death: Projectiles surrounding Mag-nut can now pierce infinitely, but their duration is reduced to 10s"""

    Ascend_Conflagration = 12023
    """Ascend: Conflagration: Dragonbreath Torcher's attacks additionally release Jalapeno effects in all lanes"""

    Ascend_Gigantism = 12024
    """Ascend: Gigantism: Obsidian Tall-nut and its holographic projections have vastly larger hitboxes and are immune to crushing from bosses
    Healing CD: 15s → 10s
    """

    Ascend_Evocation = 12025
    """Ascend: Evocation: Hypnotized Abyssal Gargantuar spawns hypnotized Abyssal Imp when smashing"""

    Ascend_MagicalIndex = 12026
    """Ascend: Magical Index: Apeacalypse Railgun now fires a continuous light beam"""

    Ascend_Sorrow = 12027
    """Ascend: Sorrow: Melancholy Commando now always unleashes its Ultimate, but with half the projectiles"""

    BlastProtection = 13000
    """Blast Protection: Damage from Zombie Jack-in-the-Box explosions is reduced to 1000"""

    EnchantedShield = 13001
    """Enchanted Shield: Plants with Shield recover HP equal to 0.1% of their Shield every second"""

    VoodooDummy = 13002
    """Voodoo Dummy: Summons a Dummy Zombie on the lawn which distributes 60% of damage taken equally among all zombies; can be moved with Zombie Glove.
    Instantly eliminates touched hypnotized zombies
    """

    VoodooDummy_A = 13003
    """Voodoo Dummy - A: The Dummy Zombie now distributes 100% of the damage it takes among all zombies"""

    VoodooDummy_B = 13004
    """Voodoo Dummy - B: Summons an additional Dummy Zombie"""

    VoodooDummy_X = 13005
    """Voodoo Dummy - X: When the Dummy Zombie takes damage, it also deals 100% of that damage to the zombie with the highest HP on the lawn"""

    SolarBlast = 13006
    """Solar Blast: Summons a Solar Reactor that periodically damages all zombies on the lawn"""

    SolarBlast_A = 13007
    """Solar Blast - A: Reduces the Solar Reactor's attack CD by 50%"""

    SolarBlast_B = 13008
    """Solar Blast - B: Increases the Solar Reactor's damage by 100%"""

    SolarBlast_X = 13009
    """Solar Blast - X: The Solar Reactor additionally calls down a Helios Meteor whenever it attacks"""

    Warhammer = 13010
    """Warhammer: Reduces the Mallet's damage, but reduces its CD to 3s"""

    Warhammer_A = 13011
    """Warhammer - A: Greatly increases the effective range of the Mallet's attack"""

    Warhammer_B = 13012
    """Warhammer - B: Further reduces the Mallet's CD"""

    Warhammer_X = 13013
    """Warhammer - X: When the Mallet hits a zombie, summons a large hammer at its location that continuously damages zombies before disappearing after a while"""

    GFishBomber = 13014
    """G-fish Bomber: A Skyglider Mecha will fight for you"""

    GFishBomber_A = 13015
    """G-fish Bomber - A: Number of attacks required for Skyglider Mecha to fire a Barrage -1"""

    GFishBomber_B = 13016
    """G-fish Bomber - B: Reduces Skyglider Mecha's attack CD"""

    GFishBomber_X = 13017
    """G-fish Bomber - X: Barrage shells from Skyglider Mecha can keep splitting while airborne"""

    MoonlightVeil = 13018
    """Moonlight Veil: Summons a Lunar Reactor that periodically restores HP to all plants on the lawn"""

    MoonlightVeil_A = 13019
    """Moonlight Veil - A: Greatly increases the amount of HP restored by the Lunar Reactor"""

    MoonlightVeil_B = 13020
    """Moonlight Veil - B: Grants all plants on the lawn a 1000-HP shield whenever the Lunar Reactor activates"""

    MoonlightVeil_X = 13021
    """Moonlight Veil - X: Whenever the Lunar Reactor activates, moonlight descends upon every plant on the lawn, which instantly kills regular Zombies within a 3x3 area and makes plants invincible for a short time"""

    IronCurtain = 13022
    """Iron Curtain: Reduces damage taken by all plants by 20%"""

    IronCurtain_A = 13023
    """Iron Curtain - A: Reduces damage taken by all plants by 40%"""

    IronCurtain_B = 13024
    """Iron Curtain - B: Reduces damage taken by all plants by 60%"""

    IronCurtain_X = 13025
    """Iron Curtain - X: Reduces damage taken by all plants by 90%; whenever a plant loses HP, it fires a pea projectile from its position with damage equal to its max HP | If the zombie has the Counterstrike Modifier, effect is changed to reducing damage taken by 99%"""

    LuckLoan = 13026
    """Luck • Loan: Gain one Modifier draw at 500 Luck, then lose 25 Luck"""

    LuckLoan_A = 13027
    """Luck • Loan - A: Gain one Modifier draw at 1000 Luck, then lose 50 Luck"""

    LuckLoan_B = 13028
    """Luck • Loan - B: Gain one Modifier draw at 1500 Luck, then lose 75 Luck"""

    LuckLoan_X = 13029
    """Luck • Loan - X: Set your Luck to 250 immediately and Rerolls to 5, triple your Luck cap, and permanently prevent you from selecting Luck Modifiers and [Resourcefulness]
    Each Modifier draw grants 25 Luck, plus an additional amount equal to 20% of your current Luck (up to 100); choosing Bronze, Silver, Gold/Random, or Diamond/Prismatic/Curse costs 20/40/60/100 Luck respectively; each reroll costs 50 Luck
    """

    LuckBounty = 13030
    """Luck • Bounty: Immediately spawns a wave of zombies with 2× HP and speed; defeating all of them grants a Modifier draw at 500 Luck"""

    LuckBounty_A = 13031
    """Luck • Bounty - A: Immediately spawns a wave of zombies with 3× HP and speed; defeating all of them grants a Modifier draw at 1000 Luck"""

    LuckBounty_B = 13032
    """Luck • Bounty - B: Immediately spawns a wave of zombies with 4× HP and speed; defeating all of them grants a Modifier draw at 1500 Luck"""

    LuckBounty_X = 13033
    """Luck • Bounty - X: Immediately doubles your current Luck and Luck cap (if your Luck is negative, its absolute value is taken before doubling, e.g.: -50 Luck → 100)"""

    InfernalCombustion = 13034
    """Infernal Combustion: Clicking anywhere releases an Infernal Combustion at the clicked location, with a 10s CD, or 1 second if it kills a zombie"""

    InfernalCombustion_A = 13035
    """Infernal Combustion - A: Increases Infernal Combustion damage by 100%"""

    InfernalCombustion_B = 13036
    """Infernal Combustion - B: Decreases Infernal Combustion CD and CD on kill by 50%"""

    InfernalCombustion_X = 13037
    """Infernal Combustion - X: Infernal Combustion can now damage plants; killing a plant triggers Jalapeno effects on all lanes and refreshes the CD; damage increases based on the total number of Modifiers the plant has"""

    PrismFighter = 13038
    """Prism Fighter: Gains a Mecha Fighter that continuously locks onto and attacks the leftmost zombie"""

    PrismFighter_A = 13039
    """Prism Fighter - A: Increases the number of refractions of Mecha Fighter's attack by 1"""

    PrismFighter_B = 13040
    """Prism Fighter - B: Increases the number of refractions of Mecha Fighter's attack by 2"""

    PrismFighter_X = 13041
    """Prism Fighter - X: Mecha Figher's Prism attacks gain infinite pierce, and refractions can hit the same target repeatedly"""

    LightningStorm = 13042
    """Lightning Storm: Summons Lightning Bolts to fight for you, periodically damaging zombies on the lawn"""

    LightningStorm_A = 13043
    """Lightning Storm - A: Increases Lightning Bolt duration by 100%"""

    LightningStorm_B = 13044
    """Lightning Storm - B: Increases Lightning Bolt attack frequency by 100%"""

    LightningStorm_X = 13045
    """Lightning Storm - X: The Lightning Bolts now attack continuously without interruption"""

    Omnipotence = 13046
    """Omnipotence: Increase Luck by 25, overall attack damage by 10%, 1 reroll, and respawn timer reduction by 10%"""

    Omnipotence_A = 13047
    """Omnipotence - A: Increase Luck by 50, overall attack damage by 20%, 2 rerolls, and respawn timer reduction by 20%"""

    Omnipotence_B = 13048
    """Omnipotence - B: Increase Luck by 75, overall attack damage by 10%, 3 rerolls, and respawn timer reduction by 30%"""

    Omnipotence_X = 13049
    """Omnipotence - X: All plants on the lawn receive 500% bonus HP, 300% independent bonus attack damage, 200% bonus attack speed, 60% crit chance and 150% crit damage"""

    NoPainsNoGains = 14000
    """No Pains No Gains: Kill all of your plants, and halve the independent damage and speed buffs for all your plants;
    The same will happen after 20 waves, but this time the buffs are doubled
    """

    AllOrNothing = 14001
    """All or Nothing: If your Luck is below 75, immediately set it to 75. When not protected by the pity system, Silver and Golden modifiers are downgraded to Bronze quality, while Diamond ones are upgraded to Prismatic quality"""

    HighGrounds = 14002
    """High Grounds: Plants deal 30% more damage when above zombies and 30% less damage when below zombies, determined by their vertical sprite positions on the screen"""

    PredatorInstinct = 14003
    """Predator Instinct: Plants deal 30% more damage to zombies that are above 50% health, and 30% less damage to those below 50% health"""

    CurseOfMCDXXXVII = 15000
    """Curse of MCDXXXVII: Magnetar's attack speed is halved. After 1,437 attacks, reverse the curse, with each volley counting as 5 attacks
    Reversal effect: Quasar projectiles from Magnetar gain an additional 1,437 base damage
    """

    BlessingOfMCDXXXVII = 15001
    """Blessing of MCDXXXVII: Quasar projectiles from Magnetar gain an additional 1,437 base damage"""

    CurseOfAggression = 15002
    """Curse of Aggression: Gatling Cherrybomber's damage is reduced by 50%. After dealing a cumulative 300M damage, reverse the curse
    Reversal effect: Each time Gatling Cherrybomber attacks, it additionally fires several projectiles from the left side of the screen, with attack equal to 0.0001% of the cumulative damage dealt by other plants
    """

    BlessingOfAggression = 15003
    """Blessing of Aggression: Each time Gatling Cherrybomber attacks, it additionally fires several projectiles from the left side of the screen, with attack equal to 0.0001% of the cumulative damage dealt by other plants"""

    CurseOfEquity = 15004
    """Curse of Equity: For each target Kaledera Eruptor has, its projectile damage is reduced by 1%, up to a max reduction of 70%. After a cumulative reduction of 50,000% through this effect, reverse the curse
    Reversal effect: For each target Kaledera Eruptor has, its projectile damage is increased by 1%
    """

    BlessingOfEquity = 15005
    """Blessing of Equity: For each target Kaledera Eruptor has, its projectile damage is increased by 1%"""

    CurseOfEndurance = 15006
    """Curse of Endurance: Mag-nut no longer fires projectiles. After attracting 5,000 projectiles, reverse the curse
    Reversal effect: Each time Mag-nut attacks, it additionally fires one projectile of the type it has attracted the most
    """

    BlessingOfEndurance = 15007
    """Blessing of Endurance: Each time Mag-nut attacks, it additionally fires one projectile of the type it has attracted the most"""

    # ==========================================================================
    # Chinese Aliases for Backward Compatibility
    # ==========================================================================
    撒豆成兵 = 0
    精兵强将 = 1
    枕戈待旦 = 2
    核能威慑 = 3
    妙手回春 = 4
    无关痛痒 = 5
    尸愁之路 = 6
    百炼成钢 = 7
    百步穿杨 = 8
    怒火攻心 = 9
    势如破竹 = 10
    冻彻心扉 = 11
    多多益善 = 12
    等价交换 = 13
    人工智能 = 14
    弹射起步 = 15
    特制弹药 = 16
    一针见血 = 17
    可控核聚变 = 18
    人多势众 = 19
    大富翁 = 20
    好运连连 = 21
    量子护盾 = 22
    高能射线 = 23
    枪枪爆头 = 24
    开炮 = 25
    电磁涡轮 = 26
    万磁王 = 27
    罪恶之力 = 28
    深度定制 = 29
    核能射线 = 30
    链式反应 = 31
    尸愁之路II = 32
    滑滑梯 = 33
    磁力护盾 = 34
    磁能科技 = 35
    爆裂连珠 = 36
    烈火锋芒 = 37
    冷寂寒冰1 = 38
    冷寂寒冰2 = 39
    泳池派对 = 40
    爱与记忆 = 41
    风刃 = 42
    狂风肆虐 = 43
    举世无双 = 44
    聪明绝顶 = 45
    自动化升级 = 46
    堆叠升级 = 47
    至极手速 = 1000
    全息制冷 = 1001
    熠熠生辉 = 1002
    极速战备 = 1003
    复制中心 = 1004
    运斤如风 = 1005
    全副武装 = 1006
    致命一击 = 1007
    强力打击 = 1008
    精准打击 = 1009
    合理投资 = 1010
    极致之冰 = 1011
    聚光盆 = 1012
    真樱 = 1013
    拆分 = 1014
    连连看 = 1015
    肉身成圣 = 1016
    斗转星移 = 1017
    灯火通明 = 1018
    强心针 = 1019
    高效恢复 = 1020
    魔力升级 = 1021
    魔力升级II = 1022
    真毁 = 2000
    排山倒海 = 2001
    升级 = 2002
    绝对力量 = 2003
    爽快射击 = 2004
    生命偷取 = 2005
    过载 = 2006
    腐化 = 2007
    净化 = 2008
    定时炸弹 = 2009
    电力相生 = 2010
    我是传奇 = 3000
    星神合一 = 3001
    火力全开 = 3002
    星月护符 = 3003
    永寂新星 = 3004
    力量会给予希望 = 3005
    无限火力 = 3006
    超新星爆发 = 3007
    小小作战 = 3008
    元素反应 = 3009
    星火燎原 = 3010
    迷你巨人 = 4000
    迷你将军 = 4001
    迷你雪皇 = 4002
    迷你丑皇 = 4003
    迷你渊海 = 4004
    迷你大帅 = 4005
    迷你鬼王 = 4006
    迷你基洛夫 = 4007
    Curse_巨人杀手 = 5000
    Curse_诅咒之力 = 5001
    Curse_诸神黄昏 = 5002
    Curse_倒反天罡 = 5003
    Curse_贪婪诅咒 = 5004
    Rogue_后备能源 = 6000
    Rogue_究极樱桃战神专精I = 6001
    Rogue_究极樱桃战神专精II = 6002
    Rogue_究极樱桃射手专精I = 6003
    Rogue_究极樱桃射手专精II = 6004
    Rogue_究极大喷菇专精I = 6005
    Rogue_究极大喷菇专精II = 6006
    Rogue_究极窝炬专精I = 6007
    Rogue_究极窝炬专精II = 6008
    Rogue_推车保护 = 6009
    UltimateDoomGatling = 7000
    UltimateSunNut = 7001
    SuperThreePeater_sp = 7002
    UltimateSnowGatlingPuff = 7003
    Random_超多阳光 = 10000
    Random_鱼丸护体 = 10001
    Random_超级高手 = 10002
    Random_唯快不破 = 10003
    Random_不死图腾 = 10004
    Random_应有尽有 = 10005
    Random_规则之力 = 10006
    Random_英雄登场 = 10007
    Random_战力飙升 = 10008
    Random_腐化契约 = 10009
    Random_终极时刻 = 10010
    Random_力场护盾 = 10011
    Random_力挽狂澜 = 10012
    Random_英雄契约 = 10013
    Random_草坪清理大师 = 10014
    Random_起死回生 = 10015
    Random_小复制 = 10016
    Random_共生之礼 = 10017
    Random_融合召唤 = 10018
    Random_回收计划 = 10019
    Tool_手拖车 = 11000
    究海蘑菇成长 = 11001
    Shooting_火神质变 = 12000
    Shooting_炮台质变 = 12001
    Shooting_死神狙质变 = 12002
    Shooting_三线雷质变 = 12003
    Shooting_毁灭嘴质变 = 12004
    Shooting_曾哥质变 = 12005
    Shooting_流光伞质变 = 12006
    Shooting_究玉质变 = 12007
    Shooting_浴火质变 = 12008
    Shooting_巨嘴质变 = 12009
    Shooting_流光裂荚质变 = 12010
    Shooting_铁豆质变 = 12011
    Shooting_魅帝菇质变 = 12012
    Shooting_黑大哥质变 = 12013
    Shooting_玄钢刺质变 = 12014
    Shooting_冬笋质变 = 12015
    Shooting_魔法寒冰质变 = 12016
    Shooting_西瓜坚果质变 = 12017
    Shooting_金瓜质变 = 12018
    Shooting_云杉质变 = 12019
    Shooting_火菜炮质变 = 12020
    Shooting_剑仙质变 = 12021
    Shooting_磁坚质变 = 12022
    Shooting_竹龙质变 = 12023
    Shooting_黑高质变 = 12024
    Shooting_无妄菇质变 = 12025
    Shooting_激光炮台质变 = 12026
    Shooting_超级机枪曾哥质变 = 12027
    Shooting_爆炸保护 = 13000
    Shooting_护盾保护 = 13001
    Shooting_木桩1 = 13002
    Shooting_木桩2 = 13003
    Shooting_木桩3 = 13004
    Shooting_木桩Max = 13005
    Shooting_烈阳1 = 13006
    Shooting_烈阳2 = 13007
    Shooting_烈阳3 = 13008
    Shooting_烈阳Max = 13009
    Shooting_战锤1 = 13010
    Shooting_战锤2 = 13011
    Shooting_战锤3 = 13012
    Shooting_战锤Max = 13013
    Shooting_裂空1 = 13014
    Shooting_裂空2 = 13015
    Shooting_裂空3 = 13016
    Shooting_裂空Max = 13017
    Shooting_明月1 = 13018
    Shooting_明月2 = 13019
    Shooting_明月3 = 13020
    Shooting_明月Max = 13021
    Shooting_硬化1 = 13022
    Shooting_硬化2 = 13023
    Shooting_硬化3 = 13024
    Shooting_硬化Max = 13025
    Shooting_交易1 = 13026
    Shooting_交易2 = 13027
    Shooting_交易3 = 13028
    Shooting_交易Max = 13029
    Shooting_宝藏1 = 13030
    Shooting_宝藏2 = 13031
    Shooting_宝藏3 = 13032
    Shooting_宝藏Max = 13033
    Shooting_业火1 = 13034
    Shooting_业火2 = 13035
    Shooting_业火3 = 13036
    Shooting_业火Max = 13037
    Shooting_光棱1 = 13038
    Shooting_光棱2 = 13039
    Shooting_光棱3 = 13040
    Shooting_光棱Max = 13041
    Shooting_天罚1 = 13042
    Shooting_天罚2 = 13043
    Shooting_天罚3 = 13044
    Shooting_天罚Max = 13045
    Shooting_全能1 = 13046
    Shooting_全能2 = 13047
    Shooting_全能3 = 13048
    Shooting_全能Max = 13049
    Shooting_不破不立 = 14000
    Shooting_两极分化 = 14001
    Shooting_傲慢之罚 = 14002
    Shooting_嫉妒之惩 = 14003
    Shooting_大帝诅咒 = 15000
    Shooting_大帝祝福 = 15001
    Shooting_究樱诅咒 = 15002
    Shooting_究樱祝福 = 15003
    Shooting_火菜炮诅咒 = 15004
    Shooting_火菜炮祝福 = 15005
    Shooting_磁坚诅咒 = 15006
    Shooting_磁坚祝福 = 15007

    # ==========================================================================
    # Legacy Aliases
    # ==========================================================================
    ADV_ENCHANTRESS_SUBSPECIES = 0
    ADV_ENCHANTRESS_ODYSSEY = 1
    ADV_GATLING_FRENZY_NO_REST = 2
    ADV_GATLING_FRENZY_EVERY_4 = 3
    ADV_TWIN_SOLAR_REDUCE_COST = 4
    ADV_TWIN_INFERNO_SUBSPECIES = 5
    ADV_OBSIDIAN_SPIKE_DAMAGE = 6
    ADV_OBSIDIAN_SPIKE_REDUCTION = 7
    ADV_PHOENIX_DRONE_SUBSPECIES = 8
    ADV_PHOENIX_THREEPEATER_BUFF = 9
    ADV_GATLING_ICICLE_PIERCE = 10
    ADV_GATLING_SUNBURST_SUBSPECIES = 11
    ADV_RADIANT_POT_GOLDEN_LIMIT = 12
    ADV_RADIANT_POT_COIN_CONVERSION = 13
    ADV_AEGIS_UMBRELLA_AUTO = 14
    ADV_MIDAS_UMBRELLA_BOOST = 15
    ADV_ARISTOCATTAIL_DRONE_DMG = 16
    ADV_THUNDER_BUNNYON_SUBSPECIES = 17
    ADV_AVARICE_SHROOM_CRATERLESS = 18
    ADV_CALAMITY_SHROOM_SPAWNS = 19
    ADV_TYCOONWOOD_COIN_LASER = 20
    ADV_MAGNATE_PLANTERN_SUBSPECIES = 21
    ADV_PHAROS_UMBRELLA_LIMIT = 22
    ADV_BOREAS_UMBRELLA_CRYOBEAM = 23
    ADV_BUCK_SHROOM_HEADSHOT = 24
    ADV_BUCK_STRIKE_SUBSPECIES = 25
    ADV_TESLA_MAGNET_RANGE = 26
    ADV_DYSON_MAGNET_LIMIT = 27
    ADV_GRIM_ARBITER_GUARANTEED = 28
    ADV_WICKED_UNDERTAKER_SOUL = 29
    ADV_BIG_BANG_SOUP_DURATION = 30
    ADV_BIG_CRUNCH_SUBSPECIES = 31
    ADV_CORNVEYOR_WEED_BUTTER = 32
    ADV_CORNPOSTER_POT_CHANCE = 33
    ADV_OMNI_PUMPKIN_SHIELD = 34
    ADV_QUASAR_MAGNETIC_COUNT = 35
    ADV_DRAGONBREATH_FREQUENCY = 36
    ADV_DRAGONBREATH_STACKING = 37
    ADV_TUNDRAL_GLACIER_ENERGY = 38
    ADV_LETHAL_GLACIER_SUBSPECIES = 39
    ADV_MESMER_CATTAIL_RADIUS = 40
    ADV_MESMER_CATTAIL_TRUE_DMG = 41
    ADV_GLOVE_COOLDOWN_REDUCED = 1000
    ADV_PLANT_RECHARGE_HALVED = 1001
    ADV_SUN_VALUE_UPGRADE = 1002
    ADV_GLOVE_HALF_CD = 1003
    ADV_IMITATER_FAST_RECHARGE = 1004
    ADV_MALLET_CD_REDUCED = 1005
    ADV_MID_GAME_LOADOUT_REPICK = 1006
    ADV_MASSIVE_DAMAGE_PROC = 1007
    ADV_PLANT_DMG_BOOST_20 = 1008
    ADV_ZOMBIE_RECEIVE_MORE_DMG = 1009
    ADV_MODIFIER_REROLL_PLUS_2 = 1010
    ADV_FREEZE_TIME_INCREASED = 1011
    ADV_DOUBLE_SUN_CAP_100K = 1012
    ADV_TRUE_CHERRY_CREMATOR = 1013
    ADV_GLOVE_DISASSEMBLE_PLANT = 1014
    ADV_VERTICAL_STACK_BONUS = 1015
    ADV_HYPNO_ZOMBIE_MASSIVE_BUFF = 1016
    ADV_METEOR_CD_HALVED = 1017
    ADV_ADD_4_LUMOS_LEVELS = 1018
    ADV_HYPNO_DEATH_EXPLOSION = 1019
    ADV_HEAL_REGENERATION_BUFF = 1020
    ADV_PLANT_HEALING_BONUS_20 = 1021
    ADV_TRUE_DOOM_SHROOM = 2000
    ADV_COLUMN_PLANTING_ENABLED = 2001
    ADV_UPGRADE_EPIC_MODIFIER = 2002
    ADV_TOP_DAMAGE_TRUE_DAMAGE = 2003
    ADV_UNLIMITED_ATTACK_SPEED_1S = 2004
    ADV_PLANT_LIFE_STEAL_1 = 2005
    ADV_DAMAGE_DELAY_SCALING = 2006
    ADV_CORRUPT_SAC_EFFECT = 2007
    ADV_REMOVE_NON_MINIBOSS_MOD = 2008
    ADV_SYNERGY_CHERRIZILLA_OBSIDIAN = 3000
    ADV_SYNERGY_MAGNETAR_HELIOS = 3001
    ADV_SYNERGY_CHERRYBOMBER_SINE = 3002
    ADV_SYNERGY_MAGNETAR_SELENE = 3003
    ADV_SYNERGY_MAELONSTROM_QUANTUM = 3004
    ADV_SYNERGY_VULCANNON_INFERNO = 3005
    ADV_SYNERGY_CHERRYBOMBER_GATLING = 3006
    ADV_SYNERGY_PHOTON_ATOMHEART = 3007
    ADV_SYNERGY_LITTERPULT_ICICLE = 3008
    ADV_SYNERGY_DOOMINATOR_NAPALM = 3009
    ADV_PET_ABYSSAL_CHIBI = 4000
    ADV_PET_STRIKER_JUNIOR = 4001
    ADV_PET_PROTOTYPE_ICEBORG = 4002
    ADV_PET_BABY_JILL = 4003
    ADV_PET_MINI_POZEIDON = 4004
    ADV_PET_YOUNG_DUKE = 4005
    ADV_PET_IMPEROR_HATCHLING = 4006
    ADV_PET_SKYGLIDER_MECHA = 4007
    ADV_BOSS_DAMAGE_BONUS_100 = 5000
    ADV_PLANT_DMG_PER_MODIFIER = 5001
    ADV_UNLOCK_SWORDSAGE_STARFRUIT = 5002
    ADV_GLASS_CANNON_MODIFIER = 5003
    ADV_SEED_PACKET_SUN_TAX = 5004
    ADV_LAWNMOWER_MAXIMUM_MASTERY = 6000
    ADV_CHERRIZILLA_MASTERY_HEAL = 6001
    ADV_CHERRIZILLA_MASTERY_DMG = 6002
    ADV_GATLING_CHERRY_MASTERY_RADIUS = 6003
    ADV_GATLING_CHERRY_MASTERY_DMG = 6004
    ADV_DOOMINATOR_MASTERY_FROZEN = 6005
    ADV_DOOMINATOR_MASTERY_HYPNO = 6006
    ADV_INFERNAL_SQUASH_MASTERY_DOT = 6007
    ADV_INFERNAL_SQUASH_MASTERY_BUFF = 6008
    ADV_FIFTH_COLUMN_TOUGHNESS = 6009
    ADV_INSTANT_100K_SUN = 10000
    ADV_INSTANT_GIGA_MECHA_NUT = 10001
    ADV_INSTANT_TIER_1_UPGRADE = 10002
    ADV_INSTANT_PLANT_SPEEDRUN = 10003
    ADV_UNDYING_TOTEM_ACQUIRED = 10004
    ADV_EPIC_PUMPKIN_STORAGE = 10005
    ADV_FULL_BOARD_CLEAR_KNOCKBACK = 10006
    ADV_SUPER_BLIZZARD_COMMANDO = 10007
    ADV_EVOLVING_ODYSSEY_PLANT = 10008
    ADV_SHROOMAGEDDON_CHALLENGE = 10009
    ADV_GLOBAL_PLANT_DMG_X2 = 10010
    ADV_REGENERATING_SHIELD = 10011
    ADV_SAURIAN_MEDALLION = 10012
    ADV_OMNI_PUMPKIN_CHALLENGE = 10013
    ADV_LAWNMOWER_RESTORATION = 10014
    ADV_LAST_SECOND_HOUSE_SAVE = 10015
    ADV_IMMEDIATE_5_IMITATERS = 10016
    ADV_DUPLICATE_COPY_BONUS = 10017
    ADV_GLOVE_MERGE_UPGRADE = 10018
    ADV_GOLDEN_RECYCLING_VASES = 10019
    ADV_WHEELBARROW_CD_REDUCED = 11000
    ADV_NAPALM_SHROOM_SEA_OF_FIRE = 12000
    ADV_APEACALYPSE_FROSTFLAME = 12001
    ADV_BERSERKER_SNIPEA_CRIT = 12002
    ADV_THREEPEATATO_MINE_EXPLODE = 12003
    ADV_DOOM_CHOMPER_EXPLOSIONS = 12004
    ADV_SHROOMAGEDDON_DEATH_DOOM = 12005


__all__ = ["AdvBuff"]
