# -*- coding: utf-8 -*-
"""
Created on Fri May 30 11:12:30 2025

@author: PRATIK MINDE
"""

import numpy as np


arr=np.array([[6,5,3],[4,7,2]])

print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.sum(arr))



#axis=0--> vertical calculation


print(np.min(arr,axis=0))
print(np.max(arr,axis=0))
print(np.mean(arr,axis=0))
print(np.sum(arr,axis=0))


#axis=1--> horizontal calculation


print(np.min(arr,axis=1))
print(np.max(arr,axis=1))
print(np.mean(arr,axis=1))
print(np.sum(arr,axis=1))