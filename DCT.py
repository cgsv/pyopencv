from math import pi, sin, cos
import numpy as np
import pprint

m = [ 52,  55,  61,  66,  70,  61,  64,  73,\
      63,  59,  55,  90, 109,  85,  69,  72,\
      62,  59,  68, 113, 144, 104,  66,  73,\
      63,  58,  71, 122, 154, 106,  70,  69,\
      67,  61,  68, 104, 126,  88,  68,  70,\
      79,  65,  60,  70,  77,  68,  58,  75,\
      85,  71,  64,  59,  55,  61,  65,  83,\
      87,  79,  69,  68,  65,  76,  78,  94 ]
am = np.array(m)
fm = am.reshape(8, 8)
fm = fm - 128



def F(u, v):
    def C(x):
        if x == 0: return 2**-0.5
        else: return 1
    def f(i, j):return fm[i, j]
    sum = 0
    for i in xrange(8):
        for j in xrange(8):
            sum += 0.25*C(u)*C(v)*f(i,j)*\
                   cos((2*i+1)*u*pi/16)*\
                   cos((2*j+1)*v*pi/16)
    return round(sum,0)

res = [[int(F(u, v)) for v in range(8)] for u in range(8)]
pprint.pprint(res)

