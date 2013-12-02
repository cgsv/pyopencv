import numpy as np
import cv2

"""
#image read example
xhh = cv2.imread("d:/xhh.jpg")
cv2.imshow('image', xhh)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""



#video capture example
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('mycapture',gray)
    cv2.imshow('mycapture1',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



"""
#video playing ,, wrong,, may need ffmpeg
cap = cv2.VideoCapture("F:/a.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    print ret
    cv2.imshow('Downton', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""

