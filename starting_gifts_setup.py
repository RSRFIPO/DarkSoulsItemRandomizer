"""
Starting gift randomization logic.

Adapted from C# to Python, originally from:
Archipelago Randomizer for Dark Souls Remastered
https://github.com/tathxo/DSAP

Original work Copyright (c) 2024 ArsonAssassin
Licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from items_setup import ITEM_TYPE


class GiftSlot:
    def __init__(self, chr_init_id, vanilla_name, is_ring_slot):
        self.chr_init_id = chr_init_id
        self.vanilla_name = vanilla_name
        self.is_ring_slot = is_ring_slot


class GiftCandidate:
    def __init__(self, item_type, item_id, quantity, display_name, description):
        self.item_type = item_type
        self.item_id = item_id
        self.quantity = quantity
        self.display_name = display_name
        self.description = description


class GiftAssignment:
    def __init__(self, slot, candidate):
        self.slot = slot
        self.candidate = candidate


def item_gift(item_id, quantity, display_name, description):
    return GiftCandidate(ITEM_TYPE.ITEM, item_id, quantity, display_name, description)


def ring_gift(item_id, display_name, description):
    return GiftCandidate(ITEM_TYPE.RING, item_id, 1, display_name, description)


# Character creation gift rows in CharaInitParam.
GIFT_SLOTS = [
    GiftSlot(2401, "Goddess's Blessing", False),
    GiftSlot(2402, "Black Firebomb", False),
    GiftSlot(2403, "Twin Humanities", False),
    GiftSlot(2404, "Binoculars", False),
    GiftSlot(2405, "Pendant", False),
    GiftSlot(2406, "Master Key", False),
    GiftSlot(2407, "Tiny Being's Ring", True),
    GiftSlot(2408, "Old Witch's Ring", True),
]

# Message IDs in menu.msgbnd/system text.
GIFT_NAME_MSG_ID_OFFSET = 132050 - 2400
GIFT_DESC_MSG_ID_OFFSET = 132350 - 2400

# Non-ring gift slots can pull from this pool.
NON_RING_GIFT_POOL = [
    item_gift(
        2100, 1, "Master Key",
        "Opens any basic\nlock. Initial equip\nfor a thief.",
    ),
    item_gift(
        240, 1, "Goddess's Blessing",
        "Divine holy water.\nFully restores HP\nand status.",
    ),
    item_gift(
        297, 10, "Black Firebomb",
        "Explodes upon impact.\nwhen thrown. More\ndeadly than std bomb.",
    ),
    item_gift(
        501, 1, "Twin Humanities",
        "Tiny sprite called\nhumanity. Somtimes\nfound on carcasses.",
    ),
    item_gift(
        371, 1, "Binoculars",
        "Use to peer at\nfaraway sights.",
    ),
    item_gift(
        376, 1, "Pendant",
        "Trinket. No effect,\nbut fond memories\ncomfort travelers.",
    ),
    item_gift(
        230, 3, "Elizabeth Mushroom",
        "Medicinal mushroom of\nElizabeth. Restores a\nlarge amount of HP.",
    ),
    item_gift(
        1070, 1, "Titanite Slab",
        "Legendary titanite slab.\nReinforces weapons\nto +15.",
    ),
    item_gift(
        409, 1, "Great Hero Soul",
        "Soul of a legendary hero.\nAcquire many souls.",
    ),
    item_gift(
        290, 40, "Throwing Knives",
        "Small throwing blades.\nUseful for pulling foes.",
    ),
    item_gift(
        291, 30, "Poison Knives",
        "Poison throwing blade.\nInflicts poison.",
    ),
    item_gift(
        292, 20, "Firebomb",
        "Bisque urn filled with\nblack powder.\nInflicts fire damage.",
    ),
    item_gift(
        293, 30, "Dung Pie",
        "Atrocious fecal waste\nmaterial. Throw at enemy\nto build up toxins.",
    ),
    item_gift(
        310, 5, "Fire Pine Resin",
        "Applies fire to right\nhand weapon.",
    ),
    item_gift(
        311, 5, "Gold Pine Resin",
        "Applies lightning to right\nhand weapon.",
    ),
    item_gift(
        313, 5, "Rotten Pine Resin",
        "Adds poison effect to\nright hand weapon.",
    ),
    item_gift(
        330, 20, "Homeward Bone",
        "Return to last bonfire\nused for resting.",
    ),
    item_gift(
        260, 15, "Green Blossom",
        "Green flower-shaped\nweed. Boosts stamina\nrecovery.",
    ),
    item_gift(
        272, 10, "Moss Clumps",
        "Blooming purple moss.\nCures poison and Toxic.",
    ),
    item_gift(
        1010, 10, "L. Titanite Shard",
        "Large titanite shard.\nReinforces weapons\nto +10.",
    ),
    item_gift(
        1000, 10, "Titanite Shard",
        "Small titanite shard.\nReinforces weapons\nto +5.",
    ),
]

# Ring gift slots can pull only from this pool.
RING_GIFT_POOL = [
    ring_gift(
        111, "Tiny Being's Ring",
        "Special tribal ring.\nSlightly boosts HP.",
    ),
    ring_gift(
        137, "Old Witch's Ring",
        "Gift from a witch.\nAncient ring with\nno obvious effect.",
    ),
    ring_gift(
        104, "Cloranthy Ring",
        "Engraved green flower\nring. Hastens the\nregeneration of stamina.",
    ),
    ring_gift(
        126, "Ring of Sacrifice",
        "Lose nothing upon\ndeath, but the\nring itself breaks.",
    ),
    ring_gift(
        100, "Havel's Ring",
        "Ring of\nDragonslayer Havel.\nRaises equipment load.",
    ),
    ring_gift(
        122, "Silver Serpent Ring",
        "Silver ring engraved\nwith a serpent.\nBoosts souls gained.",
    ),
    ring_gift(
        150, "Calamity Ring",
        "A useless ring befitting\nof no finger.\nBest left unknown.",
    ),
    ring_gift(
        119, "Hawk Ring",
        "Ring of a knight of Gwyn.\nExtends bow range.",
    ),
    ring_gift(
        125, "Rusted Iron Ring",
        "Old rusted ring.\nImproves movement\nin poor footing.",
    ),
    ring_gift(
        123, "Slumbering Ring",
        "Ring of an assassin\nsorcerer. Engraved with\na slumbering dragon.",
    ),
]


def validate_gift_pools():
    non_ring_slot_count = len([slot for slot in GIFT_SLOTS if not slot.is_ring_slot])
    ring_slot_count = len([slot for slot in GIFT_SLOTS if slot.is_ring_slot])
    if len(NON_RING_GIFT_POOL) < non_ring_slot_count:
        raise ValueError("Not enough non-ring starting gift candidates.")
    if len(RING_GIFT_POOL) < ring_slot_count:
        raise ValueError("Not enough ring starting gift candidates.")

    for candidate in NON_RING_GIFT_POOL:
        if candidate.item_type == ITEM_TYPE.RING:
            raise ValueError("Ring candidate found in non-ring starting gift pool.")
    for candidate in RING_GIFT_POOL:
        if candidate.item_type != ITEM_TYPE.RING:
            raise ValueError("Non-ring candidate found in ring starting gift pool.")


def randomize_starting_gifts(chr_init_param, random_source):
    validate_gift_pools()
    non_ring_pool = list(NON_RING_GIFT_POOL)
    ring_pool = list(RING_GIFT_POOL)
    assignments = []

    for slot in GIFT_SLOTS:
        pool = ring_pool if slot.is_ring_slot else non_ring_pool
        candidate = random_source.choice(pool)
        pool.remove(candidate)

        chr_init = chr_init_param.find_chr_by_id(slot.chr_init_id)
        if chr_init is None:
            raise ValueError("Could not find starting gift CharaInit row {}.".format(slot.chr_init_id))

        chr_init.ring_1 = 0
        chr_init.item_1 = 0
        chr_init.item_1_num = 0

        if candidate.item_type == ITEM_TYPE.RING:
            chr_init.ring_1 = candidate.item_id
        else:
            chr_init.item_1 = candidate.item_id
            chr_init.item_1_num = candidate.quantity

        assignments.append(GiftAssignment(slot, candidate))

    return assignments


def update_gift_messages(messages, assignments):
    message_by_id = {message.id: message for message in messages}
    updated_count = 0
    for assignment in assignments:
        name_id = assignment.slot.chr_init_id + GIFT_NAME_MSG_ID_OFFSET
        desc_id = assignment.slot.chr_init_id + GIFT_DESC_MSG_ID_OFFSET
        if name_id in message_by_id:
            message_by_id[name_id].text = assignment.candidate.display_name
            updated_count += 1
        if desc_id in message_by_id:
            message_by_id[desc_id].text = assignment.candidate.description
            updated_count += 1
    return updated_count


def assignments_as_string(assignments):
    ret = "Randomized Starting Gifts:\n"
    for assignment in assignments:
        ret += "  {}: {}\n".format(
            assignment.slot.vanilla_name,
            assignment.candidate.display_name)
    return ret
