import cv2
import numpy as np

def showPic(img):
#    img = cv2.imread("D:/xhh.jpg")
    cv2.namedWindow("MyImage")
    cv2.imshow("MyImage", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # emptyImage = np.zeros(img.shape, np.unit8)
    # emptyImage2 = img.copy()
    # empytImage3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("haha.jpg", img)

def showSplit(img):
    b, g, r = cv2.split(img)
    cv2.imshow("Blue", r)
    cv2.imshow("Red", g)
    cv2.imshow("Green", b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        img[j,i] = 255
    return img

if __name__ == '__main__':
    img = cv2.imread("D:/xhh.jpg")
    salt(img, 100)
#    showPic(img)
    showSplit(img)


