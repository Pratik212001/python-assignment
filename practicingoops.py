# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:51:04 2025

@author: PRATIK MINDE
"""

class student:
    rollno=None
    name=None
    std=None
    division=None
    sem1=None
    sem2=None
    average=None
    
    
    def __init__(self,rollno,name,std,division,sem1,sem2):
        self.rollno=rollno
        self.name=name
        self.std=std
        self.division=division
        self.sem1=sem1
        self.sem2=sem2
        
    def calculate (self):
        self.average=(self.sem1+self.sem2)/2
        
    def display(self):
        print(self.rollno,'',self.name,'',self.std,'',self.division,'',self.sem1,'',self.sem2,'',self.average,'')
        
student1=student(24,"pratik",6,"c",78,94)
student1.calculate()
student1.display()
        
        
        
        
        