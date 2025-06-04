# -*- coding: utf-8 -*-
"""
Created on Wed May 21 11:22:08 2025

@author: PRATIK MINDE
"""

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


now=datetime.now()

print(now)
today=datetime.today()

yest=today-timedelta(days=20)
print(yest)



print(now.strftime("%y"))





print(yest.strftime(("%p")))
