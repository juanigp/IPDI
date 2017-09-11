# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 11:00:00 2017

@authors:

"""

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def ClampedAddition(rgb1,rgb2):
    rgb1 = rgb1.astype(np.uint16)
    rgb2 = rgb2.astype(np.uint16)
    width,height,depth = rgb1.shape
    rgb1 = np.reshape(rgb1,(width*height,depth))
    rgb2 = np.reshape(rgb2,(width*height,depth))
    
    rgb3 = np.zeros(rgb1.shape)

    rgb3[:,0] = rgb1[:,0] + rgb2[:,0]
    rgb3[:,1] = rgb1[:,1] + rgb2[:,1]
    rgb3[:,2] = rgb1[:,2] + rgb2[:,2] 
    
    for i in range(width*height): 
        if (rgb3[i,0] > 255):
            rgb3[i,0] = 255
        if (rgb3[i,1] > 255):
            rgb3[i,1] = 255
        if (rgb3[i,2] > 255):
            rgb3[i,2] = 255
    
    rgb3 = rgb3.astype(np.uint8)
    
    if depth == 4:
        rgb3[:,3] = rgb1[:,3]
    return np.reshape(rgb3,(width,height,depth))

def AverageAddition(rgb1,rgb2):
    rgb1 = rgb1.astype(np.uint16)
    rgb2 = rgb2.astype(np.uint16)
    width,height,depth = rgb1.shape
    rgb1 = np.reshape(rgb1,(width*height,depth))
    rgb2 = np.reshape(rgb2,(width*height,depth))
    
    rgb3 = np.zeros(rgb1.shape)
    
    rgb3[:,0] = (rgb1[:,0] + rgb2[:,0])/2
    rgb3[:,1] = (rgb1[:,1] + rgb2[:,1])/2
    rgb3[:,2] = (rgb1[:,2] + rgb2[:,2])/2 

    
    rgb3 = rgb3.astype(np.uint8)
    
    if depth == 4:
        rgb3[:,3] = rgb1[:,3]
    return np.reshape(rgb3,(width,height,depth))


def ClampedSubstraction(rgb1,rgb2):
    rgb1 = rgb1.astype(np.int16)
    rgb2 = rgb2.astype(np.int16)
    width,height,depth = rgb1.shape
    rgb1 = np.reshape(rgb1,(width*height,depth))
    rgb2 = np.reshape(rgb2,(width*height,depth))
    
    rgb3 = np.zeros(rgb1.shape)

    rgb3[:,0] = (rgb1[:,0] - rgb2[:,0])
    rgb3[:,1] = (rgb1[:,1] - rgb2[:,1])
    rgb3[:,2] = (rgb1[:,2] - rgb2[:,2])
    
    for i in range(width*height):    
        if (rgb3[i,0] < 0):
            rgb3[i,0] = 0
        if (rgb3[i,1] < 0):
            rgb3[i,1] = 0
        if (rgb3[i,2] < 0):
            rgb3[i,2] = 0
    
    if depth == 4:
        rgb3[:,3] = rgb1[:,3]
    rgb3 = rgb3.astype(np.uint8)
    return np.reshape(rgb3,(width,height,depth))

def AverageSubstraction(rgb1,rgb2):
    rgb1 = rgb1.astype(np.int16)
    rgb2 = rgb2.astype(np.int16)
    width,height,depth = rgb1.shape
    rgb1 = np.reshape(rgb1,(width*height,depth))
    rgb2 = np.reshape(rgb2,(width*height,depth))
    
    rgb3 = np.zeros(rgb1.shape)    

    rgb3[:,0] = (rgb1[:,0] - rgb2[:,0] + 255)/2
    rgb3[:,1] = (rgb1[:,1] - rgb2[:,1] + 255)/2
    rgb3[:,2] = (rgb1[:,2] - rgb2[:,2] + 255)/2        
    
    if depth == 4:
        rgb3[:,3] = rgb1[:,3]
    rgb3 = rgb3.astype(np.uint8)
    return np.reshape(rgb3,(width,height,depth))

def AbsoluteSubstraction(rgb1,rgb2):
    rgb1 = rgb1.astype(np.int16)
    rgb2 = rgb2.astype(np.int16)
    width,height,depth = rgb1.shape
    rgb1 = np.reshape(rgb1,(width*height,depth))
    rgb2 = np.reshape(rgb2,(width*height,depth))
    
    rgb3 = np.zeros(rgb1.shape)
    
    rgb3[:,0] = abs(rgb1[:,0] - rgb2[:,0])
    rgb3[:,1] = abs(rgb1[:,1] - rgb2[:,1])
    rgb3[:,2] = abs(rgb1[:,2] - rgb2[:,2])

    if depth == 4:
        rgb3[:,3] = rgb1[:,3]
    rgb3 = rgb3.astype(np.uint8)
    return np.reshape(rgb3,(width,height,depth))
    
def IfBrighter(rgb1,rgb2):
    rgb1 = rgb1.astype(np.int16)
    rgb2 = rgb2.astype(np.int16)

    width,height,depth = rgb1.shape
    rgb1 = np.reshape(rgb1,(width*height,depth))
    rgb2 = np.reshape(rgb2,(width*height,depth))
    
    rgb3 = np.zeros(rgb1.shape)

    
    for i in range(width*height):
        if rgb1[i,0] >= rgb2[i,0]:
            rgb3[i,0] = rgb1[i,0]
        else:
            rgb3[i,0] = rgb2[i,0]
        if rgb1[i,1] >= rgb2[i,1]:
            rgb3[i,1] = rgb1[i,1]
        else:
            rgb3[i,0] = rgb2[i,1]
        if rgb1[i,2] >= rgb2[i,2]:
            rgb3[i,2] = rgb1[i,2]
        else:
            rgb3[i,0] = rgb2[i,2]

    if depth == 4:
        rgb3[:,3] = rgb1[:,3]
    
    rgb3 = rgb3.astype(np.uint8)
    return np.reshape(rgb3,(width,height,depth))

def IfDarker(rgb1,rgb2):
    rgb1 = rgb1.astype(np.int16)
    rgb2 = rgb2.astype(np.int16)

    width,height,depth = rgb1.shape
    rgb1 = np.reshape(rgb1,(width*height,depth))
    rgb2 = np.reshape(rgb2,(width*height,depth))
    
    rgb3 = np.zeros(rgb1.shape)

    
    for i in range(width*height):
        if rgb1[i,0] <= rgb2[i,0]:
            rgb3[i,0] = rgb1[i,0]
        else:
            rgb3[i,0] = rgb2[i,0]
        if rgb1[i,1] <= rgb2[i,1]:
            rgb3[i,1] = rgb1[i,1]
        else:
            rgb3[i,0] = rgb2[i,1]            
        if rgb1[i,2] <= rgb2[i,2]:
            rgb3[i,2] = rgb1[i,2]
        else:
            rgb3[i,0] = rgb2[i,2]

    if depth == 4:
        rgb3[:,3] = rgb1[:,3]
    
    rgb3 = rgb3.astype(np.uint8)
    return np.reshape(rgb3,(width,height,depth))
