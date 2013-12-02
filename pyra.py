import cv2
import numpy as np

img = cv2.imread('xhh.jpg')

low = cv2.pyrDown(img)

up = cv2.pyrUp(low)

l = cv2.subtract(img, up)
print l

print img.shape
print low.shape
print up.shape

cv2.imshow('hh', img)
cv2.imshow('h2', up)
cv2.waitKey(0)
cv2.destroyAllWindows()
