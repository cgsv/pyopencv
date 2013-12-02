import cv2
import numpy as np
import sys, random, string, os

def pimg(imgfile, pchar, rowint = 3, colint = 2):
    def mapnum(i):
        if i > 128: return ' '
        #return pchar
        return random.choice(string.printable)
    img = cv2.imread(imgfile,0)
    #print img.shape
    for i in range(0,img.shape[0],rowint):
        print ''.join(map(mapnum, img[i,::colint]))

if __name__ == '__main__':
    imgf = "D:/tian.bmp"
    imgf = "D:/xhh.jpg"
    if len(sys.argv) > 1:
        imgf = sys.argv[1]
    pimg(imgf,'@')
    os.system('pause')
