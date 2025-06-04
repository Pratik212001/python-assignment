# -*- coding: utf-8 -*-
"""
Created on Fri May 23 10:39:40 2025

@author: PRATIK MINDE
"""

class student:
    __rollno=None
    __name=None
    __eng=None
    __sci=None
    __maths=None
    __total=None
    __perc=None
    
    
    def accept(self,__rollno,__name,__eng,__sci,__maths):
        self.rollno=__rollno
        self.name=__name
        self.eng=__eng
        self.sci=__sci
        self.maths=__maths
        
    def calculate(self):
        self.total=self.eng+self.sci+self.maths
        self.perc=self.total/3
        
        
    def display(self):
        print(self.rollno,'',self.name,'',self.eng,'',self.sci,'',self.maths,'',self.total,'',self.perc,'')
        
        
        
stud1=student()
stud1.accept(1,"pratik",96,98,98)
stud1.calculate()
stud1.display()
stud2=student()
stud2.accept(2,"sattu",98,98,97)
stud2.calculate()
stud2.display()


