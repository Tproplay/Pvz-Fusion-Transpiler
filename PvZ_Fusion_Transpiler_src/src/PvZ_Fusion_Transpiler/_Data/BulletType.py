from enum import Enum, EnumMeta

class BulletTypeMeta(EnumMeta):
    def __getattr__(cls, name: str):
        cand = "Bullet_" + name
        if cand in cls._member_map_:
            return cls._member_map_[cand]
        cand_lower = cand.lower()
        name_lower = name.lower()
        for k, v in cls._member_map_.items():
            k_lower = k.lower()
            if k_lower == cand_lower or k_lower == name_lower:
                return v
        for k, v in cls._member_map_.items():
            k_clean = k[7:] if k.startswith("Bullet_") else k
            if k_clean.lower().startswith(name_lower):
                return v
        raise AttributeError(f"type object '{cls.__name__}' has no attribute '{name}'")

    def __getitem__(cls, name: str):
        try:
            return super().__getitem__(name)
        except KeyError:
            cand = "Bullet_" + name
            if cand in cls._member_map_:
                return cls._member_map_[cand]
            cand_lower = cand.lower()
            name_lower = name.lower()
            for k, v in cls._member_map_.items():
                k_lower = k.lower()
                if k_lower == cand_lower or k_lower == name_lower:
                    return v
            for k, v in cls._member_map_.items():
                k_clean = k[7:] if k.startswith("Bullet_") else k
                if k_clean.lower().startswith(name_lower):
                    return v
            raise


