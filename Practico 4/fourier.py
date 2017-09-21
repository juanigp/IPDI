# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:27:03 2017

@author: Bruna Luciano, Payares Natalia & Rodriguez Nicolas

"""
from escalas import RGB2YIQ, YIQ2RGB
import numpy as np
from scipy import misc,fftpack
import matplotlib.pyplot as plt

def EscalaGrises(rgb):
    
    yiq = RGB2YIQ(rgb)
    
    yiq[:,:,1] = 0
    yiq[:,:,2] = 0
    
    rgbOut = YIQ2RGB(yiq)
    
    return rgbOut   
    
def FourierTrans(image):
    
    image = RGB2YIQ(image)
    
    mat = image[:,:,0]#temporal
    width,height = mat.shape
    trans = np.zeros((width,height,2))
    transComp = np.complex_(trans)
    
#    for i in range(height):
#        trans[i,:] = fft(mat[i,:])
#    for i in range(width):
#        trans[:,i] = fft(mat[:,i])
        
    transComp[:,:,0] = fftpack.fft2(mat)
    
    trans[:,:,1] = np.angle(transComp[:,:,0])
    trans[:,:,0] = np.abs(transComp[:,:,0])
    trans[:,:,0] = np.log10(trans[:,:,0] + 1)
    
#    cuad = np.zeros((np.uint8(np.round(width/2)),np.uint8(np.round(height/2))))
    
#    #Referencias en la matriz
#    #   C1  C2
#    #   C3  C4
#    
#    #Copiamos C1 en "cuad"
#    cuad = trans[0:(np.uint8(width//2) - 1),0:(np.uint8(height//2) - 1),0]
#    #Copiamos C4 y pegamos donde estaba C1
#    trans[0:(np.uint8(width//2) - 1),0:(np.uint8(height//2) - 1),0] = trans[(np.uint8(width//2)):(width - 1),(np.uint8(height//2)):(height - 1),0]
#    #Pegamos "cuad" (C1) donde estaba C4
#    trans[(np.uint8(width//2)):(width - 1),(np.uint8(height//2)):(height - 1),0] = cuad
#    
#    #Copiamos C2 en "cuad"
#    cuad = trans[(np.uint8(np.round(width/2))):(width - 1),0:(np.uint8(np.round(height/2)) - 1),0]
#    #Copiamos C3 y pegamos donde estaba C2
#    trans[(np.uint8(np.round(width/2))):(width - 1),0:(np.uint8(np.round(height/2)) - 1),0] = trans[0:(np.uint8(np.round(width/2)) - 1),(np.uint8(np.round(height/2))):(height - 1),0]
#    #Pegamos "cuad" (C2) donde estaba C3
#    trans[0:(np.uint8(np.round(width/2)) - 1),(np.uint8(np.round(height/2))):(height - 1),0] = cuad
#    
#    #La matriz debería quedar
#    #   C4  C3
#    #   C2  C1

    for i in range(width):
        for j in range(height//2):
            aux = trans[(i+width//2)%width, (j+height//2)%height, 0]
            trans[(i+width//2)%width, (j+height//2)%height, 0] = trans[i, j, 0]
            trans[i,j,0] = aux
    
    return trans

def Fourier2RGB(trans):
    
    width,height,deph = trans.shape
    rgb = np.zeros((width,height,4))
    
    minVal = trans[0,0,0]
    maxVal = trans[0,0,0]
    
    for i in range(width):
        for j in range(height):
            minVal = min(minVal,trans[i,j,0])
            maxVal = max(maxVal,trans[i,j,0])
    
    rgb[:,:,0] = (trans[:,:,0] - minVal)*255/(maxVal - minVal)
    rgb[:,:,1] = (trans[:,:,0] - minVal)*255/(maxVal - minVal)
    rgb[:,:,2] = (trans[:,:,0] - minVal)*255/(maxVal - minVal)
    rgb[:,:,3] = 255
    
    rgb = rgb.astype(np.uint8)

    return rgb

def InvFourierTrans(trans):
    
    width,height,deph = trans.shape
    
    image = np.zeros((width,height,4))
    yiq = np.zeros((width,height,4))
    
    for i in range(width):
        for j in range(height//2):
            aux = trans[(i+width//2)%width, (j+height//2)%height, 0]
            trans[(i+width//2)%width, (j+height//2)%height, 0] = trans[i, j, 0]
            trans[i,j,0] = aux
            
    trans[:,:,0] = np.power(10,trans[:,:,0]) - 1
    comp = np.zeros((width,height))
    comp = np.complex_(comp)
    comp[:,:] = trans[:,:,0]*np.exp(1j*trans[:,:,1])
    
    yiq[:,:,0] = np.real(fftpack.ifft2(comp))
    yiq[:,:,3] = 1

    
    image = YIQ2RGB(yiq)
    
    return image


