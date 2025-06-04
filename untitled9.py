# -*- coding: utf-8 -*-
"""
Created on Fri May 23 10:51:56 2025

@author: PRATIK MINDE
"""

class employee:
    eid=None
    name=None
    age=None
    salary=None
    TA=None
    
    
    def accept(self,eid,name,age,salary,TA):
        self.eid=eid
        self.name=name
        self.age=age
        self.salary=salary
        self.TA=TA
        
        
    def display (self):
        print(self.eid,'',self.name,'',self.age,'',self.salary,'',self.TA,'')
        
emp1=employee()
emp1.accept(101,'pratik',24,60000,1800)

emp2=employee()
emp2.accept(102,'sattu',28,50000,1500)

emp1.display()
emp2.display()
        