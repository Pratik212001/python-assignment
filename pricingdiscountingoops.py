# -*- coding: utf-8 -*-
"""
Created on Fri May 23 11:45:26 2025

@author: PRATIK MINDE
"""

class product:
    code=None
    name=None
    price=None
    discount=None
    actualprice=None
    
    
    def accept(self,code,name,price):
        self.code=code
        self.name=name
        self.price=price
        
        
    def calculate (self):
        if self.price >5000 and self.price<10000:
            self.discount=self.price*0.20
        elif self.price >1000 and self.price<5000:
            self.discount=self.price*0.10
            
        else:
            self.discount=0
            
        self.actualprice=self.price-self.discount
         

           
    def display (self):
        print(self.code,'',self.name,'',self.price,'',self.discount,'',self.actualprice,'')
           
product1=product()
product1.accept(102,'perfume',8000)
product1.calculate()
product1.display()
            
            
        