# -*- coding: utf-8 -*-
"""
Created on Tue May 27 13:10:41 2025

@author: PRATIK MINDE
"""

class Students:
    _rollno=None
    _name=None
    _standard=None
    _maths=None
    _science=None
    _english=None
    _avg=None
    
    
    def __init__(self,rollno,name,standard,maths,science,english):
        self._rollno=rollno
        self._name=name
        self._standard=standard
        self._maths=maths
        self._science=science
        self._english=english
        
    def calculate(self):
        self._avg=(self._maths+self._science+self._english)/3
        
    def __str__(self):
        return f"roll no={self._rollno},name={self._name},class={self._standard},avg={self._avg}"
    
    
class Enggstudents(Students):
    __practical=None
    __workshop=None
    def __init__(self,rollno,name,standard,maths,science,english,practical,workshop):
     super().__init__(rollno,name,standard,maths,science,english)
     self.__practical=practical
     self.__workshop=workshop
     
    def calculate(self):
        self._avg=(self._maths+self._science+self._english+self.__practical+self.__workshop)/3
        
    def __str__(self):
        return f"roll no={self._rollno},name={self._name},class={self._standard},avg={self._avg}"
    
    
s1=Students(101, "pratik",8,56,65,80)    
s1.calculate()
print(s1)

engg1=Enggstudents(101, "sham", "first year", 85, 65, 90, 97, 92)
engg1.calculate()
print(engg1)
        