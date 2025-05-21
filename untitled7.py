# -*- coding: utf-8 -*-
"""
Created on Tue May 20 11:08:58 2025

@author: PRATIK MINDE
"""
# importing regular expressions

import re

text="hello to all"

if re.match(r'^hi',text):
    print("match found")
    
else:
    print("match not found")



x=re.findall(r'\d+','india is 7908 largest country in the world')

print(x)


# replacing space


b=re.sub(r'\s+','=','my name is pratik')

print(b)


# spliting 


c=re.split(r',;','mango,banana;grapes')

print(c)


#searching

m=re.search(r'(\w+)@(\w+)\.(\w+)',)