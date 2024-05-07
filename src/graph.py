import matplotlib.pyplot as plt
import numpy as np


def graph(image: np.ndarray,
          start_pos: tuple[int, int], end_pos: tuple[int, int]) -> np.ndarray:
    sx, sy = start_pos
    ex, ey = end_pos
    max_brightness_array = image[sy:ey, sx:ex]
    return max_brightness_array
