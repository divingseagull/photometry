import numpy as np
import matplotlib.pyplot as plt
# import astropy ...

from src import marking
from src import graph

target = input("Enter target image: ")
image = plt.imread(f"../images/{target}")

# plt.imshow(image, cmap='gray')
# plt.plot(graph.graph(image, (1590, 292), (1624, 319)))
plt.plot(graph.graph(image, (2650, 404), (2672, 422)))
plt.show()
