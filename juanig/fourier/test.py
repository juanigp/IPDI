# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:01:18 2017

@author: Juanig
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
from some_functions import YIQ

"""
a = np.zeros([100])


for i in range(100):
    a[i] = np.cos( (i)/10 )

plt.plot(a)    
f = np.fft.fft( a )
#a[:] = f[:].real

plt.plot(f)

"""




"""
#a = [0,1,0]
N = 100
a = np.zeros([N])
for i in range(100):
    a[i] = np.sin( (2*np.pi*i*30)/N )

A = np.fft.fft(a)
A_mag = np.zeros([A.size])
A_ang = A_mag.copy()
A_mag[:] = abs(A[:]) 
A_ang[:] = np.angle(A[:])

plt.figure(0)
plt.plot(a)
plt.figure(1)
plt.plot(A_mag)
plt.figure(2)
plt.plot(A_ang)

"""

img_name = 'stp1.png'
img = misc.imread(img_name)
img_YIQ = YIQ(img/255)
Y_array =  np.uint8( np.round( img_YIQ[:,:,0].copy() * 255 ))  #arreglo bidimensional de luminancias

width, height = Y_array.shape

dft_array = np.zeros([width,height]) #arreglo de complejos
mag_array = dft_array.copy()         #arreglo de modulos
ang_array = dft_array.copy()         #arreglo de fase

dft_array = np.complex_(dft_array)

#transformada de filas
for i in range(height):
    dft_array[:,i] = np.fft.fft(Y_array[:,i])  

#transformada de columnas
for i in range (width):
    dft_array[i,:] = np.fft.fft(dft_array[i,:])

#modulo y fase
mag_array[:,:] = abs(dft_array[:,:])
ang_array[:,:] = np.angle(dft_array[:,:])


#logartimo
#mag_array[:,:] = np.log10(mag_array[:,:]+1)   # +1 ya que log(0) = 0

#hallo minimo y maximo
min_ = mag_array[0,0]
max_ = mag_array[0,0]
for i in range(width):
    for j in range(height):
        if mag_array[i,j] > max_:
            max_ = mag_array[i,j]
        if mag_array[i,j]<min_:
            min_ = mag_array[i,j]
            
#interpolacion lineal
mag_array[:,:] = mag_array[:,:] * 255/(max_ - min_) - min_ * 255/(max_ - min_)


#traslacion        
for i in range(width):
    for j in range(height//2):
        aux = mag_array[(i+width//2)%width, (j+height//2)%height ]
        mag_array[(i+width//2)%width, (j+height//2)%height ] = mag_array[i, j]
        mag_array[i,j] = aux

"""
aux = mag_array.copy()
for i in range(width):
    for j in range(height):
        mag_array[(i+width//2)%width, (j+height//2)%height ] = aux[i,j].copy()
"""

#imagen en escala de grises
img_dft = np.zeros([width,height,3])
img_dft[:,:,0] = mag_array.copy()
img_dft[:,:,1] = mag_array.copy()
img_dft[:,:,2] = mag_array.copy() 
img_dft = np.uint8( np.round( img_dft )*50 )


        



"""
#imagen original en blanco y negro
img_Y = np.zeros([width,height,3])
img_Y[:,:,0] = Y_array.copy()
img_Y[:,:,1] = Y_array.copy()
img_Y[:,:,2] = Y_array.copy() 
img_Y = np.uint8( np.round(img_Y ) )
"""

plt.figure(3)
plt.imshow(img_dft)
