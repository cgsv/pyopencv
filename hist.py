import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('xhh.jpg')
mask = np.zeros(img.shape[:2], np.uint8)
mask[20:100, 20:100] = 255
mask_img = cv2.bitwise_and(img,img, mask = mask)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('haha', mask_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print img1.shape
hist = cv2.calcHist([img1], [0], None, [256], [0,256])
print hist.shape
#plt.hist(hist,256,[0,256])
#plt.hist(img1.ravel(), 256,[0,256])
#plt.plot(hist)

color = ('b', 'g', 'r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])
plt.show()
