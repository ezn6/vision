from cv2 import cv2 as cv
import matplotlib.pyplot as plt

img_path = "C:/Users/kcour/0907.png"
img = cv.imread(img_path)
kernel = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
dilation = cv.dilate(img, kernel, iterations=1)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(dilation)
plt.show()
