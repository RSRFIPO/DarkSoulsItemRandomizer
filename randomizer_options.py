
class RandOptDifficulty:
    EASY = 0
    MEDIUM = 1
    HARD = 2

    NUM = 3

    strings = ['Fair', 'Unfair', 'Very Unfair']

    @classmethod
    def as_strings(cls):
        return cls.strings
    
    @classmethod
    def as_string(cls, diff):
        if (diff >= cls.NUM):
            return None #error
        return cls.strings[diff]
    
    @classmethod
    def from_string(cls, str):
        return cls.strings.index(str)

class RandOptKeyDifficulty:
    LEAVE_ALONE = 0
    RANDOMIZE = 1
    RACE_MODE = 2
    SPEEDRUN_MODE = 3

    NUM = 4

    strings = ['Not Shuffled', 'Shuffled', 'Race Mode', 'Race Mode +']
    
    @classmethod
    def as_strings(cls):
        return cls.strings
    
    @classmethod
    def as_string(cls, diff):
        if (diff >= cls.NUM):
            return None #error
        return cls.strings[diff]
    
    @classmethod
    def from_string(cls, str):
        return cls.strings.index(str)
    
class RandOptStartItemsDifficulty:
    SHIELD_AND_1H = 0
    SHIELD_AND_2H = 1
    COMBINED_POOL_AND_2H = 2

    NUM = 3

    strings = ['Shield & 1H Weapon', 'Shield & 1/2H Weapon', 'Shield/Weapon & Weapon']
    
    @classmethod
    def as_strings(cls):
        return cls.strings
    
    @classmethod
    def as_string(cls, diff):
        if (diff >= cls.NUM):
            return None #error
        return cls.strings[diff]
    
    @classmethod
    def from_string(cls, str):
        return cls.strings.index(str)
            
    
class RandOptSoulItemsDifficulty:
    SHUFFLE = 0
    CONSUMABLE = 1
    TRANSPOSE = 2

    NUM = 3

    strings = ['Shuffled', 'Replaced', 'Transposed']
    
    @classmethod
    def as_strings(cls):
        return cls.strings
    
    @classmethod
    def as_string(cls, diff):
        if (diff >= cls.NUM):
            return None #error
        return cls.strings[diff]
    
    @classmethod
    def from_string(cls, str):
        return cls.strings.index(str)

class RandOptBossSoulTransposeChance:
    CHANCE_10 = 10
    CHANCE_25 = 25
    CHANCE_50 = 50
    CHANCE_75 = 75

    values = [CHANCE_10, CHANCE_25, CHANCE_50, CHANCE_75]
    strings = ['10%', '25%', '50%', '75%']

    @classmethod
    def as_strings(cls):
        return cls.strings

    @classmethod
    def as_string(cls, chance):
        if chance not in cls.values:
            return None
        return cls.strings[cls.values.index(chance)]

    @classmethod
    def from_string(cls, str):
        return cls.values[cls.strings.index(str)]

    @classmethod
    def verify(cls, chance):
        if chance not in cls.values:
            return cls.CHANCE_75
        return chance

class RandOptAscendWeaponsChance:
    CHANCE_5 = 5
    CHANCE_15 = 15
    CHANCE_25 = 25

    values = [CHANCE_5, CHANCE_15, CHANCE_25]
    strings = ['5%', '15%', '25%']

    @classmethod
    def as_strings(cls):
        return cls.strings

    @classmethod
    def as_string(cls, chance):
        if chance not in cls.values:
            return None
        return cls.strings[cls.values.index(chance)]

    @classmethod
    def from_string(cls, str):
        return cls.values[cls.strings.index(str)]

    @classmethod
    def verify(cls, chance):
        if chance not in cls.values:
            return cls.CHANCE_25
        return chance
            
class RandOptGameVersion:
    PTDE = "DARK SOULS: Prepare To Die Edition"
    REMASTERED = "DARK SOULS: REMASTERED"
    
    @classmethod
    def as_string(cls, version):
        if version == cls.PTDE:
            return cls.PTDE
        elif version == cls.REMASTERED:
            return cls.REMASTERED
        else:
            return ""

