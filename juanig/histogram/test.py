# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:31:45 2017

@author: Juanig
"""

import some_functions as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


name = 'nebula.png'
img = misc.imread(name)
out = sf.piecewise_linear_filter(img, 0.1, 0.8)

plt.figure(0)
plt.imshow(img)

plt.figure(1)
plt.imshow(out)

img_y = sf.YIQ(img)[:,:,0].copy()
width,height = img_y.shape
img_y = np.reshape(img_y,[width*height])


plt.figure(2)
hist, bin_edges = np.histogram(img_y*100, bins = 100)

y_pos = np.arange(len(bin_edges))

plt.bar( y_pos, hist, align='center', alpha=0.5 )
plt.xticks(y_pos, bin_edges)
#plt.xlim(min(bin_edges), max(bin_edges))
plt.show()   