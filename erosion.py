import cv2
import numpy as np

davep = cv2.imread('dave.png',0)
lap = cv2.Canny(davep, 100, 200)

#lap = cv2.Laplacian(davep, cv2.CV_64F)

img = cv2.imread('xhh.jpg')
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
cv2.imshow('mm', erosion)
cv2.imshow('mm1', dilation)
cv2.imshow('mm2', lap)
cv2.waitKey(0)
cv2.destroyAllWindows()