class BulletType(Enum, metaclass=BulletTypeMeta):
    Bullet_pea = 0
    Bullet_cherry = 1
    Bullet_nut = 2
    Bullet_superCherry = 3
    Bullet_zombieBlock = 4
    Bullet_zombieBlock2 = 5
    Bullet_zombieBlock3 = 6
    Bullet_potato = 7
    Bullet_smallSun = 8
    Bullet_puff = 9
    Bullet_puffPea = 10
    Bullet_ironPea = 11
    Bullet_threeSpike = 12
    Bullet_puffRandomColor = 13
    Bullet_puffLove = 14
    Bullet_snowPea = 15
    Bullet_snowPuffPea = 16
    Bullet_iceSpark = 17
    Bullet_smallIceSpark = 18
    Bullet_magicTrack = 20
    Bullet_snowPuff = 21
    Bullet_blackPuff = 22
    Bullet_doom = 23
    Bullet_iceDoom = 24
    Bullet_firePea_yellow = 25
    Bullet_firePea_orange = 26
    Bullet_firePea_red = 27
    Bullet_squash = 28
    Bullet_kelp = 29
    Bullet_fireKelp = 30
    Bullet_squashKelp = 32
    Bullet_normalTrack = 33
    Bullet_iceTrack = 34
    Bullet_fireTrack = 35
    Bullet_cherrySquash = 36
    Bullet_cactus = 37
    Bullet_lanternCactus_glow = 38
    Bullet_star = 39
    Bullet_lanternStar = 40
    Bullet_seaStar = 41
    Bullet_cactusStar = 42
    Bullet_jackboxStar = 43
    Bullet_pickaxeStar = 44
    Bullet_magnetStar = 45
    Bullet_ironStar = 46
    Bullet_magnetCactus = 47
    Bullet_superStar = 48
    Bullet_ultimateStar = 49
    Bullet_firePea_small = 50
    Bullet_sword = 51
    Bullet_cabbage = 52
    Bullet_sunCabbage = 53
    Bullet_kernal = 54
    Bullet_butter = 55
    Bullet_bigKernal = 56
    Bullet_bigButter = 57
    Bullet_basketball = 58
    Bullet_melon = 59
    Bullet_winterMelon = 60
    Bullet_garlicKernal = 61
    Bullet_garlicButter = 62
    Bullet_garlicCabbage = 63
    Bullet_garlicMelon = 64
    Bullet_cannon = 65
    Bullet_cornMelon = 66
    Bullet_butterMelon = 67
    Bullet_fireCannon = 68
    Bullet_iceCannon = 69
    Bullet_cabbageMelon = 70
    Bullet_superMelon = 71
    Bullet_ultimateMelon = 72
    Bullet_melonCannon = 73
    Bullet_silverCabbage = 74
    Bullet_goldCabbage = 75
    Bullet_silverKernal = 76
    Bullet_goldKernal = 77
    Bullet_silverButter = 78
    Bullet_goldButter = 79
    Bullet_smallGoldCannon = 80
    Bullet_silverMelon = 81
    Bullet_goldMelon = 82
    Bullet_goldMelonCannon = 83
    Bullet_ultimateCannon = 84
    Bullet_ultimateKernal = 85
    Bullet_fireMelon = 86
    Bullet_firePea_super = 87
    Bullet_garlicBomb = 89
    Bullet_puffIronPea = 90
    Bullet_lourCactus = 91
    Bullet_puffPotato = 92
    Bullet_steelPea = 93
    Bullet_shulkLeaf = 94
    Bullet_sunSpike = 95
    Bullet_endoSun = 96
    Bullet_extremeSnowPea = 97
    Bullet_silverCoin = 98
    Bullet_goldCoin = 99
    Bullet_ultimateCactus = 100
    Bullet_snowBall = 101
    Bullet_doomCactus = 102
    Bullet_bigMelon = 103
    Bullet_fireStar = 104
    Bullet_fireCherry = 105
    Bullet_lanternCactus_dark = 106
    Bullet_firePea_ultimate = 107
    Bullet_redIronPea = 108
    Bullet_normalSun = 109
    Bullet_firePea_purple = 110
    Bullet_springMelon = 111
    Bullet_smallKernal = 112
    Bullet_smallButter = 113
    Bullet_portalPea = 114
    Bullet_goldSquashKelp = 115
    Bullet_ironPea_air = 116
    Bullet_kernal_magnet = 117
    Bullet_butter_magnet = 118
    Bullet_kernal_portal = 119
    Bullet_butter_portal = 120
    Bullet_kernal_iron = 121
    Bullet_butter_iron = 122
    Bullet_pea_doom = 123
    Bullet_pea_doom_fire = 124
    Bullet_doom_fire = 125
    Bullet_doom_big = 126
    Bullet_spruce = 127
    Bullet_spruceShulk = 128
    Bullet_icePeach = 129
    Bullet_passionFruit = 130
    Bullet_passionFruit2 = 131
    Bullet_water = 132
    Bullet_iceBlock = 133
    Bullet_water_big = 134
    Bullet_iceBlock_big = 135
    Bullet_shulkLeaf_water = 136
    Bullet_iceBlock_recover = 137
    Bullet_shulkLeaf_ice = 138
    Bullet_lotusSpruce = 139
    Bullet_kernal_ultimate = 140
    Bullet_BlackHole_gold = 141
    Bullet_shulkLeaf_ultimate = 142
    Bullet_iceSword = 143
    Bullet_fireStar_red = 144
    Bullet_cherryStar = 145
    Bullet_jalaStar = 146
    Bullet_ultimateStar_fire = 147
    Bullet_spruceBallista = 148
    Bullet_waterBallista = 149
    Bullet_waterBallista2 = 150
    Bullet_spruce_bamboo = 151
    Bullet_doom_throw = 152
    Bullet_hypnoPea = 153
    Bullet_hypnoPea_fire = 154
    Bullet_puff_cherry = 155
    Bullet_melon_small = 156
    Bullet_cabbage_small = 157
    Bullet_melon_hypno = 158
    Bullet_ultimatePuff = 159
    Bullet_corn_ulti = 160
    Bullet_butter_ulti = 161
    Bullet_cabbage_ulti = 162
    Bullet_melon_ulti = 163
    Bullet_watercan = 164
    Bullet_ultimateSun = 165
    Bullet_ultimateExplodeCannon = 166
    Bullet_cherryJalapeno = 167
    Bullet_helmetPea = 168
    Bullet_lunarCabbage = 169
    Bullet_redLunarCabbage = 170
    Bullet_puffNut = 171
    Bullet_melon_magnet = 172
    Bullet_melon_iron = 173
    Bullet_melon_portal = 174
    Bullet_pea_jala = 175
    Bullet_winterMelon_ultimate = 176
    Bullet_pea_garlic = 177
    Bullet_pea_threeCherry = 178
    Bullet_pea_bombCherry = 179
    Bullet_ultimateCattail = 180
    Bullet_nuclear = 181
    Bullet_seaShroom = 182
    Bullet_smallIceSpark_skin2 = 183
    Bullet_cannon_sun = 184
    Bullet_lourCactus1 = 185
    Bullet_squashMelon = 186
    Bullet_melonCannon2 = 187
    Bullet_cabbage_explode = 188
    Bullet_ultimateStar_magic = 189
    Bullet_ultimateStar_fire_magic = 190
    Bullet_fireStar_magic = 191
    Bullet_cannon_jalaNut = 192
    Bullet_starFume = 193
    Bullet_doom_ulti = 194
    Bullet_doom_big_ulti = 195
    Bullet_kernal_squash = 196
    Bullet_butter_squash = 197
    Bullet_iceTrack_big = 198
    Bullet_star_ifv = 199
    Bullet_cabbage_ice = 200
    Bullet_kernal_ice = 201
    Bullet_butter_ice = 202
    Bullet_squashCabbage = 203
    Bullet_helmetPea_black = 204
    Bullet_helmetPea_black_fire = 205
    Bullet_firePea_garlic = 206
    Bullet_poisonSpark = 207
    Bullet_smallIceSpark_sp = 208
    Bullet_sunSpike_sp = 209
    Bullet_shadow_poison = 210
    Bullet_cabbage_fire = 211
    Bullet_cabbage_ulti2 = 212
    Bullet_melon_ulti2 = 213
    Bullet_butter_ulti2 = 214
    Bullet_corn_ulti2 = 215
    Bullet_ultimatePuff2 = 216
    Bullet_smallIceSpark_sp2 = 217
    Bullet_smallIceSpark2 = 218
    Bullet_cabbage_doom = 219
    Bullet_kernal_jala = 220
    Bullet_butter_jala = 221
    Bullet_springMelon_obsidian = 222
    Bullet_doomMelon = 223
    Bullet_snowBall_black = 224
    Bullet_kernal_doom = 225
    Bullet_butter_doom = 226
    Bullet_pea_star = 227
    Bullet_magicTrack_hypno = 228
    Bullet_ironPea_curse = 229
    Bullet_petKirov = 230
    Bullet_potato_explode = 231
    Bullet_nut_fire = 232
    Bullet_jackbox_black = 233
    Bullet_cactus_ice = 234
    Bullet_squash_doom = 235
    Bullet_squash_bigDoom = 236
    Bullet_squash_doom_ulti = 237
    Bullet_squash_bigDoom_ulti = 238
    Bullet_steelPea_fire = 239
    Bullet_pea_chomper = 240
    Bullet_helmetPea_black_big = 241
    Bullet_cabbage_three = 242
    Bullet_star_ice = 243
    Bullet_sword_ulti = 244
    Bullet_pea2 = 245
    Bullet_star_garlic = 246
    Bullet_lunarEssence = 247
    Bullet_pea_curse = 248
    Bullet_star_holy = 249
    Bullet_ultimateStar_solar = 250
    Bullet_ultimateStar_lunar = 251
    Bullet_ultimateMelon1 = 252
    Bullet_cactus_green = 253
    Bullet_ultimateStar_lunar_fire = 254
    Bullet_ultimateStar_solar_fire = 255
    Bullet_lostMachine_red = 256
    Bullet_puff_green = 257


__all__ = ["BulletType", "BulletTypeMeta"]
