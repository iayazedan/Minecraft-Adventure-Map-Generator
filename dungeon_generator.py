import numpy as np
import random

def generate_dungeon(width, height):
    dungeon = np.zeros((width, height))
    num_rooms = random.randint(5, 15)
    
    for _ in range(num_rooms):
        room_x = random.randint(10, width - 10)
        room_y = random.randint(10, height - 10)
        room_w = random.randint(3, 6)
        room_h = random.randint(3, 6)
        
        for x in range(room_x, room_x + room_w):
            for y in range(room_y, room_y + room_h):
                dungeon[x][y] = 1  # Room area
    return dungeon
