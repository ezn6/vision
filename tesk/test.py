import numpy as np
from cv2 import cv2 as cv
img_path = "C:/Users/kcour/cute.jpg"
img = cv.imread(img_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
x_edges = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=5)
x_edges = cv.convertScaleAbs(x_edges)  # x_edges결과에 절댓값적용, 8비트로 변환
y_edges = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=5)
y_edges = cv.convertScaleAbs(y_edges)  # y_edges결과에 절댓값적용, 8비트로 변환
img_grad = cv.addWeighted(x_edges, 1, y_edges, 1, 0)
cv.imshow("XEdge", x_edges)  # 수직방향 에지 검출
cv.imshow("Yedge", y_edges)  # 수평방향 에지 검출
cv.imshow("Sobel", img_grad)  # 결합
cv.waitKey(0)
cv.destroyAllWindows()
