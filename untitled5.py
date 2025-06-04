# -*- coding: utf-8 -*-
"""
Created on Fri May 30 10:42:12 2025

@author: PRATIK MINDE
"""

import numpy as np


arr=np.array([[1,2,3],[4,5,6]])

print(arr)
print(arr.ndim)
print(arr.shape)


arr1=np.zeros((3,4),dtype="int")
arr1[0][2]=100
print(arr1)

arr2=np.ones((3,4),dtype="int")
print(arr2)


arr3=np.arange(1,12,5)
print(arr3)

a=[1,2,3,4,5,6]


b=2
a1=[]
for i in a:
  if i>b:
      a1+=i
print(a1)