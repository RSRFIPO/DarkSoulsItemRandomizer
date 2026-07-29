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
    GiftCandidate(
        ITEM_TYPE.ITEM,
        2100,
        1,
        "Master Key",
        "Opens any basic lock.\nInitial equipment for thieves.",
    ),
    GiftCandidate(
        ITEM_TYPE.ITEM,
        240,
        3,
        "Divine Blessing x3",
        "Holy water from Goddess Gwynevere.\nFully restores HP and status.",
    ),
    GiftCandidate(
        ITEM_TYPE.ITEM,
        297,
        10,
        "Black Firebomb x10",
        "Explodes, inflicting fire damage.\nMore deadly than a firebomb.",
    ),
    GiftCandidate(
        ITEM_TYPE.ITEM,
        501,
        1,
        "Twin Humanities",
        "Rare tiny black sprite found on corpses.\nUse to gain 2 humanity.",
    ),
    GiftCandidate(
        ITEM_TYPE.ITEM,
        371,
        1,
        "Binoculars",
        "Used to peer at faraway sights.",
    ),
    GiftCandidate(
        ITEM_TYPE.ITEM,
        376,
        1,
        "Pendant",
        "Trinket. No effect, but fond memories\ncomfort travelers.",
    ),
]

# Ring gift slots can pull only from this pool.
RING_GIFT_POOL = [
    GiftCandidate(
        ITEM_TYPE.RING,
        111,
        1,
        "Tiny Being's Ring",
        "Special tribal ring.\nSlightly boosts HP.",
    ),
    GiftCandidate(
        ITEM_TYPE.RING,
        137,
        1,
        "Old Witch's Ring",
        "Gift from a witch.\nAncient ring with no obvious effect.",
    ),
    GiftCandidate(
        ITEM_TYPE.RING,
        104,
        1,
        "Cloranthy Ring",
        "Boosts stamina recovery speed.",
    ),
    GiftCandidate(
        ITEM_TYPE.RING,
        146,
        1,
        "Wolf Ring",
        "One of the special rings granted to\nfour knights of Gwyn. Boosts poise.",
    ),
]
