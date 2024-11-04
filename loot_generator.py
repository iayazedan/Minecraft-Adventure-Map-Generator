import random

loot_table = {
    "common": ["apple", "bread"],
    "rare": ["diamond", "gold_ingot"],
    "legendary": ["nether_star", "enchanted_golden_apple"]
}

def generate_loot():
    chance = random.random()
    if chance < 0.7:
        return random.choice(loot_table["common"])
    elif chance < 0.9:
        return random.choice(loot_table["rare"])
    else:
        return random.choice(loot_table["legendary"])
