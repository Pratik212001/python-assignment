# -*- coding: utf-8 -*-
"""
Created on Wed May 28 11:30:35 2025

@author: PRATIK MINDE
"""

a=5
b=5
m=[1,2,3,4,5,6,7]
try:
    c=a/b

except ZeroDivisionError as e:
    print(e)
    
else:
    print(c)
    
try:
    print(m[2])
except IndexError as e:
    print(e)
    
else:
    print(m[3])
    
