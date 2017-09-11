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

# transform entire image from rgb to yiq
def RGB2YIQ(rgb):
    width,height,depth = rgb.shape
    rgb = np.reshape(rgb/255,(width*height,depth))
    yiq = np.zeros(rgb.shape)
#    for i in range(width*height):
    yiq[:,0] = 0.229*rgb[:,0] + 0.587*rgb[:,1] + 0.114*rgb[:,2]
    yiq[:,1] = 0.595716*rgb[:,0] - 0.274453*rgb[:,1] - 0.321263*rgb[:,2]
    yiq[:,2] = 0.211456*rgb[:,0] - 0.522591*rgb[:,1] + 0.311135*rgb[:,2]
    if depth == 4:
        yiq[:,3] = rgb[:,3]
    return np.reshape(yiq,(width,height,depth))

def YIQ2RGB(yiq):
    width,height,depth = yiq.shape
    yiq = np.reshape(yiq,(width*height,depth))
    rgb = np.zeros(yiq.shape)
#    for i in range(width*height):
    rgb[:,0] = yiq[:,0] + 0.9663*yiq[:,1] + 0.6210*yiq[:,2]
    rgb[:,1] = yiq[:,0] - 0.2721*yiq[:,1] - 0.6474*yiq[:,2]
    rgb[:,2] = yiq[:,0] - 1.1070*yiq[:,1] + 1.7046*yiq[:,2]
    if depth == 4:
        rgb[:,3] = yiq[:,3]
        # boundary check:
    for i in range(width*height):
        for j in range(3):
            rgb[i,j] = min(1,max(rgb[i,j],0))
            
    rgb = rgb*255
    rgb = rgb.astype(np.uint8)
    
    return np.reshape(rgb,(width,height,depth))

def RGB2HSV(rgb):
    width,height,depth = rgb.shape
    rgb = np.reshape(rgb,(width*height,depth))
    hsv = np.zeros(rgb.shape)
    for i in range(width*height):
        r = rgb[i,0]/255
        g = rgb[i,1]/255
        b = rgb[i,2]/255
        cmax = max(r,g,b)
        cmin = min(r,g,b)
        d = cmax - cmin
        
        if (d == 0):
            hsv[i,0] = 0
        elif (cmax == r):
            hsv[i,0] = 60*(((g - b)/d) % 6)
        elif (cmax == g):
            hsv[i,0] = 60*(((b - r)/d) + 2)
        elif (cmax == b):
            hsv[i,0] = 60*(((r - g)/d) + 4) 
        
        if (cmax == 0):
            hsv[i,1] = 0
        else:
            hsv[i,1] = d/cmax
        
        hsv[i,2] = cmax
        
    if depth == 4:
        hsv[:,3] = rgb[:,3]
        
    return np.reshape(hsv,(width,height,depth))

def HSV2RGB(hsv):
    width,height,depth = hsv.shape
    hsv = np.reshape(hsv,(width*height,depth))
    rgb = np.zeros(hsv.shape)
    for i in range(width*height):
        c = hsv[i,2]*hsv[i,1]
        x = c*(1 - abs(((hsv[i,0]/60) % 2) - 1))
        m = hsv[i,2] - c
        
        if ((hsv[i,0] >= 0)and(hsv[i,0] < 60)):
            r = c
            g = x
            b = 0
        elif ((hsv[i,0] >= 60)and(hsv[i,0] < 120)):
            r = x
            g = c
            b = 0
        elif ((hsv[i,0] >= 120)and(hsv[i,0] < 180)):
            r = 0
            g = c
            b = x
        elif ((hsv[i,0] >= 180)and(hsv[i,0] < 240)):
            r = 0
            g = x
            b = c
        elif ((hsv[i,0] >= 240)and(hsv[i,0] < 300)):
            r = x
            g = 0
            b = c
        elif ((hsv[i,0] >= 300)and(hsv[i,0] < 360)):
            r = c
            g = 0
            b = x
        
        rgb[i,0] = (r + m)*255
        rgb[i,1] = (g + m)*255
        rgb[i,2] = (b + m)*255
    
    if depth == 4:
        rgb[:,3] = hsv[:,3]
        
    rgb = rgb.astype(np.uint8)
   
    return np.reshape(rgb,(width,height,depth))

def brightenYIQ(yiq,a):

#    for i in range(width):
#        for j in range(height):
#            yiq[i,j,0] = np.power(yiq[i,j,0],np.power(2.,-a))
    yiq[:,:,0] = np.power(yiq[:,:,0],np.power(2.,-a))
         
    return yiq

def brightenHSV(hsv,a):
    hsv[:,:,2] = np.power(hsv[:,:,2],np.power(2.,-a))
    
    return hsv


