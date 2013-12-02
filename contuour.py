import numpy as np
import cv2

im = cv2.imread('xhh.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('haha', image)
cv2.drawContours(im, contours, -1, (0,255,0), 1)
#cv2.imshow('img', im)
length = len(contours)
mimg = np.zeros(im.shape, dtype=np.uint8)
for i in range(length):
    cv2.drawContours(mimg, contours, i, (0,0,255),1)
    cv2.imshow('img', mimg)
    cv2.waitKey(100)
#cv2.imshow('th', thresh)
#print contours.shape
cv2.waitKey(0)
cv2.destroyAllWindows()
