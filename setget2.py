# -*- coding: utf-8 -*-
"""
Created on Mon May 26 11:50:25 2025

@author: PRATIK MINDE
"""

class Employee:
    
    eid=None
    name=None
    age=None
    experince=None
    
    
   
    def seteid(self,eid):
        self.eid=eid
    def geteid(self):
        return self.eid
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setage(self,age):
        self.age=age
    def getage(self):
        return self.age
    def setexperience(self,experience):
        self.experience=experience
    def getexperience(self):
        return self.experience
    
    
    
    
emp1=Employee()
emp1.seteid(101)
emp1.setname('pratik')
emp1.setage(25)
emp1.setexperience(5)


print(emp1.geteid(),emp1.getname(),emp1.getage(),emp1.getexperience())    