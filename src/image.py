import numpy as np
import matplotlib.pyplot as plt

from src.marker import Marker


class Image:
    def __init__(self, image: np.ndarray):
        self.array = image
        self.markers: dict[str, Marker] = dict()

    def graph(self, start_pos: tuple[int, int], end_pos: tuple[int, int]) -> None:
        sx, sy = start_pos
        ex, ey = end_pos
        area_arr = self.array[sy:ey, sx:ex]
        plt.plot(area_arr.max(axis=1))
        plt.show()

    def get_brightness(self, marker_name: str) -> np.float64:
        pass
