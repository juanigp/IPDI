# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:09:17 2017

@author: Felix Thomsen

1.) fill out the parts with ?

2.) rewrite the functions that they do not contain explicit for-loops using the [:] operator

3.) implement the conversion between RGB and HSV 
"""

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

import math



# transform entire image from rgb to yiq
def YIQ(rgb):
    width,height,depth = rgb.shape
    rgb = np.reshape(rgb,(width*height,depth))
    yiq = np.zeros(rgb.shape)
    for i in range(width*height):
        yiq[i,0] = 0.299*rgb[i,0]+0.587*rgb[i,1]+0.114*rgb[i,2]
        yiq[i,1] = 0.595716*rgb[i,0]-0.274453*rgb[i,1]-0.321263*rgb[i,2]
        yiq[i,2] = 0.211456*rgb[i,0]-0.522591*rgb[i,1]+0.311135*rgb[i,2]
        if depth == 4:
            yiq[i,3] = rgb[i,3]
    return np.reshape(yiq,(width,height,depth))

def RGB(yiq):
    width,height,depth = yiq.shape
    yiq = np.reshape(yiq,(width*height,depth))
    rgb = np.zeros(yiq.shape)
    for i in range(width*height):
        rgb[i,0] = 1*yiq[i,0]+0.9563*yiq[i,1]+0.6210*yiq[i,2]
        rgb[i,1] = 1*yiq[i,0]-0.2721*yiq[i,1]-0.6474*yiq[i,2]
        rgb[i,2] = 1*yiq[i,0]-1.1070*yiq[i,1]+1.7046*yiq[i,2]
        if depth == 4:
            rgb[i,3] = yiq[i,3]
        # boundary check:
        for j in range(3):
            rgb[i,j] =  min(1,max(rgb[i,j],0)) #min 255
    return np.reshape(rgb,(width,height,depth))


def brighten(yiq,a):
    width,height,depth = yiq.shape
    for i in range(width):
        for j in range(height):
            yiq[i,j,0] = a*yiq[i,j,0]
    return yiq

# load data
rgbIn = misc.imread('lena512.png')
# show data
plt.figure(0)

plt.imshow(rgbIn)

# transoform to yiq
yiqIn = YIQ(rgbIn/255.0)
# processing (brighten image)
yiqOut = brighten(yiqIn,1) #*255

#show processed data
rgbOut = RGB(yiqOut)

plt.figure(1)
plt.imshow(rgbOut)

