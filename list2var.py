# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:45:45 2018

@author: Ben WORK ONLY
"""

import matplotlib
matplotlib.use('Agg')
import pylab
import matplotlib.pyplot as plt
import numpy as np

x_train = np.zeros((72000,1500)) #0.85*90000
x_test = np.zeros((18000,1500))  #0.15*90000
tr_count = 0
te_count = 0

fname = open("C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/RTS_List.txt", "r+")
for line in fname:
    fields = line.strip().split()
    if fields:              #only lines that aren't empty
        row = int(fields[0])
        column = int(fields[1])
        if (row+column)%5==0:
            x_test[te_count] = (pixel[0:1500, row, column])
            print(row,column)
            te_count=te_count+1      
        else:
            x_train[tr_count] = (pixel[0:1500, row, column])
            tr_count = tr_count+1
fname.close()