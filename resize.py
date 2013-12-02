import cv2
import numpy as np

img = cv2.imread('xhh.jpg')
rows,cols,c = img.shape
M = np.float32([[1, 0, 30],[0,1,50]])
#dst = cv2.warpAffine(img, M, (cols, rows))
M1 = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.7)
dst = cv2.warpAffine(img, M1, (cols, rows))
#res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#res2 = cv2.resize(img, (img.shape[0]*2, img.shape[1]*3))
cv2.imshow('haha', dst)
#cv2.imshow('org', img)
#cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
