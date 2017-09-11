# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:05:30 2017

@author: Juanig
"""

#import some_functions as sf

from some_functions import RGB,YIQ,brighten,RGB_sum,YIQ_interpolated_sum,if_darker, if_lighter

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import os

p = os.path.dirname(__file__)+'/'
print(p)

img1 = misc.imread('lena512.png')
img2 = misc.imread('baboon.png')
#img2 = misc.imread('black.png')

#""
#out = RGB_sum(img1,img2,'average')
#out = RGB_sum(img1,img2,'clamped')
#out = YIQ_interpolated_sum(img1,img2)
#out = YIQ_interpolated_sum(img1,img2, 'clamped')
#out = YIQ_interpolated_sum(img1,img2,'average')
#out = if_darker(img1,img2)
#out = if_lighter(img1,img2)
#a = out.data

plt.figure(0)
plt.imshow(img1)

plt.figure(1)
plt.imshow(img2)

plt.figure(2)
#plt.imshow(out)
#"""
"""
height,width,channels = img1.shape
test = np.zeros(img1.shape)


test[:,:,3] = 255
test[:,:,0] = img1[:,:,0]
test[:,:,1] = img1[:,:,1]
test[:,:,2] = img1[:,:,2]

a = np.zeros([height,width])

# channel swap
a = test[:,:,0].copy()
test[:,:,0] = test[:,:,2]
test[:,:,2] = a

test = np.uint8(np.round(test)) 

plt.imshow(test)
"""

#a = np.zeros[]


