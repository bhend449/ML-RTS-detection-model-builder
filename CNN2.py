# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 00:32:17 2017

@author: Ben WORK ONLY
"""

from keras.models import Sequential
from keras.layers import Dense, Dropout,Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D, Flatten, LSTM
import numpy as np

x_test = np.load('C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/x_test.npy')
x_train = np.load('C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/x_train.npy')
y_test = np.load('C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/y_test.npy')
y_train = np.load('C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/y_train.npy')
X_train = np.expand_dims(x_train, axis=2) # reshape (569, 30) to (569, 30, 1) 
#Y_train = np.expand_dims(y_train, axis=2) # reshape (569, 30) to (569, 30, 1) 
X_test = np.expand_dims(x_test, axis=2) # reshape (569, 30) to (569, 30, 1) 
#Y_test = np.expand_dims(y_test, axis=2) # reshape (569, 30) to (569, 30, 1) 


model = Sequential()
#model.add(Embedding(512, output_dim=1500))
model.add(Conv1D(32, 12, activation='relu', input_shape=(1500, 1)))
#l1 = model.get_weights()
#model.add(Activation('relu'))
#l2 = model.get_weights()
#model.add(Conv1D(64, 4, activation='relu'))
model.add(MaxPooling1D(3))
#p1 = model.add(MaxPooling1D(3))
model.add(Conv1D(64, 12, activation='relu'))

model.add(MaxPooling1D(3))
model.add(Conv1D(128, 12, activation='relu'))
#model.add(Conv1D(128, 4, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=16, epochs=5)
score = model.evaluate(X_test, y_test, batch_size=16)


#model.save('C:/Users/Ben WORK ONLY/Desktop/GH repos/RTS ML detect beta/CNNlin_model.h5')