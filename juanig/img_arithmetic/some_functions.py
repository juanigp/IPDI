# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:09:17 2017

@author: Felix Thomsen

1.) fill out the parts with ?

2.) rewrite the functions that they do not contain explicit for-loops using the [:] operator

3.) implement the conversion between RGB and HSV
"""

import numpy as np






# transform entire image from rgb to yiq
def YIQ(rgb):
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
     
    #::::::::::::::::::::::::::::::
    return np.reshape(rgb,(width,height,depth))


def brighten(yiq,a):
    yiq[:,:,0] = a*yiq[:,:,0]
    return yiq



############## cuasi sumas y restas ###############

def RGB_sum(img1, img2, frmat):
    img1 = np.uint16(np.round(img1))
    img2 = np.uint16(np.round(img2))
    width, height, depth = img1.shape
    
    out = np.zeros(img1.shape)
  
    if (frmat == 'clamped'):   
        for i in range(width):
            for j in range(height):
                for k in range(3):
                    out[i,j,k] = img1[i,j,k] + img2[i,j,k]
                    if out[i,j,k] > 255:
                        out[i,j,k] = 255
                    
    elif (frmat == 'average'):
        for i in range(3):
            out[:,:,i] = ( img1[:,:,i] + img2[:,:,i] )/2
            
    if depth == 4:
        out[:,:,3] = 255
    
    out = np.uint8(np.round(out))
    return out


def YIQ_sum(img1, img2):
    img1 = YIQ(img1/255)
    img2 = YIQ(img2/255)
    width, height, depth = img1.shape   
    out = np.zeros(img1.shape)
    

    out[:,:,1] = (img1[:,:,0]*img1[:,:,1] + img2[:,:,0]*img2[:,:,1])/(img1[:,:,0]+img2[:,:,0])
    out[:,:,2] = (img1[:,:,0]*img1[:,:,2] + img2[:,:,0]*img2[:,:,2])/(img1[:,:,0]+img2[:,:,0])   

    out[:,:,0] =  img1[:,:,0] + img2[:,:,0]
    
    for i in range(width):
        for j in range(height):
            if out[i,j,0]>1:
                out[i,j,0] = 1
                
    out = RGB(out)*255
    out = np.uint8(np.round(out))
    
    if depth == 4:
        out[:,:,3] = 255
    return out
    


def RGB_subtraction(img1, img2, frmat):
    img1 = np.int16(np.round(img1))
    img2 = np.int16(np.round(img2))
    width, height, depth = img1.shape
    
    out = np.zeros(img1.shape)
  
    if (frmat == 'clamped'):   
        for i in range(width):
            for j in range(height):
                for k in range(3):
                    out[i,j,k] = img1[i,j,k] - img2[i,j,k]
                    if out[i,j,k] < 0:
                        out[i,j,k] = 0
                    
    elif (frmat == 'average'):
        for i in range(3):
            out[:,:,i] = ( img1[:,:,i] - img2[:,:,i] )/2 + 127 
            
    if depth == 4:
        out[:,:,3] = 255
    
    out = np.uint8(np.round(out))
    return out




def YIQ_subtraction(img1, img2):
    img1 = YIQ(img1/255)
    img2 = YIQ(img2/255)
    width, height, depth = img1.shape   
    out = np.zeros(img1.shape)
    

    out[:,:,1] = (img1[:,:,0]*img1[:,:,1] - img2[:,:,0]*img2[:,:,1])/(img1[:,:,0]+img2[:,:,0])
    out[:,:,2] = (img1[:,:,0]*img1[:,:,2] - img2[:,:,0]*img2[:,:,2])/(img1[:,:,0]+img2[:,:,0])   

    out[:,:,0] =  img1[:,:,0] - img2[:,:,0]
    
    for i in range(width):
        for j in range(height):
            if out[i,j,0]<0:
                out[i,j,0] = 0
                
    out = RGB(out)*255
    out = np.uint8(np.round(out))
    
    if depth == 4:
        out[:,:,3] = 255
    return out
    



def if_darker(img1,img2):
    img1 = YIQ(img1/255)
    img2 = YIQ(img2/255)
    width, height, depth = img1.shape   
    out = np.zeros(img1.shape)  
    
    for i in range(width):
        for j in range(height):
            for k in range(3):
                if img1[i,j,0] < img2[i,j,0]:
                    out[i,j,k] = img1[i,j,k]
                else:
                    out[i,j,k] = img2[i,j,k]
    out = RGB(out)*255
    out = np.uint8(np.round(out))
    
    if depth == 4:
        out[:,:,3] = 255
    return out                   
        
def if_lighter(img1,img2):
    img1 = YIQ(img1/255)
    img2 = YIQ(img2/255)
    width, height, depth = img1.shape   
    out = np.zeros(img1.shape)  
    
    for i in range(width):
        for j in range(height):
            for k in range(3):
                if img1[i,j,0] > img2[i,j,0]:
                    out[i,j,k] = img1[i,j,k]
                else:
                    out[i,j,k] = img2[i,j,k]
    out = RGB(out)*255
    out = np.uint8(np.round(out))
    
    if depth == 4:
        out[:,:,3] = 255
    return out                   
 






       