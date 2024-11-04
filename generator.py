import numpy as np
from terrain_generator import generate_terrain
from dungeon_generator import generate_dungeon
from loot_generator import generate_loot
from nbtlib import File, Compound, Int, List

def create_adventure_map():
    width, height = 100, 100
    terrain = generate_terrain(width, height)
    dungeons = generate_dungeon(width, height)
    
    # Combine terrain and dungeon layers
    adventure_map = terrain + dungeons
    
    # Add loot to specific points in the dungeon
    for (x, y) in np.argwhere(dungeons > 0):
        loot = generate_loot()
        print(f"Loot at ({x}, {y}): {loot}")
    
    # Export to NBT format
    export_to_nbt(adventure_map)

def export_to_nbt(map_data):
    nbt_data = Compound({
        "AdventureMap": List([Int(val) for val in map_data.flatten()])
    })
    with open("example_output/map.nbt", "wb") as f:
        nbt_file = File({"AdventureMapData": nbt_data})
        nbt_file.write(f)

if __name__ == "__main__":
    create_adventure_map()
