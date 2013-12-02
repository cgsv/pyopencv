import cv2
import numpy as np

feng = cv2.imread("fengjing.jpg")
haibao = cv2.imread("haibao.bmp")

rows,cols,channels = haibao.shape
roi = feng[0:rows, 0:cols]
#feng[0:rows, 0:cols] = cv2.addWeighted(xhh, 0.7, feng[0:rows, 0:cols],0.3,0)
#feng[0:rows, 0:cols] = xhh

haibao2gray = cv2.cvtColor(haibao, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(haibao2gray, 230, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

bg1 = cv2.bitwise_and(roi, roi, mask = mask)
fg1 = cv2.bitwise_and(haibao, haibao, mask = mask_inv)

dst = cv2.add(bg1, fg1)
roi[mask!=255] = 0 
feng[0:rows, 0:cols] = dst
#feng[0:rows, 0:cols] = roi

cv2.imshow('haha', feng)
#c = 1.0
#for i in range(10):
    #cv2.imshow('haha', np.uint8(image * c))
    #c -= 0.1
    #cv2.waitKey(500)
cv2.waitKey(0)
cv2.destroyAllWindows()
