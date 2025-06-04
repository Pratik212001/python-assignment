# -*- coding: utf-8 -*-
"""
Created on Mon May 26 11:26:28 2025

@author: PRATIK MINDE
"""

class Book:
    bid=None
    name=None
    author=None
    price=None
    
    
    def setbid(self,bid):
        self.bid=bid
    def getbid(self):
        return self.bid
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setauthor(self,author):
        self.author=author
    def getauthor(self):
        return self.author
    def setprice(self,price):
        self.price=price
    def getprice(self):
        return self.price
    
b1=Book()
b1.setbid(101)
b1.setname('story of my life')
b1.setauthor("helen keller")
b1.setprice(545)

print(b1.getbid())
print(b1.getname())
print(b1.getauthor())
print(b1.getprice())
      
    
    
    
    