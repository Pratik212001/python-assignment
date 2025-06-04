# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:32:35 2025

@author: PRATIK MINDE
"""

class product:
    name=None
    code=None
    price=None
    

    def __init__(self,name,code,price):
      self.name=name
      self.code=code
      self.price=price
    
    
    def display(self):
      print(self.name,'',self.code,'',self.price,'')
    

p1=product('pencil',1,10)
p1.display()
    
    