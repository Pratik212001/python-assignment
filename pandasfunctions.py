# -*- coding: utf-8 -*-
"""
Created on Sat May 31 14:16:57 2025

@author: PRATIK MINDE
"""


import pandas as pd

ds1=pd.Series([1,2,3,4,5,6])

print(ds1)

print(type(ds1))

ds1.index=list('ABCDEF')

print(ds1)

#using dictionary

ds2=pd.Series({'name':'amol','age':12})

print(ds2)

import numpy as np

ds1=pd.Series([1,1,1,2,2,33,4,4,5])

print(ds1.mode())

print(ds1[2:5:2])


print(ds1.count())
ds1[9]=np.nan
ds1[10]=np.nan
print(ds1)

ds1.dropna(inplace=True)

print(ds1)

print(ds1.mean())
print(ds1.mode())
print(ds1.max())
print(ds1.min())
print(ds1.count())