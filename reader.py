# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:52:47 2017

@author: Ben WORK ONLY
"""

import pylab
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,1500)
fname = open("C:/Users/Ben WORK ONLY/PiCam/samp_WN_List.txt", "r+")

for line in fname:
    fields = line.strip().split()
    if fields:              #only lines that aren't empty
        row = int(fields[0])
        column = int(fields[1])
        print(row,column)
        p = pixel[0:1500, row, column]
        plt.plot(x,p)
        plt.savefig('C:/Users/Ben WORK ONLY/PiCam/Plots/%d_%d' % (row,column))
        plt.plot(x,p)
        plt.close()

            
fname.close()
        
        
        
        
#x = np.arange(0,500)

#plt.plot(x,p)