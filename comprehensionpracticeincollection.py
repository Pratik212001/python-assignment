# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:44:28 2025

@author: PRATIK MINDE
"""

a=[1,2,3,4,5,6]

b=list(map(lambda x:x**3,a))


print(b)


c=tuple(filter(lambda x:x%2==0,a))

d=tuple(filter(lambda x:x%2!=0,a))

print(c)

print(d)