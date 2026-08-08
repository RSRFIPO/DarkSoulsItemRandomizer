class NPCWeaponCategory:
    DAGGER = "dagger"
    STRAIGHT_SWORD = "straight_sword"
    GREATSWORD = "greatsword"
    ULTRA_GREATSWORD = "ultra_greatsword"
    CURVED_SWORD = "curved_sword"
    CURVED_GREATSWORD = "curved_greatsword"
    KATANA = "katana"
    PIERCING_SWORD = "piercing_sword"
    AXE = "axe"
    GREATAXE = "greataxe"
    HAMMER = "hammer"
    GREAT_HAMMER = "great_hammer"
    FIST = "fist"
    SPEAR = "spear"
    HALBERD = "halberd"
    WHIP = "whip"
    SHIELD = "shield"
    CATALYST = "catalyst"
    PYROMANCY_FLAME = "pyromancy_flame"
    TALISMAN = "talisman"
    BOW = "bow"
    CROSSBOW = "crossbow"
    OTHER = "other"

NPC_MELEE_WEAPON_CATEGORIES = [
 NPCWeaponCategory.DAGGER,
 NPCWeaponCategory.STRAIGHT_SWORD,
 NPCWeaponCategory.GREATSWORD,
 NPCWeaponCategory.ULTRA_GREATSWORD,
 NPCWeaponCategory.CURVED_SWORD,
 NPCWeaponCategory.CURVED_GREATSWORD,
 NPCWeaponCategory.KATANA,
 NPCWeaponCategory.PIERCING_SWORD,
 NPCWeaponCategory.AXE,
 NPCWeaponCategory.GREATAXE,
 NPCWeaponCategory.HAMMER,
 NPCWeaponCategory.GREAT_HAMMER,
 NPCWeaponCategory.FIST,
 NPCWeaponCategory.SPEAR,
 NPCWeaponCategory.HALBERD,
 NPCWeaponCategory.WHIP
]

NPC_SWORD_CATEGORIES = [
 NPCWeaponCategory.STRAIGHT_SWORD,
 NPCWeaponCategory.GREATSWORD,
 NPCWeaponCategory.ULTRA_GREATSWORD
]

NPC_CURVED_SWORD_CATEGORIES = [
 NPCWeaponCategory.CURVED_SWORD,
 NPCWeaponCategory.CURVED_GREATSWORD
]

NPC_AXE_CATEGORIES = [
 NPCWeaponCategory.AXE,
 NPCWeaponCategory.GREATAXE
]

NPC_HAMMER_CATEGORIES = [
 NPCWeaponCategory.HAMMER,
 NPCWeaponCategory.GREAT_HAMMER
]

