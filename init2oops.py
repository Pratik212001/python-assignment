# -*- coding: utf-8 -*-
"""
Created on Mon May 26 12:07:31 2025

@author: PRATIK MINDE
"""
class Employee:
    
    eid=None
    name=None
    age=None
    experince=None
    def __init__(self,eid,name,age,experience):
        
        self.eid=eid
        self.name=name
        self.age=age
        self.experience=experience
        
        
        
    def display(self):
        print(self.eid,"",self.name,"",self.age,"",self.experience,"")
        
emp1=Employee(101,"pratik",25,5)
emp1.display()