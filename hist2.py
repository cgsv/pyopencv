from pylab import *
import cv2

img = cv2.imread('xhh.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#equ = cv2.equalizeHist(img)
#res = np.hstack((img, equ))
#cv2.imshow('haha', res)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

imshow(hist, interpolation = 'nearest')
show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()
