from pylab import *
import cv2

img = cv2.imread('d:/xhh.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hh = np.histogram(img1,256,[0,256])
his = hh[0]
his1 = his/float(sum(his))
img1f = img1.ravel()

for m in range(len(img1f)):
	img1f[m]= int(255* sum(his1[:img1f[m]]))


aaa = img1f.reshape(img.shape[:2])
plt.imshow(aaa, cmap = cm.gray);plt.show()
