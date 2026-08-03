from npc_weapon_categories import NPCWeaponCategory

# Static candidate pool for NPC weapon randomization. Requirements are sourced
# from the Dark Souls Remastered weapon/shield community tables and cross-
# checked against the local item IDs from the Meowmaritus item table gist.
# Pyromancy flames are intentionally excluded because their NPC visual impact
# is low and the few original flame slots should remain unchanged.
NPC_WEAPON_POOL = {
 100000: (NPCWeaponCategory.DAGGER, 5, 8, 0, 0), # Dagger
 101000: (NPCWeaponCategory.DAGGER, 5, 14, 0, 0), # Parrying Dagger
 102000: (NPCWeaponCategory.DAGGER, 5, 0, 0, 0), # Ghost Blade
 103000: (NPCWeaponCategory.DAGGER, 6, 12, 0, 0), # Bandit's Knife
 104000: (NPCWeaponCategory.DAGGER, 6, 20, 0, 0), # Priscilla's Dagger
 200000: (NPCWeaponCategory.STRAIGHT_SWORD, 8, 10, 0, 0), # Shortsword
 201000: (NPCWeaponCategory.STRAIGHT_SWORD, 10, 10, 0, 0), # Longsword
 202000: (NPCWeaponCategory.STRAIGHT_SWORD, 10, 10, 0, 0), # Broadsword
 204000: (NPCWeaponCategory.STRAIGHT_SWORD, 10, 14, 0, 0), # Balder Side Sword
 205000: (NPCWeaponCategory.STRAIGHT_SWORD, 16, 10, 0, 0), # Crystal Straight Sword
 206000: (NPCWeaponCategory.STRAIGHT_SWORD, 12, 12, 0, 0), # Sunlight Straight Sword
 207000: (NPCWeaponCategory.STRAIGHT_SWORD, 10, 10, 0, 0), # Barbed Straight Sword
 208000: (NPCWeaponCategory.STRAIGHT_SWORD, 16, 22, 0, 0), # Silv. Knight Str. Sword
 209000: (NPCWeaponCategory.STRAIGHT_SWORD, 10, 10, 0, 14), # Astora's Straight Sword
 210000: (NPCWeaponCategory.STRAIGHT_SWORD, 16, 16, 0, 0), # Darksword
 211000: (NPCWeaponCategory.STRAIGHT_SWORD, 16, 10, 0, 0), # Drake Sword
 300000: (NPCWeaponCategory.GREATSWORD, 16, 10, 0, 0), # Bastard Sword
 301000: (NPCWeaponCategory.GREATSWORD, 16, 10, 0, 0), # Claymore
 302000: (NPCWeaponCategory.GREATSWORD, 24, 0, 0, 0), # Man-serpent Greatsword
 303000: (NPCWeaponCategory.GREATSWORD, 16, 14, 0, 0), # Flamberge
 304000: (NPCWeaponCategory.GREATSWORD, 20, 10, 0, 0), # Crystal Greatsword
 306000: (NPCWeaponCategory.GREATSWORD, 40, 10, 0, 0), # Stone Greatsword
 307000: (NPCWeaponCategory.GREATSWORD, 24, 18, 20, 20), # Greatsword of Artorias
 309000: (NPCWeaponCategory.GREATSWORD, 16, 10, 28, 0), # Moonlight Greatsword
 310000: (NPCWeaponCategory.GREATSWORD, 20, 18, 0, 0), # Black Knight Sword
 311000: (NPCWeaponCategory.GREATSWORD, 24, 18, 20, 20), # Greatsword of Artorias
 314000: (NPCWeaponCategory.GREATSWORD, 20, 10, 0, 0), # Great Lord Greatsword
 350000: (NPCWeaponCategory.ULTRA_GREATSWORD, 24, 10, 0, 0), # Zweihander
 351000: (NPCWeaponCategory.ULTRA_GREATSWORD, 28, 10, 0, 0), # Greatsword
 352000: (NPCWeaponCategory.ULTRA_GREATSWORD, 40, 0, 0, 0), # Demon Great Machete
 354000: (NPCWeaponCategory.ULTRA_GREATSWORD, 50, 10, 0, 0), # Dragon Greatsword
 355000: (NPCWeaponCategory.ULTRA_GREATSWORD, 32, 18, 0, 0), # Black Knight Greatsword
 400000: (NPCWeaponCategory.CURVED_SWORD, 7, 13, 0, 0), # Scimitar
 401000: (NPCWeaponCategory.CURVED_SWORD, 9, 13, 0, 0), # Falchion
 402000: (NPCWeaponCategory.CURVED_SWORD, 9, 14, 0, 0), # Shotel
 403000: (NPCWeaponCategory.CURVED_SWORD, 7, 0, 0, 0), # Jagged Ghost Blade
 405000: (NPCWeaponCategory.CURVED_SWORD, 7, 20, 0, 0), # Painting Guardian Sword
 406000: (NPCWeaponCategory.CURVED_SWORD, 11, 13, 0, 0), # Quelaag's Furysword
 450000: (NPCWeaponCategory.CURVED_GREATSWORD, 24, 13, 0, 0), # Server
 451000: (NPCWeaponCategory.CURVED_GREATSWORD, 28, 13, 0, 0), # Murakumo
 453000: (NPCWeaponCategory.CURVED_GREATSWORD, 24, 13, 0, 0), # Gravelord Sword
 500000: (NPCWeaponCategory.KATANA, 14, 14, 0, 0), # Uchigatana
 501000: (NPCWeaponCategory.KATANA, 20, 16, 0, 0), # Washing Pole
 502000: (NPCWeaponCategory.KATANA, 14, 20, 0, 0), # Iaito
 503000: (NPCWeaponCategory.KATANA, 16, 14, 0, 0), # Chaos Blade
 600000: (NPCWeaponCategory.PIERCING_SWORD, 5, 12, 0, 0), # Mail Breaker
 601000: (NPCWeaponCategory.PIERCING_SWORD, 7, 12, 0, 0), # Rapier
 602000: (NPCWeaponCategory.PIERCING_SWORD, 10, 12, 0, 0), # Estoc
 603000: (NPCWeaponCategory.PIERCING_SWORD, 8, 16, 16, 0), # Velka's Rapier
 604000: (NPCWeaponCategory.PIERCING_SWORD, 8, 20, 0, 0), # Ricard's Rapier
 700000: (NPCWeaponCategory.AXE, 8, 8, 0, 0), # Hand Axe
 701000: (NPCWeaponCategory.AXE, 12, 8, 0, 0), # Battle Axe
 702000: (NPCWeaponCategory.AXE, 18, 12, 0, 16), # Crescent Axe
 703000: (NPCWeaponCategory.AXE, 24, 0, 0, 0), # Butcher Knife
 704000: (NPCWeaponCategory.AXE, 36, 8, 0, 0), # Golem Axe
 705000: (NPCWeaponCategory.AXE, 14, 14, 0, 0), # Gargoyle Tail Axe
 750000: (NPCWeaponCategory.GREATAXE, 32, 8, 0, 0), # Greataxe
 751000: (NPCWeaponCategory.GREATAXE, 46, 0, 0, 0), # Demon's Greataxe
 752000: (NPCWeaponCategory.GREATAXE, 50, 8, 0, 0), # Dragon King Greataxe
 753000: (NPCWeaponCategory.GREATAXE, 36, 18, 0, 0), # Black Knight Greataxe
 800000: (NPCWeaponCategory.HAMMER, 10, 10, 0, 0), # Club
 801000: (NPCWeaponCategory.HAMMER, 12, 0, 0, 0), # Mace
 802000: (NPCWeaponCategory.HAMMER, 11, 0, 0, 0), # Morning Star
 803000: (NPCWeaponCategory.HAMMER, 11, 10, 0, 0), # Warpick
 804000: (NPCWeaponCategory.HAMMER, 14, 0, 0, 0), # Pickaxe
 809000: (NPCWeaponCategory.HAMMER, 12, 0, 0, 0), # Reinforced Club
 810000: (NPCWeaponCategory.HAMMER, 14, 0, 0, 0), # Blacksmith Hammer
 811000: (NPCWeaponCategory.HAMMER, 16, 0, 0, 0), # Blacksmith Giant Hammer
 812000: (NPCWeaponCategory.HAMMER, 14, 0, 0, 0), # Hammer of Vamos
 850000: (NPCWeaponCategory.GREAT_HAMMER, 28, 0, 0, 0), # Great Club
 851000: (NPCWeaponCategory.GREAT_HAMMER, 50, 0, 0, 30), # Grant
 852000: (NPCWeaponCategory.GREAT_HAMMER, 46, 0, 0, 0), # Demon's Great Hammer
 854000: (NPCWeaponCategory.GREAT_HAMMER, 40, 0, 0, 0), # Dragon Tooth
 855000: (NPCWeaponCategory.GREAT_HAMMER, 26, 0, 0, 0), # Large Club
 856000: (NPCWeaponCategory.GREAT_HAMMER, 58, 0, 0, 0), # Smough's Hammer
 901000: (NPCWeaponCategory.FIST, 5, 8, 0, 0), # Caestus
 902000: (NPCWeaponCategory.FIST, 6, 14, 0, 0), # Claw
 903000: (NPCWeaponCategory.FIST, 20, 0, 0, 0), # Dragon Bone Fist
 904000: (NPCWeaponCategory.FIST, 10, 10, 0, 0), # Dark Hand
 1000000: (NPCWeaponCategory.SPEAR, 11, 10, 0, 0), # Spear
 1001000: (NPCWeaponCategory.SPEAR, 13, 15, 0, 0), # Winged Spear
 1002000: (NPCWeaponCategory.SPEAR, 13, 12, 0, 0), # Partizan
 1003000: (NPCWeaponCategory.SPEAR, 12, 10, 0, 0), # Demon's Spear
 1004000: (NPCWeaponCategory.SPEAR, 16, 16, 24, 0), # Channeler's Trident
 1006000: (NPCWeaponCategory.SPEAR, 16, 22, 0, 0), # Silver Knight Spear
 1050000: (NPCWeaponCategory.SPEAR, 24, 10, 0, 0), # Pike
 1051000: (NPCWeaponCategory.SPEAR, 24, 24, 0, 0), # Dragonslayer Spear
 1052000: (NPCWeaponCategory.SPEAR, 12, 0, 14, 0), # Moonlight Butterfly Horn
 1053000: (NPCWeaponCategory.SPEAR, 12, 0, 14, 0), # Moonlight Butterfly Horn
 1054000: (NPCWeaponCategory.SPEAR, 24, 24, 0, 0), # Dragonslayer Spear
 1100000: (NPCWeaponCategory.HALBERD, 16, 12, 0, 0), # Halberd
 1101000: (NPCWeaponCategory.HALBERD, 36, 12, 0, 0), # Giant's Halberd
 1102000: (NPCWeaponCategory.HALBERD, 16, 14, 0, 0), # Titanite Catch Pole
 1103000: (NPCWeaponCategory.HALBERD, 16, 12, 0, 0), # Gargoyle's Halberd
 1105000: (NPCWeaponCategory.HALBERD, 32, 18, 0, 0), # Black Knight Halberd
 1106000: (NPCWeaponCategory.HALBERD, 15, 12, 0, 0), # Lucerne
 1107000: (NPCWeaponCategory.HALBERD, 14, 12, 0, 0), # Scythe
 1150000: (NPCWeaponCategory.HALBERD, 14, 14, 0, 0), # Great Scythe
 1151000: (NPCWeaponCategory.HALBERD, 16, 14, 0, 0), # Lifehunt Scythe
 1200000: (NPCWeaponCategory.BOW, 7, 12, 0, 0), # Short Bow
 1201000: (NPCWeaponCategory.BOW, 9, 14, 0, 0), # Longbow
 1202000: (NPCWeaponCategory.BOW, 9, 18, 0, 0), # Black Bow of Pharis
 1204000: (NPCWeaponCategory.BOW, 11, 12, 0, 0), # Composite Bow
 1205000: (NPCWeaponCategory.BOW, 7, 16, 0, 16), # Darkmoon Bow
 1250000: (NPCWeaponCategory.CROSSBOW, 10, 8, 0, 0), # Light Crossbow
 1251000: (NPCWeaponCategory.CROSSBOW, 14, 8, 0, 0), # Heavy Crossbow
 1252000: (NPCWeaponCategory.CROSSBOW, 16, 14, 0, 0), # Avelyn
 1253000: (NPCWeaponCategory.CROSSBOW, 20, 16, 0, 0), # Sniper Crossbow
 1300000: (NPCWeaponCategory.CATALYST, 6, 0, 10, 0), # Sorcerer's Catalyst
 1301000: (NPCWeaponCategory.CATALYST, 6, 0, 10, 0), # Beatrice's Catalyst
 1302000: (NPCWeaponCategory.CATALYST, 10, 10, 12, 0), # Tin Banishment Catalyst
 1303000: (NPCWeaponCategory.CATALYST, 6, 0, 24, 0), # Logan's Catalyst
 1304000: (NPCWeaponCategory.CATALYST, 4, 0, 0, 16), # Tin Darkmoon Catalyst
 1305000: (NPCWeaponCategory.CATALYST, 6, 0, 10, 0), # Oolacile Ivory Catalyst
 1306000: (NPCWeaponCategory.CATALYST, 4, 0, 32, 0), # Tin Crystallization Ctlyst.
 1307000: (NPCWeaponCategory.CATALYST, 12, 10, 10, 0), # Demon's Catalyst
 1308000: (NPCWeaponCategory.CATALYST, 6, 0, 14, 0), # Izalith Catalyst
 1360000: (NPCWeaponCategory.TALISMAN, 4, 0, 0, 10), # Talisman
 1361000: (NPCWeaponCategory.TALISMAN, 4, 0, 0, 14), # Canvas Talisman
 1362000: (NPCWeaponCategory.TALISMAN, 4, 0, 0, 10), # Thorolund Talisman
 1363000: (NPCWeaponCategory.TALISMAN, 4, 0, 0, 16), # Ivory Talisman
 1365000: (NPCWeaponCategory.TALISMAN, 4, 0, 0, 14), # Sunlight Talisman
 1366000: (NPCWeaponCategory.TALISMAN, 4, 0, 0, 24), # Darkmoon Talisman
 1367000: (NPCWeaponCategory.TALISMAN, 4, 0, 16, 0), # Velka's Talisman
 1400000: (NPCWeaponCategory.SHIELD, 7, 0, 0, 0), # Large Leather Shield
 1401000: (NPCWeaponCategory.SHIELD, 8, 11, 0, 0), # Target Shield
 1402000: (NPCWeaponCategory.SHIELD, 7, 13, 0, 0), # Buckler
 1403000: (NPCWeaponCategory.SHIELD, 5, 0, 0, 0), # Small Leather Shield
 1404000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 16), # Effigy Shield
 1405000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Crystal Ring Shield
 1406000: (NPCWeaponCategory.SHIELD, 6, 0, 0, 0), # Cracked Round Shield
 1408000: (NPCWeaponCategory.SHIELD, 7, 0, 0, 0), # Leather Shield
 1409000: (NPCWeaponCategory.SHIELD, 7, 0, 0, 0), # Plank Shield
 1410000: (NPCWeaponCategory.SHIELD, 6, 0, 0, 0), # Caduceus Round Shield
 1411000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Crystal Ring Shield
 1450000: (NPCWeaponCategory.SHIELD, 8, 0, 0, 0), # Heater Shield
 1451000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Knight Shield
 1452000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Tower Kite Shield
 1453000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Grass Crest Shield
 1454000: (NPCWeaponCategory.SHIELD, 11, 0, 0, 0), # Hollow Soldier Shield
 1455000: (NPCWeaponCategory.SHIELD, 12, 0, 0, 0), # Balder Shield
 1456000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Crest Shield
 1457000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Dragon Crest Shield
 1460000: (NPCWeaponCategory.SHIELD, 6, 0, 0, 0), # Warrior's Round Shield
 1461000: (NPCWeaponCategory.SHIELD, 14, 0, 0, 0), # Iron Round Shield
 1462000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Spider Shield
 1470000: (NPCWeaponCategory.SHIELD, 10, 12, 0, 0), # Spiked Shield
 1471000: (NPCWeaponCategory.SHIELD, 14, 0, 0, 0), # Crystal Shield
 1472000: (NPCWeaponCategory.SHIELD, 12, 0, 0, 0), # Sunlight Shield
 1473000: (NPCWeaponCategory.SHIELD, 14, 0, 0, 0), # Silver Knight Shield
 1474000: (NPCWeaponCategory.SHIELD, 16, 0, 0, 0), # Black Knight Shield
 1475000: (NPCWeaponCategory.SHIELD, 11, 14, 0, 0), # Pierce Shield
 1476000: (NPCWeaponCategory.SHIELD, 6, 0, 0, 0), # Red and White Round Shield
 1477000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Caduceus Kite Shield
 1478000: (NPCWeaponCategory.SHIELD, 12, 0, 0, 0), # Gargoyle's Shield
 1500000: (NPCWeaponCategory.SHIELD, 16, 0, 0, 0), # Eagle Shield
 1501000: (NPCWeaponCategory.SHIELD, 30, 0, 0, 0), # Tower Shield
 1502000: (NPCWeaponCategory.SHIELD, 36, 0, 0, 0), # Giant Shield
 1503000: (NPCWeaponCategory.SHIELD, 38, 0, 0, 0), # Stone Greatshield
 1505000: (NPCWeaponCategory.SHIELD, 50, 0, 0, 0), # Havel's Greatshield
 1506000: (NPCWeaponCategory.SHIELD, 30, 0, 0, 0), # Bonewheel Shield
 1507000: (NPCWeaponCategory.SHIELD, 34, 0, 0, 0), # Greatshield of Artorias
 1600000: (NPCWeaponCategory.WHIP, 7, 14, 0, 0), # Whip
 1601000: (NPCWeaponCategory.WHIP, 10, 10, 0, 0), # Notched Whip
 9000000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 16), # Effigy Shield
 9001000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 18), # Sanctus
 9002000: (NPCWeaponCategory.SHIELD, 10, 0, 0, 0), # Bloodshield
 9003000: (NPCWeaponCategory.SHIELD, 34, 0, 0, 0), # Black Iron Greatshield
 9010000: (NPCWeaponCategory.CURVED_SWORD, 9, 25, 0, 0), # Gold Tracer
 9011000: (NPCWeaponCategory.DAGGER, 5, 25, 0, 0), # Dark Silver Tracer
 9012000: (NPCWeaponCategory.GREATSWORD, 22, 18, 18, 18), # Abyss Greatsword
 9014000: (NPCWeaponCategory.SHIELD, 31, 0, 0, 0), # Cleansing Greatshield
 9015000: (NPCWeaponCategory.GREATAXE, 48, 10, 0, 0), # Stone Greataxe
 9016000: (NPCWeaponCategory.SPEAR, 15, 12, 0, 0), # Four-pronged Plow
 9017000: (NPCWeaponCategory.CATALYST, 10, 10, 0, 0), # Manus Catalyst
 9018000: (NPCWeaponCategory.CATALYST, 6, 0, 10, 0), # Oolacile Catalyst
 9019000: (NPCWeaponCategory.WHIP, 15, 10, 0, 0), # Guardian Tail
 9020000: (NPCWeaponCategory.GREATSWORD, 20, 16, 0, 0), # Obsidian Greatsword
}
