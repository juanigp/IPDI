# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:02:49 2017

@author: Juanig
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cmath


"""
class complexNum:
    realPart, imaginaryPart = 0, 0
    def __init__(self,re,im):
        self.realPart = re
        self.imaginaryPart = im

    def magnitude(self):
        return np.sqrt(self.realPart**2 + self.imaginaryPart**2)

    def square(self):
        a = complexNum(0,0)

"""




width, height = 500,500

c = complex(-0.1,0.65)
abs_max = 10
it_max = 1000

xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5

xw = xmax-xmin
yh = ymax-ymin

julia = np.zeros((width, height))

for i in range(width):
    for j in range(height):
        it = 0
        z = complex(i/width * xw + xmin, j/height * yh + ymin )
        while abs(z) <= abs_max and it <= it_max :
            z = z**2+c
            it+=1
        julia[i,j] = it/it_max



figure = plt.figure(0)
subplot1 = figure.add_subplot(211)
subplot1.imshow(julia, cmap = cm.hot)
plt.show()




"""
#this how u do it in spyder

plt.figure(0)
plt.imshow(julia, cmap = cm.hot)

"""
