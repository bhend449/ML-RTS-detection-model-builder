# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:13:36 2017
Import matlab arrays and convert them to python format
@author: Ben WORK ONLY
"""

import h5py
import numpy as np

mat = h5py.File('RTSdataChecker.mat')
pixel = mat["RTSdata"]   # Must be called the same as the variable it was saved 
                    # under in Matlab (or however the block was created)
pixel = np.array(pixel)