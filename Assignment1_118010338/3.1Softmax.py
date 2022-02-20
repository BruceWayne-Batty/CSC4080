# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 05:57:34 2022

@author: Coding
"""

import numpy as np

def softmax(x):
    return np.exp(x-np.max(x))/np.sum(np.exp(x-np.max(x)))
def CE(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

Y = softmax(np.array([1,3,5]))
P = np.array([0.1,0.1,0.8])
print("The Result After Softmax is:")
for i in Y:
    print(i,end=' ')


'''
print("\n")
print("And the cross-entrophy is:")
print(CE(Y,P))
'''

