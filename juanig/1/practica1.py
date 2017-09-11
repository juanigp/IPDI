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

def _YIQ(rgb):
    width, height, depth = rgb.shape
    rgb = np.reshape(rgb,(width*height,depth))
    yiq = np.zeros(rgb.shape)

    yiq[:,0] = 0.299*rgb[:,0]+0.587*rgb[:,1]+0.114*rgb[:,2]
    yiq[:,1] = 0.595716*rgb[:,0]-0.274453*rgb[:,1]-0.321263*rgb[:,2]
    yiq[:,2] = 0.211456*rgb[:,0]-0.522591*rgb[:,1]+0.311135*rgb[:,2]
    if depth == 4:
        yiq[:,3] = rgb[:,3]
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
            rgb[i,j] =  min(1 ,max(rgb[i,j], 0)) #min 255
    return np.reshape(rgb,(width,height,depth))

def _RGB(yiq):
    width,height,depth = yiq.shape
    yiq = np.reshape(yiq,(width*height,depth))

    rgb = np.zeros(yiq.shape)
    rgb[:,0] = 1*yiq[:,0]+0.9563*yiq[:,1]+0.6210*yiq[:,2]
    rgb[:,1] = 1*yiq[:,0]-0.2721*yiq[:,1]-0.6474*yiq[:,2]
    rgb[:,2] = 1*yiq[:,0]-1.1070*yiq[:,1]+1.7046*yiq[:,2]
    if depth == 4:
        rgb[:,3] = yiq[:,3]
        
        
    # boundary check:
    # ::::::::::::::::::::::::::::
    
    for i in range (height*width):
        for j in range (3):
            rgb[i,j] =  min(1 ,max(rgb[i,j], 0)) #min 255
        
     
           
    #map(lambda x: 1 if x>1 else x, rgb)     
    #[1 if  i == 1 else i for i in rgb]
    #rgb[rgb > 1] = 1
    #::::::::::::::::::::::::::::::
    return np.reshape(rgb,(width,height,depth))


def brighten(yiq,a):
    width,height,depth = yiq.shape
    for i in range(width):
        for j in range(height):
            yiq[i,j,0] = a*yiq[i,j,0]
    return yiq

def _brighten(yiq,a):
    yiq[:,:,0] = a*yiq[:,:,0]
    return yiq


def floatToInt(x):
    width, height, depth = x.shape
    a = np.zeros(x.shape)
    for i in range(width):
        for j in range(height):
            for k in range (4):
                a[i,j,k] = int ( x[i,j,k]*255 )
    return a


"""
#def doTheThing(x):
# load data
rgbIn = misc.imread('lena512.png')
# show data

#this works
figure = plt.figure(0)
subplot1 = figure.add_subplot(211)
subplot1.imshow(rgbIn)

# transoform to yiq
yiqIn = YIQ(rgbIn/255.0)

# processing (brighten image)
yiqOut = brighten(yiqIn,0.5) 

#show processed data
rgbOut = RGB(yiqOut)*255

rgbOut2 = np.uint8(np.round(rgbOut))
subplot2 = figure.add_subplot(212)
subplot2.imshow(rgbOut2)


plt.show()


"""



#def doMyThing(x):  #plot in spyder
    # load data
rgbIn = misc.imread('lena512.png')
# show data
plt.figure(0)
plt.imshow(rgbIn)

# transoform to yiq
yiqIn = _YIQ(rgbIn/255.0)

# processing (brighten image)
yiqOut = _brighten(yiqIn,0.5) #*255

#show processed data
rgbOut = _RGB(yiqOut)

plt.figure(1)
plt.imshow(rgbOut)
#plt.imshow(rgbOut2)




#doTheThing(2)
#doMyThing(0.5)