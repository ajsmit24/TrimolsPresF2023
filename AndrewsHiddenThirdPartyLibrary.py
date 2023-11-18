# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:35:56 2023

@author: smith
"""

import numpy as np
import time
np.random.seed(0)

def function1(i):
    lst=[]
    for j in range(2,i):
        m=function2(j)
        lst.append(m)
    return lst

def function2(a):
    for j in range(a):
        temp=[k**k for k in range(j)]
    return np.random.rand(a, a)

def function3(a):
    return np.linalg.inv(a)

def function4():
    time.sleep(1)


function4()