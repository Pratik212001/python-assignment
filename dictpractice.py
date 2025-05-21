# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:29:02 2025

@author: PRATIK MINDE
"""

a={}

print(type(a))


my_dict={"name":"pratik","age":25,"address":"yedgaon"}


print(my_dict)


my_dict["age"]=30


print(my_dict)



print(my_dict.get("name","not found"))

print(my_dict.get("age","not found"))

del my_dict["address"]


for key,value in my_dict.items():
    print("key=",key,"value=",value )
    
for k in my_dict.key():
    print(k)
    
for v in my_dict.key():
    print(v)

print(my_dict)