NPC_WEAPON_CATEGORY_PROFILES = {
 6000: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6002: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6003: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6004: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire's Sunlight Maggot
 6540: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6541: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6542: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6543: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6544: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Solaire
 6010: [NPCWeaponCategory.PIERCING_SWORD] + NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD, NPCWeaponCategory.KATANA, NPCWeaponCategory.DAGGER], # Darkmoon Knightess
 6020: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Oscar
 6021: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Oscar
 6030: NPC_CURVED_SWORD_CATEGORIES + [NPCWeaponCategory.DAGGER], # Logan
 6031: NPC_CURVED_SWORD_CATEGORIES + [NPCWeaponCategory.DAGGER], # Logan
 6032: NPC_CURVED_SWORD_CATEGORIES + [NPCWeaponCategory.DAGGER], # Logan
 6040: [NPCWeaponCategory.PIERCING_SWORD] + NPC_CURVED_SWORD_CATEGORIES, # Griggs
 6041: [NPCWeaponCategory.PIERCING_SWORD] + NPC_CURVED_SWORD_CATEGORIES, # Griggs
 6080: NPC_HAMMER_CATEGORIES + NPC_AXE_CATEGORIES, # Petrus
 6090: NPC_HAMMER_CATEGORIES + NPC_AXE_CATEGORIES, # Vince
 6091: NPC_HAMMER_CATEGORIES + NPC_AXE_CATEGORIES, # Vince
 6100: NPC_AXE_CATEGORIES, # Nico
 6101: NPC_AXE_CATEGORIES, # Nico
 6130: NPC_AXE_CATEGORIES + [NPCWeaponCategory.KATANA, NPCWeaponCategory.SPEAR], # Laurentius
 6131: NPC_AXE_CATEGORIES + [NPCWeaponCategory.KATANA, NPCWeaponCategory.SPEAR], # Laurentius
 6180: [NPCWeaponCategory.DAGGER, NPCWeaponCategory.PIERCING_SWORD, NPCWeaponCategory.SPEAR, NPCWeaponCategory.KATANA], # Ingward
 6250: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Crestfallen Merchant
 6260: [NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.CURVED_GREATSWORD], # Domhnall
 6270: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.KATANA], # Crestfallen Warrior
 6271: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.KATANA], # Crestfallen Warrior
 6280: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Siegmeyer
 6281: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Siegmeyer
 6282: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Siegmeyer
 6283: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Siegmeyer
 6284: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Siegmeyer
 6290: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Sieglinde
 6291: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Sieglinde
 6300: [NPCWeaponCategory.CURVED_SWORD, NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.KATANA, NPCWeaponCategory.DAGGER], # Lautrec
 6301: [NPCWeaponCategory.CURVED_SWORD, NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.KATANA, NPCWeaponCategory.DAGGER], # Lautrec
 6590: [NPCWeaponCategory.CURVED_SWORD, NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.KATANA, NPCWeaponCategory.DAGGER], # Lautrec
 6591: [NPCWeaponCategory.CURVED_SWORD, NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.KATANA, NPCWeaponCategory.DAGGER], # Lautrec
 6310: [NPCWeaponCategory.CURVED_GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREATSWORD], # Shiva
 6320: [NPCWeaponCategory.SPEAR, NPCWeaponCategory.HALBERD], # Patches
 6321: [NPCWeaponCategory.SPEAR, NPCWeaponCategory.HALBERD], # Patches
 6370: [NPCWeaponCategory.PIERCING_SWORD, NPCWeaponCategory.DAGGER], # Oswald
 6420: [NPCWeaponCategory.KATANA, NPCWeaponCategory.CURVED_SWORD], # Ninja
 6490: [NPCWeaponCategory.SPEAR, NPCWeaponCategory.HALBERD], # Lautrec's Pike Friend
 6510: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.CURVED_GREATSWORD], # Tarkus
 6530: [NPCWeaponCategory.AXE, NPCWeaponCategory.GREATAXE], # Mildred
 6531: [NPCWeaponCategory.AXE, NPCWeaponCategory.GREATAXE], # Mildred
 6550: [NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.ULTRA_GREATSWORD], # Leeroy
 6551: [NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.ULTRA_GREATSWORD], # Leeroy
 6560: [NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.GREATSWORD], # Kirk
 6561: [NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.GREATSWORD], # Kirk
 6562: [NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.GREATSWORD], # Kirk
 6580: [NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.ULTRA_GREATSWORD], # Havel
 6600: [NPCWeaponCategory.PIERCING_SWORD, NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.CURVED_SWORD], # Ricard
 6610: [NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.HALBERD], # Crystal Knight
 6640: [NPCWeaponCategory.ULTRA_GREATSWORD, NPCWeaponCategory.GREATAXE, NPCWeaponCategory.GREAT_HAMMER, NPCWeaponCategory.GREATSWORD, NPCWeaponCategory.CURVED_GREATSWORD], # Berenike Darkmoon
 6650: [NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.CURVED_SWORD, NPCWeaponCategory.SPEAR, NPCWeaponCategory.HALBERD], # Balder Darkmoon
 6740: [NPCWeaponCategory.DAGGER, NPCWeaponCategory.CURVED_SWORD, NPCWeaponCategory.KATANA], # Ciaran
 6801: NPC_AXE_CATEGORIES + [NPCWeaponCategory.HALBERD], # Forest Bandit
 6802: NPC_SWORD_CATEGORIES + [NPCWeaponCategory.HALBERD], # Forest Knight
 6803: NPC_CURVED_SWORD_CATEGORIES, # Pharis
 6804: [NPCWeaponCategory.STRAIGHT_SWORD, NPCWeaponCategory.SPEAR, NPCWeaponCategory.CURVED_SWORD, NPCWeaponCategory.DAGGER], # Forest Mage
 6805: NPC_HAMMER_CATEGORIES + [NPCWeaponCategory.SPEAR], # Forest Cleric
 6806: [NPCWeaponCategory.DAGGER, NPCWeaponCategory.PIERCING_SWORD, NPCWeaponCategory.KATANA] # Forest Thief
}

