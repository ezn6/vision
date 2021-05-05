import numpy as np
from cv2 import cv2 as cv
img_path = "C:/Users/kcour/cute.jpg"
img = cv.imread(img_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img, (5, 5), 5)  # sigma=1 일때
# img_blur = cv.GaussianBlur(img, (5, 5), 3)  # sigma=3 일때
# img_blur = cv.GaussianBlur(img, (5, 5), 5)  # sigma=5 일때
# img_blur = cv.GaussianBlur(img, (5, 5), 7)  # sigma=7 일때
edges = cv.Canny(img_blur, 50, 100, 3)
cv.imshow("Edge", edges)
cv.waitKey(0)
cv.destroyAllWindows()
