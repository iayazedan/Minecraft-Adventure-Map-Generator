import numpy as np
from noise import pnoise2

def generate_terrain(width, height, scale=0.1):
    terrain = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            noise_value = pnoise2(x * scale, y * scale)
            if noise_value < -0.05:
                terrain[x][y] = 1  # Water
            elif noise_value < 0.05:
                terrain[x][y] = 2  # Plains
            else:
                terrain[x][y] = 3  # Mountains
    return terrain