def get_npc_weapon_category_from_base_id(base_id):
    if 100000 <= base_id <= 199999 or base_id == 9011000:
        return NPCWeaponCategory.DAGGER
    if 200000 <= base_id <= 299999:
        return NPCWeaponCategory.STRAIGHT_SWORD
    if 300000 <= base_id <= 349999 or base_id in [9012000, 9020000]:
        return NPCWeaponCategory.GREATSWORD
    if 350000 <= base_id <= 399999:
        return NPCWeaponCategory.ULTRA_GREATSWORD
    if 400000 <= base_id <= 449999 or base_id == 9010000:
        return NPCWeaponCategory.CURVED_SWORD
    if 450000 <= base_id <= 499999:
        return NPCWeaponCategory.CURVED_GREATSWORD
    if 500000 <= base_id <= 599999:
        return NPCWeaponCategory.KATANA
    if 600000 <= base_id <= 699999:
        return NPCWeaponCategory.PIERCING_SWORD
    if 700000 <= base_id <= 749999:
        return NPCWeaponCategory.AXE
    if 750000 <= base_id <= 799999 or base_id == 9015000:
        return NPCWeaponCategory.GREATAXE
    if 800000 <= base_id <= 849999:
        return NPCWeaponCategory.HAMMER
    if 850000 <= base_id <= 899999:
        return NPCWeaponCategory.GREAT_HAMMER
    if 900000 <= base_id <= 999999:
        return NPCWeaponCategory.FIST
    if 1000000 <= base_id <= 1099999 or base_id == 9016000:
        return NPCWeaponCategory.SPEAR
    if 1100000 <= base_id <= 1199999:
        return NPCWeaponCategory.HALBERD
    if 1300000 <= base_id <= 1308999 or base_id in [9017000, 9018000]:
        return NPCWeaponCategory.CATALYST
    if 1330000 <= base_id <= 1332999:
        return NPCWeaponCategory.PYROMANCY_FLAME
    if 1360000 <= base_id <= 1367999:
        return NPCWeaponCategory.TALISMAN
    if base_id == 1203000 or base_id == 9021000:
        return NPCWeaponCategory.OTHER
    if 1200000 <= base_id <= 1205999:
        return NPCWeaponCategory.BOW
    if 1250000 <= base_id <= 1253999:
        return NPCWeaponCategory.CROSSBOW
    if 1396000 <= base_id <= 1510999 or 9000000 <= base_id <= 9003999 or base_id == 9014000:
        return NPCWeaponCategory.SHIELD
    if 1600000 <= base_id <= 1699999 or base_id == 9019000:
        return NPCWeaponCategory.WHIP
    return NPCWeaponCategory.OTHER

def get_npc_weapon_category_choices(chr_init_id, original_category):
    if original_category in NPC_MELEE_WEAPON_CATEGORIES:
        return NPC_WEAPON_CATEGORY_PROFILES.get(chr_init_id, [original_category])
    return [original_category]
