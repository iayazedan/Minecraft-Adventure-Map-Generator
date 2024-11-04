# Minecraft Adventure Map Generator

This project procedurally generates an adventure map with dungeons, biomes, and loot tables for Minecraft. It outputs files in the NBT format to be imported into Minecraft.

## Features
- Procedural terrain with biomes
- Randomized dungeon generation
- Loot tables with item rarity
- Exported to NBT format compatible with Minecraft

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run the generator: `python generator.py`
3. Generated files will be in the `example_output` directory.

## Requirements
- `nbtlib`: For handling NBT files.
- `numpy`: For procedural generation of terrain.
- `random`: For random loot and dungeon generation.
