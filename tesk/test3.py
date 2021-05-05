import numpy as np
from cv2 import cv2 as cv
import matplotlib.pyplot as plt


def color_rect():
    g = np.zeros((256, 256, 3), np.uint8)
    for i in range(256):
        g[i, 0, :] = (0, i, 255 - i)
        g[i, 255, :] = (255-i, i, i)
        for j in range(256):
            g[i, j, :] = (1-j/256)*g[i, 0, :] + j/256*g[i, 255, :]
    return g


g = color_rect()
col = cv.cvtColor(g, cv.COLOR_BGR2RGB)
plt.imshow(col)
plt.show()
