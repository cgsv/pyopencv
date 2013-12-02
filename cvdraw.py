import numpy as np
import cv2
from math import sqrt

"""
img = np.zeros((512,512,3), np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img, (50, 50), (300, 300), (0, 255, 0), 10)
cv2.circle(img, (250,250), 50, (0,0,255),7)
cv2.ellipse(img, (400,400), (100, 100), 0, -60, 240, (0,255,0), 50)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'cgsv', (10, 500), font, 4, (255,255,0))


cv2.imshow('mydrawing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x,y), 100, (255,0,0), -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image1")
cv2.setMouseCallback('image1', draw_circle)

while True:
    cv2.imshow('image1', img)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()
"""

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

def distance(x1,y1,x2,y2):
    return int(sqrt((x1-x2)**2 + (y1-y2)**2))

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                #cv2.circle(img,(x,y),5,(0,0,255),-1)
                cv2.circle(img,(ix, iy),distance(ix,iy,x,y),(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            #cv2.circle(img,(x,y),5,(0,0,255),-1)
            cv2.circle(img,(ix, iy),distance(ix,iy,x,y),(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
