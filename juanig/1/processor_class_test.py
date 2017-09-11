# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:03:51 2017

@author: Juanig
"""

import numpy as np
from scipy import misc
from some_functions import RGB,YIQ,brighten,RGB_sum,YIQ_interpolated_sum,if_darker, if_lighter



class ImageProcessor:
    def __init__(self):
        self._img1 = np.zeros([512,512,4])
        self._img2 = np.zeros([512,512,4])
        self._img3 = np.zeros([512,512,4])
        pass
    
    @property
    def img1(self):
        return self._img1
    
    @img1.setter
    def img1(self, value):
        self._img1 = value
    
    @img1.deleter
    def img1(self):
        pass
    
    @property
    def img2(self):
        return self._img2
    
    @img2.setter
    def img2(self, value):
        self._img2 = value
    
    @img2.deleter
    def img2(self):
        pass    
    
    @property
    def img3(self):
        return self._img3
    
    @img3.setter
    def img3(self, value):
        self._img3 = value
    
    @img3.deleter
    def img1(self):
        pass    

    def process(self, operation):
        if operation == 'Suma RGB clampeada':
            self._img3 = RGB_sum(self._img1, self._img2,'clamped')
        elif operation == 'Suma RGB promediada':
            pass
        elif operation == 'Suma YIQ clampeada':
            pass
        elif operation == 'If darker':
            pass
        elif operation == 'If lighter':
            pass
        
##############################################################################
 
class Processor:
    def __init__(self):
        self.img1_ = np.zeros([512,512,4])
        self.img2_ = np.zeros([512,512,4])
    
    @property
    def img1(self):
        return self.img1_
    
    @img1.setter
    def img1(self, img):
        self.img1_ = img 
        
    @property
    def img2(self):
        return self.img2_
    
    @img2.setter
    def img2(self, img):
        self.img2_ = img         
  
    
class MainWindow:
    def __init__(self):
        self.img_processor = Processor()    
    
    def load_img(self, img, file):
        img = misc.imread(file)
        return img
    #...
              
    
def load_image(img, file):
    img = misc.imread(file).copy()
    return img    


def change_value(var, value):
    var = value
    return var

x = 3
j = change_value(x,5)
print(x)
 
    
im1 = np.zeros([512,512,4])
window = MainWindow()
load_image(im1, 'lena512.png')
#window.img_processor.img1 = misc.imread('lena512.png')
window.img_processor.img1 = window.load_img( window.img_processor.img1, 'lena512.png' )

print( window.img_processor.img1 )
#print(im1)
    
    
        



        
"""       
img1 = misc.imread('lena512.png')       
sim = foo()
#sim.img = img1                   #this doesnt work
#sim.img = misc.imread('lena512.png')     #this works!
"""


#print(sim.img)



"""
x.img1 = misc.imread('lena512.png')      
print (x.img1)
"""












        