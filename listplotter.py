# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 00:51:21 2017

@author: Ben WORK ONLY
"""
matplotlib.use('Agg')
import pylab
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

for i in range(0,4982):
                t = np.arange(0,1500)
                p = x[i,0:1500]
                plt.plot(t,p)
                plt.savefig('C:/Users/Ben WORK ONLY/PiCam/Plots2/%d' % (i))
                plt.plot(t,p)
                plt.close()
                print(i)
                print(np.std(p))
                
        
        
        
        
#x = np.arange(0,500)

#plt.plot(x,p)