class RandOptLordvesselLocation:
    GWYNEVERE = 'Gwynevere'
    RANDOMIZED = 'Randomized'
    FIRELINK = 'Firelink'

    @classmethod
    def as_strings(cls):
        return [cls.GWYNEVERE, cls.RANDOMIZED, cls.FIRELINK]
    
    @classmethod
    def get_default(cls):
        return cls.RANDOMIZED
    
    @classmethod 
    def verify(cls, check_value):
        if check_value not in cls.as_strings():
            return cls.RANDOMIZED   #something bad happened - use default value
        return check_value

class RandomizerOptions:
    def __init__(self, difficulty, fashion_souls, key_placement, 
     use_lordvessel, use_lord_souls, soul_items_diff, start_items_diff,
     game_version, randomize_npc_armor, ascend_weapons, keys_not_in_dlc, set_up_hints,
     no_black_knight_weapons, reroll_seed_each_run=False, randomize_npc_weapons=False,
     boss_soul_transpose_chance=RandOptBossSoulTransposeChance.CHANCE_75,
     ascend_weapons_chance=RandOptAscendWeaponsChance.CHANCE_25):
         self.difficulty = difficulty
         self.fashion_souls = fashion_souls
         self.key_placement = key_placement
         self.use_lordvessel = use_lordvessel
         self.use_lord_souls = use_lord_souls
         self.soul_items_diff = soul_items_diff
         self.start_items_diff = start_items_diff
         self.game_version = game_version
         self.randomize_npc_armor = randomize_npc_armor
         self.ascend_weapons = ascend_weapons
         self.keys_not_in_dlc = keys_not_in_dlc
         self.set_up_hints = set_up_hints
         self.no_online_items = True
         self.better_start_spells = True
         self.no_black_knight_weapons = no_black_knight_weapons
         self.reroll_seed_each_run = reroll_seed_each_run
         self.randomize_npc_weapons = randomize_npc_weapons
         self.boss_soul_transpose_chance = RandOptBossSoulTransposeChance.verify(boss_soul_transpose_chance)
         self.ascend_weapons_chance = RandOptAscendWeaponsChance.verify(ascend_weapons_chance)
         
    def bool_option_to_string(self, b):
        if b:
            return "On"
        else:
            return "Off"
         
    def as_string(self):
        return_string = "Randomizer Settings:\n"
        return_string += "  Game Version: " + RandOptGameVersion.as_string(self.game_version) + "\n"
        return_string += "  Difficulty: " + RandOptDifficulty.as_string(self.difficulty) + "\n"
        return_string += "  Fashion Souls: " + self.bool_option_to_string(self.fashion_souls) + "\n"
        return_string += "  Key Difficulty: " + RandOptKeyDifficulty.as_string(self.key_placement) + "\n"
        return_string += "  Lordvessel: " + self.use_lordvessel + "\n"
        return_string += "  Senile Primordial Serpents: " + self.bool_option_to_string(self.use_lord_souls) + "\n"
        return_string += "  Soul Items: " + RandOptSoulItemsDifficulty.as_string(self.soul_items_diff) + "\n"
        if self.soul_items_diff == RandOptSoulItemsDifficulty.TRANSPOSE:
            return_string += "  Boss Soul Transpose Chance: " + RandOptBossSoulTransposeChance.as_string(self.boss_soul_transpose_chance) + "\n"
        return_string += "  Starting Items: " + RandOptStartItemsDifficulty.as_string(self.start_items_diff) + "\n"
        return_string += "  Laundromat Mixup: " + self.bool_option_to_string(self.randomize_npc_armor) + "\n"
        return_string += "  Eager Smiths: " + self.bool_option_to_string(self.ascend_weapons) + "\n"
        if self.ascend_weapons:
            return_string += "  Eager Smiths Chance: " + RandOptAscendWeaponsChance.as_string(self.ascend_weapons_chance) + "\n"
        return_string += "  No DLC: " + self.bool_option_to_string(self.keys_not_in_dlc) + "\n"
        return_string += "  Seek Guidance Hints: " + self.bool_option_to_string(self.set_up_hints) + "\n"
        return_string += "  No Black Knight Weapons: " + self.bool_option_to_string(self.no_black_knight_weapons) + "\n"
        return_string += "  Randomize NPC Weapons: " + self.bool_option_to_string(self.randomize_npc_weapons) + "\n"
        return return_string
        
