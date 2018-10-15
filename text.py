# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:52:47 2017

@author: Ben WORK ONLY

There are 2,313 RTS candidates, so add 2,637 WN signals to create np.array(4950,1500)
"""
import matplotlib
matplotlib.use('Agg')
import pylab
import matplotlib.pyplot as plt
import numpy as np
#x_train = np.zeros((4982,1500))
x_train = np.zeros((76500,1500)) #0.85*90000
x_test = np.zeros((13500,1500))  #0.15*90000
tr_count = 0
te_count = 0


fname = open("C:/Users/Ben WORK ONLY/PiCam/RTS_List_train.txt", "r+")
for line in fname:
    fields = line.strip().split()
    if fields:              #only lines that aren't empty
        row = int(fields[0])
        column = int(fields[1])
        x_train[tr_count] = (pixel[0:1500, row, column])
        print(row,column)
        tr_count=tr_count+1        
fname.close()


gname = open("C:/Users/Ben WORK ONLY/PiCam/WN_ListSh_train.txt", "r+")       
for line in gname:
    fields = line.strip().split()
    if fields:              #only lines that aren't empty
        row = int(fields[0])
        column = int(fields[1])
        x_train[tr_count] = (pixel[0:1500, row, column])
        print(row,column)
        tr_count=tr_count+1
gname.close()


np.save('C:/Users/Ben WORK ONLY/PiCam/x_train.npy',x_train)


hname = open("C:/Users/Ben WORK ONLY/PiCam/RTS_List_test.txt", "r+")
for line in hname:
    fields = line.strip().split()
    if fields:              #only lines that aren't empty
        row = int(fields[0])
        column = int(fields[1])
        x_test[te_count] = (pixel[0:1500, row, column])
        print(row,column)
        te_count=te_count+1      
hname.close()



iname = open("C:/Users/Ben WORK ONLY/PiCam/WN_ListSh_test.txt", "r+")        
for line in iname:
    fields = line.strip().split()
    if fields:              #only lines that aren't empty
        row = int(fields[0])
        column = int(fields[1])
        x_test[te_count] = (pixel[0:1500, row, column])
        print(row,column)
        te_count=te_count+1
iname.close()

np.save('C:/Users/Ben WORK ONLY/PiCam/x_test.npy',x_test)