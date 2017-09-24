# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:53:08 2017

@author: Juanig
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
from some_functions import YIQ

def pascal_level(n):         #creates the nth level of pascal's triangle and returns a string (useless)

    c = 1
    s = ''
    for i in range(1,n+1):
        s = s +' '+ str(c) 
        c = c*(n-i)//i
    return s


def gaussian_kernel(n):     #creates a n x n gaussian filter kernel 
    one_d = np.zeros([n])
    c = 1
    for i in range(1,n+1):  #fills 1d array
        one_d[i-1] = c
        c = c*(n-i)//i

    result = np.outer(one_d, one_d) #outer product, resulting in nxn array
    
    s = 0                           #takes the average
    for i in range(n):
        for j in range(n):
            s = s + result[i,j]
            
    result = result/s
    return result

    

def bartlett_kernel(n):            #creates a n x n bartlett filter kernel
    one_d = np.zeros([n])
    one_d[0] = 1
    for i in range(1,n):
        if i <= ((n//2)) :
            one_d[i] = one_d[i-1] + 1
        else:
            one_d[i] = one_d[i-1] - 1
            
    result = np.outer(one_d, one_d)
    s = 0
    for i in range(n):
        for j in range(n):
            s = s + result[i,j]
            
    result = result/s
    return result

#laplacian and identity kernel as "constants"
laplacian_v4 = np.array( [[0,-1,0],[-1,4,-1],[0,-1,0]] )
laplacian_v8 = np.array( [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]] )
identity_3x3 = np.array( [[0,0,0],[0,1,0],[0,0,0]] )


def matrix_convolution (a,b) :      #convolution between two matrices, image handling requires additional considerations

    wa,ha = a.shape
    wb, hb = b.shape
    
    result = np.zeros([wa,ha])
    
    for i in range(wa):
        for j in range(ha):          
            for x in range(wb):
                for y in range(hb):
                    #index of matrix a 
                    ix = i - wb//2 + x
                    jy = j - hb//2 + y
                    
                    if ix < 0 :
                        ix = 0
                    elif ix >= wa:
                        ix = wa - 1
                    
                    if jy < 0 :
                        jy = 0
                    elif jy >= ha:
                        jy = ha - 1
                        
                    result[i,j] = result[i,j] + a[ix,jy]*b[x,y]
                    
    return result

  



#open image
img_name = 'city.png'
img = misc.imread(img_name)

#set kernel
b = laplacian_v8*0.1 + identity_3x3
#b = gaussian_kernel(5)  
#b = bartlett_kernel(3)

#separate y channel
img_yiq = YIQ(img/255)
img_y = np.uint8( np.round( img_yiq[:,:,0].copy() * 255 ))
width, height = img_y.shape

#convolution
b_img_y = matrix_convolution(img_y,b)

#clamp
for i in range(width):                                  
    for j in range(height):
        b_img_y[i,j] =  min(255 ,max(b_img_y[i,j], 0))

#cast
b_img_y = np.uint8( np.round( b_img_y ))


#save
plt.imsave('img_original.png', img_y, cmap = plt.cm.gray)
plt.imsave('img_filtered.png', b_img_y, cmap = plt.cm.gray)

print('ready (: ')


                
                    








