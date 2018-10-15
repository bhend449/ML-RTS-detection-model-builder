# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:23:56 2017

@author: Ben WORK ONLY
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 00:51:21 2017

@author: Ben WORK ONLY
"""
#matplotlib.use('Agg')
from keras.models import load_model
import pylab
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

model = load_model('C:/Users/Ben WORK ONLY/PiCam/CNN2_model.h5')

detArray = np.zeros((300,300))


for i in range(1,300):
    print(i)
    for j in range(1,300):
        pix = pixel[0:1500, i, j]
        ppix = pix[None,:,None]
        mp = model.predict(ppix)
        imp = int(mp)
        detArray[i,j]=imp
        #print(i,j,mp[0])
#        if mp[0] == 0:
#            print(i,j,mp[0])
#            x = np.arange(0,1500)
#            plt.plot(x,pix)
#            plt.savefig('C:/Users/Ben WORK ONLY/PiCam/RTS_CNN2demo/%d_%d' % (i,j))
#            plt.plot(x,pix)
#            plt.close()

        
        
        
#x = np.arange(0,500)

#plt.plot(x,p)