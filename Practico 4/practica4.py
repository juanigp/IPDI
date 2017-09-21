# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:41:13 2017

@author: Bruna Luciano, Payares Natalia & Rodriguez Nicolas
"""

from escalas import RGB2YIQ, YIQ2RGB
from scipy import misc
from fourier import EscalaGrises
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def histogram(rgb, bins=256):
    
    yiq = RGB2YIQ(rgb)
    width,height,depth = rgb.shape
    yiq = np.reshape(yiq,(width*height,depth))
#    gray = EscalaGrises(rgb)
#    gray = np.reshape(gray[:,:,0],(width*height,1))
#    
    cumHistogram = np.zeros(256)
#    
#    for i in range(width*height):
#        aux = gray[i,0]
#        histogram[aux] = histogram[aux] + 1
       
    h = np.histogram(yiq[:,0],bins,range=(0,1))
    
    histogram = h[0]
    
    cumHistogram[0] = histogram[0]
    
    for i in range(255):
        cumHistogram[i + 1] = cumHistogram[i] + histogram[i + 1]
        
#    cumHistogram[:] = cumHistogram[:]/cumHistogram[255]
    
    
    return (histogram,cumHistogram)

def normHisto(histogram):
    
    histo = np.zeros(histogram.shape)
    histo = histogram
    
    maximum = histo[0]
    
    for i in range(histogram.__len__() - 1):
        if (maximum < histo[i]):
            maximum = histo[i]
    
    histo = histo/maximum
    
    return histo

def brightenLAT(rgb,Min,Max):
    yiq = np.zeros(rgb.shape)
    
    yiq = RGB2YIQ(rgb)
    
    width,height,depth = rgb.shape

    yiq = np.reshape(yiq,(width*height,depth))

    for i in range(width*height):
        if (yiq[i,0] < Min):
            yiq[i,0] = 0
        elif (yiq[i,0] > Max):
            yiq[i,0] = 1
        else:
            yiq[i,0] = (yiq[i,0] - Min)/(Max - Min)
            
    yiq = np.reshape(yiq,(width,height,depth))
    
    rgbOut = YIQ2RGB(yiq)
    
    return rgbOut

def brightenCM(rgb,cumHisto):
    yiq = np.zeros(rgb.shape)
    
    yiq = RGB2YIQ(rgb)
    
    width,height,depth = rgb.shape

    yiq = np.reshape(yiq,(width*height,depth))
    
#    for i in range(width*height):
#        if ((yiq[i,0] != 0) and (yiq[i,0] != 1)):
#            
#            left = np.uint8(yiq[i,0]*255) - 1
#            right = np.uint8(yiq[i,0]*255) + 1
#            leftOut = cumHisto[(np.uint8(yiq[i,0]*255) - 1)]
#            rightOut = cumHisto[(np.uint8(yiq[i,0]*255) + 1)]
##            yiq[i,0] = (yiq[i,0] - np.uint8(yiq[i,0]*255) + 1)*(cumHisto[np.uint8(yiq[i,0]*255) + 1] - cumHisto[np.uint8(yiq[i,0]*255) - 1])/2 + cumHisto[np.uint8(yiq[i,0]*255) - 1]
#            yiq[i,0] = (yiq[i,0] - left)*(rightOut - leftOut)/(right - left) + leftOut

    for i in range(width*height):
        yiq[i,0] = cumHisto[np.uint8(yiq[i,0]*255)]
   
    yiq = np.reshape(yiq,(width,height,depth))
    
    rgbOut = YIQ2RGB(yiq)
    
    return rgbOut

def gaussHisto(histogram,mean,sigma):
    gauss = np.zeros(histo.__len__())
    
    for i in range(histo.__len__()):
        gauss[i] = mlab.normpdf(i/255,mean,sigma)
    
    gaussCum = np.zeros(256)
    
    gaussCum[0] = gauss[0]
    
    for i in range(255):
        gaussCum[i + 1] = gaussCum[i] + gauss[i + 1]
        
    gauss = normHisto(gauss)
    gaussCum = normHisto(gaussCum)
    
    return (gauss,gaussCum)
    

hola = misc.imread('lena512.png')

plt.figure(0)
plt.imshow(hola)

plt.figure(1)
plt.imshow(EscalaGrises(hola))

histo,cumHisto = histogram(hola)

histo = normHisto(histo)

gauss,gaussCum = gaussHisto(histo,80/255,0.4)

plt.figure(2)
plt.plot(histo)
plt.plot(gauss)

cumHisto = normHisto(cumHisto)

plt.figure(3)
plt.plot(cumHisto)
plt.plot(gaussCum)

plt.figure(4)
plt.imshow(brightenLAT(hola,0.2,0.85))

plt.figure(5)
plt.imshow(brightenCM(hola,gaussCum))
